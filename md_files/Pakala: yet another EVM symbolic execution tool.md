# Pakala: yet another EVM symbolic execution tool¶

[![ilo Pakala li pakala e mani sona](../../_images/pakala-mani-
sona.svg.png)](https://www.jonathangabel.com/archive/2012/projects_t47.html)

Pakala is a tool for symbolic execution of EVM bytecode (like Manticore or
Mythril).

It is now available [on Github!](https://github.com/palkeo/pakala)

## Why another?¶

Mostly, because it’s a great way to learn how the EVM works, and because it
works differently than the other tools I know of so the coverage is slightly
different (see below).

Also, I decided not to do CFG analysis or anything, which makes it simple:
without tests, it’s only 2000 lines of code.

It basically looks for ways to get money out of the contract, into an address
the attacker controls. That’s the most obvious kind of vulnerability that
people would seek to exploit.

The goal during development was to apply these simple checks to all the
contracts in existence, with as little false positives as possible.

It led me to a string of interesting discoveries, that are the subject of
[another article](stealing_ether.html).

## What does it looks for?¶

Right now, there are only two built-in analyses:

>   * call `suicide()` to an user-controlled address.
>
>   * `send()` more ethers than the attacker sent.
>
>

Pakala can stack an arbitrary number of calls to the contract, to allow for
state-changing calls first, and then withdrawals.

## What makes it different¶

This tool operates at the level of EVM bytecode, and aims at being agnostic to
higher-level languages.

### Simple and clean¶

For simplicity, there is no CFG analysis or anything. It just execute the code
symbolically, in order.

Even if the code is far from perfect, it has been developed with readability
in mind, and ships with unit tests and integration tests scanning solidity
contracts.

There are approximately as many lines of code as there are lines of tests.

### Z3 abstraction layer¶

It uses Z3, but through Claripy, which is an abstraction layer that exposes a
nice interface, and does caching and black magic.

I also added a SHA3 layer on top of it, which does what’s needed to support
cryptographic hashes properly, without this detail leaking anywhere in the
code (thanks Johannes Krupp for your help on that!)

### False positive rate¶

The false positive rate should be very low.

From experience, the kind of false positives it will find are for contracts
that can be emptied but only after a certain time without any other address
interacting (which is not guaranteed to happen in real life…). That’s the case
for some games/ponzi-schemes similar to Fomo3D, where the last one to interact
wins.

### Two layers: finding executions and stacking them¶

Similarly to
[teEther](https://www.usenix.org/conference/usenixsecurity18/presentation/krupp),
it is made of two independent layers:

The first one executes a contract and tries to find a list of “outcomes”. An
outcome is a valid execution of the contract that led to a state change
(storage written, or money sent), associated to the precondition that needs to
be satisfied for this specific execution to trigger.

The second layer is able to tell whether an outcome is doing something bad,
corresponding to a vulnerability.

It can also stack multiple outcomes on top of each other, to simulate a
sequence of multiple calls to the contract. That means it’s able to detect
vulnerabilities that need more than one transaction (typically, changing the
owner, then calling an “ownerOnly” function).

This approach allows it to only execute the contract once, and then focus on
stacking the outcomes, which is pretty efficient. However, that means there is
no support for calling external contracts. It will never be able to find
reentrancy bugs either.

You can use it as a reverse engineering tool: by simply listing the outcomes
it is possible to get a good understanding of what the contract is doing.

### Difference with Mythril¶

Compared to Mythril, that’s also a symbolic execution tool developed in
Python: Mythril recursively calls other contracts and does everything in one
step.

Because Pakala has these two independent steps it doesn’t support calling
other contracts, but this has the upside of being able to build a list of
valid executions that the second step can stack. That’s much faster if you
want to go deeper in the number of transactions.

I made a solidity test suite with various simple contracts that are vulnerable
(`solidity_tests/`):

  * Pakala found bugs in: 12/12 (`python -m unittest discover solidity_tests/`)

  * Mythril found bugs in: 6/12 (`ulimit -Sv 5000000; for i in solidity_tests/*.sol; do echo $i && ../mythril/myth -mether_thief,suicide -x $i -t4 --execution-timeout 600; done`)

Obviously the test-cases are made to test what Pakala supports, so they are
biased: We don’t include contracts calling other contracts, for example.

Here we test things like being able to write to an arbitrary storage location
and overriding another variable, needing multiple transactions, mapping from
address to variables, integer overflows…

But this is to show the complementarity of the approach that Pakala uses. A
deeper comparison would be useful.

## Demo time¶

Previous: [ Syncing a Parity Archive Node: How-To ](parity_archive_node.html)
Next: [ How to steal Ethers: scanning for vulnerable contracts
](stealing_ether.html)

### [palkeo](../../index.html)

  * [Projects](../index.html)
  * [Blog articles](../../blog/index.html)
  * [Links](http://links.palkeo.com)
  * [Repository](http://repo.palkeo.com/)
  * [About](../../about.html)

##  04 December 2018

  * Language: [English](../../blog/language/english.html)
  * Tags:  [ethereum](../../blog/tag/ethereum.html) [pakala](../../blog/tag/pakala.html)

### [Table of Contents](../../index.html)

  * Pakala: yet another EVM symbolic execution tool
    * Why another?
    * What does it looks for?
    * What makes it different
      * Simple and clean
      * Z3 abstraction layer
      * False positive rate
      * Two layers: finding executions and stacking them
      * Difference with Mythril
    * Demo time

### Related Topics

  * [Projects](../index.html)
    * [Ethereum: hunting for buggy smart contracts](index.html)
      * Previous: [How to steal Ethers: scanning for vulnerable contracts](stealing_ether.html "previous chapter")
      * Next: [Syncing a Parity Archive Node: How-To](parity_archive_node.html "next chapter")

(C)2020, palkeo.

