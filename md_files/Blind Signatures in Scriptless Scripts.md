  * [![](/images/bird.png)](https://twitter.com/n1ckler "follow on twitter")
  * [![](/images/GitHub-Mark-64px.png)](https://github.com/jonasnick "github repo")
  * [![](/images/rss.png)](/atom.xml "subscribe via RSS")

  * [Blog](/)
  * [Code](https://github.com/jonasnick)
  * [About](/about)
  * [Archives](/blog/archives)

# Blind Signatures in Scriptless Scripts

Jul 31st, 2018

[![](/images/bob-youtube.png)](https://youtu.be/XORDEX-RrAI?t=25484)

At the recent Building on Bitcoin conference in Lisbon I gave a talk about a
few new ideas in the scriptless scripts framework. The first part was mainly
about [blind coinswaps](https://github.com/apoelstra/scriptless-
scripts/pull/1), which is a way to swap bitcoins with a tumbler without
revealing which coin are swapped. The second part about how to exchange ecash
tokens peer-to-peer using scriptless scripts and Brands credentials. You can
find the talk [on youtube](https://youtu.be/XORDEX-RrAI?t=25484) and the
slides [here](/slides/2018-bob.pdf). Thanks to
[kanzure](https://twitter.com/kanzure) there's also a
[transcript](https://diyhpl.us/wiki/transcripts/building-on-
bitcoin/2018/blind-signatures-and-scriptless-scripts/) of the talk.

EDIT: I've added a note about the security of Blind Schnorr signatures against
forgery to the [slides](/slides/2018-bob.pdf). In short, a naive
implementation of the scheme is vulnerable to [Wagner's
attack](http://www.enseignement.polytechnique.fr/informatique/profs/Francois.Morain/Master1/Crypto/projects/Wagner02.pdf).
An attacker can forge a signature using 65536 parallel signing sessions and
`O(2^32)` work.

Posted by Jonas Nick Jul 31st, 2018 [bitcoin](/blog/categories/bitcoin/),
[crypto](/blog/categories/crypto/), [lightning](/blog/categories/lightning/)

[« Exploiting Low Order Generators in One-Time Ring
Signatures](/blog/2017/05/23/exploiting-low-order-generators-in-one-time-ring-
signatures/ "Previous Post: Exploiting Low Order Generators in One-Time Ring
Signatures") [Schnorr and Taproot in Lightning »](/blog/2018/09/04/schnorr-
and-taproot-in-lightning/ "Next Post: Schnorr and Taproot in Lightning")

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

