[![](https://substackcdn.com/image/fetch/w_96,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F83c90dd4-d6b5-4f1a-87dc-810f4816f885_256x256.png)](https://alfablok.substack.com)

# [AlfaBlok](https://alfablok.substack.com)

SubscribeSign in

Share this post

ETH hedging in DeFi: new back-test results

alfablok.substack.com

Copy link

Twitter

Facebook

Email

# ETH hedging in DeFi: new back-test results

### Perma hedging with put options priced with a Black-Scholes engine.

[![](https://substackcdn.com/image/fetch/w_90,h_90,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa7a5ff54-9882-49a7-abac-
ca2173498483_545x454.png)](https://substack.com/profile/8382123-alfablok)

|

[AlfaBlok](https://substack.com/profile/8382123-alfablok)

| Apr 29, 2020  
---  
  
[Comment](https://alfablok.substack.com/p/eth-hedging-in-defi-new-back-
test/comments)

[Share](javascript:void\(0\))  
  
### Introduction

Last week [we looked at](https://alfablok.substack.com/p/eth-hedging-back-
test-better-than) creating a permanent hedge position on ETH using [Hegic’s
](https://www.hegic.co/)beta version, with a very basic pricing engine. We saw
that with that engine, the systematic hedging system nearly always won.

This week, we look at a more sophisticated implementation of the hedging
system, with a Black Scholes dynamic approach to pricing.

Neither [Hegic ](https://www.hegic.co)nor [Opyn ](https://opyn.co/)can
guarantee these specific prices, but the results here can serve as a good
benchmark for what to expected. In this post we look at the results of this
updated strategy model, and compare it against simply holding.

### Pricing approach

The [Black-Scholes
price](https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model) engine isn’t
perfect, but many market participants use it to measure current market
conditions.

Here’s the basic idea: you submit some parameters (Current Price, Strike
Price, Volatility, and Time to Maturity), and the system works out a price.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F32457e22-d3f9-4f30-b307-b69ab8654591_1124x225.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F32457e22-d3f9-4f30-b307-b69ab8654591_1124x225.png)

It’s key to understand that options are traded in the market with open
pricing. Participants exchange at freely agreed prices, without obeying any
model.

For that reason, typically the model is used as follows:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Faefce135-0801-469f-9e52-c88daf8dfa74_1546x307.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Faefce135-0801-469f-9e52-c88daf8dfa74_1546x307.png)

People work out “implied volatility”, from option traded prices seen in the
market place.

### Volatility input to the model

DeFi Options on ETH only became available recently, so we don’t have
historical implied volatility, nor historical put-contract pricing.

We will try to use the next best thing. We’ll experiment with two approaches:

  1.  **Historical Volatility:** We will feed into Black-Scholes historical vol for the last cycle, and work out a price from it. Then we’ll add a 20% bias on top. This approach looks _BACK_ to get to volatility _._  

  2.  **Realized volatility:** We will feed the actual realized volatility for the coming cycle (since we can magically see the future during the back test). Then we’ll add a 20% bias on top. This approach looks _FORWARD_ to get to volatility _._

>  _Side Note: The first approach would be directly implementable in DeFi: An
> AMM (automatic market maker) could be created, that used the last periods’
> volatility to “make” a price. It should be studied, what the LP’s P &L look
> like, when supplying liquidity a Black-Scholes “uniswap”. _

The second approach, gives us a perhaps a more reliable representation of how
the strategy would have worked in real life pricing. Implied vol and realized
vol have shown to have a reasonably consistent bias in S&P VIX for example.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F78abbea8-9d45-4ea3-ab57-c969b1f18700_569x358.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F78abbea8-9d45-4ea3-ab57-c969b1f18700_569x358.png)

_Implied Volatility = Realized Volatility + “the Delta” in the graph_

This shows that implied vol on average behaves like realized vol + a certain
bias. We can replicate that, by looking at the actual realized vol, and then
adding an additional bias on top, to create conservatively “expensive” option,
to test the strategy with. The higher the volatility, the higher option
prices.

In the interest of length, in this post we’ll be looking at the results from
the second approach only. In our testing both models behaved reasonably
similarly. More info available in [A/B testing both volatility
models](https://alfablok.substack.com/p/volatility-matters).

 **In summary** : the results below use option pricing based on realized
volatility.

### Gas costs

Based on feedback on the previous back-test, we now account for Gas costs
associated with the deployment of the strategy. Here’s the basic approach:

  * We take a number of transactions per cycle as a parameter (2tx for example = 1 tx to buy put, 1tx to exercise option, for example)

  * We look at actual ETH fees per tx paid historically at each expiration/refresh time.

  * We multiply both by the ETH historical price at expiration/refresh time.

This feels very realistic. In our mind, this transaction probably could be
optimized to 1 or 2 tx per cycle, no more.

### Results

The system behaves as expected. It outperforms during down-turns, it under-
performs in market rallies.

Let’s look at one particular example, taking the period from Jan 2017 to Jan
2020:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F66e759fa-d7f7-48d8-960d-cde78a02ca4d_1949x1494.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F66e759fa-d7f7-48d8-960d-cde78a02ca4d_1949x1494.png)

This is a particular trading path starting on one particular date, and
finishing on a particular date too.

Now let’s look at 200 different entry exit paths within this same total
period, to see whether timing in and out mattered:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F99f6673c-9fdc-4e5c-ae63-a1a3f343ba5e_999x1031.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F99f6673c-9fdc-4e5c-ae63-a1a3f343ba5e_999x1031.png)

As you can see, the strategy is clearly time sensitive. Let’s look at four
different time periods and see the general results.

### General patterns

Here’s a high level summary of how the strategy behaved from 2017 to 2020.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F2e2c68f7-5ce6-4426-80b1-da0f157c2e4e_942x957.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F2e2c68f7-5ce6-4426-80b1-da0f157c2e4e_942x957.png)

Here’s a numerical summary of that same data:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe36df085-c164-407c-9524-7cd9bfd1deac_1445x556.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe36df085-c164-407c-9524-7cd9bfd1deac_1445x556.png)

