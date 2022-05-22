[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/33938f871040&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Dapper
Labs](https://miro.medium.com/fit/c/64/64/1*4qrJW34TWRKo2UlCo9IqbQ.png)](https://medium.com/dapperlabs?source=post_page
-----33938f871040--------------------------------)

Published in

[Dapper Labs

](https://medium.com/dapperlabs?source=post_page-----
33938f871040--------------------------------)

[![Dapper
Labs](https://miro.medium.com/fit/c/96/96/1*4qrJW34TWRKo2UlCo9IqbQ.png)](/@hellodapper?source=post_page
-----33938f871040--------------------------------)

[Dapper Labs](/@hellodapper?source=post_page-----
33938f871040--------------------------------)

Follow

Sep 26, 2019

·

12 min read

# “Who can deploy code on Flow?” and answers to other important questions from
Flow’s AMA

## Flow’s technical architect addresses questions ranging from “Which of
Flow’s feature should we be most excited about?” to “Why not just wait for
Ethereum 2.0?”

![](https://miro.medium.com/max/1400/1*ix30s1sX2l7PdEnCVi9WYQ.png)

Last week, Dapper Labs CTO and Flow’s technical architect, Dieter Shirley,
answered the following questions in the Flow community Discord during a “Ask
Me Anything” session.

You can find Dieter’s answers after the break. If you want to take part in
future Flow AMAs, [you’re invited to join Flow’s Community
Discord](https://discord.gg/hfxW25U).

  * Which of Flow’s feature should we be most excited about?
  * Is Flow an open network?
  * Who can deploy code on Flow?
  * Can Flow transactions be censored?
  * Do geoblocking, terms of service, and other “real world” rules apply to Flow?
  * What happens to Flow is Dapper Labs disappears?
  * Will Flow’s code be sufficiently open-sourced to support the protocol if “Satoshi” (i.e. the creator) disappears?
  * How will Flow handle state bloat?
  * Is Dapper Labs’ approach to Flow aligned with the principles of decentralization?
  * Will Flow allow self-sovereign users to control their keys unconditionally?
  * Can I trust Flow with my valuable digital assets?
  * Can the Flow team solve the hard problems around a decentralized Proof of Stake network?
  * What’s Flow’s approach to upgradeable smart contracts?
  * Can a group of “little guys” prevent bad behavior from malicious “elite nodes”?
  * Why isn’t Flow built as a Layer 2 solution on top of an existing smart contract platform?
  * Will the Collector Nodes within a cluster be required batch transactions into a collection in any particular order?
  * Why not use the Eth chain as a finality gadget for Flow, thereby making use of the security of the Ethereum chain?
  * Why build Flow when Ethereum 2.0 is right around the corner?
  * If a layer 1 blockchain powerful enough to run Flow existed when you began development, would you have preferred to build flow as a layer 2 versus a layer 1?
  * Are you concerned about Flow meeting its obligations as a smart contract platform with high performance, decentralization, and security?
  * Can you clarify how layered architecture breaks ACID guarantees?
  * How does Flow ensure the nodes responsible for storing the global state do not tamper with that state?
  * Does Flow intend to be real-time capable to support games like Call of Duty or Starcraft II?
  * When can I have access to any sort of information to create an SDK within Unreal Engine 4?

## Which of Flow’s features should we be most excited about?

 **Dieter Shirley:** Depends on what kind of person you are! I think smart
contract devs are going to be most excited about some of the changes we’re
making to the programming model. It’s exactly the kind of stuff I wished we
had while we were writing CryptoKitties and Cheeze Wizards. End users should
just be excited about the new dapp options that are coming. We’ve talked to
lots of big entertainment companies that are excited about the possibilities
of decentralized experiences, but they saw CryptoKitties hit a hard cap with
the network capacity. They want to ship something, but only if the technology
can keep up with their audience size.

##  **Is Flow an open network?**

Yes, Flow will be an open network.

##  **Does anyone have the power to deploy code without permission?**

Anyone will be able to deploy a smart contract to the network.

##  **Can transactions be censored?**

Flow’s transaction submission process is censorship-resistant.

##  **Can contracts be updated by anyone other than the deployer?**

“Beta mode” smart contracts can be updated by anyone who controls the account
that owns that contract. (Accounts on Flow have multi-sig support, so access
controls can be very fine-grained.)

##  **Does geoblocking, ToS, and other “real world” rules apply?**

The “real-world” rules like geoblocking, ToS, etc. will only apply be applied
at the application level (i.e. access to a web application) and not at the
protocol-level, similarly to how things work on Ethereum today.

##  **What happens to Flow if Dapper Labs disappears?**

The code will be open-sourced ASAP and at that point, anyone can run their own
version of the Flow network.

## Will Flow’s code be sufficiently open-sourced to support the protocol if
“Satoshi” (i.e. the creator, like Dieter or the Dapper Labs team) disappears?

Yes. The code will be open-sourced ASAP and, over time, Dapper Labs will
become a minority participant.

## How will Flow handle state bloat?

 **New blockchains love to claim fast transactions-per-second (TPS), but the
faster they go the faster they run into state bloat issues. How does Flow
handle this? Just add more ssds to certain nodes?**

State bloat is an important long term issue, and we will implement “storage
rent” on day one. Storage rent encourages thoughtful use of on-chain storage
and our implementation allows old data to be archived out of the “working set”
when the rent payment runs out. (Archived data will be referenced by a content
hash, so it can always be securely re-introduced again in future.)

## Is Dapper Labs’ approach to Flow aligned with the principles of
decentralization?

 **It seems like the larger Dapper mission is to become the “AppStore” of
blockchain. A nice and safe walled garden with a curated selection of fun apps
that play by all the rules. This makes total sense from a business
perspective. You want to capture and monetize your audience. But
philosophically, this falls well short of my definition of decentralization.**

The goals of the Dapper interface and games teams and the goals of Flow are
perfectly aligned, but aren’t identical for exactly the reasons you
articulate. At the user interface level, we want to curate “the best of the
blockchain” for our users, without requiring them to be able to audit smart
contracts in order to know what experiences they can trust.

> Flow can’t be a gated community or else we’ll cut off the greatest creative
> force in the world: a million minds free to explore an open sandbox.

Flow, however, can’t be a gated community or else we’ll cut off the greatest
creative force in the world: a million minds free to explore an open sandbox.
There’s no conflict, tho. We can choose the experiences we highlight in our
interfaces, without blocking anything on Flow. Heck, we won’t even block stuff
in the interface (which isn’t to say you might not see a stern warning now and
again!). Chrome (for example) doesn’t hard-block access to any websites, but I
sure appreciate those phishing warnings when they come up…

## Will Flow allow self-sovereign users to control their keys unconditionally?

 **I want to, know how to, and do control my own keys unconditionally. I
appreciate you’re building for a future audience that might not share those
values, but right now I and people similar to me are your audience and
customers.**

Flow will always support unconditional self-sovereignty for folks who have the
skills and desire to manage their own keys.

Indeed, many of the improvements we’ve made to the account model in Flow exist
solely to support folks like you. (For example, Flow will let you cycle your
keys regularly without having to transfer your assets to a new account.) It’s
true that we usually focus on how we’re helping people who are intimidated by
key management, but we haven’t (and won’t) forget about more sophisticated
users. There’s no shortage of Trezors and Ledger Nanos inside these walls!

## Can I trust Flow with my valuable digital assets?

 **I already barely trust Ethereum enough to hold NFT assets of non-trivial
value. I would not treat them the same way on any lesser stateful chain,
sidechain, or anything else that offers less than (the not perfect, build
kinda the best we got right now) stateful decentralization standard that is
Ethereum.**

Trust always has to be earned, we agree. In the immediate term, CryptoKitties
and Cheeze Wizards can stay on Ethereum for as long as their owners want them
to.

## Can the Flow team solve the hard problems around a decentralized Proof of
Stake network?

 **Are there any live PoS networks with meaningful economic activity (not
DPoS) and full stateful smart contract functionality? I know many are in
active development. The question here is, how can we trust your team has
solved the legitimately hard problems to bootstrap a decentralized PoS network
with the right incentive structures and design decisions. I don’t believe
there are any examples of this to even compare to in an adversarial
environment with truly high economic stakes.**

It’s not an easy problem but our internal team is amazing and we have some of
the smartest people in the world advising us. We have several security proofs
in our Technical Papers, with more forthcoming. By the time the network goes
live, we will have had lots of public review of our plans to ensure they
represent the best thinking possible.

## What’s Flow’s approach to upgradeable smart contracts?

 **“Beta” smart contracts. If I’m a hacker I’m just going to wait until after
the beta period to exploit a bug. If I’m a security researcher with loose
morals, better hope there’s a bug bounty larger than the beta value. As a
user, there will be weird pressure to “get in early” during beta and then have
the carpet pulled out from under you with a hack or unscrupulous dev
switchero. Please learn from the train-wreck that is EOS upgradable contracts.
imo Ethereum contracts are already too upgradable. I already distrust the
level of admin powers and proxying in many popular dapps. What gives me trust?
True immutability as a base requirement. Then value held * time. Hackers are
surprisingly rational actors economically. The black/grey/white incentives in
the “beta” system don’t seem properly aligned.**

You’re absolutely right. There’s no easy answer here. We think that our
solution finds a better balance of the issues than other approaches, but no
solution will be perfect. We can assure you we aren’t taking this issue
lightly, however, and our thoughts run deeper than “Devs want upgradability?
Let’s give ’em upgradability!” We totally understand that there are many
trade-offs here, and are seeking better answers. (If you want some idea of
what we’re thinking about, y[ou can start
here](https://en.wikipedia.org/wiki/Design_by_contract))

## Can a group of “little guys” prevent bad behaviour from malicious “elite
nodes”?

 **How do you prevent the problems seen in DPoS-style super nodes from
happening to the compute/capital intensive Execution Nodes? Can a
morally/technically correct group of “little guys” prevent bad behaviour from
malicious “elite nodes”?**

The honest “little guys” can definitely prevent bad behaviour from the
compute-intensive Execution Nodes. Indeed, the Execution Nodes don’t even get
paid if those honest “little guys” don’t explicitly approve their work. The
stake required for Execution Nodes in Flow isn’t for joining consensus, it’s a
bond against malicious behaviour. The job of Execution Nodes is purely
deterministic: Do this calculation. Do it correctly. We will check your work,
and if there’s a single mistake, we’ll slash your stake. The Verification
Nodes and Consensus Nodes are the ones checking the result, and slashing
Byzantine behaviour when its discovered. And participating as one of these
“honest little guys” is possible with consumer hardware, home broadband, and a
minimal stake.

##  **Why wasn’t Flow built as a Layer 2 solution on top of an existing smart
contract platform?**

Unfortunately, there is no current smart contract platform that is fast enough
to support Flow as a Layer 2, while also being properly decentralized. The way
you could build Flow as a Layer 2 would be to have a smart contract (or series
of smart contracts) running on another network and performing the work of the
Consensus Nodes. While we have carefully designed the role of the Consensus
Nodes to be a light as possible, they’ll still need to be able to handle a
workload equivalent to hundreds of transactions per second. They also need to
be able to run some custom cryptography (most notably aggregated BLS
signatures), which is simply too expensive to run inside another chain’s VM.
In fact, Flow may be the first blockchain powerful enough to run Flow as a
Layer 2!

##  **Will the Collector Nodes within a cluster be required batch transactions
into a collection in any particular order?**

Collectors can arrange transactions in collections in any particular order
they like. To prevent collectors from having too much power over the
transaction order, Flow _shuffles_ all transactions in a block before the
block is executed.

##  **Why not use the Eth chain as a finality gadget for Flow, thereby making
use of the security of the Ethereum chain?**

We have been considering doing this, but it requires that we build some kind
of Ethereum light client into the Consensus Nodes. The final decision will
come down to a balance of cost and benefit.

##  **Why declare that eth’s scaling problems are the be-all-end-all state of
the Eth chain, when Eth 2 is right around the corner?**

Building inter-contract dapps is really hard on sharded blockchains. Eth2 is a
sharded blockchain. Additionally, my understanding is that it Eth2 isn’t
scheduled to be ready for prime-time until 2021.

##  **If a layer 1 blockchain powerful enough to run Flow existed when you
began development, would you have preferred to build flow as a layer 2 versus
a layer 1?**

That’s a hard question to answer in the abstract because there are so many
aspects to a trustworthy chain than just the capacity. Our Layer 2 solution
can only be as robust as the Layer 1 it’s built on. But in principle, yes. If
there had been a strongly decentralized network (at the level of Bitcoin and
Ethereum) that was capable of acting as our Layer 1, we would have absolutely
considered it.

##  **Are you concerned that there are too many responsibilities of your
blockchain — trying to be a smart contract platform with high performance +
maintaining decentralization and security?**

That was the challenge we set to ourselves because we believe that its only by
having all of those properties that the magic happens. The response to
CryptoKitties surprised the whole team, and the possibilities of an
interoperable decentralized ecosystem are too valuable for humanity not to try
to achieve.

##  **Could you explain further / justify the claim made in your technical
paper that a layered architecture (layer 1 / layer 2) breaks ACID
guarantees?**

Yeah, [the Primer](https://www.withflow.org/primer) is a high-level document
and we chose to elide some subtleties for readability. Virtually all
blockchains ensure that each transaction is processed atomically, but sharded
blockchains (and most layer two solutions) limit the state that is visible to
a single transaction. So, if you are lucky, and all your state is in a single
shard/zone/side-chain, you get full atomicity (or “ACID guarantees” as we say
in the Primer). But if you _aren’t_ lucky, and the state lives in two
different shards, you need to have some kind of multi-transaction scheme to
update the data in two places. And, while each transaction is atomic, there
are no atomicity guarantees made between transactions. This isn’t an
unsolvable problem. You can create a system of escrow, or temporary state
locks, or various other schemes to make it work, but those mechanisms are
complex and (worse!) error prone. We think that the ability for any smart
contract to talk synchronously with any other smart contract is the super
power of blockchains, and sharding is the kryptonite.

## How does Flow ensure the nodes responsible for storing the global state do
not tamper with that state?

 **If consensus nodes are not responsible for maintaining the growing state,
but rather that is delegated to specialized nodes in order to maintain high
decentralization of the consensus nodes via lower participation barrier, how
does the protocol ensure that these specialized nodes responsible for storing
the global state do not tamper with that global state?**

Correct. The computational state is maintained by dedicated Execution Nodes.
Whenever an Execution Node computes a block, it issues an Execution Receipt
that also contains state commitments (e.g. a Merkle root). The verifiers check
the computation (verification is distributed and parallelized). If the
verifiers agree with the result, they issue a Result Approval to the Consensus
Nodes. If and only if more than 2/3 of verifiers agree and there are no faulty
computation challenges pending, the consensus nodes will seal the result.

While verification is a probabilistic process, we can guarantee with almost
certainty that no faulty results will be sealed (for details, [see our White
paper.](https://www.withflow.org/technical-papers))

##  **Does Flow intend to be realtime capable like xaya claims to be?**

 **I’m talking about reaction-based Multiplayer games, e.g. FPS like Call of
Duty or RTS like starCraft II**

I haven’t looked at Xaya in-depth, so I can’t speak to their claims. They seem
overly bold, to be honest. Having said that, I think that “state channels”, a
scaling solution akin to payment channels (like the Lightning Network), could
be adopted to a gaming context, where your “netcode library” is implemented in
terms of state channels. I believe modern computers could handle the extra
load pretty easily. The upshot would be that you’d have a single on-chain
transaction to start a “session”, and then you’d have the normal guarantees of
state channels during your session, and then you’d have a single on-chain
transaction to close the session. (Maybe more if there was a dispute.) Real-
time gaming with most of the guarantees of blockchain! (BTW — This capability
would be especially well suited to a fast, high-capacity chain like Flow, but
should be implementable on any smart-contract platform.)

##  **When can I have access to any sort of information to create a SDK within
Unreal Engine 4?**

Informational drops are going to keep happening between now and the network
launch next year. You will _definitely_ have the information you need to build
alternate client libraries before the network goes live.

# Do you have a question about Flow?

Check out the Flow site to learn more about the project.

  * [Read Flow’s FAQ](https://www.withflow.org/faq/)
  * [Read Flow’s primer](https://www.withflow.org/primer/)
  * [Read Flow’s technical papers](https://www.withflow.org/technical-papers/)

If you still want to learn more, [you’re invited to join Flow’s Community
Discord](https://discord.gg/hfxW25U).

\--

\--

\--

## [More from Dapper Labs](/dapperlabs?source=post_page-----
33938f871040--------------------------------)

The serious business of fun and games on the blockchain

[Read more from Dapper Labs](/dapperlabs?source=post_page-----
33938f871040--------------------------------)

## Recommended from Medium

[[![Polkacity](https://miro.medium.com/fit/c/40/40/1*87uDDIis41omGm31kzFzmQ.jpeg)](/@polkacity?source=post_internal_links
---------0----------------------------)

[Polkacity

](/@polkacity?source=post_internal_links---------
0----------------------------)

## Polkacity on Binance Smart Chain

![](https://miro.medium.com/focal/112/112/50/50/1*Ka835FdgQYteIR4dHVhsxA.jpeg)](/@polkacity/polkacity-
on-binance-smart-chain-2cdacad5b64a?source=post_internal_links---------
0----------------------------)

[[![Sadman
Ishrak](https://miro.medium.com/fit/c/40/40/1*dqhjqUwbg8IOaEO_7N2s7w.jpeg)](/@sadmanishrak?source=post_internal_links
---------1----------------------------)

[Sadman Ishrak

](/@sadmanishrak?source=post_internal_links---------
1----------------------------)

in

[Coinmonks

](https://medium.com/coinmonks?source=post_internal_links---------
1----------------------------)

## Become Blockchain Smart Under 5 Minutes (NO Fluffy BS)

![](https://miro.medium.com/focal/112/112/50/50/0*XobO_6L98NnrC4Yz.)](/coinmonks/what-
is-blockchain-simplest-explanation-4fdaa95c0e63?source=post_internal_links
---------1----------------------------)

[[![MIXMARVEL](https://miro.medium.com/fit/c/40/40/1*Lmg30I_2GnmgYi9_8WCe5Q@2x.png)](/@mixmarvelgame?source=post_internal_links
---------2----------------------------)

[MIXMARVEL

](/@mixmarvelgame?source=post_internal_links---------
2----------------------------)

in

[MIXMARVEL Official Blog

](https://medium.com/mixmarvel-official-blog?source=post_internal_links
---------2----------------------------)

## NFTs would change the whole game of the art industry, says Mary Ma

![](https://miro.medium.com/focal/112/112/50/50/1*xG0t5tRyxnJFjVJf5qudJA.png)](/mixmarvel-
official-blog/nfts-would-change-the-whole-game-of-the-art-industry-says-mary-
ma-ee6d702c6828?source=post_internal_links---------
2----------------------------)

[[![SecretSwap](https://miro.medium.com/fit/c/40/40/1*oLiy2OudPjIcWFBP3YqzTQ.png)](/@secret_swap?source=post_internal_links
---------3----------------------------)

[SecretSwap

](/@secret_swap?source=post_internal_links---------
3----------------------------)

## DRO-kenomics: Diving into Hydro Finance Tokenomics

![](https://miro.medium.com/focal/112/112/50/50/1*NB3DO7MzeTHgfoZgVk1MBw.png)](/@secret_swap/dro-
kenomics-diving-into-hydro-finance-tokenomics-
dff35b402a29?source=post_internal_links---------3----------------------------)

[[![Leigh
Diprose](https://miro.medium.com/fit/c/40/40/1*jSujBg1vWouK22nKdRIdrg.jpeg)](/@_LeighDiprose_?source=post_internal_links
---------4----------------------------)

[Leigh Diprose

](/@_LeighDiprose_?source=post_internal_links---------
4----------------------------)

in

[Consensus AI

](https://medium.com/consensus-ai?source=post_internal_links---------
4----------------------------)

## Consensus Update #6 — The State of Blockchain in the US

![](https://miro.medium.com/focal/112/112/50/50/1*6bWwx4qHLiMcDQH8Pm_lqQ.jpeg)](/consensus-
ai/consensus-update-6-the-state-of-blockchain-in-the-
us-99de027a2c2b?source=post_internal_links---------
4----------------------------)

[[![Baklava
Chef](https://miro.medium.com/fit/c/40/40/1*41Ad38Y4NlzLo58jz3VAXg.png)](/@baklavaspace?source=post_internal_links
---------5----------------------------)

[Baklava Chef

](/@baklavaspace?source=post_internal_links---------
5----------------------------)

## Baklava Space Integrates Chainlink Price Feeds To Secure Its Yield Farms on
Avalanche

![](https://miro.medium.com/focal/112/112/50/50/0*Lbyc-
cnutHbeTe49)](/@baklavaspace/baklava-space-integrates-chainlink-price-feeds-
to-secure-its-yield-farms-on-avalanche-5892728be80?source=post_internal_links
---------5----------------------------)

[[![Ömer
Take](https://miro.medium.com/fit/c/40/40/1*fbxywJGd1MVGzki3sDqMJg.jpeg)](/@omersuratake?source=post_internal_links
---------6----------------------------)

[Ömer Take

](/@omersuratake?source=post_internal_links---------
6----------------------------)

in

[BCISTCenter

](https://medium.com/bcistcenter?source=post_internal_links---------
6----------------------------)

## FinTech’s pathway under COVID-19 circumstances

![](https://miro.medium.com/focal/112/112/50/50/1*XRf2Se7wTFnkm_0f4EtHEw.jpeg)](/bcistcenter/fintechs-
pathway-under-covid-19-circumstances-7c0a4f6477ca?source=post_internal_links
---------6----------------------------)

[[![MIXMARVEL](https://miro.medium.com/fit/c/40/40/1*Lmg30I_2GnmgYi9_8WCe5Q@2x.png)](/@mixmarvelgame?source=post_internal_links
---------7----------------------------)

[MIXMARVEL

](/@mixmarvelgame?source=post_internal_links---------
7----------------------------)

in

[MIXMARVEL Official Blog

](https://medium.com/mixmarvel-official-blog?source=post_internal_links
---------7----------------------------)

## 120,000 MIX to DeHero’s Valentine’s Day Celebration from MixMarvel

![](https://miro.medium.com/focal/112/112/50/50/1*K6T6k_dIMalyz_AxOSoSuw.jpeg)](/mixmarvel-
official-blog/120-000-mix-to-deheros-valentine-s-day-celebration-from-
mixmarvel-552c0f7ce983?source=post_internal_links---------
7----------------------------)

[](/?source=post_page-----33938f871040--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
33938f871040--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
33938f871040--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
33938f871040--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
33938f871040--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----33938f871040--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----33938f871040--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fdapperlabs%2Fflow-
ama-with-dieter-shirley-33938f871040&source=post_page
--------------------------nav_reg-----------)

[![Dapper
Labs](https://miro.medium.com/fit/c/176/176/1*4qrJW34TWRKo2UlCo9IqbQ.png)](/@hellodapper)

[

## Dapper Labs

](/@hellodapper)

800 Followers

The serious business of fun and games on the blockchain

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F92fd7014333&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fdapperlabs%2Fflow-
ama-with-dieter-
shirley-33938f871040&newsletterV3=6544777e30d2&newsletterV3Id=92fd7014333&user=Dapper+Labs&userId=6544777e30d2&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Jonathan
Anand](https://miro.medium.com/fit/c/40/40/0*7qGUHnASCSwQciHR)](/@jonathananand?source=read_next_recirc
---------0---------------------0194a225_516a_4def_b213_9d40495add3c-------)

[Jonathan Anand

](/@jonathananand?source=read_next_recirc---------0---------------------
0194a225_516a_4def_b213_9d40495add3c-------)

## DAOS: The Corporate Structure of the Future

![](https://miro.medium.com/focal/112/112/50/50/1*-ofIUgCBjgM1zxWkpZQzgA.png)](/@jonathananand/daos-
the-corporate-structure-of-the-future-eb26ca40de9d?source=read_next_recirc
---------0---------------------0194a225_516a_4def_b213_9d40495add3c-------)

[[![Serenity
Shield](https://miro.medium.com/fit/c/40/40/1*Jdh1QWTjAzTyNwTXk3hmfg.png)](/@SerenityShield?source=read_next_recirc
---------1---------------------0194a225_516a_4def_b213_9d40495add3c-------)

[Serenity Shield

](/@SerenityShield?source=read_next_recirc---------1---------------------
0194a225_516a_4def_b213_9d40495add3c-------)

## Serenity Shield — Planning Ahead

![](https://miro.medium.com/focal/112/112/50/50/1*3QOrWce8BvuX6U7my3X6bg.jpeg)](/@SerenityShield/serenity-
shield-planning-ahead-b2ac4b6f969d?source=read_next_recirc---------1
---------------------0194a225_516a_4def_b213_9d40495add3c-------)

[[![Rapid
Innovation](https://miro.medium.com/fit/c/40/40/1*DUuhkL3ywG0_eoZ121CiDw.jpeg)](/@rapidinnovation?source=read_next_recirc
---------2---------------------0194a225_516a_4def_b213_9d40495add3c-------)

[Rapid Innovation

](/@rapidinnovation?source=read_next_recirc---------2---------------------
0194a225_516a_4def_b213_9d40495add3c-------)

## Rapid Innovation Welcomes Exo Fi as New Development Client

![](https://miro.medium.com/focal/112/112/50/50/0*dtX0wp0nCOApoIH0.jpeg)](/@rapidinnovation/rapid-
innovation-welcomes-exo-fi-as-new-development-
client-a37b9c1ae98?source=read_next_recirc---------2---------------------
0194a225_516a_4def_b213_9d40495add3c-------)

[[![Coderlabny](https://miro.medium.com/fit/c/40/40/1*dM5S0mhj0vUNy7_nzAQURQ.png)](/@coderlabny?source=read_next_recirc
---------3---------------------0194a225_516a_4def_b213_9d40495add3c-------)

[Coderlabny

](/@coderlabny?source=read_next_recirc---------3---------------------
0194a225_516a_4def_b213_9d40495add3c-------)

## The Quick and Dirty Guide to get Up and Running with OmniChain NFTs

![](https://miro.medium.com/focal/112/112/50/50/1*o2FIkTiLMrvcasUNlRHRhg.png)](/@coderlabny/the-
quick-and-dirty-guide-to-get-up-and-running-with-omnichain-
nfts-c85f89726cf8?source=read_next_recirc---------3---------------------
0194a225_516a_4def_b213_9d40495add3c-------)

[Help

](https://help.medium.com/hc/en-us)

[Status

](https://medium.statuspage.io)

[Writers

](https://about.medium.com/creators/)

[Blog

](https://blog.medium.com)

[Careers

](/jobs-at-medium/work-at-medium-959d1a85284e)

[Privacy

](https://policy.medium.com/medium-privacy-policy-f03bf92035c9)

[Terms

](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f)

[About

](https://medium.com/about?autoplay=1)

[Knowable

](https://knowable.fyi)

