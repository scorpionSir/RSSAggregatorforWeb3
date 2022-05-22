[ ![0xb10c logo](/0xb10c.png) ](/)

# 0xB10C

Bitcoin Developer

[Blog](/) [Mempool Observations](/mempool-observations) [Projects](/projects)
[Talks](/talks)

☀  requires JS

##  The stair-pattern in time-locked Bitcoin transactions

##### The off-by-one-error that covered another off-by-one-error up

Monday, April 27, 2020

Some of the regularly used Bitcoin wallets, for example, the Bitcoin Core
wallet and the Electrum Bitcoin Wallet, set the locktime of newly constructed
transactions to the current block height. This is as an anti-fee-sniping
measure and visible as a stair-like pattern when plotting time-locked
transactions by their mempool arrival time and locktime. The plot, however,
reveals transactions time-locked to a future block height. These should,
usually, not be relayed through the Bitcoin network.

* * *

Bitcoin transactions can contain so-called time locks as a time-based validity
condition. Different types of time locks are used in Bitcoin. The focus here
lies on transactions time-locked with a lock-by-block-height to an absolute
block height by utilizing the `nLocktime` field. This field holds a 32-bit
unsigned integer and is present in every Bitcoin transaction. A `nLocktime`
value between `0` and `500000000` specifies a lock-by-block-height. The
Bitcoin consensus rules define that a transaction with a lock-by-block-height
of `n` can only be included in a block with a height of `n` `+` `1` or higher.
Likewise, a block with the height `n` can only include transactions with a
locktime of `n` `-` `1` or less. At least one input of the transaction must
have a `nSequence` below `0xFFFFFFFF` for the time lock to be enforced.
Otherwise, the lock is ignored. The Bitcoin Core software does not relay
transactions with an enforced locktime higher than the current block height.

Some Bitcoin wallets specify a lock-by-block-height with the current height
when creating a new transaction. This makes a potentially disruptive mining
strategy, called fee-sniping, less profitable. Fee-sniping is currently not
used by miners but could cause chain reorgs in the future. Since the block
subsidy declines to zero over time, transaction fees will become the main
monetary incentive for miners. If a recent block contains a transaction paying
a relatively high fee, then it could be profitable for a larger miner to
attempt to reorg this block. By mining a replacement block, the sniping miner
can pay out the transaction fees to himself, as long as his block ends up in
the strong-chain. The fee-sniping miner is not limited to pick the same
transactions as the miner he is trying to snipe. He would want to maximize his
profitability by picking the highest feerate transactions from both the to-be-
replaced-block and the recently broadcast transactions currently residing in
the mempool. The more hashrate a fee-sniping miner controls, the higher is the
probability that he will win the block-race. Miners have the risk of losing
such a block-race, leaving them without reward.

A constant backlog of transactions paying a similar or even the same feerate
would be needed to incentivize miners to move the chain forward. When mining a
next block yields roughly the same revenue as sniping the previous, then a
rational miner would not start a block-race. However, setting the current
block height as a lock-by-block-height forbids a fee-sniping miner to use
transactions from the mempool his replacement block. It creates an incentive
to move the chain forward to be able to include the next batch of time-locked
transactions in a block. While this does not fully mitigate fee-sniping, it
reduces profitability. The more transactions enforce a time lock to the
current block height, the less profitable fee-sniping is.

![anti-fee-sniping example](/data/mo/mo1-locktime-stairs/fee-sniping.png)

Example: Making fee-sniping less profitable by setting the current block
height as a lock-by-block-height. Block `b2`, with a height of `n` `+` `1`,
pays its miner a high fee. Another miner, Eve, attempts to snipe block `b2`
with block `b2*`. The mempool includes two transactions paying a relatively
high fee of one bitcoin each. However, Eve can only include transaction `tx1`
in block `b2*`. Transaction `tx2` can not be included in `b2*` as it is only
valid in a block with a hight of `n` `+` `2` or more.

When the block height increases, the locktime newly constructed transactions
should increase as well. Transactions with the locktime set to the current
block height should appear as a stair-pattern when plotted by mempool arrival
time and locktime.

### Observation

