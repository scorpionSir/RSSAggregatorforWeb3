[ ![0xb10c logo](/0xb10c.png) ](/)

# 0xB10C

Bitcoin Developer

[Blog](/) [Mempool Observations](/mempool-observations) [Projects](/projects)
[Talks](/talks)

☀  requires JS

##  The Incomplete History of Bitcoin Development

#####

Sunday, August 4, 2019

To fully understand the rationale behind the current state of Bitcoin
development, knowledge about historical events is essential. This blog post
highlights selected historical events, software releases and bug fixes before
and after Satoshi left the project. It additionally contains a section about
the current state of Bitcoin development. The linked
[timeline](/projects/bitcoin-dev-history/#timeline-bitcoin-history) provides
extra detail for each event.

I wasn't following the Bitcoin space when a majority of these events happened.
A big part of the timeline is adapted from a talk [John
Newbery](https://twitter.com/jfnewbery) gave on the [History and Philosophy of
Bitcoin Development](https://www.meetup.com/BitDevsNYC/events/262321510/). The
title of this blog post is supposed to remind you that it can't and doesn't
include every event. History is in the beholder's eye. History evolves. If you
have a suggestion about something missing or want to propose a change, please
create an issue in the open-source project [bitcoin-development-
history](https://github.com/0xB10C/bitcoin-development-history), which is used
to generate the attached timeline.

![picture of the timeline starting in in 2007](/data/blog/004-bitcoin-
development-history/timeline-2007.png)

#### With Satoshi

The timeline tells a story beginning in early 2007. Satoshi Nakamoto starts
working on Bitcoin. The peer-to-peer electronic cash system with no trusted
third party. A system only controlled by the software which its users run.

Early on contributors join Satoshi working on Bitcoin. These new contributors
add, next to many other things, support for [Linux](/projects/bitcoin-dev-
history/#2009-release-0-2-0) and [macOS](/projects/bitcoin-dev-
history/#2010-release-0-3-0) to the project. Over the summer of 2010 Satoshi
authors a few critical software changes. For example,
[checkpoints](/projects/bitcoin-dev-history/#2010-release-0-3-2) are
introduced as a safeguard against malicious peers broadcasting low difficulty
chains. A node enforcing these checkpoints rejects chains that don’t include
specific block hashes at specific heights. Checkpoints are hard-coded by
Satoshi alone which in theory allows Satoshi to control which chain the
network follows.

A few days after adding checkpoints Satoshi releases the first consensus
change in [version v0.3.3](/projects/bitcoin-dev-history/#2010-release-0-3-3).
Satoshi urges users to upgrade. Over the next month, multiple [minor
versions](/projects/bitcoin-dev-history/#2010-release-multiple-0-3-xx) are
released. One of them fixes a [critical overflow bug](/projects/bitcoin-dev-
history/#2010-bug-overflow-bug). This bug was exploited to create two high-
value UTXOs. Satoshi advises miners to reorg the chain containing the blocks
with the malicious transactions.

A week later Satoshi introduces an [alert system](/projects/bitcoin-dev-
history/#2010-post-alert-system) to inform node operators about similar bugs
and problems in the network. The alert system includes a safe mode. The safe
mode, once triggered, disables all money handling RPC methods in the entire
network. Only Satoshi can create valid network alerts by signing them with a
private key. Some users raise the question of what could happen when a second
party, for example, a government, gets access to this key.

Satoshi has a lot of power over the Bitcoin network at this point. The main
concern here isn't that Satoshi would turn evil and try to destroy the
network, but rather that there shouldn't be such a single point of failure in
a decentralized system.

In December 2010 Satoshi opens his [last thread](/projects/bitcoin-dev-
history/#2010-post-final) on bitcointalk announcing the removal of the safe
mode. Satoshi writes in one of his [last emails](/projects/bitcoin-dev-
history/#2011-other-last-contact-satoshi): _»I 've moved on to other things.
It's in good hands with Gavin and everyone.«_ Some might argue Satoshi
stepping away from Bitcoin is one of his greatest contributions.

#### Without Satoshi

Around the same time, the [development process](/projects/bitcoin-dev-
history/#2010-other-moved-to-github) moves from SVN to GitHub, which leads to
longtime [contributors](/projects/bitcoin-dev-history/#2011-other-new-
contributors) like TheBlueMatt, sipa, laanwj and gmaxwell joining the project.
In mid-2011 the [BIP process](/projects/bitcoin-dev-history/#2011-other-first-
bip) for Bitcoin Improvement Proposals is introduced. In the last quarter of
2011 and the first months of 2012, the community discusses [various
proposals](/projects/bitcoin-dev-history/#2011-other-p2sh), which would allow
the receiver of a transaction to specify the script needed to spend it. Out of
them, P2SH is merged.

In fall 2012 the [Bitcoin Foundation](/projects/bitcoin-dev-
history/#2012-other-bitcoin-foundation) is announced. The Bitcoin Foundation
hopes to achieve for Bitcoin what the Linux Foundation does for Linux. Some
people raise the fear of development centralization in the announcement
thread.

Bitcoin version [v0.8.0 is released](/projects/bitcoin-dev-
history/#2013-release-0-8-0) in spring 2013. Two weeks after the release an
[unexpected hardfork](/projects/bitcoin-dev-history/#2013-bug-hardfork) splits
the network in nodes that have and haven't yet upgraded. The hardfork is
resolved fairly quickly. Different miners react by shifting their hashpower to
the chain valid for both upgraded and not upgraded nodes.

In late 2013 the Bitcoin software is [rebranded to Bitcoin
Core](/projects/bitcoin-dev-history/#2013-other-rebranding-to-core). In the
following year companies such as [Chaincode](/projects/bitcoin-dev-
history/#2014-company-chaincode) and [Blockstream](/projects/bitcoin-dev-
history/#2014-company-blockstream) are founded. Later the [MIT Digital
Currency Initiative](/projects/bitcoin-dev-history/#2015-other-mit-dci) joins
Chaincode and Blockstream by paying developers and researchers to work on
Bitcoin. In February 2015 Joseph Poon and Tadge Dryja release the first draft
of the [Lightning Whitepaper](/projects/bitcoin-dev-history/#2015-other-
lightning-whitepaper). The next year Luke Dashjr revises the BIP process with
[BIP 2](/projects/bitcoin-dev-history/#2016-other-bip-2) and the Bitcoin Core
release v0.13.0 includes [SegWit](/projects/bitcoin-dev-
history/#2016-release-0-13-1) as a softfork. In November 2016 the [alert
system](/projects/bitcoin-dev-history/#2016-other-alert-system-retired) is
retired and in August 2017 [SegWit](/projects/bitcoin-dev-history/#2017-other-
segwit-activated) gets activated. The year 2019 brings a new company, [Square
Crypto](/projects/bitcoin-dev-history/#2019-company-squarecrypto), sponsoring
Bitcoin development. In May Pieter Wuille proposes [BIP
taproot](/projects/bitcoin-dev-history/#2019-post-taproot).

#### The current state of Bitcoin development

Over the years the Bitcoin development culture became more decentralized,
well-defined and rigorous. There are currently [six Bitcoin Core
maintainers](https://bitcointalk.org/index.php?topic=1774750.0), distributed
over three continents. Only they can merge commits by contributors. Before
commits get merged, however, they have to go through a [review
process](https://github.com/bitcoin/bitcoin/blob/master/CONTRIBUTING.md#peer-
review), which has gotten a lot stricter.

For example, a competing proposal, to the earlier mentioned P2SH, was
[`OP_EVAL`](/projects/bitcoin-dev-history/#2011-other-p2sh). The [pull
request](https://github.com/bitcoin/bitcoin/pull/669) implementing `OP_EVAL`
was merged at the end of 2011. It had only one reviewer, though it changes
consensus-critical code. Russell O’Connor opened an
[issue](https://github.com/bitcoin/bitcoin/issues/729) criticizing parts of
the implementation and that such a big and consensus-critical change should
have had a lot more review and testing.

This fueled an ongoing discussion on how to ensure higher code quality through
more testing and review. Today each pull request should at least be reviewed
by multiple developers. If a change touches security-critical or even
consensus-critical code, the review process needs many reviewers, a lot of
testing and usually spans over multiple months. John Newbery, an active
Bitcoin Core contributor, told me that there is _" no chance a consensus
change would be merged with a single reviewer today"_.

A lot of work went into automated testing. There are [unit-
tests](https://github.com/bitcoin/bitcoin/blob/master/src/test/README.md)
written in C++ and [functional-
test](https://github.com/bitcoin/bitcoin/blob/master/test/functional/README.md)
written in Python. Every non-trivial change should update existing tests or
add new ones to the frameworks. Next to unit- and functional-tests, there is
an initiative to do [fuzz-
testing](https://github.com/bitcoin/bitcoin/blob/master/doc/fuzzing.md) on
Bitcoin Core and a [benchmarking
framework](https://github.com/bitcoin/bitcoin/blob/master/doc/benchmarking.md)
to monitor code performance. The website
[bitcoinperf.com](https://bitcoinperf.com), for example, offers both a
[Grafana](https://bitcoinperf.com/d/YiV16Vsik/overview) and a
[codespeed](https://codespeed.bitcoinperf.com/) interface visualizing periodic
benchmarking results.

A well-defined [release
process](https://github.com/bitcoin/bitcoin/blob/master/doc/release-
process.md) has been put together over the years. Major releases of Bitcoin
Core are scheduled every six months. The
[schedule](https://github.com/bitcoin/bitcoin/issues/15940) includes a
[translation
process](https://github.com/bitcoin/bitcoin/blob/master/doc/translation_process.md),
a feature freeze and usually multiple release candidates. Recent efforts by
[Cory Fields](https://github.com/theuni) and [Carl
Dong](https://twitter.com/carl_dong) aim to increase the [Bitcoin Core build
system security](https://www.youtube.com/watch?v=I2iShmUTEl8) with
[deterministic and
bootstrappable](https://github.com/bitcoin/bitcoin/blob/master/contrib/guix/README.md)
builds. The new build system might not be fully ready for the v0.19.0 release
of Bitcoin Core this fall but could provide greater build security in the
future.

#### Conclusion

Over the past ten years, the Bitcoin development culture has changed a lot.
Moving from being very centralized around Satoshi to being more decentralized
with more than a [thousand GitHub contributors in
2018](https://twitter.com/_jonasschnelli_/status/1080713877355081729). It has
become clear that high standards for code review, code quality, and security
are needed. These standards are followed and constantly improved.

I think to fully understand the rationale behind the current state of Bitcoin
development, knowledge about historical events is essential. There is a
timeline with more events attached below. Some suggested further reading could
be [The Tao Of Bitcoin Development](https://medium.com/@bergealex4/the-tao-of-
bitcoin-development-ff093c6155cd) written by [Alex
B.](https://twitter.com/bergealex4), [The Bitcoin Core Merge
Process](https://medium.com/@elombrozo/the-bitcoin-core-merge-
process-74687a09d81d) written by [Eric
Lombrozo](https://twitter.com/eric_lombrozo) and the blog post by [Jameson
Lopp](https://twitter.com/lopp): [Who Controls Bitcoin
Core?](https://blog.lopp.net/who-controls-bitcoin-core-/)

#### Acknowledgments

I'm thankful for John Newbery helping me to shape and review this blog post.
He did a lot of the historical digging for his [History and Philosophy of
Bitcoin Development](https://www.meetup.com/BitDevsNYC/events/262321510/)
talk, which this blog post is based upon. I'm also very grateful for
[Chaincode Labs](https://chaincode.com) inviting me to their 2019 Summer
Residency where I met a lot of awesome people, learned a ton and started
working on this blog post and the timeline.

[Timeline](/projects/bitcoin-dev-history/)

Enable JavaScript to view comments. Comments are privacy friendly and self-
hosted with [isso](https://posativ.org/isso/).

All text and images in this work are licensed under a [Creative Commons
Attribution-ShareAlike 4.0 International
License](http://creativecommons.org/licenses/by-sa/4.0/) [![Creative Commons
License](https://i.creativecommons.org/l/by-
sa/4.0/80x15.png)](http://creativecommons.org/licenses/by-sa/4.0/)

#### Next

![Image for Frequently Asked Questions: Bitcoin Transaction
Monitor](/data/blog/005-bitcoin-transaction-monitor-faq/twitter-card.png)
[](/blog/005-bitcoin-transaction-monitor-faq/)

* * *

October 10, 2019

#### Frequently Asked Questions: Bitcoin Transaction Monitor

The [Bitcoin Transaction Monitor](https://mempool.observer/monitor) provides
deeper insights into the usage of the Bitcoin network by showing transactions
by time and feerate. This post answers frequently asked questions about the
Bitcoin Transaction Monitor itself.

[](/blog/005-bitcoin-transaction-monitor-faq/)

#### Previous

![Image for A List of Public Bitcoin Feerate Estimation
APIs](/data/blog/003-feerate-api-list/feerate-api.png) [](/blog/003-a-list-of-
public-bitcoin-feerate-estimation-apis/)

* * *

June 29, 2019

#### A List of Public Bitcoin Feerate Estimation APIs

My search for a list of public Bitcoin feerate estimation APIs ended without
any real results. [Jameson Lopp](https://twitter.com/lopp) has a section on
feerate estimators on his [bitcoin.page](https://www.lopp.net/bitcoin-
information/fee-estimates.html) and [Antoine Le
Calvez's](https://twitter.com/khannib) dashboard
[txstats.com](https://txstats.com/dashboard/db/fee-estimation) provides a
visualization of different estimation APIs. But that is not what I was looking
for. That's why I compiled this list.

[](/blog/003-a-list-of-public-bitcoin-feerate-estimation-apis/)

[ ![logo stackexchange](/img/footer/stackexchange.svg)
](https://bitcoin.stackexchange.com/users/63817/0xb10c) [ ![logo
linkedin](/img/footer/linkedin.svg) ](https://linkedin.com/in/0xb10c) [ ![logo
mastodon](/img/footer/mastodon.svg) ](https://x0f.org/@0xb10c) [ ![logo
twitter](/img/footer/twitter.svg) ](https://twitter.com/0xb10c) [ ![logo
keybase](/img/footer/keybase.svg) ](https://keybase.io/b10c) [ ![logo
github](/img/footer/github.svg) ](https://github.com/0xb10c) [ ![logo
rss](/img/footer/rss.svg) ](https://b10c.me/feed.xml) [ ![logo
reddit](/img/footer/reddit.svg) ](https://reddit.com/u/0xb10c) [ ![logo
mail](/img/footer/gmail.svg) ](mailto:0xb10c+b10c-me@gmail.com)

