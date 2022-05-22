[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/795db1f8a3d&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Portis](https://miro.medium.com/fit/c/64/64/1*sjSyv6BBfH6HEcOo0Xr-7A.png)](https://medium.com/portis?source=post_page
-----795db1f8a3d--------------------------------)

Published in

[Portis

](https://medium.com/portis?source=post_page-----
795db1f8a3d--------------------------------)

[![portis](https://miro.medium.com/fit/c/96/96/1*nMh3K62zk5kXXR9gtGhLQQ.png)](/@portis?source=post_page
-----795db1f8a3d--------------------------------)

[portis](/@portis?source=post_page-----
795db1f8a3d--------------------------------)

Follow

Aug 9, 2019

·

6 min read

# The UX of TX

## Network fees for blockchain transactions are notoriously difficult to
explain to mainstream users. The Gas Station Network allows DApps to foot the
gas bill. Problem solved, right? Not quite.

![](https://miro.medium.com/max/1400/1*zNRkCnMV6FNaqpRPedKqSg.jpeg)

Photo by [Wojtek
Witkowski](https://unsplash.com/@wojtek?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
on [Unsplash](https://unsplash.com/search/photos/road-
fog?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

# Ain’t Nobody Paying Your AWS Fees

Whenever we discuss the hard parts of blockchain UX, the two issues that
always stand out are **private key management** and **network fees**. This
post is about the latter.

## Users don’t like network fees

Network fees are confusing and feel out of place. Even if users do understand
why they’re needed, they might get upset about the whole idea. After all, in
the familiar world of web2, they aren’t paying anyone to use web apps, so this
requirement can create antagonism towards your DApp.

## The friction is real

Paying gas fees requires users to get their hands on some ETH, which means
going through KYC and buying a lot more than they need just for gas. All of
this, even if they only want to interact with your DApp, not necessarily buy
something.

![](https://miro.medium.com/max/598/1*k6B70CmRndD9D3U_g3cW1Q.gif)

“There has to be a better way!”

# “Free Rides!”

In the early days of Portis, we were determined to let users experience the
true potential of DApps. We wanted to get around the issue of network fees, so
we simply gave each new user $1 of ETH for free.

Scalable? Hell no. Abusable? You bet.

But it did the trick. DApp owners loved it since it gave their users an
opportunity to actually use their DApp with minimal friction.

At some point, despite our phone verification process, the abuse became too
costly to manage (in some countries, it’s well worth your time to go to great
lengths of trouble for $1 of free ETH), so we had to shut it down.

## Nevertheless, our little experiment was a success

We saw that once you remove the friction of network fees, churn is reduced
significantly.

> After all, the difference between 1 cent and free is more than just 1 cent.

# Introducing MetaTx

In September 2018, while we were still giving out $1 of free ETH to new Portis
users, a group of people in ETHBerlin were discussing the same issue of
network fees and how it might be solved using something called Meta
Transactions (or MetaTx for short). This group would go on to become the
[MetaCartel](https://www.metacartel.org/).

From conference to hackathon to meetup, discussions continued, and this group
grew in size, as more and more developers were eager to solve this challenge
in an elegant fashion.

![](https://miro.medium.com/max/1400/0*BqkXhKvj9upwya5W)

MetaCartel dinner during DevCon 4. The two guys sitting to the right of the
guy standing up in the colorful sweater? Portis co-founders Tom and Itay :)

# “Do You Accept the Charges?”

Since the DApps themselves sponsor the users’ gas fees, we like to compare
MetaTxs to collect calls. The user is trying to make a call to the DApp’s
smart contract, and the DApp is the one picking up the tab for the call by
agreeing to accept the charges (in theory, it can be anyone accepting the
charges, but we believe it will be mostly DApps, and perhaps also wallet
providers).

![](https://miro.medium.com/max/1000/0*N_tcpsY34UB2aRtW)

Instead of asking users to deposit gas money in their wallets so they can
submit transactions to the network, they only need to sign messages that
convey what a regular transaction would have done. A “gasless transaction” if
you will.

Those signed messages are sent to a relayer using a regular HTTP API endpoint.
The relayer then wraps the message inside a MetaTx, paying the gas fees for
both the user’s original message/transaction and the newly wrapped
transaction.

![](https://miro.medium.com/max/1400/1*lfu4U1ykW_6dktb1sN3mrQ.png)

The DApp smart contract knows how to handle this MetaTx, unwrapping it and
executing the content of the message as if it was a regular transaction.

At first, this seems like a terrific solution, but further investigation
reveals plenty of difficult challenges, mainly revolving around centralization
and synchronization.

The [Gas Station Network](https://github.com/tabookey/tabookey-gasless)
(developed by the amazing team at
[TabooKey](https://twitter.com/TabooKeyNet)), which we talked about in a
[previous post](/@portis/sponsor-your-users-gas-fees-with-portis-and-tabookey-
s-gas-stations-network-7fd7c8406869), solves these challenges and provides a
robust and decentralized way of sponsoring users’ network fees.

# Less Is More

We got the GSN hooked up to Portis (Ropsten only, mainnet coming **very**
soon. Update: **mainnet is live!** ), and the experience in our demo DApp
[CryptoPuppers](https://cryptopuppers.portis.io/) was amazing: a brand new
user could write to the blockchain for free in seconds! Couple that with the
smooth Portis onboarding experience and we have removed literally all
friction. A few clicks are all it takes to interact with a smart contract.
Outstanding!

## Once we finished geeking out, our first dilemma was “so… what do we write
under network fees?”

One approach was to simply show nothing. After all, when you upload an image
to Instagram or book an apartment on Airbnb, the app doesn’t tell you that
they’ve just paid $0.000001 for AWS on your behalf.

On the other hand, gas fees wouldn’t necessarily always be free. Some DApps
won’t sponsor them. Others might only sponsor gas fees for specific actions
and/or certain users. We like our UI to be consistent.

![](https://miro.medium.com/max/770/1*a4Xivrsdsq3H7dsjxND49g.png)

“Look Ma, No Gas!”

A decision was made — under “network fees” we will write down “Free”. We
believed DApps might also wish to convey to the user that they have sponsored
their gas fees, as this is still not the norm everywhere.

# A Match Made In Heaven

In our quest to offer users the best blockchain UX possible, we released a
feature last year called “Trust this App”, which we [explained
here](/coinmonks/restoring-user-trust-in-dapps-bfa83ab47452).

As a user, trusting a specific app means you won’t need to manually confirm
each action through Portis, as long as you’re only paying small amounts for
network fees. Portis will keep track of users’ network fee expenses, and if
they exceed $1 per hour, they will revert to using manual confirmations.

The Gas Station Network makes sure that last part will never occur (as DApps
are footing the gas bill for each transaction), meaning that by combining
these two features (gas sponsoring + trust this app) we can finally offer end-
users a web3 experience that feels like web2.

![](https://miro.medium.com/max/810/1*vex1CwwGY6tGcfJJvNDjUQ.gif)

# Simple. Secure. Seamless.

There are many scenarios that need to be considered, such as what happens when
the DApp turns off the relay (or it runs out of funds), which users are worthy
of being sponsored, and many more.

Luckily we have a wonderful community of DApp developers to brainstorm with
and figure out solutions to these challenges, so we can provide users with
solutions that are both secure and simple to understand.

We’re looking forward to exploring these uncharted territories with our
partners, paving together the path of least resistance to the blockchain.

Make sure you also check the [GSN website](https://gsn.openzeppelin.com/)
built by the terrific team at
[Zeppelin](https://medium.com/u/4e5199c3ee0a?source=post_page-----
795db1f8a3d--------------------------------).

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

1

\--

\--

1

## [More from Portis](/portis?source=post_page-----
795db1f8a3d--------------------------------)

Making blockchains simple for users

[Read more from Portis](/portis?source=post_page-----
795db1f8a3d--------------------------------)

## Recommended from Medium

[[![Jon
Law](https://miro.medium.com/fit/c/40/40/1*3tnp2dkCJWDFg-w8wpp9ig.png)](/@jonwlaw?source=post_internal_links
---------0----------------------------)

[Jon Law

](/@jonwlaw?source=post_internal_links---------0----------------------------)

## Cryptocurrency Explained: Blockchain

](/@jonwlaw/cryptocurrency-explained-
blockchain-a7ee58f7a070?source=post_internal_links---------
0----------------------------)

[[![PhotoChromic](https://miro.medium.com/fit/c/40/40/1*qMbvIhlf2u4PkhvlKCC0bg.png)](/@photochromic?source=post_internal_links
---------1----------------------------)

[PhotoChromic

](/@photochromic?source=post_internal_links---------
1----------------------------)

in

[Photochromic

](https://medium.com/photochromic?source=post_internal_links---------
1----------------------------)

## PhotoChromic Private Sale Spotlight

![](https://miro.medium.com/focal/112/112/50/50/1*6cj2xCCMCFPrVxDAWSn0Lw.jpeg)](/photochromic/photochromic-
private-sale-spotlight-afe80c962ede?source=post_internal_links---------
1----------------------------)

[[![Danda
Thor](https://miro.medium.com/fit/c/40/40/0*2Gh8G9CnJFlZGSTC.jpg)](/@dandathor?source=post_internal_links
---------2----------------------------)

[Danda Thor

](/@dandathor?source=post_internal_links---------
2----------------------------)

## AMA RECAP : CRYPTO MALLU CLUB x META VISA

![](https://miro.medium.com/focal/112/112/50/50/1*4dIPdCeWg280X6WHvXK8tQ.png)](/@dandathor/ama-
recap-crypto-mallu-club-x-meta-visa-3908909de028?source=post_internal_links
---------2----------------------------)

[[![Jayson
Berryhill](https://miro.medium.com/fit/c/40/40/0*ubT1cEBwaf74Iory.jpeg)](/@jaysonberryhill?source=post_internal_links
---------3----------------------------)

[Jayson Berryhill

](/@jaysonberryhill?source=post_internal_links---------
3----------------------------)

in

[Wholechain®

](https://medium.com/wholechain?source=post_internal_links---------
3----------------------------)

## Wholechain works on GS1 standards to achieve interoperability with leading
blockchain traceability…

![](https://miro.medium.com/focal/112/112/50/50/1*k_Rmr6DfxGgV2708Hc3Q6g.png)](/wholechain/wholechain-
works-on-gs1-standards-to-achieve-interoperability-with-leading-blockchain-
traceability-6baa102ff068?source=post_internal_links---------
3----------------------------)

[[![Vulkania](https://miro.medium.com/fit/c/40/40/1*xtiA3Ks9Iw_tcf-M-
MTERw.png)](/@vulkania?source=post_internal_links---------
4----------------------------)

[Vulkania

](/@vulkania?source=post_internal_links---------4----------------------------)

## Vulkania.io Roadmap for Q4 2021

![](https://miro.medium.com/focal/112/112/50/50/1*xzj4uxQHAZYmexUB9c3EXQ.jpeg)](/@vulkania/vulkania-
io-roadmap-for-q4-2021-6ec1952ac1b0?source=post_internal_links---------
4----------------------------)

[[![BENQI](https://miro.medium.com/fit/c/40/40/1*zNwDSxgp23kzsvionO5M_Q.png)](/@benqifinance?source=post_internal_links
---------5----------------------------)

[BENQI

](/@benqifinance?source=post_internal_links---------
5----------------------------)

## John Nahas and Wilson Wu joins BENQI as Strategic Advisors

![](https://miro.medium.com/focal/112/112/50/50/0*lyRaQWe5BC8STbzs)](/@benqifinance/john-
nahas-and-wilson-wu-joins-benqi-as-strategic-
advisors-45a837f3629f?source=post_internal_links---------
5----------------------------)

[[![4NTS
Guild](https://miro.medium.com/fit/c/40/40/1*DKkCIyQyVvAvs7tHXME7Fg.png)](/@royo-4nts?source=post_internal_links
---------6----------------------------)

[4NTS Guild

](/@royo-4nts?source=post_internal_links---------
6----------------------------)

in

[NEAR Protocol

](https://medium.com/nearprotocol?source=post_internal_links---------
6----------------------------)

## NEAR Joins ICON’s BTP Ecosystem

![](https://miro.medium.com/focal/112/112/50/50/1*q4TVF_VLW7gTUG2dEIDvAw.png)](/nearprotocol/near-
joins-icons-btp-ecosystem-97c3d8c2b1fc?source=post_internal_links---------
6----------------------------)

[[![Matthew
Mills](https://miro.medium.com/fit/c/40/40/1*mH8hZcpbBCS8yg-8f-v6rw.png)](/@millsmgb?source=post_internal_links
---------7----------------------------)

[Matthew Mills

](/@millsmgb?source=post_internal_links---------7----------------------------)

in

[myStake

](https://medium.com/mystake?source=post_internal_links---------
7----------------------------)

## Introducing myStake

![](https://miro.medium.com/focal/112/112/50/50/1*W1uGB8vGMAt8DFecNdZocw.png)](/mystake/introducing-
mystake-8f0cf607b209?source=post_internal_links---------
7----------------------------)

[](/?source=post_page-----795db1f8a3d--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
795db1f8a3d--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
795db1f8a3d--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
795db1f8a3d--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
795db1f8a3d--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----795db1f8a3d--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----795db1f8a3d--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fportis%2Fthe-
ux-of-tx-795db1f8a3d&source=post_page--------------------------
nav_reg-----------)

[![portis](https://miro.medium.com/fit/c/176/176/1*nMh3K62zk5kXXR9gtGhLQQ.png)](/@portis)

[

## portis

](/@portis)

433 Followers

<https://portis.io>

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F4462dd2c963a&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fportis%2Fthe-
ux-of-
tx-795db1f8a3d&newsletterV3=56bd0a809585&newsletterV3Id=4462dd2c963a&user=portis&userId=56bd0a809585&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Monte
Singman](https://miro.medium.com/fit/c/40/40/0*Q1B7_rWDa9Mn2lAD.)](/@msingman?source=read_next_recirc
---------0---------------------1d731e8c_d2c7_452b_b267_95fc38ac408f-------)

[Monte Singman

](/@msingman?source=read_next_recirc---------0---------------------
1d731e8c_d2c7_452b_b267_95fc38ac408f-------)

## Making games with empathy

![](https://miro.medium.com/focal/112/112/50/50/1*atq1SOBjFiOJhk1-AJVY3Q.png)](/@msingman/making-
games-with-empathy-d42b363796e8?source=read_next_recirc---------0
---------------------1d731e8c_d2c7_452b_b267_95fc38ac408f-------)

[[![Salt Design
Studio](https://miro.medium.com/fit/c/40/40/1*skqv2KVm5hpaLZTgBC7UvA.png)](/@saltdesignstudio?source=read_next_recirc
---------1---------------------1d731e8c_d2c7_452b_b267_95fc38ac408f-------)

[Salt Design Studio

](/@saltdesignstudio?source=read_next_recirc---------1---------------------
1d731e8c_d2c7_452b_b267_95fc38ac408f-------)

## Designing tools/apps for UI UX designers

![](https://miro.medium.com/focal/112/112/50/50/1*hyFZJpI5UFRMe7tu0U0iZg.png)](/@saltdesignstudio/designing-
tools-apps-for-ui-ux-designers-952a039294d3?source=read_next_recirc---------1
---------------------1d731e8c_d2c7_452b_b267_95fc38ac408f-------)

[[![Alvin Chai](https://miro.medium.com/fit/c/40/40/1*MU2DiQuWpAZEM-
KKTPjDBw.jpeg)](/@alvin_67836?source=read_next_recirc---------2
---------------------1d731e8c_d2c7_452b_b267_95fc38ac408f-------)

[Alvin Chai

](/@alvin_67836?source=read_next_recirc---------2---------------------
1d731e8c_d2c7_452b_b267_95fc38ac408f-------)

## What is UX Design?

![UX
Design](https://miro.medium.com/focal/112/112/50/50/1*tQlIutkDjpoDKIWoQiKGsw.jpeg)](/@alvin_67836/what-
is-ux-design-2d464e91f0e?source=read_next_recirc---------2
---------------------1d731e8c_d2c7_452b_b267_95fc38ac408f-------)

[[![Amanda
Batista](https://miro.medium.com/fit/c/40/40/1*Jtp60g8OPUyyOAL9lOIiIA.jpeg)](/@aabatista?source=read_next_recirc
---------3---------------------1d731e8c_d2c7_452b_b267_95fc38ac408f-------)

[Amanda Batista

](/@aabatista?source=read_next_recirc---------3---------------------
1d731e8c_d2c7_452b_b267_95fc38ac408f-------)

## UX/UI Case study — Freelancer app

![](https://miro.medium.com/focal/112/112/50/50/0*HpPBpsmrrqUTHoi5.png)](/@aabatista/ux-
ui-case-study-freelancer-app-2f25831fe83d?source=read_next_recirc---------3
---------------------1d731e8c_d2c7_452b_b267_95fc38ac408f-------)

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

