Close

Menu

  * [About Us](https://blog.sigmaprime.io/pages/about-us.html)

[![Blog Logo](./imgs/blog/sigp-logo-black.png)](https://blog.sigmaprime.io/)
__Menu

# Beacon Fuzz - Update #07

[Mehdi Zerouali](https://blog.sigmaprime.io/author/mehdi-zerouali.html) | Wed
19 August 2020 Estimated read time: 5 min Image credits: [Photo by Hans-Peter
Gauster](https://unsplash.com/@sloppyperfectionist)

_Beacon Fuzz - Progress Update #7: Structural Differential Fuzzing_

# Beacon Fuzz - Update #07  
  

Sigma Prime is leading the development and maintenance of [beacon-
fuzz](https://github.com/sigp/beacon-fuzz), a differential fuzzing solution
for Eth2 clients. This post is part of our series of status updates where we
discuss current progress, interesting challenges encountered and direction for
future work. See [#00](https://blog.sigmaprime.io/beacon-fuzz.html) and the
repository's [README](https://github.com/sigp/beacon-
fuzz/blob/master/README.md) for more context.

## Summary

  * Community Fuzzing Debrief
  * Latest Bugs Identified
  * Structural Differential Fuzzing with `beaconfuzz_v2`
  * Next Steps

## Community Fuzzing Debrief

In our [previous update](https://blog.sigmaprime.io/beacon-fuzz-06.html), we
announced our community fuzzing or _"fuzzing at home"_ initiative, which
allows anyone to contribute to the security of eth2 by running our `eth2fuzz`
tool from their laptops/desktops/cloud infrastructure, using `Docker`.

We were very pleased with the response received from the community! Thanks to
everyone who joined our fuzzing [Discord channel](https://discord.gg/AkPb4vx)
and tried our _Dockerised_ fuzzing framework.

Congratulations to [@Butta](https://github.com/Buttaa),
[@cooganb](https://github.com/cooganb), [@Daft-
Wullie](https://github.com/Daft-Wullie) and
[@MysticRyuujin](https://github.com/MysticRyuujin) for identifying 4 unique
bugs!

We've realised that a lot of community members were attempting to run
`eth2fuzz` on Windows machines. While the _dockerisation_ process was meant to
ensure maximum interoperability between different operating systems, we
realised that some of our settings were hardcoded for Linux support only. This
was quickly fixed by the team and [other
improvements](https://github.com/sigp/beacon-
fuzz/commit/7317c1ecd6d151070140d8e4206b3e2ca7f42fdd) were added based on user
feedback.

## Latest Bugs Identified With `ethfuzz`

The community fuzzing initiative lead to the identification of the following
bugs across three Eth2 implementations:

### Lodestar

  * Memory exhaustion/OOM when parsing invalid `ENR` string (refer to [this issue](https://github.com/ChainSafe/discv5/issues/64) for more details);
  * `AssertionError` in `bcrypto` library (refer to [this issue](https://github.com/ChainSafe/discv5/issues/70) for more details);
  * Failed `val->IsArrayBufferView` assertion when parsing invalid `ENR` string (refer to [this issue](https://github.com/ChainSafe/discv5/issues/71) for more details).

### Nimbus

  * Overflow/underflow in `ProposerSlashing` processing (refer to [this issue](https://github.com/status-im/nim-beacon-chain/issues/1323) for more details).

### Teku

  * Lack of checks of validator indices in Attester Slashings (`ArrayIndexOutOfBoundsException` in `AttesterSlashing` processing, refer to [this issue](https://github.com/PegaSysEng/teku/issues/2345) for more details).

## Differential Fuzzing

Over the last few weeks, we've been focussing our efforts on the differential
fuzzing part of the project, i.e. `beaconfuzz_v2`, in order to identify
potential discrepancies between clients that could lead to consensus splits
(forks) on the eth2 network. Our previous attempt at performing differential
fuzzing across eth2 implementations was carried using a C++ based fuzzer,
inherited from Guido Vranken's
[eth2.0-fuzzing](https://github.com/guidovranken/eth2.0-fuzzing) and extended
to support more eth2 implementations and target all state transition
functions.

`beaconfuzz_v2` has been written from scratch using Rust (the language we're
most comfortable with at Sigma Prime) and the related [Pull
Request](https://github.com/sigp/beacon-fuzz/pull/55) has now been merged into
`master`!

This allows us to perform structure-aware/grammar-based differential fuzzing
on different eth2 clients. We currently support Lighthouse, Prysm and Nimbus.
`beaconfuzz_v2` has been developed in a modular approach, and we look forward
to adding support for other eth2 implementations in the coming days.

`beaconfuzz_v2` currently leverages two fuzzing engines:
[libfuzzer](https://llvm.org/docs/LibFuzzer.html) and
[honggfuzz](https://github.com/google/honggfuzz).

Considering the complexity of this fuzzing framework (each fuzzer needs to
instantiate _goroutines_ for Prysm and their related garbage collectors),
we're reaching a decent fuzzing speed as can be seen in the screenshots below
_(Lenovo laptop, 8x Intel i7-8550U CPU @ 1.80GHz, 16GB of RAM)_ :

![coverage](./imgs/beacon-fuzz/hongfuzz.svg)

_Honggfuzz exercising the process voluntary_exit functions on Lighthouse,
Prysm and Nimbus_

![coverage](./imgs/beacon-fuzz/libFuzzer.svg)

_libFuzzer exercising the process deposit functions on Lighthouse, Prysm and
Nimbus_

### Structural Awareness

As explained in a [previous update](https://blog.sigmaprime.io/beacon-
fuzz-04.html), structural fuzzing, or grammar-based fuzzing, is a technique
instructing fuzzing engines to generate inputs based on a particular set of
rules. By default, coverage-guided mutation based fuzzers such as AFL or
Honggfuzz do not provide any input grammar, which can result in inefficient
fuzzing for complicated input types (such as the ones we use in eth2), where
any traditional mutation (e.g. bit flipping, bit XORing) is exceedingly
unlikely to produce a valid input (in our case invalid SSZ containers).

By leveraging the latest update to the `libfuzzer-sys` and `cargo_fuzz`
crates, `beaconfuzz_v2` defines fuzz targets that take well-formed instances
of custom types by deriving and implementing the `Arbitrary` trait, which
allows us to create structured inputs from raw byte buffers. This has been
incorporated into Beacon Fuzz via this [Pull
Request](https://github.com/sigp/beacon-fuzz/pull/55).

`beaconfuzz_v2` provides two different types of fuzzers:

  * `HonggFuzz` targets: Standard differential mutation fuzzing, using the standard mutation algorithms from HonggFuzz. Useful for detecting differences between clients when processing malformed/invalid consensus objects (e.g. `fuzz_attestation`, `fuzz_proposer_slashing`, `fuzz_voluntary_exit`, etc.);
  * `libFuzzer` targets (targets names ending with `-struct`): Structural differential fuzzing leveraging the work described above to produce valid consensus objects (e.g. `fuzz_attestation-struct`, `fuzz_proposer_slashing-struct`, `fuzz_voluntary_exit-struct`, etc.).

### Identifying Our First Discrepancy

While running our fuzzers, we've identified a discrepancy affecting Prysm when
handling an invalid `SignedVoluntaryExit` which looks like the following:

    
    
    {
      Message:
          {
            Epoch:
                0,
            ValidatorIndex:
                0
          },
      Signature:
          0x000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    }
    

_Note: BLS signature verification is disabled on all targets to speed up
fuzzing execution and exercise different code_

While Lighthouse and Nimbus both rejected this consensus object when calling
their `process_exit` functions, Prysm seemed to accept it and produced a
post-`BeaconState` as a result of the state transition.

Our fuzzers are calling the `ProcessVoluntaryExitsNoVerify` on Prysm, which we
thought only disabled BLS signature verification. It turned out that this
function also skips the spec checks on `VoluntaryExit`s! Compare
[`ProcessVoluntaryExitsNoVerify`](https://github.com/prysmaticlabs/prysm/blob/ec800bac7c4982a921a3f3bf8880e10e52fef22d/beacon-
chain/core/blocks/exit.go#L64-L83) with the function actually used in
production
([`VerifyExit`](https://github.com/prysmaticlabs/prysm/blob/ec800bac7c4982a921a3f3bf8880e10e52fef22d/beacon-
chain/core/blocks/exit.go#L104-L139)) for details.

This allowed us to confirm that our differential fuzzing was indeed working!
Thanks [Nishant](https://github.com/nisdas) for quickly fixing this issue in
[this Pull Request](https://github.com/prysmaticlabs/prysm/pull/6986).

### First Consensus Bug Identified with `beaconfuzz_v2`

Our fuzzing effort lead to the identification of another discrepancy affecting
Prysm on `Attestation` processing.

Similarly to the `VoluntaryExit` fuzzing, we are targeting the
`ProcessAttestationNoVerify` function when calling the Prysm FFI. This
function is also missing spec checks, particularly verifying that the
attesting indices are non-empty. This check is performed using the
[`isValidAttestationIndices`](https://github.com/prysmaticlabs/prysm/blob/fd80f7328695f2f3b110d8b073f51addadce528b/shared/attestationutil/attestation_utils.go#L152)
function and appeared to be missing in Prysm's attestation batch verification
([`VerifyAttestations`](https://github.com/prysmaticlabs/prysm/blob/366e53c41652fb61917da7c4d9ddd67eb9b0fd02/beacon-
chain/core/blocks/attestation.go#L261) in
[`ProcessOperations`](https://github.com/prysmaticlabs/prysm/blob/7f741e48e0b6e2904f6fd9b1a75f6b56529635d3/beacon-
chain/core/state/transition.go#L586) does not call
`isValidAttestationIndices`).

This bug, if exploited in the wild, could have caused a network split. Thanks
to [Protolambda](https://github.com/protolambda) for helping us debug this
issue and kudos to the Prysmatic Labs team for providing a quick fix in [this
Pull Request](https://github.com/prysmaticlabs/prysm/pull/6983).

## Next Steps

Over the next few weeks, the Beacon Fuzz team will be looking into:

  * Finalising the integration of Teku into `beaconfuzz_v2`
  * Running `beaconfuzz_v2` on a dedicated fuzzing infrastructure
  * Start attacking the P2P networking stack of Eth2 clients

[ __Twitter ](https://twitter.com/share?text=Beacon Fuzz - Update
#07&url=https://blog.sigmaprime.io/beacon-fuzz-07.html) [ __Facebook
](https://www.facebook.com/sharer/sharer.php?u=https://blog.sigmaprime.io/beacon-
fuzz-07.html) [ __Google+
](https://plus.google.com/share?url=https://blog.sigmaprime.io/beacon-
fuzz-07.html)

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

