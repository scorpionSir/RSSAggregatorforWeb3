[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/48ec3670f363&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Portis](https://miro.medium.com/fit/c/64/64/1*sjSyv6BBfH6HEcOo0Xr-7A.png)](https://medium.com/portis?source=post_page
-----48ec3670f363--------------------------------)

Published in

[Portis

](https://medium.com/portis?source=post_page-----
48ec3670f363--------------------------------)

[![portis](https://miro.medium.com/fit/c/96/96/1*nMh3K62zk5kXXR9gtGhLQQ.png)](/@portis?source=post_page
-----48ec3670f363--------------------------------)

[portis](/@portis?source=post_page-----
48ec3670f363--------------------------------)

Follow

Aug 9, 2019

·

4 min read

# Introducing: Portis One-Click Pay

## Letting non-crypto users easily sign payable transactions is an important
milestone in the road to mainstream adoption. We believe our new direct
purchase flow will help pave that path.

![](https://miro.medium.com/max/1400/1*H0aMZIyURoVCCTAzg9fWBw.jpeg)

Photo by
[rupixen](https://unsplash.com/@rupixen?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
on
[Unsplash](https://unsplash.com/search/photos/purchase?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

When we created Portis, we set out to solve the biggest issue that was
immediately evident when starting to use any DApp: **onboarding**.

“Install this extension or special browser, understand private keys and gas
fees, go to an exchange, open an account and figure out what it means to
withdraw to your wallet.” **_Yeesh_**. Users faced a lot of noise when all
they wanted to do was to simply buy a $10 NFT.

With the [Portis SDK](https://github.com/portis-project/web-sdk), developers
were able to ease the transition for new non-crypto users (without
compromising user custodianship). After we [integrated with the Gas Stations
Network](/@portis/sponsor-your-users-gas-fees-with-portis-and-tabookey-s-gas-
stations-network-7fd7c8406869), they could even solve the issue of having to
explain gas fees, as they could sponsor them instead.

We continued to chip away at friction by adding support for stablecoins such
as DAI and xDAI, integrating with Wyre’s API to enable fiat-to-crypto onramps
and building several other useful UX features like [trust this
app](https://docs.portis.io/#/trust-this-app), [change
network](https://docs.portis.io/#/methods?id=changenetwork), and more.

However, direct purchase flows were still too hard.

# The web3 checkout flow

Anyone with a background with e-commerce will be all too familiar with the
following diagram.

![](https://miro.medium.com/max/1400/0*RwljDkSsqQRprG9q.png)

Usually, you assume that if your user got to that last step — you’re golden.
After all, using services like Stripe or PayPal is super easy for users: they
punch in their CC details and that’s it. Service/product acquired.

If only it were that simple in the world of crypto. Without resorting to
centralized escrow solutions (we’re big believers in decentralization, so
that’s gonna a be a no from us dawg), **users cannot complete a transaction
until they have the required amount of crypto in their wallets**. Otherwise,
their transaction would simply get rejected by the network.

This means, that if your user has no crypto (which is extremely likely if your
DApp is targeting mainstream users, as it probably should), their “purchasing
items” step will look something like this:

  1. Goes to sign a transaction
  2. Sees “insufficient funds” message
  3. (Hopefully) Redirected to purchase crypto
  4. Completes crypto purchase (usually has to manually input how much)
  5. Waits until crypto is in their wallet
  6. Once the crypto is inside their wallet — goes back to your DApp and signs the transaction

> That final purchase step is fragile enough, since someone is making a
> decision to spend their hard-earned cash on your product.

Adding so much friction on top, in an age where making web2 purchases is so
easy, will most likely result in the dreaded “[shopping cart
abandonment](https://en.wikipedia.org/wiki/Abandonment_rate)" event.

It’s as if mainstream people had to make a bank transaction to a different
account before each online purchase, wait until the transfer went through, and
only once it did, come back to your website to complete the purchase. Fat
chance of that happening.

# Time to unclog your conversion funnel

We’ve been listening to DApp developers and hearing their cries of pain over
this issue. And to tackle it we’ve introduced our new direct purchase flow!

![](https://miro.medium.com/max/808/1*b1cdUKWyv35ugCVml-vnfA.gif)

## How does it work?

When a user goes to sign a transaction but has insufficient funds, we let them
sign the transaction anyway, but we don’t submit it to the network. We then
ask them to approve purchasing the required amount of ETH.

 **Only after we detect that the ETH is in their wallet, we submit their pre-
signed transaction to the network.**

It’s not like we’re letting users do anything they couldn’t otherwise do
themselves, we’re simply making their lives easier by constructing the flow in
a manner which resembles the one they know and love from web2 apps.

And by doing that, we’re empowering developers using Portis, since they can
improve their conversion rates. To top it off, developers don’t have to do
anything, as our One-Click pay flow kicks in automatically.

More #BUIDL, more #SIMPL, just the way we like it.

Happy coding!

The Portis Team

Have any questions? Join the conversation on our
[Telegram](https://t.me/PortisHQ?source=post_page---------------------------)
and
[Twitter](https://twitter.com/portis_io?source=post_page---------------------------).
Ready to #BUIDL? Head on to our
[docs](http://docs.portis.io/?source=post_page---------------------------).  
Got any suggestions? [We 💙 feedback](https://portis.hellonext.co)!

\--

\--

\--

## [More from Portis](/portis?source=post_page-----
48ec3670f363--------------------------------)

Making blockchains simple for users

[Read more from Portis](/portis?source=post_page-----
48ec3670f363--------------------------------)

## Recommended from Medium

[[![Alex
Bentley](https://miro.medium.com/fit/c/40/40/1*vX_pF-e2oPtwF2gD6vg_sA.png)](/@alex-
bentley?source=post_internal_links---------0----------------------------)

[Alex Bentley

](/@alex-bentley?source=post_internal_links---------
0----------------------------)

in

[Crypto Unchained

](https://medium.com/crypto-unchained?source=post_internal_links---------
0----------------------------)

## When They Get Scared, They Sell

![](https://miro.medium.com/focal/112/112/50/50/1*xYPSZVYPA0A3m1YvwgKxpw.jpeg)](/crypto-
unchained/when-they-get-scared-they-
sell-7dc5ef9e55cc?source=post_internal_links---------
0----------------------------)

[[![BitFlex
FinTech](https://miro.medium.com/fit/c/40/40/1*rGoGQs6XwCtuhhi9DCiTvQ.png)](/@bitflexcrypto?source=post_internal_links
---------1----------------------------)

[BitFlex FinTech

](/@bitflexcrypto?source=post_internal_links---------
1----------------------------)

## BitFlex FinTech X Celo Alliance for Prosperity — Improving the
accessibility of Digital Assets in…

![](https://miro.medium.com/focal/112/112/50/50/1*AO-9Jk6ztcgWdlMisp3gwA.png)](/@bitflexcrypto/bitflex-
fintech-x-celo-alliance-for-prosperity-improving-the-accessibility-of-digital-
assets-in-67ce0637451d?source=post_internal_links---------
1----------------------------)

[[![Tobi
Obiniyi](https://miro.medium.com/fit/c/40/40/1*iI0bs3IikeLato3VoNS4rw.jpeg)](/@blasttoby?source=post_internal_links
---------2----------------------------)

[Tobi Obiniyi

](/@blasttoby?source=post_internal_links---------
2----------------------------)

## COULD THESE BE THE REASONS FOR THE RECENT PRICE SURGE IN DOGECOIN?

](/@blasttoby/could-these-be-the-reasons-for-the-recent-price-surge-in-
dogecoin-ed9dc9eedfb3?source=post_internal_links---------
2----------------------------)

[[![Shuule](https://miro.medium.com/fit/c/40/40/0*3rxMhZhcqjvHSRC7)](/@isopye81?source=post_internal_links
---------3----------------------------)

[Shuule

](/@isopye81?source=post_internal_links---------3----------------------------)

## SWAPULT

![](https://miro.medium.com/focal/112/112/50/50/0*gThsiL0Qo1w_G_52)](/@isopye81/swapult-c25ba631eb9?source=post_internal_links
---------3----------------------------)

[[![Ronnie Moshe
Rendel](https://miro.medium.com/fit/c/40/40/0*roemXBGaslwYi6GQ)](/@yeshivaventures?source=post_internal_links
---------4----------------------------)

[Ronnie Moshe Rendel

](/@yeshivaventures?source=post_internal_links---------
4----------------------------)

## Decentralized Charity & Investment for Existing YouTube Networks

![](https://miro.medium.com/focal/112/112/50/50/1*v3ZsN9V13GgKrDCUgya31Q.png)](/@yeshivaventures/decentralized-
charity-investment-for-existing-youtube-
networks-c50e23ba938c?source=post_internal_links---------
4----------------------------)

[[![Hakan
Kayış](https://miro.medium.com/fit/c/40/40/2*q9RAz9uCTM4prX4lMrrgNQ.jpeg)](/@hakankayis?source=post_internal_links
---------5----------------------------)

[Hakan Kayış

](/@hakankayis?source=post_internal_links---------
5----------------------------)

## The Development of Cryptocurrency in Turkey

![](https://miro.medium.com/focal/112/112/50/50/1*6Azek5DO9YDry1wc9DOO9w.png)](/@hakankayis/the-
development-of-cryptocurrency-in-turkey-17b0950bdb7?source=post_internal_links
---------5----------------------------)

[[![EthValidator](https://miro.medium.com/fit/c/40/40/2*Uii5dff9ylObKb7SUYYTVw.png)](/@ethvalidator?source=post_internal_links
---------6----------------------------)

[EthValidator

](/@ethvalidator?source=post_internal_links---------
6----------------------------)

## Eth2 News | May 28, 2020

![](https://miro.medium.com/focal/112/112/50/50/1*psSrlPPIbBlY4mx8n6IPpg.png)](/@ethvalidator/eth2-news-
may-28-2020-3d5265bb344b?source=post_internal_links---------
6----------------------------)

[[![Fantasy Cricket Fan
Token](https://miro.medium.com/fit/c/40/40/1*9MDwlH5ICaVKtky-
JdTNqA.png)](/@fcftoken?source=post_internal_links---------
7----------------------------)

[Fantasy Cricket Fan Token

](/@fcftoken?source=post_internal_links---------7----------------------------)

## What is Fantasy Cricket Fan Token ($FCFT)?🏏

![](https://miro.medium.com/focal/112/112/50/50/1*MpOYPZ2vhbhqOqLkgA8TSg@2x.jpeg)](/@fcftoken/what-
is-fantasy-cricket-fan-token-fcft-79b33400d87e?source=post_internal_links
---------7----------------------------)

[](/?source=post_page-----48ec3670f363--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
48ec3670f363--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
48ec3670f363--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
48ec3670f363--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
48ec3670f363--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----48ec3670f363--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----48ec3670f363--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fportis%2Fintroducing-
portis-one-click-pay-48ec3670f363&source=post_page--------------------------
nav_reg-----------)

[![portis](https://miro.medium.com/fit/c/176/176/1*nMh3K62zk5kXXR9gtGhLQQ.png)](/@portis)

[

## portis

](/@portis)

433 Followers

<https://portis.io>

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F4462dd2c963a&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fportis%2Fintroducing-
portis-one-click-
pay-48ec3670f363&newsletterV3=56bd0a809585&newsletterV3Id=4462dd2c963a&user=portis&userId=56bd0a809585&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Fanezul
Fane](https://miro.medium.com/fit/c/40/40/1*M4KkF9EjGm3YOiJmTcJ1Ig.jpeg)](/@fanezul?source=read_next_recirc
---------0---------------------467d7d5d_452c_4ef4_b639_f259e7db4c2f-------)

[Fanezul Fane

](/@fanezul?source=read_next_recirc---------0---------------------
467d7d5d_452c_4ef4_b639_f259e7db4c2f-------)

## What can we expect from Apple’s March ‘Peek Performance’ event?

![](https://miro.medium.com/focal/112/112/50/50/1*Gr6k3M1gIX9emramsMgbvA.jpeg)](/@fanezul/what-
can-we-expect-from-apples-march-peek-performance-
event-48c4b1236fee?source=read_next_recirc---------0---------------------
467d7d5d_452c_4ef4_b639_f259e7db4c2f-------)

[[![Bhagwatrajpoot](https://miro.medium.com/fit/c/40/40/0*gp5ARgmcmHDNIMd9)](/@bhagwatrajpoot7389?source=read_next_recirc
---------1---------------------467d7d5d_452c_4ef4_b639_f259e7db4c2f-------)

[Bhagwatrajpoot

](/@bhagwatrajpoot7389?source=read_next_recirc---------1---------------------
467d7d5d_452c_4ef4_b639_f259e7db4c2f-------)

## Core Components and Native Components

![](https://miro.medium.com/focal/112/112/50/50/0*wyL9daHQYChPJudp.jpg)](/@bhagwatrajpoot7389/core-
components-and-native-components-394a33e1b44e?source=read_next_recirc---------
1---------------------467d7d5d_452c_4ef4_b639_f259e7db4c2f-------)

[[![NeftyBlocks](https://miro.medium.com/fit/c/40/40/1*PuKj9kEEX-
zEsf_RFBLylA.png)](/@neftyblocks?source=read_next_recirc---------2
---------------------467d7d5d_452c_4ef4_b639_f259e7db4c2f-------)

[NeftyBlocks

](/@neftyblocks?source=read_next_recirc---------2---------------------
467d7d5d_452c_4ef4_b639_f259e7db4c2f-------)

## Three Questions with Taco About “Brigade”

![](https://miro.medium.com/focal/112/112/50/50/1*MLjy5aOKDMfeX9iUr1Idzg.png)](/@neftyblocks/three-
questions-with-taco-about-brigade-b861d23416ae?source=read_next_recirc
---------2---------------------467d7d5d_452c_4ef4_b639_f259e7db4c2f-------)

[[![Anthony Oliver](https://miro.medium.com/fit/c/40/40/1*_0JRPkfiBDdO1LgCK6a
--w.jpeg)](/@antcoliver?source=read_next_recirc---------3---------------------
467d7d5d_452c_4ef4_b639_f259e7db4c2f-------)

[Anthony Oliver

](/@antcoliver?source=read_next_recirc---------3---------------------
467d7d5d_452c_4ef4_b639_f259e7db4c2f-------)

## Racing to Talk About Elden Ring

![](https://miro.medium.com/focal/112/112/50/50/1*bA-Y17sTdCP9RqlBMBBmig.jpeg)](/@antcoliver/racing-
to-talk-about-elden-ring-c89d7d9e6221?source=read_next_recirc---------3
---------------------467d7d5d_452c_4ef4_b639_f259e7db4c2f-------)

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

