[](https://medium.com/)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/45b6626dc2c0&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](https://medium.com/)

[Home](https://medium.com/)

[Notifications](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![slock.it Blog](https://miro.medium.com/fit/c/64/64/1*ESYB-
YgQa2FKWPo2ofqCiQ.png)](https://blog.slock.it/?source=post_page-----
45b6626dc2c0--------------------------------)

Published in

[slock.it Blog

](https://blog.slock.it/?source=post_page-----
45b6626dc2c0--------------------------------)

[![Simon
Jentzsch](https://miro.medium.com/fit/c/96/96/1*DEDHanvpXujRRBfICx9bHA.png)](https://medium.com/@simon.jentzsch.x7?source=post_page
-----45b6626dc2c0--------------------------------)

[Simon Jentzsch](https://medium.com/@simon.jentzsch.x7?source=post_page-----
45b6626dc2c0--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Faa7a73543e46&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fblockchain-
in-a-
shell-45b6626dc2c0&user=Simon+Jentzsch&userId=aa7a73543e46&source=post_page-
aa7a73543e46----45b6626dc2c0---------------------follow_byline-----------)

Mar 9, 2020

·

4 min read

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F45b6626dc2c0&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fblockchain-
in-a-
shell-45b6626dc2c0&source=--------------------------bookmark_header-----------)

[

Save

](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F45b6626dc2c0&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fblockchain-
in-a-
shell-45b6626dc2c0&source=--------------------------bookmark_header-----------)

# Blockchain in a shell

Have you ever tried to send a transaction directly in your shell? Or how about
a shell script running as a cron job, which reads events from the chain?

Of course, you can run and sync a local node and then run a curl command
against your node:

    
    
    curl -H "Content-Type:text/json" -X POST -d '{"method":"eth_getTransactionReceipt","params":["0xbbb6223001678b8694acaa13dc597692485598cd0a5310bce975418c54b65f14"],"id":1,"jsonrpc":"2.0"}' [https://l](https://rpc.slock.it/mainnet)ocalhost:8545 | jq -r .result

Not nice, but since your full client is running, you should be able to trust
the response. But what if you can’t or don’t want to run a local node and also
don’t want to rely on a centralized remote service?

Incubed is a stateless minimal verification client you can directly use in
your shell. The same request would look like this:

    
    
    in3 eth_getTransactionReceipt 0xbbb6223001678b8694acaa13dc597692485598cd0a5310bce975418c54b65f14

Incubed doesn’t need any syncing node since it connects with the Incubed
network and locally verifies the responses. You can learn more about how this
works [here](/incubed-secure-blockchain-access-for-iot-db4687b3dfa1).

# Installing

The in3 executable is only 300 kB big and includes all you need (even the
complete EVM) to fetch and verify data.

 **For Linux:**

    
    
     _# Add the slock.it ppa to your system  
    _ sudo add-apt-repository ppa:devops-slock-it/in3 _# install the commandline tool in3  
    _ apt-get install in3

 **For MacOS:**

    
    
     _# Add a brew tap  
    _ brew tap slockit/in3 _# install all binaries and libraries  
    _ brew install in3

 **For Windows:**

Just download the latest release from
<https://github.com/slockit/in3-c/releases>

**For Docker:**

    
    
     docker run slockit/in3 eth_getBlockByNumber latest false

By the way, the whole Docker image is only 2.8 MB!

# Let’s Play

Once installed, you can do most things you usually would do with the web3.js-
library and even more on the command line.

Let’s get the first transaction of the latest block:

    
    
    in3 eth_getBlockByNumber latest true | jq ‘.transactions[0]’

If you want to call a function of a contract, in3 will use the ABI encoder:

    
    
    in3 call -to 0xbb9bc244d798123fde783fcc1c72d3bb8c189413 "numberOfProposals():uint"

In order to send a transaction, you can specify a keyfile. Incubed will then
ask for your passphrase to decrypt it. You could also pass a raw key or add
the password as an argument, but this is, of course, not recommended.

    
    
    in3 send -pk mykeyfile.json -to 0x27a37a1210df14f7e058393d026e2fb53b7cf8c1 -gas 1000000 "registerServer(string,uint256)" "https://in3.slock.it/kovan1" 0xFF

Deploying contracts works the same way. You can even pipe the output of the
Solidity compiler directly into Incubed. This command would compile, deploy a
contract, wait until it is mined (-w option), and then return the transaction
receipt, where we use the contractAddress.

    
    
    CONTRACT=`solc — bin MyContract.sol | in3 send -gas 5000000 -pk my_private_key.json -d — -w | jq -r .contractAddress`

I have used this to create shell scripts for preparing test enviroments.

Even offline verifications are possible. You can pipe the proofs into a file,
put it on a USB stick, and then verify the response on a different machine
with no internet connection.

    
    
     _# getting the proof  
    _ in3 –ro eth_getTransactionReceipt 0x2736D225f85740f42D17987100dc8d58e9e162528d58e9e162 > proof.json# verifying the proof  
    in3 –ri eth_getTransactionReceipt 0x2736D225f85740f42D17987100dc8d58e9e162528d58e9e162 < proof.json

If you like your shell and need to sign data, you can use the signing
features:

    
    
    in3 sign -st hash -pk my_private_key.json 0x487b2cbb7997e45b4e9771d14c336b47c87dc2424b11590e32b3a8b9ab327999

Or use ecrecover of a signature to verify the signature and find out who
signed it:

    
    
    in3 ecrecover -st hash 0x487b2cbb7997e45b4e9771d14c336b47c87dc2424b11590e32b3a8b9ab327999 0x0f804ff891e97e8a1c35a2ebafc5e7f129a630a70787fb86ad5aec0758d98c7b454dee5564310d497ddfe814839c8babd3a727692be40330b5b41e7693a445b71c

Incubed is a multichain client, so you can simply define the chain you want to
work with by using the option -c goerli. In case you are running a test
against your local client (maybe using a dev-chain), you can also specify
‘local’ (or the URL of your client).

    
    
    in3 -c local eth_getBlockByNumber latest true   
    | jq '.transactions[0]'

If you have a dApp that is connecting to a client running on localhost:8545
and you can’t or don’t want to sync a node, specifying the port will start
Incubed as a proxy node and a replacement for a full or light client, but
still verifying each request:

    
    
    in3 -c goerli -s 1 -port 8545

Or as Docker :

    
    
    docker run -p 8545:8545 slockit/in3 -c goerli -s 1 -port 8545

# ENS

Addresses are good, but names are better. Using ENS in a shell is supported
for all commands, and wherever you may use an address, domain names are
accepted as well.

    
    
    in3 call -to cryptokitties.eth "pregnantKitties():uint"

# Autocompletion

Autocompletion can increase productivity on the shell. For Incubed, there is
simple support for Bash, which you should include in your .bashrc:

    
    
    _IN3_WORDS=`in3 autocompletelist`  
    complete -W "$_IN3_WORDS" in3

Or for zsh, the more advanced completion:

    
    
    curl <https://raw.githubusercontent.com/slockit/in3-c/develop/scripts/_in3.sh> > /usr/local/share/zsh/site-functions/_in3.sh

![](https://miro.medium.com/max/1400/1*sbqs_u15Ikn4oXtqg-IGSQ.gif)

There are a lot more features in these 300k, so give it a try and check out
[https://in3.readthedocs.io/en/develop/api-
cmd.html](https://in3.readthedocs.io/en/develop/api-cmd.html#)

Simon Jentzsch  
(CTO, slock.it and VP of Blockchain Development at Blockchains LLC)

Resources:

  * <https://github.com/slockit/in3> (TypeScript)
  * <https://github.com/slockit/in3-c> (C + Bindings)
  * <https://in3.readthedocs.io/en/develop/> (Developer Documentation)

Thanks toDani Putney

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fslock-
it-
blog%2F45b6626dc2c0&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fblockchain-
in-a-
shell-45b6626dc2c0&user=Simon+Jentzsch&userId=aa7a73543e46&source=-----45b6626dc2c0
---------------------clap_footer-----------)

\--

1

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fslock-
it-
blog%2F45b6626dc2c0&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fblockchain-
in-a-
shell-45b6626dc2c0&user=Simon+Jentzsch&userId=aa7a73543e46&source=-----45b6626dc2c0
---------------------clap_footer-----------)

\--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fslock-
it-
blog%2F45b6626dc2c0&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fblockchain-
in-a-
shell-45b6626dc2c0&user=Simon+Jentzsch&userId=aa7a73543e46&source=-----45b6626dc2c0
---------------------clap_footer-----------)

\--

1

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F45b6626dc2c0&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fblockchain-
in-a-
shell-45b6626dc2c0&source=--------------------------bookmark_footer-----------)

## [More from slock.it Blog](https://blog.slock.it/?source=post_page-----
45b6626dc2c0--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Fslock-
it-
blog%2F45b6626dc2c0&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fblockchain-
in-a-
shell-45b6626dc2c0&collection=slock.it+Blog&collectionId=15115b6d917a&source=post_page
-----45b6626dc2c0---------------------follow_footer-----------)

