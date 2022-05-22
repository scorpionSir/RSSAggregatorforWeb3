[![](https://substackcdn.com/image/fetch/w_96,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F37b09348-f4f1-47a2-b9e0-a2007299e6e4_256x256)](https://proofofwork.news)

# [Proof of Work](https://proofofwork.news)

SubscribeSign in

Share this post

Proof of Work #72

proofofwork.news

Copy link

Twitter

Facebook

Email

# Proof of Work #72

[Eric Meltzer](https://substack.com/profile/138320-eric-meltzer)

Jun 27, 2019

[Share](javascript:void\(0\))

A few housekeeping notes; We’re now running updates from Keep & Solana, two
interesting new projects. As I’ve noted before, we run updates from a variety
of projects with the only criteria being that they are doing something
interesting technologically or socially in the space—I’m not an investor in
either Keep or Solana, but am personally interested in reading their updates
and seeing how they progress.

A neat thing [someone](https://twitter.com/lay2000lbs) built recently:
[PoolTogether](https://www.pooltogether.us/), a lottery based on the prize-
linked savings account mechanic, where each user locks up some money, and then
one user is awarded all of the interest accrued on everyone else’s deposits
(which are lent out on PoW’s own [compound.finance](http://compound.finance),
but the principal is returned to each depositor. Interested to see if anyone
forks this to a rake-free version (PoolTogether takes 10%), since doing so
would be trivial. In the case where PoolTogether spent all of their 10% rake
doing marketing, I’d expect that to outcompete a totally rake-free version
that no one would have any incentive to market.

Especially interesting updates from Sia, Grin, and the Plasma group this week.
More next week!

#### Bitcoin & Friends

 **Aviv from Spacemesh**

 _Spacemesh is a programmable cryptocurrency powered by a novel proof-of-
space-time consensus protocol._

  * Full node: Added ed21599 signatures to transactions and made the p2p address-book persistent to store, and configurable from store. we've added numerous improvements to our automations tests and to the framework itself, as a preparation for more rigorous tests.

  * App: focus is on node integration for getting transactions and statuses and on error handling across the app.

  * Community: Made available [Wasm 2019 Berlin Workshop videos](https://www.youtube.com/playlist?list=PL5BszCNLCnMOt7wCU9CmTaaFPP3-cIKmR).

 **JZ from Decred**

 _Decred  is an autonomous digital currency with a hybrid consensus system. It
is built to be a self-ruling currency where everyone can vote on the rules and
project-level decision making proportionately to their stake._

  * The [Decred Bug Bounty renewal proposal](https://proposals.decred.org/proposals/073694ed82d34b2bfff51e35220e8052ad4060899b23bc25791a9383375cae70) is live for voting on Politeia. It's receiving strong support as the consensus seems to be that the program was run exceedingly well over the last six months. We haven't met quorum yet (20%) so everyone is encouraged to vote.

  * Decred project lead Jake Yocom-Piatt had a piece published on Coindesk entitled ["Staking Isn’t Just a Way to Earn Crypto Money – And It Shouldn’t Be"](https://www.coindesk.com/staking-isnt-just-a-way-to-earn-crypto-money-and-it-shouldnt-be) examining the important role that PoS can play in crypto governance.

  * Episode 2 of our new podcast series ["Decred in Depth" is out featuring developer Luke Powell](https://www.youtube.com/watch?v=W6yUVq97cd8) covering topics such as Politeia, dcrtime, and the Decred contractor model

  * The SF Decred Devs team is holding a [happy hour at Coinbase Custody on June 26th](https://www.meetup.com/San-Francisco-Decred-Meetup/events/262420787/). As always, everyone is welcome to drop by for food, drinks, and enthralling conversation.

 **Johnny from Stellar**

 _Stellar is an open network for sending and exchanging value of any kind. Its
global network enables digitization of assets - from carbon credits to
currencies - and enables movement around the internet with ease._

  * We're aiming to ship Stellar Core 11.2.0 this week — [the third release candidate is out here](https://github.com/stellar/stellar-core/releases/tag/v11.2.0rc3). It includes several features for admins, including automatic quorum set generation and quorum monitoring.

  * [SEP-0020](https://github.com/stellar/stellar-protocol/blob/master/ecosystem/sep-0020.md) (Validator Self Verification) and [CAP-0015](https://github.com/stellar/stellar-protocol/blob/master/core/cap-0015.md) (Fee Bump Transactions) have had several updates to them, and are moving to fully accepted proposals.

  * [Satoshipay recently did a video with us](https://www.youtube.com/watch?v=aaCc0s1bWAs&feature=youtu.be) explaining their business focused on micro-transactions, and the value Stellar brings them.

  * We've built new documentation for creating assets on Stellar, in particular around stablecoins. See our [new doc](https://www.stellar.org/developers/guides/walkthroughs/connect-to-wallets.html) and our [new diagram](http://diagrams.stellar.org/cross-border-payments/) explaining this.

  * Wirex [added a short video on Stellar Federation](https://www.youtube.com/watch?v=-QZjmRUofEw) in their platform, showing its utility within the ecosystem.

 **Izaak from Coda**

 _Coda is the first cryptocurrency protocol with a constant-sized blockchain.
Coda compresses the entire blockchain into a tiny snapshot the size of a few
tweets using recursive zk-SNARKs._

  * Avery [hooked up wallet GUI](https://github.com/CodaProtocol/coda/pull/2669) to interact with working daemon.

  * We sent out the first edition of our [’Succinct’ newsletter](https://docs.google.com/forms/d/e/1FAIpQLSdChigoRhyZqg1RbaA6ODiqJ4q42cPpNbSH-koxXHjLwDeqDw/viewform), which was a team effort but special thanks to Claire and Carey.

  * Our most recent testnet ran for 2250 blocks with proof of stake! It crashed due to some bad infrastructure code.

  * Paul added [GraphQL](https://github.com/CodaProtocol/coda/pull/2691) apis for querying the trustworthiness of peers.

  * Conner re-added [MacOS builds](https://github.com/CodaProtocol/coda/pull/2697) to our CI.

#### Privacy coins

 **Mitchell from Monero**

 _Monero is a open-source, privacy-focused cryptocurrency using the ASIC-
resistant CryptoNote PoW algorithm. It enforces all privacy features at the
protocol level to ensure that all transactions create a single fungible
anonymity pool._

  * Monero Konferenco was a huge success! All of the presentations are publicly available: [schedule](https://monerokon.com/schedule "https://monerokon.com/schedule"), [Saturday talks](https://www.youtube.com/watch?v=0vGFd8wfm8M "https://www.youtube.com/watch?v=0vGFd8wfm8M"), [Sunday talks](https://www.youtube.com/watch?v=AsJaMw-3gGE "https://www.youtube.com/watch?v=AsJaMw-3gGE").

 **Daniel from Grin**

 _Grin is a community-driven implementation of the Mimblewimble protocol that
aims to be privacy preserving, scalable, fair, and minimal._

  * Merged PRs: [1 in /grin](https://github.com/mimblewimble/grin/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A2019-06-17..2019-06-23+) | [2 in /grin-wallet](https://github.com/mimblewimble/grin-wallet/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A2019-06-17..2019-06-23+) | 3 unique contributors

  * @yeastplume [submitted the final wallet pr](https://www.grin-forum.org/t/yeastplume-progress-update-thread-mar-19-to-sep-19/4303/28) ahead of the hard fork.

  * v2.0.0 beta binaries were released for [node](https://github.com/mimblewimble/grin/releases/tag/v2.0.0-beta.1) and [wallet](https://github.com/mimblewimble/grin-wallet/releases/tag/v2.0.0-beta.1).

  * A [hard fork practice round](https://www.grin-forum.org/t/join-us-to-test-grin-hard-fork/5281) was conducted successfully on a private testnet.

  * Igno has [taken some leave](https://www.grin-forum.org/t/on-ignos-absence/5301) for an indefinite period.

  * In the [last governance meeting](https://github.com/mimblewimble/grin-pm/blob/master/notes/20190618-meeting-governance.md), we covered bug bounties, @hashmap was added as contact person in our security vulnerability disclosure process, and discussed the new governance process proposal.

  * On the back of that, we begun [iterating on an RFC process](https://github.com/mimblewimble/grin-rfcs), improvements welcomed as PRs directly to the repo.

  * More Grin info [here](https://grinnews.substack.com/).

 **Beni from Beam**

 _Beam is a confidential and scalable cryptocurrency based on Mimblewimble._

  * We are happy to announce the 2019 Qtum & Beam Privacy Hackathon that will challenge participants to leverage the Qtum and Beam platforms in order to develop anonymous assets and blockchain privacy solutions \- June 19th - August 18th, 2019 - Learn more [here](https://hackathon.qtum.org/) and register [here](https://hackathon.qtum.org/signup)

  * [SWAP] List of cases when we need to notify second side about failures (will be supplemented) [#702](https://github.com/BeamMW/beam/issues/702)

  * [SWAP] Display "Swap conditions match" first before claiming "Swap Accepted." [#666](https://github.com/BeamMW/beam/issues/666)

  * [SWAP+CLI] - Move the all related SWAP command to separate group in help [#731](https://github.com/BeamMW/beam/issues/731)

  * There are [163 open issues](http://email.mg1.substack.com/c/eJwlULmOhDAM_RrSLUoCBChSzF7d1luiHAaiJQElzoz4-w0zkiU_X89-Ngph2eMpERKSnCBOzkpiJe256TVxaZojgFduk-TIenNGodvD1cVbQckqVS9gFGIEIwY2dzPvB86NHYBS1ozzSI494aSydRAMSLhDPPcAZJMr4pGq5lbx72KLwzXr2uy-BO-g_M9vAbqA4lxKGRJxklM20pZzJgpqalZ_te1HP9Kh-xS0bWhXtdQvrE5ZJ1Tm7-IjUWoIrlQutjf_eCafZ-F5gAzwSBsgQiT4ekRROpUen4PDc4Kg9AZWYszwGivqOyYoJWWN3ct3gryoj-juypz_4txydA) in /beam

  * Excluding merges, [10 authors have pushed 51 commits](https://github.com/BeamMW/beam/pulse) to master and 57 commits to all branches. On master, 90 files have changed and there have been [10071 additions](https://github.com/BeamMW/beam/compare/master@%7B1555936846%7D...master)

#### Smart contracting platforms

 **Evan from[Ethereum](https://weekinethereumnews.com/)**

 _Ethereum  is a decentralized platform for applications that aims to resist
fraud, censorship or third-party interference._

  * [What’s New in Eth2](https://notes.ethereum.org/c/Sk8Zs--CQ/https%3A%2F%2Fbenjaminion.xyz%2Fnewineth2%2F20190621.html). Since it is the first issue in awhile, it’s a good summary of the different phases of Eth2 

  * Argent unveils [Hopper](https://medium.com/argenthq/introducing-hopper-mobile-web-friendly-privacy-for-ethereum-d02a8c400dad), “a zero-knowledge-based trustless mixer” to deposit 1 eth and withdraw to different address

  * [EF-supported teams: development update](https://blog.ethereum.org/2019/06/21/ef-supported-teams-development-report-2019-pt-1/). Extensive updates from each EF team.

 **Jing from Plasma**

 _Plasma Group is building "Generalized Plasma", a layer 2 scaling
infrastructure for Ethereum that allows for general state transitions on layer
2._

  * [Implemented state manager](https://github.com/plasma-group/pigi/pull/276)

  * [Completed ownership predicate contract](https://github.com/plasma-group/pigi/pull/290)

  * Plasma implementers call this Wednesday (June 26th) at 7am PST

    * Add questions and topics to the agenda thread [here](https://plasma.build/t/request-for-topics-plasma-implementers-call-22/104)

    * Or check out the recording & notes for the last call [here](https://plasma.build/t/retrospective-plasma-implementers-call-21/89/5)

    * The Zoom link is (and will continue to be) [here](https://zoom.us/j/798238576)

 **Peter from NEAR**

 _NEAR is a sharded proof-of-stake blockchain._

  * 21 PRs across [10 repos](https://github.com/nearprotocol) and 10 authors. Featured repos: [nearcore](https://github.com/nearprotocol/nearcore), [nearlib](https://github.com/nearprotocol/nearlib), [near-shell](https://github.com/nearprotocol/near-shell/), and [near-wallet](https://github.com/nearprotocol/near-wallet)

  * Streamlined our release process

  * First version of staking is complete and currently being tested

  * Deployed test version Nightshade, our new model consensus

  * Updates across all libraries for Nightshade merge

  * Bug fixes and UI improvements in wallet

  * Updated syntax in near-shell

  * Added advanced access keys in core

  * Chunks for sharding are underway in a[ ~1800 line PR](https://github.com/nearprotocol/nearcore/pull/1013)

 **AJ from Tezos**

 _Tezos is a self-amending blockchain that features formally verified smart
contracts, on-chain governance, and a proof-of-stake consensus algorithm which
enables all token holders to participate in the network.  _

  * [Tezos Foundation will give away to Ledger Nano S](https://tezos.foundation/news/tezos-foundation-to-give-away-ledger-nano-s-hardware-wallets-to-celebrate-one-year-since-betanet-launch) to all fundraiser contributors as a celebration for it’s 1 year launch of Mainnet. 

  * Serokell publishes [parsing Typed eDSL](https://serokell.io/blog/parsing-typed-edsl). 

  * [Reading list for the upcoming Tezos proposal](https://www.reddit.com/r/tezos/comments/c3n49r/reading_list_prepare_for_the_upcoming_proposal/) that will be injected by Cryptium Labs and Nomadic Labs. 

  * [Tezos Foundation issues a grant for smart contract language, LIGO](https://tezos.foundation/news/tezos-foundation-issues-grant-to-support-ligo), that enables developers to write smart contracts with languages like Python. Another smart contract language, SmartPy.io will be launching soon for Tezos

  * [Introducing a new standard interface for creating and managing fungible assets use smart Contracts on Tezos.](https://medium.com/tocqueville-group/assets-on-tezos-3c103e03abc9) This project is being built in coordination with TQ, Nomadic Labs, and Serokell. 

 **Topper from Quorum Control**

 _Quorum Control makes Tupelo, a permissionless proof of stake DLT platform
purpose-built to model individual objects that enables flexible public or
private data models._

  * Opened the 0.4.0 TestNet to the public!  It is now [fully available for anyone’s use](https://docs.quorumcontrol.com/tutorials/rpc_server.html). 

  * Held an event in conjunction with [BerChain](https://berchain.com/) to demo the Tupelo platform for the Berlin development community.

  * QC team is fresh off a full team offsite where we finalized the Q3 roadmap focusing on ease-of-use and adoption for application developers.

  * Check out the [PGC talk by QCs CMO Stephanie Mello](https://www.youtube.com/watch?v=eKT5nookYdI) as she lays out strategies for bringing blockchain and community to gaming for developers. 

**Andrew from Solana**

 _Solana is a scalable blockchain that utilizes proof of history to verify the
ordering and passage of time between events._ _It consists of a network of 200
physically distinct nodes which support a sustained throughput of more than
50,000 TPS.  _

  * We are preparing for Mainnet in Q3/Q4.

  * We just [published a piece explaining Proof of History](https://medium.com/solana-labs/proof-of-history-a-clock-for-blockchain-cf47a61a9274) and why that leads to super quick blockchains. 

  * We are about to announce Turbine - Solana's Block Propagation Protocol.

  * We are working on the Tour del SOL, or Solana’s validation-client competition.

  * We have added 4 team members in the [past 60 days and are hiring](https://solana.com/careers/index.php).

 **Michael from Loom**

 _Loom Network is a platform for building highly scalable DPoS sidechains to
Ethereum, with a focus on large-scale games and social apps._

  * Loom hits ATH of [99K transactions in single day](https://twitter.com/StakeWithUs/status/1140842415865004032)

  * Loom is now live on DappRadar: <https://dappradar.com/rankings/protocol/loom>​

  * Rolled out support for [Universal Transaction Signing with Portis wallet](https://twitter.com/loomnetwork/status/1142073446098178048/photo/1)

  * [Released developer guide](https://loomx.io/developers/en/deposit-and-withdraw-trx.html) on how to integrate TRON dapps with Loom and let users deposit/withdraw TRX

  * [Infinity Stones ](https://twitter.com/infstones)goes live as the latest Loom validator  

  * [​](https://loomx.io/developers/en/deposit-and-withdraw-trx.html)Over 214M tokens have been staked on Loom, which amounts to ~27% of circulating supply

 **Myles from EOS**

 _EOS is a new blockchain architecture designed to enable vertical and
horizontal scaling of decentralized applications._

  * [Block.one](http://block.one/) published details on [EOSVM](https://eos.io/news/eos-virtual-machine-a-high-performance-blockchain-webassembly-interpreter/), a new WASM-based VM that will be introduced in EOSIO 2.0

  * NEWDEX has [developed](https://medium.com/@marketing_27690/the-smart-contract-on-the-newdex-is-coming-lets-look-forward-to-it-1621ee584481) smart contracts for fully on-chain matching and settlement of exchange orders. They are now in the process of having the contracts audited by security firms. 

  * Korean exchange Bithumb [announced](https://medium.com/eos-nodeone/bithumb-announces-start-of-eos-blockchain-voting-4231d734a45b) its plans to start participating in EOS voting

  * Everipedia [launched](https://medium.com/@Everipedia/unveiling-everipedia-2-0-public-beta-and-updated-roadmap-f64711de2cb1https://medium.com/@Everipedia/unveiling-everipedia-2-0-public-beta-and-updated-roadmap-f64711de2cb1) Everipedia 2.0

 **Kate and Dean from Agoric**

 _Founded by pioneers in secure development and distributed systems, Agoric
uses a secure subset of JavaScript to enable object capabilities and smart
contracts._

  * We are excited to announce Agoric’s partnership with Cosmos and Cosmos’ Interchain Foundation. Agoric and Cosmos are jointly creating the IBC (Inter­Blockchain Communication) protocol. IBC will provide true interoperability across multiple blockchains, and expand the market available to millions of current and future smart contracts developers worldwide.

  * Dean [spoke at Zcon1](https://youtu.be/EAGaYg3hq88) (video [here](https://youtu.be/EAGaYg3hq88)) with an update on what we’ve accomplished since last year’s Zcon0, including the creation of a secure runtime for JavaScript (SES), a running end-to-end Cosmos-based testnet, the Cosmos IBC collaboration, and further work on our smart contract framework and components. 

#### Financial Infrastructure

 **Antonio from dYdX**

 _dYdX is a decentralized exchange for margin trading, borrowing, lending, and
eventually derivatives. dYdX allows traders to trustlessly short and get
leverage on crypto assets._

  * Launched [direct borrow flow](https://twitter.com/dydxprotocol/status/1143234881150836737)! Use dYdX to borrow crypto directly to your wallet

  * Launched the [ETH-USDC market](https://twitter.com/dydxprotocol/status/1139225179609919490) through 0x

  * Launched [improved cross trading flow](https://twitter.com/dydxprotocol/status/1138567000718843905)

  * Enabled unlimited duration borrows on dYdX. Borrow any asset for as long as you want!

  * Working on adding limit orders

  * [Hiring](https://dydx.exchange/careers/) product designers & engineers full-time in SF!

 **Brendan from Dharma**

 _Dharma is the easiest place to borrow and lend cryptocurrencies. It enables
non-custodial peer-to-peer lending through smart contracts on Ethereum._

  * Launched upgraded [borrow experience](https://blog.dharma.io/upgrading-our-borrow-experience-50693d23229c)! borrowers can now submit orders with custom principal amounts, interest rates, and collateral requirements. We'll go out and find the lender.

  * Rolled out new community updates to Dharma telegram group and various high value accounts

  * Began working on an affiliate program

  * We're hiring [full stack engineers in SF](https://careers.dharma.io/)!

 **Coulter from MakerDAO**

 **Lazar from MARKET Protocol**

 _MARKET Protocol is a framework for creating tokens that track prices of
traditional or digital assets._

  * We officially launched [MPX and Position Tokens](https://medium.com/market-protocol/mpexplained-trading-position-tokens-95e120c71b77), introducing our first token – leveraged BTC/DAI! Traders can start trading on [MPX](https://mpexchange.io/) (ex. US for now)

  * We published Part 2 of our MPExplained educational series: [Trading Position Tokens](https://medium.com/market-protocol/mpx-and-position-tokens-are-live-6dfd432df9aa). Check it out to learn more about trading BTC/DAI tokens

 **Robert from Compound**

 _Compound is a money market protocol on the Ethereum blockchain — allowing
individuals, institutions, and applications to frictionlessly earn interest on
or borrow cryptographic assets without having to negotiate with a counterparty
or peer._

  * Helped launch [PoolTogether](https://www.pooltogether.us/), a no-loss lottery built on Maker's DAI and Compound v2

#### Layer two and interoperability

 **Zaki from Cosmos**

 _The  Cosmos Network is a decentralized network of independent, scalable, and
interoperable blockchains._

  * Chorus One wrote up their Delegation Voucher's [implementation](https://medium.com/chorus-one/delegation-vouchers-cfb511a29aac) of tokenized staking rewards.

  * Kava Labs announced their architecture for [multicollateral DeFi](https://medium.com/kava-labs/defi-coming-to-cosmos-808034b733be?postPublishedType=repub) on Cosmos. 

  * [A comparison of Tendermint, HotStuff, and SBFT](https://ittaiab.github.io/2019-06-23-what-is-the-difference-between/)

  * [A proposal to implement constrained subkeys is working it's way through governance.](https://forum.cosmos.network/t/proposal-adding-subkey-feature-to-cosmos-sdk-and-apply-it-to-the-hub/2358)

 **Alexandra from Polkadot**

 _[Polkadot](https://polkadot.network/) empowers blockchain networks to work
together under the protection of shared security._

  * [Polkadot.network](https://polkadot.network/) is now available in Japanese, Korean, Chinese (Mandarin), and Russian

  * Foundations laid for a [Polkadot x Zcash bridge](https://twitter.com/polkadotnetwork/status/1140666986420154368)

  * Web3 Foundation is[ providing grants to build the Web3 ecosystem](https://github.com/w3f/Web3-collaboration/blob/master/grants/grants.md). 

  * Lots of [openings to build Polkadot](http://web3.bamboohr.com/jobs/)

  * New submissions for [PolkaDAO](https://www.reddit.com/r/dot/comments/c2xfnk/polkadao_update/)

  * [Last call for speaker and workshop submissions at Web3 Summit](https://twitter.com/web3summit/status/1142084776997900289)

 **Paul from Veil**

 **Matt from 0x**

 _0x_  is an open protocol that enables the peer-to-peer exchange of assets on
the Ethereum blockchain.

  * Hosted an internal hackathon earlier this month. Check out the projects [here](https://blog.0xproject.com/the-inaugural-0x-team-hackathon-8359b68b98e7)

  * 0x relayer Bamboo Relay has [implemented a Coordinator model](https://medium.com/bamboo-relay/0x-coordinator-model-eap-acceptance-bc37b5e58256) to allow for unlimited soft cancels

 **Tony from Liquidity.Network**

 _Liquidity Network is a transfer and swap platform for any token_

  * Liquidity Network's COO Guillaume Felley will present NOCUST at the Ethereum Technology & Application Convention at Beijing on 29-30 June 2019. Let's join him there! Full event details [here](https://bss.csdn.net/m/topic/ethereum2019/index_en)

 **Dong Mo from Celer**

 _Celer Network is a layer-2 scaling platform that enables fast, easy and
secure off-chain transactions for not only payment transactions, but also
generalized off-chain smart contracts._

  * We've fixed CelerX game bugs under unstable network conditions.

  * We are integrating new off-chain service provider data.

  * We completed syncing game and reward history data and finished setting up sing-up and invite flow testing environment. 

  * We are preparing for mainnet internal release.

  * We completed work on upgradability of channel contracts and migrated system setup to Kubernetes.

  * We began end-to-end system and performance testing this week.

#### Application infrastructure

 **Alexandra from Parity Technologies**

 _Parity  Technologies builds core blockchain infrastructure, from Parity
Ethereum, an Ethereum client, to Polkadot, an interoperable blockchain
network._

  * New tutorial: [How to build a UTXO chain on Substrate](https://twitter.com/ParityTech/status/1141369671838572544).

  * [Energy Web](https://twitter.com/ParityTech/status/1141282067319336960), a chain built with Parity Ethereum features, launches

  * ChainX launches--the first mainnet launch of a chain built on Substrate

  * New breakdown: [how Substrate and Polkadot fits into the blockchain scalability ecosystem](https://hackernoon.com/simply-explained-blockchain-scalability-solutions-past-present-and-future-1bc4d5c309b6)

  * Free [Substrate workshop in Barcelona](https://twitter.com/ParityTech/status/1141999040994971648)

  * [We're hiring!](https://www.parity.io/jobs/) New opening: [Content Strategist.](https://www.parity.io/jobs/#berlin-content-strategist)

**Matt from Keep Network**

 _The Keep Network is a privacy layer for public chains, enabling
interactivity with private data and interoperability across chains. It does
this with keeps, off-chain containers for private data that help smart
contracts harness the full power of the public blockchain._

  * Private testnet is up and running

  * Callbacks for relay entries - as an application developer you can specify what contract and what function should be invoked when your relay entry is ready

  * Command-line interface for calling smart contract functions - it's used primarily for development purposes - we can call any function from our smart contracts from the command line, and execute view functions in previous blocks' context, it's very helpful for debugging purposes.

  * [EIP 152](https://github.com/ethereum/EIPs/pull/2129) confirmed for next Ethereum hard fork

 **David from Sia**

 _Sia is a decentralized cloud storage platform leveraging blockchain
technology to create a data storage marketplace that is more robust and more
affordable than traditional cloud storage providers._

  * RC2 version of the upcoming 1.4.1 version of Sia was released in Discord for testing. It features memory use, performance and UI improvements compared to the previous RC.

  * Eddie, Zach, Manasi, and Steve worked on multiple improvements on the UI, as more clear explanation texts, improved screens when creating an allowance or recovering backups, the ability to cancel the allowance on the UI and the correction of multiple visual glitches.

  * Matt added a new API endpoint for checking the current filter of hosts set up by the user: /hostdb/filtermode [GET]. On siac, this is used with the command siac hostdb filtermode. The previous command for setting a new filter has been moved to siac hostdb setfiltermode.

  * David tweaked the Hosts selection process when the renter forms an allowance, that now penalizes harder hosts with little remaining storage if the software expects it won’t suffice for our storage needs.

  * The Sia network reached 400 TB of used storage. This represents a 100 TB increase in the last 25 days

  * The Goobox app developers published an article explaining how to backup Synology NAS machines on the Sia network using their SiaS3 product: <https://medium.com/@goobox/backup-files-to-sia-using-synology-nas-goobox-2f31e273bbab>

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

