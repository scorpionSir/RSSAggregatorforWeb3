[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/742e30be9780&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![DefiDollar](https://miro.medium.com/fit/c/64/64/1*acjRchHa7v0vT46m5lAQVQ.png)](https://medium.com/defidollar?source=post_page
-----742e30be9780--------------------------------)

Published in

[DefiDollar

](https://medium.com/defidollar?source=post_page-----
742e30be9780--------------------------------)

[![atvanguard](https://miro.medium.com/fit/c/96/96/1*Bm8one51ZA1c3k8Oty022w.jpeg)](/@atvanguard?source=post_page
-----742e30be9780--------------------------------)

[atvanguard](/@atvanguard?source=post_page-----
742e30be9780--------------------------------)

Follow

May 24, 2020

·

5 min read

# Introducing DefiDollar

Quite recently there has been a lot of discussion about Dai moving from its
peg and the hassle of involved governance proposals to maintain its stability.
Also, even centralized stable coins are often trading above or below the peg.

Other risks associated with centralized coins include counterparty risk, bank
run risks, asset seizure risk, and effects from negative interest rates.

# DefiDollar

![](https://miro.medium.com/max/1400/1*DrTXRuzl9AZMA7qjL8hwpQ.png)

 _DefiDollar_ is an attempt at being an **index of stable coins** that uses
Defi primitives to **stay near the dollar mark** and **subsidize the
collateralization ratio**. Let me demonstrate the mechanics of the DefiDollar
by walking you through its complete lifecycle.

  * Since DefiDollar (DUSD) is backed by existing stable coins, for the sake of the illustration, we start with choosing two stable coins, _A_ and _B_ for e.g. Dai and sUSD as the underlying reserves, in an equal ratio.
  * To mint 200 DUSD, the user deposits 100 coins each of _A_ and _B_.
  * Within the mint transaction, _A_ and _B_ are locked in [Aave](https://aave.com/), and the corresponding interest-bearing Aave coins _aA_ and _aB_ are deposited in a liquidity ([balancer](https://docs.balancer.finance/)) pool. Interest income from Aave is redirected to an _earnings pool_.
  *  _aA_ and _aB_ in the pool can be traded using an Automated Market Maker mechanism (a pool-based swap mechanism used by Uniswap and [curve.fi](http://curve.fi) and for which balancer provides a framework).

![](https://miro.medium.com/max/1400/0*oXZ3uSS2SecF6Dhd)

The DefiDollar way

  * Now, say the price of A fluctuates to $1.1 and B goes to $0.9.
  * This opens an arbitrage opportunity since, in the pool, A and B are still in a 1:1 ratio. Hence, arbitrageurs will trade _A_ for _B_ from the pool which will cause the values of both the pools to come close to $100 each and the DefiDollar will be balanced again. A small fee from these trades will also be directed to the _earnings pool._

While the arbitrage opportunity discussed above will keep the _relative_
_prices_ of the underlying coins in sync, there is still a possibility that
the DefiDollar slips from its peg. A couple of such scenarios are when all of
the underlying coins have fallen above or below the $1 mark.

# Oracles

To be able to explain this, let me draw your attention back to the _earnings
pool_ discussed above, which was accruing earnings from the interest and trade
fees. Let’s say this pool has accrued 5 coins of A and B each over some time.
This pool will act as a volatility cushion.

Say the price of _A_ and _B_ has dropped to $0.97 and $0.98 respectively and
so DUSD would be at about $0.975. To rebalance the pools again, an oracle
(chainlink) would periodically be pushing prices of the underlying coins to
the core smart contract.

![](https://miro.medium.com/max/1400/0*t7mwk8gRs2J5sxMF)

Prices are fetched from the chainlink reference contract

Since the pool of _A_ is valued at $97; to cover the deficit of $3, the
protocol will send (3 / .97) = 3.092 coins from the _earnings pool_ to the
main pool. Similarly, the pool of _B_ is in a deficit of $2, and hence (2 /
0.98) = 2.04 of B will be sent to the main liquidity pool. This way DefiDollar
will be at the $ mark again.

After there are enough funds for the volatility cushion, any following
earnings will act as the protocol fee.

# What happens if the DefiDollar moves from its peg?

If DUSD is trading above the peg, there is an instant profit to be made since
the protocol allows one to generate a DUSD by locking $1 worth of other
stablecoins. Arbitrageurs will mint more DefiDollars and sell them in markets
causing the price to be driven down.

If DUSD is trading below the peg, there is instant profit to be made since the
protocol allows to redeem one DUSD for $1 worth of other stablecoins.
Arbitrageurs will buy the coins and redeem them from the protocol causing the
price to be driven up.

The above mechanism is different from how the Maker system works. Following is
an excerpt from[ _The Rise of
sUSD_](https://synthetix.community/blog/2020/04/13/the-rise-of-susd#the-
missing-gear).

> Maker is a clever system: levers and pulleys designed to maintain a soft peg
> without coercion. A combination of monetary policy and arbitrage
> opportunities drives the peg towards $1 in either direction. But, during a
> period in March 2019 when the peg was drifting slightly, Twitter user and
> DeFi whisperer @DegenSpartan highlighted a [**subtle crack in the arbitrage
> model**](https://twitter.com/DegenSpartan/status/1103189312529620993).
>
> When the peg is under $1, the Maker system theoretically incentivizes CDP
> owners − the users who have leveraged their ETH collateral to mint DAI − to
> buy back the stablecoin at a discount to repay their debt below cost.
> However, this mechanism wasn’t quite working that March, and to understand
> why, we need to remember that the most common type of CDP user is someone
> who is long ETH and wants to lever up using DAI. At this stage in the market
> cycle, the market sentiment was overwhelmingly bullish. Unfortunately for
> the peg, **a couple of cents of arbitrage wasn’t enough to encourage enough
> traders to unwind their positions**.
>
> There are always some arbitrageurs waiting in the wings, but at some point
> the overlap between CDP owners and traders positioned to perform arbitrage
> disappears. And the equilibrium price where this occurs could very well be
> 96 or 97 or 98 cents.

# Key Benefits

  * A more stable coin.
  * Stablecoin hedging
  * An avenue for AMM based efficient stable coin swaps.
  * Requires minimal governance.
  * Captures the momentary upticks in yield of a particular underlying asset i.e. it is common to see Dai, sUSD, bUSD giving out 30%+ APR but only for a few hours.
  * Risk diversification. The protocol will be unopinionated about whether centralized coins can be used as an underlying asset. However, there is likely some substantial diversification potential.

# Live on Kovan Testnet

DefiDollar is live on the kovan testnet and can be played around with on
[https://defidollar.xyz/](http://defidollar.xyz/). We currently support DAI,
TUSD and MKR (swapped to underlying assets through Uniswap V2) to mint DUSD.
These coins can be obtained from the faucet links beneath the input amount box
in our app. Kovan ETH can be obtained from the
[faucet](https://faucet.kovan.network/). We also have a dark mode!

![](https://miro.medium.com/max/1400/1*EGBeeLLsc9hO5MjL1z6dWQ.png)

If you like the idea please mint/burn some DUSD, swap Aave interest-bearing
coins, rebalance DUSD using the chainlink oracle and let us know your
thoughts. 👋

DefiDollar was created by [Deep Joshi](https://twitter.com/imdeepjoshi), who
worked on all things design, [Manthan Joshi](https://twitter.com/itsmnthn) who
hacked on the frontend and [Arpit](https://twitter.com/atvanguard) who coded
the smart contracts! Our DMs are open :)

\--

\--

\--

## [More from DefiDollar](/defidollar?source=post_page-----
742e30be9780--------------------------------)

Building to simplify open finance for everyone

[Read more from DefiDollar](/defidollar?source=post_page-----
742e30be9780--------------------------------)

## Recommended from Medium

[[![Shinobi
Protocol](https://miro.medium.com/fit/c/40/40/1*CpJwmi6F4sppjf1onfmcOQ.png)](/@ShinobiProtocol?source=post_internal_links
---------0----------------------------)

[Shinobi Protocol

](/@ShinobiProtocol?source=post_internal_links---------
0----------------------------)

## Public Beta Test Overview

![](https://miro.medium.com/focal/112/112/50/50/1*LU3KbG3ap5f2LhbwMkBQlQ.png)](/@ShinobiProtocol/public-
beta-test-overview-c56ff9effc06?source=post_internal_links---------
0----------------------------)

[[![Cryptogenik | SYNC
Network](https://miro.medium.com/fit/c/40/40/1*r_teyFinW7Mf_iuOBYe7BA.png)](/@cryptogenik?source=post_internal_links
---------1----------------------------)

[Cryptogenik | SYNC Network

](/@cryptogenik?source=post_internal_links---------
1----------------------------)

in

[SYNC Network

](https://medium.com/sync-network?source=post_internal_links---------
1----------------------------)

## New Artists DG NFT exposition

![](https://miro.medium.com/focal/112/112/50/50/1*4PbyTMY_5OZVVAx7k9VAYg.jpeg)](/sync-
network/new-artists-dg-nft-exposition-c381c1e2ccb8?source=post_internal_links
---------1----------------------------)

[[![Poor
Richard](https://miro.medium.com/fit/c/40/40/1*pJzV13iIby7L-ljK3Alilw.gif)](/@prrichard61?source=post_internal_links
---------2----------------------------)

[Poor Richard

](/@prrichard61?source=post_internal_links---------
2----------------------------)

## Seamless Web of Deserved Trust $DAG powered by Constellation Network

![](https://miro.medium.com/focal/112/112/50/50/1*C5l2kB5CvUd7MHTZkoGOCQ.png)](/@prrichard61/seamless-
web-of-deserved-trust-dag-powered-by-constellation-
network-b8d5abea3d9e?source=post_internal_links---------
2----------------------------)

[[![Ekaterina
Kulikova](https://miro.medium.com/fit/c/40/40/0*XlrLC_ACQsaxfhta)](/@forkulikova?source=post_internal_links
---------3----------------------------)

[Ekaterina Kulikova

](/@forkulikova?source=post_internal_links---------
3----------------------------)

## Crodo

![](https://miro.medium.com/focal/112/112/50/50/0*Qqja-
bxhDgFpLBpc)](/@forkulikova/crodo-e4bae2cfd58?source=post_internal_links
---------3----------------------------)

[[![Cryptokruelty](https://miro.medium.com/fit/c/40/40/1*mxLtTajW3e0MlbWkHIMWgw.jpeg)](/@cryptokruelty?source=post_internal_links
---------4----------------------------)

[Cryptokruelty

](/@cryptokruelty?source=post_internal_links---------
4----------------------------)

## The truth behind Safemoon, Piggybanktoken, Cake Monster, Nobility, and
Rocketbusd.

![](https://miro.medium.com/focal/112/112/50/50/1*7PTIGv4CRO1euCVPAgZ9EA.png)](/@cryptokruelty/the-
truth-behind-safemoon-piggybanktoken-cake-monster-nobility-and-
rocketbusd-21158f32ed64?source=post_internal_links---------
4----------------------------)

[[![Patrick
Waller](https://miro.medium.com/fit/c/40/40/1*zcu_iKu8fAilAWgP658LBA.jpeg)](/@firewaller?source=post_internal_links
---------5----------------------------)

[Patrick Waller

](/@firewaller?source=post_internal_links---------
5----------------------------)

## Getting started: Cryptocurrency

![](https://miro.medium.com/focal/112/112/61/28/1*jmSnfcKXXwi6F55QXrRqOA.jpeg)](/@firewaller/getting-
started-cryptocurrency-7d249366aab3?source=post_internal_links---------
5----------------------------)

[[![Crypto
Lemon](https://miro.medium.com/fit/c/40/40/1*wuYJoiWWrdUxj3fOgOEQSg.jpeg)](/@crypto-
lemon?source=post_internal_links---------6----------------------------)

[Crypto Lemon

](/@crypto-lemon?source=post_internal_links---------
6----------------------------)

## Gaming behemoths are about to enter the P2E world

![](https://miro.medium.com/focal/112/112/50/50/0*1zjCkjp6p__4LwKp.png)](/@crypto-
lemon/gaming-behemoths-are-about-to-enter-
the-p2e-world-a811a69c49b1?source=post_internal_links---------
6----------------------------)

[[![Rob
Knight](https://miro.medium.com/fit/c/40/40/1*kiBsi5BR4UXNED5VVb0GuQ.jpeg)](/@rob-
flickto?source=post_internal_links---------7----------------------------)

[Rob Knight

](/@rob-flickto?source=post_internal_links---------
7----------------------------)

in

[Flickto

](https://medium.com/flickto?source=post_internal_links---------
7----------------------------)

## It’s time for another Flickto NFT drop!

](/flickto/its-time-for-another-flickto-nft-drop-
ce7ae8627f7b?source=post_internal_links---------7----------------------------)

[](/?source=post_page-----742e30be9780--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
742e30be9780--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
742e30be9780--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
742e30be9780--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
742e30be9780--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----742e30be9780--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----742e30be9780--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fdefidollar%2Fintroducing-
defidollar-742e30be9780&source=post_page--------------------------
nav_reg-----------)

[![atvanguard](https://miro.medium.com/fit/c/176/176/1*Bm8one51ZA1c3k8Oty022w.jpeg)](/@atvanguard)

[

## atvanguard

](/@atvanguard)

588 Followers

Building @HubbleExchange

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F484fb0d114bc&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fdefidollar%2Fintroducing-
defidollar-742e30be9780&newsletterV3=694ca2a647c1&newsletterV3Id=484fb0d114bc&user=atvanguard&userId=694ca2a647c1&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Angle](https://miro.medium.com/fit/c/40/40/1*5qGUSOK5O8GX5kQAsdLVfg.png)](/@angleprotocol?source=read_next_recirc
---------0---------------------53c4439c_c5ab_4a7f_85ee_730e3c06bdde-------)

[Angle

](/@angleprotocol?source=read_next_recirc---------0---------------------
53c4439c_c5ab_4a7f_85ee_730e3c06bdde-------)

in

[Angle Protocol

](https://medium.com/angle-protocol?source=read_next_recirc---------0
---------------------53c4439c_c5ab_4a7f_85ee_730e3c06bdde-------)

## Angle Router is Live!

![](https://miro.medium.com/focal/112/112/50/50/1*t5-po9KHNmm7Qz7JeUd_ug.png)](/angle-
protocol/angle-router-is-live-91138c8eceec?source=read_next_recirc---------0
---------------------53c4439c_c5ab_4a7f_85ee_730e3c06bdde-------)

[[![Perpetual
Protocol](https://miro.medium.com/fit/c/40/40/1*IBeJPzrwlCYNmfS5P7ltkA.png)](/@perpetualprotocol?source=read_next_recirc
---------1---------------------53c4439c_c5ab_4a7f_85ee_730e3c06bdde-------)

[Perpetual Protocol

](/@perpetualprotocol?source=read_next_recirc---------1---------------------
53c4439c_c5ab_4a7f_85ee_730e3c06bdde-------)

in

[Perpetual Protocol

](https://medium.com/perpetual-protocol?source=read_next_recirc---------1
---------------------53c4439c_c5ab_4a7f_85ee_730e3c06bdde-------)

## Announcing the PERP Convertible Voucher Offering

![](https://miro.medium.com/focal/112/112/50/50/0*x0HkDKDGwzdTTOC2)](/perpetual-
protocol/announcing-the-perp-convertible-voucher-
offering-5587715fa03c?source=read_next_recirc---------1---------------------
53c4439c_c5ab_4a7f_85ee_730e3c06bdde-------)

[[![Yaron
Velner](https://miro.medium.com/fit/c/40/40/0*4wc5mMqfaMTZO6vi.jpg)](/@yaron_velner?source=read_next_recirc
---------2---------------------53c4439c_c5ab_4a7f_85ee_730e3c06bdde-------)

[Yaron Velner

](/@yaron_velner?source=read_next_recirc---------2---------------------
53c4439c_c5ab_4a7f_85ee_730e3c06bdde-------)

in

[B.Protocol

](https://medium.com/b-protocol?source=read_next_recirc---------2
---------------------53c4439c_c5ab_4a7f_85ee_730e3c06bdde-------)

## B.Protocol <> Vesta Integration is LIVE!

![](https://miro.medium.com/focal/112/112/50/50/0*ir-
YYtvAhD1V6Cgd)](/b-protocol/b-protocol-vesta-integration-is-
live-3f5173169de7?source=read_next_recirc---------2---------------------
53c4439c_c5ab_4a7f_85ee_730e3c06bdde-------)

[[![Matt Marks](https://miro.medium.com/fit/c/40/40/1*sug0xHnU-
lrYeBK8HbOySg.jpeg)](/@MattFromVIA?source=read_next_recirc---------3
---------------------53c4439c_c5ab_4a7f_85ee_730e3c06bdde-------)

[Matt Marks

](/@MattFromVIA?source=read_next_recirc---------3---------------------
53c4439c_c5ab_4a7f_85ee_730e3c06bdde-------)

in

[via-exchange

](https://medium.com/via-exchange?source=read_next_recirc---------3
---------------------53c4439c_c5ab_4a7f_85ee_730e3c06bdde-------)

## Summary on DeFi from past Q1

![](https://miro.medium.com/focal/112/112/50/50/1*49QzhjdUy2cFvn4TMf0f9A.png)](/via-
exchange/summary-on-defi-from-past-q1-ad12ffe35e3b?source=read_next_recirc
---------3---------------------53c4439c_c5ab_4a7f_85ee_730e3c06bdde-------)

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

