[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/9085b84982eb&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Spatium
Blog](https://miro.medium.com/fit/c/64/64/1*Af7ihrFRI_0VaZWS9EcuKA.png)](https://medium.com/spatium-
blog?source=post_page-----9085b84982eb--------------------------------)

Published in

[Spatium Blog

](https://medium.com/spatium-blog?source=post_page-----
9085b84982eb--------------------------------)

[![Spatium](https://miro.medium.com/fit/c/96/96/1*Af7ihrFRI_0VaZWS9EcuKA.png)](/@spatium_news?source=post_page
-----9085b84982eb--------------------------------)

[Spatium](/@spatium_news?source=post_page-----
9085b84982eb--------------------------------)

Follow

Dec 17, 2019

·

6 min read

#  **Meet Spatium Hybrid**

![](https://miro.medium.com/max/1400/1*HrjQD1DftePxh4uW_ikfeg.png)

The situation on the crypto market shows that storage solutions based on the
[one-point-of-failure concept](http://bit.ly/2IR5xq3) are not worth a risk to
keep funds in them. This statement is fair even for cold storages, which are
represented as the most secure and convenient option in the industry:
[personal devices](https://blog.kraken.com/post/3245/flaw-found-in-keepkey-
crypto-hardware-wallet/) and hardware on the side of [third-
parties](https://idax.zendesk.com/hc/en-us/articles/360037327571-Urgent-
announcement-about-current-situation-of-IDAX-Global) were compromised not even
once. At the same time, exchanges and other companies are looking for ways to
get rid of exploits, increase their reputation and quality of services, plus
attract more audience, while users are seeking a way to keep their funds as
safe as possible and stay connected to the liquidity and promo actions of
exchanges to be ready for sudden market changes. With that said, we need a
solution in which funds could be kept offline not in one place, yet fund’s
owner could have full control over them from his device and have a connection
with a crypto service all the time. We are building such a solution — it is
called **Spatium Hybrid.**

#  **How it works**

![](https://miro.medium.com/max/1400/1*D6wgZfkmJQ_c_UGC5GC6bw.jpeg)

In the core of our system is [Spatium Protocol](http://bit.ly/2BV3Qnz). It’s
based on a variety of well-proven algorithms: Secure Multi-Party Computation
(SMPC). The combination of these technics with biometry provides us with an
ability to offer a secure, flexible, and easy-to-use **solution without the
private key and backups.**

The private key is replaced with the set of secrets that are generated, stored
and processed independently and never occur in one place. The secrets are
generated directly from the user’s biometry with every single use. [Biometric
data is not stored anywhere](http://bit.ly/2LjNqdl) and can’t be extracted
from the secrets. Users can store the secrets on N devices on their choice. To
perform any action with funds, the transaction must be signed by M-of-N
devices (sounds like multisig [but it's not](http://bit.ly/2re5fmZ)). The
signing process is off-chain, so it’s faster then on-chain solutions. Each
secret has its own permissions and can’t be used to take actions with money
without fund’s owner consent.

While, generally, we provide everyone with the opportunity to store secrets on
N devices on their choice and be their own custody, we see Spatium Hybrid as a
solution for those who want to share the responsibility for the fund’s safety
with the professional-level **Security Provider** and be able to manage their
funds very fast. The user can choose the entity he interested in from the
list.

Spatium Hybrid uses two secrets:

 **Secret A** is stored on user’s **Wallet Device** and is used to initiate
transactions and manage funds from phone, desktop or watches.

 **Secret B** , used for confirmations, is stored on the side of the **Virtual
Device** (Security Provider). Such an entity can be a custodial service,
centralized or decentralized exchange, bank or Spatium itself.

The process of work with Security Provider works as follows:

  1. The user installs the Spatium software on his device;
  2. Creates a wallet and locally generates Secret A with his biometry;
  3. Chooses the Security Provider, which will keep safe Secret B, and sets permissions;
  4. The institution receives a request and generates Secret B on its side. From this moment the user can perform actions with the funds;
  5. Secret A can be used to sign the transaction, while Secret B on the side of the professional Security Provider will be used to confirm the transaction.

![](https://miro.medium.com/max/1400/1*5knE4e98wLqol6PREZ1ZhA.jpeg)

As the Security Provider has only its own secret with the specific set of
permissions, no actions can be performed with funds without the user’s
consent. If Security Provider will be compromised (hacked or secret will be
stolen by employe), attackers still won’t have access to funds, as to gain
access to funds they also will need a Secret A, stored on the users’ side.

 **Our system provides the ability to distinguish the responsibility over
funds from the control, giving decentralized and centralized services an
opportunity to offer for their clients secure storage solutions, while users
will enjoy fast and convenient funds’ management.**

# Advantages and benefits

Such an architecture provides users and Security Providers with benefits that
are unique on the market.

For users:

  *  **No private key.** It is eliminated from the system;
  *  **No backups.** The secret is in you;
  *  **Instant transactions from users’ wallet.** As the user and exchange/bank are connected (if chosen as a Security Provider), he will have access to instant withdrawals/deposits/trades right from the users’ wallet with on-chain confirmations processed afterward;
  *  **Non-custodial solution.** Digital assets are not stored in one place, which makes them more secure;
  *  **Institutional-level security under your control.** Funds are protected by security professionals and the user retain full control over his money;
  *  **You set permissions.** Each secret has its own permissions set by the user and Security Provider or attacker can’t get access to coins without users’ secret;
  *  **Blockchain-agnostic.** SMPC technology is blockchain-agnostic and supports any coin or token from the box;
  *  **Universal addresses.** Unlike multisig, SMPC-based addresses can be used in DeFi and dApps;
  *  **Responsibility deligation.** The user can get the secret’s backup, stored on the Security Provider’s side, by request;
  *  **Conditional authorization.** The private key provides full access to funds, and if it will be stolen it can be used to withdraw all funds without limitations. With a set of secrets, this can be solved.
  *  **Legal.** Businesses can satisfy legal requirements without centralized custodianship.
  *  **Insurance.** If the customer has no full single access to the funds, they can be insured.

We are working on the implementation of additional features for every party,
as we believe that only win-win approach is the right one.

# How we deal with backups

We use biometry to provide everyone with the most secure and convenient way to
manage funds. Also, we believe that:

> the best way to keep your data safe — not to store it at all

With that said, we don’t store any biometric data and any images of it
anywhere. Instead, when the user has randomly generated Secret A on his
device, our app creates a neural network and sets its parameters so that it
could convert face data to that secret. Parameters of the neural network,
which are not sensitive data, then are bonded to users’ email and stored on
the side of the security provider. If the user loses access to his device, he
can get a new one, install Spatium Wallet App, enter the email used for
registration, and generate from his face Secret A again with the parameters of
the neural network.

# Sitting on both chairs

Spatium Hybrid solution solves one of the oldest problems of the crypto
industry — the choice between high security level of funds and the access to
big trading volumes. Now funds can be managed from the cold storage made of
hot wallets with convenient and fast access to liquidity, while Security
Providers have the opportunity to attract more users and offer them new
features, some of which are unique on the market and were missing for a long
time.

In the following articles, we will explore in detail Spatium Hybrid
implementations for banks and exchanges with benefits for each type of
Security Provider.

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
9085b84982eb--------------------------------)

Keyless & genuinely decentralized solution to manage digital assets.

[Read more from Spatium Blog](/spatium-blog?source=post_page-----
9085b84982eb--------------------------------)

## Recommended from Medium

[[![PlatON Network](https://miro.medium.com/fit/c/40/40/1*ZQqlB47jJ-
IZ_SBDT8g1Iw.jpeg)](/@platon-network?source=post_internal_links---------
0----------------------------)

[PlatON Network

](/@platon-network?source=post_internal_links---------
0----------------------------)

in

[PlatON Network

](https://medium.com/platon-network?source=post_internal_links---------
0----------------------------)

## PlatON Algorithm Scientist Dr.

![](https://miro.medium.com/focal/112/112/50/50/1*CfdZGLMhE2T8zzC5iebRFw.jpeg)](/platon-
network/platon-algorithm-scientist-dr-3374c85cc84b?source=post_internal_links
---------0----------------------------)

[[![Coinsandcoins](https://miro.medium.com/fit/c/40/40/1*THj766vMNwyH8lx1bqKWkQ.jpeg)](/@coinsandcoins1?source=post_internal_links
---------1----------------------------)

[Coinsandcoins

](/@coinsandcoins1?source=post_internal_links---------
1----------------------------)

## Regulator Reiterates Call for EU Ban on Proof-of-Work Mining

](/@coinsandcoins1/regulator-reiterates-call-for-eu-ban-on-proof-of-work-
mining-35a649d7ecb9?source=post_internal_links---------
1----------------------------)

[[![Nikkiefimov](https://miro.medium.com/fit/c/40/40/0*t5oXWgP3FEhAWOvk)](/@nikkiefimov?source=post_internal_links
---------2----------------------------)

[Nikkiefimov

](/@nikkiefimov?source=post_internal_links---------
2----------------------------)

## Stages of launching projects on the CRODO.IO Launchpad

![](https://miro.medium.com/focal/112/112/50/50/1*hA6Jr6xBbU8fRxEZGLh9VA.png)](/@nikkiefimov/stages-
of-launching-projects-on-the-crodo-io-
launchpad-8ec2fd434a64?source=post_internal_links---------
2----------------------------)

[[![Onchain
Custodian](https://miro.medium.com/fit/c/40/40/0*7PUqh2JT1Oy7ZmeZ.jpg)](/@oncustodian?source=post_internal_links
---------3----------------------------)

[Onchain Custodian

](/@oncustodian?source=post_internal_links---------
3----------------------------)

in

[Onchain Custodian

](https://medium.com/onchain-custodian?source=post_internal_links---------
3----------------------------)

## Key takeaways from the APAC Family Office Investment Summit 2020

![](https://miro.medium.com/focal/112/112/50/50/1*sA5ULBNqi1434rHO12bRTQ@2x.jpeg)](/onchain-
custodian/key-takeaways-from-the-apac-family-office-investment-
summit-2020-b7698f10e721?source=post_internal_links---------
3----------------------------)

[[![Sean O'Donoghue
Morgan](https://miro.medium.com/fit/c/40/40/0*G2F0cR9Gb6V_j52f.)](/@bitcoincity?source=post_internal_links
---------4----------------------------)

[Sean O'Donoghue Morgan

](/@bitcoincity?source=post_internal_links---------
4----------------------------)

in

[CoinYou

](https://medium.com/coinyou?source=post_internal_links---------
4----------------------------)

## How To Create A Multi-Currency Crypto Wallet (For Beginners)

![](https://miro.medium.com/focal/112/112/50/50/1*yDjlcS-
mgqJmmaGX_rcIgA.jpeg)](/coinyou/how-to-create-a-multi-currency-crypto-wallet-
for-beginners-a1825c0e00cc?source=post_internal_links---------
4----------------------------)

[[![Jonathan Morgan](https://miro.medium.com/fit/c/40/40/0*EyVaYlCXLKO-
pjN3.)](/@jonathan-morgan?source=post_internal_links---------
5----------------------------)

[Jonathan Morgan

](/@jonathan-morgan?source=post_internal_links---------
5----------------------------)

## Marlin (POND) Cryptocurrency Price Prediction, Forecast, and Technical
Analysis — Oct 21st, 2021

](/@jonathan-morgan/marlin-pond-cryptocurrency-price-prediction-forecast-and-
technical-analysis-oct-21st-2021-c715be399532?source=post_internal_links
---------5----------------------------)

[[![GetBlock](https://miro.medium.com/fit/c/40/40/1*-vI2q611od-2vjBzNYNbVQ.png)](/@getblock?source=post_internal_links
---------6----------------------------)

[GetBlock

](/@getblock?source=post_internal_links---------6----------------------------)

## About the Hive Project

![](https://miro.medium.com/focal/112/112/50/50/1*eIDNSnndg0RXKpBvFZfvwA.png)](/@getblock/about-
the-hive-project-1ee31190092f?source=post_internal_links---------
6----------------------------)

[[![Elite Mangudai AKA
Simbatoshi](https://miro.medium.com/fit/c/40/40/1*tU7e0xDackSHccF6IqbSaw.png)](/@Simbatoshi?source=post_internal_links
---------7----------------------------)

[Elite Mangudai AKA Simbatoshi

](/@Simbatoshi?source=post_internal_links---------
7----------------------------)

## Behind the scenes of the Dogecoin incident — Elon vs. Bitcoin —
Institutions

![](https://miro.medium.com/focal/112/112/50/50/1*rNMC0-oX4md0yzfzI20EBg.jpeg)](/@Simbatoshi/behind-
the-scenes-of-the-dogecoin-incident-elon-vs-bitcoin-
institutions-b58a24835cc5?source=post_internal_links---------
7----------------------------)

[](/?source=post_page-----9085b84982eb--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
9085b84982eb--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
9085b84982eb--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
9085b84982eb--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
9085b84982eb--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----9085b84982eb--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----9085b84982eb--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fspatium-
blog%2Fmeet-spatium-hybrid-9085b84982eb&source=post_page
--------------------------nav_reg-----------)

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
blog%2Fmeet-spatium-
hybrid-9085b84982eb&newsletterV3=eb4a6667c312&newsletterV3Id=69561b2e7b9e&user=Spatium&userId=eb4a6667c312&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Odoriko](https://miro.medium.com/fit/c/40/40/1*t4a_qVR50wRThw7KthqovQ.png)](/@Odoriko_bird?source=read_next_recirc
---------0---------------------b7d71b5e_544e_408a_8ea7_aab31de8f62f-------)

[Odoriko

](/@Odoriko_bird?source=read_next_recirc---------0---------------------
b7d71b5e_544e_408a_8ea7_aab31de8f62f-------)

in

[SUSHI TOP Marketing

](https://medium.com/sushi-top-marketing?source=read_next_recirc---------0
---------------------b7d71b5e_544e_408a_8ea7_aab31de8f62f-------)

## Next-generation credit card Nudge launches “Cashless to earn”, a
demonstration programme that…

![](https://miro.medium.com/focal/112/112/50/50/0*gGiBbenhjHF9wCgq)](/sushi-
top-marketing/next-generation-credit-card-nudge-launches-cashless-to-earn-a-
demonstration-programme-that-df9b766ed4d3?source=read_next_recirc---------0
---------------------b7d71b5e_544e_408a_8ea7_aab31de8f62f-------)

[[![Rishabh
Pote](https://miro.medium.com/fit/c/40/40/1*oFCbd16eHKX2qxYlPKHOYg@2x.jpeg)](/@rishabh.pote?source=read_next_recirc
---------1---------------------b7d71b5e_544e_408a_8ea7_aab31de8f62f-------)

[Rishabh Pote

](/@rishabh.pote?source=read_next_recirc---------1---------------------
b7d71b5e_544e_408a_8ea7_aab31de8f62f-------)

## NFTs… Beyond Art.

](/@rishabh.pote/nfts-beyond-art-4c69964a36f8?source=read_next_recirc---------
1---------------------b7d71b5e_544e_408a_8ea7_aab31de8f62f-------)

[[![Detix](https://miro.medium.com/fit/c/40/40/1*0IfwN9VHT_RI_pC3ZCvvpw.jpeg)](/@Detix?source=read_next_recirc
---------2---------------------b7d71b5e_544e_408a_8ea7_aab31de8f62f-------)

[Detix

](/@Detix?source=read_next_recirc---------2---------------------
b7d71b5e_544e_408a_8ea7_aab31de8f62f-------)

## 7 reasons to invest in Detix NFT

![](https://miro.medium.com/focal/112/112/50/50/1*Dc0ALHoxsvOg5IpHc6xWyQ.png)](/@Detix/7-reasons-
to-invest-in-detix-nft-1753a3f7963b?source=read_next_recirc---------2
---------------------b7d71b5e_544e_408a_8ea7_aab31de8f62f-------)

[[![Nikelenjelo](https://miro.medium.com/fit/c/40/40/1*gJ6ODZGc9b0mE8zPvOGzWQ.png)](/@nikelenjeloo?source=read_next_recirc
---------3---------------------b7d71b5e_544e_408a_8ea7_aab31de8f62f-------)

[Nikelenjelo

](/@nikelenjeloo?source=read_next_recirc---------3---------------------
b7d71b5e_544e_408a_8ea7_aab31de8f62f-------)

## The first pioneer of the new trend in 2022: Imaginary Ones

![](https://miro.medium.com/focal/112/112/50/50/1*YNbu9N075RmFQuybl7mMCw.png)](/@nikelenjeloo/the-
first-pioneer-of-the-new-trend-in-2022-imaginary-
ones-1e3d7d7b9776?source=read_next_recirc---------3---------------------
b7d71b5e_544e_408a_8ea7_aab31de8f62f-------)

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

