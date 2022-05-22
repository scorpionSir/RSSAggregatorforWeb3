[![](https://substackcdn.com/image/fetch/w_96,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F37b09348-f4f1-47a2-b9e0-a2007299e6e4_256x256)](https://proofofwork.news)

# [Proof of Work](https://proofofwork.news)

SubscribeSign in

Share this post

Proof of Work #76

proofofwork.news

Copy link

Twitter

Facebook

Email

# Proof of Work #76

[Eric Meltzer](https://substack.com/profile/138320-eric-meltzer)

Oct 15, 2019

[Share](javascript:void\(0\))

Hi from Shanghai!

Just a heads up that this is three weeks worth of updates, so some teams’
updates may seem a bit longer. No intro this week but we’ll be back next week!

#### Bitcoin & Friends

 **Jimmy on Bitcoin**

 **[Optech](https://bitcoinops.org/en/newsletters/) on Bitcoin [ed: sign up
for their newsletter too! it’s great!]**

  * Production users of Bitcoin Core are especially encouraged to test this [latest release candidate](https://bitcoincore.org/bin/bitcoin-core-0.19.0/) to ensure that it fulfills all of your organization’s needs.

  * Experienced users of LND are encouraged to [help test](https://github.com/lightningnetwork/lnd/releases/tag/v0.8.0-beta-rc2) the next release.

 **Tony from Kadena**

 _Kadena is building Pact, a formally verifiable smart-contracting language
for financial applications, and Chainweb, a PoW blockchain that uses multiple
chains in parallel to increase throughput._

  * As part of Kadena's progress towards mainnet launch this winter, we recently released [testnet v3](https://medium.com/@vivkadena/kadena-public-testnet-v3-mining-hash-algorithm-api-acc0e08401f3) featuring open mining of the Kadena tesnet.

  * Kadena received a grant from the Interchain Foundation for [Kadenament](https://www.coindesk.com/cosmos-will-have-3-coding-languages-heres-why-that-matters-for-ethereum), an implementation of the Pact smart contract language on Tendermint.

  * Introduction of [Kadena Improvement Protocols](https://medium.com/kadena-io/introducing-kips-kadena-improvement-proposals-5533e507c7af) (KIPS).

  * The hash function for our mainnet will be Blake2S [PR 431](https://github.com/kadena-io/chainweb-node/pull/431).

  * Standalone mining API [PR 270](https://github.com/kadena-io/chainweb-node/pull/270) & [PR 348](https://github.com/kadena-io/chainweb-node/pull/348).

  * Gauntlet Networks published a post on their [security analysis of Kadena's protocol](https://medium.com/gauntlet-networks/analysis-of-kadenas-public-blockchain-protocol-31c66347e32e).

  * Kadena Scalable Permissioned Blockchain is now on MS [Azure Marketplace](https://www.forbes.com/sites/darrynpollock/2019/08/28/kadena-offers-free-enterprise-grade-blockchain-service-on-microsoft-azure/#135e1e203085).

 **Aviv from Spacemesh**

 _Spacemesh is a programmable cryptocurrency powered by a novel proof-of-
space-time consensus protocol._

  * Spacemesh is chosen as  _SD Times_[Open Source Project of the Week](https://sdtimes.com/os/sd-times-open-source-project-of-the-week-spacemesh/)

  * The current focus for SVM is the Golang binding - check it out here [Spacemesh virtual machine repo](https://github.com/spacemeshos/svm)

  * The wallet/node application continues to be refined as we track towards v0.2 release and our upcoming test net.  [Bug fixes here.](https://github.com/spacemeshos/smapp/issues?q=is%3Aissue+is%3Aclosed)

  * Defined end-user labeling of TXs [here](https://github.com/spacemeshos/product/blob/master/transactions_state.md)

  * [Watch](https://www.youtube.com/watch?v=wE7hpa-UgOA&feature=youtu.be) Crypt-O-Mesh Technology Room Session with Tal Moran 

  * "A New Human Chain" [blog](https://spacemesh.io/a-new-human-chain/) by Lane Rettig about why he joined Spacemesh.

  * Cleaned up and revamped Spacemesh product repo with [updated roadmap, timeline, and several specs](https://github.com/spacemeshos/product)

  * New pages in the testnet guide in preparation for the open testnet. [See](https://testnet.spacemesh.io/#/all)

  * Major cleanup to go-spacemesh wikis - lots of outdated information removed. [Still more to do.](https://github.com/spacemeshos/go-spacemesh/wiki)

  * Updated [product plan](https://github.com/spacemeshos/product/blob/master/product_plan.md)

  * Making SVM work with wasmer 0.8 - [Spacemesh virtual machine repo](https://github.com/spacemeshos/svm)

  * [Overview of Spacemesh Virtual Machine 1st Milestone](https://medium.com/spacemesh/svm-446b106025bd)

  * For our go-spacemesh p2p full node client, we added signatures to activation transactions and NIPoST persistency as part of our node reboot tolerance. We are running tests and defining the protocol parameters and specs that we will run the test net with. [Merged issues](https://github.com/spacemeshos/go-spacemesh/pulls?q=is%3Apr+is%3Aclosed)

  * More info on [our site](https://spacemesh.io/)

 **Izaak from Coda**

 _Coda is the first cryptocurrency protocol with a constant-sized blockchain.
Coda compresses the entire blockchain into a tiny snapshot the size of a few
tweets using recursive zk-SNARKs._

  * Izaak is teaching an all-day Zero Knowledge workshop during SF Blockchain Week with Vitalik. You'll get hands-on experience programming SNARKs into your dapp - [early bird tickets](http://bit.ly/SFBWZKP) available until 10/18. 

  * Paul made it possible to refer to information about the [protocol state](https://github.com/CodaProtocol/coda/pull/3101) in transactions, which will enable time-locked accounts, conditional payments and other more sophisticated functionality.

  * Matthew added an OCaml syntax extension to make [versioning types](https://github.com/CodaProtocol/coda/pull/3621/files) (for backwards compatibility) far easier.

  * Gareth fixed a [bug](https://github.com/CodaProtocol/coda/pull/3611) in the GraphQL API.

  * Carey added docs for the [GUI wallet](https://github.com/CodaProtocol/coda/pull/3587), which looks great.

#### Privacy coins

 **Daniel from Grin**

 _Grin is a community-driven implementation of the Mimblewimble protocol that
aims to be privacy preserving, scalable, fair, and minimal._

  * Merged PRs: [10 in /grin](https://github.com/mimblewimble/grin/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A2019-09-30..2019-10-06+) | [5 in /grin-wallet](https://github.com/mimblewimble/grin-wallet/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A2019-09-30..2019-10-06+) | 4 unique contributors

  * In the last [governance meeting](https://github.com/mimblewimble/grin-pm/blob/master/notes/20190924-meeting-governance.md), the site redesign work was reviewed, the process for how to publish the security audit findings was agreed on, and the proposal to hire a cryptographer was evaluated.

  * Yeastplume added [experimental support of TOR hidden services in grin-wallet](https://www.grin-forum.org/t/yeastplume-progress-update-thread-mar-19-to-sep-19/4303/40).

  * [Node](https://github.com/mimblewimble/grin/milestone/14) and [Wallet](https://github.com/mimblewimble/grin-wallet/milestone/5) milestones for v2.1.0 were all completed and a beta1 was cut. Expect another beta version imminently, and everything is so far on track for a release in mid-October.

  * [Grin-tech.org domain has expired](https://www.grin-forum.org/t/grin-tech-org-domain-expiration/6153). Ignotus Peverell - if you're reading this [ _ed: pretty sure Ignotus is a POW reader!]_ , please get in touch with us or renew the domain. The community is working on mitigations, but we'd like to retain control of the domain if possible. We've provisionally redirected to a new project website, [https://grin.mw](https://grin.mw/) until we regain control of the old [grin-tech.org](http://grin-tech.org/) domain.

  * Grin [v2.1.0-beta3](https://www.grin-forum.org/t/grin-grin-wallet-2-1-0-beta-3-released/6174) was released.

  * In the last [development meeting](https://github.com/mimblewimble/grin-pm/blob/master/notes/20191001-meeting-development.md), planning and branching following v2.1.0 was covered, some discussion on the TOR proof of concept, and whether we should alway be storing the kernel excess.

  * Daniel from Grin [appeared on the ZeroKnowledge podcast](https://www.zeroknowledge.fm/97).

  * Grin is 100% funded by donations. Please support Grin development - [Donate now](https://grin-tech.org/general_funding).

  * More Grin info [here](https://grinnews.substack.com/).

 **Beni from Beam**

 _Beam is a confidential and scalable cryptocurrency based on Mimblewimble._

  * We have released our latest Roadmap update and you can read it [here](https://medium.com/beam-mw/beam-development-status-and-roadmap-update-2bfdcaa9c729)

  * Read [how to setup a free Beam node using Google Cloud Computing](https://medium.com/beam-mw/how-to-setup-a-free-beam-node-with-google-cloud-computing-4fc3d3e8d85a)

  * [GUI Swap] Close Create Swap Offer page on Public Offer click [#931](https://github.com/BeamMW/beam/issues/931)

  * [GUI Swap] The received amount isn't displayed correctly [#927](https://github.com/BeamMW/beam/issues/927)

  * [GUI Swap] Accept offer button on Atomic Swap [#888](https://github.com/BeamMW/beam/issues/888)

  * [GUI Swap] Add statuses to Atomic swap transactions [#889](https://github.com/BeamMW/beam/issues/889)

  * [GUI Swap] View send beam/receive beam switch [#914](https://github.com/BeamMW/beam/issues/914)

  * Excluding merges, [9 contributors have pushed 123 commits](https://github.com/BeamMW/beam/pulse) to master and 130 commits to all branches. On master, 148 files have changed and there have been 5606 additions

 **Arnaud from AZTEC Protocol**

 _AZTEC Protocol is an efficient zero-knowledge protocol built on top of
Ethereum, making plug-and-play value transmission and asset governance privacy
tools for developers and companies.  _

  * Our main priorities are a POC implementation of [PLONK](https://vitalik.ca/general/2019/09/22/plonk.html) (the universal zk-snark construction we released in collaboration with Protocol Labs), the launch of our Ignition ceremony MPC ([sign up here](https://aztecprotocol.us7.list-manage.com//subscribe?u=0f5fa2f22c3349ec01c3d1fdc&id=1b8d51cab0)), and the final touches for our production launch.

  * Tom and Zac are at Devcon this week, reach out on twitter or at [tom@aztecprotocol.com](mailto:tom@aztecprotocol.com) or [zac@aztecprotocol.com](mailto:zac@aztecprotocol.com) if you want to meet up

  * We’ve been busy running dress rehearsals for our Ignition ceremony, and making changes to the Ignition codebase to make offline participation easier.

  * This week we have also been shoring up our browser extension, adding a more complete UI test harness and a UI.

  *  **ASK:** We’re looking for people who want to get involved with Ignition. You can [sign up here](https://aztecprotocol.us7.list-manage.com//subscribe?u=0f5fa2f22c3349ec01c3d1fdc&id=1b8d51cab0), or learn more about what it entails [here](https://medium.com/aztec-protocol/snapshot-of-the-aztec-ceremony-3052f979577f).

#### Smart contracting platforms

 **Evan from[Ethereum](https://weekinethereumnews.com/)**

 _Ethereum  is a decentralized platform for applications that aims to resist
fraud, censorship or third-party interference._

  * [Beam Sync](https://medium.com/@jason.carver/intro-to-beam-sync-a0fd168be14a) from the Python client team.  In order to reduce sync time to a matter of minutes, it gets all block headers, executes a recent block using the witness and subsequently fills in state as it executes blocks by getting data from peers.

  * “[Wasm execution engine [running in] the shard chain/client we built in lighthouse](https://twitter.com/wjvill/status/1176973082604572673)” - the ConsenSys Quilt team

  * [Connext v2 is on mainnet](https://medium.com/connext/connext-v2-0-is-on-mainnet-b818864d3687) using the unified Ethereum state channel spec.  Natively supports wallets, stricter trust assumptions

  * A tactical shift for eth2: [less shards (64?) but faster cross-shard comms](https://notes.ethereum.org/@vbuterin/HkiULaluS) and 8x higher throughput per shard

  * Meanwhile, Vitalik wrote down a bunch of things that were well known to people who read Week in Ethereum News, but apparently Coindesk reporters don't.  To wit: the [eth1 to eth2 transition plan](https://ethresear.ch/t/the-eth1-eth2-transition/6265), why [sharding does not break defi composability](https://ethresear.ch/t/cross-shard-defi-composability/6268), and some options for a [2way bridge between eth1 and eth2](https://ethresear.ch/t/two-way-bridges-between-eth1-and-eth2/6286)

  * Plasma Group and Uniswap ran an [Optimistic Rollup demo at Devcon](https://decrypt.co/10030/plasma-group-and-uniswap-release-new-ethereum-scaling-solution-at-devcon), which enables hundreds of transactions per second

 **Peter from NEAR**

 _NEAR is a sharded proof-of-stake blockchain._

  * 60 PRs across 18 repos by 20 authors. Featured repos: [nearcore](https://github.com/nearprotocol/nearcore), [nearlib](https://github.com/nearprotocol/nearlib), [near-shell](https://github.com/nearprotocol/near-shell/), [near-wallet](https://github.com/nearprotocol/near-wallet), [near-bindgen](https://github.com/nearprotocol/near-bindgen), and [borsh](https://github.com/nearprotocol/borsh).

  * New [documentation portal](https://docs.nearprotocol.com/) that is easier to [contribute to](https://github.com/nearprotocol/docs/tree/master/website)

  * BLS support for block production / approvals

  * “View and Change” methods dramatically [improved](https://github.com/nearprotocol/NEPs/pull/18)

  * New CI process with hooks added to [explorer](https://github.com/nearprotocol/near-explorer/pull/85)

  * Memory limits increased for [contracts deploying contracts](https://github.com/nearprotocol/nearcore/pull/1373)

  * Factory contracts are available! [Here’s an example](https://github.com/nearprotocol/near-bindgen/pull/27) in rust

  * Removed block transactions

  * Merkle proofs added to state responses

  * Economics now include [storage rent](https://github.com/nearprotocol/nearcore/pull/1352)

  * 33 PRs across 19 repos by 17 authors. Featured repos:[ nearcore](https://github.com/nearprotocol/near-wallet),[ nearlib](https://github.com/nearprotocol/nearlib),[ near-shell](https://github.com/nearprotocol/near-shell/),[ near-wallet](https://github.com/nearprotocol/near-wallet),[ near-bindgen](https://github.com/nearprotocol/near-bindgen), [docs](https://github.com/nearprotocol/docs), [assemblyscript](https://github.com/nearprotocol/assemblyscript), [near-runtime-ts](https://github.com/nearprotocol/near-runtime-ts), [crypto-corgis](https://github.com/nearprotocol/crypto-corgis-solution), [borsh](https://github.com/nearprotocol/borsh), and [near-explorer](https://github.com/nearprotocol/near-explorer/);

  * [Genesis ](https://github.com/nearprotocol/NEPs/pull/19)block design;

  * [NEP-4](https://github.com/nearprotocol/NEPs/pull/4) Market-integrated Token Standard;

  * [Adapt nearlib staging](https://github.com/nearprotocol/nearlib/pull/80) to support master branch from nearcore with legacy tx result in nearlib;

  * [Account Detail Page](https://github.com/nearprotocol/near-explorer/pull/93) added to explorer;

  * [Link account names](https://github.com/nearprotocol/near-explorer/issues/96) (sender/receiver) to /accounts/<name> in list of transactions;

  * Move away from compiler and create [new near compiler frontend](https://github.com/nearprotocol/near-runtime-ts/pull/86) in near-runtime-ts;

  * [Several UI and storage changes](https://github.com/nearprotocol/crypto-corgis-solution/pull/4) in crypto corgis;

  * [Replace env_test feature](https://github.com/nearprotocol/near-bindgen/issues/29) with wasm target conditional compilation in near-bindgen;

  * [Manual Recovery w/ Seed Phrase](https://github.com/nearprotocol/near-wallet/issues/156) in near-wallet. 

  * 60 PRs across 20 repos by 20 authors. Featured repos:[near-explorer](https://github.com/nearprotocol/near-explorer/), [nearcore](https://github.com/nearprotocol/near-wallet),[ nearlib](https://github.com/nearprotocol/nearlib), [NEARStudio](https://github.com/nearprotocol/NEARStudio/),[ near-shell](https://github.com/nearprotocol/near-shell/),[ near-bindgen](https://github.com/nearprotocol/near-bindgen), [near-bindgen-as](https://github.com/nearprotocol/near-bindgen-as), [docs](https://github.com/nearprotocol/docs), and [near-runtime-ts](https://github.com/nearprotocol/near-runtime-ts);

  * [Unit tests](https://github.com/nearprotocol/near-explorer/pull/104) for the front-end in near-explorer;

  * Include [transaction detail page](https://github.com/nearprotocol/near-explorer/issues/91);

  * Codeowner added on [staging](https://github.com/nearprotocol/nearcore/pull/1443) and [master](https://github.com/nearprotocol/nearcore/pull/1442);

  * Updated [Genesis block design](https://github.com/nearprotocol/NEPs/pull/19);

  * [Switch to BLS key](https://github.com/nearprotocol/nearcore/pull/1418) for validators in testnet.json;

  * [Updated near-shell](https://github.com/nearprotocol/NEARStudio/pull/155) to test new functions;

  * Use [new staking transaction format;](https://github.com/nearprotocol/nearlib/pull/84)

  * [Updated error handling](https://github.com/nearprotocol/nearlib/pull/85) done by staging;

 **AJ from Tezos**

 _Tezos is a self-amending blockchain that features formally verified smart
contracts, on-chain governance, and a proof-of-stake consensus algorithm which
enables all token holders to participate in the network.  _

  * TzStats has launched a [Tezos Babylon testnet](https://babylonnet.tzstats.com/), Babylon is the current tezos upgrade proposal. 

  * Tezos Global Summit, [TQuorum](http://tquorum.com/) is underway with hundreds of people all over the world learning more about the Tezos protocol. The Summit will feature talks from key contributors in the Tezos ecosystem, technical workshops, and panels. 

  * [Tezos Agora](http://tezosagora.org/) has launched, the first governance explorer + discussion forum for Tezos. 

  * [Tezos Rust Node: a deep dive in the Tezos P2P layer](https://medium.com/simplestaking/tezos-rust-node-a-deep-dive-into-the-tezos-p2p-layer-98e3b3e3b704)

 **Topper from Quorum Control**

 _Quorum Control makes Tupelo, a permissionless proof of stake DLT platform
purpose-built to model individual objects that enables flexible public or
private data models._

  * The team conducted another round of performance testing on the latest version of Tupelo and published the results. The upshot is that when getting transactions signed by the network at 200tx/sec the mean response time was 144 ms. The devil is in the details and you can [read more about those here](https://docs.quorumcontrol.com/platform_performance.html#september-27th---latest-update).

  * Additional monitoring was put on the test and game networks this week to improve escalation paths using opsgenie. The additional alerts focus on CPU usage and key processes being up. This work is part of our ongoing efforts to “productionize” the test networks in anticipation of upcoming production apps launching on them.

  * The team released improvements to the wasm SDK moving it to v0.0.13 which includes better memory handling and a simplification of the resolve interface. Additional details on the [release and associated PRs are available](https://github.com/quorumcontrol/tupelo-wasm-sdk/releases/tag/v0.0.13) and we welcome feedback in our [developer Telegram channel](https://t.me/joinchat/IhpojEWjbW9Y7_H81Y7rAA).

  * Optimizations were made eliminating unnecessary portions of ChainTrees from exchanges between clients, signers, and their associated caches. The update improves performance significantly when large ChainTrees are signed. Tupelo version 0.5.0, available for download next week, includes the change.

  * The team made strides in the development of a Tupelo specific web wallet using our WASM SDK. The Tupelo wallet enables users to create, send, and receive ChainTrees and tokens.

  * Optimizations were made eliminating unnecessary portions of ChainTrees from exchanges between clients, signers, and their associated caches. The update improves performance significantly when large ChainTrees are signed. Tupelo version 0.5.0, available for download next week, includes the change.

  * The team made strides in the development of a Tupelo specific web wallet using our WASM SDK. The Tupelo wallet enables users to create, send, and receive ChainTrees and tokens.

 **Michael from Loom**

 _Loom Network is a universal layer 2 hub. Developers can deploy and scale
their dapps directly on Loom’s mainnet as well as interoperate with other
major layer 1 chains such as Ethereum, Binance, Libra, Bitcoin, etc._

  * Huobi is the [latest validator to go live on Loom's Basechain](https://medium.com/loom-network/huobi-to-become-a-loom-network-validator-f7034401bf79)

  * Launched a [Bounties and Rewards Program](https://medium.com/loom-network/bounties-and-rewards-earn-loom-tokens-for-participating-in-the-network-f1bf65a96463), where the community can earn millions of locked LOOM tokens to the community for contributing to the network — running validators, deploying dapps, creating content, as well as curating and voting on content

#### Financial Infrastructure

 **Nelson from Cadence**

 _Cadence is a digital securitization and investment platform for private
credit. Cadence issues tokenized assets that are digital reflections of real
world fiat and investment transactions._

  * We were featured in the most recent Asset-Backed Alert in the piece, [Burger Chain Tests Blockchain Deal](https://withcadence.io/blog/news-item/burger-chain-tests-blockchain-deal/) for a $30M+ whole-business securitization.

  * Through August, we’ve now issued over $17.3M in offerings.

  * We recently launched extended authentication with Plaid, allowing our users to connect any bank account they’d like.

  * Our recently launched [real-time data feature](https://withcadence.io/blog/delivering-on-the-promise-of-real-time-data-for-private-credit/) has been a success and continues to expand with new offerings and new originators.

  * Cadence Founder & CEO Nelson Chu gave a keynote at the World Blockchain Forum in NYC on Sept. 27 titled, “The Future of Securitization On Chain.” He also moderated a panel on “Blockchain & Fintech Industry Trends.”

  * We're [hiring engineers](https://angel.co/company/withcadence/jobs)!

 **Antonio from dYdX**

 _dYdX is a decentralized exchange for margin trading, borrowing, lending, and
eventually derivatives. dYdX allows traders to trustlessly short and get
leverage on crypto assets._

  * Making various frontend improvements to our ETH-DAI native market

  * Improving reliability of orderbook and matching-engine services

  * Over $4.5M liquidated last week. Liquidators earned over $225k in liquidation fees. Check out our [open source liquidator bot](https://github.com/dydxprotocol/liquidator) to get in on the liquidation action!

  * [Hiring](https://dydx.exchange/careers/) software engineers & product designers full-time in SF!

 **Brendan from Dharma**

 _Dharma is the easiest place to borrow and lend cryptocurrencies. It enables
non-custodial peer-to-peer lending through smart contracts on Ethereum._

  * Continued product work on Dharma V2 onboarding flows

  * Released Coinbase oauth for Dharma V2 beta users

  * Gave access to 150 new users from the Dharma V2 waitlist

#### Layer two and interoperability

 **Tieshun from Namebase**

 _Namebase is the easiest way to buy, sell, and use Handshake._

  * Handshake was invited to present at the ICANN66 Montreal meetup in November. If you're going, look for the people wearing the yellow Handshake t-shirts!

 **Zaki from Cosmos**

 _The  Cosmos Network is a decentralized network of independent, scalable, and
interoperable blockchains._

  * [Postmortem](https://forum.cosmos.network/t/cosmos-hub-3-upgrade-post-mortem/2772) on the Delayed Cosmos Hub-3 update

  * New decentralized [testnet forming](https://forum.cosmos.network/t/looking-for-new-testnet-participants-made-from-mainnet-ledger/2745/2).

  * First Community Contribution of an IBC Application protocol: [Interchain Accounts](https://github.com/cosmos/ics/pull/278)

  * [Cosmos Web Assembly Design spec](https://hackmd.io/-1EmvfxiR9WrabXvxdOfQA?view).

 **Alexandra from Polkadot**

 _[Polkadot](https://polkadot.network/) empowers blockchain networks to work
together under the protection of shared security._

  * Kusama is an early, unaudited and unrefined release of Polkadot. After several key fixes to Polkadot, including the Babe consensus layer, we’re pleased to release the next chapter in Kusama: [New Kusama CC-2 v.0.6.2 release](https://github.com/paritytech/polkadot/releases/tag/v0.6.2).

  * New guide: [projects' options for connecting to Polkadot](https://medium.com/@KILT_Protocol/your-options-as-a-para-chain-thread-on-polkadot-edaf507ad442).

  * Presentation recording: [how parathreads work](https://twitter.com/ParityTech/status/1178702935812972545).

  * Interview: [Polkascan's multi-chain block explorer](https://twitter.com/polkadotnetwork/status/1178645478516445185).

  * Updates to the [Polkadot wiki](https://wiki.polkadot.network/en/) cover the research behind Polkadot.

  * Polkadot parathreads [PR merged](https://twitter.com/gavofyork/status/1182543953897369600): now anyone can access Polkadot connectivity. 

  * New Q&A on [Kusama](https://twitter.com/kusamanetwork/status/1183769628268478466), an early Polkadot release. 

  * Recording out: Polkadot researcher Dr. Alistair Stewart on [governance design decisions](https://twitter.com/polkadotnetwork/status/1183654945477795840). 

  * Web3 Foundation is hiring people to [help build Polkadot](https://web3.bamboohr.com/jobs/), as well as [providing grants](https://github.com/w3f/Web3-collaboration/blob/master/grants/grants.md) for software development, research, technical education and community engagement efforts related to Polkadot. 

**Dong Mo from Celer**

 _Celer Network is a layer-2 scaling platform that enables fast, easy and
secure off-chain transactions for not only payment transactions, but also
generalized off-chain smart contracts._

  * We finished new version of game platform page and the result page.

  * We keep working on the new version of payment history and match history.

  * We fixed bugs and improved stability.

  * We were testing and improving the new OSP functionality.

  * Operational setup for upcoming games releases.

  * We were preparing to open-source OSP code. 

  * We completed the development of SGN reward component.

  * We were working on the final checklist for launching async-game.

  * We are designing FIAT solutions for gaming platform.

  * We completed the first version of the Celer Web client and continue to test SGN components

  * We began the design and development of Q4 OSP functionality

#### Application infrastructure

 **Alexandra from Parity Technologies**

 _Parity  Technologies builds core blockchain infrastructure, from Parity
Ethereum, an Ethereum client, to Polkadot, an interoperable blockchain
network._

  * [New Parity Ethereum release](https://twitter.com/ParityTech/status/1177253153374429185) v2.5.9-stable and v2.6.4-beta adds the block numbers for the Istanbul hard fork for Ropsten, Görli, Rinkeby and Kovan testnets.

  * [Presentation recording](https://twitter.com/ParityTech/status/1178701484344655872): Universal Offline Signatures, developed to standardize [Parity Signer](https://www.parity.io/signer/) and hardware wallets of the future.

  * There's an open-source block explorer for any blockchain built with the Substrate framework. [New podcast interview](https://twitter.com/RelayChain/status/1177645343468670977) goes into the details. 

  * Interview with CEO Jutta Steiner: [making blockchain development easier using Substrate](https://twitter.com/DavidJN79/status/1176116274587414528).

  * We [released an update to Parity Signer](https://twitter.com/ParityTech/status/1179378636387999750), the app that lets you take an old mobile device and turn it into a hardware wallet. New features include Kusama CC2 support and support for Universal Offline Signatures, the standard created for efficient data transmission through QR codes.

  * [HiveNet detailed why they're building their blockchain](https://medium.com/official-hivenet-blog/hivenet-to-build-on-parity-substrate-fd90e640ea83) on Parity's Substrate blockchain framework.

  * The [pure Rust implementation of secp256k1](https://github.com/paritytech/libsecp256k1) is now under @paritytech.

  * [We passed 100 team members and are still growing!](https://www.parity.io/jobs/#jobs) Openings include Blockchain Ops, Blockchain Runtime Engineer, DevOps, Ecosystem Development Lead, Full Stack Developer, HR Manager, Internal Tools Developer, Junior Ops Manager, and Rust/Core Developer. 

  * Parity CEO Dr. Jutta Steiner was [on BBC4](https://twitter.com/jutta_steiner/status/1182463799405764608) to discuss the future of blockchain.

  * Ivo from AdEx network spoke about [leveraging Substrate to solve validator downtime. ](https://twitter.com/polkadotnetwork/status/1181964130254761992)

  * Polkascan, the chain explorer for Substrate chains, now [supports Kulupu](https://twitter.com/polkascan/status/1180243866311647233) (a Substrate PoW chain).

  * [C++ API for Substrate demo](https://twitter.com/polkadotnetwork/status/1182567775052685313). 

 **Doug from Livepeer**

 _Livepeer is a decentralized video infrastructure network, dramatically
reducing prices for developers and businesses building video streaming
applications at scale.  _

  * The Streamflow release is [now feature-frozen](https://github.com/livepeer/protocol/tree/streamflow) and undergoing an external security audit.

  * Users of the popular Wowza media server for live streaming can now tap into the Livepeer Streamflow preview network for transcoding - [pilots are open](https://mailchi.mp/livepeer.org/pluginpartner).

  * The Streamflow release is [now feature-frozen](https://github.com/livepeer/protocol/tree/streamflow) and undergoing an external security audit with Trail of Bits.

  * A new staking application is now in in beta, with the goal of allowing new users to go through their initial staking experience in under 5 minutes. Give it a try at [http://beta.explorer.livepeer.org](http://beta.explorer.livepeer.org/)

  * Benchmarks for [initial GPU mining \+ transcoding](https://medium.com/livepeer-blog/livepeer-gpu-miner-update-663a3e19de56) are published on the blog.

 **Matt from Keep Network**

 _The Keep Network is a privacy layer for public chains, enabling
interactivity with private data and interoperability across chains. It does
this with keeps, off-chain containers for private data that help smart
contracts harness the full power of the public blockchain._

  *  **tBTC:R**

    * Completed refactoring of how tBTC talks to ECDSA keeps

    * Implemented state management for ECDSA keep sMPC cluster nodes

    * Made good progress on the upgrade to the most recent bitcoin SPV version

    * Implemented a preliminary signer selection process, allowing different signers in the system for different deposits.

    * Implemented the first several steps of the redemption flow.

    * Several dApp updates in the pipe, including an initial pass at a dApp for deposit redemption.

  *  **Random beacon:  **

    * Completed work on random beacon pricing research

    * Refined network setup to allow for nodes behind NAT

    * Enhanced validation of group tickets to cover the check of all ticket values

    * Made progress on the pricing implementation, we are currently filling in the last gaps

    * Support is now there for multiple bootstrap peers.

    * The remaining pieces of beacon group candidate selection have been completed.

    * Progress on beacon pricing as well as stake management.

    * For more updates and questions join our [Slack](https://bit.ly/2FMkV6T) and check out the [Keep blog](https://blog.keep.network/).

 **David from Sia**

 _Sia is a decentralized cloud storage platform leveraging blockchain
technology to create a data storage marketplace that is more robust and more
affordable than traditional cloud storage providers._

  * Community member tbenz9 was busy this week, [improving the output](https://gitlab.com/NebulousLabs/Sia/merge_requests/3865) for the command siac alerts. It now sorts the output based on alert severity and is easier to read. 

  * He also [updated the main README fil](https://gitlab.com/NebulousLabs/Sia/merge_requests/3847)e to include instructions for building Sia for the Raspberry Pi

  * And [added a new siac utils bruteforce-seed command](https://gitlab.com/NebulousLabs/Sia/merge_requests/3872) that will attempt to find a missing word from a Sia seed

  * Chris [fixed a community reported bug](https://gitlab.com/NebulousLabs/Sia/merge_requests/3868) where the consensus API endpoint height and block hash did not match

  * Matthew [improved the siac ratelimit command](https://gitlab.com/NebulousLabs/Sia/merge_requests/3857)s by allowing them to accept values in various units

  * Marcin dramatically improved the[ formatting and behavior of siac commands ](https://gitlab.com/NebulousLabs/Sia/merge_requests/3794)when not all the modules were loaded

  * The Sia team held a community meetup in LA on Thursday September 26th

  * Nebulous still has [4 open job postings](https://angel.co/company/nebulous/jobs)

  * Community member tbenz9 [improved the output](https://gitlab.com/NebulousLabs/Sia/merge_requests/3866) for the command siac renter -v to show current allowance details.

  * He also fixed a [number of spelling errors](https://gitlab.com/NebulousLabs/Sia/merge_requests/3876) and removed duplicate documentation in various sections of the codebase.

  * Marcin updated a piece of code called the [transactionbuilder](https://gitlab.com/NebulousLabs/Sia/merge_requests/3873) to support double-spend creation. This is necessary for his upcoming watchdog implementation.

  * Marcin also removed a [few hundred lines of code](https://gitlab.com/NebulousLabs/Sia/merge_requests/3878) that are no longer needed due to previously completed code updates.

  * The Sia team now officially supports the [Sia-coldstorage](https://gitlab.com/NebulousLabs/sia-coldstorage) app.  This wallet is used for offline (cold) Siacoin and Siafund storage.

  * Nebulous announced their [settlement for Siafunds sold in 2014](https://www.reddit.com/r/siacoin/comments/dbu31b/announcing_our_sec_settlement_for_siafunds_no/).  This is a landmark crypto settlement that may influence many other coins that have had a securities sale in the last few years.

  * Sia community site [Siastats.info](http://siastats.info/) announced a new feature to [obtain a csv file with all your transactions](https://www.reddit.com/r/siacoin/comments/daydpc/now_you_can_obtain_a_csv_file_with_all_your/) converted to local currencies. This feature should make Siacoin taxes much easier to calculate.

  * Sia community site siacentral launched [version 1.0.5](https://siacentral.com/host-manager/download) of their popular host-manager app.

  * There has been a wave of Discord users impersonating Sia team members and asking for donations.  Nebulous employees or moderators will never ask you for coins, for trades or for your seed. If you’re caught impersonating a team member or moderator you will be banned immediately without warning.

  * Sia had big news this week with the addition of a new core dev, and a big exchange now trading Siacoins.

  * Nebulous hired Peter-Jan Brone as a Sia Core Developer. He will focus in extending the host and renter functionalities and building the future “payment routing” feature of Sia. 

  * Marcin removed the old Host-Renter communication protocol, that got replaced on version 1.4.0. If you are hosting on 1.3.7 or earlier, remember to update your client right away.

  * Matt added a specific API endpoint for cancelling a renter’s allowance /renter/allowance/cancel [POST]. The current endpoint is still valid to avoid impacting compatibility.

  * rishi.vikram.1, tbenz9, pjbrone and lukechampine extended the Sia documentation, improving the API and Resources documentation and detailing instructions for building the code in Go 1.13.

  * Various fixes and improvements have been applied to the miner and gateway modules, to the host database functions and to the file repair functionality.

  * Community member ScottG released the alpha [version 1.0.9 of Repertory](https://bitbucket.org/blockstorage/repertory-testing/downloads/). Repertory is an app that allows you to mount Sia storage as another drive on your computer. This version enables sharing these mounted drives across two Windows computers

  * The Kraken exchange [listed Siacoin](https://blog.kraken.com/post/2842/siacoin-trading-starts-october-9/), available on the standard, Pro and OTC services.

  * The Sia network reached a new record of used storage on Saturday: 605 TB.

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

