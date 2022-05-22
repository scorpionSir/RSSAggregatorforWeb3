[ ![Fuel Labs](https://fuel-labs.ghost.io/content/images/2021/09/logo-
full-1.png) ](https://fuel-labs.ghost.io)

  * [Home](https://fuel-labs.ghost.io/)
  * [About](https://fuel-labs.ghost.io/about/)

[ ](https://twitter.com/fuellabs_ "Twitter")

Subscribe

[Optimistic](https://fuel-labs.ghost.io/tag/optimistic/)

# Announcing the Fuel v0 Open Beta

Scaling arrives all the same…and now it’s here

  * [ ![Fuel Labs](/content/images/size/w100/2021/09/logo.svg) ](/author/fuel-labs/)

#### [Fuel Labs](/author/fuel-labs/)

Jan 20, 2020 • 4 min read

![Announcing the Fuel v0 Open
Beta](/content/images/size/w2000/2021/09/1_R0EINxv5i9ugMnwHndxAnw.png)

A little over two months [we announced](https://medium.com/@fuellabs/fuel-
scaling-stablecoin-payments-10x-today-50x-in-the-near-future-961e3113b39b)
that sustainable scaling would be coming to Ethereum in the form of Fuel, the
most advanced, efficient, and secure optimistic rollup. As of a few days ago,
the long wait is finally over: [our first public testnet is now live, and the
code is open-
source](https://twitter.com/fuellabs_/status/1215366574862938112)! Fuel v0 is
a series of short-lived testnets that test stability and performance, and will
see a series of improvements over the coming months. We’re aiming for
launching a long-lived testnet of Fuel v1 by the end of Q1 2020.

## Fuel v0 Features

⛽ The Fuel v0 testnets will be a series of short-lived testnets as we
iteratively improve performance and stability and add new features (which
we’ll discuss in the next section).

⚙️ Fuel is a highly-optimized version of [Minimal Viable Merged
Consensus](https://ethresear.ch/t/minimal-viable-merged-consensus/5617) (aka
Optimistic Rollup) that is more responsive and cheaper than the original
design, while retaining identical security guarantees. By using Yul instead of
Solidity for low-level memory manipulation, our fraud proofs can execute in
under 1M gas.

🔒 The safety and security of Fuel is __optimal__. With cheap fraud proofs, it
is highly-resilient against chain congestion attacks, unlike Plasma and state
channel networks. As with any properly-design optimistic rollup, the only way
to attack it is for miners to conduct a week-long 51% attack on the main chain
— highly visible, easily attributable, and impossible in practice for a chain
as important and secure as Ethereum.

🔀 Rather than the accounts data model used by Ethereum, Fuel uses the UTXO
data model similarly to Bitcoin. This allows for parallelizable transaction
verification and, more importantly, provides substantially more efficient
state access patterns. As a consequence, Fuel full nodes don’t require [a fast
SSD](https://twitter.com/ercwl/status/1164202440952074241). Both ether and
tokens are supported through the use of colored coins (yes, those are finally
happening, and not on Bitcoin).

⚡ To eliminate the hassle of a one-week withdrawal delay for funds that
channels, Plasma, and vanilla optimistic rollup are burdened with,
transactions on Fuel can also send funds to HTLCs, which allow for atomic
swaps. When combined with a liquidity provider network, users can [instantly
withdraw their funds](https://ethresear.ch/t/trustless-two-way-bridges-with-
side-chains-by-halting/5728), potentially in as quickly as a single block.
This also opens yet another door for liquidity providers to earn returns on
their ether and tokens completely trustlessly.

🦄 Thanks to the use of the UTXO data model over the accounts data model,
transfers that swap funds between two parties can be constructed. This means
scalable and completely non-custodial exchanges can be built on top of Fuel,
with only order matching happening off-chain.

⚙️ By moving state and state accesses completely off-chain, optimistic rollup
is __sustainably scalable__. Uncontrolled state growth is [the largest problem
and bottleneck facing Ethereum
today](https://blog.ethereum.org/2019/12/30/eth1x-files-state-of-stateless-
ethereum). Fuel eliminates this problem in practice completely __today__ ,
without having to wait for Eth 2.0 or stateless Ethereum.

🤷 One key principle that we will defend to the death is that Fuel is — and
will always be — completely tokenless. [Tokens are not necessary to secure an
L2](https://medium.com/@adlerjohn/the-why-s-of-optimistic-
rollup-7c6a22cbb61a): that’s what the Ethereum chain is for after all. Tokens
for L2 systems serve no functional purpose, they exist only to enrich the
developers and their investors at the cost of higher friction and additional
rent-seeking for users. Fuel on the other hand is completely permissionless
and non-custodial. Our block production model is a __priority aggregator__ ,
namely that we have a short period of time where we have exclusive access to
including transactions in blocks.

⏩ Tired of waiting 6–12 second for the next Ethereum block that will secure
the next Fuel block? We support instant trusted transactions: if you, the
receiver __choose__ to trust us until the next block, you can accept a
received transaction as valid. You’ll receive signed cryptographic proof from
both the transaction sender and us, so any double-spending on our part would
be provably attributable. Unlike other scaling projects that use a shared bond
pool for instant transactions — [which doesn’t actually add any
safety](https://twitter.com/jadler0/status/1184015361475108864) — and
obfuscate risks by describing attacks as “inconvenient” to pull off, we make
our trust relationships explicit so that users can make informed choices.

😸 Our code is now open-source under the Apache 2 license. Check it out
[here](https://github.com/FuelLabs).

## Future Improvements

We have a number of improvements to both our Fuel optimistic rollup chain and
surrounding tooling planned.

We’ll soon be releasing Yul+, which builds upon the
[Yul](https://solidity.readthedocs.io/en/latest/yul.html) intermediate
language by adding in-memory structures, enums, constants, and other Quality-
of-Life improvements. This allows contracts with lots of memory accesses
(anything that will deal with calldata a lot, such as all rollups) to be
written in a readable manner while remaining extremely gas-efficient.

A Bitcoin-like predicate scripting system with covenants is in this works.
This will enable a whole multitude of smart contract applications on Fuel, all
while retaining the performance gains of the UTXO data model over the accounts
data model.

The only performance advantage of zk rollups over optimistic rollups is that
the former can get away with not posting witness data (i.e. transaction
signatures) on-chain. With BLS aggregate signature schemes, this advantage
disappears completely and optimistic rollups are in fact __more__ scalable
than zk rollups. We are actively researching cutting-edge signature
aggregation schemes that combine numerous desirable properties.

Given that optimistic rollups can be thought of as a form of transactions
batching, we can build highly scalable and decentralized social networks on
top of Fuel! Twitter, Reddit, you name it, can all be built as uncensorable
and completely open social networks that can leverage Ethereum’s money legos
and DeFi ecosystem.

## Wrapping Up

This is just the beginning. We have big plans for the future of Fuel and the
promise of highly-scalable stablecoin payments — and other usecases — it
brings to the table. If you’d like to support our R&D efforts, consider
contributing [to our Gitcoin grant](https://gitcoin.co/grants/199/fuel-labs).

In the meantime, for more info and to keep up to date with our work:

Website: [https://fuel.sh](https://fuel.sh/)  
Twitter: https://twitter.com/FuelLabs_  
GitHub: <https://github.com/FuelLabs>

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

