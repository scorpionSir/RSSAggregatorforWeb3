[ Curve Finance ](https://blog.curve.fi)

  * [Home](https://blog.curve.fi/)
  * [Trade on Curve](https://curve.fi/)

[ ](https://twitter.com/CurveFinance "Twitter")

Subscribe

# Building liquid staking with Curve

  * [ ](/author/michael/)

#### [Michael Egorov](/author/michael/)

Feb 24, 2020 • 2 min read

As proof of stake on Ethereum becomes closer, new PoS blockchains (Cosmos,
Tezos and others) have been launched, there are and will be stakeable
ERC20-compatible tokens (NuCypher, Livepeer, Ren Project, Skale, KEEP, The
Graph), staking-as-a-service looks more and more as a lucrative business.

However, centralized exchanges (such as Binance) quickly jumped on the
bandwagon of this business model and offered staking while the underlying
token can be traded on the exchange. This created a situation of tough
competition for cryptocurrency stakers while harming decentralization.

In order to fix this, the concept of Liquid Staking was created. There are a
few groups working on this concept and collaborating in [Liquid Staking
working group](https://t.me/liquidstaking), with the groups including but not
limited to [StakeDAO](https://github.com/StakeDAO/stakeDAO-Liquid-Pools),
[StakerDAO](https://www.stakerdao.com/), [P2P](https://p2p.org/) and others.
However, while it's certainly possible to tokenize stake, how easy it is to do
automatic market making for it?

Staked assets behave very similarly to interest-bearing tokens (such as
[cTokens](https://compound.finance/ctokens)): they have a uniformly growing
"target price". Real price can go slightly above and below the target, and
that's where good market-making opportunities appear.

Let's consider for the sake of example staking NuCypher's NU tokens which
cannot be quickly unbonded, and let's call the staking derivative which grows
as more NU are created stakedNU. In NuCypher, you can restake - reinvest
staking compensation into staking process, or not.

In the proposed arrangement, 5% of NU is not staked but placed in automatic
market-maker created by Curve, to do MM between stakedNU and NU. The stakedNU
token is created for all other (95%) of NU which are staked.

![](https://blog.curve.fi/content/images/2020/02/staking-MM.svg)

Let's consider two situations: price of stakedNU/NU being lower and higher
than the target price.

Suppose that at some point the target price p*=1.10, and the actual price
appeared to be lower: p=1.05. As soon as the price becomes significantly lower
than p*, we stop restaking NU, so that staking process has free (unbonded)
staking compensation. This compensation is used to buy off the discounted
stakedNU from the market created by Curve, and the obtained stakedNU are
immediately burned, so that all the underlying NU now correspond to less
stakedNU. Since p<p*, the increase of amount of staked NU per stakedNU is more
than the amount of NU not restaked, so this process makes a profit for "liquid
stakers" equal to:

[amount of NU compensation] * (p* - p) / p.

If it appears that p>p*, it's instead more profitable to sell stakedNU to the
pool. The staking DAO takes stakedNU from reserves and sells those to the pool
for more NU that the actual underlying NU the sold pieces had. Those NU are
immediately bonded and more stakedNU than was originally taken are created.
However, we need to redistribute profit from this arbitrage, so we burn the
excess of stakedNU to do that. The burnt amount is:

[amount of stakedNU sold] * (p - p*) / p*.

While NU was just chosen to be a good example, the mechanism above can be
applied to many digital assets: ETH 2.0, Livepeer, Ren Project, Skale, KEEP,
The Graph and others. Depending on restaking or unbonding dynamics, the source
of funds for buying discounted staked tokens could be different: if unbonding
time is fast, for example (several days for Livepeer), a larger amount can be
unbonded, and the price can be quickly brought up to the "peg".

In conclusion, the process described above allows to use Curve to do automatic
market-making for any staked asset, and use arbitrage with staking/unstaking
to push the price of the liquid stake back to its fundamental value and make
money in that process at the same time.

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

## How Curve hacked Curve

In March, a sUSD incentivized pool was launched with Synthetix. The trial was
overwhelmingly successful as, while having smaller value in the pool, the pool
was providing a much deeper liquidity than sETH/ETH Uniswap pool. However, on
April 20th (was it only a week ago?), we (Angel and I)

](/how-curve-hacked-curve/)

  * [ ](/author/michael/)

[Michael Egorov](/author/michael/) Apr 28, 2020 • 2 min read

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

