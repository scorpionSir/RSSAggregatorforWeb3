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
0.16.2

# Bitcoin Core version 0.16.2 released

29 July 2018

ALL TOPICS

  * How to Upgrade
    * Downgrading warning
  * Compatibility
    * 0.16.2 change log
      * Wallet
      * RPC and other APIs
      * GUI
      * Build system
      * Tests and QA
      * Miscellaneous
  * Credits

Bitcoin Core version 0.16.2 is _not available for security reasons_ :

~~https://bitcoincore.org/bin/bitcoin-core-0.16.2/~~

This is a new minor version release, with various bugfixes as well as updated
translations.

Please report bugs using the issue tracker at GitHub:

<https://github.com/bitcoin/bitcoin/issues>

To receive security and update notifications, please subscribe to:

<https://bitcoincore.org/en/list/announcements/join/>

# How to Upgrade

If you are running an older version, shut it down. Wait until it has
completely shut down (which might take a few minutes for older versions), then
run the installer (on Windows) or just copy over `/Applications/Bitcoin-Qt`
(on Mac) or `bitcoind`/`bitcoin-qt` (on Linux).

The first time you run version 0.15.0 or newer, your chainstate database will
be converted to a new format, which will take anywhere from a few minutes to
half an hour, depending on the speed of your machine.

Note that the block database format also changed in version 0.8.0 and there is
no automatic upgrade code from before version 0.8 to version 0.15.0 or higher.
Upgrading directly from 0.7.x and earlier without re-downloading the
blockchain is not supported. However, as usual, old wallet versions are still
supported.

## Downgrading warning

Wallets created in 0.16 and later are not compatible with versions prior to
0.16 and will not work if you try to use newly created wallets in older
versions. Existing wallets that were created with older versions are not
affected by this.

# Compatibility

Bitcoin Core is extensively tested on multiple operating systems using the
Linux kernel, macOS 10.8+, and Windows Vista and later. Windows XP is not
supported.

Bitcoin Core should also work on most other Unix-like systems but is not
frequently tested on them.

## 0.16.2 change log

