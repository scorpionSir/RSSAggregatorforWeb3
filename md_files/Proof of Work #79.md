[![](https://substackcdn.com/image/fetch/w_96,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F37b09348-f4f1-47a2-b9e0-a2007299e6e4_256x256)](https://proofofwork.news)

# [Proof of Work](https://proofofwork.news)

SubscribeSign in

Share this post

Proof of Work #79

proofofwork.news

Copy link

Twitter

Facebook

Email

# Proof of Work #79

[Eric Meltzer](https://substack.com/profile/138320-eric-meltzer)

Nov 18, 2019

[Share](javascript:void\(0\))

Hi from Boston, and welcome to a double-edition of PoW.

I’ve been playing around with a lot of apps recently and I wanted to highlight
a few of the particularly compelling ones:

  1. [Mixin Messenger](https://mixin.one/messenger). My partner invested in this last year and I never get around to playing with it. The app is quite popular in China—it’s an encrypted messaging app that uses the Signal protocol for end to end encryption, and has a crypto wallet that lets you do things like send red envelopes to friends and do easy p2p transfers. The crypto functionality is built on a federated semi-custodial multisig solution that I frankly don’t quite understand yet (the code is all on [Github](https://github.com/MixinNetwork/mixin/issues) but I haven’t finished reading through it) but so far I’ve only used it for small amounts of coin and to play around. The toy bots people have built for this are pretty impressive—there’s a Bitcoin faucet bot that gives you 100 satoshis the first time you hit it, and increases the amount by 100 each time you remember to ping the bot, a dice bot that replicates the old SatoshiDice functionality, and a lightning-based instant exchange bot that allows you to swap between any of the coins the messenger supports (most of the top twenty). I’m going to revisit this one in a later newsletter once I have a better understanding of how the underlying distributed multisig part works so that I have a better feel for how secure this is.

  2. Coinbase’s new Tezos staking flow in the [app](https://www.coinbase.com/mobile). Coinbase hired a bunch of good designers over the past year or so and it clearly paid off. This is honestly one of the best experiences in crypto (the realtime count-up is so cool). 

  3. The [Ironbelly](https://ironbelly.app/) Grin Wallet. Sending Grin is still kind of a hassle because of the interactivity thing but playing with this is just.. fun. I can’t explain it, but I really like it and so does everyone I’ve sent this to. 

#### Bitcoin & Friends

 **Eric on Bitcoin**

  * Mike Dubrovsky of PowX dropped a “[litepaper](https://twitter.com/MikeDubrovsky/status/1190058462002241538?s=20)” (why didn’t they call it a light paper, missed dadjoke opportunity) about a new optical Proof of Work. The aim here is to move the needle way over to the CapEx side of the dial from the current mostly-OpEx situation. This would make cost of electricity less relevant, and potentially lead to more geographically decentralized mining. Lots of potential issues, but super interesting. I’ve put this under the Bitcoin header because the ultimate aim is to integrate it into BTC; whether this is at all likely is unclear at the moment. 

**[Optech](https://bitcoinops.org/en/newsletters/) on Bitcoin [ed: sign up for
their newsletter too! it’s great!]**

  *  **Upgrade to C-Lightning 0.7.3:**  this latest [release](https://github.com/ElementsProject/lightning/releases/tag/v0.7.3) adds support for a PostgreSQL backend, makes it possible to send funds directly to a particular address when closing a channel, and allows you keep your HD wallet seed encrypted when `lightningd` isn’t running

  * Experienced users are encouraged to help test the latest release candidates for the upcoming version of [Bitcoin Core](https://bitcoincore.org/bin/bitcoin-core-0.19.0/).

 **Tony from Kadena**

 _Kadena is building Pact, a formally verifiable smart-contracting language
for financial applications, and Chainweb, a PoW blockchain that uses multiple
chains in parallel to increase throughput._

  * Mining of Kadena's public blockchain is now live! Thank you for the response from the mining community (we notified our opt-in miner email list towards the end of last week). At the time of this update, there have been over 150,000 blocks mined. For context, it took Ethereum 28 days to cross the same milestone. We see this as validation of our approach to scaling Proof of Work using parallel chains. Given that we are currently only available for CPU mining (we anticipate GPU mining to open in about a week), we're working hard to encourage and support adoption. We look forward to the full launch of our hybrid blockchain platform in December!

  * Since we've opened up mining, we've quickly seen the hash rate go from 20 MH/second to between 4-5 GH/second. We're already seeing over 5000 CPUs solving blocks on mainnet. Watch mainnet mining at <https://explorer.chainweb.com/mainnet>.

  * Formally verified multi-step escrow transactions [PR 565](https://github.com/kadena-io/pact/pull/565).

  * The Pact smart contract language now has explicit module imports [PR 585](https://github.com/kadena-io/pact/pull/585).

  * SPV and cross-chain transfer infrastructure [PR 429](https://github.com/kadena-io/chainweb-node/pull/429), [PR 452](https://github.com/kadena-io/chainweb-node/pull/452) and [PR 456](https://github.com/kadena-io/chainweb-node/pull/456).

  * Gas model using data-driven analysis [PR 640](https://github.com/kadena-io/pact/pull/640).

  * Anastasia Bez, Will Martino, and Monica Quaintance published [Kadena's token economics model](https://medium.com/kadena-io/the-kadena-token-economic-model-8090d7545eef).

  * Tony Pham [spoke to Cointelegraph](https://cointelegraph.com/news/crypto-firms-join-azure-as-microsoft-fights-amazon-for-market-share) about Kadena's enterprise-grade solutions on Azure Marketplace.

  * Kadenamint, the implementation of Pact on Tendermint, was featured in a blog post by the Interchain Foundation about "[Virtual Machines Take Off in the Cosmos](https://medium.com/@interchain_io/virtual-machines-take-off-in-the-cosmos-3d11bd6ae942)."

  * Monica gave a presentation on "[Kadenamint, Cosmos and Pact](https://www.blockchaing.org/home/2019/10/29/san-francisco-blockchain-week-2019-cesc-day-2): Universal Smart Contracts" at CESC/San Francisco Blockchain Week.

  * Monica appeared on [Bloomberg Technology](https://youtu.be/Z-2G3sPxSgc) to discuss blockchain developments and [Kadena's token sale on CoinList](https://coinlist.co/kadena).

 **Aviv from Spacemesh**

 _Spacemesh is a programmable cryptocurrency powered by a novel proof-of-
space-time consensus protocol._

  * We launched the Spacemesh Ambassadors Program - [sign up here](https://spacemesh.io/ambassador/)

  * We created a Spacemesh Protocol Overview to further explain what powers Spacemesh under the hood. [Check it out](https://spacemesh.io/overview)

  * For the Spacemesh App, we continued work on auto-update and retrieving TX statuses. - [closed issues in smapp repo.](https://github.com/spacemeshos/smapp/issues?q=is%3Aissue+is%3Aclosed)

  * For the Go-Spacemesh Smesher, we continued to work towards our open Testnet. We revised some of the PoET APIs, added VRF validation to Hare messages and refactored our logging Infra to support different log levels. [Merged issues](https://github.com/spacemeshos/go-spacemesh/pulls?q=is%3Apr+is%3Aclosed)

  * For the Spacemesh Virtual Machine (SVM), we added gas-metering for a restricted set of wasm. [Issues defined here](https://github.com/spacemeshos/svm/tree/gas-metering)

  * Spacemesh Co-founder Tomer Afek's article has been published by Cointelegraph Spain. [Cómo la tecnología Blockchain y las criptomonedas están preparadas para cambiar el balance de poder en el mundo](https://es.cointelegraph.com/news/how-blockchain-and-crypto-are-poised-to-shift-the-balance-of-power)

  * Are you passionate about the next iteration of blockchain technology? Sign up to be a [Spacemesh Ambassador](https://spacemesh.io/ambassador/) today.

  * Spacemesh App: we are continuing to work hard on TX statuses and auto-update functionality for Mac and Windows. [closed issues in smapp repo.](https://github.com/spacemeshos/smapp/issues?q=is%3Aissue+is%3Aclosed)

  * Spacemesh Smesher: we are refining APIs for integration of the node binary with the Spacemesh App UI, and running functional testing on the Testnet infrastructure, defining gaps. [Merged issues](https://github.com/spacemeshos/go-spacemesh/pulls?q=is%3Apr+is%3Aclosed)

  * For our smart contracts initiative, the Spacemesh Virtual Machine (SVM), we are rewriting the gas-estimation algorithm to be of linear complexity. We’ve also released a couple of SVM issues to [Gitcoin](https://gitcoin.co/spacemeshos)

  * More info on[ our site.](http://spacemesh.io/)

 **Izaak from Coda**

 _Coda is the first cryptocurrency protocol with a constant-sized blockchain.
Coda compresses the entire blockchain into a tiny snapshot the size of a few
tweets using recursive zk-SNARKs._

  * John has been developing the [archive node](https://github.com/CodaProtocol/coda/pull/3875), for those who want to store the entire history of Coda.

  * Michelle has been working on implementing the [delegation and staking flows](https://github.com/CodaProtocol/coda/pull/3864/files) in the desktop wallet.

  * Echo [fixed a bug](https://github.com/CodaProtocol/coda/pull/3881) which we saw on our last testnet that caused nodes to crash if they connected to a peer that they had "banned" for misbehavior.

#### Privacy coins

 **Elena & Zooko from Zcash**

 _Zcash is a  digital currency utilizing zk-SNARKs to enable its privacy-
protecting properties._

  * The next DevFund Protocol Hangout is 11/6. The discussion will be hosted by Sonya and you can sign up [here](https://forum.zcashcommunity.com/t/wednesday-11-6-zcash-protocol-hangout-dev-fund-edition-2/35144).

  * The ECC live stream has been rescheduled for 11/12 at 10:30 am MST. Hear from company leadership about the dev fund, goals for the coming year, product flight plan and more.

  * [Zecwallet-Lite UI beta 1 is here](https://forum.zcashcommunity.com/t/zecwallet-lite-ui-beta1/35267). Please take some time to try out the wallet and send us feedback.

  * Don’t miss the [Cypherpunk Privacy Reading List](https://www.zfnd.org/blog/cypherpunk-privacy-reading-list/) put out by Zcash Foundation.

  * [ECC transferred ownership of the Zcash trademark](https://electriccoin.co/blog/electric-coin-co-donates-zcash-trademark-to-zcash-foundation/) to the Zcash Foundation. Zcash Foundation shared an [updated timeline ](https://www.zfnd.org/blog/updated-community-sentiment-timeline/)for DevFund proposals. If you missed the Protocol hangout, check out the recording in Zcash Foundation’s weekly [newsletter](https://news.zfnd.org/archive/zcash-governance-and-ecosystem-updates-zcash/).

  * The ECC quarterly live stream is on  **Tuesday 11/12 at 10:30 am MST**. Hear from company leadership about the dev fund, goals for the coming year, product flight plan and more.

  * Make sure to check out our [blog](https://electriccoin.co/blog/) for the latest releases. [Release 2.1.0 ](https://electriccoin.co/blog/new-release-2-1-0/)set the mainnet activation of the Blossom network upgrade to an activation height of 653600, which should occur in early December. [Release 2.1.0.1 ](https://electriccoin.co/blog/new-release-2-1-0-1/)fixes a security issue that we were made aware of this morning. We recommend reading the blog and downloading the updated releases.

  * ECC continued work on updating <https://explorer.testnet.z.cash/>, <https://explorer.z.cash/>, and <https://faucet.testnet.z.cash/>

  * We’ve added functionality to the iOS SDK so that developers are able to download and trial decrypt blocks in order to find transactions that pertain the the wallet; specifically, we implemented: download blocks, validate blocks, scan blocks, and a block progress indicator.

  * While iOS is getting up to parity with Android, Android has been refining its code, exploring future-compatibility for next network upgrades, merged in security fixes (<https://github.com/zcash/librustzcash/issues/120>, <https://github.com/zcash/zcash-android-wallet-sdk/issues/30>), and merged a threat model for the android SDK.

  * Full Zcash updates are available [here](https://forum.zcashcommunity.com/c/weekly-updates).

 **Daniel from Grin**

 _Grin is a community-driven implementation of the Mimblewimble protocol that
aims to be privacy preserving, scalable, fair, and minimal._

  * Merged PRs: [7 in /grin](https://github.com/mimblewimble/grin/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A2019-10-28..2019-11-03+) | [1 in /grin-wallet](https://github.com/mimblewimble/grin-wallet/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A2019-10-28..2019-11-03+) | 5 unique contributors

  * Added [support for Homebrew](https://github.com/Homebrew/homebrew-core/pull/45833). Node and wallet can now be installed on the Mac by running `brew install grin grin-wallet`.

  * Freezed scope ahead of the [v3.0.0 hard-fork](https://github.com/mimblewimble/grin-pm/issues/204) in Jan 2020.

  * New RFC proposal: [Enabling faster sync](https://github.com/mimblewimble/grin-rfcs/pull/29).

  * New RFC proposal: [Wallet Update Process Enhancements](https://github.com/mimblewimble/grin-rfcs/pull/30).

  * In the last [development meeting](https://github.com/mimblewimble/grin-pm/blob/master/notes/20191029-meeting-development.md) v3.0.0 was scoped and a v2.1.1 patch of the node agreed.

  * Program for grincon1 [was announced](https://www.grin-forum.org/t/grincon1-tentative-program-schedule/6384/). November 22 at c-base in Berlin. [Sign up for free](https://grincon.org/) and see you there!

  * Last chance to make suggestions towards the [Grin 2020 roadmap](https://www.grin-forum.org/t/grin2020-roadmap-calling-for-blog-posts-with-ideas/6327/3).

  * Merged PRs: [1 in /grin](https://github.com/mimblewimble/grin/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A2019-11-04..2019-11-10+) | [2 in /grin-wallet](https://github.com/mimblewimble/grin-wallet/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A2019-11-04..2019-11-10+) | 1 unique contributor

  * Thank you to the anonymous donor who [donated another Bitcoin Coinbase reward from 2010 to Grin's General Fund](https://www.grin-forum.org/t/donation-to-the-grin-general-fund-nov-11/6446). We're humbled by the show of support and will do our utmost to spend the funds wisely.

  * New RFC proposal: [Payment Proofs](https://github.com/mimblewimble/grin-rfcs/pull/31).

  * Yeastplume has been busy [working on improvements to transaction and wallet state management](https://www.grin-forum.org/t/yeastplume-progress-update-thread-oct-to-dec-19/6211/6).

  * In the last [governance meeting](https://github.com/mimblewimble/grin-pm/blob/master/notes/20191105-meeting-governance.md) website onboarding improvements, assignment of RFC shepherds, and a review of open research problems were covered.

  * [grincon1](https://grincon.org/) is less than ten days away. GRIN ANNUAL DEVELOPMENT CONFERENCE. November 22. c-base raumstation. Berlin. Join us, attendance is open and free. ツ

  * Grin is 100% funded by donations. Please support Grin development - [Donate now](https://grin-tech.org/general_funding).

  * More Grin info [here](https://grinnews.substack.com/).

 **Arnaud from AZTEC Protocol**

 _AZTEC Protocol is an efficient zero-knowledge protocol built on top of
Ethereum, making plug-and-play value transmission and asset governance privacy
tools for developers and companies.  _

  * After 10 days of continuous computation for Ignition (our MPC ceremony) >60 participants from >18 countries have successfully added entropy. The ceremony is on track to hit over 200 participants over the next month. Watch live on [https://ignition.aztecprotocol.com](https://ignition.aztecprotocol.com/)

  * We have been working on better testing for [Barretenberg](https://github.com/AztecProtocol/barretenberg), our ECC library. We’ve added a more thorough build pipeline and building and testing on several architectures and OSs.

  * We’re continuing work on final deploy tests and integration tests for our mainnet protocol, preparing for our launch later this year.

#### Smart contracting platforms

 **Peter from NEAR**

 _NEAR is a sharded proof-of-stake blockchain._

  * 77 PRs across 26 repos by 20 authors. Featured repos:[ nearcore](https://github.com/nearprotocol/near-wallet),[ nearlib](https://github.com/nearprotocol/nearlib),[ near-shell](https://github.com/nearprotocol/near-shell/),[ near-wallet](https://github.com/nearprotocol/near-wallet),[ near-bindgen](https://github.com/nearprotocol/near-bindgen), [near-fiddle-api](https://github.com/nearprotocol/near-fiddle-api), [NEARStudio](https://github.com/nearprotocol/NEARStudio/), [assemblyscript](https://github.com/nearprotocol/assemblyscript), [borsh](https://github.com/nearprotocol/borsh), [create-near-app](https://github.com/nearprotocol/create-near-app), [stakewars](https://github.com/nearprotocol/stakewars) and [near-explorer](https://github.com/nearprotocol/near-explorer/);

  * Check out [Alex live coding](https://www.twitch.tv/nearprotocol/videos) core features of the NEAR Protocol

    * A massive [refactoring of Nightshade](https://github.com/nearprotocol/nearcore/commits/refactor_nightshade) that significantly reduces the number of messages exchanged and also addresses issues with chunk producers going offline.

    * [Finality gadget](https://github.com/nearprotocol/nearcore/commits/nfg2) routine that computes the last finalized block and implementation of the fork choice rule that respects the finality gadget.

  * [The second part](https://youtu.be/QhQi2nAd-r0) of the whiteboard lunch series is live

  * [Adding genesis tools for stakewars into dockerfile](https://github.com/nearprotocol/nearcore/pull/1567) in nearcore

  * [Speeding up / less network for block sync](https://github.com/nearprotocol/nearcore/pull/1555) in nearcore

  * [Cleanup and usability improvements](https://github.com/nearprotocol/near-bindgen/pull/39) in near-bindgen

  * [Seed phrase recovery support](https://github.com/nearprotocol/near-wallet/pull/167) in near-wallet

  * [Implemented multinet support](https://github.com/nearprotocol/near-explorer/pull/119) in near-explorer

  * [Added a cross-contract call example](https://github.com/nearprotocol/nomicon/pull/4) in nomicon

  * 93 PRs across 21 repos by 22 authors. Featured repos:[ nearcore](https://github.com/nearprotocol/near-wallet),[ nearlib](https://github.com/nearprotocol/nearlib),[ near-shell](https://github.com/nearprotocol/near-shell/),[ near-wallet](https://github.com/nearprotocol/near-wallet),[ near-bindgen](https://github.com/nearprotocol/near-bindgen), [assemblyscript-json](https://github.com/nearprotocol/assemblyscript-json), [nomicon](https://github.com/nearprotocol/nomicon), [near-contract-helper](https://github.com/nearprotocol/near-contract-helper), [borsh](https://github.com/nearprotocol/borsh), [stakewars](https://github.com/nearprotocol/stakewars) and [near-explorer](https://github.com/nearprotocol/near-explorer/);

  * [Fixing chunks retrieval for non-validators](https://github.com/nearprotocol/nearcore/pull/1660) in nearcore

  * [Merklization of execution outcomes](https://github.com/nearprotocol/nearcore/commit/7214e61418bf2c26f7096c3765afc93889d2b538) in nearcore

  * A three part PR ([1](https://github.com/nearprotocol/nearcore/pull/1591), [2](https://github.com/nearprotocol/nearcore/pull/1645) and [3](https://github.com/nearprotocol/nearcore/pull/1657)) improving transaction pool and implementing delaying receipts to prevent spamming shards in nearcore

  * Major overhaul of [networking code](https://github.com/nearprotocol/nearcore/commit/935c7e05496b4c214b7b5d6b7aa6822a69270e43) in nearcore

  * [Chart that shows growth of contracts deployed](https://github.com/nearprotocol/near-explorer/issues/121) in near-explorer

  * NEP outlining the details of the [Proposed implementation of the randomness beacon](https://github.com/nearprotocol/NEPs/pull/22)

  * [near-shell 0.14.1 published ](https://github.com/nearprotocol/near-shell/releases/tag/v0.14.1)

  * [Node & Staking and visual changes](https://github.com/nearprotocol/near-wallet/pull/149) in near-wallet

 **AJ from Tezos**

 _Tezos is a self-amending blockchain that features formally verified smart
contracts, on-chain governance, and a proof-of-stake consensus algorithm which
enables all token holders to participate in the network.  _

  * [tZERO Partners with Alliance Investments to Tokenize River Plaza on Tezos Blockchain](https://www.businesswire.com/news/home/20191030005153/en/tZERO-Partners-Alliance-Investments-Tokenize-River-Plaza), a Luxury Real Estate Development in Manchester, UK

  * [Tezos Foundation Strengthens Support For Tezos Block Explorers And App Accessibility](https://tezos.foundation/news/tezos-foundation-strengthens-support-for-tezos-block-explorers-and-app-accessibility)

  * [Tezos Commons is hosting 10 meetups](https://medium.com/tezoscommons/tezos-community-events-november-bd7267c175ea) across the globe for November. 

  * [StakerDAO Launches Platform for Governing Financial Assets ](https://www.businesswire.com/news/home/20191030005296/en/StakerDAO-Launches-Platform-Governing-Financial-Assets-Secure)in a Secure, Decentralized, and Compliant Manner.

  * [A Digital Collectible Card Game is Coming Soon to Tezos](https://medium.com/tezoscommons/a-digital-collectible-card-game-coming-soon-to-tezos-ddd939f3b119)

 **Topper from Quorum Control**

 _Quorum Control makes Tupelo, a permissionless proof of stake DLT platform
purpose-built to model individual objects that enables flexible public or
private data models._

  * The team is finalizing a significant Tupelo core update to enable Tupelo developers to specify “conditions” as part of the transactions they submit.  These take the form of lisp like logical conditionals and will allow a range of new functions to be described in greater detail upon release.

  * Architecture and implementation planning for new HAMT based batched transaction consensus algorithm.  This change will provide significantly higher transaction throughput ([currently at 250 tx/sec for 21 signers](https://docs.tupelo.org/platform_performance.html)) under load while still maintaining very low latency.

  * We are hiring for [Developer Evangelist and Platform Engineer](https://www.tupelo.org/careers) positions. Submit resumes to [info@quorumcontrol.com](mailto:info@quorumcontrol.com).

 **Andrew from Solana**

 _Solana is a scalable blockchain that utilizes proof of history to verify the
ordering and passage of time between events. It consists of a network of 200
physically distinct nodes which support a sustained throughput of more than
50,000 TPS.  _

  * Last week was a big week for our engineering team. We released solana.0.20 and fixed some of the bugs that was keeping our TPS down.  Check the Github.<https://github.com/solana-labs>

  * Tour del SOL is racing. TdS is Solana’s validation-client event. Check [solana.com/tds](http://solana.com/tds) for updates.

  * We hosted four events at our offices in San Francisco and had hundreds of great people come and hang out.

  * The theme of last week was performance testing and we hit some major benchmarks. SLP1 is on the horizon. Check the Github.<https://github.com/solana-labs>

  * Tour del SOL is racing. TdS is Solana’s validation-client event. Check [solana.com/tds](http://solana.com/tds) for updates.

  * We wrote a post on SFBW and the great projects we worked with: <https://medium.com/solana-labs/solana-at-sfbw-showed-that-cooperation-is-key-to-blockchain-growth-d1cab5011b10>

  * We are working to best support developers looking to build on Solana. Experience with onboarding to a new Layer 1? Let us know. [andrew@solana.com](mailto:andrew@solana.com)

  * We are looking for industry experts to interview for our [#nosharding Podcast.](https://solana.com/category/podcast/)

 **Michael from Loom**

 _Loom Network is a universal layer 2 hub. Developers can deploy and scale
their dapps directly on Loom’s mainnet as well as interoperate with other
major layer 1 chains such as Ethereum, Binance, Libra, Bitcoin, etc._

  * Released [Build 1328 Hard Fork](https://loomx.io/developers/en/extdev-release-notes.html#extdev-build-1328-hard-fork-2019-10-27) \-- including improvements for sending Ethereum transactions using the eth_sendRawTransaction JSON-RPC method, validator node monitoring, and performance enhancements

  * As part of a [Transfer Gateway upgrade](https://loomx.io/developers/en/how-to-prepare-for-the-transfer-gateway-update.html) (scheduled for Nov 12), added a new API for interacting with Eth gateway contracts

  * Released article [clarifying common misconceptions around Loom](https://medium.com/loom-network/5-misconceptions-about-loom-network-that-need-to-die-%EF%B8%8F-2c6eba1f657d)

  * [Released two brand new CryptoZombies courses](https://medium.com/loom-network/two-new-advanced-solidity-lessons-smart-contract-testing-and-dapp-deployment-with-truffle-aeeb790cc6f4). Learn how to test your smart contracts and deploy your dapp to Ethereum and Basechain using Truffle.

  * Launched the [CryptoZombies for Libra](https://medium.com/loom-network/become-a-facebook-libra-blockchain-developer-and-master-the-move-language-with-cryptozombies-a29a5e2f34d6) course, a 10-part lesson for mastering the basics of Libra and the Move programming language.

#### Financial Infrastructure

 **Antonio from dYdX**

 _dYdX is a decentralized exchange for margin trading, borrowing, lending, and
eventually derivatives. dYdX allows traders to trustlessly short and get
leverage on crypto assets._

  * [Dolomite DEX launching](https://cointelegraph.com/news/dolomite-dex-to-launch-margin-trading-with-stop-loss-orders) margin trading built on dYdX!

  * Rolling out new designs for our trade page

  * Working on: isolated closes on our native markets, price charts using native market data, MCD upgrade plans

  * Launched isolated position closes on native market

  * Removed all non-dYdX markets from the site

  * Launching updated trade page designs this week

  * dYdX is now [running a MakerDAO V2 Oracle reporter](https://blog.makerdao.com/introducing-oracles-v2-and-defi-feeds/)

  * Released [multi-collateral DAI upgrade plan](https://medium.com/dydxderivatives/multi-collateral-dai-migration-on-dydx-e130575c4454)

  * Working on: WebSocket API for orders, replace order API endpoint, pending balance API endpoint, MCD upgrade

  * [Hiring](https://dydx.exchange/careers/) software engineers & product designers full-time in SF!

 **Vanessa from Celo**

 _Celo’s aim is to empower anyone with a smartphone anywhere in the world to
have access to financial services, send money to phone numbers, and pay
merchants — all on a decentralized platform that is developed and operated by
the community._

  * [Announced The Great Celo Stake Off](https://medium.com/celohq/announcing-the-great-celo-stake-off-12eb15dd5eb0), an incentivized competition running on top of the Baklava testnet. In total, the top 50 teams by accumulated testnet tokens and various other criteria will be rewarded with up to 2 million mainnet staking tokens (Celo Gold). [Register](https://docs.google.com/forms/d/e/1FAIpQLSfbn5hTJ4UIWpN92-o2qMTUB0UnrFsL0fm97XqGe4VhhN_r5A/viewform) to participate. 

  * Published two blog posts on how Celo’s Proof of Stake works:

    * [Consensus and Proof of Stake in the Celo Protocol](https://medium.com/celohq/consensus-and-proof-of-stake-in-the-celo-protocol-3ff8eee331f6)

    * [Celo’s Proof of Stake Mechanism](https://medium.com/celohq/celos-proof-of-stake-mechanism-31061fbebea)

  * C Labs team is finalizing the development of Baklava testnet features (proof of stake system contracts, validator proxies, validator user experience tools, and more)

  * C Labs team is in Liberia this week piloting cash transfers with GiveDirectly. Early finding: the new ‘Celo Lite’ mode was successful in enabling sending a transaction from a $20 phone purchased at the Monrovia Airport!

  * [Follow along](https://www.instagram.com/withcelo/) the C Labs journey and meet users on the new Instagram account [withcelo](https://www.instagram.com/withcelo/).

  * Wrapped up the inaugural Prosper Retreat, and given success, will host more in 2020. [Read about one participant’s experience](https://medium.com/celohq/if-money-were-beautiful-the-whole-world-would-be-like-prosper-retreat-6770145d226)

 **Coulter from MakerDAO**

 _Maker is comprised of a decentralized stablecoin, collateral loans, and
community governance._

  * Maker is making [big changes to terminology](https://blog.makerdao.com/say-goodbye-to-cdps-and-hello-to-maker-vaults/) for the launch of Multi-Collateral Dai. CDPs will be renamed Vaults, MCD will just be "Dai" and today's Single Collateral Dai will be known as "Sai."

  * The latest blog [recapping everything Maker has been up to in October](https://blog.makerdao.com/making-maker-october-2019/) is now live. It's a perfect way to catch up on everything we're working on. 

  * You can now [test your favorite dapps](https://blog.makerdao.com/test-your-favorite-dapps-pre-mcd-launch/) pre-MCD launch

  * 2gether has integrated Dai into [their Visa card ](https://medium.com/2gether/today-is-the-dai-2gether-now-supports-dai-ddeef4f4873b)

  * With Argentina's recent capital controls only allowing the purchase of $200 USD per month for its citizens, [Mariano Conti's talk from Devcon](https://slideslive.com/38920018/living-on-defi-how-i-survive-argentinas-50-inflation) about living in ARG and being paid in Dai is that much more relevant.

  * Here is [what to expect](https://blog.makerdao.com/what-to-expect-with-the-launch-of-multi-collateral-dai/) with the launch of Multi-Collateral Dai. It includes terminology updates, exchange information, Oasis news, migration procedures and more. 

  * 100 million Dai! The total circulation of Dai hit an all-time high, leading MKR holders to an [executive vote](https://blog.makerdao.com/executive-vote-stability-fee-debt-ceiling-nov-7/) to increase the debt ceiling. 

  * We partnered with [Althea in a pilot](https://blog.althea.net/althea-in-abuja/) to bring bandwidth to the people of Nigeria.

#### Layer two and interoperability

 **Tieshun from Namebase**

 _Namebase is the easiest way to buy, sell, and use Handshake._

  * Many Handshake contributors are at the ICANN66 meetup this week in Montreal. The Handshake panel will be at 1:30-3pm est on Tuesday. 

  * Boyma from [Purse.io](http://purse.io/) gave a presentation on Handshake at the ICANN66 meetup in Montreal. Here is the [recording](https://zoom.us/recording/play/ErFyW-rWKtwP0pnDCsRkdcxakWsL2l2j7sZ1D5nDoa1uYQkFcA7fL5gzsbiWJnED?startTime=1572978711000).

  * Shayan Eskandari helped host the first ever Handshake meetup in Montreal! Over 20 crypto enthusiasts showed up to hear presentations from Boyma, Mark Tyneway, Matthew Zipkin, and Tieshun Roquerre. Here are some pictures from the meetup:

 **Alexandra from Polkadot**

 _[Polkadot](https://polkadot.network/) empowers blockchain networks to work
together under the protection of shared security._

  * Kusama network successfully [transitioned to Proof of Stake](https://twitter.com/a4fri/status/1188939968531615745?s=20), [added support for all major cryptocurrency wallets, launched Council elections](https://medium.com/polkadot-network/kusama-cc-2-prepos-a0ce785bb629), and [passed 200 nodes](https://twitter.com/kusamanetwork/status/1188809380759621633?s=20).

  * Introduced an [experimental Wasmtime execution engine](https://github.com/paritytech/substrate/pull/3869/) for Substrate-based parachains to speed up block sync and validation.

  * New [Polkadot Ecosystem Fund launched](https://polkadot.network/announcing-the-polkadot-ecosystem-fund/?utm_source=twitter&utm_medium=social&utm_campaign=Polychain%20Cap%20Fund) by Web3 Foundation and Polychain Capital to support teams building Polkadot parachains.

  * Kusama, a canary network for Polkadot, [received several updates](https://github.com/paritytech/polkadot/releases), including improved block import latency, typed RPC queries, support for an experimental AOT wasm compiler, optimized CPU footprint, and some key performance improvements.

  * Plasm Network, a scalable DApps parachain built with Plasma and Lightning Network, [launched their testnet](https://medium.com/staked-technologies/plasm-testnet-launch-90d7e58328b3).

  * Kusama webinar with Bill Laboon published on [YouTube](https://www.youtube.com/watch?v=sFhFwTlU-A8&list=PLOyWqupZ).

 **Matt from 0x**

 _0x_  is an open protocol that enables the peer-to-peer exchange of assets on
the Ethereum blockchain.

  * We just announced the upcoming vote for 0x v3! Introducing 0x v3 is an exciting new chapter for our protocol and community, as this upgrade includes ZRX staking and a powerful set of bridge contracts that aggregate liquidity from 0x and other DEX networks like Kyber, Uniswap, and MakerDAO's Oasis. Learn more about the v3 upgrade [here](https://blog.0xproject.com/0x-the-community-owned-liquidity-api-26da5732447e).

  * We introduced a new initiative [OpenZKP](https://blog.0xproject.com/introducing-openzkp-1dea6b22dceb), an open-source zk-STARK implementation. Check out our [documentation](https://docs.rs/zkp-stark/0.1.2/zkp_stark/) and [examples](https://github.com/0xProject/OpenZKP/tree/master/crypto/stark/examples).

  * [The 0x Core Team is hiring](https://0x.org/about/jobs) across a variety of roles. Join us and do the most impactful work of your life.

 **Dong Mo from Celer**

 _Celer Network is a layer-2 scaling platform that enables fast, easy and
secure off-chain transactions for not only payment transactions, but also
generalized off-chain smart contracts._

  * We finished the social feed for the home screen and the new landing page UI.

  * We improved the matching UI.

  * We finished integrating the FIAT on-ramp and off-ramp APIs on iOS.

  * On our backend side, we continue implementing Q4 OPS features and enhancements. 

  * We completed the development and testing of the SGN gateway.

  * We provided support for Celer events during SF Blockchain week.

  * We completed the fiat onramp functionality.

  * We released an internal test version for USD on-ramp and off-ramp features.

  * We added email verification in cloud backup flow.

  * We fixed bugs and improved stability.

  * We continued our development of OSP features for Q4.

  * We provided support for CelerX campaign and operational improvements.

  * We implemented SGN penalty feature.

#### Application infrastructure

 **Mark from Helium**

 _Helium is a decentralized, open wireless network built on a new blockchain
for the physical world. It relies on a novel type of work called Proof of
Coverage, and a new consensus algorithm (based on HoneyBadger BFT). The Helium
Network is used to route data for long range, lower power devices (often
called "IoT" devices)._

 _The Helium Network is built on Hotspots. The Helium Hotspot is a combination
LongFi wireless router and Helium blockchain miner built and distributed by
Helium, Inc. Hotspots create a long-range wireless network for routing packets
to and from Helium LongFi-enabled devices and perform ongoing mining duties to
secure the Helium Network.  Hotspot operators are rewarded in Helium Token
(HNT), a new cryptocurrency native to the Helium blockchain.  
_

 _The Helium Network went live in Austin, TX in August 2019 and has already
grown to over 1250 Hotspots deployed across hundreds of cities in the United
States._

  * [helium.com](http://helium.com/)

  * Live coverage map, block explorer, and consensus viewer -> [network.helium.com](http://network.helium.com/)

  * Blockchain and network statistics -> [dashboard.helium.com](http://dashboard.helium.com/)

  * Developer Docs -> [developer.helium.com](http://developer.helium.com/)

  * Blockchain and Proof of Coverage Docs -> [developer.helium.com/blockchain/overview](http://developer.helium.com/blockchain/overview)

  * Helium on GitHub -> [helium.com/github](http://helium.com/github)

 **Alexandra from Parity Technologies**

 _Parity  Technologies builds core blockchain infrastructure, from Parity
Ethereum, an Ethereum client, to Polkadot, an interoperable blockchain
network._

  * Kusama network successfully [transitioned to Proof of Stake](https://twitter.com/a4fri/status/1188939968531615745?s=20), [added support for all major cryptocurrency wallets, launched Council elections](https://medium.com/polkadot-network/kusama-cc-2-prepos-a0ce785bb629), and [passed 200 nodes](https://twitter.com/kusamanetwork/status/1188809380759621633?s=20).

  * An [experimental Wasmtime execution engine](https://github.com/paritytech/substrate/pull/3869/) introduced to Substrate to speedup block sync and validation.

  * [Gather](https://www.parity.io/gather-why-a-decentralized-blockchain-platform-is-the-only-sustainable-answer-to-the-meetup-com-pricing-hike/), a decentralized blockchain alternative to Meetup.com built on Substrate by community members

  * New Parity presentations from Devcon 5: Wei Tang on [Building Ethereum 2.0 on Substrate](https://slideslive.com/38920039/building-ethereum-20-on-substrate) and [Ethereum Backwards Compatibility](https://slideslive.com/38920010/toward-backward-compatible-ethereum-upgrades), Thibaut Sardan on [Building a DApp on a Light Client](https://slideslive.com/38920073/lessons-learned-to-build-a-dapp-on-a-light-client).

  * New video series about projects [Built with Substrate](https://www.youtube.com/playlist?list=PLp0_ueXY_enWpe1riaQOVw4tEWPmtX8e-).

  * [Kusama network received several updates](https://github.com/paritytech/polkadot/releases), including improved block import latency, typed RPC queries, support for an experimental AOT wasm compiler, optimized CPU footprint, and some key performance improvements.

  * Plasm Network, a scalable DApp platform built on Substrate, [launched their testnet](https://medium.com/staked-technologies/plasm-testnet-launch-90d7e58328b3).

  * Kusama webinar with Bill Laboon published on [YouTube](https://www.youtube.com/watch?v=sFhFwTlU-A8&list=PLOyWqupZ).

  * [New Relay Chain podcast episode](https://relaychain.fm/8-censorship-human-rights-activism) released on censorship vs content moderation with [Jillian York](https://twitter.com/jilliancyork).

  * We're hiring! [Check out our jobs.](https://www.parity.io/jobs/#jobs)

 **Matt from Keep Network**

 _The Keep Network is a privacy layer for public chains, enabling
interactivity with private data and interoperability across chains. It does
this with keeps, off-chain containers for private data that help smart
contracts harness the full power of the public blockchain._

  *  **tBTC:**

    * Started looking ahead to what v2 of tBTC will look like

    * Plugged the redemption dApp into the tBTC contracts, now working through bugs

    * Progress on planning remaining work through mainnet

 **Random beacon:  **

    * Group size for random number generation increased to 64 members

    * We are progressing on optimizing the cost of the beacon, including distributed key generation, group selection, and new relay entry submission

    * We are setting up the infrastructure for Ropsten contract deployment

    * For more updates and questions join our [Slack](https://join.slack.com/t/keep-network/shared_invite/enQtNTMzMjUwNTUxNjA3LWI2ZjIxNGNmZGMxMTYzYjE0YmY2MjNkNDFkN2JiMDFlYmFkZDIyMzI4ZTZkNmNjZjgwMzVhYjU4YWQ5MjBiYmY) and check out the [Keep blog](https://blog.keep.network/).

 **Doug from Livepeer**

 _Livepeer is a decentralized video infrastructure network, dramatically
reducing prices for developers and businesses building video streaming
applications at scale.  _

  * The first [public testnet for the upcoming Streamflow scaling update](https://medium.com/livepeer-blog/livepeers-public-streamflow-testnet-is-now-live-45b8fb500932) has continued to run for a week. A [beta explorer is available](https://explorer-streamflow.now.sh/) for token holders to begin learning the participate post upgrade.

  * Developer documentation for infrastructure operators is now online, to [learn how to scale out GPUs for video encoding behind a Livepeer orchestrator node](https://livepeer.readthedocs.io/en/latest/streamflow-public-testnet.html).

  * The next steps before mainnet release are enabling local video transcoding validation and more intelligent failover and node selection to enable high video encoding reliability in the case of node failures. 

  * The first [public testnet for the upcoming Streamflow scaling update](https://medium.com/livepeer-blog/livepeers-public-streamflow-testnet-is-now-live-45b8fb500932) has continued to run for two weeks. 

  * A [new token holder app](http://explorer.livepeer.org/) launched, featuring staking and protocol exploration. It is functional for both the mainnet version of Livepeer and the Streamflow testnet.

 **David from Sia**

 _Sia is a decentralized cloud storage platform leveraging blockchain
technology to create a data storage marketplace that is more robust and more
affordable than traditional cloud storage providers._

  * Matt created a new tool, connmonitor, that will provide more granular information about the bandwidth usage by each Sia module.

  * Marcin added a watchdog subsystem to the renter module to improve its reliability. This watchdog monitors the blockchain for information about the renter’s contracts (like contracts that failed to be included on the blockchain or proofs of storage submitted by hosts) and takes necessary actions, like broadcasting again a stalled contract or informing about a host that failed its obligations.

  * Matt expanded and added clarity to the readme file of the Sia directories.

  * Matt improved the API documentation: the format has been cleaned, the difference between available and recoverable files has been clarified and typos were corrected.

  * Accounts impersonating Sia are messaging users about a fake mandatory update, not created by Nebulous. It links to a false GitHub repository with binaries for downloading that will likely infect the user with malware. No one from Sia will ever contact you privately to install software or transfer tokens.

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

