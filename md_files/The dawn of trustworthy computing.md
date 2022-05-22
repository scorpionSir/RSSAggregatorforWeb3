When we currently use a smart phone or a laptop on a cell network or the
Internet, the other end of these interactions typically run on other solo
computers, such as web servers. Practically all of these machines have
architectures that were designed to be controlled by a single person or a
hierarchy of people who know and trust each other. From the point of view of a
remote web or app user, these architectures are based on full trust in an
unknown "root" administrator, who can control everything that happens on the
server: they can read, alter, delete, or block any data on that computer at
will.  Even data sent encrypted over a network is eventually unencrypted and
ends up on a computer controlled in this total way. With current web services
we are fully trusting, in other words we are fully vulnerable to, the
computer, or more specifically the people who have access to that computer,
both insiders and hackers, to faithfully execute our orders, secure our
payments, and so on. If somebody on the other end wants to ignore or falsify
what you've instructed the web server to do, no strong security is stopping
them, only fallible and expensive human institutions which often stop at
national borders.  
  
The high vulnerability we have to web servers stands in sharp contrast to
traditional commercial protocols, such as ticket-selling at a movie theater,
that distribute a transaction so that no employee can steal money or resources
undetected. There is no "root administrator" at a movie theater who can pocket
your cash undetected.  Because, unlike a web server, these traditional
protocols, called financial controls, can securely handle cash, you didn't
have to fill out a form  to see a movie, shop for groceries, or conduct most
other kinds of every-day commerce. You just plunked down some coin and took
your stuff or your seat. Imperfect and slow as these processes often are (or
were), these analog or paper-based institutions often provided security,
financial control, and/or verifiability of fiduciary transactions in many ways
far superior to what is possible on web servers, at much less hassle and
privacy loss to customers. On the Internet, instead of securely and reliably
handing over cash and getting our goods or services, or at least a ticket, we
have to fill out forms and make ourselves vulnerable to identity theft in
order to participate in e-commerce, and it often is very difficult to
prohibitive to conduct many kinds of commerce, even purely online kinds,
across borders and other trust boundaries. Today's computers are not very
trustworthy, but they are so astronomically faster than humans at so many
important tasks that we use them heavily anyway. We reap the tremendous
benefits of computers and public networks at large costs of identity fraud and
other increasingly disastrous attacks.  
  
Recently developed and developing technology, often called "the block chain",
is starting to change this. A block chain computer is a virtual computer, a
computer in the cloud, shared across many traditional computers and protected
by cryptography and consensus technology. A Turing-complete block chain with
large state gives us this shared computer. Earlier efforts included state-
machine replication (see list of papers linked below).  QuixCoin is a recent
and Ethereum is a current project that has implemented such a scheme. These
block chain computers will allow us to put the most crucial parts of our
online protocols on a far more reliable and secure footing, and make possible
fiduciary interactions that we previously dared not do on a global network  
  
Much as pocket calculators pioneered an early era of limited personal
computing before the dawn of the general-purpose personal computer, Bitcoin
has pioneered the field of trustworthy computing with a partial block chain
computer. Bitcoin has implemented a currency in which someone in Zimbabwe can
pay somebody in Albania without any dependence on local institutions, and can
do a number of other interesting trust-minimized operations, including
multiple signature authority. But the limits of Bitcoin's language and its
tiny memory mean it can't be used for most other fiduciary applications, the
most obvious example being risk pools that share collateral across a pool of
financial instruments.  
  
A block-chain computer, in sharp contrast to a web server, is shared across
many such traditional computers controlled by dozens to thousands of people.
By its very design each computer checks each other's work, and thus a block
chain computer reliably and securely executes our instructions up to the
security limits of block chain technology, which is known formally as
anonymous and probabilistic Byzantine consensus (sometimes also called
Nakamoto  consensus).  The most famous security limit is the much-discussed
"51% attack".  We won't discuss this limit the underlying technology further
here, other than saying that the oft-used word "trustless" is exaggerated
shorthand for the more accurate mouthful "trust-minimized", which I will use
here.  "Trust" used in this context means the need to trust remote strangers,
and thus be vulnerable to them.  
  
Trust-minimized code means you can trust the code without trusting the owners
of any particular remote computer. A smart phone user in Albania can use the
block chain to interact with a computer controlled by somebody in Zimbabwe,
and they don't have to know or trust each other in any way, nor do they need
to depend on the institutions of either's countries, for the underlying block
chain computer to run its code securely and reliably. Regardless of where any
of the computers or their owners are, the block chain computer they share will
execute as reliably and securely as consensus technology allows, up to the
aforementioned limits. This is an extremely high level of reliability, and a
very high level of security, compared to web server technology.  
  
