[ ![The Integral](https://integral.dydx.exchange/content/images/2020/04/dydx-
logo-white-1.svg) ](https://integral.dydx.exchange)

  * [ ![The Integral](https://integral.dydx.exchange/content/images/2020/04/dydx-logo-white-1.svg) ](https://integral.dydx.exchange)
  * ### Categories

[

###

Open Finance ](/tag/open-finance/)

[

###

Derivatives ](/tag/derivatives/)

[

###

Macroeconomics ](/tag/macroeconomics/)

[

###

dYdX Announcements ](/tag/dydx-announcements/)

[

###

Educational ](/tag/educational/)

[Trade](https://trade.dydx.exchange)

# Understanding Perpetual Market Funding

[Derivatives](https://integral.dydx.exchange/tag/derivatives/) • Jun 2, 2020

[
](https://www.linkedin.com/shareArticle?mini=true&url=https://integral.dydx.exchange/understanding-
perpetual-market-funding/&title=Understanding%20Perpetual%20Market%20Funding)
[
](https://twitter.com/intent/tweet?text=Understanding%20Perpetual%20Market%20Funding&url=https://integral.dydx.exchange/understanding-
perpetual-market-funding/)

**At the heart of each perpetual market is the funding rate. The funding rate
helps keep the price of a perpetual close to its index price by incentivizing
traders to buy when the price is low relative to the index and to sell when
the price is high relative to the index.**  
  
 **Without a well-designed funding rate, the price of the perpetual may
deviate systematically from the index price, which may make the perpetual less
efficient and riskier to trade, and may disincentivize liquidity providers.**  
  
 **While funding rates across exchanges tend to share the same major
components, no two are the same. Differences in funding rate designs are
likely to affect price dynamics in ways that are subtle but nevertheless
significant.**  
  
 **Funding rates can also be used to generate crypto dollar yields by
investors who take the receiving side of the funding payments. The yield
offered by perpetual funding is often larger than that of most financial
products available in traditional finance.**

Funding rates play an important role in crypto markets today because of just
how much global trade volume is concentrated in perpetual products. As we
discussed in our recent article [comparing perpetual
exchanges](https://integral.dydx.exchange/comparing-perpetual-markets/),
perpetual markets have found very strong demand among crypto traders because
they offer a convenient way to hold leveraged positions without an expiry
date. Unlike futures contracts, perpetuals don’t need to be regularly rolled
over in order to maintain one’s exposure to a position.

The purpose of the funding rate is to encourage the price of a perpetual
contract to trade close to the price of the underlying, both over the long
term and the short term. A good funding rate makes it easier to predict and
understand the price of the perpetual, which is important for attracting both
traders and liquidity providers. Another way to frame the funding rate is as
the cost to hold either a long or short position, similar to how margin
exchanges charge interest on borrowed capital. A well-designed funding rate
allows the price activity of the perpetual to almost exactly mirror the
underlying spot market. The BitMEX BTC–USD contract provides a good example of
this, and of the success of the funding rate model that they pioneered.

![](https://integral.dydx.exchange/content/images/2020/06/Screen-
Shot-2020-06-02-at-5.08.29-PM.png)Source: TradingView

After BitMEX saw success with their perpetual contract, various crypto
exchanges rushed to launch their own perpetual products. The main ideas from
BitMEX’s original funding rate design remain unchanged in most perpetual
markets, still, no two perpetual markets use exactly the same design. We’ll
examine these differences in more detail below.

We will also discuss how perpetual market funding rates can be used as yield-
generating instruments. Within a given perpetual market, any position
collecting funding is subject to market risk. The key to using perpetual
funding as a source of yield is to hedge that risk out of the equation.

## How do funding rates work?

Funding rates work by putting a price on any deviations that occur in the
perpetual market price relative to a target price which is either equal to or
derived from the spot price of the underlying. When a perpetual consistently
trades above its target, it is assumed that longs are more in-demand, and so
traders holding long positions will make payments to traders with short
positions. On the other hand, when a perpetual market consistently trades
below its target, it is assumed that shorts are more in demand, and so shorts
will pay longs. The greater the deviation between the perpetual price and the
target price, the greater the magnitude of the funding rate.

When calculating funding payments, the funding rate is applied to the notional
size of a trader’s position. This means that traders with higher leverage will
pay more, relative to the collateral securing their position. Funding rates
can be applied at various points in a position’s lifecycle, but most perpetual
markets either charge funding once every eight hours, once every hour, or
continuously.

Two important concepts in the funding rate calculation are the index price and
the mark price. The index price is an average of spot prices from various
exchanges and the mark price is derived from the index price, sometimes
including a decaying basis rate that accounts for the amount of time until the
next funding payment. The mark price is the primary reference price used
throughout the calculation of the funding rate.

Within the funding rate calculation itself, there are typically two main
components: an interest rate component and a premium component. The interest
rate component is usually a constant, which may depend on the particular
assets underlying the perpetual. In the case of the dYdX and BitMEX perpetual
markets, the interest rate component is fixed at 0.01% per eight hours.
Meanwhile, the premium component quantifies how far the perpetual market is
trading from the mark price. It is often calculated as the distance between
the mark price and the impact bid and ask prices, which are defined as the
prices necessary to clear the bid and ask sides of the orderbook,
respectively, by a predefined amount. The smaller the distance, the lesser the
premium component. As an example, BitMEX uses the following formula:

    
    
    Premium Index (P) = (Max(0, Impact Bid Price - Mark Price) - Max(0, Mark Price - Impact Ask Price)) / Spot Price + Fair Basis used in Mark Price
    

Most funding rate designs apply a time-weighted average when calculating the
premium component. A time-weighted average is preferred as a sampling method
in order to make manipulation of the funding rate more difficult. The exact
timing of the sampling can be randomized as an additional precaution. The
funding rate is then calculated by summing the interest rate component and the
average premium component. The most popular perpetual markets will also apply
a clamp function, which requires the premium to be of a certain magnitude
before it will affect the funding rate. Other funding models do not use a
clamp, for example, the funding rate calculation for the dYdX BTC–USDC
perpetual market is simply the following:

    
    
    Funding Rate = One-Hour Premium + Interest Rate Component
    

## Funding Rate Design

 _Funding_ rates are not one-size-fits-all. All designs have tradeoffs and
exchanges have a big incentive to find a funding rate that users will trade
with the most. Given that BitMEX has been a pioneer and leader in perpetual
markets in terms of volume and open interest for some time, most funding rates
are based to some extent on BitMEX’s funding rate formula.

### Binance

Binance largely used BitMEX’s design, but with a few changes. Binance doesn’t
factor in a funding basis when calculating the premium component, which
essentially means that funding rates don’t rely on or have memory of previous
funding rates. Binance calculates its funding rate every second, which only
relies on the premium component that second.

### ByBit

ByBit also largely stuck with BitMex’s design, with one notable change. On
ByBit, funding is calculated every eight hours, but that funding rate isn’t
applied until the following funding period. It’s unclear exactly what this
accomplishes.

### FTX

FTX has one of the more unique funding rate designs in the space. Unlike most
exchanges where the premium component is scaled so as to be realized over an
eight-hour period, premiums on FTX are calculated every hour but scaled to
have a realization period of 24 hours. This means that a price differential of
a given size will result in relatively less funding. Similar to Binance, FTX
doesn’t factor in a funding basis when calculating the premium component.
Instead of using an impact price for the mark price, FTX uses a mark price
which is simply the median of last bid and last ask, which could introduce
more volatility into the funding rate, compared with other designs. Finally,
FTX doesn’t use an interest rate component, which means we may expect FTX
perpetual contracts to trade at a premium relative to other perpetuals with
positive interest rate components.

### Deribit

Like FTX, Deribit’s funding rate calculation is quite a bit different from
BitMEX. Deribit calculates and applies the finding rate in real-time, every
single millisecond. Deribit is the only perpetual market with a funding rate
that is applied and paid in real time as it is calculated. Deribit uses a 30
second exponential moving average price in its mark price calculations, which
places more weight on recent prices.

### Kraken

Like Deribit, Kraken applies funding payments continuously. There is an
important difference however, in that these payments are made using the
funding rate calculated from the previous four-hour period. Like most other
exchanges, the premium component on Kraken is scaled so as to have a
realization period of eight hours.

### dYdX

The dYdX perpetual market design differs from BitMEX’s in a few key ways.
Funding on dYdX’s perpetual market is calculated and applied every second,
with the funding rate itself updating every hour. By applying funding
continuously, we aim to keep the perpetual price as close to the index as
possible at all times, avoiding the “basis” which, in other designs,
accumulates over the time period leading up to the funding payment. This
design was a good fit for us given that we apply funding payments in a
decentralized manner via the dYdX Perpetual Protocol smart contracts. Like
BitMEX, we include an interest rate component fixed at 0.01% per eight hours,
and use a time-weighted impact price to calculate the premium.

## Funding Rates as Yield

As we discussed in our article on [crypto dollar
yields](https://integral.dydx.exchange/crypto-dollar-yields/), perpetual
contract funding can be a great source of dollar yield for investors and even
savers. Positions can be created in which there is no exposure to the
underlying price of the cryptocurrency, but the position is constantly earning
interest in the form of the funding rate. These are constructed by taking the
opposite side of the funding rate and then hedging that exposure through the
spot market.

Let’s walk through an example.

Assume that the price of a perpetual market has consistently traded above its
corresponding index price over an hour window. In this case, the funding rate
for that period will be positive, meaning longs will pay funding to shorts.

A trader who wants to collect the funding rate would open a short position on
the perpetual. For this example, let’s assume the price of the perpetual is
$10,005 BTC/USD and the index price is $10,000 BTC/USD. Once they enter a
short position at $10,005 BTC/USD through the perpetual, they are now exposed
to fluctuations in the price of BTC. If the price of BTC goes up, their
position will be much more underwater than the funding they’ve collected.

To hedge out of this market risk, the trader can create a position that is
“delta-neutral,” meaning changes in the underlying price don’t affect the
position’s PnL. In our example, the trader would offset their perpetual short
position by going long BTC on the spot market. That way, if the price of BTC
goes up or down, the position's dollar value remains the same, while
collecting the funding rate every settlement period.

The same trade can also be done in reverse. Let’s say the perpetual was
trading at $9,998 BTC/USD and the index price is $10,000 BTC/USD. In this case
the funding is negative and shorts pay longs. A trader would enter into a long
position through the perpetual and then short BTC on a margin exchange, or
even another perpetual market. The trader would have to take into account any
interest or funding payments made on account of the short position.

This type of trade is similar to a traditional “[cash and
carry](https://www.investopedia.com/terms/c/cashandcarry.asp).” Historically,
cash and carry trades on Bitcoin perpetual markets have yielded very high
annualized returns, frequently in the double digits. Since capital is needed
to go both long and short, leverage can be used to make the trade more
efficient. When leverage is applied, the position collects an amount of
funding proportional to the notional size of the trade, and not just the
amount of collateral. The downside of using leverage is that positions can be
liquidated, which can quickly wipe out any funding earned.

## Funding Rates on dYdX

Since its launch, the BTC–USDC perpetual on dYdX has seen a significantly
elevated funding rate compared with other stablecoin-denominated perpetual
markets. **In just 1 month after launching, longs have paid shorts a total of
13% in funding, equal to 156% in annualized earnings.**

![](https://integral.dydx.exchange/content/images/2020/06/history.png)

Why has our funding rate remained elevated?

Our first cohort of traders has been just slightly long biased. As we
discussed in this post, when the price of the perpetual is higher than the
price of the index over time, the funding rate will be high in order to
incentivize shorts to come and take the other side. Over time, it will be
interesting to see what type of trader gravitates to dYdX and how our funding
rate reacts to that market structure. In the meantime, we’re excited to see
more traders coming in to take the other side of the market!

 _Special thanks to dYdX Engineer[Ken Schiller](https://twitter.com/kenadia),
for his excellent research on the perpetual funding market._

* * *

 **[dYdX](https://trade.dydx.exchange?trk-origin=Integral)** is the most
powerful open trading platform for crypto assets with spot, margin, and
perpetual markets.

 **[Start trading on dYdX today](https://trade.dydx.exchange?trk-
origin=Integral)** and check out our new **[BTC-USDC Perpetual
Market](https://trade.dydx.exchange/perpetual/BTC-USDC?trk-origin=Integral)**!

You can reach dYdX via email at
[contact@dydx.exchange](mailto:contact@dydx.exchange), on
[Twitter](https://twitter.com/dydxprotocol), or on our [official
**Discord**](https://discord.gg/yah42Rb).

#### Subscribe to our newsletter

Get the latest posts delivered right to your inbox.

Your email address Subscribe

![Success!](https://integral.dydx.exchange/assets/images/success.png?v=c7f248bd02)

Now check your inbox and click the link to confirm your subscription.

Please enter a valid email address

Oops! There was an error sending the email, please try later.

[ ](https://integral.dydx.exchange/author/dydx/)

####  [dYdX Exchange](https://integral.dydx.exchange/author/dydx/)

dYdX is a decentralized exchange that supports spot, margin, and perpetuals
trading. The Integral is a blog covering Open Finance, Crypto Markets,
Bitcoin, Crypto Derivatives and dYdX Announcements.

No results for your search, please try with something else.

The Integral (C) 2022   •   Published with [Ghost](https://ghost.org)

[ ](https://t.me/joinchat/GBnMlBb9mQblQck2pThTgw) [
](https://www.linkedin.com/company/dydx/) [
](https://twitter.com/dydxprotocol)

[JavaScript license
information](https://integral.dydx.exchange/assets/html/javascript.html?v=c7f248bd02)

Great! You've successfully subscribed.

Great! Next, complete checkout for full access.

Welcome back! You've successfully signed in.

Success! Your account is fully activated, you now have access to all content.