### Wallet

  * [#13622](https://github.com/bitcoin/bitcoin/pull/13622) [`c04a4a5`](https://github.com/bitcoin/bitcoin/commit/c04a4a5) Remove mapRequest tracking that just effects Qt display. (TheBlueMatt)
  * [#12905](https://github.com/bitcoin/bitcoin/pull/12905) [`cfc6f74`](https://github.com/bitcoin/bitcoin/commit/cfc6f74) [rpcwallet] Clamp walletpassphrase value at 100M seconds (sdaftuar)
  * [#13437](https://github.com/bitcoin/bitcoin/pull/13437) [`ed82e71`](https://github.com/bitcoin/bitcoin/commit/ed82e71) wallet: Erase wtxOrderd wtx pointer on removeprunedfunds (MarcoFalke)

### RPC and other APIs

  * [#13451](https://github.com/bitcoin/bitcoin/pull/13451) [`cbd2f70`](https://github.com/bitcoin/bitcoin/commit/cbd2f70) rpc: expose CBlockIndex::nTx in getblock(header) (instagibbs)
  * [#13507](https://github.com/bitcoin/bitcoin/pull/13507) [`f7401c8`](https://github.com/bitcoin/bitcoin/commit/f7401c8) RPC: Fix parameter count check for importpubkey (kristapsk)
  * [#13452](https://github.com/bitcoin/bitcoin/pull/13452) [`6b9dc8c`](https://github.com/bitcoin/bitcoin/commit/6b9dc8c) rpc: have verifytxoutproof check the number of txns in proof structure (instagibbs)
  * [#12837](https://github.com/bitcoin/bitcoin/pull/12837) [`bf1f150`](https://github.com/bitcoin/bitcoin/commit/bf1f150) rpc: fix type mistmatch in `listreceivedbyaddress` (joemphilips)
  * [#12743](https://github.com/bitcoin/bitcoin/pull/12743) [`657dfc5`](https://github.com/bitcoin/bitcoin/commit/657dfc5) Fix csBestBlock/cvBlockChange waiting in rpc/mining (sipa)

### GUI

  * [#12432](https://github.com/bitcoin/bitcoin/pull/12432) [`f78e7f6`](https://github.com/bitcoin/bitcoin/commit/f78e7f6) [qt] send: Clear All also resets coin control options (Sjors)
  * [#12617](https://github.com/bitcoin/bitcoin/pull/12617) [`21dd512`](https://github.com/bitcoin/bitcoin/commit/21dd512) gui: Show messages as text not html (laanwj)
  * [#12793](https://github.com/bitcoin/bitcoin/pull/12793) [`cf6feb7`](https://github.com/bitcoin/bitcoin/commit/cf6feb7) qt: Avoid reseting on resetguisettigs=0 (MarcoFalke)

### Build system

  * [#13544](https://github.com/bitcoin/bitcoin/pull/13544) [`9fd3e00`](https://github.com/bitcoin/bitcoin/commit/9fd3e00) depends: Update Qt download url (fanquake)
  * [#12573](https://github.com/bitcoin/bitcoin/pull/12573) [`88d1a64`](https://github.com/bitcoin/bitcoin/commit/88d1a64) Fix compilation when compiler do not support `__builtin_clz*` (532479301)

### Tests and QA

  * [#13061](https://github.com/bitcoin/bitcoin/pull/13061) [`170b309`](https://github.com/bitcoin/bitcoin/commit/170b309) Make tests pass after 2020 (bmwiedemann)
  * [#13192](https://github.com/bitcoin/bitcoin/pull/13192) [`79c4fff`](https://github.com/bitcoin/bitcoin/commit/79c4fff) [tests] Fixed intermittent failure in `p2p_sendheaders.py` (lmanners)
  * [#13300](https://github.com/bitcoin/bitcoin/pull/13300) [`d9c5630`](https://github.com/bitcoin/bitcoin/commit/d9c5630) qa: Initialize lockstack to prevent null pointer deref (MarcoFalke)
  * [#13545](https://github.com/bitcoin/bitcoin/pull/13545) [`e15e3a9`](https://github.com/bitcoin/bitcoin/commit/e15e3a9) tests: Fix test case `streams_serializedata_xor` Remove Boost dependency. (practicalswift)
  * [#13304](https://github.com/bitcoin/bitcoin/pull/13304) [`cbdabef`](https://github.com/bitcoin/bitcoin/commit/cbdabef) qa: Fix `wallet_listreceivedby` race (MarcoFalke)

### Miscellaneous

  * [#12887](https://github.com/bitcoin/bitcoin/pull/12887) [`2291774`](https://github.com/bitcoin/bitcoin/commit/2291774) Add newlines to end of log messages (jnewbery)
  * [#12859](https://github.com/bitcoin/bitcoin/pull/12859) [`18b0c69`](https://github.com/bitcoin/bitcoin/commit/18b0c69) Bugfix: Include `<memory>` for `std::unique_ptr` (luke-jr)
  * [#13131](https://github.com/bitcoin/bitcoin/pull/13131) [`ce8aa54`](https://github.com/bitcoin/bitcoin/commit/ce8aa54) Add Windows shutdown handler (ken2812221)
  * [#13652](https://github.com/bitcoin/bitcoin/pull/13652) [`20461fc`](https://github.com/bitcoin/bitcoin/commit/20461fc) rpc: Fix that CWallet::AbandonTransaction would leave the grandchildren, etc. active (Empact)

# Credits

Thanks to everyone who directly contributed to this release:

  * 532479301
  * Ben Woosley
  * Bernhard M. Wiedemann
  * Chun Kuan Lee
  * Cory Fields
  * fanquake
  * Gregory Sanders
  * joemphilips
  * John Newbery
  * Kristaps Kaupe
  * lmanners
  * Luke Dashjr
  * MarcoFalke
  * Matt Corallo
  * Pieter Wuille
  * practicalswift
  * Sjors Provoost
  * Suhas Daftuar
  * Wladimir J. van der Laan

And to those that reported security issues:

  * Braydon Fuller
  * Himanshu Mehta

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

