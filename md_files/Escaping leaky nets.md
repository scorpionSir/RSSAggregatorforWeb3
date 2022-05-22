[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/349eec0598c7&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Spatium
Blog](https://miro.medium.com/fit/c/64/64/1*Af7ihrFRI_0VaZWS9EcuKA.png)](https://medium.com/spatium-
blog?source=post_page-----349eec0598c7--------------------------------)

Published in

[Spatium Blog

](https://medium.com/spatium-blog?source=post_page-----
349eec0598c7--------------------------------)

[![Spatium](https://miro.medium.com/fit/c/96/96/1*Af7ihrFRI_0VaZWS9EcuKA.png)](/@spatium_news?source=post_page
-----349eec0598c7--------------------------------)

[Spatium](/@spatium_news?source=post_page-----
349eec0598c7--------------------------------)

Follow

Nov 19, 2019

·

5 min read

# Escaping leaky nets

![](https://miro.medium.com/max/1400/1*6JzoU9WR2IL8zAUjnIXAAw.png)

It hurts whenever some service asks your private data. And in pain is
everyone: the one, who is not concerned about the security, and a cypherpunk,
for whom each such a requirement is like a red flag. The subject becomes even
more poignant when you are asked to provide a photo/video of you. It feels
like you are being robbed, and they are stealing your sense of privacy. But
what’s worse — your data can be passed to third parties, making you feel nude
and defenceless in the world, where walls have eyes.

In this material, we will consider the problems of the biometrical data
storage and explore how they can be solved with the combination of SMPC
technology and the open-source approach.

# Pixel hunting

Digital nets of IT-giants gather more and more data from the user trying to
solve the puzzle of him and use this complete picture “to provide better
service”. They suck out everything from him so he couldn’t hide any secret in
the room. But even if you use the Internet very rarely, you may have heard
that nets of Google, Facebook, and other huge IT corporations are full of
breaches. In the past, they had been not able to provide the necessary level
of security for their clients’ private data, which led to multiple leaks.
Names, bank cards info, emails, phone numbers, passport info, and other
sensitive data was leaked and afterward traded somewhere / uploaded for the
public. And to access it all you need, ironically, just to google it.

Now [they want your biometry in their leaky
nets](https://mashable.com/article/facebook-video-selfies-fight-fake-
accounts/). Of course, “it is the measure of making your account on the
platform more secure”. But how many times has your account on any service been
hacked, comparing to the number of hacks of those companies? The problem is
not in security measures you can employ to secure your account — it is about
the ability of companies to keep your data safe. The subject they fail
abysmally.

And this is not to mention the provision of your data on a commercial basis to
third parties for increasing their marketing campaigns’ effectiveness. Yes, it
is written in “Terms of Service”, but users are forced to accept them —
otherwise, they will lose connection with their friends, relatives and
colleagues.

According to European laws, all services must delete biometric data from their
servers after 30 days since they got them. But with the current power and
authority, which will only increase, — IT-giants are the law. Users must
protect their data themselves, by demanding from those companies the highest
available security level for their data and transparency of its deleting
process. But they can’t hear you from the low. At the same time, many users
don’t care how their private data will be used — they are ready to provide
everything by request.

You can provide your biometry to access the device or social network, but
doing the same for financial services is another matter. Users must be
conscious of this subject and not allow leaky nets to capture their biometry.
Search for alternatives.

# Anonymous shelter

With that said, although biometry is a [good way to provide the highest
security level](http://bit.ly/2pG5dDG), users should look for the best way to
keep such data safe — not to store it. Spatium shares that vision.

The storage of users’ visual data is worth a lot and related to high risks. We
are not interested in building a negative reputation around the service.
That’s why we don’t store biometry at all: data is processed locally on each
party’s device — only hashes are collected.

Biometry is used in conjunction with the [SMPC
technology](http://bit.ly/2BV3Qnz) for secrets generation. Data can be
gathered from the camera on the mobile device with installed Spatium Software
Wallet app or with a fingerprint sensor in Spatium Biometric Wallet. Generated
secrets are encrypted and separated between the funds’ owner and parties he
has chosen and processed independently. None of the parties can get access to
money without funds’ owner consent. Biometric data are deleted after each
interaction with the system and generated from scratch with each new session.
With this approach, the secret is always with the user, copies are not stored
anywhere, and he can access his funds from anywhere securely and conveniently.

Distribution of secrets between parties, chosen by the user, opens a road for
unique features. One of them we previously called **Hybrid**. It can be used
to share the responsibility for the funds’ safety with the entity, able to
provide professional-level security for the secret on its side. As the
security provider has only its own secret with the specific set of
permissions, it can’t perform any action with funds without the user’s
consent. Beyond funds safety, this solution provides users with a convenient
way to manage funds: since a user and the security provider are connected (via
the authorization and the split access to funds), it becomes possible to
implement solutions for instant deposits/withdrawals/trades performing right
from the users’ wallet with on-chain confirmations processed afterward. We
will discuss this feature in-depth later.

Users are free to install the Spatium Software Wallet app on any supported
device (desktop, smartphone, watches). At the same time, to achieve the
highest security level, users can use Spatium Biometric Wallet. It is a
hardware wallet in the credit card shape with a fingerprint sensor. This
solution also doesn’t store any biometrical data, has open software and
provides easy and convenient access to funds.

We believe that the open-source approach is one of the keys to the solution to
problems mentioned above. That is why our repositories will be opened for the
public. Moreover, Spatium solutions already have been completely
[audited](https://drive.google.com/file/d/11EqXjuxY-
FAAcZscdgr4v0c-mYVdcVce/view) and tested by open-source code reviewers as well
as professional security companies.

# Untraceable motion.

Centralized systems have shown that they are not capable of storing users’
private data safely. Such sensitive material as biometry must be managed in
other ways. The combination of biometry with SMPC technology and open-source
approach can lead to the creation of platforms, where the problem of data
leaks will be eliminated, while users will be provided with secure, flexible
and convenient solutions to manage their funds.

In the next article, we will provide more details about how we manage
biometrical data.

 **Spatium** develops solutions to store and manage digital assets powered by
SMPC and biometry. In our technology, the private key is replaced with the
encrypted set of secrets, stored on behalf of funds owner’s devices,
individuals and institutions, chosen by him. Even if some of the parties are
compromised — funds will stay safe. Such an approach dramatically decreases
the risk of theft and provides a previously unavailable level of flexibility
and unique benefits for everyone on the market: no single point of failure,
easy recovery, no need in backups, blockchain agnostic, access levels
differentiation, instant crypto/crypto and crypto/fiat exchange, fully
compliant solution, support of dApps and DeFi services, etc.

\--

\--

\--

## [More from Spatium Blog](/spatium-blog?source=post_page-----
349eec0598c7--------------------------------)

Keyless & genuinely decentralized solution to manage digital assets.

[Read more from Spatium Blog](/spatium-blog?source=post_page-----
349eec0598c7--------------------------------)

## Recommended from Medium

[[![bigb0ss](https://miro.medium.com/fit/c/40/40/2*dQeYrzAgazLb6kr9EDi8HQ.png)](/@bigb0ss?source=post_internal_links
---------0----------------------------)

[bigb0ss

](/@bigb0ss?source=post_internal_links---------0----------------------------)

## [HTB] Postman — Write-up

![](https://miro.medium.com/focal/112/112/50/50/0*FyFfBgtRcrRHE1Va.png)](/@bigb0ss/htb-
postman-write-up-34bc4fe5daa?source=post_internal_links---------
0----------------------------)

[[![Renato
Marinho](https://miro.medium.com/fit/c/40/40/1*JH0JTmpsTGDOH129UenyGg.png)](/@rmarinho?source=post_internal_links
---------1----------------------------)

[Renato Marinho

](/@rmarinho?source=post_internal_links---------1----------------------------)

in

[Morphus Labs

](https://medium.com/morphuslabs?source=post_internal_links---------
1----------------------------)

## Guildma is now using Finger and Signed Binary Proxy Execution to evade
defenses

![](https://miro.medium.com/focal/112/112/50/50/0*SxaRtrYHLu5C2XLe.png)](/morphuslabs/guildma-
is-now-using-finger-and-signed-binary-proxy-execution-to-evade-
defenses-85356e5a0e3?source=post_internal_links---------
1----------------------------)

[[![Richard de
Vries](https://miro.medium.com/fit/c/40/40/1*uK1SRzc37ghaqfgnm6xYcQ.jpeg)](/@vries-
richard-de?source=post_internal_links---------2----------------------------)

[Richard de Vries

](/@vries-richard-de?source=post_internal_links---------
2----------------------------)

in

[Tales from a Security Professional

](https://medium.com/tales-from-a-security-
professional?source=post_internal_links---------2----------------------------)

## Requirements, we always forget the most important one.

![Requirement gathering is not a straight-line
process.](https://miro.medium.com/focal/112/112/50/50/0*XirPhVCBFmU3Xcy8.jpg)](/tales-
from-a-security-professional/requirements-we-always-forget-the-most-important-
one-9e4fdd92796e?source=post_internal_links---------
2----------------------------)

[[![Lakshay
baheti](https://miro.medium.com/fit/c/40/40/1*nJgZ-83xLRBvslzQjjObPA.jpeg)](/@lakshaybaheti1?source=post_internal_links
---------3----------------------------)

[Lakshay baheti

](/@lakshaybaheti1?source=post_internal_links---------
3----------------------------)

## Capture the Flag — CTF

![](https://miro.medium.com/focal/112/112/50/50/1*Jr2126l9qHp3PPsn_CBZbA.jpeg)](/@lakshaybaheti1/capture-
the-flag-ctf-50267bae4559?source=post_internal_links---------
3----------------------------)

[[![Fetchr](https://miro.medium.com/fit/c/40/40/1*87tFXrvGhXpdf_lcxP9kMA.png)](/@fetchr?source=post_internal_links
---------4----------------------------)

[Fetchr

](/@fetchr?source=post_internal_links---------4----------------------------)

## How to Safeguard Your Online Business from Cyber Attacks

![](https://miro.medium.com/focal/112/112/50/50/1*2Fh0jOCtKuCaUuUjB3yD8g.jpeg)](/@fetchr/how-
to-safeguard-your-online-business-from-cyber-
attacks-3a0c9c603939?source=post_internal_links---------
4----------------------------)

[[![aNumak &
Company](https://miro.medium.com/fit/c/40/40/1*7noTroH1BEO9q9roy0jLHQ.jpeg)](/@anumakandcompany?source=post_internal_links
---------5----------------------------)

[aNumak & Company

](/@anumakandcompany?source=post_internal_links---------
5----------------------------)

## 2022 In The Digital World

![](https://miro.medium.com/focal/112/112/50/50/0*2jL3gYLaUhXh5EzH)](/@anumakandcompany/2022-in-
the-digital-world-80ba639281b7?source=post_internal_links---------
5----------------------------)

[[![HOPPY](https://miro.medium.com/fit/c/40/40/1*bWxjHTqFa_coxmtaft1Ojw.png)](/@hoppymeme?source=post_internal_links
---------6----------------------------)

[HOPPY

](/@hoppymeme?source=post_internal_links---------
6----------------------------)

## ACY Finance: Wining against the Bots

![](https://miro.medium.com/focal/112/112/50/50/1*9U-TekV1bbNaO_JXxrdV-w.png)](/@hoppymeme/acy-
finance-wining-against-the-bots-7bea99e4c851?source=post_internal_links
---------6----------------------------)

[[![Koltonbowen](https://miro.medium.com/fit/c/40/40/1*UPLn-
LHfQCj3-zuJXl09vQ.jpeg)](/@koltonbowen?source=post_internal_links---------
7----------------------------)

[Koltonbowen

](/@koltonbowen?source=post_internal_links---------
7----------------------------)

## Vulnhub: Potato

![](https://miro.medium.com/focal/112/112/50/50/0*h7MF_291tRtN38Lr.png)](/@koltonbowen/vulnhub-
potato-2e0f9ae6a65?source=post_internal_links---------
7----------------------------)

[](/?source=post_page-----349eec0598c7--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
349eec0598c7--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
349eec0598c7--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
349eec0598c7--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
349eec0598c7--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----349eec0598c7--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----349eec0598c7--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fspatium-
blog%2Fescaping-leaky-nets-349eec0598c7&source=post_page
--------------------------nav_reg-----------)

[![Spatium](https://miro.medium.com/fit/c/176/176/1*Af7ihrFRI_0VaZWS9EcuKA.png)](/@spatium_news)

[

## Spatium

](/@spatium_news)

51 Followers

Spatium — true, decentralized, keyless crypto storage solution, bringing
complex cryptographic technologies from security experts to blockchain
enthusiasts.

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F69561b2e7b9e&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fspatium-
blog%2Fescaping-leaky-
nets-349eec0598c7&newsletterV3=eb4a6667c312&newsletterV3Id=69561b2e7b9e&user=Spatium&userId=eb4a6667c312&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Biimuel](https://miro.medium.com/fit/c/40/40/1*iqWqktO1y8BgW5B6Nh1u9Q.jpeg)](/@biimuel699?source=read_next_recirc
---------0---------------------f57d58de_f774_4efa_b371_e57cb8e3b0bd-------)

[Biimuel

](/@biimuel699?source=read_next_recirc---------0---------------------
f57d58de_f774_4efa_b371_e57cb8e3b0bd-------)

## PlutoNetwork to work alongside Pandora.finance

![](https://miro.medium.com/focal/112/112/50/50/1*GlJMMPYCdEg1UM_5vSgTeA.jpeg)](/@biimuel699/plutos-
network-to-work-alongside-pandora-finance-81d3210f3156?source=read_next_recirc
---------0---------------------f57d58de_f774_4efa_b371_e57cb8e3b0bd-------)

[[![Eight13](https://miro.medium.com/fit/c/40/40/1*dmbNkD5D-u45r44go_cf0g.png)](/@admin_10467?source=read_next_recirc
---------1---------------------f57d58de_f774_4efa_b371_e57cb8e3b0bd-------)

[Eight13

](/@admin_10467?source=read_next_recirc---------1---------------------
f57d58de_f774_4efa_b371_e57cb8e3b0bd-------)

## Eight13

![](https://miro.medium.com/focal/112/112/50/50/1*jcXo5aBcbPexh0NcGhTxuQ.jpeg)](/@admin_10467/eight13-9caffc6ea329?source=read_next_recirc
---------1---------------------f57d58de_f774_4efa_b371_e57cb8e3b0bd-------)

[[![Binary Gold
Finance](https://miro.medium.com/fit/c/40/40/1*3336ASuaAj64Xy1nQ8v-ow.png)](/@bgold-
io?source=read_next_recirc---------2---------------------
f57d58de_f774_4efa_b371_e57cb8e3b0bd-------)

[Binary Gold Finance

](/@bgold-io?source=read_next_recirc---------2---------------------
f57d58de_f774_4efa_b371_e57cb8e3b0bd-------)

## BGOLD UPDATES

![](https://miro.medium.com/focal/112/112/50/50/1*0_KTI512QofPp-
neSslp5A.png)](/@bgold-io/bgold-updates-7106f1faf9e7?source=read_next_recirc
---------2---------------------f57d58de_f774_4efa_b371_e57cb8e3b0bd-------)

[[![Fantomville](https://miro.medium.com/fit/c/40/40/1*UtvC6UTKDqS_F26UG6DFWw.png)](/@fantomville?source=read_next_recirc
---------3---------------------f57d58de_f774_4efa_b371_e57cb8e3b0bd-------)

[Fantomville

](/@fantomville?source=read_next_recirc---------3---------------------
f57d58de_f774_4efa_b371_e57cb8e3b0bd-------)

## Fantomville Update #1

](/@fantomville/fantomville-update-1-36501ddc7133?source=read_next_recirc
---------3---------------------f57d58de_f774_4efa_b371_e57cb8e3b0bd-------)

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

