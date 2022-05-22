[![](https://substackcdn.com/image/fetch/w_96,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F83c90dd4-d6b5-4f1a-87dc-810f4816f885_256x256.png)](https://alfablok.substack.com)

# [AlfaBlok](https://alfablok.substack.com)

SubscribeSign in

Share this post

Back-testing details - why does the system diverge?

alfablok.substack.com

Copy link

Twitter

Facebook

Email

# Back-testing details - why does the system diverge?

### A closer look at the back-testing engine and its results.

[![](https://substackcdn.com/image/fetch/w_90,h_90,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa7a5ff54-9882-49a7-abac-
ca2173498483_545x454.png)](https://substack.com/profile/8382123-alfablok)

|

[AlfaBlok](https://substack.com/profile/8382123-alfablok)

| Apr 18, 2020  
---  
  
[Comment](https://alfablok.substack.com/p/back-testing-details-why-does-
the/comments)

[Share](javascript:void\(0\))  
  
### System testing

This is the process applied:

  1. I buy protection on 1 ETH. With left-overs after purchase, I buy ETH.

  2. At expiration: if contract has intrinsic value, I collect it, and buy ETH with all proceeds.

  3. Day after expiration: Open new put contracts for the new total amount of ETH held. I pay for it with my own ETH held.

  4. Repeat 2 and 3 at every expiration.I’m very interested if anyone has feedback on the testing systyem. To me it’s important that the correct figures are shown:

Let’s look at the system over a short time period.

 **Flat pricing scenario**

 _P &L defined as_: (value of current position / value at start of investment)
-1 .

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F18ce3dfe-9ada-46e2-b24f-28daabd5207f_1024x647.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F18ce3dfe-9ada-46e2-b24f-28daabd5207f_1024x647.png)

As expected, hedging underperforms by 2% a week.

 **Increasing price:**

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd01be7ca-23f2-498c-b00f-51b90fd1d3cb_1044x693.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd01be7ca-23f2-498c-b00f-51b90fd1d3cb_1044x693.png)

If prices increase continuously, HODL outperforms hedging.

 **Decreasing price:**

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F9c1e1eeb-09e8-4182-b401-13c831e6ae06_705x535.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F9c1e1eeb-09e8-4182-b401-13c831e6ae06_705x535.png)

In this example where price went down for three weeks straight, hedging only
loses the fees weekly. Crucially, during this period, it’s buying ETH all the
while.

Let’s look at same graph, but qty held, instead of USD value.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F0ef43c72-00bd-4768-84fb-b9b53972cf69_705x535.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F0ef43c72-00bd-4768-84fb-b9b53972cf69_705x535.png)

As you can see, as prices go down, not only am I keeping my P&L flat-ish, I am
also increasing my ETH holdings!

### Extreme example

Let’s illustrate a 70% drop in a week:

Price starts at 10, drops to 3, goes back up to 10:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F18ec2e0a-bdd1-4b8c-9979-67ab4ecc52e3_744x1126.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F18ec2e0a-bdd1-4b8c-9979-67ab4ecc52e3_744x1126.png)

This is a key observation: Price went 10 to 3, then 3 to 10. At the end of the
process, hodling is flat 0% in (still at 10), whereas the P&L for hedging is
at 215%!!! UP.

Why?

At expiry, I collected $7 in intrinsic value (the loss in value), and used
these $7 to buy ETH, when ETH was specially cheap ($3). So I get 2,33 eth for
my $7. Those are in addition to the 0,98 I was holding, for a total 3.2 ETH.
All the while, I have only 1 ETH when I hold.

When prices goes back from 3 to 10, hodling gets a 3.3X boost on 1 ETH, and
goes back to $10 holdings, P&L=0%. I started with $10, I still have $10.

Hedging gets the same 3.3X boost but on 3.2ETH position, so ends up at 32$
holdings. P&L=215% gain on my $10 initial investment.

### Main idea

The reason I highlight this is because this is a key pattern: when price comes
back up after a down turn, hedging absolutely outstrips hodling because of the
higher amount of ETH held.

You have leveraged gains on the way up. You have 2% cost on the way down. And
the system is going up and down all the time. The more volatile it is, the
more it creates unbalance in favor of hedging.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe0df4ed8-d750-4595-baa0-41069b5ef8be_1545x931.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe0df4ed8-d750-4595-baa0-41069b5ef8be_1545x931.png)

When the strategy re-loads weekly instead of monthly, the results are even
more exaggerated. In this particular run from August 2015 to April 2020,
Hedging ended up holding 1200 ETH, vs 1 ETH in the HODL strategy. Also please
note that during black-thursday, which saw a 50% decrease, it literally
doubled its ETH exposure, in a single cycle.

Why? Again, price drops 50%, I collect 50% in intrinsic value, I buy ETH with
it, which is at 50% price, and so I double my stake in a single step.

If the system is indeed exponential, then the higher the refresh cycle, the
more chances of catching drops, and load up on ETH faster.

### Questions/Research:

>Ideas for errors/bugs in the buying/mechanic of the model engine?

>Is there any DeFi tool that allows you to implement a simple strategy like
the one presented here, in a hands-off way? ie. I post ETH to an address, and
then the smart-contract buys options from Hegic as per strategy heuristic.
Want to work on one? DM.

>Could an AMM be built, that was bonded to a curve, that created an option
price to one party, and yield for the other, and find a price in the market?
Like uniswap intrinsically producing prices by the size and direction of the
orders from its users.  

[CommentComment](https://alfablok.substack.com/p/back-testing-details-why-
does-the/comments)

[ShareShare](javascript:void\(0\))

![](https://substackcdn.com/image/fetch/w_66,h_66,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Favatars%2Flogged-
out.png)

## Create your profile

Your nameYour bio Subscribe to the newsletter

0 subscriptions will be displayed on your profile (edit)

Skip for now

Save & Post Comment

## Only paid subscribers can comment on this post

[Already a paid subscriber? **Sign in**](https://substack.com/sign-
in?redirect=%2Fp%2Fback-testing-details-why-does-
the&for_pub=alfablok&change_user=false)

#### Check your email

For your security, we need to re-authenticate you.

Click the link we sent to , or [click here to sign
in](https://substack.com/sign-in?redirect=%2Fp%2Fback-testing-details-why-
does-the&for_pub=alfablok&with_password=true).

TopNewCommunity[](javascript:void\(0\))

No posts

# Ready for more?

 **Subscribe**

© 2022 AlfaBlok

[Privacy](https://alfablok.substack.com/privacy) ∙ [Terms](/tos) ∙ [Collection
notice](https://substack.com/ccpa#personal-data-collected)

[ Publish on
Substack](https://substack.com/signup?utm_source=substack&utm_medium=web&utm_content=footer)[
Get the app](https://substack.com/app/app-store-redirect?utm_campaign=app-
marketing&utm_content=web-footer-button)

[Substack](https://substack.com) is the home for great writing

This site requires JavaScript to run correctly. Please [turn on
JavaScript](https://enable-javascript.com/) or unblock scripts

