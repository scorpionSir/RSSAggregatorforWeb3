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
0.14.0

# Bitcoin Core version 0.14.0 released

8 March 2017

ALL TOPICS

  * Compatibility
  * Notable changes
    * Performance Improvements
    * Manual Pruning
    * `getinfo` Deprecated
    * ZMQ On Windows
    * Nested RPC Commands in Debug Console
    * Network Activity Toggle
    * Out-of-sync Modal Info Layer
    * Support for JSON-RPC Named Arguments
    * Opt into RBF When Sending
    * Sensitive Data Is No Longer Stored In Debug Console History
    * Retaining the Mempool Across Restarts
    * Final Alert
    * GUI Changes
    * Low-level RPC changes
    * HTTP REST Changes
    * Minimum Fee Rate Policies
    * Fee Estimation Changes
    * Removal of Priority Estimation
    * P2P connection management
    * Introduction of assumed-valid blocks
    * Fundrawtransaction change address reuse
    * Unused mempool memory used by coincache
  * 0.14.0 Change log \- {:.} RPC and other APIs \- {:.} Block and transaction handling \- {:.} P2P protocol and network code \- {:.} Validation \- {:.} Build system \- {:.} GUI \- {:.} Wallet \- {:.} Tests and QA \- {:.} Documentation \- {:.} Miscellaneous
  * Credits

Bitcoin Core version 0.14.0 is _not available for security reasons_ :

~~https://bitcoin.org/bin/bitcoin-core-0.14.0/~~

This is a new major version release, including new features, various bugfixes
and performance improvements, as well as updated translations.

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

## Performance Improvements

Validation speed and network propagation performance have been greatly
improved, leading to much shorter sync and initial block download times.

  * The script signature cache has been reimplemented as a “cuckoo cache”, allowing for more signatures to be cached and faster lookups.
  * Assumed-valid blocks have been introduced which allows script validation to be skipped for ancestors of known-good blocks, without changing the security model. See below for more details.
  * In some cases, compact blocks are now relayed before being fully validated as per BIP152.
  * P2P networking has been refactored with a focus on concurrency and throughput. Network operations are no longer bottlenecked by validation. As a result, block fetching is several times faster than previous releases in many cases.
  * The UTXO cache now claims unused mempool memory. This speeds up initial block download as UTXO lookups are a major bottleneck there, and there is no use for the mempool at that stage.

## Manual Pruning

Bitcoin Core has supported automatically pruning the blockchain since 0.11.
Pruning the blockchain allows for significant storage space savings as the
vast majority of the downloaded data can be discarded after processing so very
little of it remains on the disk.

Manual block pruning can now be enabled by setting `-prune=1`. Once that is
set, the RPC command `pruneblockchain` can be used to prune the blockchain up
to the specified height or timestamp.

## `getinfo` Deprecated

The `getinfo` RPC command has been deprecated. Each field in the RPC call has
been moved to another command’s output with that command also giving
additional information that `getinfo` did not provide. The following table
shows where each field has been moved to:

`getinfo` field | Moved to  
---|---  
`"version"` | `getnetworkinfo()["version"]`  
`"protocolversion"` | `getnetworkinfo()["protocolversion"]`  
`"walletversion"` | `getwalletinfo()["walletversion"]`  
`"balance"` | `getwalletinfo()["balance"]`  
`"blocks"` | `getblockchaininfo()["blocks"]`  
`"timeoffset"` | `getnetworkinfo()["timeoffset"]`  
`"connections"` | `getnetworkinfo()["connections"]`  
`"proxy"` | `getnetworkinfo()["networks"]&<a
href="https://github.com/bitcoin/bitcoin/pull/91">#91</a>;0&<a
href="https://github.com/bitcoin/bitcoin/pull/93">#93</a>;["proxy"]`  
`"difficulty"` | `getblockchaininfo()["difficulty"]`  
`"testnet"` | `getblockchaininfo()["chain"] == "test"`  
`"keypoololdest"` | `getwalletinfo()["keypoololdest"]`  
`"keypoolsize"` | `getwalletinfo()["keypoolsize"]`  
`"unlocked_until"` | `getwalletinfo()["unlocked_until"]`  
`"paytxfee"` | `getwalletinfo()["paytxfee"]`  
`"relayfee"` | `getnetworkinfo()["relayfee"]`  
`"errors"` | `getnetworkinfo()["warnings"]`  
  
## ZMQ On Windows

