[ ![0xb10c logo](/0xb10c.png) ](/)

# 0xB10C

Bitcoin Developer

[Blog](/) [Mempool Observations](/mempool-observations) [Projects](/projects)
[Talks](/talks)

☀  requires JS

##  Following the Blockchain.com feerate recommendations

##### Wallet fingerprinting nearly a third of all Bitcoin transactions

Monday, July 13, 2020

Transactions sent with Blockchain.com wallets make up for about a third of all
Bitcoin transactions. A methodology to identify these transactions is
described and used. Insights about the wallet-usage are derived from the
resulting dataset. The privacy implications and possible improvements are
discussed.

* * *

One of the first observations made when building the [Bitcoin Transaction
Monitor](https://mempool.observer/monitor) was that many transactions
precisely follow the recommendations of a feerate estimator. These
transactions appear as horizontal bands, which rise and sink as the feerate
recommendations change.

![Transactions following the Blockchain.com feerate
recommendations](/data/mo/mo3-blockchaincom-recommendations/bands.png)

Most of these transactions share the same fingerprint. Only P2PKH outputs are
spent. No SegWit and neither multisig are spent. With every transaction,
either one or two outputs are created. When two outputs are created, then at
least one of them is a P2PKH output. The transactions are not time-locked,
have a version of one, and do not signal [BIP-125
replaceability](https://github.com/bitcoin/bips/blob/master/bip-0125.mediawiki).
However, all are
[BIP-69](https://github.com/bitcoin/bips/blob/master/bip-0069.mediawiki)
compliant.

This matches the fingerprint of the Blockchain.com wallets: namely a Web, an
iOS, and an Android wallet. The wallets can only receive and spend P2PKH
outputs. While users can pay to all address formats1, the change-output, if
created, is a P2PKH output. The wallets construct the transactions with a
locktime of zero and a transaction version of one. The inputs and outputs are
all lexicographically sorted as specified by BIP-69.

The wallets use the Blockchain.com feerate estimator, which is publicly
accessible via [an API](https://b10c.me/blog/003-a-list-of-public-bitcoin-
feerate-estimation-apis/#blockchaininfo-api). The API returns two feerate
estimates: _priority_ and _regular_. The _priority_ feerate aims for
confirmation in the next hour and the _regular_ feerate for confirmation in an
hour or more. By default, the wallets follow the recommendations closely.
Users can set a custom feerate, but a warning is displayed.

### Methodology

Combining the feerate estimates and the transaction fingerprints makes it
possible to identify transactions sent with one of the Blockchain.com wallets.
While the majority of the Blockchain.com transactions pay exactly the
recommended feerate, some under- or overpay by a fixed percentage. This is
caused by incorrect assumptions about the transaction size during the
calculation of the transaction fee. The transaction fee is the product of the
targeted feerate and the assumed transaction size. The final and actual
transaction size is only known after adding the signature to the transaction.

    
    
    fee  =  target feerate  ×  assumed transaction size
    

All underpaying transactions have two outputs. However, during the fee
calculation, the size of a one-output transaction is assumed. For example, for
a P2PKH _1in ⇒ 2out_ transaction (226 bytes), the size of a _1in ⇒ 1out_
transaction (192 bytes) is used. This incorrect assumption results in the
transaction only paying around 85% (192 byte / 226 byte) of the recommended
feerate. As the transaction inputs make up for a large part of the transaction
size, the effect is smaller for transactions with more inputs. This behavior
was only present in the Blockchain.com Web wallet. A fix was
[released](https://github.com/blockchain/blockchain-
wallet-v4-frontend/releases/tag/v4.32.6) on April 21st, 2020.

![Transactions over- and underpaying by a fixed
percentage](/data/mo/mo3-blockchaincom-recommendations/over-underpaying.png)

The overpaying transactions all have a single output. For these, a second
output is assumed during the fee calculation. To calculate the fee of a P2PKH
_1in ⇒ 1out_ transaction (192 bytes), the size of a _1in ⇒ 2out_ transaction
(226 bytes) is used. This results in the transaction paying about 118% (226
byte / 192 byte) of the recommended feerate. Similar to the underpaying
transactions, the effect is smaller for transactions with more inputs. These
transactions are assumed to originate from the Blockchain.com iOS wallet. This
has not yet been confirmed.

![Visual explainer for methodology used to identify Blockchain.com
transactions](/data/mo/mo3-blockchaincom-recommendations/methodology.png)

Out of the set of transactions with the Blockchain.com wallet fingerprint, the
transactions paying the feerate recommended by the Blockchain.com feerate
estimator are selected. Transactions broadcast on April 19th, 2020, are shown.
The y-axis is centered around the _regular_ recommendation, which was 3
sat/vbyte for most of the day. Between 12:00 UTC and 17:00 UTC, the _regular_
recommendation briefly jumped to 4 sat/vbyte for a few minutes each. On other
days the feerate recommendations are usually more volatile. April 19th is a
Sunday. Sundays are known for less network activity compared to weekdays. This
day has been specifically chosen to showcase the methodology.

Identifying Blockchain.com wallet transactions with this methodology is not
assumed to be perfectly accurate or reliable. For example, transactions send
with a custom feerate can not be identified and are false negatives.
Transactions constructed by different wallets that pay a similar feerate and
share the fingerprint could be identified as false positives. When the
recommended feerate is volatile, which is often the case for the _priority_
recommendation (for example, shortly after [the daily BitMEX
broadcast](https://b10c.me/mempool-observations/2-bitmex-broadcast-13-utc/)),
then some transactions might pay a feerate not recoded by the Bitcoin
Transaction Monitor. Additionally, the wallets could construct a transaction
using an older recommendation, which is different from the recommendation at
the time the transaction is broadcast. These transactions are false negatives
as well.

### Observations

The described methodology is used to identify the transactions send with
Blockchain.com wallets between April 1st and May 20th, 2020. The resulting
dataset spans over 50 days and contains about 4 million transactions. These
pay a total fee of 445.73 BTC and account for about 1.34 GB of block space.
Roughly two-thirds of the Blockchain.com wallet transactions target the
_regular_ feerate while the remaining third targets the _priority_ feerate.

Roughly the same number of outputs are created as are spend. Blockchain.com
wallet transactions have either a single payment-output or a payment-output
and a change-output. As the change-outputs are always P2PKH outputs, it is
possible to determine the payment-output type. Out of all outputs created
about 31.7% are P2PKH, 23.3% are P2SH, 0.34% are P2WPKH, and less than 0.01%
are P2WSH payment-outputs. The remaining 45.5% are P2PKH change-outputs. The
most commonly used input-output combinations are _P2PKH ⇒ P2PKH + P2PKH_ with
33%, _P2PKH ⇒ P2SH + P2PKH_ with 26%, and _P2PKH ⇒ P2PKH_ with around 7%.

  

Users of the Blockchain.com wallet are most active between 15:00 UTC and 18:00
UTC and least active between 4:00 UTC and 5:00 UTC. At around 5:00 UTC, the
number of transactions per minute starts to rise. At this time it is 8am in
Moscow, and 7am in central Europe. Between 5:00 UTC and 10:00 UTC, the number
of transactions per minute rises from about 30 to just above 60. The
transactions per minute remain constant until rising again at noon UTC, which
is 8am on the US east coast. The daily maximum is reached at around 16:00 UTC
with just above 75 transactions per minute. From there on, the activity
declines until reaching the minimum number of transactions per minute at
around 4:00 UTC again.

![Activity hours of Blockchain.com wallet users.](/data/mo/mo3-blockchaincom-
recommendations/time-of-day.png)

The transactions broadcast per minute with Blockchain.com wallets are shown.
The error bands show the standard deviation. The time between 8am and 8pm is
marked for central Asia, Europe, and eastern US timezones.

  

[Reportedly](https://thecryptofeed.net/articles/blockchain-com-says-they-
account-for-a-third-of-all-bitcoin-transactions/), Blockchain.com claims that
their wallets are responsible for one-third of all Bitcoin transactions. They
[publish](https://www.blockchain.com/charts/my-wallet-n-tx) the daily number
of transactions sent by their wallets. This lead to a discussion on the
accuracy and correctness of these numbers. The described dataset can be used
to verify this claim. The number of daily transactions in the dataset and the
published numbers can be compared. The total number of transactions sharing
the fingerprint with the Blockchain.com wallet transactions acts as an upper-
bound. The total transactions per day are retrieved from
[transactionfee.info](https://transactionfee.info/charts/transactions-per-
day/) to calculate Blockchain.com's share of the network.

![Showing that the Blockchain.com published numbers could be reasonably
accurate.](/data/mo/mo3-blockchaincom-recommendations/one-third.png)

The daily transaction count published by Blockchain.com translates into a
network share of 30% to 35%. The share of the transactions with the same
fingerprint, the upper-bound, is on average about three absolute percent
higher. The share of the identified transactions in the dataset is about four
to five absolute percent lower than the Blockchain.com reported numbers at
around 27% on average. The transactions account for about 13% of the daily
fees paid, and 20% of the daily block space used.

However, the numbers reported by Blockchain.com still lie in a reasonable
range. There are multiple reasons why the described dataset could contain
fewer transactions than are reported by Blockchain.com. Some users might send
transactions with a custom feerate. These are not picked up by the described
methodology. Furthermore, it's not clear if the reported numbers include
transactions send with the [Blockchain.com Wallet
API](https://www.blockchain.com/de/api/blockchain_wallet_api). The API allows
users to construct transactions sending to multiple recipients which are not
accounted for in the described dataset.

  

With the knowledge that the Blockchain.com Web wallet underpaid the
recommended feerate for transactions with two outputs, and the iOS wallet
overpays on transactions with one output, the wallet's shares can be
estimated. For this, the assumption that the ratio of two-output to one-output
transactions is similar in all wallets must hold. The Web wallet accounts for
one-third and the iOS wallet for half of the Blockchain.com wallet
transactions. The Android wallet probably accounts for a majority of the
remaining 17%. However, this can not be verified as no data is indicating the
share of the Android wallet.

![Share of Web wallet transactions with two
outputs.](/data/mo/mo3-blockchaincom-recommendations/web-wallet-share.png)

Between April 1st and April 22nd, the two-output transactions send with the
Web wallet made up for about a third of all two-output transactions send with
Blockchain.com wallets. The shown mean is weighted with the transaction
counts. A fix [released](https://github.com/blockchain/blockchain-
wallet-v4-frontend/releases/tag/v4.32.6) on April 21st resolved the
underpaying behavior for two-output transactions in the Web wallet. It took a
few days until the release got deployed.

![Share of iOS wallet transactions with a single
output.](/data/mo/mo3-blockchaincom-recommendations/iOS-wallet-share.png)

Between April 1st and May 20th, the one-output transactions send with the iOS
wallet made up for about half of all one-output transactions constructed by
Blockchain.com wallets. The shown mean is weighted with the transaction counts
per input-output combination. It's unclear why the iOS wallet would account
for 60% to 70% of the _4+in ⇒ 1out_ transactions.

  

The iOS wallet overpays and the Web wallet underpaid the recommended feerate
for some input-output combinations. This is noticeable in the time it takes
for a transaction to confirm when targeting the _regular_ feerate
recommendation. The overpaying transactions fill up most of the block space,
and transactions paying or underpaying the recommended feerate are only
included in later blocks. In median, a one-output transaction send with the
iOS wallet confirms the fastest. Two-output transactions sent with the Web
wallet took the longest. The Web wallet's effect was the strongest for
transactions with one-input and two-outputs, which is the [most commonly
used](https://transactionfee.info/charts/transactions-1in-2out/) input-output
combination. These only paid about 85% of the recommended feerate.
Transactions send with the Android wallet, iOS wallet transactions with two
outputs or Web wallet transactions with one output confirm after the iOS
wallet transactions with one-output and before the Web wallet transactions
with two-outputs.

![Time to confirmation by input-output
combination](/data/mo/mo3-blockchaincom-recommendations/time-to-
confirmation.png)

Box plots for the different input-output combinations show the distribution of
the times it took for the transactions to confirm. The data ranges from April
1st to April 22nd, 2020. On April 21st, the fix for the Web wallet was
released. The median time to confirmation is annotated. Not outliners are
shown in the box plots.

Paying a slightly higher feerate than the Blockchain.com iOS wallet pays for a
one-output transactions could be a good trade-off between a fast confirmation
and paying a low transaction fee. An advanced user could target a feerate of,
for example, about 120% of the _regular_ recommendation. A miner would include
the transaction in a block before any of the Blockchain.com transactions are
included. Targeting, for example, 102% of the _regular_ recommendation could
be an option too. This would be cheaper, but the transaction might take longer
to confirm as the overpaying iOS wallet transactions confirm first. The
effectiveness of these strategies might be reduced when the feerate
recommendations are volatile during high activity hours.

  

Taking a closer look at the transactions paying the recommended feerate shows
transactions with P2SH outputs pay a slightly higher feerate than transactions
with P2PKH outputs. In the Blockchain.com wallets, the assumed size of a
single P2PKH output with 34 bytes is used in the fee calculation. P2SH
outputs, with 32 bytes, are slightly smaller. Transactions with a P2SH output
pay for two extra bytes, when the P2PKH output size is used. This results in
transactions with P2SH outputs paying a slightly higher feerate. Something
similar can be observed for transactions with a P2WPKH output, which have a
size of 31 bytes. These pay for three bytes they do not have. P2WSH outputs
take up 43 bytes, and thus transactions with a P2WSH output slightly underpay
the recommended feerate as they are not paying for 9 bytes.

Users sending their funds to other wallets or services by creating a
transaction that pays to a P2SH or a P2WPKH output unknowingly pay a minimally
higher fee than they would have to. On average, these transactions confirm
earlier. Transactions with P2WSH outputs pay slightly less than the
recommendation and take longer to confirm on average. These effects are
probably most noticeable during high activity hours.

![Closer look at the transactions paying the recommended
feerate.](/data/mo/mo3-blockchaincom-recommendations/closer-look.png)

Transactions paying exactly the recommended feerate of 3 sat/vbyte on April
19th, 2020, are shown. Between 12:00 UTC and 15:00 UTC, the recommended
feerate was briefly at 4 sat/vbyte or more. This is out-of-bounds and not
shown. The most common input-output combinations are annotated. It's visible
that transactions with P2SH outputs, here marked in orange, pay a slightly
higher feerate that P2PKH transactions. Transactions with P2WSH outputs are
out-of-bounds on this graph, and transactions with more than four outputs are
not shown.

Some transactions with the same input-output combinations appear multiple
times at different feerates and have slightly different sizes. Low and high
R-values in the ECDSA signatures can cause a one-byte size difference per
input. Some transactions have the same input-output combination and the same
size but pay a different fee, even when targeting the same feerate. This is
caused by the iOS and Android wallet assuming a different P2PKH input size as
the Web wallet. The Web wallet uses [147
bytes](https://github.com/blockchain/blockchain-
wallet-v4-frontend/blob/cbea2ba2ccfc50327186b8c8e9313a3c812c5ee5/packages/blockchain-
wallet-v4/src/coinSelection/coin.js#L20-L24), and the
[Android](https://github.com/blockchain/My-
Wallet-V3-Android/blob/cba6a66c93c41daf6dcabfc398cf25f0f9ec2fb4/wallet/src/main/java/info/blockchain/wallet/payment/CoinSelection.kt#L6-L8)
and [iOS](https://github.com/blockchain/My-
Wallet-V3-iOS/blob/master/BitcoinKit/Services/CoinSelection/CoinSelection.swift#L35-L39)
wallet both use 149 bytes. P2PKH inputs are usually either 147 or 148 bytes.
This depends on the R-value in the signature being either low or high. The
sizes assumed by the Android and iOS wallet are incorrect. P2PKH inputs with
149 bytes were only possible when high-S values were allowed in the
standardness rules before October 2015. More history on the lengths of ECDSA
signatures can be found [here](https://transactionfee.info/charts/bitcoin-
script-ecdsa-length/).

### Privacy

The more information a passive observer can derive from a Bitcoin transaction
and public metadata, the worse the impact on the privacy of the sender and the
recipient. Being able to identify the sending wallet is an information leak.
To improve the privacy of Blockchain.com wallet users and to reduce the
effectiveness of the described methodology, the recommended feerate should not
be followed as closely, and the wallet fingerprint should be broadened.

A key part of reliably identifying Blockchain.com wallet transactions is to
select the transactions that pay exactly the recommended feerates. By
introducing randomness in feerates, the transactions mix with non-
Blockchain.com wallet transactions. This increases the false-positive rate of
the described methodology making it less reliable.

The term anonymity pool is used to describe the set of transactions with the
same wallet fingerprint. The more wallets construct transactions with the same
fingerprint, the harder it gets to identify the wallet a transaction
originates from. This improves the privacy of all Bitcoin users. While the
Blockchain.com anonymity pool consists of often more than 100000 transactions
per day, the Blockchain.com wallets make up for at least 80% of these
transactions. The fingerprint can be broadened in different ways, which
increases the anonymity pool size and thus decreases the Blockchain.com's
share. This would have a positive effect on the privacy of Blockchain.com
wallet users and the privacy of all other Bitcoin users. To broaden the
fingerprint of the Blockchain.com wallet, it could, for example, support
receiving to and spending from different address types, time-lock some of the
created transactions to the current block height, or set a random transaction
version when constructing the transaction.

For advanced users, it might be possible to hide their transactions in the
anonymity pool of the Blockchain.com transactions. This could be done by
mimicking the Blockchain.com wallet fingerprint and paying exactly the
recommended feerate. If done correctly, somebody trying to wallet fingerprint
transactions with the described methodology would false positively identify
the transaction as sent by a Blockchain.com wallet. Blockchain.com could track
which transactions were constructed by one of their wallets and which only try
to mimic their wallets. This information could be sold to adversaries.

* * *

_Personal note: I value the privacy of the individual. I won 't publish the
transactions or txids I identified as Blockchain.com transactions. However, a
motivated passive listener could easily use the outlined methodology to start
tagging Blockchain.com users. I publish the above intending to raise awareness
about the issue. Especially the awareness of Blockchain.com, users of the
Blockchain.com wallets, and developers of other wallets closely following a
feerate estimator. If you think I should have disclosed this privately before
publishing it, please let me know - either in private or by calling me out
publicly._

_While my[Mempool Observations](https://b10c.me/mempool-observations/) are fun
to write, the process is very time-consuming. You can support me
[here](https://b10c.me/projects/), which enables me to spend more of my time
researching and writing. If you work for a company interested in improving
your on-chain foot- and fingerprint, then I'd be more than happy to chat. If
you are working on improving Bitcoin privacy, especially on removing wallet
fingerprints, then I'd like to contribute the things I've learned starring at
my [Bitcoin Transaction Monitor](https://mempool.observer/monitor/). My
contact information can be found at the bottom of this page._

* * *

  1. I realized that I was not able to send to a bech32 P2WPKH address in the Android wallet when trying to withdraw funds used to test the wallet behavior. It is however possible to send to a bech32 address in the Web wallet. ↩︎

Enable JavaScript to view comments. Comments are privacy friendly and self-
hosted with [isso](https://posativ.org/isso/).

All text and images in this work are licensed under a [Creative Commons
Attribution-ShareAlike 4.0 International
License](http://creativecommons.org/licenses/by-sa/4.0/) [![Creative Commons
License](https://i.creativecommons.org/l/by-
sa/4.0/80x15.png)](http://creativecommons.org/licenses/by-sa/4.0/)

#### Previous

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

