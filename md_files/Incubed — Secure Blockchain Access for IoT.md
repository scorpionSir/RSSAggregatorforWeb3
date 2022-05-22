[](https://medium.com/)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/db4687b3dfa1&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](https://medium.com/)

[Home](https://medium.com/)

[Notifications](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![slock.it Blog](https://miro.medium.com/fit/c/64/64/1*ESYB-
YgQa2FKWPo2ofqCiQ.png)](https://blog.slock.it/?source=post_page-----
db4687b3dfa1--------------------------------)

Published in

[slock.it Blog

](https://blog.slock.it/?source=post_page-----
db4687b3dfa1--------------------------------)

[![Simon
Jentzsch](https://miro.medium.com/fit/c/96/96/1*DEDHanvpXujRRBfICx9bHA.png)](https://medium.com/@simon.jentzsch.x7?source=post_page
-----db4687b3dfa1--------------------------------)

[Simon Jentzsch](https://medium.com/@simon.jentzsch.x7?source=post_page-----
db4687b3dfa1--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Faa7a73543e46&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fincubed-
secure-blockchain-access-for-iot-
db4687b3dfa1&user=Simon+Jentzsch&userId=aa7a73543e46&source=post_page-
aa7a73543e46----db4687b3dfa1---------------------follow_byline-----------)

Sep 27, 2019

·

6 min read

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fdb4687b3dfa1&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fincubed-
secure-blockchain-access-for-iot-
db4687b3dfa1&source=--------------------------bookmark_header-----------)

[

Save

](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fdb4687b3dfa1&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fincubed-
secure-blockchain-access-for-iot-
db4687b3dfa1&source=--------------------------bookmark_header-----------)

# Incubed — Secure Blockchain Access for IoT

What does the “S” in IoT stand for? “Secure” … but there is no “S” because
making an IoT device secure _and_ open at the same time is incredibly
difficult.

Let’s demonstrate this difficulty with a simple example. This is our “Sharing
Box.” You can insert anything you want others to use, then set a price and let
somebody rent it. But how do you ensure that only users who have paid are able
to open it?

Most developers would probably set up a server somewhere in the cloud and run
a database to store info regarding who has paid and when. Our small box would
then need a good Wi-Fi connection to access this server. Simple, right?
However, there are major issues with this centralized solution:

  1. There is a single point of failure: If your server is offline for whatever reason, all sharing boxes stop working.
  2. Any hacker could simply attack this server and gain access to all sharing boxes. This would be a nightmare! And please don’t say that your server is safe or that this would never happen; it happens all the time. And if it is not an attacker, your admin may simply be having a bad day.

Scary, isn’t it? So let’s decentralize our Sharing Box! This is where
blockchain comes in. Here we have thousands of nodes, and as long as a single
node runs, the blockchain works. The more nodes are running, the harder it is
for an attacker to overtake the network.

 **Connecting Devices to the Blockchain**

While the blockchain solves a lot of security issues (and it makes payments
much easier!), the question remains: How do we connect our small box to the
blockchain?

![](https://miro.medium.com/max/1400/1*yk0zpf80LS-wqxalAdxuFg.png)

To connect, we usually become a peer and start synchronizing and verifying all
the network’s transactions. For a **full node** on Ethereum, this means we
would need about 140 GB of storage and have to constantly synchronize and
verify blocks and transactions to be sure we had the correct data. This is way
too much for our small box.

To address this issue, smart people optimized storage with the **pruned node**
, which simply tosses older states and reduces the node to only 90 GB. Way
better but still too much.

Once the first **light client** was released, everyone hoped it would finally
solve the storage problem. A light client only stores the data it needs, but
this comes with a price: It relies on full nodes. However, it’s still able to
verify because it constantly syncs with other peers. The light client takes us
down to a few hundred MB, which is good, but that still doesn’t fit on a
microcontroller. Even syncing requires a constant bandwidth, and if you’re
offline for a few days, it takes several minutes to catch up. Bandwidth is
very expensive for mobile devices!

That’s why some developers started to use a so-called **remote client** : a
central full node on a server (or even a centralized RPC service like Infura).
But this is a bad idea since it means we might as well use the unsecure,
centralized server option we mentioned earlier.

# Using Incubed

You see, establishing a secure connection to the blockchain on a small loT
device isn’t easy, but that’s why we built **Incubed** , a stateless client
that can run with zero storage (except for the code and optional cache).
Incubed operates without a single point of failure and is able to verify all
data. Just like a light client uses full nodes to fetch data to verify,
Incubed relies on a set of distributed full nodes. Anybody can run and
register such a node in the registry contract. But other than the light
client, we don’t constantly sync within the peer-to-peer network; we only send
requests as needed. This is important since it means

  1. We get immediate responses (no need to catch up); and
  2. No constant bandwidth reading the blockheaders.

This is crucial not only for IoT devices but also apps and websites connecting
securely to the blockchain. However, if anyone can run such a node, we must be
able to prove and verify the data. (When we talk about data, we mean all
standard [JSON-RPC calls](https://github.com/ethereum/wiki/wiki/JSON-RPC),
including eth_call.)

![](https://miro.medium.com/max/1400/0*cWuhIJ-tRwGkdiwg)

Let’s see how this works by looking at our Sharing Box:

  1. Anybody can use the app and pay to open the box. This is done by sending a transaction to a smart contract, which stores the paid amount and checks all requirements (like KYC and conflicting bookings). If all is good, the transaction is confirmed by creating an event with the public address of the user (the one with permission to open the box) and the time range the user paid for. You can even call this contract a digital twin of the Sharing Box since it defines the rules and behavior of the device. If this transaction is successfully executed, the app only needs to store the transaction hash (which is used as an identifier).
  2. Now, if the user wants to open the box, the app connects to it using Bluetooth and sends a message, which contains:  
\- a signature created with the user’s private key, which verifies that the
data wasn’t manipulated and that the message was authorized by the user;  
\- a timestamp to ensure that nobody can replay it; and  
\- the transaction hash of the previously sent transaction, which tells the
box where the payment occurred.

  3. Our box receives this data and needs to verify that the user who signed the message has permission to do so. This means we need proof that this transaction — and, as a result, the event — _really_ happened on the blockchain. This verification is done by Incubed.   
The Incubed client picks a random public node from a registry contract and
requests the proof for the transaction receipt (the result of an Ethereum
transaction confirming the paid booking). Since the Sharing Box has no
internet connection we let the phone collect the data.  
(If you want to know more about how proofs work, watch this
[video](https://www.youtube.com/watch?v=wlUlypmt6Oo) ).

  4. Once the box has received the response, Incubed verifies the Merkle proof and the blockheader of the transaction receipt. The receipt must contain an event that tells us that who is allowed access and when. If the signer of this signature is the one, we can accept it and **open the door**!

# Verifying the Blockheader

Incubed is able to verify transactions and even functions calls of smart
contracts by using Merkle proofs against a blockheader, but how can we be sure
this blockheader is correct? This depends on the consensus mechanism the
blockchain uses.

![](https://miro.medium.com/max/1400/0*PzLUcT2U2MpVFt4H)

For **proof of authority** , there is a list of keys allowed to sign the
blockheader. To verify the blockheader, we simply check if the signature was
created from a key on the list. Since the signature is part of the
blockheader, this is all we need. (and the correct set of validators)

For **proof of work** (like the public Ethereum chain), anybody can create
blocks as long as he or she is able to put enough work into it. But to know
whether a block is accepted, we ask the registered Incubed nodes to pay a
deposit and sign blockhashes (just the hash of the blockheader). If the nodes
were to sign a wrong hash, they would lose their deposit because this signed
blockhash can be verified by anyone inside a smart contract. All you need is
an independent node checking if the signature is correct before our small box
receives it. Since anybody is incentivized to find a wrong blockhash and can
receive the deposit of the signer, the same node that gave us the proof can
check the signature, which reduces the number of requests. Because the client
chooses which signature to accept, the server cannot cheat and sign with a
different key.

# Putting it on a microcontroller

![](https://miro.medium.com/max/1400/0*tXhC9fnXUUI-DC-X)

This verification allows us to put everything on a small chip like
[nRF52840](https://www.nordicsemi.com/Products/Low-power-short-range-
wireless/nRF52840), which only has 256 KB of RAM and 1 MB of flash memory. One
of these costs about $3 and enables a completely decentralized, stateless, and
verified connection to the blockchain.

Just imagine what else we can build with Incubed!

Simon Jentzsch (CTO, Slock.it)

Resources :

  * <https://github.com/slockit/in3> (TypeScript)
  * <https://github.com/slockit/in3-c> ( C for embedded devices )
  * <https://in3.readthedocs.io/en/develop/> (Developer Documentation )

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fslock-
it-
blog%2Fdb4687b3dfa1&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fincubed-
secure-blockchain-access-for-iot-
db4687b3dfa1&user=Simon+Jentzsch&userId=aa7a73543e46&source=-----db4687b3dfa1
---------------------clap_footer-----------)

\--

1

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fslock-
it-
blog%2Fdb4687b3dfa1&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fincubed-
secure-blockchain-access-for-iot-
db4687b3dfa1&user=Simon+Jentzsch&userId=aa7a73543e46&source=-----db4687b3dfa1
---------------------clap_footer-----------)

\--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fslock-
it-
blog%2Fdb4687b3dfa1&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fincubed-
secure-blockchain-access-for-iot-
db4687b3dfa1&user=Simon+Jentzsch&userId=aa7a73543e46&source=-----db4687b3dfa1
---------------------clap_footer-----------)

\--

1

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fdb4687b3dfa1&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fincubed-
secure-blockchain-access-for-iot-
db4687b3dfa1&source=--------------------------bookmark_footer-----------)

## [More from slock.it Blog](https://blog.slock.it/?source=post_page-----
db4687b3dfa1--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Fslock-
it-
blog%2Fdb4687b3dfa1&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fincubed-
secure-blockchain-access-for-iot-
db4687b3dfa1&collection=slock.it+Blog&collectionId=15115b6d917a&source=post_page
-----db4687b3dfa1---------------------follow_footer-----------)

IoT + Blockchain

[Read more from slock.it Blog](https://blog.slock.it/?source=post_page-----
db4687b3dfa1--------------------------------)

## Recommended from Medium

[[![Infinite Virtual
Space](https://miro.medium.com/fit/c/40/40/1*Lw9yqM2fJPJo93GnHXgR9A.png)](https://infinitevirtualspace.medium.com/?source=post_internal_links
---------0----------------------------)

[Infinite Virtual Space

](https://infinitevirtualspace.medium.com/?source=post_internal_links---------
0----------------------------)

## IVS Weekly Update (18/4)

![](https://miro.medium.com/focal/112/112/50/50/1*P25fCaJb6jGle7YYui87Bg.jpeg)](https://infinitevirtualspace.medium.com/ivs-
weekly-update-18-4-9e5a8283db67?source=post_internal_links---------
0----------------------------)

[[![Gisele
Schout](https://miro.medium.com/fit/c/40/40/2*U0TSOHlJrKuHXz7hl6m-8A.png)](https://medium.com/@gisele_schout?source=post_internal_links
---------1----------------------------)

[Gisele Schout

](https://medium.com/@gisele_schout?source=post_internal_links---------
1----------------------------)

in

[Stakin

](https://medium.com/stakin?source=post_internal_links---------
1----------------------------)

## An Introduction to Near Protocol

![NEAR_Protocol_Introduction_By_Stakin](https://miro.medium.com/focal/112/112/50/50/0*H1satNfGW_NEB-
Fa)](https://medium.com/stakin/an-introduction-to-near-
protocol-1299f9413d7d?source=post_internal_links---------
1----------------------------)

[[![Solanews](https://miro.medium.com/fit/c/40/40/1*oZXsELB0883raR4Qwy2kZQ.png)](https://solanews.medium.com/?source=post_internal_links
---------2----------------------------)

[Solanews

](https://solanews.medium.com/?source=post_internal_links---------
2----------------------------)

## Syndica

![](https://miro.medium.com/focal/112/112/50/50/1*ILXYhm8Ck5Q971XYTcuCLQ.jpeg)](https://solanews.medium.com/syndica-8ebd7eb76d50?source=post_internal_links
---------2----------------------------)

[[![Saurabh
Jha](https://miro.medium.com/fit/c/40/40/0*Et3dXlmPv3XX51ms.jpg)](https://medium.com/@saurabhjha?source=post_internal_links
---------3----------------------------)

[Saurabh Jha

](https://medium.com/@saurabhjha?source=post_internal_links---------
3----------------------------)

## WhatsApp is A BlockChain Hiding in Plain Sight & Its Mass Potential is
Immense

![](https://miro.medium.com/focal/112/112/50/50/1*Bwmk_IQ72g_pWGuEvAei5w.png)](https://medium.com/@saurabhjha/whatsapp-
is-a-blockchain-hiding-in-plain-sight-its-mass-potential-is-
immense-49248a2aac61?source=post_internal_links---------
3----------------------------)

[[![Minda](https://miro.medium.com/fit/c/40/40/2*QUwlPPa57OUc4aNYe87yAw.jpeg)](https://medium.com/@Mindalin?source=post_internal_links
---------4----------------------------)

[Minda

](https://medium.com/@Mindalin?source=post_internal_links---------
4----------------------------)

## Providing solutions to optimizing defi users assets

![](https://miro.medium.com/focal/112/112/50/50/1*dOjhhRZCRkPpbnLeVmdPAg.jpeg)](https://medium.com/@Mindalin/providing-
solutions-to-optimizing-defi-users-
assets-46c3e3b2ae83?source=post_internal_links---------
4----------------------------)

[[![Blockstars](https://miro.medium.com/fit/c/40/40/1*1vJTym8WhpvuMVJMXLedbA.jpeg)](https://blog.blockstars.gg/?source=post_internal_links
---------5----------------------------)

[Blockstars

](https://blog.blockstars.gg/?source=post_internal_links---------
5----------------------------)

## Introducing Blockstars

![](https://miro.medium.com/focal/112/112/50/50/1*wi44w2wYNhh9xRuQTLLBug.jpeg)](https://blog.blockstars.gg/introducing-
blockstars-c8543ecda536?source=post_internal_links---------
5----------------------------)

[[![Quantix](https://miro.medium.com/fit/c/40/40/1*B5WJP3DsO3JYfZO5IPm0tw@2x.jpeg)](https://medium.com/@marketing.quantix?source=post_internal_links
---------6----------------------------)

[Quantix

](https://medium.com/@marketing.quantix?source=post_internal_links---------
6----------------------------)

## Community rewards: DAO & Treasury

![](https://miro.medium.com/focal/112/112/50/50/1*XTyldKnKTfvsP2vuP4Zl6Q.jpeg)](https://medium.com/@marketing.quantix/communirt-
rewards-dao-treasury-8a5052421185?source=post_internal_links---------
6----------------------------)

[[![Jae
Kwon](https://miro.medium.com/fit/c/40/40/1*ZClqep_sUukFEA7aXeMQuw.png)](https://medium.com/@jaekwon?source=post_internal_links
---------7----------------------------)

[Jae Kwon

](https://medium.com/@jaekwon?source=post_internal_links---------
7----------------------------)

in

[HackerNoon.com

](https://medium.com/hackernoon?source=post_internal_links---------
7----------------------------)

## Tendermint 0.8 Release

](https://medium.com/hackernoon/tendermint-0-8-release-
eff1d308b583?source=post_internal_links---------7----------------------------)

[](https://medium.com/?source=post_page-----
db4687b3dfa1--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
db4687b3dfa1--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
db4687b3dfa1--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
db4687b3dfa1--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
db4687b3dfa1--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----db4687b3dfa1--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----db4687b3dfa1--------------------------------)

[Get
started](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fincubed-
secure-blockchain-access-for-iot-db4687b3dfa1&source=post_page
--------------------------nav_reg-----------)

[![Simon
Jentzsch](https://miro.medium.com/fit/c/176/176/1*DEDHanvpXujRRBfICx9bHA.png)](https://medium.com/@simon.jentzsch.x7)

[

## Simon Jentzsch

](https://medium.com/@simon.jentzsch.x7)

74 Followers

CTO Slock,.it

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Faa7a73543e46&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fincubed-
secure-blockchain-access-for-iot-
db4687b3dfa1&user=Simon+Jentzsch&userId=aa7a73543e46&source=post_page-
aa7a73543e46-------------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fusers%2Faa7a73543e46%2Flazily-
enable-writer-
subscription&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fincubed-
secure-blockchain-access-for-iot-
db4687b3dfa1&user=Simon+Jentzsch&userId=aa7a73543e46&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Karlos](https://miro.medium.com/fit/c/40/40/1*B6ew3-sqDUr00-aGP-6RGw.jpeg)](https://medium.com/@karlkino7?source=read_next_recirc
---------0---------------------0c326f92_de78_4d09_a41e_a983a0e80e91-------)

[Karlos

](https://medium.com/@karlkino7?source=read_next_recirc---------0
---------------------0c326f92_de78_4d09_a41e_a983a0e80e91-------)

## Web 3.0 and the danger of proprietary cloud compute services

![](https://miro.medium.com/focal/112/112/50/50/1*1Joh3GY3JEjXgX8zfvdUTA.jpeg)](https://medium.com/@karlkino7/web-3-0-and-
the-danger-of-proprietary-cloud-compute-
services-c1d6372d83e8?source=read_next_recirc---------0---------------------
0c326f92_de78_4d09_a41e_a983a0e80e91-------)

[[![BlockVision](https://miro.medium.com/fit/c/40/40/1*s-AQ6dCj7KRfOtM_jHLogw.png)](https://medium.com/@BlockVision?source=read_next_recirc
---------1---------------------0c326f92_de78_4d09_a41e_a983a0e80e91-------)

[BlockVision

](https://medium.com/@BlockVision?source=read_next_recirc---------1
---------------------0c326f92_de78_4d09_a41e_a983a0e80e91-------)

## BlockVision Live on Optimism to Improve Efficiency Building on Web 3.0

![](https://miro.medium.com/focal/112/112/50/50/1*Q-5E7-SLiUybfgtOHGsalg.png)](https://medium.com/@BlockVision/blockvision-
live-on-optimism-to-improve-efficiency-building-on-
web-3-0-2022e01a03ca?source=read_next_recirc---------1---------------------
0c326f92_de78_4d09_a41e_a983a0e80e91-------)

[[![Rwdaunch](https://miro.medium.com/fit/c/40/40/1*meRTbYWdHVqIjqRjimsq_g@2x.jpeg)](https://medium.com/@ramseydaunch?source=read_next_recirc
---------2---------------------0c326f92_de78_4d09_a41e_a983a0e80e91-------)

[Rwdaunch

](https://medium.com/@ramseydaunch?source=read_next_recirc---------2
---------------------0c326f92_de78_4d09_a41e_a983a0e80e91-------)

## Uniswap Governance: Proposals (Thesis Fodder Part 1)

](https://medium.com/@ramseydaunch/uniswap-governance-proposals-thesis-fodder-
part-1-76dd077a685b?source=read_next_recirc---------2---------------------
0c326f92_de78_4d09_a41e_a983a0e80e91-------)

[[![M-Zohaib Nasir](https://miro.medium.com/fit/c/40/40/1*yFrYQthUU-xQa_-
SG1Z1Ig.jpeg)](https://inthediary.medium.com/?source=read_next_recirc---------
3---------------------0c326f92_de78_4d09_a41e_a983a0e80e91-------)

[M-Zohaib Nasir

](https://inthediary.medium.com/?source=read_next_recirc---------3
---------------------0c326f92_de78_4d09_a41e_a983a0e80e91-------)

## Brownie 101- New Project

![](https://miro.medium.com/focal/112/112/50/50/1*bQF2YgkbYJRM3H9U3LAv-w.png)](https://inthediary.medium.com/brownie-101-new-
project-b53d58467b60?source=read_next_recirc---------3---------------------
0c326f92_de78_4d09_a41e_a983a0e80e91-------)

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

