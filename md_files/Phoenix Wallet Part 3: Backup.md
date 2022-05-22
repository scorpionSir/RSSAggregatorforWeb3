[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/f63a9470d4e7&~feature=LoOpenInAppButton&~channel=ShowPostUnderUser&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![ACINQ](https://miro.medium.com/fit/c/96/96/1*C_yfYIhszWi885XNVFxnkg.png)](/@ACINQ?source=post_page
-----f63a9470d4e7--------------------------------)

[ACINQ](/@ACINQ?source=post_page-----
f63a9470d4e7--------------------------------)

Follow

Dec 12, 2019

·

3 min read

# Phoenix Wallet Part 3: Backup

 **TL; DR:** Each time channels are updated, Phoenix sends an encrypted
version of their data to its peer. This allows for easy backup/restore of
channels while maintaining privacy.

On a traditional Bitcoin wallet, backup is as simple as writing down a list of
words, once and for all. It is not as simple with Lightning because backups
need to be updated after each transaction. It’s also very tricky because from
a protocol point of view, restoring an out-of-date backup is the same as a
cheating attempt, and will result in your peer taking all your funds.

For Eclair Mobile, we came up with the idea to use Google Drive as a remote
backup system, by uploading an encrypted version of the channel data every
time they were updated. It worked well enough and the feature was later
replicated by a few other Lightning wallets, but it also required a dependency
(and an account) to a external service provider (Google). We wanted to do
better.

The idea of _static backups_ has been floating around for some time now, but
they are not a silver bullet and suffer from two main drawbacks:

  * You need to remember what peers you have a channel with, meaning that you need to make a backup every time you create a channel. It’s an improvement, but it’s still not as good as doing a backup once and for all.
  * Restoring a channel will close it. It costs you money and takes time.

 **Our idea with Phoenix is, on top of static backups, to make our peer store
a backup of our channels for us**. This immediately raises two questions: (1)
how would I know who my former peers were when I need to restore my wallet and
(2) why would my former peer cooperate and help me restore my funds.

Phoenix’s answer for (1) is easy enough: the peer is always ACINQ. That kind
of simplification is one of the advantages behind the choice to always connect
to the same nodes.

Now regarding (2), ACINQ needs an incentive to cooperate. In the case of
Phoenix:

  * ACINQ is always the funder, with a non-zero reserve, which means that ACINQ always has something at stake. From there, in order to recover its funds, ACINQ has two choices: either force-close(*), which means paying high fees (funder pays the commitment fees in unilateral close scenarii as per the LN protocol), or help users recover their channels, which could lead to earning future routing fees.
  * Just like the `data_loss_protect` feature of the LN protocol, ACINQ doesn’t have a way to tell the difference between a recovery scenario and a normal reconnection. When reconnecting and exchanging commitment number about existing channels, ACINQ will _always_ return the last encrypted channel data. We actually plan to go one step further and make ACINQ always send its data _first_ , preventing it from gaining any information — true or false — from Phoenix beforehand. This is an example of shifting the trust balance in favour of Phoenix.

(*) Note that if ACINQ chooses to force-close, Phoenix would still recover its
money thanks to _static backups_.

To summarise, if you (a Phoenix user) lose your data (uninstall app, lose
phone, …), just reinstall the app with the same seed, and you will instantly
recover your channels and be ready to make payments. We have demonstrated this
use case in our [preview
video](https://twitter.com/acinq_co/status/1185129586482388992).

This article is **part 3** of a series of articles introducing Phoenix. Other
articles in this series:

  * [Part 1: Introducing Phoenix](/@ACINQ/introducing-phoenix-5c5cc76c7f9e)
  * [Part 2: Pay-to-Open](/@ACINQ/phoenix-part-2-pay-to-open-4a8a482dd4d)
  * [Part 4: Trampoline payments](/@ACINQ/phoenix-wallet-part-4-trampoline-payments-fb1befd027c8)

\--

\--

\--

## [More from ACINQ](/@ACINQ?source=post_page-----
f63a9470d4e7--------------------------------)

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fcb6983c5b91b&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ACINQ%2Fphoenix-
wallet-
part-3-backup-f63a9470d4e7&newsletterV3=74c0a4fc8ad0&newsletterV3Id=cb6983c5b91b&user=ACINQ&userId=74c0a4fc8ad0&source=-----f63a9470d4e7
---------------------subscribe_user-----------)

We are building an implementation of Lightning, a scalable instant payment
network built on top of the Bitcoin blockchain.

Love podcasts or audiobooks? Learn on the go with our new app.

[Try
Knowable](https://knowable.fyi/?utm_source=medium&utm_medium=referral&utm_campaign=medium-
post-footer&source=post_page-----f63a9470d4e7--------------------------------)

