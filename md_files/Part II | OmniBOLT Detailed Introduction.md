[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/3a98c0cd714a&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![OmniBOLT](https://miro.medium.com/fit/c/64/64/1*Eax06VpAs4_LvYwm9mKHgA.png)](https://medium.com/omnibolt?source=post_page
-----3a98c0cd714a--------------------------------)

Published in

[OmniBOLT

](https://medium.com/omnibolt?source=post_page-----
3a98c0cd714a--------------------------------)

[![OmniBOLT](https://miro.medium.com/fit/c/96/96/2*-Qd9OlgSGltPYkwnUAdhVw.png)](/@omniboltofficial?source=post_page
-----3a98c0cd714a--------------------------------)

[OmniBOLT](/@omniboltofficial?source=post_page-----
3a98c0cd714a--------------------------------)

Follow

Mar 11, 2020

·

6 min read

# Part II | OmniBOLT Detailed Introduction

![](https://miro.medium.com/max/1400/1*neY8m0b-uUMadmc9A8jmxg.jpeg)

To help community better understand OmniLayer, OmniBOLT, Lightning Network and
related programs, we make a solid essay to explain them in detail, and we
break them down into two parts, this piece is the Part II, which starts with
the core module of OmniBOLT — — Atom Swap among Channels. Also, you can check
the [**Part I here**](/omnibolt/part-i-omnibolt-detailed-
introduction-178f00fe9364). Now, let’s start to dig deeply into **the
lightning network flagship protocol: OmniBOLT !**

# Intro

Lightning network aims to scale the Bitcoin network, facilitating quick off-
chain payment of Bitcoin among independent peers on the network. Based on its
fundamental theory, OmniBOLT defines the quick circulation protocol for smart
assets layer on Bitcoin network, especially for those issued by OmniLayer
protocol.

 **Because of the fundamental support of smart asset, not only BTC instant
payment is supported as the currently implemented LND and BOLT, but also the
following advantages:**

  *  **Instant payment of smart assets issued on OmniLayer.**
  *  **Cross channel atomic swap of different assets.**
  *  **Decentralized exchange on top of lightning channels with quick exchange speed.**
  *  **Collateral Lending contract based on atomic swap.**
  *  **More flexible contracts for Decentralized Finance.**

Reders who have interest shall directly go to the OmniBOLT specification
repository on Github: ****[**chapter 6: DEX, Collateral Lending Contract,
online store …**](https://github.com/LightningOnOmnilayer/Omni-BOLT-
spec/blob/master/OmniBOLT-06-Mortgage-Loan-Contracts-for-Crypto-Assets.md)
****_(_[ _https://github.com/LightningOnOmniLayer/Omni-BOLT-
spec/blob/master/OmniBOLT-06-Mortgage-Loan-Contracts-for-Crypto-
Assets.md)_](https://github.com/LightningOnOmniLayer/Omni-BOLT-
spec/blob/master/OmniBOLT-06-Mortgage-Loan-Contracts-for-Crypto-Assets.md\))
__ to seek more examples.

OmniBOLT greatly extends the ability of the Bitcoin lightning network. It
appeared on August 1st, 2019.

# Content

5\. Atom Swap among Channels

6\. Applications：collateral lending, online pet store, etc

7\. Implementation and API for wallet

# 5\. Atom Swap among Channels

In general, atomic swaps take place between different blockchains, for
exchanging tokens with no trust of each other. Channels defined in OmniBOLT
can be funded by any token issued on OmniLayer. If one needs to trade his
tokens, say USDT, for someone else’s Bitcoins, both parties are required to
acknowledge receipt of funds of USDT and BTC, within a specified timeframe
using a cryptographic hash function. If one of the involved parties fails to
confirm the transaction within the timeframe, then the entire transaction is
voided, and funds are not exchanged, but refunded to original account. The
latter action ensures to remove counterparty risk.

The standard swap procedure between channels is:

![](https://miro.medium.com/max/1400/1*PDOUjexUQBkL8SJ3dzD8mw.png)

    
    
    - where Tx 1 transfers 1000 USDT to Bob in channel `[Alice, USDT, Bob]`, locked by Hash(R), t1 and Bob's signature.- Tx 2 transfers 1 BTC to Alice in channel `[Alice, BTC, Bob]`, locked by Hash(R), t2(`t2 < t1`) and Alice's signature .

Hashed TimeLock Swap Contract (HTLSC) consists of two seperated HTLCs with
extra specified exchange rate of tokens and time lockers.

Simply there are 5 steps in a swap. In step 3, Alice sends R to Bob, hence she
can unlock transaction 2 to get her 1 BTC in the channel `[Alice, BTC, Bob]`.
Therefore Bob knows R, and use R to unlock his 900 USDT in the channel
`[Alice, USDT, Bob]`.

No participant is able to cheat. After inputting R in each channel, the
transaction 1 and 2 turn into general commitment transactions, which is the
same procedure that how an [HTLC transforms to a commitment
transaction](https://github.com/LightningOnOmnilayer/Omni-BOLT-
spec/blob/master/OmniBOLT-05-Atomic-Swap-among-Channels.md#terminate-htlc-off-
chain).

In channel `[Alice, USDT, Bob]`, Alice creates an HTLC and its mirror
transactions on Bob side, with time locker `t1`, which in the diagram is 3
days as an example.

![](https://miro.medium.com/max/1400/1*Resg7uN5KY-7Idv2ENfQwg.png)

At the same time, Bob creates another HTLC in the channel `[Alice, BTC, Bob]`
and its mirror transactions on Alice side, sending the agreed number of BTCs
to Alice. Time locker `t2` is set to be 2 days, less than `t1=3` days.

![](https://miro.medium.com/max/1400/1*P_bKcM4l0tA3f1gSIsdSSQ.png)

Atomic swap is the foundation of lots of blockchain applications. Next chapter
will present some examples, which are intuitive and will help our readers to
build much more complex applications for real-world businesses.

# 6\. Applications：collateral lending, online pet store, etc

Following examples use multi-stage atomic swaps for specific scenarios. The
procedures shall be implemented as a piece of program written in a turing
complete language, like Javascript or Solidity, calling OBD API to complete
the fundamental tasks. All participants shall run the programs to check if all
the transactions are valid and if the counterparties are honest.

##  **Collateral Lending Contract (CLC)**

Collateral Lending Contract serves this certain purpose:

“ _You deposit something valuable as mortgage in an escrow account, and I lend
money to you according to a proper LTV(Loan to Value). If you repay the loan
within agreed deadline, Iwill return your mortgage. If you don’t, your
mortgage will be mine._ ”

Actually an HTLSC creates an escrow accounts for participants in a loan. We
assume a normal scenario:

Bob wants to borrow 900 USDT from Alice, he uses his 1 BTC as collateral.

So Bob initiates a swap (HTLSC 1):

Bob → Alice: swap(amount = 1 BTC, property = USDT, exchange rate = 900,
time_locker = 30 days, Hash(R1), …).

This creates HTLSC in channel [Alice, BTC, Bob].

Alice → Bob: swap_accepted(amount = 900 USDT, exchange_rate = 900, time_locker
= 20 days, Hash(R1), …).

This creates HTLSC in channel [Alice, USDT, Bob].

Meanwhile, Bob needs to create the redeem swap (HTLSC 2) to get his 1 BTC
back:

Bob → Alice: swap(amount = 900 USDT, property = BTC, exchange_rate = 1/900,
time_locker = 60 days, Hash(R2), …).

This creates HTLSC in channel [Alice, USDT, Bob].

Alice → Bob: swap_accepted(amount = 1 BTC, exchange_rate = 1/900, time_locker
= 50 days, Hash(R2), …).

This creates HTLSC in channel [Alice, BTC, Bob].

Only when the participants accepted the two swaps, and their OBDs helps to
create all the corresponding transaction required by HTLSC, Bob is able to use
R1 to get his 900 USDT by HTLSC 1 in channel [Alice, USDT, Bob], hence Alice
gets 1 BTC as collateral from Bob.

And after a timeframe, Bob wants to redeem his 1 BTC. He uses R2 in HTLSC 2 to
get his 1 BTC back by HTLSC 2 in channel [Alice, BTC, Bob], hence Alice gets
her 900 USDT back in channel [Alice, USDT, Bob].

Of course, Alice can require a loan rate according to her knowledge of the
price of BTC. For example, she requires Bob to create a swap with exchange
rate 1/905. Then she will get 905 USDT when Bob redeems his BTC.

##  **Online Pet Store**

This example is one stage swap, which is quite straight forward:

  1. Alice issues smart asset “PET” on OmniLayer, for each token represents a crypto cat.
  2. Bob establishes an USDT channel and a PET channel with Alice, and funds the USDT channel.
  3. Bob creates a HTLSC to pay Alice 100 USDT for one cat.

That’s it :-)

# 7\. Implementation and API for wallet

Implementation of OmniBOLT specification can be found in this repository
[LightningOnOmniLayer](https://github.com/LightningOnOmnilayer/LightningOnOmni)：

[https://github.com/LightningOnOmniLayer/LightningOnOmni](https://github.com/LightningOnOmnilayer/LightningOnOmni)

as well as the API online documentation can be found
[here](https://api.omnilab.online/)：

<https://api.omnilab.online/>

Javascript API:

<https://github.com/LightningOnOmniLayer/DebuggingTool/blob/master/js/obdapi.js.>

GUI debugging tool:

<https://github.com/LightningOnOmniLayer/DebuggingTool> Reference：

# Reference

Bitcoin Lightning network White Paper： lightning.network/lightning-network-
paper.pdf

BOLT specification: <https://github.com/lightningnetwork/lightning-rfc>

Lightning Network Project: <https://github.com/lightningnetwork/lnd>

OmniLayer Specification: <https://github.com/OmniLayer/spec>

OmniBOLT Specification:

<https://github.com/omnilaboratory/Omni-BOLT-spec>

OmniBOLT Project:

<https://github.com/omnilaboratory/obd>

OmniLayer Wallet: <https://github.com/OmniLayer/omniwallet>

OmniJ: <https://github.com/OmniLayer/OmniJ>

# Follow us:

 **OmniBOLT Twitter** : <https://twitter.com/omni_bolt>

**OmniLAB Twitter** : <https://twitter.com/OmniLabOfficial>

**OmniLAB Website** : <https://omnilab.online/>

**OmniBOLT Linkedin** :
<https://www.linkedin.com/company/omnibolt/?viewAsMember=true>

**OmniLAB Linkedin** :
<https://www.linkedin.com/company/omnilabofficial/?viewAsMember=true>

**OmniBOLT Reddit** | <https://www.reddit.com/user/OmniBOLT>

**OmniLAB Reddit** | <https://www.reddit.com/user/OmniLAB>

\--

\--

\--

## [More from OmniBOLT](/omnibolt?source=post_page-----
3a98c0cd714a--------------------------------)

OmniBOLT(Omni Basis of Lightning Technology) is the world’s first stable coin
circulation specification (on Omnilayer) for Lightning Network.

[Read more from OmniBOLT](/omnibolt?source=post_page-----
3a98c0cd714a--------------------------------)

[](/?source=post_page-----3a98c0cd714a--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
3a98c0cd714a--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
3a98c0cd714a--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
3a98c0cd714a--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
3a98c0cd714a--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----3a98c0cd714a--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----3a98c0cd714a--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fomnibolt%2Fpart-
ii-omnibolt-detailed-introduction-3a98c0cd714a&source=post_page
--------------------------nav_reg-----------)

[![OmniBOLT](https://miro.medium.com/fit/c/176/176/2*-Qd9OlgSGltPYkwnUAdhVw.png)](/@omniboltofficial)

[

## OmniBOLT

](/@omniboltofficial)

18 Followers

OmniBOLT (Omni Basis of Lightning Technology) is the world’s first stable coin
circulation specification on Omnilayer for Lightning Network.

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fusers%2F23e27e311f41%2Flazily-enable-
writer-
subscription&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fomnibolt%2Fpart-
ii-omnibolt-detailed-
introduction-3a98c0cd714a&user=OmniBOLT&userId=23e27e311f41&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Sae'Von
Springer](https://miro.medium.com/fit/c/40/40/1*evagaEC6NnVODRDjJQh8DQ.jpeg)](/@nativeassets?source=read_next_recirc
---------0---------------------28ed5e18_6290_41e7_bcc9_7d9d7c44d79f-------)

[Sae'Von Springer

](/@nativeassets?source=read_next_recirc---------0---------------------
28ed5e18_6290_41e7_bcc9_7d9d7c44d79f-------)

## Ethereum: The Smart Contract Standard | A Beginner’s Guide

![](https://miro.medium.com/focal/112/112/50/50/1*Dcgarm7EBDyA0L6Q0324Hw.jpeg)](/@nativeassets/ethereum-
the-smart-contract-standard-a-beginners-
guide-5999e10d5964?source=read_next_recirc---------0---------------------
28ed5e18_6290_41e7_bcc9_7d9d7c44d79f-------)

[[![Adamnite](https://miro.medium.com/fit/c/40/40/1*NaMEIJTwn7ylBiqQGiAayw.png)](/@adamnite?source=read_next_recirc
---------1---------------------28ed5e18_6290_41e7_bcc9_7d9d7c44d79f-------)

[Adamnite

](/@adamnite?source=read_next_recirc---------1---------------------
28ed5e18_6290_41e7_bcc9_7d9d7c44d79f-------)

## A dive into Delegated Proof of Stake

![](https://miro.medium.com/focal/112/112/50/50/0*VT7k3fa_DNiVY3ws)](/@adamnite/a-dive-
into-delegated-proof-of-stake-1f2dedc0533f?source=read_next_recirc---------1
---------------------28ed5e18_6290_41e7_bcc9_7d9d7c44d79f-------)

[[![jihwan.eth](https://miro.medium.com/fit/c/40/40/1*y1eFTOSYmCx2M-VVjIhEnQ.jpeg)](/@jihwan.eth?source=read_next_recirc
---------2---------------------28ed5e18_6290_41e7_bcc9_7d9d7c44d79f-------)

[jihwan.eth

](/@jihwan.eth?source=read_next_recirc---------2---------------------
28ed5e18_6290_41e7_bcc9_7d9d7c44d79f-------)

## About Celestia

![](https://miro.medium.com/focal/112/112/50/50/1*ufJ1ltfn_YYxUyOmzt92hA.png)](/@jihwan.eth/about-
celestia-39e35cff1871?source=read_next_recirc---------2---------------------
28ed5e18_6290_41e7_bcc9_7d9d7c44d79f-------)

[[![bitcoinmusk](https://miro.medium.com/fit/c/40/40/0*v_4sJvi5sAVCFde9)](/@bitcoinmusk2022?source=read_next_recirc
---------3---------------------28ed5e18_6290_41e7_bcc9_7d9d7c44d79f-------)

[bitcoinmusk

](/@bitcoinmusk2022?source=read_next_recirc---------3---------------------
28ed5e18_6290_41e7_bcc9_7d9d7c44d79f-------)

## Defi Helps You Obtain Your Desires

![](https://miro.medium.com/focal/112/112/50/50/1*cn5KECQAtWHvGTf9U0_8IQ.jpeg)](/@bitcoinmusk2022/defi-
helps-you-obtain-your-desires-40c4091d0f2c?source=read_next_recirc---------3
---------------------28ed5e18_6290_41e7_bcc9_7d9d7c44d79f-------)

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

