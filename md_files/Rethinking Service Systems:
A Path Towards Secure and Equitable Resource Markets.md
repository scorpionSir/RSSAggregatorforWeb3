[ ![NuCypher](https://blog.nucypher.com/content/images/2019/03/NuCypher-blu-
whi.png) ](https://blog.nucypher.com)

  * [Blog](https://blog.nucypher.com/)
  * [Website](https://www.nucypher.com/)
  * [Documentation](https://docs.nucypher.com/en/latest/)
  * [GitHub](https://github.com/nucypher)

[ ](https://twitter.com/nucypher "Twitter")

Subscribe

# Rethinking Service Systems: A Path Towards Secure and Equitable Resource
Markets

  * [ ![Ghada Almashaqbeh](/content/images/size/w100/2020/07/profile-3.jpg) ](/author/ghada/)

#### [Ghada Almashaqbeh](/author/ghada/)

Jul 29, 2020 • 7 min read

![Rethinking Service Systems:

A Path Towards Secure and Equitable Resource
Markets](/content/images/size/w2000/2020/07/3ade1335-871c-4d19-b3f0-c7f4c6b83fcf-1.jpg)

Net neutrality, equitable and monopoly-free ecosystems, decentralization and
transparency, privacy and anti-censorship — these are some of the slogans we
carry around when we think about the future of the Internet and its digital
services. We dream of flexible systems that allow anyone, from anywhere, to
obtain or provide a service without any pre-identification. We even imagine
decentralized resource markets in which computing services are exchanged for
payments.

The pursuit of this dream started a long time ago with the development of
peer-to-peer (P2P) networks. [BitTorrent](https://www.bittorrent.com/) is a
prime example, enabling peers (or end users) to distribute content to each
other without any mediator. Ambitious technologists started to think of ways
to utilize this architecture to provide other types of services, like file
storage and access control, with the goal of disrupting the traditional
centralized infrastructure-based paradigm.

Cryptocurrencies and blockchain technology have accelerated this trend by
providing a decentralized payment mechanism to reward service providers, and
an append-only log to audit system operation. In fact, the circular dependency
here is ironic; cryptocurrencies and their blockchains are basically P2P-based
systems that are useful in building P2P-based resource markets.

To succeed in realizing this dream, we need to build secure and efficient
large-scale systems. This cannot be done in an ad-hoc way. Instead, aspects of
secure systems design, distributed services, applied cryptography, and
economics need to be invoked. Towards this goal, we present a generic
framework for building distributed resource markets, and discuss the security
and performance challenges in building such markets along with potential
solutions.

## Distributed Resource Markets - A Myth or Reality

Are decentralized ecosystems that allow participants to trade resources
_securely and efficiently_ already a reality? Assuming that security and
performance requirements are satisfied, can these ecosystems be financially
efficient enough to achieve wide adoption?

The answer is yes _and_ no!

Bitcoin, Ethereum, and other widely used cryptocurrencies are some examples of
successful systems in which miners (or peers) trade computation, storage, and
bandwidth power for mining rewards and transaction fees. Other initiatives
have more recently attempted to build decentralized services on top of these
cryptocurrencies with the goal of replacing other infrastructure-based
services (see the table below).

Service Type | Traditional Solution | P2P-based Solution  
---|---|---  
Key management | [Azure Key Vault](https://azure.microsoft.com/en-
us/services/key-vault/) | [NuCypher](https://www.nucypher.com/)  
File storage | [Dropbox](https://www.dropbox.com/) |
[Filecoin](https://filecoin.io/)  
Content distribution | [Akamai](https://www.akamai.com/) |
[CacheCash](https://academiccommons.columbia.edu/doi/10.7916/d8-kmv2-7n57)  
Video Transcoding | [Amazon Elastic
Transcoder](https://aws.amazon.com/elastictranscoder/) |
[Livepeer](https://livepeer.org/)  
  
Although most of these initiatives are still early stage, with a multitude of
unknowns regarding the go-to-market strategy of Web 3.0 and its applications,
we can still see a glorious future ahead.

## A Paved Way Ahead of Us?!

Unfortunately, _no_! The permissionless, open access environment of P2P
networks (i.e., allowing anyone to join and dealing with untrusted
participants) introduces many security and performance issues. Will these
peers be "available" when needed to provide the service? Can they be "trusted"
to provide the correct service? How will financial incentives shape the
behaviors of these peers? Will it be more profitable to attack or protect the
system? Will added security harm the system's efficiency and scalability?

All these questions need to be addressed before having successful deployment
and practical adoption.

## A Design Framework for Distributed Resource Markets

The framework is a list of distilled steps based on our own experiences in
blockchain-based systems design. Like any scientific design procedure,
iteration and customization would be needed based on the task at hand.

![](https://blog.nucypher.com/content/images/2020/07/design-steps.jpg)

**_Viability Assessment._** Before looking into building a distributed
resource market, one has to assess its viability. This includes studying
demand side (who is interested in the service) and supply side (who can
provide the service) to answer several questions; Are there tangible
advantages to encourage customers to replace traditional solutions with fully
distributed ones? Does providing the service require special machines or large
amounts of resources that exceed the capabilities of the average end-user?
Such a viability study is an important step in assessing the potential for
practical adoption before investing time and effort into designing the system.

 _ **Threat Modeling.**_ Despite the many advantages they offer —
decentralization, transparency, and lowered service costs — there is still a
big gap between the promise of P2P-based systems and their performance in
practice. Adding monetary incentives, by using another P2P-based payment
service, widens this gap. This is due to the perception that these systems are
not secure, where the recent large number of [security
breaches](https://www.investopedia.com/news/largest-cryptocurrency-hacks-so-
far-year/) give credence to these doubts.

The best practice for designing a secure system requires a threat modeling
step to investigate potential security risks. Such a model can guide designers
in deploying the proper countermeasures, and evaluating the security level of
a system. For resource markets, building a threat model requires a framework
that can handle large-scale distributed systems, explicitly account for the
financial motivations of the attackers, and help in spotting any potential
collusion between these attackers. An example of such a framework is
[ABC](https://arxiv.org/pdf/1903.03422.pdf) which is geared towards
cryptocurrency-based models and managing the complexity of the threat spaces.

**_Unique Aspects of Operating a Distributed Market._** _ ****_ Operating in a
flexible open access environment comes at a cost. Dealing with untrusted
parties means that [fair exchange is
impossible](http://www.cs.technion.ac.il/users/wwwb/cgi-bin/tr-
get.cgi/1980/CS/CS0175.pdf), which raises the question of when to pay servers
- before or after providing the service? If paid first, a malicious server may
not serve the customer; if served first, a malicious customer may not pay
after obtaining the service.

Furthermore, accounting attacks, in which participants collude with each other
pretending that the service has been delivered, could be a hammer that
destroys the market. This is particularly a problem in systems that require
sponsoring service requests. For example, in content distribution, a publisher
(e.g., Netflix) can hire caches (or servers) to distribute content to its
clients. Servers and clients may collude so that clients pretend to be served,
allowing servers to collect payments from the publisher (the sponsor) for
free.

The above security issues (and many others depending on the service type)
require a careful design of a decentralized service-payment exchange protocol
that can reduce the risks of dealing with untrusted, possibly colluding
parties. Such a protocol represents the _backbone_ of the resource market; if
it fails, the whole market fails! Servers will not be willing to participate
if they are not being paid. The same holds true for customers — they will not
be willing to use the system if they pay for a service that they do not
receive.

Operating such a market also requires devising mechanisms for service pricing,
term negotiation for server recruiting, and matching protocols to match these
servers with interested customers.

 ** _Financial and Cryptographic Security Measures._** Usually, security
threats are addressed via cryptographic means (e.g., encryption and digital
signatures), or algorithmic approaches (e.g., ordering the actions in a way
that enforces secure behavior). Monetary-incentivized systems introduce new
types of attacks that cannot be addressed using conventional approaches. In
particular, having financially-motivated attackers requires addressing certain
types of threats using financial techniques. These fall into two categories:
detect-and-punish mechanisms, where parties are required to lock penalty
deposits that are forfeited if they are caught cheating, and designing
algorithms that, if performed maliciously, require larger amounts of resources
than when performed honestly. Such techniques make cheating unprofitable, so
that rational parties will choose to act in an honest way.

For example, to reduce the risks of the impossibility of fair exchange,
micropayments are usually employed. That is, instead of paying a large chunk
of money for the full service, payment is divided into _small_ values, each of
which is exchanged for a _small_ service amount. For instance, one can pay to
retrieve a file in small data chunks instead of paying for the full file all
at once. Thus, a server loses only a small payment if a client does not pay
for a chunk retrieval. Similarly, a client loses only a small payment if it
pays in advance and the server does not send the data chunk in return.

On the other hand, to thwart accounting attacks, system designers need to
incorporate suitable techniques that prove or confirm resource expenditure,
and consequently, confirm that payments are well deserved. In file storage,
for example, [proof-of-spacetime](https://eprint.iacr.org/2016/035.pdf) can be
used to prove that a server is still storing the clients’ files.

It should be noted here that there is " _no one solution fits all_." Some
services may not need high payment frequency of micropayments; the amount of
service is already small and each client may send a few requests in any time
period. Also, each service may require a different resource expenditure
confirmation technique. Furthermore, which threat mitigation technique to
deploy may depend on the operational stage of the network (i.e., early stages
when the goal is encouraging adoption vs. later mature network operation).

_**Optimize for Efficiency.**_ Although designing a secure system is the
ultimate goal, efficiency is an important driving factor of the viability of
practical adoption and deployment. Hence, system designers need to exploit any
opportunity that allows for optimizing performance. This also involves
choosing the right trade-off between security and efficiency in the sense of
risk management. That is to say, threats that have high impact need to be
prioritized over low impact ones. Moreover, looking into alternative
cryptographic primitives that are lightweight (or optimizing their
implementation) while maintaining the required security guarantees is another
effective venue to utilize.

Another important aspect is system scalability — whether it is in terms of
interactivity, amount of data exchanged between the participant, or the amount
of data logged on the blockchain. A prime example is employing [probabilistic
micropayment schemes](https://arxiv.org/pdf/1911.08520.pdf) or [payment
networks](https://en.wikipedia.org/wiki/Lightning_Network) to aggregate small
transactions used to pay for the service into few larger ones before
processing. Another example is batching client requests and replies together
to reduce interaction, or even batching work confirmations to reduce the
amount of data logged on the blockchain.

 _ **Testing and Deployment.**_ To prove the viability of the system,
conventional practices of prototyping, benchmarking, and controlled deployment
(aka testnets) can be used to evaluate both efficiency and resistance to
attacks before moving to production or mainnets. These also provide a starting
point to attract early adopters and test the system at a large scale. This
stage may inspire designers to revisit specific parts of the system for
further optimization based on the results of the conducted experiments, or
feedback from the community.

## The Path Forward - The Sky is the Limit

The emerging movement towards decentralized applications (or dApps) and
services highlights two facts; there is a wide passion for such a work
paradigm, and there is a need for decentralized versions of all digital
services/systems around us. Having a decentralized service (e.g., a file
storage network) that relies on a centrally-managed service (e.g., an access
control service) will imprint the whole system as centrally-managed.

The good news is that the sky is the limit when it comes to what we want to
build. The bad news is that the sky is also the limit, to some extent, when it
comes to the challenges we will face on the security, privacy, scalability,
and performance fronts. Thus, following a systematized design approach is a
key. We hope that the framework described here will provide a stepping stone
along this path.

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

