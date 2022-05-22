[![Colony
Blog](/content/images/2018/11/horizontal_white-1-1.png)](https://blog.colony.io)

  * [Blog](https://blog.colony.io/)
  * [Colony](https://colony.io)

[ ](https://twitter.com/joincolony "Twitter")

[ ](https://feedly.com/i/subscription/feed/https://blog.colony.io/rss/ "RSS")

27 May 2020 / [ICO](/tag/ico/)

# Introducing Coin Machine 🎰

### A simple way to sell tokens.  

Ethereum’s DeFi sector is vibrant and growing, with many projects presenting
sophisticated proposals for putting financial services on the blockchain.
Among these, the problem of fundraising—selling tokens to support
projects—remains evergreen, with many ideas
([DAICOs](https://ethresear.ch/t/explanation-of-daicos/465), [Continuous
Organizations](https://github.com/C-ORG/whitepaper), and
[various](https://nexusmutual.io/)
[flavors](https://fundraising.aragon.black/) of [bonding
curves](https://www.bancor.network/) and [market
makers](https://uniswap.org/)) floating around the ecosystem.

We at Colony were looking for a reasonable way to sell tokens, but found that
none of these mechanisms quite met our needs. Some were too complex, or too
prone to manipulation, or had difficult UX. Ultimately we wanted something
dead-simple and easy-to-use, but which still supported some key behaviours.
So, without further ado, we present: Coin Machine.

Coin Machine is a mechanism which sells limited amounts of tokens in fixed-
price batches, adjusting prices up or down in between sale periods based on
recent demand. Think of it like a continuous series of hard-capped micro-ICOs
in which token price is determined by performance in prior sales. Coin Machine
sacrifices continual availability and real-time price adjustment for the
simple semantics of fixed price and fixed supply, thereby also sidestepping
the challenges of price manipulation, volatility, and front-running.

![](https://blog.colony.io/content/images/2020/11/Coin-Machine-UI.png)The Coin
Machine UI

Specifically, Coin Machine takes the following parameters: a target and
maximum number of tokens to sell per period, as well as a period length (i.e.
hour, day) as well as a number of periods to use as a price averaging window.
Coin Machine then sells _up to_ _the maximum_ number of tokens per period, but
adjusts the prices based on the target number of tokens. In this way, if more
than the target number of tokens is sold each period (representing high
demand), the prices will adjust upward. Alternatively, if fewer than the
target number of tokens are sold, the prices will adjust downward. If exactly
the target number of tokens are sold each period, prices remain constant,
while the length of the averaging window determines the volatility of price
over time.

While the interval-based nature of the adjustment means that prices will
always slightly lag the market, we feel that given the mechanism’s purpose—to
bring tokens into circulation, rather than create a perpetual market-
maker—this is an acceptable tradeoff. If we create some small arbitrage
opportunity, then Colony is served by having more tokens enter the market; it
is not necessary that we capture 100% of the value of the tokens sold, and the
cap on the maximum number of tokens sold bounds the upside of any arbitrage.
In exchange, we gain simplicity and security, while still allowing for prices
to automatically adjust, which we believe is an appropriate balance for this
use-case.

* * *

![](https://blog.colony.io/content/images/2020/02/horizontal_00284B-33-.png)

 _Colony makes it easy for people all over the world to build organisations
together, online._

  
 _Join the conversation on_[ _Discord_](https://clny.io/discord) _, follow us
on_[ _Twitter_](https://twitter.com/joincolony/) _, sign up for (occasional
and awesome)_[ _email updates_](https://colony.io/) _, or if you’re feeling
old-skool, drop us an_[ _email_](/cdn-cgi/l/email-
protection#88e0ede4e4e7c8ebe7e4e7e6f1a6e1e7) _._

![Daniel Kronovet](https://blog.colony.io/content/images/2020/03/sea.jpg)

#### [Daniel Kronovet](/author/krono/)

Research engineer at Colony, focused on experimental decision-making
mechanisms.

[Read More](/author/krono/)

-- Colony Blog --

### [ICO](/tag/ico/)

  * [The Colony Token Sale](/the-colony-token-sale-7ac14c845bc0/)

[1 post →](/tag/ico/) [ ](/re-introducing-colony/)

[ Blockchain

## (Re)Introducing Colony

The important thing is this: we’re about to launch New Colony.

](/re-introducing-colony/)

  * Jack du Rose 

[![Jack du
Rose](https://blog.colony.io/content/images/2018/11/NUmw0Wrn_400x400.jpg)](/author/jack/)

2 min read

[ ](/2020-and-beyond/)

[ community

## Colony 2020 and Beyond

(an interview with co-founder Jack Du Rose) On March 25, 2020 I had the
pleasure of interviewing Colony co-founder, Jack du Rose. We ended up having a
delightfully broad-reaching discussion, covering: The history

](/2020-and-beyond/)

  * Corey Morrow 

[![Corey
Morrow](https://blog.colony.io/content/images/2020/05/1.png)](/author/corey/)

13 min read

[ ![Colony Blog icon](/content/images/2018/11/logomark_color-2.png) Colony
Blog ](https://blog.colony.io)

--

Introducing Coin Machine 🎰

Share this

[
](https://twitter.com/share?text=Introducing%20Coin%20Machine%20%F0%9F%8E%B0&url=https://blog.colony.io/introducing-
coin-machine/)

[Colony Blog](https://blog.colony.io) (C) 2022 [Latest
Posts](https://blog.colony.io) [Twitter](https://twitter.com/joincolony)
[Ghost](https://ghost.org)

![Ghostboard
pixel](https://ghostboard.io/api/noscript/605e1f5f268aa214c195a5e3/pixel.gif)

