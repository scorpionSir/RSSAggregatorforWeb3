[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/376457fb865e&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Spatium
Blog](https://miro.medium.com/fit/c/64/64/1*Af7ihrFRI_0VaZWS9EcuKA.png)](https://medium.com/spatium-
blog?source=post_page-----376457fb865e--------------------------------)

Published in

[Spatium Blog

](https://medium.com/spatium-blog?source=post_page-----
376457fb865e--------------------------------)

[![Spatium](https://miro.medium.com/fit/c/96/96/1*Af7ihrFRI_0VaZWS9EcuKA.png)](/@spatium_news?source=post_page
-----376457fb865e--------------------------------)

[Spatium](/@spatium_news?source=post_page-----
376457fb865e--------------------------------)

Follow

Nov 8, 2019

·

7 min read

# The Private Key to Failure

![](https://miro.medium.com/max/1400/1*hlq5xrhpXEInu5DoeDbR4Q@2x.png)

Any journey to the world of cryptocurrencies starts with the study of what is
private and public keys. The use of a private key as the only authentication
factor to access an address on the blockchain is one of the basic and oldest
concepts in the crypto industry. It was a simple and elegant solution at the
moment of the Bitcoin’s whitepaper release. But what was meeting requirements
of cypherpunks community in the time of the first experiments with the digital
cash, will not meet them in the era, when the crypto industry receives
millions of dollars in investments and the number of users grows each day.

Most technological approaches in the blockchain industry have completely
changed in the last decade: for example, the concept of a Crypto Wallet has
evolved from a single «wallet.dat» file in the distributive of the Bitcoin’s
client to a complex Web3-browsers like Trust Wallet or hardware security
modules (HSM), integrated into smartphones. But the concept of the private key
as the only authentication factor to access an address on a blockchain hasn’t
changed since Satoshi. The difficulties related to the management of such
private data have already caused a lot of problems in the crypto industry.

In our first article, we will discuss those problems and why it is time to
take steps to more secure and flexible solutions.

# One key to rule them all

In a fast-changing IT-driven society the convenience of physical and software
UX of the product is one of the leading factors to use it. And this is one of
the main problems of the private key on the way to mass adoption — for most
users as well as the business it is a too complex method to interact with a
blockchain. Let’s explore:

  *  **Falls from usual web experience.** Users are accustomed to a combination of login and password as a way to access their apps every day. The private key, which comes with a set of rules of how to manage it, instantly discourages most people when they start learning how to use it;
  *  **Hard to remember.** The private key is a long alphanumerical set of characters, which is almost impossible to remember. Can you please remember this for me: E9873D79C6D87DC0FB6A5778633389F4453213303DA61F20BD67FC233AA33262?
  *  **Complex backup.** As it is really hard to remember, everyone (even if they have remembered it) will make a copy and will try to keep the private key somewhere online or offline in a safe place. But the problem is that people can lose their backups, forget where they left them. Those copies could be accidentally or willfully destroyed. And this is without mentioning how important it is to provide the highest level of security to every backup you make. Because once someone gets access to your private key — he has access to your funds.
  *  **Inheritance transfer.** If the private key holder gets in a coma, becomes disabled, disappears or dies before telling the relatives where he keeps his digital assets and where the private key is, they will have a hard time trying to access those funds. In most cases, such funds will be lost forever.
  *  **Full access only.** There is no option to set terms on which access to funds will be granted. For example, it can’t be set how much can be spent from a specific wallet, in a day and to what addresses. Once someone gets a private key — he has full control over the funds.
  *  **Malicious employees.** In traditional systems, security access can be differentiated between parties: each employee can get access only to the place or information he was permitted. In case of the private key anyone that have it — receives full control.
  *  **Fear of responsibility.** The majority of potential users (masses and businesses) are not ready to be self-responsible for the security of their funds. For them, it is easier to delegate the responsibility for funds management to a third-party like a bank. Also, if something goes wrong (their bank is robbed or hacked), they will get a refund from assurance.

There are projects that do solve some of the mentioned problems in their
product, but none of them solves the whole list, because the concept of a
private key is in the heart of their system. While inconvenience and
inflexibility is a part of this concept, it won’t fit in a fast-changing world
and will only slow down the mass adoption of the crypto industry.

The decentralization requires a self-responsibility (and it doesn’t matter is
it about a funds management or a content posting). Most of the people are not
ready to take this responsibility, and that is a reason why they prefer to
stay or return to services with a centralized architecture. Then, for what was
all this movement on a revolutionary road of decentralization? Is this
inconvenience worth the fall back to the beginning?

# Mordor Fortress

One of the fundamental principles of secure systems development is not to
create one point of failure in them. The private key violates this principle.
And today, all the existing blockchain projects are using the private keys to
provide users access to their funds. Thus all of them have this vulnerability.

Even top exchanges with a professional team and the highest level of
incorporated security cannot guarantee a 100% safety of user’s funds. Since
the beginning of the crypto industry, hackers stole more than $ 4B in
cryptocurrencies. Here are only a few examples of the biggest hacks, which
took place just in recent years: Coincheck — $ 530M, Bitgrail — $195M;
Nicahash — $62M.

To prevent malicious parties from access to private keys, their holders use
various security approaches:

  1.  **Hot Wallets.** Every service that claims to securely store private keys online on their servers falls in this category. In many cases, users don’t have access to them making this solution convenient. They don’t need to think about proper keys management — they just enjoy the service. Plus in most cases it’s free. But at the same time, users don’t have any control over their funds and they must trust a service that can be hacked or whose employees can perform malicious activities from their side. So this is the least secure option.
  2.  **HSM / Secure Enclave.** This solution includes hardware wallets, Industrial HSMs and any other products that use a secure enclave technology to store and manage private keys. The convenience can grade from low to mid-level compared to previous approaches and it is expensive. Moreover, the users must trust a proprietary firmware of the hardware provider.
  3.  **Deep Cold Storage (air gaps)**. This is the most secure option: private keys are generated using community audited code in offline air-gapped computers (they were never been and will never be online or connected to any network and ). The signing process is also performed offline. Every OS is wiped clean after every production run, with the destruction of all data. The room where key management takes place is free from mobile and recording devices. All this is happening in the custody with 24/7 security guard. With that said, it is the most inconvenient and expensive though a very secure option.

Mentioned above security approaches, implemented to secure digital assets, in
most cases share much in common. With the defense strategy of Mordor —
monumental bastions with the whole army around them are put in place to
prevent any kind of a weapon attack — to all of these in one moment become
useless when the one critical and irremovable vulnerability, the One Ring, is
executed. When it is destroyed, the whole system falls. From that perspective
height of Barad-dûr’s walls and towers doesn’t matter at all as any sensible
adversary will never try to storm the front door.

And that is where we meet another side of the Mordor security problem: all
employed guards, who must prevent the potential intruders from accessing
Orodruin and destroying the One Ring, are unable to detect two little hobbits,
who use the trivial number security system exploits:

  1. The thoroughly hidden vulnerability in the underlying system (cave in the mountains), patching of which is entrusted to a non-qualified low-paid employee (Shelob);
  2. The malicious party that has access to confidential information about vulnerabilities in the security system (Gollum);
  3. Unscrupulous employees and a human factor (Cirith Ungol Orcs);
  4. The parallel DDOS attack, which drags the attention of the security system to itself (the attack of Men of the West on the Black Gates).

It is important to notice that most of these problems appear in any system
from time to time, but with proper security architecture, they won’t cause the
crash of it. All existing blockchain projects are based on the private keys
and it’s a single point of failure that cannot be fixed.

# Letting the boat go

The private key as a sole authentication factor to access a blockchain is more
than a 10-year-old security concept, which faced a lot of troubles in its
history. With all the problems that impede the adoption of the crypto
industry, the private key should leave us to the digital lands of happiness.
Though we will remember it for all the fun it gave to us and for the
knowledge, it provided in fields of security and cryptography.

In the next article, we are going to explore the innovative security approach
of the Spatium protocol in detail and why it will continue the good deeds of
the private keys.

#spatium_vision

 **Spatium** develops solutions to store and manage digital assets powered by
SMPC and biometry. In our technology, the private key is replaced with the
encrypted set of secrets, stored on behalf of funds owner’s devices,
individuals and institutions, chosen by him. Even if some of the parties are
compromised — funds will stay safe. Such an approach dramatically decreases
the risk of theft and provides a previously unavailable level of flexibility
and unique benefits for everyone on the market: no single point of failure,
easy recovery, no need in backups, blockchain agnostic, access levels
differentiation, instant crypto/crypto and crypto/fiat exchange, fully
compliant solution, support of dApps and DeFi services, etc.

\--

\--

\--

## [More from Spatium Blog](/spatium-blog?source=post_page-----
376457fb865e--------------------------------)

Keyless & genuinely decentralized solution to manage digital assets.

[Read more from Spatium Blog](/spatium-blog?source=post_page-----
376457fb865e--------------------------------)

## Recommended from Medium

[[![jamilapatersonofficial](https://miro.medium.com/fit/c/40/40/1*W5-2uk96EgYwsHPAuCyThw.png)](/@jamilapatersonofficial?source=post_internal_links
---------0----------------------------)

[jamilapatersonofficial

](/@jamilapatersonofficial?source=post_internal_links---------
0----------------------------)

## Binance Smart Chain’s record-breaking maneuvers can have this effect on
Binane Coin

![](https://miro.medium.com/focal/112/112/50/50/0*_2mLishld_nXwRW6.jpg)](/@jamilapatersonofficial/binance-
smart-chains-record-breaking-maneuvers-can-have-this-effect-on-binane-
coin-c0ee3c54cd74?source=post_internal_links---------
0----------------------------)

[[![Emmanuel
Udoaka](https://miro.medium.com/fit/c/40/40/1*N1jwr9VZJBBx88q7n3XcVg.jpeg)](/@emmasplendour08?source=post_internal_links
---------1----------------------------)

[Emmanuel Udoaka

](/@emmasplendour08?source=post_internal_links---------
1----------------------------)

## ABOUT AMARA FINANCE

![](https://miro.medium.com/focal/112/112/50/50/1*2vIvbB4MnR22GQD2Zv3crg.jpeg)](/@emmasplendour08/about-
amara-finance-e0ffa749bda4?source=post_internal_links---------
1----------------------------)

[[![TRON Core
Devs](https://miro.medium.com/fit/c/40/40/2*C2hv474k9tT9r1g4CCeEvg.jpeg)](/@coredevs?source=post_internal_links
---------2----------------------------)

[TRON Core Devs

](/@coredevs?source=post_internal_links---------2----------------------------)

## Best Practice of Transferring Assets to Smart Contracts

![](https://miro.medium.com/focal/112/112/50/50/1*80TYSk4YhTE3fWeV27JWLw.png)](/@coredevs/best-
practice-of-transferring-assets-to-smart-
contracts-e6b5e53e77ff?source=post_internal_links---------
2----------------------------)

[[![Zichain](https://miro.medium.com/fit/c/40/40/1*IT-t9AihT9bNlzRMOqOcWw.png)](/@zichain?source=post_internal_links
---------3----------------------------)

[Zichain

](/@zichain?source=post_internal_links---------3----------------------------)

in

[Zichain

](https://medium.com/zichain?source=post_internal_links---------
3----------------------------)

## The last few years well deserve the name of ‘the golden age of
cryptocurrency’, since the…

![](https://miro.medium.com/focal/112/112/50/50/1*NYP-
HrdQwsWE_0TiKPiP_A.jpeg)](/zichain/the-last-few-years-well-deserve-the-name-
of-the-golden-age-of-cryptocurrency-since-the-
dcdb0e988986?source=post_internal_links---------3----------------------------)

[[![EXPERIENCE CRYPTO
24/7](https://miro.medium.com/fit/c/40/40/2*8jhxOi58qzx6kNDcs1ABAw.png)](/@xcrypto247?source=post_internal_links
---------4----------------------------)

[EXPERIENCE CRYPTO 24/7

](/@xcrypto247?source=post_internal_links---------
4----------------------------)

## P3T ~ Making Money With Crypto Just Got Ridiculously Easy!

![](https://miro.medium.com/focal/112/112/50/50/1*a8Nt9kXJu37tAXsUD4xxOw@2x.jpeg)](/@xcrypto247/p3t-making-
money-with-crypto-just-got-ridiculously-
easy-2c5da6c7a780?source=post_internal_links---------
4----------------------------)

[[![Unmarshal](https://miro.medium.com/fit/c/40/40/1*yPTij_a2AGnjp_62oVQM3w.png)](/@unmarshal-
io?source=post_internal_links---------5----------------------------)

[Unmarshal

](/@unmarshal-io?source=post_internal_links---------
5----------------------------)

in

[unmarshal

](https://medium.com/unmarshal-io?source=post_internal_links---------
5----------------------------)

## Unmarshal Collaborates with Polkarare to Build a Multi-chain NFT
Marketplace, advancing the Web3…

![](https://miro.medium.com/focal/112/112/50/50/0*ZK0untkWDikf3fTv)](/unmarshal-
io/unmarshal-collaborates-with-polkarare-to-build-a-multi-chain-nft-
marketplace-advancing-the-web3-80dedf4d3b6d?source=post_internal_links
---------5----------------------------)

[[![Ed Ludbrook - Future of
Crypto](https://miro.medium.com/fit/c/40/40/0*DWALvygld93em9wL.jpg)](/@edludbrook?source=post_internal_links
---------6----------------------------)

[Ed Ludbrook - Future of Crypto

](/@edludbrook?source=post_internal_links---------
6----------------------------)

## Why The US Government Hates Crypto?

![](https://miro.medium.com/focal/112/112/50/50/1*GSvLDZOFXGsX29uxQ30OfA.jpeg)](/@edludbrook/why-
the-us-government-hates-crypto-e163606dfff4?source=post_internal_links
---------6----------------------------)

[[![Mark
Lewis](https://miro.medium.com/fit/c/40/40/0*xPetGYe2cur4wqoT.jpg)](/@jiffy360.india?source=post_internal_links
---------7----------------------------)

[Mark Lewis

](/@jiffy360.india?source=post_internal_links---------
7----------------------------)

## What Is Truz Coin?

![](https://miro.medium.com/focal/112/112/50/50/1*dUk_q15IHJD8720-Gvr7Sw@2x.jpeg)](/@jiffy360.india/what-
is-truz-coin-2a4d604605b2?source=post_internal_links---------
7----------------------------)

[](/?source=post_page-----376457fb865e--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
376457fb865e--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
376457fb865e--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
376457fb865e--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
376457fb865e--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----376457fb865e--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----376457fb865e--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fspatium-
blog%2Fthe-private-key-to-failure-376457fb865e&source=post_page
--------------------------nav_reg-----------)

[![Spatium](https://miro.medium.com/fit/c/176/176/1*Af7ihrFRI_0VaZWS9EcuKA.png)](/@spatium_news)

[

## Spatium

](/@spatium_news)

51 Followers

Spatium — true, decentralized, keyless crypto storage solution, bringing
complex cryptographic technologies from security experts to blockchain
enthusiasts.

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F69561b2e7b9e&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fspatium-
blog%2Fthe-private-key-to-
failure-376457fb865e&newsletterV3=eb4a6667c312&newsletterV3Id=69561b2e7b9e&user=Spatium&userId=eb4a6667c312&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Icaro Moro](https://miro.medium.com/fit/c/40/40/1*ToDx4V99Kn34RqGjbS-
tkQ.jpeg)](/@icaromoro?source=read_next_recirc---------0---------------------
71f5c981_8607_4b6a_92ed_474ab983870d-------)

[Icaro Moro

](/@icaromoro?source=read_next_recirc---------0---------------------
71f5c981_8607_4b6a_92ed_474ab983870d-------)

in

[Bitso (EN)

](https://medium.com/bitso-en?source=read_next_recirc---------0
---------------------71f5c981_8607_4b6a_92ed_474ab983870d-------)

## Understanding crypto metrics

](/bitso-en/understanding-crypto-metrics-6f1e2e2cabe9?source=read_next_recirc
---------0---------------------71f5c981_8607_4b6a_92ed_474ab983870d-------)

[[![lalav](https://miro.medium.com/fit/c/40/40/1*oq0-OA2MPTVNLqsr9N08ng.jpeg)](/@llalav?source=read_next_recirc
---------1---------------------71f5c981_8607_4b6a_92ed_474ab983870d-------)

[lalav

](/@llalav?source=read_next_recirc---------1---------------------
71f5c981_8607_4b6a_92ed_474ab983870d-------)

in

[Bitpowr Technologies

](https://medium.com/bitpowr?source=read_next_recirc---------1
---------------------71f5c981_8607_4b6a_92ed_474ab983870d-------)

## History of the Blockchain, how it all started, and where it’s headed?

![](https://miro.medium.com/focal/112/112/50/50/1*2fc8eYxQNPix_S0WfJ5dOw.jpeg)](/bitpowr/history-
of-the-blockchain-how-it-all-started-and-where-its-
headed-923183cb1140?source=read_next_recirc---------1---------------------
71f5c981_8607_4b6a_92ed_474ab983870d-------)

[[![Dan
Morgan](https://miro.medium.com/fit/c/40/40/0*16Dq3UFEaqXDY67o)](/@danmorgan980?source=read_next_recirc
---------2---------------------71f5c981_8607_4b6a_92ed_474ab983870d-------)

[Dan Morgan

](/@danmorgan980?source=read_next_recirc---------2---------------------
71f5c981_8607_4b6a_92ed_474ab983870d-------)

## Broad Market Sell-off Opens Up Buying Opportunity

![](https://miro.medium.com/focal/112/112/50/50/0*CNVIIAUI9BQnGL00.png)](/@danmorgan980/broad-
market-sell-off-opens-up-buying-
opportunity-7c86ff2f52f1?source=read_next_recirc---------2
---------------------71f5c981_8607_4b6a_92ed_474ab983870d-------)

[[![Living
Roots](https://miro.medium.com/fit/c/40/40/1*jae_Z-o46v6viN8FiiuxOw.png)](/@Living_Roots?source=read_next_recirc
---------3---------------------71f5c981_8607_4b6a_92ed_474ab983870d-------)

[Living Roots

](/@Living_Roots?source=read_next_recirc---------3---------------------
71f5c981_8607_4b6a_92ed_474ab983870d-------)

in

[Coinmonks

](https://medium.com/coinmonks?source=read_next_recirc---------3
---------------------71f5c981_8607_4b6a_92ed_474ab983870d-------)

## Open traceability: Technical documentation

![](https://miro.medium.com/focal/112/112/50/50/1*DxcQ1Vebdqz58W0gEXdWJg.jpeg)](/coinmonks/open-
traceability-technical-documentation-6c86e92cbc36?source=read_next_recirc
---------3---------------------71f5c981_8607_4b6a_92ed_474ab983870d-------)

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

