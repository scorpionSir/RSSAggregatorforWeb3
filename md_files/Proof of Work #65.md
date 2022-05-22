[![](https://substackcdn.com/image/fetch/w_96,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F37b09348-f4f1-47a2-b9e0-a2007299e6e4_256x256)](https://proofofwork.news)

# [Proof of Work](https://proofofwork.news)

SubscribeSign in

Share this post

Proof of Work #65

proofofwork.news

Copy link

Twitter

Facebook

Email

# Proof of Work #65

[Eric Meltzer](https://substack.com/profile/138320-eric-meltzer)

May 8, 2019

[Share](javascript:void\(0\))

Hi from sunny Boston!

Binance suffered a hack yesterday, the specifics of which remain unclear. Some
combination of multiple techniques allowed the hacker(s) to send themselves a
single giant transaction of >7000 BTC to an address under their control, from
the Binance hot wallet. Binance announced that this would be 100% covered from
their insurance fund, and that no user funds would be affected.

Jeremy Rubin, a BTC core dev and friend-of-the-newsletter had the following
suggestion

[![Twitter avatar for
@JeremyRubin](https://substackcdn.com/image/twitter_name/w_36/JeremyRubin.jpg)Jeremy
Rubin @JeremyRubin@cz_binance if you reveal your private keys for the hacked
coins (or a subset of them) you can decentralized-ly at zero cost to you,
coordinate a reorg to undo the
theft.](https://twitter.com/JeremyRubin/status/1125919526485254144)

[May 8th 2019

80 Retweets321
Likes](https://twitter.com/JeremyRubin/status/1125919526485254144)

You can replace “reveal the private keys” (which would allow miners to make
their own transactions spending the hacker’s coins to miner addresses) with
“create a double-spend of the hack transaction back to a Binance-controlled
wallet, and add a massive fee—700 BTC? 7000 BTC?—to incent miners to reorg the
chain to reflect the Binance transaction rather than the hacker’s
transaction.”

This suggestion was made when roughly 50 blocks had elapsed, so what Jeremy
was suggesting would require a massive amount of hashpower to pull off. It’s
also not a new suggestion (the wonderful Bitmex Research pointed to [this
thread](https://www.reddit.com/r/Bitcoin/comments/4vupa6/p2shinfo_shows_movement_out_of_multisig_wallets/d61qyaj/))
and so far it’s never actually been tried. In general, sentiment in the
community was so massively against this move that it probably would have
caused a chainsplit, and therefore been untenable.

However, would it be advisable for an exchange who has just been hacked and
realizes it VERY rapidly to try this after only 2-3 blocks have elapsed? The
bitcoin chain is reorg-ed by a few blocks occasionally in the course of normal
mining, which is part of how the “wait 6 confirmations” rule came about. If
the exchange noticed the hack within 2 blocks, or even before it made it out
of the mempool, and immediately submitted a competing transaction with a much
higher fee, I don’t think most of the community would have any problem with
it. However, if exchanges started doing this frequently, they would perhaps be
incentivizing _miners_ to hack them, since the miners know that the exchange
will attempt to “burn” the hacked funds into fees…

Anyway, this story has an uneventful and perhaps happy ending:

[![Twitter avatar for
@cz_binance](https://substackcdn.com/image/twitter_name/w_36/cz_binance.jpg)CZ
Binance @cz_binanceAfter speaking with various parties, including
@JeremyRubin, @_prestwich, @bcmakes, @hasufl, @JihanWu and others, we decided
NOT to pursue the re-org approach. Considerations
being:](https://twitter.com/cz_binance/status/1125996194734399488)

[May 8th 2019

480 Retweets2,126
Likes](https://twitter.com/cz_binance/status/1125996194734399488)

[![Twitter avatar for
@cz_binance](https://substackcdn.com/image/twitter_name/w_36/cz_binance.jpg)CZ
Binance @cz_binancecons: 1 we may damage credibility of BTC, 2 we may cause a
split in both the bitcoin network and community. Both of these damages seems
to out-weight $40m revenge. 3 the hackers did demonstrate certain weak points
in our design and user confusion, that was not obvious
before.](https://twitter.com/cz_binance/status/1125996197343154176)

[May 8th 2019

128 Retweets1,245
Likes](https://twitter.com/cz_binance/status/1125996197343154176)

So for now, this has been a koan-like lesson on the nature of Nakamoto
consensus and its lack of transaction finality, but we didn’t get to see how
Bitcoin would behave in a particularly extreme scenario.

More next week, as always thanks for reading!

#### Bitcoin & Friends

 **[Optech](https://bitcoinops.org/en/newsletters/) on Bitcoin**

  * [Bitcoin Core 0.18.0 released](https://bitcoincore.org/en/releases/0.18.0/)

  *  **Proposal for support of Schnorr signatures and Taproot script commitments:**  Pieter Wuille [posted](https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2019-May/016914.html) to the Bitcoin-Dev mailing list a proposed [BIP for Taproot](https://github.com/sipa/bips/blob/bip-schnorr/bip-taproot.mediawiki) (using Schnorr signatures) and a proposed [BIP for Tapscript](https://github.com/sipa/bips/blob/bip-schnorr/bip-tapscript.mediawiki), a small variation on Bitcoin’s current Script language to be used with Taproot encumbrances. 

**James from Summa**

 _Summa builds tools to exchange crypto in a convenient and trustless
fashion._

  * We added a basic infura websocket client to [riemann-ether](https://github.com/summa-tx/riemann-ether)

  * [bitcoin-spv](https://github.com/summa-tx/bitcoin-spv) now has tools for calculating Bitcoin sighashes on-chain and verifying Bitcoin signatures, plus a better readme :)

 **Tony from Kadena**

 _Kadena is building Pact, a formally verifiable smart-contracting language
for financial applications, and Chainweb, a PoW blockchain that uses multiple
chains in parallel to increase throughput._

  * Monica Quaintance presented Kadena’s hybrid blockchain and its enterprise applications at  _MIT Technology Review_ ’s [Business of Blockchain](mailto:https://events.technologyreview.com/video/watch/monica-quaintance-permissioned-blockchains) conference.    

  * Looking ahead in May, Kadena's Will Martino, Stuart Popejoy, and Monica Quaintance are speaking at Consensus and then we're aiming to release testnet v1 at the end of the month.

  * The Kadena team would enjoy meeting up with folks during New York Blockchain Week. Read about the events we're participating in on our [Medium post](https://medium.com/kadena-io/kadena-at-consensus-2019-7786d7655423).

  * Eliminated network/chain malleability attacks in application layer [PR 153](https://github.com/kadena-io/chainweb-node/pull/153).

  * Implemented "Adaptive" Difficulty Adjustment for improved early network conditions [PR 167](https://github.com/kadena-io/chainweb-node/pull/167).

  * Mining hashrate target calculation performance improvement [PR 115](https://github.com/kadena-io/chainweb-node/pull/115).

  * Better legibility of compiler errors in Pact SDK PR [467](https://github.com/kadena-io/pact/pull/467).

  * Monica Quaintance and Tarun Chitra of Gauntlet Networks published a security paper, [covered by Forbes](https://www.forbes.com/sites/darrynpollock/2019/04/29/high-frequency-trading-researcher-publishes-findings-on-jpmorgan-blockchain-spin-off/#5136fb552915), that proves Chainweb as the first scalable Proof of Work blockchain.

  * Emily Pillmore and Stuart Popejoy were interviewed on [Hashing It Out](https://thebitcoinpodcast.com/hashing-it-out-43) to discuss Pact, the smart contract language with built-in Formal Verification used in Kadena's Chainweb.

  * The Next Web published Stuart Popejoy's analysis of [how IBM's Hyperledger is not a real blockchain](https://thenextweb.com/podium/2019/05/05/ibms-hyperledger-isnt-a-real-blockchain-heres-why).

 **Aviv from Spacemesh**

 _Spacemesh is a programmable cryptocurrency powered by a novel proof-of-
space-time consensus protocol._

  *  **ED25519 Public Key Extraction Go Library**

    * <https://github.com/spacemeshos/ed25519>

    * An open-source drop-in replacement to [golang/crypto/ed25519](https://godoc.org/golang.org/x/crypto/ed25519) with additional functionality.

    * We have developed this for the Spacemesh protocol since we could not find a good open source alternative. We hope that the open source blockchain dev community will find these capabilities useful in other scenarios and platforms. 

    * In the ed25519 signature scheme, in order to verify the validity of a given signature, the validator should posses the public key of the signer. It can be sent along with the message and its signature, which means that the overall data being sent includes 256 bits of the public key. 

    * Full update => <https://spacemesh.io/weekly-updates/> 

 **JZ from Decred**

 _Decred  is an autonomous digital currency with a hybrid consensus system. It
is built to be a self-ruling currency where everyone can vote on the rules and
project-level decision making proportionately to their stake._

  * Richard's proposal to [amend the Decred constitution](https://proposals.decred.org/proposals/fd56bb79e0383f40fc2d92f4473634c59f1aa0abda7aabe29079216202c83114) passed easily with 98.81% support and 12k tickets voting.

  * Marco has flipped the switch and started a vote to authorize the work necessary to [decentralize the Decred treasury](https://proposals.decred.org/proposals/c96290a2478d0a1916284438ea2c59a1215fe768a87648d04d45f6b7ecb82c3f).

  * [Jake did an AMA on r/CryptoCurrency](https://www.reddit.com/r/CryptoCurrency/comments/bjubwv/ama_decred_project_lead_jake_yocompiatt/) that received tons of great questions about the future of the project.

  * A final warning to those who haven't upgraded. A hard fork will take place on Thursday, May 9th and you must be on [version 1.4 of Decrediton or the CLI tools](https://www.decred.org/downloads/) in order to not be forked off the network. If you're using a third party wallet you likely don't need to do anything.

 **Johnny from Stellar**

 _Stellar is an open network for sending and exchanging value of any kind. Its
global network enables digitization of assets - from carbon credits to
currencies - and enables movement around the internet with ease._

  * Stellar v11.1.0 is scheduled to be released at the end of the month.

  * Horizon v0.17.6 released this week with minor fixes

  * [New Go SDK released](https://www.stellar.org/developers/go/reference/index.html), announcement & [v1.1 is out](https://github.com/stellar/go/releases/tag/horizonclient-v1.1.0).

 **Izaak from Coda**

 _Coda is the first cryptocurrency protocol with a constant-sized blockchain.
Coda compresses the entire blockchain into a tiny snapshot the size of a few
tweets using recursive zk-SNARKs._

  * Jiawei has [started implementing](https://github.com/CodaProtocol/coda/pull/2356) the stake-voting augmentation to our consensus mechanism. Read the [RFC here](https://github.com/CodaProtocol/coda/pull/2227) to learn more about how this makes Coda resilient against long-lasting network partitions.

  * Avery and John have been working on the [GraphQL ](https://github.com/CodaProtocol/coda/pull/2330)[API](https://github.com/CodaProtocol/coda/pull/2342).

  * Echo fixed a [race condition](https://github.com/CodaProtocol/coda/pull/2352) in the transaction pool.

  * Paul worked on implementing the[trust system](https://github.com/CodaProtocol/coda/pull/2354).

#### Privacy coins

 **Paige & Zooko from Zcash**

 _Zcash is a  digital currency utilizing zk-SNARKs to enable its privacy-
protecting properties._

  * [ZIP and NUP Process Updates to Enhance Community Engagement](https://forum.zcashcommunity.com/t/zip-and-nup-process-updates-to-enhance-community-engagement/33330)

  * [Following along with ZIP editors](https://forum.zcashcommunity.com/t/following-along-with-zip-editors/33346)

  * Zcashd 2.0.5 is planned for release next week  

  * [Reference Wallet Team Twitter Q&A thread](https://twitter.com/hashtag/ZcashRefWalletQA?src=hash&lang=en)

  * Full update: <https://forum.zcashcommunity.com/t/may-03-2019-weekly-update-community-comms/33368>  

 **Mitchell from Monero**

 _Monero is a open-source, privacy-focused cryptocurrency using the ASIC-
resistant CryptoNote PoW algorithm. It enforces all privacy features at the
protocol level to ensure that all transactions create a single fungible
anonymity pool._

  * Looking into the [Lelantus transaction construction](https://eprint.iacr.org/2019/373), put together a method and some example code showing how to form a [Lelantus commitment for Monero](https://github.com/SarangNoether/skunkworks/blob/lelantus/lelantus/migration.md "https://github.com/SarangNoether/skunkworks/blob/lelantus/lelantus/migration.md").

  * GUI will soon have an update pop-up to [alert users when they should upgrade](https://github.com/monero-project/monero-gui/pull/2100 "https://github.com/monero-project/monero-gui/pull/2100"), including a link and checksum

  * [Revamping the send page](https://github.com/monero-project/monero-gui/issues/2148. "https://github.com/monero-project/monero-gui/issues/2148.") for better UX flow.

  * High [transaction volume](https://bitinfocharts.com/comparison/monero-transactions.html "https://bitinfocharts.com/comparison/monero-transactions.html") last week, more than 10k/day. Many have speculated increased traffic may be related to the new [Minko](https://bitinfocharts.com/comparison/monero-transactions.html "https://bitinfocharts.com/comparison/monero-transactions.html")game, however this is not publicly confirmed (as far as I know).  

 **Daniel from Grin**

 _Grin is a community-driven implementation of the Mimblewimble protocol that
aims to be privacy preserving, scalable, fair, and minimal._

  * Merged PRs: [11 in /grin](https://github.com/mimblewimble/grin/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A2019-04-29..2019-05-05+) | [1 in /grin-wallet](https://github.com/mimblewimble/grin-wallet/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A2019-04-29..2019-05-05+) | 5 unique contributors

  * The UTXO set [keeps shrinking](https://grin.report/d/xoo9N43iz/chain?orgId=1&fullscreen&panelId=2&from=1554073200000&to=1557147331887). It has been reduced by ~35% over the past 10 days.

  * The [last dev meeting](https://github.com/mimblewimble/grin-pm/blob/master/notes/20190430-meeting-development.md) covered planning for v1.1.0, future I2P support, git branching models, and tx slate versioning.

  * [2019 Q1 Financial Transparency Report](https://github.com/mimblewimble/grin-pm/blob/master/financials/reports/funding_transparency_2019Q1.md) is up.

  * @yeastplume been keeping busy [working on invoicing support for wallet and a rust implementation of wallet seed sharding using Samir's Secret Sharing](https://www.grin-forum.org/t/yeastplume-progress-update-thread-mar-19-to-sep-19/4303/19).

  * @quentinlesceller has been hard at work [getting Azure Pipelines properly set up](https://github.com/mimblewimble/grin/pull/2744) as we move away from Travis.

  * Forum discussion on [optimising Merkle Proofs by aggregation](https://www.grin-forum.org/t/aggregate-merkle-proofs/4948).

  * [Niffler wallet v0.3 is out](https://www.grin-forum.org/t/niffler-an-out-of-the-box-open-sourced-grin-gui-wallet/4760/6), incorporating v1 of the Hedwig relay service.

  * The [videos of the talks at Grin Amsterdam](https://www.youtube.com/playlist?list=PLvgCPbagiHgpJXhrKAJu0Q-mbCVhpqgu7) some weeks back are now up on Youtube.

  * More Grin info [here](https://grinnews.substack.com/).

 **Beni from Beam**

 _Beam is a confidential and scalable cryptocurrency based on Mimblewimble._

  * We will be attending some super cool events during the NYC Blockchain Week 2019, this is [here](https://medium.com/beam-mw/mimblewimble-nyc-consensus-2019-2d4ea1db374) to know all the  _wheres_  and  _whens_

  * Have a look on this [Atomic Swap Demo](https://www.youtube.com/watch?v=exdkYRGkjjM&t=1s) done by Beam’s CTO, Alex Romanov

  * R&D Updates

  * We have begun the preparation for the Fork Release

  * Good progress on the Lightning Network POC (Laser Beam)

  * Still a lot to be done when it comes to the integration with Trezor T and to the development of our Atomic Swap Feature [#447](http://email.mg1.substack.com/c/eJwlUMmOwyAM_ZpymwgIgXLg0Nluc55jxOI2aBISgWmVvx_SSpb8vD3bz1uE25p3g1CQ1AJ5jMGQYKjiXjkSy3jNAIuNsyFbdXP0FuOaji4uJCWTCQK0Y1Lx4aw1syF4eeZuuHqttOSKk20tONoaIiQPBu6Q9zUBmc2EuJVTfznx72a3iFN1nV-XFryDXX5-G3ANNBdLqVAaEEKRaDhlmgrOmWyo71j3JcSH0vQ8fEoqejqcBF1urCvVFbT-72Al2ThIsVUOzrfl8Uw-j8N9A5PgUWZAhEzwJUf7d2w9S00R9xGSdTMEg7nCa6xpMDBJKWlrwto0Suag3nK8W7__AxPYc7A)

  * Work in progress on Bright Boson 2.1 for Desktop and Mobile wallets

  * Work on the Mobile Restore functionality

  * We have begun to develop the following features:

    * Add dialogue window on "Confirm seed phase" screen [#132](https://github.com/BeamMW/ios-wallet/issues/132)

    * Reference Exchange Rate for Wallet Balance [#127](https://github.com/BeamMW/ios-wallet/issues/127)

 **Arnaud from AZTEC Protocol**

 _AZTEC Protocol is an efficient zero-knowledge protocol built on top of
Ethereum, making plug-and-play value transmission and asset governance privacy
tools for developers and companies.  _

  * We have submitted an [update to EIP-1108](https://github.com/ethereum/EIPs/pull/1987), which aims to reduce the gas costs of key opcodes and precompiles used in elliptic curve cryptography. [This EIP](https://github.com/ethereum/EIPs/blob/e81104b20f9c4794167dbad9d76e13fd5eb3f3e5/EIPS/eip-1108.md) would benefit a variety of protocols (including Zether, Rollup, Matter Labs and of course AZTEC). For example, an AZTEC transaction would go from ~820k gas to about 197k gas.

  * Our work on a better client side library continues, focussing on making APIs more developer friendly friendly.

  * This week our CTO Zac was on the [Zero Knowledge Podcast](https://twitter.com/zeroknowledgefm/status/1123897748670025733), talking about range proofs, standards, and privacy on Ethereum.

  * In addition to the two cryptographer roles, we are now hiring for a **Senior Solidity Engineer** and a **Senior Engineer**. You can apply [here](http://email.mg2.substack.com/c/eJwlUEuOwyAMPU3ZNSKQpGHBoq1mrhHxcVumBEfgTJU5_RBF8sKy_fw-zhA8MW96wUJsLZCn4LVQgg8t87rz7diPLJTpkQFmE6KmvAJbVhuDMxQw7fe9kuylwUnVg3RcXQYu7eDAenvpjOx5Lweh2M4xmdUHSA40_ELeMAGL-kW0lJO8nsR3LZOeEBuHe_tH4M5LRkKH8Szr6AdtYUEL3iouRcs7LjvRtM2NX-_jnY-3QbS37ut66vj8FE1ZbSHj3vXfzLI2OVUBdecy-EBzSNQEPJTRtoBO8CkRiCAzOkKpXqcKntcUaJsgGRvB6wNSvUt1kQOrNB5rPklXsfjAxwfz-x-f0nXk), or by emailing [arnaud@aztecprotocol.com](mailto:arnaud@aztecprotocol.com) with the name of the role as the subject.

#### Smart contracting platforms

 **Evan from[Ethereum](https://weekinethereumnews.com/)**

 _Ethereum  is a decentralized platform for applications that aims to resist
fraud, censorship or third-party interference._

  * The Ethereum Name Service permanent registrar has now been deployed. You have [one year to migrate](https://manager.ens.domains/)

  * [Metacash](https://medium.com/lamarkaz/dai-in-the-hands-of-all-8ed335879ae9): gasless (using metatransactions with CREATE2) noncustodial Dai wallet for Android, with iOS coming.

  * RicMoo on CREATE2 magic: [offchain contract wallets which can be updated](https://blog.ricmoo.com/wisps-the-magical-world-of-create2-5c2177027604)

 **Jing from Plasma**

 _Plasma Group is building "Generalized Plasma", a layer 2 scaling
infrastructure for Ethereum that allows for general state transitions on layer
2._

  * Published explainer of the generalized plasma architecture [on medium.](https://medium.com/plasma-group/plapps-and-predicates-understanding-the-generalized-plasma-architecture-fc171b25741)

  * Prototyped research of offline atomic swaps, allowing for batch defragmentation

  * Cleaned up the last of the research blockers for plasma payments

  * Had a cringey AMA on [Youtube Live](https://youtu.be/5QqWB3ZMqdQ).

 **Erik from NEAR**

 _NEAR is a sharded proof-of-stake blockchain._

  * 12 PRs in [nearcore](https://github.com/nearprotocol/nearcore) from 6 different authors

  * Implementation of [Nightshade sharding](https://ethresear.ch/t/nightshade-was-whale-fishing-a-new-near-sharding-design/5275) is in progress - [PR with 9.5k+ lines in 45+ commits](https://github.com/nearprotocol/nearcore/pull/928).

  * Application/Dev layer

    * [Adding Access keys to Nearlib](https://github.com/nearprotocol/nearcore/pull/918)

    * CLI dev tools (near-shell):

      * [Use NODE_ENV-driven config in tests](https://github.com/nearprotocol/near-shell/pull/35)

      * [Optimized AssemblyScript builds](https://github.com/nearprotocol/near-shell/commit/f8a96615bdfc8070fdb10916248ff3e6f7e9a9f9)

      * Removed extra dependencies to allow faster installs

    * NEARStudio

      * [Ask user confirmation before closing tab with unsaved changes](https://github.com/nearprotocol/NEARStudio/commit/5f19b76d35feb3552cea9e5a9360d83f7c0d2132)

      * [Downloaded project has dev keys necessary for deploy](https://github.com/nearprotocol/NEARStudio/pull/118)

    * Wallet

      * Working on account recovery: [UI](https://github.com/nearprotocol/near-wallet/pull/29) and [backend](https://github.com/nearprotocol/near-contract-helper/pull/28).

  * Blockchain Layer

    * [Added ETH headers validation](https://github.com/nearprotocol/nearcore/pull/901) as initial step for ETH <> NEAR bridge.

    * [Benchmarking tools](https://github.com/nearprotocol/nearcore/pull/921) and comparison with Tendermint.

 **AJ from Tezos**

 _Tezos is a self-amending blockchain that features formally verified smart
contracts, on-chain governance, and a proof-of-stake consensus algorithm which
enables all token holders to participate in the network.  _

  * The Final "Promotion" Phase of the first Historical Tezos Amendment has started. Keep track [here](https://tzscan.io/proposals). Once reaching 81% Quorum, then new Tezos upgrade will seamlessly go live. 

  * An update from Tezos Baker and Builder, Cryptium Labs: [Meanwhile at Cryptium Labs](https://medium.com/cryptium/meanwhile-at-cryptium-labs-1-part-ii-607227fc6d65)

  * Cloud HSM support for Tezos on [Azure ](https://github.com/tezzigator/azure-tezos-signer)and [Google Cloud ](https://github.com/tezzigator/remote-signer/tree/gcp-nonbigtable)is now available

  * [Decet is building a new a type of decentralized exchange commodities on Tezos](https://medium.com/@gspeagle/the-whats-whys-basis-price-in-grain-markets-and-decets-tezos-solution-5898d6352b29), specific to grain producers. 

  * [Go Tezos Major Release v1.0.0](https://definitelynotagoat.github.io/go-tezos/), A GoLang Tezos Library

  * [Learn](https://medium.com/@keefertaylor/signing-tezos-transactions-with-ioss-secure-enclave-and-face-id-6166a752519) about Keefer Taylor’s project that enables you to sign Tezos transactions with iOS’s secure enclave and Face ID

 **Topper from Quorum Control**

 _Quorum Control makes Tupelo, a permissionless proof of stake DLT platform
purpose-built to model individual objects that enables flexible public or
private data models._

  *  **Ongoing Production Framework of Tupelo TestNet**

  * Infrastructure improvements focused on bootstrapping process for signing nodes 

  * Overnight _daily_ performance benchmarking process in development

  * Protobuff conversion of internal type handling - more seamless types between SDKs

  * Read our published post “[No Smart Contract Needed: Real Estate on Tupelo](https://www.quorumcontrol.com/blog/2019/4/30/no-smart-contract-needed-real-estate-on-tupelo)” 

**Michael from Loom**

 _Loom Network is a platform for building highly scalable DPoS sidechains to
Ethereum, with a focus on large-scale games and social apps._

  * Released DPoS V3.0 -- includes multiple delegations per user, redelegations to other validators, merging of reward delegations, referrer rewards for wallets, voting power cap, statistics in preparation for enabling slashing, web3 Json interface now works with block explorers, Go contracts have alpha support via web3, and various bug fixes

  * Launched [Trezor support for PlasmaChain staking ](https://twitter.com/loomnetwork/status/1125375961896243200)via Metamask

  * 188M LOOM tokens are now staked on PlasmaChain, which amounts to ~24% of circulating supply

  * [Battle Racers](https://medium.com/loom-network/loom-sdk-projects-battle-racers-collect-parts-customize-cars-trade-with-others-and-race-in-7f1b588285e2) is the latest game being built on Loom

 **Myles from EOS**

 _EOS is a new blockchain architecture designed to enable vertical and
horizontal scaling of decentralized applications._

  * The EOS [resource exchange (REX)](https://medium.com/eos-new-york/the-ultimate-guide-to-rex-participation-on-eos-9cc0e449b320) is officially live on the mainnet 

  * [EOSIO v1.8.0](https://medium.com/eosio/eosio-version-1-8-0-rc1-2d2d68995bbe) release candidate published. New features will allow dApps to abstract away blockchain resource management from end-users. 

  * Dan Larimer [published](https://medium.com/@bytemaster/high-liquidity-price-pegged-token-algorithm-d86d71188162) an idea for a new model for decentralized stablecoins 

  * EOS New York put forth a [proposal](https://medium.com/eos-new-york/addressing-eos-token-smart-contracts-and-a-proposal-for-core-development-funding-on-eos-f43b91c57fe2) for a new form of blockchain revenue. Read more about it in Greymass's post [here](https://blog.greymass.com/eos/@greymass/greymass-support-of-the-tokenauction-referendum-proposal)

  * Liberland [announced](https://cryptodaily.co.uk/2019/04/liberland-initiates-decentralized-autonomous-government-with-eosio) that it will use EOSIO to build various blockchain-based government services

 **Zaki from Cosmos**

 _The  Cosmos Network is a decentralized network of independent, scalable, and
interoperable blockchains._

  * Videos of the two most recent IBC calls [#3](https://www.youtube.com/watch?v=C8cGyDvYSQU&t=12s) and [#4](https://www.youtube.com/watch?v=SKwxxlyNW8w&t=2s)

  * [Change Parameters like inflation etc via governance proposa](https://github.com/cosmos/cosmos-sdk/pull/4206)l

  * Governance proposal[ #7](https://hubble.figment.network/cosmos/chains/cosmoshub-2/governance/proposals/7) use the community pool as an on-chain treasury

  * Working on Gitian based [reproducible builds ](https://github.com/cosmos/cosmos-sdk/pull/4262)of the Cosmos Hub

 **Kate and Dean from Agoric**

 _Founded by pioneers in secure development and distributed systems, Agoric
uses a secure subset of JavaScript to enable object capabilities and smart
contracts._

  * On our[ Electronic Rights Transfer Protocol (ERTP) branch](https://github.com/Agoric/SwingSet/tree/ertp-again/demo/contractHost), Mark has made some major advances. We’ve split our purse abstraction into ‘purses’ and ‘payments,’ where payments represent digital assets in transit, with the transfer rights locked up. We’ve also added a way to generalize kinds of digital assets (fungible, non-fungible) and valid operations on them. Lastly, our contracts now have a flexible API for representing a particular position in an ongoing smart contract, which can itself be bought and sold. Someone who buys a position in a smart contract can verify with the contract host to see what they would be joining. 

  * We [implemented a new device model](https://github.com/Agoric/SwingSet/issues/26) for their "SwingSet" environment, in which external functions are made available as capability-oriented "device nodes", allowing them to be shared between vats and managed just like normal objects. This will support inter-machine and inter-chain communication links in the next few weeks.

  * We’ve added a [“Comms” vat ](https://github.com/Agoric/SwingSet/tree/master/src/kernel/commsSlots)to our SwingSet environment, which is responsible for sending and receiving messages from external machines and translating and relaying them to other vats on the same machine.

#### Financial Infrastructure

 **Antonio from dYdX**

 _dYdX is a decentralized exchange for margin trading, borrowing, lending, and
eventually derivatives. dYdX allows traders to trustlessly short and get
leverage on crypto assets._

  * Just 5 days after our public launch we're already up to over $2.3M outstanding supply and $800k outstanding borrow on dYdX!

  * Shipping new frontend features: Added tooltips to the app and working on adding trade history

  * Working on adding USDC to dYdX. If you're interested in lending or borrowing high volumes of USDC please reach out to [contact@dydx.exchange](mailto:contact@dydx.exchange)

  * [Hiring](https://dydx.exchange/careers/) product designers and engineers full-time in SF!

 **Coulter from MakerDAO**

 _Maker is comprised of a decentralized stablecoin, collateral loans, and
community governance._

  * April was extremely eventful for Maker, so if you missed anything, get a recap of all updates, partnerships, and more in our Making Maker [blog](https://blog.makerdao.com/making-maker-april-2019/) post.

  * Maker has become an associate founding member of the International Token Standardization Association (ITSA). More info [here](https://itsa.global/maker-became-an-associate-founding-member-of-the-international-token-standardization-association-itsa/).

  * On our weekly community call, we demoed a first look at the Multi-Collateral Dai CDP Portal. Coindesk [recapped](https://www.coindesk.com/makerdao-demos-tech-to-back-stablecoin-dai-with-any-crypto-asset?utm_source=twitter&utm_medium=coindesk&utm_term=&utm_content=&utm_campaign=Organic%20) it.

 **Lazar from MARKET Protocol**

 _MARKET Protocol is a framework for creating tokens that track prices of
traditional or digital assets._

  * Completed rewards program UI design

  * Rolled out alerts and notifications using PagerDuty

  * Added MKT:USD rate endpoint to MPX API

  * Integrated new contracts and middleware with MPX admin

  * Refactored MARKET.js in preparation for integration with ethers.js (web3 replacement)

 **Robert from Compound**

 _Compound is a money market protocol on the Ethereum blockchain — allowing
individuals, institutions, and applications to frictionlessly earn interest on
or borrow cryptographic assets without having to negotiate with a counterparty
or peer._

  * [Announced](https://twitter.com/compoundfinance/status/1124216392251609088) Compound v2 alpha test

#### Layer two and interoperability

 **Rahul from 0x**

 _0x_  is an open protocol that enables the peer-to-peer exchange of assets on
the Ethereum blockchain.

  * 0x v3.0 possible feature set released on our [forum](https://forum.0x.org/t/0x-v3-feature-set/366)

  * [April dev update](https://blog.0xproject.com/development-update-18-april-2019-dbb5d63aa60b) \- in particular, check out our [ERC 721 support for 0x Instant](https://0x.org/instant)

  * New hires Patryk Adas (Designer) and David Sun (Intern)

 **Tony from Liquidity.Network**

 _Liquidity Network is a transfer and swap platform for any token_

  * Liquidity Network releases v2 of the mobile app with the following cool features. Details can be found [here](https://blog.liquidity.network/2019/05/02/liquidity-v2-mobile-app-release/).

    * Sleek design and cool interface 

    * Support for ERC-20 tokens on-chain & off-chain 

    * Support for [$DAI](https://twitter.com/search?q=%24DAI&src=ctag)

    * Improved user experience 

    * Hub security checks   

  * Integrating the TEX library into the front-end and working on client performances

 **Dong Mo from Celer**

 _Celer Network is a layer-2 scaling platform that enables fast, easy and
secure off-chain transactions for not only payment transactions, but also
generalized off-chain smart contracts._

  * We finished new “Backup your wallet” flow and tested Alpha Mainnet OSP config and mobile SDK.

  * We tested game inviting flow, fixed bugs and edge cases.

  * We tested and refined app adaptability for different games from the developer portal.

  * We've completed dispute design UI flow for fully decentralized turn-based games and the setup of a new backend stack for Alpha Mainnet Launch.

  * We are in the process of testing and fixing issues found on the new backend.

  * We have Implemented a more robust on-chain event monitoring and support payments with numeric conditions, not only boolean.

 **Alexandra from Parity Technologies**

 _Parity  Technologies builds core blockchain infrastructure, from Parity
Ethereum, an Ethereum client, to Polkadot, an interoperable blockchain
network._

  * [New Polkadot website](https://polkadot.network/). 

  * In Hong Kong, Gavin Wood [spoke on staking on Polkadot.](https://twitter.com/polkadotnetwork/status/1124053865899466752)

  * New [Builders’ Portal](https://twitter.com/ParityTech/status/1123888189226266625) for Polkadot. 

  * [Web3 Summit tickets are live.](https://twitter.com/web3summit/status/1123201575009300482)

  * New Substrate tutorials [here](https://twitter.com/nczhu/status/1122494821774573570). 

  * Build Your Own Blockchain with Substrate [workshop](https://www.meetup.com/meetup-group-eEMURxBh/events/261105483/) during NY Blockchain Week. 

  * Robert Habermeier will be at the [Founders meetup](https://www.meetup.com/meetup-group-eEMURxBh/events/261105680/) during NY Blockchain Week. 

  * Web3 Foundation is [providing grants to build the Web3 ecosystem](https://github.com/w3f/Web3-collaboration/blob/master/grants/grants.md).

  * We’re hiring a [Release Manager for Parity Ethereum](https://twitter.com/ParityTech/status/1123922149134278660).

#### Application infrastructure

 **Wes from Theta**

 _Theta is an end-to-end infrastructure for decentralized video streaming._

  * Improved off-chain transaction batching logic, resulting in 80% reduction in redundant/unnecessary on-chain transactions for a given number of concurrent users

  * On the streaming side, introduced new technique of slicing video into smaller segments, improving peering efficiency

  * Completed first monthly distribution of TFUEL for users running the Pre-Guardian Node client

 **Doug from Livepeer**

 _Livepeer is a decentralized video infrastructure network, dramatically
reducing prices for developers and businesses building video streaming
applications at scale.  _

  * [Writeup and summary of the DTok, decentralized TikTok, app](https://medium.com/stakecapital/ethcapetown-hackathon-winners-168520fdefec) built by the Stake Capital team on Livepeer.

  * Achieved 99.5% success rate for live video transcoding on the Streamflow test network. Targeting over 99.99% before mainnet upgrade.

  * Shipped "API Node" to create simple REST interface for developers getting started with Livepeer's upcoming Streamflow release.

 **Ryan from FOAM**

 _FOAM  is building spatial applications and proof of location that bring
geospatial data to blockchains and empower a consensus driven map of the
world._

  * Highest amount of activity on the FOAM Map yet, this week saw 25+ challenges with active voting. The voting contract increased from 400k tokens to 800k , 1.7m, 2.7m to over 7m tokens. 

  * Third [weekly scavenger](https://twitter.com/Blockcities/status/1124790537368887300 "https://twitter.com/Blockcities/status/1124790537368887300") hunt with Blockcities complete, now utilizing an Ethereum logic app running on Microsoft Azure cloud infrastructure for automation. 

  * Cartographer Tools Dashboard - [Development Preview released ](https://discourse.foam.space/t/cartographer-tools-development-preview/781 "https://discourse.foam.space/t/cartographer-tools-development-preview/781")

  * [FOAM Map Developer Grant program announced](https://discourse.foam.space/t/announcing-the-foam-map-developer-grant/783 "https://discourse.foam.space/t/announcing-the-foam-map-developer-grant/783")! We are excited to see what will be built from this.

  * [FOAM at New York Blockchain Week](https://discourse.foam.space/t/new-york-blockchain-week-with-foam/771 "https://discourse.foam.space/t/new-york-blockchain-week-with-foam/771"): Find us at Ethereal, Token Summit and ETH New York hackathon happening at the FOAM Offices in the New Lab. We will be hosting workshops, talks and API prizes. 

#### Other

 **Bowen from Hydro/DDEX.io**

 _Hydro  Protocol is an open source framework for building Decentralized
Exchanges. DDEX is the first decentralized exchange for Ethereum and ERC-20
tokens built on the Hydro Protocol. _

  * Automated market making bots with multiple strategy to provide liquidity for hydro dexes. \- empower everyone to be liqudity provider :<https://github.com/HydroProtocol/amm-bots> 

  * A Decentralized Exchange Scaffold - launch a DEX in minutes: <https://github.com/HydroProtocol/hydro-scaffold-dex>

 **Sam from OpenBazaar**

 _OpenBazaar is an open source project developing a protocol for e-commerce
transactions in a fully decentralized marketplace._

  * OpenBazaar [version 2.3.3](https://github.com/OpenBazaar/openbazaar-desktop/releases/tag/v2.3.3) was released. This release includes one of the most significant UX improvements to date: Listings load almost instantly. We've changed how we do IPFS and IPNS calls, as well as added a tiered routing structure, and the result is a [huge improvement](https://youtu.be/PoVWVLSH7Tg) in loading speed.

  * The infrastructure needed for the social features of the Haven app is now completed, and internal testing of the app is reaching the final states.

####  **China & Asia Updates**

 **Mining 🔨**

  * Bitmain announced a new BTC/BCH miner T17 (7nm, 40TH/s)

  * SparkPool, the largest $ETH mining pool, [closed out its pooling on $ETC and $XMR](https://support.sparkpool.com/hc/zh-cn/articles/360000254562-%E5%85%B3%E4%BA%8EETC-XMR%E7%9F%BF%E6%B1%A0%E4%B8%8B%E6%9E%B6%E6%B8%85%E5%B8%90%E9%80%9A%E7%9F%A5) in order to focus on its staking business

  * Other than Sparkpool and F2pool, the majority of top Asian PoW mining pools show no interest in staking, due to the current limited TAM (~$6B of total PoS coins) and there is no advantage when competing with exchanges and wallets for stake access 

  * After the recent “China Mining Ban”, $BTC hash rate sees a steady growth back to 54E, now less than 10E from ATH 60E

 **Trading/Exchanges 💰**

  * UEX, an Asia based exchange shuts down due to “Business Adjustment”

  * Korea exchange CoinBin (formerly Youbit) filed for bankruptcy with a loss of $26M and a series of scandals involving executive inside jobs and exit scams 

  * We are expecting more mid-to-small sized exchanges started in the last cycle to shut down over time 

  * A strong signal of the IEO hype dies down is from the recent Binance Launchpad IEO $MATIC: over 58% of the IEO participants won the $MATIC allocation ticket via the lottery system. The previous IEO $CELER saw a lottery win rate of only 1%. The significant decline of the Binance IEO hotness indicates the wave of IEO hype is quickly fading away 

**Regulation** **🚧**

  * SEC of Thailand approved the [first initial coin offering (ICO) portal](https://www.bangkokpost.com/business/news/1643532/), which will be able to issue securities token offerings

  * Singapore MAS and the central banks of Canada (BoC) successfully completed a [cross-border payments using blockchain technology](https://www.coindesk.com/central-banks-settle-cross-border-payments-with-blockchain-for-first-time) with their central bank digital currencies that are in trial period 

  * Japan FSA has pushed out[ new regulations for cold storage and hot wallet management](https://www.reuters.com/article/us-japan-cryptocurency/japan-to-require-crypto-exchanges-to-bolster-internal-oversight-source-idUSKCN1RS0YO) to combat insider jobs 

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

