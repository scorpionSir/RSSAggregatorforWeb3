[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/9d1e3e5742d8&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Compound](https://miro.medium.com/fit/c/64/64/1*MzcWuVj0jfuGCiUYeCAVWA.png)](https://medium.com/compound-
finance?source=post_page-----9d1e3e5742d8--------------------------------)

Published in

[Compound

](https://medium.com/compound-finance?source=post_page-----
9d1e3e5742d8--------------------------------)

[![Adam
Bavosa](https://miro.medium.com/fit/c/96/96/1*IhBdnwAtRmJwbnJ27s4BAA.jpeg)](/@adam.bavosa?source=post_page
-----9d1e3e5742d8--------------------------------)

[Adam Bavosa](/@adam.bavosa?source=post_page-----
9d1e3e5742d8--------------------------------)

Follow

Sep 2, 2020

·

3 min read

# Compound.js

A JavaScript SDK for Ethereum and the Compound Protocol

![Announcing Compound.js a JavaScript SDK for Ethereum and
Compound](https://miro.medium.com/max/1400/1*Z1WAN3VRPHjZnaW8aHGLlQ.png)

We’re excited to announce a new software development kit that we’ve been
working on. Enter **Compound.js** ; a JavaScript SDK for Ethereum and the
Compound Protocol. This tool streamlines the software development process for
building DApps that accelerate DeFi.

At the time of this announcement, the SDK is officially in beta. It is
available for all, open source, on [GitHub](https://github.com/compound-
finance/compound-js) and [NPM](https://www.npmjs.com/package/@compound-
finance/compound-js). Compound.js works in the web browser and Node.js. It has
just one dependency: the latest version of
[Ethers.js](https://github.com/ethers-io/ethers.js/).

Built with simplicity in mind, developers can write intuitive, one-line
methods to initialize JSON RPC requests that interact with the Compound
Protocol.

In addition to Compound methods, developers can make generic **Ethereum read
and write calls** to any smart contract. Lastly, REST API calls can be made to
the [Compound API](https://compound.finance/docs/api) that is hosted by
Compound Labs.

# Ethereum JSON RPC with Compound.js

Reading and writing from the blockchain can be done swiftly with Compound.js;
no need to initialize an object.

In the following examples, A JSON RPC provider or Web3 provider can be passed
as the `provider` attribute in the options object. When writing to the
blockchain, a private key or mnemonic can be passed in the options object as
well.

## Write to the Blockchain (eth_sendTransaction)

Write operations are initialized with **Compound.eth.trx**. The return value
is an Ethers.js transaction object. Here is an example for sending ETH in the
web browser.

## Read from the Blockchain (eth_call)

Reading from any smart contract on the blockchain can be done using
**Compound.eth.read**. Here is an example for reading the USDC balance in the
[Uniswap USDC-ETH
pair](https://uniswap.info/pair/0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc).

A contract ABI can also be passed to the options object. In that case, you
would then provide a string of the method name as the second parameter,
instead of the whole method definition.

# Compound Protocol Methods

Simple one-liners are available for major protocol methods like **supply** ,
**redeem** , **borrow** , **repayBorrow** , and more.

In examples like the following, a Compound object must be instantiated first.
The constructor can have `window.ethereum` passed in the browser, or a private
key/mnemonic alongside a JSON RPC provider if you’re using Node.js.

## Supplying to the Protocol

Here is an example for supplying Ether to the Compound Protocol using
Compound.js.

More examples of object **initialization** and deeper description of the
**transaction options** parameter are available in the [Compound.js GitHub
repository readme](https://github.com/compound-finance/compound-js).

## Governance and COMP Methods

The SDK has elegant methods for Compound governance functionality through the
COMP and Governor smart contracts.

Here is an example for fetching the amount of COMP token that has accrued for
an address (more on [COMP Distribution](/compound-finance/expanding-compound-
governance-ce13fcd4fe36) here).

Voting on a Compound governance proposal is as simple using the SDK’s
**castVote** method.

More governance related methods are defined in the [Compound.js
Documentation](https://compound-finance.github.io/compound-
js/docs/index.html).

## Getting Prices

Fetching prices from the Open Price Feed can be done with the **getPrice**
method.

The first parameter is the asset that you want the price of, and the second
parameter (optional) is the asset you want that price converted to. The
default output is USD with 6 decimal places.

This method supports all assets that are posted to the Open Price Feed, and
also cTokens.

# Compound API Methods

The [Compound REST API](https://compound.finance/docs/api) can be queried
using Compound.js. Each of the available services has their own method.

  * market
  * account
  * cToken
  * governance

Each of the request parameters defined in the documentation (linked above) can
be passed in the JavaScript object parameter. Here is an example for querying
the Market History Service.

# Roadmap and Contribution

[Compound.js](https://github.com/compound-finance/compound-js) is in **open
beta** and is available for free on
[NPM](https://www.npmjs.com/package/@compound-finance/compound-js). The plan
for next steps is to add more Compound Protocol related methods for ease of
development. Also, smarter logging of errors and results would greatly improve
the developer experience.

Remember that the Compound Protocol is decentralized and upgraded by the
community. As a result, this SDK will morph however the community sees fit!

A community contribution guide will be available in the future for anyone to
help improve the SDK.

If you have **questions** or comments, please join the [Compound
Discord](https://compound.finance/discord/) and send us a message in the
**#💻development** channel.

\--

\--

\--

## [More from Compound](/compound-finance?source=post_page-----
9d1e3e5742d8--------------------------------)

Compound is an algorithmic, autonomous interest rate protocol built for
developers, to unlock a universe of open financial applications.

[Read more from Compound](/compound-finance?source=post_page-----
9d1e3e5742d8--------------------------------)

## Recommended from Medium

[[![Said
BADAOUI](https://miro.medium.com/fit/c/40/40/1*Q7WTRqUW4PotqBS3hHc6wQ.png)](/@themeptation?source=post_internal_links
---------0----------------------------)

[Said BADAOUI

](/@themeptation?source=post_internal_links---------
0----------------------------)

## Deploy a NextJS application using GitLab CI/CD & Docker on DigitalOcean
Droplet Ubuntu 18.04

![](https://miro.medium.com/focal/112/112/50/50/1*yfNH1kJWODm1_W-
qffXmiw@2x.png)](/@themeptation/deploy-a-nextjs-application-using-gitlab-ci-
cd-docker-on-digitalocean-droplet-
ubuntu-18-04-d8163c64a893?source=post_internal_links---------
0----------------------------)

[[![Oren
Magid](https://miro.medium.com/fit/c/40/40/0*RWbWj1Hib4uQVXt3)](/@orenmagid?source=post_internal_links
---------1----------------------------)

[Oren Magid

](/@orenmagid?source=post_internal_links---------
1----------------------------)

## Thinking About Passing “By Value” and “By Reference” in JavaScript

](/@orenmagid/thinking-about-passing-by-value-and-by-reference-in-
javascript-457bf1554184?source=post_internal_links---------
1----------------------------)

[[![syd](https://miro.medium.com/fit/c/40/40/2*wkPELnarstXyU7nG1nRnMg.jpeg)](/@00110011?source=post_internal_links
---------2----------------------------)

[syd

](/@00110011?source=post_internal_links---------2----------------------------)

## Introducing TypeScript…

![](https://miro.medium.com/focal/112/112/50/50/1*yyId_Q4GfjXtjCCMnxtcpg.png)](/@00110011/introducing-
typescript-c3d34f64fc02?source=post_internal_links---------
2----------------------------)

[[![Rohit Kumar Thakur](https://miro.medium.com/fit/c/40/40/1*Ud-
Mz31o0jymGcyxb-h9fg.png)](/@ninza7?source=post_internal_links---------
3----------------------------)

[Rohit Kumar Thakur

](/@ninza7?source=post_internal_links---------3----------------------------)

in

[JavaScript in Plain English

](https://medium.com/javascript-in-plain-english?source=post_internal_links
---------3----------------------------)

## Text to Speech Conversion using React Native Expo (Android & IOS)

![](https://miro.medium.com/focal/112/112/50/50/0*G4SXJvUFxdUZ7ITN)](/javascript-
in-plain-english/text-to-speech-conversion-using-react-native-expo-android-
ios-f68f3e3ac5d9?source=post_internal_links---------
3----------------------------)

[[![Cloudmersive](https://miro.medium.com/fit/c/40/40/1*3v0ktJZ-a-
uV7KOqs9vF6Q.png)](/@cloudmersive?source=post_internal_links---------
4----------------------------)

[Cloudmersive

](/@cloudmersive?source=post_internal_links---------
4----------------------------)

## Set a Canonical URL in Node.JS

![](https://miro.medium.com/focal/112/112/50/50/1*kasNCKoFIHRWY2bhfyvFPw.jpeg)](/@cloudmersive/set-
a-canonical-url-in-node-js-848f5679410c?source=post_internal_links---------
4----------------------------)

[[![Fresh Frontend
Links](https://miro.medium.com/fit/c/40/40/0*gXNjh86g-yiSa8qJ.png)](/@frontender-
ua?source=post_internal_links---------5----------------------------)

[Fresh Frontend Links

](/@frontender-ua?source=post_internal_links---------
5----------------------------)

## Frontend Weekly Digest #201 (8–14 March 2021)

![](https://miro.medium.com/focal/112/112/50/50/1*yygmP4naFfE-
DWptz74R9Q.jpeg)](/@frontender-ua/frontend-weekly-
digest-201-8-14-march-2021-2ecd28407113?source=post_internal_links---------
5----------------------------)

[[![ScriptBees](https://miro.medium.com/fit/c/40/40/0*lczFh-3vBveD10j_.jpg)](/@scriptbees?source=post_internal_links
---------6----------------------------)

[ScriptBees

](/@scriptbees?source=post_internal_links---------
6----------------------------)

## How Angular & Ionic Powers Both Web and App Stores

![](https://miro.medium.com/focal/112/112/50/50/0*P_wyKMMD4tDnnbTN)](/@scriptbees/how-
angular-ionic-powers-both-web-and-app-
stores-d34191876f27?source=post_internal_links---------
6----------------------------)

[[![Cloudmersive](https://miro.medium.com/fit/c/40/40/1*3v0ktJZ-a-
uV7KOqs9vF6Q.png)](/@cloudmersive?source=post_internal_links---------
7----------------------------)

[Cloudmersive

](/@cloudmersive?source=post_internal_links---------
7----------------------------)

## How to Validate a Postal Code in Node.JS

![](https://miro.medium.com/focal/112/112/50/50/1*_Zx48ZEpfo_lUtEVAEnW7A.jpeg)](/@cloudmersive/how-
to-validate-a-postal-code-in-node-js-3ebdc97f7e0f?source=post_internal_links
---------7----------------------------)

[](/?source=post_page-----9d1e3e5742d8--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
9d1e3e5742d8--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
9d1e3e5742d8--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
9d1e3e5742d8--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
9d1e3e5742d8--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----9d1e3e5742d8--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----9d1e3e5742d8--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fcompound-
finance%2Fcompound-js-9d1e3e5742d8&source=post_page--------------------------
nav_reg-----------)

[![Adam
Bavosa](https://miro.medium.com/fit/c/176/176/1*IhBdnwAtRmJwbnJ27s4BAA.jpeg)](/@adam.bavosa)

[

## Adam Bavosa

](/@adam.bavosa)

964 Followers

DevRel @ [Compound.finance](http://Compound.finance)

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F320c371ec7d6&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fcompound-
finance%2Fcompound-
js-9d1e3e5742d8&newsletterV3=c323ca802342&newsletterV3Id=320c371ec7d6&user=Adam+Bavosa&userId=c323ca802342&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Julia Ah-Yionne](https://miro.medium.com/fit/c/40/40/1*JlqTCJTF3Tn4lrXV-
dn_hQ.png)](/@julia.ahyionne?source=read_next_recirc---------0
---------------------c95254e1_3158_44da_9fa3_f2899c8beea0-------)

[Julia Ah-Yionne

](/@julia.ahyionne?source=read_next_recirc---------0---------------------
c95254e1_3158_44da_9fa3_f2899c8beea0-------)

in

[UmamiWallet

](https://medium.com/umamiwallet?source=read_next_recirc---------0
---------------------c95254e1_3158_44da_9fa3_f2899c8beea0-------)

## Umami — Token management

![](https://miro.medium.com/focal/112/112/50/50/1*m2jMhI4LEg3eH7dMJ81eAg.png)](/umamiwallet/umami-
token-management-8aaa7a179bda?source=read_next_recirc---------0
---------------------c95254e1_3158_44da_9fa3_f2899c8beea0-------)

[[![Ragnar
Doge](https://miro.medium.com/fit/c/40/40/1*ifp5EU07oSWKWHz6x_VQYg.jpeg)](/@RagnarDoge?source=read_next_recirc
---------1---------------------c95254e1_3158_44da_9fa3_f2899c8beea0-------)

[Ragnar Doge

](/@RagnarDoge?source=read_next_recirc---------1---------------------
c95254e1_3158_44da_9fa3_f2899c8beea0-------)

## A design of PoE ( Proof of Excellence) token #1

](/@RagnarDoge/a-design-of-poe-proof-of-excellence-
token-1-fc18fd3413da?source=read_next_recirc---------1---------------------
c95254e1_3158_44da_9fa3_f2899c8beea0-------)

[[![Leona Hioki \(日置 玲於奈
\)](https://miro.medium.com/fit/c/40/40/1*XAdbjZ8xjWjWphJdSOaA-w.jpeg)](/@leonahioki?source=read_next_recirc
---------2---------------------c95254e1_3158_44da_9fa3_f2899c8beea0-------)

[Leona Hioki (日置 玲於奈 )

](/@leonahioki?source=read_next_recirc---------2---------------------
c95254e1_3158_44da_9fa3_f2899c8beea0-------)

## A zkRollup with no history transaction data (Intmax) report 1

![](https://miro.medium.com/focal/112/112/50/50/1*aKcWdhtBVvnWk-
TTvGFuxA.jpeg)](/@leonahioki/a-zkrollup-with-no-history-transaction-data-
intmax-の開発経過1-223a5e89b6e2?source=read_next_recirc---------2
---------------------c95254e1_3158_44da_9fa3_f2899c8beea0-------)

[[![Serenity
Shield](https://miro.medium.com/fit/c/40/40/1*Jdh1QWTjAzTyNwTXk3hmfg.png)](/@SerenityShield?source=read_next_recirc
---------3---------------------c95254e1_3158_44da_9fa3_f2899c8beea0-------)

[Serenity Shield

](/@SerenityShield?source=read_next_recirc---------3---------------------
c95254e1_3158_44da_9fa3_f2899c8beea0-------)

## Serenity Shield — Planning Ahead

![](https://miro.medium.com/focal/112/112/50/50/1*3QOrWce8BvuX6U7my3X6bg.jpeg)](/@SerenityShield/serenity-
shield-planning-ahead-b2ac4b6f969d?source=read_next_recirc---------3
---------------------c95254e1_3158_44da_9fa3_f2899c8beea0-------)

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