Previously the ZeroMQ notification system was unavailable on Windows due to
various issues with ZMQ. These have been fixed upstream and now ZMQ can be
used on Windows. Please see [this
document](https://github.com/bitcoin/bitcoin/blob/master/doc/zmq.md) for help
with using ZMQ in general.

## Nested RPC Commands in Debug Console

The ability to nest RPC commands has been added to the debug console. This
allows users to have the output of a command become the input to another
command without running the commands separately.

The nested RPC commands use bracket syntax (i.e. `getwalletinfo()`) and can be
nested (i.e. `getblock(getblockhash(1))`). Simple queries can be done with
square brackets where object values are accessed with either an array index or
a non-quoted string (i.e. `listunspent()&<a
href="https://github.com/bitcoin/bitcoin/pull/91">#91</a>;0&<a
href="https://github.com/bitcoin/bitcoin/pull/93">#93</a>;[txid]`). Both
commas and spaces can be used to separate parameters in both the bracket
syntax and normal RPC command syntax.

## Network Activity Toggle

A RPC command and GUI toggle have been added to enable or disable all p2p
network activity. The network status icon in the bottom right hand corner is
now the GUI toggle. Clicking the icon will either enable or disable all p2p
network activity. If network activity is disabled, the icon will be grayed out
with an X on top of it.

Additionally the `setnetworkactive` RPC command has been added which does the
same thing as the GUI icon. The command takes one boolean parameter, `true`
enables networking and `false` disables it.

## Out-of-sync Modal Info Layer

When Bitcoin Core is out-of-sync on startup, a semi-transparent information
layer will be shown over top of the normal display. This layer contains
details about the current sync progress and estimates the amount of time
remaining to finish syncing. This layer can also be hidden and subsequently
unhidden by clicking on the progress bar at the bottom of the window.

## Support for JSON-RPC Named Arguments

Commands sent over the JSON-RPC interface and through the `bitcoin-cli` binary
can now use named arguments. This follows the [JSON-RPC
specification](http://www.jsonrpc.org/specification) for passing parameters
by-name with an object.

`bitcoin-cli` has been updated to support this by parsing `name=value`
arguments when the `-named` option is given.

Some examples:

    
    
    src/bitcoin-cli -named help command="help"
    src/bitcoin-cli -named getblockhash height=0
    src/bitcoin-cli -named getblock blockhash=000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
    src/bitcoin-cli -named sendtoaddress address="(snip)" amount="1.0" subtractfeefromamount=true
    

The order of arguments doesn’t matter in this case. Named arguments are also
useful to leave out arguments that should stay at their default value. The
rarely-used arguments `comment` and `comment_to` to `sendtoaddress`, for
example, can be left out. However, this is not yet implemented for many RPC
calls, this is expected to land in a later release.

The RPC server remains fully backwards compatible with positional arguments.

## Opt into RBF When Sending

A new startup option, `-walletrbf`, has been added to allow users to have all
transactions sent opt into RBF support. The default value for this option is
currently `false`, so transactions will not opt into RBF by default. The new
`bumpfee` RPC can be used to replace transactions that opt into RBF.

## Sensitive Data Is No Longer Stored In Debug Console History

The debug console maintains a history of previously entered commands that can
be accessed by pressing the Up-arrow key so that users can easily reuse
previously entered commands. Commands which have sensitive information such as
passphrases and private keys will now have a `(...)` in place of the
parameters when accessed through the history.

## Retaining the Mempool Across Restarts

The mempool will be saved to the data directory prior to shutdown to a
`mempool.dat` file. This file preserves the mempool so that when the node
restarts the mempool can be filled with transactions without waiting for new
transactions to be created. This will also preserve any changes made to a
transaction through commands such as `prioritisetransaction` so that those
changes will not be lost.

## Final Alert

The Alert System was [disabled and
deprecated](https://bitcoin.org/en/alert/2016-11-01-alert-retirement) in
Bitcoin Core 0.12.1 and removed in 0.13.0. The Alert System was retired with a
maximum sequence final alert which causes any nodes supporting the Alert
System to display a static hard-coded “Alert Key Compromised” message which
also prevents any other alerts from overriding it. This final alert is hard-
coded into this release so that all old nodes receive the final alert.

## GUI Changes

  * After resetting the options by clicking the `Reset Options` button in the options dialog or with the `-resetguioptions` startup option, the user will be prompted to choose the data directory again. This is to ensure that custom data directories will be kept after the option reset which clears the custom data directory set via the choose datadir dialog.

  * Multiple peers can now be selected in the list of peers in the debug window. This allows for users to ban or disconnect multiple peers simultaneously instead of banning them one at a time.

  * An indicator has been added to the bottom right hand corner of the main window to indicate whether the wallet being used is a HD wallet. This icon will be grayed out with an X on top of it if the wallet is not a HD wallet.

## Low-level RPC changes

  * `importprunedfunds` only accepts two required arguments. Some versions accept an optional third arg, which was always ignored. Make sure to never pass more than two arguments.

  * The first boolean argument to `getaddednodeinfo` has been removed. This is an incompatible change.

  * RPC command `getmininginfo` loses the “testnet” field in favor of the more generic “chain” (which has been present for years).

  * A new RPC command `preciousblock` has been added which marks a block as precious. A precious block will be treated as if it were received earlier than a competing block.

  * A new RPC command `importmulti` has been added which receives an array of JSON objects representing the intention of importing a public key, a private key, an address and script/p2sh

  * Use of `getrawtransaction` for retrieving confirmed transactions with unspent outputs has been deprecated. For now this will still work, but in the future it may change to only be able to retrieve information about transactions in the mempool or if `txindex` is enabled.

  * A new RPC command `getmemoryinfo` has been added which will return information about the memory usage of Bitcoin Core. This was added in conjunction with optimizations to memory management. See [#8753](https://github.com/bitcoin/bitcoin/pull/8753). for more information.

  * A new RPC command `bumpfee` has been added which allows replacing an unconfirmed wallet transaction that signaled RBF (see the `-walletrbf` startup option above) with a new transaction that pays a higher fee, and should be more likely to get confirmed quickly.

## HTTP REST Changes

  * UTXO set query (`GET /rest/getutxos/<checkmempool>/<txid>-<n>/<txid>-<n> /.../<txid>-<n>.<bin|hex|json>`) responses were changed to return status code `HTTP_BAD_REQUEST` (400) instead of `HTTP_INTERNAL_SERVER_ERROR` (500) when requests contain invalid parameters.

## Minimum Fee Rate Policies

Since the changes in 0.12 to automatically limit the size of the mempool and
improve the performance of block creation in mining code it has not been
important for relay nodes or miners to set `-minrelaytxfee`. With this release
the following concepts that were tied to this option have been separated out:

  * incremental relay fee used for calculating BIP 125 replacement and mempool limiting. (1000 satoshis/kB)
  * calculation of threshold for a dust output. (effectively 3 * 1000 satoshis/kB)
  * minimum fee rate of a package of transactions to be included in a block created by the mining code. If miners wish to set this minimum they can use the new `-blockmintxfee` option. (defaults to 1000 satoshis/kB)

The `-minrelaytxfee` option continues to exist but is recommended to be left
unset.

## Fee Estimation Changes

  * Since 0.13.2 fee estimation for a confirmation target of 1 block has been disabled. The fee slider will no longer be able to choose a target of 1 block. This is only a minor behavior change as there was often insufficient data for this target anyway. `estimatefee 1` will now always return -1 and `estimatesmartfee 1` will start searching at a target of 2.

  * The default target for fee estimation is changed to 6 blocks in both the GUI (previously 25) and for RPC calls (previously 2).

## Removal of Priority Estimation

  * Estimation of “priority” needed for a transaction to be included within a target number of blocks has been removed. The RPC calls are deprecated and will either return -1 or 1e24 appropriately. The format for `fee_estimates.dat` has also changed to no longer save these priority estimates. It will automatically be converted to the new format which is not readable by prior versions of the software.

  * Support for “priority” (coin age) transaction sorting for mining is considered deprecated in Core and will be removed in the next major version. This is not to be confused with the `prioritisetransaction` RPC which will remain supported by Core for adding fee deltas to transactions.

## P2P connection management

  * Peers manually added through the `-addnode` option or `addnode` RPC now have their own limit of eight connections which does not compete with other inbound or outbound connection usage and is not subject to the limitation imposed by the `-maxconnections` option.

  * New connections to manually added peers are performed more quickly.

## Introduction of assumed-valid blocks

  * A significant portion of the initial block download time is spent verifying scripts/signatures. Although the verification must pass to ensure the security of the system, no other result from this verification is needed: If the node knew the history of a given block were valid it could skip checking scripts for its ancestors.

  * A new configuration option ‘assumevalid’ is provided to express this knowledge to the software. Unlike the ‘checkpoints’ in the past this setting does not force the use of a particular chain: chains that are consistent with it are processed quicker, but other chains are still accepted if they’d otherwise be chosen as best. Also unlike ‘checkpoints’ the user can configure which block history is assumed true, this means that even outdated software can sync more quickly if the setting is updated by the user.

  * Because the validity of a chain history is a simple objective fact it is much easier to review this setting. As a result the software ships with a default value adjusted to match the current chain shortly before release. The use of this default value can be disabled by setting -assumevalid=0

## Fundrawtransaction change address reuse

  * Before 0.14, `fundrawtransaction` was by default wallet stateless. In almost all cases `fundrawtransaction` does add a change-output to the outputs of the funded transaction. Before 0.14, the used keypool key was never marked as change-address key and directly returned to the keypool (leading to address reuse). Before 0.14, calling `getnewaddress` directly after `fundrawtransaction` did generate the same address as the change-output address.

  * Since 0.14, fundrawtransaction does reserve the change-output-key from the keypool by default (optional by setting `reserveChangeKey`, default = `true`)

  * Users should also consider using `getrawchangeaddress()` in conjunction with `fundrawtransaction`’s `changeAddress` option.

## Unused mempool memory used by coincache

  * Before 0.14, memory reserved for mempool (using the `-maxmempool` option) went unused during initial block download, or IBD. In 0.14, the UTXO DB cache (controlled with the `-dbcache` option) borrows memory from the mempool when there is extra memory available. This may result in an increase in memory usage during IBD for those previously relying on only the `-dbcache` option to limit memory during that time.

# 0.14.0 Change log

Detailed release notes follow. This overview includes changes that affect
behavior, not code moves, minor refactors and string updates. For convenience
in locating the code changes and accompanying discussion, both the pull
request and git merge commit are mentioned.

### RPC and other APIs

  * [#8421](https://github.com/bitcoin/bitcoin/pull/8421) [`b77bb95`](https://github.com/bitcoin/bitcoin/commit/b77bb95) httpserver: drop boost dependency (theuni)
  * [#8638](https://github.com/bitcoin/bitcoin/pull/8638) [`f061415`](https://github.com/bitcoin/bitcoin/commit/f061415) rest.cpp: change `HTTP_INTERNAL_SERVER_ERROR` to `HTTP_BAD_REQUEST` (djpnewton)
  * [#8272](https://github.com/bitcoin/bitcoin/pull/8272) [`91990ee`](https://github.com/bitcoin/bitcoin/commit/91990ee) Make the dummy argument to getaddednodeinfo optional (sipa)
  * [#8722](https://github.com/bitcoin/bitcoin/pull/8722) [`bb843ad`](https://github.com/bitcoin/bitcoin/commit/bb843ad) bitcoin-cli: More detailed error reporting (laanwj)
  * [#6996](https://github.com/bitcoin/bitcoin/pull/6996) [`7f71a3c`](https://github.com/bitcoin/bitcoin/commit/7f71a3c) Add preciousblock RPC (sipa)
  * [#8788](https://github.com/bitcoin/bitcoin/pull/8788) [`97c7f73`](https://github.com/bitcoin/bitcoin/commit/97c7f73) Give RPC commands more information about the RPC request (jonasschnelli)
  * [#7948](https://github.com/bitcoin/bitcoin/pull/7948) [`5d2c8e5`](https://github.com/bitcoin/bitcoin/commit/5d2c8e5) Augment getblockchaininfo bip9_softforks data (mruddy)
  * [#8980](https://github.com/bitcoin/bitcoin/pull/8980) [`0e22855`](https://github.com/bitcoin/bitcoin/commit/0e22855) importmulti: Avoid using boost::variant::operator!=, which is only in newer boost versions (luke-jr)
  * [#9025](https://github.com/bitcoin/bitcoin/pull/9025) [`4d8558a`](https://github.com/bitcoin/bitcoin/commit/4d8558a) Getrawtransaction should take a bool for verbose (jnewbery)
  * [#8811](https://github.com/bitcoin/bitcoin/pull/8811) [`5754e03`](https://github.com/bitcoin/bitcoin/commit/5754e03) Add support for JSON-RPC named arguments (laanwj)
  * [#9520](https://github.com/bitcoin/bitcoin/pull/9520) [`2456a83`](https://github.com/bitcoin/bitcoin/commit/2456a83) Deprecate non-txindex getrawtransaction and better warning (sipa)
  * [#9518](https://github.com/bitcoin/bitcoin/pull/9518) [`a65ced1`](https://github.com/bitcoin/bitcoin/commit/a65ced1) Return height of last block pruned by pruneblockchain RPC (ryanofsky)
  * [#9222](https://github.com/bitcoin/bitcoin/pull/9222) [`7cb024e`](https://github.com/bitcoin/bitcoin/commit/7cb024e) Add ‘subtractFeeFromAmount’ option to ‘fundrawtransaction’ (dooglus)
  * [#8456](https://github.com/bitcoin/bitcoin/pull/8456) [`2ef52d3`](https://github.com/bitcoin/bitcoin/commit/2ef52d3) Simplified `bumpfee` command (mrbandrews)
  * [#9516](https://github.com/bitcoin/bitcoin/pull/9516) [`727a798`](https://github.com/bitcoin/bitcoin/commit/727a798) Bug-fix: listsinceblock: use fork point as reference for blocks in reorg’d chains (kallewoof)
  * [#9640](https://github.com/bitcoin/bitcoin/pull/9640) [`7bfb770`](https://github.com/bitcoin/bitcoin/commit/7bfb770) Bumpfee: bugfixes for error handling and feerate calculation (sdaftuar)
  * [#9673](https://github.com/bitcoin/bitcoin/pull/9673) [`8d6447e`](https://github.com/bitcoin/bitcoin/commit/8d6447e) Set correct metadata on bumpfee wallet transactions (ryanofsky)
  * [#9650](https://github.com/bitcoin/bitcoin/pull/9650) [`40f7e27`](https://github.com/bitcoin/bitcoin/commit/40f7e27) Better handle invalid parameters to signrawtransaction (TheBlueMatt)
  * [#9682](https://github.com/bitcoin/bitcoin/pull/9682) [`edc9e63`](https://github.com/bitcoin/bitcoin/commit/edc9e63) Require timestamps for importmulti keys (ryanofsky)
  * [#9108](https://github.com/bitcoin/bitcoin/pull/9108) [`d8e8b06`](https://github.com/bitcoin/bitcoin/commit/d8e8b06) Use importmulti timestamp when importing watch only keys (on top of [#9682](https://github.com/bitcoin/bitcoin/pull/9682)) (ryanofsky)
  * [#9756](https://github.com/bitcoin/bitcoin/pull/9756) [`7a93af8`](https://github.com/bitcoin/bitcoin/commit/7a93af8) Return error when importmulti called with invalid address (ryanofsky)
  * [#9778](https://github.com/bitcoin/bitcoin/pull/9778) [`ad168ef`](https://github.com/bitcoin/bitcoin/commit/ad168ef) Add two hour buffer to manual pruning (morcos)
  * [#9761](https://github.com/bitcoin/bitcoin/pull/9761) [`9828f9a`](https://github.com/bitcoin/bitcoin/commit/9828f9a) Use 2 hour grace period for key timestamps in importmulti rescans (ryanofsky)
  * [#9474](https://github.com/bitcoin/bitcoin/pull/9474) [`48d7e0d`](https://github.com/bitcoin/bitcoin/commit/48d7e0d) Mark the minconf parameter to move as ignored (sipa)
  * [#9619](https://github.com/bitcoin/bitcoin/pull/9619) [`861cb0c`](https://github.com/bitcoin/bitcoin/commit/861cb0c) Bugfix: RPC/Mining: GBT should return 1 MB sizelimit before segwit activates (luke-jr)
  * [#9773](https://github.com/bitcoin/bitcoin/pull/9773) [`9072395`](https://github.com/bitcoin/bitcoin/commit/9072395) Return errors from importmulti if complete rescans are not successful (ryanofsky)

### Block and transaction handling

  * [#8391](https://github.com/bitcoin/bitcoin/pull/8391) [`37d83bb`](https://github.com/bitcoin/bitcoin/commit/37d83bb) Consensus: Remove ISM (NicolasDorier)
  * [#8365](https://github.com/bitcoin/bitcoin/pull/8365) [`618c9dd`](https://github.com/bitcoin/bitcoin/commit/618c9dd) Treat high-sigop transactions as larger rather than rejecting them (sipa)
  * [#8814](https://github.com/bitcoin/bitcoin/pull/8814) [`14b7b3f`](https://github.com/bitcoin/bitcoin/commit/14b7b3f) wallet, policy: ParameterInteraction: Don’t allow 0 fee (MarcoFalke)
  * [#8515](https://github.com/bitcoin/bitcoin/pull/8515) [`9bdf526`](https://github.com/bitcoin/bitcoin/commit/9bdf526) A few mempool removal optimizations (sipa)
  * [#8448](https://github.com/bitcoin/bitcoin/pull/8448) [`101c642`](https://github.com/bitcoin/bitcoin/commit/101c642) Store mempool and prioritization data to disk (sipa)
  * [#7730](https://github.com/bitcoin/bitcoin/pull/7730) [`3c03dc2`](https://github.com/bitcoin/bitcoin/commit/3c03dc2) Remove priority estimation (morcos)
  * [#9111](https://github.com/bitcoin/bitcoin/pull/9111) [`fb15610`](https://github.com/bitcoin/bitcoin/commit/fb15610) Remove unused variable `UNLIKELY_PCT` from fees.h (fanquake)
  * [#9133](https://github.com/bitcoin/bitcoin/pull/9133) [`434e683`](https://github.com/bitcoin/bitcoin/commit/434e683) Unset fImporting for loading mempool (morcos)
  * [#9179](https://github.com/bitcoin/bitcoin/pull/9179) [`b9a87b4`](https://github.com/bitcoin/bitcoin/commit/b9a87b4) Set `DEFAULT_LIMITFREERELAY` = 0 kB/minute (MarcoFalke)
  * [#9239](https://github.com/bitcoin/bitcoin/pull/9239) [`3fbf079`](https://github.com/bitcoin/bitcoin/commit/3fbf079) Disable fee estimates for 1-block target (morcos)
  * [#7562](https://github.com/bitcoin/bitcoin/pull/7562) [`1eef038`](https://github.com/bitcoin/bitcoin/commit/1eef038) Bump transaction version default to 2 (btcdrak)
  * [#9313](https://github.com/bitcoin/bitcoin/pull/9313),[#9367](https://github.com/bitcoin/bitcoin/pull/9367) If we don’t allow free txs, always send a fee filter (morcos)
  * [#9346](https://github.com/bitcoin/bitcoin/pull/9346) [`b99a093`](https://github.com/bitcoin/bitcoin/commit/b99a093) Batch construct batches (sipa)
  * [#9262](https://github.com/bitcoin/bitcoin/pull/9262) [`5a70572`](https://github.com/bitcoin/bitcoin/commit/5a70572) Prefer coins that have fewer ancestors, sanity check txn before ATMP (instagibbs)
  * [#9288](https://github.com/bitcoin/bitcoin/pull/9288) [`1ce7ede`](https://github.com/bitcoin/bitcoin/commit/1ce7ede) Fix a bug if the min fee is 0 for FeeFilterRounder (morcos)
  * [#9395](https://github.com/bitcoin/bitcoin/pull/9395) [`0fc1c31`](https://github.com/bitcoin/bitcoin/commit/0fc1c31) Add test for `-walletrejectlongchains` (morcos)
  * [#9107](https://github.com/bitcoin/bitcoin/pull/9107) [`7dac1e5`](https://github.com/bitcoin/bitcoin/commit/7dac1e5) Safer modify new coins (morcos)
  * [#9312](https://github.com/bitcoin/bitcoin/pull/9312) [`a72f76c`](https://github.com/bitcoin/bitcoin/commit/a72f76c) Increase mempool expiry time to 2 weeks (morcos)
  * [#8610](https://github.com/bitcoin/bitcoin/pull/8610) [`c252685`](https://github.com/bitcoin/bitcoin/commit/c252685) Share unused mempool memory with coincache (sipa)
  * [#9138](https://github.com/bitcoin/bitcoin/pull/9138) [`f646275`](https://github.com/bitcoin/bitcoin/commit/f646275) Improve fee estimation (morcos)
  * [#9408](https://github.com/bitcoin/bitcoin/pull/9408) [`46b249e`](https://github.com/bitcoin/bitcoin/commit/46b249e) Allow shutdown during LoadMempool, dump only when necessary (jonasschnelli)
  * [#9310](https://github.com/bitcoin/bitcoin/pull/9310) [`8c87f17`](https://github.com/bitcoin/bitcoin/commit/8c87f17) Assert FRESH validity in CCoinsViewCache::BatchWrite (ryanofsky)
  * [#7871](https://github.com/bitcoin/bitcoin/pull/7871) [`e2e624d`](https://github.com/bitcoin/bitcoin/commit/e2e624d) Manual block file pruning (mrbandrews)
  * [#9507](https://github.com/bitcoin/bitcoin/pull/9507) [`0595042`](https://github.com/bitcoin/bitcoin/commit/0595042) Fix use-after-free in CTxMemPool::removeConflicts() (sdaftuar)
  * [#9380](https://github.com/bitcoin/bitcoin/pull/9380) [`dd98f04`](https://github.com/bitcoin/bitcoin/commit/dd98f04) Separate different uses of minimum fees (morcos)
  * [#9596](https://github.com/bitcoin/bitcoin/pull/9596) [`71148b8`](https://github.com/bitcoin/bitcoin/commit/71148b8) bugfix save feeDelta instead of priorityDelta in DumpMempool (morcos)
  * [#9371](https://github.com/bitcoin/bitcoin/pull/9371) [`4a1dc35`](https://github.com/bitcoin/bitcoin/commit/4a1dc35) Notify on removal (morcos)
  * [#9519](https://github.com/bitcoin/bitcoin/pull/9519) [`9b4d267`](https://github.com/bitcoin/bitcoin/commit/9b4d267) Exclude RBF replacement txs from fee estimation (morcos)
  * [#8606](https://github.com/bitcoin/bitcoin/pull/8606) [`e2a1a1e`](https://github.com/bitcoin/bitcoin/commit/e2a1a1e) Fix some locks (sipa)
  * [#8681](https://github.com/bitcoin/bitcoin/pull/8681) [`6898213`](https://github.com/bitcoin/bitcoin/commit/6898213) Performance Regression Fix: Pre-Allocate txChanged vector (JeremyRubin)
  * [#8223](https://github.com/bitcoin/bitcoin/pull/8223) [`744d265`](https://github.com/bitcoin/bitcoin/commit/744d265) c++11: Use std::unique_ptr for block creation (domob1812)
  * [#9125](https://github.com/bitcoin/bitcoin/pull/9125) [`7490ae8`](https://github.com/bitcoin/bitcoin/commit/7490ae8) Make CBlock a vector of shared_ptr of CTransactions (sipa)
  * [#8930](https://github.com/bitcoin/bitcoin/pull/8930) [`93566e0`](https://github.com/bitcoin/bitcoin/commit/93566e0) Move orphan processing to ActivateBestChain (TheBlueMatt)
  * [#8580](https://github.com/bitcoin/bitcoin/pull/8580) [`46904ee`](https://github.com/bitcoin/bitcoin/commit/46904ee) Make CTransaction actually immutable (sipa)
  * [#9240](https://github.com/bitcoin/bitcoin/pull/9240) [`a1dcf2e`](https://github.com/bitcoin/bitcoin/commit/a1dcf2e) Remove txConflicted (morcos)
  * [#8589](https://github.com/bitcoin/bitcoin/pull/8589) [`e8cfe1e`](https://github.com/bitcoin/bitcoin/commit/e8cfe1e) Inline CTxInWitness inside CTxIn (sipa)
  * [#9349](https://github.com/bitcoin/bitcoin/pull/9349) [`2db4cbc`](https://github.com/bitcoin/bitcoin/commit/2db4cbc) Make CScript (and prevector) c++11 movable (sipa)
  * [#9252](https://github.com/bitcoin/bitcoin/pull/9252) [`ce5c1f4`](https://github.com/bitcoin/bitcoin/commit/ce5c1f4) Release cs_main before calling ProcessNewBlock, or processing headers (cmpctblock handling) (sdaftuar)
  * [#9283](https://github.com/bitcoin/bitcoin/pull/9283) [`869781c`](https://github.com/bitcoin/bitcoin/commit/869781c) A few more CTransactionRef optimizations (sipa)
  * [#9499](https://github.com/bitcoin/bitcoin/pull/9499) [`9c9af5a`](https://github.com/bitcoin/bitcoin/commit/9c9af5a) Use recent-rejects, orphans, and recently-replaced txn for compact-block-reconstruction (TheBlueMatt)
  * [#9813](https://github.com/bitcoin/bitcoin/pull/9813) [`3972a8e`](https://github.com/bitcoin/bitcoin/commit/3972a8e) Read/write mempool.dat as a binary (paveljanik)

### P2P protocol and network code

  * [#8128](https://github.com/bitcoin/bitcoin/pull/8128) [`1030fa7`](https://github.com/bitcoin/bitcoin/commit/1030fa7) Turn net structures into dumb storage classes (theuni)
  * [#8282](https://github.com/bitcoin/bitcoin/pull/8282) [`026c6ed`](https://github.com/bitcoin/bitcoin/commit/026c6ed) Feeler connections to increase online addrs in the tried table (EthanHeilman)
  * [#8462](https://github.com/bitcoin/bitcoin/pull/8462) [`53f8f22`](https://github.com/bitcoin/bitcoin/commit/53f8f22) Move AdvertiseLocal debug output to net category (Mirobit)
  * [#8612](https://github.com/bitcoin/bitcoin/pull/8612) [`84decb5`](https://github.com/bitcoin/bitcoin/commit/84decb5) Check for compatibility with download in FindNextBlocksToDownload (sipa)
  * [#8594](https://github.com/bitcoin/bitcoin/pull/8594) [`5b2ea29`](https://github.com/bitcoin/bitcoin/commit/5b2ea29) Do not add random inbound peers to addrman (gmaxwell)
  * [#8085](https://github.com/bitcoin/bitcoin/pull/8085) [`6423116`](https://github.com/bitcoin/bitcoin/commit/6423116) Begin encapsulation (theuni)
  * [#8715](https://github.com/bitcoin/bitcoin/pull/8715) [`881d7ea`](https://github.com/bitcoin/bitcoin/commit/881d7ea) only delete CConnman if it’s been created (theuni)
  * [#8707](https://github.com/bitcoin/bitcoin/pull/8707) [`f07424a`](https://github.com/bitcoin/bitcoin/commit/f07424a) Fix maxuploadtarget setting (theuni)
  * [#8661](https://github.com/bitcoin/bitcoin/pull/8661) [`d2e4655`](https://github.com/bitcoin/bitcoin/commit/d2e4655) Do not set an addr time penalty when a peer advertises itself (gmaxwell)
  * [#8822](https://github.com/bitcoin/bitcoin/pull/8822) [`9bc6a6b`](https://github.com/bitcoin/bitcoin/commit/9bc6a6b) Consistent checksum handling (laanwj)
  * [#8936](https://github.com/bitcoin/bitcoin/pull/8936) [`1230890`](https://github.com/bitcoin/bitcoin/commit/1230890) Report NodeId in misbehaving debug (rebroad)
  * [#8968](https://github.com/bitcoin/bitcoin/pull/8968) [`3cf496d`](https://github.com/bitcoin/bitcoin/commit/3cf496d) Don’t hold cs_main when calling ProcessNewBlock from a cmpctblock (TheBlueMatt)
  * [#9002](https://github.com/bitcoin/bitcoin/pull/9002) [`e1d1f57`](https://github.com/bitcoin/bitcoin/commit/e1d1f57) Make connect=0 disable automatic outbound connections (gmaxwell)
  * [#9050](https://github.com/bitcoin/bitcoin/pull/9050) [`fcf61b8`](https://github.com/bitcoin/bitcoin/commit/fcf61b8) Make a few values immutable, and use deterministic randomness for the localnonce (theuni)
  * [#8969](https://github.com/bitcoin/bitcoin/pull/8969) [`3665483`](https://github.com/bitcoin/bitcoin/commit/3665483) Decouple peer-processing-logic from block-connection-logic (#2) (TheBlueMatt)
  * [#8708](https://github.com/bitcoin/bitcoin/pull/8708) [`c8c572f`](https://github.com/bitcoin/bitcoin/commit/c8c572f) have CConnman handle message sending (theuni)
  * [#8709](https://github.com/bitcoin/bitcoin/pull/8709) [`1e50d22`](https://github.com/bitcoin/bitcoin/commit/1e50d22) Allow filterclear messages for enabling TX relay only (rebroad)
  * [#9045](https://github.com/bitcoin/bitcoin/pull/9045) [`9f554e0`](https://github.com/bitcoin/bitcoin/commit/9f554e0) Hash P2P messages as they are received instead of at process-time (TheBlueMatt)
  * [#9026](https://github.com/bitcoin/bitcoin/pull/9026) [`dc6b940`](https://github.com/bitcoin/bitcoin/commit/dc6b940) Fix handling of invalid compact blocks (sdaftuar)
  * [#8996](https://github.com/bitcoin/bitcoin/pull/8996) [`ab914a6`](https://github.com/bitcoin/bitcoin/commit/ab914a6) Network activity toggle (luke-jr)
  * [#9131](https://github.com/bitcoin/bitcoin/pull/9131) [`62af164`](https://github.com/bitcoin/bitcoin/commit/62af164) fNetworkActive is not protected by a lock, use an atomic (jonasschnelli)
  * [#8872](https://github.com/bitcoin/bitcoin/pull/8872) [`0c577f2`](https://github.com/bitcoin/bitcoin/commit/0c577f2) Remove block-request logic from INV message processing (TheBlueMatt)
  * [#8690](https://github.com/bitcoin/bitcoin/pull/8690) [`791b58d`](https://github.com/bitcoin/bitcoin/commit/791b58d) Do not fully sort all nodes for addr relay (sipa)
  * [#9128](https://github.com/bitcoin/bitcoin/pull/9128) [`76fec09`](https://github.com/bitcoin/bitcoin/commit/76fec09) Decouple CConnman and message serialization (theuni)
  * [#9226](https://github.com/bitcoin/bitcoin/pull/9226) [`3bf06e9`](https://github.com/bitcoin/bitcoin/commit/3bf06e9) Remove fNetworkNode and pnodeLocalHost (gmaxwell)
  * [#9352](https://github.com/bitcoin/bitcoin/pull/9352) [`a7f7651`](https://github.com/bitcoin/bitcoin/commit/a7f7651) Attempt reconstruction from all compact block announcements (sdaftuar)
  * [#9319](https://github.com/bitcoin/bitcoin/pull/9319) [`a55716a`](https://github.com/bitcoin/bitcoin/commit/a55716a) Break addnode out from the outbound connection limits (gmaxwell)
  * [#9261](https://github.com/bitcoin/bitcoin/pull/9261) [`2742568`](https://github.com/bitcoin/bitcoin/commit/2742568) Add unstored orphans with rejected parents to recentRejects (morcos)
  * [#9441](https://github.com/bitcoin/bitcoin/pull/9441) [`8b66bf7`](https://github.com/bitcoin/bitcoin/commit/8b66bf7) Massive speedup. Net locks overhaul (theuni)
  * [#9375](https://github.com/bitcoin/bitcoin/pull/9375) [`3908fc4`](https://github.com/bitcoin/bitcoin/commit/3908fc4) Relay compact block messages prior to full block connection (TheBlueMatt)
  * [#9400](https://github.com/bitcoin/bitcoin/pull/9400) [`8a445c5`](https://github.com/bitcoin/bitcoin/commit/8a445c5) Set peers as HB peers upon full block validation (instagibbs)
  * [#9561](https://github.com/bitcoin/bitcoin/pull/9561) [`6696b46`](https://github.com/bitcoin/bitcoin/commit/6696b46) Wake message handling thread when we receive a new block (TheBlueMatt)
  * [#9535](https://github.com/bitcoin/bitcoin/pull/9535) [`82274c0`](https://github.com/bitcoin/bitcoin/commit/82274c0) Split CNode::cs_vSend: message processing and message sending (TheBlueMatt)
  * [#9606](https://github.com/bitcoin/bitcoin/pull/9606) [`3f9f962`](https://github.com/bitcoin/bitcoin/commit/3f9f962) Consistently use GetTimeMicros() for inactivity checks (sdaftuar)
  * [#9594](https://github.com/bitcoin/bitcoin/pull/9594) [`fd70211`](https://github.com/bitcoin/bitcoin/commit/fd70211) Send final alert message to older peers after connecting (gmaxwell)
  * [#9626](https://github.com/bitcoin/bitcoin/pull/9626) [`36966a1`](https://github.com/bitcoin/bitcoin/commit/36966a1) Clean up a few CConnman cs_vNodes/CNode things (TheBlueMatt)
  * [#9609](https://github.com/bitcoin/bitcoin/pull/9609) [`4966917`](https://github.com/bitcoin/bitcoin/commit/4966917) Fix remaining net assertions (theuni)
  * [#9671](https://github.com/bitcoin/bitcoin/pull/9671) [`7821db3`](https://github.com/bitcoin/bitcoin/commit/7821db3) Fix super-unlikely race introduced in 236618061a445d2cb11e72 (TheBlueMatt)
  * [#9730](https://github.com/bitcoin/bitcoin/pull/9730) [`33f3b21`](https://github.com/bitcoin/bitcoin/commit/33f3b21) Remove bitseed.xf2.org form the dns seed list (jonasschnelli)
  * [#9698](https://github.com/bitcoin/bitcoin/pull/9698) [`2447c10`](https://github.com/bitcoin/bitcoin/commit/2447c10) Fix socket close race (theuni)
  * [#9708](https://github.com/bitcoin/bitcoin/pull/9708) [`a06ede9`](https://github.com/bitcoin/bitcoin/commit/a06ede9) Clean up all known races/platform-specific UB at the time PR was opened (TheBlueMatt)
  * [#9715](https://github.com/bitcoin/bitcoin/pull/9715) [`b08656e`](https://github.com/bitcoin/bitcoin/commit/b08656e) Disconnect peers which we do not receive VERACKs from within 60 sec (TheBlueMatt)
  * [#9720](https://github.com/bitcoin/bitcoin/pull/9720) [`e87ce95`](https://github.com/bitcoin/bitcoin/commit/e87ce95) Fix banning and disallow sending messages before receiving verack (theuni)
  * [#9268](https://github.com/bitcoin/bitcoin/pull/9268) [`09c4fd1`](https://github.com/bitcoin/bitcoin/commit/09c4fd1) Fix rounding privacy leak introduced in [#9260](https://github.com/bitcoin/bitcoin/pull/9260) (TheBlueMatt)
  * [#9075](https://github.com/bitcoin/bitcoin/pull/9075) [`9346f84`](https://github.com/bitcoin/bitcoin/commit/9346f84) Decouple peer-processing-logic from block-connection-logic (#3) (TheBlueMatt)
  * [#8688](https://github.com/bitcoin/bitcoin/pull/8688) [`047ded0`](https://github.com/bitcoin/bitcoin/commit/047ded0) Move static global randomizer seeds into CConnman (sipa)
  * [#9289](https://github.com/bitcoin/bitcoin/pull/9289) [`d9ae1ce`](https://github.com/bitcoin/bitcoin/commit/d9ae1ce) net: drop boost::thread_group (theuni)

### Validation

  * [#9014](https://github.com/bitcoin/bitcoin/pull/9014) [`d04aeba`](https://github.com/bitcoin/bitcoin/commit/d04aeba) Fix block-connection performance regression (TheBlueMatt)
  * [#9299](https://github.com/bitcoin/bitcoin/pull/9299) [`d52ce89`](https://github.com/bitcoin/bitcoin/commit/d52ce89) Remove no longer needed check for premature v2 txs (morcos)
  * [#9273](https://github.com/bitcoin/bitcoin/pull/9273) [`b68685a`](https://github.com/bitcoin/bitcoin/commit/b68685a) Remove unused `CDiskBlockPos*` argument from ProcessNewBlock (TheBlueMatt)
  * [#8895](https://github.com/bitcoin/bitcoin/pull/8895) [`b83264d`](https://github.com/bitcoin/bitcoin/commit/b83264d) Better SigCache Implementation (JeremyRubin)
  * [#9490](https://github.com/bitcoin/bitcoin/pull/9490) [`e126d0c`](https://github.com/bitcoin/bitcoin/commit/e126d0c) Replace FindLatestBefore used by importmulti with FindEarliestAtLeast (gmaxwell)
  * [#9484](https://github.com/bitcoin/bitcoin/pull/9484) [`812714f`](https://github.com/bitcoin/bitcoin/commit/812714f) Introduce assumevalid setting to skip validation presumed valid scripts (gmaxwell)
  * [#9511](https://github.com/bitcoin/bitcoin/pull/9511) [`7884956`](https://github.com/bitcoin/bitcoin/commit/7884956) Don’t overwrite validation state with corruption check (morcos)
  * [#9765](https://github.com/bitcoin/bitcoin/pull/9765) [`1e92e04`](https://github.com/bitcoin/bitcoin/commit/1e92e04) Harden against mistakes handling invalid blocks (sdaftuar)
  * [#9779](https://github.com/bitcoin/bitcoin/pull/9779) [`3c02b95`](https://github.com/bitcoin/bitcoin/commit/3c02b95) Update nMinimumChainWork and defaultAssumeValid (gmaxwell)
  * [#8524](https://github.com/bitcoin/bitcoin/pull/8524) [`19b0f33`](https://github.com/bitcoin/bitcoin/commit/19b0f33) Precompute sighashes (sipa)
  * [#9791](https://github.com/bitcoin/bitcoin/pull/9791) [`1825a03`](https://github.com/bitcoin/bitcoin/commit/1825a03) Avoid VLA in hash.h (sipa)

### Build system

  * [#8238](https://github.com/bitcoin/bitcoin/pull/8238) [`6caf3ee`](https://github.com/bitcoin/bitcoin/commit/6caf3ee) ZeroMQ 4.1.5 && ZMQ on Windows (fanquake)
  * [#8520](https://github.com/bitcoin/bitcoin/pull/8520) [`b40e19c`](https://github.com/bitcoin/bitcoin/commit/b40e19c) Remove check for `openssl/ec.h` (laanwj)
  * [#8617](https://github.com/bitcoin/bitcoin/pull/8617) [`de07fdc`](https://github.com/bitcoin/bitcoin/commit/de07fdc) Include instructions to extract Mac OS X SDK on Linux using 7zip and SleuthKit (luke-jr)
  * [#8566](https://github.com/bitcoin/bitcoin/pull/8566) [`7b98895`](https://github.com/bitcoin/bitcoin/commit/7b98895) Easy to use gitian building script (achow101)
  * [#8604](https://github.com/bitcoin/bitcoin/pull/8604) [`f256843`](https://github.com/bitcoin/bitcoin/commit/f256843) build,doc: Update for 0.13.0+ and OpenBSD 5.9 (laanwj)
  * [#8640](https://github.com/bitcoin/bitcoin/pull/8640) [`2663e51`](https://github.com/bitcoin/bitcoin/commit/2663e51) depends: Remove Qt46 package (fanquake)
  * [#8645](https://github.com/bitcoin/bitcoin/pull/8645) [`8ea4440`](https://github.com/bitcoin/bitcoin/commit/8ea4440) Remove unused Qt 4.6 patch (droark)
  * [#8608](https://github.com/bitcoin/bitcoin/pull/8608) [`7e9ab95`](https://github.com/bitcoin/bitcoin/commit/7e9ab95) Install manpages via make install, also add some autogenerated manpages (nomnombtc)
  * [#8781](https://github.com/bitcoin/bitcoin/pull/8781) [`ca69ef4`](https://github.com/bitcoin/bitcoin/commit/ca69ef4) contrib: delete `qt_translations.py` (MarcoFalke)
  * [#8783](https://github.com/bitcoin/bitcoin/pull/8783) [`64dc645`](https://github.com/bitcoin/bitcoin/commit/64dc645) share: remove qt/protobuf.pri (MarcoFalke)
  * [#8423](https://github.com/bitcoin/bitcoin/pull/8423) [`3166dff`](https://github.com/bitcoin/bitcoin/commit/3166dff) depends: expat 2.2.0, ccache 3.3.1, fontconfig 2.12.1 (fanquake)
  * [#8791](https://github.com/bitcoin/bitcoin/pull/8791) [`b694b0d`](https://github.com/bitcoin/bitcoin/commit/b694b0d) travis: cross-mac: explicitly enable gui (MarcoFalke)
  * [#8820](https://github.com/bitcoin/bitcoin/pull/8820) [`dc64141`](https://github.com/bitcoin/bitcoin/commit/dc64141) depends: Fix Qt compilation with Xcode 8 (fanquake)
  * [#8730](https://github.com/bitcoin/bitcoin/pull/8730) [`489a6ab`](https://github.com/bitcoin/bitcoin/commit/489a6ab) depends: Add libevent compatibility patch for windows (laanwj)
  * [#8819](https://github.com/bitcoin/bitcoin/pull/8819) [`c841816`](https://github.com/bitcoin/bitcoin/commit/c841816) depends: Boost 1.61.0 (fanquake)
  * [#8826](https://github.com/bitcoin/bitcoin/pull/8826) [`f560d95`](https://github.com/bitcoin/bitcoin/commit/f560d95) Do not include `env_win.cc` on non-Windows systems (paveljanik)
  * [#8948](https://github.com/bitcoin/bitcoin/pull/8948) [`e077e00`](https://github.com/bitcoin/bitcoin/commit/e077e00) Reorder Windows gitian build order to match Linux (Michagogo)
  * [#8568](https://github.com/bitcoin/bitcoin/pull/8568) [`078900d`](https://github.com/bitcoin/bitcoin/commit/078900d) new var `DIST_CONTRIB` adds useful things for packagers from contrib (nomnombtc)
  * [#9114](https://github.com/bitcoin/bitcoin/pull/9114) [`21e6c6b`](https://github.com/bitcoin/bitcoin/commit/21e6c6b) depends: Set `OSX_MIN_VERSION` to 10.8 (fanquake)
  * [#9140](https://github.com/bitcoin/bitcoin/pull/9140) [`018a4eb`](https://github.com/bitcoin/bitcoin/commit/018a4eb) Bugfix: Correctly replace generated headers and fail cleanly (luke-jr)
  * [#9156](https://github.com/bitcoin/bitcoin/pull/9156) [`a8b2a82`](https://github.com/bitcoin/bitcoin/commit/a8b2a82) Add compile and link options echo to configure (jonasschnelli)
  * [#9393](https://github.com/bitcoin/bitcoin/pull/9393) [`03d85f6`](https://github.com/bitcoin/bitcoin/commit/03d85f6) Include cuckoocache header in Makefile (MarcoFalke)
  * [#9420](https://github.com/bitcoin/bitcoin/pull/9420) [`bebe369`](https://github.com/bitcoin/bitcoin/commit/bebe369) Fix linker error when configured with –enable-lcov (droark)
  * [#9412](https://github.com/bitcoin/bitcoin/pull/9412) [`53442af`](https://github.com/bitcoin/bitcoin/commit/53442af) Fix ‘make deploy’ for OSX (jonasschnelli)
  * [#9475](https://github.com/bitcoin/bitcoin/pull/9475) [`7014506`](https://github.com/bitcoin/bitcoin/commit/7014506) Let autoconf detect presence of `EVP_MD_CTX_new` (luke-jr)
  * [#9513](https://github.com/bitcoin/bitcoin/pull/9513) [`bbf193f`](https://github.com/bitcoin/bitcoin/commit/bbf193f) Fix qt distdir builds (theuni)
  * [#9471](https://github.com/bitcoin/bitcoin/pull/9471) [`ca615e6`](https://github.com/bitcoin/bitcoin/commit/ca615e6) depends: libevent 2.1.7rc (fanquake)
  * [#9468](https://github.com/bitcoin/bitcoin/pull/9468) [`f9117f2`](https://github.com/bitcoin/bitcoin/commit/f9117f2) depends: Dependency updates for 0.14.0 (fanquake)
  * [#9469](https://github.com/bitcoin/bitcoin/pull/9469) [`01c4576`](https://github.com/bitcoin/bitcoin/commit/01c4576) depends: Qt 5.7.1 (fanquake)
  * [#9574](https://github.com/bitcoin/bitcoin/pull/9574) [`5ac6687`](https://github.com/bitcoin/bitcoin/commit/5ac6687) depends: Fix QT build on OSX (fanquake)
  * [#9646](https://github.com/bitcoin/bitcoin/pull/9646) [`720b579`](https://github.com/bitcoin/bitcoin/commit/720b579) depends: Fix cross build for qt5.7 (theuni)
  * [#9705](https://github.com/bitcoin/bitcoin/pull/9705) [`6a55515`](https://github.com/bitcoin/bitcoin/commit/6a55515) Add options to override BDB cflags/libs (laanwj)
  * [#8249](https://github.com/bitcoin/bitcoin/pull/8249) [`4e1567a`](https://github.com/bitcoin/bitcoin/commit/4e1567a) Enable (and check for) 64-bit ASLR on Windows (laanwj)
  * [#9758](https://github.com/bitcoin/bitcoin/pull/9758) [`476cc47`](https://github.com/bitcoin/bitcoin/commit/476cc47) Selectively suppress deprecation warnings (jonasschnelli)
  * [#9783](https://github.com/bitcoin/bitcoin/pull/9783) [`6d61a2b`](https://github.com/bitcoin/bitcoin/commit/6d61a2b) release: bump gitian descriptors for a new 0.14 package cache (theuni)
  * [#9789](https://github.com/bitcoin/bitcoin/pull/9789) [`749fe95`](https://github.com/bitcoin/bitcoin/commit/749fe95) build: add –enable-werror and warn on vla’s (theuni)
  * [#9831](https://github.com/bitcoin/bitcoin/pull/9831) [`99fd85c`](https://github.com/bitcoin/bitcoin/commit/99fd85c) build: force a c++ standard to be specified (theuni)

### GUI

  * [#8192](https://github.com/bitcoin/bitcoin/pull/8192) [`c503863`](https://github.com/bitcoin/bitcoin/commit/c503863) Remove URLs from About dialog translations (fanquake)
  * [#8540](https://github.com/bitcoin/bitcoin/pull/8540) [`36404ae`](https://github.com/bitcoin/bitcoin/commit/36404ae) Fix random segfault when closing “Choose data directory” dialog (laanwj)
  * [#8517](https://github.com/bitcoin/bitcoin/pull/8517) [`2468292`](https://github.com/bitcoin/bitcoin/commit/2468292) Show wallet HD state in statusbar (jonasschnelli)
  * [#8463](https://github.com/bitcoin/bitcoin/pull/8463) [`62a5a8a`](https://github.com/bitcoin/bitcoin/commit/62a5a8a) Remove Priority from coincontrol dialog (MarcoFalke)
  * [#7579](https://github.com/bitcoin/bitcoin/pull/7579) [`0606f95`](https://github.com/bitcoin/bitcoin/commit/0606f95) Show network/chain errors in the GUI (jonasschnelli)
  * [#8583](https://github.com/bitcoin/bitcoin/pull/8583) [`c19f8a4`](https://github.com/bitcoin/bitcoin/commit/c19f8a4) Show XTHIN in GUI (rebroad)
  * [#7783](https://github.com/bitcoin/bitcoin/pull/7783) [`4335d5a`](https://github.com/bitcoin/bitcoin/commit/4335d5a) RPC-Console: support nested commands and simple value queries (jonasschnelli)
  * [#8672](https://github.com/bitcoin/bitcoin/pull/8672) [`6052d50`](https://github.com/bitcoin/bitcoin/commit/6052d50) Show transaction size in transaction details window (Cocosoft)
  * [#8777](https://github.com/bitcoin/bitcoin/pull/8777) [`fec6af7`](https://github.com/bitcoin/bitcoin/commit/fec6af7) WalletModel: Expose disablewallet (MarcoFalke)
  * [#8371](https://github.com/bitcoin/bitcoin/pull/8371) [`24f72e9`](https://github.com/bitcoin/bitcoin/commit/24f72e9) Add out-of-sync modal info layer (jonasschnelli)
  * [#8885](https://github.com/bitcoin/bitcoin/pull/8885) [`b2fec4e`](https://github.com/bitcoin/bitcoin/commit/b2fec4e) Fix ban from qt console (theuni)
  * [#8821](https://github.com/bitcoin/bitcoin/pull/8821) [`bf8e68a`](https://github.com/bitcoin/bitcoin/commit/bf8e68a) sync-overlay: Don’t block during reindex (MarcoFalke)
  * [#8906](https://github.com/bitcoin/bitcoin/pull/8906) [`088d1f4`](https://github.com/bitcoin/bitcoin/commit/088d1f4) sync-overlay: Don’t show progress twice (MarcoFalke)
  * [#8918](https://github.com/bitcoin/bitcoin/pull/8918) [`47ace42`](https://github.com/bitcoin/bitcoin/commit/47ace42) Add “Copy URI” to payment request context menu (luke-jr)
  * [#8925](https://github.com/bitcoin/bitcoin/pull/8925) [`f628d9a`](https://github.com/bitcoin/bitcoin/commit/f628d9a) Display minimum ping in debug window (rebroad)
  * [#8774](https://github.com/bitcoin/bitcoin/pull/8774) [`3e942a7`](https://github.com/bitcoin/bitcoin/commit/3e942a7) Qt refactors to better abstract wallet access (luke-jr)
  * [#8985](https://github.com/bitcoin/bitcoin/pull/8985) [`7b1bfa3`](https://github.com/bitcoin/bitcoin/commit/7b1bfa3) Use pindexBestHeader instead of setBlockIndexCandidates for NotifyHeaderTip() (jonasschnelli)
  * [#8989](https://github.com/bitcoin/bitcoin/pull/8989) [`d2143dc`](https://github.com/bitcoin/bitcoin/commit/d2143dc) Overhaul smart-fee slider, adjust default confirmation target (jonasschnelli)
  * [#9043](https://github.com/bitcoin/bitcoin/pull/9043) [`273bde3`](https://github.com/bitcoin/bitcoin/commit/273bde3) Return useful error message on ATMP failure (MarcoFalke)
  * [#9088](https://github.com/bitcoin/bitcoin/pull/9088) [`4e57824`](https://github.com/bitcoin/bitcoin/commit/4e57824) Reduce ambiguity of warning message (rebroad)
  * [#8874](https://github.com/bitcoin/bitcoin/pull/8874) [`e984730`](https://github.com/bitcoin/bitcoin/commit/e984730) Multiple Selection for peer and ban tables (achow101)
  * [#9145](https://github.com/bitcoin/bitcoin/pull/9145) [`924745d`](https://github.com/bitcoin/bitcoin/commit/924745d) Make network disabled icon 50% opaque (MarcoFalke)
  * [#9130](https://github.com/bitcoin/bitcoin/pull/9130) [`ac489b2`](https://github.com/bitcoin/bitcoin/commit/ac489b2) Mention the new network toggle functionality in the tooltip (paveljanik)
  * [#9218](https://github.com/bitcoin/bitcoin/pull/9218) [`4d955fc`](https://github.com/bitcoin/bitcoin/commit/4d955fc) Show progress overlay when clicking spinner icon (laanwj)
  * [#9280](https://github.com/bitcoin/bitcoin/pull/9280) [`e15660c`](https://github.com/bitcoin/bitcoin/commit/e15660c) Show ModalOverlay by pressing the progress bar, allow hiding (jonasschnelli)
  * [#9296](https://github.com/bitcoin/bitcoin/pull/9296) [`fde7d99`](https://github.com/bitcoin/bitcoin/commit/fde7d99) Fix missed change to WalletTx structure (morcos)
  * [#9266](https://github.com/bitcoin/bitcoin/pull/9266) [`2044e37`](https://github.com/bitcoin/bitcoin/commit/2044e37) Bugfix: Qt/RPCConsole: Put column enum in the right places (luke-jr)
  * [#9255](https://github.com/bitcoin/bitcoin/pull/9255) [`9851a84`](https://github.com/bitcoin/bitcoin/commit/9851a84) layoutAboutToChange signal is called layoutAboutToBeChanged (laanwj)
  * [#9330](https://github.com/bitcoin/bitcoin/pull/9330) [`47e6a19`](https://github.com/bitcoin/bitcoin/commit/47e6a19) Console: add security warning (jonasschnelli)
  * [#9329](https://github.com/bitcoin/bitcoin/pull/9329) [`db45ad8`](https://github.com/bitcoin/bitcoin/commit/db45ad8) Console: allow empty arguments (jonasschnelli)
  * [#8877](https://github.com/bitcoin/bitcoin/pull/8877) [`6dc4c43`](https://github.com/bitcoin/bitcoin/commit/6dc4c43) Qt RPC console: history sensitive-data filter, and saving input line when browsing history (luke-jr)
  * [#9462](https://github.com/bitcoin/bitcoin/pull/9462) [`649cf5f`](https://github.com/bitcoin/bitcoin/commit/649cf5f) Do not translate tilde character (MarcoFalke)
  * [#9457](https://github.com/bitcoin/bitcoin/pull/9457) [`123ea73`](https://github.com/bitcoin/bitcoin/commit/123ea73) Select more files for translation (MarcoFalke)
  * [#9413](https://github.com/bitcoin/bitcoin/pull/9413) [`fd7d8c7`](https://github.com/bitcoin/bitcoin/commit/fd7d8c7) CoinControl: Allow non-wallet owned change addresses (jonasschnelli)
  * [#9461](https://github.com/bitcoin/bitcoin/pull/9461) [`b250686`](https://github.com/bitcoin/bitcoin/commit/b250686) Improve progress display during headers-sync and peer-finding (jonasschnelli)
  * [#9588](https://github.com/bitcoin/bitcoin/pull/9588) [`5086452`](https://github.com/bitcoin/bitcoin/commit/5086452) Use nPowTargetSpacing constant (MarcoFalke)
  * [#9637](https://github.com/bitcoin/bitcoin/pull/9637) [`d9e4d1d`](https://github.com/bitcoin/bitcoin/commit/d9e4d1d) Fix transaction details output-index to reflect vout index (jonasschnelli)
  * [#9718](https://github.com/bitcoin/bitcoin/pull/9718) [`36f9d3a`](https://github.com/bitcoin/bitcoin/commit/36f9d3a) Qt/Intro: Various fixes (luke-jr)
  * [#9735](https://github.com/bitcoin/bitcoin/pull/9735) [`ec66d06`](https://github.com/bitcoin/bitcoin/commit/ec66d06) devtools: Handle Qt formatting characters edge-case in update-translations.py (laanwj)
  * [#9755](https://github.com/bitcoin/bitcoin/pull/9755) [`a441db0`](https://github.com/bitcoin/bitcoin/commit/a441db0) Bugfix: Qt/Options: Restore persistent “restart required” notice (luke-jr)
  * [#9817](https://github.com/bitcoin/bitcoin/pull/9817) [`7d75a5a`](https://github.com/bitcoin/bitcoin/commit/7d75a5a) Fix segfault crash when shutdown the GUI in disablewallet mode (jonasschnelli)

### Wallet

  * [#8152](https://github.com/bitcoin/bitcoin/pull/8152) [`b9c1cd8`](https://github.com/bitcoin/bitcoin/commit/b9c1cd8) Remove `CWalletDB*` parameter from CWallet::AddToWallet (pstratem)
  * [#8432](https://github.com/bitcoin/bitcoin/pull/8432) [`c7e05b3`](https://github.com/bitcoin/bitcoin/commit/c7e05b3) Make CWallet::fFileBacked private (pstratem)
  * [#8445](https://github.com/bitcoin/bitcoin/pull/8445) [`f916700`](https://github.com/bitcoin/bitcoin/commit/f916700) Move CWallet::setKeyPool to private section of CWallet (pstratem)
  * [#8564](https://github.com/bitcoin/bitcoin/pull/8564) [`0168019`](https://github.com/bitcoin/bitcoin/commit/0168019) Remove unused code/conditions in ReadAtCursor (jonasschnelli)
  * [#8601](https://github.com/bitcoin/bitcoin/pull/8601) [`37ac678`](https://github.com/bitcoin/bitcoin/commit/37ac678) Add option to opt into full-RBF when sending funds (rebase, original by petertodd) (laanwj)
  * [#8494](https://github.com/bitcoin/bitcoin/pull/8494) [`a5b20ed`](https://github.com/bitcoin/bitcoin/commit/a5b20ed) init, wallet: ParameterInteraction() iff wallet enabled (MarcoFalke)
  * [#8760](https://github.com/bitcoin/bitcoin/pull/8760) [`02ac669`](https://github.com/bitcoin/bitcoin/commit/02ac669) init: Get rid of some `ENABLE_WALLET` (MarcoFalke)
  * [#8696](https://github.com/bitcoin/bitcoin/pull/8696) [`a1f8d3e`](https://github.com/bitcoin/bitcoin/commit/a1f8d3e) Wallet: Remove last external reference to CWalletDB (pstratem)
  * [#8768](https://github.com/bitcoin/bitcoin/pull/8768) [`886e8c9`](https://github.com/bitcoin/bitcoin/commit/886e8c9) init: Get rid of fDisableWallet (MarcoFalke)
  * [#8486](https://github.com/bitcoin/bitcoin/pull/8486) [`ab0b411`](https://github.com/bitcoin/bitcoin/commit/ab0b411) Add high transaction fee warnings (MarcoFalke)
  * [#8851](https://github.com/bitcoin/bitcoin/pull/8851) [`940748b`](https://github.com/bitcoin/bitcoin/commit/940748b) Move key derivation logic from GenerateNewKey to DeriveNewChildKey (pstratem)
  * [#8287](https://github.com/bitcoin/bitcoin/pull/8287) [`e10af96`](https://github.com/bitcoin/bitcoin/commit/e10af96) Set fLimitFree = true (MarcoFalke)
  * [#8928](https://github.com/bitcoin/bitcoin/pull/8928) [`c587577`](https://github.com/bitcoin/bitcoin/commit/c587577) Fix init segfault where InitLoadWallet() calls ATMP before genesis (TheBlueMatt)
  * [#7551](https://github.com/bitcoin/bitcoin/pull/7551) [`f2d7056`](https://github.com/bitcoin/bitcoin/commit/f2d7056) Add importmulti RPC call (pedrobranco)
  * [#9016](https://github.com/bitcoin/bitcoin/pull/9016) [`0dcb888`](https://github.com/bitcoin/bitcoin/commit/0dcb888) Return useful error message on ATMP failure (instagibbs)
  * [#8753](https://github.com/bitcoin/bitcoin/pull/8753) [`f8723d2`](https://github.com/bitcoin/bitcoin/commit/f8723d2) Locked memory manager (laanwj)
  * [#8828](https://github.com/bitcoin/bitcoin/pull/8828) [`a4fd8df`](https://github.com/bitcoin/bitcoin/commit/a4fd8df) Move CWalletDB::ReorderTransactions to CWallet (pstratem)
  * [#8977](https://github.com/bitcoin/bitcoin/pull/8977) [`6a1343f`](https://github.com/bitcoin/bitcoin/commit/6a1343f) Refactor wallet/init interaction (Reaccept wtx, flush thread) (jonasschnelli)
  * [#9036](https://github.com/bitcoin/bitcoin/pull/9036) [`ed0cc50`](https://github.com/bitcoin/bitcoin/commit/ed0cc50) Change default confirm target from 2 to 6 (laanwj)
  * [#9071](https://github.com/bitcoin/bitcoin/pull/9071) [`d1871da`](https://github.com/bitcoin/bitcoin/commit/d1871da) Declare wallet.h functions inline (sipa)
  * [#9132](https://github.com/bitcoin/bitcoin/pull/9132) [`f54e460`](https://github.com/bitcoin/bitcoin/commit/f54e460) Make strWalletFile const (jonasschnelli)
  * [#9141](https://github.com/bitcoin/bitcoin/pull/9141) [`5ea5e04`](https://github.com/bitcoin/bitcoin/commit/5ea5e04) Remove unnecessary calls to CheckFinalTx (jonasschnelli)
  * [#9165](https://github.com/bitcoin/bitcoin/pull/9165) [`c01f16a`](https://github.com/bitcoin/bitcoin/commit/c01f16a) SendMoney: use already-calculated balance (instagibbs)
  * [#9311](https://github.com/bitcoin/bitcoin/pull/9311) [`a336d13`](https://github.com/bitcoin/bitcoin/commit/a336d13) Flush wallet after abandontransaction (morcos)
  * [#8717](https://github.com/bitcoin/bitcoin/pull/8717) [`38e4887`](https://github.com/bitcoin/bitcoin/commit/38e4887) Addition of ImmatureCreditCached to MarkDirty() (spencerlievens)
  * [#9446](https://github.com/bitcoin/bitcoin/pull/9446) [`510c0d9`](https://github.com/bitcoin/bitcoin/commit/510c0d9) SetMerkleBranch: remove unused code, remove cs_main lock requirement (jonasschnelli)
  * [#8776](https://github.com/bitcoin/bitcoin/pull/8776) [`2a524b8`](https://github.com/bitcoin/bitcoin/commit/2a524b8) Wallet refactoring leading up to multiwallet (luke-jr)
  * [#9465](https://github.com/bitcoin/bitcoin/pull/9465) [`a7d55c9`](https://github.com/bitcoin/bitcoin/commit/a7d55c9) Do not perform ECDSA signing in the fee calculation inner loop (gmaxwell)
  * [#9404](https://github.com/bitcoin/bitcoin/pull/9404) [`12e3112`](https://github.com/bitcoin/bitcoin/commit/12e3112) Smarter coordination of change and fee in CreateTransaction (morcos)
  * [#9377](https://github.com/bitcoin/bitcoin/pull/9377) [`fb75cd0`](https://github.com/bitcoin/bitcoin/commit/fb75cd0) fundrawtransaction: Keep change-output keys by default, make it optional (jonasschnelli)
  * [#9578](https://github.com/bitcoin/bitcoin/pull/9578) [`923dc44`](https://github.com/bitcoin/bitcoin/commit/923dc44) Add missing mempool lock for CalculateMemPoolAncestors (TheBlueMatt)
  * [#9227](https://github.com/bitcoin/bitcoin/pull/9227) [`02464da`](https://github.com/bitcoin/bitcoin/commit/02464da) Make nWalletDBUpdated atomic to avoid a potential race (pstratem)
  * [#9764](https://github.com/bitcoin/bitcoin/pull/9764) [`f8af89a`](https://github.com/bitcoin/bitcoin/commit/f8af89a) Prevent “overrides a member function but is not marked ‘override’” warnings (laanwj)
  * [#9771](https://github.com/bitcoin/bitcoin/pull/9771) [`e43a585`](https://github.com/bitcoin/bitcoin/commit/e43a585) Add missing cs_wallet lock that triggers new lock held assertion (ryanofsky)
  * [#9316](https://github.com/bitcoin/bitcoin/pull/9316) [`3097ea4`](https://github.com/bitcoin/bitcoin/commit/3097ea4) Disable free transactions when relay is disabled (MarcoFalke)
  * [#9615](https://github.com/bitcoin/bitcoin/pull/9615) [`d2c9e4d`](https://github.com/bitcoin/bitcoin/commit/d2c9e4d) Wallet incremental fee (morcos)
  * [#9760](https://github.com/bitcoin/bitcoin/pull/9760) [`40c754c`](https://github.com/bitcoin/bitcoin/commit/40c754c) Remove importmulti always-true check (ryanofsky)

### Tests and QA

  * [#8270](https://github.com/bitcoin/bitcoin/pull/8270) [`6e5e5ab`](https://github.com/bitcoin/bitcoin/commit/6e5e5ab) Tests: Use portable #! in python scripts (/usr/bin/env) (ChoHag)
  * [#8534](https://github.com/bitcoin/bitcoin/pull/8534),[#8504](https://github.com/bitcoin/bitcoin/pull/8504) Remove java comparison tool (laanwj,MarcoFalke)
  * [#8482](https://github.com/bitcoin/bitcoin/pull/8482) [`740cff5`](https://github.com/bitcoin/bitcoin/commit/740cff5) Use single cache dir for chains (MarcoFalke)
  * [#8450](https://github.com/bitcoin/bitcoin/pull/8450) [`21857d2`](https://github.com/bitcoin/bitcoin/commit/21857d2) Replace `rpc_wallet_tests.cpp` with python RPC unit tests (pstratem)
  * [#8671](https://github.com/bitcoin/bitcoin/pull/8671) [`ddc3080`](https://github.com/bitcoin/bitcoin/commit/ddc3080) Minimal fix to slow prevector tests as stopgap measure (JeremyRubin)
  * [#8680](https://github.com/bitcoin/bitcoin/pull/8680) [`666eaf0`](https://github.com/bitcoin/bitcoin/commit/666eaf0) Address Travis spurious failures (theuni)
  * [#8789](https://github.com/bitcoin/bitcoin/pull/8789) [`e31a43c`](https://github.com/bitcoin/bitcoin/commit/e31a43c) pull-tester: Only print output when failed (MarcoFalke)
  * [#8810](https://github.com/bitcoin/bitcoin/pull/8810) [`14e8f99`](https://github.com/bitcoin/bitcoin/commit/14e8f99) tests: Add exception error message for JSONRPCException (laanwj)
  * [#8830](https://github.com/bitcoin/bitcoin/pull/8830) [`ef0801b`](https://github.com/bitcoin/bitcoin/commit/ef0801b) test: Add option to run bitcoin-util-test.py manually (jnewbery)
  * [#8881](https://github.com/bitcoin/bitcoin/pull/8881) [`e66cc1d`](https://github.com/bitcoin/bitcoin/commit/e66cc1d) Add some verbose logging to bitcoin-util-test.py (jnewbery)
  * [#8922](https://github.com/bitcoin/bitcoin/pull/8922) [`0329511`](https://github.com/bitcoin/bitcoin/commit/0329511) Send segwit-encoded blocktxn messages in p2p-compactblocks (TheBlueMatt)
  * [#8873](https://github.com/bitcoin/bitcoin/pull/8873) [`74dc388`](https://github.com/bitcoin/bitcoin/commit/74dc388) Add microbenchmarks to profile more code paths (ryanofsky)
  * [#9032](https://github.com/bitcoin/bitcoin/pull/9032) [`6a8be7b`](https://github.com/bitcoin/bitcoin/commit/6a8be7b) test: Add format-dependent comparison to bctest (laanwj)
  * [#9023](https://github.com/bitcoin/bitcoin/pull/9023) [`774db92`](https://github.com/bitcoin/bitcoin/commit/774db92) Add logging to bitcoin-util-test.py (jnewbery)
  * [#9065](https://github.com/bitcoin/bitcoin/pull/9065) [`c9bdf9a`](https://github.com/bitcoin/bitcoin/commit/c9bdf9a) Merge `doc/unit-tests.md` into `src/test/README.md` (laanwj)
  * [#9069](https://github.com/bitcoin/bitcoin/pull/9069) [`ed64bce`](https://github.com/bitcoin/bitcoin/commit/ed64bce) Clean up bctest.py and bitcoin-util-test.py (jnewbery)
  * [#9095](https://github.com/bitcoin/bitcoin/pull/9095) [`b8f43e3`](https://github.com/bitcoin/bitcoin/commit/b8f43e3) test: Fix test_random includes (MarcoFalke)
  * [#8894](https://github.com/bitcoin/bitcoin/pull/8894) [`faec09b`](https://github.com/bitcoin/bitcoin/commit/faec09b) Testing: Include fRelay in mininode version messages (jnewbery)
  * [#9097](https://github.com/bitcoin/bitcoin/pull/9097) [`e536499`](https://github.com/bitcoin/bitcoin/commit/e536499) Rework `sync_*` and preciousblock.py (MarcoFalke)
  * [#9049](https://github.com/bitcoin/bitcoin/pull/9049) [`71bc39e`](https://github.com/bitcoin/bitcoin/commit/71bc39e) Remove duplicatable duplicate-input check from CheckTransaction (TheBlueMatt)
  * [#9136](https://github.com/bitcoin/bitcoin/pull/9136) [`b422913`](https://github.com/bitcoin/bitcoin/commit/b422913) sync_blocks cleanup (ryanofsky)
  * [#9151](https://github.com/bitcoin/bitcoin/pull/9151) [`4333b1c`](https://github.com/bitcoin/bitcoin/commit/4333b1c) proxy_test: Calculate hardcoded port numbers (MarcoFalke)
  * [#9206](https://github.com/bitcoin/bitcoin/pull/9206) [`e662d28`](https://github.com/bitcoin/bitcoin/commit/e662d28) Make test constant consistent with consensus.h (btcdrak)
  * [#9139](https://github.com/bitcoin/bitcoin/pull/9139) [`0de7fd3`](https://github.com/bitcoin/bitcoin/commit/0de7fd3) Change sync_blocks to pick smarter maxheight (on top of [#9196](https://github.com/bitcoin/bitcoin/pull/9196)) (ryanofsky)
  * [#9100](https://github.com/bitcoin/bitcoin/pull/9100) [`97ec6e5`](https://github.com/bitcoin/bitcoin/commit/97ec6e5) tx_valid: re-order inputs to how they are encoded (dcousens)
  * [#9202](https://github.com/bitcoin/bitcoin/pull/9202) [`e56cf67`](https://github.com/bitcoin/bitcoin/commit/e56cf67) bench: Add support for measuring CPU cycles (laanwj)
  * [#9223](https://github.com/bitcoin/bitcoin/pull/9223) [`5412c08`](https://github.com/bitcoin/bitcoin/commit/5412c08) unification of Bloom filter representation (s-matthew-english)
  * [#9257](https://github.com/bitcoin/bitcoin/pull/9257) [`d7ba4a2`](https://github.com/bitcoin/bitcoin/commit/d7ba4a2) Dump debug logs on travis failures (sdaftuar)
  * [#9221](https://github.com/bitcoin/bitcoin/pull/9221) [`9e4bb31`](https://github.com/bitcoin/bitcoin/commit/9e4bb31) Get rid of duplicate code (MarcoFalke)
  * [#9274](https://github.com/bitcoin/bitcoin/pull/9274) [`919db03`](https://github.com/bitcoin/bitcoin/commit/919db03) Use cached utxo set to fix performance regression (MarcoFalke)
  * [#9276](https://github.com/bitcoin/bitcoin/pull/9276) [`ea33f19`](https://github.com/bitcoin/bitcoin/commit/ea33f19) Some minor testing cleanups (morcos)
  * [#9291](https://github.com/bitcoin/bitcoin/pull/9291) [`8601784`](https://github.com/bitcoin/bitcoin/commit/8601784) Remove mapOrphanTransactionsByPrev from DoS_tests (sipa)
  * [#9309](https://github.com/bitcoin/bitcoin/pull/9309) [`76fcd9d`](https://github.com/bitcoin/bitcoin/commit/76fcd9d) Wallet needs to stay unlocked for whole test (morcos)
  * [#9172](https://github.com/bitcoin/bitcoin/pull/9172) [`5bc209c`](https://github.com/bitcoin/bitcoin/commit/5bc209c) Resurrect pstratem’s “Simple fuzzing framework” (laanwj)
  * [#9331](https://github.com/bitcoin/bitcoin/pull/9331) [`c6fd923`](https://github.com/bitcoin/bitcoin/commit/c6fd923) Add test for rescan feature of wallet key import RPCs (ryanofsky)
  * [#9354](https://github.com/bitcoin/bitcoin/pull/9354) [`b416095`](https://github.com/bitcoin/bitcoin/commit/b416095) Make fuzzer actually test CTxOutCompressor (sipa)
  * [#9390](https://github.com/bitcoin/bitcoin/pull/9390),[#9416](https://github.com/bitcoin/bitcoin/pull/9416) travis: make distdir (MarcoFalke)
  * [#9308](https://github.com/bitcoin/bitcoin/pull/9308) [`0698639`](https://github.com/bitcoin/bitcoin/commit/0698639) test: Add CCoinsViewCache Access/Modify/Write tests (ryanofsky)
  * [#9406](https://github.com/bitcoin/bitcoin/pull/9406) [`0f921e6`](https://github.com/bitcoin/bitcoin/commit/0f921e6) Re-enable a blank v1 Tx JSON test (droark)
  * [#9435](https://github.com/bitcoin/bitcoin/pull/9435) [`dbc8a8c`](https://github.com/bitcoin/bitcoin/commit/dbc8a8c) Removed unused variable in test, fixing warning (ryanofsky)
  * [#9436](https://github.com/bitcoin/bitcoin/pull/9436) [`dce853e`](https://github.com/bitcoin/bitcoin/commit/dce853e) test: Include tx data in `EXTRA_DIST` (MarcoFalke)
  * [#9525](https://github.com/bitcoin/bitcoin/pull/9525) [`02e5308`](https://github.com/bitcoin/bitcoin/commit/02e5308) test: Include tx data in `EXTRA_DIST` (MarcoFalke)
  * [#9498](https://github.com/bitcoin/bitcoin/pull/9498) [`054d664`](https://github.com/bitcoin/bitcoin/commit/054d664) Basic CCheckQueue Benchmarks (JeremyRubin)
  * [#9554](https://github.com/bitcoin/bitcoin/pull/9554) [`0b96abc`](https://github.com/bitcoin/bitcoin/commit/0b96abc) test: Avoid potential NULL pointer dereference in `addrman_tests.cpp` (practicalswift)
  * [#9628](https://github.com/bitcoin/bitcoin/pull/9628) [`f895023`](https://github.com/bitcoin/bitcoin/commit/f895023) Increase a sync_blocks timeout in pruning.py (sdaftuar)
  * [#9638](https://github.com/bitcoin/bitcoin/pull/9638) [`a7ea2f8`](https://github.com/bitcoin/bitcoin/commit/a7ea2f8) Actually test assertions in pruning.py (MarcoFalke)
  * [#9647](https://github.com/bitcoin/bitcoin/pull/9647) [`e99f0d7`](https://github.com/bitcoin/bitcoin/commit/e99f0d7) Skip RAII event tests if libevent is built without `event_set_mem_functions` (luke-jr)
  * [#9691](https://github.com/bitcoin/bitcoin/pull/9691) [`fc67cd2`](https://github.com/bitcoin/bitcoin/commit/fc67cd2) Init ECC context for `test_bitcoin_fuzzy` (gmaxwell)
  * [#9712](https://github.com/bitcoin/bitcoin/pull/9712) [`d304fef`](https://github.com/bitcoin/bitcoin/commit/d304fef) bench: Fix initialization order in registration (laanwj)
  * [#9707](https://github.com/bitcoin/bitcoin/pull/9707) [`b860915`](https://github.com/bitcoin/bitcoin/commit/b860915) Fix RPC failure testing (jnewbery)
  * [#9269](https://github.com/bitcoin/bitcoin/pull/9269) [`43e8150`](https://github.com/bitcoin/bitcoin/commit/43e8150) Align struct COrphan definition (sipa)
  * [#9820](https://github.com/bitcoin/bitcoin/pull/9820) [`599c69a`](https://github.com/bitcoin/bitcoin/commit/599c69a) Fix pruning test broken by 2 hour manual prune window (ryanofsky)
  * [#9824](https://github.com/bitcoin/bitcoin/pull/9824) [`260c71c`](https://github.com/bitcoin/bitcoin/commit/260c71c) qa: Check return code when stopping nodes (MarcoFalke)
  * [#9875](https://github.com/bitcoin/bitcoin/pull/9875) [`50953c2`](https://github.com/bitcoin/bitcoin/commit/50953c2) tests: Fix dangling pwalletMain pointer in wallet tests (laanwj)
  * [#9839](https://github.com/bitcoin/bitcoin/pull/9839) [`eddaa6b`](https://github.com/bitcoin/bitcoin/commit/eddaa6b) [qa] Make import-rescan.py watchonly check reliable (ryanofsky)

### Documentation

  * [#8332](https://github.com/bitcoin/bitcoin/pull/8332) [`806b9e7`](https://github.com/bitcoin/bitcoin/commit/806b9e7) Clarify witness branches in transaction.h serialization (dcousens)
  * [#8935](https://github.com/bitcoin/bitcoin/pull/8935) [`0306978`](https://github.com/bitcoin/bitcoin/commit/0306978) Documentation: Building on Windows with WSL (pooleja)
  * [#9144](https://github.com/bitcoin/bitcoin/pull/9144) [`c98f6b3`](https://github.com/bitcoin/bitcoin/commit/c98f6b3) Correct waitforblockheight example help text (fanquake)
  * [#9407](https://github.com/bitcoin/bitcoin/pull/9407) [`041331e`](https://github.com/bitcoin/bitcoin/commit/041331e) Added missing colons in when running help command (anditto)
  * [#9378](https://github.com/bitcoin/bitcoin/pull/9378) [`870cd2b`](https://github.com/bitcoin/bitcoin/commit/870cd2b) Add documentation for CWalletTx::fFromMe member (ryanofsky)
  * [#9297](https://github.com/bitcoin/bitcoin/pull/9297) [`0b73807`](https://github.com/bitcoin/bitcoin/commit/0b73807) Various RPC help outputs updated (Mirobit)
  * [#9613](https://github.com/bitcoin/bitcoin/pull/9613) [`07421cf`](https://github.com/bitcoin/bitcoin/commit/07421cf) Clarify getbalance help string to explain interaction with bumpfee (ryanofsky)
  * [#9663](https://github.com/bitcoin/bitcoin/pull/9663) [`e30d928`](https://github.com/bitcoin/bitcoin/commit/e30d928) Clarify listunspent amount description (instagibbs)
  * [#9396](https://github.com/bitcoin/bitcoin/pull/9396) [`d65a13b`](https://github.com/bitcoin/bitcoin/commit/d65a13b) Updated listsinceblock rpc documentation (accraze)
  * [#8747](https://github.com/bitcoin/bitcoin/pull/8747) [`ce43630`](https://github.com/bitcoin/bitcoin/commit/ce43630) rpc: Fix transaction size comments and RPC help text (jnewbery)
  * [#8058](https://github.com/bitcoin/bitcoin/pull/8058) [`bbd9740`](https://github.com/bitcoin/bitcoin/commit/bbd9740) Doc: Add issue template (AmirAbrams)
  * [#8567](https://github.com/bitcoin/bitcoin/pull/8567) [`85d4e21`](https://github.com/bitcoin/bitcoin/commit/85d4e21) Add default port numbers to REST doc (djpnewton)
  * [#8624](https://github.com/bitcoin/bitcoin/pull/8624) [`89de153`](https://github.com/bitcoin/bitcoin/commit/89de153) build: Mention curl (MarcoFalke)
  * [#8786](https://github.com/bitcoin/bitcoin/pull/8786) [`9da7366`](https://github.com/bitcoin/bitcoin/commit/9da7366) Mandatory copyright agreement (achow101)
  * [#8823](https://github.com/bitcoin/bitcoin/pull/8823) [`7b05af6`](https://github.com/bitcoin/bitcoin/commit/7b05af6) Add privacy recommendation when running hidden service (laanwj)
  * [#9433](https://github.com/bitcoin/bitcoin/pull/9433) [`caa2f10`](https://github.com/bitcoin/bitcoin/commit/caa2f10) Update the Windows build notes (droark)
  * [#8879](https://github.com/bitcoin/bitcoin/pull/8879) [`f928050`](https://github.com/bitcoin/bitcoin/commit/f928050) Rework docs (MarcoFalke)
  * [#8887](https://github.com/bitcoin/bitcoin/pull/8887) [`61d191f`](https://github.com/bitcoin/bitcoin/commit/61d191f) Improve GitHub issue template (fanquake)
  * [#8787](https://github.com/bitcoin/bitcoin/pull/8787) [`279bbad`](https://github.com/bitcoin/bitcoin/commit/279bbad) Add missing autogen to example builds (AmirAbrams)
  * [#8892](https://github.com/bitcoin/bitcoin/pull/8892) [`d270c30`](https://github.com/bitcoin/bitcoin/commit/d270c30) Add build instructions for FreeBSD (laanwj)
  * [#8890](https://github.com/bitcoin/bitcoin/pull/8890) [`c71a654`](https://github.com/bitcoin/bitcoin/commit/c71a654) Update Doxygen configuration file (fanquake)
  * [#9207](https://github.com/bitcoin/bitcoin/pull/9207) [`fa1f944`](https://github.com/bitcoin/bitcoin/commit/fa1f944) Move comments above bash command in build-unix (AmirAbrams)
  * [#9219](https://github.com/bitcoin/bitcoin/pull/9219) [`c4522e7`](https://github.com/bitcoin/bitcoin/commit/c4522e7) Improve windows build instructions using Linux subsystem (laanwj)
  * [#8954](https://github.com/bitcoin/bitcoin/pull/8954) [`932d02a`](https://github.com/bitcoin/bitcoin/commit/932d02a) contrib: Add README for pgp keys (MarcoFalke)
  * [#9093](https://github.com/bitcoin/bitcoin/pull/9093) [`2fae5b9`](https://github.com/bitcoin/bitcoin/commit/2fae5b9) release-process: Mention GitHub release and archived release notes (MarcoFalke)
  * [#8743](https://github.com/bitcoin/bitcoin/pull/8743) [`bae178f`](https://github.com/bitcoin/bitcoin/commit/bae178f) Remove old manpages from contrib/debian in favour of doc/man (fanquake)
  * [#9550](https://github.com/bitcoin/bitcoin/pull/9550) [`4105cb6`](https://github.com/bitcoin/bitcoin/commit/4105cb6) Trim down the XP notice and say more about what we support (gmaxwell)
  * [#9246](https://github.com/bitcoin/bitcoin/pull/9246) [`9851498`](https://github.com/bitcoin/bitcoin/commit/9851498) Developer docs about existing subtrees (gmaxwell)
  * [#9401](https://github.com/bitcoin/bitcoin/pull/9401) [`c2ea1e6`](https://github.com/bitcoin/bitcoin/commit/c2ea1e6) Make rpcauth help message clearer, add example in example .conf (instagibbs)
  * [#9022](https://github.com/bitcoin/bitcoin/pull/9022),[#9033](https://github.com/bitcoin/bitcoin/pull/9033) Document dropping OS X 10.7 support (fanquake, MarcoFalke)
  * [#8771](https://github.com/bitcoin/bitcoin/pull/8771) [`bc9e3ab`](https://github.com/bitcoin/bitcoin/commit/bc9e3ab) contributing: Mention not to open several pulls (luke-jr)
  * [#8852](https://github.com/bitcoin/bitcoin/pull/8852) [`7b784cc`](https://github.com/bitcoin/bitcoin/commit/7b784cc) Mention Gitian building script in doc (Laudaa) (laanwj)
  * [#8915](https://github.com/bitcoin/bitcoin/pull/8915) [`03dd707`](https://github.com/bitcoin/bitcoin/commit/03dd707) Add copyright/patent issues to possible NACK reasons (petertodd)
  * [#8965](https://github.com/bitcoin/bitcoin/pull/8965) [`23e03f8`](https://github.com/bitcoin/bitcoin/commit/23e03f8) Mention that PPA doesn’t support Debian (anduck)
  * [#9115](https://github.com/bitcoin/bitcoin/pull/9115) [`bfc7aad`](https://github.com/bitcoin/bitcoin/commit/bfc7aad) Mention reporting security issues responsibly (paveljanik)
  * [#9840](https://github.com/bitcoin/bitcoin/pull/9840) [`08e0690`](https://github.com/bitcoin/bitcoin/commit/08e0690) Update sendfrom RPC help to correct coin selection misconception (ryanofsky)
  * [#9865](https://github.com/bitcoin/bitcoin/pull/9865) [`289204f`](https://github.com/bitcoin/bitcoin/commit/289204f) Change bitcoin address in RPC help message (marijnfs)

### Miscellaneous

  * [#8274](https://github.com/bitcoin/bitcoin/pull/8274) [`7a2d402`](https://github.com/bitcoin/bitcoin/commit/7a2d402) util: Update tinyformat (laanwj)
  * [#8291](https://github.com/bitcoin/bitcoin/pull/8291) [`5cac8b1`](https://github.com/bitcoin/bitcoin/commit/5cac8b1) util: CopyrightHolders: Check for untranslated substitution (MarcoFalke)
  * [#8557](https://github.com/bitcoin/bitcoin/pull/8557) [`44691f3`](https://github.com/bitcoin/bitcoin/commit/44691f3) contrib: Rework verifybinaries (MarcoFalke)
  * [#8621](https://github.com/bitcoin/bitcoin/pull/8621) [`e8ed6eb`](https://github.com/bitcoin/bitcoin/commit/e8ed6eb) contrib: python: Don’t use shell=True (MarcoFalke)
  * [#8813](https://github.com/bitcoin/bitcoin/pull/8813) [`fb24d7e`](https://github.com/bitcoin/bitcoin/commit/fb24d7e) bitcoind: Daemonize using daemon(3) (laanwj)
  * [#9004](https://github.com/bitcoin/bitcoin/pull/9004) [`67728a3`](https://github.com/bitcoin/bitcoin/commit/67728a3) Clarify `listenonion` (unsystemizer)
  * [#8674](https://github.com/bitcoin/bitcoin/pull/8674) [`bae81b8`](https://github.com/bitcoin/bitcoin/commit/bae81b8) tools for analyzing, updating and adding copyright headers in source files (isle2983)
  * [#8976](https://github.com/bitcoin/bitcoin/pull/8976) [`8c6218a`](https://github.com/bitcoin/bitcoin/commit/8c6218a) libconsensus: Add input validation of flags (laanwj)
  * [#9112](https://github.com/bitcoin/bitcoin/pull/9112) [`46027e8`](https://github.com/bitcoin/bitcoin/commit/46027e8) Avoid ugly exception in log on unknown inv type (laanwj)
  * [#8837](https://github.com/bitcoin/bitcoin/pull/8837) [`2108911`](https://github.com/bitcoin/bitcoin/commit/2108911) Allow bitcoin-tx to parse partial transactions (jnewbery)
  * [#9204](https://github.com/bitcoin/bitcoin/pull/9204) [`74ced54`](https://github.com/bitcoin/bitcoin/commit/74ced54) Clarify CreateTransaction error messages (instagibbs)
  * [#9265](https://github.com/bitcoin/bitcoin/pull/9265) [`31bcc66`](https://github.com/bitcoin/bitcoin/commit/31bcc66) bitcoin-cli: Make error message less confusing (laanwj)
  * [#9303](https://github.com/bitcoin/bitcoin/pull/9303) [`72bf1b3`](https://github.com/bitcoin/bitcoin/commit/72bf1b3) Update comments in ctaes (sipa)
  * [#9417](https://github.com/bitcoin/bitcoin/pull/9417) [`c4b7d4f`](https://github.com/bitcoin/bitcoin/commit/c4b7d4f) Do not evaluate hidden LogPrint arguments (sipa)
  * [#9506](https://github.com/bitcoin/bitcoin/pull/9506) [`593a00c`](https://github.com/bitcoin/bitcoin/commit/593a00c) RFC: Improve style for if indentation (sipa)
  * [#8883](https://github.com/bitcoin/bitcoin/pull/8883) [`d5d4ad8`](https://github.com/bitcoin/bitcoin/commit/d5d4ad8) Add all standard TXO types to bitcoin-tx (jnewbery)
  * [#9531](https://github.com/bitcoin/bitcoin/pull/9531) [`23281a4`](https://github.com/bitcoin/bitcoin/commit/23281a4) Release notes for estimation changes (morcos)
  * [#9486](https://github.com/bitcoin/bitcoin/pull/9486) [`f62bc10`](https://github.com/bitcoin/bitcoin/commit/f62bc10) Make peer=%d log prints consistent (TheBlueMatt)
  * [#9552](https://github.com/bitcoin/bitcoin/pull/9552) [`41cb05c`](https://github.com/bitcoin/bitcoin/commit/41cb05c) Add IPv6 support to qos.sh (jamesmacwhite)
  * [#9542](https://github.com/bitcoin/bitcoin/pull/9542) [`e9e7993`](https://github.com/bitcoin/bitcoin/commit/e9e7993) Docs: Update CONTRIBUTING.md (jnewbery)
  * [#9649](https://github.com/bitcoin/bitcoin/pull/9649) [`53ab12d`](https://github.com/bitcoin/bitcoin/commit/53ab12d) Remove unused clang format dev script (MarcoFalke)
  * [#9625](https://github.com/bitcoin/bitcoin/pull/9625) [`77bd8c4`](https://github.com/bitcoin/bitcoin/commit/77bd8c4) Increase minimum debug.log size to 10MB after shrink (morcos)
  * [#9070](https://github.com/bitcoin/bitcoin/pull/9070) [`7b22e50`](https://github.com/bitcoin/bitcoin/commit/7b22e50) Lockedpool fixes (kazcw)
  * [#8779](https://github.com/bitcoin/bitcoin/pull/8779) [`7008e28`](https://github.com/bitcoin/bitcoin/commit/7008e28) contrib: Delete spendfrom (MarcoFalke)
  * [#9587](https://github.com/bitcoin/bitcoin/pull/9587),[#8793](https://github.com/bitcoin/bitcoin/pull/8793),[#9496](https://github.com/bitcoin/bitcoin/pull/9496),[#8191](https://github.com/bitcoin/bitcoin/pull/8191),[#8109](https://github.com/bitcoin/bitcoin/pull/8109),[#8655](https://github.com/bitcoin/bitcoin/pull/8655),[#8472](https://github.com/bitcoin/bitcoin/pull/8472),[#8677](https://github.com/bitcoin/bitcoin/pull/8677),[#8981](https://github.com/bitcoin/bitcoin/pull/8981),[#9124](https://github.com/bitcoin/bitcoin/pull/9124) Avoid shadowing of variables (paveljanik)
  * [#9063](https://github.com/bitcoin/bitcoin/pull/9063) [`f2a6e82`](https://github.com/bitcoin/bitcoin/commit/f2a6e82) Use deprecated `MAP_ANON` if `MAP_ANONYMOUS` is not defined (paveljanik)
  * [#9060](https://github.com/bitcoin/bitcoin/pull/9060) [`1107653`](https://github.com/bitcoin/bitcoin/commit/1107653) Fix bloom filter init to isEmpty = true (robmcl4)
  * [#8613](https://github.com/bitcoin/bitcoin/pull/8613) [`613bda4`](https://github.com/bitcoin/bitcoin/commit/613bda4) LevelDB 1.19 (sipa)
  * [#9225](https://github.com/bitcoin/bitcoin/pull/9225) [`5488514`](https://github.com/bitcoin/bitcoin/commit/5488514) Fix some benign races (TheBlueMatt)
  * [#8736](https://github.com/bitcoin/bitcoin/pull/8736) [`5fa7b07`](https://github.com/bitcoin/bitcoin/commit/5fa7b07) base58: Improve DecodeBase58 performance (wjx)
  * [#9039](https://github.com/bitcoin/bitcoin/pull/9039) [`e81df49`](https://github.com/bitcoin/bitcoin/commit/e81df49) Various serialization simplifcations and optimizations (sipa)
  * [#9010](https://github.com/bitcoin/bitcoin/pull/9010) [`a143b88`](https://github.com/bitcoin/bitcoin/commit/a143b88) Split up AppInit2 into multiple phases, daemonize after datadir lock errors (laanwj)
  * [#9230](https://github.com/bitcoin/bitcoin/pull/9230) [`c79e52a`](https://github.com/bitcoin/bitcoin/commit/c79e52a) Fix some benign races in timestamp logging (TheBlueMatt)
  * [#9183](https://github.com/bitcoin/bitcoin/pull/9183),[#9260](https://github.com/bitcoin/bitcoin/pull/9260) Mrs Peacock in The Library with The Candlestick (killed main.{h,cpp}) (TheBlueMatt)
  * [#9236](https://github.com/bitcoin/bitcoin/pull/9236) [`7f72568`](https://github.com/bitcoin/bitcoin/commit/7f72568) Fix races for strMiscWarning and `fLargeWork*Found`, make QT runawayException use GetWarnings (gmaxwell)
  * [#9243](https://github.com/bitcoin/bitcoin/pull/9243) [`7aa7004`](https://github.com/bitcoin/bitcoin/commit/7aa7004) Clean up mapArgs and mapMultiArgs Usage (TheBlueMatt)
  * [#9387](https://github.com/bitcoin/bitcoin/pull/9387) [`cfe41d7`](https://github.com/bitcoin/bitcoin/commit/cfe41d7) RAII of libevent stuff using unique ptrs with deleters (kallewoof)
  * [#9472](https://github.com/bitcoin/bitcoin/pull/9472) [`fac0f30`](https://github.com/bitcoin/bitcoin/commit/fac0f30) Disentangle progress estimation from checkpoints and update it (sipa)
  * [#9512](https://github.com/bitcoin/bitcoin/pull/9512) [`6012967`](https://github.com/bitcoin/bitcoin/commit/6012967) Fix various things -fsanitize complains about (sipa)
  * [#9373](https://github.com/bitcoin/bitcoin/pull/9373),[#9580](https://github.com/bitcoin/bitcoin/pull/9580) Various linearization script issues (droark)
  * [#9674](https://github.com/bitcoin/bitcoin/pull/9674) [`dd163f5`](https://github.com/bitcoin/bitcoin/commit/dd163f5) Lock debugging: Always enforce strict lock ordering (try or not) (TheBlueMatt)
  * [#8453](https://github.com/bitcoin/bitcoin/pull/8453),[#9334](https://github.com/bitcoin/bitcoin/pull/9334) Update to latest libsecp256k1 (laanwj,sipa)
  * [#9656](https://github.com/bitcoin/bitcoin/pull/9656) [`7c93952`](https://github.com/bitcoin/bitcoin/commit/7c93952) Check verify-commits on pushes to master (TheBlueMatt)
  * [#9679](https://github.com/bitcoin/bitcoin/pull/9679) [`a351162`](https://github.com/bitcoin/bitcoin/commit/a351162) Access WorkQueue::running only within the cs lock (TheBlueMatt)
  * [#9777](https://github.com/bitcoin/bitcoin/pull/9777) [`8dee822`](https://github.com/bitcoin/bitcoin/commit/8dee822) Handle unusual maxsigcachesize gracefully (jnewbery)
  * [#8863](https://github.com/bitcoin/bitcoin/pull/8863),[#8807](https://github.com/bitcoin/bitcoin/pull/8807) univalue: Pull subtree (MarcoFalke)
  * [#9798](https://github.com/bitcoin/bitcoin/pull/9798) [`e22c067`](https://github.com/bitcoin/bitcoin/commit/e22c067) Fix Issue [#9775](https://github.com/bitcoin/bitcoin/pull/9775) (Check returned value of fopen) (kirit93)
  * [#9856](https://github.com/bitcoin/bitcoin/pull/9856) [`69832aa`](https://github.com/bitcoin/bitcoin/commit/69832aa) Terminate immediately when allocation fails (theuni)

# Credits

Thanks to everyone who directly contributed to this release:

  * accraze
  * adlawren
  * Alex Morcos
  * Alexey Vesnin
  * Amir Abrams
  * Anders Øyvind Urke-Sætre
  * Anditto Heristyo
  * Andrew Chow
  * anduck
  * Anthony Towns
  * Brian Deery
  * BtcDrak
  * Chris Moore
  * Chris Stewart
  * Christian Barcenas
  * Christian Decker
  * Cory Fields
  * crowning-
  * CryptAxe
  * CryptoVote
  * Dagur Valberg Johannsson
  * Daniel Cousens
  * Daniel Kraft
  * Derek Miller
  * djpnewton
  * Don Patterson
  * Doug
  * Douglas Roark
  * Ethan Heilman
  * fsb4000
  * Gaurav Rana
  * Geoffrey Tsui
  * Greg Walker
  * Gregory Maxwell
  * Gregory Sanders
  * Hampus Sjöberg
  * isle2983
  * Ivo van der Sangen
  * James White
  * Jameson Lopp
  * Jeremy Rubin
  * Jiaxing Wang
  * jnewbery
  * John Newbery
  * Johnson Lau
  * Jon Lund Steffensen
  * Jonas Schnelli
  * jonnynewbs
  * Jorge Timón
  * Justin Camarena
  * Karl-Johan Alm
  * Kaz Wesley
  * kirit93
  * Koki Takahashi
  * Lauda
  * leijurv
  * lizhi
  * Luke Dashjr
  * maiiz
  * MarcoFalke
  * Marijn Stollenga
  * Marty Jones
  * Masahiko Hyuga
  * Matt Corallo
  * Matthew King
  * matthias
  * Micha
  * Michael Ford
  * Michael Rotarius
  * Mitchell Cash
  * mrbandrews
  * mruddy
  * Nicolas DORIER
  * nomnombtc
  * Patrick Strateman
  * Pavel Janík
  * Pedro Branco
  * Peter Todd
  * Pieter Wuille
  * poole_party
  * practicalswift
  * R E Broadley
  * randy-waterhouse
  * Richard Kiss
  * Robert McLaughlin
  * rodasmith
  * Russell Yanofsky
  * S. Matthew English
  * Sev
  * Spencer Lievens
  * Stanislas Marion
  * Steven
  * Suhas Daftuar
  * Thomas Snider
  * UdjinM6
  * unsystemizer
  * whythat
  * Will Binns
  * Wladimir J. van der Laan
  * wodry
  * Zak Wilcox

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

