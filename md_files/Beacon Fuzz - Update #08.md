Close

Menu

  * [About Us](https://blog.sigmaprime.io/pages/about-us.html)

[![Blog Logo](./imgs/blog/sigp-logo-black.png)](https://blog.sigmaprime.io/)
__Menu

# Beacon Fuzz - Update #08

[Mehdi Zerouali](https://blog.sigmaprime.io/author/mehdi-zerouali.html) | Thu
01 October 2020 Estimated read time: 9 min Image credits: [Photo by Eric
Prouzet](https://unsplash.com/@eprouzet)

_Beacon Fuzz - Progress Update #8:_  
  
_Cloud fuzzing infrastructure, Teku integration,  
BLS fuzzing, and slashing processing discrepancies._

# Beacon Fuzz - Update #08  
  

Sigma Prime is leading the development and maintenance of [beacon-
fuzz](https://github.com/sigp/beacon-fuzz), a differential fuzzing solution
for Eth2 clients. This post is part of our series of status updates where we
discuss current progress, interesting challenges encountered and direction for
future work. See [#00](https://blog.sigmaprime.io/beacon-fuzz.html) and the
repository's [README](https://github.com/sigp/beacon-
fuzz/blob/master/README.md) for more context.

## Summary

  * Slashing Processing Discrepancies
  * BLS Differential Fuzzing
  * Cloud Fuzzing Infrastructure
  * Teku Integration
  * Plans for a Custom Fuzzing Engine

## Discrepancies in Differential Fuzzing

While no directly exploitable bug was identified over the last few weeks with
`beaconfuzz_v2`, our structural differential fuzzer has been performing quite
well and uncovering some minor differences between implementations that we've
investigated. This section describes two of these discrepancies.

### Difference in Proposer Slashing Processing

_Refer to[this issue](https://github.com/sigp/beacon-fuzz/issues/74) for
context and more detailed information._

The target `fuzz_proposer_slashing-struct` (structural differential fuzzer
exercising the `ProposerSlashing` processing functions as part of
`beaconfuzz_v2`) raised a difference between Lighthouse and Nimbus on one
hand, and Prysm on the other, triggered with the following `ProposerSlashing`
object:

    
    
    ProposerSlashing {
        signed_header_1: SignedBeaconBlockHeader {
            message: BeaconBlockHeader {
                slot: Slot(74),
                proposer_index: 0,
                parent_root: 0x000000000000002f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f,
                state_root: 0x2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f,
                body_root: 0x2f2f2f2f2f0000000a000000000000000000000100000000000075757514bbbb,
            },
            signature: 0xa1baa9d1823b4965b4e4584a12b453c89b88b47b0c7aed40a2cf2d5f094f09dbe15400024eac0000460175757515111005b43e5428b6e7fead6e6a0428ee4672
        },
        signed_header_2: SignedBeaconBlockHeader {
            message: BeaconBlockHeader {
                slot: Slot(74),
                proposer_index: 0,
                parent_root: 0x000000000000002f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f,
                state_root: 0x2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f2f,
                body_root: 0x2f2f2f2f2f0000000a000000000000000000000100000000000075757514bbbb,
            },
            signature: 0xa1baa9d1823b4965b4e4584a12b453c89b88b47b0c7aed4098cf2d5f094f09dbe15e00014eac00004601000000005655000000000075757500000014bbbbbbbb
        },
    }
    

Investigation of how clients handle this particular part of the state
transition revealed that Prysm implements the `process_proposer_slashing`
function slightly differently from Lighthouse and Nimbus. Let's take a look at
how this particular function is defined in the [eth2
spec](https://github.com/ethereum/eth2.0-specs/blob/dev/specs/phase0/beacon-
chain.md#proposer-slashings):

    
    
    def process_proposer_slashing(state: BeaconState, proposer_slashing: ProposerSlashing) -> None:
        header_1 = proposer_slashing.signed_header_1.message
        header_2 = proposer_slashing.signed_header_2.message
    
        # Verify header slots match
        assert header_1.slot == header_2.slot
        # Verify header proposer indices match
        assert header_1.proposer_index == header_2.proposer_index
        # Verify the headers are different
        assert header_1 != header_2
        # Verify the proposer is slashable
        proposer = state.validators[header_1.proposer_index]
        assert is_slashable_validator(proposer, get_current_epoch(state))
        # Verify signatures
        for signed_header in (proposer_slashing.signed_header_1, proposer_slashing.signed_header_2):
            domain = get_domain(state, DOMAIN_BEACON_PROPOSER, compute_epoch_at_slot(signed_header.message.slot))
            signing_root = compute_signing_root(signed_header.message, domain)
            assert bls.Verify(proposer.pubkey, signing_root, signed_header.signature)
    
        slash_validator(state, header_1.proposer_index)
    

As we can see, for a proposer slashing to be valid, the two block headers must
be different (`assert header_1 != header_2`). A header is defined as the
message field in a `SignedBeaconBlock` (i.e. a `BeaconBlockHeader`, see
relevant SSZ container definition
[here](https://github.com/ethereum/eth2.0-specs/blob/dev/specs/phase0/beacon-
chain.md#signedbeaconblockheader)).

The `ProposerSlashing` object produced by the structural differential fuzzer
has two same headers, with different BLS signatures. After going through the
[Prysm
codebase](https://github.com/prysmaticlabs/prysm/blob/b0917db4c79d9ec9c06884539697eb96138b5240/beacon-
chain/core/blocks/proposer_slashing.go#L67-L101), we can notice that when
processing a `ProposerSlashing`, The Prysm client compares the
`SignedBeaconBlockHeader` instead of the `BeaconBlockHeader`:

    
    
    ...
    if proto.Equal(slashing.Header_1, slashing.Header_2) {
      return errors.New("expected slashing headers to differ")
    }
    ...
    

As a result, this particular `ProposerSlashing` is deemed valid by Prysm
because the BLS signature verification is disabled on beacon-fuzz for coverage
optimisation and fuzzing speed purposes (i.e. every BLS signature check always
returns `true`), while Lighthouse and Nimbus rejects it since they perform the
spec check mentioned above (`assert header_1 != header_2`) on the
`BeaconBlockHeaders`.

While this discrepancy is not directly exploitable _per se_ , as it would
require a malicious actor to be able to produce two different, valid BLS
signatures for the same message (`BeaconBlockHeader`), it was quickly
remediated by the Prysmatic Labs crew in this [Pull
Request](https://github.com/prysmaticlabs/prysm/pull/7252).

Additionally, the Eth2 EF research team introduced [additional test
vectors](https://github.com/ethereum/eth2.0-specs/pull/2047#event-3764950810)
to the specs repository to cover this particular scenario.

### Difference in Attester Slashing Processing

_Refer to[this issue](https://github.com/sigp/beacon-fuzz/issues/61) for
context and more detailed information._

The target `fuzz_attester_slashing-struct` (structural differential fuzzer
exercising the `AttesterSlashing` processing functions as part of
`beaconfuzz_v2`) raised a difference between Lighthouse and Prysm on one hand,
and Nimbus on the other, triggered with the following `AttesterSlashing`
object:

    
    
    {
      Attestation1: {
            AttestingIndices:[1],
            Data: {
                Slot: 0,
                Index: 0,
                BeaconBlockRoot: 0x000000000000000000000000000000000000000000000000000000006d000000,
                Source: {
                  Epoch: 0,
                  Root: 0x0000000000000000000000000000000000000000000000000000000000000000
                },
                Target: {
                  Epoch: 2858902030909440,
                  Root: 0x0000000000000000000000000000000000000000000000000000000000000000
                }
            },
            Signature: 0x000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
      },
          Attestation2:
              {
                AttestingIndices:[1, 281474976710658],
                Data: {
                    Slot: 0,
                    Index: 0,
                    BeaconBlockRoot: 0x000000000000000000000000000000000000000000000000000000006d000000,
                    Source: {
                      Epoch: 7143424,
                      Root: 0x0000000000000000000000000000000000000000000000000000000000000000
                    },
                    Target: {
                      Epoch: 0,
                      Root: 0x0000000000000000000000000000000000000000000000000000000000000000
                    }
                },
                Signature: 0x000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
              },
    }
    

As per the [eth2
specification](https://github.com/ethereum/eth2.0-specs/blob/dev/specs/phase0/beacon-
chain.md#attester-slashings):

    
    
    def process_attester_slashing(state: BeaconState, attester_slashing: AttesterSlashing) -> None:
        attestation_1 = attester_slashing.attestation_1
        attestation_2 = attester_slashing.attestation_2
        assert is_slashable_attestation_data(attestation_1.data, attestation_2.data)
        assert is_valid_indexed_attestation(state, attestation_1)
        assert is_valid_indexed_attestation(state, attestation_2)
    
        slashed_any = False
        indices = set(attestation_1.attesting_indices).intersection(attestation_2.attesting_indices)
        for index in sorted(indices):
            if is_slashable_validator(state.validators[index], get_current_epoch(state)):
                slash_validator(state, index)
                slashed_any = True
        assert slashed_any
      ```
    
    The function `is_valid_indexed_attestation` is defined as follows:
    
    ```python
    def is_valid_indexed_attestation(state: BeaconState, indexed_attestation: IndexedAttestation) -> bool:
        """
        Check if ``indexed_attestation`` is not empty, has sorted and unique indices and has a valid aggregate signature.
        """
        # Verify indices are sorted and unique
        indices = indexed_attestation.attesting_indices
        if len(indices) == 0 or not indices == sorted(set(indices)):
            return False
        # Verify aggregate signature
        pubkeys = [state.validators[i].pubkey for i in indices]
        domain = get_domain(state, DOMAIN_BEACON_ATTESTER, indexed_attestation.data.target.epoch)
        signing_root = compute_signing_root(indexed_attestation.data, domain)
        return bls.FastAggregateVerify(pubkeys, signing_root, indexed_attestation.signature)
    

Investigation revealed that Lighthouse and Prysm perform the indexed
attestation validation as part of their signature verification:

  * For [Lighthouse](https://github.com/sigp/lighthouse/blob/c9596fcf0ee3a17bfb1df48e23ed6339c3791457/consensus/state_processing/src/per_block_processing/is_valid_indexed_attestation.rs#L39-L51):

    
    
    if verify_signatures.is_true() {
        verify!(
            indexed_attestation_signature_set(
                state,
                |i| get_pubkey_from_state(state, i),
                &indexed_attestation.signature,
                &indexed_attestation,
                spec
            )?
            .verify(),
            Invalid::BadSignature
        );
    }
    

The closure `|i| get_pubkey_from_state(state, i)` would return an error for
_out-of-range_ attesting indices, however since fuzzing disables BLS
verification, that particular check is not performed (the entire code block is
skipped).

Similarly for Prysm (see snippet
[#1](https://github.com/prysmaticlabs/prysm/blob/de3f112a0500234a27d9cd8b29a60dc26fba6394/beacon-
chain/core/blocks/attester_slashing.go#L79-L103) and
[#2](https://github.com/prysmaticlabs/prysm/blob/3734bfacce3b927c56c83c7acbbf24b4b8a76835/beacon-
chain/core/blocks/attestation.go#L305-L327)), when BLS signatures are
disabled, `PublicKeyFromBytes()` returns an empty BLS signature, regardless of
the attesting indices provided (therefore not checking for _out-of-range_
attesting indices).

As a result, the `AttesterSlashing` object produced by the structural fuzzer
is considered valid by Lighthouse and Prysm, with the associated state
transition resulting in a post-`BeaconState`.

When analysing how Nimbus processes `AttesterSlashing`s (see snippet
[#1](https://github.com/status-im/nim-beacon-
chain/blob/4b38619c4f51847fc591e85327ed226ad46d24ac/beacon_chain/spec/state_transition_block.nim#L193-L224)
and [#2](https://github.com/status-im/nim-beacon-
chain/blob/4b38619c4f51847fc591e85327ed226ad46d24ac/beacon_chain/spec/beaconstate.nim#L442-L447)),
we can see that Nimbus performs an additional check on the attesting indices:

    
    
    let num_validators = state.validators.lenu64
    if anyIt(indexed_attestation.attesting_indices, it >= num_validators):
      return err("indexed attestation: not all indices valid validators")
    

As a result, the `AttesterSlashing` generated by the structural fuzzer is
rejected by Nimbus (since the second attesting index in the second
`IndexedAttestation` causes the check above to fail).

While these discrepancies aren't directly exploitable, they demonstrate the
efficiency of our structural differential fuzzer, highlighting subtle
differences between implementations.

## BLS Differential Fuzzing

We've also written 10 dedicated fuzzers for the following BLS-12-381 libraries
(refer to this [Pull Request](https://github.com/sigp/beacon-fuzz/pull/80):

  * [Milagro BLS](https://github.com/sigp/milagro_bls)
  * [BLST](https://github.com/supranational/blst)
  * [ZKCrypto](https://github.com/zkcrypto/bls12_381) (library used in ZCash)

These fuzzers live in the `bls-fuzz` directory and exercise the serialization
of public keys and signatures, along with elliptic curve additions and
multiplications.

As a result, we've identified the following bugs/discrepancies affecting the
BLST library:

  * [Point Decompression does not handle invalid byte lengths](https://github.com/supranational/blst/issues/14)
  * [Point Decompression does not enforce field points are less than field modulus](https://github.com/supranational/blst/issues/15)

These critical vulnerabilities would have allowed malicious actors to perform
signature malleability attacks (i.e. producing two different signatures for
the same message), with disastrous consequences for Eth2 (think RANDAO
manipulation!).

Additionally, another non-critical discrepancy has been raised, please refer
to [this issue](https://github.com/supranational/blst/issues/16) for further
details.

## Cloud Fuzzing Infrastructure

Over the past few weeks, we've been deploying and running our fuzzers on a
dedicated cloud infrastructure (AWS). We're currently using 16 EC2 instances
running more than 30 fuzzers, including fuzzers targeting the various eth2
networking stacks.

At the moment, we're building, deploying and monitoring these fuzzers
_manually_ , with the help of some simple build scripts. We'll be working on
an automated tooling over the next few weeks, with the help of DevOps experts.

## Teku Integration into `beaconfuzz_v2`

We've been working away at incorporating Teku into the `beaconfuzz_v2`
differential fuzzing. As this is the first client to be integrated with
`beaconfuzz_v2` that is written in an interpreted language, this involves an
additional technical step of running the Java Virtual Machine (JVM) to execute
the Teku bytecode.

The [Java Native Interface
(JNI)](https://docs.oracle.com/en/java/javase/14/docs/specs/jni/intro.html) is
used to invoke and interact with the JVM. As this interface is designed for
use with C or C++, it was not feasible to directly invoke the JNI from Rust.
Instead, we incorporated some small C "glue code" to act as an intermediary.

While much of this "glue code" could be reused from the previous Teku
integration as part of the C++ based `beaconfuzz_v1`, there were some nuances
with regards to converting the C++ code to C and passing the result data
directly to byte buffers managed by Rust (to avoid excessive allocations and
memory use within C).

Refer to [this pull request](https://github.com/sigp/beacon-fuzz/pull/81) for
the Rust & C side of the Teku integration. Though some more polishing and
testing is needed before the PR can be merged, we can successfully execute
Teku attestation processing as part of the existing differential fuzzer.

This integration has also involved some Java-based harness code (to expose
relevant Teku state-transition operations), as well as modifications to Teku
to allow disabling of BLS signature verification (for performance improvements
and consistency with existing fuzzing harnesses). This was completed in Teku
PRs [#1444](https://github.com/PegaSysEng/teku/pull/1444) and
[#2363](https://github.com/PegaSysEng/teku/pull/2363) respectively.

By keeping all Java code in the Teku repository, we can take advantage of the
Teku CI to detect breaking changes that require updates to the fuzzing
harnesses, and it also allows the harnesses to be more easily reused for other
projects.

Much thanks to the Teku team for their assistance with these modifications and
in getting this functionality merged (of particular note was their help
implementing unit tests for the harnesses, structuring the fuzzing harness
project, and integrating it into the build system.)

## Custom Fuzzing Engine

We've also started exploring the possibility of building our own custom
fuzzing engine (as opposed to relying on existing ones such as AFL, libFuzzer
and Honggfuzz).

A custom fuzzing engine would have the following advantages:

  * **Coverage** : Currently, our fuzzing targets use one `BeaconState` per run (selected randomly when these fuzzers initialize). This is due to a constraint in the way libFuzzer and other mutation-based fuzzing engines handle fuzzing inputs: each state transition function takes both a `BeaconState` and a consensus-object (e.g. `Attestation`, `Deposit`, and other SSZ containers). Traditional fuzzing engines only allow to mutate _one_ input (in our case the consensus object as a SSZ container), forcing us to rely on the same `BeaconState` for all fuzzing cycles. By creating our own customized fuzzing engine, we can swap `BeaconState`s periodically (for example, every 1,000 fuzzing cycle)
  * **Speed** : A custom fuzzing engine will also allow us to significantly increase the fuzzing speed by allowing us to load the `BeaconState`s in memory once per fuzzing initialisation (as opposed to loading them from disk for each client implementation exercised). Additionally, better multithreading management will also increase fuzzing speed.
  * **Custom Mutations** : We're planning on using [this Rust library](https://github.com/gamozolabs/basic_mutator) as a base for our mutation algorithms, allowing us to alternate between structural and mutation-based fuzzing within the **same targets**.

## Next Steps

Over the next few weeks, the Beacon Fuzz team will be looking into:

  * Fuzzing the new endpoints developed by the client teams as part of the [weak subjectivity checkpoint](https://notes.ethereum.org/@adiasg/weak-subjectvity-eth2) syncing support;
  * Enhancing the DevOps experience on our cloud fuzzing infrastructure;
  * Potentially performing more BLS differential fuzzing, targeting different bindings.

[ __Twitter ](https://twitter.com/share?text=Beacon Fuzz - Update
#08&url=https://blog.sigmaprime.io/beacon-fuzz-08.html) [ __Facebook
](https://www.facebook.com/sharer/sharer.php?u=https://blog.sigmaprime.io/beacon-
fuzz-08.html) [ __Google+
](https://plus.google.com/share?url=https://blog.sigmaprime.io/beacon-
fuzz-08.html)

[ethereum](https://blog.sigmaprime.io/tag/ethereum.html)[blockchain
security](https://blog.sigmaprime.io/tag/blockchain-
security.html)[fuzzing](https://blog.sigmaprime.io/tag/fuzzing.html)[cybersecurity](https://blog.sigmaprime.io/tag/cybersecurity.html)[differential
fuzzing](https://blog.sigmaprime.io/tag/differential-fuzzing.html)[beacon
chain](https://blog.sigmaprime.io/tag/beacon-chain.html)

![Mehdi Zerouali](https://blog.sigmaprime.io/imgs/authors/mz.jpg)

#### [Mehdi Zerouali](https://blog.sigmaprime.io/author/mehdi-zerouali.html)

Mehdi is a co-founder and a director of Sigma Prime. He is a penetration
tester particularly interested in decentralised systems, with a strong focus
on the Ethereum platform.

__Sydney, Australia

