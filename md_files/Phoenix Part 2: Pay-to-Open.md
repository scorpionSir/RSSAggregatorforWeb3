[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/4a8a482dd4d&~feature=LoOpenInAppButton&~channel=ShowPostUnderUser&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![ACINQ](https://miro.medium.com/fit/c/96/96/1*C_yfYIhszWi885XNVFxnkg.png)](/@ACINQ?source=post_page
-----4a8a482dd4d--------------------------------)

[ACINQ](/@ACINQ?source=post_page-----
4a8a482dd4d--------------------------------)

Follow

Dec 12, 2019

·

3 min read

# Phoenix Part 2: Pay-to-Open

 **TL; DR:** When you receive a Lightning payment, we will automatically and
instantly create a channel to you if needed, solving the inbound liquidity
issue.

Let’s suppose you just installed Phoenix. Your balance is zero, you have no
channels. How can you receive your first payment? It’s easy: just go to the
_receive_ tab and display a LN payment request.

![](https://miro.medium.com/max/520/1*XsCJKI7eR6yujtWC5RWD7w.gif)

Wait, what just happened? How was the sender able to route a payment to you if
there was no channel to route to? Let’s see what happened.

The way Lightning works, payments are routed through channels, which could be
public or private. Public channels are announced as part of the gossip between
Lightning nodes. Private channels are not announced and only known by their
initiators, but information about them can be attached to Lightning invoices
as _routing hints_. For example, all channels created by Eclair Mobile are
private, and a Lightning invoice created on Eclair Mobile will contain routing
hints for your existing private channels.

 **Phoenix uses those _routing hints_ to tell the sender how to find a route,
even if there are no channels — public or private — in the first place**. To
do that, we leverage the fact that Phoenix is only connected to the ACINQ
node. This makes things very simple: Phoenix Wallet just needs to make up a
fake channel between the ACINQ node and itself, with a specially crafted
identifier, and add it to the invoice. The sender won’t notice anything, it
will build a route that goes to a certain number of nodes, then ACINQ, then
through the fake channel to Phoenix Wallet.

Now when the ACINQ node receives the payment onion, it will unwrap it and see
that it needs to forward it to a fake channel. Because of the way fake channel
identifiers are built, the ACINQ node will know that this isn’t a real
channel, and will also be able to know what the actual node identifier of the
Phoenix user is. Then two things can happen:

  * ACINQ already has existing channels with the target Phoenix Wallet: then it’s business as usual, and ACINQ will forward the payment through those channels.
  * There is no channel to this node, or there is not enough liquidity available in the existing channels. That’s where Pay-to-Open comes into play.

The Pay-to-Open feature works like this:

  1. ACINQ tells Phoenix that it has a pending incoming payment and it proposes to open a channel and push the amount corresponding to the payment on Phoenix Wallet’s side. There is a fee, essentially to cover the cost of the funding transaction for this new channel.
  2. Phoenix displays a pop-up asking the user whether they agree or not.
  3. If the user says “yes”, then Phoenix will send the _payment preimage_ to the ACINQ node.
  4. The ACINQ node will use the _preimage_ to pull funds from the sender, and will fund a new channel to Phoenix, with an initial balance for Phoenix set to the amount they agreed upon. Done!

Note also that with this scheme, the ACINQ node is the funder. In the current
version of Lightning, it means that ACINQ will have to pay the on-chain fees
for the commitment transaction if the channel closes unexpectedly.

This effectively solves the inbound liquidity issue on the wallet’s side.
**Instead of having to _a priori_ manage channel liquidity to make sure you
can receive a payment of a certain amount, you don’t have to do anything and
channels will be created when needed.**

This article is **part 2** of a series of articles introducing Phoenix. Other
articles in this series:

  * [Part 1: Introducing Phoenix](/@ACINQ/introducing-phoenix-5c5cc76c7f9e)
  * [Part 3: Backup](/@ACINQ/phoenix-wallet-part-3-backup-f63a9470d4e7)
  * [Part 4: Trampoline payments](/@ACINQ/phoenix-wallet-part-4-trampoline-payments-fb1befd027c8)

\--

2

\--

\--

2

## [More from ACINQ](/@ACINQ?source=post_page-----
4a8a482dd4d--------------------------------)

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fcb6983c5b91b&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ACINQ%2Fphoenix-
part-2-pay-to-
open-4a8a482dd4d&newsletterV3=74c0a4fc8ad0&newsletterV3Id=cb6983c5b91b&user=ACINQ&userId=74c0a4fc8ad0&source=-----4a8a482dd4d
---------------------subscribe_user-----------)

We are building an implementation of Lightning, a scalable instant payment
network built on top of the Bitcoin blockchain.

Love podcasts or audiobooks? Learn on the go with our new app.

[Try
Knowable](https://knowable.fyi/?utm_source=medium&utm_medium=referral&utm_campaign=medium-
post-footer&source=post_page-----4a8a482dd4d--------------------------------)

