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
0.20.0

# Bitcoin Core version 0.20.0 released

3 June 2020

ALL TOPICS

  * 0.20.0 Release Notes
  * How to Upgrade
  * Compatibility
  * Known Bugs
  * Notable changes
    * P2P and network changes \- {:.} Removal of BIP61 reject network messages from Bitcoin Core
    * Updated RPCs
    * Build System
    * New settings
    * Updated settings
    * Removed settings
    * GUI changes
    * Wallet
    * Documentation changes
  * Low-level changes
    * Utilities
    * Command line
    * New RPCs
    * Updated RPCs
    * Tests
    * Build system
  * 0.20.0 change log \- {:.} Mining \- {:.} Block and transaction handling \- {:.} P2P protocol and network code \- {:.} Wallet \- {:.} RPC and other APIs \- {:.} GUI \- {:.} Build system \- {:.} Platform support \- {:.} Tests and QA \- {:.} Documentation \- {:.} Miscellaneous
  * Credits

# 0.20.0 Release Notes

Bitcoin Core version 0.20.0 is now available from:

<https://bitcoincore.org/bin/bitcoin-core-0.20.0/>

This release includes new features, various bug fixes and performance
improvements, as well as updated translations.

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

## P2P and network changes

#### Removal of BIP61 reject network messages from Bitcoin Core

