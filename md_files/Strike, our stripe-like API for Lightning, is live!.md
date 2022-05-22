[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/cd1dce76ce2e&~feature=LoOpenInAppButton&~channel=ShowPostUnderUser&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![ACINQ](https://miro.medium.com/fit/c/96/96/1*C_yfYIhszWi885XNVFxnkg.png)](/@ACINQ?source=post_page
-----cd1dce76ce2e--------------------------------)

[ACINQ](/@ACINQ?source=post_page-----
cd1dce76ce2e--------------------------------)

Follow

May 24, 2018

·

3 min read

# Strike, our stripe-like API for Lightning, is live!

 **TL; DR:** We are releasing Strike, an API and dashboard that makes it easy
to accept Lightning payments on Bitcoin Mainnet. Fee is 1% and automated
withdrawals are free.

A few months ago we announced [Strike, an easy to use, stripe-like API for
Lightning](/@ACINQ/introducing-strike-a-stripe-like-api-for-
lightning-c84762f4f634). It was only available for Bitcoin testnet, and today
we open it on Bitcoin mainnet.

# Why an API for Lightning?

The Lightning Network is a high performance trustless payment network built on
top of the Bitcoin blockchain. It enables **instant payments with very low
fees, even for very small amounts**.

We are proud members of the Lightning development community, and we [have
released and are maintaining](https://github.com/ACINQ/eclair/releases) all
the open source tools that you need to run a Lightning node and “be your own
payment processor”. But we believe that some businesses may be interested in a
tradeoff where they get **most of the benefits of Lightning** , while keeping
their **integration costs as low as possible**. This is what Strike is about:
add Lightning payments to your business in no time and with as little impact
on your operations as possible.

With Strike, receiving Lightning payments will look very familiar to any web
developer: it boils down to making an API call and listening to a webhook
event.

![](https://miro.medium.com/max/1400/1*gTKB-XiwJrbUaxL0yg4jVA.gif)

How does it work? **We receive lightning payments on your behalf, aggregate
them and periodically send an on-chain bitcoin transaction** to your wallet.

In other words, you can offer instant and cheap payments to your customers,
and you still get paid with the good old on-chain Bitcoin transactions that
you are used to.

# Wait… doesn’t that make you a trusted 3rd party?

Yes, it does, but our service only requires a **minimum level of trust** ,
because we send you an on-chain Bitcoin transaction whenever the aggregate
amount reaches a configurable threshold.

For example, if you set your withdraw threshold to 0.1 BTC, then you will
never trust us for more than 0.1 BTC.

# Are there other benefits to using Strike?

In addition to making it easy to integrate Lightning payments to your checkout
process, Strike brings two additional benefits:

By using Strike, and because automated payouts are free, you completely
**shield yourself and your customers from on-chain fees** that are
unpredictable and subject to significant variations.

Because payments are aggregated, **your wallet ends up managing a smaller UTXO
set** with higher amounts, as opposed to a very high number of UTXOs with tiny
amount, that could be difficult to spend if on-chain fees go up in the future.

# How much will you charge for this service?

We take a **1% fee on payments, and that’s it**. Automated payouts to your
Bitcoin wallet are free of charge, because we batch them among merchants. The
threshold for automated withdrawals can be set between 0.1–1 BTC.

You can also trigger a withdrawal manually, but in that case there is an
additional fee of 0.5 mBTC.

# How do I get started?

Go to [https://strike.acinq.co](http://strike.acinq.co), create an
[account](https://strike.acinq.co/#/signup), read the
[doc](https://strike.acinq.co/#/documentation) and receive your first
payments!

We will be releasing a [WooCommerce](https://woocommerce.com/) plugin shortly,
and we are also looking at other options, such as Shopify.

## Interested? Want to know more?

Contact us at strike@acinq.co.

\--

1

\--

\--

1

## [More from ACINQ](/@ACINQ?source=post_page-----
cd1dce76ce2e--------------------------------)

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fcb6983c5b91b&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ACINQ%2Fstrike-
our-stripe-like-api-for-lightning-is-live-
cd1dce76ce2e&newsletterV3=74c0a4fc8ad0&newsletterV3Id=cb6983c5b91b&user=ACINQ&userId=74c0a4fc8ad0&source=-----cd1dce76ce2e
---------------------subscribe_user-----------)

We are building an implementation of Lightning, a scalable instant payment
network built on top of the Bitcoin blockchain.

Love podcasts or audiobooks? Learn on the go with our new app.

[Try
Knowable](https://knowable.fyi/?utm_source=medium&utm_medium=referral&utm_campaign=medium-
post-footer&source=post_page-----cd1dce76ce2e--------------------------------)

[](/?source=post_page-----cd1dce76ce2e--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
cd1dce76ce2e--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
cd1dce76ce2e--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
cd1dce76ce2e--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
cd1dce76ce2e--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----cd1dce76ce2e--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----cd1dce76ce2e--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ACINQ%2Fstrike-
our-stripe-like-api-for-lightning-is-live-cd1dce76ce2e&source=post_page
--------------------------nav_reg-----------)

[![ACINQ](https://miro.medium.com/fit/c/176/176/1*C_yfYIhszWi885XNVFxnkg.png)](/@ACINQ)

[

## ACINQ

](/@ACINQ)

1.1K Followers

We are building an implementation of Lightning, a scalable instant payment
network built on top of the Bitcoin blockchain.

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fcb6983c5b91b&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ACINQ%2Fstrike-
our-stripe-like-api-for-lightning-is-live-
cd1dce76ce2e&newsletterV3=74c0a4fc8ad0&newsletterV3Id=cb6983c5b91b&user=ACINQ&userId=74c0a4fc8ad0&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Thales
Tozatto](https://miro.medium.com/fit/c/40/40/1*5T-wWylXAs56bktZfAeGcg.jpeg)](/@ttozatto.ds?source=read_next_recirc
---------0---------------------34c8539f_d225_405f_ae4e_aa9e5a49ad68-------)

[Thales Tozatto

](/@ttozatto.ds?source=read_next_recirc---------0---------------------
34c8539f_d225_405f_ae4e_aa9e5a49ad68-------)

## Can we guess the best cryptos looking at Sharpe Ratio?

![](https://miro.medium.com/focal/112/112/50/50/1*nxOlCGWRL_OXYeZDb2citA.png)](/@ttozatto.ds/can-
we-guess-the-best-cryptos-looking-at-sharpe-
ratio-19cfc89a71a?source=read_next_recirc---------0---------------------
34c8539f_d225_405f_ae4e_aa9e5a49ad68-------)

[[![Oluebube
Nwosu](https://miro.medium.com/fit/c/40/40/1*a8dduyNn9I8wJJMvi-11Xg.jpeg)](/@meetoluebube?source=read_next_recirc
---------1---------------------34c8539f_d225_405f_ae4e_aa9e5a49ad68-------)

[Oluebube Nwosu

](/@meetoluebube?source=read_next_recirc---------1---------------------
34c8539f_d225_405f_ae4e_aa9e5a49ad68-------)

## How do blockchains agree on data publishing?

](/@meetoluebube/how-do-blockchains-agree-on-data-publishing-
dca4611e77a0?source=read_next_recirc---------1---------------------
34c8539f_d225_405f_ae4e_aa9e5a49ad68-------)

[[![Frank
Albanese](https://miro.medium.com/fit/c/40/40/0*2e_f_yMXZRop-Z1N)](/@albanesefc9?source=read_next_recirc
---------2---------------------34c8539f_d225_405f_ae4e_aa9e5a49ad68-------)

[Frank Albanese

](/@albanesefc9?source=read_next_recirc---------2---------------------
34c8539f_d225_405f_ae4e_aa9e5a49ad68-------)

in

[Coinmonks

](https://medium.com/coinmonks?source=read_next_recirc---------2
---------------------34c8539f_d225_405f_ae4e_aa9e5a49ad68-------)

## If Your Stacking Sats — You are Most Likely a Market Leader of the Next
Bullrun

![](https://miro.medium.com/focal/112/112/50/50/1*96GDlH6_kfqPvmrk4Hc3PA.png)](/coinmonks/if-
your-stacking-sats-you-are-most-likely-a-market-leader-of-the-next-
bullrun-5f0f0d3d41c5?source=read_next_recirc---------2---------------------
34c8539f_d225_405f_ae4e_aa9e5a49ad68-------)

[[![Innocent
Amarachi](https://miro.medium.com/fit/c/40/40/1*70t4Ai4U416pNsf0XmqPag.jpeg)](/@innocentamarachi20?source=read_next_recirc
---------3---------------------34c8539f_d225_405f_ae4e_aa9e5a49ad68-------)

[Innocent Amarachi

](/@innocentamarachi20?source=read_next_recirc---------3---------------------
34c8539f_d225_405f_ae4e_aa9e5a49ad68-------)

## Explaining Blockchain as if to a five year old

](/@innocentamarachi20/explaining-blockchain-as-if-to-a-five-year-
old-4bdaacfc1a2c?source=read_next_recirc---------3---------------------
34c8539f_d225_405f_ae4e_aa9e5a49ad68-------)

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

