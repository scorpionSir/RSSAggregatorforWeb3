[](https://medium.com/)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/d038b4da398b&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](https://medium.com/)

[Home](https://medium.com/)

[Notifications](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![slock.it Blog](https://miro.medium.com/fit/c/64/64/1*ESYB-
YgQa2FKWPo2ofqCiQ.png)](https://blog.slock.it/?source=post_page-----
d038b4da398b--------------------------------)

Published in

[slock.it Blog

](https://blog.slock.it/?source=post_page-----
d038b4da398b--------------------------------)

[![Markus Keil](https://miro.medium.com/fit/c/96/96/0*GlDBIC-
dIsbsqYLI)](https://medium.com/@markus.keil?source=post_page-----
d038b4da398b--------------------------------)

[Markus Keil](https://medium.com/@markus.keil?source=post_page-----
d038b4da398b--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fff05ccdbed9a&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fhow-
to-not-run-an-ethereum-archive-node-a-
journey-d038b4da398b&user=Markus+Keil&userId=ff05ccdbed9a&source=post_page-
ff05ccdbed9a----d038b4da398b---------------------follow_byline-----------)

Jan 18, 2019

·

7 min read

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fd038b4da398b&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fhow-
to-not-run-an-ethereum-archive-node-a-
journey-d038b4da398b&source=--------------------------bookmark_header-----------)

[

Save

](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fd038b4da398b&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fhow-
to-not-run-an-ethereum-archive-node-a-
journey-d038b4da398b&source=--------------------------bookmark_header-----------)

#  **How to (not) run an Ethereum Archive Node — A Journey**

Here at Slock.it we provide RPC services for our developers.

You can think of it as an internal Infura.

We decided to run at least one archive node per Ethereum blockchain that we
work with regularly.  
That approach worked fine for smaller chains like Kovan, Ropsten or Tobalaba,
but the Mainnet gave us a real headache.

For those chains, running an archive node just meant, starting Parity with the
proper command line switches, waiting a few days and we’re ready to let the
developers use it.

## What is an archive node, anyways?

Before we start our journey I want to specify what an “archive node” actually
is for us.

 _tl;dr; it’s — pruning=archive — fat-db=on — tracing=on (using parity)_

But what does this all mean? Is it important to enable all this?

For normal blockchain operations where you don’t want to dig into history or
have all the data available at your fingertips, you don’t need an archive
node.

So most users will be satisfied with a warp-synced pruned node, but if you’re
doing R&D, it really helps to have everything readily available.

So let’s analyze the command line from above:

  * — pruning=archive -> This directs Parity to maintain all the states in the state-trie. Normally it only keeps the states for the last few blocks.  
So every time the global state changes (a balance changes or the storage of a
contract), it is recorded on-chain. So it becomes quite large over time.

  * — fat-db=on -> this doesn’t mean we put Parity’s internal database on a fast food only diet, but it has the same effect. It will roughly double the amount of data stored in the state database. The reason for this is that it stores additional information to be able to enumerate all accounts and storage keys that are on the chain.
  * — tracing=on -> This enables Parity’s transaction tracing by default, and you can get the EVM trace of each transaction without having to replay it.

As you see, much of this is just trading disk space for expensive computation.

To clarify for the “Ethereum full nodes need 2TB maximalists”. You can think
of an archive node as a full node with a super heavy cache enabled. A normal
full node, such as the pruned parity node, has all data needed to recompute
all the data of the archive node, we just want it faster so we store and
compute absolutely everything.

Now that we know what an archive node is and what it’s good for, let’s see how
we can run one.

##  **Episode I to III: The (bad) prequels**

From the word on the Ethereum streets, we knew that an archive node would
probably require a couple hundred gigabytes of storage and should be on SSDs
and not on spinning rust.

That was easy to arrange. We got a hold of the most bang-per-buck SSD VPS we
could find.

The Specs looked beefy enough: 10 Cores, 50 GB RAM and a whopping 1.2 TB of
SSD storage. Should be plenty, right?

After we had started Parity with the flags mentioned above, we sat down and
the first couple of thousand blocks flew by. 1000 blocks per second. Nice!

After about 3–4 days (this number comes from my faded memory, so don’t nail me
down on it) we hit the Shanghai DoS attack and dropped to 10 blocks per
second.

 **Meh!**

We let it run a few more days; and after 2 weeks (still syncing) we got a
warning from our monitoring about free disk space.

If I remember correctly, we were at 4 to 4.5 million blocks (or was it only
3.something?) — doesn’t matter really. But what mattered was the fact that
with only slightly more than half the chain synced, we nearly reached the
capacity of 1.2 TB.

So we looked around if there was any other provider that would give us
terabytes of fast SSD storage on the cheap.

Sure, we could just have went to AWS or Azure and paid them tons of blockchain
money, but this would have meant waiting longer for the Lambos. No way! Lambos
are important!

So we came up with this interesting idea of using a jerry rigged hybrid
solution.

(Disclaimer: Yes, I know we could have dug through the code of Parity and
RocksDB to find out that this was kind of a stupid idea, but where’s the fun
in that?)

The basic assumption of this idea was: All this data is there for historical
purposes. Parity shouldn’t touch “old” data and should only work with the
latest states.

This meant that we came up with a plan to build a hybrid storage solution from
cheap VPS’s by using an SSD based VPS with a smaller SSD and then a large SAS
RAID-based HDD system with enough storage for the (what we presumed) cold
data.

We created this using an overlay file system where we mounted the volume of
the SAS HDDs over the network as read-only and then overlaid the local SSD
storage as an R/W layer.

This means that every write goes to the SSD and every read is tried on the SSD
first and if it’s not there, is read from the network storage.

So far so good. After we managed to get the hybrid running (this topic could
easily fill another blog post), Parity worked just fine and started to sync
blocks.

After a while, it started reading an awful lot of data from the network disk.
We let it continue. Over time it ramped up in blocks/second sync speed, but
then the smaller SSD (it was not on the aforementioned SSD VPS for various
reasons) filled up and I had to move the newer files from SSD to HDD to make
room for new stuff. It got a nice daily routine. Stop Parity, move files,
start again, wait for monitoring to complain again, repeat.

But as it chewed through the blocks, it started to get painstakingly slow; to
a point where the sync speed dropped to only 1–3 blocks per MINUTE. No chance
we could catch mainnet with that.

We said: Ok this is pointless. Running an archive node on an inexpensive VPS
was not an option.

##  **Episode IV: A new hope!**

After these attempts, we decided to build our own machine that would run our
mainnet archive node.

![](https://miro.medium.com/max/1400/1*ctRGGoNHBtcM_lvB83ihcA.jpeg)

The Ingredients for our mainnet archive node

From our experience, the main bottleneck seemed to be iops and disk space.

And these were the final specs:

  * 4x 1TB Samsung 960 EVO NVMe SSDs
  * 1x Highpoint NVMe Raid card
  * A Ryzen 5 processor
  * 16 gigs of ram
  * and a small 240 gig boot SSD

![](https://miro.medium.com/max/1400/1*DCIfWZqecjIcO2D27Eaffg.jpeg)

The RAID Card with all 4 SSDs installed — An I/O Beast

The Samsung SSDs were put into a ZFS raidZ configuration, so even if one died
we’d still have the chain and we would have almost 3TB of NVMe SSD space for
the chain.

So we started Parity (as the only process on this box) and let it rip through
the chain. The sync speeds were quite good. 10 to 20 times increase to the
first VPS.

But even after 3 weeks it was still not finished…

##  **Episode V: The Empire strikes back**

At the moment we’re still ~900k blocks behind the main chain (which was at
around block 6,600,000 when I was writing this post). sync rates have dropped
to a measly 1–1.5 blocks/second since the high-volume blocks of early 2018.

It is quite a mystery why it is so slow. Disk I/O is at 160MB/s read
throughput all the time (the NVMe RAID can easily output 2GB/s random reads)
and very low CPU usage.

One explanation we came up with is that RocksDB has now 1.2TB to juggle with
and Parity may need to read from that dataset once every block. It seems that
each query has to crunch through a huge index to find what it’s looking for.

We thought we were defeated! We thought a parity node with all the state
history will not happen.

## Episode VI: Return of the Jedi

We abandoned the idea for a couple of weeks. But then Afri Schoedon started
writing about the differences of full vs. archived nodes and that is still
possible to run an archived node. One just has to be patient. Very patient.

So we took another go at this and resumed our archive sync in early December
2018. And what do you know? a couple days before Christmas we finally achieved
sync! The gift of archive sync!

So it is possible to have an archived Ethereum node running and Iguess you can
get away with lower specs as well.

We accumulated 1.94 TB on our ZFS. And we have ~550GB to spare.  
Also, we started the sync in October (but had some weeks where we paused).

So it’s not a matter of hours or days. It’s a matter of weeks, but as stated
above: Unless you really need all the states or a “because we can” you’ll be
much faster with a full node using the pruned states.

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fslock-
it-
blog%2Fd038b4da398b&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fhow-
to-not-run-an-ethereum-archive-node-a-
journey-d038b4da398b&user=Markus+Keil&userId=ff05ccdbed9a&source=-----d038b4da398b
---------------------clap_footer-----------)

\--

5

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fslock-
it-
blog%2Fd038b4da398b&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fhow-
to-not-run-an-ethereum-archive-node-a-
journey-d038b4da398b&user=Markus+Keil&userId=ff05ccdbed9a&source=-----d038b4da398b
---------------------clap_footer-----------)

\--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fslock-
it-
blog%2Fd038b4da398b&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fhow-
to-not-run-an-ethereum-archive-node-a-
journey-d038b4da398b&user=Markus+Keil&userId=ff05ccdbed9a&source=-----d038b4da398b
---------------------clap_footer-----------)

