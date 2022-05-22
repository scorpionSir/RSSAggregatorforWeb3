[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/6304a40034f&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![ChainSecurity](https://miro.medium.com/fit/c/64/64/1*DQeE6Ua45H5MtGGv6WFVuA.png)](https://medium.com/chainsecurity?source=post_page
-----6304a40034f--------------------------------)

Published in

[ChainSecurity

](https://medium.com/chainsecurity?source=post_page-----
6304a40034f--------------------------------)

[![Petar
Tsankov](https://miro.medium.com/fit/c/96/96/1*5cqpWtBnq1KgpxEGMpUR8A.png)](/@petar.tsankov?source=post_page
-----6304a40034f--------------------------------)

[Petar Tsankov](/@petar.tsankov?source=post_page-----
6304a40034f--------------------------------)

Follow

Jan 23, 2020

·

7 min read

# Release of Securify v2.0

[![](https://miro.medium.com/max/1400/1*nzCjd-
sgvByh6qqRPmp4TA.png)](https://github.com/eth-sri/securify2)

# We are happy to announce Securify v2.0, the new release of the popular
security scanner for Ethereum smart contracts.

[Securify v2.0](https://github.com/eth-sri/securify2) outperforms state-of-
the-art vulnerability scanners for smart contracts by bringing:

  *  **High precision** , thanks to a _brand new intermediate representation (IR) for Solidity_ and fully declarative context-sensitive static analysis;
  *  **Improved scalability** , leveraging a _fully declarative static analysis_ powered by the efficient [Souffle](https://souffle-lang.github.io/) Datalog engine;
  *  **High vulnerability coverage** , covering _37 distinct security properties_ adopted from the [Smart Contract Weakness Classification Registry](https://github.com/SmartContractSecurity/SWC-registry) and classified by their severity.

Importantly, **Securify v2.0 remains** **free and open-source.** You can
download Securify v2.0 for free on [GitHub](https://github.com/eth-
sri/securify2).

# What does Securify v2.0 support?

  * Ethereum smart contracts written in Solidity 0.5.* and 0.6.*
  * 37 vulnerabilities classified by their severity (the full list of supported vulnerabilities is at the bottom of this article)

# What is new in Securify v2.0?

We now discuss the key technical details and improvements added to Securify
v2.0. These make Securify the most comprehensive and extensible static
analyzer for Solidity.

## 1\. Source code analysis with a new Intermediate Representation

In contrast to the first version of the tool, **Securify v2.0 analyzes source
code** , not EVM bytecode. While analyzing Solidity source code is more
difficult due to the richer structure of the language, it captures important
semantic information that is missing in the bytecode. Importantly, Solidity
precisely captures the storage model of a contract, allowing clear distinction
between variables and mappings, information which is not present in the low-
level hash-based storage model used in the bytecode.

To deal with the complexity of the Solidity language, Securify v2.0 compiles
Solidity into a **new clean and concise Intermediate Representation (IR) for
Solidity**. The new IR is based on the [MLton compiler](http://mlton.org/) for
[Standard ML](https://smlnj.org/) and features:

  *  **Control-flow graph** (CFG) over basic blocks;
  *  **Basic blocks resemble continuations** , usually seen in continuation-passing style, where each block accepts arguments and has a pointer to the next block in the form of a transfer that can pass arguments;
  *  **Static single assignment** (SSA) form for variables and three-address code style for statements.

To illustrate the IR, consider the following Solidity code:

    
    
    contract ToyExample{    function inc(uint x) internal returns (uint){        return x+1;    }    function main() external{        uint res;        for(uint i = 0; i < 42; i++){            res = inc(i);            require(res > 0);        }    }}

Securify v2.0 uses the Solidity compiler to obtain the AST of the contract and
to then transforms it into the following intermediate representation:

![](https://miro.medium.com/max/1400/1*hTQdd3RXfFcCGOm6tbOFtQ.png)

The code follows the single static assignment form (SSA) assigning the result
of each operation to a fresh variable (identified by the statement’s label).
The code is divided into multiple basic blocks. BLOCK00 corresponds to the
definition of function inc and BLOCK01 to the definition of the main function.
Variables are passed between the blocks in the form of arguments (see
annotated edges). This representation is concise, with a limited number of
node types, maintaining only the information necessary for the analysis. The
IR is complete, in the sense that any Solidity smart contract can be mapped to
it.

## 2\. Higher precision via call-site sensitivity

Securify v2.0 achieves higher precision via call-site sensitivity. To get a
better idea of what call-site sensitivity is and how it benefits our analysis,
consider the following example:

    
    
    contract CallSitesTest {    mapping(address => uint) aMapping;    function id(address x) public returns (address){        return x;    }    function unrestrictedStorage(address arbitraryAddress) external{        address a = id(arbitraryAddress);        aMapping[a] = 1;    }    function restrictedStorage(address arbitraryAddress) external {        address b = id(msg.sender);        aMapping[b] = 1;    }}

In the example above, functions _unrestrictedStorage_ and _restrictedStorage_
accept an arbitrary address as an argument from the user. Note that function
_unrestrictedStorage_ allows anyone to write to an arbitrary location in the
storage, while function _restrictedStorage_ allows a user can write only to
_aMapping[msg.sender]_ in the storage (where _msg.sender_ is the user’s
address). To identify this vulnerability, Securify v2.0 tags user-provided
values as untrusted (in this example, it taints _arbitraryAddress_ ) and
propagates the tag along the program’s dependency graph. A precise analysis
would identify that address a is untrusted, reporting function
_unrestrictedStorage_ as vulnerable, while address _b_ is trusted, reporting
function _restrictedStorage_ as safe.

The first version of Securify uses call-site insensitive analysis which tags
the return value of function _id_ as untrusted, because it returns the value
of _arbitraryAddress_ when function _id_ is called by function
_unrestrictedStorage_. In particular, the analysis does not differentiate
whether the function _id_ is called from function _unrestrictedStorage_ or
function _restrictedStorage_. As a result of this imprecision, the analysis
reports the _restrictedStorage_ function as vulnerable too.

In contrast, Securify v2.0 differentiates whether the function id is called
from the function _unrestrictedStorage_ or _restrictedStorage_ (hence the name
call-site sensitive). The additional precision correctly identifies that
address _b_ is not untrusted and, in turn, the function _restrictedStorage_ is
correctly marked as safe.

## 3\. Improved scalability via fully declarative analysis

The first version of Securify implements deeper vulnerability checks in a
combination of Java and Datalog. This slows down the analysis because it
requires passing all intermediate Datalog results to Java.

In contrast, the analysis of Securify v2.0 is fully declarative and
implemented in Datalog. This greatly improves the performance and scalability
of the analysis. Moreover, the fully declarative analysis improves Securify’s
maintenance and extensibility as the declarative patterns are easier to
specify.

## 4\. Higher vulnerability coverage

 **Securify v2.0 supports 37 known vulnerability patterns**. It classifies
them into five severity levels: _critical_ , _high_ , _medium_ , _low_ , and
_info_. Similarly to the first version of the tool, Securify v2.0 reports
violations, which are behaviors that are guaranteed to violate a given
security property, and warnings, which behaviors that may violate the security
property.

# How to use Securify v2.0?

The easiest way to use Security v2.0 using its Docker image as follows:

    
    
    docker run -it -v `pwd`:/share securify /share/myContract.sol

An alternative method to install Securify v2.0 as python package following the
instructions on GitHub:

    
    
    securify myContract.sol

In addition to analyzing a Solidity contract, Securify v2.0 can analyze any
contract available on Etherscan.io:

    
    
    securify -b <contractAddress> — key /path/to/api_key.txt

Users can control which severity levels should be reported by Securify using
the -i argument:

    
    
    securify myContract.sol -i CRITICAL HIGH

Further, users can specify which vulnerability to check for using the -p
argument:

    
    
    securify myContract.sol -p LockedEther

For further help, you can check out the [README](https://github.com/eth-
sri/securify2/blob/master/README.md) instructions on
[GitHub](https://github.com/eth-sri/securify2).

# Supported vulnerabilities

Securify v2.0 supports the following vulnerabilities:

    
    
    |----|-----------------------------------| ---------|---------|  
    | ID | Pattern name                      | Severity | SWC ID  |   
    |----|-----------------------------------| ---------|---------|  
    |  1 | TODAmount                         | Critical | SWC-114 |  
    |  2 | TODReceiver                       | Critical | SWC-114 [|](https://swcregistry.io/docs/SWC-114\)|)  
    |  3 | TODTransfer                       | Critical | SWC-114 |  
    |  4 | UnrestrictedWrite                 | Critical | SWC-124 |   
    |  5 | RightToLeftOverride               | High     | SWC-130 |  
    |  6 | ShadowedStateVariable             | High     | SWC-119 |   
    |  7 | UnrestrictedSelfdestruct          | High     | SWC-106 |  
    |  8 | UninitializedStateVariable        | High     | SWC-109 |  
    |  9 | UninitializedStorage              | High     | SWC-109 |  
    | 10 | UnrestrictedDelegateCall          | High     | SWC-112 |  
    | 11 | DAO                               | High     | SWC-107 |  
    | 12 | ERC20Interface                    | Medium   | -       |  
    | 13 | ERC721Interface                   | Medium   | -       |  
    | 14 | IncorrectEquality                 | Medium   | SWC-132 |  
    | 15 | LockedEther                       | Medium   | -       |  
    | 16 | ReentrancyNoETH                   | Medium   | SWC-107 |  
    | 17 | TxOrigin                          | Medium   | SWC-115 |  
    | 18 | UnhandledException                | Medium   | -       |  
    | 19 | UnrestrictedEtherFlow             | Medium   | SWC-105 |  
    | 20 | UninitializedLocal                | Medium   | SWC-109 |  
    | 21 | UnusedReturn                      | Medium   | SWC-104 |  
    | 22 | ShadowedBuiltin                   | Low      | -       |  
    | 23 | ShadowedLocalVariable             | Low      | -       |  
    | 24 | CallToDefaultConstructor          | Low      | -       |  
    | 25 | CallInLoop                        | Low      | SWC-104 |  
    | 26 | ReentrancyBenign                  | Low      | SWC-107 |  
    | 27 | Timestamp                         | Low      | SWC-116 |  
    | 28 | AssemblyUsage                     | Info     | -       |  
    | 29 | ERC20Indexed                      | Info     | -       |  
    | 30 | LowLevelCalls                     | Info     | -       |  
    | 31 | NamingConvention                  | Info     | -       |  
    | 32 | SolcVersion                       | Info     | SWC-103 |  
    | 33 | UnusedStateVariable               | Info     | -       |  
    | 34 | TooManyDigits                     | Info     | -       |  
    | 35 | ConstableStates                   | Info     | -       |  
    | 36 | ExternalFunctions                 | Info     | -       |   
    | 37 | StateVariablesDefaultVisibility   | Info     | SWC-108 |  
    |----|-----------------------------------| ---------|---------|

The following SWC vulnerabilities do not apply to Solidity contracts with
pragma >=0.8 and are therefore not checked by Securify v2.0:

  * SWC-118 (Incorrect Constructor Name)
  * SWC-129 (Usage of +=)

# How can I contribute?

Securify v2.0 is available on GitHub at <https://github.com/eth-
sri/securify2>.

To contribute, please report any issues and bugs you have encountered while
using the tool.

# Acknowledgments

The following people have contributed to Securify v2.0:

  * Ioannis Sachinoglou
  * Lavrentios Frobeen
  * Frederic Vogel
  * [Dimitar Dimitrov](https://www.sri.inf.ethz.ch/people/dimitar)
  * [Petar Tsankov](https://www.sri.inf.ethz.ch/people/petar)

The team would also like to thank the [Ethereum
Foundation](https://blog.ethereum.org/2018/08/17/ethereum-foundation-grants-
update-wave-3/), which partially funded the development of Securify v2.0.

\--

\--

\--

## [More from ChainSecurity](/chainsecurity?source=post_page-----
6304a40034f--------------------------------)

From the world of secure smart contracts

[Read more from ChainSecurity](/chainsecurity?source=post_page-----
6304a40034f--------------------------------)

## Recommended from Medium

[[![Serafettin
Ozsoy](https://miro.medium.com/fit/c/40/40/1*ndPeAonifp4LprVZd7JCAA.jpeg)](/@serafettinozsoy?source=post_internal_links
---------0----------------------------)

[Serafettin Ozsoy

](/@serafettinozsoy?source=post_internal_links---------
0----------------------------)

## Blockchain and Financial Services Industry in Turkey

![](https://miro.medium.com/focal/112/112/50/50/1*Wo18cIUmfj4r9KJt7REXTw.jpeg)](/@serafettinozsoy/blockchain-
and-financial-services-industry-in-
turkey-b7e192413960?source=post_internal_links---------
0----------------------------)

[[![Judeamanze](https://miro.medium.com/fit/c/40/40/1*dmbNkD5D-u45r44go_cf0g.png)](/@judeamanze662?source=post_internal_links
---------1----------------------------)

[Judeamanze

](/@judeamanze662?source=post_internal_links---------
1----------------------------)

## CPLAY DEFI : A revolutionary project designed to provide solutions to the
decentralised system.

![](https://miro.medium.com/focal/112/112/50/50/1*hxVUBfrwydfNWtyj87er5A.jpeg)](/@judeamanze662/cplay-
defi-a-revolutionary-project-designed-to-provide-solutions-to-the-
decentralised-system-7af732b54e5d?source=post_internal_links---------
1----------------------------)

[[![Mecha
Infinity](https://miro.medium.com/fit/c/40/40/1*Egwk7-Sg18rH4DSELsFJ6g.png)](/@MechaInfinity?source=post_internal_links
---------2----------------------------)

[Mecha Infinity

](/@MechaInfinity?source=post_internal_links---------
2----------------------------)

## Mecha Infinity Decentralization And Blockchain

![](https://miro.medium.com/focal/112/112/50/50/1*6FMfcUGBc3uwe5-Z-mvbIQ.png)](/@MechaInfinity/mecha-
infinity-decentralization-and-
blockchain-5df8738f3d90?source=post_internal_links---------
2----------------------------)

[[![Neironix](https://miro.medium.com/fit/c/40/40/1*mwpSQo32c2GzG69srKbp5g.png)](/@neironix-
io?source=post_internal_links---------3----------------------------)

[Neironix

](/@neironix-io?source=post_internal_links---------
3----------------------------)

## “Market Challenge”: Battle of the TOP 50 companies

![](https://miro.medium.com/focal/112/112/50/50/1*iYugkrIGP6qzWtVwP8FKBg.png)](/@neironix-
io/market-challenge-battle-of-the-
top-50-companies-926e95062647?source=post_internal_links---------
3----------------------------)

[[![Tom
Nguyen](https://miro.medium.com/fit/c/40/40/0*EkzCjyGCeo5LgN47.)](/@mrtomnguyen?source=post_internal_links
---------4----------------------------)

[Tom Nguyen

](/@mrtomnguyen?source=post_internal_links---------
4----------------------------)

## Emrify HIT tokenization of health information: the seed for health
disruptions

](/@mrtomnguyen/emrify-hit-tokenization-of-health-information-the-seed-for-
health-disruptions-b63f3ff42683?source=post_internal_links---------
4----------------------------)

[[![Betdao](https://miro.medium.com/fit/c/40/40/1*E4Bv_8PeLEj9pK3Xmn9rSQ.png)](/@betdao?source=post_internal_links
---------5----------------------------)

[Betdao

](/@betdao?source=post_internal_links---------5----------------------------)

## BetDao Tokenomics

](/@betdao/betdao-tokenomics-312aa2a94f58?source=post_internal_links---------
5----------------------------)

[[![Kent
Barton](https://miro.medium.com/fit/c/40/40/1*D3ufpQxroYPkgpjLbDgaUw.jpeg)](/@seven7hwave?source=post_internal_links
---------6----------------------------)

[Kent Barton

](/@seven7hwave?source=post_internal_links---------
6----------------------------)

in

[Good Audience

](https://medium.com/good-audience?source=post_internal_links---------
6----------------------------)

## Scaling Civility: How to Preserve Ethereum’s Most Crucial Strength

![](https://miro.medium.com/focal/112/112/50/50/1*vCvw_oyhJlZfJD2D2-K8Zw.png)](/good-
audience/scaling-civility-how-to-preserve-ethereums-most-crucial-
strength-439e227e3091?source=post_internal_links---------
6----------------------------)

[[![StakingCabin](https://miro.medium.com/fit/c/40/40/1*Es_zrrRF_SHVBYlw64Uh8g.jpeg)](/@stakingcabin?source=post_internal_links
---------7----------------------------)

[StakingCabin

](/@stakingcabin?source=post_internal_links---------
7----------------------------)

## StakingCabin Joins IXO Network

![](https://miro.medium.com/focal/112/112/50/50/1*TSVlDy7oxPd3dsYdoL1YeQ.jpeg)](/@stakingcabin/stakingcabin-
joins-ixo-network-f713b91b51c9?source=post_internal_links---------
7----------------------------)

[](/?source=post_page-----6304a40034f--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
6304a40034f--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
6304a40034f--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
6304a40034f--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
6304a40034f--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----6304a40034f--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----6304a40034f--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fchainsecurity%2Frelease-
of-securify-v2-0-6304a40034f&source=post_page--------------------------
nav_reg-----------)

[![Petar
Tsankov](https://miro.medium.com/fit/c/176/176/1*5cqpWtBnq1KgpxEGMpUR8A.png)](/@petar.tsankov)

[

## Petar Tsankov

](/@petar.tsankov)

84 Followers

Co-founder and CEO of LatticeFlow

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fusers%2Ff24e3e8bcc2c%2Flazily-enable-
writer-
subscription&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fchainsecurity%2Frelease-
of-
securify-v2-0-6304a40034f&user=Petar+Tsankov&userId=f24e3e8bcc2c&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Robert
Reinhart](https://miro.medium.com/fit/c/40/40/1*Y1utMCT_OiiLycrJ6IgSrw.jpeg)](/@robertreinhart24?source=read_next_recirc
---------0---------------------f8f8617e_e0b4_46f5_95c4_71a045f7f645-------)

[Robert Reinhart

](/@robertreinhart24?source=read_next_recirc---------0---------------------
f8f8617e_e0b4_46f5_95c4_71a045f7f645-------)

## Smart Contract Verification, Simplified

![](https://miro.medium.com/focal/112/112/50/50/1*8K53OXcoHMLkAOwwf88-yQ.png)](/@robertreinhart24/smart-
contract-verification-simplified-ff441110f88a?source=read_next_recirc---------
0---------------------f8f8617e_e0b4_46f5_95c4_71a045f7f645-------)

[[![Mark
Mathis](https://miro.medium.com/fit/c/40/40/1*GwGIgHi9ngu0bsSrr_v79g.png)](/@cipherz?source=read_next_recirc
---------1---------------------f8f8617e_e0b4_46f5_95c4_71a045f7f645-------)

[Mark Mathis

](/@cipherz?source=read_next_recirc---------1---------------------
f8f8617e_e0b4_46f5_95c4_71a045f7f645-------)

## Production Contract Security — Part 2

![](https://miro.medium.com/focal/112/112/50/50/1*jJJQY1PsW1u-k1xkaI5qLA.png)](/@cipherz/production-
contract-security-part-2-b631a67b6b4e?source=read_next_recirc---------1
---------------------f8f8617e_e0b4_46f5_95c4_71a045f7f645-------)

[[![Ankita
Sinha](https://miro.medium.com/fit/c/40/40/1*IScePEXQTV_Icxoxabqlwg.jpeg)](/@sinhaankitasinha31?source=read_next_recirc
---------2---------------------f8f8617e_e0b4_46f5_95c4_71a045f7f645-------)

[Ankita Sinha

](/@sinhaankitasinha31?source=read_next_recirc---------2---------------------
f8f8617e_e0b4_46f5_95c4_71a045f7f645-------)

## What are Zero-Knowledge Techniques and Zero-Knowledge Proofs (ZKPs)

![https://www.google.com/url?sa=i&url=https%3A%2F%2Fblog.goodaudience.com%2Fwhat-
is-zero-knowledge-proof-and-why-you-should-
care-36977d738339&psig=AOvVaw1N660zHA-
BrU6QhDFadXTL&ust=1648226867293000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCOjn8tqZ3_YCFQAAAAAdAAAAABAD](https://miro.medium.com/focal/112/112/50/50/0*YgSRxuKHBg25l_EN.png)](/@sinhaankitasinha31/what-
are-zero-knowledge-techniques-and-zero-knowledge-proofs-
zkps-9e0c236c829e?source=read_next_recirc---------2---------------------
f8f8617e_e0b4_46f5_95c4_71a045f7f645-------)

[[![Oleg
Kubrakov](https://miro.medium.com/fit/c/40/40/1*EE7PQXb1v7xgo29gvrnopg.jpeg)](/@OlegKubrakov?source=read_next_recirc
---------3---------------------f8f8617e_e0b4_46f5_95c4_71a045f7f645-------)

[Oleg Kubrakov

](/@OlegKubrakov?source=read_next_recirc---------3---------------------
f8f8617e_e0b4_46f5_95c4_71a045f7f645-------)

in

[Godly Dev

](https://medium.com/godly-dev?source=read_next_recirc---------3
---------------------f8f8617e_e0b4_46f5_95c4_71a045f7f645-------)

## An overlooked attack vector in smart contracts security

![](https://miro.medium.com/focal/112/112/50/50/0*zeaj1IRIZT3O9e4Y)](/godly-
dev/an-overlooked-attack-vector-in-smart-contracts-
security-4d9182a77c96?source=read_next_recirc---------3---------------------
f8f8617e_e0b4_46f5_95c4_71a045f7f645-------)

[Help

](https://help.medium.com/hc/en-us)

[Status

](https://medium.statuspage.io)

[Writers

](https://about.medium.com/creators/)

[Blog

](https://blog.medium.com)

[Careers

](/jobs-at-medium/work-at-medium-959d1a85284e)

[Privacy

](https://policy.medium.com/medium-privacy-policy-f03bf92035c9)

[Terms

](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f)

[About

](https://medium.com/about?autoplay=1)

[Knowable

](https://knowable.fyi)

