Close

Menu

  * [About Us](https://blog.sigmaprime.io/pages/about-us.html)

[![Blog Logo](./imgs/blog/sigp-logo-black.png)](https://blog.sigmaprime.io/)
__Menu

# Beacon Fuzz - Update #05

[Mehdi Zerouali](https://blog.sigmaprime.io/author/mehdi-zerouali.html) | Wed
17 June 2020 Estimated read time: 4 min Image credits: [Photo by Sergio
Souza](https://unsplash.com/@serjosoza)

_Beacon Fuzz - Progress Update #5_

# Beacon Fuzz - Update #05  
  

Sigma Prime is leading the development and maintenance of [beacon-
fuzz](https://github.com/sigp/beacon-fuzz), a differential fuzzing solution
for Eth2 clients. This post is part of our series of status updates where we
discuss current progress, interesting challenges encountered and direction for
future work. See [#00](https://blog.sigmaprime.io/beacon-fuzz.html) and the
repository's [README](https://github.com/sigp/beacon-
fuzz/blob/master/README.md) for more context.

## Summary

  * Prysm client integration and first bugs
  * Lodestar integration and first bugs
  * Lighthouse ENR crate bug
  * Dockerising Eth2fuzz
  * Next Steps

## Prysm Integration

As mentioned in our previous updates, one of the biggest challenges faced
while working on Beacon Fuzz was the integration of the Prysm client alongside
ZRNT, protolambda's Go executable Eth2 specification. The issues encountered
by the team were documented extensively in our previous posts
([#1](http://localhost:8000/beacon-fuzz-01.html),
[#2](http://localhost:8000/beacon-fuzz-02.html),
[#4](http://localhost:8000/beacon-fuzz-04.html)).

Recently, Prysmatic Labs
[announced](https://twitter.com/raulitojordan/status/1267100659259670528?s=20)
their _"biggest feature of the year"_ , which allows developers to build the
Prysm client using the native `go build` functionality, without the need of
using `Bazel`. As mentioned by Preston in the [related pull
request](https://github.com/prysmaticlabs/prysm/pull/6053), this removes a lot
of friction for external contributors and developers wanting to
integrate/build on top off the Eth2 Golang implementation. We requested this
feature in [this issue](https://github.com/prysmaticlabs/prysm/issues/6005)
and were very happy to see it implemented, a big thank you to the Prysmatic
Labs crew!

As a result, significant progress has been made in fuzzing Prysm (progress can
be tracked in [this branch](https://github.com/sigp/beacon-
fuzz/tree/eth2fuzz_add_prysm_go_fuzzing)) which yielded the identification of
the following vulnerabilities:

  * **Panic due to an _out-of-bands_ slice range**: identified in in the `go-ssz` library, while fuzzing `Attestation` parsing. Refer to [this issue](https://github.com/prysmaticlabs/prysm/issues/6083) for the detailed bug report and [this pull request](https://github.com/prysmaticlabs/go-ssz/pull/112) for the related fix.
  * **Panic due to a *nil pointer dereference** *: identified in `ProposerSlashing` processing while fuzzing the `VerifyProposerSlashing` function. Refer to [this issue](https://github.com/prysmaticlabs/prysm/issues/6127) for the detailed bug report and [this pull request](https://github.com/prysmaticlabs/prysm/pull/6218) for the related fix.

## Lodestar Integration

A new Eth2 implementation has made it to Beacon Fuzz! We're glad to have been
able to perform some fuzzing on [`Lodestar`](), the JavaScript client
developed by ChainSafe. We've been primarily targeting
serialisation/deserialisation functions by leveraging
[`jsfuzz`](https://github.com/fuzzitdev/jsfuzz), a coverage guided fuzzer for
JS/NodeJS packages, heavily based on `go-fuzz` and `AFL`.

The first Lodestar fuzzing round lead to the identification of the four
following bugs:

  * `TypeError` bug when SSZ decoding a `BeaconBlock` with an invalid `BigInt` parent scope (refer to [this issue](https://github.com/ChainSafe/ssz/issues/22) for more details);
  * `RangeError` bug when SSZ decoding an empty `BeaconBlock` container (refer to [this issue](https://github.com/ChainSafe/ssz/issues/23) for more details);
  * `TypeError` bug when decoding an invalid base64 `ENR` string (refer to [this issue](https://github.com/ChainSafe/discv5/issues/56) for more details);
  * `TypeError` bug when decoding an invalid `ENR` `RLP` encoded string (refer to [this issue](https://github.com/ChainSafe/discv5/issues/59) for more details).

We're looking forward to targeting the state transition functions next, when
these bugs are resolved by the Lodestar development team.

## Lighthouse ENR Crate Bug

While fuzzing the Lighthouse [ENR crate](https://github.com/AgeManning/enr),
we identified a vulnerability that can be exploited when a non-utf8 string is
attempted to be decoded as an ENR.

Specifically, [Honggfuzz](https://github.com/google/honggfuzz), the fuzzing
engine used to identify this vulnerability, produced the string `49ŷ` that
caused a panic in the related crate. This bug is reproducible
[here](https://play.rust-
lang.org/?version=stable&mode=debug&edition=2018&gist=a40ac5b60914f5046aad61d0c2334a64).

This vulnerability was fixed by Age in [this pull
request](https://github.com/AgeManning/enr/pull/12/files).

## Dockerising Eth2fuzz

We're currently in the process of _dockerising_ our fuzzers to enable the
community to participate in identifying bugs across the Eth2 implementations.
Since each fuzzing instance uses a random _seed_ , the more people run these
fuzzers, the more chances we have to uncover bugs and vulnerabilities. We've
been running our fuzzers on our local infrastructure and are exploring
integrated, continuous fuzzing options (see section below), but would love to
see these fuzzers running on other machines. We were hoping to have the
_dockerisation_ process ready for this blog post, but have been running into
the following issues:

  * Compilation time and resulting disk space is currently quite prohibitive (we're targeting initial support for 3 to 4 different implementations);
  * Race conditions currently prevent running different fuzzing engines on different implementations simultaneously;
  * An obscure bug affecting `jsfuzz` preventing us from fuzzing the Lodestar when using containers.

We're hoping to have these resolved imminently and to start working on easy-
to-follow instructions for the community to participate in the Eth2 fuzzing
effort. Stay tuned for an exciting announcement over the coming days!

## Next Steps

Over the next few weeks, the Beacon Fuzz team will be looking into:

  * Finalising the dockerisation process
  * Fuzzing the p2p networking stack of the Eth2 clients
  * Working on the FFI bindings to complete the revamp in Rust
  * Start deploying our work to continuous fuzzing environments (OSS Fuzz)

[ __Twitter ](https://twitter.com/share?text=Beacon Fuzz - Update
#05&url=https://blog.sigmaprime.io/beacon-fuzz-05.html) [ __Facebook
](https://www.facebook.com/sharer/sharer.php?u=https://blog.sigmaprime.io/beacon-
fuzz-05.html) [ __Google+
](https://plus.google.com/share?url=https://blog.sigmaprime.io/beacon-
fuzz-05.html)

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

