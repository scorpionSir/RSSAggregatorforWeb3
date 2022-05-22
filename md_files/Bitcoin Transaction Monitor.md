[ ![0xb10c logo](/0xb10c.png) ](/)

# 0xB10C

Bitcoin Developer

[Blog](/) [Mempool Observations](/mempool-observations) [Projects](/projects)
[Talks](/talks)

☀  requires JS

##  Bitcoin Transaction Monitor

#####

Thursday, October 10, 2019

Whenever you, an exchange or somebody else sends a Bitcoin transaction, it
gets broadcast to all nodes in the Bitcoin network. Each broadcast transaction
is represented by a dot on the [Bitcoin Transaction
Monitor](https://mempool.observer/monitor) scatterplot. The transactions are
arranged by the time of arrival at my Bitcoin node and its feerate (fee per
size). The plot reveals activity patterns of wallets, exchanges, and users
transacting on the Bitcoin network.

##### Building the Transaction Monitor

I first got the idea of plotting Bitcoin transactions by their arrival time
and feerate as I was working on my [mempool.observer](/projects/mempool-
observer-2019-version/) project. Plotting the output of Bitcoin Core's
`getrawmempool` RPC generated chart below. While there are big white areas of
confirmed transactions, there are definitely activity patterns visible. This
sparked my interest and I started to dive deeper.

![plotting the output of the getrawmempool RPC of Bitcoin
Core](/data/projects/bitcoin-transaction-monitor/early-idea.png) plotting the
output of the getrawmempool RPC of Bitcoin Core

My first goal was to find a way to efficiently extract the incoming
transactions. Polling the mempool via the `getrawmempool` RPC was not an
option. The RPC can run for multiple seconds if the mempool holds a few
thousand transactions which is not too uncommon. I started profiling the RPC
but found no obvious way to speed it up. Additionally, by polling, I would
miss the confirmed transactions that entered the mempool between my last poll
and a new block.

Bitcoin Core can be configured to publish transactions that enter the mempool
via a ZMQ interface. These ZMQ messages contain the raw binary Bitcoin
transaction. However, as I previously noted in my blog post [Plotting the
Bitcoin Feerate Distribution](/blog/002-plotting-the-bitcoin-feerate-
distribution/), Bitcoin transactions don't contain the fee they pay as an
explicit value. The fee is implicitly set by leaving a bit of the previous
output amount to the miner when creating the new outputs. This means that I
would have had to query the transaction fee for every transaction that
arrived. As this would have made the project quite resource hungry I started
thinking about my alternatives.

The best performing alternative I found was to
[patch](https://github.com/0xB10C/bitcoin/commit/f03785b4e0c0aa4d74a2934e20ed607d6b8758e2)
my Bitcoin Core instance and to create a custom ZMQ publisher that sends the
transaction and the fee. This approach allowed me to just subscribe to my
newly added ZMQ publisher and be able to extract this data. The biggest
downside here is probably that it meant that this creates a big hurdle for
somebody wanting to self-host the Transaction Monitor.

The next step was to build a backend that keeps the last few thousand
transactions and attach an API to it for retrieval in a frontend. I choose a
Redis [sorted-set](https://redislabs.com/ebook/part-2-core-
concepts/chapter-3-commands-in-redis/3-5-sorted-sets/) and used the
transaction arrival timestamp as score. This allowed me to quickly retrieve
the most recent entries while being able to drop older transactions. I ended
up implementing a 30-second cache and gzipped the JSON responses to speed up
API calls even more. All in all, this allowed me to reduce the average
response time to around 700ms (from more than 12s when starting off) and to
respond to concurrent requests with nearly no increase in the response time.

For maximal flexibility, I choose [D3.js](https://d3js.org/) to visualize the
data in the frontend. D3.js comes with a steep learning curve but was the only
library that allowed for the interactivity and performance I aimed for. At
first, I tried to draw the dots for the transactions as objects in an SVG.
However, this is slow with multiple thousand transactions drawn. The
alternative was to use an HTML canvas that basically acts as a bitmap image.
By using a Canvas the interactivity and the data-bindings that D3.js offers
are lost. I ended up using a
[Quadtree](https://en.wikipedia.org/wiki/Quadtree) (a tree data structure
where each internal node has four children) to find transactions close to the
user's mouse pointer which enabled me to restore the interactivity while
keeping the performance high.

I wanted to be able to filter transactions by their properties and thus I
wrote a Golang library that allows me to answer questions about raw Bitcoin
transactions. This library is called [rawtx](https://github.com/0xB10C/rawtx)
([project page](/projects/library-rawtx/)).

> The Bitcoin Transaction Monitor lets you now highlight transactions based on
> the block they are included in.<https://t.co/q1sbHn4Tqy>
> [pic.twitter.com/hQcKvocg6O](https://t.co/hQcKvocg6O)
>
> -- b10c (@0xB10C) [January 15,
> 2020](https://twitter.com/0xB10C/status/1217471074671243266?ref_src=twsrc%5Etfw)

#### Privacy Implications

I reflected a bit about the privacy implications before publishing the
Transaction Monitor. For somebody familiar with the Bitcoin ecosystem, it's
companies, wallets, and users, it's fairly trivial to attribute some
transactions to entities using the Transaction Monitor. This was a point for
not publishing it. However, I think there is a bigger total gain for the
community in raising the awareness that the pseudonymity sets are small. Users
and companies often leave distinct _mempool-fingerprints_. I've asked the
following question in my [Frequently Asked Questions: Bitcoin Transaction
Monitor](/blog/005-bitcoin-transaction-monitor-faq/) post as well:

Everything I display is public information. If I can build a Transaction
Monitor in my free time that visualizes this data and could run on your
laptop, what can a motivated bad actor do with far more resources?

#### Prior Art

  * basil00's [TxMon](https://reqrypt.org/txmon.html), [archived](http://archive.ph/gr11T)
  * Conor Scott's [draw_mempool (master)](https://github.com/conscott/draw_mempool), [screenshots](https://github.com/conscott/draw_mempool/tree/9feb575f1597ed9e42140af9fbec924702578fb3)
  * Jan Vornberger's [bitcoinmonitor.com](http://www.bitcoinmonitor.com/)

> How is the Bitcoin network being used?  
>  
> I've build a Bitcoin Transaction Monitor to gain deeper insights on the
> Bitcoin network usage. Transactions are plotted by time and feerate, which
> reveals interesting activity patterns. <https://t.co/CWgyPpdjJo>
>
> -- b10c (@0xB10C) [October 10,
> 2019](https://twitter.com/0xB10C/status/1182295216709148672?ref_src=twsrc%5Etfw)

> This is a neat new visualization of recent bitcoin transactions that makes
> it abundantly clear that some services are still hard coding their fee rates
> - there are no known fee estimators that recommended over 60 satoshis /
> vbyte during this period. <https://t.co/VKJ2ivg6xE>
> [pic.twitter.com/0MoYtWkvco](https://t.co/0MoYtWkvco)
>
> -- Jameson Lopp (@lopp) [October 10,
> 2019](https://twitter.com/lopp/status/1182302770285748226?ref_src=twsrc%5Etfw)

Enable JavaScript to view comments. Comments are privacy friendly and self-
hosted with [isso](https://posativ.org/isso/).

All text and images in this work are licensed under a [Creative Commons
Attribution-ShareAlike 4.0 International
License](http://creativecommons.org/licenses/by-sa/4.0/) [![Creative Commons
License](https://i.creativecommons.org/l/by-
sa/4.0/80x15.png)](http://creativecommons.org/licenses/by-sa/4.0/)

#### Next

![Image for Contribution: Colab version of the Optech Schnorr / Taproot
Workshop](/data/projects/colab-taproot-workshop/header.png)
[](/projects/contribution-optech-taproot-workshop-colab/)

* * *

November 27, 2019

#### Contribution: Colab version of the Optech Schnorr / Taproot Workshop

[Bitcoin Optech](https://bitcoinops.org/) created a
[workshop](https://bitcoinops.org/en/schorr-taproot-workshop/) explaining the
Schnorr and Taproot upgrade to engineers. However, users needed to compile a
patched version of Bitcoin Core with Taproot support and download and set up
the Jupyter notebooks.

[](/projects/contribution-optech-taproot-workshop-colab/)

#### Previous

![Image for rawtx library](/data/projects/rawtx/header.png)
[](/projects/library-rawtx/)

* * *

September 28, 2019

#### rawtx library

The rawtx Golang module helps you (and me) to answer questions about raw
Bitcoin transactions, their inputs, outputs, and scripts. I use the rawtx
package for example in my [Bitcoin Transaction Monitor](/projects/bitcoin-
transaction-monitor/) and [transactionfee.info](/projects/transactionfee-
info-2020-version/) projects.

[](/projects/library-rawtx/)

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

