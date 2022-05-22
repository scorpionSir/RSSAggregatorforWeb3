[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/70782c9e6730&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Instadapp](https://miro.medium.com/fit/c/64/64/1*Jdx_PVb-M-
wDOIBWGFLXhg.png)](https://medium.com/instadapp?source=post_page-----
70782c9e6730--------------------------------)

Published in

[Instadapp

](https://medium.com/instadapp?source=post_page-----
70782c9e6730--------------------------------)

[![Sowmay
Jain](https://miro.medium.com/fit/c/96/96/2*EIXsRWhRSsce2xNnlPjsIQ.jpeg)](/@sowmay?source=post_page
-----70782c9e6730--------------------------------)

[Sowmay Jain](/@sowmay?source=post_page-----
70782c9e6730--------------------------------)

Follow

Nov 12, 2019

·

6 min read

# MCD Migration for Compound Users and Whale CDPs

![](https://miro.medium.com/max/1400/1*rcns8ZGkziHtHwp3VW-UPg.png)

[InstaDApp’s](https://instadapp.io/) approach to DeFi has been to proactively
understand the critical problems in the space, and work on solving them in a
way that’s as trustless and user-friendly as possible.

The **migration to Multi Collateral DAI on Nov 18th** is one of the most
important transitions in the DeFi space thus far. In our opinion, a successful
transition will be a strong testament to the resilience and flexibility of the
DeFi space, much like how successfully managing the [massive volatility in ETH
prices](https://twitter.com/vitalikbuterin/status/987754190406672384) earlier
this year can be seen as a big confidence boost.

As such, we would like to play our part in helping the ecosystem manage this
transition. In our estimation, the most tricky aspects in achieving this
transition are: **(1) the deep interlocking of DAI in various protocols**
(particularly Compound), and **(2) around the need for sufficient SAI
liquidity** (Single Collateral Dai) in the markets during the ongoing
transition.

In this post, we seek to do the following:

  * Articulate our stance on why a successful migration is important for the ecosystem.
  * Clarify the difference between the 2 forms of DAI, and where the confusion stems from.
  * Explain user-facing and potential systemic problems for **Compound users** and **whale CDP owners.**
  * Present our approach to solving the user problem and in turn, mitigating the systemic problems.

 **[NOTE]** For users who are just DAI holders or manage smaller CDPs,
migration should be easy. They will be able to do the migration either using
the InstaDApp or Maker’s site directly. **For Compound users and holders of
bigger CDPs (or anyone who’s interested), please read on.**

Before we begin, note that terminology is a major source of confusion for many
users, even seasoned ones, given the fact that many outlets and projects refer
to the same things using different terminologies.

  *  **Single Collateral DAI** — Maker now refers to this as SAI. This is essentially the “old“ DAI, collateralized only with ETH.
  *  **Multi Collateral DAI** — Maker now refers to this as DAI, as from their point of view, this will be the new default and can be collateralized by multiple tokens. This is also the token that integrates the ‘Dai Savings Rate (DSR)’.

To maximize clarity, we will be referring to **Single Collateral Dai as Sai
and Multi Collateral Dai as Dai** throughout this article.

# For Compound Users

![](https://miro.medium.com/max/1400/1*cKLtOBBd2UQ899_7c5ZMuQ.png)

Compound | SAI debt => DAI debt

Compound Finance is the [biggest holder of
Sai](https://etherscan.io/token/0x89d24a6b4ccb1b6faa2625fe562bdd9a23260359#balances).
Over 34M (25% of Sai supply) is supplied to Compound with over 14M borrowed,
resulting in +40% utilization, at the time of writing.

As such, it is **important for Compound users to be able to easily migrate**
over their debt position from SAI to DAI since the market needs to unfold in a
manner that Compound SAI borrowers are also paying back their debt with proper
alignment. Otherwise, due to the lack of liquidity, the utilization ratio will
max out, freezing the overall Compound SAI market. Let’s dive in.

## Complications

From the **borrower point of view** , Compound SAI borrowers have to pay back
their initial debt (and again borrow equivalent DAI). Since most debt is
borrowed to leverage ETH or other tokens, it is likely they would not have
enough capital at hand. As such, they will need to go through a complex multi-
step process, which looks like this:

  1. Sell off existing token holdings to buy SAI.
  2. Wipe SAI debt.
  3. Draw DAI debt.
  4. Sell DAI to buy the existing token holdings again.

As such, provided the complexity, likely slippage and capital requirements to
payback, it could be unattractive for borrowers to collect SAI from the
market.

Compounding the problem is that from the **lender point of view** , existing
Sai lenders are likely to withdraw to migrate their SAI to DAI, while
potential SAI lenders are also likely to migrate their SAI as well.

When borrowers are not converting their debt position, and lenders are rapidly
converting their SAI holdings, **this has the potential of maxing out the
Compound utilization ratio (which is already very high), and freezing
remaining SAI lenders to take any further actions.**

![](https://miro.medium.com/proxy/1*t5hrOTWP34_l-u-OjAlfzw.png)

 _High utilization rate on Compound Finance_

To prevent that scenario, it is critical to create a proper equilibrium
between SAI lenders and borrowers. The most important factor here is to allow
Compound users to bypass the technical complexities, financial hurdles, and
capital requirements and make it seamless for them to migrate their debt.

## Removing Friction From Compound Migration

In our past experience with the protocol bridge, we have observed how critical
removing frictions from capital intensive operations are — within 3 weeks of
the [launch of our Protocol
Bridge](https://twitter.com/InstaDApp/status/1148299303003119616), it
facilitated the movement of over $40M of ETH between MakerDAO and Compound,
and a big part of the success was in allowing positions to be switched
seamlessly and trustlessly.

Similarly, we will be launching an **InstaDApp Migration Bridge** , of which
one of the main functions is to allow Compound users to convert their SAI debt
to DAI debt in just a single click. This will, in turn, maintain the healthy
money circulation between lenders and borrowers, maximizing the chances of a
healthy functioning market throughout the whole migration.

# For Whale CDP Owners

![](https://miro.medium.com/max/1400/1*12x3aRoFJ_D4UyuSP62S4g.png)

CDP => Vault

Whale CDP holders account for the majority supply of SAI. In fact, the top 100
CDPs generated around 80% of the total SAI supply
([source](https://makerscan.io/cups/leaderboard/100)).

## Complications

In order to migrate CDPs, sufficient liquidity is needed in the migration
contract. For smaller CDPs, it’s likely there will be sufficient liquidity.
However, assuming minor CDPs keep migrating, the SAI balance in the migration
contract will continuously decrease.

Whale CDPs will be prevented from migrating to their CDPs to a Vault, due to
the lack of SAI balance in the migration contract available to wipe the CDP
debt. The inability of this large CDPs to migrate will mean that the majority
of the liquidity and ETH collateral currently used for SAI debt will not be
able to move to the MCD system.

## Solution: Fractional Migration

The InstaDApp Migration Bridge **** will allow whale CDP owners to
fractionally migrate their CDP to MCD Vaults in just a single click. They
don’t need to wait for the migration contract to have an equivalent amount of
SAI supply.

For example, if a user is unable to move 100% of their CDP due to the SAI
balance of the migration contract, they will be able to partially migrate
their CDP up to the value of the SAI balance currently available in the
migration contract.

The process is user-controlled action and owners will have to manually migrate
each time. This will allow whale CDPs to get their migrations started in a
completely trustless manner, without having to wait for the full SAI balance
to be available in the migration contract.

At [InstaDApp](https://instadapp.io/), we work hard on observing the problems
that occur across protocols, and to remove the friction points that result
from them. We believe that reducing the technical, financial and capital
obstacles to operating in this space will be the key to allowing more and more
users and capital to enter the wonderful world of DeFi.

As for next steps, we invite everyone to do the following:

  *  **If you own a big CDP** , feel free to reach us out via [email](mailto:info@instadapp.io) or text any admin on our [Telegram](https://t.me/instadapp) group for personal guidance.
  * [Reach out](mailto:info@instadapp.io) to us if you would like to collaborate on anything.
  * Discuss this topic with us in our [Telegram](https://t.me/instadapp) or [Discord](https://discord.gg/DRtKDP9) channels.
  * Last but not least, look out for our announcement on [Twitter](https://twitter.com/instadapp), post MCD transition, where we will be launching the solutions that we discussed above.

The article is co-authored by Ming and thanks to
[Anthony](https://twitter.com/sassal0x),
[Ryan](https://twitter.com/RyanSAdams),
[Camila](https://twitter.com/CamiRusso),
[Spencer](https://twitter.com/spencernoon), and
[Dan](https://twitter.com/delitzer) for feedback & edits.

\--

\--

\--

## [More from Instadapp](/instadapp?source=post_page-----
70782c9e6730--------------------------------)

Powerful DeFi Management Platform

[Read more from Instadapp](/instadapp?source=post_page-----
70782c9e6730--------------------------------)

## Recommended from Medium

[[![Patrick
Cryptozoa](https://miro.medium.com/fit/c/40/40/1*-30dTMXh_7SOW209YAN9IQ.jpeg)](/@cryptozoa?source=post_internal_links
---------0----------------------------)

[Patrick Cryptozoa

](/@cryptozoa?source=post_internal_links---------
0----------------------------)

in

[Cryptozoa

](https://medium.com/cryptozoa?source=post_internal_links---------
0----------------------------)

## THE CRYPTOZOAN — APRIL 13th, 2022 UPDATE

](/cryptozoa/the-cryptozoan-
april-13th-2022-update-7ef6a7639c87?source=post_internal_links---------
0----------------------------)

[[![SocialVibes](https://miro.medium.com/fit/c/40/40/2*46Fb-
BKVwFRJJ4zu6-zwgQ.jpeg)](/@estalontech?source=post_internal_links---------
1----------------------------)

[SocialVibes

](/@estalontech?source=post_internal_links---------
1----------------------------)

in

[Crypto Creators Economy-18 Checklist to accepting cryptocurrency in your
business!

](https://medium.com/crypto-creators-economy-18-checklist-to-
accepting?source=post_internal_links---------1----------------------------)

## Crypto Creators Economy Checklist 8: Storing Your Crypto In Cold Storage

![](https://miro.medium.com/focal/112/112/50/50/1*pDMijDTfPciDAHwsr77S9w.jpeg)](/crypto-
creators-economy-18-checklist-to-accepting/crypto-creators-economy-
checklist-8-storing-your-crypto-in-cold-
storage-d520702e91ac?source=post_internal_links---------
1----------------------------)

[[![CY
Tan](https://miro.medium.com/fit/c/40/40/1*pOHhzfbxARrCBdhDqYcXvA.png)](/@cy_perlin?source=post_internal_links
---------2----------------------------)

[CY Tan

](/@cy_perlin?source=post_internal_links---------
2----------------------------)

in

[PERL.eco

](https://medium.com/perlin-network?source=post_internal_links---------
2----------------------------)

## PERL.eco — The Planetary Ecosystem Registration Ledger

![](https://miro.medium.com/focal/112/112/50/50/1*9We7wNJaHq0LEGPgfkNeEw.png)](/perlin-
network/perl-eco-the-planetary-ecosystem-registration-
ledger-57566298b880?source=post_internal_links---------
2----------------------------)

[[![Farce
Raisonner](https://miro.medium.com/fit/c/40/40/1*rnLIIgPA0UREwfnbvzbV9g.png)](/@raisonner?source=post_internal_links
---------3----------------------------)

[Farce Raisonner

](/@raisonner?source=post_internal_links---------
3----------------------------)

in

[Bare-knickle (Digital Cash)

](https://medium.com/token-suisse?source=post_internal_links---------
3----------------------------)

## Parsing the Young DAO Concept

![](https://miro.medium.com/focal/112/112/50/50/0*GNX3ELNcyhqNhTE5.)](/token-
suisse/parsing-the-young-dao-concept-d3aa6fe4630a?source=post_internal_links
---------3----------------------------)

[[![Sheraz
ahmed](https://miro.medium.com/fit/c/40/40/1*UVPQuc5E7bGRWWVpNwx98Q.jpeg)](/@jonesahmed71?source=post_internal_links
---------4----------------------------)

[Sheraz ahmed

](/@jonesahmed71?source=post_internal_links---------
4----------------------------)

## Electric Capital closes $1 billion in funds to back crypto startups, buy
tokens

![](https://miro.medium.com/focal/112/112/50/50/0*xwcODaUDAsxC9z50)](/@jonesahmed71/electric-
capital-closes-1-billion-in-funds-to-back-crypto-startups-buy-
tokens-b37bd776ce59?source=post_internal_links---------
4----------------------------)

[[![Ignacio
Patterson](https://miro.medium.com/fit/c/40/40/1*WWhcgYbZeakxiDpZGBP0XA.jpeg)](/@ignacio-
patterson?source=post_internal_links---------5----------------------------)

[Ignacio Patterson

](/@ignacio-patterson?source=post_internal_links---------
5----------------------------)

## Martin Lewis Bitcoin Code — Review

![](https://miro.medium.com/focal/112/112/50/50/0*5UvgAxUYoKHjzZIt.jpg)](/@ignacio-
patterson/martin-lewis-bitcoin-code-
review-9b6348c06573?source=post_internal_links---------
5----------------------------)

[[![Taylor
Kennedy](https://miro.medium.com/fit/c/40/40/1*eZZxR4-DelqhAITqf6TIqA.jpeg)](/@tldrtaylor?source=post_internal_links
---------6----------------------------)

[Taylor Kennedy

](/@tldrtaylor?source=post_internal_links---------
6----------------------------)

in

[DataDrivenInvestor

](https://medium.com/datadriveninvestor?source=post_internal_links---------
6----------------------------)

## 📊 Fully Audited Earnings Per Share in Staking’s Sweetspot HEX Means BIG
Payouts for Shareholders

![HEX
Price](https://miro.medium.com/focal/112/112/50/50/1*Z9Lu4WS7ZlscKViuU7gt-A.jpeg)](/datadriveninvestor/fully-
audited-earnings-per-share-in-stakings-sweetspot-hex-means-big-payouts-for-
shareholders-10972b1f5a3c?source=post_internal_links---------
6----------------------------)

[[![jerkytreats.eth](https://miro.medium.com/fit/c/40/40/1*e830Wv-
UBeRZWi83t9WlBg.png)](/@JerkyTreats?source=post_internal_links---------
7----------------------------)

[jerkytreats.eth

](/@JerkyTreats?source=post_internal_links---------
7----------------------------)

## The Bull Case for Crypto Regulation

![](https://miro.medium.com/focal/112/112/50/50/1*qd3rprjOTpP9MxayOMEMdg.jpeg)](/@JerkyTreats/the-
bull-case-for-crypto-regulation-1f29f7a08f1e?source=post_internal_links
---------7----------------------------)

[](/?source=post_page-----70782c9e6730--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
70782c9e6730--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
70782c9e6730--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
70782c9e6730--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
70782c9e6730--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----70782c9e6730--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----70782c9e6730--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Finstadapp%2Fmcd-
migration-70782c9e6730&source=post_page--------------------------
nav_reg-----------)

[![Sowmay
Jain](https://miro.medium.com/fit/c/176/176/2*EIXsRWhRSsce2xNnlPjsIQ.jpeg)](/@sowmay)

[

## Sowmay Jain

](/@sowmay)

616 Followers

Building Instadapp

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F5610fbf52484&operation=register&redirect=https%3A%2F%2Fmedium.com%2Finstadapp%2Fmcd-
migration-70782c9e6730&newsletterV3=21786e9fd68f&newsletterV3Id=5610fbf52484&user=Sowmay+Jain&userId=21786e9fd68f&source=--------------------------subscribe_user-----------)

## More from Medium

[[![CYBAVO
Inc.](https://miro.medium.com/fit/c/40/40/1*QIy-I3YFsvXqvDi66KjSVw.png)](/@cybavo?source=read_next_recirc
---------0---------------------4a42872b_0607_4cdd_b36b_9a10b88e28fa-------)

[CYBAVO Inc.

](/@cybavo?source=read_next_recirc---------0---------------------
4a42872b_0607_4cdd_b36b_9a10b88e28fa-------)

## The Rise of DAOs: How They Can Transform Institutional Decision-making

![](https://miro.medium.com/focal/112/112/50/50/0*YFKiG_pNX_uTB-
Tt.png)](/@cybavo/the-rise-of-daos-how-they-can-transform-institutional-
decision-making-fbcfba67e8ba?source=read_next_recirc---------0
---------------------4a42872b_0607_4cdd_b36b_9a10b88e28fa-------)

[[![Flor
Gomez](https://miro.medium.com/fit/c/40/40/1*HRflIXbj_1OT9Qc01YxHpw.png)](/@wine-
flor?source=read_next_recirc---------1---------------------
4a42872b_0607_4cdd_b36b_9a10b88e28fa-------)

[Flor Gomez

](/@wine-flor?source=read_next_recirc---------1---------------------
4a42872b_0607_4cdd_b36b_9a10b88e28fa-------)

in

[WIVA by WiV Technology

](https://medium.com/wivmedia?source=read_next_recirc---------1
---------------------4a42872b_0607_4cdd_b36b_9a10b88e28fa-------)

## All you need to know about wine and NFTs -in 4mins read-

![](https://miro.medium.com/focal/112/112/50/50/1*5-E6UTXsLb7r_lsf9B2FbQ.png)](/wivmedia/all-
you-need-to-know-about-wine-and-nfts-in-3-mins-
read-70e1047b1e00?source=read_next_recirc---------1---------------------
4a42872b_0607_4cdd_b36b_9a10b88e28fa-------)

[[![Raziel](https://miro.medium.com/fit/c/40/40/1*LI29OC8Nnmq_5YrxHfW3xw.png)](/@arcadeventures?source=read_next_recirc
---------2---------------------4a42872b_0607_4cdd_b36b_9a10b88e28fa-------)

[Raziel

](/@arcadeventures?source=read_next_recirc---------2---------------------
4a42872b_0607_4cdd_b36b_9a10b88e28fa-------)

## Arcade Ventures: The day you become a VC

![](https://miro.medium.com/focal/112/112/50/50/1*-NEVNrhUFK0usT9T_Fk2kA.png)](/@arcadeventures/arcade-
ventures-the-day-you-become-a-vc-420e2ee29da8?source=read_next_recirc---------
2---------------------4a42872b_0607_4cdd_b36b_9a10b88e28fa-------)

[[![SES](https://miro.medium.com/fit/c/40/40/1*GpJ4ezvZjHirfIzKM-Q7Gg.jpeg)](/@electricsergey?source=read_next_recirc
---------3---------------------4a42872b_0607_4cdd_b36b_9a10b88e28fa-------)

[SES

](/@electricsergey?source=read_next_recirc---------3---------------------
4a42872b_0607_4cdd_b36b_9a10b88e28fa-------)

## Can NFT’s and Web 3.0 help save our planet?

![](https://miro.medium.com/focal/112/112/50/50/1*nkYthrahsb8wRTwUw8FmbA.png)](/@electricsergey/can-
nfts-and-web-3-0-help-save-our-planet-ed2a36617c8e?source=read_next_recirc
---------3---------------------4a42872b_0607_4cdd_b36b_9a10b88e28fa-------)

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

