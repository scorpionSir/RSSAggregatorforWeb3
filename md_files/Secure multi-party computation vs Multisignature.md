[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/9e5698f9fcbb&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Spatium
Blog](https://miro.medium.com/fit/c/64/64/1*Af7ihrFRI_0VaZWS9EcuKA.png)](https://medium.com/spatium-
blog?source=post_page-----9e5698f9fcbb--------------------------------)

Published in

[Spatium Blog

](https://medium.com/spatium-blog?source=post_page-----
9e5698f9fcbb--------------------------------)

[![Spatium](https://miro.medium.com/fit/c/96/96/1*Af7ihrFRI_0VaZWS9EcuKA.png)](/@spatium_news?source=post_page
-----9e5698f9fcbb--------------------------------)

[Spatium](/@spatium_news?source=post_page-----
9e5698f9fcbb--------------------------------)

Follow

Nov 8, 2019

·

5 min read

# Secure multi-party computation vs Multisignature

![](https://miro.medium.com/max/1400/0*WSnI9Dk5btB3H4oN.png)

Recently, we have declared [Multi-party computation (MPC) as the technology,
which fits our principles](/@spatium_news/spatium-vision-constructing-a-new-
security-paradigm-2c26b03c2dbd) to build a keyless, convenient and flexible
security solutions, and briefly [explored how it
works](/@spatium_news/spatium-protocol-smpc-on-your-guard-ba45b07e0b26).

>  ** _In short:_** _the private key is replaced with a set of secrets
> distributed between user’s gadgets or devices stored on behalf of chosen
> institutions or people. Each party independently generates, stores and
> processes its secret separated from other parties._

It is a similar concept with multisig, but these are two different
technologies. Let’s take a close look at the differences between them.

# Compatibility

Multisig works with the limited number of blockchains, while MPC is a
blockchain agnostic technology — it works with any ledger from the box as the
support comes on the cryptography level.

As crypto industry moves towards mass adoption, users need to have blockchain
addresses of their coins compatible with future services. But multisig already
fails to support dApps and DeFi services — it doesn’t work with them, since it
is implemented as a smart-contract (if we talk about Ethereum). By contrast,
MPC provides users with a simple address that can be used in any decentralized
service or application and works with them perfectly.

There is a misconception, that MPC has a lack of hardware security module
(HSM) support. Сontrariwise — MPC is a technology that can be deployed on
mobile, desktop or server device with authorization policies being changed
with ease, as it is completely software solution. HSM operators will have only
blockchain addresses and infrastructure changes won’t affect them. On the
other side, multisig can cause problems to HSMs because it doesn’t support
blockchains — only cryptographic curves like secp256k1 (Bitcoin) or
edwards25519 (Monero). It means that changes in the code of a blockchain in
case of a hard fork or some other reason can lead to issues which can take
months to resolve or need an employment of a new hardware.

Another misconception: MPC is a proprietary technology that is not well tested
and relies on peer review. There are [MPC solutions that are open
source](https://csrc.nist.gov/publications/detail/nistir/8214/final) because
such an approach can help technology to evolve, expand and provide benefits to
every party on the market.

# Speed

Multisig transactions are signed on-chain and there is a need in confirmations
that can take a long time. The MPC transactions are signed off-chain with
confirmation comes afterward. As confirmations are performed simultaneously
sometimes the speed can be low, but in general off-chain approach of MPC can
give the market speed that it requires.

Moreover, when parties are participating in a quorum, multisig scripts entail
more data to accommodate metadata about each signer. At that, the time to
process a new block and the final cost for the end-user increase.

With MPC, as parties are processing their secrets independently, their devices
can stay online 24/7, and not think about the possibility of being
compromised. Secrets participate in the transaction signing anonymously, and
lack of data helps to keep transaction time short and costs less.

# Privacy

If the multisig participant shares his address on the internet or to someone,
all transactions with that address can be traced and related to him (if they
take place on the public blockchain). MPC secrets, used in the transaction
signing, can be seen by participants, but the secret owner can’t be
identified. The process works as follows:

  1. Party receives a notification about a transaction;
  2. Goes through the multi-factor authentication;
  3. Takes a close look on the transaction;
  4. Confirms or declines it.

It can be noted, that with MPC secrets, it is impossible to distinguish which
one of them was used to sign the transaction: at the end of the computation
they all look the same. From that perspective this tech can have a hard way
getting to a corporate segment, where it is important to know which party
signed a transaction. But overall, anonymity is one of the technology’s
benefits.

Especially when it comes to the fact that MPC secrets leave no trace on the
ledger. This tech can be used externally on any blockchains — even built
without multisig capabilities initially. MPC could be taken as an additional
privacy measure for anonymity-oriented blockchains like Monero.

# Flexibility

Any changes in the multisig addresses involve changes in the code. For
businesses, this can mean dependence on third-party IT service for daily
operations and sufficient time and money expenditures.

Limited flexibility in supporting advanced quorum authorization policies (more
than 2-of-3) is also a problem for multisig. This can be an easy target for a
hacker (or a group of hackers). Institutions like banks cherish the security
of their customers and require more complex quorums. Also, they do that to
meet compliance requirements.

It is hard to change approval rules in the multisig, as it can involve a lot
of man-hours to develop such a solution and even more to deploy it. Also,
factors based on transaction amount, geolocation, etc. are not available.
Customized application-based code can help the vendor to mitigate these
problems — but such a solution is exposed to various attacks as it is much
less secure than cryptographic mechanisms.

In the MPC the number of parties for a quorum is unlimited and can implement
any rules to sign a transaction: the amount of money, type of payment,
geolocation, time of day, etc.

# K.O.

MPC has clear advantages over the multisig and can replace the latter shortly
due to resulting benefits for all participants on the market.

In the next article, we will continue to cover our principles of building
future-ready security systems and will talk about the second of them —
biometry.

Stay tuned.

#spatium_vision

 **Spatium** develops solutions to store and manage digital assets powered by
SMPC and biometry. In our technology, the private key is replaced with the
encrypted set of secrets, stored on behalf of funds owner’s devices,
individuals and institutions, chosen by him. Even if some of the parties are
compromised — funds will stay safe. Such an approach dramatically decreases
the risk of theft and provides a previously unavailable level of flexibility
and unique benefits for everyone on the market: no single point of failure,
easy recovery, no need in backups, blockchain agnostic, access levels
differentiation, instant crypto/crypto and crypto/fiat exchange, fully
compliant solution, support of dApps and DeFi services, etc.

\--

\--

\--

## [More from Spatium Blog](/spatium-blog?source=post_page-----
9e5698f9fcbb--------------------------------)

Keyless & genuinely decentralized solution to manage digital assets.

[Read more from Spatium Blog](/spatium-blog?source=post_page-----
9e5698f9fcbb--------------------------------)

## Recommended from Medium

[[![UBIX.Network](https://miro.medium.com/fit/c/40/40/1*XUdQ-
uxZp_cDEmogO6d5xw.png)](/@ubix-network?source=post_internal_links---------
0----------------------------)

[UBIX.Network

](/@ubix-network?source=post_internal_links---------
0----------------------------)

in

[SilentNotary

](https://medium.com/silentnotary?source=post_internal_links---------
0----------------------------)

## When Copyrights Leave You With No Rights

![](https://miro.medium.com/focal/112/112/50/50/1*ISH9JSrp7RytHmIpqaoGhQ.jpeg)](/silentnotary/when-
copyrights-leave-you-with-no-rights-92a6d427b74?source=post_internal_links
---------0----------------------------)

[[![CUDOS](https://miro.medium.com/fit/c/40/40/1*NI027y25_04FOoN-4b-08w.png)](/@cudostoken?source=post_internal_links
---------1----------------------------)

[CUDOS

](/@cudostoken?source=post_internal_links---------
1----------------------------)

## 🏗 How Cudos is building the infrastructure needed for Web3 🌐

![](https://miro.medium.com/focal/112/112/50/50/0*sB_rxL_wjRapD7IB)](/@cudostoken/how-
cudos-is-building-the-infrastructure-needed-for-
web3-2fbf6586ce72?source=post_internal_links---------
1----------------------------)

[[![CrypTalks
App](https://miro.medium.com/fit/c/40/40/1*gcBeM5pK7SQsqd3-cH22HQ.png)](/@cryptalk_app?source=post_internal_links
---------2----------------------------)

[CrypTalks App

](/@cryptalk_app?source=post_internal_links---------
2----------------------------)

## Why the three biggest financial frauds in history could not have happened
today

![](https://miro.medium.com/focal/112/112/50/50/1*SV2KsWE4OrgG4PZ1h27bfg.jpeg)](/@cryptalk_app/why-
the-three-biggest-financial-frauds-in-history-could-not-have-happened-
today-a3d8f0a06527?source=post_internal_links---------
2----------------------------)

[[![CUDOS](https://miro.medium.com/fit/c/40/40/1*NI027y25_04FOoN-4b-08w.png)](/@cudostoken?source=post_internal_links
---------3----------------------------)

[CUDOS

](/@cudostoken?source=post_internal_links---------
3----------------------------)

in

[CUDOS

](https://medium.com/cudos?source=post_internal_links---------
3----------------------------)

## 🚀 Project Artemis — phase two — network upgrade! 🌖

![](https://miro.medium.com/focal/112/112/50/50/0*o7iTo0RIa-
aq_DiO)](/cudos/project-artemis-phase-two-network-
upgrade-7b50c4382ab0?source=post_internal_links---------
3----------------------------)

[[![MYU_DAO](https://miro.medium.com/fit/c/40/40/0*4nmVSj2bnIJD7xHn)](/@myudao2022?source=post_internal_links
---------4----------------------------)

[MYU_DAO

](/@myudao2022?source=post_internal_links---------
4----------------------------)

## MAVIA’s Token Economy System.

![](https://miro.medium.com/focal/112/112/50/50/0*nYjZ-A5KOQXSaZJl)](/@myudao2022/mavias-
token-economy-system-b6a269d79deb?source=post_internal_links---------
4----------------------------)

[[![Ché Köhler](https://miro.medium.com/fit/c/40/40/2*xFRIkFPVP-
pDOvWmOctM9g.jpeg)](/@chekohler?source=post_internal_links---------
5----------------------------)

[Ché Köhler

](/@chekohler?source=post_internal_links---------
5----------------------------)

## dApp Review: PickFlix

![](https://miro.medium.com/focal/112/112/50/50/0*4DBI51_nqU5y573V.jpg)](/@chekohler/dapp-
review-pickflix-4a56d4a1b877?source=post_internal_links---------
5----------------------------)

[[![ZENZO
Ecosystem](https://miro.medium.com/fit/c/40/40/1*xnlS1VgncGcqI2rF-6P6wA.png)](/@zenzo-
ecosystem?source=post_internal_links---------6----------------------------)

[ZENZO Ecosystem

](/@zenzo-ecosystem?source=post_internal_links---------
6----------------------------)

## ZENZO Monthly Report: October 2019

![](https://miro.medium.com/focal/112/112/50/50/1*Jg2qdbgIYzQ4cNsJgr4OMA.png)](/@zenzo-
ecosystem/zenzo-monthly-report-
october-2019-f9cd6e4d9115?source=post_internal_links---------
6----------------------------)

[[![Statecraft
Tech](https://miro.medium.com/fit/c/40/40/2*3FjConaJT6Rsw3a1G__Gjg.png)](/@statecrafttech?source=post_internal_links
---------7----------------------------)

[Statecraft Tech

](/@statecrafttech?source=post_internal_links---------
7----------------------------)

in

[Statecraft Tech

](https://medium.com/ktrade?source=post_internal_links---------
7----------------------------)

## MULTI-
MODALTRIPPLANNINGAPPLICATIONMINIMUMVIABLEPRODUCTLAUNCHESUSINGBLOCKCHAIN

![](https://miro.medium.com/focal/112/112/50/50/1*_mrO5-OE5e6BlZjiX9PAuA.jpeg)](/ktrade/multi-
modaltripplanningapplicationminimumviableproductlaunchesusingblockchain-e98e70ef659a?source=post_internal_links
---------7----------------------------)

[](/?source=post_page-----9e5698f9fcbb--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
9e5698f9fcbb--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
9e5698f9fcbb--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
9e5698f9fcbb--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
9e5698f9fcbb--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----9e5698f9fcbb--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----9e5698f9fcbb--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fspatium-
blog%2Fsecure-multi-party-computation-vs-
multisignature-9e5698f9fcbb&source=post_page--------------------------
nav_reg-----------)

[![Spatium](https://miro.medium.com/fit/c/176/176/1*Af7ihrFRI_0VaZWS9EcuKA.png)](/@spatium_news)

[

## Spatium

](/@spatium_news)

51 Followers

Spatium — true, decentralized, keyless crypto storage solution, bringing
complex cryptographic technologies from security experts to blockchain
enthusiasts.

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F69561b2e7b9e&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fspatium-
blog%2Fsecure-multi-party-computation-vs-
multisignature-9e5698f9fcbb&newsletterV3=eb4a6667c312&newsletterV3Id=69561b2e7b9e&user=Spatium&userId=eb4a6667c312&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Jesse Abernathy
Phoenix](https://miro.medium.com/fit/c/40/40/1*PDAxJ9cqtLYg-EeQR-
xoHg.jpeg)](/@jesseabernathyphoenix?source=read_next_recirc---------0
---------------------70b81b56_95c7_4ecf_8ec7_9dca033240dd-------)

[Jesse Abernathy Phoenix

](/@jesseabernathyphoenix?source=read_next_recirc---------0
---------------------70b81b56_95c7_4ecf_8ec7_9dca033240dd-------)

## Jesse Abernathy of Phoenix Explains the Ins and Outs of DAOs

![Jesse Abernathy Phoenix
cubes](https://miro.medium.com/focal/112/112/50/50/1*xb-
KAILf3iVZDwZA_7RwAg.jpeg)](/@jesseabernathyphoenix/jesse-abernathy-of-phoenix-
explains-the-ins-and-outs-of-daos-af2fe10ba139?source=read_next_recirc
---------0---------------------70b81b56_95c7_4ecf_8ec7_9dca033240dd-------)

[[![fiat24@Fiat24](https://miro.medium.com/fit/c/40/40/1*Zg--
VABjKAFNybh1P8l-Cg.png)](/@fiat24?source=read_next_recirc---------1
---------------------70b81b56_95c7_4ecf_8ec7_9dca033240dd-------)

[fiat24@Fiat24

](/@fiat24?source=read_next_recirc---------1---------------------
70b81b56_95c7_4ecf_8ec7_9dca033240dd-------)

in

[fiat24

](https://medium.com/fiat24?source=read_next_recirc---------1
---------------------70b81b56_95c7_4ecf_8ec7_9dca033240dd-------)

## Fiat24 launches their eponymous DApp, a revolutionary banking concept
addressing needs in both…

![](https://miro.medium.com/focal/112/112/50/50/1*nK0mGHkDZls4efZL-
hYlEA.png)](/fiat24/fiat24-launches-their-eponymous-dapp-a-revolutionary-
banking-concept-addressing-needs-in-both-f3d45eb43abe?source=read_next_recirc
---------1---------------------70b81b56_95c7_4ecf_8ec7_9dca033240dd-------)

[[![Maksimjeet
Chowdhary](https://miro.medium.com/fit/c/40/40/1*weKBD592bCyDljfQH-Y6eg.jpeg)](/@maksimjeet?source=read_next_recirc
---------2---------------------70b81b56_95c7_4ecf_8ec7_9dca033240dd-------)

[Maksimjeet Chowdhary

](/@maksimjeet?source=read_next_recirc---------2---------------------
70b81b56_95c7_4ecf_8ec7_9dca033240dd-------)

## ERC-998 — the ostensible standard of the future

![](https://miro.medium.com/focal/112/112/50/50/1*QfE70nF8b9Bu_NTUBgqKqg.png)](/@maksimjeet/erc-998-the-
ostensible-standard-of-the-future-75b99089e6ba?source=read_next_recirc
---------2---------------------70b81b56_95c7_4ecf_8ec7_9dca033240dd-------)

[[![ROTTENSWAP](https://miro.medium.com/fit/c/40/40/1*8N9AVhzE6pofyXCmE0I7WA.png)](/@rottenswap?source=read_next_recirc
---------3---------------------70b81b56_95c7_4ecf_8ec7_9dca033240dd-------)

[ROTTENSWAP

](/@rottenswap?source=read_next_recirc---------3---------------------
70b81b56_95c7_4ecf_8ec7_9dca033240dd-------)

## ROTTENSWAP Kicks Off DeFi Summer 2022

![](https://miro.medium.com/focal/112/112/50/50/0*x38_gtFX973siQgz)](/@rottenswap/rottenswap-
kicks-off-defi-summer-2022-3caf95e3ec1a?source=read_next_recirc---------3
---------------------70b81b56_95c7_4ecf_8ec7_9dca033240dd-------)

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

