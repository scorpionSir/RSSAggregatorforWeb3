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
0.14.3

# Bitcoin Core version 0.14.3 released

28 September 2018

ALL TOPICS

  * Compatibility
  * Notable changes
  * Known Bugs
  * 0.14.3 Change log \- {:.} Consensus \- {:.} RPC and other APIs \- {:.} P2P protocol and network code \- {:.} Build system \- {:.} Miscellaneous \- {:.} GUI \- {:.} Wallet
  * Credits

Bitcoin Core version _0.14.3_ is now available from:

<https://bitcoin.org/bin/bitcoin-core-0.14.3/>

This is a new minor version release, including various bugfixes and
performance improvements.

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

Denial-of-Service vulnerability CVE-2018-17144 ——————————-

A denial-of-service vulnerability exploitable by miners has been discovered in
Bitcoin Core versions 0.14.0 up to 0.16.2. It is recommended to upgrade any of
the vulnerable versions to 0.14.3, 0.15.2 or 0.16.3 as soon as possible.

# Known Bugs

Since 0.14.0 the approximate transaction fee shown in Bitcoin-Qt when using
coin control and smart fee estimation does not reflect any change in target
from the smart fee slider. It will only present an approximate fee calculated
using the default target. The fee calculated using the correct target is still
applied to the transaction and shown in the final send confirmation dialog.

# 0.14.3 Change log

Detailed release notes follow. This overview includes changes that affect
behavior, not code moves, refactors and string updates. For convenience in
locating the code changes and accompanying discussion, both the pull request
and git merge commit are mentioned.

### Consensus

  * [#14247](https://github.com/bitcoin/bitcoin/pull/14247) [`52965fb`](https://github.com/bitcoin/bitcoin/commit/52965fb) Fix crash bug with duplicate inputs within a transaction (TheBlueMatt, sdaftuar)

### RPC and other APIs

  * [#10445](https://github.com/bitcoin/bitcoin/pull/10445) [`87a21d5`](https://github.com/bitcoin/bitcoin/commit/87a21d5) Fix: make CCoinsViewDbCursor::Seek work for missing keys (Pieter Wuille, Gregory Maxwell)
  * [#9853](https://github.com/bitcoin/bitcoin/pull/9853) Return correct error codes in setban(), fundrawtransaction(), removeprunedfunds(), bumpfee(), blockchain.cpp (John Newbery)

### P2P protocol and network code

  * [#10234](https://github.com/bitcoin/bitcoin/pull/10234) [`d289b56`](https://github.com/bitcoin/bitcoin/commit/d289b56) [net] listbanned RPC and QT should show correct banned subnets (John Newbery)

### Build system

### Miscellaneous

  * [#10451](https://github.com/bitcoin/bitcoin/pull/10451) [`3612219`](https://github.com/bitcoin/bitcoin/commit/3612219) contrib/init/bitcoind.openrcconf: Don’t disable wallet by default (Luke Dashjr)
  * [#10250](https://github.com/bitcoin/bitcoin/pull/10250) [`e23cef0`](https://github.com/bitcoin/bitcoin/commit/e23cef0) Fix some empty vector references (Pieter Wuille)
  * [#10196](https://github.com/bitcoin/bitcoin/pull/10196) [`d28d583`](https://github.com/bitcoin/bitcoin/commit/d28d583) PrioritiseTransaction updates the mempool tx counter (Suhas Daftuar)
  * [#9497](https://github.com/bitcoin/bitcoin/pull/9497) [`e207342`](https://github.com/bitcoin/bitcoin/commit/e207342) Fix CCheckQueue IsIdle (potential) race condition and remove dangerous constructors. (Jeremy Rubin)

### GUI

  * [#9481](https://github.com/bitcoin/bitcoin/pull/9481) [`7abe7bb`](https://github.com/bitcoin/bitcoin/commit/7abe7bb) Give fallback fee a reasonable indent (Luke Dashjr)
  * [#9481](https://github.com/bitcoin/bitcoin/pull/9481) [`3e4d7bf`](https://github.com/bitcoin/bitcoin/commit/3e4d7bf) Qt/Send: Figure a decent warning colour from theme (Luke Dashjr)
  * [#9481](https://github.com/bitcoin/bitcoin/pull/9481) [`e207342`](https://github.com/bitcoin/bitcoin/commit/e207342) Show more significant warning if we fall back to the default fee (Jonas Schnelli)

### Wallet

  * [#10308](https://github.com/bitcoin/bitcoin/pull/10308) [`28b8b8b`](https://github.com/bitcoin/bitcoin/commit/28b8b8b) Securely erase potentially sensitive keys/values (tjps)
  * [#10265](https://github.com/bitcoin/bitcoin/pull/10265) [`ff13f59`](https://github.com/bitcoin/bitcoin/commit/ff13f59) Make sure pindex is non-null before possibly referencing in LogPrintf call. (Karl-Johan Alm)

# Credits

Thanks to everyone who directly contributed to this release:

  * Cory Fields
  * CryptAxe
  * fanquake
  * Jeremy Rubin
  * John Newbery
  * Jonas Schnelli
  * Gregory Maxwell
  * Karl-Johan Alm
  * Luke Dashjr
  * MarcoFalke
  * Matt Corallo
  * Mikerah
  * Pieter Wuille
  * practicalswift
  * Suhas Daftuar
  * Thomas Snider
  * Tjps
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

