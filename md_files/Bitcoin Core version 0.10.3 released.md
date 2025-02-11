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
0.10.3

# Bitcoin Core version 0.10.3 released

14 October 2015

ALL TOPICS

  * Upgrading and downgrading
    * How to Upgrade
    * Downgrade warning
  * Notable changes
    * Fix buffer overflow in bundled upnp
    * Test for LowS signatures before relaying
    * Minimum relay fee default increase
  * 0.10.3 Change log
  * Credits

Bitcoin Core version 0.10.3 is now available from:

<https://bitcoin.org/bin/bitcoin-core-0.10.3/>

This is a new minor version release, bringing security fixes and translation
updates. It is recommended to upgrade to this version as soon as possible.

Please report bugs using the issue tracker at github:

<https://github.com/bitcoin/bitcoin/issues>

# Upgrading and downgrading

## How to Upgrade

If you are running an older version, shut it down. Wait until it has
completely shut down (which might take a few minutes for older versions), then
run the installer (on Windows) or just copy over /Applications/Bitcoin-Qt (on
Mac) or bitcoind/bitcoin-qt (on Linux).

## Downgrade warning

Because release 0.10.0 and later makes use of headers-first synchronization
and parallel block download (see further), the block files and databases are
not backwards-compatible with pre-0.10 versions of Bitcoin Core or other
software:

  * Blocks will be stored on disk out of order (in the order they are received, really), which makes it incompatible with some tools or other programs. Reindexing using earlier versions will also not work anymore as a result of this.

  * The block index database will now hold headers for which no block is stored on disk, which earlier versions won’t support.

If you want to be able to downgrade smoothly, make a backup of your entire
data directory. Without this your node will need start syncing (or importing
from bootstrap.dat) anew afterwards. It is possible that the data from a
completely synchronised 0.10 node may be usable in older versions as-is, but
this is not supported and may break as soon as the older version attempts to
reindex.

This does not affect wallet forward or backward compatibility.

# Notable changes

## Fix buffer overflow in bundled upnp

Bundled miniupnpc was updated to 1.9.20151008. This fixes a buffer overflow in
the XML parser during initial network discovery.

Details can be found here: <http://talosintel.com/reports/TALOS-2015-0035/>

This applies to the distributed executables only, not when building from
source or using distribution provided packages.