Transactions observed by the [Bitcoin Transaction
Monitor](https://mempool.observer/monitor) project on December 17, 2019 are
plotted. A stair-pattern of transactions with a lock-by-block-height is
visible.

Javascript is disabled or blocked. Here is a screenshot of the interactive
chart you are not seeing.

![noscript chart replacement](/data/mo/mo1-locktime-stairs/noscript-
chart-1.png)

The scatterplot shows a dot for each transaction with a locktime between
608507 and 608519 that was broadcast on December 17, 2019, between 12:06 and
14:08 UTC. The radius represents the feerate the transaction paid. Blocks
found in the displayed timeframe (height 608509 to 608519) are drawn.

Some transactions are locked to a height below the current block height. These
are likely not broadcast immediately after their creation. This happens, for
example, with high-latency mixers and some CoinJoin implementations.
Additionally, the Bitcoin Core wallet [randomly
chooses](https://github.com/bitcoin/bitcoin/blob/e6acd9f72c61bf535d9413854b1434ec40633ca0/src/wallet/wallet.cpp#L2490-L2495)
a locktime up to 100 blocks below the current height for 10% of the signed
transactions to increase the privacy of the not immediately broadcast
transactions.

The plot, however, does show transactions with two different locktimes
arriving at the same time. Transactions time-locked to the current block
height and transactions time-locked to the next block height. Between block
608511 and block 608512, for example, transactions with a locktime of 608511,
the current height, and 608512, the next block height, arrived. These should,
normally, not be relayed trough the network.

### Interpretation

The transactions time-locked to the next block height have inputs with a
`nSequence` number of `0xFFFFFFFF`. The lock-by-block-height is thus not
enforced. All of these transactions have common properties and share a
somewhat unique fingerprint. All are spending P2SH, nested P2WSH, or P2WSH
inputs and are
[BIP-69](https://github.com/bitcoin/bips/blob/master/bip-0069.mediawiki)
compliant (inputs and outputs ordered lexicographically). Most of them pay a
feerate of 12.3 sat/vbyte and all spending 2-of-3 multisig inputs. This leads
to the assumption that these transactions are constructed with the same wallet
or by the same entity.

Javascript is disabled or blocked. Here is a screenshot of the interactive
chart you are not seeing.

![noscript chart replacement](/data/mo/mo1-locktime-stairs/noscript-
chart-2.png)

The same transactions as above are shown but transactions spending multisig
inputs are highlighted in blue.

The fingerprint, especially spending 2-of-3 multisig, limits the number of
wallets or entities which the transactions could originate from. Reaching out
to a possible entity, which prefers to remain unnamed, proved to be
successful. They confirmed the two off-by-one-errors. Firstly, the
transactions should be time-locked to the current block height and not the
next block height. Secondly, at least one of the inputs should have a
nSequence number of `0xFFFFFFFF-1` or less for the time-lock to be enforced. A
fix for this has been released in early 2020\. However, it will take a while
before all instances of the currently deployed software are upgraded.

Between September 2019 and March 2020, about 10.9 million (19%) out of the
57.49 million total transactions set a locktime. Out of these, 1.16 million
transactions had an unenforced locktime. That represents 2% of the total and
about 10% of all transactions with a locktime. More than 98% of the
transactions with an unenforced time-lock share the same fingerprint as the
transactions observed on the 17th of December. The remaining 21577
transactions are likely broadcast by other entities. Out of these, 92.5% have
an unenforced lock-by-block-height and 7.5% an unenforced lock-by-block-time.
Some transactions with unenforced locktimes might have valid use-cases while
others unknowingly set an unenforced locktime.

### Conclusion

Some bitcoin wallets reduce the profitability of fee-sniping by time-locking
transactions to the next block. This appears as a stair-pattern when plotting
the arrival time and the locktime of transactions. The plot reveals
transactions with locktimes higher than the current block height. These
should, usually, not be relayed through the Bitcoin network. This leads to the
discovery that a large entity transacting on the Bitcoin network does not
properly set the `nSequence` field of their transaction inputs. This allowed
for the off-by-one-error in the transaction locktimes to remain unnoticed.

* * *

_I thank[David Harding](https://dtrt.org/) for commenting on an early draft of
this article. I found the background information he provided to be very
valuable. Any errors that remain are my own._

Enable JavaScript to view comments. Comments are privacy friendly and self-
hosted with [isso](https://posativ.org/isso/).

All text and images in this work are licensed under a [Creative Commons
Attribution-ShareAlike 4.0 International
License](http://creativecommons.org/licenses/by-sa/4.0/) [![Creative Commons
License](https://i.creativecommons.org/l/by-
sa/4.0/80x15.png)](http://creativecommons.org/licenses/by-sa/4.0/)

#### Next

![Image for The daily BitMEX broadcast at 13:08 UTC](/data/mo/mo2-bitmex-
broadcast/header.png) [](/mempool-observations/2-bitmex-broadcast-13-utc/)

* * *

May 4, 2020

#### The daily BitMEX broadcast at 13:08 UTC

At around 13:00 UTC every day, BitMEX, a cryptocurrency exchange and
derivative trading platform, broadcasts multiple megabytes of large
transactions into the Bitcoin network. This affects the transaction fees paid
during European afternoons and US business hours. The transaction size could
be …

[](/mempool-observations/2-bitmex-broadcast-13-utc/)

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

