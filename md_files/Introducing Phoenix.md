[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/5c5cc76c7f9e&~feature=LoOpenInAppButton&~channel=ShowPostUnderUser&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![ACINQ](https://miro.medium.com/fit/c/96/96/1*C_yfYIhszWi885XNVFxnkg.png)](/@ACINQ?source=post_page
-----5c5cc76c7f9e--------------------------------)

[ACINQ](/@ACINQ?source=post_page-----
5c5cc76c7f9e--------------------------------)

Follow

Dec 12, 2019

·

7 min read

# Introducing Phoenix

 **TL; DR:** Phoenix is a non-custodial Lightning Wallet that offers the same
UX as a good old Bitcoin wallet.

Today we are releasing Phoenix, a 2nd-generation mobile Lightning Wallet.

# Why do you call it a 2nd-generation wallet?

When we first announced [Eclair Mobile](/@ACINQ/announcing-eclair-
wallet-a8d8c136fc7e) back in 2017, we chose to make it a standard Bitcoin
wallet with opt-in Lightning support. Eclair Mobile has a pretty UI, but the
UX still lets you see a lot of the inner workings of Lightning. For example,
users see separate on-chain and off-chain balances, have to manage channels,
incoming liquidity, and so on.

With Phoenix, we started again from scratch — hence the name. **UX is
basically that of a good old bitcoin wallet, but with instant and cheap
payments**.

No more channel management, no more liquidity issues, no more backup
headaches! UX improvements are so significant that it deserved to be in a
class of its own.

# “Same UX as a Bitcoin wallet”. Really?

Let’s review a typical use case for a Bitcoin wallet, before Lightning
existed.

  1. Install a new wallet app
  2. Receive 0.004 BTC
  3. Send 0.001 BTC
  4. Receive 0.003 BTC
  5. Uninstall & Restore
  6. Send the remaining 0.006 BTC and end up with an empty wallet

This is seemingly very simple, and indeed this is trivial with a legacy
Bitcoin wallet, but is utterly difficult to achieve with Lightning. Here are
all the hurdles to overcome:

Step 1) is easy. Or is it really? On a traditional Bitcoin wallet this is
where you would write down your seed. You can’t do that with Lightning because
backups need to be updated after each transaction. There are attempts at
_static backups_ , but those have edge cases and won’t cover in-flight
payments.

Step 2) gets worse. You can’t receive funds over Lightning if you don’t have a
channel. But you need bitcoins to open a channel right? So you can’t receive
bitcoins if you don’t already have bitcoins. Quite annoying.

Step 3) is straightforward on a standard Bitcoin wallet. Even if the incoming
transaction made in 2) isn’t yet confirmed, you can spend it right away and
create a chain of unconfirmed transactions. But on Lightning you can’t,
because a channel needs to be confirmed to be usable. So if you created a
channel in 2), you will have to wait typically 2 or 3 confirmations before you
can make a payment.

Step 4): same as 2).

Step 5) at best, if your Lightning wallet supports _static backups_ of some
sort, you will be able to close your channels and retrieve your funds on-
chain. But it is going to cost you network fees, and you won’t be on Lightning
anymore.

Step 6) here the user sends out all her remaining funds in one transaction.
Note that, in this particular example, that would be the sum of two UTXOs
(0.003 BTC + 0.003 BTC). Let’s suppose that you created two channels in steps
2) and 4), then until very recently you wouldn’t have been able to combine
them in a single payment. Another thing: in Lightning, both sides of a channel
have to maintain a minimum “reserve” amount, as part of the incentive
mechanism. This can quickly turn into an UX nightmare because a) you can’t
spend _all_ your funds, and b) the unspendable amount depends on the number of
underlying channels. Phew!

The good news is, we solved all those challenges one by one. Here is what the
use case looks like, with Phoenix (100% on Lightning!):

Lightning made easy

There is no magic, of course, and achieving this required a combination of new
features and trade-offs.

# Features

