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

Sep 25, 2019  

## Announcing the go-filecoin alphanet

Yesterday, we launched the **go-filecoin** alphanet, [**go-filecoin** release
0.5.6](https://github.com/filecoin-project/go-filecoin/releases/tag/0.5.6)
([right on schedule](https://filecoin.io/blog/update-2019-q2-q3/#1-launches-
testnet-on-dec-11-mainnet-in-2020-q1) – well actually, a day early!). As we
announced in our [2019 Q2 & Q3
Update](https://filecoin.io/blog/update-2019-q2-q3/), this was our last major
interim milestone before our upcoming testnet launch in December 2019.

The **go-filecoin** alphanet integrates a number of significant protocol
features, but perhaps one of the most important is that it is a _long-running
network_. We [launched our first development networks
(devnets)](https://filecoin.io/blog/opening-filecoin-project-repos/) earlier
this year, but our devnets have not historically included the full machinery
for seamless network upgrades. Therefore, whenever we wanted to release new
go-filecoin functionality to one of our devnets, we had to trigger a hard
network reset. Nodes that were using older go-filecoin versions could no
longer connect to the devnets unless they downloaded the latest release and
setup their nodes from scratch. Now, with the alphanet launch, we have
implemented much of the functionality for seamless network upgrades. While we
may still perform hard network resets when necessary, we won’t be required to
in order to expose new features to network nodes. This is a major improvement
in the realism of our early networks and in the user experience for those who
are willing to test them out.

The alphanet release also includes the implementation of several important
protocol features, such as:

  * Our updated _Proof-of-Spacetime_ (PoSt) construction – Rational PoSt
  * Improvements to our Expected Consensus (EC) algorithm implementation
  * Drastically faster chainsync, using [Graphsync](https://github.com/ipfs/go-graphsync)’s IPLD DAG-traversal protocol
  * New [HTTP API design](https://github.com/filecoin-project/filecoin-http-api) (still WIP)
  * And more!

A more detailed description of the major changes in this release can be found
in our [go-filecoin CHANGELOG](https://github.com/filecoin-project/go-
filecoin/blob/master/CHANGELOG.md). (Note: At the time of this writing, the
update for release 0.5.6, i.e. the initial alphanet release, is still an [open
PR in the go-filecoin repo](https://github.com/filecoin-project/go-
filecoin/pull/3490/files). It should merge shortly.)

Now is as good a time as any to begin testing out the Filecoin protocol
implementation and networks. Here are a few pointers for how to get started:

  * Follow our [getting started instructions](https://docs.filecoin.io/go-filecoin-tutorial/Home.html) on our new documentation site to download the latest release and connect to the alphanet.
  * Check out the activity on our [network statistics dashboard](https://stats.kittyhawk.wtf/).
  * Join our [community chat](https://github.com/filecoin-project/community#chat) to ask questions, chat with others in the community, and collaborate on projects
  * If you are a developer who would like to build projects for the Filecoin ecosystem, please reach out on our [discussion forum](https://discuss.filecoin.io/t/highlighting-community-projects) to add a project to the Filecoin Shipyard and/or apply for a [Filecoin dev grant](https://filecoin.io/grants/). The deadline for this wave of grant applications is on September 30, 11:59PM PDT.

We’re excited for you to connect to the Filecoin alphanet. Onward!

### Related Articles

[View all articles](../../../blog)

[ ](../../../blog/posts/filecoin-2019-q2-q3-update/)

updates

##  [ Filecoin 2019 Q2 & Q3 Update: Testnet & Mainnet Launches, Highlights
from 2019, Roadmap Update, and More
](../../../blog/posts/filecoin-2019-q2-q3-update/)

The most important news in this update is that we’re getting very close to
launching the network. We are delayed from our prior estimates, but – as you
will read below – we have made tremendous progress on all fronts!

Sep 24, 2019

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

[ ](../../../blog/posts/filecoin-testnet-is-live/)

updates

##  [ Filecoin Testnet is live ](../../../blog/posts/filecoin-testnet-is-
live/)

Today marks an important milestone for the Filecoin project: the launch of the
Filecoin testnet (on schedule)! After significant research, design, and
development, the Filecoin protocol is ready for live network testing. We’re
thrilled to share it with you.

Dec 11, 2019

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

