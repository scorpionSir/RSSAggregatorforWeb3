[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/e1653e4e7336&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![BlockRocket](https://miro.medium.com/fit/c/64/64/1*txNUAyxbcu2dKnsOnhoy_g.png)](https://medium.com/blockrocket?source=post_page
-----e1653e4e7336--------------------------------)

Published in

[BlockRocket

](https://medium.com/blockrocket?source=post_page-----
e1653e4e7336--------------------------------)

[![James
Morgan](https://miro.medium.com/fit/c/96/96/1*pU0bCzBaLEnySQq0APCjWg.jpeg)](/@james.morgan?source=post_page
-----e1653e4e7336--------------------------------)

[James Morgan](/@james.morgan?source=post_page-----
e1653e4e7336--------------------------------)

Follow

Apr 23, 2020

·

5 min read

# Powering MetaFactory 🤖 auctions using sealed bids

## Private auctions delivered by Web3, PGP cryptography and stable coins 🔥

![](https://miro.medium.com/max/1400/1*a46q0PwGzVU9WQ0viOE5Hw.png)

<https://metafactory.ai/>

We’ve recently been helping build out the first _genesis_ iteration of the
[MetaFactory](https://metafactory.ai), working with the team behind the
project to explore new and interesting auction mechanics.

[MetaFactory](https://metafactory.ai) are pushing the envelope by exploring
new and novel ways to engage in commerce and how to build engaged and loyal
communities. The ultimate goal being to foster an engaged, incentivised and
happy community which will produce apparel and other items in the metaverse
and _real_ world.

We have so far explored several concepts which we may be included in the
future iterations of the project including sealed bids, vickery auctions, plus
curved and bonded sales.

Additionally we explored awesome concepts like [charged
particles](https://charged-particles.eth.link/) as well as using NFT’s in
novel and interesting ways in conjunction with other crypto economic and
governance models. Team [BlockRocket](https://blockrocket.tech/) and
[MetaFactory](https://metafactory.ai) come from a blockchain heavy/native
backgrounds and our focus is always on leveraging the power of decentralised
networks with cryptocurrency focused technologies then adding a big sprinkle
of innovation on top!

## What are the requirements?

In the alpha version, we have built a solution which will hopefully provide a
simple and pain free way for users to make blind bids to compete in an auction
for a limited run of bomber jackets that come with membership rights and a
non-fungible token…

At the very core of the problem are several requirements which need to be met,
below we listed the high level ones out:

  * As a **_platform_** , we do not want the user to use anything other than a web3 wallet and to own the chosen currency for the auction.
  * As a **_platform_** , we want to make it very hard or impossible to read other peoples bids.
  * As an **_auctioneer_** , I need to be able to read all blind bids committed.
  * As an **_auctioneer_** , I need to be able to prove the authenticity of a blind bid.
  * As an **_auctioneer_** , I need to be able to result the auction, drawing the funds from the winning bidders.
  * As a **_user_** , I do not want other participants to see what I bid.
  * As a **_user_** , I do not want to overcommit my funds as a consequence of obscuring my true bid.
  * As a **_user_** , I want to be easily see what I have previously bid.

The interesting point here is that there are many ways to solve this common
problem but often they have trade-offs, especially in user experience.

For example, we initially considered running a blind auction where users over
commit funds. In this example, a user may bid $50 but escrows $250 in the
contract to obscure the true bid. However this pattern creates a number of UX
challenges and seems overly zealous, not to mention stopping anyone who only
has $50 for participating.

## What did we build?

So, adhering to the assumed guidelines above we amassed our weapons of choice
and started to build, our toolset comprising of:

  * A [smart contract](https://etherscan.io/address/0x9d2454de493141CcCD06Eba254e95A81D294598C) on Ethereum to store all registered bids
  * [PGP](https://en.wikipedia.org/wiki/Pretty_Good_Privacy) (via [openpgp-js](https://github.com/openpgpjs/openpgpjs)) to encrypt the bid so only [MetaFactory](https://metafactory.ai) and the user can view it
  * Web3 to facilitate cryptographic data signatures to verify and validate interactions
  * [DAI](https://makerdao.com/en/) stable coin cryptocurrency as the payment vehicle
  * [IPFS](https://ipfs.io/) public storage to store the encrypted bundles and not pollute on chain block space

The general flow can be seen in the diagram below:

![](https://miro.medium.com/max/1324/1*9Cg103KMqeKFsqq_7MD-Ig.png)

First, a user decides on the amount they are willing to pay as well as some
sizing and contact information. They then sign the data using their web3
wallet, allowing us to verify the data comes from the account who holds those
private keys.

Next, we then encrypt the data using [MetaFactory](https://metafactory.ai)’s
public PGP key, this allows only [MetaFactory](https://metafactory.ai) to
decrypt the bids. Next we push the PGP payload to IPFS turning a large chunky
PGP object into a small 46 character IPFS hash. Finally the user submits a
transaction to store their signed, encrypted bid on-chain and into a smart
contract.

When going through this process no funds are taken! We do check allowances of
the payment token, DAI in this case, asking them to approve the registry
contract which will be responsible for resulting the auction and pulling all
the funds together at that point in the flow.

Lastly the registry smart contract only allows new bids between two dates,
enforcing the time limited nature of this auction.

To result the auction we first extract all bids from IPFS, decrypt them,
verify the bidder and the signed payload match, sort them by highest price and
date entered. We then check the winners still have the funds to fulfil the bid
placed, discounting invalid bids and winners which no longer have enough
funds. Once sorted and validated we result the auction by drawing the funds
from the winning users and place the funds in the smart contract. The result
is ordered list of the winning (and unsuccessful) bids and who placed them.

## Thats a wrap

What we hope we achieved is a slightly novel method which means all users can
take part and no user has to over commit funds up front, also hoping to meet
the criteria mentioned above. This is a tricky conundrum but we feel this
approach is one of the cleanest and fairest while maintaining crucial
integrity.

The future of [MetaFactory](https://metafactory.ai) is looking bright and
fruitful with so many innovative and community driven and focused ventures on
the horizon.

Check out [MetaFactory](https://metafactory.ai) and get involved in first
[limited edition sale](https://metafactory.ai) for a chance at winning very
special unique item 🌶

Remember to come join their [Discord](https://discord.gg/U3wdre) server to
scope out what they are up to and how the experiment is progressing.

Reached out to us at [BlockRocket](http://blockrocket.tech) if you want help
to realise your product vision and start building the future of commerce and
community with web3.

Website 👉 🌐 — [www.blockrocket.tech](https://www.blockrocket.tech/)

Email 👉 ✉️ — [hello@blockrocket.tech](mailto:hello@blockrocket.tech)

Tweet us 👉🐦—
[@blockrockettech](https://twitter.com/blockrockettech?source=post_page---------------------------)

Hope this all made sense, James 👊

![](https://miro.medium.com/max/1400/0*h8OmFW6Zmhfbsgfn.png)

\--

\--

\--

## [More from BlockRocket](/blockrocket?source=post_page-----
e1653e4e7336--------------------------------)

Blockchain and decentralised engineering & consultancy based in Manchester, UK
— we build products and help companies understand blockchain and web3
technologies. We have vast knowledge in tokensiation, governance, smart
contract engineerind, IPFS and crypto www.blockrocket.tech

[Read more from BlockRocket](/blockrocket?source=post_page-----
e1653e4e7336--------------------------------)

## Recommended from Medium

[[![Cryptoforever14](https://miro.medium.com/fit/c/40/40/1*LNhq48QoHOKjdIo7jChRpg@2x.jpeg)](/@cryptoforever14?source=post_internal_links
---------0----------------------------)

[Cryptoforever14

](/@cryptoforever14?source=post_internal_links---------
0----------------------------)

## SHIBA COMPETITION

](/@cryptoforever14/shiba-competition-52db967958d9?source=post_internal_links
---------0----------------------------)

[[![BRUGU SOFTWARE
SOLUTIONS](https://miro.medium.com/fit/c/40/40/2*yHqafKRhYN87yPpib-0E3A.png)](/@brugusoftwaresolutions?source=post_internal_links
---------1----------------------------)

[BRUGU SOFTWARE SOLUTIONS

](/@brugusoftwaresolutions?source=post_internal_links---------
1----------------------------)

## Build and Launch your Own NFT Marketplace -Whitelabel NFT Marketplace
Development

![](https://miro.medium.com/focal/112/112/50/50/0*2D1w7SVT9oHlFWpe)](/@brugusoftwaresolutions/build-
and-launch-your-own-nft-marketplace-whitelabel-nft-marketplace-
development-a2d1c122b8d6?source=post_internal_links---------
1----------------------------)

[[![Ehsan Yazdanparast](https://miro.medium.com/fit/c/40/40/1*I2ZEGKeALjFpCg-
cTNKyYg@2x.jpeg)](/@ehsan-yazdanparast?source=post_internal_links---------
2----------------------------)

[Ehsan Yazdanparast

](/@ehsan-yazdanparast?source=post_internal_links---------
2----------------------------)

in

[Coinmonks

](https://medium.com/coinmonks?source=post_internal_links---------
2----------------------------)

## Cryptocurrency Market Updates (31 March 2022)

![Top Performer Cryptocurrencies \(31 Mar
2022\)](https://miro.medium.com/focal/112/112/50/50/1*e45uTRjJZ5JlFpBWYLWJLg.jpeg)](/coinmonks/cryptocurrency-
market-updates-31-march-2022-c987fb04e8ff?source=post_internal_links---------
2----------------------------)

[[![ALPEX](https://miro.medium.com/fit/c/40/40/1*Dvp5YXT43NTWXt7tnWC6zQ.jpeg)](/@alpex?source=post_internal_links
---------3----------------------------)

[ALPEX

](/@alpex?source=post_internal_links---------3----------------------------)

in

[ALPEX

](https://medium.com/alpex?source=post_internal_links---------
3----------------------------)

## ALPEX MARKETS WRAP (30/4/2021–17:00PM Fri

![](https://miro.medium.com/focal/112/112/50/50/1*aSGEKC6LsULcNzgBFR-
UWA.png)](/alpex/alpex-markets-wrap-30-4-2021-17-00pm-
fri-128b19f50158?source=post_internal_links---------
3----------------------------)

[[![Porn
Bit](https://miro.medium.com/fit/c/40/40/1*HZOuq5v6Djm75SnGDrg5RA.png)](/@PornBit?source=post_internal_links
---------4----------------------------)

[Porn Bit

](/@PornBit?source=post_internal_links---------4----------------------------)

## PornBit NFT Drop

![](https://miro.medium.com/focal/112/112/50/50/1*H_-
yemsINgWgIk85VWU5cg.jpeg)](/@PornBit/pornbit-nft-drop-
cc2ea3b1ebc7?source=post_internal_links---------4----------------------------)

[[![APY
Vision](https://miro.medium.com/fit/c/40/40/1*b2ai54UOpGz9XHbrRHiyXw.png)](/@apyvision?source=post_internal_links
---------5----------------------------)

[APY Vision

](/@apyvision?source=post_internal_links---------
5----------------------------)

in

[APY Vision

](https://medium.com/apy-vision?source=post_internal_links---------
5----------------------------)

## APY.Vision 2020.52 Update

![](https://miro.medium.com/focal/112/112/50/50/1*Rek8DCF-F4TLxprhdVSAYQ.png)](/apy-
vision/apy-vision-2020-52-update-593ea2f925d0?source=post_internal_links
---------5----------------------------)

[[![bubblo](https://miro.medium.com/fit/c/40/40/0*YvcZaay3K7Gg7b_i.jpg)](/@BubbloApp?source=post_internal_links
---------6----------------------------)

[bubblo

](/@BubbloApp?source=post_internal_links---------
6----------------------------)

## New Kid on the Blockchain: Bubblo Brings Big Data Home

![](https://miro.medium.com/focal/112/112/50/50/0*8C6WJ_sn5Hmhj4WS)](/@BubbloApp/new-
kid-on-the-blockchain-bubblo-brings-big-data-
home-54b9f44a5515?source=post_internal_links---------
6----------------------------)

[[![Victor
Bonhomme](https://miro.medium.com/fit/c/40/40/2*Y1cGFgW86J1CPSowffQ9DQ.jpeg)](/@vb_90215?source=post_internal_links
---------7----------------------------)

[Victor Bonhomme

](/@vb_90215?source=post_internal_links---------7----------------------------)

in

[iExec

](https://medium.com/iex-ec?source=post_internal_links---------
7----------------------------)

## RLC Token Economics — iExec

![](https://miro.medium.com/focal/112/112/50/50/1*_mS74pkby7FbNkBjbv-2VQ.png)](/iex-
ec/rlc-token-economics-iexec-34757f4885c2?source=post_internal_links---------
7----------------------------)

[](/?source=post_page-----e1653e4e7336--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
e1653e4e7336--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
e1653e4e7336--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
e1653e4e7336--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
e1653e4e7336--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----e1653e4e7336--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----e1653e4e7336--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fblockrocket%2Fpowering-
metafactory-auctions-using-sealed-bids-e1653e4e7336&source=post_page
--------------------------nav_reg-----------)

[![James
Morgan](https://miro.medium.com/fit/c/176/176/1*pU0bCzBaLEnySQq0APCjWg.jpeg)](/@james.morgan)

[

## James Morgan

](/@james.morgan)

488 Followers

Founder of @knownorigin_io @BlockRocketTech @blockchain_manc — NFT nerd,
crypto enthusiast, lover of music, humanist, mostly found hacking web3

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F1a825ddddb12&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fblockrocket%2Fpowering-
metafactory-auctions-using-sealed-
bids-e1653e4e7336&newsletterV3=6bb848438230&newsletterV3Id=1a825ddddb12&user=James+Morgan&userId=6bb848438230&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Colin
Adams](https://miro.medium.com/fit/c/40/40/1*RbKmHEMsKslJnuorr6Dlfw.jpeg)](/@Colin_Adams15z?source=read_next_recirc
---------0---------------------7ab7c367_3d4c_4f5f_8a71_b594c8079d3e-------)

[Colin Adams

](/@Colin_Adams15z?source=read_next_recirc---------0---------------------
7ab7c367_3d4c_4f5f_8a71_b594c8079d3e-------)

in

[ChainSafe

](https://medium.com/chainsafe-systems?source=read_next_recirc---------0
---------------------7ab7c367_3d4c_4f5f_8a71_b594c8079d3e-------)

## ChainSafe Gaming SDK Spotlight: Arsenal Fabwelt

![](https://miro.medium.com/focal/112/112/50/50/0*UyUZtXA2ap51wC9D.jpeg)](/chainsafe-
systems/chainsafe-gaming-sdk-spotlight-arsenal-
fabwelt-1bcbbf364c59?source=read_next_recirc---------0---------------------
7ab7c367_3d4c_4f5f_8a71_b594c8079d3e-------)

[[![Jwbenhayon](https://miro.medium.com/fit/c/40/40/0*3pd4O5yyPSdxMpA0)](/@jwbenhayon?source=read_next_recirc
---------1---------------------7ab7c367_3d4c_4f5f_8a71_b594c8079d3e-------)

[Jwbenhayon

](/@jwbenhayon?source=read_next_recirc---------1---------------------
7ab7c367_3d4c_4f5f_8a71_b594c8079d3e-------)

## A Modern ERC721 Implementation Guide: Using solmate, dynamic burning via
signatures, ERC721 vs…

![](https://miro.medium.com/focal/112/112/50/50/1*EsP4qWloLpiReiVWlEJcQQ.jpeg)](/@jwbenhayon/a-modern-
erc721-implementation-guide-using-solmate-dynamic-burning-via-signatures-
erc721-vs-88f5696462d6?source=read_next_recirc---------1---------------------
7ab7c367_3d4c_4f5f_8a71_b594c8079d3e-------)

[[![Steve
Simkins](https://miro.medium.com/fit/c/40/40/1*HtOl7he4IgmldKJfbovgVg.png)](/@stevedsimkins?source=read_next_recirc
---------2---------------------7ab7c367_3d4c_4f5f_8a71_b594c8079d3e-------)

[Steve Simkins

](/@stevedsimkins?source=read_next_recirc---------2---------------------
7ab7c367_3d4c_4f5f_8a71_b594c8079d3e-------)

in

[Pinata

](https://medium.com/pinata?source=read_next_recirc---------2
---------------------7ab7c367_3d4c_4f5f_8a71_b594c8079d3e-------)

## How to Offset Your NFT Project Carbon Emissions with Aerial

![](https://miro.medium.com/focal/112/112/50/50/1*KxoVDEZFH3mJrlfeguMYjg.jpeg)](/pinata/how-
to-offset-your-nft-project-carbon-emissions-with-
aerial-b5b4b95faba0?source=read_next_recirc---------2---------------------
7ab7c367_3d4c_4f5f_8a71_b594c8079d3e-------)

[[![Bryan
T.](https://miro.medium.com/fit/c/40/40/1*KloKBJpNHGPZ7tdewBjZAA.png)](/@hatruongv?source=read_next_recirc
---------3---------------------7ab7c367_3d4c_4f5f_8a71_b594c8079d3e-------)

[Bryan T.

](/@hatruongv?source=read_next_recirc---------3---------------------
7ab7c367_3d4c_4f5f_8a71_b594c8079d3e-------)

in

[Digital Unicorn Insights

](https://medium.com/digital-unicorn?source=read_next_recirc---------3
---------------------7ab7c367_3d4c_4f5f_8a71_b594c8079d3e-------)

## What Is a Smart Contract Security Audit?

![](https://miro.medium.com/focal/112/112/50/50/1*Q9LZvXUP2L8FHEK12EyWGw.png)](/digital-
unicorn/what-is-a-smart-contract-security-
audit-8f783f4a7155?source=read_next_recirc---------3---------------------
7ab7c367_3d4c_4f5f_8a71_b594c8079d3e-------)

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

