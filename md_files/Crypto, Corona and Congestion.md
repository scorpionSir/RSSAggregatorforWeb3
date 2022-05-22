[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/cf0dfadc4df0&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Argent](https://miro.medium.com/fit/c/64/64/1*VmJdPIIMxo_J-
EVVvtmt_Q.png)](https://medium.com/argenthq?source=post_page-----
cf0dfadc4df0--------------------------------)

Published in

[Argent

](https://medium.com/argenthq?source=post_page-----
cf0dfadc4df0--------------------------------)

[![Itamar
Lesuisse](https://miro.medium.com/fit/c/96/96/0*WJGl61ia_RRMrZ4Z.jpg)](/@itamarl?source=post_page
-----cf0dfadc4df0--------------------------------)

[Itamar Lesuisse](/@itamarl?source=post_page-----
cf0dfadc4df0--------------------------------)

Follow

Mar 13, 2020

·

5 min read

# Crypto, Corona and Congestion

## Argent’s lessons learned from a challenging couple of days

[“What we really need to cancel is
2020](https://twitter.com/KingJames/status/1237972755275870208?s=20)”. I’m not
quite where Lebron James is at (I’m actually very excited about what 2020
holds for Ethereum), but there’s no doubt the last couple of days have been
challenging for our team and the wider community.

I wanted to share our thoughts on the Ethereum network’s recent congestion,
its impact on Argent wallet owners, and the lessons we learned.

In summary, while the majority of cases were fine there’s clearly things we
need to improve further.

We’ll work on five points:

  1. Improving the visibility of transaction statuses
  2. Giving you more granular control of transactions in an emergency
  3. Managing expectations during congestion
  4. Doing our bit to help minimise congestion
  5. Improving trading within Argent

Now, to start with some context.

#  **What actually happened?**

From Wednesday night the Ethereum network got extremely congested. Gas prices
rocketed 900% compared to their average (100 gwei vs the usual <10 gwei). Eth
Gas Station even recommended 119 gwei for a slow transaction at one point.

This caused transactions across the network to fail. (For more on the role gas
plays in Ethereum, [see this
post](https://ethereum.stackexchange.com/questions/3/what-is-meant-by-the-
term-gas)).

![](https://miro.medium.com/max/1400/1*jRnbkzRQeuBw2V0gg8lGuA.png)

The recent spike in gas price is clearly shown by[
Etherscan](https://etherscan.io/chart/gasprice)

#  **Why did this happen?**

The price of ETH fell dramatically (over 40% in a day) and this liquidated
many people’s Collateralised Debt Positions, as well as their leveraged
positions with dYdX. The volume of transactions surged as people reacted,
clogging the network.

The gas guzzling breakdown

#  **What this meant for Argent**

Unfortunately some transactions failed for Argent wallet owners, as they did
for people across the network. We understand this was frustrating and
concerning. Our team worked through the night to figure out how to give
Argent’s community the best chance of having their transactions go through.

Before going further it’s worth quickly explaining how transactions at Argent
work. We’re a non-custodial wallet (we don’t hold your assets) but we do pay
the gas. How?

We use a system called meta-transactions. With this you authorise a
transaction and this information is sent to a relayer that pays the
transaction and sends it to the destination. The relayer is also non-custodial
— it can’t tamper with a transaction.

In the last couple of days, we used this system to maximise Argent users’
chances of their transactions going through, despite the congestion.

> As an example of this, we’ve spent a total of **55 ETH on gas since
> Wednesday**.

 **We sent ALL transaction at FAST gas price** , paying up to 200–220 gwei for
some of the more expensive ones, even hitting 300 gwei on a couple of
occasions.

Overall we believe this gave Argent owners a better chance to get a
transaction through than any other wallet. But things were far from perfect
and we know paying that kind of gas is not sustainable.

Here are some of the lessons we learned and what we’re doing about them.

#  **1) Visibility of transaction statuses**

We need to improve Argent wallet owners’ visibility of their transaction
statuses. As quickly as possible telling them if it succeeded or not.

Today the status can sometimes lag as we have a complex system that can
dynamically increase gas for transactions without the sender noticing (as we
pay for it behind the scenes). The adjustments cause the transaction hash to
change and the app might not get the latest status.

If you got in touch with our support the last couple of days, this is why
refreshing data in Argent worked.

 ** _What are we doing to improve it?_**

We’re putting the final touches on a more dynamic update system. It has
actually been live for many iOS users already. It should be live for everyone,
including on Android, by the end of the month.

#  **2) More granular control over transactions**

We pay the gas and while we always send everything FAST during congestion,
there may be an emergency when you want to go even faster. You may, for
example, want to close your CDP with 500 gwei gas price. Today you can only do
that by using our [Emergency Kit](/argenthq/the-ultimate-non-custodial-
test-1b3b007e8a53).

 ** _What are we doing to improve it?_**

We’ll make it possible in the app for you to pay the gas for a super fast
transaction in an emergency.

#  **3) Managing expectations during congestion**

A side effect of us abstracting gas from users is that they are unaware when
there’s congestion.

 ** _What are we doing to improve it?_**

During congestion we will show a clear warning in the app. This links to the
next point.

#  **4) Doing our bit to help minimise congestion**

Gas is designed to regulate the network’s usage to minimize the chance of
congestion. Some of the transactions our users made (e.g. a few Dai to a
friend, or an exchange) weren’t urgent and could likely have waited until the
congestion died down.

 ** _What are we doing to improve it?_**

We’ll introduce a fair use policy for gas. This is still to be defined but
will likely mean that each user has a certain gas allowance a month. They can
go over it, but they’d cover the cost. At a time of congestion they may see
the gas required and decide to wait for it to die down.

It’s important to note that **core security actions** for your wallet (e.g.
adding / removing Guardians, recovery, etc.) **will always stay free.**

#  **5) Exchange improvements**

The last couple of days showed we can do a better job of helping people
exchange during high market volatility. Some trades failed as even with 1%
slippage the market moved too fast.

 ** _What are we doing to improve it?_**

We’re implementing token to token transactions without the need to go through
ETH. So you can go from DAI to USDC, for example, and not DAI-ETH-USDC.

We’re also working on exchange routing to seamlessly connect to several DEXs
within Argent. Depending on what’s best for you we’ll route the trade to the
best DEX or even split it amongst multiple DEXs to limit slippage.

# The conclusion

To wrap up, we’re grateful to all our users for weathering the volatility and
we’re excited about an even stronger Argent in the months to come.

![](https://miro.medium.com/max/1400/1*d-v254BvNfGmXNV14hVIZA.png)

\--

2

\--

\--

2

## [More from Argent](/argenthq?source=post_page-----
cf0dfadc4df0--------------------------------)

Our blog has moved to: www.argent.xyz/blog

[Read more from Argent](/argenthq?source=post_page-----
cf0dfadc4df0--------------------------------)

## Recommended from Medium

[[![Peng
Zhong](https://miro.medium.com/fit/c/40/40/1*-XXXJLN45ee2Ack6Pxrb1g.jpeg)](/@nylira?source=post_internal_links
---------0----------------------------)

[Peng Zhong

](/@nylira?source=post_internal_links---------0----------------------------)

in

[Tendermint Blog

](https://medium.com/tendermint?source=post_internal_links---------
0----------------------------)

## Accelerating the Internet of Blockchains: Tendermint in 2020

![](https://miro.medium.com/focal/112/112/50/50/1*hQ96ehhbidma-
yGqRxCxGA.jpeg)](/tendermint/accelerating-the-internet-of-blockchains-
tendermint-in-2020-85cdb2956cdd?source=post_internal_links---------
0----------------------------)

[[![Jason
Wu](https://miro.medium.com/fit/c/40/40/2*m1leALlDvHNXhrcJHwSQBg.jpeg)](/@JasonDeFiner?source=post_internal_links
---------1----------------------------)

[Jason Wu

](/@JasonDeFiner?source=post_internal_links---------
1----------------------------)

in

[DataDrivenInvestor

](https://medium.com/datadriveninvestor?source=post_internal_links---------
1----------------------------)

## Basics of Second Generation Blockchain and its Applications in Capital
Market

![](https://miro.medium.com/focal/112/112/50/50/1*r8iXqK5-SaRvdHLQTT1V0w.png)](/datadriveninvestor/basics-
of-second-generation-blockchain-and-its-applications-in-capital-
market-244f75ce72ff?source=post_internal_links---------
1----------------------------)

[[![Loopstarter](https://miro.medium.com/fit/c/40/40/1*sJJvAmCej0EMFVYQT6XD_g.png)](/@loopstarter01_25107?source=post_internal_links
---------2----------------------------)

[Loopstarter

](/@loopstarter01_25107?source=post_internal_links---------
2----------------------------)

## Loopstarter Launches on Binance Smart Chain & Why We Built on BSC ?

![](https://miro.medium.com/focal/112/112/50/50/1*BZGYLnb5UrmoA0gFGU8bNw.png)](/@loopstarter01_25107/loopstarter-
launches-on-binance-smart-chain-why-we-built-on-
bsc-204f1f864628?source=post_internal_links---------
2----------------------------)

[[![VeChain
Foundation](https://miro.medium.com/fit/c/40/40/0*LYcooa4R5aE5OPJ5.jpg)](/@vechainofficial?source=post_internal_links
---------3----------------------------)

[VeChain Foundation

](/@vechainofficial?source=post_internal_links---------
3----------------------------)

in

[VeChain Foundation

](https://medium.com/vechain-foundation?source=post_internal_links---------
3----------------------------)

## Canadian Sustainable Apparel Frank and Oak Showcases New Collection Traced
by VeChain In Its First…

![](https://miro.medium.com/focal/112/112/50/50/0*d1Q9cBkfua2lABZ1)](/vechain-
foundation/canadian-sustainable-apparel-frank-and-oak-showcases-new-
collection-traced-by-vechain-in-its-
first-8b9f3d8cd058?source=post_internal_links---------
3----------------------------)

[[![Osabuohien
Oghagbon](https://miro.medium.com/fit/c/40/40/1*dmbNkD5D-u45r44go_cf0g.png)](/@gwyccqwz?source=post_internal_links
---------4----------------------------)

[Osabuohien Oghagbon

](/@gwyccqwz?source=post_internal_links---------4----------------------------)

## Choice Coin is a digital asset(open source), that stands out to tackle the
“problem” associated…

](/@gwyccqwz/choice-coin-is-a-digital-asset-open-source-that-stands-out-to-
tackle-the-problem-associated-afad8b69f6ab?source=post_internal_links---------
4----------------------------)

[[![Ben
Mason](https://miro.medium.com/fit/c/40/40/1*QTJCgzN1y3Pj0oXWgZKmmg@2x.jpeg)](/@benmason77?source=post_internal_links
---------5----------------------------)

[Ben Mason

](/@benmason77?source=post_internal_links---------
5----------------------------)

## Welcome to the AreaX NFT platform on the Telos blockchain network.

![](https://miro.medium.com/focal/112/112/50/50/1*xTIZYvMMe1HovevB4memqA@2x.jpeg)](/@benmason77/welcome-
to-the-areax-nft-platform-on-the-telos-blockchain-
network-e99ae9d010d7?source=post_internal_links---------
5----------------------------)

[[![Lisa](https://miro.medium.com/fit/c/40/40/1*Mea6oSOYrEUysHDG4bYNkw.jpeg)](/@lisaspace?source=post_internal_links
---------6----------------------------)

[Lisa

](/@lisaspace?source=post_internal_links---------
6----------------------------)

in

[DefiSpace

](https://medium.com/defispace?source=post_internal_links---------
6----------------------------)

## How dApps Can Revolutionize Finance

![](https://miro.medium.com/focal/112/112/50/50/0*oFScYjcMMylY3Mpv.jpeg)](/defispace/how-
dapps-can-revolutionize-finance-3bf6f305da48?source=post_internal_links
---------6----------------------------)

[[![Jordan](https://miro.medium.com/fit/c/40/40/1*fZ8TS6eZL3JHbQyE1m39vA.jpeg)](/@jordan-66924?source=post_internal_links
---------7----------------------------)

[Jordan

](/@jordan-66924?source=post_internal_links---------
7----------------------------)

## Gaimin.io — Market Analysis and Project Review

![](https://miro.medium.com/focal/112/112/50/50/0*DjN-5oCI5upAijeF.png)](/@jordan-66924/gaimin-
io-market-analysis-and-project-review-1c9cc070a7eb?source=post_internal_links
---------7----------------------------)

[](/?source=post_page-----cf0dfadc4df0--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
cf0dfadc4df0--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
cf0dfadc4df0--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
cf0dfadc4df0--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
cf0dfadc4df0--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----cf0dfadc4df0--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----cf0dfadc4df0--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fargenthq%2Fcrypto-
corona-and-congestion-cf0dfadc4df0&source=post_page--------------------------
nav_reg-----------)

[![Itamar
Lesuisse](https://miro.medium.com/fit/c/176/176/0*WJGl61ia_RRMrZ4Z.jpg)](/@itamarl)

[

## Itamar Lesuisse

](/@itamarl)

822 Followers

Co-founder at Argent, previously founded Peak, ex Amazon, Visa and BCG.

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F851b04281316&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fargenthq%2Fcrypto-
corona-and-congestion-
cf0dfadc4df0&newsletterV3=bb811113f974&newsletterV3Id=851b04281316&user=Itamar+Lesuisse&userId=bb811113f974&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Celal
AKSU](https://miro.medium.com/fit/c/40/40/1*5bA5N39dDBHjKUJ6yRCq-g.jpeg)](/@celalaksu?source=read_next_recirc
---------0---------------------59b4d2ad_34ed_4de4_bcd5_9ea7c5eda7a9-------)

[Celal AKSU

](/@celalaksu?source=read_next_recirc---------0---------------------
59b4d2ad_34ed_4de4_bcd5_9ea7c5eda7a9-------)

## How did I start blockchain technology with patika and near?

](/@celalaksu/how-did-i-start-blockchain-technology-with-patika-and-near-
ce74b2e95516?source=read_next_recirc---------0---------------------
59b4d2ad_34ed_4de4_bcd5_9ea7c5eda7a9-------)

[[![Sarah
Knapp](https://miro.medium.com/fit/c/40/40/1*wJWr8Vt3dfJ8MoliI1jHMw.jpeg)](/@sarah.a.knapp?source=read_next_recirc
---------1---------------------59b4d2ad_34ed_4de4_bcd5_9ea7c5eda7a9-------)

[Sarah Knapp

](/@sarah.a.knapp?source=read_next_recirc---------1---------------------
59b4d2ad_34ed_4de4_bcd5_9ea7c5eda7a9-------)

## What Exactly Is Blockchain?

![](https://miro.medium.com/focal/112/112/50/50/1*QE2GgTpA0CLzUzD7PSlmbQ.jpeg)](/@sarah.a.knapp/what-
exactly-is-blockchain-bd3b37f8a104?source=read_next_recirc---------1
---------------------59b4d2ad_34ed_4de4_bcd5_9ea7c5eda7a9-------)

[[![NVSTX - Copy Investment
App](https://miro.medium.com/fit/c/40/40/1*dD9BOi_GQ0yBXK8xE474eQ.png)](/@nvstx?source=read_next_recirc
---------2---------------------59b4d2ad_34ed_4de4_bcd5_9ea7c5eda7a9-------)

[NVSTX - Copy Investment App

](/@nvstx?source=read_next_recirc---------2---------------------
59b4d2ad_34ed_4de4_bcd5_9ea7c5eda7a9-------)

## 3 reasons why Waves price gained 100%+ in the last week

![](https://miro.medium.com/focal/112/112/50/50/0*9cyJckFkJUXYVmNY.png)](/@nvstx/3-reasons-
why-waves-price-gained-100-in-the-last-
week-3f94b4644c6f?source=read_next_recirc---------2---------------------
59b4d2ad_34ed_4de4_bcd5_9ea7c5eda7a9-------)

[[![Gyanapriya
Pradhan](https://miro.medium.com/fit/c/40/40/0*eWma5JFdE8y3spjV)](/@gyana.cse7?source=read_next_recirc
---------3---------------------59b4d2ad_34ed_4de4_bcd5_9ea7c5eda7a9-------)

[Gyanapriya Pradhan

](/@gyana.cse7?source=read_next_recirc---------3---------------------
59b4d2ad_34ed_4de4_bcd5_9ea7c5eda7a9-------)

## Ethereum Crypto Currency

![](https://miro.medium.com/focal/112/112/50/50/1*K6jFvxsJpD4b77h0jfkAQA.jpeg)](/@gyana.cse7/ethereum-
crypto-currency-ee33533510f0?source=read_next_recirc---------3
---------------------59b4d2ad_34ed_4de4_bcd5_9ea7c5eda7a9-------)

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

