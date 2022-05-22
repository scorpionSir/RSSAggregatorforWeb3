[ NAKAMOTO ](https://nakamoto.com)

  * [Home](https://nakamoto.com/)
  * [Twitter](https://twitter.com/nakamoto)
  * [Contribute](https://nakamoto.com/contribute/)
  * [About](https://nakamoto.com/about/)

__

__

# Zcash, the HTTPS of Blockchains

Jan 2, 2020  5 min read  [Zooko Wilcox](/author/zooko/ "Zooko Wilcox")[Josh
Swihart](/author/jswihart/ "Josh Swihart")

[ ![Zcash, the HTTPS of
Blockchains](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)
](/zcash-the-https-of-blockchains/)

There is no privacy without financial privacy. The books you've bought, the
places you've been, the people you've been with – all of this and more can be
deciphered from a list of receipts. Yet right now, public blockchains like
Bitcoin or Ethereum record information of this kind about you for anyone who
looks at it — today or years from now.

In the past, we had a similar problem on the internet, where users were
sending unencrypted data back and forth, unwittingly exposing themselves to
eavesdroppers and identity thieves. The solution then was an encrypted web-
browsing protocol for the public internet called HTTPS. We've developed a
conceptually similar solution today for encrypted transactions on a public
blockchain, called Zcash. Let's review the parallels, and the implications for
financial privacy.

## From HTTP to HTTPS

What would happen if you sent your credit card information over the internet
without encrypting it? It's quite possible that your information would be
stolen and used by someone nefarious. Thieves are constantly looking to sniff
out and capture unencrypted information as it moves from computer to computer,
looking for credit card numbers and bank account passwords.

But sending unencrypted information like this in so-called _clear text_ was
actually a common activity in the [early
days](https://en.wikipedia.org/wiki/History_of_the_Internet#ARPANET) of the
internet. That's because when the internet started, it was mostly populated by
academics. It was a _trusted network_ where most people knew each other and
wouldn't misbehave. Thus, when Tim Berners-Lee
[invented](https://webfoundation.org/about/vision/history-of-the-web/) the
World Wide Web and the corresponding [HTTP](https://developer.mozilla.org/en-
US/docs/Web/HTTP/Overview) protocol for reading web pages, he didn't design it
for an adversarial environment. He assumed that other WWW users were friendly
academics, like himself. And for a time he was right.

But in [March
1991](https://www.nsf.gov/od/lpa/nsf50/nsfoutreach/htm/n50_z2/pages_z3/28_pg.htm)
the NSF altered its acceptable use policy to finally allow commercial traffic
on the internet, which began a period of [explosive
growth](https://upload.wikimedia.org/wikipedia/commons/6/61/NSFNETTrafficGraph-
June1994.jpg?1578024500942) that we're still living through today. And with
that growth came (a) money and (b) problems. In particular, once people
started trying to use the internet for commerce, thieves arose that would try
to listen to the unencrypted HTTP traffic for credit card numbers that were
printed in cleartext.

The solution turned out to be encryption, though this was initially
controversial. In the early days of the Internet, [the NSA and
others](https://youtu.be/H9Cu36Qj3dQ?t=2410) were concerned about the the
potential use of cryptography by terrorists and criminals. This controversy
raged for several years and was known as the [First Crypto
War](https://www.schneier.com/blog/archives/2015/06/history_of_the_.html).

A key moment occurred in 1994, when Netscape invented an encrypted web-
browsing protocol called [HTTPS](https://en.wikipedia.org/wiki/HTTPS), which
enabled e-commerce and the modern WWW as we know it. As an example, this is
what sending your credit card information over the Internet with and without
HTTPS would look like to a would-be thief:

![](https://lh4.googleusercontent.com/W4e24NTk68zzoekTZsX-
vbcGqXBHrXGmr_gstSc7NUoGo2Ouwc-
IKJ9AFpU0dbx1nSvLnJfhg65f2ltz9tH2XQek7w-lqXacEMRvxGkP3DwIqNHAvJqGvs-Y4ymQ1BcvO-
vxos1Z)

Once it became obvious that encryption was actually necessary for the safety
of both individuals and businesses, the tide began to turn in the First Crypto
War. Eventually even the NSA came to recognize that public access to
encryption was far more beneficial than harmful.

![](https://nakamoto.com/content/images/2020/01/image-7.png)

Today, HTTPS is a requirement for transmitting data between computers on the
internet. You used to see it in green lock symbols in web browsers. Nowadays
it's so ubiquitous that the _[absence](https://www.cnet.com/news/say-good-bye-
to-that-green-secure-lock-on-google-chrome/)_ of HTTPs is cause for concern!
Indeed, HTTPS is actually mandatory for [all US government
agencies](https://https.cio.gov/), including those which were initially
against public access to encryption.

![](https://nakamoto.com/content/images/2020/01/image-8.png)

Ultimately, the technology won because the World Wide Web was being used for
commerce, and the only way to support safe and secure commerce on the Web was
through encryption.

## From blockchain to Zcash

That brief history lesson brings us to the present day. While HTTPS is now
omnipresent, there's a new problem with financial privacy, and it's
paradoxically present in cryptocurrencies – which the average user might be
forgiven for thinking are naturally encrypted, but which actually leak
financial information on the public internet.

The reason is that cryptocurrencies like Bitcoin and Ethereum work by
_broadcasting_ transactions and recording them on a world-readable public
blockchain. Anyone that knows your address can see your balance, with whom you
are transacting, the amount, date and time of all your transactions, and the
frequency of transactions between you and others. Like the time before HTTPS,
anyone can read anything.

To make this concrete, consider the relatively harmless case of crypto
developer Con Kolivas, who accepted public donations for his open source work
through the Bitcoin address
[15qSxP1SQcUX3o4nhkfdbgyoWEFMomJ4rZ](https://github.com/ckolivas/cgminer/blob/master/AUTHORS).
His name is now mapped to that address, and recorded in block explorers like
BTC.com. As [shown below](https://btc.com/15qSxP1SQcUX3o4nhkfdbgyoWEFMomJ4rZ),
the total amount Kolivas received in donations (703.51246006 BTC), the exact
amount sent in each donation, and the number and timestamps of all donations
are all permanently world-readable.

![](https://nakamoto.com/content/images/2020/01/image-10.png)

This is a relatively harmless case because Kolivas is a sophisticated user who
was publicly soliciting donations. He knew that his address would be public on
the internet and mapped to his name. However, consumers and businesses cannot
allow all of their personal and commercial transactions to be publicly
analyzable in such a manner.

That's why
[Zcash](https://www.wnycstudios.org/podcasts/radiolab/articles/ceremony) was
invented in 2016. Zcash uses a cryptographic breakthrough called [zero-
knowledge proofs](https://www.wired.com/story/zero-knowledge-proofs/) layered
on top of the Bitcoin protocol, to provide a means for nodes on the network to
verify that a transaction is valid – without giving them any information about
the transaction, including sender, receiver, or transaction amount. If we
think of a blockchain as a public ledger, fully shielded Zcash transactions
don't print the from or to addresses of each transaction, or the amounts.

![](https://lh5.googleusercontent.com/NrcxS5eLgMkN9CrkpRHicQ39vyjNiy_NJNSalat7bPIBT3Ac2SxN2UnOPnW7Jfee-
ZjINia0_YXzmVv4IzM9SxOfDRpj7WQzb3ra787XYzJylhdg5GU67x61XVXON12p6E7fsM52)

We can also understand the difference at the level of an individual's privacy
by comparing the [screenshot
below](https://btc.com/7c44e15103955780b4aaf825f0915f19edc114cc330f41b7279c5f03894aac70)
of a Bitcoin transaction going to Con Kolivas versus the more limited data
shown in a [fully
shielded](https://explorer.zcashfr.io/insight/tx/06e99f77c5c132dd81811eaadf614bb6c7447c4f61f54b67da60363cd2e062f8)
Zcash transaction.

![](https://nakamoto.com/content/images/2020/01/image-13.png)In a Bitcoin
transaction, the timestamp, amount, and the addresses of the senders and
receivers are public. In this example the name of the receiver is also
public.![](https://nakamoto.com/content/images/2020/01/Screenshot-2020-01-04-at-14.46.54.png)In
a fully shielded Zcash transaction, the timestamp is public, but no
information about sender, receiver, or amount is public.

This is why we think of Zcash as analogous to HTTPs. It's a privacy-preserving
digital currency on a public blockchain. Like HTTPS, fully shielded Zcash
transactions prevent eavesdropping and protect financial privacy. Compare the
figure below to the illustration above on HTTPS. In both cases, eavesdroppers
can no longer see the financial metadata associated with appropriately
encrypted transactions.

![](https://lh3.googleusercontent.com/xg-z-
SotwJ5MicfBoBhKjG08PafQw_4ewl9jAanQ5AcfkdirV8hwztlC5rGeaokh6tnmVTt5w6bqNxEKX90KADWNp4cCBtmlk0Uu_bmffmZIz1wXFINYaxGfHsd6yft8eZqBkxth)

Just as HTTPS became standard on the public internet to protect credit card
transactions, we believe strong encryption will in time become standard on
public blockchains to protect cryptocurrency transactions. Strong encryption
is necessary to protect individuals, businesses, and nations on an
increasingly hostile and invasive Internet. That's why we invented Zcash.

[__](https://www.facebook.com/sharer.php?u=https://nakamoto.com/zcash-the-
https-of-
blockchains/)[__](https://twitter.com/intent/tweet?url=https://nakamoto.com/zcash-
the-https-of-
blockchains/&text=Zcash%2C%20the%20HTTPS%20of%20Blockchains)[__](https://pinterest.com/pin/create/button/?url=https://nakamoto.com/zcash-
the-https-of-
blockchains/&media=&description=Zcash%2C%20the%20HTTPS%20of%20Blockchains)[__](https://www.linkedin.com/shareArticle?mini=true&url=https://nakamoto.com/zcash-
the-https-of-
blockchains/&title=Zcash%2C%20the%20HTTPS%20of%20Blockchains)[__](https://reddit.com/submit?url=https://nakamoto.com/zcash-
the-https-of-
blockchains/&title=Zcash%2C%20the%20HTTPS%20of%20Blockchains)[__](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https://nakamoto.com/zcash-
the-https-of-
blockchains/&title=Zcash%2C%20the%20HTTPS%20of%20Blockchains)[__](http://vk.com/share.php?url=https://nakamoto.com/zcash-
the-https-of-
blockchains/&title=Zcash%2C%20the%20HTTPS%20of%20Blockchains)[__](https://getpocket.com/edit?url=https://nakamoto.com/zcash-
the-https-of-
blockchains/)[__](https://t.me/share/url?url=https://nakamoto.com/zcash-the-
https-of-blockchains/&text=Zcash%2C%20the%20HTTPS%20of%20Blockchains)

![Zooko
Wilcox](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

#### Zooko Wilcox

[Website](https://z.cash/) [Twitter](https://twitter.com/@zooko) [More
posts](/author/zooko/)

Founder and CEO of the Electric Coin Company and co-inventor of Zcash.

![Josh
Swihart](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

#### Josh Swihart

[Website](https://z.cash/) [Twitter](https://twitter.com/@jswihart) [More
posts](/author/jswihart/)

Head of Growth at the Electric Coin Company, creators of Zcash.

[__Previous Post](/bitcoins-p2p-network/)

[Next Post __](/coinbases-pragmatic-crypto-culture/)

Please enable JavaScript to view the [comments powered by
Disqus.](https://disqus.com/?ref_noscript)

[ NAKAMOTO ](https://nakamoto.com)

__

