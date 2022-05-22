[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/8e740dac31fa&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Muun](https://miro.medium.com/fit/c/64/64/1*ZHNsPvynwNOPydFxp27GCw.png)](https://medium.com/muunwallet?source=post_page
-----8e740dac31fa--------------------------------)

Published in

[Muun

](https://medium.com/muunwallet?source=post_page-----
8e740dac31fa--------------------------------)

[![Nico
Rey](https://miro.medium.com/fit/c/96/96/0*DicjFSxJ_k4MCpwk.)](/@rey.nico?source=post_page
-----8e740dac31fa--------------------------------)

[Nico Rey](/@rey.nico?source=post_page-----
8e740dac31fa--------------------------------)

Follow

Oct 21, 2019

·

7 min read

# How to Build a Bulletproof Lightning Node

![](https://miro.medium.com/max/1400/1*Y6eR7MC0wzghjTzMSx9yIg.jpeg)

 _Originally published at_[
_https://blog.muun.com_](https://blog.muun.com/how-to-build-a-bulletproof-
lightning-node/) _on October 21, 2019._

Every time I think of bitcoin and the Lightning Network, I keep security and
privacy in mind. Nobody wants to lose money, right? When building
infrastructure, I keep the same mindset. What happens when you build
infrastructure for bitcoin? Well…

Let’s talk from a security and reliability standpoint: how can we build a
strong and secure Linux box to run LND? This is critical for a Lightning node
because it is software that manages a hot wallet. Also, this is relatively new
software, so it is less battle-tested than others.

 **In this post, we analyze possible edge cases and security breaches on
services. We also share some specific insights on LND secret management.**

# Starting with a solid and secure base

Nowadays, instance hardening is a must for whatever you are building. Your
software could be great at security, but your entire ecosystem is only as
secure as its weakest link.

Let’s be super clear on this: it’s mandatory to have all the security updates
enabled and to keep the Linux kernel and Lightning software updated.

Let’s consider a Linux instance. Why is this important? Mainly because you run
the software that boots up and loads the kernel, with all the tools you need
to ship your delightful application. All this software must be protected
against malicious bugs such as 0-day attacks, privilege escalation, and so on.

In the case of LND, a dangerous exploit was discovered a few months ago, and
the ability to smoothly upgrade our nodes was critical:

A good practice to keep the software updated is to watch the LND repository
for releases, so for each release, we can dig into the changelog and apply it
to our nodes.

All in all, I always recommend the K.I.S.S. (“keep it simple, stupid”)
principle: install just the software you need, configure it properly, and
upgrade it periodically.

You also need to consider which parts you will expose to the Internet: is the
service safe enough to be exposed to all the Internet? Is this an attack
vector? Do you need a firewall to protect it?

Some software packages use network control endpoints, such as RPC endpoints,
to control the software and do operations over it. Basically, every control
point you need to use may go over that network control endpoint.

At least once in the life of any developer, you will be tempted to grant all
permissions to an app or just forward all the ports on the router to the app.
Nothing is wrong with it; you’re just fully exposing a control endpoint to the
whole Internet, where the bad guys are more than ready to start attacking
using a wide variety of known tools and strategies!

So, is this service robust enough to be exposed to all the Internet? Maybe not
at all. Is this an attack vector? Sure it is! Do you need a firewall? Yes!

Let’s look at LND’s case in particular. Under the hood, LND exposes three
major ports:

  * 9735: the port from which nodes are reachable. There’s no way around this one; it must be exposed to all the Internet to allow other nodes to connect to you and open channels.
  * 10009: the management port (the RPC port). This port SHOULDN’T be exposed to the Internet, because it is the way you control your node, create invoices, open channels, connect to peers, and so on. Ideally, this port should listen only on localhost, where you run lncli (the command line interface software to talk with LND). You could, though, expose it to a private network subnet where your management server is. Just be sure to keep an eye on the network neighbors.
  * 8080: If enabled, this is the REST API listen port. Like the previous one, DON’T expose this to the Internet. It is fair enough to expose it to your internal network or subnet.

 _A note on listening on your private network_ : your private network now
turns into your weak link! If you share your network connection with someone
else, take care of access management. We may explore this in future posts.

![](https://miro.medium.com/max/1400/1*zUx0ObYkkD8JhBSgGMQ7XQ.jpeg)

What happens when you leave the default SSH connection port exposed to the
Internet? Yup. Thousands of bots hitting your SSH server brute-forcing
usernames and passwords every second. The same happens with almost every
service you expose on its default port, given that automated attacks are
incredibly fast these days. If you are handling money, better safe than sorry!

![](https://miro.medium.com/max/1400/0*oSL-A9L4-YfDSmMc.jpg)

When your Linux box is strong enough to serve a shiny Lightning node, your
next concern is securing the secret values. LND strongly relies on secret
files, passwords, and certificates, and we must take care of them.

# Storing your secrets

LND handles several secrets on each instance. These are a wallet password,
keys, certificates, macaroon files for gRPC authentication, and a recovery
seed.

What do you do with them? Shall we write it on plain paper and keep it in a
secret box under your bed?

![](https://miro.medium.com/max/1400/0*yZLGYX8mWEPPvnjC.gif)

Well, working with LND has some challenges worth mentioning:

A software update requires a restart, and restarting a node requires the
wallet password. Losing your password makes things difficult: you will not be
able to start your node again.

Recovering your funds from a broken LND instance requires your 24-word seed.
If you cannot remember your seed, you’re in big trouble. Of course, you won’t
be in as much trouble as you would be if it’s stolen: an attacker will drain
your wallet in a matter of minutes if this happens.

Last, the node interaction (opening a channel, listing peers, making a
payment, or generating an invoice) requires macaroon files.

So, is plain paper storage a good idea? Certainly not, at least for management
files. If someone steals your macaroon files, he will get control over your
running node with full capabilities to drain it.

Things could get even more complex. What if you want to run several nodes at a
time? In this case, secret organization becomes crucial, and considering a
custom piece of software to handle them might be a good idea.

If you want to cut down on human error, a simple piece of software that
interacts with the node and a secret storage system (a key: value system) are
enough. However, you must take into account the secret rotation feature: a
must when doing updates or node migrations, because certificates will change
if the node’s IP or hostname changes.

AWS Secrets Manager is a good example: with a good trade-off between cost,
implementation difficulty, scalability, and security, it became the source of
truth for LND Secrets. Another solution, Hashicorp Vault, is recommended as
well.

This choice requires serious consideration because it’s not easy to fulfill
the requirements for a secret management strategy. Here are some key aspects
you need to consider:

  * Scalability: consider that you might end up running multiple environments, networks, and nodes. For example, two environments (development, production) could have two networks (testnet, mainnet) each. Even worse, if you happen to be running more than one node, you will need to consider all combinations for each one of them.
  * Security: choose secret and secure storage that only you and your nodes can access. Make sure there is enough granularity, and pay attention to how you distribute the ability to grant access by the right node/network/environment combination. This is very important: we don’t want a development/testnet node to have access to a production/mainnet node credentials. If something fails in development, we may expose production to a big security breach!
  * Flexibility: take into consideration the fact that secrets such as tls.cert and tls.key need to be replaced every time your node’s domain or IP address changes (The key-cert pair is attached to a defined IP/hostname). Therefore, make sure you have the ability to update secrets regularly. Well-tested key management software is a game-changer when working with LND.

# Conclusion

Bringing up a Lightning node could be a great Lightning experience and an
opportunity to learn about security, software scalability, and secret
management. It will also help you think about keeping a clean and simple way
to deploy and upgrade your nodes. Because LND is in constant development, it’s
important to be up to date with the software and its requirements to build a
fast, reliable infrastructure ready to join the Lightning network.

 _Visit Muun Website:_[ _https://muun.com/_](https://muun.com/)

 _Follow Muun on Twitter:_[
_https://twitter.com/MuunWallet_](https://twitter.com/MuunWallet)

 _Originally published at_[
_https://blog.muun.com_](https://blog.muun.com/how-to-build-a-bulletproof-
lightning-node/) _on October 21, 2019._

\--

\--

\--

## [More from Muun](/muunwallet?source=post_page-----
8e740dac31fa--------------------------------)

Stories from Muun, the most powerful Bitcoin and Lightning wallet

[Read more from Muun](/muunwallet?source=post_page-----
8e740dac31fa--------------------------------)

## Recommended from Medium

[[![Radware](https://miro.medium.com/fit/c/40/40/1*DHrZHFBqugr3jJlul7Spyw.jpeg)](/@RadwareBlog?source=post_internal_links
---------0----------------------------)

[Radware

](/@RadwareBlog?source=post_internal_links---------
0----------------------------)

## IoT Hackers Trick Brazilian Bank Customers into Providing Sensitive
Information

![](https://miro.medium.com/focal/112/112/50/50/0*I8JDWRKtQM8R8DHW.jpg)](/@RadwareBlog/iot-
hackers-trick-brazilian-bank-customers-into-providing-sensitive-
information-846664ff2ea8?source=post_internal_links---------
0----------------------------)

[[![Polis
Chain](https://miro.medium.com/fit/c/40/40/1*3r5nQFBZXpWGCAvsAhXqPg.png)](/@polischain?source=post_internal_links
---------1----------------------------)

[Polis Chain

](/@polischain?source=post_internal_links---------
1----------------------------)

## New Platform is live!

![](https://miro.medium.com/focal/112/112/50/50/1*MTsZFgdiI9uHSplGTaG8SA.png)](/@polischain/new-
platform-is-live-709ffe1772e6?source=post_internal_links---------
1----------------------------)

[[![ViSa](https://miro.medium.com/fit/c/40/40/1*wWLCpkPdU4tsxNjYnhwWXg.jpeg)](/@myvisa?source=post_internal_links
---------2----------------------------)

[ViSa

](/@myvisa?source=post_internal_links---------2----------------------------)

## OWASP Security Vulnerabilities 2020

![](https://miro.medium.com/focal/112/112/50/50/1*T1UjfUzmZCkG-
WEy8hQIug.jpeg)](/@myvisa/owasp-security-
vulnerabilities-2020-e92f6657951e?source=post_internal_links---------
2----------------------------)

[[![Money
Quick](https://miro.medium.com/fit/c/40/40/1*7aTMA5vEqGTu-39X7pzGng.png)](/@moneyquicks?source=post_internal_links
---------3----------------------------)

[Money Quick

](/@moneyquicks?source=post_internal_links---------
3----------------------------)

## Binance

![](https://miro.medium.com/focal/112/112/50/50/1*dUZVIBDk9LOAfPChs4cuPw@2x.jpeg)](/series/binance-9bedb84e019b?source=post_internal_links
---------3----------------------------)

[[![Daniel
J.Anthony](https://miro.medium.com/fit/c/40/40/0*QSuGclj8YwOTLKok.)](/@Daniel.Anthony?source=post_internal_links
---------4----------------------------)

[Daniel J.Anthony

](/@Daniel.Anthony?source=post_internal_links---------
4----------------------------)

## Scan Magento site for malware!

](/@Daniel.Anthony/scan-magento-site-for-
malware-8fdd41cbde52?source=post_internal_links---------
4----------------------------)

[[![Abhinav
Pathak](https://miro.medium.com/fit/c/40/40/2*yTXFe6LTz3JyoStJ4ZW-6Q.jpeg)](/@pathakabhi24?source=post_internal_links
---------5----------------------------)

[Abhinav Pathak

](/@pathakabhi24?source=post_internal_links---------
5----------------------------)

in

[System Weakness

](https://medium.com/system-weakness?source=post_internal_links---------
5----------------------------)

## Chrome Extensions Used For Hacking

![](https://miro.medium.com/focal/112/112/50/50/1*Re8hZDHJpsC-9QXlI07pdg.jpeg)](/system-
weakness/chrome-extensions-used-for-
hacking-6fdb57a02dc4?source=post_internal_links---------
5----------------------------)

[[![Jossef
Harush](https://miro.medium.com/fit/c/40/40/1*zrkR7PYXfzIAwrWc3eHd7w.png)](/@jossef?source=post_internal_links
---------6----------------------------)

[Jossef Harush

](/@jossef?source=post_internal_links---------6----------------------------)

in

[checkmarx-security

](https://medium.com/checkmarx-security?source=post_internal_links---------
6----------------------------)

## Webhook Party — Malicious packages caught exfiltrating data via legit
webhook services

![](https://miro.medium.com/focal/112/112/50/50/1*9IS6g2_nFzf9ZXtwZU-
KXA.png)](/checkmarx-security/webhook-party-malicious-packages-caught-
exfiltrating-data-via-legit-webhook-
services-6e046b07d191?source=post_internal_links---------
6----------------------------)

[[![stack
overflow](https://miro.medium.com/fit/c/40/40/1*OmdzyBoiZDxFfxtP6gbcDw.png)](/@PratikshaBhad?source=post_internal_links
---------7----------------------------)

[stack overflow

](/@PratikshaBhad?source=post_internal_links---------
7----------------------------)

## sdes 8 b

](/@PratikshaBhad/sdes-8-b-126d5133662b?source=post_internal_links---------
7----------------------------)

[](/?source=post_page-----8e740dac31fa--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
8e740dac31fa--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
8e740dac31fa--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
8e740dac31fa--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
8e740dac31fa--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----8e740dac31fa--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----8e740dac31fa--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fmuunwallet%2Fhow-
to-build-a-bulletproof-lightning-node-8e740dac31fa&source=post_page
--------------------------nav_reg-----------)

[![Nico
Rey](https://miro.medium.com/fit/c/176/176/0*DicjFSxJ_k4MCpwk.)](/@rey.nico)

[

## Nico Rey

](/@rey.nico)

2 Followers

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fusers%2Fed8a14017648%2Flazily-enable-
writer-
subscription&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fmuunwallet%2Fhow-
to-build-a-bulletproof-lightning-
node-8e740dac31fa&user=Nico+Rey&userId=ed8a14017648&source=--------------------------subscribe_user-----------)

## More from Medium

[[![BlockApex](https://miro.medium.com/fit/c/40/40/1*9OehZq_96XPXT5qV65i7QQ.jpeg)](/@blockapex?source=read_next_recirc
---------0---------------------a9ee62ef_32e1_4f6d_a0a5_8de4566c906d-------)

[BlockApex

](/@blockapex?source=read_next_recirc---------0---------------------
a9ee62ef_32e1_4f6d_a0a5_8de4566c906d-------)

## The Rise and Fall of Proof of Work: Is Proof Of Stake The Inevitable
Solution?

![](https://miro.medium.com/focal/112/112/50/50/1*cOYRlJCQEhQUxK6KIdDjZA.png)](/@blockapex/the-
rise-and-fall-of-proof-of-work-is-proof-of-stake-the-inevitable-
solution-4e16adb6b427?source=read_next_recirc---------0---------------------
a9ee62ef_32e1_4f6d_a0a5_8de4566c906d-------)

[[![Perrybiz](https://miro.medium.com/fit/c/40/40/1*fre0jD23MdLLvjDL-
EnjKg.png)](/@percyding66?source=read_next_recirc---------1
---------------------a9ee62ef_32e1_4f6d_a0a5_8de4566c906d-------)

[Perrybiz

](/@percyding66?source=read_next_recirc---------1---------------------
a9ee62ef_32e1_4f6d_a0a5_8de4566c906d-------)

## Learning Crypto #3: Solidity & Remix

![](https://miro.medium.com/focal/112/112/50/50/1*CEXufviPdkAp4Wb-_3DN2g.png)](/@percyding66/learning-
crypto-3-solidity-remix-2fd344a77f31?source=read_next_recirc---------1
---------------------a9ee62ef_32e1_4f6d_a0a5_8de4566c906d-------)

[[![Xelene
Aguiar](https://miro.medium.com/fit/c/40/40/0*NvjNL0j7BVEcRf3x)](/@xelene.aguiar?source=read_next_recirc
---------2---------------------a9ee62ef_32e1_4f6d_a0a5_8de4566c906d-------)

[Xelene Aguiar

](/@xelene.aguiar?source=read_next_recirc---------2---------------------
a9ee62ef_32e1_4f6d_a0a5_8de4566c906d-------)

## Busted: 3 Myths about the use of Blockchain in Supply Chain Management

![](https://miro.medium.com/focal/112/112/50/50/0*qsr_xor55z5Xb2dx)](/@xelene.aguiar/busted-3-myths-
about-the-use-of-blockchain-in-supply-chain-
management-4f98584a6b45?source=read_next_recirc---------2---------------------
a9ee62ef_32e1_4f6d_a0a5_8de4566c906d-------)

[[![Bennie Seybold](https://miro.medium.com/fit/c/40/40/1*sI32j8_Q-
New7Wukwl4Bhg.jpeg)](/@bennie3033?source=read_next_recirc---------3
---------------------a9ee62ef_32e1_4f6d_a0a5_8de4566c906d-------)

[Bennie Seybold

](/@bennie3033?source=read_next_recirc---------3---------------------
a9ee62ef_32e1_4f6d_a0a5_8de4566c906d-------)

## Instant Settlement Protocols — How Blockchain Will Revolutionize Payroll

![](https://miro.medium.com/focal/112/112/50/50/1*cUvV_BVfQA7aH0Dpj4cyfA.png)](/@bennie3033/instant-
settlement-protocols-bb7aa8d10cb6?source=read_next_recirc---------3
---------------------a9ee62ef_32e1_4f6d_a0a5_8de4566c906d-------)

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

