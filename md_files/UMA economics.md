[![](https://substackcdn.com/image/fetch/w_96,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F83c90dd4-d6b5-4f1a-87dc-810f4816f885_256x256.png)](https://alfablok.substack.com)

# [AlfaBlok](https://alfablok.substack.com)

SubscribeSign in

Share this post

UMA economics

alfablok.substack.com

Copy link

Twitter

Facebook

Email

# UMA economics

### A look at how UMA generates benefits to users, sponsors, and $UMA holders

[![](https://substackcdn.com/image/fetch/w_90,h_90,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa7a5ff54-9882-49a7-abac-
ca2173498483_545x454.png)](https://substack.com/profile/8382123-alfablok)

|

[AlfaBlok](https://substack.com/profile/8382123-alfablok)

| May 20, 2020  
---  
  
[Comment1](https://alfablok.substack.com/p/uma-economics/comments)

[Share](javascript:void\(0\))  
  
In this post we take a look at:

  * Primer on UMA - what is it, how it works

  * Benefits to token holders, token sponsors, and $UMA holders

  * Discounted cash flow valuation of the protocol under various scenarios.

### What does UMA do?

UMA makes “minting and collateralizing” ERC20 tokens safe and easy.

  * It allows people to mint new ERC20 tokens with collateral behind them.

  * Collateral can be safely liquidated by token-holders.

  * Liquidation values can be linked to S&P 500 price, Gold Price, BTC hash rate, or any other “human verifiable” feed, thus creating “synthetic trackers”.

  * In case of collateral-liquidation disputes, UMA provides a decentralized Human Oracle platform (the DVM) to settle contracts.

###  **What is a synthetic token?**

For example, if Gold is trading at 1800 USD, and you get 1 gold synthetic
token, you should be able to liquidate at least 1800 USD worth of value from
collateral behind it. That’s the basic premise of a synthetic token.

To guarantee you will be able to exercise this right, synthetic token sponsors
(producers) must keep overcollateralized positions behind the tokens, and risk
losing all collateral if they don’t meet this over-coverage commitment.

Since collateral covering more than the entire price is behind these tokens,
they are traded in the market for the same value as if it was real gold.

####  **Example gold synth:**

In the specific case of Gold at 1800 USD, I could have a 2500 DAI locked in
the contract per every one gold ERC20 token in circulation. That being
verifiable on-chain, the Gold token could be traded at 1800 DAI price in the
market.

####  **Examples of possible synthetic tokens**

  * Gold ERC20, 

  * Oil ERC20, 

  * KWh_USD ERC20, 

  * Jamaica_gold_medals in the Olympics ERC20, 

  * Tesla Stock ERC20, 

  * Effective 12month Fed Interest rate ERC20, 

  * 10yr Treasury yield ERC20. 

There’s no limit to what you can imagine minting and collateralizing.

####  **Existing synths**

All Dai and Synthetix sTokens in circulation have one thing in common: They’re
all collateralized synths.

For the first time, UMA democratizes the ability for anyone to “mint and
collateralize” their own synths. And it allows synth sponsors to do “easily”,
without having to write all the collateral management logic from scratch and
using a trusted oracle and efficient price oracle system.

###  **Architecture**

You can think of it as two large components:

  *  **A customizable synth writer:** this can mint new ERC20s, locking in collateral. UMA calls this “token factory”.

  *  **A distributed human oracle system (DVM)**. The DVM orchestrates humans voting on price feeds, to enable collateral withdrawal from the minted ERC20s in case of disputes.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F642443c7-0e84-49f3-9a1f-a91700651295_827x854.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F642443c7-0e84-49f3-9a1f-a91700651295_827x854.png)

###  **Oracle system**

UMA uses clever game theory to minimize the number of times participants call
the Oracle, saving both fees and time. This is how it works:

  *  **Undisputed liquidations** : When collateral liquidations are done without issues, and both parties are happy with the pricing of collateral, no Oracle is required.

  *  **Disputed liquidations** : If the sponsor disagrees with liquidation, they’re able to freeze collateral release, and invoke UMA’s DVM oracle to vote on a price and settle the liquidation neutrally.

Both parties benefit from collateral being in escrow while the token is
circulating. Both parties benefit from UMA acting as an independent third
party in case of dispute

###  **Synth Example: Light Crude Oil**

Say you wanted Synthetix to have a synth with the price of Light Crude Oil, an
sLCO, and imagine that wasn’t available. You could now build your own:

  * You get UMA holders to approve adding an LCO price feed in the system.

  * You parameterize a token factory with collateralization rates, etc 

  * You stake your collateral, and then use UMA to mint erc20 tokens, with collateral redemption linked to LCO price feed.

  * You now have your own collateralized DeFi token ready to trade in the market. 

As a sponsor, you can pre-mint a batch of ERC20 collateralized tokens, and set
up as an LP on an AMM with your new token, and receive fees from users buying
it from the pool.

It’s key to appreciate that to launch such a token, you wouldn’t have to come
up with all the collateralization and oracling logic yourself; you could
simply parameterize a factory/minter, stake the collateral, and rely on UMA
contracts for the management of collateral during liquidation, settlement and
pricing.

 _(Today sponsors would also have to come up with “keepers” to monitor
inappropriate liquidations, although in the future there may exist generic
players doing this for all sponsors)._

###  **Benefits**

 **For token minters (sponsors):  **

  * Able to open new token markets with safe collateral custody.

  * Higher speed to market, by using ready-made UMA settlement logic

  * Higher customer trust, by using battle-tested UMA on-chain settlement and oracling logic

 **For token holders:**

  * Exposure to new risk markets (Oil, Gas, Electricity, Bets, Commodities, Indices, etc), backed by on-chain verifiable collateral

  * More trust. Safe settlement guarantees, based on battle-tested UMA settlement logic

  * 24/7 trading, high liquidity, fungibility, and all ERC20 general benefits.

 **For $UMA participants:**

  * Potential to be the underlying platform for a large chunk of all synthetic tokens minted and collateralized in DeFi world-wide.

  * UMA holders economically benefit from increasing amounts of collateral custodied in the platform

It is hard to imagine all that can be built on top of this new DeFi lego. No
limit to all things one could want to collateralize and trade on.

###  **Economics and opportunity**

The “synth” market in Fiat is over 500T in size. If all of this financial
engineering was ported to the ethereum distributed machine, the opportunity
would be gigantic. UMA could become _the_ platform in which millions of ERC20
tokens are collateralized.

What are the economics of this system?

####  **Two sources of earnings:**

  1. Token sponsors pay on-going fees when locking collateral in UMA tokens.

  2. Disputed liquidations carry fees for human price verification.

In other words, earnings produced by the protocol scale with the amount of
collateral stored in it, and the amount of human intervention required.

####  **Scenarios considered:**

The UMA team works under the central premise that low human intervention
should be necessary, for game-theoretical reasons.

On that basis, we concentrate on two key parameters to build outcome
scenarios:

  * Fee rate charged for locking collateral into synths

  * Total amount of collateral locked in

###  **RESULTS**

This is the matrix of the present value of earning flows for the protocol at
0% discount rate, for a range of scenarios produced by mixing:

  *  _ **Collateral ceiling:** the natural collateral maximum the protocol will achieve_

  *  _ **Year** : by what year is that maximum reached_

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F41c1a0db-3773-47e4-ae47-21fbf528dff1_1064x821.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F41c1a0db-3773-47e4-ae47-21fbf528dff1_1064x821.png)

 _0% Disc rate / 1% collateral fee / 1% dispute rate / 3% penalty fee_

The matrix shows valuation behavior across many scenarios at once.

For clarity, the 500B ceiling by 2030 cell, computes these earnings flows:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F27cd98b8-f19d-403c-b8a1-2e723939daaa_924x868.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F27cd98b8-f19d-403c-b8a1-2e723939daaa_924x868.png)

Notice how in the 0% discount scenario, present value is full value.

Same info graphically: 500B ceiling by 2030: This is how the model assumes
collateral growth & ceiling during the simulations.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F6e9039e1-a7a0-4eab-
bbd8-aa4b3b361c3f_651x512.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F6e9039e1-a7a0-4eab-
bbd8-aa4b3b361c3f_651x512.png)

 _@ 0% Disc Rate_

Our collateral growth model is exponential, and flat once the ceiling is
reached. We think it would make sense for adoption to be exponential as a
best-case scenario.

As you can see, earnings and collateral scale in tandem.

###  **HIGH RATES SCENARIOs**

Let’s now look at how the matrix looks, if we raise store fees to 5% and
dispute rates to 5%.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F41a4b42e-c7e0-4430-947c-aff239d70838_1066x836.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F41a4b42e-c7e0-4430-947c-aff239d70838_1066x836.png)

