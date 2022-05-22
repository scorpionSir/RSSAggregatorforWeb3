[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/485a488d571e&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![UniLogin](https://miro.medium.com/fit/c/64/64/1*pbXgdMyIerXmHIJzLcj0Tg.png)](https://medium.com/universal-
ethereum?source=post_page-----485a488d571e--------------------------------)

Published in

[UniLogin

](https://medium.com/universal-ethereum?source=post_page-----
485a488d571e--------------------------------)

[![Alex Van de
Sande](https://miro.medium.com/fit/c/96/96/1*uSFtzUEJ_BHRsKRg613LRg.jpeg)](/@avsa?source=post_page
-----485a488d571e--------------------------------)

[Alex Van de Sande](/@avsa?source=post_page-----
485a488d571e--------------------------------)

Follow

Apr 27, 2020

·

6 min read

# Turtles All the Way Down: Multisigs Owning Multisigs

## Using UniLogin and Gnosis Safe to control a multisig from another multisig.

Despite challenging times, our team is doing our best not to slow down. After
tackling the nuances of remote work, we have been focusing on stability and
polishing [UniLogin](https://unilogin.io/).

Meanwhile we are happy to see that some integrations we’ve being working on
are going live, namely [**Kickback**](http://kickback.events) and [**Gnosis
Safe Multisig**](https://gnosis-safe.io/app).

But wait, didn’t we already [announce we were using Gnosis Safe](/universal-
ethereum/universal-login-beta-3-gnosis-safe-support-more-9b72be0e01f8)? To
explain, let’s clarify some terms.

Besides their prediction markets and exchanges, the Ethereum development
company Gnosis has also built two widely used multisig contract wallets: the
original _Gnosis multisig_ and the newer _Gnosis Safe_ , which supports
etherless transactions. The latter is what we use internally as our contract-
based accounts.

But Gnosis also offers Gnosis Safe as a frontend service for teams, so they
have an app named _“Gnosis Safe Multisig”_ (no relation to the previous
“Gnosis Multisig”). The Gnosis Safe Multisig app, which was formerly named
“Gnosis Safe for Teams”, allows you to create and manage safes from MetaMask
or other service providers, now including [UniLogin](https://unilogin.io/),
which is _itself_ a multisig.

#  **But _why_?**

![](https://miro.medium.com/max/1400/1*ljWIX_woIMOmfqUDHRpnHA.png)

An identity picker concept from 2014 that would allow multiple addresses for
each user “profile,” including one for a collective account.

Is this just a curiosity to make a point about daisy-chaining contracts
together? **Not at all!** In fact, the idea of modularity and that every
account would eventually be a rich, smart account has permeated Ethereum
development since the early days. You can see this from this screenshot from
my [2014 presentation of a vision for an Ethereum
browser](https://www.youtube.com/watch?v=IgNjs_WaFSc) at Devcon0. In fact,
when Geth was first developing account management, it was believed that public
key pair accounts would be just a temporary measure and that in less than a
year most people would have migrated to what we then called “proxy accounts.”

This goes deep into the heart of what an “identity” is. What makes you “you”
online?

On the traditional web, it’s about authorization: proving to a central server
within their reasonable bounds that you are the correct person, with
increasingly hard challenges (a session cookie and, if that fails, a username
and password, then a “forgot password” flow, and then sometimes you might be
able to escalate it to a human in the help desk).

In the crypto space, traditionally it has been a very binary choice: if you
have the private key, then those are your coins. If you lose access to your
key, or if someone else gets access to that key, then too bad, you’ve lost
them.

![](https://miro.medium.com/max/1400/1*-eeJXWuN20oAyok3cW3HuA.png)

It’s our belief that in a decentralized world, the concept of “you” will be a
constellation of devices and keys that all agree to slowly expand. Your phone,
your laptop, your tablet, an email, a smart card, maybe someday a smart
passport, your watch, eyeglasses, or any other smart wearable will be added to
this constellation of your identity. Each device (and each app in each device)
holds a single untransferable key that is authorized to do a few actions on
your behalf and enables you to vote to add or remove devices to that identity
or expand these permissions. **Your digital identity is a democracy made of
your devices.**

![](https://miro.medium.com/max/1400/1*jv8wDeb222AV0Yc5oPcovQ.png)

If Alice and Bob wants to start a common enterprise, let’s say a bar and
restaurant called “Foo,” they should be able to control that identity together
in a similar fashion: for some actions (like posting on a social media app)
one of the keys should be enough to authorize it, for other more important
actions (like moving funds) they would need multiple approvals.

What if now the Foo Bar wants to vote in a trade union of local bars? Or if
the local trade unions want to do an assembly vote on state level? Not
necessarily all of these collective contracts would follow the same rules, but
the important lesson is that they should be infinitely scalable, from the
small decision of which of your devices to authorize a transaction, up to who
has a right to vote on the global election.

# In practice: how do we get there?

Enough with the theory, how does it look today?

  1. Go to the [Gnosis Safe app](https://gnosis-safe.io/app/).
  2. Click connect to wallet > Show More > UniLogin.
  3. Select your username. If you already have a login it will connect you to one, otherwise it will create one for you.
  4.  **If you are in the US, you can now use Apple Pay,** thanks to our Wyre integration! Otherwise you can always use the excellent Ramp in Europe or just use crypto if you are already onboarded.

![](https://miro.medium.com/max/1400/1*X08YZp5_doSPvfvjC3taDw.gif)

As soon as the transfer is detected, a new account will be created for you,
which uses Gnosis Safe behind the scenes. Now to create a _new_ Gnosis Safe,
just click “create new safe” and then follow the instructions on the page.
**When you are asked for a list of owners instead of hunting down Ethereum
addresses to copy paste, just type your UniLogin username**! Whenever you are
using UniLogin you always get assigned an ENS name on account creation, and
since this page supports ENS lookups, all you need to do is type the given
name and the right account will be found automatically.

![](https://miro.medium.com/max/1400/1*mI4KbAVawCVKnvGkbAa0rw.gif)

This will create your second level multisig, from your personal level multisig
account. It doesn’t look that complicated does it? If you’re curious to see
how it looks like technically, [check the transaction that generates the safe,
from the first
one](https://etherscan.io/tx/0x6c17dcfce2d2c38861333cb2c4427c49bd58f73451f5d24ecca812678c52026e#internal).

 **Warning: Don’t put more than a few dollars into your account yet.**

![](https://miro.medium.com/max/1400/1*lCRQji7nhJiImGjgcF12MA.png)

Some browsers (like Safari), are changing their approach to local storage and
are clearing it with more frequency in order to combat tracking. So you might
get logged out and without access to your main account. To make sure that this
doesn’t happen, make sure to download the “recovery” key PDF.

This should not happen in most browsers at the moment but we are changing the
user flow to make sure this is more prominent to avoid user losses.

# Also try it on Kickback!

We are also happy you can use UniLogin with our good friends from Kickback
too. Just go to ****[**kickback.events**](http://kickback.events) and select
“UniLogin” as your wallet option.

![](https://miro.medium.com/max/1400/1*D0rFs-Wx3EkZ91fsenYjTQ.png)

## Integration with Blocknative

Both Kickback and Gnosis safe use [**Blocknative’s
OnBoard.js**](https://docs.blocknative.com/onboard), which is why if you are
already using it, add one configuration line to integrate with your app (see
line 5 in the snippet below):

The Blocknative team helped us to improve usability by giving users instant
feedback during onboarding when ether is being transferred into an account,
even before a transaction is mined.

# Follow us!

To make sure you don’t miss the next posts in the series, follow us
[Medium](https://medium.com/universal-ethereum) and
[Twitter](https://twitter.com/unilogin).

# Pilot program

Still not signed-up for our Beta program? Fix it!

[Join our Pilot program](http://tiny.cc/unilogin) 👮🏽 🛩

\--

\--

\--

## [More from UniLogin](/universal-ethereum?source=post_page-----
485a488d571e--------------------------------)

The best user onboarding solution for Ethereum dapps.

[Read more from UniLogin](/universal-ethereum?source=post_page-----
485a488d571e--------------------------------)

## Recommended from Medium

[[![BFis_Finance](https://miro.medium.com/fit/c/40/40/1*SJdPMuxoEj3feHQXTO69dA.png)](/@bfi.finance?source=post_internal_links
---------0----------------------------)

[BFis_Finance

](/@bfi.finance?source=post_internal_links---------
0----------------------------)

## Defi With BFIs.Finance | Connecting Metamask to BSC Mainnet

![](https://miro.medium.com/focal/112/112/50/50/0*5OD5Mr0RsXggwgt5)](/@bfi.finance/defi-
with-bfis-finance-connecting-metamask-to-bsc-
mainnet-4b25c77484e3?source=post_internal_links---------
0----------------------------)

[[![Investa](https://miro.medium.com/fit/c/40/40/1*BQv4YYC4OpXpOhwxJEGoaQ.jpeg)](/@investa?source=post_internal_links
---------1----------------------------)

[Investa

](/@investa?source=post_internal_links---------1----------------------------)

## USDT Stablecoin Depegged Amidst Crypto Bloodbath

![](https://miro.medium.com/focal/112/112/50/50/1*P35AdlT8dLY2h5fAUHeOUQ.jpeg)](/@investa/usdt-
stablecoin-depegged-amidst-crypto-bloodbath-
aeb6c9c6f7c8?source=post_internal_links---------1----------------------------)

[[![Crypto
Scrat](https://miro.medium.com/fit/c/40/40/1*9i7JrJG_Mmcv6qwRWdFX0Q.png)](/@CryptoScrat?source=post_internal_links
---------2----------------------------)

[Crypto Scrat

](/@CryptoScrat?source=post_internal_links---------
2----------------------------)

in

[cryptoscrat

](https://medium.com/cryptoscrat?source=post_internal_links---------
2----------------------------)

## Vetting The Tech And How To Stay Away From Hype

![](https://miro.medium.com/focal/112/112/50/50/1*B4UTlA_eeqicWPFCv2JK-w.png)](/cryptoscrat/vetting-
the-tech-and-how-to-stay-away-from-hype-9be1a822f0c?source=post_internal_links
---------2----------------------------)

[[![Hashbon
FiRe](https://miro.medium.com/fit/c/40/40/1*28DfNWj1LqCtYbOaLRNTpA.jpeg)](/@hashbon?source=post_internal_links
---------3----------------------------)

[Hashbon FiRe

](/@hashbon?source=post_internal_links---------3----------------------------)

## Hashbon Weekly Report 13/12

![](https://miro.medium.com/focal/112/112/50/50/0*9EeDZomPkLGrSDK4)](/@hashbon/weekly-
report-13-12-109f265cd76b?source=post_internal_links---------
3----------------------------)

[[![Victor](https://miro.medium.com/fit/c/40/40/1*W00OaylrkuwNdnrOSGre8A.jpeg)](/@victorswae?source=post_internal_links
---------4----------------------------)

[Victor

](/@victorswae?source=post_internal_links---------
4----------------------------)

## CoinSmart Exchange Review

![](https://miro.medium.com/focal/112/112/50/50/1*sYe3gThlipd95q0xPMDyYQ.jpeg)](/@victorswae/coinsmart-
exchange-review-6ef4e58ecbe?source=post_internal_links---------
4----------------------------)

[[![The Serenity
Fund](https://miro.medium.com/fit/c/40/40/1*PeMFt7S22Rq5famUrcC6cQ.png)](/@serenityfund?source=post_internal_links
---------5----------------------------)

[The Serenity Fund

](/@serenityfund?source=post_internal_links---------
5----------------------------)

in

[Coinmonks

](https://medium.com/coinmonks?source=post_internal_links---------
5----------------------------)

## [Strategy Paper] Assess the Risk of Stablecoin Investments

![](https://miro.medium.com/focal/112/112/50/50/0*MWFy5w342ntVWJmy)](/coinmonks/strategy-
paper-assess-the-risk-of-stablecoin-
investments-5c221aee51c?source=post_internal_links---------
5----------------------------)

[[![support Mile_platform](https://miro.medium.com/fit/c/40/40/1*d1KVSJt-
vWstxOs7w18EhA.jpeg)](/@mile_coin?source=post_internal_links---------
6----------------------------)

[support Mile_platform

](/@mile_coin?source=post_internal_links---------
6----------------------------)

## ✈️How to participate in MILE ICO ?✈️

![](https://miro.medium.com/focal/112/112/50/50/1*oG0na9ghV1MH-
INJEvQUmg.png)](/@mile_coin/how-to-participate-in-mile-ico-
ec0e359a72a9?source=post_internal_links---------6----------------------------)

[[![kalpak
savaliya](https://miro.medium.com/fit/c/40/40/0*sZCvSEcTew0sVbt5)](/@kalpak.webmarketing?source=post_internal_links
---------7----------------------------)

[kalpak savaliya

](/@kalpak.webmarketing?source=post_internal_links---------
7----------------------------)

## Demand Curve: How Ahrefs&#8217; homepage educates prospects to purchase :
Tech Big News

](/@kalpak.webmarketing/demand-curve-how-ahrefs-8217-homepage-educates-
prospects-to-purchase-tech-big-news-d88d0888957f?source=post_internal_links
---------7----------------------------)

[](/?source=post_page-----485a488d571e--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
485a488d571e--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
485a488d571e--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
485a488d571e--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
485a488d571e--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----485a488d571e--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----485a488d571e--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Funiversal-
ethereum%2Fturtles-all-the-way-down-multisigs-owning-
multisigs-485a488d571e&source=post_page--------------------------
nav_reg-----------)

[![Alex Van de
Sande](https://miro.medium.com/fit/c/176/176/1*uSFtzUEJ_BHRsKRg613LRg.jpeg)](/@avsa)

[

## Alex Van de Sande

](/@avsa)

1.99K Followers

Designer, Ethereum Foundation, Mist Browser.

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F9649ed57f949&operation=register&redirect=https%3A%2F%2Fmedium.com%2Funiversal-
ethereum%2Fturtles-all-the-way-down-multisigs-owning-
multisigs-485a488d571e&newsletterV3=a109bd84ad93&newsletterV3Id=9649ed57f949&user=Alex+Van+de+Sande&userId=a109bd84ad93&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Daniel Bar
丹尼尔👩🏼‍🎤](https://miro.medium.com/fit/c/40/40/2*33G3WVOdp78jgz0UT7zNdA.png)](/@damndaniel?source=read_next_recirc
---------0---------------------d4036534_c80c_4fef_a35e_193041387207-------)

[Daniel Bar 丹尼尔👩🏼‍🎤

](/@damndaniel?source=read_next_recirc---------0---------------------
d4036534_c80c_4fef_a35e_193041387207-------)

in

[Bitfwd

](https://medium.com/bitfwd?source=read_next_recirc---------0
---------------------d4036534_c80c_4fef_a35e_193041387207-------)

## Fractal Commons: Why Blockathon DAO

![](https://miro.medium.com/focal/112/112/50/50/0*addgOFZTNU27CtDQ)](/bitfwd/fractal-
commons-why-blockathon-dao-85a481af21a9?source=read_next_recirc---------0
---------------------d4036534_c80c_4fef_a35e_193041387207-------)

[[![Mayank
Mishra](https://miro.medium.com/fit/c/40/40/1*lhEylqsUsqvphCCkJ542tA.png)](/@mayankmishra-57578?source=read_next_recirc
---------1---------------------d4036534_c80c_4fef_a35e_193041387207-------)

[Mayank Mishra

](/@mayankmishra-57578?source=read_next_recirc---------1---------------------
d4036534_c80c_4fef_a35e_193041387207-------)

## Centralized vs. Distributed Organizations (DAOs) :

![DAO](https://miro.medium.com/focal/112/112/50/50/1*TohkOOSQJVjhHTCUbsO3pg.jpeg)](/@mayankmishra-57578/centralized-
vs-distributed-organizations-daos-107bb03e8db8?source=read_next_recirc
---------1---------------------d4036534_c80c_4fef_a35e_193041387207-------)

[[![Nicholas
Gardner](https://miro.medium.com/fit/c/40/40/1*Xj0vOk9MkRQsTReBq9LG-Q.png)](/@nickgardner0651?source=read_next_recirc
---------2---------------------d4036534_c80c_4fef_a35e_193041387207-------)

[Nicholas Gardner

](/@nickgardner0651?source=read_next_recirc---------2---------------------
d4036534_c80c_4fef_a35e_193041387207-------)

## Modularity Creates Adaptation: The Celestia Thesis

![](https://miro.medium.com/focal/112/112/50/50/1*28Ve9dqkisZZ01B8dhdHOg.png)](/@nickgardner0651/modularity-
creates-adaptation-the-celestia-thesis-b00903e59ea8?source=read_next_recirc
---------2---------------------d4036534_c80c_4fef_a35e_193041387207-------)

[[![Sandeep Singh
Baghel](https://miro.medium.com/fit/c/40/40/1*9XFSfwTPQVH3oTseyThsUQ.jpeg)](/@yononsensedude?source=read_next_recirc
---------3---------------------d4036534_c80c_4fef_a35e_193041387207-------)

[Sandeep Singh Baghel

](/@yononsensedude?source=read_next_recirc---------3---------------------
d4036534_c80c_4fef_a35e_193041387207-------)

in

[Cryption Network

](https://medium.com/cryption-digital-services?source=read_next_recirc
---------3---------------------d4036534_c80c_4fef_a35e_193041387207-------)

## Cryption Network is Hiring!

![](https://miro.medium.com/focal/112/112/50/50/0*IsgyVEEqAf-s54cz)](/cryption-
digital-services/cryption-network-is-
hiring-81f0cf56f6b8?source=read_next_recirc---------3---------------------
d4036534_c80c_4fef_a35e_193041387207-------)

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

