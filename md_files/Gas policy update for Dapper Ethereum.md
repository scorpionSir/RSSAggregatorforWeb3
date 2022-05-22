[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/117a7474a423&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Dapper
Labs](https://miro.medium.com/fit/c/64/64/1*4qrJW34TWRKo2UlCo9IqbQ.png)](https://medium.com/dapperlabs?source=post_page
-----117a7474a423--------------------------------)

Published in

[Dapper Labs

](https://medium.com/dapperlabs?source=post_page-----
117a7474a423--------------------------------)

[![Dapper
Labs](https://miro.medium.com/fit/c/96/96/1*4qrJW34TWRKo2UlCo9IqbQ.png)](/@hellodapper?source=post_page
-----117a7474a423--------------------------------)

[Dapper Labs](/@hellodapper?source=post_page-----
117a7474a423--------------------------------)

Follow

Sep 3, 2020

·

5 min read

# Gas policy update for Dapper Ethereum

![](https://miro.medium.com/max/1400/1*PjbAXYZ1vfK5v6w22h4nPg@2x.png)

If you’ve used Ethereum in the last few months, you’re well aware of the
impact the network’s gas prices have had on dapp games. With daily average
gwei prices reaching as high as **250+** , the gas fees associated with a
single game transaction can often exceed the ETH being spent. While parts of
the ecosystem are thriving, the dapp gaming community is being forced to find
alternative solutions for their players–Dapper Ethereum included. While we
continue to believe bypassing the need to manually set gas on the fly makes
interacting with dapp games much easier, the realities of the current
ecosystem have forced us to re-evaluate and update our gas policy.

[In addition to the changes we announced
earlier](https://support.dapperlabs.com/hc/en-us/articles/360052128754-Dapper-
version-1-0-0-beta-41-Updates-to-Transaction-Passes), we will no longer be
subsidizing gas for non-Dapper Labs developed games and some non-core
CryptoKitties functions. We’re rolling out the updated policy starting this
**Thursday, September 3rd**.

Now that we’ve ripped that band-aid off, we’d like to be upfront and give you
the exact reason _“Why?”_ and some of the data which has led us to this change
in policy.

# So, why the changes now?

When we first launched CryptoKitties, a major pain point reported by our
players was having to deal with gas. This early feedback pushed the team to
develop a way of removing gas adjustments from the dapp experience entirely.
By achieving this, players could instead focus on playing their favorite
games. However, Ethereum has changed quite a bit since 2017 and we’ve had to
accept new realities–for better and worse. Context is always important, so
here are a few main points which led to our decision.

 **Consistently high gas pricing**. As Ethereum and it’s users grow, how the
network is used is bound to change. As early as 2018, gas use across the whole
network has increased significantly and this trend doesn’t look to be slowing
down anytime soon. For a dapp experimenting with gas abstraction, this makes
things rather difficult.

![](https://miro.medium.com/max/1400/1*neu24UFD5Zvv4m7tsNaS7w.png)

 **The increasing cost of supporting DeFi**. The intended use for Dapper has
always been for games and entertainment with the hope of bringing the benefit
of blockchain to the masses. As cost rose, a compromise we made to continue
subsidizing gas for the community was to lower the number of free weekly
transactions. However, we quickly found this was not enough. From January to
July 2020, our monthly ETH costs increased by **998.88%**. **** From our
internal analysis, a good portion of this was going to subsidize expensive
DeFi transactions.

At current ETH rates, our total spend for July in USD was close to
**$107,000**.

![](https://miro.medium.com/max/1400/1*NNXkzJEmXc1w7fsKKMCG4Q.png)

Monthly subsidized gas in ETH

 **Gas attacks**. The draw of free gas proved too valuable of an asset and,
unfortunately, some bad actors abused our offering. Minting endless gas tokens
or making thousands of micro-transactions weekly, these attacks became more
common as gas pricing spiked. This not only increased cost but also caused a
heavy amount of tech-debt for our engineering team. They had to spend valuable
time monitoring specific transactions rather than focusing on how we could
maintain the best possible product for the community.

# CryptoKitties deep dive

As part of our investigation, we looked into the CryptoKitties contracts for
insight into how gas was being spent. Working alongside their team we dug
deeper into the costs and discovered some interesting behavior.

## The true cost of listing and delisting on the marketplace

Two of the most used functions in the core CryptoKitties contract, exceeding
gifting and even breeding, is listing and delisting cats on the marketplace.
The cost of this innocuous function has skyrocketed as of late. On average, we
found most players place their kitties for sale at about $0.50 cents. The cost
of this action alone can end up being **$2.50** **per** **transaction**. In
the last couple of months, Dapper has subsidized over **$40,500** USD just for
listing and delisting kitties! Regrettably, this cost is simply not
sustainable. In order to continue supporting functions crucial to
CryptoKitties’ core game loop, listing and delisting will no longer be
subsidized by Dapper. All other core functions remain free.

![](https://miro.medium.com/max/1004/1*DKayhjCtA3KrVZzOusluxw.png)

Breakdown of gas expenses to the core CryptoKitties contract

Specifically, these are the specific functions no longer being subsidized:

  * cancelSiringAuction @kittycore
  * cancelSaleAuction @kittycore
  * createSaleAuction @kittycore
  * createSireAuction @kittycore

# Additional Improvements

In addition to the above changes, we’ve also made improvements to Dapper
Ethereum which will alleviate cost while at the same time providing an even
better experience for our community.

  1. Contract (wallet) creation is now more efficient and costs less gas to deploy.
  2. Our co-signers are now more effective at calculating gas prices and are able to better adjust for gas spikes.
  3. We’ve made improvements to our fraud detection to get ahead of future gas attacks.
  4. We’ve lowered the number of purchasable [transaction passes](https://support.dapperlabs.com/hc/en-us/articles/360035211074-How-to-use-Dapper-Pass-and-Transaction-Passes) to **1** , **3** , and **8** as requested by the community so passes can be used on a per-transaction basis.

# Looking ahead to Flow

The learnings we’ve gained from developing on Ethereum have played a major
part in how we’re approaching [**Flow’s**](https://www.onflow.org/)
architecture. While our experiment with Dapper Ethereum may not have panned
out exactly how we expected, we’re very excited for the future with Flow!
Tackling accessibility to the blockchain world is no easy task, but thanks to
feedback (both positive and negative!) we’ve received across all our
products–we couldn’t be more excited for what’s to come. To see what the Flow
team and our early partner developers are up to, join the [Flow
Discord](https://discord.gg/flow) to keep up with the latest developments!

As always, if you have any questions or feedback on these recent changes,
don’t hesitate to reach out on any of our Discord servers or [contact the
Dapper team directly](mailto:support@dapperlabs.com).

\--

2

\--

\--

2

## [More from Dapper Labs](/dapperlabs?source=post_page-----
117a7474a423--------------------------------)

The serious business of fun and games on the blockchain

[Read more from Dapper Labs](/dapperlabs?source=post_page-----
117a7474a423--------------------------------)

## Recommended from Medium

[[![Marginless](https://miro.medium.com/fit/c/40/40/1*3NGcUomlxyLnMsMzWQ1HQw.jpeg)](/@Marginless?source=post_internal_links
---------0----------------------------)

[Marginless

](/@Marginless?source=post_internal_links---------
0----------------------------)

## Interview: Betting Association Founder Gives His Take on the Worldwide
Betting Phenomenon and It’s…

![](https://miro.medium.com/focal/112/112/50/50/1*hsYVOkKwA8S42DxFX2MyCg.jpeg)](/@Marginless/interview-
betting-association-founder-gives-his-take-on-the-worldwide-betting-
phenomenon-and-its-cedf6ff29cf4?source=post_internal_links---------
0----------------------------)

[[![Kommunitas](https://miro.medium.com/fit/c/40/40/1*80tbsYxdhT5vlKX7A6o4LQ.png)](/@kommunitas?source=post_internal_links
---------1----------------------------)

[Kommunitas

](/@kommunitas?source=post_internal_links---------
1----------------------------)

## Kommunitas has officially invested in CryptoVsZombie

![](https://miro.medium.com/focal/112/112/50/50/1*fOsXFvYLOWUE4l2EKQ7mgw@2x.jpeg)](/@kommunitas/kommunitas-
has-officially-invested-in-
cryptovszombie-304831fc2a93?source=post_internal_links---------
1----------------------------)

[[![Sonali
Pandey](https://miro.medium.com/fit/c/40/40/0*5MtR5L0GGzhzQn1J)](/@sonalipandey?source=post_internal_links
---------2----------------------------)

[Sonali Pandey

](/@sonalipandey?source=post_internal_links---------
2----------------------------)

in

[The Capital

](https://medium.com/the-capital?source=post_internal_links---------
2----------------------------)

## Beginner’s guide to Uniswap: Introduction and Functioning

![](https://miro.medium.com/focal/112/112/50/50/1*gYfUM9qd3iuc_Rulk3GqXQ.jpeg)](/the-
capital/beginners-guide-to-uniswap-introduction-and-functioning-
fe3869af1e4b?source=post_internal_links---------2----------------------------)

[[![Aman
Kuvera](https://miro.medium.com/fit/c/40/40/1*wzqB_1aaPAY7ryDj6Xer2Q.png)](/@amankuvera?source=post_internal_links
---------3----------------------------)

[Aman Kuvera

](/@amankuvera?source=post_internal_links---------
3----------------------------)

## What is yield farming and how they are the best passive income strategy?

![](https://miro.medium.com/focal/112/112/50/50/1*pMhCDVRjBapilKmupLWoBw.png)](/@amankuvera/what-
is-yield-farming-and-how-they-are-the-best-passive-income-strategy-
dcaccb117a9c?source=post_internal_links---------3----------------------------)

[[![anya
betadin](https://miro.medium.com/fit/c/40/40/1*NaBXemlxrBMHvwuv6FJk0g.jpeg)](/@anyabett89?source=post_internal_links
---------4----------------------------)

[anya betadin

](/@anyabett89?source=post_internal_links---------
4----------------------------)

## What is InsureDAO

](/@anyabett89/what-is-insuredao-27b1dc6918cb?source=post_internal_links
---------4----------------------------)

[[![Bitcoin
Dood](https://miro.medium.com/fit/c/40/40/1*u0ePLv9u9ixTe8r6QZRA0g.png)](/@thebitcoindood?source=post_internal_links
---------5----------------------------)

[Bitcoin Dood

](/@thebitcoindood?source=post_internal_links---------
5----------------------------)

in

[Investments & Partnerships

](https://medium.com/investments-partnerships?source=post_internal_links
---------5----------------------------)

## CSP DAO Project Review: Cryptomeda

![](https://miro.medium.com/focal/112/112/50/50/0*Zp9ZlllPFK0f8Ipw.jpg)](/investments-
partnerships/csp-dao-project-review-
cryptomeda-8a6ffbddab4d?source=post_internal_links---------
5----------------------------)

[[![Cryptobuddy](https://miro.medium.com/fit/c/40/40/1*hZHJoXOkEjdbQbUaEkaOyA.png)](/@cryptobuddy.info?source=post_internal_links
---------6----------------------------)

[Cryptobuddy

](/@cryptobuddy.info?source=post_internal_links---------
6----------------------------)

## AMA Recap with KSM Starter on Cryptobuddy

![](https://miro.medium.com/focal/112/112/50/50/1*GRfk0N_3SfOX77Unen_kEA.jpeg)](/@cryptobuddy.info/ama-
recap-with-ksm-starter-on-cryptobuddy-4de590f58467?source=post_internal_links
---------6----------------------------)

[[![Sonali
Pandey](https://miro.medium.com/fit/c/40/40/0*5MtR5L0GGzhzQn1J)](/@sonalipandey?source=post_internal_links
---------7----------------------------)

[Sonali Pandey

](/@sonalipandey?source=post_internal_links---------
7----------------------------)

in

[The Capital

](https://medium.com/the-capital?source=post_internal_links---------
7----------------------------)

## New regulations for crypto in Europe poses existential questions for DeFi

![](https://miro.medium.com/focal/112/112/50/50/0*kp8KDL1s4ohyR-KF)](/the-
capital/new-regulations-for-crypto-in-europe-poses-existential-questions-for-
defi-e67d8b2f6dfe?source=post_internal_links---------
7----------------------------)

[](/?source=post_page-----117a7474a423--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
117a7474a423--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
117a7474a423--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
117a7474a423--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
117a7474a423--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----117a7474a423--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----117a7474a423--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fdapperlabs%2Fgas-
policy-update-for-dapper-ethereum-117a7474a423&source=post_page
--------------------------nav_reg-----------)

[![Dapper
Labs](https://miro.medium.com/fit/c/176/176/1*4qrJW34TWRKo2UlCo9IqbQ.png)](/@hellodapper)

[

## Dapper Labs

](/@hellodapper)

800 Followers

The serious business of fun and games on the blockchain

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F92fd7014333&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fdapperlabs%2Fgas-
policy-update-for-dapper-
ethereum-117a7474a423&newsletterV3=6544777e30d2&newsletterV3Id=92fd7014333&user=Dapper+Labs&userId=6544777e30d2&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Rayyan
Sorefan](https://miro.medium.com/fit/c/40/40/1*M-VdveH_-S4wTcWA1jcEhw@2x.jpeg)](/@rayyansorefan?source=read_next_recirc
---------0---------------------32c8c7be_93e4_474f_b5d6_3d59947fdb36-------)

[Rayyan Sorefan

](/@rayyansorefan?source=read_next_recirc---------0---------------------
32c8c7be_93e4_474f_b5d6_3d59947fdb36-------)

in

[Coinmonks

](https://medium.com/coinmonks?source=read_next_recirc---------0
---------------------32c8c7be_93e4_474f_b5d6_3d59947fdb36-------)

## NFTs: A tool used by criminals to launder money and fund terror
organisations

![](https://miro.medium.com/focal/112/112/50/50/0*6FkfKp1Do1RoAFky)](/coinmonks/nfts-
a-tool-used-by-criminals-to-launder-money-and-fund-terror-
organisations-589ec06fe508?source=read_next_recirc---------0
---------------------32c8c7be_93e4_474f_b5d6_3d59947fdb36-------)

[[![Madison Mariani](https://miro.medium.com/fit/c/40/40/1*cEG6fSJn-
Nm0wwbeez1aSA.png)](/@madisonmariani?source=read_next_recirc---------1
---------------------32c8c7be_93e4_474f_b5d6_3d59947fdb36-------)

[Madison Mariani

](/@madisonmariani?source=read_next_recirc---------1---------------------
32c8c7be_93e4_474f_b5d6_3d59947fdb36-------)

in

[B2C2 Group

](https://medium.com/b2c2-crypto-liquidity?source=read_next_recirc---------1
---------------------32c8c7be_93e4_474f_b5d6_3d59947fdb36-------)

## Client Spotlight: Quantfury

![](https://miro.medium.com/focal/112/112/50/50/1*5B4mjHum_3Vy4zRqTTchSQ.png)](/b2c2-crypto-
liquidity/client-spotlight-quantfury-3d05114d250b?source=read_next_recirc
---------1---------------------32c8c7be_93e4_474f_b5d6_3d59947fdb36-------)

[[![Nushi](https://miro.medium.com/fit/c/40/40/1*wOWBCAiTgDruoj7Gy0bNRQ.png)](/@0xnushi?source=read_next_recirc
---------2---------------------32c8c7be_93e4_474f_b5d6_3d59947fdb36-------)

[Nushi

](/@0xnushi?source=read_next_recirc---------2---------------------
32c8c7be_93e4_474f_b5d6_3d59947fdb36-------)

in

[Winter Bears

](https://medium.com/winter-bears?source=read_next_recirc---------2
---------------------32c8c7be_93e4_474f_b5d6_3d59947fdb36-------)

## Hello, Winter Bears DAO!

![](https://miro.medium.com/focal/112/112/50/50/0*XtuWzVPpHKinAoJT.png)](/winter-
bears/hello-winter-bears-dao-bb120d282ab7?source=read_next_recirc---------2
---------------------32c8c7be_93e4_474f_b5d6_3d59947fdb36-------)

[[![WK
Wright](https://miro.medium.com/fit/c/40/40/2*1c0J23IMbLsx2a90u7qPVw.png)](/@wkwright?source=read_next_recirc
---------3---------------------32c8c7be_93e4_474f_b5d6_3d59947fdb36-------)

[WK Wright

](/@wkwright?source=read_next_recirc---------3---------------------
32c8c7be_93e4_474f_b5d6_3d59947fdb36-------)

## Asia’s tech news #143: Indonesian social commerce, Malaysia’s tech moves,
Vietnam’s EV news…

![](https://miro.medium.com/focal/112/112/50/50/0*ItJ7CCpjnDHTivrr)](/@wkwright/asias-
tech-news-143-indonesian-social-commerce-malaysia-s-tech-moves-vietnam-s-ev-
news-e32529f21f01?source=read_next_recirc---------3---------------------
32c8c7be_93e4_474f_b5d6_3d59947fdb36-------)

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

