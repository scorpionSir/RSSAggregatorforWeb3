[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/7ebb87d1fa22&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Mysterium
Network](https://miro.medium.com/fit/c/64/64/1*17ydm95DmW8qBxy7RmyVdg.png)](https://medium.com/mysterium-
network?source=post_page-----7ebb87d1fa22--------------------------------)

Published in

[Mysterium Network

](https://medium.com/mysterium-network?source=post_page-----
7ebb87d1fa22--------------------------------)

[![Roberto
Vis](https://miro.medium.com/fit/c/96/96/0*RSohKtHvz8Hd5X5D.jpg)](/@robertovis?source=post_page
-----7ebb87d1fa22--------------------------------)

[Roberto Vis](/@robertovis?source=post_page-----
7ebb87d1fa22--------------------------------)

Follow

Nov 12, 2019

·

7 min read

# Introducing the Mysterium Payment System

![](https://miro.medium.com/max/1400/1*8LsfD_7xAntynvEbSZzaeQ.png)

We are excited to announce we’re drawing closer to launching payments on
Mysterium Network.

Payments are a crucial element of Mysterium Network. As such, we needed to
design a solution which was capable of meeting real world requirements of
scalability and affordability. This system also had to comply with the ethos
of decentralised ecosystems. These are two opposing forces, with no solution
fit for Mysterium Network readily available in the market.

There was no easy way around it for us. But we believe we found a solution
that fits these requirements.

This is more than just an exciting milestone for Mysterium Network We have
worked extensively towards this moment for the better part of the year and are
almost ready to deploy it.

# Core challenges in designing payments for Mysterium Network:

Payments in Mysterium Network need to be lightweight and fast while honouring
the core fundamentals of blockchain-systems: transparency, fairness, openness,
protection from double-spending and fraud. It has to do all of this without
relying on any centralised entity — making it trustless.

This trustless element has been the hardest goal to achieve by far, yet the
most crucial.

Once deployed, payments will ensure that users can transact with one another
autonomously, without a need for an intermediary (including us). If our
attempt is successful — users won’t have to trust each other either. Instead,
they will trust in the network’s built-in economic game which is designed to
incentivise everyone to cooperate. [(Learn more about the distributed
trustless ethos here)](/@preethikasireddy/eli5-what-do-we-mean-by-blockchains-
are-trustless-aa420635d5f6).

Very soon we will start to introduce various components of Mysterium payments
onto the testnet, so you can experiment and become familiar with how it’s all
going to work (more on this later in this blogpost). Eventually, the goal is
to launch on the Mainnet with MYST tokens.

We work relentlessly towards such high standards because we believe it will
help achieve our mission — to provide a secure and open internet for all. We
understand the potential power of decentralized technologies to bring value
and opportunity to people everywhere, but making them usable in real-world
conditions is a challenge not solved by many so far.

![](https://miro.medium.com/max/1400/0*gPfvfw8Qd4YCBT9D.png)

# Our quest to find the best P2P payment system

The architecture of our payments system is a fusion of research and
experimentation with existing Layer 2 solutions. This eventually led to us
building a homegrown one, based on all our findings.

It first began as a research and development project as we strived to find the
best design for fast, secure and trustless P2P payments. While blockchain
payments are (generally) secure,[ censorship-
resistant](https://www.quora.com/What-does-censorship-resistance-mean-in-the-
context-of-blockchain), and have an open and
[permissionless](https://coincenter.org/entry/what-does-permissionless-mean)
APIs, they’re still relatively expensive and slow. And that just didn’t work
in our case.

This lack of scalability — a network’s ability to grow and handle a growing
number of users — means at a certain size the network will get clogged up by
all the transactions being processed. Due to this, an Ethereum transaction
could cost up to one dollar and take a couple of hours to be ‘settled’ in a
block. These transactions get even more expensive when the network’s
processing capacity becomes saturated. These limitations are unsuitable for
the VPN service provided by Mysterium Network, which require fast, frequent
and very small transactions — known as micropayments — executed on a global
scale.

We analysed various Layer 2 solutions — independent networks or chains running
‘on top’ of the original blockchain to avoid it becoming too crowded. But none
of these fit our particular use case. They were either still in their very
early stage of development, too insecure or overly complex, or built for
general use cases, making them non-optimal for Mysterium Network’s use case.
These barriers led us to start working on a completely new payment system from
scratch.

Developing a unique P2P payment system is not an easy task. Our goal was to
create infrastructure which best serves the needs of both consumers of
Mysterium Network, and nodes in the network.

Here are the main requirements of our proposed system:

  1. High throughput — the network’s ability to handle frequent and small payments (eventually thousands per second)
  2. Support for our native utility token, MYST
  3. Anonymity while also being secure, such as through the use of identity registration and reputation system
  4. Great user experience, removing as much complexity as possible for the end-user.

Going back to the trust conundrum, we also had to consider that _consumers_
won’t pay a large amount of up-front and the service _providers_ (nodes) are
unlikely to offer their services without prepayment.

This is why we use a micropayment system, which lets nodes offer their service
in short intervals, such as 20 seconds or 5 minutes. This pay-as-you-go model
means that participants can start transacting straight away. A user can pay
for a VPN service a couple of times per minute, sending (and therefore
risking) only tiny amounts of tokens in exchange for the bandwidth they are
renting.

![](https://miro.medium.com/max/1400/0*s6v8ipa_W7Hb8I8P.png)

# The “Mysterium Accountant” concept and an introduction to payment promises
(digital IOUs)

Our proposed solution fuses the technologies and methodologies used by other
payment solutions, such as State Channels. However, we are introducing a new
party to the network called “Mysterium Accountant”. The Accountant will verify
‘payment promises’ made by consumers to nodes.

![](https://miro.medium.com/max/1400/0*8tY0EkLmKPixaHLM.png)

Instead of users constantly paying nodes in high volumes, consumers can make
‘promises’ to providers, similar to IOUs. These promises are “verified” by
Mysterium Accountant. The Accountant has a record of each consumer’s actual
balance and funds, as well as a record of all of the promises made. When node
runners decide they want to settle the account, the final tallied record is
executed on the blockchain and sent as a single transaction.

Mysterium Accountant plays a similar role to a ‘hub’ between consumers and
nodes. In saying that, it cannot use or freeze user funds. It’s only function
is to verify the payment promises. This introduction of the “Mysterium
Accountant” also takes our network one step closer towards becoming a
trustless service.

As these micropayments are ‘promises’, rather than on-chain payments, we
reduce the amount of transactions sent to the blockchain. This allows the
network to handle much larger volumes of users and transactions, making our
network faster and more scalable. This is our lightweight solution for
micropayments. With it, we aim to provide hundreds of thousands of
transactions per second!

![](https://miro.medium.com/max/1400/0*bk-bOnDsaJ5dQrlS.png)

To make sure we still honour decentralization, we designed the system in a way
so there can be multiple Accountants existing in the network at the same time.
It’s a very broad concept to explain within one post, so more will follow with
much deeper explanations.

You can also dive deeper into specific concepts in our [micropayments
whitepaper.](https://github.com/mysteriumnetwork/payments-smart-
contracts/blob/master/docs/paper/accountant-pattern.pdf)

![](https://miro.medium.com/max/1400/0*szwoiDps2RJr_f4w.png)

# What happens next?

We’re currently working to implement this payment solution on our testnet. You
will gradually see payment options in our various interfaces and applications.
At first, as we migrate to this new payment model, nodes and users won’t have
to do anything. Eventually, you might see various engagement elements, such as
a ‘top-up’ button in a Mysterium app, new functionality in SDKs and so on.

Upon launch, we will assign newly minted tokens to each user on the testnet so
you can experiment and play with this system. As with all new technologies,
there will be an ongoing process of revising and iterating. We hope to learn a
great deal about possible use cases, edge cases, abuse angles and on and on.
We welcome your play and feedback, as it will be vital for us in getting ready
to release usable and secure payments on the mainnet with actual tokens.

 _With the introduction of payments on mainnet, we aim to create an incentive
for both consumers and nodes to meet on the Network on fair terms._

Eventually, Node runners will begin to receive tokens as they rent their
bandwidth, applying a pay-per-use model, moving away from monthly bounties.
Future payment and charging models may be adapted as our network starts to
operate in real-world market conditions. Nodes will be able to withdraw funds
to their wallets.

As the whole network will be open, it will open up the possibility for anyone
to create better user-oriented apps, incorporate privacy into all sorts of
services, create a better user experience for withdrawing earnings, add more
use-cases for nodes, and more.

A big thank you to our current node runners, who are the backbone of our
network and are helping us to build the foundations for an open and uncensored
internet.

If you’re not yet part of our network, [learn more about becoming a node
runner](https://mysterium.network/2019/07/11/the-definitive-guide-to-being-a-
mysterium-node/), or [download our software here](https://mysterium.network/).

[Original article](https://mysterium.network/2019/11/04/introducing-mysterium-
payment-system/) posted on [Mysterium Network’s
blog](https://mysterium.network/blog/).

[![](https://miro.medium.com/max/1360/1*KVemUIEgTpc-
zXcp0L3hjQ.jpeg)](https://mailchi.mp/mysterium.network/newsletter)[![](https://miro.medium.com/max/1360/1*oQQM-0ehwV3qaOQVLyUHfQ.jpeg)](https://discord.me/mysterium)

[![](https://miro.medium.com/max/1360/1*lEacU_01BunT2KNjtTv4QA.jpeg)](https://twitter.com/MysteriumNet)[![](https://miro.medium.com/max/1360/1*x369MiNvI6Tg3BqAp9uhcg.png)](https://www.youtube.com/channel/UCBxzWnZEHvuj-
nfP00YImHQ)[![](https://miro.medium.com/max/1360/1*hXGcxWk6fFWeh-
MqlwhoZg.jpeg)](https://t.me/mysterium_network)

\--

\--

\--

## [More from Mysterium Network](/mysterium-network?source=post_page-----
7ebb87d1fa22--------------------------------)

Decentralized VPN built on blockchain - https://mysterium.network

[Read more from Mysterium Network](/mysterium-network?source=post_page-----
7ebb87d1fa22--------------------------------)

## Recommended from Medium

[[![Remme](https://miro.medium.com/fit/c/40/40/1*-1hRy266JYZUElqW7ugx-w.png)](/@remme?source=post_internal_links
---------0----------------------------)

[Remme

](/@remme?source=post_internal_links---------0----------------------------)

in

[Remme Protocol

](https://medium.com/remme?source=post_internal_links---------
0----------------------------)

## Blockchain for Web 3.0.

![](https://miro.medium.com/focal/112/112/50/50/1*0HEcUnKx5WJN2rlZU9FLnQ.png)](/remme/blockchain-
for-web-3-0-a2b94582caef?source=post_internal_links---------
0----------------------------)

[[![PAID
NETWORK](https://miro.medium.com/fit/c/40/40/1*wqdbpdDng3d4vMn8TWZRSg.jpeg)](/@paidnetwork?source=post_internal_links
---------1----------------------------)

[PAID NETWORK

](/@paidnetwork?source=post_internal_links---------
1----------------------------)

## The $PAID BSC Bridge is Now Up and Running!

![](https://miro.medium.com/focal/112/112/50/50/0*OFGausZXhMyqDSG9)](/@paidnetwork/the-
paid-bsc-bridge-is-now-up-and-running-7bb58703a08a?source=post_internal_links
---------1----------------------------)

[[![Bears
Deluxe](https://miro.medium.com/fit/c/40/40/1*OepiBXgjhqRSMFic9V0UTw.png)](/@bearsdeluxe?source=post_internal_links
---------2----------------------------)

[Bears Deluxe

](/@bearsdeluxe?source=post_internal_links---------
2----------------------------)

## A Brief History of Bears Deluxe

![](https://miro.medium.com/focal/112/112/50/50/1*WplxaOrRfPTKKERtcjN4_Q.png)](/@bearsdeluxe/a-brief-
history-of-bears-deluxe-37390fc3af4a?source=post_internal_links---------
2----------------------------)

[[![Pist
Trust](https://miro.medium.com/fit/c/40/40/1*04AdM1u6HAZGRQaZeYwtYA.jpeg)](/@pist-
trust?source=post_internal_links---------3----------------------------)

[Pist Trust

](/@pist-trust?source=post_internal_links---------
3----------------------------)

## PIST TRUST Mainnet Launched!

![](https://miro.medium.com/focal/112/112/50/50/1*QhhSxb72YDkFcMdA19eDag.png)](/@pist-
trust/pist-trust-mainnet-launched-3b7e882b38a?source=post_internal_links
---------3----------------------------)

[[![Oen Soem](https://miro.medium.com/fit/c/40/40/1*MQyx9krUrNMV-
DrmtxsewQ.jpeg)](/@soemoen1206?source=post_internal_links---------
4----------------------------)

[Oen Soem

](/@soemoen1206?source=post_internal_links---------
4----------------------------)

## Gaimin- Blockchain Powered Gaming Platform Which Connects The World.

![](https://miro.medium.com/focal/112/112/50/50/1*e4Q_Qm9hpk8TPsSZGzcQQg.png)](/@soemoen1206/gaimin-
blockchain-powered-gaming-platform-which-connects-the-
world-9a49df4c4556?source=post_internal_links---------
4----------------------------)

[[![Kamal
Pandey](https://miro.medium.com/fit/c/40/40/1*CPtGP4tt_1H-p1ugTll5Ng.jpeg)](/@kamallpandey?source=post_internal_links
---------5----------------------------)

[Kamal Pandey

](/@kamallpandey?source=post_internal_links---------
5----------------------------)

## The Top 5 Crypto Metaverse Projects on Solana Blockchain

![](https://miro.medium.com/focal/112/112/50/50/0*BtvYHqHkYTVLE_9P.jpg)](/@kamallpandey/the-
top-5-crypto-metaverse-projects-on-solana-
blockchain-4dbf89bbd7ba?source=post_internal_links---------
5----------------------------)

[[![Propy](https://miro.medium.com/fit/c/40/40/1*ytYb9equg6sC6Sr4VdEcCQ.png)](/@propy?source=post_internal_links
---------6----------------------------)

[Propy

](/@propy?source=post_internal_links---------6----------------------------)

in

[Propy

](https://medium.com/propy?source=post_internal_links---------
6----------------------------)

## Propy Global Ambassadors Program

![](https://miro.medium.com/focal/112/112/50/50/1*hwTCx-
qenGA4gsejmzqJYw.png)](/propy/who-else-wants-to-modernize-the-real-estate-
market-5b1079b752b6?source=post_internal_links---------
6----------------------------)

[[![Jefrey S. Santos](https://miro.medium.com/fit/c/40/40/1*VI-
ikJLanC_tji0FO_3jmA.jpeg)](/@jefreysantos?source=post_internal_links---------
7----------------------------)

[Jefrey S. Santos

](/@jefreysantos?source=post_internal_links---------
7----------------------------)

in

[Capitual

](https://medium.com/capitual?source=post_internal_links---------
7----------------------------)

## 5 Industries That Will Benefit The Most From Blockchain Technology

![](https://miro.medium.com/focal/112/112/50/50/1*UdBhNnKkwrvC1wQfNLigWg.jpeg)](/capitual/5-industries-
that-will-benefit-the-most-from-blockchain-
technology-19d4cff1d459?source=post_internal_links---------
7----------------------------)

[](/?source=post_page-----7ebb87d1fa22--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
7ebb87d1fa22--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
7ebb87d1fa22--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
7ebb87d1fa22--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
7ebb87d1fa22--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----7ebb87d1fa22--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----7ebb87d1fa22--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fmysterium-
network%2Fintroducing-the-mysterium-payment-
system-7ebb87d1fa22&source=post_page--------------------------
nav_reg-----------)

[![Roberto
Vis](https://miro.medium.com/fit/c/176/176/0*RSohKtHvz8Hd5X5D.jpg)](/@robertovis)

[

## Roberto Vis

](/@robertovis)

1.4K Followers

Helping build an ecosystem of Empowerment.

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F5e9e7bc80970&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fmysterium-
network%2Fintroducing-the-mysterium-payment-
system-7ebb87d1fa22&newsletterV3=af677b29d743&newsletterV3Id=5e9e7bc80970&user=Roberto+Vis&userId=af677b29d743&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Francesco
Passanti](https://miro.medium.com/fit/c/40/40/1*V3xXZ6hTIdHVoOQzsOs-
Pw.jpeg)](/@francescopassanti?source=read_next_recirc---------0
---------------------4ebce3a6_6ef8_419f_b611_14c951661ea1-------)

[Francesco Passanti

](/@francescopassanti?source=read_next_recirc---------0---------------------
4ebce3a6_6ef8_419f_b611_14c951661ea1-------)

## Geolocation on Cloudflare Workers

![](https://miro.medium.com/focal/112/112/50/50/1*HMNjtNOqNGBKt76qInaZOw.png)](/@francescopassanti/geolocation-
on-cloudflare-workers-f1447da3ac5d?source=read_next_recirc---------0
---------------------4ebce3a6_6ef8_419f_b611_14c951661ea1-------)

[[![Andrew
Cachia](https://miro.medium.com/fit/c/40/40/1*KPfMDAEZyTctuAWOnCGQcQ.png)](/@andcachia?source=read_next_recirc
---------1---------------------4ebce3a6_6ef8_419f_b611_14c951661ea1-------)

[Andrew Cachia

](/@andcachia?source=read_next_recirc---------1---------------------
4ebce3a6_6ef8_419f_b611_14c951661ea1-------)

## Allowing admin users to decide who should and shouldn’t receive daily push
notifications

![](https://miro.medium.com/focal/112/112/50/50/1*dZC4RFF1sSNzeC9lBLqNGw.png)](/@andcachia/allowing-
admin-users-to-decide-who-should-and-shouldnt-receive-daily-push-
notifications-2b5fcbe4b0fb?source=read_next_recirc---------1
---------------------4ebce3a6_6ef8_419f_b611_14c951661ea1-------)

[[![OMNUUM](https://miro.medium.com/fit/c/40/40/1*9pxqed8ExmdwaqyUynmgfA.png)](/@omnuum?source=read_next_recirc
---------2---------------------4ebce3a6_6ef8_419f_b611_14c951661ea1-------)

[OMNUUM

](/@omnuum?source=read_next_recirc---------2---------------------
4ebce3a6_6ef8_419f_b611_14c951661ea1-------)

in

[OMNUUM

](https://medium.com/omnuum?source=read_next_recirc---------2
---------------------4ebce3a6_6ef8_419f_b611_14c951661ea1-------)

## [Features] How To Get Hacked

![](https://miro.medium.com/focal/112/112/50/50/1*65mNZahFF9sTIaVjGv5OdQ.png)](/omnuum/features-
how-to-get-hacked-96e0ae79cb3e?source=read_next_recirc---------2
---------------------4ebce3a6_6ef8_419f_b611_14c951661ea1-------)

[[![MegaFans](https://miro.medium.com/fit/c/40/40/1*u2V8ZMIWfqqRKC7mD685uw.png)](/@MegaFans?source=read_next_recirc
---------3---------------------4ebce3a6_6ef8_419f_b611_14c951661ea1-------)

[MegaFans

](/@MegaFans?source=read_next_recirc---------3---------------------
4ebce3a6_6ef8_419f_b611_14c951661ea1-------)

## MegaFans Now in Four Major App Stores Globally

](/@MegaFans/megafans-now-in-four-major-app-stores-globally-
cbe1dade78ce?source=read_next_recirc---------3---------------------
4ebce3a6_6ef8_419f_b611_14c951661ea1-------)

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

