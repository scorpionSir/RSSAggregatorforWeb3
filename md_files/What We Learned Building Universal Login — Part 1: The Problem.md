[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/6098d600e127&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![UniLogin](https://miro.medium.com/fit/c/64/64/1*pbXgdMyIerXmHIJzLcj0Tg.png)](https://medium.com/universal-
ethereum?source=post_page-----6098d600e127--------------------------------)

Published in

[UniLogin

](https://medium.com/universal-ethereum?source=post_page-----
6098d600e127--------------------------------)

[![Marek
Kirejczyk](https://miro.medium.com/fit/c/96/96/0*QVEwR2ZHvUmeVXCv.png)](/@marekkirejczyk?source=post_page
-----6098d600e127--------------------------------)

[Marek Kirejczyk](/@marekkirejczyk?source=post_page-----
6098d600e127--------------------------------)

Follow

Jan 20, 2020

·

4 min read

# What We Learned Building Universal Login — Part 1: The Problem

![](https://miro.medium.com/max/1400/1*PwU7-ZauqAk1_KJPuWndsw.png)

Ethereum conferences are the heartbeat of the ecosystem: Universal Login
started as an idea at EDCON Toronto, found a team at Dappcon, was launched as
a company at Devcon, **so we’ll be proud to be at this years**[
**ETHDenver**](https://medium.com/u/79079ae79889?source=post_page-----
6098d600e127--------------------------------) **, talking about the lessons we
learned and the next steps on the project.**

Defining the problem you want to solve often sounds simple, but in fact it’s
often the most complicated part of trying to solve it. In this post we want to
talk about our journey on figuring out the real issues that plague onboarding
users to Ethereum apps.

In the next few posts, we hope to talk about how we are doing on security,
user experience and—equally important—developer experience. To follow these,
follow our series or **simply watch**[ **our ETHDENVER
talk**](http://www.ethdenver.com) **!**

We started Universal Login as a research project in summer 2018, over a year
ago. Some would say it is a long time in blockchain space, but for us, it felt
short and intense. We BUIDLed, we tested, we learned, and pivoted — a lot.

#  **The Goal**

We started with a clear goal: to onboard the first one billion users to the
essential part of the blockchain ecosystem: dapps.

We call it, for short: **solving onboarding**.

# The Challenge

We are living in a hermetic and relatively small blockchain community. It is
easy to forget how hard it is for a non-tech-savvy user to use dapps. If you
are a dapp developer, you are probably aware that any marketing effort pointed
outside of the blockchain community is pointless. The moment you want to
activate users, conversions cut down to almost zero.

![](https://miro.medium.com/max/1400/1*18N1IL1rO1cvOMMujU7ytQ.png)

The Awesome Blockchain Project Funnel vs dapp

There has been great improvement in usability in the blockchain space since we
started, but the fundamental onboarding problem is still not solved.

![](https://miro.medium.com/max/1400/1*ChQMODjiPIhkGyxZYECVrw.png)

Solving onboarding is confusing and feels bad sometimes, but it is a problem
that we need to solve.

We thought we solved it, we thought we nailed it — so many times. And boy, we
were wrong.

It turns out that solving __ onboarding consists of many sub-problems. It is
like inception: you solve one problem, another pops up. You have to go deeper.

![](https://miro.medium.com/max/1140/0*g7vIRdHsOJ5wLBPB.jpg)

Solving onboarding forces you to go deeper again and again

Below is a list of some of the sub-problems we found along the way, grouped
into major categories. Some were more obvious, others less so.

#  **Funds Security**

  * Private key getting lost or stolen leads to loss of funds
  * A single smart contract’s vulnerability can lead to catastrophic failure
  * Solving onboarding also means solving the custodial vs. non-custodial trade-off. Custodial: can be easy to use, but funds are only as secure as your custodian. Non-custodial: hard to use, as secure as your setup, but not easy to properly secure.
  * Finally, once you solve all of those problems, you need to explain how it all works and build a brand that people trust.

#  **User Experience**

  * The mental model of blockchain is complicated with private keys, gas fees, and transactions that can succeed or fail
  * Transactions are slow, and you need to do many of them to perform basic actions (i.e., famous ERC20 approve and transferFrom example). That is not what mainstream users are used to.
  * Buying cryptocurrency is hard, as it requires many steps with registrations, KYC, custom software installations, etc.

#  **Developer Experience**

  * As a dapp developer, you find yourself spending time solving UX challenges instead of working on your core application.
  * Implementing good onboarding flow and optimizing it takes months of developments, with on-ramp integrations and tackling edge cases.
  * The blockchain development model is surprisingly complicated in comparison to Web and Mobile development. And I am not even talking about security of smart-contracts or front-running. Rather about stuff like:  
[👷](https://www.compart.com/en/unicode/U+1F477)Constructing an application
state based on multiple sources: blockchain state, blockchain events, and
database; reacting to state changes and edge-cases like network reorgs. As
your application become successful it all becomes part of the game.  
[👷](https://www.compart.com/en/unicode/U+1F477) Handling waiting for
transactions, gas parameters, failed transactions.  
[👷](https://www.compart.com/en/unicode/U+1F477) Occasionally looking at te
mempool to give feedback on what is going on with their transaction.  
[👷](https://www.compart.com/en/unicode/U+1F477)And there is only more stuff
coming all the time with half a dozen of L2 solutions being around the corner

  * The main takeaway is: Onboarding solutions should not add complexity to the development model, they should simplify it.

The answer to each of the sub-problem affects other sub-problems, while every
single one of sub-problem can make all other solutions irrelevant.

![](https://miro.medium.com/max/960/1*3F_5wtzxzHrTS8rn-17_JA.gif)

What solving onboarding feels like

I am pretty sure each of those problems is going to be obvious looking
backward, but none of those problems are easy now. We can see many attempts,
but none of them fully solve onboarding yet. We believe the solution is around
the corner. We believe we have found a way.

We will explain how we solve onboarding, its sub-problems and what we have
learned in next posts in the series. Stay tuned!

 **Follow us on**[ **Medium**](https://medium.com/universal-ethereum) **and**[
**Twitter**](https://twitter.com/unilogin) **and sign-up to our**[ **pilot
program**](http://tiny.cc/unilogin) **.**

\--

1

\--

\--

1

## [More from UniLogin](/universal-ethereum?source=post_page-----
6098d600e127--------------------------------)

The best user onboarding solution for Ethereum dapps.

[Read more from UniLogin](/universal-ethereum?source=post_page-----
6098d600e127--------------------------------)

## Recommended from Medium

[[![Centralex](https://miro.medium.com/fit/c/40/40/1*pVGh9pUYfRAhh_nDUvEpwQ.png)](/@centralex?source=post_internal_links
---------0----------------------------)

[Centralex

](/@centralex?source=post_internal_links---------
0----------------------------)

## Crypto-DeFi, an AMA with Decentralized Club

![](https://miro.medium.com/focal/112/112/50/50/1*6Nj-
QR6OD_gunBNSFJaSrQ.png)](/@centralex/crypto-defi-an-ama-with-decentralized-
club-747f3f838b05?source=post_internal_links---------
0----------------------------)

[[![New
Alchemy](https://miro.medium.com/fit/c/40/40/1*ssooLxDf4CVM5uB-M5f4ag.jpeg)](/@newalchemy?source=post_internal_links
---------1----------------------------)

[New Alchemy

](/@newalchemy?source=post_internal_links---------
1----------------------------)

in

[New Alchemy

](https://medium.com/new-alchemy?source=post_internal_links---------
1----------------------------)

## The Abyss DAICO Smart Contract Audit (New)

![](https://miro.medium.com/focal/112/112/50/50/1*XMnO6IpgN0kDIsB5d5ngoQ.png)](/new-
alchemy/the-abyss-daico-smart-contract-audit-
new-d0717ef9c838?source=post_internal_links---------
1----------------------------)

[[![SONM](https://miro.medium.com/fit/c/40/40/1*JkmZc7poyCeSaM3mfWtg4A.png)](/@sonm?source=post_internal_links
---------2----------------------------)

[SONM

](/@sonm?source=post_internal_links---------2----------------------------)

in

[SONM

](https://medium.com/sonm?source=post_internal_links---------
2----------------------------)

## Decentralized Computing on Ethereum Smart - Contracts is Gaining Momentum

![](https://miro.medium.com/focal/112/112/50/50/1*xcxhV-
RtEgVxcyC7MiRPAg.png)](/sonm/decentralized-computing-is-gaining-
momentum-c921f75e2a5c?source=post_internal_links---------
2----------------------------)

[[![Atlo](https://miro.medium.com/fit/c/40/40/1*XEXFQjKNIV0fla5FDyRUAA.png)](/@atlo?source=post_internal_links
---------3----------------------------)

[Atlo

](/@atlo?source=post_internal_links---------3----------------------------)

## INTRO TO TERRNADO

![](https://miro.medium.com/focal/112/112/50/50/1*CgFZdqusGPvRCnnTfbTI7w.png)](/@atlo/intro-
to-terrnado-d74e71b24ab7?source=post_internal_links---------
3----------------------------)

[[![Manti
Tarak](https://miro.medium.com/fit/c/40/40/1*80ujuOX3RkOcyja0UOCFyQ.jpeg)](/@mantitarak?source=post_internal_links
---------4----------------------------)

[Manti Tarak

](/@mantitarak?source=post_internal_links---------
4----------------------------)

## STABILA Public Blockchain Project Focused on Financial Security

![](https://miro.medium.com/focal/112/112/50/50/1*Qnm30i9dYrr71Kqb7ZO6kQ.png)](/@mantitarak/stabila-
public-blockchain-project-focused-on-financial-
security-f89f5a43a650?source=post_internal_links---------
4----------------------------)

[[![Khilone](https://miro.medium.com/fit/c/40/40/1*XVzm4V7GMJqTtgntnWGHzQ.jpeg)](/@khilonecrypto?source=post_internal_links
---------5----------------------------)

[Khilone

](/@khilonecrypto?source=post_internal_links---------
5----------------------------)

in

[Khilone

](https://medium.com/khilone?source=post_internal_links---------
5----------------------------)

## The Unofficial Weekly Stratis Retrospect #3 — Khilone

![](https://miro.medium.com/focal/112/112/50/50/1*MYJVuJyg22wE7n943eZcVg.png)](/khilone/the-
unofficial-weekly-stratis-
retrospect-3-khilone-2d498560c2bd?source=post_internal_links---------
5----------------------------)

[[![Zebpay](https://miro.medium.com/fit/c/40/40/1*KuzqvzFyXhC3Un2ebJocWw.jpeg)](/@zebpay?source=post_internal_links
---------6----------------------------)

[Zebpay

](/@zebpay?source=post_internal_links---------6----------------------------)

in

[Zebpay

](https://medium.com/zebpay?source=post_internal_links---------
6----------------------------)

## Ethereum: 5 Things You Should Know

![](https://miro.medium.com/focal/112/112/50/50/0*kQo5wVLv0PxUvexn.)](/zebpay/ethereum-5-things-
you-should-know-b98251d63ed1?source=post_internal_links---------
6----------------------------)

[[![Crypto
Queen](https://miro.medium.com/fit/c/40/40/1*P-eQnpFwamQOlywNQScvBQ.jpeg)](/@Cryptoqueen55?source=post_internal_links
---------7----------------------------)

[Crypto Queen

](/@Cryptoqueen55?source=post_internal_links---------
7----------------------------)

## Wificoin: A rare crypto gem

![](https://miro.medium.com/focal/112/112/50/50/1*8Fq_0SvfxAIIOpDLBvhRmg.jpeg)](/@Cryptoqueen55/wificoin-
a-rare-crypto-gem-4e98f1825c9a?source=post_internal_links---------
7----------------------------)

[](/?source=post_page-----6098d600e127--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
6098d600e127--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
6098d600e127--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
6098d600e127--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
6098d600e127--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----6098d600e127--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----6098d600e127--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Funiversal-
ethereum%2Fwhat-we-learned-building-universal-login-part-1-the-
problem-6098d600e127&source=post_page--------------------------
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
ethereum%2Fwhat-we-learned-building-universal-login-part-1-the-
problem-6098d600e127&newsletterV3=1ad34b4ecc2e&newsletterV3Id=6e6d213135fd&user=Marek+Kirejczyk&userId=1ad34b4ecc2e&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Steve
Simkins](https://miro.medium.com/fit/c/40/40/1*HtOl7he4IgmldKJfbovgVg.png)](/@stevedsimkins?source=read_next_recirc
---------0---------------------aa2cda2a_1819_418a_8c06_42e28f81fbf5-------)

[Steve Simkins

](/@stevedsimkins?source=read_next_recirc---------0---------------------
aa2cda2a_1819_418a_8c06_42e28f81fbf5-------)

in

[Pinata

](https://medium.com/pinata?source=read_next_recirc---------0
---------------------aa2cda2a_1819_418a_8c06_42e28f81fbf5-------)

## How to Offset Your NFT Project Carbon Emissions with Aerial

![](https://miro.medium.com/focal/112/112/50/50/1*KxoVDEZFH3mJrlfeguMYjg.jpeg)](/pinata/how-
to-offset-your-nft-project-carbon-emissions-with-
aerial-b5b4b95faba0?source=read_next_recirc---------0---------------------
aa2cda2a_1819_418a_8c06_42e28f81fbf5-------)

[[![Colin
Adams](https://miro.medium.com/fit/c/40/40/1*RbKmHEMsKslJnuorr6Dlfw.jpeg)](/@Colin_Adams15z?source=read_next_recirc
---------1---------------------aa2cda2a_1819_418a_8c06_42e28f81fbf5-------)

[Colin Adams

](/@Colin_Adams15z?source=read_next_recirc---------1---------------------
aa2cda2a_1819_418a_8c06_42e28f81fbf5-------)

in

[ChainSafe

](https://medium.com/chainsafe-systems?source=read_next_recirc---------1
---------------------aa2cda2a_1819_418a_8c06_42e28f81fbf5-------)

## ChainSafe Gaming SDK Spotlight: Arsenal Fabwelt

![](https://miro.medium.com/focal/112/112/50/50/0*UyUZtXA2ap51wC9D.jpeg)](/chainsafe-
systems/chainsafe-gaming-sdk-spotlight-arsenal-
fabwelt-1bcbbf364c59?source=read_next_recirc---------1---------------------
aa2cda2a_1819_418a_8c06_42e28f81fbf5-------)

[[![OnecdotIN](https://miro.medium.com/fit/c/40/40/0*yi272vJBZV1u_rV-)](/@onecdotin?source=read_next_recirc
---------2---------------------aa2cda2a_1819_418a_8c06_42e28f81fbf5-------)

[OnecdotIN

](/@onecdotin?source=read_next_recirc---------2---------------------
aa2cda2a_1819_418a_8c06_42e28f81fbf5-------)

## Minting Gaming assets on Polygon using Onecdot APIs

![](https://miro.medium.com/focal/112/112/50/50/1*anYrQiKZtv6DJpaan33MiA.png)](/@onecdotin/minting-
gaming-assets-on-polygon-using-onecdot-
apis-686bf8099352?source=read_next_recirc---------2---------------------
aa2cda2a_1819_418a_8c06_42e28f81fbf5-------)

[[![OMNUUM](https://miro.medium.com/fit/c/40/40/1*9pxqed8ExmdwaqyUynmgfA.png)](/@omnuum?source=read_next_recirc
---------3---------------------aa2cda2a_1819_418a_8c06_42e28f81fbf5-------)

[OMNUUM

](/@omnuum?source=read_next_recirc---------3---------------------
aa2cda2a_1819_418a_8c06_42e28f81fbf5-------)

in

[OMNUUM

](https://medium.com/omnuum?source=read_next_recirc---------3
---------------------aa2cda2a_1819_418a_8c06_42e28f81fbf5-------)

## [ NFT 101 ] #03 Creating Wallet

![](https://miro.medium.com/focal/112/112/50/50/1*RmMha-
qODvTGn4_B8ngl4Q.jpeg)](/omnuum/nft-101-03-creating-
wallet-516c1a9e0e54?source=read_next_recirc---------3---------------------
aa2cda2a_1819_418a_8c06_42e28f81fbf5-------)

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

