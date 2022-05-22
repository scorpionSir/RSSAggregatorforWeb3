[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/64bc0f23b81f&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Spatium
Blog](https://miro.medium.com/fit/c/64/64/1*Af7ihrFRI_0VaZWS9EcuKA.png)](https://medium.com/spatium-
blog?source=post_page-----64bc0f23b81f--------------------------------)

Published in

[Spatium Blog

](https://medium.com/spatium-blog?source=post_page-----
64bc0f23b81f--------------------------------)

[![Spatium](https://miro.medium.com/fit/c/96/96/1*Af7ihrFRI_0VaZWS9EcuKA.png)](/@spatium_news?source=post_page
-----64bc0f23b81f--------------------------------)

[Spatium](/@spatium_news?source=post_page-----
64bc0f23b81f--------------------------------)

Follow

Nov 8, 2019

·

6 min read

# Spatium Vision: Constructing a New Security Paradigm

![](https://miro.medium.com/max/1400/0*I5-sJ4nIwFrenBm9.png)

In the previous article, we have researched in detail the problems of the
private keys and explained why they should be replaced with new security
approaches (you can read the article [here](/@spatium_news/the-private-key-to-
failure-15cdc9cacd1f)).

>  _Brief: If strategic nuclear forces used the same security approach as the
> crypto industry — it would be based on the one red button, which could
> launch all rockets at once if pushed by a random person._

In this material, we will explore our vision of some principles that modern
security systems could use for keeping up with the fast-changing requirements
of the market, and create future-ready products.

# No private key

Today crypto industry receives millions of dollars in investments. Hence, it
is better to abandon the private key, which is the single point of failure,
rather than constantly trying to guard it from hackers. And this is where we
meet the MPC (multi-party computation) technology. Let’s go to a short
explanation of it.

The private key is replaced with the set of secrets. These secrets are
distributed between the user and the number of parties chosen by him. MPC
parties can be any user’s gadgets or devices stored on behalf of chosen
institutions or people. Each party independently generates, stores and
processes its secret separated from other parties. To perform any action with
funds, the quorum of parties, set by the user, is needed. Each party, on their
own, can not get access to funds or perform any transaction without the funds’
owner. The transaction is initiated by one party and sequentially co-signed by
the other parties, participating in the signing process.

Described architecture eliminates the risk of private keys theft: you can’t
steal something that does not exist. Also, it solves a problem of a secret
data loss due to one of the parties getting compromised.

MPC has a number of important benefits:

  1.  **Security.** Replacement of the private key with the set of secrets eliminates the single point of failure. If the risk of the single private key’s compromisation is 1/x, then the risk of the simultaneous compromisation of N secrets is 1/x^N — a value of a different order. Such an approach provides the security level of the cold storage with only hot wallets in use (and without limitations of cold wallets).
  2.  **Flexibility.** Usually, the private key is stored somewhere on one entity (software wallet, hardware wallet, paper wallet, etc). It does not seem a good idea to use the same wallet to store millions and to buy goods daily. Sure, funds can be separated between hardware and software wallets, but then, the user will need to manage two private keys and two backups, which is not convenient. With MPC, the user can build hierarchies of parties with secrets (conditional authorizations) for a variety of use-cases: 2-of-2 signs for online shopping, 3-of-4 signs for funds transfer, etc. Each configuration can be set as the optimal solution for a specific task. The number of use-cases and configurations is limited only by the user’s imagination.
  3.  **Access levels differentiation.** The user can assign the rights (in terms of access to funds) for each party. For example, a bank can be delegated full responsibility for the storage of funds without access to them. Large enterprises can configure complex authorisation logic needed to perform transaction signing. For example, in a small company, transactions can be signed by one of the two employees from the financial department, while in the big companies, the signing process can require the quorum of the directors.

Such functionality can be implemented via the multi-sig, but it will work only
with on-chain transactions of the limited number of digital assets and only
with specific types of addresses, while with MPC the same can be done off-
chain with digital assets of any blockchain, making it more convenient and
faster solution. Also, MPC address can be used in dApps and DeFi services,
while multi-sig address can’t (detailed comparison of both technologies will
be provided in one of the following materials).

The use of MPC for the transaction signing is based on advanced and proven
cryptographic techniques: Threshold signature, Zero-knowledge proof, Paillier
encryption, Homomorphic encryption. Spatium is one of the pioneers in the
field — the team began to work in the subject in 2017 and were the first in
the world, who suggested the open-source MPC algorithms to the public (April
2018).

# No backup

The private key (or the seed phrase in HD wallets) is always generated
randomly. Thus, it is necessary to make a backup of it. That’s where a lot of
problems appear: backups are often get lost, destroyed, or become unusable, so
the user should provide a high level of security for them. But despite the
attempts to keep backups safe, the probability of unauthorized access to them
is still high. That’s why it is needed to go another way — not to make backups
at all. An optimal solution is to use biometry.

Biometry is the method of authorization based on a user’s biometric data (e.q.
fingerprint), used by government structures in various countries as the
technical approach providing the highest level of security. Beyond that, it is
a very convenient method to access the system (and getting rights to be
distinguished for an entity as well).

Today biometry is often used to encrypt the private key in the system. But, if
it is used to generate secrets on each access to perform every operation, we
will free the user from the necessity to remember a private key/seed phrase or
keep them offline and will provide him with the ability to access his funds in
a secure, fast and convenient way from anywhere — as “keys will always be in
his hand”.

# Not proprietary

Kerckhoffs’s principle says: a cryptosystem should be secure even if
everything about the system, except the key, is public knowledge.
Unfortunately, the majority of IT projects do not follow this principle.
Instead, their software is proprietary, and no one knows what is in their
code. Meanwhile, a lot of scandals has appeared in the news recently about
[backdoors](https://en.wikipedia.org/wiki/Backdoor_\(computing\)) found in the
hardware of Intel, AMD, etc. If you want your funds to be stored securely, you
need to take this aspect very seriously.

HSM / Secure Enclave devices provide a very high level of security, but the
user is obliged to trust the firmware of the hardware vendor, which in most
cases is not open-source. In particular, he should be convinced that his
private data is not being uploaded to the vendor’s servers, where it can be
provided to anyone upon request. For example, access to such data can be
granted to government forces for the AML-analysis and to perform censorship:
transaction cancellation, funds confiscation, etc. Advertising agencies also
can be interested in the data to examine the financial situation of the user
and define the products he is interested in. Moreover, the user is obliged to
trust that the firmware developers won’t use this private data to steal his
funds themselves.

But exploits can be found [even in hardware wallets with the open-source
firmware](https://www.kaspersky.com/blog/hardware-wallets-hacked/25315/),
which are designed specifically for the needs of the crypto industry. So the
user must follow all related news and manually update his software all the
time to protect his funds form new attack vectors. All this doesn’t seem like
a convenient solution.

In light of the above, it is clear that the firmware codebase should be open,
and the update process must occur automatically without the user’s intent,
providing him with the maximum level of convenience.

# Outro

Here is our vision of a security system that will meet the high requirements
of the market and stay secure and convenient even years later.

In the next article, we will explore how all mentioned principles are
implemented in the Spatium protocol to bring the future-ready product to
masses and institutions.

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
64bc0f23b81f--------------------------------)

Keyless & genuinely decentralized solution to manage digital assets.

[Read more from Spatium Blog](/spatium-blog?source=post_page-----
64bc0f23b81f--------------------------------)

## Recommended from Medium

[[![Jonathan Morgan](https://miro.medium.com/fit/c/40/40/0*EyVaYlCXLKO-
pjN3.)](/@jonathan-morgan?source=post_internal_links---------
0----------------------------)

[Jonathan Morgan

](/@jonathan-morgan?source=post_internal_links---------
0----------------------------)

## Bitcoin (BTC) Cryptocurrency Price Prediction, Forecast, and Technical
Analysis — Sept 15th, 2021

](/@jonathan-morgan/bitcoin-btc-cryptocurrency-price-prediction-forecast-and-
technical-analysis-sept-15th-2021-e24905c1e620?source=post_internal_links
---------0----------------------------)

[[![Worldopo](https://miro.medium.com/fit/c/40/40/1*YR1sBsDZtErsQ7ods4iNGg.png)](/@worldopo.io?source=post_internal_links
---------1----------------------------)

[Worldopo

](/@worldopo.io?source=post_internal_links---------
1----------------------------)

## Gaming and Blockchain join forces thanks to Ethereum

![](https://miro.medium.com/focal/112/112/50/50/0*PUD-42c6fuu90nno.jpg)](/@worldopo.io/gaming-
and-blockchain-join-forces-thanks-to-
ethereum-d63b12873c67?source=post_internal_links---------
1----------------------------)

[[![Seele](https://miro.medium.com/fit/c/40/40/2*OR26HNb7rtLlDxKhk-t-
bg.jpeg)](/@seelen?source=post_internal_links---------
2----------------------------)

[Seele

](/@seelen?source=post_internal_links---------2----------------------------)

## SEELE’s Staking on the SeeleN Ecological Nerv Ledger Platform Exceeding 10
Billion

![](https://miro.medium.com/focal/112/112/50/50/1*5BpGrtsvKnRzZhP5Fm8VxA.png)](/@seelen/seeles-
staking-on-the-seelen-ecological-nerv-ledger-platform-
exceeding-10-billion-1987a3a61293?source=post_internal_links---------
2----------------------------)

[[![FFQuest](https://miro.medium.com/fit/c/40/40/1*iG5K1TDVYisOONkwzXEowg.png)](/@ffquest?source=post_internal_links
---------3----------------------------)

[FFQuest

](/@ffquest?source=post_internal_links---------3----------------------------)

in

[Coinmonks

](https://medium.com/coinmonks?source=post_internal_links---------
3----------------------------)

## How to survive crypto crash losses

![](https://miro.medium.com/focal/112/112/50/50/0*hJaVkWZHyFzYMsKR)](/coinmonks/how-
to-survive-crypto-crash-losses-560e24063e9?source=post_internal_links---------
3----------------------------)

[[![Nzegbo](https://miro.medium.com/fit/c/40/40/1*dmbNkD5D-u45r44go_cf0g.png)](/@nzegboray79?source=post_internal_links
---------4----------------------------)

[Nzegbo

](/@nzegboray79?source=post_internal_links---------
4----------------------------)

## NEOX is a newly developed app that enable users to initiate payments with
cyryptocurrencies.

![](https://miro.medium.com/focal/112/112/50/50/1*zHyg3fug6UqR-
OgFCvgkZg.jpeg)](/@nzegboray79/neox-is-a-newly-developed-app-that-enable-
users-to-initiate-payments-with-
cyryptocurrencies-e8e70abd794a?source=post_internal_links---------
4----------------------------)

[[![Jonathan Morgan](https://miro.medium.com/fit/c/40/40/0*EyVaYlCXLKO-
pjN3.)](/@jonathan-morgan?source=post_internal_links---------
5----------------------------)

[Jonathan Morgan

](/@jonathan-morgan?source=post_internal_links---------
5----------------------------)

## Polkadot DOT Price Prediction [$82 IN SIGHT] Dec 29 2021

](/@jonathan-morgan/polkadot-dot-price-prediction-82-in-sight-
dec-29-2021-e9e7be33ed11?source=post_internal_links---------
5----------------------------)

[[![Blockchain
Consulting](https://miro.medium.com/fit/c/40/40/0*80SQCJmtc8N5pTjl.jpg)](/@blockchainco52?source=post_internal_links
---------6----------------------------)

[Blockchain Consulting

](/@blockchainco52?source=post_internal_links---------
6----------------------------)

## Will Crypto Market Survive the COVID-19 Outbreak?

![](https://miro.medium.com/focal/112/112/50/50/1*VH3Yo2SSbRU-
JbHZy8L6aw.png)](/@blockchainco52/will-crypto-market-survive-the-
covid-19-outbreak-affc12c946d0?source=post_internal_links---------
6----------------------------)

[[![CUDOS](https://miro.medium.com/fit/c/40/40/1*NI027y25_04FOoN-4b-08w.png)](/@cudostoken?source=post_internal_links
---------7----------------------------)

[CUDOS

](/@cudostoken?source=post_internal_links---------
7----------------------------)

in

[CUDOS

](https://medium.com/cudos?source=post_internal_links---------
7----------------------------)

## The UK announces its intention to become a global crypto hub

![](https://miro.medium.com/focal/112/112/50/50/0*UrNyv2i0RBiRG-
eT)](/cudos/the-uk-announces-its-intention-to-become-a-global-crypto-
hub-8db41583035a?source=post_internal_links---------
7----------------------------)

[](/?source=post_page-----64bc0f23b81f--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
64bc0f23b81f--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
64bc0f23b81f--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
64bc0f23b81f--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
64bc0f23b81f--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----64bc0f23b81f--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----64bc0f23b81f--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fspatium-
blog%2Fspatium-vision-constructing-a-new-security-
paradigm-64bc0f23b81f&source=post_page--------------------------
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
blog%2Fspatium-vision-constructing-a-new-security-
paradigm-64bc0f23b81f&newsletterV3=eb4a6667c312&newsletterV3Id=69561b2e7b9e&user=Spatium&userId=eb4a6667c312&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Libra
Incentix](https://miro.medium.com/fit/c/40/40/0*WJMilSqJXb71gIb1.jpg)](/@Libra_Incentix?source=read_next_recirc
---------0---------------------f7e3ea59_4159_44e7_a152_3c7c4acc2c77-------)

[Libra Incentix

](/@Libra_Incentix?source=read_next_recirc---------0---------------------
f7e3ea59_4159_44e7_a152_3c7c4acc2c77-------)

## 📣 Libra Incentix marketplace: what you need to know.

![](https://miro.medium.com/focal/112/112/50/50/1*et3h4hRICP2d9j0ffE-7Og.jpeg)](/@Libra_Incentix/libra-
incentix-marketplace-what-you-need-to-
know-133095c06ff5?source=read_next_recirc---------0---------------------
f7e3ea59_4159_44e7_a152_3c7c4acc2c77-------)

[[![Victor Kelechi
Kingsley](https://miro.medium.com/fit/c/40/40/1*-lqdBbczsmlf54nT-03R3A.jpeg)](/@officialmrawesome?source=read_next_recirc
---------1---------------------f7e3ea59_4159_44e7_a152_3c7c4acc2c77-------)

[Victor Kelechi Kingsley

](/@officialmrawesome?source=read_next_recirc---------1---------------------
f7e3ea59_4159_44e7_a152_3c7c4acc2c77-------)

## " While we were absent minded, a virus has eaten deep into Crypto and will
soon take all your money.

![](https://miro.medium.com/focal/112/112/50/50/1*fzc5GKs7KaCUEsRhZ09DnA.jpeg)](/@officialmrawesome/while-
we-were-absent-minded-a-virus-has-eaten-deep-into-crypto-and-will-soon-take-
all-your-money-dfb7572ac32d?source=read_next_recirc---------1
---------------------f7e3ea59_4159_44e7_a152_3c7c4acc2c77-------)

[[![Sibca
Awan](https://miro.medium.com/fit/c/40/40/1*-CSeTC_po0RKJOExWUOr8A.jpeg)](/@sibca?source=read_next_recirc
---------2---------------------f7e3ea59_4159_44e7_a152_3c7c4acc2c77-------)

[Sibca Awan

](/@sibca?source=read_next_recirc---------2---------------------
f7e3ea59_4159_44e7_a152_3c7c4acc2c77-------)

in

[Coinmonks

](https://medium.com/coinmonks?source=read_next_recirc---------2
---------------------f7e3ea59_4159_44e7_a152_3c7c4acc2c77-------)

## Bluemetaverse Offers Peer-To-Peer Tools That Bridge NFTs With The Metaverse

![](https://miro.medium.com/focal/112/112/50/50/1*QS42iSnPY4AzuKjTJTI8QA.png)](/coinmonks/bluemetaverse-
offers-peer-to-peer-tools-that-bridge-nfts-with-the-
metaverse-3255e91456c3?source=read_next_recirc---------2---------------------
f7e3ea59_4159_44e7_a152_3c7c4acc2c77-------)

[[![F2Pool 🐟](https://miro.medium.com/fit/c/40/40/2*tA6hhNuR-
jmtEx9vKp0J5A.png)](/@f2pool?source=read_next_recirc---------3
---------------------f7e3ea59_4159_44e7_a152_3c7c4acc2c77-------)

[F2Pool 🐟

](/@f2pool?source=read_next_recirc---------3---------------------
f7e3ea59_4159_44e7_a152_3c7c4acc2c77-------)

in

[f2pool

](https://medium.com/f2pool?source=read_next_recirc---------3
---------------------f7e3ea59_4159_44e7_a152_3c7c4acc2c77-------)

## [PoW Round-Up] Mining revenue bounced back, Bitcoiners to meet in Miami

![](https://miro.medium.com/focal/112/112/50/50/0*XOpC0Ztjk-1V6gV7)](/f2pool/pow-
round-up-mining-revenue-bounced-bitcoiners-to-meet-in-miami-
cd0339c0d7da?source=read_next_recirc---------3---------------------
f7e3ea59_4159_44e7_a152_3c7c4acc2c77-------)

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

