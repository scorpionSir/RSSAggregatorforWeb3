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
0.14.2

# Bitcoin Core version 0.14.2 released

17 June 2017

ALL TOPICS

  * Compatibility
  * Notable changes
    * miniupnp CVE-2017-8798
  * Known Bugs
  * 0.14.2 Change log \- {:.} RPC and other APIs \- {:.} P2P protocol and network code \- {:.} Build system \- {:.} Miscellaneous \- {:.} GUI \- {:.} Wallet
  * Credits

Bitcoin Core version 0.14.2 is _not available for security reasons_ :

~~https://bitcoin.org/bin/bitcoin-core-0.14.2/~~

This is a new minor version release, including various bugfixes and
performance improvements, as well as updated translations.

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

## miniupnp CVE-2017-8798

Bundled miniupnpc was updated to 2.0.20170509. This fixes an integer
signedness error (present in MiniUPnPc v1.4.20101221 through v2.0) that allows
remote attackers (within the LAN) to cause a denial of service or possibly
have unspecified other impact.

This only affects users that have explicitly enabled UPnP through the GUI
setting or through the `-upnp` option, as since the last UPnP vulnerability
(in Bitcoin Core 0.10.3) it has been disabled by default.

If you use this option, it is recommended to upgrade to this version as soon
as possible.

# Known Bugs

Since 0.14.0 the approximate transaction fee shown in Bitcoin-Qt when using
coin control and smart fee estimation does not reflect any change in target
from the smart fee slider. It will only present an approximate fee calculated
using the default target. The fee calculated using the correct target is still
applied to the transaction and shown in the final send confirmation dialog.

# 0.14.2 Change log

Detailed release notes follow. This overview includes changes that affect
behavior, not code moves, refactors and string updates. For convenience in
locating the code changes and accompanying discussion, both the pull request
and git merge commit are mentioned.

### RPC and other APIs

  * [#10410](https://github.com/bitcoin/bitcoin/pull/10410) [`321419b`](https://github.com/bitcoin/bitcoin/commit/321419b) Fix importwallet edge case rescan bug (ryanofsky)

### P2P protocol and network code

  * [#10424](https://github.com/bitcoin/bitcoin/pull/10424) [`37a8fc5`](https://github.com/bitcoin/bitcoin/commit/37a8fc5) Populate services in GetLocalAddress (morcos)
  * [#10441](https://github.com/bitcoin/bitcoin/pull/10441) [`9e3ad50`](https://github.com/bitcoin/bitcoin/commit/9e3ad50) Only enforce expected services for half of outgoing connections (theuni)

### Build system

  * [#10414](https://github.com/bitcoin/bitcoin/pull/10414) [`ffb0c4b`](https://github.com/bitcoin/bitcoin/commit/ffb0c4b) miniupnpc 2.0.20170509 (fanquake)
  * [#10228](https://github.com/bitcoin/bitcoin/pull/10228) [`ae479bc`](https://github.com/bitcoin/bitcoin/commit/ae479bc) Regenerate bitcoin-config.h as necessary (theuni)

### Miscellaneous

  * [#10245](https://github.com/bitcoin/bitcoin/pull/10245) [`44a17f2`](https://github.com/bitcoin/bitcoin/commit/44a17f2) Minor fix in build documentation for FreeBSD 11 (shigeya)
  * [#10215](https://github.com/bitcoin/bitcoin/pull/10215) [`0aee4a1`](https://github.com/bitcoin/bitcoin/commit/0aee4a1) Check interruptNet during dnsseed lookups (TheBlueMatt)

### GUI

  * [#10231](https://github.com/bitcoin/bitcoin/pull/10231) [`1e936d7`](https://github.com/bitcoin/bitcoin/commit/1e936d7) Reduce a significant cs_main lock freeze (jonasschnelli)

### Wallet

  * [#10294](https://github.com/bitcoin/bitcoin/pull/10294) [`1847642`](https://github.com/bitcoin/bitcoin/commit/1847642) Unset change position when there is no change (instagibbs)

# Credits

Thanks to everyone who directly contributed to this release:

  * Alex Morcos
  * Cory Fields
  * fanquake
  * Gregory Sanders
  * Jonas Schnelli
  * Matt Corallo
  * Russell Yanofsky
  * Shigeya Suzuki
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

