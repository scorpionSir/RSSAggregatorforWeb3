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

  *   *   * 

![](../../../images/icons/social/share.svg)

Aug 19, 2020  

## Welcome to the Space Race

The [Filecoin Testnet Incentives Program](https://filecoin.io/blog/announcing-
testnet-incentives/) is kicking off on, Monday August 24th at 10pm UTC (3pm PT
| 6am CST on Tuesday, August 25th)! For the next 3 weeks, miners on the
Filecoin Testnet will be competing for up to 4M FIL in prizes as they race to
onboard as much storage space as possible. In the past month, we’ve already
seen over 240 miners from 5 continents preparing to participate - reaching
sealing speeds of 1 TiB / second (15 PiB sealed within 3 days)! Huge thanks to
all miners for their help diagnosing issues, proposing fixes, and stress-
testing the network in exciting ways. 🙏

Now, it’s time to start your engines. 🚀 Lotus is in code-freeze for the
competition, and we have [officially merged the “next” branch into
“master”](https://github.com/filecoin-project/lotus/commits/master) in
preparation for resetting the Filecoin Testnet to start the Space Race. `Epoch
0` will start on Monday August 24th at 10pm UTC exactly, with the genesis
being released approximately ~2 hours ahead of time for miners to get set up.

Let the countdown begin! ⏱

### The Competition

Space Race is a collaborative competition intended to stress-test the network,
encourage participation all over the world, and help miners get ready to run
the world’s biggest decentralized storage network. In this 3-week competition,
miners are competing to onboard as much storage capacity as possible to the
network. The top 100 miners globally, as well as the top 50 miners from each
continent, will earn Filecoin rewards based on how much storage they and the
network achieve during the competition period. Once the competition is live,
you’ll be able to track progress at
[**https://spacerace.filecoin.io**](https://spacerace.filecoin.io
"https://spacerace.filecoin.io").

In addition to onboarding storage capacity, the 20 largest block reward
winners will split an additional **100K FIL** prize proportionally based on
how much block reward they win. You’ll be able to track the standings on this
prize at
[**https://reward.testnet.filecoin.io/**](https://reward.testnet.filecoin.io/
"https://reward.testnet.filecoin.io/") once the network’s up.

_For now, you can see ‘calibration’ versions of both competition dashboards
at_
[_https://calibration.spacerace.filecoin.io/_](https://calibration.spacerace.filecoin.io/
"https://calibration.spacerace.filecoin.io/") _and_
[_https://reward.calibration.fildev.network/_](https://reward.calibration.fildev.network/
"https://reward.calibration.fildev.network/") _respectively._

### Space Race Eligibility

Filecoin aims to create a decentralized, efficient, and robust foundation for
humanity’s information. Successfully reaching that goal requires a global
network of miners able to demonstrate responsible stewardship of client data.
Therefore, in order to be eligible for Space Race, participating miners must
respond to storage and retrieval deal requests from competition bots,
maintaining a **80% success rate** or above for BOTH storage and retrieval
deals. Bots will start making deals with miners who have successfully sealed
sectors within 12-24 hours after competition launch, and will continue making
deal requests throughout the competition.

To demonstrate they can execute the whole sector lifecycle (onboarding,
upgrading, and terminating a sector), participants must perform _at least one_
**committed capacity sector upgrade** during the competition to be eligible
for rewards. See instructions in the [Filecoin
docs](https://docs.filecoin.io/mine/spacerace/#how-do-i-demonstrate-a-sector-
upgrade).

Miners will be able to track their deal success rate and sector lifecycle
status in the spacerace.filecoin.io dashboard. For additional details on the
rules and eligibility requirements, see the [Space Race docs and
FAQ](https://docs.filecoin.io/mine/spacerace/). Please join the **#space-
race** channel on [Filecoin slack](http://filecoin.io/slack) for the latest
competition updates, and **#fil-testnet** for network/debugging questions once
the competition begins!

### Incentives Calibration Period

Since late July, we’ve been running a Space Race “calibration” network for
miners to practice in real competition conditions and see how their
performance influences hypothetical competition standings. This calibration
period was a critical addition to ensure that miners participating in the
Space Race were able to meet eligibility criteria by making successful storage
and retrieval deals - and that the network was stable enough to enable their
success.

The Calibration Period also saw huge improvements in network functionality and
performance. New features launched in the calibration devnet included the
ability to upgrade committed space with real deals, store multiple deals in
one sector, request fast retrieval from miners via a plaintext copy, and
exchange FIL for successful deals via payment channels. Similar to
[EIP1559](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-1559.md), the
calibration network also introduced burning gas for the on-chain resources
that message execution consumes, and enabling message senders to directly pay
priority fee to block producing miners, untethered to gas usage.

Huge thanks to the great community in the **#fil-net-calibration** channel on
[Filecoin slack](http://filecoin.io/slack) for all their help upgrading the
network over the past few weeks! 💪 If you’re still not happy with your
standings, you have a few more days to iron out any last issues. Please ensure
you’re up to date with the latest calibration network to make sure you’re
ready to start Space Race with the latest fixes on Monday.

### Participating in Space Race

Thanks to the calibration period, miners in the Space Race have a number of
new tools (and better docs!) to help them participate successfully in the
competition.

**Competition Faucet:** our new and improved
[faucet](https://spacerace.faucet.glif.io/) helps miners smoothly onboard
their storage onto the network, while avoiding pointless hoarding or spamming.
We want to simulate real-world dynamics around efficient gas and fee prices by
fairly limiting access to testnet FIL, without overly inconveniencing large
miners.

We’ve evolved our faucet logic significantly during the calibration period to
try to find a reasonable setup. To get started, new addresses are allocated an
amount that is sufficient to start sealing, but not too significant to be
easily abused. Most storage onboarding needs should be met with the
reimbursement mechanism that distributes more testnet FIL as more sectors are
sealed. Miners can regularly tap the faucet for additional but small streams
of testnet FIL for their daily operations. Larger miners may be expected to
have multiple Github accounts to initialize their operations, but
reimbursement should kick in fairly quickly.

  * To receive testnet FIL from the faucet, miners must authenticate with a Github account **over 48 hours old**.
  * Miners can receive a one-time grant of 100 testnet FIL to any address.
  * Once a participant has an active miner actor, they can return to the faucet for additional requests of testnet FIL **once per 24 hours**. The first of these requests will return 1,000 testnet FIL, and subsequent requests will return 200 testnet FIL. To receive these top-ups, enter your miner ID into the faucet and funds will be sent to the worker address. 
    * This is separate from the one-time grant - so miners can request both the one-time grant and miner actor grant within the first 24 hours.
  * In addition, for miners able to seal data at high-velocity, we have a faucet bot that will **send reimbursements for initial pledge** to miner addresses in real time - allowing speedy miners to continue sealing quickly. (Note that this mechanism will only exist for the Space Race, not mainnet.)

Filecoin is a community-built network, and a healthy economy is built through
collaboration, not abuse. This is a good first exercise in collaboration ahead
of Mainnet launch. 🤝

**Connectivity Checker & Logs:** Miners can check their dialability and
connectivity status on [the
dashboard](https://calibration.spacerace.filecoin.io/check) to ensure they can
successfully receive storage and retrieval deals. For miners who encounter
connectivity issues, please see the [Filecoin
Documentation](https://docs.filecoin.io/mine/connectivity) to ensure your
storage miner is well configured. To track and debug any issues with storage
and retrieval deals, miners can also search for their miner and see a log of
all requests from the competition bots
[here](https://calibration.spacerace.filecoin.io/).

**Deal Filtering:** If a miner is receiving a lot of deals from other clients,
resulting in poor success with the competition bots, one can use the deal
acceptance criteria [described in the Space Race
FAQ](https://docs.filecoin.io/mine/spacerace/#how-do-i-prioritize-deals-from-
competition-bots) to only accept deals from specified clients (Client IDs for
the competition bots are included there).

**Documentation:** Based on the challenges observed in the Calibration
network, we’ve added lots of new documentation to help miners onboard
smoothly. See new pages for [miner
troubleshooting](https://docs.filecoin.io/mine/), [improving
connectivity](https://docs.filecoin.io/mine/connectivity/), and [Space Race
FAQs](https://docs.filecoin.io/mine/spacerace/#frequently-asked-questions). We
also have a [whole host of great suggestions for more documentation
improvements from the community](https://github.com/filecoin-
project/lotus/issues/2956), so expect to see more updates here as the team
works on these suggestions over the next few days. 🙏

![Launch Roadster](https://filecoin.io/vintage/images/blog/launch-
roadster.jpg)

### Space Race Events

Please join us for the **Space Race Opening Ceremony** on Wednesday, August
26th at 10pm UTC (3pm PT | 6am CST on Thursday, August 27th). We’ll celebrate
the start of Space Race and have presentations from the team.

The Space Race will also feature a number of events for participants:

  * **Weekly workshops** on Tuesdays at 6PM (PST) | Wednesdays at 9AM (CST) | 1am (UTC) 
    * 8 / 25: Filecoin Mining Workshop #1 - How to troubleshoot common issues
    * 9 / 01: Filecoin Mining Workshop #2 - Improvements and new features
    * 9 / 08: Filecoin Mining Workshop #3 - Getting ready for Mainnet
  * **Live AMAs with the Filecoin team** on Wednesdays at 6PM (PST) | Thursdays at 9AM (CST) | 1am (UTC)
  * **Miner Show and Tell** on Thursdays at 6PM (PST) | Thursdays at 9am (CST) | 1am (UTC)
  * **Space Race Report** on Fridays at 5pm (PST) | Saturdays at 8am (CST) | 12am (UTC)
  * Other special **Deep-Dives** on subjects like Filecoin’s CryptoEconomics, Mining Cluster Configuration, etc will be scheduled throughout the competition

All events will be recorded and available online. If you’d like to participate
in the Miner Show and Tell, please join the **#space-race** channel on
[Filecoin slack](http://filecoin.io/slack) where we’ll share a signup link
next week.

We’re pumped to see what the Space Race holds for all of us - and very proud
of the huge improvements we’ve made together over the past few weeks. It’s an
honor to be building this network alongside you! 🛠️

### Related Articles

[View all articles](../../../blog)

[ ](../../../blog/posts/announcing-space-race-2/)

updates

##  [ Announcing Space Race 2 ](../../../blog/posts/announcing-space-race-2/)

For the past 3 weeks, miners across the community have been participating in
the Filecoin Space Race to onboard as much storage as possible to the Testnet.

Sep 12, 2020

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

