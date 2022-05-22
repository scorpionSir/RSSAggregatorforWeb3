[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/9f58dc3d8407&~feature=LoOpenInAppButton&~channel=ShowPostUnderUser&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![ACINQ](https://miro.medium.com/fit/c/96/96/1*C_yfYIhszWi885XNVFxnkg.png)](/@ACINQ?source=post_page
-----9f58dc3d8407--------------------------------)

[ACINQ](/@ACINQ?source=post_page-----
9f58dc3d8407--------------------------------)

Follow

Aug 16, 2018

·

3 min read

# Enabling automated backup on Eclair Wallet

 ** _TL; DR:_** _Latest release of Eclair Wallet Testnet includes automated
encrypted backups using Google Drive. Will be rolled out to mainnet ASAP._

![](https://miro.medium.com/max/800/1*-l1sogewTzlFw5XxmkHRCw.gif)

# A bit #Reckless until now

Until now, upon installing Eclair Wallet for Android, a huge scary disclaimer
warned users that funds allocated to Lightning channels weren’t being backed
up. In other words, funds stored in channels would be lost if the user
uninstalled the app, or even deleted application data, or simply lost their
phone with open channels (of course, on-chain funds are always protected by
the seed and can be recovered).

# Backing up Lightning channels is difficult

The reason for this is that backing up Lightning channels is far more complex
than backing up on-chain funds. On-chain is easy: everyone is used to writing
down a list of words once and for all. But there are two problems with the
backup of Lightning funds. First the backup needs to be updated every time the
state of the channel changes (which happens several times during a single
payment!). The second problem is even worse: if you restore channels from a
backup that you _think_ is up to date, but is actually an old stale state,
then your counterparty could believe you are attempting to cheat on them, and
take all your money as a punishment.

# How it works

We decided to use Google Drive to store channel backup data. It is updated
every time a channel’s state changes. Note that only the channel data is
saved, not the routing table which can be fetched from the network. To be more
precise, the data we store is encrypted using a key derived from the main
seed, and its name is also derived from this same seed. This allows users to
seamlessly restore their Eclair Wallet app, using only the 12 words they are
used to; it also supports having an unlimited number of different wallets
simultaneously, and restore one or the other.

We know that some may not like the fact that we rely on Google Drive (which
means having to create a Google account) for that — especially those who
install Eclair Wallet straight from our [GitHub
repo](https://github.com/ACINQ/eclair-wallet/releases) —, but this is both the
easiest and most convenient way we found to meet our needs for now, and there
is little privacy concern since everything is encrypted on-device. We should
add that it wouldn’t be too difficult to change the back-end in the future.

If for some reason you try to restore an outdated backup (this shouldn’t be
possible, but still), then you will still be fine, provided that your peer
supports [dataloss protection](/@ACINQ/adding-data-loss-protection-to-
eclair-598c62494096) (this is the case for Eclair and LND nodes, and soon for
c-lightning).

Given how sensitive this feature is, we are very interested in getting user
feedback before rolling out the mainnet version. Please [download the testnet
app](https://play.google.com/store/apps/details?id=fr.acinq.eclair.wallet),
and [report any bugs](https://github.com/ACINQ/eclair-wallet)!

\--

1

\--

\--

1

## [More from ACINQ](/@ACINQ?source=post_page-----
9f58dc3d8407--------------------------------)

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fcb6983c5b91b&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ACINQ%2Fenabling-
automated-backup-on-eclair-
wallet-9f58dc3d8407&newsletterV3=74c0a4fc8ad0&newsletterV3Id=cb6983c5b91b&user=ACINQ&userId=74c0a4fc8ad0&source=-----9f58dc3d8407
---------------------subscribe_user-----------)

We are building an implementation of Lightning, a scalable instant payment
network built on top of the Bitcoin blockchain.

Love podcasts or audiobooks? Learn on the go with our new app.

[Try
Knowable](https://knowable.fyi/?utm_source=medium&utm_medium=referral&utm_campaign=medium-
post-footer&source=post_page-----9f58dc3d8407--------------------------------)

[](/?source=post_page-----9f58dc3d8407--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
9f58dc3d8407--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
9f58dc3d8407--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
9f58dc3d8407--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
9f58dc3d8407--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----9f58dc3d8407--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----9f58dc3d8407--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ACINQ%2Fenabling-
automated-backup-on-eclair-wallet-9f58dc3d8407&source=post_page
--------------------------nav_reg-----------)

[![ACINQ](https://miro.medium.com/fit/c/176/176/1*C_yfYIhszWi885XNVFxnkg.png)](/@ACINQ)

[

## ACINQ

](/@ACINQ)

1.1K Followers

We are building an implementation of Lightning, a scalable instant payment
network built on top of the Bitcoin blockchain.

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fcb6983c5b91b&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ACINQ%2Fenabling-
automated-backup-on-eclair-
wallet-9f58dc3d8407&newsletterV3=74c0a4fc8ad0&newsletterV3Id=cb6983c5b91b&user=ACINQ&userId=74c0a4fc8ad0&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Liane Walker-
Meininger](https://miro.medium.com/fit/c/40/40/1*dmbNkD5D-u45r44go_cf0g.png)](/@liane_walker?source=read_next_recirc
---------0---------------------391c4c51_fd76_471d_b536_9bd3366620e2-------)

[Liane Walker-Meininger

](/@liane_walker?source=read_next_recirc---------0---------------------
391c4c51_fd76_471d_b536_9bd3366620e2-------)

## Part 2: Once upon a time there was Decentralized Finance (DeFi)…

![](https://miro.medium.com/focal/112/112/50/50/0*ecgDvNV0vynbJG10)](/@liane_walker/part-2-1-once-
upon-a-time-there-was-decentralized-finance-
defi-b53dc5446bad?source=read_next_recirc---------0---------------------
391c4c51_fd76_471d_b536_9bd3366620e2-------)

[[![Jason Payne](https://miro.medium.com/fit/c/40/40/1*JeMXu0tbwzgCTqJ-A-
Xb2w.jpeg)](/@xneo?source=read_next_recirc---------1---------------------
391c4c51_fd76_471d_b536_9bd3366620e2-------)

[Jason Payne

](/@xneo?source=read_next_recirc---------1---------------------
391c4c51_fd76_471d_b536_9bd3366620e2-------)

## Terra | UST | LUNA | An Opportunity for Wizards and Warriors of DeFi

![](https://miro.medium.com/focal/112/112/50/50/0*ngFRuqwsnNwln4Y6.jpg)](/@xneo/terra-
ust-luna-an-opportunity-for-wizards-and-warriors-of-
defi-3ead3d703221?source=read_next_recirc---------1---------------------
391c4c51_fd76_471d_b536_9bd3366620e2-------)

[[![ignatius
juniour](https://miro.medium.com/fit/c/40/40/1*Dpk19RtpdUDwARcaHwuykA.jpeg)](/@talktoignilitt?source=read_next_recirc
---------2---------------------391c4c51_fd76_471d_b536_9bd3366620e2-------)

[ignatius juniour

](/@talktoignilitt?source=read_next_recirc---------2---------------------
391c4c51_fd76_471d_b536_9bd3366620e2-------)

## 3 Most Vital Assets For The Duet Protocol.

![](https://miro.medium.com/focal/112/112/50/50/1*NydIqUssLuzwnKi3-X8VBg.png)](/@talktoignilitt/3-most-
vital-assets-for-the-duet-protocol-e1557e3b3596?source=read_next_recirc
---------2---------------------391c4c51_fd76_471d_b536_9bd3366620e2-------)

[[![Cryptool](https://miro.medium.com/fit/c/40/40/1*XXsGsGsqm34IVbqcSa-
PVw.jpeg)](/@cryptool?source=read_next_recirc---------3---------------------
391c4c51_fd76_471d_b536_9bd3366620e2-------)

[Cryptool

](/@cryptool?source=read_next_recirc---------3---------------------
391c4c51_fd76_471d_b536_9bd3366620e2-------)

## How is the NEAR algorithm stablecoin USN different from UST?

![](https://miro.medium.com/focal/112/112/50/50/1*nKuyKspn0hIjWHJGv3UCJw.png)](/@cryptool/how-
is-the-near-algorithm-stablecoin-usn-different-from-
ust-c06c3fd31e2e?source=read_next_recirc---------3---------------------
391c4c51_fd76_471d_b536_9bd3366620e2-------)

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