[](/?source=post_page-----4a8a482dd4d--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
4a8a482dd4d--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
4a8a482dd4d--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
4a8a482dd4d--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
4a8a482dd4d--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----4a8a482dd4d--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----4a8a482dd4d--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ACINQ%2Fphoenix-
part-2-pay-to-open-4a8a482dd4d&source=post_page--------------------------
nav_reg-----------)

[![ACINQ](https://miro.medium.com/fit/c/176/176/1*C_yfYIhszWi885XNVFxnkg.png)](/@ACINQ)

[

## ACINQ

](/@ACINQ)

1.1K Followers

We are building an implementation of Lightning, a scalable instant payment
network built on top of the Bitcoin blockchain.

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fcb6983c5b91b&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ACINQ%2Fphoenix-
part-2-pay-to-
open-4a8a482dd4d&newsletterV3=74c0a4fc8ad0&newsletterV3Id=cb6983c5b91b&user=ACINQ&userId=74c0a4fc8ad0&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Blockchain Hat](https://miro.medium.com/fit/c/40/40/1*F6DIGg-
By5Rj67kvHDoOfg.png)](/@blockchainhat?source=read_next_recirc---------0
---------------------45b6b363_0341_4a2e_8b61_5d783c9f6513-------)

[Blockchain Hat

](/@blockchainhat?source=read_next_recirc---------0---------------------
45b6b363_0341_4a2e_8b61_5d783c9f6513-------)

## Who gives the best DeFi lending protocol development?

![](https://miro.medium.com/focal/112/112/50/50/1*6y0peNXcanK4LsaPRRwntg.jpeg)](/@blockchainhat/who-
gives-the-best-defi-lending-protocol-
development-30ef0e0ad1a4?source=read_next_recirc---------0
---------------------45b6b363_0341_4a2e_8b61_5d783c9f6513-------)

[[![Bryant Jimin
Son](https://miro.medium.com/fit/c/40/40/1*hdt42F4Y1m3AWg2Ej8RNZg.jpeg)](/@bryantson?source=read_next_recirc
---------1---------------------45b6b363_0341_4a2e_8b61_5d783c9f6513-------)

[Bryant Jimin Son

](/@bryantson?source=read_next_recirc---------1---------------------
45b6b363_0341_4a2e_8b61_5d783c9f6513-------)

## Quantum computers will bring the extinction of Bitcoins and other
cryptocurrencies, and here is why

![](https://miro.medium.com/focal/112/112/50/50/1*2OWr42ytVg7rrMjypSjMiA.png)](/@bryantson/quantum-
computers-will-bring-the-extinction-of-bitcoins-and-other-cryptocurrencies-
and-here-is-why-37d179634615?source=read_next_recirc---------1
---------------------45b6b363_0341_4a2e_8b61_5d783c9f6513-------)

[[![Truflation](https://miro.medium.com/fit/c/40/40/1*hAFjyzQ9r_JI7VyrELxrzQ.jpeg)](/@truflation?source=read_next_recirc
---------2---------------------45b6b363_0341_4a2e_8b61_5d783c9f6513-------)

[Truflation

](/@truflation?source=read_next_recirc---------2---------------------
45b6b363_0341_4a2e_8b61_5d783c9f6513-------)

in

[Truflation

](https://medium.com/truflation?source=read_next_recirc---------2
---------------------45b6b363_0341_4a2e_8b61_5d783c9f6513-------)

## 5 Reasons Why DeFi Needs Fiat Inflation Data

![](https://miro.medium.com/focal/112/112/50/50/1*Da10Xt0iwdvtjHHTaOffDw.png)](/truflation/5-reasons-
why-defi-needs-fiat-inflation-data-afcd74b6af17?source=read_next_recirc
---------2---------------------45b6b363_0341_4a2e_8b61_5d783c9f6513-------)

[[![Ben J
Holcomb](https://miro.medium.com/fit/c/40/40/0*X3NOcH2RgDdy7K71.)](/@benjholcomb?source=read_next_recirc
---------3---------------------45b6b363_0341_4a2e_8b61_5d783c9f6513-------)

[Ben J Holcomb

](/@benjholcomb?source=read_next_recirc---------3---------------------
45b6b363_0341_4a2e_8b61_5d783c9f6513-------)

in

[CryptoStars

](https://medium.com/cryptostars?source=read_next_recirc---------3
---------------------45b6b363_0341_4a2e_8b61_5d783c9f6513-------)

## My Top Crypto Plays Going into 2022

![](https://miro.medium.com/focal/112/112/50/50/1*Yn_el1ve328aDDsHaWBDtw.png)](/cryptostars/my-
top-crypto-plays-going-into-2022-efb71bddebae?source=read_next_recirc---------
3---------------------45b6b363_0341_4a2e_8b61_5d783c9f6513-------)

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

