![Privacy & VPN Blog - Orchid](/img/orchid-logo-
text.svg)](https://www.orchid.com/)![Privacy & VPN Blog - Orchid](/img/orchid-
logo-small.svg)](https://www.orchid.com/)

![Open Menu](/img/icons/hamburger.svg)

![Close Menu](/img/icons/close.svg)

  * [Home](https://www.orchid.com/)
  * [Create Account](https://www.orchid.com/join)
  * [How It Works](https://www.orchid.com/how-it-works)
  * [OXT](https://www.orchid.com/oxt)
  * [About](https://www.orchid.com/about-us)
  * [Blog](/)
  * [Contact](https://www.orchid.com/contact)
  * ![](/img/globe.svg)English
    * [한국어](//blog.ko.orchid.com/orchid-a-new-approach-to-vpns/)
    * [English](//blog.orchid.com/orchid-a-new-approach-to-vpns/)
    * [日本](//blog.ja.orchid.com/orchid-a-new-approach-to-vpns/)
    * [中文](//blog.zh.orchid.com/orchid-a-new-approach-to-vpns/)
    * [Indonesian](//blog.id.orchid.com/orchid-a-new-approach-to-vpns/)
    * [русский](//blog.ru.orchid.com/orchid-a-new-approach-to-vpns/)

Download](//www.orchid.com/download)

# [Blog](/)

![Orchid: A New Approach to
VPNs](/static/95f14a02e4d39bfa96617f554d357c6a/new-approach.jpg)

# Orchid: A New Approach to VPNs

Oct 9, 2019  
  

Orchid is a decentralized, market-based system for anonymous communication and
virtual private networking, including a bandwidth market where node providers
stake tokens to advertise their services using the Ethereum blockchain and
receive payment in OXT (Orchid’s native cryptocurrency).

> Using a distributed system allows you, as a user, to distribute trust across
> multiple distinct VPN providers, thereby breaking apart the flow of your
> information so no single entity can see the entire picture.

In the Orchid marketplace, incentives are used to create economic security and
reliability between clients and servers in a permissionless way. This peer-to-
peer marketplace is dynamic; clients can select single- or multi-hop onion
routed circuits by selecting nodes randomly weighted on stake and filtered on
secondary desiderata (price, location, etc.). A single hop route has the
benefits of a normal VPN connection, creating a tunnel to route your traffic
over a public network or your ISP, while a multi-hop connection provides
additional privacy benefits by securing your network data from any one
provider.

Traditional VPNs today are limited; the centralized nature of their offering
cannot compete with the distributed properties of combining multiple different
providers to offer multi-hop level security. And even if a single company
offers multiple hop VPN routes, there is still a single centralized entity you
are placing your trust into. Using a distributed system allows you, as a user,
to distribute trust across multiple distinct VPN providers, thereby breaking
apart the flow of your information so no single entity can see the entire
picture. Such a system is not possible when purchasing a VPN service from a
single provider.

Staking aligns incentives against operator malfeasance, and linear stake
weighting in particular neutralizes sybil attacks. A stochastic nanopayment
solution scales transaction throughput, enabling a highly liquid bandwidth
market without a trusted central party. Nanopayments on the scale of packets
allow high frequency, trustless interactions by reducing the implicit floated
balances between transactors to miniscule levels.

![Illustration of the lifecycle of OXT](/img/uploads/orchid-platform-
illustration.png)

## Core Technology

Orchid’s technology is highly modular. Each component is intended to be
somewhat separable, and to interact well with a particular role in the larger
ecosystem. Abstractly, the system involves:

  * Users who run the Orchid App
  * Service providers who run the Orchid Server
  * A protocol that intermediates client/server interactions
  * Several smart contracts deployed to the Ethereum blockchain that support the economically sound and technically secure operation of the protocols

In pursuit of security, we have tended to remove features and design elements
that we did not think would continue to function basically “as is” for many
years.

![A fun illustration of OXT](/img/a-new-approach-decorative-illustration.png)

## Orchid Cryptocurrency (OXT)

OXT is expected to be a “pre-mined” cryptocurrency based on the ERC-20
standard that will be used to decentralize trust between buyers and sellers in
the Orchid marketplace. It also functions as a tool to promote security and
healthy market dynamics, as providers can adjust their OXT stake to remain
competitive. At launch we intend there to be a limited supply of one billion
(1,000,000,000). We do not intend ever to create any additional OXT.

## Orchid Protocol

The Orchid software is designed to use a custom VPN protocol, similar in scope
to OpenVPN or WireGuard. The Orchid protocol is designed for high-performance
networking and runs on top of WebRTC, a common web standard, widely used to
transmit video and audio from inside browsers. Our protocol is intended to
allow users to request access to remote network resources and pay for these
resources using OXT via a nanopayments system.

## Orchid Server Design

Service providers on Orchid are anticipated to run a server similar to a
typical VPN daemon for protocols such as OpenVPN, but which speaks the Orchid
protocol. Orchid servers maintain registration information in a stake registry
and provider directory. The stake registry is optimized to enable the Orchid
client to automatically discover random servers on behalf of users in a
decentralized environment, while the provider directory allows server nodes to
register metadata such as geolocation or additional services offered.
Collectively, the Orchid Servers make up the Network.

## The Orchid Network Design

Orchid uses a set of data structures stored on the Ethereum blockchain that
allows clients to efficiently select bandwidth-sellers’ nodes.

Clients are expected to select nodes for proxy chains using a two-step process
of random relative stake-weighted linear selection, followed by secondary
constraint filtering. The first stage linear selection is performed by the
scan function on the node directory tree. The App generates a random point
locally and passes it in as the single argument to scan, which then descends
down the node directory tree. The search terminates in the single unique leaf,
or internode, whose stake segment intersects the chosen random point.

After selecting one or more nodes based on linear relative stake weighting,
the app can then filter by additional criteria such as exit geolocation,
latency (ping), price, custom node metadata tags, and arbitrary whitelists.

[Orchid’s Network: Random Selection + Stake Weighting](/orchids-network-
random-selection-stake-weighting/)

![Orchid enabling a smartphone to connect to the world wide web](/img/oxt-
illustration.png)

## The Orchid App Design

The Orchid App is a client similar to a typical VPN client for protocols such
as OpenVPN, but which speaks the Orchid protocol. The Orchid network client is
intended to go past the basic functionality offered by most VPN clients, with
features such as the ability to analyze network traffic and to pick multiple
providers in a multi-hop configuration. The Orchid client is accessible via
iOS, Android, macOS, Linux, and (soon) Windows.

## Orchid Nanopayments Design

Orchid’s structure uses a new probabilistic nanopayment system designed to
allow the system to scale to potentially millions of transactions per second,
enabling decentralized payments on a per-packet basis. This nanopayment system
is the foundation of the Orchid peer-to-peer bandwidth marketplace where
clients pay Node operators OXT lottery tickets for proxy bandwidth. The system
is designed to lower the transaction costs for small payments by amortizing
transaction fees across many transactions and even across multiple parties.

See [Introducing Nanopayments](/introducing-nanopayments/) for more details.

## The Orchid Marketplace

The Orchid Market is a decentralized peer-to-peer (P2P) network, which allows
users running the Orchid App to purchase bandwidth from one or more sellers
running the Orchid server in order to form a proxy chain to a specific
resource on the Internet (such as a website).

The main participant roles in the Orchid Market are:

  * A user running the Orchid App who initiates proxy chain connections
  * One or more relay nodes who forward encrypted traffic (optionally)
  * An exit node who provides the final connection to an external destination (e.g., a website)
  * A bandwidth seller who accepts nanopayments for traffic (either a relay or exit)

Bandwidth sellers register their nodes on the Ethereum blockchain and user
clients select suitable nodes for routes through calls to Ethereum smart
contracts. Orchid’s structure uses stake-weighting: sellers lock up OXT
cryptocurrency to form stake deposits associated with their nodes in order to
receive traffic in proportion to their relative stake.

## Conclusion

The various components described above collectively form Orchid. When we put
the pieces together, we are in the process of creating a new VPN product that
harnesses the nature of decentralization to distribute trust across multiple
providers and ultimately give the user far more agency and control than is
available on the current market. By combining a decentralized design with a
market-based incentive structure, we believe that users can protect their
privacy and control their data while creating demand to support a healthy
marketplace.

We anticipate in the future that the open source community developing on our
protocol will be working on solutions for traffic analysis resistance, payment
anonymity, low-variance nanopayments, improved double-spend detection and
prevention, traffic obfuscation, improved censorship resistance, whitelist
surety bonds, and more.

As both governments and corporations attempt to control our online
interactions, the VPN market is skyrocketing. But in order to achieve what
users desire in a VPN service, we need a new model. At Orchid, we think that a
peer-to-peer marketplace and decentralized architecture on the Ethereum
blockchain can help pave the way for a new era of online interaction, where
individuals, not organizations, control the future.

## Stay Up to date with Orchid

If you want to keep current on the latest Orchid news and be among the first
to test out the network, [sign up for our
newsletter](https://www.orchid.com/#newsletter-signup) to receive launch
updates.

Website: [www.orchid.com](https://www.orchid.com)

Twitter: <https://twitter.com/OrchidProtocol>

Linkedin: <https://www.linkedin.com/company/orchidprotocol/>

Telegram (Announcements): <https://t.me/officialorchidlabs>

Telegram (Community): <https://t.me/OrchidOfficial>

Facebook: <https://www.facebook.com/OrchidProtocol/>

Medium: <https://medium.com/orchid-labs>

Github: <https://github.com/OrchidTechnologies>

Reddit: <https://www.reddit.com/r/orchid>

* * *

 _If you enjoyed this blog,[subscribe here](https://www.orchid.com/newsletter-
signup) for privacy news, commentary, and product updates from Orchid._

  * [VPN](/tag/vpn/)
  * [Decentralization](/tag/decentralization/)
  * [Blockchain](/tag/blockchain/)

](https://twitter.com/intent/tweet?text=%22Orchid%3A%20A%20New%20Approach%20to%20VPNs%22%20by%20%40OrchidProtocol%20https%3A%2F%2Fblog.orchid.com%2Forchid-
a-new-approach-to-vpns%2F
)[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fblog.orchid.com%2Forchid-
a-new-approach-to-vpns%2F
)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fblog.orchid.com%2Forchid-
a-new-approach-to-vpns%2F)

Download the app and join Orchid’s privacy network today!Get
Orchid](https://www.orchid.com/get-
orchid?utm_medium=website&utm_source=web&utm_campaign=blog-post-
sticky&utm_content=no-js-blog)

## Keep Reading

](/miko-matsumura-on-creating-immortal-software/)

#### Miko Matsumura on Creating “Immortal Software”

](/miko-matsumura-on-creating-immortal-software/)

Mar 8, 2021

](/marvin-tong-on-battling-the-data-empire-with-privacy-and-decentralization/)

[

#### Marvin Tong on Battling the “Data Empire” with Privacy and
Decentralization

](/marvin-tong-on-battling-the-data-empire-with-privacy-and-decentralization/)

Mar 22, 2021

](/emin-gn-sirer-on-the-asteroid-heading-for-technological-dinosaurs/)

[

#### Emin Gün Sirer on the Asteroid Heading for Technological Dinosaurs

](/emin-gn-sirer-on-the-asteroid-heading-for-technological-dinosaurs/)

Apr 12, 2021

![](/img/coral-electric.svg)![](/img/coral-real.svg)![](/img/coral-real-
mobile.svg)![](/img/footer-fish.svg)

![Privacy & VPN Blog - Orchid](/img/orchid-logo-
world.svg)](https://www.orchid.com/)© 2022 Orchid Labs Inc.

[Privacy Policy](https://www.orchid.com/privacy-policy) | [Terms of
Service](https://www.orchid.com/service-terms)

  * [How it Works](https://www.orchid.com/how-it-works)
  * [About Us](https://www.orchid.com/about-us)
  * [Contact](https://www.orchid.com/contact)

  * [Download](https://www.orchid.com/download)
  * [Podcast](https://www.orchid.com/podcast)
  * [Blog](/)

  * [Whitepaper](https://www.orchid.com/assets/whitepaper/whitepaper.pdf)
  * [Partners](https://www.orchid.com/partners)
  * [FAQ](https://www.orchid.com/faq)

 **Follow Us**

  * [![Twitter](/img/icons/social-twitter.svg)](https://twitter.com/OrchidProtocol)
  * [![Reddit](/img/icons/reddit.svg)](https://www.reddit.com/r/orchid/)
  * [![Discord](/img/icons/social-discord.svg)](https://discord.gg/GDbxmjxX9F)
  * [![Telegram](/img/icons/social-telegram.svg)](https://www.t.me/OrchidOfficial)
  * [![Github](/img/icons/social-github.svg)](https://github.com/OrchidTechnologies)
  * [![Facebook](/img/icons/social-facebook.svg)](https://www.facebook.com/OrchidProtocol)
  * [![YouTube](/img/icons/social-youtube.svg)](https://www.youtube.com/channel/UCIH_BKBlNemsCzDhPYZBlHw)
  * [![LinkedIn](/img/icons/social-linkedin.svg)](https://www.linkedin.com/company/orchidprotocol)

