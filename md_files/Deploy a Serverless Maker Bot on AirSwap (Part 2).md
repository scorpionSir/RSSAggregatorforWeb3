[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/682fb4d9cabd&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Fluidity](https://miro.medium.com/fit/c/64/64/1*5pEAonqQtkWjGPLSudRP7g.png)](https://medium.com/fluidity?source=post_page
-----682fb4d9cabd--------------------------------)

Published in

[Fluidity

](https://medium.com/fluidity?source=post_page-----
682fb4d9cabd--------------------------------)

[![Graham
Perich](https://miro.medium.com/fit/c/96/96/1*WVfsHH572KkyAGt6KuYoew.png)](/@grahamperich?source=post_page
-----682fb4d9cabd--------------------------------)

[Graham Perich](/@grahamperich?source=post_page-----
682fb4d9cabd--------------------------------)

Follow

Dec 2, 2019

·

5 min read

# Deploy a Serverless Maker Bot on AirSwap (Part 2)

 _In this two-part tutorial, learn how to quickly set up a maker for AirSwap
Instant using the new AirSwap Maker Kit and zero-config deployment with
Vercel._

AirSwap is a peer-to-peer token trading network. In [Part 1](/fluidity/deploy-
a-serverless-maker-bot-on-airswap-part-i-1f711ff4d379) of this tutorial we
built a simple maker bot, ran it locally, and queried it. Now, we’ll walk
through a few final steps to deploy our maker to the cloud and query it via
[AirSwap Instant](https://instant.development.airswap.io/).

![](https://miro.medium.com/max/1400/1*kQ7nR08QJNYObkb8yoNUxg.png)

# Deploying with Vercel

This is probably the easiest part of the tutorial, because Vercel makes
deployment so easy. Simply run the following command inside of `airswap-
vercel-example/`

    
    
    $ now

When the deployment finishes, you’ll see your maker address printed out. Keep
this handy, we’ll be using it shortly. It should be formatted as
`https://maker.<your vercel username>.vercel.app`

 _This address shouldn’t be longer than 32 characters including the https://
prefix. If it’s longer, consider changing the “name” of your maker in_`
_now.json_` _to something shorter, or using a shorter Vercel username._

# Approve tokens for trading

We need to approve the Swap contract to move tokens on our behalf in order for
it to work properly. This is a fundamental necessity of almost every kind of
decentralized exchange system on Ethereum. You’ll need to complete this step
for any token that you want your maker to trade, but you should only ever have
to perform it once per token. The AirSwap CLI includes a command to automate
token approvals, so let’s take care of that now.

On the command line, open the `.env` file that you created in the `airswap-
vercel-example` directory and copy the `ETHEREUM_ACCOUNT` value to import it
into the CLI.

    
    
    $ airswap account:import

Now we’re ready to run the token approval script.

    
    
    $ airswap token:approve

When prompted for the address of the token you want to approve, paste in the
Rinkeby DAI address. In Part 1, we got some test DAI from the Compound Faucet.
Paste the address into the prompt and hit enter/return on your keyboard.

    
    
    0x5592ec0cfb4dbc12d3ab100b257153436a1f0fea

Finally, double-check that everything is correct and type “yes”. Your
transaction will now be submitted to the Ethereum network, and you just have
to wait a minute or two for the miners to finalize it.

![](https://miro.medium.com/max/1400/1*CWRJWVXWDEhzGS1Os_Gxdw.png)

# Using the Indexer

At the end of Part 1, we queried our maker locally by pasting our
`localhost:3000` address into the prompt. We could query any maker directly
peer-to-peer in this fashion, but what if we don’t already know a maker’s
location in advance? How can we discover other traders on the network? That’s
where the [Indexer](https://docs.airswap.io/contracts/indexer) smart contract
comes in. An Indexer is a smart contract that aggregates trade intents. In our
example we are trading DAI/WETH, so we will publish an intent to the indexer
that signals this to the network. Then, other traders who are interested in
trading DAI/WETH can discover our address on the indexer and ask for a quote
or order. In fact, this is exactly the method that [AirSwap
Instant](https://instant.development.airswap.io/) employs to help traders
discover each other. AirSwap Maker Kit also has a script for setting Indexer
intents, which we’ll use below.

First, approve the indexer to stake AST

    
    
    $ airswap indexer:enable

![](https://miro.medium.com/max/1400/1*sV7Lkd6TdBA8N2kI6dIlYg.png)

Now, we can decide how much we want to stake. The more we stake, the higher up
on the list we’ll appear when traders query the indexer. You can acquire up to
5000 test AST from the [Rinkeby faucet](https://ast-faucet-
ui.development.airswap.io/). You can also run the `airswap indexer:get`
command to view the current state of the list.

    
    
    airswap indexer:set

![](https://miro.medium.com/max/1400/1*fEj-VAPDxGj9DIRf9-XYPg.png)

Replace “m.tutorial.now.sh” with the URL of your maker.

# Querying your maker on AirSwap Instant

Now that we’ve completed all the necessary steps, we should be able to
communicate with our maker on the web. To verify this, let’s head over to the
development version of AirSwap Instant running on the Rinkeby test net:
<https://instant.development.airswap.io>

Using MetaMask, switch to a different address than the one you’re using for
your maker. Change the base asset in the top right to “WETH” (we set our maker
to trade DAI for WETH).

![](https://miro.medium.com/max/1400/0*w-eps_BZqfsNMgtA)

Now, open the [Chrome Network
debugger](https://developers.google.com/web/tools/chrome-devtools/network) and
request an order for some DAI. You should see your maker appear in the network
activity, and one of the quotes in the “All Quotes” results should be from
your maker. Congratulations, your maker is now online 🎉

![](https://miro.medium.com/max/1400/0*gcxsrPubeuIN9bXE)

Now that you have a working end-to-end example, you can start to customize the
code and add your own logic. You should also check out your [Vercel
Dashboard](https://zeit.co/dashboard). It provides many helpful tools such as
log monitoring that will help you debug your deployed maker.

 _Note: The information contained in this blog post is solely for information
purposes and does not constitute financial or legal advice. Users agree that
their activity and conduct in connection with their use of AirSwap or any
tools described in this post, including any resultant transactions, will be in
compliance with all applicable laws, rules, regulations, requirements,
guidelines, policies, economic or financial sanctions._

# About AirSwap

AirSwap enables peer-to-peer trading on the Ethereum blockchain. Built on a
decentralized protocol, traders can add or remove liquidity through a suite of
trustless products that are easy to use and free. Our mission is to empower
the world with frictionless trade.

[Blog](https://medium.com/fluidity) | [Twitter](https://twitter.com/airswap) |
[Discord](https://chat.airswap.io) | [Developers](https://docs.airswap.io) |
[Makers](https://makers.airswap.io) |
[Reddit](https://www.reddit.com/r/airswap) |
[Facebook](https://www.facebook.com/airswapio/) |
[Linkedin](http://www.linkedin.com/company/airswap/) |
[Subscribe](https://upscri.be/b0fed8-2) |
[Support](https://support.airswap.io) | [Request a
Feature](https://airswap.canny.io) | [FAQ](https://support.airswap.io/faq) |
[Trade Now](https://instant.airswap.io)

\--

\--

\--

## [More from Fluidity](/fluidity?source=post_page-----
682fb4d9cabd--------------------------------)

Rebuilding Finance for a Frictionless World

[Read more from Fluidity](/fluidity?source=post_page-----
682fb4d9cabd--------------------------------)

## Recommended from Medium

[[![Alessandro
Alinone](https://miro.medium.com/fit/c/40/40/2*ta0hFFRtSXmlMypsEiLE1w.png)](/@Alinone?source=post_internal_links
---------0----------------------------)

[Alessandro Alinone

](/@Alinone?source=post_internal_links---------0----------------------------)

in

[Now4real

](https://medium.com/now4real?source=post_internal_links---------
0----------------------------)

## Single Sign-On and Custom Auth with Now4real

![](https://miro.medium.com/focal/112/112/50/50/0*IDPOPGzFTbD73d3Q)](/now4real/single-
sign-on-and-custom-auth-with-now4real-3bfd8f3266?source=post_internal_links
---------0----------------------------)

[[![Puneet
Sapra](https://miro.medium.com/fit/c/40/40/2*StPEzvbp2U2_CA3V_2loIQ.jpeg)](/@dm8typrogrammer?source=post_internal_links
---------1----------------------------)

[Puneet Sapra

](/@dm8typrogrammer?source=post_internal_links---------
1----------------------------)

in

[The Mighty Programmer

](https://medium.com/the-mighty-programmer?source=post_internal_links---------
1----------------------------)

## No more fear of pointers

![](https://miro.medium.com/focal/112/112/50/50/1*OB6t3wg6Ed6i7juPxq5aDg.png)](/the-
mighty-programmer/variable-and-pointer-fb637566bfd9?source=post_internal_links
---------1----------------------------)

[[![Chirag
Saxena](https://miro.medium.com/fit/c/40/40/0*B7sysvOsdmo0t-2E)](/@007chiragsaxena?source=post_internal_links
---------2----------------------------)

[Chirag Saxena

](/@007chiragsaxena?source=post_internal_links---------
2----------------------------)

in

[Towards Dev

](https://medium.com/towardsdev?source=post_internal_links---------
2----------------------------)

## Amazon Athena

![](https://miro.medium.com/focal/112/112/50/50/0*e1a5OKiJU-
gYtZ5K)](/towardsdev/amazon-athena-bd657c122207?source=post_internal_links
---------2----------------------------)

[[![Ali
Akhtar](https://miro.medium.com/fit/c/40/40/0*UJqG2W7r365v43pb.)](/@ali-
akhtar?source=post_internal_links---------3----------------------------)

[Ali Akhtar

](/@ali-akhtar?source=post_internal_links---------
3----------------------------)

## Realm Notifications (RealmSwift Part 2)

![](https://miro.medium.com/focal/112/112/50/50/0*QABc7Qb2ZYGzunoo.jpg)](/@ali-
akhtar/realm-notifications-realmswift-
part-2-60c66ab99ea9?source=post_internal_links---------
3----------------------------)

[[![Mayur
Parmar](https://miro.medium.com/fit/c/40/40/1*9r1Dn7oJx7dvb94Zq2aAvQ.png)](/@th3cyb3rc0p?source=post_internal_links
---------4----------------------------)

[Mayur Parmar

](/@th3cyb3rc0p?source=post_internal_links---------
4----------------------------)

in

[System Weakness

](https://medium.com/system-weakness?source=post_internal_links---------
4----------------------------)

## CVE-2020–29474 EgavilanMedia Address Book 1.0 Exploit — SQLi Auth Bypass

![](https://miro.medium.com/focal/112/112/50/50/1*RAa2br1kgsYhBZ2f1r6Byg.png)](/system-
weakness/cve-2020-29474-egavilanmedia-address-book-1-0-exploit-sqli-auth-
bypass-228cd4864262?source=post_internal_links---------
4----------------------------)

[[![Ali
Balouchi](https://miro.medium.com/fit/c/40/40/0*g3u5vghcE7SGZaBg)](/@alibalouchi.74?source=post_internal_links
---------5----------------------------)

[Ali Balouchi

](/@alibalouchi.74?source=post_internal_links---------
5----------------------------)

## Using local libraries in Google Colab

![](https://miro.medium.com/focal/112/112/50/50/1*jCrRrP5-H-IgdwYc-
rkMXw.png)](/@alibalouchi.74/using-local-libraries-in-google-
colab-553ef65fbe05?source=post_internal_links---------
5----------------------------)

[[![Jude
Harris](https://miro.medium.com/fit/c/40/40/1*gr5xuXucGhVuwRY0AJ7MLA.png)](/@jude-
blogs?source=post_internal_links---------6----------------------------)

[Jude Harris

](/@jude-blogs?source=post_internal_links---------
6----------------------------)

in

[CodeX

](https://medium.com/codex?source=post_internal_links---------
6----------------------------)

## How To Program

![](https://miro.medium.com/focal/112/112/50/50/0*FCAXnuVz3ckbZ8gB)](/codex/how-
to-program-bbfd87682e77?source=post_internal_links---------
6----------------------------)

[[![Kyler
Middleton](https://miro.medium.com/fit/c/40/40/1*PV75yJ4OnwMv0JIXrgfJWw.jpeg)](/@kymidd?source=post_internal_links
---------7----------------------------)

[Kyler Middleton

](/@kymidd?source=post_internal_links---------7----------------------------)

in

[FAUN Publication

](https://medium.com/faun?source=post_internal_links---------
7----------------------------)

## Let’s Do DevOps: Commit Regex Validation with GitHub Actions

![](https://miro.medium.com/focal/112/112/50/50/1*DMDkX3uydHdiaeZbIzrXfg.png)](/faun/lets-
do-devops-commit-regex-validation-with-github-
actions-d95261fa573e?source=post_internal_links---------
7----------------------------)

[](/?source=post_page-----682fb4d9cabd--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
682fb4d9cabd--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
682fb4d9cabd--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
682fb4d9cabd--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
682fb4d9cabd--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----682fb4d9cabd--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----682fb4d9cabd--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Ffluidity%2Fdeploy-
a-serverless-maker-bot-on-airswap-part-2-682fb4d9cabd&source=post_page
--------------------------nav_reg-----------)

[![Graham
Perich](https://miro.medium.com/fit/c/176/176/1*WVfsHH572KkyAGt6KuYoew.png)](/@grahamperich)

[

## Graham Perich

](/@grahamperich)

128 Followers

👨‍💻 Software Engineer - building the future of trade @AirSwap

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fusers%2F31c7466246f4%2Flazily-enable-
writer-
subscription&operation=register&redirect=https%3A%2F%2Fmedium.com%2Ffluidity%2Fdeploy-
a-serverless-maker-bot-on-airswap-
part-2-682fb4d9cabd&user=Graham+Perich&userId=31c7466246f4&source=--------------------------subscribe_user-----------)

## More from Medium

[[![patharanor](https://miro.medium.com/fit/c/40/40/1*lYLafMRX5TAd0ouaSz9-yA.jpeg)](/@patharanor?source=read_next_recirc
---------0---------------------a005b2d1_80e1_4568_99ba_36a5e29ab22d-------)

[patharanor

](/@patharanor?source=read_next_recirc---------0---------------------
a005b2d1_80e1_4568_99ba_36a5e29ab22d-------)

## Page Refresh issue in NextJS with S3 + CloudFront

](/@patharanor/page-refresh-issue-in-nextjs-
with-s3-cloudfront-e2cf2639bdb0?source=read_next_recirc---------0
---------------------a005b2d1_80e1_4568_99ba_36a5e29ab22d-------)

[[![Jan
Halama](https://miro.medium.com/fit/c/40/40/1*d6LWNlD35WNK5qd8itp3mg.jpeg)](/@jan_halama?source=read_next_recirc
---------1---------------------a005b2d1_80e1_4568_99ba_36a5e29ab22d-------)

[Jan Halama

](/@jan_halama?source=read_next_recirc---------1---------------------
a005b2d1_80e1_4568_99ba_36a5e29ab22d-------)

in

[Superface

](https://medium.com/superface?source=read_next_recirc---------1
---------------------a005b2d1_80e1_4568_99ba_36a5e29ab22d-------)

## Lessons learned integrating AppSignal APM with NestJS

![](https://miro.medium.com/focal/112/112/50/50/0*yvE2Zi_p26a7E_QU.jpg)](/superface/lessons-
learned-integrating-appsignal-apm-with-
nestjs-d0ebf391949c?source=read_next_recirc---------1---------------------
a005b2d1_80e1_4568_99ba_36a5e29ab22d-------)

[[![Randika
Swaris](https://miro.medium.com/fit/c/40/40/0*nS2mO7Yu1ikK8drd)](/@randika07?source=read_next_recirc
---------2---------------------a005b2d1_80e1_4568_99ba_36a5e29ab22d-------)

[Randika Swaris

](/@randika07?source=read_next_recirc---------2---------------------
a005b2d1_80e1_4568_99ba_36a5e29ab22d-------)

## How to use a Cloudflare Domain with a Cloudfront distribution

![](https://miro.medium.com/focal/112/112/50/50/1*741LcZxMyIbCLKz85HBo3A.png)](/@randika07/how-
to-use-a-cloudflare-domain-with-a-cloudfront-
distribution-d79c377888f7?source=read_next_recirc---------2
---------------------a005b2d1_80e1_4568_99ba_36a5e29ab22d-------)

[[![Nader](https://miro.medium.com/fit/c/40/40/1*Nz_JU0Ek2XVmcgggW7TGpg.jpeg)](/@nader-
almogazy?source=read_next_recirc---------3---------------------
a005b2d1_80e1_4568_99ba_36a5e29ab22d-------)

[Nader

](/@nader-almogazy?source=read_next_recirc---------3---------------------
a005b2d1_80e1_4568_99ba_36a5e29ab22d-------)

in

[Qache

](https://medium.com/qache?source=read_next_recirc---------3
---------------------a005b2d1_80e1_4568_99ba_36a5e29ab22d-------)

## Qache — Your New Server-Side Caching Solution

![](https://miro.medium.com/focal/112/112/50/50/1*iobKqp5QRVeTcQSvAuI3Jg.png)](/qache/qache-
your-new-server-side-caching-solution-6651b0563bc8?source=read_next_recirc
---------3---------------------a005b2d1_80e1_4568_99ba_36a5e29ab22d-------)

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

