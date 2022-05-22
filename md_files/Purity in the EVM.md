Close

Menu

  * [About Us](https://blog.sigmaprime.io/pages/about-us.html)

[![Blog Logo](./imgs/blog/sigp-logo-black.png)](https://blog.sigmaprime.io/)
__Menu

# Purity in the EVM

[Paul Hauner](https://blog.sigmaprime.io/author/paul-hauner.html) | Fri 08
June 2018 Updated on Fri 08 June 2018 Estimated read time: 14 min

# Purity in the EVM

_This document provides a definition of purity suitable for a signature
validation contract. It provides resources for designing an on-chain purity-
checking contract._

**This document is not official advice. Errors may be present.**

This document is available as a Git repository at [github.com/sigp/opcode-
purity](https://github.com/sigp/opcode-purity).

## Background

This document is the result of "reverse engineering" the following two
contracts and the majority any credit attributed to this document is deserving
of their authors:

  * [Serpent Purity Checker](https://github.com/ethereum/research/blob/master/impurity/check_for_impurity.se) in [ethereum/research](https://github.com/ethereum/research) by Vitalik Buterin.
  * [LLL Port](https://github.com/ethereum/casper/pull/143/files) of the above Serpent Purity Checker by [@ralexstokes](https://github.com/ralexstokes).

Vitalik's contract was ported to LLL by Alex with the intention that it would
be used to verify the "purity" of signature validation (valsig) contracts in
the (now deprecated) EIP-1011 proposal. Before we discuss the concept of
purity, first we should understand the purpose of valsig contracts.

Valsig contracts were to be used to abstract the signature validation of vote
and logout messages -- allowing validators to implement arbitrarily complex
signature schemes instead of just relying upon transaction signatures (ECDSA).

Unfortunately, the use of arbitrary external valsig contracts opens the
possibility for a damaging attack vector whereby a validator can, because they
control signature validation, double-vote then prevent punishment by ensuring
that the slash validation fails whilst the vote validation succeeds. Such an
attack can be eliminated by reducing the space of possible valsig contracts to
only those which are "pure": those which will always return the result given
the same signature to validate.

Therefore, EIP-1011 required that each valsig contract must have its purity
approved by an on-chain smart contract before it is permitted to be used for
validation. The contract that scanned and determined valsig contact purity was
called the _purity checker_ and it is the focus of this document.

## Definition of Purity

This contract provides the following definition of purity for an Ethereum
smart-contract:

_A contract is considered pure if it will always return the same result given
sufficient gas for execution and the same transaction data and value.
Specifically, it may read the data and value fields of a transaction but no
other transaction information, it may not read block information and it must
not read from or write to storage._

There is some room for subjectivity in the definition of purity, specifically
in what can be considered "inputs" to the "function" that is the smart
contract. This definition includes only transaction data and value (\\(T_d\\),
\\(T_v\\) in the Yellow Paper) but given no concrete definition of what is
transaction "context" (as opposed to transaction "input") a definition of
purity can be conceived which permits the origin address (derived from
\\(T_w\\), \\(T_r\\) and \\(T_s\\)) to be read as well. Such a definition is
not compatible with signature validation contracts and is therefore excluded
from this document.

## Detecting Impurity On-Chain

This document assumes that detecting the purity of a contract is going to be
performed on the contracts bytecode. This is more accurate than performing the
action on source code because it eliminates any quirks which may be introduced
during compilation. This also has the benefit of allowing on-chain
verification of one contract by another as a contract may go and retrieve the
bytecode of another contract and iterate through it inside the EVM.

The process of determining the purity of some bytecode will generally involve
starting at the first byte (which must be an opcode), attempting to match it
against the opcodes defined in the table, performing some action depending on
the purity of that opcode (e.g., permit, deny or attempt address detection)
and then repeating the process on the next opcode.

It is important to note that not each byte in some bytecode must be an opcode,
instead it may be a parameter supplied to a `PUSH` opcode. The Serpent
contract provided in the Background section provides an example of how one can
keep track of opcodes and parameters throughout the iteration process in order
to allow for back-searching of opcodes and parameters as required for address
detection in call-type opcodes (see Address Detection Techniques).

The rest of the document focuses on defining the purity categories for each
opcode, outlining techniques that can be used to deal with call-type opcodes
and then provides some detail as to why certain opcodes have been categorised
as pure or potentially-impure.

## Impurity Categories

There are three classifications for impure opcodes: always impure, potentially
impure call-type and future impure opcodes. Each category is described below.

### Always Impure

These opcodes have no use other than to mutate state, return mutable state or
provide context about the execution environment. Any contract which includes
an "always impure" opcode should be immediately considered impure.

### Future Impure Opcodes

These opcodes are assumed to be reserved for future impure opcodes. At the
time of writing, there is no formal declaration that this is the case and this
judgement is solely based off the authors informal conversations with the
Ethereum community.

### Potentially Impure Call-Type

Call-type opcodes (see the table for a listing) may execute code at some other
address. It is possible for an external call to be either pure or impure,
depending on the address specified for the call. The use of a call-type opcode
can only be considered pure if the address specified is:

  * An address that has already been determined to be pure.
  * Any of the precompile addresses within the range of `0x0000000000000000000000000000000000000001` to `0x0000000000000000000000000000000000000008`. _Note: the purity of these contracts is yet to be confirmed._

See the Address Detection Techniques section for some techniques for
extracting the address supplied to a call-type opcode from bytecode.

**Any call to an externally-owned (non-contract) address should be considered
impure**. This is because it can potentially have impure code deployed to it.

## Impure Opcode Table

Opcode Value | Mnemonic | Impurity Category  
---|---|---  
`0x31` | BALANCE | Always Impure  
`0x32` | ORIGIN | Always Impure  
`0x33` | CALLER | Always Impure  
`0x3a` | GASPRICE | Always Impure  
`0x3b` | EXTCODESIZE | Always Impure  
`0x3c` | EXTCODECOPY | Always Impure  
`0x40` | BLOCKHASH | Always Impure  
`0x41` | COINBASE | Always Impure  
`0x42` | TIMESTAMP | Always Impure  
`0x43` | NUMBER | Always Impure  
`0x44` | DIFFICULTY | Always Impure  
`0x45` | GASLIMIT | Always Impure  
`0x46` \- `0x4F` | Range of future impure opcodes | Future Impure Opcodes  
`0x54` | SLOAD | Always Impure  
`0x55` | SSTORE | Always Impure  
`0xf0` | CREATE | Always Impure  
`0xff` | SELFDESTRUCT | Always Impure  
`0xf1` | [CALL](CALL) | Potentially Impure Call-Type  
`0xf2` | [CALLCODE](CALLCODE) | Potentially Impure Call-Type  
`0xf4` | [DELEGATECALL](DELEGATECALL) | Potentially Impure Call-Type  
`0xfa` | [STATICCALL](STATICCALL) | Potentially Impure Call-Type  
* `0xfb` | CREATE2 | Always Impure  
  
_* Opcodes which were not implemented at the time of writing, but the author
has an expectation they will be implemented in the future._

## Address Detection Techniques

Call-type opcodes (see the table for a listing) can only be considered pure if
they call a specific set of addresses (see Potentially Impure Call-Types).
Therefore, in order to permit some call-type opcodes it is necessary to
determine the called address from the bytecode. This section describes methods
which may be used to find the address supplied to the call-type opcode with
certainty.

The code which may place an address on the stack for call-type opcode can be
arbitrarily complex and only discoverable by executing said code. To allow
purity checking within a single Ethereum transaction the techniques here are
simplistic and will provide false positives (indicating impurity). However,
these techniques should never produce false negatives (indicating purity).

Techniques are provided in a Python-like pseudo-code and concrete examples can
be found in the two contracts specified in the Background section.

### Convenience Functions

First two convenience functions are declared; `get_opcode(n)` and
`get_last_opcode_param(n)`.

#### Convenience Function `get_opcode(n)`

Returns the `n`'th opcode declared in the subject `bytecode[]`.

If `n` is out of bounds of `bytecode[]` the function returns `None`.

Example:

    
    
    ADD = 0x01
    PUSH2 = 0x61
    
    bytecode = [PUSH2, 2, 1, ADD]
    get_opcode(0)
    # 3
    get_opcode(2)
    # None
    

#### Convenience Function `get_last_opcode_param(n)`

Returns the final parameter supplied to the `n`'th opcode declared in the
subject `bytecode[]`.

If `n` is out of bounds of `bytecode[]` or the `n`'th opcode does not have
parameters the function returns `None`.

Example:

    
    
    ADD = 0x01
    PUSH2 = 0x61
    
    bytecode = [PUSH2, 2, 1, ADD]
    get_last_opcode_param(0)
    # 1
    get_last_opcode_param(1)
    # None
    get_last_opcode_param(2)
    # None
    

### Address Detection Functions

Four functions are now declared which return an address if a specific pattern
of opcodes is found to precede a call-type opcode. If all of these functions
return `None`, then the contract should be assumed to be impure.

Each function takes an input `c` which is the index of the call-type opcode in
question. It is assumed that the on-chain purity checking contract is
iterating over the bytecode in question and each time it detects a call-type
opcode it runs these functions to attempt to detect the address being called.

#### Address Detection Function #1

    
    
    PUSH1 = 0x60
    PUSH32 = 0x7f
    
    def address_detector_1(c):
        if PUSH1 <= get_opcode(c-2) <= PUSH32:
            return get_last_opcode_param(c-2)
        else:
            return None
    

#### Address Detection Function #2

    
    
    SUB = 0x03
    GAS = 0x5a
    PUSH1 = 0x60
    PUSH32 = 0x7f
    
    def address_detector_2(c):
        if (get_opcode(c-1) == SUB and
           get_opcode(c-2) == GAS and
           PUSH1 <= get_opcode(c-3) <= PUSH32):
            return get_last_opcode_param(c-3)
        else:
            return None
    

#### Address Detection Function #3

    
    
    GAS = 0x5a
    SWAP1 = 0x90
    
    def address_detector_3(c):
        if (get_opcode(c-1) == GAS OR
           get_opcode(c-1) == SWAP1):
            return get_last_opcode_param(c-2)
        else:
            return None
    

#### Address Detection Function #4

    
    
    DUP1 = 0x80
    DUP16 = 0x8f
    
    def address_detector_4(c):
        if (DUP1 <= get_opcode(c-1) <= DUP16):
            return get_last_opcode_param(c-2)
        else:
            return None
    

## Opcode Listing

This section contains an opcode-by-opcode listing of each defined opcode. For
each opcode the following is provided:

  * **Summary** : a brief description of what the opcode does.
  * **Impurity Reasoning** : a reference demonstrating impurity reasoning.
  * **Potential Attack** : a scenario which assumes some attacker has deployed a contract and wishes to be able to have some pre-determined or ad hoc control of the return result of the contract. This section does not exhaustively list potential attacks, it simply provides an example for demonstrative purposes.

Specifications of opcodes can be found in Appendix H of the [Ethereum Yellow
Paper](https://ethereum.github.io/yellowpaper/paper.pdf).

### BALANCE

**Summary:** Returns the balance of some address.  
**References:** [`py-evm/evm/vm/logic/context.py:
balance()`](https://github.com/ethereum/py-
evm/blob/fa5817b1db12bd61907ac0123fa9ef1a6fb928d1/evm/vm/logic/context.py#L16)  
**Impurity Reasoning:** reads state.  
**Potential Attack:** An attacker may influence the return value of a contract
call by altering the balance of some external account.

### ORIGIN

**Summary:** Returns the address of the sender of the transaction which
triggered execution. In Solidity, this is `tx.origin`.  
**References:** [`py-evm/evm/vm/logic/context.py:
origin()`](https://github.com/ethereum/py-
evm/blob/fa5817b1db12bd61907ac0123fa9ef1a6fb928d1/evm/vm/logic/context.py#L21)  
**Impurity Reasoning:** reads illegal transaction context.  
**Potential Attack:** An attacker may influence the return value of a contract
call by varying the private key with which a transaction is signed.

### CALLER

**Summary:** Returns the address directly responsible for the execution. In
Solidity, this is `msg.sender`.  
**References:** [`py-evm/evm/vm/logic/context.py:
caller()`](https://github.com/ethereum/py-
evm/blob/fa5817b1db12bd61907ac0123fa9ef1a6fb928d1/evm/vm/logic/context.py#L29)  
**Impurity Reasoning:** reads illegal transaction context.  
**Potential Attack:** An attacker may influence the return value of a contract
call by varying the private key with which a transaction is signed or using an
intermediary contract to alter the `CALLER` value.

### GASPRICE

**Summary:** Returns the current gas price.  
**References:** [`py-evm/evm/vm/logic/context.py:
gasprice()`](https://github.com/ethereum/py-
evm/blob/fa5817b1db12bd61907ac0123fa9ef1a6fb928d1/evm/vm/logic/context.py#L105)  
**Impurity Reasoning:** reads illegal transaction context.  
**Potential Attack:** An attacker may influence the return value of a contract
call by using some means to alter the gas price (e.g., directly controlling
block proposers).

### EXTCODESIZE

**Summary:** Returns the size of the code held at some address.  
**References:** [`py-evm/evm/vm/logic/context.py:
extcodesize()`](https://github.com/ethereum/py-
evm/blob/fa5817b1db12bd61907ac0123fa9ef1a6fb928d1/evm/vm/logic/context.py#L110)  
**Impurity Reasoning:** reads state.  
**Potential Attack:** An attacker may influence the return value of a
contract.  
call by deploying code to some pre-computed address.

### EXTCODECOPY

**Summary:** Copies some amount of code at some address to some position in
memory.  
**References:** [`py-evm/evm/vm/logic/context.py:
extcodecopy()`](https://github.com/ethereum/py-
evm/blob/fa5817b1db12bd61907ac0123fa9ef1a6fb928d1/evm/vm/logic/context.py#L133)  
**Impurity Reasoning:** reads state.  
**Potential Attack:** An attacker may influence the return value of a contract
call by deploying code to some pre-computed address.

### BLOCKHASH

**Summary:** Returns the hash of some past block (within the previous 256
complete blocks).  
**References:** [`py-evm/evm/vm/logic/block.py:
blockhash()`](https://github.com/ethereum/py-
evm/blob/fa5817b1db12bd61907ac0123fa9ef1a6fb928d1/evm/vm/logic/block.py#L7)  
**Impurity Reasoning:** reads state.  
**Potential Attack:** An attacker may influence the return value of a contract
call by controlling some portion of block proposers and selecting block hashes
based upon how they will influence the contract call.

### COINBASE

**Summary:** Returns the beneficiary address of the block.  
**References:** [`py-evm/evm/vm/logic/block.py:
coinbase()`](https://github.com/ethereum/py-
evm/blob/fa5817b1db12bd61907ac0123fa9ef1a6fb928d1/evm/vm/logic/block.py#L13)  
**Impurity Reasoning:** reads state.  
**Potential Attack:** An attacker may influence the return value of a contract
call by controlling some portion of block proposers and declaring the
beneficiary address based upon how it will influence the contract call.

### TIMESTAMP

**Summary:** Returns the timestamp of the block.  
**References:** [`py-evm/evm/vm/logic/block.py:
timestamp()`](https://github.com/ethereum/py-
evm/blob/fa5817b1db12bd61907ac0123fa9ef1a6fb928d1/evm/vm/logic/block.py#L17)  
**Impurity Reasoning:** reads state.  
**Potential Attack:** An attacker may influence the return value of a contract
call by controlling some portion of block proposers and declaring the
timestamp based upon how it will influence the contract call.

### NUMBER

**Summary:** Returns the number of the block (count of blocks in the chain
since genesis).  
**References:** [`py-evm/evm/vm/logic/block.py:
number()`](https://github.com/ethereum/py-
evm/blob/fa5817b1db12bd61907ac0123fa9ef1a6fb928d1/evm/vm/logic/block.py#L21)  
**Impurity Reasoning:** reads state.  
**Potential Attack:** An attacker may influence the return value of a contract
call by selecting in which block a transaction should be included.

### DIFFICULTY

**Summary:** Returns the block difficulty.  
**References:** [`py-evm/evm/vm/logic/block.py:
difficulty()`](https://github.com/ethereum/py-
evm/blob/fa5817b1db12bd61907ac0123fa9ef1a6fb928d1/evm/vm/logic/block.py#L25)  
**Impurity Reasoning:** reads state.  
**Potential Attack:** An attacker may influence the return value of a contract
call by assuming some control of the collective hash rate and modifying it
based upon how it will influence the contract call.

### GASLIMIT

**Summary:** Returns the block gas limit.  
**References** [`py-evm/evm/vm/logic/block.py:
gaslimit()`](https://github.com/ethereum/py-
evm/blob/fa5817b1db12bd61907ac0123fa9ef1a6fb928d1/evm/vm/logic/block.py#L29)  
**Impurity Reasoning:** reads state.  
**Potential Attack:** An attacker may influence the return value of a contract
call by using some means to alter the gas limit (e.g., directly controlling
block proposers or spamming the network).

### SLOAD

**Summary:** Returns a word from storage.  
**References** [`py-evm/evm/vm/logic/storage.py:
sload()`](https://github.com/ethereum/py-
evm/blob/fa5817b1db12bd61907ac0123fa9ef1a6fb928d1/evm/vm/logic/storage.py#L55)  
**Impurity Reasoning:** reads state.  
**Potential Attack:** At the time of writing the author is not aware of any
attack using SLOAD if all other purity directives are followed. However,
attacks could be imagined if combined with the `SLOAD` opcodes (other attacks
may be possible).

### SSTORE

**Summary:** Saves some word to storage.  
**References:** [`py-evm/evm/vm/logic/storage.py:
sstore()`](https://github.com/ethereum/py-
evm/blob/fa5817b1db12bd61907ac0123fa9ef1a6fb928d1/evm/vm/logic/storage.py#L11)  
**Impurity Reasoning:** reads and mutates state.  
**Potential Attack:** At the time of writing the author is not aware of any
attack using SSTORE if all other purity directives are followed. However,
attacks could be imagined if combined with the `SSTORE` or `GAS` opcodes
(other attacks may be possible).

### CREATE

**Summary:** Creates a new account given some code.  
**References:** [`py-evm/evm/vm/logic/system.py:
Create.__call__()`](https://github.com/ethereum/py-
evm/blob/fa5817b1db12bd61907ac0123fa9ef1a6fb928d1/evm/vm/logic/system.py#L110)  
**Impurity Reasoning:** reads and mutates state.  
**Potential Attack:** At the time of writing the author is not aware of any
attack using CREATE if all other purity directives are followed. However,
attacks could be imagined if combined with the `EXTCODESIZE` opcode (other
attacks may be possible).

### SELFDESTRUCT

**Summary:** Registers the account for deletion, sending remaining Ether to
some address.  
**References:** [`py-evm/evm/vm/logic/system.py:
_selfdestruct()`](https://github.com/ethereum/py-
evm/blob/fa5817b1db12bd61907ac0123fa9ef1a6fb928d1/evm/vm/logic/system.py#L74)  
**Impurity Reasoning:** reads and mutates state.  
**Potential Attack:** An attacker may self-destruct a contract, causing all
future calls to it to fail.

### CALL

**Summary:** Message-calls to some address.  
**References:** [`py-evm/evm/vm/logic/call.py:
Call()`](https://github.com/ethereum/py-
evm/blob/fa5817b1db12bd61907ac0123fa9ef1a6fb928d1/evm/vm/logic/call.py#L134)  
**Potential Impurity Reasoning:** Executes code from another account.  
**Potential Attack:** An attacker may call an impure contract and use its
return data.

### CALLCODE

**Summary:** Execute the code of some other account using the state of this
account.  
**References:** [`py-evm/evm/vm/logic/call.py:
CallCode()`](https://github.com/ethereum/py-
evm/blob/fa5817b1db12bd61907ac0123fa9ef1a6fb928d1/evm/vm/logic/call.py#L169)  
**Potential Impurity Reasoning:** Executes code from another account.  
**Potential Attack:** An attacker may callcode an impure contract and read or
mutate state.

### DELEGATECALL

**Summary:** Execute the code of some other account using the state of this
account whilst retaining the same values for `sender` and `value`.  
**References:** [`py-evm/evm/vm/logic/call.py:
DelegateCall()`](https://github.com/ethereum/py-
evm/blob/fa5817b1db12bd61907ac0123fa9ef1a6fb928d1/evm/vm/logic/call.py#L203)  
**Potential Impurity Reasoning:** Executes code from another account.  
**Potential Attack:** An attacker may delegate an impure contract and read or
mutate state.

### STATICCALL

**Summary:** Message-calls to some address without persisting state
modifications.  
**References:** [`py-evm/evm/vm/logic/call.py:
StaticCall()`](https://github.com/ethereum/py-
evm/blob/fa5817b1db12bd61907ac0123fa9ef1a6fb928d1/evm/vm/logic/call.py#L306)  
**Potential Impurity Reasoning:** Executes code from another account.  
**Potential Attack:** An attacker may call an impure contract and use its
return data.

### CREATE2

_This opcode has not been implemented at the time of writing._

**Summary:** Creates a new account given some code and some nonce (as opposed
to `CREATE` which uses the current account nonce).  
**References:**
[EIP86](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-86.md).  
**Impurity Reasoning:** Reads and mutates state.  
**Potential Attack:** An attacker could craft a contract which succeeds the
first time it is called, but fails all other times.

[ __Twitter ](https://twitter.com/share?text=Purity in the
EVM&url=https://blog.sigmaprime.io/evm-purity.html) [ __Facebook
](https://www.facebook.com/sharer/sharer.php?u=https://blog.sigmaprime.io/evm-
purity.html) [ __Google+
](https://plus.google.com/share?url=https://blog.sigmaprime.io/evm-
purity.html)

[ethereum](https://blog.sigmaprime.io/tag/ethereum.html)[purity](https://blog.sigmaprime.io/tag/purity.html)[opcodes](https://blog.sigmaprime.io/tag/opcodes.html)

![Paul Hauner](https://blog.sigmaprime.io/imgs/authors/ph-profile.jpg)

#### [Paul Hauner](https://blog.sigmaprime.io/author/paul-hauner.html)

Paul is a co-founder of Sigma Prime and a core team member of Sydney Homeless
Connect. He has a keen interest in consensus mechanisms and information
security. @paulhauner on Github.

__Sydney, Australia

