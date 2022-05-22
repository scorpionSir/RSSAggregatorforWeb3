Close

Menu

  * [About Us](https://blog.sigmaprime.io/pages/about-us.html)

[![Blog Logo](./imgs/blog/sigp-logo-black.png)](https://blog.sigmaprime.io/)
__Menu

# Dapper Ethereum Smart Contract Wallet: Security Review

[Mehdi Zerouali](https://blog.sigmaprime.io/author/mehdi-zerouali.html) | Thu
09 May 2019 Updated on Thu 09 May 2019 Estimated read time: 11 min

_Sigma Prime was commercially engaged by Dapper Labs to perform a time-boxed
security review of an Ethereum smart contract wallet. This post details 3
vulnerabilities which were identified in the course of this assessment, and
subsequently resolved. The full security assessment report for this engagement
and the supporting test suite are
available[here](https://github.com/sigp/public-audits/tree/master/)._

# Executive Summary

Dapper Labs commercially engaged Sigma Prime to perform a security review of
the Dapper smart contract wallet. The review focused on security aspects of
the smart contract's Solidity implementation, though general recommendations
and informational comments relating to code quality and gas usage
optimisations were also provided.

Sigma Prime's assessment identified some issues and improvements, which were
promptly addressed by Dapper Labs. Reviewers note that despite these issues,
the smart contracts were particularly well written and the code quality was of
a high calibre.

This review was initially conducted on commit 2d68897.

Retesting activities targeted the commit 6b3784e, which contains code
modifications and corrections made as a result of the initial report. Sigma
Prime's retesting concluded that the smart contract remediations were
effective and no further vulnerabilities were identified.

The testing team identified a total of six (6) issues during this assessment,
of which:

  * One (1) is classified as high risk;
  * One (1) is classified as medium risk;
  * Four (4) are classified as informational.

**All these issues have been acknowledged and addressed by the Dapper Labs
development team.**

# Introduction

[Dapper Labs](https://www.dapperlabs.com/) is a Blockchain startup renowned
for the creation of [CryptoKitties](https://www.cryptokitties.co/), a
collectable game using the [ERC-721 standard](http://erc721.org/) on Ethereum.
This post details a recent review of _Dapper_ , an Ethereum smart contract
wallet designed and developed by Dapper Labs.

Dapper is a smart contract wallet for Ethereum which provides an authorisation
mapping, enabling fine-grained and user-sovereign control over the wallet's
funds and assets (e.g. Ether, ERC223 tokens, non-fungible tokens, etc.). This
wallet also allows users to play supported decentralised applications (e.g.
[CryptoKitties](https://www.cryptokitties.co/),
[Decentraland](https://decentraland.org/),
[Etheremon](https://www.etheremon.com/)) without having to worry about paying
for transaction fees on the Ethereum network (i.e. gas).

This wallet implements the following features:

  * **Multi-signature support (two-of-two) with a co-signing check:** co-signing addresses can be other contracts (to potentially enforce additional verification);
  * **Recovery operation:** a backup transaction that removes all existing authorisations and sets a new device key as the sole administrator.

The main smart contract of this wallet is `CoreWallet` and can be used in two
forms:

  * **Standalone full wallet** , by deploying the `FullWallet` contract;
  * **Cloned wallet** , by leveraging a `WalletFactory` contract.

The `CoreWallet` provides support for _1-of-1_ or _2-of-2_ multi-signatures. A
**_signer_** is an individual entity that signs invocations and interacts with
the wallet. A signer must be **authorised** to invoke actions on the wallet.
Optionally, a **_signer_** can also have a **_co-signer_** , which places an
additional requirement of needing signatures from both the **_signer_** and
the **_co-signer_** to invoke functions on the wallet.

A **_signer_** can be removed from the **authorised** users by setting its
**_co-signer_** to zero.

The `CoreWallet` smart contract supports four different methods of interacting
with the wallet:

  1. A **_signer_** invokes a method directly when there are no **_co-signers_** (`invoke0`);
  2. A **_signer_** supplies the **_co-signer_** 's signature with the method invocation (`invoke1SignerSends`);
  3. A **_co-signer_** supplies the **_signer_** 's signature with the method invocation (`invoke1CosignerSends`);
  4. Anyone explicitly supplies both the **_signer_** and **_co-signer_** signatures with the method invocation (`invoke2`).

The `CoreWallet` also supports chaining calls. This allows authorised users to
perform multiple operations such as sending ETH, sending tokens (e.g. ERC20,
ERC223, ERC721), or administering the wallet (e.g. change authorisations)
within a single Ethereum transaction. Chaining calls considerably reduces the
gas costs associated with each operation.

Furthermore, the Dapper smart contract wallet supports interaction with a
range of standards and protocols, namely:

  * **[`ERC721`](https://github.com/ethereum/EIPs/issues/721) (Non-Fungible Token Standard)** allowing the interaction of this wallet with NFTs (non-fungible tokens) through the `ERC721Received` interface;
  * **[`ERC223`](https://github.com/ethereum/EIPs/issues/223) (ERC223 Token Standard)** describes a token standard to help prevent accidental sending of tokens to contracts, by implementing a `tokenFallback` function;
  * **[`ERC165`](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-165.md) (Standard Interface Detection)** creates a standard method to publish and detect the interfaces implemented by a smart contract;
  * **[`ERC1271`](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-1271.md) (Standard Signature Validation Method)** provides a standard way for contracts to validate signatures.

**All vulnerabilities identified during this assessment have been remediated
by Dapper Labs.**

# Detailed Findings

This section provides a detailed description of three vulnerabilities
identified within the Dapper smart contract wallet. Each vulnerability has a
severity classification which is determined by its likelihood and impact.
Please refer to our [full report](https://github.com/sigp/public-
audits/blob/master/dapper-wallet/review.pdf) for further information.

## Replay Attacks on Co-Signer Signed Invocations (Resolved)

### Background information

Replay attacks (sometimes also referred to as _playback_ attacks) are a class
of network attacks where a malicious actor purposefully and fraudulently re-
transmits a message (or in a Blockchain context, a transaction) with the
intention of causing the message to be successfully processed more than once.
This category of attacks can affect a wide variety of protocols and systems
(e.g authentication protocols such as remote key-less vehicles, speech
recognition devices, etc. ), and can be seen as a simple _"Man-in-the-Middle"_
attack.

One way to mitigate replay attacks is to introduce cryptographic nonces, which
can be seen as numbers (pseudo-random or incremental/sequential numbers) which
can ensure, **_when used appropriately_** , that old messages/transactions
cannot be successfully repeated.

### The Vulnerability

Due to the **_co-signer_** `nonce` not being incremented upon signing, the
signed messages by co-signers are able to be replayed if the co-signer is re-
assigned as another co-signer, or later assigned as a signer (with or without
another co-signer).

Let's take a look at the `authorizations` and `nonces` mappings:

    
    
    mapping(uint256 => uint256) public authorizations;
    mapping(address => uint256) public nonces;
    

In this storage mapping, the `uint256` keys actually represent authorised
wallet addresses which are prepended with an `authVersion` number. This
mapping therefore keeps track of who is authorised to access the wallet and
the version number allows the wallet to clear all existing authorisations by
incrementing the `authVersion` variable.

The `nonces` mapping stores the current nonce for each authorised address.

This nonce is then checked and incremented in the `invoke1SignerSends`,
`invoke1CosignerSends`, and `invoke2` functions (`invoke0` does not need to
check/increment the nonce as the native built-in nonce mechanism of Ethereum
transactions protects against replay attacks).

In `invoke1SignerSends`:

    
    
    uint256 nonce = nonces[msg.sender];
    
    // calculate hash
    bytes32 operationHash = keccak256(
        abi.encodePacked(
        EIP191_PREFIX,
        EIP191_VERSION_DATA,
        this,
        nonce,
        data));
    
    // recover cosigner
    address cosigner = ecrecover(operationHash, v, r, s);
    

In `invoke1CosignerSends`:

    
    
    bytes32 operationHash = keccak256(
        abi.encodePacked(
        EIP191_PREFIX,
        EIP191_VERSION_DATA,
        this,
        nonce,
        data));
    
    // recover signer
    address signer = ecrecover(operationHash, v, r, s);
    

The signer nonce is explicitly passed as an argument to the
`invoke1CosignerSends` function while it is fetched in the `nonces` mapping
for `invoke1SignerSends`.

In `invoke2`, both signatures are submitted, along with the **_signer_**
nonce:

    
    
    bytes32 operationHash = keccak256(
                abi.encodePacked(
                EIP191_PREFIX,
                EIP191_VERSION_DATA,
                this,
                nonce,
                data));
    
    // recover signer and cosigner
    address signer = ecrecover(operationHash, v[0], r[0], s[0]);
    address cosigner = ecrecover(operationHash, v[1], r[1], s[1]);
    

We notice that only the signer nonce is incremented:

    
    
    //increment signer nonce
    nonces[signer]++;
    

The following scenario illustrates the ability to replay:

  1. **Step 1:** `Message A`: (Send ETH to Trent) — `invoke2(signer=Alice, Cosigner=Bob, from=Alice)`   
Here `Message A` has been signed by Bob with a nonce of 1.  

  2. **Step 2:** `Message B`: (Bob gets authorised as a **_signer_** and his own **_cosigner_** ) — `setAuthorized(signer=Bob, authorizedAddress=Bob)`   
Here Bob becomes authorised to invoke methods on the wallet, without a
**_cosigner_**

  3. **Step 3:** `Message A'`(Replay to send ETH to Trent) — `invoke2(signer=Bob, Cosigner=Bob, from=Trent)`   
Here Trent successfully retransmits `Message A` to get the wallet to send ETH
an additional time.

There are two valid exploitation scenarios:

  1. The cosigner becomes a cosigner for another party;
  2. The cosigner becomes a signer and cosigner for themselves.

We have written dedicated tests using the `pytest` framework to illustrate
this attack, please refer to our test suite
([`tests/test_replay.py`](https://github.com/sigp/public-
audits/blob/master/dapper-wallet/tests/tests/test_replay.py))

### Recommendation

We suggested a couple of possible solutions to mitigate the replay attacks on
the `CoreWallet` smart contract:

  1. Integrate the nonce of the **_cosigner_** into the messages:

    * By utilising the nonce of both the **_cosigner_** and the **_signer_** , as well as incrementing accordingly, the **_cosigner_** 's signed message would only be valid for the combination of **__**nonce pair. Once this has occurred, then`nonces[cosigner]++` will force the signed message to become invalid;
    * The drawback for this proposed solution is that the **_cosigner_** is then blocked from performing any other transactions that may increment the nonce. This means that a **_cosigner_** will be able to deny the transaction execution of any message they cosigned and messages will be required to come in order. (Nonces may be out of sync and messages will not get through). 
  2. Introduce a `message_nonce`:

    * By using a message nonce, the signature validation becomes message specific;
    * The downside of this method is that two competing messages from disjoint signers will be _conflicting_ and only one message would be successfully processed. This creates a competition/race between messages.

### Resolution

The development team fixed this vulnerability in commit 6b3784e by including
the signing address as part of the signature data. This effectively ties the
signature nonce to the signing address creating a unique signature for each
signing address and signer nonce.

## Outdated ERC-721 Implementation (Resolved)

### Background information

The `ERC-721` standard describes how to build non-fungible tokens on the
Ethereum Blockchain. All `ERC-721` compliant tokens must implement the
interface available [here](http://erc721.org/). In particular, all wallets
must implement the `onERC721Received()` function as specified in the standard.

### The Vulnerability

The Dapper Ethereum smart contract wallet (`CoreWallet`, deployed in its
cloned and full versions) inherits the `ERC721Receiver` contract and as such,
implements the `onERC721Received()` function.

Due to the fact that Dapper Labs were the original creators of the `ERC-721`
standard, the method of calling `onERC721Received()` conforms to a _draft_ of
the `ERC-721` standard, not the final version. The final version of the
standard was not published until after the `CryptoKitties` smart contracts
were released, hence utilisation of the outdated implementation.

Specifically, the `onERC721Received()` function was not up to date with the
latest `ERC-721` standard as not take the correct arguments as specified by
the standard:

  * **`ERC-721` standard**: `onERC721Received(address, address, uint256, bytes)`
  * **Dapper implementation** : `onERC721Received(address, uint256, bytes)`

This function is to be called by `ERC-721` contracts when a
`safeTransferFrom()` is made to a contract address. Typically, these contracts
would implement a function which verifies that the recipient address, when a
contract, is compliant with the `ERC721TokenReceiver` interface, expecting the
`onERC721Received()` function of the Dapper contract to return `0x150b7a02`
(equals to
`bytes4(keccak256("onERC721Received(address,address,uint256,bytes)"))`).

Since the Dapper wallet returns `0xf0b9e5ba` (equals to `bytes4
(keccak256("onERC721Received(address,uint256,bytes)"))`), any `ERC-721` token
(other than _CryptoKitties_ ) safe transfer to a Dapper smart contract wallet
would effectively fail.

Here's how an `ERC-721` token could implement this:

    
    
    bytes4 private constant _ERC721_RECEIVED = 0x150b7a02;
    
    function safeTransferFrom(address from, address to, uint256 tokenId, bytes _data) public {
      transferFrom(from, to, tokenId);
      require(_checkOnERC721Received(from, to, tokenId, _data));
    }
    
    
    function _checkOnERC721Received(address from, address to, uint256 tokenId, bytes _data) internal returns (bool) {
      if (!to.isContract()) {
          return true;
      }
    
      bytes4 retval = IERC721Receiver(to).onERC721Received(msg.sender, from, tokenId, _data);
      return (retval == _ERC721_RECEIVED);
        }
    

### Recommendation

We suggested changing `ERC721Receiver` and `ERC721Receivable` contracts to
comply with the latest `ERC-721` standard. Specifically, updating the
`onERC721Received()` function to take an additional address (i.e. the address
calling the `safeTransferFrom()` function).

### Resolution

The development team updated the related smart contracts to support both the
final ERC721 specification `ERC721ReceiverFinal`, and the previous one,
`ERC721ReceiverDraft` (used for example by the _CryptoKitties_ contract).

## ERC-721 Event Log Poisoning (Resolved)

### Background information

Events and logs in Ethereum are traditionally used to facilitate
communications between smart contract and user interfaces (i.e front ends such
as web or mobile applications). For example, in the context of non-fungible
tokens, an ERC-721 transfer will emit the `Transfer` event log, prompting user
interfaces to notify the related user(s) that a particular collectable was
received.

### The Vulnerability

The Dapper Ethereum smart contract wallet (`CoreWallet` , deployed in its
cloned and full versions) inherits the `ERC721Receiver` contract and therefore
implements the `onERC721Received()` function, which when called emits the
`ERC721Received` event log.

This function can be called externally by any Ethereum account, resulting in
`ERC721Received` events being generated arbitrarily.

Furthermore, the `_from`, `_tokenId`, and `_data` event parameters can be
forged to any arbitrary value, allowing attackers to potentially replicate and
use existing asset IDs (e.g. valid _CryptoKitties_ token IDs), which could
generate confusion for DApp users.

We have developed a dedicated test using `pytest` to illustrate this issue
(see `tests/test_event_poisoning.py`).

_Note: Front-end software that potentially consumes these events (e.g. mobile
application, web application, browser extension) were outside the scope of
this assessment_

### Recommendation

We suggested the following approach to the development team:

  1. Implementing the following `require` statement in the `onERC721Received()` function:

    
    
    require(msg.sender.doesContractImplementInterface(0x150b7a02));
    

This would ensure that only `ERC-721` compliant contracts can call this
function and trigger the `ERC721Received` event emission. Please note that
this additional restriction can be bypassed by creating a malicious contract
which complies with the `ERC-721` interface and implements an external
function (e.g. `generateLogInWallet()` which calls `wallet.onERC721Received()`
).

  1. Another more restrictive approach could be to whitelist contracts which are authorised to call the `onERC721Received()` function.

### Resolution

The two `onERC721Received()` functions no longer emit the `ERC721Received`
event log in the updated version of the assessed smart contract.

# Conclusion

This review focused exclusively on the Dapper smart contract wallet. The
contract was particularly well written and all vulnerabilities identified
during this assessment were acknowledged and addressed by the development
team.

At the time of writing, Sigma Prime is in the process of performing a security
assessment on various off-chain components (APIs, browser extension,
databases, cloud infrastructure, etc.) supporting this wallet.

Sigma Prime is very supportive of efforts that bring Ethereum to a broad
audience and we've enjoyed working with Dapper Labs on this assessment. If
you're interested in a security review by Sigma Prime, feel free to reach out
to us via [email](mailto:contact@sigmaprime.io).

[ __Twitter ](https://twitter.com/share?text=Dapper Ethereum Smart Contract
Wallet: Security Review&url=https://blog.sigmaprime.io/dapper-wallet-
review.html) [ __Facebook
](https://www.facebook.com/sharer/sharer.php?u=https://blog.sigmaprime.io/dapper-
wallet-review.html) [ __Google+
](https://plus.google.com/share?url=https://blog.sigmaprime.io/dapper-wallet-
review.html)

[ethereum](https://blog.sigmaprime.io/tag/ethereum.html)[blockchain](https://blog.sigmaprime.io/tag/blockchain.html)[wallet](https://blog.sigmaprime.io/tag/wallet.html)[cybersecurity](https://blog.sigmaprime.io/tag/cybersecurity.html)[smart
contract audit](https://blog.sigmaprime.io/tag/smart-contract-
audit.html)[solidity security review](https://blog.sigmaprime.io/tag/solidity-
security-review.html)

![Mehdi Zerouali](https://blog.sigmaprime.io/imgs/authors/mz.jpg)

#### [Mehdi Zerouali](https://blog.sigmaprime.io/author/mehdi-zerouali.html)

Mehdi is a co-founder and a director of Sigma Prime. He is a penetration
tester particularly interested in decentralised systems, with a strong focus
on the Ethereum platform.

__Sydney, Australia

