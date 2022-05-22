  * [![](/images/bird.png)](https://twitter.com/n1ckler "follow on twitter")
  * [![](/images/GitHub-Mark-64px.png)](https://github.com/jonasnick "github repo")
  * [![](/images/rss.png)](/atom.xml "subscribe via RSS")

  * [Blog](/)
  * [Code](https://github.com/jonasnick)
  * [About](/about)
  * [Archives](/blog/archives)

# Secure Protocols on BIP-taproot

Jun 25th, 2019

[![](/images/2019-breaking.png)](https://youtu.be/DKOG0BQMmmg?t=21866)

At [Breaking Bitcoin](https://breaking-bitcoin.com/) 2019 in Amsterdam I gave
a talk about how to build secure protocols on BIP-taproot or more specifically
how to avoid the dangers we learned about so far. There was not enough time to
cover everything. The talk also gives an introduction to how to use our [MuSig
implementation in
libsecp256k1-zkp](https://github.com/ElementsProject/secp256k1-zkp/blob/secp256k1-zkp/include/secp256k1_musig.h).
The video recording is on [youtube](https://youtu.be/DKOG0BQMmmg?t=21866)
([slides](/slides/2019-breaking.pdf)). Thanks to
[kanzure](https://twitter.com/kanzure) there's also a
[transcript](https://diyhpl.us/wiki/transcripts/breaking-bitcoin/2019/secure-
protocols-bip-taproot/) of the talk.

**Erratum** : MuSig nonces can not be pre-shared. Only nonce commitments. See
<https://github.com/ElementsProject/secp256k1-zkp/pull/73> for details.

Posted by Jonas Nick Jun 25th, 2019 [bitcoin](/blog/categories/bitcoin/),
[crypto](/blog/categories/crypto/)

[« nix-bitcoin](/blog/2019/06/25/nix-bitcoin/ "Previous Post: nix-bitcoin")
[X-only Pubkeys and Insecure MuSig Shortcuts »](/blog/2019/11/19/x-only-
pubkeys-and-insecure-musig-shortcuts/ "Next Post: X-only Pubkeys and Insecure
MuSig Shortcuts")

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

