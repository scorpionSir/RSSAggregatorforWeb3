[ Curve Finance ](https://blog.curve.fi)

  * [Home](https://blog.curve.fi/)
  * [Trade on Curve](https://curve.fi/)

[ ](https://twitter.com/CurveFinance "Twitter")

Subscribe

# Discovery of a very unprobable Ledger JS signing issue

  * [ ](/author/angel/)

#### [Angel Angelov](/author/angel/)

Jul 5, 2020 • 1 min read

A Curve user wanted to swap 5 Bitcoin for wBTC.

As Curve now supports native Bitcoin deposit routed through the renVM, the
user deposit the Bitcoin and after six confirmations, Metamask prompted the
user to confirm a transaction to mint renBTC and swap it to wBTC (via the
Curve sbtc pool).

The Ledger device then showed the transaction on the device but when user
clicked to accept it, the device then responded with an error 6985 (user
cancelled).

Working with [@btchip](https://twitter.com/BTChip) we discovered that in this
case the transaction data was encoded using EIP-155 [Simple replay attack
protection](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-155.md)
which includes v, s, r (the three parts of a transaction signature).

When Ethereum Ledger app was created EIP 155 didn't exist and as a result, the
app doesn't know when the transaction data ends as the three parts (v, s, r)
can either be missing (pre EIP-155) or not (using EIP-155).

Communication with a Ledger happens in chunks because the communication buffer
is limited. In this case, the user had an unlucky combination of derivation
path and transaction data  
and ended with a chunk that could look like the final part of a valid pre EIP
155 tx for the parser(right before the start of v, r, s). As a result, the
parser thought it was signing a pre EIP-155 transaction while it was actually
signing an EIP-155 transaction. The parser thinks data transmission is
finished and returns an error on the v,r,s chunk of data which follows.

The user tried Ledger with Metamask, Ledger directly through Curve, 3
different ledgers Nano S devices as well as 2 OSes, MyCrypto and MyEtherWallet
without success.

I managed to successfully resolve the issue, while
[@btchip](https://twitter.com/BTChip) was working on a fix, by getting the
user to mint renBTC by using a recovery function in the contract which
resulted in different transaction data which Ledger javascript library parsed
correctly.

Ledger has now fixed the issue in their js library by checking if the
transaction is EIP-155 or not to ensure this bug isn't accidentally
reproduced.

## Sign up for more like this.

Enter your email Subscribe

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

