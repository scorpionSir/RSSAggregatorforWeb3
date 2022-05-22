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

Jul 14, 2020  

## Getting Ready for Filecoin’s Space Race

As we enter the home stretch into Filecoin’s mainnet launch,
[Lotus](https://docs.lotu.sh/) (the Filecoin reference implementation) is
making fast progress. In the past 2 weeks alone the team has landed a [major
data transfer improvement](https://github.com/filecoin-project/go-data-
transfer/pull/55) to the Filecoin market implementation, finished up the final
sector-lifecycle features for [verified](https://github.com/filecoin-
project/go-fil-markets/pull/304) & [fast-
retrieval](https://github.com/filecoin-project/lotus/pull/2323) deals and
[upgrading Committed Capacity sectors](https://github.com/filecoin-
project/lotus/pull/2220), and shipped large improvements to the [Filecoin
actors](https://github.com/filecoin-project/specs-actors/releases). The mining
community is also accelerating quickly, with miners all over the world
onboarding petabytes of storage onto the Filecoin Testnet - which reached a
new milestone of **20PB of onboarded storage** this week. 🎉

![](https://filecoin.io/vintage/images/blog/testnet-stats-jul-14.jpg)

In the path to mainnet launch, our next big milestone is the launch of the
[Filecoin Testnet Incentives Program](https://filecoin.io/blog/announcing-
testnet-incentives/) \- nicknamed the _Filecoin Space Race_. This
collaborative competition is intended to stress-test the network, encourage
participation all over the world, and help miners get ready to run the world’s
biggest decentralized storage network. In this 3-week competition, miners will
compete to onboard as much storage capacity as possible to the network. The
top 100 miners globally, as well as the top 50 miners from each continent,
will earn Filecoin rewards based on how much storage they and the network
achieve during the competition period. In addition to rewarding competition
winners, Filecoin tokens from Space Race are intended to help miners onboard
their storage capacity quickly on the Filecoin mainnet, and additional
optimizations are in the works to make this an even smoother onboarding
process. For a reminder on the rules and eligibility requirements, see our
[announcement blog post](https://filecoin.io/blog/announcing-testnet-
incentives/).

### New Block Reward Incentive

In addition to onboarding storage capacity - an important part of validating
the Filecoin network works as intended to _create a decentralized, efficient,
and robust foundation for humanity’s information_ is testing the actual mining
of blocks in the Filecoin blockchain. Once the main network launches, this
will be one of the main ways that miners are rewarded for operating the
network. Therefore, to ensure the testnet incentives competition closely
mimics the dynamics of the mainnet, we’re excited to announce an **additional
prize of 100K FIL** to be split proportionally among the 20 largest block
reward winners. This additional reward pool will abide by the same [rules and
requirements](https://filecoin.io/blog/announcing-testnet-incentives/#rules)
as the storage race, and have its own leaderboard.

Please join the **#space-race** channel on [Filecoin
slack](https://filecoin.io/slack) for the latest updates!

### Filecoin Bug Bounty Program

Running a testnet incentives program is a critical step ahead of mainnet
launch to identify and fix any bugs or critical security issues before the
mainnet is live. Therefore, we **strongly encourage** Space Race participants
to use this testnet to evaluate and report any potential attacks, issues, or
bugs they may find in the Filecoin protocol or reference implementation.
**Please stress test the network, try to break things, and report any issues
you encounter!**

To help with that, we’ll be rewarding participants through our new [**Filecoin
bug bounty program**](https://bounty.filecoin.io/) to earn Filecoin for
helping improve the network. If you’re interested in finding and squashing
bugs, and getting rewarded for it, check it out! We’ll also be announcing
additional targets and bounties on the [bug bounty
website](https://bounty.filecoin.io/) ahead of the Space Race competition.

### New Incentives Calibration Period

We’ve been planning for a July 20th launch for our testnet incentives program,
but have heard a [strong request from the
community](https://filecoinproject.slack.com/archives/CPFTWMY7N/p1594401718461200)
to create a window for competition participants to try out their mining setups
with the latest features and real competition conditions - including the
leaderboard(s), storage and retrieval deal evaluation system, and updated
economic parameters. Many improvements have landed in the last few weeks, and
both miners and developers want to ensure they’re well tested ahead of the
competition.

Therefore, we’re adding a 2-week calibration period prior to our 3-week
competition. During this 2-week calibration period (July 20-Aug 2), miners
will be able to practice in real competition conditions and see how their
performance influences hypothetical competition standings. This will take
place on a new devnet with all the latest features and optimizations. We’ll
reset the Filecoin Testnet and begin the official 3-week competition period
the week of August 3rd.

During this 2-week calibration period, miners are heavily encouraged to
transition their main attention and focus to the Space Race devnet in order to
identify and debug any issues with their setups ahead of competition launch.
Please join the **#space-race** channel on [Filecoin
slack](https://filecoin.io/slack) where we will share instructions on how to
get started next week!

The Space Race will also feature a number of events for participants:

  * Opening and closing ceremonies
  * AMAs with competition organizers to answer questions on network incentives, program structure, and eligibility rules
  * Workshops to help miners better understand the latest updates to Filecoin’s cryptoeconomic parameters, the new features landed in Lotus over the last few weeks, how to efficiently configure large-scale mining setups to make the most of the competition, and more
  * AMAs with Filecoin community participants
  * Opportunities for participating teams to present their setups
  * And more!

### Roadmap Update

While we’re excited to give the mining community (and the development team)
more time to make the most of this competition, we cannot compress the time
between the Space Race and Filecoin’s Mainnet Launch. This is a critical
window for critical bugfixing, operational setup time, and final parameter
optimizations following the testnet incentives program. Therefore, we’re
updating our mainnet launch window to **August 31st - September 21st** to
reflect this additional calibration period.

As usual, we will keep the [public project roadmap Gantt
chart](https://app.instagantt.com/shared/s/1152992274307505/latest) updated
with the latest estimates for upcoming milestones. Please remember that these
dates are still best-effort optimistic estimates based on the latest
information available, as requested by the community. They are not promises,
conservative estimates, or any kind of guarantee. If a security vulnerability
or other major concern arises, we will make sure to take the requisite time
and fully address the problem before our mainnet launch. We sincerely hope
this isn’t required, but it is a necessary part of our commitment to launching
a secure blockchain network.

As ever, we’re excited and grateful to be building alongside you. 🛠️

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

