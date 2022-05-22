[](https://medium.com/)

[Get unlimited access](https://medium.com/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/e9bb63750280&~feature=LoOpenInAppButton&~channel=ShowPostUnderUser&~stage=mobileNavBar)

[](https://medium.com/)

[Home](https://medium.com/)

[Notifications](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Jack
Mallers](https://miro.medium.com/fit/c/96/96/1*LMTxg8uEKM958_Dv1oG-2w.jpeg)](/?source=post_page
-----e9bb63750280--------------------------------)

[Jack Mallers](/?source=post_page-----
e9bb63750280--------------------------------)

Follow

Apr 1, 2020

·

8 min read

# Announcing strike.me by Zap

Yo. Today I am extremely excited to release Strike’s latest feature,
[strike.me](http://strike.me/). A few months ago [I announced
Strike](https://medium.com/@JimmyMow/announcing-strike-by-zap-4f578c7c8984),
an application that allows you to make Bitcoin and Lightning payments with
your bank account or debit card. However, as I mentioned in my post, Strike is
only the beginning.

Today, we are announcing [strike.me](http://strike.me/jack), a social tipping
platform that allows anyone in the world to accept tips. These tips are
Lightning Network invoices, payable by any compatible wallet anywhere in the
world. Payments are then on-the-fly auto-converted to cash in your account as
the receiver.

Every Strike user has a [strike.me](http://strike.me/) page where you can
customize your username, description, profile picture, and more.

![](https://miro.medium.com/max/1400/1*jHby21tOZbCmhgyRD6MXgQ.png)

[My strike.me page 🙂](https://strike.me/jack)

With Strike, we use Bitcoin and Lightning for real-time, cheap, and global
settlement. Lightning has this chicken and egg problem where users making
payments, and merchants offering products, have this positive correlation; one
has to inform the other. By providing real-world utility for those looking to
participate in this new economy, we open up the world to use cases that quite
frankly don’t exist yet. We are looking beyond helping people make Bitcoin and
Lightning payments. There is much more to do with our infrastructure, and
we’re just scratching the surface. With [strike.me](https://strike.me) we
introduce our first tool on the merchant and acquiring side, with many more to
come.

So why start with tipping and why now?

# The Story

We live in a world where various content distribution platforms live in the
palm of our hands. Over recent years, this has resulted in consumer
preferences shifting away from mediums like radio, TV, magazines, and
newspapers and into newer mediums such as social media, blogs, apps, and the
internet at large. In turn, this gave rise to the digital content creation
market where monetizing the individual is a growing phenomenon and an
exploding industry. We are seeing YouTubers, gamers, Instagram influencers,
adult film actors/actresses, etc. _become_ the brand.

But how are these people of the internet monetizing their content, their new-
found audience, and more specifically, accepting payments?

The amount of content uploaded to the internet today is eye-opening and
growing ([with an expected compound and annual growth rate of
16.5%](https://www.credenceresearch.com/report/digital-content-creation-
market)):

  * Over **2 million blog posts** are published on the Internet every day.
  *  **1 billion stories** are shared through Facebook products (Facebook, Instagram, etc.) every day.
  * Over **300 hours** of video are uploaded to YouTube every minute.

Holy shit. That’s a lot of content. Who is consuming all of this content?
Apparently an expansive, global, market. That’s who:

  * [There are **4.18 billion mobile Internet users** worldwide.](https://www.statista.com/statistics/617136/digital-population-worldwide/)
  * [ **100% of 18- to 29-year-olds** are on the internet.](https://www.statista.com/statistics/266587/percentage-of-internet-users-by-age-groups-in-the-us/)
  * [The average Internet user spends **6.5 hours online every day**.](https://wearesocial.com/global-digital-report-2019)

# The Money

Tips and donations are a popular, albeit new revenue model for independent
content creators. In light of creators seeking alternative forms of
compensation outside of advertising, the tipping economy has emerged as a
viable solution. This is particularly important when considering a central
third-party may have control over [how you
monetize](https://medium.com/internet-creators-guild/youtube-de-monetization-
explained-44464f902a22#.4astpj6y4). Consumers are more than willing to
personally support their favorite content creators. The well-known problem is
how exactly content creators accept payment, especially considering their
audience is spread all over the world.

Top gaming streamers like [Jeremy “DisguisedToast” ****
Wang](https://en.wikipedia.org/wiki/Disguised_Toast)
[claim](https://www.tubefilter.com/2018/10/10/twitch-streamers-earn-per-month-
breakdown-disguisedtoast/) donations make up a significant portion of their
revenue, often surpassing ad revenue. Erotic photographer [Holly
Randall](https://en.wikipedia.org/wiki/Holly_Randall)
[mentioned](https://www.youtube.com/watch?v=Aauwl88Hgr4) that tips in the
adult industry for personal content such as camming, Snapchat, and more
provide new ways for models to monetize their work. Tips allow creators to
generate monthly recurring income in addition to enabling a “one-off” market
where users can tip-per-use.

PayPal is the most used processor for tips, and we believe we have identified
various issues. Using Paypal as an example:

  1. Compatibility

  * In order to tip someone without prohibitive fees, a user needs to be on PayPal already. Venmo users cannot pay PayPal users, CashApp users cannot pay Venmo users, and Zelle users cannot pay CashApp users. This is very limiting to the audience, especially on a global scale.

2\. Fees

  * PayPal’s fees frequently price out smaller merchants and murder the micropayment economy. Currently, online transactions cost a merchant 2.9% + $0.30 if the payment is coming from within the U.S. and 4.4% + $0.30 if the payment is coming from outside the U.S. This fee structure obsoletes the micropayment economy entirely.

3\. Censorship

  * Arguably the biggest issue is PayPal’s stance on who they serve on their platform. In November of 2019, PayPal removed support for over 100,000 PornHub performers. Currently, PornHub recommends users to pay models through bank deposits, requiring users to enter their beneficiary name, ABA Routing number, and Account number to make a donation.

What is needed is a global, interoperable, protocol for transferring value
cheaply and instantly. One that is compatible with thousands of wallets and
apps by default. One that is inherently global and knows of no borders. One
that uses a money that requires no permission or third-party authority to
acquire, hold, and spend. We need Bitcoin to underpin this new budding form of
internet commerce. And last, but not least, we need infrastructure and a set
of tools that make it usable and desirable for all.

# The Product

Ever since Bitcoin’s inception, it has been touted as the solution to internet
commerce. A natively digital asset that is inherently global, comparatively
free, instantly settles, where users can send both micropayments and large
amounts. A streamer in the US can get tipped $1.00 by a fan in Russia
instantly with no charge. Right?

Well, no. Without the Lightning Network, the Bitcoin blockchain (or any
decentralized censorship-resistant blockchain) comes with its own limitations.
Finality and settlement aren’t instant and the cost to make a payment is quite
literally the opposite of free.

There are also many issues for merchants accepting bitcoin as payment. We run
into the same issues for all merchants; volatility, taxes, custody, managing a
wallet, and so on have never been worth it to the acquiring side.

What if anyone in the world can scan a QR code with any compatible Bitcoin and
Lightning app? What if a full node in Australia, a Strike user in Chicago, and
everyone in-between could tip users instantly? What if the receiver didn’t
have to deal with volatility, taxes, custody, and wallet backups? What if the
receiver simply received fiat in their account whenever they got tipped? What
would that look like?

It would look like [strike.me](https://strike.me), that’s what it would look
like.

# strike.me

With [strike.me](http://strike.me), the goal is simple: we want to give the
content creators of the internet the ability to be a merchant to everyone in
the world. Anyone in the world looking to tip you can download any compatible
application, scan the QR code, click pay, and you get fiat in your bank
account.

Popular payment apps like Venmo are limited to their own economy and censor
users in various industries. Payment applications each service their own
niche. Venmo is a social application, Cash App allows simple pseudonymous
payments, and PayPal has more global reach than both. They all respectfully
cater to their own segregated economies.

Strike, on the other hand, is built on top of the world’s first global digital
currency. [strike.me](http://strike.me) users can transact socially,
pseudonymously, and globally. Oh, and it already has millions of customers
that can use it, because there are millions around the world that own and use
bitcoin.

## How it works

Every single Strike user has a [strike.me](http://strike.me) page created for
them when they create their account. Inside of Strike, you can navigate to
your profile where you can adjust your username, profile picture, description,
and whether or not your page is public.

![](https://miro.medium.com/max/1656/1*NI3vCWSwzFdXqKmBXPg-tg.png)

![](https://miro.medium.com/max/1656/1*LXbHhgQ8zKRllFRF7MCuJQ.png)

Once your page is public, it will be located at **strike.me/
_YOUR_USERNAME_**.

![](https://miro.medium.com/max/1400/1*jHby21tOZbCmhgyRD6MXgQ.png)

[strike.me/jack](http://strike.me/jack)

Anyone can then visit your page, enter an amount, and send you a tip whether
they have Strike or any other compatible wallet and/or application.

Finally, as the receiver of a tip, you simply get fiat.

![](https://miro.medium.com/max/1656/1*ewynNBWPig3rd8TpmfZYDg.png)

![](https://miro.medium.com/max/1656/1*8W7yat83YzQoaPEK7mE-Aw.png)

# What’s Next

The ability for those on the internet to accept payment from anyone in the
world, as fiat in their account, instantly and with no fees is a major step
forward for the digital content creation market.

All of our existing Strike BETA testers can help us test today by simply
updating their Strike app and turning on their [strike.me](http://strike.me)
profile. If you are looking to join our BETA program, you can sign up at
[strike.zaphq.io](http://strike.zaphq.io).

If you are a blogger, podcaster, YouTube personality, Instagram influencer,
Twitch streamer, adult film model, or any internet content creator with a
special use case that is interested in hosting a [strike.me](http://strike.me)
page for accepting tips and donations please reach out to me on
[Twitter](https://twitter.com/JackMallers) or at
[zap@jackmallers.com](mailto:zap@jackmallers.com). I’d love to hear your story
and get you onboard.

Currently, Strike usage has been explosive. In the last 20 days, we’ve seen
$20,000 worth of payments on Strike, with $3,000 worth of payments made in a
single day earlier this week. With our existing group of small private BETA
users alone, Strike is already on pace to achieve $250,000-$500,000 worth of
volume in a calendar year.

I’ll be moving Strike out of BETA sooner than you think, with many more Strike
features and products coming out over the coming months.

# Thanks

Alright, friends, that’s going to wrap up today's updates. I am excited to see
existing Strike BETA testers turn on their [strike.me](http://strike.me) page
and start accepting tips! Tweet me your [strike.me](http://strike.me) page,
I’ll send you a tip 😃

As always, shoutout to the Zap team. We wanted to get a merchant tool into the
wild, and we were able to put this together in a hackathon. An unbelievably
talented group of individuals that continues to build, even in times like
these.

Lastly, to the community. Thank you for the continued support. We are just
getting started with Strike, with so many more features and products to come
for both consumers and merchants. I hope everyone is staying healthy and I
wish you and your love ones the best in these tough times ❤️.

You can contact me [@JackMallers](https://twitter.com/JackMallers) on twitter
or [zap@jackmallers.com](mailto:zap@jackmallers.com) via email. Feel free to
[join our
slack](https://join.slack.com/t/zaphq/shared_invite/enQtMzgyNDA2NDI2Nzg0LWQ1OGMyMWI3YTdmYTQ0YTVmODg4ZmNkYjQ1MzUxNGExMGRmZWEyNTUyOGQzMzZkYTdhODE3NmQxZWZiOGFkYWI)
if you’d like to be more interactive with the Zap community or discuss Strike.

More things, soon come.

Catch you on the flip side ✌️🍻

\--

6

\--

\--

6

## [More from Jack Mallers](/?source=post_page-----
e9bb63750280--------------------------------)

Follow

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F17e301c987a4&operation=register&redirect=https%3A%2F%2Fjimmymow.medium.com%2Fannouncing-
strike-me-by-
zap-e9bb63750280&newsletterV3=fb26851df6e0&newsletterV3Id=17e301c987a4&user=Jack+Mallers&userId=fb26851df6e0&source=-----e9bb63750280
---------------------subscribe_user-----------)

zap.jackmallers.com

Love podcasts or audiobooks? Learn on the go with our new app.

[Try
Knowable](https://knowable.fyi/?utm_source=medium&utm_medium=referral&utm_campaign=medium-
post-footer&source=post_page-----e9bb63750280--------------------------------)

## Recommended from Medium

[[![Acuity Knowledge
Partners](https://miro.medium.com/fit/c/40/40/2*3dBCLymTtK-
eskkDsKS6xQ.jpeg)](https://acuityknowledgepartners.medium.com/?source=post_internal_links
---------0----------------------------)

[Acuity Knowledge Partners

](https://acuityknowledgepartners.medium.com/?source=post_internal_links
---------0----------------------------)

## Can you trade off compliance?

![](https://miro.medium.com/focal/112/112/50/50/1*WwGkT_n4X-pJhRKWBTMDeA.jpeg)](https://acuityknowledgepartners.medium.com/the-
cost-of-ignoring-compliance-87ed2ece2ebe?source=post_internal_links---------
0----------------------------)

[[![Anthony
McGuire](https://miro.medium.com/fit/c/40/40/1*jwvt6eu0UiR7ToY3rdljKQ.png)](https://anthonymcguire.medium.com/?source=post_internal_links
---------1----------------------------)

[Anthony McGuire

](https://anthonymcguire.medium.com/?source=post_internal_links---------
1----------------------------)

## The Mighty Ducks and The Bored Apes

![](https://miro.medium.com/freeze/focal/112/112/50/50/1*yfnSPSL10GmxIEtWQfJ1JA.gif)](https://anthonymcguire.medium.com/the-
mighty-ducks-and-the-bored-apes-da9e5551e86d?source=post_internal_links
---------1----------------------------)

[[![Zack
Seckler](https://miro.medium.com/fit/c/40/40/1*entZOG6YZ0ae21mkCh9IEw.jpeg)](https://medium.com/@zackseckler?source=post_internal_links
---------2----------------------------)

[Zack Seckler

](https://medium.com/@zackseckler?source=post_internal_links---------
2----------------------------)

in

[Creators Are Us

](https://medium.com/creators-are-us?source=post_internal_links---------
2----------------------------)

## Rei Inamoto

![nikelab_screenshot](https://miro.medium.com/focal/112/112/50/50/0*-6M-Fh5vlWonb8jp.jpg)](https://medium.com/@zackseckler/rei-
inamoto-abac9688a8a9?source=post_internal_links---------
2----------------------------)

[[![!mpact](https://miro.medium.com/fit/c/40/40/2*0GsdlZFvX-
ypzUzyMsKXqA.png)](https://impactmagazine.medium.com/?source=post_internal_links
---------3----------------------------)

[!mpact

](https://impactmagazine.medium.com/?source=post_internal_links---------
3----------------------------)

## Doug Baumoel

![](https://miro.medium.com/focal/112/112/50/50/1*d7-3s6jzNVNw3OSOccxu1g.png)](https://impactmagazine.medium.com/doug-
baumoel-2b6d1f1e2ae?source=post_internal_links---------
3----------------------------)

[[![Intpaymentsolutions](https://miro.medium.com/fit/c/40/40/0*snWZkXUo-3uTsixf)](https://intpaymentsolutions.medium.com/?source=post_internal_links
---------4----------------------------)

[Intpaymentsolutions

](https://intpaymentsolutions.medium.com/?source=post_internal_links---------
4----------------------------)

## Importance Of Card Not Present Transaction In 2020

![Importance Of Card Not Present Transaction In
2020](https://miro.medium.com/focal/112/112/50/50/0*jvDe-
ojl0dIDiW0T.jpg)](https://intpaymentsolutions.medium.com/importance-of-card-
not-present-transaction-in-2020-9d5ad47687d8?source=post_internal_links
---------4----------------------------)

[[![@bh!
Author](https://miro.medium.com/fit/c/40/40/2*31fecCVOFk-5HPiNs76TeQ.jpeg)](https://medium.com/@bHi.as.author?source=post_internal_links
---------5----------------------------)

[@bh! Author

](https://medium.com/@bHi.as.author?source=post_internal_links---------
5----------------------------)

## The Ascension

![](https://miro.medium.com/focal/112/112/50/50/1*7N4gtft3a8ZYbdV94Oej6g.jpeg)](https://medium.com/@bHi.as.author/the-
ascension-103e39ff8756?source=post_internal_links---------
5----------------------------)

[[![Nataliya.ai](https://miro.medium.com/fit/c/40/40/2*w2PKSrnL5ZnEy1EiGoaGUw.jpeg)](https://nataliyadotai.medium.com/?source=post_internal_links
---------6----------------------------)

[Nataliya.ai

](https://nataliyadotai.medium.com/?source=post_internal_links---------
6----------------------------)

in

[Balanced Fashion by Nataliya.ai

](https://medium.com/nataliya-makulova?source=post_internal_links---------
6----------------------------)

## Fashion Tech News & Start Up Events in NYC | 8.16–9.14.17 | Notes on
Sustainability, Part 2 🌱

![](https://miro.medium.com/focal/112/112/50/50/1*ypGImtQLUww0lH4E6SNt_Q.jpeg)](https://nataliyadotai.medium.com/fashion-
tech-news-start-up-events-in-nyc-8-16-9-14-17-notes-on-sustainability-
part-2-a2cdb576b09e?source=post_internal_links---------
6----------------------------)

[[![OyeLabs](https://miro.medium.com/fit/c/40/40/2*sjscSn4i8f1MnN2en2hB7Q.png)](https://myoyelabs.medium.com/?source=post_internal_links
---------7----------------------------)

[OyeLabs

](https://myoyelabs.medium.com/?source=post_internal_links---------
7----------------------------)

## Drizly-The Amazon For Liquor

![](https://miro.medium.com/focal/112/112/50/50/1*Z68fzAMerjoq-
dBTWeDVIw.png)](https://myoyelabs.medium.com/drizly-the-amazon-for-
liquor-f5b5ccc537c1?source=post_internal_links---------
7----------------------------)

[](https://medium.com/?source=post_page-----
e9bb63750280--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
e9bb63750280--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
e9bb63750280--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
e9bb63750280--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
e9bb63750280--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----e9bb63750280--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----e9bb63750280--------------------------------)

[Get
started](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fjimmymow.medium.com%2Fannouncing-
strike-me-by-zap-e9bb63750280&source=post_page--------------------------
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
strike-me-by-
zap-e9bb63750280&newsletterV3=fb26851df6e0&newsletterV3Id=17e301c987a4&user=Jack+Mallers&userId=fb26851df6e0&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Shivali Rawat](https://miro.medium.com/fit/c/40/40/1*hAfjZoy-
oie4q_qiBnuptA.jpeg)](https://medium.com/@shivalirawat28?source=read_next_recirc
---------0---------------------948acdb9_5c38_4564_9093_24b8bbb4e105-------)

[Shivali Rawat

](https://medium.com/@shivalirawat28?source=read_next_recirc---------0
---------------------948acdb9_5c38_4564_9093_24b8bbb4e105-------)

in

[Coinmonks

](https://medium.com/coinmonks?source=read_next_recirc---------0
---------------------948acdb9_5c38_4564_9093_24b8bbb4e105-------)

## Is Bitcoin really Driving the Altcoin Market?

![](https://miro.medium.com/focal/112/112/50/50/1*KM6941-66_kbqnXbR0AGHg.jpeg)](https://medium.com/@shivalirawat28/is-
bitcoin-really-driving-the-altcoin-market-85bf07fecaa9?source=read_next_recirc
---------0---------------------948acdb9_5c38_4564_9093_24b8bbb4e105-------)

[[![lbayas](https://miro.medium.com/fit/c/40/40/1*7gL_QeHJLifQ638OIL4k0A.jpeg)](https://medium.com/@lbayas?source=read_next_recirc
---------1---------------------948acdb9_5c38_4564_9093_24b8bbb4e105-------)

[lbayas

](https://medium.com/@lbayas?source=read_next_recirc---------1
---------------------948acdb9_5c38_4564_9093_24b8bbb4e105-------)

in

[Cryptograf

](https://medium.com/cryptograf?source=read_next_recirc---------1
---------------------948acdb9_5c38_4564_9093_24b8bbb4e105-------)

## Crypto, Ai, and the Social Good

![](https://miro.medium.com/focal/112/112/50/50/0*TFyMKkYV0hNSAxze.png)](https://medium.com/@lbayas/crypto-
ai-and-the-social-good-5332e0a1cdd0?source=read_next_recirc---------1
---------------------948acdb9_5c38_4564_9093_24b8bbb4e105-------)

[[![Truflation](https://miro.medium.com/fit/c/40/40/1*hAFjyzQ9r_JI7VyrELxrzQ.jpeg)](https://truflation.medium.com/?source=read_next_recirc
---------2---------------------948acdb9_5c38_4564_9093_24b8bbb4e105-------)

[Truflation

](https://truflation.medium.com/?source=read_next_recirc---------2
---------------------948acdb9_5c38_4564_9093_24b8bbb4e105-------)

in

[Truflation

](https://medium.com/truflation?source=read_next_recirc---------2
---------------------948acdb9_5c38_4564_9093_24b8bbb4e105-------)

## Truflation Oracle Update [March 2022] — Detailed Report

![](https://miro.medium.com/focal/112/112/50/50/1*smOGIn71vqZVzcedr9juZQ.jpeg)](https://truflation.medium.com/truflation-
oracle-update-march-2022-detailed-report-8ecaa1317475?source=read_next_recirc
---------2---------------------948acdb9_5c38_4564_9093_24b8bbb4e105-------)

[[![Lorenzo Primiterra, The Crypto
Nomad](https://miro.medium.com/fit/c/40/40/1*1sh7zdIQ22z6SCpGJE9DhA.jpeg)](https://lorenzoprimiterra.medium.com/?source=read_next_recirc
---------3---------------------948acdb9_5c38_4564_9093_24b8bbb4e105-------)

[Lorenzo Primiterra, The Crypto Nomad

](https://lorenzoprimiterra.medium.com/?source=read_next_recirc---------3
---------------------948acdb9_5c38_4564_9093_24b8bbb4e105-------)

in

[BLOCK6

](https://learn.block6.tech/?source=read_next_recirc---------3
---------------------948acdb9_5c38_4564_9093_24b8bbb4e105-------)

## Bitcoin as legal tender: report from El Salvador

![](https://miro.medium.com/focal/112/112/50/50/1*mplNZi7a8jmmZylZSDtjQQ.jpeg)](https://lorenzoprimiterra.medium.com/bitcoin-
as-legal-tender-report-from-el-salvador-6a008003d48d?source=read_next_recirc
---------3---------------------948acdb9_5c38_4564_9093_24b8bbb4e105-------)

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

