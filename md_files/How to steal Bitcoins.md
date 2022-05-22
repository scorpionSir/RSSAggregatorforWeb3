# How to steal Bitcoins¶

Every Bitcoin address is based on a secret key, from which the public key
(associated to a Bitcoin address) is calculated. Once you have the private key
for an address, you have the control of that address and can use it to
transfer funds.

This secret key is a 32-bytes unsigned integer. You can generate a lot of
secret keys, calculate the public keys associated to them and see if they
contain bitcoins. If it’s the case, you can transfer the money to an address
you control, because you have the secret key.

Such an attack is completely infeasible, because the private key space is
really, really huge. There are
`115792089237316195423570985008687907853269984665640564039457584007913129639936`
secret keys available (1077).

Oh, and they are all listed on [directory.io](http://directory.io) ! Of
course, this website is [kind of a joke](http://directory.io/faq), and all is
calculated on the fly when you request a specific page. It also shows the
danger of entering your secret key on an unknown website, for example to see
if it was compromised…

However, we can bruteforce only a tiny fraction of this space, concentrating
on secret keys with some distinctive features. This is what I will explain.

## Private keys are numbers…¶

So, why not try really tiny numbers ?

I have made a script that tries every secret key, counting from 1. After some
seconds, I found dozens of already used addresses, with private key smaller
than 100 000 !

In particular, the
[1EHNa6Q4Jz2uvNExL497mE43ikXhwF6kZm](http://blockchain.info/address/1EHNa6Q4Jz2uvNExL497mE43ikXhwF6kZm)
address (corresponding to the private key 1) was already used quite a lot, as
4 bitcoins already flowed through it.

## Brainwallet¶

[Brainwallet](http://brainwallet.org) is a website that allow people to create
private keys from a passphrase. It calculates the private key from the sha256
of the passphrase.

By using a password dictionary, we can search for private keys corresponding
to classic password that were already used. A search allowed me to find nearly
10 000 addresses that have contained Bitcoins at some point in time ! I was
never able to find any address containing money, and nearly every time they
had contained only really small amounts of money, but here is an interesting
sample :

    
    
    asd - 1G4Mt5JLtrdj4hM6MkyaQpHmZzVoojLFX3
    cat - 162TRPRZvdgLVNksMoMyGJsYBfYtB4Q8tM
    hello - 1HoSFymoqteYrmmr7s3jDDqmggoxacbk37
    password - 16ga2uqnF1NqpAuQeeg7sTCAdtDUwDyJav
    test - 1HKqKTMpBTZZ8H5zcqYEWYBaaWELrDEXeE
    fuckyou - 1LdgTMX2MEqdfT3VcDpX4GyD1mqCP8LkYe
    1 - 12AKRNHpFhDSBDD9rSn74VAzZSL3774PxQ
    icecream - 1CwjHYsPUc4Du8dx7AkdBJj4ebWC8bxkF3
    alfanumerico - 19JsLFDRxuTsAjapE79FgoVNdNdB2hNU5M
    [empty string] - 1HZwkjkeaoZfTSaJxDw6aKkxp45agDiEzN
    correct horse battery staple - 1JwSSubhmg6iPtRjtyqhUYYH7bZg3Lfy1T
    

If we look at the history of transactions on these addresses we can see that
in a lot of cases, a few seconds after money was deposed in them, it was
withdrew to another account.

In particular, it was often sent to one of these accounts :

  * [1brain7kAZxPagLt2HRLxqyc3VgGSa1GR](https://blockchain.info/address/1brain7kAZxPagLt2HRLxqyc3VgGSa1GR)

  * [15LPodNPGv5qsKPc4PUfyeJKdDReWjCknS](https://blockchain.info/address/15LPodNPGv5qsKPc4PUfyeJKdDReWjCknS)

  * [1mineraceNChe36ftTXU5Y8EvypyM3iu8](https://blockchain.info/address/1mineraceNChe36ftTXU5Y8EvypyM3iu8)

We can see that the first address already stole 0.36 Bitcoins, 2 seconds after
they were transferred to the address corresponding to the key « alfanumerico »
! This address seems to contain more than 1 Bitcoin, probably stolen all
automatically… Notice that the address starts with « brain », maybe it could
have something to do with Brainwallet, no ?

Another interesting fact, the second address stole very tiny amounts of money
from classical addresses, and we can even see that a comment was left about
one of these transactions :

    
    
    Stop taking this dust! You must wait until there is more sent to complex ones! Set the trap...
    

A Bitcoin theft that left a comment to another, advising him to stop stealing
tiny amounts of money and wait for bigger amount on more difficult addresses…

## Technical considerations¶

To bruteforce Bitcoins like that, you need to find the address associated to a
private key, as fast as possible. But, you will also need to know if each of
the address was already used in a transaction.

For that, you will need to iterate trough the entire blockchain. You can then
fill a [Bloom filter](https://en.wikipedia.org/wiki/Bloom_filter) with every
address seen in it. Once it is built, you will be able to know if an address
was used in the network with a really small lookup time.

As we have seen, it seems that some people even built a gigantic database,
mapping from “classic” addresses to their associated private keys. They seems
to be able to steal money only seconds after it was deposited…

## Conclusion¶

Well, it seems that there is money to make, and here is the proof that some
people are already on it…

This also demonstrate that you can use a service like Brainwallet, but you
need to choose a really strong passphrase, that will resist bruteforce. If any
computer or any other human can think of it, you are doomed !

Instead of attacking every potential transaction that used a weak private key,
it’s also possible to focus on weak random number generators, or
implementation problems in [ECDSA](https://en.wikipedia.org/wiki/ECDSA). This
is also a reality, and you can check out [this blog
post](http://www.nilsschneider.net/2013/01/28/recovering-bitcoin-private-
keys.html) for more.

Previous: [ Pourquoi les nerds sont impopulaires ? ](../thoughts/nerds.html)
Next: [ List of quality games ](jeux.html)

### [palkeo](../index.html)

  * [Projects](../projets/index.html)
  * [Blog articles](index.html)
  * [Links](http://links.palkeo.com)
  * [Repository](http://repo.palkeo.com/)
  * [About](../about.html)

##  08 March 2014

  * Language: [English](language/english.html), [French](language/french.html)
  * Tag: [bitcoin](tag/bitcoin.html)

(C)2020, palkeo.

