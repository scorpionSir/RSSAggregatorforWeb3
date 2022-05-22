[ ![0xb10c logo](/0xb10c.png) ](/)

# 0xB10C

Bitcoin Developer

[Blog](/) [Mempool Observations](/mempool-observations) [Projects](/projects)
[Talks](/talks)

☀  requires JS

##  The 300 MB default maxmempool Problem

#####

Monday, December 18, 2017

Unconfirmed transactions are quite a hassle for bitcoin users. I recently came
across an interesting problem which is not the usual "my transaction is stuck"
problem.

In the last weeks of 2017, the number of unconfirmed transactions has again
reached all-time highs. Periods with over 100k transactions in my mempool were
not unusual. Bitcoin Core limits the system memory allocated for storing
unconfirmed transactions to 300 MB by default. This serves as an anti-DoS
feature. Fully used 300 MB of RAM equal about 110 MB of actual raw transaction
data. This default value [can be
changed](https://en.bitcoin.it/wiki/Running_Bitcoin) with the `-maxmempool
<n>` option where `n` is the number of megabytes allocated to store
unconfirmed transactions.

    
    
     $ bitcoin-cli getmempoolinfo
     {
       "size": 123803,               # amount of tx
       "bytes": 107840125,           # raw tx bytes
       "usage": 298526272,           # tx in ram bytes
       "maxmempool": 300000000,      # maxmempool in bytes
       "mempoolminfee": 0.00016486   # min tx-fee to get accepted
     }
    

Once 300 MB of system memory is filled, Bitcoin Core starts dropping low-
feerate transactions from the mempool for high-feerate transactions.
Additionally, a `mempoolminfee`-threshold is set to prevent new low fee
transactions from entering the mempool.

![transactions dropping from the mempool](/data/blog/001-300MB-default-
problem/transactions-dropping-from-mempool.png)

A node operator can increase or decrease the `maxmempool` option to better fit
their system. I assume that for example, some block-explorers have increased
their nodes `maxmempool`. I know that Jochen Hoenicke, for example, has a node
running with a [`maxmempool` of
2GB](https://www.reddit.com/r/Bitcoin/comments/7i6rnu/why_is_no_one_talking_about_the_178000/dqx5osf/).

#### The Problem

Small differences in the mempool are common. However, with an increased
`maxmempool` a nodes mempool can differ vastly from a majority of other nodes
on the network. These nodes, especially when they power a block-explorer,
still many keep unconfirmed transactions the majority of the network has
already dropped. This can be irritating for users.

I came across a particular form of this problem, when a friend asked me, why
he can see a certain low-fee transaction on [bitaps.com](https://bitaps.com),
but not on [blockchain.info](https://blockchain.info). My local node, with a
default 300 MB `maxmempool`, responded with an error on calling the
`getrawtransaction` RPC with the txid.

    
    
     $ bitcoin-cli getrawtransaction <txid>
     error code: -5
     error message:
     No such mempool transaction.
    

However, using the [bitaps.com](https://bitaps.com) API to query the raw
transaction worked fine. I tried rebroadcasting the raw transaction with
`sendrawtransaction`. This failed.

    
    
     $ bitcoin-cli sendrawtransaction <rawtx>
     error code: -25
     error message:
     Missing inputs
    

Looking at the missing input I noticed that it references an unconfirmed
change output from a transaction with equally low fees. However, I again
wasn't able to find the parent transaction for the input in my local mempool
or on [blockchain.info](https://blockchain.info). Only
[bitaps.com](https://bitaps.com) had it. And this transaction again referenced
an unconfirmed low-fee output as an input.

With the context of the `maxmempool`-limit this started to make sense.

#### My take on what happened

My take on what happened is, that [bitaps.com](https://bitaps.com) has a
higher `maxmempool`-limit than e.g. [blockchain.info](https://blockchain.info)
and therefore does not drop the transactions. A user checking
[bitaps.com](https://bitaps.com) sees the transaction, a user checking
[blockchain.info](https://blockchain.info) doesn't.

![chained mempool transactions](/data/blog/001-300MB-default-problem/chained-
mempool-tx.png)

The real issue appears when the original sender is not aware of this and has a
peer with a larger-than-default mempool. He unknowingly continues to chain
transactions to an unconfirmed parent transaction that the vast majority of
the network rejects. The broadcasted transaction spends an output that
references a dropped transaction and therefore is invalid.

* * *

David Harding [pointed
out](https://twitter.com/hrdng/status/955492510998069249) that the sender
could use [BIP-125 Replace-By-
Fee](https://github.com/bitcoin/bips/blob/master/bip-0125.mediawiki) to update
an unconfirmed transaction with new outputs:

Enable JavaScript to view comments. Comments are privacy friendly and self-
hosted with [isso](https://posativ.org/isso/).

All text and images in this work are licensed under a [Creative Commons
Attribution-ShareAlike 4.0 International
License](http://creativecommons.org/licenses/by-sa/4.0/) [![Creative Commons
License](https://i.creativecommons.org/l/by-
sa/4.0/80x15.png)](http://creativecommons.org/licenses/by-sa/4.0/)

#### Next

![Image for Plotting the Bitcoin Feerate
Distribution](/data/blog/002-plotting-feerate-distribution/twitter.png)
[](/blog/002-plotting-the-bitcoin-feerate-distribution/)

* * *

March 18, 2018

#### Plotting the Bitcoin Feerate Distribution

How did the median Bitcoin feerate evolve [from 2013 to
2015?](https://transactionfee.info/charts/feerate/median?avg=7&step=false&start=2013-01-01&end=2015-01-01)
When were the [feerate spikes in
2017?](https://transactionfee.info/charts/feerate/percentiles?avg=7&step=false&start=2017-01-01&end=2018-01-01)
Visualizing the Bitcoin feerate distribution per block was on my todo list
since I've started working on the first version of my [mempool.observer
project](/projects/mempool-observer-2017-version/) in mid-2017. But acquiring
the data …

[](/blog/002-plotting-the-bitcoin-feerate-distribution/)

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

