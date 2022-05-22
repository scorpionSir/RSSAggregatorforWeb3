[ NAKAMOTO ](https://nakamoto.com)

  * [Home](https://nakamoto.com/)
  * [Twitter](https://twitter.com/nakamoto)
  * [Contribute](https://nakamoto.com/contribute/)
  * [About](https://nakamoto.com/about/)

__

__

# What are the Key Properties of Bitcoin?

Jan 3, 2020  13 min read  [Jameson Lopp](/author/lopp/ "Jameson Lopp")

[ ![What are the Key Properties of
Bitcoin?](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)
](/what-are-the-key-properties-of-bitcoin/)

What is Bitcoin? Many have attempted to answer this question, but I believe
that our quest to do so is [doomed to continue in
perpetuity](https://www.coindesk.com/nobody-understands-bitcoin-thats-ok). The
continuing development of the protocol is where the cutting edge of research
into what Bitcoin is and discussion about what it should strive to be actually
occurs.

It can be tricky for newcomers to wrap their head around what sort of
proposals are more likely to be accepted for Bitcoin because there are plenty
of unwritten rules regarding protocol changes. Some of these rules are more on
the philosophical side, some are more on the engineering and security side,
and some are a blend of the two.

##  **Consensus, Not Command & Control**

There is no authority in Bitcoin - even the principles outlined in this
article are by no means authoritative, they are simply observations made by
myself and other ecosystem participants.

  * Bitcoin is a system that automates the continual discovery of consensus amongst its participants. It is machine consensus that enforces human consensus.
  * Consensus failures can destroy the whole system by causing loss of confidence in its reliability.
  * Consensus code should be ringfenced and rarely touched.
  * Protocol changes should not be forced upon users without their consent. That is, users should opt into changes rather than having to opt out.
  * As such, software clients should not update automatically, as that would take power away from users and put it in the hands of developers.
  * Due to the distributed nature of the network, it should not be assumed that every user is paying attention to protocol changes.

How do we make changes to the system? In order to change the consensus code we
must somehow achieve human consensus to change the rules of the system. The
Bitcoin Improvement Proposal process is [described
here](https://github.com/bitcoin/bips/blob/master/bip-0001.mediawiki). It's
not perfect, but consensus-building is a messy process.

Johnson Lau did a good job describing the different types of forks (means of
making machine consensus changes) [in this
post](https://lists.linuxfoundation.org/pipermail/bitcoin-
dev/2017-April/013985.html) and Paul Sztorc has [written at
length](https://www.truthcoin.info/blog/protocol-upgrade-terminology/) about
different levels of coercion that are possible with forks.

How have changes been made historically?

  * By [Satoshi decree](https://bitcointalk.org/index.php?topic=626.msg6490)
  * On-chain miner ‘voting’ ([BIP 16](https://github.com/bitcoin/bips/blob/master/bip-0016.mediawiki))
  * Flag day upgrade ([BIP 30](https://github.com/bitcoin/bips/blob/master/bip-0030.mediawiki))
  * IsSuperMajority (double threshold switchover) mechanism ([BIP 34](https://github.com/bitcoin/bips/blob/master/bip-0034.mediawiki), [BIP 65](https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki), [BIP 66](https://github.com/bitcoin/bips/blob/master/bip-0066.mediawiki))
  * Version Bits ([BIP 9](https://github.com/bitcoin/bips/blob/master/bip-0009.mediawiki))

Who gets to accept or reject proposed changes? At the developer level the goal
is to achieve “rough consensus” which means you don’t need 100% agreement, but
you need to develop any proposal to the point that there are no reasonable
objections remaining against implementing it.

How do we measure support for changes to the system? Developers will discuss
amongst themselves and other ecosystem participants who may be affected by a
proposal. Anyone who is paying attention to ongoing development efforts is
welcome to provide input via discussions on mailing lists, code repositories,
social media, etc.

Ultimately, the governance of the protocol does not occur via a well-defined,
top-down fashion. Rather, it [inverts traditional models of
governance](https://youtu.be/_IMzSCSeM68) via enforcement from the bottom up.

##  **Trust Minimization**

> “Bitcoin is P2P electronic cash that is valuable over legacy systems because
> of the monetary autonomy it brings to its users through decentralization.
> Bitcoin seeks to address the root problem with conventional currency: all
> the trust that’s required to make it work . Not that justified trust is a
> bad thing, but trust makes systems brittle, opaque, and costly to operate.
> Trust failures result in systemic collapses, trust curation creates
> inequality and monopoly lock-in, and naturally arising trust choke-points
> can be abused to deny access to due process.  
>  
> Through the use of cryptographic proof and decentralized networks Bitcoin
> minimizes and replaces these trust costs. With the available technology,
> there are fundamental trade-offs between scale and decentralization. If the
> system is too costly people will be forced to trust third parties rather
> than independently enforcing the system’s rules. If the Bitcoin blockchain’s
> resource usage, relative to the available technology, is too great, Bitcoin
> loses its competitive advantages compared to legacy systems because
> validation will be too costly (pricing out many users), forcing trust back
> into the system. If capacity is too low and our methods of transacting too
> inefficient, access to the chain for dispute resolution will be too costly,
> again pushing trust back into the system.”  
>  
> \- Greg Maxwell

Bitcoin developer Matt Corallo also[ wrote about the importance of this
property](http://bluematt.bitcoin.ninja/2017/02/28/bitcoin-trustlessness/):

> Of Bitcoin’s many properties, trustlessness, or the ability to use Bitcoin
> without trusting anything but the open-source software you run, is, by far,
> king. More specifically, interest in Bitcoin appears to almost exclusively
> derive from a desire to avoid needing to trust some third party or
> combination of third parties. This should hardly be news to anyone, but an
> understanding of exactly why this trustlessness is so important (and what
> forms it takes) is critical to building and upgrading Bitcoin technology.

Having a requirement for minimizing trust is a fundamental property that
enables many of the other principles covered in this post. These principles
can be understood as coming from and working towards a low-trust aim. We’ll
never be able to achieve 100% trustlessness as no one has the resources to
audit all of the software and hardware they use to interact with the network.
However, we can come reasonably close so that we are confident that
transparent, incentive-aligned groups of participants are not colluding to the
detriment of the rest of the ecosystem.

##  **Decentralization**

An open system such as Bitcoin will not retain the desired properties
described in this post if it becomes sufficiently centralized such that
aspects of the network can be controlled by individuals or cartels.
_Decentralization is the means, not the end_. By distributing power as widely
as possible we minimize the trust required in any single entity because we
know that no single entity can interfere with our use of the system.

> “ _A lot of people automatically dismiss e-currency as a lost cause because
> of all the companies that failed since the 1990's. I hope it's obvious it
> was only the centrally controlled nature of those systems that doomed them.
> I think this is the first time we're trying a decentralized, non-trust-based
> system._ ”  
>  
> \- [Satoshi
> Nakamoto](https://satoshi.nakamotoinstitute.org/posts/p2pfoundation/2/#selection-25.0-25.307)

There are many potential dimensions of centralization and they can be
[difficult to quantify](https://news.earn.com/quantifying-
decentralization-e39db233c28e):

  * Exchanges
  * Developers
  * Software clients
  * Mining pools
  * Mining hardware
  * Economically active nodes
  * General value ownership distribution
  * Percent of users who control their own private keys
  * Percent of users who audit the ledger with their own node

High centralization in any given metric isn’t necessarily a system killer, but
we should consider that a system is only as strong as its weakest point. As
such, any changes to the system should take care to avoid consolidating power
along any possible axis.

##  **Censorship Resistance**

No one should have the power to prevent others from interacting with the
Bitcoin network. Nor should anyone have the power to indefinitely block a
valid transaction from being confirmed. While miners can freely choose not to
confirm a transaction, any valid transaction paying a competitive fee should
eventually be confirmed by an economically rational miner.

##  **Pseudonymity**

No official identification should be required to own or use Bitcoin. This
principle strengthens the censorship resistance and fungibility of the system,
as it is more difficult to select transactions to consider “tainted” when the
system itself does not keep track of users. This principle can also be
extended to the realization that the system does not even require its users to
be human.

##  **Open Source**

Bitcoin client source code should always be open for anyone to read, modify,
copy, and share. Bitcoin’s value is built upon the transparency and
auditability of the system. The ability to audit any aspect of the system
ensures that we need not trust any specific entities to act honestly.
Ecosystem participants are incentivized to act honestly because they know they
will be penalized for misbehavior. If the code being used to interact with the
system can not itself be audited, then any audit functionality enabled by the
code becomes worthless.

##  **Open Collaboration**

While anyone is welcome to conduct research and development privately, any
attempts to make protocol changes, especially non-backwards compatible
changes, should occur in the open rather than behind closed doors. Bitcoin
belongs to humanity, thus it is important that proposed changes be open to
public comment. The Bitcoin Improvement Proposal process is the recommended
way to go about suggesting changes, though because no authority can enforce
that the process be followed, it’s not a requirement.

The issue of voluntary organization and the power dynamics that result from it
can result in the perception that specific people or groups are authorities,
but this is [an illusion of power.](https://blog.lopp.net/who-controls-
bitcoin-core-/)

##  **Permissionless**

No arbitrary gatekeepers should be able to prevent anyone from participating
on the network (as a transactor, node, miner, etc). This is a result of trust
minimization, censorship resistance, and pseudonymity.

##  **Legal Indifference**

Bitcoin should be unconcerned with the laws of nation states, just like other
Internet protocols. Regulators will have to figure out how to respond to the
functionality enabled by Bitcoin-powered technology, not the other way around.

##  **Fungibility**

Fungibility is an important property of sound money. If every user needed to
perform taint analysis on all the funds they received, then the utility of the
system would drop significantly.

All UTXOs should be equally spendable. Unfortunately this is not currently the
case, and there are services that track “tainted” UTXOs that are tied to
criminal activity. The side effect of this is that innocent users can get
caught up in seizure actions due to spending UTXOs that are only several hops
removed from a "tainted" UTXO.

Fungibility requires privacy; privacy comes from having a large set of users
amongst whom you can’t distinguish transaction ownership. There are,
unfortunately, [many known
threats](https://github.com/OpenBitcoinPrivacyProject/wallet-
ratings/blob/master/report-03/threat%20model.wiki) to the privacy of Bitcoin
users and as a result, Bitcoin in its current state is far from perfectly
fungible.

##  **Forward Compatibility**

Bitcoin supports signing transactions without broadcasting them; there is a
principle that any currently possible signed but not broadcast transactions
should remain valid and broadcastable. A good example of this are transactions
with nLocktime that are not valid for confirmation until after the time
specified by the transaction; this could be used for inheritance or other time
delayed purposes. There could be dangerous repercussions to changing this rule
- an unknowable number of unbroadcast transactions could become invalid. No
one wants to be responsible for destroying someone’s wealth because a rule
upon which a user was relying was pulled out from underneath them.

The fact that Bitcoin has stuck to this principle gives everyone confidence in
the protocol. Anyone can secure their funds by whatever scheme they dream up
and deploy it without needing permission. So long as they are following the
rules of the protocol, the worst that might happen is for nodes to stop
relaying certain transactions by default.

##  **Resource Minimization**

In order to keep verification costs low, block space is scarce. As such, it
should be expensive for anyone to consume a lot of block space. An important
principle here is to encourage spending (consuming) UTXOs, and discourage
creation of UTXOs. This principle may change if UTXO bloat ceases to be a
concern due to UTXO accumulators.

Validation should be cheap because it supports trust minimization if more
users can afford to audit the system; cheap validation also makes resource
exhaustion attacks expensive. Bitcoin provides the mechanism to reject
cheaply-produced invalid blocks quickly. This is the fundamental principle of
hash cash — force the attacker to pay dearly in order to create spam. By first
downloading the 80 byte block header, a node can obtain proof of work and
perform correct and fast validation before ever syncing the block’s
transactions.

We should also prioritize efficient use of block space by only storing the
minimum data required for validating complex operations rather than storing
and executing complex operations on the blockchain itself.

##  **Verification > Computation**

A subset of the resource minimization principle. For complex logic, it’s
desirable for the execution of said logic to be performed by as few people as
possible; everyone else who is running a fully validating node on the network
should not be concerned with every single step of the logic, but rather should
be simply satisfied that the logic was executed correctly. Correctness is more
important than completeness.

> ‘ _Use the blockchain for what the blockchain is good for._ ’  
>  
> — Andrew Poelstra

The greatest possible optimization for any system is to avoid performing
computation in the first place. Blockchains are good for storing timestamped
data for auditing purposes; storing a proof of computation that can be checked
by anyone who cares should suffice, as opposed to requiring every participant
to compute logic for transactions that don’t concern them.

##  **Convergence**

Any two Bitcoin clients, if they connect to a single honest peer, should
eventually converge on the same chain tip. As an example, [Bitcoin ABC broke
this principle](https://blog.bitmex.com/bitcoin-cash-abcs-rolling-10-block-
checkpoints/) by instituting a 10 block maximum chain reorganization rule. As
a result, if there was a network partition and a country such as China was cut
off from the rest of the Internet, those miners would continue mining a
different chain and when the networks were rejoined the two chain forks would
not converge to the chain with the most cumulative proof of work.

All transaction operations must be deterministic. It should only be possible
for a transaction to be executed in one way if the system state is the same;
factors that are external to the system should have no effect upon its
computations. Similarly, you should not have scripts that work in two
different ways in two different machines. The only solution to this is
isolation - smart contracts and transactions must be independent from non-
deterministic elements.

Protocol changes should not create the potential for transactions to be
invalidated by blockchain reorganizations. Not only should transaction
operations be deterministic, they should be stateless. For example, see the
[OP_BLOCKNUMBER proposal
](https://bitcointalk.org/index.php?topic=1786.msg22119)made in 2010.

Several people have proposed opcodes that might render a transaction invalid
after a reorg. The proposals are generally requested to be redesigned to be
always forward valid using the OP_CLTV design, but sometimes that's unwanted
or impractical and it's suggested that it might be acceptable to have an
opcode that encumbers a transaction for a hundred blocks similar to a coinbase
transaction or OP_CSV 100 blocks.

##  **Transaction Immutability**

Each additional block added to the chain after a given block should make it
far less likely that the given block will be orphaned by a chain
reorganization. While the protocol allows for arbitrary length chain
reorganizations, long reorgs would likely be disruptive as some software or
nodes may not be able to handle them gracefully. Also, reorganizations longer
than 100 blocks could be additionally disruptive due to causing spent coinbase
transactions to cease existing, effectively destroying value.

While there can technically be no guarantee of immutability, we can guarantee
that it becomes impractically expensive to reverse a transaction after it is
sufficiently buried under enough proof of work.

##  **Denial of Service Resistance**

It should not be possible for a remote peer to make a request to a Bitcoin
node that consumes an inordinate amount of resources. An example of
functionality that breaks this principle are the SPV bloom filters, which in
adversarial conditions can be used to eat up a lot of disk I/O on a target
peer by making them scan through a lot of block data. You can see many of the
DoS protection rules[
here](https://github.com/bitcoin/bitcoin/blob/v0.19.0/src/net_processing.cpp)
if you search for “misbehav” on the page. Actions that are considered harmful
are giving various scores and if a peer exceeds the max misbehavior score,
your node will disconnect to prevent further abuse.

##  **Race Condition Avoidance**

Race conditions occur when a system's behavior is dependent on the sequence or
timing of uncontrollable events. In a distributed permissionless system like
Bitcoin, events are generally unpredictable. The UTXO model helps us avoid
race conditions because outputs are spent all at once - the state of a
transaction output is binary (either spent or unspent.)

This is another reason why transactions should not have dependencies on the
system’s state; it can create race conditions and complexity when state
changes during a blockchain reorganization.

##  **Conservatism**

  * Money should be stable in the long run.
  * We should be conservative about making changes, both in order to minimize risk to the system, and to allow people to continue using the system in the way they see fit.
  * Users should not be expected to be highly responsive to system issues, thus we should be proactive and cautious in order to limit them!

What is conservatism really about? It’s how we ensure social scalability.

> The secret to Bitcoin’s success is that its prolific resource consumption
> and poor computational scalability is buying something even more valuable:
> social scalability.  
>  
> \- [Nick Szabo](https://unenumerated.blogspot.com/2017/02/money-blockchains-
> and-social-scalability.html)

The problem inherent to many systems operated by humans is that the rules of
the system may be applied arbitrarily or may be subject to change at someone
else’s whim. This results in systems being less reliable.

> When we can secure the most important functionality of a financial network
> by computer science rather than by the traditional accountants, regulators,
> investigators, police, and lawyers, we go from a system that is manual,
> local, and of inconsistent security to one that is automated, global, and
> much more secure.  
>  
> \- [Nick Szabo](https://unenumerated.blogspot.com/2017/02/money-blockchains-
> and-social-scalability.html)

##  **Incentive Alignment**

Bitcoin only works because the rules of the system create incentives for
participants to be honest. Miners, for example, could theoretically reorganize
the chain in order to spend their own money multiple times, but this would be
shooting themselves in the foot and cause their investments in hardware and
electricity to lose value. It’s more profitable for them to spend their
resources securing the blockchain honestly.

##  **Ossification**

There is a general belief that over time it will become more and more
difficult to make changes to the base protocol as the ecosystem grows. This is
because there will be fewer and fewer changes that are uncontroversial to the
wider variety of perspectives and incentives of the user base. As such, it
will be more likely that improvements will have to take place in other layers
built on top of Bitcoin.

##  **Unlikely Consensus Changes**

  * Increasing the total number of issued bitcoins beyond **21 million**. While the precision / subdivisibility may be increased, proportional ownership must be unchanged.
  * Any rule that adds required, explicit centralization. For example, a change requiring that all blocks be signed by some central organization.
  * [Demurrage](http://en.wikipedia.org/wiki/Demurrage_%28currency%29) (deletion or reassignment of coins judged to be “lost” or “unused”). It’s not possible to objectively say that the private key to a UTXO has been lost simply because it has not been spent after a certain period of time. There are only around 5,000 provably lost / burned BTC at time of writing, though there may be over 1,000,000 lost BTC.

##  **Conflicting Principles**

Fungibility (privacy) improvements that result in it becoming impossible to
audit the money supply are unlikely, as degrading auditability in return for
improved fungibility is a controversial trade-off.

It may be the case at some point that it will become desirable to render some
UTXOs unspendable in order to protect the network, such as P2PK funds that
could be [vulnerable to quantum
attacks](https://www2.deloitte.com/nl/nl/pages/innovatie/artikelen/quantum-
computers-and-the-bitcoin-blockchain.html). Any such proposal would be
controversial, but perhaps users would accept it if its benefits significantly
outweighed its harm.

Future-proof validity isn't guaranteed because the chain could be reorganized
prior to the coinbase transaction in which the value was originally created.
There is a 100 block coinbase maturity rule to help protect against such a
scenario, and mainnet rarely sees reorganizations more than one block deep at
time of writing.

Ultimately, one of the greatest causes of conflict in the Bitcoin ecosystem is
the fact that it can not be everything to everyone. To do so would be
Bitcoin’s downfall, as there are fundamental trade-offs between various
priorities, such as:

  * Optimizing for low cost of full system validation vs low cost of transacting
  * Optimizing for a feature-rich programming language vs a small attack surface

## Proceeding Together Apace  

> In order to enable users to continue to transact and trust in Bitcoin as
> they always have, the community of Bitcoin users must continue to enforce
> that changes happen only through consensus among the ever-broadening group.
> Conversely, in order to keep Bitcoin from stagnating unnecessarily, its
> community must be willing to form consensus around and make changes which
> help the system they wish to use without hurting others and make common-
> sense changes, whatever form they might take. Critically, this means that
> all changes which do not harm the utility of Bitcoin for any of its many
> use-cases, while helping others, should be made, wherever possible.  
>  
> \- Matt Corallo

[__](https://www.facebook.com/sharer.php?u=https://nakamoto.com/what-are-the-
key-properties-of-
bitcoin/)[__](https://twitter.com/intent/tweet?url=https://nakamoto.com/what-
are-the-key-properties-of-
bitcoin/&text=What%20are%20the%20Key%20Properties%20of%20Bitcoin%3F)[__](https://pinterest.com/pin/create/button/?url=https://nakamoto.com/what-
are-the-key-properties-of-
bitcoin/&media=&description=What%20are%20the%20Key%20Properties%20of%20Bitcoin%3F)[__](https://www.linkedin.com/shareArticle?mini=true&url=https://nakamoto.com/what-
are-the-key-properties-of-
bitcoin/&title=What%20are%20the%20Key%20Properties%20of%20Bitcoin%3F)[__](https://reddit.com/submit?url=https://nakamoto.com/what-
are-the-key-properties-of-
bitcoin/&title=What%20are%20the%20Key%20Properties%20of%20Bitcoin%3F)[__](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https://nakamoto.com/what-
are-the-key-properties-of-
bitcoin/&title=What%20are%20the%20Key%20Properties%20of%20Bitcoin%3F)[__](http://vk.com/share.php?url=https://nakamoto.com/what-
are-the-key-properties-of-
bitcoin/&title=What%20are%20the%20Key%20Properties%20of%20Bitcoin%3F)[__](https://getpocket.com/edit?url=https://nakamoto.com/what-
are-the-key-properties-of-
bitcoin/)[__](https://t.me/share/url?url=https://nakamoto.com/what-are-the-
key-properties-of-
bitcoin/&text=What%20are%20the%20Key%20Properties%20of%20Bitcoin%3F)

![Jameson
Lopp](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

#### Jameson Lopp

[Website](https://www.lopp.net) [Twitter](https://twitter.com/@lopp) [More
posts](/author/lopp/)

Cofounder & CTO of Casa. Creator of statoshi.info, bitcoin.page, and
lightning.how.

[__Previous Post](/credible-neutrality/)

[Next Post __](/bitcoin-becomes-the-flag-of-technology/)

### You might also like...

[ ![What will happen to cryptocurrency in the
2020s?](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)
](/crypto-in-the-2020s/)

##  [What will happen to cryptocurrency in the 2020s?](/crypto-in-the-2020s/)

Jan 5, 2020  7 min read

[ ![Bitcoin's P2P
Network](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)
](/bitcoins-p2p-network/)

##  [Bitcoin's P2P Network](/bitcoins-p2p-network/)

Dec 29, 2019  8 min read

[ ![Gnutella: an Intro to
Gossip](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)
](/gnutella/)

##  [Gnutella: an Intro to Gossip](/gnutella/)

Dec 29, 2019  11 min read

Please enable JavaScript to view the [comments powered by
Disqus.](https://disqus.com/?ref_noscript)

[ NAKAMOTO ](https://nakamoto.com)

__

