[![](https://substackcdn.com/image/fetch/w_96,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F37b09348-f4f1-47a2-b9e0-a2007299e6e4_256x256)](https://proofofwork.news)

# [Proof of Work](https://proofofwork.news)

SubscribeSign in

Share this post

Proof of Work #68

proofofwork.news

Copy link

Twitter

Facebook

Email

# Proof of Work #68

[Eric Meltzer](https://substack.com/profile/138320-eric-meltzer)

May 31, 2019

[Share](javascript:void\(0\))

Hi from Beijing!

As always, the Chinese crypto scene is fascinating. Last year it felt like an
absolute circus—over the top parties, actresses buying crypto, conferences at
massive venues—and now a lot of that has quieted down, and 90% of the
speculators have exited the scene. The people who are left are grizzled
veterans, who’ve survived the receeding wave of speculation and also the total
shutdown of fiat exchanges in China. The number one thing that strikes me
every time I come here is how many people think purely in terms of stacking
Bitcoin (and a few premium alts) rather than in terms of accumulating more
fiat money.

There are also a lot more truly interesting projects coming out of China these
days. I was initially skeptical that the crypto scene would truly end up Asia-
centered as a result of the US regulatory environment being so hostile (a
skepticism shared by a lot of my Chinese crypto friends) but these days I am
beginning to think that will actually come to pass. The hardware (miners),
infrastructure (mining installations), and financial institutions (the crypto
exchanges) are all here, and that ends up creating a fertile ground for new
projects. The number one blocker to this in my opinion was the lure of cheap
cash via ICO, but that seems to have come and gone, and now there are a lot of
very technical and interesting teams here building stuff. Over the next few
issues I’m going to discuss a few of the best ones in detail!

More next week, thanks as always for reading!

#### Bitcoin & Friends

 **[BitcoinOptech](https://bitcoinops.org/en/newsletters/) on Bitcoin**

  *  **Proposed new opcode for transaction output commitments:**  Jeremy Rubin posted to the Bitcoin-Dev mailing list a proposal to soft fork in an `OP_CHECKOUTPUTSHASHVERIFY` opcode that allows a Bitcoin address to require the transaction spending it include a certain set of outputs. This enables a restricted form of Bitcoin covenants which can be used to reduce the amount of data that needs to be placed onchain in certain situations, potentially reducing costs or improving privacy in those cases. For details, please see this newsletter’s [special section about the proposal](https://bitcoinops.org/en/newsletters/2019/05/29/#proposed-transaction-output-commitments).

  *  _Final stack empty:_  in legacy, segwit, and proposed [bip-tapscript](https://github.com/sipa/bips/blob/bip-schnorr/bip-tapscript.mediawiki) scripts, a script evaluates successfully if it contains exactly one element that is  _true_. Russell O’Connor [raised](https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2019-May/016935.html) a point he’s [raised before](https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2018-December/016558.html) and requested that this opportunity be taken to require tapscript only evaluate successfully if it ends with an empty stack. Pieter Wuille [replied](https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2019-May/016947.html) that his work on [miniscript](http://bitcoin.sipa.be/miniscript/miniscript.html) (see [Newsletter #32](https://bitcoinops.org/en/newsletters/2019/02/05/)) showed that, for the subset of scripts miniscript will create, this change in semantics will at most save 0.25 vbytes per tapscript. Also, although the change may simplify development for anyone writing scripts by hand, it’s a bit risky as every development guide to Script written to date teaches that scripts must terminate with a  _true_ value on the stack. Wuille summarized, “so overall this feels like something with marginal costs, but also at most marginal benefits.”

  *  _Move the oddness byte:_  Bitcoin public keys are most naturally specified using an X,Y coordinate pair, as was done in the early days of Bitcoin with [uncompressed public keys](https://btcinformation.org/en/developer-guide#public-key-formats). However, because a valid pubkey must be on the elliptic curve, it’s possible to find both valid Y coordinates (one odd, one even) for any given X coordinate given the curve formula. In compressed key format, the first byte contains a single bit to specify whether the Y coordinate is odd or even, followed by 32 bytes to encode the X coordinate. The proposed bip-taproot followed this convention and used 33 bytes to encode the taproot output key.

This week, John Newbery
[suggested](https://lists.linuxfoundation.org/pipermail/bitcoin-
dev/2019-May/016943.html) that we use some method to avoid placing this byte
in the scriptPubKey. Wuille agreed that this could be useful and will attempt
implementing a variation where the bit will be included as part of the taproot
witness data. This will reduce the cost create a taproot output by one vbyte
(making it the same as P2WSH currently).

 **Aviv from Spacemesh**

 _Spacemesh is a programmable cryptocurrency powered by a novel proof-of-
space-time consensus protocol._

  * After finishing to implement most of the Spacemesh Protocol major flows, we are now focused on testing and benchmarking to verify our network is tuned up to work with many nodes at scale on the cloud using our automation framework. 

  * We are doing tests and benchmarks for gossip, mining, sync and consensus protocols. Another on-going effort is integration of the BLS signature scheme into the platform.

  * On the App front, this week we integrated our Edwards25519 WASM library into the App and worked on the App's desktop notifications feature.

  * For more details check our pulse❣️<https://github.com/spacemeshos/go-spacemesh/pulse>

 **JZ from Decred**

 _Decred  is an autonomous digital currency with a hybrid consensus system. It
is built to be a self-ruling currency where everyone can vote on the rules and
project-level decision making proportionately to their stake._

  * Developer Donald Adu-Poku has [released dcrpool; a stratum Decred PoW mining pool](https://github.com/decred/dcrpool). Considering the importance Proof-of-Work mining has in our Multifactor Consensus system it made sense for us to ensure that there is high quality free and open source mining infrastructure available.

  * Lots of activity over a bunch of other repos as well this week including dcrdata with 14 PRs, 7 for politeiagui, dcrweb with 8, and decrediton receiving 9.

  * One extremely meta Politeia proposal is [wrapping up voting](https://proposals.decred.org/proposals/b9f342a0f917abb7a2ab25d5ed0aca63c06fe6dcc9d09565a9cde3b6fe7e6737) and another which seeks to [incentivize "biz dev" has just been submitted for discussion](https://proposals.decred.org/proposals/cb446a469987d6603d93f442ef0d4e45bacbea47a72b5ce89f9c3cac3868d627). We're overall quite pleased with the quality of the submitted proposals seeking to be funded by the Decred treasury, we are finding however that the stakeholders are tight with the purse strings, which is equally encouraging.

  * If you're in [Berlin on June 5th be sure to drop in on our meetup](https://twitter.com/decredproject/status/1131793706686787584) hosted by BlueYard Capital. [Noah](https://twitter.com/NoahPierau) and I will be attending along with a few other community members, and developer [Jamie Holdstock](https://twitter.com/JamieHoldstock) who will be giving a presentation outlining what it's like to work for a DAE (decentralized autonomous entity) and where the project is headed in the near term.

 **Izaak from Coda**

 _Coda is the first cryptocurrency protocol with a constant-sized blockchain.
Coda compresses the entire blockchain into a tiny snapshot the size of a few
tweets using recursive zk-SNARKs._

  * Corey [integrated libp2p](https://github.com/CodaProtocol/coda/pull/2450) into Coda's networking stack.

  * Nathan [added](https://github.com/CodaProtocol/coda/pull/2445/files) fine-grained, type-level tracking of the amount of validation performed on blocks and proofs from the network, catching a few bugs in the process.

  * Avery built the "send Coda" screen for the desktop wallet. Check out the [screenshots on the PR](https://github.com/CodaProtocol/coda/pull/2489)!

  * Brandon got a [portable Mac build](https://github.com/CodaProtocol/coda/pull/2463) working to make installing the desktop wallet super simple.

  * We've also welcomed three new team members recently. [Carey Janecka](https://www.linkedin.com/in/cjanecka/), Front End Developer, joins from Coinbase. [Claire Kart](https://www.linkedin.com/in/claire-arthurs-kart-6601b67/), Marketing & Community, joins from Ripple. [Pranay Mohan](https://www.linkedin.com/in/pranaymohan/), Developer Relations, joins from Snapchat. 

#### Privacy coins

 **Paige & Zooko from Zcash**

 _Zcash is a  digital currency utilizing zk-SNARKs to enable its privacy-
protecting properties._

  * Last week: v2.0.5-2 released - includes migration tool and counterfeit defense consensus code

  * This week: final review of and decision on draft ZIPs for NU3 consideration

  * Targeting 2.0.6 for Blossom testnet deployment

  * More in the full update: <https://forum.zcashcommunity.com/t/may-24-2019-weekly-update-engineering/33602>

 **Mitchell from Monero**

 _Monero is a open-source, privacy-focused cryptocurrency using the ASIC-
resistant CryptoNote PoW algorithm. It enforces all privacy features at the
protocol level to ensure that all transactions create a single fungible
anonymity pool._

  * New compressed LSAG signatures will offer ~25% reduction in rate of blockchain growth, and around 15-25% speedup in verification times, [first draft here](https://github.com/b-g-goodell/research-lab/tree/master/publications/bulletins/MRL-0012-CLSAG "https://github.com/b-g-goodell/research-lab/tree/master/publications/bulletins/MRL-0012-CLSAG").

  * The Monero Konferenco [schedule is now public](https://monerokon.com/schedule "https://monerokon.com/schedule"). (My "TBD" talk title will be " _Visualizing Monero: a figure is worth a thousand logs_.")

  * Researching several new schemes that may potentially replace our current ring signature scheme - [Spartan](https://eprint.iacr.org/2019/550 "https://eprint.iacr.org/2019/550") and [RingCT3.0](https://eprint.iacr.org/2019/508 "https://eprint.iacr.org/2019/508") and [Lelantus](https://lelantus.io/lelantus.pdf "https://lelantus.io/lelantus.pdf").

  * We now have a client implementation for the Monero wallet and daemon RPC written in Go, [repository here](https://github.com/monero-ecosystem/go-monero-rpc-client "https://github.com/monero-ecosystem/go-monero-rpc-client").

 **Daniel from Grin**

 _Grin is a community-driven implementation of the Mimblewimble protocol that
aims to be privacy preserving, scalable, fair, and minimal._

  * @antiochp proposed Elder channels, a lightning-style layer 2 protocol for Grin. Over the week, we saw not [one](https://gist.github.com/antiochp/dfb1cb0273421584a1fcf2341da9d683), not [two](https://gist.github.com/antiochp/d490280fa0b87e0cd84f961b0911119f), but [three](https://gist.github.com/antiochp/e54fece52dc408d738bf434a14680988) iterations of the mechanism.

  * Merged PRs: [6 in /grin](https://github.com/mimblewimble/grin/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A2019-05-20..2019-05-26+) | [5 in /grin-wallet](https://github.com/mimblewimble/grin-wallet/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A2019-05-20..2019-05-26+) | 5 unique contributors

  * The [last governance meeting](https://github.com/mimblewimble/grin-pm/blob/master/notes/20190521-meeting-governance.md) covered payment to Coinspect for audit, project budget feedback, and wiki access control.

  * @yeastplume [has begun to target improvements for the v2.0.0 hard fork](https://www.grin-forum.org/t/yeastplume-progress-update-thread-mar-19-to-sep-19/4303/25)coming up in a few months.

  * @jaspervdm [open-sourced his multi-party bulletproof builder](https://github.com/vault713/grinswap/blob/master/src/swap/multisig/types.rs#L15) ahead of the full GrinSwap crate.

  * The third brother Peverell, Cadmus, made an appearance recently. Here's a [proposal to optimise (larger) syncs through parallelisation](https://github.com/mimblewimble/grin/issues/2837).

  * Slides from @hashmap's [Mimblewimle introduction (in Russian)](https://hashmap.dev/slides/mw-intro-rus.html) are now online.

  * [Grin Vault](https://play.google.com/store/apps/details?id=com.grinvault.floonet), a grin wallet for Android, was announced and is in open beta (not open sourced yet).

  * New [update of Niffler wallet](https://www.grin-forum.org/t/niffler-an-out-of-the-box-open-sourced-grin-gui-wallet/4760/8).

  * More Grin info [here](https://grinnews.substack.com/).

 **Beni from Beam**

 _Beam is a confidential and scalable cryptocurrency based on Mimblewimble._

  * [Cold Wallet](https://github.com/BeamMW/beam/wiki/Cold-wallet-implementation) Testnet [Release Notes](https://github.com/BeamMW/beam/releases/tag/testnet_cw) | Create and sign transactions [#593](https://github.com/BeamMW/beam/issues/593)

  * Atomic Swap - Important progress (validation for non-negative values, process exceptions, fix secret extracting, confirmation for CLI, changed BTC address version)

  * Laser Beam (Lightning Integration) - Good progress and demo almost ready

  * Cold Wallet restore -  _in progress_

  * Hard Wallet integration [#624](https://github.com/BeamMW/beam/issues/624) -  _in progress_

  *  Desktop Wallet: Login / Restore Screens [#649](https://github.com/BeamMW/beam/issues/649) -  _done_

  *  Desktop Wallet: Add QR code to Address Book [#629](https://github.com/BeamMW/beam/issues/629) -  _in progress_

  *  Desktop Wallet: Multi language UI [#618](https://github.com/BeamMW/beam/issues/618) -  _in progress_

 **Arnaud from AZTEC Protocol**

 _AZTEC Protocol is an efficient zero-knowledge protocol built on top of
Ethereum, making plug-and-play value transmission and asset governance privacy
tools for developers and companies.  _

  * This week we released a first draft of our [trusted setup](https://github.com/AztecProtocol/Setup) code. Notably, we decided to extend it to compute a common reference string which can be used to construct structured reference strings for SONIC zk-SNARKS.

  * We also released a [Loan dApp starter kit](https://github.com/AztecProtocol/loan-dapp-starter-kit) to demonstrate how AZTEC proofs can be combined and assembled, and to demonstrate in-browser proof construction. As part of this starter kit, we also released [scripts](https://github.com/AztecProtocol/aztec-ganache-starter-kit) to make deploying AZTEC to local networks easier.

  * The team was at ETHNewYork last weekend, where we sponsored a prize, [won by the Polymath team](https://twitter.com/PolymathNetwork/status/1130604707523846146) who produced a zero-knowledge payroll dapp.

  * [EIP-1108](https://eips.ethereum.org/EIPS/eip-1108), which would significantly reduce gas costs for AZTEC and other cryptography heavy applications on Ethereum, was accepted (pending a couple of additional benchmarks) to the scheduled Istanbul hardfork.

  * In addition to the two cryptographer roles, we are now hiring for a **Senior Solidity Engineer** and a **Senior Engineer**. You can apply [here](http://email.mg2.substack.com/c/eJwlUEuOwyAMPU3ZNSKQpGHBoq1mrhHxcVumBEfgTJU5_RBF8sKy_fw-zhA8MW96wUJsLZCn4LVQgg8t87rz7diPLJTpkQFmE6KmvAJbVhuDMxQw7fe9kuylwUnVg3RcXQYu7eDAenvpjOx5Lweh2M4xmdUHSA40_ELeMAGL-kW0lJO8nsR3LZOeEBuHe_tH4M5LRkKH8Szr6AdtYUEL3iouRcs7LjvRtM2NX-_jnY-3QbS37ut66vj8FE1ZbSHj3vXfzLI2OVUBdecy-EBzSNQEPJTRtoBO8CkRiCAzOkKpXqcKntcUaJsgGRvB6wNSvUt1kQOrNB5rPklXsfjAxwfz-x-f0nXk), or by emailing [arnaud@aztecprotocol.com](mailto:arnaud@aztecprotocol.com) with the name of the role as the subject.

#### Smart contracting platforms

 **Evan from[Ethereum](https://weekinethereumnews.com/)**

 _Ethereum  is a decentralized platform for applications that aims to resist
fraud, censorship or third-party interference._

  * Lots of phase2 execution work coming out of eth2 meetings in New York.  Vitalik’s [Eth2, phase2, proposal2](https://notes.ethereum.org/w1Pn2iMmSTqCmVUTGV4T5A?viewPhase#) and Will Villanueva and Matt Garnett's [Eth Execution Environment proposal](https://ethresear.ch/t/eth-execution-environment-proposal/5507), as well as [Ewasm Scout](https://ethresear.ch/t/phase-2-execution-prototyping-engine-ewasm-scout/5509), the phase2 execution prototyping engine

  * [Ethereum Foundation Q2 update](https://blog.ethereum.org/2019/05/21/ethereum-foundation-spring-2019-update/) and how it will spend $30m this year

  * [MetaMask user metrics](https://medium.com/metamask/metamask-metrics-fbec0e2ceaa7). 265k MAUs in April.

 **Erik from NEAR**

 _NEAR is a sharded proof-of-stake blockchain._

  * 22 PRs merged or proposed across 4 repos and 5 authors: [nearcore](https://github.com/nearprotocol/nearcore), [nearlib](https://github.com/nearprotocol/nearlib), [near-shell](https://github.com/nearprotocol/near-shell/) and [near-wallet](https://github.com/nearprotocol/near-wallet)

  * Initial support for app-specific keys added to NEAR Wallet

  * Support for ability to send tokens to another account, and view tokens in profile page of Wallet

  * Additional functionality in command line to make method calls to smart contracts

  * Support for setting network ID in near-shell added

  * Stabilizing current nearcore, which is released and running.

  * [Implementation of economics](https://github.com/nearprotocol/nearcore/pull/952): charging storage rent and transaction fees.

  * Continue Nightshade development: [integration tests](https://github.com/nearprotocol/nearcore/pull/928/commits), [chunk production and network](https://github.com/nearprotocol/nearcore/compare/ghost...chunks).

 **AJ from Tezos**

 _Tezos is a self-amending blockchain that features formally verified smart
contracts, on-chain governance, and a proof-of-stake consensus algorithm which
enables all token holders to participate in the network.  _

  * History has been made - [Tezos successfully reaches Quorum of 81.39%](https://tzscan.io/proposals) in its final phase of the first protocol amendment. The new protocol will automatically switch once the voting period over, signifying the first example of a true democratic implementation of a protocol upgrade coordinated by the community. 

  * [Nomadic Labs releases an update for Tezos Node software](https://blog.nomadic-labs.com/). This software update implements ‘Snapshots’ (s[pin up a full tezos nodes in a few minutes](https://medium.com/tezos/https-medium-com-tezos-spinning-up-a-tezos-node-in-under-a-few-minutes-3b3328e173f3)), ‘History Mode’ (dramatically decreases storage usage), and formally verified  Multi Sig smart contracts. Click on the link above to read more about how to update your Tezos Node

  * Tezos Block Explorers: In addition to Tzscan.io, new updates have been released for two block explorers built by Cryptonomics, [Arronax Beta](https://arronax-beta.cryptonomic.tech/#/), and Tezos Southeast Asia, [Tezos.ID](https://tezos.id/)

  * [Chorus Mobility receives support and seed funding from the Tezos Foundation](https://tezos.foundation/news/chorus-mobility-receives-support-and-seed-funding-from-the-tezos-foundation).

  * [Announcing TPlus](https://www.reddit.com/r/tezos/comments/bsadsw/announcement_tplus/), a tool that will make it easier to manage tezos nodes for multiple use cases such as smart contract development, environment testing, and CLI tools. 

**Topper from Quorum Control**

 _Quorum Control makes Tupelo, a permissionless proof of stake DLT platform
purpose-built to model individual objects that enables flexible public or
private data models._

  * Ongoing Optimization of Production Tupelo TestNet

  * Final testing on a major infrastructure improvement to streamline cross-platform development. Defines the core Tupelo types as protocol buffer messages and uses those across all platform-specific development kits.

  * Removed signer produced errors for transactions to prevent attack vector of malicious signers returning fake errors.

  * Read Part 2 of our published posts on NFTs, [“Digital Scarcity (Am I original? Am I the only one?)”](https://www.quorumcontrol.com/blog/2019/5/23/part-2-digital-scarcity-am-i-original-am-i-the-only-one)

 **Michael from Loom**

 _Loom Network is a platform for building highly scalable DPoS sidechains to
Ethereum, with a focus on large-scale games and social apps._

  * [Cryptium Labs](https://twitter.com/CryptiumLabs) goes live as the latest Loom validator

  * Over 202M tokens have been staked on Loom, which amounts to ~26% of circulating supply 

  * [Axie Infinity](https://medium.com/loom-network/https-medium-com-loom-network-announcing-an-alliance-with-axie-infinity-plus-validator-services-5a2adabb64df) will be running a validator, providing in-game rewards to their delegators, and fully migrating to Loom

  * [May Game Release (v0.1.21)](https://www.kickstarter.com/projects/328862817/zombie-battleground-the-new-generation-of-ccg-tcg/posts/2515842) \-- [Relentless](https://loom.games/) rebranding, updated desktop downloads, and tons of bug fixes

 **Myles from EOS**

 _EOS is a new blockchain architecture designed to enable vertical and
horizontal scaling of decentralized applications._

  * [Block.one](http://block.one/) just [purchased](https://bloks.io/transaction/b904bc59c5e4b734cb49f4cee61257e406f2ea66ed4c31cd5d4cf7858c6f7e8e) 32 GB worth of RAM on the EOS mainnet (likely related to their upcoming June 1st announcement) 

  * EOSIO Labs [releases](https://medium.com/eosio/eosio-software-release-native-sdks-for-swift-and-java-e6086ddd37b8) native SDKs for Swift and Java 

  * Greymass released [the beta version](https://blog.greymass.com/eos/@greymass/the-future-of-the-greymass-wallet-beta-version-available-now) of its new desktop wallet — Anchor (previous called eos-voter)

  * [Decentium](https://decentium.org/x/decentiumcrw/introducing-d), a Medium alternative built on top of EOS, launched. 

 **Zaki from Cosmos**

 _The  Cosmos Network is a decentralized network of independent, scalable, and
interoperable blockchains._

  * We released a a bug fix and ergonomics release of [Gaia](https://github.com/cosmos/cosmos-sdk/releases/tag/v0.34.5). This adds support for the Ledger Nano X.

  * Cosmosstation released a [javascript library](https://github.com/cosmostation/cosmosjs) for generating and signing transactions on the cosmos hub.

  * We have upcoming hackathons in [Berlin](https://hackatom-berlin.cosmos.network/) and [Seoul](https://blog.cosmos.network/cosmos-hackatom-is-coming-to-seoul-f2cb83172307). 

  * [ICS 4](https://github.com/cosmos/ics/pull/34/files):  IBC Channels and Packets is in final review

 **Kate and Dean from Agoric**

 _Founded by pioneers in secure development and distributed systems, Agoric
uses a secure subset of JavaScript to enable object capabilities and smart
contracts._

  * This week Mark successfully implemented a particular example of higher order contracts. “Higher order” contracts allow you to effectively tokenize _positions_ in contracts. In this particular scenario, Bob writes a covered call giving Alice the option to buy Bob’s stock shares. Alice makes a new escrow agent that allows her to trade this seat at the table to Fred, and Fred is able to verify that these are the rights he is interested in. The escrow agent code is able to treat the “seat at the table” as if it were a straightforward token, allowing us to use these “higher order” tokens in any smart contract component that accepts tokens.

#### Financial Infrastructure

 **Antonio from dYdX**

 _dYdX is a decentralized exchange for margin trading, borrowing, lending, and
eventually derivatives. dYdX allows traders to trustlessly short and get
leverage on crypto assets._

  * Everett Hu joined the team as a frontend engineer, welcome Everett!

  * Antonio wrote an [overview of decentralized lending protocols](https://medium.com/dydxderivatives/decentralized-lending-an-overview-1e00fdc2d3ee)

  * Shipped transaction history. Can now view a history of all trades, deposits, and withdrawals directly in the app

  * Working on adding a DAI-USDC market powered by 0x

  * Finishing up a design sprint focusing on a new borrow flow and an improved cross trading experience

  * Building price oracles for new assets, so we can add them to dYdX

  * [Hiring](https://dydx.exchange/careers/) product designers & engineers full-time in SF!

 **Brendan from Dharma**

 _Dharma is the easiest place to borrow and lend cryptocurrencies. It enables
non-custodial peer-to-peer lending through smart contracts on Ethereum._

  * Launched USDC! Users can now borrow and lend USDC at 8% APR from anywhere in the world, instantly. If you're interested in borrowing or lending USDC in high volumes, please reach out [max@dharma.io](mailto:max@dharma.io)

  * Began testing our new '[Instant Matching](https://blog.dharma.io/introducing-instant-matching-9c54ca0d2a66)' feature with early user cohort

  * Implemented automatic 8% discount for loan liquidators

  * Our very own Brendan Forster gave an [inspiring talk](https://www.youtube.com/watch?time_continue=8995&v=ZhpIeQJNbZw) about #DeFi at Fluidity!

  * We're [hiring](https://boards.greenhouse.io/dharma) a General Counsel and Full Stack Engineers in SF!

 **Coulter from MakerDAO**

 _Maker is comprised of a decentralized stablecoin, collateral loans, and
community governance._

  * Dai has been added to [Coinbase](https://blog.coinbase.com/dai-dai-is-now-available-on-coinbase-b95da99ef6ce)! 

  * Maker is helpful fuel the DeFi movement. Read [more](https://blog.makerdao.com/defi-ing-tradition-how-makerdao-helps-cultivate-the-defi-ecosystem/).

  * We're sharing the details of the [most recent update](https://blog.makerdao.com/update-the-road-to-multi-collateral-dai-kovan-release-v0-2-6/) (MCD v0.2.6) on Kovan testnet as we track toward Multi-Collateral [#Dai](https://twitter.com/hashtag/Dai?src=hashtag_click). This update covers the CDP Portal, Governance Dashboard, Testchain DSS deployment scripts and new developer guides.

  * We've partnered with Experimental to have Dai [integrated into their game](https://blog.e11.io/experimental-partners-with-makerdao-80670f59a60f), CryptoWars. 

**Lazar from MARKET Protocol**

 _MARKET Protocol is a framework for creating tokens that track prices of
traditional or digital assets._

  * We reached a big milestone this week, our platform is feature complete for launch!

  * Deployed updated platform to staging environment on Kovan, mainnet to follow

  * Still finalizing our solidity refactor based on recommendations from our security audit

  * Drafted an update to our website to support MPX and minting platform launch

 **Robert from Compound**

 _Compound is a money market protocol on the Ethereum blockchain — allowing
individuals, institutions, and applications to frictionlessly earn interest on
or borrow cryptographic assets without having to negotiate with a counterparty
or peer._

  * Launched [Compound v2](https://medium.com/compound-finance/compound-v2-is-live-157db0b7cfc8), and began migrating users 

  * Released mainnet contract addresses & [documentation](https://compound.finance/developers) for developers to build applications on top of Compound

#### Layer two and interoperability

 **Rahul from 0x**

 _0x_  is an open protocol that enables the peer-to-peer exchange of assets on
the Ethereum blockchain.

  * Check out our [educational videos](https://www.youtube.com/playlist?list=PLN51Tjs40v5PIm4avEo1m2Uz08qj0YWPa%27) around the 0x smart contracts

  * Awarded [Mine Auction](https://twitter.com/0xProject/status/1131701759334686720) the 0x price at ETH NY, a marketplace for trading staking contracts

  * New [Relayer Report](https://blog.0xproject.com/relayer-report-21-augur-sees-the-lite-b6315df9fa66), digging into the AugurLite fork, 0x at ETH New York, and ENS support on Emoon

 **Tony from Liquidity.Network**

 _Liquidity Network is a transfer and swap platform for any token_

  * Liquidity Network has the honor of being a platinum sponsor for the [Crypto Valley Conference 2019](http://www.cryptovalleyconference.com/) from 24th - 26th June 2019 at Zug, Switzerland

  * Liquidity Network is running a survey to collect users' opinions about current exchange ecosystem. Please participate [here](https://docs.google.com/forms/d/e/1FAIpQLSfPA7QTkdFBSDvh26eXZas-maPZ1rsV9Eb1HAP0mIH0DLmdHw/viewform). 

 **Dong Mo from Celer**

 _Celer Network is a layer-2 scaling platform that enables fast, easy and
secure off-chain transactions for not only payment transactions, but also
generalized off-chain smart contracts._

  * We refactored game platform architecture, to clearly distinguish different game modes. 

  * We've finished on-chain dispute process on iOS and fixed issues and improved app based on ETHNewYork feedback. 

  * We are in the process of developing new wallet UI. 

  * We implemented design reviews and started implementing features for end-of-June milestone. 

  * Fast-track cold bootstrap for new users and upgradable cChannel on-chain contracts. 

  * System stress testing and identified improvements on our backend system.

 **Alexandra from Parity Technologies**

 _Parity  Technologies builds core blockchain infrastructure, from Parity
Ethereum, an Ethereum client, to Polkadot, an interoperable blockchain
network._

  * [Polkadot PoC 4 is here!](https://twitter.com/polkadotnetwork/status/1130431664478478336)

  * [PolkaDAO is live!](https://medium.com/polkadot-network/polkadao-is-live-e61c39d0b259)

  * New [Japanese Substrate Telegram channel](https://twitter.com/WatanabeSota/status/1131521111680643072).

  * A contributor, Sota Watanabe, created a [Plasma Substrate Runtime Module Library](https://medium.com/staked-technologies/plasm-plasma-on-substrate-16f017fc41e).

  * Thibaut Sardan presented [Fether](https://twitter.com/ParityTech/status/1131603414515900416), a light client wallet.

  * Inspired by MolochDAO, Amar Singh created [SunshineDAO](https://twitter.com/ParityTech/status/1131561956224249856).

  * There's still some Early Adopter tickets left for [Web3 Summit](https://www.web3summit.com/tickets/) during Berlin Blockchain Week.

  * Web3 Foundation is [providing grants to build the Web3 ecosystem](https://github.com/w3f/Web3-collaboration/blob/master/grants/grants.md).

  * We added new jobs, including [Business Development Manager](https://www.parity.io/jobs/#berlin-business-development-manager).

#### Application infrastructure

 **Wes from Theta**

 _Theta is an end-to-end infrastructure for decentralized video streaming._

  * Added Ledger/Trezor support for Theta mainnet to the Theta web wallet

  * Added support for automatic tokens splits between video relayers and streamers/content creators

  * CTO Jieyi Long presented his paper “[Scalable BFT Consensus Mechanism Through Aggregated Signature Gossip](https://github.com/thetatoken/theta-protocol-ledger/blob/master/docs/multi-level-bft-tech-report.pdf)” at IEEE crypto conference in Seoul

  * Theta Fuel (TFUEL) listed on Binance

 **Doug from Livepeer**

 _Livepeer is a decentralized video infrastructure network, dramatically
reducing prices for developers and businesses building video streaming
applications at scale.  _

  * The Livepeer node now supports builds for its upcoming release in Linux, Windows, and OS X.

  * Participation rate in the protocol has surpassed 40% of all LPT staked - on the path to the 50% target before inflation rate begins reducing itself.

 **David from Sia**

 _Sia is a decentralized cloud storage platform leveraging blockchain
technology to create a data storage marketplace that is more robust and more
affordable than traditional cloud storage providers._

  * Luke worked on the seed-based file recovery feature: asynchronous upload of metadata snapshots and synchronization of these snapshots across the hosts have been added

  * Chris added the ability to cancel ongoing downloads and uploads to Sia

  * Matt worked on multiple MRs oriented to improve the file repair process

  * Internal tests by Nebulous are revealing a great improvement in scalability: in the next version, 15+ TB will be able to be uploaded per renter node

  * Luke updated his `us` library to allow FUSE capabilities (<https://www.reddit.com/r/siacoin/comments/bryifi/writeable_fuse_demo/>). Thanks to this, a local directory connected to Sia can be mounted on the system, enabling operations like uploading data to internet directly from Sia hosts. It also better handles small files and document edits, by bundling them before sending them to Sia.

  * Community member @tbenz9 published a proof-of-concept script for storing automatically on Sia security camera footage (an ideal use case of Sia): <https://www.reddit.com/r/siacoin/comments/brr0xs/a_rudimentary_guide_how_to_automatically_store/>

  * Stay up to date with all the latest in our Discord server - <https://discord.gg/sia>

#### Other

 **Ari from Decentraland**

 _Decentraland is a virtual world where you can build and explore 3D
creations, play games and socialize._

  * Last week, we released an update to the Builder allowing users to export their scenes for use with the SDK.

  * Currently testing Picture Frame support for additional third-party NFTs.

  * Testing and optimizing the performance of loading scenes in the Unity-based Decentraland Client.

  * Released various minor bug fixes to improve click actions and animations in the SDK.

 **Sam from OpenBazaar**

 _OpenBazaar is an open source project developing a protocol for e-commerce
transactions in a fully decentralized marketplace._

  * Corey [integrated libp2p](https://github.com/CodaProtocol/coda/pull/2450) into Coda's networking stack.

  * Nathan [added](https://github.com/CodaProtocol/coda/pull/2445/files) fine-grained, type-level tracking of the amount of validation performed on blocks and proofs from the network, catching a few bugs in the process.

  * Avery built the "send Coda" screen for the desktop wallet. Check out the [screenshots on the PR](https://github.com/CodaProtocol/coda/pull/2489)!

  * Brandon got a [portable Mac build](https://github.com/CodaProtocol/coda/pull/2463) working to make installing the desktop wallet super simple.

  * We've also welcomed three new team members recently. [Carey Janecka](https://www.linkedin.com/in/cjanecka/), Front End Developer, joins from Coinbase. [Claire Kart](https://www.linkedin.com/in/claire-arthurs-kart-6601b67/), Marketing & Community, joins from Ripple. [Pranay Mohan](https://www.linkedin.com/in/pranaymohan/), Developer Relations, joins from Snapchat. 

[ShareShare](javascript:void\(0\))

TopNew[](javascript:void\(0\))

No posts

# Ready for more?

 **Subscribe**

© 2022 Eric Meltzer

[Privacy](https://proofofwork.news/privacy) ∙ [Terms](/tos) ∙ [Collection
notice](https://substack.com/ccpa#personal-data-collected)

[ Publish on
Substack](https://substack.com/signup?utm_source=substack&utm_medium=web&utm_content=footer)[
Get the app](https://substack.com/app/app-store-redirect?utm_campaign=app-
marketing&utm_content=web-footer-button)

[Substack](https://substack.com) is the home for great writing

This site requires JavaScript to run correctly. Please [turn on
JavaScript](https://enable-javascript.com/) or unblock scripts

