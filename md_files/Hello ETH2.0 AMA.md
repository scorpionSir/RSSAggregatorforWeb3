[![logo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAICAYAAAD5nd/tAAAACXBIWXMAAA7DAAAOwwHHb6hkAAABj0lEQVQoz12Sv0vDQBTHT0HrD4QWRJRLi3QQOojon1JxUhcFQQeViknrJjiIglgRhW4OTiLSWXB10MnJoToI0lp6ESu1TZNc/L7LFcGDD+8u4X3y3r0wKeUUeAqwEBVYZa9amhCb0bydjbdti/vAsy0jALPYp0EZSODq91W8W2AQPGqZg9CUvkvGUv08fSEywwGESDIaoAW+QQHJbWEq+Y+mqc8OCV3wASZBzP+qJJ8ZY2JrpKgqMvk8Yh8kvL6b6sZ+WZicki/BIBgFUVCk5ywsTr4ikvxI+l4F+w20e21bcQiNGUiZ2OZdSGLYr+jW9+hcw3NUx/DBY6pSCcELZCQ8RMtvOK+K9aErO5ugCqdJCDESVVzSwgMSQhLRwjMl1C1Xw+H4Mf/zPQFhxN5J3qrEbGJRmGMDwjIMYfF+yDNauK+FvVp4qlqG6F4PpY3goMIWxebdiVdbi1CiDC+dtwBdfmcA+X/CQqflFGQP6nf5+20C6blB4yYnRW7chcihCYbwFk0ZzAES9eiIq+DiFyR9m3ZUxiupAAAAAElFTkSuQmCC)![logo](/static/9c635c914229a850d1a9fd284014bdd0/65e33/eco_logo.png)](/)

  * [新闻资讯](/)

  *   * [零时学院](/c0llege)

  * [开发者门户](/develop)

  * [生态漫游](/ecos)

Ξ

Search by [](https://www.algolia.com/?utm_source=react-
instantsearch&utm_medium=website&utm_content=&utm_campaign=poweredby)

## Hello ETH2.0 AMA

Original version of 「Hello ETH2.0 」AMA!

* * *

E

ECN 2020-08-16

 **Hi there 🙂**

ECN finally lands on Medium, with our first Ask-Me-Anything summary script.
The #Hello, ETH2.0# AMA lasted for 2.5 hours from 21:00 pm to 23:30 pm (UTC+8)
last night, livestreamed on WeChat in English & Chinese and also on Twitter in
English documentation. It’s really informative and insightful as an Ethereum
2.0 primer, with five eth buidlers from the wide ecosystem spectrum.

* * *

  

# Guests

  * Afri Schoedon, Pioneer of ETH2 Multi-Client Testnets
  * Raul Jordan, Co-founder of Prysmatic Labs
  * Steve Guo, CTO of Loopring
  * A Jian, Editor of EthFans
  * Jason, Unitimes Community Partner

#  

# Topics

Eth2 launch roadmap / multi-client testnets / layer2 scalability / PoS /
community building

* * *

#  

# Q&A

_Note: the answers from Steve, A Jian and Jason are translated from Chinese
into English by ECN. In case of any discrepancy, the Chinese version shall
prevail._

**Q1** Ethereum has been interesting and exciting global users with its rapid
growth. Now with the long-anticipated milestone getting closer, the calls for
Ethereum 2.0 are growing louder. Could you explain what Ethereum 2.0 looks
like in plain words? How does it differ from current eth1 main chain?

**Raul:**

To me, eth2 is a total redesign of the Ethereum blockchain to maximize for
decentralization, censorship resistance, and scalability at the same time. It
takes all the earnings we have had over the past few years and turns them into
a much more sustainable approach to achieve its original goal of becoming a
“world computer”.

**A Jian:** (translated)

Danny Ryan said “eth2.0 is built for Ethereum, and finally it will become
Ethereum itself”. Ethereum 2.0 is to build the base layer of the next-
generation Ethereum blockchain ecosystem.

Eth2 differs from the current Ethereum in two respects: 1) use PoS (Proof of
Stake) algorithm to drive the blockchain operation; 2) to improve scalability
by “beacon chain + multi-shard chain” architecture.

In plain words, blocks in eth2 are not produced by PoW miners, but confirmed
and finalized by stakers who deposited their ETH. Besides, “beacon chain +
multi-shard chain” architecture separates the state inside PoS and that of
transactions. Instead of executing transactions, beacon chain will handle
finalization and communicate with shards. Shards could be considered as
complicated blockchains resembling the current eth1 chain, which excute
transactions.

