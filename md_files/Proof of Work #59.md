[![](https://substackcdn.com/image/fetch/w_96,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F37b09348-f4f1-47a2-b9e0-a2007299e6e4_256x256)](https://proofofwork.news)

# [Proof of Work](https://proofofwork.news)

SubscribeSign in

Share this post

Proof of Work #59

proofofwork.news

Copy link

Twitter

Facebook

Email

# Proof of Work #59

[Eric Meltzer](https://substack.com/profile/138320-eric-meltzer)

Mar 21, 2019

[Share](javascript:void\(0\))

Today’s PoW is abbreviated a bit because I’ve been busy with welcoming a new
Bitcoiner into the world. Proof of Baby
[here](https://www.blockchain.com/btc/tx/9439b6de84d4d5d7dd9b990c713d820b451a412cdef325f64cfa95fe43864556?show_adv=true).

More next week… :)

#### Bitcoin & Friends

 **[Optech](https://bitcoinops.org/en/newsletters/2019/03/12/) on Bitcoin [ed:
sign up for their newsletter too! it’s great!]**

  *  **Help test Bitcoin Core 0.18.0 RC2:**  The second Release Candidate (RC) for the next major version of Bitcoin Core has been [released](https://bitcoincore.org/bin/bitcoin-core-0.18.0/). Testing is still needed by organizations and experienced users who plan to run the new version of Bitcoin Core in production. Use [this issue](https://github.com/bitcoin/bitcoin/issues/15555)for reporting feedback.

 **Spy node ban list updated:**  some IP addresses are performing various
attacks that are likely aimed at monitoring transaction propagation so that
they can attempt to determine which nodes originated which transactions. To
help node operators refuse connections from those IP addresses, Gregory
Maxwell maintains a ban list that can be imported into Bitcoin Core and
compatible nodes. There is absolutely no need to use this centralized
list—your fully decentralized node will attempt to connect to a diverse enough
set of peers that it should establish at least one honest connection—but using
this ban list may reduce the amount of traffic you waste on spy nodes and
other bad actors. The list comes in two formats, one for use on the command
line with [bitcoin-cli](https://people.xiph.org/~greg/banlist.cli.txt) and one
that can be pasted into the debug console of [Bitcoin Core
GUI](https://people.xiph.org/~greg/banlist.gui.txt). The blacklisted IP
addresses are banned for one year and Bitcoin Core will remember the bans
between restarts, so you only need to import the list once. Note: some users
have reported that the ban list may exceed the maximum buffer size for the GUI
on some platforms, requiring pasting it in chunks of about 250 entries each in
order to load the whole list.

 **Aviv from Spacemesh**

 _Spacemesh is a programmable cryptocurrency powered by a novel proof-of-
space-time consensus protocol._

  * Hare Protocol [test functions](https://github.com/spacemeshos/go-spacemesh/pull/637) for testing latency and scenarios in real-world network conditions

  * [Containers](https://github.com/spacemeshos/go-spacemesh/pull/641) for testing node scenarios in real-world conditions

  * [New methods](https://github.com/spacemeshos/go-spacemesh/pull/655) for testing network scenarios

  * Basic [GRPC layer](https://github.com/spacemeshos/poet-ref/commit/5cc4ab2a36b4df26c268f8fc911d58a9c800b676) for communication with POET server

  * App - [derive wallet file encryption key](https://github.com/spacemeshos/smapp/pull/36)

  * App - new wallet [core features](https://github.com/spacemeshos/smapp/pull/39)

  * App - Additional new features [merged PRs](https://github.com/spacemeshos/smapp/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Aclose)

  * Full update <https://spacemesh.io/weekly-updates/> 

 **JZ from Decred**

 _Decred’s vision is to build a self-directed, decentralized future ruled by
the collective intelligence of the community. It will be built upon the
pillars of sovereignty, transparency, inclusivity, privacy, and security.
Everyone can vote on the rules and project-level decision making
proportionately to their stake, yielding decisions and policies in the best
interest of all — not just a select few.  _

  * A new consensus vote has begun to enable Lightning Network to work on Decred by activating [DCP-0004](https://github.com/decred/dcps/blob/master/dcp-0004/dcp-0004.mediawiki). Stakeholders are encouraged to [set their vote bits in Decrediton or dcrwallet](https://docs.decred.org/governance/consensus-rule-voting/how-to-vote/) so they can participate. The vote can be [monitored here](https://voting.decred.org/).

  * New issue of [Politeia Digest covering March 1-14](https://medium.com/politeia-digest/issue-12-mar-1-mar-14-2019-bc77f1cfca8f) on Decred's Politeia governance platform. 1 new proposal submitted, 6 proposals finished voting (5 accepted, 1 rejected).

  * A wild fiat pair appears... We're extremely pleased to announce that [OKCoin has listed Decred](https://www.okcoin.com/market#product=dcr_usd) and is providing us our first DCR/USD pair along with BTC and ETH pairs. [Read more about it here](https://medium.com/@OKCoin/decred-dcr-now-listed-on-okcoin-a7ea9adea7b7).

  * The [Wall Street Journal published a nice overview piece on Decred](https://www.wsj.com/articles/gerons-take-decred-aims-to-reach-cryptos-decentralized-ideals-11552523191?emailToken=cb3b61375ed0a00da464e7cc3612d038yrCaz57a1y%2B%2BZHR0nDW7zHyhh2LjFszoo1ISaf3OZwHq9qBf6mjPrhpyQd1Rw8EcEnqwLrFJ93nsp00hoeTonWwqyyVdVmOXKZ9Q3hCjdpvhcxOEyMqHKMBsFEce/9fg) which includes some quotes from project lead Jake Yocom-Piatt.

 **Johnny from Stellar**

 _Stellar is an open network for sending and exchanging value of any kind. Our
global network enables digitization of assets - from carbon credits to
currencies - and enables movement around the internet with ease. In doing so,
it’s faster, cheaper, and more environmentally friendly than alternative
platforms, and it empowers users and organizations to create a global,
dependable network of trust while maintaining decentralization._

  * [Core: Stellar Core 10.3.0 has been released.](https://github.com/stellar/stellar-core/releases/tag/v10.3.0) Includes large performance improvements when nodes first join the network (primarily due to database optimizations). Version 11 in up next.

  * [Horizon: Horizon 0.17.4 has been released](https://github.com/stellar/go/releases/tag/horizon-v0.17.4). Includes compatibility with Stellar Core 10.3.0.

  * Platform: Go SDK, txnbuild, and other platform tools have seen major improvements in the last few weeks. [Take a look at what we're up to](https://github.com/orgs/stellar/projects/4).

  * Protocol Updates: [CAP-0017](https://github.com/stellar/stellar-protocol/blob/master/core/cap-0017.md) accepted, [CAP-0018](https://github.com/stellar/stellar-protocol/blob/master/core/cap-0018.md) FCP, many additional drafts. [New process for adding protocol changes here](https://github.com/stellar/stellar-protocol/blob/master/README.md).

  * Stellar Development Foundation: [New Stellar Logo](https://www.stellar.org/blog/announcing-the-new-stellar-logo/), [Denelle Dixon](https://www.stellar.org/blog/why-im-joining-stellar/) (Mozilla COO) [joins as SDF's Executive Director & CEO](https://www.prnewswire.com/news-releases/the-stellar-development-foundation-appoints-denelle-dixon-previously-mozilla-coo-as-executive-director-and-ceo-300812763.html).

 **Izaak from Coda**

 _Coda is the first cryptocurrency protocol with a constant-sized blockchain.
Coda compresses the entire blockchain into a tiny snapshot the size of a few
tweets using recursive ZK-snarks_

  * Echo began [hooking in](https://github.com/CodaProtocol/coda/pull/1849) the trust and peer-banning mechanism.

  * Jiawei has been [fixing](https://github.com/CodaProtocol/coda/pull/1856) [bugs](https://github.com/CodaProtocol/coda/pull/1857) and writing several integration tests.

  * Paul has been [making](https://github.com/CodaProtocol/coda/pull/1886) [sure](https://github.com/CodaProtocol/coda/pull/1887) [all](https://github.com/CodaProtocol/coda/pull/1858) network communication will be backwards compatible across protocol upgrades.

  * Matt has made numerous improvements in snarky, including adding a [generic conditional](https://github.com/o1-labs/snarky/pull/131).

#### Privacy coins

 **Paige & Zooko from Zcash**

 _Zcash is a  privacy-protecting, digital currency built on strong science._

  * Draft ZIPs for NU3 (the network upgrade after Blossom) are due by the end of the month

  * Blossom spec auditing underway next week

  * Continued implementation work on Sprout -> Sapling migration tool and the automatic counterfeiting plan

  * Open sourced reference wallet code

  * Full update here: <https://forum.zcashcommunity.com/t/march-15-2019-weekly-update-engineering/32911>

 **Mitchell from Monero**

 _Monero is a open-source privacy-focused cryptocurrency, maintained by a
grassroots community of volunteers and crowdfunded contributors since 2014.
Monero uses an ASIC-resistant CryptoNote PoW algorithm, and enforces all
privacy features at the protocol level to ensure that all transactions create
a single fungible anonymity pool._

  * We’re reviewing a recent proposal to create [shorter MLSAGs](https://github.com/monero-project/research-lab/issues/52) with hidden amounts.

  * [Monero Koferenco](https://monerokon.com/) is going to be hosted in Denver, CO, USA on 22-23 June. There’s still room for a few more[ conference speakers](https://monerokon.com/speaker-list), so please[ submit an abstract](https://monerokon.com/call-for-papers).

  * The [hashrate has remained stable](https://www.coinwarz.com/network-hashrate-charts/monero-network-hashrate-chart) at ~250 MH/s since [last week’s network upgrade](https://ww.getmonero.org/downloads/ "https://ww.getmonero.org/downloads/"), which switched to the [CryptoNightR](https://github.com/monero-project/monero/pull/5126) variant with ASIC-incompatible random integer math.

  * We’re discussing a recent proposal for a [bitmessage-style messaging protocol](https://github.com/monero-project/research-lab/issues/51) for Monero addresses, which is metadata free since no information about the sender or receiver is included, and the message is simply the ciphertext, which each user tries to decrypt with their own keys.

 **Daniel from Grin**

 _Grin is a community-driven implementation of the Mimblewimble protocol that
aims to be privacy preserving, scalable, fair, and minimal._

  * [11 Pull Requests were merged](https://github.com/mimblewimble/grin/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A2019-03-11..2019-03-17+) in the past week, by 8 unique contributors.

  * @yeastplume has been busy [hammering away on grin-wallet](https://www.grin-forum.org/t/yeastplume-progress-update-thread-mar-19-to-sep-19/4303/9). Slate versioning and conversions. API v2, and more.

  * @bddap has been making [Wallet API v2 contributions](https://github.com/mimblewimble/grin-wallet/pull/2).

  * The [governance meeting](https://github.com/mimblewimble/grin-pm/blob/master/notes/20190312-meeting-governance.md) approved a 3 month donation for Ignotus Peverell to work full-time on the project.

  * We're [evaluating our current security and vulnerability disclosure process](https://www.grin-forum.org/t/please-help-evaluate-grins-security-process/4537).

  * [Knockturn Allee](https://cycle42.com/knockturn) \- Open source WooCommerce/WordPress plugin to help businesses accept Grin payments, by Cycle42.

  * [grin.report](https://grin.report/) \- New site for grin network performance stats, by @mcdallas.

  * [Grin Amsterdam event](https://www.grinamsterdam.com/) is taking place on March 26th - come join us there!

  * More Grin info [here](https://grinnews.substack.com/).

 **Beni from Beam**

 _A confidential and scalable cryptocurrency based on Mimblewimble._

  * [UTXO set, horizons and cut through](https://github.com/BeamMW/beam/wiki/UTXO-set,-horizons-and-cut-through)

  *  Add API to send specific UTXO [#502](https://github.com/BeamMW/beam/issues/502)

  *  Transaction in "Waiting for receiver" status should be able to live 12 hours [#473](https://github.com/BeamMW/beam/issues/473)

  * Node Explorer: Store the logs in "logs" folder [#514](https://github.com/BeamMW/beam/issues/514)

  * Bug Wallet Fix  [#529](https://github.com/BeamMW/beam/issues/529)

  * [Blockchain Explorer](https://github.com/BeamMW/blockex/releases/tag/explorer_2.0)

  *  Atomic Swap CLI [#447](https://github.com/BeamMW/beam/issues/447)  _in progress_

  * Fast Sync [#454](https://github.com/BeamMW/beam/issues/454) _  in progress_

  * [Android wallet ](https://github.com/BeamMW/android-wallet)Mainnet  _in progress_

  * [iOS  wallet ](https://github.com/BeamMW/ios-wallet/projects/1)Testnet   _in progress_

  * Hardware wallet - Trezor  _in progress_

 **Arnaud from AZTEC Protocol**

 _AZTEC Protocol is an efficient zero-knowledge protocol built on top of
Ethereum, making plug-and-play value transmission and asset governance privacy
tools for developers and companies.  _

  * We are preparing for our full audit, with the focus being on finalising APIs, bug fixing, writing documentation and general cleanup. We merged [3 pull requests](https://github.com/AztecProtocol/AZTEC/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A2019-03-10..2019-03-17+) this week along those lines.

  * Ongoing feature work this week includes: 

    * [Improved proof versioning](https://github.com/AztecProtocol/AZTEC/pull/68) (to allow for upgradability of the proof verifiers through consent of assets which use AZTEC)

    * [Minting and burning in fully private assets](https://github.com/AztecProtocol/AZTEC/tree/feat-mint-and-burn/packages/protocol/contracts/ACE/validators/mint)

  * Our CTO Zac Williamson presented [a deep dive into AZTEC](https://www.youtube.com/watch?v=ykXvg7yirSA) at ETHCC

  * We’re hiring for **two cryptographers** and **one senior engineer** to join the team. You can apply [here](https://angel.co/aztec-protocol-3/jobs), or by emailing [arnaud@aztecprotocol.com](mailto:arnaud@aztecprotocol.com) with the name of the role as the subject.

#### Smart contracting platforms

 **Evan from[Ethereum](https://weekinethereumnews.com/)**

 _Ethereum  is a decentralized platform for applications that run exactly as
programmed without any chance of fraud, censorship or third-party
interference._

  * Latest issue of [what’s new in eth2](https://notes.ethereum.org/c/Sk8Zs--CQ/https%3A%2F%2Fbenjaminion.xyz%2Fnewineth2%2F20190315.html)

  * Connext’s [DaiCard](https://medium.com/connext/introducing-the-dai-card-fc46520078d3) launches on mainnet. Instant Dai payments over state channels. Limited to $30 right now as it is still beta.

  * Vitalik Buterin “[scalable blockchains as data layers](https://www.youtube.com/watch?v=mOm47gBMfg8&feature=youtu.be)” talk at Taipei meetup on getting 270,000 transactions per second through zk rollups

 **Erik from NEAR**

 _NEAR is a sharded proof-of-stake blockchain that enables great usability for
both developers and their end-users._

  * 25 PRs in [nearcore](https://github.com/nearprotocol/nearcore) from 10 different authors ([weekly digest for 3/3-3/13](https://github.com/nearprotocol/nearcore/issues/715)).

  * New Whiteboard Series episode with [Stan Kladko SKALE Labs](https://www.youtube.com/watch?v=XwqmnaPHsX8&list=PL9tzQn_TEuFWweVbfTbaedFdwVrvaYPq4&index=9)

  * Blockchain Layer:

    * Stabilizing TestNet “Alpha”: [reactive catchup for blocks](https://github.com/nearprotocol/nearcore/pull/699) and bug fixes.

    * [Caching authority computation](https://github.com/nearprotocol/nearcore/pull/671) to speed up startup time

  * Application / Development Layer:

    * Continued work on [improving](https://github.com/nearprotocol/nearcore/pull/726) receipts for cross-contract calls.

    * Deployed [new docs](https://docs.nearprotocol.com/).

 **AJ from Tezos**

 _Tezos is a self-amending blockchain that features formally verified smart
contracts, on-chain governance, and a proof-of-stake consensus algorithm which
enables all token holders to participate in the network.  _

  * Introducing a new smart contract langauge for Tezos, Ligo. LIGO is a simple smart contract language designed for developing longer contracts than one would naturally write in Michelson. It is an imperative language that compiles down to clean Michelson code, featuring a Pascal-like syntax and a simple type system.

  * Tezos smart contract initiatives announced so far in 2019: SmartPy.io, Ligo, ConseilJS, Liquidity 1.0 with ReasonML toggle, and Fi. 

  * [Prestigious Thai University, Chulalongkorn University, has partnered with Tezos Southeast Asia](https://en.prnasia.com/releases/apac/chulalongkorn-university-teams-up-with-tezos-southeast-asia-to-launch-thailand-s-leading-blockchain-academic-initiative-239630.shtml) to create the nation’s premier blockchain education and research programme. 

  * Tezos 101: B9labs has launched its free Tezos introductory development course, sign up [here](https://academy.b9lab.com/courses/course-v1:B9lab+TEZ-101+2019-03/about)

  * [TQ will be hosting a ‘Tezos Day’ event on April 18th](https://twitter.com/TQTezos/status/1105975343892983808) in Paris during Paris Blockchain Week.

 **Topper from Quorum Control**

 _Tupelo is a permissionless proof of stake DLT platform purpose-built to
model individual objects that enables flexible public or private data models._

  * We spoke at this year’s [NFT.NYC](http://nft.nyc/) conference in February. Hear our full talk _“[Moving NFT Checks Off Chain](https://www.quorumcontrol.com/blog/2019/3/6/moving-nft-check-off-chain)”_

  * We made scalability and efficiency improvements to our gossip protocol

  * We introduced more flexible and configurable storage options for data that interacts with the platform

 **Michael from Loom**

 _Loom Network is a platform for building highly scalable DPoS sidechains to
Ethereum, with a focus on large-scale games and social apps._

  * Over 100M LOOM [now staked on PlasmaChain](https://dashboard.dappchains.com/), around 15% of the circulating supply.

  * [Integrated the top 100 ERC20 tokens](https://medium.com/loom-network/plasmachain-integrates-with-top-100-erc20-tokens-enabling-lightning-fast-layer-2-stablecoin-fb9c99e879d4) on PlasmaChain, including major stablecoins DAI, USDC, TUSD, PAX, GUSD, and EURS.

  * 2 more external validators went live on PlasmaChain -- [Bixin](https://bixin.com/) and [Hey Network](https://www.hey.network/)

  * Launched BNB payments and released [limited edition Zombie Battleground Card Packs](https://twitter.com/cz_binance/status/1105764401045364736) with a [chance to win $10,000 in BNB prizes](https://loom.games/en/binance-promo/).

 **Myles from EOS**

 _EOS is a new blockchain architecture designed to enable vertical and
horizontal scaling of decentralized applications._

  * [EOSIO v1.7.0](https://github.com/EOSIO/eos/releases/tag/v1.7.0) was released 

  * EOS Rio's [Hyperion History API](https://medium.com/@eosriobrazil/presenting-hyperion-history-api-solution-f8a8fda5865b) went live (listen to [our interview](https://eosvoter.transistor.fm/episodes/hyperion-history-api-with-eos-rio) with the team!) 

  * EOS Weekly released a [fantastic video](https://www.youtube.com/watch?v=kTjF0-Edxw8) explaining the brilliant EOSIO accounts and permission systems 

  * dfuse released new [contract debugging tools](https://www.dfuse.io/en/blog/debug-like-a-pro-as-in-production-with-console-outputs)

 **Zaki from Cosmos**

 _The  Cosmos Network is a decentralized network of independent, scalable, and
interoperable blockchains, creating the foundation for a new token economy._

  * Cosmos community launched the mainnet for the Cosmos Hub with the suggested allocation of ATOMs from the fundraising process: <https://cosmos.network/launch> 67 validators participated in launch and stability was achieved within minutes of the expected genesis time.

  * More than 70 million of 238 million atoms have been staked. I am super pleased that 3 of the top 10 validators were not participants in the fundraiser.

  * What next? [The Hub might halt and recove](https://blog.cosmos.network/the-4-classes-of-faults-on-mainnet-bfabfbd2726c)r. The Hub might vote for a software upgrade that enables [transfers](https://blog.cosmos.network/the-3-phases-of-the-cosmos-hub-mainnet-fdff3a68c4c0).

  * Look for governance proposals [here](https://hubble.figment.network/chains/cosmoshub-1/governance). I'm surprised there hasn't been one.  
Work is in progress on the next
[Tendermint](https://github.com/tendermint/tendermint/milestone/23) and
[Cosmos Hub software release](https://github.com/cosmos/cosmos-
sdk/milestone/13) but no upgrades on Hub will happen without governance.

 **Kate and Dean from Agoric**

 _Founded by pioneers in secure development and distributed systems, Agoric
uses a secure subset of JavaScript to enable object capabilities and smart
contracts._

  * Agoric began work on a new "Vat" implementation, codenamed SwingSet, to use techniques from the [KeyKOS](https://en.wikipedia.org/wiki/KeyKOS) operating system and apply them to [SES-confined JavaScript execution](https://github.com/Agoric/SES). Github repo [here](https://github.com/Agoric/SwingSet). 

  * Kate was a guest on the free software podcast Libre Lounge, [talking about Object Capabilities](https://librelounge.org/episodes/episode-13-object-capabilities-with-kate-sills.html). 

  * We [created a website](https://agoric.com/safe-modules/) for our safe modules program for JavaScript. More on this to come. 

#### Financial Infrastructure

 **Antonio from dYdX**

 _dYdX is a decentralized exchange for margin trading, borrowing, lending, and
eventually derivatives. dYdX allows traders to trustlessly short and get
leverage on crypto assets._

  * Gearing up for the alpha launch of our new margin trading product

  * Testing internally on Kovan Testnet

  * Wrapping up security audit with Open Zeppelin

  * [Hiring](https://boards.greenhouse.io/dydx) software engineers and product designers full-time in SF!

 **Brendan from Dharma**

 _Dharma is the easiest place to borrow and lend cryptocurrencies. We enable
non-custodial peer-to-peer lending through smart contracts on Ethereum._

  * R

 **Coulter from MakerDAO**

 _Maker is unlocking the power of the blockchain for everyone by creating an
inclusive platform for economic empowerment -- allowing equal access to the
global financial marketplace._

  * The vote to raise the Stability Fee to 3.5% passed and went into immediate effect. We encourage anyone to join our Governance & Risk calls where these are discussed.

  * For PiDay (3/14), we worked with @SendCrypto to create [#PiDai for #PiDay](https://blog.makerdao.com/pidai-for-piday/), where anyone could send Dai to charities, just by tweeting. 

  * Helena Network became the first project to create a [dapp on the xDai sidechain](https://media.consensys.net/prediction-markets-platform-becomes-first-dapp-on-xdai-sidechain-f26e6d691799), bringing their prediction markets platform a better UX.

  * Connext [released Dai Card](https://medium.com/connext/introducing-the-dai-card-fc46520078d3), a browser-based wallet for low cost payments instantly in Dai. 

 **Lazar from MARKET Protocol**

 _MARKET Protocol is a framework for creating tokens that track prices of
traditional or digital assets, providing financial access to anyone._

  * Another big week! We have a full version of MPX up and running for internal testing

  * Implemented Error logging across dev, staging, and production environments

  * Completed work on admin panel API, now focused on user account API

  * Completed user account design flows for new & returning users

  * Lots of bug stomping across APIs, admin, & DEX

 **Robert from Compound**

 _Compound is a money market protocol on the Ethereum blockchain — allowing
individuals, institutions, and applications to frictionlessly earn interest on
or borrow cryptographic assets without having to negotiate with a counterparty
or peer._

  * No update this week.

#### Layer two and interoperability

 **Tieshun from Namebase**

 _Namebase is the easiest way to buy, sell, and use Handshake._

  * No updates this week.

 **Paul from Veil**

 _Veil  is a peer-to-peer prediction market and derivatives platform built on
top of Augur, 0x, and Ethereum._

  * Launched market creation feature. Now any Veil user can create their own prediction market and collect bets for free. [Read more about the feature](https://medium.com/veil-blog/create-your-own-prediction-market-d41ec7c19675) or [create your own market now](https://veil.co/create). We’ve already seen people create markets on the [future Celer token price](https://app.veil.co/market/what-will-be-the-celer-token-price-after-the-1st-hour-of-trading-at-binance-1050cbbf), [Andrew Yang’s Twitter followers](https://app.veil.co/market/will-2020-presidential-candidate-andrew-yang-have-250-000-or-more-twitter-followers-on-april-1-2019-37458e3c), and [Boeing’s 737 Max grounding](https://app.veil.co/market/will-faa-revert-boeing-737-max-8-grounding-decision-before-30th-march-2019-ac0f59c3).

  * Added  feature, so users can respond to markets by liking them as well as betting in them.

  * Revamped home page to make it easier to filter markets by category and sort by volume or likes. [Go to home page](https://app.veil.co/).

 **Rahul from 0x**

 _0x_  is an open protocol that enables the peer-to-peer exchange of assets on
the Ethereum blockchain.

  * New [Relayer Report](https://blog.0xproject.com/relayer-report-19-extension-contracts-ethfinex-on-v2-and-tokenary-interview-48c040659773), covering the Ethfinex V2 switch and an interview with Tokenary

  * ZEIP-23 is [live on mainnet](https://blog.0xproject.com/zeip-23-vote-post-mortem-311c9323e228): trade arbitrary bundles of tokens

  * [Announcing the addition](https://twitter.com/0xProject/status/1107674943917981696) of Daniel Pyrathon to the 0x Core Team 

 **Tony from Liquidity.Network**

 _Transfer and Swap Platform for any Token_

  * Bug fixing on [client library](https://docs.liquidity.network/), which is fully compatible with all major browsers

  * Revive [Liquidity Canvas](https://canvas.liquidity.network/) 

  * Liquidity Faucet included on coming V2 mobile app

 **Dong Mo from Celer**

 _Celer Network is a leading layer-2 scaling platform that enables fast, easy
and secure off-chain transactions for not only payment transactions, but also
generalized off-chain smart contract. It enables everyone to quickly build,
operate, and use highly scalable decentralized applications through
innovations in off-chain scaling techniques and incentive-aligned
cryptoeconomics._

  * We continued on our design and implementation of the CelerX platform. 

  * Investigation of OSP performance with a larger number of users.

  * Design enhancements for OSP protocol and system storage.

\- We finished the following CelerX game UI: game menu, history, history
detail and quick match.

\- We continue to fixed bugs and improve stability.

 **Alexandra from Parity Technologies**

 _Parity  Technologies builds core blockchain infrastructure. From Parity
Ethereum, the most advanced Ethereum client, to Polkadot, the next-generation
interoperable blockchain network._

  * New [PolkaDAO](https://twitter.com/polkadotnetwork/status/1104015102657863680), a user-led platform for the Polkadot community

  * Initial version of [off-chain worker threads](https://twitter.com/gavofyork/status/1103691351756062720) for Substrate

  * First draft of [Universal Offline Signatures](https://twitter.com/MaciejHirsz/status/1105510966547095552) for Parity Signer

  * New: [Polkadot research hub](https://twitter.com/polkadotnetwork/status/1106334700329668611)

  * New guide: [How to build a (simple) Token Curated Registry DAppchain](https://twitter.com/ParityTech/status/1106525949686886401) using Substrate.

  * Substrate has a subreddit: [/substrate](https://www.reddit.com/r/substrate/)

  * [Polkawallet released their 0.1.0 beta version](https://twitter.com/polkadotnetwork/status/1104005799909703682) featuring asset management, staking, democracy, and more.

  * Interested in building on Polkadot? The Web3 Foundation is [providing grants.](https://www.parity.io/jobs/)

  * Like talking to devs and traveling? [We're hiring a Tech Ambassador.](https://twitter.com/ParityTech/status/1101052488344653824)

#### Application infrastructure

 **Wes from Theta**

 _Theta is an end-to-end infrastructure for decentralized video streaming._

  * Theta mainnet successfully launched on March 15th

  * Exchange integration with mainnet expected to wrap up early to mid-week

  * Theta Fuel (operational/gas token of the protocol) distributed to all Theta tokenholders on mainnet

  * Announced partnership with MovieBloc startup to distribute movies + other video content

 **Doug from Livepeer**

 _Livepeer is a decentralized video infrastructure network, dramatically
reducing prices for developers and businesses building video streaming
applications at scale.  _

  * Active contributions from collaborators Epic Labs on [a classifier to very non-deterministic GPU video transcoding](https://github.com/livepeer/verification-classifier). 

  * In an effort to continuously increase reliability of the network for the Streamflow release, work continued on the orchestrator failover and redundancy strategies for video broadcasters.

  * On the research track, we explored [a multi-registry construction](https://github.com/livepeer/research/issues/26) for nodes on the network, in an effort to aid double-spend prevention in probabilistic micropayments and make additional services available on the Livepeer network.

  * Network participation surpassed 31% of LPT actively staked.

 **Ryan from FOAM**

 _FOAM  is building spatial applications and proof of location that bring
geospatial data to blockchains and empower a consensus driven map of the
world._

  * Hosted a talk on The Importance of Time Synchronization by way of historical examination and updates on Proof of Location Developments, video [here](https://t.co/biWwS4HxLz "https://t.co/biWwS4HxLz"). 

  * Progress on time sync simulations on our local test net and Tendermint based MVP as well as on the custom firmware we are developing for the radio nodes. 

  * Leaderboard moving out of beta with 3Box web3 identities now integrated 

 **David from Sia**

 _Sia is a decentralized cloud storage platform leveraging blockchain
technology to create a data storage marketplace that is more robust and more
affordable than traditional cloud storage providers._

  * The path towards the final 1.4.0 release: The public testing of the latest Release Candidate 3 has revealed issues for renters using the Windows version. The team is currently working in their correction:  
\- DavidVorick identified a misuse of the Sia paths in multiple parts of the
code, that while compatible with Unix systems, are incorrect on Windows  
\- eddiewang is finishing the last 2 tasks from a list of 8 issues identified
on the UI: a problem of stuck uploads on the UI and the correction of paths on
Windows

  * Bug fixes and other improvements  
\- A bug that could throw a panic error while shutting down Sia, repaired by
ChrisSchinnerl  
\- Two bugs related to writing logs during file repair checks, corrected by
ChrisSchinnerl and DavidVorick  
\- An optimization during file chunk repairs, by MSevey  
\- eddiewang updated the contents of the Sia website, as links to the Sia blog
and the Sia Youtube channel. Also, some biographies of the team were corrected
by stevefunk

  * Stats  
\- 3 Nebulous repo were updated. 5 issues were created, 2 were closed. 7 MRs
were merged.  
\- GitLab users stevefunk, zherbert, eddiewang, ChrisSchinnerl, MSevey and
DavidVorick had code contributions merged into Sia.

  * From the community: Decentralizer 1.0  
The community member [@hakkane](https://web.telegram.org/#/im?p=%40hakkane)
released the UI version of Decentralizer and the updated 1.0 version of its
CLI tool. Decentralizer is an app that allows renters to micro-manage their
contracts, detect and avoid hosting farms, manual selection of hosts, and geo-
fencing. It is free and open source: <https://keops.cc/decentralizer>

#### Other

 **Ari from Decentraland**

 _Decentraland is a virtual world where you can build and explore 3D
creations, play games and socialize._

  * No update this week.

 **Bowen from Hydro/DDEX.io**

 _Hydro  Protocol is an open source framework for building Decentralized
Exchanges. DDEX is the first decentralized exchange for Ethereum and ERC-20
tokens built on the Hydro Protocol. _

  * Hydro Contract update 1.1 : Remove EIP 712 Domain, Add isMakerOnly field, Update makerRebateRate logic,    
- 0xE2a0BFe759e2A4444442Da5064ec549616FFF101 

  * Hydro Relayer Starter Kit - Read.me ready, ETA Launch by the end of March 

  * Mutli Chain Wallet in Development - Flexible framework to support more Public chains, ETA 4/18  

 **Sam from OpenBazaar**

 _OpenBazaar is an open source project developing a protocol for e-commerce
transactions in a fully decentralized marketplace._

  * 2.3.1 release candidate testing has found some bugs relating to the IPFS rebase. Data migrations weren't handled properly and are being fixed now. We're working on a 5th release candidate now.

  * An external audit for an OpenBazaar token smart contract that controls a major aspect of token distribution was completed and only minor issues found. They are being resolved now.

  * Development on the Haven mobile app continues. The 2.3.1 rebase is needed for the social and messaging aspects of the app and is expected to speed up parts of the app significantly.

 **Martín from Zeppelin**

 _Zeppelin builds tools for the secure development, deployment and operation
of decentralized systems. We also help companies secure their systems by
performing security audits._

  * Ramon Recuero wrote [Bootstrapping a Developer Ecosystem with Zeppelin](https://blog.zeppelin.solutions/bootstrapping-a-developer-ecosystem-with-zeppelin-39d8e75847e1) explaining why Zeppelin provides a strong foundation to kickstart an ecosystem of decentralized systems

  * Zeppelin & TabooKey announced the [Gas Station Network Alliance](https://blog.zeppelinos.org/gas-station-network-alliance/)

  * Released [OpenZeppelin 2.2.0](https://forum.zeppelin.solutions/t/openzeppelin-2-2-0/408)!

  * Ramon Recuero [announced the ZepKit](https://blog.zeppelinos.org/introducing-zepkit/) and Dennison wrote an [introductory guide](https://blog.zeppelinos.org/getting-started-with-zepkit/?utm_campaign=zos-technical-zepkit&utm_medium=newsletter&utm_source=pow) for it!

  * Santiago Palladino published the [ZeppelinOS Feb 2019 development update](https://forum.zeppelin.solutions/t/february-2019-development-update/346/2)

  * Leo Arias shared his [ERC20Snapshot for OpenZeppelin draft review](https://forum.zeppelin.solutions/t/draft-review-erc20snapshot/302)

  * Leo Arias wrote a [quality checklist for smart contracts before an audit](https://blog.zeppelin.solutions/follow-this-quality-checklist-before-an-audit-8cc6a0e44845)

  * Dennison Bertram [hosted a live coding workshop with the community](https://twitter.com/DennisonBertram/status/1101145475741347840) in New York and another one in [Paris during ETHCC](https://www.eventbrite.com/e/zeppelinos-live-coding-workshop-learn-zepkit-upgradability-evm-packages-and-transparent-proxies-tickets-57537635617)

  * The Zeppelin team went to ETHDenver and Dennison wrote a [recap and bounty Winners](https://blog.zeppelin.solutions/ethdenver-2019-recap-and-zeppelin-bounty-winners-59dbbad3996d)!

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

