[](https://medium.com/)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/f4938a1bee11&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](https://medium.com/)

[Home](https://medium.com/)

[Notifications](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Enigma](https://miro.medium.com/fit/c/64/64/1*aIQTqQDM97_LBgHTkHGqcA.png)](https://blog.enigma.co/?source=post_page
-----f4938a1bee11--------------------------------)

Published in

[Enigma

](https://blog.enigma.co/?source=post_page-----
f4938a1bee11--------------------------------)

[![Enigma
Project](https://miro.medium.com/fit/c/96/96/2*2SRmuGkTHWle_KyV3jfGhQ.png)](https://medium.com/@EnigmaMPC?source=post_page
-----f4938a1bee11--------------------------------)

[Enigma Project](https://medium.com/@EnigmaMPC?source=post_page-----
f4938a1bee11--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F4f5f09fa22fb&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fenigma-
development-update-
april-2020-f4938a1bee11&user=Enigma+Project&userId=4f5f09fa22fb&source=post_page-4f5f09fa22fb
----f4938a1bee11---------------------follow_byline-----------)

May 5, 2020

·

5 min read

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Ff4938a1bee11&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fenigma-
development-update-
april-2020-f4938a1bee11&source=--------------------------bookmark_header-----------)

[

Save

](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Ff4938a1bee11&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fenigma-
development-update-
april-2020-f4938a1bee11&source=--------------------------bookmark_header-----------)

# Enigma Development Update — April 2020

## We have achieved our second major milestone (out of three) on the path to
secret contracts! Plus: Secret Zone and Secret Apps.

![](https://miro.medium.com/max/1400/1*sPwc3zPlQhtgCuGGoYEtoQ.png)

Hello to the community! What follows is a recap of important updates from the
past month, **as well as an announcement regarding our newest development
milestone.** This post expands upon our usual [weekly updates on the
developers forum](https://forum.enigma.co/t/enigma-community-update-
may-1-2020/1578) and includes ways for developers, validators, and community
members to get more involved with the project!

Last month was busy and exciting for the Enigma dev team! Most importantly,
**we reached**[ **milestone 2 of
3**](https://forum.enigma.co/t/milestone-2-of-3-cosmwasm-in-sgx-without-
encryption/1548) **on the path to enabling secret contracts, which means
compiling and running a full node with**[
**wasmi**](https://paritytech.github.io/wasmi/wasmi/index.html) **inside**[
**SGX**](https://software.intel.com/sgx) **.** All basic functionality for
executing [CosmWasm](https://www.cosmwasm.com/) contracts in a secure enclave
is now implemented and tested! You can follow our progress by looking at our
[GitHub project
boards](https://github.com/enigmampc/EnigmaBlockchain/projects) for each dev
sprint. We’ve also made progress on the SafeTrace API for privacy-preserving
contact tracing, and we’re currently participating in the Cosmos Game of
Zones. Keep reading for all the details!

# SafeTrace: Privacy-Preserving Contact Tracing API

Following our [announcement of the SafeTrace project](/safetrace-privacy-
preserving-contact-tracing-for-covid-19-c5ae8e1afa93) in March, we built an
MVP demo and front-end integration, joined the TCN Coalition, and hosted a
[webinar with Outlier Ventures](https://youtu.be/BCikIjwvhB4) to explore
SafeTrace’s capabiilities. Outlier also presented their work on
[APEX](/enigma-data-sharing-without-liability-50dfde071207), a collaborative
analytics product built on the Enigma Discovery network. The goal is to
leverage our expertise and create something useful (and privacy-preserving!)
in response to the COVID-19 pandemic. For more info, you can read our full
update on [SafeTrace](https://github.com/enigmampc/safeTrace).

[

## SafeTrace: April 2020 Development Update

### We’ve built an MVP demo and front-end integration, joined the TCN
Coalition, and will host an upcoming webinar with…

blog.enigma.co

](/safetrace-april-2020-development-update-4c5f77bfddfa)

# Cosmos Game of Zones

Recently, we have been gearing up for the [Game of
Zones](https://goz.cosmosnetwork.dev), a series of adversarial testnet
challenges designed to prepare the Cosmos ecosystem for the upcoming launch of
the IBC module. Our dev team has created an [IBC
zone](https://github.com/enigmampc/EnigmaBlockchain/releases/tag/goz), which
relayers will use to interact with our “[Secret Zone.](/secret-zone-making-
privacy-one-with-the-cosmos-20cd72551f2e)” Learn more about how the Enigma
blockchain fits into the Cosmos ecosystem here:

[

## Secret Zone: Making Privacy One With the Cosmos

### How the Enigma Blockchain Fits Into the Cosmos Ecosystem

blog.enigma.co

](/secret-zone-making-privacy-one-with-the-cosmos-20cd72551f2e)

# Protocol Development: Enabling Secret Contracts

Since deploying the Enigma blockchain in February of this year, we have been
focused on building the necessary components for private computation inside
Trusted Execution Environments (TEEs), namely Intel SGX. This work, led by
Guy, Assaf, Tom and Reuven, comprises many specific tasks, organized into
these project milestones on GitHub:

  * [Milestone 1](https://github.com/enigmampc/EnigmaBlockchain/milestone/1) — Integrating Smart Contracts into the Enigma Blockchain **(complete!)**
  * [Milestone 2](https://github.com/enigmampc/EnigmaBlockchain/milestone/2) — Executing CosmWasm Smart Contracts in SGX **(complete!)**
  * [Milestone 3](https://github.com/enigmampc/EnigmaBlockchain/milestone/3) — Adding Encryption for Secret Contracts Running in SGX

Achieving milestone 2 required integrating an internal runtime (wasmi) inside
the SGX enclave. We also fixed some CosmWasm [issues along the
way](https://github.com/enigmampc/EnigmaBlockchain/issues/126). We anticipated
this would be challenging, and it turned out to be even more so, given the
original runtime that comes with CosmWasm (Wasmer) is incompatible with SGX.
This, along with defining clear boundaries between code that lives outside the
enclave (untrusted code) and inside the enclave (trusted code) meant that we
needed to surgically remove Wasmer from CosmWasm internals and develop our own
VM interface that interconnects smart contract executions on our blockchain
with the new enclave-enabled wasmi runtime.

## Read more about our design approach:

[

## Secret Contracts on Enigma Blockchain

### Secret Contracts on Enigma Blockchain This post describes our current
thinking around bringing Secret Contract…

forum.enigma.co

](https://forum.enigma.co/t/secret-contracts-on-enigma-blockchain/1284)

[

## (Dev discussion/Issue) WASM implementation

### One feedback that we've received frequently is that a lot of our
development happens behind closed doors. We want to…

forum.enigma.co

](https://forum.enigma.co/t/dev-discussion-issue-wasm-implementation/1303)

# What does this mean for developers?

As of now, developers have the ability to deploy smart contracts (though not
yet secret contracts) on the [Enigma blockchain
testnet](https://github.com/chainofsecrets/KamutBlockchain). The `compute`
module gives the ability to run the CosmWasm state machine inside trusted
execution environments maintained by node operators. As our dev team continues
to make progress towards enabling secret contracts, we are focused on
improving our developer onboarding process (and looking for help). Our goal is
to make it as easy as possible for Rust developers to build and deploy
contracts on the Enigma testnet. Please let us know if you have any feedback
on our current documentation:

## [Enigma Blockchain Contracts Guide: initial walkthrough for working with
the cosmwasm-based smart contracts on the Secret
Network](https://github.com/enigmampc/enigma-blockchain-contracts-guide)

[

## enigmampc/enigma-blockchain-contracts-guide

### This repository can be used to get up and running on a local Enigma
Blockchain developer testnet (enigmadev) to start…

github.com

](https://github.com/enigmampc/enigma-blockchain-contracts-guide)

Learn more and help us with testing by sharing feedback [here on the
forum](https://forum.enigma.co/t/developer-walkthrough-update-testers-
wanted/1514):

[

## Developer Walkthrough Update -- Testers wanted!

### Dev-X Status Update As you know, we're currently hard at work doing the
R&D for upgrade proposals to the Enigma…

forum.enigma.co

](https://forum.enigma.co/t/developer-walkthrough-update-testers-wanted/1514)

# What does this mean for node runners?

Achieving this new milestone has been exciting, and it means we’re one step
closer to proposing secret contract functionality to the mainnet blockchain.
From that point forward, validators would need to use SGX-enabled hardware to
participate as “secret nodes” in the network. If you want to launch an SGX
node and become a validator, here are the instructions:

  1. How to [install SGX](https://github.com/enigmampc/EnigmaBlockchain/blob/master/docs/dev/setup-sgx.md)
  2. How to [run a full node](https://github.com/enigmampc/EnigmaBlockchain/blob/master/docs/validators-and-full-nodes/run-full-node-mainnet.md)
  3. How to [be a validator](https://github.com/enigmampc/EnigmaBlockchain/blob/master/docs/validators-and-full-nodes/join-validator-mainnet.md)

[As mentioned previously](/the-future-of-enigma-a-letter-from-the-
ceo-c149cf3b0b11), **we are currently exploring an incentivized testnet that
will allow testnet validators to receive Secret (SCRT) while helping us test
out secret contract functionality!** If you’re interested in being notified
when we’re able to share more details, please fill out [this
form](https://airtable.com/shrBVxhT82kZxZ91L):

## [Secret Games Interest Form](https://airtable.com/shrBVxhT82kZxZ91L)

# Our Next Milestone

Read more on GitHub: [CosmWasm Inside SGX With
Encryption](https://github.com/enigmampc/EnigmaBlockchain/milestone/3)

[

## enigmampc/EnigmaBlockchain

### You can't perform that action at this time. You signed in with another tab
or window. You signed out in another tab or…

github.com

](https://github.com/enigmampc/EnigmaBlockchain/milestone/3)

![](https://miro.medium.com/max/144/0*c03oGNbGvablROeK)

# Summary

Overall, we’re thrilled to keep building toward the vision of Secret Apps.
We’re continuing research into various use cases, including coin mixers,
access control, secret voting and more! Please don’t hesitate to reach out
with any ideas or questions. You can find our team and community on
[Discord](http://enigma.co/discord) and the [developers
forum](http://forum.enigma.co).

Stay tuned for our weekly community updates and Governance Working Group
discussions. Our next call is planned for this Friday at 12:00pm EDT. We’ll
share the link on [Discord](http://enigma.co/discord) and on the community-
hosted [RocketChat](http://chat.secret.foundation).

As always, thank you for being a part of our mission to bring essential
privacy solutions to the blockchain space — and to make privacy a public good!
We are deeply grateful for your support.

Onwards and upwards,

— _The Enigma Team_

![](https://miro.medium.com/max/1400/0*dtLAgol2OFwFKgPY.png)

 **To discuss the Enigma protocol or receive technical support:  
**[
_Forum_](http://forum.enigma.co/?source=post_page---------------------------)
_|_[
_Discord_](https://discord.gg/SJK32GY?source=post_page---------------------------)
_|_[
_Twitter_](https://twitter.com/enigmampc?source=post_page---------------------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fenigmampc%2Ff4938a1bee11&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fenigma-
development-update-
april-2020-f4938a1bee11&user=Enigma+Project&userId=4f5f09fa22fb&source=-----f4938a1bee11
---------------------clap_footer-----------)

\--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fenigmampc%2Ff4938a1bee11&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fenigma-
development-update-
april-2020-f4938a1bee11&user=Enigma+Project&userId=4f5f09fa22fb&source=-----f4938a1bee11
---------------------clap_footer-----------)

\--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fenigmampc%2Ff4938a1bee11&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fenigma-
development-update-
april-2020-f4938a1bee11&user=Enigma+Project&userId=4f5f09fa22fb&source=-----f4938a1bee11
---------------------clap_footer-----------)

\--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Ff4938a1bee11&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fenigma-
development-update-
april-2020-f4938a1bee11&source=--------------------------bookmark_footer-----------)

## [More from Enigma](https://blog.enigma.co/?source=post_page-----
f4938a1bee11--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Fenigmampc%2Ff4938a1bee11&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fenigma-
development-update-
april-2020-f4938a1bee11&collection=Enigma&collectionId=6cb5d792f282&source=post_page
-----f4938a1bee11---------------------follow_footer-----------)

Official Blog of Enigma - Securing the Decentralized Web.

[Read more from Enigma](https://blog.enigma.co/?source=post_page-----
f4938a1bee11--------------------------------)

## Recommended from Medium

[[![3Сommas
Blog](https://miro.medium.com/fit/c/40/40/1*j_eo807TRgXa36dLiH_8mg.png)](https://3commastutorials.medium.com/?source=post_internal_links
---------0----------------------------)

[3Сommas Blog

](https://3commastutorials.medium.com/?source=post_internal_links---------
0----------------------------)

## Storing information on the blockchain

![](https://miro.medium.com/focal/112/112/50/50/0*IaZO-
vMoJb0DLkqT)](https://3commastutorials.medium.com/storing-information-on-the-
blockchain-ecd6da74a403?source=post_internal_links---------
0----------------------------)

[[![GokuMarket
Exchange](https://miro.medium.com/fit/c/40/40/1*fyrWB8ZxzKK9aBXqo4LcdA.png)](https://gokumarket.medium.com/?source=post_internal_links
---------1----------------------------)

[GokuMarket Exchange

](https://gokumarket.medium.com/?source=post_internal_links---------
1----------------------------)

in

[GokuMarket

](https://medium.com/gokumarket?source=post_internal_links---------
1----------------------------)

## Brave to Integrate with @Solana Blockchain on its Privacy-enabled #Browser

![](https://miro.medium.com/focal/112/112/50/50/1*2Yvn7CQ06dPSLpkex5uEig.png)](https://medium.com/gokumarket/brave-
to-integrate-with-solana-blockchain-on-its-privacy-enabled-
browser-d5aa37ce5bdb?source=post_internal_links---------
1----------------------------)

[[![TronFi](https://miro.medium.com/fit/c/40/40/1*rHVelii65iq6CqzNTT7-ZQ.png)](https://tronfi.medium.com/?source=post_internal_links
---------2----------------------------)

[TronFi

](https://tronfi.medium.com/?source=post_internal_links---------
2----------------------------)

## Salmon code open-sourced and apply for audit, Pearl code time-locked.

](https://tronfi.medium.com/salmon-code-open-sourced-and-apply-for-audit-
pearl-code-time-locked-ccc5e884525d?source=post_internal_links---------
2----------------------------)

[[![IIB
Council](https://miro.medium.com/fit/c/40/40/1*8rrfp1rz35nY4WRzMTCTHg.png)](https://medium.com/@iibcouncil?source=post_internal_links
---------3----------------------------)

[IIB Council

](https://medium.com/@iibcouncil?source=post_internal_links---------
3----------------------------)

## What is blockchain? (A Complete Guide for Beginners) — IIB Council

![](https://miro.medium.com/focal/112/112/50/50/0*54hT05XcW_MWjM2_.jpg)](https://medium.com/@iibcouncil/what-
is-blockchain-a-complete-guide-for-beginners-iib-
council-4efdd3253327?source=post_internal_links---------
3----------------------------)

[[![belguso](https://miro.medium.com/fit/c/40/40/0*-0rKmucNVIUZR70z)](https://medium.com/@belguso988?source=post_internal_links
---------4----------------------------)

[belguso

](https://medium.com/@belguso988?source=post_internal_links---------
4----------------------------)

## Let’s Earn — Runs on Blockchain Auto Stakeout Protocol

![](https://miro.medium.com/focal/112/112/50/50/0*ZJcLY7_LbHZK03LQ)](https://medium.com/@belguso988/lets-
earn-runs-on-blockchain-auto-stakeout-
protocol-4687298a508a?source=post_internal_links---------
4----------------------------)

[[![ZOYBLOC](https://miro.medium.com/fit/c/40/40/1*eaU0XlQbTJhX5Jhd3LHBfw.png)](https://medium.com/@zoybloc?source=post_internal_links
---------5----------------------------)

[ZOYBLOC

](https://medium.com/@zoybloc?source=post_internal_links---------
5----------------------------)

## Values of ZOYBLOC Part 1

![](https://miro.medium.com/focal/112/112/50/50/1*zfShSXKeMRejSl8UICfclQ.png)](https://medium.com/@zoybloc/values-
of-zoybloc-part-1-d556670f583?source=post_internal_links---------
5----------------------------)

[[![Lumenswap](https://miro.medium.com/fit/c/40/40/1*fhtIn95cqWHB6FxfkAd1Ug.jpeg)](https://medium.com/@lumenswap?source=post_internal_links
---------6----------------------------)

[Lumenswap

](https://medium.com/@lumenswap?source=post_internal_links---------
6----------------------------)

in

[Lumenswap

](https://medium.com/lumenswap?source=post_internal_links---------
6----------------------------)

## Ninth milestone — DAO

![](https://miro.medium.com/focal/112/112/50/50/1*QFkUF49vybuaqdMQmckauw.jpeg)](https://medium.com/lumenswap/ninth-
milestone-dao-dbecb5b03e3a?source=post_internal_links---------
6----------------------------)

[[![XTRABYTES™
\(XBY\)](https://miro.medium.com/fit/c/40/40/1*8UCC0DTTThUev2U_xBNtJg.png)](https://medium.com/@XTRABYTES?source=post_internal_links
---------7----------------------------)

[XTRABYTES™ (XBY)

](https://medium.com/@XTRABYTES?source=post_internal_links---------
7----------------------------)

## The Unfortunate Rise of Permission Blockchains

![](https://miro.medium.com/focal/112/112/50/50/0*X5U54YeZBUlQFO0g.png)](https://medium.com/@XTRABYTES/the-
unfortunate-rise-of-permission-
blockchains-6ed3e2bee4e9?source=post_internal_links---------
7----------------------------)

[](https://medium.com/?source=post_page-----
f4938a1bee11--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
f4938a1bee11--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
f4938a1bee11--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
f4938a1bee11--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
f4938a1bee11--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----f4938a1bee11--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----f4938a1bee11--------------------------------)

[Get
started](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fenigma-
development-update-april-2020-f4938a1bee11&source=post_page
--------------------------nav_reg-----------)

[![Enigma
Project](https://miro.medium.com/fit/c/176/176/2*2SRmuGkTHWle_KyV3jfGhQ.png)](https://medium.com/@EnigmaMPC)

[

## Enigma Project

](https://medium.com/@EnigmaMPC)

6.5K Followers

Enigma is securing the decentralized web. We solve for privacy with “secret”
smart contracts, allowing dApps and blockchains to use private/sensitive data.

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F4f5f09fa22fb&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fenigma-
development-update-
april-2020-f4938a1bee11&user=Enigma+Project&userId=4f5f09fa22fb&source=post_page-4f5f09fa22fb
-------------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Ffcc87216ce8e&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fenigma-
development-update-
april-2020-f4938a1bee11&newsletterV3=4f5f09fa22fb&newsletterV3Id=fcc87216ce8e&user=Enigma+Project&userId=4f5f09fa22fb&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Rusty
Stanberry](https://miro.medium.com/fit/c/40/40/1*fVTiKqeHHgyPw9fSVOVWAg.jpeg)](https://medium.com/@rstanberry?source=read_next_recirc
---------0---------------------a368899a_46e0_4c48_8a20_3a3bbc001b33-------)

[Rusty Stanberry

](https://medium.com/@rstanberry?source=read_next_recirc---------0
---------------------a368899a_46e0_4c48_8a20_3a3bbc001b33-------)

## Why you shouldn’t use the Polygon Bridge.

![](https://miro.medium.com/focal/112/112/50/50/0*Tl_gLe6FDLZkq-6X)](https://medium.com/@rstanberry/why-
you-shouldnt-use-the-polygon-bridge-a3dc5245e6bc?source=read_next_recirc
---------0---------------------a368899a_46e0_4c48_8a20_3a3bbc001b33-------)

[[![Christina
Ramsey](https://miro.medium.com/fit/c/40/40/0*7AdTtg97JMM5I1p2.jpg)](https://medium.com/@christinajohnson-
ramsey?source=read_next_recirc---------1---------------------
a368899a_46e0_4c48_8a20_3a3bbc001b33-------)

[Christina Ramsey

](https://medium.com/@christinajohnson-ramsey?source=read_next_recirc---------
1---------------------a368899a_46e0_4c48_8a20_3a3bbc001b33-------)

in

[Helium Foundation

](https://medium.com/decentralized-wireless-alliance?source=read_next_recirc
---------1---------------------a368899a_46e0_4c48_8a20_3a3bbc001b33-------)

## New Name for the Manufacturing Oversight Committee

![](https://miro.medium.com/focal/112/112/50/50/0*KB0ke5A--hH-
NBm-)](https://medium.com/decentralized-wireless-alliance/new-name-for-the-
manufacturing-oversight-committee-729eb12bf075?source=read_next_recirc
---------1---------------------a368899a_46e0_4c48_8a20_3a3bbc001b33-------)

[[![JaviWalk](https://miro.medium.com/fit/c/40/40/1*GeLKsWfO-8i5B6T8ngYgnw.jpeg)](https://medium.com/@JaviWalk?source=read_next_recirc
---------2---------------------a368899a_46e0_4c48_8a20_3a3bbc001b33-------)

[JaviWalk

](https://medium.com/@JaviWalk?source=read_next_recirc---------2
---------------------a368899a_46e0_4c48_8a20_3a3bbc001b33-------)

## So… What are ‘cryptocurrencies’ anyway?

![](https://miro.medium.com/focal/112/112/50/50/1*O1v6nISWvkZLKuiQ3UMxjQ.jpeg)](https://medium.com/@JaviWalk/so-
what-are-cryptocurrencies-anyway-f373e68e48e2?source=read_next_recirc---------
2---------------------a368899a_46e0_4c48_8a20_3a3bbc001b33-------)

[[![Emma
Theo](https://miro.medium.com/fit/c/40/40/1*LSC12DXxNgPXDjY3cnwYaQ.png)](https://medium.com/@emmanuelneduobi?source=read_next_recirc
---------3---------------------a368899a_46e0_4c48_8a20_3a3bbc001b33-------)

[Emma Theo

](https://medium.com/@emmanuelneduobi?source=read_next_recirc---------3
---------------------a368899a_46e0_4c48_8a20_3a3bbc001b33-------)

## Cypherdog Security: Protecting The Cyberspace!

![](https://miro.medium.com/focal/112/112/50/50/1*5g_-G67gI78SvXKEXp968w.jpeg)](https://medium.com/@emmanuelneduobi/cypherdog-
security-protecting-the-cyberspace-395d0c981452?source=read_next_recirc
---------3---------------------a368899a_46e0_4c48_8a20_3a3bbc001b33-------)

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

