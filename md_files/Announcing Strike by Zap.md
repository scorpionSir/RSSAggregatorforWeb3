[](https://medium.com/)

[Get unlimited access](https://medium.com/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/4f578c7c8984&~feature=LoOpenInAppButton&~channel=ShowPostUnderUser&~stage=mobileNavBar)

[](https://medium.com/)

[Home](https://medium.com/)

[Notifications](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Jack
Mallers](https://miro.medium.com/fit/c/96/96/1*LMTxg8uEKM958_Dv1oG-2w.jpeg)](/?source=post_page
-----4f578c7c8984--------------------------------)

[Jack Mallers](/?source=post_page-----
4f578c7c8984--------------------------------)

Follow

Jan 30, 2020

·

11 min read

# Announcing Strike by Zap

Yo. Today I am thrilled, excited, and incredibly proud to release Zap’s most
ambitious product to date. The direct result of years of Bitcoin + Lightning
development, countless hours of user research, and intense product iteration
all led to this.

Today, we are announcing Strike, an application that allows you to make
Lightning payments with your bank account or debit card. Using Strike requires
the following: a debit card or bank account. That’s it; no wallet, no node, no
channels, no swaps, no liquidity management, no anything. It’s an application,
sitting on top of our infrastructure piece Olympus, designed to usher in an
era of Bitcoin that we believe has the best shot of achieving our mainstream
hopes and desires.

# The Story

When describing Zap’s design and product decisions, I’ve frequently described
Zap as **available in response**.

Back in September of 2019,[ I announced
Olympus](https://medium.com/@JimmyMow/announcing-olympus-lightning-enabled-
fiat-ramps-by-zap-1f5349a96ee9). Olympus was initially designed as a
Lightning-enabled fiat ramp, to allow users to buy bitcoin inside of their
existing Zap wallet. It was our answer to how we scale Lightning to millions
of users. However, as we tested, tinkered, tried, failed, and most importantly
learned, our product evolved. Those four months of intense user research and
study inspired the in-house hackathon that birthed Strike. Strike was never
the goal or the plan, but rather a **response**.

Our ideas and assumptions were simple. If we allowed users to instantly buy
BTC, delivered over Lightning by using a debit card linked to their Lightning
wallet, we would have it solved.

Right? Wrong. As we continued to experiment, we learned very quickly that we
were providing the right answer to the wrong question. In my Olympus
announcement, I proposed that Olympus solved the following question: How do we
get a user onto Lightning with the least amount of friction? However, what
Olympus solved was how to get _bitcoin_ onto Lightning with the least
friction. We completely missed the _user._

So for this blog post, I wanted to walk through our journey and learnings, and
introduce our new product and all we have in store for the future. This blog
post may be a bit longer than my typical post, but I believe the learnings
from our research and the outcome that is Strike is monumental and
transformative.

So, without further ado, let’s take a deep dive exploring the tremendous
amount of friction involved in getting a user onto Lightning, and the
important points that I missed.

# Volatility

The first very clear issue was bitcoin’s inherent volatility. Traditionally,
bitcoin’s volatility has been seen as a feature. In markets, volatility
screams opportunity, and it is bitcoin’s volatility (traditionally to the
upside) that has attracted many of its existing users and market participants.
One of the more popular value propositions of Bitcoin in its first 11 years of
existence is wealth creation. Buying bitcoin, holding bitcoin, and having its
value and purchasing power go up as time goes on.

However, in a consumer-merchant setting where people are _using_ bitcoin,
volatility is a non-starter. Frequently when testing, users would buy bitcoin
delivered over Lightning to their Zap wallet, and shortly after price would
move. We ran into a scenario with users where the bitcoin price fluctuated up
or down 5% after the initial purchase. This caused the following:

 _Not spending BTC because it’s appreciating_

or

 _Not spending BTC at a loss because of hopes it would appreciate_

Merchants have an entirely different relationship with volatility which makes
accepting bitcoin extremely difficult. A typical merchant prices their
operations in their denominated fiat currency. A volatile day for bitcoin
could throw away months of profit for a given merchant, and the risk-reward
profile just wasn’t worth it.

# Taxes

In the United States, bitcoin is taxed as property, and spending bitcoin in
exchange for any good, service, or currency is a taxable event, plain and
simple. Many do not know, but this extends to the Lightning Network and every
single Lightning Network payment. Yes, purchase of your Fold and Bitrefill
gift cards, your Yalls articles, and your Satoshis Place art are all taxable
events that need to be reported to the IRS.

This was a major oversight when designing Olympus. All activity was a taxable
event, and this created enormous amounts of overhead for each individual user
and for myself. Yes, sats back is nice, but is it worth capital gains tax
headaches? In our user research and testing, the answer was no. Users enjoyed
micropayments, cross border payments, social tipping, and so on, but did not
evaluate it as worth it when taking into account the tax consequences.

As a merchant, this was arguably a bigger issue. Merchants were accepting
bitcoin via Lightning, and every now and then converting to fiat to pay
operational expenses. The tax headache was not worth it, and nearly all
merchants opted out of accepting bitcoin.

The regulatory and tax scene in the United States is a huge impediment to
allowing Lightning to be used in mainstream commerce. Imagining a world where
millions of people are using Lightning to conduct commerce dies with the
introduction of the regulatory and tax scene currently in place. It was a
devastating truth to stumble upon, but one that is very much real.

## Creating A Wallet, Custody, and Owning Bitcoin

Many of our testers were not as familiar with Bitcoin as many reading this
post. If we want millions of mainstream consumers benefiting from Bitcoin and
Lightning, surely we should test with that audience in mind.

When asking a given user if they would buy an article for a few pennies, the
answer was almost always yes. However, when they were told it required
installing a Lightning wallet and buying bitcoin, their answer was no thanks.

> I have a few pennies in USD. If that’s not enough for the article, then I
> don’t care to buy it.

Direct quote.

Setting up a wallet, waiting for something you don’t understand to finish
syncing, being limited in your ability by something called “capacity,” and
having to buy bitcoin and manage backups was far too much for almost all
users. Many of our testers didn’t even get to the point of purchase, it was
all a bit overwhelming. That hit me hard. Ok, I get it, volatility and taxes
are tough. But you don’t even want to own bitcoin? For fuck’s sake, how am I
supposed to allow you to benefit from this technology?

If we look at my Olympus demo, we can see I owned zero bitcoin, and my goal
was to pay a Bitrefill QR code.

Did I really need to download a Lightning wallet, write down my seed phrase,
back up my channels, and be exposed to tax consequences and volatility to pay
the Bitrefill Lightning invoice? I wasn’t using bitcoin to speculate, and I
wasn’t using bitcoin for censorship resistance or privacy (as my identity and
debit card was linked to my node).

What if my debit card could pay the Lightning invoice? What if by connecting
my bank account, I can scan any Lightning invoice, hit pay, and it would work?
No wallet, no backups, no channels, no capacity, no custody issues, no
volatility, no taxes. What if instead of “spend and replace” it was “buy and
spend in seconds without noticing”? What if the few pennies in USD from the
above user _was_ enough? What would that look like?

It would look like Strike, that’s what it would look like.

# The Product

In order to accomplish this, a debit card or a bank account would need to be
interoperable with Bitcoin and the Lightning Network, lowering the barrier of
entry into this new economy. Users wouldn’t have to deal with volatility, they
wouldn’t have to deal with taxes, they wouldn’t need to set up a wallet to
interact with the protocols, and they wouldn’t even need to own bitcoin to
scan a Lightning QR code. What if everyone’s bank account could speak Bitcoin?

The jump from Olympus to Strike is quite small, we simply added a few things
and removed a few things. Small, simple, totally ordinary and innocuous
things.

However, because of the way we are able to integrate them into the
environment, they have this decisive impact and become extremely powerful. We
aren’t just changing how Bitcoin looks, but also how it feels. We’re changing
a consumer’s relationship with Bitcoin and Lightning, how it is used, and how
it is viewed. We’re opening up new ambitions, new ideas, new possibilities,
and a new, mainstream audience.

We have Strike for iOS, Android, Desktop, and a browser extension. You can
view a playlist of demos I put together on [my YouTube
channel](https://www.youtube.com/channel/UCcn2uBP2TvT-z6jiCP-
RhbA?view_as=subscriber).

![](https://miro.medium.com/max/1400/1*7NwzLpJIGCumD6kqUVi-tg.png)

# What this means

Bank accounts and debit cards can now speak to nodes all over the world, and
nodes all over the world can now speak to bank accounts and debit cards. The
possibilities are endless and the sky is the limit.

Can Strike be used to buy bitcoin? Sure, create an invoice from your existing
wallet and pay it. After completion, you’ll have less fiat in Strike and more
bitcoin in your wallet.

Can Strike be used to sell bitcoin? Sure, create a request in Strike and send
to it from your wallet. After completion, you’ll have more fiat in Strike and
less bitcoin in your wallet.

Can Strike be used for remittance payments? Yes, of course, it can. Just scan
the QR code and click pay.

Can Strike be used for internet tipping? Yes, of course, it can. Just scan the
QR code and click pay.

Is Strike another custodial wallet? No, not at all. It owns nobody’s coins and
nobody’s keys. If BTC is hacked and stolen, it’s my BTC and I’m fucked, nobody
else. That’s the way it should be. In a weird way, it’s a beautiful and
innovative hybrid.

# Strike in the wild

There are real people using Strike today, let me tell you my favorite user
story so far.

My family owns a cannabis business in Colorado. In Colorado, there are only a
handful of banks in the entire state willing to bank those in the cannabis
industry, and the waitlist to be banked by ours is now longer than two years.
Our family business struggles to stay banked, operates a security budget to
protect and migrate cash in our stores, and we’ve struggled immensely with
payment processors.

Those processing payments in the cannabis industry charge between 5%-15%, and
are known to be unreliable and unstable. For example, ours was recently down
for two months leaving us unable to process any credit/debit card payments.
This leaves businesses exposed and allows Strike to provide a level of fault
tolerance otherwise missing.

When I visited Colorado for Christmas, I showed my parents Strike. We ran to
the store and I demoed it to all of our upper management and employees. My
parents were already running a [BTCPay Server](https://btcpayserver.org/)
instance and offered a 10% discount for anyone who paid in BTC, as it was so
much easier for us to accept. The problem was, no customer was able to get a
Lightning wallet set up to make payments ranging from $0.10–$500. With Strike,
this changes immediately. All you need is the app and a debit card.

We passed Strike around to a few frequent customers and family friends,
telling them if you use this app, you get a 10% discount. It worked. Customers
young and old were using Strike to shop at our store, getting a discount, and
helping our business. Do they know what Bitcoin is? I have no idea. Did they
know they were using Bitcoin under the hood as a payment rail to transfer and
settle value? Absolutely not. Bitcoin was behind the scenes, making a
difference and benefiting individual lives and businesses without anyone
noticing they were even using it.

![](https://miro.medium.com/max/6048/1*mJ4H_h8dv-AJEYW1uHVvJA.jpeg)

![](https://miro.medium.com/max/6048/1*KEDp8Sc0lviWg0LTC_tFIw.jpeg)

Strike being used at Helping Hands Herbals in Boulder, CO, USA

The possibilities are endless. What about Twitch streamers and content
creators? Content creators can set up a Strike donation page and every time
someone donates BTC, they get fiat in their bank account (or whatever custom
fiat:BTC ratio they’d like). Magic.

The smallest changes can be transformative, but they have to be the right
changes. Discovering what those changes are takes patience, you have to pay
attention, you have to be **available in response**.

# The Future

Lightning offers real-time, cheap, and global settlement and self-clearing to
the world’s first natively digital asset class. We’ve put in the work to make
the barrier of entry low, and the flexibility + ease of use high.

There’s a lot of real-time and automated risk management, trading, compliance
and legal policy, application and protocol development to test. As I’ve said
before, this is not a race, and we will go at our own pace. However, we do
feel ready to expand those helping us test Strike.

So, here is the plan. We will continually widen our BETA every week, and start
with US users only, until we feel comfortable opening up usage globally. Our
goal is to be in a public BETA and put Strike on App Stores in the coming
months. This will take a community effort. A lot of testing, reporting of
bugs, feedback on features, and collaboration. If you’d like to join the beta
list, you can do so at [strike.zaphq.io](https://strike.zaphq.io). If you have
a special use case and really want to start testing today, email me at
zap@jackmallers.com, I’d love to hear your story and get you a download link.

You all know me, I have big plans. Partnerships to be announced, new products
and features, and events I’ll be hosting in Chicago to demonstrate the tech.
This is certainly exciting but very much the beginning.

# Thanks

Alright, everyone, that’s all I have for today. Not only am I unbelievably
excited, but I have a new-found sense of ambition.

To [CMT Digital](https://cmt.digital/), thank you. The work you continue to do
for Bitcoin on the legal, market, trading and compliance side of making these
dreams of ours come true is some of the most inspiring work I’ve seen in the
space. Colleen and everyone over at CMT maintains a low profile, but it’s
important to know that nothing that you’ve seen in the blog post works without
their dedication to our shared vision for the future.

I personally would like to shoutout the Zap team. Strike may look simple, but
this was the furthest from easy. We went through it all, together. Testing,
trying, failing, and repeating. Through it all, we stayed the course and
delivered a product we are all so incredibly proud of. We are all lucky to
have this group working on Bitcoin and I am the luckiest to be able to spend
so much time learning from and supporting this group every day. Hats off, you
should be proud. I certainly am.

Lastly, to the community. I was recently brought to tears on [my last podcast
appearance](https://www.whatbitcoindid.com/podcast/the-lightning-
network-2019-review-with-jack-mallers) because of the support you all give me.
It feels like I dropped out of college yesterday, and to think we have pulled
together the necessary banking partners, trading partners, regulatory
partners, written the code, and gotten to this point is beyond me. I love you
all like family, and I wish you knew how much I mean that. I think I’ve
stumbled upon something really cool here, and I hope to make y’all proud. It’s
always love Bitcoin fam ❤️

You can contact me [@JackMallers](https://twitter.com/JackMallers) on twitter
or zap@jackmallers.com via email. Feel free to [join our
slack](https://join.slack.com/t/zaphq/shared_invite/enQtMzgyNDA2NDI2Nzg0LWQ1OGMyMWI3YTdmYTQ0YTVmODg4ZmNkYjQ1MzUxNGExMGRmZWEyNTUyOGQzMzZkYTdhODE3NmQxZWZiOGFkYWI)
if you’d like to be more interactive with the Zap community or discuss Strike.

As I said above, I’ve got more coming. I’ll talk to you sooner than you think.

Be easy. Peace out 👊 🍻

\--

24

\--

\--

24

## [More from Jack Mallers](/?source=post_page-----
4f578c7c8984--------------------------------)

Follow

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F17e301c987a4&operation=register&redirect=https%3A%2F%2Fjimmymow.medium.com%2Fannouncing-
strike-by-
zap-4f578c7c8984&newsletterV3=fb26851df6e0&newsletterV3Id=17e301c987a4&user=Jack+Mallers&userId=fb26851df6e0&source=-----4f578c7c8984
---------------------subscribe_user-----------)

zap.jackmallers.com

Love podcasts or audiobooks? Learn on the go with our new app.

[Try
Knowable](https://knowable.fyi/?utm_source=medium&utm_medium=referral&utm_campaign=medium-
post-footer&source=post_page-----4f578c7c8984--------------------------------)

## Recommended from Medium

[[![Bitcoin
Support](https://miro.medium.com/fit/c/40/40/1*UQ5KcTYk3yWq2KRK9BE48Q.png)](https://medium.com/@bitcoinguidance?source=post_internal_links
---------0----------------------------)

[Bitcoin Support

](https://medium.com/@bitcoinguidance?source=post_internal_links---------
0----------------------------)

in

[Coinmonks

](https://medium.com/coinmonks?source=post_internal_links---------
0----------------------------)

## Coinbase is planning to invest in Indian cryptocurrency and Web3 once tax
regulations become…

![Coinbase is planning to invest in Indian cryptocurrency and Web3 once tax
regulations become
clearer](https://miro.medium.com/focal/112/112/50/50/0*iMPTqPmEJPRsNN-4.jpeg)](https://medium.com/@bitcoinguidance/coinbase-
is-planning-to-invest-in-indian-cryptocurrency-and-web3-once-tax-regulations-
become-dbc244ced75a?source=post_internal_links---------
0----------------------------)

[[![BestChange](https://miro.medium.com/fit/c/40/40/1*HiYpgKAAUb73_Zg-W0jGVg.png)](https://bestchange.medium.com/?source=post_internal_links
---------1----------------------------)

[BestChange

](https://bestchange.medium.com/?source=post_internal_links---------
1----------------------------)

## Commissions in the Bitcoin network rise to a two-year high, and miners are
switched off in China

![](https://miro.medium.com/focal/112/112/50/50/1*ZBZu_JEsTeHDemGLb2JRZg.jpeg)](https://bestchange.medium.com/commissions-
in-the-bitcoin-network-rise-to-a-two-year-high-and-miners-are-switched-off-in-
china-2f5b3b8cf3ca?source=post_internal_links---------
1----------------------------)

[[![Avalanche](https://miro.medium.com/fit/c/40/40/1*vPuxYoTQ_nTjEe-
OisXiKw.png)](https://avalancheavax.medium.com/?source=post_internal_links
---------2----------------------------)

[Avalanche

](https://avalancheavax.medium.com/?source=post_internal_links---------
2----------------------------)

in

[Avalanche

](https://medium.com/avalancheavax?source=post_internal_links---------
2----------------------------)

## Avalanche 101: An Overview of the Internet of Finance

![](https://miro.medium.com/focal/112/112/50/50/0*x-K-
rkGiEER7FBR_)](https://avalancheavax.medium.com/avalanche-101-an-overview-of-
the-internet-of-finance-7cdc5a2bee46?source=post_internal_links---------
2----------------------------)

[[![Avalanche](https://miro.medium.com/fit/c/40/40/1*vPuxYoTQ_nTjEe-
OisXiKw.png)](https://avalancheavax.medium.com/?source=post_internal_links
---------3----------------------------)

[Avalanche

](https://avalancheavax.medium.com/?source=post_internal_links---------
3----------------------------)

in

[Avalanche

](https://medium.com/avalancheavax?source=post_internal_links---------
3----------------------------)

## Order from Amazon, Walmart and eBay using AVAX on Shopping.io

![](https://miro.medium.com/focal/112/112/50/50/0*h2ppDzbCRiQKDIUT)](https://avalancheavax.medium.com/order-
from-amazon-walmart-and-ebay-using-avax-on-shopping-
io-8fae47f4888d?source=post_internal_links---------
3----------------------------)

[[![Tellor
Core](https://miro.medium.com/fit/c/40/40/2*losCEos6N68CYQZ0JBBaag.png)](https://tellor.medium.com/?source=post_internal_links
---------4----------------------------)

[Tellor Core

](https://tellor.medium.com/?source=post_internal_links---------
4----------------------------)

in

[Tellor

](https://medium.com/tellor?source=post_internal_links---------
4----------------------------)

## Tellor Tribute — Mechanisms of the Token Supply Growth Rate

![](https://miro.medium.com/focal/112/112/50/50/1*Xb_7PomQE57lN8Ozpx-
_uQ.jpeg)](https://tellor.medium.com/tellor-tribute-mechanisms-of-the-token-
supply-growth-rate-de14dbdd72f1?source=post_internal_links---------
4----------------------------)

[[![Acura
Network](https://miro.medium.com/fit/c/40/40/1*k3MHYt7kCurrLFLMZFW3hA.png)](https://acuranetwork.medium.com/?source=post_internal_links
---------5----------------------------)

[Acura Network

](https://acuranetwork.medium.com/?source=post_internal_links---------
5----------------------------)

## Acura Announces a Strategic Collaboration with ChainGuardians

![](https://miro.medium.com/focal/112/112/50/50/1*MGCQ8tpdhU5qqsFOyGAxHg.jpeg)](https://acuranetwork.medium.com/acura-
announces-a-strategic-collaboration-with-
chainguardians-f2aba573bd63?source=post_internal_links---------
5----------------------------)

[[![Gianluca
Busato](https://miro.medium.com/fit/c/40/40/0*SqLMbg9AHtdEC_NN.jpg)](https://medium.com/@gianlucabusato?source=post_internal_links
---------6----------------------------)

[Gianluca Busato

](https://medium.com/@gianlucabusato?source=post_internal_links---------
6----------------------------)

in

[Venice Swap

](https://medium.com/veniceswap?source=post_internal_links---------
6----------------------------)

## ERC-20 Token Standard simply explained

![](https://miro.medium.com/focal/112/112/50/50/1*RD8AzSYTm--
uI_AW5twaqA.jpeg)](https://medium.com/@gianlucabusato/erc-20-token-standard-
simply-explained-a22b444f06bf?source=post_internal_links---------
6----------------------------)

[[![Stanley
Charles](https://miro.medium.com/fit/c/40/40/0*n8WF_bIMwUFfDSh_)](https://medium.com/@stanjosec?source=post_internal_links
---------7----------------------------)

[Stanley Charles

](https://medium.com/@stanjosec?source=post_internal_links---------
7----------------------------)

## What’s Up With Cryptocurrency?

![](https://miro.medium.com/focal/112/112/50/50/1*qsQ6bDwCXusqwRZ0oY6vZw.jpeg)](https://medium.com/@stanjosec/whats-
up-with-cryptocurrency-71c44810b54e?source=post_internal_links---------
7----------------------------)

[](https://medium.com/?source=post_page-----
4f578c7c8984--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
4f578c7c8984--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
4f578c7c8984--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
4f578c7c8984--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
4f578c7c8984--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----4f578c7c8984--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----4f578c7c8984--------------------------------)

[Get
started](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fjimmymow.medium.com%2Fannouncing-
strike-by-zap-4f578c7c8984&source=post_page--------------------------
nav_reg-----------)

[![Jack
Mallers](https://miro.medium.com/fit/c/176/176/1*LMTxg8uEKM958_Dv1oG-2w.jpeg)](/)

[

## Jack Mallers

](/)

4.4K Followers

[zap.jackmallers.com](http://zap.jackmallers.com)

Follow

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F17e301c987a4&operation=register&redirect=https%3A%2F%2Fjimmymow.medium.com%2Fannouncing-
strike-by-
zap-4f578c7c8984&newsletterV3=fb26851df6e0&newsletterV3Id=17e301c987a4&user=Jack+Mallers&userId=fb26851df6e0&source=--------------------------subscribe_user-----------)

## More from Medium

[[![theCynicalCryptoAxolotl](https://miro.medium.com/fit/c/40/40/0*xKGuI3J47f4R6rIt.jpg)](https://medium.com/@cynicCryptoAxo?source=read_next_recirc
---------0---------------------a14fb0a6_c526_4573_afbd_35a8731001f7-------)

[theCynicalCryptoAxolotl

](https://medium.com/@cynicCryptoAxo?source=read_next_recirc---------0
---------------------a14fb0a6_c526_4573_afbd_35a8731001f7-------)

in

[Coinmonks

](https://medium.com/coinmonks?source=read_next_recirc---------0
---------------------a14fb0a6_c526_4573_afbd_35a8731001f7-------)

## “Bitcoin Is Destroying The World!” — No, It Might As Well Save It

![](https://miro.medium.com/focal/112/112/50/50/1*0uJAlfXs0IgoxP7xOaIEug.png)](https://medium.com/@cynicCryptoAxo/bitcoin-
is-destroying-the-world-no-it-might-as-well-save-
it-461a68b572fc?source=read_next_recirc---------0---------------------
a14fb0a6_c526_4573_afbd_35a8731001f7-------)

[[![Anchorage
Digital](https://miro.medium.com/fit/c/40/40/1*34oaWlK1bw0KhZCE9ZZTqA.png)](https://anchorage.medium.com/?source=read_next_recirc
---------1---------------------a14fb0a6_c526_4573_afbd_35a8731001f7-------)

[Anchorage Digital

](https://anchorage.medium.com/?source=read_next_recirc---------1
---------------------a14fb0a6_c526_4573_afbd_35a8731001f7-------)

in

[Anchorage Digital

](https://medium.com/anchorage?source=read_next_recirc---------1
---------------------a14fb0a6_c526_4573_afbd_35a8731001f7-------)

## Anchorage launches custody support for 31 new assets

![](https://miro.medium.com/focal/112/112/50/50/1*T-K2XH4fiLDP-
fxU_NU40w.png)](https://anchorage.medium.com/anchorage-launches-custody-
support-for-31-new-assets-8b4ec91963b9?source=read_next_recirc---------1
---------------------a14fb0a6_c526_4573_afbd_35a8731001f7-------)

[[![Fahad](https://miro.medium.com/fit/c/40/40/1*7coRP8dNpAJt8EuY2CPEJQ.gif)](https://medium.com/@faham123714?source=read_next_recirc
---------2---------------------a14fb0a6_c526_4573_afbd_35a8731001f7-------)

[Fahad

](https://medium.com/@faham123714?source=read_next_recirc---------2
---------------------a14fb0a6_c526_4573_afbd_35a8731001f7-------)

## What actually are Cryptocurrencies | Everything that you need to know
(2022)

![](https://miro.medium.com/focal/112/112/50/50/0*_1qlr7zQcRjc4_iU)](https://medium.com/@faham123714/what-
actually-are-cryptocurrencies-everything-that-you-need-to-
know-2022-eac9962e21d?source=read_next_recirc---------2---------------------
a14fb0a6_c526_4573_afbd_35a8731001f7-------)

[[![2EZ Crypto
🛡👩‍🌾](https://miro.medium.com/fit/c/40/40/0*ecBY4opEZ8SK1St0.jpg)](https://medium.com/@2ezCrypto?source=read_next_recirc
---------3---------------------a14fb0a6_c526_4573_afbd_35a8731001f7-------)

[2EZ Crypto 🛡👩‍🌾

](https://medium.com/@2ezCrypto?source=read_next_recirc---------3
---------------------a14fb0a6_c526_4573_afbd_35a8731001f7-------)

## The EZ Side Update: March 6th, 2022

![](https://miro.medium.com/focal/112/112/50/50/1*OHHL-
LtOBt9Cku_IZzQP9Q.png)](https://medium.com/@2ezCrypto/the-ez-side-update-
march-6th-2022-afe56474e3f0?source=read_next_recirc---------3
---------------------a14fb0a6_c526_4573_afbd_35a8731001f7-------)

[Help

](https://help.medium.com/hc/en-us)

[Status

](https://medium.statuspage.io)

[Writers

](https://about.medium.com/creators/)

[Blog

](https://blog.medium.com)

[Careers

](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e)

[Privacy

](https://policy.medium.com/medium-privacy-policy-f03bf92035c9)

[Terms

](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f)

[About

](https://medium.com/about?autoplay=1)

[Knowable

](https://knowable.fyi)

