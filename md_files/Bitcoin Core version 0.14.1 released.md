![Close](/img/icons/ico_close.svg?1652976465)

Bitcoin.org is a community funded project, donations are appreciated and used
to improve the website.

Make a donation

Bitcoin.org needs your support!

×

Donate to Bitcoin.org

Use this QR code or address below

[ 3E8ociqZa9mZUSwGdSmAEMAoAxBK3FNDcd
](bitcoin:3E8ociqZa9mZUSwGdSmAEMAoAxBK3FNDcd)

$5.00

(... BTC)

$25.00

(... BTC)

$50.00

(... BTC)

[![Bitcoin](/img/bitcoin-core/bitcoin-core.svg?1652976465)](/en/bitcoin-core/)

  * Features
    * [Overview](/en/bitcoin-core/features/)
    * [Validation](/en/bitcoin-core/features/validation)
    * [Privacy](/en/bitcoin-core/features/privacy)
    * [Requirements](/en/bitcoin-core/features/requirements)
    * [User Interface](/en/bitcoin-core/features/user-interface)
    * [Network Support](/en/bitcoin-core/features/network-support)
  * [Get Help](/en/bitcoin-core/help)
  * Contribute
    * [Bug reports](/en/bitcoin-core/contribute/issues)
    * [Code](/en/development)
    * [Documentation](/en/bitcoin-core/contribute/documentation)
    * [Translations](/en/bitcoin-core/contribute/translations)
    * [Tech Support](/en/bitcoin-core/contribute/support)
  * [News](/en/version-history)
  * [Download](/en/download)

  * English
    *       * [Bahasa Indonesia](/id/)
      * [Català](/ca/)
      * [Dansk](/da/)
      * [Deutsch](/de/)
      * [English](/en/)
      * [Español](/es/)
      * [Français](/fr/)
      * [Italiano](/it/)
      * [Magyar](/hu/)
      * [Nederlands](/nl/)
      * [Polski](/pl/)
      * [Português Brasil](/pt_BR/)
      * [Română](/ro/)
      * [Slovenščina](/sl/)
      * [Srpski](/sr/)
    *       * [Svenska](/sv/)
      * [Türkçe](/tr/)
      * [Ελληνικά](/el/)
      * [български](/bg/)
      * [Русский](/ru/)
      * [Українська](/uk/)
      * [العربية](/ar/)
      * [فارسی](/fa/)
      * [עברית](/he/)
      * [हिन्दी](/hi/)
      * [한국어](/ko/)
      * [日本語](/ja/)
      * [简体中文](/zh_CN/)
      * [繁體中文](/zh_TW/)

Bahasa Indonesia Català Dansk Deutsch English Español Français Italiano Magyar
Nederlands Polski Português Brasil Română Slovenščina Srpski Svenska Türkçe
Ελληνικά български Русский Українська العربية فارسی עברית हिन्दी 한국어 日本語 简体中文
繁體中文 Language: en

[Bitcoin](/en/) > [Core](/en/bitcoin-core/) > [News](/en/version-history) >
0.14.1

# Bitcoin Core version 0.14.1 released

22 April 2017

ALL TOPICS

  * Compatibility
  * Notable changes
    * RPC changes
    * Mining
    * UTXO memory accounting
  * 0.14.1 Change log \- {:.} RPC and other APIs \- {:.} Block and transaction handling \- {:.} P2P protocol and network code \- {:.} Build system \- {:.} GUI \- {:.} Mining \- {:.} Tests and QA \- {:.} Miscellaneous
  * Credits

Bitcoin Core version 0.14.1 is _not available for security reasons_ :

~~https://bitcoin.org/bin/bitcoin-core-0.14.1/~~

This is a new minor version release, including various bugfixes and
performance improvements, as well as updated translations.

Please report bugs using the issue tracker at github:

<https://github.com/bitcoin/bitcoin/issues>

To receive security and update notifications, please subscribe to:

<https://bitcoincore.org/en/list/announcements/join/>

# Compatibility

Bitcoin Core is extensively tested on multiple operating systems using the
Linux kernel, macOS 10.8+, and Windows Vista and later.

