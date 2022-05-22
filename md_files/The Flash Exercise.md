[](https://medium.com/)

[Get unlimited access](https://medium.com/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/859336761a88&~feature=LoOpenInAppButton&~channel=ShowPostUnderUser&~stage=mobileNavBar)

[](https://medium.com/)

[Home](https://medium.com/)

[Notifications](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Primitive](https://miro.medium.com/fit/c/96/96/1*IJFmMdSn_ypT6FdYvG-f0g.png)](/?source=post_page
-----859336761a88--------------------------------)

[Primitive](/?source=post_page-----
859336761a88--------------------------------)

Follow

May 25, 2020

·

3 min read

# The Flash Exercise

![](https://miro.medium.com/max/1076/1*NV0NnYcZVNRpi-QCzbjoBA.jpeg)

Zeus

# tl:dr: Exercising an option will pay you first.

For the past few weeks we have been testing the contracts and optimizing their
gas usage. In the process of this, we noticed that by reorganizing the logic
in the exercise function, we can enable flash exercises.

Vanilla options are often never exercised because it _uses_ the option. The
option had extrinsic time value, which is effectively burned when it’s used.
It’s often the case options are _sold_ to close, rather than exercised to
close.

Why build in flash exercises then? There is a case where an option is
exercised: when the option expires _in the money_. At this point in time, the
option’s value is _almost_ 100% of its _intrinsic_ value, the difference
between the execution price of buying the underlying tokens and the market
value of the underlying tokens. Therefore, a flash exercise will give us the
underlying token _first_ which we can then sell and use the proceeds to pay
the _strike price_ of the option. The flash exerciser then walks away with the
profit without using any capital.

Another benefit to flash exercises is that they implicitly enable flash loans
to be taken out on the underlying tokens. These underlying tokens MUST remain
in the option contract so option holders can exercise. Underlying tokens sit
in the contract as dead assets, but flash loans enable them to be utilized.
These flash loans work now because the flash exercise will check the net
output of underlying tokens, and if it is zero it means the underlying tokens
were returned. If the net output of underlying tokens is greater than zero,
the contract will require the payment, the _strike price_.

This is a feature that has been added to the final design specification of the
vanilla option primitive. The ability to flash exercise these options
introduces new ways to manage continuous option positions. The flash exercise
can be abstracted away so that a user can exercise an option and receive just
the net profit. Going a step further, rolling an option position could be done
using the proceeds of flash exercised options. Therefore, exiting an old
position and entering a new position requires zero upfront capital, as long as
the profit from the old pays for the new.

# Developer Update

Primitive has been working on the final specification of the protocol. We are
working towards a model of permissionless options which can be created by
anyone.

The code is being prepared and scoped for an audit to be done. The audit will
give us insight into the security of the protocol, but it will not be a final
measure which determines a V1 release. Ultimately, the first official launch
of the protocol will come when the Primitive team determines the smart
contracts have been thoroughly tested and reviewed.

In the meantime, we are working on solving two problems: (1) allowing anyone
to create an option on a token and (2) an option market that uses a pooled
liquidity model as a medium of exchange.

The next immediate steps will be deploying the protocol to a testnet like
Kovan, which will be done in June.

What options do you want to create?

# Community

##  **Our community’s home is the discord here** :

<https://discord.gg/rzRwJ4K>

## Follow our Twitter:

[

## Primitive

### The latest Tweets from Primitive (@PrimitiveFi). Permissionless options
protocol. Built on #Ethereum. Powered by Prime…

twitter.com

](https://twitter.com/PrimitiveFi)

## Our Github Repository is Open:

<https://github.com/primitivefinance/primitive-contracts>

\--

\--

\--

## [More from Primitive](/?source=post_page-----
859336761a88--------------------------------)

Follow

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fef69815f4399&operation=register&redirect=https%3A%2F%2Fprimitivefinance.medium.com%2Fthe-
flash-
exercise-859336761a88&newsletterV3=60c08806472a&newsletterV3Id=ef69815f4399&user=Primitive&userId=60c08806472a&source=-----859336761a88
---------------------subscribe_user-----------)

Permissionless options protocol. Built on Ethereum.

Love podcasts or audiobooks? Learn on the go with our new app.

[Try
Knowable](https://knowable.fyi/?utm_source=medium&utm_medium=referral&utm_campaign=medium-
post-footer&source=post_page-----859336761a88--------------------------------)

## Recommended from Medium

[[![Georgiana
Ghiciuc](https://miro.medium.com/fit/c/40/40/1*MqHeCZXLiPTXz_Hsc7EYLQ.png)](https://medium.com/@GGhiciuc?source=post_internal_links
---------0----------------------------)

[Georgiana Ghiciuc

](https://medium.com/@GGhiciuc?source=post_internal_links---------
0----------------------------)

## Follow-up on “The United Nations of Crypto” aka Web3 Summit in Berlin | Our
Favorite Talks

![](https://miro.medium.com/focal/112/112/50/50/1*g-701WkV0Qe73Ovkd7hDYQ.jpeg)](https://medium.com/@GGhiciuc/follow-
up-on-the-united-nations-of-crypto-aka-web3-summit-in-berlin-our-favorite-
talks-441a129a76ad?source=post_internal_links---------
0----------------------------)

[[![Miguel
Palhas](https://miro.medium.com/fit/c/40/40/1*iGHNqvTeI5Ra96KlpjacYw.jpeg)](https://medium.com/@naps62?source=post_internal_links
---------1----------------------------)

[Miguel Palhas

](https://medium.com/@naps62?source=post_internal_links---------
1----------------------------)

in

[UTRUST

](https://medium.com/utrust?source=post_internal_links---------
1----------------------------)

## Smart Contracts: A Beginner’s Guide

![](https://miro.medium.com/focal/112/112/50/50/1*c9NsjjfgHQ4qzXlh7ZxO6Q.png)](https://medium.com/@naps62/smart-
contracts-a-beginners-guide-d354e487b577?source=post_internal_links---------
1----------------------------)

[[![GRAFT
Blockchain](https://miro.medium.com/fit/c/40/40/1*9-oUTze4EUwWUcI3E7lQyg.png)](https://medium.com/@graftnetwork?source=post_internal_links
---------2----------------------------)

[GRAFT Blockchain

](https://medium.com/@graftnetwork?source=post_internal_links---------
2----------------------------)

## GRAFT DEVELOPMENT STATUS UPDATE MAY 2018

![](https://miro.medium.com/focal/112/112/50/50/0*BHTcJyRJIerFWbld.png)](https://medium.com/@graftnetwork/graft-
development-status-update-may-2018-ec50e011a6db?source=post_internal_links
---------2----------------------------)

[[![faith
samuel](https://miro.medium.com/fit/c/40/40/0*HSQz_y4inQfZ56SZ)](https://medium.com/@faithsamuel46?source=post_internal_links
---------3----------------------------)

[faith samuel

](https://medium.com/@faithsamuel46?source=post_internal_links---------
3----------------------------)

in

[Ayagigs

](https://medium.com/myayacash?source=post_internal_links---------
3----------------------------)

## Solid World Partners With Aya

![](https://miro.medium.com/focal/112/112/50/50/1*Jd_O1dBvGW9sU40hoIpHxg.png)](https://medium.com/@faithsamuel46/solid-
world-partners-with-aya-66e2b12f2c7a?source=post_internal_links---------
3----------------------------)

[[![Vinay
Kanamarlapudi](https://miro.medium.com/fit/c/40/40/1*wwH2Zm8SEpWiKfn7Pr4MeQ.jpeg)](https://vinaykanamarlapudi.medium.com/?source=post_internal_links
---------4----------------------------)

[Vinay Kanamarlapudi

](https://vinaykanamarlapudi.medium.com/?source=post_internal_links---------
4----------------------------)

## What is Web3.0 — A Deep dive, beginner level explanation of Web3.0 and
Dapps

![](https://miro.medium.com/focal/112/112/50/50/1*P09iz6pcW6YWuTJdq9zUAQ.png)](https://vinaykanamarlapudi.medium.com/what-
is-web3-0-a-deep-dive-beginner-level-explanation-of-web3-0-and-
dapps-2f372efd69ef?source=post_internal_links---------
4----------------------------)

[[![Gelek pro](https://miro.medium.com/fit/c/40/40/1*G5ygoHI8NLZ8AqA_t-
ggYQ.jpeg)](https://medium.com/@gelekpro3?source=post_internal_links---------
5----------------------------)

[Gelek pro

](https://medium.com/@gelekpro3?source=post_internal_links---------
5----------------------------)

## Services from Authpaper Limited Authpaper

![](https://miro.medium.com/focal/112/112/50/50/1*rSMWca9Oicw76JasW9sOog.png)](https://medium.com/@gelekpro3/services-
from-authpaper-limited-authpaper-4033c31d1aea?source=post_internal_links
---------5----------------------------)

[[![Empower Team](https://miro.medium.com/fit/c/40/40/1*FLNxIn-
pDXhRQ4_F_5FyVA.png)](https://hi-85666.medium.com/?source=post_internal_links
---------6----------------------------)

[Empower Team

](https://hi-85666.medium.com/?source=post_internal_links---------
6----------------------------)

in

[Empower

](https://medium.com/empowerplastic?source=post_internal_links---------
6----------------------------)

## Norwegian recyclers using blockchain to reach a circular economy

![](https://miro.medium.com/focal/112/112/50/50/0*1XC-
ahNOqBiCfjdl.png)](https://hi-85666.medium.com/norwegian-recyclers-using-
blockchain-to-reach-a-circular-economy-cc2aa77e7c73?source=post_internal_links
---------6----------------------------)

[[![Valoce](https://miro.medium.com/fit/c/40/40/1*dmbNkD5D-u45r44go_cf0g.png)](https://medium.com/@valoce9485?source=post_internal_links
---------7----------------------------)

[Valoce

](https://medium.com/@valoce9485?source=post_internal_links---------
7----------------------------)

## BEP 721 token: The Binance Smart Chain upheld NFT

](https://medium.com/@valoce9485/bep-721-token-the-binance-smart-chain-upheld-
nft-4e4ab34b281c?source=post_internal_links---------
7----------------------------)

[](https://medium.com/?source=post_page-----
859336761a88--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
859336761a88--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
859336761a88--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
859336761a88--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
859336761a88--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----859336761a88--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----859336761a88--------------------------------)

[Get
started](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fprimitivefinance.medium.com%2Fthe-
flash-exercise-859336761a88&source=post_page--------------------------
nav_reg-----------)

[![Primitive](https://miro.medium.com/fit/c/176/176/1*IJFmMdSn_ypT6FdYvG-f0g.png)](/)

[

## Primitive

](/)

135 Followers

Permissionless options protocol. Built on Ethereum.

Follow

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fef69815f4399&operation=register&redirect=https%3A%2F%2Fprimitivefinance.medium.com%2Fthe-
flash-
exercise-859336761a88&newsletterV3=60c08806472a&newsletterV3Id=ef69815f4399&user=Primitive&userId=60c08806472a&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Simpler
Everyday](https://miro.medium.com/fit/c/40/40/1*4z2X2lilhxZ7q6MK22dITw.png)](https://simplereveryday.medium.com/?source=read_next_recirc
---------0---------------------d213fb7e_cb9c_4ed8_a2e2_ab130627009b-------)

[Simpler Everyday

](https://simplereveryday.medium.com/?source=read_next_recirc---------0
---------------------d213fb7e_cb9c_4ed8_a2e2_ab130627009b-------)

in

[Coinmonks

](https://medium.com/coinmonks?source=read_next_recirc---------0
---------------------d213fb7e_cb9c_4ed8_a2e2_ab130627009b-------)

## Nani Defi?

![](https://miro.medium.com/focal/112/112/50/50/0*l2Bxb9JfmNbLd-
oX.jpg)](https://simplereveryday.medium.com/nani-
defi-b79fd294ddc?source=read_next_recirc---------0---------------------
d213fb7e_cb9c_4ed8_a2e2_ab130627009b-------)

[[![Crypto
Cutie](https://miro.medium.com/fit/c/40/40/1*cS7gDAaNTAxmmfX5_yC6mg.jpeg)](https://cryptocutie.medium.com/?source=read_next_recirc
---------1---------------------d213fb7e_cb9c_4ed8_a2e2_ab130627009b-------)

[Crypto Cutie

](https://cryptocutie.medium.com/?source=read_next_recirc---------1
---------------------d213fb7e_cb9c_4ed8_a2e2_ab130627009b-------)

## Short or Delta Neutral, that is the question

![](https://miro.medium.com/focal/112/112/50/50/1*Ym5D7NFXJZYzhVYDlmvhGg.png)](https://cryptocutie.medium.com/short-
or-delta-neutral-that-is-the-question-37889733b0e?source=read_next_recirc
---------1---------------------d213fb7e_cb9c_4ed8_a2e2_ab130627009b-------)

[[![EksiMaya](https://miro.medium.com/fit/c/40/40/1*_pvGFN9p6jt7Zfc7CVLSBQ.png)](https://medium.com/@eksimaya?source=read_next_recirc
---------2---------------------d213fb7e_cb9c_4ed8_a2e2_ab130627009b-------)

[EksiMaya

](https://medium.com/@eksimaya?source=read_next_recirc---------2
---------------------d213fb7e_cb9c_4ed8_a2e2_ab130627009b-------)

## ProtoFi Long Term Investment

![](https://miro.medium.com/focal/112/112/50/50/1*nHi4681pfEAkKA9WW_i6Cw.png)](https://medium.com/@eksimaya/protofi-
long-term-investment-88480914c00f?source=read_next_recirc---------2
---------------------d213fb7e_cb9c_4ed8_a2e2_ab130627009b-------)

[[![Vulture
Finance](https://miro.medium.com/fit/c/40/40/1*sAKtU493hL2UoLIMu1H_gA.jpeg)](https://medium.com/@vulturefi?source=read_next_recirc
---------3---------------------d213fb7e_cb9c_4ed8_a2e2_ab130627009b-------)

[Vulture Finance

](https://medium.com/@vulturefi?source=read_next_recirc---------3
---------------------d213fb7e_cb9c_4ed8_a2e2_ab130627009b-------)

## How Vulture manages Asset Liability

![](https://miro.medium.com/focal/112/112/50/50/1*4kn-
iZalljU4kxHRyX1gPA.jpeg)](https://medium.com/@vulturefi/how-vulture-manages-
asset-liability-d900841d7911?source=read_next_recirc---------3
---------------------d213fb7e_cb9c_4ed8_a2e2_ab130627009b-------)

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

