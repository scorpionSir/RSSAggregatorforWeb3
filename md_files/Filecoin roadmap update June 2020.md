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

Jun 24, 2020  

## Filecoin roadmap update June 2020

Our June 2020 roadmap update covers progress made since the [last roadmap
update](https://filecoin.io/blog/roadmap-update-april-2020/) and a peek into
what’s next for the Filecoin project as we enter the homestretch to the
mainnet launch.

### Where we are now

The last two months have seen significant progress across the project. There
is a lot happening in the ecosystem — thank you to everyone contributing to
the implementations, participating in the testnet, developing applications,
building tools and services, applying to devgrants, and more!

Here are a few highlights:

  * 💾 **Testnet Highlights**
    * **2️⃣ Testnet Phase 2.** We launched [Phase 2 of the Filecoin Testnet](https://filecoin.io/blog/filecoin-testnet-phase-2-is-here/) on May 14th — in accordance with the “Option 2” timing selected by core implementers & recommended by the community. This major milestone includes two interoperable Filecoin implementations ([ **go-filecoin**](https://github.com/filecoin-project/go-filecoin) and [**lotus**](https://github.com/filecoin-project/lotus/)), implementations of WinningPoSt and WindowPoSt (the two flavors of Filecoin _Proofs-of-Spacetime_ we use in the protocol), and Drand (a distributed randomness beacon network) as an external source of randomness for consensus. Testnet Phase 2 also included large improvements to our actors and storage market implementations, and [refined cryptoeconomic structures](https://filecoin.io/blog/filecoin-cryptoeconomic-constructions/). For how to get started on the testnet, check out our [new documentation site](https://docs.filecoin.io/).
    * ✨ **Filecoin Testnet Phase 2 reached 9PB.** The Phase 2 testnet reached 9PB of proved data within ~1 month, nearly 2x our previous high watermark. Last week, we reset our testnet to take advantage of the latest Lotus and Proofs optimizations. Since then, we’ve already seen over 6 PB of data onboarded with the network growing by 15 GB/sec, or around 1.2 PB/day. See the up-to-date stats on our [dashboard](https://stats.testnet.filecoin.io/). ![Testnet Stats](https://filecoin.io/vintage/images/blog/fil-testnet-stats.jpg)
    * **💸Incentivized testnet.** Earlier this month, we announced the rules and hardware recommendations for [incentivized testnet](https://filecoin.io/blog/announcing-testnet-incentives/), our 3 week collaborative competition intended to stress-test the network, encourage participation all over the world, and provide miners with an opportunity to test-drive Filecoin in advance of the mainnet launch. Miners will need to successfully complete real storage and retrieval deals and execute the full sector life cycle — creating committed capacity sectors, upgrading them to store real data, and terminating them — to be eligible for rewards. Join us for a Filecoin Live Q&A this Thursday at [filecoin.io/slack](https://filecoin.io/slack) to learn more.
  * 🧬 **Filecoin Implementation Highlights**
    * **🏃‍♀️Performance and Reliability improvements.** A major focus for our work since starting Testnet Phase 2 has been hardening and making efficiency improvements to our core implementation subsystems. We fixed issues related to sealing that were reported shortly after we launched Testnet Phase 2. We also improved sync time significantly by [batching PoRep verifications](https://github.com/filecoin-project/specs-actors/pull/340), allowing them to be performed in parallel. Now, if sync is interrupted before reaching the target height, it [picks up where it left off](https://github.com/filecoin-project/lotus/pull/1705) instead of restarting from genesis. Thank you to the many community members who have participated in finding bugs and helping fix them - special thanks [@hayeah](https://github.com/hayeah) for the sync improvement!
    * **🔋Hardware specs & PoRep for Mainnet Launch.** Filecoin will use the **SDR _Proof-of-Replication algorithm_** for our testnet incentives competition and for mainnet launch. **Note:** Miners should expect Filecoin to regularly upgrade its proofs after launch. While the Filecoin team does not recommend any specific hardware configuration, we did [share some setups ](https://filecoin.io/blog/announcing-testnet-incentives/#hardware)we’ve used for various types of testing. However, it is overwhelmingly likely that there are more efficient setups, and we strongly encourage miners to test and experiment to find the best combinations.
    * **⚖️ Filecoin’s cryptoeconomic constructions**. We made significant progress on defining and solidifying Filecoin’s cryptoeconomic constructions to ensure that the network can support the long-term needs of its clients and provide a solid foundation for Filecoin’s mainnet launch. While we’re still conducting extensive modeling and testing to finalize parameters, [this overview](https://filecoin.io/blog/filecoin-cryptoeconomic-constructions/) describes how the cryptoeconomic structure of Filecon will create a public blockchain powered by useful work, a reliable cloud storage service, and a thriving decentralized economy.
    * 🤝 **Offline data transfers.** For petabyte-scale datasets and larger, the most sensible solutions often involve shipping data on hard drives. Filecoin’s [offline data transfer feature](https://filecoin.io/blog/offline-data-transfer-for-large-scale-data/) allows users with very large datasets to complete the data transfer step offline (e.g. by shipping hard drives from the client to the storage miner), and have the storage and retrieval deals work as intended on-chain.
    * **💇‍♀️Proof efficiency and memory utilization improvements.** We’ve made changes to how we seal data that have significantly improved the memory usage and performance of sealing. Similarly, [Neptune](https://github.com/filecoin-project/neptune) (our Rust implementation of the Poseidon hash function tuned for Filecoin) now allows us to build merkle trees on GPU. These performance improvements continue to make Filecoin more efficient and accessible to a wide community of miners.
    * **🔐 Phase 2 Trusted Setup.** Phase 2 of our Trusted Setup Ceremony has begun on the first set of circuits, with more participants joining over the coming weeks. In preparation, we significantly reduced the memory required for our “large circuits”, which will allow much smaller participant hardware for our Phase 2 Trusted Setup Ceremony. Community participation begins on June 29th, so come [sign up today](https://forms.gle/XxLgsHmxdPjb7jJa9) to participate.
  * 👨‍👩‍👧‍👦 **Ecosystem Highlights**
    * **🔍 Filecoin Discover.** The purpose of [Filecoin Discover](https://filecoin.io/blog/intro-filecoin-discover/) is to help seed Filecoin as the home for humanity’s most important datasets and make it accessible to others. Datasets include: [ENCODE](https://www.encodeproject.org/), [1000 Genomes](https://www.internationalgenome.org/), [Project Gutenberg](https://www.gutenberg.org/), [Berkeley’s Self Driving Data](https://bdd-data.berkeley.edu/), and more. Since May 7th, Filecoin miners have signed up to store **dozens** of petabytes worth of important data.
    * 🥳 **Textile Powergate.** With a number of hackathons coming up, [Textile Powergate](https://docs.textile.io/powergate/) and [Buckets](https://docs.textile.io/hub/buckets/) are a great way to get started building on Filecoin. [Last week’s tutorial](https://blog.textile.io/buckets-diffing-syncing-archiving/) explains how to create a Bucket and archive your data in the Filecoin network using Powergate under the hood. If you’d like to build an app on top of Powergate, you can also follow the [JS client tutorial ](https://blog.textile.io/integrating-powergate/)to learn more. Textile Hub, a collection of hosted IPFS, Filecoin, and ThreadsDB nodes that make it easy for developers to onboard on Textile, is also adding support for Filecoin in the next few weeks as well. Learn more about these great tools for developers in Textile’s recap from the [IPFS Pinning Summit](https://blog.textile.io/learn-more-about-threads-and-the-powergate-from-the-ipfs-pinning-summit/).
    * 🧠 **Storage Devs Show & Tell.** On June 23rd, members in the Filecoin community held our second Storage Developers’ “Show & Tell” call, where groups building in the Filecoin ecosystem got together, demoed their projects, and started cross-pollinating ideas. Presenting teams included [Fleek](https://fleek.co/), [Starling](https://starlingstorage.io/getting-started.html), and [Textile](https://textile.io/). It’s always awesome to see what these groups are building to make Filecoin easier to use!
    * **👫 Filecoin Virtual Community Meetup.** On Tuesday, June 16th, the Filecoin team hosted our very first Filecoin Virtual Community Meetup! Our community meetups are an opportunity to meet the people behind the many tools and projects being built in the Filecoin ecosystem. If you missed it, you can find the [recap blog post here](https://filecoin.io/blog/filecoin-virtual-community-meetup-recap/) which features the meetup recording. Hope to see you at our next virtual meetup on July 14th!
    * **📞 Mining Community Call.** We hosted our second [Filecoin Mining Community Call](https://filecoin.io/blog/miner-community-call-may-2020/) at the end of May - a big thank you to everyone who [asked questions](https://filecoin.io/blog/mining-community-call-thank-you/)! The call included updates on our growing miner ecosystem, Verified Clients, Filecoin Discover, and Testnet Incentives. Check out the recap [here](https://filecoin.io/blog/mining-community-call-thank-you/) and join our next Mining Community Call in Q3.
    * 🌟 **Custody support.** Token custodians [Gemini](https://gemini.com/blog/upcoming-support-for-filecoin), [Coinbase](https://blog.coinbase.com/coinbase-custody-to-support-celo-gold-cgld-filecoin-fil-keep-network-keep-near-protocol-6b54fc4c183a), and [Anchorage](https://medium.com/anchorage/anchorage-to-support-custody-and-unlocking-contracts-for-filecoin-at-launch-b4f514012793) have all announced support for custodianship of Filecoin tokens at mainnet launch. Anchorage will also support unlocking contracts for Filecoin at launch. If you plan to hold Filecoin, check out these custodian options to learn more.
    * 🛳️ **Filecoin DevGrants Wave 3.** We received a tremendous response from community members to the [Wave 3 RFPs](https://github.com/filecoin-project/devgrants/blob/master/rfps/new-wave-3-rfps.md) including 44 proposals (an additional 48 proposals were received for the PB-scale miner testing RFP alone). Grant recipients are being notified and a full list will be published soon. Winning Wave 3 proposals included a MetaMask SNAP plugin for Filecoin, User Research with professional archivists at museums and similar orgs, a Data CID Status Checker and Storage Oracle, Filecoin Cloud Images, a Proxy Re-encryption service to support data forwarding use cases, and a Multichain API among a number of other projects. Wave 4 of the Filecoin DevGrants program closes on July 1st — [apply here](https://filecoin.io/grants/)!
    * ✏️ **Filecoin Community Highlights series.** The Filecoin blog has been featuring Filecoin use cases and developers in the community who are building essential tools and services on the Filecoin network. We hope these stories inspire others to join us in our mission to build world-class tools for the distributed web. Our latest highlights feature [Small Data Industries](https://filecoin.io/blog/community-ben-fino-radin-sdi/) and [Open Work Labs](https://filecoin.io/blog/community-jonathan-schwartz-owl/). More to come soon!
    * 🙋 **May Q &A with Juan Benet.** Following the launch of Testnet Phase 2, we held an online Q&A session with Juan Benet, founder of the Filecoin Project. During this 1-hour session, we fielded hundreds of questions from more than 1,400 community members all over the world. Questions ranged from roadmap and timing updates to details on verified clients, hardware requirements, and the latest on testnet incentives! You can read more about the event in our recap [here](https://filecoin.io/blog/may-q-and-a-thank-you/). Our next Q&A is this Thursday, June 25th - join us in the **#fil-ama** channel on [Slack](https://filecoin.io/slack) to learn more.

### What’s next

We are continuing to make fast progress towards our mainnet roadmap. See our
public project roadmap (the Gantt chart)
[here](https://app.instagantt.com/shared/s/1152992274307505/latest). We would
like to highlight some notable upcoming milestones.

**(1) Go-Filecoin graduating to community maintenance.** As we’ve [explained
in the past](https://filecoin.io/blog/announcing-lotus/#why-multiple-
implementations), having multiple independent implementations of the Filecoin
protocol is important for the long-term security and resilience of the
Filecoin Network. Each of the 4 Filecoin implementations have made huge
strides in the past few months:

  * In April, we launched our first interop network with both [**lotus**](https://github.com/filecoin-project/lotus) and [**go-filecoin**](https://github.com/filecoin-project/lotus) nodes interoperating. Shortly after that, we launched [Testnet Phase 2](https://filecoin.io/blog/filecoin-testnet-phase-2-is-here/) including both interoperable implementations and updated _Proofs-of-Spacetime_.
  * [**Fuhon**](https://github.com/filecoin-project/cpp-filecoin), the Filecoin C++ implementation by Soramitsu, has been working hard to add full interoperability. The team is making good progress and will be joining Testnet in the coming weeks.
  * [**Forest**](https://github.com/ChainSafe/forest), the Rust Filecoin implementation by ChainSafe, has recently updated proofs and market actors and is actively working on chain sync and data propagation - including a Rust implementation of [Bitswap](https://github.com/ipfs/go-bitswap/blob/master/docs/how-bitswap-works.md), IPFS’s data sync algorithm.

Now, as we turn the corner towards mainnet launch, we’re excited to graduate
[**go-filecoin**](https://github.com/filecoin-project/go-filecoin) to
community maintenance. Having all 4 implementations of Filecoin be managed and
improved by different teams gives each the focus and independence to meet our
longstanding decentralization and security objectives for the wider Filecoin
network.

To that end, we’re offering a [Wave 4 DevGrant
RFP](https://github.com/filecoin-project/devgrants/issues/140) for teams
interested in taking on maintainership for **go-filecoin** going forward.
**go-filecoin** is nearly feature-complete; taking it across the finish line
for mainnet launch could create several future opportunities for teams that
maintain the project. For example, if highly optimized to be a great product
for miners, **go-filecoin** could become the implementation of choice for a
large portion of the Filecoin community. Additionally, developing deep
expertise in understanding and building Filecoin nodes can unlock other
businesses, such as hosting nodes as a service and/or building second-layer
products and solutions for the greater Filecoin ecosystem. **Please get in
touch** [**via GitHub**](https://github.com/filecoin-
project/devgrants/issues/140) **if you’re interested!**

Each of the four implementations is getting closer to feature-complete for the
Filecoin mainnet launch. Here’s a snapshot of their progress across the
primary parts of the Filecoin protocol:

| lotus | go-filecoin | forest | fuhon  
---|---|---|---|---  
1\. Node | ✅ | ✅ | ✅ | ✅  
2\. Files & data | ✅ | 🔶 | 🔶 | ✅  
3\. Virtual Machine | ✅ | ✅ | 🔶 | 🔶  
4\. VM Actors | 🔶 | 🔶 | 🔶 | 🔶  
5\. Blockchain | ✅ | ✅ | ✅ | ✅  
6\. Token | ✅ | ✅ | ✅ | ✅  
7\. Storage Mining | ✅ | 🔄 | 🔄 | 🔄 🔶  
8\. Market | ✅ | ✅ | 🔄 | ✅  
  
_✅ :fully featured implementation | 🔄 :reuses components from another
implementation | 🔶 :partial implementation_

**(2) Filecoin Ignite.** To help support the fast-growing Filecoin ecosystem,
we’re excited to launch [Filecoin Ignite](https://ignite.fil.events/) to bring
the community together for a series of hackathons and learning events. We
currently have 6 main events lined up including:
[SpaceRace](https://filecoin.io/blog/announcing-testnet-incentives/), a world-
wide competition for Filecoin Miners, and [HackFS](https://hackfs.com/), a 30
day virtual hackathon in collaboration with the ETHGlobal team starting on
July 6th. We’re also participating in the [Spark University
Hackathon](https://filecoin.io/blog/spark-university-hackathon/), an 8 week
online competition bringing together developers from universities around the
world to build on Filecoin.

[Reach out and let us know](https://forms.gle/yhGiSC8rRcAY9YvE8) if you’d like
to host an Ignite event! With over 4 Million FIL and 250K USD in prizes spread
out across events, now is a great time to start building on Filecoin. 🚀

**(3) Trusted Setup.** [Phase 2 of our Trusted Setup
Ceremony](https://filecoin.io/blog/trusted-setup-update/) — where participants
from all over the world contribute their resources to help generate secure
parameters for the Filecoin network, along with public attestations for anyone
to verify — has begun on the first set of circuits. More participants are
joining over the coming weeks, with community participation beginning on June
29th. To participate: fill out [this
form](https://forms.gle/XxLgsHmxdPjb7jJa9) and join the **#fil-trustedsetup**
room on [Slack](https://filecoin.io/slack) where we’ll be coordinating with
participants. Thanks for your support!

**(4) Testnet Incentives Program.** The [Testnet Incentives
Program](https://filecoin.io/blog/announcing-testnet-incentives/) (also known
as [SpaceRace](http://ignite.fil.eth.link/)) is a 3 week cooperative
competition to encourage active participation in the Filecoin testnet. **We’re
aiming to start the competition on July 20th** _(pending final features,
testing, and competition preparation)_! Miners will need to successfully
complete real storage and retrieval deals and execute the full sector life
cycle to be eligible for global and regional pools totaling **up to 4 million
FIL** in rewards (to be delivered after mainnet launch, subject to some
vesting/time locks). Join us for a Filecoin Live Q&A this Thursday in the
**#fil-ama** channel on [Slack](https://filecoin.io/slack) to learn more.

### We’re in the homestretch.

Filecoin is getting closer to mainnet launch, and the whole project continues
to pick up steam. Our roadmap currently places launch near the end of our
mainnet launch window. As before, we will update the [public project roadmap
Gantt chart](https://app.instagantt.com/shared/s/1152992274307505/latest) with
the latest estimates for upcoming milestones – including Filecoin Ignite,
SpaceRace (our testnet competition), and Trusted Setup. Please remember that
these dates are still best-effort **optimistic estimates** based on the latest
information available, as requested by the community. They are not promises,
conservative estimates, or any kind of guarantee. If a security vulnerability
or other major concern arises, we will make sure to take the requisite time
and fully address the problem before our mainnet launch. We sincerely hope
this isn’t required, but it is a necessary part of our commitment to launching
a secure blockchain network.

We’re constantly reminded that building a blockchain is like building a
software rocket — it is fundamentally hard, and we have to be extraordinarily
careful to make sure that what we launch is secure and stable. We’re rolling
full steam ahead, as fast as we responsibly can. Every day, the number of
opportunities to participate in the ecosystem only grows, so please jump in to
help and/or reach out to the community on our [discussion
forum](http://discuss.filecoin.io/) or on [Slack](https://filecoin.io/slack)!
As ever, we’re excited and grateful to be building alongside you. 🛠️

Onwards!

### Related Articles

[View all articles](../../../blog)

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

[ ](../../../blog/posts/meet-andrew-hill/)

interviews

##  [ Meet Andrew Hill, Co-Founder and CEO of Textile
](../../../blog/posts/meet-andrew-hill/)

Welcome to the first blog post in our Filecoin Community Highlights series.
Over the next few weeks, we will be featuring Filecoin use cases and
developers in the community who are building essential tools and services on
the Filecoin network.

Mar 23, 2020

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

