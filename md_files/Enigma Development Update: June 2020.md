[](https://medium.com/)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/cc23f54afe9a&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](https://medium.com/)

[Home](https://medium.com/)

[Notifications](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Enigma](https://miro.medium.com/fit/c/64/64/1*aIQTqQDM97_LBgHTkHGqcA.png)](https://blog.enigma.co/?source=post_page
-----cc23f54afe9a--------------------------------)

Published in

[Enigma

](https://blog.enigma.co/?source=post_page-----
cc23f54afe9a--------------------------------)

[![James
Waugh](https://miro.medium.com/fit/c/96/96/2*Q4zRpsuf4GKFMEuZjWyC_w.jpeg)](https://medium.com/@jwaup?source=post_page
-----cc23f54afe9a--------------------------------)

[James Waugh](https://medium.com/@jwaup?source=post_page-----
cc23f54afe9a--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F4ae4fe949e3c&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fenigma-
development-update-
june-2020-cc23f54afe9a&user=James+Waugh&userId=4ae4fe949e3c&source=post_page-4ae4fe949e3c
----cc23f54afe9a---------------------follow_byline-----------)

Jul 10, 2020

·

4 min read

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fcc23f54afe9a&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fenigma-
development-update-
june-2020-cc23f54afe9a&source=--------------------------bookmark_header-----------)

[

Save

](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fcc23f54afe9a&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fenigma-
development-update-
june-2020-cc23f54afe9a&source=--------------------------bookmark_header-----------)

# Enigma Development Update: June 2020

## Learn more about our successful completion of our last “secret contracts”
milestone, SafeTrace progress, and the upcoming launch of the first secret
contracts testnet!

![](https://miro.medium.com/max/1400/1*mz7k1zQuPEgdRB9MVF7Jgg.png)

Hello to the community! What follows is a recap of important updates from the
past month, including our progress towards enabling [secret
contracts](https://blog.scrt.network/secret-contracts-update-
milestone-3-of-3-is-complete). This post expands upon our regular community
updates on the [forum](https://forum.scrt.network) and includes ways for
developers, validators, and others to get more involved with the project!

In June, the Enigma team achieved a significant milestone on the path to
upgrading [Secret Network](https://scrt.network). That means compiling and
running a full node with
[wasmi](https://paritytech.github.io/wasmi/wasmi/index.html) inside
[SGX](https://software.intel.com/sgx) with encryption abilities. All basic
functionality for executing [CosmWasm](https://www.cosmwasm.com/) contracts in
a secure enclave is now implemented and continues to be tested! You can follow
our progress by reviewing our development and product sprints on these [GitHub
project boards](https://github.com/enigmampc/SecretNetwork/projects).

 **We now expect to have the first public testnet for secret contracts live in
the month of July, coinciding with the start of the**[ **Secret
Games**](https://blog.scrt.network/announcing-the-secret-games) **.** We will
continue to share regular updates on development progress on the [Secret
Forum](https://forum.scrt.network) — and we have more info about this testnet
later in this post. Keep reading for all the details!

# Protocol Development: Enabling Secret Contracts

Since our community launched the Secret Network in February of this year, we
have been focused on building the necessary components for private computation
inside Trusted Execution Environments (TEEs), namely Intel SGX. This work, led
by Guy, Assaf, Tom, Reuven and Itzik, comprises many specific tasks, organized
into these project milestones on GitHub:

  * [Milestone 1](https://github.com/enigmampc/EnigmaBlockchain/milestone/1) — Integrating Smart Contracts into the Secret Network
  * [Milestone 2](https://github.com/enigmampc/EnigmaBlockchain/milestone/2) — Executing CosmWasm Smart Contracts in SGX
  * [Milestone 3](https://github.com/enigmampc/EnigmaBlockchain/milestone/3) — Adding Encryption for Secret Contracts Running in SGX

Lately, our team has been focused on [WIP
documentation](https://build.scrt.network/protocol/encryption-specs.html) for
the cryptography elements of the secret protocol. This means encrypted inputs,
outputs and state. Read more about Milestone 3 in this [blog
post](https://blog.scrt.network/secret-contracts-update-milestone-3-of-3-is-
complete) by Enigma developer Assaf Morami.

# What does this mean for developers?

Developers will soon have the ability to deploy secret contracts on the Secret
Games testnet, maintained by Enigma. Our `compute` module for the Cosmos SDK
gives the ability to run CosmWasm inside trusted execution environments (TEEs)
maintained by node operators (secret nodes). As our dev team continues to test
secret contract functionality, we are focused on improving our developer
onboarding process and looking for help. The goal is to make it as easy as
possible for Rust developers to build and deploy contracts. Please let us know
if you have any feedback on our evolving
[documentation](https://build.scrt.network). This walkthrough is for an
implementation of CosmWasm without any encryption features:

## [Contract Development Guide](https://build.scrt.network/dev/contract-dev-
guide.html)

# What does this mean for node runners?

Building toward this new milestone has been exciting, and it means we’re one
step closer to proposing secret contract functionality to the Secret Network.
From that point forward, validators will need to use SGX-enabled hardware to
participate as “secret nodes” in the network.

## [Announcing the Secret Games](https://blog.scrt.network/announcing-the-
secret-games/)

If you want to launch a node and become a mainnet validator today, here are
the instructions:

  1. [Install SGX](https://build.scrt.network/validators-and-full-nodes/setup-sgx.html)
  2. [Run a full node](https://build.scrt.network/validators-and-full-nodes/run-full-node-mainnet.html)
  3. [Become a validator](https://build.scrt.network/validators-and-full-nodes/join-validator-mainnet.html)

We recently announced our incentivized testnet program, called the Secret
Games, that will allow developers and testnet validators to receive Secret
(SCRT) while helping us test secret contract functionality! If you’re
interested in being notified when we share more details, please fill out [this
form](https://airtable.com/shrBVxhT82kZxZ91L):

## [Secret Games Interest Form](https://airtable.com/shrBVxhT82kZxZ91L)

# CosmWasm

Recently, we have been collaborating with the [CosmWasm
team](https://www.cosmwasm.com), which is building a smart contracting
platform for the [Cosmos ecosystem](https://cosmos.network). The [Cosmos
SDK](https://docs.cosmos.network), [Tendermint](https://tendermint.com) and
the [Inter-Blockchain Communication protocol](https://github.com/cosmos/ics)
are designed to enable scalable, interoperable application-specific
blockchains. Enigma’s dev team is excited to contribute alongside Ethan Frey,
Simon Warta, et al. They have invited [Reuven](https://github.com/reuvenpo) to
be a core contributor of the CosmWasm project, following some updates made in
coordination with releasing version 0.9 of CosmWasm. Stay tuned for a detailed
post on the `x/compute` module.

We’ve also written recently about how the Secret Network fits into the growing
Cosmos ecosystem. Our privacy solutions can help many zones and other hubs
with interoperable trusted computation services for any blockchain. [Secret
Hub](https://blog.scrt.network/secret-hub) facilitates adoption of
application-specific networks, which are greater than the sum of their parts!

# SafeTrace: Privacy-Preserving Contact Tracing API

The Enigma team also continues to develop privacy-first applications that help
solve real-world problems. Since our [April Development Update on
SafeTrace](/safetrace-april-2020-development-update-4c5f77bfddfa), we have
been focused on connecting with app developers and other strategic partners.
We are excited to further develop SafeTrace and the Enigma Confidential
Computing Platform (ECCP), including our work with [IBM
Cloud](https://www.ibm.com/cloud/blog/enigma-and-ibm-cloud-are-protecting-
human-lives-as-well-as-data-privacy). For more info, you can review the
documentation in our [open source code
base](https://github.com/enigmampc/safeTrace).

[

## Enigma and IBM Cloud Are Protecting Human Lives as Well as Data Privacy

### Today, data privacy has become a primary focus for enterprises,
institutions, and individuals.

www.ibm.com

](https://www.ibm.com/cloud/blog/enigma-and-ibm-cloud-are-protecting-human-
lives-as-well-as-data-privacy)

# Going Forward

Overall, we’re thrilled to keep building toward the vision of privacy-
preserving Secret Apps. We’re continuing research into various use cases,
including secret voting, access control, and more! Please don’t hesitate to
reach out to our team or the Secret Foundation with any ideas or questions.
You can find us on [RocketChat](https://chat.scrt.network),
[Discord](https://discord.com/invite/SJK32GY), and the [Secret
Forum](http://forum.scrt.network). If you’d like to get more involved in our
developer community, please fill out this form:

Stay tuned for our weekly community updates and governance meetings. Our next
open discussion is planned for Wednesday July 15 at 11:00am EDT / 3:00pm UTC.
Here is the link to join and participate:

## [meet.scrt.network/discussion](https://meet.scrt.network/discussion)

Thank you for supporting our mission to bring essential privacy solutions to
the decentralized web — and to advance privacy as a public good! We are deeply
grateful for your help.

Onwards and upwards,

The Enigma Team

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fenigmampc%2Fcc23f54afe9a&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fenigma-
development-update-
june-2020-cc23f54afe9a&user=James+Waugh&userId=4ae4fe949e3c&source=-----cc23f54afe9a
---------------------clap_footer-----------)

\--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fenigmampc%2Fcc23f54afe9a&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fenigma-
development-update-
june-2020-cc23f54afe9a&user=James+Waugh&userId=4ae4fe949e3c&source=-----cc23f54afe9a
---------------------clap_footer-----------)

\--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fenigmampc%2Fcc23f54afe9a&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fenigma-
development-update-
june-2020-cc23f54afe9a&user=James+Waugh&userId=4ae4fe949e3c&source=-----cc23f54afe9a
---------------------clap_footer-----------)

\--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fcc23f54afe9a&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fenigma-
development-update-
june-2020-cc23f54afe9a&source=--------------------------bookmark_footer-----------)

## [More from Enigma](https://blog.enigma.co/?source=post_page-----
cc23f54afe9a--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Fenigmampc%2Fcc23f54afe9a&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fenigma-
development-update-
june-2020-cc23f54afe9a&collection=Enigma&collectionId=6cb5d792f282&source=post_page
-----cc23f54afe9a---------------------follow_footer-----------)

Official Blog of Enigma - Securing the Decentralized Web.

[Read more from Enigma](https://blog.enigma.co/?source=post_page-----
cc23f54afe9a--------------------------------)

## Recommended from Medium

[[![Dre Tech Tips](https://miro.medium.com/fit/c/40/40/1*nmxknuy5XH-
bp5WsAYGaqg.png)](https://medium.com/@dretechtips?source=post_internal_links
---------0----------------------------)

[Dre Tech Tips

](https://medium.com/@dretechtips?source=post_internal_links---------
0----------------------------)

in

[ILLUMINATION

](https://medium.com/illumination?source=post_internal_links---------
0----------------------------)

## The Ultimate Guide on Securing your Linux Servers

![](https://miro.medium.com/focal/112/112/50/50/0*F8nCKMWa7JR8cPFi)](https://medium.com/illumination/the-
ultimate-guide-on-securing-your-linux-servers-
efa68065868b?source=post_internal_links---------0----------------------------)

[[![flyw33d](https://miro.medium.com/fit/c/40/40/1*Gqgmo94sKqMT3nl5a8UeJg.jpeg)](https://professorcouts.medium.com/?source=post_internal_links
---------1----------------------------)

[flyw33d

](https://professorcouts.medium.com/?source=post_internal_links---------
1----------------------------)

## Make Your Online Protection Reality

![](https://miro.medium.com/focal/112/112/50/50/1*j0ygxtpcMo74J5j5ESAAGg.jpeg)](https://professorcouts.medium.com/make-
your-online-protection-reality-33b30fe778b7?source=post_internal_links
---------1----------------------------)

[[![Max](https://miro.medium.com/fit/c/40/40/1*dmbNkD5D-u45r44go_cf0g.png)](https://medium.com/@maxmichels?source=post_internal_links
---------2----------------------------)

[Max

](https://medium.com/@maxmichels?source=post_internal_links---------
2----------------------------)

## Stop WordPress XMLRPC attacks

![](https://miro.medium.com/focal/112/112/50/50/0*sUX0cXytSYUl11s5)](https://medium.com/@maxmichels/stop-
wordpress-xmlrpc-attacks-efd632851e5e?source=post_internal_links---------
2----------------------------)

[[![ALTER](https://miro.medium.com/fit/c/40/40/1*k6f6WtLIEuPHz4JvCy_mNw.png)](https://blog.altermail.live/?source=post_internal_links
---------3----------------------------)

[ALTER

](https://blog.altermail.live/?source=post_internal_links---------
3----------------------------)

## ALTER announces collaboration with Huddle01: One-click meetings for calls
and video conferencing!

![](https://miro.medium.com/focal/112/112/50/50/1*G3TRf1FliL3lVwND9fYRvw.jpeg)](https://blog.altermail.live/alter-
announces-collaboration-with-huddle01-one-click-meetings-for-calls-and-video-
conferencing-e2851ab49405?source=post_internal_links---------
3----------------------------)

[[![Grazia
Meyeroff](https://miro.medium.com/fit/c/40/40/1*dmbNkD5D-u45r44go_cf0g.png)](https://quinche2018.medium.com/?source=post_internal_links
---------4----------------------------)

[Grazia Meyeroff

](https://quinche2018.medium.com/?source=post_internal_links---------
4----------------------------)

## {UPDATE} 爆金大亨-神秘寶藏 Hack Free Resources Generator

](https://quinche2018.medium.com/update-爆金大亨-神秘寶藏-hack-free-resources-
generator-f2f2ec33a06a?source=post_internal_links---------
4----------------------------)

[[![Lucy
Hales](https://miro.medium.com/fit/c/40/40/1*6AkXJR9LlGKUYvbkYCBtlg.jpeg)](https://lucyhales.medium.com/?source=post_internal_links
---------5----------------------------)

[Lucy Hales

](https://lucyhales.medium.com/?source=post_internal_links---------
5----------------------------)

## The Biggest DDoS Attack in the History

![](https://miro.medium.com/focal/112/112/50/50/1*Dl0F36mQqB_LNtA_dKd3ug.jpeg)](https://lucyhales.medium.com/the-
biggest-ddos-attack-in-the-history-6ecdc7d3377b?source=post_internal_links
---------5----------------------------)

[[![Toradex](https://miro.medium.com/fit/c/40/40/2*pi5gDvKlFpV1yWZq6K3mrw.jpeg)](https://medium.com/@toradex?source=post_internal_links
---------6----------------------------)

[Toradex

](https://medium.com/@toradex?source=post_internal_links---------
6----------------------------)

## Guest Webinar: Secure your Embedded Device with Prove & Run and Toradex

![](https://miro.medium.com/focal/112/112/50/50/1*hXbrnicaPhdg_Icq1UyrrQ.jpeg)](https://medium.com/@toradex/guest-
webinar-secure-your-embedded-device-with-prove-run-and-
toradex-43dcdda906eb?source=post_internal_links---------
6----------------------------)

[[![CryptoCell](https://miro.medium.com/fit/c/40/40/1*Ph6rnCv0XwxLn6WYRSEIRA.png)](https://medium.com/@Cryptocell?source=post_internal_links
---------7----------------------------)

[CryptoCell

](https://medium.com/@Cryptocell?source=post_internal_links---------
7----------------------------)

in

[Cryptocurrency Secrets for Beginners

](https://medium.com/cryptocurrency-secrets-for-
beginners?source=post_internal_links---------7----------------------------)

## Advantages and Disadvantages of Cryptocurrency

![](https://miro.medium.com/focal/112/112/50/50/1*NGAm6wzPBbcakliNwnC4mw.png)](https://medium.com/cryptocurrency-
secrets-for-beginners/advantages-and-disadvantages-of-
cryptocurrency-99c247f4d22b?source=post_internal_links---------
7----------------------------)

[](https://medium.com/?source=post_page-----
cc23f54afe9a--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
cc23f54afe9a--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
cc23f54afe9a--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
cc23f54afe9a--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
cc23f54afe9a--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----cc23f54afe9a--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----cc23f54afe9a--------------------------------)

[Get
started](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fenigma-
development-update-june-2020-cc23f54afe9a&source=post_page
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
june-2020-cc23f54afe9a&user=James+Waugh&userId=4ae4fe949e3c&source=post_page-4ae4fe949e3c
-------------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fusers%2F4ae4fe949e3c%2Flazily-
enable-writer-
subscription&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fenigma-
development-update-
june-2020-cc23f54afe9a&user=James+Waugh&userId=4ae4fe949e3c&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Ian
Quinn](https://miro.medium.com/fit/c/40/40/1*Y6Dz1Cf_TCta6jgsYIIYpw.jpeg)](https://medium.com/@ian_h_quinn?source=read_next_recirc
---------0---------------------66fa036f_3fd7_4122_8ed4_223a65b85ea7-------)

[Ian Quinn

](https://medium.com/@ian_h_quinn?source=read_next_recirc---------0
---------------------66fa036f_3fd7_4122_8ed4_223a65b85ea7-------)

## Monero’s Solutions for On-Chain Privacy

![](https://miro.medium.com/focal/112/112/50/50/1*9jcabM4UOMAZEEo27JH84Q.jpeg)](https://medium.com/@ian_h_quinn/moneros-
solutions-for-on-chain-privacy-33b421836968?source=read_next_recirc---------0
---------------------66fa036f_3fd7_4122_8ed4_223a65b85ea7-------)

[[![Justin
d’Anethan](https://miro.medium.com/fit/c/40/40/1*v5gYDG4zfErphCl7HhILQA.jpeg)](https://justindanethan.medium.com/?source=read_next_recirc
---------1---------------------66fa036f_3fd7_4122_8ed4_223a65b85ea7-------)

[Justin d’Anethan

](https://justindanethan.medium.com/?source=read_next_recirc---------1
---------------------66fa036f_3fd7_4122_8ed4_223a65b85ea7-------)

## On Bitcoin As The Antithesis Of Ponzi Schemes

![](https://miro.medium.com/focal/112/112/50/50/1*evsyJp48g81vrcXyEsORWw.jpeg)](https://justindanethan.medium.com/on-
bitcoin-as-the-antithesis-of-ponzi-
schemes-59fdbfd520ea?source=read_next_recirc---------1---------------------
66fa036f_3fd7_4122_8ed4_223a65b85ea7-------)

[[![0xMac.eth](https://miro.medium.com/fit/c/40/40/1*5iragY3cOfYs6PuxFbNclw.png)](https://medium.com/@0xMac.eth?source=read_next_recirc
---------2---------------------66fa036f_3fd7_4122_8ed4_223a65b85ea7-------)

[0xMac.eth

](https://medium.com/@0xMac.eth?source=read_next_recirc---------2
---------------------66fa036f_3fd7_4122_8ed4_223a65b85ea7-------)

## How to use Ledger through MeteMask

![](https://miro.medium.com/focal/112/112/50/50/0*2BqN5Ng7id3lPcRu.png)](https://medium.com/@0xMac.eth/how-
to-use-ledger-through-metemask-e65d98995ea0?source=read_next_recirc---------2
---------------------66fa036f_3fd7_4122_8ed4_223a65b85ea7-------)

[[![Pramodaa](https://miro.medium.com/fit/c/40/40/0*NERhF0-LpF9KiQAd)](https://medium.com/@pramodaa27?source=read_next_recirc
---------3---------------------66fa036f_3fd7_4122_8ed4_223a65b85ea7-------)

[Pramodaa

](https://medium.com/@pramodaa27?source=read_next_recirc---------3
---------------------66fa036f_3fd7_4122_8ed4_223a65b85ea7-------)

in

[Coinmonks

](https://medium.com/coinmonks?source=read_next_recirc---------3
---------------------66fa036f_3fd7_4122_8ed4_223a65b85ea7-------)

## Dive intoWeb3

![](https://miro.medium.com/focal/112/112/50/50/1*_o9NxaIN3wyN-30UuHKmRQ.png)](https://medium.com/coinmonks/dive-
intoweb3-a708eb31e573?source=read_next_recirc---------3---------------------
66fa036f_3fd7_4122_8ed4_223a65b85ea7-------)

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

