[](https://medium.com/)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/3610fd739502&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](https://medium.com/)

[Home](https://medium.com/)

[Notifications](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Enigma](https://miro.medium.com/fit/c/64/64/1*aIQTqQDM97_LBgHTkHGqcA.png)](https://blog.enigma.co/?source=post_page
-----3610fd739502--------------------------------)

Published in

[Enigma

](https://blog.enigma.co/?source=post_page-----
3610fd739502--------------------------------)

[![Assaf
Morami](https://miro.medium.com/fit/c/96/96/1*JXIPOovEEjz8_2R6KhagFQ.png)](https://medium.com/@assafmo?source=post_page
-----3610fd739502--------------------------------)

[Assaf Morami](https://medium.com/@assafmo?source=post_page-----
3610fd739502--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F8475b3eaa650&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fsecret-
contracts-update-milestone-3-of-3-is-
complete-3610fd739502&user=Assaf+Morami&userId=8475b3eaa650&source=post_page-8475b3eaa650
----3610fd739502---------------------follow_byline-----------)

Jun 17, 2020

·

8 min read

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F3610fd739502&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fsecret-
contracts-update-milestone-3-of-3-is-
complete-3610fd739502&source=--------------------------bookmark_header-----------)

[

Save

](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F3610fd739502&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fsecret-
contracts-update-milestone-3-of-3-is-
complete-3610fd739502&source=--------------------------bookmark_header-----------)

# Secret Contracts Update: Milestone 3 of 3 is Complete!

## Assaf Morami, developer at Enigma, shares a major update on running
CosmWasm inside an enclave with encryption — the latest achievement on the
journey to Secret Apps.

![](https://miro.medium.com/max/1400/1*-hwB41MLqCzh30DXEBwRcw.png)

Hello to the Secret Network community!

Today we have exciting news. **Enigma has reached our third milestone of three
on the path to enabling _secret contracts:_ **smart contracts that can run on
a distributed system of nodes equipped for trusted computation. This allows
applications to use encrypted data without revealing the information. We have
achieved this goal by running [CosmWasm](https://www.cosmwasm.com/) contracts
inside secure enclaves across the Secret Network!

This post covers the technical details of this milestone, the significance of
this achievement, and next steps for the network and ecosystem.

Since participating in the launch of Secret Network (a Cosmos SDK / Tendermint
chain) earlier this year, Enigma has been focused on building a `compute`
module for private computation on a distributed system of nodes equipped with
Trusted Execution Environments (TEEs). This work, led by
[myself](https://forum.scrt.network/u/assafmo),
[Tom](https://forum.scrt.network/u/toml),
[Itzik](https://forum.scrt.network/u/cashmaney),
[Reuven](https://forum.scrt.network/u/reuven), and
[Guy](https://forum.scrt.network/u/guy) comprises many specific tasks,
organized into these project milestones on GitHub:

  * [Milestone 1](https://github.com/enigmampc/SecretNetwork/milestone/1?closed=1) — Integrating Smart Contracts into the Enigma Blockchain (complete)
  * [Milestone 2 ](https://github.com/enigmampc/SecretNetwork/milestone/2?closed=1)— Executing CosmWasm Smart Contracts Inside the Enclave (complete)
  * [Milestone 3](https://github.com/enigmampc/SecretNetwork/milestone/3?closed=1) — Adding Encryption for Secret Contracts Running Inside the Enclave **(now complete)**

Achieving Milestone 3 involved working on the `compute` module in parallel
with the CosmWasm team and building encryption capabilities into the system.
This milestone also resulted in our updated [encryption
specs](https://build.scrt.network/protocol/encryption-specs.html) (feedback
welcome!). Next, our team is excited to conduct further testing with the
Secret Network community in the upcoming Secret Games.

Read on for all the details!

# Achieving Milestone 3 — Technical Details

First, allow me to say we are happy to contribute open-source technology
alongside our community of privacy advocates, developers and infrastructure
providers. Enabling privacy-preserving smart contracts will create significant
benefits for users of decentralized applications. As we continue building our
[Secret Hub](https://blog.scrt.network/secret-hub), I hope we connect and
collaborate as much as possible with members of the Cosmos ecosystem. Enigma
believes multichain governance and coordination is extremely important for the
long-term sustainability and health of the overall ecosystem.

The following section is quite technical, so if you’re mostly interested in
what’s next, scroll down to the “What does this mean for…” sections below.

Now, let’s recall this post by Enigma’s CEO Guy Zyskind:

>  **“A key design choice in this protocol was to remove the need for off-
> chain communication. Everything needs to be handled on-chain for simplicity
> and consistency.”**

[

## Network key management/agreement

### This post describes the process in which validators obtain shared keys to
be used in secret contracts. For the time…

forum.scrt.network

](https://forum.scrt.network/t/network-key-management-agreement/1324)

## [Secret Network Key Management /
Agreement](https://forum.scrt.network/t/network-key-management-agreement/1324)

This forum post includes Guy’s description of the bootstrap protocol and three
phases in the process by which validators obtain shared keys to be used in
secret contracts. For the time being, we assume all keys are derived from a
single source of true randomness: a master seed. The registration protocol
essentially allows all validators to share a truly random seed that is only
ever accessible from a validator’s enclave. Learn more in [that
post](https://forum.scrt.network/t/network-key-management-agreement/1324).

Our team continued the journey developing the initialization logic for the
enclave. We created a bootstrapping protocol to get a shared random seed to
all validators, then we built processes for key generation and node
registration. [This GitHub
issue](https://github.com/enigmampc/SecretNetwork/issues/43) details our work
on lifecycle management for new nodes, which are not able to start syncing
blocks until they are confirmed as registered nodes. That way, our system
protects the integrity of the trusted execution environments running across
the Secret Network.

In this task, [hello world local node to
enclave](https://github.com/enigmampc/SecretNetwork/issues/44), we prepared a
skeleton for the implementation of (`register_validator` and `share_seed`)
functionalities, as well as any other API we need between a node and its
enclave. This task, [on-chain bootstrap
skeleton](https://github.com/enigmampc/SecretNetwork/issues/42), outlined the
interface of the bootstrap module. It has a list of registered validators ,
and validators are in one of two states (pending, registered). There is a
`register_validator()` transaction handler to deal with new validators
joining, plus a `share_seed()` transaction handler to deal with sharing
encrypted seed values for new validators. Also, there is a
`confirm_validator()` transaction handler.

## Phase 1

See the logic described here in Phase 1 (`register_validator()`):

  * `register_node()` ~ [enclave part](https://github.com/enigmampc/SecretNetwork/issues/45) | [node part](https://github.com/enigmampc/SecretNetwork/issues/46) | [on-chain part](https://github.com/enigmampc/SecretNetwork/issues/47)
  * `confirm_node()` ~ [node part](https://github.com/enigmampc/SecretNetwork/issues/51) | [on-chain part](https://github.com/enigmampc/SecretNetwork/issues/52)

## Phase 2

See the logic described here in Phase 2:

  * `share_seed()` ~ [on-chain part](https://github.com/enigmampc/SecretNetwork/issues/50) | [node part](https://github.com/enigmampc/SecretNetwork/issues/49) | [enclave part](https://github.com/enigmampc/SecretNetwork/issues/48)

Next, let’s recall this additional post by Guy:

[

## Input/Output/State Encryption/Decryption protocol

### For the most part, our goal is to keep the input/output encryption
protocol built for Discovery largely unchanged. The…

forum.scrt.network

](https://forum.scrt.network/t/input-output-state-encryption-decryption-
protocol/1325)

## [Input / Output / State Encryption
Protocol](https://forum.scrt.network/t/input-output-state-encryption-
decryption-protocol/1325)

This forum post includes a sketch of the encryption / decryption protocol. We
assume validators start with shared keys. Those keys are used to generate the
initial keys once the random seed has been shared with a new validator.

## INPUTS

Secret contract execution should enable users to encrypt their inputs, which
will only ever be decrypted inside of secure enclaves. Therefore, this
protocol is part of a larger user transaction that should trigger a secret
contract.

## OUTPUTS

Encrypted outputs (where the output is encrypted with the sender’s key), are
handled largely the same way as encrypted inputs. We can use the same
`ephemeral_secret` to encrypt the output (which is stored as part of the
contract’s state), and only the sender will be able to decrypt it.

## STATE

The simplest solution to get to an encrypted state, and assuming we have a
public state which allows for arbitrary values, is to allow selective
encryption of specific state dict entries (i.e., the key is public and the
value is encrypted). If a developer wants to encrypt the whole state, they
should have a single attribute called ‘state’ and fully encrypt a state
dictionary as the value.

To [implement key management inside the
Enclave](https://github.com/enigmampc/SecretNetwork/issues/163), we had to
[properly set IV for AES
](https://github.com/enigmampc/SecretNetwork/issues/165)[bug](https://github.com/enigmampc/SecretNetwork/issues?q=is%3Aopen+is%3Aissue+label%3Abug)
and [implement CSPRNG key
derivation](https://github.com/enigmampc/SecretNetwork/issues/166). Tom did a
nice job [fixing the nonce in
encryption/decryption](https://github.com/enigmampc/SecretNetwork/issues/164)
by implementing a pseudo-random nonce in encryption/decryption (should be
deterministic).

Initially, we were using only `master_state_key`, but we managed to enable
[simple state
encryption/decryption](https://github.com/enigmampc/SecretNetwork/issues/178):

  * `read_db()` for wasmi
  * `write_db()` for wasmi

As part of `register_validator()`, we need to verify report signatures [on-
chain](https://github.com/enigmampc/SecretNetwork/issues/53) and [inside an
enclave](https://github.com/enigmampc/SecretNetwork/issues/54). We also
[implemented a connector to new remote attestation service (using API keys
instead of two-way
TLS)](https://github.com/enigmampc/SecretNetwork/issues/161).

## Generating Secret Contract IDs

 _Reuven went on a quest to_[ _investigate alternative algorithms for
generating secret contract
IDs_](https://github.com/enigmampc/SecretNetwork/issues/186) _: “One of the
issues we hit recently when thinking about key-derivation for the storage of
secret contracts was how to make sure a different key is derived for each
deployed contract. We reached the conclusion that the best option we have is
to derive the key from the hash of the WASM binary the enclave is executing.
This has the disadvantage that two contracts deployed with the same code will
end up using the same keys for their storage._

 _One of the ideas that came up is to generate the contract ID after running
the contract’s init, based on some data or properties that are unique to it
(maybe related to the signature of the deployer or using SGX randomness), and
then have the enclave sign the result.”_

After we managed to [fix bootstrap trust
issues](https://github.com/enigmampc/SecretNetwork/issues/181), our team
[generated a signed contract
ID](https://github.com/enigmampc/SecretNetwork/issues/200). Then, we [handled
encryption for inputs and outputs in CosmWasm
JS](https://github.com/enigmampc/SecretNetwork/issues/196). Along with that,
our dev team had to fix a bunch of things in order to match our finished
[encryption specs](https://github.com/enigmampc/SecretNetwork/issues/195). For
example, in state encryption, we [fixed contract_id &
field_name](https://github.com/enigmampc/SecretNetwork/issues/219). The name
`contract_id` __ was renamed to __`contract_key`, which needs to be derived
and used in a secure manner, so `field_name` __ can now be encrypted.

Finally, our team successfully managed to achieve [**stateful contract
execution in SGX (with
encryption)**](https://github.com/enigmampc/SecretNetwork/issues/39) **.**
This particular GitHub issue is almost the same as
[#38](https://github.com/enigmampc/SecretNetwork/issues/38) from Milestone 2,
except with a secret contract that has state. We had to define more ins and
outs between the enclave and the CosmWasm Rust and Go components.

 **Now, we have an encrypted version of**[ **get_state and
set_state**](https://github.com/enigmampc/SecretNetwork/issues/57) **from
CosmWasm.** This should overlay the existing implementation of CosmWasm as
much as possible. The complexity is in actually navigating between running
contracts inside of the enclave, plus actually storing and fetching data that
lives outside of the enclave (in the untrusted part of the validator).

## [Read the Full Encryption
Specs](https://build.scrt.network/protocol/encryption-specs.html)

![](https://miro.medium.com/max/1400/0*HudnK5EIi9ZvEZUW.png)

# What does this mean for developers?

Just imagine all the possibilities! You might have heard us talk about
sustainable growth and usability of privacy solutions. Now you can build
CosmWasm secret contracts and help with testing as we prepare to upgrade
Secret Network later this year — hopefully in the fall. There are many
potential use cases for truly decentralized applications which enable app
developers to use encrypted data without revealing a user’s personal
information.

You can get started by reviewing our evolving
[documentation](https://build.scrt.network). Any feedback would be much
appreciated! We have a [guide](https://build.scrt.network/dev/contract-dev-
guide.html) for setting up your dev environment for building CosmWasm smart
contracts. Let us know if you are interested in working on a demo app. Also,
if you haven’t already, please join our new [Secret
Chat](https://chat.scrt.network) and [Secret
Forum](https://forum.scrt.network) to talk with the Enigma team and Secret
Network community of validators and developers. You’re also welcome to share
information about your experience by filling out this [brief
survey](https://airtable.com/shrUfQrmQp6QAP7sm).

# What does this mean for validators?

The next step after further internal testing of secret contracts is the launch
of the **Secret Games:** an exciting period of network testing and development
for Secret Network! As part of this, there will be an **incentivized testnet**
for validators, with more information on this shared in the coming days.
(Watch the[ Secret Network blog!](http://blog.scrt.network)) If you are
interested in participating in this testnet, please fill out [this
form](https://airtable.com/shrBVxhT82kZxZ91L)!

[ **Secret Games Interest Form**](https://airtable.com/shrBVxhT82kZxZ91L)

In the future, as secret contracts are introduced on mainnet, the network will
need to be upgraded to add the `compute` module. That requires active
participation by all the node operators who support [Secret
Network](https://scrt.network). Validators will also have to register machines
equipped with secure enclaves.

Keep track of the state of Secret Network and on-chain proposals using your
choice of block explorer: [Secret Explorer](https://explorer.cashmaney.com),
[SecretScan](https://secretscan.io) or
[Puzzle](https://puzzle.report/enigma/chains/enigma-1).

# What does this mean for everyone?

As we know, privacy is a fundamental human right. Now all kinds of developers
have a more accountable solution for privacy-preserving computation. Secret
Network is designed to enable new kinds of solutions with encryption services
built on a distributed network of secret nodes. This offers developers a
practical and interoperable way to protect sensitive data in their
applications, giving users the power to control how their valuable information
is used and shared.

 **Let’s work to build privacy-first solutions with unique capabilities,
empowering people to create more useful systems for humanity.**

 _Assaf Morami — Enigma Dev Team_

![](https://miro.medium.com/max/1400/1*1kydiFy8MJU-Fp16vT_zZw.png)

 _To discuss Secret Network and join our community, visit our official
channels:  
_[Forum](https://forum.scrt.network/) |
[RocketChat](https://chat.scrt.network/) |
[Twitter](https://twitter.com/SecretNetwork) |
[Telegram](https://t.me/scrtnetwork) |
[Discord](https://blog.enigma.co/enigma.co/discord)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fenigmampc%2F3610fd739502&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fsecret-
contracts-update-milestone-3-of-3-is-
complete-3610fd739502&user=Assaf+Morami&userId=8475b3eaa650&source=-----3610fd739502
---------------------clap_footer-----------)

\--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fenigmampc%2F3610fd739502&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fsecret-
contracts-update-milestone-3-of-3-is-
complete-3610fd739502&user=Assaf+Morami&userId=8475b3eaa650&source=-----3610fd739502
---------------------clap_footer-----------)

\--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fenigmampc%2F3610fd739502&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fsecret-
contracts-update-milestone-3-of-3-is-
complete-3610fd739502&user=Assaf+Morami&userId=8475b3eaa650&source=-----3610fd739502
---------------------clap_footer-----------)

\--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F3610fd739502&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fsecret-
contracts-update-milestone-3-of-3-is-
complete-3610fd739502&source=--------------------------bookmark_footer-----------)

## [More from Enigma](https://blog.enigma.co/?source=post_page-----
3610fd739502--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Fenigmampc%2F3610fd739502&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fsecret-
contracts-update-milestone-3-of-3-is-
complete-3610fd739502&collection=Enigma&collectionId=6cb5d792f282&source=post_page
-----3610fd739502---------------------follow_footer-----------)

Official Blog of Enigma - Securing the Decentralized Web.

[Read more from Enigma](https://blog.enigma.co/?source=post_page-----
3610fd739502--------------------------------)

## Recommended from Medium

[[![YJ
Kim](https://miro.medium.com/fit/c/40/40/0*30k2oV4FAQLGTale)](https://medium.com/@quinn.kim?source=post_internal_links
---------0----------------------------)

[YJ Kim

](https://medium.com/@quinn.kim?source=post_internal_links---------
0----------------------------)

## Square 4) Recap on School projects I’ve done in last two years

](https://medium.com/@quinn.kim/square-4-recap-on-school-projects-ive-done-in-
last-two-years-ac0aeca2f92f?source=post_internal_links---------
0----------------------------)

[[![Maddy
King](https://miro.medium.com/fit/c/40/40/1*wuWPHlBMrozOdqut15ptXA.jpeg)](https://medium.com/@maddy.king?source=post_internal_links
---------1----------------------------)

[Maddy King

](https://medium.com/@maddy.king?source=post_internal_links---------
1----------------------------)

in

[Enspiral Dev Academy

](https://medium.com/enspiral-dev-academy?source=post_internal_links---------
1----------------------------)

## Tech is right for you and for me.

![](https://miro.medium.com/focal/112/112/50/50/1*SVyBIlRRRQvHdnELzjmUJQ.png)](https://medium.com/enspiral-
dev-academy/tech-is-right-for-you-and-for-
me-8460c5a9adeb?source=post_internal_links---------
1----------------------------)

[[![Gavin
Austin](https://miro.medium.com/fit/c/40/40/1*zzvnakOKULH3GvRoawH1_A.png)](https://gavinaustinsays.medium.com/?source=post_internal_links
---------2----------------------------)

[Gavin Austin

](https://gavinaustinsays.medium.com/?source=post_internal_links---------
2----------------------------)

## A Writer’s Guide to Surviving Agile Software Development

![](https://miro.medium.com/focal/112/112/50/50/1*n0_EfgiQ5_SftowS5uKVHA.png)](https://gavinaustinsays.medium.com/a-writers-
guide-to-surviving-agile-software-
development-67d84d25dc4e?source=post_internal_links---------
2----------------------------)

[[![Hasanain
Alsabonchi](https://miro.medium.com/fit/c/40/40/1*gTS4rf5LKMktyclbMd59xA.jpeg)](https://medium.com/@hsadeveloper?source=post_internal_links
---------3----------------------------)

[Hasanain Alsabonchi

](https://medium.com/@hsadeveloper?source=post_internal_links---------
3----------------------------)

## Add Two Linked List Numbers

![](https://miro.medium.com/focal/112/112/50/50/1*RkwLaBRGu5s5Naf_4U7aaw.png)](https://medium.com/@hsadeveloper/add-
two-linked-list-numbers-125b3f63736c?source=post_internal_links---------
3----------------------------)

[[![Hyejung
Lim](https://miro.medium.com/fit/c/40/40/1*_9gz83zQWFd10F1mn748uQ.jpeg)](https://medium.com/@aspynlim?source=post_internal_links
---------4----------------------------)

[Hyejung Lim

](https://medium.com/@aspynlim?source=post_internal_links---------
4----------------------------)

## [1–1–1] Setting-up a Single Node Hadoop Cluster

![](https://miro.medium.com/focal/112/112/50/50/1*8h2nJlgZ12ivKoOf_daP_g.png)](https://medium.com/@aspynlim/1-1-1-setting-
up-a-single-node-hadoop-cluster-d981bc3d5196?source=post_internal_links
---------4----------------------------)

[[![ReapMind
Innovations](https://miro.medium.com/fit/c/40/40/1*Ti7A_v5JTYdAxmCwMdIClg.png)](https://reapmind.medium.com/?source=post_internal_links
---------5----------------------------)

[ReapMind Innovations

](https://reapmind.medium.com/?source=post_internal_links---------
5----------------------------)

## How Much Does It Cost To Make A Mobile App?

![](https://miro.medium.com/focal/112/112/50/50/0*HElfEXQt3vM__T4e)](https://reapmind.medium.com/how-
much-does-it-cost-to-make-a-mobile-app-6db208350647?source=post_internal_links
---------5----------------------------)

[[![Sophie
Ha](https://miro.medium.com/fit/c/40/40/1*hvKzExLkA0Gmgjffu_cJQg.png)](https://medium.com/@hays_37127?source=post_internal_links
---------6----------------------------)

[Sophie Ha

](https://medium.com/@hays_37127?source=post_internal_links---------
6----------------------------)

in

[APISplatform

](https://medium.com/apisplatform?source=post_internal_links---------
6----------------------------)

## Innovative incentive system of APIS(APIX), Early bird’s 7th round is
starting soon!

![](https://miro.medium.com/focal/112/112/50/50/1*E1I5v3zPzp_Xz3tTHsMeUQ@2x.jpeg)](https://medium.com/apisplatform/innovative-
incentive-system-of-apis-apix-early-birds-7th-round-is-starting-
soon-18c86bc0db85?source=post_internal_links---------
6----------------------------)

[[![Angel
Ruiz](https://miro.medium.com/fit/c/40/40/1*oVdAKkh1da4dHA4pu2kRKg.jpeg)](https://jangunru.medium.com/?source=post_internal_links
---------7----------------------------)

[Angel Ruiz

](https://jangunru.medium.com/?source=post_internal_links---------
7----------------------------)

## VI, understanding the basics.

![](https://miro.medium.com/focal/112/112/50/50/0*ts7tI3RXwCw2qYlM)](https://jangunru.medium.com/vi-
understanding-the-basics-96bb7d9dcedc?source=post_internal_links---------
7----------------------------)

[](https://medium.com/?source=post_page-----
3610fd739502--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
3610fd739502--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
3610fd739502--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
3610fd739502--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
3610fd739502--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----3610fd739502--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----3610fd739502--------------------------------)

[Get
started](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fsecret-
contracts-update-milestone-3-of-3-is-complete-3610fd739502&source=post_page
--------------------------nav_reg-----------)

[![Assaf
Morami](https://miro.medium.com/fit/c/176/176/1*JXIPOovEEjz8_2R6KhagFQ.png)](https://medium.com/@assafmo)

[

## Assaf Morami

](https://medium.com/@assafmo)

7 Followers

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F8475b3eaa650&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fsecret-
contracts-update-milestone-3-of-3-is-
complete-3610fd739502&user=Assaf+Morami&userId=8475b3eaa650&source=post_page-8475b3eaa650
-------------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fusers%2F8475b3eaa650%2Flazily-
enable-writer-
subscription&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fsecret-
contracts-update-milestone-3-of-3-is-
complete-3610fd739502&user=Assaf+Morami&userId=8475b3eaa650&source=--------------------------subscribe_user-----------)

## More from Medium

[[![sallygu.eth](https://miro.medium.com/fit/c/40/40/1*hj-E9Wb_8DYVwXglnEgXFQ@2x.jpeg)](https://medium.com/@sally_gu?source=read_next_recirc
---------0---------------------709e198b_9a1c_4ccf_96e2_5a9698cb3a61-------)

[sallygu.eth

](https://medium.com/@sally_gu?source=read_next_recirc---------0
---------------------709e198b_9a1c_4ccf_96e2_5a9698cb3a61-------)

## How does oracle make Web3 a better place?

![](https://miro.medium.com/focal/112/112/50/50/0*rItQN43mLObaUjdA)](https://medium.com/@sally_gu/how-
does-oracle-make-web3-a-better-place-32fa93d4c21e?source=read_next_recirc
---------0---------------------709e198b_9a1c_4ccf_96e2_5a9698cb3a61-------)

[[![Eugene
Zaid](https://miro.medium.com/fit/c/40/40/1*YhG5G7oG8BYFBEvQmSoNXw.jpeg)](https://medium.com/@eugene.zaid?source=read_next_recirc
---------1---------------------709e198b_9a1c_4ccf_96e2_5a9698cb3a61-------)

[Eugene Zaid

](https://medium.com/@eugene.zaid?source=read_next_recirc---------1
---------------------709e198b_9a1c_4ccf_96e2_5a9698cb3a61-------)

## Continuing my exploration of the #dlt technologies and smart contracts, I
stumbled across the AWS…

![AWS Managed
Blockchain](https://miro.medium.com/focal/112/112/50/50/1*GkSRx1t_ZY8rBzGBdddJFQ.jpeg)](https://medium.com/@eugene.zaid/continuing-
my-exploration-of-the-dlt-technologies-and-smart-contracts-i-stumbled-across-
the-aws-4fae8ad43d39?source=read_next_recirc---------1---------------------
709e198b_9a1c_4ccf_96e2_5a9698cb3a61-------)

[[![JaviWalk](https://miro.medium.com/fit/c/40/40/1*GeLKsWfO-8i5B6T8ngYgnw.jpeg)](https://medium.com/@JaviWalk?source=read_next_recirc
---------2---------------------709e198b_9a1c_4ccf_96e2_5a9698cb3a61-------)

[JaviWalk

](https://medium.com/@JaviWalk?source=read_next_recirc---------2
---------------------709e198b_9a1c_4ccf_96e2_5a9698cb3a61-------)

## So… What are ‘cryptocurrencies’ anyway?

![](https://miro.medium.com/focal/112/112/50/50/1*O1v6nISWvkZLKuiQ3UMxjQ.jpeg)](https://medium.com/@JaviWalk/so-
what-are-cryptocurrencies-anyway-f373e68e48e2?source=read_next_recirc---------
2---------------------709e198b_9a1c_4ccf_96e2_5a9698cb3a61-------)

[[![Julian Voelkel](https://miro.medium.com/fit/c/40/40/1*PKSq6EWa1eQzcPYn-
Yy7TQ.jpeg)](https://julianvoelkel.medium.com/?source=read_next_recirc
---------3---------------------709e198b_9a1c_4ccf_96e2_5a9698cb3a61-------)

[Julian Voelkel

](https://julianvoelkel.medium.com/?source=read_next_recirc---------3
---------------------709e198b_9a1c_4ccf_96e2_5a9698cb3a61-------)

in

[51nodes

](https://medium.com/51nodes?source=read_next_recirc---------3
---------------------709e198b_9a1c_4ccf_96e2_5a9698cb3a61-------)

## Improving Scalability and Privacy of Blockchains: 2022 Update on Zero-
Knowledge Proofs

![](https://miro.medium.com/focal/112/112/50/50/1*qRkIBiGxEcgEpM46BzBLQA.png)](https://medium.com/51nodes/improving-
scalability-and-privacy-of-blockchains-2022-update-on-zero-knowledge-
proofs-2d90615f0dd?source=read_next_recirc---------3---------------------
709e198b_9a1c_4ccf_96e2_5a9698cb3a61-------)

[Help

](https://help.medium.com/hc/en-us)

[Status

](https://medium.statuspage.io)

[Writers

](https://about.medium.com/creators/)

[Blog

](https://blog.medium.com)

[Careers

](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e)

[Privacy

](https://policy.medium.com/medium-privacy-policy-f03bf92035c9)

[Terms

](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f)

[About

](https://medium.com/about?autoplay=1)

[Knowable

](https://knowable.fyi)

