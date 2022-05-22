[ NAKAMOTO ](https://nakamoto.com)

  * [Home](https://nakamoto.com/)
  * [Twitter](https://twitter.com/nakamoto)
  * [Contribute](https://nakamoto.com/contribute/)
  * [About](https://nakamoto.com/about/)

__

__

# A beginner's guide to DeFi

Jan 3, 2020  11 min read  [Linda J. Xie](/author/ljxie/ "Linda J. Xie")

[ ![A beginner's guide to
DeFi](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)
](/beginners-guide-to-defi/)

Decentralized finance, also referred to as “DeFi” or open finance, aims to
recreate traditional financial systems (such as lending, borrowing,
derivatives, and exchange) with automation in place of middlemen. Once fully
automated, the financial building blocks of DeFi can be composed to produce
more complex capabilities. Today, the primary venue for decentralized finance
is [Ethereum](https://blog.coinbase.com/a-beginners-guide-to-
ethereum-46dd486ceecf), but in principle these ideas can be implemented on any
smart contract platform.

In this beginner’s guide to decentralized finance (“DeFi”) we review the
following:

  *  _ _ _Stablecoins.___ A building block of decentralized finance. Unlike cryptocurrencies like Bitcoin or Ethereum that are known for their price volatility, a stablecoin is engineered to remain “stable” at exactly 1.00 units of fiat. Most stablecoins are pegged to the USD, but some are in other fiat currencies like the Chinese RMB.
  *  _Decentralized lending._ Programmatically take out a loan on the blockchain. No bank account required.
  *  _Decentralized exchanges_. Buy and sell cryptocurrencies through a blockchain, rather than a centralized exchange like Coinbase. In principle, a machine can trade on these!
  *  _Collateralization_. Provide digital assets to collateralize your decentralized loans, providing the lender some recourse in the event of default.
  *  _Decentralized Identity_. Identities are used in the context of smart contracts for things like assessing your creditworthiness for a decentralized loan.
  *  _ _ _Composability_. __Snapping together DeFi functions that do different things, much like software libraries. For example, if one contract takes in crypto and generates interest, the second contract could automatically reinvest that interest.
  *  _Risk management_. High returns in DeFi are often accompanied by even higher risks. Fortunately, new tools are arising to help hedge these risks.

Let’s go through these concepts one by one.

# Stablecoins

If we try recreating traditional financial products on a blockchain, we are
faced with an immediate problem: price volatility. Specifically, the native
cryptocurrency of the Ethereum blockchain (namely ETH) experiences [large
intraday swings](https://www.coinbase.com/price/ethereum) in the USD/ETH
exchange rate, sometimes moving 10% or more in a single day.  
  
An instrument with this degree of price volatility is less than ideal for a
number of traditional financial products. For example, if you take out a loan,
you don’t want loan payments to oscillate by 10% right before a payment. That
degree of volatility would make it hard to plan for the future.  
  
Stablecoins are one solution to this problem. These are cryptocurrencies
specially engineered to remain “stable” at an exchange rate of approximately
1.00 units of fiat per coin. The [Stablecoin
Index](https://stablecoinindex.com/) and [Stablecoin
Stats](https://stablecoinstats.com/) provide a good list of the top
stablecoins.  
  
There are three general categories of stablecoins: centralized fiat-
collateralized, decentralized crypto-collateralized, and decentralized
algorithmic.

  1.  _Centralized fiat-collateralized stablecoins_ are backed 1:1 by fiat in a bank account. For example, the stablecoin [USD Coin (USDC)](https://www.coinbase.com/usdc) issued by Coinbase is backed 1:1 by US dollars in a bank account. There is little risk to holding or using the coin as long as you trust the issuing entity and underlying fiat. Another benefit is that there is a centralized entity that is liable if something goes wrong, which many individuals and businesses prefer. In the US, FDIC deposit insurance covers up to at least $250,000, while other countries have their own [deposit insurance](https://en.wikipedia.org/wiki/Deposit_insurance) terms. While these sound like ideal features, not everyone has access to centralized stablecoins. For example, the [user agreement](https://support.usdc.circle.com/hc/en-us/articles/360001233386-Circle-USDC-User-Agreement) for USDC states that it is only available in [supported jurisdictions](https://support.usdc.circle.com/hc/en-us/articles/360015179832) and users are prohibited from transacting USDC for certain activities.
  2.  _Decentralized crypto-collateralized stablecoins_ don’t have a central operator or user agreement. This means anyone can use them without the permission of a company or government. However, the tradeoff to not directly backing a stablecoin with fiat is increased complexity around maintaining stability. Rather than the simple model of USDC where $1000 of USDC is backed by $1000 in a bank, crypto-collateralized stablecoins back $1000 of their coin with at least $1000 of (highly volatile) cryptocurrency.  
  
For example, [Maker](https://makerdao.com/en/) is a system built on Ethereum
that governs a decentralized stablecoin called
[DAI](http://coinbase.com/earn/dai). DAI aims to be pegged at 1.00 USD. The
way the peg works is that DAI can be “minted” by anyone within the Maker
system by locking up crypto as collateral (primarily ETH) and taking out a
loan of DAI. The collateral provided needs to be greater than the amount
borrowed so that the loan is overcollateralized.  
  
For example, you can lock up $200 worth of ETH as collateral to borrow $100
worth of DAI, which you can then use to trade on an exchange. The main reason
to do this is leverage - if you believe the price of ETH will not drop
significantly, in which case you are getting a “free” $100 to trade on crypto
exchanges. If the price of ETH drops so that your $200 worth of ETH is now
below the collateralization requirement, the Maker algorithm will seize your
collateral and liquidate it to get back ~$100. In this fashion the Maker
algorithm tries not to lose money on a loan.  
  
While the Maker system is significantly more complex than something like USDC,
in theory an end user of DAI who isn’t minting wouldn’t need to understand the
complexity, in much the same way that users of normal US dollars don’t need to
understand the intricacies of monetary policy. With that said, DAI does
present its own risks, including smart contract risk and the possibility of
DAI breaking the peg and trading significantly above or below 1.00 USD/DAI.

  3.  _Decentralized algorithmic stablecoins_ are the third class of stablecoins. These do not have any collateral backing their system, relying solely on algorithms to get the price to remain stable. One example includes [Basis](https://www.basis.io/), which shut down before it was launched. A concern some have with this model is that a well funded and motivated entity could attack such a system and drive people to lose confidence in the stability of the peg. This could then lead to a death spiral and the collapse of the stablecoin. 

In general, the first two types of stablecoins have proven most popular.
Whether it is fiat or crypto providing the collateral, people appear to want
certainty around price stability. With that said, there are ongoing
experiments around the third class of stablecoin, with people looking to
combine both the crypto-collateralization and algorithmic elements.

# Decentralized lending

Given functional stablecoins like USDC and DAI, we can start rebuilding pieces
of the traditional financial system as automated smart contracts. One of the
most fundamental is the concept of borrowing and lending.

There are a number of DeFi platforms which enable borrowing and lending of
Ethereum tokens directly through smart contracts, like
[Compound](https://compound.finance/), [dYdX](https://dydx.exchange/), and
[Dharma](https://www.dharma.io/). An impressive feature of these smart
contracts is that a borrower need not find a lender or vice versa. Instead,
the smart contract replaces the role of the middleman, and interest rates are
calculated algorithmically according to supply and demand.

## Centralized order books for lending and borrowing

Before we explain how this works, it’s worth reviewing how some _centralized_
crypto exchanges implement borrowing and lending. Here’s a visual of the
Bitfinex [funding book](https://www.bitfinex.com/funding_book):

![](https://lh5.googleusercontent.com/YwjNlwqgZwB0M8Jfi3qIXUe0kACS6NfS9oXnd8quDBA5k1rDm_wfK-
ayXMLt3UK-
Bpr8e_WyZLItMZwh905qCD_Vcw6GEEotvDzR276NKeiKEgkq9ScmLgwdjXAk7t72-K2qSvw4)

  
To understand what is being shown in this snapshot, start with the left hand
side. The first row represents a borrower in the market who is willing to take
out a 30-day loan for $4,421.58 at a 0.0265% daily rate. Right below them is
another borrower willing to take out a 30-day loan for $34,292.38 at a
slightly lower 0.0263% interest rate.  
  
On the right hand side are the lenders. The first row represents a lender
willing to lend out up to $8,199.32 for 2 days at a 0.027418% daily rate. The
next row is someone willing to lend $255.68 for two days at the slightly
higher rate of 0.027436% per day.  
  
And so on and so forth. This is how a centralized order book for loans works.
In the above example, the highest rate a borrower is willing to accept is
0.0265% daily interest, while the lowest rate a lender is willing to give is
0.027418% daily interest. One of these two parties will give in and either
raise or lower their price of money, and then a deal will be made. Bitfinex
provides the service to set up the order book and match users, and then takes
a cut off the top of each loan for their trouble.

## Decentralized order books for lending and borrowing

Some decentralized services for lending and borrowing take this to the next
level. Rather than building an order book and facilitating matches, they allow
users to directly lend or borrow from the smart contract itself, which
dynamically raises or lowers interest rates to match. For example, if a large
amount of crypto is borrowed from the smart contract, a higher interest rate
is charged to borrowers. Moreover, in order to borrow funds, a user needs to
provide collateral to the smart contract, providing an amount greater than
what was borrowed so the loan is overcollateralized.

But why is decentralized lending even useful? The answer is that it’s a
massively scalable application. A crypto service which makes more interest
than traditional bank accounts with lower risk could in theory attract
billions in deposits. Compound is already at
[$120M](https://compound.finance/) in deposits, and other services are growing
fast. The main risks are related to smart contract bugs and crypto volatility,
but the interest rates are also substantially higher than typical bank rates
of 2% or lower. Here’s a snapshot of interest rates that can be earned for
lending out stablecoins on different platforms, from
[LoanScan](https://loanscan.io/):

![](https://lh4.googleusercontent.com/nUof1_mbV2dTx7GDa2RcFHH2SCGX7jE8W0hCfZ4f4hJzcXwDNedU0vJvjXsXiihMH3TiuLb3CTYWR1yQ193BGFQbdZCijfqUQrpLNd_QzDNgUXQov8Zbjs2M3BhyT1v5tf564KrE)

# Decentralized exchange

Decentralized crypto exchanges attempt to put services like Coinbase Pro on
the blockchain. That is, they aim to facilitate trades of different
cryptocurrencies between two parties.

To understand the use case, start with centralized cryptocurrency exchanges.
These exchanges, like Coinbase Pro, act as an intermediary and custodian where
two parties deposit their assets and are able to trade with each other. While
they have worked at scale to facilitate billions of dollars in trades,
centralized exchanges do present a single point of failure that can be hacked,
censor transactions, or prevent certain people from trading.

Decentralized exchanges aim to address this by using smart contracts to reduce
or eliminate middleman.The dream is fully peer-to-peer exchange of all digital
assets.

There are a number of projects pursuing decentralized exchange of Ethereum-
based tokens in various forms, like [Uniswap](https://uniswap.io/),
[0x](https://0x.org/), and [Kyber](https://kyber.network/). For example,
Uniswap utilizes a so-called automated market maker (AMM) to algorithmically
provide liquidity. Buyers and sellers pull liquidity from the smart contract
directly and receive a price quote based on the token quantity desired and the
liquidity available. Uniswap will always quote a price regardless of the order
size by asymptotically increasing the price as the size of the order
increases.  
  
Decentralized exchanges can currently handle only a fraction of the volume of
centralized exchanges, and as such can’t really convert large amounts of money
back and forth. Moreover, many of these projects are limited to trading
Ethereum-based tokens on the Ethereum blockchain, which limits their access to
large cap coins with their own chains. Still, there are promising technologies
like [atomic swaps](https://blockgeeks.com/guides/atomic-swaps/) and [zk-
STARKs](https://blog.0xproject.com/introducing-openzkp-1dea6b22dceb) that may
address these limitations.

# Decentralized identity

One issue with the decentralized lending and borrowing services mentioned thus
far is that they require quite a lot of collateral. This overcollateralization
requirement can be a highly inefficient use of capital -- and many people do
not have the extra funds in the first place to provide as collateral.  
  
However, people are working on decentralized identity and reputation systems
that will reduce the collateralization requirements. One of the first
applications would be building blockchain analogs of fiat-based credit bureaus
like Experian, TransUnion, and Equifax that institutions like banks rely on
for credit scores.  
  
Now, to anticipate an objection, it’s certainly true that credit bureaus can
put certain groups such as international and young people at a disadvantage.
But newer services like Lending Club have addressed the problem of
overreliance on FICO scores by offering additional data points like home
ownership, income, and length of employment.

Decentralized identity and reputation services could offer something similar
by including attributes such as social media reputation, history of repayment
of previous loans, vouching from other reputable users, and the like. Making
this useful for actual financial decisions will require a lot of trial and
error on the specific data points to use and the corresponding collateral
requirements, and we are just at the beginning of that process.  
  
Interestingly, in the long run, DeFi with decentralized identity systems could
become another option for people locked out of traditional financial systems.
For example, there are [one billion people](https://id4d.worldbank.org/global-
dataset) without an official ID, and ~50% of women in low income countries
lack an ID. However, many of these people _do_ have smartphones. So it’s
possible that once decentralized IDs work in the developed world, that they
could be rapidly exported to the developing world as a leapfrog technology --
much like smartphones themselves.

# Composability

We’ve covered decentralized stablecoins, loans, exchanges, and identity. But
perhaps the most important aspect of building decentralized finance building
blocks on a smart contract platform like Ethereum is the _composability_. Just
like a software library, smart contracts for different financial applications
can plug into each other like lego pieces.  
  
For example, if you want to add the ability to trade tokenized assets on your
platform, you can easily make the assets tradable by integrating a
decentralized exchange protocol. And these smart contract lego pieces can even
create completely new concepts that haven’t been explored in the traditional
world.  
  
One example is the project called [2100](https://2100.co/) that brings
together DeFi and social media by allowing participants to use their Twitter
accounts to “mint” new tokens for themselves, essentially generating digital
dollars from their social capital. Popular accounts can put out premium
content that is only accessible to a specific group of token holders, which
allows them to monetize their following. One can then do interesting things
like bet on certain Twitter accounts becoming more popular.  
  
Another example is the project called
[PoolTogether](https://www.pooltogether.com/), which combines DeFi and
lotteries to create a “no-loss” lottery. Users purchase lottery tickets on-
chain, and all funds from ticket purchases earn interest on Compound. At the
end of the lottery, everyone gets their funds back -- but one person gets all
of the interest earned on the pooled money. It’s essentially a way to use
lottery mechanics to incentive savings and wealth creation!

As DeFi matures, we should expect the libraries to start getting used outside
the crypto community. Eventually you’ll be able to add one line of code to add
a full decentralized marketplace to a video game, or another line of code to
allow merchants in your e-commerce store to earn interest on their balance.

# Risks

While DeFi is fascinating, it is important to acknowledge the risks that come
with it. Let’s enumerate some classes of risk:

  *  _Smart contract risk._ Many of these systems are new and need more time to be battle tested. When protocols are interacting with each other, the smart contract risk compounds. If one protocol has a critical smart contract bug, then it can cause the entire system to be vulnerable. It would be wise to avoid putting too much capital in any of these systems during the early days.  

  *  _Collateralization and volatility risk._ There are also risks associated with specific collateral types used to back loans. Overcollateralization reduces volatility risk, but if the price of the collateralized asset falls too quickly, a margin call isn’t guaranteed to cover the full amount that was borrowed. However this should be less of a risk with a reasonable collateralization ratio and vetted collateral types. Another potential issue is that the interest rate volatility on many DeFi platforms could make it impractical for someone to participate. There will likely be interest rate swaps or other methods to lock in a rate for a premium but this also adds its own complexities.  

  *  _Regulatory risk._ DeFi platforms have varying degrees of decentralization, and we have not yet seen court cases that test all the claims being made. We’ll have to see what happens here.

Decentralized insurance like [Nexus Mutual](https://nexusmutual.io/) and
[Convexity](https://twitter.com/snarkyzk/status/1194442219530280960?lang=en)
are an area within DeFi that provides the ability to hedge some of these
risks. Prediction markets like [Augur](https://www.augur.net/) also address
the hedging use case by allowing users to bet on the probability that there
will be a smart contract issue with one of the protocols they are using.  
  
With that said, these hedging methods themselves are in their infancy, and add
smart contract risk of their own. We do think they will mature, however. And
if the DeFi space gets large enough, then traditional insurance companies
might offer products too.

# Resources

The DeFi space is large and growing larger. Hundreds of millions of dollars
worth of cryptocurrency has already been deployed and the space’s future
potential is massive. This article only covered a handful of use cases, but
we’ve provided some further reading below to understand DeFi further and keep
up with the developments.

 _Understanding DeFi_

  * [The DeFi Series](https://medium.com/alethio/the-defi-series-an-overview-of-the-ecosystem-and-major-protocols-da27d7b11191)
  * [Decentralized Lending](https://medium.com/dydxderivatives/decentralized-lending-an-overview-1e00fdc2d3ee)
  * [DeFiprime](https://defiprime.com/)

 _Keeping up with DeFi_

  * [The Defiant newsletter](https://thedefiant.substack.com/)
  * [Compound Digest newsletter](https://compound.substack.com/)
  * [DeFi Pulse](https://defipulse.com/)

Thank you to Balaji Srinivasan, Will Warren, and Jordan Clifford for reviewing
this post!

 _Disclaimer: Linda Xie is a Managing Director of Scalar Capital Management,
LLC, an investment manager focused on cryptoassets. This post is not
investment advice._

[__](https://www.facebook.com/sharer.php?u=https://nakamoto.com/beginners-
guide-to-
defi/)[__](https://twitter.com/intent/tweet?url=https://nakamoto.com/beginners-
guide-to-
defi/&text=A%20beginner's%20guide%20to%20DeFi)[__](https://pinterest.com/pin/create/button/?url=https://nakamoto.com/beginners-
guide-to-
defi/&media=&description=A%20beginner's%20guide%20to%20DeFi)[__](https://www.linkedin.com/shareArticle?mini=true&url=https://nakamoto.com/beginners-
guide-to-
defi/&title=A%20beginner's%20guide%20to%20DeFi)[__](https://reddit.com/submit?url=https://nakamoto.com/beginners-
guide-to-
defi/&title=A%20beginner's%20guide%20to%20DeFi)[__](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https://nakamoto.com/beginners-
guide-to-
defi/&title=A%20beginner's%20guide%20to%20DeFi)[__](http://vk.com/share.php?url=https://nakamoto.com/beginners-
guide-to-
defi/&title=A%20beginner's%20guide%20to%20DeFi)[__](https://getpocket.com/edit?url=https://nakamoto.com/beginners-
guide-to-defi/)[__](https://t.me/share/url?url=https://nakamoto.com/beginners-
guide-to-defi/&text=A%20beginner's%20guide%20to%20DeFi)

![Linda J.
Xie](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

#### Linda J. Xie

[Website](https://lindajxie.com) [Twitter](https://twitter.com/@ljxie) [More
posts](/author/ljxie/)

Cofounder of Scalar Capital and advisor to 0x. Previously Product Manager at
Coinbase.

[__Previous Post](/coinbases-pragmatic-crypto-culture/)

[Next Post __](/it-will-take-years-for-smart-people-to-understand-
cryptocurrencies/)

### You might also like...

[ ![What will happen to cryptocurrency in the
2020s?](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)
](/crypto-in-the-2020s/)

##  [What will happen to cryptocurrency in the 2020s?](/crypto-in-the-2020s/)

Jan 5, 2020  7 min read

Please enable JavaScript to view the [comments powered by
Disqus.](https://disqus.com/?ref_noscript)

[ NAKAMOTO ](https://nakamoto.com)

__

