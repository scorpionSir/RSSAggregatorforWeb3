[![](https://substackcdn.com/image/fetch/w_96,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F83c90dd4-d6b5-4f1a-87dc-810f4816f885_256x256.png)](https://alfablok.substack.com)

# [AlfaBlok](https://alfablok.substack.com)

SubscribeSign in

Share this post

ETH Hedging back-test. Better than hodling?

alfablok.substack.com

Copy link

Twitter

Facebook

Email

# ETH Hedging back-test. Better than hodling?

### A backtest analysis of ETH hedging using DeFi native puts.

[![](https://substackcdn.com/image/fetch/w_90,h_90,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa7a5ff54-9882-49a7-abac-
ca2173498483_545x454.png)](https://substack.com/profile/8382123-alfablok)

|

[AlfaBlok](https://substack.com/profile/8382123-alfablok)

| Apr 18, 2020  
---  
  
[Comment1](https://alfablok.substack.com/p/eth-hedging-back-test-better-
than/comments)

[Share](javascript:void\(0\))  
  
### What is hedging?

Hedging allows people to reduce the downside impact of an investment, by
betting _for and against its success_ simultaneously. Basic example: If I buy
Apple shares, I will gain if Apple price goes up, and lose if it goes down. If
instead of simply buying Apple shares, I buy Apple + put contracts on Apple,
then I will gain if Apple goes up (from the shares increasing in value), and I
will also gain if prices tank (from the put option contracts). This, share +
put on the share, is a hedged position, since you cover both upside and
downside.

The chart below illustrates such a hedge position, comparing ETH alone (blue),
vs ETH + put contracts on it (pink):

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F98c72a45-d683-47ba-b47d-9c4713bb1dbd_705x507.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F98c72a45-d683-47ba-b47d-9c4713bb1dbd_705x507.png)

This type of position is also called “convex” (V shape"). It is what professor
Nassim Taleb calls antifragile.

###

### DeFi Options now available

For the first time, you can now buy put contracts from DeFi protocols. These
are inmutable, trustless, decentralized smart contracts, ie. you don’t have to
rely on centralized, censorship liable entities, to get your puts. You are
simply interacting with Ethereum contracts, that will be operating in exactly
the same way, indefinitely, and permissionlessly.

You can buy such option contracts from protocols like [Hegic
](https://www.hegic.co/)and [Opyn](https://opyn.co/), both available and
running today on Ethereum contracts today.

###

### Back-testing ETH hedging

In this post, we’re going to be back-testing the performance of an ETH hedging
strategy, implemented with one of these DeFi protocols. We will be pretending
these puts were live from 2015, and we’ll be simulating the continuos hedging
of an investment in ETH for the entire period. We will use actual ETH pricing,
and actual option pricing from the protocol. At the end, we’ll compare how the
hedging strategy results fared vs more common “hodling” strategies.

For this first back-test, we have picked Hegic options, for its simplicity of
operation. We will be testing Opyn options in a future post.

### Exercise goals

We’re comparing the performance of two strategies:

  1. Make an investment and hold it indefinitely. (HODL)

  2. Make the same investment, and hedge it dynamically with Hegic puts. (HEDGE)

We want to see how strategy 2 performs compared to strategy 1.

### Current hegic costs

  * 2% per ETH protected per week.

  * 1% per contract settled if Intrinsic value collected at expiration.

Hegic allows three expiration periods

  * 1 week (2% cost)

  * 2 weeks (4% cost)

  * 4 weeks (8% cost)

### Procedure

 **For hodling**

  1. I buy 1 ETH

  2. I hold.

 **For hedging**

  1. I buy protection on 1 ETH. With left-overs after purchase, I buy ETH.

  2. At expiration: if contract has intrinsic value, I collect it, and buy ETH with all proceeds.

  3. Day after expiration: Open new put contracts for the new total amount of ETH held. I pay for it with my own ETH held.

  4. Repeat 2 and 3 at every expiration.

### Results

As it turns out, results depend a lot on the frequency of the hedging, and the
cost of the options.

Let’s look at same parameters comparing 7, 14, and 30 day option expirations,
at 2% cost (current Hegic cost).

#### 30 day hedge cycles. 2%

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F06776388-429f-43cb-a2b5-563921e3078f_1538x928.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F06776388-429f-43cb-a2b5-563921e3078f_1538x928.png)

#####  **Result: 6X overperformance vs Hodl.**

Please note that the Hodling green line is flat, because I always hold my
initial investment - 1 ETH. In hedging, I have less and less ETH if I buy
options that expire worthless, and I accumulate more ETH when options
accumulate with value, and I convert it into ETH.

#### 14 day hedge cycles. 2% weekly cost

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd4d640da-0e77-48f6-8619-961b923e8852_1538x928.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd4d640da-0e77-48f6-8619-961b923e8852_1538x928.png)

#####  **Result: 400X overperformance vs Hodl.**

Going from 4 weeks to 2 weeks, basically increases the amount of sampling of
ETH prices by the strategy, improving performance.

#### 7 day hedge cycles, 2% weekly cost

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F40fd658c-a95c-432f-acd5-53b1520039d6_1538x928.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F40fd658c-a95c-432f-acd5-53b1520039d6_1538x928.png)

#####  **Result** : 200,000X overperformance vs Hodl.

Looking at the 1 week hedging cycle test, it becomes clear that returns are
exponentially better than Hodling as I increase the hedging frequency.

If these results feel _too good to be true…_ we hear you. We felt the same
way! We spent tens of hours double-checking everything, even got a number of
third parties to run the numbers independently. In the end, consensus is that
our model is sound, and results robust. For those wanting the inner story,
there’s a more detailed explanation about why the return becomes
parabolic/geometric with shorter expiration times available to anyone
interested. To not make this post extremely long, we post it
[separately](https://alfablok.substack.com/p/back-testing-details-why-does-
the) [here](https://alfablok.substack.com/p/back-testing-details-why-does-
the).

But the conclusion is simple: this hedging system, with puts at 2% weekly
cost, becomes exponentially better than Hodling over time.

For fun, we tested the system with other pricing parameters. Let’s see how
system behaves at 4% weekly option cost:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F4dd6013c-11cf-40f3-a7e3-61e23a149eaf_1545x931.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F4dd6013c-11cf-40f3-a7e3-61e23a149eaf_1545x931.png)

As feared, while hedging premium is high at the low 2% weekly cost, just by
increasing it to 4%, hedging becomes a lot worse than hodling.

These results show the strategy isn’t a winning strategy per se, but rather,
that it depends heavily on the pricing of the options.

At any rate, at the current 2% weekly pricing, the backtests show this is a
winning strategy for option buyers - more on that later.

### Time dependence

These tests assumed starting the strategy in August 2015, and exiting in April
2020. Let’s now test how the strategy would have performed at several “random”
entry and exit dates within this period. We want to see if returns depended on
specific certain price evolution paths.

To reflect time dependence, we test out 200 different start-finish combination
dates, from full ETH price history.

The next table shows the results. Specifically, it shows hedging over-
performance for 4 week expiration cycles, exploring 200 different date
combinations from 2015 to 2020.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F5776f59c-ded9-4b5c-8a15-c8d16e5c8d20_1238x1033.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F5776f59c-ded9-4b5c-8a15-c8d16e5c8d20_1238x1033.png)

