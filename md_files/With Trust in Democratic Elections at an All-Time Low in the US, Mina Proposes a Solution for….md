[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/96018bf18f80&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![MinaProtocol](https://miro.medium.com/fit/c/64/64/1*ubOSZmkEWyTUhMdLMlB1nA.png)](https://medium.com/minaprotocol?source=post_page
-----96018bf18f80--------------------------------)

Published in

[MinaProtocol

](https://medium.com/minaprotocol?source=post_page-----
96018bf18f80--------------------------------)

[![Mina
Protocol](https://miro.medium.com/fit/c/96/96/1*PS93B9ts3XuCR1iso_Q5tQ.png)](/@minaprotocol?source=post_page
-----96018bf18f80--------------------------------)

[Mina Protocol](/@minaprotocol?source=post_page-----
96018bf18f80--------------------------------)

Follow

Nov 2, 2020

·

4 min read

#  **With Trust in Democratic Elections at an All-Time Low in the US, Mina
Proposes a Solution for Verifying Vote Counts**

 _Mina offers verifying vote counts as a future use case for zk-SNARKs to
increase transparency and build trust in our electoral process._

 **San Francisco, CA; November 2, 2020**

A [Pew Research survey](https://www.pewresearch.org/fact-
tank/2020/10/07/voters-anxiously-approach-an-unusual-election-and-its-
potentially-uncertain-aftermath/ft_2020-10-06_voter-concerns_02/) published in
April found that only 14% of voters were “very confident” the 2020
presidential election would be conducted fairly and accurately. The electoral
process is complicated with many moving parts, but verifying vote counts is
one aspect that can be addressed with technology.

[Mina](https://minaprotocol.com/), developed by [O(1)
Labs](https://o1labs.org/), introduced verifying vote counts as one of its
first proposed use cases for its lightweight blockchain. Mina uses the
mathematical concept of zero-knowledge proofs, which allows for the
verification of data without revealing identity, to enable the syncing of its
entire blockchain in mere seconds. Mina’s lightweight design is intended to
usher in a new era of accessibility and scalability for blockchain.

Once the Mina mainnet launches, developers will be able to leverage Mina to
create verifiable SNARK-powered smart contracts, or Snapps, for enabling the
verification of any type of data, including payments, loan eligibility, data
ownership, ID, and — most relevant to today — vote counts.

Izaak Meckler, CTO and Co-Founder of O(1) Labs, the team behind Mina, conveyed
in [ZKPROOF](https://zkproof.org/2020/06/08/recursive-snarks/) that “a
verifiable electoral system should be private in the sense that each vote will
have no identifying information attached to it. It will be verifiable in the
sense that at the end we’ll have a small proof of the result that can be
easily checked on almost any device, including a browser or a phone.”

Izaak expands upon these concepts in a [Mina blog](/minaprotocol/using-
cryptography-to-verify-vote-counts-and-make-elections-more-transparent-
trusted-54a214b00716), sharing how verification of vote counts via Snapps
could work. At a high level, the voting state machine would be defined by:

  1.  **State:** The current tally of votes, along with a set of “ballot stubs”, each a piece of data unique to a given voter, to prevent double voting. Only the hash of this state will appear on chain.
  2.  **Update:** An update to the state is a valid vote, which consists of the vote itself, a zk-SNARK proving eligibility to vote (which provides a level of anonymity) and a valid ballot stub.

Beyond the state machine, there are two components of a snapp’s architecture:

  1.  **State store:** The snapp’s state must be stored somewhere. This state is essentially the tally of the election before, as well as the set of “ballot stubs” to make sure no one votes twice. This doesn’t have to be held by a single party. It could be as centralized as being stored with AWS, or as decentralized as Sia or Filecoin.
  2.  **Prover:** Some party is responsible for proving correctness of each state transition, SNARKing together all the user-submitted state transitions, and uploading the aggregated SNARK to the Mina blockchain to update the on-chain snapp state. Beyond stand-alone verifiable computation, having the hash of a snapp’s state on chain has two types of benefits.

End users will ultimately be able to use the Mina blockchain to verify the
correctness of a claimed result of an election as well as check whether or not
their vote was included.

Izaak expressed, “If we are really serious about having fair elections, we
need the ability to both detect and respond to manipulation. On the detection
side, this is a technology that would be useful at the point of vote counting,
but it needs to be accompanied by powerful, mass organizations of people that
are capable of detecting and responding to manipulation on every level, from
voter suppression, to propaganda, to outright fraud at the point of vote
counting.”

Evan Shapiro, Co-Founder and CEO of O(1) Labs, expressed, “If we cannot trust
the facts of a system due to a lack of transparency and verifiability, the
system falls apart. When it comes to the electoral process, we cannot afford
to allow that to happen. We look forward to launching the Mina mainnet, at
which point, developers can use the protocol to create verifiable Snapps that,
collectively, will form the basis for a new, more transparent and secure Web
3.0.”

For media inquiries, please contact Kili Wall at (310) 260–7901 or
Kili(at)MelrosePR(dot)com.

 **About Mina  
**[Mina](https://minaprotocol.com/) is the world’s lightest blockchain,
powered by participants. Rather than apply brute computing force, Mina uses
advanced cryptography and recursive zk-SNARKs to design an entire blockchain
that is and always will be about 22kb, the size of a couple tweets, ushering
in a new era of blockchain accessibility. With its robust decentralized
network and open-programmable currency, Mina is powering a more efficient and
fair Web 3.0 so anyone can participate, build, exchange and thrive. Mina is a
project of [O(1) Labs](https://o1labs.org/), a leader in verifiable
computation.

\--

\--

\--

## [More from MinaProtocol](/minaprotocol?source=post_page-----
96018bf18f80--------------------------------)

Mina Protocol's Official Blog

[Read more from MinaProtocol](/minaprotocol?source=post_page-----
96018bf18f80--------------------------------)

## Recommended from Medium

[[![Fianna
Chrotoem](https://miro.medium.com/fit/c/40/40/1*dmbNkD5D-u45r44go_cf0g.png)](/@malacoderm1934?source=post_internal_links
---------0----------------------------)

[Fianna Chrotoem

](/@malacoderm1934?source=post_internal_links---------
0----------------------------)

## {UPDATE} Word Buddies-Crossword Puzzle Hack Free Resources Generator

](/@malacoderm1934/update-word-buddies-crossword-puzzle-hack-free-resources-
generator-85769cef3136?source=post_internal_links---------
0----------------------------)

[[![Hacker Noon
Support](https://miro.medium.com/fit/c/40/40/0*auvc6nbuXOzbe4Yh.jpg)](/@SupportNoon?source=post_internal_links
---------1----------------------------)

[Hacker Noon Support

](/@SupportNoon?source=post_internal_links---------
1----------------------------)

in

[HackerNoon.com

](https://medium.com/hackernoon?source=post_internal_links---------
1----------------------------)

## 2020 Noonies Winners Announced 🎉

![](https://miro.medium.com/focal/112/112/50/50/1*FyJHtw8KUMS-
yxBz4UzlvA.png)](/hackernoon/2020-noonies-winners-
announced-a73c4b9f834d?source=post_internal_links---------
1----------------------------)

[[![Burak
Aytekin](https://miro.medium.com/fit/c/40/40/1*cAYeOMdy4AY3y2V98a2-oQ.jpeg)](/@burakayt?source=post_internal_links
---------2----------------------------)

[Burak Aytekin

](/@burakayt?source=post_internal_links---------2----------------------------)

in

[DataBulls

](https://medium.com/databulls?source=post_internal_links---------
2----------------------------)

## 4 Suggestions to Increase the Security of Your Home Network

![](https://miro.medium.com/focal/112/112/50/50/0*6sLxT1lIvu340876)](/databulls/4-suggestions-
to-increase-the-security-of-your-home-
network-f431643881dd?source=post_internal_links---------
2----------------------------)

[[![Aghiath
Chbib](https://miro.medium.com/fit/c/40/40/0*YT_zDlCD543GIME9.jpg)](/@AghiathChbib?source=post_internal_links
---------3----------------------------)

[Aghiath Chbib

](/@AghiathChbib?source=post_internal_links---------
3----------------------------)

in

[Aghiath-Chbib

](https://medium.com/aghiath-chbib?source=post_internal_links---------
3----------------------------)

## Major Incident That Changed Cybersecurity

![](https://miro.medium.com/focal/112/112/50/50/1*IUtNM3m2qKhpttdZPMXmUQ.jpeg)](/aghiath-
chbib/major-incident-that-changed-cybersecurity-
fd643837403b?source=post_internal_links---------3----------------------------)

[[![Sunny Slim
Idiah](https://miro.medium.com/fit/c/40/40/1*5tAcTZR8SWpI5WqeU39zEA.jpeg)](/@sunnyslim?source=post_internal_links
---------4----------------------------)

[Sunny Slim Idiah

](/@sunnyslim?source=post_internal_links---------
4----------------------------)

## How to See All Passwords For Wi-Fi Networks on Your Android Devices Easily

![](https://miro.medium.com/focal/112/112/50/50/0*CgveF09b1oFXm6my.png)](/@sunnyslim/how-
to-see-all-passwords-for-wi-fi-networks-on-your-android-devices-
easily-4569669d5119?source=post_internal_links---------
4----------------------------)

[[![Musyoka
Ian](https://miro.medium.com/fit/c/40/40/0*h7xPb8zou4bnQVlG)](/@musyokaian?source=post_internal_links
---------5----------------------------)

[Musyoka Ian

](/@musyokaian?source=post_internal_links---------
5----------------------------)

## Web Application Brute Force bypass even with a CSRF Token

![](https://miro.medium.com/focal/112/112/50/50/0*SHBco44EUK8HQ-4e.jpg)](/@musyokaian/web-
application-brute-force-bypass-even-with-a-csrf-
token-36f52eb227c9?source=post_internal_links---------
5----------------------------)

[[![Ayush
Budhiraja](https://miro.medium.com/fit/c/40/40/1*dmbNkD5D-u45r44go_cf0g.png)](/@ayush.ab44?source=post_internal_links
---------6----------------------------)

[Ayush Budhiraja

](/@ayush.ab44?source=post_internal_links---------
6----------------------------)

## Lame | HackTheBox

![](https://miro.medium.com/focal/112/112/50/50/1*y2dKgWtWxomgIrT7wjh2kQ.png)](/@ayush.ab44/lame-
hackthebox-7c2f51088f8e?source=post_internal_links---------
6----------------------------)

[[![BASIS
ID](https://miro.medium.com/fit/c/40/40/0*QOlY38yMThVrIiLX.jpg)](/@basisid?source=post_internal_links
---------7----------------------------)

[BASIS ID

](/@basisid?source=post_internal_links---------7----------------------------)

## How do we make sure that a person is real and alive?

![](https://miro.medium.com/focal/112/112/50/50/1*ZyelUehjcG8eG1yknIodvQ.jpeg)](/@basisid/realornot-896bc5edf295?source=post_internal_links
---------7----------------------------)

[](/?source=post_page-----96018bf18f80--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
96018bf18f80--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
96018bf18f80--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
96018bf18f80--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
96018bf18f80--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----96018bf18f80--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----96018bf18f80--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fminaprotocol%2Fwith-
trust-in-democratic-elections-at-an-all-time-low-in-the-us-mina-proposes-a-
solution-for-96018bf18f80&source=post_page--------------------------
nav_reg-----------)

[![Mina
Protocol](https://miro.medium.com/fit/c/176/176/1*PS93B9ts3XuCR1iso_Q5tQ.png)](/@minaprotocol)

[

## Mina Protocol

](/@minaprotocol)

2.5K Followers

The world’s lightest blockchain, powered by participants.

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F7208bdd8f530&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fminaprotocol%2Fwith-
trust-in-democratic-elections-at-an-all-time-low-in-the-us-mina-proposes-a-
solution-
for-96018bf18f80&newsletterV3=b6d3ede7e247&newsletterV3Id=7208bdd8f530&user=Mina+Protocol&userId=b6d3ede7e247&source=--------------------------subscribe_user-----------)

## More from Medium

[[![wanchain](https://miro.medium.com/fit/c/40/40/0*bqt8whPQE8LQ5vIE.jpg)](/@wanchain_org?source=read_next_recirc
---------0---------------------deea94d8_0a48_4fce_bfbd_c2f1243e3a71-------)

[wanchain

](/@wanchain_org?source=read_next_recirc---------0---------------------
deea94d8_0a48_4fce_bfbd_c2f1243e3a71-------)

in

[Wanchain

](https://medium.com/wanchain-foundation?source=read_next_recirc---------0
---------------------deea94d8_0a48_4fce_bfbd_c2f1243e3a71-------)

## Wanchain deploys new Moonbeam bridges

![](https://miro.medium.com/focal/112/112/50/50/1*pnsNKQrSq6fsgJTddm5BQw.jpeg)](/wanchain-
foundation/wanchain-deploys-new-moonbeam-
bridges-24207b4eeebe?source=read_next_recirc---------0---------------------
deea94d8_0a48_4fce_bfbd_c2f1243e3a71-------)

[[![Cartesi
Foundation](https://miro.medium.com/fit/c/40/40/1*6G8_PZAKj84Vy8R2qf9Kxw.png)](/@cartesi?source=read_next_recirc
---------1---------------------deea94d8_0a48_4fce_bfbd_c2f1243e3a71-------)

[Cartesi Foundation

](/@cartesi?source=read_next_recirc---------1---------------------
deea94d8_0a48_4fce_bfbd_c2f1243e3a71-------)

in

[Cartesi

](https://medium.com/cartesi?source=read_next_recirc---------1
---------------------deea94d8_0a48_4fce_bfbd_c2f1243e3a71-------)

## How a CTSI holder plays an active role in advancing Creepts on The
Blockchain OS.

![](https://miro.medium.com/focal/112/112/50/50/1*8wH4E_1KM1Y-Co-f8hlyUA.png)](/cartesi/how-
a-ctsi-holder-plays-an-active-role-in-advancing-creepts-on-the-blockchain-
os-4351adf6ae7d?source=read_next_recirc---------1---------------------
deea94d8_0a48_4fce_bfbd_c2f1243e3a71-------)

[[![Stefan
Ionescu](https://miro.medium.com/fit/c/40/40/1*yOKRpYWa7u6gJqQMM91OeA.jpeg)](/@stefan-
ionescu?source=read_next_recirc---------2---------------------
deea94d8_0a48_4fce_bfbd_c2f1243e3a71-------)

[Stefan Ionescu

](/@stefan-ionescu?source=read_next_recirc---------2---------------------
deea94d8_0a48_4fce_bfbd_c2f1243e3a71-------)

in

[Reflexer Labs

](https://medium.com/reflexer-labs?source=read_next_recirc---------2
---------------------deea94d8_0a48_4fce_bfbd_c2f1243e3a71-------)

## How to Participate in RAI Surplus Auctions

![](https://miro.medium.com/focal/112/112/50/50/1*teOWaIehFOY_00Kk2QulPA.jpeg)](/reflexer-
labs/how-to-participate-in-rai-surplus-
auctions-c6ec6cfe1c44?source=read_next_recirc---------2---------------------
deea94d8_0a48_4fce_bfbd_c2f1243e3a71-------)

[[![Kacper
Koziol](https://miro.medium.com/fit/c/40/40/0*zYRkze3ZOlGz9XtU)](/@kacperkozi?source=read_next_recirc
---------3---------------------deea94d8_0a48_4fce_bfbd_c2f1243e3a71-------)

[Kacper Koziol

](/@kacperkozi?source=read_next_recirc---------3---------------------
deea94d8_0a48_4fce_bfbd_c2f1243e3a71-------)

in

[Oiler Network

](https://medium.com/oiler-network?source=read_next_recirc---------3
---------------------deea94d8_0a48_4fce_bfbd_c2f1243e3a71-------)

## Introducing Fossil

![](https://miro.medium.com/focal/112/112/50/50/1*Gh2SGPYm9hy4t0UAZ6f6Pg.png)](/oiler-
network/introducing-fossil-ce4c23ad17c4?source=read_next_recirc---------3
---------------------deea94d8_0a48_4fce_bfbd_c2f1243e3a71-------)

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