Microsoft ended support for Windows XP on [April 8th,
2014](https://www.microsoft.com/en-us/WindowsForBusiness/end-of-xp-support),
No attempt is made to prevent installing or running the software on Windows
XP, you can still do so at your own risk but be aware that there are known
instabilities and issues. Please do not report issues about Windows XP to the
issue tracker.

Bitcoin Core should also work on most other Unix-like systems but is not
frequently tested on them.

# Notable changes

## RPC changes

  * The first positional argument of `createrawtransaction` was renamed from `transactions` to `inputs`.

  * The argument of `disconnectnode` was renamed from `node` to `address`.

These interface changes break compatibility with 0.14.0, when the named
arguments functionality, introduced in 0.14.0, is used. Client software using
these calls with named arguments needs to be updated.

## Mining

In previous versions, getblocktemplate required segwit support from downstream
clients/miners once the feature activated on the network. In this version, it
now supports non-segwit clients even after activation, by removing all segwit
transactions from the returned block template. This allows non-segwit miners
to continue functioning correctly even after segwit has activated.

Due to the limitations in previous versions, getblocktemplate also recommended
non-segwit clients to not signal for the segwit version-bit. Since this is no
longer an issue, getblocktemplate now always recommends signalling segwit for
all miners. This is safe because ability to enforce the rule is the only
required criteria for safe activation, not actually producing segwit-enabled
blocks.

## UTXO memory accounting

Memory usage for the UTXO cache is being calculated more accurately, so that
the configured limit (`-dbcache`) will be respected when memory usage peaks
during cache flushes. The memory accounting in prior releases is estimated to
only account for half the actual peak utilization.

The default `-dbcache` has also been changed in this release to 450MiB. Users
who currently set `-dbcache` to a high value (e.g. to keep the UTXO more fully
cached in memory) should consider increasing this setting in order to achieve
the same cache performance as prior releases. Users on low-memory systems
(such as systems with 1GB or less) should consider specifying a lower value
for this parameter.

Additional information relating to running on low-memory systems can be found
here: [reducing-bitcoind-memory-
usage.md](https://gist.github.com/laanwj/efe29c7661ce9b6620a7).

# 0.14.1 Change log

Detailed release notes follow. This overview includes changes that affect
behavior, not code moves, refactors and string updates. For convenience in
locating the code changes and accompanying discussion, both the pull request
and git merge commit are mentioned.

### RPC and other APIs

  * [#10084](https://github.com/bitcoin/bitcoin/pull/10084) [`142fbb2`](https://github.com/bitcoin/bitcoin/commit/142fbb2) Rename first named arg of createrawtransaction (MarcoFalke)
  * [#10139](https://github.com/bitcoin/bitcoin/pull/10139) [`f15268d`](https://github.com/bitcoin/bitcoin/commit/f15268d) Remove auth cookie on shutdown (practicalswift)
  * [#10146](https://github.com/bitcoin/bitcoin/pull/10146) [`2fea10a`](https://github.com/bitcoin/bitcoin/commit/2fea10a) Better error handling for submitblock (rawodb, gmaxwell)
  * [#10144](https://github.com/bitcoin/bitcoin/pull/10144) [`d947afc`](https://github.com/bitcoin/bitcoin/commit/d947afc) Prioritisetransaction wasn’t always updating ancestor fee (sdaftuar)
  * [#10204](https://github.com/bitcoin/bitcoin/pull/10204) [`3c79602`](https://github.com/bitcoin/bitcoin/commit/3c79602) Rename disconnectnode argument (jnewbery)

### Block and transaction handling

  * [#10126](https://github.com/bitcoin/bitcoin/pull/10126) [`0b5e162`](https://github.com/bitcoin/bitcoin/commit/0b5e162) Compensate for memory peak at flush time (sipa)
  * [#9912](https://github.com/bitcoin/bitcoin/pull/9912) [`fc3d7db`](https://github.com/bitcoin/bitcoin/commit/fc3d7db) Optimize GetWitnessHash() for non-segwit transactions (sdaftuar)
  * [#10133](https://github.com/bitcoin/bitcoin/pull/10133) [`ab864d3`](https://github.com/bitcoin/bitcoin/commit/ab864d3) Clean up calculations of pcoinsTip memory usage (morcos)

### P2P protocol and network code

  * [#9953](https://github.com/bitcoin/bitcoin/pull/9953)/[#10013](https://github.com/bitcoin/bitcoin/pull/10013) [`d2548a4`](https://github.com/bitcoin/bitcoin/commit/d2548a4) Fix shutdown hang with >= 8 -addnodes set (TheBlueMatt)
  * [#10176](https://github.com/bitcoin/bitcoin/pull/10176) [`30fa231`](https://github.com/bitcoin/bitcoin/commit/30fa231) net: gracefully handle NodeId wrapping (theuni)

### Build system

  * [#9973](https://github.com/bitcoin/bitcoin/pull/9973) [`e9611d1`](https://github.com/bitcoin/bitcoin/commit/e9611d1) depends: fix zlib build on osx (theuni)

### GUI

  * [#10060](https://github.com/bitcoin/bitcoin/pull/10060) [`ddc2dd1`](https://github.com/bitcoin/bitcoin/commit/ddc2dd1) Ensure an item exists on the rpcconsole stack before adding (achow101)

### Mining

  * [#9955](https://github.com/bitcoin/bitcoin/pull/9955)/[#10006](https://github.com/bitcoin/bitcoin/pull/10006) [`569596c`](https://github.com/bitcoin/bitcoin/commit/569596c) Don’t require segwit in getblocktemplate for segwit signalling or mining (sdaftuar)
  * [#9959](https://github.com/bitcoin/bitcoin/pull/9959)/[#10127](https://github.com/bitcoin/bitcoin/pull/10127) [`b5c3440`](https://github.com/bitcoin/bitcoin/commit/b5c3440) Prevent slowdown in CreateNewBlock on large mempools (sdaftuar)

### Tests and QA

  * [#10157](https://github.com/bitcoin/bitcoin/pull/10157) [`55f641c`](https://github.com/bitcoin/bitcoin/commit/55f641c) Fix the `mempool_packages.py` test (sdaftuar)

### Miscellaneous

  * [#10037](https://github.com/bitcoin/bitcoin/pull/10037) [`4d8e660`](https://github.com/bitcoin/bitcoin/commit/4d8e660) Trivial: Fix typo in help getrawtransaction RPC (keystrike)
  * [#10120](https://github.com/bitcoin/bitcoin/pull/10120) [`e4c9a90`](https://github.com/bitcoin/bitcoin/commit/e4c9a90) util: Work around (virtual) memory exhaustion on 32-bit w/ glibc (laanwj)
  * [#10130](https://github.com/bitcoin/bitcoin/pull/10130) [`ecc5232`](https://github.com/bitcoin/bitcoin/commit/ecc5232) bitcoin-tx input verification (awemany, jnewbery)

# Credits

Thanks to everyone who directly contributed to this release:

  * Alex Morcos
  * Andrew Chow
  * Awemany
  * Cory Fields
  * Gregory Maxwell
  * James Evans
  * John Newbery
  * MarcoFalke
  * Matt Corallo
  * Pieter Wuille
  * practicalswift
  * rawodb
  * Suhas Daftuar
  * Wladimir J. van der Laan

As well as everyone that helped translating on
[Transifex](https://www.transifex.com/projects/p/bitcoin/).

[Go back to the version history](/en/version-history)

[ ![Bitcoin](/img/icons/logo-footer.svg?1652976465) ](/en/)

Support Bitcoin.org: Donate

[3E8ociqZa9mZUSwGdSmAEMAoAxBK3FNDcd](bitcoin:3E8ociqZa9mZUSwGdSmAEMAoAxBK3FNDcd)

Introduction:

  * [Individuals](/en/bitcoin-for-individuals)
  * [Businesses](/en/bitcoin-for-businesses)
  * [Developers](https://developer.bitcoin.org/)
  * [Getting started](/en/getting-started)
  * [How it works](/en/how-it-works)
  * [You need to know](/en/you-need-to-know)
  * [White paper](/en/bitcoin-paper)

Resources:

  * [Resources](/en/resources)
  * [Exchanges](/en/exchanges)
  * [Community](/en/community)
  * [Vocabulary ](/en/vocabulary)
  * [Events](/en/events)
  * [Bitcoin Core](/en/bitcoin-core/)

Participate:

  * [Support Bitcoin](/en/support-bitcoin)
  * [Buy Bitcoin](/en/buy)
  * [Running a full node](/en/full-node)
  * [Development](/en/development)

Other:

[Avoid Scams](/en/scams) [Legal](/en/legal) [Privacy Policy](/en/privacy)
[Press](/en/press) [About bitcoin.org](/en/about-us) [Blog](/en/blog)

© Bitcoin Project 2009-2022 Released under the [MIT
license](http://opensource.org/licenses/mit-license.php)  
Bitcoin Core pages on Bitcoin.org are [maintained separately](/en/bitcoin-
core/about-site) from the rest of the site.

[Network Status](/en/alerts)

  * English
    *       * [Bahasa Indonesia](/id/)
      * [Català](/ca/)
      * [Dansk](/da/)
      * [Deutsch](/de/)
      * [English](/en/)
      * [Español](/es/)
      * [Français](/fr/)
      * [Italiano](/it/)
      * [Magyar](/hu/)
      * [Nederlands](/nl/)
      * [Polski](/pl/)
      * [Português Brasil](/pt_BR/)
      * [Română](/ro/)
      * [Slovenščina](/sl/)
      * [Srpski](/sr/)
    *       * [Svenska](/sv/)
      * [Türkçe](/tr/)
      * [Ελληνικά](/el/)
      * [български](/bg/)
      * [Русский](/ru/)
      * [Українська](/uk/)
      * [العربية](/ar/)
      * [فارسی](/fa/)
      * [עברית](/he/)
      * [हिन्दी](/hi/)
      * [한국어](/ko/)
      * [日本語](/ja/)
      * [简体中文](/zh_CN/)
      * [繁體中文](/zh_TW/)

Bahasa Indonesia Català Dansk Deutsch English Español Français Italiano Magyar
Nederlands Polski Português Brasil Română Slovenščina Srpski Svenska Türkçe
Ελληνικά български Русский Українська العربية فارسی עברית हिन्दी 한국어 日本語 简体中文
繁體中文 en