Instead of the cashier and ticket-ripper of the movie theater, the block chain
consists of thousands of computers that can process digital tickets, money,
and many other fiduciary objects in digital form.  Think of thousands of
robots wearing green eye shades, all checking each other's accounting.
Individually the robots (or their owners) are not very trustworthy, but
collectively, coordinated by mathematics, they produce results of high
reliability and security.  
  
Often block chain proponents talk about the "decentralized" block chain versus
the "centralized" web or centralized institutions. It's actually the protocol
(Nakamoto consensus, which is highly distributed) combined with strong
cryptography, rather than just decentralization _per se_ , that is the source
of the far higher reliability and and much lower vulnerability of block
chains. The cryptography provides an unforgeable chain of evidence for all
transactions and other data uploaded to the block chain. Many other
decentralized or peer-to-peer (P2P) technologies do not provide anything close
to the security and reliability provided by a block chain protected by full
Byzantine or Nakamoto consensus and cryptographic hash chains, but deceptively
style themselves as block chains or cryptocurrency.  
  
A big drawback is that our online and distributed block chain computer is much
slower and more costly than a web server: by one very rough estimate, about
10,000 times slower and more costly, or about the same as it cost to run a
program on a normal computer in 1985. For this reason, we only run on the
block chain that portion of an application that needs to be the most reliable
and secure: what I call fiduciary code. Since the costs of human ("wet")
problems caused by the unreliability and insecurity of web servers running
fiduciary code are often far higher than the extra hardware needed to run
block chain code, when web server reliability and security falls short, as it
often does for fiduciary computations such as payments and financial
contracts, it will often make more sense  to run that code on the block chain
than to run it less reliably and securely on a web server. Even better, the
block chain makes possible new fiduciary-intensive applications, such as
posting raw money itself to the Internet, securely and reliably accessible
anywhere on the globe -  apps that we would never dare do with a web server.  
  
What kinds of fiduciary code can we run?  We are still thinking up new
applications and the categories will be in flux, but a very productive
approach is to think of fiduciary applications by analogy to traditional legal
code that governs traditional fiduciary institutions. Fiduciary code will
often execute some of the functions traditionally thought of as the role of
commercial law or security, but with software that securely and reliably spans
the global regardless of traditional jurisdiction. Thus:  
  
* Property titles (registered assets), where the on-chain registry is either the legally official registry for off-chain assets or controls on-chain ones, thus providing reliable and secure custody of them. One can think of a cryptocurrency such as Bitcoin as property titles (or at least custody enforced by the block chain consensus protocol) to bits recognized as being a fixed portion of a currency, or as controlling unforgeably costly bits, or both. Block chains could also control hardware which controls the function of and access to physical property.  
  
* Smart contracts: here users (typically two of them) agree via user interface to execute block chain code, which may include transfer of money and other chain-titled assets at various times or under various conditions, transfer and verification of other kinds of information, and other combinations of wet or traditional (off-chain) and dry (on-chain) performance. A block chain can hold cryptocurrency as collateral (like an escrow) which incentivizes off-chain performance that can be verified on-chain, by the parties or by third parties. A full block chain computer can pool on-chain assets into a single chain-controlled risk pool spread among many similar financial contracts, reducing the amount of collateral that needs to be stored on-chain while minimizing the need for off-chain collateral calls. The block chain can also make the search, negotiation, and verification phases of contracting more reliable and secure. With on-chain smart contracts we will be able to buy and sell many online services and financial instruments by button and slider instead of by laboriously filling out forms that disclose our private information.  
  
* On-chain treasuries, trusts, and similar, where money lives on the block chain and is controlled by multiple signature ("multisig") authority.  Putting a treasury with signature authority on a block chain computer is low-hanging fruit, but is often tied to more speculative efforts under the label "distributed autonomous organization (DAO)", which may include voting shares and other mechanisms to control the treasury like a corporation or other kind of of organization.  
  
I hope to discuss these block chain applications, especially smart contracts,
in future posts. While there is much futurism in many block chain discussions,
including many trying to solve problems that aren't actually solved by the
block chain, I will generally stick to low-hanging fruit that could be
usefully implemented on Quixcoin, Ethereum, or similar technology in the near
future, often interfacing to still necessary parts of traditional protocols
and institutions rather than trying to reinvent and replace them in whole.  
  

### References

[Here](http://bitstein.org/blog/nick-szabo-the-computer-science-of-crypto-
currency/) is a list of basic computer science papers describing the
technology of block chains (including cryptocurrencies).  
  
[Wet vs. dry code](http://unenumerated.blogspot.com/2006/11/wet-code-and-
dry.html)

