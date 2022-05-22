[](https://medium.com/)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/6db33a733e79&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](https://medium.com/)

[Home](https://medium.com/)

[Notifications](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![slock.it Blog](https://miro.medium.com/fit/c/64/64/1*ESYB-
YgQa2FKWPo2ofqCiQ.png)](https://blog.slock.it/?source=post_page-----
6db33a733e79--------------------------------)

Published in

[slock.it Blog

](https://blog.slock.it/?source=post_page-----
6db33a733e79--------------------------------)

[![Heiko Burkhardt](https://miro.medium.com/fit/c/96/96/0*ekxk-
WtuUcQFHCOt)](https://medium.com/@burkhardt.heiko?source=post_page-----
6db33a733e79--------------------------------)

[Heiko Burkhardt](https://medium.com/@burkhardt.heiko?source=post_page-----
6db33a733e79--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fc9f67a78f6e5&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fanalyzing-
solidity-smart-contracts-with-
piet-6db33a733e79&user=Heiko+Burkhardt&userId=c9f67a78f6e5&source=post_page-c9f67a78f6e5
----6db33a733e79---------------------follow_byline-----------)

Aug 7, 2019

·

3 min read

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F6db33a733e79&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fanalyzing-
solidity-smart-contracts-with-
piet-6db33a733e79&source=--------------------------bookmark_header-----------)

[

Save

](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F6db33a733e79&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fanalyzing-
solidity-smart-contracts-with-
piet-6db33a733e79&source=--------------------------bookmark_header-----------)

# Analyzing Solidity Smart Contracts with Piet

![](https://miro.medium.com/max/1400/1*MfMQmnfBChUs4-D7W_MDvw.png)

If you develop, audit, or use complex smart contracts, you may have wished
for:

  * a **graphical representation** of a smart contract architecture that helps you communicate with coworkers or clients (or even just document it);
  * an easily understandable **inheritance structure;**
  * a fast way to **interact with contracts** through a graphical user interface (e.g., read the state, send transactions, or list events);
  * a compelling way to create **smart contract documentation** from NatSpec annotations.

Piet, our new software, fills these needs by parsing Solidity code,
graphically representing contracts and their relations, and providing a smart
contract inspector.

[ **Live
demo**](https://piet.slock.it/?container=examples%2Fexport1562664060589.piet.json)

[ **GitHub Repository**](https://github.com/slockit/piet)

 **Warning:** Piet has not yet undergone in-depth testing and may contain
serious bugs.

# Getting Started

[Piet](https://piet.slock.it) supports Solidity source files, Truffle build
files, and piet container files. To load these files, click on `Load` in the
`Files` tab.

You can also use Piet is to retrieve the Solidity sources directly from a
public GitHub repository. To do so, pass the GitHub account and repository
name as the URL parameters `gitHubUser` and`gitHubRepo`. Optionally, you can
use the URL parameter `subDir` to pass a path to the repository directory
containing the contracts. This prevents Piet from scanning the complete
repository for Solidity files. Similarly, you can use the parameter
`container` to load a Piet container file.

For example:

    
    
    [https://piet.slock.it/?gitHubUser=gnosis&gitHubRepo=safe-contracts&subDir=contracts](https://piet.slock.it/?gitHubUser=gnosis&gitHubRepo=safe-contracts&subDir=contracts)<https://piet.slock.it/?container=examples%2Fexport1562664060589.piet.json>

If available, Piet uses an injected web3 object to interact with a blockchain.
You can also use RPCs or [Incubed](https://github.com/slockit/in3) to connect
to a chain. To change the connection method, click on the connection icon in
the lower-left corner.

# Inheritance Structure

![](https://miro.medium.com/max/1400/1*G6vJDrVc4o52tRkfJeLeBg.png)

Inheritance graph

This view shows the inheritance structure of the Gnosis Safe smart contracts
and the structs and enumeration defined in these contracts. In the example
above, the contract `DailyLimitModule` inherits the contract members from the
contract `Module` and defines the struct `DailyLimit`.

# Contract Inspector

![](https://miro.medium.com/max/1400/1*L_buuQP7Gf3BlXu6qMX4HA.png)

Calling a function

If a contract is selected by clicking on its name in the graph view, the
contract inspector shows the member elements of the selected contract (e.g.,
state variables, functions, modifiers, and events). Documentation labels
derived from NatSpec annotations in the Solidity code will also be shown.

You can retrieve the state of a contract instance and send transactions via
the contract inspector. To enable these interactions, provide the address of
the contract by clicking on the edit icon and pasting the address.

# Piet Container File

If you have loaded a lot of contracts, moved around the boxes in the
inheritance graph, or added instance addresses to contracts you can create a
Piet container file to save your work. To create a container file, click on
`Save` in the `File` tab.

# Additional Features

Piet also provides the following features:

  * Event browser
  * NatSpec to Markdown documentation generator
  * Node inspection via JSON RPC calls
  * Transaction history view
  * Code and ABI view

[ **CHECK OUT PIET**](https://piet.slock.it)

![](https://miro.medium.com/max/1400/1*rkEZLDYYoXNaUz2-3udsMg.png)

Event browser

![](https://miro.medium.com/max/1400/1*DAVCRWlpn90zbb15kfUDhQ.png)

Node inspection

![](https://miro.medium.com/max/1400/1*ThTAglrmKFAWDy6q1KNGxQ.png)

Documentation generator

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fslock-
it-
blog%2F6db33a733e79&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fanalyzing-
solidity-smart-contracts-with-
piet-6db33a733e79&user=Heiko+Burkhardt&userId=c9f67a78f6e5&source=-----6db33a733e79
---------------------clap_footer-----------)

\--

1

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fslock-
it-
blog%2F6db33a733e79&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fanalyzing-
solidity-smart-contracts-with-
piet-6db33a733e79&user=Heiko+Burkhardt&userId=c9f67a78f6e5&source=-----6db33a733e79
---------------------clap_footer-----------)

\--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fslock-
it-
blog%2F6db33a733e79&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fanalyzing-
solidity-smart-contracts-with-
piet-6db33a733e79&user=Heiko+Burkhardt&userId=c9f67a78f6e5&source=-----6db33a733e79
---------------------clap_footer-----------)

\--

1

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F6db33a733e79&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fanalyzing-
solidity-smart-contracts-with-
piet-6db33a733e79&source=--------------------------bookmark_footer-----------)

## [More from slock.it Blog](https://blog.slock.it/?source=post_page-----
6db33a733e79--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Fslock-
it-
blog%2F6db33a733e79&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fanalyzing-
solidity-smart-contracts-with-
piet-6db33a733e79&collection=slock.it+Blog&collectionId=15115b6d917a&source=post_page
-----6db33a733e79---------------------follow_footer-----------)

IoT + Blockchain

[Read more from slock.it Blog](https://blog.slock.it/?source=post_page-----
6db33a733e79--------------------------------)

[](https://medium.com/?source=post_page-----
6db33a733e79--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
6db33a733e79--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
6db33a733e79--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
6db33a733e79--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
6db33a733e79--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----6db33a733e79--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----6db33a733e79--------------------------------)

[Get
started](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fanalyzing-
solidity-smart-contracts-with-piet-6db33a733e79&source=post_page
--------------------------nav_reg-----------)

[![Heiko Burkhardt](https://miro.medium.com/fit/c/176/176/0*ekxk-
WtuUcQFHCOt)](https://medium.com/@burkhardt.heiko)

[

## Heiko Burkhardt

](https://medium.com/@burkhardt.heiko)

20 Followers

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Fc9f67a78f6e5&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fanalyzing-
solidity-smart-contracts-with-
piet-6db33a733e79&user=Heiko+Burkhardt&userId=c9f67a78f6e5&source=post_page-c9f67a78f6e5
-------------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fusers%2Fc9f67a78f6e5%2Flazily-
enable-writer-
subscription&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fanalyzing-
solidity-smart-contracts-with-
piet-6db33a733e79&user=Heiko+Burkhardt&userId=c9f67a78f6e5&source=--------------------------subscribe_user-----------)

## More from Medium

[[![DuckDuckDev](https://miro.medium.com/fit/c/40/40/1*ZOYuJSJvKywcA8c1sIKz-w.jpeg)](https://medium.com/@duckddev?source=read_next_recirc
---------0---------------------433994fb_37fc_4a0d_85d5_07e1a383c3f9-------)

[DuckDuckDev

](https://medium.com/@duckddev?source=read_next_recirc---------0
---------------------433994fb_37fc_4a0d_85d5_07e1a383c3f9-------)

## OpenZeppelin Override TypeError Fixes

](https://medium.com/@duckddev/openzeppelin-override-typeerror-fixes-
db7e571c39d9?source=read_next_recirc---------0---------------------
433994fb_37fc_4a0d_85d5_07e1a383c3f9-------)

[[![StErMi](https://miro.medium.com/fit/c/40/40/2*mDoMM6mrDi13fMu427FK9A.jpeg)](https://stermi.medium.com/?source=read_next_recirc
---------1---------------------433994fb_37fc_4a0d_85d5_07e1a383c3f9-------)

[StErMi

](https://stermi.medium.com/?source=read_next_recirc---------1
---------------------433994fb_37fc_4a0d_85d5_07e1a383c3f9-------)

## Capture the Ether Part 1: what is it and how to start

![](https://miro.medium.com/focal/112/112/50/50/1*xyU7pSB2_38nQnZJUM6EBg.png)](https://stermi.medium.com/capture-
the-ether-part-1-what-is-it-and-how-to-
start-c44138d4b936?source=read_next_recirc---------1---------------------
433994fb_37fc_4a0d_85d5_07e1a383c3f9-------)

[[![Jeffersonx
Xavier](https://miro.medium.com/fit/c/40/40/1*N9OL4MFynLtR1u0GQgvM6w.jpeg)](https://jefferson-
xavier.medium.com/?source=read_next_recirc---------2---------------------
433994fb_37fc_4a0d_85d5_07e1a383c3f9-------)

[Jeffersonx Xavier

](https://jefferson-xavier.medium.com/?source=read_next_recirc---------2
---------------------433994fb_37fc_4a0d_85d5_07e1a383c3f9-------)

## Create your own private blockchain using Ethereum

![](https://miro.medium.com/focal/112/112/50/50/0*-zwmlifLw288zg9E.png)](https://jefferson-
xavier.medium.com/create-your-own-private-blockchain-using-
ethereum-3836ce9d04e6?source=read_next_recirc---------2---------------------
433994fb_37fc_4a0d_85d5_07e1a383c3f9-------)

[[![Mo Ashouri](https://miro.medium.com/fit/c/40/40/1*mWwZGvZuuSN-
gEMEhsbGbg.jpeg)](https://ashourics.medium.com/?source=read_next_recirc
---------3---------------------433994fb_37fc_4a0d_85d5_07e1a383c3f9-------)

[Mo Ashouri

](https://ashourics.medium.com/?source=read_next_recirc---------3
---------------------433994fb_37fc_4a0d_85d5_07e1a383c3f9-------)

## Ownership Exploitation in Solidity

](https://ashourics.medium.com/ownership-exploitation-in-
solidity-a457e0fa66c9?source=read_next_recirc---------3---------------------
433994fb_37fc_4a0d_85d5_07e1a383c3f9-------)

[Help

](https://help.medium.com/hc/en-us)

[Status

](https://medium.statuspage.io)

[Writers

](https://about.medium.com/creators/)

[Blog

](https://blog.medium.com)

[Careers

](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e)

[Privacy

](https://policy.medium.com/medium-privacy-policy-f03bf92035c9)

[Terms

](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f)

[About

](https://medium.com/about?autoplay=1)

[Knowable

](https://knowable.fyi)