Additionally, upnp has been disabled by default. This may result in a lower
number of reachable nodes on IPv4, however this prevents future libupnpc
vulnerabilities from being a structural risk to the network (see
<https://github.com/bitcoin/bitcoin/pull/6795>).

## Test for LowS signatures before relaying

Make the node require the canonical ‘low-s’ encoding for ECDSA signatures when
relaying or mining. This removes a nuisance malleability vector.

Consensus behavior is unchanged.

If widely deployed this change would eliminate the last remaining known vector
for nuisance malleability on SIGHASH_ALL P2PKH transactions. On the down-side
it will block most transactions made by sufficiently out of date software.

Unlike the other avenues to change txids on transactions this one was randomly
violated by all deployed bitcoin software prior to its discovery. So, while
other malleability vectors where made non-standard as soon as they were
discovered, this one has remained permitted. Even BIP62 did not propose
applying this rule to old version transactions, but conforming implementations
have become much more common since BIP62 was initially written.

Bitcoin Core has produced compatible signatures since a28fb70e in September
2013, but this didn’t make it into a release until 0.9 in March 2014; Bitcoinj
has done so for a similar span of time. Bitcoinjs and electrum have been more
recently updated.

This does not replace the need for BIP62 or similar, as miners can still
cooperate to break transactions. Nor does it replace the need for wallet
software to handle malleability sanely[1]. This only eliminates the cheap and
irritating DOS attack.

[1] On the Malleability of Bitcoin Transactions Marcin Andrychowicz, Stefan
Dziembowski, Daniel Malinowski, Łukasz Mazurek
<http://fc15.ifca.ai/preproceedings/bitcoin/paper_9.pdf>

## Minimum relay fee default increase

The default for the `-minrelaytxfee` setting has been increased from `0.00001`
to `0.00005`.

This is necessitated by the current transaction flooding, causing outrageous
memory usage on nodes due to the mempool ballooning. This is a temporary
measure, bridging the time until a dynamic method for determining this fee is
merged (which will be in 0.12).

(see <https://github.com/bitcoin/bitcoin/pull/6793>, as well as the 0.11.0
release notes, in which this value was suggested)

# 0.10.3 Change log

Detailed release notes follow. This overview includes changes that affect
external behavior, not code moves, refactors or string updates.

  * [#6186](https://github.com/bitcoin/bitcoin/pull/6186) [`e4a7d51`](https://github.com/bitcoin/bitcoin/commit/e4a7d51) Fix two problems in CSubnet parsing
  * [#6153](https://github.com/bitcoin/bitcoin/pull/6153) [`ebd7d8d`](https://github.com/bitcoin/bitcoin/commit/ebd7d8d) Parameter interaction: disable upnp if -proxy set
  * [#6203](https://github.com/bitcoin/bitcoin/pull/6203) [`ecc96f5`](https://github.com/bitcoin/bitcoin/commit/ecc96f5) Remove P2SH coinbase flag, no longer interesting
  * [#6226](https://github.com/bitcoin/bitcoin/pull/6226) [`181771b`](https://github.com/bitcoin/bitcoin/commit/181771b) json: fail read_string if string contains trailing garbage
  * [#6244](https://github.com/bitcoin/bitcoin/pull/6244) [`09334e0`](https://github.com/bitcoin/bitcoin/commit/09334e0) configure: Detect (and reject) LibreSSL
  * [#6276](https://github.com/bitcoin/bitcoin/pull/6276) [`0fd8464`](https://github.com/bitcoin/bitcoin/commit/0fd8464) Fix getbalance * 0
  * [#6274](https://github.com/bitcoin/bitcoin/pull/6274) [`be64204`](https://github.com/bitcoin/bitcoin/commit/be64204) Add option `-alerts` to opt out of alert system
  * [#6319](https://github.com/bitcoin/bitcoin/pull/6319) [`3f55638`](https://github.com/bitcoin/bitcoin/commit/3f55638) doc: update mailing list address
  * [#6438](https://github.com/bitcoin/bitcoin/pull/6438) [`7e66e9c`](https://github.com/bitcoin/bitcoin/commit/7e66e9c) openssl: avoid config file load/race
  * [#6439](https://github.com/bitcoin/bitcoin/pull/6439) [`255eced`](https://github.com/bitcoin/bitcoin/commit/255eced) Updated URL location of netinstall for Debian
  * [#6412](https://github.com/bitcoin/bitcoin/pull/6412) [`0739e6e`](https://github.com/bitcoin/bitcoin/commit/0739e6e) Test whether created sockets are select()able
  * [#6694](https://github.com/bitcoin/bitcoin/pull/6694) [`f696ea1`](https://github.com/bitcoin/bitcoin/commit/f696ea1) [QT] fix thin space word wrap line brake issue
  * [#6704](https://github.com/bitcoin/bitcoin/pull/6704) [`743cc9e`](https://github.com/bitcoin/bitcoin/commit/743cc9e) Backport bugfixes to 0.10
  * [#6769](https://github.com/bitcoin/bitcoin/pull/6769) [`1cea6b0`](https://github.com/bitcoin/bitcoin/commit/1cea6b0) Test LowS in standardness, removes nuisance malleability vector.
  * [#6789](https://github.com/bitcoin/bitcoin/pull/6789) [`093d7b5`](https://github.com/bitcoin/bitcoin/commit/093d7b5) Update miniupnpc to 1.9.20151008
  * [#6795](https://github.com/bitcoin/bitcoin/pull/6795) [`f2778e0`](https://github.com/bitcoin/bitcoin/commit/f2778e0) net: Disable upnp by default
  * [#6797](https://github.com/bitcoin/bitcoin/pull/6797) [`91ef4d9`](https://github.com/bitcoin/bitcoin/commit/91ef4d9) Do not store more than 200 timedata samples
  * [#6793](https://github.com/bitcoin/bitcoin/pull/6793) [`842c48d`](https://github.com/bitcoin/bitcoin/commit/842c48d) Bump minrelaytxfee default

# Credits

Thanks to everyone who directly contributed to this release:

  * Adam Weiss
  * Alex Morcos
  * Casey Rodarmor
  * Cory Fields
  * fanquake
  * Gregory Maxwell
  * Jonas Schnelli
  * J Ross Nicoll
  * Luke Dashjr
  * Pavel Vasin
  * Pieter Wuille
  * randy-waterhouse
  * ฿tcDrak
  * Tom Harding
  * Veres Lajos
  * Wladimir J. van der Laan

And all those who contributed additional code review and/or security research:

  * timothy on IRC for reporting the issue
  * Vulnerability in miniupnp discovered by Aleksandar Nikolic of Cisco Talos

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

