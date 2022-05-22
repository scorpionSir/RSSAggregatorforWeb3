[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/48fb0415695a&~feature=LoOpenInAppButton&~channel=ShowPostUnderUser&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![The
LAO](https://miro.medium.com/fit/c/96/96/2*X_8LYIcePYE1DMhi8vcHFw.png)](/@thelaoofficial?source=post_page
-----48fb0415695a--------------------------------)

[The LAO](/@thelaoofficial?source=post_page-----
48fb0415695a--------------------------------)

Follow

Mar 2, 2020

·

5 min read

#  **Moloch v2 Smart Contract Audit Report for The LAO**

[ _OpenLaw_](https://www.openlaw.io/) _, and_[
_Moloch_](https://molochdao.com/) _in conjunction with_[ _ConsenSys
Diligence_](https://diligence.consensys.net/) _, have worked through ConsenSys
Diligence’s audit report and made the major changes recommended by Diligence._

![](https://miro.medium.com/max/1280/1*i4Zd3Lm7RBtz2zRldCFPSQ.gif)

[The LAO](http://thelao.io) is poised to be a game-changer in financing
emerging Ethereum ventures. With The LAO, there will be a cohesive legal
structure to enable members to not just give grants, but to invest in
blockchain-based projects in exchange for tokenized stock or utility tokens.
Using the tooling provided by [OpenLaw](https://www.openlaw.io/), the LAO will
be set up as a limited liability entity, organized in Delaware, using curated
Moloch v2 [smart contracts](https://github.com/openlawteam/TheLAO) to handle
mechanics related to voting, funding, and allocation of collected funds.

Our thesis is that the Moloch v2 smart contracts will look like the ERC-20
token standard developed today, but for venture capital financing. Moloch’s
blockchain-based governance model has narrowly focused its technical and game
theory design choices to coordinate charity grants for Ethereum projects,
pushing its core governance to a vote-weighted multi-signature smart contract
with a “ragequit” mechanism that allows its membership to opt-out and receive
a proportion of the [custodied
funds](https://etherscan.io/address/0x211a94468ba1e379236b45ca42dc63ee93139c7e#tokentxns)
equal to their voting weight at any time.

Over the past several weeks, OpenLaw, Moloch and ConsenSys Diligence have been
working together to audit the Moloch v2 smart contract code — rigorously
looking for any potential security vulnerabilities in the code and making
appropriate changes.

# Security Audit Report

The LAO takes security very seriously. We chose Moloch smart contracts early
on, since, as a rule of thumb, the simpler the smart contracts, the better —
and the Moloch is ruthless in removing unnecessary code. As we gear up for
this to be a massive success, we have been aggressively making sure that the
code is bugless and reviewed by the best.

A strong and thorough smart contract audit report should be detailed and
include the following key information such as the background of the audit,
issues of the audit based on the severity, description and recommendations.

The ConsenSys Diligence audit report can be found
[here](https://diligence.consensys.net/audits/2020/01/the-lao/). We’ve made
changes based on the Diligence report and have outlined some key pieces of the
code that we feel are important to emphasize and highlight. The trust model
section is a basic overview of how the proposal process works at a high level
to prevent unwanted proposals. The pull-pattern, limit on whitelisted tokens,
and token overflow section are the major fixes made in conjunction with
Diligence to improve security and simplify the codebase.

 _Trust Model_

The trust model has been the beating heart of the original Moloch[
code](https://github.com/metacartel/MCV/blob/master/MCV-Whitepaper.md) and
continues in the same vein for MolochDAOv.2/LAO. The LAO/MolochDAOv2 uses a
social approach to avoid malicious/spam proposals. Proposals can be submitted
by anyone, but for a proposal to move forward, it must be sponsored by a
current member, to be voted on. This is similar to admitting a new member to a
country club, where the potential member has to be sponsored/vouched for by a
current member. Off-chain, it is expected proposals will be vetted by at least
one Member before they decide to sponsor a proposal.

Continuing as a Member is permission-based and community policed by other
Members, where a Member can “ragequit” if they find a proposal too outrageous
and receive their capital back. Members can also be subject to a “ragekick”
vote where they can be removed upon a vote by the other Members.

 _Moving the Distribution of tokens to a “Pull Pattern”_

Instead of airdropping ERC20 token distributions directly into a Member or
Project’s wallet, the Moloch has moved to the more secure “[Pull
Pattern](https://consensys.github.io/smart-contract-best-
practices/recommendations/#favor-pull-over-push-for-external-calls).” During
the audit process most of the vulnerabilities found by Diligence were solvable
by instituting a pull pattern. The pull pattern works as follow’s — A User’s
balance is credited in the GuildBank address with any ERC20 tokens they are
entitled to, and then when the User is ready they can withdraw from their
token balance.

 _Limit on Whitelisted Tokens_

Due to concerns about running out of gas on when iterating over a high number
of tokens and locking out access to funds forever, the “uint256 constant
MAX_TOKEN_WHITELIST_COUNT = 400” and “uint256 constant
MAX_TOKEN_GUILDBANK_COUNT = 200” have been hardcoded into the Moloch code. A
successful LAO with 200 projects funded and tokenized, would justify the
launch of another LAO. There is also a function for withdrawing tokens called
“withdrawBalance” where a User can withdraw each individual token by its
contract address. A single address withdrawal creates a layer of robustness
that can serve as a safeguard in the event one of the other tokens attempting
to be withdrawn is broken and prevents the use of “withdrawTokens” (which
iterates over the entire list of tokens).

 _Token Overflow_

If a token overflows — for example if an ERC20 token was subject to an extreme
hyperinflation event, then some functionality such as processProposal,
cancelProposal will break due to safeMath reverts. To account for a bad actor
— hyperinflating their tokens, a fix was implemented to create a function
“unsafeInternalTransfer()” that does not use SafeMath. Another safeguard in
the Moloch code worth noting is that in order for a token to be used within
the Moloch it must pass a whitelisting proposal process via a Member vote.
Also, the LAO is considering setting up a token factory contract for projects,
to ensure that the creation of ERC20’s is standardized and provide an added
layer of due diligence for a project’s ERC20s.

#  **Next Steps**

The LAO is targeted to launch for the members public sale in the next few
weeks. We have recently opened up for pre-registration of members so they can
easily get their accredited investor and KYC checks prior to the date of sale,
see [here](https://www.thelao.io/verify). If you’re a project that would like
to apply for funding prior to the date of sale, please do so
[here](https://www.thelao.io/apply).

If you’re interested in learning more about The LAO, please reach out to us at
[hello@thelao.io](mailto:hello@thelao.io). If you have any questions, check
out our [docs](https://docs.thelao.io/), which cover questions about The LAO’s
structure and operation, or hit us up via [email](http://hello@thelao.io/) or
[telegram.](https://t.me/joinchat/FLvdBBVz3o9pfi-rfd9BqQ)

\--

\--

\--

## [More from The LAO](/@thelaoofficial?source=post_page-----
48fb0415695a--------------------------------)

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F71c8a361b148&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40thelaoofficial%2Fmoloch-v2-smart-
contract-audit-report-for-the-
lao-48fb0415695a&newsletterV3=61217eadf32d&newsletterV3Id=71c8a361b148&user=The+LAO&userId=61217eadf32d&source=-----48fb0415695a
---------------------subscribe_user-----------)

A For-Profit, Limited Liability Autonomous Organization, powered by
@OpenLawOfficial.

Love podcasts or audiobooks? Learn on the go with our new app.

[Try
Knowable](https://knowable.fyi/?utm_source=medium&utm_medium=referral&utm_campaign=medium-
post-footer&source=post_page-----48fb0415695a--------------------------------)

## Recommended from Medium

[[![Jonny
Fry](https://miro.medium.com/fit/c/40/40/1*qtf4RKMFs_gf0cY4QzNOaQ.jpeg)](/@jonnyfry175?source=post_internal_links
---------0----------------------------)

[Jonny Fry

](/@jonnyfry175?source=post_internal_links---------
0----------------------------)

## A Stock Market crash — how soon? Will this trigger Blockchain technology be
further embraced?

![](https://miro.medium.com/focal/112/112/50/50/1*I5phrhGZ1qq7gjPo9JHiGA.png)](/@jonnyfry175/a-stock-
market-crash-how-soon-will-this-trigger-blockchain-technology-be-further-
embraced-e4e04911536c?source=post_internal_links---------
0----------------------------)

[[![hummingbot](https://miro.medium.com/fit/c/40/40/1*cvsDWXQPJsHRi6nmUVdGkw.png)](/@CoinAlpha?source=post_internal_links
---------1----------------------------)

[hummingbot

](/@CoinAlpha?source=post_internal_links---------
1----------------------------)

in

[Hummingbot Blog

](https://medium.com/hummingbot?source=post_internal_links---------
1----------------------------)

## Mapping the crypto market maker landscape

![](https://miro.medium.com/focal/112/112/50/50/1*b10iJxthEBj6tmE2vV9qmg.png)](/hummingbot/mapping-
the-crypto-market-maker-landscape-c420a036bd28?source=post_internal_links
---------1----------------------------)

[[![ErgoPad.io](https://miro.medium.com/fit/c/40/40/1*zyQG56e_Bb_r9szHuXJc_g.jpeg)](/@ergopad?source=post_internal_links
---------2----------------------------)

[ErgoPad.io

](/@ergopad?source=post_internal_links---------2----------------------------)

## Ergopad Project Update #5

![](https://miro.medium.com/focal/112/112/50/50/1*tCySB8MiyOXuUvKikD_KZw.png)](/@ergopad/ergopad-
project-update-5-e17a91afcb9b?source=post_internal_links---------
2----------------------------)

[[![META 1
Coin](https://miro.medium.com/fit/c/40/40/1*EasRnukwgBX7FobaKG6rKw.png)](/@meta1coin?source=post_internal_links
---------3----------------------------)

[META 1 Coin

](/@meta1coin?source=post_internal_links---------
3----------------------------)

## 7 Reasons Accepting Cryptocurrency for #business

![](https://miro.medium.com/focal/112/112/50/50/1*skX6wTi_FgsqVcGjtB47ow@2x.jpeg)](/@meta1coin/7-reasons-
accepting-cryptocurrency-for-business-990fb4025f0?source=post_internal_links
---------3----------------------------)

[[![ruslan
wing](https://miro.medium.com/fit/c/40/40/0*8tOcPaqFiIC5qAWK.jpg)](/@ruslanwing100?source=post_internal_links
---------4----------------------------)

[ruslan wing

](/@ruslanwing100?source=post_internal_links---------
4----------------------------)

## Bounty for XDC Market making

![](https://miro.medium.com/focal/112/112/50/50/1*az58NshDMALFtZ4zopOx3g.png)](/@ruslanwing100/bounty-
for-xdc-market-making-6326540e1766?source=post_internal_links---------
4----------------------------)

[[![Harith Kamarul](https://miro.medium.com/fit/c/40/40/2*R5aay0bWhvAMIw-a-
aKkzA.jpeg)](/@harithk?source=post_internal_links---------
5----------------------------)

[Harith Kamarul

](/@harithk?source=post_internal_links---------5----------------------------)

in

[Etherscan Blog

](https://medium.com/etherscan-blog?source=post_internal_links---------
5----------------------------)

## Ethereum in 2020: the View from the Block Explorer

![](https://miro.medium.com/focal/112/112/50/50/1*O63zJmPgJULSkl17BqNa7w.png)](/etherscan-
blog/ethereum-in-2020-the-view-from-the-block-
explorer-2f9a1db2ee15?source=post_internal_links---------
5----------------------------)

[[![Based
Club](https://miro.medium.com/fit/c/40/40/1*_RYOZj1LcBprD237MIMazg.jpeg)](/@BasedClub_co?source=post_internal_links
---------6----------------------------)

[Based Club

](/@BasedClub_co?source=post_internal_links---------
6----------------------------)

## Recap BasedClub with MELD

![](https://miro.medium.com/focal/112/112/50/50/1*BNXkGrnvq6yksY3k3EoHuQ.jpeg)](/@BasedClub_co/recap-
basedclub-with-meld-cb90c9df772e?source=post_internal_links---------
6----------------------------)

[[![HoneyFarm](https://miro.medium.com/fit/c/40/40/0*1BmUztDnATxanCyi)](/@honeyfarmchef?source=post_internal_links
---------7----------------------------)

[HoneyFarm

](/@honeyfarmchef?source=post_internal_links---------
7----------------------------)

## HoneyMoon 1st Week Recap

![](https://miro.medium.com/focal/112/112/50/50/1*hPO-
cOcuosLYtiMlYcJajA.png)](/@honeyfarmchef/honeymoon-1st-week-
recap-85be09de897f?source=post_internal_links---------
7----------------------------)

[](/?source=post_page-----48fb0415695a--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
48fb0415695a--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
48fb0415695a--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
48fb0415695a--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
48fb0415695a--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----48fb0415695a--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----48fb0415695a--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40thelaoofficial%2Fmoloch-v2-smart-
contract-audit-report-for-the-lao-48fb0415695a&source=post_page
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

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F71c8a361b148&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40thelaoofficial%2Fmoloch-v2-smart-
contract-audit-report-for-the-
lao-48fb0415695a&newsletterV3=61217eadf32d&newsletterV3Id=71c8a361b148&user=The+LAO&userId=61217eadf32d&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Shadowheartz](https://miro.medium.com/fit/c/40/40/1*hZ6UaovpxDU-Y4AKYIOX5A.png)](/@shadowheartz?source=read_next_recirc
---------0---------------------272abbca_cdfc_4dc7_aef7_dedd72160e49-------)

[Shadowheartz

](/@shadowheartz?source=read_next_recirc---------0---------------------
272abbca_cdfc_4dc7_aef7_dedd72160e49-------)

## NFT Smart Contract Analysis — PXN: Ghost Division

![](https://miro.medium.com/focal/112/112/50/50/1*YbYNUZ7_SwL896xMrEqC8A.jpeg)](/@shadowheartz/nft-
smart-contract-analysis-pxn-ghost-
division-954a276d9ee4?source=read_next_recirc---------0---------------------
272abbca_cdfc_4dc7_aef7_dedd72160e49-------)

[[![ZMOK.io](https://miro.medium.com/fit/c/40/40/1*4ud58n-m1yn4vUakWTqn_A.png)](/@zmok-
io?source=read_next_recirc---------1---------------------
272abbca_cdfc_4dc7_aef7_dedd72160e49-------)

[ZMOK.io

](/@zmok-io?source=read_next_recirc---------1---------------------
272abbca_cdfc_4dc7_aef7_dedd72160e49-------)

## Ethereum Global Pending Transactions Mempool

![](https://miro.medium.com/focal/112/112/50/50/1*STUX06xG17NptshTbXGsEw.png)](/@zmok-
io/ethereum-global-pending-transactions-
mempool-173771dcc248?source=read_next_recirc---------1---------------------
272abbca_cdfc_4dc7_aef7_dedd72160e49-------)

[[![Zoumana
Cisse](https://miro.medium.com/fit/c/40/40/1*6IxBVXBYLv_ZJl346aJ9ow@2x.jpeg)](/@zouvier?source=read_next_recirc
---------2---------------------272abbca_cdfc_4dc7_aef7_dedd72160e49-------)

[Zoumana Cisse

](/@zouvier?source=read_next_recirc---------2---------------------
272abbca_cdfc_4dc7_aef7_dedd72160e49-------)

in

[Block Magnates

](https://medium.com/block-magnates?source=read_next_recirc---------2
---------------------272abbca_cdfc_4dc7_aef7_dedd72160e49-------)

## Beating Ethernaut: level 6 Delegation

![](https://miro.medium.com/focal/112/112/72/48/0*MuTUzkDvCSLS1UJd.jpg)](/block-
magnates/beating-ethernaut-level-6-d497213ee5cf?source=read_next_recirc
---------2---------------------272abbca_cdfc_4dc7_aef7_dedd72160e49-------)

[[![Light](https://miro.medium.com/fit/c/40/40/1*PGFt8Ll2bru-
QxN73DTQpQ.jpeg)](/@daniel153282028?source=read_next_recirc---------3
---------------------272abbca_cdfc_4dc7_aef7_dedd72160e49-------)

[Light

](/@daniel153282028?source=read_next_recirc---------3---------------------
272abbca_cdfc_4dc7_aef7_dedd72160e49-------)

## Solidity Modifier

](/@daniel153282028/solidity-modifier-e68a31ec953f?source=read_next_recirc
---------3---------------------272abbca_cdfc_4dc7_aef7_dedd72160e49-------)

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