Results are about 6X better, but the break-even still happens at about 500M to
1T in collateral.

###  **50% DISCOUNT RATE**

Let’s look at both these scenarios, but now at 50% disc rate, to discount
uncertainty by 50% every year we travel into the future in each scenario.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F29775d8e-a43b-4ed8-af0f-b6163428f627_1063x804.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F29775d8e-a43b-4ed8-af0f-b6163428f627_1063x804.png)

Here’s an example of the same **500B by 2030 example** : **211M Valuation**

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fccdb8300-680b-4ade-9546-09880c90c71b_899x869.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fccdb8300-680b-4ade-9546-09880c90c71b_899x869.png)

Same scenario graphically:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F3e182599-218e-48ae-b252-3055eccbed5c_706x546.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F3e182599-218e-48ae-b252-3055eccbed5c_706x546.png)

 _@50% disc rate_

Notice how Earnings grow until 60M, two orders of magnitude less than at 0%
disc rate. After reaching the collateral ceiling, DR continues growing at 50%
but collateral is flat. Thus the “wave” shape of the present value of
earnings.

####  **HIGH DISCOUNT RATE & HIGH RATE**

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F2b20b705-be7d-45b7-9084-1284f9d00762_1067x817.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F2b20b705-be7d-45b7-9084-1284f9d00762_1067x817.png)

