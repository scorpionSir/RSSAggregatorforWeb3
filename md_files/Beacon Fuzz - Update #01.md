Close

Menu

  * [About Us](https://blog.sigmaprime.io/pages/about-us.html)

[![Blog Logo](./imgs/blog/sigp-logo-black.png)](https://blog.sigmaprime.io/)
__Menu

# Beacon Fuzz - Update #01

[Nathaniel Jensen](https://blog.sigmaprime.io/author/nathaniel-jensen.html) |
Tue 31 December 2019 Estimated read time: 10 min Image credits: [Photo by
Timothy Dykes](https://unsplash.com/@timothycdykes)

_Beacon Fuzz - Progress Update #1_

# Beacon Fuzz - Update #01  
  
Integrating new Eth2 clients, Fuzzing in the cloud

Sigma Prime is leading the development and maintenance of [beacon-
fuzz](https://github.com/sigp/beacon-fuzz), a differential fuzzing solution
for Eth2 clients. This post is part of our series of monthly status updates
where we discuss current progress, interesting challenges encountered, and
direction for future work. See [#00](https://blog.sigmaprime.io/beacon-
fuzz.html) and the repository's [README](https://github.com/sigp/beacon-
fuzz/blob/master/README.md) for more context.

## Summary

Over the last few weeks we've been making quiet progress, focusing primarily
on incorporating new clients, improving consistency and maintainability, and
updating the targeted spec. Achievements and points of interest include:

  * Updated to spec [v0.9.1](https://github.com/ethereum/eth2.0-specs/tree/v0.9.1)
  * Full integration of [ZRNT](https://github.com/protolambda/zrnt), [PySpec](https://github.com/ethereum/eth2.0-specs/tree/dev/test_libs/pyspec), and [Lighthouse](https://github.com/sigp/lighthouse)
  * [Nimbus](https://github.com/status-im/nimbus/) and [Trinity](https://github.com/ethereum/trinity) integration POCs
  * [First bug](https://github.com/status-im/nim-beacon-chain/issues/659) identified by Beacon Fuzz on Nimbus ( _attestation processing function_ )
  * Challenges incorporating [Prysm](https://github.com/prysmaticlabs/prysm) as a second Golang client
  * Continuous fuzzing on [Fuzzit](https://fuzzit.dev/)
  * Leveraging Python sub-interpreters for concurrently fuzzing multiple Python implementations (in our case, Trinity and PySpec)
  * An additional fuzzing target: `attester_slashing`/`process_attester_slashing()`

## To Eth2 Spec v0.9.1

All of our fuzzers are now operating on the
[v0.9.1](https://github.com/ethereum/eth2.0-specs/tree/v0.9.1) Eth2 spec, with
matching starter corpora available [here](https://github.com/sigp/beacon-fuzz-
corpora/tree/master/0-9-1).

This was relatively straightforward to implement (at the fuzzer level). The
majority of the work was associated with updating the Golang helper
library/preprocessor to remove crosslinks and transfers,and freezing client
implementations to a suitable commit/tag. It wasn't possible to find a
suitable commit in all cases, as some implementations were working on v0.9.1
and v0.9.2 in parallel and had some sections associated with each.

## Nimbus and Trinity Integrations

A big thanks to the Nimbus team, who developed a static library
[`nfuzz`](https://github.com/status-im/nim-beacon-chain/tree/master/nfuzz)
that implements harnesses for several targets. There is a working POC on our
`add-nimbus` branch (which will shortly be merged to master after a few
logging and error-handling changes are finalized). This is currently being
exercised on Fuzzit (see **Fuzzit** section of this blog post for more
details). Fuzzit Similarly, Trinity has been successfully integrated. Its
harnesses currently live in the `add-trinity` branch until some spec version
differences are resolved (when clients implement spec v0.9.2 or v0.9.3). Some
interesting details pertaining to this integration are discussed in more
detail in the section below.

## Incorporating Additional Implementations With Pragmatic Isolation

For differential fuzzing, it's desirable that each client implementation is
exercised in relative isolation with minimal modification. Although sometimes
necessary, each modification to the implementation code increases the risk of
introducing "false-positive" bugs (which are detected by the fuzzer but are
not present in the actual implementation), or masking client bugs such that
the fuzzer cannot detect them.

Similarly, we want to avoid crashes caused by interference between clients
(e.g. when implementations rely on different versions of the same dependency
or rely on the same global state). Although current clients don't clash much,
we should not rely on this, and should consider the issue now before it
becomes a major headache. Hypothetically, each implementation could achieve
effective memory isolation by running in a separate process. However, this
introduces substantial overhead and complications with instrumentation. As our
current fuzzing engine, libfuzzer, runs the fuzzing harness in a single
process, any multi-process solution would also require a significant re-
architecture.

So how do we achieve a reasonable level of in-process isolation, where clients
do not affect the correctness of others? For clients in different languages
(or VM runtimes), we deem it reasonable to leave as-is, realizing that a
clashing symbol name is highly unlikely, and we primarily focus on cases where
there are multiple clients in the same language.

So far, this is the case for Python (Trinity and Pyspec), and Golang (Prysm
and ZRNT). Isolation solutions are specific to each language.

### Python and Sub-Interpreters

The CPython interpreter and runtime relies on a global thread state. Naively
trying to embed or link multiple interpreters is doomed to fail (as we'd
quickly discovered). Fortunately, we stumbled upon a lesser-known feature of
the CPython C-API: [sub-
interpreters](https://docs.python.org/3/c-api/init.html#sub-interpreter-
support). They are quite niche and, currently,
[Apache/mod_wsgi](https://github.com/GrahamDumpleton/mod_wsgi) is one of the
few major projects that leverage them.

With a couple C function-calls, we can start a new sub-interpreter that is
reasonably isolated - each execution environment maintains its own `sys.path`,
`builtins`, and other modules. Although _currently_ of limited functionality
(they cannot provide true parallelism due to the Global Interpreter Lock, and
have no Python-level ability to communicate between interpreters), they are
perfect for our use case (we don't care about inter-interpreter communication,
and the fuzzer process is single-threaded/serialized anyway).

If you are interested in learning more about Python sub-interpreters, the
following links are useful:

  * [https://lwn.net/Articles/754162/](https://lwn.net/Articles/754162)
  * <https://talkpython.fm/episodes/show/225/can-subinterpreters-free-us-from-python-s-gil>
  * <https://ericsnowcurrently.blogspot.com/2016/09/solving-mutli-core-python.html>
  * <https://docs.python.org/3.8/c-api/init.html#sub-interpreter-support>

### Golang Library Linking Errors

When working to integrate Prysm, we found that the existing approach (designed
by [Guido Vranken](https://github.com/guidovranken/)) did not extend to more
than one Golang client in the same fuzzer. As of now, we can test with ZRNT or
Prysm (having a successful POC that integrates their
[bazel](https://bazel.build/) build system), but not both. We are also limited
to performing Prysm tests without input preprocessing (which relies on ZRNT).

The rest of this section will examine the issue in more detail, including an
exploration of possible approaches along with their identified challenges and
associated costs.

#### Existing approach

The existing approach uses a forked [`go-
fuzz`](https://github.com/guidovranken/go-fuzz/tree/libfuzzer-extensions)
(modified to return output for differential comparison). `go-fuzz` produces a
[`c-archive`](https://golang.org/cmd/go/#hdr-Build_modes) static library with
provided coverage instrumentation and a harness endpoint. As this archive
contains the Go runtime, redefinitions and symbol clashes occur when trying to
link more than one of them. Possible approaches generally involve leaving `go-
fuzz` unchanged and resolving linking problems, or modifying or removing `go-
fuzz` from the build process.

#### A) Renaming symbols

We can use `objcopy` to rename symbols in the archive such that symbol clashes
are avoided. It is difficult to programmatically rename only the symbols that
clash, therefore it is more simple and maintainable to use `objcopy --prefix-
symbols=` to prefix all symbols. Unfortunately, Prysm and ZRNT rely on
external systems or shared libraries, so renaming everything breaks these
references. (ZRNT doesn't use shared libraries, but the `cgo` runtime
references libraries such as
[`stdlib.h`](https://golang.org/src/runtime/cgo/gcc_linux_amd64.c) and
[`libpthread`](https://golang.org/src/runtime/cgo/gcc_libinit.c).)

#### B) Building as shared libraries

We could modify `go-fuzz` to produce shared/dynamic libraries with the
[buildmode](\(https://golang.org/cmd/go/#hdr-Build_modes\) c-shared.

With a shared library, internal symbols can have the same name as defined
elsewhere, as long as the externally visible symbols don't clash.

Unfortunately, we found the library produced by c-shared to expose many
runtime-related symbols that clash e.g. x_cgo_init, _cgo_panic.

As we don't make use of these externally, one option could be to wrap the
shared library such that it only exposes the fuzzing harness \(and
instrumentation\) interface, though this introduces more build complexit).

A combination of this and **A)** , where we rename only externally visible
symbols, could also be possible.

#### C) Combining into a single library built by `go-fuzz`

This approach involves creating a single Go package such that the harness
produced by `go-fuzz` exercises each Golang client.

While this would likely reduce runtime memory overhead (as only a single Go
runtime is used), relative isolation is lost. For Golang clients, this
isolation may be less important; especially if they make use of recent
_[semantic import
versioning](https://github.com/golang/go/wiki/Modules#semantic-import-
versioning)_ mechanisms that can allow the use of different major versions of
the same module. Our remaining concern would be if multiple clients relied on
some (unintentionally) shared, global state.

This approach also introduces other drawbacks. `go-fuzz` expects to produce a
single harness from a `Fuzz()` function. To remain as such, we would need this
`Fuzz()` function to perform the differential comparison between Go clients,
returning the result to the c++ differential module only if no differences are
found. This breaks some separation of concerns and is effectively a violation
of the [DRY principle](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself),
with its associated costs.

Alternatively, we could further modify the `go-fuzz` fork to allow the export
of multiple harness functions. This increases the differences between our fork
and `go-fuzz` proper, as well as the associated maintenance burden.

One should also consider the increased build complexity involved in combining
Prysm's Bazel-based build with the ZRNT's go module.

#### D) Building without `go-fuzz`

This approach is similar to **C)** , where only a single library is produced
exercising all Golang clients, but now we avoid `go-fuzz` entirely. This would
allow us to have full control over the build, exporting a separate harness
interface for each client, and avoiding the need to rely on, and maintain, a
fork of `go-fuzz`. All differential logic also remains contained in the
`fuzzing::Differential` c++ class.

The main cost involved would be to implement our own coverage instrumentation;
the difficulty or feasibility of which would greatly vary, depending on the
coverage measurements strategy adopted (simply compiling with the clang
`-fsanitize=fuzzer-no-link` flag, or implementing go-specific hooks).

## Our First Bug and How to Obtain Useful Debug Info

We have identified our first potential bug thanks to the `process_attestation`
fuzzer. When passed an invalid attestation, Nimbus crashes with an
`AssertionError` instead of returning a handle-able error value (i.e. `false`)
or raising a catchable exception.

See the related [GitHub issue](https://github.com/status-im/nim-beacon-
chain/issues/659) on the Nimbus repository for more information.

Currently, the crash corpus directly returned by `beacon-fuzz` is not very
useful to debug with. This is the raw data, before it has passed through
preprocessing, so it is different from what is passed to each client harness:

  1. The input is most likely invalid SSZ data that the preprocessing converts to a valid SSZ-encoded object.
  2. The input contains a `uint16_t` reference to a `BeaconState` file, which the preprocessing "dereferences", passing the `BeaconState` and the remaining input to the client harness. Only when combined with the relevant `BeaconState` does the corpus contain all details required to replicate the bug.

For debugging purposes, it would be much more useful to have the data as
passed to the client harness (after preprocessing). To this end, we have
produced a [`corpora-extract`](https://github.com/sigp/beacon-
fuzz/tree/fuzzit/files/tools/corpora-extract) CLI tool (working title) that
converts a corpus to such data. Better documentation and features to follow.

# Fuzzit

We have successfully published a few fuzzers to [Fuzzit](https://fuzzit.dev),
a _fuzzing-as-a-service_ , cloud platform. The current deployment has the
`block` and `shuffle` fuzzers exercising ZRNT, Nimbus, and Lighthouse. As
Fuzzit requires the upload of pre-built executables, some changes were needed
to get our current _"run-in-place"_ fuzzer executables to comply. These
changes were performed on the [`fuzzit`](https://github.com/sigp/beacon-
fuzz/tree/fuzzit) branch, and also involve additional manual configuration.

Once built, the current fuzzer executable depends on the following external
files:

  * Several shared libraries - both cpython "dynlibs", and system-installed `pcre`, `rocksdb`, `ssl`, `leveldb` etc.
  * A directory of `BeaconState` SSZ files specified by the `ETH2_FUZZER_STATE_CORPUS_PATH` environment variable.
  * Python harness scripts located in absolute paths set at compile-time.

Fortunately, Fuzzit accepts a `.tar.gz` archive. As long as it contains a
`./*fuzzer*` executable, everything else is ok and we don't have to try to
embed all components and modules into a single binary.

Operation was successful once we used relative paths for runtime references,
included relevant shared libraries, and modified the runtime load path to
point to the libraries. We modified the Python script paths to be relative to
the executable and bundled relevant shared libraries (collected via `ldd -v
./fuzzer` and referenced at runtime by setting
[`LD_LIBRARY_PATH`](https://linux.die.net/man/8/ld-linux)). However, the
current cpython install configuration contains absolute paths and couldn't be
moved, so Python clients were disabled for the POC.

The current POC has been sufficient to confirm feasibility of fuzzing on
Fuzzit, so automated build of a suitable bundle and CI integration will
follow.

## Next Steps

Welcome Przmek (aka [@cryptomental](https://github.com/cryptomental)) to the
Beacon Fuzz team!

Przmek has a wealth of fuzzing experience (differential and otherwise) thanks
to his efforts with Eth1. He will initially be focussing on resolving the
integration issues with multiple Golang clients.

Some of the areas we'll be working on over the upcoming weeks:

  * Upgrade to spec [v0.9.3](https://github.com/ethereum/eth2.0-specs/tree/v0.9.3) or [v0.9.4](https://github.com/ethereum/eth2.0-specs/tree/v0.9.4) once 3 or more clients have implemented it. (Likely mid-late Jan)
  * Create fuzzing targets for the rest of the state transition functions (epoch state transitions).
  * Improved mutation via [libprotobuf-mutator](https://github.com/google/libprotobuf-mutator). This involves converting SSZ into protobuf and back, and utilizing libprotobuf-mutator for [structure-aware fuzzing](https://github.com/google/fuzzing/blob/master/docs/structure-aware-fuzzing.md). Some work has started here but a working POC is still in progress. Once operational, this is expected to vastly improve fuzzing coverage.
  * Improved use of continuous fuzzing services (fuzzit for now), and to submit a request to Google [OSS-Fuzz](https://google.github.io/oss-fuzz/) in the near future.

[ __Twitter ](https://twitter.com/share?text=Beacon Fuzz - Update
#01&url=https://blog.sigmaprime.io/beacon-fuzz-01.html) [ __Facebook
](https://www.facebook.com/sharer/sharer.php?u=https://blog.sigmaprime.io/beacon-
fuzz-01.html) [ __Google+
](https://plus.google.com/share?url=https://blog.sigmaprime.io/beacon-
fuzz-01.html)

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

