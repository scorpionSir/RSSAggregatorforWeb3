Close

Menu

  * [About Us](https://blog.sigmaprime.io/pages/about-us.html)

[![Blog Logo](./imgs/blog/sigp-logo-black.png)](https://blog.sigmaprime.io/)
__Menu

# Announcing Beacon Fuzz, an Eth2 Differential Fuzzer

[Mehdi Zerouali](https://blog.sigmaprime.io/author/mehdi-zerouali.html) | Thu
21 November 2019 Updated on Thu 21 November 2019 Estimated read time: 4 min

_Sigma Prime was approached by the Ethereum Foundation to lead the development
and maintenance of a differential fuzzer for Ethereum 2.0 clients. This
document explains our approach for the proposed differential fuzzer, and
defines the upcoming milestones for this project._

# Context

Fuzz testing (or fuzzing) is a process that allows the identification of bugs
(not just security-related bugs) by providing randomised and unexpected data
inputs to software, with the goal of causing crashes (or in Rust, panics) and
other unexpected behaviours (e.g. memory leaks).

Popular modern fuzzing frameworks, including AFL and libFuzzer, allow for
several types of fuzzing:

  * **In-process fuzzing:** the fuzzing engine executes the target many times with multiple data inputs in the same process. It must tolerate any kind of input (empty, huge, malformed, etc);
  * **White-box fuzzing:** the fuzzing toolset leverages compiler instrumentation and requires access to the source code
  * **Coverage-guided fuzzing** : for every input/test case, the fuzzing framework tracks code paths (sections of the code which have been reached), and produces variants of each test case to generate additional input data with the goal of increasing code coverage.

Sigma Prime has been utilising
[libFuzzer](https://llvm.org/docs/LibFuzzer.html) on
[Lighthouse](https://github.com/sigp/lighthouse) to identify vulnerabilities
which affect our crates and our dependencies. This process has been successful
in identifying multiple bugs, some of which were caused by upstream
dependencies used by various projects in the Blockchain space (refer to our
[fuzzing update](https://lighthouse.sigmaprime.io/fuzzing-01.html) and the
security section of our [Lighthouse
updates](https://lighthouse.sigmaprime.io/) for more details).

Differential fuzzing is the process of fuzz testing multiple implementations
of the same specification and detecting any deviation/differences between the
outputs produced by each of these implementations.

In May 2019, the Ethereum Foundation engaged [Guido
Vranken](https://github.com/guidovranken/) to build a platform that allows
differential fuzzing to be performed across the various Ethereum 2.0 clients.
[This work](https://github.com/guidovranken/eth2.0-fuzzing) leveraged
libFuzzer, and focussed on fuzzing ZRNT and Pyspec, the Go and Python
executable Ethereum 2.0 specification.

Vranken’s work leverages libFuzzer by creating modules (1 module per
implementation to be fuzzed), orchestrated in C++, to be provided the same
fuzzing input.

# Approach

Since September 2019, Sigma Prime (primarily [Nathaniel
Jensen](https://github.com/gnattishness)) has been building upon Guido
Vranken’s prior work by:

  * Analysing the long-term maintainability of the differential fuzzing platform and exploring other potential options to achieve the same goals;
  * Upgrading the fuzzing targets to match the latest version of the Ethereum 2.0 specification (version 0.8.3 at the time of writing);
  * Adding more fuzzing targets;
  * Establishing a set of valid inputs (corpora) to be used by the differential fuzzer.

Sigma Prime’s work on the differential fuzzer, named `beacon-fuzz`, is
accessible at the following repositories:

  * <https://github.com/sigp/beacon-fuzz/>
  * <https://github.com/sigp/beacon-fuzz-corpora>

Beacon-fuzz currently runs the following fuzzing targets:

  * **block** : `process_block()`
  * **block_header** : `process_block_header()`
  * **attestation** : `process_attestation()`
  * **shuffle** : `compute_shuffled_index()`

Implementations are now loading a BeaconState from file through a pre-
processing function that uses a `state_id` reference and passes the relevant
state to the different fuzz targets.

The four fuzzing targets currently support implementations from ZRNT, Pyspec,
and Lighthouse.

# Upcoming Milestones

Coverage tracking and optimisation is a main priority. We’re adding more valid
inputs to the corpora (refer to the https://github.com/sigp/beacon-fuzz-
corpora repository) and are exploring adding valid post-states (Beacon states
generated after a valid state transition) to the `BeaconState` corpus.

Specifically, we are working on adding support for the following epoch state
transition related functions in new fuzzing targets:

  * `process_justification_and_finalization`
  * `process_final_updates`
  * `process_slashings`
  * `process_registry_updates`
  * `process_rewards_and_penalties`

We’re also ensuring consistent behaviour in the various implementations when
returning empty byte arrays as opposed to uninitialized pointers.

Sigma Prime is also exploring the possibility of creating custom libFuzzer
mutators to enable structure-aware mutation-based fuzzing. Custom mutators can
be considered as libFuzzer plugins and are user-defined functions which
perform the following:

  * Parses the input data following a defined scheme (or grammar)
  * Performs mutations of the parsed data (by leveraging libFuzzer mutations)
  * Encodes (in our case, SSZ-serialises) the mutated data

This approach should provide greater coverage by generating and mutating valid
beacon states.

The plan is to progressively onboard all Eth2 implementations:

  * Nimbus
  * Prysm
  * Trinity
  * Shasper
  * Artemis/Harmony
  * Lodestar

We have started reaching out to the development teams listed above to
integrate their respective clients.

# Conclusion

We're very excited to further contribute to the Eth2 security ecosystem beyond
[Lighthouse](https://lighthouse.sigmaprime.io) and proud to have received a
[grant](https://blog.ethereum.org/2019/11/21/eth2-quick-update-no-4/) from the
Ethereum Foundation to support this effort. We're looking forward to sharing
updates about this project on a monthly basis with a focus on documenting the
technical challenges and keeping the community informed on the latest
developments. We will also actively be seeking input and feedback from experts
in the fuzzing and Ethereum security communities. If you want to help, please
feel free to [DM me on Twitter](https://twitter.com/ethzed)!

[ __Twitter ](https://twitter.com/share?text=Announcing Beacon Fuzz, an Eth2
Differential Fuzzer&url=https://blog.sigmaprime.io/beacon-fuzz.html) [
__Facebook
](https://www.facebook.com/sharer/sharer.php?u=https://blog.sigmaprime.io/beacon-
fuzz.html) [ __Google+
](https://plus.google.com/share?url=https://blog.sigmaprime.io/beacon-
fuzz.html)

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

