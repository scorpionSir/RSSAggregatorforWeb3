[ ![Fuel Labs](https://fuel-labs.ghost.io/content/images/2021/09/logo-
full-1.png) ](https://fuel-labs.ghost.io)

  * [Home](https://fuel-labs.ghost.io/)
  * [About](https://fuel-labs.ghost.io/about/)

[ ](https://twitter.com/fuellabs_ "Twitter")

Subscribe

[Ethereum](https://fuel-labs.ghost.io/tag/ethereum/)

# Burner Wallet + Fuel = 🔥

Burner Wallet has been a mainstay of Ethereum technology over the past two
years, being used in hundreds of settings at Ethereum’s largest events. The
success of the Burner Wallet has come from the focusing on providing an easy
UX that beginners can easily use.

  * [ ![Fuel Labs](/content/images/size/w100/2021/09/logo.svg) ](/author/fuel-labs/)

#### [Fuel Labs](/author/fuel-labs/)

Mar 30, 2020 • 3 min read

![Burner Wallet + Fuel =
🔥](/content/images/size/w2000/2021/09/1_G4Q00RPoX8GqRybZr6FyKQ.png) Fuel Labs
and Burner Wallet team up for world takeover

Today we release an experimental version of Burner Wallet powered by Fuel.

One important factor in this user experience is ensuring that transactions can
process quickly, reliability and with little-to-no transaction fee. While
Burner Wallets typically use the xDai chain to power these fast & cheap
transactions, optimistic rollups are opening the door to a new family of
scaling technology.

Over the past few weeks, the Burner Wallet and Fuel teams have been busy
closely collaborating on a wallet effort, the Fuel Burner Wallet.

Today we launch an experimental version of Burner using the [Fuel open-
beta](https://github.com/FuelLabs/fuel-core) optimistic rollup side chain
running on Görli.

[Fuel](https://fuel.sh/) is a trustless scalable sidechain that leverages the
optimistic rollup design paradigm to (1) lower the cost of transactions, (2)
increase throughput to thousands of TPS, and (3) enables a better user
experience with seamless transactions.

Using the Burner Wallet 2 framework, anyone can now create a wallet using the
Fuel open-beta technology. These wallets can support any existing Ethereum
asset (ERC20 tokens in addition to native Ether) and provide low-cost, high-
throughput transactions.

## The Wallet

Without further ado, checkout the open-source [Fuel Burner
Wallet](https://burner.fuel.sh/)!

## Try it Out!

(1) Open the [****burner.fuel.sh****](https://burner.fuel.sh/) wallet on
mobile, (2) faucet yourself FakeDai, (3) vote by sending FakeDai to either the
****For**** or ****Against**** ProgPow addresses.

[React App![](https://fmmdg.csb.app/favicon.ico)](https://fmmdg.csb.app/)The
first ever live coin vote on an optimistic rollup regarding ProgPow Ethereum.

## Video Walkthrough

## Fuel Plugin

The Fuel integration was built as a [plugin for the modular Burner Wallet 2
](https://github.com/FuelLabs/fuel-burner-plugin)framework. Developers who
wish to integrate Fuel tokens into their wallet can do so by adding only a few
lines of code to their project:

    
    
    import { FuelGateway, FuelAsset } from ‘fuel-burner-plugin’;
    
    const fuelFakeDai = new FuelAsset({
      id: ‘fakeDai’,
      name: ‘FakeDai’,
      network: ‘5’, // Goerli testnet
      address: ‘0xCF852d1295fD158D43D58ceD47F88f4f4ab0931C’,
      icon: ‘/static/fakedai.png’,
    });
    
    const core = new BurnerCore({
      signers: [new LocalSigner()],
      gateways: [new FuelGateway()],
      assets: [fuelFakeDai],
    });
    

Check out the [sample Fuel Burner Wallet on
Github](https://github.com/FuelLabs/fuel-burner-wallet) for the full code.

As the Fuel project progresses, the Burner Factory will add support for Fuel-
powered assets as well. This will allow both new and existing Ethereum tokens
to be added to a Burner Wallet and easily transferred.

## In Conclusion

Together, Fuel Labs and Burner Wallet are working on the next generation of
Ethereum payments technology. As both teams are currently running off of
grants, we would deeply appreciate your support.

 **Donate to Fuel Labs:**  
[gitcoin.co/grants/199/fuel-labs](https://gitcoin.co/grants/199/fuel-labs)

 ** **Donate to Burner Wallet Factory:****  
[gitcoin.co/grants/145/burner-wallet-2-burner-
factory](https://gitcoin.co/grants/145/burner-wallet-2-burner-factory)

 ** **Fuel Links:****  
 _ _Website__ [fuel.sh](https://fuel.sh/)  
 _ _Github:__[ _ _github.com/fuellabs__](https://github.com/fuellabs)  
 _ _Twitter__ [@FuelLabs_](https://twitter.com/FuelLabs_)

 ** **Burner Wallet Links:****  
 _ _Website__ : [burnerwallet.co](https://burnerwallet.co/)  
 _ _Github:__[github.com/burner-wallet](https://github.com/burner-wallet)  
 _ _Twitter__ : [@DMihal](https://twitter.com/dmihal) / [Austin
Griffith](https://twitter.com/austingriffith)

 ** **Fuel Burner Wallet Codebase (under Apache-2.0):****  
[github.com/fuellabs/fuel-burner-wallet](https://github.com/fuellabs/fuel-
burner-wallet)  
[github.com/fuellabs/fuel-burner-plugin](https://github.com/fuellabs/fuel-
burner-plugin)

[Fuel in NodeJS in under 10 MinutesSetup, faucet and transfer using Fuel with
NodeJS![](https://fuel-labs.ghost.io/favicon.png)Fuel LabsFuel
Labs![](https://fuel-
labs.ghost.io/content/images/2021/09/1_XWwrZGJgPUCyerldSAPcSQ.png)](https://fuel-
labs.ghost.io/fuel-in-nodejs-in-under-10-minutes/)[Build your own customized
Burner Wallet (without the Burner Factory)This guide will explain how to use
the Burner Wallet 2 libraries to easily build your own custom
wallet.![](https://cdn-static-1.medium.com/_/fp/icons/Medium-
Avatar-500x500.svg)MediumDavid
Mihal![](https://miro.medium.com/max/1200/1*U4aJUVRC4Ua76oLXuL6HKg.jpeg)](https://medium.com/@dmihal/build-
your-own-customized-burner-wallet-without-the-burner-factory-dfbe598cdada)

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

