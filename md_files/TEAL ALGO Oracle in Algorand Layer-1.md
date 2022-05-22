[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/57e75f54eab9&~feature=LoOpenInAppButton&~channel=ShowPostUnderUser&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Borderless
Capital](https://miro.medium.com/fit/c/96/96/2*8KIOXE8g8bE5g2A_h3sWaA.jpeg)](/@borderlesscapital?source=post_page
-----57e75f54eab9--------------------------------)

[Borderless Capital](/@borderlesscapital?source=post_page-----
57e75f54eab9--------------------------------)

Follow

Aug 25, 2020

·

4 min read

# TEAL ALGO Oracle in Algorand Layer-1

![](https://miro.medium.com/max/192/0*YVxvZArRvGDCVyJE.png)

Price is a fundamental component of economic transactions. It is the
multiplier required to calculate the amount of value exchanged between
participants. In a blockchain, the ability to reference a price on-chain
enables a seamless and trustless transaction environment, especially for
automated transactions and smart contracts. Oracles are the entities in charge
of broadcasting off-chain data such as market price to the blockchain, and
serve as a source of truth that allows on-chain dApps to measure the value of
assets referenced within a transaction.

[Rand Labs](https://randlabs.io) has recently revealed a novel architecture
for an _Algorand Oracle_ that facilitates the swap of two assets fully on-
chain, you can read more about the testnet implementation
[here](https://developer.algorand.org/articles/algorand-exchange-price-
oracle/).

We have committed additional resources to the project and have successfully
evolved the Oracle from our initial prototype into a _TEAL_ -compatible
ALGO/USD on-chain _Oracle_ using [Coinbase.com](https://coinbase.com) as the
data source. The revamped _Oracle_ is now in production and running on
Algorand’s MainNet.

The TEAL ALGO Oracle will inspire and enable a new generation of financial
products in the crypto ecosystem. For the first time in a high performance
public-permissionless blockchain, the Oracle runs on layer 1 of the protocol.
This means that any Algorand user or application will be able to reference the
market price of an asset inside of their transaction (including _atomic
transfers_ ) with negligible fees and receive a confirmation in under five
seconds, only possible due to its unique Pure Proof-of-Stake consensus based
on VRF primitives, introduced initially by Silvio Micali, Michael Rabin and
Salil Vadha. This infrastructure will democratize access to DeFi products and
services which are cost prohibitive for sub-$1k transactions on other
blockchain platforms. Developers will have the choice over what data provider
they use for their oracle, and the authenticity of the published data can be
verified using signed messages of the provider that will come in the next
iteration of this technology.

For the implementation, a _price submitter_ is needed where the price is
attached to the _Note_ field of the transaction with the Oracle’s signature.
Any _TEAL_ code using this _Oracle_ data must pay a fee that is used to cover
the on-chain _price submitter’s_ transaction fees. Since the _TEAL ALGO
Oracle_ contract can be referenced by any dApp, the service can potentially
run continuously if enough applications integrate it into their stack. In
addition, dApps (such as an on-chain Decentralized Exchange) can increase
their Byzantine Fault Tolerance by using multiple price sources, since the
_price submitter_ could provide up to three price sources signed by different
entities in a single transaction.

Each round, the _price submitter_ generates a transaction containing a
_Message Pack_ in the _Note_ field that includes the price, timestamp and
signed _TEAL_ code that is used to verify the signed price within an _atomic
transfer._

E.g.:

    
    
    {  
     "decimals": 4, "last_trade_at": "2020-08-18T19:06:34.944785Z", "price": 5853, "signature": { "l": { "type": "Buffer", "data": [ 1, ..., 16 ] }, "sig": { "type": "Buffer", "data": [ 157, ..., 15 ] } }, "timestamp": "2020-08-18T19:24:44.078Z" }

To use the _Oracle,_ users must create a group transaction with one
transaction paying the _Oracle_ fee, only the transaction free in this
version, while the other transactions can reference the signed price in any
way related to user needs. For a complete explanation, refer to this
[article](https://developer.algorand.org/articles/algorand-exchange-price-
oracle/) and also this [on-chain example in
testnet](https://testnet.algoexplorer.io/transactions/group/Txm1kD7K2twbuKfknDL%2F7ydCtL%2BGrKSPEf5srzht3xg%3D).

You can view the _TEAL ALGO Oracle_ working tirelessly here:
[PRICEP3G2F5L6ZG5WTJIAKEQW4OJJ3FM4XVFQDZI7M2VBTFVUHTTR2AU2U](https://algoexplorer.io/address/PRICEP3G2F5L6ZG5WTJIAKEQW4OJJ3FM4XVFQDZI7M2VBTFVUHTTR2AU2U)

We [open sourced](https://github.com/randlabs/algo-price-oracle) the code to
empower all developers and apps with the ability to implement custom _TEAL
Oracles_ that broadcast any type of data to Algorand’s Layer 1. A wide range
of off-chain data can be brought on-chain by a variation of this Algorand
_TEAL Oracle_ , including stock prices, or fiat currency pair exchange rates,
smart contract data from other chains, weather and sensor data, just to name a
few.

The _TEAL ALGO Oracle_ has a transaction fee of .001 ALGOs/block to record the
ALGO/USD price from Coinbase in each Algorand block.

Borderless Capital has sponsored this research since its inception, and has
further committed to bootstrap the initiative by funding the _TEAL ALGO
Oracle_ contract with enough ALGOs for it to run for one year. Now, any
developer or dApp can use the _TEAL ALGO Oracle_ at no cost. After that
period, developers and apps can fuel the Oracle by sending it 0.001 ALGOs for
each block they would like the Oracle to operate for, and the Oracle will
produce a new on-chain price which can be referenced by any _TEAL_ contracts
(both stateless or stateful).

“ _We see the opportunity to sponsor the TEAL ALGO Oracle as a continued
demonstration of our commitment to push the limits of Blockchain technology.
This initiative may be one of the most significant additions to Algorand’s
infrastructure to date. It not only provides one of the core building blocks
for Algorand’s Finance 3.0 and DeFi ecosystem, it also inspires other
developers to utilize this technology to develop their own innovations_ “ ~
David Garcia, founding managing partner of Borderless Capital.

 _Originally published by Rand Labs at_[ _https://medium.com_](/randlabs/teal-
algo-oracle-in-algorand-layer-1-30cceba1f125) _on August 25, 2020._

\--

\--

\--

## [More from Borderless Capital](/@borderlesscapital?source=post_page-----
57e75f54eab9--------------------------------)

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F1c33ae759495&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40borderlesscapital%2Fteal-
algo-oracle-in-algorand-
layer-1-57e75f54eab9&newsletterV3=554e3c0c6258&newsletterV3Id=1c33ae759495&user=Borderless+Capital&userId=554e3c0c6258&source=-----57e75f54eab9
---------------------subscribe_user-----------)

Borderless Capital is a financial institution focused exclusively on powering
Algorand’s borderless economy.

Love podcasts or audiobooks? Learn on the go with our new app.

[Try
Knowable](https://knowable.fyi/?utm_source=medium&utm_medium=referral&utm_campaign=medium-
post-footer&source=post_page-----57e75f54eab9--------------------------------)

## Recommended from Medium

[[![Meta
Invest](https://miro.medium.com/fit/c/40/40/0*MV5Sj63_9xHJvJ8C)](/@metainvestnft?source=post_internal_links
---------0----------------------------)

[Meta Invest

](/@metainvestnft?source=post_internal_links---------
0----------------------------)

## Meta Invest, a Metaverse platform, NFT, Dapp, Web3, etc

![](https://miro.medium.com/freeze/focal/112/112/50/50/1*lok1vSpVOMuVqGnbeGfjsA.gif)](/@metainvestnft/meta-
invest-a-metaverse-platform-nft-dapp-web3-etc-
ef94e7153619?source=post_internal_links---------0----------------------------)

[[![buatminning](https://miro.medium.com/fit/c/40/40/0*cmRZHkWqnrCj1QPq.jpg)](/@buatminning?source=post_internal_links
---------1----------------------------)

[buatminning

](/@buatminning?source=post_internal_links---------
1----------------------------)

## InsureDAO Testnet is live today with Mission Bingo Challenge!

![](https://miro.medium.com/focal/112/112/50/50/0*PzPT7TCnNjFxvfjA.png)](/@buatminning/insuredao-
testnet-is-live-today-with-mission-bingo-
challenge-b4141bdf5ce5?source=post_internal_links---------
1----------------------------)

[[![Zeuss](https://miro.medium.com/fit/c/40/40/1*FO2tBfHpIcQQRd_z0TirPg.png)](/@Zeuss1110?source=post_internal_links
---------2----------------------------)

[Zeuss

](/@Zeuss1110?source=post_internal_links---------
2----------------------------)

## Ethereum Approaches Major Upgrade as Testnet Set to Undergo Merge in June

![](https://miro.medium.com/focal/112/112/50/50/1*UmNiC6-tNC5VbllNnJGlVQ.png)](/@Zeuss1110/ethereum-
approaches-major-upgrade-as-testnet-set-to-undergo-merge-in-
june-39f9bcc90727?source=post_internal_links---------
2----------------------------)

[[![Aniel
Essien](https://miro.medium.com/fit/c/40/40/1*x2lkZMi_chTYhtSQZKTJDw.jpeg)](/@anieljoshua94?source=post_internal_links
---------3----------------------------)

[Aniel Essien

](/@anieljoshua94?source=post_internal_links---------
3----------------------------)

## Staking activities in the lead as Persistence is set for a world class
event

![](https://miro.medium.com/focal/112/112/50/50/0*4ZnZB4F7jmrYo6ks)](/@anieljoshua94/staking-
activities-in-the-lead-as-persistence-is-set-for-a-world-class-event-up-till-
mid-october-c94608c9274c?source=post_internal_links---------
3----------------------------)

[[![NKB
Group](https://miro.medium.com/fit/c/40/40/1*shgS6A71Pchab6gzXP9Pxg.png)](/@theNKBGroup?source=post_internal_links
---------4----------------------------)

[NKB Group

](/@theNKBGroup?source=post_internal_links---------
4----------------------------)

## Breaking News: Windows can be hacked by fake DNS queries.

![](https://miro.medium.com/focal/112/112/50/50/1*76k3BCPLW2KOWtoSWrcPPA.png)](/@theNKBGroup/breaking-
news-windows-can-be-hacked-by-fake-dns-
queries-7e635c16e92f?source=post_internal_links---------
4----------------------------)

[[![Godspower Kpobari
Vizor](https://miro.medium.com/fit/c/40/40/1*SdpzVkNZc6i2VHwYuFV1Aw.jpeg)](/@jayj80822?source=post_internal_links
---------5----------------------------)

[Godspower Kpobari Vizor

](/@jayj80822?source=post_internal_links---------
5----------------------------)

## Marlin Protocol

![](https://miro.medium.com/focal/112/112/50/50/1*iw6eXrwd2OTA98h43xiQyg.png)](/@jayj80822/marlin-
protocol-9bdfe14bbb9a?source=post_internal_links---------
5----------------------------)

[[![Techracers](https://miro.medium.com/fit/c/40/40/1*eQcJD986pALOUSYArX_dWw.png)](/@Techracer?source=post_internal_links
---------6----------------------------)

[Techracers

](/@Techracer?source=post_internal_links---------
6----------------------------)

## Healthcare Innovation with Blockchain Powered Internet of things

![](https://miro.medium.com/focal/112/112/50/50/0*xHVQ-18T0KGx4wBQ.jpg)](/@Techracer/healthcare-
innovation-with-blockchain-powered-internet-of-
things-5bd289d1ecdb?source=post_internal_links---------
6----------------------------)

[[![Interchain
Foundation](https://miro.medium.com/fit/c/40/40/1*3eEnGimfA4YJrycw-
lz5jg.png)](/@interchain-io?source=post_internal_links---------
7----------------------------)

[Interchain Foundation

](/@interchain-io?source=post_internal_links---------
7----------------------------)

## Composable Finance receives grant from Interchain Foundation to Bridge
DotSama and IBC

![](https://miro.medium.com/focal/112/112/50/50/0*ckKkn0vIu3aPG1fT)](/@interchain-
io/composable-finance-receives-grant-from-interchain-foundation-to-bridge-
dotsama-and-ibc-db3fdc56294?source=post_internal_links---------
7----------------------------)

[](/?source=post_page-----57e75f54eab9--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
57e75f54eab9--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
57e75f54eab9--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
57e75f54eab9--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
57e75f54eab9--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----57e75f54eab9--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----57e75f54eab9--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40borderlesscapital%2Fteal-
algo-oracle-in-algorand-layer-1-57e75f54eab9&source=post_page
--------------------------nav_reg-----------)

[![Borderless
Capital](https://miro.medium.com/fit/c/176/176/2*8KIOXE8g8bE5g2A_h3sWaA.jpeg)](/@borderlesscapital)

[

## Borderless Capital

](/@borderlesscapital)

102 Followers

Borderless Capital is a financial institution focused exclusively on powering
Algorand’s borderless economy.

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F1c33ae759495&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40borderlesscapital%2Fteal-
algo-oracle-in-algorand-
layer-1-57e75f54eab9&newsletterV3=554e3c0c6258&newsletterV3Id=1c33ae759495&user=Borderless+Capital&userId=554e3c0c6258&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Mike
Gilchrist](https://miro.medium.com/fit/c/40/40/1*4XwLCS6ThXA0MXlTqWUi3w@2x.jpeg)](/@mikegilchrist84?source=read_next_recirc
---------0---------------------70a8cf2b_321c_48eb_955d_64cfaa6daf2e-------)

[Mike Gilchrist

](/@mikegilchrist84?source=read_next_recirc---------0---------------------
70a8cf2b_321c_48eb_955d_64cfaa6daf2e-------)

## A bunch of questions, a few visions

![](https://miro.medium.com/focal/112/112/50/50/1*kDVxwllIBR1nBjbLqm_xDg@2x.jpeg)](/@mikegilchrist84/greetings-4e58c91e4bd4?source=read_next_recirc
---------0---------------------70a8cf2b_321c_48eb_955d_64cfaa6daf2e-------)

[[![Reserveum - International Analitical
Group](https://miro.medium.com/fit/c/40/40/1*GnDsWUnMIYdK4MDNGBwjAQ.png)](/@Reserveum?source=read_next_recirc
---------1---------------------70a8cf2b_321c_48eb_955d_64cfaa6daf2e-------)

[Reserveum - International Analitical Group

](/@Reserveum?source=read_next_recirc---------1---------------------
70a8cf2b_321c_48eb_955d_64cfaa6daf2e-------)

in

[RESERVEUM | Fair Digital Money

](https://medium.com/fair-digital-money?source=read_next_recirc---------1
---------------------70a8cf2b_321c_48eb_955d_64cfaa6daf2e-------)

## Reserveum Digest 02.2022–05.2022

![](https://miro.medium.com/focal/112/112/50/50/1*04icZRB1XDd5u3hYIF76Og.jpeg)](/fair-
digital-money/reserveum-
digest-02-2022-05-2022-5880120ad57a?source=read_next_recirc---------1
---------------------70a8cf2b_321c_48eb_955d_64cfaa6daf2e-------)

[[![Himanshu Jain](https://miro.medium.com/fit/c/40/40/1*Xaf4UelWAC24wJ-
bZBoQHw.png)](/@himanshujain06?source=read_next_recirc---------2
---------------------70a8cf2b_321c_48eb_955d_64cfaa6daf2e-------)

[Himanshu Jain

](/@himanshujain06?source=read_next_recirc---------2---------------------
70a8cf2b_321c_48eb_955d_64cfaa6daf2e-------)

## Prime editing: The new CAShable gene editing

![An image of DNA in a
helix.](https://miro.medium.com/focal/112/112/50/50/0*ldD3G5dCnB9fCC03)](/@himanshujain06/prime-
editing-the-new-cashable-gene-editing-41439f330e3f?source=read_next_recirc
---------2---------------------70a8cf2b_321c_48eb_955d_64cfaa6daf2e-------)

[[![Minh's Tech
Blogging](https://miro.medium.com/fit/c/40/40/0*bZGKzj1IlEtOYFZV)](/@thaominn-178?source=read_next_recirc
---------3---------------------70a8cf2b_321c_48eb_955d_64cfaa6daf2e-------)

[Minh's Tech Blogging

](/@thaominn-178?source=read_next_recirc---------3---------------------
70a8cf2b_321c_48eb_955d_64cfaa6daf2e-------)

in

[SotaTek

](https://medium.com/sota-tek-jsc?source=read_next_recirc---------3
---------------------70a8cf2b_321c_48eb_955d_64cfaa6daf2e-------)

## SotaTek Partners With Algorand: Exclusive TEAL App Development

![](https://miro.medium.com/focal/112/112/50/50/0*KBjcHbWAApgvKn5I.jpg)](/sota-
tek-jsc/sotatek-partners-with-algorand-exclusive-teal-app-development-
adc00e8694b6?source=read_next_recirc---------3---------------------
70a8cf2b_321c_48eb_955d_64cfaa6daf2e-------)

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

