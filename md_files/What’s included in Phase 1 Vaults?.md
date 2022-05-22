[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/b49715fb2ae8&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![safenetwork](https://miro.medium.com/fit/c/64/64/1*oEy3kCG2HULiXdpEQdr6Nw.jpeg)](https://medium.com/safenetwork?source=post_page
-----b49715fb2ae8--------------------------------)

Published in

[safenetwork

](https://medium.com/safenetwork?source=post_page-----
b49715fb2ae8--------------------------------)

[![MaidSafe](https://miro.medium.com/fit/c/96/96/1*_aSR7-KPlJ-
loTqzHF1E1g.jpeg)](/@maidsafe?source=post_page-----
b49715fb2ae8--------------------------------)

[MaidSafe](/@maidsafe?source=post_page-----
b49715fb2ae8--------------------------------)

Follow

Sep 11, 2019

·

4 min read

#  ** _What’s included in Phase 1 Vaults?_**

![](https://miro.medium.com/max/1250/1*U-lZK0mLeW71cTxLQWZLEQ.jpeg)

So you’ve come looking for some more information on what we’ve included in
this [Phase 1 Vaults](/safenetwork/new-release-phase-1-vaults-9c0d24661c1)
release? Well, you’ve come to the right place! We’ve tried to keep this fairly
non-technical. However, if anything is unclear or you need any support, head
over to the [Forum](https://safenetforum.org/t/new-release-vault-phase-1-real-
vault/29712) where the team and community will be ready and waiting to answer
your questions.

#  **Data Types**

We’ve implemented the 8 data types as defined in the Data Types
RFC’s([0054](https://github.com/maidsafe/rfcs/blob/master/text/0054-published-
and-unpublished-data/0054-published-and-unpublished-data.md) and
[0055](https://github.com/maidsafe/rfcs/blob/master/text/0055-unpublished-
immutable-data/0055-unpublished-immutable-data.md)) which can, very simply, be
categorised into Public (or Published) and Private (or Unpublished). We’ve got
a [standalone post ](/safenetwork/an-overview-of-data-types-on-the-safe-
network-c2c78fce5638)which explains these types in more detail but in essence,
they give every user ultimate control over how to maintain his or her data.

Public data is the content you publish to the Network that _everyone_ can see
it. This is the [Perpetual Web](/safenetwork/a-spotlight-on-the-perpetual-
web-9850349fab0b) in action. Private data, on the other hand, is slightly more
nuanced and brings to life the concepts around [Take Control of Your
Data](/safenetwork/a-spotlight-on-take-control-of-your-data-34d0a8e8ac64) that
you might have heard us discuss before.

#  **Test Safecoin**

We’ve implemented the basic functions defined in the [Safecoin
RFC](https://github.com/maidsafe/rfcs/blob/master/text/0057-safecoin-
revised/0057-safecoin-revised.md) (including creating balances, coin
transfers, and transactions).

#  **SAFE CLI**

The CLI (Command Line Interface) provides many of the commands necessary to
interact with the[ SAFE Network](https://safenetwork.tech/), including storing
and browsing, finding data and using Wallet-related commands. It is worth
noting that while we’re implementing all the data types, the CLI will only use
a selected range (see later in this post).

At this point, we’re showcasing _functionality_. We haven’t implemented a GUI
because we want to let you get closer to the action and interact with a
greater degree of control without having to navigate around a GUI. This makes
it perfect for developers, as you will have the permission to access many of
the operations that can be made on SAFE Network data. It will allow you to
also use it for automated scripts in a piped chain of commands, for example.

By developing the Network in this way, we’re able to decouple the GUI
development from the back-end functionality of those GUI apps. With the CLI
and its API being separate, we can test the operations needed to manipulate
data on the Network more efficiently, by having automated tests and by using
the CLI itself. Once this layer is solid and stable, developing a GUI is a
more straightforward task (as the expected underlying functionality has been
validated).

 **So what can the CLI do?**

First off, the CLI needs to be authorised by you before it can access your
account. Therefore, you’ll need to first authenticate yourself via the SAFE
Authenticator CLI (all the details can be found
[here](https://safenetforum.org/t/release-safe-authenticator-
mobile-v0-1-1/27801)).

Currently, you can use the following data types:

  * [Create files](https://github.com/maidsafe/safe-cli/blob/master/README.md#files) (via the PublishedImmutable data type)
  * [Set up NRS](https://github.com/maidsafe/safe-cli/blob/master/README.md#nrs-name-resolution-system) (PublishedAppendOnly)
  * [Access a Wallet](https://github.com/maidsafe/safe-cli/blob/master/README.md#wallet) and its commands (UnpublishedAppendOnly)

 **Creating files**

As we’ve mentioned, you can upload files to these Vaults. We’ve got a [super-
clear guide](https://github.com/maidsafe/safe-cli#files) here on how to do
this, as well as details of what you can do with your data once it has been
uploaded. But here’s a quick overview here of how it works…

Data is uploaded to the Vaults and stored as Published ImmutableData files
[_(head to this post for all the details on the different data
type)_](/safenetwork/an-overview-of-data-types-on-the-safe-
network-c2c78fce5638). That data is stored in a container which maps the data
path together with the corresponding ImmutableData NRS (more details below).
And this map is stored on the Vault within a special container called
FilesContainer, which is stored as Published AppendOnlyData data. Simples!

 **NRS**

NRS means Name Resolution System. The easiest way to think about it is how
SAFE lets you have human-readable URLs.

Each piece of data on the Vault is held in a unique location with an
associated XOR address name. This data can be accessed using the XOR address
as a URL. Hence XOR-URL. We have been working on developing a more human-
friendly URL system that can be easily remembered when trying to share them
with other people or recognised quickly. Just like URLs on the current
Internet today.

As an example, compare a XOR — URL (
_safe://sadoiofsefohf89243hf9huheofhdoih289euhfafoishaoifdha893f2fh9eahfoiasef_
) with an NRS URL ( _safe://maidsafe_ ). This human-friendly naming system can
be used not just to find data on the Vault but also can be used as a URL to
enable the sourcing of websites, web applications, files and folders. It can
even be used in Safecoin wallets for receiving transfers, SAFE IDs, etc in a
memorable format.

Details on how to create your own NRS and how to work with others can all be
found [here](https://github.com/maidsafe/safe-cli#nrs-name-resolution-system).

 **Wallets**

As part of this release, we’ve included the
[Wallet](https://github.com/maidsafe/safe-cli/blob/master/README.md#wallet) in
this CLI, which is a type of Container. A Container in this context means a
structure to hold data (kind of like a folder). The Wallet holds your secret
keys, which enable you to spend your Safecoin. The Wallet also holds the links
to your SafeKeys, which holds your Safecoins. And importantly, everything that
is stored in the Wallet is only accessible by you, the owner.

Details on how to set up your very own Wallet, as well as adding test
Safecoins, view your balance and make transfers can be found over
[here](https://github.com/maidsafe/safe-cli#wallet), as well as setting up
your Keys.

And that’s it! Next up, Phase 2. This will see the introduction of
[PARSEC](/safenetwork/parsec-a-paradigm-shift-for-asynchronous-and-
permissionless-consensus-e312d721f9d8), swiftly followed up by Phase 3 and 4
which will be iterative versions of the testnet, ultimately ending up in the
implementation of Routing and, then…we have a Network! Make sure you keep up
to date on progress by checking in each Thursday for the [Dev
Update](https://safenetforum.org/c/development/updates) or check out
[Twitter](https://twitter.com/maidsafe) for the latest news and releases.

\--

\--

\--

## [More from safenetwork](/safenetwork?source=post_page-----
b49715fb2ae8--------------------------------)

Stories from around the SAFE Network

[Read more from safenetwork](/safenetwork?source=post_page-----
b49715fb2ae8--------------------------------)

## Recommended from Medium

[[![Santosh
Kumar](https://miro.medium.com/fit/c/40/40/1*_g9S-LpLxV9Rz7RFYwKlnA.png)](/@santoshjram?source=post_internal_links
---------0----------------------------)

[Santosh Kumar

](/@santoshjram?source=post_internal_links---------
0----------------------------)

## Deep dive into SolarWinds Sunburst backdoor

![](https://miro.medium.com/focal/112/112/50/50/1*q8hAlnCgCMySBbJJWgieZA.jpeg)](/@santoshjram/deep-
dive-into-solarwinds-sunburst-backdoor-e24c0e9042c6?source=post_internal_links
---------0----------------------------)

[[![Chamindra de
Silva](https://miro.medium.com/fit/c/40/40/0*wlwrWCZk1IS6eFv4.jpg)](/@ChamindraS?source=post_internal_links
---------1----------------------------)

[Chamindra de Silva

](/@ChamindraS?source=post_internal_links---------
1----------------------------)

## Software of the People, built by the People for the People

![](https://miro.medium.com/focal/112/112/50/50/1*WWi0ZXZv8-qRvCMbBhhBkA.png)](/@ChamindraS/software-
of-the-people-built-by-the-people-for-the-
people-81baf384be7?source=post_internal_links---------
1----------------------------)

[[![Xpool](https://miro.medium.com/fit/c/40/40/1*dHn0kX9BNqSSCzTYHGWJ1w.png)](/@xpool?source=post_internal_links
---------2----------------------------)

[Xpool

](/@xpool?source=post_internal_links---------2----------------------------)

## How To Stake And Get Profit on Xpool?

![](https://miro.medium.com/focal/112/112/50/50/1*6JphbKcFE4rTh0gHB4NZdg.png)](/@xpool/how-
to-stake-and-get-profit-on-xpool-87bb8c842690?source=post_internal_links
---------2----------------------------)

[[![Jehanna
Tod](https://miro.medium.com/fit/c/40/40/1*dmbNkD5D-u45r44go_cf0g.png)](/@americanism2012?source=post_internal_links
---------3----------------------------)

[Jehanna Tod

](/@americanism2012?source=post_internal_links---------
3----------------------------)

## {UPDATE} White Trip Hack Free Resources Generator

](/@americanism2012/update-white-trip-hack-free-resources-
generator-e8c7f05155d9?source=post_internal_links---------
3----------------------------)

[[![Asaad Taha,
PhD](https://miro.medium.com/fit/c/40/40/0*Tz8rmefZuXmsBANm.jpeg)](/@asaad-
taha?source=post_internal_links---------4----------------------------)

[Asaad Taha, PhD

](/@asaad-taha?source=post_internal_links---------
4----------------------------)

## Data integrity vendor Precisely to acquire data management player Infogix

](/@asaad-taha/data-integrity-vendor-precisely-to-acquire-data-management-
player-infogix-dfb9ee6944ca?source=post_internal_links---------
4----------------------------)

[[![Het
Mehta](https://miro.medium.com/fit/c/40/40/1*bQZNLpoSmF2B6icmvrLnxw.jpeg)](/@hetmehtaa?source=post_internal_links
---------5----------------------------)

[Het Mehta

](/@hetmehtaa?source=post_internal_links---------
5----------------------------)

## The Secure Edge: Daily Round-up of Infosec Blogs — Issue #73

![](https://miro.medium.com/focal/112/112/50/50/0*OEjLfi7yR-
eOpRbb)](/@hetmehtaa/the-secure-edge-daily-round-up-of-infosec-blogs-
issue-73-e314ce3402b8?source=post_internal_links---------
5----------------------------)

[[![Het
Mehta](https://miro.medium.com/fit/c/40/40/1*bQZNLpoSmF2B6icmvrLnxw.jpeg)](/@hetmehtaa?source=post_internal_links
---------6----------------------------)

[Het Mehta

](/@hetmehtaa?source=post_internal_links---------
6----------------------------)

## The Secure Edge: Daily Round-up of Infosec Blogs — Issue #14

![](https://miro.medium.com/focal/112/112/50/50/0*YUuCcmk9-ljg29x6)](/@hetmehtaa/the-
secure-edge-daily-round-up-of-infosec-blogs-
issue-14-604f6a219d1e?source=post_internal_links---------
6----------------------------)

[[![Madison
Asper](https://miro.medium.com/fit/c/40/40/1*h7Ya9h2xQPFdphYYXWyXpQ.jpeg)](/@madisonasper2703?source=post_internal_links
---------7----------------------------)

[Madison Asper

](/@madisonasper2703?source=post_internal_links---------
7----------------------------)

in

[AQX Official

](https://medium.com/aqx-official?source=post_internal_links---------
7----------------------------)

## What is 2FA?

![](https://miro.medium.com/focal/112/112/50/50/1*lNlaDLdiuD2DjDpmXU7DPQ.jpeg)](/aqx-
official/what-is-2fa-21dc7016e784?source=post_internal_links---------
7----------------------------)

[](/?source=post_page-----b49715fb2ae8--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
b49715fb2ae8--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
b49715fb2ae8--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
b49715fb2ae8--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
b49715fb2ae8--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----b49715fb2ae8--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----b49715fb2ae8--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fsafenetwork%2Fwhats-
included-in-phase-1-vaults-b49715fb2ae8&source=post_page
--------------------------nav_reg-----------)

[![MaidSafe](https://miro.medium.com/fit/c/176/176/1*_aSR7-KPlJ-
loTqzHF1E1g.jpeg)](/@maidsafe)

[

## MaidSafe

](/@maidsafe)

1.1K Followers

Building the SAFE Network. The world’s first autonomous data network. Privacy,
security, freedom. Join us at <https://safenetforum.org/>

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F2fe910544d0b&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fsafenetwork%2Fwhats-
included-in-
phase-1-vaults-b49715fb2ae8&newsletterV3=6876251327a7&newsletterV3Id=2fe910544d0b&user=MaidSafe&userId=6876251327a7&source=--------------------------subscribe_user-----------)

## More from Medium

[[![hyper](https://miro.medium.com/fit/c/40/40/1*jCGgBRkdlF_BUfyMbV5R_g.png)](/@hyper-
io?source=read_next_recirc---------0---------------------
6e8379bc_e392_444f_a173_ecf466ec2eaf-------)

[hyper

](/@hyper-io?source=read_next_recirc---------0---------------------
6e8379bc_e392_444f_a173_ecf466ec2eaf-------)

## Introducing Hyper {Nano}: Hyper Cloud in a Bottle ⚡️🍷

](/@hyper-io/introducing-hyper-nano-hyper-cloud-in-a-
bottle-️-3baa1f2306c2?source=read_next_recirc---------0---------------------
6e8379bc_e392_444f_a173_ecf466ec2eaf-------)

[[![Samuel
Nwoye](https://miro.medium.com/fit/c/40/40/1*ZkzlRVtKoeW2RAhHWVdVNQ.jpeg)](/@nwoyesamuelc?source=read_next_recirc
---------1---------------------6e8379bc_e392_444f_a173_ecf466ec2eaf-------)

[Samuel Nwoye

](/@nwoyesamuelc?source=read_next_recirc---------1---------------------
6e8379bc_e392_444f_a173_ecf466ec2eaf-------)

## Leveraging Kubernetes Network Policy for Securing your Applications

![cluster_orchestration](https://miro.medium.com/focal/112/112/50/50/1*UQpkcjCrYd-
ptrNv3OwIhQ.png)](/@nwoyesamuelc/leveraging-kubernetes-network-policy-for-
securing-your-applications-fead25a34ced?source=read_next_recirc---------1
---------------------6e8379bc_e392_444f_a173_ecf466ec2eaf-------)

[[![Think Future
Technologies](https://miro.medium.com/fit/c/40/40/1*r1h88_54yId0cqMjhQFnyg.jpeg)](/@tft.us?source=read_next_recirc
---------2---------------------6e8379bc_e392_444f_a173_ecf466ec2eaf-------)

[Think Future Technologies

](/@tft.us?source=read_next_recirc---------2---------------------
6e8379bc_e392_444f_a173_ecf466ec2eaf-------)

## Hire Golang Developer with Think Future Technologies

![](https://miro.medium.com/focal/112/112/50/50/1*QvD7ovHAIzXkkFuPy-
Ohvg.png)](/@tft.us/hire-golang-developer-with-think-future-
technologies-6cba1aac4336?source=read_next_recirc---------2
---------------------6e8379bc_e392_444f_a173_ecf466ec2eaf-------)

[[![Cay
McDonald](https://miro.medium.com/fit/c/40/40/0*uWYKKnrZsGC_bhXQ)](/@csmcdonald?source=read_next_recirc
---------3---------------------6e8379bc_e392_444f_a173_ecf466ec2eaf-------)

[Cay McDonald

](/@csmcdonald?source=read_next_recirc---------3---------------------
6e8379bc_e392_444f_a173_ecf466ec2eaf-------)

## Swarm Learning Applications in Production and Operations Management

](/@csmcdonald/swarm-learning-applications-in-production-and-operations-
management-6a2c1f071a01?source=read_next_recirc---------3---------------------
6e8379bc_e392_444f_a173_ecf466ec2eaf-------)

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

