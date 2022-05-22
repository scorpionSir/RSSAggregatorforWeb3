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
0.18.1

# Bitcoin Core version 0.18.1 released

9 August 2019

ALL TOPICS

  * How to Upgrade
  * Compatibility
  * Known issues
    * Wallet GUI
  * 0.18.1 change log \- {:.} P2P protocol and network code \- {:.} Wallet \- {:.} RPC and other APIs \- {:.} GUI \- {:.} Build system \- {:.} Tests and QA \- {:.} Documentation \- {:.} Miscellaneous
  * Credits

Bitcoin Core version 0.18.1 is now available from:

<https://bitcoincore.org/bin/bitcoin-core-0.18.1/>

This is a new minor version release, including new features, various bug fixes
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
no automatic upgrade code from before version 0.8 to version 0.15.0 or later.
Upgrading directly from 0.7.x and earlier without redownloading the blockchain
is not supported. However, as usual, old wallet versions are still supported.

# Compatibility

Bitcoin Core is supported and extensively tested on operating systems using
the Linux kernel, macOS 10.10+, and Windows 7 and newer. It is not recommended
to use Bitcoin Core on unsupported systems.

Bitcoin Core should also work on most other Unix-like systems but is not as
frequently tested on them.

From 0.17.0 onwards, macOS <10.10 is no longer supported. 0.17.0 is built
using Qt 5.9.x, which doesn’t support versions of macOS older than 10.10.
Additionally, Bitcoin Core does not yet change appearance when macOS “dark
mode” is activated.

# Known issues

## Wallet GUI

For advanced users who have both (1) enabled coin control features, and (2)
are using multiple wallets loaded at the same time: The coin control input
selection dialog can erroneously retain wrong-wallet state when switching
wallets using the dropdown menu. For now, it is recommended not to use coin
control features with multiple wallets loaded.

# 0.18.1 change log

### P2P protocol and network code

  * [#15990](https://github.com/bitcoin/bitcoin/pull/15990) Add tests and documentation for blocksonly (MarcoFalke)
  * [#16021](https://github.com/bitcoin/bitcoin/pull/16021) Avoid logging transaction decode errors to stderr (MarcoFalke)
  * [#16405](https://github.com/bitcoin/bitcoin/pull/16405) fix: tor: Call `event_base_loopbreak` from the event’s callback (promag)
  * [#16412](https://github.com/bitcoin/bitcoin/pull/16412) Make poll in InterruptibleRecv only filter for POLLIN events (tecnovert)

### Wallet

  * [#15913](https://github.com/bitcoin/bitcoin/pull/15913) Add -ignorepartialspends to list of ignored wallet options (luke-jr)

### RPC and other APIs

  * [#15991](https://github.com/bitcoin/bitcoin/pull/15991) Bugfix: fix pruneblockchain returned prune height (jonasschnelli)
  * [#15899](https://github.com/bitcoin/bitcoin/pull/15899) Document iswitness flag and fix bug in converttopsbt (MarcoFalke)
  * [#16026](https://github.com/bitcoin/bitcoin/pull/16026) Ensure that uncompressed public keys in a multisig always returns a legacy address (achow101)
  * [#14039](https://github.com/bitcoin/bitcoin/pull/14039) Disallow extended encoding for non-witness transactions (sipa)
  * [#16210](https://github.com/bitcoin/bitcoin/pull/16210) add 2nd arg to signrawtransactionwithkey examples (dooglus)
  * [#16250](https://github.com/bitcoin/bitcoin/pull/16250) signrawtransactionwithkey: report error when missing redeemScript/witnessScript (ajtowns)

### GUI

  * [#16044](https://github.com/bitcoin/bitcoin/pull/16044) fix the bug of OPEN CONFIGURATION FILE on Mac (shannon1916)
  * [#15957](https://github.com/bitcoin/bitcoin/pull/15957) Show “No wallets available” in open menu instead of nothing (meshcollider)
  * [#16118](https://github.com/bitcoin/bitcoin/pull/16118) Enable open wallet menu on setWalletController (promag)
  * [#16135](https://github.com/bitcoin/bitcoin/pull/16135) Set progressDialog to nullptr (promag)
  * [#16231](https://github.com/bitcoin/bitcoin/pull/16231) Fix open wallet menu initialization order (promag)
  * [#16254](https://github.com/bitcoin/bitcoin/pull/16254) Set `AA_EnableHighDpiScaling` attribute early (hebasto)
  * [#16122](https://github.com/bitcoin/bitcoin/pull/16122) Enable console line edit on setClientModel (promag)
  * [#16348](https://github.com/bitcoin/bitcoin/pull/16348) Assert QMetaObject::invokeMethod result (promag)

### Build system

  * [#15985](https://github.com/bitcoin/bitcoin/pull/15985) Add test for GCC bug 90348 (sipa)
  * [#15947](https://github.com/bitcoin/bitcoin/pull/15947) Install bitcoin-wallet manpage (domob1812)
  * [#15983](https://github.com/bitcoin/bitcoin/pull/15983) build with -fstack-reuse=none (MarcoFalke)

### Tests and QA

  * [#15826](https://github.com/bitcoin/bitcoin/pull/15826) Pure python EC (sipa)
  * [#15893](https://github.com/bitcoin/bitcoin/pull/15893) Add test for superfluous witness record in deserialization (instagibbs)
  * [#14818](https://github.com/bitcoin/bitcoin/pull/14818) Bugfix: test/functional/rpc_psbt: Remove check for specific error message that depends on uncertain assumptions (luke-jr)
  * [#15831](https://github.com/bitcoin/bitcoin/pull/15831) Add test that addmultisigaddress fails for watchonly addresses (MarcoFalke)

### Documentation

  * [#15890](https://github.com/bitcoin/bitcoin/pull/15890) Remove text about txes always relayed from -whitelist (harding)

### Miscellaneous

  * [#16095](https://github.com/bitcoin/bitcoin/pull/16095) Catch by reference not value in wallettool (kristapsk)
  * [#16205](https://github.com/bitcoin/bitcoin/pull/16205) Replace fprintf with tfm::format (MarcoFalke)

# Credits

Thanks to everyone who directly contributed to this release:

  * Andrew Chow
  * Anthony Towns
  * Chris Moore
  * Daniel Kraft
  * David A. Harding
  * fanquake
  * Gregory Sanders
  * Hennadii Stepanov
  * John Newbery
  * Jonas Schnelli
  * João Barbosa
  * Kristaps Kaupe
  * Luke Dashjr
  * MarcoFalke
  * MeshCollider
  * Pieter Wuille
  * shannon1916
  * tecnovert
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