We see there’s a clear distinction before and after May-18. This coincides
with a time of sharp descents in ETH price, that lasted until December. The
fact we see so much green after the period, tells us that this strategy
particularly benefits of continued negative moves in price. The investment
periods in which ETH drops always significantly outperform. This makes sense,
that’s when puts display their protective power.

Conclusion is therefore, that this system is time sensitive, and that it
outperforms if big price drops take place, or underperforms otherwise.

### HEDGE vs HODL. General Results

Results below show statistical information about all results observed in 200
random date periods between Aug’15 and April’20.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fbacd0b9c-c1d2-432a-b87b-e1f56d545b9b_789x570.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fbacd0b9c-c1d2-432a-b87b-e1f56d545b9b_789x570.png)

So clearly, the strategy isn’t good in all environments. At 4% weekly cost,
the strategy is in fact significantly worse than hodling.

At current 2% pricing though, this is a no-brainer strategy really.
Unfortunately, we don’t think it’s going to be possible to execute it, as
we’ll explain below.

### Analysis

We implemented a simple put strategy on ETH with Hegic option, and we back-
tested it with real life ETH pricing.

We found that a person that used the system with 30 day expiration cycles,
starting in 2015, would have ended up 8 times ahead of Hodling to date. With
weekly expiration cycles, 200,000 times.

