[ ![NuCypher](https://blog.nucypher.com/content/images/2019/03/NuCypher-blu-
whi.png) ](https://blog.nucypher.com)

  * [Blog](https://blog.nucypher.com/)
  * [Website](https://www.nucypher.com/)
  * [Documentation](https://docs.nucypher.com/en/latest/)
  * [GitHub](https://github.com/nucypher)

[ ](https://twitter.com/nucypher "Twitter")

Subscribe

# To Work, or Not to Work - Accountability in the NuCypher Network

  * [ ![Ghada Almashaqbeh](/content/images/size/w100/2020/07/profile-3.jpg) ](/author/ghada/)

#### [Ghada Almashaqbeh](/author/ghada/)

Aug 6, 2020 • 7 min read

![To Work, or Not to Work -  Accountability in the NuCypher
Network](/content/images/size/w2000/2020/08/ggg-2.jpg)

In the land of NuCypher, there is a set of characters: Alice, Enrico, Bob, and
Ursula. Currently, as one of the services that NuCypher provides, these
characters work together to implement a decentralized access control service
(or key management system).

In particular, Alice owns some data that is stored encrypted under her public
key on some storage network. Alice wants to go on a vacation - to unplug in
her own words. Enrico, her faithful honest friend, will continue to encrypt
Alice's data and disseminate it to the storage network. While being away,
Alice wants to give Bob some temporary access rights to this data. Not
unconditional access, instead she wants three conditions to be satisfied: The
storage network does not get to see the raw data, neither Bob nor the storage
network get a hold of the secret decryption key, and a given access policy
(specifying a duration and which data to access) must be enforced.

NuCypher land residents are fond of decentralized solutions. Thus, they
resorted to fancy cryptographic primitives (namely, [threshold proxy re-
encryption](https://github.com/nucypher/umbral-doc/blob/master/umbral-
doc.pdf)) and smart-contract based cryptocurrency
([Ethereum](https://ethereum.org/en/)) to build a service that will help Alice
in her quest. Alice can recruit Ursulas to convert a ciphertext under her
public key to a new ciphertext under Bob's public key. So after contacting
Ursulas, Bob obtains a ciphertext that only he can decrypt. All of this can be
done without any intervention from Alice! So she can enjoy her vacation
without blocking Bob.

## Free Labor?!

Ursula does not provide this service out of the kindness of her heart. She
collects payments for providing the re-encryption service from both Alice and
the NuCypher network. The former is a service fee (in Ether) that Alice pays
for each of her access policies that Ursula maintains, while the latter is a
subsidy from the network (newly minted NU tokens) — much like mining fees in
other cryptocurrencies.

The amount of payment is computed based on the availability of Ursula, the
number of policies she participates in, and the amount of stake she pledged
when joining the network. To confirm being online, every now and then, Ursula
has to invoke a function in one of the NuCypher smart contracts, confirming
that she is available to serve Bob's requests. It is an empty function call;
it does not require any proofs that Ursula was up or responsive to Bob during
the past period.

## To Work - or Not to Work - That is the Question!

As a self-interested player, Ursula may follow any strategy, even those that
deviate from the honest behavior, to maximize her financial profits. This
involves any technique that allows Ursula to save resources and collect the
full amount of payments as if she has expended the full amount of resources to
provide the re-encryption service.

Ursula realized that the current approach of confirming activity is flawed.
She can go offline, ignoring Bob's requests, and come online only to call the
confirm activity function, which again does not require submitting any proof
that Ursula was online and responsive during the past period.

Furthermore, the revenue computation (both fees and subsidy) is agnostic to
the number of requests Ursula serves. Thus, an active Ursula who may serve a
huge number of re-encryption requests, and one who does not receive any
requests (or more importantly, a malicious/lazy Ursula that does not answer
Bob’s requests), will both collect the same amount of revenue if they hold
identical policies.

Nonetheless, Ursula has an economic incentive to log her availability and
provide a satisfactory level of service. If she "cheats" she will risk
devaluing her stake since the network will be less useful to users who will
leave and cease paying fees. However, we recognize the long-term need for a
more intelligent and specialized technique to hold Ursula _accountable_ and
prevent her from cheating the system.

## Impact of Network Operation Stage

Recall that Ursula collects two types of payments: Subsidy and service fees.
Much like other cryptocurrencies, subsides will disappear later once all
NuCypher's NU tokens are minted. This leaves Ursula with only the service fees
as the source of income. We found that this change in financial incentives
affects which accountability (or confirm activity) technique we need to deploy
in order to enforce Ursula's honesty.

In the first 5 to 8 years after network launch, when subsidies will likely
dominate fees, we are concerned with the availability of Ursulas and their
willingness to serve all requests coming from Bob. In other words, regardless
of the number of requests served, the revenue total value (both subsidy and
fees) will be computed based on the length of time during which an Ursula is
online and well-behaved.

On the other hand, in later stages, when subsidies disappear, confirm activity
will be tied to providing the re-encryption service, in the sense that the
payment will be partially computed based on the amount of service provided.
This requires Ursula to confirm its activity by proving that she served a
given number of distinct re-encryption requests during a given period.

To make the distinction clear, we refer to the first as _confirm availability_
, and for the second as _confirm service activity_.

## Enforcing "To Work"

We introduce several solutions for both forms of confirming activity. These
solutions differ in the trust, security guarantees, interactivity, and
efficiency. We present these solutions briefly below, while a more detailed
and complete version can be found [here](https://github.com/nucypher/confirm-
activity-doc/blob/master/confirm-activity/confirm-activity-doc.pdf).

 ** _Confirm availability solution._** Here we use a detect-and-punish
approach embedded within an _optimistic service monitoring_ process. This
means that it is only invoked when Bob complains that an Ursula is
unresponsive. The proposed solution labels Ursulas as working Ursulas and
gateway Ursulas. The former are contacted in a regular way to handle the re-
encryption service, while the latter act as challengers that are contacted
only when there is a complaint from Bob - at which time they will attest
whether a working Ursula is indeed unavailable.

Hence, for each round, a set of Ursulas is selected at random to act as
gateways. Bob proceeds as usual by contacting a set of working Ursulas
recorded in Alice's policy for the re-encryption service. If a working Ursula
does not reply, Bob complains to a gateway Ursula and hands her the request.
This gateway challenges the working Ursula by forwarding the request again and
waiting for an answer. If one is received, the gateway forwards it to Bob and
closes the complaint.

On the other hand, meaning no response is received, the gateway notifies the
rest of the gateways selected for that round to repeat the same process. If no
response is received by any of them, the quorum [collectively
signs](https://www.usenix.org/conference/usenixsecurity16/technical-
sessions/presentation/kogias) a proof-of-unavailability against the working
Ursula and submits this proof to the NuCypher staking contract. Such a proof
will cause a portion of Ursula's stake to be slashed as a punishment.

 ** _Confirm service activity solutions._** Here we devise three solutions
that allow producing a proof attesting to the statement _"An Ursula has served
ω distinct requests correctly"_ for some positive integer ω representing the
number of served requests. These solutions are referred to as zero knowledge
proof-based (ZKP-based), committee-attestation, and commit/challenge/open-
based.

For the **ZKP-based approach** , we utilize the fact that in our network each
Ursula already produces a ZKP attesting to the correctness of each re-
encryption request she performs. Our solution is to aggregate the proofs of
all served requests within a round into one proof attesting to the above
statement. This accumulation can be done by using generic techniques like
[proof carrying data
(PCD)](https://people.eecs.berkeley.edu/~alexch/docs/CT10.pdf) or
[incrementally verifiable computation
(IVC)](https://link.springer.com/chapter/10.1007/978-3-540-78524-8_1).

An alternative, possibly more efficient approach, is to view the above
statement as an instance of arithmetic circuit satisfiability problem and
combine it with a highly efficient ZKP system, e.g.,
[Bulletproofs](https://eprint.iacr.org/2017/1066). That is, build a circuit
that takes the set of correctness proofs and their count _ω_ as inputs, and
outputs 1 if the number of correct distinct proofs equals to _ω_. Then, invoke
a circuit parser to convert the circuit into the bulletproof format, which
allows the prover (Ursula in this case) to produce a single proof. Ursula can
submit this proof to the network to claim her payments.

As for the **committee-attestation approach** , it shares a similar theme to
confirm availability solution mentioned previously. For each round, a
committee of Ursulas (and possibly outsider verifiers) is elected to attest
for the work load an Ursula served. In detail, the working Ursula sends all
Bob requests she served along with the correctness proofs to this committee.
After verifying all the proofs, the committee collectively signs the _"An
Ursula has served ω distinct requests correctly"_ statement, while replacing
_ω_ with the actual number of served requests. The committee (or the working
Ursula) submits the signed statement to the network so the working Ursula can
claim her payments.

Lastly, for the **commit/challenge/open approach** , we introduce a mechanism
inspired from the [Merkle tree-based ZKP
system](https://eprint.iacr.org/2019/650) proposed by Dottling et al. For each
round a working Ursula constructs a Merkle hash tree of all served requests
and their correctness proofs. Then, she uses the root as a random beacon to be
fed into an iterative hash process to select _n_ leaf nodes at random to open
them (i.e., these are the challenges). Ursula signs the Merkle tree root and
the activity proof will be composed of the signed root, the challenge leaf
nodes along with their openings, and membership paths of the challenge leaves.
Ursula sends this proof either to a sidechain (maintained by round-selected
committee) or to the main network to verify. Once verified, Ursula will be
rewarded with the service payment.

## Current and Future Plans

Which solution to adopt will be based on benchmark testing and the development
vision of the NuCypher network. The ZKP-based solution provides several
advantages including non-interactivity, as opposed to the committee-
attestation one that needs interaction with the committee. It also supports
computational soundness as opposed to the statistical one of the
commit/challenge/open solution. Nonetheless, it could be the case that the
other solutions are more efficient especially if we incorporate committee
attestation or sidechains to support other functionalities in the network.

Thus, for now we lay down all these solutions, and continue to explore more
creative techniques for the confirm activity problem, for the sake of
NuCypher's benefit as well as other decentralized, possibly related, projects
in the space. We also envision that some of the proposed techniques will be
useful for future services that the NuCypher network may provide. Our next
step will be looking into the implementation, testing, and adoption of these
techniques.

## Sign up for more like this.

Enter your email Subscribe

[ ![Developer Update - Abiotic Alice and DKG \(October
2021\)](/content/images/size/w600/2021/10/2021-10-13-10.46.21.jpg)
](/developer-update-october-2021/)

[

## Developer Update - Abiotic Alice and DKG (October 2021)

NuCypher's proxy re-encryption (PRE) service is leveling up. Recently, the
demand for access-conditioned content in Web3 has exploded: subscriptions,
streaming, private NFTs, NFTs as access tokens, the list goes on. Many of
those are building on NuCypher (soon Threshold!) and proxy re-encryption. For
example: Masterfile is building an enterprise NFT

](/developer-update-october-2021/)

  * [ ![MacLane Wilkison](/content/images/size/w100/2019/05/IMG_8077.jpg) ](/author/maclane/)

[MacLane Wilkison](/author/maclane/) Oct 13, 2021 • 3 min read

[

## NuCypher Community Update - September 2021

Once a month we'll be putting out community updates in the format of team
member interviews. September's update is an interview NuCypher's CTO, David
Nuñez.

](/september-nu-community-update/)

  * [ ![Ryan Caruso](/content/images/size/w100/2020/12/IMG_5522.JPG) ](/author/ryan/)

[Ryan Caruso](/author/ryan/) Sep 17, 2021 • 13 min read

[

## NuCypher + Keep: KEaNU AMA, Hosted by Staking Hub

Hey NuCypher and Keep community, here is the transcribed copy of the AMA
hosted by Figment's Staking Hub. Thanks to the hosts, the Nu + Keep team, and
those who asked questions from the community.

](/nucypher-keep-keanu-ama-hosted-by-staking-hub/)

  * [ ![Ryan Caruso](/content/images/size/w100/2020/12/IMG_5522.JPG) ](/author/ryan/)

[Ryan Caruso](/author/ryan/) Jun 28, 2021 • 9 min read

[NuCypher](https://blog.nucypher.com) (C) 2022

  * [Telegram](https://t.me/nucypher)
  * [Discord](https://discord.com/invite/7rmXa3S)
  * [Twitter](https://twitter.com/nucypher)

[Powered by Ghost](https://ghost.org/)

