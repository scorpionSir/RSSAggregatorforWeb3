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

Oct 16, 2019  

## Announcing Lotus, our first alternate Filecoin implementation

One of our most important goals is to make the Filecoin mainnet as secure and
resilient as possible. One part of our network security strategy is launching
the Filecoin network with multiple implementations. Today, we are delighted to
announce [**lotus**](https://github.com/filecoin-project/lotus), our first
alternate Filecoin implementation.

For [several months](https://filecoin.io/blog/update-2019-q2-q3/#3-roadmap-
update), we have been working simultaneously toward building [**go-
filecoin**](https://github.com/filecoin-project/go-filecoin), our original
reference implementation, while also collaborating with other teams to build
multiple implementations of the [Filecoin protocol
spec](https://github.com/filecoin-project/specs/). This effort will not alter
our testnet and mainnet timelines, but it will make the Filecoin mainnet more
secure and resilient. **lotus** is the first of many multiple implementation
announcements that are coming very soon!

Specifically, today we’re announcing:

  1. The opening of the **lotus** codebase
  2. The launch of the **lotus** devnet

Let’s dive in!

### Why multiple implementations?

As we’ve mentioned
[elsewhere](https://filecoin.io/blog/update-2019-q2-q3/#3-roadmap-update),
building a blockchain is like building a software rocket. We are working to
ensure that our protocol and software implementations are secure – we have an
internal protocol security team and are performing internal implementation
security audits, external security audits, and more. But no matter how hard we
work to protect the system and individual nodes, there is always the chance
that an implementation bug might rear its head and result in adverse
consequences for the network.

Having multiple software implementations that interoperate on the same network
reduces this risk significantly. While each implementation might have its own
set of bugs, it is unlikely that all implementations will have the exact same
set of security issues – especially if these implementations do not share
security-critical software components. Thus, launching a cryptocurrency
network with multiple implementations decreases the likelihood of a
catastrophic bug that can adversely affect or even take down the entire
Filecoin network.

Multiple implementations offer other benefits, such as the ability to increase
engagement with different developer communities and the opportunity to explore
different implementation architectures (which may offer different performance
and other optimizations). Ever since Ethereum launched with Geth and Parity,
we have seen an increasing number of cryptonetworks launching with multiple
software implementations.

Because multiple implementations are so valuable for network security,
resilience, and community engagement, we have made it a goal to launch
Filecoin (in March 2020) with 2+ interoperable protocol implementations. As of
today, we have several Filecoin implementations in progress – **go-filecoin**
, **lotus** , and others that will be formally announced soon. We are looking
for even more talented teams to build Filecoin implementations. If interested,
please apply for our [grant](https://github.com/filecoin-
project/devgrants/issues/43) to build an additional implementation by
following the instructions [here](http://filecoin.io/grants)!

### Tell me more about **lotus**

[**lotus**](https://github.com/filecoin-project/lotus) is a minimal,
experimental implementation of the [Filecoin protocol
specification](https://github.com/filecoin-project/specs/), and is written in
Go. The codebase is not yet feature-complete, but several core Filecoin
protocol features have already been implemented, including:

  * **Mining.** Miners can now start mining on the lotus devnet and start earning storage power. **lotus** has also implemented multiple sector sizes, so miners with many different storage configurations can mine on the network. **lotus** integrates with [**rust-fil-proofs**](https://github.com/filecoin-project/rust-fil-proofs/), so miners can submit _Proofs-of-Spacetime_ on schedule in order to avoid being slashed. What’s more, the storage mining functionality is implemented as a separate module, so advanced miners can optimize mining processes as they wish for their particular hardware configurations.
  * **Storage.** Storage clients can create deals with miners, set up payment channels to miners, transfer data for storage, and pay miners for storing their data correctly.
  * **Retrieval.** Retrieval clients can pay to retrieve their data from storage miners (i.e. [retrieval v0](https://filecoin-project.github.io/specs/#retrieval-v0-libp2p-services)).
  * And much more! Check out the codebase on GitHub [here](https://github.com/filecoin-project/lotus)!

In addition to opening the **lotus** codebase, today we are also announcing
the launch of the first public **lotus** development network (devnet). After
setting up a **lotus** node, you can connect to the devnet and begin storing
data with other nodes or start mining. Read the [*Getting Started with *
_lotus___](https://filecoin.io/blog/announcing-lotus/#getting-started-with-
lotus) section below for more details.

A few very important notes:

  * The **lotus** codebase is still a minimal, experimental implementation of the Filecoin protocol, and will evolve quickly between now and our testnet launch, scheduled for December 11, 2019.
  * The lotus devnet will be reset many times between now and testnet launch. Do not expect network stability before testnet launch on December 11, 2019.
  * We plan to launch the Filecoin main network with **go-filecoin** , **lotus** , and 1+ additional implementation in March 2020.
  * The **lotus** devnet and the **go-filecoin** alphanet are not _currently_ the same network. They will continue to be different networks until **go-filecoin** and **lotus** nodes can interoperate. This interop will happen before we launch in March 2020, but exact date is still TBD.

### Getting started with **lotus**

We encourage miners, clients, and developers to start experimenting with
**lotus** today! We hope that your engagement and participation will help
strengthen the security of the **lotus** codebase and network in advance of
our December 11, 2019 testnet launch.

For miners and users, there are 4 main ways to get involved with **lotus**
today:

  1. Download, install, and run **lotus** locally (instructions [here](https://github.com/filecoin-project/lotus#building))
  2. Connect to the **lotus** devnet (instructions [here](https://github.com/filecoin-project/lotus#devnet))
  3. Contribute to the **lotus** codebase (open issues [here](https://github.com/filecoin-project/lotus/issues))
  4. Explore network activity via the [lotus devnet dashboard](https://lotus-metrics.kittyhawk.wtf/)

Adventurous developers can begin exploring the [**lotus** RPC
API](https://github.com/filecoin-project/lotus/blob/master/api/api.go) to
start building applications on the **lotus** devnet (and eventually testnet).
Note that **lotus** will continue to evolve significantly until testnet, so be
prepared for breaking changes.

Through any and all of these steps, we hope you will help us out by reporting
any and all issues you encounter. Identifying issues helps us reach our
security goals more quickly, so we really like bug reports. 🙏 You can post
issues or explore what others have posted on:

  * [Lotus Help discussion forum](https://discuss.filecoin.io/c/lotus-help)
  * #fil-lotus channel on [community chat](https://github.com/filecoin-project/community#chat)
  * #fil-help channel on [community chat](https://github.com/filecoin-project/community#chat) (make sure to mention that you need help with **lotus** specifically)
  * [GitHub issues on the **lotus** repo](https://github.com/filecoin-project/lotus/issues)

### Many Thanks

As always, many thanks for your continued support of the Filecoin project. We
are excited to continue working with you to build a robust, decentralized, and
efficient foundation for humanity’s information.

Onward!

### Related Articles

[View all articles](../../../blog)

[ ](../../../blog/posts/the-evolution-of-a-lotus-node/)

events

##  [ The Evolution of a Lotus Node ](../../../blog/posts/the-evolution-of-a-
lotus-node/)

A look into the past, present, and future of a Lotus node from the Retrieval
Market Builders Mini-Summit.

Jun 22, 2021

[ ](../../../blog/posts/announcing-filecoin-implementations-in-rust-and-c/)

updates

##  [ Announcing Filecoin implementations in Rust and C++
](../../../blog/posts/announcing-filecoin-implementations-in-rust-and-c/)

Today, we are excited to announce two additional implementations of the
Filecoin protocol: forest – being implemented in Rust by ChainSafe, and fuhon
– being implemented in C++ by Soramitsu. These implementations are in active
development, and are now fully open for anyone to use or contribute to. Check
them out on GitHub!

Jan 31, 2020

[ ](../../../blog/posts/filecoin-implementations-progress-update/)

updates

##  [ Filecoin Implementations Progress Update ](../../../blog/posts/filecoin-
implementations-progress-update/)

One of Filecoin’s launch goals has always been to have multiple independent
protocol implementations to help secure the network at launch.

Oct 20, 2020

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

