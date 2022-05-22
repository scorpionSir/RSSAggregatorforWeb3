[ ![0xb10c logo](/0xb10c.png) ](/)

# 0xB10C

Bitcoin Developer

[Blog](/) [Mempool Observations](/mempool-observations) [Projects](/projects)
[Talks](/talks)

☀  requires JS

##  A List of Public Bitcoin Feerate Estimation APIs

#####

Saturday, June 29, 2019

My search for a list of public Bitcoin feerate estimation APIs ended without
any real results. [Jameson Lopp](https://twitter.com/lopp) has a section on
feerate estimators on his [bitcoin.page](https://www.lopp.net/bitcoin-
information/fee-estimates.html) and [Antoine Le
Calvez's](https://twitter.com/khannib) dashboard
[txstats.com](https://txstats.com/dashboard/db/fee-estimation) provides a
visualization of different estimation APIs. But that is not what I was looking
for. That's why I compiled this list.

I opted to only include publicly advertised feerate estimation APIs by e.g.
payment processors and block explorers. I'm purposefully leaving out list APIs
by wallets, such as Mycelium and Trezor because their APIs are not publicly
advertised. Additionally, I'm leaving out Bitcoin Core's feerate estimates via
the [`estimatesmartfee`
RPC](https://bitcoincore.org/en/doc/0.18.0/rpc/util/estimatesmartfee/). I
don't consider the RPC publicly reachable as in _reachable over the web by
everyone_ (some [services](https://wasabiwallet.io/swagger/index.html) wrap
the `estimatesmartfee` RPC however).

The following list of public feerate APIs is lexicographically sorted.

* * *

### bitcoiner.live API

The [bitcoiner.live](https://bitcoiner.live/) API provides `sat/vByte`
estimates for confirmation in half an hour, 1 hour, 2 hours, 3 hours, 6 hours,
12 hours and 24 hours. It's reachable under
[`https://bitcoiner.live/api/fees/estimates/latest`](https://bitcoiner.live/api/fees/estimates/latest).

    
    
    {
      "timestamp": 1563456789,
      "estimates": {
        "30": {
          "sat_per_vbyte": 12.0,
          [ ... ]
        },
        "60": {
          "sat_per_vbyte": 12.0,
          [ ... ]
        },
        "120": {
          "sat_per_vbyte": 8.0,
          [ ... ]
        },
        [ ... ]
      }
    }
    

* * *

### BitGo API

Bitgo's feerate API is reachable under
[`https://www.bitgo.com/api/v2/btc/tx/fee`](https://www.bitgo.com/api/v2/btc/tx/fee)
and there is documentation available
[here](https://bitgo.com/api/v2/#operation/v2.tx.getfeeestimate). The API
returns estimates for different block targets in **`sat/kB`**. ( _`sat/kB /
1000 = sat/Byte`_ )

    
    
    {
      "feePerKb": 61834,
      "cpfpFeePerKb": 61834,
      "numBlocks": 2,
      "confidence": 80,
      "multiplier": 1,
      "feeByBlockTarget": {
        "1": 64246,
        "2": 61834,
        "3": 56258,
        [ ... ]
      }
    }
    

* * *

### Bitpay Insight API

The API of Bitpay's Insight instance is available under
[`https://insight.bitpay.com/api/utils/estimatefee?nbBlocks=2,4,6`](https://insight.bitpay.com/api/utils/estimatefee?nbBlocks=2,4,6).
With the parameter `nbBlocks` the confirmation target in the next _`n`_ blocks
can be specified. Feerates are in **`BTC/kB`**. _(`BTC/kB x 100000 =
sat/Byte`)_

    
    
    {
      "2": 0.00051894,
      "4": 0.00047501,
      "6": 0.00043338
    }
    

* * *

### Blockchain.info API

Blockchain.info recommends **`sat/Byte`** feerates via
[`https://api.blockchain.info/mempool/fees`](https://api.blockchain.info/mempool/fees).
They provide a `regular` and a `priority` feerate. Additionally a `minimum`
and `maximum` feerate are included.

    
    
    {
      "limits": {
        "min": 2,
        "max": 79
      },
      "regular": 4,
      "priority": 53
    }
    

* * *

### Blockchair API

The Blockchair API offers a transaction fee suggestion in **`sat/Byte`** via
[`https://api.blockchair.com/bitcoin/stats`](https://api.blockchair.com/bitcoin/stats).
While their API is publicly available for occasional requests, they require an
API key for more and periodical requests. You can read more about the API
[here](https://github.com/Blockchair/Blockchair.Support/blob/master/API.md).

    
    
    {
      "data": {
        [ ... ]
        "suggested_transaction_fee_per_byte_sat": 1
      },
      [ ... ]
    }
    

* * *

### BlockCypher API

The BlockCypher API includes a `low`, `medium` and `high` feerate estimate in
[`https://api.blockcypher.com/v1/btc/main`](https://api.blockcypher.com/v1/btc/main).
The feerates are in **`sat/kB`**. ( _`sat/kB / 1000 = sat/Byte`_ )

    
    
    {
      [ ... ]
      "high_fee_per_kb": 41770,
      "medium_fee_per_kb": 25000,
      "low_fee_per_kb": 15000,
      [ ... ]
    }
    

* * *

### Blockstream.info API

Blockstream.info offers an API returning feerates for different confirmation
targets in **`sat/vByte`** under [`https://blockstream.info/api/fee-
estimates`](https://blockstream.info/api/fee-estimates). The API is documented
[here](https://github.com/Blockstream/esplora/blob/master/API.md#fee-
estimates).

    
    
    {
      "2": 32.749,
      "3": 32.749,
      "4": 24.457,
      "6": 20.098,
      "10": 18.17,
      "20": 10.113,
      "144": 1,
      "504": 1,
      "1008": 1
    }
    

* * *

### BTC.com API

BTC.com offers a feerate estimate for the next block in **`sat/Byte`** under
[`https://btc.com/service/fees/distribution`](https://btc.com/service/fees/distribution).

    
    
    {
      "tx_size": [ ... ],
      "tx_size_count": [ ... ],
      "tx_size_divide_max_size": [ ... ],
      "tx_duration_time_rate": [ ... ],
      "fees_recommended": {
        "one_block_fee": 14
      },
      "update_time": "1563456789"
    }
    

* * *

### earn.com API

The API behind [bitcoinfees.earn.com](https://bitcoinfees.earn.com) is
reachable under
[`https://bitcoinfees.earn.com/api/v1/fees/recommended`](https://bitcoinfees.earn.com/api/v1/fees/recommended).
Feerate estimates for the `fastest` confirmation, a confirmation in `half an
hour` and `a hour` are shown in **`sat/Byte`**.

    
    
    {
      "fastestFee": 44,
      "halfHourFee": 44,
      "hourFee": 4
    }
    

* * *

Please let me know if you know a feerate estimation API I should add to the
list.

Enable JavaScript to view comments. Comments are privacy friendly and self-
hosted with [isso](https://posativ.org/isso/).

All text and images in this work are licensed under a [Creative Commons
Attribution-ShareAlike 4.0 International
License](http://creativecommons.org/licenses/by-sa/4.0/) [![Creative Commons
License](https://i.creativecommons.org/l/by-
sa/4.0/80x15.png)](http://creativecommons.org/licenses/by-sa/4.0/)

#### Next

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

#### Previous

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
the data wasn't as easy as I first thought.

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

