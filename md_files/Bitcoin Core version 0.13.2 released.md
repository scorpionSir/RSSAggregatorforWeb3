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
0.13.2

# Bitcoin Core version 0.13.2 released

3 January 2017

ALL TOPICS

  * Compatibility
  * Notable changes
    * Change to wallet handling of mempool rejection
  * 0.13.2 Change log \- {:.} Consensus \- {:.} RPC and other APIs \- {:.} Block and transaction handling \- {:.} P2P protocol and network code \- {:.} Build system \- {:.} GUI \- {:.} Wallet \- {:.} Tests and QA \- {:.} Miscellaneous
  * Credits

Bitcoin Core version 0.13.2 is now available from:

<https://bitcoin.org/bin/bitcoin-core-0.13.2/>

This is a new minor version release, including various bugfixes and
performance improvements, as well as updated translations.

Please report bugs using the issue tracker at github:

<https://github.com/bitcoin/bitcoin/issues>

To receive security and update notifications, please subscribe to:

<https://bitcoincore.org/en/list/announcements/join/>

# Compatibility

Microsoft ended support for Windows XP on [April 8th,
2014](https://www.microsoft.com/en-us/WindowsForBusiness/end-of-xp-support),
an OS initially released in 2001. This means that not even critical security
updates will be released anymore. Without security updates, using a bitcoin
wallet on a XP machine is irresponsible at least.

In addition to that, with 0.12.x there have been varied reports of Bitcoin
Core randomly crashing on Windows XP. It is [not
clear](https://github.com/bitcoin/bitcoin/issues/7681#issuecomment-217439891)
what the source of these crashes is, but it is likely that upstream libraries
such as Qt are no longer being tested on XP.

We do not have time nor resources to provide support for an OS that is end-of-
life. From 0.13.0 on, Windows XP is no longer supported. Users are suggested
to upgrade to a newer version of Windows, or install an alternative OS that is
supported.

No attempt is made to prevent installing or running the software on Windows
XP, you can still do so at your own risk, but do not expect it to work: do not
report issues about Windows XP to the issue tracker.

From 0.13.1 onwards OS X 10.7 is no longer supported. 0.13.0 was intended to
work on 10.7+, but severe issues with the libc++ version on 10.7.x keep it
from running reliably. 0.13.1 now requires 10.8+, and will communicate that to
10.7 users, rather than crashing unexpectedly.

# Notable changes

## Change to wallet handling of mempool rejection

When a newly created transaction failed to enter the mempool due to the limits
on chains of unconfirmed transactions the sending RPC calls would return an
error. The transaction would still be queued in the wallet and, once some of
the parent transactions were confirmed, broadcast after the software was
restarted.

This behavior has been changed to return success and to reattempt mempool
insertion at the same time transaction rebroadcast is attempted, avoiding a
need for a restart.

Transactions in the wallet which cannot be accepted into the mempool can be
abandoned with the previously existing abandontransaction RPC (or in the GUI
via a context menu on the transaction).

# 0.13.2 Change log

Detailed release notes follow. This overview includes changes that affect
behavior, not code moves, refactors and string updates. For convenience in
locating the code changes and accompanying discussion, both the pull request
and git merge commit are mentioned.

### Consensus

  * [#9293](https://github.com/bitcoin/bitcoin/pull/9293) [`e591c10`](https://github.com/bitcoin/bitcoin/commit/e591c10) [0.13 Backport [#9053](https://github.com/bitcoin/bitcoin/pull/9053)] IBD using chainwork instead of height and not using header timestamp (gmaxwell)
  * [#9053](https://github.com/bitcoin/bitcoin/pull/9053) [`5b93eee`](https://github.com/bitcoin/bitcoin/commit/5b93eee) IBD using chainwork instead of height and not using header timestamps (gmaxwell)

### RPC and other APIs

  * [#8845](https://github.com/bitcoin/bitcoin/pull/8845) [`1d048b9`](https://github.com/bitcoin/bitcoin/commit/1d048b9) Don’t return the address of a P2SH of a P2SH (jnewbery)
  * [#9041](https://github.com/bitcoin/bitcoin/pull/9041) [`87fbced`](https://github.com/bitcoin/bitcoin/commit/87fbced) keypoololdest denote Unix epoch, not GMT (s-matthew-english)
  * [#9122](https://github.com/bitcoin/bitcoin/pull/9122) [`f82c81b`](https://github.com/bitcoin/bitcoin/commit/f82c81b) fix getnettotals RPC description about timemillis (visvirial)
  * [#9042](https://github.com/bitcoin/bitcoin/pull/9042) [`5bcb05d`](https://github.com/bitcoin/bitcoin/commit/5bcb05d) [rpc] ParseHash: Fail when length is not 64 (MarcoFalke)
  * [#9194](https://github.com/bitcoin/bitcoin/pull/9194) [`f26dab7`](https://github.com/bitcoin/bitcoin/commit/f26dab7) Add option to return non-segwit serialization via rpc (instagibbs)
  * [#9347](https://github.com/bitcoin/bitcoin/pull/9347) [`b711390`](https://github.com/bitcoin/bitcoin/commit/b711390) [0.13.2] wallet/rpc backports (MarcoFalke)
  * [#9292](https://github.com/bitcoin/bitcoin/pull/9292) [`c365556`](https://github.com/bitcoin/bitcoin/commit/c365556) Complain when unknown rpcserialversion is specified (sipa)
  * [#9322](https://github.com/bitcoin/bitcoin/pull/9322) [`49a612f`](https://github.com/bitcoin/bitcoin/commit/49a612f) [qa] Don’t set unknown rpcserialversion (MarcoFalke)

### Block and transaction handling

  * [#8357](https://github.com/bitcoin/bitcoin/pull/8357) [`ce0d817`](https://github.com/bitcoin/bitcoin/commit/ce0d817) [mempool] Fix relaypriority calculation error (maiiz)
  * [#9267](https://github.com/bitcoin/bitcoin/pull/9267) [`0a4aa87`](https://github.com/bitcoin/bitcoin/commit/0a4aa87) [0.13 backport [#9239](https://github.com/bitcoin/bitcoin/pull/9239)] Disable fee estimates for a confirm target of 1 block (morcos)
  * [#9196](https://github.com/bitcoin/bitcoin/pull/9196) [`0c09d9f`](https://github.com/bitcoin/bitcoin/commit/0c09d9f) Send tip change notification from invalidateblock (ryanofsky)

### P2P protocol and network code

  * [#8995](https://github.com/bitcoin/bitcoin/pull/8995) [`9ef3875`](https://github.com/bitcoin/bitcoin/commit/9ef3875) Add missing cs_main lock to ::GETBLOCKTXN processing (TheBlueMatt)
  * [#9234](https://github.com/bitcoin/bitcoin/pull/9234) [`94531b5`](https://github.com/bitcoin/bitcoin/commit/94531b5) torcontrol: Explicitly request RSA1024 private key (laanwj)
  * [#8637](https://github.com/bitcoin/bitcoin/pull/8637) [`2cad5db`](https://github.com/bitcoin/bitcoin/commit/2cad5db) Compact Block Tweaks (rebase of [#8235](https://github.com/bitcoin/bitcoin/pull/8235)) (sipa)
  * [#9058](https://github.com/bitcoin/bitcoin/pull/9058) [`286e548`](https://github.com/bitcoin/bitcoin/commit/286e548) Fixes for p2p-compactblocks.py test timeouts on travis ([#8842](https://github.com/bitcoin/bitcoin/pull/8842)) (ryanofsky)
  * [#8865](https://github.com/bitcoin/bitcoin/pull/8865) [`4c71fc4`](https://github.com/bitcoin/bitcoin/commit/4c71fc4) Decouple peer-processing-logic from block-connection-logic (TheBlueMatt)
  * [#9117](https://github.com/bitcoin/bitcoin/pull/9117) [`6fe3981`](https://github.com/bitcoin/bitcoin/commit/6fe3981) net: don’t send feefilter messages before the version handshake is complete (theuni)
  * [#9188](https://github.com/bitcoin/bitcoin/pull/9188) [`ca1fd75`](https://github.com/bitcoin/bitcoin/commit/ca1fd75) Make orphan parent fetching ask for witnesses (gmaxwell)
  * [#9052](https://github.com/bitcoin/bitcoin/pull/9052) [`3a3bcbf`](https://github.com/bitcoin/bitcoin/commit/3a3bcbf) Use RelevantServices instead of node_network in AttemptToEvict (gmaxwell)
  * [#9048](https://github.com/bitcoin/bitcoin/pull/9048) [`9460771`](https://github.com/bitcoin/bitcoin/commit/9460771) [0.13 backport [#9026](https://github.com/bitcoin/bitcoin/pull/9026)] Fix handling of invalid compact blocks (sdaftuar)
  * [#9357](https://github.com/bitcoin/bitcoin/pull/9357) [`03b6f62`](https://github.com/bitcoin/bitcoin/commit/03b6f62) [0.13 backport [#9352](https://github.com/bitcoin/bitcoin/pull/9352)] Attempt reconstruction from all compact block announcements (sdaftuar)
  * [#9189](https://github.com/bitcoin/bitcoin/pull/9189) [`b96a8f7`](https://github.com/bitcoin/bitcoin/commit/b96a8f7) Always add default_witness_commitment with GBT client support (sipa)
  * [#9253](https://github.com/bitcoin/bitcoin/pull/9253) [`28d0f22`](https://github.com/bitcoin/bitcoin/commit/28d0f22) Fix calculation of number of bound sockets to use (TheBlueMatt)
  * [#9199](https://github.com/bitcoin/bitcoin/pull/9199) [`da5a16b`](https://github.com/bitcoin/bitcoin/commit/da5a16b) Always drop the least preferred HB peer when adding a new one (gmaxwell)

### Build system

  * [#9169](https://github.com/bitcoin/bitcoin/pull/9169) [`d1b4da9`](https://github.com/bitcoin/bitcoin/commit/d1b4da9) build: fix qt5.7 build under macOS (theuni)
  * [#9326](https://github.com/bitcoin/bitcoin/pull/9326) [`a0f7ece`](https://github.com/bitcoin/bitcoin/commit/a0f7ece) Update for OpenSSL 1.1 API (gmaxwell)
  * [#9224](https://github.com/bitcoin/bitcoin/pull/9224) [`396c405`](https://github.com/bitcoin/bitcoin/commit/396c405) Prevent FD_SETSIZE error building on OpenBSD (ivdsangen)

### GUI

  * [#8972](https://github.com/bitcoin/bitcoin/pull/8972) [`6f86b53`](https://github.com/bitcoin/bitcoin/commit/6f86b53) Make warnings label selectable (jonasschnelli) (MarcoFalke)
  * [#9185](https://github.com/bitcoin/bitcoin/pull/9185) [`6d70a73`](https://github.com/bitcoin/bitcoin/commit/6d70a73) Fix coincontrol sort issue (jonasschnelli)
  * [#9094](https://github.com/bitcoin/bitcoin/pull/9094) [`5f3a12c`](https://github.com/bitcoin/bitcoin/commit/5f3a12c) Use correct conversion function for boost::path datadir (laanwj)
  * [#8908](https://github.com/bitcoin/bitcoin/pull/8908) [`4a974b2`](https://github.com/bitcoin/bitcoin/commit/4a974b2) Update bitcoin-qt.desktop (s-matthew-english)
  * [#9190](https://github.com/bitcoin/bitcoin/pull/9190) [`dc46b10`](https://github.com/bitcoin/bitcoin/commit/dc46b10) Plug many memory leaks (laanwj)

### Wallet

  * [#9290](https://github.com/bitcoin/bitcoin/pull/9290) [`35174a0`](https://github.com/bitcoin/bitcoin/commit/35174a0) Make RelayWalletTransaction attempt to AcceptToMemoryPool (gmaxwell)
  * [#9295](https://github.com/bitcoin/bitcoin/pull/9295) [`43bcfca`](https://github.com/bitcoin/bitcoin/commit/43bcfca) Bugfix: Fundrawtransaction: don’t terminate when keypool is empty (jonasschnelli)
  * [#9302](https://github.com/bitcoin/bitcoin/pull/9302) [`f5d606e`](https://github.com/bitcoin/bitcoin/commit/f5d606e) Return txid even if ATMP fails for new transaction (sipa)
  * [#9262](https://github.com/bitcoin/bitcoin/pull/9262) [`fe39f26`](https://github.com/bitcoin/bitcoin/commit/fe39f26) Prefer coins that have fewer ancestors, sanity check txn before ATMP (instagibbs)

### Tests and QA

  * [#9159](https://github.com/bitcoin/bitcoin/pull/9159) [`eca9b46`](https://github.com/bitcoin/bitcoin/commit/eca9b46) Wait for specific block announcement in p2p-compactblocks (ryanofsky)
  * [#9186](https://github.com/bitcoin/bitcoin/pull/9186) [`dccdc3a`](https://github.com/bitcoin/bitcoin/commit/dccdc3a) Fix use-after-free in scheduler tests (laanwj)
  * [#9168](https://github.com/bitcoin/bitcoin/pull/9168) [`3107280`](https://github.com/bitcoin/bitcoin/commit/3107280) Add assert_raises_message to check specific error message (mrbandrews)
  * [#9191](https://github.com/bitcoin/bitcoin/pull/9191) [`29435db`](https://github.com/bitcoin/bitcoin/commit/29435db) 0.13.2 Backports (MarcoFalke)
  * [#9077](https://github.com/bitcoin/bitcoin/pull/9077) [`1d4c884`](https://github.com/bitcoin/bitcoin/commit/1d4c884) Increase wallet-dump RPC timeout (ryanofsky)
  * [#9098](https://github.com/bitcoin/bitcoin/pull/9098) [`ecd7db5`](https://github.com/bitcoin/bitcoin/commit/ecd7db5) Handle zombies and cluttered tmpdirs (MarcoFalke)
  * [#8927](https://github.com/bitcoin/bitcoin/pull/8927) [`387ec9d`](https://github.com/bitcoin/bitcoin/commit/387ec9d) Add script tests for FindAndDelete in pre-segwit and segwit scripts (jl2012)
  * [#9200](https://github.com/bitcoin/bitcoin/pull/9200) [`eebc699`](https://github.com/bitcoin/bitcoin/commit/eebc699) bench: Fix subtle counting issue when rescaling iteration count (laanwj)

### Miscellaneous

  * [#8838](https://github.com/bitcoin/bitcoin/pull/8838) [`094848b`](https://github.com/bitcoin/bitcoin/commit/094848b) Calculate size and weight of block correctly in CreateNewBlock() (jnewbery)
  * [#8920](https://github.com/bitcoin/bitcoin/pull/8920) [`40169dc`](https://github.com/bitcoin/bitcoin/commit/40169dc) Set minimum required Boost to 1.47.0 (fanquake)
  * [#9251](https://github.com/bitcoin/bitcoin/pull/9251) [`a710a43`](https://github.com/bitcoin/bitcoin/commit/a710a43) Improvement of documentation of command line parameter ‘whitelist’ (wodry)
  * [#8932](https://github.com/bitcoin/bitcoin/pull/8932) [`106da69`](https://github.com/bitcoin/bitcoin/commit/106da69) Allow bitcoin-tx to create v2 transactions (btcdrak)
  * [#8929](https://github.com/bitcoin/bitcoin/pull/8929) [`12428b4`](https://github.com/bitcoin/bitcoin/commit/12428b4) add software-properties-common (sigwo)
  * [#9120](https://github.com/bitcoin/bitcoin/pull/9120) [`08d1c90`](https://github.com/bitcoin/bitcoin/commit/08d1c90) bug: Missed one “return false” in recent refactoring in [#9067](https://github.com/bitcoin/bitcoin/pull/9067) (UdjinM6)
  * [#9067](https://github.com/bitcoin/bitcoin/pull/9067) [`f85ee01`](https://github.com/bitcoin/bitcoin/commit/f85ee01) Fix exit codes (UdjinM6)
  * [#9340](https://github.com/bitcoin/bitcoin/pull/9340) [`fb987b3`](https://github.com/bitcoin/bitcoin/commit/fb987b3) [0.13] Update secp256k1 subtree (MarcoFalke)
  * [#9229](https://github.com/bitcoin/bitcoin/pull/9229) [`b172377`](https://github.com/bitcoin/bitcoin/commit/b172377) Remove calls to getaddrinfo_a (TheBlueMatt)

# Credits

Thanks to everyone who directly contributed to this release:

  * Alex Morcos
  * BtcDrak
  * Cory Fields
  * fanquake
  * Gregory Maxwell
  * Gregory Sanders
  * instagibbs
  * Ivo van der Sangen
  * jnewbery
  * Johnson Lau
  * Jonas Schnelli
  * Luke Dashjr
  * maiiz
  * MarcoFalke
  * Masahiko Hyuga
  * Matt Corallo
  * matthias
  * mrbandrews
  * Pavel Janík
  * Pieter Wuille
  * randy-waterhouse
  * Russell Yanofsky
  * S. Matthew English
  * Steven
  * Suhas Daftuar
  * UdjinM6
  * Wladimir J. van der Laan
  * wodry

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