Same idea. Raising fees, disputes, or penalties, helps increase the earnings,
but break-even remains largely in the same magnitudes. With 50% Disc rate,
only more than 50%+ per year collateral growth survives valuations.

###  **Conclusions**

It is down to each person to make their own judgment as to what amount of
collateral may eventually be locked in UMA contracts, and how fast it will get
there.

What’s clear either way, is that for the protocol to justify valuations of
$100M+, the roadmap somehow should include a clear path towards
collateralizations in the range of tens of Billions or more.

This seems to be a theme for many DeFi protocols. In our previous analysis of
Maker, a similar conclusion was reached. Current market valuations suggest
investors are “implicitly pricing in” these protocols will reach billions+ in
collateral.

###  **Final thoughts**

In our opinion, the market will eventually “weigh” these protocols properly,
and find their price. More importantly perhaps, is to consider UMA as an
example of an emerging new class of business. The DeFi business. A new
category of economic engine, that creates transparent win-win scenarios for
its users, generates earnings and is governed by skin in the game DAOs.

We can learn much by looking at how these impressive teams build their
communities, make design choices, get financed, and operate in the real world
to bring to life these new types of economic engines.

It is fascinating to see this whole industry unfold and to think of all that
could be built in the coming decades.

Maximum respect and gratitude to Allison Lu for being available for comments,
and to the whole UMA team for the incredible protocol they’re building. It’s
an inspiration for the entire eco-system, and potentially a key building block
in a nascent industry that could become huge.

* * *

We write this for the benefit of everyone interested in learning about DeFi,
and because we think these are genuinely interesting topics and help the
community think in economic ways that we find exciting ourselves.

* * *

We don’t have any premium tiers - subscription is free for all! Subscribe now
to get new articles.

 **Subscribe**

You can also follow us on twitter at <https://twitter.com/CryptoEsp>

[Comment1](https://alfablok.substack.com/p/uma-economics/comments)

[ShareShare](javascript:void\(0\))

![](https://substackcdn.com/image/fetch/w_66,h_66,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Flogged-
out.png)

## Create your profile

Your nameYour bio Subscribe to the newsletter

0 subscriptions will be displayed on your profile (edit)

Skip for now

Save & Post Comment

## Only paid subscribers can comment on this post

[Already a paid subscriber? **Sign in**](https://substack.com/sign-
in?redirect=%2Fp%2Fuma-economics&for_pub=alfablok&change_user=false)

#### Check your email

For your security, we need to re-authenticate you.

Click the link we sent to , or [click here to sign
in](https://substack.com/sign-in?redirect=%2Fp%2Fuma-
economics&for_pub=alfablok&with_password=true).

[![](https://substackcdn.com/image/fetch/w_66,h_66,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F42d1a4b3-7589-4d49-92d3-d04b959a596b_807x1015.jpeg)](https://substack.com/profile/1286450-mr-
loop)

|

[Mr. Loop](javascript:void\(0\))

[Sep 9, 2020](https://alfablok.substack.com/p/uma-economics/comment/490471)

What does this say about UMA's current valuation at 1 Billion $? Extremely
overvalued ? :)

Expand full comment

[Reply](javascript:void\(0\))  
  
---|---  
  
TopNewCommunity[](javascript:void\(0\))

No posts

# Ready for more?

 **Subscribe**

© 2022 AlfaBlok

[Privacy](https://alfablok.substack.com/privacy) ∙ [Terms](/tos) ∙ [Collection
notice](https://substack.com/ccpa#personal-data-collected)

[ Publish on
Substack](https://substack.com/signup?utm_source=substack&utm_medium=web&utm_content=footer)[
Get the app](https://substack.com/app/app-store-redirect?utm_campaign=app-
marketing&utm_content=web-footer-button)

[Substack](https://substack.com) is the home for great writing

This site requires JavaScript to run correctly. Please [turn on
JavaScript](https://enable-javascript.com/) or unblock scripts

