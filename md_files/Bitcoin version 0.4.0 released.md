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
0.4.0

# Bitcoin version 0.4.0 released

23 September 2011

[Full announcement (including
signatures)](http://sourceforge.net/mailarchive/message.php?msg_id=28132490)

Bitcoin version 0.4.0 is now available for download at:
<http://sourceforge.net/projects/bitcoin/files/Bitcoin/bitcoin-0.4.0/>

The main feature in this release is wallet private key encryption; you can set
a passphrase that must be entered before sending coins. See below for more
information; if you decide to encrypt your wallet, **WRITE DOWN YOUR
PASSPHRASE AND PUT IT IN A SECURE LOCATION**. If you forget or lose your
wallet passphrase, you lose your bitcoins. Previous versions of bitcoin are
unable to read encrypted wallets, and will crash on startup if the wallet is
encrypted.

Also note: bitcoin version 0.4 uses a newer version of Berkeley DB (bdb
version 4.8) than previous versions (bdb 4.7). If you upgrade to version 0.4
and then revert back to an earlier version of bitcoin the it may be unable to
start because bdb 4.7 cannot read bdb 4.8 “log” files.

## Notable bug fixes from version 0.3.24

  * Fix several bitcoin-becomes-unresponsive bugs due to multithreading deadlocks.

  * Optimize database writes for large (lots of inputs) transactions (fixes a potential denial-of-service attack)

## Wallet Encryption

Bitcoin supports native wallet encryption so that people who steal your wallet
file don’t automatically get access to all of your Bitcoins. In order to
enable this feature, chose “Encrypt Wallet” from the Options menu. You will be
prompted to enter a passphrase, which will be used as the key to encrypt your
wallet and will be needed every time you wish to send Bitcoins. If you lose
this passphrase, you will lose access to spend all of the bitcoins in your
wallet, no one, not even the Bitcoin developers can recover your Bitcoins.
This means you are responsible for your own security, store your passphrase in
a secure location and do not forget it.

Remember that the encryption built into bitcoin only encrypts the actual keys
which are required to send your bitcoins, not the full wallet. This means that
someone who steals your wallet file will be able to see all the addresses
which belong to you, as well as the relevant transactions, you are only
protected from someone spending your coins.

It is recommended that you backup your wallet file before you encrypt your
wallet. To do this, close the Bitcoin client and copy the wallet.dat file from
`~/.bitcoin/` on Linux, `/Users/(user name)/Library/Application
Support/Bitcoin/` on Mac OSX, and `%APPDATA%/Bitcoin/` on Windows (that is
`/Users/(user name)/AppData/Roaming/Bitcoin` on Windows Vista and 7 and
`/Documents and Settings/(user name)/Application Data/Bitcoin` on Windows XP).
Once you have copied that file to a safe location, reopen the Bitcoin client
and Encrypt your wallet. If everything goes fine, delete the backup and enjoy
your encrypted wallet. Note that once you encrypt your wallet, you will never
be able to go back to a version of the Bitcoin client older than 0.4.

Keep in mind that you are always responsible for your own security. All it
takes is a slightly more advanced wallet-stealing trojan which installs a
keylogger to steal your wallet passphrase as you enter it in addition to your
wallet file and you have lost all your Bitcoins. Wallet encryption cannot keep
you safe if you do not practice good security, such as running up-to-date
antivirus software, only entering your wallet passphrase in the Bitcoin client
and using the same passphrase only as your wallet passphrase.

See the `doc/README` file in the bitcoin source for technical details of
wallet encryption.

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

