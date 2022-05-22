[![](https://substackcdn.com/image/fetch/w_96,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F83c90dd4-d6b5-4f1a-87dc-810f4816f885_256x256.png)](https://alfablok.substack.com)

# [AlfaBlok](https://alfablok.substack.com)

SubscribeSign in

Share this post

Risk/Reward of liquidity provision in AMMs

alfablok.substack.com

Copy link

Twitter

Facebook

Email

# Risk/Reward of liquidity provision in AMMs

### Impact of price moves and liquidity changes in ROI compared to HODLing.

[![](https://substackcdn.com/image/fetch/w_90,h_90,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa7a5ff54-9882-49a7-abac-
ca2173498483_545x454.png)](https://substack.com/profile/8382123-alfablok)

|

[AlfaBlok](https://substack.com/profile/8382123-alfablok)

| Apr 5, 2020  
---  
  
[Share](javascript:void\(0\))  
  
### The basics of Automatic Market Makers

One of the hottest spaces in DeFi are AMMs, or automatic market makers.
[Uniswap ](https://uniswap.exchange/)has taken the DeFi space by storm, and
exciting projects such as [Balancer](https://balancer.finance/) are just being
announced, promising to introduce a lot of new opportunities in this space.

AMMs allow users to swap crypto assets, for example DAI for ETH, without
requiring a centralized counterparty. This is unlike traditional exchanges
such as Coinbase, Kraken, or Binance, which act as intermediaries between
token buyers and sellers. Whereas these companies are centralized, subject to
regulations, censorship and identity control, AMMs are simply smart-contract
systems operating unstoppably on top of distributed ledgers such as Ethereum.

One interesting element of AMMs, is that they require some users to act as the
liquidity providers in the service. Liquidity providers commit their own asset
pairs, to so called “liquidity pools”.

When using Uniswap and swaping ETH for DAI for example, you are trading your
assets against one of these liquidity pools.

### Fee structure in liquidity pools

AMMs charge a certain transaction fee to the users of the service. In the case
of Uniswap, it’s 0,3% of the value exchanged. This 0,3% is added to the
liquidity pool, and distributed to the users who committed funds to it,
proportionally to their contribution.

 **Example** :

Consider pool A:

  * 100 ETH + 10,000 DAI in it

  * 75% pool contributed by user A, and 25% to user B.

Users are able to swap assets against this pool. For example, **User Z**
trades 30 ETH for 3000 DAI with it. This generates a fee of 0,3% of the trade,
or 9 DAI . This fee is deducted from the transaction (user only gets 2991
DAI), and the 9 DAI are left in the liquidity pool. Since the pool is owned
75/25 between users A/B, this extra 9 DAI in the pool is split accordingly.

Had the pool been larger, with a third user committing funds to it, the fees
would have been further diluted. The point we’re trying to illustrate is that
the larger the pool, the lower the fees collected by individual contributors.

In short, the fees that liquidity providers end up recouping depend on two big
factors:

  1.  **Transaction volume**. 2X more transactions, generate 2X more fees for liquidity providers.

  2.  **Pool size**. 2X pool size, generate 1/2X fees for liquidity providers. Conversly, 1/2X pool size, generates 2X fees.

### Returns for liquidity providers vs Hodling

Anyone can decide to send funds into a liquidity pool, and therefore
participate from the fees generated. However, adding funds to a pool isn’t
guaranteed to be a winning strategy, compared to a simple buy and hold
strategy.

Let’s compare the returns of buy and hold, vs. a liquidity pool strategy:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F6fd27216-29dc-4533-bd8a-6e41b659b4ac_887x609.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F6fd27216-29dc-4533-bd8a-6e41b659b4ac_887x609.png)

 _Chart assumptions: ETH price = 100 DAI, Fees = 0,3%, Pool size = 30K ETH,
Monthly volume=200K ETH, position period = 1 year._

The strategy underperforms buy and hold if ETH loses more than ~80% of its
value, or if it grows more than ~120% of its value during this period.
Conversely, it outperforms it prices stay within these ranges.

Here is another way to visualize pools vs hodling:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ffb02eafb-
dd73-4e5b-9c14-6e0301654b30_874x624.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ffb02eafb-
dd73-4e5b-9c14-6e0301654b30_874x624.png)

This time, instead of looking at the position in $ terms in the Y axis, we
simply look at the pool position, divided the hodl position, to get a the
relative % difference between the two.

### Impact of changes in liquidity pool size

Let’s now assume we made the same contribution to a pool, with the same
transaction volume, but with twice the total liquidity in it:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F33947f5e-8fde-4c01-847c-c70b538f870b_877x631.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F33947f5e-8fde-4c01-847c-c70b538f870b_877x631.png)

As expected, the higher liquidity in the pool translates into lower fees, and
this brings the entire curve down. This means that the range in which the
strategy is profitable is narrower.

  *  **Original range:** -80% to +120%

  *  **2X liquidity pool range** : -60% to +80% 

It’s important to note that if liquidity increased 2X, and the transaction
volume also increased 2X, the two factors would cancel each other (2 x 1/2 =
1). What really impacts liquidity providers therefore, is how the transaction
volume moves _**with respect to**_ liquidity.

Taking this into account, let’s put it all together, and look at a fuller
spectrum of Pooling vs Hodling, for price variations vs Tx Volume/Liquidity
variations:

######

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F0acca040-7756-4c32-95e0-8699a27b1ee1_1101x458.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F0acca040-7756-4c32-95e0-8699a27b1ee1_1101x458.png)

 _% = Liquidity pool strategy premium over hodling._

 _Chart assumptions: ETH price = 100 DAI, Fees = 0,3%, Pool size = 30K ETH,
Monthly volume=200K ETH, position period = 1 year._

### Historical evolution of liquidity pool sizes and transaction volumes

From the previous analysis, it’s clear that not only do you need to have a
certain view about where the asset price is going, but also about how the pool
size and tx values are likely to evolve.

Luckily, uniswap provides information about pool and transaction volumes at
<https://uniswap.info/>.

#### Historical Liquidity for DAI-ETH pool

Let’s look at how liquidity (the size of pool), has evolved during the past
few months.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb1aff97f-02c2-42b2-b552-4294f861f00f_1173x506.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb1aff97f-02c2-42b2-b552-4294f861f00f_1173x506.png)

 _Information from uniswap.info as of April 7th 2020_

Liquidity stayed at around 16K ETH between december and mid February. It then
started increasing up to the current levels of about 32K ETH. It basically
doubled in about 3 months.

#### Historical transaction volumes for DAI-ETH

Let’s now look at the transaction volumes this pool saw, during the same
period. This is, how much eth was exchanged for DAI.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc9b9c95b-a192-4e09-a908-38eaa64cb9ae_1273x528.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc9b9c95b-a192-4e09-a908-38eaa64cb9ae_1273x528.png)

