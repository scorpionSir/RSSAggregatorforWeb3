[![](https://substackcdn.com/image/fetch/w_96,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F37b09348-f4f1-47a2-b9e0-a2007299e6e4_256x256)](https://proofofwork.news)

# [Proof of Work](https://proofofwork.news)

SubscribeSign in

Share this post

Proof of Work 75

proofofwork.news

Copy link

Twitter

Facebook

Email

# Proof of Work 75

[Eric Meltzer](https://substack.com/profile/138320-eric-meltzer)

Sep 28, 2019

[Share](javascript:void\(0\))

Hi from Boston!

I had lunch with a friend recently who showed me this crazy org she’s
assembled called the [Yellow Hat
DAO](https://github.com/carboclan/pm/blob/master/README.md). As far as I can
tell it’s not really a DAO in the sense I usually think of them, in that it
doesn’t have a programmatic reward/rules system that underlies it. But it’s a
group of people that seem to have coalesced from the ether, funded by a mix of
ICO treasuries, individual wealth, random grants, hackathon prizes etc etc. to
reliably churn out weird and interesting stuff. One of the central things the
Yellow Hats seem to like to play with is the permissionless aspect of wrapping
one thing inside another that blockchain protocols enable. To see how weird
and fun this can get, let’s look at
[LSDai](https://github.com/carboclan/pm/blob/master/research/LSDai.md), one of
their projects.

So we have Dai, which is created by depositing ETH into a contract. You can
then take the Dai and deposit that into another (interest bearing, this time,
e.g. Compound) contract and get rDai which is **r** edeemable for your locked
up Dai. LSDai takes that rDai as an input, and creates short and long Dai
interest tokens, so that people can hedge the interest rate offered by (again,
e.g.) [Compound](https://compound.finance/).

I find what these guys have built to be pretty interesting (we’ll be running
occasional updates from them here), and I’m equally interested by the method
of organization, which is completely ad-hoc and flexible, and _is_ in fact a
DAO in the sense that there is no legal entity out there. It seems like
something Bruce Sterling would be into.

More next week! Also, I’ll be bouncing around Asia from the 1st to the 15th
roughly, if you’re working on something cool and are in that half of the
world, feel free to ping me on Twitter.

#### **Satoshi’s Treasure Hunter’s Journal**

  * The Tezos Minihunt is underway, with 13 clues in the wild and 14 required to unlock a wallet containing 5000 XTZ! Hunters have tracked clues around the world, and chased Eric all over the MIT campus to obtain keys. The 14th and final clue will be released sometime in the following week or so. 

  * The Tezos Main Hunt for 1M XTZ is under development, with smart contract work [being done by Stove Labs](https://medium.com/@matej.sima/cooking-with-stove-labs-1-541d06a05c9a)

  * The Bitcoin Hunt continues, with new clues over the past few days. The next set of clues is scheduled to appear on university campuses around the world!

  * If you run a project or crypto business and are interested in advertising to our userbase of over 100k (including many folks new to crypto), ping us at q@satoshistreasure.xyz. 

#### Bitcoin & Friends

 **Jimmy on Bitcoin**

 **[Optech](https://bitcoinops.org/en/newsletters/) on Bitcoin [ed: sign up
for their newsletter too! it’s great!]**

  * [Bitcoin Core #16400](https://github.com/bitcoin/bitcoin/issues/16400) refactors part of the mempool transaction acceptance code, to potentially enable package relay, which could allow nodes to accept a transaction below the node’s minimum feerate if the transaction came bundled with a child transaction whose fee was high enough to pay the minimum feerate for both it and its parent. If widely deployed, package relay would allow users who create transactions a long time before broadcasting them (e.g. timelocked transactions or LN commitment transactions) to safely pay the minimum possible fee and use CPFP to bump it up later. 

**Aviv from Spacemesh**

 _Spacemesh is a programmable cryptocurrency powered by a novel proof-of-
space-time consensus protocol._

  * [BlockTV interview](https://blocktv.com/watch/2019-09-18/5d820db42919d) with Spacemesh CEO Tomer Afek

  * [BitMedia article](https://bit-media.org/blockchain/spacemesh-making-blockchain-technology-accessible-to-all/) about low barrier-to-entry mining and the Spacemesh Vision

  * Getting app functional on Windows and Linux (Ubuntu) in addition to MacOs and app testing on five-node local network, initial sandbox integration - [Merged fixes](https://github.com/spacemeshos/smapp/issues/204)

  * Currently we are shifting focus to start large scale cloud testing for testnet. We are also starting a process of documenting our code and updating our wikis as preparation for test net launch. [Merged issues](https://github.com/spacemeshos/go-spacemesh/pulls?q=is%3Apr+is%3Aclosed)

  * More updates on [our site](https://spacemesh.io/weekly-updates/)

 **JZ from Decred**

 _Decred  is an autonomous digital currency with a hybrid consensus system. It
is built to be a self-ruling currency where everyone can vote on the rules and
project-level decision making proportionately to their stake._

  * We've [tagged v1.2.0 of dcrstakepool](https://github.com/decred/dcrstakepool/releases/tag/v1.2.0) which is the first release since late 2017, so there are a ton of changes in the 160 pull requests made by 20 contributors. Among them are security and privacy enhancements as well as a slick new interface.

  * Two Politeia proposals are currently up for stakeholder vote:

    1. [Permabull Nino's Decred research proposal](https://proposals.decred.org/proposals/f0d1bd7447182328b44c691de88cb660b63df17f1f3a94990af19acea57c09bb) (you can listen to the [Decred in Depth interview covering his research here](https://soundcloud.com/decredindepth/ep-5-decred-as-strong-accounting-ticket-metrics-with-permabull-nino)).

    2. As well as one requesting funds for [events in Eastern Europe by the CryptoDealers team](https://proposals.decred.org/proposals/fdd68c87961549750adf29e178128210cb310294080211cf6a35792aa1bb7f63). May Stakey have mercy on them.

  * A quick recap of recent Pi proposals that have passed:

    1. [TinyDecred](https://proposals.decred.org/proposals/20e967dad9e7398901decf3cfe0acf4e0853f6558a62607265c63fe791b8b124) \- a Python toolkit for Decred which was already built by the developer, who proposed payment in arrears. [The code can now be found on GitHub](https://github.com/decred/tinydecred).

    2. [Decred DEX](https://proposals.decred.org/proposals/417607aaedff2942ff3701cdb4eff76637eca4ed7f7ba816e5c0bd2e971602e1) funding (discussed in last week's issue of PoW).

    3. [RFP: Decred Designated Market Maker](https://proposals.decred.org/proposals/30822c16533890abc6e243eb6d12264b207c3923c14af42cd9b883e71c7003cd) \- A proposal by myself to gauge stakeholder interest in hiring a market maker.

    4. [i2 Trading: DCR Market Making](https://proposals.decred.org/proposals/2eb7ddb29f151691ba14ac8c54d53f6692c1f5e8fe06244edf7d3c33fb440bd9) \- The winner among three market makers that submitted proposals to provide liquidity for Decred.

 **James from Summa**

 _Summa builds tools to exchange crypto in a convenient and trustless
fashion._

  * We released [bitcoin-spv](https://github.com/summa-tx/bitcoin-spv) in Golang and JS, sponsored by the [Interchain Foundation](https://interchain.io/). More implementations 

  * We also shipped a full [Bitcoin relay](https://github.com/summa-tx/relays), which is running on [Ropsten](https://ropsten.etherscan.io/address/0x516d8ee665e86438349dbaaa215c5cac4522fcd5). We're also working on a [cosmos-sdk module](https://github.com/summa-tx/relays/tree/golang) with equivalent features :)

  * Library releases: [riemann-ether@3.0.0](https://github.com/summa-tx/riemann-ether) \-- More and better Infura tooling

 **Izaak from Coda**

 _Coda is the first cryptocurrency protocol with a constant-sized blockchain.
Coda compresses the entire blockchain into a tiny snapshot the size of a few
tweets using recursive zk-SNARKs._

  * Testnet [BETA] Launched in Phase 2 this week, with longer, more stable releases; 70 community members signed up to stake and there is a lot of activity on our [Discord channel](http://bit.ly/CodaDiscord)

  * Phase 1 of Testnet concluded last week, we had 120+ community members join, and 90+ run a node. Lots of good technical developments all recapped in our [Phase 1 Retro Blog](http://bit.ly/TestnetRetroPhase1)

  * We have a [beautiful testnet landing page](https://codaprotocol.com/testnet.html) implemented by Michelle. Thanks to Harold and the whole product team for the design.

  * We are now using the [Poseidon hash function](https://github.com/CodaProtocol/coda/pull/3455), which has improved our SNARKs by up to 8x. Improving SNARK performance will help us to decrease our block times, which is important for fast confirmation.

  * John [improved](https://github.com/CodaProtocol/coda/pull/3384) the usability of the CLI by re-prompting the user when they enter an incorrect password for their wallet file.

#### Privacy coins

 **Zooko from Zcash**

 _Zcash is a  digital currency utilizing zk-SNARKs to enable its privacy-
protecting properties._

  * No update this week as the relevant people are out of office

 **Daniel from Grin**

 _Grin is a community-driven implementation of the Mimblewimble protocol that
aims to be privacy preserving, scalable, fair, and minimal._

  * Merged PRs: [5 in /grin](https://github.com/mimblewimble/grin/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A2019-09-16..2019-09-22+) | [0 in /grin-wallet](https://github.com/mimblewimble/grin-wallet/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A2019-09-16..2019-09-22+) | 3 unique contributors

  * In the [last dev meeting](https://github.com/mimblewimble/grin-pm/blob/master/notes/20190917-meeting-development.md) it was established that we're on track for v2.1.0 release for mid-october, audit findings have been fixed, security canaries were agreed and as a result, Igno was removed from the security contact list. The meeting also briefly discussed an RFC proposing to make tor hidden services the default tx building method.

  * The [community sub-team was announced](https://www.grin-forum.org/t/announcing-the-grin-community-subteam-help-organise-grincon1/6080), first objective on the agenda is to plan this year's grin conference, grincon1.

  * The [fundraising sub-team was announced](https://www.grin-forum.org/t/announcing-the-fundraising-subteam/6114) by community member @nass, which will work to raise funds to help safeguard the long term continuity of Grin development.

  * A [dedicated repo for security](https://www.grin-forum.org/t/announcing-the-grin-security-repo/6105) was created to keep track of keys, incidents, audits, canaries, and more.

  * As part of transaction building research, we're collating [research papers on mixnets and ACNs](https://github.com/lehnberg/mixnet-and-acn-research) in one place.

  * Since we last gave an update, Grin has been joined by a mysterious, always good vibes, abstract painter, @LovelyGrin. Their artwork is unlicensed and on display in [this repo](https://github.com/lovelygrin/artwork), with new work constantly being added. Check it out!

  * Grin is 100% funded by donations. Please support Grin development - [Donate now](https://grin-tech.org/general_funding).

  * The Chinese community Gringotts 古灵阁 organised Full Node Day to encourage more users to run full nodes. [Overview in English](https://www.grin-forum.org/t/grin-full-node-day/6124), and [full details in Chinese](https://mp.weixin.qq.com/s?__biz=MzAwMzk0NTQ3Mg==&mid=2247483754&idx=1&sn=b1c357c9fca4d5d0e856a64b5788ddd5&chksm=9b322405ac45ad13659ae5555fe50b47a2bb956f6ca6806852d912c50ba2630cfe81a13c532b&token=922184680&lang=zh_CN#rd). 

  * Photos and some details (if you squint) from [an event booth about the Avalon Grin G1 Asic miner](https://www.grin-forum.org/t/first-grin-asic-ads-in-conference/6125), allegedly due by end of October.

  * More Grin info [here](https://grinnews.substack.com/).

 **Beni from Beam**

 _Beam is a confidential and scalable cryptocurrency based on Mimblewimble._

  * Beam listed on Binance. Read [here](https://info.binance.com/en/research/BEAM-2019-09-19.html) Binance Research analysis about Beam

  * We have released the [latest version of Beam Wallet on Android](https://medium.com/beam-mw/clear-cathode-3-1-android-release-notes-8ed4a149c4c7) (Clear Cathode 3.1) with some awesome features including Wallet Restore

  * We have developed Laser Beam (state channels) on Beam. See Alex Romanov, Beam CTO, showing [a demo](https://www.youtube.com/watch?v=sGxt29ZW4k0) of this awesome tech

  * Clear Cathode 3.1.6 Android - [Release Notes](https://github.com/BeamMW/android-wallet/releases/tag/clear_cathode_3.1_hotfix)

    * [Hotfix] Clear Cathode 3.1 Android - [Release Notes](https://github.com/BeamMW/android-wallet/releases/tag/clear_cathode_3.1)

    * Good progress on [Clear Cathode 3.2 Desktop](https://github.com/BeamMW/beam/projects/20)

    * [Atomic Swap] Show the composite status of the nodes for all the coins in a user-friendly and informative way [#831](https://github.com/BeamMW/beam/issues/831)

 **Arnaud from AZTEC Protocol**

 _AZTEC Protocol is an efficient zero-knowledge protocol built on top of
Ethereum, making plug-and-play value transmission and asset governance privacy
tools for developers and companies.  _

  * Our main priorities are a POC implementation of [PLONK](https://vitalik.ca/general/2019/09/22/plonk.html) (the universal zk-snark construction we released in collaboration with Protocol Labs), the launch of our Ignition ceremony MPC ([sign up here](https://aztecprotocol.us7.list-manage.com//subscribe?u=0f5fa2f22c3349ec01c3d1fdc&id=1b8d51cab0)), and the final touches for our production launch.

  * Our CTO Zac has been hard at work building an efficient PLONK prover and verifier [proof of concept](https://github.com/AztecProtocol/barretenberg/tree/polynomials). This week, we achieved our first round of benchmarks which we’ll be sharing soon.

  * [Vitalik announced](https://twitter.com/VitalikButerin/status/1174632632329441280) his participation in our Ignition ceremony, using his own implementation of the MPC. 

  * Trail of Bits is in the final couple of days of their Audit of both our [MPC codebase](https://github.com/AztecProtocol/Setup) and our [protocol codebase](https://github.com/AztecProtocol/aztec). Report to be published in the next couple of weeks.

  * We’ve made progress on our browser extension, adding simplified APIs for most of our proof constructions and a basic UI this week.

  *  **ASK:** We’re looking for people who want to get involved with Ignition. You can [sign up here](https://aztecprotocol.us7.list-manage.com//subscribe?u=0f5fa2f22c3349ec01c3d1fdc&id=1b8d51cab0), or learn more about what it entails [here](https://medium.com/aztec-protocol/snapshot-of-the-aztec-ceremony-3052f979577f).

#### Smart contracting platforms

 **Evan from[Ethereum](https://weekinethereumnews.com/)**

 _Ethereum  is a decentralized platform for applications that aims to resist
fraud, censorship or third-party interference._

  * [What’s New in Eth2](https://notes.ethereum.org/@ChihChengLiang/Sk8Zs--CQ/https%3A%2F%2Fbenjaminion.xyz%2Fnewineth2%2F20190920.html?type=book) including the work being done around BLS sig standardization

  * Matter Labs releases their [zk rollup code](https://github.com/matter-labs/rollup). Scalability through trustless layer 2 chains is near.

 **Jing from Plasma**

 _Plasma Group is building "Generalized Plasma", a layer 2 scaling
infrastructure for Ethereum that allows for general state transitions on layer
2._

  * This past 3 weeks, we've been working on a collaboration with a DEX to create a PoC with our scaling solution Optimistic Rollup, which enables smart contracts on layer 2 ([blog post on it here](https://medium.com/plasma-group/ethereum-smart-contracts-in-l2-optimistic-rollup-2c1cef2ec537)). 

    * For this we merged the following issues: [#409](https://github.com/plasma-group/pigi/pull/409) Mock end to end rollupchain example

    *  [#429](https://github.com/plasma-group/pigi/pull/429) Client-side executeTransaction(...)

    *  [#431](https://github.com/plasma-group/pigi/pull/431), [#432](https://github.com/plasma-group/pigi/pull/432) Ignore empty leaves when calling update(...), and batch merkle update

    *  [#435](https://github.com/plasma-group/pigi/pull/435), [#425](https://github.com/plasma-group/pigi/pull/442) Signature checking for wallet and aggregator, signatures for balances receipt

    * [#439](https://github.com/plasma-group/pigi/pull/439) , [#441](https://github.com/plasma-group/pigi/pull/441) Persisted state machine for rollup client, and persist pending block

    *  [#445](https://github.com/plasma-group/pigi/pull/445), [#449](https://github.com/plasma-group/pigi/pull/449), [#446](https://github.com/plasma-group/pigi/pull/446) Rollup serialization, ABI serliazation for wallet, Wallet tree fixes and improvements

    *  [#448](https://github.com/plasma-group/pigi/pull/448) Big meaty juicy rollup contracts

  * This work is powered by the Optimistic Virtual Machine, or OVM, an abstraction created from examining architectural overlaps inherent to many L2 constructions.  The OVM is a generalized state machine which can execute a broad class of L2 protocols using optimistic game semantics. We also published a demo [State Channels on OVM blog post.](https://medium.com/plasma-group/the-ovm-%EF%B8%8Fs-your-scaling-solution-state-channel-edition-ed13de56e249) 

    * For this we've merged the following issues:

    * [#403](https://github.com/plasma-group/pigi/pull/403) Sparse Merkle Tree and MerkleInclusionQuantifier

    * [#410](https://github.com/plasma-group/pigi/pull/410) Equality Decider

    * [#428](https://github.com/plasma-group/pigi/pull/428) Implement MerkleTree.getMerkleProof(...)

    * [#450](https://github.com/plasma-group/pigi/pull/450) State receipt ingestion in rollup OVM

 **Peter from NEAR**

 _NEAR is a sharded proof-of-stake blockchain._

  * 47 PRs across 20 repos by 19 authors. Featured repos: [nearcore](https://github.com/nearprotocol/nearcore), [nearlib](https://github.com/nearprotocol/nearlib), [near-shell](https://github.com/nearprotocol/near-shell/), [near-wallet](https://github.com/nearprotocol/near-wallet), [near-bindgen](https://github.com/nearprotocol/near-bindgen), and [borsh](https://github.com/nearprotocol/borsh).

  * "Delete account" added to near shell

  * "Delete account added to nearlib

  * Generic decoder added to AssemblyScript runtime

  * Trust wallet integration in progress

  * Block queries optimized in explorer (2s -> 55ms)

  * Batch transactions exposed in Rust bindgen

  * Transaction signing in Ledger hardware wallet :)

  * Batched transactions implemented

  * NEAR <> Ethereum bridge is underway <https://github.com/nearprotocol/near-bridge>

**AJ from Tezos**

 _Tezos is a self-amending blockchain that features formally verified smart
contracts, on-chain governance, and a proof-of-stake consensus algorithm which
enables all token holders to participate in the network.  _

  * Check out the [new website](https://archetype-lang.org/) from Edukera and learn how Archetype helps to develop smarter Smart Contracts on Tezos. Archetype is a domain-specific language to develop Smart Contracts on the Tezos blockchain, with a specific focus on contract security. 

  * Tezos co-founder, Arthur, is building a coin stabilization technology for Tezos called [Checker](https://checker.is/). Checker is a software project implementing financial logic designed to help stabilize the value of a cryptographic coin with respect to an externally provided index. 

 **Topper from Quorum Control**

 _Quorum Control makes Tupelo, a permissionless proof of stake DLT platform
purpose-built to model individual objects that enables flexible public or
private data models._

  * Ongoing optimization of production Tupelo TestNets including dedicated game TestNet.

  * Developed more complex benchmarking to model and measure various read/write scenarios under load.   

  * Bumped to Go v1.13 which reduces memory requirements improving mobile browser options for WASM SDK.

 **Michael from Loom**

 _Loom Network is a platform for building highly scalable DPoS sidechains to
Ethereum, with a focus on large-scale games and social apps._

  * We have [teamed up with MakerDAO to create multichain Dai](https://medium.com/loom-network/making-a-multichain-dai-maker-and-loom-network-to-build-dai-gateways-to-tron-binance-and-other-39ca20bd2a1d). Maker will be using Loom's cross-chain gateways to bring Dai to Tron, Binance Chain, and other major chains

  * Announced a new [CryptoZombies for Libra and Move ](https://medium.com/loom-network/master-the-basics-of-libra-blockchain-development-before-everyone-else-ad699112b326)course and plans for Libra integration

  * [Loom mainnet upgrade to Basechain](https://medium.com/loom-network/basechain-is-coming-99fdb643950a), including additional validators, more rewards, staking referrals, slashing, a multichain LOOM token, new dapps, and more

  * New video developer tutorial on [how to create and deploy contracts to Loom testnet](https://youtu.be/c6lkTVTxtIA)

  * New developer guide on [how to build your own Binance Chain Token (BEP2)](https://loomx.io/developers/en/deposit-and-withdraw-bep2.html) and use Loom smart contract functionality

 **Myles from EOS**

 _EOS is a new blockchain architecture designed to enable vertical and
horizontal scaling of decentralized applications._

  * The big update this week was the [successful completion](https://twitter.com/BrendanBlumer/status/1176193670040580096) of a hard fork to EOSIO v1.8.0, which will enable dApps to manage resources on behalf of users 

  * [Block.one](http://block.one/)[hinted](https://twitter.com/BrendanBlumer/status/1174758398904033280) that they may begin voting with their stake on the EOS mainnet soon

#### Financial Infrastructure

 **Antonio from dYdX**

 _dYdX is a decentralized exchange for margin trading, borrowing, lending, and
eventually derivatives. dYdX allows traders to trustlessly short and get
leverage on crypto assets._

  * Launched Isolated Position on native dYdX ETH-DAI market!

  * Added WalletConnect: now you can connect many different mobile wallets to our desktop app

  * Added Ledger support: connect to dYdX directly through your hardware wallet

#### Layer two and interoperability

 **Tieshun from Namebase**

 _Namebase is the easiest way to buy, sell, and use Handshake._

  * Published a [comprehensive explainer](https://medium.com/namebase/meet-handshake-decentralizing-dns-to-improve-the-security-of-the-internet-708a39b0ba2) on Handshake, which was featured in the #3 spot on Hacker News. Lots of great discussion [there](https://news.ycombinator.com/item?id=20995969) as well. 

**Alexandra from Polkadot**

 _[Polkadot](https://polkadot.network/) empowers blockchain networks to work
together under the protection of shared security._

  * New guide: [Preparing for Your Parachain Auction](https://twitter.com/polkadotnetwork/status/1174356846964039680).

  * Gavin Wood's [presentation on how parathreads work is online](https://twitter.com/polkadotnetwork/status/1174368278254424064).

  * All [videos from the Polkadot developer event, DOTcon 0.5, are up](https://twitter.com/polkadotnetwork/status/1175090161308307457).

  * New info on the Polkadot wiki about [how Polkadot's BABE block production mechanism approaches randomness](https://wiki.polkadot.network/en/latest/polkadot/learn/randomness/).

  * Web3 Foundation is hiring people to [help build Polkadot](https://web3.bamboohr.com/jobs/), as well as [providing grants](https://github.com/w3f/Web3-collaboration/blob/master/grants/grants.md) for software development, research, technical education and community engagement efforts related to Polkadot. 

#### Application infrastructure

 **Alexandra from Parity Technologies**

 _Parity  Technologies builds core blockchain infrastructure, from Parity
Ethereum, an Ethereum client, to Polkadot, an interoperable blockchain
network._

  * New [PoW blockchain built on Substrate](https://twitter.com/sorpaas/status/1175036376099610625).

  * A community member created a [multisig wallet for Substrate](https://twitter.com/DappForce/status/1175787017994670081).

  * Huge [Substrate hackathon](https://twitter.com/Qinwen13250317/status/1175350725095747585) happened in Hangzhou.

  * Want to come build cool tech for a better web? [We're hiring!](https://www.parity.io/jobs/#jobs)

 **Doug from Livepeer**

 _Livepeer is a decentralized video infrastructure network, dramatically
reducing prices for developers and businesses building video streaming
applications at scale.  _

  * The design-heavy [Livepeer Primer](http://livepeer.org/primer) explains the Livepeer network, protocol, and staking in under 10 minutes.

  * GPU's can now mine Ethereum (mainnet) and transcode video through Livepeer concurrently (currently only on testnet) with minimal efficiency loss on the mining side. See [early setup instructions](https://github.com/mk-livepeer/bot-miner-setup) for alpha testers here.

  * The Streamflow scaling protocol update, including Ethereum probabilistic micropayments, is running successfully on an internal testnet and is undergoing audits and going to public testnet in the first week of October.

 **Matt from Keep Network**

 _The Keep Network is a privacy layer for public chains, enabling
interactivity with private data and interoperability across chains. It does
this with keeps, off-chain containers for private data that help smart
contracts harness the full power of the public blockchain._

  *  **tBTC:**

    * We fixed a bug about deposit forwarding the initial transfer to keep - the initial transfer included funder bond and keep payment. Only the keep payment should go to keep,

    * We introduced proper logging in t-ECDSA keep clients, the same logger we use in the random beacon,

    * We implemented an algorithm for calculating recovery ID of ECDSA signatures,

    * We iterated on the mechanism for price oracle replacement - more to come!

 **Random beacon:  **

    * We implemented a misbehaving member disqualification in distributed key generation. Every single misbehavior case is now detected and properly handled,

    * We finished the implementation of a set of integration tests covering all known misbehavior scenarios,

    * We fixed a bug related to disqualifications: we were not dropping shares of a member we found guilty of not providing correct shares,

    * We made progress on pricing for the beacon but it is not yet completed.

    * For more updates and questions join our [Slack](https://bit.ly/2FMkV6T) and check out the [Keep blog](https://blog.keep.network/).

 **Ryan from FOAM**

 _FOAM  is building spatial applications and proof of location that bring
geospatial data to blockchains and empower a consensus driven map of the
world._

  * FOAM is refining functional programming tools for a workshop at Devcon.

  * [Cliquebait](https://github.com/f-o-a-m/cliquebait) is finally about to support Geth 1.9.x, biggest benefit is using solc 0.5 means you get access to the istanbul evm instructions

  * Continuing work on Hardware developer kit.

  * [Chantrelle and purescript-web3](https://blog.foam.space/foam-developer-stack-900543944f5e) undergoing major updates 

  * Work on writing Cosmos SDK and Haskell continues to move along

  * We saw two game-changing FOAM hacks at ETH Berlin and subsequently ETH Boston 

  * The [Mapcovery project](https://www.youtube.com/watch?v=WSnmM0HCFg0) was made by the Gnosis Team and won the grand prize at ETH Berlin. Mapcovery is an innovative solution that allows users to recover their Gnosis Safe Wallet by memorizing Five Points of Interest from the FOAM Map. 

  * At ETH Boston, UniSwap created a [project](https://vimeo.com/358977168) for Decentralized Restaurant Reviews with the FOAM Map and 3Box Chat threads. [Code is here](https://github.com/ianlapham/foamdemo)!

 **David from Sia**

 _Sia is a decentralized cloud storage platform leveraging blockchain
technology to create a data storage marketplace that is more robust and more
affordable than traditional cloud storage providers._

  * The Sia team is working towards solidifying the features that will be released with Sia v1.4.2.

  * Hotfix version [1.4.1.2](http://1.4.1.2/) was released this week for Sia. It includes improvements on file downloads, and most importantly, fixes for the propagation of transactions on the network. For this last reason everybody is encouraged to [update](https://sia.tech/get-started) as soon as possible

  * A usual complain of users syncing their Sia client the first time is that the initial boot after bootstrapping the blockchain (manually downloading it) takes very long. This is because additional renter and transaction databases need to be built, but Chris has enabled instant boot: Sia will initialize immediately and allow some interactions while the databases are built in the background.

  * Work has started on the new alert system of Sia, which will present to the user alerts when something unusual happens that requires his attention. Chris has created the framework of this system and added the first two alerts: when contracts fail to be formed or renewed due to low funds and alerts for files with a dangerously low redundancy.

  * To facilitate checking this new alert system, community contributor tbenz9 has added the new siac alerts command for printing all the alerts emitted by the Sia daemon.

  * Matt added the new API endpoint renter/uploadready to facilitate third-party apps to know when Sia is ready to upload files.

  * Chris added unique IDs to each downloads and the endpoint renter/downloadinfo to check them.

  * Community member @Rezant [released version](https://www.reddit.com/r/siacoin/comments/d5w1es) 1.0.3 of his Sia Central Host Manager app, which provides an easy and feature-rich experience for Sia hosts. This new version includes the possibility of bootstrapping the blockchain on your first start up, better validation of settings and other bug fixes

#### Other

 **Dave from Decentraland**

 _Decentraland is a virtual world where you can build and explore 3D
creations, play games and socialize._

  * Design and development event, [Game Jam 2019](http://gamejam.decentraland.org/) kicked off on Sept. 16. It runs for another week until the 30th. Over $250k USD in prizes up for grabs

  * Video tutorial series on working with the SDK released in full on our [YouTube channel](https://www.youtube.com/channel/UCLXcTgzr05cFZaN972nuEXw)

  * SDK: We improved feedback for entities out of scene bounds and implemented bug fixes with player movement, materials, P2P communication and exporting to 3rd-party servers

  * Builder: Custom Asset Packs released, allowing creators to add and manage their own 3D assets in the Builder, for a more personal Decentraland

  * Builder: Scaling introduced, allowing creators to set the size of models they use, giving them further flexibility with their creative scenes  

 **Bowen from Hydro/DDEX.io**

 _Hydro  Protocol is an open source framework for building Decentralized
Exchanges. DDEX is the first decentralized exchange for Ethereum and ERC-20
tokens built on the Hydro Protocol. _

  * [Margin.ddex.io](http://margin.ddex.io/) ready to beta launch on 10/8. 

  * Oracle development - Identified issue in the oracle and fixed 

  * DeFi. WTF  <https://www.defi.wtf/> Preparation ongoing with Community members for Osaka Devcon. 

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

