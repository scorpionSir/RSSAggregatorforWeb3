[ ![0xb10c logo](/0xb10c.png) ](/)

# 0xB10C

Bitcoin Developer

[Blog](/) [Mempool Observations](/mempool-observations) [Projects](/projects)
[Talks](/talks)

☀  requires JS

##  Frequently Asked Questions: Bitcoin Transaction Monitor

#####

Thursday, October 10, 2019

The [Bitcoin Transaction Monitor](https://mempool.observer/monitor) provides
deeper insights into the usage of the Bitcoin network by showing transactions
by time and feerate. This post answers frequently asked questions about the
Bitcoin Transaction Monitor itself.

![header image](/data/blog/005-bitcoin-transaction-monitor-faq/header.png)
Bitcoin Transaction Monitor: transactions plotted over time and feerate

##### Why did you build a Bitcoin Transaction Monitor?

With Bitcoin, a permissionless network has been created, where everybody can
join. Companies, services, and individual users broadcast transactions to the
network. Plotting these transactions by _arrival time_ and _feerate_ reveals
interesting activity patterns. The Bitcoin Transaction Monitor is built to
visualize, share and inform about these patterns. I hope it lets us gain
deeper insights into the usage of the Bitcoin network.

##### Where do you get the data about the transactions from?

I run a Bitcoin Core node connected to the Bitcoin network, which passes valid
transactions to `memod` (mempool observer daemon) over the ZMQ-interface. Each
passed transaction is processed by `memod` and written into a database.

##### Doesn't the Transaction Monitor reveal private information about
transactions ?

The Bitcoin Transaction Monitor shows activity and usage patterns of the
Bitcoin network. This information can be (and probably is already) used by bad
actors to weaken the privacy or even completely depseudonymize transactions.
Yet this information broadcasted on the Bitcoin network is entirely public.
Raising the awareness of what transactions can reveal is far more valuable
than hiding public information.

> If I can build a Transaction Monitor in my free time that visualizes this
> data and could run on your laptop, what can a motivated bad actor do with
> far more resources?

##### What are future ideas for the Bitcoin Transaction Monitor?

Provided I have the time and come up with an efficient architecture I'd like
to archive and display historical data. Additionally, providing a live
visualization of incoming transactions would be interesting. There is a
[GitHub issue](https://github.com/0xB10C/memo/issues/50) which has a few
feature suggestions.

[Project: Bitcoin Transaction Monitor](/projects/bitcoin-transaction-monitor/)
[GitHub issue with feature
suggestions](https://github.com/0xB10C/memo/issues/50)

Enable JavaScript to view comments. Comments are privacy friendly and self-
hosted with [isso](https://posativ.org/isso/).

All text and images in this work are licensed under a [Creative Commons
Attribution-ShareAlike 4.0 International
License](http://creativecommons.org/licenses/by-sa/4.0/) [![Creative Commons
License](https://i.creativecommons.org/l/by-
sa/4.0/80x15.png)](http://creativecommons.org/licenses/by-sa/4.0/)

#### Next

![Image for Evolution of the signature size in
Bitcoin](/data/blog/006-signatures/header.png) [](/blog/006-evolution-of-the-
bitcoin-signature-length/)

* * *

November 10, 2020

#### Evolution of the signature size in Bitcoin

Digital signatures are an essential building block of the Bitcoin protocol and
account for a large part of the data stored on the blockchain. We detail how
the size of the encoded ECDSA signatures reduced multiple times over the last
years and how the proposed Schnorr signature compares to the length of the
currently used ECDSA signatures.

[](/blog/006-evolution-of-the-bitcoin-signature-length/)

#### Previous

![Image for The Incomplete History of Bitcoin
Development](/data/blog/004-bitcoin-development-history/timeline-2007.png)
[](/blog/004-the-incomplete-history-of-bitcoin-development/)

* * *

August 4, 2019

#### The Incomplete History of Bitcoin Development

To fully understand the rationale behind the current state of Bitcoin
development, knowledge about historical events is essential. This blog post
highlights selected historical events, software releases and bug fixes before
and after Satoshi left the project. It additionally contains a section about
the current state of Bitcoin development. The linked
[timeline](/projects/bitcoin-dev-history/#timeline-bitcoin-history) provides
extra detail for each event.

[](/blog/004-the-incomplete-history-of-bitcoin-development/)

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

