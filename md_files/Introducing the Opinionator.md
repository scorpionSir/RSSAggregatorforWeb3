[](https://medium.com/)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/1d0bf0438aab&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](https://medium.com/)

[Home](https://medium.com/)

[Notifications](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![slock.it Blog](https://miro.medium.com/fit/c/64/64/1*ESYB-
YgQa2FKWPo2ofqCiQ.png)](https://blog.slock.it/?source=post_page-----
1d0bf0438aab--------------------------------)

Published in

[slock.it Blog

](https://blog.slock.it/?source=post_page-----
1d0bf0438aab--------------------------------)

[![Jonas
Bentke](https://miro.medium.com/fit/c/96/96/0*0kWq_v4ZL7sa8-sp.jpg)](https://medium.com/@jonas.bentke?source=post_page
-----1d0bf0438aab--------------------------------)

[Jonas Bentke](https://medium.com/@jonas.bentke?source=post_page-----
1d0bf0438aab--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fe21dab5c1913&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fintroducing-
the-
opinionator-1d0bf0438aab&user=Jonas+Bentke&userId=e21dab5c1913&source=post_page-e21dab5c1913
----1d0bf0438aab---------------------follow_byline-----------)

Aug 21, 2019

·

7 min read

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F1d0bf0438aab&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fintroducing-
the-
opinionator-1d0bf0438aab&source=--------------------------bookmark_header-----------)

[

Save

](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F1d0bf0438aab&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fintroducing-
the-
opinionator-1d0bf0438aab&source=--------------------------bookmark_header-----------)

#  **Introducing the Opinionator**

![](https://miro.medium.com/max/1400/1*QcsoNc68VPOB0wAYSEAJEA.jpeg)

Image by Gerd Altmann from Pixabay

The DAO marked a milestone in the history of slock.it, but also brought to
light many questions that the Ethereum community hadn’t fully considered
before. One of the biggest questions is: How should we make decisions that
affect hundreds of thousands of people? We at slock.it have been working on an
opinion collection tool to capture the views of the community based on all the
available information on the Ethereum blockchain.

 **Why We Need It**

Currently, many voting tools used in the community weight your vote based on
the amount of Ether you possess. This might work well to get a first glance of
what investors want, but it does not capture the whole picture. Although it’s
generally acknowledged that oligarchies are not an ideal way to govern a
public good, there are still many stakeholders that are not considered in the
voting process. Let’s look at an example:

Alice is a student currently studying in beautiful Mittweida, trying to finish
her master’s degree in distributed ledger technology. During her free time,
she creates a contract that enables users to play a game based on the Ethereum
blockchain. She does it for fun, not for profit. The game takes off and
thousands of people start using her contract. Alice does not have tons of
Ether lying around to make a difference in a coin based vote, but she
certainly has a lot to lose if the blockchain changes in a way that will
affect her players.

Now have a look at Bob. He knows Alice and tells her about an open-source
smart contract library that he wrote and deployed to the mainnet. Alice
decides to use this library in her blockchain game. Bob doesn’t have much
Ether, but a lot of people use his library. Shouldn’t he have a say in what’s
going on?

Moreover, what do all those casual gamers have to say? They don’t hodl — they
spend their Ether to play the game and drive the chain through the gas they
spend. Surely, they also should have a say.

That’s why we developed the Opinionator.

 **What can it do**

So, what does the Opinionator do differently from all the other voting tools
out there? For starters, we don’t view it as a voting tool, but as an opinion
collection tool. Furthermore, it considers a lot more than just the amount of
ETH you have.

Looking back at Alice and Bob, we can see that counting Ether does not really
help them get their opinions registered. But what does? Alice and Bob are
developers whose contracts are used hundreds of times a day. People are
spending money to use those contracts. Why don’t we measure that?

That’s exactly what we did. We developed a tool that measures the weight of
your vote based on four main attributes extracted from the blockchain: the
amount of Ether you possess, the amount of gas you’ve spent, the amount of gas
spent using your contract, and the accumulated difficulty you’ve solved for
creating a block. Here is a quick rundown on what each of these four
components means:

  *  _Amount of Ether you possess._ Although the weight of your vote isn’t based primarily on how much Ether you have, it is still a factor that needs to be considered while making decisions.
  *  _Amount of gas you’ve spent._ If you actually use Ether the way it was designed to be used, why should you have less of a say than someone who is just hodling? Every unit of gas ever spent by an address is accumulated and used to weight your vote.
  *  _Gas spent on your contract._ This is where Alice and Bob really shine. They created value and usability for the network, which will reflect in their voting power. The Opinionator dissects every trace in every transaction and finds the gas value spent on your contract. If Charlie uses Alice’s contract, which then calls Bob’s library, the gas spent on the library call will be counted toward Bob, the rest toward Alice, and Charlie gets the total amount of gas spent for himself.
  *  _Accumulated difficulty_. Without our miner friends, nothing would go, so let’s let them have a say. Since it was way easier to solve a block early in Ethereum’s history, we can’t simply count the number of blocks found. Instead, we measure the difficulty the miner had to solve to create the block.

 **How can I use it**

At this point, you may be wondering: “What does a vote actually look like? Do
I have to spend money to vote?” No! Voting is free. Here is what you do:

First, go to [voting.slock.it](http://voting.slock.it) and pick a poll and
then click on “Click here to vote”.

![](https://miro.medium.com/max/1400/1*n1uDZU3iRNHCknKG5wlBEA.png)

Choose what and how you want to sign. The most straightforward method is to
use MetaMask. If you don’t use MetaMask, you can sign the vote yourself and
paste your address and the signature of the vote into the appropriate fields.

![](https://miro.medium.com/max/1340/1*x36hgqYAL-5cJdbY57AA1g.png)

Click the Sign button to complete your vote.

![](https://miro.medium.com/max/1310/1*uHoSNsbF3aHCGEcxY74NSA.png)

![](https://miro.medium.com/max/1318/1*JjTYJLSZ5yAd9DxNhez0Pw.png)

You will get a receipt (explained below) and then you’re done!

![](https://miro.medium.com/max/1328/1*CupFNnABtEENKXEJzHoY5g.png)

How you sign the message is totally up to you. One easy way is to use
[myetherwallet.com](https://vintage.myetherwallet.com/signmsg.html) since it
supports all common ways to import your precious private keys.

“But how can I trust that you are actually using my vote when you store all
the votes off-chain?” We’ve got you covered. With the current system, it’s not
very convenient to store every vote on-chain, but we made sure you can prove
we counted your vote.

Here’s how it works. Each vote is made public through our
[API](https://voting.slock.it/api/votes), where you can find all given votes.
To make sure the numbers reflect your vote, we give you a signed receipt. That
receipt is simply your signed vote signed by us. That way, we show you we
received your vote and ensure you can’t just claim to have voted even when you
didn’t (trust goes both ways). With this information, you can count the votes
yourself since all the necessary information to prove or disprove is now
public.

You can also create your own polls. Polls and proposals are stored on the
blockchain, which means that this will create transaction costs for you. You
can create simple yes/no polls or craft your own proposals. Once you create a
poll, you can use the admin functions there to create your proposals (for
those that aren’t yes/no polls).

One last word about the start and end date of a poll. If you leave the start
date blank, it will start straight away. If you leave the end date blank it
will never end. As soon as a poll ends, no one will be able to vote on it
again.

 **How did we do it**

The Opinionator consists of 4 crucial parts.

  1. The Importer
  2. The Database
  3. The Backend
  4. The UI

We used Parity Ethereum as our Ethereum client. (It is not as easy as you
might think to run a full archive node. If you want to know more, read the
blog post by our Big Data Guru, Markus.)

The first step is to get all that blockchain data into the database. For this,
we wrote an importer that takes every block apart, sorts it, and writes it to
the database. For this, it requests the data via IPC from the Parity node.
First, we take the block and parse out each transaction, including its traces.
All of that is then stuffed into the MongoDB database. That data can be
retrieved by our backend, which uses some huge queries to get what we want.
After a lot of database optimization, we got it down to usable response times.
Just to give you a glimpse of what we have to do: To get the amount of gas
spent on a contract, we must find every trace that addresses the contract and
subtract every subsequent trace from it.

The backend is giving us the raw data from the database. That is useful but
doesn’t go far enough. So we wrote a user interface that enables you to
visualize that data in as many ways as you want. You want to know how the poll
turned out when you split the weight evenly with 50% importance tied to Ether
holdings and 50% tied to gas use? Or what happens when you configure the
weights to 10% Ether, 47% gas, 38% developer, and 5% miner? The Opinionator
can show you all of that, ensuring you get the whole picture of who wants
what. If you think your poll is more important to developers, check out what
they say. If you think it’s only important to miners, have a look. It’s that
simple.

![](https://miro.medium.com/max/1400/1*hk0wZLf93Ufh-EqqiQCcVA.png)

![](https://miro.medium.com/max/1400/1*QOqNhxni7jbkBzdanoPvVw.png)

 **Conclusion**

That’s it. Now you can find out what people think in the Ethereum community.
Share the URL from your poll via social media to make sure your followers know
what’s going on, and you are set to go.

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fslock-
it-
blog%2F1d0bf0438aab&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fintroducing-
the-
opinionator-1d0bf0438aab&user=Jonas+Bentke&userId=e21dab5c1913&source=-----1d0bf0438aab
---------------------clap_footer-----------)

\--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fslock-
it-
blog%2F1d0bf0438aab&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fintroducing-
the-
opinionator-1d0bf0438aab&user=Jonas+Bentke&userId=e21dab5c1913&source=-----1d0bf0438aab
---------------------clap_footer-----------)

\--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fslock-
it-
blog%2F1d0bf0438aab&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fintroducing-
the-
opinionator-1d0bf0438aab&user=Jonas+Bentke&userId=e21dab5c1913&source=-----1d0bf0438aab
---------------------clap_footer-----------)

\--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F1d0bf0438aab&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fintroducing-
the-
opinionator-1d0bf0438aab&source=--------------------------bookmark_footer-----------)

## [More from slock.it Blog](https://blog.slock.it/?source=post_page-----
1d0bf0438aab--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Fslock-
it-
blog%2F1d0bf0438aab&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fintroducing-
the-
opinionator-1d0bf0438aab&collection=slock.it+Blog&collectionId=15115b6d917a&source=post_page
-----1d0bf0438aab---------------------follow_footer-----------)

IoT + Blockchain

[Read more from slock.it Blog](https://blog.slock.it/?source=post_page-----
1d0bf0438aab--------------------------------)

## Recommended from Medium

[[![Alchemist
Warden](https://miro.medium.com/fit/c/40/40/1*w33vKw4HeHxh44q5GuDZ1g@2x.jpeg)](https://medium.com/@alchemist.warden?source=post_internal_links
---------0----------------------------)

[Alchemist Warden

](https://medium.com/@alchemist.warden?source=post_internal_links---------
0----------------------------)

in

[WARDEN Official

](https://medium.com/wardenofficial?source=post_internal_links---------
0----------------------------)

## Weekly Update Q1/1–2

![](https://miro.medium.com/focal/112/112/50/50/1*XAW5YwnmTNk6twwzhkzrKA.png)](https://medium.com/wardenofficial/weekly-
update-q1-1-2-3fe35e66553b?source=post_internal_links---------
0----------------------------)

[[![bidcoin](https://miro.medium.com/fit/c/40/40/2*ZOzUpALAdJaSN61GBEaCQQ.png)](https://medium.com/@bidcoin?source=post_internal_links
---------1----------------------------)

[bidcoin

](https://medium.com/@bidcoin?source=post_internal_links---------
1----------------------------)

## What is Bidcoin ?

![](https://miro.medium.com/focal/112/112/50/50/1*MGdPkrIudfsF9mQY9qbypw.png)](https://medium.com/@bidcoin/what-
is-bidcoin-ca801e933b8b?source=post_internal_links---------
1----------------------------)

[[![Team
Dopex](https://miro.medium.com/fit/c/40/40/1*8f8t-FvO44mmWk5OX4wh4Q.png)](https://teamdopex.medium.com/?source=post_internal_links
---------2----------------------------)

[Team Dopex

](https://teamdopex.medium.com/?source=post_internal_links---------
2----------------------------)

in

[Dopex

](https://blog.dopex.io/?source=post_internal_links---------
2----------------------------)

## Announcement: Dopex (DPX) Public Token Sale!

![](https://miro.medium.com/focal/112/112/50/50/0*Gvs2iQGJg828BuQY)](https://blog.dopex.io/announcement-
dopex-dpx-public-token-sale-81b36d67b7f6?source=post_internal_links---------
2----------------------------)

[[![scubalive](https://miro.medium.com/fit/c/40/40/1*dmbNkD5D-u45r44go_cf0g.png)](https://medium.com/@drogpooresttu1971?source=post_internal_links
---------3----------------------------)

[scubalive

](https://medium.com/@drogpooresttu1971?source=post_internal_links---------
3----------------------------)

## Gold Club Casino $30 Free Chip

](https://medium.com/@drogpooresttu1971/gold-club-casino-30-free-
chip-4a842b09a25a?source=post_internal_links---------
3----------------------------)

[[![ScrumbleGames](https://miro.medium.com/fit/c/40/40/1*MKbG3vkfTRsyjvz5u4v-nw.png)](https://medium.com/@owenburke_12019?source=post_internal_links
---------4----------------------------)

[ScrumbleGames

](https://medium.com/@owenburke_12019?source=post_internal_links---------
4----------------------------)

## Envion — Worlds Most Profitable Standard!

![](https://miro.medium.com/focal/112/112/50/50/1*BpC7psZILeeVOGl3AUSPnw.png)](https://medium.com/@owenburke_12019/envion-
worlds-most-profitable-standard-1a57aa9491d?source=post_internal_links
---------4----------------------------)

[[![Vetter](https://miro.medium.com/fit/c/40/40/1*AtmqvEGAmwsX2H741xuAYw.png)](https://medium.com/@vetterecosystem?source=post_internal_links
---------5----------------------------)

[Vetter

](https://medium.com/@vetterecosystem?source=post_internal_links---------
5----------------------------)

## Does crowd sourcing intelligence work?

](https://medium.com/@vetterecosystem/does-crowd-souring-intelligence-
work-9fd8ed57553d?source=post_internal_links---------
5----------------------------)

[[![Stefan
Beyer](https://miro.medium.com/fit/c/40/40/1*44NXo0JzFdf79ls48QE_EA.jpeg)](https://medium.com/@stbeyer?source=post_internal_links
---------6----------------------------)

[Stefan Beyer

](https://medium.com/@stbeyer?source=post_internal_links---------
6----------------------------)

in

[Cryptonics

](https://medium.com/cryptronics?source=post_internal_links---------
6----------------------------)

## Smart Contract Security Audits — An Experience Report

![](https://miro.medium.com/focal/112/112/50/50/1*wyX-
VsShVXNjCXjxK2gjHA.jpeg)](https://medium.com/cryptronics/smart-contract-
security-audits-an-experience-report-e3e56a0cc04c?source=post_internal_links
---------6----------------------------)

[[![Suse
Joe](https://miro.medium.com/fit/c/40/40/0*howH0pryi37LO0dD.)](https://medium.com/@shadyjay_99981?source=post_internal_links
---------7----------------------------)

[Suse Joe

](https://medium.com/@shadyjay_99981?source=post_internal_links---------
7----------------------------)

## INTRODUCTION

![](https://miro.medium.com/focal/112/112/50/50/1*FsaNqq15Jk96zBzVqrLPxg.png)](https://medium.com/@shadyjay_99981/introduction-51353759e276?source=post_internal_links
---------7----------------------------)

[](https://medium.com/?source=post_page-----
1d0bf0438aab--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
1d0bf0438aab--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
1d0bf0438aab--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
1d0bf0438aab--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
1d0bf0438aab--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----1d0bf0438aab--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----1d0bf0438aab--------------------------------)

[Get
started](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fintroducing-
the-opinionator-1d0bf0438aab&source=post_page--------------------------
nav_reg-----------)

[![Jonas
Bentke](https://miro.medium.com/fit/c/176/176/0*0kWq_v4ZL7sa8-sp.jpg)](https://medium.com/@jonas.bentke)

[

## Jonas Bentke

](https://medium.com/@jonas.bentke)

3 Followers

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fe21dab5c1913&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fintroducing-
the-
opinionator-1d0bf0438aab&user=Jonas+Bentke&userId=e21dab5c1913&source=post_page-e21dab5c1913
-------------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fusers%2Fe21dab5c1913%2Flazily-
enable-writer-
subscription&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fintroducing-
the-
opinionator-1d0bf0438aab&user=Jonas+Bentke&userId=e21dab5c1913&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Master
Ventures](https://miro.medium.com/fit/c/40/40/1*FJIUYrUpYcWRy8xnrWZk-g.png)](https://masterventures.medium.com/?source=read_next_recirc
---------0---------------------c1d5d7e6_5064_4f38_a84f_e4591648abdc-------)

[Master Ventures

](https://masterventures.medium.com/?source=read_next_recirc---------0
---------------------c1d5d7e6_5064_4f38_a84f_e4591648abdc-------)

## The Current State of DeFi Security

![](https://miro.medium.com/focal/112/112/50/50/1*6C6jjyBF-b3M-LnO8dR8hw.jpeg)](https://masterventures.medium.com/the-
current-state-of-defi-security-3f8d4cf422b8?source=read_next_recirc---------0
---------------------c1d5d7e6_5064_4f38_a84f_e4591648abdc-------)

[[![plebbit](https://miro.medium.com/fit/c/40/40/1*oRFV9KX5zxR62_9ZtwPV2g.png)](https://medium.com/@plebbit?source=read_next_recirc
---------1---------------------c1d5d7e6_5064_4f38_a84f_e4591648abdc-------)

[plebbit

](https://medium.com/@plebbit?source=read_next_recirc---------1
---------------------c1d5d7e6_5064_4f38_a84f_e4591648abdc-------)

## Plebbit receives grant from Protocol Labs (IPFS/ETH2/Filecoin) to build
decentralized Reddit…

![](https://miro.medium.com/focal/112/112/50/50/1*2fjE5cxYTUvqSw5mqQm-0Q.png)](https://medium.com/@plebbit/plebbit-
receives-grant-from-protocol-labs-ipfs-eth2-filecoin-to-build-decentralized-
reddit-3173413f274?source=read_next_recirc---------1---------------------
c1d5d7e6_5064_4f38_a84f_e4591648abdc-------)

[[![DegenTech](https://miro.medium.com/fit/c/40/40/1*aBRDLHOaDBhNr4g3j08R4w.png)](https://degentech.medium.com/?source=read_next_recirc
---------2---------------------c1d5d7e6_5064_4f38_a84f_e4591648abdc-------)

[DegenTech

](https://degentech.medium.com/?source=read_next_recirc---------2
---------------------c1d5d7e6_5064_4f38_a84f_e4591648abdc-------)

## [DegenTech] Important announcement about Aliens.farms

![](https://miro.medium.com/focal/112/112/50/50/1*Rn3r0OSrj8p5Cu-
sAeOQmw.png)](https://degentech.medium.com/degentech-important-announcement-
about-aliens-farms-16aaa7eff867?source=read_next_recirc---------2
---------------------c1d5d7e6_5064_4f38_a84f_e4591648abdc-------)

[[![Financely
Group](https://miro.medium.com/fit/c/40/40/1*bxcz0JDoHPsYnPXWc2f4UQ.jpeg)](https://financelygroup.medium.com/?source=read_next_recirc
---------3---------------------c1d5d7e6_5064_4f38_a84f_e4591648abdc-------)

[Financely Group

](https://financelygroup.medium.com/?source=read_next_recirc---------3
---------------------c1d5d7e6_5064_4f38_a84f_e4591648abdc-------)

## Emerging markets.

](https://financelygroup.medium.com/emerging-
markets-95e3e3f0460c?source=read_next_recirc---------3---------------------
c1d5d7e6_5064_4f38_a84f_e4591648abdc-------)

[Help

](https://help.medium.com/hc/en-us)

[Status

](https://medium.statuspage.io)

[Writers

](https://about.medium.com/creators/)

[Blog

](https://blog.medium.com)

[Careers

](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e)

[Privacy

](https://policy.medium.com/medium-privacy-policy-f03bf92035c9)

[Terms

](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f)

[About

](https://medium.com/about?autoplay=1)

[Knowable

](https://knowable.fyi)

