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

Apr 17, 2020  

## Filecoin roadmap update April 2020

Our April 2020 roadmap update covers progress made since the [last roadmap
update](https://filecoin.io/blog/roadmap-update-february-2020/) and a peek
into what’s next for the Filecoin project as we get closer to the mainnet
launch.

# Where we are now

The last two months have seen significant progress across the project. There
is a lot happening in the ecosystem – thank you to everyone contributing to
the implementations, participating in the testnet, developing applications,
building tools and services, applying to devgrants, and more!

Here are a few highlights:

  * 💾 **Testnet Highlights**
    * ✨ **5PB on the Filecoin testnet.** Over the last two months, we have seen the Filecoin testnet cross **5PB of proven storage**. There are tens more PBs that are currently sealing and will soon be counted for storage power on-chain. Proven network storage is currently growing at a rate ~50 TB per day! You can expect some fluctuation in the amount of proven network storage on any given day, since some mining nodes come and go. See the up-to-date stats on our [dashboard](https://stats.testnet.filecoin.io/). Overall, this is a really strong start for the Filecoin network. We’ve seen mining interest that indicates the Filecoin mainnet might launch with hundreds of PB of storage capacity 👀! Let’s keep this momentum going. 💪 ![Recent screenshot of Filecoin testnet stats dashboard at https://stats.testnet.filecoin.io](https://filecoin.io/vintage/images/blog/dashboard-2020-04-17.jpg)
    * 🖇️ **lotus and go-filecoin interoperate.** In several of our blog posts ([1](https://filecoin.io/blog/announcing-lotus/#why-multiple-implementations), [2](https://filecoin.io/blog/announcing-filecoin-implementations-in-rust-and-c++/#the-importance-of-multiple-implementations), [3](https://filecoin.io/blog/roadmap-update-february-2020/#what-s-next)), we have mentioned the importance of having multiple interoperable implementations for the security of the Filecoin network. [In our last roadmap update](https://filecoin.io/blog/roadmap-update-february-2020/#what-s-next), we mentioned that **launching our first interop network** was one of our two main priorities before Testnet Phase 2. After a tremendous amount of hard work and testing, we have accomplished this milestone – **lotus** and **go-filecoin** can now interoperate on the same network! This is a huge milestone for the Filecoin project, and another step towards the finalization and convergence needed before we can launch the Filecoin mainnet. If you’re interested in joining the interop network, you can run [**lotus** ’s interopnet branch](https://github.com/filecoin-project/lotus/tree/interopnet) or [**go-filecoin** ’s interop branch](https://github.com/filecoin-project/go-filecoin/tree/interop) (and follow [these instructions](https://github.com/filecoin-project/go-filecoin/issues/3999), if running **go-filecoin** ). Note that we are still doing active development on these branches, and there may be bugs. If you find one, file a bug report please ([lotus GitHub issues](https://github.com/filecoin-project/lotus/issues), [go-filecoin GitHub issues](https://github.com/filecoin-project/go-filecoin/issues))!
  * 🧬 **Filecoin Node Implementation Highlights**
    * 🔍 **Completed the first round of our internal protocol security audit.** Also as mentioned in our [last roadmap update](https://filecoin.io/blog/roadmap-update-february-2020/#what-s-next), our other major priority before Testnet Phase 2 was the completion of our internal protocol security audit. Great news! We’ve finished the first round of this audit, and drafted a number of protocol changes to ensure that our mainnet launch construction is secure and economically sound. The Filecoin core developers are hard at work implementing these protocol changes, and these should land in **lotus** and **go-filecoin** within the next few weeks. More information on timing can be found in the “What’s Next” section below.
    * 🏃‍♀️🏃‍♀️🏃‍♀️ **PoRep optimizations.** Last time, we talked about optimizations we had made to our PoRep implementation. Over the last couple months, we have made more and bigger optimizations! Instead of using binary Merkle trees, we now use oct-trees, which, in combination with our [Poseidon implementation](https://github.com/filecoin-project/neptune), significantly reduce our circuit constraints, leading to fewer SNARKs in our PoRep overall. Our PoRep is a complex engine, and these optimizations are tricky and often require reworking fundamental aspects of our cryptographic construction. We will keep working on improving PoRep performance, but these optimizations go a long way toward improving the experience for our miners!
    * 👤 **Improved usability.** The **lotus** and **go-filecoin** implementations have improved usability in a number of dimensions over the last two months. These include performance improvements in chainsync, memory allocation, and message retrieval. The implementations now also have improved UX for many commands, and more + more detailed command documentation.
    * 🤝 **Offline data transfers.** Massive, petabyte-scale datasets are simply too expensive to transfer over the internet, both in terms of time and money. With very large datasets, the most economical means of transferring data is often shipping hard drives directly to your recipient. The [offline data transfer feature in lotus](https://github.com/filecoin-project/lotus/pull/1242) allows users with very large datasets to initiate storage deals with miners online, transfer data to miners offline, and have the deal work as intended on-chain. We are already seeing partners use offline data transfers on the testnet in preparation for mainnet. We will post a more specific update on some of these exciting use cases soon!
    * 🔥 **Modular, scalable storage mining architecture.** We redesigned our storage mining interfaces and implementation to support medium-size miners (tens of nodes), single-node miners, and non-Go implementations. You can find a description of the storage mining interface [here](https://github.com/filecoin-project/specs-storage) and an implementation of the interface [here](https://github.com/filecoin-project/sector-storage)!
  * 👨‍👩‍👧‍👦 **Ecosystem Highlights**
    * 🥳 **Textile Powergate.** The Textile team has been hard at work building [Powergate](https://github.com/textileio/powergate) over the last few months. Powergate offers several extremely valuable features for Filecoin users today. For example, Powergate makes it easier to store redundant copies of the same CID on the Filecoin network, manage long-term deals and deal health, and make Filecoin data available on the IPFS network. Read Textile’s most recent [Progress Update](https://blog.textile.io/filecoin-tools-progress-update-8-april/) for a summary of Powergate features and use cases. We can’t wait to access Filecoin through the Powergate – it promises to be a smooth and user-friendly experience! We can’t wait to see what comes next!
    * 🧠 **Storage Devs Show & Tell.** On March 25, members in the Filecoin community held a Storage Developers’ “Show & Tell” call, where groups building in the Filecoin ecosystem got together, demoed their projects, and started cross-pollinating ideas! Participating teams included [The Shoah Foundation](https://sfi.usc.edu/), [Small Data Industries](https://smalldata.industries/), [Node Factory](https://nodefactory.io/), [Numbers Protocol](https://numbersprotocol.io/), [Zondax](https://zondax.ch/), [Open Work Labs](https://www.openworklabs.com/), and [Textile](http://textile.io/). We’re looking forward to participating in more of these types of calls over the next few months!
    * 📀 **Filecoin tipset explorer.** Members of the Filecoin community recently created this [Filecoin Tipset Explorer](http://stats.fil-test.net:8888/), a dev tool which can be used to explore the state of the blockchain on the current testnet!
    * 🛳️ **Filecoin DevGrants Wave 2 winners announced!** Wave 2 of the Filecoin DevGrants program received 17 strong community proposals, and [6 DevGrants](https://filecoin.io/blog/filecoin-dev-grants-wave-3-new-rfps/#wave-2-projects) were ultimately awarded. Congrats to the grant recipients! These winning proposals include a [Filecoin reputation system](https://github.com/filecoin-project/devgrants/pull/82/files), [a Filecoin-backed NFT snapshot bot](https://github.com/filecoin-project/devgrants/pull/77/files), a file uploader and reader, a [mobile wallet in Flutter](https://github.com/filecoin-project/devgrants/pull/69/files), [paper submission for weighted BLS](https://github.com/filecoin-project/devgrants/pull/86/files), and [filscout.io](https://filscout.io/) – another [community-built block explorer](https://github.com/filecoin-project/devgrants/pull/74/files)!
    * 👟 **Filecoin DevGrants Wave 3.** Wave 3 of the Filecoin DevGrants program recently came to a close, with a [fresh list of RFPs](https://github.com/filecoin-project/devgrants/blob/master/rfps/new-wave-3-rfps.md). We received 44 proposals from community members (excluding proposals for the large-scale miner testing RFP, described below). Some of the RFPs and proposals included projects such as an easy-to-use storage client application with erasure coding and basic encryption, simple storage webapps, and resumable data transfers with GraphSync. We encourage you to apply to Wave 4 of the Filecoin DevGrants program due June 30th – please see more information about the program and the application instructions [here](https://filecoin.io/grants/).
    * 🐳 **~50 proposals received for large-scale miner testing.** Towards the end of February, the Filecoin DevGrants program published an [RFP](https://github.com/filecoin-project/devgrants/blob/master/rfps/rfp-pbscale-miner-testing.md) for large-scale miners (5PB+ in storage capacity) to help test various features of the Filecoin implementations and network, such as sealing rates, _Proof-of-Spacetime_ performance, benchmarks, optimal hardware and software configurations, and more. This RFP received 48 applications from large miners – we’re excited to work with some of these mining teams to improve network robustness and performance in advance of mainnet!
    * ✏️ **Filecoin Community Highlights series.** Over the next few weeks, we will be featuring Filecoin use cases and developers in the community who are building essential tools and services on the Filecoin network. We hope these stories inspire others to join us in our mission to build world-class tools for the distributed web. Our first highlights feature [Textile](https://filecoin.io/blog/community-andrew-hill-textile/) and [Numbers Protocol](https://filecoin.io/blog/community-tammy-yang-bofu-chen-numbers/). More to come soon!
    * 🙋 **March Q &A with Juan Benet.** In early March, we held an online Q&A session with Juan Benet, founder of the Filecoin Project. During this 1-hour session, we fielded hundreds of questions from more than 1,200 community members all over the world. Questions ranged from hardware requirements, to timelines, to the inner workings of our proofs construction! You can read more about the event in our recap [here](https://filecoin.io/blog/march-q-and-a-thank-you/).
    * 🌟 **Gemini support.** Gemini announced [on its blog](https://gemini.com/blog/upcoming-support-for-filecoin) that it will be supporting the custody of Filecoin. Excited that Gemini will be part of mainnet launch and beyond!
    * 📢 **Testimony in U.S. Congress’s Small Business Committee.** Protocol Labs’ Marvin Ammori testified in a [congressional hearing](https://www.youtube.com/watch?v=Y44NAunjNXw&feature=youtu.be) before the U.S. House of Representatives’ Small Business Committee in early March to discuss the benefits of blockchain for small businesses. Read his [testimony](https://smallbusiness.house.gov/uploadedfiles/03-04-20_mr._ammori_testimony.pdf) online, and a related [op-ed ](https://morningconsult.com/opinions/how-blockchain-can-boost-small-businesses/)in _Morning Consult_.
    * 🌐 **IPFS Q1 2020 Update.** The IPFS Project recently published its [Q1 2020 update](https://blog.ipfs.io/weekly-84/), highlighting some of the growth and activity within the IPFS ecosystem. Some highlights to call out here: the [IPFS Roadmap for 2020](https://blog.ipfs.io/2020-02-10-our-focus-for-2020/) was announced, the [IPFS Netflix collaboration leads to new improvements in IPFS Bitswap](https://blog.ipfs.io/2020-02-14-improved-bitswap-for-container-distribution/), and IPFS is [now supported out of the box in Opera for Android](https://blog.ipfs.io/2020-03-30-ipfs-in-opera-for-android/). We encourage you to read the full update, it’s exciting to see a summary of some of the great things that are happening in the ecosystem!

In short, the last two months demonstrated important progress across protocol,
engineering, and ecosystem. It’s not easy to persevere in a more difficult
global context, and we’re proud of the work we’ve done to date, our current
velocity, and the acceleration of energy and efforts we are seeing in the
ecosystem!

# What’s next

We are continuing to make progress towards our mainnet roadmap, and updating
estimates and milestones as we get better information (especially related to
protocol and network security). See our public project roadmap (the Gantt
chart) [here](https://app.instagantt.com/shared/s/1152992274307505/latest). We
would like to highlight some recent updates regarding our project roadmap.

**(1) Hardware specs timing.** As mentioned in the highlights above, we are
working hard to optimize and improve the _Proof-of-Replication_ (PoRep) we
will be using for mainnet. We have a new version implemented, and ready to go.
But we are trying hard with another new version, that is significantly faster
and cheaper, but not yet certain to work. This second one would significantly
decrease the cost of computation over storage, and likely change which
computation hardware is optimal. We will know in May if this one will work or
not. From that point, we can run all the benchmarks to make hardware
recommendations. We recommend that miners do not purchase proving hardware at
scale yet. Because our PoRep could change, this might yield different optimal
hardware configurations in a few weeks.

**(2) Testnet Phase 2 - Rewards.** We will be offering some rewards for
participating in specific tests during Testnet Phase 2. We are still working
out the details, but it looks like we will be able to have over **1 million
FIL** in rewards across a wide variety of tests. (FIL will be delivered after
mainnet launch and subject to some vesting/time locks). The tests will measure
miners’ ability to store and transfer files, for example: total amount of
storage capacity, storage deals made, files retrieved, data serving bandwidth,
data serving latency, and more. The critical time period for these tests will
most likely be 2-3 weeks within the month of **June**. We will publish more
details in **May,** so that miners have enough time to prepare.

**(3) Testnet Phase 2 - Timing Decision.** All 4 implementation teams are
pushing a lot of code right now implementing a number of hard protocol
changes, ahead of **Testnet Phase 2**. We originally hoped to have the full
code for mainnet ready in **lotus** and **go-filecoin** _before_ starting
Testnet Phase 2, but we are not there yet. Testing, optimization, internal
protocol security audits, and cryptoeconomic analysis have resulted in several
important changes being finalized and implemented now. This led us to a
decision point regarding the timing of Testnet Phase 2.

For this decision, the dev teams wanted to gather input from a broader set of
stakeholders before making the final call. We know that as time passes, the
Filecoin community – especially Filecoin Miners – will need to make more and
more decisions for the long-term good of the network, so this decision was a
good opportunity to practice.

We conducted an informal information-gathering poll on our [Filecoin community
Slack](https://join.slack.com/t/filecoinproject/shared_invite/zt-dj58b7fq-
weyaTEvjHoYF_ENkQHR6Ig), where our most engaged miners and other community
members converse. We presented three timing options. In all three options, we
included an adjustment to estimates for our mainnet launch window, pushing it
out by 2 weeks to account for all of the work that needs to happen in that
period, including testing and validation, security audits, network operations
testing, testing Filecoin improvement proposals and network upgrades, and
more. The three options were:

  * **Option 1 - Testnet Phase 2 around April 20, Mainnet launch window from August 3 to September 4.** This option would mean us launching Testnet Phase 2 next week, as estimated, but without all of the protocol changes that are being implemented now. The final proofs and consensus would not be in place, so large changes would have landed during testnet as network upgrades, making the network shakier during that time and increasing the overall time to mainnet.
  * **Option 2 - Testnet Phase 2 around May 11, Mainnet launch window from July 20 to August 21.** This option would have us land the most critical protocol changes first, and then implement the rest as protocol upgrades during testnet. Executing these changes as protocol upgrades on a live network would increase the time to mainnet, but would also be a good opportunity for us to practice formal network upgrades in testnet.
  * **Option 3 - Testnet Phase 2 around May 25, Mainnet launch window from July 6 to August 7.** This option would have us wait until all the mainnet changes are done and ready. We would take longer to launch Testnet Phase 2 and we would not exercise formal upgrades in testnet, but this would likely be the fastest path to mainnet launch.

There were ~100 community members who expressed an opinion in the poll, with
about equal support for Options 2 and 3, and little support for Option 1 (<
20%). When we considered the input weighted by impact and contribution to the
network so far, Option 2 edged ahead of Option 3. Thank you to everyone who
participated, and especially those who considered the long-term health of the
network in their preferences!

Ultimately, the decision rests with the **lotus** , **go-filecoin** , and
testnet developers, but the input gathered from the community was an important
factor in their decisionmaking process. The dev teams have chosen **Option 2,
which leads to an estimated Testnet Phase 2 launch the week of May 11 and an
estimated mainnet launch window from July 20 to August 21.** We have updated
the [public project roadmap Gantt
chart](https://app.instagantt.com/shared/s/1152992274307505/latest) to reflect
these new estimates. If a security vulnerability or other major concern
arises, we will make sure to take the requisite time and fully address the
problem before our mainnet launch. We sincerely hope this isn’t required, but
it is a necessary part of our commitment to launching a secure blockchain
network.

Please remember that these dates are still best-effort **optimistic
estimates** based on the latest information available, as requested by the
community. They are not promises, nor are they conservative estimates. These
estimates are not at all any kind of guarantee. These are open estimates, for
an open community, and for the broader teams of people working on Filecoin
across a number of organizations. Having real-time best-effort information is
best for all the developers and miners trying to coordinate across many
different organizations – it is not an end-user consumer product date with
overly conservative dates.

We’re constantly reminded that building a blockchain is like building a
software rocket – it is fundamentally hard, and we have to be extraordinarily
careful to make sure that what we launch is secure and stable. We’re rolling
full steam ahead, as fast as we responsibly can. Every day, the number of
opportunities to participate in the ecosystem only grows, so if you believe in
the same vision of the world that we do, please keep an eye out for those
opportunities and/or [reach out to the
community](https://filecoin.io/#community) on our discussion forum or on
Slack! As ever, we’re excited and grateful to be building alongside you. 🛠️

Onwards!

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

