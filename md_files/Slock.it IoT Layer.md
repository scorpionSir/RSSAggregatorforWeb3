[](https://medium.com/)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/f305601df963&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](https://medium.com/)

[Home](https://medium.com/)

[Notifications](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![slock.it Blog](https://miro.medium.com/fit/c/64/64/1*ESYB-
YgQa2FKWPo2ofqCiQ.png)](https://blog.slock.it/?source=post_page-----
f305601df963--------------------------------)

Published in

[slock.it Blog

](https://blog.slock.it/?source=post_page-----
f305601df963--------------------------------)

[![Christoph Jentzsch](https://miro.medium.com/fit/c/96/96/0*LS-
Stb5ArckCafkQ.jpeg)](https://chrjentzsch.medium.com/?source=post_page-----
f305601df963--------------------------------)

[Christoph Jentzsch](https://chrjentzsch.medium.com/?source=post_page-----
f305601df963--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F697fe9612b56&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fslock-
it-iot-
layer-f305601df963&user=Christoph+Jentzsch&userId=697fe9612b56&source=post_page-697fe9612b56
----f305601df963---------------------follow_byline-----------)

Jun 8, 2018

·

8 min read

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Ff305601df963&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fslock-
it-iot-
layer-f305601df963&source=--------------------------bookmark_header-----------)

[

Save

](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Ff305601df963&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fslock-
it-iot-
layer-f305601df963&source=--------------------------bookmark_header-----------)

#  **Slock.it IoT Layer**

#  **Enabling the economy of things**

Exploring the field of technical devices means exploring new technologies and
understanding the world around us. In recent years, we’ve learned that
interaction with software is first and foremost screen-based. But that is
changing now. As the machine to machine interaction as well as the machine to
human interaction become more and more important, they open up new
possibilities for us to experience the world around us. The more devices are
connected to each other, the more possibilities they offer us. This change
provides a completely new way for users to experience their private and work
lives.

Most of us are familiar with **human to machine interaction** , in short: We
as humans pay a machine to do a certain service for us. In these times of
blockchain technology and cryptocurrencies, an example could look like this:
We pay a smart door lock to give us access to the apartment behind. Or we pay
a smart bike lock to let us use a bicycle. We can also pay a smart power plug
to turn on the power of any connected machine.

This is already reality. Just last month we made our Slock.it mobile App
available in the App store for android and apple devices to download for free
so that people can link their smart devices to the blockchain and give other
people access via payment. Although the app is still in testing mode, you can
already get a feeling of what we want it to eventually look like.

Another form of interaction is the **machine to machine communication**.
Imagine an electric car that needs to be charged. Driving to a charging
station would take extra time. But what if the car could buy electricity via
induction at a red traffic light?

In order for machines to be part of an economy of things, they need to
cooperate with each other on a different level beyond just transferring data.
They need to exchange values, and, most importantly, they need to be able to
enter into complex agreements.

Not too far into the future we will also see **machine to human
interactions**. So if we have an autonomous car, it needs someone to change
the tires. Not for free. The car itself will pay someone to do this.

Now, if this is the future we are heading into, we need a secure and open
infrastructure which will enable those use cases. However, the current IoT
infrastructure cannot deliver that.

 ** _Challenges we are facing_**

So far, the internet of things is quite fragmented and unsafe. Machines don’t
have wallets. They don’t have real digital cash. There are also high security
risks when it comes to interoperability. When building IoT systems you usually
have a tradeoff. Either you can decide to build a closed but secure system or
you can build a system which is open and integrated with IoT clouds, allowing
third-party access. Option one is fairly secure, although very limited in its
ability to use other apps or machines on top of it. Option two is great when
you want other apps to be built on top of your solution. However, you become
more and more vulnerable to each third party integration you are using. When
you get connected with others, you’re giving them a key to interact with your
system, and they, in return, could give this key to a third party. Which, of
course, is something you don’t want.

blockchain gives us the opportunity to solve a lot of these issues. It gives
us wallets for machines once they have keys. With blockchain technology, you
don’t have any single point of failure or one data center which stores all the
keys. Additionally, you have a common layer which acts as an open API to
interact with others. With blockchain and smart contracts, we can get both:
security and interoperability.

It’s a nice vision to use blockchain technology for IoT devices. And yet, how
can you securely connect a device to the blockchain? First, you have to ask
whether you “just” want to write to (sending a transaction) or read from the
blockchain. Surprisingly, it is much easier to write than to read. For
writing, it is sufficient to have a private key within the device and a
connection to a node in the p2p network of the blockchain of your choice.
Although getting a confirmation that your transaction was actually included is
again a read process, which is harder. In order to read, you need to verify
the chain. This brings us to the second matter you need to address, choosing a
client and its configuration. There are different options to this: First,
running a **full client.** This **** stores everything, the whole state, the
past states, the whole blockchain. The downside: you need a lot of storage,
high bandwidth and a lot of CPU power. This is just impossible in the IoT
world. Now there is also a **pruned full node**. There you delete all the past
states and store only the blockchain itself in addition to the most recent
states. That’s already a big step. With this you still have the full
verification of the blockchain history. However, most disadvantages stay, such
as long synchronization time and still quite some storage demand.

Then there’s the **light client** , which seems most fitting to the IoT world.
It needs roughly 50 MB and you only synchronize the blockheaders without
computing the state by running all the transactions of a block. After
verifying the blockheaders, you can use a Merkle Proof to verify a certain
part of the state in the blockchain. This sounds good. But still, if you
measure how much data goes through this light client, it is still far too much
for most practical IoT use cases. This is because the light client is still
part of the p2p network and acts as a node. It also means, it needs to
synchronize before it first starts, and again in the case, it has been offline
for a while. So for use cases where you want to read from the blockchain once
a month or so, this is still impractical. The lightest option is the **remote
client**. This means you just connect to a server and it responds to your
request. The drawback here: It’s not trustfree. You have to trust the
information you’re getting from the server. Also, it introduces a single point
of failure to your solution. So what could we do? (For a more detailed
explanation of clients and configuration options, this post is highly
recommended: <https://dev.to/5chdn/the-ethereum-blockchain-size-will-not-
exceed-1tb-anytime-soon-58a>)

![](https://miro.medium.com/max/1400/0*XwkUguKX0tdTyaBx)

 ** _Introducing Slock.it IN_** ³ ** _(Incubed)_**

Our team at Slock.it got together to brainstorm different options. We wanted
to have a secure solution which removes the need to trust a single server and
we didn’t want to spend time synchronizing the chain. Neither did we want to
store anything beyond the software itself. We also wanted it to work with all
EVM-based blockchains, have minimal bandwidth requirements, and it was
supposed to only communicate when it was actually needed. We found the answer,
and called it INCUBED (IN³)! A trustless **in** centivized remote **n** ode
**n** etwork. In short, a network of remote nodes, which are incentivized to
always give you the right response.

 **Incubed** consists of a network of nodes which act as servers to the IoT
devices that are running a Slock.it client. Those nodes have paid a deposit
which they would lose in case they give a wrong response. Those nodes also act
as watchdogs checking each others’ responses. The IoT devices which run a
Slock.it client only verify the responses, similar to a light client. But
instead of synchronizing the blockheaders, they receive signed blockhashes
from the Incubed nodes. Since they can verify how much they deposited, they
know how secure the response is. Additionally, they can ask for several signed
blockhashes from multiple nodes.

In detail it works like this:

  * I am a full node. I register at the registry smart contract and pay a deposit, which I would lose if I lied. Several nodes will do the same.
  * An IoT device, running the Slock.it client now sends an RPC request to one of those nodes. There are three things the device needs to know in order to verify that the information is true: 1. The Merkle proof, similar to a light client. 2. The current block header. 3. A signed blockhash (from that blockheader) from several incubed nodes which are specified by the device.
  * The device can publish this information. If someone finds this to be wrong, he can claim the deposit of this node. This is done by so called watchdogs. The node which received the initial request from the client also acts as a watchdog.
  * Since the IoT device, running the Slock.it client, asked other incubed nodes to sign the blockhash as well, it can verify the response and claim the deposit in case a wrong blockhash was signed. This happens in the convict function within the registry smart contract. (The only piece of information within the Ethereum virtual machine which you can get from the past are the blockhashes from the last 256 blocks. This is what Slock.it is using to build a fully decentralized system without any central authority or central node controlling the system.)

![](https://miro.medium.com/max/1400/0*A6DutYjPKYDWDcVO)

For the security critical service of signing blockhashes, the incubed nodes
will receive a micropayment from the client. This can come directly from the
device or optionally the device operator (if existent).

Incubed, though, is only part of a greater product Slock.it is building at the
moment. **The Slock.it IoT Layer** has much more to it. It includes payment
channels, hub services, a discovery service (marketplace for IoT devices) a
messaging system, access control smart contracts and integrations within
existing IoT clouds, as well as software images for commonly used systems on a
chip such as the raspberry pi or the samsung artik.

![](https://miro.medium.com/max/1400/0*DTxk5W_NgIH0OBEf)

This Slock.it IoT Layer solves the problem of efficiently connecting a device
to the blockchain and adds the necessary features for it to become usable to
non-blockchain developers working on IoT systems. It is highly interoperable
with other devices and completely decentralized. You get the security of a
blockchain, the interoperability of IoT clouds, and all this without needing a
login other than your cryptographic keys.

At [EventHorizon](https://youtu.be/faesmyMPlYY) in Berlin this past April, we
were able to present this idea to a large crowd of experts, government
representatives, decision-makers, start-ups and established market
participants. For us, it was a huge success. Slock.it was
[awarded](https://twitter.com/eventhorizonx/status/986942707015782400) by the
participants with the “Top of the Horizon” prize, which we’re honored to have
received.

Here you can find the video of the presentation explaining the concept:
<https://youtu.be/faesmyMPlYY>

![](https://miro.medium.com/max/1400/1*mBMw5RfvNQnTn1pfPYbINw.jpeg)

<https://twitter.com/Kevin_ODonovan/status/986887097087819781>

As the interaction between machine and machine as well as machine to human
becomes more and more important in today’s world, the possibilities seem
endless. We at Slock.it are working on building a solution **from developers
for developers** which solves the security and interoperability problems that
exist in many IoT systems. We will have those IoT devices pay and receive
payments, as well as enter into complex agreements in order to enable the
economy of things.

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fslock-
it-
blog%2Ff305601df963&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fslock-
it-iot-
layer-f305601df963&user=Christoph+Jentzsch&userId=697fe9612b56&source=-----f305601df963
---------------------clap_footer-----------)

\--

2

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fslock-
it-
blog%2Ff305601df963&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fslock-
it-iot-
layer-f305601df963&user=Christoph+Jentzsch&userId=697fe9612b56&source=-----f305601df963
---------------------clap_footer-----------)

\--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fslock-
it-
blog%2Ff305601df963&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fslock-
it-iot-
layer-f305601df963&user=Christoph+Jentzsch&userId=697fe9612b56&source=-----f305601df963
---------------------clap_footer-----------)

\--

2

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Ff305601df963&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fslock-
it-iot-
layer-f305601df963&source=--------------------------bookmark_footer-----------)

## [More from slock.it Blog](https://blog.slock.it/?source=post_page-----
f305601df963--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Fslock-
it-
blog%2Ff305601df963&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fslock-
it-iot-
layer-f305601df963&collection=slock.it+Blog&collectionId=15115b6d917a&source=post_page
-----f305601df963---------------------follow_footer-----------)

IoT + Blockchain

[Read more from slock.it Blog](https://blog.slock.it/?source=post_page-----
f305601df963--------------------------------)

## Recommended from Medium

[[![Spheron \(previously
ArGoApp\)](https://miro.medium.com/fit/c/40/40/1*0lVtiLa6b7cerLEDSHXOgw.jpeg)](https://spheron.medium.com/?source=post_internal_links
---------0----------------------------)

[Spheron (previously ArGoApp)

](https://spheron.medium.com/?source=post_internal_links---------
0----------------------------)

## How is Spheron (previously ArGoApp) removing barriers to assist Web2.0

![](https://miro.medium.com/focal/112/112/50/50/1*U9ZQZ2x7dshmK_B-
HbMPUw.jpeg)](https://spheron.medium.com/how-is-argoapp-removing-barriers-to-
assist-web2-0-developers-move-to-the-new-
web-a93e7822b93b?source=post_internal_links---------
0----------------------------)

[[![Dukidumbla](https://miro.medium.com/fit/c/40/40/0*6TlKuPEhZLO7IG8o.jpg)](https://medium.com/@dukidumbla?source=post_internal_links
---------1----------------------------)

[Dukidumbla

](https://medium.com/@dukidumbla?source=post_internal_links---------
1----------------------------)

## expected idea of ULTIX.IO stage Presentation

![](https://miro.medium.com/focal/112/112/50/50/0*57cSzUg5xrQiLRqu.png)](https://medium.com/@dukidumbla/expected-
idea-of-ultix-io-stage-presentation-e6ae3b4596db?source=post_internal_links
---------1----------------------------)

[[![Munch
Project](https://miro.medium.com/fit/c/40/40/1*P91wdCr1nMbEp7BZwMIe3Q.jpeg)](https://munchproject.medium.com/?source=post_internal_links
---------2----------------------------)

[Munch Project

](https://munchproject.medium.com/?source=post_internal_links---------
2----------------------------)

## It’s grow time! The MUNCH farm for asset staking is now live!

![](https://miro.medium.com/focal/112/112/50/50/1*Pkrck25uORRt00ghMVSMUQ.jpeg)](https://munchproject.medium.com/its-
grow-time-the-munch-farm-for-asset-staking-is-now-
live-9c01186833cf?source=post_internal_links---------
2----------------------------)

[[![Genius](https://miro.medium.com/fit/c/40/40/1*dmbNkD5D-u45r44go_cf0g.png)](https://medium.com/@geni29056?source=post_internal_links
---------3----------------------------)

[Genius

](https://medium.com/@geni29056?source=post_internal_links---------
3----------------------------)

## EKTA best Project

![](https://miro.medium.com/focal/112/112/50/50/1*9j2R5KVqnHw52lf41xDVJg.jpeg)](https://medium.com/@geni29056/ekta-
best-project-f9905f96915a?source=post_internal_links---------
3----------------------------)

[[![Patreon
Token](https://miro.medium.com/fit/c/40/40/1*AjzBVNG42eOnsyfY7WfhrA.png)](https://patreontoken.medium.com/?source=post_internal_links
---------4----------------------------)

[Patreon Token

](https://patreontoken.medium.com/?source=post_internal_links---------
4----------------------------)

## Cardano (ADA): A Research-Laden History and Roadmap

![](https://miro.medium.com/focal/112/112/50/50/0*KwU1G0fn0hyFpoSz.jpg)](https://patreontoken.medium.com/cardano-
ada-a-research-laden-history-and-
roadmap-b27f68ce7b6a?source=post_internal_links---------
4----------------------------)

[[![Pandaswap](https://miro.medium.com/fit/c/40/40/1*GVypEzs4hMBf0nIXJQRzow.png)](https://pandaswapex.medium.com/?source=post_internal_links
---------5----------------------------)

[Pandaswap

](https://pandaswapex.medium.com/?source=post_internal_links---------
5----------------------------)

## The Pandaswap Project | Avalanche

![](https://miro.medium.com/focal/112/112/50/50/1*qEGIATrkfEeO2yMlpP2inA.png)](https://pandaswapex.medium.com/the-
pandaswap-project-avalanche-f011e5320c12?source=post_internal_links---------
5----------------------------)

[[![Injective
Labs](https://miro.medium.com/fit/c/40/40/1*syKbtBges_DDxCr3SbRnyg.jpeg)](https://injectiveprotocol.medium.com/?source=post_internal_links
---------6----------------------------)

[Injective Labs

](https://injectiveprotocol.medium.com/?source=post_internal_links---------
6----------------------------)

in

[Injective

](https://medium.com/injective-labs?source=post_internal_links---------
6----------------------------)

## Injective Launches the World’s First Decentralized Stock Futures Trading

![](https://miro.medium.com/focal/112/112/50/50/0*Et_nZ7QN2NQtA-
Jf)](https://medium.com/injective-labs/injective-launches-the-worlds-first-
decentralized-stock-futures-trading-feb1c8aefc71?source=post_internal_links
---------6----------------------------)

[[![EOSeoul](https://miro.medium.com/fit/c/40/40/2*0oLSvgFH9d4xyXrJT9qMYQ.png)](https://medium.com/@eoseoulkor?source=post_internal_links
---------7----------------------------)

[EOSeoul

](https://medium.com/@eoseoulkor?source=post_internal_links---------
7----------------------------)

in

[EOSeoul

](https://medium.com/eoseoul?source=post_internal_links---------
7----------------------------)

## EOS Worker Proposal System Announcement

![](https://miro.medium.com/focal/112/112/50/50/1*88CJ3b6zYg7RanWvXND_Zw.png)](https://medium.com/eoseoul/eos-
worker-proposal-system-announcement-e6b3e8084e6b?source=post_internal_links
---------7----------------------------)

[](https://medium.com/?source=post_page-----
f305601df963--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
f305601df963--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
f305601df963--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
f305601df963--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
f305601df963--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----f305601df963--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----f305601df963--------------------------------)

[Get
started](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fslock-
it-iot-layer-f305601df963&source=post_page--------------------------
nav_reg-----------)

[![Christoph Jentzsch](https://miro.medium.com/fit/c/176/176/0*LS-
Stb5ArckCafkQ.jpeg)](https://chrjentzsch.medium.com)

[

## Christoph Jentzsch

](https://chrjentzsch.medium.com)

1K Followers

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F697fe9612b56&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fslock-
it-iot-
layer-f305601df963&user=Christoph+Jentzsch&userId=697fe9612b56&source=post_page-697fe9612b56
-------------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F5e97cc975e28&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fslock-
it-iot-
layer-f305601df963&newsletterV3=697fe9612b56&newsletterV3Id=5e97cc975e28&user=Christoph+Jentzsch&userId=697fe9612b56&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Superfluid](https://miro.medium.com/fit/c/40/40/1*JINdTrpldrRv2LcYpoW0Vg.gif)](https://medium.com/@superfluid_HQ?source=read_next_recirc
---------0---------------------67fe3df0_7903_41b0_bcbf_cb5a802a38ae-------)

[Superfluid

](https://medium.com/@superfluid_HQ?source=read_next_recirc---------0
---------------------67fe3df0_7903_41b0_bcbf_cb5a802a38ae-------)

in

[Superfluid Blog

](https://medium.com/superfluid-blog?source=read_next_recirc---------0
---------------------67fe3df0_7903_41b0_bcbf_cb5a802a38ae-------)

## Superfluid Sponsoring ETHernals 2022 Hackathon

![](https://miro.medium.com/focal/112/112/50/50/1*r1uPaSLri9KjVbu8P-Rfbg.png)](https://medium.com/superfluid-
blog/superfluid-sponsoring-
ethernals-2022-hackathon-2b6ddb135aa8?source=read_next_recirc---------0
---------------------67fe3df0_7903_41b0_bcbf_cb5a802a38ae-------)

[[![Timothy Hao Chi
Ho](https://miro.medium.com/fit/c/40/40/1*JlD7bKJG1GAjl5MxZN96kw.png)](https://tim-
hch.medium.com/?source=read_next_recirc---------1---------------------
67fe3df0_7903_41b0_bcbf_cb5a802a38ae-------)

[Timothy Hao Chi Ho

](https://tim-hch.medium.com/?source=read_next_recirc---------1
---------------------67fe3df0_7903_41b0_bcbf_cb5a802a38ae-------)

in

[ChainSafe

](https://blog.chainsafe.io/?source=read_next_recirc---------1
---------------------67fe3df0_7903_41b0_bcbf_cb5a802a38ae-------)

## Glow of the Canopy #1 🌱: Nourishing the Filecoin Virtual Machine with help
from Forest 🌲

![](https://miro.medium.com/focal/112/112/50/50/0*fH72IfjPczZ2c8qs)](https://blog.chainsafe.io/glow-
of-the-canopy-1-nourishing-the-filecoin-virtual-machine-with-help-from-
forest-6249354f9fb9?source=read_next_recirc---------1---------------------
67fe3df0_7903_41b0_bcbf_cb5a802a38ae-------)

[[![Novon](https://miro.medium.com/fit/c/40/40/1*R3iiw5VD_oo5bveXJVITFg.jpeg)](https://medium.com/@novondotio?source=read_next_recirc
---------2---------------------67fe3df0_7903_41b0_bcbf_cb5a802a38ae-------)

[Novon

](https://medium.com/@novondotio?source=read_next_recirc---------2
---------------------67fe3df0_7903_41b0_bcbf_cb5a802a38ae-------)

in

[Xord

](https://medium.com/xord?source=read_next_recirc---------2
---------------------67fe3df0_7903_41b0_bcbf_cb5a802a38ae-------)

## Novon: Docking into Xord

![](https://miro.medium.com/focal/112/112/50/50/1*jGGFEVEhrt_K9SIRLiFe7w.png)](https://medium.com/xord/novon-
docking-into-xord-fc88b70696c2?source=read_next_recirc---------2
---------------------67fe3df0_7903_41b0_bcbf_cb5a802a38ae-------)

[[![AI
Network](https://miro.medium.com/fit/c/40/40/1*GWMy0ibykACFKS_rRxFlcw.png)](https://ai-
network.medium.com/?source=read_next_recirc---------3---------------------
67fe3df0_7903_41b0_bcbf_cb5a802a38ae-------)

[AI Network

](https://ai-network.medium.com/?source=read_next_recirc---------3
---------------------67fe3df0_7903_41b0_bcbf_cb5a802a38ae-------)

in

[AI Network

](https://medium.com/ai-network?source=read_next_recirc---------3
---------------------67fe3df0_7903_41b0_bcbf_cb5a802a38ae-------)

## AI Network Monthly Update: April 2022

![](https://miro.medium.com/focal/112/112/50/50/1*fWUB5N27bdJsIZdCNfV9bA.jpeg)](https://medium.com/ai-
network/ai-network-monthly-update-
april-2022-bb1d38bcd3e6?source=read_next_recirc---------3---------------------
67fe3df0_7903_41b0_bcbf_cb5a802a38ae-------)

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

