Close

Menu

  * [About Us](https://blog.sigmaprime.io/pages/about-us.html)

[![Blog Logo](./imgs/blog/sigp-logo-black.png)](https://blog.sigmaprime.io/)
__Menu

# Beacon Fuzz - Update #06

[Mehdi Zerouali](https://blog.sigmaprime.io/author/mehdi-zerouali.html) | Sun
12 July 2020 Estimated read time: 4 min Image credits: [Photo by Hans-Peter
Gauster](https://unsplash.com/@sloppyperfectionist)

_Beacon Fuzz - Progress Update #6:_  
_Community fuzzing, new bugs and next steps_

# Beacon Fuzz - Update #06  
  

Sigma Prime is leading the development and maintenance of [beacon-
fuzz](https://github.com/sigp/beacon-fuzz), a differential fuzzing solution
for Eth2 clients. This post is part of our series of status updates where we
discuss current progress, interesting challenges encountered and direction for
future work. See [#00](https://blog.sigmaprime.io/beacon-fuzz.html) and the
repository's [README](https://github.com/sigp/beacon-
fuzz/blob/master/README.md) for more context.

## Summary

  * Community Fuzzing
  * New Bugs
  * Next Steps

## Community Fuzzing

We're happy to announce that the _dockerisation_ process of our `eth2fuzz`
tool is now complete! If you'd like to help catch bugs on the major Eth2
implementations on your own hardware or cloud infrastructure, you can now
follow these simple steps:

  1. Clone the `beacon-fuzz` repository:
    * `git clone https://github.com/sigp/beacon-fuzz`
  2. Change your current directory to `eth2fuzz`:
    * `cd beacon-fuzz/eth2fuzz`
  3. Make sure the Docker service is running on your machine
    * For Linux hosts using `systemd`: `sudo systemctl start docker`
  4. Build the fuzzing container for any given Eth2 client (we currently support Lighthouse, Nimbus, Prysm, Teku and Lodestar):
    * For example, if you want to fuzz Prysm: `make prysm`

Congratulations, you now have successfully built a Docker container that holds
everything you need to fuzz the Prysm client's state transition functions! Use
the `help` function to get a list of available commands:

    
    
    docker run -it -v `pwd`/workspace:/eth2fuzz/workspace eth2fuzz_prysm help
    

If you'd like to see all the fuzzing targets available on the Docker you've
just built, run the following command:

    
    
    docker run -it -v `pwd`/workspace:/eth2fuzz/workspace eth2fuzz_prysm list
    

The output should be:

    
    
    prysm_attestation
    prysm_attester_slashing
    prysm_block
    prysm_block_header
    prysm_deposit
    prysm_proposer_slashing
    prysm_voluntary_exit
    

For example, to start fuzzing the attestation processing function:

    
    
    docker run -it -v `pwd`/workspace:/eth2fuzz/workspace eth2fuzz_prysm target prysm_attestation
    

The `eth2fuzz` [README](https://github.com/sigp/beacon-
fuzz/blob/master/eth2fuzz/README.md) contains detailed instructions and
explanations on what is currently supported:

  * **Continuous fuzzing** : `eth2fuzz` can be configured to continuously fuzz all available targets for a given client, using the `continuously` CLI parameter. Alternatively, you can use the `Makefile` to fuzz all targets, each one running during 1 hour. For example, `make fuzz-nimbus` will build the relevant fuzzing container and exercise all fuzzing harnesses.
  * **Fuzzing all clients** : Want to fuzz all clients on all targets? Use the `make fuzz-all` command which will go through all clients and all implementations (and stop as soon as a bug is identified when using libFuzzer), dedicating 1 hour for each target, per client.
  * **Different fuzzing engine support** : For some clients, we support different fuzzing engines (Afl, Honggfuzz, libFuzzer). Depending on the implementation you're targeting, you can switch to a different fuzzer (libFuzzer is the default), which will enable different mutations. More fuzzing engines will be added in the near future!

We'd like to thank Justin Drake for suggesting this initiative and helping us
with testing it!

If you find a bug during your fuzzing adventures, or if you encounter any
issues with `eth2fuzz`, join our `beacon-fuzz` [Discord
channel](https://discord.gg/AkPb4vx) on the Sigma Prime server and drop us a
message!

## New Bugs

Our fuzzing effort over the last month have resulted in the idenfitication of
the following bugs:

  * **Nimbus:** `IndexError` bug in the the attester slashing processing function: Due to insufficient input validation when calling `isValidAttestation()`, this externally trigerrable vulnerability could lead to a crash of the client (refer to [this issue](https://github.com/status-im/nim-beacon-chain/issues/1207) for more details). This vulnerability has since been fixed by the Nimbus development team (see [this Pull Request](https://github.com/status-im/nim-beacon-chain/pull/1214)).
  * **Lodestar:** Memory exhaustion vulnerability when parsing invalid ENRs: when providing a maliciously crafted ENR string, we can trigger a JavaScript heap _out-of-memory_ error, which can lead to a Denial-of-Service condition (refer to [this issue](https://github.com/ChainSafe/discv5/issues/64) for more details).

## Next Steps

As the Eth2 state transition specification can most likely now be considered
final, we're shifting our efforts to the differential part of our fuzzing
infrastructure.

![coverage](./imgs/beacon-fuzz/diagram-update.svg)

`eth2fuzz` and `eth2diff` can now be considered complete (a few more features
and improvements will however be added). These tools allowed us to identify
**[26 unique bugs](https://github.com/sigp/beacon-fuzz#trophies)** across
**every** Eth2 implementation.

Most of our time over the upcoming weeks will be spent on `beacon-fuzz-2`, to
leverage Foreign Function Interfaces (FFI) in order to identify state
transition discrepancies that would cause network splits and chain forks. A
detailed overview of our fuzzing architecture for Eth2 can be found in a
[previous post](https://blog.sigmaprime.io/beacon-fuzz-04.html).

We will also be accelerating our efforts on fuzzing the various p2p networking
stacks.

[ __Twitter ](https://twitter.com/share?text=Beacon Fuzz - Update
#06&url=https://blog.sigmaprime.io/beacon-fuzz-06.html) [ __Facebook
](https://www.facebook.com/sharer/sharer.php?u=https://blog.sigmaprime.io/beacon-
fuzz-06.html) [ __Google+
](https://plus.google.com/share?url=https://blog.sigmaprime.io/beacon-
fuzz-06.html)

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

