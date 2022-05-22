[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/6e99b21e0193&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Portis](https://miro.medium.com/fit/c/64/64/1*sjSyv6BBfH6HEcOo0Xr-7A.png)](https://medium.com/portis?source=post_page
-----6e99b21e0193--------------------------------)

Published in

[Portis

](https://medium.com/portis?source=post_page-----
6e99b21e0193--------------------------------)

[![portis](https://miro.medium.com/fit/c/96/96/1*nMh3K62zk5kXXR9gtGhLQQ.png)](/@portis?source=post_page
-----6e99b21e0193--------------------------------)

[portis](/@portis?source=post_page-----
6e99b21e0193--------------------------------)

Follow

Nov 12, 2019

·

3 min read

# Terminal.co supports Portis for instant DApp Logs & Analytics

## With just a few lines of code, begin collecting logs and analytics of your
DApp’s web3 interactions through Portis, by augmenting it with Terminal’s SDK

![](https://miro.medium.com/max/1400/1*Tz18n1AReRLLMtUbr0jR0A.jpeg)

Photo by [Chris
Liverani](https://unsplash.com/@chrisliverani?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
on
[Unsplash](https://unsplash.com/s/photos/data?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

Since its launch in September, [Terminal](https://terminal.co/) is well on its
way towards [making life easier for Ethereum
developers](https://twitter.com/austingriffith/status/1177398902405783553).

Terminal is a hub designed to better develop, test, and manage Ethereum
artifacts and infrastructure. The team’s mission — to empower the next million
blockchain developers by serving as the next-gen Github for Web3.

Although it is fair to say that development in the Ethereum ecosystem (and
blockchain as a whole) is accelerating at breakneck speeds, problems with the
developer experience are stalling the inevitable escape velocity we seek,
mainstream adoption.

# 👑 Data is King

One of the first things any developer building a regular ol’ web application
does is set up some sort of logging and analytics for their app, using tools
like [Sentry](https://www.sentry.io/) and [Amplitude](https://amplitude.com/).
So why aren’t most of us doing the same when building our web3 applications?

Well, because building such tools yourself is time-consuming, and hey, you’ve
got enough on your plate already. However, the value of tracking this
information is obvious, and that’s why such platforms are so popular in the
world of web2 applications.

## Now, thanks to Terminal’s new SDK, you can have the same power for all of
your DApp’s web3 interactions!

With Terminal’s new SDK, you can easily keep track of all web3 interactions
carried out in your DApp from their sleek dashboard. By wrapping the Portis
provider with the Terminal SDK, logs will get pushed to your Terminal Logging
Platform and look something like this:

![](https://miro.medium.com/max/1400/1*jCgV2tl1DMWGdhuBJROe8A.png)

Start having proper logging and debugging, with the ability to search, filter,
and analyze all of your logs. All logs surfaced for a specific project will be
aggregated and displayed in the analytics platform:

![](https://miro.medium.com/max/1400/1*jgipgHPQzdrCVKSPaLozaw.png)

# Super simple integration — just the way we like it

To begin surfacing logs for calls of your Portis-Powered DApp, simply wrap
your Portis web3 instance in a few easy steps:

First, install the Terminal SDK ([more
details](https://www.npmjs.com/package/@terminal-packages/sdk))

`npm i @terminal-packages/sdk`

Then, [sign up ](https://terminal.co/signup)for Terminal and [generate a
Terminal API key](https://docs.terminal.co/terminal-platform/create-an-api-
key).

Finally, wrap the Portis provider by importing the Terminal SDK package and
generate a web3 instance by including the Terminal account API Key, Source,
Terminal ProjectID & Provider.

 **apiKey** is where you paste your Terminal API Key.

 **Source** will be “PORTIS” (obviously 😎). After importing the TerminalSDK it
will show as a sourceType within the autocompletion. It can also be a string.

 **ProjectID** can be retrieved from your Terminal project settings.

 **customHttpProvider** is where you pass along the Portis provider.

    
    
    import Portis from '@portis/web3';  
    import {TerminalHttpProvider} from '@terminal-packages/sdk';const portis = new Portis('YOUR_DAPP_ID', 'mainnet');  
    const web3 = new Web3(  
        new TerminalHttpProvider({  
            apiKey: apiKey,  
            source: "PORTIS",  
            projectId: "TERMINAL_PROJECT_ID",  
            customHttpProvider: portis.provider  
        })  
    );

For more information about adding provider options check out the [Terminal SDK
Quickstart Guide](/logs-analytics/hexsdk/hexsdk-quickstart).

Once your Portis web3 instance is wrapped inside the TerminalSDK, all web3
interactions will be logged to your Terminal account.

## Congrats! You’ve just added analytics to your DApp with a few lines of
code.

More #BUIDL, more #SIMPL, just the way we like it.

Happy coding!

The Portis Team

Have any questions? Join the conversation on our
[Telegram](https://t.me/PortisHQ?source=post_page---------------------------)
and
[Twitter](https://twitter.com/portis_io?source=post_page---------------------------).
Ready to #BUIDL? Head on to our
[docs](http://docs.portis.io/?source=post_page---------------------------).  
Got any suggestions? [We 💙 feedback](https://portis.hellonext.co/)!

\--

\--

\--

## [More from Portis](/portis?source=post_page-----
6e99b21e0193--------------------------------)

Making blockchains simple for users

[Read more from Portis](/portis?source=post_page-----
6e99b21e0193--------------------------------)

[](/?source=post_page-----6e99b21e0193--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
6e99b21e0193--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
6e99b21e0193--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
6e99b21e0193--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
6e99b21e0193--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----6e99b21e0193--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----6e99b21e0193--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fportis%2Fterminal-
co-supports-portis-for-instant-dapp-logs-
analytics-6e99b21e0193&source=post_page--------------------------
nav_reg-----------)

[![portis](https://miro.medium.com/fit/c/176/176/1*nMh3K62zk5kXXR9gtGhLQQ.png)](/@portis)

[

## portis

](/@portis)

433 Followers

<https://portis.io>

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F4462dd2c963a&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fportis%2Fterminal-
co-supports-portis-for-instant-dapp-logs-
analytics-6e99b21e0193&newsletterV3=56bd0a809585&newsletterV3Id=4462dd2c963a&user=portis&userId=56bd0a809585&source=--------------------------subscribe_user-----------)

## More from Medium

[[![OMNUUM](https://miro.medium.com/fit/c/40/40/1*9pxqed8ExmdwaqyUynmgfA.png)](/@omnuum?source=read_next_recirc
---------0---------------------f417ea02_9faf_4048_a930_1b2b78d32396-------)

[OMNUUM

](/@omnuum?source=read_next_recirc---------0---------------------
f417ea02_9faf_4048_a930_1b2b78d32396-------)

in

[OMNUUM

](https://medium.com/omnuum?source=read_next_recirc---------0
---------------------f417ea02_9faf_4048_a930_1b2b78d32396-------)

## [OMNUUM] Build Your Own Universe!

![](https://miro.medium.com/focal/112/112/50/50/1*uicvDApO61W8I79pyQMLbA.png)](/omnuum/omnuum-
build-your-own-universe-1c503c153af3?source=read_next_recirc---------0
---------------------f417ea02_9faf_4048_a930_1b2b78d32396-------)

[[![WP Smart Contracts](https://miro.medium.com/fit/c/40/40/0*fJsWt5eSGbHN-
aHJ.jpg)](/@wpsmartcontracts?source=read_next_recirc---------1
---------------------f417ea02_9faf_4048_a930_1b2b78d32396-------)

[WP Smart Contracts

](/@wpsmartcontracts?source=read_next_recirc---------1---------------------
f417ea02_9faf_4048_a930_1b2b78d32396-------)

## Create multiple collections in a single Smart Contract

![](https://miro.medium.com/focal/112/112/50/50/1*LKTI-
Eq89Y33Yu4iUqACow.png)](/@wpsmartcontracts/create-multiple-collections-in-a-
single-smart-contract-40d7b138d333?source=read_next_recirc---------1
---------------------f417ea02_9faf_4048_a930_1b2b78d32396-------)

[[![Gil Givoni](https://miro.medium.com/fit/c/40/40/0*abCvHtd-
qMaYJ9jH)](/@gil.givoni?source=read_next_recirc---------2---------------------
f417ea02_9faf_4048_a930_1b2b78d32396-------)

[Gil Givoni

](/@gil.givoni?source=read_next_recirc---------2---------------------
f417ea02_9faf_4048_a930_1b2b78d32396-------)

in

[Overwolf Blog

](https://medium.com/overwolf?source=read_next_recirc---------2
---------------------f417ea02_9faf_4048_a930_1b2b78d32396-------)

## Update on CurseForge API

![](https://miro.medium.com/freeze/focal/112/112/50/50/1*wRK2aw2eLbyLxjpLCyjK2A.gif)](/overwolf/update-
on-curseforge-api-180468476253?source=read_next_recirc---------2
---------------------f417ea02_9faf_4048_a930_1b2b78d32396-------)

[[![Recruin | Blockchain & Tech Startup
Recruitment](https://miro.medium.com/fit/c/40/40/0*Q8nnWINieubKGhYA)](/@recruin?source=read_next_recirc
---------3---------------------f417ea02_9faf_4048_a930_1b2b78d32396-------)

[Recruin | Blockchain & Tech Startup Recruitment

](/@recruin?source=read_next_recirc---------3---------------------
f417ea02_9faf_4048_a930_1b2b78d32396-------)

## Searching for Solidity Developers on GitHub. Finding email addresses in 3
ways. Part 2

![](https://miro.medium.com/focal/112/112/50/50/1*izh3v7rkUtjEdpoL-
EIGVA.jpeg)](/@recruin/searching-for-solidity-developers-on-github-finding-
email-addresses-in-3-ways-part-2-19257d592080?source=read_next_recirc---------
3---------------------f417ea02_9faf_4048_a930_1b2b78d32396-------)

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

