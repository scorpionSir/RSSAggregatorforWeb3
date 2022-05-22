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

# Comparing Perpetual Markets

[Derivatives](https://integral.dydx.exchange/tag/derivatives/) • May 14, 2020

[
](https://www.linkedin.com/shareArticle?mini=true&url=https://integral.dydx.exchange/comparing-
perpetual-markets/&title=Comparing%20Perpetual%20Markets) [
](https://twitter.com/intent/tweet?text=Comparing%20Perpetual%20Markets&url=https://integral.dydx.exchange/comparing-
perpetual-markets/)

**Perpetual markets are far and away the most liquid avenues to access
cryptocurrency exposure. Ushered into the ecosystem by derivatives exchange
BitMEX, perpetual markets now facilitate billions in daily turnover across
exchanges all over the world, with a record $45 billion in volume transacted
on March 12th, 2020. Perpetual markets have outpaced spot markets for myriad
reasons, but the primary levers pulling in traders include high leverage,
margining in crypto instead of fiat, and no expiry (as opposed to dated
futures). As the cryptocurrency derivatives space has matured, a number of
different perpetual contracts have been launched that vary based on their
payout profiles, accepted forms of collateral, and liquidation mechanisms.**

Perpetual markets were first brought to the crypto space by BitMEX in
[2016](https://blog.bitmex.com/announcing-the-launch-of-the-perpetual-xbtusd-
leveraged-swap/). Their swap product helped alleviate the issues traders faced
when having to roll their futures positions. With standard quarterly futures,
traders that want to hold Bitcoin exposure indefinitely have to constantly
move their positions to further dated contracts, which forces them to incur
extra costs. BitMEX’s perpetual swap solved this problem by creating a Bitcoin
derivative contract that never expired.

### How do perpetual markets work?

The underlying mechanism that enables perpetual markets is the funding rate.
With perpetual markets, one side, either longs or shorts, pays the other side
over a specified time window. The amount paid is a reflection of both how much
leverage each side is employing as well as the delta between the index price
and the price of the perpetual contract.

Since perpetual markets attempt to emulate margin spot markets, the first
component of funding is an interest rate component accounting for the
difference in lending rates between the base and quote currencies. The other
component of the funding calculation is how far the perpetual market price is
from the desired index price. If the perpetual is below the index price,
shorts pay longs so that traders are enticed to go long and move the perpetual
price in line with the index. If the perpetual is above the index price, longs
pay shorts so that traders are enticed to go short and move the perpetual
price in line with the index.

Apart from maintaining orderly markets, perpetual funding can be used by
investors as interest yielding financial products. As we discussed in our
[piece on crypto dollar yields](https://integral.dydx.exchange/crypto-dollar-
yields/), BitMex’s perpetual swap paid out 8% in annual interest to shorts
over the course of 2019.

After BitMex saw success with its perpetual swap, many exchanges rushed to
bring their own perpetual products to market. ByBit was the first pure
derivatives exchange to launch their own perpetual, and shortly after their
market began trading, OKEx expanded their offering to include perpetuals. From
the start of 2019, a flood of new derivative exchanges and products came to
market including Deribit, Kraken’s Cryptofacilities, FTX, Binance, and Huobi.

Volume transacted on perpetual markets has far surpassed volume transacted on
spot and margin exchanges. Since the start of 2020, perpetual markets offered
on BitMex, Binance, and OKEx each averaged well over $1 billion USD in daily
volume, while spot books like Coinbase averaged roughly $100 million USD in
daily volume during the same period.

![](https://integral.dydx.exchange/content/images/2020/05/skew_btc_futures__aggregated_daily_volumes
--
2-.png)![](https://integral.dydx.exchange/content/images/2020/05/skew_btc_spot__aggregated_daily_volumes
--1-.png)

As mentioned above, the primary reasons perpetuals have become so dominant are
because they offer far more leverage than spot comparables and because they
can be margined in cryptocurrencies, eliminating the need to deal with the
traditional fiat system. With increased leverage, users can keep fewer assets
on exchange, which decreases the amount of counterparty risk their assets are
exposed to. Overall, perpetual markets, and cryptocurrency derivative
exchanges more broadly, are more efficient versions of their traditional
counterparts — virtually anyone in the world can use them, collateral can be
sent anywhere in the world in minutes, and all parts of the trading process
are handled automatically.

The growth of the perpetual market is only accelerating. New types of products
are coming to market at a rapid pace, offering users a variety of ways to get
exposure to cryptocurrencies and earn a yield on their assets. In this post,
we will look at the different types of perpetual markets available today, how
they’re structured, and what traders should know before using them.

### Non-Linear Inverse Perpetuals

One of the main tenets of cryptocurrency derivative markets is that they can
be accessed through the underlying cryptocurrency rather than fiat currency.
In the earlier days of the industry, this was paramount as derivative
exchanges found it hard to establish banking partnerships given the perceived
risk. Similarly, cryptocurrency derivative exchanges operate globally, without
a central clearing house. The exchange itself must act as the clearing house
and seize collateral when positions go into default.

Inverse perpetuals solved these problems by allowing traders to speculate on
the price of Bitcoin and hedge their holdings using Bitcoin as collateral
rather than fiat. Inverse futures are derivatives in which the price is quoted
in one currency, which in the case of most Bitcoin futures is the dollar, and
margined and settled in a base currency, which in the case of Bitcoin futures
is actual Bitcoin. A simpler way to understand this concept is to think
through how the contract is used. Speculators and hedgers trading inverse
futures are trading contracts that are priced in dollars, but are
collateralizing their positions in Bitcoin. The underlying contract is worth
$1USD/BTCUSD, but all of the PnL calculations are priced in BTC.

With cryptocurrency being used as the underlying collateral, exchanges can
easily seize assets if they need to liquidate sunk positions. Furthermore, the
fact that cryptocurrency is the only currency needed to trade inverse futures
means that virtually anybody in the world can access them.

A key feature of non-linear inverse perpetuals, and where their name stems
from, is the fact that their payout curve isn’t linear. This means that a 1%
movement in the contract price doesn’t equate to a 1% change in the PnL. The
reason for this is that the value of the collateral changes as the price of
the asset underlying the derivative changes. When the price goes lower, the
value of the collateral falls with it, meaning the position is less secure as
the price falls. On the opposite side, if the price goes higher, the value of
the collateral goes up as well, making the position more secure.

![](https://lh6.googleusercontent.com/WFeANx6Q10vHZ_wq7147RJRVibJ6B3wfuXosbU0ZE_M8dCG_bvZCiCjFMpWKWZ-7bIsxDhJMQWDYFyGUKbdROQeITCbyFU2wLVvZ0b-f_DduKKcYr-
Kt_l0AL_N3l-t5DkMzIovi)

This negative convexity is the reason that longs tend to get liquidated so
much more often than shorts. When prices move against long positions, the
value of their collateral decreases at the same time, meaning the position
becomes **increasingly** weak as the price falls. This is clearly evident in
the volume of long liquidations vs. short liquidations on BitMex’s inverse
perpetual.

![](https://integral.dydx.exchange/content/images/2020/05/skew_bitmex_xbtusd_liquidations.png)
_Figure: Liquidation volume on BitMEX since Sep 2018. Liquidation of long
positions (“Sell Liquidations”) are shown in red._

Today, a number of exchanges offer non-linear inverse perpetuals including
BitMex, Deribit, OKEx, ByBit, Kraken, and FTX. While most venues first
launched with Bitcoin products, a number of exchanges like Deribit and ByBit
added support for Ethereum inverse perpetuals shortly after, which have so far
seen modest success. From a liquidation mechanism standpoint, these venues
employ either auto liquidation or partial liquidation. In both cases, the
underlying crypto collateral is seized and sold on the market to ensure the
position doesn’t enter a state of default.

![](https://integral.dydx.exchange/content/images/2020/05/Frame-5-4.png)

### Vanilla Perpetuals

As their name implies, vanilla perpetuals are simpler contracts in which the
quote currency is used for margin and settlement. For most vanilla contracts
this is some type of stablecoin, usually USDC or Tether (USDT). With vanilla
perpetuals, the speculators, hedgers, and arbitrageurs trading them are
primarily concerned with their dollar holdings as their contracts and PnL are
all measured in dollars. These users aren’t concerned with the value of
Bitcoin and generally want to trade these contracts to earn more dollars.
Unlike inverse perpetuals, vanilla perpetuals have a linear payout curve, so a
1% change in the underlying results in a 1% move in the position’s PnL.

Interestingly, vanilla perpetuals retain the feature of allowing users to get
exposure to Bitcoin without touching the fiat system. Since they’re margined
in stablecoins, there’s no need to act with an intermediary in the traditional
world — collateral can be seized immediately and virtually any user has access
to these products.

Given the linear payout curve, vanilla perpetuals are used more for an
absolute dollar return than they are for hedging market exposure of an
underlying cryptocurrency, which means they are more frequently used by
speculators and arbitrageurs.

Many of the newer perpetual markets have opted towards the vanilla model, most
likely as a way to differentiate from the crowded inverse perpetuals space and
to attract new users who are less concerned with the long term market price of
cryptocurrencies and primarily want to trade volatility. Similarly, many of
the existing exchanges that offer inverse perpetuals have added support for
vanilla perpetuals to make sure they cover the full breadth of the market.
Today, the exchanges that offer perpetual markets structured as vanilla
perpetuals are Binance, ByBit, OKEx, FTX, and Huobi.

![](https://integral.dydx.exchange/content/images/2020/05/Table--2--2-.png)

### Decentralized Perpetuals

The market has resoundingly voiced its preference for perpetual markets as the
financial product of choice when it comes to getting liquid exposure to
cryptocurrencies. While today’s largest perpetual markets facilitate tens of
billions of dollars in trading volume daily, most of these exchanges expose
user assets to a large degree of counterparty risk. Similarly, the liquidation
processes that many of these exchanges employ are extremely opaque, opening up
questions as to whether or not positions are ever unduly liquidated.

To address these problems, a number of decentralized platforms, dYdX included,
have launched perpetual markets in which traders retain custody of their funds
at all times and enjoy a new level of transparency into the liquidation
process and operation of the insurance fund. Rather than custody funds in a
centralized exchange, funds are held in a non-custodial smart contract. At no
point in the position’s lifecycle do funds have to be exposed to a third
party. All liquidations are executed on the blockchain, allowing full
transparency into the amount of collateral that was liquidated, the price at
which the position went into default, and the price at which the position was
closed.

While the design space for these products is large, today’s decentralized
perpetual markets are all structured using stablecoins as the margin and
settlement currency. Given this, they exhibit linear payout curves where any
change in the underlying price is reflected in PnL on a one to one basis. In
terms of accepted forms of stablecoin collateral, today’s markets have focused
on USDC and Dai, primarily because they are already deeply integrated in defi
lending markets, decentralized spot exchanges, and automated market maker
platforms like Uniswap.

Smart contract-based derivatives markets make a lot of sense given the very
nature of what a derivative instrument is — you don’t need the underlying
asset to transact, you just need a reference to its value. Similarly, the fact
that decentralized finance components are so composable, it’s relatively easy
to create new financial markets. All an exchange really needs is a reliable
price feed to act as the system’s reference point, and the decentralized
finance ecosystem has robust oracle solutions including
[MakerDAO](https://developer.makerdao.com/feeds/) and
[Chainlink’s](https://chain.link/) price feeds. Alongside robust oracles,
decentralized finance is already home to a capital market system powered by
stablecoins, so capital can flow much more seamlessly than in the traditional
world.

dYdX perpetual markets are a good example of an instrument built on top of
more programmable and transparent infrastructure that also allows the market
to accomplish its most in demand goals: trading cryptocurrency exposure. Over
time, usability and liquidity will converge, making it easier for users who
want to leverage the non-custodial nature of decentralized perpetuals rather
than a centralized exchange. A lot of the market structure components
available through dYdX’s perpetual contract are the same as traditional venues
— off-chain orderbooks, maker taker liquidity, and professional market makers
— all of which make transition to decentralized financial products more user
friendly. The first contract offered by dYdX tracks the value of BTC relative
to USD, but dYdX can leverage the underlying infrastructure to easily support
perpetual contracts across a huge range of assets.

In addition to dYdX, two other platforms have launched non-custodial perpetual
markets: Futureswap and MCDEX. Futureswap is a decentralized derivatives
exchange that offers non-custodial trading products. Its first ETH/USD
contract will pool assets through liquidity pools and will provide exchange
functionality through an automated market maker, similar to Uniswap. MCDEX is
another derivatives platform that offers a non-custodial ETH/USD perpetual
product, with the key difference of requiring traders to collateralize their
positions with ETH, so the contracts are structured as inverse perpetuals.

![](https://integral.dydx.exchange/content/images/2020/05/Table--3.png)

### Conclusion

Perpetual markets are one of the most actively used financial products in the
cryptocurrency ecosystem. They play a powerful role in allowing users to
express financial exposure and capture some pretty high yields during extreme
market conditions. Luckily for users, the market is rapidly evolving. New
contracts are rushing to market, looking to address users’ most pressing needs
and most demanded features.

Already today, a variety of perpetual markets have launched and seen strong
traction in the market. Non-linear inverse perpetuals have been the most
popular type of contract so far, but vanilla perpetuals have benefited from
the recent increase in stablecoin users and total market capitalization. Non-
linear perpetuals have also benefited because they are extremely powerful
hedging tools for long term BTC holders that don’t want to sell their holdings
into fiat. This ability to short sell a non-linear inverse perpetual contract
to lock in the USD value and potentially collect funding for holding that
position down the line has also created a new cryptonative financial product,
the synthetic crypto dollar. A lot of the flow in today’s perpetual markets is
capital taking the opposite side of the futures curve.

While there is clear market demand for perpetual contracts, users still face
many issues when trading on today’s largest venues. Counterparty risk is high
when facing derivatives exchanges as the attack vectors are centralized to one
company. Hacks are rare but users are subject to each exchange's liquidation
mechanisms, many of which leave users with little transparency. To solve these
problems, perpetual markets are being created on top of Turing-complete
blockchains like Ethereum. These platforms transparently publish liquidation
details to public blockchains, allow users to maintain control of their funds
throughout the entire trading process,, and can be used to create a much
larger number of markets.

* * *

dYdX is the most powerful open trading platform for crypto assets with spot,
margin, and perpetual markets.

[Start trading on dYdX today](https://trade.dydx.exchange/perpetual/BTC-
USDC?trk-origin=perp-landing) and check out our new BTC <> USDC perpetual
market!

You can reach dYdX via email at contact@dydx.exchange, on
[twitter](https://twitter.com/dydxprotocol), or on our [official
telegram](https://t.me/dydxofficial).

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

