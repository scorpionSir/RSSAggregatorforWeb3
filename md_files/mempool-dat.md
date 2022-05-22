[ ![0xb10c logo](/0xb10c.png) ](/)

# 0xB10C

Bitcoin Developer

[Blog](/) [Mempool Observations](/mempool-observations) [Projects](/projects)
[Talks](/talks)

☀  requires JS

##  mempool-dat

#####

Thursday, May 16, 2019

A Golang package that can deserialize Bitcoin Core's `mempool.dat` files. This
is a toy project. I developed this to learn more about Golang and the
`mempool.dat` file format by Bitcoin Core.

This Go package parses Bitcoin Core's `mempool.dat` files. These are
automatically written since Bitcoin Core v0.14.0 on shutdown and can be
written manually by calling the RPC `savemempool` since Bitcoin Core v0.16.0.

The package offers access to the mempool.dat's

    
    
    - header
        - version
        - number of transactions
    - mempool entries
        - raw transaction parsed as (https://godoc.org/github.com/btcsuite/btcd/wire#MsgTx)
        - first seen timestamp
        - the feeDelta
    - and the not-parsed mapDeltas as byte slices
    

[Source on GitHub](https://github.com/0xB10C/mempool-dat) [Documentation on
GoDoc](https://godoc.org/github.com/0xB10C/mempool-dat/lib)

I've talked about the `LoadMempool()` and `DumpMempool()` functions of
[Bitcoin Core](https://github.com/bitcoin/bitcoin/) at the 2019 [Chaincode
Labs Summer Residency](https://residency.chaincode.com/) seminar. These
functions are used to write and read the `mempool.dat` file.

[Slides (Google Slides)](https://docs.google.com/presentation/d/1F-kILuxeK-
huIOSCyJ2D7PQCr_os_y2cIJSSvDAk35U)

Enable JavaScript to view comments. Comments are privacy friendly and self-
hosted with [isso](https://posativ.org/isso/).

All text and images in this work are licensed under a [Creative Commons
Attribution-ShareAlike 4.0 International
License](http://creativecommons.org/licenses/by-sa/4.0/) [![Creative Commons
License](https://i.creativecommons.org/l/by-
sa/4.0/80x15.png)](http://creativecommons.org/licenses/by-sa/4.0/)

#### Next

![Image for mempool.observer \(2019 version\)](/data/projects/mempool-
observer/header.png) [](/projects/mempool-observer-2019-version/)

* * *

June 1, 2019

#### mempool.observer (2019 version)

The [mempool.observer](https://mempool.observer) website displays
visualizations about my Bitcoin mempool. For example, a visualization of my
current mempool and the historical mempool of my node is shown. The idea is to
provide information about the current mempool state to a Bitcoin user with a
seemingly stuck and longtime-unconfirmed transaction. Additionally, the site
can be used for double-checking feerate estimates before sending a
transaction.

[](/projects/mempool-observer-2019-version/)

#### Previous

![Image for c-lightning plugin:
csvexportpays](https://raw.githubusercontent.com/0xB10C/c-lightning-plugin-
csvexportpays/6461045b3dc1fe371b19045e4647eeb6c9e0ebaf/screenshot.png)
[](/projects/c-lightning-plugin-csvexportpays/)

* * *

March 2, 2019

#### c-lightning plugin: csvexportpays

A toy plugin for c-lightning to export all payments made with a c-lightning
node to a `.csv` file. I build this a few days after Blockstream released the
plugin support in c-lightning v0.7 to showcase how simple it is to build
plugins.

[](/projects/c-lightning-plugin-csvexportpays/)

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