While the size of the pool doubled over approximately 3 months, transaction
volume aproximately doubled _**each month!**_ between November and February.
It then went on to explode in March (due to Black Thursday).

Here you can see the data combined:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fec3d9809-8d5e-4850-8778-3e5a5ae790e7_761x498.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fec3d9809-8d5e-4850-8778-3e5a5ae790e7_761x498.png)

This is heavily skewed due to the highly turbulent events during black-
Thursday in March.

For more clarity, here’s the chart of Tx Volume / Liquidity, normalized to
that ratio in November.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F558237bf-a9bf-419d-8ca8-5a789cb4a0b1_787x568.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F558237bf-a9bf-419d-8ca8-5a789cb4a0b1_787x568.png)

Between November and February the ratio went up 4,5X, before shooting up to
15X in March. April is currently on track to finish between 150K and 200K,
bringing it more in-line with February levels.

Still, from November to February you can see that the transaction volume
increased much more rapidly than liquidity. This means going “south” quite
dramatically in the heatmap we showed above = very good news for liquidity
providers.

Let’s look at this graphically. Here are the price and pool values between Jan
1st 2020 and April 1st 2020:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F66e97ee1-c70d-41f9-ac35-095824e2b2e9_459x176.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F66e97ee1-c70d-41f9-ac35-095824e2b2e9_459x176.png)

Let’s see how this move between January and April in the pooling return
premium heatmap:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F1afd3fe9-763c-478f-b69c-78426901b453_1657x705.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F1afd3fe9-763c-478f-b69c-78426901b453_1657x705.png)

 _ **% = return premium over HODLing.** Chart assumptions: ETH starting price
= 130 DAI, Fees = 0,3%, Starting pool size = 18,66K ETH, Starting monthly
volume=41K ETH, position period = 90 days._

ETH price was mostly flat during the period, but Tx/Liquidity went up 10X. The
result is pool providers outperformed HODLers by nearly 33% during the period.

The black-thursday event helps illustrate the defensive nature of this
strategy - as volatility went up, tx volume grew much much faster than
liquidity volume. This was to the benefit of liquidity providers, who saw the
losses in their positions hedged by the increase in fees.

We will have to keep monitoring this space, but up until now liquidity
provision has shown to be a lot less dynamic than the Tx volumes.

### Conclusions

We’ve seen that AMMs provide an opportunity to contribute your assets to
liquidity pools, and be rewarded for it.

We have seen that compared to simply holding these assets, pooling can either
outperform, or underperform Buy and hold, depending mainly on price evolution
and the ratio between Tx Volume and pool size.

Pooling can be expected to outperform in two types of scenarios:

  *  _ **Lateral or slightly deteriorating markets**_ :   
The maximum performance takes place when underlying asset moderately decreases
in price. If the price increases or decreases dramatically, the strategy
starts under-performing.

  * _**Increase in Tx Volume relative to Liquidity**_ :   
When transaction volume outpaces liquidity added to the pool, this increases
the fees received and helps the pooling strategy over perform. Conversely, if
liquidity in the pool increases faster than Tx volume, share of received fees
are is reduced, narrowing the range of pricing that keeps the strategy
positive.

Combined with the experience during Black-Thursday, the analysis suggests that
this is in the whole, a defensive strategy, that can heavily outperform in
times of turbulence, and provide an interesting hedge during mild price
decreases.

In the future, it will be interesting to see if solutions such as [gelato
finance](https://play.gelato.finance/), can allow automation of the entry/exit
into this type of strategy, acting as a stop/loss of sorts.

###  **Final thoughts**

Nassim Taleb is a strong defender of “convexity” when taking risk. This means
having upside, or optionality, on both sides of the risk spectrum. This
particular strategy, relative to hodling, is concave, penalizing you on sharp
moves on either direction. In his terminology, it is fragile.

Unless you have tooling that allows you to monitor changes in pool and pricing
conditions and act on changes quickly, buy and hold (protected with some puts
if possible!), is perhaps safer strategy to follow for most people.

If you are interested in the topic of risk management within DeFi space,
please subscribe to be notified about our upcoming article “Achieving a crypto
antifragile position with DeFi put options”.

**Subscribe**

In the meantime, [tell your friends](https://alfablok.substack.com/p/coming-
soon?utm_source=substack&utm_medium=email&utm_content=share&action=share)!

* * *

Much appreciation to teams in the @BalancerLabs and @UniswapExchange discords
providing feedback and inputs on draft versions of the article.  
Writing to help move forward the community. All comments/thoughts welcome!

[ShareShare](javascript:void\(0\))

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

