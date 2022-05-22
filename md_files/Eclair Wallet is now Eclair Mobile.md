[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/e4d7eb2019a3&~feature=LoOpenInAppButton&~channel=ShowPostUnderUser&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![ACINQ](https://miro.medium.com/fit/c/96/96/1*C_yfYIhszWi885XNVFxnkg.png)](/@ACINQ?source=post_page
-----e4d7eb2019a3--------------------------------)

[ACINQ](/@ACINQ?source=post_page-----
e4d7eb2019a3--------------------------------)

Follow

Jan 4, 2019

·

4 min read

# Eclair Wallet is now Eclair Mobile

 **TL; DR:** Eclair Wallet is now Eclair Mobile, with background routing sync
and custom Electrum server support. Reception of funds over Lightning will be
enabled in 2019.

![](https://miro.medium.com/max/1400/1*1S5VillMKVqoXWD52qtDMg.jpeg)

We decided to rename Eclair Wallet to Eclair Mobile because the former name
was too generic and regularly caused confusion among our users. Hopefully it
will be clearer now:

  * [ **Eclair**](https://github.com/ACINQ/eclair) is a full LN node implementation, it is intended to run on a desktop or server. It is the software that powers the [ACINQ node](https://acinq.co/node), one of the oldest, most reliable and most connected nodes in the network.
  * [ **Eclair Mobile**](https://github.com/ACINQ/eclair-mobile) is a Bitcoin & Lightning mobile wallet for Android.

Here are a few things you should know about Eclair Mobile.

## Eclair Mobile is a Lightning node

It runs an actual stripped-down Lightning node on your smartphone, which is
derived from and shares ~90% of the code of Eclair. **It is not a remote
control to some Lightning node or API hosted by us** : your funds stay on your
device.

Note that Eclair Mobile only opens private/unannounced LN channels, that’s why
your node and your channels won’t appear on any explorers.

Eclair Mobile relies on Electrum servers for accessing the Bitcoin blockchain.
Until now it connected to a set of predefined servers, but **latest version
support selecting a custom Electrum server of your choice**. This way you can
point to your own Electrum server and not trust anyone. Note that when using
that feature, Eclair Mobile will always use SSL and expects a valid
certificate.

## Eclair Mobile is also a regular off-chain Bitcoin wallet

You can perfectly use Eclair Mobile as a simple, segwit-ready Bitcoin Wallet
without even using Lightning. Most of the features commonly found in a Bitcoin
wallet are supported.

It is **particularly easy to select the right fee when sending an on-chain
payment** : you can choose a precomputed fast/medium/slow fee or set a custom
one, and **we will soon add replace-by-fee support** , to allow you to easily
modify the fee of an unconfirmed transaction. This gives you full control, and
it will be useful in the future when fees rise again (they will!).

## Eclair Mobile computes payment routes on-device

It is well known that LN preserves the trustless and censorship resistant
properties of Bitcoin, and even adds significant privacy guarantees on top of
it. But **most of these are lost if you delegate the route calculation to a
third party** : it defeats the purpose of onion routing and make your payments
trivially censorable.

That’s why we have put a lot of effort into optimizing the way routing table
is synced in the LN protocol, to ensure that lighter nodes don’t get left
behind as the network grows and bring the full benefit of LN to our users.

With the latest release, **Eclair Mobile now has a low footprint background
sync mechanism for its routing table**. This means that when you start the
wallet, it will be immediately ready to use.

And now for the most awaited question…

# When will you enable receiving LN payments?

You may know that Eclair Mobile currently only allows _sending_ money over
Lightning, not _receiving._ We made this choice for several reasons:

  * For mobile users, the #1 use case for Lightning is to send payments. Being able to do with Bitcoin what you would do with your credit card is already a great achievement ;
  * It is far safer, because it saves us from monitoring the blockchain, which is difficult to do reliably, especially on mobile devices. In fact, you can turn off your phone for an unlimited period of time, even with funds in open channels and you will be perfectly safe ;
  * Inbound liquidity is necessary to receive funds, it is tricky to explain, and the protocol was missing some crucial parts to make it seamless for inexperienced users. By going too fast too early, we would have spent a considerable amount of time providing support to users who couldn’t receive money right after having opened a channel (while all the money is on their side). Dual funding and liquidity advertisement (discussed during the Lightning Summit last Nov and scheduled for LN 1.1) will finally bring the tools allowing us to address this at scale and in a reasonably user-friendly way.

In short, only allowing sending money was the safest choice, while bringing
most of the benefits that LN could offer during its first year on mainnet. We
believe that the upcoming evolutions of the protocol **will allow us to enable
receive-over-LN in Eclair Mobile in 2019**.

Finally, developing a mobile Lightning wallet is no easy task, and it is very
rewarding to receive feedback from our users from all over the world, in
[Switzerland,](https://twitter.com/hillotweet/status/1043077697126232065)
[Brazil,](https://twitter.com/ricardoreis007/status/1046482231043215366?s=12)
[Australia](https://twitter.com/danielalexiuc/status/993667149238435840),
[Germany](https://twitter.com/leblitzdick/status/1050845952788099072),
[China](https://twitter.com/BeijingMeetup/status/1067345417669496832)… Thank
you all and a Happy New Year!

\--

1

\--

\--

1

## [More from ACINQ](/@ACINQ?source=post_page-----
e4d7eb2019a3--------------------------------)

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fcb6983c5b91b&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ACINQ%2Feclair-
wallet-is-now-eclair-
mobile-e4d7eb2019a3&newsletterV3=74c0a4fc8ad0&newsletterV3Id=cb6983c5b91b&user=ACINQ&userId=74c0a4fc8ad0&source=-----e4d7eb2019a3
---------------------subscribe_user-----------)

We are building an implementation of Lightning, a scalable instant payment
network built on top of the Bitcoin blockchain.

Love podcasts or audiobooks? Learn on the go with our new app.

[Try
Knowable](https://knowable.fyi/?utm_source=medium&utm_medium=referral&utm_campaign=medium-
post-footer&source=post_page-----e4d7eb2019a3--------------------------------)

## Recommended from Medium

[[![Crypto
Doyle](https://miro.medium.com/fit/c/40/40/1*iXKJsbFwiLYY_99aIOU9ww.jpeg)](/@eric-11919?source=post_internal_links
---------0----------------------------)

[Crypto Doyle

](/@eric-11919?source=post_internal_links---------
0----------------------------)

in

[Roxe Inc.

](https://medium.com/roxepaymentnetwork?source=post_internal_links---------
0----------------------------)

## Webinar: The Future of International Payments

![](https://miro.medium.com/focal/112/112/50/50/1*uVjXSVK2EwIfCFbUaVT8nA.jpeg)](/roxepaymentnetwork/webinar-
the-future-of-international-payments-fd3b0e039157?source=post_internal_links
---------0----------------------------)

[[![Mobula](https://miro.medium.com/fit/c/40/40/1*DjZPeq4uhxF49vDFHf8G4A.jpeg)](/@mobula?source=post_internal_links
---------1----------------------------)

[Mobula

](/@mobula?source=post_internal_links---------1----------------------------)

## Introduction to Mobula

![](https://miro.medium.com/focal/112/112/50/50/1*Z1ug99iLTZUlLkCijSKnhA.png)](/@mobula/introduction-
to-mobula-2088cf11914?source=post_internal_links---------
1----------------------------)

[[![Pedro Gonçalo
Ferreira](https://miro.medium.com/fit/c/40/40/0*cr69MfqoTnFHLIF-.)](/@pedrogoncaloferreira?source=post_internal_links
---------2----------------------------)

[Pedro Gonçalo Ferreira

](/@pedrogoncaloferreira?source=post_internal_links---------
2----------------------------)

in

[FrankfurtValley

](https://medium.com/frankfurtvalley?source=post_internal_links---------
2----------------------------)

## Iconic Funds’ Physical Bitcoin ETP Listing on Deutsche Börse’s Xetra

![](https://miro.medium.com/focal/112/112/50/50/1*A1UCJNeOj_lUVZrXN35Dsg.jpeg)](/frankfurtvalley/iconic-
funds-physical-bitcoin-etp-listing-on-deutsche-börse-s-
xetra-2fde7e797a94?source=post_internal_links---------
2----------------------------)

[[![Nigeria Bitcoin
Community](https://miro.medium.com/fit/c/40/40/1*8gtthAD2GdhZ1kBv3ByYLQ.jpeg)](/@infonigeriabitcoincommunity?source=post_internal_links
---------3----------------------------)

[Nigeria Bitcoin Community

](/@infonigeriabitcoincommunity?source=post_internal_links---------
3----------------------------)

in

[The Capital

](https://medium.com/the-capital?source=post_internal_links---------
3----------------------------)

## Coinomi Review: How to Store All Cryptos in one App for Free (2019 Update)

![](https://miro.medium.com/focal/112/112/50/50/0*ies_wr3sGmt_2Rl8)](/the-
capital/coinomi-review-how-to-store-all-cryptos-in-one-app-for-
free-2019-update-edde8902ba65?source=post_internal_links---------
3----------------------------)

[[![GoCrypto](https://miro.medium.com/fit/c/40/40/2*y57v2JQKIGgBEbJRkzAvWQ@2x.png)](/@eligmacompany?source=post_internal_links
---------4----------------------------)

[GoCrypto

](/@eligmacompany?source=post_internal_links---------
4----------------------------)

in

[GoCrypto Blog

](https://medium.com/eligma-blog?source=post_internal_links---------
4----------------------------)

## 2021 starts big. Eligma raises a new 4 million EUR equity investment at a
50 million EUR valuation

![](https://miro.medium.com/focal/112/112/50/50/1*9xMJPRHjia3QnGQcf0mxDA.png)](/eligma-
blog/2021-starts-big-eligma-raises-a-new-4-million-eur-equity-investment-
at-a-50-million-eur-valuation-74ffb1f3bbd3?source=post_internal_links---------
4----------------------------)

[[![M H
Ali](https://miro.medium.com/fit/c/40/40/1*0ubkDn_rCzRcgqON2QCYmQ.jpeg)](/@mhali9381?source=post_internal_links
---------5----------------------------)

[M H Ali

](/@mhali9381?source=post_internal_links---------
5----------------------------)

## 🔥 Get💰Reward: 10,000 Metawar- $50 instant distribution

![](https://miro.medium.com/focal/112/112/50/50/1*2eclWM3OUYrbP4DsdXe97g.jpeg)](/@mhali9381/get-
reward-10-000-metawar-50-instant-
distribution-d2e0c038f71e?source=post_internal_links---------
5----------------------------)

[[![STEX.com](https://miro.medium.com/fit/c/40/40/2*burpmq5dQTvsxtgDRpwV_A.png)](/@stex-
com?source=post_internal_links---------6----------------------------)

[STEX.com

](/@stex-com?source=post_internal_links---------6----------------------------)

## STEX Announces Free DeFi Listing on its Global Cryptocurrency Exchange

![](https://miro.medium.com/focal/112/112/50/50/1*L4KsFkYmmruWYxjACvJdLw.png)](/@stex-
com/stex-announces-free-defi-listing-on-its-global-cryptocurrency-
exchange-7cc00ce0d779?source=post_internal_links---------
6----------------------------)

[[![XT.com](https://miro.medium.com/fit/c/40/40/2*-b2UqXn8fCFR6pK8NOxNWg.jpeg)](/@XT_com?source=post_internal_links
---------7----------------------------)

[XT.com

](/@XT_com?source=post_internal_links---------7----------------------------)

## XT Will Hold SHIBACASH Trading Competition

![](https://miro.medium.com/focal/112/112/50/50/1*ZthOLLjkCZp2bPas5R82Ww.png)](/@XT_com/xt-
will-hold-shibacash-trading-
competition-4114afc241a4?source=post_internal_links---------
7----------------------------)

[](/?source=post_page-----e4d7eb2019a3--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
e4d7eb2019a3--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
e4d7eb2019a3--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
e4d7eb2019a3--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
e4d7eb2019a3--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----e4d7eb2019a3--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----e4d7eb2019a3--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ACINQ%2Feclair-
wallet-is-now-eclair-mobile-e4d7eb2019a3&source=post_page
--------------------------nav_reg-----------)

[![ACINQ](https://miro.medium.com/fit/c/176/176/1*C_yfYIhszWi885XNVFxnkg.png)](/@ACINQ)

[

## ACINQ

](/@ACINQ)

1.1K Followers

We are building an implementation of Lightning, a scalable instant payment
network built on top of the Bitcoin blockchain.

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fcb6983c5b91b&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ACINQ%2Feclair-
wallet-is-now-eclair-
mobile-e4d7eb2019a3&newsletterV3=74c0a4fc8ad0&newsletterV3Id=cb6983c5b91b&user=ACINQ&userId=74c0a4fc8ad0&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Jacob
Wilson](https://miro.medium.com/fit/c/40/40/0*j0C8oCmJWNKBYluY.jpg)](/@Jacobwilsonmr?source=read_next_recirc
---------0---------------------adad1c76_9097_49b8_803e_7b333415b423-------)

[Jacob Wilson

](/@Jacobwilsonmr?source=read_next_recirc---------0---------------------
adad1c76_9097_49b8_803e_7b333415b423-------)

## Crypto Markets are highly volatile and needs exclusive expertise to trade
crypto assets and new…

](/@Jacobwilsonmr/crypto-markets-are-highly-volatile-and-needs-exclusive-
expertise-to-trade-crypto-assets-and-new-4cd57343c7e?source=read_next_recirc
---------0---------------------adad1c76_9097_49b8_803e_7b333415b423-------)

[[![Sylant](https://miro.medium.com/fit/c/40/40/1*zGyqYdg3g-mTQcs21foEiw.png)](/@investorsylant?source=read_next_recirc
---------1---------------------adad1c76_9097_49b8_803e_7b333415b423-------)

[Sylant

](/@investorsylant?source=read_next_recirc---------1---------------------
adad1c76_9097_49b8_803e_7b333415b423-------)

## upCRO, the new upToken by Rootkit

![](https://miro.medium.com/focal/112/112/50/50/1*rCo26CMjiuTYhhjvbe7KDQ.png)](/@investorsylant/upcro-
the-new-uptoken-by-rootkit-70b443f0b43e?source=read_next_recirc---------1
---------------------adad1c76_9097_49b8_803e_7b333415b423-------)

[[![goldhaxx](https://miro.medium.com/fit/c/40/40/1*YW3Jz79WYwlWyoIQoBs2jA.png)](/@goldhaxx?source=read_next_recirc
---------2---------------------adad1c76_9097_49b8_803e_7b333415b423-------)

[goldhaxx

](/@goldhaxx?source=read_next_recirc---------2---------------------
adad1c76_9097_49b8_803e_7b333415b423-------)

## InvictusDAO: Should I buy bonds?

![](https://miro.medium.com/focal/112/112/50/50/1*VYBmeJSLBsHDdEPmyMuTyw.png)](/@goldhaxx/invictusdao-
should-i-buy-bonds-cb49301925bf?source=read_next_recirc---------2
---------------------adad1c76_9097_49b8_803e_7b333415b423-------)

[[![Bixin](https://miro.medium.com/fit/c/40/40/1*yO43dKz4InZzdB2SKHMhHg.jpeg)](/@Bixin?source=read_next_recirc
---------3---------------------adad1c76_9097_49b8_803e_7b333415b423-------)

[Bixin

](/@Bixin?source=read_next_recirc---------3---------------------
adad1c76_9097_49b8_803e_7b333415b423-------)

## Florida Lawsuit Could Finally Unmask Satoshi Nakamoto — The Mysterious $60+
Billion Father Of…

![](https://miro.medium.com/focal/112/112/50/50/1*gwxgZ_4Hu_nsAD1VtxCDUw.png)](/@Bixin/florida-
lawsuit-could-finally-unmask-satoshi-nakamoto-the-mysterious-60-billion-
father-of-31aa4f7007b4?source=read_next_recirc---------3---------------------
adad1c76_9097_49b8_803e_7b333415b423-------)

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

