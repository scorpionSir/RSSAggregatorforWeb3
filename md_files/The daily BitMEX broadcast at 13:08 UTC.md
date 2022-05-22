[ ![0xb10c logo](/0xb10c.png) ](/)

# 0xB10C

Bitcoin Developer

[Blog](/) [Mempool Observations](/mempool-observations) [Projects](/projects)
[Talks](/talks)

☀  requires JS

##  The daily BitMEX broadcast at 13:08 UTC

##### Using a fingerprint to reason about a footprint

Monday, May 4, 2020

At around 13:00 UTC every day, BitMEX, a cryptocurrency exchange and
derivative trading platform, broadcasts multiple megabytes of large
transactions into the Bitcoin network. This affects the transaction fees paid
during European afternoons and US business hours. The transaction size could
be greatly reduced by implementing current industry standards in the BitMEX
wallet. Once activated, utilizing Schnoor and Taproot combined with output
batching seems to be the most promising for improving the transaction count
and size.

* * *

The observation that BitMEX broadcasts transactions every day at around 13:00
UTC is [not novel](https://twitter.com/ziggamon/status/1134490591264497664).
The transactions are mainly withdrawals initiated by BitMEX users and some
internal UTXO consolidations1. As part of their [wallet security
practice](https://www.bitmex.com/app/security#Wallet-Security), BitMEX reviews
and processes all withdrawals by hand. They
[claim](https://twitter.com/BitMEXdotcom/status/1135306176344862721) that
doing so multiple times a day would be infeasible and worry that spreading the
transaction broadcast over the day, which would lighten the burden on the
network, could decrease their user's experience.

BitMEX transactions have a unique fingerprint which originates from their in-
house multi-signature wallet solution. All transactions strictly spend P2SH
outputs with 3-of-4 multisig redeem scripts. The four public keys used in the
redeem script are uncompressed. The hashed and encoded redeem script result in
addresses with the prefix '3BMex'2. BitMEX does not spend SegWit outputs, and
all transactions have a version of 2. These properties make it straightforward
to recognize BitMEX transactions on the chain and in the mempool.

### Observations

A dataset consisting of the transactions observed by the [Bitcoin Transaction
Monitor](https://mempool.observer/monitor) between September 2019 and March
2020 is used. In these six months, BitMEX broadcast around 415 000
transactions into the Bitcoin network. Summed together, these take up around
593 MB and pay a total miner fee of 181 BTC. This represents about 2.8% of the
total bytes and 3.8% of the total fees broadcast in this period.

The median broadcast contains 2209 transactions, 5688 3-of-4 multi-signature
inputs, pays 0.95 BTC in miner fees, and has a total size of 3.16 MB. The
input count, the miner fees, and the total broadcast size grow linear with the
transaction count. On weekends, fewer transactions are broadcast than on
weekdays, and thus the input count, total miner fee, and broadcast size are
usually less.

![Broadcasts statistics covering transaction count, fees and size split up by
weekend and weekday.](/data/mo/mo2-bitmex-broadcast/stats.png)

With more than 500 bytes each, the 3-of-4 multi-signature inputs account for
most of the transaction size. About 26% of the transactions have one, 36% have
two, 32% have three, 3% have four, and about 2% have five or more inputs. The
transactions have either one (46%) or two outputs (54%).

The miner fees for withdrawals are not paid by BitMex. They are deducted from
the withdrawing users. The transaction feerate does not depend on the input
count nor the transaction size. Users choose a miner fee when withdrawing.
However, they do not know how many inputs the final withdrawal transaction
will spend and thus can not reason about the transaction size and required
feerate. All observed transaction fees are a multiple of 10 000 satoshi, which
is the minimum step size the withdrawal frontend allows. 10 000 satoshi is the
smallest, and most commonly (44%) observed withdrawal fee. It is followed by
100 000 satoshi (30%), 20 000 satoshi (17.5%), and 50 000 satoshi (3%). The
most commonly observed feerates, which result from the combination of a user-
picked fee and an algorithmically chosen number of inputs, are 17 (24%), 9
(19%), 60 (16%), 12 (10%), 88 (8%) and 18 sat/vbyte (8%).

BitMEX starts processing withdrawals at [13:00
UTC](https://bitmex.freshdesk.com/support/solutions/articles/13000015790-what-
time-are-withdrawals-processed-). It takes a few minutes before the
transactions are broadcast to the network. On some days, the first
transactions can be observed as early as 13:05 UTC. In median, the first
transaction arrives at 13:08:30 UTC. It takes about 2:14 minutes in median
until all transactions arrive on weekdays and 1:57 minutes in median on
weekends.

![time of day when BitMex transactions are broadcast](/data/mo/mo2-bitmex-
broadcast/time-distribution.png)

On three days in the observed six months, the broadcast was delayed by a few
minutes. These broadcasts are out-of-bounds for this plot. On the 1st of
November, 2449 transactions were broadcast starting at 13:40 UTC, on the 14th
of December, 1715 transactions were broadcast at 13:35 UTC, and on the 7th of
February, 2794 transactions were broadcast at 13:26 UTC.

The 25th percentile of broadcast transactions takes about 10 minutes to
confirm, the 50th percentile about 27 minutes and the 75th for about 71
minutes. The 80th percentile takes about two hours, the 86th for more than
three hours, the 92nd over five hours, and the 99th percentile over ten hours.

### Effects

Broadcasting multiple megabytes of transactions at various feerate levels has
immediate and noticeable effects on the network. The feerate estimators adjust
their recommendations, and the wallets using these recommendations set a
higher feerate when constructing a transaction. The minimum feerate for block-
inclusion rises and the time-to-confirmation spikes.

Feerate estimators correctly react to the thousands of large transactions
spread over different feerate levels. They recommend paying a higher feerate
to outbid the BitMEX transactions, which take up a significant part of the
available space in the next blocks. The median estimated feerates for
inclusion in the next, in the next three and the next six blocks, increase
sharply at around 13:00 UTC. The next block estimate stays at a high level for
a few hours. The three and six block estimates continue to increase to a
maximum between 16:00 and 17:00 UTC.

![Plot showing the effect on the feerate estimators](/data/mo/mo2-bitmex-
broadcast/effect-estimated-feerate.png)

The median estimated feerate is calculated by aggregating multiple estimates.
For each feerate estimator, the estimates between September 2019 and March
2020 are grouped by minute of day3. The median feerate estimate is picked and
averaged with the median estimates of other estimators for the block target. A
list of public feerate estimators with their block targets can be found
[here](https://b10c.me/blog/003-a-list-of-public-bitcoin-feerate-estimation-
apis/).

The feerates of the newly arriving transactions react to the increased
estimates. The average feerate sharply increases at around 13:00 UTC and
continues to rise over the next hours. At about 15:30 UTC, the daily maximum
is reached. From there on, the feerate starts to decrease slowly. It takes
until around 21:00 UTC before it sinks below the level of the initial spike.
At 13:00 UTC, it is afternoon in Europe and morning in the US. The higher
network activity at this time likely amplifies and lengthens the effect of the
BitMex broadcast. However, most of the near-vertical increase is presumably
caused by BitMEX alone. The effect of the US business hours is visible as a
slow increase and decrease over multiple hours.

![Plot showing the effect on the observed feerate](/data/mo/mo2-bitmex-
broadcast/effect-observed-feerate.png)

The feerate relative to midnight UTC is grouped by minute of day. The group
average is plotted.

Calculating the additional fees Bitcoin users pay as a result of the BitMEX
broadcast is hard. There is no data for days without a broadcast to compare
to. However, the magnitude of the effect can be estimated. Therefore, the
following assumption about the effect is made: The BitMEX broadcast causes an
average feerate increase by 4 sat/vbyte between 13:00 UTC and 21:00 UTC. The
blue area in the figure above visualizes the assumption. On average, 42.5 vMB
of non-BitMEX transactions arrive in the eight hours between 13:00 UTC and
21:00 UTC. If 4 additional satoshi are paid for each broadcast vbyte, then a
total of 1.7 BTC of additional fees are paid by Bitcoin users per day due to
the BitMEX broadcast. This represents about 17% of the total fees arriving
during the eight hours and about 6.8% of the total daily transaction fees.
However, it is unclear if the assumption holds. The estimate can only show the
magnitude of the average daily effect. One or even multiple days without a
BitMEX broadcast would be needed to further study it.

Both the median block feerate and the 5th percentile block feerate spike and
stay at an elevated level before slowly declining to pre-broadcast levels at
around 22:00 UTC. Transactions send with a low feerate might take a few hours
until they are included in a block during this period. The 5th percentile
block feerate represents nearly the minimum feerate included a block while not
picking up, for example, the parents of child-pays-for-parent transactions.

![Plot showing the effect on the block feerate](/data/mo/mo2-bitmex-
broadcast/effect-block-feerate.png)

The median and 5th percentile block feerate are calculated from the blocks in
the blockchain. The observed block arrival time (not the miner timestamp in
the block header) is used to group the blocks by minute of day. The group
median and the 5th percentile are plotted.

The median time-to-confirmation, the time between a transaction being first
observed and its confirmation in a block, spikes between 13:00 and 14:00 UTC
and remains at a slightly elevated level until around 21:00 UTC.

![Plot showing the effect on the time to first
confirmation](/data/mo/mo2-bitmex-broadcast/effect-time-to-confirmation.png)

Transactions are grouped by the minute of day of their arrival time. The
median time-to-confirmation for each minute of day is plotted. Only
transactions seen in the mempool and a block are used. Replaced transactions
are ignored.

### Improvements

The effects can be minimized by reducing the number of bytes broadcast to the
Bitcoin network. This can be achieved both by decreasing the transaction count
and size of the individual transactions.

The four uncompressed public keys used in every BitMEX input could be replaced
by compressed public keys. An uncompressed public key is 65 bytes long and can
be encoded in 33 bytes as a compressed public key by leaving out redundant
data. Wallets started using compressed public keys [as early as
2012](https://transactionfee.info/charts/bitcoin-script-pubkey-
compression/?start=2011-07-26&end=2013-03-13), and [by 2017 more than
95%](https://transactionfee.info/charts/bitcoin-script-pubkey-
compression/?start=2016-11-01) of all public keys added to the blockchain per
day are compressed4. By using compressed public keys, BitMEX could reduce
their transaction size by as much as 23%.

Transaction batching could help to minimize the amount of 3-of-4 multisig
change outputs being created. Spending the 3-of-4 multisig outputs makes up
for most of the block space used by BitMEX. Every output created needs to be
spent by supplying three signatures of around 71 bytes each and a redeem
script with four uncompressed public keys of 65 bytes each. This totals at
around 532 bytes per input. However, an even more block space-efficient
alternative would be to use a non-multisig wallet for user deposits, which are
periodically consolidated into a multisig wallet. Spending a few high-value
3-of-4 multisig outputs for multiple withdrawals batched together greatly
reduces the overall transaction count. Additionally, BitMEX operational costs
for manually reviewing and processing a few high-value transactions per day
would likely be lower than they currently are for reviewing a few thousand
lower-value withdrawals.

Spending SegWit would help as well. The large scripts used in the 3-of-4 P2SH
multisig inputs would be placed in the witness data. There they have less
effect on the transaction weight. In December 2019, BitMEX
[mentioned](https://blog.bitmex.com/bitmex-enables-bech32-sending-support/)
that their priority lies on upgrading their wallet to use P2SH wrapped SegWit.
They estimated around 65% in transaction weight savings for an average
withdrawal transaction.

Once activated, BitMEX users and the whole network could greatly benefit from
BitMEX utilizing Schnorr and Taproot. The three ECDSA signatures in the inputs
of BitMEX transactions with around 71 bytes each can be replaced by a single
64 bytes aggregate signature. The four uncompressed public keys of 65 bytes
each can be replaced by a single 32 byte tweaked public key. This public key
would be an aggregate of the three most commonly used public keys. It could be
tweaked for additional spending conditions5. A single P2TR (Pay-to-Taproot)
input does account for around 57 vbytes. This is an 89% reduction when
compared to the current input size. Combined with output batching, this could
drastically minimize the on-chain footprint of the BitMEX broadcast.
Additionally, Taproot would remove the unique fingerprint of BitMEX
transactions, which would, in turn, increase the privacy of BitMEX users.

### Conclusion

By using the fingerprint of BitMEX transactions, their footprint on the
Bitcoin network is observed and discussed. The daily broadcast has a
significant impact on the Bitcoin network and user fees. By utilizing scaling
techniques, some of which have been industry standards for multiple years, the
impact could be reduced. BitMEX is stepping in the right direction by planning
to switch to nested SegWit. They, however, shouldn't stop there.

* * *

_Disclaimer: I 've written this article to educate and inform. It's published
without bad intentions and no malice aforethought against BitMEX. I have not
been paid to cover this topic by neither BitMEX nor a competitor nor anybody
else. The information and data herein have been obtained from sources I
believe to be reliable. I make no representation or warranty as to its
accuracy, completeness, or correctness. This article has not been extensively
peer-reviewed._

* * *

  1. These usually don't contain many inputs, which is untypical for consolidations. On second thought, these might as well be withdrawals to other accounts on BitMEX. ↩︎

  2. I suspect that BitMEX reuses three of the four public keys of their multi-signature setup for multiple addresses (redeem scripts). A fourth and extra public key is used to iterate the redeem scripts until a '3BMex' prefixed vanity address is found. This is clever but wastes 1+65 bytes for each UTXO spent. Additionally, it might not have any security benefit if the fourth private key is not kept. ↩︎

  3. Minute of day: Imagine a vector with 24*60 (1440) entries. The first would be for minute 00:00, the second for 00:01 the sixty-third for minute 01:02, and the last for minute 23:59. ↩︎

  4. I assume that BitMEX currently accounts for the majority uncompressed public keys added to the blockchain per day. ↩︎

  5. If the second footnote holds, then the tweak might not even be required. Bonus: It could, however, be used to create vanity addresses prefixed with, for example, `'bc1mex'` (`'bc1bmex'` is not possible as the character `'b'` can't be used in the data part of the Bech32 address format). ↩︎

Enable JavaScript to view comments. Comments are privacy friendly and self-
hosted with [isso](https://posativ.org/isso/).

All text and images in this work are licensed under a [Creative Commons
Attribution-ShareAlike 4.0 International
License](http://creativecommons.org/licenses/by-sa/4.0/) [![Creative Commons
License](https://i.creativecommons.org/l/by-
sa/4.0/80x15.png)](http://creativecommons.org/licenses/by-sa/4.0/)

#### Next

![Image for Following the Blockchain.com feerate
recommendations](/data/mo/mo3-blockchaincom-recommendations/header.png)
[](/mempool-observations/3-blockchaincom-recommendations/)

* * *

July 13, 2020

#### Following the Blockchain.com feerate recommendations

Transactions sent with Blockchain.com wallets make up for about a third of all
Bitcoin transactions. A methodology to identify these transactions is
described and used. Insights about the wallet-usage are derived from the
resulting dataset. The privacy implications and possible improvements are
discussed.

[](/mempool-observations/3-blockchaincom-recommendations/)

#### Previous

![Image for The stair-pattern in time-locked Bitcoin
transactions](/data/mo/mo1-locktime-stairs/header.png) [](/mempool-
observations/1-locktime-stairs/)

* * *

April 27, 2020

#### The stair-pattern in time-locked Bitcoin transactions

Some of the regularly used Bitcoin wallets, for example, the Bitcoin Core
wallet and the Electrum Bitcoin Wallet, set the locktime of newly constructed
transactions to the current block height. This is as an anti-fee-sniping
measure and visible as a stair-like pattern when plotting time-locked
transactions by their mempool arrival time and locktime. The plot, however,
reveals transactions time-locked to a future block height. These should,
usually, not be relayed through the Bitcoin network.

[](/mempool-observations/1-locktime-stairs/)

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

