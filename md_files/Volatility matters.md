[![](https://substackcdn.com/image/fetch/w_96,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F83c90dd4-d6b5-4f1a-87dc-810f4816f885_256x256.png)](https://alfablok.substack.com)

# [AlfaBlok](https://alfablok.substack.com)

SubscribeSign in

Share this post

Volatility matters

alfablok.substack.com

Copy link

Twitter

Facebook

Email

# Volatility matters

### A more detailed look at how volatility is approached in the back-test

[![](https://substackcdn.com/image/fetch/w_90,h_90,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa7a5ff54-9882-49a7-abac-
ca2173498483_545x454.png)](https://substack.com/profile/8382123-alfablok)

|

[AlfaBlok](https://substack.com/profile/8382123-alfablok)

| Apr 29, 2020  
---  
  
[Comment](https://alfablok.substack.com/p/volatility-matters/comments)

[Share](javascript:void\(0\))  
  
Volatility plays a central role in how option traders price contracts.

Here’s how we dealt with volatility as a parameter during our back test.

### Approach one: historical volatility.

 **Example:** 30 day expiration cycles.

  * At expiry, I buy a new At the money put.

  * To price the put, I take the standard deviation of returns over the last 30 days, I annualize them, and I input that into a Black-Scholes engine.

  * On top of the BS price, I add an additional 20%, to make puts more expensive, and make the model more robust.

This is the resulting volatility:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F5ea151fc-2e92-4ebc-9a7a-ee8a097f925a_2406x1964.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F5ea151fc-2e92-4ebc-9a7a-ee8a097f925a_2406x1964.png)

 _Note: In the vertical axis, it’s 00s. eg. 1,5 = 150%, 2,0 = 200%, etc._

### Approach two: realized volatility.

 **Example:** 30 day expiration cycles.

  * At expiry, I buy a new At the money put.

  * To price the put, I take the standard deviation of returns over _the next 30 days_ (since I’m doing a back-test, I actually can look at the volatility ahead), and I input that into a Black-Scholes engine.

  * On top of the BS price, I add an additional 20%, to make puts more expensive, and make the model more robust.

  * This is consistent with Implied Vol being uniformly higher than Realized Vol in sampling from VIX on S&P500.

This is the resulting volatility:

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F3ef42d01-536e-446f-8dc7-8f5142a5d998_2417x1937.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F3ef42d01-536e-446f-8dc7-8f5142a5d998_2417x1937.png)

As you can see, the realized model shows the same volatility as the historical
model, just shifted 30 days. In the realized volatility model, volatility is
“perfectly” priced ahead of time, whereas historical vol method is just
delayed.

### Impact on results

Let’s look at the same period and parameters, run with both Historical and
Realized Volatility models.

 _ **Realized**_

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fdabe033e-0295-4bfc-a550-00dc330a0e95_2055x1033.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fdabe033e-0295-4bfc-a550-00dc330a0e95_2055x1033.png)

 _ **Historical**_

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd9cf3fb9-4f21-4b00-a100-bf2bec2ba525_2052x1031.png)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd9cf3fb9-4f21-4b00-a100-bf2bec2ba525_2052x1031.png)

Results are quite similar. This was unexepcted to us, but it seems to indicate
that price action is a much bigger driver for actual returns.

I know option pricing is a very heated space - interested in hearing people’s
thoughts about the approach, and possible alternatives/ideas, to produce the
most reliable results possible.

[CommentComment](https://alfablok.substack.com/p/volatility-matters/comments)

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
in?redirect=%2Fp%2Fvolatility-matters&for_pub=alfablok&change_user=false)

#### Check your email

For your security, we need to re-authenticate you.

Click the link we sent to , or [click here to sign
in](https://substack.com/sign-in?redirect=%2Fp%2Fvolatility-
matters&for_pub=alfablok&with_password=true).

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

