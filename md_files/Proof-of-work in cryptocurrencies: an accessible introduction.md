Close

Menu

  * [About Us](https://blog.sigmaprime.io/pages/about-us.html)

[![Blog Logo](./imgs/blog/sigp-logo-black.png)](https://blog.sigmaprime.io/)
__Menu

# Proof-of-work in cryptocurrencies: an accessible introduction

[Paul Hauner](https://blog.sigmaprime.io/author/paul-hauner.html) | Wed 06
December 2017 Updated on Wed 06 December 2017 Estimated read time: 11 min

_This article provides an accessible explanation of the "proof-of-work"
consensus algorithm as used in Bitcoin, Ethereum and many other
cryptocurrencies. It does not assume expertise with computer science or
cryptography, however is targeted at a technical audience._

# Introduction

The Bitcoin protocol was first described by [Satoshi Nakamoto
(2008)](https://bitcoin.org/bitcoin.pdf). In 2009, the first implementation of
the Bitcoin protocol emerged as the ledger of the now US$276 bitcoin (BTC)
cryptocurrency (notice that the protocol has a capital "B" whilst the currency
does not). The bitcoin blockchain is a transaction ledger, where transactions
are ordered into blocks, and the blocks into a chain:

![Blockchain structure](/imgs/pow-intro/Blockchain---Copy-of-Page-1.svg)

Nakamoto was not the first to describe a blockchain; - [Haber and Stornetta
(1991)](https://link.springer.com/article/10.1007/BF00196791) described such a
concept more than fifteen years earlier. However, the Nakamoto paper was the
first to conceptualise a _distributed blockchain_ ; a blockchain which does
not rely upon a single organisation to store the chain, but instead relies
upon a network of individuals to share the chain with each other.

Prior to Nakamoto's paper, many of the technologies required for a distributed
blockchain already existed (e.g., peer-to-peer filesharing and cryptography).
The core innovation of the [Nakamoto paper](https://bitcoin.org/bitcoin.pdf)
was the introduction of a consensus mechanism which allowed a "decentralised"
network of distrusting peers to agree on a state of account balances. This
consensus mechanism has become known as Nakamoto consensus.

Nakamoto consensus is specific to bitcoin, however, it falls into a larger
category of _proof-of-work consensus_. Cryptocurrencies such as Ethereum,
Litecoin and Zcash all use a form of proof-of-work consensus and this article
will describe the concepts needed to understand the consensus mechanisms
behind these and many other cryptocurrencies.

For readability, we will use the term "cryptocurrency" as a generic term for
proof-of-work based cryptocurrencies, however, it is actually a misnomer as
there are cryptocurrencies which do not use proof-of-work (e.g., EOS, NXT,
Cardano).

# Why do cryptocurrencies need proof-of-work?

Cryptocurrencies allow anyone to anonymously produce blocks and extend their
currency ledger. This is fundamental to their ability to escape regulation and
government controls; stopping a cryptocurrency will be incredibly difficult if
anyone with a computer can anonymously produce a block.

This "open door" philosophy raises an obvious challenge: if anyone can extend
the ledger, what would stop the blockchain from growing at a rate equal to the
amount of people attempting to extend it? This is especially true considering
that the production of a new block (akin to a new page of a ledger) is
rewarded handsomely (bitcoin currently offers 12.5 BTC, which is worth
USD$235,000 at the time of writing).

Cryptocurrencies needed a _rate-limiting_ solution; a way to reduce the speed
at which the ledger can be extended. Proof-of-work is the solution to this
rate-limiting problem. It requires each extension of the ledger (block) to
have a "proof-of-work" which gets more difficult as production capacity
increases. In fact, proof-of-work ensures that the production of a new block
is _so_ difficult that the entire applied computing capacity of the world
(universe, even) cannot produce more than one block each ten minutes.

# What is a proof-of-work?

A proof-of-work is exactly as it sounds: a proof that some amount of work was
done. A large hole in the ground could serve as an easily-verifiable proof-of-
digging and a chalkboard full of words serves as a proof-of-writing. Both of
those activities required "work", so they're each a proof-of-work.

As cryptocurrencies are computer protocols, a proof of computational work is
required. Like the other examples, the proof needs to be "hard" to generate
and "easy" to validate. Such a proof scheme was first described by [Dwork and
Naor (1992)](http://www.hashcash.org/papers/pvp.pdf) to address email spam.
This proof scheme has two major properties, both of which we will explain in
this section; it is _probabilistic_ and it uses _cryptographic hashing
algorithms_.

## What is a probabilistic proof-of-work?

To explain a probabilistic proof-of-work we will use an analogy:

There is a black box with a button and a screen. When the button is pressed, a
random number between `1` and `100` is displayed on the screen. A validator,
Alice, hands the box to a worker, Bob, and stipulates that he may only return
the box when it displays a `1` or `2`. Given there is a `1` in `50` chance of
any button press resulting in a number in this range, Alice could assert that
Bob _probably_ had to press the button fifty times for the box to display a
`1` or `2`.

![The black box](/imgs/pow-intro/Blockchain---Page-2--1-.svg)

In the analogy, the number on the screen is an easily verifiable proof that
Bob has _probably_ done button-pushing work and the _difficulty_ of that work
was defined by Alice's range of acceptable numbers. If Alice were to accept
any number between `1` and `25`, Bob would only need to press the button four
times (on average) and the task would be less difficult.

Of course, there is a possibility that Bob "got lucky" and only pressed the
button once, but over multiple events we can have confidence that the number
of button pushes will average out to Alice's desired amount.

## What is cryptographic hashing?

A "hash function" is described by Wikipedia as "any function that can be used
to map data of arbitrary size to data of a fixed size". In this context, we're
looking at a function which takes data of any length and produces a very large
number (known as a digest or hash). The same data should always produce the
same digest, so this is why the data is said to be "mapped" to the digest
(hash). The diagram below is indicative of a 32 byte (256 bit) hashing
algorithm:

![Hashing](/imgs/pow-intro/Blockchain---Hash-w--Cat.svg)

There are many different hashing algorithms used by cryptocurrencies but
bitcoin uses an algorithm designed by the US National Security Agency (NSA)
named "SHA256". For this article we'll stick to bitcoin's proof-of-work using
SHA256 as it is the easiest to understand. Cryptocurrencies like Zcash have
more elaborate schemes designed to reduce the advantage of using specialised
hashing hardware, however, at their core they involve elaborate extensions to
bitcoin's original implementation.

Let's have a look at a couple of examples of using a SHA256 function (the
disgest is presented in
[hexadecimal)](https://en.wikipedia.org/wiki/Hexadecimal):

    
    
    // SHA256 hash functions
    sha256("1") = 6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b
    sha256("1") = 6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b
    sha256("2") = d4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35
    sha256("hello") = 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
    

There are a two particularly interesting things in these examples which are
useful for proof-of-work:

  * The same input always produces the same digest
  * A slight change in the input, causes a dramatic change in the digest

Furthermore, SHA256 also has a couple of more useful features which make it
specifically a _cryptographic_ hashing algorithm:

  * There is a single, most efficient way to generate the digest and that method is publicly known; **there are no shortcuts to generating hashes**.
  * It is very easy to calculate the digest when given the data, but infeasible to calculate the data when given the only the digest. In other words, **the function is "one-directional"** and it is effectively impossible to "reverse" the process and discover the input data for a given digest.
  * It is "collision resistant" - i.e., it is extraordinarily unlikely that different data will produce the same digest. This feature allows us to assume that the **digest of some data is a unique "fingerprint"** which describes only that data.

In a nutshell, cryptographic hashing algorithms are useful for proof-of-work
because they take some data and give us a special "random" number for that
data. The use of the word "random" here would certainly bother the computer
scientists in the room ([for good
reason](https://crypto.stackexchange.com/questions/12822/are-the-sha-family-
hash-outputs-practically-random)), however, the analogy is useful for our
understanding.

## Probabilistic proof-of-work using cryptographic hashing

To understand how we can use cryptographic hashing to produce a probabilistic
proof-of-work (like the black box example), let's consider a scenario where
there are two co-workers, Bob and Alice. Alice believes that Bob sends too
many message and wants disincentivise this by declaring that each message must
come with a "proof-of-work". Alice reasons that Bob will send less messages if
they are harder to send. This is what Alice's system is going to look like:

![The Bob filter](/imgs/pow-intro/Blockchain---Alice-Filter--2-.svg)

To establish the difficulty of the proof, Alice declares that Bob may only
send her messages if the first character of the hash of the message is `7`.
Knowing this, Bob starts the process by hashing his next message to Alice:

    
    
    sha256("Lunchtime?") = e0f3490b3575d929a17a0bdf3e4ebbbb6e72c0d480ab07c524a1aa38fc98d553
    

Unfortunately, this hash starts with an `e` and Alice will never accept it.
There needs to be some method to modify the hash without changing the message.
To achieve this, Alice defines a new message format with a _nonce_ ; a field
which may be modified for the sole purpose of affecting the hash:
`[<message>][<nonce>]`. Bob will need to modify the nonce until he can meet
Alice's requirement:

    
    
    // Bob's attempts:
    sha256("[Lunchtime?][1]") = c4bcc... # wrong
    sha256("[Lunchtime?][2]") = d16aa... # wrong
    ...
    sha256("[Lunchtime?][16]") = 74241... # correct!
    

Now Bob has done his work to discover a suitable nonce, he can send
`[Lunchtime?][16]` to Alice who can verify the proof-of-work with a single,
efficient round of the SHA256 hashing algorithm.

    
    
    // Alice's verification:
    sha256("[Lunchtime?][16]") = 74241d2b61c35fae1bec86a52fce8331b69d648e31398205d228abbaeebe129c
    

Whilst useful for demonstration, this analogy would not be a very practical
solution for Alice and Bob; Alice would need to write some software so that
Bob's messages are intercepted and checked before she is alerted (as manually
verifying his proofs is likely more effort than reading the message).
Furthermore, the requirement for Bob to produce a proof-of-work would add a
delay to message sending; not great for urgent messages.

Impracticalities aside, this analogy demonstrates that a cryptographic hashing
algorithm can be used to find an effectively random number for any piece of
data, and the uncertainty in that number can be used to generate a
probabilistic proof-of-work.

# How do cryptocurrencies use proof-of-work?

The use of proof-of-work in cryptocurrencies is fairly similar to our previous
example: a block is a set of data (with a nonce field) and the protocol only
considers a block to be valid if the digest from a specific hash function
falls within a acceptable range. The process of hashing blocks is called
"mining" and those who do it are called "miners".

![Block hashing](/imgs/pow-intro/Blockchain---Block-Hashing--1-.svg)

## Varying difficulty

In the Alice and Bob example, Alice's difficulty was statically defined. This
differs from cryptocurrencies where the difficulty can vary over time. The
difficulty varies in response to observed _block times_ (the time interval
between blocks). The exact method for calculating the difficulty can be
complex and is varied between cryptocurrencies, however, it can be summarised
in that "shorter block times result in an increased difficulty, and longer
block times result in a decreased difficulty". The end result being, as
discussed earlier, no matter how much hashing power is applied to discovering
blocks, the interval between blocks always approximates a target time (in
bitcoin this is 10 minutes, in Ethereum this is ~13 seconds).

## Competition

Miners are in competition with each other, each seeking to be the first to
discover a new block which passes the difficultly filter. Due to the
probabilistic nature of proof-of-work, whichever miner is able to hash the
most blocks is the most likely to discover a block. The motive to compete is a
chance at obtaining the block reward.

Those seeking to extend the blockchain (miners) will listen for transactions
on the network and collate those transations into a block, ensuring that those
transactions are valid (e.g., not double-spends) and that the block reward has
been directed to an address of its choosing. Just like Bob did in our example,
the miner will then start to produce a proof-of-work by performing successive
rounds of modifying the nonce and checking the hash digest.

If the miner discovers a valid nonce, it will broadcast the new block to the
network. Those miners who receive and verify that block will stop attempting
to produce an equivalent to that block. Instead, they will attempt to produce
a successor to that block - i.e., extend upon the newly created block. This is
the process that continues indefinitely and ensures the extension of the
ledger.

![Competition](/imgs/pow-intro/Blockchain---Competition.svg)

## The longest chain is the true chain

There does exist a scenario where two miners find a valid nonce at the same
time, but the ordering or set of transactions between the two is different.
This scenario is called a _fork_ ; there are two competing chains extending
from one block and the network must choose which chain to recognise as
canonical (the single source of truth). At this point in time, it is
impossible to know which chain is canonical and the miners must simply choose
one - likely whichever one happened to get to them first. Statistically,
whichever block is chosen by the majority of the hash power will be extended
first. As soon as one chain has more blocks than another, it becomes the
canonical chain and the other, shorter chain is discarded.

![Forks](/imgs/pow-intro/Blockchain---Forks.svg)

# The wider implications of proof-of-work

Proof-of-work is a novel mechanism for creating a distributed, permissionless
blockchain. However, it does not come without significant drawbacks, an
incredible amount of energy consumption and a power bias awarded to those with
the most hashing power.

The energy usage of bitcoin's proof-of-work is truly astounding and deeply
concerning; current [estimates](https://digiconomist.net/bitcoin-energy-
consumption) place its consumption at 0.14% of global energy usage and almost
equal to that of Morocco. Considering that bitcoin hashing is incentivised by
profit and performed anonymously, the responsible use of sustainable energy is
questionable.

The probabilistic and anonymous nature of proof-of-work necessarily means that
those with the most hashing power are the most likely to produce blocks. This
gives the cryptocurrency a dependence on those prominent miners as they have
the power to collude and [destabilise the
network](https://en.bitcoin.it/wiki/Majority_attack). As demonstrated in the
August 2017 [New York Agreement](https://medium.com/@DCGco/bitcoin-scaling-
agreement-at-consensus-2017-133521fe9a77), individuals and organisations who
control large portions of bitcoin's hashing power are awarded greater power
than those who simply seek to use the cryptocurrency to store and transfer
value. A scenario where control over the currency is biased towards those
incentivised by transaction fees and currency inflation surely grinds against
the founding principles of bitcoin.

Nevertheless, proof-of-work continues as the most prominent blockchain
cryptocurrency consensus mechanism. For bitcoin, it looks to continue
indefinitely. Ethereum, the second biggest cryptocurrency by market cap and
largest by transaction volume, has clear plans to move to the drastically more
energy-efficient and faster [proof-of-
stake](https://en.wikipedia.org/wiki/Proof-of-stake) consensus mechanism.

[ __Twitter ](https://twitter.com/share?text=Proof-of-work in
cryptocurrencies: an accessible
introduction&url=https://blog.sigmaprime.io/what-is-proof-of-work.html) [
__Facebook
](https://www.facebook.com/sharer/sharer.php?u=https://blog.sigmaprime.io/what-
is-proof-of-work.html) [ __Google+
](https://plus.google.com/share?url=https://blog.sigmaprime.io/what-is-proof-
of-work.html)

[ethereum](https://blog.sigmaprime.io/tag/ethereum.html)[blockchain](https://blog.sigmaprime.io/tag/blockchain.html)[cryptocurrency](https://blog.sigmaprime.io/tag/cryptocurrency.html)

![Paul Hauner](https://blog.sigmaprime.io/imgs/authors/ph-profile.jpg)

#### [Paul Hauner](https://blog.sigmaprime.io/author/paul-hauner.html)

Paul is a co-founder of Sigma Prime and a core team member of Sydney Homeless
Connect. He has a keen interest in consensus mechanisms and information
security. @paulhauner on Github.

__Sydney, Australia

