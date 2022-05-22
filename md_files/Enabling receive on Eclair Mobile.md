[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/2e1b87bd1e3a&~feature=LoOpenInAppButton&~channel=ShowPostUnderUser&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![ACINQ](https://miro.medium.com/fit/c/96/96/1*C_yfYIhszWi885XNVFxnkg.png)](/@ACINQ?source=post_page
-----2e1b87bd1e3a--------------------------------)

[ACINQ](/@ACINQ?source=post_page-----
2e1b87bd1e3a--------------------------------)

Follow

Feb 19, 2019

·

6 min read

# Enabling receive on Eclair Mobile

 **TL; DR:** We have enabled receive on [Eclair Mobile
Testnet](https://play.google.com/store/apps/details?id=fr.acinq.eclair.wallet)
0.4.0, with a background watcher mechanism and a basic liquidity service.

In [our last blog post](/@ACINQ/eclair-wallet-is-now-eclair-
mobile-e4d7eb2019a3) we explained the reasons which led us to limit Eclair
Mobile to only sending money until now. There were three of them:

  * For mobile users, the #1 use case for Lightning is to send payments;
  * It is far safer, because it saves us from monitoring the blockchain;
  * Inbound liquidity is necessary to receive funds and we don’t have the tools to address this yet.

In other words, if we want to enable receive on Eclair Mobile, the two main
problems are **security** and **liquidity**. Let’s see how we addressed them.

But before going into details, here is a quick demo of the receive experience:

Receive over Lightning on Eclair Mobile

# Monitoring the blockchain

## A note about watch towers

The go-to answer to monitoring the blockchain has often been watch towers.
When we first [released our app](/@ACINQ/announcing-eclair-
wallet-a8d8c136fc7e) in 2017, we hinted that “trustless third-party watchers”
would be how we would do it too. But there are a few catch 22s.

While it is already technically possible and even fairly easy to develop and
run such a watcher, operating one is challenging because the data needed to
watch a single channel isn’t constant size: watch towers need to store an ever
increasing amount of opaque data that needs to be indexed and is impossible to
compress…

It gets worse: because we don’t want to trust watch towers, we give them so
little information about channels, that they have no way to know when a
channel has been closed (so they can’t clean up data), or even if there is a
real channel in the first place. The latter opens the way to abuse and make it
even more difficult to operate a watch tower in a sustainable way.

It should be noted that the upcoming SIGHASH_NOINPUT opcode will make it
possible to have constant-size storage; there is no ETA though. There may also
be a way to offer this as a paying service, but it is easier said than done
and we haven’t found a model that was both acceptable for users and
economically viable.

For those reasons, we decided to not rely on watch towers for now. Here is how
we did it instead:

## Step 1: Having enough time to react

The first thing to do is to make sure that we have enough time to react if our
counterparty tries to cheat. As long as the wallet was send-only, we didn’t
really care, because publishing a revoked commitment would actually _give_ us
money, which is why the refund timeout was set to 144 blocks (~1 day) by
default.

For maximum safety, Eclair Mobile will now require a refund delay (a.k.a.
retaliation window) of 2016 blocks (~2 weeks) from its counterparties, which
is the highest value allowed by LN spec. This means that whatever happens,
your funds will be safe if you start Eclair Mobile at least once every two
weeks.

Note that as a consequence, when enabling the receive feature, Eclair Mobile
will ask you to close any channel that has a refund timeout smaller than that.
Any new channel you open will have the correct setting by default.

With that in place, we still need to have users start the app every two weeks,
which is not very satisfying. We could remind them to do so using periodic
notifications, but that’s not very satisfying either, and they would probably
quickly get annoyed.

This is why we added what we call a background watcher.

## Step 2: Adding a background watcher

Every now and then, Eclair Mobile will start a very lightweight background
task, that will connect to Electrum servers (or your own Electrum server if
you configured it), check if the funding transaction of any of your channel
has been spent, and raise an alarm if something fishy has been detected.

If all your funding transactions are still unspent, then everything is fine:
we are good for another two weeks, and there is no need to bother the user at
all.

Even if one of your funding transaction has been spent, but the spending
transactions is an expected one, such as a mutual or unilateral close, then
there is no need to do anything either for another two weeks.

In fact, the only time when the user will have to actually start the app is if
the spending tx is an actual cheating attempt (which hopefully will never
happen). Only in this case will the watcher send a notification to the user,
requesting them to start the app as soon as possible.

Note that depending on the brand and battery settings, some devices may
prevent the background watcher to operate reliably. If that is the case,
Eclair Mobile’s self-diagnostic feature will detect it and warn the user.

## Summary and tradeoffs

Our mechanism protects your funds without forcing you to trust a third party,
and with few requirements on your part. One of them is that your device must
be reasonably well connected to the internet. If you go off the grid for more
than two weeks, you should close your channels.

Even then, you could still rely on game theory: after all, your counterparties
have no way to know if you are online or not. Critically, our background
watcher doesn’t connect to them when checking the blockchain; just because
your channels stay inactive for weeks or months doesn’t mean that you are not
watching them.

If you lose your phone, then this is similar as going offline: you have two
weeks to restore your app on another phone, or your funds will be at risk. But
again, even if you take longer than two weeks, your counterparties cannot know
that they have an opportunity to defraud you.

Now that we have a way to secure our channels, the other main pain point was
liquidity.

# Getting Inbound liquidity

## Some context

When you want to send money over Lightning, you need to have a channel open
with money on your side of it. If you don’t have a channel, opening one is
pretty straightforward: you just need to connect to a peer on the network and
fund a new channel. Pretty much anybody will accept this incoming channel
request, as it doesn’t cost them anything.

When receiving money, that’s another story: this time your counterparty needs
to have funds on their side. Not everyone will want to put funds in a channel
to you, because it costs them money in locked capital, therefore there is an
incentive issue.

## The end goal

As we stated in our previous blog post, we believe that the combination of
[advertising your willingness to provide
liquidity](https://lists.linuxfoundation.org/pipermail/lightning-
dev/2018-November/001532.html) to other nodes (for a fee) with the ability to
dual fund channels is the proper way to address this issue.

But we don’t have it yet, so in the meantime we have tried to approach it with
what’s currently possible.

## In the mean time

The idea is to use the _push_msat_ (*) feature to pay in advance for incoming
liquidity. Starting from today, when you open a channel to our testnet node
(the venerable
[endurance](http://03933884aaf1d6b108397e5efe5c86bcf2d8ca8d2f700eda99db9214fc2712b134@34.250.234.192:9735)),
if you push funds, we will automatically open a channel back to your node.
This is a trusted dual funding, which is not ideal, even if you only trust us
with the push amount.

(*) This feature allows you to unconditionally send funds to your counterparty
when you open a channel with her.

The results looks a bit like a [Decker-
Wattenhofer](https://www.tik.ee.ethz.ch/file/716b955c130e6c703fac336ea17b1670/duplex-
micropayment-channels.pdf) setup with two channels, one with all the funds on
your side, an the other with all the funds on our side. An alternative to end
up with a single balanced channel would have been to require an upfront
payment of the total amount you wanted on your side, and then open a single
balanced channel, but (1) you would have had to trust us for far more money
and (2) we would still have to make two on-chain transactions, so it wouldn’t
have been less costly in terms of blockchain space.

Pricing for testnet has been set to 1% as an example, meaning that if you open
a channel with us and push 0.1mBTC worth of bitcoins, we will open a channel
to you and fund it with 10 mBTC. Here is what the UX looks like currently in
Eclair Mobile:

Requesting inbound liquidity from ACINQ node

# A call to testers

Receiving Ligthning payments is now possible with our testnet application
(version 0.4.0), and your feedback is welcome! We plan to add this option to
our mainnet application within a few weeks. In the meantime, happy testing!

\--

3

\--

\--

3

## [More from ACINQ](/@ACINQ?source=post_page-----
2e1b87bd1e3a--------------------------------)

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fcb6983c5b91b&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ACINQ%2Fenabling-
receive-on-eclair-
mobile-2e1b87bd1e3a&newsletterV3=74c0a4fc8ad0&newsletterV3Id=cb6983c5b91b&user=ACINQ&userId=74c0a4fc8ad0&source=-----2e1b87bd1e3a
---------------------subscribe_user-----------)

We are building an implementation of Lightning, a scalable instant payment
network built on top of the Bitcoin blockchain.

Love podcasts or audiobooks? Learn on the go with our new app.

[Try
Knowable](https://knowable.fyi/?utm_source=medium&utm_medium=referral&utm_campaign=medium-
post-footer&source=post_page-----2e1b87bd1e3a--------------------------------)

## Recommended from Medium

[[![Hexarchia](https://miro.medium.com/fit/c/40/40/1*agVGGhgv2nFuHz49uacmJQ.png)](/@hexarchia?source=post_internal_links
---------0----------------------------)

[Hexarchia

](/@hexarchia?source=post_internal_links---------
0----------------------------)

## Hexarchia: Genesis NFTs Whitelist

![](https://miro.medium.com/focal/112/112/50/50/1*YXwJqiQZode-
kW93ptSW1Q.jpeg)](/@hexarchia/hexarchia-genesis-nfts-
whitelist-1a8bdec37ac9?source=post_internal_links---------
0----------------------------)

[[![Noda
Network](https://miro.medium.com/fit/c/40/40/1*8HiF7icefEGjCE62spfykg.png)](/@nodanetwork?source=post_internal_links
---------1----------------------------)

[Noda Network

](/@nodanetwork?source=post_internal_links---------
1----------------------------)

## 🔥HURRY TO BUY NCN TOKENS! ☑️ Last day of IDO. Listing tomorrow!

![](https://miro.medium.com/focal/112/112/50/50/1*u3L2psY06au0-7ju7LofkA.jpeg)](/@nodanetwork/hurry-
to-buy-ncn-tokens-️-last-day-of-ido-listing-
tomorrow-e1365ac938eb?source=post_internal_links---------
1----------------------------)

[[![Zhen](https://miro.medium.com/fit/c/40/40/1*9Z8L1L4ABewgZsGwDFMDYA.jpeg)](/@ZhenIOST?source=post_internal_links
---------2----------------------------)

[Zhen

](/@ZhenIOST?source=post_internal_links---------2----------------------------)

in

[IOST

](https://medium.com/iost?source=post_internal_links---------
2----------------------------)

## IOST X Kindai University of Japan | HIVEHack Hackathon Is Now Open For
Everyone!

![](https://miro.medium.com/focal/112/112/50/50/0*tNb3lighcjA_L2v6)](/iost/iost-
x-kindai-university-of-japan-hivehack-hackathon-is-now-open-for-
everyone-4e14f0958446?source=post_internal_links---------
2----------------------------)

[[![Jack Plotkin](https://miro.medium.com/fit/c/40/40/2*n--
7ueUfr_kYkztuT-8yjg.jpeg)](/@plotkinjack151?source=post_internal_links
---------3----------------------------)

[Jack Plotkin

](/@plotkinjack151?source=post_internal_links---------
3----------------------------)

in

[Analytics Vidhya

](https://medium.com/analytics-vidhya?source=post_internal_links---------
3----------------------------)

## Blockchains in Healthcare: From Bitcoin to Bitcare

![](https://miro.medium.com/focal/112/112/50/50/1*dZoqW37TBut6pap8aw7fLQ.jpeg)](/analytics-
vidhya/blockchains-in-healthcare-from-bitcoin-to-
bitcare-36ce477f1a2?source=post_internal_links---------
3----------------------------)

[[![Bluzelle](https://miro.medium.com/fit/c/40/40/1*LNyfScSw8YljDxBD93gxzw.png)](/@bluzelle?source=post_internal_links
---------4----------------------------)

[Bluzelle

](/@bluzelle?source=post_internal_links---------4----------------------------)

in

[The Blueprint by Bluzelle

](https://medium.com/the-blueprint-bluzelle-blog?source=post_internal_links
---------4----------------------------)

## Introducing Bluzelle Oracles

![](https://miro.medium.com/focal/112/112/50/50/1*uxgVaMnq29UrIyukYi7Lcw.png)](/the-
blueprint-bluzelle-blog/introducing-bluzelle-
oracles-6b06c547d830?source=post_internal_links---------
4----------------------------)

[[![Derek
Fang](https://miro.medium.com/fit/c/40/40/0*LES062cfiXjybvj1.jpg)](/@derekgoogo?source=post_internal_links
---------5----------------------------)

[Derek Fang

](/@derekgoogo?source=post_internal_links---------
5----------------------------)

## Introducing SnailSwap, an AMM Dex which is deeply integrated with Cex

![](https://miro.medium.com/focal/112/112/50/50/1*GjAxdEtwc6oASekxyYU7pg.png)](/@derekgoogo/introducing-
snailswap-an-amm-dex-which-is-deeply-integrated-with-
cex-54a7cc0ce43a?source=post_internal_links---------
5----------------------------)

[[![Polkamarkets Labs](https://miro.medium.com/fit/c/40/40/1*PPK-
guusKU6CJXPaOSl2Rw.png)](/@polkamarkets?source=post_internal_links---------
6----------------------------)

[Polkamarkets Labs

](/@polkamarkets?source=post_internal_links---------
6----------------------------)

## An Exclusive Look At Polkamarkets, An Autonomous Prediction Markets
Protocol

![An Exclusive Look At Polkamarkets, An Autonomous Prediction Markets
Protocol](https://miro.medium.com/focal/112/112/50/50/1*FYeeWqY9OubohRwqqMESEw.jpeg)](/@polkamarkets/an-
exclusive-look-at-polkamarkets-993243b87a77?source=post_internal_links
---------6----------------------------)

[[![Giles Crouch | Digital
Anthropologist](https://miro.medium.com/fit/c/40/40/1*_Vgp-2S9h5LahHm87QTjuw.jpeg)](/@gilescrouch?source=post_internal_links
---------7----------------------------)

[Giles Crouch | Digital Anthropologist

](/@gilescrouch?source=post_internal_links---------
7----------------------------)

## How Can Blockchain Go Mainstream?

![](https://miro.medium.com/focal/112/112/50/50/1*PnDDokTwBQS84Em8DvcC3w.png)](/@gilescrouch/how-
can-blockchain-go-mainstream-6b7a0cad148f?source=post_internal_links---------
7----------------------------)

[](/?source=post_page-----2e1b87bd1e3a--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
2e1b87bd1e3a--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
2e1b87bd1e3a--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
2e1b87bd1e3a--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
2e1b87bd1e3a--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----2e1b87bd1e3a--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----2e1b87bd1e3a--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ACINQ%2Fenabling-
receive-on-eclair-mobile-2e1b87bd1e3a&source=post_page
--------------------------nav_reg-----------)

[![ACINQ](https://miro.medium.com/fit/c/176/176/1*C_yfYIhszWi885XNVFxnkg.png)](/@ACINQ)

[

## ACINQ

](/@ACINQ)

1.1K Followers

We are building an implementation of Lightning, a scalable instant payment
network built on top of the Bitcoin blockchain.

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fcb6983c5b91b&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40ACINQ%2Fenabling-
receive-on-eclair-
mobile-2e1b87bd1e3a&newsletterV3=74c0a4fc8ad0&newsletterV3Id=cb6983c5b91b&user=ACINQ&userId=74c0a4fc8ad0&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Elijah
G.](https://miro.medium.com/fit/c/40/40/0*rpguajXaW9vIhqfN.jpg)](/@greenerockvc?source=read_next_recirc
---------0---------------------7aa7e84a_e096_4f71_975e_0e8dca0a2f4c-------)

[Elijah G.

](/@greenerockvc?source=read_next_recirc---------0---------------------
7aa7e84a_e096_4f71_975e_0e8dca0a2f4c-------)

## Ethereum 2.0 (ETH2) Memo

](/@greenerockvc/ethereum-2-0-eth2-memo-9a449ce22b5e?source=read_next_recirc
---------0---------------------7aa7e84a_e096_4f71_975e_0e8dca0a2f4c-------)

[[![Harshit Verma](https://miro.medium.com/fit/c/40/40/1*YZE9mEEn9l5juO-
qpDJ3iA.jpeg)](/@harshit.verma?source=read_next_recirc---------1
---------------------7aa7e84a_e096_4f71_975e_0e8dca0a2f4c-------)

[Harshit Verma

](/@harshit.verma?source=read_next_recirc---------1---------------------
7aa7e84a_e096_4f71_975e_0e8dca0a2f4c-------)

## What is Ethereum and how does it work?

![](https://miro.medium.com/focal/112/112/50/50/1*1w6FxxpreQg1bIu6XHW4Iw.jpeg)](/@harshit.verma/what-
is-ethereum-and-how-does-it-work-65b5a2c30d47?source=read_next_recirc---------
1---------------------7aa7e84a_e096_4f71_975e_0e8dca0a2f4c-------)

[[![BlockApex](https://miro.medium.com/fit/c/40/40/1*9OehZq_96XPXT5qV65i7QQ.jpeg)](/@blockapex?source=read_next_recirc
---------2---------------------7aa7e84a_e096_4f71_975e_0e8dca0a2f4c-------)

[BlockApex

](/@blockapex?source=read_next_recirc---------2---------------------
7aa7e84a_e096_4f71_975e_0e8dca0a2f4c-------)

## Cryptocurrency: Cutting-edge or Criminal?

![](https://miro.medium.com/focal/112/112/50/50/0*9lmsC_9D18Y4ZaPS.png)](/@blockapex/cryptocurrency-
cutting-edge-or-criminal-8362138ea758?source=read_next_recirc---------2
---------------------7aa7e84a_e096_4f71_975e_0e8dca0a2f4c-------)

[[![Khe Han
Chu](https://miro.medium.com/fit/c/40/40/1*c6wVNGqAexDlfhsGvuh4SA.jpeg)](/@khehanchu?source=read_next_recirc
---------3---------------------7aa7e84a_e096_4f71_975e_0e8dca0a2f4c-------)

[Khe Han Chu

](/@khehanchu?source=read_next_recirc---------3---------------------
7aa7e84a_e096_4f71_975e_0e8dca0a2f4c-------)

in

[CryptoStars

](https://medium.com/cryptostars?source=read_next_recirc---------3
---------------------7aa7e84a_e096_4f71_975e_0e8dca0a2f4c-------)

## Blockchain 101 for Blockheads — the Usefulness and Uses of Blockchain

![](https://miro.medium.com/focal/112/112/50/50/1*pLtCvGw3qyBSd1RPpGfLaw.jpeg)](/cryptostars/blockchain-101-for-
blockheads-the-usefulness-and-uses-of-
blockchain-22b3b4494aeb?source=read_next_recirc---------3---------------------
7aa7e84a_e096_4f71_975e_0e8dca0a2f4c-------)

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

