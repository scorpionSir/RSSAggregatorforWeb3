[![](https://substackcdn.com/image/fetch/w_96,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F37b09348-f4f1-47a2-b9e0-a2007299e6e4_256x256)](https://proofofwork.news)

# [Proof of Work](https://proofofwork.news)

SubscribeSign in

Share this post

Proof of Work #70

proofofwork.news

Copy link

Twitter

Facebook

Email

# Proof of Work #70

### State power weakening

[Eric Meltzer](https://substack.com/profile/138320-eric-meltzer)

Jun 13, 2019

[Share](javascript:void\(0\))

Normally I try to avoid speculating on the medium-term or far future—my job is
to speculate on the relatively near future (5 years or so), and I know first
hand how hard that is to do well. But if you’ll indulge me in a bit of long-
term speculation for the length of this email, I’d like to think out loud a
bit about what’s happening to state power as a direct result of technology. I
also won’t bother to hide my glee about these developments—as a Jew I have a
deep-seated distrust of nation states, and I’ve been dismayed by the
increasing power that surveillance and weapons technologies have granted to
state actors. That the tide is changing now is a source of deep joy for me,
and a strong motivator to keep me investing in this space (as if the moongainz
weren’t enough, haha)

The first and most obvious trend is that of cryptocurrencies eroding the
State’s ability to print money. This started with Bitcoin, and was [clearly
part of Satoshi’s intent](https://bitcointalk.org/index.php?topic=2216056.0)
in releasing the Bitcoin software. Unsurprisingly, this is becoming most
apparent in countries with extremely weak fiat currencies like Venezuela—and
also, it happens slowly (then fast) because the fiat financial system resists
outflows pretty well. But at the end of the day it’s a leaky bucket, and the
cat is not going back into the bag on this one. The money landscape in Dec
2008 was entirely national fiat currencies—in January 2009 it suddenly
included a decentralized digital currency. In January 2019, Bitcoin and a
plethora of altcoins exist. In January 2029, I suspect that FacebookCoin style
corporate currencies, decentralized currencies like Bitcoin, and national fiat
currencies will all be competing, with the former two categories making up a
very large chunk of world commerce.

The second ongoing trend is the inability of state defense agencies to deal
with what William Gibson termed “an increase in individual lethal agency.” Put
simply, the number of people one determined individual can kill if they want
to is increasing and shows no signs of slowing down. From a State power
perspective, this means that waging war even on supposedly much weaker
adversaries is way more costly, because they can respond asymmetrically e.g.
through terror attacks.

The final trend that seems to be reducing state power is the existence of the
Internet as an information dissemination tool. This one is a bit of a mixed
bag—the internet permits surveillance that increases state power, but it also
permits people to share information widely in a way that was previously only
available to state actors. I think on balance this will end up decreasing
state power; surveillance will become more and more difficult as financial
transactions move onto things like Mobilecoin, Zcash etc and as communications
increasingly are over end-to-end encrypted open source tools like Signal; at
the same time, the tools of mass influence will be wielded increasingly by
non-state actors (corporations, small interest groups, etc).

One of the main differences between people who have been in the crypto space
for a long time and people who are relatively new is the degree to which they
understand that cryptocurrencies are inherently an anti-state technology, and
need to be built from the ground up to withstand multi-state attacks. At the
moment, very few if any cryptocurrencies meet this bar (although Bitcoin is by
far the closest). Naval Ravikant referred to the State as the “final boss” for
crypto; I agree with that assessment and think that the boss fight may be
coming sooner than people think.

More next week. Especially interesting updates this week from Sia and Maker!

####  **Satoshi’s Treasure Hunter’s Journal**

  * Released the Clan Key which required users to start a chain by shooting videos of themselves outside making a clan gesture, and posting the video on twitter. To extend the chain, the next person should have someone shoot a video of them holding a phone playing the previous video in the chain, and making the same secret gesture, and then quote-tweet the previous “block” in the chain. Every tweet of this game includes a hashtag #clanchain

  * All tweets can be seen [here](https://twitter.com/search?f=tweets&vertical=default&q=%23clanchain&src=typd)

  * This clue will end on June 15th, and the team with the longest chain wins. So far, some of the longest chains include: #CipherToshi #steemclan #clarksonclan among which #CipherToshi is so far the longest with 51 tweets

#### Bitcoin & Friends

 **Jimmy on Bitcoin**

 **[Optech](https://bitcoinops.org/en/newsletters/) on Bitcoin [ed: sign up
for their newsletter too! it’s great!]**

  * A new paper by Gleb Naumenko, Pieter Wuille, Gregory Maxwell, Sasha Fedorova, and Ivan Beschastnikh describes an alternative transaction relay protocol, [Erlay](https://arxiv.org/pdf/1905.10518.pdf). 

  * Bitrefill CEO Sergej Kotliar gave a presentation about LN for the Optech executive briefing last month. The [video](https://www.youtube.com/watch?v=1UDD9PMFTds) is now available.

  * The author of the COSHV proposal we described [last week](https://bitcoinops.org/en/newsletters/2019/05/29/#proposed-transaction-output-commitments) has replaced it with a [similar proposal](https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2019-June/016997.html) under a different name.

 **Aviv from Spacemesh**

 _Spacemesh is a programmable cryptocurrency powered by a novel proof-of-
space-time consensus protocol._

  * Implemented [XDR serialization for TX api calls](https://github.com/spacemeshos/smapp/pull/107)

  * Changed [wallet and accounts default names](https://github.com/spacemeshos/smapp/pull/111)

  * Implemented [Disk volumes and free space checking across different OSes](https://github.com/spacemeshos/smapp/pull/112)

  * Merged the new VRF eligibility oracle that relies on previously merged bls signature schemes

  * Merged the activation transaction sync flow

  * Added a network on-the-wire and in-memory deduplication to reduce bandwidth

  * Track our progress by browsing go-spacmesh [merged PRs](https://github.com/spacemeshos/go-spacemesh/pulls?q=is%3Apr+is%3Aclosed)

  * We co-hosted and participated in [WASM on the Blockchain 2019 Berlin](https://avive.github.io/wasm_on_the_blockchain). 

  * The weekend community workshop at Full Node Berlin was jam-packed with excellent sessions and discussions.  _Videos and decks will be published soon_. 

  * Wasm smart contracts are coming to your favorite blockchain, but we have several big issues to solve first...

 **JZ from Decred**

 _Decred  is an autonomous digital currency with a hybrid consensus system. It
is built to be a self-ruling currency where everyone can vote on the rules and
project-level decision making proportionately to their stake._

  * The [May edition of the Decred Journal](https://decredcommunity.org/blog/decred-journal-may-2019) has dropped, covering the latest hard fork that activated DCP4 and paved the way for Lightning Network, which is now mainnet ready. It also brings word of the iOS wallet for Decred which just put out a release candidate this week in preparation for the imminent final release.

  * We also have a [new issue of the Politeia Digest](https://medium.com/politeia-digest/issue-17-may-28-june-9-bc5bb77e4f6c) which summarizes the four proposals that were up for vote, all of which passed with support between 76% and 99%. The Decred treasury balance hit 617k DCR (approx +15k DCR/month) — $16.5 million (+$408k/month) based on $26.70 DCR price.

 **Johnny from Stellar**

 _Stellar is an open network for sending and exchanging value of any kind. Its
global network enables digitization of assets - from carbon credits to
currencies - and enables movement around the internet with ease._

  * The Stellar Public Network successfully upgraded to Protocol 11 and updated its maximum operations/ledger to 1000. You can [read more about the improvements here](https://medium.com/stellar-development-foundation/protocol-11-improvements-b78c19c4df3f).

  * Stellar is hosting [Meridian](https://medium.com/stellar-development-foundation/introducing-meridian-24c3396b868d), its first global conference, in Mexico City. You can [sign up on the waitlist here](https://meridian.stellar.org/).

  * Multiple features for making quorum management easier for administrators and organizations are coming in 11.2.0, including [automatic quorum generation](https://github.com/stellar/stellar-core/pull/2125) and [a quorum intersection checker](https://github.com/stellar/stellar-core/pull/2127).

 **Izaak from Coda**

 _Coda is the first cryptocurrency protocol with a constant-sized blockchain.
Coda compresses the entire blockchain into a tiny snapshot the size of a few
tweets using recursive zk-SNARKs._

  * Deepthi [rewrote](https://github.com/CodaProtocol/coda/pull/2609) the parallel-scan (one of Coda's two core data structures), and the new code is beautiful!

  * Paul [removed](https://github.com/CodaProtocol/coda/pull/2627) all the warnings from our codebase.

  * Carey, Avery, and Pranay have been [pushing](https://github.com/CodaProtocol/coda/pull/2626) [the desktop wallet](https://github.com/CodaProtocol/coda/pull/2608) [UI](https://github.com/CodaProtocol/coda/pull/2600) forward.

  * Jiawei [refactored](https://github.com/CodaProtocol/coda/pull/2602) the flow of async communication between various components of the daemon to make it more explicit.

#### Privacy coins

 **Paige & Zooko from Zcash**

 _Zcash is a  digital currency utilizing zk-SNARKs to enable its privacy-
protecting properties._

  * Progress towards NU3 feature selection 

  * Code review focus on librustzcash improvements and insight explorer support

  * Zcon1 test wallet app & continue ref wallet improvements

  * More in the full update: <https://forum.zcashcommunity.com/t/weekly-update-engineering/33731>

**Beni from Beam**

 _Beam is a confidential and scalable cryptocurrency based on Mimblewimble._

  * Focus on Privacy - Team Beam is attending the Blockchain Cruise \- June 9th-13th 2019

  * Alex Romanov, Beam CTO, will lead our first Vietnamese AMA on [Telegram](https://t.me/Mimblewimblevn) on June 18th, 2019, 1:00 PM (GMT)

  * Swap: [changed Beam Lock time](https://github.com/BeamMW/beam/commit/7dc87e91fce92efd31d78adea8644402a219885a)

  *  Swap: [process invalid credentials](https://github.com/BeamMW/beam/commit/53d0c68d2c3446c394ecf56702fe26eac6e4d2e0)

  *  Swap:  Transaction statuses change [#703](https://github.com/BeamMW/beam/issues/703)

  *  Swap: Rename "--swap_coins" to "--swap_init" [#698](https://github.com/BeamMW/beam/issues/698)

  *  Swap: Don't show help list after errors with 0 (zero) amount [#704](https://github.com/BeamMW/beam/issues/704)

  *  Desktop: Address book - Add ability to edit comment for addresses [#623](https://github.com/BeamMW/beam/issues/623)

  *  CLI Wallet: Add a command to get full transaction details [#613](https://github.com/BeamMW/beam/issues/613)

  *  Wallet - Multi-language support [#618](https://github.com/BeamMW/beam/issues/618)

  *  Edit Address pop-over should allow user to select / copy the address [#608](https://github.com/BeamMW/beam/issues/608)

 **Arnaud from AZTEC Protocol**

 _AZTEC Protocol is an efficient zero-knowledge protocol built on top of
Ethereum, making plug-and-play value transmission and asset governance privacy
tools for developers and companies.  _

  * This week in addition to updates to our client side library and our MPC code, we [added](https://github.com/AztecProtocol/AZTEC/pull/185) the multisig with timelock contract which will help us administer AZTEC

  * We also received the first ever [pull request](https://github.com/AztecProtocol/AZTEC/pull/184) for our EVM scripting language Huff by an external developer

  * Next week, Oana and Tom Waite will be at the [zkp coding workshop](https://twitter.com/paddypisa/status/1136957365876678656) in London. If you're around, say hi!

  * In addition to the two cryptographer roles, we are now hiring for a **Senior Solidity Engineer** and a **Senior Engineer**. You can apply [here](http://email.mg2.substack.com/c/eJwlUEuOwyAMPU3ZNSKQpGHBoq1mrhHxcVumBEfgTJU5_RBF8sKy_fw-zhA8MW96wUJsLZCn4LVQgg8t87rz7diPLJTpkQFmE6KmvAJbVhuDMxQw7fe9kuylwUnVg3RcXQYu7eDAenvpjOx5Lweh2M4xmdUHSA40_ELeMAGL-kW0lJO8nsR3LZOeEBuHe_tH4M5LRkKH8Szr6AdtYUEL3iouRcs7LjvRtM2NX-_jnY-3QbS37ut66vj8FE1ZbSHj3vXfzLI2OVUBdecy-EBzSNQEPJTRtoBO8CkRiCAzOkKpXqcKntcUaJsgGRvB6wNSvUt1kQOrNB5rPklXsfjAxwfz-x-f0nXk), or by emailing [arnaud@aztecprotocol.com](mailto:arnaud@aztecprotocol.com) with the name of the role as the subject.

#### Smart contracting platforms

 **Evan from[Ethereum](https://weekinethereumnews.com/)**

 _Ethereum  is a decentralized platform for applications that aims to resist
fraud, censorship or third-party interference._

  * Raul Jordan’s [Eth2 history and high level overview](https://www.tokendaily.co/blog/design-principles-of-ethereum-2-0)

  * Starkware and 0x release [StarkDEX](https://blog.0xproject.com/starkdex-bringing-starks-to-ethereum-6a03fffc0eb7) demo running on Ropsten. 550 transactions per second using STARKs at only ~6000 gas per trade.  Mainnet release planned “in several months.” 

  * Alex Beregszaszi’s [history of Ewasm](https://drive.google.com/file/d/1JfajqP1kDzy2-Hd1BjYi7eLLuZnChzBS/view)

  * [Microsoft releases its open source Solidity formal verification tool](https://www.microsoft.com/en-us/research/blog/researchers-work-to-secure-azure-blockchain-smart-contracts-with-formal-verification/?ocid=msr_blog_verisol_tw) using its Boogie IR language

 **Peter from NEAR**

 _NEAR is a sharded proof-of-stake blockchain._

  * 29 PRs across 9 repos and 10 authors. Featured repos: [nearcore](https://github.com/nearprotocol/nearcore), [nearlib](https://github.com/nearprotocol/nearlib), [near-shell](https://github.com/nearprotocol/near-shell/) and [near-wallet](https://github.com/nearprotocol/near-wallet) 

  * We now support [smart contracts written in Rust](https://github.com/nearprotocol/near-runtime-rs)

  * You can attach tokens to any call and send tokens to accounts from the command line in near-shell

  * View account and command syntax improvements in near-shell

  * Feature fixes in wallet such as display username, send money, account recovery, login redirect and UI.

  * Add keys for account in nearlib

  * Switched to u128 to nearcore

 **Topper from Quorum Control**

 _Quorum Control makes Tupelo, a permissionless proof of stake DLT platform
purpose-built to model individual objects that enables flexible public or
private data models._

  * Ongoing Optimization of Production Tupelo TestNet (0.2.3) and the release of a second TestNet (0.4.0) with additional signing nodes.

  * [Tupelo version 0.4.0](https://docs.quorumcontrol.com/download.html) has been released!

  * [New improved performance results](https://docs.quorumcontrol.com/platform_performance.html) published for v0.4.0 (mean finality in 297 ms with 100 signing nodes at 200 TPS)

  * New release includes new configuration options for notary groups.

  * New release completes the removal of msgp in favor of protobuf.

  * Read Part 3 of our published posts on NFTs, [Part 3: Digital Twins (Only Their Mother Can Tell Them Apart!)](https://www.quorumcontrol.com/blog/digitaltwin)

 **Michael from Loom**

 _Loom Network is a platform for building highly scalable DPoS sidechains to
Ethereum, with a focus on large-scale games and social apps._

  * [Launched TRON + PlasmaChain integration](https://loom.ly/RrMDYbo). Now users can send TRX and native TRON-based assets between Loom and TRON mainnet.  

  * Released [collectible TRON-themed Relentless card packs](https://t.co/6IWbMmaKSz) on the Loom Marketplace, with a promotion for $13.5k in TRX prizes.

  * Over 211M tokens have been staked on Loom, which amounts to ~27% of circulating supply.

 **Myles from EOS**

 _EOS is a new blockchain architecture designed to enable vertical and
horizontal scaling of decentralized applications._

  * Ivan on Tech [interviewed](https://www.youtube.com/watch?v=-yU_hu_LGos) Dan Larimer about Voice, EOS VM, EOSIO 2, and more

  * Ashe Oro published an [overview](https://medium.com/@Ashe_Oro/b1june-recap-and-reflections-153b925444ec) of the B1June event 

  * EOSIO Labs [released](https://medium.com/eosio/eosio-labs-release-webauthn-example-web-app-for-eosio-yubikey-support-aa700eac8879) a WebAuthn Example Web App for EOSIO YubiKey Support

  * The Block [reported](https://www.theblockcrypto.com/2019/06/06/block-one-poured-150-million-into-its-new-social-media-platform/) that B1 has a $150M budget for Voice, its social network project

  * [Block.one](http://block.one/) released a detailed "[strategic vision](https://eos.io/strategic-vision/)" roadmap 

 **Zaki from Cosmos**

 _The  Cosmos Network is a decentralized network of independent, scalable, and
interoperable blockchains._

  * A fully functional Ethereum . -> Cosmos oracle is in [final code review](https://github.com/cosmos/peggy/pull/51).

  * Several interesting IBC specification were merged. [Relayer Module](https://github.com/cosmos/ics/tree/master/spec/ics-026-relayer-module) [Connection Handler](https://github.com/cosmos/ics/tree/master/spec/ics-025-handler-interface)

  * Preethi wrote a [deep dive](https://www.preethikasireddy.com/posts/how-does-cosmos-work-part1) on [Cosmos](https://www.preethikasireddy.com/posts/how-does-cosmos-work-part2). 

  * Gautier also wrote a [Cosmos](https://blog.cosmos.network/what-does-the-launch-of-cosmos-mean-for-the-blockchain-ecosystem-952e14f67d0d) explainer.

  * This week we are hosting an IBC retreat, Interchain Unconference and Cosmos Hackathon all in Berlin.

#### Financial Infrastructure

 **Antonio from dYdX**

 _dYdX is a decentralized exchange for margin trading, borrowing, lending, and
eventually derivatives. dYdX allows traders to trustlessly short and get
leverage on crypto assets._

  * Launched the DAI-USDC market! Integrates with 0x for the buy/sell liquidity. Read more here: <https://medium.com/dydxderivatives/dai-usdc-market-launches-on-dydx-bde957c48e2e>

  * Added TradingView charts

  * Working on improvements to the borrow & cross trading flows

  * Building price oracles for new assets

  * [Hiring](https://dydx.exchange/careers/) product designers & engineers full-time in SF!

 **Brendan from Dharma**

 _Dharma is the easiest place to borrow and lend cryptocurrencies. It enables
non-custodial peer-to-peer lending through smart contracts on Ethereum._

  * Added front-end improvements to Dharma Account page

  * Lowered interest rates across all assets. The following rates are what borrowers pay and what lenders earn: ETH — 1% APR USDC — 6% APR DAI — 8% APR

  * Built out new custom borrow feature that will allow borrowers to specify custom loan terms

  * Worked with a number of CDP holders to refinance their DAI debt with Dharma

  * We're [hiring](https://boards.greenhouse.io/dharma) a General Counsel and Full Stack Engineers in SF!

 **Coulter from MakerDAO**

 _Maker is comprised of a decentralized stablecoin, collateral loans, and
community governance._

  * A new [Dai in Numbers report](https://blog.makerdao.com/dai-in-numbers-momentum-report/) is out. TLDR: Adoption continues to grow ~20% per month. A record 1.4 billion Dai were traded in May, and 325M Dai have been generated through the Maker Protocol. 

  * Dai and gaming are becoming a perfect match. This week Maker [partnered with Axie Infinity](https://blog.makerdao.com/game-on-maker-and-axie-infinity-partner-receive-dai-themed-nfts-for-opening-cdps/) to bring Dai to their game, and for those that have CDPs, you can claim an NFT that has unique benefits in-game.

  * Publish0x now lets users [tip in Dai](https://www.publish0x.com/publish0x-official-blog/dai-token-integrated-for-tipping-on-publish0x-xryydn) on their platform.

 **Lazar from MARKET Protocol**

 _MARKET Protocol is a framework for creating tokens that track prices of
traditional or digital assets._

  * We announced our mainnet launch coming June 24th! See our [blog post](https://medium.com/market-protocol/mpx-mainnet-ahead-2881b915d334) for more information

  * Our first product available for minting and trading: tokenized BTC/DAI positions (both long and short)

  * Early access is now available, users can try [MPX](https://mpexchange.io/) prior to our official launch with market makers

 **Robert from Compound**

 _Compound is a money market protocol on the Ethereum blockchain — allowing
individuals, institutions, and applications to frictionlessly earn interest on
or borrow cryptographic assets without having to negotiate with a counterparty
or peer._

  * Added  _[cToken API](https://compound.finance/developers/api#CTokenService)_  to retrieve detailed market and token data for each supported market

  * Added  _[Market History API](https://compound.finance/developers/api#MarketHistoryService)_  to retrieve historical interest rate and market size data for each supported market

#### Layer two and interoperability

 **Matt from 0x**

 _0x_  is an open protocol that enables the peer-to-peer exchange of assets on
the Ethereum blockchain.

  * [Added a pair of off-the-shelf React UIs](https://0x.org/launch-kit) to 0x Launch Kit for both orderbook relayers and NFT marketplaces.

  * [Released a demo of StarkDEX](https://blog.0xproject.com/starkdex-bringing-starks-to-ethereum-6a03fffc0eb7), a proof-of-concept technology developed in collaboration with StarkWare to scale decentralized exchange.

  * [dYdX is now sourcing liquidity from 0x](https://medium.com/dydxderivatives/dai-usdc-market-launches-on-dydx-bde957c48e2e) via Radar Relay.

  * More development updates [here](https://blog.0xproject.com/development-update-19-may-2019-d420cc8bc02e).

 **Tony from Liquidity.Network**

 _Liquidity Network is a transfer and swap platform for any token_

  * Have you ever wished an explorer for Liquidity Network's off-chain transactions? Now, it comes! Head to <https://explorer.liquidity.network/> to get some statistic data of our off-chain transfers.

  * We are excited to join USDC’s ecosystem to bring crypto to the masses by offering a simple and innovative way to transfer and swap crypto assets. Read more about this collaboration in the [Liquidity blog](https://blog.liquidity.network/2019/05/28/usdc-integrated-on-the-liquidity-networks-ecosystem-as-the-first-fiat-backed-stable-coin/) and [Centre Blog](https://medium.com/centre-blog/usdc-ecosystem-spotlight-usdc-broadens-defi-footprint-as-value-transferred-on-chain-surpasses-10b-9b98808d28c6)! 

 **Dong Mo from Celer**

 _Celer Network is a layer-2 scaling platform that enables fast, easy and
secure off-chain transactions for not only payment transactions, but also
generalized off-chain smart contracts._

  * We were updating our mobile app reward features: sign-up, referral, and daily check-in. 

  * We were updating game features: multi-token and onboarding. 

  * We were testing state channel-related APIs: state migration and deposit. 

  * Stability & robustness improvements in backend servers. 

  * Operational enhancements in monitoring & automated maintenance. 

  * We are continuing work on channel contract upgradability.

 **Alexandra from Parity Technologies**

 _Parity  Technologies builds core blockchain infrastructure, from Parity
Ethereum, an Ethereum client, to Polkadot, an interoperable blockchain
network._

  * All tests passed for [Parity's "Shasper" Ethereum 2.0 spec v0.6.3 implementation](https://twitter.com/sorpaas/status/1137019533540114432).

  * New [PolkaDAO update: 1250 DAI distributed.](https://twitter.com/polkadotnetwork/status/1138088174192910337)

  * First round of speakers announced for [Web3 Summit](https://web3summit.com/speakers/).

  * Web3 Foundation is [providing grants to build the Web3 ecosystem](https://github.com/w3f/Web3-collaboration/blob/master/grants/grants.md). [We're hiring!](https://www.parity.io/jobs/) New opening: [Content Marketer.](https://www.parity.io/jobs/#berlin-content-marketer)

#### Application infrastructure

 **Doug from Livepeer**

 _Livepeer is a decentralized video infrastructure network, dramatically
reducing prices for developers and businesses building video streaming
applications at scale.  _

  * Published a [decentralization update](https://medium.com/livepeer-blog/livepeer-decentralization-update-8d34d03af701) focused on the decentralization axis of network operations, development, and governance. 

  * A community group built an [Aragon DAO that can act as a delegator in the Livepeer protocol](https://github.com/videoDAC/livepeer-aragon). It is live on mainnet.

  * Development has largely been focused on benchmarking and reliability for the transcoding infrastructure in Streamflow, and unlocking the GPU transcoding alongside mining. 

 **Ryan from FOAM**

 _FOAM  is building spatial applications and proof of location that bring
geospatial data to blockchains and empower a consensus driven map of the
world._

  * [FOAM Location Update and Demo Documentation](https://blog.foam.space/foam-location-update-and-demo-documentation-58162d1ec075 "https://blog.foam.space/foam-location-update-and-demo-documentation-58162d1ec075"), We recently demonstrated a major milestone in our Proof of Location technology by processing and validating a Presence Claim over radio.

  * [FOAM.tools](https://foam.tools/ "https://foam.tools/") has launched, The Cartographer Tools are designed to help validators with voting and challenge decisions. The Cartographer Tools complement the FOAM Map and display information differently than the main map to help cartographers make more efficient decisions on challenges.

  * The Foamspace Developer Team had a great time in LA hosting a weekend of lectures and hacking sessions on Functional Programming with Haskell/Purescript and building with the FOAM web3 stack <https://0mphalos.github.io/mayday-convoluted-weekend/about/>

  * [foam.space](https://foam.space/ "https://foam.space/") relaunched 

 **David from Sia**

 _Sia is a decentralized cloud storage platform leveraging blockchain
technology to create a data storage marketplace that is more robust and more
affordable than traditional cloud storage providers._

  * As part of the upcoming seed-based file recovery feature, lukechampine added new API endpoints for handling remote backups.

  * Matt improved the file repair process, that is now better identifying the file chunks with low redundancy needing repair. He also improved the handling of large uploads and memory usage

  * Community member Shatnerz corrected errors caused by the 1.4.0 update on the Sia-Ant-Farm package, which is used as a local testnet for Sia

  * The Release Candidate of 1.4.1 is expected to be released for community testers imminently

  * Eddie added an advanced prompt for setting up the renter’s allowance in Sia-UI, that now can be customized for the duration of contracts, number of hosts and how much it is expect to be uploaded and downloaded.

  * Eddie added also the very anticipated dark mode to the Sia-UI.

  * The Sia team has hired Manasi Vora as Head of Product Strategy. She will focus on the growth and improvement of the Sia network, as well as enterprise business development

  * Goobox has added the possibility of paying their SiaS3 storage service with cryptocurrencies. Additionally, they now offer a free trial of 14 days

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