These figures suggests that current flat 2% Hegic pricing is… _very
attractive_ to option buyers. At a flat 2% pricing, the strategy is a winner.
The challenge is, it’s most likely a loser for liquidity providers in the pool
providing the options. And if it’s not a winning proposition for them… it’s
not clear how much additional liquidity will join this pool in the future.

None of this is news to Hegic founder and team by the way, who make it clear
that this was always intended as a Beta release to experiment, and who knew
the pricing might be too cheap. The team has in fact been working on a wider-
scale release planned for April, with much effort gone into the issue of
pricing. The key element in the new release: it includes implied volatility
when calculating prices, moving away from current flat pricing.

We’ll be sure to test their new model and take a similar back-testing approach
to the one you’ve seen here. To make sure you don’t miss it, please subscribe!

 **Subscribe**

### Conclusions

We wanted to test how ETH hedging worked in DeFi. In the end, what we found is
that there’s a slightly complex answer to that question. At least with Hegic’s
current protocol. We found that _it does work_ , the backtest shows
significant over performance relative to hodling…. but that it may be down to
the particular Hegic Pricing model… and that this pricing may not be available
in the market for long, if no liquidity providers fund the contracts. So the
conclusion is that it works, but that it probably you won’t be able to benefit
from it.

Encouraging, but not conclusive yet. We’ll have to wait for hedging back-tests
applied with Opyn options, which have a different pricing structure, and
obviously re-testing Hegic once they release their v1.

### Final thoughts

I am left with the question of whether a flat-pricing option protocol could
actually exist, and an optimum “% fee” be found.

The arrival of Uniswap and other AMMs show it is possible for systems to
produce a price without oracles. I wonder if an AMM could be built, were
option pricing was produced by an AMM, without oracles.

Finally, I am very interested in the idea that a protocol could be built that
implemented an unstoppable hedging strategy like the one described here,
automatically purchasing options on a position, in an unstoppable way on
Ethereum. If you are a builder, or think could contribute in any way, please
DM!

Special thank you to Hegic Founder
[@0mllwntrmt3](https://twitter.com/0mllwntrmt3), and the people hanging out in
the team’s discord for their time discussing the project. Really excited about
the upcoming release, and the new pricing engine. Important work for the
entire community!!!

**Subscribe**

We’re planning more posts on DeFi protocols, Liquidity Pools, strategy back-
tests, and token fundamental analysis over the coming weeks and months. Please
subscribe to keep posted!

In the mean time, you help us a lot when you share the newsletter. Thank
you!!!

[Share](https://alfablok.substack.com/p/eth-hedging-back-test-better-
than?utm_source=substack&utm_medium=email&utm_content=share&action=share)

[Comment1](https://alfablok.substack.com/p/eth-hedging-back-test-better-
than/comments)

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
in?redirect=%2Fp%2Feth-hedging-back-test-better-
than&for_pub=alfablok&change_user=false)

#### Check your email

For your security, we need to re-authenticate you.

Click the link we sent to , or [click here to sign
in](https://substack.com/sign-in?redirect=%2Fp%2Feth-hedging-back-test-better-
than&for_pub=alfablok&with_password=true).

[![](https://substackcdn.com/image/fetch/w_66,h_66,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F28789b5e-537d-444f-96c5-6f4f0be0c5ce_400x400.jpeg)](https://substack.com/profile/291811-josh-
johnson)

|

[Josh Johnson](javascript:void\(0\))

[Writes  The Entropy Report
](https://joshjohnson.substack.com?utm_source=substack&utm_medium=web&utm_content=comment_metadata)·[Apr
19, 2020](https://alfablok.substack.com/p/eth-hedging-back-test-better-
than/comment/170626)Liked by AlfaBlok

Would be interesting to see how this could be used within a TokenSet RoboSet.
Rather than exiting ETH to $ during a crossover event, hedge the ETH
automatically. Might also provide initial baseline level of demand for the
options and give retail exposure to this instrument.

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

