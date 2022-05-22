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

[Jul 21  
2019](https://blog.samouraiwallet.com/post/186458671552/a-holistic-approach-
to-coinjoin)

### [A holistic approach to
CoinJoin](https://blog.samouraiwallet.com/post/186458671552/a-holistic-
approach-to-coinjoin)

Earlier this week I was asked the differences between Wasabi and Whirlpool by
a user in our Whirlpool telegram channel. Of course, both implementations are
based on ZeroLink, and both implementations generally do the same thing. I
believe I gave a fair comparison between the two tools. [My original comments
can be found here.](https://href.li/?https://t.me/whirlpool_trollbox/7895)  

As I mentioned in my original comments, all CoinJoin transactions are affected
by merging inputs if proper precautions are not taken by the wallet software.
You have to think of "mixing" in a holistic way, it isn't a single process
that affords bulletproof privacy. Certainly anyone claiming they have solved
privacy concerns in Bitcoin is a liar.  

As we see it, there are two main aspects of "mixing", the actual CoinJoining
of UTXOs between participants, which both Samourai and Wasabi provide
implementations of, and secondly the actual spending of those UTXOs by the
user in a way that doesn't compromise their privacy, what we like to call
PostMix Strategy, which only Samourai provides currently.

In the CoinJoin protocol itself there are some key differences in the quality
of the mixes that each implementation creates. For example: In Samourai
Whirlpool, each mix is "theoretically perfect" \- What this means in practice
is each mix has the maximum amount of entropy possible for a transaction of
that composition - For a 5 input / 5 output Whirlpool transaction this means
there are 1496 possible interpretations and no possible deterministic links
between any of the inputs and outputs (See:[ KYCP.org
Example](https://href.li/?https://www.kycp.org/#/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2/in)
) . Additionally as we do not have a concept of "unmixed change" within the
mix you do not see the distinct "peeling chain" pattern on the blockchain.
Instead you see more of a fractal tree branch cloud emerge. (See:[ OXT
Whirlpool
Explorer](https://href.li/?https://oxt.me/static/whirlpool_explorer/index.html)
)

Alternatively in Wasabi's implementation of ZeroLink there is routinely 30-60%
of inputs issued from the same previous transaction, visually identifiable
deterministic links between inputs and outputs, and multiple outputs belonging
to a single participant in a given transaction, essentially mixing with
yourself. These factors in combination with the fact unmixed change is part of
the actual transaction as well as the static address used to collect the
coordinator fee would disqualify these are transactions as "Theoretically
Perfect".

When viewed in isolation these differences are not serious issues. The peeling
chain and unmixed change can be mitigated against by the user staying around
until their entire amount has been mixed for example, but when viewed
holistically and crucially with lack of a PostMix spending strategy these
architectural differences have serious consequences when common user behavior
intervenes.  

This was demonstrated by the trivial de-anonymization of Wasabi's own donation
to The Tor Project which carelessly merged an input in a transaction with a
100% deterministic links (See:
[KYCP](https://href.li/?https://www.kycp.org/#/ded9e1c3331dad9947d21cf72547e18deeea5cbe31e625a7b4848595d2c61ce2/in))
that revealed not only a Wirex account address, but also 38 fully mixed inputs
as their own (See:
[KYCP](https://href.li/?https://www.kycp.org/#/c580d1bfa85f6994be20f09f063141b0e976f7097a2d5fbca084911477646091:1/in))

 **My point is not to kick a competitor when they are down, my point is, if
this can happen to the experts who run Wasabi then this is absolutely
happening on a broader scale with less sophisticated users, and they likely
have no idea it is happening, let alone what steps they need to make to
prevent it.**

## How to prevent these issues  

A well thought out PostMix strategy in combination with a well defined
CoinJoin protocol is essential and must work in conjunction with each other.

We disagree strongly with the approach taken by Wasabi in response to these
raised concerns - which seem to be well intended but utterly naive - that
users should read long Medium articles and learn the finer details of proper
Coin Control techniques before spending.  

**This is a dangerous burden to put on users and an arrogant position to take
by the developers**. Samourai has instead developed multiple PostMix spending
tools that by default will apply advanced coin selection rules to help make
sure that the transactions you make after mixing are not leaking unwanted meta
data on the block chain as you spend and guaranteeing healthy amounts of
entropy as a cloak of plausible deniability.

We have spent years developing and fine tuning our coin selection algorithms,
testing them against tools we have developed and Open Sourced to score the
transactions. We have invited Wasabi to use these tools to help strengthen
their postmix spending proposition (See:[
1](https://href.li/?https://pbs.twimg.com/media/D_qrFHAXUAAOYnB.jpg)[
2)](https://href.li/?https://pbs.twimg.com/media/D_qrFHGX4AEjAEY.jpg) which
was unfortunately rebuffed.  

We have innovated on Peer2Peer CoinJoin transactions between you and a friend
designed to mix as you spend. And we have implemented PayJoin which is a type
of transaction that appears to be a normal "simple" transaction with 2
outputs, but is in fact another Mini CoinJoin where even the amount displayed
on the blockchain is misleading. This type of transaction is especially
subversive as it successfully tricks analysis platforms to incorrectly cluster
the inputs - creating a cloud of false positives.

I knew that it was likely that Wasabi would respond negatively to these
comments, but I would suggest to fix the underlying issues that are putting
users are risk instead of choosing to Doxx or launch personal attacks against
Samourai or our staff.  

  * [July 21, 2019](https://blog.samouraiwallet.com/post/186458671552/a-holistic-approach-to-coinjoin)

  1. [![](https://assets.tumblr.com/images/default_avatar/cone_closed_16.png)](https://darthmesquite.tumblr.com/ "Untitled ")[darthmesquite](https://darthmesquite.tumblr.com/ "Untitled") liked this 

  2. [![](https://64.media.tumblr.com/06144ecfa3533f1ca97f899e40d6a2a0/96bc706e4988d33b-f8/s16x16u_c1/35417a574aa6fd82ec0a220f660e0d4f30118799.pnj)](https://ehyowarrenzy.tumblr.com/ "Aloha ")[ehyowarrenzy](https://ehyowarrenzy.tumblr.com/ "Aloha") liked this 

  3. [![](https://64.media.tumblr.com/avatar_36fa1c18c89f_16.pnj)](https://blog.samouraiwallet.com/ "Samourai Wallet")[samouraiwallet](https://blog.samouraiwallet.com/ "Samourai Wallet") posted this 

[Older Post](https://blog.samouraiwallet.com/post/186208584657) [Newer
Post](https://blog.samouraiwallet.com/post/187001617347)
![](https://px.srvcs.tumblr.com/impixu?T=1653240643&J=eyJ0eXBlIjoidXJsIiwidXJsIjoiaHR0cDovL2Jsb2cuc2Ftb3VyYWl3YWxsZXQuY29tL3Bvc3QvMTg2NDU4NjcxNTUyL2EtaG9saXN0aWMtYXBwcm9hY2gtdG8tY29pbmpvaW4iLCJyZXF0eXBlIjowLCJyb3V0ZSI6Ii9wb3N0LzppZC86c3VtbWFyeSIsIm5vc2NyaXB0IjoxfQ==&U=CEMCMPAJNE&K=d3a2ea34e7f0111d2799e39a514cc68dc4a983d4acd03412fbe3cdaf08f709e3&R=)![](https://px.srvcs.tumblr.com/impixu?T=1653240643&J=eyJ0eXBlIjoicG9zdCIsInVybCI6Imh0dHA6Ly9ibG9nLnNhbW91cmFpd2FsbGV0LmNvbS9wb3N0LzE4NjQ1ODY3MTU1Mi9hLWhvbGlzdGljLWFwcHJvYWNoLXRvLWNvaW5qb2luIiwicmVxdHlwZSI6MCwicm91dGUiOiIvcG9zdC86aWQvOnN1bW1hcnkiLCJwb3N0cyI6W3sicG9zdGlkIjoiMTg2NDU4NjcxNTUyIiwiYmxvZ2lkIjoyMzUxNTI3NzMsInNvdXJjZSI6MzN9XSwibm9zY3JpcHQiOjF9&U=HHJFKELAKE&K=7f3742f24b38deee082bbb956a7a96c6f51c1bfae77b9011d4fb27b9ce57fc4b&R=)

