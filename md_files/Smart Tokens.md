[](https://medium.com/)

[Get unlimited access](https://medium.com/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/3c59a6b770ef&~feature=LoOpenInAppButton&~channel=ShowPostUnderUser&~stage=mobileNavBar)

[](https://medium.com/)

[Home](https://medium.com/)

[Notifications](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Primitive](https://miro.medium.com/fit/c/96/96/1*IJFmMdSn_ypT6FdYvG-f0g.png)](/?source=post_page
-----3c59a6b770ef--------------------------------)

[Primitive](/?source=post_page-----
3c59a6b770ef--------------------------------)

Follow

May 8, 2020

·

6 min read

# Smart Tokens

![](https://miro.medium.com/max/772/1*WvwYAX_2N0_-2LdxC46Y9Q.jpeg)

Prometheus Carrying Fire — Jan Cossiers (1600–1671) — Prado Museum

# tl:dr: Smart tokens are ERC-20 tokens with extra features.

The ERC-20 standard is powerful for a few reasons, but one of them is how easy
it is to build liquidity around. These tokens are plugged into liquidity
models with ease, and what we get is a more liquid market that is better for
all parties. Liquidity models will continue to grow and iterate towards zero
impermanent loss, but what about the tokens?

# System Tokens

Many of the most liquid tokens have their value derived from the system it is
embedded in. For example, Dai is derived from the Dai Stablecoin System.
However, Dai _as a token_ isn’t unique, it’s not even called Dai on the Kovan
testnet.

![](https://miro.medium.com/max/1400/1*T8HeRGcZ47-7Wff5Fwp90Q.jpeg)

Maker Dao’s Dai Stablecoin System — <https://github.com/makerdao/dss>

# Smart Tokens

A smart token has a small and simple system baked into it on the contract
level. It’s a primitive that has its value derived from itself rather than an
external system. In this way, it’s ignorant to every other contract on the EVM
and this gives the primitive strength from flexibility.

The Primitive Protocol is designing smart tokens that can be used as pieces to
more complex systems. In addition, we design extension contracts which make
interactions with the smart tokens easier. These pieces will be an additional
set in our arsenal of DeFi legos.

We’ve designed our first smart token with the options market of DeFi in mind.
This is because options on tokens will be one of the fundamental steps in the
growth of DeFi. An option is the right to swap a strike token for an
underlying token; its a limit order frozen in time but only available over a
fixed time period.

## The Prime Smart Token

The Prime is a smart token we’ve designed that matches the specification of a
vanilla option. It has the critical attributes of a vanilla option:
optionality and a fixed lifetime. Users who hold Primes have the ability to
swap their strike tokens into underlying tokens until the Prime _expires_
(fixed lifetime). We’ve baked these properties into the ERC-20 token.

![](https://miro.medium.com/max/1100/1*ImEK_AAvutWEJyod23Bc-A.png)

The Prime Smart Token —Vanilla Option Specification

The functionality of a vanilla option from legacy finance is: the right to buy
or sell the underlying asset for the strike price. To match this
specification, the Prime has a ‘swap’ function which does this action. It will
swap the tokens at a fixed ratio, which is specified when the Prime is
deployed to the EVM (created). Since Primes could be options on any token, and
the denomination could be any token, the ratio between those two quantities is
called the strike ratio.

Legacy options are denominated in local currencies like the US Dollar and this
is called the strike price. Primes are denominated in any strike token, so we
have a strike _ratio_ rather than a strike _price_.

# Extension Contracts

Extension contracts are designed to use the Prime or any smart token as a part
to a larger system. They are built specifically with the user in mind.

## Liquidity Pool

We’ve designed a pool to act as a supply side counter-party. This pool will be
able to meet demand of users who want to buy specific Primes (vanilla
options).

Its capable of doing this because it has logic to do three tasks: (1) Accept
deposits of underlying tokens from liquidity providers, (2) Mint Primes using
the underlying tokens, (3) Sell those Primes for a premium to buyers.

The first task is like any other pool depositing method. When an LP deposits
funds they get a proportional share of liquidity tokens which can be redeemed
for a portion of the pool.

The second task is where the flexibility of the Prime comes in. The Prime
contract knows how to output Primes based on the amount of input underlying
tokens. The pool sends underlying tokens, calls the mint function, and then
receives Prime tokens, which can then be sold.

The third task is more complex. The premium, the value of a vanilla option, is
derived from its intrinsic and extrinsic values. The intrinsic value is the
difference between the strike ratio and the market ratio between the
underlying and strike tokens. To calculate this value, an oracle is needed.
The second difficulty is estimating the extrinsic value, which is based on the
time until expiry and the implied volatility of the option.

## An Oracle

We offload this premium calculation work to another contract called the Prime
Oracle. In the case that the pricing model is inaccurate or the contract has a
bug, we can redeploy a new version of the oracle without affecting the pool.
This is an extension contract that the pool uses as an upgrade-able bridge to
a pricing model.

To calculate the intrinsic value, the pool will use an oracle to get the
current market ratio between the underlying and strike token. It then compares
this amount to the strike ratio, the ratio defined in the Prime contract. The
difference is the _intrinsic_ value. At this stage, we are using Compound’s
oracle, but the final decision on what oracle to use will come down to the
security it can provide.

To calculate the extrinsic value we use the following formula:

![](https://miro.medium.com/max/1400/1*CklTVmcN3l9HXK0w3cBHyQ.jpeg)

Implied Volatility is a difficult value to get and we have not found it. What
we can do is use a proxy for it, and we do that by using the _utilization_ of
the pool; a proxy for demand.

![](https://miro.medium.com/max/1400/1*GkegTNUpqB681vKfyeHGBA.jpeg)

When we combine the intrinsic and extrinsic value, we get the premium. This
premium is fed to the pool, and the pool will sell the Primes to buyers for
this value.

# Systems

This combination of smart tokens and extension contracts is the Primitive
Protocol. With all these parts, such as the pool, oracle, and the base
primitive the Prime, we have a more complex system that was designed to meet a
goal.

Pools, or even other tokens, can design around the specification of the Prime
to create new products, and we expect teams to do this.

 **That is why we are here to help.** If you have a suggestion, request, or
question you can join the protocol’s developers and users in the
[Discord](https://discord.gg/rzRwJ4K).

## Next Steps

As you know, the pool contract that was initially deployed to mainnet had a
bug in it, which led us to pause the contract. We have been making changes to
the pool contract and testing it for the past seven days. We are hoping we
could have a limited _alpha_ version of this contract ready to go for a
_small_ amount of test funds to go through it within the next week.

Currently, the
[Prime](https://etherscan.io/address/0xced83f96aa38bfe34617ea1f699f9f0022548f61)
smart token is on mainnet with a
[_Trader_](https://etherscan.io/address/0xff5c103d76586bb55bb33ce01f3dec9cee55617f)
contract that makes it easy to interact with the Prime. Keep in mind, these
contracts have not been secured yet. Any funds that are held in these
contracts are effectively 100% at risk.

Our priority is security and we are taking the steps to secure the contracts
for the V1 release.

## Twitter

Follow us on [twitter](https://twitter.com/PrimitiveFi) to get the latest
updates.

## Documentation

Our [documentation](https://docs.primitive.finance) has the details of the
protocol! The contract documentation is currently being added. The contracts
are still subject to many more changes.

\--

\--

\--

## [More from Primitive](/?source=post_page-----
3c59a6b770ef--------------------------------)

Follow

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fef69815f4399&operation=register&redirect=https%3A%2F%2Fprimitivefinance.medium.com%2Fsmart-
tokens-3c59a6b770ef&newsletterV3=60c08806472a&newsletterV3Id=ef69815f4399&user=Primitive&userId=60c08806472a&source=-----3c59a6b770ef
---------------------subscribe_user-----------)

Permissionless options protocol. Built on Ethereum.

Love podcasts or audiobooks? Learn on the go with our new app.

[Try
Knowable](https://knowable.fyi/?utm_source=medium&utm_medium=referral&utm_campaign=medium-
post-footer&source=post_page-----3c59a6b770ef--------------------------------)

## Recommended from Medium

[[![YooShi](https://miro.medium.com/fit/c/40/40/1*V5ExlsMSwxL_msAtlw16RA.png)](https://yooshi.medium.com/?source=post_internal_links
---------0----------------------------)

[YooShi

](https://yooshi.medium.com/?source=post_internal_links---------
0----------------------------)

## YooShi Diary- May 21

![](https://miro.medium.com/focal/112/112/50/50/1*We9MPPZFhz_PuVMyYeTRmg.jpeg)](https://yooshi.medium.com/yooshi-
diary-may-21-56123c08248b?source=post_internal_links---------
0----------------------------)

[[![CryptoBuyClub - Latest Crypto Buying
Guide](https://miro.medium.com/fit/c/40/40/1*XK0LREDzbXHMAiCcUFAK4w.png)](https://cryptobuyclub.medium.com/?source=post_internal_links
---------1----------------------------)

[CryptoBuyClub - Latest Crypto Buying Guide

](https://cryptobuyclub.medium.com/?source=post_internal_links---------
1----------------------------)

in

[Coinmonks

](https://medium.com/coinmonks?source=post_internal_links---------
1----------------------------)

## How to Buy Sanin Inu Coin ($SANI) — Beginner’s Guide

![How to Buy Sanin Inu Coin
\($SANI\)](https://miro.medium.com/focal/112/112/50/50/0*BbxeKmdY2UMmCU_L.png)](https://cryptobuyclub.medium.com/how-
to-buy-sanin-inu-coin-sani-beginners-
guide-b98f8428bd2a?source=post_internal_links---------
1----------------------------)

[[![Albacore
Labs](https://miro.medium.com/fit/c/40/40/1*mVQ6zPaLbLoUUdjK2yZI3g.png)](https://medium.com/@albacorelabs?source=post_internal_links
---------2----------------------------)

[Albacore Labs

](https://medium.com/@albacorelabs?source=post_internal_links---------
2----------------------------)

## Becoming Satoshi: The susceptibility of the crypto-ecosystem to
misinformation

![](https://miro.medium.com/focal/112/112/50/50/1*pnNDKevfR51uJ9NY5M2z_g.png)](https://medium.com/@albacorelabs/becoming-
satoshi-the-susceptibility-of-the-crypto-ecosystem-to-
misinformation-b0edd45b578c?source=post_internal_links---------
2----------------------------)

[[![Utopia](https://miro.medium.com/fit/c/40/40/1*auPoSC-Q-mmS-
akeuAbJKQ.png)](https://utopiacoin.medium.com/?source=post_internal_links
---------3----------------------------)

[Utopia

](https://utopiacoin.medium.com/?source=post_internal_links---------
3----------------------------)

## Utopia’s Pre IDO Whitelist Competition Open Now

](https://utopiacoin.medium.com/utopias-pre-ido-whitelist-competition-open-
now-ffe50472244e?source=post_internal_links---------
3----------------------------)

[[![Ubikiri](https://miro.medium.com/fit/c/40/40/2*_762WwsYjmOTi-8aylhN9g.png)](https://medium.com/@ubikiri?source=post_internal_links
---------4----------------------------)

[Ubikiri

](https://medium.com/@ubikiri?source=post_internal_links---------
4----------------------------)

## Ubikiri introduction.

](https://medium.com/@ubikiri/ubikiri-
introduction-9a6326a6b2e5?source=post_internal_links---------
4----------------------------)

[[![Scrate](https://miro.medium.com/fit/c/40/40/1*EV4INbTw4faHbu1sTwKuaQ.png)](https://scrateio.medium.com/?source=post_internal_links
---------5----------------------------)

[Scrate

](https://scrateio.medium.com/?source=post_internal_links---------
5----------------------------)

## Falcon Project AMA ReCap

![](https://miro.medium.com/focal/112/112/50/50/1*_SriXgro9xutuW3Wgh02IQ.jpeg)](https://scrateio.medium.com/falcon-
project-ama-recap-1d4d60dec18c?source=post_internal_links---------
5----------------------------)

[[![Satori
Research](https://miro.medium.com/fit/c/40/40/0*KUupMPgeUkJJtPow.jpg)](https://researchsatori.medium.com/?source=post_internal_links
---------6----------------------------)

[Satori Research

](https://researchsatori.medium.com/?source=post_internal_links---------
6----------------------------)

## Another Bull Bites the Dust

![](https://miro.medium.com/focal/112/112/50/50/1*aIKi2hB3jxHyl_T6hi1C0g.png)](https://researchsatori.medium.com/another-
bull-bites-the-dust-70591e41f76?source=post_internal_links---------
6----------------------------)

[[![Semadalabs](https://miro.medium.com/fit/c/40/40/0*DymKqrJwB5Lot2Ld.jpg)](https://medium.com/@semadaresearch?source=post_internal_links
---------7----------------------------)

[Semadalabs

](https://medium.com/@semadaresearch?source=post_internal_links---------
7----------------------------)

in

[@semadaresearch

](https://medium.com/semadaresearch?source=post_internal_links---------
7----------------------------)

## Semada’s Analysis of the Reserve Stable Currency Protocol

![](https://miro.medium.com/focal/112/112/50/50/1*Th48HN_qKSjQs_8QrSZiYQ.jpeg)](https://medium.com/@semadaresearch/semadas-
analysis-of-the-reserve-stable-currency-
protocol-b9746743f2c8?source=post_internal_links---------
7----------------------------)

[](https://medium.com/?source=post_page-----
3c59a6b770ef--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
3c59a6b770ef--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
3c59a6b770ef--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
3c59a6b770ef--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
3c59a6b770ef--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----3c59a6b770ef--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----3c59a6b770ef--------------------------------)

[Get
started](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fprimitivefinance.medium.com%2Fsmart-
tokens-3c59a6b770ef&source=post_page--------------------------
nav_reg-----------)

[![Primitive](https://miro.medium.com/fit/c/176/176/1*IJFmMdSn_ypT6FdYvG-f0g.png)](/)

[

## Primitive

](/)

135 Followers

Permissionless options protocol. Built on Ethereum.

Follow

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fef69815f4399&operation=register&redirect=https%3A%2F%2Fprimitivefinance.medium.com%2Fsmart-
tokens-3c59a6b770ef&newsletterV3=60c08806472a&newsletterV3Id=ef69815f4399&user=Primitive&userId=60c08806472a&source=--------------------------subscribe_user-----------)

## More from Medium

[[![0bOptions](https://miro.medium.com/fit/c/40/40/1*NZL1TL-
pSGV3tQCtNYA6Xg.png)](https://medium.com/@0bOptions?source=read_next_recirc
---------0---------------------a5522805_a317_4f5f_8ec6_98f066d6eefb-------)

[0bOptions

](https://medium.com/@0bOptions?source=read_next_recirc---------0
---------------------a5522805_a317_4f5f_8ec6_98f066d6eefb-------)

## 0bOptions Integrates Chainlink Keepers to Decentralize the Automation of
Its Prediction Market

![](https://miro.medium.com/focal/112/112/50/50/0*vcXAvLja9DNGefWx)](https://medium.com/@0bOptions/0boptions-
integrates-chainlink-keepers-to-decentralize-the-automation-of-its-prediction-
market-44fe33e8949a?source=read_next_recirc---------0---------------------
a5522805_a317_4f5f_8ec6_98f066d6eefb-------)

[[![Xander
Hoskinson](https://miro.medium.com/fit/c/40/40/1*OLhtydi5l7k3xe0SKservQ@2x.jpeg)](https://xanderhoskinson.medium.com/?source=read_next_recirc
---------1---------------------a5522805_a317_4f5f_8ec6_98f066d6eefb-------)

[Xander Hoskinson

](https://xanderhoskinson.medium.com/?source=read_next_recirc---------1
---------------------a5522805_a317_4f5f_8ec6_98f066d6eefb-------)

## Liquid Staking with Solana — Lido & Orca

![](https://miro.medium.com/focal/112/112/50/50/1*k2n7OudrSkjjkm19npxEFg.png)](https://xanderhoskinson.medium.com/liquid-
staking-with-solana-lido-orca-ef4e2d58fe3a?source=read_next_recirc---------1
---------------------a5522805_a317_4f5f_8ec6_98f066d6eefb-------)

[[![MoonRock](https://miro.medium.com/fit/c/40/40/1*34suloMDfhoqlN0_2lCXSg.png)](https://medium.com/@moonrockofficial?source=read_next_recirc
---------2---------------------a5522805_a317_4f5f_8ec6_98f066d6eefb-------)

[MoonRock

](https://medium.com/@moonrockofficial?source=read_next_recirc---------2
---------------------a5522805_a317_4f5f_8ec6_98f066d6eefb-------)

## RockSwap: How to Swap USDC to SOL

![](https://miro.medium.com/focal/112/112/50/50/1*qo9NEOCxsuOHIMra7RHxhQ.png)](https://medium.com/@moonrockofficial/rockswap-
how-to-swap-usdc-to-sol-33984eedb444?source=read_next_recirc---------2
---------------------a5522805_a317_4f5f_8ec6_98f066d6eefb-------)

[[![Float](https://miro.medium.com/fit/c/40/40/1*J7CTogn8-RTn8wMQJVX3ew.png)](https://medium.com/@_FLOAT_?source=read_next_recirc
---------3---------------------a5522805_a317_4f5f_8ec6_98f066d6eefb-------)

[Float

](https://medium.com/@_FLOAT_?source=read_next_recirc---------3
---------------------a5522805_a317_4f5f_8ec6_98f066d6eefb-------)

## Float Capital Integrates Chainlink Price Feeds to Help Secure Magic
Internet Assets on Avalanche

![](https://miro.medium.com/focal/112/112/50/50/0*Th9csIUYvrnHjGCp)](https://medium.com/@_FLOAT_/float-
capital-integrates-chainlink-price-feeds-to-help-secure-magic-internet-assets-
on-avalanche-db1b20eae985?source=read_next_recirc---------3
---------------------a5522805_a317_4f5f_8ec6_98f066d6eefb-------)

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

