[](https://medium.com/)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/28d25261359c&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](https://medium.com/)

[Home](https://medium.com/)

[Notifications](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Enigma](https://miro.medium.com/fit/c/64/64/1*aIQTqQDM97_LBgHTkHGqcA.png)](https://blog.enigma.co/?source=post_page
-----28d25261359c--------------------------------)

Published in

[Enigma

](https://blog.enigma.co/?source=post_page-----
28d25261359c--------------------------------)

[![James
Waugh](https://miro.medium.com/fit/c/96/96/2*Q4zRpsuf4GKFMEuZjWyC_w.jpeg)](https://medium.com/@jwaup?source=post_page
-----28d25261359c--------------------------------)

[James Waugh](https://medium.com/@jwaup?source=post_page-----
28d25261359c--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F4ae4fe949e3c&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fenigma-
development-update-
may-2020-28d25261359c&user=James+Waugh&userId=4ae4fe949e3c&source=post_page-4ae4fe949e3c
----28d25261359c---------------------follow_byline-----------)

Jun 4, 2020

·

5 min read

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F28d25261359c&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fenigma-
development-update-
may-2020-28d25261359c&source=--------------------------bookmark_header-----------)

[

Save

](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F28d25261359c&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fenigma-
development-update-
may-2020-28d25261359c&source=--------------------------bookmark_header-----------)

# Enigma Development Update: May 2020

## Learn about the latest progress towards privacy-preserving Secret Apps and
the next exciting milestone: the launch of a public “secret contracts”
incentivized testnet in July.

![](https://miro.medium.com/max/1400/1*pSU8DGQ36lVM94c94_8EZw.png)

 _[You can also read this announcement on the_[ _Secret
Blog_](https://blog.scrt.network/secret-network-development-update-may-2020)
_.]_

Hello to the Secret Network community! What follows is a recap of important
updates from the past month, including our progress towards “[secret
contracts](/defining-secret-contracts-f40ddee67ef2)” and new documentation of
encryption specs. This post expands upon our regular updates on the [Secret
Forum](https://forum.scrt.network) and includes ways for developers,
validators, and other community members to get more involved with the project!

In May, the Enigma team made significant progress toward achieving [milestone
3 of 3](https://github.com/enigmampc/SecretNetwork/milestone/3) on the path to
enabling secret contracts on [Secret Network](https://scrt.network), which
means compiling and running a full node with
[wasmi](https://paritytech.github.io/wasmi/wasmi/index.html) inside
[SGX](https://software.intel.com/sgx) with encryption abilities. All basic
functionality for executing [CosmWasm](https://www.cosmwasm.com/) contracts in
a secure enclave is now implemented and continues to be tested! You can follow
our progress by reviewing our dev sprints on these [GitHub project
boards](https://github.com/enigmampc/EnigmaBlockchain/projects).

What does this mean? **We now expect to have the first public testnet for
secret contracts live in the month of July, coinciding with the start of the
Secret Games.** We’ll continue to share regular updates on development
progress on the [Secret Network forum](https://forum.scrt.network) — and we
have more info about this testnet later in this post. Keep reading for all the
details!

# Protocol Development: Enabling Secret Contracts

Since our community launched the Secret Network in February of this year, we
have been focused on building the necessary components for private computation
inside Trusted Execution Environments (TEEs), namely Intel SGX. This work, led
by Guy, Assaf, Tom, Reuven and Itzik, comprises many specific tasks, organized
into these project milestones on GitHub:

  * [Milestone 1](https://github.com/enigmampc/SecretNetwork/milestone/1) — Integrating Smart Contracts into the Enigma Blockchain (complete!)
  * [Milestone 2 ](https://github.com/enigmampc/SecretNetwork/milestone/2)— Executing CosmWasm Smart Contracts in SGX (complete!)
  * [Milestone 3](https://github.com/enigmampc/SecretNetwork/milestone/3) — Adding Encryption for Secret Contracts Running in SGX

Lately, our team has been focused on WIP documentation for the cryptography
elements of the secret protocol. This means encrypted inputs, outputs and
state. Read more about Milestone 3 on GitHub: [CosmWasm Inside SGX With
Encryption](https://github.com/enigmampc/EnigmaBlockchain/milestone/3). We’d
appreciate any feedback on our new documentation of Enigma’s cryptography
specifications.

## Encryption Specs (wip):

[

## enigmampc/SecretNetwork

### ⚠️ This is a very advanced WIP. Before the genesis of a new chain, there
must be a bootstrap node to generate…

github.com

](https://github.com/enigmampc/EnigmaBlockchain/blob/master/docs/encryption-
specs.md)

 **Discuss on the Secret Forum:**

[

## An update on the encryption protocol

### Hi! 👋 We're pretty close to finalizing our encryption protocol: This^
document includes: Bootstrapping the network…

forum.scrt.network

](https://forum.scrt.network/t/an-update-on-the-encryption-protocol/1641)

# What does this mean for developers?

Developers will soon have the ability to deploy secret contracts on the
[Secret Testnet](https://github.com/chainofsecrets/secrettestnet.io),
maintained by Chain of Secrets. Our `compute` module for the Cosmos SDK gives
the ability to run CosmWasm inside trusted execution environments (TEEs)
maintained by node operators (secret nodes). As our dev team continues to make
progress towards enabling secret contracts, we are focused on improving our
developer onboarding process and looking for help. The goal is to make it as
easy as possible for Rust developers to build and deploy contracts. Please let
us know if you have any feedback on our current documentation:

[

## enigmampc/enigma-blockchain-contracts-guide

### This repository can be used to get up and running on a local Enigma
Blockchain developer testnet (enigmadev) to start…

github.com

](https://github.com/enigmampc/enigma-blockchain-contracts-guide)

## What does this mean for node runners?

Building toward this new milestone has been exciting, and it means we’re one
step closer to proposing secret contract functionality to the Secret Network.
From that point forward, validators will need to use SGX-enabled hardware to
participate as “secret nodes” in the network.

If you want to launch a node and become a mainnet validator today, here are
the instructions:

  1. [Install SGX](https://github.com/enigmampc/EnigmaBlockchain/blob/master/docs/dev/setup-sgx.md) (optional until secret contracts are on mainnet)
  2. [Run a full node](https://github.com/enigmampc/EnigmaBlockchain/blob/master/docs/validators-and-full-nodes/run-full-node-mainnet.md)
  3. [Be a validator](https://github.com/enigmampc/EnigmaBlockchain/blob/master/docs/validators-and-full-nodes/join-validator-mainnet.md)

[As mentioned previously](/the-future-of-enigma-a-letter-from-the-
ceo-c149cf3b0b11), we are currently planning an incentivized testnet program,
called the Secret Games, that will allow developers and testnet validators to
receive Secret (SCRT) while helping us test secret contract functionality! If
you’re interested in being notified when we share more details, please fill
out [this form](https://airtable.com/shrBVxhT82kZxZ91L):

## [Secret Games Interest Form](https://airtable.com/shrBVxhT82kZxZ91L)

# CosmWasm

Recently, we have been collaborating with the [CosmWasm
team](https://www.cosmwasm.com), which is building a smart contracting
platform for the [Cosmos ecosystem](https://cosmos.network). The [Cosmos
SDK](https://docs.cosmos.network), [Tendermint](https://tendermint.com) and
the [Inter-Blockchain Communication protocol](https://github.com/cosmos/ics)
are designed to enable scalable, interoperable application-specific
blockchains. Enigma’s dev team is excited to contribute alongside Ethan Frey
and Simon Warta to develop modules for WASM computation. They have invited
Reuven to be a core contributor of the CosmWasm project, following some
updates made in coordination with releasing version 0.8 of CosmWasm. Stay
tuned for a detailed post on the x/compute module.

We’ve also written recently about how the Secret Network fits into the growing
Cosmos ecosystem. Our privacy solutions can help many zones and other hubs
with interoperable trusted computation services for any blockchain. Secret Hub
facilitates adoption of application-specific networks, which are greater than
the sum of their parts!

## [Secret Hub: Making Privacy One With the
Cosmos](https://blog.scrt.network/secret-hub)

![](https://miro.medium.com/max/1400/1*QJxvP1xunMwWpuG2IhGbpg.png)

# SafeTrace: Privacy-Preserving Contact Tracing API

The Enigma team also continues to develop privacy-first standalone
applications that help solve real-world problems. Since our [April Development
Update on SafeTrace](/safetrace-april-2020-development-update-4c5f77bfddfa),
we have been focused on connecting with app developers and other
collaborators. We are continuing to build relationships as a member of the TCN
Coalition. We also hosted a [webinar with Outlier
Ventures](https://youtu.be/BCikIjwvhB4) to explore capabilities of SafeTrace.
For more info, you can review the documentation in our [open source code
base](https://github.com/enigmampc/safeTrace).

We will have another exciting announcement shortly about the future of
SafeTrace, so stay tuned to the [Enigma blog](https://blog.enigma.co)!

## [SafeTrace: April 2020 Development Update](/safetrace-
april-2020-development-update-4c5f77bfddfa)

![](https://miro.medium.com/max/1400/1*70tXk1wRdHZ4cwgNdsbk4A.png)

# Going Forward

Overall, we’re thrilled to keep building toward the vision of privacy-
preserving Secret Apps. We’re continuing research into various use cases,
including secret voting, access control, and more! Please don’t hesitate to
reach out to our team and the Secret community with any ideas or questions.
You can find us on [RocketChat](https://chat.scrt.network),
[Discord](https://discord.com/invite/SJK32GY), and the [Secret
Forum](http://forum.scrt.network).

Stay tuned for our weekly community updates and governance meetings. Our next
open discussion is planned for this Friday at 2:00pm EDT. Here is the link to
join: <https://meet.scrt.network/discussion>

Thank you for being a part of our mission to bring essential privacy solutions
to the blockchain space — and to make privacy a public good! We are deeply
grateful for your support.

Onwards and upwards,  
 _The Enigma Team_

![](https://miro.medium.com/max/1400/1*nOAbFfwWV3KmBXP7Y012Fw.png)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fenigmampc%2F28d25261359c&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fenigma-
development-update-
may-2020-28d25261359c&user=James+Waugh&userId=4ae4fe949e3c&source=-----28d25261359c
---------------------clap_footer-----------)

\--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fenigmampc%2F28d25261359c&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fenigma-
development-update-
may-2020-28d25261359c&user=James+Waugh&userId=4ae4fe949e3c&source=-----28d25261359c
---------------------clap_footer-----------)

\--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fenigmampc%2F28d25261359c&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fenigma-
development-update-
may-2020-28d25261359c&user=James+Waugh&userId=4ae4fe949e3c&source=-----28d25261359c
---------------------clap_footer-----------)

\--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F28d25261359c&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fenigma-
development-update-
may-2020-28d25261359c&source=--------------------------bookmark_footer-----------)

## [More from Enigma](https://blog.enigma.co/?source=post_page-----
28d25261359c--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Fenigmampc%2F28d25261359c&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fenigma-
development-update-
may-2020-28d25261359c&collection=Enigma&collectionId=6cb5d792f282&source=post_page
-----28d25261359c---------------------follow_footer-----------)

Official Blog of Enigma - Securing the Decentralized Web.

[Read more from Enigma](https://blog.enigma.co/?source=post_page-----
28d25261359c--------------------------------)

## Recommended from Medium

[[![Gwenneth
Liberati](https://miro.medium.com/fit/c/40/40/1*dmbNkD5D-u45r44go_cf0g.png)](https://prosecutory2004.medium.com/?source=post_internal_links
---------0----------------------------)

[Gwenneth Liberati

](https://prosecutory2004.medium.com/?source=post_internal_links---------
0----------------------------)

## {UPDATE} Little Snake Game Hack Free Resources Generator

](https://prosecutory2004.medium.com/update-little-snake-game-hack-free-
resources-generator-2cefa2180bd6?source=post_internal_links---------
0----------------------------)

[[![Rianon
Nerin](https://miro.medium.com/fit/c/40/40/1*dmbNkD5D-u45r44go_cf0g.png)](https://sugan1900.medium.com/?source=post_internal_links
---------1----------------------------)

[Rianon Nerin

](https://sugan1900.medium.com/?source=post_internal_links---------
1----------------------------)

## {UPDATE} Leviathan: The Last Day of the Decade Visual Novel Hack Free
Resources Generator

](https://sugan1900.medium.com/update-leviathan-the-last-day-of-the-decade-
visual-novel-hack-free-resources-
generator-b1b94408ed7d?source=post_internal_links---------
1----------------------------)

[[![Brandea
Sletten](https://miro.medium.com/fit/c/40/40/1*dmbNkD5D-u45r44go_cf0g.png)](https://bannerall1940.medium.com/?source=post_internal_links
---------2----------------------------)

[Brandea Sletten

](https://bannerall1940.medium.com/?source=post_internal_links---------
2----------------------------)

## {UPDATE} 攻城三國 M-SLG策略國戰 Hack Free Resources Generator

](https://bannerall1940.medium.com/update-攻城三國-m-slg策略國戰-hack-free-resources-
generator-19617c2b799?source=post_internal_links---------
2----------------------------)

[[![Best Roof
Guy](https://miro.medium.com/fit/c/40/40/1*R1w8S9oN91Zrr0qCUUTXbA.jpeg)](https://medium.com/@bestroofguyTX?source=post_internal_links
---------3----------------------------)

[Best Roof Guy

](https://medium.com/@bestroofguyTX?source=post_internal_links---------
3----------------------------)

## Baltimore Homeowners Protect Yourself From Roofing Scams

](https://medium.com/@bestroofguyTX/baltimore-homeowners-protect-yourself-
from-roofing-scams-da08337b29d9?source=post_internal_links---------
3----------------------------)

[[![Graham
Perry](https://miro.medium.com/fit/c/40/40/1*gvGCw4olnezmLDK40tn9Kg.jpeg)](https://iamgrahamperry.medium.com/?source=post_internal_links
---------4----------------------------)

[Graham Perry

](https://iamgrahamperry.medium.com/?source=post_internal_links---------
4----------------------------)

## Zoom Meeting of the Commodity Arbitration Club! Join ME!

![](https://miro.medium.com/focal/112/112/50/50/0*LQzJhFZoYxdkukZl.jpg)](https://iamgrahamperry.medium.com/zoom-
meeting-of-the-commodity-arbitration-club-join-
me-10c0e299b08e?source=post_internal_links---------
4----------------------------)

[[![Seclore](https://miro.medium.com/fit/c/40/40/1*r4eKIp1PVEXRHvPlwWAVsA.png)](https://seclore.medium.com/?source=post_internal_links
---------5----------------------------)

[Seclore

](https://seclore.medium.com/?source=post_internal_links---------
5----------------------------)

## Seclore Launches Data-Centric Security for Microsoft Teams

](https://seclore.medium.com/seclore-launches-data-centric-security-for-
microsoft-teams-186cef18b945?source=post_internal_links---------
5----------------------------)

[[![Judith J.
Francis](https://miro.medium.com/fit/c/40/40/1*dmbNkD5D-u45r44go_cf0g.png)](https://medium.com/@francisjud?source=post_internal_links
---------6----------------------------)

[Judith J. Francis

](https://medium.com/@francisjud?source=post_internal_links---------
6----------------------------)

## Cyber security: Cyber crime: an unprecedented threat to society?

](https://medium.com/@francisjud/cyber-security-cyber-crime-an-unprecedented-
threat-to-society-36adcc46bb7e?source=post_internal_links---------
6----------------------------)

[[![iteo](https://miro.medium.com/fit/c/40/40/1*pijZTbezQdYlST4hP6DNWw.png)](https://iteo.medium.com/?source=post_internal_links
---------7----------------------------)

[iteo

](https://iteo.medium.com/?source=post_internal_links---------
7----------------------------)

## Brain hacking — attacker methods to get what they want

![](https://miro.medium.com/focal/112/112/50/50/1*VMLqfENGCI2Sq2zc-Q0qSA.png)](https://iteo.medium.com/brain-
hacking-attacker-methods-to-get-what-they-
want-7d5ac3aa59bc?source=post_internal_links---------
7----------------------------)

[](https://medium.com/?source=post_page-----
28d25261359c--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
28d25261359c--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
28d25261359c--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
28d25261359c--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
28d25261359c--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----28d25261359c--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----28d25261359c--------------------------------)

[Get
started](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fenigma-
development-update-may-2020-28d25261359c&source=post_page
--------------------------nav_reg-----------)

[![James
Waugh](https://miro.medium.com/fit/c/176/176/2*Q4zRpsuf4GKFMEuZjWyC_w.jpeg)](https://medium.com/@jwaup)

[

## James Waugh

](https://medium.com/@jwaup)

94 Followers

multidimensional human #cre8

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F4ae4fe949e3c&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fenigma-
development-update-
may-2020-28d25261359c&user=James+Waugh&userId=4ae4fe949e3c&source=post_page-4ae4fe949e3c
-------------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fusers%2F4ae4fe949e3c%2Flazily-
enable-writer-
subscription&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fenigma-
development-update-
may-2020-28d25261359c&user=James+Waugh&userId=4ae4fe949e3c&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Joe
Walker](https://miro.medium.com/fit/c/40/40/1*NoKl8fHJhdTOSO7WjwrkeQ.jpeg)](https://medium.com/@IAmJoeWalker?source=read_next_recirc
---------0---------------------54d7d3f6_cf6d_46d6_b1b0_4bf2ea888620-------)

[Joe Walker

](https://medium.com/@IAmJoeWalker?source=read_next_recirc---------0
---------------------54d7d3f6_cf6d_46d6_b1b0_4bf2ea888620-------)

## KOIN Tokenomics part 2: how to assess real value based on mana

![](https://miro.medium.com/focal/112/112/50/50/1*2alrltyxtOA-W456eZDL8g.png)](https://medium.com/@IAmJoeWalker/koin-
tokenomics-part-2-how-to-assess-real-value-based-on-
mana-f69007f7e617?source=read_next_recirc---------0---------------------
54d7d3f6_cf6d_46d6_b1b0_4bf2ea888620-------)

[[![Hipo](https://miro.medium.com/fit/c/40/40/1*1bPB2ag4W0zrdxnGcNo4IQ.png)](https://medium.hipo.one/?source=read_next_recirc
---------1---------------------54d7d3f6_cf6d_46d6_b1b0_4bf2ea888620-------)

[Hipo

](https://medium.hipo.one/?source=read_next_recirc---------1
---------------------54d7d3f6_cf6d_46d6_b1b0_4bf2ea888620-------)

## Hipo vs. Other Protocols: What’s the Difference

![](https://miro.medium.com/focal/112/112/50/50/1*_gNfErLq8eAtr2X_qaSLjA.jpeg)](https://medium.hipo.one/hipo-
vs-other-protocols-whats-the-difference-a3936629bb74?source=read_next_recirc
---------1---------------------54d7d3f6_cf6d_46d6_b1b0_4bf2ea888620-------)

[[![crypt
osi](https://miro.medium.com/fit/c/40/40/0*hP1WScz49hyYutvo.)](https://medium.com/@cryptosixxx?source=read_next_recirc
---------2---------------------54d7d3f6_cf6d_46d6_b1b0_4bf2ea888620-------)

[crypt osi

](https://medium.com/@cryptosixxx?source=read_next_recirc---------2
---------------------54d7d3f6_cf6d_46d6_b1b0_4bf2ea888620-------)

## RubySwap Monthly Burn #7 May 2022

![](https://miro.medium.com/focal/112/112/50/50/1*FahYa2XKghtAPRuU24V-Rg.png)](https://medium.com/@cryptosixxx/rubyswap-
monthly-burn-7-may-2022-5e40416fc2d0?source=read_next_recirc---------2
---------------------54d7d3f6_cf6d_46d6_b1b0_4bf2ea888620-------)

[[![Poornima](https://miro.medium.com/fit/c/40/40/0*AzQ8h8xvMNrHx1VB.jpg)](https://poornima-
ks.medium.com/?source=read_next_recirc---------3---------------------
54d7d3f6_cf6d_46d6_b1b0_4bf2ea888620-------)

[Poornima

](https://poornima-ks.medium.com/?source=read_next_recirc---------3
---------------------54d7d3f6_cf6d_46d6_b1b0_4bf2ea888620-------)

## Game Theory

](https://poornima-ks.medium.com/game-
theory-67fafbcee1db?source=read_next_recirc---------3---------------------
54d7d3f6_cf6d_46d6_b1b0_4bf2ea888620-------)

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

