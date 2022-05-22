[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/76561e4d1b85&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![DefiDollar](https://miro.medium.com/fit/c/64/64/1*acjRchHa7v0vT46m5lAQVQ.png)](https://medium.com/defidollar?source=post_page
-----76561e4d1b85--------------------------------)

Published in

[DefiDollar

](https://medium.com/defidollar?source=post_page-----
76561e4d1b85--------------------------------)

[![atvanguard](https://miro.medium.com/fit/c/96/96/1*Bm8one51ZA1c3k8Oty022w.jpeg)](/@atvanguard?source=post_page
-----76561e4d1b85--------------------------------)

[atvanguard](/@atvanguard?source=post_page-----
76561e4d1b85--------------------------------)

Follow

Oct 29, 2020

·

6 min read

#  **DefiDollar: Initial Liquidity Mining Offering (ILMO)**

![](https://miro.medium.com/max/1400/1*gu7hbtHD82vo5muxoWtaTg.png)

DefiDollar DAO Token (DFD)

DefiDollar ($DUSD) aspires to be a risk-insured stablecoin layer for DeFi. It
aims to provide a safe and stable way for users to hold their assets. In the
shorter term, $DUSD is a stablecoin optimized for peg safety, yield and
diversification. Just recently, we [shared](/defidollar/the-next-chapter-of-
defidollar-b227935f10e7) our vision, roadmap and DFD — the DefiDollar
Governance token and details around the retroactive token distribution.

# Introducing the DFD Liquidity Mining

We have been working on a new mechanism to ensure a balanced and healthy
distribution of the $DFD token.

## TL;DR

Honest farmers need to deposit $DUSD to participate in the initial liquidity
distribution. $DUSD can be [minted](https://app.dusd.finance/mint/) with DAI,
USDC, USDT, TUSD, yCRV and yUSD from our app. **This is not a token sale!** At
the end of the 4 day period (TGE), $DUSD will be auto-converted into an equal
number of balancer pool tokens (BPT) that have exposure to both the
contributed $DUSD and a proportional share in the pool of 3mil DFD tokens
**(3% of the token supply)**. The BPTs will also be auto-staked. The staked
BPTs will unlock linearly over a month and will **farm an additional 1mil
DFD** during this period.  
Additional distribution details will accompany the ILMO launch blog with
participation instructions.

The mechanism ensures the following:

  * No gas wars to participate
  * Parity in DFD mined irrespective of when you contribute DUSD.
  * Everyone starts DFD farming simultaneously, no action required after the initial contribution

So let’s dive deeper into the mechanics of the ILMO:

The DefiDollar team will be launching the liquidity mining of the DFD token
via a genesis ceremony that will start on **Oct 30, 2020–1400 UTC**. The
ceremony will be the following sequence of events:

  1. Team deposits 3mil (3% supply) DFD tokens in a contract.
  2. Users can make a claim on the 3% initial supply by depositing $DUSD in the same contract. This will remain live for 4 days and will end on **Nov** **3, 2020–1600 UTC**. _This is a new approach to liquidity mining. The team does not receive any funds contributed during the ILMO._
  3. At the end of the period, 3mil DFD and accumulated DUSD are put together in a y:z ratio Bal pool.
  4. The contributed amount of DUSD will determine the weights of the genesis pool. %weight (y) for DFD in the Bal pool will be a function of DUSD collected determined as follows.

    
    
    y = 93 – 5x; constraint at 50 <= y <= 90  
    where x is the DUSD collected denoted in million units

This means that the pool will start off in the following ratio based on the
amount of $DUSD deposited during the ceremony period:

![](https://miro.medium.com/max/1332/0*RzovjzV9lDxG3UZZ)

The balancer pool weights are dynamic — lower interest in the genesis ceremony
makes the balancer pool more
[bullish](https://twitter.com/DegenSpartan/status/1268707235573579778) on the
DFD token. This makes it favorable for the initial liquidity providers by
minimizing their impermanent loss. This is in line with creating a healthy
ecosystem by aligning and incentivizing the early believers of the project.

5\. After the pool has been initialized, everyone who contributed liquidity in
the genesis period will receive an equal number of Balancer Pool Tokens (BPTs)
to the DUSD they contributed. This BPT is representative of the initial
liquidity contributed in $DUSD and a corresponding share in the 3mil DFD
tokens. **10% of these BPTs will be available immediately to be released** and
the **remaining 90% will vest over 1 month**.

6\. The interesting part here is that the BPTs for all users will be staked
immediately and begin farming more DFD exactly at the same time — **The users
do not need to make a claim or stake transaction.** LPs of the genesis
balancer pool will remain incentivized with an additional 1% tokens (1 mil)
over one month (the entire vesting period).

At the end of 1 month, the holding of the initial LPs would look like:

1\. Vested BPTs (Share in the initial 3% DFD + **DUSD which could more or less
than what was originally contributed** ).

2\. Share in 1% additional DFD farmed during this period.

3\. 0.1% swap fees from the DFD:DUSD Balancer pool.

4\. Balancer liquidity mining rewards on DFD* and DUSD.  
*subject to DFD getting whitelisted for BAL rewards

# Retroactive Distribution

\- 1.5 mil DFD tokens (1.5% of total supply) is being distributed
retroactively to early $DUSD believers. Following users are being considered
for the distribution:

The distributions have been considered from the time the $DUSD cap was raised
(Sep 4, 2020 — 1630 UTC).

A. $DUSD holders and stakers until Sep 22, 2020 — 1600 UTC  
B. $swDUSD (The swervy fork) holders and stakers until Oct 7, 2020 — 1600 UTC.

The following incentives have been considered from Sep 22, 2020 — 1600 UTC.

C. [DUSD <>
USDC](https://pools.balancer.exchange/#/pool/0xed5ad5f258eef6a9745042bde7d46e8a5254c183/)
Balancer pool liquidity provider.  
D. [DUSD <> ETH
uniswap](https://info.uniswap.org/pair/0x8ccd68af5e35fe01c56ad40cd2ed27cbd7767fb1)
liquidity providers  
E. Wallets that trade $DUSD from the above pools. To filter out sybil attack
wallets, we have only considered trades ≥ $10 in value.

 **Furthermore, we have assigned a minimum of 500 DFD tokens to all
participating wallets.**

\- You may check the calculation script and your retroactive token rewards
[here](https://github.com/defidollar/liquidity-mining/tree/master/dfd).

\- The tokens will have **30% immediate unlock** at TGE and the rest 70% will
vest linearly every block over **6 months**. Eligible users will be able to
claim their tokens from the LP rewards page on our app just a bit after the 4
day genesis period has concluded.

# A User-Centric Token Distribution Strategy

While designing our liquidity mining genesis ceremony, we were inspired by the
brilliant piece on [Liquidity Mining: A User-Centric Token Distribution
Strategy](/bollinger-investment-group/liquidity-mining-a-user-centric-token-
distribution-strategy-1d05c5174641) by Dmitriy Berenzon and believe have
tackled the most pressing issues plaguing the current liquidity mining
landscape. For instance,

  * Technical Risk: Our liquidity mining contract has been audited by PeckShield.
  * Rug pulling: Our team is public and has been iterating on the product for 6 months and is backed by a brilliant set of investors.
  * Information asymmetry: The way we have designed our liquidity mining scheme, does not favor whales or early participants. All big and small farmers start farming DFD at the same time without the need for active involvement post genesis.
  * Gas costs: Users can get in anytime when the gas costs are favorable during the 4 day genesis period thereby countering gas-guzzling behavior.
  * Retroactive token distribution for early supporters.

# Risks

Please note that the DUSD contributed will be vesting over one month in form
of the BPT tokens becoming eligible for withdrawals. This entails that the
usual risks of providing liquidity to a Balancer pool apply. Case in point the
impermanent loss:

![](https://miro.medium.com/max/1400/0*bqP0F57et66Tu7fz)

Impermanent Loss for different combinations of Balancer pool weights
[(Source)](/balancer-protocol/80-20-balancer-pools-ad7fed816c8d)

As mentioned in the [blog ](/balancer-protocol/80-20-balancer-pools-
ad7fed816c8d)_“With a 5x price change, the impermanent loss for a standard
50/50 pool would be 25.4% whereas in a 95/5 pool it would be only 3.88%, over
6.5 times smaller.”_

So the risk of impermanent loss although reduced with a 95/5 pool, is not
entirely eliminated. The greater the interest in the genesis ceremony the
closer the weights tend towards 50:50 DFD:DUSD pool. We believe that instead
of defining the weights ourselves it is prudent to let the market determine
the proper equilibrium.

Another risk is that if there is a tremendous sell pressure, then LPs who do
not remove liquidity from the pool will end up holding a large amount of DFD
tokens having paid for them with their initial investment.

# Concluding remarks

  * ~5.5% of the token supply is being released to the community during the first month (3% genesis + 1% genesis pool mining + 0.625% for retroactive participants + ~0.86% will be utilized for incentivizing other pools as in when they make sense).
  * The initial liquidity mining offering is not a token sale, the contributors will get their contribution amounts back gradually as the BPTs vest — **This however does not guarantee that they will get back 100% of the contributed amount**. This varies depending on a multitude of market forces and participant behaviors.
  * We are working on some final touches on our app and preparing to initiate the genesis ceremony on **Oct 30, 2020–1400 UTC.** We hope that our community finds merit in this exciting new mechanism which we believe is also a step towards a fairer token distribution.
  * The address of the DFD contract is: [0x20c36f062a31865bED8a5B1e512D9a1A20AA333A](https://etherscan.io/address/0x20c36f062a31865bED8a5B1e512D9a1A20AA333A).  
 **It’s not possible to buy the token. No liquidity has been added to any
Uniswap or balancer pools. Please exercise caution and  
beware of scammers trying to con you.**

  * Please join our [Discord](https://discord.gg/zGmC547) and [Telegram](https://t.me/defidollar_community), we’ll be very happy to answer queries and follow us on [Twitter](https://twitter.com/defidollar) for updates.

## Contact Us

> [ _Website_](http://dusd.finance/) _|_[ _App_](http://app.dusd.finance/)
> _|_[ _Twitter_](https://twitter.com/defidollar) _|_[
> _Discord_](http://discord.gg/zGmC547) _|_[
> _Telegram_](https://t.me/defidollar_community) _|_[
> _Docs_](https://docs.dusd.finance/)

\--

\--

\--

## [More from DefiDollar](/defidollar?source=post_page-----
76561e4d1b85--------------------------------)

Building to simplify open finance for everyone

[Read more from DefiDollar](/defidollar?source=post_page-----
76561e4d1b85--------------------------------)

## Recommended from Medium

[[![Crypto
Lemon](https://miro.medium.com/fit/c/40/40/1*wuYJoiWWrdUxj3fOgOEQSg.jpeg)](/@crypto-
lemon?source=post_internal_links---------0----------------------------)

[Crypto Lemon

](/@crypto-lemon?source=post_internal_links---------
0----------------------------)

## The power of compounding with DeFi 2.0 (Olympus DAO, Gyro…)

![](https://miro.medium.com/focal/112/112/50/50/0*fefU4cpXQYvyKX_6.png)](/@crypto-
lemon/the-power-of-compounding-with-defi-2-0-olympus-dao-
gyro-b6737a0b1395?source=post_internal_links---------
0----------------------------)

[[![atvanguard](https://miro.medium.com/fit/c/40/40/1*Bm8one51ZA1c3k8Oty022w.jpeg)](/@atvanguard?source=post_internal_links
---------1----------------------------)

[atvanguard

](/@atvanguard?source=post_internal_links---------
1----------------------------)

in

[DefiDollar

](https://medium.com/defidollar?source=post_internal_links---------
1----------------------------)

## A Curvy DefiDollar

![](https://miro.medium.com/focal/112/112/50/50/1*amu2NcspIPv0p26OOOAm1w.png)](/defidollar/a-curvy-
defidollar-c249438c154a?source=post_internal_links---------
1----------------------------)

[[![Ancientkingdom](https://miro.medium.com/fit/c/40/40/1*JVqkX0Aq0XaOxaUPP6fpcg.png)](/@ancientkingdom?source=post_internal_links
---------2----------------------------)

[Ancientkingdom

](/@ancientkingdom?source=post_internal_links---------
2----------------------------)

## Ancient Kingdom has associated with Breach in a long-term relationship

![](https://miro.medium.com/focal/112/112/50/50/0*zpvIsfz0Z3QGaVQI)](/@ancientkingdom/ancient-
kingdom-has-associated-with-breach-in-a-long-term-
relationship-5d6adeff60d1?source=post_internal_links---------
2----------------------------)

[[![Bio_Logik](https://miro.medium.com/fit/c/40/40/1*0_6Q-k2xtuEAE15yjayL2A.jpeg)](/@.Bio_Logik.?source=post_internal_links
---------3----------------------------)

[Bio_Logik

](/@.Bio_Logik.?source=post_internal_links---------
3----------------------------)

## DMme: from project to product, steady and constant progress

![](https://miro.medium.com/focal/112/112/50/50/1*TrzLh7icRWX_QLeLNxaPOw.png)](/@.Bio_Logik./dmme-
from-project-to-product-steady-and-constant-
progress-9b6bf91351b7?source=post_internal_links---------
3----------------------------)

[[![EOS
Nation](https://miro.medium.com/fit/c/40/40/1*doohyn1Uc4BOxPHXSd7k5g.jpeg)](/@eosnationbp?source=post_internal_links
---------4----------------------------)

[EOS Nation

](/@eosnationbp?source=post_internal_links---------
4----------------------------)

## DPOS in Action | Part 2

![](https://miro.medium.com/focal/112/112/50/50/1*hyFHVAzFH8IH_h3JxAjDiQ.jpeg)](/@eosnationbp/dpos-
in-action-part-2-ae06402b1c45?source=post_internal_links---------
4----------------------------)

[[![INVESTART](https://miro.medium.com/fit/c/40/40/1*F0jpaiTUxs-
KE07S2ZpGLQ.png)](/@admin-82109?source=post_internal_links---------
5----------------------------)

[INVESTART

](/@admin-82109?source=post_internal_links---------
5----------------------------)

## What is the best protection against inflation?

](/@admin-82109/what-is-the-best-protection-against-
inflation-d74659075561?source=post_internal_links---------
5----------------------------)

[[![jerkytreats.eth](https://miro.medium.com/fit/c/40/40/1*e830Wv-
UBeRZWi83t9WlBg.png)](/@JerkyTreats?source=post_internal_links---------
6----------------------------)

[jerkytreats.eth

](/@JerkyTreats?source=post_internal_links---------
6----------------------------)

## Crypto Narratives : Bitcoin

![](https://miro.medium.com/focal/112/112/50/50/1*h5DxIlpu7oWnmNFfCrAulQ.jpeg)](/@JerkyTreats/crypto-
narratives-bitcoin-59aaf1528e5e?source=post_internal_links---------
6----------------------------)

[[![Delton
Rhodes](https://miro.medium.com/fit/c/40/40/1*55QCpgJx5HvgHryKP8Kvng.jpeg)](/@deltonrhodes?source=post_internal_links
---------7----------------------------)

[Delton Rhodes

](/@deltonrhodes?source=post_internal_links---------
7----------------------------)

in

[The Green Light

](https://medium.com/the-green-light?source=post_internal_links---------
7----------------------------)

## Crypto Insurance Needs More Transparency

![](https://miro.medium.com/focal/112/112/50/50/1*hZcllibWJs_WRN3hXAeWOg.jpeg)](/the-
green-light/crypto-insurance-needs-more-
transparency-62141e23d778?source=post_internal_links---------
7----------------------------)

[](/?source=post_page-----76561e4d1b85--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
76561e4d1b85--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
76561e4d1b85--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
76561e4d1b85--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
76561e4d1b85--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----76561e4d1b85--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----76561e4d1b85--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fdefidollar%2Fdefidollar-
initial-liquidity-mining-offering-ilmo-76561e4d1b85&source=post_page
--------------------------nav_reg-----------)

[![atvanguard](https://miro.medium.com/fit/c/176/176/1*Bm8one51ZA1c3k8Oty022w.jpeg)](/@atvanguard)

[

## atvanguard

](/@atvanguard)

588 Followers

Building @HubbleExchange

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F484fb0d114bc&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fdefidollar%2Fdefidollar-
initial-liquidity-mining-offering-
ilmo-76561e4d1b85&newsletterV3=694ca2a647c1&newsletterV3Id=484fb0d114bc&user=atvanguard&userId=694ca2a647c1&source=--------------------------subscribe_user-----------)

## More from Medium

[[![BlockVision](https://miro.medium.com/fit/c/40/40/1*s-AQ6dCj7KRfOtM_jHLogw.png)](/@BlockVision?source=read_next_recirc
---------0---------------------b8fee591_7204_4a76_956e_4f1a232857a5-------)

[BlockVision

](/@BlockVision?source=read_next_recirc---------0---------------------
b8fee591_7204_4a76_956e_4f1a232857a5-------)

## BlockVision’s Asset Hack Tracking Technology: How to Stay Ahead of the
Crypto Security Game

![](https://miro.medium.com/focal/112/112/50/50/1*C0DG6syw2ZvvG9O9WVyVMA.png)](/@BlockVision/blockvisions-
asset-hack-tracking-how-to-stay-ahead-of-the-crypto-security-
game-33274c9a7cf5?source=read_next_recirc---------0---------------------
b8fee591_7204_4a76_956e_4f1a232857a5-------)

[[![Hotpot
Sets](https://miro.medium.com/fit/c/40/40/1*9CJMsHBupw3EDQizx6H9Jg.png)](/@hotpot-
sets?source=read_next_recirc---------1---------------------
b8fee591_7204_4a76_956e_4f1a232857a5-------)

[Hotpot Sets

](/@hotpot-sets?source=read_next_recirc---------1---------------------
b8fee591_7204_4a76_956e_4f1a232857a5-------)

## Hotpot V3 49th Weekly Report

![](https://miro.medium.com/focal/112/112/50/50/1*F4BqwM7QF4KKEPL81V-_gg.jpeg)](/@hotpot-
sets/hotpot-v3-49th-weekly-report-5257b8d35917?source=read_next_recirc
---------1---------------------b8fee591_7204_4a76_956e_4f1a232857a5-------)

[[![NEARDeFi](https://miro.medium.com/fit/c/40/40/1*GaKUUyyoy9hq-Cr-
ZdqeKw.jpeg)](/@NEARDeFi?source=read_next_recirc---------2
---------------------b8fee591_7204_4a76_956e_4f1a232857a5-------)

[NEARDeFi

](/@NEARDeFi?source=read_next_recirc---------2---------------------
b8fee591_7204_4a76_956e_4f1a232857a5-------)

## Meta Yield Deepdive

![](https://miro.medium.com/focal/112/112/50/50/0*A7ef9MwFkPTHHMKk)](/@NEARDeFi/meta-
yield-965f3ff4723a?source=read_next_recirc---------2---------------------
b8fee591_7204_4a76_956e_4f1a232857a5-------)

[[![fl](https://miro.medium.com/fit/c/40/40/1*dabnMe0goe7aAkOwXRUguw.png)](/@fldev?source=read_next_recirc
---------3---------------------b8fee591_7204_4a76_956e_4f1a232857a5-------)

[fl

](/@fldev?source=read_next_recirc---------3---------------------
b8fee591_7204_4a76_956e_4f1a232857a5-------)

in

[Deviant Finance

](https://medium.com/deviantdao?source=read_next_recirc---------3
---------------------b8fee591_7204_4a76_956e_4f1a232857a5-------)

## Deviant Finance: Q1 2022 Status Report

![](https://miro.medium.com/focal/112/112/50/50/0*7UWHsPMyB52ZO4YM)](/deviantdao/deviant-
finance-q1-2022-status-report-11769216c9a6?source=read_next_recirc---------3
---------------------b8fee591_7204_4a76_956e_4f1a232857a5-------)

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