**Q2** It’s been years since Ethereum 2.0 plan was initiated. There are many
opinions and wild guesses occurring across the community about its official
launch time. Could you share with us the current development progress of
Ethereum 2.0? What are the major challenges to be solved? And when do you
expect Ethereum 2.0 to go live?

**Afri:**

It’s good to talk about launch roadmap without coming up with a concrete
dates. One could say it’s January the 3rd or July the 30th. But the truth is,
it won’t be neither of the dates. We cannot tell when the mainnet genesis will
happen. This is because there are so many moving parts.

But I can give a realistic view on the open issues and milestones. First of
all, **all clients have to implement the final version of the spec, v0.12.1.**
Currently only one client has a release out currently, and the other four
clients are still working towards a stable release. We will see a first multi-
client testnet with the final v0.12.1 spec be launched potentially end of this
month.

If this goes well, we will be able to prepare the public multi-client testnet
launch under mainnet conditions early July. This is the long awaited
milestone, sometimes mistakenly referred to as “official” multi-client
testnet. **But if it goes well, we can do the final public testing in July.**

There might be a couple of smaller developer testnets on the side, but the
main focus should be the public one. **If the public multi-client testnet
turns out to be stable over the period of two or three months, we can start
working towards a real mainnet launch.**

First of all this requires a deposit contract. A ceremony to determine the
contract that is to be used as the one and only bridge to ETH2 deposits needs
to be held. How this will look like is not entirely defined yet. I know Carl
is preparing that. We should ask him soon. **I expect the earliest possible
date for such a ceremony would be end of August or rather mid September.**

**Once the ceremony is done and the contract is deployed, technically the rush
into ETH2 has officially started.** Even without official launch date, people
could start making the first validator deposits on the ETH1 chain as this is
an entirely permissionless process.

**I would suggest to schedule the minimum genesis time for the beacon chain
mainnet to be exactly 90 days after the genesis time of the official multi-
client testnet.** This would give us 8 weeks of testing and 4 weeks of buffer
time in case we would have to fix something.

Regardless of the deployed deposit contract, we can always push back the
genesis time for mainnet if needed. But given the steps outlined above, the
earliest possible mainnet genesis time would be somewhere in October. This
does not take into account that **we need at least 16k deposits before we see
a mainnet genesis event.** This could additionally take some weeks to ramp up.

So, to sum up…. **November if everything goes well.** October if we are very
optimistic and pushy about the date. Pessimisticly speaking, it would be 2021
in case anything needs to be patched in the spec and adapted by all clients….
I don’t think we will launch in December.

**Q3** (1/3) Interoperability has been one of Ethereum’s edges. The question
for Raul is that by far is there anything more happening around client
interoperability? And why client interoperability matters so much to eth2?

**Raul:**

Client interoperability matters so much because that’s the way we can **catch
critical bugs in a single implementation.** For example, if all of eth2 ran
using our Prysm implementation, we would never find a critical problem
regarding validator rewards and penalties that we have found thanks to client
interoperability.

**(2/3)** The multi-client testnet is considered to be the ultimate hurdle
before we see real eth2. As the initiator of eth2 multi-client testnets
Schlesi and Witti, could Afri share with us the primary targets of multi-
clients, and Witti’s current running state?

**Afri:**

The first phase of Ethereum 2.0, the phase 0, is the beacon chain. The old
ETH1 clients will not be able to run a beacon chain. **For the first time, a
variety of newly implemented clients will be working together on a brand new
blockchain with a new, unique approach to networking and consensus.**

Before such a mainnet can be launched, we need testnets that mimic mainnet
conditions as good as possible. **This requires us to have stable, long-term,
and persistent testnets up and running that are supported by not only one
client but multiple clients, ideally, all clients.** The Schlesi testnet was
one of many steps in that direction, the Witti testnet is another, and soon we
will launch Altona.

Witti is running fairly stable. It currently has seen around 150k slots and
good livelyness. The participation rate of validators is hovering at 71%.

All clients still experience bugs and introduce new optimizations. I suspect
we **still need a lot more multi-client testing.**

**(3/3)** One more question for Afri. It’s said that the final multi-client
testnet has to remain stable for at least 2 months before beacon chain
release, so what are the indicators for stability measurement? When is the
public multi-client testnet expected to go live?

**Afri:**

Indicators for stability are: **no consensus issues and no permanent forks
obviously, all clients should agree upon the correct chain.** Also, we need to
finalize proper networking, there are a lot of rough edges and hiccups between
the different clients. I hope we can ban ENR into the backend of the clients
before we launch and have proper multi-address format for wiring nodes.

Further indicators are **attestations and validator activity.** If we maintain
**above 80–90% activity** and the chain **stays in perfect liveliness with
high finality** , we should be good to go.

