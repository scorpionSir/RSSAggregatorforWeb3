Close

Menu

  * [About Us](https://blog.sigmaprime.io/pages/about-us.html)

[![Blog Logo](./imgs/blog/sigp-logo-black.png)](https://blog.sigmaprime.io/)
__Menu

# Beacon Fuzz - Update #03

[Mehdi Zerouali](https://blog.sigmaprime.io/author/mehdi-zerouali.html) | Tue
07 April 2020 Estimated read time: 5 min Image credits: [Photo by Samuel
Myles](https://unsplash.com/@samdasherx13)

_Beacon Fuzz - Progress Update #3_

# Beacon Fuzz - Update #03  
  
New Fuzzing Engine, New Bugs

Sigma Prime is leading the development and maintenance of [beacon-
fuzz](https://github.com/sigp/beacon-fuzz), a differential fuzzing solution
for Eth2 clients. This post is part of our series of status updates where we
discuss current progress, interesting challenges encountered, and direction
for future work. See [#00](https://blog.sigmaprime.io/beacon-fuzz.html) and
the repository's [README](https://github.com/sigp/beacon-
fuzz/blob/master/README.md) for more context.

## Summary

Lots of Eth2-related fuzzing has happened at Sigma Prime over the past few
weeks! Great progress was made by the Beacon Fuzz team:

  * New fuzzing engine: Honggfuzz
  * Coverage Reports and Beacon Fuzz Revamp in Rust
  * Critical SSZ bug identified in Lighthouse
  * Beacon State Fuzzing and Overflows
  * Java integration
  * New team member

## Honggfuzz

[Honggfuzz](https://github.com/google/honggfuzz) is an easy to use
evolutionary fuzzer (developed and maintained by Google) with the following
interesting features:

  * **Multi-process and multi-threaded** : Honggfuzz can leverage all available CPU cores with a single running instance (by automatically sharing the corpus information with all fuzzing processes);
  * **Extremely fast with the support of persistent fuzzing** : A standard `LLVMFuzzerTestOneInput` function can be tested with up to 1 million iterations per second!
  * **Great track record of finding bugs (e.g OpenSSL)** : Honggfuzz is the only fuzzer that managed to identify a critical vulnerability in OpenSSL. The [trophies](https://github.com/google/honggfuzz#trophies) list is quite impressive.
  * **Keeps fuzzing even after the identification of a crash** : identification of a crash doesn't mean that the fuzzing stops, as opposed to the behaviour of `libFuzzer` (painful for continuous fuzzing).

In the latest benchmarks published by Google via their project
[FuzzBench](https://google.github.io/fuzzbench/), Honggfuzz seems to be more
efficient in terms of reached coverage (code blocks) than AFL and libFuzzer.

![coverage](https://www.fuzzbench.com/reports/2020-03-04/bloaty_fuzz_target_ranking.svg)

_Source:[fuzz bench](https://google.github.io/fuzzbench/)_

We've decided to experiment with Honggfuzz to leverage its different set of
mutation algorithms (compared to libFuzzer and AFL). This was a great decision
considering that this new fuzzing engine helped us identify the bugs described
in this article.

![Honggfuzz](./imgs/beacon-fuzz/honggfuzz.jpg)

_Screenshot illustrating Honggfuzz exercising the process deposit function of
Lighthouse_

## Coverage Reports and Beacon Fuzz Revamp

Over the past few weeks, we decided to get a better view on the code coverage
of our fuzzing inputs. As such, code coverage reports were produced using
[Kcov](https://github.com/SimonKagstrom/kcov), indicating a coverage of more
than **84%** using the `eth2spec` tests:

![coverage](./imgs/beacon-fuzz/coverage.png)

_Coverage reports produced
using[Kcov](https://github.com/SimonKagstrom/kcov/)_

To generate interesting samples/inputs, we've created a CLI tool, currently
named **all_fuzz** that allows:

  * Automatic fuzzing of lighthouse harnesses (without user interaction)
  * Swapping between multiple fuzzing engines (Honggfuzz, AFL, libFuzzer)
  * Multi-threading
  * Automatic and pseudo-random selection of a `BeaconState` per fuzzing thread
  * Crash report/detection

This allowed the identification of the two bugs described in the following
sections.

We've also started rewriting Beacon Fuzz in Rust (from C++) as the team is
more familiar/experienced with this language.

## Critical SSZ Bug in Lighthouse

Honggfuzz found a crash in Lighthouse related to our SSZ decoding which failed
to ensure that all offsets were in-bounds for variable length types.

When decoding a specific, custom, mutated `BeaconState` SSZ file, Lighthouse
tries to allocate too much memory, causing a memory allocation failure which
leads to a panic. The affected function in our SSZ crate is `pub fn
decode_list_of_variable_length_items<T: Decode>`

In fact, this is an attack vector that [Paul](https://twitter.com/paulhauner)
had identified [last
year](https://notes.ethereum.org/ruKvDXl6QOW3gnqVYb8ezA#4-Offsets-are-out-of-
bounds).

We thought we had a test internally that would catch this particular case, but
as described in [this
issue](https://github.com/sigp/lighthouse/pull/974#issuecomment-606414975),
the error we were catching in the relevant unit test was in fact unrelated to
the test case we wanted to cover.

This bug was quickly addressed by Paul and a fix has been submitted in [this
Pull Request](https://github.com/sigp/lighthouse/pull/974) (to be merged
soon).

## Beacon State Fuzzing and Overflows

When fuzzing the `BeaconState` struct in `debug` mode with Honggfuzz, a panic
was triggered by a multiplication overflow when attempting to get the Beacon
proposer index for a mutated `BeaconState`.

Indeed, the underlying issue stems from these particular lines (see the
function
[`compute_proposer_index`](https://github.com/sigp/lighthouse/blob/e04fc8ddb488785e54552005ca96eede3910262d/eth2/types/src/beacon_state.rs#L420-L426)):

    
    
    let effective_balance = self.validators[candidate_index].effective_balance;
    if effective_balance * MAX_RANDOM_BYTE
        >= spec.max_effective_balance * u64::from(random_byte)
    {
        return Ok(candidate_index);
    }
    i += 1;
    }
    

The mutations performed by Honggfuzz triggered an integer overflow in the
condition `if effective_balance * MAX_RANDOM_BYTE >=
spec.max_effective_balance * u64::from(random_byte)`.

The Beacon State is currently considered as a trusted container: it is
internally constructed and iterated by clients and cannot (at this stage) be
provided as an externally user-supplied input. This might however change as
future syncing strategies might enable beacon nodes to request `BeaconState`
objects from peers for faster syncing (as opposed to requesting block
batches).

This is important as some of the bugs that our fuzzing effort will identify
won't necessarily be exploitable (including the overflow described above).
However, it's important to clarify the overflow assumptions of the eth2
specification, and this bug lead to an [interesting
discussion](https://github.com/ethereum/eth2.0-specs/issues/1701).

As a result, the [remerkleable](https://github.com/protolambda/remerkleable)
Python package maintained by [protolambda](https://github.com/protolambda) and
used in the python executable eth2 spec has been updated to provide stronger
guarantees on overflows.

## Java Integration

The team has also been making great progress in integrating Teku (formerly
known as Artemis/Harmony):

  * New fuzzing harnesses have been written in Java to exercise the relevant state transition functions. These harnesses compile, and the relevant `CLASSPATH` is passed to the fuzzer during build;
  * Similar to the Python module, the C++ fuzzing endpoint launches an (in-process) Java runtime and interacts with a Teku harness via the Java Native Interface (JNI). Embedding all these runtimes can bloat the central process, but avoids overheads and complications involved with passing corpora and coverage data via IPC, as well as reliably ensuring signals and crashes are managed by the fuzzer.
  * All currently supported harnesses have been implemented for Teku, and the integration will be merged to master upon completion of beacon_fuzz support for spec `v0.11`.

## New Team Member

[Patrick](https://twitter.com/Pat_Ventuzelo) has recently joined the Beacon
Fuzz crew and has been instrumental in achieving the milestones decribed in
this article. We're really glad to have him onboard are look forward to
working with him closely on Beacon Fuzz over the coming weeks and months!

## Next steps

  * Update to Eth2 spec `v0.11` (nearing completion)
  * Process interesting corpora on all available implementations
  * Continue revamp of Beacon Fuzz in Rust
  * Integrate the use of the `Arbitrary` trait for grammar-based fuzzing
  * Proposal submission to [OSS-Fuzz](https://google.github.io/oss-fuzz/)

[ __Twitter ](https://twitter.com/share?text=Beacon Fuzz - Update
#03&url=https://blog.sigmaprime.io/beacon-fuzz-03.html) [ __Facebook
](https://www.facebook.com/sharer/sharer.php?u=https://blog.sigmaprime.io/beacon-
fuzz-03.html) [ __Google+
](https://plus.google.com/share?url=https://blog.sigmaprime.io/beacon-
fuzz-03.html)

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

