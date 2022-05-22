[![](https://substackcdn.com/image/fetch/w_96,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F37b09348-f4f1-47a2-b9e0-a2007299e6e4_256x256)](https://proofofwork.news)

# [Proof of Work](https://proofofwork.news)

SubscribeSign in

Share this post

Proof of Work #77

proofofwork.news

Copy link

Twitter

Facebook

Email

# Proof of Work #77

[Eric Meltzer](https://substack.com/profile/138320-eric-meltzer)

Oct 23, 2019

[Share](javascript:void\(0\))

Good morning from Boston! A few unfinished thoughts from my Asia trip that
I’ll expand upon in the next few issues:

  1. In some cases, exchanges are the enemy. A few bad-actor crypto exchanges in Asia print coins out of nowhere to engineer pump-and-dumps which they directly benefit from. Neither projects nor whales are colluding here; the exchanges themselves are doing this on their own. I used to think decentralized exchanges were something that only hardcore crypto folks cared about, but in the absence of regulation, decentralized exchanges may start to be in more demand as retail realizes how some of the exchanges are fleecing them.

  2. Bitcoin isn’t going anywhere, there are huge inflows to mining in China (setting up big farms, creating new ASICs, etc) despite the price coming down. 

  3. China seems fairly serious about a digital fiat project.

More next time! Thanks for reading.

#### Bitcoin & Friends

 **Jimmy on Bitcoin**

 **[Optech](https://bitcoinops.org/en/newsletters/) on Bitcoin [ed: sign up
for their newsletter too! it’s great!]**

  * Upgrade LND to version 0.8.0-beta: LND’s newest release uses a more extensible packet format, improves backup safety, increases watchtower client integration, makes routing more likely to succeed, and includes many other new features and bug fixes.

  * Upgrade to Eclair 0.3.2: Eclair’s newest release improves backups, makes syncing gossip data more bandwidth efficient (especially for non-routing nodes, such as nodes on mobile devices), and includes many other new features and bug fixes.

  * Review RCs: two popular Bitcoin infrastructure projects have issued Release Candidates (RCs) for the next version of their software. We encourage developers and experienced users to help test these RCs so that any problems can be found and fixed before their general public release:  
Bitcoin Core 0.19.0rc1  
C-Lightning 0.7.3-rc2

 **Johnny from Stellar**

 _Stellar is an open network for sending and exchanging value of any kind. Its
global network enables digitization of assets - from carbon credits to
currencies - and enables movement around the internet with ease._

  *  **On Monday, 10/28, at 1600 UTC**  validators will vote on whether to upgrade the public network to Stellar-core v12.0.0. If you run Stellar-core or Horizon, you should [upgrade right now](https://www.stellar.org/developers/blog/horizon-v0-22-0-released-protocol-12-support/). It has a few big changes including:  
 \- Node status monitoring improvements  
 \- The introduction of a new operation that [makes path payments
symmetrical](https://github.com/stellar/stellar-core/pull/2269)  
 \- The [removal of bucket shadows](https://github.com/stellar/stellar-
core/pull/2205)  
 \- The [end of inflation](https://github.com/stellar/stellar-core/pull/2297)
as we know it

  *  **On Wednesday, 10/30, at 0900 UTC**  there will be a testnet reset, which means everything will get wiped from the testnet ledger. If you are in the middle of something, make a plan to recreate any ledger entries you need, including accounts and balances. Read [here](https://www.stellar.org/developers/guides/concepts/test-net.html#best-practices-for-using-testnet) for best practices when using the testnet.

  *  **[Horizon 0.21.1](https://www.stellar.org/developers/blog/horizon-v0-22-0-released-protocol-12-support/)**  was just released on Thursday, 10/10. The big change: it includes support for Stellar-core v12.0.0! If you run Horizon, make sure and upgrade now.

  *  **[SEP-0024](https://github.com/stellar/stellar-protocol/blob/master/ecosystem/sep-0024.md)** : SEP-0024 has gone from DRAFT to ACTIVE to replace the now-deprecated SEP-0006. If you are curious about the differences between SEP-0024 and SEP-0006, msfeldstein breaks them down [here](https://github.com/stellar/stellar-protocol/pull/407).

  * [Meridian](https://meridian.stellar.org/), the first official Stellar conference, has an entire track of programming dedicated to developers. It’s taking place November 4–5, so if you’re interested in attending, [grab a ticket](https://www.eventbrite.com/e/meridian-tickets-66494150795). You can use the code 'STROOP50' for 50% off at checkout.

  * The second round of the Stellar Community Fund has come to a close. You can [view the winners here](https://medium.com/stellar-community/stellar-community-fund-2-the-results-69b3f6a6040e)! We are now [accepting proposals](https://galactictalk.org/t/SCF) for round 3.

 **Izaak from Coda**

 _Coda is the first cryptocurrency protocol with a constant-sized blockchain.
Coda compresses the entire blockchain into a tiny snapshot the size of a few
tweets using recursive zk-SNARKs._

  * Echo [reduced memory consumption by 35%](https://github.com/CodaProtocol/coda/pull/3662) by replacing glibc's malloc with Jemalloc.

  * Avery got the Coda wallet [working in Ubuntu](https://github.com/CodaProtocol/coda/pull/3689).

  * Paul and Matthew have made and applied tools to enforce a [versioning discipline](https://github.com/CodaProtocol/coda/pull/3646) across the codebase for all types that go on the wire.

  * Izaak is teaching an all-day Zero Knowledge workshop during SF Blockchain Week featuring closing remarks and a happy hour with Vitalik. You'll get hands-on experience programming SNARKs into your dapp - use code POW for 50% off any ticket (limited quantity). <http://bit.ly/SFBWZKP>

#### Privacy coins

 **Paige & Zooko from Zcash**

 _Zcash is a  digital currency utilizing zk-SNARKs to enable its privacy-
protecting properties._

  * [Stanford PING and REJECT](https://crypto.stanford.edu/timings/): Researchers at Stanford presented two types of active side-channel attacks against private (a.k.a. shielded) transactions in [Zcash](https://z.cash/). This Security announcement has been shared earlier this month in the Zcash community forum. Be sure to upgrade your nodes to Version 2.0.7-3 immediately and discontinue use of older versions. _Please note that the issue does not put funds at risk of theft or counterfeiting._

  * Other updates to zcashd core team: 

    * Putting final touches on mempool DoS fix for 2.1.0 which we expect to come out soon

    * Putting final touches in librustzcash v0.1.0

    * Added “developer tooling” making it easier to work simultaneously on librustzcash/zcashd

    * Transitioning to scrum to help increase cycle time

    * Core Team [current backlog](https://github.com/zcash/zcash/projects/23)

  * Dev-Infra team continues to work on updating/migrating Python2 code to Python3 as well as making several major Zcash components Docker compatible. 

  * The reference wallet team has spent the past few weeks paying down technical debt and addressing security concerns. 

    * handled all but one high-level security concerns brought up through internal review (sanitizing inputs, adding encryption between communication, etc.).

    * started to restructure the iOS and Android SDK so that there can be demo apps that showcase and isolate a specific functionality. Right now, the Android app looks more like a demo app--and it's not maintained to be stable. We've started on the iOS one!

    * added docker support and adding CI testing framework for `lightwalletd`. Now you can deploy a lightwalletd server with a simple docker file!

    * gotten feedback from multiple wallet partners on our sdk and lightwalletd server and we’re iterating based on that feedback.

    * In other wallet-related news, [ZecWallet](https://twitter.com/zecwallet/status/1179117062897070080) lightclient CLI is now available for beta testing on Zcash mainnet.  

  * Workshops and events: Daira and Str4d will give two talks at an upcoming[ ZKProof Community Event](https://www.eventbrite.com/e/zkproof-community-event-amsterdam19-tickets-68989889617) in Amsterdam (10/28 - 10/29). Str4d's talk will be on Halo itself, and Daira’s will be an update of hir scaling proposal. 

  * See all Zcash community updates [here](https://forum.zcashcommunity.com/c/weekly-updates).

 **Daniel from Grin**

 _Grin is a community-driven implementation of the Mimblewimble protocol that
aims to be privacy preserving, scalable, fair, and minimal._

  * Merged PRs: [2 in /grin](https://github.com/mimblewimble/grin/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A2019-10-14..2019-10-20+) | [3 in /grin-wallet](https://github.com/mimblewimble/grin-wallet/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A2019-10-14..2019-10-20+) | 3 unique contributors

  * Results of the [Coinspect Security Audit](https://www.grin-forum.org/t/grin-security-audit-2-results/6264) were published. Shout out to Coinspect for their excellent audit work, and to all the grin donors who made it possible in the first place.

  * Call for speakers for grincon1: November 22 in Berlin - [submit your proposal](https://www.grin-forum.org/t/grincon1-call-for-presenters/6250) by Oct 30.

  * Following [grin-wallet beta5](https://github.com/mimblewimble/grin-wallet/releases/tag/v2.1.0-beta.5) all issues are resolved. Release of Grin v2.1.0 for node and wallet is now imminent - likely within a few days of this update being written.

  * Grin v3.0.0 [release planning](https://github.com/mimblewimble/grin-pm/issues/204) issue.

  * [Transaction building over TOR Hidden Services](https://www.grin-forum.org/t/grin-wallet-experimental-tor-integration/6233) merged. Improves privacy during the tx building process, generates a receiving address, and resolves port forwarding / NAT traversal requirements.

  * In the last [development meeting](https://github.com/mimblewimble/grin-pm/blob/master/notes/20191015-meeting-development.md), Security audit publication date, 2.1.0 release, 3.0.0 planning, and release packaging was discussed.

  * Grin is 100% funded by donations. Please support Grin development - [Donate now](https://grin-tech.org/general_funding).

  * More Grin info [here](https://grinnews.substack.com/).

 **Beni from Beam**

 _Beam is a confidential and scalable cryptocurrency based on Mimblewimble._

  * Fantastic time at the [Eurasia Conference](https://www.eurasiablockchain.com/) in Istanbul, Oct. 18-19th 2019

  * Vladislav Gelfer aka [Valdok](https://github.com/valdok), Beam Lead Dev, will be attending [ZK Proof](https://zkproof.org/) in Amsterdam, October 28-29th 2019

  * Clear Cathode Android 3.2 - [Release notes](https://github.com/BeamMW/android-wallet/releases/tag/clear_cathode_3.2)

  * We have 231 open issues in [/ beam](https://github.com/BeamMW/beam/issues), 28 open issues in [/ android-wallet](https://github.com/BeamMW/android-wallet/issues), and 38 open issues in [/ ios-wallet](https://github.com/BeamMW/ios-wallet/issues)

  * We had 50 commits in [/ beam](https://github.com/BeamMW/beam/graphs/commit-activity) and 1 commits on [/ android-wallet](https://github.com/BeamMW/android-wallet/pulse) _ _

#### Smart contracting platforms

 **Evan from[Ethereum](https://weekinethereumnews.com/)**

 _Ethereum  is a decentralized platform for applications that aims to resist
fraud, censorship or third-party interference._

  *  **Eth1**

    * [Special-purpose light clients for old receipts and transactions](https://ethereum-magicians.org/t/special-purpose-light-clients-for-old-receipts-and-transactions/3711)

    * A quick [EIP2124 explainer](https://twitter.com/trent_vanepps/status/1184677267995320322) to help compatible nodes find each other

 **Eth2**

    * [Prysmatic’s client update](https://medium.com/prysmatic-labs/ethereum-2-0-development-update-37-prysmatic-labs-6368654013c5)

 **Layer 2**

    * [Dai Card live on Connext v2](https://medium.com/connext/dai-card-on-connext-v2-0-eed923c52de2). Send Dai back and forth for free.

 **Jing from Plasma**

 _Plasma Group is building "Generalized Plasma", a layer 2 scaling
infrastructure for Ethereum that allows for general state transitions on layer
2._

  * Implemented Uniswap on optimistic rollup as a two-token trading game for DEVCON: [https://unipig.exchange](https://unipig.exchange/)

 **Peter from NEAR**

 _NEAR is a sharded proof-of-stake blockchain._

  * 57 PRs across 16 repos by 24 authors. Featured repos:[ nearcore](https://github.com/nearprotocol/near-wallet),[ nearlib](https://github.com/nearprotocol/nearlib),[ near-shell](https://github.com/nearprotocol/near-shell/),[ near-wallet](https://github.com/nearprotocol/near-wallet),[ near-bindgen](https://github.com/nearprotocol/near-bindgen), [docs](https://github.com/nearprotocol/docs), [NEARStudio](https://github.com/nearprotocol/NEARStudio/), [assemblyscript](https://github.com/nearprotocol/assemblyscript), [near-evm](https://github.com/nearprotocol/near-evm), [borsh](https://github.com/nearprotocol/borsh), [stakewars](https://github.com/nearprotocol/stakewars) and [near-explorer](https://github.com/nearprotocol/near-explorer/);

  * [Show transactions on Block Details page](https://github.com/nearprotocol/nearcore/pull/1450) in [near-explorer](https://github.com/nearprotocol/near-explorer/);

  * [Switch Network for Stake Wars](https://github.com/nearprotocol/near-explorer/issues/110) in [near-explorer](https://github.com/nearprotocol/near-explorer/);

  * [Massive rewrite of networking](https://github.com/nearprotocol/nearcore/commit/16159beec0e92be56adb4ee657550b9dac43e1bb) to support better peer discovery and message routing  in [nearcore](https://github.com/nearprotocol/near-wallet);

  * [Fixing transaction propagation](https://github.com/nearprotocol/nearcore/commit/dbbdfe782c512815078c2f2ed811f44fb49f7aec), [large overhaul of nightshade](https://github.com/nearprotocol/nearcore/commit/bf46cd7bbe1497a19c90f9e9a546f2d8fd2b5541) preparing to implement challenges, [proper logic](https://github.com/nearprotocol/nearcore/commit/e0e0255148868a54f9e75941745ca8a4f24802a1) to retry requesting shard chunks in [nearcore](https://github.com/nearprotocol/near-wallet);

  * [Work on diving state into parts](https://github.com/nearprotocol/nearcore/commit/8e8114ad086f4486274c3e4c7da53488551a8b60) preparing for proper state sync in [nearcore](https://github.com/nearprotocol/near-wallet);

  * [Add a check into Runtime to compare input and output balances](https://github.com/nearprotocol/nearcore/pull/1450) in [nearcore](https://github.com/nearprotocol/near-wallet);

  * [Native test runner to replace docker runner and clean up](https://github.com/nearprotocol/nearcore/pull/1451) in [nearcore](https://github.com/nearprotocol/near-wallet);

  * [Creating a new near compiler frontend](https://github.com/nearprotocol/near-runtime-ts/pull/86) in [near-runtime-ts](https://github.com/nearprotocol/near-runtime-ts);

  * [Updated dependencies](https://github.com/nearprotocol/borsh/pull/25) in [borsh](https://github.com/nearprotocol/borsh);

  * [Set initialBalance for create_account - 1 NEAR](https://github.com/nearprotocol/near-shell/pull/160) in [near-shell](https://github.com/nearprotocol/near-shell/);

 **Topper from Quorum Control**

 _Quorum Control makes Tupelo, a permissionless proof of stake DLT platform
purpose-built to model individual objects that enables flexible public or
private data models._

  * Topper, our CEO, has recently shared a decentralized version of a ridesharing app demo built on Tupelo.  An explanation of “Decentracar” and its key components [can be found here](https://www.tupelo.org/posts/decentracar).   The [github repo for “Decentracar”](https://github.com/quorumcontrol/decentracar) and [demo site](https://quorumcontrol.github.io/decentracar/) supplement the walkthrough.

  * In addition, an article on the related topic of the difference between disintermediation and decentralization in blockchain apps and DLTs [can be found here](https://www.tupelo.org/posts/dlt-isnt-disintermediation). 

  * In our ongoing effort to make it even easier to get started developing with Tupelo, we have migrated to [tupelo.org](http://www.tupelo.org/) and released an improved version of our website.  We also are continuing to bring new examples and content to our [docs site](http://docs.tupelo.org/).

 **Michael from Loom**

 _Loom Network is a universal layer 2 hub. Developers can deploy and scale
their dapps directly on Loom’s mainnet as well as interoperate with other
major layer 1 chains such as Ethereum, Binance, Libra, Bitcoin, etc._

  * Loom is [adding Bitcoin support to Basechain](https://medium.com/loom-network/who-needs-lightning-network-when-you-have-loom-basechain-e21b1f7c107c), giving developers a simple interface to send and receive BTC for zero fees and with instant confirmation times.

  * Axie Infinity went live as [the latest Basechain validator](https://medium.com/axie-infinity/announcing-axies-loom-validator-is-up-4a39151bb06d)

  * Neon District [launches Founder's sale](https://twitter.com/neondistrictRPG/status/1185623247641042945) on Basechain

  * [Strategy game Blocklords](https://twitter.com/loomnetwork/status/1185204285392478209) launches on Basechain

  * [New casino game Crazy House](https://medium.com/loom-network/built-on-loom-crazy-house-a-new-provably-fair-casino-experience-featuring-prizes-509309860064) launches on Basechain

  * Released [support for WalletConnect](https://twitter.com/loomnetwork/status/1181977851538661376)

#### Financial Infrastructure

 **Antonio from dYdX**

 _dYdX is a decentralized exchange for margin trading, borrowing, lending, and
eventually derivatives. dYdX allows traders to trustlessly short and get
leverage on crypto assets._

  * Adding native ETH-USDC and DAI-USDC markets

  * Onboarding market makers. dYdX is now the [most liquid DEX for ETH-DAI](https://twitter.com/dydxprotocol/status/1186344642259738624?s=20)

  * Working on adding trading chart data from our native markets

  * Improving stability of native markets

  * Improving performance & fixing bugs on frontend app

  * [Hiring](https://dydx.exchange/careers/) software engineers & product designers full-time in SF!

#### Layer two and interoperability

 **Tieshun from Namebase**

 _Namebase is the easiest way to buy, sell, and use Handshake._

  * Namebase's CEO Tieshun Roquerre will give a talk on making the Internet more secure with Handshake at SFBW! He'll be speaking at the Epicenter Technical Stage at 2:10pm on 10/31. 

 **Alexandra from Polkadot**

 _[Polkadot](https://polkadot.network/) empowers blockchain networks to work
together under the protection of shared security._

  * Kusama, an early Polkadot release, is [on track for switching to PoS this week.](https://twitter.com/kusamanetwork/status/1186212587610001408)

  * New recording out on [how Polkadot's unique Grandpa consensus algorithm works](https://twitter.com/polkadotnetwork/status/1184741002445316096). 

  * New info up on the wiki on [SPREE](https://wiki.polkadot.network/docs/en/learn-spree) (Shared Protected Runtime Execution Enclaves), also known as "trust wormholes," which allow parachains to trust one another regardless of how they upgrade and evolve.

  * Web3 Foundation is hiring people to [help build Polkadot](https://web3.bamboohr.com/jobs/), as well as [providing grants](https://github.com/w3f/Web3-collaboration/blob/master/grants/grants.md) for software development, research, technical education and community engagement efforts related to Polkadot.

 **Dong Mo from Celer**

 _Celer Network is a layer-2 scaling platform that enables fast, easy and
secure off-chain transactions for not only payment transactions, but also
generalized off-chain smart contracts._

  * We were working on the final checklist for launching async-game.

  * We were designing FIAT solutions for gaming platform.

  * On our backend, we completed the first version of the Celer Web client and continue to test SGN components.

  * We began the design and development of Q4 OSP functionality.

#### Application infrastructure

 **Alexandra from Parity Technologies**

 _Parity  Technologies builds core blockchain infrastructure, from Parity
Ethereum, an Ethereum client, to Polkadot, an interoperable blockchain
network._

  * [Parity devs hacked on Substrate to create Gather,](https://twitter.com/gautamdhameja/status/1185879334227189762) a decentralized meetup platform.

  * [Interview with Benjamin Kampmann](https://www.parity.io/people-of-parity-benjamin-kampmann/), a developer who works on the Substrate blockchain framework.

  * We're hiring! [Check out our jobs.](https://www.parity.io/jobs/#jobs)

 **Matt from Keep Network**

 _The Keep Network is a privacy layer for public chains, enabling
interactivity with private data and interoperability across chains. It does
this with keeps, off-chain containers for private data that help smart
contracts harness the full power of the public blockchain._

  *  **tBTC:**

    * Merged Uniswap on-chain liquidation pathway

    * Zeroed in on a minimum feature set for an initial release

 **Random beacon:  **

    * Finished work on securing broadcast channel for DKG execution; only stakers selected to the group can publish to the channel

    * Implemented additional tests to make sure no duplicate group candidate tickets can be submitted

    * Improved the execution time of our solidity tests, we are about two times faster

    * Made progress on preparing to a public testnet release from the infrastructure side

    * Made progress on pricing implementation but we lost some time on a bug in go-ethereum; we provided a [bugfix](https://github.com/ethereum/go-ethereum/pull/20189), and we hope to finish pricing work this week

    * For more updates and questions join our [Slack](https://join.slack.com/t/keep-network/shared_invite/enQtNTMzMjUwNTUxNjA3LWI2ZjIxNGNmZGMxMTYzYjE0YmY2MjNkNDFkN2JiMDFlYmFkZDIyMzI4ZTZkNmNjZjgwMzVhYjU4YWQ5MjBiYmY) and check out the [Keep blog](https://blog.keep.network/)

 **Ryan from FOAM**

 _FOAM  is building spatial applications and proof of location that bring
geospatial data to blockchains and empower a consensus driven map of the
world._

  * FOAM led successful talks and workshops at DevConV in Osaka on "[Functional Programming in Ethereum](https://slides.com/foam/functional-programming-for-ethereum "https://slides.com/foam/functional-programming-for-ethereum")" and "[Rapidly Deploying an ETH 1.x Application in a Day](https://slides.com/foam/full-stack-eth-app "https://slides.com/foam/full-stack-eth-app")" slides linked 

  * [Announced](https://twitter.com/foamspace/status/1181228190255079424?s=20 "https://twitter.com/foamspace/status/1181228190255079424?s=20") a new platform, FOAM In-Sight in collaboration with Google Cloud Platform, Blocklytics and Chainlink for a hybrid cloud/blockchain application with a demo for DevConV. Main-net next.

  * FOAM participated in the Diffusion Hackathon in Berlin this past weekend with talks, workshops and winning projects building on our stack,[ linked here ](https://twitter.com/foamspace/status/1185970561341632512?s=20 "https://twitter.com/foamspace/status/1185970561341632512?s=20")

  * A [winner](https://twitter.com/blocklytics/status/1179805984233050112 "https://twitter.com/blocklytics/status/1179805984233050112") of The Graph hackathon built on FOAM with a new way of visualizing votes in the TCR via a subgraph.

  * Participating in "A Chain Reaction: Launching an Interchain Interoperability Standard" with Cosmos in Berlin discussing how IBC will be utilized for location services

 **David from Sia**

 _Sia is a decentralized cloud storage platform leveraging blockchain
technology to create a data storage marketplace that is more robust and more
affordable than traditional cloud storage providers._

  * Community member Rishivikram Nandakumar [added a new feature to siac renter setlocalpath](https://gitlab.com/NebulousLabs/Sia/merge_requests/3899) that allows a user to update the localpath of a file being tracked by Sia.

  * Chris [improved the performance](https://gitlab.com/NebulousLabs/Sia/merge_requests/3668) of siac renter unstuckall and added a progress indicator.

  * Matthew [added new functionality](https://gitlab.com/NebulousLabs/Sia/merge_requests/3905) to view stuck directories in siac.

  * Steve announced a new “Built with Sia” brand that all 3rd party apps built with Sia are encouraged to adopt.  You can read the policy and view the assets [here](https://support.sia.tech/article/yh3r6tb68h-brand-guidelines).

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

