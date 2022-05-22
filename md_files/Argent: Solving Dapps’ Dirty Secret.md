[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/3ddb4f741a6&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Argent](https://miro.medium.com/fit/c/64/64/1*VmJdPIIMxo_J-
EVVvtmt_Q.png)](https://medium.com/argenthq?source=post_page-----
3ddb4f741a6--------------------------------)

Published in

[Argent

](https://medium.com/argenthq?source=post_page-----
3ddb4f741a6--------------------------------)

[![Matthew
Wright](https://miro.medium.com/fit/c/96/96/2*ERO4eG8KsAnsZzf7ZVSmzA.png)](/@matthew_argent?source=post_page
-----3ddb4f741a6--------------------------------)

[Matthew Wright](/@matthew_argent?source=post_page-----
3ddb4f741a6--------------------------------)

Follow

Mar 24, 2020

·

3 min read

# Argent: Solving Dapps’ Dirty Secret

## How to not sacrifice your security when using Dapps

![](https://miro.medium.com/max/1400/1*xE_FbX_zzb-aWNBXq_KZYw.png)

[CoinDesk recently drew attention to this
problem](https://www.coindesk.com/long-festering-defi-dapp-bug-still-not-
fixed-by-industry) — but they weren’t aware it has been solved

Dapps have a dirty secret: they can often access an unlimited number of tokens
from your wallet. Sounds crazy, but that’s the reality behind the innocuous
sounding ERC20 Approve method.

Here’s how we solved it.

## First, how could a Dapp access all my tokens?

Traditionally, when your wallet interacts with a Dapp it uses the ERC20
approve method. This gives the Dapp permission to transfer tokens from your
wallet, up to a ceiling.

Contrary to the CoinDesk headline, it’s actually not a bug. Asking for such a
high amount of tokens was a deliberate design choice: one that prioritized
convenience over security. This is because it sought to minimize how many
transactions you have to make with the Dapp.

![](https://miro.medium.com/max/1400/1*L9mHKTkTyAe4B4uijxSs1g.png)

Here’s how accessing Dapps used to look. Not so welcoming. Or safe. (Image
credit: Saturn Network)

The problem, aside from poor user experience, is how insecure it is.

Dapps would usually ask you to approve an insanely high number, e.g. 10⁵⁰.
Pretty much unlimited.

You could be wiped out if there was a bug or malicious actor.

 **What was done about it?**

Some people argued that you could inspect a Dapp’s smart contracts to check it
wouldn’t steal all your tokens. But this is complex, ignores the risk that
developers can upgrade the smart contracts, and doesn’t protect the majority
of people who don’t know how to read through a smart contract.

#  **How we solved it**

We’ve solved this through two separate approaches to accessing Dapps.

## a) **Integrating** Dapps natively in Argent

We’ve natively integrated a handful of core DeFi Dapps (Maker, Compound and
Kyber) — to help you borrow, earn and exchange.

We integrated these at smart contract level and ensured that only the amount
requested is approved. And this all happens automatically under the hood —
it’s invisible to Argent wallet owners.

Safer, and much easier too.

## b) Connecting to desktop Dapps

As well as our native Dapp integrations you can also use Argent to access
desktop Dapps. We do this through WalletConnect (a standard for connecting
mobile wallets to desktop Dapps).

We’ve customized our WalletConnect integration to make it even safer. There
are three main security features, as [we wrote in this post](/argenthq/faster-
cheaper-and-safer-dapp-access-70057611ed46).

 **1\. Only approve what you want to spend**

Argent detects if a Dapp is requesting a large amount and encourages you to
only approve the amount you want to spend.

(We also call it ‘pre-authorise’, not approve, to clarify the process).

 **2\. Protected by your daily transaction limit**

With Argent you choose a daily transaction limit. Any transactions that exceed
this limit are blocked for 24 hours. You can unblock them with your Guardians
(your hardware wallets or friends you trust).

This limit also applies to the amount you pre-authorise a Dapp to take. This
means there’s no risk of anyone draining your wallet.

 **3\. Easily revoke a Dapp’s access to a token**

Changed your mind about a Dapp? Revoke their access with a tap.

# What’s next for Argent?

We want to make Dapps accessible to everyone. Stay tuned for some big DeFi
news very soon!

## [Download on iOS](https://argent.link/getargt?utm_content=erc20approve) |
[Download on Android](https://argent.link/getargt?utm_content=erc20approve)|
[Follow us on Twitter](https://twitter.com/argentHQ)

\--

\--

\--

## [More from Argent](/argenthq?source=post_page-----
3ddb4f741a6--------------------------------)

Our blog has moved to: www.argent.xyz/blog

[Read more from Argent](/argenthq?source=post_page-----
3ddb4f741a6--------------------------------)

## Recommended from Medium

[[![Cryp†Øfͥบsͣiͫon🆇rp](https://miro.medium.com/fit/c/40/40/0*OIcH5EGA5y16Ults)](/@cryptofusionxrp?source=post_internal_links
---------0----------------------------)

[Cryp†Øfͥบsͣiͫon🆇rp

](/@cryptofusionxrp?source=post_internal_links---------
0----------------------------)

## XRP price rebounds after worst month since June 2021 &#8212;&#160;major
recovery ahead?

![](https://miro.medium.com/focal/112/112/50/50/0*Q3C_IUFcOGAPjwE7.jpg)](/@cryptofusionxrp/xrp-
price-rebounds-after-worst-month-since-june-2021-8212-160-major-recovery-
ahead-49c32e74ce0e?source=post_internal_links---------
0----------------------------)

[[![yAxis
Project](https://miro.medium.com/fit/c/40/40/1*tpXRgC2LwCjhAeYB2bgMZg.png)](/@yaxis?source=post_internal_links
---------1----------------------------)

[yAxis Project

](/@yaxis?source=post_internal_links---------1----------------------------)

## The MetaVault

![](https://miro.medium.com/focal/112/112/50/50/1*yYJPkWVW-0oy5PSt-
wqBYA.png)](/@yaxis/the-metavault-1d8c8774c81f?source=post_internal_links
---------1----------------------------)

[[![Ugly Old
Goat](https://miro.medium.com/fit/c/40/40/1*rT2XsVfnFDO4_ROCEwxwfw.jpeg)](/@homeytel?source=post_internal_links
---------2----------------------------)

[Ugly Old Goat

](/@homeytel?source=post_internal_links---------2----------------------------)

## GO WITH THE FLOW . . . trade the ebb . . . steady as she goes

![](https://miro.medium.com/focal/112/112/50/50/1*pT9dZzU9755BiYKchF3MhA.png)](/@homeytel/go-
with-the-flow-trade-the-ebb-steady-as-she-
goes-88f41ed28680?source=post_internal_links---------
2----------------------------)

[[![Ersin
Akinci](https://miro.medium.com/fit/c/40/40/1*vuxGIvisVqWuf238jCWFWw.jpeg)](/@ersin-
akinci?source=post_internal_links---------3----------------------------)

[Ersin Akinci

](/@ersin-akinci?source=post_internal_links---------
3----------------------------)

in

[The Startup

](https://medium.com/swlh?source=post_internal_links---------
3----------------------------)

## I’m tired of people misunderstanding Bitcoin

![](https://miro.medium.com/focal/112/112/50/50/1*h5EnKu1EDHzXZUNTc4AwDA.jpeg)](/swlh/im-
tired-of-people-misunderstanding-
bitcoin-7eb299a65193?source=post_internal_links---------
3----------------------------)

[[![Marvellous Ugochi
Kalu](https://miro.medium.com/fit/c/40/40/1*aQ1EYYUsCSKql3drsh2g8g.jpeg)](/@Kalumarvellous99?source=post_internal_links
---------4----------------------------)

[Marvellous Ugochi Kalu

](/@Kalumarvellous99?source=post_internal_links---------
4----------------------------)

in

[Coinmonks

](https://medium.com/coinmonks?source=post_internal_links---------
4----------------------------)

## Experience Unified Margin Trading With Bit.com

![](https://miro.medium.com/focal/112/112/50/50/0*55a4XY2lhc-
FMXAY)](/coinmonks/experience-unified-margin-trading-with-bit-
com-8b1676e48697?source=post_internal_links---------
4----------------------------)

[[![Royale](https://miro.medium.com/fit/c/40/40/1*28O7Zw24bBLGU-
pFgMoxfw.jpeg)](/@officialroyale?source=post_internal_links---------
5----------------------------)

[Royale

](/@officialroyale?source=post_internal_links---------
5----------------------------)

in

[OfficialRoyale

](https://medium.com/officialroyale?source=post_internal_links---------
5----------------------------)

## Royale Finance & DeXe Trading Competition

![](https://miro.medium.com/focal/112/112/50/50/1*wE3PH51L4-n0d9OfMBnRMw.png)](/officialroyale/royale-
finance-dexe-trading-competition-14e8e8bc0f4d?source=post_internal_links
---------5----------------------------)

[[![Asadulmollah](https://miro.medium.com/fit/c/40/40/1*yZr1dn5VxIMGrB2yfD0QbA.jpeg)](/@Asadulmollah?source=post_internal_links
---------6----------------------------)

[Asadulmollah

](/@Asadulmollah?source=post_internal_links---------
6----------------------------)

## #MBZ #MovieBizCoin #ERC #Crypto #Giveaway #aladdincenter #bountyThis
project is unique in its…

](/@Asadulmollah/mbz-moviebizcoin-erc-crypto-giveaway-aladdincenter-
bountythis-project-is-unique-in-its-3cad15022552?source=post_internal_links
---------6----------------------------)

[[![Iron
Finance](https://miro.medium.com/fit/c/40/40/1*Fs57gPAzXy3eIYG_aobIOg.png)](/@ironfinance?source=post_internal_links
---------7----------------------------)

[Iron Finance

](/@ironfinance?source=post_internal_links---------
7----------------------------)

## The Foundry: Introduction

![](https://miro.medium.com/focal/112/112/50/50/1*kHGsmHTT9RbxH834Urm2-w.png)](/@ironfinance/the-
foundry-introduction-87aa4a497174?source=post_internal_links---------
7----------------------------)

[](/?source=post_page-----3ddb4f741a6--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
3ddb4f741a6--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
3ddb4f741a6--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
3ddb4f741a6--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
3ddb4f741a6--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----3ddb4f741a6--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----3ddb4f741a6--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fargenthq%2Fargent-
solving-dapps-dirty-secret-3ddb4f741a6&source=post_page
--------------------------nav_reg-----------)

[![Matthew
Wright](https://miro.medium.com/fit/c/176/176/2*ERO4eG8KsAnsZzf7ZVSmzA.png)](/@matthew_argent)

[

## Matthew Wright

](/@matthew_argent)

268 Followers

Argent

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fbc0ecaada35e&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fargenthq%2Fargent-
solving-dapps-dirty-
secret-3ddb4f741a6&newsletterV3=d2ca4399e666&newsletterV3Id=bc0ecaada35e&user=Matthew+Wright&userId=d2ca4399e666&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Diana
Berryman](https://miro.medium.com/fit/c/40/40/1*mD_Uk8zRoCULPnS_CIzRoQ.jpeg)](/@soc1albutterfly?source=read_next_recirc
---------0---------------------105d231c_9f41_41e9_ab10_572568c2675f-------)

[Diana Berryman

](/@soc1albutterfly?source=read_next_recirc---------0---------------------
105d231c_9f41_41e9_ab10_572568c2675f-------)

in

[The Cake.chat

](https://medium.com/the-cake-chat?source=read_next_recirc---------0
---------------------105d231c_9f41_41e9_ab10_572568c2675f-------)

## The Cake is officially a DAO

![](https://miro.medium.com/focal/112/112/50/50/1*ZRDOujusDcYwfM_LK7mL7g.png)](/the-
cake-chat/the-cake-is-officially-a-dao-bd3abb11bd53?source=read_next_recirc
---------0---------------------105d231c_9f41_41e9_ab10_572568c2675f-------)

[[![Joe
Walker](https://miro.medium.com/fit/c/40/40/1*NoKl8fHJhdTOSO7WjwrkeQ.jpeg)](/@IAmJoeWalker?source=read_next_recirc
---------1---------------------105d231c_9f41_41e9_ab10_572568c2675f-------)

[Joe Walker

](/@IAmJoeWalker?source=read_next_recirc---------1---------------------
105d231c_9f41_41e9_ab10_572568c2675f-------)

## KOIN Tokenomics part 2: how to assess real value based on mana

![](https://miro.medium.com/focal/112/112/50/50/1*2alrltyxtOA-W456eZDL8g.png)](/@IAmJoeWalker/koin-
tokenomics-part-2-how-to-assess-real-value-based-on-
mana-f69007f7e617?source=read_next_recirc---------1---------------------
105d231c_9f41_41e9_ab10_572568c2675f-------)

[[![uNBees](https://miro.medium.com/fit/c/40/40/1*TmPyATneZUroP3LSj7XQKA.png)](/@unbees?source=read_next_recirc
---------2---------------------105d231c_9f41_41e9_ab10_572568c2675f-------)

[uNBees

](/@unbees?source=read_next_recirc---------2---------------------
105d231c_9f41_41e9_ab10_572568c2675f-------)

in

[Coinmonks

](https://medium.com/coinmonks?source=read_next_recirc---------2
---------------------105d231c_9f41_41e9_ab10_572568c2675f-------)

## DAO’s — The Human Side of Crypto

![](https://miro.medium.com/focal/112/112/50/50/1*9EIJlwcH39rR_vhZ0Dc1ng.jpeg)](/coinmonks/daos-
the-human-side-of-crypto-521b18190c15?source=read_next_recirc---------2
---------------------105d231c_9f41_41e9_ab10_572568c2675f-------)

[[![Annee
Park](https://miro.medium.com/fit/c/40/40/1*Bc5MRNc8VNknxBnXvp-n3g.png)](/@f3annee?source=read_next_recirc
---------3---------------------105d231c_9f41_41e9_ab10_572568c2675f-------)

[Annee Park

](/@f3annee?source=read_next_recirc---------3---------------------
105d231c_9f41_41e9_ab10_572568c2675f-------)

in

[f3vc

](https://medium.com/f3vc?source=read_next_recirc---------3
---------------------105d231c_9f41_41e9_ab10_572568c2675f-------)

## wtf is DeFi?

![](https://miro.medium.com/focal/112/112/50/50/1*PEYEEB59DycuEGwPU4pW1g.png)](/f3vc/wtf-
is-defi-cf2dec07546e?source=read_next_recirc---------3---------------------
105d231c_9f41_41e9_ab10_572568c2675f-------)

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

