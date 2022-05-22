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
0.16.1

# Bitcoin Core version 0.16.1 released

15 June 2018

ALL TOPICS

  * How to Upgrade
    * Downgrading warning
  * Compatibility
  * Notable changes
    * Miner block size removed
    * 0.16.1 change log
      * Policy
      * Mining
      * Block and transaction handling
      * P2P protocol and network code
      * Wallet
      * GUI
      * Build system
      * Tests and QA
      * Miscellaneous
      * Documentation
  * Credits

Bitcoin Core version 0.16.1 is _not available for security reasons_ :

~~https://bitcoincore.org/bin/bitcoin-core-0.16.1/~~

This is a new major version release, including new features, various bugfixes
and performance improvements, as well as updated translations.

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

# Notable changes

## Miner block size removed

The `-blockmaxsize` option for miners to limit their blocks’ sizes was
deprecated in version 0.15.1, and has now been removed. Miners should use the
`-blockmaxweight` option if they want to limit the weight of their blocks’
weights.

## 0.16.1 change log

### Policy

  * [#11423](https://github.com/bitcoin/bitcoin/pull/11423) [`d353dd1`](https://github.com/bitcoin/bitcoin/commit/d353dd1) [Policy] Several transaction standardness rules (jl2012)

### Mining

  * [#12756](https://github.com/bitcoin/bitcoin/pull/12756) [`e802c22`](https://github.com/bitcoin/bitcoin/commit/e802c22) [config] Remove blockmaxsize option (jnewbery)

### Block and transaction handling

  * [#13199](https://github.com/bitcoin/bitcoin/pull/13199) [`c71e535`](https://github.com/bitcoin/bitcoin/commit/c71e535) Bugfix: ensure consistency of m_failed_blocks after reconsiderblock (sdaftuar)
  * [#13023](https://github.com/bitcoin/bitcoin/pull/13023) [`bb79aaf`](https://github.com/bitcoin/bitcoin/commit/bb79aaf) Fix some concurrency issues in ActivateBestChain() (skeees)

### P2P protocol and network code

  * [#12626](https://github.com/bitcoin/bitcoin/pull/12626) [`f60e84d`](https://github.com/bitcoin/bitcoin/commit/f60e84d) Limit the number of IPs addrman learns from each DNS seeder (EthanHeilman)

### Wallet

  * [#13265](https://github.com/bitcoin/bitcoin/pull/13265) [`5d8de76`](https://github.com/bitcoin/bitcoin/commit/5d8de76) Exit SyncMetaData if there are no transactions to sync (laanwj)
  * [#13030](https://github.com/bitcoin/bitcoin/pull/13030) [`5ff571e`](https://github.com/bitcoin/bitcoin/commit/5ff571e) Fix zapwallettxes/multiwallet interaction. (jnewbery)

### GUI

  * [#12999](https://github.com/bitcoin/bitcoin/pull/12999) [`1720eb3`](https://github.com/bitcoin/bitcoin/commit/1720eb3) Show the Window when double clicking the taskbar icon (ken2812221)
  * [#12650](https://github.com/bitcoin/bitcoin/pull/12650) [`f118a7a`](https://github.com/bitcoin/bitcoin/commit/f118a7a) Fix issue: “default port not shown correctly in settings dialog” (251Labs)
  * [#13251](https://github.com/bitcoin/bitcoin/pull/13251) [`ea487f9`](https://github.com/bitcoin/bitcoin/commit/ea487f9) Rephrase Bech32 checkbox texts, and enable it with legacy address default (fanquake)

### Build system

  * [#12474](https://github.com/bitcoin/bitcoin/pull/12474) [`b0f692f`](https://github.com/bitcoin/bitcoin/commit/b0f692f) Allow depends system to support armv7l (hkjn)
  * [#12585](https://github.com/bitcoin/bitcoin/pull/12585) [`72a3290`](https://github.com/bitcoin/bitcoin/commit/72a3290) depends: Switch to downloading expat from GitHub (fanquake)
  * [#12648](https://github.com/bitcoin/bitcoin/pull/12648) [`46ca8f3`](https://github.com/bitcoin/bitcoin/commit/46ca8f3) test: Update trusted git root (MarcoFalke)
  * [#11995](https://github.com/bitcoin/bitcoin/pull/11995) [`686cb86`](https://github.com/bitcoin/bitcoin/commit/686cb86) depends: Fix Qt build with Xcode 9 (fanquake)
  * [#12636](https://github.com/bitcoin/bitcoin/pull/12636) [`845838c`](https://github.com/bitcoin/bitcoin/commit/845838c) backport: [#11995](https://github.com/bitcoin/bitcoin/pull/11995) Fix Qt build with Xcode 9 (fanquake)
  * [#12946](https://github.com/bitcoin/bitcoin/pull/12946) [`e055bc0`](https://github.com/bitcoin/bitcoin/commit/e055bc0) depends: Fix Qt build with XCode 9.3 (fanquake)
  * [#12998](https://github.com/bitcoin/bitcoin/pull/12998) [`7847b92`](https://github.com/bitcoin/bitcoin/commit/7847b92) Default to defining endian-conversion DECLs in compat w/o config (TheBlueMatt)

### Tests and QA

  * [#12447](https://github.com/bitcoin/bitcoin/pull/12447) [`01f931b`](https://github.com/bitcoin/bitcoin/commit/01f931b) Add missing signal.h header (laanwj)
  * [#12545](https://github.com/bitcoin/bitcoin/pull/12545) [`1286f3e`](https://github.com/bitcoin/bitcoin/commit/1286f3e) Use wait_until to ensure ping goes out (Empact)
  * [#12804](https://github.com/bitcoin/bitcoin/pull/12804) [`4bdb0ce`](https://github.com/bitcoin/bitcoin/commit/4bdb0ce) Fix intermittent rpc_net.py failure. (jnewbery)
  * [#12553](https://github.com/bitcoin/bitcoin/pull/12553) [`0e98f96`](https://github.com/bitcoin/bitcoin/commit/0e98f96) Prefer wait_until over polling with time.sleep (Empact)
  * [#12486](https://github.com/bitcoin/bitcoin/pull/12486) [`cfebd40`](https://github.com/bitcoin/bitcoin/commit/cfebd40) Round target fee to 8 decimals in assert_fee_amount (kallewoof)
  * [#12843](https://github.com/bitcoin/bitcoin/pull/12843) [`df38b13`](https://github.com/bitcoin/bitcoin/commit/df38b13) Test starting bitcoind with -h and -version (jnewbery)
  * [#12475](https://github.com/bitcoin/bitcoin/pull/12475) [`41c29f6`](https://github.com/bitcoin/bitcoin/commit/41c29f6) Fix python TypeError in script.py (MarcoFalke)
  * [#12638](https://github.com/bitcoin/bitcoin/pull/12638) [`0a76ed2`](https://github.com/bitcoin/bitcoin/commit/0a76ed2) Cache only chain and wallet for regtest datadir (MarcoFalke)
  * [#12902](https://github.com/bitcoin/bitcoin/pull/12902) [`7460945`](https://github.com/bitcoin/bitcoin/commit/7460945) Handle potential cookie race when starting node (sdaftuar)
  * [#12904](https://github.com/bitcoin/bitcoin/pull/12904) [`6c26df0`](https://github.com/bitcoin/bitcoin/commit/6c26df0) Ensure bitcoind processes are cleaned up when tests end (sdaftuar)
  * [#13049](https://github.com/bitcoin/bitcoin/pull/13049) [`9ea62a3`](https://github.com/bitcoin/bitcoin/commit/9ea62a3) Backports (MarcoFalke)
  * [#13201](https://github.com/bitcoin/bitcoin/pull/13201) [`b8aacd6`](https://github.com/bitcoin/bitcoin/commit/b8aacd6) Handle disconnect_node race (sdaftuar)

### Miscellaneous

  * [#12518](https://github.com/bitcoin/bitcoin/pull/12518) [`a17fecf`](https://github.com/bitcoin/bitcoin/commit/a17fecf) Bump leveldb subtree (MarcoFalke)
  * [#12442](https://github.com/bitcoin/bitcoin/pull/12442) [`f3b8d85`](https://github.com/bitcoin/bitcoin/commit/f3b8d85) devtools: Exclude patches from lint-whitespace (MarcoFalke)
  * [#12988](https://github.com/bitcoin/bitcoin/pull/12988) [`acdf433`](https://github.com/bitcoin/bitcoin/commit/acdf433) Hold cs_main while calling UpdatedBlockTip() signal (skeees)
  * [#12985](https://github.com/bitcoin/bitcoin/pull/12985) [`0684cf9`](https://github.com/bitcoin/bitcoin/commit/0684cf9) Windows: Avoid launching as admin when NSIS installer ends. (JeremyRand)

### Documentation

  * [#12637](https://github.com/bitcoin/bitcoin/pull/12637) [`60086dd`](https://github.com/bitcoin/bitcoin/commit/60086dd) backport: [#12556](https://github.com/bitcoin/bitcoin/pull/12556) fix version typo in getpeerinfo RPC call help (fanquake)
  * [#13184](https://github.com/bitcoin/bitcoin/pull/13184) [`4087dd0`](https://github.com/bitcoin/bitcoin/commit/4087dd0) RPC Docs: `gettxout*`: clarify bestblock and unspent counts (harding)
  * [#13246](https://github.com/bitcoin/bitcoin/pull/13246) [`6de7543`](https://github.com/bitcoin/bitcoin/commit/6de7543) Bump to Ubuntu Bionic 18.04 in build-windows.md (ken2812221)
  * [#12556](https://github.com/bitcoin/bitcoin/pull/12556) [`e730b82`](https://github.com/bitcoin/bitcoin/commit/e730b82) Fix version typo in getpeerinfo RPC call help (tamasblummer)

# Credits

Thanks to everyone who directly contributed to this release:

  * 251
  * Ben Woosley
  * Chun Kuan Lee
  * David A. Harding
  * e0
  * fanquake
  * Henrik Jonsson
  * JeremyRand
  * Jesse Cohen
  * John Newbery
  * Johnson Lau
  * Karl-Johan Alm
  * Luke Dashjr
  * MarcoFalke
  * Matt Corallo
  * Pieter Wuille
  * Suhas Daftuar
  * Tamas Blummer
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

