[![](https://substackcdn.com/image/fetch/w_96,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F37b09348-f4f1-47a2-b9e0-a2007299e6e4_256x256)](https://proofofwork.news)

# [Proof of Work](https://proofofwork.news)

SubscribeSign in

Share this post

Proof of Work #61

proofofwork.news

Copy link

Twitter

Facebook

Email

# Proof of Work #61

[Eric Meltzer](https://substack.com/profile/138320-eric-meltzer)

Apr 3, 2019

[Share](javascript:void\(0\))

Hi from San Francisco!

At Primitive, my partner Dovey and I feel that a part of our advantage over
other managers is our visibility into both the US and Asian crypto scenes.
There’s a real blindness among many people in the US scene to what’s going on
in Asia, particularly in China. We’ve decided to give away this advantage to
everyone reading PoW, in the form of an additional column of updates on the
Asian crypto scene: mining, exchange hacks, random shitcoins raising hundreds
of millions of RMB, Chinese government regs and all. This is a bit
experimental: if you like it, or if you don’t please hit reply and let me
know!

Some highlights this week: Sia hit a huge milestone with their 1.4 release,
which gets them close to being able to work as a truly viable low-cost
filesharing solution, Grin got a cool Chinese name (古灵币, literally “ancient
spirit coin”), and Coinbase launched a staking service that supports Tezos to
start.

Tiny housekeeping thing: projects that don’t update in a given week won’t be
mentioned. Don’t worry, they haven’t been dropped—they’ll be listed again any
time they send an update.

Thanks as always for reading PoW, and please ping me here or on Twitter if
there is any way I can make it more useful for you!

#### China & Asia Updates

 **Mining**

  * Upcoming wet season brings extremely low electricity costs (lower than 3 US cents) revitalizing the mining community

  * The consensus among miners is that total BTC hashrate will go back up to 60E. Even if BTC price stays around $4000, thanks to cheap electricity, many old mining models can be back online and profitable again (even WhatsMiner M3 and Avalon 7 Series, which are in the red now)

  * Bitmain announced new CEO, Micree remains as chairman of the board, and Jihan remains a board member. Jihan made a first public appearance for a keynote 3 days after the announcement 

**ASIC**

  * Sales of the new AntMiner S17 from Bitmain will start on April 9th 

  * A new ASIC firm VidToo (Hangzhou) announced a Cuckoo Cycle ASIC G1, claiming to be 50x more efficient than GPUs. Detailed specs will be published in late April. Currently announced Grin ASICs now include Innosilicon, VidToo and Obelisk—of these, only Obelisk has published [specs](https://obelisk.tech/products/grn1.html) so far. 

**Exchanges**

  * DragonEx was hacked, Bitthumb was hacked, and there is some suspicion that Coinbene was also hacked. [ _ed: I assume that 100% of “hacks” are actually inside jobs until proven otherwise_ ]

  * Gate.io (finally) announced its own [exchange coin](https://www.gateio.co/article/16808) with a fairly unique distribution model (different than all the BNB clones)

  * Too many IEOs to keep track of (Huobi, Bittrex, ZB, ..everybody is doing IEOs) 

**Regulatory**

  * The Cyberspace Administration of China ( _ed: I wonder what[Gibson](http://twitter.com/greatdismal) thinks when he reads those four words_) announced the first batch of companies that are compliant with regulation filing known as “blockchain information service registration” There are 197 companies in the first batch including Alibaba, Tencent, and Baidu ([full list here](http://www.cac.gov.cn/1124305122_15539349948111n.pdf), filing [requirements here](http://www.cac.gov.cn/2019-01/10/c_1123971164.htm)).

#### Bitcoin & Friends

 **[Optech](https://bitcoinops.org/en/newsletters/2019/03/12/) on Bitcoin [ed:
sign up for their newsletter too! it’s great!]**

  * Bitcoin fees are up a bit recently: after over a year of most Bitcoin transactions confirming rather quickly as long as they paid a feerate above the default minimum relay fee (except during [a brief exceptional period](https://bitcoinops.org/en/newsletters/2018/11/20/)), a modest backlog has developed over the previous week and raised the feerates for people who need their transactions to confirm within the next several blocks. Spenders willing to wait a bit longer can still save money. For more information, we recommend [Johoe’s mempool statistics](https://jochen-hoenicke.de/queue/#0,1w) and [P2SH.info’s fee estimate tracker](https://p2sh.info/dashboard/db/fee-estimation?orgId=1).

  *  **Trampoline payments for LN:**  Pierre-Marie Padiou started a [thread](https://lists.linuxfoundation.org/pipermail/lightning-dev/2019-March/001939.html) on the Lightning-Dev mailing list suggesting that Alice could send a payment to Zed even if she didn’t know a path to his node by first sending a payment to an intermediate node (Dan) and asking Dan to figure out the route the rest of the way to Zed. This would especially benefit Alice if she ran a lightweight LN node that didn’t attempt to keep track of the entire network. For increased privacy, Alice could use several intermediate nodes rather than just one (each one receiving its own instructions encrypted by Alice). A downside described in the email is that Alice could only make a rough guess about the required fees as she wouldn’t know the actual path, so she’d probably end up paying more in fees than if she chose the route herself.

 **Aviv from Spacemesh**

 _Spacemesh is a programmable cryptocurrency powered by a novel proof-of-
space-time consensus protocol._

  * [Basic NIPST construction flow](https://github.com/spacemeshos/go-spacemesh/pull/714) with communication to both PoET server and PoST process

  * [Automated Hare protocol testing](https://github.com/spacemeshos/go-spacemesh/pull/733) using the automation framework

  * Database [deduplication](https://github.com/spacemeshos/go-spacemesh/pull/694) for mesh transactions

  * [PoET handling RPCs from nodes](https://github.com/spacemeshos/poet-ref/pull/28)

  * PoST Merkle tree [cache optimizations](https://github.com/spacemeshos/merkle-tree/pull/6)

  * App [receive coins screen](https://github.com/spacemeshos/smapp/pull/57)

  * App send coins - connect to local node API through [gRPC calls](https://github.com/spacemeshos/smapp/pull/58)

  * App local node setup - [logical disk and capacity selection](https://github.com/spacemeshos/smapp/pull/59)

  * [Restore wallet](https://github.com/spacemeshos/smapp/pull/60) from 12 words or a wallet file

 **JZ from Decred**

 _Decred  is an autonomous digital currency with a hybrid consensus system. It
is built to be a self-ruling currency where everyone can vote on the rules and
project-level decision making proportionately to their stake._

  * Dave Collins has made some [dcrd optimizations which will be landing in our v1.5 release](https://github.com/decred/dcrd/pull/1656). They make an initial blockchain sync 20-25% faster, bringing things down to around 45 minutes for a full sync on typical hardware.

  * Richard has published a new issue of the [Politeia Digest covering March 15-31](https://medium.com/politeia-digest/issue-13-mar-15-mar-31-2019-fe4cb1507d1b), it includes discussion of the two live dev proposals that are up for vote; one to put out an RFP for Trust Wallet integration and another to move forward with the planning phase for potential ATM integration work.

  * We also have about 9 days to go for our on-chain consensus vote, so stakeholders who wish to participate should make sure their vote choices are set in their wallet. The vote can be monitored at <https://voting.decred.org/>.

 **Johnny from Stellar**

 _Stellar is an open network for sending and exchanging value of any kind. Its
global network enables digitization of assets - from carbon credits to
currencies - and enables movement around the internet with ease._

  * Core — CAP005 (surge pricing), CAP006 (buyOffer), CAP020 (Bucket list) got first round of reviews, ETA unchanged (end of April release).

  * Platform — Making good progress planning for new ingestion system, proposed Q2 Platform goals will be out this week.

  * Platform —  Additional work is being done on improved [ticker.stellar.org](http://ticker.stellar.org/)

 **Izaak from Coda**

 _Coda is the first cryptocurrency protocol with a constant-sized blockchain.
Coda compresses the entire blockchain into a tiny snapshot the size of a few
tweets using recursive zk-SNARKs._

  * We have finished fixing all of the known bugs in our proof-of-stake and implementation and now have a fully-functioning Ouroboros Praos.

  * Deepthi [implemented ](https://github.com/CodaProtocol/coda/pull/1936)a check in the SNARK to ensure coinbases are correctly distributed.

  * Paul has been improving the [versioning ](https://github.com/CodaProtocol/coda/pull/2075)of types for backwards compatibility.

  * Jiawei fixed an [important bug ](https://github.com/CodaProtocol/coda/pull/2056)in how common ancestors of blocks are computed. 

#### Privacy coins

 **Paige & Zooko from Zcash**

 _Zcash is a  digital currency utilizing zk-SNARKs to enable its privacy-
protecting properties._

  * zcashd v2.0.4 [released](https://z.cash/blog/new-release-2-0-4/)

  * Final call on [ZIP drafts for NU3 consideration](https://forum.zcashcommunity.com/t/call-for-nu3-zips-and-network-upgrade-pipeline-process-changes/32749) (due before Monday, April 1st)

  * Merged the updated [ZIP 0 specification](https://github.com/zcash/zips/blob/master/zip-0000.rst) (now both ECC and the Zcash Foundation have an Editor representative)

  * Read the [full weekly update](https://forum.zcashcommunity.com/t/march-29-2019-weekly-update-engineering/33058) for more

 **Mitchell from Monero**

 _Monero is a open-source, privacy-focused cryptocurrency using the ASIC-
resistant CryptoNote PoW algorithm. It enforces all privacy features at the
protocol level to ensure that all transactions create a single fungible
anonymity pool._

  * The wallet [will support socks proxy](https://github.com/monero-project/monero/pull/5090) (for Tor/i2pd/Kovri).

  * Monero researchers and developers are now [fully funded](https://ccs.getmonero.org/funding-required/) thanks to a generous anonymous donor(s).

  * The quick fact sheet for politicians, journalists, etc. [has been updated](https://github.com/monero-ecosystem/outreach-docs/blob/master/monero-outreach-docs/en/quickfacts/QuickFacts.pdf) by the Monero Outreach workgroup.

  * While the possibility "colored coin" transactions with RingCT/Monero has been known, the signatures were previously proportionally sized to the number of colors. A new approach removes this dependency, i.e. fixed size regardless of number of colors.

 **Daniel from Grin**

 _Grin is a community-driven implementation of the Mimblewimble protocol that
aims to be privacy preserving, scalable, fair, and minimal._

  * [12 Pull Requests were merged](https://github.com/mimblewimble/grin/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A2019-03-25..2019-03-31+) in the past week, by 8 unique contributors.

  * We passed 100k blocks height this week, @antiochp put together [some stats](https://gitter.im/grin_community/dev?at=5c9a0cc9a21ce51a20c3ac2a). 330k transactions resulting in 728k outputs, but only 48k UTXOs to keep track of...

  * @ignopeverell showed progress well under way for I2P support. Work includes dusting off the abandoned /i2p-rs client to make it ready for integration in Grin. This, and more, in his new [monthly progress update](https://www.grin-forum.org/t/igno-progress-update-thread-mar-to-june-2019/4676).

  * @yeastplume is in the process of merging a [final version of the v2 API](https://www.grin-forum.org/t/yeastplume-progress-update-thread-mar-19-to-sep-19/4303/15), and getting ready for an upcoming v1.1.0 release.

  * [Slean mining was announced](https://www.grin-forum.org/t/slean-mining-mining-cuckatoo3x-using-low-memory-gpus/4651) by @lolliedieb at the Grin Amsterdam event, making it possible for low memory GPUs to mine the Cuckatoo ASIC tuned algorithm efficiently.

  * And almost simultaneously, [there was another announcement](https://www.grin-forum.org/t/solving-cuckatoo-with-less-memory/4656) for another method that can be used to solve Cuckatoo with less memory.

  * In the [Governance meeting](https://github.com/mimblewimble/grin-pm/blob/master/notes/20190326-meeting-governance.md), ETH donations and potential changes to the phase out schedule was discussed.

  * Some incorrect news reporting made me [clarify the proof of work discussion in that meeting](https://www.grin-forum.org/t/clarifications-on-proof-of-work-phase-out-following-tuesdays-governance-meeting/4691)according to my own understanding of it.

  * @tromp [submitted a proposal](https://www.grin-forum.org/t/grin-improvement-proposal-1-put-later-phase-outs-on-hold-and-rephrase-primary-pow-commitment/4653) for specifying our proof-of-work commitment to hold for 18 months into the future, and to put later phase outs on hold. To be discussed and possibly voted on in the next governance meeting.

  * @garyyu worked with the community to [give Grin an official Chinese name](https://www.grin-forum.org/t/give-grin-a-chinese-name-grin/4376/102): 古灵币

  * [2Miners](https://www.grin-forum.org/t/2miners-grin-mining-pool-is-online-pplns-solo/4655) announced support for Grin in their mining pool for SOLO and PPLNS.

  * Grin++ node and wallet is [now on mainnet](https://github.com/GrinPlusPlus/GrinPlusPlus/releases/tag/v0.2.0).

  * [GrinPurse](https://www.grin-forum.org/t/the-first-gui-wallet-of-grin-released-awesome/4643): A closed source grin GUI wallet for macOS and Windows, made by Bitmesh exchange. To be open sourced in the next week according to the developers.

  * More Grin info [in this weekly newsletter](https://grinnews.substack.com/).

 **Beni from Beam**

 _Beam is a confidential and scalable cryptocurrency based on Mimblewimble._

  * We have released our [iOS Testnet Wallet](https://medium.com/beam-mw/mimblewimble-ios-wallet-release-notes-10110-b06f40ed727a)

  * [CoinGecko](https://www.coingecko.com/en#footer) implemented Beam as a donation method

  * [Proof of Review](https://www.proofofreview.com/) has [reviewed](https://www.proofofreview.com/wp-content/uploads/2019/04/Review-BEAM.pdf) Beam

  *  iOS Testnet - [Release Notes](https://github.com/BeamMW/ios-wallet/releases/tag/Testnet-1.0.1.10)

  *  Preparing for Bright Boson 2.0 Mainnet Release (Testnet version was [released](https://medium.com/beam-mw/beam-mimblewimble-brightboson-release-notes-2044701-9154d9b3f27d) last week) 

  * [Hardware wallet](https://github.com/BeamMW/trezor-crypto) \- Trezor  _in progress_

  *  [Atomic Swap](https://github.com/BeamMW/beam/tree/atomic_swap) CLI [#447](https://github.com/BeamMW/beam/issues/447)  _in progress_

  * [One side payments](https://github.com/BeamMW/beam/issues/540)   _in progress_

  * Bug Fixing [#554](https://github.com/BeamMW/beam/issues/554), [#552](https://github.com/BeamMW/beam/issues/552)

  * Bug Fixing [ #573](https://github.com/BeamMW/beam/issues/573)

 **Arnaud from AZTEC Protocol**

 _AZTEC Protocol is an efficient zero-knowledge protocol built on top of
Ethereum, making plug-and-play value transmission and asset governance privacy
tools for developers and companies.  _

  * We merged [3 pull requests](https://github.com/AztecProtocol/AZTEC/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A2019-03-24..2019-03-31+) this week, including:

    * [One fixing small issues](https://github.com/AztecProtocol/AZTEC/pull/79) and adding support for different kinds of notes (for example [El-Gamal treasury notes](https://github.com/AztecProtocol/AZTEC/issues/71) which extends AZTEC to [support account-based models](https://github.com/AztecProtocol/specification#type-2-el-gamal-treasury-notes))

    * [The feature work ](https://github.com/AztecProtocol/AZTEC/pull/73)to allow zero-knowledge assets to mint and burn in full confidentiality

  * This week [we implemented semantic release](https://github.com/AztecProtocol/AZTEC/pull/80) to make our repo easier to consume and contribute to

  * We’re still hiring for two cryptographers and one senior engineer to join the team. You can apply [here](http://email.mg2.substack.com/c/eJwlUEuOwyAMPU3ZNSKQpGHBoq1mrhHxcVumBEfgTJU5_RBF8sKy_fw-zhA8MW96wUJsLZCn4LVQgg8t87rz7diPLJTpkQFmE6KmvAJbVhuDMxQw7fe9kuylwUnVg3RcXQYu7eDAenvpjOx5Lweh2M4xmdUHSA40_ELeMAGL-kW0lJO8nsR3LZOeEBuHe_tH4M5LRkKH8Szr6AdtYUEL3iouRcs7LjvRtM2NX-_jnY-3QbS37ut66vj8FE1ZbSHj3vXfzLI2OVUBdecy-EBzSNQEPJTRtoBO8CkRiCAzOkKpXqcKntcUaJsgGRvB6wNSvUt1kQOrNB5rPklXsfjAxwfz-x-f0nXk), or by emailing [arnaud@aztecprotocol.com](mailto:arnaud@aztecprotocol.com) with the name of the role as the subject

#### Smart contracting platforms

 **Evan from[Ethereum](https://weekinethereumnews.com/)**

 _Ethereum  is a decentralized platform for applications that aims to resist
fraud, censorship or third-party interference._

  * Beacon Chain testiest are nigh: Nimbus eth2 [testnet is running](https://our.status.im/the-nimbus-mvp-testnet-is-here/).  Prysmatic Labs is “on the [brink of our public testnet release](https://medium.com/prysmatic-labs/ethereum-2-0-serenity-testnet-update-closer-than-ever-259cace9a1b1).” Lighthouse also says they will have a [testnet any day now](https://twitter.com/ethZed/status/1111499764418240512).

  * Plasma Group: [understanding the generalized plasma architecture](https://medium.com/plasma-group/plapps-and-predicates-understanding-the-generalized-plasma-architecture-fc171b25741)

  * Virgil Griffith on how [Ethereum changes fundamental assumptions of game theory](https://medium.com/@virgilgr/ethereum-is-game-changing-technology-literally-d67e01a01cf8)

  * UMA put a [synthetic index of US large cap equity](https://medium.com/uma-project/announcing-us-stock-index-token-powered-by-uma-and-dai-c394586c575a) on mainnet. Get exposure to US equity from anywhere in the world

 **Erik from NEAR**

 _NEAR is a sharded proof-of-stake blockchain._

  * 24 PRs in [nearcore](https://github.com/nearprotocol/nearcore) from 10 different authors

  * [Clean ups and bug fixes](https://github.com/nearprotocol/nearcore/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Aclosed+label%3Atestnet+updated%3A%3E%3D2019-03-23+) for TestNet and [dev ops](https://github.com/nearprotocol/nearcore/pull/765) configuration to run on GCP

  * Updated docs for [running a TestNet on GCP](https://docs.nearprotocol.com/tutorials/run-your-own-testnet) and [syncing to a local node](https://docs.nearprotocol.com/quick_start/expert)

  * Added persistent collections to NEAR AssemblyScript library

  * Integrated NEAR, React and next.js at our internal hackathon with a [fun toy](https://metanear.com/) and a [simpler example](https://app.near.ai/ee4arncdv/).

  * near-shell updates

    * Near new_project generates a blank project in chosen dir 

    * Ability to run tests against devnet now works.

  * Updated UI for the debugger.

  * Made [example chess game](https://github.com/nearprotocol/near-chess) deployed on GitHub Pages 

  * Automated deployment: `npm run deploy` builds contract, deploys it to devnet and deploys frontend to GitHub Pages.

 **AJ from Tezos**

 _Tezos is a self-amending blockchain that features formally verified smart
contracts, on-chain governance, and a proof-of-stake consensus algorithm which
enables all token holders to participate in the network.  _

  * [Coinbase Custody launches its first full-service, regulated, insured, and 100% offline staking service](https://blog.coinbase.com/coinbase-custody-launches-staking-support-for-tezos-makerdao-governance-to-follow-68f7bc51bc53). Tezos will be the first coin on this platform and offer full baking services for institutional clients. Coinbase Custody has scale to more than 60 clients and $600 million in assets under custody. 

  * [Obsidian Systems updates Kiln to v0.5.0](https://medium.com/@obsidian.systems/bake-with-kiln-a-call-for-beta-testers-d0b65a44e205): Kiln is baking software that enables users to easily setup, run, maintain a baking node with a full-fledged GUI. 

  * [Cryptium Labs introduces its Tezos Protocol proposal for future vote](https://medium.com/cryptium/introducing-the-burebrot-protocol-upgrade-beebf202353a). The Burebrot Protocol upgrade proposal will enable bakers to have more flexibility for their services. 

  * Grants: Tezos Foundation has announced they have funded [Cryptium Labs](https://tezos.foundation/news/cryptium-labs-receives-grant-to-develop-protocol-improvements) and T[ezos Riot forum](https://tezos.foundation/news/tezos-foundation-supports-tezos-riot-forum). 

  * [Crypto Curve](https://twitter.com/Crypto_Curve/status/1111319600904454156) wallet is now fully integrated with Tezos 

  * There is 10 days remaining for the current Tezos proposal in the exploration phase: Follow the voting [here](https://www.tezos.help/votes/).

 **Topper from Quorum Control**

 _Tupelo is a permissionless proof of stake DLT platform purpose-built to
model individual objects that enables flexible public or private data models._

  *  **New release 0.1.1 live**

    * Adds support for **TUPELO_PUBLIC_IP** environment variable which libp2p will broadcast for routing

    * Renames coins to tokens throughout API and codebase

    * Improves reliability through several defect fixes including a race condition in gossip code

  * Initiated transition to Go modules 

  * Read our take on [Why a DLT is often better for Centralized Systems](https://www.quorumcontrol.com/blog/2019/3/28/why-a-dlt-is-still-often-better-for-centralized-systems)

 **Michael from Loom**

 _Loom Network is a platform for building highly scalable DPoS sidechains to
Ethereum, with a focus on large-scale games and social apps._

  * Enabled the ability to sign transactions on PlasmaChain using only your Ethereum wallet, allowing any Ethereum user to seamlessly interact with PlasmaChain: no new wallet to download, no login, no gas.

  * Added in a new governance ability to PlasmaChain which let validators vote to enable new hard forks.

  * Released a [major Zombie Battleground update](https://www.kickstarter.com/projects/328862817/zombie-battleground-the-new-generation-of-ccg-tcg/posts/2465838) (v0.1.15) with a new user interface and updated card art.

  * Published post on [the technicals of setting up an HSM](https://medium.com/loom-network/hsm-policies-and-the-importance-of-validator-security-ec8a4cc1b6f) to ensure validator security, by one of Loom's PlasmaChain validators: <https://stakewith.us/>

  * Published "[How Crypto Is Transforming the Gaming Ecosystem](https://medium.com/loom-network/how-crypto-could-transform-the-gaming-ecosystem-e8bb1323c6ff)," by one of Loom's PlasmaChain validators: <https://chorus.one/>

 **Myles from EOS**

 _EOS is a new blockchain architecture designed to enable vertical and
horizontal scaling of decentralized applications._

  * A production-ready version of the [REX code](https://medium.com/eosio/eosio-contracts-version-1-6-0-9795101c7abd) has been released

  * [Block.one](http://block.one/) released an [analysis](https://medium.com/eosio/analysis-of-bancor-equations-supporting-rex-74ef4aaeca1c) of the Bancor equations used in REX

  * The [eosfinex beta](https://medium.com/eosfinexproject/tutorial-an-eosfinex-walkthrough-893daf82f6d0) exchange went live 

  * dfuse released a [self-serve API solution](https://www.dfuse.io/en/blog/announcing-the-dfuse-self-serve-auth-api-bringing-full-autonomy-to-buidlrs) for developers

 **Zaki from Cosmos**

 _The  Cosmos Network is a decentralized network of independent, scalable, and
interoperable blockchains._

  * [Tendermint 0.31 release](https://github.com/tendermint/tendermint/blob/master/CHANGELOG.md#v0311) focused on reducing excess bandwidth consumption under .load.

  * [V0.34 of the Cosmos SDK](https://github.com/cosmos/cosmos-sdk/projects/31) is nearing release which is planned to be transfers enabled released.

  * The Cosmos governance process continues to work towards initial social norms around [upgrades](https://forum.cosmos.network/t/cosmos-hub-on-chain-governance-proposal-resolution-recommendation/1773) for enabling transfers.

  * [On the IBC front, specification of the relayer algorithm is making progress this week](https://github.com/cosmos/ics/pull/37).

 **Kate and Dean from Agoric**

 _Founded by pioneers in secure development and distributed systems, Agoric
uses a secure subset of JavaScript to enable object capabilities and smart
contracts._

  * Agoric's ["SwingSet" vat platform](https://github.com/Agoric/SwingSet) now supports evaluation of contract code outside of SES, providing a fallback for use in typical standard JS development tools, to preserve line numbers and stack traces. 

  * The shim which implements the proposed Javascript "Realms" API is being moved out of the [TC39 proposal repository](https://github.com/tc39/proposal-realms) into a [dedicated repository](https://github.com/Agoric/realms-shim). The TC39 repo will continue to host the specification text itself.

#### Financial Infrastructure

 **Antonio from dYdX**

 _dYdX is a decentralized exchange for margin trading, borrowing, lending, and
eventually derivatives. dYdX allows traders to trustlessly short and get
leverage on crypto assets._

  * Received final security audit report from Open Zeppelin on our new smart contracts, no critical issues were found. We will release the report when we open source the code in advance of our upcoming product launch

  * Finishing up final features and testing for the alpha launch of our new margin trading product

  * Work trialing one engineering & one design candidate

  * [Hiring](https://boards.greenhouse.io/dydx) software engineers and product designers full-time in SF!

 **Brendan from Dharma**

 _Dharma is the easiest place to borrow and lend cryptocurrencies. It enables
non-custodial peer-to-peer lending through smart contracts on Ethereum._

  * Dharma Protocol hit cumulative 1M USD in transaction volume this past week, the vast majority of that volume coming from the past 6 weeks since the rollout of Dharma Lever.

  * We're hiring full stack developers in SF. No crypto experience necessary. If interested, shoot us an email ([nadav@dharma.io](mailto:nadav@dharma.io) or [brendan@dharma.io](mailto:brendan@dharma.io)) or [apply here](http://email.mg2.substack.com/c/eJwlUMtuhDAM_BpyK8IBNuGQQ7vt_gbKw0C6IUF5dMXfNyskW7Jle8YzWmZcQzzFEVImJWGcrREAcIOBGDEY4CMnNs1LRNyldSLHguQoylktsw3-vT9OPdkE0J4CQ30D0DhOi1KMM6Ymxqnqp4mRN8csi7HoNQr8w3gGj8SJLecjNf1nQx81pF_RtTrU0mwy7vLDSZVq9xtUIlbQDqaup7zjNccW2o5-3eFxHzn_Hn4oQDN0-0rbVFTKUj8r1E6iUBG9kb4OL9TWhuujfB4oPL6Sw5wxknyZUTXO9XIv3uZzRi-VQyOuk6p5oFUXqRwmVF-8OGIIS1heIT7_AW5hckU)

 **Coulter from MakerDAO**

 _Maker is comprised of a decentralized stablecoin, collateral loans, and
community governance._

  * We released a [major update on the status](https://blog.makerdao.com/update-road-to-multi-collateral-dai/) of Multi-Collateral Dai, including a sneak peek of the CDP Portal and more.

  * We [announced](https://medium.com/protea/protea-makerdao-aea74f34b6c) Protea as one of the first grantees of the Community Fund.

  * Coinbase Custody announced [upcoming support](https://blog.coinbase.com/coinbase-custody-launches-staking-support-for-tezos-makerdao-governance-to-follow-68f7bc51bc53) for MKR governance (!) 

  * Ujo Music [integrated Dai](https://media.consensys.net/introducing-streaming-payments-for-ujo-with-connext-payment-channels-and-dai-16725929fe38) into its new feature, Streaming Payments, in order to help support artists.

 **Lazar from MARKET Protocol**

 _MARKET Protocol is a framework for creating tokens that track prices of
traditional or digital assets._

  * We launched our exchange MPX on mainnet! Our whole team is proud of this accomplishment, woot woot!

  * Currently wETH / DAI is available for trading so that our market makers can integrate and begin providing liquidity.

  * This release is a big step towards the mainnet launch of our Position Token minting platform, which is coming soon. We will have more information to share in the coming weeks.

 **Robert from Compound**

 _Compound is a money market protocol on the Ethereum blockchain — allowing
individuals, institutions, and applications to frictionlessly earn interest on
or borrow cryptographic assets without having to negotiate with a counterparty
or peer._

  * No updates this week.

#### Layer two and interoperability

 **Paul from Veil**

 _Veil  is a peer-to-peer prediction market and derivatives platform built on
top of Augur, 0x, and Ethereum._

  * Started auditing user-created markets. Now by default Veil shows audited markets to users. Unaudited and draft markets are still available, but we want to encourage trading in markets that are very unlikely to resolve as invalid on Augur.

  * Launched Instant Settlement via 0x's new MultiAssetProxy, which enables Veil to relay redemptions for multiple tokens at once—like both long tokens and short tokens in a market. This feature is one of the first on Mainnet to use ZEIP-23.

 **Rahul from 0x**

 _0x_  is an open protocol that enables the peer-to-peer exchange of assets on
the Ethereum blockchain.

  * 0x Roadmap Part 3, introducing 0x Mesh, a peer-to-peer communication network that should greatly advance shared liquidity capabilities 

  * Had a successful meetup that will be on our [YouTube channel](https://twitter.com/0xProject/status/1111782512705961984) soon 

  * Check out our new [explore page](https://0x.org/explore) to deep dive into the 0x Ecosystem

 **Tony from Liquidity.Network**

 _Liquidity Network is a transfer and swap platform for any token_

  * Liquidity Network will have a live [AMA](https://www.facebook.com/events/830402530672440/) on 4th April (4pm ICT) at both [Liquidity Network  Telegram group](https://t.me/liquiditynetwork) and [Asia Blockchain Review Telegram group](https://t.me/asiablockchainreview).

 **Dong Mo from Celer**

 _Celer Network is a layer-2 scaling platform that enables fast, easy and
secure off-chain transactions for not only payment transactions, but also
generalized off-chain smart contracts._

  * We've completed CelerX server code and integration with game server. 

  * We implemented more efficient multi-session generalized channel. 

  * We recently open sourced new Celer channel contract and continued planning Q2 milestones. 

  * On our mobile side, we've finished and improved CelerX gaming platform UI design.

  * We refined UI for a new game on CelerX platform. 

  * We keep fixing bugs and improving CelerX stability.

 **Alexandra from Parity Technologies**

 _Parity  Technologies builds core blockchain infrastructure, from Parity
Ethereum, an Ethereum client, to Polkadot, an interoperable blockchain
network._

  * GRANDPA, Polkadot's unique consensus algorithm, is [finalising blocks in ~2 seconds](https://twitter.com/andrebeat/status/1110916051846553600) on the Alexander testnet.

  * All current Serenity state tests are passing for [Parity's Ethereum 2.0 implementation](https://twitter.com/sorpaas/status/1110535361602748417), Shasper.

  * New [Polkadot wiki.](https://wiki.polkadot.network/)

  * Osuke [used Substrate to create a zk-SNARKs chain](https://twitter.com/zoom_zoomzo/status/1110135582657638405)

  * New [Substrate runtime examples.](https://wiki.polkadot.network/en/latest/polkadot/build/examples/)

  * New "People of Parity" interview with [DevOps Engineer, Erin Grismack.](https://twitter.com/ParityTech/status/1111637066943746053)

  * [Validator slots open](https://twitter.com/polkadotnetwork/status/1111609636573061120) on Polkadot's "Alexander" testnet.

  * [Upcoming events](https://twitter.com/ParityTech/status/1110953535804489728) in Wrocław, Seoul, and Buenos Aires. Gavin Wood will also be at [DOT Day in Tokyo](https://twitter.com/polkadotnetwork/status/1111270029465739264). 

  * Recording out of the [sneak peek of the new Zcash client](https://twitter.com/zeroknowledgefm/status/1111641863914749952) we're building with Zcash Foundation.

  * Interested in building on Polkadot? The Web3 Foundation is [providing grants.](https://www.parity.io/jobs/)

  * Like talking to devs and traveling? [We're hiring a Tech Ambassador.](https://twitter.com/ParityTech/status/1101052488344653824)

#### Application infrastructure

 **Doug from Livepeer**

 _Livepeer is a decentralized video infrastructure network, dramatically
reducing prices for developers and businesses building video streaming
applications at scale.  _

  * Beta signups are open for testing out Livepeer's Streamflow transcoding network. The ideal user here is a video developer who works on an application that streams video at scale. [Sign up here](https://livepeer.us16.list-manage.com/subscribe?u=57807e9b74db375864b2c4c68&id=b9626dd647) if you'd like to test the network.

  * The Livepeer Streamflow paper was translated into [Portugese](https://github.com/felipegaucho/wiki-1/blob/master/STREAMFLOW.md), with Chinese and French translations pending.

 **Ryan from FOAM**

 _FOAM  is building spatial applications and proof of location that bring
geospatial data to blockchains and empower a consensus driven map of the
world._

  * Completed work on a custom LoRa radio firmware for time synchronization that can speak to the FOAM blockchain stack with 12 modules, which represents 4 Zone Anchor nodes.

  * Released [version 2.0](https://github.com/f-o-a-m/chanterelle "https://github.com/f-o-a-m/chanterelle") of Chanterelle, with more on the way 

  * Making progress on our ForthState Plasma fork 

  * Challenges are on the rise on the FOAM Map, see recent activity in the [FOAM Daily Digest ](https://us19.campaign-archive.com/home/?u=e88f92fc087c0abfb94d292eb&id=b81a90cf65 "https://us19.campaign-archive.com/home/?u=e88f92fc087c0abfb94d292eb&id=b81a90cf65")

 **David from Sia**

 _Sia is a decentralized cloud storage platform leveraging blockchain
technology to create a data storage marketplace that is more robust and more
affordable than traditional cloud storage providers._

  * The RC4 of the upcoming version 1.4.0 of Sia was released for beta-testing among the Sia #contributors. The bugs for Windows bugs identified during the testing of the RC3 have been corrected, together with some contract formation issues. This is probably the last RC version before the final general release, which is expected to be released this week.

  * 3 different improvements and bug corrections related to stuck uploads, by DavidVorick and ChrisSchinnerl

  * An improvement to the contract formation process: better handling of cases where the host has a locked wallet or insufficient collateral, by lukechampine

  * Better calculation of the `maxcollateral` parameter of hosts, by lukechampine

  * Richer logs during contract formation, by MSevey

  * 2 Nebulous repo were updated. 7 issues were created, 8 were closed. 8 MRs were merged.

  * GitLab users ChrisSchinnerl, MSevey, lukechampine and DavidVorick had code contributions merged into Sia.

#### Other

 **Bowen from Hydro/DDEX.io**

 _Hydro  Protocol is an open source framework for building Decentralized
Exchanges. DDEX is the first decentralized exchange for Ethereum and ERC-20
tokens built on the Hydro Protocol. _

  * Hydro Starter Kit launch 4/2 

  * Hydro Scan online -<https://hydroscan.io/> 

  * Launching US Stock Index Token with MakerDao and UMA   
[https://medium.com/uma-](https://medium.com/uma-project/announcing-us-stock-
index-token-powered-by-uma-and-dai-c394586c575a)project/announcing-us-stock-
index-token-powered-by-uma-and-dai-c394586c575a

 **Sam from OpenBazaar**

 _OpenBazaar is an open source project developing a protocol for e-commerce
transactions in a fully decentralized marketplace._

  * OpenBazaar [version 2.3.2](https://github.com/OpenBazaar/openbazaar-desktop/releases/tag/v2.3.2) has been released. This is a hot fix to address the problem with users running in dual-stack mode. There are a few minor other bugs fixed as well.

  * Minor IPFS changes introduced while we worked on the major recent rebase are now being implemented on the server side.

  * Significant changes are being made to how product discovery works in order to speed them up and decrease the likelihood of getting stale listings; early results show huge speed improvements and we believe they'll be included in the next release.

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

