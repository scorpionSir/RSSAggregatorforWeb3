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
0.7.1

# Bitcoin-Qt version 0.7.1 released

19 October 2012

Bitcoin-Qt version 0.7.1 is now available from:
<http://sourceforge.net/projects/bitcoin/files/Bitcoin/bitcoin-0.7.1/>

This is a bug-fix minor release.

Please report bugs using the issue tracker at github:
<https://github.com/bitcoin/bitcoin/issues>

Project source code is hosted at github; you can get source-only
tarballs/zipballs directly from there:
<https://github.com/bitcoin/bitcoin/tarball/v0.7.1> # .tar.gz
<https://github.com/bitcoin/bitcoin/zipball/v0.7.1> # .zip

Ubuntu Linux users can use the “Personal Package Archive” (PPA) maintained by
Matt Corallo to automatically keep up-to-date. Just type: sudo apt-add-
repository ppa:bitcoin/bitcoin sudo apt-get update in your terminal, then
install the bitcoin-qt package: sudo apt-get install bitcoin-qt

## KNOWN ISSUES

Mac OSX 10.5 is no longer supported.

## How to Upgrade

If you are running an older version, shut it down. Wait until it has
completely shut down (which might take a few minutes for older versions), then
run the installer (on Windows) or just copy over /Applications/Bitcoin-Qt (on
Mac) or bitcoind/bitcoin-qt (on Linux).

If you were running on Linux with a version that might have been compiled with
a different version of Berkeley DB (for example, if you were using an Ubuntu
PPA version), then run the old version again with the -detachdb argument and
shut it down; if you do not, then the new version will not be able to read the
database files and will exit with an error.

Explanation of -detachdb (and the new “stop true” RPC command): The Berkeley
DB database library stores data in both “.dat” and “log” files, so the
database is always in a consistent state, even in case of power failure or
other sudden shutdown. The format of the “.dat” files is portable between
different versions of Berkeley DB, but the “log” files are not– even minor
version differences may have incompatible “log” files. The -detachdb option
moves any pending changes from the “log” files to the “blkindex.dat” file for
maximum compatibility, but makes shutdown much slower. Note that the
“wallet.dat” file is always detached, and versions prior to 0.6.0 detached all
databases at shutdown.

## New features

  * Added a boolean argument to the RPC `stop` command, if true sets -detachdb to create standalone database .dat files before shutting down.

  * -salvagewallet command-line option, which moves any existing wallet.dat to wallet.{timestamp}.dat and then attempts to salvage public/private keys and master encryption keys (if the wallet is encrypted) into a new wallet.dat. This should only be used if your wallet becomes corrupted, and is not intended to replace regular wallet backups.

  * Import $DataDir/bootstrap.dat automatically, if it exists.

## Dependency changes

  * Qt 4.8.2 for Windows builds

  * openssl 1.0.1c

## Bug fixes

  * Clicking on a bitcoin: URI on Windows should now launch Bitcoin-Qt properly.

  * When running -testnet, use RPC port 18332 by default.

  * Better detection and handling of corrupt wallet.dat and blkindex.dat files. Previous versions would crash with a DB_RUNRECOVERY exception, this version detects most problems and tells you how to recover if it cannot recover itself.

  * Fixed an uninitialized variable bug that could cause transactions to be reported out of order.

  * Fixed a bug that could cause occasional crashes on exit.

  * Warn the user that they need to create fresh wallet backups after they encrypt their wallet.

* * *

Thanks to everybody who contributed to this release:

  * Gavin Andresen
  * Jeff Garzik
  * Luke Dashjr
  * Mark Friedenbach
  * Matt Corallo
  * Philip Kaufmann
  * Pieter Wuille
  * Rune K. Svendsen
  * Virgil Dupras
  * Wladimir J. van der Laan
  * fanquake
  * kjj2
  * xanatos

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

