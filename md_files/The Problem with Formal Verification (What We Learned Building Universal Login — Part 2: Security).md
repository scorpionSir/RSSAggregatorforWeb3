[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/2e49ca4e7319&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![UniLogin](https://miro.medium.com/fit/c/64/64/1*pbXgdMyIerXmHIJzLcj0Tg.png)](https://medium.com/universal-
ethereum?source=post_page-----2e49ca4e7319--------------------------------)

Published in

[UniLogin

](https://medium.com/universal-ethereum?source=post_page-----
2e49ca4e7319--------------------------------)

[![Marek
Kirejczyk](https://miro.medium.com/fit/c/96/96/0*QVEwR2ZHvUmeVXCv.png)](/@marekkirejczyk?source=post_page
-----2e49ca4e7319--------------------------------)

[Marek Kirejczyk](/@marekkirejczyk?source=post_page-----
2e49ca4e7319--------------------------------)

Follow

Feb 3, 2020

·

6 min read

# The Problem with Formal Verification

## What We Learned Building Universal Login — Part 2: Security

![](https://miro.medium.com/max/1400/1*hnOxSPce9XNdN1qW1AWucQ.png)

This is the second blog post in a series “What We Learned Building Universal
Login”:

  * [Part 1: The Problem](/universal-ethereum/what-we-learned-building-universal-login-part-1-the-problem-6098d600e127)
  *  **Part 2: Security**
  * Part 3: Developer Experience (coming soon!)
  * Part 4: User Experience (coming soon!)

# TL;DR

To solve onboarding, one needs to solve the security aspect of it. Our
takeaways are:

  * To avoid single points of failure, build an ecosystem rather than a single app/API provider
  * In this use-case, security of smart-contracts is even more crucial than usual
  * Formal verification fails, because it is too unstable and expensive, and it forces you to do write-once rather than ongoing development
  * Gnosis safe contract fits our requirements perfectly and comes with bonuses
  * So now we can better focus on our core: solving onboarding, with the best possible UX and dev experience

# Security

As described in [part 1 of this series](/universal-ethereum/what-we-learned-
building-universal-login-part-1-the-problem-6098d600e127), **security** is one
of three sets of challenges to solve user onboarding to Ethereum (the other
two are user experience and developer experience) and it consist of many
smaller sub-problems, each affecting each other:

  * Private key getting lost or stolen leads to loss of funds
  * A single smart contract’s vulnerability can lead to catastrophic failure
  * Solving onboarding also means solving the custodial vs. non-custodial trade-off. Custodial: can be easy to use, but funds are only as secure as your custodian. Non-custodial: hard to use, as secure as your setup, but not easy to properly secure.
  * Finally, once you solve all of those problems, you need to explain how it all works and build a brand that people trust.

# No single point of failure

Our general philosophy around solving security is to avoid a single point of
failure (SPOF) as much as possible, by using a multisig wallet.

[🔑](https://emojipedia.org/key/) Private key lost? — no problem you store
multiple keys on different devices, you can use other devices to reconnect to
your funds

[🔑](https://emojipedia.org/key/) Private key stolen? — no problem, each key
has limited permissions (once the amount of money is big enough to justify
extra security)

 **But what about other SPOFs?**

[🔒](https://emojipedia.org/locked/) custodian (a 3rd party that stores funds)  
[🔒](https://emojipedia.org/locked/) application (a wallet or dapp potentially
hackable)  
[🔒](https://emojipedia.org/locked/) domain (vulnerable to hijacking)  
[🔒](https://emojipedia.org/locked/) etc

# Ecosystem

The problem with multisig wallets, so far, was that they were too hard to use.
That is why our goal is to use a thriving ecosystem of apps and wallets. Each
one of them can increase your safety.

 **The key to solve onboarding is not to build a dapp or a smart wallet. It is
to build a secure ecosystem. That is the only way to avoid a single point of
failure in the long run.**

That also solves the custodial vs non-custodial paradox.

That, unfortunately, leaves one potential point of failure: the smart
contract.

# The smart contracts

To ensure no single vulnerability in a smart contract is a key to build a
multisig. We were very aware of this critical problem from the very beginning.

From the first days of our research, we were investing heavily in security.
Our first approach was to use formal verification.

# Formal verification

We assumed that with formal verification (FV):

  * we could move fast with confidence (by doing ongoing formal verification as we kept developing smart contracts)
  * we could hire a person in-house to work on it to propagate necessary skills within the team

Soon Tomasz, a PhD in computer science, with specialization in blockchain and
a background in formal verification, joined our team.

We used a well tested technological stack: K (formal verification language),
KEVM (EVM specification in K), and ACT (high-level specification language
build by DApphub — a team working on formal verification of Maker).

![](https://miro.medium.com/max/1400/0*x4jKDeFCNNQNbeL3.png)

The ecosystem for creating proofs on EVM

As a by-product of that work with co-op with Tomek, I wrote a series of blog
posts on formal verification available here: part [1](/ethworks/formal-
verification-for-n00bs-part-1-b4781db2a383), [2](/ethworks/formal-
verification-for-n00bs-part-2-proving-the-correctness-of-a-
token-74085f5cd6c1), [3](/ethworks/formal-verification-for-n00bs-part-3-an-
attempt-to-prevent-classic-hack-with-klab-8e8d13318086), [4](/ethworks/formal-
verification-for-n00bs-part-4-understanding-k-language-6069c20cfd47).

Our initial work showed much promise: in 2–3 months, we learned basics of
formal verification, formally proved one of the critical contracts (KeyHolder
that store keys), and added formal verification to our continuous integration.

Boy, we thought we had it solved! We were wrong.

# Challenges of Formal Verification

Unfortunately, in the fourth month, we realized we were far from success, as
problems started to pile up:

  * proving loops and signatures turned out to be quite challenging
  * the formal verification started taking more and more time (before it was launched after each commit, now only at night)
  * we have to keep adding additional code to smart-contracts to make FV work
  * small changes in code could result in significant changes in proofs
  * small changes in proofs could lead to significant changes in the speed of verification

> Swap _a+b_ to _b+a_ in a proof could add (or subtract) an extra hour to your
> proving time

By the end of the fourth month, formally verifying one not-too-complicated
contract would take close to four hours. It was maybe 10% of our solidity code
base.

 **It was becoming evident that:**

  *  **you need to modify your code and fine-tune proofs heavily to make it work at all**
  *  **continuous formal verification is too troublesome to be cost-effective**

>  **To work effectively with FV, one has to use a “write once, verify once”
> approach, rather than ongoing verification**

We also learned that other teams using formal verification were running into
other significant problems:

  * they verify most of the code automatically while leaving the hardest parts to manual formal verification on paper
  * a small bug in proofs could lead to falsely verified code

And so we decided to investigate other approaches that would give us
confidence and allow us to iterate faster.

# Gnosis Safe

Gnosis Safe — a smart wallet contract- was a source for inspiration for us
from the very beginning.

![](https://miro.medium.com/max/1400/0*EROmAMLgvtuPzCfg.png)

As we were running pilots and gaining understanding of what is it that users
and developers need, we discovered that Gnosis Safe contracts matured and they
were very aligned with what we are building.

>  _Gnosis Safe, smart contracts were built by a rock-solid team, formally
> verified by authors of K, audited, and battle-tested. Moreover, they have
> almost all the functionalities we would like to build in the upcoming
> months._

# Bonus

Gnosis Safe comes with a bunch of additional benefits:

  *  **The brand:** It takes time and testing to convince people that your smart contract code is safe. Gnosis Safe has already done that.
  *  **Modules:** That allow extending functionality. A bunch of great modules already exist.

> Thanks to Gnosis Safe contracts, Universal Login starting day one has
> support for great features like state channels and daily limits.

# What’s next?

Security is just a part of a puzzle. Even the best security is worth nothing
without adoption.

Before you can build adoption among users, you have to build adoption among
developers. And so, user experience and developer experience are the topics of
the next two posts in the series. Stay tuned.

# Follow us!

To make sure you don’t miss the next posts in the series, follow us
[Medium](https://medium.com/universal-ethereum) and
[Twitter](https://twitter.com/unilogin).

# Pilot program

Still not signed-up for our Beta program? Fix it!

[Join our Pilot program](http://tiny.cc/unilogin) 👮🏽 🛩

\--

\--

\--

## [More from UniLogin](/universal-ethereum?source=post_page-----
2e49ca4e7319--------------------------------)

The best user onboarding solution for Ethereum dapps.

[Read more from UniLogin](/universal-ethereum?source=post_page-----
2e49ca4e7319--------------------------------)

## Recommended from Medium

[[![Patrick
OConnell](https://miro.medium.com/fit/c/40/40/1*ZsISKsgfyqXvjosiRwJuww.jpeg)](/@PatrickOConnellNM?source=post_internal_links
---------0----------------------------)

[Patrick OConnell

](/@PatrickOConnellNM?source=post_internal_links---------
0----------------------------)

## How Blockchain Technology Might Enhance Travel Trust& Authenticity In The
Travel Experience

![Picture with word
“Blockchain”](https://miro.medium.com/focal/112/112/50/50/0*bswFi224NsylxCYI)](/@PatrickOConnellNM/how-
blockchain-technology-might-enhance-travel-trust-authenticity-in-the-travel-
experience-dd721fc266e1?source=post_internal_links---------
0----------------------------)

[[![ælf](https://miro.medium.com/fit/c/40/40/1*jwUViMDcHsDSMZvA5vrYNw.png)](/@aelfblockchain?source=post_internal_links
---------1----------------------------)

[ælf

](/@aelfblockchain?source=post_internal_links---------
1----------------------------)

in

[aelf

](https://medium.com/aelfblockchain?source=post_internal_links---------
1----------------------------)

## Official AMA Recap — Featuring aelf CEO & COO

![](https://miro.medium.com/focal/112/112/50/50/1*WcsyOhdME_L9zhhfy5A_Ow.png)](/aelfblockchain/official-
ama-recap-featuring-aelf-ceo-coo-2b7d16d738ce?source=post_internal_links
---------1----------------------------)

[[![Kinesis
Money](https://miro.medium.com/fit/c/40/40/1*i5LaQ6VWS3J9WilWsZpLYQ.png)](/@kinesis-
money?source=post_internal_links---------2----------------------------)

[Kinesis Money

](/@kinesis-money?source=post_internal_links---------
2----------------------------)

## An Insight Into The Kinesis Blockchain

![](https://miro.medium.com/focal/112/112/50/50/1*sh9KEn5Yyisa_lZiXEPLjg.jpeg)](/@kinesis-
money/kinesis-blockchain-insight-b14284e620ad?source=post_internal_links
---------2----------------------------)

[[![Wulf Kaal](https://miro.medium.com/fit/c/40/40/1*rRQQrlP-
McHlxFDJU9iAnQ.jpeg)](/@wulfkaal?source=post_internal_links---------
3----------------------------)

[Wulf Kaal

](/@wulfkaal?source=post_internal_links---------3----------------------------)

## Blockchain Innovation for the Hedge Fund Industry

![](https://miro.medium.com/focal/112/112/50/50/1*vnLi4iprNtniZYuqwAZzXg.jpeg)](/@wulfkaal/blockchain-
innovation-for-the-hedge-fund-industry-cc4ae59eaaf?source=post_internal_links
---------3----------------------------)

[[![BlockPegnio
Insights](https://miro.medium.com/fit/c/40/40/2*ZhqfN_HKYZhKnju6HC_xNQ.png)](/@blockpegnioltd?source=post_internal_links
---------4----------------------------)

[BlockPegnio Insights

](/@blockpegnioltd?source=post_internal_links---------
4----------------------------)

in

[BlockPegnio

](https://medium.com/blockpegnio?source=post_internal_links---------
4----------------------------)

## BlockPegnio integrates Chainlink’s Oracles for on-chain verified randomness
in game interactions

![](https://miro.medium.com/focal/112/112/50/50/1*0yOjE3qtegOY6gnGdX8ECg.png)](/blockpegnio/blockpegnio-
integrates-chainlinks-oracles-for-on-chain-verified-randomness-in-game-
interactions-96cef98dcafb?source=post_internal_links---------
4----------------------------)

[[![Scott A. Joseph](https://miro.medium.com/fit/c/40/40/1*Unjf7-UB-
lUq63lh3gHuNg.png)](/@globalscotty?source=post_internal_links---------
5----------------------------)

[Scott A. Joseph

](/@globalscotty?source=post_internal_links---------
5----------------------------)

in

[Another Block In The Chain

](https://medium.com/another-block-in-the-chain?source=post_internal_links
---------5----------------------------)

## Asia: Driving The Adoption Of Security Tokens

![](https://miro.medium.com/focal/112/112/50/50/0*8MLv6J910TH1sToi)](/another-
block-in-the-chain/asia-driving-the-adoption-of-security-
tokens-521a11673794?source=post_internal_links---------
5----------------------------)

[[![Synapse Network](https://miro.medium.com/fit/c/40/40/1*M6kjZyDy_X4B--
Z7ar76ZQ.png)](/@synapsenetwork?source=post_internal_links---------
6----------------------------)

[Synapse Network

](/@synapsenetwork?source=post_internal_links---------
6----------------------------)

## The Synapse Network enters Polygon!

![](https://miro.medium.com/focal/112/112/50/50/1*I2Izm8DdsicrcE_AvR9LoA.png)](/@synapsenetwork/the-
synapse-network-enters-polygon-843462b4ba54?source=post_internal_links
---------6----------------------------)

[[![HaMech](https://miro.medium.com/fit/c/40/40/1*rQ3aQ6VF2M2PhNVyGjw2rA.jpeg)](/@hamech?source=post_internal_links
---------7----------------------------)

[HaMech

](/@hamech?source=post_internal_links---------7----------------------------)

in

[CryptoStars

](https://medium.com/cryptostars?source=post_internal_links---------
7----------------------------)

## The simplest way to understand Blockchain

![](https://miro.medium.com/focal/112/112/50/50/0*K-wEKrn2NM2qW-l5)](/cryptostars/the-
simplest-way-to-understand-blockchain-dff97e699908?source=post_internal_links
---------7----------------------------)

[](/?source=post_page-----2e49ca4e7319--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
2e49ca4e7319--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
2e49ca4e7319--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
2e49ca4e7319--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
2e49ca4e7319--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----2e49ca4e7319--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----2e49ca4e7319--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Funiversal-
ethereum%2Fwhat-we-learned-building-universal-login-
part-1-security-2e49ca4e7319&source=post_page--------------------------
nav_reg-----------)

[![Marek
Kirejczyk](https://miro.medium.com/fit/c/176/176/0*QVEwR2ZHvUmeVXCv.png)](/@marekkirejczyk)

[

## Marek Kirejczyk

](/@marekkirejczyk)

1.94K Followers

Ethereum blockchain Engineer. Ethworks, Universal Login.

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F6e6d213135fd&operation=register&redirect=https%3A%2F%2Fmedium.com%2Funiversal-
ethereum%2Fwhat-we-learned-building-universal-login-
part-1-security-2e49ca4e7319&newsletterV3=1ad34b4ecc2e&newsletterV3Id=6e6d213135fd&user=Marek+Kirejczyk&userId=1ad34b4ecc2e&source=--------------------------subscribe_user-----------)

## More from Medium

[[![SlowMist](https://miro.medium.com/fit/c/40/40/1*IMpTvjP5XQImlGDZYxVV5g.png)](/@slowmist?source=read_next_recirc
---------0---------------------e1eaa3b9_efc5_4551_b720_9c73777160bd-------)

[SlowMist

](/@slowmist?source=read_next_recirc---------0---------------------
e1eaa3b9_efc5_4551_b720_9c73777160bd-------)

## Crypto Compliance Series| What is Peel Chain

![](https://miro.medium.com/focal/112/112/50/50/1*vmIXhlScBsdzEacGO2lbHQ.png)](/@slowmist/crypto-
compliance-series-what-is-peel-chain-7b5be0bb7214?source=read_next_recirc
---------0---------------------e1eaa3b9_efc5_4551_b720_9c73777160bd-------)

[[![Zoumana
Cisse](https://miro.medium.com/fit/c/40/40/1*6IxBVXBYLv_ZJl346aJ9ow@2x.jpeg)](/@zouvier?source=read_next_recirc
---------1---------------------e1eaa3b9_efc5_4551_b720_9c73777160bd-------)

[Zoumana Cisse

](/@zouvier?source=read_next_recirc---------1---------------------
e1eaa3b9_efc5_4551_b720_9c73777160bd-------)

in

[Block Magnates

](https://medium.com/block-magnates?source=read_next_recirc---------1
---------------------e1eaa3b9_efc5_4551_b720_9c73777160bd-------)

## Beating Ethernaut: level 8 Vault

![](https://miro.medium.com/focal/112/112/69/51/0*6K5Z-Xio2todYp5o.jpg)](/block-
magnates/beating-ethernaut-level-8-vault-f34ae9556c03?source=read_next_recirc
---------1---------------------e1eaa3b9_efc5_4551_b720_9c73777160bd-------)

[[![StErMi](https://miro.medium.com/fit/c/40/40/2*mDoMM6mrDi13fMu427FK9A.jpeg)](/@stermi?source=read_next_recirc
---------2---------------------e1eaa3b9_efc5_4551_b720_9c73777160bd-------)

[StErMi

](/@stermi?source=read_next_recirc---------2---------------------
e1eaa3b9_efc5_4551_b720_9c73777160bd-------)

## Damn Vulnerable DeFi Challenge #2 Solution — Naive receiver

](/@stermi/damn-vulnerable-defi-challenge-2-solution-naive-
receiver-341376fdc967?source=read_next_recirc---------2---------------------
e1eaa3b9_efc5_4551_b720_9c73777160bd-------)

[[![OLUWADAMILOLA](https://miro.medium.com/fit/c/40/40/1*rozx3yMzWcGVro3AKL9HuA@2x.jpeg)](/@dameeolawuyi?source=read_next_recirc
---------3---------------------e1eaa3b9_efc5_4551_b720_9c73777160bd-------)

[OLUWADAMILOLA

](/@dameeolawuyi?source=read_next_recirc---------3---------------------
e1eaa3b9_efc5_4551_b720_9c73777160bd-------)

in

[Coinmonks

](https://medium.com/coinmonks?source=read_next_recirc---------3
---------------------e1eaa3b9_efc5_4551_b720_9c73777160bd-------)

## What The Heck is Value Types In Solidity And Why Should You Care?

![](https://miro.medium.com/focal/112/112/50/50/1*Mh-
BL4JI_9aqYFUvCympWQ@2x.jpeg)](/coinmonks/what-the-heck-is-values-types-in-
solidity-and-why-should-you-care-6ea676441e70?source=read_next_recirc---------
3---------------------e1eaa3b9_efc5_4551_b720_9c73777160bd-------)

[Help

](https://help.medium.com/hc/en-us)

[Status

](https://medium.statuspage.io)

[Writers

](https://about.medium.com/creators/)

[Blog

](https://blog.medium.com)

[Careers

](/jobs-at-medium/work-at-medium-959d1a85284e)

[Privacy

](https://policy.medium.com/medium-privacy-policy-f03bf92035c9)

[Terms

](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f)

[About

](https://medium.com/about?autoplay=1)

[Knowable

](https://knowable.fyi)

