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
    * [한국어](//blog.ko.orchid.com/how-orchid-improves-privacy-using-a-public-blockchain/)
    * [English](//blog.orchid.com/how-orchid-improves-privacy-using-a-public-blockchain/)
    * [日本](//blog.ja.orchid.com/how-orchid-improves-privacy-using-a-public-blockchain/)
    * [中文](//blog.zh.orchid.com/how-orchid-improves-privacy-using-a-public-blockchain/)
    * [Indonesian](//blog.id.orchid.com/how-orchid-improves-privacy-using-a-public-blockchain/)
    * [русский](//blog.ru.orchid.com/how-orchid-improves-privacy-using-a-public-blockchain/)

Download](//www.orchid.com/download)

# [Blog](/)

![How Orchid improves privacy using a public
blockchain](/static/2e74b6d76448cb7144d59159c7c41525/Orchid_BlogPost_Privacy.jpg)

# How Orchid improves privacy using a public blockchain

Apr 8, 2020  
  

 **What do we mean when we say privacy?**

One of a typical VPN app's central UI features is a prominent "on/off" button.
The simple two state design will feel familiar to anyone who uses a VPN. It
makes for a simple user experience in which it is obvious to people whether or
not the VPN is engaged and they are receiving the benefit or not.

But in truth, privacy is more nuanced than a simple binary of "on" or "off".
It's a spectrum. Different users have different objectives and use cases for
employing privacy tools. Some are trying to access content from a geography
where that content is blocked. Others simply want to browse the Internet while
keeping their identity and activity private. Even within private browsing,
there are sub-use cases, depending on whom you want privacy _from_. Do you
want to keep the medical condition you were researching private, so that your
mobile carrier or home Internet provider can't sell the data those websites
collect to advertisers? Are you a political dissident in a country that would
jail you for your views? The more sophisticated the organization and the
harder they're trying to track you, the more difficult it is to achieve
privacy from them.

**Different use cases require different levels of privacy**

To illustrate where various privacy needs and solutions fall relative to one
another, it's worth considering a few different use cases. At the most severe
end, a person might be looking for privacy from an extremely sophisticated
actor, such as a hostile government. This could be for a number of reasons,
and we won't get into the ethics of those here. One key point we would like to
make is a technical one. A major government intelligence apparatus is
exceedingly difficult to maintain privacy from. A fugitive -- Edward Snowden,
for example -- could not depend on a VPN alone. Advanced state actors possess
extremely sophisticated technical as well as legal tools, some beyond the
abilities and understanding of commercially available security techniques.

VPNs can and do, however, play a vital part in protecting the privacy of
dissidents, journalists, and others who are under threat from governments in
many cases. In Venezuela, for example, they are an essential tool for
opposition figures.

That said, most people want Internet privacy for far more quotidian and
relatable reasons: either to access content that is blocked in a particular
geography, or to protect themselves from being hacked or tracked as they
browse the Internet day to day. In these cases, a VPN solves the problem by
encrypting traffic, protecting a user's IP address and by exiting in a
different geography.

Take the example of a startup executive using a public WiFi network while on
an airport layover. Hackers often take advantage of public, unsecured networks
to steal sensitive information from unsuspecting users. The executive in this
example could -- should -- use a VPN to protect herself and her company's
intellectual property from the bad actors that may be lurking. In this case,
the VPN adds a critical layer of protection.

**Enter Orchid: the Privacy Network**

The Orchid network is a new kind of peer-to-peer network for privacy. Instead
of relying on volunteers, Orchid uses financial incentives to align the actors
in the system and reward healthy network growth. Over time, Orchid will grow
to the point that it offers network security beyond anything currently
available. One thing is for sure: Orchid will take on a life of its own --- it
is permissionless, decentralized, and incentivized to grow.

The Orchid app is the first client side application that can harness the new
Orchid network, allowing users to create VPN connections for privacy.
[Download Orchid](https://www.orchid.com/download) and [follow the
instructions](https://www.orchid.com/join) to try the app out. The app goes
further than a typical VPN in a few important ways: by offering advanced
features for multi-hop circuits, by providing access to a network of providers
and by allowing users to pay only for what they use.

**What protections does the Orchid app provide today?**

Standard Internet connections operate by transmitting packets of data.
Different routers and physical infrastructure can see these packets as they
move from the source to the destination. Their owners are therefore in a
position to build a profile of the Internet usage of their paying user (you!)
They can also block content as they see fit. Typically these infrastructure
owners are ISPs --- mobile carriers providing phone data connections, home
cable Internet providers, and WiFi hotspot operators. In all these cases, the
ISP is in an advantaged position to monitor and/or restrict Internet usage. It
is common in many countries for ISPs to restrict content so that users cannot
load certain websites.

In Orchid, users gain privacy by configuring a single- or multi-hop circuit
and funding it with OXT. With a single-hop circuit, Orchid:

  * Prevents websites from seeing your real IP address and physical location;
  * Prevents your ISP from seeing what websites you are visiting and when;
  * Enables access to the open Internet--once a user can connect to Orchid, they are not restricted by ISP level firewalls and can browse the entire Internet freely.

A potential problem with using only a single VPN provider is that the provider
running the single node circuit knows both your IP address and the content you
are accessing. One solution is to trust no single provider with enough
information to know both who you are and what information you are accessing.
To that end, Orchid supports an advanced feature that allows users to
configure multi-hop routes by stringing together multiple nodes into a
flexible multi-hop circuit. Orchid currently supports several underlying
protocols including the native Orchid VPN protocol and OpenVPN, allowing users
to mix and match Orchid nodes with traditional VPN nodes. Our current
implementation will protect you from casual observation of your network
traffic but we DO NOT recommend that you rely solely on Orchid's multi-hop
feature to protect your privacy or anonymity against a persistent adversary.
For example, the current implementation is not sufficiently resistant to
timing attacks.

**Privacy and public payments**

The Orchid app pays for it's circuit by authorizing a continuous stream of
tiny nanopayments to providers for the duration of the connection. While the
[nanopayment architecture](/introducing-nanopayments) locks user funds into a
smart contract and only issues on-chain payments to providers very rarely,
occasional winning tickets result in OXT payments posted on the public
Ethereum blockchain. When that happens, the user's Ethereum address, the
provider's Ethereum address, and a timestamp are stored publically on the
Ethereum blockchain. Note that the payment address of the provider is not a
mapping to any single server; instead it is an arbitrary (and potentially
temporary) payment address that the provider created specifically to receive
funds. Also, the frequency of how often on-chain payments occur is
configurable.

All information gained by a potential network attacker constitutes an
advantage. However, consider exactly what information is revealed. For an
Orchid user running a single hop circuit, the information revealed includes:

  * The user's payment address when service starts is seen by the provider
  * The user's real IP and destination addresses is seen by the provider
  * When a rare on-chain payment is made, the user's address and provider's address are stored on Ethereum with a timestamp available to the public

When considering anonymity, it is important to understand if the user is
linked to the OXT used in their circuit. Worst case, if the user purchased OXT
on an exchange with their real identity, or the VPN provider used in the
circuit maintained logs, then either of those two entities could be compelled
to give information that could deanonymize the user.

Comparatively, a user who paid for a VPN service with a credit card has leaked
more information than an Ethereum address, as the VPN provider knows full name
and complete address information for the credit card paying user. So the
protections in the single hop use case are very comparable.

A multi-hop circuit affords greater network protections, but to setup a multi-
hop Orchid circuit, it would be naive to pay for each hop from the same
Ethereum wallet. In that configuration, each provider would be able to see
that wallet's address and potentially use that address to get information
about the user. To mitigate that, a better way to setup multi-hop circuits
would be to use different wallet addresses for each Orchid hop. If every
wallet address is independently dissociated from the user, the full circuit
might be quite difficult to link back to the user.

**Orchid is a privacy movement**

The goal of Orchid is to start a new network, ecosystem and Open Source
movement to create new privacy tools with stronger protections and
capabilities than we have right now. Our mission is to restore the open and
accessible Internet for everyone. Please join us.

* * *

 _If you enjoyed this blog,[subscribe here](https://www.orchid.com/newsletter-
signup) for privacy news, commentary, and product updates from Orchid._

  * [Privacy](/tag/privacy/)
  * [VPN](/tag/vpn/)
  * [Blockchain](/tag/blockchain/)

](https://twitter.com/intent/tweet?text=%22How%20Orchid%20improves%20privacy%20using%20a%20public%20blockchain%22%20by%20%40OrchidProtocol%20https%3A%2F%2Fblog.orchid.com%2Fhow-
orchid-improves-privacy-using-a-public-blockchain%2F
)[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fblog.orchid.com%2Fhow-
orchid-improves-privacy-using-a-public-blockchain%2F
)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fblog.orchid.com%2Fhow-
orchid-improves-privacy-using-a-public-blockchain%2F)

Download the app and join Orchid’s privacy network today!Get
Orchid](https://www.orchid.com/get-
orchid?utm_medium=website&utm_source=web&utm_campaign=blog-post-
sticky&utm_content=no-js-blog)

## Keep Reading

](/rohan-grey-joins-priv8s-expanding-roster-of-speakers/)

#### Rohan Grey joins Priv8’s expanding roster of speakers

](/rohan-grey-joins-priv8s-expanding-roster-of-speakers/)

Mar 9, 2021

](/marvin-tong-on-battling-the-data-empire-with-privacy-and-decentralization/)

[

#### Marvin Tong on Battling the “Data Empire” with Privacy and
Decentralization

](/marvin-tong-on-battling-the-data-empire-with-privacy-and-decentralization/)

Mar 22, 2021

](/starting-today-it-only-costs-1-to-get-started-with-orchid/)

[

#### Starting today, it only costs $1 to get started with Orchid

](/starting-today-it-only-costs-1-to-get-started-with-orchid/)

Mar 25, 2021

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

