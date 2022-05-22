[![](https://substackcdn.com/image/fetch/w_96,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F37b09348-f4f1-47a2-b9e0-a2007299e6e4_256x256)](https://proofofwork.news)

# [Proof of Work](https://proofofwork.news)

SubscribeSign in

Share this post

Proof of Work #67

proofofwork.news

Copy link

Twitter

Facebook

Email

# Proof of Work #67

[Eric Meltzer](https://substack.com/profile/138320-eric-meltzer)

May 21, 2019

[Share](javascript:void\(0\))

Hi from muggy Hong Kong! I first came here when I was a student at Peking
University in Beijing—someone messed up my visa filing, and I was only allowed
to stay in the Mainland for 3 months at a time, so my college periodically
flew me to HK so that I could set foot on “not-China-for-this-particular-
purpose-but-totally-China-otherwise” ground and then come straight back. I
remember pressing my face up against the window of a cab to see the neon
lights of some street in Kowloon through sheets of rain so heavy it felt like
we were underwater, and being ecstatic that there was a city in the world like
this, wide awake at 3AM. Of the two big Asian city-states, I strongly prefer
ultra-capitalist HK to Singapore, and I also particularly love the Bitcoin
scene here, something which I’ll write at length about some other time.

Today I’d like to highlight an [interesting
contribution](https://github.com/JeremyRubin/bips/blob/op-
checkoutputshashverify/bip-coshv.mediawiki) from friend-of-PoW Jeremy Rubin,
both as a cool thing in and of itself, and as an example of how Bitcoin
development works. Bitcoin’s slow adoption of new features is often
misunderstood as Bitcoin development itself being stalled, when actually its
[very active](https://medium.com/@ElectricCapital/dev-report-476df4ff1fd2),
but just unusually conservative in service of keeping Bitcoin chain security
as high as possible.

In this BIP draft, Jeremy proposes a constrained and minimal type of covenant
be added to Bitcoin.
[Covenants](https://fc16.ifca.ai/bitcoin/papers/MES16.pdf) are essentially a
type of restriction on where a given set of coins can be spent. They’re a very
useful smart-contract primitive, which would enable things like “vaults” which
could protect your Bitcoin from being easily spent by someone who got your
private key (details in the linked paper), but have the downside of
potentially enabling someone to mint BTC that can only ever be spent to
specific addresses. There was some worry that this might enable e.g. a nation
state to demand that all BTC held by its citizens enter into covenants that
only allowed it to be spent among pre-approved addresses, for example.

Jeremy’s version of covenants are wrapped with a multisig-based key which can
pre-empt/nullify the covenant. Further, they don’t allow arbitrary ouputs to
be added—all outputs must be specified at construction, which means these
covenants can only be used to expand to a finite number of steps, which
alleviates a lot of the fungibility worries. Finally, in this proposal,
“covenants are restricted to be spendable as a single input only, preventing
the 'half spend' problem.”

These limited covenants get us some pretty neat things, though. First, you can
use them to essentially commit a bunch of future payments in a single
transaction during a time when fees are especially high, and then expand the
payments (confirming them on chain) either in one or multiple tiered steps,
when fees are lower. Similarly you can use them to instantiate a bunch of
channels instead of payments, which allows instant liquidity for the coins
involved. These covenants can also be used to create a construction very
similar to the “vaults” in the initial covenants paper, and also have some
benefits for implementing trustless CoinJoin, a privacy preserving aggregation
technique.

Whether or not Jeremy’s BIP will make it into Bitcoin is unclear at this
point—the proposal is very new and will definitely receive a lot of feedback
and tweaks. However, it’s a great example of how you can add interesting
features to Bitcoin while avoiding compromise of BTC’s core value
proposition—a trustless store of value with high on-chain security. I’ll track
this BIP as it makes its way through the approval process and provide
commentary in future newsletters.

In another interesting development, Veil (a prediction market interface
initially built to execute onto Augur) has forked the Augur codebase and
removed the decentralized oracle part (enabling market creators to choose an
oracle, including the Augur oracle itself, or a centralized one instead) and
thereby have also removed REP. This (ETH projects forking out somewhat
unnecessary ERC20 tokens) is something I expected to see sooner, and I’m very
curious to watch it develop with Veil. A skeptic would say that this move is
likely to end up with a lot of people using centralized oracles, essentially
obviating the need for a blockchain at all—an optimist would say that other
decentralized oracles without tokens will become available, and there will be
increased liquidity as a result of removing the REP requirement. Watch this
space!

Thanks as always for reading—more next week!

#### Bitcoin & Friends

 **Jimmy and[Optech](https://bitcoinops.org/en/newsletters/) on Bitcoin**

  * Proposed anyprevout sighash modes: two weeks ago, Anthony Towns [posted](https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2019-May/016929.html) a proposed BIP to the Bitcoin-Dev and Lightning-Dev mailing lists for consideration. 

  * A [talk](https://diyhpl.us/wiki/transcripts/magicalcryptoconference/2019/crypto-in-cryptocurrency/) by Andrew Poelstra about the cryptography used in cryptocurrencies.

  * A [panel](https://diyhpl.us/wiki/transcripts/magicalcryptoconference/2019/bitcoin-without-internet/) by Rodolfo Novak, Elaine Ou, Adam Back, and Richard Myers about using Bitcoin without direct access to the Internet.

  * A [panel](https://diyhpl.us/wiki/transcripts/magicalcryptoconference/2019/ln-present-and-future-panel/) by Will O’Beirne, Lisa Neigut, Alex Bosworth with moderation by Leigh Cuen discussing the future of LN, mostly the short-term and medium-term conclusion of current development efforts surrounding the LN 1.1 specification.

 **Tony from Kadena**

 _Kadena is building Pact, a formally verifiable smart-contracting language
for financial applications, and Chainweb, a PoW blockchain that uses multiple
chains in parallel to increase throughput._

  * Kadena announced that the [Chainweb Mainnet launch date](https://www.coindesk.com/enterprise-blockchain-kadena-announces-mainnet-launch-this-october) and on boarding of $3 billion ETF fund USCF will take place October 30.

  * Chainweb transaction load generator improvements [PR 194](https://github.com/kadena-io/chainweb-node/pull/194), [PR 196](https://github.com/kadena-io/chainweb-node/pull/196), [PR 200](https://github.com/kadena-io/chainweb-node/pull/200).

  * Chainweb improvements to mempool synchronization performance [PR 202](https://github.com/kadena-io/chainweb-node/pull/202).

  * Full persistence of Chainweb cross-chain consensus [PR 184](https://github.com/kadena-io/chainweb-node/pull/184).

  * Upgrade of Chainweb to full disk persistence for Pact state [PR 187](https://github.com/kadena-io/chainweb-node/pull/187).

  * Pact document capabilities and module governance in reference docs [PR 500](https://github.com/kadena-io/pact/pull/500).

  * Pact full persistence of multi-step "Pact" co-routines [PR 496](https://github.com/kadena-io/pact/pull/496).

  * Founders Stuart Popejoy and Will Martino were interviewed on [CoinDesk Live at Consensus](https://youtu.be/Lv4teJ9gy-Q?t=24009).

  * Will Martino and Tony Pham were interviewed by [Hacker Noon about smart contracts](https://hackernoon.com/smart-contracts-on-blockchain-with-will-martino-and-tony-pham-c05cc9b62bed).

  * Stuart Popejoy was on the [Crypto and Blockchain Talk](http://cryptoandblockchaintalk.com/greatest-minds-of-blockchain-stuart-popejoy-talks-about-evaluating-blockchains-56) podcast to discuss evaluating blockchains.

  * Will Martino spoke on a [Consensus panel about enterprise privacy](https://www.coindesk.com/events/consensus-2019/videos) moderated by Brady Dale.

 **Aviv from Spacemesh**

 _Spacemesh is a programmable cryptocurrency powered by a novel proof-of-
space-time consensus protocol._

  * [ed25591-wasm](https://github.com/spacemeshos/ed25519-WASM) \- New library for using our enhanced ed25591 signatures scheme from node.js / Electron apps such as the Spacemesh App

  * P2P address resolving from [DHT to addrbook](https://github.com/spacemeshos/go-spacemesh/pull/890)

  * ATX [edge case handling](https://github.com/spacemeshos/go-spacemesh/pull/901)

  * Additional [automation framework capabilities](https://github.com/spacemeshos/go-spacemesh/pull/888) in order to test various atx flows

  * Automation framework [prometheus support](https://github.com/spacemeshos/go-spacemesh/pull/872)

 **JZ from Decred**

 _Decred  is an autonomous digital currency with a hybrid consensus system. It
is built to be a self-ruling currency where everyone can vote on the rules and
project-level decision making proportionately to their stake._

  * Marco was showing off [dcrd](https://twitter.com/marco_peereboom/status/1128763544118362112) and [dcrwallet](https://twitter.com/marco_peereboom/status/1130477030594752512) running on RISC-V after getting the Go tooling working. Considering all the x86 CPU exploits popping up lately many of us are very excited about the prospect of being able to run Decred on open hardware.

  * Jake gave a talk at Consensus providing an overview and update on the project. [Brady Dale of Coindesk live-tweeted it](https://twitter.com/BradyDale/status/1128670013974622208) for those who were unable to attend the festivities in New York.

  * Raedah Group has released a [new beta for the Decred wallet for iOS](https://github.com/raedahgroup/dcrios), and it's [available on TestFlight](https://testflight.apple.com/join/7KL4VnB2) for anybody that wants to give it a spin. Feel free to file any issues on GitHub if you run into them.

 **Johnny from Stellar**

 _Stellar is an open network for sending and exchanging value of any kind. Its
global network enables digitization of assets - from carbon credits to
currencies - and enables movement around the internet with ease._

  * [Keybase launches Stellar wallet for all users](https://keybase.io/blog/keybase-stellar-launch), adding integration for federation addresses and Keybase's end-to-end encryption of secrets and messages.

  * Seema Phalke (Lead Developer, IBM Worldwire) [discusses her experience building on Stellar](https://www.youtube.com/watch?v=ksZAjFGGeRU).

  * SatoshiPay discusses Stellar's [increased efforts in decentralization](https://medium.com/@SatoshiPay/stellar-network-growth-and-decentralisation-e99c52ade798).

  * [A new ticker has been released for Stellar](https://medium.com/stellar-developers-blog/a-new-ticker-for-the-stellar-community-4ba7961e0759), providing better data for markets, issuers, and assets.

  * [ZkVM, a new design for fast, confidential smart contracts](https://medium.com/stellar-developers-blog/zkvm-a-new-design-for-fast-confidential-smart-contracts-d1122890d9ae), is now being developed at Stellar.

  * [Stellar Core v11.1.0rc1 has been released](https://github.com/stellar/stellar-core/releases/tag/v11.1.0rc1?utm_source=Stellar.org++News&utm_campaign=f595089d5d-EMAIL_CAMPAIGN_2019_03_08_10_59_COPY_01&utm_medium=email&utm_term=0_563f658d41-f595089d5d-281208849).

  * [New Go SDK v1.2.0 has been released](https://github.com/stellar/go/releases/tag/horizonclient-v1.2.0).

  * 93 pull requests, 53 issues closed in the last two weeks across 8 repositories.

#### Privacy coins

 **Paige & Zooko from Zcash**

 _Zcash is a  digital currency utilizing zk-SNARKs to enable its privacy-
protecting properties._

  * 2.0.5 delayed, anticipate a Monday(5/20) release

  * [Transparency report published](https://z.cash/blog/electric-coin-company-q2-2019-transparency-report/)

  * Full update: <https://forum.zcashcommunity.com/t/may-17-2019-weekly-update-community-comms/33532>

 **Mitchell from Monero**

 _Monero is a open-source, privacy-focused cryptocurrency using the ASIC-
resistant CryptoNote PoW algorithm. It enforces all privacy features at the
protocol level to ensure that all transactions create a single fungible
anonymity pool._

  * The new RandomX PoW algorithm is [ready for you to test](https://github.com/monero-project/monero/pull/5549 "https://github.com/monero-project/monero/pull/5549"), and we're [planning audits](https://repo.getmonero.org/monero-project/ccs-proposals/merge_requests/66 "https://repo.getmonero.org/monero-project/ccs-proposals/merge_requests/66").

  * Continuing to find ways to compress linkable spontaneously anonymous group (LSAG) signatures.

 **Daniel from Grin**

 _Grin is a community-driven implementation of the Mimblewimble protocol that
aims to be privacy preserving, scalable, fair, and minimal._

  * Merged PRs: [10 in /grin](https://github.com/mimblewimble/grin/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A2019-05-13..2019-05-19+) | [4 in /grin-wallet](https://github.com/mimblewimble/grin-wallet/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A2019-05-13..2019-05-19+) | 8 unique contributors

  * grin wallet [1.1.0-beta3](https://github.com/mimblewimble/grin-wallet/releases/tag/v1.1.0-beta.3) released, along side beta2 of the node.

  * @yeastplume has been working on the [samir's secret sharing library](https://www.grin-forum.org/t/yeastplume-progress-update-thread-mar-19-to-sep-19/4303/24)and will be integrating it into wallet.

  * [The latest dev meeting](https://github.com/mimblewimble/grin-pm/blob/master/notes/20190514-meeting-development.md) covered the timeline for 1.1.0 release, scheduled hard fork planning, and deprecation of http transfer support.

  * Proposal by @jaspervdm for [improved bulletproof rewinds](https://github.com/mimblewimble/grin-wallet/issues/105).

  * Proposal by @antiochp for optimising [relative kernel lock heights](https://github.com/mimblewimble/grin/issues/2829).

  * New gitter channel for grin-related [cryptography](https://gitter.im/grin_community/crypto).

  * [Slides from @lehnberg's project overview](https://github.com/mimblewimble/grin-pm/blob/master/presentations/meetups/20190516-GrinMoscow-overview-Lehnberg.pdf) for the first Grin Moscow Meetup are now up.

  * More Grin info [here](https://grinnews.substack.com/).

 **Beni from Beam**

 _Beam is a confidential and scalable cryptocurrency based on Mimblewimble._

  * Quite a busy week for Team Beam with the following releases:

    * [Bright Boson 2.1.4910](https://medium.com/beam-mw/mimblewimble-bb214910-rn-50e7923f8494) \- with some cool privacy-oriented new features and improvements

    * [Bright Boson 2.1.0 Android](https://medium.com/beam-mw/mimblewimble-bb210-android-rn-c1ec9e933b) \- adding here the following features: proof of payment, privacy mode to hide amounts, fingerprint recognition and many more…

    * [Bright Boson 2.2.17 iOS ](https://medium.com/beam-mw/mimblewimble-bb22-ios-rn-dec811be1252)\- third release for our iOS wallet with some super cool new features i.e.: QR code that can include the amount of Beams and the UTXO info that can be hidden in the privacy mode

  * Meet Beam’s CEO Alexander Zaidelson in Moscow at the [Russian Blockchain Week](https://techweek.moscow/blockchain), May the 22nd, 2019

#### Smart contracting platforms

 **Evan from[Ethereum](https://weekinethereumnews.com/)**

 _Ethereum  is a decentralized platform for applications that aims to resist
fraud, censorship or third-party interference._

  * [Everything you need to know about Eth2 through phase 2](https://medium.com/@william.j.villanueva/a-journey-through-phase-2-of-ethereum-2-0-c7a2397a36cb)

  * Using [Eth2 as an Eth1 finality gadget](https://medium.com/@ralexstokes/the-finality-gadget-2bf608529e50)

  * Matter doing over “[100 TPS of ZK transactions on ETH mainnet](https://twitter.com/the_matter_labs/status/1129439834819440641)” but couldn’t test higher because they crashed Digital Ocean

 **Erik from NEAR**

 _NEAR is a sharded proof-of-stake blockchain._

  * 22 total PRs merged or proposed across three repos with 4 authors: [nearcore](https://github.com/nearprotocol/nearcore), [nearlib](https://github.com/nearprotocol/nearlib) and [near-wallet](https://github.com/nearprotocol/near-wallet)

  * NEAR hosted and/or participated in several events for consensus week in NYC. Here are the recorded live streams (youtube versions available next week):

    * [Proof of Stake Protocols and Validators panel](https://www.pscp.tv/w/1MYGNdDkBmnxw?t=39m20s)

    * [Blockchain Gaming in 2019 Panel](https://www.pscp.tv/w/1YpKkvDnvwBxj?t=1h14m43s)

  * The first NEARathon has concluded. Judging and winners announcement here

  * Application/Dev Layer

    * [Implemented economics](https://docs.google.com/document/d/1rydPgSHwPaKQLL57Xogsw8tgjTPKG98cK3kgK_PnjCQ/edit#) that deducts fees directly from the balance instead of using gas/mana

    * Implemented [RLP](https://github.com/ethereum/wiki/wiki/RLP) in [assemblyscript](https://github.com/nearprotocol/assemblyscript-rlp).

    * Added testing to near-runtime-ts.

    * Wallet

      * Completed phone verification UI

      * Integrated phone verification with blockchain

      * Integrated app-specific access keys into the wallet

      * Introduced common request error handling components

    * Nearlib

      * Make continuous integration tests work with shared TestNet

  * Blockchain Layer

    * Big[ refactoring PR](https://github.com/nearprotocol/nearcore/pull/946) of existing consensus to prepare for merge of Nightshade

    * Breaking the[ gigantic research PR](https://github.com/nearprotocol/nearcore/pull/946) on the new consensus into smaller, mergeable PRs

 **AJ from Tezos**

 _Tezos is a self-amending blockchain that features formally verified smart
contracts, on-chain governance, and a proof-of-stake consensus algorithm which
enables all token holders to participate in the network.  _

  * Coinbase CEO, Brian Armstrong, gives an update on the[ performance of Coinbase Custody’s Tezos staking infrastructure](https://twitter.com/brian_armstrong/status/1130508625502441473)

  * T[ezo Asia 2019 - The Future Frontier of Blockchain Technology ](https://www.tezos.org.sg/tezosasia2019/)has been announced. This all day conference will be hosted by Tezos Southeast Asia and Tocqueville Group on June 7th. 

  * Tezos Commons hosted it’s first [Tezos Meetup in India](https://twitter.com/blockchainedind/status/1129724173100736512), Bangalore with over 80 participants attending to learn more about Tezos and the ecosystem. 

  * Tezos first proposal update: The first amendment proposed for Tezos will reach a Quorum of 81.39% this week with the majority voting “yay.” Subsequently, the Tezos protocol will activate the new protocol automatically, signalling the first protocol upgrade in Tezos history from coordination amongst the broad Tezos community. 

**Topper from Quorum Control**

 _Quorum Control makes Tupelo, a permissionless proof of stake DLT platform
purpose-built to model individual objects that enables flexible public or
private data models._

  * Ongoing Optimization of Production Tupelo TestNet

  * Improvements to persistent state through rolling upgrades

  * Substantial performance improvements upgrading libp2p pubsub, fixing a problem with rapid subscriptions

  * [New improved performance results](https://docs.quorumcontrol.com/platform_performance.html) published for v0.2.3 (mean finality in 423 ms with 100 signing nodes at 200 TPS)

  * TestNet upgraded to v0.2.3

  * Read Part 1 of our published posts on NFTs, “[A Taxonomy of NFTs (Collectibles and Assets and Digital Twins, Oh My!)](https://www.quorumcontrol.com/blog/2019/5/17/a-taxonomy-of-nfts-collectibles-and-assets-and-digital-twins-oh-my)”

 **Myles from EOS**

 _EOS is a new blockchain architecture designed to enable vertical and
horizontal scaling of decentralized applications._

  * EOS savings fund (eosio.saving contract) was [burned](https://eosq.app/tx/26ca16319febafc0942a8c6e3be26c16b84846b7cfe5f6ade906a0b86a6c2bb7)

  * EOS New York put forth [a proposal](https://medium.com/eos-new-york/the-missing-piece-to-the-eos-incentive-model-bd39977d243f) to reward and incentivize voters on EOS

  * Dan Larimer published a [new proposal](https://medium.com/@bytemaster/high-liquidity-price-pegged-token-algorithm-d86d71188162) for a highly liquid stablecoin 

  * dGoods (EOS-native NFT standard) [v1.0 released](https://medium.com/dgoods/dgoods-v1-0-public-beta-release-72f896ad7aed)

  * Everipedia published their [EOS UTXO](https://everipedia.org/wiki/lang_en/eosio-utxo/) protocol

  * [Block.one](http://block.one/)'s [June 1st event](https://block.one/june1/) will be live-streamed 

  * We debuted our new bi-weekly [EOS Update](https://eosupdate.substack.com/) newsletter (subscribe for more in-depth updates)

 **Zaki from Cosmos**

 _The  Cosmos Network is a decentralized network of independent, scalable, and
interoperable blockchains._

  * The Cosmos Hub reference implementation was split into it's own repo from the Cosmos SDK. Meet [Gaia](https://github.com/cosmos/gaia).

  * PolychainLabs release [Tenderseed](https://gitlab.com/polychain/tenderseed), a stateless P2P seed node for Tendermint chains.

  * We announced our Seoul [Hackathon](https://blog.cosmos.network/cosmos-hackatom-is-coming-to-seoul-f2cb83172307).

  * Poloniex announced the intention to support Cosmos [staking](https://medium.com/circle-trader/cosmos-atom-staking-is-coming-to-poloniex-d587d6c6615d).

 **Kate and Dean from Agoric**

 _Founded by pioneers in secure development and distributed systems, Agoric
uses a secure subset of JavaScript to enable object capabilities and smart
contracts._

  * Our team grew! We’d like to welcome four new hires: Michael Fig, Chris Hibbert, Tatyana Roberts, and Paul Walton. They will be contributing in engineering, operations, and business development.

  * We’ve been hard at work on our testnet, [building on our “SwingSet” environment](https://github.com/Agoric/SwingSet/).

#### Financial Infrastructure

 **Antonio from dYdX**

 _dYdX is a decentralized exchange for margin trading, borrowing, lending, and
eventually derivatives. dYdX allows traders to trustlessly short and get
leverage on crypto assets._

  * Surpassed $13M in total trade volume on <https://trade.dydx.exchange/>

  * Open sourced a bot to automatically liquidate dYdX accounts and earn the 5% liquidation spread: <https://github.com/dydxprotocol/liquidator>

  * Released a developer documentation page: [https://docs.dydx.exchange](https://docs.dydx.exchange/#/)

  * Designing improvements to our borrowing and cross trading flows.

  * Releasing trade history soon.

  * [Hiring](https://dydx.exchange/careers/) software engineers & product designers full-time in SF!

 **Coulter from MakerDAO**

 _Maker is comprised of a decentralized stablecoin, collateral loans, and
community governance._

  * Latin America Community Lead Mariano DiPietra discussing Dai helping the economy in places like Venezuela

  * Business Development Associate Jennifer Senhaji on stage discussing our 165+ Dai integrations

  * Nik Kunkel, Head of Backend Services, on a panel for decentralized stablecoins

  * Maker COO Steven Becker helped wrap up Consensus 2019 by chatting DeFi on stage with Placeholder VC's Chris Burniske

  * Watch Head of Business Development Greg DiPrisco explain how [Dai will go beyond banks](https://www.youtube.com/watch?v=9lKg6nlyc14)

 **Lazar from MARKET Protocol**

 _MARKET Protocol is a framework for creating tokens that track prices of
traditional or digital assets._

  * Continued progress with our security audit prior to MARKET Protocol mainnet release

  * Added trade order validation flow to MPX UI and checks

  * Implemented new email verification and onboarding screens

  * Migrated from Redis to Postgres database

  * Implemented needed functionality for user notification system

 **Robert from Compound**

 _Compound is a money market protocol on the Ethereum blockchain — allowing
individuals, institutions, and applications to frictionlessly earn interest on
or borrow cryptographic assets without having to negotiate with a counterparty
or peer._

  * Continued alpha-testing Compound v2

#### Layer two and interoperability

 **Paul from Veil**

 _Veil  is a peer-to-peer prediction market and derivatives platform built on
top of Augur, 0x, and Ethereum._

  * Launched markets on the 2020 US Democratic nomination denominated in Dai. [Trade here](https://veil.co/2020).

  * Deployed a custom version of Augur called [AugurLite](https://github.com/veilco/augur-lite) to support Dai markets.

  * Published a [blog post](https://medium.com/veil-blog/augurlite-follow-up-59fefaf240c9) with details about AugurLite and how we use it.

 **Tony from Liquidity.Network**

 _Liquidity Network is a transfer and swap platform for any token_

  * LQD can now be traded on [Uniswap](https://uniswap.exchange/).

  * [New bounty](https://gitcoin.co/issue/liquidity-network/liquidity-burner/1/2972) on Gitcoin! Developers wanting to start with Liquidity can create a Liquidity Burner, a fork of the awesome Burner wallet!

  * Liquidity Canvas competition is back, full details can be found [here.](https://blog.liquidity.network/2019/05/16/liquidity-canvas-competition-is-back/) 

 **Dong Mo from Celer**

 _Celer Network is a layer-2 scaling platform that enables fast, easy and
secure off-chain transactions for not only payment transactions, but also
generalized off-chain smart contracts._

  * We've finished fully decentralized turn-based game and wallet import flow with off-chain state syncing. 

  * We released Alpha Mainnet version. 

  * Operational readiness for ETHNewYork users. 

  * System improvements, bug fixing, and monitoring scripts. 

  * Continue R&D design & planning for end-of-June milestone.

 **Alexandra from Parity Technologies**

 _Parity  Technologies builds core blockchain infrastructure, from Parity
Ethereum, an Ethereum client, to Polkadot, an interoperable blockchain
network._

  * Gavin Wood and Jutta Steiner discussed Polkadot and Substrate on Laura Shin's [Unchained](https://twitter.com/ParityTech/status/1128322927286525952). 

  * Gavin Wood's presentation on ["Governance: What, Why, and How"](https://twitter.com/polkadotnetwork/status/1128737134301667333) is up. 

  * Gautam Dhameja built a Substrate runtime that [allows the addition of validators using proposals or root privileges](https://github.com/gautamdhameja/substrate-poa). 

  * New [People of Parity interview](https://twitter.com/ParityTech/status/1128997644372779008) with Polkadot{.js} creator Jaco Greeff.

  * There's still some Early Adopter tickets left for [Web3 Summit](https://www.web3summit.com/tickets/) during Berlin Blockchain Week.

  * Web3 Foundation is [providing grants to build the Web3 ecosystem](https://github.com/w3f/Web3-collaboration/blob/master/grants/grants.md).

  * [New positions added to our jobs page](https://twitter.com/ParityTech/status/1125721291456172032).

#### Application infrastructure

 **Doug from Livepeer**

 _Livepeer is a decentralized video infrastructure network, dramatically
reducing prices for developers and businesses building video streaming
applications at scale.  _

  * View [this Livepeer and Ethereum Swarm integration](https://www.loom.com/share/3bf9ed1f183d432a96a947420dcbe065) created at EthNewYork, showing video playlists constructed via Livepeer propagated by Swarm's decentralized networking infrastructure.

  * The Streamflow internal testnet achieved 99.7% reliability in a chaos based simulation and 99.97% reliability in a friendly simulation - the march towards a public testnet continues.

  * [Preliminary support for Nvidia GPU based transcoding](https://github.com/livepeer/lpms/pull/114) has been implemented in the Livepeer Media Server.

 **David from Sia**

 _Sia is a decentralized cloud storage platform leveraging blockchain
technology to create a data storage marketplace that is more robust and more
affordable than traditional cloud storage providers._

  * Multiple bug fixes were implemented this week, including some related to the recovery of contracts from backups, redundancy of files and the host-renter negotiation of contracts.

  * The team is finishing some blocking elements necessary for the 1.4.1 release.

  * ChrisSchinnerl started working on Partial Uploads, which will be featured on version 1.4.2. This will allow renters to just upload the changes of a file, instead of the whole file, after each file modification, representing considerable savings for the renter on files frequently updated.

  * Two new S3-compatible API projects, both built on Sia, have launched today. Filebase and Goobox both allow you to easily store files backed by the decentralized cloud. No messing with crypto, no waiting for a blockchain to sync.

  * Community member @Rezant released an online troubleshooting tool for hosts on SiaCentral that attempts to connect to the host and verifies its correct configuration: <https://troubleshoot.siacentral.com/>​

  * Swing by our Discord to keep up with all the latest: <https://discord.gg/sia>

#### Other

 **Sam from OpenBazaar**

 _OpenBazaar is an open source project developing a protocol for e-commerce
transactions in a fully decentralized marketplace._

  * Ethereum precision work continues on server and client side in order to integrate ETH for the upcoming 2.4 release.

  * Lots of behind the scenes work - both development and logistics - to get prepped for the Haven beta launch.

####  **China & Asia Updates**

 **Mining 🔨**

  * WhatsMiner announced its new flagship miner M20 in Hangzhou, with a foundry service from Samsung

  * [Recent BitMain hash rate disclosure](https://blog.bitmain.com/en/hashrate-disclosure/) shows that its SHA256 hashrate is down almost 90% from last month ... 🧐 it is unlikely due to massive farm shut-downs since mining is _super_ profitable now, so most likely a spin-out of its mining business or some other kind of hashrate re-allocation 

  * Another notable personnel update of Bitmain is that its Chief Economist Chuanwei Zhou, recently quit Bitmain to join WxBlockchain. Before Bitmian, Zhou was a researcher at the People’s Bank of China  

 **Trading/Exchanges 💰**

  * There is an [unconfirmed rumor](https://twitter.com/proofofresearch/status/1129650849423286272?s=21) about HitBTC exit scamming, as many have been [experiencing withdrawal issues](https://bitcoinexchangeguide.com/hitbtc-appears-insolvent-blockchain-analysis/) for more than a month 

  * Former BCH team is now working with Coinex on its own public chain, Coinex Chain. Note that Coinex is founded by the former founder of one of the largest BTC mining pools, ViaBTC, who is also a close friend of Jihan 

**Misc**

  * Samsung is going big into both ASIC foundry services for mining and end user blockchain application with its Galaxy 10

  * HTC plans to implement a native Bitcoin full node on its next generation of EXODUS 1s

  * The biggest non-custodial wallet in Asia, ImToken, launched its native DEX in beta, based on both Kyber and 0x. ImToken has close to 10M registered users and is the biggest ERC-20 and ETH wallet in the world 

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