The `-enablebip61` command line option to enable BIP61 has been removed.
([#17004](https://github.com/bitcoin/bitcoin/pull/17004))

This feature has been disabled by default since Bitcoin Core version 0.18.0.
Nodes on the network can not generally be trusted to send valid messages
(including reject messages), so this should only ever be used when connected
to a trusted node. Please use the alternatives recommended below if you rely
on this removed feature:

  * Testing or debugging of implementations of the Bitcoin P2P network protocol should be done by inspecting the log messages that are produced by a recent version of Bitcoin Core. Bitcoin Core logs debug messages (`-debug=<category>`) to a stream (`-printtoconsole`) or to a file (`-debuglogfile=<debug.log>`).

  * Testing the validity of a block can be achieved by specific RPCs:

    * `submitblock`

    * `getblocktemplate` with `'mode'` set to `'proposal'` for blocks with potentially invalid POW

  * Testing the validity of a transaction can be achieved by specific RPCs:

    * `sendrawtransaction`

    * `testmempoolaccept`

  * Wallets should not assume a transaction has propagated to the network just because there are no reject messages. Instead, listen for the transaction to be announced by other peers on the network. Wallets should not assume a lack of reject messages means a transaction pays an appropriate fee. Instead, set fees using fee estimation and use replace-by-fee to increase a transaction’s fee if it hasn’t confirmed within the desired amount of time.

The removal of BIP61 reject message support also has the following minor RPC
and logging implications:

  * `testmempoolaccept` and `sendrawtransaction` no longer return the P2P reject code when a transaction is not accepted to the mempool. They still return the verbal reject reason.

  * Log messages that previously reported the reject code when a transaction was not accepted to the mempool now no longer report the reject code. The reason for rejection is still reported.

## Updated RPCs

  * The RPCs which accept descriptors now accept the new `sortedmulti(...)` descriptor type which supports multisig scripts where the public keys are sorted lexicographically in the resulting script. ([#17056](https://github.com/bitcoin/bitcoin/pull/17056))

  * The `walletprocesspsbt` and `walletcreatefundedpsbt` RPCs now include BIP32 derivation paths by default for public keys if we know them. This can be disabled by setting the `bip32derivs` parameter to `false`. ([#17264](https://github.com/bitcoin/bitcoin/pull/17264))

  * The `bumpfee` RPC’s parameter `totalFee`, which was deprecated in 0.19, has been removed. ([#18312](https://github.com/bitcoin/bitcoin/pull/18312))

  * The `bumpfee` RPC will return a PSBT when used with wallets that have private keys disabled. ([#16373](https://github.com/bitcoin/bitcoin/pull/16373))

  * The `getpeerinfo` RPC now includes a `mapped_as` field to indicate the mapped Autonomous System used for diversifying peer selection. See the `-asmap` configuration option described below in _New Settings_. ([#16702](https://github.com/bitcoin/bitcoin/pull/16702))

  * The `createmultisig` and `addmultisigaddress` RPCs now return an output script descriptor for the newly created address. ([#18032](https://github.com/bitcoin/bitcoin/pull/18032))

## Build System

  * OpenSSL is no longer used by Bitcoin Core. ([#17265](https://github.com/bitcoin/bitcoin/pull/17265))

  * BIP70 support has been fully removed from Bitcoin Core. The `--enable-bip70` option remains, but it will throw an error during configure. ([#17165](https://github.com/bitcoin/bitcoin/pull/17165))

  * glibc 2.17 or greater is now required to run the release binaries. This retains compatibility with RHEL 7, CentOS 7, Debian 8 and Ubuntu 14.04 LTS. ([#17538](https://github.com/bitcoin/bitcoin/pull/17538))

  * The source code archives that are provided with gitian builds no longer contain any autotools artifacts. Therefore, to build from such source, a user should run the `./autogen.sh` script from the root of the unpacked archive. This implies that `autotools` and other required packages are installed on the user’s system. ([#18331](https://github.com/bitcoin/bitcoin/pull/18331))

## New settings

  * New `rpcwhitelist` and `rpcwhitelistdefault` configuration parameters allow giving certain RPC users permissions to only some RPC calls. ([#12763](https://github.com/bitcoin/bitcoin/pull/12763))

  * A new `-asmap` configuration option has been added to diversify the node’s network connections by mapping IP addresses Autonomous System Numbers (ASNs) and then limiting the number of connections made to any single ASN. See issue [#16599](https://github.com/bitcoin/bitcoin/pull/16599), PR [#16702](https://github.com/bitcoin/bitcoin/pull/16702), and the `bitcoind help` for more information. This option is experimental and subject to removal or breaking changes in future releases, so the legacy /16 prefix mapping of IP addresses remains the default. ([#16702](https://github.com/bitcoin/bitcoin/pull/16702))

## Updated settings

  * All custom settings configured when Bitcoin Core starts are now written to the `debug.log` file to assist troubleshooting. ([#16115](https://github.com/bitcoin/bitcoin/pull/16115))

  * Importing blocks upon startup via the `bootstrap.dat` file no longer occurs by default. The file must now be specified with `-loadblock=<file>`. ([#17044](https://github.com/bitcoin/bitcoin/pull/17044))

  * The `-debug=db` logging category has been renamed to `-debug=walletdb` to distinguish it from `coindb`. The `-debug=db` option has been deprecated and will be removed in the next major release. ([#17410](https://github.com/bitcoin/bitcoin/pull/17410))

  * The `-walletnotify` configuration parameter will now replace any `%w` in its argument with the name of the wallet generating the notification. This is not supported on Windows. ([#13339](https://github.com/bitcoin/bitcoin/pull/13339))

## Removed settings

  * The `-whitelistforcerelay` configuration parameter has been removed after it was discovered that it was rendered ineffective in version 0.13 and hasn’t actually been supported for almost four years. ([#17985](https://github.com/bitcoin/bitcoin/pull/17985))

## GUI changes

  * The “Start Bitcoin Core on system login” option has been removed on macOS. ([#17567](https://github.com/bitcoin/bitcoin/pull/17567))

  * In the Peers window, the details for a peer now displays a `Mapped AS` field to indicate the mapped Autonomous System used for diversifying peer selection. See the `-asmap` configuration option in _New Settings_ , above. ([#18402](https://github.com/bitcoin/bitcoin/pull/18402))

  * A “known bug” [announced](https://bitcoincore.org/en/releases/0.18.0/#wallet-gui) in the release notes of version 0.18 has been fixed. The issue affected anyone who simultaneously used multiple Bitcoin Core wallets and the GUI coin control feature. ([#18894](https://github.com/bitcoin/bitcoin/pull/18894))

  * For watch-only wallets, creating a new transaction in the Send screen or fee bumping an existing transaction in the Transactions screen will automatically copy a Partially-Signed Bitcoin Transaction (PSBT) to the system clipboard. This can then be pasted into an external program such as [HWI](https://github.com/bitcoin-core/HWI) for signing. Future versions of Bitcoin Core should support a GUI option for finalizing and broadcasting PSBTs, but for now the debug console may be used with the `finalizepsbt` and `sendrawtransaction` RPCs. ([#16944](https://github.com/bitcoin/bitcoin/pull/16944), [#17492](https://github.com/bitcoin/bitcoin/pull/17492))

## Wallet

  * The wallet now by default uses bech32 addresses when using RPC, and creates native segwit change outputs. ([#16884](https://github.com/bitcoin/bitcoin/pull/16884))

  * The way that output trust was computed has been fixed, which affects confirmed/unconfirmed balance status and coin selection. ([#16766](https://github.com/bitcoin/bitcoin/pull/16766))

  * The `gettransaction`, `listtransactions` and `listsinceblock` RPC responses now also include the height of the block that contains the wallet transaction, if any. ([#17437](https://github.com/bitcoin/bitcoin/pull/17437))

  * The `getaddressinfo` RPC has had its `label` field deprecated (re-enable for this release using the configuration parameter `-deprecatedrpc=label`). The `labels` field is altered from returning JSON objects to returning a JSON array of label names (re-enable previous behavior for this release using the configuration parameter `-deprecatedrpc=labelspurpose`). Backwards compatibility using the deprecated configuration parameters is expected to be dropped in the 0.21 release. ([#17585](https://github.com/bitcoin/bitcoin/pull/17585), [#17578](https://github.com/bitcoin/bitcoin/pull/17578))

## Documentation changes

  * Bitcoin Core’s automatically-generated source code documentation is now available at https://doxygen.bitcoincore.org. ([#17596](https://github.com/bitcoin/bitcoin/pull/17596))

# Low-level changes

## Utilities

  * The `bitcoin-cli` utility used with the `-getinfo` parameter now returns a `headers` field with the number of downloaded block headers on the best headers chain (similar to the `blocks` field that is also returned) and a `verificationprogress` field that estimates how much of the best block chain has been synced by the local node. The information returned no longer includes the `protocolversion`, `walletversion`, and `keypoololdest` fields. ([#17302](https://github.com/bitcoin/bitcoin/pull/17302), [#17650](https://github.com/bitcoin/bitcoin/pull/17650))

  * The `bitcoin-cli` utility now accepts a `-stdinwalletpassphrase` parameter that can be used when calling the `walletpassphrase` and `walletpassphrasechange` RPCs to read the passphrase from standard input without echoing it to the terminal, improving security against anyone who can look at your screen. The existing `-stdinrpcpass` parameter is also updated to not echo the passphrase. ([#13716](https://github.com/bitcoin/bitcoin/pull/13716))

## Command line

  * Command line options prefixed with main/test/regtest network names like `-main.port=8333` `-test.server=1` previously were allowed but ignored. Now they trigger “Invalid parameter” errors on startup. ([#17482](https://github.com/bitcoin/bitcoin/pull/17482))

## New RPCs

  * The `dumptxoutset` RPC outputs a serialized snapshot of the current UTXO set. A script is provided in the `contrib/devtools` directory for generating a snapshot of the UTXO set at a particular block height. ([#16899](https://github.com/bitcoin/bitcoin/pull/16899))

  * The `generatetodescriptor` RPC allows testers using regtest mode to generate blocks that pay an arbitrary output script descriptor. ([#16943](https://github.com/bitcoin/bitcoin/pull/16943))

## Updated RPCs

  * The `verifychain` RPC default values are now static instead of depending on the command line options or configuration file (`-checklevel`, and `-checkblocks`). Users can pass in the RPC arguments explicitly when they don’t want to rely on the default values. ([#18541](https://github.com/bitcoin/bitcoin/pull/18541))

  * The `getblockchaininfo` RPC’s `verificationprogress` field will no longer report values higher than 1. Previously it would occasionally report the chain was more than 100% verified. ([#17328](https://github.com/bitcoin/bitcoin/pull/17328))

## Tests

  * It is now an error to use an unqualified `walletdir=path` setting in the config file if running on testnet or regtest networks. The setting now needs to be qualified as `chain.walletdir=path` or placed in the appropriate `[chain]` section. ([#17447](https://github.com/bitcoin/bitcoin/pull/17447))

  * `-fallbackfee` was 0 (disabled) by default for the main chain, but 0.0002 by default for the test chains. Now it is 0 by default for all chains. Testnet and regtest users will have to add `fallbackfee=0.0002` to their configuration if they weren’t setting it and they want it to keep working like before. ([#16524](https://github.com/bitcoin/bitcoin/pull/16524))

## Build system

  * Support is provided for building with the Android Native Development Kit (NDK). ([#16110](https://github.com/bitcoin/bitcoin/pull/16110))

# 0.20.0 change log

### Mining

  * [#18742](https://github.com/bitcoin/bitcoin/pull/18742) miner: Avoid stack-use-after-return in validationinterface (MarcoFalke)

### Block and transaction handling

  * [#15283](https://github.com/bitcoin/bitcoin/pull/15283) log: Fix UB with bench on genesis block (instagibbs)
  * [#16507](https://github.com/bitcoin/bitcoin/pull/16507) feefilter: Compute the absolute fee rather than stored rate (instagibbs)
  * [#16688](https://github.com/bitcoin/bitcoin/pull/16688) log: Add validation interface logging (jkczyz)
  * [#16805](https://github.com/bitcoin/bitcoin/pull/16805) log: Add timing information to FlushStateToDisk() (jamesob)
  * [#16902](https://github.com/bitcoin/bitcoin/pull/16902) O(1) `OP_IF/NOTIF/ELSE/ENDIF` script implementation (sipa)
  * [#16945](https://github.com/bitcoin/bitcoin/pull/16945) introduce CChainState::GetCoinsCacheSizeState (jamesob)
  * [#16974](https://github.com/bitcoin/bitcoin/pull/16974) Walk pindexBestHeader back to ChainActive().Tip() if it is invalid (TheBlueMatt)
  * [#17004](https://github.com/bitcoin/bitcoin/pull/17004) Remove REJECT code from CValidationState (jnewbery)
  * [#17080](https://github.com/bitcoin/bitcoin/pull/17080) Explain why `fCheckDuplicateInputs` can not be skipped and remove it (MarcoFalke)
  * [#17328](https://github.com/bitcoin/bitcoin/pull/17328) GuessVerificationProgress: cap the ratio to 1 (darosior)
  * [#17399](https://github.com/bitcoin/bitcoin/pull/17399) Templatize ValidationState instead of subclassing (jkczyz)
  * [#17407](https://github.com/bitcoin/bitcoin/pull/17407) node: Add reference to mempool in NodeContext (MarcoFalke)
  * [#17708](https://github.com/bitcoin/bitcoin/pull/17708) prevector: Avoid misaligned member accesses (ajtowns)
  * [#17850](https://github.com/bitcoin/bitcoin/pull/17850),[#17896](https://github.com/bitcoin/bitcoin/pull/17896),[#17957](https://github.com/bitcoin/bitcoin/pull/17957),[#18021](https://github.com/bitcoin/bitcoin/pull/18021),[#18021](https://github.com/bitcoin/bitcoin/pull/18021),[#18112](https://github.com/bitcoin/bitcoin/pull/18112) Serialization improvements (sipa)
  * [#17925](https://github.com/bitcoin/bitcoin/pull/17925) Improve UpdateTransactionsFromBlock with Epochs (JeremyRubin)
  * [#18002](https://github.com/bitcoin/bitcoin/pull/18002) Abstract out script execution out of `VerifyWitnessProgram()` (sipa)
  * [#18388](https://github.com/bitcoin/bitcoin/pull/18388) Make VerifyWitnessProgram use a Span stack (sipa)
  * [#18433](https://github.com/bitcoin/bitcoin/pull/18433) serialization: prevent int overflow for big Coin::nHeight (pierreN)
  * [#18500](https://github.com/bitcoin/bitcoin/pull/18500) chainparams: Bump assumed valid hash (MarcoFalke)
  * [#18551](https://github.com/bitcoin/bitcoin/pull/18551) Do not clear validationinterface entries being executed (sipa)

### P2P protocol and network code

  * [#15437](https://github.com/bitcoin/bitcoin/pull/15437) Remove BIP61 reject messages (MarcoFalke)
  * [#16702](https://github.com/bitcoin/bitcoin/pull/16702) Supply and use asmap to improve IP bucketing in addrman (naumenkogs)
  * [#16851](https://github.com/bitcoin/bitcoin/pull/16851) Continue relaying transactions after they expire from mapRelay (ajtowns)
  * [#17164](https://github.com/bitcoin/bitcoin/pull/17164) Avoid allocating memory for addrKnown where we don’t need it (naumenkogs)
  * [#17243](https://github.com/bitcoin/bitcoin/pull/17243) tools: add PoissonNextSend method that returns mockable time (amitiuttarwar)
  * [#17251](https://github.com/bitcoin/bitcoin/pull/17251) SocketHandler logs peer id for close and disconnect (Sjors)
  * [#17573](https://github.com/bitcoin/bitcoin/pull/17573) Seed RNG with precision timestamps on receipt of net messages (TheBlueMatt)
  * [#17624](https://github.com/bitcoin/bitcoin/pull/17624) Fix an uninitialized read in ProcessMessage(…, “tx”, …) when receiving a transaction we already have (practicalswift)
  * [#17754](https://github.com/bitcoin/bitcoin/pull/17754) Don’t allow resolving of std::string with embedded NUL characters. Add tests (practicalswift)
  * [#17758](https://github.com/bitcoin/bitcoin/pull/17758) Fix CNetAddr::IsRFC2544 comment + tests (tynes)
  * [#17812](https://github.com/bitcoin/bitcoin/pull/17812) config, net, test: Asmap feature refinements and functional tests (jonatack)
  * [#17951](https://github.com/bitcoin/bitcoin/pull/17951) Use rolling bloom filter of recent block txs for AlreadyHave() check (sdaftuar)
  * [#17985](https://github.com/bitcoin/bitcoin/pull/17985) Remove forcerelay of rejected txs (MarcoFalke)
  * [#18023](https://github.com/bitcoin/bitcoin/pull/18023) Fix some asmap issues (sipa)
  * [#18054](https://github.com/bitcoin/bitcoin/pull/18054) Reference instead of copy in BlockConnected range loop (jonatack)
  * [#18376](https://github.com/bitcoin/bitcoin/pull/18376) Fix use-after-free in tests (vasild)
  * [#18454](https://github.com/bitcoin/bitcoin/pull/18454) Make addr relay mockable, add test (MarcoFalke)
  * [#18458](https://github.com/bitcoin/bitcoin/pull/18458) Add missing `cs_vNodes` lock (MarcoFalke)
  * [#18506](https://github.com/bitcoin/bitcoin/pull/18506) Hardcoded seeds update for 0.20 (laanwj)
  * [#18808](https://github.com/bitcoin/bitcoin/pull/18808) Drop unknown types in getdata (jnewbery)
  * [#18962](https://github.com/bitcoin/bitcoin/pull/18962) Only send a getheaders for one block in an INV (jnewbery)

### Wallet

  * [#13339](https://github.com/bitcoin/bitcoin/pull/13339) Replace %w by wallet name in -walletnotify script (promag)
  * [#15931](https://github.com/bitcoin/bitcoin/pull/15931) Remove GetDepthInMainChain dependency on locked chain interface (ariard)
  * [#16373](https://github.com/bitcoin/bitcoin/pull/16373) bumpfee: Return PSBT when wallet has privkeys disabled (instagibbs)
  * [#16524](https://github.com/bitcoin/bitcoin/pull/16524) Disable -fallbackfee by default (jtimon)
  * [#16766](https://github.com/bitcoin/bitcoin/pull/16766) Make IsTrusted scan parents recursively (JeremyRubin)
  * [#16884](https://github.com/bitcoin/bitcoin/pull/16884) Change default address type to bech32 (instagibbs)
  * [#16911](https://github.com/bitcoin/bitcoin/pull/16911) Only check the hash of transactions loaded from disk (achow101)
  * [#16923](https://github.com/bitcoin/bitcoin/pull/16923) Handle duplicate fileid exception (promag)
  * [#17056](https://github.com/bitcoin/bitcoin/pull/17056) descriptors: Introduce sortedmulti descriptor (achow101)
  * [#17070](https://github.com/bitcoin/bitcoin/pull/17070) Avoid showing GUI popups on RPC errors (MarcoFalke)
  * [#17138](https://github.com/bitcoin/bitcoin/pull/17138) Remove wallet access to some node arguments (jnewbery)
  * [#17237](https://github.com/bitcoin/bitcoin/pull/17237) LearnRelatedScripts only if KeepDestination (promag)
  * [#17260](https://github.com/bitcoin/bitcoin/pull/17260) Split some CWallet functions into new LegacyScriptPubKeyMan (achow101)
  * [#17261](https://github.com/bitcoin/bitcoin/pull/17261) Make ScriptPubKeyMan an actual interface and the wallet to have multiple (achow101)
  * [#17290](https://github.com/bitcoin/bitcoin/pull/17290) Enable BnB coin selection for preset inputs and subtract fee from outputs (achow101)
  * [#17373](https://github.com/bitcoin/bitcoin/pull/17373) Various fixes and cleanup to keypool handling in LegacyScriptPubKeyMan and CWallet (achow101)
  * [#17410](https://github.com/bitcoin/bitcoin/pull/17410) Rename `db` log category to `walletdb` (like `coindb`) (laanwj)
  * [#17444](https://github.com/bitcoin/bitcoin/pull/17444) Avoid showing GUI popups on RPC errors (take 2) (MarcoFalke)
  * [#17447](https://github.com/bitcoin/bitcoin/pull/17447) Make -walletdir network only (promag)
  * [#17537](https://github.com/bitcoin/bitcoin/pull/17537) Cleanup and move opportunistic and superfluous TopUp()s (achow101)
  * [#17553](https://github.com/bitcoin/bitcoin/pull/17553) Remove out of date comments for CalculateMaximumSignedTxSize (instagibbs)
  * [#17568](https://github.com/bitcoin/bitcoin/pull/17568) Fix when sufficient preset inputs and subtractFeeFromOutputs (achow101)
  * [#17677](https://github.com/bitcoin/bitcoin/pull/17677) Activate watchonly wallet behavior for LegacySPKM only (instagibbs)
  * [#17719](https://github.com/bitcoin/bitcoin/pull/17719) Document better -keypool as a look-ahead safety mechanism (ariard)
  * [#17843](https://github.com/bitcoin/bitcoin/pull/17843) Reset reused transactions cache (fjahr)
  * [#17889](https://github.com/bitcoin/bitcoin/pull/17889) Improve CWallet:MarkDestinationsDirty (promag)
  * [#18034](https://github.com/bitcoin/bitcoin/pull/18034) Get the OutputType for a descriptor (achow101)
  * [#18067](https://github.com/bitcoin/bitcoin/pull/18067) Improve LegacyScriptPubKeyMan::CanProvide script recognition (ryanofsky)
  * [#18115](https://github.com/bitcoin/bitcoin/pull/18115) Pass in transactions and messages for signing instead of exporting the private keys (achow101)
  * [#18192](https://github.com/bitcoin/bitcoin/pull/18192),[#18546](https://github.com/bitcoin/bitcoin/pull/18546) Bugfix: Wallet: Safely deal with change in the address book (luke-jr)
  * [#18204](https://github.com/bitcoin/bitcoin/pull/18204) descriptors: Improve descriptor cache and cache xpubs (achow101)
  * [#18274](https://github.com/bitcoin/bitcoin/pull/18274) rpc/wallet: Initialize nFeeRequired to avoid using garbage value on failure (kallewoof)
  * [#18312](https://github.com/bitcoin/bitcoin/pull/18312) Remove deprecated fee bumping by totalFee (jonatack)
  * [#18338](https://github.com/bitcoin/bitcoin/pull/18338) Fix wallet unload race condition (promag)

### RPC and other APIs

  * [#12763](https://github.com/bitcoin/bitcoin/pull/12763) Add RPC Whitelist Feature from [#12248](https://github.com/bitcoin/bitcoin/pull/12248) (JeremyRubin)
  * [#13716](https://github.com/bitcoin/bitcoin/pull/13716) cli: `-stdinwalletpassphrase` and non-echo stdin passwords (kallewoof)
  * [#16689](https://github.com/bitcoin/bitcoin/pull/16689) Add missing fields to wallet rpc help output (ariard)
  * [#16821](https://github.com/bitcoin/bitcoin/pull/16821) Fix bug where duplicate PSBT keys are accepted (erasmospunk)
  * [#16899](https://github.com/bitcoin/bitcoin/pull/16899) UTXO snapshot creation (dumptxoutset)
  * [#17156](https://github.com/bitcoin/bitcoin/pull/17156) psbt: Check that various indexes and amounts are within bounds (achow101)
  * [#17264](https://github.com/bitcoin/bitcoin/pull/17264) Set default bip32derivs to true for psbt methods (Sjors)
  * [#17283](https://github.com/bitcoin/bitcoin/pull/17283) improve getaddressinfo test coverage, help, code docs (jonatack)
  * [#17302](https://github.com/bitcoin/bitcoin/pull/17302) cli: Add “headers” and “verificationprogress” to -getinfo (laanwj)
  * [#17318](https://github.com/bitcoin/bitcoin/pull/17318) replace asserts in RPC code with `CHECK_NONFATAL` and add linter (adamjonas)
  * [#17437](https://github.com/bitcoin/bitcoin/pull/17437) Expose block height of wallet transactions (promag)
  * [#17519](https://github.com/bitcoin/bitcoin/pull/17519) Remove unused `COINBASE_FLAGS` (narula)
  * [#17578](https://github.com/bitcoin/bitcoin/pull/17578) Simplify getaddressinfo labels, deprecate previous behavior (jonatack)
  * [#17585](https://github.com/bitcoin/bitcoin/pull/17585) deprecate getaddressinfo label (jonatack)
  * [#17746](https://github.com/bitcoin/bitcoin/pull/17746) Remove vector copy from listtransactions (promag)
  * [#17809](https://github.com/bitcoin/bitcoin/pull/17809) Auto-format RPCResult (MarcoFalke)
  * [#18032](https://github.com/bitcoin/bitcoin/pull/18032) Output a descriptor in createmultisig and addmultisigaddress (achow101)
  * [#18122](https://github.com/bitcoin/bitcoin/pull/18122) Update validateaddress RPCExamples to bech32 (theStack)
  * [#18208](https://github.com/bitcoin/bitcoin/pull/18208) Change RPCExamples to bech32 (yusufsahinhamza)
  * [#18268](https://github.com/bitcoin/bitcoin/pull/18268) Remove redundant types from descriptions (docallag)
  * [#18346](https://github.com/bitcoin/bitcoin/pull/18346) Document an RPCResult for all calls; Enforce at compile time (MarcoFalke)
  * [#18396](https://github.com/bitcoin/bitcoin/pull/18396) Add missing HelpExampleRpc for getblockfilter (theStack)
  * [#18398](https://github.com/bitcoin/bitcoin/pull/18398) Fix broken RPCExamples for waitforblock(height) (theStack)
  * [#18444](https://github.com/bitcoin/bitcoin/pull/18444) Remove final comma for last entry of fixed-size arrays/objects in RPCResult (luke-jr)
  * [#18459](https://github.com/bitcoin/bitcoin/pull/18459) Remove unused getbalances() code (jonatack)
  * [#18484](https://github.com/bitcoin/bitcoin/pull/18484) Correctly compute redeemScript from witnessScript for signrawtransaction (achow101)
  * [#18487](https://github.com/bitcoin/bitcoin/pull/18487) Fix rpcRunLater race in walletpassphrase (promag)
  * [#18499](https://github.com/bitcoin/bitcoin/pull/18499) Make rpc documentation not depend on call-time rpc args (MarcoFalke)
  * [#18532](https://github.com/bitcoin/bitcoin/pull/18532) Avoid initialization-order-fiasco on static CRPCCommand tables (MarcoFalke)
  * [#18541](https://github.com/bitcoin/bitcoin/pull/18541) Make verifychain default values static, not depend on global args (MarcoFalke)
  * [#18809](https://github.com/bitcoin/bitcoin/pull/18809) Do not advertise dumptxoutset as a way to flush the chainstate (MarcoFalke)
  * [#18814](https://github.com/bitcoin/bitcoin/pull/18814) Relock wallet only if most recent callback (promag)

### GUI

  * [#15023](https://github.com/bitcoin/bitcoin/pull/15023) Restore RPC Console to non-wallet tray icon menu (luke-jr)
  * [#15084](https://github.com/bitcoin/bitcoin/pull/15084) Don’t disable the sync overlay when wallet is disabled (benthecarman)
  * [#15098](https://github.com/bitcoin/bitcoin/pull/15098) Show addresses for “SendToSelf” transactions (hebasto)
  * [#15756](https://github.com/bitcoin/bitcoin/pull/15756) Add shortcuts for tab tools (promag)
  * [#16944](https://github.com/bitcoin/bitcoin/pull/16944) create PSBT with watch-only wallet (Sjors)
  * [#16964](https://github.com/bitcoin/bitcoin/pull/16964) Change sendcoins dialogue Yes to Send (instagibbs)
  * [#17068](https://github.com/bitcoin/bitcoin/pull/17068) Always generate `bitcoinstrings.cpp` on `make translate` (D4nte)
  * [#17096](https://github.com/bitcoin/bitcoin/pull/17096) Rename debug window (Zero-1729)
  * [#17105](https://github.com/bitcoin/bitcoin/pull/17105) Make RPCConsole::TabTypes an enum class (promag)
  * [#17125](https://github.com/bitcoin/bitcoin/pull/17125) Add toolTip and placeholderText to sign message fields (dannmat)
  * [#17165](https://github.com/bitcoin/bitcoin/pull/17165) Remove BIP70 support (fanquake)
  * [#17180](https://github.com/bitcoin/bitcoin/pull/17180) Improved tooltip for send amount field (JeremyCrookshank)
  * [#17186](https://github.com/bitcoin/bitcoin/pull/17186) Add placeholder text to the sign message field (Danny-Scott)
  * [#17195](https://github.com/bitcoin/bitcoin/pull/17195) Send amount placeholder value (JeremyCrookshank)
  * [#17226](https://github.com/bitcoin/bitcoin/pull/17226) Fix payAmount tooltip in SendCoinsEntry (promag)
  * [#17360](https://github.com/bitcoin/bitcoin/pull/17360) Cleaning up hide button tool tip (Danny-Scott)
  * [#17446](https://github.com/bitcoin/bitcoin/pull/17446) Changed tooltip for ‘Label’ & ‘Message’ text fields to be more clear (dannmat)
  * [#17453](https://github.com/bitcoin/bitcoin/pull/17453) Fix intro dialog labels when the prune button is toggled (hebasto)
  * [#17474](https://github.com/bitcoin/bitcoin/pull/17474) Bugfix: GUI: Recognise `NETWORK_LIMITED` in formatServicesStr (luke-jr)
  * [#17492](https://github.com/bitcoin/bitcoin/pull/17492) Bump fee returns PSBT on clipboard for watchonly-only wallets (instagibbs)
  * [#17567](https://github.com/bitcoin/bitcoin/pull/17567) Remove macOS start on login code (fanquake)
  * [#17587](https://github.com/bitcoin/bitcoin/pull/17587) Show watch-only balance in send screen (Sjors)
  * [#17694](https://github.com/bitcoin/bitcoin/pull/17694) Disable 3rd-party tx-urls when wallet disabled (brakmic)
  * [#17696](https://github.com/bitcoin/bitcoin/pull/17696) Force set nPruneSize in QSettings after the intro dialog (hebasto)
  * [#17702](https://github.com/bitcoin/bitcoin/pull/17702) Move static placeholder texts to forms (laanwj)
  * [#17826](https://github.com/bitcoin/bitcoin/pull/17826) Log Qt related info (hebasto)
  * [#17886](https://github.com/bitcoin/bitcoin/pull/17886) Restore English translation option (achow101)
  * [#17906](https://github.com/bitcoin/bitcoin/pull/17906) Set CConnman byte counters earlier to avoid uninitialized reads (ryanofsky)
  * [#17935](https://github.com/bitcoin/bitcoin/pull/17935) Hide HD & encryption icons when no wallet loaded (brakmic)
  * [#17998](https://github.com/bitcoin/bitcoin/pull/17998) Shortcut to close ModalOverlay (emilengler)
  * [#18007](https://github.com/bitcoin/bitcoin/pull/18007) Bugfix: GUI: Hide the HD/encrypt icons earlier so they get re-shown if another wallet is open (luke-jr)
  * [#18060](https://github.com/bitcoin/bitcoin/pull/18060) Drop PeerTableModel dependency to ClientModel (promag)
  * [#18062](https://github.com/bitcoin/bitcoin/pull/18062) Fix unintialized WalletView::progressDialog (promag)
  * [#18091](https://github.com/bitcoin/bitcoin/pull/18091) Pass clientmodel changes from walletframe to walletviews (jonasschnelli)
  * [#18101](https://github.com/bitcoin/bitcoin/pull/18101) Fix deprecated QCharRef usage (hebasto)
  * [#18121](https://github.com/bitcoin/bitcoin/pull/18121) Throttle GUI update pace when -reindex (hebasto)
  * [#18123](https://github.com/bitcoin/bitcoin/pull/18123) Fix race in WalletModel::pollBalanceChanged (ryanofsky)
  * [#18160](https://github.com/bitcoin/bitcoin/pull/18160) Avoid Wallet::GetBalance in WalletModel::pollBalanceChanged (promag)
  * [#18360](https://github.com/bitcoin/bitcoin/pull/18360) Bump transifex slug and update English translations for 0.20 (laanwj)
  * [#18402](https://github.com/bitcoin/bitcoin/pull/18402) Display mapped AS in peers info window (jonatack)
  * [#18492](https://github.com/bitcoin/bitcoin/pull/18492) Translations update pre-branch (laanwj)
  * [#18549](https://github.com/bitcoin/bitcoin/pull/18549) Fix Window -> Minimize menu item (hebasto)
  * [#18578](https://github.com/bitcoin/bitcoin/pull/18578) Fix leak in CoinControlDialog::updateView (promag)
  * [#18894](https://github.com/bitcoin/bitcoin/pull/18894) Fix manual coin control with multiple wallets loaded (promag)

### Build system

  * [#16667](https://github.com/bitcoin/bitcoin/pull/16667) Remove mingw linker workaround from win gitian descriptor (fanquake)
  * [#16669](https://github.com/bitcoin/bitcoin/pull/16669) Use new fork of osslsigncode for windows gitian signing (fanquake)
  * [#16949](https://github.com/bitcoin/bitcoin/pull/16949) Only pass –disable-dependency-tracking to packages that understand it (fanquake)
  * [#17008](https://github.com/bitcoin/bitcoin/pull/17008) Bump libevent to 2.1.11 in depends (stefanwouldgo)
  * [#17029](https://github.com/bitcoin/bitcoin/pull/17029) gitian: Various improvements for windows descriptor (dongcarl)
  * [#17033](https://github.com/bitcoin/bitcoin/pull/17033) Disable _FORTIFY_SOURCE when enable-debug (achow101)
  * [#17057](https://github.com/bitcoin/bitcoin/pull/17057) Switch to upstream libdmg-hfsplus (fanquake)
  * [#17066](https://github.com/bitcoin/bitcoin/pull/17066) Remove workaround for ancient libtool (hebasto)
  * [#17074](https://github.com/bitcoin/bitcoin/pull/17074) Added double quotes (mztriz)
  * [#17087](https://github.com/bitcoin/bitcoin/pull/17087) Add variable printing target to Makefiles (dongcarl)
  * [#17118](https://github.com/bitcoin/bitcoin/pull/17118) depends macOS: point –sysroot to SDK (Sjors)
  * [#17231](https://github.com/bitcoin/bitcoin/pull/17231) Fix boost mac cross build with clang 9+ (theuni)
  * [#17265](https://github.com/bitcoin/bitcoin/pull/17265) Remove OpenSSL (fanquake)
  * [#17284](https://github.com/bitcoin/bitcoin/pull/17284) Update retry to current version (RandyMcMillan)
  * [#17308](https://github.com/bitcoin/bitcoin/pull/17308) nsis: Write to correct filename in first place (dongcarl)
  * [#17324](https://github.com/bitcoin/bitcoin/pull/17324),[#18099](https://github.com/bitcoin/bitcoin/pull/18099) Update univalue subtree (MarcoFalke)
  * [#17398](https://github.com/bitcoin/bitcoin/pull/17398) Update leveldb to 1.22+ (laanwj)
  * [#17409](https://github.com/bitcoin/bitcoin/pull/17409) Avoid hardcoded libfaketime dir in gitian (MarcoFalke)
  * [#17466](https://github.com/bitcoin/bitcoin/pull/17466) Fix C{,XX} pickup (dongcarl)
  * [#17483](https://github.com/bitcoin/bitcoin/pull/17483) Set gitian arch back to amd64 (MarcoFalke)
  * [#17486](https://github.com/bitcoin/bitcoin/pull/17486) Make Travis catch unused variables (Sjors)
  * [#17538](https://github.com/bitcoin/bitcoin/pull/17538) Bump minimum libc to 2.17 for release binaries (fanquake)
  * [#17542](https://github.com/bitcoin/bitcoin/pull/17542) Create test utility library from src/test/util/ (brakmic)
  * [#17545](https://github.com/bitcoin/bitcoin/pull/17545) Remove libanl.so.1 from ALLOWED_LIBRARIES (fanquake)
  * [#17547](https://github.com/bitcoin/bitcoin/pull/17547) Fix configure report about qr (hebasto)
  * [#17569](https://github.com/bitcoin/bitcoin/pull/17569) Allow export of environ symbols and work around rv64 toolchain issue (laanwj)
  * [#17647](https://github.com/bitcoin/bitcoin/pull/17647) lcov: filter depends from coverage reports (nijynot)
  * [#17658](https://github.com/bitcoin/bitcoin/pull/17658) Add ability to skip building qrencode (fanquake)
  * [#17678](https://github.com/bitcoin/bitcoin/pull/17678) Support for S390X and POWER targets (MarcoFalke)
  * [#17682](https://github.com/bitcoin/bitcoin/pull/17682) util: Update tinyformat to upstream (laanwj)
  * [#17698](https://github.com/bitcoin/bitcoin/pull/17698) Don’t configure `xcb_proto` (fanquake)
  * [#17730](https://github.com/bitcoin/bitcoin/pull/17730) Remove Qt networking features (fanquake)
  * [#17738](https://github.com/bitcoin/bitcoin/pull/17738) Remove linking librt for backwards compatibility (fanquake)
  * [#17740](https://github.com/bitcoin/bitcoin/pull/17740) Remove configure checks for win libraries we don’t link against (fanquake)
  * [#17741](https://github.com/bitcoin/bitcoin/pull/17741) Included `test_bitcoin-qt` in msvc build (sipsorcery)
  * [#17756](https://github.com/bitcoin/bitcoin/pull/17756) Remove `WINDOWS_BITS` from build system (fanquake)
  * [#17769](https://github.com/bitcoin/bitcoin/pull/17769) Set `AC_PREREQ` to 2.69 (fanquake)
  * [#17880](https://github.com/bitcoin/bitcoin/pull/17880) Add -Wdate-time to Werror flags (fanquake)
  * [#17910](https://github.com/bitcoin/bitcoin/pull/17910) Remove double `LIBBITCOIN_SERVER` linking (fanquake)
  * [#17928](https://github.com/bitcoin/bitcoin/pull/17928) Consistent use of package variable (Bushstar)
  * [#17933](https://github.com/bitcoin/bitcoin/pull/17933) guix: Pin Guix using `guix time-machine` (dongcarl)
  * [#17948](https://github.com/bitcoin/bitcoin/pull/17948) pass -fno-ident in Windows gitian descriptor (fanquake)
  * [#18003](https://github.com/bitcoin/bitcoin/pull/18003) Remove –large-address-aware linker flag (fanquake)
  * [#18004](https://github.com/bitcoin/bitcoin/pull/18004) Don’t embed a build-id when building libdmg-hfsplus (fanquake)
  * [#18051](https://github.com/bitcoin/bitcoin/pull/18051) Fix behavior when `ALLOW_HOST_PACKAGES` unset (hebasto)
  * [#18059](https://github.com/bitcoin/bitcoin/pull/18059) Add missing attributes to Win installer (fanquake)
  * [#18104](https://github.com/bitcoin/bitcoin/pull/18104) Skip i686 build by default in guix and gitian (MarcoFalke)
  * [#18107](https://github.com/bitcoin/bitcoin/pull/18107) Add `cov_fuzz` target (MarcoFalke)
  * [#18135](https://github.com/bitcoin/bitcoin/pull/18135) Add –enable-determinism configure flag (fanquake)
  * [#18145](https://github.com/bitcoin/bitcoin/pull/18145) Add Wreturn-type to Werror flags, check on more Travis machines (Sjors)
  * [#18264](https://github.com/bitcoin/bitcoin/pull/18264) Remove Boost Chrono (fanquake)
  * [#18290](https://github.com/bitcoin/bitcoin/pull/18290) Set minimum Automake version to 1.13 (hebasto)
  * [#18320](https://github.com/bitcoin/bitcoin/pull/18320) guix: Remove now-unnecessary gcc make flag (dongcarl)
  * [#18331](https://github.com/bitcoin/bitcoin/pull/18331) Use git archive as source tarball (hebasto)
  * [#18397](https://github.com/bitcoin/bitcoin/pull/18397) Fix libevent linking for `bench_bitcoin` binary (hebasto)
  * [#18426](https://github.com/bitcoin/bitcoin/pull/18426) scripts: `Previous_release`: improve behaviour on failed download (theStack)
  * [#18429](https://github.com/bitcoin/bitcoin/pull/18429) Remove double `LIBBITCOIN_SERVER` from bench-Makefile (brakmic)
  * [#18528](https://github.com/bitcoin/bitcoin/pull/18528) Create `test_fuzz` library from src/test/fuzz/fuzz.cpp (brakmic)
  * [#18558](https://github.com/bitcoin/bitcoin/pull/18558) Fix boost detection for arch armv7l (hebasto)
  * [#18598](https://github.com/bitcoin/bitcoin/pull/18598) gitian: Add missing automake package to gitian-win-signer.yml (achow101)
  * [#18676](https://github.com/bitcoin/bitcoin/pull/18676) Check libevent minimum version in configure script (hebasto)
  * [#18945](https://github.com/bitcoin/bitcoin/pull/18945) Ensure source tarball has leading directory name (laanwj)

### Platform support

  * [#16110](https://github.com/bitcoin/bitcoin/pull/16110) Add Android NDK support (icota)
  * [#16392](https://github.com/bitcoin/bitcoin/pull/16392) macOS toolchain update (fanquake)
  * [#16569](https://github.com/bitcoin/bitcoin/pull/16569) Increase init file stop timeout (setpill)
  * [#17151](https://github.com/bitcoin/bitcoin/pull/17151) Remove OpenSSL PRNG seeding (Windows, Qt only) (fanquake)
  * [#17365](https://github.com/bitcoin/bitcoin/pull/17365) Update README.md with working Android targets and API levels (icota)
  * [#17521](https://github.com/bitcoin/bitcoin/pull/17521) Only use D-Bus with Qt on linux (fanquake)
  * [#17550](https://github.com/bitcoin/bitcoin/pull/17550) Set minimum supported macOS to 10.12 (fanquake)
  * [#17592](https://github.com/bitcoin/bitcoin/pull/17592) Appveyor install libevent[thread] vcpkg (sipsorcery)
  * [#17660](https://github.com/bitcoin/bitcoin/pull/17660) Remove deprecated key from macOS Info.plist (fanquake)
  * [#17663](https://github.com/bitcoin/bitcoin/pull/17663) Pass `-dead_strip_dylibs` to ld on macOS (fanquake)
  * [#17676](https://github.com/bitcoin/bitcoin/pull/17676) Don’t use OpenGL in Qt on macOS (fanquake)
  * [#17686](https://github.com/bitcoin/bitcoin/pull/17686) Add `-bind_at_load` to macOS hardened LDFLAGS (fanquake)
  * [#17787](https://github.com/bitcoin/bitcoin/pull/17787) scripts: Add macho pie check to security-check.py (fanquake)
  * [#17800](https://github.com/bitcoin/bitcoin/pull/17800) random: don’t special case clock usage on macOS (fanquake)
  * [#17863](https://github.com/bitcoin/bitcoin/pull/17863) scripts: Add macho dylib checks to symbol-check.py (fanquake)
  * [#17899](https://github.com/bitcoin/bitcoin/pull/17899) msvc: Ignore msvc linker warning and update to msvc build instructions (sipsorcery)
  * [#17916](https://github.com/bitcoin/bitcoin/pull/17916) windows: Enable heap terminate-on-corruption (fanquake)
  * [#18082](https://github.com/bitcoin/bitcoin/pull/18082) logging: Enable `thread_local` usage on macos (fanquake)
  * [#18108](https://github.com/bitcoin/bitcoin/pull/18108) Fix `.gitignore` policy in `build_msvc` directory (hebasto)
  * [#18295](https://github.com/bitcoin/bitcoin/pull/18295) scripts: Add macho lazy bindings check to security-check.py (fanquake)
  * [#18358](https://github.com/bitcoin/bitcoin/pull/18358) util: Fix compilation with mingw-w64 7.0.0 (fanquake)
  * [#18359](https://github.com/bitcoin/bitcoin/pull/18359) Fix sysctl() detection on macOS (fanquake)
  * [#18364](https://github.com/bitcoin/bitcoin/pull/18364) random: remove getentropy() fallback for macOS < 10.12 (fanquake)
  * [#18395](https://github.com/bitcoin/bitcoin/pull/18395) scripts: Add pe dylib checking to symbol-check.py (fanquake)
  * [#18415](https://github.com/bitcoin/bitcoin/pull/18415) scripts: Add macho tests to test-security-check.py (fanquake)
  * [#18425](https://github.com/bitcoin/bitcoin/pull/18425) releases: Update with new Windows code signing certificate (achow101)
  * [#18702](https://github.com/bitcoin/bitcoin/pull/18702) Fix ASLR for bitcoin-cli on Windows (fanquake)

### Tests and QA

  * [#12134](https://github.com/bitcoin/bitcoin/pull/12134) Build previous releases and run functional tests (Sjors)
  * [#13693](https://github.com/bitcoin/bitcoin/pull/13693) Add coverage to estimaterawfee and estimatesmartfee (Empact)
  * [#13728](https://github.com/bitcoin/bitcoin/pull/13728) lint: Run the ci lint stage on mac (Empact)
  * [#15443](https://github.com/bitcoin/bitcoin/pull/15443) Add getdescriptorinfo functional test (promag)
  * [#15888](https://github.com/bitcoin/bitcoin/pull/15888) Add `wallet_implicitsegwit` to test the ability to transform keys between address types (luke-jr)
  * [#16540](https://github.com/bitcoin/bitcoin/pull/16540) Add `ASSERT_DEBUG_LOG` to unit test framework (MarcoFalke)
  * [#16597](https://github.com/bitcoin/bitcoin/pull/16597) travis: Run full test suite on native macos (Sjors)
  * [#16681](https://github.com/bitcoin/bitcoin/pull/16681) Use self.chain instead of ‘regtest’ in all current tests (jtimon)
  * [#16786](https://github.com/bitcoin/bitcoin/pull/16786) add unit test for wallet watch-only methods involving PubKeys (theStack)
  * [#16943](https://github.com/bitcoin/bitcoin/pull/16943) Add generatetodescriptor RPC (MarcoFalke)
  * [#16973](https://github.com/bitcoin/bitcoin/pull/16973) Fix `combine_logs.py` for AppVeyor build (mzumsande)
  * [#16975](https://github.com/bitcoin/bitcoin/pull/16975) Show debug log on unit test failure (MarcoFalke)
  * [#16978](https://github.com/bitcoin/bitcoin/pull/16978) Seed test RNG context for each test case, print seed (MarcoFalke)
  * [#17009](https://github.com/bitcoin/bitcoin/pull/17009), [#17018](https://github.com/bitcoin/bitcoin/pull/17018), [#17050](https://github.com/bitcoin/bitcoin/pull/17050), [#17051](https://github.com/bitcoin/bitcoin/pull/17051), [#17071](https://github.com/bitcoin/bitcoin/pull/17071), [#17076](https://github.com/bitcoin/bitcoin/pull/17076), [#17083](https://github.com/bitcoin/bitcoin/pull/17083), [#17093](https://github.com/bitcoin/bitcoin/pull/17093), [#17109](https://github.com/bitcoin/bitcoin/pull/17109), [#17113](https://github.com/bitcoin/bitcoin/pull/17113), [#17136](https://github.com/bitcoin/bitcoin/pull/17136), [#17229](https://github.com/bitcoin/bitcoin/pull/17229), [#17291](https://github.com/bitcoin/bitcoin/pull/17291), [#17357](https://github.com/bitcoin/bitcoin/pull/17357), [#17771](https://github.com/bitcoin/bitcoin/pull/17771), [#17777](https://github.com/bitcoin/bitcoin/pull/17777), [#17917](https://github.com/bitcoin/bitcoin/pull/17917), [#17926](https://github.com/bitcoin/bitcoin/pull/17926), [#17972](https://github.com/bitcoin/bitcoin/pull/17972), [#17989](https://github.com/bitcoin/bitcoin/pull/17989), [#17996](https://github.com/bitcoin/bitcoin/pull/17996), [#18009](https://github.com/bitcoin/bitcoin/pull/18009), [#18029](https://github.com/bitcoin/bitcoin/pull/18029), [#18047](https://github.com/bitcoin/bitcoin/pull/18047), [#18126](https://github.com/bitcoin/bitcoin/pull/18126), [#18176](https://github.com/bitcoin/bitcoin/pull/18176), [#18206](https://github.com/bitcoin/bitcoin/pull/18206), [#18353](https://github.com/bitcoin/bitcoin/pull/18353), [#18363](https://github.com/bitcoin/bitcoin/pull/18363), [#18407](https://github.com/bitcoin/bitcoin/pull/18407), [#18417](https://github.com/bitcoin/bitcoin/pull/18417), [#18423](https://github.com/bitcoin/bitcoin/pull/18423), [#18445](https://github.com/bitcoin/bitcoin/pull/18445), [#18455](https://github.com/bitcoin/bitcoin/pull/18455), [#18565](https://github.com/bitcoin/bitcoin/pull/18565) Add fuzzing harnesses (practicalswift)
  * [#17011](https://github.com/bitcoin/bitcoin/pull/17011) ci: Use busybox utils for one build (MarcoFalke)
  * [#17030](https://github.com/bitcoin/bitcoin/pull/17030) Fix Python Docstring to include all Args (jbampton)
  * [#17041](https://github.com/bitcoin/bitcoin/pull/17041) ci: Run tests on arm (MarcoFalke)
  * [#17069](https://github.com/bitcoin/bitcoin/pull/17069) Pass fuzzing inputs as constant references (practicalswift)
  * [#17091](https://github.com/bitcoin/bitcoin/pull/17091) Add test for loadblock option and linearize scripts (fjahr)
  * [#17108](https://github.com/bitcoin/bitcoin/pull/17108) fix “tx-size-small” errors after default address change (theStack)
  * [#17121](https://github.com/bitcoin/bitcoin/pull/17121) Speed up `wallet_backup` by whitelisting peers (immediate tx relay) (theStack)
  * [#17124](https://github.com/bitcoin/bitcoin/pull/17124) Speed up `wallet_address_types` by whitelisting peers (immediate tx relay) (theStack)
  * [#17140](https://github.com/bitcoin/bitcoin/pull/17140) Fix bug in `blockfilter_index_tests` (jimpo)
  * [#17199](https://github.com/bitcoin/bitcoin/pull/17199) use default address type (bech32) for `wallet_bumpfee` tests (theStack)
  * [#17205](https://github.com/bitcoin/bitcoin/pull/17205) ci: Enable address sanitizer (asan) stack-use-after-return checking (practicalswift)
  * [#17206](https://github.com/bitcoin/bitcoin/pull/17206) Add testcase to simulate bitcoin schema in leveldb (adamjonas)
  * [#17209](https://github.com/bitcoin/bitcoin/pull/17209) Remove no longer needed UBSan suppressions (issues fixed). Add documentation (practicalswift)
  * [#17220](https://github.com/bitcoin/bitcoin/pull/17220) Add unit testing for the CompressScript function (adamjonas)
  * [#17225](https://github.com/bitcoin/bitcoin/pull/17225) Test serialisation as part of deserialisation fuzzing. Test round-trip equality where possible (practicalswift)
  * [#17228](https://github.com/bitcoin/bitcoin/pull/17228) Add RegTestingSetup to `setup_common` (MarcoFalke)
  * [#17233](https://github.com/bitcoin/bitcoin/pull/17233) travis: Run unit and functional tests on native arm (MarcoFalke)
  * [#17235](https://github.com/bitcoin/bitcoin/pull/17235) Skip unnecessary fuzzer initialisation. Hold ECCVerifyHandle only when needed (practicalswift)
  * [#17240](https://github.com/bitcoin/bitcoin/pull/17240) ci: Disable functional tests on mac host (MarcoFalke)
  * [#17254](https://github.com/bitcoin/bitcoin/pull/17254) Fix `script_p2sh_tests` `OP_PUSHBACK2/4` missing (adamjonas)
  * [#17267](https://github.com/bitcoin/bitcoin/pull/17267) bench: Fix negative values and zero for -evals flag (nijynot)
  * [#17275](https://github.com/bitcoin/bitcoin/pull/17275) pubkey: Assert CPubKey’s ECCVerifyHandle precondition (practicalswift)
  * [#17288](https://github.com/bitcoin/bitcoin/pull/17288) Added TestWrapper class for interactive Python environments (jachiang)
  * [#17292](https://github.com/bitcoin/bitcoin/pull/17292) Add new mempool benchmarks for a complex pool (JeremyRubin)
  * [#17299](https://github.com/bitcoin/bitcoin/pull/17299) add reason checks for non-standard txs in `test_IsStandard` (theStack)
  * [#17322](https://github.com/bitcoin/bitcoin/pull/17322) Fix input size assertion in `wallet_bumpfee.py` (instagibbs)
  * [#17327](https://github.com/bitcoin/bitcoin/pull/17327) Add `rpc_fundrawtransaction` logging (jonatack)
  * [#17330](https://github.com/bitcoin/bitcoin/pull/17330) Add `shrinkdebugfile=0` to regtest bitcoin.conf (sdaftuar)
  * [#17340](https://github.com/bitcoin/bitcoin/pull/17340) Speed up fundrawtransaction test (jnewbery)
  * [#17345](https://github.com/bitcoin/bitcoin/pull/17345) Do not instantiate CAddrDB for static call CAddrDB::Read() (hebasto)
  * [#17362](https://github.com/bitcoin/bitcoin/pull/17362) Speed up `wallet_avoidreuse`, add logging (jonatack)
  * [#17363](https://github.com/bitcoin/bitcoin/pull/17363) add “diamond” unit test to MempoolAncestryTests (theStack)
  * [#17366](https://github.com/bitcoin/bitcoin/pull/17366) Reset global args between test suites (MarcoFalke)
  * [#17367](https://github.com/bitcoin/bitcoin/pull/17367) ci: Run non-cross-compile builds natively (MarcoFalke)
  * [#17378](https://github.com/bitcoin/bitcoin/pull/17378) TestShell: Fix typos & implement cleanups (jachiang)
  * [#17384](https://github.com/bitcoin/bitcoin/pull/17384) Create new test library (MarcoFalke)
  * [#17387](https://github.com/bitcoin/bitcoin/pull/17387) `wallet_importmulti`: use addresses of the same type as being imported (achow101)
  * [#17388](https://github.com/bitcoin/bitcoin/pull/17388) Add missing newline in `util_ChainMerge` test (ryanofsky)
  * [#17390](https://github.com/bitcoin/bitcoin/pull/17390) Add `util_ArgParsing` test (ryanofsky)
  * [#17420](https://github.com/bitcoin/bitcoin/pull/17420) travis: Rework `cache_err_msg` (MarcoFalke)
  * [#17423](https://github.com/bitcoin/bitcoin/pull/17423) ci: Make ci system read-only on the git work tree (MarcoFalke)
  * [#17435](https://github.com/bitcoin/bitcoin/pull/17435) check custom ancestor limit in `mempool_packages.py` (theStack)
  * [#17455](https://github.com/bitcoin/bitcoin/pull/17455) Update valgrind suppressions (practicalswift)
  * [#17461](https://github.com/bitcoin/bitcoin/pull/17461) Check custom descendant limit in `mempool_packages.py` (theStack)
  * [#17469](https://github.com/bitcoin/bitcoin/pull/17469) Remove fragile `assert_memory_usage_stable` (MarcoFalke)
  * [#17470](https://github.com/bitcoin/bitcoin/pull/17470) ci: Use clang-8 for fuzzing to run on aarch64 ci systems (MarcoFalke)
  * [#17480](https://github.com/bitcoin/bitcoin/pull/17480) Add unit test for non-standard txs with too large scriptSig (theStack)
  * [#17497](https://github.com/bitcoin/bitcoin/pull/17497) Skip tests when utils haven’t been compiled (fanquake)
  * [#17502](https://github.com/bitcoin/bitcoin/pull/17502) Add unit test for non-standard bare multisig txs (theStack)
  * [#17511](https://github.com/bitcoin/bitcoin/pull/17511) Add bounds checks before base58 decoding (sipa)
  * [#17517](https://github.com/bitcoin/bitcoin/pull/17517) ci: Bump to clang-8 for asan build to avoid segfaults on ppc64le (MarcoFalke)
  * [#17522](https://github.com/bitcoin/bitcoin/pull/17522) Wait until mempool is loaded in `wallet_abandonconflict` (MarcoFalke)
  * [#17532](https://github.com/bitcoin/bitcoin/pull/17532) Add functional test for non-standard txs with too large scriptSig (theStack)
  * [#17541](https://github.com/bitcoin/bitcoin/pull/17541) Add functional test for non-standard bare multisig txs (theStack)
  * [#17555](https://github.com/bitcoin/bitcoin/pull/17555) Add unit test for non-standard txs with wrong nVersion (dspicher)
  * [#17571](https://github.com/bitcoin/bitcoin/pull/17571) Add `libtest_util` library to msvc build configuration (sipsorcery)
  * [#17591](https://github.com/bitcoin/bitcoin/pull/17591) ci: Add big endian platform - s390x (elichai)
  * [#17593](https://github.com/bitcoin/bitcoin/pull/17593) Move more utility functions into test utility library (mzumsande)
  * [#17633](https://github.com/bitcoin/bitcoin/pull/17633) Add option –valgrind to run the functional tests under Valgrind (practicalswift)
  * [#17635](https://github.com/bitcoin/bitcoin/pull/17635) ci: Add centos 7 build (hebasto)
  * [#17641](https://github.com/bitcoin/bitcoin/pull/17641) Add unit test for leveldb creation with unicode path (sipsorcery)
  * [#17674](https://github.com/bitcoin/bitcoin/pull/17674) Add initialization order fiasco detection in Travis (practicalswift)
  * [#17675](https://github.com/bitcoin/bitcoin/pull/17675) Enable tests which are incorrectly skipped when running `test_runner.py --usecli` (practicalswift)
  * [#17685](https://github.com/bitcoin/bitcoin/pull/17685) Fix bug in the descriptor parsing fuzzing harness (`descriptor_parse`) (practicalswift)
  * [#17705](https://github.com/bitcoin/bitcoin/pull/17705) re-enable CLI test support by using EncodeDecimal in json.dumps() (fanquake)
  * [#17720](https://github.com/bitcoin/bitcoin/pull/17720) add unit test for non-standard “scriptsig-not-pushonly” txs (theStack)
  * [#17767](https://github.com/bitcoin/bitcoin/pull/17767) ci: Fix qemu issues (MarcoFalke)
  * [#17793](https://github.com/bitcoin/bitcoin/pull/17793) ci: Update github actions ci vcpkg cache on msbuild update (hebasto)
  * [#17806](https://github.com/bitcoin/bitcoin/pull/17806) Change filemode of `rpc_whitelist.py` (emilengler)
  * [#17849](https://github.com/bitcoin/bitcoin/pull/17849) ci: Fix brew python link (hebasto)
  * [#17851](https://github.com/bitcoin/bitcoin/pull/17851) Add `std::to_string` to list of locale dependent functions (practicalswift)
  * [#17893](https://github.com/bitcoin/bitcoin/pull/17893) Fix double-negative arg test (hebasto)
  * [#17900](https://github.com/bitcoin/bitcoin/pull/17900) ci: Combine 32-bit build with centos 7 build (theStack)
  * [#17921](https://github.com/bitcoin/bitcoin/pull/17921) Test `OP_CSV` empty stack fail in `feature_csv_activation.py` (theStack)
  * [#17931](https://github.com/bitcoin/bitcoin/pull/17931) Fix `p2p_invalid_messages` failing in Python 3.8 because of warning (elichai)
  * [#17947](https://github.com/bitcoin/bitcoin/pull/17947) add unit test for non-standard txs with too large tx size (theStack)
  * [#17959](https://github.com/bitcoin/bitcoin/pull/17959) Check specific reject reasons in `feature_csv_activation.py` (theStack)
  * [#17984](https://github.com/bitcoin/bitcoin/pull/17984) Add p2p test for forcerelay permission (MarcoFalke)
  * [#18001](https://github.com/bitcoin/bitcoin/pull/18001) Updated appveyor job to checkout a specific vcpkg commit ID (sipsorcery)
  * [#18008](https://github.com/bitcoin/bitcoin/pull/18008) fix fuzzing using libFuzzer on macOS (fanquake)
  * [#18013](https://github.com/bitcoin/bitcoin/pull/18013) bench: Fix benchmarks filters (elichai)
  * [#18018](https://github.com/bitcoin/bitcoin/pull/18018) reset fIsBareMultisigStd after bare-multisig tests (fanquake)
  * [#18022](https://github.com/bitcoin/bitcoin/pull/18022) Fix appveyor `test_bitcoin` build of `*.raw` (MarcoFalke)
  * [#18037](https://github.com/bitcoin/bitcoin/pull/18037) util: Allow scheduler to be mocked (amitiuttarwar)
  * [#18056](https://github.com/bitcoin/bitcoin/pull/18056) ci: Check for submodules (emilengler)
  * [#18069](https://github.com/bitcoin/bitcoin/pull/18069) Replace ‘regtest’ leftovers by self.chain (theStack)
  * [#18081](https://github.com/bitcoin/bitcoin/pull/18081) Set a name for CI Docker containers (fanquake)
  * [#18109](https://github.com/bitcoin/bitcoin/pull/18109) Avoid hitting some known minor tinyformat issues when fuzzing strprintf(…) (practicalswift)
  * [#18155](https://github.com/bitcoin/bitcoin/pull/18155) Add harness which fuzzes EvalScript and VerifyScript using a fuzzed signature checker (practicalswift)
  * [#18159](https://github.com/bitcoin/bitcoin/pull/18159) Add –valgrind option to `test/fuzz/test_runner.py` for running fuzzing test cases under valgrind (practicalswift)
  * [#18166](https://github.com/bitcoin/bitcoin/pull/18166) ci: Run fuzz testing test cases (bitcoin-core/qa-assets) under valgrind to catch memory errors (practicalswift)
  * [#18172](https://github.com/bitcoin/bitcoin/pull/18172) Transaction expiry from mempool (0xB10C)
  * [#18181](https://github.com/bitcoin/bitcoin/pull/18181) Remove incorrect assumptions in `validation_flush_tests` (MarcoFalke)
  * [#18183](https://github.com/bitcoin/bitcoin/pull/18183) Set `catch_system_errors=no` on boost unit tests (MarcoFalke)
  * [#18195](https://github.com/bitcoin/bitcoin/pull/18195) Add `cost_of_change` parameter assertions to `bnb_search_test` (yancyribbens)
  * [#18209](https://github.com/bitcoin/bitcoin/pull/18209) Reduce unneeded whitelist permissions in tests (MarcoFalke)
  * [#18211](https://github.com/bitcoin/bitcoin/pull/18211) Disable mockforward scheduler unit test for now (MarcoFalke)
  * [#18213](https://github.com/bitcoin/bitcoin/pull/18213) Fix race in `p2p_segwit` (MarcoFalke)
  * [#18224](https://github.com/bitcoin/bitcoin/pull/18224) Make AnalyzePSBT next role calculation simple, correct (instagibbs)
  * [#18228](https://github.com/bitcoin/bitcoin/pull/18228) Add missing syncwithvalidationinterfacequeue (MarcoFalke)
  * [#18247](https://github.com/bitcoin/bitcoin/pull/18247) Wait for both veracks in `add_p2p_connection` (MarcoFalke)
  * [#18249](https://github.com/bitcoin/bitcoin/pull/18249) Bump timeouts to accomodate really slow disks (MarcoFalke)
  * [#18255](https://github.com/bitcoin/bitcoin/pull/18255) Add `bad-txns-*-toolarge` test cases to `invalid_txs` (MarcoFalke)
  * [#18263](https://github.com/bitcoin/bitcoin/pull/18263) rpc: change setmocktime check to use IsMockableChain (gzhao408)
  * [#18285](https://github.com/bitcoin/bitcoin/pull/18285) Check that `wait_until` returns if time point is in the past (MarcoFalke)
  * [#18286](https://github.com/bitcoin/bitcoin/pull/18286) Add locale fuzzer to `FUZZERS_MISSING_CORPORA` (practicalswift)
  * [#18292](https://github.com/bitcoin/bitcoin/pull/18292) fuzz: Add `assert(script == decompressed_script)` (MarcoFalke)
  * [#18299](https://github.com/bitcoin/bitcoin/pull/18299) Update `FUZZERS_MISSING_CORPORA` to enable regression fuzzing for all harnesses in master (practicalswift)
  * [#18300](https://github.com/bitcoin/bitcoin/pull/18300) fuzz: Add option to merge input dir to test runner (MarcoFalke)
  * [#18305](https://github.com/bitcoin/bitcoin/pull/18305) Explain why test logging should be used (MarcoFalke)
  * [#18306](https://github.com/bitcoin/bitcoin/pull/18306) Add logging to `wallet_listsinceblock.py` (jonatack)
  * [#18311](https://github.com/bitcoin/bitcoin/pull/18311) Bumpfee test fix (instagibbs)
  * [#18314](https://github.com/bitcoin/bitcoin/pull/18314) Add deserialization fuzzing of SnapshotMetadata (`utxo_snapshot`) (practicalswift)
  * [#18319](https://github.com/bitcoin/bitcoin/pull/18319) fuzz: Add missing `ECC_Start` to `key_io` test (MarcoFalke)
  * [#18334](https://github.com/bitcoin/bitcoin/pull/18334) Add basic test for BIP 37 (MarcoFalke)
  * [#18350](https://github.com/bitcoin/bitcoin/pull/18350) Fix mining to an invalid target + ensure that a new block has the correct hash internally (TheQuantumPhysicist)
  * [#18378](https://github.com/bitcoin/bitcoin/pull/18378) Bugfix & simplify bn2vch using `int.to_bytes` (sipa)
  * [#18393](https://github.com/bitcoin/bitcoin/pull/18393) Don’t assume presence of `__builtin_mul_overflow(…)` in `MultiplicationOverflow(…)` fuzzing harness (practicalswift)
  * [#18406](https://github.com/bitcoin/bitcoin/pull/18406) add executable flag for `rpc_estimatefee.py` (theStack)
  * [#18420](https://github.com/bitcoin/bitcoin/pull/18420) listsinceblock block height checks (jonatack)
  * [#18430](https://github.com/bitcoin/bitcoin/pull/18430) ci: Only clone bitcoin-core/qa-assets when fuzzing (MarcoFalke)
  * [#18438](https://github.com/bitcoin/bitcoin/pull/18438) ci: Use homebrew addon on native macos (hebasto)
  * [#18447](https://github.com/bitcoin/bitcoin/pull/18447) Add coverage for script parse error in ParseScript (pierreN)
  * [#18472](https://github.com/bitcoin/bitcoin/pull/18472) Remove unsafe `BOOST_TEST_MESSAGE` (MarcoFalke)
  * [#18474](https://github.com/bitcoin/bitcoin/pull/18474) check that peer is connected when calling sync_* (MarcoFalke)
  * [#18477](https://github.com/bitcoin/bitcoin/pull/18477) ci: Use focal for fuzzers (MarcoFalke)
  * [#18481](https://github.com/bitcoin/bitcoin/pull/18481) add BIP37 ‘filterclear’ test to p2p_filter.py (theStack)
  * [#18496](https://github.com/bitcoin/bitcoin/pull/18496) Remove redundant `sync_with_ping` after `add_p2p_connection` (jonatack)
  * [#18509](https://github.com/bitcoin/bitcoin/pull/18509) fuzz: Avoid running over all inputs after merging them (MarcoFalke)
  * [#18510](https://github.com/bitcoin/bitcoin/pull/18510) fuzz: Add CScriptNum::getint coverage (MarcoFalke)
  * [#18514](https://github.com/bitcoin/bitcoin/pull/18514) remove rapidcheck integration and tests (fanquake)
  * [#18515](https://github.com/bitcoin/bitcoin/pull/18515) Add BIP37 remote crash bug [CVE-2013-5700] test to `p2p_filter.py` (theStack)
  * [#18516](https://github.com/bitcoin/bitcoin/pull/18516) relax bumpfee `dust_to_fee` txsize an extra vbyte (jonatack)
  * [#18518](https://github.com/bitcoin/bitcoin/pull/18518) fuzz: Extend descriptor fuzz test (MarcoFalke)
  * [#18519](https://github.com/bitcoin/bitcoin/pull/18519) fuzz: Extend script fuzz test (MarcoFalke)
  * [#18521](https://github.com/bitcoin/bitcoin/pull/18521) fuzz: Add `process_messages` harness (MarcoFalke)
  * [#18529](https://github.com/bitcoin/bitcoin/pull/18529) Add fuzzer version of randomized prevector test (sipa)
  * [#18534](https://github.com/bitcoin/bitcoin/pull/18534) skip backwards compat tests if not compiled with wallet (fanquake)
  * [#18540](https://github.com/bitcoin/bitcoin/pull/18540) `wallet_bumpfee` assertion fixup (jonatack)
  * [#18543](https://github.com/bitcoin/bitcoin/pull/18543) Use one node to avoid a race due to missing sync in `rpc_signrawtransaction` (MarcoFalke)
  * [#18561](https://github.com/bitcoin/bitcoin/pull/18561) Properly raise FailedToStartError when rpc shutdown before warmup finished (MarcoFalke)
  * [#18562](https://github.com/bitcoin/bitcoin/pull/18562) ci: Run unit tests sequential once (MarcoFalke)
  * [#18563](https://github.com/bitcoin/bitcoin/pull/18563) Fix `unregister_all_during_call` cleanup (ryanofsky)
  * [#18566](https://github.com/bitcoin/bitcoin/pull/18566) Set `-use_value_profile=1` when merging fuzz inputs (MarcoFalke)
  * [#18757](https://github.com/bitcoin/bitcoin/pull/18757) Remove enumeration of expected deserialization exceptions in ProcessMessage(…) fuzzer (practicalswift)
  * [#18878](https://github.com/bitcoin/bitcoin/pull/18878) Add test for conflicted wallet tx notifications (ryanofsky)
  * [#18975](https://github.com/bitcoin/bitcoin/pull/18975) Remove const to work around compiler error on xenial (laanwj)

### Documentation

  * [#16947](https://github.com/bitcoin/bitcoin/pull/16947) Doxygen-friendly script/descriptor.h comments (ch4ot1c)
  * [#16983](https://github.com/bitcoin/bitcoin/pull/16983) Add detailed info about Bitcoin Core files (hebasto)
  * [#16986](https://github.com/bitcoin/bitcoin/pull/16986) Doxygen-friendly CuckooCache comments (ch4ot1c)
  * [#17022](https://github.com/bitcoin/bitcoin/pull/17022) move-only: Steps for “before major release branch-off” (MarcoFalke)
  * [#17026](https://github.com/bitcoin/bitcoin/pull/17026) Update bips.md for default bech32 addresses in 0.20.0 (MarcoFalke)
  * [#17081](https://github.com/bitcoin/bitcoin/pull/17081) Fix Makefile target in benchmarking.md (theStack)
  * [#17102](https://github.com/bitcoin/bitcoin/pull/17102) Add missing indexes/blockfilter/basic to doc/files.md (MarcoFalke)
  * [#17119](https://github.com/bitcoin/bitcoin/pull/17119) Fix broken bitcoin-cli examples (andrewtoth)
  * [#17134](https://github.com/bitcoin/bitcoin/pull/17134) Add switch on enum example to developer notes (hebasto)
  * [#17142](https://github.com/bitcoin/bitcoin/pull/17142) Update macdeploy README to include all files produced by `make deploy` (za-kk)
  * [#17146](https://github.com/bitcoin/bitcoin/pull/17146) github: Add warning for bug reports (laanwj)
  * [#17157](https://github.com/bitcoin/bitcoin/pull/17157) Added instructions for how to add an upsteam to forked repo (dannmat)
  * [#17159](https://github.com/bitcoin/bitcoin/pull/17159) Add a note about backporting (carnhofdaki)
  * [#17169](https://github.com/bitcoin/bitcoin/pull/17169) Correct function name in ReportHardwareRand() (fanquake)
  * [#17177](https://github.com/bitcoin/bitcoin/pull/17177) Describe log files + consistent paths in test READMEs (fjahr)
  * [#17239](https://github.com/bitcoin/bitcoin/pull/17239) Changed miniupnp links to https (sandakersmann)
  * [#17281](https://github.com/bitcoin/bitcoin/pull/17281) Add developer note on `c_str()` (laanwj)
  * [#17285](https://github.com/bitcoin/bitcoin/pull/17285) Bip70 removal follow-up (fjahr)
  * [#17286](https://github.com/bitcoin/bitcoin/pull/17286) Fix help-debug -checkpoints (ariard)
  * [#17309](https://github.com/bitcoin/bitcoin/pull/17309) update MSVC instructions to remove Qt OpenSSL linking (fanquake)
  * [#17339](https://github.com/bitcoin/bitcoin/pull/17339) Add template for good first issues (michaelfolkson)
  * [#17351](https://github.com/bitcoin/bitcoin/pull/17351) Fix some misspellings (RandyMcMillan)
  * [#17353](https://github.com/bitcoin/bitcoin/pull/17353) Add ShellCheck to lint tests dependencies (hebasto)
  * [#17370](https://github.com/bitcoin/bitcoin/pull/17370) Update doc/bips.md with recent changes in master (MarcoFalke)
  * [#17393](https://github.com/bitcoin/bitcoin/pull/17393) Added regtest config for linearize script (gr0kchain)
  * [#17411](https://github.com/bitcoin/bitcoin/pull/17411) Add some better examples for scripted diff (laanwj)
  * [#17503](https://github.com/bitcoin/bitcoin/pull/17503) Remove bitness from bitcoin-qt help message and manpage (laanwj)
  * [#17539](https://github.com/bitcoin/bitcoin/pull/17539) Update and improve Developer Notes (hebasto)
  * [#17561](https://github.com/bitcoin/bitcoin/pull/17561) Changed MiniUPnPc link to https in dependencies.md (sandakersmann)
  * [#17596](https://github.com/bitcoin/bitcoin/pull/17596) Change doxygen URL to doxygen.bitcoincore.org (laanwj)
  * [#17598](https://github.com/bitcoin/bitcoin/pull/17598) Update release process with latest changes (MarcoFalke)
  * [#17617](https://github.com/bitcoin/bitcoin/pull/17617) Unify unix epoch time descriptions (jonatack)
  * [#17637](https://github.com/bitcoin/bitcoin/pull/17637) script: Add keyserver to verify-commits readme (emilengler)
  * [#17648](https://github.com/bitcoin/bitcoin/pull/17648) Rename wallet-tool references to bitcoin-wallet (hel-o)
  * [#17688](https://github.com/bitcoin/bitcoin/pull/17688) Add “ci” prefix to CONTRIBUTING.md (hebasto)
  * [#17751](https://github.com/bitcoin/bitcoin/pull/17751) Use recommended shebang approach in documentation code block (hackerrdave)
  * [#17752](https://github.com/bitcoin/bitcoin/pull/17752) Fix directory path for secp256k1 subtree in developer-notes (hackerrdave)
  * [#17772](https://github.com/bitcoin/bitcoin/pull/17772) Mention PR Club in CONTRIBUTING.md (emilengler)
  * [#17804](https://github.com/bitcoin/bitcoin/pull/17804) Misc RPC help fixes (MarcoFalke)
  * [#17819](https://github.com/bitcoin/bitcoin/pull/17819) Developer notes guideline on RPCExamples addresses (jonatack)
  * [#17825](https://github.com/bitcoin/bitcoin/pull/17825) Update dependencies.md (hebasto)
  * [#17873](https://github.com/bitcoin/bitcoin/pull/17873) Add to Doxygen documentation guidelines (jonatack)
  * [#17907](https://github.com/bitcoin/bitcoin/pull/17907) Fix improper Doxygen inline comments (Empact)
  * [#17942](https://github.com/bitcoin/bitcoin/pull/17942) Improve fuzzing docs for macOS users (fjahr)
  * [#17945](https://github.com/bitcoin/bitcoin/pull/17945) Fix doxygen errors (Empact)
  * [#18025](https://github.com/bitcoin/bitcoin/pull/18025) Add missing supported rpcs to doc/descriptors.md (andrewtoth)
  * [#18070](https://github.com/bitcoin/bitcoin/pull/18070) Add note about `brew doctor` (givanse)
  * [#18125](https://github.com/bitcoin/bitcoin/pull/18125) Remove PPA note from release-process.md (fanquake)
  * [#18170](https://github.com/bitcoin/bitcoin/pull/18170) Minor grammatical changes and flow improvements (travinkeith)
  * [#18212](https://github.com/bitcoin/bitcoin/pull/18212) Add missing step in win deployment instructions (dangershony)
  * [#18219](https://github.com/bitcoin/bitcoin/pull/18219) Add warning against wallet.dat re-use (corollari)
  * [#18253](https://github.com/bitcoin/bitcoin/pull/18253) Correct spelling errors in comments (Empact)
  * [#18278](https://github.com/bitcoin/bitcoin/pull/18278) interfaces: Describe and follow some code conventions (ryanofsky)
  * [#18283](https://github.com/bitcoin/bitcoin/pull/18283) Explain rebase policy in CONTRIBUTING.md (MarcoFalke)
  * [#18340](https://github.com/bitcoin/bitcoin/pull/18340) Mention MAKE=gmake workaround when building on a BSD (fanquake)
  * [#18341](https://github.com/bitcoin/bitcoin/pull/18341) Replace remaining literal BTC with `CURRENCY_UNIT` (domob1812)
  * [#18342](https://github.com/bitcoin/bitcoin/pull/18342) Add fuzzing quickstart guides for libFuzzer and afl-fuzz (practicalswift)
  * [#18344](https://github.com/bitcoin/bitcoin/pull/18344) Fix nit in getblockchaininfo (stevenroose)
  * [#18379](https://github.com/bitcoin/bitcoin/pull/18379) Comment fix merkle.cpp (4d55397500)
  * [#18382](https://github.com/bitcoin/bitcoin/pull/18382) note the costs of fetching all pull requests (vasild)
  * [#18391](https://github.com/bitcoin/bitcoin/pull/18391) Update init and reduce-traffic docs for -blocksonly (glowang)
  * [#18464](https://github.com/bitcoin/bitcoin/pull/18464) Block-relay-only vs blocksonly (MarcoFalke)
  * [#18486](https://github.com/bitcoin/bitcoin/pull/18486) Explain new test logging (MarcoFalke)
  * [#18505](https://github.com/bitcoin/bitcoin/pull/18505) Update webchat URLs in README.md (SuriyaaKudoIsc)
  * [#18513](https://github.com/bitcoin/bitcoin/pull/18513) Fix git add argument (HashUnlimited)
  * [#18577](https://github.com/bitcoin/bitcoin/pull/18577) Correct scripted-diff example link (yahiheb)
  * [#18589](https://github.com/bitcoin/bitcoin/pull/18589) Fix naming of macOS SDK and clarify version (achow101)

### Miscellaneous

  * [#15600](https://github.com/bitcoin/bitcoin/pull/15600) lockedpool: When possible, use madvise to avoid including sensitive information in core dumps (luke-jr)
  * [#15934](https://github.com/bitcoin/bitcoin/pull/15934) Merge settings one place instead of five places (ryanofsky)
  * [#16115](https://github.com/bitcoin/bitcoin/pull/16115) On bitcoind startup, write config args to debug.log (LarryRuane)
  * [#16117](https://github.com/bitcoin/bitcoin/pull/16117) util: Replace boost sleep with std sleep (MarcoFalke)
  * [#16161](https://github.com/bitcoin/bitcoin/pull/16161) util: Fix compilation errors in support/lockedpool.cpp (jkczyz)
  * [#16802](https://github.com/bitcoin/bitcoin/pull/16802) scripts: In linearize, search for next position of magic bytes rather than fail (takinbo)
  * [#16889](https://github.com/bitcoin/bitcoin/pull/16889) Add some general std::vector utility functions (sipa)
  * [#17049](https://github.com/bitcoin/bitcoin/pull/17049) contrib: Bump gitian descriptors for 0.20 (MarcoFalke)
  * [#17052](https://github.com/bitcoin/bitcoin/pull/17052) scripts: Update `copyright_header` script to include additional files (GChuf)
  * [#17059](https://github.com/bitcoin/bitcoin/pull/17059) util: Simplify path argument for cblocktreedb ctor (hebasto)
  * [#17191](https://github.com/bitcoin/bitcoin/pull/17191) random: Remove call to `RAND_screen()` (Windows only) (fanquake)
  * [#17192](https://github.com/bitcoin/bitcoin/pull/17192) util: Add `check_nonfatal` and use it in src/rpc (MarcoFalke)
  * [#17218](https://github.com/bitcoin/bitcoin/pull/17218) Replace the LogPrint function with a macro (jkczyz)
  * [#17266](https://github.com/bitcoin/bitcoin/pull/17266) util: Rename decodedumptime to parseiso8601datetime (elichai)
  * [#17270](https://github.com/bitcoin/bitcoin/pull/17270) Feed environment data into RNG initializers (sipa)
  * [#17282](https://github.com/bitcoin/bitcoin/pull/17282) contrib: Remove accounts from bash completion (fanquake)
  * [#17293](https://github.com/bitcoin/bitcoin/pull/17293) Add assertion to randrange that input is not 0 (JeremyRubin)
  * [#17325](https://github.com/bitcoin/bitcoin/pull/17325) log: Fix log message for -par=1 (hebasto)
  * [#17329](https://github.com/bitcoin/bitcoin/pull/17329) linter: Strip trailing / in path for git-subtree-check (jnewbery)
  * [#17336](https://github.com/bitcoin/bitcoin/pull/17336) scripts: Search for first block file for linearize-data with some block files pruned (Rjected)
  * [#17361](https://github.com/bitcoin/bitcoin/pull/17361) scripts: Lint gitian descriptors with shellcheck (hebasto)
  * [#17482](https://github.com/bitcoin/bitcoin/pull/17482) util: Disallow network-qualified command line options (ryanofsky)
  * [#17507](https://github.com/bitcoin/bitcoin/pull/17507) random: mark RandAddPeriodic and SeedPeriodic as noexcept (fanquake)
  * [#17527](https://github.com/bitcoin/bitcoin/pull/17527) Fix CPUID subleaf iteration (sipa)
  * [#17604](https://github.com/bitcoin/bitcoin/pull/17604) util: Make schedulebatchpriority advisory only (fanquake)
  * [#17650](https://github.com/bitcoin/bitcoin/pull/17650) util: Remove unwanted fields from bitcoin-cli -getinfo (malevolent)
  * [#17671](https://github.com/bitcoin/bitcoin/pull/17671) script: Fixed wget call in gitian-build.py (willyko)
  * [#17699](https://github.com/bitcoin/bitcoin/pull/17699) Make env data logging optional (sipa)
  * [#17721](https://github.com/bitcoin/bitcoin/pull/17721) util: Don’t allow base58 decoding of non-base58 strings. add base58 tests (practicalswift)
  * [#17750](https://github.com/bitcoin/bitcoin/pull/17750) util: Change getwarnings parameter to bool (jnewbery)
  * [#17753](https://github.com/bitcoin/bitcoin/pull/17753) util: Don’t allow base32/64-decoding or parsemoney(…) on strings with embedded nul characters. add tests (practicalswift)
  * [#17823](https://github.com/bitcoin/bitcoin/pull/17823) scripts: Read suspicious hosts from a file instead of hardcoding (sanjaykdragon)
  * [#18162](https://github.com/bitcoin/bitcoin/pull/18162) util: Avoid potential uninitialized read in `formatiso8601datetime(int64_t)` by checking `gmtime_s`/`gmtime_r` return value (practicalswift)
  * [#18167](https://github.com/bitcoin/bitcoin/pull/18167) Fix a violation of C++ standard rules where unions are used for type-punning (TheQuantumPhysicist)
  * [#18225](https://github.com/bitcoin/bitcoin/pull/18225) util: Fail to parse empty string in parsemoney (MarcoFalke)
  * [#18270](https://github.com/bitcoin/bitcoin/pull/18270) util: Fail to parse whitespace-only strings in parsemoney(…) (instead of parsing as zero) (practicalswift)
  * [#18316](https://github.com/bitcoin/bitcoin/pull/18316) util: Helpexamplerpc formatting (jonatack)
  * [#18357](https://github.com/bitcoin/bitcoin/pull/18357) Fix missing header in sync.h (promag)
  * [#18412](https://github.com/bitcoin/bitcoin/pull/18412) script: Fix `script_err_sig_pushonly` error string (theStack)
  * [#18416](https://github.com/bitcoin/bitcoin/pull/18416) util: Limit decimal range of numbers parsescript accepts (pierreN)
  * [#18503](https://github.com/bitcoin/bitcoin/pull/18503) init: Replace `URL_WEBSITE` with `PACKAGE_URL` (MarcoFalke)
  * [#18526](https://github.com/bitcoin/bitcoin/pull/18526) Remove PID file at the very end (hebasto)
  * [#18553](https://github.com/bitcoin/bitcoin/pull/18553) Avoid non-trivial global constants in SHA-NI code (sipa)
  * [#18665](https://github.com/bitcoin/bitcoin/pull/18665) Do not expose and consider `-logthreadnames` when it does not work (hebasto)

# Credits

Thanks to everyone who directly contributed to this release:

  * 0xb10c
  * 251
  * 4d55397500
  * Aaron Clauson
  * Adam Jonas
  * Albert
  * Amiti Uttarwar
  * Andrew Chow
  * Andrew Toth
  * Anthony Towns
  * Antoine Riard
  * Ava Barron
  * Ben Carman
  * Ben Woosley
  * Block Mechanic
  * Brian Solon
  * Bushstar
  * Carl Dong
  * Carnhof Daki
  * Cory Fields
  * Daki Carnhof
  * Dan Gershony
  * Daniel Kraft
  * dannmat
  * Danny-Scott
  * darosior
  * David O’Callaghan
  * Dominik Spicher
  * Elichai Turkel
  * Emil Engler
  * emu
  * Fabian Jahr
  * fanquake
  * Filip Gospodinov
  * Franck Royer
  * Gastón I. Silva
  * gchuf
  * Gleb Naumenko
  * Gloria Zhao
  * glowang
  * Gr0kchain
  * Gregory Sanders
  * hackerrdave
  * Harris
  * hel0
  * Hennadii Stepanov
  * ianliu
  * Igor Cota
  * James Chiang
  * James O’Beirne
  * Jan Beich
  * Jan Sarenik
  * Jeffrey Czyz
  * Jeremy Rubin
  * JeremyCrookshank
  * Jim Posen
  * John Bampton
  * John L. Jegutanis
  * John Newbery
  * Jon Atack
  * Jon Layton
  * Jonas Schnelli
  * João Barbosa
  * Jorge Timón
  * Karl-Johan Alm
  * kodslav
  * Larry Ruane
  * Luke Dashjr
  * malevolent
  * MapleLaker
  * marcaiaf
  * MarcoFalke
  * Marius Kjærstad
  * Mark Erhardt
  * Mark Tyneway
  * Martin Erlandsson
  * Martin Zumsande
  * Matt Corallo
  * Matt Ward
  * Michael Folkson
  * Michael Polzer
  * Micky Yun Chan
  * Neha Narula
  * nijynot
  * naumenkogs
  * NullFunctor
  * Peter Bushnell
  * pierrenn
  * Pieter Wuille
  * practicalswift
  * randymcmillan
  * Rjected
  * Russell Yanofsky
  * Samer Afach
  * Samuel Dobson
  * Sanjay K
  * Sebastian Falbesoner
  * setpill
  * Sjors Provoost
  * Stefan Richter
  * stefanwouldgo
  * Steven Roose
  * Suhas Daftuar
  * Suriyaa Sundararuban
  * TheCharlatan
  * Tim Akinbo
  * Travin Keith
  * tryphe
  * Vasil Dimov
  * Willy Ko
  * Wilson Ccasihue S
  * Wladimir J. van der Laan
  * Yahia Chiheb
  * Yancy Ribbens
  * Yusuf Sahin HAMZA
  * Zakk
  * Zero

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

