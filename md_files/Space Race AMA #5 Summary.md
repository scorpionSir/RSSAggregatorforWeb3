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

  * [events](../../../blog/events)

  *   *   * 

![](../../../images/icons/social/share.svg)

Oct 2, 2020  

## Space Race AMA #5 Summary

As a part of the Space Race events program, the Filecoin team are hosting
weekly live AMA’s with the Filecoin community. On September 30th our team
hosted our fifth AMA answering 20+ questions on Space Race 2, Filecoin mining
and Mainnet Liftoff.

A summary of the most popular questions and answers is below. We look forward
to hosting more sessions like this as mainnet launch approaches! In the
meantime, stay tuned for updates on the [Filecoin Community
Slack](https://filecoin.io/slack). You can also find us on [Wechat (Filecoin-
Official)](https://weixin.qq.com/r/1xz54Y-EctINrcuC90nF), and
[Twitter](https://twitter.com/Filecoin).

### Summarized Questions and Answers

Most questions and answers are quoted directly, some are edited for
readability.

**When will Filecoin go live?**

The Filecoin Mainnet will go live on epoch 148,888.

**When will I be able to mine Filecoin?**

The Filecoin network is currently in its “Mainnet Ignition” phase, where
miners, clients, and other network participants are onboarding ahead of
Mainnet Liftoff. If you’d like to get started mining Filecoin - now is a great
time to get set up on the network.

**Will all storage power in Space Race be transferred to the Mainnet? Will
testnet FIL be transferred to the Mainnet too?**

We plan to transfer **all** sectors from Space Race 1 and 2 to mainnet. 🎉 The
pledge collateral for these sectors and earned block rewards will also be
transferred to reward dedicated miners who helped stress-test and improve the
protocol throughout the Space Race competition, and set them up for a strong
Mainnet Liftoff. We plan to do other state upgrades that may adjust or
redistribute balances between now and mainnet launch.

**Is there more information on deal types, verified deals? When they will
start and how will they affect a miner’s block production?**

More details around Verified Client and its principles and processes will be
announced soon. The specific mechanics of how they will impact block
production is already in the code. The mechanism will only go live after those
details are announced and multiple verified clients exist on the network.

**Will Protocol Labs visit China during the Wanxiang Blockchain Summit this
October?**

We would love to attend the Wanxiang Blockchain Summit in person, however with
the global pandemic that isn’t possible right now. We plan to participate
virtually in a number of talks and panels, and we are looking forward to
visiting China sometime next year once the situation improves.

**Will there be major updates or lotus upgrades during this golden week in
China?**

No! We’re being careful to avoid having any mandatory upgrades during Golden
Week. We are planning a new consensus-breaking release of Lotus towards the
end of Golden Week, with an upgrade epoch late on Friday, October 9th.

Happy Mid-Autumn Festival! 中秋节和国庆节快乐！

**How will miners make the Discover HDD data available on the Mainnet? Will we
need to seal the 5 to 8 TB of data or can we use sectors we have already
sealed?**

Filecoin Discover will be one of many verified clients when the mechanism is
deployed. Discover disks are just means for data transport and it’s the
verified client deals that will give miners higher quality-adjusted power.

**Who is now stewarding the go-filecoin implementation?**

There was an RFP proposal here for a community maintainer:
<https://github.com/filecoin-project/devgrants/issues/140> \- IPFSForce
applied for this RFP and was accepted through the Filecoin DevGrant
application process. IPFSForce has been an engaged and reputable member of the
community and we are very happy to have this team improving and stewarding the
go-filecoin implementation. Don’t miss out on the next RFP!

**Can miners use apps other then lotus to mine during SR2?**

Not yet, unfortunately, though we certainly encourage folks to write their own
node and miner implementations.

Our external implementations are close to being able to mine and validate the
ignition network, but they’re not there quite yet. Stay tuned for updates!

**How can I show up on one of the various miner lists so Slingshot clients can
make storage deals with me?**

This list is generated by a community member who sends query-ask messages to
active miners and attempts to make storage deals with each of them. If a miner
accepts a deal and begins sealing it, the status will be marked ‘active-
sealing’. In order for your miner to show up on this list, please make sure
you are configuring your mining node in a way that allows you to be dialable
and to accept storage deals from clients. We have put together a small script
that you can use to make some deal-acceptance changes on the fly without
having to restart your node. This replaces the previous jq-based deal
acceptance logic. For example, you can download the script
(<https://gist.github.com/ribasushi/53b7383aeb6e6f9b030210f4d64351d5#file-
dealfilter-pl>), make it executable (chmod 755 dealfilter.pl), and point your
miner at it so you don’t have to restart your node for future deal acceptance
changes!

Additional instructions can be found in this Filecoin Slack message:
<https://filecoinproject.slack.com/archives/C019UFEACBT/p1601061393028300>

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

