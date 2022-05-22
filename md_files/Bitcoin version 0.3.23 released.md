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
0.3.23

# Bitcoin version 0.3.23 released

14 June 2011

Win32, Linux, MacOSX and source releases for bitcoin v0.3.23 have been
uploaded to
<http://sourceforge.net/projects/bitcoin/files/Bitcoin/bitcoin-0.3.23/>

This is another quick bugfix release, trying to deal with the influx of new
bitcoin users.

Priority for next version: wallet encryption

Main items of note:

P2P connect-to-node logic changed to reduce timeout a bit. The network saw a
huge influx of new users, who do not permit incoming connections. This change
is a short-term hack, to more quickly hunt for useful P2P connections. Better
“leaf node” logic is in the works, but this should let us limp along until
then. One may use -upnp to properly forward ports, and help the network.
Transaction fee reduced to 0.0005 for new transactions (see note below) Client
will relay transactions with fees as low as 0.0001 BTC (see note below)

**NOTE:** There has been some fee confusion recently. Free transactions are
supported and relayed as they always have been, according to special anti-spam
rules. See <https://en.bitcoin.it/wiki/Transaction_fees> for details.

There were no changes between -rc1 and -final.

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

