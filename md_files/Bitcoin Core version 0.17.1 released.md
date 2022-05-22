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
0.17.1

# Bitcoin Core version 0.17.1 released

25 December 2018

ALL TOPICS

  * How to Upgrade
    * Downgrading warning
  * Compatibility
  * Notable changes
    * `listtransactions` label support
  * 0.17.1 change log \- {:.} P2P protocol and network code \- {:.} Wallet \- {:.} RPC and other APIs \- {:.} GUI \- {:.} Build system \- {:.} Tests and QA \- {:.} Documentation
  * Credits

Bitcoin Core version 0.17.1 is now available from:

<https://bitcoincore.org/bin/bitcoin-core-0.17.1/>

This is a new minor version release, with various bugfixes and performance
improvements, as well as updated translations.

Please report bugs using the issue tracker at GitHub:

<https://github.com/bitcoin/bitcoin/issues>

To receive security and update notifications, please subscribe to:

<https://bitcoincore.org/en/list/announcements/join/>

# How to Upgrade

If you are running an older version, shut it down. Wait until it has
completely shut down (which might take a few minutes for older versions), then
run the installer (on Windows) or just copy over `/Applications/Bitcoin-Qt`
(on Mac) or `bitcoind`/`bitcoin-qt` (on Linux).

If your node has a txindex, the txindex db will be migrated the first time you
run 0.17.0 or newer, which may take up to a few hours. Your node will not be
functional until this migration completes.

The first time you run version 0.15.0 or newer, your chainstate database will
be converted to a new format, which will take anywhere from a few minutes to
half an hour, depending on the speed of your machine.

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
Linux kernel, macOS 10.10+, and Windows 7 and newer (Windows XP is not
supported).

Bitcoin Core should also work on most other Unix-like systems but is not
frequently tested on them.

From 0.17.0 onwards macOS <10.10 is no longer supported. 0.17.0 is built using
Qt 5.9.x, which doesn’t support versions of macOS older than 10.10.

# Notable changes

## `listtransactions` label support

The `listtransactions` RPC `account` parameter which was deprecated in 0.17.0
and renamed to `dummy` has been un-deprecated and renamed again to `label`.

When bitcoin is configured with the `-deprecatedrpc=accounts` setting,
specifying a label/account/dummy argument will return both outgoing and
incoming transactions. Without the `-deprecatedrpc=accounts` setting, it will
only return incoming transactions (because it used to be possible to create
transactions spending from specific accounts, but this is no longer possible
with labels).

When `-deprecatedrpc=accounts` is set, it’s possible to pass the empty string
“” to list transactions that don’t have any label. Without
`-deprecatedrpc=accounts`, passing the empty string is an error because
returning only non-labeled transactions is not generally useful behavior and
can cause confusion.

# 0.17.1 change log

