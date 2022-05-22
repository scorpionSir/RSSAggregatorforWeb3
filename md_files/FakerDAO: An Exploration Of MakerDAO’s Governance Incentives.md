  * [Home](/)
  * [Contact](/contact)
  * [Services](/services)
  * [Projects](/projects)
  * [Community](/community)
  * [Blog](/blog)

Menu

#  [![ScopeLift](//images.squarespace-
cdn.com/content/v1/54b81e72e4b0fee4b01a42e9/1581018368646-GMT0JDHOVLSGDECYFQVQ/SCOPELIFT-
long-cropped.png?format=1500w)](/)

Street Address

Philadelphia, PA

Phone Number

Your Custom Text Here

# [![ScopeLift](//images.squarespace-
cdn.com/content/v1/54b81e72e4b0fee4b01a42e9/1581018368646-GMT0JDHOVLSGDECYFQVQ/SCOPELIFT-
long-cropped.png?format=1500w)](/)

  * [Home](/)
  * [Contact](/contact)
  * [Services](/services)
  * [Projects](/projects)
  * [Community](/community)
  * [Blog](/blog)

#  [FakerDAO: An Exploration Of MakerDAO’s Governance
Incentives](/blog/fakerdao)

March 9, 2020 [Ben DiFrancesco](/blog?author=54b81e71e4b06e38ad58f2f2)

The MakerDAO project is one of the most interesting experiments in the crypto
space. It pushes boundaries along multiple dimensions. Perhaps the most
overlooked aspect of the project, at least until recently, is its governance.

Somehow, we seem to forget the “DAO” aspect of MakerDAO. Yet the decisions
made by MKR token holders— a fluid community spread throughout the world— are
some of the highest stakes votes in all of crypto. The Maker contracts secure
well over half a Billion dollars of collateral, backing loans that yield
nearly 150 Million dollars worth of the Dai and Sai stablecoins.

Countless other decentralized finance projects also integrate with Maker. From
usage of Dai for payments, to reliance on the Dai Savings Rate to yield
interest, a huge swath of Ethereum’s emerging DeFi ecosystem depends on the
project.

A conservative estimate would be that over a Billion dollars worth of value
hinges on the sound decision making of the MKR token holders in their
executive votes. The case could be made for several Billion.

This post introduces a simple smart contract construction that demonstrates
why the MakerDAO governance model, as currently conceived, may not be
incentive compatible with the long term health of the Maker ecosystem. We have
written this contract not to attack Maker, but to harden it.

