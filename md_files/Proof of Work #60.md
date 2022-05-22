[![](https://substackcdn.com/image/fetch/w_96,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F37b09348-f4f1-47a2-b9e0-a2007299e6e4_256x256)](https://proofofwork.news)

# [Proof of Work](https://proofofwork.news)

SubscribeSign in

Share this post

Proof of Work #60

proofofwork.news

Copy link

Twitter

Facebook

Email

# Proof of Work #60

[Eric Meltzer](https://substack.com/profile/138320-eric-meltzer)

Mar 28, 2019

[Share](javascript:void\(0\))

Hi from increasingly warm Boston! Something I’ve been curious about for a
while is how the social differences in Proof of Stake vs. Proof of Work will
affect the security of those two systems. Many PoS adherents emphasize its
similarity to PoW by saying that stake can be thought of as “virtualized
ASICs” and that the security model should be in many ways identical. Recently
I’ve been lurking in some private groups for people running EOS, Cosmos, and
IOST validators/block producers in order to understand more about how the PoS
sausage is made. The thing that leapt out at me was how _social_ PoS is. The
various validators know eachother, talk to eachother, and often try and
collude or break collusion (for example setting fee floors etc) in the course
of a given days worth of messages.

This is in stark contrast to PoW miners, who rarely talk to eachother, and
have thus far never made a very serious attempt at collusion.

I think there are two major forces driving this disparity:

  1. Proof of Stake validation capex is an infinitesimal fraction of PoW capex, so the main competitive edge one can get is increasing the stake AUM via delegation (essentially increasing ones block reward for “free”). To do this one needs to be loud, and social! You need to go get to know all the big stakeholders, and this leads to an atmosphere which is conducive to collusion. In PoW, to increase the amount of coinbase reward you get, you just need to bring more ASICs online. 

  2. PoS validators are mostly being used in systems with complex rulesets around smart contracting, which leads to the need for intervention (i.e. EOS’s fund recovery stuff, etc) whereas the main PoW coin wants nothing more from miners than SHA256 nonces. Thus, in PoS systems unfriendly collusion has a nucleation point around the already ongoing discussions about what types of transactions and featuresets to support, whereas in PoW collusion would have to start purely for the sake of collusion. To be clear I do not think this is an inherent feature of PoS but rather a coincidence of what systems are using what consensus algos. 

I think PoS (and the Stellar consensus algo) remain the most interesting
alternatives to classical PoW, and wish PoW diehards would be less dismissive
of them outright, but at the moment I’m pretty unimpressed by the state of the
art. I will keep an eye on how these systems develop—stuff like Cosmos is a
fascinating test at scale of how a really well-engineered PoS system will
develop, and anyone interested in crypto should be watching them closely.

In other news, Blockstream has finally released a really good Bitcoin [mobile
wallet](https://itunes.apple.com/app/id1402243590). As one would expect from
the company that employs more Bitcoin Core devs than any other, it has a bunch
of features that most mobile wallets leave out, like the ability to increase
the fee attached to a transaction if fees get higher and you need something to
go through quickly, a 2 of 2 multisig with a really clever timelock [recovery
mechanism](https://github.com/blockstream/gdk), the ability to set a threshold
after which 2FA is necessary (so you can send your friend 100$ in BTC when you
lost a bet with no hassle, but an attacker can’t take your entire balance)
etc. After playing around a bit, this is definitely my go-to Bitcoin mobile
wallet rec.

#### Bitcoin & Friends

 **Jimmy on Bitcoin**

 **[Optech](https://bitcoinops.org/en/newsletters/2019/03/12/) on Bitcoin [ed:
sign up for their newsletter too! it’s great!]**

  * Version 2 P2P transport proposal: Jonas Schnelli sent a [proposed BIP](https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2019-March/016806.html) to the Bitcoin-Dev mailing list that specifies an algorithm to be used to encrypt traffic between peers. It also specifies some other minor changes to the creation of protocol messages, such as allowing peers to use bandwidth-saving short identifiers and eliminating the SHA256-based checksum on messages, as the [AEAD](https://en.wikipedia.org/wiki/Authenticated_encryption)-based encryption scheme protects data integrity

  *  **Loop announced:**  Lightning Labs [announced](https://blog.lightning.engineering/posts/2019/03/20/loop.html) a new tool and service to facilitate  _submarine swaps_ , HTLC-based atomic swaps of offchain bitcoins for onchain bitcoins. In essence, Alice sends Bob an LN payment secured by a secret she knows, preventing Bob from claiming it. Bob then creates an onchain payment that Alice can spend by revealing the secret. Alice waits for the payment to receive a suitable number of confirmations and then spends it onchain to any address she chooses—revealing the secret in the process. Bob sees Alice’s onchain transaction and uses its revealed secret to claim the LN payment Alice sent him earlier. If Alice doesn’t reveal the secret, the onchain payment contains a refund condition that allows Bob to spend it back to himself after a timelock expires.

  *  **Square Crypto developer group announced:**  the CEO of Square [announced on Twitter](https://twitter.com/jack/status/1108487911802966017) that they are forming a group to employ several contributors to open source Bitcoin projects, including both developers and a designer. See their announcement for application instructions. (Note: Square is also a sponsoring member of Optech.)

 **James from Summa**

 _Summa builds tools to exchange crypto in a convenient and trustless
fashion._

  * Barbara and the frontend team are hard at work polishing the new wallet app

  * As part of a new integration, the research team has designed a novel cross-chain relay mechanism. Look for an introductory blog post soon :)

 **Tony from Kadena**

 _Kadena is building Pact, a formally verifiable smart-contracting language
for financial applications, and Chainweb, a PoW blockchain that uses multiple
chains in parallel to increase throughput._

  * “Kadena just went live with [Chainweb Testnet](https://medium.com/kadena-io/announcement-kadena-public-blockchain-testnet-live-dbfb8a6477c5) for our public blockchain! We’re proud of the whole team for shipping a scalable proof of work blockchain that is environmentally friendly. If you’re in NYC and want to see a demo, come to our meetup tonight (3/27) at 6pm. Below are bullets of what’s in v0 of Chainweb Testnet along with other updates.”

  * For a detailed description of Chainweb’s architecture, [see here](https://github.com/kadena-io/chainweb-node/blob/master/docs/Architecture.md).

  * Download and test the network yourself with a [chainweb-node](https://github.com/kadena-io/chainweb-node).

·      v0 includes 10 chains as we are testing the security and stability of
braiding multiple Bitcoin-like (proof of work) chains.

·      v0 is testing global latencies by syncing across servers in Asia,
Europe, North America, and South America.

·      v0 supports transactions written in Pact, Kadena’s open-source smart
contract language that is easy to learn and purpose-built for blockchain.

·      v0 is private but open source on [Github](https://github.com/kadena-
io/chainweb-node) so you can look at the code as well as compile and run your
own network & tests. We plan for v1 to offer a mining client; [sign up
here](https://upscri.be/26f493/) to get on the mining list.

·      Chainweb is designed to provide blockchain scalability  _and_  security
through its multi-chain configuration. We believe it is the first of its kind.
For more about Chainweb, check out the [101/FAQs](https://medium.com/kadena-
io/all-about-chainweb-101-and-faqs-6bd88c325b45) and read the
[whitepaper](https://kadena.io/docs/chainweb-v15.pdf).

  * Tony Pham wrote a Medium post on [Kadena’s roadmap to a hybrid blockchain](https://medium.com/kadena-io/kadenas-roadmap-to-a-hybrid-blockchain-platform-dc0ff7c178a6) platform, sharing learnings and milestones as the company looks ahead in 2019.

  * Will Martino (Kadena CEO) and Kyle Samani (Multicoin Capital Managing Partner) hosted an AMA on PoW and PoS on [Kadena’s Discord](https://discordapp.com/invite/bsUcWmX) on March 20.

  * Will was interviewed by CoinDesk’s Nolan Bauerle about Kadena’s blockchain platform on the [Road to Consensus](https://www.coindesk.com/podcasts/road-to-consensus/will-martino-who-needs-private-blockchains) podcast which was published on March 20.

  * Will was interviewed on [The Blockchain Show](http://www.theblockchainshow.com/season2-episode-117-kadena-will-martino) podcast that aired on March 21.

  * Kadena founders Stuart Popejoy and Will Martino were interviewed by Anthony Pompliano on the [Off the Chain](https://player.fm/series/off-the-chain-2428336/stuart-popejoy-will-martino-co-founders-of-kadena-the-intersection-of-public-and-private-blockchains) podcast episode that aired on March 22.

 **Aviv from Spacemesh**

 _Spacemesh is a programmable cryptocurrency powered by a novel proof-of-
space-time consensus protocol._

  * [NIPST construction flow](https://github.com/spacemeshos/go-spacemesh/commit/c70e6383d128996509cc2e4d204eb478f95aa8c4)

  * Updated [P2P Ping protocol](https://github.com/spacemeshos/go-spacemesh/commit/6a50382ec8842db4eef4930fa616460bacf3504d)

  * Limiting number of [P2p ingress connections](https://github.com/spacemeshos/go-spacemesh/commit/705ac1caeb60ac5212261bee3d77a9ec1858c185)

  * New [POET service tests](https://github.com/spacemeshos/poet-ref/commit/fc2c24f7a98867b31b849ccfcbbf508c177de411)

  * POST Merkle tree - [unbalanced trees support](https://github.com/spacemeshos/merkle-tree/commit/1a334a4997301c9db11b74d1bf8811f54a2329c1)

  * Testnet interactive guide - [updated content](https://testnet.spacemesh.io/)

  * mut full_update := { <https://spacemesh.io/weekly-updates/> }

 **JZ from Decred**

 _Decred  is an autonomous digital currency with a hybrid consensus system. It
is built to be a self-ruling currency where everyone can vote on the rules and
project-level decision making proportionately to their stake._

  * We're super pleased to launch <https://timestamp.decred.org/>, a web fronted for [dcrtime](https://github.com/decred/dcrtime) which allows users to anchor unlimited records to the Decred blockchain for free (dctime built upon the work of Peter Todd's OpenTimestamps). It achieves this by creating a Merkle tree with all the hashes it receives and then anchors the Merkle root in the OP_RETURN field of an on-chain transaction it creates on an hourly basis. So basically, anybody can take any amount of data and create a cryptographic record of its existence at a certain point of time while keeping their data totally private.

  * We also just released version 4.0 of [dcrdata](https://explorer.dcrdata.org/) our Decred block explorer written from scratch in Go. It comes with a number of performance and UI improvements as well as sweet charts. It's quite cool to visualize things like the [Decred network hashrate increasing 1,000x](https://explorer.dcrdata.org/charts?chart=hashrate) in just over a year.

  * Our consensus vote to activate [DCP-0004](https://github.com/decred/dcps/blob/master/dcp-0004/dcp-0004.mediawiki) and enable Lightning Network is still ongoing. There have been some interesting discussions as of late on participation in cryptocurrency governance among projects that attempt to empower their stakeholders. What we're seeing with the current vote is that of the ~47% of Decred in existence that is locked in PoS ~53.5% are actively participating in this consensus vote so far. The vote can be followed on <https://voting.decred.org/> and it currently has 99.97% support.

 **Johnny from Stellar**

 _Stellar is an open network for sending and exchanging value of any kind. Its
global network enables digitization of assets - from carbon credits to
currencies - and enables movement around the internet with ease._

  * Core - 10.3.0 released, rollout uneventful so far (a good thing); expanding quorum set as validators upgrade

  * Core - V11 - Protocol changes landing: Cap0005, cap0006 in code review, cap0020 shortly

  * Platform - Release of Horizon 0.17.4 went smoothly

  * Platform - Bartek in SF next week, working on new Horizon ingestion prototype with core team

  * Platform - New Go SDK on track to be ready end of Q1

  * Platform - Nikhil starting work on basic Kelp web UI

 **Izaak from Coda**

 _Coda is the first cryptocurrency protocol with a constant-sized blockchain.
Coda compresses the entire blockchain into a tiny snapshot the size of a few
tweets using recursive zk-SNARKs._

  * Matthew [reduced witness generation time](https://github.com/o1-labs/snarky/pull/148) attributable to Snarky by >2.5x. 

  * Nathan [rewrote](https://github.com/CodaProtocol/coda/pull/1820) our logging infrastructure, upgraded our JSON logging format to support value interpolation, and optimized our log processor. 

  * Echo [refactored and documented](https://github.com/CodaProtocol/coda/pull/1924) how we synchronize merkle tree ledgers and patched a potential vulnerability which could allow peers to answer unasked messages.

#### Privacy coins

 **Paige & Zooko from Zcash**

 _Zcash is a  digital currency utilizing zk-SNARKs to enable its privacy-
protecting properties._

  * A [security announcement was posted in the forum](https://forum.zcashcommunity.com/t/zcashd-security-announcement-2019-03-19/32972) regarding a bug in the Zcashd wallet, which could result in Sprout z-addresses displaying an incorrect balance. Sapling z-addresses are not impacted by this issue. This would occur if someone sending funds to a Sprout z-address intentionally sent a different amount in the note commitment of a Sprout output than the value provided in the ciphertext (the encrypted message from the sender). A code fix for the wallet has been written and the integration into an official Zcash release is targeted for our next release (version 2.0.4, expected March 25th).

  * We developed consensus code that preserves the Zcash monetary base in the event of a counterfeiting compromise within Zcash’s shielded supply. We intend to deploy this as a backwards compatible consensus rule in the Zcashd v2.0.5 release, scheduled for the beginning of May. We believe this new rule does not materially affect users and is low-risk to deploy. Read more about [turnstile enforcement against counterfeiting](https://z.cash/blog/turnstile-enforcement-against-counterfeiting/), including tracking shielded value pools and codifying the existing policy.

  * Jack Gavigan, Product and Regulatory Relations, outlined why [Zcash is Compatible with AML/CFT Regulation](https://z.cash/blog/zcash-is-compatible-with-aml-cft-regulation/): “From an AML/CFT perspective, Zcash is similar in nature to cash..." 

  * [eToro released a market research report](https://www.etoro.com/wp-content/uploads/2019/03/ZEC.pdf) which concluded, “Zcash is … reinventing the way people think about privacy coins.

 **Mitchell from Monero**

 _Monero is a open-source, privacy-focused cryptocurrency using the ASIC-
resistant CryptoNote PoW algorithm. It enforces all privacy features at the
protocol level to ensure that all transactions create a single fungible
anonymity pool._

  * Translating 8 new languages for the GUI: Kurdish, Bengali, Persian, Irish, Urdu, Zulu Greek and Nepali. If you speak a language besides English, we [welcome your translations](https://github.com/monero-ecosystem/monero-translations/blob/master/pootle.md).

  * Had a special 2.5 hour [developer meeting](https://repo.getmonero.org/monero-project/monero-site/blob/b87354501b6343f9146f331805ddadc45696f728/_posts/2019-03-24-logs-for-the-dev-meeting-held-on-2019-03-24.md) to discuss the future of Monero’s approach toward proof of work algorithms, most likely RandomX with an ASIC-friendly SHA-3 fallback. Summaries can be found [here](https://www.reddit.com/r/Monero/comments/b50mfy/logs_from_the_25_hr_dev_meeting_on_moneros_pow/).

  * We’re beginning to thoroughly review the RandomX proof of work algorithm. Every set of eyes helps, so check out the [design](https://github.com/tevador/RandomX/blob/master/doc/design.md) and [specs](https://github.com/tevador/RandomX/blob/master/doc/specs.md).

 **Daniel from Grin**

 _Grin is a community-driven implementation of the Mimblewimble protocol that
aims to be privacy preserving, scalable, fair, and minimal._

  * [13 Pull Requests were merged](https://github.com/mimblewimble/grin/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A2019-03-18..2019-03-24+) in the past week, by 8 unique contributors.

  * [Dandelion++ rewrite](https://github.com/mimblewimble/grin/pull/2628) by @antiochp is in for v1.1.0.

  * v1.1.0 and v1.0.3 release timelines and scheduled hard fork process were among the things discussed in [the latest dev meeting](https://github.com/mimblewimble/grin-pm/blob/master/notes/20190319-meeting-development.md).

  * @yeastplume has been busy with [getting rustdoc working for Wallet API v2](https://www.grin-forum.org/t/yeastplume-progress-update-thread-mar-19-to-sep-19/4303/12).

  * Investigation to look into [alternatives to TravisCI](https://github.com/mimblewimble/grin/issues/2691).

  * @taek provided some [details on the GRN1 ASIC miner from Obelisk](https://www.grin-forum.org/t/obelisk-grn1-chip-details/4571) which prompted a much wider discussion regarding the phase out schedule and ASIC manufacturing in general, with participation from Innosilicon as well.

  * @phooton announced [GrinPro2](https://www.grin-forum.org/t/grinpro-2-first-to-get-5-gps-on-vegas/4603) miner in beta - achieving 5GPS on Vegas chips.

  * [Wallet for Grin++](https://www.grin-forum.org/t/announcing-the-grin-wallet-finally/4546), the C++ implementation of Grin, is now live after work by @DavidBurkett

  * [Vite: A new mobile wallet for Grin](https://www.grin-forum.org/t/here-comes-the-sketch-of-grin-mobile-wallet/4555) in development.

  * More Grin info [here](https://grinnews.substack.com/).

 **Beni from Beam**

 _Beam is a confidential and scalable cryptocurrency based on Mimblewimble._

  * Beam will co-host the [Building the new web Event in Seoul](https://www.eventbrite.nl/e/building-the-new-web-seoul-with-beam-algorand-nervos-ocean-protocol-tickets-58852705025), April 3rd 2019

  * Great initiative from Beam Community with <https://beamprivacy.community/>

  * Dev. Team will attend [The 2nd ZKProof Workshop in Berkeley](https://zkproof.org/workshop2/main.html), CA on April 10-12th 2019

  * We have released [Testnet Bright Boson 2.0.4707](https://github.com/BeamMW/beam/releases/tag/testnet_bb_2.0)

  * Team Beam attended [Blockchain UA](https://blockchainua.com/en), on March 22nd 2019

  * We have launched our [official blog in Russian](https://medium.com/beam-russian)

  *  Testnet Bright Boson 2.0.4707- [Release Notes](https://github.com/BeamMW/beam/releases/tag/testnet_bb_2.0)

  * [Android wallet](https://github.com/BeamMW/android-wallet) Testnet - [Release Notes](https://github.com/BeamMW/android-wallet/releases/tag/Testnet-1.0.16)

  * UI wallet [ #552](https://github.com/BeamMW/beam/issues/552),  [#476](https://github.com/BeamMW/beam/issues/476)

  * CLI wallet [#249](https://github.com/BeamMW/beam/issues/249),  [#248](https://github.com/BeamMW/beam/issues/248)

  * Documentation [#527](https://github.com/BeamMW/beam/issues/527)

  * UI wallet [#446](https://github.com/BeamMW/beam/issues/446), [#380](https://github.com/BeamMW/beam/issues/380)

  * API [#519](https://github.com/BeamMW/beam/issues/519) , [#515](https://github.com/BeamMW/beam/issues/515), [#536](https://github.com/BeamMW/beam/issues/536) ,[#537](https://github.com/BeamMW/beam/issues/537), [#528](https://github.com/BeamMW/beam/issues/528), [#548](https://github.com/BeamMW/beam/issues/548)

  * MacOS binaries signature [#517](https://github.com/BeamMW/beam/issues/517)

  * Fast sync [#407](https://github.com/BeamMW/beam/issues/407) [#454](https://github.com/BeamMW/beam/issues/454)

  * Payment proof [#415](https://github.com/BeamMW/beam/issues/415)

  *  Atomic Swap CLI [#447](https://github.com/BeamMW/beam/issues/447)  _in progress_

  * [iOS  wallet ](https://github.com/BeamMW/ios-wallet/projects/1)Testnet   _in progress_

  * Hardware wallet - Trezor  _in progress_

  * One side payments   _in progress_

  * [147 open issues](https://github.com/BeamMW/beam/issues) and [398 closed issues](https://github.com/BeamMW/beam/issues?q=is%3Aissue+is%3Aclosed)

  * [60 commits](https://github.com/BeamMW/beam/graphs/commit-activity) by 7 unique contributors

 **Arnaud from AZTEC Protocol**

 _AZTEC Protocol is an efficient zero-knowledge protocol built on top of
Ethereum, making plug-and-play value transmission and asset governance privacy
tools for developers and companies.  _

  * We merged [4 pull requests](https://github.com/AztecProtocol/AZTEC/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A2019-03-17..2019-03-24+) this week, including our [new proof versioning work](https://github.com/AztecProtocol/AZTEC/pull/68), adding [test coverage tooling](https://github.com/AztecProtocol/AZTEC/pull/76), and various cleanups and bug fixes prior to our audit

  * We released a draft full [specification](https://github.com/AztecProtocol/specification) of the AZTEC protocol, including data structures and program flows

  * This week we’re finishing up [minting and burning in fully private assets](https://github.com/AztecProtocol/AZTEC/pull/73) including by integrating the new proof versioning work

  * Our CTO Zac Williamson presented [at zk0x03](https://twitter.com/zeroknowledgefm/status/1109046346185670657)

  * We’re hiring for **** two cryptographers and one senior engineer to join the team. You can apply [here](http://email.mg2.substack.com/c/eJwlUEuOwyAMPU3ZNSKQpGHBoq1mrhHxcVumBEfgTJU5_RBF8sKy_fw-zhA8MW96wUJsLZCn4LVQgg8t87rz7diPLJTpkQFmE6KmvAJbVhuDMxQw7fe9kuylwUnVg3RcXQYu7eDAenvpjOx5Lweh2M4xmdUHSA40_ELeMAGL-kW0lJO8nsR3LZOeEBuHe_tH4M5LRkKH8Szr6AdtYUEL3iouRcs7LjvRtM2NX-_jnY-3QbS37ut66vj8FE1ZbSHj3vXfzLI2OVUBdecy-EBzSNQEPJTRtoBO8CkRiCAzOkKpXqcKntcUaJsgGRvB6wNSvUt1kQOrNB5rPklXsfjAxwfz-x-f0nXk), or by emailing [arnaud@aztecprotocol.com](mailto:arnaud@aztecprotocol.com) with the name of the role as the subject.

#### Smart contracting platforms

 **Evan from[Ethereum](https://weekinethereumnews.com/)**

 _Ethereum  is a decentralized platform for applications that aims to resist
fraud, censorship or third-party interference._

  * Counterfactual releases [Playground](https://medium.com/statechannels/development-update-3-counterfactual-playground-release-f428be4b8950) developer alpha with demo environment and multiple demo applications. Go build with generalized state channels

  * How [Vitalik sees](https://www.reddit.com/r/ethtrader/comments/b2z0l3/into_the_ether_vitalik_buterin_current_and_future/eiwozk2/) Eth’s strategy: “Ethereum is best suited to continue to provide value and prosper in the presence of a growing number of such chains by going for the “stable L1, no on-chain governance, focus more innovation on L2 over time” approach, ie. basically moderate bitcoin values, except that it’s actually a very defensible position when you have a scalable data layer and any kind of richly-stateful VM at all at L1”

  * Two great dev tool update: [Ganache v2.0](https://github.com/trufflesuite/ganache/releases/tag/v2.0.0) and [Embark v4.0](https://embark.status.im/news/2019/03/19/introducing-embark-4/) 

 **Erik from NEAR**

 _NEAR is a sharded proof-of-stake blockchain._

  * 17 PRs in [nearcore](https://github.com/nearprotocol/nearcore) from 10 different authors

  * We can now run a multi-node Proof-of-Authority version of our network

  * Follow [the documentation](https://docs.nearprotocol.com/tutorials/testnet-alpha-multi-node) to launch your own network and attach our studio IDE to it

  * Implemented the first version of concurrency model checking for our Nightshade consensus algorithm

  * Updated runtime WASM API to support faster reads and writes

  * Streamlined command line tools for local development, testing, and deployment

  * Benchmarks for the client excluding network and consensus

  * Improved APIs and integration tests for DevNet while improving stability

 **AJ from Tezos**

 _Tezos is a self-amending blockchain that features formally verified smart
contracts, on-chain governance, and a proof-of-stake consensus algorithm which
enables all token holders to participate in the network.  _

  * The first Tezos amendment vote has successfully concluded, Athens A won the majority by gathering a total of 18,181 votes out of a total of 25,855 votes. Athens A proposes to increase t the gas limit + reduce the staking threshold of 10,000 XTZ to 8,000 XTZ. [These two changes will now go through an exploration phase](https://tzscan.io/proposals) that requires a 80% quorum. 

  * [Nomadic Labs is working on future amendments for proposals](https://blog.nomadic-labs.com/meanwhile-at-nomadic-labs-2.html): zk-SNARKS and tendermint consensus are planned for this year. 

  * [Introducing Mi-Cho-Coq](https://blog.nomadic-labs.com/meanwhile-at-nomadic-labs-2.html): A framework for the Coq proof assistant to specify Michelson smart contracts and prove properties about them.

  * Trezor has enabled built-in baking and endorsing for its hardware wallet.

 **Topper from Quorum Control**

 _Tupelo is a permissionless proof of stake DLT platform purpose-built to
model individual objects that enables flexible public or private data models._

  *  **New release 0.1.0 released:**

  * Incorporates the actor model for improved performance and maintainability

  * Improves troubleshooting options adding open tracing

  * Adds an ipld chaintree storage adapter

  * Includes automated docker builds

  * Read our use-case analysis “[DLT for the supply chain](https://medium.com/@KevinTharayil/use-case-analysis-distributed-ledger-for-the-supply-chain-3cbd9dcf9b1e)”  

**Michael from Loom**

 _Loom Network is a platform for building highly scalable DPoS sidechains to
Ethereum, with a focus on large-scale games and social apps._

  * [Integrating both EOS and TRON into PlasmaChain](https://medium.com/loom-network/connecting-ethereum-eos-and-tron-making-blockchain-interoperability-a-reality-e5ef6c67716). With this, PlasmaChain effectively becomes a universal layer 2, connecting Ethereum, EOS, TRON, and Cosmos (with more to come). 

  * Now [over 121M tokens have been staked on the network](https://twitter.com/loomnetwork/status/1110103341583892482), which amounts to ~18% of circulating supply. 

 **Myles from EOS**

 _EOS is a new blockchain architecture designed to enable vertical and
horizontal scaling of decentralized applications._

  * No updates this week.

 **Zaki from Cosmos**

 _The  Cosmos Network is a decentralized network of independent, scalable, and
interoperable blockchains._

  * We hits 100 million atoms out of 236 millions Atoms staked.   
The first Cosmos Hub governance
[proposa](https://hubble.figment.network/chains/cosmoshub-1/governance/proposals/1)l
is being voted on.

  * We kicked off the first implementer's call for [Cosmos IBC](https://www.youtube.com/watch?v=LTgntJt9E8Y&t=2s). The IBC protocol is being specified in the [Interchain Standards Repo.](https://github.com/cosmos/ics)

  * A draft [proposal](https://forum.cosmos.network/t/proposal-plan-for-enabling-atom-transfers/1744/11) to enable Atom transfers is in proces.  
[Version 0.34 of the Cosmos SDK](https://github.com/cosmos/cosmos-
sdk/projects/31) is in process and with the approval of governance will be
part of the transfers enabled upgrade.

 **Kate and Dean from Agoric**

 _Founded by pioneers in secure development and distributed systems, Agoric
uses a secure subset of JavaScript to enable object capabilities and smart
contracts._

  * Mark wrote [the draft specification for a standalone SES engine](https://github.com/Agoric/SES/blob/master/docs/draft-standalone-spec.md). Rather than taking an existing JavaScript engine and creating a SES runtime within it, this would be SES compliant from the beginning, meaning that many of the problematic and non-deterministic parts of JavaScript just wouldn’t exist in the first place.  

  * Agoric's new ["SwingSet" vat implementation](https://github.com/Agoric/SwingSet) is now feature complete and passes all tests, including the ERTP contract host examples (Mint, Purse, ContractHost, and Escrow Agent). 

#### Financial Infrastructure

 **Antonio from dYdX**

 _dYdX is a decentralized exchange for margin trading, borrowing, lending, and
eventually derivatives. dYdX allows traders to trustlessly short and get
leverage on crypto assets._

  * Testing initial version of our new margin trading product. Gearing up for a private alpha release in a few weeks

  * Reach out to us at contact@dydx.exchange if you'd like to participate as an alpha user!

  * Work trialing an engineering as well as a design candidate

  * [Hiring](https://boards.greenhouse.io/dydx) engineers & product designers full-time in SF

 **Brendan from Dharma**

 _Dharma is the easiest place to borrow and lend cryptocurrencies. It enables
non-custodial peer-to-peer lending through smart contracts on Ethereum._

  * We had our best week ever with over 250k USD in borrow volume. We're on track to do .5M in borrow volume in March

  * Based on the increasing Maker stability fee and demand for borrowing DAI, this week's APR for DAI will be 5.5%

  * This week we are raising our transaction limits to 250k USD and 2k ETH

  * We're hiring full stack developers in SF. No crypto experience necessary. If interested, shoot us an email ([nadav@dharma.io](mailto:nadav@dharma.io) or [brendan@dharma.io](mailto:brendan@dharma.io)) or [apply here](https://angel.co/dharma-labs/jobs)

 **Coulter from MakerDAO**

 _Maker is comprised of a decentralized stablecoin, collateral loans, and
community governance._

  * An executive vote to increase the Stability Fee to 7.5% has gone live. You can read more [here](https://blog.makerdao.com/executive-vote-stability-fee-of-7-5/) or join the discussion on our [subreddit](https://www.reddit.com/r/MakerDAO/).

  * Thanks to boxylabs, you can now get Dai directly [within a tweet](https://twitter.com/boxylabs/status/1109096315336581120). Pretty neat functionality! 

  * You can now book a vacation in Dai. [Travala](https://www.travala.com/) added Dai as a native payment to their platform. Aloha & Mahalo! 

  * The team at Dether created a [bridge between Dai and cash](https://medium.com/dether/you-can-now-become-a-token-atm-without-holding-tokens-e42cf2c9d3ac). So you can buy and sell Dai for cash. 

  * Dai is also integrated into [0x Instant](https://0x.org/instant), making it super easy to add Dai purchasing to any app or website. 

 **Lazar from MARKET Protocol**

 _MARKET Protocol is a framework for creating tokens that track prices of
traditional or digital assets._

  * Last week we focused on bug fixes and preparing a release candidate of MPX, our DEX

  * We will not add new features until after mainnet launch

  * Next up is penetration testing and our security audit

  * Soon we will share more information about our mainnet release timeline

 **Robert from Compound**

 _Compound is a money market protocol on the Ethereum blockchain — allowing
individuals, institutions, and applications to frictionlessly earn interest on
or borrow cryptographic assets without having to negotiate with a counterparty
or peer._

  * [Announced Compound v2](https://medium.com/compound-finance/compound-v2-fe4b1fb62abb), an upgraded version of the Compound protocol that will support a wider array of assets

  * Continued security audits for Compound v2

#### Layer two and interoperability

 **Tieshun from Namebase**

 _Namebase is the easiest way to buy, sell, and use Handshake._

  * No updates this week.

 **Paul from Veil**

 _Veil  is a peer-to-peer prediction market and derivatives platform built on
top of Augur, 0x, and Ethereum._

  * Added search to the [Veil homepage](https://app.veil.co/) to make it easier to find markets.

  * Created market-specific Discord channels and linked to them from markets in Veil.

  * [New user profiles](https://app.veil.co/u/tr33) that show markets created by that user in addition to their activity.

 **Rahul from 0x**

 _0x_  is an open protocol that enables the peer-to-peer exchange of assets on
the Ethereum blockchain.

  * Hosting a [0x meetup](https://www.meetup.com/0xCommunity/events/259742676/?_xtd=gqFyqTI3NjUwNDEyMqFwo3dlYg&from=ref) this Thursday March 28th in San Francisco

  * [0x Roadmap Part 2](https://blog.0xproject.com/0x-roadmap-2019-part-2-scalability-r-d-c0fc2d5101e5), Scalability R&D: our research engineer Remco dives into ZKPs (zero knowledge proofs)

  * [Dai integration](https://twitter.com/MakerDAO/status/1107671168390033408) with 0x Instant: with just a few lines of code, add Dai purchasing to your website

 **Tony from Liquidity.Network**

 _Liquidity Network is a transfer and swap platform for any token_

  * [The Liquidity's first Asia meetup](https://www.eventbrite.com/e/unblock-bangkok-blockchain-scalability-challenges-and-future-directions-tickets-58697726480) will be at Bangkok, Thailand on 26 March. Come and join us!

  * [Pitch Night Finale for Future of Blockchain event](https://medium.com/future-of-blockchain/inaugural-future-of-blockchain-pitch-day-finale-the-finalists-c362df68897a). Representing Liquidity Network is Liquidity Stream. Built by a team of four from Imperial, Liquidity Stream uses Liquidity Network’s NOCUST protocol for pay-as-you-watch-video-on-demand.

  * Our [second Asia meetup](https://www.eventbrite.com/e/unblock-saigon-blockchain-scalability-challenges-and-future-directions-tickets-58845608800) will be held at Ho Chi Minh Vietnam on 28 March. See you all there!

  * Liquidity Network has the honor to be a platinum sponsor of [1st International Summer School on Security & Privacy for Blockchains and Distributed Ledger Technologies.](https://bdlt.school/)

  * [The new hub with passive delivery](https://etherscan.io/address/0x83afd697144408c344ce2271ce16f33a74b3d98b) was rolled out to production on the Ethereum mainnet

 **Dong Mo from Celer**

 _Celer Network is a layer-2 scaling platform that enables fast, easy and
secure off-chain transactions for not only payment transactions, but also
generalized off-chain smart contracts._

  * We have finished player matching API validation on CelerX. 

  * We are continuing the development of game platform UI design. 

  * We have developed popups during and after the game. 

  * We added a game result screen and finished quick match data integration. 

  * We finalized design of CelerX platform client/servers interactions and continuing the development of CelerX server code. 

  * We are implementing on-chain dispute flow in new OSP protocol and preparing to open-source cChannel 1.0.

 **Alexandra from Parity Technologies**

 _Parity  Technologies builds core blockchain infrastructure, from Parity
Ethereum, an Ethereum client, to Polkadot, an interoperable blockchain
network._

  * New article: [A brief summary of everything Substrate and Polkadot](https://www.parity.io/a-brief-summary-of-everything-substrate-polkadot/)

  * New [Substrate sample](https://github.com/gautamdhameja/substrate-inherents-sample) shows how to use inherents in your custom modules.

  * At Zero Knowledge Summit, Marek Kotewicz gave a [first peek at the Zcash client](https://twitter.com/zeroknowledgefm/status/1109113361780953089) we're building with the Zcash Foundation

  * Ocean Protcol has documentation on [how they use Parity Secret Store](https://twitter.com/FabianGompf/status/1108365780188581889)

  * We [signed an open letter](https://twitter.com/ParityTech/status/1107955651613995009) urging Members of the European Parliament to vote against Article 11 and 13.

  * Interested in building on Polkadot? The Web3 Foundation is [providing grants.](https://www.parity.io/jobs/)

  * Like talking to devs and traveling? [We're hiring a Tech Ambassador.](https://twitter.com/ParityTech/status/1101052488344653824)

#### Application infrastructure

 **Wes from Theta**

 _Theta is an end-to-end infrastructure for decentralized video streaming._

  * No update this week

 **Doug from Livepeer**

 _Livepeer is a decentralized video infrastructure network, dramatically
reducing prices for developers and businesses building video streaming
applications at scale.  _

  * Work continued on [transcoder redundancy and failover](https://github.com/livepeer/go-livepeer/issues/775). The aim is to provide a high level of reliability for video applications in using the network that surpasses multi-cloud centralized architectures.

  * [Assessing metrics for video quality verification](https://medium.com/@epiclabs.io/assessing-metrics-for-video-quality-verification-in-livepeers-ecosystem-f66f724b2aea) in Livepeer, a post by Epic Labs.

  * Scout.cool [takes a deeper look into the economics of running transcoders](https://forum.livepeer.org/t/transcoder-analytics-part-2-do-you-really-understand-the-income-of-a-transcoder/613) under various reward strategies.

 **Ryan from FOAM**

 _FOAM  is building spatial applications and proof of location that bring
geospatial data to blockchains and empower a consensus driven map of the
world._

  * Working on a fork of the Forth State Plasma MVP Side chain with Tendermint Consensus as well as collaborating on open issues [here](https://github.com/FourthState/plasma-mvp-sidechain "https://github.com/FourthState/plasma-mvp-sidechain"). 

  * Given that the FOAM Token has "Proof of Use" restrictions on those that participated in the Token Sale, this has lead to some technical issues when it comes to 0x DEX integrations. To resolve, the 0x protocol will need to additionally check for token transfer permissions before allowing an order to be placed, we have been coordinating on this and the Pull Request "Simulate Maker transfer in order validation" is [here](https://github.com/0xProject/0x-monorepo/pull/1714 "https://github.com/0xProject/0x-monorepo/pull/1714"). 

  * Hosted a Community Call on the theme of building decentralized infrastructure featuring the Althea Mesh project, video [here](https://www.youtube.com/watch?v=ADocEA4oD7s&t=260s "https://www.youtube.com/watch?v=ADocEA4oD7s&t=260s"). 

 **David from Sia**

 _Sia is a decentralized cloud storage platform leveraging blockchain
technology to create a data storage marketplace that is more robust and more
affordable than traditional cloud storage providers._

  * The release candidates have been successful and identified several tough bugs that the Sia development team is continuing to work through. The team regrets delaying the release but is confident that releasing stable software is worth the wait. Many of the code commits this week were in support of debugging, verifying, and improving the quality of code in the product.

  * Matthew Sevey from the Sia development team had this to say “the two main fixes/features we focused on this week were improvements to the host to enable the renter to scale past 6TB and improved handling of siapaths to reduce errors with different [operating systems], specifically windows. So the testing we are doing is to gain confidence that we sufficiently addressed those two issues.”

  * The team expects to publish 1.4.0 RC4 to the Sia development community for testing this upcoming week

  * Improved API documentation with new CURL examples <https://gitlab.com/NebulousLabs/Sia/merge_requests/3524> and <https://gitlab.com/NebulousLabs/Sia/merge_requests/3535>

  * Tweak Timeouts and limits <https://gitlab.com/NebulousLabs/Sia/merge_requests/3540> and <https://gitlab.com/NebulousLabs/Sia/merge_requests/3541>

  * Various scaling improvements.

  * Siacoin will be listed on ICE Data Services <https://www.reddit.com/r/siacoin/comments/b2vdvh/siacoin_listed_on_ice_data_services/>

  * Community contributors and Sia Advent of Code participants are eligible to receive a free Sia shirt. <https://www.reddit.com/r/siacoin/comments/b3k6li/sia_draco_shirt_arrived_today/>

#### Other

 **Ari from Decentraland**

 _Decentraland is a virtual world where you can build and explore 3D
creations, play games and socialize._

  * On March 18th, we launched the drag-and-drop scene [Builder](https://builder.decentraland.org/) and started the [Creator Contest](https://contest.decentraland.org/), rewarding creative scenes with MANA and LAND.

  * Since the Builder’s launch, we’ve been running continual QA testing, making iterative UI improvements, and fixing bugs.

  * In the [SDK](https://docs.decentraland.org/), we’ve added a new component making texture support more robust and optimized. A bug in GLTF model rotation has also been fixed so model rotation matches the standards of other platforms - making it easier to import content.

  * Finally, we’ve started to set up up performance tests in the Decentraland Client.

 **Bowen from Hydro/DDEX.io**

 _Hydro  Protocol is an open source framework for building Decentralized
Exchanges. DDEX is the first decentralized exchange for Ethereum and ERC-20
tokens built on the Hydro Protocol. _

  * Hydro Scan live  \- Visualize # of  Traders, Trading Volume - <https://hydroscan.io/>

  * Hydro Starter Kit  \- Finish documentation - Public BETA 4/2 

  * Hydro Protocol v1.1 - Smart Contract Upgrade on 3/27 12:00 AM Beijing time, update maker rebate logic, Goal : To be more market maker friendly 

 **Sam from OpenBazaar**

 _OpenBazaar is an open source project developing a protocol for e-commerce
transactions in a fully decentralized marketplace._

  * A new OpenBazaar release was published, [2.3.1](https://github.com/OpenBazaar/openbazaar-desktop/releases/tag/v2.3.1), a minor release which primarily includes a rebase to the latest IPFS code. It also includes multiple bug fixes and the ability to update which coins vendors accept on listings in bulk.

  * Work on 2.3.2 has begun, with a focus on improved message protocol routing and a sweep wallet feature.

  * Work has begun on a simple UI for claiming rewards from usage of the token.

 **Martín from Zeppelin**

 _Zeppelin builds tools for the secure development, deployment and operation
of decentralized systems. Zeppelin also helps companies secure their systems
by performing security audits._

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

