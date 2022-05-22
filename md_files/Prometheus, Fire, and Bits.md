[](https://medium.com/)

[Get unlimited access](https://medium.com/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/c0a164d3c157&~feature=LoOpenInAppButton&~channel=ShowPostUnderUser&~stage=mobileNavBar)

[](https://medium.com/)

[Home](https://medium.com/)

[Notifications](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Primitive](https://miro.medium.com/fit/c/96/96/1*IJFmMdSn_ypT6FdYvG-f0g.png)](/?source=post_page
-----c0a164d3c157--------------------------------)

[Primitive](/?source=post_page-----
c0a164d3c157--------------------------------)

Follow

May 1, 2020

·

8 min read

# Prometheus, Fire, and Bits

![](https://miro.medium.com/max/1400/1*IgDXx-Pk-8GntiiHIg_hTw.jpeg)

Prometheus tortured by the eagle. Christian Griepenkerl (1839–1916).

In Greek mythology, the Titan Prometheus steals fire from the Gods and brings
it to Earth’s humanist civilization. Also accredited with molding humanity
from clay, the rebellious Titan was eternally punished for his theft of fire.
However, with fire, humans could extend their civilization beyond their clay
limitations and into an energetic force. Innovation preceded by theft against
the old gods pushed us forward.

## The Primitive Protocol

Primitive designs base smart contracts that operate under the conditions of
ignorance and bliss. These primitives serve as tools for protocols on DeFi to
use, including our own protocol.

##  **Alpha Release Features:**

  * ETH Put ERC-20 Token with 200 DAI strike price expiring May 30, 2020.
  * Liquidity Pool for DAI that mints put option tokens and sells them for premium.
  * Premium charged by pool based on the pool’s utilization, a proxy for volatility.

## Prime

The first contract we have designed is the Prime, a base ‘smart’ ERC-20 binary
option primitive. A holder of a Prime has the right to swap Token A to Token
B, which was wrapped into the Prime, at a fixed exchange rate, for a fixed
lifetime. This is similar to a binary option, because the holder is betting
that the market exchange rate between Token A and Token B will eventually be
greater than the exchange rate defined in the Prime. This ability to swap,
also called the right to exercise, has a limited period of availability. Each
Prime has an embedded strike date, which is when the Prime will ‘expire’. Upon
expiry, the ability to exercise and mint new Primes is locked.

## Mainnet and Community

We are live on mainnet as of today, May 1st, 2020. Our goal is to build
community on day zero, when the protocol is still seeding itself into the
world of DeFi. The next development cycles will be taking the community’s
sentiment as a key input to what is built. The usefulness of our primitives
starts with the users and builders in our community and this is why it is
critical for us to start developing that relationship starting now.

## Risk and Security

The contracts are not secure and anyone who interacts with them are putting
their funds at risk. The front-end interface continues to be a work in
progress. Our focus during this early period of development has been on the
security of the contracts, rather than the front-end interface. We have gone
through multiple iterations and have settled on a simple design which can be
both improved and built upon going forward.

##  **The Prime as an Option ERC-20 Token Primitive**

Primes are relatively cheap. The value of Primes decays over time as their
strike date gets closer, which makes them useful for short-term hedging
instruments. As a user, I can buy a Prime which effectively locks in an
exchange rate between two tokens, that can be exercised at some future time
before expiry. The key benefit is that I do not have to put up the capital to
exercise the swap until I want to exercise. The only price paid is the
premium, which is often much less than the assets the Prime has effective
control over.

Our mantra for designing primitives is: “Strength, Security, and Simplicity”.
In the Prime contract, there are four core functions which each take different
token inputs and output different results. The contract assumes tokens are
sent into it before its functions are called. This is because the contract
caches its balance at the end of every transaction so in the next transaction
they can compare the current balance with the previous balance. The difference
in these balances is how many tokens were sent into the contract, and this
determines how many tokens will be sent out. This gives external contracts and
accounts flexibility because they can determine which tokens to push to the
Prime. The Prime operates with ignorance of how tokens are sent into it, which
drastically simplifies the contract’s code.

## Alpha Architecture

For our alpha release, we have built two contracts that are meant to make
interactions with the Prime simple. Primes are options that need a counter-
party to provide the ‘underlying’ asset, which every Prime wraps into it.
We’ve designed a liquidity pool to serve as a counter-party. We’ve also
designed a trader contract that would allow users to directly mint, swap,
redeem, and close Prime option positions.

##  **Pooled Liquidity**

The pool we have designed for this release is an ETH Short Put pool. Liquidity
Providers (“LP”) will deposit DAI, the DAI is used to mint new ETH Puts, which
are then sold to buyers for premium. The premium’s earned by the pool are
distributed to the LPs based on their provided DAI. LPs in this pool are
betting that the price of ETH will be above 200 DAI (the strike price for the
first Prime option) at May 30, 2020 (the expiration date for the first Prime
option). These options are American style, which means the assets can be
exercised at any time before expiry. LPs are effectively buying ETH at a 200
DAI price, which would attribute a loss to them if the market price of ETH is
below 200 DAI.

The premium that the pool charges is based on the utilization of the pool,
time to expiry, and ‘moneyness’ of the option; the ratio of the strike price
to the market price. If the pool has low utilization, the premium will be
cheap. If the pool has high utilization, the premium will be expensive. This
algorithmic premium should be able to promote demand or supply based on what
the pool needs. This pricing model is actively being researched and developed
on, this release will serve as the first live test of it in action.

## Buying Options from the Pool

Users can hedge against the price of ETH declining by purchasing a Prime from
the pool and holding it. If the price of ETH goes below 200 DAI, Prime holders
start to earn a return. The true breakeven is at a lower price, because the
premium that was paid also needs to be earned back. Once the premium is
earned, net profit starts to accrue. For example, if the price of the Prime is
1 DAI, the strike price is 200 DAI, and the market price is 190 DAI, the user
would profit (200 -1- 190) = 9 DAI if they exercised their Prime option.

There is no direct way for the user to sell their Prime back to the pool. This
is not because of technological limitation, but because of the focus on
security for the alpha release. A pool that supports multiple Primes increases
the surface area for the contracts to be attacked by a factor of four, because
of the additional connections that are made between contracts. The logic for a
pool to handle multiple Prime markets will be developed for the next release.

## Future Pools

This alpha release pool is a short put pool. The next pools we build will have
specific trading strategies that can be more complex. The pool being designed
for the beta release will be taking a synthetic long position on ether. This
works by having the pool write put options using its own pool, while
purchasing call options from another pool. The pool will earn premiums by
writing and selling the ether put options, and then the premiums will be spent
on purchasing ether call options, a synthetic long position. Multiple pools
can be designed to trade specific strategies like this. Lazy capital’s heaven,
where LPs can deposit funds into a pool that trades synthetic longs, spreads,
calendars, etc.

## Risk

The Alpha Primitive release is deployed to mainnet with unaudited contracts.
Users who interact with any Primitive contracts will put their funds at risk.

We have purposefully developed the alpha contracts with limited features,
pause functions, and admin access control in order to mitigate risk.
Ironically, adding access control through an admin key degrades the security
of the contracts, but it gives us more flexibility in the event of a
vulnerability.

##  **Security Risk**

In the event of a vulnerability, and depending on the severity, we can pause
every function except withdraws.

 **Access Control**

In the event an Admin private key is compromised, they would be able to pause
the protocol and set new addresses for the Pool. The level of access control
we’ve integrated into the contracts will not be there in future releases, only
the alpha. The worst case scenario is if a private key was compromised, and
the compromising party added a malicious Prime contract designed to steal the
Pool’s funds.

 **Oracle Risk**

In the event of a flash crash of ether’s DAI price, the only oracle risk is in
the Pool contract. Depending on the severity of the crash and the secondary
effects on the Pool, we can pause the Pool. The Pool charges a premium to
option buyers using the price of ETH in DAI as a parameter, which is what the
oracle provides. The Pool could potentially charge a premium that is lower
than the true value, which would attribute a net loss to the LPs.

 **Surface Area Risk**

The Prime contract which is the ERC-20 option does not have any direct oracle
interactions. It also does not have a direct integration with the pool
contract, it is a standalone contract. This was a purposeful design that
reduces the the possible vectors of attack on the Prime contract.

 **Concentrated Risk**

The Pool contract facilitates the interactions between traders and liquidity
providers, a bridge. However, this is where the most risk is concentrated in
the Primitive Protocol. The Pool contract will hold deposits from LPs while
also facilitating trades with Traders using the Pool’s funds.

 **Liquidity Provider Risk**

LP funds are at risk while they remain unutilized in the Pool, and Traders
funds are at risk when they conduct transactions. Utilized Pool funds are
locked in the Prime contract as underlying assets, which remains separate from
the Pool. Only the holder of the Prime has access to the underlying assets of
that Prime, up until the expiration date.

 **Option Holder (User) Risk**

In the event the Pool has its entire balance sheet drained, underlying and
strike assets, no funds locked in the Prime contract would be affected. At
this point, the Pool would be paused to prevent further damage. A
vulnerability in the Pool contract will likely not affect Prime option
holders, but it is absolutely a possibility.

 **Worst-Case Scenario**

The worst case scenario would be if the Pool used all their funds to
underwrite options, and the Pool’s Prime Redeem balance was drained. In this
case, the Pool has no way to access their underlying assets or claimable
strike assets. Therefore, to mitigate this risk, we have limited the amount of
times that the Redeem balance of the Pool is transferred.

## Zero to One, with Community

We are moving into the development of the Beta, which will bring a new ERC-20
token that is embedded with an option. Imagine a token that has the value of
the base token while simultaneously having the option to swap to another
token…

Join our team for this journey.

## Resources

Twitter: <https://twitter.com/PrimitiveFi>

Github: <https://github.com/primitivefinance/>

Website: <https://alpha.primitive.finance/>

Discord: <https://discord.gg/rzRwJ4K>

Protocol Overview (WIP):
<https://docs.google.com/document/d/19neM6bFmTCBdxLygQbDDJubwcLcuMIx8x2Fs-
llt9sQ/edit?usp=sharing>

## Contracts

PrimeOption Alpha V0:
<https://etherscan.io/address/0xced83f96aa38bfe34617ea1f699f9f0022548f61>

PrimePool Alpha V0:
<https://etherscan.io/address/0xf7a7126C6eB9c2cC0dB9F936bA4d0D5685662830>

PrimeTrader Alpha V0:
<https://etherscan.io/address/0xff5c103d76586bb55bb33ce01f3dec9cee55617f>

PrimeRedeem Alpha V0:
<https://etherscan.io/address/0xb0a4d596939715f203fa9e907935938fedea715f>

\--

1

\--

\--

1

## [More from Primitive](/?source=post_page-----
c0a164d3c157--------------------------------)

Follow

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fef69815f4399&operation=register&redirect=https%3A%2F%2Fprimitivefinance.medium.com%2Fprometheus-
fire-and-
bits-c0a164d3c157&newsletterV3=60c08806472a&newsletterV3Id=ef69815f4399&user=Primitive&userId=60c08806472a&source=-----c0a164d3c157
---------------------subscribe_user-----------)

Permissionless options protocol. Built on Ethereum.

Love podcasts or audiobooks? Learn on the go with our new app.

[Try
Knowable](https://knowable.fyi/?utm_source=medium&utm_medium=referral&utm_campaign=medium-
post-footer&source=post_page-----c0a164d3c157--------------------------------)

## Recommended from Medium

[[![Richie](https://miro.medium.com/fit/c/40/40/1*7uQyGmrMwP1x9__VgGvZKw.jpeg)](https://medium.com/@richie-
fallclis?source=post_internal_links---------0----------------------------)

[Richie

](https://medium.com/@richie-fallclis?source=post_internal_links---------
0----------------------------)

## How to start farming on JustLiquidity

![](https://miro.medium.com/focal/112/112/50/50/1*Cwi-QlqSz-
xjwqVkIBPGRg.jpeg)](https://medium.com/@richie-fallclis/how-to-start-farming-
on-justliquidity-2aef21024c16?source=post_internal_links---------
0----------------------------)

[[![David de Caires
Watson](https://miro.medium.com/fit/c/40/40/1*nvjCfC43g1uXRL8zGLU-
fw.jpeg)](https://ecopragmatist.medium.com/?source=post_internal_links
---------1----------------------------)

[David de Caires Watson

](https://ecopragmatist.medium.com/?source=post_internal_links---------
1----------------------------)

in

[The Kernel

](https://medium.com/generation-atomic?source=post_internal_links---------
1----------------------------)

## How To Turn Nuclear Reactors Into Clean, Green, Money-Printing Machines

![](https://miro.medium.com/focal/112/112/50/50/1*Ev7CcVUIF-
SEW2AwMds5jw.png)](https://ecopragmatist.medium.com/how-to-turn-nuclear-
reactors-into-clean-green-money-printing-
machines-c8b35e8b41b8?source=post_internal_links---------
1----------------------------)

[[![Steven
Jim](https://miro.medium.com/fit/c/40/40/0*tbfAgHDgh0o0R9pw.jpg)](https://stevenjim.medium.com/?source=post_internal_links
---------2----------------------------)

[Steven Jim

](https://stevenjim.medium.com/?source=post_internal_links---------
2----------------------------)

in

[The AMA Room

](https://medium.com/theamaroom?source=post_internal_links---------
2----------------------------)

## DefiCliq with Shantanu Kumar — AMA @ The AMA Room

![](https://miro.medium.com/focal/112/112/50/50/0*1nDwNgaEf3OhlnVs.jpeg)](https://stevenjim.medium.com/deficliq-
with-shantanu-kumar-ama-the-ama-room-c15c4efd9734?source=post_internal_links
---------2----------------------------)

[[![Polygen](https://miro.medium.com/fit/c/40/40/1*LFUj-1H6vdhyzbHIFOTMQw.jpeg)](https://medium.com/@polygen?source=post_internal_links
---------3----------------------------)

[Polygen

](https://medium.com/@polygen?source=post_internal_links---------
3----------------------------)

in

[Polygen Ecosystem

](https://medium.com/polygen-ecosystem?source=post_internal_links---------
3----------------------------)

## Polygon x Polygen Partnership

![](https://miro.medium.com/focal/112/112/50/50/1*WS6J-zQAyuo8v6HGstZl-g.jpeg)](https://medium.com/@polygen/polygon-
x-polygen-partnership-10ae8ab0d7ad?source=post_internal_links---------
3----------------------------)

[[![Satoshi_storyteller](https://miro.medium.com/fit/c/40/40/1*fuW9eWuizZ1G7PwVVYTdug.jpeg)](https://satoshi-
storyteller.medium.com/?source=post_internal_links---------
4----------------------------)

[Satoshi_storyteller

](https://satoshi-storyteller.medium.com/?source=post_internal_links---------
4----------------------------)

in

[SatoshiClub

](https://medium.com/realsatoshiclub?source=post_internal_links---------
4----------------------------)

## AMA Satoshi Club x Timecoin Protocol , October 3rd

![](https://miro.medium.com/focal/112/112/50/50/1*TJNanaxV4cnVo8Qfr3GG8A.jpeg)](https://satoshi-
storyteller.medium.com/ama-satoshi-club-x-timecoin-protocol-
october-3rd-6a7e7ad7bf0a?source=post_internal_links---------
4----------------------------)

[[![ZB
Academy](https://miro.medium.com/fit/c/40/40/1*hvrjrQiNtYGMiWyZsqjINA.png)](https://zbacademy.medium.com/?source=post_internal_links
---------5----------------------------)

[ZB Academy

](https://zbacademy.medium.com/?source=post_internal_links---------
5----------------------------)

## ZB Academy: Sotheby’s considers accepting cryptocurrency payments

![](https://miro.medium.com/focal/112/112/50/50/1*1X3VVIEdTxjQKQZYonEGgQ.jpeg)](https://zbacademy.medium.com/zb-
academy-sothebys-considers-accepting-cryptocurrency-
payments-5a311dde3a1?source=post_internal_links---------
5----------------------------)

[[![WanSwap](https://miro.medium.com/fit/c/40/40/1*ld1jPeSLQpbg9K5YAwCJtA.jpeg)](https://wanbrigade.medium.com/?source=post_internal_links
---------6----------------------------)

[WanSwap

](https://wanbrigade.medium.com/?source=post_internal_links---------
6----------------------------)

in

[WanSwap

](https://medium.com/wanswap?source=post_internal_links---------
6----------------------------)

## Introducing WanSwap — The Wanchain Based Cross-chain Decentralized Exchange
With Automated Market…

![](https://miro.medium.com/focal/112/112/50/50/1*l9GKEQD3eAXnOfnkFULydg.png)](https://wanbrigade.medium.com/introducing-
wanswap-the-wanchain-based-cross-chain-decentralized-exchange-with-automated-
market-5e5f5956c223?source=post_internal_links---------
6----------------------------)

[[![Urban
Crypto](https://miro.medium.com/fit/c/40/40/0*lHpJCKBCkHwZIqws)](https://urbancryptos.medium.com/?source=post_internal_links
---------7----------------------------)

[Urban Crypto

](https://urbancryptos.medium.com/?source=post_internal_links---------
7----------------------------)

## Volatility in Cryptocurrency — Is It a Good Thing?

](https://urbancryptos.medium.com/volatility-in-cryptocurrency-is-it-a-good-
thing-514cfa635110?source=post_internal_links---------
7----------------------------)

[](https://medium.com/?source=post_page-----
c0a164d3c157--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
c0a164d3c157--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
c0a164d3c157--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
c0a164d3c157--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
c0a164d3c157--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----c0a164d3c157--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----c0a164d3c157--------------------------------)

[Get
started](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fprimitivefinance.medium.com%2Fprometheus-
fire-and-bits-c0a164d3c157&source=post_page--------------------------
nav_reg-----------)

[![Primitive](https://miro.medium.com/fit/c/176/176/1*IJFmMdSn_ypT6FdYvG-f0g.png)](/)

[

## Primitive

](/)

135 Followers

Permissionless options protocol. Built on Ethereum.

Follow

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fef69815f4399&operation=register&redirect=https%3A%2F%2Fprimitivefinance.medium.com%2Fprometheus-
fire-and-
bits-c0a164d3c157&newsletterV3=60c08806472a&newsletterV3Id=ef69815f4399&user=Primitive&userId=60c08806472a&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Futureswap](https://miro.medium.com/fit/c/40/40/1*NGMukeROgN1Arm04Ji9MBw.png)](https://medium.com/@futureswap?source=read_next_recirc
---------0---------------------6c662a9a_1c53_4766_975a_30b7190ac821-------)

[Futureswap

](https://medium.com/@futureswap?source=read_next_recirc---------0
---------------------6c662a9a_1c53_4766_975a_30b7190ac821-------)

in

[Futureswap

](https://medium.com/futureswap?source=read_next_recirc---------0
---------------------6c662a9a_1c53_4766_975a_30b7190ac821-------)

## FST Goes Cross-Chain, with Native Bridging between Ethereum and Avalanche

![Image of a pixelated character going through a portal with copy superimposed
in between saying “cross-chain oracle-less bridging | Futureswap + Celer
bridge”](https://miro.medium.com/focal/112/112/50/50/0*mbwPjA166MSgkXXh)](https://medium.com/@futureswap/fst-
goes-cross-chain-with-native-bridging-between-ethereum-and-
avalanche-192880f4825b?source=read_next_recirc---------0---------------------
6c662a9a_1c53_4766_975a_30b7190ac821-------)

[[![Canoe
Capital](https://miro.medium.com/fit/c/40/40/1*THw0ylIhWfng8iKJNHSsSg.jpeg)](https://canoecapital.medium.com/?source=read_next_recirc
---------1---------------------6c662a9a_1c53_4766_975a_30b7190ac821-------)

[Canoe Capital

](https://canoecapital.medium.com/?source=read_next_recirc---------1
---------------------6c662a9a_1c53_4766_975a_30b7190ac821-------)

## The “VE” Fat Middle Thesis

![](https://miro.medium.com/focal/112/112/50/50/0*3fiAtOzfYUhPjuAq.jpeg)](https://canoecapital.medium.com/the-
ve-fat-middle-thesis-2e6401400af?source=read_next_recirc---------1
---------------------6c662a9a_1c53_4766_975a_30b7190ac821-------)

[[![Crypto
Lemon](https://miro.medium.com/fit/c/40/40/1*wuYJoiWWrdUxj3fOgOEQSg.jpeg)](https://medium.com/@crypto-
lemon?source=read_next_recirc---------2---------------------
6c662a9a_1c53_4766_975a_30b7190ac821-------)

[Crypto Lemon

](https://medium.com/@crypto-lemon?source=read_next_recirc---------2
---------------------6c662a9a_1c53_4766_975a_30b7190ac821-------)

## SpiritSwap Tokenomics deep dive

![](https://miro.medium.com/focal/112/112/50/50/1*Xy9q7YBg8quAVZ_Ie454Ag.jpeg)](https://medium.com/@crypto-
lemon/spiritswap-tokenomics-deep-dive-b2180c478d9c?source=read_next_recirc
---------2---------------------6c662a9a_1c53_4766_975a_30b7190ac821-------)

[[![Mushrooms
Finance](https://miro.medium.com/fit/c/40/40/1*5jSsny3rOoSn40SQO3scjA.jpeg)](https://mushroomsfi.medium.com/?source=read_next_recirc
---------3---------------------6c662a9a_1c53_4766_975a_30b7190ac821-------)

[Mushrooms Finance

](https://mushroomsfi.medium.com/?source=read_next_recirc---------3
---------------------6c662a9a_1c53_4766_975a_30b7190ac821-------)

in

[Mushrooms Finance

](https://blog.mushrooms.finance/?source=read_next_recirc---------3
---------------------6c662a9a_1c53_4766_975a_30b7190ac821-------)

## Week #78 Notice of Mushrooms

![](https://miro.medium.com/focal/112/112/50/50/0*6_oBBvf1sfptwLaY.jpg)](https://mushroomsfi.medium.com/week-78-notice-
of-mushrooms-2d4d9060d24d?source=read_next_recirc---------3
---------------------6c662a9a_1c53_4766_975a_30b7190ac821-------)

[Help

](https://help.medium.com/hc/en-us)

[Status

](https://medium.statuspage.io)

[Writers

](https://about.medium.com/creators/)

[Blog

](https://blog.medium.com)

[Careers

](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e)

[Privacy

](https://policy.medium.com/medium-privacy-policy-f03bf92035c9)

[Terms

](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f)

[About

](https://medium.com/about?autoplay=1)

[Knowable

](https://knowable.fyi)

