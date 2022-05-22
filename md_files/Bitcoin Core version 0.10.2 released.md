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
0.10.2

# Bitcoin Core version 0.10.2 released

19 May 2015

ALL TOPICS

  * Upgrading and downgrading
    * How to Upgrade
    * Downgrade warning
  * Notable changes
  * 0.10.2 Change log
  * Credits

Bitcoin Core version 0.10.2 is now available from:

<https://bitcoin.org/bin/bitcoin-core-0.10.2/>

This is a new minor version release, bringing minor bug fixes and translation
updates. It is recommended to upgrade to this version.

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

This fixes a serious problem on Windows with data directories that have non-
ASCII characters (https://github.com/bitcoin/bitcoin/issues/6078).

For other platforms there are no notable changes.

For the notable changes in 0.10, refer to the release notes at
https://github.com/bitcoin/bitcoin/blob/v0.10.0/doc/release-notes.md

# 0.10.2 Change log

Detailed release notes follow. This overview includes changes that affect
external behavior, not code moves, refactors or string updates.

Wallet:

  * [`824c011`](https://github.com/bitcoin/bitcoin/commit/824c011) fix boost::get usage with boost 1.58

Miscellaneous:

  * [`da65606`](https://github.com/bitcoin/bitcoin/commit/da65606) Avoid crash on start in TestBlockValidity with gen=1.
  * [`424ae66`](https://github.com/bitcoin/bitcoin/commit/424ae66) don’t imbue boost::filesystem::path with locale “C” on windows (fixes [#6078](https://github.com/bitcoin/bitcoin/pull/6078))

# Credits

Thanks to everyone who directly contributed to this release:

  * Cory Fields
  * Gregory Maxwell
  * Jonas Schnelli
  * Wladimir J. van der Laan

And all those who contributed additional code review and/or security research:

  * dexX7
  * Pieter Wuille
  * vayvanne

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

