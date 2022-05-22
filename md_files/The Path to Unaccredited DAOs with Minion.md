[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/8113213f7195&~feature=LoOpenInAppButton&~channel=ShowPostUnderUser&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![The
LAO](https://miro.medium.com/fit/c/96/96/2*X_8LYIcePYE1DMhi8vcHFw.png)](/@thelaoofficial?source=post_page
-----8113213f7195--------------------------------)

[The LAO](/@thelaoofficial?source=post_page-----
8113213f7195--------------------------------)

Follow

Jun 9, 2020

·

6 min read

#  **Charting the Path to Unaccredited DAOs with Minion**

 _The LAO team is extending Moloch v2, with Raid Guild’s Minon framework, to
create new structures that could open up the pathway towards unaccredited,
for-profit DAOs._

![](https://miro.medium.com/max/1080/0*X6wjaYm1Se7N1SOu)

The era of DAOs is just beginning. With the creation of the Moloch v2 smart
contracts, we’re nearing an ERC-20-like standard for blockchain-based
organizations.

One fact that’s thus far underappreciated is that these smart contracts are
just the tip of the iceberg. The Moloch v2 smart contracts can be extended
through [Raid Guild](https://raidguild.org/)’s framework called
[Minion](https://github.com/raid-guild/moloch-minion). These extensions open
up an entirely new universe of possibilities for DAOs and the range of
transactions they can undertake.

On [The LAO](https://www.thelao.io/) team side, we’ve been fascinated with how
these extensions may change the landscape of DAOs and wanted to share some of
our initial findings. In short, we believe that Minions will enable DAOs to
increase in their complexity and also open up pathways to create entirely new
structures that protect investors and potentially even provide a pathway to
create for-profit DAOs that unaccredited investors may participate in.

##  **Overview of Minion**

By way of background, a Minion is a short extension that interacts with the
[Moloch v2/LAO](/@thelaoofficial/moloch-v2-smart-contract-audit-report-for-
the-lao-48fb0415695a) smart contract. At its core, Minion is an escrow program
that receives funding from a DAO. However, the Minion can **only** transfer
funds to another Ethereum address after it has been authorized by DAO members
via their proposal sequence — a true programmatic proxy.

Through Minion, Moloch-based DAOs will be able to seamlessly create sub-groups
of DAOs, which enable DAO members to segregate and pool funds in a way that
will protect investors, manage tax risk, and potentially also decrease the
risk of fraud. They also open up the possibility of creating DAOs to interact
with liquidity pools, but we’ll discuss that in a separate post.

##  **Overview of The LAO’s New Minion — _Baby DAO_**

We’ve been playing around with a Minion pattern that we’ve internally been
calling “Baby DAOs.” This structure enables a group of members in a parent DAO
to authorize the creation of a “Baby” for any purpose.

![](https://miro.medium.com/max/1400/0*TP6kxkKkNykrIfx7)

These babies can be thought of as “throw away” pools that can be used to raise
funding or provide an investment for a specific project or initiative. For
example, when DAO babies are combined with Moloch v2 functionality, you can
coordinate a wider range of financial functions and explore more opportunities
to cooperate without losing the security and trust assumptions of smart
contracts:

  * Group of DAO-members pool capital to source and approve investment opportunities (and “rage quit” if they want their capital back)
  * Create a “baby,” which members of the DAO that want to participate in an investment have to voluntarily fund and join (and possibly even rage quit prior to an investment if they somehow change their mind).
  * All without the need for members to charge fees to facilitate investment.

The result is fairly profound. DAOs and DAO babies could enable the Ethereum
ecosystem to efficiently rely on the collective wisdom of the crowd in order
to identify potential investment opportunities, but each member will have to
voluntarily approve and pledge their capital in order to participate in the
investment.

Under such an approach, the risk of individual fraud is presumably decreased
for two reasons. First, since the main DAO has to authorize the creation of a
Baby DAO, the main DAO members act as a natural filtering mechanism, enabling
a group to better identify and flag potential investment opportunities that
are fraudulent and specious in nature. Second, since entering into an
investment requires an affirmative act on the part of the member — and since
the member retains the right to walk away with their pledged capital at
multiple points during the process — no member has control over another
members’ funds. The DAO itself becomes effectively non-custodial in nature.

Due to these characteristics, a DAO-plus-Baby architecture, such as that
outlined above, opens up the possibility of creating DAOs where unaccredited
and accredited investors could work together, potentially decreasing⁠ — if not
dramatically decreasing⁠ — the risk of fraud that underpins most of the global
securities law regulations.

DAOs are the most transparent and participatory organizations and we have seen
to date. Through the above architecture, the risk of asymmetric information
should theoretically decrease in much the same way that we’re seen on the
internet and other open-source projects. Open source projects have tended to
verify “Linus’s law” ( _i.e._ , “given enough eyeballs, all bugs are
shallow”). We think the same approach could apply for investments. If a DAOs
has enough members, then the risk of member’s identifying or authorizing the
investment into a project that is fraudulent in nature should go down.

This structure we think is appealing from a policy perspective. A crowd of
accredited and potentially even unaccredited investors could source potential
projects to invest in and members could pool their capital to facilitate the
investment. In this flow, there is equal access to deal flow and potentially a
large pool of capital for projects to receive needed funding. At the same
time, no one member has control over another member’s funds.

These possibilities are simply not possible in the legacy world.

##  **Smart Contract Breakdown**

Currently, we are working on different versions of the Minion
[code](https://github.com/openlawteam/LAOproxy/tree/master). The Minion can be
configured to work with raw Ether, WETH/ERC-20s, or both. The goal at the end
of the day will be to pare these down as much as possible. In the interest of
simplicity, the Minion itself has only a few core functions: _Constructor_ ,
_doWithdraw_ , _proposeAction_ and _executeAction_.

When the Minion is deployed, the “Constructor” function requires a DAO address
to interact with (this DAO is the _Parent_ , and in our case, The LAO).

The Minion/LAOproxy is funded directly with ETH or WETH by sending it to its
contract address. In the case of WETH/ERC20s there is also the option to
receive funding via the Moloch v2 proposal process (the “Do Withdraw” function
is used to withdraw ERC-20s received via the Parent DAO).

Even though a Minion can receive its funding entirely outside of the Parent
DAO, the decision to release those funds from the Minion still resides with
the Parent DAO.

To release these funds anyone can execute “Propose Action” which requests the
Parent DAO’s permission to release funds to a specified recipient address and
amount, along with a description (when “Propose Action” is called it “Submits
Proposal” to the Parent DAO).

The Members of the Parent DAO can then evaluate this request through the
standard Moloch v2 “Sponsor Proposal” -> “Vote” -> “Process Proposal”
sequence.

If the proposal has passed, then the Minion may finally call “Execute Action”
to send the funds in the amount approved by the Parent DAO directly from the
Minion to the recipient address named in “Propose Action.”

This, again, is just the beginning of a slew of different types of future
DAOs. By extending the Moloch v2 smart contracts through Minion, we now have
the possibility of opening up to a range of DAOs and Baby DAOs, as well as,
the transactions they can operate with. Stay tuned as we experiment with the
tremendous possibilities that await!

# Learn More

If you would like more information about becoming a LAO member or project,
please reach out to us at [hello@thelao.io](http://hello@thelao.io/). For
further information, check out our [docs](https://docs.thelao.io/), which
cover questions about The LAO’s structure and operation, or hit us up via
[email](http://hello@thelao.io/) or
[telegram.](https://t.me/joinchat/FLvdBBVz3o9pfi-rfd9BqQ)

\--

\--

\--

## [More from The LAO](/@thelaoofficial?source=post_page-----
8113213f7195--------------------------------)

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F71c8a361b148&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40thelaoofficial%2Fthe-
path-to-unaccredited-daos-with-
minion-8113213f7195&newsletterV3=61217eadf32d&newsletterV3Id=71c8a361b148&user=The+LAO&userId=61217eadf32d&source=-----8113213f7195
---------------------subscribe_user-----------)

A For-Profit, Limited Liability Autonomous Organization, powered by
@OpenLawOfficial.

Love podcasts or audiobooks? Learn on the go with our new app.

[Try
Knowable](https://knowable.fyi/?utm_source=medium&utm_medium=referral&utm_campaign=medium-
post-footer&source=post_page-----8113213f7195--------------------------------)

## Recommended from Medium

[[![Zhen](https://miro.medium.com/fit/c/40/40/1*9Z8L1L4ABewgZsGwDFMDYA.jpeg)](/@ZhenIOST?source=post_internal_links
---------0----------------------------)

[Zhen

](/@ZhenIOST?source=post_internal_links---------0----------------------------)

in

[IOST

](https://medium.com/iost?source=post_internal_links---------
0----------------------------)

## IOST Bi-Weekly Report | DeFi-ning Plans for H2 2020

![](https://miro.medium.com/focal/112/112/50/50/1*M9Rd5vEW0TZbtslVFeEG9Q.jpeg)](/iost/iost-
bi-weekly-report-defi-ning-plans-
for-h2-2020-72e935b3e272?source=post_internal_links---------
0----------------------------)

[[![Patract｜ Wasm Contract Open
Platform](https://miro.medium.com/fit/c/40/40/1*wvsPk8PikZhFsYqBWWvsNA.png)](/@patractlabs?source=post_internal_links
---------1----------------------------)

[Patract｜ Wasm Contract Open Platform

](/@patractlabs?source=post_internal_links---------
1----------------------------)

## Introducing Patract Hub: the Polkadot Smart Contract Developer Center

![](https://miro.medium.com/focal/112/112/50/50/1*0dC0Q9jMjFb5JNdQIQlzMg@2x.png)](/@patractlabs/introducing-
patract-hub-the-polkadot-smart-contract-developer-center-
ec82efb8a727?source=post_internal_links---------1----------------------------)

[[![BLOCK.CO](https://miro.medium.com/fit/c/40/40/1*QoZbQ7vieGRq0CRaXyoiFQ.png)](/@blockdotco?source=post_internal_links
---------2----------------------------)

[BLOCK.CO

](/@blockdotco?source=post_internal_links---------
2----------------------------)

## The Ultimate List of NFT (Non-Fungible Token) Real Use Cases

![](https://miro.medium.com/focal/112/112/50/50/1*fYRAziNK5ZT1Xao2c6-TjA.png)](/@blockdotco/the-
ultimate-list-of-nft-non-fungible-tokens-real-use-cases-
ab7ff93b0deb?source=post_internal_links---------2----------------------------)

[[![Shyna
Hegde](https://miro.medium.com/fit/c/40/40/1*3IB7x3d7HJlNLZhZL845Lg.jpeg)](/@shynahegde?source=post_internal_links
---------3----------------------------)

[Shyna Hegde

](/@shynahegde?source=post_internal_links---------
3----------------------------)

## Web3 and everything in between

![](https://miro.medium.com/focal/112/112/50/50/1*xD2mCk0DBjyV6PRLUqZ82A.jpeg)](/@shynahegde/web3-and-
everything-in-between-d6b50be0d8bb?source=post_internal_links---------
3----------------------------)

[[![0xBEE](https://miro.medium.com/fit/c/40/40/1*16yoBILWbqE4FPy8i1gB7A.jpeg)](/@0xBEE?source=post_internal_links
---------4----------------------------)

[0xBEE

](/@0xBEE?source=post_internal_links---------4----------------------------)

## The hum of bees is the voice of the garden🥀

![](https://miro.medium.com/focal/112/112/50/50/1*oV1sU5559U47TAJrp1PFdw.jpeg)](/@0xBEE/the-
hum-of-bees-is-the-voice-of-the-garden-957937e49de2?source=post_internal_links
---------4----------------------------)

[[![Lukas
Götz](https://miro.medium.com/fit/c/40/40/1*dKTIHQseLc6zUFzB5OlZpQ.jpeg)](/@lukasgoetz?source=post_internal_links
---------5----------------------------)

[Lukas Götz

](/@lukasgoetz?source=post_internal_links---------
5----------------------------)

in

[block42

](https://medium.com/block42-blockchain-company?source=post_internal_links
---------5----------------------------)

## Company Update Q2/2020

![](https://miro.medium.com/focal/112/112/50/50/1*hD67dxwRX0dWwKhe_yl9Vw.png)](/block42-blockchain-
company/we-would-like-to-keep-our-clients-partners-and-followers-informed-
about-the-progress-block42-makes-bdda64f43908?source=post_internal_links
---------5----------------------------)

[[![Zamm
Street](https://miro.medium.com/fit/c/40/40/0*H1Co7Ip1Gw-B1O-w.jpg)](/@newmokha?source=post_internal_links
---------6----------------------------)

[Zamm Street

](/@newmokha?source=post_internal_links---------6----------------------------)

## Get Smart (Contracts)

](/@newmokha/get-smart-contracts-38a4cbaa2c2c?source=post_internal_links
---------6----------------------------)

[[![Blockonomist
Staff](https://miro.medium.com/fit/c/40/40/1*kSYEnOr1yWmwSqj8_KVlMA.png)](/@blockonomist?source=post_internal_links
---------7----------------------------)

[Blockonomist Staff

](/@blockonomist?source=post_internal_links---------
7----------------------------)

in

[Blockonomist

](https://medium.com/blockonomist?source=post_internal_links---------
7----------------------------)

## CRYPTOCURRENCIES IN CHORUS

![Gettyimages](https://miro.medium.com/focal/112/112/50/50/0*DioSvPlqNf9k91hk.jpg)](/blockonomist/cryptocurrencies-
in-chorus-c4967b5381a?source=post_internal_links---------
7----------------------------)

[](/?source=post_page-----8113213f7195--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
8113213f7195--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
8113213f7195--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
8113213f7195--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
8113213f7195--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----8113213f7195--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----8113213f7195--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40thelaoofficial%2Fthe-
path-to-unaccredited-daos-with-minion-8113213f7195&source=post_page
--------------------------nav_reg-----------)

[![The
LAO](https://miro.medium.com/fit/c/176/176/2*X_8LYIcePYE1DMhi8vcHFw.png)](/@thelaoofficial)

[

## The LAO

](/@thelaoofficial)

608 Followers

A For-Profit, Limited Liability Autonomous Organization, powered by
@OpenLawOfficial.

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F71c8a361b148&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40thelaoofficial%2Fthe-
path-to-unaccredited-daos-with-
minion-8113213f7195&newsletterV3=61217eadf32d&newsletterV3Id=71c8a361b148&user=The+LAO&userId=61217eadf32d&source=--------------------------subscribe_user-----------)

## More from Medium

[[![CYBAVO
Inc.](https://miro.medium.com/fit/c/40/40/1*QIy-I3YFsvXqvDi66KjSVw.png)](/@cybavo?source=read_next_recirc
---------0---------------------db02a7f4_0d47_4956_a4eb_3e9213c66761-------)

[CYBAVO Inc.

](/@cybavo?source=read_next_recirc---------0---------------------
db02a7f4_0d47_4956_a4eb_3e9213c66761-------)

## The Rise of DAOs: How They Can Transform Institutional Decision-making

![](https://miro.medium.com/focal/112/112/50/50/0*YFKiG_pNX_uTB-
Tt.png)](/@cybavo/the-rise-of-daos-how-they-can-transform-institutional-
decision-making-fbcfba67e8ba?source=read_next_recirc---------0
---------------------db02a7f4_0d47_4956_a4eb_3e9213c66761-------)

[[![Julien
Thevenard](https://miro.medium.com/fit/c/40/40/1*QaG8sGsBpfp0LOF1YcyN_g.jpeg)](/@julienthevenard?source=read_next_recirc
---------1---------------------db02a7f4_0d47_4956_a4eb_3e9213c66761-------)

[Julien Thevenard

](/@julienthevenard?source=read_next_recirc---------1---------------------
db02a7f4_0d47_4956_a4eb_3e9213c66761-------)

## Upcoming trends in DeFi

![](https://miro.medium.com/focal/112/112/50/50/0*z2kW4snfGRbbqVod)](/@julienthevenard/upcoming-
trends-in-defi-87916e4f5ac3?source=read_next_recirc---------1
---------------------db02a7f4_0d47_4956_a4eb_3e9213c66761-------)

[[![Fox
Rogers](https://miro.medium.com/fit/c/40/40/1*6GpGAS_zUlnTb2NDoDRRRw.jpeg)](/@foxrogers?source=read_next_recirc
---------2---------------------db02a7f4_0d47_4956_a4eb_3e9213c66761-------)

[Fox Rogers

](/@foxrogers?source=read_next_recirc---------2---------------------
db02a7f4_0d47_4956_a4eb_3e9213c66761-------)

in

[Cauldron.co

](https://medium.com/cauldron-co?source=read_next_recirc---------2
---------------------db02a7f4_0d47_4956_a4eb_3e9213c66761-------)

## Cauldron raises $1.4m to debut Sci-Fi project in Web3 gaming

![](https://miro.medium.com/focal/112/112/50/50/0*xmKHAnNgzYH5P5sr.jpg)](/cauldron-
co/cauldron-raises-1-4m-to-debut-sci-fi-project-in-
web3-gaming-7abfb2d86343?source=read_next_recirc---------2
---------------------db02a7f4_0d47_4956_a4eb_3e9213c66761-------)

[[![Alex
Shibu](https://miro.medium.com/fit/c/40/40/1*whmc_doZN0cdaAesKxOIsQ.png)](/@alexshibu?source=read_next_recirc
---------3---------------------db02a7f4_0d47_4956_a4eb_3e9213c66761-------)

[Alex Shibu

](/@alexshibu?source=read_next_recirc---------3---------------------
db02a7f4_0d47_4956_a4eb_3e9213c66761-------)

## wEb3 & why DAOs the tech of tomorrow?

![](https://miro.medium.com/focal/112/112/50/50/0*L7nVbYcZlqAehk_x)](/@alexshibu/web3-why-
daos-the-tech-of-tomorrow-4b46ba95ca69?source=read_next_recirc---------3
---------------------db02a7f4_0d47_4956_a4eb_3e9213c66761-------)

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