As I outlined earlier, **the soonest possible launch date for a public multi-
client testnet would be mid-July.**

**Q4** (1/2) After the official launch of eth2, with the support of layer1
solutions like PoS and sharding, Ethereum is heading into a new scalability
epoch.The adoptions of Rollup techniques fuel the transaction speed while
reducing the transaction fees significantly, bringing much better experience
to users. As the CTO of Loopring, the first and ever decentralized protocol
with working ZK-Rollup, could you please describe how is ZK-Rollup designed to
optimize our user experience?

**Steve:** (translated)

Zk-Rollup is a scalability solution applied to Ethereum, often known as a
layer2 solution. It can support more transaction processings with faster speed
and lower cost. **It executes all computations off-chain and only needs to
submit a small zero knowledge proof (cannot be faked) to verify.** Since the
proofs will be verified on Ethereum, and sufficient data will be stored to
clarify the sate of off-chain accounts, **ZK-Rollup will share the same
security level as Ethereum.**

Loopring chose zkSnark as its zk proof framework (tested by ZCash for years),
with smallest verifying data size so far, which means lowest on-chain cost.
And zkSnark doesn’t require many off-chain computing resources to generate
proofs.

![](https://i.ibb.co/LQ50yGM/AMA-1-19a5159578.pnghttps://i.ibb.co/LQ50yGM/AMA-1-19a5159578.png)

cr: Loopring

There is a relayer system in ZK-Rollup. First, the relayer will organize all
account information off-chain into a Merkle tree where the hashes are computed
in pairs until we get the Merkle root hash. Given that any change in arbitrary
leaf value results in different root hash, the root hash will be the only
display of the whole tree’s current state.

Then the relayer will collect a transaction set（transfer or buy&sell）off-chain
and generate zk proofs for those transactions. The proof generation process:
the last stored root hash R1; every transaction is signed by users; update the
Merkle tree according to those transactions, and verify the changes; get the
updated root hash R2.

Finally, the relayer submits critical data (e.g. balance), zk proof and
updated root hash R2 onto the blockchain. The pre-deployed smart contract will
verify if the proof is valid based on the recorded root hash R1 and
transaction data input. If it’s valid, the root hash R2 can be updated because
the relayer has conducted honest changes to the off-chain Merkle tree.

Here lies the key point of this scheme: **it slashes the resources consumption
and improve the overall blockchain performance by only keeping data storage
and zk proof verification on chain, and moving computations off chain.** And
more important, the security and validity of processing asset off-chain can be
guaranteed by on-chain verification, so that **we don’t need to compromise
security for better performance.** Theoretically, Loopring could bear **2025
tx/s at a cost of $150 per million transactions with the same security level
as Ethereum mainnet.**

**(2/2)** Could Steve and Jason further share your insights of how Ethereum
ecosystem will benefit from the combination of Layer1+Layer2 scalability? And
what are the potential driving forces for DeFi?

**Steve:** (translated)

The real application of layer2 scalability is indispensable for Ethereum
ecosystem. Recently some fraud schemes lead to a surge of gas price, and the
network has been slowed down, which would be damaging for mass adoption of
Ethereum. For example, Reddit has already decided to use Ethereum as its token
distribution platform. With the tremendous user base of Reddit flooding onto
Ethereum, the traffic would be too much for the network to handle.

Fortunately Loopring has implemented a payment system, Loopring Pay, based on
ZkRollup, which was officially launched on June 7th. Now it has already
supported 10+ token transfers on layer2 with zero fees, which helps mitigate
issues like network congestion and expensive fees. **While for DeFi apps, if
we can handle transfers on layer2, then the layer1 bandwidth coud be eased.**

**Jason:** (translated)

To begin with, it’s a matter of choice. The rising layer2 scalability
solutions endows developers and users with more choices, while avoiding the
potential single layer2 failure. Take ZK-Rollup and Optimistic Rollup schemes
for example. Seen from token transactions, ZK-Rollup is a better choice for
DEX apps and users with faster transaction speed and settlement. Maybe that’s
why Loopring adopted ZK-Rollup. While Optimistic Rollup is more friendly with
logical implementation of smart contracts, which allows developers to build
more delicate DeFi apps. So we saw Synthetix with Optimistic Rollup. More
choices popping in, more prosperous the ecosystem will be.

Second, at a higher level, **the security and scalability of Ethereum get
improved.** Layer1, the Ethereum main chain, serves as the basic security
guarantee for data. On one hand, scalable layer1 improve on-chain data
processing while lowering the possibility of spam transaction attacks. On the
other hand, with more solutions deploying on layer2, layer1 can alleviate its
scalability burden and focus more on security side. That is, Ethereum will
become more reliable while ensuring the user experience, which encourages more
users to build on Ethereum, including DeFi apps, where security comes as a
priority.

Third, I’d like to talk about value capture and network effects. **The
combination of layer1+layer2 enables Ethereum to cover the demands of most
applications in finance or other spaces.** With PoS and booming DeFi, there
will be more staking assets on Ethereum, which might eventually make Ethereum
the “settlement layer”. Meanwhile, greater network effects will come along
with thriving finance, which would be strong positive feedback by driving the
further development of Ethereum ecosystem including DeFi.

**Q5** It’s been known that when eth2 phase 0 happens, Proof of Work Ethereum
will turn into a Proof of Stake blockchain where staking economy will be a
major player. What are your insights of staking economy? How could various
stakeholders participate in eth2 staking, such as average investors, miners,
mining pools and DeFi services etc.?

**Raul:**

The staking economy, to me, will define the security of Ethereum. We wish to
make staking easy for most people, including hobbyists that want to run a
validator at home. If most staking only happens on a few centralized
exchanges, we believe the chain will not be as secure or trustless as it
should be.

Most stakers can get started today with experimenting on eth2 by joining one
of the public testnets. At Prysmatic Labs, we run a public testnet called Onyx
that you can join here: [https://prylabs.net](https://prylabs.net/) and
monitor here: [https://beaconcha.in](https://beaconcha.in/)

**A Jian:** (translated)

Eth2 staking distinguishes itself from existing staking model due to its
unique protocols. To decentralize, the protocol layer places many curbs on
staking, and this is exactly where service providers could come in.

Now when speaking of eth2, it’s more about the coming phase 0, which won’t
bring disruptive changes to the whole ecosystem at once. So it’s totally fine
to keep watching.

I suggest that if you want to participate in eth2 staking, understanding how
its protocols are designed would be helpful for your assessments, no matter
you choose to DIY or use third-party services.

**Jason:** (translated)

On the market side, staking behavior results in reduced ETH market circulation
**which will definitely stimulate a rise in ETH price.** This is what all ETH
holders would like to see. As integral parts in Ethereum ecosystem, most
average investors, miners and pools are driven by earnings. After all
stakeholders need to make their ends meet in the first place, and then they
could afford to sustain Ethereum’s growth.

Therefore, players in the Ethereum ecosystem will form a community with shared
interests. Everyone is expecting Ethereum to play safe, which potentially
empowers and pushing Ethereum forward. There is a funny but vivid expression
for how staking economy will affect Ethereum: too big to fail.

A more straightforward way for average investors to participate is purchasing
ETH, or staking their ETH via staking services provided by exchanges or
wallets. If you want to run your own PoS node, it’s not that difficult.

This is what DeFi servers would like to see, as implementing fractional
reserves is a little bit tricky. One thing is that managing your asset with
DeFi is still risky. For another, other public chains are relatively smaller
in volume, and sometimes staking earnings will fail to cover the loss when its
price goes down. However, maybe DeFi servers could see net earnings by staking
with extra asset in their pools.

**Steve:** (translated)

**Personally, I’m optimistic about eth2 staking giving rise to the ETH
price.** And it’s likely more than 10 million ETH will be locked in staking.

According to a staking survey from ConsenSys, with a sample of 287: **32.8%
users will run their own validator nodes, and 33.1% will use a third party
staking services.**

![AMA2.png](https://i.ibb.co/WDtHXTQ/AMA-1-19a5159578.png)

cr: ConsenSys

Loopring is also considering to provide our own staking pool, as users will
gain no excess earnings by leaving their assets in smart contracts. But
staking will do. However, we promise that users’ assets will still remain non-
custodial via smart contracts, which means users have the right to know and
control their assets position.

**Q6** A Jian and Jason are representatives from Chinese Ethereum communities
EthFans and Unitimes. We wonder what are the challenges for community builders
on the verge of Ethereum 2.0? What could be best practices to engage community
members or even more mainstream population into the next generation of
Ethereum?

**A Jian:** (translated)

A big challenge lies in the **complexity and durative roadmap of eth2
system,** which requires more patience to tell what really matters at the
current stage and what really values in a long term. Otherwise, there’s time
reserved for us to popularize the complicated eth2 system with more delicate
efforts.

I think community builders should keep a good sense of the whole changing
ecosystem, to deliver interesting and exciting stuff in this ecosystem.
Technologies might be dry, but there are always marvels and novelties
happening around the Ethereum ecosystem. **The ecosystem as a whole is
diversified and fascinating.**

**Jason:** (translated)

The biggest challenge facing the Ethereum community is that currently there
are still not many fans and contributors for the blockchain open source
technology.

On the one hand, the technical threshold is a bit high, which means people
should have a good mastering in various disciplines to better understand
blockchain. On the other hand, such technology is too advanced to be
popularized and even some are still biased towards it.

Let’s say Ethereum, with the biggest and strongest developer community, still
has a long way to go in building Chinese Ethereum community.

One thing is that in the past few years, most users have been wandering in
secondary market for earnings, staying out of the Ethereum ecosystem
construction. For another, it’s a bit hard for some potential Ethereum
learners to get over with the language barrier, less community maturity and
rapid iteration of Ethereum technologies. Eth2 or eth1.x might be around
before someone could understand eth1. And in this case, we still need to
**carry forward education on Ethereum and developer community building.**

Now we have EthFans, Unitimes, ECN and EthPlanet to work as Chinese community
contributors. **Eth2 is a brand new start as well as an opportunity for
Chinese Ethereum community to thrive.** We still get plenty to do such as
organizing online or offline seminars, workshops and developing educational
resources.

* * *

#  

# Free Talk

**Q1**.We knew that ETH2.0 will introduce Casper consensus. What’s the
advantage of it? What problems will it fix?

**Raul** :

A specific problem Casper solves is that allows for more secure proof of stake
consensus than those which exist out there today. Most other proof of stake
chains make the compromise of being delegated proof of stake. That is, the
protocol only supports a small number validators (maybe 20–100). Ethereum 2.0
Casper allows for a maximum of 4 million validators, encouraging
decentralization and increasing security.

Other protocols do not allow a large number of validators because they cannot
scale their consensus algorithm if that happens. Ethereum 2.0’s casper allows
you to have scalability and a high number of validators.

**A Jian** : (translated)

The consensus of Eth2.0 can be divided into two components:

  1. LMD-GHOST fork choice rule, which considers the latest signature of validators as the agreement of the fork chain, and selects the fork with most signatures as the calonical chain.

  2. Casper FFG. Its significance is to maintain block consensus and prevent long-range attacks. It enables the network to keep finalizing beacon chain by the design of reward and punishment mechanism, which can be understood as regular updates of the genesis state (so GHOST doesn’t have to track too deep to determine the main chain). The overall effect will be as Raul said, Ethereum’s PoS can support 100x or 1000x validators than other PoS chains.

**Q2**.How can we handle the centralization risk of staking?

**Raul** :

We can help with this problem by making it easier for people to run their own
node. Eth2.0 nodes are easier to run than eth1 or EOS nodes. This will help
encourage decentralization and reduce exchanges holding all of the stake.

**Q3**.Has Ethereum ever considered to adopt Lighting Network used by Bitcoin
as a layer2 solution? Why is ZK-Rollup better than LN?

**Steve** : (translated)

We can put it this way: ZK-Rollup is a more efficient and faster solution to
achieve the asset consistency than LN. Intermediate nodes are required in LN
while ZK-Rollup has its own relayer. ZK-Rollup is not likely to be deployed on
Bitcoin because it needs support from smart contract and specific elliptic
curve computations.

  

# The End.

* * *

Yet it will never end. See you next time💗

* * *

Ethereum Community Network

以太坊社区网络

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAIAAAAC64paAAAACXBIWXMAABcRAAAXEQHKJvM/AAADm0lEQVQ4yyWU1yv9YRzHnzulKLkR5QLxS1aJyDw2WdkS4Zinc+yRvcLJ3nvvHSG7jBtKVi7IhaRcuBDlD/i9vs734uv7eD6f53mvzxHm5uZRUVHBwcEREREODg6Ojo7W1tb6+voWFhYeHh7//h49PT0bGxsvLy9TU9Po6GiKaaFR8GdycrK9vX1ubi4zMzM9Pb2np6epqamoqIgPuVy+urra2dm5vb39/Pzc3Nw8MDDQ0dGxuLgYExMjOKatre3p6amvr0+hUOTn5+fm5t7d3ZWXl/f393d3d3M074KCgq2tLbVaXVtbyylDQ0Ph4eHSzbOzs2xPTU1lZ2fX1dXV1NS8v78XFxfX19fPzMwolcqWlhb+T1l1dfX4+DiHLi8vR0ZGCmgAtaSkpLW1lYNcXFzc3d0BNj8/PzExwSWfn5+3t7egY8k7NDQ0KysLdM7OzkJHR2dwcPDj44PqjIyMhISEtLS00tLSiooK6r6+vg4ODqCwsLCAVFDw9/dPTEzc3d2VYNvZ2alUqunp6f39/evra5hTWllZaWRkFBISAjy2KLi/v2cJOnahvbOzw1kiMDAQSkgXFha2tra2vr6OkrCCv/rvgbaTk1NycjLSaqAh3uvrq6Q2DBsbG4+OjmDC+uLiguXw8HB8fLxMJmP38vIS28bGxjgXztAJCgpCFIIgdHV1CwsLQcIGp4IiLi6ut7eXbXTOy8sDCEbExsb6+fmdnJxAAXXOz8/d3NyElpYW2EgCYGjQ6KmRwNXVlXNfXl7oIWGUQRVHUlJScCEpKUkYGxuTjaurK7hRBH7aNjc3AUl1Q0MDgfn9/YUF+cVRX19f+IPUyspKYBeSHh8fQ4w2slFWVoZgYPv+/iaYaPH29sYpNFND8kkxIZWaCQnubWxsoIS3tzcosLSqqgrywFlaWgLF2dkZIPEPdra2thRgKsUCG4jL3t7ew8MDAeRaTkUwyFPEN8YyFSzR7+bmhg/yix3gF/b29iyo4M3loPj5+UFMDMvJyUEeJglSpIA7OJScIDhZkpphwogwg1xC/+joKMaenp5SzTZUierh4eHj4yOR7Orqopli0ib5rBlJpGewwAxbPGNUAgICcJIPS0tLEGHEysrKyMgIbYSfnw3yK40k3JgNxEBGAwMD3GZOmEe0ZQYxiR62IKxJHg/3kz/BrwnpYUR4o7y2tranp2dqaqqPj4+ZmRk3mJiYICyOahJONg0NDUkbsP8DL00/zmMjxB8AAAAASUVORK5CYII=)![](/static/57048268f8823dd1ea147faa8e568647/d786d/footer_wechat.png)

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAACXBIWXMAAAsTAAALEwEAmpwYAAAEtUlEQVQ4y01VbUxbZRQ+t1Bm2PicA+0Q2WJM/O0vE5f9848mYIxEcB1Q+knbe/t5u5aWFkrRaGewuFDiNhHovW35LISPwIKDZTJjtE4xkWQON2d0mgyny9iI83rObTU2Obk3773vc5/zPs9zCu2sAO1sAuiqtoyClu65hLKdEyq1NuEwVq3WlqzT2sS63L2gwmfl+E4BFhjsSdDgHk0eIw+GC1YBAqFlBBMOajnhaZ1drNE7xEMGZ7Lc5EyVYpXhfQWuVels4lP0Du4r03EinOwYywMmQEbVWBPQZhYZBFPpkIXBkazocKeKWX68yOWbVvq7M4W+YKbQ6Z1SWvnxfR2u1H4EPohs63BPlcE5Aq1mxCGGassIBLtXiJkKX6gxupIHOM9EUSi8VDA1scncuHYPYkNZZjS5Bdtbv0MikWX8ofkCAjY6k6UyU044hFfQ20QALZeQ2yRmJgSzecaVQ4OfKXbvPwJJksAamAd3eB3CA1ng+y7Ia7/8vAvvnV5TsHy6CEHLZKasUII4QGBK+gq1ScwIjDZRWTqXGT6yBu7e9aP+6EZ5IHoFLP5VeCDdgd3dPYhG1xTEVO9IEsNaFIkhwEoSgM6M2nz44G+YXr0IbdwMnLTMwqstaQXbuWB39yy+4gjNA+ubZPb2UrAn3YWbP/wBp7pmC02u1AEUCgGFEiBrkJokwNTEN0yO3R0wudOM0TWO18ljBmcqrLcPe03uhKrNHAeNZYj5t4uh+KcKizv9GJJ6ErGqCbCWrEFqfre5A9sXJDA4xhidbQSfjVYYHILbzCd9J/Sx4Gtv9jWzgQnYQaCXGwIA4IWVpe8ZzjNZhKQeJ3JApiWf+UOZwuvfPoJnjreD1SMwJrSC0fFRA+sV3vL2zvr4nkygxTgQqW8MPFff2AWN6j5GeijB1c9vgts3pTQ6UhVo/iNACSDTks+uIWDtcQ3wARECfXNwqifzAssPN+vZQZeO+9Bs7xyv9/YuPOuLLIKnZw6kHQm+2LgF5E8SNQ+YMzItbn71G8y0SND1zgoTiq5CJHb5Cf/bS2ozP/yiMzhzLNx/+Y3+s5ulp+NZiLx/RT7DhbkthtxBOuRbFlQUJ5JfSHwpHzb9PN3TjDc8B85A+iVX10TQG1kMYT0fjF6E4Lur/4kyMHAJRUmRKCq0ThXZppyySXGiBNxG0/4l3YPX1f3QpO6BXdxksp+1WD1ik70zDb7wLH6uQQb7Ovsrw/szhWjuEiRGidkPGpwaZGzKJrGkBNxH09IGte4DRtNxBlpNscPtlnglFjRr4/Kzn279Cb2RFdkyertYjRg1Tdx5Soo8duT4UDYpTpSAG9fv5tLCnwNNRwx0liFwBQV57Wr2NkNgVnd6n8EpohjCEcQolqcNzTNsmVqvIqaUTWLqxQTE4xuKS5/8yJwZXGLOnV9nVpe3mRieGbVJzGQwTp44FVqcNDQg5DlG88zo/BjkqYFMSTGKE20i05LPyAWkJglAZya3ScwIjBvDc05AK5sHpGoxi/IXaGpQ0MlOFCdKAJmWrEUfktVEAejMsMViYkZgbTKOkB+w+dLbksSSioYtKVed+xsQj5Jp5Xs8GlLzhD03obU4sdv+h/EPsbi7Iqfeg68AAAAASUVORK5CYII=)![](/static/1b87ba5dd8a4dda4d8d17e472bd9cefb/002c1/footer_ethereum.png)

订阅

[ ](https://twitter.com/EthereumCN)[ ](https://discord.gg/KUywx3JJJU)[
](https://i.ibb.co/mBgmDgF/footer-wechat.webp)[
](https://github.com/EthereumCN)[ ](Mailto:eth@ecn.co)[
](https://www.ethereum.cn/rss.xml)

蜀ICP备2021001286号 ](https://beian.miit.gov.cn/)

Ethereum Community Network

以太坊社区网络

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAIAAAAC64paAAAACXBIWXMAABcRAAAXEQHKJvM/AAADm0lEQVQ4yyWU1yv9YRzHnzulKLkR5QLxS1aJyDw2WdkS4Zinc+yRvcLJ3nvvHSG7jBtKVi7IhaRcuBDlD/i9vs734uv7eD6f53mvzxHm5uZRUVHBwcEREREODg6Ojo7W1tb6+voWFhYeHh7//h49PT0bGxsvLy9TU9Po6GiKaaFR8GdycrK9vX1ubi4zMzM9Pb2np6epqamoqIgPuVy+urra2dm5vb39/Pzc3Nw8MDDQ0dGxuLgYExMjOKatre3p6amvr0+hUOTn5+fm5t7d3ZWXl/f393d3d3M074KCgq2tLbVaXVtbyylDQ0Ph4eHSzbOzs2xPTU1lZ2fX1dXV1NS8v78XFxfX19fPzMwolcqWlhb+T1l1dfX4+DiHLi8vR0ZGCmgAtaSkpLW1lYNcXFzc3d0BNj8/PzExwSWfn5+3t7egY8k7NDQ0KysLdM7OzkJHR2dwcPDj44PqjIyMhISEtLS00tLSiooK6r6+vg4ODqCwsLCAVFDw9/dPTEzc3d2VYNvZ2alUqunp6f39/evra5hTWllZaWRkFBISAjy2KLi/v2cJOnahvbOzw1kiMDAQSkgXFha2tra2vr6OkrCCv/rvgbaTk1NycjLSaqAh3uvrq6Q2DBsbG4+OjmDC+uLiguXw8HB8fLxMJmP38vIS28bGxjgXztAJCgpCFIIgdHV1CwsLQcIGp4IiLi6ut7eXbXTOy8sDCEbExsb6+fmdnJxAAXXOz8/d3NyElpYW2EgCYGjQ6KmRwNXVlXNfXl7oIWGUQRVHUlJScCEpKUkYGxuTjaurK7hRBH7aNjc3AUl1Q0MDgfn9/YUF+cVRX19f+IPUyspKYBeSHh8fQ4w2slFWVoZgYPv+/iaYaPH29sYpNFND8kkxIZWaCQnubWxsoIS3tzcosLSqqgrywFlaWgLF2dkZIPEPdra2thRgKsUCG4jL3t7ew8MDAeRaTkUwyFPEN8YyFSzR7+bmhg/yix3gF/b29iyo4M3loPj5+UFMDMvJyUEeJglSpIA7OJScIDhZkpphwogwg1xC/+joKMaenp5SzTZUierh4eHj4yOR7Orqopli0ib5rBlJpGewwAxbPGNUAgICcJIPS0tLEGHEysrKyMgIbYSfnw3yK40k3JgNxEBGAwMD3GZOmEe0ZQYxiR62IKxJHg/3kz/BrwnpYUR4o7y2tranp2dqaqqPj4+ZmRk3mJiYICyOahJONg0NDUkbsP8DL00/zmMjxB8AAAAASUVORK5CYII=)![](/static/57048268f8823dd1ea147faa8e568647/d786d/footer_wechat.png)

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAACXBIWXMAAAsTAAALEwEAmpwYAAAEtUlEQVQ4y01VbUxbZRQ+t1Bm2PicA+0Q2WJM/O0vE5f9848mYIxEcB1Q+knbe/t5u5aWFkrRaGewuFDiNhHovW35LISPwIKDZTJjtE4xkWQON2d0mgyny9iI83rObTU2Obk3773vc5/zPs9zCu2sAO1sAuiqtoyClu65hLKdEyq1NuEwVq3WlqzT2sS63L2gwmfl+E4BFhjsSdDgHk0eIw+GC1YBAqFlBBMOajnhaZ1drNE7xEMGZ7Lc5EyVYpXhfQWuVels4lP0Du4r03EinOwYywMmQEbVWBPQZhYZBFPpkIXBkazocKeKWX68yOWbVvq7M4W+YKbQ6Z1SWvnxfR2u1H4EPohs63BPlcE5Aq1mxCGGassIBLtXiJkKX6gxupIHOM9EUSi8VDA1scncuHYPYkNZZjS5Bdtbv0MikWX8ofkCAjY6k6UyU044hFfQ20QALZeQ2yRmJgSzecaVQ4OfKXbvPwJJksAamAd3eB3CA1ng+y7Ia7/8vAvvnV5TsHy6CEHLZKasUII4QGBK+gq1ScwIjDZRWTqXGT6yBu7e9aP+6EZ5IHoFLP5VeCDdgd3dPYhG1xTEVO9IEsNaFIkhwEoSgM6M2nz44G+YXr0IbdwMnLTMwqstaQXbuWB39yy+4gjNA+ubZPb2UrAn3YWbP/wBp7pmC02u1AEUCgGFEiBrkJokwNTEN0yO3R0wudOM0TWO18ljBmcqrLcPe03uhKrNHAeNZYj5t4uh+KcKizv9GJJ6ErGqCbCWrEFqfre5A9sXJDA4xhidbQSfjVYYHILbzCd9J/Sx4Gtv9jWzgQnYQaCXGwIA4IWVpe8ZzjNZhKQeJ3JApiWf+UOZwuvfPoJnjreD1SMwJrSC0fFRA+sV3vL2zvr4nkygxTgQqW8MPFff2AWN6j5GeijB1c9vgts3pTQ6UhVo/iNACSDTks+uIWDtcQ3wARECfXNwqifzAssPN+vZQZeO+9Bs7xyv9/YuPOuLLIKnZw6kHQm+2LgF5E8SNQ+YMzItbn71G8y0SND1zgoTiq5CJHb5Cf/bS2ozP/yiMzhzLNx/+Y3+s5ulp+NZiLx/RT7DhbkthtxBOuRbFlQUJ5JfSHwpHzb9PN3TjDc8B85A+iVX10TQG1kMYT0fjF6E4Lur/4kyMHAJRUmRKCq0ThXZppyySXGiBNxG0/4l3YPX1f3QpO6BXdxksp+1WD1ik70zDb7wLH6uQQb7Ovsrw/szhWjuEiRGidkPGpwaZGzKJrGkBNxH09IGte4DRtNxBlpNscPtlnglFjRr4/Kzn279Cb2RFdkyertYjRg1Tdx5Soo8duT4UDYpTpSAG9fv5tLCnwNNRwx0liFwBQV57Wr2NkNgVnd6n8EpohjCEcQolqcNzTNsmVqvIqaUTWLqxQTE4xuKS5/8yJwZXGLOnV9nVpe3mRieGbVJzGQwTp44FVqcNDQg5DlG88zo/BjkqYFMSTGKE20i05LPyAWkJglAZya3ScwIjBvDc05AK5sHpGoxi/IXaGpQ0MlOFCdKAJmWrEUfktVEAejMsMViYkZgbTKOkB+w+dLbksSSioYtKVed+xsQj5Jp5Xs8GlLzhD03obU4sdv+h/EPsbi7Iqfeg68AAAAASUVORK5CYII=)![](/static/1b87ba5dd8a4dda4d8d17e472bd9cefb/002c1/footer_ethereum.png)

订阅

[ ](https://twitter.com/EthereumCN)[ ](https://discord.gg/KUywx3JJJU)[
](https://i.ibb.co/mBgmDgF/footer-wechat.webp)[
](https://github.com/EthereumCN)[ ](Mailto:eth@ecn.co)[
](https://www.ethereum.cn/rss.xml)

[ 蜀ICP备2021001286号 ](https://beian.miit.gov.cn/)