\--

5

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fd038b4da398b&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fhow-
to-not-run-an-ethereum-archive-node-a-
journey-d038b4da398b&source=--------------------------bookmark_footer-----------)

## [More from slock.it Blog](https://blog.slock.it/?source=post_page-----
d038b4da398b--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Fslock-
it-
blog%2Fd038b4da398b&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fhow-
to-not-run-an-ethereum-archive-node-a-
journey-d038b4da398b&collection=slock.it+Blog&collectionId=15115b6d917a&source=post_page
-----d038b4da398b---------------------follow_footer-----------)

IoT + Blockchain

[Read more from slock.it Blog](https://blog.slock.it/?source=post_page-----
d038b4da398b--------------------------------)

## Recommended from Medium

[[![Derby
Stars](https://miro.medium.com/fit/c/40/40/1*mKdHRzao8P1CKwP7RFvDxg.png)](https://medium.com/@DerbyStars?source=post_internal_links
---------0----------------------------)

[Derby Stars

](https://medium.com/@DerbyStars?source=post_internal_links---------
0----------------------------)

## Derby Stars Closes Seed Round Co-led by Patron and Galaxy Interactive

![](https://miro.medium.com/focal/112/112/48/33/1*qGPXbK0f0-5q8Lhxbn6Qrw.png)](https://medium.com/@DerbyStars/derby-
stars-closes-seed-round-co-led-by-patron-and-galaxy-interactive-
dc69969e2892?source=post_internal_links---------0----------------------------)

[[![Tanyaa
Sharma](https://miro.medium.com/fit/c/40/40/1*RSLbSEB6TGO1goPEK5K6yQ.jpeg)](https://tanyaasharma90.medium.com/?source=post_internal_links
---------1----------------------------)

[Tanyaa Sharma

](https://tanyaasharma90.medium.com/?source=post_internal_links---------
1----------------------------)

## How Blockchain Technology Empowering New Search Engine Tools:

](https://tanyaasharma90.medium.com/how-blockchain-technology-empowering-new-
search-engine-tools-5dd0b951214d?source=post_internal_links---------
1----------------------------)

[[![APEX Team](https://miro.medium.com/fit/c/40/40/1*tchCSGdy6OU-
sRiLks5kRw.jpeg)](https://apexteam.medium.com/?source=post_internal_links
---------2----------------------------)

[APEX Team

](https://apexteam.medium.com/?source=post_internal_links---------
2----------------------------)

in

[APEX Network

](https://medium.com/apex-network?source=post_internal_links---------
2----------------------------)

## APEX Network — Behind the Scenes #4 — The Community Management team picks
Jimmy Hu’s brain

![](https://miro.medium.com/focal/112/112/50/50/1*JwidvjfYZ_aKtKTU2_-PrA.png)](https://medium.com/apex-
network/apex-network-behind-the-scenes-4-the-community-management-team-picks-
jimmy-hus-brain-a643451e45eb?source=post_internal_links---------
2----------------------------)

[[![Toroabasi
Etim](https://miro.medium.com/fit/c/40/40/1*dmbNkD5D-u45r44go_cf0g.png)](https://medium.com/@toroabasietim909?source=post_internal_links
---------3----------------------------)

[Toroabasi Etim

](https://medium.com/@toroabasietim909?source=post_internal_links---------
3----------------------------)

## Why Invest in MATRIX ETF ?

](https://medium.com/@toroabasietim909/why-invest-in-matrix-
etf-1dd9627a1870?source=post_internal_links---------
3----------------------------)

[[![taijusanagi](https://miro.medium.com/fit/c/40/40/1*TyzT6SOAfooelamY8cD9IA.jpeg)](https://medium.com/@taijusanagi?source=post_internal_links
---------4----------------------------)

[taijusanagi

](https://medium.com/@taijusanagi?source=post_internal_links---------
4----------------------------)

in

[BlockBaseLab

](https://medium.com/blockbase?source=post_internal_links---------
4----------------------------)

## BlockBaseLab - Blockchain Peer Learning Community

![](https://miro.medium.com/focal/112/112/50/50/1*_-771wsdhBxW2hWCv3HyxQ.png)](https://medium.com/blockbase/introduce-
blockchain-peer-learning-community-84de3bb0092d?source=post_internal_links
---------4----------------------------)

[[![WINiota](https://miro.medium.com/fit/c/40/40/0*0FNCWc7QzTbS5VLQ.jpg)](https://medium.com/@WINiota_42868?source=post_internal_links
---------5----------------------------)

[WINiota

](https://medium.com/@WINiota_42868?source=post_internal_links---------
5----------------------------)

## WINiota -Disrupting the Establishment

![](https://miro.medium.com/focal/112/112/50/50/1*wN-IPR5qfXroO0ynP-
FmyQ.jpeg)](https://medium.com/@WINiota_42868/winiota-disrupting-the-
establishment-56609a6c19f6?source=post_internal_links---------
5----------------------------)

[[![Thomas
Kal](https://miro.medium.com/fit/c/40/40/1*sJxozu1FO7vCc7D_P_WdCQ.jpeg)](https://thomaskal.medium.com/?source=post_internal_links
---------6----------------------------)

[Thomas Kal

](https://thomaskal.medium.com/?source=post_internal_links---------
6----------------------------)

in

[OpenPredict

](https://medium.com/openpredict?source=post_internal_links---------
6----------------------------)

## OpenPredict Goes Chain-Agnostic, Starting with Binance Smart Chain

![](https://miro.medium.com/focal/112/112/50/50/1*oXHEfz4236O_DmXTvTVLYg.png)](https://medium.com/openpredict/openpredict-
goes-chain-agnostic-starting-with-binance-smart-chain-
cc5cef45ce98?source=post_internal_links---------6----------------------------)

[[![Joelle](https://miro.medium.com/fit/c/40/40/2*oe_0tsZTs0ASP6fWhzvGHQ@2x.png)](https://medium.com/@J0elle?source=post_internal_links
---------7----------------------------)

[Joelle

](https://medium.com/@J0elle?source=post_internal_links---------
7----------------------------)

## What do you need to know before Polkadot goes online? What do you want to
know about Acala?

![](https://miro.medium.com/focal/112/112/50/50/1*-7qhkAy-
LNjNdjcxBhbxzg.png)](https://medium.com/@J0elle/what-do-you-need-to-know-
before-polkadot-goes-online-what-do-you-want-to-know-about-
acala-6cb54977f9ab?source=post_internal_links---------
7----------------------------)

[](https://medium.com/?source=post_page-----
d038b4da398b--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
d038b4da398b--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
d038b4da398b--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
d038b4da398b--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
d038b4da398b--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----d038b4da398b--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----d038b4da398b--------------------------------)

[Get
started](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fhow-
to-not-run-an-ethereum-archive-node-a-journey-d038b4da398b&source=post_page
--------------------------nav_reg-----------)

[![Markus Keil](https://miro.medium.com/fit/c/176/176/0*GlDBIC-
dIsbsqYLI)](https://medium.com/@markus.keil)

[

## Markus Keil

](https://medium.com/@markus.keil)

16 Followers

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fff05ccdbed9a&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fhow-
to-not-run-an-ethereum-archive-node-a-
journey-d038b4da398b&user=Markus+Keil&userId=ff05ccdbed9a&source=post_page-
ff05ccdbed9a-------------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fusers%2Fff05ccdbed9a%2Flazily-
enable-writer-
subscription&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fhow-to-
not-run-an-ethereum-archive-node-a-
journey-d038b4da398b&user=Markus+Keil&userId=ff05ccdbed9a&source=--------------------------subscribe_user-----------)

## More from Medium

[[![AUFT
IO](https://miro.medium.com/fit/c/40/40/1*ExDAjrRfMweMEvhQ7uzKOA.png)](https://auft-
io.medium.com/?source=read_next_recirc---------0---------------------
d84a1351_051e_47a9_baa4_06a88120184f-------)

[AUFT IO

](https://auft-io.medium.com/?source=read_next_recirc---------0
---------------------d84a1351_051e_47a9_baa4_06a88120184f-------)

## Auft Alpha GUN.js/Gun.eco Integration. Why is it important?

![](https://miro.medium.com/focal/112/112/50/50/1*ohKv5n77BujzNnW_O-
PQ1g.png)](https://auft-io.medium.com/auft-alpha-gun-js-gun-eco-integration-
why-is-it-important-5be19b04bd8d?source=read_next_recirc---------0
---------------------d84a1351_051e_47a9_baa4_06a88120184f-------)

[[![Masayoshi
Mitsui](https://miro.medium.com/fit/c/40/40/1*kZa0rDP3em1gqPpzmbx_pg.jpeg)](https://masa256k1.medium.com/?source=read_next_recirc
---------1---------------------d84a1351_051e_47a9_baa4_06a88120184f-------)

[Masayoshi Mitsui

](https://masa256k1.medium.com/?source=read_next_recirc---------1
---------------------d84a1351_051e_47a9_baa4_06a88120184f-------)

in

[CollaboGate

](https://blog.getunid.io/?source=read_next_recirc---------1
---------------------d84a1351_051e_47a9_baa4_06a88120184f-------)

## Overview of DID Standards & Specs

![](https://miro.medium.com/focal/112/112/50/50/1*IJLZTrnGuRhmd6pobMRwdA.jpeg)](https://blog.getunid.io/overview-
of-did-standards-specs-3edef973fd30?source=read_next_recirc---------1
---------------------d84a1351_051e_47a9_baa4_06a88120184f-------)

[[![Julio Marques
Eman](https://miro.medium.com/fit/c/40/40/1*mKmi4i1JDhtaiWnxIdU-0w.jpeg)](https://medium.com/@juliomarqueseman?source=read_next_recirc
---------2---------------------d84a1351_051e_47a9_baa4_06a88120184f-------)

[Julio Marques Eman

](https://medium.com/@juliomarqueseman?source=read_next_recirc---------2
---------------------d84a1351_051e_47a9_baa4_06a88120184f-------)

## Airtrace 3.0 — Understanding Hyperledger Besu, the technology on the rise.

![](https://miro.medium.com/focal/112/112/50/50/1*aGbzCyyPZNgFo9epr_j25Q.png)](https://medium.com/@juliomarqueseman/airtrace-3-0-understanding-
hyperledger-besu-the-technology-on-the-rise-
fbe17acc9130?source=read_next_recirc---------2---------------------
d84a1351_051e_47a9_baa4_06a88120184f-------)

[[![aviva
vaknin](https://miro.medium.com/fit/c/40/40/1*LNzhZ49C4SMdJ_0HccZTxg.jpeg)](https://medium.com/@vakninaviva?source=read_next_recirc
---------3---------------------d84a1351_051e_47a9_baa4_06a88120184f-------)

[aviva vaknin

](https://medium.com/@vakninaviva?source=read_next_recirc---------3
---------------------d84a1351_051e_47a9_baa4_06a88120184f-------)

in

[cisco-fpie

](https://medium.com/cisco-fpie?source=read_next_recirc---------3
---------------------d84a1351_051e_47a9_baa4_06a88120184f-------)

## Decentralized Identities Demystified

![](https://miro.medium.com/focal/112/112/50/50/1*0Gh8AU7rleUFt5jC_JZTNg.png)](https://medium.com/cisco-
fpie/decentralized-identities-demystified-49a65159196c?source=read_next_recirc
---------3---------------------d84a1351_051e_47a9_baa4_06a88120184f-------)

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

