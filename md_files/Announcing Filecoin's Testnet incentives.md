[ ![Filecoin](../../../images/filecoin-logo.svg) ](../../../)

  * [Store](../../../store/)
  * [Provide](../../../provide/)
  * [Build](../../../build/)

    * Docs
    * Tools & services
    * Grants
    * Roadmap
    * Videos
    * Filecoin Community
    * Events

  * [Blog](../../../blog/)

Explore the Network

  * [Filfox.info](https://filfox.info/en)
  * [Filscan.io](https://filscan.io/#/tipset/chain)
  * [Filscout.io](https://filscout.io/en/)
  * [Spacegap](https://spacegap.github.io)
  * These explorers were built by community members and may have inaccuracies

[ EN ](../../../en) [ 中文 ](../../../zh-cn)

Category:

  * [updates](../../../blog/updates)

  *   *   * 

![](../../../images/icons/social/share.svg)

Jun 9, 2020  

## Announcing Filecoin's Testnet incentives

After years of research and development, Filecoin’s mainnet launch is within
sight. Today, we’re announcing Filecoin’s testnet incentives program and
inviting miners all over the world to compete to earn global and regional
pools totaling **up to 4 million Filecoin tokens.**

## Program structure

The testnet incentives program is a collaborative competition intended to
stress-test the network, encourage participation all over the world, and help
miners get ready to run the world’s biggest decentralized storage network. The
competition’s basic structure is simple: for three weeks, miners will compete
to onboard as much storage capacity as possible to the network. The top 100
miners globally, as well as the top 50 miners from each continent, will earn
Filecoin rewards based on how much storage they and the network achieve during
the test period.

There are two ways miners can earn more rewards:

  * The total size of the reward pool increases alongside total network storage capacity.
  * The total pool of rewards is split between eligible mining operations _pro rata_ , based on how much storage they add as a percentage of total network storage.

“Regions” are the six continents, excluding Antarctica. We use [this
list](https://unstats.un.org/unsd/methodology/m49/) to decide which continent
a country falls into. The total reward pools split between the top mining
operations are:

Total FIL rewards (global pool) | Global network storage achieved  
---|---  
100k | 5 PiB  
200k | 10 PiB  
300k | 25 PiB  
500k | 50 PiB  
1MM * | 100 PiB  
  
##### _* Only unlocked if each region achieves at least 1PiB of storage_

Total FIL rewards (regional pool) | Regional network storage achieved  
---|---  
25k | 100 TiB  
50k | 500 TiB  
100k | 1 PiB  
250k | 5 PiB  
500k | 10 PiB  
  
Here’s a sample calculation:

  * During the competition, a mining operation located in Argentina seals 1.5 PiB of storage to the network.
  * The South America region has 5.0 PiB of total storage, so the regional leaders will split 250,000 FIL. 3.0 PiB are held by the top 50 mining operations in the region, with the remainder held by smaller miners.
  * The global leaderboard has 120 PiB of total storage, with 100 PiB held by the top 100 mining operations and 20 PiB held by smaller miners. Each region has also reached 1 PiB of total storage, so the largest global reward tier (1MM FIL) is unlocked.
  * 1.5 PiB is enough for a top-100 place on the global leaderboard.
  * The mining operation would be eligible to receive **125,000 FIL** from the regional leaderboard (250k total FIL rewards * 1.5 PiB / 3.0 PiB) and **15,000 FIL** from the global leaderboard (1MM total FIL rewards * 1.5 PiB / 100 PiB), for a total of **140,000 FIL**.

In addition to committing sealed storage, miners **must be prepared to
successfully complete terabytes of real storage and retrieval deals** to be
eligible for rewards. They also must demonstrate the ability to **execute the
full sector life cycle** – creating committed capacity sectors, upgrading them
to store real data, and terminating them.

The competition will include a dashboard where miners can view global and
regional reward tiers, as well as individual miner storage power, deal success
rate, and sector life cycle command completion, in real time. Miners will also
be able to display their names (individual or company) alongside their miner
ID on the leaderboard.

## Rules

  * Any rewards earned will be encoded into the genesis block and will **vest linearly over six months from mainnet launch**.
  * To be eligible for rewards, miners must “claim” their miner ID from the dashboard following the provided instructions before the competition ends and pass an AML/KYC check.
  * The metric used to calculate storage is raw byte-power. Sector quality & verified deals are not considered for purposes of calculating rewards.
  * A miner’s “location,” for regional leaderboards, is the physical location of the mining operation. Operations split between multiple regions must run multiple miners. Miners from regions other than the most competitive region will be required to submit documentation verifying their location claims. **Claiming to be from a different location will disqualify you from rewards and leaderboard inclusion.**
  * If a bug is identified during the competition that threatens the validity of the power table, or the Filecoin team identifies some other unforeseen exceptional circumstance, the Filecoin team may end the competition early. Rewards will still be awarded for the period prior to the discovery of any such bug, to the extent they can be reliably determined. If the bug is responsibly disclosed to the Filecoin team, the team reporting it will be eligible for rewards of up to 250,000 FIL, depending on the severity and practicality of the bug, as determined by the Filecoin team.
  * While we don’t expect it, in the unlikely event that Protocol Labs or the Filecoin Foundation determine in their sole discretion that legal or regulatory issues prevent the delivery of any portion of rewards, the rewards may be restructured, postponed, or cancelled.

## Hardware

Filecoin will use the **SDR proof-of-replication** (very similar to the
existing testnet construction) for testnet incentives and at mainnet launch.
Miners should expect Filecoin to regularly upgrade its proofs after launch.

**The Filecoin team does not recommend any specific hardware configuration.**
For the sake of convenience, here are some setups we’ve used for various types
of testing. It is overwhelmingly likely that there are more efficient setups,
and we strongly encourage miners to test and experiment to find the best
combinations.

  * [Testing and small-scale mining](https://pcpartpicker.com/user/tperson/saved/H2BskL)
  * [Large-scale mining](https://filecoin.io/vintage/mining-hardware-config-testnet-v1.pdf)

## Timing

The competition will run for a total of three weeks. We’ll confirm the exact
start date when we fix a launch date, but the competition may begin **as soon
as early July**. We strongly encourage miners to start preparing now.

## Join the testnet and start mining

Whether you’re an experienced miner or just getting started, the testnet
incentives competition is a great time to ramp up your participation on the
Filecoin network. Get started with the [docs for Lotus](https://docs.lotu.sh/)
(a Filecoin node and miner) and join the [Filecoin
Slack](https://join.slack.com/t/filecoinproject/shared_invite/zt-dj58b7fq-
weyaTEvjHoYF_ENkQHR6Ig).

### Related Articles

[View all articles](../../../blog)

[ ](../../../blog/posts/announcing-filecoin-s-testnet-incentives/)

updates

##  [ Announcing Filecoin's Testnet incentives
](../../../blog/posts/announcing-filecoin-s-testnet-incentives/)

After years of research and development, Filecoin’s mainnet launch is within
sight. Today, we’re announcing Filecoin’s testnet incentives program and
inviting miners all over the world to compete to earn global and regional
pools totaling up to 4 million Filecoin tokens.

Jun 9, 2020

[ ](../../../blog/posts/announcing-filecoin-s-testnet-incentives/)

[ ](../../../blog/posts/getting-ready-for-filecoin-s-space-race/)

updates

##  [ Getting Ready for Filecoin’s Space Race ](../../../blog/posts/getting-
ready-for-filecoin-s-space-race/)

As we enter the home stretch into Filecoin’s mainnet launch, Lotus (the
Filecoin reference implementation) is making fast progress. In the past 2
weeks alone the team has landed a major data transfer improvement to the
Filecoin market implementation, finished up the final sector-lifecycle
features for verified & fast-retrieval deals and upgrading Committed Capacity
sectors, and shipped large improvements to the Filecoin actors.

Jul 14, 2020

[ ](../../../blog/posts/welcome-to-the-space-race/)

##  [ Welcome to the Space Race ](../../../blog/posts/welcome-to-the-space-
race/)

The Filecoin Testnet Incentives Program is kicking off on, Monday August 24th
at 10pm UTC (3pm PT | 6am CST on Tuesday, August 25th)!

Aug 19, 2020

Filecoin is an open-source cloud storage marketplace, protocol, and incentive
layer.

##### Reach out

  * [Slack ](https://filecoin.io/slack)
  * [WeChat  ](https://weixin.qq.com/r/1xz54Y-EctINrcuC90nF)
  * [Twitter ](https://twitter.com/Filecoin)
  * [Forum ](https://github.com/filecoin-project/community#forums)
  * [Matrix ](https://riot.im/app/#/group/+filecoin:matrix.org)

##### Resources

  * [Research](https://research.filecoin.io/)
  * [Blog](https://filecoin.io/blog/)
  * [Github](https://github.com/filecoin-project)
  * [ProtoSchool](https://proto.school/course/filecoin)
  * [Security](https://security.filecoin.io/)

##### Sign up for Filecoin updates

Your email Submit

Something went wrong. Please try again.

You’ve been signed up for our newsletter. Thank you!

