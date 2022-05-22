[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/9acebd4ff6ef&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Horizon
Games](https://miro.medium.com/fit/c/64/64/1*ikCUFjCj4oHVLxbkYNU06g.png)](https://medium.com/horizongames?source=post_page
-----9acebd4ff6ef--------------------------------)

Published in

[Horizon Games

](https://medium.com/horizongames?source=post_page-----
9acebd4ff6ef--------------------------------)

[![Philippe
Castonguay](https://miro.medium.com/fit/c/96/96/1*KccjAOL2T6YnKj3pHX3L7A.jpeg)](/@PhABC?source=post_page
-----9acebd4ff6ef--------------------------------)

[Philippe Castonguay](/@PhABC?source=post_page-----
9acebd4ff6ef--------------------------------)

Follow

Sep 14, 2018

·

9 min read

# Here Be Dragons : Going Beyond ERC-20 and ERC-721 To Reduce Gas Cost by ~80%

![](https://miro.medium.com/max/1400/1*91Wk1EAp8KOc7qtIRSf3AQ.jpeg)

 **TL;DR :** We’ve designed and implemented a token contract which allows us
to transfer bundles of different types of tokens for 80% to 90% less gas than
ERC-20 and ERC-721. This is accomplished by “packing” different token balances
together, saving a substantial amount of storage space on the blockchain. One
trade-off is that the maximum user balance for each token type is lower,
however this can be adjusted to be made acceptable for many projects. Multi-
class token contracts are particularly interesting for the gaming world, where
transferring bundles of items (sets, decks, etc.) is common. —
[PhABCD](https://twitter.com/PhABCD) @ Twitter

# Ethereum Token Standards

In the last six months, we have seen an explosion of new token standards in
the Ethereum ecosystem, which is a great thing. In the end, “adoption is key”
as [Matt Lockyer](https://medium.com/u/9cb5f31cb9fa?source=post_page-----
9acebd4ff6ef--------------------------------) said in his [blog post on token
standards](/@mattdlockyer/the-tokens-of-babel-token-standards-on-the-
blockchain-745c87c640c1). Just as with websites or cryptocurrencies, over
time, the ones that are truly important will be adopted while insignificant
ones will be ignored. This acceleration in Ethereum token design proposals can
be observed in the [exhaustive list of Ethereum Token Standard
proposals](https://github.com/PhABC/ethereum-token-standards-list) I recently
created. It was therefore not surprising for us to realize the token interface
we were working on for our first game at [Horizon Games](/horizongames/a-new-
dimension-of-gaming-728d7ae301c5), SkyWeaver, was being contemplated by others
as well. Before going into the details that lead to our more efficient token
contract design, let’s review the two most popular token standards today and
what they are good for: ERC-20 and ERC-721. For those familiar with these,
feel free to skip the next two sections.

# ERC-20 Standard: Fungible Tokens

When we think of money, we usually think of all dollars as identical. You
don’t open your wallet (if you still have one) and choose which $20 bill you
want to give the merchant. To both of you, all valid $20 bills are the same.
This is generally speaking what we mean by “fungible”, where each object or
element is interchangeable with others of the same “type”. In the realm of
cryptocurrencies, Ether and Bitcoin are generally said to be fungible, where 1
Ether is equal to any other 1 Ether. When people create tokens on the Ethereum
network, via token sales for example, they usually create fungible tokens and
usually these tokens are said to comply with the [ERC-20 Token
Standard](https://www.investopedia.com/news/what-erc20-and-what-does-it-mean-
ethereum/).

![](https://miro.medium.com/max/1400/1*WLkrkM8c6qtLjIJpMJ_sOg.png)

Standardization is important for developers as it makes our life much easier.
Imagine if each laptop had a different keyboard layout and you couldn’t change
it. It would be quite painful indeed and hence why standardizing some
interface (e.g. keyboard) is important for user experience. Currently, with
ERC-20 token standard, if Bob wants to transfer 100
[ZRX](https://0xproject.com/) or [ANT](https://aragon.one/) tokens to Alice
(both ERC-20 compliant), he simply needs to execute the`transfer(Alice, 100)`
function in both cases. If these tokens _did not_ use the same standard, then
perhaps Bob would need to call `transfer(Alice, 100)` in the case of
transferring ZRXs, but `sendTokens(Bob, Alice, 100)` in the case of
transferring ANTs. This would be kind of confusing, since Bob and all the
other developers would always need to check how each token works and write
code for each different implementation. Standards are important as they
simplify life for everyone and allow people to easily integrate in their own
system tools developed by others. On the other hand, a given standard might
not satisfy the needs of all applications, hence these several new token
standards being proposed.

#  **ERC-721 Standard: Non-Fungible Tokens**

Fungibility is not always desired, however. Each house and car is unique and
therefore should be considered “non-fungible”. Similarly in the digital world,
it is possible to have some digital objects that are unique, hence the
recently proposed [ERC-721 Non Fungible Tokens (NFT)
Standard](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-721.md). NFTs
were popularized by [CryptoKitties](https://www.cryptokitties.co/), where each
cat is unique and therefore non-fungible. Although most projects currently
using or intending to use non-fungible tokens are video games, it is important
to note that gaming is not the only area where NFTs can be useful. You can
read more about the possible applications of NFTs in this [non-technical blog
post](https://fulldecent.blogspot.com/2018/06/nontechnical-what-is-
erc-721.html) by [William
Entriken](https://medium.com/u/6c5e37620483?source=post_page-----
9acebd4ff6ef--------------------------------).

![](https://miro.medium.com/max/1400/1*7-GUJ7hgovnkWbIEgXHMUg.png)

NFT functionality is slightly different than fungible tokens, necessitating a
different standard: ERC-721. Indeed, instead of sending X number of tokens,
you need to specify _which_ token you want to send. In the case of ERC-721
tokens, when Bob calls the function `transfer(Alice, 100)`, Bob is _not_
sending 100 tokens, but sending the token `#100`. The actual implementation of
the transfer function is slightly different in the new ERC-721 standard, but
the essence is the same.

Contracts following the ERC-20 standard keep track of a single class of
divisible token and contracts following the ERC-721 standard keep track of
many indivisible tokens. However, it can be useful to keep track of many
different types of fungible and non-fungible tokens within the same contract,
both for simplicity and efficiency, as explained in the next section.

# Multi-Class Token Contracts

At [horizongames.net](https://horizongames.net/), we make games for players
who want to have fun without spending much (or at all), and so minimizing on-
chain costs is critical. We therefore wanted to have a single contract that
keeps track of all our tokens so that transferring many different tokens
simultaneously would be efficient. In the case of our flagship trading card
game [SkyWeaver](https://skyweaver.net/), users might want to sell their decks
on a market, buy bundles of cards or claim a many rewards at once. All of
these scenarios involve multiple token types (e.g. cards) being transferred.
This means that whether we choose our virtual goods to be fungible or not, we
would still need a slightly different interface than ERC-20 and ERC-721.
Currently, we found five proposed token standards that had similar intentions

  * [ERC-998: Composable Non-Fungible Token Standard](https://eips.ethereum.org/EIPS/eip-998)
  * [ERC-888: MultiDimensional Token Standard](https://github.com/ethereum/EIPs/pull/888)
  * [ERC-1155: Multi Token Standard](https://github.com/ethereum/EIPs/issues/1155)
  * [ERC-1178: Multi-Class Token Standard](https://eips.ethereum.org/EIPS/eip-1178)
  * [ERC-1203: Multi-Class Token Standard](https://eips.ethereum.org/EIPS/eip-1203)

The latter four standards (888, 1155, 1178, 1203) are practically identical in
their intentions and reflect most our implementation. For simplicity, we will
refer to these proposed token standards as Multi-Class Token (MCT) contracts.
The four MCT proposals can be summarized as having a mapping variable such
that`balances[Bob][tokenA]` is the number of `tokenA` Bob currently owns. With
a standard
[ERC-20](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-20.md) token
contract A, `balances[BobAddress]` returns Bob’s `tokenA` balance since there
is only one token class tracked on this contract. With a standard
[ERC-721](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-721.md)
contract B, `balances[BobAddress]` would return a list of all NFT tokens Bob
currently owns on contract B. MCTs are obviously incompatible with both ERC-20
and ERC-721 standards giving the additional balance mapping. **Yet, despite
this lack of compatibility, we argue that this new token interface can lead to
significant efficiency gains under the right circumstances.** Indeed, we will
show that we can transfer a large amount of tokens from different classes more
efficiently by “packing” the balance of various tokens together.

For the sake of simplicity, in the rest of this post, we will assume that all
token classes/types within an MCT contract are fungible tokens. MCTs could
implement various token standards within the same contract, but this beyond
the scope of this post.

# Balance Packing Transfer Efficiency

One of the advantages of having multiple fungible token classes within the
same contract is that we can more efficiently transfer different token classes
in a single transaction. Most of the efficiency gains can be attributed to the
ability to “pack” balances together within a share “storage slot” (256 bits),
saving some storage cost. Storing data on the blockchain is one of the most
expensive operations. Occupying _less_ storage space can significantly reduce
costs, and this might be even truer [in the near
future](https://ethresear.ch/t/a-simple-and-principled-way-to-compute-rent-
fees/1455).

![](https://miro.medium.com/max/1400/1*OHmE52kI_aLLK4dgIKVqBw.png)

In our [MCT implementation](https://github.com/arcadeum/multi-token-standard),
we store 16 token balances within a single `uint256` (a 256 bits unsigned
integer) where each token balance occupies 16 bits. You can then keep track of
as many token balances as you want by having many `uint256` where balances are
packed in. However, because of this packing, a given token balance can’t
exceed 2¹⁶, or `65,546`. This can be a reasonable limit for many applications.
For instance, under what circumstances would a single player need to be able
to own more than 2¹⁶ swords? The one instance where this limit could become a
problem is for a custodial exchange or proxy contract holding the funds on the
behalf of many users, however, it is unclear whether or not this will be a
problem in practice. Nevertheless, the amount of packing can easily be
modified. For instance, packing 8 token balances in an `uint256` instead of 16
increases the balance limit from `65,546` to `4,294,967,296`. One can also do
the opposite and increase the amount of token balances packed per `uint256`,
reducing the balance limit but increasing storage efficiency.

The efficiency gains come from the fact that you can transfer 16 token classes
with a single storage update, which is much less costly. However, the balance
of these token classes needs to be packed within the _same_ `uint256` in order
to benefit from this efficiency gain. Indeed, if you transfer 16 token classes
where their balance is stored in different `uint256`, then you will have 16
storage updates, like a regular ERC-20 transfer. This means that token classes
that are more likely to be transferred together should have IDs that are close
to each others (e.g. 23, 24, 25, etc.) as well, increasing the likelihood of
having many token classes within the same `uint256.`

These compromises and assumptions might be inappropriate for some
applications, but we believe others will find this useful.

# Comparing Transfer Costs Between Standards

We transferred a single token from 100 different classes for ERC-20, ERC-721
and MCTs. In the case of ERC-721, each token type is a different NFT, within
the same contract. In the case of ERC-20, each token type is a different
ERC-20 token, stored in different contracts. For both ERC-721 and ERC-20, we
also wrote a wrapper contract that transfers on behalf of users, saving on the
base transaction cost. The cost here does not include the `approval` call cost
that such wrapping contracts would necessitate.

##  **Transferring 100 ERC-721 tokens in different transaction calls :**

  * Total gas cost : **5,113,036**
  * Gas Cost Per Transfer : **51,130**

##  **Transferring 100 ERC-721 tokens with a wrapper contract :**

  * Total gas cost : **2,463,700**
  * Gas Cost Per Transfer : **24,637**

##  **Transferring 100 ERC-20 tokens in different transaction calls :**

  * Total gas cost : **5,153,300**
  * Gas Cost Per Transfer : **51,533**

##  **Transferring 100 ERC-20 tokens with wrapper contract :**

  * Total gas cost : **3,373,822**
  * Gas Cost Per Transfer : **33,738**

##  **Transferring 100 fungible tokens from MCT contract without balance
packing :**

  * Total gas cost : **2,788,039**
  * Gas Cost Per Transfer : **27,880**

##  **Transferring 100 fungible tokens from MCT contract with balance
packing**

  * Total gas cost : **467,173**
  * Gas Cost Per Transfer : **4,671**

Note that the balance packing calculation assumes tokens have close by IDs,
hence the result above is a cost lower bound. The balance packing can offer
significant efficiency gains under the right circumstances, up to 10x savings
compared to regular transfers and 5x–7x when using wrapper contracts for batch
transfers. In addition, I am fairly convinced additional significant
optimization are possible without adding much complexity.

Computational efficiency is not the only efficiency that matters and better
[price discovery](https://en.wikipedia.org/wiki/Price_discovery) efficiency is
an advantage fungible tokens have over non-fungible ones. Stay tuned for a
post on this topic.

# Conclusion

In this post, we discussed the concept of Multi-Class Token contracts and how
they are distinct from now popular ERC-20 and ERC-721 token standards. Via
balance packing, we also showed how having many fungible token classes within
the same contract can lead to significant efficiency gains when transferring
multiple token classes at once. We hope that this post will lead to more
research in MCTs and token transfer efficiency in general.

You can find our MCT implementation (an ERC1155 contract) with balance packing
here: <https://github.com/arcadeum/multi-token-standard>

\--

5

\--

\--

5

## [More from Horizon Games](/horizongames?source=post_page-----
9acebd4ff6ef--------------------------------)

We’re building a New Dimension where Internet economies are fun, accessible,
and for the benefit of all participants. www.horizon.io

[Read more from Horizon Games](/horizongames?source=post_page-----
9acebd4ff6ef--------------------------------)

## Recommended from Medium

[[![Rahul
Rai](https://miro.medium.com/fit/c/40/40/1*kWMve42OWk2JLLg_3IGj5Q@2x.jpeg)](/@rah-1?source=post_internal_links
---------0----------------------------)

[Rahul Rai

](/@rah-1?source=post_internal_links---------0----------------------------)

## The Hitchhiker’s Guide to DeFi (Part II) — DEXs & AMMs

![](https://miro.medium.com/focal/112/112/50/50/1*BUIO-3WNUmcszsk2itqMgQ.png)](/@rah-1/the-
hitchhikers-guide-to-defi-part-ii-dexs-
amms-3dce1cfbf959?source=post_internal_links---------
0----------------------------)

[[![Chrisikpe](https://miro.medium.com/fit/c/40/40/0*0HO7JQ9k8EGWQtaC)](/@chrisikpe2000?source=post_internal_links
---------1----------------------------)

[Chrisikpe

](/@chrisikpe2000?source=post_internal_links---------
1----------------------------)

## RENA FINANCE and the FUTURE of DEFI

![](https://miro.medium.com/focal/112/112/50/50/1*LqV8LgT20IMHIQnPV5tZhA.jpeg)](/@chrisikpe2000/rena-
finance-and-the-future-of-defi-d4c85106a536?source=post_internal_links
---------1----------------------------)

[[![01
Exchange](https://miro.medium.com/fit/c/40/40/1*AVQmyGyymquLJl3bunTLnA.png)](/@01exchange?source=post_internal_links
---------2----------------------------)

[01 Exchange

](/@01exchange?source=post_internal_links---------
2----------------------------)

## 01 Exchange Introduces Power Perpetuals (#SQUOL)

![](https://miro.medium.com/focal/112/112/98/28/0*mADXKZ04SlqRmsb3.jpg)](/@01exchange/01-exchange-
introduces-power-perpetuals-squol-1c8aa1dbc1d8?source=post_internal_links
---------2----------------------------)

[[![Roei
Levav](https://miro.medium.com/fit/c/40/40/1*6iRRJq7OdnFxnf9DSDgQzQ.jpeg)](/@Roeil?source=post_internal_links
---------3----------------------------)

[Roei Levav

](/@Roeil?source=post_internal_links---------3----------------------------)

in

[Efficient Frontier

](https://medium.com/efficient-frontier?source=post_internal_links---------
3----------------------------)

## About Efficient Frontier

![](https://miro.medium.com/focal/112/112/50/50/1*KkeX6k_bayo3OV5Led1i-g.jpeg)](/efficient-
frontier/efficient-frontier-about-dfdb60d19f51?source=post_internal_links
---------3----------------------------)

[[![jamilapatersonofficial](https://miro.medium.com/fit/c/40/40/1*W5-2uk96EgYwsHPAuCyThw.png)](/@jamilapatersonofficial?source=post_internal_links
---------4----------------------------)

[jamilapatersonofficial

](/@jamilapatersonofficial?source=post_internal_links---------
4----------------------------)

## To book profits, here’s what traders can do with their Ethereum holdings

![](https://miro.medium.com/focal/112/112/50/50/1*4Sbi3zUx-
lMaYPLs9o23HA.jpeg)](/@jamilapatersonofficial/to-book-profits-heres-what-
traders-can-do-with-their-ethereum-
holdings-6ccfc87b4db?source=post_internal_links---------
4----------------------------)

[[![kristi
kinzel](https://miro.medium.com/fit/c/40/40/1*OeY9385ApB0U1pZwfkL0lQ.jpeg)](/@kristikinzel86?source=post_internal_links
---------5----------------------------)

[kristi kinzel

](/@kristikinzel86?source=post_internal_links---------
5----------------------------)

## Missed on Doge, Shib, SHINJA? GAMEIN is here. Get ready for Private Sale

![](https://miro.medium.com/focal/112/112/50/50/1*lzBgzIvDqqh_BYgEE_r4vg.jpeg)](/@kristikinzel86/missed-
on-doge-shib-shinja-gamein-is-here-get-ready-for-private-sale-
ef240db90740?source=post_internal_links---------5----------------------------)

[[![Abaga Stephen](https://miro.medium.com/fit/c/40/40/1*jXx7e4zA-
TrMgzIxrJsZeg.jpeg)](/@dikeabaga?source=post_internal_links---------
6----------------------------)

[Abaga Stephen

](/@dikeabaga?source=post_internal_links---------
6----------------------------)

## INTRODUCTION ON DOAIBU.

![](https://miro.medium.com/focal/112/112/50/50/1*XnLIRRC0sEKtnoPqSClY9w.jpeg)](/@dikeabaga/a-brief-
introduction-on-doaibu-b08d74eee818?source=post_internal_links---------
6----------------------------)

[[![Budylevavarvara](https://miro.medium.com/fit/c/40/40/0*pIbWHRTVBEEH6xnQ.jpg)](/@budylevavarvara?source=post_internal_links
---------7----------------------------)

[Budylevavarvara

](/@budylevavarvara?source=post_internal_links---------
7----------------------------)

## Let’s take a closer look at the Goldfinch project

![](https://miro.medium.com/focal/112/112/50/50/1*4U5cSkdsO_7A5j0sNYUqBw.png)](/@budylevavarvara/lets-
take-a-closer-look-at-the-goldfinch-project-
afa83e1f1155?source=post_internal_links---------7----------------------------)

[](/?source=post_page-----9acebd4ff6ef--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
9acebd4ff6ef--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
9acebd4ff6ef--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
9acebd4ff6ef--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
9acebd4ff6ef--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----9acebd4ff6ef--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----9acebd4ff6ef--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fhorizongames%2Fgoing-
beyond-erc20-and-erc721-9acebd4ff6ef&source=post_page
--------------------------nav_reg-----------)

[![Philippe
Castonguay](https://miro.medium.com/fit/c/176/176/1*KccjAOL2T6YnKj3pHX3L7A.jpeg)](/@PhABC)

[

## Philippe Castonguay

](/@PhABC)

374 Followers

Distributed Ledger Technologies | Smart contract research and development
@HorizonGames | Computational neuroscience research

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F1580157d84ad&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fhorizongames%2Fgoing-
beyond-erc20-and-
erc721-9acebd4ff6ef&newsletterV3=62c1161d949c&newsletterV3Id=1580157d84ad&user=Philippe+Castonguay&userId=62c1161d949c&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Rebels Haunted
Mansion](https://miro.medium.com/fit/c/40/40/1*VgGmgEsLuaTLnMRUfYE6yg.png)](/@rebelkidsnft?source=read_next_recirc
---------0---------------------d275d779_3551_44a7_b56e_4fd076755a52-------)

[Rebels Haunted Mansion

](/@rebelkidsnft?source=read_next_recirc---------0---------------------
d275d779_3551_44a7_b56e_4fd076755a52-------)

## Rebel Kid: Spring Roadmap

![](https://miro.medium.com/focal/112/112/50/50/1*-2MeI9jDD8r9PUb9ELoZMQ.png)](/@rebelkidsnft/rebel-
kid-spring-roadmap-510f65f002d1?source=read_next_recirc---------0
---------------------d275d779_3551_44a7_b56e_4fd076755a52-------)

[[![JP
Beauchamp](https://miro.medium.com/fit/c/40/40/1*dT0UZAqNTDPepfMLRVZnhQ.jpeg)](/@jpbeauchamp81?source=read_next_recirc
---------1---------------------d275d779_3551_44a7_b56e_4fd076755a52-------)

[JP Beauchamp

](/@jpbeauchamp81?source=read_next_recirc---------1---------------------
d275d779_3551_44a7_b56e_4fd076755a52-------)

in

[RoundtableDAO Project Reviews

](https://medium.com/roundtabledao-project-reviews?source=read_next_recirc
---------1---------------------d275d779_3551_44a7_b56e_4fd076755a52-------)

## Heroes of NFT — First Collectible NFT Card Game on Avalanche

![](https://miro.medium.com/focal/112/112/50/50/1*qqEHqmBdeSB2U6wAMKvFQg.png)](/roundtabledao-
project-reviews/heroes-of-nft-first-collectible-nft-card-game-on-
avalanche-860bff1dca43?source=read_next_recirc---------1---------------------
d275d779_3551_44a7_b56e_4fd076755a52-------)

[[![CryptoAnt Gang](https://miro.medium.com/fit/c/40/40/1*VG-
eabQdBTTDzc0yZzerlQ.png)](/@cryptoantgang?source=read_next_recirc---------2
---------------------d275d779_3551_44a7_b56e_4fd076755a52-------)

[CryptoAnt Gang

](/@cryptoantgang?source=read_next_recirc---------2---------------------
d275d779_3551_44a7_b56e_4fd076755a52-------)

## Introducing the DAOPAD — A Community-governed Decentralized NFT Incubator
and LaunchPad

![](https://miro.medium.com/focal/112/112/50/50/1*gN2bLcA_rxT2yAbg2PSUpQ.png)](/@cryptoantgang/introducing-
the-daopad-a-community-governed-decentralized-nft-incubator-and-
launchpad-48a587f6c57f?source=read_next_recirc---------2---------------------
d275d779_3551_44a7_b56e_4fd076755a52-------)

[[![poochcafenft](https://miro.medium.com/fit/c/40/40/1*FvaWA3obM9sVO0CsMtT5nA@2x.jpeg)](/@poochcafenft?source=read_next_recirc
---------3---------------------d275d779_3551_44a7_b56e_4fd076755a52-------)

[poochcafenft

](/@poochcafenft?source=read_next_recirc---------3---------------------
d275d779_3551_44a7_b56e_4fd076755a52-------)

## meet your creator

![](https://miro.medium.com/focal/112/112/50/50/1*_HU2eHhk4ZMKpkjKf1G1pQ.png)](/@poochcafenft/meet-
your-creator-46756ef4f070?source=read_next_recirc---------3
---------------------d275d779_3551_44a7_b56e_4fd076755a52-------)

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

