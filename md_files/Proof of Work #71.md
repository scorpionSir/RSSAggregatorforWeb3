[![](https://substackcdn.com/image/fetch/w_96,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F37b09348-f4f1-47a2-b9e0-a2007299e6e4_256x256)](https://proofofwork.news)

# [Proof of Work](https://proofofwork.news)

SubscribeSign in

Share this post

Proof of Work #71

proofofwork.news

Copy link

Twitter

Facebook

Email

# Proof of Work #71

[Eric Meltzer](https://substack.com/profile/138320-eric-meltzer)

Jun 20, 2019

[Share](javascript:void\(0\))

A quick note about an attack on Bitcoin that’s been observed in the wild
recently. Block witholding attacks have been discussed for a long time—the
term refers to two different things, confusingly, but what we’re discussing
here is when someone (often from a competing pool) joins a mining pool that
pays out based on the average hashrate of the pool but withholds valid blocks,
so the pool misses out on earnings and potentially becomes unprofitable.

Recently, [F2pool](https://bitkan.com/en/news/topic/217913) mentioned on
wechat that it was observable from hashrate distribution that this was
actually happening a lot. Interestingly, there’s been a proposed fix for this
from [Luke Dashjr](https://lists.linuxfoundation.org/pipermail/bitcoin-
dev/2012-June/001506.html) for a _long_ time, but it would require a hard fork
so it hasn’t been implemented yet. While it might not be a massively urgent
problem, I would love to see increasing adoption of things at the pool level
which make Bitcoin more decentralized (like Matt Corrallos
[BetterHash](https://github.com/TheBlueMatt/bips/blob/betterhash/bip-
XXXX.mediawiki)) and I plan to write a bit more about that in the next issue.

More next week!

#### Bitcoin & Friends

 **Jimmy on Bitcoin**

 **[Optech](https://bitcoinops.org/en/newsletters/) on Bitcoin [ed: sign up
for their newsletter too! it’s great!]**

  * Bitcoin Core contributor meetings: many contributors met in person for a periodic [CoreDev.tech](https://coredev.tech/)event last week, with real-time [transcripts](https://diyhpl.us/wiki/transcripts/bitcoin-core-dev-tech/) provided by contributor Bryan Bishop:

  * Presentation: The Next Softfork: Bitcoin Optech contributor Steve Lee gave a presentation during last month’s Optech Executive briefings about possible future Bitcoin soft forks. The [video](https://youtu.be/fDJRy6K_3yo) is now available

 **Tony from Kadena**

 _Kadena is building Pact, a formally verifiable smart-contracting language
for financial applications, and Chainweb, a PoW blockchain that uses multiple
chains in parallel to increase throughput._

  * The Kadena team is working on stability as we look forward to Chainweb Testnet v2 in a couple months.

  * Pact 3.0 was [released](https://www.coindesk.com/kadena-releases-updated-smart-contract-language-for-hybrid-blockchains), the smart contract language with Formal Verification now supports modular governance, SPV and hybrid blockchains.

  * Pact API overhaul for Chainweb [PR 504](https://github.com/kadena-io/pact/pull/504) and [PR 510](https://github.com/kadena-io/pact/pull/510).

  * Pact support for cross-chain multi-step transactions using SPV [PR 246](https://github.com/kadena-io/chainweb-node/pull/246).

  * Released JavaScript pact-lang-api to work with Pact 3.0 [PR 530](https://github.com/kadena-io/pact/pull/530).

  * Chainweb node startup performance improvements [PR 241](https://github.com/kadena-io/chainweb-node/pull/241) and [PR 243](https://github.com/kadena-io/chainweb-node/pull/243).

  * Chainweb improvements to mempool sync logic [PR 234](https://github.com/kadena-io/chainweb-node/pull/234).

  * Ability to send a single transaction to Chainweb for submitting and resolving via an internal listen call [PR 231](https://github.com/kadena-io/chainweb-node/pull/231). 

  * Kadena CEO Will Martino was a guest on a recent episode of the [Crypto and Blockchain Talk](http://cryptoandblockchaintalk.com/enterprise-blockchain-the-consortium-model-explained-by-will-martino-58) podcast to chat about enterprise blockchain.

  * Monica Quaintance explained Chainweb on NEAR Protocol's [Whiteboard Series Episode 19](https://www.youtube.com/watch?v=55EjinSeSMo&feature=youtu.be).

  * Monica Quaintance had a [TV interview with Bloomberg Technology](https://www.youtube.com/watch?v=Zfy6lj818KY&feature=youtu.be)'s Emily Chang to discuss the future of blockchain and cryptocurrency.

 **Aviv from Spacemesh**

 _Spacemesh is a programmable cryptocurrency powered by a novel proof-of-
space-time consensus protocol._

  * Misc Spacemesh App [UI improvements](https://github.com/spacemeshos/smapp/pull/114)

  * Spacemesh App new wallet addresses feature [logic and UI](https://github.com/spacemeshos/smapp/pull/121)

  * Full node - Eligibility oracle but fixes and work on stabilizing and refining mining and p2p tests

  * Community - Spacemesh Epicenter.tv episode aired <https://epicenter.tv/episode/291/>

 **JZ from Decred**

 _Decred  is an autonomous digital currency with a hybrid consensus system. It
is built to be a self-ruling currency where everyone can vote on the rules and
project-level decision making proportionately to their stake._

  * The [Decred bug bounty](https://bounty.decred.org/) program is up for renewal, Degeri has [submitted a new proposal](https://proposals.decred.org/proposals/073694ed82d34b2bfff51e35220e8052ad4060899b23bc25791a9383375cae70) and provided a recap of the last five months. Of the 58 submissions, 9 were eligible for a payout and a total of $3,729 of the $100,000 budgeted for the program was spent.

  * Raedah Group; one of Decred's corporate contractors, has begun the process of [implementing Decred support for Trezor Blockbook](https://github.com/raedahgroup/blockbook). This is the final piece of the puzzle needed to get Decred running on [Trust Wallet as all the client side code](https://github.com/TrustWallet/wallet-core/tree/master/src/Decred) has been completed by the Trust Wallet team.

  * Three big events coming up for Decred. We'll be hosting our first [get together in Beijing on June 20th](https://twitter.com/DecredCN/status/1138739545594220544), as well as being out in force and presenting at [Campus Party in Brazil from June 19 to the 23rd](https://twitter.com/Decred_BR/status/1139323911848570880). Community member Ana Dalia will also be speaking about [Decred at the Blockchain Summit Latam in Mexico City](https://twitter.com/BlockSummitLA/status/1137828122563399681) on July 4-5.

 **Johnny from Stellar**

 _Stellar is an open network for sending and exchanging value of any kind. Its
global network enables digitization of assets - from carbon credits to
currencies - and enables movement around the internet with ease._

  * [Horizon 0.18.0 has been released](https://github.com/stellar/go/releases/tag/horizon-v0.18.0) along with our new [Ticker API 1.0.0](https://github.com/stellar/go/releases/tag/ticker-v1.0.0).

  * [CAP-0021 has moved to FCP: Acceptance](https://github.com/stellar/stellar-protocol/pull/326), along with [CAP-0015 after this PR is merged in](https://github.com/stellar/stellar-protocol/pull/323).

  * The Core Team merged [8 PRs in the last week](https://github.com/stellar/stellar-core/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Aclosed+closed%3A%3E%3D2019-06-07+), and the Platform Team merged 59 PRs in over various repositories (including the Go monorepo, JS SDKs, Java SDKs, and others).

  * The Platform Team found [a major bug in the Go compiler](https://github.com/golang/go/issues/32560).

  * We're now hiring [an integration engineer](https://jobs.lever.co/stellar/0e5a506b-1964-40b4-93ab-31a1ee4e4f90) in addition to [our existing roles on our jobs page](https://jobs.lever.co/stellar).

#### Privacy coins

 **Paige & Zooko from Zcash**

 _Zcash is a  digital currency utilizing zk-SNARKs to enable its privacy-
protecting properties._

  * Product updates, including current priorities  

  * Zcon1 takes place next week in Split, Croatia 

  * Q2 livestream updates available on our YouTube channel 

  * Full details: <https://forum.zcashcommunity.com/t/june-14-2019-weekly-update-community-comms/33778> 

 **Mitchell from Monero**

 _Monero is a open-source, privacy-focused cryptocurrency using the ASIC-
resistant CryptoNote PoW algorithm. It enforces all privacy features at the
protocol level to ensure that all transactions create a single fungible
anonymity pool._

  * CLI v0.14.1.0 has been [released](https://web.getmonero.org/downloads/ "https://web.getmonero.org/downloads/"), now with deterministic builds. GUI coming in the next week or so.

  * [Monero Konferenco](https://monerokon.com/ "https://monerokon.com/") begins this Saturday in Denver, CO with [speakers](https://monerokon.com/schedule "https://monerokon.com/schedule") from around the globe. You can still [register](https://monerokon.com/registration "https://monerokon.com/registration") (and there are some [free tickets for volunteers](https://www.reddit.com/r/Monero/comments/c1paik/one_down_three_free_volunteer_tickets_left/ "https://www.reddit.com/r/Monero/comments/c1paik/one_down_three_free_volunteer_tickets_left/")).

  * All open Community Crowdfunding System proposals (developers, researchers, and outreach) [have been funded](https://ccs.getmonero.org/work-in-progress/ "https://ccs.getmonero.org/work-in-progress/"). Thank you to our anonymous benefactors!

  * [Analysis of Lelantus](https://ccs.getmonero.org/work-in-progress/ "https://ccs.getmonero.org/work-in-progress/") shared, including prototyping code for Monero-to-Lelantus output migration. Reviewing Omniring next.

  * Compressed linkable spontaneously anonymous group (LSAG) signatures are [integrated in a test branch](https://github.com/moneromooo-monero/bitmonero/commit/60dd50e92d349cad765634125ee6d2284bef91bb "https://github.com/moneromooo-monero/bitmonero/commit/60dd50e92d349cad765634125ee6d2284bef91bb").

 **Daniel from Grin**

 _Grin is a community-driven implementation of the Mimblewimble protocol that
aims to be privacy preserving, scalable, fair, and minimal._

  * Merged PRs: [5 in /grin](https://github.com/mimblewimble/grin/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A2019-06-11..2019-06-16+) | [3 in /grin-wallet](https://github.com/mimblewimble/grin-wallet/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A2019-06-11..2019-06-16+) | 3 unique contributors

  * An [iteration of Grin's governance process was proposed](https://www.grin-forum.org/t/proposal-grin-governance-iteration/5191). To be discussed in this week's governance meeting, it's arguably one of the most significant proposals thus far.

  * With less than 30 days left for the scheduled hard fork, v2.0.0 milestones for [node](https://github.com/mimblewimble/grin/milestone/12) and [wallet](https://github.com/mimblewimble/grin-wallet/milestone/2)are almost complete. Beta binaries are due to be released and we are on track to run a private testnet this week.

  * @yeastplume has been [focusing on testing and prep work ahead of the hard fork](https://www.grin-forum.org/t/yeastplume-progress-update-thread-mar-19-to-sep-19/4303/26).

  * [New bulletproof rewind scheme](https://github.com/mimblewimble/grin-wallet/pull/122) by @jaspervdm merged.

  * Paper: [Revelio](https://eprint.iacr.org/2019/684.pdf), a new privacy-preserving proof of reserves protocol for Grin exchanges.

  * Merged PRs: [3 in /grin](https://github.com/mimblewimble/grin/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A2019-06-03..2019-06-10+) | [2 in /grin-wallet](https://github.com/mimblewimble/grin-wallet/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A2019-06-03..2019-06-10+) | 4 unique contributors

  * Grin v1.1.0 has been released, see detailed upgrade information [here](https://www.grin-forum.org/t/upgrade-information-grin-v1-1-0/5147).

  * We have published [tentative timelines and info](https://www.grin-forum.org/t/grin-first-hard-fork-mid-july/5148) on the v2.0.0 hard-fork that is happening in mid-July. Affected parties take note and plan accordingly.

  * The [last governance meeting](https://github.com/mimblewimble/grin-pm/blob/master/notes/20190604-meeting-governance.md) covered the hard fork schedule, Grin budget, a Governance working group, and a contact group for Pools & Exchanges.

  * Following the 1.1.0 release, @yeastplume is [moving forward with 2.0.0 work](https://www.grin-forum.org/t/yeastplume-progress-update-thread-mar-19-to-sep-19/4303/26).

  * @antiochp took a pass at [improving the Dandelion++ implementation](https://github.com/mimblewimble/grin/pull/2876), and also expanded on ideas for a [simplified timer design](https://github.com/mimblewimble/grin/issues/2880).

  * [MMR Storage Optimization](https://github.com/mimblewimble/grin/issues/2873) proposal by @antiochp.

  * Vite announced an [update to their wallet](https://www.grin-forum.org/t/grin-transaction-status-update-on-vite-grin-mobile-wallet/5167?u=lehnberg).

  * More Grin info [here](https://grinnews.substack.com/).

 **Beni from Beam**

 _Beam is a confidential and scalable cryptocurrency based on Mimblewimble._

  * We are happy to offer our European friends the capacity to purchase Beam using Euros, thanks to our integration on Elastum

  * We have launched a unique Web Series on Youtube, [#FocusOnPrivacy](https://www.youtube.com/watch?v=4vHlUBxga_s) where you will discover what Crypto players feel and think about privacy

  * Swaps: Fixed rollback/rescan, added addition test for TX without “change”, changed Beam Lock time for testing

  *  Wrong error in our bridge when LTC user doesn't have enough money to swap [#717](https://github.com/BeamMW/beam/issues/717)

  *  Add a command to get full transaction details [#613](https://github.com/BeamMW/beam/issues/613)

  *  Add the transaction type to transaction history [#614](https://github.com/BeamMW/beam/issues/614)

 **Arnaud from AZTEC Protocol**

 _AZTEC Protocol is an efficient zero-knowledge protocol built on top of
Ethereum, making plug-and-play value transmission and asset governance privacy
tools for developers and companies.  _

  * This week, we are starting work on adding note management to our client side software, to abstract away our UTXO based model from dapp developers.

  * We are also starting work on upgradeable note registries to make it easier to add support for new public token types, and mixer contracts.

  * We’re welcoming [Charlie Cowan](https://www.linkedin.com/in/charlie-cowan-b8257615a/) to the team as a summer intern.

  * In addition to the two cryptographer roles, we are now hiring for a Senior Solidity Engineer and a Senior Engineer. You can apply [here](http://email.mg2.substack.com/c/eJwlUEuOwyAMPU3ZNSKQpGHBoq1mrhHxcVumBEfgTJU5_RBF8sKy_fw-zhA8MW96wUJsLZCn4LVQgg8t87rz7diPLJTpkQFmE6KmvAJbVhuDMxQw7fe9kuylwUnVg3RcXQYu7eDAenvpjOx5Lweh2M4xmdUHSA40_ELeMAGL-kW0lJO8nsR3LZOeEBuHe_tH4M5LRkKH8Szr6AdtYUEL3iouRcs7LjvRtM2NX-_jnY-3QbS37ut66vj8FE1ZbSHj3vXfzLI2OVUBdecy-EBzSNQEPJTRtoBO8CkRiCAzOkKpXqcKntcUaJsgGRvB6wNSvUt1kQOrNB5rPklXsfjAxwfz-x-f0nXk), or by emailing [arnaud@aztecprotocol.com](mailto:arnaud@aztecprotocol.com) with the name of the role as the subject.

#### Smart contracting platforms

 **Evan from[Ethereum](https://weekinethereumnews.com/)**

 _Ethereum  is a decentralized platform for applications that aims to resist
fraud, censorship or third-party interference._

  * [Eth2 spec v0.7](https://github.com/ethereum/eth2.0-specs/releases/tag/v0.7.0) – phase 1 now executable

  * Vitalik: [Universal fee market execution environment to rule them all](https://ethresear.ch/t/one-fee-market-ee-to-rule-them-all/5608)

  * [ethers.js v5 beta](https://blog.ricmoo.com/beta-release-ethers-js-v5-59d0db222d7b)

 **Jing from Plasma**

 _Plasma Group is building "Generalized Plasma", a layer 2 scaling
infrastructure for Ethereum that allows for general state transitions on layer
2._

  * Hosted [Scaling Ethereum](https://www.scalingethereum.org/), a workshop with developers and teams from all over the world coming together to solve outstanding research problems. Focuses on oracles, DEX, layer 1 and layer 2: 

  * Found a solution to history compression in Plasma Cash, utilizing SNARKs

  * Created [a design for a more efficient rollup chain](https://plasma.build/t/rollup-plasma-for-mass-exits-complex-disputes/90) using optimistic execution, allows for any Ethereum smart contract on plasma!! Wowowow

 **Peter from NEAR**

 _NEAR is a sharded proof-of-stake blockchain._

  * 29 PRs across [9 repos](https://github.com/nearprotocol) and 11 authors. Featured repos: [nearcore](https://github.com/nearprotocol/nearcore), [nearlib](https://github.com/nearprotocol/nearlib), [near-shell](https://github.com/nearprotocol/near-shell/), and [near-wallet](https://github.com/nearprotocol/near-wallet) 

  * Added authorized apps management in Wallet with additional UI fixes

  * Setup CI for Nightshade integration in [nearlib](https://github.com/nearprotocol/nearlib)

  * Updated AssemblyScript JSON and bindings

  * Wait properly for compiler loading in Studio

  * Basic end-to-end tests for Studio workflow (running on CI) in operations

  * Added self-call for contract-based account in blockchain layer

  * Major progress on separating large logical blocks into chunks for the new [Nightshade](https://www.youtube.com/watch?v=4CKvfYJTjxk&feature=youtu.be&t=377) sharding design (commits [1](https://github.com/nearprotocol/nearcore/commit/83b7a8827e012c3314bd30886d11da28ea4d7fff) and [2](https://github.com/nearprotocol/nearcore/commit/8da81e68898c2ff848dd5d75c0e8382ec29e1b3f))

 **AJ from Tezos**

 _Tezos is a self-amending blockchain that features formally verified smart
contracts, on-chain governance, and a proof-of-stake consensus algorithm which
enables all token holders to participate in the network.  _

  * [Tezos Foundation announces its new cohort of grantees for advancing the Tezos Ecosystem. ](https://tezos.foundation/news/announcing-first-cohort-of-ecosystem-grants-and-support-for-new-block-explorers-new-rfp-issued)The new grants focus on better development tools and new block explorers. 

  * The co-creator of PricewaterhouseCooper (PWC) Switzerland’s blockchain initative is joining the [Tezos Foundation as the newly appointed CFO and Head of Operations](https://tezos.foundation/news/pwc-blockchain-expert-roman-schnider-joins-tezos-foundation-as-cfo-and-head-of-operations)

  * Nomadic Labs is preparing a proposal for Tezos protocol, called [Emmy+](https://blog.nomadic-labs.com/emmy-an-improved-consensus-algorithm.html), which will focus on improving the consensus algorithm. 

  * [Ligo Lang](http://ligolang.org/): the public beta of Ligo, a smart contract language for Tezos is now live. 

**Topper from Quorum Control**

 _Quorum Control makes Tupelo, a permissionless proof of stake DLT platform
purpose-built to model individual objects that enables flexible public or
private data models._

  * Ongoing Optimization of Production Tupelo TestNets

  * Initial exploration of in-browser transactions (temporarily blocked by uncovered libp2p defect).

  * Moved signer configuration to file-based system making it easier to setup and maintain custom notary groups with their own validation rules.

  * Prototyped moving from BN to BLS12-381 curves for signatures but the performance was too severely compromised in the library’s current state.

  * NFT series complete please check out any you missed: [Part 1](https://www.quorumcontrol.com/blog/2019/5/17/a-taxonomy-of-nfts-collectibles-and-assets-and-digital-twins-oh-my), [Part 2](https://www.quorumcontrol.com/blog/2019/5/23/part-2-digital-scarcity-am-i-original-am-i-the-only-one), [Part 3](https://www.quorumcontrol.com/blog/digitaltwin). 

**Michael from Loom**

 _Loom Network is a platform for building highly scalable DPoS sidechains to
Ethereum, with a focus on large-scale games and social apps._

  * Released [developer tutorial](https://twitter.com/loomnetwork/status/1138830641779433474) covering how to sign Layer 2 transactions on PlasmaChain directly from native Ethereum wallets

  * [Announced Loom Wallet](https://twitter.com/loomnetwork/status/1138845957989253122), which will allow users to display Loom PlasmaChain assets, send/receive transactions, deposit/withdraw to Ethereum + major chains (soon), and sign in with MetaMask

  * Over 213M tokens have been staked on Loom, which amounts to ~27% of circulating supply

 **Myles from EOS**

 _EOS is a new blockchain architecture designed to enable vertical and
horizontal scaling of decentralized applications._

  * [Decentium](https://decentium.org/decentiumcrw/introducing-d) — a censorship-resistant Medium alternative (with a very slick UI) launched on EOS

  * EOS NY [responds](https://decentium.org/eosnewyorkio/you-cannot-fa) to reports of widespread "bot" activity on EOS 

  * Blockchain gaming company Upland [raises](https://medium.com/@upland/introducing-upland-the-virtual-property-game-built-on-eos-f68e61adb406) money from EOS VC

 **Zaki from Cosmos**

 _The  Cosmos Network is a decentralized network of independent, scalable, and
interoperable blockchains._

  * The DGaming Foundation open sourced a modified Cosmos SDK with a [secure random beacon](https://github.com/dgamingfoundation/tendermint/blob/dcr-random/docs/arcade/arcade.md).

  * The Folks at Lunie HQ opensourced a number of [Javascript client libraries ](https://twitter.com/luniehq/status/1139882460244795392)for the Cosmos SDK.

  * [HackAtom Berlin](https://twitter.com/cosmos/status/1140348949116723200) was insanely successful producing prototype code for WASM in the CosmosSDK, several IBC application prototypes, transferable staking rewards.

  * The Interchain Foundation released a Request for Proposals for the [Q3 grants program](https://medium.com/@interchain_io/request-for-proposals-2019-expanding-environments-93c0f51ec9a1).

 **Kate and Dean from Agoric**

 _Founded by pioneers in secure development and distributed systems, Agoric
uses a secure subset of JavaScript to enable object capabilities and smart
contracts._

  * We had a blast working with Cosmos this week in Berlin at the Interchain Conversations conference and their hackathon. Two Agoric-related entries won at the hackathon:

    * Aaron Davis (kumavis) of MetaMask has created a [plugin for browserify using Agoric’s SES](https://github.com/MetaMask/sesify) that reduces the risk of using third-party packages. At the hackathon, he additionally built a visualizer for JavaScript package dependencies that colors each module node based on the level of security exposure. 

    * We demoed our integration with Cosmos, running “Swingset” on a cosmos chain. In order to show our full stack, we built a simple pixel marketplace (think Million Dollar Homepage or Reddit’s /r/Place) that uses our Electronic Rights Protocol and provides the ability to color, buy, and sell pixels as well as create further abstractions. 

#### Financial Infrastructure

 **Coulter from MakerDAO**

 _Maker is comprised of a decentralized stablecoin, collateral loans, and
community governance._

  * Learn Dai. Earn Dai. Coinbase has launched the [Dai Earn campaign](https://blog.coinbase.com/earn-dai-while-learning-about-the-stablecoin-and-how-its-generated-b1137486d06f). Simply watch the lessons, answer a quick quiz, and the Dai is yours! 

  * Dai continues to find its way into gaming. We [partnered with Axie Infinity](https://blog.makerdao.com/game-on-maker-and-axie-infinity-partner-receive-dai-themed-nfts-for-opening-cdps/), one of the biggest blockchain games, on an integration for unique Dai-themed NFTs for those who have opened CDPs. We're also contributing Dai to the top Axie players. 

  * A VERY deep dive into [why people are using Dai](https://blog.makerdao.com/understanding-the-dai-user-insights-into-adoption/) and how it affects UX -- Great read of (and for!) organizations choosing to integrate Dai.

 **Lazar from MARKET Protocol**

 _MARKET Protocol is a framework for creating tokens that track prices of
traditional or digital assets._

  * Last week we announced the [upcoming launch](https://medium.com/market-protocol/mpx-mainnet-ahead-2881b915d334) of our platform [MPX](https://mpexchange.io/). Early access is available now prior to market makers onboarding before launch

  * We published Part 1 of our MPExplained educational series: [Pricing Position Tokens](https://medium.com/market-protocol/position-tokens-pricing-on-mpx-explained-7b2d2ddb556f). Check it out to learn more about our first product, BTC/DAI

 **Robert from Compound**

 _Compound is a money market protocol on the Ethereum blockchain — allowing
individuals, institutions, and applications to frictionlessly earn interest on
or borrow cryptographic assets without having to negotiate with a counterparty
or peer._

  * Launched a [Market Overview](https://compound.finance/markets), with detailed transparency into the protocol

  * Hired two software engineers

#### Layer two and interoperability

 **Tony from Liquidity.Network**

 _Liquidity Network is a transfer and swap platform for any token_

  * Liquidity Network has the honor to sponsor the [1st International Summer School on Security & Privacy for Blockchains and Distributed Ledger Technologies](https://bdlt.school/), hosted by TU Wien in Vienna – Austria from 2 to 6 September 2019.

  * Liquidity team is excited to announce the [results](https://blog.liquidity.network/2019/06/14/canvascompetiton-2-0-winner-announcement/) of #CanvasCompetition 2.0! Thank you to all participants and congratulations to the winners

 **Dong Mo from Celer**

 _Celer Network is a layer-2 scaling platform that enables fast, easy and
secure off-chain transactions for not only payment transactions, but also
generalized off-chain smart contracts._

  * We finished wired up sign-up flow, invite flow and reward flow.

  * We refined CelerX APIs for game developers. 

  * We reinforced multi-token support.

  * We finished new functionality for upcoming mainnet release.

  * We finished code fixes, structural improvements, and improved error handling. 

  * We are continuing to work on channel contract upgradability and begin the migration of system set up to Kubernetes.

 **Alexandra from Parity Technologies**

 _Parity  Technologies builds core blockchain infrastructure, from Parity
Ethereum, an Ethereum client, to Polkadot, an interoperable blockchain
network._

  * [We released Zebra](https://www.parity.io/parity-releases-zebra-in-collaboration-with-zcash-foundation/), the first alternative Zcash client, with the Zcash Foundation.

  * Shiny new [Substrate developer hub.](https://substrate.dev/)

  * We introduced [Lightbeam](https://www.parity.io/lightbeam-webassembly-compiler/), our Optimising Streamling WebAssembly Compiler, intended for our Substrate smart contract subsystem.

  * New [Parity Ethereum release.](https://twitter.com/ParityTech/status/1138829312059170816)ps://[titter.com/ParityTech/status/1138829312059170816](http://titter.com/ParityTech/status/1138829312059170816)

  * Jutta Steiner [joined as a guardian at Matrix Foundation.](https://twitter.com/jutta_steiner/status/1138815580184731650)

  * New [Polkadot Ambassador program.](https://medium.com/polkadot-network/announcing-the-launch-of-the-polkadot-ambassador-program-ba381808ca70) 

  * [Join us at Web3 Summit this August!](https://web3summit.com/speakers/)

  * Web3 Foundation is [providing grants to build the Web3 ecosystem](https://github.com/w3f/Web3-collaboration/blob/master/grants/grants.md). 

  * [We're hiring!](https://www.parity.io/jobs/) New opening: [Content Marketer.](https://www.parity.io/jobs/#berlin-content-marketer)

#### Application infrastructure

 **Doug from Livepeer**

 _Livepeer is a decentralized video infrastructure network, dramatically
reducing prices for developers and businesses building video streaming
applications at scale.  _

  * Livepeer Inc, one of the companies that builds software and product on the Livepeer network, [closed an $8,000,000 Series A round of financing](https://techcrunch.com/2019/06/17/decentralized-video-infrastructure-platform-livepeer-raises-8m-series-a/). 

  * Epic Labs published their [latest research findings](https://medium.com/@epiclabs.io/assessing-metrics-for-video-quality-verification-in-livepeers-ecosystem-iii-744ba1c1d5d7?sk=4b5376e9d147b8d0ba8174aaad0c6a96) on video quality assessment within the Livepeer network. 

 **Matt from Keep Network**

 _The Keep Network is a privacy layer for public chains, enabling
interactivity with private data and interoperability across chains. It does
this with keeps, off-chain containers for private data that help smart
contracts harness the full power of the public blockchain._

  * Major stakers have been invited to begin testing on our private testnet

  * Stake delegation is done!

  * We’ve made progress on state management (woohoo, groups survive client restarts!)

  * Merged RFC specifying contract upgrade schemes

  * Implemented a network node bootstrap mechanism

  * Implemented support for concurrently running relay requests

  * Keep’s Ecosystem Growth & Innovation Lead Jarrell James joined a privacy in a [blockchain panel](https://twitter.com/MicheleDaliessi/status/1138025638122741762/photo/1) at CogX in London

  * For more updates join our [Slack](https://keep-network.slack.com/) and check out the [Keep blog](https://blog.keep.network/)

 **David from Sia**

 _Sia is a decentralized cloud storage platform leveraging blockchain
technology to create a data storage marketplace that is more robust and more
affordable than traditional cloud storage providers._

  * Release candidate 1 of Sia version 1.4.1 was publicly released for testing. This release introduces seed-based file recovery, several new API endpoints, changes in many siac commands, significant scaling improvements, and many bug fixes

  * As mentioned last week, community member Danger and Sia Core Developer Nemo created a proof of concept mobile app for Sia that allows a user to upload and download files from the Sia network without syncing the blockchain. [Read more](https://www.reddit.com/r/siacoin/comments/bztaox/a_new_chapter_in_sia_mobile_app_development/​).

  * Sia based product, Filebase, wrote an excellent tutorial on using Filebase with Arq.  Read more about it [here](https://medium.com/filebase/encrypted-backups-on-sia-using-filebase-and-arq-9e409e06aff8​) 

  * Sia based product, Goobox, wrote an excellent tutorial on using Goobox as a mounted disk and file sharing.  Read more about it [here](https://medium.com/@goobox/mount-goobox-as-a-disk-share-files-ea2ee923c242​) 

  * Community member tbenz9 released a 2nd public beta for Siasync.  Read more about the changes [here](https://www.reddit.com/r/siacoin/comments/c12noi/siasync_v100beta2_released/​) 

  * The Sia network continues to grow, passing 360 TB this week.

#### Other

 **Bowen from Hydro/DDEX.io**

 _Hydro  Protocol is an open source framework for building Decentralized
Exchanges. DDEX is the first decentralized exchange for Ethereum and ERC-20
tokens built on the Hydro Protocol. _

  * Hydro Wallet SDK update - Ledger <https://github.com/HydroProtocol/hydro-sdk-wallets>

  * Adding Compund Ctoken

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

