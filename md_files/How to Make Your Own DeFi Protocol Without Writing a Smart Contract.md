[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/a820a90d9124&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Authereum](https://miro.medium.com/fit/c/64/64/1*w__iPpsW58dKOv7ZU4tD2A.png)](https://medium.com/authereum?source=post_page
-----a820a90d9124--------------------------------)

Published in

[Authereum

](https://medium.com/authereum?source=post_page-----
a820a90d9124--------------------------------)

[![Chris
Whinfrey](https://miro.medium.com/fit/c/96/96/1*uRxZNSG6t9DyVQS-53TijQ@2x.png)](/@cwhinfrey?source=post_page
-----a820a90d9124--------------------------------)

[Chris Whinfrey](/@cwhinfrey?source=post_page-----
a820a90d9124--------------------------------)

Follow

May 1, 2020

·

5 min read

# How to Make Your Own DeFi Protocol Without Writing a Smart Contract

![](https://miro.medium.com/max/1400/1*069vhCkWEMF1RuEe2SRClA.png)

Decentralized finance, or “DeFi”, has grown to become the undeniably dominant
use case for Ethereum today. With funds locked in DeFi protocols exceeding $1
billion earlier this year, we are witnessing the start of an entirely new
financial system being built from the bottom up. New DeFi protocols seem to be
popping up every week. These protocols, often colloquially referred to as
“Money Legos”, can be combined and composed to create entirely new financial
products.

At Authereum, we’re making building with these protocols easier than ever
before. In this post we’ll explore how you can take advantage of Authereum’s
[batched transactions](/authereum/introducing-batched-transactions-with-
authereum-f82dac9b62e7) API to create your own protocol without writing a
single line of smart contract code.

# Batched Transactions

Regular Ethereum accounts, also known as Externally Owned Accounts (EOAs),
have an unfortunate limitation. Each transaction from an EOA can only directly
interact with a single address or contract. This frequently shows up in dapp
interactions with messages like “You must first unlock X before you Y”.

Contract based accounts like Authereum do not suffer from this limitation and
can batch transactions to multiple contracts for a smoother user experience.
The “approval” step can be completely abstracted away in the eyes of the user
and they can simply perform the action that they intended too. Dapps like
[Erasure Bay](https://erasurebay.org/) and
[1inch.exchange](https://1inch.exchange/) are already using batched
transactions to improve their user experiences.

But what if we take this a step further? We can abstract away entire protocols
to create something entirely new.

# Our Building Blocks

![](https://miro.medium.com/max/800/1*kOeu0uM3qP-p_VRwn05viQ.gif)

DeFi protocols can be built with other protocols

The number of DeFi protocols we can build with is growing every day but they
primarily fall into a few main categories:

  * Exchange — [Uniswap](https://uniswap.exchange/swap), [dYdX](https://dydx.exchange/), [Kyber Network](https://kyber.network/), [0x](https://0x.org/)
  * Lending/Borrowing — [Compound](https://compound.finance/), [dYdX](https://dydx.exchange/), [Aave](https://aave.com/)
  * Synthetic Assets — [Maker](https://makerdao.com/), [Synthetix](https://www.synthetix.io/), [FutureSwap](https://www.futureswap.com/)
  * Insurance — [Nexus Mutual](https://nexusmutual.io/), [Opyn](https://opyn.co/#/)

 **In this example, we’ll be building an ETH lending protocol using Maker and
Compound that gets a better return than Compound itself** (based on todays
lending rates).

# Our Lending App

![](https://miro.medium.com/max/1400/1*r4AnRSmk07SU5Oc09Fts7Q.png)

The underlying protocols can be abstracted away for a simple interface

Our example DeFi protocol, lets users lend their ETH to earn interest. We
could just lend ETH on Compound but the rates are abysmally low and hardly
worth the effort (currently < 0.01%). This app will take advantage of Maker’s
low stability fee (currently 0%) and Compound’s much higher DAI lending rate
(currently 4.31%). If you want to take at the full implementation you can find
it [here](https://github.com/authereum/lend-
demo/blob/master/src/components/LendPage/LendPage.tsx).

## Lending

To get users a return on their ETH we will:

  * Open a Vault and deposit ETH
  * Withdraw DAI from the Vault
  * Lend that DAI out on Compound

This will allow users to maintain full exposure to ETH while also earning
about ~2.15% interest. This is half of the DAI lending rate on Compound
because only half the value of the ETH collateral can be withdrawn from the
Vault in order to maintain a healthy collateralization ratio.

To do this we’ll batch 3 transactions:

  1.  **Open the Vault, deposit ETH, and withdraw DAI**  
Maker makes these steps easy to do with one transaction. The function we want
to interact with on the smart contract is:

    
    
    function openLockETHAndDraw(  
      address manager,  // A contract in the Maker system  
      address jug,      // A contract in the Maker system  
      address ethJoin,  // A contract in the Maker system  
      address daiJoin,  // A contract in the Maker system  
      bytes32 ilk,      // 🤔IDK, ask someone at Maker  
      uint256 wadD      // The amount of DAI to withdraw  
    )

Our first transaction will look something like this:

    
    
    const openVaultTransaction = {  
      to: makerProxy,            // The contract being called  
      data: openVaultData,       // Our calldata for the function above  
      value: ethLendAmount,      // The amount of ETH being lent  
      gasLimit: GAS_LIMIT        // The amount of gas to include  
    }

 **2\. Approve DAI to the cDAI contract  
** Compounds DAI lending contract is also an ERC20 called cDAI! You can
deposit DAI and receive cDAI that will earn interest. First, we must approve a
transfer of DAI to the cDAI contract. (No need to approve an unlimited amount
when using batched transactions.) To do this we call `approve` on the DAI
contract with the cDAI contract’s address as our `_spender` and the amount of
DAI withdrawn above as the `_value`.

    
    
    function approve(  
      address _spender,  // The cDAI contract address  
      uint256 _value.    // The DAI withdrawn from the vault  
    )

Our second transaction will then look like this:

    
    
    const approveDaiTransaction = {  
      to: daiAddress,         // The DAI contract address  
      data: approveDaiData,   // The calldata for `approve`  
      value: '0',             // No ETH needed  
      gasLimit: GAS_LIMIT     // The amount of gas to include  
    }

 **3\. Lend DAI on Compound  
** Now we call `mint` on the cDAI contract which will take our DAI that we
approved and mint cDAI. This is the cDAI contract's `mint` function:

    
    
    function mint(  
      uint256 mintAmount // The DAI withdrawn from the vault  
    )

Our third transaction will look like this:

    
    
    const mintCDaiTransaction = {  
      to: cDaiAddress,      // The cDAI contract address  
      data: mintCDaiData,   // The calldata for `mint`  
      value: '0',           // No ETH needed  
      gasLimit: GAS_LIMIT   // The amount of gas to include  
    }

 **🔮✨This is where the magic happens✨🧙‍♂️  
** We can now batch up our transactions and send them off the Ethereum network
to be executed as a single on-chain transaction.

    
    
    import Authereum from 'authereum'  
    const authereum = new Authereum('mainnet')  
    const provider = authereum.getProvider()// Send off our batched transaction!  
     **await provider.sendTransactionBatch([  
      openVaultTransaction,  
      approveDaiTransaction,  
      mintCDaiTransaction  
    ])**

And that’s it! We can now get a larger return on ETH than most of the major
lending protocols including Compound itself, dYdX, and Aave. You can find the
code for the full working demo [here](https://github.com/authereum/lend-
demo/blob/master/src/components/LendPage/LendPage.tsx) and and run it
yourself.

# Conclusion

Contract based accounts make it easy to mix and match DeFi protocols to make
something entirely new. The number of protocols is constantly growing and the
possibilities for combining them are exploding. What will you come up with?

 _You can find more information about Authereum and our batched transactions
API in our_[ _docs_](https://docs.authereum.com/web3-provider#send-
transaction-batch) _. Have some questions or want to chat about your idea?
Jump in our_[ _Telegram_](https://t.me/authereum) _and shoot us a message.
Lastly, follow_[ _Authereum_](https://twitter.com/authereum) _on Twitter for
all of our latest news and updates._

\--

2

\--

\--

2

## [More from Authereum](/authereum?source=post_page-----
a820a90d9124--------------------------------)

Log into Ethereum

[Read more from Authereum](/authereum?source=post_page-----
a820a90d9124--------------------------------)

## Recommended from Medium

[[![MetaGrail](https://miro.medium.com/fit/c/40/40/1*ZOqHt5srFQTm8Tdos-
ydxA@2x.jpeg)](/@MetaGrail?source=post_internal_links---------
0----------------------------)

[MetaGrail

](/@MetaGrail?source=post_internal_links---------
0----------------------------)

## From DeFi to SocialFi: How decentralized technologies are distributing
power

![](https://miro.medium.com/focal/112/112/50/50/1*Pj0ij0gAlv9tRHA7ePZkHA.png)](/@MetaGrail/from-
defi-to-socialfi-how-decentralized-technologies-are-distributing-
power-104a6ea33368?source=post_internal_links---------
0----------------------------)

[[![Lumen](https://miro.medium.com/fit/c/40/40/0*DctxJsBSWw696z6M)](/@lumenmoney?source=post_internal_links
---------1----------------------------)

[Lumen

](/@lumenmoney?source=post_internal_links---------
1----------------------------)

## Lumen

](/@lumenmoney/lumen-6fd7f6a1caa4?source=post_internal_links---------
1----------------------------)

[[![Solensson](https://miro.medium.com/fit/c/40/40/1*ApHP8I7dPoSsIBAbpooxvg.png)](/@deepcrypto?source=post_internal_links
---------2----------------------------)

[Solensson

](/@deepcrypto?source=post_internal_links---------
2----------------------------)

in

[Darma Cash (DMCH) Project

](https://medium.com/darma-cash-dmch-project?source=post_internal_links
---------2----------------------------)

## Darma Cash (DMCH) anonymous public chain technology(9): Block-DAG (Update)

![](https://miro.medium.com/focal/112/112/50/50/0*gLEtDjcSRMk4Zw9V)](/darma-
cash-dmch-project/darma-cash-dmch-anonymous-public-chain-technology-9-block-
dag-update-874fc3d7e518?source=post_internal_links---------
2----------------------------)

[[![Netvrk](https://miro.medium.com/fit/c/40/40/1*7WMnj0Nnpa4FL4_zzP7thw.png)](/@netvrk?source=post_internal_links
---------3----------------------------)

[Netvrk

](/@netvrk?source=post_internal_links---------3----------------------------)

## Netvrk Partners with Metawars

![](https://miro.medium.com/focal/112/112/50/50/1*9ZPqk9oeXfPkFtJjqIU6kA.jpeg)](/@netvrk/netvrk-
partners-with-metawars-f3322c726ebe?source=post_internal_links---------
3----------------------------)

[[![spare7](https://miro.medium.com/fit/c/40/40/1*0i61ZkFs1INS5MFQuobhKQ.jpeg)](/@estee2277?source=post_internal_links
---------4----------------------------)

[spare7

](/@estee2277?source=post_internal_links---------
4----------------------------)

## Overview about Ideaology

![](https://miro.medium.com/focal/112/112/50/50/1*xcAXTJ5V-MwIdHUsQhWjtg.jpeg)](/@estee2277/overview-
about-ideaology-a848971c8a54?source=post_internal_links---------
4----------------------------)

[[![NKN](https://miro.medium.com/fit/c/40/40/0*ShvXaX4QUWRaULHU.jpg)](/@NKN_ORG?source=post_internal_links
---------5----------------------------)

[NKN

](/@NKN_ORG?source=post_internal_links---------5----------------------------)

in

[#NKN

](https://medium.com/nknetwork?source=post_internal_links---------
5----------------------------)

## NKN Monthly Report, May 2018

![](https://miro.medium.com/focal/112/112/50/50/1*7t1BG1QUsYTWk40yyY82TA.png)](/nknetwork/nkn-
monthly-report-may-2018-c4bffac5830f?source=post_internal_links---------
5----------------------------)

[[![BitCherry
Official](https://miro.medium.com/fit/c/40/40/1*ILeykjen_zz3Yw551rNOcg.png)](/@bitcherryofficial?source=post_internal_links
---------6----------------------------)

[BitCherry Official

](/@bitcherryofficial?source=post_internal_links---------
6----------------------------)

in

[BitCherryGlobal

](https://medium.com/bitcherryglobal?source=post_internal_links---------
6----------------------------)

## BitCherry Developer Ambassador Recruitment Program

![](https://miro.medium.com/focal/112/112/50/50/1*UmCXwlARnkhYNB_X4H1P5g.png)](/bitcherryglobal/bitcherry-
developer-ambassador-recruitment-
program-2741da74fdd8?source=post_internal_links---------
6----------------------------)

[[![William
McKenzie](https://miro.medium.com/fit/c/40/40/1*gM05dcBye5YcTCxU7XdCIw.jpeg)](/@williammckenzie1997?source=post_internal_links
---------7----------------------------)

[William McKenzie

](/@williammckenzie1997?source=post_internal_links---------
7----------------------------)

in

[Tezos Commons

](https://medium.com/tezoscommons?source=post_internal_links---------
7----------------------------)

## Enter Jakarta — Why it’s Significant

![](https://miro.medium.com/focal/112/112/50/50/1*-rOSKFIrtict5NOGFb8mtQ.png)](/tezoscommons/enter-
jakarta-why-its-significant-a79d15d4b8ce?source=post_internal_links---------
7----------------------------)

[](/?source=post_page-----a820a90d9124--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
a820a90d9124--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
a820a90d9124--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
a820a90d9124--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
a820a90d9124--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----a820a90d9124--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----a820a90d9124--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fauthereum%2Fhow-
to-make-your-own-defi-protocol-without-writing-a-smart-
contract-a820a90d9124&source=post_page--------------------------
nav_reg-----------)

[![Chris
Whinfrey](https://miro.medium.com/fit/c/176/176/1*uRxZNSG6t9DyVQS-53TijQ@2x.png)](/@cwhinfrey)

[

## Chris Whinfrey

](/@cwhinfrey)

719 Followers

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fa1bcf3cfe05c&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fauthereum%2Fhow-
to-make-your-own-defi-protocol-without-writing-a-smart-
contract-a820a90d9124&newsletterV3=acd535aa0a46&newsletterV3Id=a1bcf3cfe05c&user=Chris+Whinfrey&userId=acd535aa0a46&source=--------------------------subscribe_user-----------)

## More from Medium

[[![SW
DAO](https://miro.medium.com/fit/c/40/40/1*KyC1aauO3vTAUP6PeCbTGQ.png)](/@sw_dao?source=read_next_recirc
---------0---------------------1e1707b0_e537_48af_8d19_482d19a0cbe3-------)

[SW DAO

](/@sw_dao?source=read_next_recirc---------0---------------------
1e1707b0_e537_48af_8d19_482d19a0cbe3-------)

in

[SW DAO

](https://medium.com/sw-dao?source=read_next_recirc---------0
---------------------1e1707b0_e537_48af_8d19_482d19a0cbe3-------)

## Sun Wallet Development Begins

![](https://miro.medium.com/focal/112/112/50/50/1*LJJ6gxcmZ1CGq-
E_cwWrsA.png)](/sw-dao/sun-wallet-begins-
development-53b97bd5a766?source=read_next_recirc---------0
---------------------1e1707b0_e537_48af_8d19_482d19a0cbe3-------)

[[![EasyFi
Network](https://miro.medium.com/fit/c/40/40/1*336ANYj6KnlmpxRDPqviFw.jpeg)](/@easyfinetwork?source=read_next_recirc
---------1---------------------1e1707b0_e537_48af_8d19_482d19a0cbe3-------)

[EasyFi Network

](/@easyfinetwork?source=read_next_recirc---------1---------------------
1e1707b0_e537_48af_8d19_482d19a0cbe3-------)

in

[EasyFi Network

](https://medium.com/easify-network?source=read_next_recirc---------1
---------------------1e1707b0_e537_48af_8d19_482d19a0cbe3-------)

## EasyFi Invites Developers to Multi-Million Fund & Grants Program

![](https://miro.medium.com/focal/112/112/50/50/1*NZN2beO1dCXBxi-
am8HzzA.png)](/easify-network/easyfi-invites-developers-to-multi-million-fund-
grants-program-5b104f0d0ef3?source=read_next_recirc---------1
---------------------1e1707b0_e537_48af_8d19_482d19a0cbe3-------)

[[![Just.Z](https://miro.medium.com/fit/c/40/40/1*njinYezIPemGjERp7xYYqg.jpeg)](/@just-z?source=read_next_recirc
---------2---------------------1e1707b0_e537_48af_8d19_482d19a0cbe3-------)

[Just.Z

](/@just-z?source=read_next_recirc---------2---------------------
1e1707b0_e537_48af_8d19_482d19a0cbe3-------)

in

[Harvest Finance

](https://medium.com/harvest-finance?source=read_next_recirc---------2
---------------------1e1707b0_e537_48af_8d19_482d19a0cbe3-------)

## Recap: Week 66

![](https://miro.medium.com/focal/112/112/50/50/1*fCnsruY1IJEjGOFH_MQixQ.png)](/harvest-
finance/recap-week-66-32cf2f956293?source=read_next_recirc---------2
---------------------1e1707b0_e537_48af_8d19_482d19a0cbe3-------)

[[![Keystone](https://miro.medium.com/fit/c/40/40/0*n-xaVYgs0Ykfpt0U.jpg)](/@keystonewallet?source=read_next_recirc
---------3---------------------1e1707b0_e537_48af_8d19_482d19a0cbe3-------)

[Keystone

](/@keystonewallet?source=read_next_recirc---------3---------------------
1e1707b0_e537_48af_8d19_482d19a0cbe3-------)

in

[Keystone

](https://medium.com/keystone-wallet?source=read_next_recirc---------3
---------------------1e1707b0_e537_48af_8d19_482d19a0cbe3-------)

## Sushi & Keystone Partnership: Secure DeFi signing on multiple blockchains

![](https://miro.medium.com/focal/112/112/50/50/0*Fu_K9JagOE1nrMwJ)](/keystone-
wallet/sushi-keystone-partnership-secure-defi-signing-on-multiple-
blockchains-349384c1c978?source=read_next_recirc---------3
---------------------1e1707b0_e537_48af_8d19_482d19a0cbe3-------)

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

