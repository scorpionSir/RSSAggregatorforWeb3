[ ![0xb10c logo](/0xb10c.png) ](/)

# 0xB10C

Bitcoin Developer

[Blog](/) [Mempool Observations](/mempool-observations) [Projects](/projects)
[Talks](/talks)

☀  requires JS

##  transactionfee.info (2018 version)

#####

Monday, January 22, 2018

We build transactionfee.info in 2018 to raise awareness about the inefficient
use of block space by exchanges, services, and wallets. The project is a joint
effort with [Bitrefill](https://www.bitrefill.com/?utm_source=b10c_me) CEO
[@ziggamon](https://twitter.com/ziggamon).

In early 2018 the price of bitcoin surged to 20.000 USD. At that time we saw
more than [400.000 daily
transactions](https://transactionfee.info/charts/transactions-per-
day/?start=2017-08-02&end=2018-04-15) on the Bitcoin network which caused a
steep increase in transaction fees. A lot of exchanges, services and wallets
did not use the block space efficiently. We build
[transactionfee.info](https://transactionfee.info) to raise community
awareness.

![Header and input field for the old transactionfee.info
site](/data/projects/transactionfee-info/old-txid-input.png) input field of
the 2018 version transactionfee.info site

Only a few exchanges and services made use of payment batching or spend SegWit
outputs in 2018. This meant, for example, that every withdrawal was costly for
exchanges as the withdrawal transaction takes up a lot of space in the
blockchain. Often the transaction fees or even a higher fixed fee was deducted
from the user's withdrawal amount. Our site allowed users to check the fee
efficiency of their transactions and their wallets. It calculated how much
fees could have been saved by using, for example, payment batching or by
spending SegWit outputs. Green checkmarks for fee- and space-saving behavior
and red crosses for inefficient and wasteful behavior.

[WayBackMachine: 26th August
2018](https://web.archive.org/web/20180826025416/https://transactionfee.info/)

> Check out <https://t.co/H6LeHNaZax>.  
>  
> It’s a new tool I’ve helped create (code by
> [@0xB10C](https://twitter.com/0xB10C?ref_src=twsrc%5Etfw)). Helps you see
> how well optimized bitcoin transactions are.  
>  
> Just paste a tx id and see if you’re overpaying for your bitcoin
> transactions and withdrawals.  
>  
> Feedback welcome! [pic.twitter.com/4jUMGky7SS](https://t.co/4jUMGky7SS)
>
> -- Sergej Kotliar (@ziggamon) [January 22,
> 2018](https://twitter.com/ziggamon/status/955457158392397825?ref_src=twsrc%5Etfw)

> Samourai users are paying the lowest transaction fees according to
> <https://t.co/ntB5Sz3mww> \- Don't use wallets that abuse their users. No
> Android device? Use
> [@GreenAddress](https://twitter.com/GreenAddress?ref_src=twsrc%5Etfw) \- If
> you don't want to use Samourai install
> [@ElectrumWallet](https://twitter.com/ElectrumWallet?ref_src=twsrc%5Etfw) \-
> This isn't marketing, this is common sense.
> [pic.twitter.com/vGhSnf9shv](https://t.co/vGhSnf9shv)
>
> -- Samourai Wallet (@SamouraiWallet) [February 4,
> 2018](https://twitter.com/SamouraiWallet/status/960152335799504901?ref_src=twsrc%5Etfw)

Later, we added a subsection with charts about payment and feerate metrics to
the site. We offered all data under a [CC0 "No Rights Reserved"
license](https://creativecommons.org/share-your-work/public-domain/cc0/). The
transactionfee.info website has appeared in numerous online news articles
since then, one, for example, being [thenextweb.com: Bitcoin’s median
transaction fee lowest since 2011 — nearing
BCH](https://thenextweb.com/hardfork/2018/05/28/bitcoins-median-transaction-
fee-some-of-the-lowest-since-2011/). The transactionfee.info data even [made
its way into
academia](https://scholar.google.de/scholar?q=%22transactionfee.info%22).

> Presenting “Payments” per day, a more accurate representation of real
> economic activity on the Bitcoin network.  
>  
> (It’s a count of all outputs that are not change outputs back to the
> sender)<https://t.co/kyuTMXz09A>  
>  
> Props [@0xB10C](https://twitter.com/0xB10C?ref_src=twsrc%5Etfw)
> [pic.twitter.com/5Z1d5PQ0gQ](https://t.co/5Z1d5PQ0gQ)
>
> -- Sergej Kotliar (@ziggamon) [February 11,
> 2018](https://twitter.com/ziggamon/status/962691031702552577?ref_src=twsrc%5Etfw)

> The potential block space efficiency gains from transaction batching are
> even greater than from implementing SegWit. Thus far the services that have
> implemented batching are imperceptible in the grand scheme of things. Plenty
> of room for improvement! <https://t.co/uPSWiaXdUT>
> [pic.twitter.com/bDj85dmXQ7](https://t.co/bDj85dmXQ7)
>
> -- Jameson Lopp (@lopp) [February 22,
> 2018](https://twitter.com/lopp/status/966730277111324674?ref_src=twsrc%5Etfw)

> New feature on <https://t.co/2G9sgi1yL5>: Bitcoin transaction fees
> distribution by percentile.  
>  
> You can see the fee rates rising and and falling and which fees are “high”
> vs “low” at any given time.<https://t.co/usCSbZZQIH>
> [pic.twitter.com/L9ntWw0oNv](https://t.co/L9ntWw0oNv)
>
> -- Sergej Kotliar (@ziggamon) [March 31,
> 2018](https://twitter.com/ziggamon/status/980124381283266562?ref_src=twsrc%5Etfw)

Due to low usage of the fee efficiency checker over 2019 and us reaching our
goal to raise awareness we decided to overhaul the site and released a second
iteration in 2020.

[Read more about the 2020 version](/projects/transactionfee-
info-2020-version/)

Enable JavaScript to view comments. Comments are privacy friendly and self-
hosted with [isso](https://posativ.org/isso/).

All text and images in this work are licensed under a [Creative Commons
Attribution-ShareAlike 4.0 International
License](http://creativecommons.org/licenses/by-sa/4.0/) [![Creative Commons
License](https://i.creativecommons.org/l/by-
sa/4.0/80x15.png)](http://creativecommons.org/licenses/by-sa/4.0/)

#### Next

![Image for lnplays.com](/data/projects/lnplays-com/header.png)
[](/projects/lnplays-com/)

* * *

June 23, 2018

#### lnplays.com

Konstantin Nick ([@sputn1ck](https://twitter.com/sputn1ck)) and I build
lnplays.com for the Lighting Hackday in June 2018. You could play Pokémon via
the Lightning Network build. Pressing the buttons of the GameBoy to move the
player and to interact with the world would generate a lightning invoice.
Paying that invoice would send the pressed button to the game-backend and the
user could see the action over the live stream. The site not longer up, but
parts of it can still be seen on
[archive.org](https://web.archive.org/web/20180625193114/https://lnplays.com/).

[](/projects/lnplays-com/)

#### Previous

![Image for mempool.observer \(2017 version\)](/data/projects/mempool-
observer/2017-header-text.png) [](/projects/mempool-observer-2017-version/)

* * *

October 7, 2017

#### mempool.observer (2017 version)

The [mempool.observer](https://mempool.observer) website displays statistics
about my Bitcoin mempool. This covers the 2017 version which I iterated on in
2019.

[](/projects/mempool-observer-2017-version/)

[ ![logo stackexchange](/img/footer/stackexchange.svg)
](https://bitcoin.stackexchange.com/users/63817/0xb10c) [ ![logo
linkedin](/img/footer/linkedin.svg) ](https://linkedin.com/in/0xb10c) [ ![logo
mastodon](/img/footer/mastodon.svg) ](https://x0f.org/@0xb10c) [ ![logo
twitter](/img/footer/twitter.svg) ](https://twitter.com/0xb10c) [ ![logo
keybase](/img/footer/keybase.svg) ](https://keybase.io/b10c) [ ![logo
github](/img/footer/github.svg) ](https://github.com/0xb10c) [ ![logo
rss](/img/footer/rss.svg) ](https://b10c.me/feed.xml) [ ![logo
reddit](/img/footer/reddit.svg) ](https://reddit.com/u/0xb10c) [ ![logo
mail](/img/footer/gmail.svg) ](mailto:0xb10c+b10c-me@gmail.com)

