[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/178f00fe9364&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![OmniBOLT](https://miro.medium.com/fit/c/64/64/1*Eax06VpAs4_LvYwm9mKHgA.png)](https://medium.com/omnibolt?source=post_page
-----178f00fe9364--------------------------------)

Published in

[OmniBOLT

](https://medium.com/omnibolt?source=post_page-----
178f00fe9364--------------------------------)

[![OmniBOLT](https://miro.medium.com/fit/c/96/96/2*-Qd9OlgSGltPYkwnUAdhVw.png)](/@omniboltofficial?source=post_page
-----178f00fe9364--------------------------------)

[OmniBOLT](/@omniboltofficial?source=post_page-----
178f00fe9364--------------------------------)

Follow

Mar 11, 2020

·

6 min read

# Part I | **OmniBOLT Detailed Introduction**

![](https://miro.medium.com/max/1400/1*neY8m0b-uUMadmc9A8jmxg.jpeg)

To help community better understand OmniLayer, OmniBOLT, Lightning Network and
related programs, we make a solid essay to explain them in detail, and we
break them down into two parts, this piece is the Part I. At the same time, we
present the core module of OmniBOLT —— Atom Swap among Channels within the
[**Part II** ,](/omnibolt/part-i-omnibolt-detailed-introduction-178f00fe9364)
which can be checked here. So, let’s start to explore **the lightning network
flagship protocol: OmniBOLT !**

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

 **1 Lightning network and OmniLayer**

 **2 Concept**

 **3 Revocable Sequence Maturity Contract Explained**

 **4 Hash Time-Locked Contract Explained**

#  **1\. Lightning network and OmniLayer**

Based on the fundamental theory of Lightning network, OmniBOLT specification
describes how to enable OmniLayer assets to be transferred via lightning
channels, and how can OmniLayer assets benefit from the novel quick payment
theory. According to the layer-2 protocol [BOLT (Basis of Lightning
Technology) ](https://github.com/lightningnetwork/lightning-
rfc/blob/master/00-introduction.md)specification for off-chain bitcoin
transfer, we propose this OmniLayer specific protocol to expand the horizons
of the basic theory, to support wider perspective of assets.

OmniBOLT itself does not issue tokens. All tokens are issued on OmniLayer, and
enter the OmniBOLT network through P2(W)SH backed channels, being locked on
the main chain, and can be redeemed on the OmniLayer main chain at any time.

# 2\. **Concept**

  *  **OBD:** OmniBOLT Daemon.
  *  **channel:** A channel refers to Poon-Dryja channel in lightning network. Channel is denoted by `[Alice, USDT, Bob]`, which means Alice and Bob build a channel and fund it by USDT.
  *  **property:** refers to tokens issued on OmniLayer, the same to “asset”.
  *  **RSMC:** Revocable Sequence Maturity Contract is composed to punish malicious peers, who broadcasts elder commitment transactions to get more refund than what’s exactly in his balance.
  *  **HTLC:** Hashed Time-Lock Contract chains multiple channels for transferring tokens from one peer to another, between whom there is no direct channel established.
  *  **Commitment Transaction:** is created but not broadcast, and may be invalidated by next commitment transaction.
  *  **BR:** Breach Remedy transaction is used in RSMC, that if Alice is cheated by broadcasting an elder commitment transaction, BR will send all her money to Bob.
  *  **RD:** Revocable Delivery transaction pays out from the 2–2 P2SH transaction output, when Alice broadcast the latest legitimate commitment transaction. It sends money to Bob immediately and will send money to Alice after relative, say 100 blocks, from current block height.
  *  **HED:** HTLC Execution Delivery
  *  **HT:** HTLC Timeout
  *  **HBR:** HTLC Breach Remedy, the breach remedy transaction in HTLC
  *  **HTRD:** HTLC Timeout Revocable Delivery, the revocable delivery transaction in HTLC
  *  **HTBR:** HTLC Timeout Breach Remedy, punishes Alice who broadcasts the elder hash time-locked transaction during the time lock period.
  *  **Atomic Swap:** Atomic swap technology enables the exchange of one cryptocurrency for another without using centralized intermediaries, such as exchanges.
  *  **HTLSC:** Hashed TimeLock Swap Contract, which consists of two separate HTLCs with extra specified exchange rate of tokens and time lockers.

# 3\. **Revocable Sequence Maturity Contract Explained**

In order to avoid malicious counterparty who rejects to sigh any payment out
of the P2SH transaction, so that the money is forever locked in the channel,
we construct a Commitment Transaction where one is able to revoke a
transaction. This is the first place we introduce the Revocable Sequence
Maturity Contract (RSMC), invented by Poon and Dryja in their white paper, in
this specification.

So the `funding_created` message does not mean both parties really deposite
money into the channel. The first round communication is just simply setup a
P2SH address, construct funding transaction but unbroadcasted and construct a
RSMC. After that, Alice or Bob can broadcast the funding transaction to
transfer real Omni assets into the channel.

The following diagram shows the steps we MUST do before any participants
broadcast the funding/commitment transactions. BR1a (Breach Remedy) can be
created later before the next commitment transaction is contructed.

![](https://miro.medium.com/max/1400/1*zRqBwR_cWP-CmM2A1mZG-A.png)

In general, RSMC consists of the following 5 steps:

step 1: Alice constructs a temporary 2–2 multi-sig address using Alice’s
temporary private key Alice2 and wait Bob’s signature: Alice2 & Bob.

step 2: Alice constructs a promise payment C1a out of Alice & Bob, one output
is 60 USDT to `Alice2 & Bob`, and the other output is 40 USDT to Bob.

step 3: RD1a is the first output of C1a, which pays Alice 60 USDT, but with a
sequence number preventing immediate payment if Alice cheat.

step 4: Bob signs C1a and RD1a, sends back to Alice.

step 5: OBD constructs refund transaction: C1a/RD1a.

This diagram shows a commitment transaction take place within a channel,
illustrating how the status have been transferred.

![](https://miro.medium.com/max/1400/1*_wRI4-mjo9jYfWyEIYDSGw.png)

#  **4\. Hash Time-Locked Contract Explained**

> “A bidirectional payment channel only permits secure transfer of funds
> inside a channel. To be able to construct secure transfers using a network
> of channels across multiple hops to the final destination requires an
> additional construction, a Hashed Timelock Contract (HTLC).”
>
> — Poon & Dryja, The Bitcoin Lightning Network: Scalable Off-chain Instant
> Payments

A big and common misleading explanation in chaining the channels using HTLC is
that if Alice wants to pay 10 USDT to David, she can use 2 hops to reach
David:

    
    
    Alice ---(10 USDT)---> Bob ---(10 USDT)---> Carol ---(10 USDT)---> David

It is confusing, because there is no concept of personal account in lightning.
The only building block lightning use case is channel. So the correct hops
are:

    
    
    [Alice --(10 USDT)--> Bob] ==(Bob has two channels)== [Bob --(10 USDT)--> Carol] ==(Carol has two channels)== [Carol --(10 USDT)--> David][A, USDT, B] stands for the channel built by A and B, funded by USDT.

Alice transfers 10 USDT to Bob inside the `[Alice, USDT, Bob]` channel, then
Bob transfers 10 USDT to Carol inside the `[Bob, USDT, Carol]` channel, and
finally Carol sends 10 USDT to David in `[Bob, USDT, Carol]`.

An HTLC implements this procedure:

 _If Bob can tell Alice_` _R_` _, which is the pre-image of_` _Hash(R)_` _that
some one else (Carol) in the chain shared with Bob 3 days ago in exchange of
10 USDT in the channel_` _[Bob, USDT, Carol]_` _, then Bob will get the 10
USDT fund inside the channel_` _[Alice, USDT, Bob]_` _, otherwise Alice gets
her 10 USDT back._

Equipped with HTLC, the internal transfer of fund `[Alice --(10 USDT in
HTLC)--> Bob]` is then an extra unbroadcasted output from funding transaction
embedded together with
[RD1a/BR1a](https://github.com/LightningOnOmnilayer/Omni-BOLT-
spec/blob/master/OmniBOLT-03-RSMC-and-OmniLayer-Transactions.md#the-
commitment_tx-and-commitment_tx_signed-message).

![](https://miro.medium.com/max/1400/1*Resg7uN5KY-7Idv2ENfQwg.png)

#  **Reference**

Bitcoin Lightning network White Paper： lightning.network/lightning-network-
paper.pdf

BOLT specification: <https://github.com/lightningnetwork/lightning-rfc>

Lightning Network Project: <https://github.com/lightningnetwork/lnd>

OmniLayer Specification: <https://github.com/OmniLayer/spec>

OmniBOLT Specification:

[

## omnilaboratory/Omni-BOLT-spec

### Based on the fundamental theory of Lightning network, OmniBOLT
specification describes how to enable OmniLayer assets…

github.com

](https://github.com/omnilaboratory/Omni-BOLT-spec)

OmniBOLT Project:

<https://github.com/omnilaboratory/obd>

OmniLayer Wallet: <https://github.com/OmniLayer/omniwallet>

OmniJ: <https://github.com/OmniLayer/OmniJ>

# Follow us

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
178f00fe9364--------------------------------)

OmniBOLT(Omni Basis of Lightning Technology) is the world’s first stable coin
circulation specification (on Omnilayer) for Lightning Network.

[Read more from OmniBOLT](/omnibolt?source=post_page-----
178f00fe9364--------------------------------)

[](/?source=post_page-----178f00fe9364--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
178f00fe9364--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
178f00fe9364--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
178f00fe9364--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
178f00fe9364--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----178f00fe9364--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----178f00fe9364--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fomnibolt%2Fpart-
i-omnibolt-detailed-introduction-178f00fe9364&source=post_page
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
i-omnibolt-detailed-
introduction-178f00fe9364&user=OmniBOLT&userId=23e27e311f41&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Joe
Walker](https://miro.medium.com/fit/c/40/40/1*NoKl8fHJhdTOSO7WjwrkeQ.jpeg)](/@IAmJoeWalker?source=read_next_recirc
---------0---------------------8c0981e7_2c08_47bb_b8be_a9f935765c21-------)

[Joe Walker

](/@IAmJoeWalker?source=read_next_recirc---------0---------------------
8c0981e7_2c08_47bb_b8be_a9f935765c21-------)

## KOIN Tokenomics part 2: how to assess real value based on mana

![](https://miro.medium.com/focal/112/112/50/50/1*2alrltyxtOA-W456eZDL8g.png)](/@IAmJoeWalker/koin-
tokenomics-part-2-how-to-assess-real-value-based-on-
mana-f69007f7e617?source=read_next_recirc---------0---------------------
8c0981e7_2c08_47bb_b8be_a9f935765c21-------)

[[![Shubham
Ambastha](https://miro.medium.com/fit/c/40/40/1*n_f0W2Bbb8eabpfKT6VyJg.jpeg)](/@ShubhamAmbastha?source=read_next_recirc
---------1---------------------8c0981e7_2c08_47bb_b8be_a9f935765c21-------)

[Shubham Ambastha

](/@ShubhamAmbastha?source=read_next_recirc---------1---------------------
8c0981e7_2c08_47bb_b8be_a9f935765c21-------)

## Defi startup Pillow which claims to offer up to 18% returns raises $3Millon
from prominent…

![](https://miro.medium.com/focal/112/112/50/50/1*LC5YqggfKCmIhanVZSQF7w.png)](/@ShubhamAmbastha/defi-
startup-pillow-which-claims-to-offer-up-to-18-returns-raises-3millon-from-
prominent-6f2a66023182?source=read_next_recirc---------1---------------------
8c0981e7_2c08_47bb_b8be_a9f935765c21-------)

[[![Hipo](https://miro.medium.com/fit/c/40/40/1*1bPB2ag4W0zrdxnGcNo4IQ.png)](/@hipoone?source=read_next_recirc
---------2---------------------8c0981e7_2c08_47bb_b8be_a9f935765c21-------)

[Hipo

](/@hipoone?source=read_next_recirc---------2---------------------
8c0981e7_2c08_47bb_b8be_a9f935765c21-------)

## Hipo vs. Other Protocols: What’s the Difference

![](https://miro.medium.com/focal/112/112/50/50/1*_gNfErLq8eAtr2X_qaSLjA.jpeg)](/@hipoone/hipo-
vs-other-protocols-whats-the-difference-a3936629bb74?source=read_next_recirc
---------2---------------------8c0981e7_2c08_47bb_b8be_a9f935765c21-------)

[[![jakedenny](https://miro.medium.com/fit/c/40/40/1*bA3p3iwx_8ICfbfGgMx02A.jpeg)](/@jakedenny?source=read_next_recirc
---------3---------------------8c0981e7_2c08_47bb_b8be_a9f935765c21-------)

[jakedenny

](/@jakedenny?source=read_next_recirc---------3---------------------
8c0981e7_2c08_47bb_b8be_a9f935765c21-------)

in

[Coinmonks

](https://medium.com/coinmonks?source=read_next_recirc---------3
---------------------8c0981e7_2c08_47bb_b8be_a9f935765c21-------)

## You can’t have the “way it was”, and arrive in the future

![](https://miro.medium.com/freeze/focal/112/112/50/50/1*xgI1il5BJLihVMJYIxLd6Q.gif)](/coinmonks/you-
cant-have-the-way-it-was-and-arrive-in-the-
future-8f801e377e52?source=read_next_recirc---------3---------------------
8c0981e7_2c08_47bb_b8be_a9f935765c21-------)

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

