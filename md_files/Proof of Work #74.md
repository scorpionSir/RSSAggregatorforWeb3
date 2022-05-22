[![](https://substackcdn.com/image/fetch/w_96,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F37b09348-f4f1-47a2-b9e0-a2007299e6e4_256x256)](https://proofofwork.news)

# [Proof of Work](https://proofofwork.news)

SubscribeSign in

Share this post

Proof of Work #74

proofofwork.news

Copy link

Twitter

Facebook

Email

# Proof of Work #74

### Don't call it a comeback

[Eric Meltzer](https://substack.com/profile/138320-eric-meltzer)

Sep 20, 2019

[Share](javascript:void\(0\))

Hi! Proof of Work is back!

We’ve been on hiatus for quite a while, while I learned how to juggle having
an ([extremely adorable](https://imgur.com/a/aBxJmmL)) 6 month old baby with
doing literally anything else at all. I feel very grateful to all the projects
have been loyally updating every single week during this time, and have
permanently decentralized PoW to eliminate myself as a SPoF.

There's a famous saying in property law that "possession is 9/10ths of the
law.” Unfortunately in the (increasingly omnipresent) digital world there's no
such thing as objectively verifiable possession—unlike in the physical world,
where our eyes suffice to determine who is in possession of something. Instead
ones "ownership" of a currency balance or digital object is granted purely at
the pleasure of whoever is running the system; Blizzard, in World of Warcraft,
or Paypal for eBay sellers. This form of "ownership" is far weaker than
possession of a physical object, but until fairly recently there's been no way
to establish a consensus that doesn't rely on a single trusted party to
determine who possesses what. This lack of real possession puts a low ceiling
on how valuable digital assets can be; their very existence depends on a
centralized party that might misbehave, or more commonly, simply disappear.

[Distributed consensus](http://www.michaelnielsen.org/ddi/how-the-bitcoin-
protocol-actually-works/) (which is what blockchains, Bitcoin etc. get us)
create the possibility of possessing digital property in an objectively
verifiable way. They create a set of rules that everyone in the system agrees
on to determine who owns what, with no privileged “superuser” that can change
that ledger and “repossess” assets without the consent of the owner. Indeed,
saying that they grant us a kind of **vision** or new sense by which we can
apprehend ownership in the digital realm is not at all off-base.

This kind of immutable, uncensorable, difficult-to-confiscate digital
ownership is a huge enabler of individual liberty, because it allows an
individual to own something without worrying that they will be judged unworthy
of that privilege by some more powerful party. Individual liberty itself is
something that I care about at an axiomatic level, but it's worth caring about
even if you have more communitarian values because societal evolution is
driven by small groups of enlightened individuals who work to push their
thinking into the larger group. Moxie Marlinspike [wrote
brilliantly](https://moxie.org/blog/we-should-all-have-something-to-hide/)
about why privacy is also a necessary enabler of this effect, and real
ownership in the digital world is likewise necessary to enable individuals to
resist the immense coercive power of the state.

I’ve touched before in this newsletter on why everyone should care about the
individual’s ability to resist state power, but I’ll reiterate briefly for
those who are just joining us. In a word, states have shown themselves to be
extremely willing to use their power over the financial system (power which is
increased to omnipotence in a centralized digital money world) to abuse
individual rights. We see this recently with “civil forfeiture” law where
local police departments steal (and it really is stealing, I’m unwilling to
use any euphemism here) cash from people with no due process at all, and we
saw it on a horrifying scale during the Holocaust, where the Austrian and
German state apparatuses were mobilized to steal billions of dollars from
Jews, before systematically exterminating them. The Holocaust itself was in
fact very much a financially motivated event, and making it more difficult for
states to take money from individuals is a useful tactic in the fight against
future genocides.

In a world where we don’t have objectively verifiable digital possession via
crypto, the move from a cash-based to a centralized digital-money based
economy is a massive setback for individual freedom. Interestingly, a world in
which we **do** have cryptocurrency is actually even more freedom-preserving
than cash, since its a lot harder to take someone’s Bitcoin from them than it
is to take their cash (indeed, harder to even prove they have any Bitcoin).

As the cryptocurrency space matures, we’ll have highly robust systems that can
be used to quickly and at scale establish who is who, who owns what, and who
wants to pay whom—that’s exactly what everyone featured in this newsletter is
working on a piece of.

I don’t have space to go into each piece of this puzzle in detail right now
(Substack is already helpfully telling me that it’s too long for most email
clients) but over the next few issues I’ll be giving an overview of each
project in the intro of the newsletter.

The first is Handshake, a project aiming to enable robust identity online by
creating a decentralized alternative namespace for (primarily) domain names.
Without going into excessive detail, the way the current domain name system
works is appalling from both a governance and security standpoint—a single
centralized entity (ICANN) decides what TLDs (.com, .org. etc) will be allowed
to exist, and a large set of trusted (but in some cases [VERY
untrustworthy](https://www.zdnet.com/article/google-builds-list-of-untrusted-
digital-certificate-suppliers/)) certificate authorities manage the
infrastructure that assures your browser that the website it is browsing is
actually the real (e.g.) google.com. ICANN, despite token efforts to the
contrary, is mostly captured by US interests, and domains which the [USG
doesn’t like](https://www.eff.org/deeplinks/2012/05/unsealed-court-records-
confirm-riaa-delays-were-behind-year-long-seizure-hip-hop) have in the past
been seized from their rightful owners via legal action against registrars.

What Handshake does is move the root of trust from ICANN to a blockchain (one
which is very similar to Bitcoin in terms of its consensus rules), and uses an
on-chain auction process to allow anyone to register a TLD that they wish to
use. In practice this means that instead of me registering ericmeltzer.com
(not actually mine, haha) and essentially having the right to rent
“ericmeltzer” from Verisign in perpetuity, or until some random 3 letter
agency decides they don’t like something I put up, I can register the .meltzer
TLD on handshake, and direct a nameserver to point eric.meltzer to whatever
site I choose. Put very simply, this brings Bitcoin’s “objectively verifiable
possession” model to names! So now, instead of bouncing from registrar to
registrar with the hellhounds of Elsevier hot on their heels,
[Scihub](https://en.wikipedia.org/wiki/Sci-Hub) can simply register a domain
on Handshake and have a permanently unseizable address for their service.

Why this is exciting from an “internet person” perspective should be obvious;
unseizable domains, and also a massive opening-up of the namespace itself. I
can’t wait to see who gets farts.poop first, and there are a couple of other
goofy ones I won’t even mention here because I don’t want to get sniped. From
an investor perspective my excitement mostly stems from the fact that domain
names in aggregate are currently more valuable than all cryptocurrencies
combined, so a more difficult to seize implementation of the naming system is
very cool. Finally, with my crypto-person hat on, the Handshake system will
also be very easy to use as a human-readable crypto addressing system! So if I
register “eric/” on Handshake, I can then put a TXT record with my Bitcoin
address, and people with compatible wallets can simply send Bitcoin to “eric”
instead of a long human-unreadable address. This same logic can of course be
followed for naming on any kind of system one might conceive of, from social
networks to gaming. If this has piqued your interest and you’d like to read
more about Handshake, there’s a [fantastic article
here](https://www.namebase.io/blog/meet-handshake-decentralizing-dns-to-
improve-the-security-of-the-internet).

More next week on Tuesday, and again after that. Thanks for reading! Please
bear with me while we shake the dust off this puppy—some updates are a bit
late, and other teams didn’t make it in this week. Things will be back to
normal in an issue or two.

#### Bitcoin & Friends

 **[Optech](https://bitcoinops.org/en/newsletters/) on Bitcoin [ed: sign up
for their [newsletter](https://bitcoinops.org/en/newsletters/) too! it’s
great!]**

  * If the first send of a transaction doesn’t result in reasonably fast confirmation, the wallet will rebroadcast the transaction to ensure it is relayed to miners. However, this is the only time full nodes do this, so spy nodes can assume any node rebroadcasting a transaction is operated by the user who created that transaction. Amiti Uttarwar’s [proposed solution](https://diyhpl.us/wiki/transcripts/scalingbitcoin/tel-aviv-2019/edgedevplusplus/rebroadcasting/) is having the node treat all transactions the same, rebroadcasting any of them when a heuristic indicates they should’ve been mined recently but weren’t. First PR from Uttarwar implementing this [here](https://github.com/bitcoin/bitcoin/issues/16698).

  * [Blockchain design patterns: Layers and scaling approaches](https://diyhpl.us/wiki/transcripts/scalingbitcoin/tel-aviv-2019/edgedevplusplus/blockchain-design-patterns/) by Andrew Poelstra and David Vorick briefly describes a long list of existing and proposed technologies for making effective use of a space-limited block chain. [ _ed: very much worth a read!]_

  * Olympus: [Lightning enabled fiat onramp](https://medium.com/@JimmyMow/announcing-olympus-lightning-enabled-fiat-ramps-by-zap-1f5349a96ee9). Very cool. 

**JZ from Decred**

 _Decred  is an autonomous digital currency with a hybrid consensus system. It
is built to be a self-ruling currency where everyone can vote on the rules and
project-level decision making proportionately to their stake._

  * First things first, it's finally happened, we have released the initial cut of the Decred privacy implementation. [Jake has provided a thorough rundown of what it is and where we plan on taking things going forward.](https://blog.decred.org/2019/08/28/Iterating-Privacy/) For those who rather listen to him talk about it live he'll be in [San Francisco on Sept. 24 at the Decred Devs meetup](https://www.meetup.com/San-Francisco-Decred-Meetup/events/264917644/) hosted by Coinbase Custody discussing all the details.

  * If you can't make it we also recorded an [episode of the Decred in Depth podcast ](https://soundcloud.com/decredindepth/jake-yocom-piatt-dcr-privacy)on the topic.

  * As an added bonus, rapper [GhostWridah put together something we call "Decred Privacy Flow"](https://soundcloud.com/decredindepth/privacy-flow/s-5ifuN) to help us commemorate the release. That's just how we roll.

  * We're also happy to announce that [Exodus has added Decred support to their mobile offering](https://www.exodus.io/decred-wallet) in addition to their fantastic desktop wallet.

  * [Trust Wallet has also honored us with Decred support.](https://trustwallet.com/decred-wallet) Their mobile wallet leverages the work we did on [Trezor Blockbook integration](https://blockbook.decred.org:9161/) for the backend.  
For a further recap of what we've been working on, do check out the [August
edition of the Decred Journal](https://medium.com/decred/decred-journal-
august-2019-43626ee68ff). Among the very exciting events that took place
recently is the successful Politeia funding of the [Decred DEX, and the
subsequent release of the preliminary design
spec](https://github.com/decred/dcrdex/tree/master/spec).  

 **James from Summa**  
 _Summa builds tools to exchange crypto in a convenient and trustless
fashion_.

  * We released v2.0.0 of bitcoin-spv, featuring a new interface, >30% gas savings, and a branch for a new experimental cross-chain relay :)

  * We're launching Cross-Chain Group with our friends at Keep to standardize developement and interoperability across chains. Get involved at https://crosschain.group/

  
 **Aviv from Spacemesh**  
 _Spacemesh is a programmable cryptocurrency powered by a novel proof-of-
space-time consensus protocol._

  * [Spacemesh Protocol Paper V1.0 released](https://spacemesh.io/spacemesh-protocol-v1-0/)

  * Fixes and improvements in the desktop app (wallet + fullnode) after 2 rounds of reviews and QA, moving forward to full integration with node. [Fixed bugs](https://github.com/spacemeshos/smapp/issues/174)

  * Implemented a safe node shutdown in the Go fullnode implementation

  * Added fetch queue to avoid double requests on same data when syncing

  * Added some fixes and memory optimizations to the Hare Protocol ([Merged issues](https://github.com/spacemeshos/go-spacemesh/pulls?q=is%3Apr+is%3Aclosed))

  * We are continuing to stabilize the codebase for the Spacemesh Virtual Machine before moving towards the next milestone, which is a standalone smart contracts vm based on wasmer with fixed storage / no gas metering.

 **Izaak from Coda**

 _Coda is the first cryptocurrency protocol with a constant-sized blockchain.
Coda compresses the entire blockchain into a tiny snapshot the size of a few
tweets using recursive zk-SNARKs._

  * Deepthi improved [error handling](https://github.com/CodaProtocol/coda/pull/3385) for invalid blocks which were causing issues on our last testnet.

  * I (Izaak) made [two](https://github.com/CodaProtocol/coda/pull/3410/files) [PRs](https://github.com/CodaProtocol/coda/pull/3413/files) implementing the super-efficient Rescue hash function. Preliminary benchmarks show it should speed up one of our SNARKs by 8-10x.

  * Jiawei added [profiling](https://github.com/CodaProtocol/coda/pull/3382) for bootstrapping and catching up after a reorg or long disconnect from the network.

#### Privacy coins

 **Daniel from Grin**

 _Grin is a community-driven implementation of the Mimblewimble protocol that
aims to be privacy preserving, scalable, fair, and minimal._

  * Merged PRs: [3 in /grin](https://github.com/mimblewimble/grin/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A2019-07-15..2019-07-21+) | [1 in /grin-wallet](https://github.com/mimblewimble/grin-wallet/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A2019-07-15..2019-07-21+) | 4 unique contributors

  * Grin hard forked to v2.0.0 [unremarkably](https://www.grin-forum.org/t/yeastplume-progress-update-thread-mar-19-to-sep-19/4303/32), which was in other words a great success.

  * Last week's [governance meeting](https://github.com/mimblewimble/grin-pm/blob/master/notes/20190716-meeting-governance.md) adopted the RFC process, the sub-teams proposal, and had updates on website redesign and security audit.

  * [Slides from last week's London Meetup](https://github.com/mimblewimble/grin-pm/blob/master/presentations/meetups/20190716-GrinLondon-Meetup4-Lehnberg.pdf) are up, covering a general update of Grin, six months after mainnet launch, and the new governance process.

  * David Vorick announced that Obelisk [has cancelled their GRN1 ASIC miner](https://www.grin-forum.org/t/grn1-cancellation-announcement/5624).

  * @nijynot announced the first release of his [Wimble wallet](https://github.com/nijynot/wimble) for Grin.

  * Grin was on [Token Talks podcast](https://podcasts.apple.com/us/podcast/grin-global-digital-cash/id1362129613?i=1000444595544).

  * First Grin [iOS <-> Android transaction](https://twitter.com/i1skn/status/1152986124937302016?s=12) using the Ironbelly wallet.

  * More Grin info [here](https://grinnews.substack.com/).

 **Beni from Beam**

 _Beam is a confidential and scalable cryptocurrency based on Mimblewimble._

  * We have released our [New Ambassador Program](https://medium.com/beam-mw/beam-revamped-ambassador-program-4ba4a06e2662)

  * Ready to release [Clear Cathode 3.1 Android](https://github.com/BeamMW/android-wallet/releases/tag/Testnet-3.1)

  * Good progress on [Clear Cathode 3.2 Desktop](https://github.com/BeamMW/beam/projects/20)

  * [Trezor Wallet] HW wallet integration [#624](https://github.com/BeamMW/beam/issues/624)

  * [Desktop Wallet] Add texts that elaborate online time (Send/receive time) [#853](https://github.com/BeamMW/beam/issues/853)

  * [Desktop Wallet] Add ability to list swap transactions in desktop wallet [#761](https://github.com/BeamMW/beam/issues/761)

 **Arnaud from AZTEC Protocol**

 _AZTEC Protocol is an efficient zero-knowledge protocol built on top of
Ethereum, making plug-and-play value transmission and asset governance privacy
tools for developers and companies.  _

  * This week, optimisations, clean-up, and merging outstanding PRs. We’re adding the finishing touches before last audit, and MPC.

  * We’ve also been [working on Huff](https://github.com/AztecProtocol/AZTEC/pull/203) recently, refactoring the compiler and adding better errors.

  * The team will be at ETHIndia (we’re sponsoring a prize if you want to get your hands dirty with AZTEC). Do say hi!

  * Last week we hosted ZK-LDN0x03, with a talk by Rami from Liquidity network, and Olivier from Hopper. The event was recorded and will be available on the [ZK-LDN youtube channel](https://www.youtube.com/playlist?list=PLPBfQd03L-pFySKSRNpPNjp6MaZzcpCXz).

  * We are always hiring for **Solidity Engineers** and **Senior Engineers**. You can apply [here](http://email.mg2.substack.com/c/eJwlUEuOwyAMPU3ZNSKQpGHBoq1mrhHxcVumBEfgTJU5_RBF8sKy_fw-zhA8MW96wUJsLZCn4LVQgg8t87rz7diPLJTpkQFmE6KmvAJbVhuDMxQw7fe9kuylwUnVg3RcXQYu7eDAenvpjOx5Lweh2M4xmdUHSA40_ELeMAGL-kW0lJO8nsR3LZOeEBuHe_tH4M5LRkKH8Szr6AdtYUEL3iouRcs7LjvRtM2NX-_jnY-3QbS37ut66vj8FE1ZbSHj3vXfzLI2OVUBdecy-EBzSNQEPJTRtoBO8CkRiCAzOkKpXqcKntcUaJsgGRvB6wNSvUt1kQOrNB5rPklXsfjAxwfz-x-f0nXk), or by emailing [arnaud@aztecprotocol.com](mailto:arnaud@aztecprotocol.com) with the name of the role you see yourself filling as the subject.

#### Smart contracting platforms

 **Evan from[Ethereum](https://weekinethereumnews.com/)**

 _Ethereum  is a decentralized platform for applications that aims to resist
fraud, censorship or third-party interference._

  * Interop week is over, but the results are spectacular: [seven Eth2 clients talking to each other](https://twitter.com/JonnyRhea/status/1172233598109442049). This was the last major hurdle before clients focus on optimizations, auditing, and UX in preparation for launch.

 **Peter from NEAR**

 _NEAR is a sharded proof-of-stake blockchain._

  * 61 PRs merged or created across ][ repos by 20 authors! Featured repos: [nearcore](https://github.com/nearprotocol/nearcore), [nearlib](https://github.com/nearprotocol/nearlib), [near-shell](https://github.com/nearprotocol/near-shell/), [near-wallet](https://github.com/nearprotocol/near-wallet), [near-bindgen](https://github.com/nearprotocol/near-bindgen), and [borsh](https://github.com/nearprotocol/borsh).

  * Shipped nearlib 0.13.3

  * System Runtime API [implemented](https://github.com/nearprotocol/nearcore/pull/1268)

  * Contract reward added to core

  * Now can query block by hash, [not just index](https://github.com/nearprotocol/nearcore/pull/1300) in core

  * Continuing refactor in near-runtime-ts

  * Tests for invalid input added to BORSH

  * [Batch transactions](https://github.com/nearprotocol/NEPs/pull/8) in progress

 **Topper from Quorum Control**

 _Quorum Control makes Tupelo, a permissionless proof of stake DLT platform
purpose-built to model individual objects that enables flexible public or
private data models._

  *  **[Major Release](https://github.com/QuorumControl/tupelo-wasm-sdk): **Released a new web assembly sdk allowing developers to build applications that connect directly to the Tupelo network from multiple development platforms (like web pages) without needing to proxy through an rpc server or running a full node. Read the [documentation here](https://github.com/QuorumControl/tupelo-wasm-sdk).

  * Published an article describing how [Tupelo relates to IPLD](https://medium.com/@tobowers/under-the-hood-tupelo-uses-ipld-libp2p-and-it-also-makes-use-of-bitswap-2d8007ba664c) and [Presented Tupelo on the Protocol Labs IPFS call](https://www.quorumcontrol.com/blog/2019/9/5/protocollabs-ipfs) highlighting the most exciting work in the community at large.  

  * Ongoing optimization of production Tupelo TestNets including new dedicated game TestNet.

 **Andrew from Solana**

 _Solana is a scalable blockchain that utilizes proof of history to verify the
ordering and passage of time between events. It consists of a network of 200
physically distinct nodes which support a sustained throughput of more than
50,000 TPS.  _

  * Great response to our [Tour del SOL](http://solana.com/tds), or Solana’s validation-client competition. We are about to kick it off! Good luck to everyone in the event (round 2 signups will be in a few weeks).

  * We just [published a blog post on Replicators](https://medium.com/solana-labs/turbine-solanas-block-propagation-protocol-solves-the-scalability-trilemma-2ddba46a51dbhttps://medium.com/solana-labs/replicators-solanas-solution-to-petabytes-of-blockchain-data-storage-ef79db053fa1) — Solana’s Solution to Petabytes of Blockchain Data Storage. It is one of our seven key innovations that make the Solana network possible. 

  * We are [hiring a few key developers](https://solana.com/careers), especially in Rust. Intros welcome! 

  * We are looking at our conference schedule for the fall. Going to something that looks amazing? Let us know. [andrew@solana.com](mailto:andrew@solana.com)

 **Michael from Loom**

 _Loom Network is a platform for building highly scalable DPoS sidechains to
Ethereum, with a focus on large-scale games and social apps._

  * [Launched Binance Chain integration](https://medium.com/loom-network/loom-plasmachain-loom-wallet-are-now-interoperable-with-binance-chain-bringing-an-erc20-bep2-bridge-509e6b202b91) with Loom, bringing an ERC20 <–> BEP2 bridge and smart contract functionality to Binance

  * [​](https://loomx.io/developers/en/deposit-and-withdraw-trx.html)Over 238M tokens have been staked on Loom, which amounts to ~30% of circulating supply

  * [Launched Binance Chain + Loom integration](https://medium.com/loom-network/loom-plasmachain-loom-wallet-are-now-interoperable-with-binance-chain-bringing-an-erc20-bep2-bridge-509e6b202b91), bringing an ERC20 <\--> BEP2 bridge and smart contract functionality to Binance

  * Released early preview of our Binance Chain integration with [a new developer guide](https://loomx.io/developers/en/deposit-and-withdraw-bnb.html) showing how to take BNB payments from directly within your dapp

  * Announced [multichain DeFi on Loom](https://medium.com/loom-network/enabling-the-next-generation-of-decentralized-finance-with-multichain-collateralized-assets-c6008028f041%E2%80%8B), including plans to integrate BTC, Binance Chain, and others

  * [Alice.finance launches](https://twitter.com/loomnetwork/status/1149355210202107904) and becomes the 1st DeFi project live on Loom

  * [Completed security audit](https://medium.com/loom-network/loom-plasmachain-completes-third-party-security-audit-and-is-now-open-source-25f2d597ee2c) by Trail of Bits and open sourced PlasmaChain mainnet

  * Released new developer tutorial on [How to Deploy Your Dapp to Loom PlasmaChain Mainnet](https://youtu.be/ltFc6wCdZ5w)

  * Released [major update for Relentless](https://medium.com/relentlesstcg/major-updates-new-emblem-new-characters-and-new-features-36d1f977f65e) including new artwork, characters, revamped interfaces, in-game pack rewards[​](https://medium.com/relentlesstcg/major-updates-new-emblem-new-characters-and-new-features-36d1f977f65e), in-game purchasing, and in-game pack opening

 **Myles from EOS**

 _EOS is a new blockchain architecture designed to enable vertical and
horizontal scaling of decentralized applications._

  * [EOSIO 1.8.0](https://medium.com/@eosio/eosio-version-1-8-0-stable-release-of-consensus-protocol-upgrade-features-eosio-8c168d95437a) stable release candidate from [Block.one](http://block.one/) published 

  * BPs agreed through an [on-chain vote](https://eosauthority.com/when1.8/) for a coordinated hard fork on September 23, 2019 

  * [Equilibrium](https://eosdt.com/), a MakerDAO-like stablecoin on EOS, is officially live 

  * dfuse announced a [set of tools](https://www.dfuse.io/en/blog/transition-seamlessly-to-eosio-1.8-with-dfuse) to help dApps seamlessly transition to EOSIO 1.8.0 

  * EOS is [now supported](https://medium.com/eos-cafe-block/trezor-is-now-available-for-eos-on-bloks-io-1670ca3be76f) on Trezor 

  * [EOSfinex](https://www.eosfinex.com/) [announced](https://medium.com/eosfinexproject/eosfinex-extends-launch-to-july-30th-7a4947ad5f4) that it will launch on July 30th

  * eosDAC introduced [DAC Factory](https://steemit.com/eosio/@eosdac/introducing-eosdac-dac-factory), a hosted DAC/DAO creation service

  * A new stable release of [EOSIO 1.8.0](https://medium.com/eosio/eosio-version-1-8-0-stable-release-of-consensus-protocol-upgrade-features-eosio-8c168d95437a) was released by B1

 **Kate and Dean from Agoric**

 _Founded by pioneers in secure development and distributed systems, Agoric
uses a secure subset of JavaScript to enable object capabilities and smart
contracts._

  * We hosted a very successful token design workshop last weekend. A big thanks to all of the guests willing to share their knowledge.

  * We analyzed performance issues on our testnet and came up with [some concrete solutions](https://github.com/Agoric/SwingSet/issues/94). 

  * We designed and documented a [new SwingSet kernel API](https://github.com/Agoric/SwingSet/issues/88).

  * Mark, Dean, and Aaron Davis (kumavis) from Metamask presented at TC39 (the JavaScript standards committee) on [SES](https://github.com/Agoric/SES), [sesify,](https://github.com/MetaMask/sesify) and "[infix bang](https://github.com/Agoric/proposal-infix-bang/)", i.e., distributed object programming in js with promise pipelining.

#### Financial Infrastructure

 **Antonio from dYdX**

 _dYdX is a decentralized exchange for margin trading, borrowing, lending, and
eventually derivatives. dYdX allows traders to trustlessly short and get
leverage on crypto assets._

  * Launched [native ETH-DAI market](https://medium.com/dydxderivatives/dydx-launches-native-eth-dai-market-30ced19701ae) complete with limit orders!

  * Working on adding isolated positions to native ETH-DAI market

  * Onboarding market makers to native ETH-DAI market. Check out our newly released [Python](https://docs.dydx.exchange/#/python) and [TypeScript](https://docs.dydx.exchange/#/typescript) clients to get started building a trading bot!

  * [Hiring](https://dydx.exchange/careers/) software engineers & product designers full-time in SF!

 **Brendan from Dharma**

 _Dharma is the easiest place to borrow and lend cryptocurrencies. It enables
non-custodial peer-to-peer lending through smart contracts on Ethereum._

  * We brought on a Senior Engineer and a Full Stack Engineer!

  * Began working on revamped lending architecture

  * Settling up with many of our liquidators who helped keep the Dharma system secure during ETH's recent price fall

  * We're hiring a [Lead Protocol Engineer](https://boards.greenhouse.io/dharma/jobs/4358538002)! all smart contract architects are welcome

 **Coulter from MakerDAO**

 _Maker is comprised of a decentralized stablecoin, collateral loans, and
community governance._

  * Two critical elements of the Maker Protocol are Auctions and Keepers. We [introduced documentation](https://blog.makerdao.com/introduction-to-auctions-and-keepers-in-mcd/) for those that want a deep dive into both. 

**Robert from Compound**

 _Compound is a money market protocol on the Ethereum blockchain — allowing
individuals, institutions, and applications to frictionlessly earn interest on
or borrow cryptographic assets without having to negotiate with a counterparty
or peer._

  * Supply increased to $100 million, setting a new milestone for the protocol

  * Experimental [announced](https://twitter.com/lbertenasco/status/1150850753260662784) a Compound lending proxy, for developers building stake-to-play, stake-to-buy, and stake-to-X dapps.

  * WBTC was added to the protocol

  * Bitgo [added support for cTokens](https://blog.bitgo.com/july-tokens-update-b87a94db3a1e); now, users can earn interest from the Compound protocol while their balance is stored at one of world’s most trusted custodians.

  * Friday, we also unveiled our new [brand](https://medium.com/compound-finance/meet-compound-300a3bc224f1)

  * [ERC-2212: Earning Interest Stakes](https://github.com/ethereum/EIPs/issues/2212) was introduced

  * [Pooled cDAI library](https://github.com/ZeframLou/pooled-cdai) was released by community developers

#### Layer two and interoperability

 **Tieshun from Namebase (with Handshake updates)**

 _Namebase is the easiest way to buy, sell, and use Handshake._

  * Namebase launched their new private beta to test their name registrar, onramp, and pro exchange for Handshake. Join the waitlist at [namebase.io](http://namebase.io)

  * Handshake community ambassadors are hosting meetups in LA, Nebraska, and Australia. Sign up for your local meetup or [join the ambassador community](https://forms.gle/RgxNv1f7SRaxzHME6) for the latest community updates on Handshake

 **Alexandra from Polkadot**

 _[Polkadot](https://polkadot.network/) empowers blockchain networks to work
together under the protection of shared security._

  * [Kusama](https://kusama.network/), an early network for developers to run their craziest Polkadot experiments before mainnet, [was announced](https://twitter.com/polkadotnetwork/status/1151170947048546305).

  * [Coindesk covered Kusama.](https://twitter.com/coindesk/status/1151167943365013510)

  * Limited seats left for the second annual Polkadot dev intensive: [DOTcon](https://twitter.com/polkadotnetwork/status/1149705455318364160) (right before [Web3 Summit](https://web3summit.com/)).

  * Plasma on Polkadot? Some community members are [discussing](https://twitter.com/WatanabeSota/status/1155732964996575232). 

  * Web3 Foundation is[ providing grants to build the Web3 ecosystem](https://github.com/w3f/Web3-collaboration/blob/master/grants/grants.md). 

  * [Job openings at Web3 Foundation](http://web3.bamboohr.com/jobs/): come help build Polkadot.

 **Dong Mo from Celer**

 _Celer Network is a layer-2 scaling platform that enables fast, easy and
secure off-chain transactions for not only payment transactions, but also
generalized off-chain smart contracts._

  * We continued on the integration and testing of new CelerX gaming API layer.

  * We were developing layouts for the new gaming UI and refactoring the local database for payment history.

  * We continued on the integration and testing of new CelerX backend. 

  * We were finalizing the work on Celer Web client and improved the new OSP protocol and multi-OSP routing.

  * We completed SGN staking and withdraw components.

  * We fixed bugs and improved stability.

#### Application infrastructure

 **Alexandra from Parity Technologies**

 _Parity  Technologies builds core blockchain infrastructure, from Parity
Ethereum, an Ethereum client, to Polkadot, an interoperable blockchain
network._

  * [We released new versions of Parity Ethereum, 2.5.8-stable and 2.6.3-beta.](https://twitter.com/ParityTech/status/1173580508510466048) The most noteworthy improvement in this release is the incorporation of all EIPs required for the Istanbul hard fork.

  * Parity Shasper (mostly) [syncs with Lighthouse](https://twitter.com/sorpaas/status/1172350637847326722)!

  * New episode of [Relay Chain podcast](https://twitter.com/RelayChain/status/1172453318003691520): we talk to Deirdre Connolly and Anna Kaplan from Zcash Foundation on the state of the Rust Zcash client, “Zebra,” originally developed by Parity Technologies and now maintained by Zcash Foundation.

  * [Totem](https://twitter.com/ParityTech/status/1172547044449443840) is building a tokenized real-world assets chain with Substrate.

  * Thanks to Polkascan, [any Substrate-based chain will have a block explorer.](https://twitter.com/polkadotnetwork/status/1172459538332692481)

  * Want to come build cool tech for a better web? [We're hiring!](https://www.parity.io/jobs/#jobs)

 **Wes from Theta**

 _Theta is an end-to-end infrastructure for decentralized video streaming._

  * Released [version 1.0.5](https://github.com/thetatoken/theta-protocol-ledger/releases) of Theta node software. Version 1.0.6 will follow shortly

  * Announced a [joint marketing campaign with Brave browser](https://medium.com/theta-network/sliver-tv-theta-network-announces-advertising-partnership-with-brave-browser-9482030c8f40) and Theta/SLIVER.tv, where we’ll be cross-promoting native ads in our respective platforms

  * Full redesign on the SLIVER.tv esports platform launched as “[SLIVER.tv 2.0](https://www.sliver.tv/)”

 **Matt from Keep Network**

 _The Keep Network is a privacy layer for public chains, enabling
interactivity with private data and interoperability across chains. It does
this with keeps, off-chain containers for private data that help smart
contracts harness the full power of the public blockchain._

  *  **tBTC:**

    * We made progress on ACLs between contracts - continuing this work this week

    * We implemented an algorithm for ECDSA signature recovery ID computation

    * Finishing touches on the setup on how we are going to integrate with Uniswap to liquidate tokens

    * We are finishing designs for the v1 redemption dApp

 **Random beacon updates:  **

    * Beacon pricing and staker rewards - made good progress both on the research and implementation, hope to have this work finished this week

    * Misbehaving group member disqualifications during distributed key generation - we have about 80% of misbehavior cases covered, continuing work on that this week, and hope to have it done by Friday

    * For more updates and questions join our [Slack](https://bit.ly/2FMkV6T) and check out the [Keep blog](https://blog.keep.network/).

 **David from Sia**

 _Sia is a decentralized cloud storage platform leveraging blockchain
technology to create a data storage marketplace that is more robust and more
affordable than traditional cloud storage providers._

  * Matt wrote extensive documentation for the renter module. David rearranged old code related to renter compatibility. Marcin made siad show an appropriate error message if the user skips to start up essential modules.

  * Matt published a [roadmap update for 2019](https://blog.sia.tech/sia-roadmap-2019-update-fa5e1baeab39), detailing the next priorities of the development team: clearer financials, support for small files, continuous backups, and an SDK library for developers. For the long term, file sharing and a multi-device file system experience are planned.

  * The whole Sia team hosted an [AMA on Reddit](https://www.reddit.com/r/siacoin/comments/ceji88/ama_with_the_sia_team_on_july_18th_at_noon/)

  * Zach published a [blog post](https://blog.sia.tech/afe6e7412a25) explaining why Sia is today the most viable non-financial blockchain application

  * Discord user @ScottG released [new versions of Repertory and Repertory-UI](https://bitbucket.org/blockstorage/repertory-ui/src/master/). This app allows you to mount Sia storage as a drive on your desktop. This new version corrects multiple bugs and improves the performance on Windows

  * Hoesa released [VLCia](https://github.com/Hoesa/VLCia): a light media player that scans and streams the contents that the user has stored on the Sia network, making the media streaming experience even easier

  * Rezant teased his [upcoming SiaCentral desktop app](https://imgur.com/a/N6bw0aP): a UI dedicated to hosting with features as more detailed financial metrics and notifications when the host goes offline or presents issues

  * Hakkane [released the version 1.1 of Decentralizer](https://medium.com/@salva.enkidu_89587/2cdfe69e8d90), an app for contracts micro-managing that now displays performance scores of hosts allowing for more customized host selection. A guide for this new feature was published

  * Chris fixed a bug reported by some users unable to finish downloads. Destination files are now properly closed at the end of the downloading. He's also working on the fix for a bug that can cause a download to be randomly corrupted. The fix is almost ready, pending on final tests. A hotfix for 1.4.1, fixing these issues, will be released over the next days.

  * Continuing the work on improving the documentation of the Sia component, Chris and David wrote extensive documentation for the siafiles. These are the small files created when a renter uploads a file, and contains the minimal information required for their download: some metadata, the public keys of the hosts storing the file and the list of file chunks. Chris worked also on the partial file uploads feature.

  * Discord user @ScottG released final versions of Repertory and Repertory-UI. This app allows you to mount Sia storage as a drive on your desktop. Compared to the betas published last week, they feature optimizations on memory and CPU usage: [here](https://bitbucket.org/blockstorage/repertory-ui) and [here](https://bitbucket.org/blockstorage/repertory)  

  * [Blocknet integrated the Sia blockchain into their services](https://blocknet.co/blocknet-makes-sia-storage-available-on-the-internet-of-blockchains/), allowing users to interact with their hosted Sia nodes. This can be a useful app for developers that need to interact with multiple blockchains remotely, using Sia as a storage layer

#### Other

 **Sam from OpenBazaar**

 _OpenBazaar is an open source project developing a protocol for e-commerce
transactions in a fully decentralized marketplace._

  * Major news: The [Haven app](https://medium.com/@drwasho/introducing-haven-b16689dd7eaf) is live! Private ecommerce on a mobile device. This is the culmination of two years of development, and this week has been devoted to wrapping up testing and launching the product.

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