Phoenix is packed with new features. We will detail some of them in other blog
posts:

  *  _Pay-to-open_. Phoenix will automatically create a channel on-the-fly if you don’t have enough inbound liquidity to receive a payment.
  *  _Spend-unconfirmed_. Also known as turbo channels. Allows you to use channels as soon as they are created, without having to wait for confirmations.
  *  _Peer backup_. No more headaches with channels backup. Just reinstall the app, enter your 12 words, and your money will be there.
  *  _Zero-reserve_ \+ _AMP_. This allows you to spend your money as one single balance, even if internally it is spread over multiple channels.
  *  _Trampoline payments._ Trustlessly delegate payment route computation, saving you from lengthy routing table sync. There is a privacy gotcha in the current version of Phoenix, detailed below.
  *  _Swaps_. Send and receive on-chain transactions seamlessly, even if you are on Lightning.

# Trade-offs

There are quite a few Lightning wallets out there, and we learnt during the
past 12 months that a good number of users are ready to use a hosted wallet,
because they feel that’s the only way to have a good UX.

We believe that we can have both: a non-custodial wallet with a good UX. This
was our starting point and we didn’t compromise on that. Phoenix, just like
Eclair Mobile, is a non-custodial Lightning wallet. It is based on Eclair and
runs a real Lightning node under the hood. **** The **keys never leave the
wallet and you would still be in full control of your funds if ACINQ
disappeared overnight** , or even the whole Lightning Network for that matter.

That was the non-negotiable part. Now here are the trade-offs that we made:

## Trust trade-offs

  *  **Phoenix only connects to ACINQ nodes**. This allows us to modify/enrich the Lightning protocol at the immediate peer level, while staying 100% LN compliant at the network level. It also makes it possible to have asymmetrical incentives, sometimes in favour of the user’s node, sometimes in favour of our node. Here are a few examples:

Example #1: A trivial example is the ability to open large channels.

Example #2: Because we trust our ability to detect cheating attempts, we
decided to not require a channel reserve from Phoenix users (we still have to
maintain one on our side). This is an example of asymmetrical incentives:
Phoenix users may be in a situation where they have nothing at stake (so a
cheating attempt would cost them nothing), while our node always has something
at stake. Having a zero reserve means that you can spend all your balance, and
makes multi-parts payments seamless because your total balance is simply the
sum of all your funds in all your channels, as you would expect.

Example #3: Because we know that the route to a Phoenix wallet will always go
through our node, we can offer additional services, like automatically offer
to open a new channel when receiving payments if the user has no channels or
not enough inbound liquidity.

  *  **Channel funding is trusted, until confirmed** , a bit like trusting an unconfirmed incoming transaction on a bitcoin wallet. Note that the way Phoenix works, all channels are always funded by our node, with a non-zero pushed amount, following an inbound layer 1 or layer 2 payment. We could have used a more advanced construct to make the funding tx depend on a `payment_preimage`, but that would also have required a delay (otherwise we would still be able to double-spend the tx) and would have prevented turbo channels. On the other hand, Phoenix users can’t fund channels themselves, because they don’t have UTXOs, and we wouldn’t trust them to not double spend their channels anyway.
  *  **Swaps are trusted** (basically we get paid and then we make the swap). Submarine (“trustless”) swaps are a thing, but they are not perfect. First they are not 100% trustless: for a swap-out you still need to trust the swap server with your prepayment. They are also more complex and require two on-chain transactions, making them more expensive. Last but not least, in the swap-out scenario, they require the receiving wallet to understand the swap protocol. You wouldn’t be able to directly send bitcoin from Phoenix to a normal bitcoin wallet.

So, yes there is some level of trust involved, for a limited number of
operations, and for a limited, well defined amount of time.Those are trade-
offs that we believe are worth making when UX is at stake.

It’s also worth noting that requiring trust, even for limited operations, is
never the best option for us. It’s a liability, and if we find ways to reduce
the level of trust we will do it.

## Privacy trade-offs

 **Information about payments (destination, amount) currently leaks to our