We want to see Maker succeed, and [in the
words](https://twitter.com/AaveAave/status/1229407777593778177) of Mariano
Conti, “if it can be done, it will be done, and we need to prepare for it.” In
fact, Mariano’s experiment with
[SelloutDAO](https://twitter.com/nanexcool/status/1168640894947471360), a one-
time experiment for auctioning MolochDAO governance rights, was part of the
inspiration for FakerDAO.

If contracts like ours represent a challenge to the long term stability of
Maker & Dai, it’s best to discuss the issue as soon as possible and search for
solutions together.

## Introducing FakerDAO

Today we are [open sourcing](https://github.com/ScopeLift/fakerdao) the
FakerDAO contracts & frontend, which we’ve also deployed to the Kovan testnet
and made available at [kovan.fakerdao.com](https://kovan.fakerdao.com/).
FakerDAO is a minimum viable implementation of a straightforward concept:
pooling MKR tokens and selling their voting power to the highest bidder.



[ ![FakerDAO UI running on the Kovan testnet at
kovan.fakerdao.com](https://images.squarespace-
cdn.com/content/v1/54b81e72e4b0fee4b01a42e9/1583942850347-ZT5UXRNQZL8DDNCDQIMY/fakerdao-
screenshot.png) ](https://kovan.fakerdao.com)

FakerDAO UI running on the Kovan testnet at
[kovan.fakerdao.com](https://kovan.fakerdao.com)



Here are some of the details of FakerDAO.

  * Any MKR holder can lock their tokens in the contract.

  * Every seven days, the contract holds an auction in which anyone can submit bids denominated in ETH¹

  * The highest bidder wins the right to control the MKR locked in the contract for the next seven days.

  * MKR depositors are paid out after each auction for the proportion of the MKR they contributed.

  * At the end of each cycle, MKR withdraws/deposits are permitted, and the process starts again.

Maker uses a voting system referred to as “approval voting.” Token holders can
choose up to 5 candidate proposals to vote for. They then stake their tokens
to signal their approval for that “slate” of candidates. The proposal with the
highest total stake at any time can be activated by anyone.

FakerDAO allows the winner of the most recent auction to choose which
proposals the deposited MKR will support. The amount of MKR available to the
winner is fixed for five days after the auction. At the end of five days,
there is a one day deposit/withdrawal period, during which the MKR available
may fluctuate up or down. After the deposit/withdrawal period, a one day
auction period determines who will control the MKR next.

You may be wondering, why would a MKR holder deposit into the FakerDAO? The
answer is simple: to earn a return on their MKR holdings.

Similarly, why would anyone bid to win the auction? As you’d guess, it’s to
gain control of voting power at a cost well below that of actually buying the
tokens. This could be for benevolent reasons (i.e. to support a proposal they
believe is best for the Maker ecosystem), or for malicious ones (i.e. to use
the voting power to attack the system in some way, including in the worst
case, to drain the collateral).

The FakerDAO contract makes no value judgements about any of its participants
or their intentions. It’s just code.

## The Free Rider Problem

Just because it’s possible for MKR holders to auction their voting power
doesn’t mean they will. Let’s examine the incentives.

The reasons for holding MKR tokens are twofold:

  1. To earn a return on MKR when it appreciates in value, i.e. a speculative investment

  2. To gain the right to participate in governance signaling

The system is designed to align and reinforce these two motivators. If the MKR
holders make good decisions, and the system functions correctly, then MKR is
burned in the process. As the total supply of MKR decreases, both the voting
power and the value (in theory) of the remaining tokens will increase.

While cleverly designed, the system is susceptible to so-called free riders.
Participating in governance takes effort. It involves following the proposals,
understanding their impacts, weighing arguments for and against given changes,
and staking tokens accordingly.

In theory, this effort might be “worth it” if one’s participation helps the
DAO make good decisions and the system flourishes. The obvious issue is that a
MKR holder who goes through all this effort receives the same reward as one
who didn’t.

There is clear evidence of this dynamic already taking place. There are
currently about 218,000 MKR signaling governance support of some kind, out of
the 987,000 in the total supply. This means nearly 80% of existing tokens are
sitting on the sidelines.

## Worse Than Free Rider

The free rider problem is made worse by the possibility of contracts like the
one we’ve presented here. By depositing their MKR into FakerDAO, passive
holders not only stand to make the same gains (through appreciation) as those
who actively participate in governance, they stand to earn **more** than
active governance participants by extracting a rent from their tokens.

There is one technical detail that is critical to understand here. MKR tokens
must be locked in the governance contract to signal approval. Therefore, any
revenue generating use of the tokens, such as depositing in FakerDAO, is
precluded by participation in governance. Active governance is now strictly
less profitable than passive holding, even **before** considering the time and
effort required to participate.

In fact, the situation is even worse than this. FakerDAO depositors aren’t
just doing _nothing_ , their actions detract from the security of the system.
The price of purchasing voting power from FakerDAO would presumably remain
well below the price of purchasing the tokens outright. Thus, FakerDAO
depositors reduce the security of the Maker system by decreasing the cost for
a would-be attacker.

## Incompatible Incentives

In the final analysis, the situation appears to be something like a prisoner's
dilemma combined with the free rider problem:

  * The best outcome for the protocol, and thus for MKR holders as a whole, relies on a large percentage of MKR holders participating actively, exercising prudential judgement, and staking their tokens to enact good governance decisions.

  * The best outcome for any individual MKR holder is achieved by ignoring governance altogether and extracting rents from their tokens, weakening Maker’s security in the process.

How will MKR holders behave when their own best interest is at odds with the
system as a whole? Game theory suggests that in the long term, this dilemma
will cause Maker’s governance to tend toward minimal participation and
compromised security.

As stated at the outset of this post, we are fans of Maker. We want it to be
successful. In that vein, we’ve developed FakerDAO and written this post in
the hopes of highlighting a potential shortcoming in its governance structure.

Are our conclusions incorrect? We’d love to hear why! If not, what can be done
to harden the project long term against such scenarios? We have some ideas
ourselves, but we’d love to hear yours.

* * *

¹ In fact, the contract can be deployed with any ERC20 as the bidding token.
To accept ETH, you would use WETH.

 _This article, and the FakerDAO contract source code, were co-authored by_[
_Matt Solomon_](https://twitter.com/msolomon44) _and_[ _Ben
DiFrancesco_](https://twitter.com/BenDiFrancesco) _of_[ _ScopeLift_](/home)
_._

[<- Introducing Umbra – Privacy Preserving Stealth Payments On The Ethereum
Blockchain](/blog/introducing-umbra)[All In On Crypto: ScopeLift's Next
Chapter ->](/blog/all-in-on-crypto-scopelifts-next-chapter)

[ ](https://twitter.com/BenDiFrancesco) [ ](https://github.com/apbendi) [
](https://www.linkedin.com/pub/ben-difrancesco/9b/426/680)

© ScopeLift 2021

