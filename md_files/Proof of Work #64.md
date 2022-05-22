[![](https://substackcdn.com/image/fetch/w_96,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F37b09348-f4f1-47a2-b9e0-a2007299e6e4_256x256)](https://proofofwork.news)

# [Proof of Work](https://proofofwork.news)

SubscribeSign in

Share this post

Proof of Work #64

proofofwork.news

Copy link

Twitter

Facebook

Email

# Proof of Work #64

[Eric Meltzer](https://substack.com/profile/138320-eric-meltzer)

May 1, 2019

[Share](javascript:void\(0\))

Hi from LA!

I’ve been at a small conference for institutional investors and crypto people
to get to know each other better. The simple takeaway so far has been that
institutional adoption is continuing to happen. It’s a slow process that
mostly so far has happened in the form of fund investment—a bunch of
endowments and a couple of pension funds have put decent-sized checks into
crypto focused funds, who are currently deploying that money into a mix of
venture-style bets and buying liquid cryptocurrencies. If you hold BTC, this
seems like a good reason (among many) to just keep holding it—my sense is that
there’s a lot of interest from large institutions, but that they are still
somewhat hampered by a lack of regulated custodians, easy tie-ins to the
tooling they are used to, etc.

Highlights: Decred lightning network goes live on testnet, Grin’s UTXO set
_shrank_ by 15% last week, Loom’s Plasmachain Universal Transaction Signing
allows users to seamlessly interact with L1/L2 txs without having to really
know or care which they are doing, and Decentraland releases cute Avatars.

No update from: Kadena, Spacemesh, Zeppelin, Theta.

#### Bitcoin & Friends

 **Jimmy on Bitcoin**

 **[Optech](https://bitcoinops.org/en/newsletters/) on Bitcoin [ed: sign up
for their newsletter too! it’s great!]**

  * 0.18.0 coming next week, big update then!

 **James from Summa**

 _Summa builds tools to exchange crypto in a convenient and trustless
fashion._

  * This week we are wrapping up our share of development on a major partnership that will significantly improve interoperability between BTC and ETH. More details to come.

  * We were super excited to learn that our friends at [Bolt Labs](http://boltlabs.tech/) are using [riemann](https://github.com/summa-tx/riemann) to prototype private payment channels for Zcash. 

  * Matthew and I will be in NYC from May 10-20 for blockchain week. We would love to meet up. Reach out to us at: team@summa.one, so that we can arrange something

 **JZ from Decred**

 _Decred  is an autonomous digital currency with a hybrid consensus system. It
is built to be a self-ruling currency where everyone can vote on the rules and
project-level decision making proportionately to their stake._

  * Lightning has struck Decred. We're very pleased to announce that our Lightning Network implementation [dcrlnd](https://github.com/decred/dcrlnd) is now live on testnet. It would appear Decred is the first coin that is not based on Bitcoin Core to go live with LN.

  * [Matheus has released a blog post](https://matheusd.com/post/announcing-dcrlnd/) outlining the tremendous development effort that went into the port as well as the sequence of events that will culminate in Lightning becoming usable on mainnet after our stakeholder voted hard fork which is scheduled to activate on May 9th. There's also a slick [video showing LN integrated into our Decrediton GUI wallet](https://www.youtube.com/watch?v=qRUqQAPo0Zs).

  * A new [Politeia vote has just gone live to amend the Decred constitution](https://proposals.decred.org/proposals/fd56bb79e0383f40fc2d92f4473634c59f1aa0abda7aabe29079216202c83114). More specifically to bring it up to date and better describe how the code places ultimate sovereignty in the hands of stakeholders.

 **Johnny from Stellar**

 _Stellar is an open network for sending and exchanging value of any kind. Its
global network enables digitization of assets - from carbon credits to
currencies - and enables movement around the internet with ease._

  * SDF has released a modified Code of Conduct, which can be found [on our website](https://www.stellar.org/community-guidelines/) and [Github](https://github.com/stellar/.github/blob/master/CODE_OF_CONDUCT.md).

  * Stellar Core v11.0.0 has been fully released on SDF nodes, and currently we're waiting on SDK compatibility before coordinating with validators to move to Stellar Protocol 11.

  * [New Go SDK released](https://github.com/stellar/go/releases/tag/horizonclient-v1.0) along with [Horizon 0.17.6](https://github.com/stellar/go/releases/tag/horizon-v0.17.6).

  * 49 Pull Requests merged in across our [Go Monorepo](https://github.com/stellar/go/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A%3E%3D2019-04-22+), [JS SDK](https://github.com/stellar/js-stellar-sdk/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A%3E%3D2019-04-22+) (and [Base](https://github.com/stellar/js-stellar-base/pulls?q=is%3Apr+is%3Amerged+merged%3A%3E%3D2019-04-22)), and [Stellar Core](https://github.com/stellar/stellar-core/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A%3E%3D2019-04-22+).

 **Izaak from Coda**

 _Coda is the first cryptocurrency protocol with a constant-sized blockchain.
Coda compresses the entire blockchain into a tiny snapshot the size of a few
tweets using recursive zk-SNARKs._

  * We have begun development of our zero-knowledge scripting system. Join us on our [Discord](https://discord.gg/wz7zQyc) to get involved.

  * John, Avery, and Brandon have been [developing](https://github.com/CodaProtocol/coda/pull/2292) our [GraphQL](https://github.com/CodaProtocol/coda/pull/2335) backend.

  * Vanishree has been analyzing our new chain selection rule.

  * Jiawei identified an important [consensus bug.](https://github.com/CodaProtocol/coda/pull/2315)

  * After a great effort from John, Paul, and others, versioning types for backwards compatibility is now complete.

#### Privacy coins

 **Paige & Zooko from Zcash**

 _Zcash is a  digital currency utilizing zk-SNARKs to enable its privacy-
protecting properties._

  * Official migration tool + documentation + testing for 2.0.5 release

  * Testing [turnstile enforcement consensus rule](https://z.cash/blog/turnstile-enforcement-against-counterfeiting/) for 2.0.5 release

  * Improving SDK, librustzcash & lightwalletd with help from community feedback

  * Full update: <https://forum.zcashcommunity.com/t/april-26-2019-weekly-update-engineering/33316>

 **Mitchell from Monero**

 _Monero is a open-source, privacy-focused cryptocurrency using the ASIC-
resistant CryptoNote PoW algorithm. It enforces all privacy features at the
protocol level to ensure that all transactions create a single fungible
anonymity pool._

  * Monero had it's Moneroversary this past week. It had a lot of [fun events](https://www.youtube.com/playlist?list=PLsSYUeVwrHBkx9Gqi4HitIEWfQo2sTdti) that went on.

 **Daniel from Grin**

 _Grin is a community-driven implementation of the Mimblewimble protocol that
aims to be privacy preserving, scalable, fair, and minimal._

  * Merged PRs: [10 in /grin](https://github.com/mimblewimble/grin/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A2019-04-22..2019-04-28+) | [4 in /grin-wallet](https://github.com/mimblewimble/grin-wallet/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Amerged+merged%3A2019-04-22..2019-04-28+) | 7 unique contributors

  * For those wondering what this Mimblewimble thing is good for: Grin's UTXO set [shrank by 15% over the past week](https://grin.report/d/xoo9N43iz/chain?orgId=1&fullscreen&panelId=2&from=1554066000000&to=1556398800000).

  * @yeastplume started [work on invoice transaction flow via API](https://github.com/mimblewimble/grin-wallet/pull/90).

  * [Slate compatibility fixes ahead of v1.1.0](https://github.com/mimblewimble/grin-wallet/pull/85), by @bddap and @yeastplume.

  * Peer max count [was increased significantly](https://github.com/mimblewimble/grin/pull/2754) by @ignopeverell.

  * [Income and spending logs were updated](https://github.com/mimblewimble/grin-pm/pull/117) by @lehnberg ahead of the Q1 transparency report.

  * @kargakis [provided a script for easy checking of unaccounted for income](https://github.com/mimblewimble/grin-pm/pull/120) in the income log.

  * [Governance meeting](https://github.com/mimblewimble/grin-pm/blob/master/notes/20190423-meeting-governance.md) discussed reporting, financial logging, supporting 3rd party projects and improving Grin evangelism.

  * @i1skn [gave a Grin intro](https://youtu.be/eUKw-NULpxM) at Crypto Monday in Berlin

  * [1st Grin meetup in Moscow announced](https://www.meetup.com/MimbleWimble-Grin-Moscow/events/260942761/) for May 16

  * More Grin info [here](https://grinnews.substack.com/).

 **Beni from Beam**

 _Beam is a confidential and scalable cryptocurrency based on Mimblewimble._

  * New [Download page](http://email.mg1.substack.com/c/eJwlUEuuwyAMPE3ZNQKS0LJg0VbqNSI-TotegAicotz-kVbywp-xZ8ZWI7xS3hVCQbIVyJN3ijhFL9xeDPFlmjNA0H5RZN3M4q1Gn-KB4oOg5K00WClcD5JR57gRs7iCHG0PdJypZTNZU8FJb85DtKDgA3lPEcii3ohrOfW3E3-2qLV2BnToQm2VSzUuSbvS8sYeI-A5aEu84pRJOnDJhpEx1rHuIfko7vQhb-Ip2VOeBhperCubKajtX2dTIFkZiL5NDoZzqN_mVxjuK6gItSyACJng7xXN69QwYYse9wmiNgs4hXmD31rzP_biKkmjcelQqI7Ta_Yfbfd_XqR1GQ), new [Home page](http://email.mg1.substack.com/c/eJwlkE2OgzAMhU9DdoOSQKBZZNGpxDVQfkwbDQkocYq4_YRW8sb287M_W43w3NKpEDKSkiHN3iniFB25HQ3xeV4SQNB-VWQvZvVWo9_ipeL9QMlLWbkY6KmVzmk5yhsfqASqF7ZY0QlhyL5lnHVxHqIFBW9I5xaBrOqFuOemuzd8qnEcR2tAhzYcNSNeccok7blkvWCMtax9SC6GX_qQ92GSbJJNT8OTtbmYjNr-tXYLJCkD0dfOZfUTjk_xcwGeO6gIR14BERLBL3OFmqsmlOjxnCFqs4JTmAp8xyqo6IabJHWN2-ojorqs9-Tf2p7_es9sPg), enhanced [News Center](http://email.mg1.substack.com/c/eJwlkE2OwyAMhU9TdoOABBoWLDqVco2IH7dFE0gETqPcfkgreWP7-dmfvUV4LuUwCBXJVqFMMRgSDLsKf3Uk1ulRAJKNsyHr5uboLcYlnyrRK0ZeZuiCD96Bl8wqMQghuZcP8EorOYAQZF0qTnYLEbIHA28ox5KBzOaFuNZLd7uIscW-79SBTTTtLUsQoiXRCMY164XmveScU07vWkj1y-76pkbNR33pWXpyWjdX0fo_6pdEinGQY-ucfj9p_xQ_Z-Cxgsmw1xkQoRD8gjeyqWnSliMeE2TrZggGywbfsUYrOzVo0taEpX0jm9N6LfFt_fEPnPpuBA)

  * We still are working on the integration with Trezor T and on the development of our Atomic Swap Feature [#447](http://email.mg1.substack.com/c/eJwlUMmOwyAM_ZpymwgIgXLg0Nluc55jxOI2aBISgWmVvx_SSpb8vD3bz1uE25p3g1CQ1AJ5jMGQYKjiXjkSy3jNAIuNsyFbdXP0FuOaji4uJCWTCQK0Y1Lx4aw1syF4eeZuuHqttOSKk20tONoaIiQPBu6Q9zUBmc2EuJVTfznx72a3iFN1nV-XFryDXX5-G3ANNBdLqVAaEEKRaDhlmgrOmWyo71j3JcSH0vQ8fEoqejqcBF1urCvVFbT-72Al2ThIsVUOzrfl8Uw-j8N9A5PgUWZAhEzwJUf7d2w9S00R9xGSdTMEg7nCa6xpMDBJKWlrwto0Suag3nK8W7__AxPYc7A)

  * We have began to develop a super cool feature that will allow us to translate our GUI&CLI Wallets [#544](http://email.mg1.substack.com/c/eJwlUE2PgyAQ_TVyWwMUtBw4tE287XmPBnBUUkUDQxv__WKbTDJvvt7MPGcQpi0eGiEhyQli7wdNBk1b7lpLfOrHCLAav2iyZ7t4Z9Bv4ezioqFk1u1oWtnKQShJgVJGBePSSilghCtIRfYtYW_y4CE40PCCeGwByKJnxD1Vl1vFu2KTxznb2m1rCe5g1t-_AmwBxfmUMqQCpBDEa06ZooIrJiRjrGb1Q3HZ3OlD3ZpOsU5Vgq4Tq1O2CY17nqwkagvBl8rJ-bO-P8nPcXjsoAO80wKIEAl-5Sj_9qVnzcHj0UMwdoFBY8zwHSsayEtzVaSsGbaiUdAn9R79y7jjH-oqc70)

  * We have finished the develop the following features: Clear all Data in iOS (contacts, addresses, transaction history) for better privacy [#107](http://email.mg1.substack.com/c/eJwlUE2vgyAQ_DXlVgMoWg4c2ibe3vkdDeCq5CkYWNr47x-2yR5mv2Z2x2qEOcRDISQkOUEc3KjIqGjHbWeIS8MUATbtVkX2bFZnNbrgzynetJQs6iagFTWYsaGmlqCp6FjXTe3EmWjoRMkeEg46jw68BQUviEfwQFa1IO7pUt8vvC8xO1yyqWzYSvIAvf38FuBCur71ugKeSUoZUgGMdsQpTpmkDZesEYyxilVPyUX7oE95b3vJenlp6DazKmWTUNu_k5tEZcC70jFF4rq9P8XPiXjsoDy8UxFDiAS_ppSvhzKzZe_wGMBrs8KoMGb4rhUnRN3eJCkyYyhOeXVS79G9tD3-ASHIdk0), Ability in iOS to connect to specific Node  [#98](http://email.mg1.substack.com/c/eJwlULuOwyAQ_BrTxQLjFwVFEind1VdagDcJOhssWBL572-dSFvMvmZ2xxmER0y7RsjISoY0-VmzWfOhcYNlPk_3BLAav2i2Fbt4Z9DHcEw1bc_ZUwMI2Uk-gnVmvBsl2tF1HKRU0hnVDWyLGSdTZg_BgYYXpD0GYIt-Im65kuequVE8PD6LrV1cKbmAWX9-CfiYT2-zLIBHknOBTECNzOuGC8XbhgQ7IUQt6qtquv7Cr-rc35S4qarl60PUudiMxv0d1CxpC8FTx5LCaX1_ip8Lcd9AB3hn0kJIDL-e0NMTzawleNwnCMYuMGtMBb5rZEQn-1ExkpkjGRX0Qb0l_zJu_wc0Y3aK), Ability to hide balance on iOS for better privacy  [#83](http://email.mg1.substack.com/c/eJwlULuOwyAQ_JrQxQL8pKBIIrm7-kqLx8ZGZ4MFSyL__eFE2mL2NbM7RiHMIR4SISHJCeLkrCRW0p6bXhOXpmcE2JRbJdmzXp1R6II_p3jTUbLIoe0H1Ymaa7CDoM9aMGFVK0TPqebAyR4STipbB96AhBfEI3ggq1wQ93Spbxc-lpgdLllXJmwluYPafn4LcCFd32pdAc8kpQypgKEmTnLKBG24YE3LGKtY9RC87e70IW7dKNgoLg3dZlalrBMq83dSkyg1eFc6uihct_en-LkQjx2kh3cqWgiR4NeT8vRUZrbsHR4TeKVXsBJjhu9aMaKtu0GQImNDMcrLk3qP7qXM8Q-oB3YH), Alert user to stay online and active when send/receive Beam  (iOS [#85](http://email.mg1.substack.com/c/eJwlUMuOwyAM_JpyawQkkHDg0FbKbc97jIB4W9QEIjCt8vdLWsmyPH6NPc4g3GPaNUJGUjKkyc-azJr23PWW-Dz9JYDV-EWTrdjFO4M-hqOLd5KSh6ZSDNJJ3rLBUmGh73orzFwdo71pDdlixsmU2UNwoOEFaY8ByKIfiFs-tZcTH6vdPT6KbVxcK7iCWX9-a-BjPr_NsgAeIOcCuQaDIF5zyhTtuGKdYIw1rLkpLuSV3tRFjoqN6tTR9c6aXGxG457HapK0heBrxVaG8_r-JD8X4r6BDvDOlQshEfxqUp-eas9agsd9gmDsArPGVOA7VoUQrRwUqTRzrEIFfazekn8Zt_8DsrJ2Fw)) & (Android [#178](http://email.mg1.substack.com/c/eJwlULGuwyAM_JqyNQokIWFgaCt1e_MbIwNui14CEZhW-ftHW8nD2T777LNAeI9p14SZWMmYZu80c7odhR0N83m-JcQV_KLZVsziLZCP4c0SvWzZQ0vgk7jZzsppvClANwJHxYXqJy4RBrbFTDMU5zFY1PjEtMeAbNEPoi0futNBXGvcPT2KaWxca3JGWH9-K4DgUvTu-IJlQaoFn3PBXAEfJ-a1aLlqe6F4P3DOG95clBjkub2ok7wqflWHvl3vvMnFZAL7997PkjYYfO2YKnNcX5_i50zaN9QBX7mKESZGX2Pq53PlrCV42mcMYBZ0mlLB71h1Y-jkpFiVcbG6FfR79Zb8E-z-D6XMeFk) **),** Ask password on every send on Android  [#174](http://email.mg1.substack.com/c/eJwlUMuOwyAM_JpwawTkyYFDWym3Pe8x4uG0aBOIwDTK3y9tJR_G9thjj1EIjxBPiZCQ5ARxdlYSK-nAzaCJS_MSATblVkn2rFdnFLrg3yze9pQ8paC2MTC0iis9DgaWhrGu6ZZl1Gah40D2kHBW2TrwBiS8IJ7BA1nlE3FPVXOt-FTi4fCZdW3CVpIbqO3ntwDlbQzOXg61roCl4FLKkApgQ0uc5JQJ2nLB2o4xVrP6LnjX3-hdXPtJsElULd0erE5ZJ1Tm772fRKnBu9LRReayHZ_i50w8d5AejlTEECLBrzHl87lwtuwdnjN4pVewEmOG71hxo2v6UZAiY0Nxy8v36j26lzLnP_2EeKs)

 **Arnaud from AZTEC Protocol**

 _AZTEC Protocol is an efficient zero-knowledge protocol built on top of
Ethereum, making plug-and-play value transmission and asset governance privacy
tools for developers and companies.  _

  * This week we finished our work on the [public](https://github.com/AztecProtocol/AZTEC/pull/89) and [private](https://github.com/AztecProtocol/AZTEC/pull/91) range proofs.

  * We are progressing with our trusted setup, this week focusing on the writing of the formal paper outlining the security properties of the system

  * Zac, our CTO, has contributed to two open source projects with the aim of making cryptography cheaper on Ethereum:

    * [Optimisations to the evmone interpreter](https://github.com/chfast/evmone/pull/11)

    * [Adding batch pairing computation to the Parity BN library](https://github.com/paritytech/bn/pull/13)

  * We have just started work on tooling upgrades for adoption of AZTEC, including a rewrite of our aztec.js client side library, and a starter kit demonstrating how to build a zero-knowledge loan. Both will be released in the coming weeks.

  * We’re still hiring for two cryptographers to join the team. You can apply [here](http://email.mg2.substack.com/c/eJwlUEuOwyAMPU3ZNSKQpGHBoq1mrhHxcVumBEfgTJU5_RBF8sKy_fw-zhA8MW96wUJsLZCn4LVQgg8t87rz7diPLJTpkQFmE6KmvAJbVhuDMxQw7fe9kuylwUnVg3RcXQYu7eDAenvpjOx5Lweh2M4xmdUHSA40_ELeMAGL-kW0lJO8nsR3LZOeEBuHe_tH4M5LRkKH8Szr6AdtYUEL3iouRcs7LjvRtM2NX-_jnY-3QbS37ut66vj8FE1ZbSHj3vXfzLI2OVUBdecy-EBzSNQEPJTRtoBO8CkRiCAzOkKpXqcKntcUaJsgGRvB6wNSvUt1kQOrNB5rPklXsfjAxwfz-x-f0nXk), or by emailing [arnaud@aztecprotocol.com](mailto:arnaud@aztecprotocol.com) with the name of the role as the subject

#### Smart contracting platforms

 **Evan from[Ethereum](https://weekinethereumnews.com/)**

 _Ethereum  is a decentralized platform for applications that aims to resist
fraud, censorship or third-party interference._

  * [Eth2.0 spec v0.6.0](https://github.com/ethereum/eth2.0-specs/releases/tag/v0.6.0) heading toward a spec freeze in less than 2 months

  * [Economic model of eth2 staking incentives](http://hackingresear.ch/economic-incentives/)

  * [Adjustable degrees of statefulness in Eth1 clients](https://medium.com/@akhounov/the-shades-of-statefulness-in-ethereum-nodes-697b0f88cd04). [Casey Detrio’s tweetstorm](https://twitter.com/cdetrio/status/1121848688727527424) also has useful context

 **Erik from NEAR**

 _NEAR is a sharded proof-of-stake blockchain._

  * 17 PRs in [nearcore](https://github.com/nearprotocol/nearcore) from 5 different authors

  * Whiteboard series recorded [with Quarkchain](https://www.youtube.com/watch?v=opEtG6NM4x4&list=PL9tzQn_TEuFWweVbfTbaedFdwVrvaYPq4&index=17&t=0s)

  * Application/Dev layer

    * [Cover](https://github.com/nearprotocol/nearcore/pull/914) access key functionality with tests

    * Switch HTTP RPC interface to JSONRPC in both Node and nearlib

    * Support configuration of multiple deployment environments for CLI tools

    * Updated [Chess](https://nearprotocol.github.io/near-chess/) and [Memegen](https://nearprotocol.github.io/near-memegen/) to use latest CLI tools / nearlib

    * Deployed [NEAR Place](https://nearprotocol.github.io/near-place/) to permanent location on GitHub pages

  * Blockchain Layer

    * [Clean up repo](https://github.com/nearprotocol/nearcore/pull/894) by splitting into runtime and chain.

    * Docker containers with [first version of Testnet](https://hub.docker.com/r/nearprotocol/nearcore) and [studio/tools](https://hub.docker.com/r/nearprotocol/studio) are published. Added [scripts](https://github.com/nearprotocol/nearcore/pull/907) to spin Testnet up on GCloud.

    * [Refactor](https://github.com/nearprotocol/nearcore/pull/896) transaction verification in MemPool to have validation code in one place and improve security

 **AJ from Tezos**

 _Tezos is a self-amending blockchain that features formally verified smart
contracts, on-chain governance, and a proof-of-stake consensus algorithm which
enables all token holders to participate in the network.  _

  * Tezos Development team, Nomadic Labs, [demonstrated snapshotting for Tezos](https://twitter.com/JacobArluck/status/1121850193526317056). Snapshotting will enable anyone to sync a Tezos node within 1-2 minutes. 

  * Cryptonomic, creator of Galleon wallet for Tezos,[ releases v.0.8.0b which now features smart contract support, Conseil v2, and version checking](https://twitter.com/CryptonomicTech/status/1119349011809546240)

  * [Recap of TQuorum: Paris, Tezos’ first all-day conference hosted in Paris. ](https://medium.com/tocqueville-group/tquorum-paris-a-recap-9d4e5f0357e8)

  * [Install Kiln to easily setup a node and start baking with a GU](https://medium.com/@obsidian.systems/how-to-install-kiln-and-bake-on-ubuntu-a13d17df63c)I. Kiln makes it simple for anyone onboard Tezos. 

  * Learn [why Tezos is the best platform for tokenizing assets](https://medium.com/tocqueville-group/why-tezos-is-the-best-platform-for-tokenized-assets-89a960cfa828)

  * Tezos successfully reached its [100th cycle](https://tzscan.io/)! 

**Topper from Quorum Control**

 _Tupelo is a permissionless proof of stake DLT platform purpose-built to
model individual objects that enables flexible public or private data models._

  * [Tupelo v0.2.0 has been released!](https://docs.quorumcontrol.com/)

  * Send and Receive Token functionality fully available from both Go and JS

  * Code simplification through moving fully to libp2p for gossip layer

  * Moving TestNet to 0.2.0 targeted for April 30th

  * Latest performance data available [here](https://docs.quorumcontrol.com/platform_performance.html)

  * Significantly improved integration test suite coverage

  * Setup for a Tupelo cluster on Kubernetes in testing

 **Michael from Loom**

 _Loom Network is a platform for building highly scalable DPoS sidechains to
Ethereum, with a focus on large-scale games and social apps._

  * Released [Universal Transaction Signing](https://medium.com/loom-network/universal-transaction-signing-seamless-layer-2-dapp-scaling-for-ethereum-b63a733fc65c), which allows our Layer 2 sidechains to verify and accept transactions signed by native Layer 1 wallets. That gives users the ability to interact with PlasmaChain dapps directly from their existing wallets (e.g., MetaMask, Scatter, TronLink, etc).

  * [Launched imToken integration](https://medium.com/loom-network/you-can-now-stake-your-loom-tokens-directly-from-your-imtoken-wallet-more-on-the-way-f48a05fb4e8e), allowing users to stake LOOM tokens directly from their imToken wallet.

  * [Certus One](https://twitter.com/CertusOne) partnered with [CMCC](https://www.cmcc.vc/wp-content/uploads/2019/04/Press_Release_CMCC_Global_partners_with_Certus_One_to_launch_LOOM_validator.pdf) to launch a validator on PlasmaChain. [​](https://twitter.com/CertusOne)

  * 182M LOOM tokens are now staked on PlasmaChain, which amounts to ~23% of circulating supply.

 **Zaki from Cosmos**

 _The  Cosmos Network is a decentralized network of independent, scalable, and
interoperable blockchains._

  * The First upgrade of the Cosmos Hub is complete and transfers were enabled

  * Changes to Cosmos economics are in the works: [Proof of Stake tax optimization](https://forum.cosmos.network/t/burn-unstaked-tokens-instead-of-rewarding-staked-tokens/1795/6) and [Changes to Cosmos economics constants](https://forum.cosmos.network/t/proposal-draft-suggested-changes-to-a-few-cosmological-constants/1984/5)

  * Tendermint design sessions on[ State Sync](https://www.youtube.com/watch?v=4k23j2QHwrM) and the [Blockchain Reactor refactor](https://www.youtube.com/watch?v=TW2xC1LwEkE)

  * Exciting work is underway for [governance to change parameters directly](https://github.com/cosmos/cosmos-sdk/pull/4206) and [initialize the light client with weak subjectivity](https://github.com/tendermint/tendermint/pull/3577)

 **Kate and Dean from Agoric**

 _Founded by pioneers in secure development and distributed systems, Agoric
uses a secure subset of JavaScript to enable object capabilities and smart
contracts._

  * Mark [presented at UC Santa Cruz on Secure Computing](https://youtu.be/g28yRvHKIgc). He talked about visualizing the “attack surface” as a way to reason about aggregate risk, and showed how the composition of several techniques, such as blockchains, object-capability languages, and smart contracts, can produce a multiplicative decrease in risk without loss of functionality.

  * Saleh, an active member of our [ocapjs.org](https://ocapjs.org/) community, [has been putting together a really fantastic solution](https://ocapjs.org/t/containment-via-service-worker/94/6) to contain third-party DOM elements on a webpage, in addition to the work that we’ve been doing to contain third-party JavaScript. 

  * We’ve continued work on our[ “SwingSet” platform](https://github.com/Agoric/SwingSet#swingset-vat) and [our module rewriter for SES.](https://groups.google.com/forum/#!msg/ses-strategy/ci9yqpD5HIg/bLTmBXUpAQAJ)

#### Financial Infrastructure

 **Antonio from dYdX**

 _dYdX is a decentralized exchange for margin trading, borrowing, lending, and
eventually derivatives. dYdX allows traders to trustlessly short and get
leverage on crypto assets._

  * Private Alpha testing our new margin trading product. Seeing strong usage so far with well over $1M supplied and $500k borrowed / traded in the first week of private testing!

  * Successfully liquidated >$75k of positions for our Alpha

  * DAI lending rate has been high due to strong demand to go leveraged long on ETH, peaking at over 77% APR returns for lenders over the weekend

  * Gearing up for our public launch: implemented charts, fixing minor frontend bugs, adding features based on feedback form Alpha users

  * [Hiring](https://dydx.exchange/careers/) product designers & engineers full-time in SF!

 **Brendan from Dharma**

 _Dharma is the easiest place to borrow and lend cryptocurrencies. It enables
non-custodial peer-to-peer lending through smart contracts on Ethereum._

  * #ReFi with #DeFi continued in full force, leading to over 1.7m in borrow volume (nearly all Dai-denominated)

  * We're hiring full stack developers in SF. No crypto experience necessary. If interested, shoot us an email ([nadav@dharma.io](mailto:nadav@dharma.io) or [brendan@dharma.io](mailto:brendan@dharma.io)) or apply here

 **Coulter from MakerDAO**

 _Maker is comprised of a decentralized stablecoin, collateral loans, and
community governance._

  * Guesser and Boost VC became the first ever [venture capital deal](https://medium.com/guesser/guesser-expands-product-and-announces-seed-round-to-make-prediction-markets-more-accessible-to-7f5c4e1e997d) done using Dai. 

  * Released a development update to Multi-Collateral Dai on [Kovan testnet](https://blog.makerdao.com/update-the-road-to-multi-collateral-dai-kovan-release-v0-2-4/), covering the MCD CDP Portal, Dai.js, and new contract addresses. 

  * Forbes [detailed](https://www.forbes.com/sites/stevenehrlich/2019/04/24/how-leading-crypto-firms-and-traditional-fintechs-build-different-kinds-of-communities/#6a3fb282192f) Maker and DeFi in a recent article featuring COO Steven Becker

  * Underscore VC sat down with CEO Rune Christensen for an interview to discuss the future of blockchain. Watch it [here](https://www.youtube.com/watch?v=huSerGBTdYA). 

  * Fomohunt [integrated](https://www.fomohunt.com/fomohunt-integrates-makerdao-dai-stablecoin/) Dai as a supported payment, and Maker is one of the first to have access to their community event tool. 

 **Lazar from MARKET Protocol**

 _MARKET Protocol is a framework for creating tokens that track prices of
traditional or digital assets._

  * Added minting fee and flow improvements to MPX

  * Completed initial integration of ethers.js

  * Integrated solidity contract release into MPX and MPX API

  * Completed alert and notification setup for production environment

#### Layer two and interoperability

 **Tieshun from Namebase**

 _Namebase is the easiest way to buy, sell, and use Handshake._

  * R

 **Paul from Veil**

 _Veil  is a peer-to-peer prediction market and derivatives platform built on
top of Augur, 0x, and Ethereum._

  * R

 **Rahul from 0x**

 _0x_  is an open protocol that enables the peer-to-peer exchange of assets on
the Ethereum blockchain.

  * New hires [Mason Liang](https://twitter.com/0xProject/status/1120757258181402625) as a research engineer and [Rui Zhang](https://twitter.com/0xProject/status/1120827531635113984) as corporate counsel

  * 0x Mesh [architecture doc](https://forum.0x.org/t/0x-mesh-architecture-doc/349) released 

  * ERC 721 tokens [are now supported](https://twitter.com/efolioapp/status/1121642341792538624) by 0x Instant, with relayer Emoon showing off an integration

 **Tony from Liquidity.Network**

 _Liquidity Network is a transfer and swap platform for any token_

  * Sleek design and cool interface 

  * Support ERC-20 tokens on-chain & off-chain 

  * Support for $DAI 

  * Improved user experience 

  * Hub security checks ️

 **Dong Mo from Celer**

 _Celer Network is a layer-2 scaling platform that enables fast, easy and
secure off-chain transactions for not only payment transactions, but also
generalized off-chain smart contracts._

  * We finished UI for game introduction, leaderboard, game history and game result. 

  * We finished defining CelerX game info APIs and loaded and displayed Gomoku game (dev version) on CelerX platform. 

  * We finished mobile sandbox for internal game developers. 

  * We completed new wallet on-boarding and open-channel UI and finished refactoring iOS UI architecture. 

  * We finished CelerX feature development for the Soft Mainnet Launch.

  * We are working on LiBA and PoLC internal testnet launch. 

  * We switched devops to containerized system deployment and finished generic channel dispute and settlement implementation.

 **Alexandra from Parity Technologies**

 _Parity  Technologies builds core blockchain infrastructure, from Parity
Ethereum, an Ethereum client, to Polkadot, an interoperable blockchain
network._

  * At Sub0, the first Substrate developer conference, [Gavin Wood presented new Substrate features](https://twitter.com/ParityTech/status/1121417074881040384), including off-chain workers (CPU, network, secure-storage, IPFS),  indexable events, fee abstractions (block weight, rewards), and on-chain parallelism. 

  * At Sub0, Robert Habermeier presented on [Substrate's swappable consensus](https://twitter.com/polkadotnetwork/status/1120987377567137793) and the Cumulus libraries for easily turning a Substrate chain into a Polkadot parachain.

  * New [Build Your Own UTXO chain](https://github.com/nczhu/utxo-workshop) tutorial.

  * New [generic binary Merkle tree implementation in Rust](https://twitter.com/sorpaas/status/1120685779263451140), compatible with Serenity.

  * May Substrate events are [here](https://github.com/nczhu/awesome-substrate). 

  * Web3 Foundation is [providing grants to build the Web3 ecosystem](https://github.com/w3f/Web3-collaboration/blob/master/grants/grants.md). 

  * We're hiring [Developer Advocates](http://parity.io/jobs), among many other positions.

#### Application infrastructure

 **Doug from Livepeer**

 _Livepeer is a decentralized video infrastructure network, dramatically
reducing prices for developers and businesses building video streaming
applications at scale.  _

  * Merged support for multiple supply-side node support and failover. Broadcaster software now automatically will negotiate prices off chain with various providers on the network, will be able to work with multiple, and fail-over automatically, all without having to go on chain. This is part of the upcoming Streamflow release.

  * The community node grants program has continued to receive a stream of applications, including for a [Livepeer Primer microsite](https://github.com/Livepeer-Community-Node/Grant-Program/issues/13), and an [improved token holder user journey](https://github.com/Livepeer-Community-Node/Grant-Program/issues/12).

 **Ryan from FOAM**

 _FOAM  is building spatial applications and proof of location that bring
geospatial data to blockchains and empower a consensus driven map of the
world._

  * Building a front end for the previously released FOAM Plasma Demo 

  * Hosted the first Community Workshop call on improvement proposals, video recording [here](https://youtu.be/qw5QtT9hRJI "https://youtu.be/qw5QtT9hRJI")

  * [The Weekly Scavenger Hunt](https://twitter.com/Blockcities/status/1122348932842033152 "https://twitter.com/Blockcities/status/1122348932842033152") with Blockcities continues, with the latest in Tokyo Japan. 

  * Tokens in the FOAM voting contract have doubled in the last month and are nearing 1m as challenges heat up on the map. 

  * Finalizing the FOAM developer grant program to launch alongside [ETH New York ](https://ethnewyork.com/ "https://ethnewyork.com")hackathon, taking place at the Foamspace teams headquarters in the New Lab. 

 **David from Sia**

 _Sia is a decentralized cloud storage platform leveraging blockchain
technology to create a data storage marketplace that is more robust and more
affordable than traditional cloud storage providers._

  * We're getting closer to our goal of seed-based file recovery, making Sia files recoverable anywhere as long as you have your seed.

  * Manually disconnecting from a peer also blacklists that peer for you, improving the future integrity of your data.

  * Renters can now delete corrupt files and have access to improved logging.

  * The `siac renter` command is now more robust. It includes the number of contracts, total data stored, and minimum redundancy.

  * Sia-UI: Renters can now drag & drop files into the UI to upload them

  * Sia-UI: The config.json file allows users to customize things like the path where the blockchain data is stored

#### Other

 **Ari from Decentraland**

 _Decentraland is a virtual world where you can build and explore 3D
creations, play games and socialize._

  * [We released the SDK 6.0 Beta.](https://decentraland.org/blog/announcements/introducing-sdk-6-beta) It includes larger 16mx16m scenes, a more robust audio engine, more animations, better textures, and other new features and optimizations.

  * [Announced Decentraland Avatars](https://decentraland.org/blog/announcements/explore-decentraland-in-style), the customizable 3D characters and identity management platform for the virtual world.

  * [Released an upload/download feature for the Builder](https://decentraland.org/blog/announcements/download-upload-builder-scenes), allowing users to backup and restore their scenes across instances of the Builder.

  * We also added support for multiple asset packs in the Builder along with fixing some small display bugs for mobile, improved some icons and hotkeys, and added a preview button for the Publish to LAND feature.

 **Bowen from Hydro/DDEX.io**

 _Hydro  Protocol is an open source framework for building Decentralized
Exchanges. DDEX is the first decentralized exchange for Ethereum and ERC-20
tokens built on the Hydro Protocol. _

  * Hydro SDK x Augur Demo: Build prediction market with Hydro <https://www.reddit.com/r/hydroprotocol/comments/bh29c6/how_to_use_hydro_to_build_a_prediction_market_in/>

  * Hydro-sdk-wallet open source repo - integrate web3 wallet with in a single SDK : <https://github.com/HydroProtocol/hydro-sdk-wallets>

  * Hydro- box -dex working in progress : <https://github.com/HydroProtocol/hydro-box-dex>

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