node**. To put it another way, Phoenix in its current version offers no
privacy benefit over a traditional hosted wallet. Why is that? Phoenix relies
on [trampoline](https://lists.linuxfoundation.org/pipermail/lightning-
dev/2019-March/001939.html) to outsource the computation of payment routes and
the specification of this new tech is still a [work-in-
progress](https://github.com/lightningnetwork/lightning-rfc/pull/654). As a
result our node is the only one currently supporting trampoline, hence the
privacy issue.

That’s obviously not satisfactory, and **it only makes sense as a temporary
measure** , the goal being to have a multitude of trampoline nodes (*), which
would result in a similar (actually, arguably better) level of privacy as non-
trampoline LN payments. Why would people run trampoline nodes you ask? Because
it allows them to earn more fees. Trampoline creates a new market for payment
route calculation, but that’s a topic for another day.

In the meantime, we plan to have Phoenix always connect over Tor (*), à la
[Blockstream Green,](https://bitcoinmagazine.com/articles/blockstream-green-
wallet-adds-early-access-tor-integration) which would significantly alleviate
the issue.

(*) Which is actually another trade-off in itself, depending on where you
live.

# When iOS?

For now Phoenix is Android-only, but we are working on an iOS version for
2020.

# What about Eclair Mobile?

Phoenix isn’t a replacement for Eclair Mobile, it operates with different
assumptions and targets different users. We intend to keep supporting Eclair
Mobile for the foreseeable future.

This article is **part 1** of a series of articles introducing Phoenix. Other
articles in this series:

  * [Part 2: Pay-to-Open](/@ACINQ/phoenix-part-2-pay-to-open-4a8a482dd4d)
  * [Part 3: Backup](/@ACINQ/phoenix-wallet-part-3-backup-f63a9470d4e7)
  * [Part 4: Trampoline payments](/@ACINQ/phoenix-wallet-part-4-trampoline-payments-fb1befd027c8)

\--

2

\--

\--

2

## [More from ACINQ](/@ACINQ?source=post_page-----
5c5cc76c7f9e--------------------------------)

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fcb6983c5b91b&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ACINQ%2Fintroducing-
phoenix-5c5cc76c7f9e&newsletterV3=74c0a4fc8ad0&newsletterV3Id=cb6983c5b91b&user=ACINQ&userId=74c0a4fc8ad0&source=-----5c5cc76c7f9e
---------------------subscribe_user-----------)

We are building an implementation of Lightning, a scalable instant payment
network built on top of the Bitcoin blockchain.

Love podcasts or audiobooks? Learn on the go with our new app.

[Try
Knowable](https://knowable.fyi/?utm_source=medium&utm_medium=referral&utm_campaign=medium-
post-footer&source=post_page-----5c5cc76c7f9e--------------------------------)

## Recommended from Medium