[](/?source=post_page-----f63a9470d4e7--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
f63a9470d4e7--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
f63a9470d4e7--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
f63a9470d4e7--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
f63a9470d4e7--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----f63a9470d4e7--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----f63a9470d4e7--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ACINQ%2Fphoenix-
wallet-part-3-backup-f63a9470d4e7&source=post_page--------------------------
nav_reg-----------)

[![ACINQ](https://miro.medium.com/fit/c/176/176/1*C_yfYIhszWi885XNVFxnkg.png)](/@ACINQ)

[

## ACINQ

](/@ACINQ)

1.1K Followers

We are building an implementation of Lightning, a scalable instant payment
network built on top of the Bitcoin blockchain.

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fcb6983c5b91b&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ACINQ%2Fphoenix-
wallet-
part-3-backup-f63a9470d4e7&newsletterV3=74c0a4fc8ad0&newsletterV3Id=cb6983c5b91b&user=ACINQ&userId=74c0a4fc8ad0&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Tobi 'Jeezman'
Adeyemi](https://miro.medium.com/fit/c/40/40/1*gDSZYolOngbE2RAqb0fRdg.jpeg)](/@tobiadeyemi?source=read_next_recirc
---------0---------------------36c601db_043e_4752_af00_af1b3e92736c-------)

[Tobi 'Jeezman' Adeyemi

](/@tobiadeyemi?source=read_next_recirc---------0---------------------
36c601db_043e_4752_af00_af1b3e92736c-------)

## Understand Lightning Liquidity

![](https://miro.medium.com/focal/112/112/50/50/1*G6Tsw6kBA4bfhImDwwT-
yw.jpeg)](/@tobiadeyemi/understand-lightning-liquidity-
ef4dd91e8ed2?source=read_next_recirc---------0---------------------
36c601db_043e_4752_af00_af1b3e92736c-------)

[[![Cryptool](https://miro.medium.com/fit/c/40/40/1*XXsGsGsqm34IVbqcSa-
PVw.jpeg)](/@cryptool?source=read_next_recirc---------1---------------------
36c601db_043e_4752_af00_af1b3e92736c-------)

[Cryptool

](/@cryptool?source=read_next_recirc---------1---------------------
36c601db_043e_4752_af00_af1b3e92736c-------)

## How is the NEAR algorithm stablecoin USN different from UST?

![](https://miro.medium.com/focal/112/112/50/50/1*nKuyKspn0hIjWHJGv3UCJw.png)](/@cryptool/how-
is-the-near-algorithm-stablecoin-usn-different-from-
ust-c06c3fd31e2e?source=read_next_recirc---------1---------------------
36c601db_043e_4752_af00_af1b3e92736c-------)

[[![IAmThatOmer∞](https://miro.medium.com/fit/c/40/40/0*oFRWopcuu0JB1ZpE.)](/@IAmThatOmer?source=read_next_recirc
---------2---------------------36c601db_043e_4752_af00_af1b3e92736c-------)

[IAmThatOmer∞

](/@IAmThatOmer?source=read_next_recirc---------2---------------------
36c601db_043e_4752_af00_af1b3e92736c-------)

in

[blindex.io

](https://medium.com/blindex-io?source=read_next_recirc---------2
---------------------36c601db_043e_4752_af00_af1b3e92736c-------)

## Why Stablecoins Are Essential For The Cryptocurrency Ecosystem?

![](https://miro.medium.com/focal/112/112/50/50/1*XYGGnvWIw_2gNZQbHs2Cbg.jpeg)](/blindex-
io/why-stablecoins-are-essential-for-the-cryptocurrency-
ecosystem-3c6c199bc212?source=read_next_recirc---------2---------------------
36c601db_043e_4752_af00_af1b3e92736c-------)

[[![BitKong](https://miro.medium.com/fit/c/40/40/1*7vkpVmWbnwNXWfDM2eof8w.png)](/@bitkong?source=read_next_recirc
---------3---------------------36c601db_043e_4752_af00_af1b3e92736c-------)

[BitKong

](/@bitkong?source=read_next_recirc---------3---------------------
36c601db_043e_4752_af00_af1b3e92736c-------)

## Stablecoins: A Bridge Between TradFi and DeFi

![](https://miro.medium.com/focal/112/112/50/50/1*CoRpzZIaSVO4sHa34lBhfA@2x.png)](/@bitkong/stablecoins-
a-bridge-between-tradfi-and-defi-4bbdf18e7340?source=read_next_recirc---------
3---------------------36c601db_043e_4752_af00_af1b3e92736c-------)

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

