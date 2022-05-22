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
0.20.1

# Bitcoin Core version 0.20.1 released

1 August 2020

ALL TOPICS

  * 0.20.1 Release Notes
  * How to Upgrade
  * Compatibility
  * Known Bugs
  * Notable changes
    * Changes regarding misbehaving peers
    * Notification changes
    * PSBT changes
  * 0.20.1 change log \- {:.} Mining \- {:.} P2P protocol and network code \- {:.} Wallet \- {:.} RPC and other APIs \- {:.} GUI \- {:.} Build system \- {:.} Tests and QA \- {:.} Miscellaneous
  * Credits

# 0.20.1 Release Notes

Bitcoin Core version 0.20.1 is now available from:

<https://bitcoincore.org/bin/bitcoin-core-0.20.1/>

This minor release includes various bug fixes and performance improvements, as
well as updated translations.

Please report bugs using the issue tracker at GitHub:

<https://github.com/bitcoin/bitcoin/issues>

To receive security and update notifications, please subscribe to:

<https://bitcoincore.org/en/list/announcements/join/>

# How to Upgrade

If you are running an older version, shut it down. Wait until it has
completely shut down (which might take a few minutes in some cases), then run
the installer (on Windows) or just copy over `/Applications/Bitcoin-Qt` (on
Mac) or `bitcoind`/`bitcoin-qt` (on Linux).

Upgrading directly from a version of Bitcoin Core that has reached its EOL is
possible, but it might take some time if the data directory needs to be
migrated. Old wallet versions of Bitcoin Core are generally supported.

# Compatibility

Bitcoin Core is supported and extensively tested on operating systems using
the Linux kernel, macOS 10.12+, and Windows 7 and newer. Bitcoin Core should
also work on most other Unix-like systems but is not as frequently tested on
them. It is not recommended to use Bitcoin Core on unsupported systems.

From Bitcoin Core 0.20.0 onwards, macOS versions earlier than 10.12 are no
longer supported. Additionally, Bitcoin Core does not yet change appearance
when macOS “dark mode” is activated.

# Known Bugs

The process for generating the source code release (“tarball”) has changed in
an effort to make it more complete, however, there are a few regressions in
this release:

  * The generated `configure` script is currently missing, and you will need to install autotools and run `./autogen.sh` before you can run `./configure`. This is the same as when checking out from git.

  * Instead of running `make` simply, you should instead run `BITCOIN_GENBUILD_NO_GIT=1 make`.

# Notable changes

## Changes regarding misbehaving peers

Peers that misbehave (e.g. send us invalid blocks) are now referred to as
discouraged nodes in log output, as they’re not (and weren’t) strictly banned:
incoming connections are still allowed from them, but they’re preferred for
eviction.

Furthermore, a few additional changes are introduced to how discouraged
addresses are treated:

  * Discouraging an address does not time out automatically after 24 hours (or the `-bantime` setting). Depending on traffic from other peers, discouragement may time out at an indeterminate time.

  * Discouragement is not persisted over restarts.

  * There is no method to list discouraged addresses. They are not returned by the `listbanned` RPC. That RPC also no longer reports the `ban_reason` field, as `"manually added"` is the only remaining option.

  * Discouragement cannot be removed with the `setban remove` RPC command. If you need to remove a discouragement, you can remove all discouragements by stop-starting your node.

## Notification changes

`-walletnotify` notifications are now sent for wallet transactions that are
removed from the mempool because they conflict with a new block. These
notifications were sent previously before the v0.19 release, but had been
broken since that release (bug
[#18325](https://github.com/bitcoin/bitcoin/pull/18325))

## PSBT changes

PSBTs will contain both the non-witness utxo and the witness utxo for segwit
inputs in order to restore compatibility with wallet software that are now
requiring the full previous transaction for segwit inputs. The witness utxo is
still provided to maintain compatibility with software which relied on its
existence to determine whether an input was segwit.

# 0.20.1 change log

### Mining

  * [#19019](https://github.com/bitcoin/bitcoin/pull/19019) Fix GBT: Restore “!segwit” and “csv” to “rules” key (luke-jr)

### P2P protocol and network code

  * [#19219](https://github.com/bitcoin/bitcoin/pull/19219) Replace automatic bans with discouragement filter (sipa)

### Wallet

  * [#19300](https://github.com/bitcoin/bitcoin/pull/19300) Handle concurrent wallet loading (promag)
  * [#18982](https://github.com/bitcoin/bitcoin/pull/18982) Minimal fix to restore conflicted transaction notifications (ryanofsky)

### RPC and other APIs

  * [#19524](https://github.com/bitcoin/bitcoin/pull/19524) Increment input value sum only once per UTXO in decodepsbt (fanquake)
  * [#19517](https://github.com/bitcoin/bitcoin/pull/19517) psbt: Increment input value sum only once per UTXO in decodepsbt (achow101)
  * [#19215](https://github.com/bitcoin/bitcoin/pull/19215) psbt: Include and allow both non_witness_utxo and witness_utxo for segwit inputs (achow101)

### GUI

  * [#19097](https://github.com/bitcoin/bitcoin/pull/19097) Add missing QPainterPath include (achow101)
  * [#19059](https://github.com/bitcoin/bitcoin/pull/19059) update Qt base translations for macOS release (fanquake)

### Build system

  * [#19152](https://github.com/bitcoin/bitcoin/pull/19152) improve build OS configure output (skmcontrib)
  * [#19536](https://github.com/bitcoin/bitcoin/pull/19536) qt, build: Fix QFileDialog for static builds (hebasto)

### Tests and QA

  * [#19444](https://github.com/bitcoin/bitcoin/pull/19444) Remove cached directories and associated script blocks from appveyor config (sipsorcery)
  * [#18640](https://github.com/bitcoin/bitcoin/pull/18640) appveyor: Remove clcache (MarcoFalke)

### Miscellaneous

  * [#19194](https://github.com/bitcoin/bitcoin/pull/19194) util: Don’t reference errno when pthread fails (miztake)
  * [#18700](https://github.com/bitcoin/bitcoin/pull/18700) Fix locking on WSL using flock instead of fcntl (meshcollider)

# Credits

Thanks to everyone who directly contributed to this release:

  * Aaron Clauson
  * Andrew Chow
  * fanquake
  * Hennadii Stepanov
  * João Barbosa
  * Luke Dashjr
  * MarcoFalke
  * MIZUTA Takeshi
  * Pieter Wuille
  * Russell Yanofsky
  * sachinkm77
  * Samuel Dobson
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

