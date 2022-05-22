[![](https://substackcdn.com/image/fetch/w_96,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F37b09348-f4f1-47a2-b9e0-a2007299e6e4_256x256)](https://proofofwork.news)

# [Proof of Work](https://proofofwork.news)

SubscribeSign in

Share this post

Proof of Work #78

proofofwork.news

Copy link

Twitter

Facebook

Email

# Proof of Work #78

[Eric Meltzer](https://substack.com/profile/138320-eric-meltzer)

Oct 30, 2019

[Share](javascript:void\(0\))

#### Bitcoin & Friends

 **Jimmy on Bitcoin**

 **[Optech](https://bitcoinops.org/en/newsletters/) on Bitcoin [ed: sign up
for their newsletter too! it’s great!]**

  *  **Help test release candidates:**  experienced users are encouraged to help test the latest release candidates for the upcoming versions of [Bitcoin Core](https://bitcoincore.org/bin/bitcoin-core-0.19.0/) and [C-Lightning](https://github.com/ElementsProject/lightning/releases/tag/v0.7.3rc3).

  * Starting the first week of November, several Bitcoin contributors will be hosting a series of weekly meetings to help guide people through review of the proposed [bip-schnorr](https://github.com/sipa/bips/blob/bip-schnorr/bip-schnorr.mediawiki), [bip-taproot](https://github.com/sipa/bips/blob/bip-schnorr/bip-taproot.mediawiki), and [bip-tapscript](https://github.com/sipa/bips/blob/bip-schnorr/bip-tapscript.mediawiki) changes. 

 **Aviv from Spacemesh**

 _Spacemesh is a programmable cryptocurrency powered by a novel proof-of-
space-time consensus protocol._

  * We are finalizing the first release of the Spacemesh open testnet. We call it Spacemesh 0.1. Anyone with a PC, an Internet connection and some free disk space should be able to join. We are working hard to release Spacemesh 0.1 this December. [Sign up here.](https://spacemesh.io/)

  * We finished revamping most of the [testnet guide content](https://testnet.spacemesh.io/#/all) to reflect sm 0.1 functionality, including a new guide page about s0.1 to [clarify the final feature set](https://testnet.spacemesh.io/#/spacemesh0.1)

  * Additional QA on app latest build to get it ready + enumerate all missing features \+ wrap up UI development - [see new issues in smapp repo.](https://github.com/spacemeshos/smapp/issues)

  * We are writing documentation and adding comments to code in preparation for open testnet. [Merged issues](https://github.com/spacemeshos/go-spacemesh/pulls?q=is%3Apr+is%3Aclosed)

  * [Article by Tomer Afek, Spacemesh CEO](https://cointelegraph.com/news/how-blockchain-and-crypto-are-poised-to-shift-the-balance-of-power)

  * We decided on [names](https://github.com/spacemeshos/product/blob/master/sm0.1_names.md) for our coin, node, and other key Spacemesh components. Long live Smesh!

  * Tal Moran speaking at the IACR conference in Santa Barbara about [Simple Proofs of Space Time and Rational Proofs of Storage.](https://www.youtube.com/watch?v=hIl1Fx0p8hY)

  * Working on app auto-update and minor fixes - [issues in smapp repo.](https://github.com/spacemeshos/smapp/issues)

  * Automat-it (out testnet infrastructure provider) are in the final stages of integration. The node's core protocols are code complete, the only things left are minor changes in the node's API. [Merged issues](https://github.com/spacemeshos/go-spacemesh/pulls?q=is%3Apr+is%3Aclosed)

  * More info on [our site.](https://spacemesh.io/weekly-updates)

#### Privacy coins

 **Paige & Zooko from Zcash**

 _Zcash is a  digital currency utilizing zk-SNARKs to enable its privacy-
protecting properties._

  *  **Core Team:  **

    * [Release v2.1.0 rc1 · Pull Request #4169 · zcash/zcash](https://github.com/zcash/zcash/pull/4169)

    * Mempool limit/DoS mitigation merged PR#4145

    * MacOs fixes PR#4166, PR#4157

    * Identified bug PR#4177 - fix in review and planned for 2.1.0

    * <https://github.com/zcash/zcash/pull/4171> – this makes it easy to define and run AFL fuzzing against parts of zcashd

    * <https://github.com/zcash/zcash/pull/4157>

  *  **Wallet Team**

    * We’re making progress on the iOS SDK, which now can get blocks, store them, and scan blocks for transaction data. We have also created an Android SDK demo app that showcases a range of functionality ([link here](https://github.com/zcash/zcash-android-wallet-sdk/tree/feature/demo-app/samples/demo-app/app/src/main/java/cash/z/wallet/sdk/demoapp/demos)). The demo app exercises: get private key, get address, get the latest height, get block, get block range, list transactions, and send.

    * Librustzcash has reached good enough test coverage (mid-60%), and it not only has more test coverage, but it’s running smarter tests. In addition to this, more of our work has been based off wallet developer feedback, which I think is a good thing. Go team!

  * Zcash turns three years old on Mon 10/28, happy birthday to us! 

  * [More updates here](https://forum.zcashcommunity.com/t/october-25-2019-weekly-update-engineering/35254)

 **Daniel from Grin**

 _Grin is a community-driven implementation of the Mimblewimble protocol that
aims to be privacy preserving, scalable, fair, and minimal._

  * Merged PRs: [2 in /grin](https://github.com/mimblewimble/grin/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A2019-10-21..2019-10-27+) | [0 in /grin-wallet](https://github.com/mimblewimble/grin-wallet/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A2019-10-21..2019-10-27+) | 1 unique contributors

  * Grin v2.1.0 node and wallet [was released](https://www.grin-forum.org/t/grin-grin-wallet-2-1-0-released/6308).

  * Call for community members to participate in the [Grin 2020 roadmap process](https://www.grin-forum.org/t/grin2020-roadmap-calling-for-blog-posts-with-ideas/6327/3).

  * [Grin South Florida meetup event](https://www.meetup.com/Grin-USA-Meetup-Group/events/265900026/) announced for December 7 in Fort Lauderdale.

  * Yeastplume's been [working on improving how the wallet handles state updates](https://www.grin-forum.org/t/yeastplume-progress-update-thread-oct-to-dec-19/6211/5).

  * Registration now open for [GRINCON1](https://grincon.org/). NOVEMBER 22. BERLIN. Sign up for free and see you there!

  * In the last [governance meeting](https://github.com/mimblewimble/grin-pm/blob/master/notes/20191022-meeting-governance.md) roadmap planning, website updates, and open research problems for Grin was covered.

  * Grin is 100% funded by donations. Please support Grin development - [Donate now](https://grin-tech.org/general_funding).

  * More Grin info [here](https://grinnews.substack.com/).

 **Beni from Beam**

 _Beam is a confidential and scalable cryptocurrency based on Mimblewimble._

  *  **General**

    *  **Vladislav Gelfer aka  [Valdok](https://github.com/valdok), Beam Lead Dev, is attending [ZK Proof](https://zkproof.org/) in Amsterdam, October 28-29th 2019 with a talk about [Lelantus](https://github.com/BeamMW/beam/wiki/Lelantus-MW)**

    * Our [website](https://www.beam.mw/) is now available in Chinese, Russian, Spanish and many more languages

  *  **[Dev](https://github.com/BeamMW/)**

    * Starting development of a Web Wallet 

    * [Beam iOS Wallet - Clear Cathode 3.1](https://github.com/BeamMW/ios-wallet/projects/12) will be released soon

    * We have 213 open issues in [/beam](https://github.com/BeamMW/beam/issues), 32 open issues in [/android-wallet](https://github.com/BeamMW/android-wallet/issues), and 28 open issues in [/ios-wallet](https://github.com/BeamMW/ios-wallet/issues)

    * We had 74 commits in [/ beam](https://github.com/BeamMW/beam/graphs/commit-activity)

 **Arnaud from AZTEC Protocol**

 _AZTEC Protocol is an efficient zero-knowledge protocol built on top of
Ethereum, making plug-and-play value transmission and asset governance privacy
tools for developers and companies.  _

  * We have officially kicked off Ignition, our trusted setup ceremony. You can follow the progress live at [https://ignition.aztecprotocol.com](https://ignition.aztecprotocol.com/)

  * We released our PLONK implementation benchmarks. Proof construction comes in at ~23 seconds for a circuit (built over BN254) of over 1 million gates. We think a typical private transaction on Ethereum will come in at ~128,000 to 512,000 PLONK gates.  
You can find the implementation here:
<https://github.com/AztecProtocol/barretenberg>

  * Outside of Ignition, we’re doing final deploy tests for our mainnet protocol, preparing for our launch later this year.

#### Smart contracting platforms

 **Peter from NEAR**

 _NEAR is a sharded proof-of-stake blockchain._

  * Alex will be coding the finality gadget and the randomness beacon [live next week](https://twitter.com/AlexSkidanov/status/1187447311711891456)! Don’t miss the opportunity to see some hardcore low-level code written live

  * 154 PRs across 22 repos by 21 authors. Featured repos:[ nearcore](https://github.com/nearprotocol/near-wallet),[ nearlib](https://github.com/nearprotocol/nearlib),[ near-shell](https://github.com/nearprotocol/near-shell/),[ near-wallet](https://github.com/nearprotocol/near-wallet),[ near-bindgen](https://github.com/nearprotocol/near-bindgen), [near-fiddle-api](https://github.com/nearprotocol/near-fiddle-api), [NEARStudio](https://github.com/nearprotocol/NEARStudio/), [assemblyscript](https://github.com/nearprotocol/assemblyscript), [borsh](https://github.com/nearprotocol/borsh), [create-near-app](https://github.com/nearprotocol/create-near-app), [stakewars](https://github.com/nearprotocol/stakewars) and [near-explorer](https://github.com/nearprotocol/near-explorer/)

  * We [merged work on Nightshade into master](https://github.com/nearprotocol/nearcore/commit/8f488f3fd9b96b1a329e6f24b4bff870f446d7df), and the current testnet is running Nightshade with 8 shards!

  * We published a proposed Proof-of-Space-Time construction and Nightshade Finality gadget paper, read about it [here](https://twitter.com/AlexSkidanov/status/1187875251998191618) or find the paper itself [here](https://near.ai/post)

  * [Seed phrase recovery support](https://github.com/nearprotocol/near-wallet/pull/167) in near-wallet.

  * Further work on stress tests, that now[ restart nodes](https://github.com/nearprotocol/nearcore/pull/1554) and [mess up with network](https://github.com/nearprotocol/nearcore/commit/f3c72387b153e7c21dba14575b0e56a7ec9dcc96) in nearcore

  * [Rpc transaction routing](https://github.com/nearprotocol/nearcore/pull/1544)  in nearcore

  * [Introduced `chunk` API](https://github.com/nearprotocol/nearcore/pull/1524)  in nearcore

  * [Fix reading fixed size arrays and add a test](https://github.com/nearprotocol/borsh/pull/35) in borsh

  * [Change tx status to use the new API](https://github.com/nearprotocol/near-shell/pull/172) in near-shell

  * [Implemented Transaction Details Page](https://github.com/nearprotocol/near-explorer/pull/109) in near-explorer

 **Topper from Quorum Control**

 _Quorum Control makes Tupelo, a permissionless proof of stake DLT platform
purpose-built to model individual objects that enables flexible public or
private data models._

  * As part of our ongoing efforts to productionize the Tupelo Testnet, GameNet, and Community service, we have been running a range of new load tests. The most recent tests uncovered a  defect and optimization opportunity.

  * The defect uncovered (and addressed) prevented highly concurrent reads to ChainTrees in the golang and the wasm clients.

  * To improve client and associated network performance, the team separated block and dht datastores.

  * The QC team actively participated in the Diffusion hackathon last weekend in Berlin, mentoring, presenting, and networking.  We [congratulate all the winners](https://twitter.com/OVioHQ/status/1186972010548727808) and look forward to the next one.

 **Andrew from Solana**

 _Solana is a scalable blockchain that utilizes proof of history to verify the
ordering and passage of time between events. It consists of a network of 200
physically distinct nodes which support a sustained throughput of more than
50,000 TPS.  _

  * We are releasing solana.0.20 today. Check the Github. <https://github.com/solana-labs>

  * It is SFBW! We have events at our office throughout the week. We partnered with some great projects: 0x, Hummingbot, Dydx, DDEX, Chainlink, SKALE, NEAR, Harmony, Coda and Nervos. Our list of events can be found here. <https://medium.com/solana-labs/solana-takes-over-san-francisco-blockchain-week-and-youre-invited-c63de1b56e35>

  * We are working to best support developers looking to build on Solana. Experience with onboarding to a new Layer 1? Let us know.

  * Tour del SOL is racing. TdS is Solana’s validation-client event. Check [solana.com/tds](http://solana.com/tds) for updates.

  * Episode #7 and #8 of our podcast #nosharding with guests Alexander Skidanov and Brad Kam is live: <https://solana.com/podcast/>

 **Myles from EOS**

 _EOS is a new blockchain architecture designed to enable vertical and
horizontal scaling of decentralized applications._

  * Dan Larimer released a [new governance proposal](https://medium.com/@bytemaster/blockchain-governance-proposal-470478e42686)

  * Dan also wrote [an article](https://medium.com/@bytemaster/how-trustless-contracts-overcome-artificial-restrictions-f8cc939faeb6) about trustless smart contracts 

  * EOS NY released their own [governance proposal](https://medium.com/eos-new-york/uniting-stake-holder-incentives-to-maximize-decentralization-performance-530af1560401)

  * [Wyoming Cloud Co.](https://www.wycloud.io/) allows user to easily purchase EOS mainnet resources

  * anyx from Greymass wrote about [vote incentivization](https://decentium.org/teamgreymass/how-vote-ince) and its negative effects

#### Financial Infrastructure

 **Nelson from Cadence**

 _Cadence is a digital securitization and investment platform for private
credit. Cadence issues tokenized assets that are digital reflections of real
world fiat and investment transactions._

  * We published our most recent case-study, exploring our first offering to feature [real-time data](https://withcadence.io/blog/case-study-cadence-first-offering-with-real-time-performance-data/), a breakthrough in the industry.

  * The past few weeks have seen several media placements with coverage in [Forbes](https://www.forbes.com/sites/benjaminpirus/2019/10/09/fatburger-and-others-feed-30-million-into-ethereum-for-new-bond-offering/)[twice](https://www.forbes.com/sites/michaeldelcastillo/2019/10/01/morningstar-is-building-a-blockchain-bridge-to-the-117-trillion-debt-securities-industry/#cd030493612e), [Blockonomi](https://blockonomi.com/fat-burger-ethereum-bond/) and [Securities.io](https://www.securities.io/fat-brands-turns-to-cadence-in-30m-bond-issuance/), among others.

  * Through Oct. 25, we’ve issued over $30M in structured notes across 27 different offerings.

  * Cadence Founder & CEO Nelson Chu, as well as Prath Reddy, Head of Capital Markets, will be speaking at the Asset-Backed Tech conference in NYC on Nov. 20.

  * We're [hiring engineers](https://angel.co/company/withcadence/jobs)!

 **Antonio from dYdX**

 _dYdX is a decentralized exchange for margin trading, borrowing, lending, and
eventually derivatives. dYdX allows traders to trustlessly short and get
leverage on crypto assets._

  * Launched native [ETH-USDC](https://trade.dydx.exchange/ETH-USDC/dydx) & [DAI-USDC](https://trade.dydx.exchange/DAI-USDC/dydx) markets!

  * Working on: Isolated position closes through native market, price charts using native market data, updated UI for trade page

  * [Hiring](https://dydx.exchange/careers/) Software Engineers & Product Designers full-time in SF!

 **Coulter from MakerDAO**

 _Maker is comprised of a decentralized stablecoin, collateral loans, and
community governance._

  * As a reminder, [the release of Multi-Collateral Dai is slated for November 18th](https://blog.makerdao.com/breaking-launch-date-of-multi-collateral-dai-announced-at-devcon-5/). We will have tons of information in the coming weeks, but please see [how to upgrade](https://blog.makerdao.com/looking-ahead-how-to-upgrade-to-multi-collateral-dai/) your Dai or CDP when it's live.

  * Here's everything you need to know about our [MCD security efforts](https://blog.makerdao.com/mcd-security-roadmap-update-october-2019/) in preparation for the launch of Multi-Collateral Dai

  * [Oasis.Trade](https://oasis.app/) has launched. The first phase of the new all-in-one DeFi hub allows for trading between BAT, ZRX, REP, and ETH against DAI. 

#### Layer two and interoperability

 **Tieshun from Namebase**

 _Namebase is the easiest way to buy, sell, and use Handshake._

  * Namebase and Sia are hosting a joint meetup on Wednesday, Oct 30 from 5pm-8pm pst in San Francisco! Namebase's CEO [@TieshunR](https://twitter.com/TieshunR) and Sia's CEO [@DavidVorick](https://twitter.com/DavidVorick) will talk about decentralized naming and decentralized storage! Food and drinks will be provided as well. RSVP here: <https://www.eventbrite.com/e/sia-handshake-meetup-tickets-78687250685>

 **Alexandra from Polkadot**

 _[Polkadot](https://polkadot.network/) empowers blockchain networks to work
together under the protection of shared security._

  * [First parachain successfully connected to Polkadot!!](https://twitter.com/gavofyork/status/1186646273685884930)

  * Fixed a sync issue with [GRANDPA](https://medium.com/polkadot-network/grandpa-block-finality-in-polkadot-an-introduction-part-1-d08a24a021b5), Polkadot’s unique consensus algorithm (validators will need to run in archive mode for the time being)

  * [Polkadot wiki](https://wiki.polkadot.network/) updated (lots more info and better organized)

  * Recording out: [Polkadot Cofounder Robert Habermeier on Polkadot research and development.](https://twitter.com/polkadotnetwork/status/1186915397989273601)

  * Recording out: [Alistair Stewart at Devcon discussing Polkadot's data availability & validity scheme](https://twitter.com/polkadotnetwork/status/1187579559841091591) that requires fewer validators per shard, and less total computational and networking resources.

  * [Parachain Development Kit](https://twitter.com/polkadotnetwork/status/1187363373979033603) information out.

  * Web3 Foundation is hiring people to [help build Polkadot](https://web3.bamboohr.com/jobs/), as well as [providing grants](https://github.com/w3f/Web3-collaboration/blob/master/grants/grants.md) for software development, research, technical education and community engagement efforts related to Polkadot.

 **Dong Mo from Celer**

 _Celer Network is a layer-2 scaling platform that enables fast, easy and
secure off-chain transactions for not only payment transactions, but also
generalized off-chain smart contracts._

  * We finished designing mobile API for depositing USD and finished UI in USD deposit flow.

  * We finished back up UI in adding USD flow.

  * We continue the implementation of Q4 OSP functionality.

  * We continue to work on the enhancements to the SGN Gateway.  

#### Application infrastructure

 **Alexandra from Parity Technologies**

 _Parity  Technologies builds core blockchain infrastructure, from Parity
Ethereum, an Ethereum client, to Polkadot, an interoperable blockchain
network._

  * Parity developers connected a [Substrate-based parachain to Polkadot](https://twitter.com/bkchr/status/1186638431948021760).

  * New [Rogue-like game built on the Substrate blockchain development framework](https://twitter.com/EAThomson/status/1186410009602736128).

  * [New podcast interview on recent Substrate developments](https://relaychain.fm/7-mentorship-values-open-source), including Substrate Large File Storage.

  * We're hiring! [Check out our jobs.](https://www.parity.io/jobs/#jobs)

 **Wes from Theta**

 _Theta is an end-to-end infrastructure for decentralized video streaming._

  * [Theta Network will be featured at the Samsung Developer Conference](https://medium.com/theta-network/theta-network-featured-at-the-samsung-developer-conference-to-demo-integration-in-smart-tvs-4a5c4bdc42bd) this week, demoing our work with Samsung’s Visual Display group in integrating Theta protocol in Samsung smart TVs

  * Recently signed an MOU with video platform [DLive to integrate Theta protocol](https://medium.com/theta-network/theta-network-partners-with-dlive-to-bring-decentralized-video-streaming-to-over-5-million-users-d65300057c4e?source=collection_home---4------1-----------------------) into their video delivery infrastructure

  * [Bitmovio video app also to add Theta protocol](https://medium.com/theta-network/bitmovio-video-platform-to-integrate-theta-mainnet-in-q4-purchase-initial-tfuel-supply-f5a007f90f3f) to their Android app in November

 **Doug from Livepeer**

 _Livepeer is a decentralized video infrastructure network, dramatically
reducing prices for developers and businesses building video streaming
applications at scale.  _

  * The upcoming scaling release - Streamflow - is [now live on a public testnet](https://medium.com/livepeer-blog/livepeers-public-streamflow-testnet-is-now-live-45b8fb500932).

  * This release includes concurrent GPU mining of cryptocurrency while transcoding video on Livepeer, probabilistic micropayments, and a more scalable architecture to support large scale transcoding. 

 **Matt from Keep Network**

 _The Keep Network is a privacy layer for public chains, enabling
interactivity with private data and interoperability across chains. It does
this with keeps, off-chain containers for private data that help smart
contracts harness the full power of the public blockchain._

  *  **tBTC:**

    * The team has started working on a design system to accompany the open source release of tBTC.

    * Redemption dApp work is under review as we look at connecting the UX flow to our contracts. 

    * The team has been working on some code reorg for JS to reduce cyclical dependencies. 

 **Random beacon:  **

    * We completed work on slashing RFC; a document describing what kind of misbehaviour will be punished by the network and how.

    * We optimised block times for distributed key generation and relay entry signing - we now produce new group key and new random number two times faster.

    * We merged the PR implementing pricing for the beacon, we are still iterating on tests and fixing some minor bugs, but most of the functionality is there.

    * We figured out how can we improve the ticket submission algorithm to make it way cheaper.

    * For more updates and questions join our [Slack](https://join.slack.com/t/keep-network/shared_invite/enQtNTMzMjUwNTUxNjA3LWI2ZjIxNGNmZGMxMTYzYjE0YmY2MjNkNDFkN2JiMDFlYmFkZDIyMzI4ZTZkNmNjZjgwMzVhYjU4YWQ5MjBiYmY) and check out the [Keep blog](https://blog.keep.network/).

 **David from Sia**

 _Sia is a decentralized cloud storage platform leveraging blockchain
technology to create a data storage marketplace that is more robust and more
affordable than traditional cloud storage providers._

  * Sia continued work this week on the file repair process and stuck uploads.

  * Matt and Chris improved the unstuck process of file chunks and speeded up the renter unstuckall command.

  * We’ll be releasing a [1.4.1.3](http://1.4.1.3/) patch to release a considerable improvement in performance and address multiple file repairs issues. [1.4.1.3](http://1.4.1.3/) will include this update and improvements to host churn.

  * David added logs to the repair process of files losing redundancy.

  * Chris added the allowance information to the backups that renters create from their metadata (and can later recover just using their wallet seed!). This will make easier and more intuitive to recover your renter, as your allowance will be set up automatically too.

  * Matt added the new API endpoints gateway/blacklist [POST] & [GET] that allows users to manually block other network peers and view the list of those currently blacklisted.

  * Nebulous will host a [Sia meetup on](https://www.eventbrite.com/e/sia-handshake-meetup-tickets-78687250685) San Francisco on Oct 30th together with the team of the Handshake protocol.

  * Community member @trinancrat#8374 released [Sia Slice](https://github.com/YoRyan/sia-slice), an app that allows you to maintain a mirror of a large file stored on the Sia network. The advantage of this app over other similar is that the file is split in chunks of 100MiB, so after making a change on the file, only the affected chunks will be uploaded. This allows cheap and fast syncing of large files that need to be frequently updated.

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

