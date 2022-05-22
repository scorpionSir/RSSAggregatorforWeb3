[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/fb1befd027c8&~feature=LoOpenInAppButton&~channel=ShowPostUnderUser&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![ACINQ](https://miro.medium.com/fit/c/96/96/1*C_yfYIhszWi885XNVFxnkg.png)](/@ACINQ?source=post_page
-----fb1befd027c8--------------------------------)

[ACINQ](/@ACINQ?source=post_page-----
fb1befd027c8--------------------------------)

Follow

Dec 15, 2019

·

4 min read

# Phoenix Wallet Part 4: Trampoline payments

 **TL; DR:** No delays when launching the app (network sync, route
calculation, etc). Open the app and pay instantly, as simple as that!

Let’s imagine that you’re using Lightning to pay for your morning coffee.
Every morning when you open your Lightning wallet, you need to sync network
updates. This consumes bandwidth, drains your battery and takes time. Then you
need to find a payment route to your coffee place’s Lightning node. This also
drains your battery and takes time. Meanwhile, customers are queuing behind
you, waiting to pay for their own coffee and wondering why this is taking
forever.

Phoenix uses [trampoline
payments](https://lists.linuxfoundation.org/pipermail/lightning-
dev/2019-March/001939.html) to get rid of these UX issues and provide faster
payments. With trampoline, your wallet doesn’t need to know every node in the
network. It only needs to know nodes that are close and some remote trampoline
nodes. As long as you can find a (short) route to a first trampoline node, you
can let that node calculate a route to the next one. And so on and so forth
until the payment reaches its destination. This allows the network to scale
without making it impractical to run a node on a phone. And of course,
**payments are still trustless**.

However, the trampoline specification is still a [work-in-
progress](https://github.com/lightningnetwork/lightning-rfc/pull/654). As a
result our node is the only one currently supporting it, which means that we
know the destination of payments, just like if you were using a custodial
wallet (but payments are trustless, which is _not_ the case with custodial
wallets). When you send a payment with Phoenix, here is what happens:

  * Phoenix looks at all of your channels, splits the payment accordingly and sends a multi-part trampoline payment to the ACINQ node.
  * The ACINQ node aggregates the incoming partial payments, unwraps the trampoline onion and forwards the payment to its final recipient.

Two things can happen when the ACINQ node forwards the payment:

  * The recipient is another Phoenix: this is business as usual, ACINQ forwards the payment or uses pay-to-open.
  * The recipient isn’t another Phoenix (and thus doesn’t support trampoline): ACINQ will find a route to that recipient and forward the payment “the old way”.

Let’s briefly talk about fees. Fee estimation is hard, because the ACINQ node
needs to be able to forward your payment to any node in the network and
collect a small fee for its route calculation work. At the moment, Phoenix
estimates the total fee to 10 times the routing fee applied by ACINQ (which is
1 sat + 0.01% of the amount sent). We will improve this by offering more
accurate fee estimation on the ACINQ node, along with a retry-by-raising-fee
mechanism in some failure cases.

EDIT: as of version 1.2.0, Phoenix starts with a low fee and then retries on
failures, raising the fee for each attempt. This results in much lower fees in
common cases.

And now for the most interesting part, the **privacy trade-offs**. As we said
before, ACINQ learns both the payer and recipient of those trampoline payments
(just like custodial wallets). We view this as a liability and we want to get
rid of it.

Today, trampoline payments work like this:

![](https://miro.medium.com/max/1400/1*KBBAwWwKVCAwKj0ykGig0Q.png)

Trampoline today — grey nodes are “legacy” routing nodes

Tomorrow, we want them to work like that:

![](https://miro.medium.com/max/1400/1*knut_Ow48VRygGRVWHdnbA.png)

Trampoline tomorrow — blue nodes are trampoline nodes, grey nodes are “legacy”
routing nodes. There may be more than two trampoline nodes, and any number of
“legacy” hops between trampoline nodes.

You can clearly see that with such a route, ACINQ doesn’t learn who the payer
or the recipient are: we get the same privacy as “normal” payments. Privacy on
the Lightning Network is a subtle, multi-layer problem though, and there is
still room for improvement. That’s why we’re actively contributing to the
specification to work towards that goal.

This vision only works if other people run Trampoline nodes. We believe that
will be the case because there’s a healthy incentive to run a trampoline node:
you contribute to the network by providing route calculation services for
wallets and receive extra fees for that. Everyone wins.

If you want to help with that ongoing effort, head over to [the
specification](https://github.com/lightningnetwork/lightning-rfc/pull/654) to
contribute!

This article is **part 4** of a series of articles introducing Phoenix. Other
articles in this series:

  * [Part 1: Introducing Phoenix](/@ACINQ/introducing-phoenix-5c5cc76c7f9e)
  * [Part 2: Pay-to-Open](/@ACINQ/phoenix-part-2-pay-to-open-4a8a482dd4d)
  * [Part 3: Backup](/@ACINQ/phoenix-wallet-part-3-backup-f63a9470d4e7)

 _Correction: An earlier version of this post said that Phoenix used a factor
of 5 to estimate the fee, it’s actually a factor of 10. Meaning that Phoenix
assumes that in the worst case scenario, the route will be 10 hops. This will
be deprecated by the retry-by-raising-fee mechanism, scheduled for january
2020._

\--

\--

\--

## [More from ACINQ](/@ACINQ?source=post_page-----
fb1befd027c8--------------------------------)

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fcb6983c5b91b&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ACINQ%2Fphoenix-
wallet-part-4-trampoline-payments-
fb1befd027c8&newsletterV3=74c0a4fc8ad0&newsletterV3Id=cb6983c5b91b&user=ACINQ&userId=74c0a4fc8ad0&source=-----fb1befd027c8
---------------------subscribe_user-----------)

We are building an implementation of Lightning, a scalable instant payment
network built on top of the Bitcoin blockchain.

Love podcasts or audiobooks? Learn on the go with our new app.

[Try
Knowable](https://knowable.fyi/?utm_source=medium&utm_medium=referral&utm_campaign=medium-
post-footer&source=post_page-----fb1befd027c8--------------------------------)

## Recommended from Medium

[[![Sun
Dery](https://miro.medium.com/fit/c/40/40/0*k4uoxYfv4UvPKvfb.jpg)](/@sund5429?source=post_internal_links
---------0----------------------------)

[Sun Dery

](/@sund5429?source=post_internal_links---------0----------------------------)

## Add Jaeger tracing to NGINX

![](https://miro.medium.com/focal/112/112/50/50/1*KmH2s6vJfIvoekpTZJtw4w.jpeg)](/@sund5429/add-
jaeger-tracing-to-nginx-7de1d731ee6e?source=post_internal_links---------
0----------------------------)

[[![Aleksei
Jegorov](https://miro.medium.com/fit/c/40/40/1*eIgcTwPqlVe2e0dhnOPaPg.jpeg)](/@alekseijegorov?source=post_internal_links
---------1----------------------------)

[Aleksei Jegorov

](/@alekseijegorov?source=post_internal_links---------
1----------------------------)

## Kotlin “use” keyword

![](https://miro.medium.com/focal/112/112/50/50/1*cgM3wCmuFV6OS8jvouGvMg.png)](/@alekseijegorov/kotlin-
use-keyword-31225f80b8c0?source=post_internal_links---------
1----------------------------)

[[![Donald Le](https://miro.medium.com/fit/c/40/40/2*hsi-
TpDaIKe94BmBED07rw.png)](/@ledinhcuong99?source=post_internal_links---------
2----------------------------)

[Donald Le

](/@ledinhcuong99?source=post_internal_links---------
2----------------------------)

in

[Automation with Love

](https://medium.com/automation-with-donald?source=post_internal_links
---------2----------------------------)

## Python fundamentals for automation test

![](https://miro.medium.com/focal/112/112/50/50/1*0jGn0Ng73T-CKJef1MgVRw.jpeg)](/automation-
with-donald/python-fundamentals-for-automation-
test-7444ba3f5ee?source=post_internal_links---------
2----------------------------)

[[![Eric
Miller](https://miro.medium.com/fit/c/40/40/0*Bq5cwdwUDYtHCyJu)](/@ericm-
moa?source=post_internal_links---------3----------------------------)

[Eric Miller

](/@ericm-moa?source=post_internal_links---------
3----------------------------)

## RMA’s Can Get Very Complicated

![](https://miro.medium.com/focal/112/112/50/50/1*8c-bdZHMBiAcCtqMrNlL9w.jpeg)](/@ericm-
moa/rmas-can-get-very-complicated-85aa85343fc9?source=post_internal_links
---------3----------------------------)

[[![Steven
Curtis](https://miro.medium.com/fit/c/40/40/1*ivmbg0Ef6mylufSXa9aLBw.jpeg)](/@stevenpcurtis?source=post_internal_links
---------4----------------------------)

[Steven Curtis

](/@stevenpcurtis?source=post_internal_links---------
4----------------------------)

in

[Swift Coding

](https://medium.com/swift-coding?source=post_internal_links---------
4----------------------------)

## Overriding in Swift

![](https://miro.medium.com/focal/112/112/50/50/1*oM9Ri-3ajPT-
rURwUV154g.png)](/swift-coding/overriding-in-
swift-f703b2091aa2?source=post_internal_links---------
4----------------------------)

[[![Nick
Lambert](https://miro.medium.com/fit/c/40/40/2*cOQGBCcvCEACP5m7-HmTWw.jpeg)](/@nick.lambert?source=post_internal_links
---------5----------------------------)

[Nick Lambert

](/@nick.lambert?source=post_internal_links---------
5----------------------------)

## Dock release Northill test net

![](https://miro.medium.com/focal/112/112/50/50/1*M6FoDLjjMf1XcXtLI1RJ0Q.jpeg)](/@nick.lambert/dock-
release-northill-test-net-4cb4c1c9ef4c?source=post_internal_links---------
5----------------------------)

[[![Jnie](https://miro.medium.com/fit/c/40/40/1*JxXeFN6CVAsO30NDQ04Cow.jpeg)](/@jniec?source=post_internal_links
---------6----------------------------)

[Jnie

](/@jniec?source=post_internal_links---------6----------------------------)

in

[Entropyfi

](https://medium.com/entropyfi?source=post_internal_links---------
6----------------------------)

## When the Prediction Market is Lossless

![](https://miro.medium.com/focal/112/112/50/50/1*FzJ_sKjsZciD-
yW2ek-r8Q.png)](/entropyfi/when-the-prediction-market-is-
lossless-8a46336a0fb?source=post_internal_links---------
6----------------------------)

[[![Shan
Desai](https://miro.medium.com/fit/c/40/40/2*AeimQROh4J5Ak1dA868b_g.jpeg)](/@shantanoodesai?source=post_internal_links
---------7----------------------------)

[Shan Desai

](/@shantanoodesai?source=post_internal_links---------
7----------------------------)

## Nugget: User Management in MQTT Mosquitto Broker with Docker

](/@shantanoodesai/nugget-user-management-in-mqtt-mosquitto-broker-with-
docker-77c39153c921?source=post_internal_links---------
7----------------------------)

[](/?source=post_page-----fb1befd027c8--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
fb1befd027c8--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
fb1befd027c8--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
fb1befd027c8--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
fb1befd027c8--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----fb1befd027c8--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----fb1befd027c8--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ACINQ%2Fphoenix-
wallet-part-4-trampoline-payments-fb1befd027c8&source=post_page
--------------------------nav_reg-----------)

[![ACINQ](https://miro.medium.com/fit/c/176/176/1*C_yfYIhszWi885XNVFxnkg.png)](/@ACINQ)

[

## ACINQ

](/@ACINQ)

1.1K Followers

We are building an implementation of Lightning, a scalable instant payment
network built on top of the Bitcoin blockchain.

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fcb6983c5b91b&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ACINQ%2Fphoenix-
wallet-part-4-trampoline-payments-
fb1befd027c8&newsletterV3=74c0a4fc8ad0&newsletterV3Id=cb6983c5b91b&user=ACINQ&userId=74c0a4fc8ad0&source=--------------------------subscribe_user-----------)

## More from Medium

[[![GreenTea_Pasta](https://miro.medium.com/fit/c/40/40/1*LOKXzQ12btpyNUOK5xKF3w.png)](/@0xGreenTea_Pasta?source=read_next_recirc
---------0---------------------f2be0908_6ec5_4a91_a924_b00ec2ac8692-------)

[GreenTea_Pasta

](/@0xGreenTea_Pasta?source=read_next_recirc---------0---------------------
f2be0908_6ec5_4a91_a924_b00ec2ac8692-------)

## UST <> BTC Forex Reserve Pool

![](https://miro.medium.com/focal/112/112/50/50/1*Ry_rLYqNbV82bt3MxvQWAg.png)](/@0xGreenTea_Pasta/ust-
btc-forex-reserve-pool-3d6c1fd37f73?source=read_next_recirc---------0
---------------------f2be0908_6ec5_4a91_a924_b00ec2ac8692-------)

[[![Silvermint](https://miro.medium.com/fit/c/40/40/1*5cLh1Eip2o45_olxBwv3VA.jpeg)](/@silvermint_45700?source=read_next_recirc
---------1---------------------f2be0908_6ec5_4a91_a924_b00ec2ac8692-------)

[Silvermint

](/@silvermint_45700?source=read_next_recirc---------1---------------------
f2be0908_6ec5_4a91_a924_b00ec2ac8692-------)

in

[Silvermint News

](https://medium.com/silvermint-news?source=read_next_recirc---------1
---------------------f2be0908_6ec5_4a91_a924_b00ec2ac8692-------)

## Calls from All the Strangest Places

![](https://miro.medium.com/focal/112/112/50/50/1*pkKZ8F5kXpQrsBvd0-A5uQ.jpeg)](/silvermint-
news/calls-from-all-the-strangest-places-c9cd4ff97750?source=read_next_recirc
---------1---------------------f2be0908_6ec5_4a91_a924_b00ec2ac8692-------)

[[![Santiago](https://miro.medium.com/fit/c/40/40/1*u6KZYS1-N3D12sf7f5zfrQ.jpeg)](/@santi_a_gogo?source=read_next_recirc
---------2---------------------f2be0908_6ec5_4a91_a924_b00ec2ac8692-------)

[Santiago

](/@santi_a_gogo?source=read_next_recirc---------2---------------------
f2be0908_6ec5_4a91_a924_b00ec2ac8692-------)

## "Bitcoin is evil" and the dangers of satanizing technology

![](https://miro.medium.com/focal/112/112/50/50/1*qane7ZeTej-
Rd9BWlHjeWg.png)](/@santi_a_gogo/bitcoin-is-evil-and-the-dangers-of-
satanizing-technology-1cd6a8f72b27?source=read_next_recirc---------2
---------------------f2be0908_6ec5_4a91_a924_b00ec2ac8692-------)

[[![Drew
Seewald](https://miro.medium.com/fit/c/40/40/1*QVYjh50XJuOLQBeH_RZoGw.jpeg)](/@realdrewdata?source=read_next_recirc
---------3---------------------f2be0908_6ec5_4a91_a924_b00ec2ac8692-------)

[Drew Seewald

](/@realdrewdata?source=read_next_recirc---------3---------------------
f2be0908_6ec5_4a91_a924_b00ec2ac8692-------)

## Crypto Evangelists Hate Me For This One Simple Reason

![The Ethereum diamond logo surrounded by clouds reflected on
water](https://miro.medium.com/focal/112/112/50/50/0*cOhFs_Gr3Ug5lCRY)](/@realdrewdata/crypto-
evangelists-hate-me-for-this-one-simple-
reason-a4aa41e004f8?source=read_next_recirc---------3---------------------
f2be0908_6ec5_4a91_a924_b00ec2ac8692-------)

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