[[![STEX.com](https://miro.medium.com/fit/c/40/40/2*burpmq5dQTvsxtgDRpwV_A.png)](/@stex-
com?source=post_internal_links---------0----------------------------)

[STEX.com

](/@stex-com?source=post_internal_links---------0----------------------------)

## STEX.com Founder Proposes International Registry of Verified Identities
Solution unveiled at…

![](https://miro.medium.com/focal/112/112/50/50/1*GnINcPF4tz1rLsQo2beFXg.jpeg)](/@stex-
com/stex-com-founder-proposes-international-registry-of-verified-identities-
solution-unveiled-at-e642407b59f8?source=post_internal_links---------
0----------------------------)

[[![Rachit
S](https://miro.medium.com/fit/c/40/40/0*jxVr0PP-O86FsiG2)](/@rachit.srivastava_863?source=post_internal_links
---------1----------------------------)

[Rachit S

](/@rachit.srivastava_863?source=post_internal_links---------
1----------------------------)

## Building a Defi Token Development Like Safemoon

![](https://miro.medium.com/focal/112/112/50/50/1*Dj_qTvRK8bXRmKla1yQRZg.png)](/@rachit.srivastava_863/building-
a-defi-token-development-like-safemoon-ade9fc4de28f?source=post_internal_links
---------1----------------------------)

[[![Moses Mee
Essien](https://miro.medium.com/fit/c/40/40/1*PHLhthVc_r1FaqUbvfhTwQ.jpeg)](/@mosesmeeessien?source=post_internal_links
---------2----------------------------)

[Moses Mee Essien

](/@mosesmeeessien?source=post_internal_links---------
2----------------------------)

## REVIEW OF 2021 F0R COMDEX

![](https://miro.medium.com/freeze/focal/112/112/50/50/1*L6dtQJ0YpRqqnQj9SOsS0w.gif)](/@mosesmeeessien/review-
of-2021-f0r-comdex-c7cc7ea10bae?source=post_internal_links---------
2----------------------------)

[[![Daniel Tal](https://miro.medium.com/fit/c/40/40/1*dZsODbLhEW9WY-
Qz3fOOFg.jpeg)](/@dhtal?source=post_internal_links---------
3----------------------------)

[Daniel Tal

](/@dhtal?source=post_internal_links---------3----------------------------)

## ICHI Weekly Review — Week 19 (May 3–9, 2021)

![](https://miro.medium.com/focal/112/112/50/50/0*UU9Wgsn9qZZ7h-vz)](/@dhtal/ichi-
weekly-review-week-19-may-3-9-2021-a01cd25c71c?source=post_internal_links
---------3----------------------------)

[[![KR1
plc](https://miro.medium.com/fit/c/40/40/2*7dAZclChrm3_0372rhOIFQ.png)](/@kr1?source=post_internal_links
---------4----------------------------)

[KR1 plc

](/@kr1?source=post_internal_links---------4----------------------------)

## KR1 March update 💫

![](https://miro.medium.com/focal/112/112/50/50/1*IgIFMLgDnSRswR770vrUqg.png)](/@kr1/kr1-march-
update-89d2804bd26a?source=post_internal_links---------
4----------------------------)

[[![Cryptonic](https://miro.medium.com/fit/c/40/40/1*L-2vhYLzy34o02fEfPrpIQ.jpeg)](/@cryptonic21?source=post_internal_links
---------5----------------------------)

[Cryptonic

](/@cryptonic21?source=post_internal_links---------
5----------------------------)

## DigiCol Review

![](https://miro.medium.com/focal/112/112/50/50/1*xoNijOa0cDaE9qjUnxBGPQ@2x.jpeg)](/@cryptonic21/digicol-
review-5870325b05a9?source=post_internal_links---------
5----------------------------)

[[![Blake
Richardson](https://miro.medium.com/fit/c/40/40/2*ba0oN7RMINL8i4J7y7Zmvw.png)](/@blake_richardson?source=post_internal_links
---------6----------------------------)

[Blake Richardson

](/@blake_richardson?source=post_internal_links---------
6----------------------------)

## The Fragility of Early Systems

![](https://miro.medium.com/focal/112/112/50/50/1*qgT5EXy1hNkE_6RyX17mqg.jpeg)](/@blake_richardson/the-
fragility-of-early-systems-4a555d6c9f53?source=post_internal_links---------
6----------------------------)

[[![BountyBase](https://miro.medium.com/fit/c/40/40/1*QAKkJe4TrgcN2VqP3kLwFg@2x.jpeg)](/@BountyBase?source=post_internal_links
---------7----------------------------)

[BountyBase

](/@BountyBase?source=post_internal_links---------
7----------------------------)

in

[Buying.com

](https://medium.com/buying-com?source=post_internal_links---------
7----------------------------)

## Buying.com 2021 First Half Recap

![](https://miro.medium.com/focal/112/112/50/50/0*nf1ic-SiRyNeXSgw)](/buying-
com/buying-com-2021-first-half-recap-72f0f66e32a5?source=post_internal_links
---------7----------------------------)

[](/?source=post_page-----5c5cc76c7f9e--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
5c5cc76c7f9e--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
5c5cc76c7f9e--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
5c5cc76c7f9e--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
5c5cc76c7f9e--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----5c5cc76c7f9e--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----5c5cc76c7f9e--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ACINQ%2Fintroducing-
phoenix-5c5cc76c7f9e&source=post_page--------------------------
nav_reg-----------)

[![ACINQ](https://miro.medium.com/fit/c/176/176/1*C_yfYIhszWi885XNVFxnkg.png)](/@ACINQ)

[

## ACINQ

](/@ACINQ)

1.1K Followers

We are building an implementation of Lightning, a scalable instant payment
network built on top of the Bitcoin blockchain.

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fcb6983c5b91b&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ACINQ%2Fintroducing-
phoenix-5c5cc76c7f9e&newsletterV3=74c0a4fc8ad0&newsletterV3Id=cb6983c5b91b&user=ACINQ&userId=74c0a4fc8ad0&source=--------------------------subscribe_user-----------)

## More from Medium

[[![GJ
Flannery](https://miro.medium.com/fit/c/40/40/1*TYZPiKmnS6YxUI_WJChMtg.jpeg)](/@gjflannery?source=read_next_recirc
---------0---------------------a56fa2fb_cb02_4c0e_8665_3174c728c57a-------)

[GJ Flannery

](/@gjflannery?source=read_next_recirc---------0---------------------
a56fa2fb_cb02_4c0e_8665_3174c728c57a-------)

## Bitcoin & The Environment, Pt. 1: Why China (Still) Matters

![](https://miro.medium.com/focal/112/112/50/50/1*ev7YJgMahmV_bm72rc7plA.jpeg)](/@gjflannery/bitcoin-
the-environment-pt-1-why-china-still-
matters-3e825d9d65c9?source=read_next_recirc---------0---------------------
a56fa2fb_cb02_4c0e_8665_3174c728c57a-------)

[[![Cybertheticproject](https://miro.medium.com/fit/c/40/40/0*TzgXcFZ1gmTQdeq8)](/@cybertheticproject?source=read_next_recirc
---------1---------------------a56fa2fb_cb02_4c0e_8665_3174c728c57a-------)

[Cybertheticproject

](/@cybertheticproject?source=read_next_recirc---------1---------------------
a56fa2fb_cb02_4c0e_8665_3174c728c57a-------)

## What does the death of the luna token mean for the future of the Terra
blockchain?

![](https://miro.medium.com/focal/112/112/50/50/1*ob6zrsYLDUevQ_PoLDfWRw.png)](/@cybertheticproject/what-
does-the-death-of-the-luna-token-mean-for-the-future-of-the-terra-
blockchain-8c3c2c6081d3?source=read_next_recirc---------1---------------------
a56fa2fb_cb02_4c0e_8665_3174c728c57a-------)

[[![Christopher
Cesario](https://miro.medium.com/fit/c/40/40/0*LyMci_3s_qOq8uQD.jpg)](/@chris-
ces?source=read_next_recirc---------2---------------------
a56fa2fb_cb02_4c0e_8665_3174c728c57a-------)

[Christopher Cesario

](/@chris-ces?source=read_next_recirc---------2---------------------
a56fa2fb_cb02_4c0e_8665_3174c728c57a-------)

## What BlockFi’s Regulation Really Means for DeFi

![](https://miro.medium.com/focal/112/112/50/50/1*wt_U4DZsQiAK9eJSg8_ONg.jpeg)](/@chris-
ces/what-blockfis-regulation-really-means-for-
defi-2a093467a20c?source=read_next_recirc---------2---------------------
a56fa2fb_cb02_4c0e_8665_3174c728c57a-------)

[[![Sunny
Jiang](https://miro.medium.com/fit/c/40/40/0*I10cpSeYz780NQRg)](/@sunnymaas.eth?source=read_next_recirc
---------3---------------------a56fa2fb_cb02_4c0e_8665_3174c728c57a-------)

[Sunny Jiang

](/@sunnymaas.eth?source=read_next_recirc---------3---------------------
a56fa2fb_cb02_4c0e_8665_3174c728c57a-------)

## When stablecoin is not stable — learning from Terra UST/LUNA Collapsion

![](https://miro.medium.com/focal/112/112/50/50/1*cIVU37FVtioMK0SMhvwKHQ.png)](/@sunnymaas.eth/when-
stablecoin-is-not-stable-learning-from-terra-ust-luna-
collapsion-a72bc4da724d?source=read_next_recirc---------3---------------------
a56fa2fb_cb02_4c0e_8665_3174c728c57a-------)

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

