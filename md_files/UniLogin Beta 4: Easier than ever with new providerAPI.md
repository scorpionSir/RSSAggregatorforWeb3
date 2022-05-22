[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/e55442c466d&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![UniLogin](https://miro.medium.com/fit/c/64/64/1*pbXgdMyIerXmHIJzLcj0Tg.png)](https://medium.com/universal-
ethereum?source=post_page-----e55442c466d--------------------------------)

Published in

[UniLogin

](https://medium.com/universal-ethereum?source=post_page-----
e55442c466d--------------------------------)

[![Marek
Kirejczyk](https://miro.medium.com/fit/c/96/96/0*QVEwR2ZHvUmeVXCv.png)](/@marekkirejczyk?source=post_page
-----e55442c466d--------------------------------)

[Marek Kirejczyk](/@marekkirejczyk?source=post_page-----
e55442c466d--------------------------------)

Follow

Feb 14, 2020

·

3 min read

# UniLogin Beta 4: Easier than ever with new providerAPI

 _Note: We recently changed the name from Universal Login to Unilogin (link to
the announcement_[ _here_](/universal-ethereum/universal-login-is-now-
unilogin-eb4683efadfc) _)._

We are happy to announce Beta 4 with a new Web3 provider API.

# Integrating Web3 provider API

A new API is straightforward to integrate; you can do it in 3 easy steps:

  *  **Install npm:**

    
    
     yarn add @universal-login/provider

  *  **Import UniLogin**

    
    
     import UniLoginProvider from '@universal-login/provider';

  *  **Configure existing web3:**

    
    
     web3.setProvider(  
      UniLoginProvider.createPicker(web3.currentProvider)  
    );

That’s it. Done!

#  **Wonders of UniLogin**

That is all you need to do to unleash all the wonders of UniLogin. When a user
wants to interact with Ethereum for the first time, the dialog to pick
UniLogin or MetaMask appears.

![](https://miro.medium.com/max/1400/1*sWw6ONmAK_qj12w7eDrp4A.png)

If the user picks MetaMask, the application works like it always did. If on
the other hand, users pick UniLogin, the application guides her step by step
into creating the account, including on-ramping.

![](https://miro.medium.com/max/1400/1*QLR_b3Og9Kooy4M53Rv2Rg.png)

If a user wants to make a transaction or interact with the blockchain, you
will get a dialog that allows you to confirm and customize gas options.

![](https://miro.medium.com/max/1400/1*5-f3bTnTlmYcF8-UyVVfTQ.png)

On top of that, when the transaction is being mined a dialog is displayed, so
that you don’t have to implement your own.

We implemented a small in-app wallet inside your application so that users
don’t have to install anything or leave your application to have full control
over his account.

# Button to trigger account management

You can add a UniLogin button. It allows the user to manage his account on
demand. Adding the button is just one line in HTML:

    
    
    <button id="unilogin-button" />

![](https://miro.medium.com/max/1400/1*fndKhP71SzXdDcMiKb0v0Q.png)

# Summary

  * With UniLogin, using Ethereum dapps is easier than ever, with the user guided step by step without ever leaving your application.
  * DApp development is faster than ever, as you can save time not having to build onboarding and top-up.

# What is next?

This is last the last beta. We are now focusing on stability and minor
features and getting the first RC1 out later this month and onward to a first
stable version in March!

# Follow us!

To make sure you don’t miss the next posts in the series, follow us
[Medium](https://medium.com/universal-ethereum) and
[Twitter](https://twitter.com/unilogin).

# Pilot program

Still not signed-up for our Beta program? Fix it!

[Join our Pilot program](http://tiny.cc/unilogin) 👮🏽 🛩

\--

1

\--

\--

1

## [More from UniLogin](/universal-ethereum?source=post_page-----
e55442c466d--------------------------------)

The best user onboarding solution for Ethereum dapps.

[Read more from UniLogin](/universal-ethereum?source=post_page-----
e55442c466d--------------------------------)

## Recommended from Medium

[[![READ/DOWNLOAD#\) Coding For Dummies \(For Dummies
\(C](https://miro.medium.com/fit/c/40/40/1*dmbNkD5D-u45r44go_cf0g.png)](/@sierra_95372?source=post_internal_links
---------0----------------------------)

[READ/DOWNLOAD#) Coding For Dummies (For Dummies (C

](/@sierra_95372?source=post_internal_links---------
0----------------------------)

## READ/DOWNLOAD#) Coding For Dummies (For Dummies (C

![](https://miro.medium.com/focal/112/112/50/50/0*GUzsQJQiuZgmGbnT.jpg)](/@sierra_95372/read-
download-coding-for-dummies-for-
dummies-c-7e6bf0b75bb1?source=post_internal_links---------
0----------------------------)

[[![Kumar
Shubham](https://miro.medium.com/fit/c/40/40/1*BeA11gEDnnu-c9IJNZvwZw.jpeg)](/@shubhamstudent5?source=post_internal_links
---------1----------------------------)

[Kumar Shubham

](/@shubhamstudent5?source=post_internal_links---------
1----------------------------)

in

[Towards Data Science

](https://medium.com/towards-data-science?source=post_internal_links---------
1----------------------------)

## Build a Job Search Portal with Django — Users App (Part 2)

![](https://miro.medium.com/focal/112/112/50/50/0*ZuoezoZ6w2gzfI7w)](/towards-
data-science/build-a-job-search-portal-with-django-users-app-
part-2-c98c5b41c8a2?source=post_internal_links---------
1----------------------------)

[[![Andra
Morutan](https://miro.medium.com/fit/c/40/40/2*XzNuI6KEpDZa-7j7pgiJ2w.jpeg)](/@andramorutan?source=post_internal_links
---------2----------------------------)

[Andra Morutan

](/@andramorutan?source=post_internal_links---------
2----------------------------)

## AEM integration with webp

![](https://miro.medium.com/focal/112/112/50/50/1*AnJKH3yVqQMpW_-
oNR6dBw.png)](/@andramorutan/aem-integration-with-
webp-78a1dac8c298?source=post_internal_links---------
2----------------------------)

[[![Niemvuilaptrinh](https://miro.medium.com/fit/c/40/40/1*UHnWofSJ4ql2ktsu7v59rw.png)](/@niemvuilaptrinh?source=post_internal_links
---------3----------------------------)

[Niemvuilaptrinh

](/@niemvuilaptrinh?source=post_internal_links---------
3----------------------------)

## Best CDN Providers for Website

![](https://miro.medium.com/focal/112/112/50/50/0*HnKSbVuZSBdjMFy4.png)](/@niemvuilaptrinh/best-
cdn-providers-for-website-b0d1b65e986c?source=post_internal_links---------
3----------------------------)

[[![Gagan
Dawar](https://miro.medium.com/fit/c/40/40/2*YNdwiiKztirX7MyzRKDJOQ.jpeg)](/@gagan.dawar?source=post_internal_links
---------4----------------------------)

[Gagan Dawar

](/@gagan.dawar?source=post_internal_links---------
4----------------------------)

## The Art of killing Agile Transformation

![](https://miro.medium.com/focal/112/112/50/50/1*b3etyERKxymZmU5tCUL1Tw.jpeg)](/@gagan.dawar/the-
art-of-killing-agile-transformation-64404f3f58ed?source=post_internal_links
---------4----------------------------)

[[![Development Seed](https://miro.medium.com/fit/c/40/40/1*L1SvC82SpZHyMlGQ-
EZhqA.png)](/@developmentseed?source=post_internal_links---------
5----------------------------)

[Development Seed

](/@developmentseed?source=post_internal_links---------
5----------------------------)

in

[Development Seed

](https://medium.com/devseed?source=post_internal_links---------
5----------------------------)

## Introducing Geolambda

![](https://miro.medium.com/focal/112/112/50/50/0*rJwNq6zZV2xeeozd.jpg)](/devseed/introducing-
geolambda-a571c1956d0a?source=post_internal_links---------
5----------------------------)

[[![Troy
Ingram](https://miro.medium.com/fit/c/40/40/1*Y-FBsRVQWWkTG3gvp7Mkwg.png)](/@troy-
ingram?source=post_internal_links---------6----------------------------)

[Troy Ingram

](/@troy-ingram?source=post_internal_links---------
6----------------------------)

in

[Nerd For Tech

](https://medium.com/nerd-for-tech?source=post_internal_links---------
6----------------------------)

## EBS Snapshot Management Using AWS Lambda and CloudWatch

![](https://miro.medium.com/focal/112/112/50/50/1*t1WzE8U3WSr8fFCe89V-hg.png)](/nerd-
for-tech/ebs-snapshot-management-using-aws-lambda-and-
cloudwatch-d961fdbe3772?source=post_internal_links---------
6----------------------------)

[[![Sergio
Pietri](https://miro.medium.com/fit/c/40/40/2*XNF8U6DhE2J1nr6dLXppAA.jpeg)](/@SergioPietri?source=post_internal_links
---------7----------------------------)

[Sergio Pietri

](/@SergioPietri?source=post_internal_links---------
7----------------------------)

## Static and Shared libraries in C

![](https://miro.medium.com/focal/112/112/50/50/1*H4zCeuFMabhJfegvAw6UGg.jpeg)](/@SergioPietri/static-
and-shared-libraries-in-c-2d7ba7d0a66a?source=post_internal_links---------
7----------------------------)

[](/?source=post_page-----e55442c466d--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
e55442c466d--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
e55442c466d--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
e55442c466d--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
e55442c466d--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----e55442c466d--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----e55442c466d--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Funiversal-
ethereum%2Funilogin-beta-4-easier-than-ever-with-new-
providerapi-e55442c466d&source=post_page--------------------------
nav_reg-----------)

[![Marek
Kirejczyk](https://miro.medium.com/fit/c/176/176/0*QVEwR2ZHvUmeVXCv.png)](/@marekkirejczyk)

[

## Marek Kirejczyk

](/@marekkirejczyk)

1.94K Followers

Ethereum blockchain Engineer. Ethworks, Universal Login.

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F6e6d213135fd&operation=register&redirect=https%3A%2F%2Fmedium.com%2Funiversal-
ethereum%2Funilogin-beta-4-easier-than-ever-with-new-
providerapi-e55442c466d&newsletterV3=1ad34b4ecc2e&newsletterV3Id=6e6d213135fd&user=Marek+Kirejczyk&userId=1ad34b4ecc2e&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Apurba Pokharel](https://miro.medium.com/fit/c/40/40/1*-PAk4rwuiC0I_-
faurRlqw.png)](/@apurbapokharel?source=read_next_recirc---------0
---------------------143bb70c_ed38_44f1_b3b6_4484e803a652-------)

[Apurba Pokharel

](/@apurbapokharel?source=read_next_recirc---------0---------------------
143bb70c_ed38_44f1_b3b6_4484e803a652-------)

## Modeling blockchains as a Deterministic Finite Automata

![](https://miro.medium.com/focal/112/112/50/50/1*c9xmAT8wwnKVhrSe_ZRz4w.png)](/@apurbapokharel/modeling-
blockchains-as-a-deterministic-finite-
automata-59c884745736?source=read_next_recirc---------0---------------------
143bb70c_ed38_44f1_b3b6_4484e803a652-------)

[[![Jeremy
Orme](https://miro.medium.com/fit/c/40/40/1*BamRItY3aSX0qMIliB8NFw.png)](/@jeremyorme?source=read_next_recirc
---------1---------------------143bb70c_ed38_44f1_b3b6_4484e803a652-------)

[Jeremy Orme

](/@jeremyorme?source=read_next_recirc---------1---------------------
143bb70c_ed38_44f1_b3b6_4484e803a652-------)

## Peer-to-peer store security (syntax)

![](https://miro.medium.com/focal/112/112/50/50/1*nJn-
IC1DB2L9tbGcohNqtg.png)](/@jeremyorme/peer-to-peer-store-security-syntax-
ee862ba56116?source=read_next_recirc---------1---------------------
143bb70c_ed38_44f1_b3b6_4484e803a652-------)

[[![Lucas |
Eaglenode](https://miro.medium.com/fit/c/40/40/1*SVy2ieBHE0aqztvIxdtFTA.jpeg)](/@eaglenode?source=read_next_recirc
---------2---------------------143bb70c_ed38_44f1_b3b6_4484e803a652-------)

[Lucas | Eaglenode

](/@eaglenode?source=read_next_recirc---------2---------------------
143bb70c_ed38_44f1_b3b6_4484e803a652-------)

in

[MATeS of Moonbeam

](https://medium.com/mates-moonbeam?source=read_next_recirc---------2
---------------------143bb70c_ed38_44f1_b3b6_4484e803a652-------)

## Remix tutorial for moonbeam smart contract developers. Part 1

![](https://miro.medium.com/focal/112/112/50/50/0*HR5ytvHuKfVi2pD9)](/mates-
moonbeam/remix-tutorial-for-moonbeam-smart-contract-developers-
part-1-eac4c8398385?source=read_next_recirc---------2---------------------
143bb70c_ed38_44f1_b3b6_4484e803a652-------)

[[![Tony
Verschueren](https://miro.medium.com/fit/c/40/40/1*Y-1UVS4uJRrvNULj_9-5XA.jpeg)](/@Krenh?source=read_next_recirc
---------3---------------------143bb70c_ed38_44f1_b3b6_4484e803a652-------)

[Tony Verschueren

](/@Krenh?source=read_next_recirc---------3---------------------
143bb70c_ed38_44f1_b3b6_4484e803a652-------)

## The Problem With Blockchains and How We Can Fix This

![](https://miro.medium.com/focal/112/112/50/50/1*62RptCHkADBqnADD7xRsKw.png)](/@Krenh/the-
problem-with-blockchains-and-how-we-can-fix-this-
bad5f02794b?source=read_next_recirc---------3---------------------
143bb70c_ed38_44f1_b3b6_4484e803a652-------)

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

