[ ![Fuel Labs](https://fuel-labs.ghost.io/content/images/2021/09/logo-
full-1.png) ](https://fuel-labs.ghost.io)

  * [Home](https://fuel-labs.ghost.io/)
  * [About](https://fuel-labs.ghost.io/about/)

[ ](https://twitter.com/fuellabs_ "Twitter")

Subscribe

[NodeJS](https://fuel-labs.ghost.io/tag/nodejs/)

# Fuel in NodeJS in under 10 Minutes

Setup, faucet and transfer using Fuel with NodeJS

  * [ ![Fuel Labs](/content/images/size/w100/2021/09/logo.svg) ](/author/fuel-labs/)

#### [Fuel Labs](/author/fuel-labs/)

Feb 27, 2020 • 4 min read

![Fuel in NodeJS in under 10
Minutes](/content/images/size/w2000/2021/09/1_XWwrZGJgPUCyerldSAPcSQ.png)

⛽ [Fuel](https://github.com/FuelLabs/fuel-core) is a complete optimistic
rollup sidechain currently operating on Ethereum’s
[Ropsten](https://ropsten.etherscan.io/address/0x2FA75F4a4F86b84E9568B4bf20a6B5466d5Bd9c1)
and
[Görli](https://goerli.etherscan.io/address/0x4E49185B26E93c94f243E0C64eEfE33Aa980e42c)
testnets.

Today we will go through getting started with Fuel!

## Why use Fuel?

  * 💸 __Cost__ : extremely low transaction fees for any ERC-20 tokens or ether (below 3500 gas per tx, to be 2400 in v1.0 VS currently ~21–50,000 gas)
  * ⚡ __Speed__ : quick zero-conf. transaction times (below 1.4s, avg. 0.8 seconds)
  * 🔀 __Meta-transactional__ : pay fees in any ERC-20 token or ether
  * 🛣️ __High throughput__ : can handle extremely high volumes of token and ether transactions (i.e. in the 10s of thousands per second)
  * ⏩ __Production direction__ : our architecture is carefully crafted for large-scale fault-tolerant consumer hardware settings for both validation and usage, without any reliance on novel cryptography, trusted setups, or expensive or customized computing hardware
  * 🙋 __Roll your own__ : completely open-source under Apache-2.0

## How does Fuel Work?

  *  _ _Basics__ : A single smart contract contains all the consensus rules, deposit and withdrawal systems for the Fuel optimistic rollup Ethereum side-chain
  *  _ _Depositing__ : Users deposit assets (i.e. any ERC-20 or Ether) which can then benefit from rock bottom transaction costs and quick confirmation times with no loss of custody or control at any time
  *  _ _Withdrawals__ : Users can withdraw at any time using a liquidity provider swap or standard withdrawals (similar to other rollup systems)
  *  _ _Transfers__ : When users transfer within Fuel, the data is compressed by our aggregator and dumped onto Ethereum, however you can always compress and post your own transaction yourself
  *  _ _Keys__ : Preferably, a secondary signing key is used to sign off on transfers and withdrawals within the side chain. Funds are deposited to that singing key’s address, which then has control over those funds within Fuel. Third-party signer objects can also be used such as those that interact with MetaMask, however raw elliptic signing of hashes must be available.
  *  _ _Wallet__ : the fuel-core wallet object will manage a user’s spendable inputs in a local key-value store database of your choosing (i.e. index db, local storage, level db etc.), output production and the signing of transactions

## Is Fuel Right For You?

Yes, if you’re any project:

  * doing transactions where you are ****cost or volume sensitive****
  * that needs ****fast confirmation speed (under 1.4 seconds)****
  * interested in building a ****Burner Wallet-like system****
  * that needs permissionless atomic swaps between ****any ERC-20 tokens****
  * that will eventually want to ****__deploy your own large-scale rollup system__****

## Getting Started in NodeJS

This tutorial will cover: (1) setting up a persistent Fuel wallet in Node, (2)
fauceting some fake DAI to your wallet, and (3) making your first transfer.

Let’s start a new Node project and install Fuel, open your terminal:

    
    
    mkdir fuel-example && cd fuel-example
    
    npm init
    
    npm install --save fuel-core
    
    nano index.js
    

First let’s (1) import fuel-core, (2) set up a signing key, (3) set up local
persistent storage using a wrapped version of LevelDB, and (4) a Signer
object.

 _ _Note: we use__ ethers _ _heavily across Fuel and here we use its
standardized__ SigningKey _ _object for the Fuel rollup wallet. This key can
be thought of as your Fuel key, where tokens can be deposited to in Fuel.__

 _ _Note: in production, private key generation and handling must be done with
better entropy and with greater care in storage. For now we will just use the
DB.__

[ Setup, faucet and transfer using Fuel with NodeJSSetup, faucet and transfer
using Fuel with NodeJS. GitHub Gist: instantly share code, notes, and
snippets.![](https://gist.github.com/fluidicon.png)Gist262588213843476![](https://github.githubassets.com/images/modules/gists/gist-
og-
image.png)](https://gist.github.com/SilentCaesar/549dcfc59ad839b29ee717d8651a14a1#file-
getting_started_with_fuel_in_nodejs_partial-js)LevelDB with fuel-core in
NodeJS

Now let’s (1) set up a Fuel wallet object with our DB and signer, and (2)
faucet some Fake DAI to our address.

 _ _Note: you can only faucet Fake DAI every 10 minutes per IP, so we wrap the
faucet in an empty try/catch as to not throw past the first 10 minute
window.__

    
    
    const wallet = new Wallet({ db, signer });
    
    try { await wallet.faucet(); } catch (e) {}
    

Now let’s listen for changes in our wallet balance; this will activate our
live mempool websocket-based pubsub system.

 _ _Note:__ listen _ _will fire at any change to the wallet balance; this
includes faucet amounts, transfers, deposits, and withdrawals.__

    
    
    await wallet.listen(async () => {    
        console.log('Balance update in transit',
       utils.formatEther(await wallet.balance(wallet.tokens.fakeDai)));
    });
    

Now let’s make a transfer transfer of 1.5 fake DAI to our own account to test
out a transfer.

    
    
    await wallet.transfer(utils.parseEther(‘1.5’), wallet.tokens.fakeDai, wallet.address);
    
    console.log('You transfered 1.5 Fake Dai to yourself, congrats!');
    
    })(); // finish async method
    

Now let’s save and run the code locally in Node.

    
    
    // cntrl + x then y then enter
    
    node index.js
    

Now you have successfully set up (1) a local Fuel wallet in Node with a (2)
persistent key value store, (3) received some fake DAI from the faucet, and
(4) made your first Fuel transfer!

Please follow/DM us on Twitter [@FuelLabs_](https://twitter.com/fuellabs_),
[@IAmNickDodson](https://twitter.com/IAmNickDodson) or give us a [Github star
or follow](https://github.com/fuellabs/fuel-core)!

Our codebase can be found here:  
<https://github.com/FuelLabs/fuel-core>

 ** **The entire code to this tutorial can be foun d at this Gist here:****  
<https://gist.github.com/SilentCicero/fb854c440dbc615df6ff419f2c33bd06>

P.S. next, we will be demonstrating how Fuel can be used in the browser.

 ** ** _ _Fin.__****

## Sign up for more like this.

Enter your email Subscribe

[ ![Beyond Monolithic Online
Hackathon](/content/images/size/w600/2022/05/BeyondMonolithicHackathonLQ.png)
](/beyond-monolithic-hackathon/)

[

## Beyond Monolithic Online Hackathon

Be a part of the next generation of blockchain by building dapps using the
Sway smart contract language on Fuel, the Fastest Modular Execution Layer, for
a chance to win up to $100,000 in prizes!

](/beyond-monolithic-hackathon/)

  * [ ](/author/ruben/)
  * [ ![Fuel Labs](/content/images/size/w100/2021/09/logo.svg) ](/author/fuel-labs/)

[Ruben Amar](/author/ruben/), [Fuel Labs](/author/fuel-labs/) May 8, 2022 • 3
min read

[ ![Meet the team behind Fuel](/content/images/size/w600/2022/03/JohnA.png)
](/meet-the-team-episode-1/)

[

## Meet the team behind Fuel

For the first episode of our "Meet the team behind Fuel" series, we are
thrilled to hear from John Adler, Co-founder of Fuel Labs and Celestia Labs.

](/meet-the-team-episode-1/)

  * [ ](/author/ruben/)
  * [ ![Fuel Labs](/content/images/size/w100/2021/09/logo.svg) ](/author/fuel-labs/)

[Ruben Amar](/author/ruben/), [Fuel Labs](/author/fuel-labs/) May 4, 2022 • 2
min read

[ ![Introducing Fuel - The Fastest Modular Execution
Layer](/content/images/size/w600/2022/04/Fuel_Trailer_Still_10.jpeg)
](/introducing-fuel-the-fastest-modular-execution-layer/)

[

## Introducing Fuel - The Fastest Modular Execution Layer

Today, we introduce the fastest modular execution layer: Fuel, adding a new
chapter to the blockchain scalability story.

](/introducing-fuel-the-fastest-modular-execution-layer/)

  * [ ![Fuel Labs](/content/images/size/w100/2021/09/logo.svg) ](/author/fuel-labs/)

[Fuel Labs](/author/fuel-labs/) Apr 18, 2022 • 4 min read

[Fuel Labs](https://fuel-labs.ghost.io) (C) 2022

[Powered by Ghost](https://ghost.org/)

