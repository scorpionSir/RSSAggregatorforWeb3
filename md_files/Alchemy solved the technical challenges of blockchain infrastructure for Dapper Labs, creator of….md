[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/faebba35e0e7&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Dapper
Labs](https://miro.medium.com/fit/c/64/64/1*4qrJW34TWRKo2UlCo9IqbQ.png)](https://medium.com/dapperlabs?source=post_page
-----faebba35e0e7--------------------------------)

Published in

[Dapper Labs

](https://medium.com/dapperlabs?source=post_page-----
faebba35e0e7--------------------------------)

[![Dapper
Labs](https://miro.medium.com/fit/c/96/96/1*4qrJW34TWRKo2UlCo9IqbQ.png)](/@hellodapper?source=post_page
-----faebba35e0e7--------------------------------)

[Dapper Labs](/@hellodapper?source=post_page-----
faebba35e0e7--------------------------------)

Follow

Nov 26, 2019

·

4 min read

# Alchemy and Dapper Labs teaming up to solve blockchain infrastructure
problems

![](https://miro.medium.com/max/1400/1*t4qpnZFmLcvegubcs0248Q.png)

Blockchain development can be rewarding and full of interesting technical
problems.

We have built a few applications and continue to do so. If you have built a
dApp or plan to, you may see that building blockchain applications (dApps) has
a lot of known and unknown challenges. Some of the problems with blockchain
infrastructure are well documented but difficult to resolve, such as nodes
being out of sync or transactions failing. In this article, we explore how our
infrastructure evolved as we aimed to solve these problems, highlighting the
learnings along the way.

Here at Dapper Labs, we tried a few infrastructure-as-a-service solutions and
running our own nodes. In the end, we were happy to find
[Alchemy](https://alchemyapi.io/), a team who we worked with to solve the
challenges of blockchain infrastructure which should’ve been solved at the
protocol level.

# Our first external infrastructure-service provider was flawed

As we scale and build new consumer experiences we often ran into problems with
the native infrastructure on Ethereum. Performance was unstable, with hours of
full outages, nodes being out of sync with the network, and congestion when
submitting transactions. Nonce management was so poor that we began storing
this ourselves. We knew this wasn’t going to be a viable solution as we
expanded our users and gaming experiences.

# We preferred to run our own nodes rather than use a broken product

Without a clear path forward, we took matters into our own hands and ran our
own nodes. We found slightly better consistency, or at least the ability to
diagnose and solve problems as soon as they occur rather than wait for
customer support.

Running our own nodes took two developers around two weeks to initially set
up. However, these developers needed to make ongoing changes to the
infrastructure to solve problems as they emerged. Load balancing caused
network-state consistency issues, so we built clusters of nodes that went
straight to failover instead. If our nodes fell out of sync, we would fail
over to the next node and only point to one node at a time. Still, problems
continued to occur.

These node issues propagated to CryptoKitties users. We had a community
manager but no support to troubleshoot specific customer complaints. When
nodes broke, Cryptokitties would get backed up and kitten births would not
happen. Transactions were sent to the network, but users could not see them.
For instance, one CryptoKitties token would seemingly have two owners.

Many problems were difficult to diagnose and solve, but the culprit was the
stability of our geth nodes on a congested network. When we would experience
one to two hours of downtime, we knew we needed a better solution. We added
health checks to compare the head of the chain to Etherscan. Even so, peer
connections were dropped abruptly.

# Introduction our work with Alchemy

While our engineers were able to run a more stable infrastructure than our
first external infrastructure provider, running nodes in house was not a
perfect solution. When we found out about Alchemy, we learned that Alchemy had
already built a scalable solution that we could plug in and help automate our
existing processes. We could shift the burden of diagnosis, troubleshooting,
and maintenance to Alchemy, while maintaining uptime for our players.

After trying Alchemy, the Dapper Labs team found that Alchemy’s product solved
our consistency issues and was simply a reliable, stable product. Our work
with Alchemy has allowed us to extend beyond our current capacity and deliver
a great experience for players on CryptoKitties, Cheeze Wizards, and other
projects.

Alchemy’s core product has allowed us to make over 7 million queries a day to
the network, run the top blockchain dApp worldwide, and submit over 1200 ETH
in transactions, including $28M+ in sales. We were able to re-resource our
node developers to build other games and Flow. Our teams work very closely
together to launch new products and ensure a seamless user experience.

# Key takeaway is find a solution that simply works

We recommend trying various solutions like we did to find an infrastructure
product that serves consistent, reliable blockchain data and writes
transactions without risk of failure. Ideally, depending on your bandwidth,
your chosen solution does not require constant maintenance. We are super happy
with Alchemy since the team is comprised of blockchain experts who we trust to
solve the technical challenges of blockchain infrastructure.

We plan to release future posts on blockchain architecture! In the past, we
have written about [how to build a dApp](/dapperlabs/cryptokitties-tips-how-
to-build-a-decentralized-application-3d5353f6bcc7). We plan to continue
sharing our experiences with architecture and infrastructure here.

Built a dApp? We’d also love to hear about your experiences!

Learn more about [Alchemy here](https://alchemyapi.io/)!

A lot of our challenges building CryptoKitties informed our approach to Flow,
a developer-friendly blockchain Dapper Labs is helping to create. [You can
learn more about Flow here](http://withflow.org/)!

\--

\--

\--

## [More from Dapper Labs](/dapperlabs?source=post_page-----
faebba35e0e7--------------------------------)

The serious business of fun and games on the blockchain

[Read more from Dapper Labs](/dapperlabs?source=post_page-----
faebba35e0e7--------------------------------)

## Recommended from Medium

[[![Blockperks](https://miro.medium.com/fit/c/40/40/1*TG6Mx3LVCgDcGrlxymR_Gw.jpeg)](/@Blockperks_NFT?source=post_internal_links
---------0----------------------------)

[Blockperks

](/@Blockperks_NFT?source=post_internal_links---------
0----------------------------)

## Introducing Blockperks NFT Marketplace — A Future for Creators

![](https://miro.medium.com/focal/112/112/50/50/1*bSKsm8UgL5LTsnS79cDddw.jpeg)](/@Blockperks_NFT/introducing-
blockperks-nft-marketplace-a-future-for-
creators-69ef86e87ca?source=post_internal_links---------
0----------------------------)

[[![Agafon
Dombrov](https://miro.medium.com/fit/c/40/40/0*QF_Qa2YByC4kK8_l)](/@agafoncrypto?source=post_internal_links
---------1----------------------------)

[Agafon Dombrov

](/@agafoncrypto?source=post_internal_links---------
1----------------------------)

## Blockchain. Why is it so important for the crypto industry?

![](https://miro.medium.com/focal/112/112/50/50/1*OWg_wszdb2OgQbbhpYUDvA.png)](/@agafoncrypto/blockchain-
why-is-it-so-important-for-the-crypto-industry-
dda36ff059fe?source=post_internal_links---------1----------------------------)

[[![BonFi
Admin](https://miro.medium.com/fit/c/40/40/1*J_ub5vxuwfcPKoVUPHZjQw.png)](/@bonfi-
org?source=post_internal_links---------2----------------------------)

[BonFi Admin

](/@bonfi-org?source=post_internal_links---------
2----------------------------)

in

[BonFi (bon.finance)

](https://medium.com/bonfiorg?source=post_internal_links---------
2----------------------------)

## BonFi available on Nerve Network!

![](https://miro.medium.com/focal/112/112/50/50/1*YsdgqUgcgASSJZvWEfwXuw.png)](/bonfiorg/bonfi-
available-on-nerve-network-b073e4f714ed?source=post_internal_links---------
2----------------------------)

[[![Cassiopeia
Services](https://miro.medium.com/fit/c/40/40/1*d3IwfBzt13Mtkp1W9LPQow.png)](/@cassiopeiaservicesltd?source=post_internal_links
---------3----------------------------)

[Cassiopeia Services

](/@cassiopeiaservicesltd?source=post_internal_links---------
3----------------------------)

## Building a commodity ecosystem through blockchain

![](https://miro.medium.com/focal/112/112/50/50/1*bAUORcGDoHfPhrU4-yOePg.png)](/@cassiopeiaservicesltd/building-
a-commodity-ecosystem-through-
blockchain-30a9a8d58a0b?source=post_internal_links---------
3----------------------------)

[[![Farmchain
Finance](https://miro.medium.com/fit/c/40/40/1*yLbKOvHpKZXwcjfMf_ciBw.jpeg)](/@farmchain-
finance?source=post_internal_links---------4----------------------------)

[Farmchain Finance

](/@farmchain-finance?source=post_internal_links---------
4----------------------------)

## Nodes Dashboard Launch

![](https://miro.medium.com/focal/112/112/50/50/1*QO2bvR-
MlqOoeJU3QzdV6A.jpeg)](/@farmchain-finance/nodes-dashboard-
launch-6fbe279af69a?source=post_internal_links---------
4----------------------------)

[[![Project
Markh](https://miro.medium.com/fit/c/40/40/1*bs_4-CccWnhvAeKhhNjmGg.png)](/@projectmarkh?source=post_internal_links
---------5----------------------------)

[Project Markh

](/@projectmarkh?source=post_internal_links---------
5----------------------------)

## Introducing Project Markh!

![](https://miro.medium.com/focal/112/112/50/50/1*1poqJG_bvwC5RHQxHFSEpg.jpeg)](/@projectmarkh/introducing-
project-markh-615c141059b?source=post_internal_links---------
5----------------------------)

[[![Kommunitas](https://miro.medium.com/fit/c/40/40/1*80tbsYxdhT5vlKX7A6o4LQ.png)](/@kommunitas?source=post_internal_links
---------6----------------------------)

[Kommunitas

](/@kommunitas?source=post_internal_links---------
6----------------------------)

## MetaShooter Private Sale has Sold out!

![](https://miro.medium.com/focal/112/112/50/50/1*x7W7zdT7Qzg-5UOguNUhjg.jpeg)](/@kommunitas/metashooter-
private-sale-has-sold-out-f61205cb8bfd?source=post_internal_links---------
6----------------------------)

[[![cc32d9](https://miro.medium.com/fit/c/40/40/1*Ab6aw1XGuCNyZL_c0qc3Hg.png)](/@cc32d9?source=post_internal_links
---------7----------------------------)

[cc32d9

](/@cc32d9?source=post_internal_links---------7----------------------------)

## EOSIO as your blockchain platform of choice

](/@cc32d9/eosio-as-your-blockchain-platform-of-
choice-964ebdcbd25c?source=post_internal_links---------
7----------------------------)

[](/?source=post_page-----faebba35e0e7--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
faebba35e0e7--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
faebba35e0e7--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
faebba35e0e7--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
faebba35e0e7--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----faebba35e0e7--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----faebba35e0e7--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fdapperlabs%2Falchemy-
solved-the-technical-challenges-of-blockchain-infrastructure-for-dapper-labs-
creator-of-faebba35e0e7&source=post_page--------------------------
nav_reg-----------)

[![Dapper
Labs](https://miro.medium.com/fit/c/176/176/1*4qrJW34TWRKo2UlCo9IqbQ.png)](/@hellodapper)

[

## Dapper Labs

](/@hellodapper)

800 Followers

The serious business of fun and games on the blockchain

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F92fd7014333&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fdapperlabs%2Falchemy-
solved-the-technical-challenges-of-blockchain-infrastructure-for-dapper-labs-
creator-of-
faebba35e0e7&newsletterV3=6544777e30d2&newsletterV3Id=92fd7014333&user=Dapper+Labs&userId=6544777e30d2&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Brooker
Belcourt](https://miro.medium.com/fit/c/40/40/1*ZohfvpUrRzEudw6fpC1qQg.jpeg)](/@covey?source=read_next_recirc
---------0---------------------ec09c24a_2658_41fa_b8f2_bc1cc62b73af-------)

[Brooker Belcourt

](/@covey?source=read_next_recirc---------0---------------------
ec09c24a_2658_41fa_b8f2_bc1cc62b73af-------)

in

[Covey

](https://medium.com/covey?source=read_next_recirc---------0
---------------------ec09c24a_2658_41fa_b8f2_bc1cc62b73af-------)

## Our Users Own Their Data

![](https://miro.medium.com/focal/112/112/50/50/1*SO4Wdp43JdMKrb-5epWXiA.png)](/covey/our-
users-own-their-data-f57683ab17c1?source=read_next_recirc---------0
---------------------ec09c24a_2658_41fa_b8f2_bc1cc62b73af-------)

[[![Serenity
Shield](https://miro.medium.com/fit/c/40/40/1*Jdh1QWTjAzTyNwTXk3hmfg.png)](/@SerenityShield?source=read_next_recirc
---------1---------------------ec09c24a_2658_41fa_b8f2_bc1cc62b73af-------)

[Serenity Shield

](/@SerenityShield?source=read_next_recirc---------1---------------------
ec09c24a_2658_41fa_b8f2_bc1cc62b73af-------)

## Serenity Shield — Planning Ahead

![](https://miro.medium.com/focal/112/112/50/50/1*3QOrWce8BvuX6U7my3X6bg.jpeg)](/@SerenityShield/serenity-
shield-planning-ahead-b2ac4b6f969d?source=read_next_recirc---------1
---------------------ec09c24a_2658_41fa_b8f2_bc1cc62b73af-------)

[[![Nathan Carroll](https://miro.medium.com/fit/c/40/40/0*J7oUFh-
D_pMtjm86)](/@nathan.carroll0402?source=read_next_recirc---------2
---------------------ec09c24a_2658_41fa_b8f2_bc1cc62b73af-------)

[Nathan Carroll

](/@nathan.carroll0402?source=read_next_recirc---------2---------------------
ec09c24a_2658_41fa_b8f2_bc1cc62b73af-------)

in

[SphereDAO

](https://medium.com/spheredao?source=read_next_recirc---------2
---------------------ec09c24a_2658_41fa_b8f2_bc1cc62b73af-------)

## Building a Credit System for Cryptocurrencies

![](https://miro.medium.com/focal/112/112/50/50/1*_X8JyCermRSCW_4MyhbE9w.png)](/spheredao/building-
a-credit-system-for-cryptocurrencies-d74a1ad2ec05?source=read_next_recirc
---------2---------------------ec09c24a_2658_41fa_b8f2_bc1cc62b73af-------)

[[![Dharm
Singh](https://miro.medium.com/fit/c/40/40/0*VSiEmNjOrK8BODlA.jpg)](/@DharmSinghAgileSoft?source=read_next_recirc
---------3---------------------ec09c24a_2658_41fa_b8f2_bc1cc62b73af-------)

[Dharm Singh

](/@DharmSinghAgileSoft?source=read_next_recirc---------3---------------------
ec09c24a_2658_41fa_b8f2_bc1cc62b73af-------)

## Blockchain Powering Smart Contracts

![](https://miro.medium.com/focal/112/112/50/50/1*Gn1sFYdludNISHLThAtmaA.jpeg)](/@DharmSinghAgileSoft/blockchain-
powering-smart-contracts-8772843f5442?source=read_next_recirc---------3
---------------------ec09c24a_2658_41fa_b8f2_bc1cc62b73af-------)

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

