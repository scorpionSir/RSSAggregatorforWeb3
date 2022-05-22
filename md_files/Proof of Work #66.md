[![](https://substackcdn.com/image/fetch/w_96,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F37b09348-f4f1-47a2-b9e0-a2007299e6e4_256x256)](https://proofofwork.news)

# [Proof of Work](https://proofofwork.news)

SubscribeSign in

Share this post

Proof of Work #66

proofofwork.news

Copy link

Twitter

Facebook

Email

# Proof of Work #66

[Eric Meltzer](https://substack.com/profile/138320-eric-meltzer)

May 17, 2019

[Share](javascript:void\(0\))

"The Street finds its own uses for things"

—William Gibson

Sometimes it takes a while, though. Most of the world still doesn’t own any
crypto, or even really understand what it is. An interesting thing about
Bitcoin is that unlike other technologies (VR, e.g.) where someone who was
directionally correct (VR in some form will almost certainly be incredible)
but had the timing wrong gets completely wrecked, with Bitcoin early adopters
are rewarded, and as adoption continues, the price continues to climb. Even if
massive adoption doesn’t happen as fast as people want it to, a patient HODLer
is likely to be rewarded, especially if BTC continues to adopt provably good
new tech (like e.g. Schnorr).

I’ve noticed this kind of slow, creeping adoption a lot more over the past few
months. More and more people know what Bitcoin is, or have a rough idea. A
much smaller percentage of them maybe bought some on Coinbase or Cash.app.
Today I went to a [really cool event at
MIT](https://www.csail.mit.edu/event/lcs35-time-capsule-event) where a time
capsule was unveiled 15 years early—the story being that Ron Rivest (the R in
RSA) designed a tricky puzzle that involved an intrinsically sequential
computation (in order to resist efforts at leveraging massively parallel
computation) that was intended to take around 35 years to solve based on
Moore’s Law estimations. Two teams managed to solve it faster (one slightly
after the other, one with pure software and commodity hardware, one with an
FPGA) and the winning guy immediately stamped his proof of solution on the
Bitcoin Cash blockchain in an OP_RETURN, and then again on the BTC blockchain
(this time in an actual block header, _swag_ , with the help of a big mining
pool).

No one seemed to bat an eye at this. Of course you stamp things on the Bitcoin
blockchain when you want to have a time-based proof that something happened.
As one does! This type of thing seems to fall in line with the idea that
Bitcoin blockspace will remain a valuable commodity even in the post-coinbase
reward era.

Sorry for the lateness of today’s newsletter—post-Consensus stuff pushed it
back a few days. Congrats to the teams that sent updates in!

#### Bitcoin & Friends

 **Jimmy on Bitcoin**

 **[Optech](https://bitcoinops.org/en/newsletters/) on Bitcoin [ed: sign up
for their newsletter too! it’s great!]**

  * Taproot proposal soft fork discussion: several replies were posted to the Bitcoin-Dev mailing list in response to [bip-taproot](https://github.com/sipa/bips/blob/bip-schnorr/bip-taproot.mediawiki) and [bip-tapscript](https://github.com/sipa/bips/blob/bip-schnorr/bip-tapscript.mediawiki).

  * Addition of derivation paths to BIP174 PSBTs: Stepan Snigirev [posted](https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2019-April/016894.html) a suggestion to the Bitcoin-Dev mailing list to allow PSBTs to include the BIP32 derivation path for the public keys used to generate the change output’s address.

 **Aviv from Spacemesh**

 _Spacemesh is a programmable cryptocurrency powered by a novel proof-of-
space-time consensus protocol._

  * [Mining flow automation tests](https://github.com/spacemeshos/go-spacemesh/pull/875)

  * [Added automation tests for sync](https://github.com/spacemeshos/go-spacemesh/pull/867)

  * [Sync automation sanity](https://github.com/spacemeshos/go-spacemesh/pull/886)

  * [Updated PoET and PoST to more efficient merkle tree](https://github.com/spacemeshos/go-spacemesh/pull/881)

  * [Network screen - initial commit](https://github.com/spacemeshos/smapp/pull/93)

  * [Merged PRs](https://github.com/spacemeshos/go-spacemesh/pulls?q=is%3Apr+is%3Aclosed+review%3Aapproved)

  * Full update at [https://spacemesh.io](https://spacemesh.io/)

 **JZ from Decred**

 _Decred  is an autonomous digital currency with a hybrid consensus system. It
is built to be a self-ruling currency where everyone can vote on the rules and
project-level decision making proportionately to their stake._

  * Lightning Network transactions are now supported on Decred mainnet. Our hard fork went off as planned on May 9th and since then a transaction making use of the new rules has been executed, meaning anyone who has not upgraded to v1.4 is now forked off the network.

  * The [Politeia proposal to decentralize the treasury](https://proposals.decred.org/proposals/c96290a2478d0a1916284438ea2c59a1215fe768a87648d04d45f6b7ecb82c3f) funds has also passed with 97.48% support, authorizing the team to implement Marco's design and vest the final bit of sovereignty with the stakeholders.

  * [April's edition of the Decred Journal](https://decredcommunity.org/blog/decred-journal-april-2019) has landed, covering all project activities including the 292 active PRs and 477 commits with 96k additions and 50k deletions spread across over two dozen contributors last month.

 **Izaak from Coda**

 _Coda is the first cryptocurrency protocol with a constant-sized blockchain.
Coda compresses the entire blockchain into a tiny snapshot the size of a few
tweets using recursive zk-SNARKs._

  * We’ve announced the SNARK challenge (<https://codaprotocol.com/blog/snark-challenge.html>) in partnership with Dekrypt and Coinlist and with support from a number of other awesome crypto projects. 

#### Privacy coins

 **Paige & Zooko from Zcash**

 _Zcash is a  digital currency utilizing zk-SNARKs to enable its privacy-
protecting properties._

  * Significant effort put towards final review, testing and documenting this week's 2.0.5 release. Several bugs were discovered so we're taking the time to properly address. 

  * Ref wallet stability improvements + researching iOS

  * A few of us will be at Consensus Construct

  * Full update: <https://forum.zcashcommunity.com/t/may-10-2019-weekly-update-engineering/33439>

 **Daniel from Grin**

 _Grin is a community-driven implementation of the Mimblewimble protocol that
aims to be privacy preserving, scalable, fair, and minimal._

  * Merged PRs: [4 in /grin](https://github.com/mimblewimble/grin/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A2019-05-06..2019-05-12+) | [4 in /grin-wallet](https://github.com/mimblewimble/grin-wallet/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A2019-05-06..2019-05-12+) | 3 unique contributors

  * Thanks to the person or entity [donating the 50 BTC coinbase reward from 2010](https://blockchair.com/bitcoin/transaction/491ee02543c25d729616de43685d837aa8461b453fd63da8eed88487db4176b7). If you're reading this, we're humbled by the vote of confidence and will do our utmost to spend it wisely.

  * @yeastplume open sourced his [Samir's Secret Sharing skunkworks project](https://github.com/yeastplume/rust-sssmc39), an entry point into further research for adding multi-sig support into the official grin wallet.

  * [v1.1.0-beta2 was released](https://github.com/mimblewimble/grin-wallet/releases/tag/v1.1.0-beta.2), now with Azure Pipelines CI courtesy of @quentinlesceller.

  * [Invoice transactions support](https://github.com/mimblewimble/grin-wallet/pull/96) now merged by @yeastplume.

  * Draft proposal for a [2019 Grin budget](https://github.com/mimblewimble/grin-pm/issues/130).

  * The [last governance meeting](https://github.com/mimblewimble/grin-pm/blob/master/notes/20190507-meeting-governance.md) discussed funding and financial transparency report, and a simplified onboarding flow.

  * [Slides from @lehnberg's talk about Atomic Swaps in Grin](https://713.mw/slides_20190509_grinswap_berlin) at last week's Binance Labs meetup in Berlin.

  * Vite wallet [added transaction status](https://www.grin-forum.org/t/we-plan-to-add-the-transaction-status-tracking-function-on-the-next-version-of-grin-mobile-wallet/4979) support.

  * More Grin info [here](https://grinnews.substack.com/).

 **Arnaud from AZTEC Protocol**

 _AZTEC Protocol is an efficient zero-knowledge protocol built on top of
Ethereum, making plug-and-play value transmission and asset governance privacy
tools for developers and companies.  _

  * This week we fixed [a bug with confidentialTransferFrom](https://github.com/AztecProtocol/AZTEC/pull/125), which made it impossible for contracts to spend notes.

  * Our work on the trusted setup MPC is progressing well, we will be running a full mock MPC at the end of this month.

  * We have been continuing our house keeping, by [refactoring our tests](https://github.com/AztecProtocol/AZTEC/pull/141) to use a local trusted setup database instead of a hosted one, and [simplifying proof construction.](https://github.com/AztecProtocol/AZTEC/blob/refactor-aztec.js/packages/aztec.js/src/proof-v2/proof.js)

  * In addition to the two cryptographer roles, we are now hiring for a **Senior Solidity Engineer** and a **Senior Engineer**. You can apply [here](http://email.mg2.substack.com/c/eJwlUEuOwyAMPU3ZNSKQpGHBoq1mrhHxcVumBEfgTJU5_RBF8sKy_fw-zhA8MW96wUJsLZCn4LVQgg8t87rz7diPLJTpkQFmE6KmvAJbVhuDMxQw7fe9kuylwUnVg3RcXQYu7eDAenvpjOx5Lweh2M4xmdUHSA40_ELeMAGL-kW0lJO8nsR3LZOeEBuHe_tH4M5LRkKH8Szr6AdtYUEL3iouRcs7LjvRtM2NX-_jnY-3QbS37ut66vj8FE1ZbSHj3vXfzLI2OVUBdecy-EBzSNQEPJTRtoBO8CkRiCAzOkKpXqcKntcUaJsgGRvB6wNSvUt1kQOrNB5rPklXsfjAxwfz-x-f0nXk), or by emailing [arnaud@aztecprotocol.com](mailto:arnaud@aztecprotocol.com) with the name of the role as the subject.

#### Smart contracting platforms

 **Evan from[Ethereum](https://weekinethereumnews.com/)**

 _Ethereum  is a decentralized platform for applications that aims to resist
fraud, censorship or third-party interference._

  * [Prysmatic releases its Eth2 testnet](https://medium.com/prysmatic-labs/ethereum-2-0-phase-0-testnet-release-1e9e682db910)

  * [Finality in Eth2](https://medium.com/@ralexstokes/how-secure-is-ethereum-2-0-consensus-41523a59f270). Put differently: why Eth2 will be much more final and secure than Eth1 or BTC – as this week’s aborted attempt by Binance to re-org BTC showed

  * A [Scratch3 extension](https://github.com/naddison36/eth-scratch3#eth-scratch3) to make it easy and kid-friendly to build games on Eth

 **AJ from Tezos**

 _Tezos is a self-amending blockchain that features formally verified smart
contracts, on-chain governance, and a proof-of-stake consensus algorithm which
enables all token holders to participate in the network.  _

  * [Tezos Foundation announces initiatives to increase network participation](https://tezos.foundation/news/initiatives-to-increase-participation-in-the-tezos-ecosystem), currently an outstanding 81% of the network is baking. 

  * [Tarides publishes it’s path to Irmin V2](https://tarides.com/blog/2019-05-13-on-the-road-to-irmin-v2.html) which will optimize Tezos persistent storage. In other words, dramatically increase Tezos storage without needing to change the protocol. 

  * [Introducing TezBlock](https://medium.com/airgap-it/tezblock-a-tezos-block-explorer-concept-a6fce860ae8e), a Tezos Block Explorer concept

  * S[pin up a Tezos Node in a few minutes with snapshotting](https://medium.com/tezos/https-medium-com-tezos-spinning-up-a-tezos-node-in-under-a-few-minutes-3b3328e173f3)

  * Tezos Korea will launch a Tezos focused blockchain course at Samsung Multicampus

 **Topper from Quorum Control**

 _Quorum Control makes Tupelo, a permissionless proof of stake DLT platform
purpose-built to model individual objects that enables flexible public or
private data models._

  * Ongoing Optimization of Production Tupelo TestNet

    * Testnet v0.2.1 with nodes having improved ability to restart and rejoin signing

    * Cross-repo integration tests extended in CI

    * Enhancements to the reliability of performance benchmarking

  * RPC improvements (GetTokenBalance / SignatureValidation on Import)

  * In progress on listening service to trigger events on state changes

 **Michael from Loom**

 _Loom Network is a platform for building highly scalable DPoS sidechains to
Ethereum, with a focus on large-scale games and social apps._

  * Released Trezor support for PlasmaChain staking, so users can delegate directly from their hardware wallets

  * Completed the Loom SDK Q1 2019 Security Audit by Trail of Bits

  * New developer tutorial on [how to create a fast, gasless ERC20 payment system](https://www.youtube.com/watch?v=c04C95OEi-o) on PlasmaChain

 **Kate and Dean from Agoric**

 _Founded by pioneers in secure development and distributed systems, Agoric
uses a secure subset of JavaScript to enable object capabilities and smart
contracts._

  * We’re very pleased to announce that we’ve[ secured $4 million in new funding](https://www.coindesk.com/ripples-xpring-outlier-ventures-back-4-million-raise-for-agoric) from Ripple’s Xpring, gumi Cryptos Capital, Kilowatt Capital, MetaStable Capital, Outlier Ventures, Lemniscap, Rockaway Blockchain and the Interchain Foundation, as well as additional funding from the Electric Coin Company (sometimes referred to as the Zcash Company, the for-profit institution behind the privacy-focused cryptocurrency zcash), Naval Ravikant and Polychain. 

  * Dean gave [an impassioned speech on smart contracts](https://www.freightwaves.com/news/smart-contracts-bringing-the-world-economy-online) at the Blockchain in Transport Alliance (BiTA) Spring Symposium. Dean explained that the ultimate vision for smart contracts is to bring the entire economy of the world online. “The diverse, vibrant world economy”, he said, “needs high integrity computation, a security model that works for software components, broad scope and interoperability with other chains.”

#### Financial Infrastructure

 **Antonio from dYdX**

 _dYdX is a decentralized exchange for margin trading, borrowing, lending, and
eventually derivatives. dYdX allows traders to trustlessly short and get
leverage on crypto assets._

  * USDC is now available to borrow and lend on [dYdX](https://dydx.exchange/)!

  * dYdX did over $2.4M of 24H trading volume over the weekend

  * Working on adding trade history to the product

  * Kicking off a design sprint to improve parts of our UI

  * Work trialed an engineering candidate

  * [Hiring](https://dydx.exchange/careers/) engineers & product designers full-time in SF!

 **Brendan from Dharma**

 _Dharma is the easiest place to borrow and lend cryptocurrencies. It enables
non-custodial peer-to-peer lending through smart contracts on Ethereum._

  * We're looking for 20 volunteers to help us test a [new feature](https://blog.dharma.io/introducing-instant-matching-9c54ca0d2a66) on Dharma. Reach out to [brendan@dharma.io](mailto:brendan@dharma.io) if interested

  * We've continued our strong growth in May, with over 1m USD borrowed this month to date

  * Planning a new round of smart contract audits for June, that will audit new functionality we've released since the audits last year

 **Coulter from MakerDAO**

 _Maker is comprised of a decentralized stablecoin, collateral loans, and
community governance._

  * Maker CEO Rune Christensen [penned a blog](https://blog.makerdao.com/the-stability-fee-is-too-damn-high/) on common misconceptions around the Stability Fee. Worth a read if you've ever thought "The Stability Fee is too high!" 

  * A guide to Multi-Collateral Dai titled "[MCD 101](https://github.com/makerdao/developerguides/blob/master/mcd/mcd-101/mcd-101.md)" was put together by Kenton Prescott, helping give an overview of the smart contracts in the Dai Credit System. 

  * Whisp joined our [weekly community call](https://www.youtube.com/watch?v=dSOB1JWAShU&feature=youtu.be) (which is public for anyone to tune in to!) in order to showcase their v1 of their product which is a payroll platform for remote workers. 

  * We partnered with Airtm to add Dai into their platform, helping bring financial stability to individuals in regions suffering from hyperinflation. Maker is also contributing 10,000 Dai to their AirDrop Venezuela campaign! [Read more](https://blog.makerdao.com/makerdao-and-airtm-partner-to-empower-financial-stability-in-south-america/).

 **Lazar from MARKET Protocol**

 _MARKET Protocol is a framework for creating tokens that track prices of
traditional or digital assets._

  * Continued progress with our security audit prior to mainnet release of MARKET Protocol

  * Built out framework for MPX notifications, including user actions to orders, rewards, and on-chain transactions

  * Refined notifications and alerts that our development team receives from our production systems

#### Layer two and interoperability

 **Rahul from 0x**

 _0x_  is an open protocol that enables the peer-to-peer exchange of assets on
the Ethereum blockchain.

  * 0x will be at ETH New York - we will be sponsoring a few prizes at the [hackathon](https://blog.0xproject.com/0x-at-ethnewyork-43e0bbd78422), including a joint prize with Wyre

  * We are looking for some SF based devs to participate in a [focus group](https://docs.google.com/forms/d/e/1FAIpQLSfg2sJMjwZPfU6Qra0VtxmmIwxRkW96xAnaknwSrWwHt6WF0w/viewform) about our documentation 

  * New [ZEIP around property based orders](https://github.com/0xProject/ZEIPs/issues/43#issuecomment-490545982), enabling the trading of NFTs around properties as opposed to the exact ID number 

 **Tony from Liquidity.Network**

 _Liquidity Network is a transfer and swap platform for any token_

  * Fixing server bugs

  * Testing server performance

 **Dong Mo from Celer**

 _Celer Network is a layer-2 scaling platform that enables fast, easy and
secure off-chain transactions for not only payment transactions, but also
generalized off-chain smart contracts._

  * We finished new Gomoku off-chain payment flow and off-chain state exchange and co-signing. 

  * We've refined CelerX JS APIs and finished dispute implementation spec.

  * We completed the setup of a Mainnet backend stack and the on-chain play SDK API. 

  * We opensourced [Celer dApp Contract](https://github.com/celer-network/cApps-eth) with template developer code and example applications.

 **Alexandra from Parity Technologies**

 _Parity  Technologies builds core blockchain infrastructure, from Parity
Ethereum, an Ethereum client, to Polkadot, an interoperable blockchain
network._

  * [Recordings from Sub0](https://www.youtube.com/watch?v=eJlWTGa1z0o&list=PLp0_ueXY_enWqrfP_vR4PLhzQj76fLT8y), the first Substrate developer conference, are out. This includes the [AMA with Gavin Wood](https://youtu.be/05H4YsyPA-U) as well as his presentation on [Substrate Module Overview and Future Directions](https://youtu.be/kpUO8g_Ig0A).

  * New tutorial on [Ink, an eDSL to write WebAssembly-based smart contracts](https://twitter.com/ParityTech/status/1125352553900838912).

  * New [intro to Rust for Substrate developers](https://twitter.com/ParityTech/status/1126528963088650246). 

  * New one-liners for [deploying a local Polkadot or Substrate network.](https://twitter.com/chevdor/status/1126524464852865025) 

  * We're at [NYC Blockchain Week](https://twitter.com/ParityTech/status/1125771556192509952). 

  * Web3 Foundation is [providing grants to build the Web3 ecosystem](https://github.com/w3f/Web3-collaboration/blob/master/grants/grants.md).

  * [New positions added to our jobs page](https://twitter.com/ParityTech/status/1125721291456172032), including Assistant to the CEO and Operations Manager. 

#### Application infrastructure

 **David from Sia**

 _Sia is a decentralized cloud storage platform leveraging blockchain
technology to create a data storage marketplace that is more robust and more
affordable than traditional cloud storage providers._

  * The development team spent this week improving the scalability, speed, and reliability of renters with large amounts of files. Ongoing scalability tests are ongoing, with a live renter already at 10 TB and growing.

  * The new global ratelimits feature will allow a renter to set bandwidth limits for Sia.

  * Chris’ final MR for renaming a directory was merged.

  * Matt better categorized InactiveContracts into Renewed and Disabled, to give a more granular view of your uploaded data and money spent.

  * Chris has been working hard on the “partial-uploads” branch which will allow for upload streaming.

  * The April 2019 Community update was posted: <https://blog.sia.tech/sia-community-update-april-2019-f683812b4245>

  * Siacoin was added to SouthXchange <https://twitter.com/southxchange/status/1124000655289589760>

  * Swing by our Discord to keep up with all the latest: <https://discord.gg/sia>

#### Other

 **Ari from Decentraland**

 _Decentraland is a virtual world where you can build and explore 3D
creations, play games and socialize._

  * Last week, [we released Picture Frames for the Builder](https://decentraland.org/blog/announcements/picture-frames-dapper), allowing users to add 2D representations of CryptoKitty NFTs to their scenes. We plan to add support for additional NFTs in future releases.

  * [Released the “Pirate Paradise” item pack for the Builder.](https://twitter.com/decentraland/status/1124029878490345473)

  * Redesigned the Builder’s item catalogue to support multiple item packs.

  * We’ve been conducting QA testing, and fixing bugs, in Decentraland’s Unity Client.

 **Sam from OpenBazaar**

 _OpenBazaar is an open source project developing a protocol for e-commerce
transactions in a fully decentralized marketplace._

  * The OB1 team was on a work retreat in Portland last week. We're working on the final push to get the Haven app into open beta testing, and also working on Ethereum integration on the OpenBazaar client side.

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

