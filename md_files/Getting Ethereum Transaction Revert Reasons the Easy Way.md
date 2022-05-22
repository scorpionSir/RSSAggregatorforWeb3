[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/24203a4d1844&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Authereum](https://miro.medium.com/fit/c/64/64/1*w__iPpsW58dKOv7ZU4tD2A.png)](https://medium.com/authereum?source=post_page
-----24203a4d1844--------------------------------)

Published in

[Authereum

](https://medium.com/authereum?source=post_page-----
24203a4d1844--------------------------------)

[![Shane
Fontaine](https://miro.medium.com/fit/c/96/96/1*qogtRncAejZBMQWQkqhrsQ.png)](/@shanefontaine?source=post_page
-----24203a4d1844--------------------------------)

[Shane Fontaine](/@shanefontaine?source=post_page-----
24203a4d1844--------------------------------)

Follow

Apr 22, 2020

·

3 min read

# Getting Ethereum Transaction Revert Reasons the Easy Way

## Use the eth-revert-reason NPM package to easily derive the reason for an
Ethereum transaction failure

![](https://miro.medium.com/max/1400/1*slhGjYt6fRpo76ZuHes0FQ.png)

Failed Ethereum transactions sometimes include a reason for the transaction
reversion. Retrieving these reasons is harder than it should be, especially
given how useful these messages are. Inconsistencies between
[Geth](https://github.com/ethereum/go-ethereum/wiki/geth) and
[Parity](https://www.parity.io/ethereum/), [Infura](https://infura.io/) and
[Alchemy](https://alchemyapi.io/), and even
[ethers.js](https://github.com/ethers-io/ethers.js/) and
[web3.js](https://github.com/ethereum/web3.js/) add to this complexity.

Authereum’s newly open-sourced `[eth-revert-
reason](http://github.com/authereum/eth-revert-reason)` NPM package handles
all the work for you and gives you exactly what you want — a reason for the
failed transaction.

Use this as an NPM package or as a simple CLI command by installing it today!
The code below shows how easy this now is:

 **NPM**

    
    
     const txHash = '0xf212cc42d0eded75041225d71da6c3a8348bdb...'  
    await getRevertReason(txHash) // 'I accidentally killed it.'

 **CLI**

    
    
     > getRevertReason 0xf212cc42d0eded75041225d71da6c3a8348bdb...  
    I accidentally killed it.

# Under the hood

The happy-path scenario for retrieving the revert reason is a simple
`eth_call` with some parsing of the resulting string and a UTF-8 conversion.
Libraries like ethers.js help with the formatting of the input, but even
without a library it is relatively straight-forward.

The non-happy-path scenarios are where it gets more complicated.

## Changing Error Messages

A little-known fact in the Ethereum ecosystem is that error messages for
transactions may differ based on the context of the block they are called in.
Take [this Authereum
transaction](https://etherscan.io/tx/0x6ea1798a2d0d21db18d6e45ca00f230160b05f172f6022aa138a0b605831d740)
as an example:

![](https://miro.medium.com/max/1400/1*QbKKM5XNTD38riq_CTJEog.png)

Failed Authereum Transaction

You can see that it failed with the revert reason `BA: Insufficient gas (ETH)
for refund`. However, if you run `eth-revert-reason` on this transaction hash,
you will get the error “LKMTA: Auth key is invalid”. **This is because the
message you receive can change depending on the context of the block you are
calling from**. If you run `eth-revert-reason` and pass in that transaction
hash, you will get the expected error!

    
    
    const txHash = '0x6ea1798a2d0d21db18d6e45ca00f230160b05f172f...'  
    const network = 'mainnet'let blockNumber = 9892242  
    await getRevertReason(txHash, network, blockNumber)  
    // 'BA: Insufficient gas (ETH) for refund'blockNumber = 9919263  
    await getRevertReason(txHash, network, blockNumber)  
    // 'LKMTA: Auth key is invalid'

## Running an Archive Node

Everyone’s favorite subject — the beloved [archive
node](https://docs.ethhub.io/using-ethereum/running-an-ethereum-node/) —plays
a role in this conversation as well.

A non-archive node allows you to `call` a transaction from the context of a
specific block. However, if the block was mined more than 128 blocks ago, then
a non-archive node will throw, claiming that the node cannot access old
blocks.

An archive node allows you to make a call from a block that is older than 128
blocks and can result in more accurate revert messages, as seen in the example
above.

Figuring out what node you are using under-the-hood may be more difficult than
you would hope, and it involves making RPC calls and inferring the node type
based on the result. Hopefully this changes in the near future.

## Kovan and Parity Traces

Another annoyance is the distinction between Kovan and the other networks, as
Kovan is only accessible with the Parity client.

In order to retrieve the revert message on Kovan, your node must have Parity
traces enabled, which is not a feature of
[Infura](https://community.infura.io/t/is-it-possible-to-enable-parity-rpc-
method-trace-rawtransaction/1463/8) (at this time) and is not too common
either.

Slightly modified string parsing must be done in this case as well.

# Conclusion

Ethereum transaction revert reasons _were_ once hard to retrieve but no longer
are. Alchemy handles this well by offering Parity traces and archive nodes
coupled with their package, but other providers like Infura either don’t
provide this or layer on additional costs.

Please feel free to [contribute to the
project](https://github.com/authereum/eth-revert-reason) or ask any questions.

We hope this helps to advance and grow the entire Ethereum ecosystem!

 _If you want to share your thoughts or learn more, jump in our_[
_Telegram_](https://t.me/authereum) _and let us know what’s on your mind.
Follow us on_[ _Twitter_](https://twitter.com/authereum) _for all of the
latest news and updates from the Authereum team._

\--

\--

\--

## [More from Authereum](/authereum?source=post_page-----
24203a4d1844--------------------------------)

Log into Ethereum

[Read more from Authereum](/authereum?source=post_page-----
24203a4d1844--------------------------------)

## Recommended from Medium

[[![Mercury Protocol](https://miro.medium.com/fit/c/40/40/1*J2lmKHnb-
HadefWK7XMyJg@2x.jpeg)](/@MercuryProtocol?source=post_internal_links---------
0----------------------------)

[Mercury Protocol

](/@MercuryProtocol?source=post_internal_links---------
0----------------------------)

in

[mercuryprotocol

](https://medium.com/mercuryprotocol?source=post_internal_links---------
0----------------------------)

## How To: Deploy Smart Contracts Onto The Ethereum Blockchain

![](https://miro.medium.com/focal/112/112/50/50/1*_7sRwfwAhn-wZS3c-YA-
Yg.png)](/mercuryprotocol/dev-highlights-of-this-week-
cb33e58c745f?source=post_internal_links---------0----------------------------)

[[![Polkadotters | Kusama & Polkadot
validators](https://miro.medium.com/fit/c/40/40/1*-aZH58Ju-
njJhQK_ikkYEg.png)](/@polkadotters?source=post_internal_links---------
1----------------------------)

[Polkadotters | Kusama & Polkadot validators

](/@polkadotters?source=post_internal_links---------
1----------------------------)

## Polkadot governance news #1

![](https://miro.medium.com/focal/112/112/50/50/1*XutLlCuVMWNa4JSYSMTKzw.png)](/@polkadotters/polkadot-
governance-news-1-dce3a84c2d43?source=post_internal_links---------
1----------------------------)

[[![Crypto Asset
Rating](https://miro.medium.com/fit/c/40/40/1*ZRgtw1TVT1-pl79IkASxWw.png)](/@assetratingcrypto?source=post_internal_links
---------2----------------------------)

[Crypto Asset Rating

](/@assetratingcrypto?source=post_internal_links---------
2----------------------------)

## SEC signs a one year deal for $125K with Blockchain analytics firm
AnChain.AI

![](https://miro.medium.com/focal/112/112/50/50/1*n2IpzmRleuScZgBJfBoe-Q.jpeg)](/@assetratingcrypto/sec-
signs-a-one-year-deal-for-125k-with-blockchain-analytics-firm-anchain-
ai-107e08a45199?source=post_internal_links---------
2----------------------------)

[[![Joshua Peters](https://miro.medium.com/fit/c/40/40/1*HQVkDC1uYcNU8KIpV-
bAAQ.jpeg)](/@joshua.peters2998?source=post_internal_links---------
3----------------------------)

[Joshua Peters

](/@joshua.peters2998?source=post_internal_links---------
3----------------------------)

## CyberKongz VX | Metaverse Horizons

![](https://miro.medium.com/focal/112/112/50/50/1*DJWSpHSNPCppEi7mhkK04w.jpeg)](/@joshua.peters2998/cyberkongz-
vx-metaverse-horizons-2e51e84a6e54?source=post_internal_links---------
3----------------------------)

[[![Sky
Walker](https://miro.medium.com/fit/c/40/40/0*SnqXAdh8-1TvTxz1)](/@wisdomgodblessp?source=post_internal_links
---------4----------------------------)

[Sky Walker

](/@wisdomgodblessp?source=post_internal_links---------
4----------------------------)

## GET YOUR FREE 1088 TRON COINS HERE👇

](/@wisdomgodblessp/get-your-free-1088-tron-coins-
here-e6508c5c9e7a?source=post_internal_links---------
4----------------------------)

[[![Synthetix
Grants](https://miro.medium.com/fit/c/40/40/1*oOdPftCBe4ZtOIpd5xdmFA.png)](/@SynthetixGrants?source=post_internal_links
---------5----------------------------)

[Synthetix Grants

](/@SynthetixGrants?source=post_internal_links---------
5----------------------------)

## Buy SNX to Fix C-Ratio Dapp

](/@SynthetixGrants/buy-snx-to-fix-c-ratio-dapp-
bd8bd351205f?source=post_internal_links---------5----------------------------)

[[![Bitspawn
Protocol](https://miro.medium.com/fit/c/40/40/1*DmVqVZo5JDwYJwBB7qXoSA.png)](/@bitspawnprotocol?source=post_internal_links
---------6----------------------------)

[Bitspawn Protocol

](/@bitspawnprotocol?source=post_internal_links---------
6----------------------------)

## CSP DAO x Bitspawn AMA Re-Cap

![](https://miro.medium.com/focal/112/112/50/50/1*nr6Yp3N3moLNsx66Vy8ZVg.jpeg)](/@bitspawnprotocol/csp-
dao-x-bitspawn-ama-re-cap-baac2b6a1d59?source=post_internal_links---------
6----------------------------)

[[![Lumenswap](https://miro.medium.com/fit/c/40/40/1*fhtIn95cqWHB6FxfkAd1Ug.jpeg)](/@lumenswap?source=post_internal_links
---------7----------------------------)

[Lumenswap

](/@lumenswap?source=post_internal_links---------
7----------------------------)

in

[Lumenswap

](https://medium.com/lumenswap?source=post_internal_links---------
7----------------------------)

## Round 5 of the lottery is now live

![](https://miro.medium.com/focal/112/112/50/50/1*-eWk56b6rpPYO4hwZqEFKg.jpeg)](/lumenswap/round-5-of-
the-lottery-is-now-live-9aafe34394e2?source=post_internal_links---------
7----------------------------)

[](/?source=post_page-----24203a4d1844--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
24203a4d1844--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
24203a4d1844--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
24203a4d1844--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
24203a4d1844--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----24203a4d1844--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----24203a4d1844--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fauthereum%2Fgetting-
ethereum-transaction-revert-reasons-the-easy-way-24203a4d1844&source=post_page
--------------------------nav_reg-----------)

[![Shane
Fontaine](https://miro.medium.com/fit/c/176/176/1*qogtRncAejZBMQWQkqhrsQ.png)](/@shanefontaine)

[

## Shane Fontaine

](/@shanefontaine)

120 Followers

Ethereum Developer

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F79989d458c54&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fauthereum%2Fgetting-
ethereum-transaction-revert-reasons-the-easy-
way-24203a4d1844&newsletterV3=6ea34a538e1c&newsletterV3Id=79989d458c54&user=Shane+Fontaine&userId=6ea34a538e1c&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Rich
Charles](https://miro.medium.com/fit/c/40/40/1*dHG3TOQaTCowOpGCitf0xg.jpeg)](/@dizzybot12?source=read_next_recirc
---------0---------------------c25b3239_d66f_4343_b20f_f08243032daa-------)

[Rich Charles

](/@dizzybot12?source=read_next_recirc---------0---------------------
c25b3239_d66f_4343_b20f_f08243032daa-------)

## How is CUDOS Faring against the current situation?

![](https://miro.medium.com/focal/112/112/50/50/1*qie-B5oXWeiwkizEOow1Zw.jpeg)](/@dizzybot12/how-
is-cudos-faring-against-the-current-
situation-7b1844fe245a?source=read_next_recirc---------0---------------------
c25b3239_d66f_4343_b20f_f08243032daa-------)

[[![Jay, Esq 🦇🔊 |
meTokens](https://miro.medium.com/fit/c/40/40/1*RJJ7Z3ENp8wkV8lxLJ7Blw.jpeg)](/@jayfrankesq?source=read_next_recirc
---------1---------------------c25b3239_d66f_4343_b20f_f08243032daa-------)

[Jay, Esq 🦇🔊 | meTokens

](/@jayfrankesq?source=read_next_recirc---------1---------------------
c25b3239_d66f_4343_b20f_f08243032daa-------)

## OMG How Was ETHDenver!?

![](https://miro.medium.com/focal/112/112/50/50/1*g3whydQ5-GMI6QyS2_tRzQ.png)](/@jayfrankesq/omg-
how-was-ethdenver-f0e21b1c75ff?source=read_next_recirc---------1
---------------------c25b3239_d66f_4343_b20f_f08243032daa-------)

[[![Leyanikitova](https://miro.medium.com/fit/c/40/40/0*Y8E8ASYXfATIdzSl)](/@leyanikitova?source=read_next_recirc
---------2---------------------c25b3239_d66f_4343_b20f_f08243032daa-------)

[Leyanikitova

](/@leyanikitova?source=read_next_recirc---------2---------------------
c25b3239_d66f_4343_b20f_f08243032daa-------)

## Why OlympusDAO is not a Ponzi?

![](https://miro.medium.com/focal/112/112/50/50/1*LkDc-
Pl1ekLqrb2O0cHiJg.png)](/@leyanikitova/why-olympusdao-is-not-a-
ponzi-b3d65a4fc58f?source=read_next_recirc---------2---------------------
c25b3239_d66f_4343_b20f_f08243032daa-------)

[[![Switchboard](https://miro.medium.com/fit/c/40/40/1*F4DeqUObWEKQbU8eB5T0CQ.png)](/@switchboardxyz?source=read_next_recirc
---------3---------------------c25b3239_d66f_4343_b20f_f08243032daa-------)

[Switchboard

](/@switchboardxyz?source=read_next_recirc---------3---------------------
c25b3239_d66f_4343_b20f_f08243032daa-------)

## Dialed in with Switchboard: Vol. 1

![](https://miro.medium.com/focal/112/112/50/50/0*h_ZXAfHEVLbZUwTe)](/@switchboardxyz/dialed-
in-with-switchboard-vol-1-9ce348ba7998?source=read_next_recirc---------3
---------------------c25b3239_d66f_4343_b20f_f08243032daa-------)

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

