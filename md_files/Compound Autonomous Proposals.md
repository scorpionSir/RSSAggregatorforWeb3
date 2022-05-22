[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/354e7a2ad6b7&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Compound](https://miro.medium.com/fit/c/64/64/1*MzcWuVj0jfuGCiUYeCAVWA.png)](https://medium.com/compound-
finance?source=post_page-----354e7a2ad6b7--------------------------------)

Published in

[Compound

](https://medium.com/compound-finance?source=post_page-----
354e7a2ad6b7--------------------------------)

[![Calvin
Liu](https://miro.medium.com/fit/c/96/96/2*KHATfyzZqZjQdzTKq1dIkA.jpeg)](/@cjliu49?source=post_page
-----354e7a2ad6b7--------------------------------)

[Calvin Liu](/@cjliu49?source=post_page-----
354e7a2ad6b7--------------------------------)

Follow

Sep 10, 2020

·

3 min read

# Compound Autonomous Proposals

![](https://miro.medium.com/max/1400/0*oJmYbQkIxn7NACPO)

The Compound protocol is maintained and upgraded through a community
governance system in which COMP token-holders and their delegates debate,
propose, and vote on all changes to the protocol. Currently, the governance
system requires users to have a minimum of 100,000 COMP delegated to their
address, before they can formally submit a governance proposal.

While this requirement has not been prohibitive to the creation of thoughtful
governance proposals over the past several months (total 22 submitted, 18
passed), there has recently been vibrant discussion on the possibility of
[lowering the 100,000 COMP-delegated
requirement](https://www.comp.xyz/t/lower-proposal-threshold-to-100-comp/282).

Whether or not a formal proposal is created to lower the requirement is up to
the community. However, today we are proud to announce a tool that
dramatically reduces the barrier to creating proposals, while still satisfying
the encoded requirements of the existing governance system: **Autonomous
Proposals.**

#  **Empowering the Community**

 **Compound Autonomous Proposals (CAPs)** allow anyone with a minimum of `100
COMP` to create and deploy an _Autonomous Proposal_ , which is a smart
contract that includes the same parameters as a formal governance proposal (
_title, description, governance actions)._

The next step is gathering public support. Anyone can support the Autonomous
Proposal by visiting
[app.compound.finance/vote](http://app.compound.finance/vote), and delegating
their votes to the Ethereum address of the CAP.

When a CAP reaches the proposal threshold (currently 100,000 delegated votes),
anyone can call the public _launchProposal_ function, which creates a formal
governance proposal — and begins the voting process. Immediately after, anyone
can then call the _vote_ function on the Autonomous Proposal, casting its
delegated votes `FOR` the submitted proposal.

When a user creates an Autonomous Proposal, they lock COMP into the CAP; at
any time, the author can call the _terminateProposal_ function, which returns
their COMP and completes the Autonomous Proposal.

#  **The First Autonomous Proposal**

[![](https://miro.medium.com/max/1400/0*5OKd8lgTUQ3FYeMQ.png)](https://compound.finance/governance/address/0x0cde9622b23ababfccef9755b5f7c9e759ef4820)

Compound Labs built the Autonomous Proposals system, tested it end-to-end,
deployed it to mainnet, and has created the first ever CAP: [**Set Pause
Guardian to Community Multi-
Sig**](https://compound.finance/governance/address/0x0cde9622b23ababfccef9755b5f7c9e759ef4820).

This CAP proposes to set the [_Pause
Guardian_](https://compound.finance/docs/governance#pause-guardian) address of
the Compound protocol to a [4-of-6 multi-
sig](https://etherscan.io/address/0xbbf3f1421D886E9b2c5D716B5192aC998af2012c#code)
formed by the Compound community. For more background, please review the
details of the CAP.

If 100,000 votes are [delegated](https://app.compound.finance/vote) to this
CAP, it will proceed into the formal governance proposal and voting process.

#  **Create Your Own**

 **Autonomous Proposals** reduce the barrier to entry for creating governance
proposals by multiple orders of magnitude (from 100,000 COMP to 100).

On the [Vote page of the Compound
Interface](https://app.compound.finance/vote), any user with 100 COMP in their
wallet will see a **Create Autonomous Proposal** button. Clicking this button
will launch a flow for users to title, describe, and configure the proposal
they wish to create, and then deploy their Autonomous Proposal.

Try it out, and share your Autonomous Proposal with the Compound community on
[Twitter (@compoundfinance)](https://twitter.com/compoundfinance), in the
[Compound Community Forum (comp.xyz)](http://comp.xyz), and in the [Compound
Discord](http://compound.finance/discord).

As Autonomous Proposals start to aggregate large numbers of delegated votes,
you’ll also start to see them on the [Governance
Leaderboard](https://compound.finance/governance/leaderboard). Perhaps your
Autonomous Proposal will be one of the first!

\--

\--

\--

## [More from Compound](/compound-finance?source=post_page-----
354e7a2ad6b7--------------------------------)

Compound is an algorithmic, autonomous interest rate protocol built for
developers, to unlock a universe of open financial applications.

[Read more from Compound](/compound-finance?source=post_page-----
354e7a2ad6b7--------------------------------)

## Recommended from Medium

[[![TechnoDunes](https://miro.medium.com/fit/c/40/40/1*RAmSaGI0Cb8rsJPDInI0tQ.png)](/@technodunesofficial?source=post_internal_links
---------0----------------------------)

[TechnoDunes

](/@technodunesofficial?source=post_internal_links---------
0----------------------------)

## How does end-to-end encryption on WhatsApp work? — TechnoDunes

![](https://miro.medium.com/focal/112/112/50/50/0*-KK__LndGvFZuFU_.jpg)](/@technodunesofficial/how-
does-end-to-end-encryption-on-whatsapp-work-
technodunes-6fcd706bd3aa?source=post_internal_links---------
0----------------------------)

[[![Critical
Stack](https://miro.medium.com/fit/c/40/40/1*MvsL1YYDeZACQkGG7r1NUQ.png)](/@Critical_Stack?source=post_internal_links
---------1----------------------------)

[Critical Stack

](/@Critical_Stack?source=post_internal_links---------
1----------------------------)

in

[Critical Stack

](https://medium.com/critical-stack?source=post_internal_links---------
1----------------------------)

## Hello World: Sharing the Story of Critical Stack

](/critical-stack/hello-world-sharing-the-story-of-critical-
stack-12f4f584dedb?source=post_internal_links---------
1----------------------------)

[[![SecureSet](https://miro.medium.com/fit/c/40/40/1*co8nkh2DLhI_qIoUJF2CIw.jpeg)](/@SecureSetHQ?source=post_internal_links
---------2----------------------------)

[SecureSet

](/@SecureSetHQ?source=post_internal_links---------
2----------------------------)

in

[Command Line

](https://medium.com/secureset-blog?source=post_internal_links---------
2----------------------------)

## SecureSet Career Series: Compliance Analyst

![](https://miro.medium.com/focal/112/112/50/50/1*XE59Pebq5rKeWXxJ3gMGTQ.png)](/secureset-
blog/secureset-career-series-compliance-
analyst-1045dcbb4b57?source=post_internal_links---------
2----------------------------)

[[![Gijs
Hollestelle](https://miro.medium.com/fit/c/40/40/1*hlP86ieOH79ZxXk5hzFl5g.jpeg)](/@gijsh?source=post_internal_links
---------3----------------------------)

[Gijs Hollestelle

](/@gijsh?source=post_internal_links---------3----------------------------)

in

[FalconForce

](https://medium.com/falconforce?source=post_internal_links---------
3----------------------------)

## FalconFriday — Recognizing Beaconing Traffic— 0xFF0D

![](https://miro.medium.com/focal/112/112/50/50/1*udKdYiVsBioZYZSxBhLagQ.jpeg)](/falconforce/falconfriday-
recognizing-beaconing-traffic-0xff0d-f0fab038c22f?source=post_internal_links
---------3----------------------------)

[[![Jazmin
Sammie](https://miro.medium.com/fit/c/40/40/1*dmbNkD5D-u45r44go_cf0g.png)](/@didact1928?source=post_internal_links
---------4----------------------------)

[Jazmin Sammie

](/@didact1928?source=post_internal_links---------
4----------------------------)

## {UPDATE} Tank Of Tanks Battle Hack Free Resources Generator

](/@didact1928/update-tank-of-tanks-battle-hack-free-resources-
generator-3682ad597595?source=post_internal_links---------
4----------------------------)

[[![100TB.com](https://miro.medium.com/fit/c/40/40/0*gA0ygbZxzIDUd5NM.png)](/@100TB?source=post_internal_links
---------5----------------------------)

[100TB.com

](/@100TB?source=post_internal_links---------5----------------------------)

in

[20ms

](https://medium.com/20ms?source=post_internal_links---------
5----------------------------)

## Should You Use A Virtual Private Network?

![](https://miro.medium.com/focal/112/112/50/50/0*o8i5kkhSlreoBNvA.jpg)](/20ms/should-
you-use-a-virtual-private-network-b89291035a81?source=post_internal_links
---------5----------------------------)

[[![PRIYANSHU
JAIN](https://miro.medium.com/fit/c/40/40/1*-aUZir71yR2wsrEugXIaIQ.jpeg)](/@priyanshujain?source=post_internal_links
---------6----------------------------)

[PRIYANSHU JAIN

](/@priyanshujain?source=post_internal_links---------
6----------------------------)

in

[HackerNoon.com

](https://medium.com/hackernoon?source=post_internal_links---------
6----------------------------)

## Set Up SSL on Github Pages With Custom Domains for Free

![](https://miro.medium.com/focal/112/112/50/50/0*sZXJ6Kxmmk2hXyYn.)](/hackernoon/set-
up-ssl-on-github-pages-with-custom-domains-for-
free-a576bdf51bc?source=post_internal_links---------
6----------------------------)

[[![The
Capital](https://miro.medium.com/fit/c/40/40/2*KME86bfQzlPI2LVVNZTbTA.png)](/@thecapital?source=post_internal_links
---------7----------------------------)

[The Capital

](/@thecapital?source=post_internal_links---------
7----------------------------)

in

[The Capital

](https://medium.com/the-capital?source=post_internal_links---------
7----------------------------)

## SolidProof Thrives as It Incorporates an Auto Audit Tool

![](https://miro.medium.com/focal/112/112/50/50/1*MXTEuRMDst82BTufJfXVCQ.jpeg)](/the-
capital/solidproof-thrives-as-it-incorporates-an-auto-audit-tool-
cc090cff750c?source=post_internal_links---------7----------------------------)

[](/?source=post_page-----354e7a2ad6b7--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
354e7a2ad6b7--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
354e7a2ad6b7--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
354e7a2ad6b7--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
354e7a2ad6b7--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----354e7a2ad6b7--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----354e7a2ad6b7--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fcompound-
finance%2Fcompound-autonomous-proposals-354e7a2ad6b7&source=post_page
--------------------------nav_reg-----------)

[![Calvin
Liu](https://miro.medium.com/fit/c/176/176/2*KHATfyzZqZjQdzTKq1dIkA.jpeg)](/@cjliu49)

[

## Calvin Liu

](/@cjliu49)

694 Followers

Strategy Lead at Compound (<https://compound.finance>)

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fb154cefe7317&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fcompound-
finance%2Fcompound-autonomous-
proposals-354e7a2ad6b7&newsletterV3=8808a762900f&newsletterV3Id=b154cefe7317&user=Calvin+Liu&userId=8808a762900f&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Antonio
Juliano](https://miro.medium.com/fit/c/40/40/1*BPUYIqAFIYW7yvXX9UYbMQ.jpeg)](/@antonio-
dydx?source=read_next_recirc---------0---------------------
e90a1110_87d7_4189_a9ff_5dda06a57385-------)

[Antonio Juliano

](/@antonio-dydx?source=read_next_recirc---------0---------------------
e90a1110_87d7_4189_a9ff_5dda06a57385-------)

## Playing to our strengths

![](https://miro.medium.com/focal/112/112/50/50/1*GbduEqI6gKQaFotFg1oGmw.png)](/@antonio-
dydx/playing-to-our-strengths-489b7de4a5cc?source=read_next_recirc---------0
---------------------e90a1110_87d7_4189_a9ff_5dda06a57385-------)

[[![Rufat](https://miro.medium.com/fit/c/40/40/0*UIddrOHzmdWZ4tc8.png)](/@rufat31947337?source=read_next_recirc
---------1---------------------e90a1110_87d7_4189_a9ff_5dda06a57385-------)

[Rufat

](/@rufat31947337?source=read_next_recirc---------1---------------------
e90a1110_87d7_4189_a9ff_5dda06a57385-------)

## Aleo is built for the private web.

![](https://miro.medium.com/focal/112/112/50/50/1*YzY8T35ddog2ofjNnzOSEA.png)](/@rufat31947337/aleo-
is-built-for-the-private-web-aec723e0222f?source=read_next_recirc---------1
---------------------e90a1110_87d7_4189_a9ff_5dda06a57385-------)

[[![Sunny Jaycer](https://miro.medium.com/fit/c/40/40/1*gHP-
kUia53LrobuS_PLsCA.jpeg)](/@sunnyjaycer?source=read_next_recirc---------2
---------------------e90a1110_87d7_4189_a9ff_5dda06a57385-------)

[Sunny Jaycer

](/@sunnyjaycer?source=read_next_recirc---------2---------------------
e90a1110_87d7_4189_a9ff_5dda06a57385-------)

in

[Ricochet Exchange

](https://medium.com/ricochet-exchange?source=read_next_recirc---------2
---------------------e90a1110_87d7_4189_a9ff_5dda06a57385-------)

## Community Call #13 Recap

![](https://miro.medium.com/focal/112/112/50/50/1*PmO9hzg6WRHGkHCqPVS2Gw.png)](/ricochet-
exchange/community-call-13-recap-7a62bc97dda3?source=read_next_recirc---------
2---------------------e90a1110_87d7_4189_a9ff_5dda06a57385-------)

[[![Blockpour](https://miro.medium.com/fit/c/40/40/1*U4_54LAJHJv3K3hovwX4hA.jpeg)](/@blockpour?source=read_next_recirc
---------3---------------------e90a1110_87d7_4189_a9ff_5dda06a57385-------)

[Blockpour

](/@blockpour?source=read_next_recirc---------3---------------------
e90a1110_87d7_4189_a9ff_5dda06a57385-------)

## Blockpour Receives Infrastructure Grant From Polygon!

![](https://miro.medium.com/focal/112/112/50/50/0*cVYGqVTt3oUESsso)](/@blockpour/blockpour-
receives-infrastructure-grant-from-
polygon-1d2be80af1f1?source=read_next_recirc---------3---------------------
e90a1110_87d7_4189_a9ff_5dda06a57385-------)

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

