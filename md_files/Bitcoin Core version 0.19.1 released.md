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
0.19.1

# Bitcoin Core version 0.19.1 released

9 March 2020

ALL TOPICS

  * 0.19.1 Release Notes
  * How to Upgrade
  * Compatibility
  * 0.19.1 change log \- {:.} Wallet \- {:.} RPC and other APIs \- {:.} GUI \- {:.} Tests and QA \- {:.} Platform support \- {:.} Miscellaneous
  * Credits

# 0.19.1 Release Notes

Bitcoin Core version 0.19.1 is now available from:

<https://bitcoincore.org/bin/bitcoin-core-0.19.1/>

This minor release includes various bug fixes and performance improvements, as
well as updated translations.

Please report bugs using the issue tracker at GitHub:

<https://github.com/bitcoin/bitcoin/issues>

To receive security and update notifications, please subscribe to:

<https://bitcoincore.org/en/list/announcements/join/>

# How to Upgrade

If you are running an older version, shut it down. Wait until it has
completely shut down (which might take a few minutes for older versions), then
run the installer (on Windows) or just copy over `/Applications/Bitcoin-Qt`
(on Mac) or `bitcoind`/`bitcoin-qt` (on Linux).

Upgrading directly from a version of Bitcoin Core that has reached its EOL is
possible, but it might take some time if the datadir needs to be migrated. Old
wallet versions of Bitcoin Core are generally supported.

# Compatibility

Bitcoin Core is supported and extensively tested on operating systems using
the Linux kernel, macOS 10.10+, and Windows 7 and newer. It is not recommended
to use Bitcoin Core on unsupported systems.

Bitcoin Core should also work on most other Unix-like systems but is not as
frequently tested on them.

From Bitcoin Core 0.17.0 onwards, macOS versions earlier than 10.10 are no
longer supported, as Bitcoin Core is now built using Qt 5.9.x which requires
macOS 10.10+. Additionally, Bitcoin Core does not yet change appearance when
macOS “dark mode” is activated.

In addition to previously supported CPU platforms, this release’s pre-compiled
distribution provides binaries for the RISC-V platform.

# 0.19.1 change log

### Wallet

  * [#17643](https://github.com/bitcoin/bitcoin/pull/17643) Fix origfee return for bumpfee with feerate arg (instagibbs)
  * [#16963](https://github.com/bitcoin/bitcoin/pull/16963) Fix `unique_ptr` usage in boost::signals2 (promag)
  * [#17258](https://github.com/bitcoin/bitcoin/pull/17258) Fix issue with conflicted mempool tx in listsinceblock (adamjonas, mchrostowski)
  * [#17924](https://github.com/bitcoin/bitcoin/pull/17924) Bug: IsUsedDestination shouldn’t use key id as script id for ScriptHash (instagibbs)
  * [#17621](https://github.com/bitcoin/bitcoin/pull/17621) IsUsedDestination should count any known single-key address (instagibbs)
  * [#17843](https://github.com/bitcoin/bitcoin/pull/17843) Reset reused transactions cache (fjahr)

### RPC and other APIs

  * [#17687](https://github.com/bitcoin/bitcoin/pull/17687) cli: Fix fatal leveldb error when specifying -blockfilterindex=basic twice (brakmic)
  * [#17728](https://github.com/bitcoin/bitcoin/pull/17728) require second argument only for scantxoutset start action (achow101)
  * [#17445](https://github.com/bitcoin/bitcoin/pull/17445) zmq: Fix due to invalid argument and multiple notifiers (promag)
  * [#17524](https://github.com/bitcoin/bitcoin/pull/17524) psbt: handle unspendable psbts (achow101)
  * [#17156](https://github.com/bitcoin/bitcoin/pull/17156) psbt: check that various indexes and amounts are within bounds (achow101)

### GUI

  * [#17427](https://github.com/bitcoin/bitcoin/pull/17427) Fix missing qRegisterMetaType for `size_t` (hebasto)
  * [#17695](https://github.com/bitcoin/bitcoin/pull/17695) disable File->CreateWallet during startup (fanquake)
  * [#17634](https://github.com/bitcoin/bitcoin/pull/17634) Fix comparison function signature (hebasto)
  * [#18062](https://github.com/bitcoin/bitcoin/pull/18062) Fix unintialized WalletView::progressDialog (promag)

### Tests and QA

  * [#17416](https://github.com/bitcoin/bitcoin/pull/17416) Appveyor improvement - text file for vcpkg package list (sipsorcery)
  * [#17488](https://github.com/bitcoin/bitcoin/pull/17488) fix “bitcoind already running” warnings on macOS (fanquake)
  * [#17980](https://github.com/bitcoin/bitcoin/pull/17980) add missing #include to fix compiler errors (kallewoof)

### Platform support

  * [#17736](https://github.com/bitcoin/bitcoin/pull/17736) Update msvc build for Visual Studio 2019 v16.4 (sipsorcery)
  * [#17364](https://github.com/bitcoin/bitcoin/pull/17364) Updates to appveyor config for VS2019 and Qt5.9.8 + msvc project fixes (sipsorcery)
  * [#17887](https://github.com/bitcoin/bitcoin/pull/17887) bug-fix macos: give free bytes to `F_PREALLOCATE` (kallewoof)

### Miscellaneous

  * [#17897](https://github.com/bitcoin/bitcoin/pull/17897) init: Stop indexes on shutdown after ChainStateFlushed callback (jimpo)
  * [#17450](https://github.com/bitcoin/bitcoin/pull/17450) util: Add missing headers to util/fees.cpp (hebasto)
  * [#17654](https://github.com/bitcoin/bitcoin/pull/17654) Unbreak build with Boost 1.72.0 (jbeich)
  * [#17857](https://github.com/bitcoin/bitcoin/pull/17857) scripts: Fix symbol-check & security-check argument passing (fanquake)
  * [#17762](https://github.com/bitcoin/bitcoin/pull/17762) Log to net category for exceptions in ProcessMessages (laanwj)
  * [#18100](https://github.com/bitcoin/bitcoin/pull/18100) Update univalue subtree (MarcoFalke)

# Credits

Thanks to everyone who directly contributed to this release:

  * Aaron Clauson
  * Adam Jonas
  * Andrew Chow
  * Fabian Jahr
  * fanquake
  * Gregory Sanders
  * Harris
  * Hennadii Stepanov
  * Jan Beich
  * Jim Posen
  * João Barbosa
  * Karl-Johan Alm
  * Luke Dashjr
  * MarcoFalke
  * Michael Chrostowski
  * Russell Yanofsky
  * Wladimir J. van der Laan

As well as to everyone that helped with translations on
[Transifex](https://www.transifex.com/bitcoin/bitcoin/).

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

