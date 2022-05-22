[ ![Filecoin](../../../images/filecoin-logo.svg) ](../../../)

  * [Store](../../../store/)
  * [Provide](../../../provide/)
  * [Build](../../../build/)

    * Docs
    * Tools & services
    * Grants
    * Roadmap
    * Videos
    * Filecoin Community
    * Events

  * [Blog](../../../blog/)

Explore the Network

  * [Filfox.info](https://filfox.info/en)
  * [Filscan.io](https://filscan.io/#/tipset/chain)
  * [Filscout.io](https://filscout.io/en/)
  * [Spacegap](https://spacegap.github.io)
  * These explorers were built by community members and may have inaccuracies

[ EN ](../../../en) [ 中文 ](../../../zh-cn)

Category:

  *   *   * 

![](../../../images/icons/social/share.svg)

Aug 19, 2020  

## 30 Days, 130 Projects: Recognizing New Ideas to Power Web3

After a month of workshops, talks, AMAs, and heads-down building, 134 teams
submitted final projects for the inaugural [HackFS](http://hackfs.com/)
hackathon, unveiling amazing tools and services to drive the decentralized
web. In total, more than 470 hackers from 50 countries across 19 time zones
participated in this 30-day virtual event.

![HackFS Talks](https://filecoin.io/vintage/images/blog/hfs-talks-finale.jpg)

On August 18, ten finalists demonstrated their projects live in front of a
panel of judges: Protocol Labs Founder and CEO Juan Benet, IPFS Project Lead
Molly Mackinlay, Filecoin Product Lead Pooja Shah, and Ethereum Foundation’s
Ken Ng. You can watch the [full
session](https://www.youtube.com/watch?v=GibA0t0z_9w) and read more for a
recap of the submissions from the 10 finalist teams.

### Applications Category

#### [Sailplane](http://sailplane.io/)

#### ![Sailplane](https://filecoin.io/vintage/images/blog/hfs-sailplane-
finale.jpg)

Sailplane is a peer-to-peer file storage service, similar to Dropbox, in a web
app using IPFS and OrbitDB. It uses IPFS and a custom OrbitDB store for file
metadata and other file management functionality. The front-end is built on
React.js and has a custom browser-based user interface.

Sailplane uses IPFS to store, send, and reference data. A custom OrbitDB store
takes output from IPFS and creates a mutable file system-like structure from
it. This structure stores paths and file CIDs. When a user uploads a file or
folder to the website, it’s added to IPFS. The output is given to the OrbitDB
store which allows for mutating the structure and replicating changes across
devices. The website also allows for downloading that structure, whether it’s
a file or a folder, at a later time. Read more about Sailplane on the
[Filecoin blog](https://filecoin.io/blog/hackfs-teams-vol-3/) and [watch the
demo](https://www.youtube.com/watch?v=Agntk5_XME4&feature=youtu.be).

#### [Public Annotation Network (PAN) Protocol](https://late-
waterfall-9957.on.fleek.co/)

![PAN Protocol](https://filecoin.io/vintage/images/blog/hfs-pan-finale.jpg)

Public Annotation Network (PAN) is an open-source, web annotation service that
lets users annotate content on any web page and read annotations published by
others. There are two ways to submit annotations: users can either publish
annotations directly to our network or submit via a publisher, which will then
publish annotations in batches on behalf of the users.

Annotation data is stored on IPFS. For better compatibility with other
services, PAN adopts the [W3C’s Web Annotation Data
Model](https://www.w3.org/TR/annotation-model/). An Ethereum smart contract
registry is used to store references to each annotation and its annotator,
ensuring that annotation data is immutable. [Watch the
demo](https://www.youtube.com/watch?v=vtZKRGCjCz8).

#### [Pnlp](https://github.com/pnlp-network/pnlp) (pronounced “pulp”)

![Pnlp](https://filecoin.io/vintage/images/blog/hfs-pnlp-finale.jpg)

Pnlp is an open publishing platform for written content on Web3. Authors can
write and publish on the open web, assemble a following, and even receive
money from readers. Subscribers can browse the best writing on the open web
and support the authors they value most.

Pnlp uses its own identity module to generate libp2p identities from Ethereum
addresses, thereby connecting IPNS keyspace to Ethereum address space. The
browser application uses Textile Buckets, hosted on Textile Hub, to interact
with IPFS and IPNS. [Watch the
demo](https://www.youtube.com/watch?v=luzDPMhHepM&feature=youtu.be).

#### [BlockSig](https://hack.ethglobal.co/showcase/blocksig-recT3kpIaPtPKNek2)

![BlockSig](https://filecoin.io/vintage/images/blog/hfs-blocksig-finale.jpg)

BlockSig is a notarized document signing solution. A notary sends out a
document signing invite which, when accepted by involved parties, generates a
unique doc token. Transactions on the contract represent state updates
corresponding to each party adding their signature to the document. The
signing by the notary is the last step in the lifecycle once other parties
have confirmed their signatures. Upon finalization, the signature proof hashes
from each party are appended to the original document and the resulting
document persisted on IPFS as encrypted contents, and mailed to all parties.
An open-sourced verification tool reconstructs the expected proofs and checks
them against an uploaded file representing the finalized state. [Watch the
demo](https://www.youtube.com/watch?v=gxQs8_PLd8c).

### Infrastructure Category

#### [Valist](https://valist.io/)

![Valist](https://filecoin.io/vintage/images/blog/hfs-valist-finale.jpg)

Valist is a decentralized binary distribution project complete with software
notarization functionality. Valist allows developers and organizations to
register public credentials to securely publish and distribute software,
firmware, and arbitrary data to users. The idea is to leverage Ethereum, IPFS,
and ultimately Filecoin to create a public “base” layer for a simplified
binary repository that both integrates with traditional package management
systems and is built upon decentralized protocols. Smart contracts on Ethereum
manage the latest source of truth for binary data stored in another layer such
as IPFS and/or Filecoin. Clients can then query the software notary for the
latest version of some software and be pointed to a verifiable, decentralized
data store. [Watch the
demo](https://gateway.pinata.cloud/ipfs/QmPRzwgKNUsaByBvJsCoW2NfN7abzJdys1EVat5k3WiP2B).

#### [IPFS Recovery](https://github.com/Wondertan/go-ipfs-recovery)

![IPFS Recovery](https://filecoin.io/vintage/images/blog/hfs-ipfsrecovery-
finale.jpg)

IPFS Recovery is building a way for content to persist on IPFS despite damage
to data and the network at large. This project implements erasure coding in
IPFS by creating redundancies of data blocks in the IPLD DAG format. IPFS
Recovery uses [Reed-Solomon
codes](https://www.cs.cmu.edu/~guyb/realworld/reedsolomon/reed_solomon_codes.html)
as well as novel [Alpha Entanglement codes](https://medium.com/unitychain/an-
introduction-to-alpha-entanglement-codes-66a8835308c5) to achieve the end
result of greater resiliency for files stored on the IPFS network. The goal is
to build a modular framework where several kinds of erasure codes can be
added. Alpha entanglements in particular are interesting as they provide the
ability to create self-healing networks. [Watch the
demo](https://www.youtube.com/watch?v=1AkG-weUEmw&feature=youtu.be).

####
[PlanetFlare](https://docs.google.com/presentation/d/1GHygwl3ahQdJoQp6Ocb9Z0cGrsox0eQG5Luy_y-
Zd44/edit#slide=id.p)

![PlanetFlare](https://filecoin.io/vintage/images/blog/hfs-planetflare-
finale.jpg)

PlanetFlare is a platform creating a decentralized data retrieval marketplace
by enabling anyone with a computer to serve assets (akin to edge points on a
CDN) and getting paid for this service. Content publishers can host their
assets on PlanetFlare and bid for CDN availability by specifying pricing. The
open market drives the cost of content distribution down and enables CDNs to
be more globally distributed since the service does not need to be limited by
centralized server locations. [Watch the
demo](https://www.youtube.com/watch?v=ISwnh0dRdqw).

### Developer Tools Category

#### [Web3API](https://web3api.dev/)

![Web3API](https://filecoin.io/vintage/images/blog/hfs-web3api-finale.jpg)

“We built a Web3 WebAssembly (WASM) runtime for universally compatible smart
contract APIs,” explained team member Jordan Ellis. “This allows protocols to
implement user-friendly wrappers in a language-agnostic way.” These WASM
modules, paired with a subgraph for historical data querying, combine together
to create a single GraphQL schema that defines the entirety of the protocol,
which the team calls a “Web3API.”

Web3APIs live on IPFS and are addressable using the Ethereum Name Service
(ENS). They can be queried from any language or platform: Node, browser, C#,
C/C++, Rust, Go, Python, etc. Decentralized apps only need to include their
lightweight client to query any Web3 API. The end result: “We’re able to bring
smart contracts into APIs with blazing speeds,” Ellis said. [Watch the
demo](https://www.youtube.com/watch?v=C52siCNscpM).

#### [Decentralized Docker
Hub](https://github.com/viraja1/decentralized_docker_hub)

![Decentralized Docker Hub](https://filecoin.io/vintage/images/blog/hfs-ddh-
finale.jpg)

Decentralized Docker Hub, powered by Powergate, lets you push and pull Docker
images from IPFS and Filecoin. It also supports ENS domain names using an IPFS
hash of the docker image set as the content hash of your ENS domain. “I
decided to work on Decentralized Docker Hub because I believe that we need an
alternative to centralized Docker images,” said Viraj Anchan. “Relying on a
single, centralized source for docker images is risky because if an image gets
deleted then it will affect all your dependencies.” Decentralized Docker Hub
leverages IPFS hot storage and Filecoin for cold storage. [Watch the
demo](https://www.youtube.com/watch?v=c0AadtIJmYo).

#### [Pygate](https://pygate.tech/)

![Pygate](https://filecoin.io/vintage/images/blog/hfs-pygate-finale.jpg)

Pygate is a gateway to the Filecoin network and IPFS technology for
Pythonistas. While most tooling to date has been geared toward JavaScript and
Golang developers, the pygate team found that Python was overwhelmingly voted
the “most wanted” language in [Stack
Overflow’s](https://insights.stackoverflow.com/survey/2020) February 2020
survey of over 65,000 developers. The pygate team is helping to bring Filecoin
to this community by building interfaces and tooling for Textile’s Powergate
in Python. Pygate’s solution includes a Python API client, sample
applications, and more!

Read more about pygate [on the Filecoin blog](https://filecoin.io/blog/hackfs-
teams-vol-1/) and [watch the
demo](https://www.youtube.com/watch?v=G7jHfv4LdbM&feature=youtu.be).

### Protocol Labs Prizes

In addition to the 10 finalists, each HackFS sponsor awarded prizes to teams
that used their technology in novel ways. Protocol Labs recognized 8 projects
as winners of the Protocol Labs HackFS prizes.

🎉Congratulations to:

  * Secured Finance, winners of the **DeFi track**
  * Kotal, winners of the **Devtools track**
  * Watchdog DAO, winners of the **Datasets track**
  * IPFS-FPS, winners of the **Video track**
  * Cadbury, winners of the **Audio track**
  * FilecoinPricingMechanism (FPM), winners of the **Mining track**
  * Myel, winners of the **Networking track**
  * Web3API, winners of the **Smart Contracts track**

![Prizes](https://filecoin.io/vintage/images/blog/hfs-prizes-finale.jpg)

[Read more](https://hack.ethglobal.co/hackfs/showcase) about all of the HackFS
teams and their submissions. We’re really excited by the phenomenal work we
saw from these teams throughout the hackathon.

For those teams looking to further their projects built for the Filecoin
ecosystem, consider applying to some of our programs for developers:

  * [Filecoin DevGrants](https://filecoin.io/grants): The Filecoin DevGrants program awards grants to teams on a quarterly basis. We are currently accepting applications for Wave 5, and all are welcome to apply.
  * [Filecoin Launchpad Accelerator](https://labs.consensys.net/tachyon/): Throughout Fall 2020, between 15 and 20 teams will be provided twelve weeks of funding, mentorship, benefits, and programming around business and blockchain-specific issues, culminating in a Demo Day and post-program fundraising support. Teams leverage access to the ConsenSys and Protocol Labs networks and expertise, ranging from entrepreneurs and legal advisors to pathbreaking technical researchers. Each team will receive $80,000 USD in investment. Applications close on August 21st.
  * [Filecoin Apollo](https://gitcoin.co/blog/apollo/): Protocol Labs + Gitcoin are opening our doors for the Ignite Incubator. It is a 6-week, invite-only program designed for Filecoin entrepreneurs and makers to help them build investable businesses. There will be opportunities for 150+ highly talented builders together to become pioneers of the Filecoin and Web3 ecosystems.

You can keep up with events for the Filecoin community by heading over to the
[Filecoin project on GitHub](https://github.com/filecoin-project) and by
checking out the [community resources](https://github.com/filecoin-
project/community). And stay connected on [Filecoin
Slack](https://filecoin.io/slack).

Onwards!

### Related Articles

[View all articles](../../../blog)

[ ](../../../blog/posts/meet-the-hackfs-teams-vol.1/)

updates

##  [ Meet the HackFS Teams Vol. 1: Omo Earth, Pygate, Unchained Index,
Padlock ](../../../blog/posts/meet-the-hackfs-teams-vol.1/)

Welcome to the sixth installment of the Filecoin Community Highlights series,
which features users and developers building essential tools and services on
the Filecoin network.

Jan 1, 2000

[ ](../../../blog/posts/meet-the-hackfs-teams-vol.2/)

updates

##  [ Meet the HackFS Teams Vol. 2: Kazan, Parcel, EduVault
](../../../blog/posts/meet-the-hackfs-teams-vol.2/)

Welcome to the seventh installment of the Filecoin Community Highlights
series, which features users and developers building essential tools and
services on the Filecoin network.

Jul 24, 2020

[ ](../../../blog/posts/meet-the-hackfs-teams-vol.3/)

updates

##  [ Meet the HackFS Teams Vol. 3: coeo, IPFS.FPS, Sailplane
](../../../blog/posts/meet-the-hackfs-teams-vol.3/)

Welcome to the ninth installment of the Filecoin Community Highlights series,
and our final post highlighting the HackFS teams building essential tools and
services on the Filecoin network.

Aug 6, 2020

Filecoin is an open-source cloud storage marketplace, protocol, and incentive
layer.

##### Reach out

  * [Slack ](https://filecoin.io/slack)
  * [WeChat  ](https://weixin.qq.com/r/1xz54Y-EctINrcuC90nF)
  * [Twitter ](https://twitter.com/Filecoin)
  * [Forum ](https://github.com/filecoin-project/community#forums)
  * [Matrix ](https://riot.im/app/#/group/+filecoin:matrix.org)

##### Resources

  * [Research](https://research.filecoin.io/)
  * [Blog](https://filecoin.io/blog/)
  * [Github](https://github.com/filecoin-project)
  * [ProtoSchool](https://proto.school/course/filecoin)
  * [Security](https://security.filecoin.io/)

##### Sign up for Filecoin updates

Your email Submit

Something went wrong. Please try again.

You’ve been signed up for our newsletter. Thank you!

