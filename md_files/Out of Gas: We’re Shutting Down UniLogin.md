[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/3b544838df1a&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![UniLogin](https://miro.medium.com/fit/c/64/64/1*pbXgdMyIerXmHIJzLcj0Tg.png)](https://medium.com/universal-
ethereum?source=post_page-----3b544838df1a--------------------------------)

Published in

[UniLogin

](https://medium.com/universal-ethereum?source=post_page-----
3b544838df1a--------------------------------)

[![Alex Van de
Sande](https://miro.medium.com/fit/c/96/96/1*uSFtzUEJ_BHRsKRg613LRg.jpeg)](/@avsa?source=post_page
-----3b544838df1a--------------------------------)

[Alex Van de Sande](/@avsa?source=post_page-----
3b544838df1a--------------------------------)

Follow

Sep 18, 2020

·

6 min read

# Out of Gas: We’re Shutting Down UniLogin

![](https://miro.medium.com/max/1400/1*g4z5_iTreMUioggy0qNuOA.png)

UniLogin is out of gas.

Not necessarily out of money, but the current Ethereum gas market, the rise of
DeFi, and new browser standards have changed the game significantly enough
that we don’t see a way forward with the project.

UniLogin started [two years ago with a vision for a Universal Login standard
for Ethereum](https://www.youtube.com/watch?v=qF2lhJzngto&t=1s), a way to
onboard new users to Ethereum directly from the browser, using smart accounts
and abstracting away all the gas. While the idea was very well received by the
community ([we packed the second largest stage at Devcon
2018](https://www.youtube.com/watch?v=TztR_7IehjU)), we made some bets on a
few assumptions that turned out to be untrue.

## Incorrect Assumption #1: Browsers could be counted to store low value
secrets

A big part of the magic behind “create any account without downloading or
installing anything else” was that we were using localstorage for initial
secrets.

We knew localstorage had a lot of issues: a malicious browser extension can
access all your browser info, a DNS attack could be used to phish users, etc.
Our strategy for that was to push users towards multisigs: every time you
logged in from a different browser or device we would add another key, meaning
that if one of them was stolen, the others could be used to prevent or limit
any harm. We could even add further security by making stronger requirements
for larger amounts (e.g., to move anything over $20 you need to install a
phone based app).

But we didn’t expect to be caught in a fight between Internet giants.
Localstorage, cookies, and any sort of client side memory is widely used and
abused by marketers to track users across the web. Some browser vendors (most
prominently Apple) are fighting back by being more aggressive on their memory
wiping policy, [including erasing all memory if the user doesn’t visit a site
in 7 days](https://webkit.org/blog/10218/full-third-party-cookie-blocking-and-
more/). As a result we (and ironically, a lot of privacy preserving “burner
wallet” websites) simply can’t rely on that method anymore.

As a result, we had to change our roadmap to include signing in via email. We
thought it would be the least invasive of the authentication methods (e.g.,
compared to social media sign in) but it did mean that now we would be hosting
(client-side encrypted!) our users wallets. It also significantly altered our
flow, since we wanted the only identifying information for the user to provide
to be an [ENS name](http://ens.domains/).

## Incorrect Assumption #2: Scalability wouldn’t be a problem

This was an explicit assumption in our presentations: usability was more
important than scalability, and given that there were so many deployed L2
solutions on the market (like xDai), as soon as scalability became a problem
we would all move there.

This turned out a deadly assumption: as soon as we had our email sign-in
solution ready, gas fees on Ethereum made the whole process unworkable.

![](https://miro.medium.com/max/1400/1*KCQztyfiHgUWBaZLrU3_gQ.png)

Step 2 of onboarding flow: send $133 to the miner

UniLogin is particularly sensitive to gas prices because _before onboarding
any users_ we were deploying on their behalf a new multisig wallet,
registering an ENS name, and sometimes using our relayer to add a Dai
transaction. After that, _every new sign-in on a different device required a
new on-chain transaction_ (to add a new key) and _every transaction would be a
bit more expensive_ due to the relayer. **Some days the whole process of
onboarding a new user was costing over $130!** Meaning you could buy a
hardware wallet for the price of signing up on our app.

We don’t consider this to be a temporary problem. Even if the gas situation
improves and makes the cost of user onboarding 10x or even 100x better that
would still be a deal breaker for many mainstream applications with millions
of users.

## Incorrect Assumption #3: Ethereum is meant for everybody

I still hold this belief and hope it will be true again in the future, but at
the moment Ethereum has been going [through a process of
gentrification](https://twitter.com/ameensol/status/1293077109347250176),
where big defi users are pricing out all other usage of the network. Games,
NFTs, DAOs, and many other exciting use cases are simply inaccessible at the
cost of multiple dollars per transaction. Of course, the natural course will
be that a lot of new stuff will move to L2 or their own chains, but right now
at the moment the process is scattered, where many apps are using different
scalability solutions.

The result is that it’s quite hard for someone to build a system right now as
the **One Universal Account**. For the foreseeable future (which is very short
in crypto!) I expect that a lot of interesting use cases will migrate to xDAI,
and that some stark/rollup solution will be the basis of a trading-specific
chain.

# Conclusion

Because our team is small and lean, we could easily squeeze out another six
months of product development and maybe try to find a bridge investment (you
can add a #4 to a list of incorrect assumptions: “that a global pandemic and
recession wouldn’t dry up a lot of VC capital in early stage startups”).

One more direction we considered would be to do a _full pivot into a L2 defi
focused wallet or a sign-in solution only for a smaller set of products in
xDAI_. However, this would be almost a restart of the project and so we
decided simply to return the remaining cash to investors and then go on the
next opportunity.

The wallet market was very hot two years ago, and now that yield farming is
the new hot thing, wallets are going through a natural consolidation. [Portis
is now ShapeShift](/portis/portis-is-now-part-of-the-shapeshift-
family-c86fc402882b).[ Fortmatic is now Magic](/fortmatic/fortmatic-is-now-
magic-reinventing-identity-for-a-more-secure-and-authentic-web-4c6a1608ddcb)
and is focused on [passwordless signups](/magiclabs/magic-raises-4m-to-end-
the-era-of-passwords-f14dda572919). Argent (which I consider to be the closest
implementation of the original vision I had for Universal Logins) announced
their login SDK at EDCON 2020, but haven’t deployed it yet. Also a shoutout to
our friends at Authereum which are still working hard on figuring this gas
thing out!

Because we always used the open philosophy of putting users in charge, we
can’t actually shut off access to user wallets, because they are actually just
a standard gnosis safe. We will continue running relayers at least until the
end of the year to facilitate users migrating their interfaces and funds
elsewhere. If after that you still need some help feel free to contact
marek@ethworks.io and we will help you figure out what you need.

# Whats next?

My co-founder Marek, along with the rest of the team, will be joining the
ranks of [Ethworks](https://ethworks.io/) — setting out on a journey to become
one of the top Ethereum and blockchain service companies worldwide.

For me personally it was quite an adventure. I travelled to many places, met a
lot of great, lovely, beautiful, intelligent, inspiring people, stepped out of
my comfort zone, had great conversations with VCs, founders, and builders of
all walks of life and did things I had never done before. I’m thankful of
everyone who I met in this road and hope to see you soon on whatever my next
step is.

 _So long and thanks for all the fish._

![](https://miro.medium.com/max/1400/1*917_kzdHrwQBrYN3UsY5Lg.jpeg)

Our team, from left to right: Natalia, Alex (behind), Albert, Marek, Jarek,
and Justyna. Not pictured: Brantly, who greatly helped communications.

\--

2

\--

\--

2

## [More from UniLogin](/universal-ethereum?source=post_page-----
3b544838df1a--------------------------------)

The best user onboarding solution for Ethereum dapps.

[Read more from UniLogin](/universal-ethereum?source=post_page-----
3b544838df1a--------------------------------)

## Recommended from Medium

[[![Michael
Lortz](https://miro.medium.com/fit/c/40/40/2*OeWAwMjimYeWAngthRitTw.jpeg)](/@hybridanalyst?source=post_internal_links
---------0----------------------------)

[Michael Lortz

](/@hybridanalyst?source=post_internal_links---------
0----------------------------)

in

[Hybrid Analyst

](https://medium.com/hybrid-analyst?source=post_internal_links---------
0----------------------------)

## Article of the Day: US to limit exporting malicious cyber tools

![](https://miro.medium.com/focal/112/112/50/50/1*YwAZP8IQMnavXreOiYkEhQ.jpeg)](/hybrid-
analyst/article-of-the-day-us-to-limit-exporting-malicious-cyber-
tools-9d8d8199c927?source=post_internal_links---------
0----------------------------)

[[![Orfeo
Morello](https://miro.medium.com/fit/c/40/40/1*wD8zHkYqsnu7-ysvvz74GQ.png)](/@orfeomorello?source=post_internal_links
---------1----------------------------)

[Orfeo Morello

](/@orfeomorello?source=post_internal_links---------
1----------------------------)

## 💾How to hide and store securely 24 words online — (Part 1)

![](https://miro.medium.com/focal/112/112/50/50/1*hhTYG94zQxC_nCo5cuA-
Gw.jpeg)](/@orfeomorello/how-to-hide-and-store-securely-24-words-online-
part-1-df12aee3b60e?source=post_internal_links---------
1----------------------------)

[[![Alisha
Gyawali](https://miro.medium.com/fit/c/40/40/0*MWfo2A51UQJZQNhe)](/@alishagyawali?source=post_internal_links
---------2----------------------------)

[Alisha Gyawali

](/@alishagyawali?source=post_internal_links---------
2----------------------------)

## Linux

![](https://miro.medium.com/focal/112/112/50/50/1*EmS-6wrdEDzqKliiFbFYzA.jpeg)](/@alishagyawali/linux-257179ab813d?source=post_internal_links
---------2----------------------------)

[[![Clark](https://miro.medium.com/fit/c/40/40/1*5c1ehGuOFj_z-
PB_nFefyA@2x.jpeg)](/@cercinus?source=post_internal_links---------
3----------------------------)

[Clark

](/@cercinus?source=post_internal_links---------3----------------------------)

in

[Mac O’Clock

](https://medium.com/macoclock?source=post_internal_links---------
3----------------------------)

## 5 Apps for Privacy & Security

![](https://miro.medium.com/focal/112/112/50/50/0*0gxV2uniLjev51ON)](/macoclock/5-apps-
for-privacy-security-70b1d04fd390?source=post_internal_links---------
3----------------------------)

[[![Pushpak
Naliyadhara](https://miro.medium.com/fit/c/40/40/1*dmbNkD5D-u45r44go_cf0g.png)](/@pushpaknaliyadhara?source=post_internal_links
---------4----------------------------)

[Pushpak Naliyadhara

](/@pushpaknaliyadhara?source=post_internal_links---------
4----------------------------)

## Cryptography, Objective Of Cryptography and Types of Cryptography

![](https://miro.medium.com/focal/112/112/50/50/1*H4Vl91fa8PJXTCi_OcOkTA.png)](/@pushpaknaliyadhara/cryptography-
objective-of-cryptography-and-types-of-cryptography-
bd2a88eeddc0?source=post_internal_links---------4----------------------------)

[[![Nur
Yesilyurt](https://miro.medium.com/fit/c/40/40/1*lU9ff1RMNjjze1BE_szBoQ.jpeg)](/@nuryslyrt?source=post_internal_links
---------5----------------------------)

[Nur Yesilyurt

](/@nuryslyrt?source=post_internal_links---------
5----------------------------)

## DAV Methods and Old Features

![](https://miro.medium.com/focal/112/112/50/50/1*Es_jBDIGOUxunp6gGfFvdg.png)](/@nuryslyrt/dav-
methods-and-old-features-625a1d1309f7?source=post_internal_links---------
5----------------------------)

[[![David
Artykov](https://miro.medium.com/fit/c/40/40/1*lzIUsYK9MV_L8mOYszaC7A.jpeg)](/@david-
artykov?source=post_internal_links---------6----------------------------)

[David Artykov

](/@david-artykov?source=post_internal_links---------
6----------------------------)

in

[DataDrivenInvestor

](https://medium.com/datadriveninvestor?source=post_internal_links---------
6----------------------------)

## Make professional and convincing Linux trojans

![](https://miro.medium.com/focal/112/112/50/50/1*vRf8cAsFIK2symHSB2_cIA.jpeg)](/datadriveninvestor/make-
professional-and-convincing-linux-trojans-
ff36fbc93704?source=post_internal_links---------6----------------------------)

[[![Victor
Grenu](https://miro.medium.com/fit/c/40/40/1*BZJwxvBwgKfF4i2tgCQFWg.png)](/@zoph?source=post_internal_links
---------7----------------------------)

[Victor Grenu

](/@zoph?source=post_internal_links---------7----------------------------)

in

[zoph.io

](https://medium.com/zoph-io?source=post_internal_links---------
7----------------------------)

## AWS Security Digest Newsletter 💌

![](https://miro.medium.com/focal/112/112/50/50/0*NgtS8rXWLCcZw4nO)](/zoph-
io/aws-security-digest-newsletter-5734dae42282?source=post_internal_links
---------7----------------------------)

[](/?source=post_page-----3b544838df1a--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
3b544838df1a--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
3b544838df1a--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
3b544838df1a--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
3b544838df1a--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----3b544838df1a--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----3b544838df1a--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Funiversal-
ethereum%2Fout-of-gas-were-shutting-down-
unilogin-3b544838df1a&source=post_page--------------------------
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
ethereum%2Fout-of-gas-were-shutting-down-
unilogin-3b544838df1a&newsletterV3=a109bd84ad93&newsletterV3Id=9649ed57f949&user=Alex+Van+de+Sande&userId=a109bd84ad93&source=--------------------------subscribe_user-----------)

## More from Medium

[[![67Corvette](https://miro.medium.com/fit/c/40/40/1*EADJDJLwbV_ELY4oWOKG7Q.jpeg)](/@67corvette?source=read_next_recirc
---------0---------------------7895bf2a_ca22_4848_9969_81af7ccaacf2-------)

[67Corvette

](/@67corvette?source=read_next_recirc---------0---------------------
7895bf2a_ca22_4848_9969_81af7ccaacf2-------)

## BITCOIN LAKE: FULL STEAM AHEAD

![](https://miro.medium.com/focal/112/112/50/50/1*CLt9DWgGZEwKUWgsFYjOvg.jpeg)](/@67corvette/bitcoin-
lake-full-steam-ahead-a27f92260734?source=read_next_recirc---------0
---------------------7895bf2a_ca22_4848_9969_81af7ccaacf2-------)

[[![Madhur
Prabhakar](https://miro.medium.com/fit/c/40/40/1*I1bGiR-X3MKk7PzzwBDqVg.jpeg)](/@madhurprabhakar?source=read_next_recirc
---------1---------------------7895bf2a_ca22_4848_9969_81af7ccaacf2-------)

[Madhur Prabhakar

](/@madhurprabhakar?source=read_next_recirc---------1---------------------
7895bf2a_ca22_4848_9969_81af7ccaacf2-------)

## Can DAOs replace governments by 2050?

![](https://miro.medium.com/focal/112/112/50/50/1*Q6G2t9SC41Cb3-DftgDi1w.jpeg)](/@madhurprabhakar/can-
daos-replace-governments-by-2050-17f6790346c5?source=read_next_recirc---------
1---------------------7895bf2a_ca22_4848_9969_81af7ccaacf2-------)

[[![Josh
Tighe](https://miro.medium.com/fit/c/40/40/1*dmbNkD5D-u45r44go_cf0g.png)](/@josh.tighe?source=read_next_recirc
---------2---------------------7895bf2a_ca22_4848_9969_81af7ccaacf2-------)

[Josh Tighe

](/@josh.tighe?source=read_next_recirc---------2---------------------
7895bf2a_ca22_4848_9969_81af7ccaacf2-------)

in

[AppLearn Engineering

](https://medium.com/applearn-engineering?source=read_next_recirc---------2
---------------------7895bf2a_ca22_4848_9969_81af7ccaacf2-------)

## The pros and cons of poly and mono repositories

![](https://miro.medium.com/focal/112/112/50/50/1*9S0TyygD_9gxl2dD6KN7Dg.jpeg)](/applearn-
engineering/poly-vs-mono-repositories-a0159516436a?source=read_next_recirc
---------2---------------------7895bf2a_ca22_4848_9969_81af7ccaacf2-------)

[[![Josh](https://miro.medium.com/fit/c/40/40/1*0Cx4S7i21cXHpDPcEuG2OA.jpeg)](/@0xjosh?source=read_next_recirc
---------3---------------------7895bf2a_ca22_4848_9969_81af7ccaacf2-------)

[Josh

](/@0xjosh?source=read_next_recirc---------3---------------------
7895bf2a_ca22_4848_9969_81af7ccaacf2-------)

in

[Letters from the Savannah

](https://medium.com/letters-from-the-savannah?source=read_next_recirc
---------3---------------------7895bf2a_ca22_4848_9969_81af7ccaacf2-------)

## Networks and Flywheels

![](https://miro.medium.com/focal/112/112/50/50/1*bAgjtPoeeEFtsRlw42MQ5Q.jpeg)](/letters-
from-the-savannah/networks-and-flywheels-f4c75216f7d5?source=read_next_recirc
---------3---------------------7895bf2a_ca22_4848_9969_81af7ccaacf2-------)

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