IoT + Blockchain

[Read more from slock.it Blog](https://blog.slock.it/?source=post_page-----
45b6626dc2c0--------------------------------)

[](https://medium.com/?source=post_page-----
45b6626dc2c0--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
45b6626dc2c0--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
45b6626dc2c0--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
45b6626dc2c0--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
45b6626dc2c0--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----45b6626dc2c0--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----45b6626dc2c0--------------------------------)

[Get
started](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fblockchain-
in-a-shell-45b6626dc2c0&source=post_page--------------------------
nav_reg-----------)

[![Simon
Jentzsch](https://miro.medium.com/fit/c/176/176/1*DEDHanvpXujRRBfICx9bHA.png)](https://medium.com/@simon.jentzsch.x7)

[

## Simon Jentzsch

](https://medium.com/@simon.jentzsch.x7)

74 Followers

CTO Slock,.it

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Faa7a73543e46&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fblockchain-
in-a-
shell-45b6626dc2c0&user=Simon+Jentzsch&userId=aa7a73543e46&source=post_page-
aa7a73543e46-------------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fusers%2Faa7a73543e46%2Flazily-
enable-writer-
subscription&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fblockchain-
in-a-
shell-45b6626dc2c0&user=Simon+Jentzsch&userId=aa7a73543e46&source=--------------------------subscribe_user-----------)

## More from Medium

[[![eSatya](https://miro.medium.com/fit/c/40/40/1*30dBHNcwnsJwRuVHhldTIg.png)](https://esatya.medium.com/?source=read_next_recirc
---------0---------------------5a13bf22_11a5_47e2_a08d_8becb9896f51-------)

[eSatya

](https://esatya.medium.com/?source=read_next_recirc---------0
---------------------5a13bf22_11a5_47e2_a08d_8becb9896f51-------)

## Making Rahat Open Source

![](https://miro.medium.com/focal/112/112/50/50/0*OVykdbyh0bn1P2hq.png)](https://esatya.medium.com/making-
rahat-open-source-82706400dbfd?source=read_next_recirc---------0
---------------------5a13bf22_11a5_47e2_a08d_8becb9896f51-------)

[[![Zhanna Manzyk](https://miro.medium.com/fit/c/40/40/1*rpjdViiSF-
sC3tLakNbdtw.jpeg)](https://medium.com/@zhanna.manzyk?source=read_next_recirc
---------1---------------------5a13bf22_11a5_47e2_a08d_8becb9896f51-------)

[Zhanna Manzyk

](https://medium.com/@zhanna.manzyk?source=read_next_recirc---------1
---------------------5a13bf22_11a5_47e2_a08d_8becb9896f51-------)

## Top Smart Contract Auditing Companies

![](https://miro.medium.com/focal/112/112/50/50/1*SpVY4_z5h8AjUX2Vt7puFQ.png)](https://medium.com/@zhanna.manzyk/top-
smart-contract-auditing-companies-a27095866cc6?source=read_next_recirc
---------1---------------------5a13bf22_11a5_47e2_a08d_8becb9896f51-------)

[[![Aidan
McMurray](https://miro.medium.com/fit/c/40/40/1*3LKvZQSBfzOM2kz_s9FtkQ.png)](https://medium.com/@aidanmcmurray?source=read_next_recirc
---------2---------------------5a13bf22_11a5_47e2_a08d_8becb9896f51-------)

[Aidan McMurray

](https://medium.com/@aidanmcmurray?source=read_next_recirc---------2
---------------------5a13bf22_11a5_47e2_a08d_8becb9896f51-------)

in

[Coinmonks

](https://medium.com/coinmonks?source=read_next_recirc---------2
---------------------5a13bf22_11a5_47e2_a08d_8becb9896f51-------)

## How Smart Contracts could Automate Banking

![](https://miro.medium.com/focal/112/112/50/50/1*qwtBSJ6MMuL1Mg82dh9B_w.png)](https://medium.com/coinmonks/how-
smart-contracts-could-automate-banking-67f7b59f1272?source=read_next_recirc
---------2---------------------5a13bf22_11a5_47e2_a08d_8becb9896f51-------)

[[![Felix](https://miro.medium.com/fit/c/40/40/1*5jdxolJE-
Hyi50Lsq6yT3g.jpeg)](https://medium.com/@0zym4nd145k1ng0fk1ng5?source=read_next_recirc
---------3---------------------5a13bf22_11a5_47e2_a08d_8becb9896f51-------)

[Felix

](https://medium.com/@0zym4nd145k1ng0fk1ng5?source=read_next_recirc---------3
---------------------5a13bf22_11a5_47e2_a08d_8becb9896f51-------)

## Getting started with DYDX

![](https://miro.medium.com/focal/112/112/50/50/1*0KdGCHHcSmQvrNXo0Z7R_w.png)](https://medium.com/@0zym4nd145k1ng0fk1ng5/getting-
started-with-dydx-40b8c2169f1?source=read_next_recirc---------3
---------------------5a13bf22_11a5_47e2_a08d_8becb9896f51-------)

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

