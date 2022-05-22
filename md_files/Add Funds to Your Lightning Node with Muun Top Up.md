[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/28baec564334&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Muun](https://miro.medium.com/fit/c/64/64/1*ZHNsPvynwNOPydFxp27GCw.png)](https://medium.com/muunwallet?source=post_page
-----28baec564334--------------------------------)

Published in

[Muun

](https://medium.com/muunwallet?source=post_page-----
28baec564334--------------------------------)

[![Dario
Sneidermanis](https://miro.medium.com/fit/c/96/96/1*X7LvaPF58TnRzGQuKbt1ow.jpeg)](/@esneider?source=post_page
-----28baec564334--------------------------------)

[Dario Sneidermanis](/@esneider?source=post_page-----
28baec564334--------------------------------)

Follow

Sep 5, 2019

·

2 min read

# Add Funds to Your Lightning Node with Muun Top Up

![](https://miro.medium.com/max/1400/1*LRTCZlYbTqUb740jil1pcA.jpeg)

 ** _Edit: As of June 2020, this feature has been disabled._**

Some months ago, [we released Lightning payments in
Muun](https://blog.muun.com/lightning-payments-easier-than-ever/). They are
instant, 100% non-custodial and don’t require any channel configuration.

Since then, we have received requests from users who wanted to use this
feature to top up their lightning nodes and get connected to ours. Therefore,
we improved the feature to make it faster and easier to use for this purpose.

As of today, **you can easily top up your Lightning node from your phone using
Muun.** Just generate an invoice of 150,000 sats (or more) from your node and
pay it with Muun. To be extra sure, we suggest you extend the expiration time
of your invoice to 2 hours.

The transaction you are sending is a submarine swap, consisting of an on-chain
transaction to a swap provider, that pays the lightning invoice with an off-
chain transaction. Both transactions happen atomically, so the whole process
is **completely trustless**.

There are two aspects of this use case that make it different from other
Lightning payments in Muun: 1) The amount being sent is probably larger (
>150,000 sats) and 2) The destination node is probably less connected than a
merchant or a Lightning App. Because of this, chances are there won’t be a
well-funded route to your node. This won’t be a problem. Instead, **Muun will
automatically open a channel to your node and you will receive the money off-
chain**.

The result is that you will top up your node gaining outbound capacity to pay
in the Lightning Network. At the same time, you will get connected to one of
our nodes, that is both well-connected and well-funded.

# Confirmation times and fees

Making a Top Up requires four confirmations from the network, meaning the
whole process will take **approximately 40 minutes**. This differs from
instant Lightning payments because there isn’t an existing well-funded route
at the moment of the payment. A channel must be open on the spot. The fees
associated with this service are to cover all the on-chain transactions needed
to manage the channel.

Are you running your own node? [Give it a
try](https://play.google.com/store/apps/details?id=io.muun.apollo&/) and tell
us what you think!

 _Originally published at_[
_https://blog.muun.com_](https://blog.muun.com/add-funds-to-your-lightning-
node-with/) _on September 5, 2019._

\--

1

\--

\--

1

## [More from Muun](/muunwallet?source=post_page-----
28baec564334--------------------------------)

Stories from Muun, the most powerful Bitcoin and Lightning wallet

[Read more from Muun](/muunwallet?source=post_page-----
28baec564334--------------------------------)

## Recommended from Medium

[[![Safe
Haven](https://miro.medium.com/fit/c/40/40/1*u46PEblEEXAE3Pcsyk_i-w.jpeg)](/@safehavenio?source=post_internal_links
---------0----------------------------)

[Safe Haven

](/@safehavenio?source=post_internal_links---------
0----------------------------)

## Safe Haven — Building solutions for inheritance, asset distribution, and
asset control on the…

![](https://miro.medium.com/focal/112/112/50/50/1*l_Wr_tDlRY_se9jbsZjakA.png)](/@safehavenio/safe-
haven-building-solutions-for-inheritance-asset-distribution-and-asset-control-
on-the-9f3c2bebecad?source=post_internal_links---------
0----------------------------)

[[![Zap
Protocol](https://miro.medium.com/fit/c/40/40/1*ZZfp8NRM_zFBYPEMDxuNbA.jpeg)](/@zapprotocol?source=post_internal_links
---------1----------------------------)

[Zap Protocol

](/@zapprotocol?source=post_internal_links---------
1----------------------------)

in

[Zap Protocol

](https://medium.com/the-zap-project?source=post_internal_links---------
1----------------------------)

## Use Kovan Zap to Access & Test the Zap Platform

![](https://miro.medium.com/focal/112/112/50/50/0*xm5EIdSAf-xvWtRS)](/the-zap-
project/use-kovan-zap-to-access-test-the-zap-
platform-f2633c0379cf?source=post_internal_links---------
1----------------------------)

[[![Jasmy](https://miro.medium.com/fit/c/40/40/1*giSDAgnhjCFdCWzYKVwTyw.jpeg)](/@jasmy-
global?source=post_internal_links---------2----------------------------)

[Jasmy

](/@jasmy-global?source=post_internal_links---------
2----------------------------)

## jasmy is listing on ZB now !

](/@jasmy-global/jasmy-is-listing-on-zb-
now-811d8c49c1f9?source=post_internal_links---------
2----------------------------)

[[![Amasa](https://miro.medium.com/fit/c/40/40/1*mPtX0aOb-YmECk81ZCp-
ug.png)](/@amasa?source=post_internal_links---------
3----------------------------)

[Amasa

](/@amasa?source=post_internal_links---------3----------------------------)

## Axie Infinity — More Than Just a Game

![](https://miro.medium.com/focal/112/112/50/50/1*b3bSNsQRyjVTmCFgK5jGuA.jpeg)](/@amasa/axie-
infinity-more-than-just-a-game-99e8f5473233?source=post_internal_links
---------3----------------------------)

[[![Aspenlabs](https://miro.medium.com/fit/c/40/40/1*dmbNkD5D-u45r44go_cf0g.png)](/@aspenlabs32?source=post_internal_links
---------4----------------------------)

[Aspenlabs

](/@aspenlabs32?source=post_internal_links---------
4----------------------------)

## NFT Crypto | Aspenlabs.io

](/@aspenlabs32/nft-crypto-aspenlabs-
io-875793bb62fc?source=post_internal_links---------
4----------------------------)

[[![Crypto currency for beginners
uk](https://miro.medium.com/fit/c/40/40/1*h-1CIsjPax23oHICXU77iA.png)](/@cryptocurrencyforbeginnersuk?source=post_internal_links
---------5----------------------------)

[Crypto currency for beginners uk

](/@cryptocurrencyforbeginnersuk?source=post_internal_links---------
5----------------------------)

## Wizardly Finance 8% daily

![](https://miro.medium.com/focal/112/112/50/50/1*XX45bEpJOMwKmAPZ7NvP3Q.png)](/@cryptocurrencyforbeginnersuk/wizardly-
finance-8-daily-ecbaf1c27f46?source=post_internal_links---------
5----------------------------)

[[![Al](https://miro.medium.com/fit/c/40/40/1*f0RO84GP7kiIqc6aK0Ckug.jpeg)](/@alhause?source=post_internal_links
---------6----------------------------)

[Al

](/@alhause?source=post_internal_links---------6----------------------------)

## Understanding Bitcoin (101)

![](https://miro.medium.com/focal/112/112/50/50/0*r3loDw--
O-rt4UH2.jpeg)](/@alhause/understanding-
bitcoin-101-f7b144c687fe?source=post_internal_links---------
6----------------------------)

[[![Death
Punch](https://miro.medium.com/fit/c/40/40/1*TQTfOHgmCuyLSdmtkna7Xg.jpeg)](/@deathpunch?source=post_internal_links
---------7----------------------------)

[Death Punch

](/@deathpunch?source=post_internal_links---------
7----------------------------)

## How to Win $1000 Without Investing in Pre-release Crypto Game

![](https://miro.medium.com/focal/112/112/50/50/1*emcE2nFxn-6_j8e9DN4eaQ.png)](/@deathpunch/how-
to-win-1000-without-investing-in-pre-release-crypto-
game-c5e6a4af1082?source=post_internal_links---------
7----------------------------)

[](/?source=post_page-----28baec564334--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
28baec564334--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
28baec564334--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
28baec564334--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
28baec564334--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----28baec564334--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----28baec564334--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fmuunwallet%2Fadd-
funds-to-your-lightning-node-with-muun-top-up-28baec564334&source=post_page
--------------------------nav_reg-----------)

[![Dario
Sneidermanis](https://miro.medium.com/fit/c/176/176/1*X7LvaPF58TnRzGQuKbt1ow.jpeg)](/@esneider)

[

## Dario Sneidermanis

](/@esneider)

143 Followers

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fusers%2F61fb7700ea57%2Flazily-enable-
writer-
subscription&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fmuunwallet%2Fadd-
funds-to-your-lightning-node-with-muun-top-
up-28baec564334&user=Dario+Sneidermanis&userId=61fb7700ea57&source=--------------------------subscribe_user-----------)

## More from Medium

[[![GBC.AI](https://miro.medium.com/fit/c/40/40/1*F-NtW7mHaPt5Gv7I7s-GjQ.png)](/@gbc-
ai?source=read_next_recirc---------0---------------------
452680a6_ff20_408e_9534_ae7376401bd5-------)

[GBC.AI

](/@gbc-ai?source=read_next_recirc---------0---------------------
452680a6_ff20_408e_9534_ae7376401bd5-------)

## What does GBC.AI do? | Blockchain 4.0

![](https://miro.medium.com/focal/112/112/50/50/1*fIzucrjtYxHhV8PlXCSa3g.png)](/@gbc-
ai/the-im-community-hosted-gbc-ai-for-an-
ama-933d39c4bd0e?source=read_next_recirc---------0---------------------
452680a6_ff20_408e_9534_ae7376401bd5-------)

[[![Tom
S](https://miro.medium.com/fit/c/40/40/1*vWUzaA9YlSZ2M3OW5yJdhA.jpeg)](/@tomscoding?source=read_next_recirc
---------1---------------------452680a6_ff20_408e_9534_ae7376401bd5-------)

[Tom S

](/@tomscoding?source=read_next_recirc---------1---------------------
452680a6_ff20_408e_9534_ae7376401bd5-------)

## How Chaincorn’s Layer 0 could revolutionize Blockchain and speed up Mass
adoption.

![](https://miro.medium.com/focal/112/112/50/50/1*8-nXgPuvFDykW07ktl36xg.png)](/@tomscoding/how-
chaincorns-layer-0-could-revolutionize-blockchain-and-speed-up-mass-
adoption-9fcea49710a?source=read_next_recirc---------1---------------------
452680a6_ff20_408e_9534_ae7376401bd5-------)

[[![VCU
Blockchain](https://miro.medium.com/fit/c/40/40/1*TubxMyNiktXYd8ITRnWAbg.png)](/@VcuBlockchain?source=read_next_recirc
---------2---------------------452680a6_ff20_408e_9534_ae7376401bd5-------)

[VCU Blockchain

](/@VcuBlockchain?source=read_next_recirc---------2---------------------
452680a6_ff20_408e_9534_ae7376401bd5-------)

## Solana NFTs on OpenSea, Binance at the Grammys, & Audius for Artists

![](https://miro.medium.com/focal/112/112/50/50/1*_vLhrxkoZLIFUuVAcBVLHw.png)](/@VcuBlockchain/solana-
nfts-on-opensea-binance-at-the-grammys-audius-for-
artists-b65cae2cfe42?source=read_next_recirc---------2---------------------
452680a6_ff20_408e_9534_ae7376401bd5-------)

[[![DeFi
adept](https://miro.medium.com/fit/c/40/40/1*DWjt4vxnKkguoQXK1hmFOw@2x.jpeg)](/@mishustinvlad1?source=read_next_recirc
---------3---------------------452680a6_ff20_408e_9534_ae7376401bd5-------)

[DeFi adept

](/@mishustinvlad1?source=read_next_recirc---------3---------------------
452680a6_ff20_408e_9534_ae7376401bd5-------)

## Aleo — is not just a new blockchain, it’s much more.

![](https://miro.medium.com/focal/112/112/50/50/1*hvbc5LSpR-
je99kGdrwHzQ.png)](/@mishustinvlad1/aleo-is-not-just-a-new-blockchain-its-
much-more-79799a498eae?source=read_next_recirc---------3---------------------
452680a6_ff20_408e_9534_ae7376401bd5-------)

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

