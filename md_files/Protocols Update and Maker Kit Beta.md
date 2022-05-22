[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/3435bca84139&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Fluidity](https://miro.medium.com/fit/c/64/64/1*5pEAonqQtkWjGPLSudRP7g.png)](https://medium.com/fluidity?source=post_page
-----3435bca84139--------------------------------)

Published in

[Fluidity

](https://medium.com/fluidity?source=post_page-----
3435bca84139--------------------------------)

[![Don
Mosites](https://miro.medium.com/fit/c/96/96/1*35Ma7kOdkcseXcXXrDm9eg.jpeg)](/@dmosites?source=post_page
-----3435bca84139--------------------------------)

[Don Mosites](/@dmosites?source=post_page-----
3435bca84139--------------------------------)

Follow

Nov 6, 2019

·

3 min read

# Protocols Update and Maker Kit Beta

 _New AirSwap contracts are on Rinkeby, with updated docs and the new Maker
Kit: a set of tools and a reference implementation ready for the new, fully
trustless AirSwap. In beta today and on mainnet later this month._

 **TL;DR** : Check out [Maker Kit](https://github.com/airswap/airswap-maker-
kit) and the new [AirSwap Docs](https://docs.airswap.io/instant/run-makers).

![](https://miro.medium.com/max/1400/1*5v658vPBar4tLaVnS6laEQ.png)

Over the years, the AirSwap network has grown and its structure evolved. Early
on, we envisioned decentralized exchange as trading parties and transfer
logic, where the Ethereum computer would be best with simple logic because
distributed systems are hard.

The simplest is an atomic swap. That is, value transferred among multiple
parties in a single transaction that either entirely succeeds or fails. This
enables peer-to-peer trading between any two parties around the world.

In the case of [AirSwap Instant](https://instant.airswap.io/), makers on the
network are long-running processes, taking on a distinctly client-server
architecture. This is similar to [RFQ in
FX](https://www.cmegroup.com/education/request-for-quote.html) — a powerful,
automated model for distributed trading networks that avoids the pitfalls of
onchain designs.

# Makers are servers

The web itself is a client-server architecture, with servers running behind
every web page, reachable over the public internet by anyone connected. This
has enabled the web to reach global scale, with reliable cloud hosting for
easy development and operation.

This is why makers on AirSwap will no longer be using websockets, instead
implementing the [Peer Protocol](https://docs.airswap.io/instant/api-
reference) using JSON-RPC over HTTP. We’ve published a new [Maker
Kit](https://github.com/airswap/airswap-maker-kit) with a reference
implementation to show just how easy it is.

This approach lets traders focus on providing on-demand quotes with ease
instead of managing deposits or wrangling expensive onchain order books. Just
create a trading strategy, wrap it in a web server, and deploy it to a
publicly accessible URL.

# Indexers are contracts

By default, maker URLs aren’t widely known. Makers signal their intent to
trade including URL on an “indexer” that other trading parties can query. To
date, indexers have been offchain services, but now are smart contracts.

Indexers include many intents to trade, so staking allows you to increase your
rank among other makers. Each entry includes a locator — a string that
represents the location of the maker. For AirSwap Instant, these locators are
URLs at a maximum length of 32 characters.

# Using the Maker Kit

Maker Kit includes a reference implementation and tests. You’ll also find a
range of helpful commands to interact with tokens, indexers, and other peers
on the network. It’s Rinkeby only for now.

![](https://miro.medium.com/max/1400/1*lU4uRWwq1ecP7H2L5hiHWw.png)

[Check it out on GitHub](https://github.com/airswap/airswap-maker-kit) to get
started.

# Migration timeline

This month, we’re undergoing a full contract security audit, integrating the
new Swap and Indexer contracts into Instant and Trader, and working with
makers to transition to the new system over the coming weeks.

The [AirSwap Docs](https://docs.airswap.io/) site includes architecture,
protocols, and contracts. We welcome you to explore the new system and join us
over at our [Discord server](https://chat.airswap.io/), where you’ll find the
team hanging out discussing ideas and helping with questions and support.

Being a maker on AirSwap is easier than ever.

See you there!

# About AirSwap

AirSwap enables peer-to-peer trading on the Ethereum blockchain. Built on a
decentralized protocol, traders can add or remove liquidity through a suite of
trustless products that are easy to use and free. Our mission is to empower
the world with frictionless trade.

[Blog](https://medium.com/fluidity) | [Twitter](https://twitter.com/airswap) |
[Discord](https://chat.airswap.io) | [Developers](https://docs.airswap.io) |
[Makers](https://makers.airswap.io) |
[Reddit](https://www.reddit.com/r/airswap) |
[Facebook](https://www.facebook.com/airswapio/) |
[Linkedin](http://www.linkedin.com/company/airswap/) |
[Subscribe](https://upscri.be/b0fed8-2) |
[Support](https://support.airswap.io) | [Request a
Feature](https://airswap.canny.io) | [FAQ](https://support.airswap.io/faq) |
[Trade Now](https://instant.airswap.io)

\--

\--

\--

## [More from Fluidity](/fluidity?source=post_page-----
3435bca84139--------------------------------)

Rebuilding Finance for a Frictionless World

[Read more from Fluidity](/fluidity?source=post_page-----
3435bca84139--------------------------------)

[](/?source=post_page-----3435bca84139--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
3435bca84139--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
3435bca84139--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
3435bca84139--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
3435bca84139--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----3435bca84139--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----3435bca84139--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Ffluidity%2Fprotocols-
update-and-maker-kit-beta-3435bca84139&source=post_page
--------------------------nav_reg-----------)

[![Don
Mosites](https://miro.medium.com/fit/c/176/176/1*35Ma7kOdkcseXcXXrDm9eg.jpeg)](/@dmosites)

[

## Don Mosites

](/@dmosites)

888 Followers

Co-Founder at @airswap, Co-Founder at @fluidityio

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fusers%2F19fca2ef04ea%2Flazily-enable-
writer-
subscription&operation=register&redirect=https%3A%2F%2Fmedium.com%2Ffluidity%2Fprotocols-
update-and-maker-kit-
beta-3435bca84139&user=Don+Mosites&userId=19fca2ef04ea&source=--------------------------subscribe_user-----------)

## More from Medium

[[![CryptoAI](https://miro.medium.com/fit/c/40/40/1*dg8Q8mNeieDvWaZSG2zL0A.jpeg)](/@CryptoAIWriter?source=read_next_recirc
---------0---------------------f6c44cec_501d_4b44_831d_b75550f4df8d-------)

[CryptoAI

](/@CryptoAIWriter?source=read_next_recirc---------0---------------------
f6c44cec_501d_4b44_831d_b75550f4df8d-------)

in

[Coinmonks

](https://medium.com/coinmonks?source=read_next_recirc---------0
---------------------f6c44cec_501d_4b44_831d_b75550f4df8d-------)

## Taro Set to Bring New Assets and Scalability to Bitcoin Using Taproot and
the Lightning Network

![](https://miro.medium.com/focal/112/112/50/50/1*z0CypG7is8giZhEdQpnaFQ.jpeg)](/coinmonks/taro-
set-to-bring-new-assets-and-scalability-to-bitcoin-using-taproot-and-the-
lightning-network-f87f1664b075?source=read_next_recirc---------0
---------------------f6c44cec_501d_4b44_831d_b75550f4df8d-------)

[[![Corn
Finance](https://miro.medium.com/fit/c/40/40/1*RA1PEzX43VAdMs_Jju4oXQ.png)](/@cornfinance?source=read_next_recirc
---------1---------------------f6c44cec_501d_4b44_831d_b75550f4df8d-------)

[Corn Finance

](/@cornfinance?source=read_next_recirc---------1---------------------
f6c44cec_501d_4b44_831d_b75550f4df8d-------)

## Reinventing the Wheel: Advanced Order Types for Decentralized AMMs

![](https://miro.medium.com/focal/112/112/50/50/0*V8PKV24Z6TTkF1g2.png)](/@cornfinance/reinventing-
the-wheel-advanced-order-types-for-decentralized-amms-
fae5e3b13a56?source=read_next_recirc---------1---------------------
f6c44cec_501d_4b44_831d_b75550f4df8d-------)

[[![kingggslayerrr](https://miro.medium.com/fit/c/40/40/1*7oLPrSA9Gyk6c2pVVqc4tA@2x.jpeg)](/@ghali.benchekroun?source=read_next_recirc
---------2---------------------f6c44cec_501d_4b44_831d_b75550f4df8d-------)

[kingggslayerrr

](/@ghali.benchekroun?source=read_next_recirc---------2---------------------
f6c44cec_501d_4b44_831d_b75550f4df8d-------)

## 01/02/2022 Market Update

![](https://miro.medium.com/focal/112/112/50/50/0*gLQIS0bx1JL8FHk4)](/@ghali.benchekroun/01-02-2022-market-
update-981ff8be2f61?source=read_next_recirc---------2---------------------
f6c44cec_501d_4b44_831d_b75550f4df8d-------)

[[![Antoine
Gaior](https://miro.medium.com/fit/c/40/40/1*9D3L1WTV6_HTCId0g9R7uQ@2x.jpeg)](/@antoinegaior?source=read_next_recirc
---------3---------------------f6c44cec_501d_4b44_831d_b75550f4df8d-------)

[Antoine Gaior

](/@antoinegaior?source=read_next_recirc---------3---------------------
f6c44cec_501d_4b44_831d_b75550f4df8d-------)

in

[Sesterce

](https://medium.com/sesterce?source=read_next_recirc---------3
---------------------f6c44cec_501d_4b44_831d_b75550f4df8d-------)

## SYNAPSE PROTOCOL

![](https://miro.medium.com/focal/112/112/50/50/1*zI4K_UfYQivLJfpOmC3wOA.png)](/sesterce/synapse-
protocol-f511e9654450?source=read_next_recirc---------3---------------------
f6c44cec_501d_4b44_831d_b75550f4df8d-------)

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

