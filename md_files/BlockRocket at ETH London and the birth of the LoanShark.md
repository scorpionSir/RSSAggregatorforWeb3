[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/4120897294fb&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![BlockRocket](https://miro.medium.com/fit/c/64/64/1*txNUAyxbcu2dKnsOnhoy_g.png)](https://medium.com/blockrocket?source=post_page
-----4120897294fb--------------------------------)

Published in

[BlockRocket

](https://medium.com/blockrocket?source=post_page-----
4120897294fb--------------------------------)

[![James
Morgan](https://miro.medium.com/fit/c/96/96/1*pU0bCzBaLEnySQq0APCjWg.jpeg)](/@james.morgan?source=post_page
-----4120897294fb--------------------------------)

[James Morgan](/@james.morgan?source=post_page-----
4120897294fb--------------------------------)

Follow

Mar 2, 2020

·

5 min read

# BlockRocket at ETH London and the birth of LoanShark🦈

## LoanShark, a trustless NFT leasing platform

This weekend the team and some of our friends travelled down to [ETH
London](https://ethlondon.com) for what was set to be a fun filled, action
packed and eventful weekend of hacking. Where some of the most exciting _ETH
thinkers_ on planet Earth 🌎 converge to discuss and innovate on web3 and
decentralised economies.

## The team assembled

Myself, [Andy Gray](https://medium.com/u/7e1fed3ccaa1?source=post_page-----
4120897294fb--------------------------------) and [Oliver
Carding](https://medium.com/u/72d04da6ef57?source=post_page-----
4120897294fb--------------------------------) headed down from Manchester,
meeting the other sharks, [@atkinsonholly](http://twitter.com/atkinsonholly)
and Jim, in London that day. The week before the hackathon we had started to
flesh out the idea on a shared doc so we had a good idea of what we wanted to
build, but didn’t really know how to build it yet.

![](https://miro.medium.com/max/1400/1*-cF5XhXhqs7ws3-jW7i71g.png)

Jim, Me, Oliver, Holly and Andy — LoanSharks 🦈

We hacked until 2am on the first night, slept a bit, and then went hard on the
second day. Fuelled by joviality and interactions with the other teams and a
vast quantities of coffee, tea, beer and nuts! 🍺

## What is Loan Shark? 🦈

 **The use-case  
** Imagine getting to the final level of a game and needing a _badass_ weapon.
Not being able to afford it, you should be able to lease the item for a set
period of time and return the item once the boss is slayed. Welcome to pay-as-
you go assets!

Imagine an avid CryptoArt collector who has amassed a collection from the
dopest crypto artists in the space. Then take a metaverse landlord from
Decentraland or CrypotVoxels looking for some killer artworks to use in the
opening of a new plot. Well, now the collector can safely lend their NFT for,
say, 7 days at a set price knowing that at the end, the artwork is safe and
sound back in their wallet.

 **How does it work?  
** Building on the shoulders of giants we leveraged
[OpenZeppelin](https://openzeppelin.com/contracts/)’s solid foundation for
token standards such as ERC-20 and ERC-721, built on top [Sablier’s payment
stream EIP-1620](https://www.sablier.finance) and harnessing DAI as the
payment token of choice.

We have created a proxy contract capable of consuming and holding other NFTs
which is itself an NFT. We then allow a user to deposit the NFT and define the
conditions of the leasing contract.

Anyone willing to take the lease can then pay the fee (by locking up a deposit
amount upfront) which is then streamed back to the lender on a per second
basis.

![](https://miro.medium.com/max/1400/1*OQvXIJd-vP8zRXoXrz4j2g.png)

You are going to need a bigger boat!!

Once finished with the NFT, even if this is early, the borrower can return the
NFT, closing the payment stream and handing back control of the NFT to the
original lender. As we use a stream, the magic is that if the asset is
returned early, _any remaining locked-up deposit amount can be returned to the
borrower_.

If the borrower does not return the NFT, once the payment stream is used up,
the lender can enforce the “return” of their asset. Also, once the stream is
used up, the shark contract reverts all proxied methods, so the NFT returns to
it original owner safe and sound.

## We won 🎉

We didn’t actual finish everything what we wanted to show but we did prove its
possible and got a simple version working (minus a few tiny 🐛).

We managed to land one of the smaller prizes sponsored by
[Pepo](https://medium.com/u/ca3cef8bdb90?source=post_page-----
4120897294fb--------------------------------) — speaking to Kevin he has
impressed by the utility of the application; one of the five categories they
judged on.

Here’s a little tweet storm overview:

The more we think about it the more we like the idea and believe there are
some valid use cases. Others have also reached out about the concept which
seems to have been received really positively in the wider ecosystem.

We’ve been chatting a bit about the future of LoanShark today and we may put a
little Gitcoin grant up to gauge further opinions and see if there is an
appetite for this to be developed into something more solid and production
ready.

## The future

More and more things have come to light now and below are some more ideas
which may be useful for these types of proxy NFT contracts.

  *  **Flash loans __** ⚡ 🦈 — Trustlessly rent a NFT to play a single move on a Gods Unchained game.
  *  **Fake IDs** 📛— NFTs can represent identities, you could lease an identity for single block to gain access to something 🤯
  *  **NFT Brokers** 🏦 — you can use a broker to lend out your NFTs and they can take a % of the stream
  *  **Charge your strean** 🛥 — interest on your stream using charged particples!
  *  **Private leasing contacts 🔍** — using [zkDAI](https://zk.money/zkAsset/zkdai) to allow private leasing contracts
  *  **Multi-token support 💰** — leverage social tokens as payment or even any ERC20 compatible token
  *  **Attention based streams** 🎲— monthly online subscriptions, access tokens can expire when payment streams stop
  *  **Extra Security 🔐** —moving your NTFs from cold storage but using the wrapper so you can use them but always retract them if lost/stolen

## ETH London breakdown

The event itself was well organised and the submissions to the hackathon were
some of the best ideas I’ve seen for a while.

With over 60% of the attendees from the UK, I was pleased to see such as large
Ethereum based community in our home country.
[BlockRocket](https://blockrocket.tech) not being based in London it’s
sometimes hard to judge what’s happening in Ethereum in the UK outside of the
big smoke.

We all came away with a renewed sense of confidence and enthusiasm that the
space is moving in the right direction. Along with finding out about lots of
new DeFi protocols and hearing some of the ETH 2.0 developments which are
being worked on.

![](https://miro.medium.com/max/1400/1*jKvOpaR_RT_XE4IDCrSdyA.png)

## Thats a wrap…

We’re still recovering from the weekend and trying to work out what to do with
the project but watch this space and please reach out if you want carry on
hacking on it or have any questions for the _LoanShark_ team.

Email — [hello@blockrocket.tech](mailto:hello@blockrocket.tech)

Twitter —
[@blockrockettech](https://twitter.com/blockrockettech?source=post_page---------------------------)

Our submission: <https://devpost.com/software/loanshark-g7ti48>

GitHub : <https://github.com/blockrockettech/loan-shark>

\--

\--

\--

## [More from BlockRocket](/blockrocket?source=post_page-----
4120897294fb--------------------------------)

Blockchain and decentralised engineering & consultancy based in Manchester, UK
— we build products and help companies understand blockchain and web3
technologies. We have vast knowledge in tokensiation, governance, smart
contract engineerind, IPFS and crypto www.blockrocket.tech

[Read more from BlockRocket](/blockrocket?source=post_page-----
4120897294fb--------------------------------)

## Recommended from Medium

[[![The JPEG
DAO](https://miro.medium.com/fit/c/40/40/1*PsmlP_FINzppkeeUz0uYyg.png)](/@thejpegdao?source=post_internal_links
---------0----------------------------)

[The JPEG DAO

](/@thejpegdao?source=post_internal_links---------
0----------------------------)

## It’s Time to DAO on Stellar

](/@thejpegdao/its-time-to-dao-on-
stellar-a9ba25cddb2c?source=post_internal_links---------
0----------------------------)

[[![Diamond_Head_Protocol](https://miro.medium.com/fit/c/40/40/1*4KvIu-I3hP4yxZWUwBnnQQ.png)](/@diamondheadprotocol?source=post_internal_links
---------1----------------------------)

[Diamond_Head_Protocol

](/@diamondheadprotocol?source=post_internal_links---------
1----------------------------)

## SpookyPumpkins — New Opensea Collection!

![](https://miro.medium.com/focal/112/112/50/50/1*NO_6FsG_ViqtDGffuAYIHQ.png)](/@diamondheadprotocol/spookypumpkins-
new-opensea-collection-47f29bb6871f?source=post_internal_links---------
1----------------------------)

[[![AldousDAO](https://miro.medium.com/fit/c/40/40/1*ywJ5yUZBwJzpaHb5qRo6uQ.png)](/@aldousdao?source=post_internal_links
---------2----------------------------)

[AldousDAO

](/@aldousdao?source=post_internal_links---------
2----------------------------)

## Brief Introduction to AldousDAO

![](https://miro.medium.com/focal/112/112/50/50/1*icuAEWdQ6XdOmlrVsfq_iQ.jpeg)](/@aldousdao/brief-
introduction-to-aldousdao-e7537efa2479?source=post_internal_links---------
2----------------------------)

[[![Dan
Held](https://miro.medium.com/fit/c/40/40/1*fbiDTdcwFrxt1TbS8AyJog.jpeg)](/@danhedl?source=post_internal_links
---------3----------------------------)

[Dan Held

](/@danhedl?source=post_internal_links---------3----------------------------)

## Bitcoin Minimalism

![](https://miro.medium.com/focal/112/112/50/50/1*zXxyEaTBnVqUEtg_5sHyVA.png)](/@danhedl/bitcoin-
minimalism-b3ed4b88e852?source=post_internal_links---------
3----------------------------)

[[![Sabri
CHERIF](https://miro.medium.com/fit/c/40/40/2*btLSM3Mz3inEoa-N0rHuSw.jpeg)](/@cherif.sabri?source=post_internal_links
---------4----------------------------)

[Sabri CHERIF

](/@cherif.sabri?source=post_internal_links---------
4----------------------------)

## Masternodes as an Investment

![](https://miro.medium.com/focal/112/112/50/50/1*1kfh5ehOtssknPCEZ9aMJw.jpeg)](/@cherif.sabri/masternodes-
as-an-investment-f3802c3fdb28?source=post_internal_links---------
4----------------------------)

[[![Golden Gorilla
Speakeasy](https://miro.medium.com/fit/c/40/40/1*oiJHmYg39a-zZgUQ_z8Xag.jpeg)](/@golden_gorilla?source=post_internal_links
---------5----------------------------)

[Golden Gorilla Speakeasy

](/@golden_gorilla?source=post_internal_links---------
5----------------------------)

## The Golden Gorilla Speakeasy NFT collection launched by serial entrepreneur
Joe J.

![](https://miro.medium.com/focal/112/112/50/50/1*aUZCWDyH-8VHu2uGcU3Xqw.png)](/@golden_gorilla/the-
golden-gorilla-speakeasy-nft-collection-launched-by-serial-entrepreneur-
joe-j-7c3b920703a?source=post_internal_links---------
5----------------------------)

[[![Anthony J
Lynch](https://miro.medium.com/fit/c/40/40/1*Wb9cWBR81nSpNJuqRS3leg.png)](/@anthonyjlynch?source=post_internal_links
---------6----------------------------)

[Anthony J Lynch

](/@anthonyjlynch?source=post_internal_links---------
6----------------------------)

in

[Investor’s Handbook

](https://medium.com/the-investors-handbook?source=post_internal_links
---------6----------------------------)

## How I Make $10,000+ a Month in Passive Crypto Income

![](https://miro.medium.com/focal/112/112/50/50/1*2wGi5OEg96vix0f4ZLhc0w.jpeg)](/the-
investors-handbook/how-i-make-10-000-a-month-in-passive-crypto-
income-474a515a8a9a?source=post_internal_links---------
6----------------------------)

[[![Sam
Maiyaki](https://miro.medium.com/fit/c/40/40/1*uVLoZKr0kMKvwtWptk9xeg.png)](/@sammaiyaki?source=post_internal_links
---------7----------------------------)

[Sam Maiyaki

](/@sammaiyaki?source=post_internal_links---------
7----------------------------)

in

[Game of Life

](https://medium.com/cryptocurrency-hub?source=post_internal_links---------
7----------------------------)

## China’s Crackdown on Bitcoin Hashrate Has Nearly Recovered

![](https://miro.medium.com/focal/112/112/50/50/1*ADwAsCMDbu9RCdbbga3e4w.jpeg)](/cryptocurrency-
hub/chinas-crackdown-on-bitcoin-hashrate-has-nearly-
recovered-7d71fdc47dfa?source=post_internal_links---------
7----------------------------)

[](/?source=post_page-----4120897294fb--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
4120897294fb--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
4120897294fb--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
4120897294fb--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
4120897294fb--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----4120897294fb--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----4120897294fb--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fblockrocket%2Fblockrocket-
at-eth-london-and-the-birth-of-the-loanshark-4120897294fb&source=post_page
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

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F1a825ddddb12&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fblockrocket%2Fblockrocket-
at-eth-london-and-the-birth-of-the-
loanshark-4120897294fb&newsletterV3=6bb848438230&newsletterV3Id=1a825ddddb12&user=James+Morgan&userId=6bb848438230&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Wrapped Companions Development
Team](https://miro.medium.com/fit/c/40/40/1*oMHCP3YB7XISL3d5w5pH_w.png)](/@wrappedcompanions?source=read_next_recirc
---------0---------------------5d2b2477_7eaf_491a_84d3_92dda5724ee1-------)

[Wrapped Companions Development Team

](/@wrappedcompanions?source=read_next_recirc---------0---------------------
5d2b2477_7eaf_491a_84d3_92dda5724ee1-------)

## The Wrapped Companion’s

![](https://miro.medium.com/focal/112/112/50/50/1*RBFk7QLTW-
Siku8dDl-d1g.png)](/@wrappedcompanions/the-wrapped-
companions-4527f8ccd66e?source=read_next_recirc---------0---------------------
5d2b2477_7eaf_491a_84d3_92dda5724ee1-------)

[[![GRIPNR](https://miro.medium.com/fit/c/40/40/1*H-A89oZTzz_PhlWbHZfLYw.jpeg)](/@gripnr?source=read_next_recirc
---------1---------------------5d2b2477_7eaf_491a_84d3_92dda5724ee1-------)

[GRIPNR

](/@gripnr?source=read_next_recirc---------1---------------------
5d2b2477_7eaf_491a_84d3_92dda5724ee1-------)

## GRIPNR Introduces The Glimmering: The World’s only 5e On-chain, Play-to-
progress TTRPG Played with…

![](https://miro.medium.com/focal/112/112/50/50/0*Qj9oDGRmZRaqieOc)](/@gripnr/gripnr-
introduces-the-glimmering-the-worlds-only-5e-on-chain-play-to-progress-ttrpg-
tabletop-9c6d8632d2ef?source=read_next_recirc---------1---------------------
5d2b2477_7eaf_491a_84d3_92dda5724ee1-------)

[[![MouseBelt
Labs](https://miro.medium.com/fit/c/40/40/1*CB3In8Rq39FDHdTHIkX8Cw.png)](/@mousebelt?source=read_next_recirc
---------2---------------------5d2b2477_7eaf_491a_84d3_92dda5724ee1-------)

[MouseBelt Labs

](/@mousebelt?source=read_next_recirc---------2---------------------
5d2b2477_7eaf_491a_84d3_92dda5724ee1-------)

in

[MouseBelt

](https://medium.com/mousebelt?source=read_next_recirc---------2
---------------------5d2b2477_7eaf_491a_84d3_92dda5724ee1-------)

## Ape TV Show Community Update #3

![](https://miro.medium.com/focal/112/112/50/50/1*dOctn_E_M2r-eBoASttUwg.jpeg)](/mousebelt/ape-
tv-show-community-update-3-21a726f2acb6?source=read_next_recirc---------2
---------------------5d2b2477_7eaf_491a_84d3_92dda5724ee1-------)

[[![Theresa
Huang](https://miro.medium.com/fit/c/40/40/0*cnjWfGVN0sZP7FKQ.)](/@theresahuang?source=read_next_recirc
---------3---------------------5d2b2477_7eaf_491a_84d3_92dda5724ee1-------)

[Theresa Huang

](/@theresahuang?source=read_next_recirc---------3---------------------
5d2b2477_7eaf_491a_84d3_92dda5724ee1-------)

in

[Tamago Finance

](https://medium.com/tamago-finance?source=read_next_recirc---------3
---------------------5d2b2477_7eaf_491a_84d3_92dda5724ee1-------)

## Tamago Finance Weekly Update: NFT Luckbox Soft Launch, Current Status, and
Upcoming Plans

![](https://miro.medium.com/focal/112/112/50/50/1*Sjk04fUfPo1R7ldVcGOiIw.jpeg)](/tamago-
finance/tamago-finance-weekly-update-nft-luckbox-soft-launch-current-status-
and-upcoming-plans-3c504e05f1d1?source=read_next_recirc---------3
---------------------5d2b2477_7eaf_491a_84d3_92dda5724ee1-------)

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

