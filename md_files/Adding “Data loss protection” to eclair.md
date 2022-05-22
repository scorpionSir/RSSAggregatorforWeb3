[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/598c62494096&~feature=LoOpenInAppButton&~channel=ShowPostUnderUser&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![ACINQ](https://miro.medium.com/fit/c/96/96/1*C_yfYIhszWi885XNVFxnkg.png)](/@ACINQ?source=post_page
-----598c62494096--------------------------------)

[ACINQ](/@ACINQ?source=post_page-----
598c62494096--------------------------------)

Follow

Mar 8, 2018

·

2 min read

# Adding “Data loss protection” to eclair

Two weeks ago, [PR #410](https://github.com/ACINQ/eclair/pull/410) was merged
into eclair’s master branch. This pull request added support for “Data loss
protection”, one of the features we absolutely wanted to implement in eclair
before going on mainnet.

![](https://miro.medium.com/max/800/1*ukyaxTYrTUG2MJv4r-UCEg.jpeg)

Why is it such a big deal? **One of the tricky thing with Lightning is that
you cannot easily backup a channel**. Suppose you simply copy your node data,
and later restart from this now outdated state; then you may broadcast what
you _think_ is the current commitment, which is actually _a revoked_
commitment and you will be punished by your counterparty.

Data loss protection is an optional feature that was added to the Lightning
Network specifications [a few months
ago](https://github.com/lightningnetwork/lightning-
rfc/commit/046f5acb1619bccf167e5539f144433495f1486b). In a nutshell, it allows
parties to **provide additional data at reconnection** , in order to give
provable information on their counterparty’s current commitment number.

For example, if Alice and Bob have a channel open together and support this
feature, Bob will tell Alice: “you are at least at commitment number _N_ , and
here is the proof”. If Alice’s commitment number is _M_ with _M_ < _N_ , then
**(1) she knows that her data is stale and (2) she can ask Bob to broadcast
his current commitment** , which is really the only thing left to do when one
of the parties loses its data anyway.

Can Bob lie? Partly: he cannot invent a future commitment number, but he can,
for example, say “you are at commitment number _N_ ” when in fact Alice is at
commitment number _P_ with _P_ > _N_. However, Bob can never be sure that
Alice has lost her data or if she is just pretending, and attempting to cheat
on LN is a _very_ risky bet…

Another way to look at it: **in order to lose money, you would have to lose
your data _and_ have a dishonest counterparty _and_ they are willing to bet
all their money that you are telling the truth** when you say you lost your
data.

A third way to look at it: with only one old backup of your data, you’ll be
able to retrieve most of your funds, provided that your counterparty is honest
(or is not willing to bet that you are honest).

# What’s next?

The next important feature we are working on at the spec level is a [better
synchronization
mechanism](https://lists.linuxfoundation.org/pipermail/lightning-
dev/2018-February/000989.html). As the Lightning Network grows on testnet, the
need appeared for a more efficient way to exchange initial routing
information, particularly for mobile devices.

\--

3

\--

\--

3

## [More from ACINQ](/@ACINQ?source=post_page-----
598c62494096--------------------------------)

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fcb6983c5b91b&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ACINQ%2Fadding-
data-loss-protection-to-
eclair-598c62494096&newsletterV3=74c0a4fc8ad0&newsletterV3Id=cb6983c5b91b&user=ACINQ&userId=74c0a4fc8ad0&source=-----598c62494096
---------------------subscribe_user-----------)

We are building an implementation of Lightning, a scalable instant payment
network built on top of the Bitcoin blockchain.

Love podcasts or audiobooks? Learn on the go with our new app.

[Try
Knowable](https://knowable.fyi/?utm_source=medium&utm_medium=referral&utm_campaign=medium-
post-footer&source=post_page-----598c62494096--------------------------------)

[](/?source=post_page-----598c62494096--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
598c62494096--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
598c62494096--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
598c62494096--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
598c62494096--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----598c62494096--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----598c62494096--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ACINQ%2Fadding-
data-loss-protection-to-eclair-598c62494096&source=post_page
--------------------------nav_reg-----------)

[![ACINQ](https://miro.medium.com/fit/c/176/176/1*C_yfYIhszWi885XNVFxnkg.png)](/@ACINQ)

[

## ACINQ

](/@ACINQ)

1.1K Followers

We are building an implementation of Lightning, a scalable instant payment
network built on top of the Bitcoin blockchain.

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fcb6983c5b91b&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ACINQ%2Fadding-
data-loss-protection-to-
eclair-598c62494096&newsletterV3=74c0a4fc8ad0&newsletterV3Id=cb6983c5b91b&user=ACINQ&userId=74c0a4fc8ad0&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Safezonetoken](https://miro.medium.com/fit/c/40/40/1*Jw2SY1jK3_vremT3ncO4Gw@2x.jpeg)](/@safezonetoken?source=read_next_recirc
---------0---------------------0ce9eb5e_4625_44e2_bb9a_61ff7d1356f4-------)

[Safezonetoken

](/@safezonetoken?source=read_next_recirc---------0---------------------
0ce9eb5e_4625_44e2_bb9a_61ff7d1356f4-------)

## SAFE ZONE V2

![](https://miro.medium.com/focal/112/112/50/50/1*EPeqJGe5qD9qGwE8u8veug@2x.jpeg)](/@safezonetoken/safe-
zone-v2-dfb6c674d2f4?source=read_next_recirc---------0---------------------
0ce9eb5e_4625_44e2_bb9a_61ff7d1356f4-------)

[[![Thales
Tozatto](https://miro.medium.com/fit/c/40/40/1*5T-wWylXAs56bktZfAeGcg.jpeg)](/@ttozatto.ds?source=read_next_recirc
---------1---------------------0ce9eb5e_4625_44e2_bb9a_61ff7d1356f4-------)

[Thales Tozatto

](/@ttozatto.ds?source=read_next_recirc---------1---------------------
0ce9eb5e_4625_44e2_bb9a_61ff7d1356f4-------)

## Can we guess the best cryptos looking at Sharpe Ratio?

![](https://miro.medium.com/focal/112/112/50/50/1*nxOlCGWRL_OXYeZDb2citA.png)](/@ttozatto.ds/can-
we-guess-the-best-cryptos-looking-at-sharpe-
ratio-19cfc89a71a?source=read_next_recirc---------1---------------------
0ce9eb5e_4625_44e2_bb9a_61ff7d1356f4-------)

[[![Bajiute](https://miro.medium.com/fit/c/40/40/1*Ca3diiPZhzVdSirSbjpbKg.jpeg)](/@bajiute?source=read_next_recirc
---------2---------------------0ce9eb5e_4625_44e2_bb9a_61ff7d1356f4-------)

[Bajiute

](/@bajiute?source=read_next_recirc---------2---------------------
0ce9eb5e_4625_44e2_bb9a_61ff7d1356f4-------)

## “Bitcoin” is dead

![](https://miro.medium.com/focal/112/112/50/50/1*DTtLzCKJUsWbWZr7fZexPw.jpeg)](/@bajiute/bitcoin-
is-dead-a168f75f8182?source=read_next_recirc---------2---------------------
0ce9eb5e_4625_44e2_bb9a_61ff7d1356f4-------)

[[![THE PAST
PROJECT](https://miro.medium.com/fit/c/40/40/1*63Qo1-vHzbzdYtVkYCiHGQ.jpeg)](/@thepastproject?source=read_next_recirc
---------3---------------------0ce9eb5e_4625_44e2_bb9a_61ff7d1356f4-------)

[THE PAST PROJECT

](/@thepastproject?source=read_next_recirc---------3---------------------
0ce9eb5e_4625_44e2_bb9a_61ff7d1356f4-------)

## Lines of Effort for The $PAST Project

](/@thepastproject/lines-of-effort-for-the-past-
project-3cd5901e8d04?source=read_next_recirc---------3---------------------
0ce9eb5e_4625_44e2_bb9a_61ff7d1356f4-------)

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

