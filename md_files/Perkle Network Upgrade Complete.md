[![esprezzo-logo@2x](https://blog.esprezzo.io/hs-fs/hubfs/esprezzo-
logo@2x.png?width=261&name=esprezzo-logo@2x.png)](https://esprezzo.io)

  * [Products](https://esprezzo.io/products)
  * [Developers](https://esprezzo.io/developers)
  * [About](https://esprezzo.io/about)
  * [Blog](https://blog.esprezzo.io)
  * [GET AN INVITE](https://esprezzo.io/invite)

##  [The Esprezzo Blog](https://blog.esprezzo.io)

# Perkle Network Upgrade Complete

by [Esprezzo Team](https://blog.esprezzo.io/author/esprezzo-team) on February
5, 2020

  * [Tweet](https://twitter.com/share)
  *   * 

On Monday we began and completed a network and protocol upgrade for Perkle.
This was a planned hard fork to enable several important new features, patches
and performance improvements.

While working on smart contract templates and testing some newer Solidity
functionality we ran into an issue with a new
[opcode](https://medium.com/@blockchain101/solidity-bytecode-and-opcode-
basics-672e9b1a88c2) only available in Constantinople and later forks of
Ethereum. Specifically the
[EXTCODEHASH](https://eips.ethereum.org/EIPS/eip-1052) opcode (EIP-1052),
which makes tasks such as checking another contract’s bytecode or analyzing
and whitelisting contracts cheaper (less
[gas](https://blockgeeks.com/guides/ethereum-gas/) needed).

Example of opcode in use in the snippet below:

`assembly { codehash := extcodehash(account) }`

**![EIP-1052-extcodehash-ethereum-opcode](https://blog.esprezzo.io/hs-
fs/hubfs/EIP-2052-extcodehash-opcode.png?width=800&name=EIP-2052-extcodehash-
opcode.png)**

Because we really want to use this new opcode, and generally stay up to date
with the leading version of the Ethereum protocol, we upgraded [Perkle](/what-
is-perkle-prkl?_ga=2.214146007.1399505960.1580857005-705690896.1578529603) to
be more in line with the Muir Glacier release of the protocol. The fork went
smoothly.

Thank you to [STEX](https://app.stex.com/en/trade/pair/ETH/PRKL) for minimal
downtime and mining pool owners, who were quick to update. As of publishing
time for this post, Perkle miners looking for updated mining pools can go with
the [official Perkle mining pool](https://mine-perkle.esprezzo.io/#/) or
[Comining](https://comining.io/).

At block 3,100,000 old clients became incompatible. If you’re managing a
Perkle mining pool and haven’t upgraded your clients yet, you’ll want to do
that as soon as possible to avoid mining blocks that are destined to become
orphans.

##### The latest software is here:

      Binary releases - <https://github.com/esprezzo/perkle/releases> 

      Source code - <https://github.com/esprezzo/perkle>

Here’s a list of the opcodes and EIPs included in this Perkle update:

  * **[EIP-145](https://eips.ethereum.org/EIPS/eip-145)** : Bitwise shifting (improves messaging speed and reduces cost)
  * **[EIP-152](https://eips.ethereum.org/EIPS/eip-152)** : Add Blake2 compression function F precompile (creates new interoperability capabilities for smart contracts)
  * **[EIP-1014](https://eips.ethereum.org/EIPS/eip-1014)** : An effort to facilitate scaling using state channels and off-chain transactions
  * **[EIP-1052](https://eips.ethereum.org/EIPS/eip-1052)** : Large scale code execution optimization (allowing contracts to check a contract’s bytecode without needing the bytecode itself, saving wasted gas)
  * **[EIP-1108](https://eips.ethereum.org/EIPS/eip-1108)** : Reduces alt_bn128 precompile gas costs
  * **[EIP-1234](https://eips.ethereum.org/EIPS/eip-1234)** : Reduces block reward from 3 to 2 and postpones difficulty increase (this needs to be updated in the official block explorer, which is still showing a reward of 3)
  * **[EIP-1344](https://eips.ethereum.org/EIPS/eip-1344)** : Adds ChainID opcode
  * **[EIP-1884](https://defipulse.com/blog/how-ethereums-istanbul-network-upgrade-affects-defi/)** : Reprices certain resource-intensive opcodes to more closely match computing resources consumed
  * **[EIP-2028](https://eips.ethereum.org/EIPS/eip-2028)** : Reduces gas cost for calling transaction data (improves scalability)
  * **[EIP-2200](https://eips.ethereum.org/EIPS/eip-2200)** : Implements net gas metering (enables new smart contract storage capabilities)Rebalance net-metered SSTORE gas cost with consideration of SLOAD gas cost
  * **[EIP-2384](https://eips.ethereum.org/EIPS/eip-2384)** : Delays Ethereum [difficulty bomb](https://www.investopedia.com/news/what-ethereums-difficulty-bomb/)

Look out for our next blog post, which will be about the smart contract work
that led to this fork!

Have an idea for a smart contract-based application? Is the thought of
mastering Solidity or the cost of experimenting on Ethereum holding you back?
Check out [Esprezzo Dispatch](/introducing-dispatch)! Dispatch is a tool for
creating automated alerts and notifications using data from blockchains,
cryptocurrencies and smart contracts.

[![Learn more about Dispatch](https://no-
cache.hubspot.com/cta/default/4632193/122c6731-2c8e-4846-9367-5009f0e9d126.png)](https://cta-
redirect.hubspot.com/cta/redirect/4632193/122c6731-2c8e-4846-9367-5009f0e9d126)

And if you're interested in joining our community, we're chatting on Discord;
[join us](https://discord.gg/uuCT89F)!

Topics: [Product Updates](https://blog.esprezzo.io/tag/product-updates),
[Perkle](https://blog.esprezzo.io/tag/perkle)

![Esprezzo Team](https://blog.esprezzo.io/hubfs/favicon-196-1.png)

###### [Esprezzo Team](https://blog.esprezzo.io/author/esprezzo-team)

We're on a mission to make it easier and faster for anyone to use blockchain
data to drive decisions and workflow automations. Whether you're a DeFi
enthusiast, crypto trader or developer building revolutionary blockchain-based
applications, we're here to help you bring your vision to reality.

[Facebook](https://www.facebook.com/esprezzoapp/)
[LinkedIn](https://www.linkedin.com/company/esprezzo-app/)
[Twitter](https://twitter.com/esprezzoapp)

## Esprezzo and blockchain-related news for developers and business leaders

Best practices and industry news for growing your business with decentralized
and blockchain-integrated applications

### Subscribe Here!

### Recent Posts

### Posts by Tags

  * [News (14)](https://blog.esprezzo.io/tag/news)
  * [Events (12)](https://blog.esprezzo.io/tag/events)
  * [Product Updates (10)](https://blog.esprezzo.io/tag/product-updates)
  * [Perkle (9)](https://blog.esprezzo.io/tag/perkle)
  * [Research & Analysis (7)](https://blog.esprezzo.io/tag/research-analysis)
  * [Education (6)](https://blog.esprezzo.io/tag/education)
  * [Partnerships (5)](https://blog.esprezzo.io/tag/partnerships)
  * [Blockchain 101 (4)](https://blog.esprezzo.io/tag/blockchain-101)
  * [Press Release (1)](https://blog.esprezzo.io/tag/press-release)

See all

### Technology

[Perkle Protocol](https://esprezzo.io/perkle)

[GitHub](https://github.com/esprezzo)

### Company

[About](https://esprezzo.io/about)

[Blog](https://blog.esprezzo.io)

[Contact](https://esprezzo.io/about#contact)

### Connect

[Discord](https://discord.gg/uuCT89F)

[Twitter](https://twitter.com/esprezzoapp)

[LinkedIn](https://www.linkedin.com/company/esprezzo-app/)

**Stay in the know**

Get news and product updates from Esprezzo

[![esprezzo_logo_red-white_sept2020@2x](https://blog.esprezzo.io/hs-
fs/hubfs/esprezzo_logo_red-
white_sept2020@2x.png?width=263&name=esprezzo_logo_red-
white_sept2020@2x.png)](https://esprezzo.io)

©2020 Esprezzo. All rights reserved.

