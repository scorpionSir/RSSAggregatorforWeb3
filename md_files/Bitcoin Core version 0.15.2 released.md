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
0.15.2

# Bitcoin Core version 0.15.2 released

28 September 2018

ALL TOPICS

  * How to Upgrade
    * Downgrading warning
  * Compatibility
  * Notable changes
    * Denial-of-Service vulnerability CVE-2018-17144
  * 0.15.2 Change log \- {:.} Build system \- {:.} Consensus \- {:.} RPC \- {:.} Wallet \- {:.} bitcoin-tx \- {:.} Tests
  * Credits

Bitcoin Core version _0.15.2_ is now available from:

<https://bitcoincore.org/bin/bitcoin-core-0.15.2/>

This is a new minor version release, including various bugfixes and
performance improvements, as well as updated translations.

Please report bugs using the issue tracker at GitHub:

<https://github.com/bitcoin/bitcoin/issues>

To receive security and update notifications, please subscribe to:

<https://bitcoincore.org/en/list/announcements/join/>

# How to Upgrade

If you are running an older version, shut it down. Wait until it has
completely shut down (which might take a few minutes for older versions), then
run the installer (on Windows) or just copy over `/Applications/Bitcoin-Qt`
(on Mac) or `bitcoind`/`bitcoin-qt` (on Linux).

The first time you run version 0.15.0 or higher, your chainstate database will
be converted to a new format, which will take anywhere from a few minutes to
half an hour, depending on the speed of your machine.

The file format of `fee_estimates.dat` changed in version 0.15.0. Hence, a
downgrade from version 0.15 or upgrade to version 0.15 will cause all fee
estimates to be discarded.

Note that the block database format also changed in version 0.8.0 and there is
no automatic upgrade code from before version 0.8 to version 0.15.0. Upgrading
directly from 0.7.x and earlier without redownloading the blockchain is not
supported. However, as usual, old wallet versions are still supported.

## Downgrading warning

The chainstate database for this release is not compatible with previous
releases, so if you run 0.15 and then decide to switch back to any older
version, you will need to run the old release with the `-reindex-chainstate`
option to rebuild the chainstate data structures in the old format.

If your node has pruning enabled, this will entail re-downloading and
processing the entire blockchain.

# Compatibility

Bitcoin Core is extensively tested on multiple operating systems using the
Linux kernel, macOS 10.8+, and Windows Vista and later. Windows XP is not
supported.

Bitcoin Core should also work on most other Unix-like systems but is not
frequently tested on them.

# Notable changes

## Denial-of-Service vulnerability CVE-2018-17144

A denial-of-service vulnerability exploitable by miners has been discovered in
Bitcoin Core versions 0.14.0 up to 0.16.2. It is recommended to upgrade any of
the vulnerable versions to 0.15.2 or 0.16.3 as soon as possible.

# 0.15.2 Change log

### Build system

  * [#11995](https://github.com/bitcoin/bitcoin/pull/11995) [`9bb1a16`](https://github.com/bitcoin/bitcoin/commit/9bb1a16) depends: Fix Qt build with XCode 9.2(fanquake)
  * [#12946](https://github.com/bitcoin/bitcoin/pull/12946) [`93b9a61`](https://github.com/bitcoin/bitcoin/commit/93b9a61) depends: Fix Qt build with XCode 9.3(fanquake)
  * [#13544](https://github.com/bitcoin/bitcoin/pull/13544) [`9fd3e00`](https://github.com/bitcoin/bitcoin/commit/9fd3e00) depends: Update Qt download url (fanquake)
  * [#11847](https://github.com/bitcoin/bitcoin/pull/11847) [`cb7ef31`](https://github.com/bitcoin/bitcoin/commit/cb7ef31) Make boost::multi_index comparators const (sdaftuar)

### Consensus

  * [#14247](https://github.com/bitcoin/bitcoin/pull/14247) [`4b8a3f5`](https://github.com/bitcoin/bitcoin/commit/4b8a3f5) Fix crash bug with duplicate inputs within a transaction (TheBlueMatt, sdaftuar)

### RPC

  * [#11676](https://github.com/bitcoin/bitcoin/pull/11676) [`7af2457`](https://github.com/bitcoin/bitcoin/commit/7af2457) contrib/init: Update openrc-run filename (Luke Dashjr)
  * [#11277](https://github.com/bitcoin/bitcoin/pull/11277) [`7026845`](https://github.com/bitcoin/bitcoin/commit/7026845) Fix uninitialized URI in batch RPC requests (Russell Yanofsky)

### Wallet

  * [#11289](https://github.com/bitcoin/bitcoin/pull/11289) [`3f1db56`](https://github.com/bitcoin/bitcoin/commit/3f1db56) Wrap dumpwallet warning and note scripts aren’t dumped (MeshCollider)
  * [#11289](https://github.com/bitcoin/bitcoin/pull/11289) [`42ea47d`](https://github.com/bitcoin/bitcoin/commit/42ea47d) Add wallet backup text to import _, add_ and dumpwallet RPCs (MeshCollider)
  * [#11590](https://github.com/bitcoin/bitcoin/pull/11590) [`6372a75`](https://github.com/bitcoin/bitcoin/commit/6372a75) [Wallet] always show help-line of wallet encryption calls (Jonas Schnelli)

### bitcoin-tx

  * [#11554](https://github.com/bitcoin/bitcoin/pull/11554) [`a69cc07`](https://github.com/bitcoin/bitcoin/commit/a69cc07) Sanity-check script sizes in bitcoin-tx (TheBlueMatt)

### Tests

  * [#11277](https://github.com/bitcoin/bitcoin/pull/11277) [`3a6cdd4`](https://github.com/bitcoin/bitcoin/commit/3a6cdd4) Add test for multiwallet batch RPC calls (Russell Yanofsky)
  * [#11647](https://github.com/bitcoin/bitcoin/pull/11647) [`1c8c7f8`](https://github.com/bitcoin/bitcoin/commit/1c8c7f8) Add missing batch rpc calls to python coverage logs (Russell Yanofsky)
  * [#11277](https://github.com/bitcoin/bitcoin/pull/11277) [`1036c43`](https://github.com/bitcoin/bitcoin/commit/1036c43) Add missing multiwallet rpc calls to python coverage logs (Russell Yanofsky)
  * [#11277](https://github.com/bitcoin/bitcoin/pull/11277) [`305f768`](https://github.com/bitcoin/bitcoin/commit/305f768) Limit AuthServiceProxyWrapper.__getattr__ wrapping (Russell Yanofsky)
  * [#11277](https://github.com/bitcoin/bitcoin/pull/11277) [`2eea279`](https://github.com/bitcoin/bitcoin/commit/2eea279) Make AuthServiceProxy._batch method usable (Russell Yanofsky)

# Credits

Thanks to everyone who directly contributed to this release:

  * fanquake
  * Jonas Schnelli
  * Luke Dashjr
  * Matt Corallo
  * MeshCollider
  * Russell Yanofsky
  * Suhas Daftuar
  * Wladimir J. van der Laan

And to those that reported security issues:

  * awemany (for CVE-2018-17144, previously credited as “anonymous reporter”)

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

