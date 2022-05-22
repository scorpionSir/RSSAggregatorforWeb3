[ ![Fuel Labs](https://fuel-labs.ghost.io/content/images/2021/09/logo-
full-1.png) ](https://fuel-labs.ghost.io)

  * [Home](https://fuel-labs.ghost.io/)
  * [About](https://fuel-labs.ghost.io/about/)

[ ](https://twitter.com/fuellabs_ "Twitter")

Subscribe

# Fuel: Scaling Token Payments 10x Today, 50x in the Near Future

A future with sustainable, trustless scaling for Ethereum

  * [ ![Fuel Labs](/content/images/size/w100/2021/09/logo.svg) ](/author/fuel-labs/)

#### [Fuel Labs](/author/fuel-labs/)

Oct 22, 2019 • 4 min read

![Fuel: Scaling Token Payments 10x Today, 50x in the Near
Future](/content/images/size/w2000/2021/09/1_UyUzXRciZt6sx6x7qD_ZOQ.png)

Two months ago, a small group of Ethereum engineers and researchers got
together to work on what would later be [popularized by Vitalik
Buterin](https://vitalik.ca/general/2019/08/28/hybrid_layer_2.html) as
__optimistic rollups__. Our work was based on the research and efforts of the
ConsenSys researcher [John Adler](https://twitter.com/jadler0), who spec’ed
out the technique as a viable scalability solution [several months
prior](https://ethresear.ch/t/minimal-viable-merged-consensus/5617). He
described a scalability approach on Ethereum that involved no consensus
changes to layer-1, and could be implemented right away to help relieve
Ethereum’s [state bloat
issue](https://twitter.com/technocrypto/status/1185745186611175424) caused
primarily by [ERC-20 token (and specifically, Tether stablecoin)
transfers](https://ethgasstation.info/). After a few in-depth conversations,
we began working hard to put together a realistic Ethereum scaling
implementation that could solve a single problem: sustainably scalable, cheap,
and reliable stablecoin payments on Ethereum:
[**Fuel**](https://docs.google.com/presentation/d/14eZOHvtII2unipjM-
wMLgKTBAi0bBPPYaBSWN37SIT0/edit?usp=sharing).

We believe the killer app for any blockchain is ****Stablecoin Payments****.
If a blockchain can master this, [it can add tremendous value to the global
economy](https://www.zerohedge.com/crypto/speculative-case-1000-eth-if-
ethereum-valued-fiat-payment-fintech-platform) with [far reaching
implications](https://www.zerohedge.com/crypto/g7-panics-says-global-
stablecoins-pose-threat-financial-stability). [Fuel](https://fuel.sh/) is
focused on addressing this on Ethereum in the form of an simplistic optimistic
rollup style approach.

## Sustainable Scaling for Ethereum

As we’ve seen time and again, the transaction throughput on Ethereum is
severely limited: capable of fewer than ~10 fresh ERC-20 transfers per second.
The reason for this limit is largely due to __state__ (i.e. the account
balances and contract storage slots). Ethereum’s uncompressed state size is
[on the order of 45
GB](https://twitter.com/jadler0/status/1166730856796495872), much too large to
fit into RAM, which results in a large number of disk accesses, especially
when processing token transfer.

Ever-increasing state bloat [is the number-one problem for Ethereum at this
time](https://twitter.com/jadler0/status/1174482002755629057), as state,
unlike history, is not prunable. We ideally want to scale Ethereum __without__
increasing state bloat or state accesses. This can in fact be accomplished
quite easily by using transaction calldata! By simply “posting” a sidechain’s
transaction data and Merkleizing it on-chain, we can almost completely
eliminate state access from the Ethereum base layer while simultaneously
scaling it sustainably (i.e. without egregious recurrent or long-term costs
for full nodes).

## Optimistic Rollups?

Fuel builds upon Adler’s seminal post on [Minimal Viable Merged
Consensus](https://ethresear.ch/t/minimal-viable-merged-consensus/5617), which
introduced a concrete minimal spec for trustless permissionless sidechains
with on-chain data availability and correctness enforced with fraud proofs
(now commonly “optimistic rollups”).

> Devcon5 in a nutshell. [pic.twitter.com/tzE4nuuzsf](https://t.co/tzE4nuuzsf)
>
> -- PhABC (@PhABCD) [October 15,
> 2019](https://twitter.com/PhABCD/status/1184220223693557762?ref_src=twsrc%5Etfw)

Optimistic rollups has several properties and guarantees that distinguishes it
from earlier scaling proposals, such as [shadow
chains](https://blog.ethereum.org/2014/09/17/scalability-part-1-building-top/)
or [Plasma](http://plasma.io/). Unlike shadow chains, it does not apply state
transition on-chain unless someone explicitly pays to do so, at cost —
applying all state transitions automatically would lead to state bloat, the
exact problem we’re trying to avoid! Unlike Plasma, it is
[permissionless](https://twitter.com/jadler0/status/1164176326829457412) and
makes use of [non-interactive fraud
proofs](https://twitter.com/jadler0/status/1184464445596147712) so as to be
[highly resistant to chain congestion
attacks](https://twitter.com/jadler0/status/1164177536495919104).

## Fuel: A High Level Overview

The Fuel sidechain is designed exclusively handle large volumes of payments on
Ethereum, and will reduce the cost Ethereum ERC-20 token transfers (at
conservative estimates) by 5-fold pre-Istanbul. Unlike channels [it does not
promise instant
finality](https://twitter.com/jadler0/status/1184015361475108864), but does
provide trustless and cheap transactions at Ethereum blocktime finality
without the high barrier of full pre-collateralization requirements that
channels have. The Fuel chain addresses instant finality by offering a semi-
permissionless operator model that allows, so long as the primary block
committer is trusted until Ethereum block finality, transactions to be
considered final and instant.

>  _ _ ** **The Fuel chain enables a Burner wallet-like experience****__

One of the primary use-cases for Fuel will be to alleviate the enormous gas
cost burden of moving token funds to/from exchanges. This would immediately
drop their out-bound costs by at least 5-fold, without [lowering the value of
underlying ERC-20 token
assets](https://twitter.com/gakonst/status/1146793715333251072). Additionally
Fuel can be used, with centralized order book matching, to perform trustless
and non-custodial native atomic exchanges.

To maximize its client-side scaling profile, Fuel uses a parallelizable UTXO
data model, that any computer or phone should be able to validate easily. Our
current estimates pre-Istanbul show our chain raising Ethereum’s total
transaction per second potential ****(TPS) to around 50**** , a far greater
volume than our current ~10 for ERC-20s (a 5-fold increase). Post-Istanbul
(with the inclusion of [EIP-2028](https://eips.ethereum.org/EIPS/eip-2028)) we
believe we can push the limit even further going to around 200 TPS. With some
[trivial upgrades to layer-1](https://eips.ethereum.org/EIPS/eip-2242) we can
push this number to the high 2000s. Furthermore, with the single integration
of [erasure code data availability proofs to
Ethereum](https://ethresear.ch/t/on-chain-non-interactive-data-availability-
proofs/5715) Ethereum’s TPS can be scaled quadratically, to on the order of
10s of thousands to millions of TPS.

## Fuel Key Takeaways

  * Optimistic rollup sidechain on Ethereum
  * UTXO data model
  * Finality at Ethereum blocktimes
  * Optional Burner-like instant transaction experience
  * Operator cannot censor transactions
  * Supports any ERC-20 Token / Ether (with focus on Dai/Tether)
  * Trustless and decentralized
  * Client-side parallalizable validation (browser friendly)
  * Focused on cheap ERC-20 transactions
  * Enter and exit freely anytime using atomic swaps and liquidity providers
  * No collateral or inbound liquidity requirements for users
  * In the future we will work toward scaling quadratically to millions of TPS

## Wallet Integrations

We are designing Fuel to be developer friendly, integration will simply be
adding a library that handles deposits, withdrawls and UTXO data. Any Ethereum
account and contract can handle Fuel transactions so long as they can either
sign or send arbritary transactions. Contract wallets will see less of gas
savings of Fuel, but will still see some significant cost reduction in token
transfer cost.

## Further Background Reading

  * [Slides from our EthPlanet Pre-DevCon V Lightning Talk](https://docs.google.com/presentation/d/14eZOHvtII2unipjM-wMLgKTBAi0bBPPYaBSWN37SIT0/edit?usp=sharing)
  * [Minimal Viable Merged Consensus](https://ethresear.ch/t/minimal-viable-merged-consensus/5617)
  * [Compact Fraud Proofs for UTXO Chains Without Intermediate State Serialization](https://ethresear.ch/t/compact-fraud-proofs-for-utxo-chains-without-intermediate-state-serialization/5885)
  * [On-Chain Non-Interactive Data Availability Proofs](https://ethresear.ch/t/on-chain-non-interactive-data-availability-proofs/5715)
  * [Multi-Threaded Data Availability On Eth 1](https://ethresear.ch/t/multi-threaded-data-availability-on-eth-1/5899)
  * [EIP-2242: Transaction Postdata](https://eips.ethereum.org/EIPS/eip-2242)

## What’s Next?

Our Ethereum smart contracts and in-browser client are currently undergoing
security audits before a mainnet release. For more info, check out the
following links and follow us on Twitter
[@FuelLabs_](https://twitter.com/FuelLabs_) for updates and ****participation
in our upcoming testnet**** and our ****formal specification release****.

Website: [https://fuel.sh](https://fuel.sh/)  
Twitter: <https://twitter.com/FuelLabs_>  
GitHub: <https://github.com/FuelLabs>

****Also stay tuned for our own custom scripting system based on UTXO
predicates, which will enable smart contract functionality on the Fuel
sidechain.****

For further technical inquiries you can tweet at our core developer
[@IAmNickDodson](https://twitter.com/iamnickdodson)  

## Sign up for more like this.

Enter your email Subscribe

[ ![Beyond Monolithic Online
Hackathon](/content/images/size/w600/2022/05/BeyondMonolithicHackathonLQ.png)
](/beyond-monolithic-hackathon/)

[

## Beyond Monolithic Online Hackathon

Be a part of the next generation of blockchain by building dapps using the
Sway smart contract language on Fuel, the Fastest Modular Execution Layer, for
a chance to win up to $100,000 in prizes!

](/beyond-monolithic-hackathon/)

  * [ ](/author/ruben/)
  * [ ![Fuel Labs](/content/images/size/w100/2021/09/logo.svg) ](/author/fuel-labs/)

[Ruben Amar](/author/ruben/), [Fuel Labs](/author/fuel-labs/) May 8, 2022 • 3
min read

[ ![Meet the team behind Fuel](/content/images/size/w600/2022/03/JohnA.png)
](/meet-the-team-episode-1/)

[

## Meet the team behind Fuel

For the first episode of our "Meet the team behind Fuel" series, we are
thrilled to hear from John Adler, Co-founder of Fuel Labs and Celestia Labs.

](/meet-the-team-episode-1/)

  * [ ](/author/ruben/)
  * [ ![Fuel Labs](/content/images/size/w100/2021/09/logo.svg) ](/author/fuel-labs/)

[Ruben Amar](/author/ruben/), [Fuel Labs](/author/fuel-labs/) May 4, 2022 • 2
min read

[ ![Introducing Fuel - The Fastest Modular Execution
Layer](/content/images/size/w600/2022/04/Fuel_Trailer_Still_10.jpeg)
](/introducing-fuel-the-fastest-modular-execution-layer/)

[

## Introducing Fuel - The Fastest Modular Execution Layer

Today, we introduce the fastest modular execution layer: Fuel, adding a new
chapter to the blockchain scalability story.

](/introducing-fuel-the-fastest-modular-execution-layer/)

  * [ ![Fuel Labs](/content/images/size/w100/2021/09/logo.svg) ](/author/fuel-labs/)

[Fuel Labs](/author/fuel-labs/) Apr 18, 2022 • 4 min read

[Fuel Labs](https://fuel-labs.ghost.io) (C) 2022

[Powered by Ghost](https://ghost.org/)

