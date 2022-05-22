[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/5c9f620b7dd2&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Fluidity](https://miro.medium.com/fit/c/64/64/1*5pEAonqQtkWjGPLSudRP7g.png)](https://medium.com/fluidity?source=post_page
-----5c9f620b7dd2--------------------------------)

Published in

[Fluidity

](https://medium.com/fluidity?source=post_page-----
5c9f620b7dd2--------------------------------)

[![Adam
Link](https://miro.medium.com/fit/c/96/96/1*K56jViUgZKtMAJknTIJnJw.jpeg)](/@rhyeal?source=post_page
-----5c9f620b7dd2--------------------------------)

[Adam Link](/@rhyeal?source=post_page-----
5c9f620b7dd2--------------------------------)

Follow

Aug 21, 2019

·

4 min read

# The Dark Side of AWS Lambda

 _Earlier this week, I walked into the office and started checking our daily
logs. Everything looked fine except there were a few failed Lambda deploys to
development overnight. Time to dig in._

What came next was a realization of the dark side of using Lambdas heavily at
a company that also follows a strong CI/CD process.

Let’s back up a bit.

![](https://miro.medium.com/max/1400/1*BSxl_1vnIA402TPm-A9ohA.png)

## Rapid Development…

\--

14

\--

\--

14

## [More from Fluidity](/fluidity?source=post_page-----
5c9f620b7dd2--------------------------------)

Rebuilding Finance for a Frictionless World

[Read more from Fluidity](/fluidity?source=post_page-----
5c9f620b7dd2--------------------------------)

## Recommended from Medium

[[![Stride](https://miro.medium.com/fit/c/40/40/1*cDDalFSSmhCcKsfV5AwWfg.png)](/@Stride?source=post_internal_links
---------0----------------------------)

[Stride

](/@Stride?source=post_internal_links---------0----------------------------)

in

[HackerNoon.com

](https://medium.com/hackernoon?source=post_internal_links---------
0----------------------------)

## CI/CD Is Not A Progression

![](https://miro.medium.com/focal/112/112/50/50/1*tjvQ8XV65JcxIETD53CNDg.jpeg)](/hackernoon/ci-
cd-is-not-a-progression-86ebc896571b?source=post_internal_links---------
0----------------------------)

[[![Jared
Gray](https://miro.medium.com/fit/c/40/40/1*tzNiaDLelOdn52z8fSdiYw.jpeg)](/@jaredgray?source=post_internal_links
---------1----------------------------)

[Jared Gray

](/@jaredgray?source=post_internal_links---------
1----------------------------)

in

[Happy Monday

](https://medium.com/happymondayinc?source=post_internal_links---------
1----------------------------)

## The Essential Guide to a Post-Covid Developer Interview

![](https://miro.medium.com/focal/112/112/50/50/0*VWJLfXN-0Y7AcvhG)](/happymondayinc/the-
essential-guide-to-a-post-covid-developer-
interview-b661a16821de?source=post_internal_links---------
1----------------------------)

[[![James
Spinella](https://miro.medium.com/fit/c/40/40/1*obPSqXuBRHdM7Tbnknt40w.png)](/@jspi?source=post_internal_links
---------2----------------------------)

[James Spinella

](/@jspi?source=post_internal_links---------2----------------------------)

in

[Dev Genius

](https://medium.com/dev-genius?source=post_internal_links---------
2----------------------------)

## The three questions I ask when reviewing a pull request

![The Mona Lisa in Louvre,
France](https://miro.medium.com/focal/112/112/50/50/1*v4Mp4pN3h9TM5-nwueQeFw.jpeg)](/dev-
genius/the-three-questions-i-ask-when-reviewing-a-pull-
request-8791b142e6cd?source=post_internal_links---------
2----------------------------)

[[![Anna
Carey](https://miro.medium.com/fit/c/40/40/1*rtVk-q1j5EA6-PeIrQCspQ.png)](/@anna-
carey?source=post_internal_links---------3----------------------------)

[Anna Carey

](/@anna-carey?source=post_internal_links---------
3----------------------------)

in

[OneZero

](https://medium.com/one-zero?source=post_internal_links---------
3----------------------------)

## It’s Time to End Whiteboard Interviews for Software Engineers

![](https://miro.medium.com/focal/112/112/56/31/1*MnqlCVLSCHQZG6A9-V4fpA.jpeg)](/one-
zero/its-time-to-end-whiteboard-interviews-for-software-
engineers-8a805abcb3ad?source=post_internal_links---------
3----------------------------)

[[![Dirk
Hoekstra](https://miro.medium.com/fit/c/40/40/2*eccitutK6ewir4D44skh3g.jpeg)](/@dirk_hoekstra?source=post_internal_links
---------4----------------------------)

[Dirk Hoekstra

](/@dirk_hoekstra?source=post_internal_links---------
4----------------------------)

in

[Better Programming

](https://medium.com/better-programming?source=post_internal_links---------
4----------------------------)

## My PHP Application Is Getting Really Popular, Now What?

![](https://miro.medium.com/focal/112/112/50/50/1*c4jCok7lThHeEWQYfmYm6A.jpeg)](/better-
programming/my-php-application-is-getting-really-popular-now-
what-68160c42f90?source=post_internal_links---------
4----------------------------)

[[![Adam
Piel](https://miro.medium.com/fit/c/40/40/1*5-yRp2RLaaKpv8Y6Zhnmng.png)](/@AdamPiel?source=post_internal_links
---------5----------------------------)

[Adam Piel

](/@AdamPiel?source=post_internal_links---------5----------------------------)

in

[Built to Adapt

](https://medium.com/built-to-adapt?source=post_internal_links---------
5----------------------------)

## What Happens After the MVP?

![](https://miro.medium.com/focal/112/112/50/50/0*EHHKzCze4u-yxDxi.)](/built-
to-adapt/what-happens-after-the-mvp-eaa7de08e917?source=post_internal_links
---------5----------------------------)

[[![Suhadev
Venkatesh](https://miro.medium.com/fit/c/40/40/0*XEy2CnPLpGDxnk4R.jpg)](/@suhadevvenkatesh?source=post_internal_links
---------6----------------------------)

[Suhadev Venkatesh

](/@suhadevvenkatesh?source=post_internal_links---------
6----------------------------)

## Dapper — Google’s Secret Weapon

![](https://miro.medium.com/focal/112/112/50/50/1*pAY5mJ2syfphaOkV-
BSJxQ.jpeg)](/@suhadevvenkatesh/dapper-googles-secret-
weapon-56e43cd61653?source=post_internal_links---------
6----------------------------)

[[![Wu
Chunliang](https://miro.medium.com/fit/c/40/40/1*ax7sqMMxMs5EscZFQg5CLA.jpeg)](/@chunlwu?source=post_internal_links
---------7----------------------------)

[Wu Chunliang

](/@chunlwu?source=post_internal_links---------7----------------------------)

in

[The PayPal Technology Blog

](https://medium.com/paypal-tech?source=post_internal_links---------
7----------------------------)

## eXplainable Artificial Intelligence (XAI): Using AI to Minimize Risks and
Improve Customer…

![](https://miro.medium.com/focal/112/112/50/50/1*F8oCVdQdQEq9f8ui58pdHg.png)](/paypal-
tech/explainable-artificial-intelligence-xai-using-ai-to-minimize-risks-and-
improve-customer-fb2bde845cce?source=post_internal_links---------
7----------------------------)

[](/?source=post_page-----5c9f620b7dd2--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
5c9f620b7dd2--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
5c9f620b7dd2--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
5c9f620b7dd2--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
5c9f620b7dd2--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----5c9f620b7dd2--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----5c9f620b7dd2--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Ffluidity%2Fthe-
dark-side-of-aws-lambda-5c9f620b7dd2&source=post_page
--------------------------nav_reg-----------)

[![Adam
Link](https://miro.medium.com/fit/c/176/176/1*K56jViUgZKtMAJknTIJnJw.jpeg)](/@rhyeal)

[

## Adam Link

](/@rhyeal)

251 Followers

CISSP, CEH, CHFI. Passionate about cyber security and cloud infrastructure.
Avid fisherman and forager of Alaska's wilderness.

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fusers%2F6b07470296ea%2Flazily-enable-
writer-
subscription&operation=register&redirect=https%3A%2F%2Fmedium.com%2Ffluidity%2Fthe-
dark-side-of-aws-
lambda-5c9f620b7dd2&user=Adam+Link&userId=6b07470296ea&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Jason
Wood](https://miro.medium.com/fit/c/40/40/1*P_3Is3pS5r1lo09JTFANRw.jpeg)](/@cloudmusings?source=read_next_recirc
---------0---------------------3e09da53_8e0d_41d2_86fe_d46970e2d4da-------)

[Jason Wood

](/@cloudmusings?source=read_next_recirc---------0---------------------
3e09da53_8e0d_41d2_86fe_d46970e2d4da-------)

## Reuse CloudFormation with mappings & config

![](https://miro.medium.com/focal/112/112/50/50/1*Q6An8JYr8-nNx1WBppJEUg.jpeg)](/@cloudmusings/reuse-
cloudformation-with-mappings-config-697aa1e49d7d?source=read_next_recirc
---------0---------------------3e09da53_8e0d_41d2_86fe_d46970e2d4da-------)

[[![Jenil Sathwara](https://miro.medium.com/fit/c/40/40/0*BpKpRipesz-
leZBS)](/@jenilsathwara?source=read_next_recirc---------1---------------------
3e09da53_8e0d_41d2_86fe_d46970e2d4da-------)

[Jenil Sathwara

](/@jenilsathwara?source=read_next_recirc---------1---------------------
3e09da53_8e0d_41d2_86fe_d46970e2d4da-------)

in

[Coinmonks

](https://medium.com/coinmonks?source=read_next_recirc---------1
---------------------3e09da53_8e0d_41d2_86fe_d46970e2d4da-------)

## Blockchain Services On Aws

![](https://miro.medium.com/focal/112/112/50/50/0*pay1eVLE4plsHz1Y.png)](/coinmonks/blockchain-
services-on-aws-ddf8a92addbd?source=read_next_recirc---------1
---------------------3e09da53_8e0d_41d2_86fe_d46970e2d4da-------)

[[![Chloe
McAteer](https://miro.medium.com/fit/c/40/40/1*fXtgJg2ZOASs0engxTn1-g@2x.jpeg)](/@chloemcateer?source=read_next_recirc
---------2---------------------3e09da53_8e0d_41d2_86fe_d46970e2d4da-------)

[Chloe McAteer

](/@chloemcateer?source=read_next_recirc---------2---------------------
3e09da53_8e0d_41d2_86fe_d46970e2d4da-------)

## How to win cloud and influence people

![](https://miro.medium.com/focal/112/112/50/50/1*ATZg4QwacgoRTXD_2cJJsw.png)](/@chloemcateer/how-
to-win-cloud-and-influence-people-aa9ea9422668?source=read_next_recirc
---------2---------------------3e09da53_8e0d_41d2_86fe_d46970e2d4da-------)

[[![Varad Karpe](https://miro.medium.com/fit/c/40/40/0*WlNc-
FS5PA9ZkJ5h)](/@varad.karpe?source=read_next_recirc---------3
---------------------3e09da53_8e0d_41d2_86fe_d46970e2d4da-------)

[Varad Karpe

](/@varad.karpe?source=read_next_recirc---------3---------------------
3e09da53_8e0d_41d2_86fe_d46970e2d4da-------)

## Everything you need to know about AWS ECS on Fargate before you get started

![](https://miro.medium.com/focal/112/112/50/50/0*BMpI5slG4bZsKV8Y.png)](/@varad.karpe/everything-
you-need-to-know-about-aws-ecs-on-fargate-before-you-get-
started-a1e9599b6694?source=read_next_recirc---------3---------------------
3e09da53_8e0d_41d2_86fe_d46970e2d4da-------)

[Help

](https://help.medium.com/hc/en-us)

[Status

](https://medium.statuspage.io)

[Writers

](https://about.medium.com/creators/)

[Blog

](https://blog.medium.com)

[Careers

](/jobs-at-medium/work-at-medium-959d1a85284e)

[Privacy

](https://policy.medium.com/medium-privacy-policy-f03bf92035c9)

[Terms

](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f)

[About

](https://medium.com/about?autoplay=1)

[Knowable

](https://knowable.fyi)

