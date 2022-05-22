Close

Menu

  * [About Us](https://blog.sigmaprime.io/pages/about-us.html)

[![Blog Logo](./imgs/blog/sigp-logo-black.png)](https://blog.sigmaprime.io/)
__Menu

# Beacon Fuzz - Update #02

[Nathaniel Jensen](https://blog.sigmaprime.io/author/nathaniel-jensen.html) |
Mon 24 February 2020 Estimated read time: 8 min Image credits: [Photo by The
Nigmatic](https://unsplash.com/@thenigmatic)

_Beacon Fuzz - Progress Update #2_

# Beacon Fuzz - Update #02  
  
First Bugs, More Eth2 Clients

Sigma Prime is leading the development and maintenance of [beacon-
fuzz](https://github.com/sigp/beacon-fuzz), a differential fuzzing solution
for Eth2 clients. This post is part of our series of monthly status updates
where we discuss current progress, interesting challenges encountered, and
direction for future work. See [#00](https://blog.sigmaprime.io/beacon-
fuzz.html) and the repository's [README](https://github.com/sigp/beacon-
fuzz/blob/master/README.md) for more context.

## Summary

The Beacon Fuzz team has been making steady progress over the last few weeks.
Key achievements and points of interest include:

  * New bugs identified in two separate implementations
  * Additional state transition fuzzing targets implemented
  * A Proof-of-Concept simultaneously exercising both [Prysm](https://github.com/prysmaticlabs/prysm) and [ZRNT](https://github.com/protolambda/zrnt)
  * Better internal tooling
  * Maintainability improvements

## New Bugs Identified

Even in its early stages, `beacon-fuzz` is already identifying some bugs and
providing value to the ecosystem:

  * [Trinity#1497](https://github.com/ethereum/trinity/issues/1497) \- two validation functions (`validate_voluntary_exit()` and `validate_proposer_slashing()`) raise an `IndexError` given invalid Validator indices, when we had expected them to only raise `ValidationError`:

There is currently some ambiguity whether this is a bug or we need to treat
`IndexError` as an expected error result. The relevant test fixtures list
`IndexError` as an expected exception, but the block importing in
`BeaconChainSyncer` only explicitly checks for `ValidationError`. In any case,
this does not crash the application, as all exceptions caused by block
importing are caught and logged at a higher level. See the issue for more
details.

  * [Nimbus#703](https://github.com/status-im/nim-beacon-chain/issues/703) \- Merkle proof validation in `process_deposit` was not enforced:

Passing an invalid deposit object (i.e. a deposit object with an invalid
merkle proof) would lead to the deposit being succesfully processed. In other
words, this bug could have allowed a malicious actor to artificially mint ETH
on the Beacon Chain without actually depositing ETH to the Eth1 contract! The
Nimbus team have also fixed the [attestation validation
crash](https://github.com/status-im/nim-beacon-chain/issues/659) discussed in
our last post.

Thesse are listed in a [Trophies](https://github.com/sigp/beacon-
fuzz#trophies) section of our README, which will be updated as more bugs are
found and can be disclosed.

## Additional state transition targets

Fuzzing targets have been implemented for the remaining state transition block
operations:

  * **deposit** : [`process_deposit()`](https://github.com/ethereum/eth2.0-specs/blob/v0.9.2/specs/core/0_beacon-chain.md#deposits)
  * **proposer_slashing** : [`process_proposer_slashing()`](https://github.com/ethereum/eth2.0-specs/blob/v0.9.2/specs/core/0_beacon-chain.md#proposer-slashings)
  * **voluntary_exit** : [`process_voluntary_exit()`](https://github.com/ethereum/eth2.0-specs/blob/v0.9.2/specs/core/0_beacon-chain.md#voluntary-exits)

With this, the only remaining block-processing endpoints are
`process_randao()` and `process_eth1_data()`, and per-epoch processing will be
the primary focus for subsequent targets.

Big thanks to the Nimbus team for, amongst other things, their quick response
accepting PRs that update their test harnesses.

### `process_deposit` precondition

While implementing the `deposit` target, we noticed it is an interesting case
where, unlike other operation processing functions, some relevant validation
occurs outside `process_deposit()`.

[`process_operations()`](https://github.com/ethereum/eth2.0-specs/blob/v0.9.2/specs/core/0_beacon-
chain.md#operations) contains

    
    
    assert len(body.deposits) == min(MAX_DEPOSITS, state.eth1_data.deposit_count - state.eth1_deposit_index)
    

This has some effect on what input `process_deposit()` can expect, but only
really implies the invariant `state.eth1_deposit_index <=
state.eth1_data.deposit_count`.

This means passing a state where `eth1_deposit_index >=
eth1_data.deposit_count` holds to `process_deposit()` is undefined behaviour;
it could be reasonable to panic or abort.

We can enforce this precondition as part of pre-processing and, given how
highly unlikely it is for random mutations to result in a correct Merkle proof
(especially as a changed `eth1_deposit_index` can invalidate an otherwise
correct proof), we might as well disable Merkle proof validation within the
`deposit` fuzzer, allowing subsequent code to be exercised. If not feasible
for all implementations to expose the ability to skip Merkle validation, pre-
processing could be used to generate a correct proof as an alternative.

It would be reasonable to then exercise `is_valid_merkle_branch()` within its
own dedicated fuzzer.

## Progress integrating multiple Go clients (Prysm)

See our [previous post](https://blog.sigmaprime.io/beacon-fuzz-01.html) for a
detailed exploration of the problem and potential approaches.

Przmek (aka [@cryptomental](https://github.com/cryptomental)) has been
plugging away, working on running multiple isolated Go clients, and has made
significant progress! There is now a PoC in which ZRNT, Prysm, Nimbus and
Lighthouse all exercise the `shuffle` target. We will need to sort out some
PRs and update the fuzzers to spec `v0.10.x` before this is merged into
master.

Some of his adventures are detailed below:

### Modifying static libraries prior to linking

We'd previously made a naive attempt that renamed all symbols to avoid
clashes. As discussed previously, this fails at link time because the `cgo`
runtime references externally defined symbols in `stdlib.h` and `libpthread`.

A more precise approach explored by Przmek involves using `objcopy --redefine-
syms` to rename only symbols that clash. While this resolved build errors, a
runtime `segfault` occurred. Further troubleshooting indicated that the
runtime performs code generation, where the generated code eventually
references these symbols by fixed names. Any further work here would require
modification to the underlying go runtime, resulting in a solution (if it
exists) that is exceedingly unsupported and difficult to maintain.

### Other unsuccessful approaches

  * That said, some experiments involved modifying clashing function names in `go-fuzz-build/src/runtime` and export lists of clashing symbols in the Go runtime's `callbacks.go`, and even renaming all clashing symbols in the runtime via `sed`.

Unfortunately, segmentation faults still occurred without narrowing things
down.

  * Deleting duplicate symbols from the object files.

This resolved some build errors due to clashes, but there were still 2 Go
runtimes being invoked that now reference each other.

  * Building static libraries with various combinations of arcane `cgo` linker flags, including `-linkmode=external` and direct linker arguments including `-Bsymbolic`, `-Bnoobjreorder`, `--allow-multiple-definition`, and `-static`.

These linker arguments either had no effect (when applied to `go-fuzz-build`
because static libraries are only linked with the executable), or had
unintended side-effects (applied "globally" and changing how every other part
of the fuzzer is linked).

### Successful PoC

The working concept involves using a combined `GOPATH`, and additional
modifications to Guido Vranken's `go-fuzz-build` fork to allow shared library
compilation via the `c-shared` build mode and application of the `-BSymbolic`
linker and `-fPIC` compilation flags (which now apply only to the contents of
the shared library).

It's also worth noting that Nim also currently makes use of Golang, wrapping
`go-libp2p` for its current libp2p library. Przmek found that this also causes
clashes when both Prysm and Nimbus were present, likely due to a shared
dependency on `go-libp2p`. Using a more recent Nimbus commit (now `v0.10.x`)
and building it as a shared library fixed those issues.

We expect to have Prysm running in master very shortly!

## Tooling improvements

We added an extension to the seed corpora script:
[`all_corpora_from_tests.py`](https://github.com/sigp/beacon-fuzz-
corpora/blob/master/scripts/all_corpora_from_tests.py) that converts _all_
relevant Eth2 consensus tests and `beaconstate` objects to corpora (including
for new state transitions). This now allows a single command to generate a
complete set of starter corpora for a spec version.

Interestingly, this script has now encountered some difficulties if we still
want it to be able to work for multiple spec versions. `v0.9.4` introduced
some naming differences with regards to the SSZ containers we use. As
[PySpec](https://github.com/ethereum/eth2.0-specs/tree/dev/test_libs/pyspec)
currently contains no `VERSION` package metadata, there is no reliable way for
the script to programmatically determine the spec version, and which names to
use. This will be provided via a user-supplied parameter for now.

## Maintainability improvements

We've made several internal changes that improve quality of life, reduce
overheads associated with adding additional targets, and ease crash
investigation. These include:

  * A generalized Makefile shared between all fuzzing targets ([`fuzzer.mk`](https://github.com/sigp/beacon-fuzz/blob/3d34ff509251a5a80b077f33290289b4a56a62bf/files/fuzzers/fuzzer.mk)):

This gets rid of a lot of copy-paste located in the per-target build process
(with associated maintainability improvements), whilst still allowing per-
target customization via an included `def.mk`. Much time was previously spent
checking that a change to the build was made correctly to all targets, so this
is an important improvement to our build process.

  * Globally enable/disable BLS verification via Makefile variable:

This allows an easy switch between fuzzing with BLS verification enabled or
not, and is generally left disabled to improve coverage (exceedingly unlikely
for a random mutation to result in a valid signature). It is also a PoC of the
interface that will be used to enable/disable individual clients (to allow
easy building of fuzzers that exercise some subset of clients available).

  * Print relevant clients when a difference is detected:

Previous output only stated that a difference was detected, and what it was -
not which clients were involved. Now, each client class contains a `name`
string and, as the number of clients increase, this is quite a welcome
improvement.

  * Nim and Rust C++ harness boilerplate put into a library:

The C++ boilerplate used to interface with Rust and Nim clients was consistent
across all block-operation harnesses so was extracted into library files,
again reducing copy-pasted code.

  * Python `FuzzerInit()` function accepting runtime arguments - allows fuzzer to change configuration (e.g. BLS enable), opening up the ability for paths to harness and config files be set at runtime by the central C++.

As additional targets are implemented, costs involved with `>= O(n)`
development processes exhaust more useful time and improvements become more
important.

## Next steps

  * Implementation of targets for epoch state transitions:
    * As these only take a `beaconstate` as input, providing a known, valid collection of `beaconstate` objects is not sufficient. We now need something to generate appropriate states - like a custom `libprotobuf` mutator.
    * Because a `beaconstate` is not untrusted input, there are many implicit preconditions and invariants that limit what states a function can expect. It can be reasonable for a client to abort when these preconditions are broken, so we want to only pass suitable states.
    * If unsuitable, we could try generating valid states for Epoch Transitions by performing a heap of block transitions via a reference spec.
  * Integration of the Java-based Teku/Artemis client:
    * Work on this is progressing smoothly and an initial proof-of-concept is imminent.
  * Update to Eth2 spec `v0.10.1`
  * Thanks to [fuzzit.dev](https://fuzzit.dev) for providing OSS licensing. We will look to integrate some CI tooling as manually testing each fuzzer consumes more time
  * Proposal submission to [OSS-Fuzz](https://google.github.io/oss-fuzz/)

[ __Twitter ](https://twitter.com/share?text=Beacon Fuzz - Update
#02&url=https://blog.sigmaprime.io/beacon-fuzz-02.html) [ __Facebook
](https://www.facebook.com/sharer/sharer.php?u=https://blog.sigmaprime.io/beacon-
fuzz-02.html) [ __Google+
](https://plus.google.com/share?url=https://blog.sigmaprime.io/beacon-
fuzz-02.html)

[ethereum](https://blog.sigmaprime.io/tag/ethereum.html)[blockchain
security](https://blog.sigmaprime.io/tag/blockchain-
security.html)[fuzzing](https://blog.sigmaprime.io/tag/fuzzing.html)[cybersecurity](https://blog.sigmaprime.io/tag/cybersecurity.html)[differential
fuzzing](https://blog.sigmaprime.io/tag/differential-fuzzing.html)[beacon
chain](https://blog.sigmaprime.io/tag/beacon-chain.html)

![Nathaniel Jensen](https://blog.sigmaprime.io/imgs/authors/nat.png)

#### [Nathaniel Jensen](https://blog.sigmaprime.io/author/nathaniel-
jensen.html)

Nat is a Security Engineer at Sigma Prime. A Computer Science graduate with
experience working as a penetration tester. Currently working on Eth2
differential fuzzing. Enjoys prodding at software and understanding systems

__Sydney, Australia

