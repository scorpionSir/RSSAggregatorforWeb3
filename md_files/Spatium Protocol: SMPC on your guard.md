[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/d78a243f519&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Spatium
Blog](https://miro.medium.com/fit/c/64/64/1*Af7ihrFRI_0VaZWS9EcuKA.png)](https://medium.com/spatium-
blog?source=post_page-----d78a243f519--------------------------------)

Published in

[Spatium Blog

](https://medium.com/spatium-blog?source=post_page-----
d78a243f519--------------------------------)

[![Spatium](https://miro.medium.com/fit/c/96/96/1*Af7ihrFRI_0VaZWS9EcuKA.png)](/@spatium_news?source=post_page
-----d78a243f519--------------------------------)

[Spatium](/@spatium_news?source=post_page-----
d78a243f519--------------------------------)

Follow

Nov 8, 2019

·

7 min read

# Spatium Protocol: SMPC on your guard

![](https://miro.medium.com/max/1400/0*Emp9m0RQwucTWWUC.png)

In our first article, we explored [the problem of private
keys](http://bit.ly/2IR5xq3), and in the second one, we covered [the three
principles, which could be used to solve it](http://bit.ly/2pG5dDG). Now let’s
discuss in detail how Spatium implements in its product the first principle —
transactions signing without the private keys.

# The protocol logic

Spatium Protocol is an open cryptographic protocol, which allows to sign
transactions on the blockchain in a distributed way with the use of Secure
Multi-Party Computation (SMPC). Within this architecture, we incorporate a
variety of well-proven algorithms: Elliptic Curve Diffie-Hellman exchange
algorithm, Paillier homomorphic encryption scheme, and Elliptic Curve Digital
Signature Algorithm (ECDSA) extension under the name of Threshold Signature
(TS).

![](https://miro.medium.com/max/1400/0*wZRcR3c7_Fayz5sK.png)

A generalized scheme of the interaction between parties is as follows:

  1. Each party uses its own partial (as in “belonging to the party” rather than “being a part of something”) secret independently generated and stored separately from other parties (i.e., on separate devices).
  2. Wallet addresses are formed and transactions are created as a result of the interaction between K out of N parties. Private keys are never generated and used, which eliminates the possibility of secret data loss due to one of the parties getting compromised.

Spatium’s Protocol has been designed in compliance with the concept of “zero
trust”: every party/device is assumed to be trustless, so access to user data
is managed by SMPC. The formation of ECDSA signatures is performed through a
distributed signature algorithm over the partial secrets, which eliminates the
possibility of constructing a private key on one of the devices without
compromising every single device. This technology allows users to arbitrarily
set the number of parties needed to form a correct transaction. Step-by-step
inspection of a transaction formation can also be maintained.

To obtain unauthorized access to the funds, an adversary must simultaneously
compromise each of the parties participating in our protocol, which is
extremely unlikely.

# Simplified plain-english explanation of the tech

The secret participating in transactions signing and a public key generation
does not leave the device where it is stored. And the secret cannot be figured
out even if one were to hack the transaction process by compromising one of
the devices. So, since one cannot maliciously collect all the secrets in one
place (unless every single device is compromised — which is practically
impossible), the attacker cannot construct a private key out of those secrets.
Moreover, due to the distributed nature of our signing algorithm, the private
key is never actually used.

How are transactions signed, then? Since signing process usually involves some
mathematical manipulation of data using a private key (and since secrets are
not a key though they can be used to get one), we get the following:

A transaction data is partially signed (via certain mathematical manipulation)
by the first secret. After that, the data is encrypted and passed to the next
device, where it is also partially signed without decrypting, and so forth.
Encrypting ensures that no party has access to the secret of another party.
Once all of the devices have participated in the algorithm based on Spatium
Protocol, a result is obtained equal to the result of the mathematical
manipulations that would be received using the ephemeral private key, but
without such private key. The public key is generated in the same way.

To illustrate the above explanation, let’s consider an extremely simple
example in terms of natural numbers. **Note: this example does not represent
the actual algorithm used.**

Imagine there are two secrets. Secret 1: 13 and Secret 2: 11.

A private key created from these two secrets is 11*13=143.

Let’s say we need to sign the number 2 (where “2” stands in for the
transaction). We need to get 143*2=286 for a successful signing. The first
party generates a random number 3, performs the following calculation:

13*2*3=78, and sends the result to the second party. This party generates a
random number 5, calculates 78*11*5=4290, and sends it back to the first
secret. Then, the first party performs the calculation 4290/3=1430 and passes
the result to the second party that performs the calculation 1430/5=286 and
sends it back to the first party. As a result, we get a transaction (the “2”)
signed with the private key (“143”) without passing the actual secrets
anywhere.

# Use cases and benefits

We see two general ways for this technology usage. Let’s explore what benefits
(beyond the elimination of a single point of failure and the security level
increase) both of them bring to the market.

>  _Case A: secrets are distributed between devices of funds owner._

Today, to perform actions with funds, the user must employ various
technological solutions for each use case: online payments (web wallets and
software wallets mostly), offline payments (software wallets), work with dApps
(software wallets), trading and token sale participation (software and
hardware wallets), long-term HODLing (hardware wallets and cold storage). Each
technological solution has its own number of authentication factors, keys
management approaches, and their reservation methods. Such fragmentation is
highly inconvenient from the UX point of view and negatively affects the
funds’ safety, as people tend to sacrifice the security for management
comfort.

With the use of distributed secrets, Spatium protocol makes it possible to
build a complex platform that will include benefits of different storage
solutions. Users can create their own authorization methods, based on this
platform, to access their digital assets.

Following the protocol, the user generates the secret on his device and
specify devices to generate and then store additional secrets. The number of
parties that can store secrets and participate in the transaction signing can
be N-of-N or M-of-N, respectively. The customer can combine devices with
secrets the way he wants to configure authorization requirements, optimal for
each use-case: smartphone + smartwatches for shopping; laptop + smartphone for
trading; all at the same time (inc. a biometric wallet) to store millions.

This approach provides simple accessibility: funds owner accesses his account
with the number of digital assets’ addresses and manages conditions for a
particular wallet access from the app.

>  ** _Let’s save your money:_** _with SMPC you can turn your old smartphone
> into a hardware wallet for free._

It is important to note, that such a technological solution is fully anonymous
and provides a great level of autonomy for users with high requirements for
decentralization.

>  _Case B: secrets are distributed between the device of funds owner and
> counterparties._

This approach can be used when the user wants to share the responsibility for
the funds’ safety with the entity, able to provide professional-level security
for the secret on its side. As the security provider has only its own secret
with the specific set of permissions, it can’t perform any action with funds
without the user’s consent.

Beyond funds safety, this solution can provide users with a convenient way to
manage funds: as a user and the security provider are connected (via the
authorization and the split access to funds), it becomes possible to implement
solutions, able to provide the opportunity for instant
deposits/withdrawals/trades performing right from the users’ wallet with on-
chain confirmations processed afterward.

We call this solution — **Hybrid**.

Let’s explore the example with Secret 1 kept on the user’s side and Secret 2
stored on the server-side of the security provider. Such counterparty can be a
custodial service, exchange, bank, or Spatium itself. After the user generates
Secret 1 on his side, he chooses the party for Secret 2 storing and sets
permissions. When the institution generates Secret 2 on its side, the user can
perform actions with the funds: Secret 1 on his device will be used to sign
the transaction, while Secret 2 on the side of the professional security
provider will be used to confirm the transaction.

Described architecture makes it possible to implement conditional
authorization, which can not be implemented with private keys, because once
the attacker gets access to them, he can use the keys outside the user’s
security solution (software wallet/hardware wallet/etc.) and perform any
action with funds without limitations.

Benefits of the Hybrid solution:

  1. Enterprise-level security for funds with the full control on the user’s side;
  2. The user can get the secret’s backup, stored on the security provider’s side, by request.
  3. The user is provided with centralized-like experience, while funds are stored in a decentralized way (conditional authorization, 2FA, whitelist, withdrawal limits, etc. — any logic can be deployed on the server).

What is main here: SMPC provides the ability to distinguish the responsibility
over funds from the control. This solves problems related to a (non) custodial
storage. Services can offer for their users secure storage solutions, with the
opportunity to manage funds in a fast and convenient way.

# Outro

SMPC eliminates problems of private keys, brings its own benefits. Some of
them (like hybrid approach) are unique on the market and can help the whole
crypto industry to become more secure, convenient and foster its mass
adoption.

In this article, we haven’t discussed how secrets can be reserved and how
transactions are signed on the cryptography level. We will explore these
subjects in detail in the following materials.

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
d78a243f519--------------------------------)

Keyless & genuinely decentralized solution to manage digital assets.

[Read more from Spatium Blog](/spatium-blog?source=post_page-----
d78a243f519--------------------------------)

## Recommended from Medium

[[![Ayaan
Shah](https://miro.medium.com/fit/c/40/40/1*o_f50CihLv2L0WKsumBDzw.jpeg)](/@Ayaan_Shah?source=post_internal_links
---------0----------------------------)

[Ayaan Shah

](/@Ayaan_Shah?source=post_internal_links---------
0----------------------------)

in

[Infinity Ventures Crypto Blog

](https://medium.com/ivcrypto?source=post_internal_links---------
0----------------------------)

## Metaverse: Digital Plots More Valuable Than Real Land

![](https://miro.medium.com/focal/112/112/50/50/0*Qwfex6aDDd0dCbcF)](/ivcrypto/metaverse-
digital-plots-more-valuable-than-real-
land-8175c42ff87a?source=post_internal_links---------
0----------------------------)

[[![Coinsandcoins](https://miro.medium.com/fit/c/40/40/1*THj766vMNwyH8lx1bqKWkQ.jpeg)](/@coinsandcoins1?source=post_internal_links
---------1----------------------------)

[Coinsandcoins

](/@coinsandcoins1?source=post_internal_links---------
1----------------------------)

## National Financial Institution of Ukraine Momentarily Outlaws Cross-Border
Crypto Purchases With…

](/@coinsandcoins1/national-financial-institution-of-ukraine-momentarily-
outlaws-cross-border-crypto-purchases-
with-54103754d10c?source=post_internal_links---------
1----------------------------)

[[![Richard Yao](https://miro.medium.com/fit/c/40/40/1*hzUTWdVGsz-
KO_qy3SxLqA.jpeg)](/@richardyaoipg?source=post_internal_links---------
2----------------------------)

[Richard Yao

](/@richardyaoipg?source=post_internal_links---------
2----------------------------)

in

[IPG Media Lab

](https://medium.com/ipg-media-lab?source=post_internal_links---------
2----------------------------)

## The Rise of NFTs and What It Means for Marketers

![](https://miro.medium.com/focal/112/112/50/50/1*bBaGLEBtJiT2AbDdNSZa7A.png)](/ipg-
media-lab/the-rise-of-nfts-and-what-it-means-for-
marketers-628efc68c90?source=post_internal_links---------
2----------------------------)

[[![Autumnlowery](https://miro.medium.com/fit/c/40/40/0*LxXDT2oIN4AyZAJ1.jpg)](/@autumnlowery159355?source=post_internal_links
---------3----------------------------)

[Autumnlowery

](/@autumnlowery159355?source=post_internal_links---------
3----------------------------)

## Best Crypto Payment For Everyone

](/@autumnlowery159355/best-crypto-payment-for-
everyone-397b4ae721a?source=post_internal_links---------
3----------------------------)

[[![Coinsandcoins](https://miro.medium.com/fit/c/40/40/1*THj766vMNwyH8lx1bqKWkQ.jpeg)](/@coinsandcoins1?source=post_internal_links
---------4----------------------------)

[Coinsandcoins

](/@coinsandcoins1?source=post_internal_links---------
4----------------------------)

## Bitcoin atm machine set up in Mexico’s Us senate Structure

](/@coinsandcoins1/bitcoin-atm-machine-set-up-in-mexicos-us-senate-
structure-34ad09afd116?source=post_internal_links---------
4----------------------------)

[[![Thais
Herminia](https://miro.medium.com/fit/c/40/40/0*gUe4Z7bbQxFJMWGJ.)](/@thaisherminia?source=post_internal_links
---------5----------------------------)

[Thais Herminia

](/@thaisherminia?source=post_internal_links---------
5----------------------------)

## Receive digital coins FREE! That, is true love 💖

![](https://miro.medium.com/focal/112/112/50/50/0*LxPn7rwAVRl7kf75.jpg)](/@thaisherminia/receive-
digital-coins-free-that-is-true-love-cebb9cefd0be?source=post_internal_links
---------5----------------------------)

[[![ZENZO
Ecosystem](https://miro.medium.com/fit/c/40/40/1*xnlS1VgncGcqI2rF-6P6wA.png)](/@zenzo-
ecosystem?source=post_internal_links---------6----------------------------)

[ZENZO Ecosystem

](/@zenzo-ecosystem?source=post_internal_links---------
6----------------------------)

## Beginner’s Guide: ZENZO Core, Forge & KOTA Demo

![](https://miro.medium.com/focal/112/112/50/50/1*E4sU7YFG6CkapwZsK-5nSg.png)](/@zenzo-
ecosystem/beginners-guide-zenzo-core-forge-kota-
demo-a722748d38cf?source=post_internal_links---------
6----------------------------)

[[![Cifris](https://miro.medium.com/fit/c/40/40/1*0cZYVi28mQ-
NnXTLUo2DMA.jpeg)](/@cifrisnft?source=post_internal_links---------
7----------------------------)

[Cifris

](/@cifrisnft?source=post_internal_links---------
7----------------------------)

## How to make money with NFT: 5 relevant ways

![](https://miro.medium.com/focal/112/112/50/50/1*8QvdPLBAZMwxFV0nfMbMbQ.jpeg)](/@cifrisnft/how-
to-make-money-with-nft-5-relevant-ways-d25167f289f?source=post_internal_links
---------7----------------------------)

[](/?source=post_page-----d78a243f519--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
d78a243f519--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
d78a243f519--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
d78a243f519--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
d78a243f519--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----d78a243f519--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----d78a243f519--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fspatium-
blog%2Fspatium-protocol-smpc-on-your-guard-d78a243f519&source=post_page
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
blog%2Fspatium-protocol-smpc-on-your-
guard-d78a243f519&newsletterV3=eb4a6667c312&newsletterV3Id=69561b2e7b9e&user=Spatium&userId=eb4a6667c312&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Pedro
Santos](https://miro.medium.com/fit/c/40/40/2*n-a1NOE0AsYvKz4dbGOHSA.jpeg)](/@jdoctor279?source=read_next_recirc
---------0---------------------8051222f_f0e8_4db6_a8fc_d75c28cf2f05-------)

[Pedro Santos

](/@jdoctor279?source=read_next_recirc---------0---------------------
8051222f_f0e8_4db6_a8fc_d75c28cf2f05-------)

## Tectone23 : The Future of Blockchain Smartphones

![](https://miro.medium.com/focal/112/112/50/50/1*nJ3rNEU49S03jpxNlvl49A.jpeg)](/@jdoctor279/tectone23-the-
future-of-blockchain-smartphones-1f9cd8af131f?source=read_next_recirc---------
0---------------------8051222f_f0e8_4db6_a8fc_d75c28cf2f05-------)

[[![WhiteSwap
Finance](https://miro.medium.com/fit/c/40/40/1*9vnxgGXwKu16fvphG6b5Og.png)](/@whiteswap?source=read_next_recirc
---------1---------------------8051222f_f0e8_4db6_a8fc_d75c28cf2f05-------)

[WhiteSwap Finance

](/@whiteswap?source=read_next_recirc---------1---------------------
8051222f_f0e8_4db6_a8fc_d75c28cf2f05-------)

in

[WhiteSwapFi

](https://medium.com/whiteswapfi?source=read_next_recirc---------1
---------------------8051222f_f0e8_4db6_a8fc_d75c28cf2f05-------)

## Tron-Ethereum token migration announcement

![](https://miro.medium.com/focal/112/112/50/50/1*5pHKijv1cqiCpB6yE7Thgg.jpeg)](/whiteswapfi/tron-
ethereum-token-migration-announcement-a44a542a12ec?source=read_next_recirc
---------1---------------------8051222f_f0e8_4db6_a8fc_d75c28cf2f05-------)

[[![Pantera](https://miro.medium.com/fit/c/40/40/1*s95NO2chmUd-
iOP6Baxo5g.png)](/@panterabch?source=read_next_recirc---------2
---------------------8051222f_f0e8_4db6_a8fc_d75c28cf2f05-------)

[Pantera

](/@panterabch?source=read_next_recirc---------2---------------------
8051222f_f0e8_4db6_a8fc_d75c28cf2f05-------)

in

[Coinmonks

](https://medium.com/coinmonks?source=read_next_recirc---------2
---------------------8051222f_f0e8_4db6_a8fc_d75c28cf2f05-------)

## SmartBCH: An Analysis Of The First Six Months — LeoFinance

![](https://miro.medium.com/focal/112/112/50/50/0*aWug0qeeRLGgdLOT)](/coinmonks/smartbch-
an-analysis-of-the-first-six-months-leofinance-
bd9616fa40a8?source=read_next_recirc---------2---------------------
8051222f_f0e8_4db6_a8fc_d75c28cf2f05-------)

[[![Eric
Wales](https://miro.medium.com/fit/c/40/40/1*vwyvUkACuHr_qO0toAlnQw.jpeg)](/@eric.wales.54?source=read_next_recirc
---------3---------------------8051222f_f0e8_4db6_a8fc_d75c28cf2f05-------)

[Eric Wales

](/@eric.wales.54?source=read_next_recirc---------3---------------------
8051222f_f0e8_4db6_a8fc_d75c28cf2f05-------)

## How to create your own token and get an operating loan from Ethereum.org
with Multi-swap

![](https://miro.medium.com/focal/112/112/50/50/1*tJNizX44onVnqPNgXWXq9A.png)](/@eric.wales.54/how-
to-create-your-own-token-and-get-an-operating-loan-from-ethereum-org-with-
multi-swap-d1fc5b0e2e1d?source=read_next_recirc---------3---------------------
8051222f_f0e8_4db6_a8fc_d75c28cf2f05-------)

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

