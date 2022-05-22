###### [![Samourai
Wallet](https://64.media.tumblr.com/avatar_36fa1c18c89f_64.pnj) Samourai
Wallet](/)

* * *

* * *

* * *

x

  * [Archive](/archive)
  * [RSS](https://blog.samouraiwallet.com/rss)
  * [Simplify](http://simplifytheme.tumblr.com) version 1.22. Theme Designed & Developed by [](http://amitjakhu.com)Amit Jakhu. Powered by [Tumblr](http://tumblr.com).

[Mar 11  
2019](https://blog.samouraiwallet.com/post/183378923792/collaborative-
transactions-cahoots)

### [Collaborative Transactions -
"Cahoots"](https://blog.samouraiwallet.com/post/183378923792/collaborative-
transactions-cahoots)

![image](https://64.media.tumblr.com/169476ac38e6177af96c58e81ededdcb/tumblr_inline_po7415iHq71tu47rq_500.png)

>   _I started to investigate the idea of nested / embedded transactions.You
> will find in the following notes some notes that can serve as a basis for
> the future._
>
>  _ **LaurentMT** April 17, 2018  
> _

##  

##  **Building on the shoulders of giants**

The idea of nested / embedded transactions aren't new. The earliest mention we
can find dates to 2013 in [a message board post by Greg Maxwell
](https://href.li/?https://bitcointalk.org/index.php?topic=139581.0)where he
not only correctly describes the **Common Input Ownership Heuristic** that
blockchain analysis firms use to create their data sets and cluster addresses
- As Maxwell describes it, _"_ _A lot of people mistakenly assume that when a
transaction spends from multiple addresses all those addresses are owned by
the same party. "  _- __ but also describes a practical method of multiple
parties collaborating to create a transaction that breaks the heuristic above.  

In April 2017, using the above message board thread as inspiration, we began
work on a collaborative transaction framework, code name Cahoots. Cahoots will
initially feature two different transaction types that make use of the idea of
collaborating with other parties. The stated goal is to befuddle blockchain
observers by tainting the heuristics they rely on. Additionally, Cahoots is an
essential part of our post-mix strategy for our soon to be released Whirlpool
mobile mixing solution. **  
**

**  
**

## **STONEWALLx2**

STONEWALLx2 builds on our existing STONEWALL transaction. The existing
STONEWALL creates a transaction on the blockchain that **simulates** a
CoinJoin transaction in a way that is mathematically indistinguishable from
the real thing. A STONEWALLx2 makes use of a second party's UTXO set in
addition to your own to compose the transaction. The result is a high entropy
"mini CoinJoin" transaction when sending to any third party. STONEWALLx2 is a
great way to quickly mix on demand when sending to any third party by
enlisting the help of a privacy conscious friend.

  

##  **Stowaway**

Stowaway is a brand new transaction built on the Cahoots framework. Where both
versions of STONEWALL are designed to look like CoinJoin transaction, a
Stowaway is designed to blend in and look like a typical bitcoin transaction -
with two inputs and two outputs - at the same time as keeping the amount sent
when reviewing the transaction on the blockchain a secret. Unlike STONEWALLx2,
Stowaway transactions can only be sent to the same person you are
collaborating with. This makes Stowaway a great option for mixing when paying
your privacy conscious friend. Maybe send a tip his way for helping out with
your STONEWALLx2 transaction earlier ;)  

  

## **Using Cahoots today**

![image](https://64.media.tumblr.com/622739b3dc4a588e699fe78b63e8fd34/tumblr_inline_po7a6fJXf51tu47rq_500.png)

  

We're still building out the full UI for Cahoots, so it is only available
within Samourai Wallet as an "easter egg" for power users, or those who are
eager to help test the bleeding edge. Full instructions for using
collaborative Cahoots transactions with your privacy conscious friends on the
bitcoin mainnet can be reviewed **by following the links below** :  

[ **Making STONEWALLx2
Transactions**](https://href.li/?https://support.samourai.io/article/74-how-
to-create-a-stonewallx2-transaction)

[ **Making Stowaway
Transactions**](https://href.li/?https://support.samourai.io/article/73-creating-
a-stowaway-transaction)

  

##  **The Future**

The future is looking bright. Soon even the average user will be able to
easily  mix their coins on a large scale basis with Whirlpool or on a per
transaction basis with both Cahoots spend types described in this article.  

Additionally, we're not the only ones working on this type of technology.
JoinMarket which **can and should** be regarded as an OG in the bitcoin
privacy space have started work on a feature called "PayJoin" which is similar
to Stowaway as an attack on the fundamental heuristics blockchain snoops
employ. [We encourage you to checkout a demo of PayJoin put together by Adam
Gibson (Waxwing).](https://href.li/?https://joinmarket.me/blog/blog/payjoin-
basic-demo/)

Putting all this together and a real Bitcoin privacy strategy starts to
emerge. There isn't a magic silver bullet to solve all our problems, a super
weapon against the blockchain snoops doesn't exist. What does exist are
guerilla tactics by privacy extremists, where even the smallest minority - the
individual - can make a large impact. Every Cahoots transaction is the
equivalent of a drop of poison in the water supply of the enemy. With each
transaction the snoops and observers lose a fundamental aspect of their
analysis. The reliability of their data sets is diminished with each Cahoots
transaction, benefiting every participant on the network. The snoops have been
dealt a severe blow. They no longer know what they thought they knew.  

Every transaction matters. Join the fight.  

 **As always we appreciate your continued support of the project.** We are
available as always to answer any questions on
[support.samourai.io](https://t.umblr.com/redirect?z=https%3A%2F%2Fsupport.samourai.io&t=NzY3NzBkZTM5NjVkNjkwNDgwMDI5NDI5YzA5MDkxMTU5ZjlmNTkyYyxaWGt4VlNrSw%3D%3D&b=t%3AgssRereQbaKEWqYj4_q6Mw&p=https%3A%2F%2Fblog.samouraiwallet.com%2Fpost%2F182192289762%2Fstaggered-
ricochet-utxo-tagging-paynym-ux&m=1) or by email at
[support@samouraiwallet.com  
](https://t.umblr.com/redirect?z=mailto%3Asupport%40samouraiwallet.com&t=N2YxZjIwZDUxMDJmNjk5ZTNjZDFiMDhmNjIzZjg4NzU3MTk3MzBkYSxaWGt4VlNrSw%3D%3D&b=t%3AgssRereQbaKEWqYj4_q6Mw&p=https%3A%2F%2Fblog.samouraiwallet.com%2Fpost%2F182192289762%2Fstaggered-
ricochet-utxo-tagging-paynym-ux&m=1)

You can download Samourai Wallet from the [Google Play
Store](https://t.umblr.com/redirect?z=https%3A%2F%2Fplay.google.com%2Fstore%2Fapps%2Fdetails%3Fid%3Dcom.samourai.wallet&t=NjAwYjc1ZjEwOGI3ZjEyMWJlNzZjMTBlODQ2MjZhZjg4Yzg1NzJjZSxaWGt4VlNrSw%3D%3D&b=t%3AgssRereQbaKEWqYj4_q6Mw&p=https%3A%2F%2Fblog.samouraiwallet.com%2Fpost%2F182192289762%2Fstaggered-
ricochet-utxo-tagging-paynym-ux&m=1)  

  * [March 11, 2019](https://blog.samouraiwallet.com/post/183378923792/collaborative-transactions-cahoots)

[Older Post](https://blog.samouraiwallet.com/post/182192289762) [Newer
Post](https://blog.samouraiwallet.com/post/185312260292)
![](https://px.srvcs.tumblr.com/impixu?T=1653240193&J=eyJ0eXBlIjoidXJsIiwidXJsIjoiaHR0cDovL2Jsb2cuc2Ftb3VyYWl3YWxsZXQuY29tL3Bvc3QvMTgzMzc4OTIzNzkyL2NvbGxhYm9yYXRpdmUtdHJhbnNhY3Rpb25zLWNhaG9vdHMiLCJyZXF0eXBlIjowLCJyb3V0ZSI6Ii9wb3N0LzppZC86c3VtbWFyeSIsIm5vc2NyaXB0IjoxfQ==&U=ICGPLGLJII&K=f0d530f147896f39b67efdd9ee36fcf9c02a2e575674b3890e0c41de9981d8be&R=)![](https://px.srvcs.tumblr.com/impixu?T=1653240193&J=eyJ0eXBlIjoicG9zdCIsInVybCI6Imh0dHA6Ly9ibG9nLnNhbW91cmFpd2FsbGV0LmNvbS9wb3N0LzE4MzM3ODkyMzc5Mi9jb2xsYWJvcmF0aXZlLXRyYW5zYWN0aW9ucy1jYWhvb3RzIiwicmVxdHlwZSI6MCwicm91dGUiOiIvcG9zdC86aWQvOnN1bW1hcnkiLCJwb3N0cyI6W3sicG9zdGlkIjoiMTgzMzc4OTIzNzkyIiwiYmxvZ2lkIjoyMzUxNTI3NzMsInNvdXJjZSI6MzN9XSwibm9zY3JpcHQiOjF9&U=PPCEJJMCJN&K=5306185ee47fd11eb6bf07cfa34c435f9df020fbca65b7b46143a564a944926a&R=)

