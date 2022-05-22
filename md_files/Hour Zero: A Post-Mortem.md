[](https://medium.com/)

[Get unlimited access](https://medium.com/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/b745f91f76c3&~feature=LoOpenInAppButton&~channel=ShowPostUnderUser&~stage=mobileNavBar)

[](https://medium.com/)

[Home](https://medium.com/)

[Notifications](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Primitive](https://miro.medium.com/fit/c/96/96/1*IJFmMdSn_ypT6FdYvG-f0g.png)](/?source=post_page
-----b745f91f76c3--------------------------------)

[Primitive](/?source=post_page-----
b745f91f76c3--------------------------------)

Follow

May 1, 2020

·

4 min read

# Hour Zero: A Post-Mortem

At 11:30 A.M. we announced our alpha release. Two hours later, we discovered a
bug.

# TL:DR

  * The bug prevents purchasing Primes from the Pool.
  * Current Prime holders are not at risk due to this bug. If you have Prime tokens, you can still freely exercise. We recommend you do so.
  * No funds are at risk due to this bug.
  * We paused the Pool, preventing new liquidity from being added.

# The Bug

![](https://miro.medium.com/max/1400/1*54WqTAwp8ut70yOLs_Ya7g.jpeg)

PrimePool.sol Alpha V0

Lines 235–241 are the area of focus here. In line 237, the premium is
calculated. If this premium is 0, the transaction will revert with the error:
“ERR_BAL_ETH” at line 241. We made the mistake of assuming the premium should
only return 0 if the `amount` is 0, which is the input parameter for the
amount of Primes to buy. However, `premium` is returning 0 due to the
volatility being calculated and returning 0.

# Timeline

  *  **1:41 P.M.:** Notified of an error being thrown when a user attempts to purchase Prime options from the pool.
  *  **2:05 P.M.:** Cycled the active liquidity in the Pool. This means we took all the tokens out of the Pool, and re-added liquidity. We had no issues with withdrawing every single token we originally deposited!
  *  **3:19 P.M.:** Identified and replicated the error in a test environment. Originally we thought the issue was a front-end one, but further investigation showed us the root cause, which was in the PrimePool contract.
  *  **3:26 P.M.:** Paused the pool. While no funds were at immediate risk due to this bug, we paused the pool to prevent new liquidity being added to the pool. This was so that we can deploy a new Pool contract without affecting any additional addresses beyond our own.

# Mistakes

We made the mistake of assuming the calculated premium in line 236 should not
return 0.

![](https://miro.medium.com/max/1234/1*CHn2mwV-KudPShZjeN4h8g.jpeg)

PrimePool.sol Alpha V0

In line 293, we make no extra checks to assure that the premium variable
(which is returned) is greater than 0. This is a mistake.

We removed the if conditional statement which would revert the transaction if
the premium is 0. You can see that if we submit a buy order with an `amount`
parameter that is not 0 (#1: in the event image below), we still get a 0
premium paid. We can see that in the buy event below, which we tested on the
forked mainnet.

![](https://miro.medium.com/max/1030/1*qPhdQ6SpGpwnvMlD-lCMng.jpeg)

1: Amount Parameter > 0, Premium: 0

Another mistake we made is that our testing suite did not have coverage of
this! In our tests, we make a lot of individual buy orders rather than
consecutive buy orders. This means that the bug was never being thrown,
because only one buy order was going into each new contract instance at a
time. We would have caught the bug if we submitted two buy orders back to
back.

# Next Steps

We suspect the 0 value being returned is due to the division in one of the
calculations. If the numerator is smaller than the denominator, it will return
0 because there are only integers in solidity land. There are three
calculations that go consecutively: calculate the pool’s utilization, use the
utilization in calculating the volatility proxy amount, set the global
volatility variable to the calculated amount, then calculate the premium. In
the premium calculation, the volatility is an input, and we multiply it. If
the volatility is 0, the premium is 0. The volatility is indeed returning 0 in
the case that Primes were bought from the pool one time. This makes all
consecutive buy orders have a 0 value calculated for their premium, which in
turn reverts the transaction.

## New Pool Contract

Over the next few hours, we will be pushing a fix that adds additional checks
to these values so that they will only be 0 in the correct situations. The
premium should be 0 if the amount sent into the contract is 0.

We will be redeploying only the Pool contract, which affects only Pool
liquidity providers. Primitive is the only liquidity provider that is
affected. We will still be able to withdraw our provided liquidity once the
user holding 200 Primes exercises their options.

## What do I do if I have Prime tokens?

Current Prime holders do not need to take any action. If you are holding Prime
tokens, you can freely exercise your right to purchase 200 DAI with 1 ETH.
This is because the Prime contract is completely separate from the pool
contract. Since they are separate, it makes it simple to redeploy the pool
contract with the fixed code.

# Learning and Onward

We’ve learned that our testing suite is not the catch-all assertion that the
contracts function in the intended ways. We failed to adequately check every
line of code. Going forward, we will be covering our math in the contracts
more diligently with its own test suite to validate the invariants.

\--

\--

\--

## [More from Primitive](/?source=post_page-----
b745f91f76c3--------------------------------)

Follow

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fef69815f4399&operation=register&redirect=https%3A%2F%2Fprimitivefinance.medium.com%2Fhour-
zero-a-post-
mortem-b745f91f76c3&newsletterV3=60c08806472a&newsletterV3Id=ef69815f4399&user=Primitive&userId=60c08806472a&source=-----b745f91f76c3
---------------------subscribe_user-----------)

Permissionless options protocol. Built on Ethereum.

Love podcasts or audiobooks? Learn on the go with our new app.

[Try
Knowable](https://knowable.fyi/?utm_source=medium&utm_medium=referral&utm_campaign=medium-
post-footer&source=post_page-----b745f91f76c3--------------------------------)

## Recommended from Medium

[[![OKC](https://miro.medium.com/fit/c/40/40/1*83OuqXEjl6wOAs7Qu8m_ow.jpeg)](https://okcofficial.medium.com/?source=post_internal_links
---------0----------------------------)

[OKC

](https://okcofficial.medium.com/?source=post_internal_links---------
0----------------------------)

## Elk.Finance and OKC AMA Recap

](https://okcofficial.medium.com/elk-finance-and-oec-ama-
recap-f672a4e38e7d?source=post_internal_links---------
0----------------------------)

[[![LimeChain](https://miro.medium.com/fit/c/40/40/1*-TUkgIHgb_7KYAWIII2ecw.jpeg)](https://medium.com/@limechainmarketing?source=post_internal_links
---------1----------------------------)

[LimeChain

](https://medium.com/@limechainmarketing?source=post_internal_links---------
1----------------------------)

in

[LimeChain

](https://medium.com/limechain?source=post_internal_links---------
1----------------------------)

## 3 Ways in which blockchain can help the COVID-19 crisis

![](https://miro.medium.com/focal/112/112/50/50/1*cOQ0oWWe9fDPePgjt5actA.jpeg)](https://medium.com/@limechainmarketing/3-ways-
in-which-blockchain-can-help-the-
covid-19-crisis-f9fdb775c5d8?source=post_internal_links---------
1----------------------------)

[[![Martin
Jee](https://miro.medium.com/fit/c/40/40/1*xwGIcfBG_dPzw3luf9iP6Q.jpeg)](https://martin-7591.medium.com/?source=post_internal_links
---------2----------------------------)

[Martin Jee

](https://martin-7591.medium.com/?source=post_internal_links---------
2----------------------------)

in

[Corda

](https://medium.com/corda?source=post_internal_links---------
2----------------------------)

## Could the future we want be built on Corda?

![](https://miro.medium.com/focal/112/112/50/50/1*tTY7vsPcKT3VQfP_IDBcYA.jpeg)](https://martin-7591.medium.com/could-
the-future-we-want-be-built-on-corda-89eccce4afa6?source=post_internal_links
---------2----------------------------)

[[![Oumaymabou](https://miro.medium.com/fit/c/40/40/0*w_C4aITbv9ksX8Yz)](https://oumaymabou257.medium.com/?source=post_internal_links
---------3----------------------------)

[Oumaymabou

](https://oumaymabou257.medium.com/?source=post_internal_links---------
3----------------------------)

in

[Coinmonks

](https://medium.com/coinmonks?source=post_internal_links---------
3----------------------------)

## What is a Blockchain?

![](https://miro.medium.com/freeze/focal/112/112/50/50/1*r45GDWbztqbpryOlc_leRg.gif)](https://oumaymabou257.medium.com/what-
is-a-blockchain-8a57d587ed?source=post_internal_links---------
3----------------------------)

[[![Sean Moss-Pultz](https://miro.medium.com/fit/c/40/40/0*rddI-
wl71O3Mq97g.jpg)](https://medium.com/@moskovich?source=post_internal_links
---------4----------------------------)

[Sean Moss-Pultz

](https://medium.com/@moskovich?source=post_internal_links---------
4----------------------------)

in

[moskovich

](https://medium.com/moskovich?source=post_internal_links---------
4----------------------------)

## Part 4: Understanding the Blockchain

![](https://miro.medium.com/focal/112/112/50/50/1*7jnD1rD1DkrPjnuvk7EpoA@2x.png)](https://medium.com/@moskovich/part-4-understanding-
the-blockchain-c7327c4417f0?source=post_internal_links---------
4----------------------------)

[[![Waves
Enterprise](https://miro.medium.com/fit/c/40/40/2*871LVLgHTHg2aYkq4hjToQ.png)](https://wavesenterprise.medium.com/?source=post_internal_links
---------5----------------------------)

[Waves Enterprise

](https://wavesenterprise.medium.com/?source=post_internal_links---------
5----------------------------)

in

[Waves Enterprise

](https://medium.com/waves-enterprise?source=post_internal_links---------
5----------------------------)

## Summing up the results of 2020

![](https://miro.medium.com/focal/112/112/50/50/0*cjxvIWpH7DltMt22)](https://wavesenterprise.medium.com/summing-
up-the-results-of-2020-c920a1fe90bc?source=post_internal_links---------
5----------------------------)

[[![CFLOW
NFT](https://miro.medium.com/fit/c/40/40/1*pM2TUFQHErl9XqGMBUtDjg.png)](https://cflow.medium.com/?source=post_internal_links
---------6----------------------------)

[CFLOW NFT

](https://cflow.medium.com/?source=post_internal_links---------
6----------------------------)

## ChainFlowers: Redefining the NFT Marketplace Ecosystem

![](https://miro.medium.com/focal/112/112/50/50/1*99-wArW1fIsrhfzlpREsKQ.png)](https://cflow.medium.com/chainflowers-
redefining-the-nft-marketplace-
ecosystem-d068ef7fa8f6?source=post_internal_links---------
6----------------------------)

[[![Franco
Zeoli](https://miro.medium.com/fit/c/40/40/1*jnn9cJmF0EHAxhB2vlT5JA.jpeg)](https://medium.com/@fzeoli?source=post_internal_links
---------7----------------------------)

[Franco Zeoli

](https://medium.com/@fzeoli?source=post_internal_links---------
7----------------------------)

in

[Nomic Foundation

](https://medium.com/nomic-foundation-blog?source=post_internal_links---------
7----------------------------)

## Nomic Labs DevX: Prioritizing projects

![](https://miro.medium.com/focal/112/112/50/50/1*f3EmlQSwTDbCZv5uRjZZIw.png)](https://medium.com/@fzeoli/nomic-
labs-devx-prioritizing-projects-9db6659cbed6?source=post_internal_links
---------7----------------------------)

[](https://medium.com/?source=post_page-----
b745f91f76c3--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
b745f91f76c3--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
b745f91f76c3--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
b745f91f76c3--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
b745f91f76c3--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----b745f91f76c3--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----b745f91f76c3--------------------------------)

[Get
started](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fprimitivefinance.medium.com%2Fhour-
zero-a-post-mortem-b745f91f76c3&source=post_page--------------------------
nav_reg-----------)

[![Primitive](https://miro.medium.com/fit/c/176/176/1*IJFmMdSn_ypT6FdYvG-f0g.png)](/)

[

## Primitive

](/)

135 Followers

Permissionless options protocol. Built on Ethereum.

Follow

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fef69815f4399&operation=register&redirect=https%3A%2F%2Fprimitivefinance.medium.com%2Fhour-
zero-a-post-
mortem-b745f91f76c3&newsletterV3=60c08806472a&newsletterV3Id=ef69815f4399&user=Primitive&userId=60c08806472a&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Canoe
Capital](https://miro.medium.com/fit/c/40/40/1*THw0ylIhWfng8iKJNHSsSg.jpeg)](https://canoecapital.medium.com/?source=read_next_recirc
---------0---------------------ed46b00f_c90e_4cc7_8d51_a9d472ee5863-------)

[Canoe Capital

](https://canoecapital.medium.com/?source=read_next_recirc---------0
---------------------ed46b00f_c90e_4cc7_8d51_a9d472ee5863-------)

## Partying with Platypuses

![](https://miro.medium.com/focal/112/112/50/50/0*O9BmbHec-
YsiLYBz.jpeg)](https://canoecapital.medium.com/partying-with-
platypuses-1f2002ff9616?source=read_next_recirc---------0---------------------
ed46b00f_c90e_4cc7_8d51_a9d472ee5863-------)

[[![CygnusDAO](https://miro.medium.com/fit/c/40/40/1*K-kxQEM3jHAXhVAZnZif0g.png)](https://cygnusdao.medium.com/?source=read_next_recirc
---------1---------------------ed46b00f_c90e_4cc7_8d51_a9d472ee5863-------)

[CygnusDAO

](https://cygnusdao.medium.com/?source=read_next_recirc---------1
---------------------ed46b00f_c90e_4cc7_8d51_a9d472ee5863-------)

## Cygnus — Access Liquidity Without Disrupting Your Investments

![](https://miro.medium.com/focal/112/112/50/50/1*7DOsXtHqVTxNRgfWq2j2RA.png)](https://cygnusdao.medium.com/cygnus-
access-liquidity-without-disrupting-your-
investments-1120856f7e0b?source=read_next_recirc---------1
---------------------ed46b00f_c90e_4cc7_8d51_a9d472ee5863-------)

[[![SecureDAO](https://miro.medium.com/fit/c/40/40/1*9CUFId1KHwOLm01D2BYTDg.png)](https://securedao.medium.com/?source=read_next_recirc
---------2---------------------ed46b00f_c90e_4cc7_8d51_a9d472ee5863-------)

[SecureDAO

](https://securedao.medium.com/?source=read_next_recirc---------2
---------------------ed46b00f_c90e_4cc7_8d51_a9d472ee5863-------)

## A Follow-Up and Explanation to SecureDAO’s Launch Process

![](https://miro.medium.com/freeze/focal/112/112/50/50/1*q7jvya0qfkAvAVAtU8SqBw.gif)](https://securedao.medium.com/a-follow-
up-and-explanation-to-securedaos-launch-
process-6d2415081f51?source=read_next_recirc---------2---------------------
ed46b00f_c90e_4cc7_8d51_a9d472ee5863-------)

[[![Bitbyte.Finance](https://miro.medium.com/fit/c/40/40/1*mSblbaHvuo_9rkpQx0Thqg.png)](https://bitbytefinance.medium.com/?source=read_next_recirc
---------3---------------------ed46b00f_c90e_4cc7_8d51_a9d472ee5863-------)

[Bitbyte.Finance

](https://bitbytefinance.medium.com/?source=read_next_recirc---------3
---------------------ed46b00f_c90e_4cc7_8d51_a9d472ee5863-------)

## What is an LP Token

![](https://miro.medium.com/focal/112/112/50/50/1*QO2MUDN5FOF0FdC_5QGQWQ.jpeg)](https://bitbytefinance.medium.com/what-
is-an-lp-token-153343b09d3f?source=read_next_recirc---------3
---------------------ed46b00f_c90e_4cc7_8d51_a9d472ee5863-------)

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

