[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/c5a4ed05ca0f&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Mysterium
Network](https://miro.medium.com/fit/c/64/64/1*17ydm95DmW8qBxy7RmyVdg.png)](https://medium.com/mysterium-
network?source=post_page-----c5a4ed05ca0f--------------------------------)

Published in

[Mysterium Network

](https://medium.com/mysterium-network?source=post_page-----
c5a4ed05ca0f--------------------------------)

[![Jaro
Šatkevič](https://miro.medium.com/fit/c/96/96/0*N_2rIH7aXTX6mPW0.jpeg)](/@chompomonim?source=post_page
-----c5a4ed05ca0f--------------------------------)

[Jaro Šatkevič](/@chompomonim?source=post_page-----
c5a4ed05ca0f--------------------------------)

Follow

Dec 12, 2019

·

8 min read

# Lightweight solution for Mysterium Network micropayments

![](https://miro.medium.com/max/1400/1*8q2GyOkFUQUTH_Y4l7Iaiw.png)

I’d like to share research on micropayments solution which we on Mysterium
team are currently building to meet needs of decentralised VPN, CDN or
streaming solutions.

The ultimate goal of [_Mysterium Network_](https://mysterium.network) is to
become fully decentralized, peer to peer and anonymous by design. The nature
of such networks is that parties ( _consumers_ and _providers_ ) are anonymous
which leads to lack of trust of each other by default, such **trust** have to
be **provided** by **protocol and math**.

Considering _trustless_ nature of the network, and aiming to reduce any risk
of loosing money or providing service without being rewarded, the _consumer_
isn’t going to pay a large amount up-front and the service _provider_ will
unlikely offer their services without prepayment.

From this above mentioned scenario arises a need to split the service into
chunks — provided in exchange for _micropayments_ — meaning that each party
risks only tiny amounts.

> This would mean that a user will pay a node a couple of times a minute,
> sending a tiny amount of tokens in exchange for the bandwidth they are
> renting.

Blockchain payments are secure, [censorship
resistant](https://www.quora.com/What-does-censorship-resistance-mean-in-the-
context-of-blockchain), [trustless](https://en.wiktionary.org/wiki/trustless)
and have open and [permissionless](https://coincenter.org/entry/what-does-
permissionless-mean) API. Unfortunately they’re also relatively expensive and
slow (ethereum transaction may cost up to dollar and took up to couple of
hours to be included into block).

Situation with centralised payment solutions like PayPal or Stripe isn’t much
better. Despite many legal limitations (not accessible in some countries,
requires to have credit cards and pass KYC procedures even for getting small
amounts) they are also quite expensive — PayPal charges $0.05 and 5%, Stripe
charges about $0.25 and 2.9% of transaction value.

> 1tx/s * 60 sec * $0.05 = **3$ per hour** for transaction fees! :(

# Solving blockchain scalability problems

Scalability is a network’s ability to grow and handle more users. Blockchain
networks can be slow and clogged up by all the transactions being processed.

While ethereum core team is working on main layer upgrade (Ethereum 2.0), many
teams across the industry are working on Layer 2 solutions — independent
networks or chains running “on top” of the original blockchain to avoid it
becoming too crowded and slow.

The two most popular Layer 2 solutions being developed are _Plasma_ and _State
Channels_. Plasmas are more complex and suffer from issues related to their
centralised operators, while State Channels are arguably more decentralised.
State Channels also better serve our use case because they are P2P and scale
well with micropayments. As the core foundation of the widely-used _Lightning
Network_ they are well tested and are simpler to implement.

He have analysed couple of solutions (see our
[whitepaper](https://github.com/mysteriumnetwork/payments-smart-
contracts/blob/master/docs/paper/accountant-pattern.pdf)) on the market but
unfortunately either they were not mature (in early development) either didn’t
had some needed properties. The’re trying to solve much harder problem that we
needed, but in same time, the price of flexibility is complexity and
usability.

To be able to deliver user friendly, fast and easy to maintain payment
solution we have researched own L2 protocol called “Accountant pattern” and
will introduce additional actor in the network — Mysterium Accountant.

Our solution is based on state channels (somehow similar to Lightning Network,
Raiden Network or Connext) but is simplified. It avoids routing and two-way
payment channels complexity. In same time it provides high transaction
throughput (thousands tx/sec), prevention against double spending and
usability.

![Whitepaper — Accountant pattern: Lightweight solution for Mysterium Network
micropayments](https://miro.medium.com/max/1400/1*h4uukbikKB0qcBiF-rQk0Q.png)

[Whitepaper](https://github.com/mysteriumnetwork/payments-smart-
contracts/blob/master/docs/paper/accountant-pattern.pdf) — Accountant pattern:
Lightweight solution for embedded micropayments

While working on protocol design we had to set our requirements and point
places where we can cut complexity.

## Setting requirements

  1.  **High throughput and scalability** — the payment solution should be able to process as many transactions per second as there are active sessions between providers and consumers. We’re talking about thousands transactions per second.
  2.  **Support for MYST token —** and ideally possibility to avoid using any other tokens.
  3.  **Secure** — Anonymity, and the permissionless nature of decentralized systems, means we need additional layers of protection against bad actors. We need a system which enables identity registration, staking and punishment mechanisms.
  4.  **Decentralized** — it should maintain at least a decent level of decentralization and should **not** be controlled by any single party.
  5.  **Low complexity** — solution should have low level of complexity when it comes to implementing it, as well it have to be cheap to operate and maintain.
  6.  **Good user experience** — The **** technical aspects do not necessarily make it successful. If users experience friction of any kind when making a payment, that platform will not be geared towards adoption. (e.g. consumers should be able to deposit funds using any popular crypto wallet, or directly from exchanges; payments should not slowdown starting using service).

##  **Reducing complexity:**

  1.  **Perishable product** — because digital services such as video/audio streaming or VPN could be named as _perishable_ (they’re selling traffic which if not used, is “gone” forever), small amounts can be lost/not paid (e.g. payment for couple or minutes of service).
  2.  **Uni-directional payments** — all payments are made by consumers and received by providers. Never vice versa.

# Technical intro into Mysterium payments solution

The main components of protocol are: uni-directional, hashed time-locked
contract ([HTLC](https://www.youtube.com/watch?v=NcKNzk-H8CY)) based **_state
channels_** , **_identity registry_** , and new party in the network called
**_“Mysterium Accountant”_**.

## State Channels and Payment Promises

![](https://miro.medium.com/max/1400/1*owwC1X_lA5BHn1iDutSsVg.gif)

Visualisation of payment via state channel

Instead of consumers constantly paying providers _on-chain_ , consumers can
make “promises” to providers, similar to
[_IOUs_](https://www.investopedia.com/terms/i/iou.asp). These payment promises
later can be settled _on-chain_ by adding them as parameters into transaction
sent to state channel smart contract. Smart contract will verify them and send
appropriate amount into receiving party.

## Mysterium Accountant

Payments using _payment promises_ over _state channels_ are elegant and
efficient. Unfortunately they require to maintain channels between each
consumer/provider pair. This means a lot of deployed smart contracts.
Additionally, to get paid, providers would need to do at least one settlement
per consumer (which is expensive).

![](https://miro.medium.com/max/1006/1*rqOj5TO_gsZMIYkz7xrmaA.png)

Everyone has channel with everyone.

Alternatively there could be single top-up smart contract per consumer (see
“2.2. Initially proposed payment solution” in our [white
paper](https://github.com/mysteriumnetwork/payments-smart-
contracts/blob/master/docs/paper/accountant-pattern.pdf)).

![](https://miro.medium.com/max/1400/1*xOz2SrTnEgN32ATnmQkOyA.png)

This solved problem of having many smart-contracts and multiple top-ups.
Unfortunately provider’s problem of doing settle transaction per consumer is
still there. Additionally this approach would introduce potential double-
spending possibilities.

To circumvent such issues we propose to introduce a new party into the network
called the _“Mysterium Accountant”. The Accountant_ will not have any
authority over transactions themselves, but instead have an overview of and
verify _promised payments_ by consumers.

![](https://miro.medium.com/max/940/1*lyPrjwfyW2SJSNzmSKVg-g.png)

Payments via “Mysterium Accountant”

The Accountant has a record of each consumer’s actual balance and funds, as
well as a record of all of the promises made. When providers decide they want
to settle the account, the final tallied record is executed on the blockchain
and sent as a single transaction.

Our network can be made secure and trustless by utilising these _Accountants_
(we expect to have at least couple of accountants run by independent players)
and two types of payment channels:

  1. Paying channels, from consumers to Accountant;
  2. Receiving channels, from Accountant to providers.

In this way, _Mysterium Accountant_ plays a similar role as an intermediary or
hub between consumers and providers.

As these micropayment channels transact in “ _promises_ ” rather than _on-
chain_ payments, we significantly reduce the amount of transactions sent to
the blockchain. The network can then handle much larger volumes of users and
transactions, allowing our network to be fast and scalable.

To make sure we still honour decentralization, there can be multiple
accountants existing in the network. In our case consumers and providers can
refer to multiple, different accountants. A specific Accountant is chosen by
consumers during VPN session establishment. All Accountants are non-custodial,
meaning they never are able to steal funds stored in their smart-contracts.
They’re just managing off-chain balances so they can’t steal or cooperate with
consumers to cheat providers.

![](https://miro.medium.com/max/1000/1*wO7UB8rZxVcgh0_qK-x8Lg.png)

Both Consumers and Providers can work with multiple accountants

## Step-by-step

To make our proposal even more clear, let’s explain all the steps will be done
inside our payment protocol.

![](https://miro.medium.com/max/1400/1*dOxAGtAy9yPfCHGgeQ4lTw.png)

  1. Consumer top-up his channel smart contract address (deterministically calculated and provided by dVPN app in a form of QR code and plain text).
  2. Once in a selected period (e.g. each 20 seconds), c _onsumer_ sends payment promises to _provider_ for provided services.
  3. At any time (e.g. each 3rd promise) _provider_ is going to exchange _promise_ given by _consumer_ into _Accountant’s promise_. Provider needs to keep only last such promise.
  4. Consumer can issue promises to multiple providers, but only last such promise (with biggest value) will be settled by provider. All settled coins will be transferred from consumer’s channel into accountant smart-contract.
  5. When provider is happy with amount of tokens promised to him, he can settle last Accountat’s _promise_ and get coins into his wallet or exchange account.

## The Registry

The last important component of this protocol is a _registry_ where all
identities — consumers, providers and accountants will be registered. Payment
channels will be created between consumers, providers and accountants during
their registration.

![](https://miro.medium.com/max/1400/1*igC46vtgawnFGyw1GTPivA.png)

Registry deploys instances of payment channels between consumers and
accountants.

Differently than in _Lightning Network_ (when channel is destroyed after each
on-chain settlement / channel closing), our channels will be reused for
multiple transactions, top-ups and settlements (funds withdrawals).

# What does this mean for our node runners?

We’re currently working on implementation of this payment solution. After it
will be up and running, all the payments in the network will be done using
tokens. Also provider node runners will be get paid on minute bases (in
comparison to weekly bonuses we’re doing right now) and will be able to
withdraw to personal wallets their rewards at any time they like.

We will not have any limitation of type of wallets consumers and providers are
using. Also VPN session establishment should be as easy and fast as it is now
(without any lag caused by payments).

Between now and fully working solution we’re expecting couple of testing
phases. About detailed plan and exact steps of introducing payments into the
Network will be informed on [Mysterium blog](https://mysterium.network/blog/).

[![](https://miro.medium.com/max/1360/1*KVemUIEgTpc-
zXcp0L3hjQ.jpeg)](https://mailchi.mp/mysterium.network/newsletter)[![](https://miro.medium.com/max/1360/1*oQQM-0ehwV3qaOQVLyUHfQ.jpeg)](https://discord.me/mysterium)

![](https://miro.medium.com/max/1360/1*cYeo9De8YtauxC0hPk-KNQ.jpeg)

[![](https://miro.medium.com/max/1360/1*lEacU_01BunT2KNjtTv4QA.jpeg)](https://twitter.com/MysteriumNet)[![](https://miro.medium.com/max/1360/1*hXGcxWk6fFWeh-
MqlwhoZg.jpeg)](https://t.me/mysterium_network)

 _I’m software engineer, blockchain specialist and martial arts instructor.
You can find me on social media:_ [twitter](https://twitter.com/chompomonim),
[facebook](https://facebook.com/chompomonim), [linked
in](https://www.linkedin.com/in/jarolt/).

\--

\--

\--

## [More from Mysterium Network](/mysterium-network?source=post_page-----
c5a4ed05ca0f--------------------------------)

Decentralized VPN built on blockchain - https://mysterium.network

[Read more from Mysterium Network](/mysterium-network?source=post_page-----
c5a4ed05ca0f--------------------------------)

## Recommended from Medium

[[![MARK](https://miro.medium.com/fit/c/40/40/1*cyqMdDi7CL6M-1Pa2DmeUg.png)](/@mark-
cryptotrust?source=post_internal_links---------0----------------------------)

[MARK

](/@mark-cryptotrust?source=post_internal_links---------
0----------------------------)

## #01 What is ATLANTIS?

![](https://miro.medium.com/focal/112/112/50/50/1*_TE_N297ZnnIpzkO68Comg.png)](/@mark-
cryptotrust/01-what-is-atlantis-b710b9260191?source=post_internal_links
---------0----------------------------)

[[![WINGS
Magazine](https://miro.medium.com/fit/c/40/40/2*068FSBeNKRotjsu3P6b6xQ.png)](/@wings.ai?source=post_internal_links
---------1----------------------------)

[WINGS Magazine

](/@wings.ai?source=post_internal_links---------1----------------------------)

in

[Wings Dao

](https://medium.com/wings-ai?source=post_internal_links---------
1----------------------------)

## $500,000 WINGS Foundation diversification fund for Ethereum ICOs

![](https://miro.medium.com/focal/112/112/50/50/1*8rAuR3KZBWz7DFDIGyGvHQ.png)](/wings-
ai/500-000-wings-foundation-diversification-fund-for-ethereum-
icos-91ce3d7e60fc?source=post_internal_links---------
1----------------------------)

[[![Lao
Zi](https://miro.medium.com/fit/c/40/40/1*eSNbVMGJViQw8SpMDkO9PA.jpeg)](/@0xlaozi?source=post_internal_links
---------2----------------------------)

[Lao Zi

](/@0xlaozi?source=post_internal_links---------2----------------------------)

## QiDao Fundamentals Review: Week 31 (11/29–12/05/2021)

![](https://miro.medium.com/focal/112/112/50/50/0*fSCjk39CObDl7okf)](/@0xlaozi/qidao-
fundamentals-review-
week-31-11-29-12-05-2021-cada1c3c7d4a?source=post_internal_links---------
2----------------------------)

[[![Howling Wolf Token](https://miro.medium.com/fit/c/40/40/1*dTVlCqsq-
nvZflQ3_H30Ew.jpeg)](/@howlingwolftoken?source=post_internal_links---------
3----------------------------)

[Howling Wolf Token

](/@howlingwolftoken?source=post_internal_links---------
3----------------------------)

## NFT P2E Game Development — Update

![](https://miro.medium.com/focal/112/112/50/50/1*JeXf-
VLW5sds1TbhGsoxpQ.png)](/@howlingwolftoken/nft-p2e-game-development-
update-3e472632b00?source=post_internal_links---------
3----------------------------)

[[![Great British
Chefs](https://miro.medium.com/fit/c/40/40/0*-sScrhKv6UdurJqm.jpg)](/@gbchefs?source=post_internal_links
---------4----------------------------)

[Great British Chefs

](/@gbchefs?source=post_internal_links---------4----------------------------)

## Originally published on Instagram

![](https://miro.medium.com/focal/112/112/50/50/0*OUpzYLEdFyHmNX6x.)](/@gbchefs/originally-
published-on-instagram-a36202f1c124?source=post_internal_links---------
4----------------------------)

[[![Samourai
Wallet](https://miro.medium.com/fit/c/40/40/0*XDO5JlThcSCx9WVv.png)](/@SamouraiWallet?source=post_internal_links
---------5----------------------------)

[Samourai Wallet

](/@SamouraiWallet?source=post_internal_links---------
5----------------------------)

in

[Samourai Wallet

](https://medium.com/samourai-wallet?source=post_internal_links---------
5----------------------------)

## Updated PSA : Wasabi Wallet is the target of ongoing behavior that appears
to be a Sybil Attack…

![](https://miro.medium.com/focal/112/112/50/50/1*Qi8tU3KEtM7lNuIt9iHL_Q.png)](/samourai-
wallet/updated-psa-wasabi-wallet-is-the-target-of-ongoing-behavior-that-
appears-to-be-a-sybil-attack-6674a322e187?source=post_internal_links---------
5----------------------------)

[[![Ganiyu
Taiwo](https://miro.medium.com/fit/c/40/40/0*acJJ6BzcW11OfBC0.)](/@Tayenwo?source=post_internal_links
---------6----------------------------)

[Ganiyu Taiwo

](/@Tayenwo?source=post_internal_links---------6----------------------------)

## Introducing Meta Farm Verse

![](https://miro.medium.com/focal/112/112/50/50/0*dwF-
yQMt4nXl9JDx)](/@Tayenwo/introducing-meta-farm-
verse-a4249fd7d81b?source=post_internal_links---------
6----------------------------)

[[![Gobble
Token](https://miro.medium.com/fit/c/40/40/1*Zp62S44gasglncyM3GLpsg@2x.jpeg)](/@gobblegobbletoken?source=post_internal_links
---------7----------------------------)

[Gobble Token

](/@gobblegobbletoken?source=post_internal_links---------
7----------------------------)

## 🦃💎$GOBBLE TOKEN JUST LAUNCHED💎🦃

![](https://miro.medium.com/focal/112/112/50/50/1*hnhKaB5IKZ51p9ZWvGu6vA@2x.jpeg)](/@gobblegobbletoken/gobbletoken-
on-twitter-facebook-instagram-discord-
etc-74b2be1a022a?source=post_internal_links---------
7----------------------------)

[](/?source=post_page-----c5a4ed05ca0f--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
c5a4ed05ca0f--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
c5a4ed05ca0f--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
c5a4ed05ca0f--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
c5a4ed05ca0f--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----c5a4ed05ca0f--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----c5a4ed05ca0f--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fmysterium-
network%2Flightweight-solution-for-mysterium-network-
micropayments-c5a4ed05ca0f&source=post_page--------------------------
nav_reg-----------)

[![Jaro
Šatkevič](https://miro.medium.com/fit/c/176/176/0*N_2rIH7aXTX6mPW0.jpeg)](/@chompomonim)

[

## Jaro Šatkevič

](/@chompomonim)

197 Followers

Software Engineer, Blockchain specialist and Martial Arts instructor

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F41a1759c919e&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fmysterium-
network%2Flightweight-solution-for-mysterium-network-
micropayments-c5a4ed05ca0f&newsletterV3=3ac2c85fa59f&newsletterV3Id=41a1759c919e&user=Jaro+%C5%A0atkevi%C4%8D&userId=3ac2c85fa59f&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Richard Paxton](https://miro.medium.com/fit/c/40/40/1*5RrovY7a03nju-
CeNBl0zw.jpeg)](/@alacergroup?source=read_next_recirc---------0
---------------------b9a13096_0545_4bee_8ba4_89a74c612717-------)

[Richard Paxton

](/@alacergroup?source=read_next_recirc---------0---------------------
b9a13096_0545_4bee_8ba4_89a74c612717-------)

in

[Coinmonks

](https://medium.com/coinmonks?source=read_next_recirc---------0
---------------------b9a13096_0545_4bee_8ba4_89a74c612717-------)

## Hong Kong Phooey: Virtual Money Laundering Syndicate Foiled

![](https://miro.medium.com/focal/112/112/50/50/1*A6BpxIjoGFP2CP1IelWeQQ.jpeg)](/coinmonks/hong-
kong-phooey-virtual-money-laundering-syndicate-
foiled-14f805ba1fbd?source=read_next_recirc---------0---------------------
b9a13096_0545_4bee_8ba4_89a74c612717-------)

[[![Renejairath](https://miro.medium.com/fit/c/40/40/0*tMDDMVxFa-
CxhoLM)](/@renejairath?source=read_next_recirc---------1---------------------
b9a13096_0545_4bee_8ba4_89a74c612717-------)

[Renejairath

](/@renejairath?source=read_next_recirc---------1---------------------
b9a13096_0545_4bee_8ba4_89a74c612717-------)

## Considerations for Investing in Digital Finance (DRAFT)

![](https://miro.medium.com/focal/112/112/50/50/0*vkX6rj6rWMklNhdw)](/@renejairath/investing-
fundamentals-for-digital-finance-1754583d8b1b?source=read_next_recirc---------
1---------------------b9a13096_0545_4bee_8ba4_89a74c612717-------)

[[![Tradervidz
Investments](https://miro.medium.com/fit/c/40/40/1*oiPaHe9SOtVXlG_m0231RQ.png)](/@TradervidzInvestments?source=read_next_recirc
---------2---------------------b9a13096_0545_4bee_8ba4_89a74c612717-------)

[Tradervidz Investments

](/@TradervidzInvestments?source=read_next_recirc---------2
---------------------b9a13096_0545_4bee_8ba4_89a74c612717-------)

in

[Digital Surge Blog

](https://medium.com/digital-surge-blog?source=read_next_recirc---------2
---------------------b9a13096_0545_4bee_8ba4_89a74c612717-------)

## BTC and Altcoin News Update — 22 March

![](https://miro.medium.com/focal/112/112/50/50/1*8r3IMQCUOrVeUBoYO55Atw.png)](/digital-
surge-blog/btc-and-altcoin-news-
update-22-march-73ea78dbaceb?source=read_next_recirc---------2
---------------------b9a13096_0545_4bee_8ba4_89a74c612717-------)

[[![Axes
DAO](https://miro.medium.com/fit/c/40/40/1*1Q-C0w8Z6LkTGenYp9Ru0A@2x.jpeg)](/@Axes_DAO?source=read_next_recirc
---------3---------------------b9a13096_0545_4bee_8ba4_89a74c612717-------)

[Axes DAO

](/@Axes_DAO?source=read_next_recirc---------3---------------------
b9a13096_0545_4bee_8ba4_89a74c612717-------)

## Dual Treasury, The Rocket Fuel of Axes DAO!

![](https://miro.medium.com/focal/112/112/50/50/1*nWKLO4C1b-Jhx95-uC-
AXw.png)](/@Axes_DAO/dual-treasury-the-rocket-fuel-of-axes-
dao-838c43862688?source=read_next_recirc---------3---------------------
b9a13096_0545_4bee_8ba4_89a74c612717-------)

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