### P2P protocol and network code

  * [#14685](https://github.com/bitcoin/bitcoin/pull/14685) [`9406502`](https://github.com/bitcoin/bitcoin/commit/9406502) Fix a deserialization overflow edge case (kazcw)
  * [#14728](https://github.com/bitcoin/bitcoin/pull/14728) [`b901578`](https://github.com/bitcoin/bitcoin/commit/b901578) Fix uninitialized read when stringifying an addrLocal (kazcw)

### Wallet

  * [#14441](https://github.com/bitcoin/bitcoin/pull/14441) [`5150acc`](https://github.com/bitcoin/bitcoin/commit/5150acc) Restore ability to list incoming transactions by label (jnewbery)
  * [#13546](https://github.com/bitcoin/bitcoin/pull/13546) [`91fa15a`](https://github.com/bitcoin/bitcoin/commit/91fa15a) Fix use of uninitialized value `bnb_used` in CWallet::CreateTransaction(…) (practicalswift)
  * [#14310](https://github.com/bitcoin/bitcoin/pull/14310) [`bb90695`](https://github.com/bitcoin/bitcoin/commit/bb90695) Ensure wallet is unlocked before signing (gustavonalle)
  * [#14690](https://github.com/bitcoin/bitcoin/pull/14690) [`5782fdc`](https://github.com/bitcoin/bitcoin/commit/5782fdc) Throw error if CPubKey is invalid during PSBT keypath serialization (instagibbs)
  * [#14852](https://github.com/bitcoin/bitcoin/pull/14852) [`2528443`](https://github.com/bitcoin/bitcoin/commit/2528443) backport: [tests] Add `wallet_balance.py` (MarcoFalke)
  * [#14196](https://github.com/bitcoin/bitcoin/pull/14196) [`3362a95`](https://github.com/bitcoin/bitcoin/commit/3362a95) psbt: always drop the unnecessary utxo and convert non-witness utxo to witness when necessary (achow101)
  * [#14588](https://github.com/bitcoin/bitcoin/pull/14588) [`70ee1f8`](https://github.com/bitcoin/bitcoin/commit/70ee1f8) Refactor PSBT signing logic to enforce invariant and fix signing bug (gwillen)
  * [#14424](https://github.com/bitcoin/bitcoin/pull/14424) [`89a9a9d`](https://github.com/bitcoin/bitcoin/commit/89a9a9d) Stop requiring imported pubkey to sign non-PKH schemes (sipa, MeshCollider)

### RPC and other APIs

  * [#14417](https://github.com/bitcoin/bitcoin/pull/14417) [`fb9ad04`](https://github.com/bitcoin/bitcoin/commit/fb9ad04) Fix listreceivedbyaddress not taking address as a string (etscrivner)
  * [#14596](https://github.com/bitcoin/bitcoin/pull/14596) [`de5e48a`](https://github.com/bitcoin/bitcoin/commit/de5e48a) Bugfix: RPC: Add `address_type` named param for createmultisig (luke-jr)
  * [#14618](https://github.com/bitcoin/bitcoin/pull/14618) [`9666dba`](https://github.com/bitcoin/bitcoin/commit/9666dba) Make HTTP RPC debug logging more informative (practicalswift)
  * [#14197](https://github.com/bitcoin/bitcoin/pull/14197) [`7bee414`](https://github.com/bitcoin/bitcoin/commit/7bee414) [psbt] Convert non-witness UTXOs to witness if witness sig created (achow101)
  * [#14377](https://github.com/bitcoin/bitcoin/pull/14377) [`a3fe125`](https://github.com/bitcoin/bitcoin/commit/a3fe125) Check that a separator is found for psbt inputs, outputs, and global map (achow101)
  * [#14356](https://github.com/bitcoin/bitcoin/pull/14356) [`7a590d8`](https://github.com/bitcoin/bitcoin/commit/7a590d8) Fix converttopsbt permitsigdata arg, add basic test (instagibbs)
  * [#14453](https://github.com/bitcoin/bitcoin/pull/14453) [`75b5d8c`](https://github.com/bitcoin/bitcoin/commit/75b5d8c) Fix wallet unload during walletpassphrase timeout (promag)

### GUI

  * [#14403](https://github.com/bitcoin/bitcoin/pull/14403) [`0242b5a`](https://github.com/bitcoin/bitcoin/commit/0242b5a) Revert “Force TLS1.0+ for SSL connections” (real-or-random)
  * [#14593](https://github.com/bitcoin/bitcoin/pull/14593) [`df5131b`](https://github.com/bitcoin/bitcoin/commit/df5131b) Explicitly disable “Dark Mode” appearance on macOS (fanquake)

### Build system

  * [#14647](https://github.com/bitcoin/bitcoin/pull/14647) [`7edebed`](https://github.com/bitcoin/bitcoin/commit/7edebed) Remove illegal spacing in darwin.mk (ch4ot1c)
  * [#14698](https://github.com/bitcoin/bitcoin/pull/14698) [`ec71f06`](https://github.com/bitcoin/bitcoin/commit/ec71f06) Add bitcoin-tx.exe into Windows installer (ken2812221)

### Tests and QA

  * [#13965](https://github.com/bitcoin/bitcoin/pull/13965) [`29899ec`](https://github.com/bitcoin/bitcoin/commit/29899ec) Fix extended functional tests fail (ken2812221)
  * [#14011](https://github.com/bitcoin/bitcoin/pull/14011) [`9461f98`](https://github.com/bitcoin/bitcoin/commit/9461f98) Disable wallet and address book Qt tests on macOS minimal platform (ryanofsky)
  * [#14180](https://github.com/bitcoin/bitcoin/pull/14180) [`86fadee`](https://github.com/bitcoin/bitcoin/commit/86fadee) Run all tests even if wallet is not compiled (MarcoFalke)
  * [#14122](https://github.com/bitcoin/bitcoin/pull/14122) [`8bc1bad`](https://github.com/bitcoin/bitcoin/commit/8bc1bad) Test `rpc_help.py` failed: Check whether ZMQ is enabled or not (Kvaciral)
  * [#14101](https://github.com/bitcoin/bitcoin/pull/14101) [`96dc936`](https://github.com/bitcoin/bitcoin/commit/96dc936) Use named args in validation acceptance tests (MarcoFalke)
  * [#14020](https://github.com/bitcoin/bitcoin/pull/14020) [`24d796a`](https://github.com/bitcoin/bitcoin/commit/24d796a) Add tests for RPC help (promag)
  * [#14052](https://github.com/bitcoin/bitcoin/pull/14052) [`7ff32a6`](https://github.com/bitcoin/bitcoin/commit/7ff32a6) Add some actual witness in `rpc_rawtransaction` (MarcoFalke)
  * [#14215](https://github.com/bitcoin/bitcoin/pull/14215) [`b72fbab`](https://github.com/bitcoin/bitcoin/commit/b72fbab) Use correct python index slices in example test (sdaftuar)
  * [#14024](https://github.com/bitcoin/bitcoin/pull/14024) [`06544fa`](https://github.com/bitcoin/bitcoin/commit/06544fa) Add `TestNode::assert_debug_log` (MarcoFalke)
  * [#14658](https://github.com/bitcoin/bitcoin/pull/14658) [`60f7a97`](https://github.com/bitcoin/bitcoin/commit/60f7a97) Add test to ensure node can generate all rpc help texts at runtime (MarcoFalke)
  * [#14632](https://github.com/bitcoin/bitcoin/pull/14632) [`96f15e8`](https://github.com/bitcoin/bitcoin/commit/96f15e8) Fix a comment (fridokus)
  * [#14700](https://github.com/bitcoin/bitcoin/pull/14700) [`f9db08e`](https://github.com/bitcoin/bitcoin/commit/f9db08e) Avoid race in `p2p_invalid_block` by waiting for the block request (MarcoFalke)
  * [#14845](https://github.com/bitcoin/bitcoin/pull/14845) [`67225e2`](https://github.com/bitcoin/bitcoin/commit/67225e2) Add `wallet_balance.py` (jnewbery)

### Documentation

  * [#14161](https://github.com/bitcoin/bitcoin/pull/14161) [`5f51fd6`](https://github.com/bitcoin/bitcoin/commit/5f51fd6) doc/descriptors.md tweaks (ryanofsky)
  * [#14276](https://github.com/bitcoin/bitcoin/pull/14276) [`85aacc4`](https://github.com/bitcoin/bitcoin/commit/85aacc4) Add autogen.sh in ARM Cross-compilation (walterwhite81)

# Credits

Thanks to everyone who directly contributed to this release:

  * Andrew Chow
  * Chun Kuan Lee
  * David A. Harding
  * Eric Scrivner
  * fanquake
  * fridokus
  * Glenn Willen
  * Gregory Sanders
  * gustavonalle
  * John Newbery
  * Jon Layton
  * Jonas Schnelli
  * João Barbosa
  * Kaz Wesley
  * Kvaciral
  * Luke Dashjr
  * MarcoFalke
  * MeshCollider
  * Pieter Wuille
  * practicalswift
  * Russell Yanofsky
  * Sjors Provoost
  * Suhas Daftuar
  * Tim Ruffing
  * Walter
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

