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
0.5.0

# Bitcoin-Qt version 0.5.0 released

21 November 2011

Bitcoin-Qt version 0.5.0 is now available for download at:
<http://sourceforge.net/projects/bitcoin/files/Bitcoin/bitcoin-0.5.0/>

The major change for this release is a completely new graphical that uses the
Qt user interface toolkit.

This release includes German, Spanish, Spanish-Castilian, Norwegian and Dutch
translations. More translations are welcome; join the project at Transifex if
you can help: <https://www.transifex.com/projects/p/bitcoin/>

Please report bugs using the issue tracker at GitHub:
<https://github.com/bitcoin/bitcoin/issues>

## MAJOR BUG FIX (CVE-2011-4447)

The wallet encryption feature introduced in Bitcoin version 0.4.0 did not
sufficiently secure the private keys. An attacker who managed to get a copy of
your encrypted wallet.dat file might be able to recover some or all of the
unencrypted keys and steal the associated coins.

If you have a previously encrypted wallet.dat, the first time you run bitcoin-
qt or bitcoind the wallet will be rewritten, Bitcoin will shut down, and you
will be prompted to restart it to run with the new, properly encrypted file.

If you had a previously encrypted wallet.dat that might have been copied or
stolen (for example, you backed it up to a public location) you should send
all of your bitcoins to yourself using a new bitcoin address and stop using
any previously generated addresses.

Wallets encrypted with this version of Bitcoin are written properly.

Technical note: the encrypted wallet’s ‘keypool’ will be regenerated the first
time you request a new bitcoin address; to be certain that the new private
keys are properly backed up you should:

  1. Run Bitcoin and let it rewrite the `wallet.dat` file

  2. Run it again, then ask it for a new bitcoin address.

Bitcoin-Qt: Address Book, then New Address…

bitcoind: run the `walletpassphrase` RPC command to unlock the wallet, then
run the `getnewaddress` RPC command.

  3. If your encrypted wallet.dat may have been copied or stolen, send all of your bitcoins to the new bitcoin address.

  4. Shut down Bitcoin, then backup the wallet.dat file. IMPORTANT: be sure to request a new bitcoin address before backing up, so that the ‘keypool’ is regenerated and backed up.

“Security in depth” is always a good idea, so choosing a secure location for
the backup and/or encrypting the backup before uploading it is recommended.
And as in previous releases, if your machine is infected by malware there are
several ways an attacker might steal your bitcoins.

Thanks to Alan Reiner (aka etotheipi) for finding and reporting this bug.

## MAJOR GUI CHANGES

  * “Splash” graphics at startup that show address/wallet/blockchain loading progress.

  * “Synchronizing with network” progress bar to show block-chain download progress.

  * Icons at the bottom of the window that show how well connected you are to the network, with tooltips to display details.

  * Drag and drop support for bitcoin: URIs on web pages.

  * Export transactions as a .csv file.

  * Many other GUI improvements, large and small.

## RPC CHANGES

  * getmemorypool : new RPC command, provides everything needed to construct a block with a custom generation transaction and submit a solution

  * listsinceblock : new RPC command, list transactions since given block

  * signmessage/verifymessage : new RPC commands to sign a message with one of your private keys or verify that a message signed by the private key associated with a bitcoin address.

## GENERAL CHANGES

  * Faster initial block download.

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

