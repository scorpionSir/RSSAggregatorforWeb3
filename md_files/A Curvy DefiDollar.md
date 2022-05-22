[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/c249438c154a&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![DefiDollar](https://miro.medium.com/fit/c/64/64/1*acjRchHa7v0vT46m5lAQVQ.png)](https://medium.com/defidollar?source=post_page
-----c249438c154a--------------------------------)

Published in

[DefiDollar

](https://medium.com/defidollar?source=post_page-----
c249438c154a--------------------------------)

[![atvanguard](https://miro.medium.com/fit/c/96/96/1*Bm8one51ZA1c3k8Oty022w.jpeg)](/@atvanguard?source=post_page
-----c249438c154a--------------------------------)

[atvanguard](/@atvanguard?source=post_page-----
c249438c154a--------------------------------)

Follow

Jul 19, 2020

·

5 min read

# A Curvy DefiDollar

![](https://miro.medium.com/max/1400/1*17L0N4GxpJmJtX_jFJY7yQ.jpeg)

DefiDollar (DUSD) is an index of stable coins that uses Defi primitives to
stay near the dollar mark and subsidize the collateralization ratio. Our
vision behind DUSD is to provide an avenue for diversifying your _crypto-
dollars_ position; to dampen the potentially disastrous effects of a
particular stablecoin like tether failing (partially or completely) from its
peg.

DUSD was originally built for the ETHGlobal
[HackMoney](https://hackathon.money/) and the details about the first design
were published in the following post. Here is a quick [demo
video](https://www.youtube.com/watch?v=m3iAvOw8ezw).

[

## Introducing DefiDollar

### Quite recently there has been a lot of discussion about Dai moving from
its peg and the hassle of involved governance…

medium.com

](/@atvanguard/introducing-defidollar-742e30be9780)

In this post, we propose a revised DUSD design that allows for higher yields,
a more robust peg safety mechanism, and yield farming techniques. While the
ideas are the same; the underlying protocols have since been changed.

 **Tl;dr  
** DUSD is a stablecoin that is collateralized by [Curve
Finance](https://www.curve.fi/) liquidity provider (LP) tokens. It uses
chainlink oracles for its stability mechanism. We leverage Curve to handle the
logic around integrating with lending protocols and token swaps; which are
essential ingredients for the stability of DUSD. We also introduce a staking
mechanism for additional peg safety. If you’d like to remain updated with
announcements, discussions, and community calls, please join our
[discord](https://discord.gg/3smXsSW) server and follow us on
[twitter](https://twitter.com/defidollar).

![](https://miro.medium.com/max/1400/1*amu2NcspIPv0p26OOOAm1w.png)

# The DUSD cliff

There are 4 components to the DUSD system.

 **A. Streams  
** This is the [price reference data](https://feeds.chain.link/) from the
chainlink oracles for the supported stablecoins.

 **B. Peaks  
** Peak refers to a yield generating protocol in which the underlying
stablecoins are deposited. The system will start with supporting 2 peaks: the
curve [susdV2](https://www.curve.fi/susdv2) and [y](https://www.curve.fi/y)
pools; hence it will be possible to mint DUSD with DAI, USDT, USDC TUSD, sUSD.
The contracts are being written in a manner that it will be possible to add
other peaks like Aave, Uniswap — but this idea is still under exploration.
Note that the peak will hold the respective LP tokens from the protocol it
supports. It will be possible to modify/add/remove peaks from the protocol
based on community deliberations.

 **Mint / redeem  
** The user is free to choose any of the supported peaks to mint/redeem DUSD.
However, note that the DUSD system will be an average of the funds in all the
peaks. Later, we might explore the possibility of assigning weights to assets
that are deposited at each peak (e.g. 60% y pool and 20% susdV2 pool and 20%
in Aave).

There will be a separate contract for each supported peak. This choice was
made to keep the gas usage low. Here is how the curve finance peak will look
like:

 **C. Base  
** This is the core contract of the entire DUSD system and is in charge of the
actual mint/redeem DUSD operations, pulling oracle prices, distributing
protocol income to DUSD stakers — which brings us to the fourth component.

 **D. Valley  
** Valley refers to the DUSD staking system. If the underlying stable-coins
fall below their $1 peg, the DUSD system will become under-collateralized. To
offset this risk, DUSD has a native staking mechanism. It’s possible to stake
DUSD with the system which acts as additional collateral for the DUSD coins
that are in free circulation (not staked). In the event of peg failure of the
underlying stablecoin assets, the stakers act as buyers of the last resort in
the DUSD system. For bearing this risk, stakers will receive all the
underlying income generated from having deposited funds in Curve.

Explaining the concept with a scenario:

  1. Let’s say 110 DUSD are backed by $110 worth of stable-coins like DAI, USDC which are deposited in Curve and hence generating income.
  2. Alice, with a higher risk appetite, decided to stake 10 DUSD. Since these staked funds act as collateral for the system, effectively the freely circulating 100 DUSD are collateralized with $110 worth of stable-coins.
  3. Over some time period the protocol generated income (on the entire $110) from underlying curve pools and now has a total of $115 in assets. At this point Alice may decide to withdraw her stake and receive her proportional share (100%) from the income, so will withdraw $10 + $5 (denominated in DUSD). Note that though the protocol income was about 4.5%, however, that is directed entirely towards staked funds. This results in a 50% APR for Alice.
  4. There may be a situation that causes one of the underlying stable-coins to break it’s peg, causing the system to be backed by $100 (instead of $110).
  5. In this situation, the entire burden of the under-collateralized system is borne by Alice. So effectively, while the freely circulating 100 DUSD are still backed by $100, the staked DUSD are worth nothing (i.e. they will remain locked in the protocol). This is how staked funds provide a volatility cushion.
  6. Say, a black swan event occurred which caused the underlying assets to fall further to $80. Since we still want DUSD to be redeemable with the protocol; the system will use the price feed from the oracle to devalue a DUSD token to $80/100 DUSD = $0.8 / DUSD.

# We yield farmin’

![](https://miro.medium.com/max/1400/1*b9OCTSzNCW-I9xq_QDvHYw.png)

As for the crops, you might have noticed that the peaks will accumulate yield
farming rewards from the protocols they hold the LP tokens of. The mechanism
to distribute the farmed tokens is currently under active discussion. Here are
some of our thoughts in decreasing order of preference:

1\. Once or twice a week, admin collects farmed tokens on behalf of the
protocol and distributes them to the DUSD holders based on how long they held
DUSD for by running an off-chain script.

2\. Make farmed tokens collect-able in realtime but this will lead to much
higher gas requirements for mint/redeem/stake operations.

3\. Use the farmed funds to create an 1. additional volatility cushion, 2. a
SAFU fund in case the dapp funds are compromised and 3. income for the
defidollar team. While this sounds the best way of using the funds however, we
do not want DUSD believers to lose out on farming opportunities.

4\. Admin distributes farmed rewards to stakers alone. This is not a preferred
choice because all DUSD liquidity providers (minters/holders) should receive
farmed benefits and not just stakers; however, it does lead to higher APR for
stakers and hence will help in enhancing the peg safety.

I’d like to reiterate that the above proposals are under active discussion and
we’d love to hear your thoughts on the above or any new effective techniques.
To be a part of the crop discussions, please join our
[discord](https://discord.gg/3smXsSW) server and say Hi 👋

# Smart contracts and Audits

We are in the final stages of the smart contract work and on the lookout for
good auditors who would be willing to audit the Defidollar smart contracts at
a subsidized cost since we are bootstrapping :) Say hi on our discord or
twitter if you’d be interested in performing the audit. Our solidity code
stands at about 500 lines for now.

\--

2

\--

\--

2

## [More from DefiDollar](/defidollar?source=post_page-----
c249438c154a--------------------------------)

Building to simplify open finance for everyone

[Read more from DefiDollar](/defidollar?source=post_page-----
c249438c154a--------------------------------)

## Recommended from Medium

[[![Ancientkingdom](https://miro.medium.com/fit/c/40/40/1*JVqkX0Aq0XaOxaUPP6fpcg.png)](/@ancientkingdom?source=post_internal_links
---------0----------------------------)

[Ancientkingdom

](/@ancientkingdom?source=post_internal_links---------
0----------------------------)

## Ancient Kingdom has associated with Breach in a long-term relationship

![](https://miro.medium.com/focal/112/112/50/50/0*zpvIsfz0Z3QGaVQI)](/@ancientkingdom/ancient-
kingdom-has-associated-with-breach-in-a-long-term-
relationship-5d6adeff60d1?source=post_internal_links---------
0----------------------------)

[[![Bio_Logik](https://miro.medium.com/fit/c/40/40/1*0_6Q-k2xtuEAE15yjayL2A.jpeg)](/@.Bio_Logik.?source=post_internal_links
---------1----------------------------)

[Bio_Logik

](/@.Bio_Logik.?source=post_internal_links---------
1----------------------------)

## DMme: from project to product, steady and constant progress

![](https://miro.medium.com/focal/112/112/50/50/1*TrzLh7icRWX_QLeLNxaPOw.png)](/@.Bio_Logik./dmme-
from-project-to-product-steady-and-constant-
progress-9b6bf91351b7?source=post_internal_links---------
1----------------------------)

[[![EOS
Nation](https://miro.medium.com/fit/c/40/40/1*doohyn1Uc4BOxPHXSd7k5g.jpeg)](/@eosnationbp?source=post_internal_links
---------2----------------------------)

[EOS Nation

](/@eosnationbp?source=post_internal_links---------
2----------------------------)

## DPOS in Action | Part 2

![](https://miro.medium.com/focal/112/112/50/50/1*hyFHVAzFH8IH_h3JxAjDiQ.jpeg)](/@eosnationbp/dpos-
in-action-part-2-ae06402b1c45?source=post_internal_links---------
2----------------------------)

[[![INVESTART](https://miro.medium.com/fit/c/40/40/1*F0jpaiTUxs-
KE07S2ZpGLQ.png)](/@admin-82109?source=post_internal_links---------
3----------------------------)

[INVESTART

](/@admin-82109?source=post_internal_links---------
3----------------------------)

## What is the best protection against inflation?

](/@admin-82109/what-is-the-best-protection-against-
inflation-d74659075561?source=post_internal_links---------
3----------------------------)

[[![jerkytreats.eth](https://miro.medium.com/fit/c/40/40/1*e830Wv-
UBeRZWi83t9WlBg.png)](/@JerkyTreats?source=post_internal_links---------
4----------------------------)

[jerkytreats.eth

](/@JerkyTreats?source=post_internal_links---------
4----------------------------)

## Crypto Narratives : Bitcoin

![](https://miro.medium.com/focal/112/112/50/50/1*h5DxIlpu7oWnmNFfCrAulQ.jpeg)](/@JerkyTreats/crypto-
narratives-bitcoin-59aaf1528e5e?source=post_internal_links---------
4----------------------------)

[[![Delton
Rhodes](https://miro.medium.com/fit/c/40/40/1*55QCpgJx5HvgHryKP8Kvng.jpeg)](/@deltonrhodes?source=post_internal_links
---------5----------------------------)

[Delton Rhodes

](/@deltonrhodes?source=post_internal_links---------
5----------------------------)

in

[The Green Light

](https://medium.com/the-green-light?source=post_internal_links---------
5----------------------------)

## Crypto Insurance Needs More Transparency

![](https://miro.medium.com/focal/112/112/50/50/1*hZcllibWJs_WRN3hXAeWOg.jpeg)](/the-
green-light/crypto-insurance-needs-more-
transparency-62141e23d778?source=post_internal_links---------
5----------------------------)

[[![mraowbot](https://miro.medium.com/fit/c/40/40/1*dmbNkD5D-u45r44go_cf0g.png)](/@mraowbot?source=post_internal_links
---------6----------------------------)

[mraowbot

](/@mraowbot?source=post_internal_links---------6----------------------------)

in

[Coinmonks

](https://medium.com/coinmonks?source=post_internal_links---------
6----------------------------)

## QuadrigaCX Was Never Legitimate

![](https://miro.medium.com/focal/112/112/50/50/1*Uc8370kOjeSfSCcmeSiVyA.jpeg)](/coinmonks/quadrigacx-
was-never-legitimate-e17c98d6c46f?source=post_internal_links---------
6----------------------------)

[[![pressfarm](https://miro.medium.com/fit/c/40/40/0*5iY9GhcD3bMVgLRf.png)](/@pressfarm?source=post_internal_links
---------7----------------------------)

[pressfarm

](/@pressfarm?source=post_internal_links---------
7----------------------------)

## Marketing Cryptocurrency 101 in 2019 — Press Farm

![](https://miro.medium.com/focal/112/112/50/50/1*rclIeOCQNw0yOOEuKouurA.jpeg)](/@pressfarm/marketing-
cryptocurrency-101-in-2019-press-farm-a813061a5589?source=post_internal_links
---------7----------------------------)

[](/?source=post_page-----c249438c154a--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
c249438c154a--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
c249438c154a--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
c249438c154a--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
c249438c154a--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----c249438c154a--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----c249438c154a--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fdefidollar%2Fa-
curvy-defidollar-c249438c154a&source=post_page--------------------------
nav_reg-----------)

[![atvanguard](https://miro.medium.com/fit/c/176/176/1*Bm8one51ZA1c3k8Oty022w.jpeg)](/@atvanguard)

[

## atvanguard

](/@atvanguard)

588 Followers

Building @HubbleExchange

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F484fb0d114bc&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fdefidollar%2Fa-
curvy-
defidollar-c249438c154a&newsletterV3=694ca2a647c1&newsletterV3Id=484fb0d114bc&user=atvanguard&userId=694ca2a647c1&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Atlendis](https://miro.medium.com/fit/c/40/40/1*QdZ3AUm1S6NHrgUDahYbTg.png)](/@Atlendis?source=read_next_recirc
---------0---------------------62f88fc4_c2c2_424c_97ea_50701b1cbbcb-------)

[Atlendis

](/@Atlendis?source=read_next_recirc---------0---------------------
62f88fc4_c2c2_424c_97ea_50701b1cbbcb-------)

## Highlights of Devconnect side event by Atlendis Labs x CowSwap

![](https://miro.medium.com/focal/112/112/50/50/1*6_EmIOqG3VpFQ7tHvJseNw.jpeg)](/@Atlendis/highlights-
of-devconnect-side-event-by-atlendis-labs-x-
cowswap-3ed75c49dcb9?source=read_next_recirc---------0---------------------
62f88fc4_c2c2_424c_97ea_50701b1cbbcb-------)

[[![Drxdefi](https://miro.medium.com/fit/c/40/40/1*JwZJzO2t-rLPT0BIlMfa0w.png)](/@drxdefi?source=read_next_recirc
---------1---------------------62f88fc4_c2c2_424c_97ea_50701b1cbbcb-------)

[Drxdefi

](/@drxdefi?source=read_next_recirc---------1---------------------
62f88fc4_c2c2_424c_97ea_50701b1cbbcb-------)

## Why is DRx Building on GateChain? 🤔👀🔨

![](https://miro.medium.com/focal/112/112/50/50/1*HB6LcFUA8Wj5R9PXuXCrJQ.png)](/@drxdefi/why-
is-drx-building-on-gatechain-469b32b028b3?source=read_next_recirc---------1
---------------------62f88fc4_c2c2_424c_97ea_50701b1cbbcb-------)

[[![Argo](https://miro.medium.com/fit/c/40/40/1*8KNNqd8bGrT4IDZ1EkksJg.png)](/@argo_so?source=read_next_recirc
---------2---------------------62f88fc4_c2c2_424c_97ea_50701b1cbbcb-------)

[Argo

](/@argo_so?source=read_next_recirc---------2---------------------
62f88fc4_c2c2_424c_97ea_50701b1cbbcb-------)

## Argo Devnet: Public Launch

![](https://miro.medium.com/focal/112/112/50/50/1*UyMWeqOGhRsmBPpdQx-
lSA.png)](/@argo_so/argo-devnet-public-
launch-b731e49d7c30?source=read_next_recirc---------2---------------------
62f88fc4_c2c2_424c_97ea_50701b1cbbcb-------)

[[![István Szentes](https://miro.medium.com/fit/c/40/40/0*vmjJ6t0DR-
SiQJWi)](/@szentes.istvan2010?source=read_next_recirc---------3
---------------------62f88fc4_c2c2_424c_97ea_50701b1cbbcb-------)

[István Szentes

](/@szentes.istvan2010?source=read_next_recirc---------3---------------------
62f88fc4_c2c2_424c_97ea_50701b1cbbcb-------)

## The House of Dukes

![](https://miro.medium.com/focal/112/112/50/50/1*Sp6wFNDKFkFky-G46mtcUg.png)](/@szentes.istvan2010/the-
house-of-dukes-88ca2dbe6d2f?source=read_next_recirc---------3
---------------------62f88fc4_c2c2_424c_97ea_50701b1cbbcb-------)

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

