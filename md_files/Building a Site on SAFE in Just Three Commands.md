[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/a2d4f2a74762&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![safenetwork](https://miro.medium.com/fit/c/64/64/1*oEy3kCG2HULiXdpEQdr6Nw.jpeg)](https://medium.com/safenetwork?source=post_page
-----a2d4f2a74762--------------------------------)

Published in

[safenetwork

](https://medium.com/safenetwork?source=post_page-----
a2d4f2a74762--------------------------------)

[![Josh
Wilson](https://miro.medium.com/fit/c/96/96/1*Ha7Eg6NDv0bnHWxuzpETAw.jpeg)](/@joshuef?source=post_page
-----a2d4f2a74762--------------------------------)

[Josh Wilson](/@joshuef?source=post_page-----
a2d4f2a74762--------------------------------)

Follow

Sep 19, 2019

·

4 min read

# Building a Site on SAFE in Just Three Commands

With the release of the new CLIs, here’s a small guide to help you make use of
the CLI and build a site on the SAFE Network in three simple commands.

But first, let’s get you set up!

What you’ll need before we start;

  * [SAFE CLI](https://github.com/maidsafe/safe-cli/releases/tag/0.2.2) downloaded
  * [SAFE_auth](https://github.com/maidsafe/safe-authenticator-cli/releases/tag/0.2.0) downloaded

Helpfully, we’ve got [a guide on how to
download](https://safenetforum.org/t/new-release-vault-phase-1-real-
vault/29712) both of these, plus user guides for both [SAFE_CLI
](https://github.com/maidsafe/safe-cli/blob/master/README.md)and
[SAFE_auth](https://github.com/maidsafe/safe-authenticator-
cli/blob/master/README.md) that we’d recommend you have handy as they give you
a detailed overview of what functionality each give you. Once you have the
SAFE_auth daemon running locally (this is in the guide too), we’re ready to
begin!

`$ safe auth` will enable the authorisation and save the authentication
locally for you. It should look something like this…

![](https://miro.medium.com/max/1400/0*h9TijSWJrPj5pGyh)

 **Command One: Uploading data**

So now, let’s say you have a local folder mysite that contains index.html and
css/styles.css so it’s not ugly.

`$ safe files put -r mysite/`

This will upload your folder to the SAFE Network. The / at the end is
important to set the root of your newly created FilesContainer to be mysite
(and not have mysite as a folder within it). You can [read more about this in
the safe-cli User Guide 2](https://github.com/maidsafe/safe-cli#files).

It will in return, print out some info about your new files on the network.
The Files Container URL is important and we’ll need it for the next step…

![](https://miro.medium.com/max/1380/0*QnLM_4gkXEui3WAt)

 **Command Two: Creating a Public Name**

The SAFE Network uses a distributed NRS to allow you to register URLs (but
without any third party). NRS means Name Resolution System and the easiest way
to think about it is how SAFE lets you have human-readable urls.

To do that and register a site, such as `thesite`:

`$ safe nrs **create** thesite -l "< **link** **to** FilesContainer **URL**
>?v=0"`

![](https://miro.medium.com/max/1380/0*EdVCfTaU884cK4lv)

`?v=0` is needed here to specify a version to point to. The SAFE Network
principles note that all public data must be versioned. And this way, we can
easily track any/all changes to a Public Name.

And now, you can check your site on the network via;

`$ safe cat safe://thesite/index.html`

![](https://miro.medium.com/max/1400/0*qVIreBHPvSgtohc5)

 **Command Three: Updating your Files**

The SAFE Network distinguishes between updating a FilesContainer, and updating
an NRS Name. The latter, must _always_ be versioned (as we saw above).

When you have changes to your site, you can update your NRS using the files
api thus:

`$ safe files sync -r ./mysite/ safe: _//thesite -u -d -r_`

![](https://miro.medium.com/max/1380/0*JQBfUpBANrTBfshb)

`-u` here updates the corresponding NrsContainer as well as the
FilesContainer, so your changes will be reflected at `safe://thesite`. `-d`
signifies that any deleted files will be deleted in the next version of the
containers, too. `-r` is again, to sync recursively.

And now, if you access safe://thesite/index.html, you’ll see your changed
files:

![](https://miro.medium.com/max/1400/0*LY-Yo9meCxYHGYOi)

Not only can you update your site easily, but inherent in the SAFE Network is
versioning. What this means is that you can actually access older versions of
a site via the version query param: `$ safe cat “safe://thesite?v=0”`, will
show you your first content, for example. Pretty neat huh?

So you’ve played around with these Command Lines. But what if you want to
actually _see_ your site in action? we have a browser proof of concept
[available for
download](https://github.com/maidsafe/safe_browser/releases/tag/CLI-POC) that
works with the above CLIs and of course, Vaults too. However, please note this
only works for Linux and Mac just now, with Windows to follow soon.

…

So after this, you’re probably thinking: why doesn’t the internet today do
this?! Why do I have to faff around with domain registrars, pay money and not
_own_ my stuff. Why do I need a server?

We agree, hence why we’re one a single mission to build the SAFE Network. A
permissionless network that removes faff, servers and allows you to just start
developing. [Why not join us](https://safenetforum.org/)?

\--

\--

\--

## [More from safenetwork](/safenetwork?source=post_page-----
a2d4f2a74762--------------------------------)

Stories from around the SAFE Network

[Read more from safenetwork](/safenetwork?source=post_page-----
a2d4f2a74762--------------------------------)

## Recommended from Medium

[[![stackpython](https://miro.medium.com/fit/c/40/40/2*UW3EVMncCjXJoxN0VynvFg.jpeg)](/@stackpython?source=post_internal_links
---------0----------------------------)

[stackpython

](/@stackpython?source=post_internal_links---------
0----------------------------)

## Django Search (with Q objects) Tutorial

![](https://miro.medium.com/focal/112/112/50/50/1*d4E3XSzQKY0XgUMjn6zlUg.png)](/@stackpython/django-
search-with-q-objects-tutorial-9c701db74e0e?source=post_internal_links
---------0----------------------------)

[[![PlantSwap.finance](https://miro.medium.com/fit/c/40/40/1*Bjh4sTaLc3XtiOPm11TRxA.png)](/@plantswapfinance?source=post_internal_links
---------1----------------------------)

[PlantSwap.finance

](/@plantswapfinance?source=post_internal_links---------
1----------------------------)

## 🌱 PlantSwap.finance is sprouting 🌱

](/@plantswapfinance/plantswap-finance-is-
sprouting-7b3bee286d4d?source=post_internal_links---------
1----------------------------)

[[![Confeur](https://miro.medium.com/fit/c/40/40/2*3CesqB54eVUGDRmA36tBSw.png)](/@confeurhq?source=post_internal_links
---------2----------------------------)

[Confeur

](/@confeurhq?source=post_internal_links---------
2----------------------------)

## Sprints vs Milestones

![](https://miro.medium.com/focal/112/112/50/50/1*yTMTBqK4AUCXWGSZvSO96w.png)](/@confeurhq/sprints-
vs-milestones-6fe700d101f9?source=post_internal_links---------
2----------------------------)

[[![Shubham
Rasal](https://miro.medium.com/fit/c/40/40/1*VjGIWG_uEDBtUYYnU4al0g.jpeg)](/@developer-
shubham-rasal?source=post_internal_links---------
3----------------------------)

[Shubham Rasal

](/@developer-shubham-rasal?source=post_internal_links---------
3----------------------------)

## Building Scalable Applications and Microservices on AWS.

![](https://miro.medium.com/focal/112/112/50/50/1*a75YpoJ6Olma1nIhn7rBHw.png)](/@developer-
shubham-rasal/building-scalable-applications-and-microservices-on-
aws-b57672d24378?source=post_internal_links---------
3----------------------------)

[[![Saurabh
Verma](https://miro.medium.com/fit/c/40/40/1*JlhkbIk4VXgkS5QohafjeQ.png)](/@_.saurabh?source=post_internal_links
---------4----------------------------)

[Saurabh Verma

](/@_.saurabh?source=post_internal_links---------
4----------------------------)

## Let world know you by using GitHub to host your website.

![](https://miro.medium.com/focal/112/112/50/50/1*UXCP8KcYQ6tdRJ-
qBoxaeg.png)](/@_.saurabh/let-world-know-you-by-using-github-to-host-your-
website-bdd04ced014d?source=post_internal_links---------
4----------------------------)

[[![Solvd](https://miro.medium.com/fit/c/40/40/1*RbiCCmiVDB6KkRzV5FNSfw.png)](/@solvd-
company?source=post_internal_links---------5----------------------------)

[Solvd

](/@solvd-company?source=post_internal_links---------
5----------------------------)

## Native vs. cross-platform mobile app development. Cracking the notorious
dilemma

![](https://miro.medium.com/focal/112/112/50/50/1*I1TjsehKB263afB6tkN7fA.jpeg)](/@solvd-
company/native-vs-cross-platform-mobile-app-development-cracking-the-
notorious-dilemma-9fa1602add73?source=post_internal_links---------
5----------------------------)

[[![vigu](https://miro.medium.com/fit/c/40/40/2*aQ7f33_HDEvagZC7dYbIgA.jpeg)](/@vigu-
madurai?source=post_internal_links---------6----------------------------)

[vigu

](/@vigu-madurai?source=post_internal_links---------
6----------------------------)

## Must have settings in VS Code

![](https://miro.medium.com/focal/112/112/50/50/1*hjkFnm5KkoDkuhr6rmNGiA.jpeg)](/@vigu-
madurai/must-have-settings-in-vs-code-371814ca076a?source=post_internal_links
---------6----------------------------)

[[![Satyajit
Roy](https://miro.medium.com/fit/c/40/40/1*mh4J433dMVdbSSZAW2EENA.jpeg)](/@email2sroy?source=post_internal_links
---------7----------------------------)

[Satyajit Roy

](/@email2sroy?source=post_internal_links---------
7----------------------------)

in

[AWS Tip

](https://medium.com/aws-tip?source=post_internal_links---------
7----------------------------)

## [Terraform] Azure HDInsight HBase accelerated disk write support

](/aws-tip/terraform-azure-hdinsight-hbase-accelerated-disk-write-support-
bfeed54aba28?source=post_internal_links---------7----------------------------)

[](/?source=post_page-----a2d4f2a74762--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
a2d4f2a74762--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
a2d4f2a74762--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
a2d4f2a74762--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
a2d4f2a74762--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----a2d4f2a74762--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----a2d4f2a74762--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fsafenetwork%2Fbuilding-
a-site-on-safe-in-just-three-commands-a2d4f2a74762&source=post_page
--------------------------nav_reg-----------)

[![Josh
Wilson](https://miro.medium.com/fit/c/176/176/1*Ha7Eg6NDv0bnHWxuzpETAw.jpeg)](/@joshuef)

[

## Josh Wilson

](/@joshuef)

22 Followers

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fusers%2Ffe84c486ac07%2Flazily-enable-
writer-
subscription&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fsafenetwork%2Fbuilding-
a-site-on-safe-in-just-three-
commands-a2d4f2a74762&user=Josh+Wilson&userId=fe84c486ac07&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Hongjje
Dev](https://miro.medium.com/fit/c/40/40/1*kvSYSwsiGQ-1vr52hVYwXg.jpeg)](/@hongjje.dev?source=read_next_recirc
---------0---------------------3644d013_8052_44b2_b3df_5a7dc30c3de6-------)

[Hongjje Dev

](/@hongjje.dev?source=read_next_recirc---------0---------------------
3644d013_8052_44b2_b3df_5a7dc30c3de6-------)

## [Leetcode] 1396. Design Underground System 문제 풀이

](/@hongjje.dev/leetcode-1396-design-underground-system-문제-
풀이-c6f02722064f?source=read_next_recirc---------0---------------------
3644d013_8052_44b2_b3df_5a7dc30c3de6-------)

[[![Yathindra
Kodithuwakku](https://miro.medium.com/fit/c/40/40/1*hhXMc6toKSUJkJQJ37BMvQ.png)](/@yathindra?source=read_next_recirc
---------1---------------------3644d013_8052_44b2_b3df_5a7dc30c3de6-------)

[Yathindra Kodithuwakku

](/@yathindra?source=read_next_recirc---------1---------------------
3644d013_8052_44b2_b3df_5a7dc30c3de6-------)

in

[Identity Beyond Borders

](https://medium.com/identity-beyond-borders?source=read_next_recirc---------1
---------------------3644d013_8052_44b2_b3df_5a7dc30c3de6-------)

## Performance optimization techniques we are using in Asgardeo — Part 01

![](https://miro.medium.com/focal/112/112/50/50/1*tD_k4VbQDq7HYb27EXK6FA.png)](/identity-
beyond-borders/performance-optimization-techniques-we-are-using-in-asgardeo-
part-01-fa436327c618?source=read_next_recirc---------1---------------------
3644d013_8052_44b2_b3df_5a7dc30c3de6-------)

[[![Mani](https://miro.medium.com/fit/c/40/40/1*O-MxGrhtiIzNf0FQli-G4Q.jpeg)](/@smj.johnsonjr?source=read_next_recirc
---------2---------------------3644d013_8052_44b2_b3df_5a7dc30c3de6-------)

[Mani

](/@smj.johnsonjr?source=read_next_recirc---------2---------------------
3644d013_8052_44b2_b3df_5a7dc30c3de6-------)

## Why I’ve learned multiple Frameworks

![](https://miro.medium.com/focal/112/112/50/50/1*xpQqEEYr_sSviQ2g1TKvRw.jpeg)](/@smj.johnsonjr/why-
ive-learned-multiple-frameworks-cddb2c177cdd?source=read_next_recirc---------2
---------------------3644d013_8052_44b2_b3df_5a7dc30c3de6-------)

[[![Muhammad Syarif](https://miro.medium.com/fit/c/40/40/0*3qIvO-
zYYgIh-I4a.jpg)](/@mhdsyarif?source=read_next_recirc---------3
---------------------3644d013_8052_44b2_b3df_5a7dc30c3de6-------)

[Muhammad Syarif

](/@mhdsyarif?source=read_next_recirc---------3---------------------
3644d013_8052_44b2_b3df_5a7dc30c3de6-------)

in

[Grow at Warung Pintar

](https://medium.com/warung-pintar?source=read_next_recirc---------3
---------------------3644d013_8052_44b2_b3df_5a7dc30c3de6-------)

## Let’s Find Out about Refactoring in Software Development

![](https://miro.medium.com/focal/112/112/50/50/1*GmUE38YnYeJX1hEXAKdjnw.jpeg)](/warung-
pintar/lets-find-out-about-refactoring-in-software-
development-719b0e64799?source=read_next_recirc---------3---------------------
3644d013_8052_44b2_b3df_5a7dc30c3de6-------)

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

