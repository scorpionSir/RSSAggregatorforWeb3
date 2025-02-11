  * [![](/images/bird.png)](https://twitter.com/n1ckler "follow on twitter")
  * [![](/images/GitHub-Mark-64px.png)](https://github.com/jonasnick "github repo")
  * [![](/images/rss.png)](/atom.xml "subscribe via RSS")

  * [Blog](/)
  * [Code](https://github.com/jonasnick)
  * [About](/about)
  * [Archives](/blog/archives)

# Fuzzing Bitcoin Consensus

May 9th, 2015

**TLDR** I ran [afl-fuzz](http://lcamtuf.coredump.cx/afl/) against
[libbitcoinconsensus](https://github.com/bitcoin/bitcoin/blob/15facb4aca75122b6ae0dcc6f6e112127e6a0e59/doc/release-
notes/release-notes-0.10.0.md#consensus-library) to discover interesting
Bitcoin scripts and used them to search for Bitcoin reimplementations
vulnerable to forking. This discovered [two
bugs](https://github.com/btcsuite/btcd/commit/f284b9b3947eb33b91e31deec74936855feed61f)
in [btcd](https://github.com/btcsuite/btcd) by Conformal. See the
[bitcoinconsensus_testcases
repository](https://github.com/jonasnick/bitcoinconsensus_testcases) for the
discovered Bitcoin scripts.

## Forks

One of the things that must not happen during regular Bitcoin operation are
_forks_. A fork occurs when there is a new block $B_{i+1}$ which is a valid
successor to block $B_i$ for some set of Bitcoin nodes $N_v$ and invalid for
the remaining nodes $N_{\neg v}$. Therefore, miners in $N_v$ will mine new
blocks on top of $B_{i+1}$ and miners in $N_{\neg v}$ will still mine on
$B_i$. As long as the majority of hashpower is in $N_{\neg v}$, the chain
divergence will be resolved after some time, because $N_{\neg v}$'s chain will
eventually get longer than $N_v$'s chain and then the nodes in $N_v$ will
switch to $N_{\neg v}$'s chain. This is due to the nature of the
[blockchain](https://en.bitcoin.it/wiki/Block_chain): nodes always trust the
longest valid chain (more exact: the chain with the most proof of work).

Consider for example the case of an update to the Bitcoin reference
implementation that [restricts valid signature
encodings](https://github.com/bitcoin/bips/blob/ced361de1d47c71e967430e17339be520b71bb1a/bip-0062.mediawiki#block-
validity). $N_v$ are the nodes running the old Bitcoin version and $N_{\neg
v}$ run the new version. As soon as the hash power of $N_{\neg v}$ exceeds
some threshold the new consensus rule can be safely activated. In the context
of Bitcoin updates this is called a
[softfork](https://en.bitcoin.it/wiki/Softfork): a valid block becomes invalid
in the new version. On the other hand, a
[hardfork](https://en.bitcoin.it/wiki/Hardfork) occurs when an invalid block
is valid in a new version, for example by [raising the maximum block size
limit](http://gavinandresen.ninja/time-to-roll-out-bigger-blocks). Then nodes
that run the old version are represented by $N_{\neg v}$. Even if the majority
of hashpower is in $N_v$, the nodes in $N_{\neg v}$ can never switch to
$N_v$'s chain because some blocks are invalid for them. Therefore, in the case
of a hardfork all nodes are required to update.

## Fuzzing

Forks in practice do not only happen deliberately because of updating
mechanisms but can also be triggered by
[bugs](https://github.com/bitcoin/bips/blob/master/bip-0050.mediawiki).
Bitcoin reimplementations such as libbitcoin, btcd, bitcore and toshi are
particularly vulnerable to these bugs because they have to match exactly the
behavior of the Bitcoin reference implementation. In order to abstract part of
the consensus critical code and allow other projects to use it, Bitcoin Core
developers created the [bitcoinconsensus
library](https://github.com/bitcoin/bitcoin/blob/15facb4aca75122b6ae0dcc6f6e112127e6a0e59/doc/release-
notes/release-notes-0.10.0.md#consensus-library). I am not aware of any
reimplementation that already adopted libbitcoinconsensus. Right now, it only
has a single function bitcoinconsensus_script_verify, which takes an output
[script](https://en.bitcoin.it/wiki/Script) and a transaction and returns if
the transaction is allowed to spend the output.

Among other conditions, a transaction is valid if the top stack item is
different from 0 after script execution. Bitcoin script is much more powerful
than just verifying signatures and therefore I was curious to find interesting
scripts, i.e. scripts that trigger unusual edge cases. I've recently heard
about successes with [afl-fuzz](http://lcamtuf.coredump.cx/afl/) whose
heuristic using code coverage seemed to be particularly well suited for the
task. Also, it has the capability to minimize a set of inputs such that the
code coverage stays the same. After fuzzing libbitcoinconsensus for two weeks
I supplied the inputs to btcd's
[txscript](https://github.com/btcsuite/btcd/tree/master/txscript), a
reimplementation in golang, and checked if the outputs differ.

## Btcd bugs

The first bug I found was in btcd's implementation of the OP_IFDUP opcode.
This opcode pushes the top stack element on the stack if it differs from 0.
Because of a type conversion in btcd, a stack element that exceeds 4 bytes
would have never been copied, which differs from bitcoinconsensus'
implementation of the opcode. The second bug concerned the representation of
the result of OP_EQUAL. This opcode compares the two top stack elements and
pushes the result on the stack. In Bitcoin Core, if the comparison fails an
empty byte array is pushed on the stack. Btcd however pushed a byte array
containing 0. This means that the following script would be valid in
bitcoinconsensus and invalid in btcd (Note that OP_0 pushes an empty byte
array to the stack):

    
    
    1
    

|

    
    
    OP_0 OP_0 OP_TRUE OP_EQUAL OP_EQUAL  
  
---|---  
  
Both bugs would have triggered hardforks. An attacker could simply broadcast a
transaction with the affected scripts and it would be mined subsequently. Btcd
would have not been able to include the block into its chain and would become
stuck on the last block. Therefore, an attacker could create a block on top of
btcd's chain paying a merchant running btcd without affecting his 'real' coins
on the main chain. Note that the attacker would not race against the hashpower
of Bitcoin miners.

Dave Collins from the btcd team fixed these issues very fast and additionally
improved the test coverage in Bitcoin Core for the
[affected](https://github.com/bitcoin/bitcoin/pull/6112) and
[more](https://github.com/bitcoin/bitcoin/pull/6075) opcodes. Additionally, he
was so kind to award me with 0.5 bitcoin for the find.

## Conclusion

You can find the result of the fuzzing, the code to produce them and test
reimplementation in the [bitcoinconsensus_testcases
repository](https://github.com/jonasnick/bitcoinconsensus_testcases). If you
are interested you can start fuzzing yourself and submit a pull request with
new scripts you found. Also, I've executed the testcases only with btcd and
bitcore so far.

Posted by Jonas Nick May 9th, 2015 [bitcoin](/blog/categories/bitcoin/),
[consensus](/blog/categories/consensus/)

[« Ethereum Bug Bounty Submissions](/blog/2015/03/17/ethereum-bug-bounty-
submissions/ "Previous Post: Ethereum Bug Bounty Submissions") [Can miners
exploit a block size increase? »](/blog/2015/06/23/can-miners-exploit-a-block-
size-increase/ "Next Post: Can miners exploit a block size increase?")

# Recent Posts

  * [MuSig2: Simple Two-Round Schnorr Multisignatures](/blog/2020/11/29/musig2-simple-two-round-schnorr-multisignatures/)
  * [BIP-{Schnorr,Taproot,Tapscript}](/blog/2020/11/29/bip-%7Bschnorr/)
  * [MuSig-DN: Schnorr Multisignatures with Verifiably Deterministic Nonces](/blog/2020/11/29/musig-dn-schnorr-multisignatures-with-verifiably-deterministic-nonces/)
  * [X-only Pubkeys and Insecure MuSig Shortcuts](/blog/2019/11/19/x-only-pubkeys-and-insecure-musig-shortcuts/)
  * [Secure protocols on BIP-taproot](/blog/2019/06/25/secure-protocols-on-bip-taproot/)

# Categories

[algo trading](/blog/categories/algo-trading) [Astar](/blog/categories/astar)
[bitcoin](/blog/categories/bitcoin) [blender](/blog/categories/blender)
[C](/blog/categories/c) [consensus](/blog/categories/consensus)
[Cpp](/blog/categories/cpp) [crypto](/blog/categories/crypto)
[cryptocurrencies](/blog/categories/cryptocurrencies)
[evolution](/blog/categories/evolution) [genetic
algorithms](/blog/categories/genetic-algorithms)
[golang](/blog/categories/golang) [java](/blog/categories/java)
[javascript](/blog/categories/javascript) [kinect](/blog/categories/kinect)
[LaTeX](/blog/categories/latex) [lightning](/blog/categories/lightning)
[machine learning](/blog/categories/machine-learning)
[MarioAI](/blog/categories/marioai) [monero](/blog/categories/monero)
[neuro](/blog/categories/neuro) [nix](/blog/categories/nix)
[pragmatics](/blog/categories/pragmatics) [privacy](/blog/categories/privacy)
[Psycholinguistics](/blog/categories/psycholinguistics)
[python](/blog/categories/python) [R](/blog/categories/r)
[racket](/blog/categories/racket) [regression](/blog/categories/regression)
[security](/blog/categories/security) [signaling
games](/blog/categories/signaling-games) [snake](/blog/categories/snake)
[source engine](/blog/categories/source-engine)
[Sweave](/blog/categories/sweave)

This work is licensed under a [Creative Commons Attribution 3.0 Unported
License](https://creativecommons.org/licenses/by/3.0/deed.en_US). 2022 - Jonas
Nick - Powered by [Octopress](https://octopress.org)

