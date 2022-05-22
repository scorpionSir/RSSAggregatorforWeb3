[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/b7d59d2ff2c7&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Muun](https://miro.medium.com/fit/c/64/64/1*ZHNsPvynwNOPydFxp27GCw.png)](https://medium.com/muunwallet?source=post_page
-----b7d59d2ff2c7--------------------------------)

Published in

[Muun

](https://medium.com/muunwallet?source=post_page-----
b7d59d2ff2c7--------------------------------)

[![Muun](https://miro.medium.com/fit/c/96/96/1*jqkB48eViAMK840DLgF5FA.png)](/@muunwallet?source=post_page
-----b7d59d2ff2c7--------------------------------)

[Muun](/@muunwallet?source=post_page-----
b7d59d2ff2c7--------------------------------)

Follow

Apr 7, 2020

·

3 min read

# Save up to 30% in fees with Muun’s new mempool-based estimator

![](https://miro.medium.com/max/1400/0*lEDFE3AzxMBT1vPl.png)

Muun users can now benefit from paying more efficient fees on transactions
that they want to be confirmed in the next block. More efficient fees mean
**not overpaying** when it isn’t needed, **nor underestimating** the fee rate
when the network congestion gets high. This new fee estimator bases its
predictions on the current state of the mempool and was entirely built and
trained by Muun’s Team.

# What’s new

The main difference with the previous estimator, and the vast majority of
them, is that the new one is **mempool-based** : this means it looks at the
current state of the mempool to suggest an optimal fee rate for your
transaction to get confirmed in the next block.

This process may sound familiar: many bitcoin users choose the fee rate of
their transactions by looking at the mempool. In contrast, the vast majority
of current estimators suggest fee rates by looking at past blocks,
transactions, and fee rates.

In cases where the mempool has a constant size, both estimators have a similar
behavior: they suggest similar fees for the next block and have the same
precision (think of precision as the probability of actually getting your
transaction confirmed in the next block if you take the suggested fee).
However, the estimators will suggest different fees when the mempool size
varies.

Variations in the mempool occur quite frequently and may have different
causes. Perhaps the simplest one is that a block might take way less or way
more than 10 minutes to be mined.

When a block isn’t mined for a long period of time, the mempool gets packed
with transactions. If your wallet doesn’t consider this, it will underestimate
the fee needed for the next block. The result is you lose precision: you set a
fee expecting your transaction to be confirmed in the next block, but it
doesn’t. Spam attacks can lead to the same scenario.

Similarly, if two or more blocks get mined in a short period of time, the
mempool may lower its size considerably. If your wallet doesn’t take this into
account, you probably pay more in fees than what is actually necessary.
Mempool-based estimators can use the current state of the mempool to prevent
either of these scenarios from happening.

# Benchmarks

In order to benchmark the new estimator, we took data from the last half-year
and chose some of the most popular estimators in the industry, including Earn,
another mempool-based estimator, and Bitcoind.

For each estimator, we set the parameters of our estimator to match its
precision (higher precision means more chances of confirmation, but more
expensive) and calculated the differences of the estimated fees.

  * Bitcoind conservative (precision 82.26%): Muun’s fee estimator is 29.89% cheaper, on average, for the same precision.
  * Bitcoind economical (precision 71.89%): Muun’s fee estimator is 12.86% cheaper, on average, for the same precision.
  * Earn (precision 87.83%): Muun’s fee estimator is 23.75% cheaper, on average, for the same precision.

# What’s next

At Muun, we consider fees to be very important in a bitcoin wallet, and we
think they will become even more relevant with time. This is one of the
reasons why we are implementing Lightning Network, and why the wallet has full
Bech32 support. In the next couple of months, we’ll keep working on improving
this estimator which, for the moment, only makes predictions for the next
block. We are also starting to work with RBF. Stay tuned!

 _Download Muun:_ [get.muun.com](get.muun.com)

 _Visit Muun Website:_[ _https://muun.com/_](https://muun.com/)

 _Follow Muun on Twitter:_[
_https://twitter.com/MuunWallet_](https://twitter.com/MuunWallet)

 _Originally published at_[
_https://blog.muun.com_](https://blog.muun.com/save-up-to-30-in-on-chain-fees-
with-muuns-new-mempool-based-estimator/) _on April 7, 2020._

\--

\--

\--

## [More from Muun](/muunwallet?source=post_page-----
b7d59d2ff2c7--------------------------------)

Stories from Muun, the most powerful Bitcoin and Lightning wallet

[Read more from Muun](/muunwallet?source=post_page-----
b7d59d2ff2c7--------------------------------)

## Recommended from Medium

[[![Michael Bacina](https://miro.medium.com/fit/c/40/40/1*txfWOaD-
SbFzvx1NtonvCQ.jpeg)](/@MikeBacina?source=post_internal_links---------
0----------------------------)

[Michael Bacina

](/@MikeBacina?source=post_internal_links---------
0----------------------------)

## Louisiana lauds legislation establishing licensing regime

![Louisiana lauds legislation establishing licensing
regime](https://miro.medium.com/focal/112/112/50/50/0*L5by8uCMb-
FLMMsm.png)](/@MikeBacina/louisiana-lauds-legislation-establishing-licensing-
regime-a376c7d67782?source=post_internal_links---------
0----------------------------)

[[![Cryptowid](https://miro.medium.com/fit/c/40/40/2*CJz-
gpKcyvcpxhYcW1VHug.jpeg)](/@cryptowid?source=post_internal_links---------
1----------------------------)

[Cryptowid

](/@cryptowid?source=post_internal_links---------
1----------------------------)

## xWIN AMA Recap — 30/07/2021

![](https://miro.medium.com/focal/112/112/50/50/1*bKYSgFXATtz6IHX189Jbmw.jpeg)](/@cryptowid/xwin-
ama-recap-30-07-2021-9fb93454a50b?source=post_internal_links---------
1----------------------------)

[[![WIZARD
TOKEN](https://miro.medium.com/fit/c/40/40/1*PvwrMPuHKUz0BQ6zkd8Cig.png)](/@wizardtokenofficial?source=post_internal_links
---------2----------------------------)

[WIZARD TOKEN

](/@wizardtokenofficial?source=post_internal_links---------
2----------------------------)

## Wizard and Polkawar are Making Magic Together!

![](https://miro.medium.com/freeze/focal/112/112/50/50/1*Ta1duQVQuyLv2uAACxLeIw.gif)](/@wizardtokenofficial/wizard-
and-polkawar-are-making-magic-together-24fa9e23ac4f?source=post_internal_links
---------2----------------------------)

[[![FMFW.io](https://miro.medium.com/fit/c/40/40/1*FguReUhkes4m9OuVuyN-
Gw.png)](/@fmfw-io?source=post_internal_links---------
3----------------------------)

[FMFW.io

](/@fmfw-io?source=post_internal_links---------3----------------------------)

in

[FMFW.io

](https://medium.com/fmfw-io?source=post_internal_links---------
3----------------------------)

## SuperBid AMA summary

![](https://miro.medium.com/focal/112/112/50/50/1*U5NyjEFELi2pv8Q7fEWL8w.png)](/fmfw-
io/superbid-ama-summary-70cdc0096811?source=post_internal_links---------
3----------------------------)

[[![The
InstaNews](https://miro.medium.com/fit/c/40/40/0*tpWoqtVasAxMwKSF.jpg)](/@ffind.us?source=post_internal_links
---------4----------------------------)

[The InstaNews

](/@ffind.us?source=post_internal_links---------4----------------------------)

## Ming Nomchong — Photographer @ming_nomchong_photo(1 comments 72 likes)

![Ming Nomchong - Photographer @ming_nomchong_photo - Jan 26,
2017](https://miro.medium.com/focal/112/112/50/50/0*vWg5PZEE4e6lwgad.)](/@ffind.us/ming-
nomchong-photographer-ming-nomchong-photo-1-comments-72-likes-
fbd74222ac0c?source=post_internal_links---------4----------------------------)

[[![DarkMatter_CO](https://miro.medium.com/fit/c/40/40/1*7Se5ifEz9OTROGjYc4XF1Q.jpeg)](/@darkmatter-
co?source=post_internal_links---------5----------------------------)

[DarkMatter_CO

](/@darkmatter-co?source=post_internal_links---------
5----------------------------)

in

[Nebular

](https://medium.com/nebular?source=post_internal_links---------
5----------------------------)

## Demystifying Microstrategy and the Recent Bitcoin Bubble

![](https://miro.medium.com/focal/112/112/50/50/1*yVe8X8XxmYeKH_no5zKbaw.jpeg)](/nebular/demystifying-
microstrategy-and-the-recent-bitcoin-
bubble-9d5104d87584?source=post_internal_links---------
5----------------------------)

[[![ShrimpyApp](https://miro.medium.com/fit/c/40/40/2*v0m6JnbBbEhcvJTqRCGL5g.png)](/@shrimpyapp?source=post_internal_links
---------6----------------------------)

[ShrimpyApp

](/@shrimpyapp?source=post_internal_links---------
6----------------------------)

in

[Good Audience

](https://medium.com/good-audience?source=post_internal_links---------
6----------------------------)

## How Crypto Traders Can Turn Portfolio Losses Into Tax Savings

![](https://miro.medium.com/focal/112/112/50/50/1*mv7ll-
gFaMOq47kaoYq3rw.png)](/good-audience/how-crypto-traders-can-turn-portfolio-
losses-into-tax-savings-d7d8a4398280?source=post_internal_links---------
6----------------------------)

[[![Ling](https://miro.medium.com/fit/c/40/40/1*5nY4atOY4BpetqEi_lxUDA.jpeg)](/@m27102856?source=post_internal_links
---------7----------------------------)

[Ling

](/@m27102856?source=post_internal_links---------
7----------------------------)

## My fourth class of creative thinking

](/@m27102856/my-fourth-class-of-creative-
thinking-9a43df242b06?source=post_internal_links---------
7----------------------------)

[](/?source=post_page-----b7d59d2ff2c7--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
b7d59d2ff2c7--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
b7d59d2ff2c7--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
b7d59d2ff2c7--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
b7d59d2ff2c7--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----b7d59d2ff2c7--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----b7d59d2ff2c7--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fmuunwallet%2Fsave-
up-to-30-in-fees-with-muuns-new-mempool-based-
estimator-b7d59d2ff2c7&source=post_page--------------------------
nav_reg-----------)

[![Muun](https://miro.medium.com/fit/c/176/176/1*jqkB48eViAMK840DLgF5FA.png)](/@muunwallet)

[

## Muun

](/@muunwallet)

24 Followers

Your secure checking account for Bitcoin

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fusers%2Fcf8aef497b6a%2Flazily-enable-
writer-
subscription&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fmuunwallet%2Fsave-
up-to-30-in-fees-with-muuns-new-mempool-based-
estimator-b7d59d2ff2c7&user=Muun&userId=cf8aef497b6a&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Jonas
Wald](https://miro.medium.com/fit/c/40/40/1*Bc0McUjbZ2pptoEgiKIQ1Q.jpeg)](/@jwald575?source=read_next_recirc
---------0---------------------9466a3e6_42c8_4fc8_a654_907697917e1f-------)

[Jonas Wald

](/@jwald575?source=read_next_recirc---------0---------------------
9466a3e6_42c8_4fc8_a654_907697917e1f-------)

in

[Nerd For Tech

](https://medium.com/nerd-for-tech?source=read_next_recirc---------0
---------------------9466a3e6_42c8_4fc8_a654_907697917e1f-------)

## Cost to start a crypto exchange ~ How can it be minimized?

![](https://miro.medium.com/focal/112/112/50/50/1*_7m4_WlE0yoiiw8a9X2lTA.png)](/nerd-
for-tech/cost-to-start-a-crypto-exchange-how-can-it-be-minimized-
ac319f6560d2?source=read_next_recirc---------0---------------------
9466a3e6_42c8_4fc8_a654_907697917e1f-------)

[[![Eliteraccoons](https://miro.medium.com/fit/c/40/40/1*zD4xA0Ym_UjJNctGrDwF3g.png)](/@eliteraccoons?source=read_next_recirc
---------1---------------------9466a3e6_42c8_4fc8_a654_907697917e1f-------)

[Eliteraccoons

](/@eliteraccoons?source=read_next_recirc---------1---------------------
9466a3e6_42c8_4fc8_a654_907697917e1f-------)

## Elite Raccoons — manifest

![](https://miro.medium.com/focal/112/112/50/50/1*e9gnap3qDL33ekhzOyI8QA.png)](/@eliteraccoons/elite-
raccoons-manifest-22e5b5066b99?source=read_next_recirc---------1
---------------------9466a3e6_42c8_4fc8_a654_907697917e1f-------)

[[![Jim
Redsaint](https://miro.medium.com/fit/c/40/40/1*3-qv5J10DCCg7-dQqCKaiQ@2x.jpeg)](/@jimchimdi?source=read_next_recirc
---------2---------------------9466a3e6_42c8_4fc8_a654_907697917e1f-------)

[Jim Redsaint

](/@jimchimdi?source=read_next_recirc---------2---------------------
9466a3e6_42c8_4fc8_a654_907697917e1f-------)

## The community DAO is bracing the hospitality industry with Airbnb vacation
rentals on the…

![](https://miro.medium.com/focal/112/112/50/50/1*WoDtlmZgJYNWQioT6dk-
TQ@2x.jpeg)](/@jimchimdi/the-community-dao-is-bracing-the-hospitality-
industry-with-airbnb-vacation-rentals-on-the-
cf724db0c903?source=read_next_recirc---------2---------------------
9466a3e6_42c8_4fc8_a654_907697917e1f-------)

[[![HornHub.finance](https://miro.medium.com/fit/c/40/40/1*4px091qjm8-fl0VAU8I9LA.jpeg)](/@hornhub-
finance?source=read_next_recirc---------3---------------------
9466a3e6_42c8_4fc8_a654_907697917e1f-------)

[HornHub.finance

](/@hornhub-finance?source=read_next_recirc---------3---------------------
9466a3e6_42c8_4fc8_a654_907697917e1f-------)

## How HornHub is Building Towards the Perfect Crescendo

![](https://miro.medium.com/focal/112/112/50/50/1*0vu9l4mlnS_Dm14ZyW1YPA.jpeg)](/@hornhub-
finance/how-hornhub-is-building-towards-the-perfect-
crescendo-224acd85447d?source=read_next_recirc---------3---------------------
9466a3e6_42c8_4fc8_a654_907697917e1f-------)

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

