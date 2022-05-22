[ ![NuCypher](https://blog.nucypher.com/content/images/2019/03/NuCypher-blu-
whi.png) ](https://blog.nucypher.com)

  * [Blog](https://blog.nucypher.com/)
  * [Website](https://www.nucypher.com/)
  * [Documentation](https://docs.nucypher.com/en/latest/)
  * [GitHub](https://github.com/nucypher)

[ ](https://twitter.com/nucypher "Twitter")

Subscribe

# WorkLock Participation Details

  * [ ![MacLane Wilkison](/content/images/size/w100/2019/05/IMG_8077.jpg) ](/author/maclane/)

#### [MacLane Wilkison](/author/maclane/)

Aug 25, 2020 • 5 min read

![WorkLock Participation
Details](/content/images/size/w2000/2020/08/worklock3.png)

The WorkLock is finally here! The WorkLock is NuCypher’s novel network node
setup mechanism that will be used to launch the network. It allows
participants to temporarily stake ETH in order to receive NU for the exclusive
purpose of running a NuCypher network node.

###  **Key Details/TLDR**

  * WorkLock escrow period: September 1, 00:00 UTC - September 28, 23:59 UTC
  * Cancellation window: September 29, 00:00 UTC - September 30, 23:59 UTC
  * Minimum escrow of 5 ETH (unless participating via [CoinList](https://coinlist.co/nucypher-worklock)).
  * 22.5% of initial supply; 225M NU
  * NU stake locked for 6 months (starting at mainnet launch, _not_ from when you escrow)
  * Time to recover escrowed ETH: <= 6 months (from network launch)
  * Mainnet launch expected in October

###  **Timeline & Mechanics**

NuCypher’s WorkLock will begin on September 1, 2020 at 00:00 UTC. The
contribution period will be open for four weeks, ending September 28, 2020 at
23:59 UTC. You can cancel your bid anytime during the contribution period and
for two additional days (the “cancellation window”) ending on September 30
23:59 UTC.

22.5% of the initial supply of NU (225M NU) will be stake-locked through the
WorkLock. Once mainnet is activated (referred to as "network launch"),
participants that made at least the minimum contribution of 5 ETH, will be
able to claim their “stake-locked” NU and start running a node on the network.
Network launch is expected to occur in October 2020. All participants making
the minimum escrow are guaranteed to receive 15,000 NU (the minimum required
stake to operate a node). (Note: This does not apply to those participating
via CoinList, in which case the amount of NU may vary). Once the minimum
stakes are allocated, the remaining “bonus” NU will be allocated pro rata
across participants that staked more than the minimum 5 ETH stake.

While we believe it is unlikely, it is possible that there may be certain edge
cases in which large participants are partially refunded a portion of their
escrow in order to prevent them from receiving a stake that exceeds the
maximum allowable stake.

After successfully running a node for **six months or less** (from network
launch; the exact time depends on your individual staking configuration as
well as the staking participation rate across the network), participants will
be able to fully recover their escrowed ETH. We anticipate that participants
can recover their escrowed ETH incrementally over time or all at once, at
their option.

NU that is pre-staked for network nodes via the WorkLock will otherwise behave
like any other staked NU and Stakers can optionally wind-down or extend their
stake, re-stake rewards, etc.

You can read more about the WorkLock mechanics and explore several example
scenarios
[here](https://docs.nucypher.com/en/latest/architecture/worklock.html#worklock-
architecture).

⚠️ 🚨 **Notice to WorkLock Participants** 🚨⚠ **:** Your participation in the
WorkLock program represents an interaction with the decentralized network and
not with NuCypher the company. Just like with other aspects of the network,
the WorkLock smart contract is decentralized and is beyond the control of
NuCypher. All ETH contributed during the WorkLock will be automatically
returned to the participant by the Worklock smart contract after the WorkLock
participant has provided Proxy Re-Encryption services for the required period
of approximately six months from network launch. If a participant does not
provide the required services, their ETH will remain escrowed in the WorkLock
smart contract. Please carefully consider this before choosing to participate
in the Worklock program. The WorkLock smart contract has been audited by both
NuCypher core developers and Trail of Bits. However, there are no guarantees
and a certain degree of smart contract risk remains.

###  **Participation Options**

The WorkLock is designed as permissionless such that anyone can participate by
interacting with the smart contract directly. The canonical way to participate
is via the NuCypher CLI (guide
[here](https://docs.nucypher.com/en/latest/guides/worklock_guide.html)). This
is the self-sovereign way to participate in the WorkLock.

There are two 3rd party web UIs developed by community members during [_Come
and Stake It_](https://blog.nucypher.com/come-and-stake-it-incentivized-
testnet/), our incentivized testnet. These UIs can connect to web3 wallets
like Metamask, and allow you to stake directly from there via a friendly and
intuitive web UI. You can deploy these applications locally by following the
GitHub links below. Alternatively, we are hosting versions of both apps on our
infrastructure during the WorkLock at the URLs below.

 _Stake NuCypher_  
* <https://stake-nu.nucypher.community/>  
* <https://github.com/nucypher/stake-nucypher>

_Stakeit Space_  
* <https://stakeit-space.nucypher.community/>  
* <https://github.com/nucypher/stakeit.space>

Finally, you can also participate via [CoinList](https://coinlist.co/nucypher-
worklock). Participating via CoinList is the simplest way to join the WorkLock
and is the best way to participate for those who don’t have the minimum
staking amount and/or want assistance with staking and running nodes.

Other ecosystem participants may also be offering pools or other participation
options. In every case, you should exercise appropriate due diligence before
participating.

###  **Running Nodes**

You can run your own NuCypher node as per the instructions
[here](https://docs.nucypher.com/en/latest/guides/network_node/ursula_configuration_guide.html).

There are also many staking infrastructure providers who can run nodes on your
behalf. A partial list can be found
[here](https://github.com/nucypher/validator-profiles). If delegating to a
provider, you should exercise appropriate due diligence. (Note: Delegation
does not mean pooling. It is not possible to pool multiple WorkLock stakes
into one worker node).

The #staking channel in NuCypher’s [discord
server](https://discord.com/invite/7rmXa3S), is a place for stakers and node
operators to troubleshoot, ask questions, and provide mutual technical
support.

⚠️ 🚨Gas is currently very expensive on the Ethereum network. Nodes must
confirm activity daily via an ETH transaction, which costs ~200k gas. Please
consider this when deciding whether to participate, especially for small
stakes. 🚨⚠

###  **NU Genesis Distribution**

The total initial supply is 1 billion NU. 225 million NU (22.5% of initial
supply) is allocated to the WorkLock. WorkLock NU is under a 6-month stake
lock. To unlock your NU stake and recover your staked ETH in 6 months or less
(from network launch), WorkLock participants are required to run a NuCypher
node. Staked ETH can be withdrawn incrementally as work is done.

The total supply of NU is ~3.89 billion and the 2.89 billion difference is
expected to be distributed as an inflation subsidy to Stakers over time. You
can read more about the inflation schedule and full staking economics
[here](https://github.com/nucypher/whitepaper/blob/master/economics/staking_protocol/NuCypher_Staking_Protocol_Economics.pdf).

###  **The NuCypher Network and NU**

The NuCypher Network is a decentralized threshold cryptography network. Nodes
in the network expose APIs and runtimes for cryptographic operations like
threshold proxy re-encryption, threshold signatures, and more, enabling use
cases like access control, secrets management, and delegated signing. The
network is anticipated to be primarily used as middleware by other
applications, several examples of which can be found
[here](https://multicoin.capital/2018/02/13/new-models-utility-tokens/).

NU is an ERC20 compatible “[work
token](https://multicoin.capital/2018/02/13/new-models-utility-tokens/).” In
the work token model, a service provider stakes (AKA bonding) the native token
of the network to earn the right to perform work for the network. In
NuCypher’s case, that work is threshold cryptography services, which enable
use cases like access control and secrets management.

NU stakers are able to earn fees paid into the network by users (in ETH), as
well as an inflation subsidy (in NU). They are also able to participate in the
[NuCypher DAO](https://blog.nucypher.com/announcing-the-nucypher-dao/), which
governs the network.

Information on the expected distribution and release schedule for NU can be
found in the charts below as well as in the NU release schedule
[here](https://www.nucypher.com/nu-release-schedule.pdf), staking economics
paper
[here](https://github.com/nucypher/whitepaper/blob/master/economics/staking_protocol/NuCypher_Staking_Protocol_Economics.pdf),
and simplified inflation/staking economics spreadsheet
[here](https://docs.google.com/spreadsheets/d/1I_PYoiCaKkgKmht6b2l1xIRRAR3tXORXLek2NwpEkFI/edit?usp=sharing).
It is possible that the below schedules and estimations may change.

![](https://blog.nucypher.com/content/images/2020/08/image.png)Genesis Block
Recipients![](https://blog.nucypher.com/content/images/2020/08/image-2.png)Post
Genesis NU
Holders![](https://blog.nucypher.com/content/images/2020/08/image-3.png)Genesis
Block Unlock Schedule

## Sign up for more like this.

Enter your email Subscribe

[ ![Developer Update - Abiotic Alice and DKG \(October
2021\)](/content/images/size/w600/2021/10/2021-10-13-10.46.21.jpg)
](/developer-update-october-2021/)

[

## Developer Update - Abiotic Alice and DKG (October 2021)

NuCypher's proxy re-encryption (PRE) service is leveling up. Recently, the
demand for access-conditioned content in Web3 has exploded: subscriptions,
streaming, private NFTs, NFTs as access tokens, the list goes on. Many of
those are building on NuCypher (soon Threshold!) and proxy re-encryption. For
example: Masterfile is building an enterprise NFT

](/developer-update-october-2021/)

  * [ ![MacLane Wilkison](/content/images/size/w100/2019/05/IMG_8077.jpg) ](/author/maclane/)

[MacLane Wilkison](/author/maclane/) Oct 13, 2021 • 3 min read

[

## NuCypher Community Update - September 2021

Once a month we'll be putting out community updates in the format of team
member interviews. September's update is an interview NuCypher's CTO, David
Nuñez.

](/september-nu-community-update/)

  * [ ![Ryan Caruso](/content/images/size/w100/2020/12/IMG_5522.JPG) ](/author/ryan/)

[Ryan Caruso](/author/ryan/) Sep 17, 2021 • 13 min read

[

## NuCypher + Keep: KEaNU AMA, Hosted by Staking Hub

Hey NuCypher and Keep community, here is the transcribed copy of the AMA
hosted by Figment's Staking Hub. Thanks to the hosts, the Nu + Keep team, and
those who asked questions from the community.

](/nucypher-keep-keanu-ama-hosted-by-staking-hub/)

  * [ ![Ryan Caruso](/content/images/size/w100/2020/12/IMG_5522.JPG) ](/author/ryan/)

[Ryan Caruso](/author/ryan/) Jun 28, 2021 • 9 min read

[NuCypher](https://blog.nucypher.com) (C) 2022

  * [Telegram](https://t.me/nucypher)
  * [Discord](https://discord.com/invite/7rmXa3S)
  * [Twitter](https://twitter.com/nucypher)

[Powered by Ghost](https://ghost.org/)

