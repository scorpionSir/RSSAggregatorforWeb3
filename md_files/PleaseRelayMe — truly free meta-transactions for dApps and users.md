[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/5b0f0f1753eb&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![BlockRocket](https://miro.medium.com/fit/c/64/64/1*txNUAyxbcu2dKnsOnhoy_g.png)](https://medium.com/blockrocket?source=post_page
-----5b0f0f1753eb--------------------------------)

Published in

[BlockRocket

](https://medium.com/blockrocket?source=post_page-----
5b0f0f1753eb--------------------------------)

[![James
Morgan](https://miro.medium.com/fit/c/96/96/1*pU0bCzBaLEnySQq0APCjWg.jpeg)](/@james.morgan?source=post_page
-----5b0f0f1753eb--------------------------------)

[James Morgan](/@james.morgan?source=post_page-----
5b0f0f1753eb--------------------------------)

Follow

Jan 29, 2020

·

9 min read

# PleaseRelayMe — truly free meta-transactions for dApps and users

## Leveraging DeFi building blocks like rDAI, Kyber along with the Gas Station
Network with the goal of providing free transactions and easing the onboarding
problem 🌶

![](https://miro.medium.com/max/1400/1*ZGZXJVtrMlV4ONyIqf7bLw.png)

GSN — Solving the user on-boarding challenge

Imagine a dApp universe where the interest from dApp revenue or user staked
collateral could fund your user’s transactions — i.e. at zero cost to the dApp
🚀

Let us introduce you to the _PleaseRelayMe_ project built by us at
[BlockRocket.tech](http://blockrocket.tech).

# Introduction

 _PleaseRelayMe_ is a free to use transaction relayer that harnesses the [Gas
Station Network](https://gsn.openzeppelin.com/). It creates a non-profit, self
funding transaction relayer funded by interest (or old school deposits) which
can be used by all with a configurable fair usage policy per dApp.

A public piece of infrastructure for the wider ecosystem built with tools such
as [rDAI](https://rdai.money) and [Kyber
Network](https://medium.com/u/a9fee3ae58e4?source=post_page-----
5b0f0f1753eb--------------------------------) and using the pioneering work
done by [OpenZepppelin](https://openzeppelin.com),
[Tabookey](https://www.tabookey.com/) and
[MetaCartel](https://www.metacartel.org) on the [Gas Station
Network](https://gsn.openzeppelin.com).

Meta-transactions and gas relayers are clearly a massive win for the ecosystem
but they still exist in application-specific environments funded by individual
dApps even though they could be used by all. Our aim is to use the rDAI
protocol to create a free to use transaction relayer where developers can
funnel the interest (earned via [Compound](https://compound.finance/) in the
case of rDai) in the form of DAI to fund transactions for all to use.

Enabling this will mean that new users to the ecosystem can be shielded from
GAS costs for their first interactions with dApps and the Ethereum ecosystem.
Developers and others with vested interests in growing the community can stake
some DAI with the benefit of free transactions for the dApp to be relayed on
their behalf.

If you’re unfamiliar with what we’ve just mentioned above and or want to learn
about the gas station network, check out these articles from [Yoav
Weiss](https://medium.com/u/c0013a425528?source=post_page-----
5b0f0f1753eb--------------------------------) and
[portis](https://medium.com/u/56bd0a809585?source=post_page-----
5b0f0f1753eb--------------------------------):

[

## 1–800-Ethereum: Gas Stations Network for Toll Free Transactions

### “The greatest victory is that which requires no battle.” — Sun Tzu

medium.com

](/tabookey/1-800-ethereum-gas-stations-network-for-toll-free-
transactions-4bbfc03a0a56)

[

## Sponsor your users’ gas fees with Portis and TabooKey’s Gas Stations
Network

### The Gas Stations Network (EIP-1613), removes one of the biggest hurdles
for onboarding new users: gas fees. In the…

medium.com

](/portis/sponsor-your-users-gas-fees-with-portis-and-tabookey-s-gas-stations-
network-7fd7c8406869)

# The Challenge

The challenge with [existing relay hub
contracts](https://gsn.openzeppelin.com/) is that they only accept ETH
deposits for relay funding. Instead, we want to give dApp developers (like
ourselves) the ability to benefit from interest-earning protocols in order to
fuel transactions for new and or existing dApp users.

What we fundamentally cannot get away from is that the cost of gas is
denominated in Ether.

> How do we convert accrued interest into Ethereum’s native currency (ETH)
> from the rDAI protocol’s DAI and use this for gas relaying?

# Research Insights

## rDAI

Research was kicked off by looking into the [rDAI
Protocol](https://rdai.money/).

> rDai (redeemable DAI) allows you to invest your money in an [Interest
> generating pool, used for collateralized
> loans](https://rdai.money/whatisdefi.html). You still hold on to the exact
> amount you invested, and can spend and transfer it at will.
>
> You also decide who benefits from the generated interest: yourself, a
> community fund, a charity, or a dApp you are using. rDAI is a fungible ERC20
> token, meaning you can send any amount to any user, and they can always
> redeem it 1:1 for DAI

The outcome of the research piece was simply to understand how you go from
depositing DAI to directing the interest at a dApp from a smart contract
perspective.

Conclusions:

  * Any owner of DAI first needs to configure a _hat_. A hat is simply an interest distribution configuration i.e. what address gets the interest earned. This is configurable to multiple recipients if required (Possibility of funding multiple dapps).
  * With a hat configured, you can mint rDAI in exchange for DAI
  * Anyone can transfer interest accrued on behalf of the recipient of the interest
  * The underlying DAI asset is easy to retrieve from the RToken contract

## On-chain Liquidity Provider

Ok, so we can earn interest on our DAI (paid in rDAI) but we still need ETH.
How do we do this? With an on-chain liquidity provider of course!

A couple of options we know of are [Uniswap](https://uniswap.io/) and [Kyber
Network](https://medium.com/u/a9fee3ae58e4?source=post_page-----
5b0f0f1753eb--------------------------------) but plenty of others are popping
up in the #DeFi space. Given the team’s previous experience interfacing with
Kyber at a smart contract level, we opted for that — a future iteration of
this project is envisioned where liquidity providers and interest protocols
could could be configured and plugged in as required.

Both Kyber and Uniswap have DAI to ETH liquidity pools that we could tap into
but not rDAI to ETH. This is not a problem for this project given the ability
to claim the underlying DAI from owning rDAI. Once we realised this, it really
completed the rough picture of what would be involved in trying to go from
accrued interest in DAI to ETH.

# Proof of Concept / MVP

The [RelayHub](https://github.com/openeth-
dev/gsn/blob/master/contracts/RelayHub.sol) smart contract is where a dApp
owner would ordinarily deposit ETH in order to fund meta transactions for
their users. Therefore, we targeted this contract for our proof of concept
project. You can find the Github repo at:

[

## blockrockettech/PleaseRelayMe

### You can't perform that action at this time. You signed in with another tab
or window. You signed out in another tab or…

github.com

](https://github.com/blockrockettech/PleaseRelayMe)

Our initial starting point was building a function for ‘fuelling’ a dApp:

There are a number of assumptions made for the purposes of writing this code:

  1. DAI has already been deposited into the rDAI contract and the hat is pointing all interest at the deployment address of this contract
  2. Only 1 dApp is using the rDAI functionality — if multiple dApps made the _rDAIRelayHub_ a beneficiary, there is no way of splitting up the interest proportionally

Other than that, we’re have tested code that achieves in principle what we
want. It takes any interest accrued, retrieves the underlying DAI, swaps for
ETH and updates the ETH balance in the universal relayer for a dApp 🔥

We deployed this to Kovan and had a play around with it using our very basic
one-page web application that can be found in the above repo.

# Fair Usage Policy

We realise we need to attempt to reduce abuse of this free facility. It could
be as simple as trying to limit the number of times an address can make calls
in a particular time period, for example, 3 calls per 24 hour time period. At
the same time, we could explore much more complicated approaches.

## Incentives

As we all know, most things in life require some form of incentivisation —
whether that's personal, financial, ethical or otherwise. _PleaseRelayMe_ will
need collateral to work at its best but where this comes from needs to be
driven from an incentive. Our thoughts on this are as follows:

  * Developers/maintainers of dApps have incentives to help new users onboard or to remove transaction costs from its users. Therefore, driving increased exposure and usage.
  * Existing users who are invested in platforms, especially platforms which generate income or social recognition, are also incentivised in a similar fashion often in a altruistic manner.

# Where Next

One of the major things that needs addressing is the limitation of a 1 dApp to
relay hub relationship. Hubs are ideally to be for multiple dApps and users.
So how do we solve this?

## Interest Payment Accounts (IPA)

The idea is an IPA _(_ not the beer unfortunately 🍺 _)_ is a smart contract
representing a dApp on the relayers that receives the interest earned by a
rDAI intended for that dApp. A relay hub can then call into an IPA when more
ETH fuel is required for funding transactions.

There are 2 approaches to doing this:

  * Minimal approach — rDAI configuration and minting done outside of _PleaseRelayMe_. The hub just talks to the IPA of a dApp in order to obtain ETH when required and when applicable
  * Full orchestration approach — _PleaseRelayMe_ would go the whole hog from depositing DAI into rDAI to interfacing with the Interest Payment Accounts on behalf of a dApp. Idea being to wrap up the many steps that would have to be orchestrated off-chain into a single transaction (ignoring the initial DAI approval that would be required to kick off the whole process).

In both cases, we feel we have a strong use case for the use of the CREATE2
opcode introduced in the Constantinople Ethereum hard fork:

[

## The CREATE2 OpCode and DApp Onboarding in Ethereum

### The Ethereum network's next major upgrade is the Constantinople upgrade
(was meant to be January 16th but has since…

hackernoon.com

](https://hackernoon.com/the-create2-opcode-and-dapp-onboarding-in-
ethereum-e2178e6c20cb)

With CREATE2 and some syntactic sugar introduced in [Solidity
0.6.2](https://github.com/ethereum/solidity/releases/tag/v0.6.2), we can pre-
generate the addresses of the IPAs using the dApp’s public key as a salt. This
gives us the ability to create a [hat](https://rdai.money/howitworks.html#nav)
in rDAI without the IPA even being deployed.

![](https://miro.medium.com/max/1400/1*ZcQZ_s_LtmnCq9O-HajrTA.png)

Second approach mapped out as best as we understand

Things to consider with both approaches:

  * Ensuring that the ETH balance for a dApp remains enough to execute a ‘refuelling’ transaction — this would require maintaining a threshold balance below which meta-transactions are not funded or automatically trigger a refuel if there is enough interest
  * Making the refuel trigger worthwhile. What we mean by this is considering whether it’s worth triggering a refuel every time there is interest to convert or every time the interest reaches a certain threshold. You wouldn’t fill up your car after every short journey you made so why do it for every bit of interest ‘dust’.

Future iterations could support a number of additional features including:

  * Giving users the ability to pay for transaction fees in DAI or rDAI by routing the appropriate amount directly into the IPA for a dApp.
  * Leveraging multi-collateral DAI and earn interest on a number of ERC20.
  * Allowing split interests payments to fund multi dApps at once.

For a time sequence diagram for approach 2, please see appendix 1.

# Application for one of our dapps — KnownOrigin

The reason we’re all here is because user on-boarding for decentralised
applications is hard.

[KnownOrigin](https://knownorigin.io) currently expects artists using the
platform to have ETH in order to list their artwork in order to make money.
What if they didn’t have to? What if their first edition listing cost **zero**
ETH and started making them revenue (in ETH) as sales kicked in.

How would this work? As always, there are a few options:

  * A percentage of the revenue that the platform earns from commission could be locked into rDAI with the interest going into the relayer
  * [Peter ‘pet3rpan’](https://medium.com/u/5acbddde0b5e?source=post_page-----5b0f0f1753eb--------------------------------) from the [MetaCartel](https://medium.com/metacartel) proposed the concept of platform users like the artists locking up DAI in exchange for platform benefits as a thank you for their interest going to the platform.
  * As dApp developers we would put a proportion of revenue into the upkeep of the relayer and maintaining a minimum amount of interest earning power.

At the time of writing, putting your DAI into the rDAI contract will enable
you to earn 7.82% interest. What does that mean in terms of number of
transactions that could be achieved by KnownOrigin? Let’s do some **_very
crude_** calculations do get a _very_ rough idea:

Scenario: 100 users lock up 50 DAI and direct their interest at KnownOrigin
IPA. KnownOrigin happens to match this amount.

This results in 100 * 50 = 5000 + 5000 = 10,000 DAI earning interest through
rDAI.

  * Interest earned per annum = 10,000 * 0.0782 = 782 DAI
  * Interest per month = 782 / 12 = 65.16 DAI
  * Transactions that can be funded per month @ 0.2 DAI per TX = 65.16 / 0.2 = **325.8 Transactions**!

On average mint nearly 500 editions a month on KO — this would nearly remove
the cost of creating editions on the platform!

# Conclusion

The _PleaseRelayMe_ project takes relay hubs to a whole new level, enabling
dApps to self-fund transactions with no capital loss —it seems like a win-win
scenario. We have only scratched the surface on the work required to implement
a scalable and robust solution that can be used by many dApps universally.
Having said that, we have a clear vision for the steps required to fulfil the
project’s ultimate goal.

We strongly believe that this would be a complementary addition to the wider
Ethereum ecosystem and are looking forward to seeing where this project goes
next.

Let us know what your thoughts are below.

If you want to speak to us directly about how to leverage this and more Web3
tools, please reach out to us using the links below.

Website — [www.blockrocket.tech](https://www.blockrocket.tech/)

Email — [hello@blockrocket.tech](mailto:hello@blockrocket.tech)

Twitter —
[@blockrockettech](https://twitter.com/blockrockettech?source=post_page---------------------------)

> A big shout out to
> [Panvala](https://medium.com/u/75628353e159?source=post_page-----
> 5b0f0f1753eb--------------------------------) for providing a small grant to
> fund the initial research of this project.

If you enjoyed this post please show it some ❤️ and give it a clap 👏

\- James, Vincent and the BlockRocket team 🙌

![](https://miro.medium.com/max/1400/0*seECl0-kTmP1D6aP.png)

## Appendix 1: Time Sequence Diagram, Approach 2

![](https://miro.medium.com/max/1400/1*ijGQHGguhI0qJRC2YIwlCQ.png)

\--

\--

\--

## [More from BlockRocket](/blockrocket?source=post_page-----
5b0f0f1753eb--------------------------------)

Blockchain and decentralised engineering & consultancy based in Manchester, UK
— we build products and help companies understand blockchain and web3
technologies. We have vast knowledge in tokensiation, governance, smart
contract engineerind, IPFS and crypto www.blockrocket.tech

[Read more from BlockRocket](/blockrocket?source=post_page-----
5b0f0f1753eb--------------------------------)

## Recommended from Medium

[[![Brian
Hoffman](https://miro.medium.com/fit/c/40/40/1*KT6r7iTAxYW0e0qhgz0Asw.jpeg)](/@brianhoffman?source=post_internal_links
---------0----------------------------)

[Brian Hoffman

](/@brianhoffman?source=post_internal_links---------
0----------------------------)

## Forget 2018. That shit is history.

![](https://miro.medium.com/freeze/focal/112/112/50/50/0*fKbdV4AjfeGor9CG.gif)](/@brianhoffman/forget-2018-that-
shit-is-history-4b6b7d288b54?source=post_internal_links---------
0----------------------------)

[[![Off the
cuff](https://miro.medium.com/fit/c/40/40/1*dmbNkD5D-u45r44go_cf0g.png)](/@offthecuff?source=post_internal_links
---------1----------------------------)

[Off the cuff

](/@offthecuff?source=post_internal_links---------
1----------------------------)

## A newbies guide to the crypto galaxy — week 4

](/@offthecuff/a-newbies-guide-to-the-crypto-galaxy-
week-4-8c2c8a0b55e6?source=post_internal_links---------
1----------------------------)

[[![Bradley
Zastrow](https://miro.medium.com/fit/c/40/40/1*QLlzH8SV5O0RQBMnJXHZog.png)](/@bradleyzastrow?source=post_internal_links
---------2----------------------------)

[Bradley Zastrow

](/@bradleyzastrow?source=post_internal_links---------
2----------------------------)

## A Hammer in Search of a Nail:

![](https://miro.medium.com/focal/112/112/50/50/1*PCIylWiOJ0v2QefyFUAEWw.jpeg)](/@bradleyzastrow/a-hammer-
in-search-of-a-nail-3994839b1893?source=post_internal_links---------
2----------------------------)

[[![Zach
Hyatt](https://miro.medium.com/fit/c/40/40/1*VdHQ_jX4vGX4nkcVtFSZiQ.jpeg)](/@zhyatt?source=post_internal_links
---------3----------------------------)

[Zach Hyatt

](/@zhyatt?source=post_internal_links---------3----------------------------)

in

[Nano

](https://medium.com/nanocurrency?source=post_internal_links---------
3----------------------------)

## Dynamic Proof-of-Work & Prioritization

![](https://miro.medium.com/focal/112/112/50/50/1*gqEoAwa3XT2p0Z4uQ39U6g.png)](/nanocurrency/dynamic-
proof-of-work-prioritization-4618b78c5be9?source=post_internal_links---------
3----------------------------)

[[![IRONCOIN](https://miro.medium.com/fit/c/40/40/1*-8RxLyAiG6xb5C2wVaqwKg.jpeg)](/@ironcoin?source=post_internal_links
---------4----------------------------)

[IRONCOIN

](/@ironcoin?source=post_internal_links---------4----------------------------)

## IRONCOIN the new crypto ready to go to the moon!

![](https://miro.medium.com/focal/112/112/50/50/0*bzFGzUqFf4pjj7va.)](/@ironcoin/ironcoin-
ico-is-now-live-f5deeef3a4dd?source=post_internal_links---------
4----------------------------)

[[![BEARNDAO](https://miro.medium.com/fit/c/40/40/1*PjP9r4gOLv3b1pMEkS3IqQ.jpeg)](/@bearndao?source=post_internal_links
---------5----------------------------)

[BEARNDAO

](/@bearndao?source=post_internal_links---------5----------------------------)

## ANNOUNCING THE MIGRATION TO BDO V2.0

![](https://miro.medium.com/focal/112/112/50/50/0*5HcA4CZ9UFwCCFbd)](/@bearndao/announcing-
the-migration-to-bdo-v2-0-e8daef36afea?source=post_internal_links---------
5----------------------------)

[[![Space
Runners](https://miro.medium.com/fit/c/40/40/1*ZHLaSb0-yF6CoAl5898GyQ.png)](/@spacerunners?source=post_internal_links
---------6----------------------------)

[Space Runners

](/@spacerunners?source=post_internal_links---------
6----------------------------)

## How to Mint Space Runners & Connect your Wallet

![](https://miro.medium.com/focal/112/112/50/50/1*kUvZn32WQJtAvML8zMU5nA.png)](/@spacerunners/how-
to-use-clover-wallet-mint-d5012f71bf76?source=post_internal_links---------
6----------------------------)

[[![Finscanner](https://miro.medium.com/fit/c/40/40/1*VaXthj0NDBIKEJJGfNodYg.png)](/@finscanner?source=post_internal_links
---------7----------------------------)

[Finscanner

](/@finscanner?source=post_internal_links---------
7----------------------------)

## Review of WhiteBIT — Take Investments To The Next Level

![](https://miro.medium.com/focal/112/112/50/50/1*lKBt959GYpjjxohmUU98PQ.png)](/@finscanner/review-
of-whitebit-take-investments-to-the-next-
level-549163c660e0?source=post_internal_links---------
7----------------------------)

[](/?source=post_page-----5b0f0f1753eb--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
5b0f0f1753eb--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
5b0f0f1753eb--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
5b0f0f1753eb--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
5b0f0f1753eb--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----5b0f0f1753eb--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----5b0f0f1753eb--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fblockrocket%2Fpleaserelayme-
truly-free-meta-transactions-for-dapps-and-users-5b0f0f1753eb&source=post_page
--------------------------nav_reg-----------)

[![James
Morgan](https://miro.medium.com/fit/c/176/176/1*pU0bCzBaLEnySQq0APCjWg.jpeg)](/@james.morgan)

[

## James Morgan

](/@james.morgan)

488 Followers

Founder of @knownorigin_io @BlockRocketTech @blockchain_manc — NFT nerd,
crypto enthusiast, lover of music, humanist, mostly found hacking web3

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F1a825ddddb12&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fblockrocket%2Fpleaserelayme-
truly-free-meta-transactions-for-dapps-and-
users-5b0f0f1753eb&newsletterV3=6bb848438230&newsletterV3Id=1a825ddddb12&user=James+Morgan&userId=6bb848438230&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Orange
Protocol](https://miro.medium.com/fit/c/40/40/1*DYwi1skjbnf8-9tI8dCDKA.png)](/@orangeprotocol?source=read_next_recirc
---------0---------------------54636dd1_74f5_4dc8_8f46_0557a93b897b-------)

[Orange Protocol

](/@orangeprotocol?source=read_next_recirc---------0---------------------
54636dd1_74f5_4dc8_8f46_0557a93b897b-------)

## Learn how to Build with Portable Reputation at ETHDenver

![](https://miro.medium.com/focal/112/112/50/50/1*DQUFck9YT5wb6SrQpnEj5g.png)](/@orangeprotocol/learn-
how-to-build-with-portable-reputation-at-
ethdenver-25c6d0944a35?source=read_next_recirc---------0---------------------
54636dd1_74f5_4dc8_8f46_0557a93b897b-------)

[[![Andrew
Wilkinson](https://miro.medium.com/fit/c/40/40/1*hkiRlFTlyB4rpKSkRZkfFg.png)](/@0x-andrew?source=read_next_recirc
---------1---------------------54636dd1_74f5_4dc8_8f46_0557a93b897b-------)

[Andrew Wilkinson

](/@0x-andrew?source=read_next_recirc---------1---------------------
54636dd1_74f5_4dc8_8f46_0557a93b897b-------)

in

[Galleon

](https://medium.com/galleondao?source=read_next_recirc---------1
---------------------54636dd1_74f5_4dc8_8f46_0557a93b897b-------)

## Hoist the Colours! Galleon Branding & Voyages

![](https://miro.medium.com/focal/112/112/50/50/1*Tb2f4h33UBhyZg7VtFZjSQ.png)](/galleondao/hoist-
the-colours-galleon-branding-voyages-80cf91da4552?source=read_next_recirc
---------1---------------------54636dd1_74f5_4dc8_8f46_0557a93b897b-------)

[[![Joseph
Appolos](https://miro.medium.com/fit/c/40/40/1*IaolXWBo2VYWhqwjv0YCYg.jpeg)](/@joseph-
appolos60?source=read_next_recirc---------2---------------------
54636dd1_74f5_4dc8_8f46_0557a93b897b-------)

[Joseph Appolos

](/@joseph-appolos60?source=read_next_recirc---------2---------------------
54636dd1_74f5_4dc8_8f46_0557a93b897b-------)

## DAO Governance — Usage Made Easy

![](https://miro.medium.com/focal/112/112/50/50/1*8KzAPtUQrvWR-
KtidQwNYQ.png)](/@joseph-appolos60/dao-governance-usage-made-easy-
ebe9d045b4e?source=read_next_recirc---------2---------------------
54636dd1_74f5_4dc8_8f46_0557a93b897b-------)

[[![Blockpour](https://miro.medium.com/fit/c/40/40/1*U4_54LAJHJv3K3hovwX4hA.jpeg)](/@blockpour?source=read_next_recirc
---------3---------------------54636dd1_74f5_4dc8_8f46_0557a93b897b-------)

[Blockpour

](/@blockpour?source=read_next_recirc---------3---------------------
54636dd1_74f5_4dc8_8f46_0557a93b897b-------)

## Blockpour Receives Infrastructure Grant From Polygon!

![](https://miro.medium.com/focal/112/112/50/50/0*cVYGqVTt3oUESsso)](/@blockpour/blockpour-
receives-infrastructure-grant-from-
polygon-1d2be80af1f1?source=read_next_recirc---------3---------------------
54636dd1_74f5_4dc8_8f46_0557a93b897b-------)

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

