[](https://medium.com/)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/c35b3a4ec10a&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](https://medium.com/)

[Home](https://medium.com/)

[Notifications](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![slock.it Blog](https://miro.medium.com/fit/c/64/64/1*ESYB-
YgQa2FKWPo2ofqCiQ.png)](https://blog.slock.it/?source=post_page-----
c35b3a4ec10a--------------------------------)

Published in

[slock.it Blog

](https://blog.slock.it/?source=post_page-----
c35b3a4ec10a--------------------------------)

[![Steffen
Kux](https://miro.medium.com/fit/c/96/96/0*59Wk_wX_AKsdO7qx.)](https://medium.com/@steffen.kux?source=post_page
-----c35b3a4ec10a--------------------------------)

[Steffen Kux](https://medium.com/@steffen.kux?source=post_page-----
c35b3a4ec10a--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F2b84d96491a4&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fincubed-
stable-
release-c35b3a4ec10a&user=Steffen+Kux&userId=2b84d96491a4&source=post_page-2b84d96491a4
----c35b3a4ec10a---------------------follow_byline-----------)

Jan 9, 2020

·

6 min read

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fc35b3a4ec10a&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fincubed-
stable-
release-c35b3a4ec10a&source=--------------------------bookmark_header-----------)

[

Save

](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fc35b3a4ec10a&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fincubed-
stable-
release-c35b3a4ec10a&source=--------------------------bookmark_header-----------)

# Incubed — Stable Release

![](https://miro.medium.com/max/1400/1*AHlW99f7btoHIPMEvFHo1A.png)

When Ethereum was conceived, the vision was to have a distributed P2P network
of independent nodes and access to dApps using these nodes, all without any
centralized services.

![](https://miro.medium.com/max/1400/1*J-CyoJwa3wJvx8U9zLkQ7w.png)

In reality, the current situation for most applications looks more like the
illustration below rather than the original ideal of complete
decentralization. The development and use of dApps are already underway, for
several reasons, most dApps rely on remote servers to connect to the
blockchain. It’s a kind of paradox: We connect to the decentralized world
using centralized access.

![](https://miro.medium.com/max/1400/1*j_dGjlf5V8Iy1O0vRGni7Q.png)

One of slock.it’s missions is to enable IoT devices to connect to the
blockchain to give these devices the ability to pay or receive payment for
services, or to realize truly secure access management. Many of these IoT
devices are based on microcontrollers, which are, unfortunately, severely
limited in terms of computing power, memory, storage, and connectivity. The
same also applies to mobile applications on smartphones or web applications.

So, to connect IoT devices to the blockchain securely and sustainably, we need
to enable microcontrollers to run blockchain clients. These devices must be
able to read data from the blockchain, write data into the blockchain, or
interact with smart contracts.

How can this be done? It’s not possible to run a full node on such a device,
and even a light client is, at best, only feasible on a high-performance IoT
(like a Raspberry Pi or better).

The solution is to use minimal verification clients, which were introduced in
the Incubed protocol by slock.it. Such a client combines the security of a
light client with the advantages of a remote client at least for the most
common IoT solutions, as well as mobile and web applications.

With Incubed, it’s possible to connect devices in a fully decentralized way,
without a central instance, and with (almost) full security.

![](https://miro.medium.com/max/1400/1*MjG-rmfP4He1JCCPCVyCag.png)

An Incubed client is a stateless client that can verify whatever requested
information belongs to a given block and confirm that this block is, in fact,
a valid block of the blockchain. The client can do this all by itself, without
the need to trust any external source.

How does Incubed work? To learn about the details, check out what we wrote in
an earlier [blog post](/slock-it-iot-layer-f305601df963) or
[presentation](https://www.youtube.com/watch?v=EDJWb3fWB1w). You can also
access the Incubed [documentation](https://in3.readthedocs.io/en) or our
[GitHub repository](https://github.com/slockit/in3) for more information.

# Typescript Vs. C

The TypeScript Incubed client provides a library to integrate the client
directly into a mobile app or a web application. It’s possible to use the
Incubed client directly or simply as an HTTP-provider for Web3.js.

This makes it possible to convert existing applications into truly
decentralized applications based on the Incubed protocol easily, quickly, and
without remarkable effort.

Nevertheless, this won’t work as a solution for IoT devices with very limited
resources. To address this, we are also publishing our C implementation with
this release, which makes it possible to integrate the Incubed client into any
program, including the firmware of microcontrollers. Depending on the edition
— each differs in the functional scope and thus the resource requirements —
the client can verify transactions, access the state, and account information,
or interact with smart contracts.

> The Incubed EVM is the most resource-efficient implementation currently
> available. This makes the Incubed client fully capable of running on a
> microcontroller.

This native implementation of the Incubed client requires minimal resources.
The nano edition (which only verifies transactions) requires the lowest amount
of resources, only about 150KB. But even the full version (including EVM),
which can enable all interactions with the blockchain, needs only about 450KB,
depending on the firmware.

# Operating an Incubed Node

The Incubed protocol is based on an open network. Anyone can operate an
Incubed node to support the decentralized network and help develop a stable
ecosystem.

Practically any full node (e.g., Geth, Parity, Nethermind, and all other
implementations that adopted EIP-1186) can become an active Incubed node by
adding the Incubed interface software and registering in the Incubed registry.

> Anyone can register and run an Incubed node.

The [documentation ](https://in3.readthedocs.io/en/latest/)explains how to do
this.

Of course, there is also a Docker image available, which is already configured
and ready to run.

# Stable Release

With the current release, the Incubed protocol goes live on the Ethereum main
net and various Ethereum test networks. IPFS is supported, too. As the Incubed
protocol is platform-agnostic, other blockchains like Bitcoin are in
development or an experimental phase.

The TypeScript-Incubed client, the Incubed node, and the Incubed registry are
published with the release version. The C-client, as well as the binding to
Java, and the WASM-client are available as a beta version. A command-line
application to interact directly from the console with the blockchain, without
the need to install and synchronize a local client, is part of the package,
too.

All software is offered under a dual license — AGPL for open-source software
applications and a commercial license for all other applications.

An important feature of the Incubed protocol, the incentive layer, will first
be available in the upcoming Stable II (productive) release. This will make it
possible to compensate Incubed nodes for the delivery of verifiable (and thus
secure) data.

The software components dealing with security and holding or managing values
were audited by Consensys Diligence. The report is published (see
<https://diligence.consensys.net/audits/2019/09/slock.it-incubed3/>).

# Roadmap

The next big milestone, which we are working on now, will be the release of
the above-mentioned incentive layer. We will also publish the C version of the
Incubed client as a productive release version. With this version, bindings to
other programming languages like Python, Go, and others will be available. The
TypeScript version will be replaced by a much more resource-efficient WASM
version without any dependencies to other libraries.

![](https://miro.medium.com/max/1400/1*M-awduN9KyU9ehrtxgRslQ.png)

Longer-term development milestones include the integration of further
blockchain technologies, level 2 technologies, and other verifiable data
services into the protocol.

# Get in Touch

The source code is available within our [GitHub
repository](https://github.com/slockit/in3), and you can also check out the
release [packages](https://in3.readthedocs.io/en/latest//download.html). Also,
we invite you to chat with us at our newly opened [Gitter
channel](https://gitter.im/slockit-in3/community) about your ideas,
requirements, and experiences with Incubed.

> GitHub: <https://github.com/slockit/in3>  
> Download Resources:
> https://in3.readthedocs[.](https://in3.readthedocs.io/en/latest/download.html)io/en/latest/download.html  
> Documentation: <https://in3.readthedocs.io/en/latest/index.html>  
> Gitter: <https://gitter.im/slockit-in3/community>

# Meetup and Launch Party

We invite you on January 15, 2020, to join us in Berlin at the Fullnode-
Coworking space for the first official Incubed meetup and Release Party for
the STABLE RELEASE! At the meetup, Christoph Jentzsch, Simon Jentzsch, Steffen
Kux and others will talk about the Incubed protocol, available resources, use
cases, and plans. Don’t miss to register! We hope to see you!

[

## Incubed Productive I Release

### The Incubed Protocol Makes Its Way to Mainnet We’re going live! Join us in
Berlin as we commemorate the official stable…

www.eventbrite.com

](https://www.eventbrite.com/e/incubed-productive-i-release-
tickets-86725031905)

For more detailed information explained on a practical example, also read the
following article:

[

## Incubed — Secure Blockchain Access for IoT

### What does the “S” in IoT stand for? Well, for „Secure“ and yes, there is
no „S“. Because making an IoT device secure…

blog.slock.it

](/incubed-secure-blockchain-access-for-iot-db4687b3dfa1)

Thanks toRebekah Devine

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fslock-
it-
blog%2Fc35b3a4ec10a&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fincubed-
stable-
release-c35b3a4ec10a&user=Steffen+Kux&userId=2b84d96491a4&source=-----c35b3a4ec10a
---------------------clap_footer-----------)

\--

1

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fslock-
it-
blog%2Fc35b3a4ec10a&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fincubed-
stable-
release-c35b3a4ec10a&user=Steffen+Kux&userId=2b84d96491a4&source=-----c35b3a4ec10a
---------------------clap_footer-----------)

\--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fslock-
it-
blog%2Fc35b3a4ec10a&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fincubed-
stable-
release-c35b3a4ec10a&user=Steffen+Kux&userId=2b84d96491a4&source=-----c35b3a4ec10a
---------------------clap_footer-----------)

\--

1

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fc35b3a4ec10a&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fincubed-
stable-
release-c35b3a4ec10a&source=--------------------------bookmark_footer-----------)

## [More from slock.it Blog](https://blog.slock.it/?source=post_page-----
c35b3a4ec10a--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Fslock-
it-
blog%2Fc35b3a4ec10a&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fincubed-
stable-
release-c35b3a4ec10a&collection=slock.it+Blog&collectionId=15115b6d917a&source=post_page
-----c35b3a4ec10a---------------------follow_footer-----------)

IoT + Blockchain

[Read more from slock.it Blog](https://blog.slock.it/?source=post_page-----
c35b3a4ec10a--------------------------------)

## Recommended from Medium

[[![Usoroanthonia](https://miro.medium.com/fit/c/40/40/1*dmbNkD5D-u45r44go_cf0g.png)](https://medium.com/@usoroanthonia?source=post_internal_links
---------0----------------------------)

[Usoroanthonia

](https://medium.com/@usoroanthonia?source=post_internal_links---------
0----------------------------)

## ABOUT FUNKIES COLLECTIBLES

![](https://miro.medium.com/focal/112/112/50/50/1*oVlh-
VeVcabipV6v6TzFlw.jpeg)](https://medium.com/@usoroanthonia/about-funkies-
collectibles-9dceb23e1b97?source=post_internal_links---------
0----------------------------)

[[![Lambda](https://miro.medium.com/fit/c/40/40/1*NGw3RB36iads09iPQiAVdQ.jpeg)](https://lambdastorage.medium.com/?source=post_internal_links
---------1----------------------------)

[Lambda

](https://lambdastorage.medium.com/?source=post_internal_links---------
1----------------------------)

in

[Lambdaofficial

](https://medium.com/lambdaofficial?source=post_internal_links---------
1----------------------------)

## Blockchain and Artificial Intelligence Convergence Advancing Both Sectors

![](https://miro.medium.com/focal/112/112/50/50/1*OiDW8p-HJgJZZGKuyXSi0A.jpeg)](https://medium.com/lambdaofficial/blockchain-
and-artificial-intelligence-convergence-advancing-both-
sectors-1894dc41eb4?source=post_internal_links---------
1----------------------------)

[[![AnthonyJoseph](https://miro.medium.com/fit/c/40/40/1*9VN6gUX97j4TSFAu09NjLA@2x.jpeg)](https://medium.com/@kvngtony?source=post_internal_links
---------2----------------------------)

[AnthonyJoseph

](https://medium.com/@kvngtony?source=post_internal_links---------
2----------------------------)

## Information on Meow Box

![](https://miro.medium.com/focal/112/112/50/50/1*1nAPVFYaxzsQz_iDLSp6QQ@2x.jpeg)](https://medium.com/@kvngtony/information-
on-meow-box-40e4271780f?source=post_internal_links---------
2----------------------------)

[[![Hoo.com](https://miro.medium.com/fit/c/40/40/1*hZIDYHvjeTabC80eq39lKA.jpeg)](https://medium.com/@Hoo_exchange?source=post_internal_links
---------3----------------------------)

[Hoo.com

](https://medium.com/@Hoo_exchange?source=post_internal_links---------
3----------------------------)

## Hoo Research ｜A Report of Arweave

![](https://miro.medium.com/focal/112/112/50/50/1*9cNaxTHcqEmfoo-S-
TQ0GQ.png)](https://medium.com/@Hoo_exchange/hoo-research-a-report-of-
arweave-9ca3a73db346?source=post_internal_links---------
3----------------------------)

[[![Morpheus Labs
Team](https://miro.medium.com/fit/c/40/40/1*zBHyFjmeXDejVn8TRtthhQ.png)](https://morpheuslabs-
io.medium.com/?source=post_internal_links---------
4----------------------------)

[Morpheus Labs Team

](https://morpheuslabs-io.medium.com/?source=post_internal_links---------
4----------------------------)

in

[Morpheus Labs

](https://medium.com/morpheus-labs?source=post_internal_links---------
4----------------------------)

## Risks of Adopting Blockchain Technology

![](https://miro.medium.com/focal/112/112/50/50/1*9AF4f8cm1qdqoyY22sPNmw.png)](https://medium.com/morpheus-
labs/risks-of-adopting-blockchain-
technology-f17c97d94d73?source=post_internal_links---------
4----------------------------)

[[![Sienna](https://miro.medium.com/fit/c/40/40/1*oZtOu-0L8WF3nd81VgCuuw.png)](https://medium.com/@sienna_network?source=post_internal_links
---------5----------------------------)

[Sienna

](https://medium.com/@sienna_network?source=post_internal_links---------
5----------------------------)

in

[Sienna Network

](https://medium.com/sienna-network?source=post_internal_links---------
5----------------------------)

## Weekly Development Update: 1

![](https://miro.medium.com/focal/112/112/50/50/1*48DSzVL1w6xwS8A7KvpFAw.png)](https://medium.com/sienna-
network/weekly-development-update-1-cf367c6442d5?source=post_internal_links
---------5----------------------------)

[[![Antier
Solutions](https://miro.medium.com/fit/c/40/40/1*_RMcbAM9HLL9cfHVC_cdfA.jpeg)](https://antiersolutions.medium.com/?source=post_internal_links
---------6----------------------------)

[Antier Solutions

](https://antiersolutions.medium.com/?source=post_internal_links---------
6----------------------------)

## 7 Insurance Processes Blockchain can Disrupt

![](https://miro.medium.com/focal/112/112/50/50/0*aOySu1mmDWhkOAkP.jpg)](https://antiersolutions.medium.com/7-insurance-
processes-blockchain-can-disrupt-49d7c8cf49c1?source=post_internal_links
---------6----------------------------)

[[![The
WireMaster](https://miro.medium.com/fit/c/40/40/0*G8xslQzw77kqaU8F.jpg)](https://medium.com/@wire_master?source=post_internal_links
---------7----------------------------)

[The WireMaster

](https://medium.com/@wire_master?source=post_internal_links---------
7----------------------------)

## Buy and sell a property on blockchain

![](https://miro.medium.com/focal/112/112/50/50/0*TWlNGT-v9__DZNcD.jpg)](https://medium.com/@wire_master/buy-
and-sell-a-property-on-blockchain-ffdfc2b74554?source=post_internal_links
---------7----------------------------)

[](https://medium.com/?source=post_page-----
c35b3a4ec10a--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
c35b3a4ec10a--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
c35b3a4ec10a--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
c35b3a4ec10a--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
c35b3a4ec10a--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----c35b3a4ec10a--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----c35b3a4ec10a--------------------------------)

[Get
started](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fincubed-
stable-release-c35b3a4ec10a&source=post_page--------------------------
nav_reg-----------)

[![Steffen
Kux](https://miro.medium.com/fit/c/176/176/0*59Wk_wX_AKsdO7qx.)](https://medium.com/@steffen.kux)

[

## Steffen Kux

](https://medium.com/@steffen.kux)

9 Followers

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F2b84d96491a4&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fincubed-
stable-
release-c35b3a4ec10a&user=Steffen+Kux&userId=2b84d96491a4&source=post_page-2b84d96491a4
-------------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fusers%2F2b84d96491a4%2Flazily-
enable-writer-
subscription&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fincubed-
stable-
release-c35b3a4ec10a&user=Steffen+Kux&userId=2b84d96491a4&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Stacksranger](https://miro.medium.com/fit/c/40/40/0*IejB5-LNCQfOEQTL)](https://medium.com/@stacksranger?source=read_next_recirc
---------0---------------------c7daf41f_3c04_4768_8007_be5725402b55-------)

[Stacksranger

](https://medium.com/@stacksranger?source=read_next_recirc---------0
---------------------c7daf41f_3c04_4768_8007_be5725402b55-------)

in

[KCV DAO

](https://medium.com/kcv-dao?source=read_next_recirc---------0
---------------------c7daf41f_3c04_4768_8007_be5725402b55-------)

## How to use KCV Mining Pool

![](https://miro.medium.com/focal/112/112/50/50/1*aD6eV5TT9vrH8SJ_wWP-
yg.png)](https://medium.com/kcv-dao/how-to-use-kcv-mining-
pool-f1425d0d24c8?source=read_next_recirc---------0---------------------
c7daf41f_3c04_4768_8007_be5725402b55-------)

[[![ChainCade
Team](https://miro.medium.com/fit/c/40/40/1*iN0u8d7fzrww_8bAc9YW3g.png)](https://medium.com/@ChainCade?source=read_next_recirc
---------1---------------------c7daf41f_3c04_4768_8007_be5725402b55-------)

[ChainCade Team

](https://medium.com/@ChainCade?source=read_next_recirc---------1
---------------------c7daf41f_3c04_4768_8007_be5725402b55-------)

## ChainCade Partners with Berry Data !

![](https://miro.medium.com/focal/112/112/50/50/1*6buPetE7Qex9RUsNkYK_Pw.png)](https://medium.com/@ChainCade/chaincade-
partners-with-berry-data-5b2c26b501c0?source=read_next_recirc---------1
---------------------c7daf41f_3c04_4768_8007_be5725402b55-------)

[[![NonceBlox](https://miro.medium.com/fit/c/40/40/1*O1sVdIeXo5id4Wti4hEbmQ.png)](https://medium.com/@Nonceblox_?source=read_next_recirc
---------2---------------------c7daf41f_3c04_4768_8007_be5725402b55-------)

[NonceBlox

](https://medium.com/@Nonceblox_?source=read_next_recirc---------2
---------------------c7daf41f_3c04_4768_8007_be5725402b55-------)

## Infinite Mint Attack

![](https://miro.medium.com/focal/112/112/50/50/1*aGvIit28FMaNvpmQyljUEQ.jpeg)](https://medium.com/@Nonceblox_/infinite-
mint-attack-3c839f41fe80?source=read_next_recirc---------2
---------------------c7daf41f_3c04_4768_8007_be5725402b55-------)

[[![Ragnar
Doge](https://miro.medium.com/fit/c/40/40/1*ifp5EU07oSWKWHz6x_VQYg.jpeg)](https://medium.com/@RagnarDoge?source=read_next_recirc
---------3---------------------c7daf41f_3c04_4768_8007_be5725402b55-------)

[Ragnar Doge

](https://medium.com/@RagnarDoge?source=read_next_recirc---------3
---------------------c7daf41f_3c04_4768_8007_be5725402b55-------)

## A design of PoE ( Proof of Excellence) token #2

![](https://miro.medium.com/focal/112/112/50/50/1*ks_fRjEkSdo_0iDf8fYO_Q.png)](https://medium.com/@RagnarDoge/a-design-
of-poe-proof-of-excellence-token-2-23959f3a9dcf?source=read_next_recirc
---------3---------------------c7daf41f_3c04_4768_8007_be5725402b55-------)

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

