[ ![Celestia Blog](https://blog.celestia.org/content/images/2021/10/g16.png)
](https://blog.celestia.org)

  * [All posts](https://blog.celestia.org/)
  * [Learn more](https://celestia.org)

Subscribe

# Celestia: A Scalable General-Purpose Data Availability Layer for
Decentralized Apps and Trust-minimized Sidechains

  * [ ![Mustafa Al-Bassam](/content/images/size/w100/2021/06/mustafa-al-bassam.5755cf7c.png) ](/author/mustafa/)

#### [Mustafa Al-Bassam](/author/mustafa/)

Nov 6, 2019 • 4 min read

One of the highlights of this year’s Devcon 5 was [optimistic
rollups](https://ethresear.ch/t/minimal-viable-merged-consensus/5617), a new
scaling solution that uses the Ethereum base chain for data availability and
enforcement of a two-way bridge of assets, with execution happening off-chain
on layer two. In addition to allowing for increased throughput and decreased
costs for general-purpose smart contracts, it is the first way to scale layer
one sustainably, by avoiding state bloat.

[Fuel Labs recently announced](https://medium.com/@fuellabs/fuel-scaling-
stablecoin-payments-10x-today-50x-in-the-near-future-961e3113b39b) that their
implementation of optimistic rollups is nearing completion, pending security
audits. Their sidechain will enable an increase in transaction throughput on
the order of 50-fold. However even with this impressive increase, it is
bottlenecked by the data availability capacity of its base chain, Ethereum. If
built on top of a chain specifically engineered from the ground up for data
availability, systems like Fuel could easily reach tens or even hundreds of
thousands of transactions per second.

To that end, we’re building the first ever scale-out data availability-focused
blockchain: **Celestia**. At its center is the core mathematical primitive
that makes sharding secure: data availability proofs using erasure codes.
Using this primitive directly, rather than through sharding, allows the
Celestia data availability layer to have the scaling of sharded blockchains
for block verification.

Our long-term vision is to help build a blockchain ecosystem with modular data
availability layers and execution engines that can be integrated together. We
believe that is the next generation of scalable blockchain architectures.

Although developers will be able to build raw applications on Celestia
directly, in the future one may be able to for example create [Fuel
sidechains](https://medium.com/@fuellabs/fuel-scaling-stablecoin-
payments-10x-today-50x-in-the-near-future-961e3113b39b) using Celestia as a
data availability layer. Or [Cosmos zones](https://cosmos.network/) and
[Tendermint](https://tendermint.com/) chains may use Celestia as a data
availability layer to enable those zones to become trust-minimized by using
fraud proofs, potentially giving the Cosmos ecosystem a more uniform level of
security, with reduced reliance on social governance to deal with bad zones.

In addition to increased transaction throughput, another benefit of this
architecture is reduced costs for applications that need a high amount of on-
chain data. For example, consider a [private voting
contract](https://www.youtube.com/watch?v=WMIHyshVZkk) where the public keys
of thousands of participants need to be posted on-chain.

![](https://blog.celestia.org/content/images/2021/06/1-1m9JJ763dSM79Fn-
Zo46tA.jpeg)Left to right: Ismail Khoffi, John Adler, Mustafa Al-Bassam.

First to bat on the Celestia team is [Mustafa Al-
Bassam](https://twitter.com/musalbas), who previously co-founded
[Chainspace](https://chainspace.io), a sharded smart contract platform that
was [acquired by Facebook](https://cheddar.com/media/facebook-blockchain-
acquisition-chainspace). He has written a number of [seminal
papers](http://www0.cs.ucl.ac.uk/staff/M.AlBassam/) whose contributions
underpin the security of sharded blockchain systems, notably a [formal fraud
and data availability proofs scheme](https://arxiv.org/abs/1809.09044).

Also on the team is [John Adler](https://twitter.com/jadler0), a layer two
scalability researcher at ConsenSys working on Phase 2 of Ethereum 2.0. He
created the first specification for an [optimistic
rollup](https://ethresear.ch/t/minimal-viable-merged-consensus/5617) scheme,
drawing inspiration from Mustafa’s earlier works on data availability.

Joining them is [Ismail Khoffi](https://twitter.com/kreuzuquer), a senior
research engineer who has many years of experience ranging from building
academic research prototypes to bringing both blockchain and non-blockchain
systems to production, including at [Tendermint](https://tendermint.com/),
[Google UK](https://www.google.co.uk/), and
[EPFL](https://www.epfl.ch/labs/dedis/).

## The Celestia Design

The core idea of Celestia is to decouple transaction execution (and validity)
from the consensus layer, so that the consensus is only responsible for a)
ordering transactions and b) guaranteeing their data availability. This is the
bare minimum that the consensus layer of a blockchain needs to do in order to
enable useful applications, such as a cryptocurrency. (In the case of proof-
of-stake protocols, a minimal consensus-critical execution layer is necessary
however, in order to determine the validator set, although this may also be
implemented as an optimistic rollup.)

![](https://blog.celestia.org/content/images/2021/06/1-2rj-
RBzjg8_L-q0MocVV-w.png)Overview of Celestia block validity rules.

For example, one can imagine a version of Bitcoin where invalid transactions
are allowed to be posted on-chain, but are simply discarded by clients when
reading the blockchain to determine its state. In this model, the blockchain
is simply used as an ordered messaging protocol, rather than a state machine
replication protocol. Designs such as [optimistic
rollups](https://ethresear.ch/t/minimal-viable-merged-consensus/5617) and [zk
rollups](https://ethresear.ch/t/on-chain-scaling-to-potentially-500-tx-sec-
through-mass-tx-validation/3477) take this idea further by using fraud or
validity proofs to enable clients to ensure the validity of posted
transactions or state transitions, without directly executing each transaction
themselves.

This is similar to [reducing consensus to atomic
broadcast](https://en.wikipedia.org/wiki/Atomic_broadcast#Equivalent_to_Consensus),
which was [first shown to be possible in
1996](https://www.cs.utexas.edu/~lorenzo/corsi/cs380d/papers/p225-chandra.pdf).
This is a departure from the state machine replication paradigm for consensus
that has been popular in distributed systems research over the past several
decades, which is also followed by Satoshi Nakamoto in the [Bitcoin
whitepaper](https://bitcoin.org/bitcoin.pdf).

In Celestia, a block that has consensus is considered valid only if the data
behind that block is available. This is to prevent block producers from
releasing block headers without releasing the data behind them, which would
prevent clients from reading the transactions necessary to compute the state
of their applications.

Celestia reduces the problem of block verification to data availability
verification, which we know how to do efficiently with sub-linear cost using
[data availability proofs](https://arxiv.org/abs/1809.09044). These proofs
utilise a primitive called [erasure
codes](https://en.wikipedia.org/wiki/Erasure_code), which are used in consumer
technologies ranging from DVDs to QR codes to satellite communication.

The proofs require each client to sample a very small number of random chunks
from each block in the chain, and only work if there are enough clients in the
network such that they are collectively sampling the entire blockchain. This
is similar to peer-to-peer file-sharing networks such as BitTorrent, where
different peers may have different pieces of a file.

This leads to an interesting consequence: the more clients you have in the
network, the greater the block size (and thus throughput) you can have
securely. Note that unlike existing scale-out designs such as sharding, in
Celestia the data throughput of the main chain increases with _non-consensus
nodes_. This is a unique and exciting property, as it means nodes that are not
producing blocks can contribute to the throughput and security of the network.

Current layer one scalability designs such as sharding primarily focus on
scaling block production, rather than block verification. The former is
useless without the latter, and we believe the latter is much more important
as incentivised block producers typically have significantly more resources
than ordinary nodes that simply want to verify the chain.

## More Information

For more reading about Celestia, see the following resources:

  * [Celestia research paper](https://arxiv.org/abs/1905.09274)
  * [Celestia Ethereum research post](https://ethresear.ch/t/a-data-availability-blockchain-with-sub-linear-full-block-validation/5503)
  * [Celestia prototype](https://github.com/celestiaorg/lazyledger-prototype)

We’re incredibly excited about this vision. If you are too, you can keep up-
to-date with developments about Celestia by subscribing to the newsletter on
our [website](https://celestia.org), joining our [Telegram
group](https://t.me/CelestiaCommunity), or following our [Twitter
feed](https://twitter.com/CelestiaOrg).

 _Thanks to Zaki Manian for feedback on this post._

## Sign up for more like this.

Enter your email Subscribe

[ ![The Ethereum Off-Chain Data Availability
Landscape](/content/images/size/w600/2022/02/Ethereum-DA-Landscape---header-BP
---FEB-2022---99.jpg) ](/ethereum-off-chain-data-availability-landscape/)

[

## The Ethereum Off-Chain Data Availability Landscape

Blockchains need to guarantee data availability (DA), especially in the case
of rollup and layer 2 (L2) chains. The blockchain data availability problem
goes like this: participants of blockchain networks can get locked out from
interpreting the state or further updating it when block producers advance the
state of the

](/ethereum-off-chain-data-availability-landscape/)

  * [ ![Aditi](/content/images/size/w100/2022/02/Goop-Troop.png) ](/author/aditi/)
  * [ ![John Adler](/content/images/size/w100/2022/02/VLiLY_YO_400x400.jpg) ](/author/john/)

[Aditi](/author/aditi/), [John Adler](/author/john/) Feb 14, 2022 • 4 min read

[ ![Quantum Gravity Bridge: Secure Off-Chain Data Availability for Ethereum
L2s with Celestia](/content/images/size/w600/2022/02/Quantum-Gravity-
Bridge-1-1.png) ](/celestiums/)

[

## Quantum Gravity Bridge: Secure Off-Chain Data Availability for Ethereum L2s
with Celestia

tl;dr: This post introduces the Quantum Gravity Bridge project, a Celestia to
Ethereum data availability (DA) bridge. From the onset of DeFi Summer in 2020,
through the eruption of NFTs in 2021, and now an escalation of DAOs, the
demand for blockspace on Ethereum has exploded. The deadly combo

](/celestiums/)

  * [ ![Aditi](/content/images/size/w100/2022/02/Goop-Troop.png) ](/author/aditi/)
  * [ ![John Adler](/content/images/size/w100/2022/02/VLiLY_YO_400x400.jpg) ](/author/john/)
  * [ ![Mustafa Al-Bassam](/content/images/size/w100/2021/06/mustafa-al-bassam.5755cf7c.png) ](/author/mustafa/)

Multiple authors Feb 8, 2022 • 6 min read

[ ![Celestia Launches Devnet](/content/images/size/w600/2021/12/devent.jpg)
](/celestia-launches-devnet/)

[

## Celestia Launches Devnet

We are excited to announce that we have successfully launched Celestia devnet!
On a cold November day in Berlin, our engineers were huddled in a conference
room clad in Celestia hoodies. Suddenly, they erupted into cheers of elation.
On their computer terminal windows were the following messages: Terminal
output from

](/celestia-launches-devnet/)

  * [ ![Nick White](/content/images/size/w100/2021/06/harmony-headshot-cropped.jpg) ](/author/nick/)

[Nick White](/author/nick/) Dec 14, 2021 • 4 min read

[Celestia Blog](https://blog.celestia.org) (C) 2022

  * [Learn more](https://celestia.org)
  * [Twitter](https://twitter.com/CelestiaOrg)
  * [Discord](https://discord.com/invite/YsnTPcSfWQ)
  * [Telegram](https://t.me/CelestiaCommunity)
  * [GitHub](https://github.com/CelestiaOrg)

[Powered by Ghost](https://ghost.org/)

