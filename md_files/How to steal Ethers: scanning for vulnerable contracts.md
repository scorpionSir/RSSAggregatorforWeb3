# How to steal Ethers: scanning for vulnerable contracts¶

Four years ago, I wrote an article [“How to steal
Bitcoins”](../../blog/stealing-bitcoin.html) that was about finding address
corresponding to weak brainwallets, and some forensic evidence that it was
exploited automatically, for profit.

This article is about Ethereum smart contracts, how you can automatically find
bugs in them allowing you to steal money. I will also present forensic
evidence that it happens in the wild.

## Introduction¶

### Smart contracts¶

[Smart contracts](https://en.wikipedia.org/wiki/Smart_contract) are programs
(executable code) that are stored in the Ethereum blockchain. That means that
they are all publicly accessible!

These program are also “accounts” that can own money. Once created, the smart
contract’s code is immutable, and it is the sole owner and manager of its own
funds. Its code can call functions to receive and send money.

They are implemented in EVM bytecode (for Ethereum Virtual Machine). It’s a
bit of an exotic architecture, and it’s purely a stack machine, but unlike x86
bytecode it is very simple. The EVM is described in Ethereum’s [yellow
paper](https://github.com/ethereum/yellowpaper).

The interactions with the environment are very limited (you can call other
contracts, send/receive money but that’s pretty much it).

Because execution cost fees (called _gas_ ), these contracts are generally
very simple, which make them perfect for automatically analyzing them.

Assuming you have Ether to pay for transaction fees, you can call any contract
that lives on the blockchain.

### Symbolic execution¶

Symbolic execution is the idea of executing a program but having user-
controlled input be “symbols” (representing an unknown value). When we
encounter a conditional statement, we execute both branches but we take note
of the “constraints” that need to be respected for that branch to run.

For example, if we analyze that code:

    
    
    function f(int user_input) {
       if (user_input % 2 == 0) {
          send_all_my_money();
       }
    }
    

There is a valid execution that calls `send_all_my_money()`, and it is
associated with the constraint `user_input % 2 == 0`.

An SMT solver like Z3 knows if such a constraint is satisfiable and will give
us values for `user_input` where it would work.

I developed a tool called [Pakala](pakala.html) to do exactly that. It is
slightly different than the other published tools because it first computes
all the interesting execution paths that the program can take, and then try to
stack these executions together to find bugs where multiple calls (executions)
are needed.

### Bugs we are looking for¶

My tool, [Pakala](pakala.html), looks for two simple things:

  * Programs that can send back more ether that they are sent.

  * Programs that can self-destruct themselves and give us all their money.

These are basically the two ways we can get free money.

Some other checks leading to arbitrary code execution could be worth adding,
and are checked by other existing tools.

### Tell me more!¶

If you want to learn more about bugs in smart contracts, I recommend you look
at at this publication: [“Smashing Ethereum Smart Contracts for Fun and Actual
Profit”](https://conference.hitb.org/hitbsecconf2018ams/materials/D1T2%20-%20Bernhard%20Mueller%20-%20Smashing%20Ethereum%20Smart%20Contracts%20for%20Fun%20and%20ACTUAL%20Profit.pdf).

You can also look at [this talk (and
paper)](https://www.usenix.org/conference/usenixsecurity18/presentation/krupp)
for something similar to what I did, presented in a more detailed and formal
way.

## Tooling¶

For my investigation, I needed two things:

>   * A tool to symbolically execute smart contracts and find exploitable
> bugs. [Mythril](https://github.com/ConsenSys/mythril-classic) or
> [Manticore](https://github.com/trailofbits/manticore) are generic tools, but
> here I developed my own tool called [Pakala](pakala.html), that specialize
> in finding exploitable bugs to steal money.
>
>   * An Ethereum archive node (to look at historical data from smart
> contracts). I needed a dedicated 4 TB SSD, and a month of computation to
> replay Ethereum’s history. [Want more details?](parity_archive_node.html).
>
>   * A blockchain explorer ([etherscan](https://etherscan.io)), and a
> disassembler for contracts without source code ([eveem](http://eveem.com/)).
>
>

I scanned all the contracts in the blockchain, around mid-2018. I also had a
real-time scanning tool running for a bit.

## Vulnerable contracts found¶

I found quite a few interesting things. Here are examples of common findings:

### Wrongly-named constructors¶

This was by far the most common bug I’ve seen in terms of volume.

It’s was a common mistake in old versions of the Solidity compiler: when your
program is initialized, a special function is ran once: the constructor. It
needs to have the same name as the name of your contract. Lots of people would
have typos in the name of the constructor (or copy/paste code) and the
constructor would end up having a different name, leading to a normal method
that can be called by anybody.

Very often that means that a constructor supposed to initialize the “owner” of
the contract (an address that can withdraw the money in it, most often) can be
called by anybody, so anybody can become the owner.

A few examples:

>   * [HOTTO
> (old)](https://etherscan.io/address/0x612f1bdbe93523b7f5036efa87493b76341726e3#code):
> a token contract with source code. If you look at the HOTTO contract you
> will see a method named `HT()` to set the owner. That was meant to be the
> constructor for sure.
>
>   *
> [HitexToken](https://etherscan.io/address/0x102e3bcc2fb6a2fe4c1c4cf09021a5638008b721#code):
> another token contract named HitexToken with an intended constructor
> `HTX()`.
>
>   * [Mobile
> switching](https://etherscan.io/address/0xb2edc59fc6108884b7bde8d623887badf031fc4b):
> a token contract without the solidity source, but if you look at [a
> disassembly](http://eveem.com/code/0xb2EDc59fC6108884b7BdE8D623887BAdF031Fc4b)
> there is a function (signature `0xc868d5ac`) to change the owner that
> anybody can call.
>
>

### Free withdrawal¶

Some contracts also don’t check anything, and allow anyone to get money out if
you ask them nicely:

>   *
> [0x768f3b7538C0285142D86e0A692A086b0f091d3F](https://etherscan.io/address/0x768f3b7538c0285142d86e0a692a086b0f091d3f)
> ([disassembly](http://eveem.com/code/0x768f3b7538C0285142D86e0A692A086b0f091d3F)):
> this one has a `sendEth(address _receiver, uint256 amount)` function in it
> that unconditionally sends the amount passed in, to the address passed in.
>
>   *
> [0xeBE6c7a839A660a0F04BdF6816e2eA182F5d542C](https://etherscan.io/address/0xeBE6c7a839A660a0F04BdF6816e2eA182F5d542C)
> ([disassembly](http://eveem.com/code/0xeBE6c7a839A660a0F04BdF6816e2eA182F5d542C)):
> this one has a `transfer()` function that sends an arbitrary amount to the
> address of your choice, _but_ it checks that `call.value - _value >= 0`,
> `call.value` being the money that you send to the contract and `_value`
> being the money you want it to send out. However it does so by using
> unsigned integers, so this condition always holds.
>
>

### Honeypots¶

An interesting class of contracts I found are honeypots, that are not really
vulnerable and result from inconsistency in the way Pakala models the way
transactions are executed on Ethereum.

[0x9F54d912a029380f2743aAf4dDD28C3f207cD719](https://etherscan.io/address/0x9f54d912a029380f2743aaf4ddd28c3f207cd719#code)
is a good example: it’s a contract that tries to trick you into sending money
to it, because you think that it will send you more money in return. But what
actually happens is that it tries to send you more money than it has: that
fails, but the contract keeps the money you sent it.

There is a list of such honeypots [on
GitHub](https://github.com/thec00n/smart-contract-honeypots), and you can
learn more about honeypots in [this
article](https://medium.com/@gerhard.wagner/the-phenomena-of-smart-contract-
honeypots-755c1f943f7b).

### Ponzi schemes¶

That’s an interesting one! Pakala was able to find quite a few “games”, that
are sorts of [Ponzi schemes](https://en.wikipedia.org/wiki/Ponzi_scheme).

The most common is a contract that keeps the address of the last person who
sent money to it. If there was nobody else who interacted with it after some
time (say, 24h) then that last person wins the amount present in the contract.

For my tool, this fits the bill: you send some money to it, and you come back
later enough to get all the money. That’s because I don’t model that other
people can interact with the contract in the meantime.

You can look at
[DonutChain](https://etherscan.io/address/0x972dc0ee6fc536378dde23e63a143cfd9995e18c#code)
for an example that won its owner 48 ETH, and that Pakala detected.

As a side note, there is also Fomo3D in the same vein (that contained millions
of dollars), but it’s much more complex. The last winner manipulated the
blockchain to be able to win, I suggest looking at [this
article](https://medium.com/coinmonks/how-the-winner-got-fomo3d-prize-a-
detailed-explanation-b30a69b7813f).

## Scavengers siphoning buggy contracts¶

Let’s go through the contracts previously mentioned and that are actually
vulnerable, but this time let’s look at what happened.

To investigate I simply used Etherscan, with both the “Transactions” and
“Internal Txns” tabs. This last tab allow you to see how the money got out of
the contract (transfers initiated by the contract itself).

>   * [HOTTO
> (old)](https://etherscan.io/address/0x612f1bdbe93523b7f5036efa87493b76341726e3):
> After the original creator got some funds out, it was hijacked by `0xacc…`
> who became the owner and [siphoned
> it](https://etherscan.io/tx/0x7ccd7a062ac661484f5c1c5d5847e6a3488d9338fc8fe90824cd175a66108c05)
> twice. Then `0x109…` also got some money out of it a few days later.
>
>   *
> [HitexToken](https://etherscan.io/address/0x102e3bcc2fb6a2fe4c1c4cf09021a5638008b721):
> This one is very similar. First `0xacc…`
> [siphoned](https://etherscan.io/tx/0x916201d86cbdf589efe1c8689cd342a795f57df5eced58cadedec2870e3f9e7b)
> the contract twice, then `0x109…` also [did
> it](https://etherscan.io/tx/0x1ae1fdce2fa54b8fc2cfff681ed7d5cee3f41e19c76e86849643ae7099c083d5)
> a few days later.
>
>   * [Mobile
> switching](https://etherscan.io/address/0xb2edc59fc6108884b7bde8d623887badf031fc4b):
> 60 days after the contract got created, we can see that `0x38a…` [siphoned
> it](https://etherscan.io/tx/0xd4c846809786ea527676e9c3663530683ce4ce5525c427fa8e4f31003208d1a7).
>
>   *
> [0x768f3b7538C0285142D86e0A692A086b0f091d3F](https://etherscan.io/address/0x768f3b7538c0285142d86e0a692a086b0f091d3f):
> 40 days after its creation, `0x38a…` sent [a
> transaction](https://etherscan.io/tx/0x26bb0e919ce6a9a4e15017d80dbc3cd2bd9951257657a61bb835f0dca9e464a8)
> that got the funds that were in the contract.
>
>   *
> [0xeBE6c7a839A660a0F04BdF6816e2eA182F5d542C](https://etherscan.io/address/0xeBE6c7a839A660a0F04BdF6816e2eA182F5d542C):
> By looking at the transaction history, we can see `0x38a…`
> [testing](https://etherscan.io/tx/0x2416a885f6aa568f8e739f2ca7fbd4412cc67f7c6b97935ee473c777c7518a72)
> the overflow bug by sending just 1 wei, then
> [trying](https://etherscan.io/tx/0x0c39aa028fbcee6642a893a548f99607f68005131bbe7507ac7f2574b94ca953)
> [to](https://etherscan.io/tx/0x34df9f0c78bb9a484f8cee198dea87b3e7a13ccf36fe4615fc5bcb3e5c4ab41c)
> [send](https://etherscan.io/tx/0x3aaf5a5a3937a49213e1ab83d46fe583fd16475319229d42771a64fc2e482661)
> the right amount, but putting it in decimal instead of hexadecimal (so
> nothing happen), and trying multiple times until they correctly convert to
> hexadecimal and are able to
> [siphon](https://etherscan.io/tx/0x57d89cb319c3ec2e9b7d478891fe9a23d4a173a03087cde1b13249e9a4eb5a57)
> the contract.
>
>

It seems like `0xacc…` was only exploiting token contracts with sources
available and wrongly-named constructors (and [did it a
lot](https://etherscan.io/txsInternal?a=0xacc6297e88d1de7d820f853d28453435dc000000)),
while `0x38a…` was more sophisticated: it exploited less trivial bugs and
didn’t need Solidity source code.

This is just the tip of the iceberg, but as you can see there are a few
addresses belonging to scavengers that actively exploit bugs to siphon
contracts.

## More?¶

The contracts mentioned here were just examples of things I found, but there
is **much more**. I started a [Twitter
account](https://twitter.com/palkeo_eth) to publish more of my findings, for
people who are interested.

Also, if you are interested by the subject I suggest looking at
[Pakala](pakala.html), the tool I developed for that.

If you have any question on this article, please contact me: `ethereum at
palkeo dot com`. I’m also available for contracting in that field.

Previous: [ Pakala: yet another EVM symbolic execution tool ](pakala.html)
Next: [ Analyzing suspicious smart contract vacuuming ](stolen_ether.html)

### [palkeo](../../index.html)

  * [Projects](../index.html)
  * [Blog articles](../../blog/index.html)
  * [Links](http://links.palkeo.com)
  * [Repository](http://repo.palkeo.com/)
  * [About](../../about.html)

##  05 December 2018

  * Language: [English](../../blog/language/english.html)
  * Tags:  [ethereum](../../blog/tag/ethereum.html) [pakala](../../blog/tag/pakala.html)

### [Table of Contents](../../index.html)

  * How to steal Ethers: scanning for vulnerable contracts
    * Introduction
      * Smart contracts
      * Symbolic execution
      * Bugs we are looking for
      * Tell me more!
    * Tooling
    * Vulnerable contracts found
      * Wrongly-named constructors
      * Free withdrawal
      * Honeypots
      * Ponzi schemes
    * Scavengers siphoning buggy contracts
    * More?

### Related Topics

  * [Projects](../index.html)
    * [Ethereum: hunting for buggy smart contracts](index.html)
      * Previous: [Analyzing suspicious smart contract vacuuming](stolen_ether.html "previous chapter")
      * Next: [Pakala: yet another EVM symbolic execution tool](pakala.html "next chapter")

(C)2020, palkeo.

