Close

Menu

  * [About Us](https://blog.sigmaprime.io/pages/about-us.html)

[![Blog Logo](./imgs/blog/sigp-logo-black.png)](https://blog.sigmaprime.io/)
__Menu

# Beacon Fuzz - Update #04

[Mehdi Zerouali](https://blog.sigmaprime.io/author/mehdi-zerouali.html) and
[Nathaniel Jensen](https://blog.sigmaprime.io/author/nathaniel-jensen.html) |
Wed 06 May 2020 Estimated read time: 8 min Image credits: [Photo by Med Badr
Chemmaoui](https://unsplash.com/@medbadrc)

_Beacon Fuzz - Progress Update #4_

# Beacon Fuzz - Update #04  
  
Structural Fuzzing & Architecture Redesign

Sigma Prime is leading the development and maintenance of [beacon-
fuzz](https://github.com/sigp/beacon-fuzz), a differential fuzzing solution
for Eth2 clients. This post is part of our series of status updates where we
discuss current progress, interesting challenges encountered, and direction
for future work. See [#00](https://blog.sigmaprime.io/beacon-fuzz.html) and
the repository's [README](https://github.com/sigp/beacon-
fuzz/blob/master/README.md) for more context.

## Summary

As client teams are ramping up their efforts to match the latest version of
the Eth2 specification (`v0.11.2`), the Beacon Fuzz crew has been pushing hard
to uncover new bugs in these implementations. Key achievements and points of
interest include:

  * Structural Fuzzing using `Arbitrary` Trait
  * First bugs in Teku
  * New bugs in Nimbus
  * Update on Golang integration
  * Challenges in replaying interesting samples across implementations
  * Beacon Fuzz Redesign Proposal

## Structural fuzzing using `Arbitrary` Trait

When using a _naive_ fuzzing strategy, raw bytes are passed to the target
functions, with the expectation that coverage-guided fuzzing engines will
instrument the relevant code and leverage their mutation algorithms to produce
samples that will reach a high number of code blocks.

Some of the types used in Eth2 can be quite complex. For example, let's take a
look at the `BeaconBlockBody` struct:

    
    
    class BeaconBlockBody(Container):
        randao_reveal: BLSSignature
        eth1_data: Eth1Data  # Eth1 data vote
        graffiti: Bytes32  # Arbitrary data
        # Operations
        proposer_slashings: List[ProposerSlashing, MAX_PROPOSER_SLASHINGS]
        attester_slashings: List[AttesterSlashing, MAX_ATTESTER_SLASHINGS]
        attestations: List[Attestation, MAX_ATTESTATIONS]
        deposits: List[Deposit, MAX_DEPOSITS]
        voluntary_exits: List[SignedVoluntaryExit, MAX_VOLUNTARY_EXITS]
    

Each of the complex types forming the `BeaconBlockBody` SSZ container are also
defined in the specification. For example, `Eth1Data` is represented as
follows:

    
    
    class Eth1Data(Container):
        deposit_root: Root
        deposit_count: uint64
        block_hash: Bytes32
    

This means that if we want to efficiently fuzz the state transition functions
that take a `BeaconBlock` as input, we need to provide samples that ideally
follow the structure described above. This is where structural fuzzing (a.k.a
_struct-aware_ or _grammar-based fuzzing_ ) comes in handy.

Previously, we were only making sure that the inputs passed to our state
transition functions were **valid SSZ** containers. This however does not
ensure that the SSZ containers are _relevant_ to the state transition in the
context of the Eth2 specification.

By leveraging the latest update to the `libfuzzer-sys` and `cargo_fuzz`
crates, we're now able to write fuzz targets that take well-formed instances
of custom types by deriving and implementing the `Arbitrary` trait, which
allows us to create structured inputs from raw byte buffers.

Thanks to [this Pull Request](https://github.com/sigp/lighthouse/pull/1040),
we have produced the following new struct-aware fuzzers targeting the
following [epoch state transition
functions](https://github.com/ethereum/eth2.0-specs/blob/dev/specs/phase0/beacon-
chain.md#epoch-processing):

  * `process_rewards_and_penalties()`
  * `process_justification_and_finalization()`
  * `process_slashings()`
  * `process_registry_updates()`
  * `process_final_updates()`

These fuzzing targets live in the `arbitrary-fuzzing-fuzzer` branch of the
[Lighthouse repository](https://github.com/sigp/lighthouse/tree/arbitrary-
fuzzing-fuzzer).

These fuzzers have been running for a few days (at the time of writing) and
have not detected any panics on Lighthouse. We'll be using the generated
samples as new inputs to our differential processor (see section **Beacon Fuzz
Redesign Proposal** ).

## First Bugs in Teku

As mentioned in our [previous update](https://blog.sigmaprime.io/beacon-
fuzz-03.html), we've been working on integrating Teku, the Java Eth2
implementation, to our fuzzing processes.

In doing so, the team has identified the following issues/hardening
opportunities that were quickly addressed by the PegaSys Engineering team:

  * Infinite loop when decoding SSZ `BitList` without _"end-of-list"_ marker bit (see Issue [#1674](https://github.com/PegaSysEng/teku/issues/1674))
  * `IndexOutOfBoundsException` when SSZ decoding 0-byte `Bitlist` (see Issue [#1678](https://github.com/PegaSysEng/teku/issues/1678))

Additionally, issues related to how the `teku transition` subcommand handles
invalid SSZ blocks and `BeaconState`s have also been raised and fixed (see
Issue [#1685](https://github.com/PegaSysEng/teku/issues/1685) and Issue
[#1677](https://github.com/PegaSysEng/teku/issues/1677)).

These last two issues are not _exploitable_ in the normal operation of the
Teku client, as the related exceptions are caught by the client in full
processing and handled gracefully. We'd like to thank [Adrian
Sutton](https://twitter.com/ajsutton) and [Ben
Edgington](https://twitter.com/benjaminion_xyz) for their help in triaging
these bugs!

## New Bugs in Nimbus

By replaying some of the samples generated from fuzzing Lighthouse, a few new
bugs affecting Nimbus have been uncovered:

  * Segmentation fault due to a stack allocation/overflow bug in `process_final_updates` (see Issue [#921](https://github.com/status-im/nim-beacon-chain/issues/921))
  * `AssertionError` in state transition (See Issue [#922](https://github.com/status-im/nim-beacon-chain/issues/922))
  * `IndexError` triggered when parsing an empty `Attestation` SSZ container (See Issue [#931](https://github.com/status-im/nim-beacon-chain/issues/931))
  * `IndexError`s triggered when decoding invalid `BeaconState`s (empty container and variable list reporting 0 length) (See Issue [#896](https://github.com/status-im/nim-beacon-chain/issues/896) and Issue [#920](https://github.com/status-im/nim-beacon-chain/issues/920))

Similarly, the issues affecting the parsing of a malformed `BeaconState` are
not _exploitable_ in the normal operation of the Nimbus client. Kudos to
[Dustin Brody](https://github.com/tersec) from the Nimbus team for fixing
these bugs [so
quickly](https://twitter.com/ethnimbus/status/1250871507624091648?s=20).

## Update on Golang Integration

When updating `beacon-fuzz` to newer spec versions, we encountered new issues
with the existing Golang build process. Our process failed for ZRNT which, as
of `v0.10.1`, had started relying on Herumi's cgo-based [BLS
implementation](https://github.com/herumi/bls-eth-go-binary). Although `go-
fuzz` doesn't support cgo (See [go-fuzz#101](https://github.com/dvyukov/go-
fuzz/issues/101)), it can normally build successfully without attempting cgo
instrumentation.

In this case, the build fails due to a commonly used, but
[unsupported](https://github.com/golang/go/issues/26366) directory structure
in `bls-eth-go-binary` (See
[zrnt#20](https://github.com/protolambda/zrnt/issues/20)).

Although a PR could provide a workaround, there would still remain the
outstanding complications dealing with multiple Golang clients (discussed in
detail in previous posts).

Prysm has started performing standalone fuzzing using the Go Compiler's built-
in coverage instrumentation (experimentally released in
[v1.14](https://golang.org/doc/go1.14#compiler)). Initial experiments have
shown this is a promising way to remove our reliance on a modified `go-fuzz`,
and resolve many complications.

As before, the _"out of the box"_ [go114-fuzz-
build](https://github.com/mdempsky/go114-fuzz-build) tool is insufficient for
our needs but implementing our own build tool is much more simple with the
builtin instrumentation.

Our [go-bfuzz-build](https://github.com/sigp/beacon-
fuzz/tree/to_spec_v0-10-1/files/tools/go-bfuzz-build) tool implements a FFI
interface that returns the bytes needed for differential comparison,
instruments cgo code, and can be easily extended to export interfaces for
multiple clients and harnesses within a single, static
[`c-archive`](https://golang.org/cmd/go/#hdr-Build_modes) library.

This is effectively an implementation of option "D) _Building without go-fuzz_
", as described in our [Beacon Fuzz #01](https://blog.sigmaprime.io/beacon-
fuzz-01.html#buildwithoutgofuzz) post.

With this, we avoid the need for hacky solutions that combine multiple
`c-archive` or `c-shared` libraries (each containing their own Go runtime)
into a single executable.

There are still some outstanding complications with this approach but it is
much more promising with regards to ongoing maintainability and functionality.
Some issues still in development include:

  * **Integrating Prysm's libraries built by Bazel** : A good solution could have been to build the Prysm harnesses with Bazel as a binary-only package then combine with the rest to build a single `c-archive`, but support has been dropped as of [go1.13](https://golang.org/doc/go1.13#go-command). Other possibilities include building the Prysm harness with a `shared` build mode (different to `c-shared`), and linking it.
  * **Programmatically accessing cgo link-time settings** (e.g. [herumi/bls.go#L5-6](https://github.com/herumi/bls-eth-go-binary/blob/6dd0e5634b870d8ae0b2d98130708e25bddcde66/bls/bls.go#L5-L6)). Because the Go build tool does not perform linking when producing a `c-archive`, we need to extract the link-time settings for use with our external linker, so it knows paths to relevant static libraries etc.

## Challenges in Replaying Interesting Samples

We've worked on another tool, `eth2diff`, that allows us to replay interesting
state transitions (i.e. inputting a `BeaconState` along with a `BeaconBlock`)
across different implementations, by leveraging the following utilities
provided by client teams:

  * **Nimbus** : `ncli`
  * **Teku** : `teku transition`
  * **Lighthouse** : `lcli`
  * **Prysm** : `pcli`
  * **ZRNT** : `zcli`

This has allowed us to identify a large portion of the bugs listed above.
However, these utilities do not include some of the checks and verification
steps implemented by Eth2 nodes. Specifically, most of these utilities assume
that the blocks have passed the checks described in the Eth2 [P2P networking
specification](https://github.com/ethereum/eth2.0-specs/blob/dev/specs/phase0/p2p-interface.md#global-
topics) (so are associated with the "current" slot), and states to be provided
are _valid_ i.e. are internally maintained, trusted objects.

This has lead to some confusion and some interesting conversations as captured
in [this issue](https://github.com/prysmaticlabs/prysm/issues/5658).

## Beacon Fuzz redesign proposal

### Challenges

Sigma Prime has been building Beacon Fuzz upon [Guido
Vranken](https://github.com/guidovranken/)'s great work since late 2019. As
the project evolved, the current architecture faces the following challenges:

  * Difficult to evaluate fuzzing coverage;
  * The project is developed in C++, which we don't have extensive experience in;
  * The project is designed to support `libFuzzer` exclusively as a fuzzing engine;

Additionally, we currently _preprocess_ all corpora to combine the SSZ
container input with a referenced `BeaconState`, which are passed as `beacon-
fuzz-testcases` to each client. The conversion from corpus to test case can be
represented as follows:

    
    
    +-------------------+-------------------------+       +-------------------------+-------------------------+
    | state_id (uint16) | Attestation (container) |  -->  | BeaconState (container) | Attestation (container) |
    +-------------------+-------------------------+       +-------------------------+-------------------------+
    

Where `state_id` represents a `BeaconState` integer filename from our
[corpora](https://github.com/sigp/beacon-fuzz-corpora#beaconstates). This
additional serialization step consumes a large amount of time during fuzzing
execution, significantly slowing down the overall process.

### New Architecture

We propose the following architecture for a new, modular version of `Beacon
Fuzz`

#### Design Overview

![coverage](./imgs/beacon-fuzz/diagram.svg)

#### Tool #1 - `eth2fuzz` \- Coverage Guided Fuzzer To Generate Samples

To generate interesting samples, we'll use a dedicated tool leveraging
explicit code coverage, allowing us to _flag_ SSZ containers that are of
interest, i.e. those that trigger new code paths. This tool can use multiple
different fuzzing engines (AFL++, HonggFuzz, libFuzzer, etc.). In fact, we've
already built this tool which lives [here](https://github.com/sigp/beacon-
fuzz/tree/master/eth2fuzz). Next step is to integrate the work done on the
structural fuzzing into `eth2fuzz`.

#### Tool #2 - `eth2diff` \- Replaying Samples Across All Implementations

As mentioned above, we have built a tool that leverages the various state
transition execution utilities (`ncli`, `zcli`, `lci`, etc.) that replays all
samples generated from `eth2fuzz`. We've created dedicated `Docker` containers
for each implementation, and one central `Docker` container to orchestrate the
execution of `eth2diff`. The goal of this tool is to detect crashes and
differences across all supported implementations, for any given set of inputs
(`BeaconState` \+ `BeaconBlock`).

This tool can be found [here](https://github.com/sigp/beacon-
fuzz/tree/master/eth2diff).

#### Tool #3 - `beacon-fuzz-2` \- Differential Fuzzing with FFI Bindings

This tool is the successor of the current existing Beacon Fuzz C++ project. It
will be developed in Rust (for ease of maintainability) and will leverage
Foreign Function Interfaces (FFI) bindings. This will inevitably result in
slower processing and fuzzing (compared to `eth2fuzz`) but should enable the
identification of more complex logic bugs.

## Conclusion

We're very keen to get feedback on our new approach and are quite excited to
continue helping the community ship safe and secure Eth2 clients. We've also
updated the [Trophies](https://github.com/sigp/beacon-fuzz#trophies) section
of Beacon Fuzz, which shows that our fuzzing efforts have helped identify 16
unique bugs/hardening opportunities across 4 implementations.

[ __Twitter ](https://twitter.com/share?text=Beacon Fuzz - Update
#04&url=https://blog.sigmaprime.io/beacon-fuzz-04.html) [ __Facebook
](https://www.facebook.com/sharer/sharer.php?u=https://blog.sigmaprime.io/beacon-
fuzz-04.html) [ __Google+
](https://plus.google.com/share?url=https://blog.sigmaprime.io/beacon-
fuzz-04.html)

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

![Nathaniel Jensen](https://blog.sigmaprime.io/imgs/authors/nat.png)

#### [Nathaniel Jensen](https://blog.sigmaprime.io/author/nathaniel-
jensen.html)

Nat is a Security Engineer at Sigma Prime. A Computer Science graduate with
experience working as a penetration tester. Currently working on Eth2
differential fuzzing. Enjoys prodding at software and understanding systems

__Sydney, Australia

