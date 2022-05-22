[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/566a4d4cbb&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![BlockRocket](https://miro.medium.com/fit/c/64/64/1*txNUAyxbcu2dKnsOnhoy_g.png)](https://medium.com/blockrocket?source=post_page
-----566a4d4cbb--------------------------------)

Published in

[BlockRocket

](https://medium.com/blockrocket?source=post_page-----
566a4d4cbb--------------------------------)

[![Vincent de
Almeida](https://miro.medium.com/fit/c/96/96/2*ZgWauu0kvr0t2CbBCA8UiQ.png)](/@vdecentralised?source=post_page
-----566a4d4cbb--------------------------------)

[Vincent de Almeida](/@vdecentralised?source=post_page-----
566a4d4cbb--------------------------------)

Follow

Apr 14, 2020

·

6 min read

# Dapp development with a local subgraph + Ganache setup

## Local subgraph development for time savings and sanity

![](https://miro.medium.com/max/1400/1*u0p4Nt1fe6jGm9MZFFvmIw.png)

If you’re looking at adding a subgraph for your Dapp through the [The
Graph](https://thegraph.com) or have already done so but your development
cycle involves deploying to a running test network in order to test your
contracts and or subgraph changes, then you may want to consider running the
stack locally.

Running a [Truffle](https://medium.com/u/9c9995b303d5?source=post_page-----
566a4d4cbb--------------------------------),
[Ganache](https://github.com/trufflesuite/ganache-cli) &
[subgraph](https://thegraph.com) stack locally should speed up Dapp
development as the results of your Dapp changes surface quicker. With faster
deploy times, blocks being mined instantly, you should see faster data flow
into your Dapp’s [subgraph](https://thegraph.com) and by extension either its
API or front-end.

There are a number of steps involved in setting up this local stack which we
will walk through with you as well as some thoughts on how the process could
be improved. The steps below follow the official Graph docs which can be found
[here](https://thegraph.com/docs/quick-start#local-development).

# Pre-Requisites

The are 3 pre-requisites for this tutorial which is for you to have a local
Ganache Ethereum blockchain, [Docker](https://www.docker.com/) installed and a
[subgraph](https://thegraph.com) project already initialised for your dapp.

There are 2 options when it comes to Ganache, an app with a nice UI and a CLI
app which we can run from the terminal / command prompt. For the purposes of
this tutorial, we’ll use the CLI. If you wish to use the app, just ensure that
it’s configured with the same params as the CLI.

First order of business, install the CLI globally if you haven’t already:

    
    
    npm install -g ganache-cli

Docker installation instructions: <https://docs.docker.com/get-docker/>

Creating a subgraph project: <https://thegraph.com/docs/define-a-
subgraph#create-a-subgraph-project>

# Step 1: Ganache and Required Parameters

With `ganache-cli` installed, we can spin up a local chain with the following
command:

    
    
    ganache-cli -h 0.0.0.0

This should be all you need to get this stack going. By default, the host is
normally `127.0.0.1` but by overriding this to `0.0.0.0` we bind the service
to all interfaces which means that our local graph node, which runs in a
docker container, will be able to talk to our local blockchain.

Due to regularly developing with `ganache-cli` , I run the CLI with more
options as follows:

    
    
    ganache-cli -h 0.0.0.0 -m "MNEMONIC_HERE" -i 5777 

The 2 extra options involve passing a mnemonic and chain ID respectively. This
allows me to import the private keys of any account once into metamask and the
chain ID allows me to have a static configuration for my local chain within
metamask — the CLI tends to generate a new chain ID every time otherwise.

You’ll know if the CLI is running when the following is one of the last
message printed to the console:

    
    
    Listening on 0.0.0.0:8545

With that confirmed, you now need to migrate / deploy your contracts onto the
local chain with the appropriate `truffle migrate` command.

# Step 2: Running a local Graph node

This bit can be a bit temperamental so bare with it — you may need a few
attempts before getting this going.

The aim is to bring up a Graph node using a docker-compose file. The required
docker-compose file can be found
[here](https://github.com/graphprotocol/graph-node/tree/master/docker).

If you’re a linux user (ignore the fact that macOS is UNIX-based if you’re a
Mac user), you’ll need to run the additional `setup.sh` script for the graph
node to work properly.

The compose file will spin up 3 containers in total, one for the node, another
for an IPFS node and a final Postgres container. Postgres is the persistence
layer for your graph node and when spinning up this container, it will
generate a `data/` directory. Data stored includes information about the
blockchain i.e. block height etc. which is used to determine whether an event
log has been parsed for example.

 ** _A common “Gotcha”_** — If you were to restart your local blockchain, your
node’s DB would then become out of sync with the current state of your chain
and you therefore would need to tear down your DB and start again.

The reason I’m boring you with all this information is to stop you from
experiencing pain when you don’t understand why one day your local stack
worked and then another, it didn’t. Fortunately, we developed a simple script
to make spinning up a local node easy:

If you saved this script in the same directory as the docker-compose file and
gave it execution privileges, you’ll find an easy, repeatable way of spinning
up a graph node after starting a fresh blockchain.

Now, time to run the above script to kick things off!

All going well, the 3 containers should spin up happy (you may need to give it
a minute or two to fully spin up). If everything is running correctly you
should see the following being printed out repeatedly from your `ganache-cli`:

    
    
    $ eth_getBlockByNumber

This means that your Graph node is polling your chain for all the information
it needs to operate. If this is not happening, check if something went wrong
in spinning up the graph node by looking at the docker logs of the container
being printed to the terminal. Alternatively, re-visit the above steps to see
where you may have gone wrong.

# Step 3: Deploying to your local Graph Node

If you’ve deployed a Rinkeby or mainnet subgraph, you’ll know that before
deploying, you need to create a project through the dashboard. Locally, you
still need to create a project to deploy to and the way in which you do it is
via the following command:

    
    
    yarn create-local

Provided your Graph node is running and configured correctly, a project should
have been created. This is a one-time only operation for every project, every
time you start a local Graph node.

From here, you can simply deploy to the node. Again, there are local scripts
you need to call rather than the ones you may be used to. For example:

    
    
    yarn build && yarn deploy-local

Will build and locally deploy your subgraph to your local subgraph. A few
things to note for the node to correctly work:

  * The network for all of your contracts defined in your `subgraph.yml` file must be `mainnet` even though you are deploying to a local node. This will not interact with the main Ethereum network — it’s just the way that `subgraph.yml` needs to be configured for your local node. I learnt the hard way…
  * You will probably already have pre-empted this, but all of your contract addresses in the `subgraph.yml` file need to match the deployment addresses from the migrations you ran against your local blockchain.

Those are the main gotchas that can throw you off.

Provided all went well, you should be told that deployment was successful and
be given a http endpoint to allow you to query for entities. This will of
course rely on data being on chain etc. which you can achieve by either
running in further migrations making state changes or make state changes to
your dapp via some snazzy UX you designed for a front-end (configuring
metamask as described above)

# Conclusion

By running a the full Ganache + subgraph stack locally, we open up the ability
to iterate much faster thanks to faster local deploys, instant block
confirmations etc. However, you can see (and have experienced) that there are
a few pain points involved in getting the stack working. We made an attempt at
improving the node start up sequence with our bash script, but there are still
a number of hoops to jump through to get going. You could automate further by
having a script that will spin up a local blockchain, migrate your contracts
to that chain, start a graph node etc. and it is something we may consider to
help our local development. However, there’s no getting away from the fact
that the out of the box solution has it’s quirks and it’s a case of weighing
up the time taken to set up the local stack vs maybe deploying to Rinkeby
instead. Whatever your thoughts on this are, in general we love the Graph here
at BlockRocket and have had more and more clients integrate this into their
stack. It’ll be interesting to see how the Dapp stack continues to develop
from this point onwards.

If you want to speak to us directly about how to leverage this and other Web 3
tools, please reach out to us using the links below.

Website — [www.blockrocket.tech](https://www.blockrocket.tech/)

Email — [hello@blockrocket.tech](mailto:hello@blockrocket.tech)

Twitter —
[@blockrockettech](https://twitter.com/blockrockettech?source=post_page---------------------------)

Check out our community meetup for our up and coming events — [Blockchain
Manchester](https://meetup.com/BlockchainManchesterMeetup?source=post_page---------------------------)

 **If you enjoyed this post please show it some ❤️ and give it a clap of 50
👏👏👏 — Vincent**

![](https://miro.medium.com/max/1400/0*h8OmFW6Zmhfbsgfn.png)

\--

3

\--

\--

3

## [More from BlockRocket](/blockrocket?source=post_page-----
566a4d4cbb--------------------------------)

Blockchain and decentralised engineering & consultancy based in Manchester, UK
— we build products and help companies understand blockchain and web3
technologies. We have vast knowledge in tokensiation, governance, smart
contract engineerind, IPFS and crypto www.blockrocket.tech

[Read more from BlockRocket](/blockrocket?source=post_page-----
566a4d4cbb--------------------------------)

## Recommended from Medium

[[![Chaitanya
Waikar](https://miro.medium.com/fit/c/40/40/0*R6VQwyS1RzsYhV5h)](/@chaitanyawaikar1993?source=post_internal_links
---------0----------------------------)

[Chaitanya Waikar

](/@chaitanyawaikar1993?source=post_internal_links---------
0----------------------------)

## AWS SQS client using Alpakka and Scala

![](https://miro.medium.com/focal/112/112/50/50/1*OyDvDxqmqdqErL9tYQS4gQ.png)](/@chaitanyawaikar1993/aws-
sqs-client-using-alpakka-and-scala-e43ff7ff23c4?source=post_internal_links
---------0----------------------------)

[[![Pedro
Ceyrat](https://miro.medium.com/fit/c/40/40/0*l1v4pWh7gJZ5Z-7i)](/@pedro.l.t.ceyrat?source=post_internal_links
---------1----------------------------)

[Pedro Ceyrat

](/@pedro.l.t.ceyrat?source=post_internal_links---------
1----------------------------)

in

[xgeeks

](https://medium.com/xgeeks?source=post_internal_links---------
1----------------------------)

## Kubernetes Dummy Operator in Java

![](https://miro.medium.com/focal/112/112/50/50/1*gG5saW3vHLaxQICHf-
PArA.jpeg)](/xgeeks/kubernetes-dummy-operator-in-
java-6b2f26198a55?source=post_internal_links---------
1----------------------------)

[[![nNipsx - Duc
Le](https://miro.medium.com/fit/c/40/40/1*gPzTlbsre_xUuxvqqlkVyw.png)](/@nnipsxz?source=post_internal_links
---------2----------------------------)

[nNipsx - Duc Le

](/@nnipsxz?source=post_internal_links---------2----------------------------)

## IDORs (Insecure Direct Object Reference) over Odoo: Open Source ERP and CRM
(Version 14)

![](https://miro.medium.com/focal/112/112/50/50/1*-TRI2UsaIL72mq_FPMc8cw.png)](/@nnipsxz/idors-
insecure-direct-object-reference-over-odoo-open-source-erp-and-crm-
version-14-2376f63efccd?source=post_internal_links---------
2----------------------------)

[[![Kye Lewis](https://miro.medium.com/fit/c/40/40/1*4G9OQbjBy-
VXNSyFqZODqA.png)](/@kye_themodernmachine?source=post_internal_links---------
3----------------------------)

[Kye Lewis

](/@kye_themodernmachine?source=post_internal_links---------
3----------------------------)

## Reverse engineering an LCD wall’s communications protocol

![](https://miro.medium.com/focal/112/112/50/50/1*ZWd_MJl959_gf9Etc3Turw.png)](/@kye_themodernmachine/reverse-
engineering-an-lcd-wall-communications-
protocol-4662031ddb40?source=post_internal_links---------
3----------------------------)

[[![Richard
Russell](https://miro.medium.com/fit/c/40/40/2*ypRkL8ta8isV6WUtkVEX2Q.jpeg)](/@russell.ajax?source=post_internal_links
---------4----------------------------)

[Richard Russell

](/@russell.ajax?source=post_internal_links---------
4----------------------------)

in

[Cold Brew Code

](https://medium.com/cold-brew-code?source=post_internal_links---------
4----------------------------)

## #100DaysOfCode Day 19: Keeping Myself Accountable (2/3)

![](https://miro.medium.com/focal/112/112/50/50/0*k5E9VbT-PLd7sXmZ)](/cold-
brew-code/100daysofcode-day-19-keeping-myself-
accountable-2-3-421e17524347?source=post_internal_links---------
4----------------------------)

[[![Tue
Nguyen](https://miro.medium.com/fit/c/40/40/1*WzSdv5W5Vtwm9R12HsqqjQ.jpeg)](/@tuenguyends?source=post_internal_links
---------5----------------------------)

[Tue Nguyen

](/@tuenguyends?source=post_internal_links---------
5----------------------------)

## Python’s typing systems

![](https://miro.medium.com/focal/112/112/50/50/1*0czQRTzL79PhTm4eJaL9Hw.png)](/@tuenguyends/python-
typing-systems-444b54371f9c?source=post_internal_links---------
5----------------------------)

[[![Abdullah
Baghuth](https://miro.medium.com/fit/c/40/40/1*tWXhGSHcGvTZ299KdVe9rA.jpeg)](/@abdullahbaghuth?source=post_internal_links
---------6----------------------------)

[Abdullah Baghuth

](/@abdullahbaghuth?source=post_internal_links---------
6----------------------------)

## Why Does Kali Linux Update Take More Than Usual

![](https://miro.medium.com/focal/112/112/50/50/1*FT_zGRNcZELFYtav8Wd28Q.jpeg)](/@abdullahbaghuth/why-
does-kali-linux-update-take-more-than-
usual-d37698366c52?source=post_internal_links---------
6----------------------------)

[[![Archie
Lister](https://miro.medium.com/fit/c/40/40/0*qSHnkaXkOQD221U4.)](/@archielister?source=post_internal_links
---------7----------------------------)

[Archie Lister

](/@archielister?source=post_internal_links---------
7----------------------------)

## Illustrating the Importance of Virtual Environments in Python

![](https://miro.medium.com/focal/112/112/50/50/0*utg6_Un3y-MABDcQ.png)](/@archielister/illustrating-
the-importance-of-virtual-environments-in-
python-39837181ce71?source=post_internal_links---------
7----------------------------)

[](/?source=post_page-----566a4d4cbb--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
566a4d4cbb--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
566a4d4cbb--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
566a4d4cbb--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
566a4d4cbb--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----566a4d4cbb--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----566a4d4cbb--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fblockrocket%2Fdapp-
development-with-a-local-subgraph-ganache-setup-566a4d4cbb&source=post_page
--------------------------nav_reg-----------)

[![Vincent de
Almeida](https://miro.medium.com/fit/c/176/176/2*ZgWauu0kvr0t2CbBCA8UiQ.png)](/@vdecentralised)

[

## Vincent de Almeida

](/@vdecentralised)

28 Followers

Fullstack Web 3 Buidler

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F7d883ce4c22d&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fblockrocket%2Fdapp-
development-with-a-local-subgraph-ganache-
setup-566a4d4cbb&newsletterV3=c4886ba0900d&newsletterV3Id=7d883ce4c22d&user=Vincent+de+Almeida&userId=c4886ba0900d&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Frontend
Team](https://miro.medium.com/fit/c/40/40/1*55KbukPZhXbLhvQ3QLpPGg.png)](/@frontendteam?source=read_next_recirc
---------0---------------------22a0d9f9_9b4c_4fea_bea7_6d7365f77f72-------)

[Frontend Team

](/@frontendteam?source=read_next_recirc---------0---------------------
22a0d9f9_9b4c_4fea_bea7_6d7365f77f72-------)

## How to handle input keyup events after the user stops typing — Svelte
actions and debouncing

![Create a stepper pure css atomic component using
tailwind](https://miro.medium.com/focal/112/112/50/50/0*dV3XrriUOiISnY7C.jpg)](/@frontendteam/how-
to-handle-input-keyup-events-after-the-user-stops-typing-svelte-actions-and-
debouncing-512b3a7e0aef?source=read_next_recirc---------0---------------------
22a0d9f9_9b4c_4fea_bea7_6d7365f77f72-------)

[[![Crizant
Lai](https://miro.medium.com/fit/c/40/40/1*1KNCmUV7Cfb0ylrQPqpFtg.jpeg)](/@crizantlai?source=read_next_recirc
---------1---------------------22a0d9f9_9b4c_4fea_bea7_6d7365f77f72-------)

[Crizant Lai

](/@crizantlai?source=read_next_recirc---------1---------------------
22a0d9f9_9b4c_4fea_bea7_6d7365f77f72-------)

## Sonos IKEA Symfonisk Bookshelf Speaker Review

![](https://miro.medium.com/focal/112/112/50/50/1*Xq0z1etUzwRNB3fRa1EP9g.jpeg)](/@crizantlai/sonos-
ikea-symfonisk-bookshelf-speaker-review-a56e32ae0bd9?source=read_next_recirc
---------1---------------------22a0d9f9_9b4c_4fea_bea7_6d7365f77f72-------)

[[![Anil
Kumar](https://miro.medium.com/fit/c/40/40/1*iVUOAnKLmGhKsc2XVdDSfw.jpeg)](/@anilbms75?source=read_next_recirc
---------2---------------------22a0d9f9_9b4c_4fea_bea7_6d7365f77f72-------)

[Anil Kumar

](/@anilbms75?source=read_next_recirc---------2---------------------
22a0d9f9_9b4c_4fea_bea7_6d7365f77f72-------)

## Why Should You Invest In Developer Experience?

![](https://miro.medium.com/focal/112/112/50/50/1*l93Ay_tGXTRvwS7ofgt5og.jpeg)](/@anilbms75/why-
should-you-invest-in-developer-experience-5b59b0d40545?source=read_next_recirc
---------2---------------------22a0d9f9_9b4c_4fea_bea7_6d7365f77f72-------)

[[![Tonytruong](https://miro.medium.com/fit/c/40/40/1*rpDDkCAUcIfW0QYQmv6MZw.png)](/@tonytruong873?source=read_next_recirc
---------3---------------------22a0d9f9_9b4c_4fea_bea7_6d7365f77f72-------)

[Tonytruong

](/@tonytruong873?source=read_next_recirc---------3---------------------
22a0d9f9_9b4c_4fea_bea7_6d7365f77f72-------)

## [DevOps]Ruby on Rails 2.7.0— The Apple Macbook M1 Issue.

![](https://miro.medium.com/focal/112/112/50/50/1*S46L30E7OhPUmYIfmZyc_w.jpeg)](/@tonytruong873/devops-
ruby-on-rails-2-7-0-the-apple-
macbook-m1-issue-13267fc05256?source=read_next_recirc---------3
---------------------22a0d9f9_9b4c_4fea_bea7_6d7365f77f72-------)

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