This is obviously only one slice of the possible results, with a very specific
system parametrization (eg. 0,5 contracts per ETH hedged, 30 day refresh
cycle).

**Summary:** Generally speaking, we see this could be an interesting
instrument for people looking to have their savings insured, if they strongly
believe a down-turn is coming. More research needed with the strategy
parametrization.

### Observations on parameters

Here’s what we’ve seen playing with inputs.

  *  **Timing:** The start of the period is plays a big role. Starting with a highly volatile parabolic advance, makes the system underperform.

  *  **Hedging lever:** With higher contracts per ETH (1+), the system can have fatal total wipe-out losses, in extended periods of price increases.

  *  **Cycle length:** Having trialed from 7 to 90 days periods, over sufficiently long periods of time, the sampling doesn’t seem to affect results (very different from last time!!!).

  *  **Tx costs** : We played from 0 to 50 Tx per cycle, and our conclusion was that from 1Tx to 5Tx per cycle, normally price and vol are still a way more dominant factor.

### General take-aways

  * Hedging is great if you catch a downfall, or a black-swan. Very high gains of over 100% observed in those periods, even at cautious parameters. 300%+ returns possible.

  * Hedging can be risky as a permanent strategy. Even at cautious settings, losses of 65% observed in periods of price growth. It’s unclear whether a hedging makes sense as a perma-strategy. At some more aggressive hedging settings, strategy can wipe out-player.

  * More research needed on the strategy itself. Optimization opportunities, for example in using Kelly Criterion, and buying OTM puts instead of ATM, to improve performance.

  * Regardless of the ultimate strategy, we think these instruments will eventually be available. 

We’re very excited about the idea of being able to send ETH to a contract, and
have trustless certainty that a risk management strategy will be applied to it
unstoppably, permissionlessly. All of it built on top of other reliable DeFi
tech. Very interested in people’s ideas around this topic, and DMs open.

How would one go about building a project like this in the age of DeFi? How
would you finance it, govern it, risk/reward from it? That’s what we plan on
exploring in the coming posts. Subscribe to get notifications!  
  
Would love to hear people’s thoughts.

 **Subscribe**

 _Thank you to the Opyn and Hegic teams for their time reviewing early drafts
of this article, and particularly to Opyn for their extensive comments on
approaches to volatility pricing._

Share and help content spread!

[Share](https://alfablok.substack.com/p/eth-hedging-in-defi-new-back-
test?utm_source=substack&utm_medium=email&utm_content=share&action=share)

[CommentComment](https://alfablok.substack.com/p/eth-hedging-in-defi-new-back-
test/comments)

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
in?redirect=%2Fp%2Feth-hedging-in-defi-new-back-
test&for_pub=alfablok&change_user=false)

#### Check your email

For your security, we need to re-authenticate you.

Click the link we sent to , or [click here to sign
in](https://substack.com/sign-in?redirect=%2Fp%2Feth-hedging-in-defi-new-back-
test&for_pub=alfablok&with_password=true).

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

