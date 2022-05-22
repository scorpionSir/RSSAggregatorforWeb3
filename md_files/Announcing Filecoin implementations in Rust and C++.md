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

Jan 31, 2020  

## Announcing Filecoin implementations in Rust and C++

Today, we are excited to announce two additional implementations of the
Filecoin protocol: [**forest**](https://github.com/ChainSafe/forest) – being
implemented in Rust by ChainSafe, and [**fuhon**](https://github.com/filecoin-
project/cpp-filecoin) – being implemented in C++ by Soramitsu. These
implementations are in active development, and are now fully open for anyone
to use or contribute to. Check them out on GitHub!

### The importance of multiple implementations

As we first mentioned in [this blog post](https://filecoin.io/blog/announcing-
lotus/), launching the Filecoin network with multiple implementations is a key
part of our network security strategy. Having multiple software
implementations that interoperate on the same network reduces the risk that a
significant bug in _one_ implementation rears its head and takes down the
entire network.

Additionally, the success of any open source project – such as Filecoin –
rests on a strong community that is collectively involved in building and
stewarding the project. Ultimately, Protocol Labs will be just one of **many**
parties devoting their energy, talent, and resources to making Filecoin an
important building block of the internet’s evolving infrastructure. We are
very excited to see the exceptional teams of ChainSafe and Soramitsu building
implementations and providing more security to the broader Filecoin ecosystem.

Today, there are **four full node implementations** of the Filecoin protocol
in progress. This is a huge step forward for increasing Filecoin network
security and growing the Filecoin ecosystem!

[![Four Filecoin
Implementations](https://filecoin.io/vintage/images/blog/four-
implementations.png)](https://filecoin.io/vintage/images/blog/four-
implementations.png)

While the four Filecoin implementations are not yet feature-complete, they are
getting really close. As published in our [most recent roadmap
update](https://filecoin.io/blog/testnet-phase-2-update/), we are aiming for
network interoperability between **lotus** and **go-filecoin** within the next
few weeks. Interoperability with **fuhon** and **forest** will follow shortly
afterwards. In the meantime, you can follow each implementation’s progress at
its respective repo on GitHub:

  * [**go-filecoin**](https://github.com/filecoin-project/go-filecoin) (written in Go)
  * [**lotus**](https://github.com/filecoin-project/lotus) (written in Go)
  * [**fuhon**](https://github.com/filecoin-project/cpp-filecoin) (written in C++)
  * [**forest**](https://github.com/ChainSafe/forest) (written in Rust)

### About ChainSafe and Soramitsu

For our first batch of implementation grants, we chose to partner with
ChainSafe and Soramitsu because of these teams’ core alignment with the
mission and values of the web3 space and their deep experience with
implementing complex blockchains. We are excited to have these exemplary teams
contributing to the Filecoin ecosystem!

### ChainSafe

[ChainSafe Systems](https://chainsafe.io/) is a blockchain R&D firm that is
building infrastructure for Web3. ChainSafe started several years ago as a
group of developers who met at early Ethereum meetups. Ever since, the team
has been building in the Ethereum, Ethereum Classic, Cosmos, Polkadot, and now
Filecoin ecosystems. In addition to the Rust Filecoin implementation,
ChainSafe is building Ethereum 2.0 and Polkadot protocol implementations. You
can read more about the team and their Rust implementation of Filecoin
[here](https://medium.com/chainsafe-systems/announcing-forest-chainsafes-
implementation-of-filecoin-in-rust-675d176be517).

### Soramitsu

[Soramitsu](https://soramitsu.co.jp/) is a boutique Japanese fintech company
with expertise creating blockchain-based infrastructure, payment systems, and
identity solutions. The Soramitsu team has deep experience building
enterprise-grade fintech systems; this commitment to robustness and high
software quality is especially important when building software rockets (e.g.
blockchains). In addition to the C++ Filecoin implementation, Soramitsu is
currently building a Polkadot implementation in C++ and is also the lead
maintainer of the [C++ implementation of
libp2p](https://github.com/soramitsu/libp2p).

### Let’s collaborate!

We are always looking for mission-aligned partners to collaborate with as we
grow the Filecoin ecosystem. If you already have an idea for something to
build or want to check out our open RFPs, apply to the [Filecoin DevGrants
program](https://filecoin.io/grants/)! If you’re interested in brainstorming
and learning more about ways to get involved, kick off a thread at
<https://discuss.filecoin.io/>.

As always, thank you for your continued support. We look forward to building
with you!

### Related Articles

[View all articles](../../../blog)

[ ](../../../blog/posts/filecoin-implementations-progress-update/)

updates

##  [ Filecoin Implementations Progress Update ](../../../blog/posts/filecoin-
implementations-progress-update/)

One of Filecoin’s launch goals has always been to have multiple independent
protocol implementations to help secure the network at launch.

Oct 20, 2020

[ ](../../../blog/posts/announcing-lotus-our-first-alternate-filecoin-
implementation/)

updates

##  [ Announcing Lotus, our first alternate Filecoin implementation
](../../../blog/posts/announcing-lotus-our-first-alternate-filecoin-
implementation/)

One of our most important goals is to make the Filecoin mainnet as secure and
resilient as possible. One part of our network security strategy is launching
the Filecoin network with multiple implementations. Today, we are delighted to
announce lotus, our first alternate Filecoin implementation.

Oct 16, 2019

[ ](../../../blog/posts/a-guide-to-filecoin-storage-mining/)

updates

##  [ A Guide to Filecoin Storage Mining ](../../../blog/posts/a-guide-to-
filecoin-storage-mining/)

An updated guide to Filecoin storage mining, and discuss some of the recently
announced incentives and opportunities for members of the growing Filecoin
community.

Jul 7, 2020

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

