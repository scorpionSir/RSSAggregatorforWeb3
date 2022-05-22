[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/7e21fb0a4e8f&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![DMM
DAO](https://miro.medium.com/fit/c/64/64/1*-L0qPeSrInrhpfHy_fZvNg.png)](https://medium.com/dmm-
dao?source=post_page-----7e21fb0a4e8f--------------------------------)

Published in

[DMM DAO

](https://medium.com/dmm-dao?source=post_page-----
7e21fb0a4e8f--------------------------------)

[![Javier
Keough](https://miro.medium.com/fit/c/96/96/1*YVbQv66nrI2TfLptDGdI1g.jpeg)](/@Javier_Keough?source=post_page
-----7e21fb0a4e8f--------------------------------)

[Javier Keough](/@Javier_Keough?source=post_page-----
7e21fb0a4e8f--------------------------------)

Follow

Sep 26, 2020

·

4 min read

# Implementing More Farming Pairs into The DMM Ecosystem

![](https://miro.medium.com/max/1400/1*o4L40OI0rg1NikZn0FAWaQ.png)

The DMM foundation is proud to unveil the integration of Chainlink (LINK) into
the ecosystem as well as additional farming features. This development will
allow users to seamlessly farm DMG with LINK, and we will also be adding other
farmable tokens, which are still being finalized. The ability to farm DMG with
other non-native tokens will play an integral role in bootstrapping the
ecosystem and allows us to further decentralize the protocol.

 **How will LINK and other tokens be integrated into the ecosystem?**

Currently, farming in the DMM Ecosystem is limited to the native token pairs —
that is mTokens that are paired with their non-mToken counterpart (like ETH-
mETH). Now for the first time, users will be able to farm DMG with non-native
tokens, perpetuating growth in the ecosystem. The first non-native pair that
yield farming will support are LINK against all mToken pairs: LINK-mETH, LINK-
mUSDT, LINK-mDAI, and LINK-mUSDC. In the near future, yield farming will also
support other non-native pairs which are still being determined.

In addition to these developments, we will be implementing a 0.5% withdrawal
fee for native pairs (USDC-mUSDC, or said differently, an underlying asset
against its wrapped mToken variant) and 1% for non-native pairs (LINK and
other farmable tokens). The fee will be used to automatically purchase DMG and
burn it, which helps offset new DMG being introduced via farming and will
continue to lower the already finite amount of DMG. Moreover, it will
encourage users to keep deposits in the protocol longer, in order to outweigh
the costs of the fees. The fee will be calculated as follows for all non-DMG
pairs:

> (fee_percentage * non-mToken holdings)

For DMG pairs we may add in the near future, the fee is calculated as follows:

> (fee_percentage * non-DMG holdings) + (fee_percentage * DMG holdings)

More general information on how yield farming works can be found: [Here](/dmm-
dao/introducing-yield-farming-into-the-dmm-ecosystem-8e33a45fc226).

 **How will the addition of the withdrawal fee impact the circulating supply
of DMG?**

If we look at a couple of key factors and do some estimations on the math, we
can actually extrapolate how much this will impact the introduction of new
DMG. Let’s take a look at these variables and work through the math:

![](https://miro.medium.com/max/480/1*8QT6k4igQD_x76AOB6yNYw.png)

The DMG growth coefficient is the main variable, aside from price, that
affects DMG introduction via yield farming.

While this number looks very large, it actually is represented as “how much
DMG gets introduced every second for every dollar being farmed in the
protocol.” This number is represented in “wei” format, meaning it actually has
18 decimals of precision when formatted. This equals _0.000000012860082_ DMG
every second for every dollar farmed. If we multiply it by the number of
seconds the contract has been in existence so far, which is about 21 days or
_180,600_ seconds, that is _0.02333333_. Now, if we divide the amount of DMG
actually distributed over the 21 days, which is 4,000 DMG, we can find out how
dollars have been withdrawn over this time period ( _4,000 / 0.02333333 =
$171,428)_. Note: this calculation is an estimation and not exact. It is based
on the average of how much time the contracts have been in existence. Now, if
we apply a 0.5% fee to the total of $171,428, we get $857.14. Let’s divide
this by the current price of DMG ($0.38) to come to our final number of 2,255
DMG burned. Meaning, had the withdrawal fee been active at the start of
farming, more than half of the DMG introduced would have been burned through
this withdrawal fee mechanism.

Of course, these estimations could change significantly depending on the
frequency of withdrawals, the price of DMG, and the composition of deposits
(more people farming with non-native pairs leads to a fee of 1% instead of
0.5%).

 **Why are these developments such a valuable addition to the DMM Ecosystem?**

We believe these developments will provide greater utility in the ecosystem
and help drive growth, which will allow the DMM ecosystem to democratize
access to yield. By granting users a wider variety of tokens to farm with, we
hope to drive the growth of mToken deposits. In turn, this will allow the DMM
Ecosystem and principle/affiliate members to seamlessly onboard additional
interest generating assets into the ecosystem. This, in conjunction with the
0.5% — 1.0% withdrawal fee, will incentivize users to lock up their assets in
the farming platform long term. In doing this, we hope to create greater
demand for mTokens; consequently, driving the value of the DMM: Governance
token (DMG).

As the DMM Ecosystem grows, we hope to add more farmable pairs and increase
the utility of the DMG tokens: by facilitating mTokens deposits. We believe
that this is an integral stepping stone to providing greater accessibility to
yield and making the financial system more equitable!

 **About DMM**

DeFi Money Market (DMM) is an ecosystem built on the Ethereum blockchain that
bridges interest-generating real world assets into the Decentralized Finance
(DeFi) ecosystem in a transparent, trust-minimized, overcollateralized, and
permissionless manner.

[Website](https://defimoneymarket.com/) |
[mTokens](https://app.defimoneymarket.com/) |
[DAO](http://dao.defimoneymarket.com/) |
[Explorer](https://explorer.defimoneymarket.com/) |
[Twitter](https://twitter.com/DMMDAO) | [Discord](https://discord.gg/nTSgC9h)
| [Telegram](https://t.me/DmmOfficial) | [Github](https://github.com/defi-
money-market-ecosystem/protocol)

\--

\--

\--

## [More from DMM DAO](/dmm-dao?source=post_page-----
7e21fb0a4e8f--------------------------------)

DeFi Money Market DAO

[Read more from DMM DAO](/dmm-dao?source=post_page-----
7e21fb0a4e8f--------------------------------)

## Recommended from Medium

[[![ProtoFi](https://miro.medium.com/fit/c/40/40/1*d8Ut8seuWstkmozGddqsrg.png)](/@protofi.app?source=post_internal_links
---------0----------------------------)

[ProtoFi

](/@protofi.app?source=post_internal_links---------
0----------------------------)

## ProtoFi Ramps Up for Launch!

![](https://miro.medium.com/focal/112/112/50/50/1*fAL8Pcmq_T8DwvEJYEL4oA.png)](/@protofi.app/protofi-
ramps-up-for-launch-52666f3c8401?source=post_internal_links---------
0----------------------------)

[[![Crypto
Society](https://miro.medium.com/fit/c/40/40/1*G8X1K33gB41svFVUW_PL7A.png)](/@cryptosocietytg?source=post_internal_links
---------1----------------------------)

[Crypto Society

](/@cryptosocietytg?source=post_internal_links---------
1----------------------------)

## Crypto Society Ama Recap with FTMO -17th October 2021.

![](https://miro.medium.com/focal/112/112/50/50/1*tWLzkA2OXPTIIGzzSORZcQ.jpeg)](/@cryptosocietytg/crypto-
society-ama-recap-with-ftmo-17th-
october-2021-3e2b0c5e2d2?source=post_internal_links---------
1----------------------------)

[[![SmartLaunch](https://miro.medium.com/fit/c/40/40/1*nPZgcZXTxjcWs5t2vb8PQg.png)](/@SmartLaunch?source=post_internal_links
---------2----------------------------)

[SmartLaunch

](/@SmartLaunch?source=post_internal_links---------
2----------------------------)

## Crypto News Today: 23/01/2022

![](https://miro.medium.com/focal/112/112/50/50/1*TRiTlCpRiwFiha7j6IMS9w.jpeg)](/@SmartLaunch/crypto-
news-today-23-01-2022-ed383163b998?source=post_internal_links---------
2----------------------------)

[[![Subsmipa](https://miro.medium.com/fit/c/40/40/1*dmbNkD5D-u45r44go_cf0g.png)](/@subsmipa?source=post_internal_links
---------3----------------------------)

[Subsmipa

](/@subsmipa?source=post_internal_links---------3----------------------------)

## TITS COIN IS A NEW MEME. What it’s all about?

![](https://miro.medium.com/focal/112/112/50/50/0*t_L5NYEEKuDb4R-6.png)](/@subsmipa/tits-
coin-is-a-new-meme-what-its-all-about-1525cdf938e?source=post_internal_links
---------3----------------------------)

[[![ITSMYNE](https://miro.medium.com/fit/c/40/40/1*UnMt3oc0OIH_zywM2ww6tQ.png)](/@itsmyne?source=post_internal_links
---------4----------------------------)

[ITSMYNE

](/@itsmyne?source=post_internal_links---------4----------------------------)

## Crypto Glossary

![](https://miro.medium.com/focal/112/112/50/50/1*IPYlLRbL0l47CobtIQ1BHA.jpeg)](/@itsmyne/crypto-
glossary-d7cc2a7a4bc1?source=post_internal_links---------
4----------------------------)

[[![Jorrit
Horstman](https://miro.medium.com/fit/c/40/40/1*OCbkYX7YyvaHvht7stYZPg.jpeg)](/@jorrith?source=post_internal_links
---------5----------------------------)

[Jorrit Horstman

](/@jorrith?source=post_internal_links---------5----------------------------)

in

[THXprotocol

](https://medium.com/thxprotocol?source=post_internal_links---------
5----------------------------)

## $THX launch mission completed 🪐— learn what is next 🔭

![](https://miro.medium.com/focal/112/112/50/50/1*oNkhHNKs2cgdniSoDQXUoQ.png)](/thxprotocol/thx-
launch-mission-completed-learn-what-is-
next-42345c88393b?source=post_internal_links---------
5----------------------------)

[[![Reiner
Knapp](https://miro.medium.com/fit/c/40/40/1*1mTmvz_BOvurrA32goDMRA.png)](/@reinknapp?source=post_internal_links
---------6----------------------------)

[Reiner Knapp

](/@reinknapp?source=post_internal_links---------
6----------------------------)

## [Day2] Baked Beans Miner earns 8% daily…

![](https://miro.medium.com/focal/112/112/50/50/1*-GqdoK0q40W6jowcjXlzJA.jpeg)](/@reinknapp/day2-baked-
beans-miner-earns-8-daily-3530cd890b14?source=post_internal_links---------
6----------------------------)

[[![chainalpha](https://miro.medium.com/fit/c/40/40/1*KUu9UW8Ui92slbRK66Ybsg.png)](/@chainalpha?source=post_internal_links
---------7----------------------------)

[chainalpha

](/@chainalpha?source=post_internal_links---------
7----------------------------)

## DailyCrypto — 05/03: RNDR, RLY and HNT on Top

![](https://miro.medium.com/focal/112/112/50/50/1*1CvByOTyDq_SOrIue4WPlw.png)](/@chainalpha/dailycrypto-05-03-rndr-
rly-and-hnt-on-top-89ac594983e0?source=post_internal_links---------
7----------------------------)

[](/?source=post_page-----7e21fb0a4e8f--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
7e21fb0a4e8f--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
7e21fb0a4e8f--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
7e21fb0a4e8f--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
7e21fb0a4e8f--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----7e21fb0a4e8f--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----7e21fb0a4e8f--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fdmm-
dao%2Fimplementing-more-farming-pairs-into-the-dmm-
ecosystem-7e21fb0a4e8f&source=post_page--------------------------
nav_reg-----------)

[![Javier
Keough](https://miro.medium.com/fit/c/176/176/1*YVbQv66nrI2TfLptDGdI1g.jpeg)](/@Javier_Keough)

[

## Javier Keough

](/@Javier_Keough)

53 Followers

Head of Ecosystem Development @DMMDAO

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fusers%2F14acc5c7db26%2Flazily-enable-
writer-
subscription&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fdmm-
dao%2Fimplementing-more-farming-pairs-into-the-dmm-
ecosystem-7e21fb0a4e8f&user=Javier+Keough&userId=14acc5c7db26&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Orkut
Buyukkokten](https://miro.medium.com/fit/c/40/40/0*oF7QKhIx7MpfHM5G.png)](/@orkut?source=read_next_recirc
---------0---------------------ceeef88f_30f0_4e66_9616_bfc2cc1f8602-------)

[Orkut Buyukkokten

](/@orkut?source=read_next_recirc---------0---------------------
ceeef88f_30f0_4e66_9616_bfc2cc1f8602-------)

## The Gift

![](https://miro.medium.com/focal/112/112/50/50/1*84GafHpeDMU3FP0vjZtWIA.jpeg)](/@orkut/the-
gift-53734fee7c7d?source=read_next_recirc---------0---------------------
ceeef88f_30f0_4e66_9616_bfc2cc1f8602-------)

[[![SailFuture](https://miro.medium.com/fit/c/40/40/1*UcPJwBwGHQ-moJ-
xLTVdRA.png)](/@sailfuture?source=read_next_recirc---------1
---------------------ceeef88f_30f0_4e66_9616_bfc2cc1f8602-------)

[SailFuture

](/@sailfuture?source=read_next_recirc---------1---------------------
ceeef88f_30f0_4e66_9616_bfc2cc1f8602-------)

## Fire and Ice.

![](https://miro.medium.com/focal/112/112/50/50/1*QL2EFiYgnzUs4780nohGtw.jpeg)](/@sailfuture/fire-
and-ice-dbdced386768?source=read_next_recirc---------1---------------------
ceeef88f_30f0_4e66_9616_bfc2cc1f8602-------)

[[![Kafka S.](https://miro.medium.com/fit/c/40/40/1*AEuGjqbHY-
jFJFI8vOrsYg.jpeg)](/@misskafkasu?source=read_next_recirc---------2
---------------------ceeef88f_30f0_4e66_9616_bfc2cc1f8602-------)

[Kafka S.

](/@misskafkasu?source=read_next_recirc---------2---------------------
ceeef88f_30f0_4e66_9616_bfc2cc1f8602-------)

## Goodbyes

![](https://miro.medium.com/focal/112/112/50/50/1*IabQNMH1l7m2mrdrQlqj6A.jpeg)](/@misskafkasu/goodbyes-606167e86541?source=read_next_recirc
---------2---------------------ceeef88f_30f0_4e66_9616_bfc2cc1f8602-------)

[[![Tristan
Collombin](https://miro.medium.com/fit/c/40/40/0*R_CgkxQQRLcXznfY)](/@tristan.collombin?source=read_next_recirc
---------3---------------------ceeef88f_30f0_4e66_9616_bfc2cc1f8602-------)

[Tristan Collombin

](/@tristan.collombin?source=read_next_recirc---------3---------------------
ceeef88f_30f0_4e66_9616_bfc2cc1f8602-------)

## Managing Addictions

](/@tristan.collombin/managing-addictions-7cf491e83424?source=read_next_recirc
---------3---------------------ceeef88f_30f0_4e66_9616_bfc2cc1f8602-------)

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

