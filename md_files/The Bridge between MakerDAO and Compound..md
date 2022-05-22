[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/eb14b2dd0fe7&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Instadapp](https://miro.medium.com/fit/c/64/64/1*Jdx_PVb-M-
wDOIBWGFLXhg.png)](https://medium.com/instadapp?source=post_page-----
eb14b2dd0fe7--------------------------------)

Published in

[Instadapp

](https://medium.com/instadapp?source=post_page-----
eb14b2dd0fe7--------------------------------)

[![Samyak
Jain](https://miro.medium.com/fit/c/96/96/1*PuXaGt3FxuA8ZK0R3jOlag.jpeg)](/@smykjain?source=post_page
-----eb14b2dd0fe7--------------------------------)

[Samyak Jain](/@smykjain?source=post_page-----
eb14b2dd0fe7--------------------------------)

Follow

Jun 10, 2019

·

3 min read

# The Bridge between MakerDAO and Compound.

![](https://miro.medium.com/max/1400/1*DCwmmETMO21P2soOj3k7xQ.png)

With the rise in Maker’s stability fees, we’ve seen CDP users shifting to
different lending protocols like Compound, Nuo, dydx, Dharma, etc. This showed
us how the change in one good DeFi protocol can affect every other protocol.

When the stability fees raised I didn’t pay my DAI debt because I don’t have
any DAI to pay. So the other option was to shift to other protocol but then I
realized that I’ve to pay my Maker’s debt first in order to take my collateral
out but again I don’t have DAI. So I came to a conclusion — “Let’s leave it
how it is”. Two days later, I read another proposal on MakerDAO that the
stability fee is being increased by an additional 2%. Now that’s enough, I
decided to shift to Compound. **I took some collateral out - > Deposited it on
Compound -> took DAI debt from Compound -> paid the DAI debt on Maker. __**
Repeated this process 3 times and bam! I was finally using the Compound. Easy!
Huh! It only took just 12 transactions. So now that I shifted what if MakerDAO
decreased the stability fees and then I want to shift back?!

> At the time of writing this article interest of DAI on different DeFi
> protocols: 16.5% on Maker, 12.35% on Compound, 10.48% on Nuo, and 14.25% on
> dYdX

There’s a lot of difference between different protocols and it’s because
there’s no connectivity between protocols.

# Decentralized Bridge between DeFi protocols

Borrowing is the heart of the banking industry for decades and it’s just
started on blockchain about a year ago. Still, a long way to go. We will see a
good surge of protocols supporting crypto-backed borrowings in the coming
years. Starting with making a bridge between **MakerDAO and Compound** , ****
our aim is to create efficiency in the whole DeFi industry.

## How does it work under the hood?

  1. User will call a function on their smart contract wallet.
  2. Contract wallet will transfer the ownership of CDP to bridge contract.
  3. “Bridging Contract” will pay the debt for the CDP. (Bridge contract will always have around 100K DAI balance to cover user’s debt)
  4. Bridge contract will take out the ETH collateral from Maker’s contract and lend them up in compound’s contract. (contract will receive CETH tokens)
  5. Bridge contract will transfer CETH to user’s contract wallet.
  6. Contract wallet will take equivalent DAI debt from the compound and send it to Bridge contract.

And vice-versa goes when the user has to switch from Compound to Maker.

![](https://miro.medium.com/max/1400/1*YFrnK20Splab9SfSqFQBTw.gif)

## What are the benefits it’s providing to the whole DeFi ecosystem?

  1. For users — Best rates on lending, borrowing and margin trading.
  2. For Maker — Solves the DAI peg problem.
  3. For Compound — Great use case and shows how it’s helping to keep DeFi stable.

A win-win situation for everyone!!!

At [InstaDApp](https://instadapp.io), we are committed to growing
Decentralised Finance ecosystem and building innovative products around
protocols to bring the mainstream adoption of the overall **#DEFI** industry.
If you have any questions, we can get in touch on
[Twitter](https://twitter.com/smykjain). Would love to have your feedback &
suggestions.

\--

\--

\--

## [More from Instadapp](/instadapp?source=post_page-----
eb14b2dd0fe7--------------------------------)

Powerful DeFi Management Platform

[Read more from Instadapp](/instadapp?source=post_page-----
eb14b2dd0fe7--------------------------------)

[](/?source=post_page-----eb14b2dd0fe7--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
eb14b2dd0fe7--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
eb14b2dd0fe7--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
eb14b2dd0fe7--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
eb14b2dd0fe7--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----eb14b2dd0fe7--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----eb14b2dd0fe7--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Finstadapp%2Fbridge-
protocols-eb14b2dd0fe7&source=post_page--------------------------
nav_reg-----------)

[![Samyak
Jain](https://miro.medium.com/fit/c/176/176/1*PuXaGt3FxuA8ZK0R3jOlag.jpeg)](/@smykjain)

[

## Samyak Jain

](/@smykjain)

135 Followers

Co-founder InstaDApp, MakerScan Alerts and Buidling Easwap. ETHSF and ETHINDIA
finalists

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F9f947916d203&operation=register&redirect=https%3A%2F%2Fmedium.com%2Finstadapp%2Fbridge-
protocols-
eb14b2dd0fe7&newsletterV3=3e560f79a82b&newsletterV3Id=9f947916d203&user=Samyak+Jain&userId=3e560f79a82b&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Daolectic
Research](https://miro.medium.com/fit/c/40/40/1*O0_BPMejPW1BMm6JcTfoXA.png)](/@daolecticresearch?source=read_next_recirc
---------0---------------------448d626b_46a2_4203_aff4_1f6af65fa668-------)

[Daolectic Research

](/@daolecticresearch?source=read_next_recirc---------0---------------------
448d626b_46a2_4203_aff4_1f6af65fa668-------)

in

[Coinmonks

](https://medium.com/coinmonks?source=read_next_recirc---------0
---------------------448d626b_46a2_4203_aff4_1f6af65fa668-------)

## $AVAX | Even the largest Avalanche is triggered by small things..!

![](https://miro.medium.com/focal/112/112/50/50/1*Tml2dI80p4A1WyyxDzsCQg.jpeg)](/coinmonks/avax-
even-the-largest-avalanche-is-triggered-by-small-
things-3ea5a94b7525?source=read_next_recirc---------0---------------------
448d626b_46a2_4203_aff4_1f6af65fa668-------)

[[![Tilmar
Goos](https://miro.medium.com/fit/c/40/40/2*xmVskBAji6nBIl5-lt_oZg.png)](/@tilmarwgoos?source=read_next_recirc
---------1---------------------448d626b_46a2_4203_aff4_1f6af65fa668-------)

[Tilmar Goos

](/@tilmarwgoos?source=read_next_recirc---------1---------------------
448d626b_46a2_4203_aff4_1f6af65fa668-------)

## Interview with former Legal Counsel Cardano Foundation Tilmar Goos on DeFi,
Yield Farming, Tax and…

![](https://miro.medium.com/focal/112/112/50/50/0*yrkwtSOl7bG2Dho-.jpeg)](/@tilmarwgoos/interview-
with-former-legal-counsel-cardano-foundation-tilmar-goos-on-defi-yield-
farming-tax-and-36ae963ec141?source=read_next_recirc---------1
---------------------448d626b_46a2_4203_aff4_1f6af65fa668-------)

[[![Mitchell
Opatowsky](https://miro.medium.com/fit/c/40/40/1*O_3Gw6uTRyZvOLhLXL7_HQ@2x.jpeg)](/@mopa?source=read_next_recirc
---------2---------------------448d626b_46a2_4203_aff4_1f6af65fa668-------)

[Mitchell Opatowsky

](/@mopa?source=read_next_recirc---------2---------------------
448d626b_46a2_4203_aff4_1f6af65fa668-------)

in

[Dexible

](https://medium.com/dexible?source=read_next_recirc---------2
---------------------448d626b_46a2_4203_aff4_1f6af65fa668-------)

## 3 Ways to Tackle DeFi Volatility like a Pro

![](https://miro.medium.com/focal/112/112/50/50/1*cETI-5erGhNd5uAV8BK2MQ@2x.png)](/dexible/3-ways-
to-tackle-defi-volatility-like-a-pro-2b266b9a19f4?source=read_next_recirc
---------2---------------------448d626b_46a2_4203_aff4_1f6af65fa668-------)

[[![Gcex](https://miro.medium.com/fit/c/40/40/1*PNkSPddwRB9i382wkbMn4A.jpeg)](/@GCexlt?source=read_next_recirc
---------3---------------------448d626b_46a2_4203_aff4_1f6af65fa668-------)

[Gcex

](/@GCexlt?source=read_next_recirc---------3---------------------
448d626b_46a2_4203_aff4_1f6af65fa668-------)

## GC Exchange — Bridging the Gap between Islamic Finance and Modern Capital
Markets

![](https://miro.medium.com/focal/112/112/50/50/1*_mJb6lu_RydPcoB03noYUg.png)](/@GCexlt/gc-
exchange-bridging-the-gap-between-islamic-finance-and-modern-capital-
markets-6bfdb4bf9e2d?source=read_next_recirc---------3---------------------
448d626b_46a2_4203_aff4_1f6af65fa668-------)

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

