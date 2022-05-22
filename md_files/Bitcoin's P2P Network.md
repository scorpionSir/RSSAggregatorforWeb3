[ NAKAMOTO ](https://nakamoto.com)

  * [Home](https://nakamoto.com/)
  * [Twitter](https://twitter.com/nakamoto)
  * [Contribute](https://nakamoto.com/contribute/)
  * [About](https://nakamoto.com/about/)

__

__

# Bitcoin's P2P Network

Dec 29, 2019  8 min read  [Haseeb Qureshi](/author/haseeb/ "Haseeb Qureshi")

[ ![Bitcoin's P2P
Network](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)
](/bitcoins-p2p-network/)

We've looked at gossip protocols in the abstract. It's now time to apply those
abstractions to Bitcoin's own P2P network.

At a high level, almost all cryptocurrencies inherit the same P2P network
design from Bitcoin. With Gnutella as background, you should now be fully
equipped to understand Bitcoin's networking layer. It's really quite similar
to Gnutella, with a few augmentations that we'll cover in this lesson.

### Entering the network

So far we've analyzed gossip networks at steady state. But how does one
actually _join_ a gossip network? Do you just randomly query nodes on the
Internet until you find someone running the right software? (Thankfully, no.)

Every P2P protocol requires an **bootstrap node** to usher you into the
network and help you initialize your peer list. This bootstrap node is your
entrance point into the P2P network, from which point you can then organically
find new peers.

![](https://nakamoto.com/content/images/2020/01/introducer-optimized-1.gif)

Of course, the danger with a bootstrap node is that if it is not
authenticated, it could be malicious and perform a [man-in-the-
middle](https://en.wikipedia.org/wiki/Man-in-the-middle_attack) or [eclipse
attack](https://www.usenix.org/system/files/conference/usenixsecurity15/sec15-paper-
heilman.pdf).

In Bitcoin Core, the canonical Bitcoin implementation, these bootstrap nodes
are hard-coded as trusted DNS servers maintained by the core developers.

    
    
    // From: https://github.com/bitcoin/bitcoin/blob/master/src/chainparams.cpp
    
    vSeeds.emplace_back("seed.bitcoin.sipa.be"); // Pieter Wuille, only supports x1, x5, x9, and xd
    vSeeds.emplace_back("dnsseed.bluematt.me"); // Matt Corallo, only supports x9
    vSeeds.emplace_back("dnsseed.bitcoin.dashjr.org"); // Luke Dashjr
    vSeeds.emplace_back("seed.bitcoinstats.com"); // Christian Decker, supports x1 - xf
    vSeeds.emplace_back("seed.bitcoin.jonasschnelli.ch"); // Jonas Schnelli, only supports x1, x5, x9, and xd
    vSeeds.emplace_back("seed.btc.petertodd.org"); // Peter Todd, only supports x1, x5, x9, and xd
    vSeeds.emplace_back("seed.bitcoin.sprovoost.nl"); // Sjors Provoost
    vSeeds.emplace_back("dnsseed.emzy.de"); // Stephan Oeste

You can retrieve an initial peer list yourself by using `dig` to perform a DNS
query to one of these bootstrap nodes through a UNIX command line.

    
    
    $ dig seed.bitcoin.sipa.be
    
    ; <<>> DiG 9.10.6 <<>> seed.bitcoin.sipa.be
    ;; global options: +cmd
    ;; Got answer:
    ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 64217
    ;; flags: qr rd ra; QUERY: 1, ANSWER: 25, AUTHORITY: 0, ADDITIONAL: 1
    
    ;; ANSWER SECTION:
    seed.bitcoin.sipa.be.    3337    IN    A    214.99.158.195
    seed.bitcoin.sipa.be.    3337    IN    A    202.230.171.5
    seed.bitcoin.sipa.be.    3337    IN    A    20.79.84.168
    seed.bitcoin.sipa.be.    3337    IN    A    91.173.63.7
    seed.bitcoin.sipa.be.    3337    IN    A    45.74.113.110
    seed.bitcoin.sipa.be.    3337    IN    A    168.160.113.156
    seed.bitcoin.sipa.be.    3337    IN    A    29.239.106.205
    seed.bitcoin.sipa.be.    3337    IN    A    25.142.230.178
    seed.bitcoin.sipa.be.    3337    IN    A    146.73.72.54
    # ... and so on.

As an interesting point of history, the first version of Bitcoin bootstrapped
its peer list by finding peers through IRC channels. Each Bitcoin node came
bundled with a [small IRC
client](https://github.com/bitcoin/bitcoin/blob/847593228de8634bf6ef5933a474c7e63be59146/src/irc.cpp)
that on first boot would join a random channel between `bitcoin00` and
`bitcoin99`. If it found other IPs in these channels, it'd try to connect to
them until it filled up its initial peer list.

This form of bootstrapping was [eventually
abandoned](https://github.com/bitcoin/bitcoin/commit/c2efd981aa14e94cce4a0a888b6ee1f4e4347924)
after the IRC server (LFNet) shut down, which temporarily bricked Bitcoin's
peer discovery procedure. Since then, Bitcoin has relied on this DNS-based
system for bootstrapping.

Initial peer discovery is an inherent chokepoint for all P2P networks. But
after that phase, a node is free to populate its peer table with whichever
peers it chooses.

### Spam protection in Bitcoin

You'll recall that one of the weaknesses of P2P protocols is quality control.
How do you stop bad actors from spamming the network to death? We hand-waved
this earlier. Turns out, Bitcoin uses a reputation system to deal with this
problem, [implemented in 2011 by Gavin
Andresen](https://github.com/bitcoin/bitcoin/pull/517).

Say you're a Bitcoin node and you've just bootstrapped your peer list. You
start by assigning each of your peers a spam score of 0. Any time that peer
misbehaves toward you, their spam score goes up. Think of this like a P2P
criminal record—in the absence of a central judicial system, everyone in the
network has to keep tabs on everyone else's behavior.

Small infractions, such as failing to send a `version` message in an initial
handshake, will increase your score by 1 point. More serious
[DoS](https://en.wikipedia.org/wiki/Denial-of-service_attack) attempts, such
as sending more than 50,000 ids in an `INV` (inventory) message, will get you
dinged 20 points.

Once a peer accumulates 100 points, your client automatically shadowbans them
for 24 hours and stops gossiping to them. These spam scores are not actually
propagated in the protocol across peers. (Why do you think they're not?) But
even so, this system serves as a decent defense against misbehaving nodes.

### Network-level privacy

P2P networks come with intrinsic privacy tradeoffs. Think about it: every
message in the network is being shouted out in the open, and anyone is free to
observe all the messages that pass by. For a financial network like Bitcoin,
this is lack of privacy isn't exactly ideal.

Bitcoin affords _some_ financial privacy thanks to its pseudonymity. If the
world knows that the account `1G9HFbCRikgPpQboURsdqszy9HbKtvceZ5` has spent
0.25 BTC at a sketchy overseas pharmacy, maybe I'm okay. But if someone can
figure out that my IP that originally sent the signed transaction, suddenly my
privacy is compromised.

This sucks. P2P networks are resistant to censorship, _but they are not at all
resistant to surveillance_.

![](https://nakamoto.com/content/images/2020/01/image-94.png)Concurrent peers
in the Bitcoin network. Credit: <https://bitnodes.earn.com/>

Let's sketch out how a sophisticated eavesdropper might surveil the network.

By default, a normal Bitcoin nodes make 8 outbound connections to other peers.
However, the Bitcoin client is open source, so anyone is free to modify their
client to connect to as many peers as they want. There are about 10,000 live
peers in the Bitcoin Network right now, and in principle one could connect to
all of them. This would make you a **supernode**.

With a supernode, you could keep track of every message sent anywhere in the
network and reconstruct the history of all messages from a god's-eye view.
This would essentially let you figure out which addresses corresponded to
which IPs and deanonymize Bitcoin transactions.

![](https://nakamoto.com/content/images/2020/01/gossip-propagation-1.gif)A
supernode could reconstruct the flow of messages after the fact. Credit:
Kauri.io

Gossip propagation is not designed to maintain privacy. Remember, the moment
after a message is received, each node immediately floods it out to all of
their outgoing peers. This leaves an obvious trace of where each message
started. Even if a passive observer were connected to just 50% of the network,
they'd be clearly see the "message wave" emanating from the sender.

In 2015, Bitcoin altered the way that it propagated gossip messages to achieve
better privacy. It now uses a method called **diffusion**. In diffusion,
instead of immediately flooding to each peer, the client waits a random
exponential delay before gossiping to each of its peers. This has the effect
of obscuring the P2P message graph, making it harder to observe where the
"message wave" originated from.

You can sketch it in code like this:

    
    
    def gossip(msg):
    	for peer in peers:
    		schedule_send(peer, msg, wait=np.random.exponential(1.0 / theta))

![](https://nakamoto.com/content/images/2020/01/diffusion-optimized-1.gif)

Even with this, however, privacy on Bitcoin's networking layer is far from
perfect. Diffusion still leaks quite a bit of information to a passive
adversary. Furthermore, P2P messages are not bilaterally encrypted, so passive
packet sniffers can easily snoop on any Bitcoin traffic in cleartext.

There's a lot of work still to be done on improving Bitcoin's network-level
privacy. Some privacy-conscious users prefer Bitcoin over
[Tor](https://www.torproject.org/) for network privacy, but [even that comes
with problems](https://arxiv.org/abs/1410.6079).

Recently, researchers at CMU came up with an improvement over diffusion known
as **Dandelion Protocol** that provides better network-level privacy
guarantees.

![](https://nakamoto.com/content/images/2020/03/dandelion.gif)Dandelion
propagation. Credit: [Jake Stutzman](https://medium.com/@jstutzman)

In Dandelion protocol, every transaction broadcast starts with a secret game
of telephone. The originator will whisper their transaction to just one peer,
who whispers it to one other peer, and so on in a chain. After a random number
of hops, the final peer will gossip out the transaction just as in Bitcoin.
But this peer is so far removed from the originator, for any observer it’s
impossible to tell who the chain started with.

This is much more effective for obfuscating the originator's IP, but it comes
at the cost of slower message propagation. Dandelion is now being considered
as a possible augmentation to Bitcoin's gossip mechanism, and has already been
implemented in [other
cryptocurrencies](https://www.monerooutreach.org/stories/dandelion.html).
We've provided more resources on Dandelion in the additional reading.

### Life in a P2P Network

You should now have a better mental model of how messages propagate in
cryptocurrency networks. Due to their gossip architectures, cryptocurrencies
are  
"eventually consistent"—they don't provide any hard guarantees about when your
message will be seen by the rest of the network. Furthermore, not all nodes
will see the same state at the same time.

![](https://nakamoto.com/content/images/2020/01/image-96.png)How long it takes
for 50% (orange) or 90% (blue) of the network to receive the latest Bitcoin
block. Credit: [DSN Group at the Karlsruhe Institute of
Technology](https://dsn.tm.kit.edu/bitcoin/index.html)

When these networks are at scale, messages can propagate quite slowly. For
Bitcoin, it used to take more than 30 seconds for 90% of the network to
receive the latest block! Today, it takes a few seconds until the entire
network synchronizes on the latest block. (Miners see new blocks much faster,
which we'll discuss later when we explore Bitcoin mining.)

This concludes our exploration of Bitcoin's networking layer. By now you
should have an intuition of how gossip protocols work and what makes them so
robust at scale. You also should understand why Satoshi chose to design the
Bitcoin network with a P2P architecture.

With that as a foundation, in the next module we will explore consensus—first,
we'll study its classical origins, leading up to Satoshi's fundamental
breakthrough which made Bitcoin possible.

### Assignment

[Take this quiz to test your learning](https://forms.gle/YAWwFUmgkhKapxDE9).
Once you've completed it, it's time to move on.

### Additional Reading

  * [Bitcoin Core 0.11: P2P Network](https://en.bitcoin.it/wiki/Bitcoin_Core_0.11_\(ch_4\):_P2P_Network), a Bitcoin Wiki walkthrough of Bitcoin Core's P2P networking stack (2018)
  * [Anonymity Properties of the Bitcoin P2P Network](https://arxiv.org/pdf/1703.08761.pdf), showing how passive observers can use statistical techniques to deanonymize Bitcoin transactions by monitoring P2P traffic, by Giulia Fanti and Pramod Viswanath (2017)
  * [The Dandelion Protocol](https://www.youtube.com/watch?v=SrE6KdBgI1o) (video), a message propagation technique with stronger anonymity properties, presented by Giulia Fanti (2018)

[ Previous Gnutella: an Intro to Gossip ](https://nakamoto.com/gnutella/)

If you've gotten this far, great work! The next chapter of the course is
coming soon. And if you want me to finish it faster, please [yell at
me](https://twitter.com/hosseeb) on Twitter, and my deep-seated fear of public
criticism down will drive me closer to madness. ᕕ( ᐛ )ᕗ

[__](https://www.facebook.com/sharer.php?u=https://nakamoto.com/bitcoins-p2p-network/)[__](https://twitter.com/intent/tweet?url=https://nakamoto.com/bitcoins-p2p-network/&text=Bitcoin's%20P2P%20Network)[__](https://pinterest.com/pin/create/button/?url=https://nakamoto.com/bitcoins-p2p-network/&media=&description=Bitcoin's%20P2P%20Network)[__](https://www.linkedin.com/shareArticle?mini=true&url=https://nakamoto.com/bitcoins-p2p-network/&title=Bitcoin's%20P2P%20Network)[__](https://reddit.com/submit?url=https://nakamoto.com/bitcoins-p2p-network/&title=Bitcoin's%20P2P%20Network)[__](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https://nakamoto.com/bitcoins-p2p-network/&title=Bitcoin's%20P2P%20Network)[__](http://vk.com/share.php?url=https://nakamoto.com/bitcoins-p2p-network/&title=Bitcoin's%20P2P%20Network)[__](https://getpocket.com/edit?url=https://nakamoto.com/bitcoins-p2p-network/)[__](https://t.me/share/url?url=https://nakamoto.com/bitcoins-p2p-network/&text=Bitcoin's%20P2P%20Network)

![Haseeb
Qureshi](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

#### Haseeb Qureshi

[Website](https://haseebq.com) [Twitter](https://twitter.com/@hosseeb) [More
posts](/author/haseeb/)

Managing partner at Dragonfly Capital. Formerly: partner at Metastable
Capital, software engineer at Airbnb and Earn.com. Effective altruist, writer,
educator.

__San Francisco

[__Previous Post](/gnutella/)

[Next Post __](/zcash-the-https-of-blockchains/)

### You might also like...

[ ![What will happen to cryptocurrency in the
2020s?](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)
](/crypto-in-the-2020s/)

##  [What will happen to cryptocurrency in the 2020s?](/crypto-in-the-2020s/)

Jan 5, 2020  7 min read

[ ![Gnutella: an Intro to
Gossip](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)
](/gnutella/)

##  [Gnutella: an Intro to Gossip](/gnutella/)

Dec 29, 2019  11 min read

[ ![P2P
Networking](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)
](/p2p-networking/)

##  [P2P Networking](/p2p-networking/)

Dec 29, 2019  9 min read

Please enable JavaScript to view the [comments powered by
Disqus.](https://disqus.com/?ref_noscript)

[ NAKAMOTO ](https://nakamoto.com)

__

