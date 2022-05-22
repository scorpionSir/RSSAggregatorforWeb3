[ Curve Finance ](https://blog.curve.fi)

  * [Home](https://blog.curve.fi/)
  * [Trade on Curve](https://curve.fi/)

[ ](https://twitter.com/CurveFinance "Twitter")

Subscribe

# How Curve hacked Curve

  * [ ](/author/michael/)

#### [Michael Egorov](/author/michael/)

Apr 28, 2020 • 2 min read

In March, a sUSD incentivized pool was
[launched](https://blog.synthetix.io/susd-liquidity-trial-with-curve-iearn/)
with Synthetix. The trial was overwhelmingly successful as, while having
smaller value in the pool, the pool was providing a much deeper liquidity than
sETH/ETH Uniswap pool.

However, on [April 20th](https://blog.synthetix.io/susd-curve-pool-
vulnerability-next-steps/) (was it only a week ago?), we
([Angel](https://twitter.com/angelangel0v) and
[I](https://twitter.com/newmichwill)) have found that there is a possibility
for the contract could potentially be slowly drained. In fact, we've drained
0.1 cent from it (and returned back). So what was the issue?

In order to understand what happened, we need to explain how the old sUSD pool
worked. That's actually a cool one. The pool was using ySUSD (sUSD lent
through [iearn](https://iearn.finance/)) and Y tokens - tokens of [Y
pool](https://beta.curve.fi/y). This way, composability of Curve was tested:
one can trade stablecoins against tokens representing Curve pools very
efficiently. Brilliant!

One of the issues with the pool was that it had a fairly high ETH gas usage
(about 2 million gas per exchange). That was acceptable by whales though.

So while going through the [code](https://github.com/curvefi/curve-
contract/blob/pool_susd_vulnerable/vyper/stableswap.vy), we've spotted two
places. First, adding a pool token instead of a stablecoin can use "virtual
price" (value per pool token) as a lending rate:

![](https://blog.curve.fi/content/images/2020/04/Screenshot-
from-2020-04-27-21-43-18.png)

Looks pretty innocent, isn't it? And since Y pool token cannot be unwrapped in
"non-lent-out" Y pool token, both exchange() and exchange_underlying() were
supposed to operate with the same Y pool token (while not unwrapping /
unwrapping ySUSD).

And here we have the place with a problem:

![](https://blog.curve.fi/content/images/2020/04/Screenshot-
from-2020-04-27-21-43-57.png)

At first, looks like nothing is going wrong here. Just changing from Compound
to iearn's Y tokens format.

The vulnerability in this call wasn't introduced by the changes in this
function: it was introduced by the lack of those. A reader could notice that
everything in exchange_underlying() works while using rate_i and rate_j,
however those shouldn't be used when one of the coins is Y token which cannot
be "unwrapped" into one single stablecoin. Using exchange_underlying() could
lead to getting more coins than expected by factor of virtual_price which was
about 1.014 at the time. This haven't been noticed before because iearn's zap
which was used for exchanges used safe exchange() method.

As soon as we've noticed the issue, we've contacted Synthetix team and quickly
[shut down](https://blog.synthetix.io/susd-curve-pool-vulnerability-next-
steps/) the pool using the available kill_me() method. The kill_me() method is
usable only during the first 2 months from the pool launch, and that time is
supposed to be used for extensive safety tests. The pool was
[relaunched](https://blog.synthetix.io/new-curve-pool-launch/) in a different
format - a very more simple contract, [fully audited by Trail of
Bits](https://www.curve.fi/audits/01-ToB.pdf) (no changes after audit), and no
lending.

The new pool appears to have very cheap exchange costs (typically, 100k-200k
gas per exchange). That enabled some good arbitrage opportunities.

What are the takeaways for the future?

  * Never deploy a pool with unaudited changes: no matter how small and obvious they are;
  * Use fuzzing tools for new changes to catch possible issues even before any audit is conducted;
  * Make optimizations to make pool composability more gas-efficient;
  * Continue hacking Curve to make it even safer for everyone.

## Sign up for more like this.

Enter your email Subscribe

[

## Discovery of a very unprobable Ledger JS signing issue

A Curve user wanted to swap 5 Bitcoin for wBTC. As Curve now supports native
Bitcoin deposit routed through the renVM, the user deposit the Bitcoin and
after six confirmations, Metamask prompted the user to confirm a transaction
to mint renBTC and swap it to wBTC (via the Curve sbtc

](/ledger-js-signing-issue/)

  * [ ](/author/angel/)

[Angel Angelov](/author/angel/) Jul 5, 2020 • 1 min read

[

## Building liquid staking with Curve

As proof of stake on Ethereum becomes closer, new PoS blockchains (Cosmos,
Tezos and others) have been launched, there are and will be stakeable
ERC20-compatible tokens (NuCypher, Livepeer, Ren Project, Skale, KEEP, The
Graph), staking-as-a-service looks more and more as a lucrative business.
However, centralized exchanges (such as Binance) quickly

](/building-liquid-staking-with-curve/)

  * [ ](/author/michael/)

[Michael Egorov](/author/michael/) Feb 24, 2020 • 2 min read

[

## Vulnerability disclosure: the discovery and the rescue

At 3 a.m. I woke up to 20 messages from Robert Leshner and Sam Sun. The news
was that the Curve contract had a critical (but not exploited) vulnerability
which allowed anyone to drain the smart contract. The bug wasn’t anything a
linter could catch: it was hidden

](/vulnerability-disclosure/)

  * [ ](/author/michael/)

[Michael Egorov](/author/michael/) Jan 25, 2020 • 3 min read

[Curve Finance](https://blog.curve.fi) (C) 2022

[Powered by Ghost](https://ghost.org/)

