[ Woobull ](https://woobull.com)

  * [About](https://woobull.com/about/)
  * [Charts](http://charts.woobull.com/)
  * [Articles](https://woobull.com/)
  * [→ Research](https://woobull.com/tag/research/)
  * [→ Infographics](https://woobull.com/tag/infographic/)
  * [→ Humour](https://woobull.com/tag/humour/)
  * [→ Bitcoin](https://woobull.com/tag/bitcoin/)
  * [→ Markets](https://woobull.com/tag/markets/)
  * [→ Dataviz](https://woobull.com/tag/data-visualisation/)
  * [→ Altcoins](https://woobull.com/tag/altcoins/)
  * [YouTube](https://www.youtube.com/channel/UCNSawUAJPtGqnhpucPqdDrw)

[ ](https://twitter.com/woonomic "Twitter")

Subscribe

[Research](https://woobull.com/tag/research/)

# Experiments on Cumulative Destruction

  * [ ](/author/willywoo/)

#### [Willy Woo](/author/willywoo/)

Apr 9, 2019 • 3 min read

## Two approaches to bring bitcoin-days-destroyed into the price domain

Okay, so this article is now well overdue given the recent price action. BTC
never rests! The last few months have been very productive in terms of
discovering new valuation metrics based on on-chain analytics. The recent
proposals using [coindays
destroyed](https://bitcoin.stackexchange.com/questions/845/what-are-bitcoin-
days-destroyed) by [Tamas
Blummer](https://medium.com/@tamas.blummer/liveliness-of-bitcoin-174001d016da)
and the team at [Adamant
Capital](https://medium.com/@adamant_capital/a-primer-on-bitcoin-investor-
sentiment-and-changes-in-saving-behavior-a5fb70109d32) have put this essential
metric once again on the map. We thought we’d give it a go at coming up with a
way to best translate the concept of destruction into a precise price level
for market analysis.

#### Experiment A: Cumulative Value-days Destroyed (CVDD) by Willy Woo

When coins move from one investor to another, the transaction carries both a
USD value and also destroys a time value relating to how long the original
investor held their coins. CVDD tracks the cumulative sum of this value-time
destruction as coins move from old hands into new hands as a ratio to the
market age. It is calculated with the following formula:

`CVDD_(USD)=(sum (bb"coin days destroyed" * price) )/ (days * 6000000`

Note that 6 million is used in calibrating the chart. This number is arbitrary
and would be different had we used hours or blocks as unit for the age of the
market.

CVDD has hit the historical Bitcoin price bottoms with remarkable accuracy.

![](https://woobull.com/content/images/2019/04/image-5.png)

Unlike [Delta Cap](https://medium.com/@kenoshaking/bitcoin-delta-
capitalization-1d51a7b256b4), CVDD tends to consistently climb in value - this
becomes useful to frame an increasing lower bound for a market bottom during
bear seasons when the market price is falling.

When used in conjunction with the Top Price model, CVDD and Top Price provides
upper and lower bands for price action.

![](https://woobull.com/content/images/2019/04/image-6.png)

When used in conjunction with CoinMetric's [Realised
Price](https://coinmetrics.io/realized-capitalization/), CVDD can help
visualization of Bitcoin's accumulation bottoms.

![](https://woobull.com/content/images/2019/04/image-7.png)

Both CVDD and Realised Price have remarkable resemblances in shape, its no
coincidence that they both use investor HODL time in their calculation.

It is important to note that both CVDD and Top Price are interesting
curiosities, and are not guaranteed to work in future cycles.

#### Experiment B: Transferred Price and Balanced Price by David Puell

Instead of using a 6-million figure, transferred price uses supply to bring
destruction into the price domain:

`bb"TransferredPrice"_(USD)=(sum(bb"coindays destroyed" * price)) / (days *
bb"supply")`

Looking at this as a life-to-date moving average of spending behavior (again,
old hands selling into new hands), it can be assumed that when subtracted from
realized price (the average paid for all coins in the market), a “fair”
valuation measure emerges. Balanced price denotes the level at which, during
bear markets, a full detox has been achieved — market price matching what was
paid minus what was spent.

`bb"BalancedPrice"_(USD)=bb"RealisedPrice"_(USD)-bb"TransferredPrice"_(USD)`![](https://woobull.com/content/images/2019/04/image-8.png)

It goes without saying that this evokes [Delta
Price](https://medium.com/@kenoshaking/bitcoin-delta-
capitalization-1d51a7b256b4) in both calculation and visualization. We believe
that Delta Price serves as a technical analysis proxy of Balanced Price. The
former seems to be agile enough to catch exact bottoms — the “wicks” — while
the latter catches the full accumulation level prior to the bull run, also
defining the brief moment when price remains below it as “capitulation.”

More iterations on coindays destroyed to follow. Stay tuned…

* * *

  * This article was co-authored with David Puell, Head of Research at Adaptive Capital.
  * A live chart of these metrics is available at [Woobull Charts](http://charts.woobull.com/bitcoin-price-models/)

## Sign up for more like this.

Enter your email Subscribe

[

## Supply Shock, predicting price by quantifying intent to buy and sell

IntroductionIn any market, price is driven by demand and supply. This is a
fundamental. The most obvious way of seeing this is in the bid and asks
between buyers and sellers. A more nuanced way would be to wave a magic wand
and gauge the intent of investors before the

](/quantifying-supply-shock/)

  * [ ](/author/willywoo/)

[Willy Woo](/author/willywoo/) Aug 10, 2021 • 4 min read

[

## The two types of Altcoins, an investor's view

This is a thread on altcoins, first published on Twitter. Altcoins are
nuanced. We have: Protocol coinsUtility tokensSecurity tokensNon-fungible
tokensBut to an investor, there's only 2 types. Oscillators and Degenerators.
You can spot them on this chart of the entire market. The vast majority of
alt-coins are Degenerators. Their price

](/the-two-types-of-altcoins-an-investors-view/)

  * [ ](/author/willywoo/)

[Willy Woo](/author/willywoo/) Nov 7, 2019 • 2 min read

[

## Introducing the Difficulty Ribbon, signaling the best times to buy Bitcoin

Introducing the Bitcoin Difficulty Ribbon. When the ribbon compresses, or
flips negative, these are the best times to buy Bitcoin. The ribbon consists
of simple moving averages on mining difficulty so we can easily see the rate
of change in difficulty. How it the Difficulty Ribbon worksThis visualisation
of network

](/introducing-the-difficulty-ribbon-the-best-times-to-buy-bitcoin/)

  * [ ](/author/willywoo/)

[Willy Woo](/author/willywoo/) Aug 1, 2019 • 2 min read

[Woobull](https://woobull.com) (C) 2022

[Powered by Ghost](https://ghost.org/)

