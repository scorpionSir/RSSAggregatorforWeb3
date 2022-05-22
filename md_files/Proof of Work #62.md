[![](https://substackcdn.com/image/fetch/w_96,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F37b09348-f4f1-47a2-b9e0-a2007299e6e4_256x256)](https://proofofwork.news)

# [Proof of Work](https://proofofwork.news)

SubscribeSign in

Share this post

Proof of Work #62

proofofwork.news

Copy link

Twitter

Facebook

Email

# Proof of Work #62

[Eric Meltzer](https://substack.com/profile/138320-eric-meltzer)

Apr 16, 2019

[Share](javascript:void\(0\))

Good afternoon from sunny but ridiculously windy Boston.

When I found out about Bitcoin in 2013, it felt like stumbling into a parallel
reality. I grew up on a strict diet of cyberpunk scifi and it felt like
something straight out of a Gibson or Sterling book—I couldn’t stop reading
about how the protocol worked, how people were using it (shoutout
SatoshiDice!) and what effects it might start to have on the global community.

Since then, as FinanceBros and other establishment critters descended on the
space, a lot of what happened with Bitcoin was exciting to me an investor, but
frankly boring as a child of the Neuromancer/Snow Crash era of scifi.

In the course of exploring custody solutions for Primitive with Dovey, I
learned about Shamir’s secret sharing, an algorithm that allows you to take a
secret string of text and split it into m pieces, of which n are required to
reconstitute the original “secret.” Invented by Adi Shamir (the “S” in “RSA”)
in 1979, SSS is a time-tested piece of pretty simple cryptography, but it
enables a lot of cool things. The more I played around with it, the more I
wanted to use it as the basis for a game, an epic hunt for Bitcoin that would
be spread around the world.

Long story short, we assembled an amazing team, and yesterday [sent out the
first clue](https://twitter.com/notgrubles/status/1117819810702872576) (via
the Blockstream satellite, shoutout
[@grubles](https://twitter.com/notgrubles/)!) that kicked off a [global
hunt](http://satoshistreasure.xyz) for 1 million dollars in BTC. The response
has been absolutely overwhelming. People showed up to the 10 spots we
indicated around the world where keys would appear en masse—some drove over 3
hours to get to a spot. Others figured out how to brute force the encryption
we used and solved the clues without having to travel (something which we
hoped would happen, but thought would take weeks—in reality it took 30
minutes..)

People are forming teams, talking strategy, speculating on the value of keys
and where the next clues will show up… and our hypothesis that Bitcoin and
cryptography enable a new type of online/offline game experience seems to be
getting validated. Subreddits are being created. Telegram groups are forming.
Our poor mongoDB is getting hammered with signups. We’re all a bit exhausted
after this first day, but we’re also incredibly excited to see what people do
with the next set of clues.

Small housekeeping update: we now order PoW updates by EricRank, a proprietary
algorithm that produces an ordinal ranking based on how interesting Eric finds
a given update. It’s prone to false negatives, but it feels better than the
old way where some of the coolest projects (Hi OpenBazaar! Maker! Sia!) are
permanently relegated to the bottom of the update. Let me know if you guys
like this better, or prefer the old format.

More next week, thanks as always for reading.

#### **China & Asia Updates**

 **Mining 🔨**

  * Bitmain S19 (53T) sold out in 4 mins. However, some believe this was a show to make it appear as though it was in high demand. The actual sales number is unknown 

  * Whatsminer launched their flagship M20S (68T) the same day in Shenzhen, expected shipment around July 

  * The so-called “mining ban” last week does not impact ANYTHING on the ground, period. [ _ed: dovey tells it like it is_ ]

  * $LTC hashrate hit ATH before, while $BSV continues to drop. Network hashrate is the only security guarantee for a PoW coin, and a clear indicator of where miner confidence lies. $LTC has a very strong miner community in Asia, second to $BTC

 **Trading 💰**

  * The biggest bank in Japan, Bank of Tokyo-Mitsubishi, started the trial of its [yen pegged stable coin ](https://www.ccn.com/japans-biggest-bank-to-carry-large-scale-trial-of-cryptocurrency-mufg-coin)“MUFG coin” last week. Over 10k of its banking customers participated in the trial 

  * It’s said that over half of the newly issued $200M tether were distributed to Chinese traders through a few local brokers [ _ed: I also heard this independently, seems likely_ ]

 **Regulation** **🚧**

  * Many lending or OTC desks in China which turned out to be Ponzi schemes are now on the verge of blowing up, so be careful if you are dealing with any 

  * China Banking and Insurance Regulatory Commission (CBIRC) urged further investigation into illegal fundraising activities involving cryptocurrency and other commonly used concepts. The use of cryptocurrency is common in local ponzi schemes. A formal legislative bill will be out in a few months. But to be honest, I rarely see any regulatory action from China impact the macro crypto market, unless it plans to fully legalize crypto and revert what it banned before

 **Misc 🤓**

  * Star Xu, the founder of OKEx, stepped down as the legal representative of OKEx’s operating entity in mainland China. Doing so sort of de-risked himself from any criminal charges that might be lobbied towards OKEx on the mainland 

  * Tencent launched a Pokémon Go -like LBS game called [“Let’s hunt the beat together”](https://trustsql.qq.com/chain_oss/game.html) powered by its blockchain platform TrustSQL to enable gaming features similar to CryptoKitties 

**Korea**

  * Government regulation continues to stifle exchanges by blocking new customers from making fiat deposits to exchange accounts. Korean companies are also not allowed to deposit to exchanges for fear of money laundering.

  * Crypto-collateralized lending is considered to be a banking service and thus restricted, so it has not been as active in Korea as it has in the US.

  * Any sort of crypto derivatives trading is illegal. In the past, Coinone tried to launch a 4x BTC token and it was banned.

 **JZ from Decred**

 _Decred  is an autonomous digital currency with a hybrid consensus system. It
is built to be a self-ruling currency where everyone can vote on the rules and
project-level decision making proportionately to their stake._

  * It's happening! [Marco has released his proposal outlining a DAE](https://proposals.decred.org/proposals/c96290a2478d0a1916284438ea2c59a1215fe768a87648d04d45f6b7ecb82c3f) (Decentralized Autonomous Entity) that would have full control over the Decred project treasury. To protect against a wide variety of attacks there will be a two-fold process needed to release funds; a draft spending proposal will need to be signed by a Politeia identity key (off-chain) followed by the stakeholders approving the transfer through a vote (on-chain) much the way consensus votes are effectuated. Some more details were provided in an interview with Marco that was [published by Invest in Blockchain this week](https://www.investinblockchain.com/put-your-money-where-your-mouth-is-decreds-treasury-proposal-closer-true-dae/).

  * We're psyched to be hosting our second [San Francisco Decred meet up on April 18](https://www.meetup.com/San-Francisco-Decred-Meetup/events/260046546/). Coinbase has been gracious enough to provide a venue for us, and Decred dev Luke Powell will be giving a talk on governance and funding in Decred, followed by a seminar on the broader topic of cryptocurrency funding models.

  * The [March edition of the Decred Journal](https://decredcommunity.org/blog/decred-journal-march-2019) is out. This issue marks a year of amazing work by bee the editor who manages the journal, and who a few of us suspect might actually be a small team of anonymous contributors.

  * On the Politeia front, the stakeholders authorized a [budget to fund integration work for Trust Wallet](https://proposals.decred.org/proposals/2ababdea7da2b3d8312a773d477272135a883ed772ba99cdf31eddb5f261d571). As it turns out the Trust Wallet team has already completed most of the work. If someone is looking to cut their teeth on a Go project relating to Decred and earn some coins in the process we're looking to have a dev do the final piece of the integration which involves adding Decred support to [Trezor Blockbook](https://github.com/trezor/blockbook). We're always looking for motivated devs so don't hesitate to [reach out](https://www.decred.org/community/).

 **David from Sia**

 _Sia is a decentralized cloud storage platform leveraging blockchain
technology to create a data storage marketplace that is more robust and more
affordable than traditional cloud storage providers._

  * Release Progress: 1.4.1: The Sia team and various community contributors have been squashing various bugs in Sia and Sia-UI including bugs around file renaming, memory leaks, and using the `siac` utility.

  * Community contributor geo-gs got an interesting bit of code merged in to Sia this week. His Merge Request titled “Add Genesis Siacoin Allocation” sets up Sia to be more easily forked from the genesis block for use in other Crypto projects supporting an Airdrop. Just to clarify, this is a fork of Sia, and Sia is not airdropping any coins; this MR simply makes it easier to fork and airdrop coins for projects based off Sia.

  * Nebulous is hiring for 5 new positions. Check them out [here](https://angel.co/nebulous/jobs).

  * Community member tbenz9 [wrote a blog post](https://medium.com/@tbenz9/securing-sia-wallets-renter-and-hosts-17a020d8b86b) on how to secure your wallet, renters, and hosts.

 **Coulter from MakerDAO**

 _Maker is comprised of a decentralized stablecoin, collateral loans, and
community governance._

  * We have another testnet release for Multi-Collateral Dai. A full rundown of what's been updated can be read [here](https://blog.makerdao.com/update-the-road-to-multi-collateral-dai-kovan-release-v0-2-3/). 

  * We have introduced a DIY Meetup program and micro-grants initiative. If you're a fan of Maker and want to meet with others in your region to talk about Dai, [check it out.](https://blog.makerdao.com/makerdao-global-meetups-and-micro-grants-initiative/)

  * Announced upgrades to the Maker Ecosystem Foundation [structure.](http://structure./)

  * At The Bold Awards, we won Best ICO/Cryptocurrency (though we never had an ICO so we'll focus on the latter). 

  * Dai is now [integrated](https://medium.com/originprotocol/pay-with-dai-on-origin-announcing-our-first-stablecoin-integration-43f86d5d7982) into Origin Protocol, allowing you to pay for goods or services with our decentralized stablecoin. 

 **Arnaud from AZTEC Protocol**

 _AZTEC Protocol is an efficient zero-knowledge protocol built on top of
Ethereum, making plug-and-play value transmission and asset governance privacy
tools for developers and companies.  _

  * Last week we officially started the first of our two audits. During our prep run, we reached 96% test coverage, and fixed a couple of important bugs.

  * This week, we are working on 2 new proofs: **public range proofs** and **private range proofs** , which allow AZTEC assets to test whether an encrypted balance is worth more, or less than either a public balance or a private balance.   
This is used for assets which have minimum/maximum notionals for trades, or
maximum/minimum ownership requirements for asset holders.

  * This week we've also started work on the trustless post-processing step of our trusted setup. We'll be publishing more information soon.

  * We’re still hiring for two cryptographers to join the team. You can apply [here](http://email.mg2.substack.com/c/eJwlUEuOwyAMPU3ZNSKQpGHBoq1mrhHxcVumBEfgTJU5_RBF8sKy_fw-zhA8MW96wUJsLZCn4LVQgg8t87rz7diPLJTpkQFmE6KmvAJbVhuDMxQw7fe9kuylwUnVg3RcXQYu7eDAenvpjOx5Lweh2M4xmdUHSA40_ELeMAGL-kW0lJO8nsR3LZOeEBuHe_tH4M5LRkKH8Szr6AdtYUEL3iouRcs7LjvRtM2NX-_jnY-3QbS37ut66vj8FE1ZbSHj3vXfzLI2OVUBdecy-EBzSNQEPJTRtoBO8CkRiCAzOkKpXqcKntcUaJsgGRvB6wNSvUt1kQOrNB5rPklXsfjAxwfz-x-f0nXk), or by emailing [arnaud@aztecprotocol.com](mailto:arnaud@aztecprotocol.com) with the name of the role as the subject

 **Ari from Decentraland**

 _Decentraland is a virtual world where you can build and explore 3D
creations, play games and socialize. [ed: decentraland has managed to get a
serious community together and people are making some pretty beautiful things.
I’m a fan]_

  * The [Creator Contest for the Builder](https://contest.decentraland.org/) concluded with around 10,000 unique submissions!

  * Since the Creator Contest, the Builder now has several UX improvements and bug fixes: a redesigned project overview page and mobile site, and we are finishing an import/export feature allowing scenes to be transferred between the SDK and the Builder.

 **Zaki from Cosmos**

 _The  Cosmos Network is a decentralized network of independent, scalable, and
interoperable blockchains._

  * We anticipate governance [proposal 3](https://hubble.figment.network/chains/cosmoshub-1/governance/proposals/3) will pass on April 17th and layout the procedure for the first network upgrade to enable transfers between on April 19th or soon after.

  * Code is [complete](https://github.com/cosmos/cosmos-sdk/pull/4036) for the proposed upgrade of the Hub.

  * We are very excited about Cosmos SDK chain [Terra](https://github.com/terra-project/core) opens sourcing their chain.

  * Lino: A Cosmos SDK powered chain with ~800k registered on the Dlive App has done about [12 million transactions](https://tracker.lino.network/#/tracker) and recently announced [PewDiePie ](https://www.coindesk.com/top-youtuber-pewdiepie-joins-blockchain-live-streaming-platform)moved to their platform. We are appreciating all the performance stress testing data coming back from these users.

  * On the Inter Blockchain Communication specification front, we merged high level documents on the [design goals and architecture of IBC](https://github.com/cosmos/ics/blob/master/docs/ibc/1_IBC_DESIGN_PHILOSOPHY.md)

 **[Optech](https://bitcoinops.org/en/newsletters/) on Bitcoin [ed: sign up
for their newsletter too! it’s great!]**

  * [History of Lightning](https://bitcoinmagazine.com/articles/history-lightning-brainstorm-beta/)

  * [lnd-admin](https://github.com/janoside/lnd-admin)

  * [Lightning Limitations](http://diyhpl.us/wiki/transcripts/boltathon/2019-04-06-alex-bosworth-major-limitations/)

 **James from Summa**

 _Summa builds tools to exchange crypto in a convenient and trustless
fashion._

  * This week we released [riemann-ledger](https://github.com/summa-tx/riemann-ledger), a simple Python library for signing Bitcoin transactions using a Ledger hardware wallet

  * Zeta got a major version to allow use by multiple applications. We also trimmed the electrum server whitelist to mitigate the effect of the recent Electrum DoS attacks

  * We just released an [in-depth exploration of standardness](https://medium.com/summa-technology/the-bitcoin-non-standard-6103330af98c) in Bitcoin. Transaction standardness controls what transactions normal users can put into blocks

 **Aviv from Spacemesh**

 _Spacemesh is a programmable cryptocurrency powered by a novel proof-of-
space-time consensus protocol._

  * Spacemesh Core: Full Node + POET Service

    * [Activation transaction flow](https://github.com/spacemeshos/go-spacemesh/pull/738)

    * New [UDP-based node discovery protocol](https://github.com/spacemeshos/go-spacemesh/pull/741) and [here](https://github.com/spacemeshos/go-spacemesh/pull/769)

    * Added block validation according to [received activation transactions](https://github.com/spacemeshos/go-spacemesh/pull/778) and [VRF](https://github.com/spacemeshos/go-spacemesh/pull/789)

    * POET proofs verification (<https://github.com/spacemeshos/go-spacemesh/pull/781>)

    * [Separate namespaces](https://github.com/spacemeshos/go-spacemesh/pull/773) for dedicated tests and CI flows

  * Spacemesh App (Wallet + Full Node)

Lots of merged PRs for the core App screens

    * Local node [UI improvements](https://github.com/spacemeshos/smapp/pull/66)

    * [Backup Wallet Screen](https://github.com/spacemeshos/smapp/pull/67) in Wallet tab

    * [Backup Wallet to file logic](https://github.com/spacemeshos/smapp/pull/69)

    * [Transactions Tab](https://github.com/spacemeshos/smapp/pull/79) (with stab data)

    * [Latest Transactions View](https://github.com/spacemeshos/smapp/pull/80) in Wallet Overview (with stab data)

    * [12 Words backup screen](https://github.com/spacemeshos/smapp/pull/78)

  * We just announced our this free community [2-days workshop](https://avive.github.io/wasm_on_the_blockchain) for blockchain and layer-2 projects that are working on wasm tech for their programmability features. Join us in Berlin this June for this special event. Participants include builders from ewasm, parity, mozilla, wasm and [wasmer.io](http://wasmer.io/). People from Spacemesh have been working on putting together this event with great people from ewasm, 1kx and Parity.

 **Johnny from Stellar**

 _Stellar is an open network for sending and exchanging value of any kind. Its
global network enables digitization of assets - from carbon credits to
currencies - and enables movement around the internet with ease._

  * Core: Stellar Core v11.0.0 is planned to be released on 4/25, with a soft release on testnet on 4/15 or 4/16 based on release of snapshot.

  * Core: Stellar Core [v11.1.0](https://github.com/stellar/stellar-core/projects/8) is planned for a mid May release, with a continued focus on performance related fixes.

  * Platform: New Go SDK is currently being dogfooded, with a plan to release more widely in the next few weeks.

  * Platform: Initial work on new Horizon ingestion service has begun — most Q2 efforts will be around creating a separate, pluggable system from the Horizon API service.

  * Kelp: Kelp UI is currently in progress, along with initial refactor of the Stellar ticker.

 **Izaak from Coda**

 _Coda is the first cryptocurrency protocol with a constant-sized blockchain.
Coda compresses the entire blockchain into a tiny snapshot the size of a few
tweets using recursive zk-SNARKs._

  * Deepthi halved [the latency](https://github.com/CodaProtocol/coda/pull/2201) between when a transaction is confirmed and when it is folded in to the succinct blockchain.

  * Brandon and Avery have [begun](https://github.com/CodaProtocol/coda/pull/2226/files) [working](https://github.com/CodaProtocol/coda/pull/2207) on our desktop wallet! UX is a priority so if you have feature requests please [make an issue](https://github.com/CodaProtocol/coda/issues/new).

  * Corey has [spec'd](https://github.com/CodaProtocol/coda/pull/2211) out our libp2p integration. This will make it possible for browser-tab nodes to connect to the gossip net and get the succinct blockchain directly.

  * I made a [SNARK function](https://github.com/CodaProtocol/coda/pull/2239) "more deterministic" using a trick I learned from Dan Boneh. The PR has an example of the kind of semantic reasoning about SNARK programs I think people should be practicing.  

####  **Ryan from FOAM**

 _FOAM  is building spatial applications and proof of location that bring
geospatial data to blockchains and empower a consensus driven map of the
world._

  * Started work on a new Curator Dashboard page for Cartographers to better track the outcome of challenges, in addition to the daily digest and email notifications 

  * Integrating 3Box NFT badges into the leaderboard 

  * Announced first Cartographer badge for top mapper of April

  * Announced a new FOAM Map Treasure hunt game in collaboration with Blockcities. A prize will be issued weekly to the Cartographer that solved the clue and adds the correct point <https://www.blockcities.co/hunt>

  * Progress on our Plasma demo MVP 

 **Paige & Zooko from Zcash**

 _Zcash is a  digital currency utilizing zk-SNARKs to enable its privacy-
protecting properties._

  * Submitted ZIP Drafts and began reviewing ECC and community-submitted [ZIP Drafts for NU3](https://github.com/zcash/zips/pulls?q=is%3Apr+is%3Aopen+label%3A%22NU3+proposal%22) consideration

  * [Blossom](https://z.cash/upgrade/blossom/) spec audit complete, begun initial implementation work

  * Released the [reference wallet Android source code](https://github.com/zcash/zcash-android-wallet-poc) for external feedback

  * More info in the full update: <https://forum.zcashcommunity.com/t/april-12-2019-weekly-update-engineering/33176> 

 **Mitchell from Monero**

 _Monero is a open-source, privacy-focused cryptocurrency using the ASIC-
resistant CryptoNote PoW algorithm. It enforces all privacy features at the
protocol level to ensure that all transactions create a single fungible
anonymity pool._

  * Monero had a bug with the Ledger device that had possible loss of funds due to incorrect change address, but the bug has been fixed, and all money that was lost has been recovered due to clever math.

  * Ledger is now safe to use provided the user is:

    \- Using GUI v0.14.0.0 (or CLI v0.14.0.2)

    \- Using Ledger Monero app v1.2.2

    \- Using Ledger Live firmware v1.5.5 or v1.6.0

 **Daniel from Grin**

 _Grin is a community-driven implementation of the Mimblewimble protocol that
aims to be privacy preserving, scalable, fair, and minimal._

  * [9 Pull Requests were merged](https://github.com/mimblewimble/grin/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A2019-04-08..2019-04-14+) in the past week, by 6 unique contributors.

  * Variable size MMR support by @antiochp [merged for 1.1.0](https://github.com/mimblewimble/grin/pull/2734)

  * @quentinlesceller in progress work on [setting up Azure Pipelines](https://github.com/mimblewimble/grin/pull/2744) as a replacement for TravisCI.

  * @yeastplume outlined his [action plan](https://www.grin-forum.org/t/yeastplume-progress-update-thread-mar-19-to-sep-19/4303/17) post Wallet API v2 in his weekly update.

  * The last [Governance meeting](https://github.com/mimblewimble/grin-pm/blob/master/notes/20190409-meeting-governance.md) discussed a Grin Improvement Proposal processes (not right now), Proof of work phaseout changes (wait and see), Funding for lehnberg part-time work (granted), and whether to allow donation for specific purposes (not via main dev fund).

  * Ironbelly mobile Grin wallet received [fellowship grant from Binance Labs](https://www.binance.com/en/blog/323308217272557568/Binance-Labs-Grants-First-Fellowship-Round-Supporting-OpenSource-Blockchain-Development).

  * Our favourite swag shop TMGOX [started accepting Grin payments via Knockturn Allee](https://twitter.com/hashmap/status/1117160465170350080?s=12).

  * [Vite mobile Grin wallet](https://www.grin-forum.org/t/a-user-friendly-mobile-wallet-for-grin-is-going-to-be-released-vite-wallet/4767) announced.

  * More Grin info [here](https://grinnews.substack.com/).

 **Evan from[Ethereum](https://weekinethereumnews.com/)**

 _Ethereum  is a decentralized platform for applications that aims to resist
fraud, censorship or third-party interference._

  * [Prysmatic eth2 dev update](https://medium.com/prysmatic-labs/ethereum-2-0-development-update-25-prysmatic-labs-5322a7762bba) – optimizing testnest for performance

  * Opera on desktop now comes with [native web3 support and Eth wallet](https://blogs.opera.com/desktop/2019/04/opera-60-reborn-3-%20-3-0-vpn-ad-blocker/)

  * zk tools and projects becoming a thing:  [websnark for fast zkSnarks generation](https://www.iden3.io/post/websnark-zksnarks-generation-browser-now-fast-and-easy) in the browser.  Also [ZoKrates v0.4.4](https://medium.com/zokrates/building-identity-linked-zksnarks-with-zokrates-a36085cdd40) – building identity-based snarks.

 **Peter from NEAR**

 _NEAR is a sharded proof-of-stake blockchain._

  * NEAR is improving developer experience and researching a new model of staking

    * 25 PRs in [nearcore](https://github.com/nearprotocol/nearcore) from 6 different authors

    * Hosted two events with Cosmos and Fluence

    * Application/Dev layer

      * Created a [proof of concept](https://nearprotocol.github.io/fortmatic-demo/) for Fortmatic integration with NEAR

      * Added Frontend deploy to the ‘deploy’ command in [CLI tool](https://github.com/nearprotocol/near-shell)

      * Added [“Top N” functionality](https://github.com/nearprotocol/near-runtime-ts/commit/20ba61dcc3d4e820bb85a0de8519bf3fff51968b) to collections in near runtime

      * Finalizing the new [wallet designs](https://projects.invisionapp.com/m/share/Y5QIVUGTVER#/357708988)

    * Blockchain Layer

      * Alex began discussion around a new model of sharding called [Whale Fishing](https://ethresear.ch/t/whale-fishing-a-new-sharding-design/5275).

      * Added testing infrastructure and improved testing coverage. 

 **AJ from Tezos**

 _Tezos is a self-amending blockchain that features formally verified smart
contracts, on-chain governance, and a proof-of-stake consensus algorithm which
enables all token holders to participate in the network.  _

  * The agenda for Tezos first all-day conference, T[Quorum Paris](https://tquorum.splashthat.com/) has been released. Join a wide variety of experts on April 18th in Paris. 

  * Bruno Le Maire, France Minister of the Economy,[ comments on Tezos development overcoming common public blockchain defects. ](https://www.capital.fr/economie-politique/bruno-le-maire-le-developpement-de-lecosysteme-blockchain-est-une-priorite-pour-le-gouvernement-1335182)

  * [Learn about building smart contracts with ReasonML](https://www.youtube.com/watch?v=GjLasXbQet8), presented by Tezos developer, Matej Sima. 

  * Tezos developer from Nomadic Labs, Pietro Abate, [discusses development on Tezos Protocol. ](https://www.youtube.com/watch?v=CIAwlFvMznU)

  * [Introducing Gingerbread](https://medium.com/zednode/introducing-gingerbread-ae61644d3bb6): an open-source project aiming to service bakers within the Tezos ecosystem

 **Topper from Quorum Control**

 _Tupelo is a permissionless proof of stake DLT platform purpose-built to
model individual objects that enables flexible public or private data models._

  * General bug fixes and upkeep

  * Other Updates:

  * Read our published post “[How to woo a Developer](https://medium.com/@stephanie_95775/have-we-put-the-cart-before-the-horse-when-it-comes-to-dlt-eaa9d6c83655)” 

  * We’re hiring a lead [community developer](https://www.quorumcontrol.com/careers). Submit resumes to [info@quorumcontrol.com](mailto:info@quorumcontrol.com)

 **Michael from Loom**

 _Loom Network is a platform for building highly scalable DPoS sidechains to
Ethereum, with a focus on large-scale games and social apps._

  * Released mobile staking for PlasmaChain, so LOOM holders can now delegate their tokens directly from their mobile wallets. [Cobo Wallet](https://twitter.com/Cobo_Wallet) is the [first to launch full native support](https://medium.com/loom-network/you-can-now-stake-your-loom-tokens-directly-from-your-cobo-wallet-plus-more-on-the-way-973fe08da3fe?__s=c1g7ppbh3pqocesaww2w).

  * Released [UI update for the PlasmaChain staking dashboard](https://dashboard.dappchains.com/).

  * 144M LOOM tokens are now staked on PlasmaChain, which amounts to ~19% of circulating supply.

  * Coins & Steel[ released a fully playable demo](https://twitter.com/coinsandsteel/status/1115605284221739008?__s=c1g7ppbh3pqocesaww2w&utm_source=drip&utm_medium=email&utm_campaign=PlasmaChain+%2B+Mobile+Wallets+%28Loom+Update+%2340%29) of their game, which is running on top of Loom.

 **Myles from EOS**

 _EOS is a new blockchain architecture designed to enable vertical and
horizontal scaling of decentralized applications._

  * EOS User Agreement was [officially adopted](https://eosauthority.com/polls_details?lnc=en&proposal=eosuseragree_20190207) as the new EOS constitution 

  * Scatter debuted [Scatter Marketplace](https://medium.com/getscatter/introducing-scatter-marketplace-5b4bb9a3cf0e), a hub to buy, sell, and rent digital goods on EOS

  * [Block.one](http://block.one/) teases their [June 1st event](https://block.one/june1/)

  * [Block.one](http://block.one/) updates the EOSIO [Ricardian contract framework](https://medium.com/eosio/eosio-software-release-ricardian-contract-specifications-and-the-ricardian-template-toolkit-a0db787429d1)

 **Kate and Dean from Agoric**

 _Founded by pioneers in secure development and distributed systems, Agoric
uses a secure subset of JavaScript to enable object capabilities and smart
contracts._

  * We merged in a number of small pull requests this week and have been working on better tutorials for our “SwingSet” vat platform for testing out smart contracts. Some of the pull requests included:

    * Using the [realms-shim repo in SES](https://github.com/Agoric/SES/pull/110) rather than the TC39 Realms proposal specification repo. 

    * [Deleting a property called “domain”](https://github.com/Agoric/SwingSet/pull/23#event-2274157379) that the Node.js REPL adds to promises. When SES tries to harden (deep freeze) all of the objects provided by Node.js, it notices that it didn’t expect the “domain” property and purposefully errors to avoid a potential vulnerability.

 **Antonio from dYdX**

 _dYdX is a decentralized exchange for margin trading, borrowing, lending, and
eventually derivatives. dYdX allows traders to trustlessly short and get
leverage on crypto assets._

  * Gearing up for the launch of our new product, stay tuned for an announcement later this week!

 **Brendan from Dharma**

 _Dharma is the easiest place to borrow and lend cryptocurrencies. It enables
non-custodial peer-to-peer lending through smart contracts on Ethereum._

  * In Dharma's first week open to the public, users borrowed over 1M USD and lent over 1.4M USD. This volume was primarily denominated in Dai, as users levered up their ETH holdings.

  * We're hiring full stack developers in SF. No crypto experience necessary. If interested, shoot us an email ([nadav@dharma.io](mailto:nadav@dharma.io) or [brendan@dharma.io](mailto:brendan@dharma.io)) or [apply here](http://email.mg2.substack.com/c/eJwlUMtuhDAM_BpyK8IBNuGQQ7vt_gbKw0C6IUF5dMXfNyskW7Jle8YzWmZcQzzFEVImJWGcrREAcIOBGDEY4CMnNs1LRNyldSLHguQoylktsw3-vT9OPdkE0J4CQ30D0DhOi1KMM6Ymxqnqp4mRN8csi7HoNQr8w3gGj8SJLecjNf1nQx81pF_RtTrU0mwy7vLDSZVq9xtUIlbQDqaup7zjNccW2o5-3eFxHzn_Hn4oQDN0-0rbVFTKUj8r1E6iUBG9kb4OL9TWhuujfB4oPL6Sw5wxknyZUTXO9XIv3uZzRi-VQyOuk6p5oFUXqRwmVF-8OGIIS1heIT7_AW5hckU)

 **Lazar from MARKET Protocol**

 _MARKET Protocol is a framework for creating tokens that track prices of
traditional or digital assets._

  * Added variable fee structure to solidity contracts

  * Completed user account administration

  * Bug fixes and backend infrastructure clean up

  * Fixed email service integration with MPX and our website

  * Updated privacy policy and terms & conditions on our website

 **Robert from Compound**

 _Compound is a money market protocol on the Ethereum blockchain — allowing
individuals, institutions, and applications to frictionlessly earn interest on
or borrow cryptographic assets without having to negotiate with a counterparty
or peer._

  * Deployed Compound v2 to Rinkeby testnet

  * [Announced](https://medium.com/compound-finance/testing-compound-v2-ace7184a0b4f) testing instructions

 **Rahul from 0x**

 _0x_  is an open protocol that enables the peer-to-peer exchange of assets on
the Ethereum blockchain.

  * [0x Roadmap 2019 part 4](https://blog.0xproject.com/0x-roadmap-2019-part-4-proposal-for-stake-based-liquidity-incentive-52c16558df29): Proposal for Stake-based Liquidity Incentives

  * Detailed economic analysis [here](https://forum.0x.org/t/research-on-protocol-fees-and-liquidity-incentives/340); our R&D lead Peter explaining the proposal [here](https://www.youtube.com/watch?v=s2wlzlQxd5E&feature=youtu.be)

  * [Reddit AMA](https://www.reddit.com/r/0xProject/comments/bc2vhe/zeip31_ama_new_0x_network_economics_monday_11am/) going through community questions and concerns

 **Tony from Liquidity.Network**

 _Liquidity Network is a transfer and swap platform for any token_

  * Liquidity Network open-sources NOCUST smart contract at <https://github.com/liquidity-network/nocust-contracts-solidity>. 

  * Please report bugs or errors if any to our Telegram Developer group <https://t.me/liquiditydevelopers>. We will reward you with your findings. 

 **Dong Mo from Celer**

 _Celer Network is a layer-2 scaling platform that enables fast, easy and
secure off-chain transactions for not only payment transactions, but also
generalized off-chain smart contracts._

  * We finished CelerX Javascript SDK for solo game developers and the first CelerX platform-compatible game. 

  * We are preparing for CelerX game internal release and are doing some advanced UI research from our users. 

  * Testing CelerX and fixing bugs for upcoming Private Alpha release.

  * We enhanced the scalability of the boolean pay flow. 

  * Code and process improvements for Celer backend deployments.

 **Alexandra from Parity Technologies**

 _Parity  Technologies builds core blockchain infrastructure, from Parity
Ethereum, an Ethereum client, to Polkadot, an interoperable blockchain
network._

  * LIVE: The [v0.3-beta version of Parity Fether](https://medium.com/paritytech/parity-fether-is-on-ethereum-mainnet-105ed0c7b491), a decentralized light-client based wallet, is live on Ethereum mainnet. 

  * There's a few tickets left for the first ever Substrate developer conference, happening in Berlin April 24-25. [Apply to attend.](https://twitter.com/ParityTech/status/1113482748784709632)

  * "How to build your own blockchain using Parity Substrate" guide is on [Hacker Noon](https://hackernoon.com/build-your-blockchain-with-parity-substrate-a8ddc4872ed7). 

  * Polkadot researcher Alistair Stewart did a whiteboard video on [how Polkadot works](https://www.youtube.com/watch?v=xBfC6uTjvbM&feature=youtu.be).

  * Web3 Summit 2019 [dates announced](https://twitter.com/web3summit/status/1116281885494136832).

  * Polkadot whitepaper was [translated to Japanese](https://github.com/stakedtechnologies/PolkadotWP/blob/to-pdf/pdf/wp.pdf). 

  * [Substrate Collectables workshop](https://shawntabrizi.github.io/substrate-collectables-workshop/#/) is now in Chinese. 

  * New guide: [How to become a validator on Polkadot](https://twitter.com/ParityTech/status/1115155205233041408).

  * Interested in building on Polkadot? The Web3 Foundation is [providing grants.](https://www.parity.io/jobs/)

  * Lots of [new jobs up](https://www.parity.io/jobs/). 

 **Wes from Theta**

 _Theta is an end-to-end infrastructure for decentralized video streaming._

  * Released Pre-Guardian Node client, an early onboarding tool ahead of Theta’s Guardian Node functionality coming in Q3 2019

  * Support for Trezor wallet for Theta mainnet at command-line interface level

  * Introduced new algorithm for peer to peer stream sharing for sub-optimal networking conditions 

 **Doug from Livepeer**

 _Livepeer is a decentralized video infrastructure network, dramatically
reducing prices for developers and businesses building video streaming
applications at scale.  _

  * Streamflow development continues, this week with a full specification for the [probabilistic micropayments implementation](https://github.com/livepeer/wiki/blob/23f48f14679e0ba9e89efe4322cf95bd0244fdb4/spec/streamflow/pm.md).

  * Network staking participation [surpassed 35%](https://scout.cool/livepeer/mainnet). 

 **Bowen from Hydro/DDEX.io**

 _Hydro  Protocol is an open source framework for building Decentralized
Exchanges. DDEX is the first decentralized exchange for Ethereum and ERC-20
tokens built on the Hydro Protocol. _

  * 6 ways to build on Hydro SDK  <https://medium.com/hydro-protocol/6-ways-to-build-on-hydro-protocol-today-850becd165b>

  * Hydro Protocol SDK 1.1 Road map - Wallet API, Admin portal API. 

  * "Defi The World" Meetup with MakerDao and DOS in Beijing 4/15 - Invite only 

 **Sam from OpenBazaar**

 _OpenBazaar is an open source project developing a protocol for e-commerce
transactions in a fully decentralized marketplace._

  * The 2.3.3 release candidate, and hopefully full release, will be published this week. This includes an IPFS rebase and changes to routing, which will improve speed significantly.

  * Haven app work continues and is undergoing internal testing before the open beta testing.

  * The code to improve precision on the server side for Ethereum integration is completed and being reviewed now.

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

