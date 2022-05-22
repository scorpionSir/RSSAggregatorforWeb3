[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/c70c73f58477&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Fluidity](https://miro.medium.com/fit/c/64/64/1*5pEAonqQtkWjGPLSudRP7g.png)](https://medium.com/fluidity?source=post_page
-----c70c73f58477--------------------------------)

Published in

[Fluidity

](https://medium.com/fluidity?source=post_page-----
c70c73f58477--------------------------------)

[![AirSwap](https://miro.medium.com/fit/c/96/96/1*S-j0-sWqnj2pMlbQUFV4iQ.jpeg)](/@airswap?source=post_page
-----c70c73f58477--------------------------------)

[AirSwap](/@airswap?source=post_page-----
c70c73f58477--------------------------------)

Follow

Aug 8, 2019

·

4 min read

# New AirSwap Protocols

 _Decentralized trade starts with an atomic swap. Today, we’re publishing new
protocols including on-chain peer discovery and delegation, enabling even more
powerful applications and integrations throughout decentralized finance._

![](https://miro.medium.com/max/1400/1*9U5icRwAxeHueTof_IjV6Q.png)

Traders on AirSwap continue to use the original Swap
[contract](https://etherscan.io/address/0x8fd3121013a07c57f0d69646e86e7a4880b467b7)
deployed years ago. It does one job well: to swap tokens and ether. Immutable
like any smart contract, it will continue to support applications that fit.

# Setting a course

Since then, we’ve seen both needs and opportunities to expand its capabilities
and deploy new protocol elements as smart contracts. Already, the components
of trade — custody, execution, and settlement — are decentralized through a
peer-to-peer design, our founding principle.

Our goal is to take flight — to become open, transparent, and immutable.
Combined with an overall aim to bolster liquidity through both online and
onchain peers, our goal to take flight also includes more open source
development and decentralized indexing capabilities.

# New features for Swap

We’ve maintained the same simplicity that makes the [Swap
Protocol](https://swap.tech/whitepaper/) elegant. We’ve added support for more
token and signature types, improved efficiency, and added two powerful new
features: affiliates and authorizations.

 **Token types** include ERC-20 and ERC-721 (NFT) with a path to supporting
more standards over time. **Signature types** include both standard and
ERC-712 (typed) for improved wallet usability and transparency. All signatures
are now more secure by implementing EIP-191.

 **Affiliates** are third-parties compensated for their part in bringing
together two parties making a trade. These come into play if a transaction is
facilitated by a third-party or a software application helps to connect its
users to other traders on the network.

 **Authorizations** are for peers that trade on behalf of others. These peers
are authorized for either side of a trade, and can be wallets (people or
programs) or smart contracts, opening a new world of integration
possibilities.

See the [Swap source code on GitHub](https://github.com/airswap/airswap-
protocols/tree/master/source/swap).

We take quality and security seriously. We maintain unit and integration tests
for full coverage, and have performed an internal audit by our team at
Fluidity with the support of researcher and advisor [Phil
Daian](https://pdaian.com/).

See the [Swap Security Report on GitHub](https://github.com/airswap/airswap-
protocols/blob/master/source/swap/reports/SECURITY.md).

# New decentralized indexers

We envision a future of many indexers, supporting makers of many kinds. An
indexer employs a token for staking, a necessary utility to give makers an
opportunity to be among the first returned when the indexer is queried.

For example, an application like [AirSwap
Instant](https://instant.airswap.io/) may be interested in querying a maximum
of 20 prospective makers at a time. By staking variable amounts of AirSwap
Token, makers can ensure that they are included among those results and able
to provide that liquidity.

In the future, an indexer could be deployed for IPFS hashes that resolve to
arbitrary URLs for makers that live around the web at various endpoints
speaking various protocols. We think the new indexer design both fits this
wide open future and matches our original vision well.

See the [Indexer source code on GitHub](https://github.com/airswap/airswap-
protocols/tree/master/source/indexer).

# New onchain liquidity

The authorization feature enables traders to deploy smart contracts that
implement the [Peer Protocol](https://swap.tech/whitepaper/#peer-protocol) and
trade on their behalf. The simplest form of this is rules that effectively
provide limit orders and partial fills. Others can include arbitrary logic and
integrations with other liquidity sources.

See the [Delegate source on GitHub](https://github.com/airswap/airswap-
protocols/tree/master/source/delegate). **For demonstration only**.

The AirSwap network today, comprised of automated makers and trading desks,
does a great job covering higher liquidity assets and large over-the-counter
trades. Onchain liquidity now lets everyday people and token teams participate
without having to run online maker software.

In combination with existing automated makers and trading desks, we think this
solution fills the long tail of liquidity completes the picture.

# Active open source development

Today we’ve published our complete [protocols
repository](https://github.com/airswap/airswap-protocols) for review and
contribution. You’ll find our team there — [Deepa
Sathaye](https://medium.com/u/2d6ffd2add6f?source=post_page-----
c70c73f58477--------------------------------), [Ethan
Wessel](https://medium.com/u/7cbea9b40fa3?source=post_page-----
c70c73f58477--------------------------------), [Alice
Henshaw](https://medium.com/u/bc6c5c22afc1?source=post_page-----
c70c73f58477--------------------------------), and [Don
Mosites](https://medium.com/u/19fca2ef04ea?source=post_page-----
c70c73f58477--------------------------------)— actively developing new
features and performing ongoing security and performance analysis. We welcome
your thoughts and contributions and look forward to continued growth as we
pursue an immutable and transparent future.

# Coming up next

This week, we released [AirSwap Trader](https://trader.airswap.io/) using the
new Swap contract in production. Our upcoming goals are to complete and deploy
a new indexer for AirSwap Instant, and then to complete the onchain peer
system.

We’ll soon publish a bug bounty for the Swap contract so stay tuned. To
discuss the new AirSwap Protocols repository and roadmap, please join our team
on the new [AirSwap server on Discord](https://discord.gg/ahRmhNZ). We’re
looking forward to it.

# About AirSwap

AirSwap enables peer-to-peer trading on the Ethereum blockchain. Built on a
decentralized protocol, traders can add or remove liquidity through a suite of
trustless products that are easy to use and free. Our mission is to empower
the world with frictionless trade.

[Blog](https://medium.com/fluidity) | [Twitter](https://twitter.com/airswap) |
[Discord](https://chat.airswap.io/) | [Developers](https://docs.airswap.io/) |
[Makers](https://makers.airswap.io/) |
[Reddit](https://www.reddit.com/r/airswap) |
[Facebook](https://www.facebook.com/airswapio/) |
[Linkedin](http://www.linkedin.com/company/airswap/) |
[Subscribe](https://upscri.be/b0fed8-2) |
[Support](https://support.airswap.io/) | [Request a
Feature](https://airswap.canny.io/) | [FAQ](https://support.airswap.io/faq) |
[Trade Now](https://instant.airswap.io/)

\--

\--

\--

## [More from Fluidity](/fluidity?source=post_page-----
c70c73f58477--------------------------------)

Rebuilding Finance for a Frictionless World

[Read more from Fluidity](/fluidity?source=post_page-----
c70c73f58477--------------------------------)

## Recommended from Medium

[[![zk - Zubin
Koticha](https://miro.medium.com/fit/c/40/40/1*V7-Ys28J1XXrrQyVWoJHKg.jpeg)](/@zubinkoticha?source=post_internal_links
---------0----------------------------)

[zk - Zubin Koticha

](/@zubinkoticha?source=post_internal_links---------
0----------------------------)

in

[ThunderCore

](https://medium.com/thundercore?source=post_internal_links---------
0----------------------------)

## Proof of Stake and the History of Distributed Consensus: Part 1, Nakamoto
Consensus, Byzantine…

![Image result for thunder
protocol](https://miro.medium.com/focal/112/112/50/50/1*pq9I-TEJMr3DhPh1gVP7VQ.png)](/thundercore/proof-
of-stake-and-the-history-of-distributed-consensus-part-1-nakamoto-consensus-
byzantine-176e0156316e?source=post_internal_links---------
0----------------------------)

[[![Em
WilliamsBee](https://miro.medium.com/fit/c/40/40/1*3oI6T9POhZ3Yr_yFjFVyCA.jpeg)](/@williambassey5_77581?source=post_internal_links
---------1----------------------------)

[Em WilliamsBee

](/@williambassey5_77581?source=post_internal_links---------
1----------------------------)

## 📢 @Chain_Guardians listed this week on @thedapplist V2 🎉

![](https://miro.medium.com/focal/112/112/50/50/1*eNvX-UAuEBRqbEB7Oo-
sFg.jpeg)](/@williambassey5_77581/chain-guardians-listed-this-week-on-
thedapplist-v2-a30026afcc77?source=post_internal_links---------
1----------------------------)

[[![Blockfluence](https://miro.medium.com/fit/c/40/40/1*pVp939YJQkMO0roThjPnBQ.png)](/@Blockfluence?source=post_internal_links
---------2----------------------------)

[Blockfluence

](/@Blockfluence?source=post_internal_links---------
2----------------------------)

## Blockfluence x Transient

](/@Blockfluence/blockfluence-x-
transient-b3fd402087fc?source=post_internal_links---------
2----------------------------)

[[![Programmable
Business](https://miro.medium.com/fit/c/40/40/1*-d40OJVex50xtPb-
SHsjsQ.png)](/@programmablebiz?source=post_internal_links---------
3----------------------------)

[Programmable Business

](/@programmablebiz?source=post_internal_links---------
3----------------------------)

in

[Programmable Business

](https://medium.com/programmable-business?source=post_internal_links---------
3----------------------------)

## Blockchain techs to watch for enterprises — promising privacy and
performance

![](https://miro.medium.com/focal/112/112/50/50/1*-WTxjj0wS-S8j8eYvWCqrQ.png)](/programmable-
business/blockchain-techs-to-watch-for-enterprises-promising-privacy-and-
performance-8586fe044342?source=post_internal_links---------
3----------------------------)

[[![Pablo
Peillard](https://miro.medium.com/fit/c/40/40/1*6gcZ4stBN1eNof0ObsZDyQ.jpeg)](/@publu?source=post_internal_links
---------4----------------------------)

[Pablo Peillard

](/@publu?source=post_internal_links---------4----------------------------)

in

[Hashing Systems

](https://medium.com/hashingsystems?source=post_internal_links---------
4----------------------------)

## Introduction to Hash Name Service: A Hashgraph-based registry

![](https://miro.medium.com/focal/112/112/50/50/0*fQLIMNiixLYCYZeV)](/hashingsystems/introduction-
to-hash-name-service-a-hashgraph-based-
registry-27d52a44ab38?source=post_internal_links---------
4----------------------------)

[[![Tom
Hamilton](https://miro.medium.com/fit/c/40/40/1*ioPWrTsc_RJZtO94geT3GQ.jpeg)](/@tom.hamilton?source=post_internal_links
---------5----------------------------)

[Tom Hamilton

](/@tom.hamilton?source=post_internal_links---------
5----------------------------)

in

[Streamr

](https://medium.com/streamrblog?source=post_internal_links---------
5----------------------------)

## Transcript: Telegram AMA with Henri Pihkala — 13th March 2019

![](https://miro.medium.com/focal/112/112/50/50/1*CIoWFHE6TUxz-M7MaX1fkw.png)](/streamrblog/transcript-
telegram-ama-with-henri-pihkala-13th-
march-2019-6133985144e3?source=post_internal_links---------
5----------------------------)

[[![DragonMaster](https://miro.medium.com/fit/c/40/40/1*5FcRAq30xRv80jU4YFCkKg.png)](/@dragonmaster?source=post_internal_links
---------6----------------------------)

[DragonMaster

](/@dragonmaster?source=post_internal_links---------
6----------------------------)

## Recap on AMA with DragonMaster x IGG

![](https://miro.medium.com/focal/112/112/50/50/1*A_XoifPgwHf61m24AOnkng.jpeg)](/@dragonmaster/recap-
on-ama-with-dragonmaster-x-igg-96b124b822e6?source=post_internal_links
---------6----------------------------)

[[![Citadao.io](https://miro.medium.com/fit/c/40/40/1*j57PKx6_mrvZ4bWRut1-yw.jpeg)](/@citadao?source=post_internal_links
---------7----------------------------)

[Citadao.io

](/@citadao?source=post_internal_links---------7----------------------------)

## CitaDAO Closes $1 Million Builders Round to bring Real Estate onto DeFi

![](https://miro.medium.com/focal/112/112/50/50/1*_bGGqJHdXRWK4VsLBb3yJg.png)](/@citadao/citadao-
closes-1-million-builders-round-to-bring-real-estate-onto-
defi-c91f0eff5a69?source=post_internal_links---------
7----------------------------)

[](/?source=post_page-----c70c73f58477--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
c70c73f58477--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
c70c73f58477--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
c70c73f58477--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
c70c73f58477--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----c70c73f58477--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----c70c73f58477--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Ffluidity%2Fnew-
airswap-protocols-c70c73f58477&source=post_page--------------------------
nav_reg-----------)

[![AirSwap](https://miro.medium.com/fit/c/176/176/1*S-j0-sWqnj2pMlbQUFV4iQ.jpeg)](/@airswap)

[

## AirSwap

](/@airswap)

2.8K Followers

AirSwap is a developer community focused on decentralized trading systems.

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F198e2de34d43&operation=register&redirect=https%3A%2F%2Fmedium.com%2Ffluidity%2Fnew-
airswap-
protocols-c70c73f58477&newsletterV3=b501917dd00d&newsletterV3Id=198e2de34d43&user=AirSwap&userId=b501917dd00d&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Uri
Kirstein](https://miro.medium.com/fit/c/40/40/1*oOsxc_QEjbYFBuuAxnW_qA.jpeg)](/@uri_kirstein?source=read_next_recirc
---------0---------------------939547fe_e598_4fe8_b710_6607255f931a-------)

[Uri Kirstein

](/@uri_kirstein?source=read_next_recirc---------0---------------------
939547fe_e598_4fe8_b710_6607255f931a-------)

in

[Certora

](https://medium.com/certora?source=read_next_recirc---------0
---------------------939547fe_e598_4fe8_b710_6607255f931a-------)

## Stopping DeFi Bugs at Scale

![](https://miro.medium.com/focal/112/112/50/50/1*FVCzmfL8qhfyDUFXrjRKrQ.png)](/certora/stopping-
defi-bugs-at-scale-6e3fba22dd3d?source=read_next_recirc---------0
---------------------939547fe_e598_4fe8_b710_6607255f931a-------)

[[![Timothy Hao Chi
Ho](https://miro.medium.com/fit/c/40/40/1*JlD7bKJG1GAjl5MxZN96kw.png)](/@tim-
hch?source=read_next_recirc---------1---------------------
939547fe_e598_4fe8_b710_6607255f931a-------)

[Timothy Hao Chi Ho

](/@tim-hch?source=read_next_recirc---------1---------------------
939547fe_e598_4fe8_b710_6607255f931a-------)

in

[ChainSafe

](https://medium.com/chainsafe-systems?source=read_next_recirc---------1
---------------------939547fe_e598_4fe8_b710_6607255f931a-------)

## Glow of the Canopy #1 🌱: Nourishing the Filecoin Virtual Machine with help
from Forest 🌲

![](https://miro.medium.com/focal/112/112/50/50/0*fH72IfjPczZ2c8qs)](/chainsafe-
systems/glow-of-the-canopy-1-nourishing-the-filecoin-virtual-machine-with-
help-from-forest-6249354f9fb9?source=read_next_recirc---------1
---------------------939547fe_e598_4fe8_b710_6607255f931a-------)

[[![GM](https://miro.medium.com/fit/c/40/40/1*gZNos5Qpk_FEbV2RXacNHg.jpeg)](/@sudogm?source=read_next_recirc
---------2---------------------939547fe_e598_4fe8_b710_6607255f931a-------)

[GM

](/@sudogm?source=read_next_recirc---------2---------------------
939547fe_e598_4fe8_b710_6607255f931a-------)

in

[Dragonfly Research

](https://medium.com/dragonfly-research?source=read_next_recirc---------2
---------------------939547fe_e598_4fe8_b710_6607255f931a-------)

## Spamming Solana: a Trip Report

![](https://miro.medium.com/focal/112/112/50/50/0*Qvg98HFQGV91vp_I)](/dragonfly-
research/spamming-solana-a-trip-report-d05e0455a3ba?source=read_next_recirc
---------2---------------------939547fe_e598_4fe8_b710_6607255f931a-------)

[[![Jeffersonx
Xavier](https://miro.medium.com/fit/c/40/40/1*N9OL4MFynLtR1u0GQgvM6w.jpeg)](/@jefferson-
xavier?source=read_next_recirc---------3---------------------
939547fe_e598_4fe8_b710_6607255f931a-------)

[Jeffersonx Xavier

](/@jefferson-xavier?source=read_next_recirc---------3---------------------
939547fe_e598_4fe8_b710_6607255f931a-------)

## Create your own private blockchain using Ethereum

![](https://miro.medium.com/focal/112/112/50/50/0*-zwmlifLw288zg9E.png)](/@jefferson-
xavier/create-your-own-private-blockchain-using-
ethereum-3836ce9d04e6?source=read_next_recirc---------3---------------------
939547fe_e598_4fe8_b710_6607255f931a-------)

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

