  * [![](/images/bird.png)](https://twitter.com/n1ckler "follow on twitter")
  * [![](/images/GitHub-Mark-64px.png)](https://github.com/jonasnick "github repo")
  * [![](/images/rss.png)](/atom.xml "subscribe via RSS")

  * [Blog](/)
  * [Code](https://github.com/jonasnick)
  * [About](/about)
  * [Archives](/blog/archives)

# Data-Driven De-Anonymization in Bitcoin

Jun 25th, 2016

[![](/images/zurich-youtube.png)](https://www.youtube.com/watch?v=HScK4pkDNds)

[**Slides**](/slides/2016-zurich-meetup.pdf)

**Abstract**

We analyse the performance of several clustering algorithms in the digital
peer- to-peer currency Bitcoin. Clustering in Bitcoin refers to the task of
finding addresses that belongs to the same wallet as a given address. In order
to assess the effectiveness of clustering strategies we exploit a vulner-
ability in the implementation of Connection Bloom Filtering to capture ground
truth data about 37,585 Bitcoin wallets and the addresses they own. In
addition to well-known clustering techniques, we introduce two new strategies,
apply them on addresses of the collected wallets and evaluate precision and
recall using the ground truth. Due to the nature of the Connection Bloom
Filtering vulnerability the data we collect is not without errors. We present
a method to correct the performance metrics in the presence of such
inaccuracies. Our results demonstrate that even modern wallet software can not
protect its users properly. Even with the most basic clustering technique
known as multi- input heuristic, an adversary can guess on average 68.59%
addresses of a victim. We show that this metric can be further improved by
combining several more sophisticated heuristics.

[**Read full thesis**](/papers/thesis.pdf)

Posted by Jonas Nick Jun 25th, 2016 [bitcoin](/blog/categories/bitcoin/),
[golang](/blog/categories/golang/)

[« A Validation-cost metric for Bitcoin](/blog/2015/12/13/validation-cost-
metric/ "Previous Post: A Validation-cost metric for Bitcoin") [The 2016
Backdoored Cryptocurrency Contest Winner
»](/blog/2016/08/31/the-2016-backdoored-cryptocurrency-contest-winner/ "Next
Post: The 2016 Backdoored Cryptocurrency Contest Winner")

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

