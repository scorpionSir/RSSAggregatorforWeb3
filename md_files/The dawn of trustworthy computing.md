#  [ Unenumerated ](https://unenumerated.blogspot.com/)

An unending variety of topics

## Thursday, December 11, 2014

###  The dawn of trustworthy computing

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
  

###  References

[Here](http://bitstein.org/blog/nick-szabo-the-computer-science-of-crypto-
currency/) is a list of basic computer science papers describing the
technology of block chains (including cryptocurrencies).  
  
[Wet vs. dry code](http://unenumerated.blogspot.com/2006/11/wet-code-and-
dry.html)

Posted by  [ Nick Szabo ](https://www.blogger.com/profile/16820399856274245684
"author profile") at  [10:16
AM](https://unenumerated.blogspot.com/2014/12/the-dawn-of-trustworthy-
computing.html "permanent link") [
![](https://resources.blogblog.com/img/icon18_email.gif)
](https://www.blogger.com/email-
post.g?blogID=17908317&postID=4319656270164814457 "Email Post") [
![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)
](https://www.blogger.com/post-
edit.g?blogID=17908317&postID=4319656270164814457&from=pencil "Edit Post")

[Email This](https://www.blogger.com/share-
post.g?blogID=17908317&postID=4319656270164814457&target=email "Email
This")[BlogThis!](https://www.blogger.com/share-
post.g?blogID=17908317&postID=4319656270164814457&target=blog
"BlogThis!")[Share to Twitter](https://www.blogger.com/share-
post.g?blogID=17908317&postID=4319656270164814457&target=twitter "Share to
Twitter")[Share to Facebook](https://www.blogger.com/share-
post.g?blogID=17908317&postID=4319656270164814457&target=facebook "Share to
Facebook")[Share to Pinterest](https://www.blogger.com/share-
post.g?blogID=17908317&postID=4319656270164814457&target=pinterest "Share to
Pinterest")

#### 26 comments:

![](//resources.blogblog.com/img/blank.gif)

Anonymous said...

    

Hi Nick,  
  
I really enjoy your work, particularly your essays on philosophy. I have to
wonder in regards to this post, doesn't this mode of trustworthy computing
challenge the general power structures that computer networks are built upon?  
  
>With current web services we are fully trusting, in other words we are fully
vulnerable to, the computer, or more specifically the people who have access
to that computer, both insiders and hackers, to faithfully execute our orders,
secure our payments, and so on. If somebody on the other end wants to ignore
or falsify what you've instructed the web server to do, no strong security is
stopping them, only fallible and expensive human institutions which often stop
at national borders.  
  
It seems to me that this flips the law as it stands on its head. No longer is
power enumerated into gatekeepers, but to the gates themselves.  
  
Anyways, I love your thoughtful work and look forward to seeing what you come
up with next.

     [ 10:45 AM ](https://unenumerated.blogspot.com/2014/12/the-dawn-of-trustworthy-computing.html?showComment=1418323515731#c1866725223118245910 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/delete-comment.g?blogID=17908317&postID=1866725223118245910 "Delete Comment")

![](//resources.blogblog.com/img/blank.gif)

Anonymous said...

    

"deveptively" I think you meant "deceptively"  

     [ 10:57 AM ](https://unenumerated.blogspot.com/2014/12/the-dawn-of-trustworthy-computing.html?showComment=1418324227777#c9147645109664961230 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/delete-comment.g?blogID=17908317&postID=9147645109664961230 "Delete Comment")

![](//resources.blogblog.com/img/blank.gif)

Anonymous said...

    

Double space after the first use of "Nakamoto"! hmm, fishy...

     [ 11:33 AM ](https://unenumerated.blogspot.com/2014/12/the-dawn-of-trustworthy-computing.html?showComment=1418326407342#c2197812756221832031 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/delete-comment.g?blogID=17908317&postID=2197812756221832031 "Delete Comment")

[![](https://resources.blogblog.com/img/blank.gif)
![](//2.bp.blogspot.com/-2DtErnkX_Dc/VNKyv2xSOvI/AAAAAAAAHig/hYoosmMzkNw/s35/profile%25252Bpic%25252Bglitch%25252B480.jpg)](https://www.blogger.com/profile/18242797331927628174)

[Richard](https://www.blogger.com/profile/18242797331927628174) said...

    

in case the other post doesn't post is the basic take away that accountability
is becoming a commodity at least should anyone know how to decipher that which
is indicative of the actions requiring or creating accountability?

     [ 12:16 PM ](https://unenumerated.blogspot.com/2014/12/the-dawn-of-trustworthy-computing.html?showComment=1418328983528#c8208431869815146216 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/delete-comment.g?blogID=17908317&postID=8208431869815146216 "Delete Comment")

![](//resources.blogblog.com/img/blank.gif)

Anonymous said...

    

Wonderful essay.  
Does this change how you feel about futarchy?  
https://github.com/psztorc/Truthcoin

     [ 12:46 PM ](https://unenumerated.blogspot.com/2014/12/the-dawn-of-trustworthy-computing.html?showComment=1418330818658#c2792981307673918376 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/delete-comment.g?blogID=17908317&postID=2792981307673918376 "Delete Comment")

[![](//resources.blogblog.com/img/blank.gif) ](http://identifi.org)

[Tim Pastoor](http://identifi.org) said...

    

Another great essay, and I specifically like the elaboration on the
misconception between "decentralized" vs "Nakamoto consensus". Still,
centralized authorities do cause a lot of harm to societies in many cases, and
in most of those cases decentralization is a better option imo.  
  
Nakamoto consensus is preferable, but only applicable to cases wherein
everyone has to agree on one specific thing. If that thing is subjective to
each party involved, thus highly relative and can't be solved by means of
Nakamoto consensus (i.e., trust among humans), it's not the case.  
  
In that case, decentralized (or even distributed) peer-to-peer networks can
still offer better solutions to the problems that are being caused by
centralized authorities. Still, making sure that only the owner has access to
his/her property remains essential, at any given moment, through strong
cryptography.  
  
One solution to solving subjective trust among individual parties can be the
whitelisting principle (i.e., how humans tend to trust each other), which is
of course still less secure than Nakamoto consensus. Since Nakamoto consensus
can not be applied in these matters, whitelisting solutions are probably the
best-effort to follow.

     [ 1:18 PM ](https://unenumerated.blogspot.com/2014/12/the-dawn-of-trustworthy-computing.html?showComment=1418332702670#c4777836235871018168 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/delete-comment.g?blogID=17908317&postID=4777836235871018168 "Delete Comment")

![](//resources.blogblog.com/img/blank.gif)

Anonymous said...

    

I love reading your blogs Nick.  
Stay up baby!

     [ 1:51 PM ](https://unenumerated.blogspot.com/2014/12/the-dawn-of-trustworthy-computing.html?showComment=1418334689397#c1785446533573384450 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/delete-comment.g?blogID=17908317&postID=1785446533573384450 "Delete Comment")

[![](//resources.blogblog.com/img/blank.gif) ](https://qointum.com)

[Qointum](https://qointum.com) said...

    

Hi Nick,  
  
You might be interested in checking out our cryptocurrency platform, Qointum.
We have smart contracts scripted in Python that are far more flexible and
natural looking than what other platforms provide. Other platforms ended up
with contorted designs because they entirely missed the concept of conserved
transferable asset objects and code access specifiers. Other platforms are
also missing a natural language for multi-chain smart contracts which allow us
to scale up across the web.  
  
You mentioned the cost to run these blockchain computers is high, not so with
Qointum. We are the first to have a new proof-of-stake algorithm (rather than
proof-of-work mining which wastes electricity) that scales from a single stake
holder to thousands, while also allowing consensus from block headers only
(without examining transactions), which lets us go multi-chain using
Simplified State Verification (SSV).

     [ 2:40 PM ](https://unenumerated.blogspot.com/2014/12/the-dawn-of-trustworthy-computing.html?showComment=1418337619212#c1215769519799839207 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/delete-comment.g?blogID=17908317&postID=1215769519799839207 "Delete Comment")

![](//resources.blogblog.com/img/blank.gif)

null said...

    

Another great read from Nick Szabo, or is it Satoshi Nakamoto?

     [ 3:04 PM ](https://unenumerated.blogspot.com/2014/12/the-dawn-of-trustworthy-computing.html?showComment=1418339057078#c8474871839277868984 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/delete-comment.g?blogID=17908317&postID=8474871839277868984 "Delete Comment")

[![](//www.blogger.com/img/blogger_logo_round_35.png)
](https://www.blogger.com/profile/15423095026354723940)

[Mark](https://www.blogger.com/profile/15423095026354723940) said...

     This comment has been removed by the author.
     [ 3:23 PM ](https://unenumerated.blogspot.com/2014/12/the-dawn-of-trustworthy-computing.html?showComment=1418340212009#c4318297373532734976 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/delete-comment.g?blogID=17908317&postID=4318297373532734976 "Delete Comment")

![](//resources.blogblog.com/img/blank.gif)

Anonymous said...

    

Reminds me of this. http://www.loper-os.org/?p=1490

     [ 5:05 PM ](https://unenumerated.blogspot.com/2014/12/the-dawn-of-trustworthy-computing.html?showComment=1418346308721#c559589381462446469 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/delete-comment.g?blogID=17908317&postID=559589381462446469 "Delete Comment")

![](//resources.blogblog.com/img/blank.gif)

Anonymous said...

    

What do you think of Codius (codius.org)? -- seems to address the cost and
speed drawbacks of the blockchain's set amount of redundancy

     [ 5:23 PM ](https://unenumerated.blogspot.com/2014/12/the-dawn-of-trustworthy-computing.html?showComment=1418347420432#c2253420129215840365 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/delete-comment.g?blogID=17908317&postID=2253420129215840365 "Delete Comment")

[![](https://resources.blogblog.com/img/blank.gif)
![](//1.bp.blogspot.com/-XVvHnQC0IvE/W0Qr5h6Q50I/AAAAAAAAA8w/NS6E4roVVSkLi-7yOeDWVW5fT19M7M_VACK4BGAYYCw/s35/Taiwan%25252B071.JPG)](https://www.blogger.com/profile/04435417871477980255)

[Jeff McDonald](https://www.blogger.com/profile/04435417871477980255) said...

     This comment has been removed by the author.
     [ 8:41 PM ](https://unenumerated.blogspot.com/2014/12/the-dawn-of-trustworthy-computing.html?showComment=1418359260091#c3870147206459162359 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/delete-comment.g?blogID=17908317&postID=3870147206459162359 "Delete Comment")

![](//resources.blogblog.com/img/blank.gif)

Anonymous said...

    

>Block chains could also control hardware which controls the function of and
access to physical property.  
  
Imagine a blockchain that operated a printing press. This press could print
codes on a special piece of paper. We could trade these pieces of paper to
each other in return for goods and services.

     [ 10:26 PM ](https://unenumerated.blogspot.com/2014/12/the-dawn-of-trustworthy-computing.html?showComment=1418365575070#c671852109600830187 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/delete-comment.g?blogID=17908317&postID=671852109600830187 "Delete Comment")

[![](//www.blogger.com/img/blogger_logo_round_35.png)
](https://www.blogger.com/profile/11543639411820745571)

[Benjamin Wright](https://www.blogger.com/profile/11543639411820745571)
said...

    

Nick: I humbly argue that effective "fiduciary code" and "smart contracts"
will benefit from traditional legal analysis and legal draftsmanship. A
skilled legal draftsman composes a better contract than someone who lacks the
skill. I explain: http://hack-igations.blogspot.com/2014/11/ethereum.html

     [ 9:20 AM ](https://unenumerated.blogspot.com/2014/12/the-dawn-of-trustworthy-computing.html?showComment=1418404858029#c3714077628756749607 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/delete-comment.g?blogID=17908317&postID=3714077628756749607 "Delete Comment")

![](//resources.blogblog.com/img/blank.gif)

Alberth said...

    

Could a Bitcoin hard fork solve this, eventually?

     [ 10:40 AM ](https://unenumerated.blogspot.com/2014/12/the-dawn-of-trustworthy-computing.html?showComment=1418409651633#c8764735646394278374 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/delete-comment.g?blogID=17908317&postID=8764735646394278374 "Delete Comment")

![](//resources.blogblog.com/img/blank.gif)

Anonymous said...

    

You sort of lost me at the movie theater example. You clearly never worked a
retail job because employees steal stuff all the time. There's plenty of ways
for insiders to steal credit card numbers or cash. And on the other end of
things there's just straight up embezzling by the "root" accountants or
managers.

     [ 12:29 PM ](https://unenumerated.blogspot.com/2014/12/the-dawn-of-trustworthy-computing.html?showComment=1418416191092#c7365385861914914034 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/delete-comment.g?blogID=17908317&postID=7365385861914914034 "Delete Comment")

![](//resources.blogblog.com/img/blank.gif)

Anonymous said...

    

"You sort of lost me at the movie theater example. You clearly never worked a
retail job because employees steal stuff all the time. There's plenty of ways
for insiders to steal credit card numbers or cash. And on the other end of
things there's just straight up embezzling by the "root" accountants or
managers."  
  
I think the main point is not so much that. It's about the difference between
a physical and a digital transaction. A physical/cash transaction is "secure"
not in the sense that theft cannot happen -- but rather that the exchange is
defined by physical reality. You hand over cash to the deli, theatre,food
truck... and that's it.  
  
The cash left you undeniably. And the vendor knows that he received payment (I
mean it's right there in the register, looks and feels like a real $20). And
that's why you never once needed to fill out a form to do any of that. The
cashier never had to know who the heck you were. The transaction was "secure".  
  
In the digital world, there is much more that needs to happen behind the
scenes - because of the nature of what data is -- being digital -- itself.
Even the swipe of a credit card involves an initial sign-up with
Identification check and it goes through a complex processes of other checks
and clearances, through various gateways and systems.  
  
The point is that there is no physical-like- "cash" equivalent that has
existed. At least until now.

     [ 2:52 PM ](https://unenumerated.blogspot.com/2014/12/the-dawn-of-trustworthy-computing.html?showComment=1418424747352#c9190086133836284843 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/delete-comment.g?blogID=17908317&postID=9190086133836284843 "Delete Comment")

[![](//www.blogger.com/img/blogger_logo_round_35.png)
](https://www.blogger.com/profile/03153421392606581139)

[Donald McIntyre](https://www.blogger.com/profile/03153421392606581139)
said...

     This comment has been removed by the author.
     [ 12:49 PM ](https://unenumerated.blogspot.com/2014/12/the-dawn-of-trustworthy-computing.html?showComment=1418503742020#c1710953552583549431 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/delete-comment.g?blogID=17908317&postID=1710953552583549431 "Delete Comment")

![](//resources.blogblog.com/img/blank.gif)

Anonymous said...

    

"You sort of lost me at the movie theater example. You clearly never worked a
retail job because employees steal stuff all the time. There's plenty of ways
for insiders to steal credit card numbers or cash. And on the other end of
things there's just straight up embezzling by the >>root<< accountants or
managers."  
  
If i'm not mistaken Nick meant that in the theater you have your cash and
assets at all times in your pockets, administrators won't see them unless
you'll expose them willingly.  
  
The analogy of "root" administrator in a movie theater would be a deposit
where you're required to store all your posessions before entering the
projection room. Then the administrators would be free to copy, steal and
destroy your posessions without your knowledge and there would be no way of
stopping them.  
  
Anonymously,  
Przemysław Bagiński

     [ 8:47 AM ](https://unenumerated.blogspot.com/2014/12/the-dawn-of-trustworthy-computing.html?showComment=1418662060013#c5157958097098199869 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/delete-comment.g?blogID=17908317&postID=5157958097098199869 "Delete Comment")

[![](//www.blogger.com/img/blogger_logo_round_35.png)
](https://www.blogger.com/profile/06678661491953418544)

[dominiksf](https://www.blogger.com/profile/06678661491953418544) said...

    

funny congruency in thought, i posted this around the same time. great to see
others thinking in this direction.  
  
  
https://bitcointalk.org/index.php?topic=400235.msg9795832#msg9795832

     [ 4:52 PM ](https://unenumerated.blogspot.com/2014/12/the-dawn-of-trustworthy-computing.html?showComment=1418777546479#c1861968168043607399 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/delete-comment.g?blogID=17908317&postID=1861968168043607399 "Delete Comment")

![](//resources.blogblog.com/img/blank.gif)

Anonymous said...

    

Hi Nick,  
  
As always great work. I really appreciate the knowledge and information you
make available to the common person like myself that doesn't always have easy
access to highly guarded research and study findings.  
  
Also, great job on finally putting a name to some of the stuff we are dealing
with on a daily basis. The "Virtual Computer" Blockchain reference is great.  
  
Respectfully,  
L. Detweiler

     [ 4:48 AM ](https://unenumerated.blogspot.com/2014/12/the-dawn-of-trustworthy-computing.html?showComment=1419166113893#c8240362341945467567 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/delete-comment.g?blogID=17908317&postID=8240362341945467567 "Delete Comment")

[![](//www.blogger.com/img/blogger_logo_round_35.png)
](https://www.blogger.com/profile/13057086390864018760)

[David Gerard](https://www.blogger.com/profile/13057086390864018760) said...

    

In your original 1994 paper on smart contracts, you note the necessity of
human intervention in case something goes wrong.  
  
It's entirely unclear to me how this is possible with a blockchain enforced by
strong cryptography.  
  
The plot of Dr Strangelove is literally a smart contract going wrong and
people's attempts to avert the preprogrammed outcome.  
  
Reddit post:
http://www.reddit.com/r/Buttcoin/comments/2pzssy/in_what_world_are_smart_contracts_actually_a_good/

     [ 2:12 PM ](https://unenumerated.blogspot.com/2014/12/the-dawn-of-trustworthy-computing.html?showComment=1419199952775#c2534754966528379595 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/delete-comment.g?blogID=17908317&postID=2534754966528379595 "Delete Comment")

[![](//www.blogger.com/img/blogger_logo_round_35.png)
](https://www.blogger.com/profile/01960732711496740182)

[Unknown](https://www.blogger.com/profile/01960732711496740182) said...

    

In the context of the movie theater and grocery store example, I was about to
say that Nick has been thinking about this for a long time. Then I googled it,
and found [this article from 1997](http://szabo.best.vwh.net/accounting.html).  
  
The point is that at the movie theater, there's a paper trail showing how much
money was received, and the cashier can't steal untraceably from the owners.
Customers insist on getting a ticket in exchange for their money. And the
ticket taker is separate to ensure that cashiers don't let their friends in
for half price.  
  
At the grocery store, similarly, there's a cash register tracking every
transaction. The owner encourages the customers to insist on receipts ("If I
forget to give you a receipt, we'll refund half your money.")  
  
Institutions like these don't prevent someone from opening the till and
running away with the funds, but they do make it evident if someone tries to
skim 1% of the money over the long term.

     [ 10:54 PM ](https://unenumerated.blogspot.com/2014/12/the-dawn-of-trustworthy-computing.html?showComment=1420268040883#c8577343424280770253 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/delete-comment.g?blogID=17908317&postID=8577343424280770253 "Delete Comment")

![](//resources.blogblog.com/img/blank.gif)

Anonymous said...

    

Post by eddie:  
  
Although smart contracts are still in their nascent stage, the potential is
clear. If a simple enough user interface were developed it could remove a host
of legal headaches, like updating your will. Imagine if allocating your assets
after your death was as simple as moving an adjustable slider that determines
who gets how much. Once the smart contract can verify the triggering condition
--in this case, your death--the contract goes into effect and your assets are
divvied up.  
  
  
A smart contract can be activated, after which point it takes on a "life of
its own", in the sense that it will process regularly over time according to
its own internal terms and logic, until it expires or is deactivated. In this
sense, it is like any other recurring OT transaction such as market trades and
payment plans.  
  
  
Smart contracts are most distinguished by the fact that they can have
scriptable clauses. (Normally on OT, a typical contract only contains data
tags, and human-readable clauses. Only the smart contracts "can come to life"
with their own custom-scripted clauses.)  
  
  
Smart contracts can have multiple parties, each with their own agents and
asset accounts.  
  
  
Only a select few functions are made available from within the script code of
a smart contract, and all funds transfers go through this tightly-controlled
interface, with notices and receipts sent to all relevant parties.  
  
  
The script code is unable to manipulate any assets excepting those explicitly
declared beforehand on the smart contract, and verified as valid property of a
legitimate party to the contract. And when funds are moved, it's to a
contract-specific name, not an account ID. For example, you wouldn't transfer
funds from account pckjsdf9872345kj34kjhsf, but rather, by that account's name
as declared in the contract, such as alice_petty_cash or bobs_acct. (This
means that it's impossible to even reference any account other than those
declared on the smart contract by name, since the functions provided can only
operate based on those names.)  
  
  

     [ 1:46 PM ](https://unenumerated.blogspot.com/2014/12/the-dawn-of-trustworthy-computing.html?showComment=1421099204288#c4416552088218270819 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/delete-comment.g?blogID=17908317&postID=4416552088218270819 "Delete Comment")

![](//resources.blogblog.com/img/blank.gif)

Anonymous said...

    

Please write more. I'm thirsty for more of this original stuff.

     [ 1:14 PM ](https://unenumerated.blogspot.com/2014/12/the-dawn-of-trustworthy-computing.html?showComment=1425762853033#c5022002638440237020 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/delete-comment.g?blogID=17908317&postID=5022002638440237020 "Delete Comment")

[Post a
Comment](https://www.blogger.com/comment.g?blogID=17908317&postID=4319656270164814457)

[Newer Post](https://unenumerated.blogspot.com/2015/05/small-game-
fallacies.html "Newer Post") [Older
Post](https://unenumerated.blogspot.com/2014/10/transportation-divergence-
and.html "Older Post") [Home](https://unenumerated.blogspot.com/)

Subscribe to: [Post Comments
(Atom)](https://unenumerated.blogspot.com/feeds/4319656270164814457/comments/default)

## Pages

  * [Home](https://unenumerated.blogspot.com/)

## About Me

[ Nick Szabo ](https://www.blogger.com/profile/16820399856274245684)

    "A premier thinker about history, law and economics, and the lessons they have for security." -- Adam Shostack, [Emergent Chaos ](http://www.emergentchaos.com/archives/2005/12/nick_szabo_blog.html)   
  
"Szabo comes out with these essays that leave me in awe." -- [Brian
Dunbar](http://space4commerce.blogspot.com/2011/06/tab-clearing_14.html)  
  
"Reading material that is eclectic, challenging and endlessly fascinating."
\-- Sean McGrath,
[Propylon](http://seanmcgrath.blogspot.com/2004_05_09_seanmcgrath_archive.html)  
  
"Like most blogs worth my attention, this blog is updated only infrequently.
That is because the authors of blogs worth my attention only post when they
have something to say that is true, relevant and not already known by their
audience. Most of the human race does not have the skill to know when an idea
has these three properties. The skill is particularly rare in the fields of
politics and economics, which is why this blog is such a rare and valuable
thing." \-- [Richard Hollerith](http://dl4.jottit.com/)  
  

[View my complete
profile](https://www.blogger.com/profile/16820399856274245684)

## Blog Archive

  * [ ► ](javascript:void\(0\)) [ 2018 ](https://unenumerated.blogspot.com/2018/) (1)
    * [ ► ](javascript:void\(0\)) [ March ](https://unenumerated.blogspot.com/2018/03/) (1)

  * [ ► ](javascript:void\(0\)) [ 2017 ](https://unenumerated.blogspot.com/2017/) (3)
    * [ ► ](javascript:void\(0\)) [ March ](https://unenumerated.blogspot.com/2017/03/) (1)
    * [ ► ](javascript:void\(0\)) [ February ](https://unenumerated.blogspot.com/2017/02/) (2)

  * [ ► ](javascript:void\(0\)) [ 2016 ](https://unenumerated.blogspot.com/2016/) (4)
    * [ ► ](javascript:void\(0\)) [ December ](https://unenumerated.blogspot.com/2016/12/) (1)
    * [ ► ](javascript:void\(0\)) [ July ](https://unenumerated.blogspot.com/2016/07/) (1)
    * [ ► ](javascript:void\(0\)) [ March ](https://unenumerated.blogspot.com/2016/03/) (1)
    * [ ► ](javascript:void\(0\)) [ February ](https://unenumerated.blogspot.com/2016/02/) (1)

  * [ ► ](javascript:void\(0\)) [ 2015 ](https://unenumerated.blogspot.com/2015/) (3)
    * [ ► ](javascript:void\(0\)) [ October ](https://unenumerated.blogspot.com/2015/10/) (1)
    * [ ► ](javascript:void\(0\)) [ July ](https://unenumerated.blogspot.com/2015/07/) (1)
    * [ ► ](javascript:void\(0\)) [ May ](https://unenumerated.blogspot.com/2015/05/) (1)

  * [ ▼ ](javascript:void\(0\)) [ 2014 ](https://unenumerated.blogspot.com/2014/) (3)
    * [ ▼ ](javascript:void\(0\)) [ December ](https://unenumerated.blogspot.com/2014/12/) (1)
      * [The dawn of trustworthy computing](https://unenumerated.blogspot.com/2014/12/the-dawn-of-trustworthy-computing.html)
    * [ ► ](javascript:void\(0\)) [ October ](https://unenumerated.blogspot.com/2014/10/) (1)
    * [ ► ](javascript:void\(0\)) [ July ](https://unenumerated.blogspot.com/2014/07/) (1)

  * [ ► ](javascript:void\(0\)) [ 2013 ](https://unenumerated.blogspot.com/2013/) (3)
    * [ ► ](javascript:void\(0\)) [ November ](https://unenumerated.blogspot.com/2013/11/) (1)
    * [ ► ](javascript:void\(0\)) [ August ](https://unenumerated.blogspot.com/2013/08/) (1)
    * [ ► ](javascript:void\(0\)) [ July ](https://unenumerated.blogspot.com/2013/07/) (1)

  * [ ► ](javascript:void\(0\)) [ 2012 ](https://unenumerated.blogspot.com/2012/) (8)
    * [ ► ](javascript:void\(0\)) [ October ](https://unenumerated.blogspot.com/2012/10/) (2)
    * [ ► ](javascript:void\(0\)) [ August ](https://unenumerated.blogspot.com/2012/08/) (2)
    * [ ► ](javascript:void\(0\)) [ July ](https://unenumerated.blogspot.com/2012/07/) (4)

  * [ ► ](javascript:void\(0\)) [ 2011 ](https://unenumerated.blogspot.com/2011/) (12)
    * [ ► ](javascript:void\(0\)) [ December ](https://unenumerated.blogspot.com/2011/12/) (1)
    * [ ► ](javascript:void\(0\)) [ July ](https://unenumerated.blogspot.com/2011/07/) (1)
    * [ ► ](javascript:void\(0\)) [ June ](https://unenumerated.blogspot.com/2011/06/) (2)
    * [ ► ](javascript:void\(0\)) [ May ](https://unenumerated.blogspot.com/2011/05/) (2)
    * [ ► ](javascript:void\(0\)) [ February ](https://unenumerated.blogspot.com/2011/02/) (2)
    * [ ► ](javascript:void\(0\)) [ January ](https://unenumerated.blogspot.com/2011/01/) (4)

  * [ ► ](javascript:void\(0\)) [ 2010 ](https://unenumerated.blogspot.com/2010/) (9)
    * [ ► ](javascript:void\(0\)) [ December ](https://unenumerated.blogspot.com/2010/12/) (1)
    * [ ► ](javascript:void\(0\)) [ October ](https://unenumerated.blogspot.com/2010/10/) (4)
    * [ ► ](javascript:void\(0\)) [ September ](https://unenumerated.blogspot.com/2010/09/) (2)
    * [ ► ](javascript:void\(0\)) [ February ](https://unenumerated.blogspot.com/2010/02/) (2)

  * [ ► ](javascript:void\(0\)) [ 2009 ](https://unenumerated.blogspot.com/2009/) (29)
    * [ ► ](javascript:void\(0\)) [ November ](https://unenumerated.blogspot.com/2009/11/) (3)
    * [ ► ](javascript:void\(0\)) [ October ](https://unenumerated.blogspot.com/2009/10/) (6)
    * [ ► ](javascript:void\(0\)) [ September ](https://unenumerated.blogspot.com/2009/09/) (3)
    * [ ► ](javascript:void\(0\)) [ August ](https://unenumerated.blogspot.com/2009/08/) (1)
    * [ ► ](javascript:void\(0\)) [ July ](https://unenumerated.blogspot.com/2009/07/) (1)
    * [ ► ](javascript:void\(0\)) [ June ](https://unenumerated.blogspot.com/2009/06/) (3)
    * [ ► ](javascript:void\(0\)) [ May ](https://unenumerated.blogspot.com/2009/05/) (6)
    * [ ► ](javascript:void\(0\)) [ April ](https://unenumerated.blogspot.com/2009/04/) (3)
    * [ ► ](javascript:void\(0\)) [ January ](https://unenumerated.blogspot.com/2009/01/) (3)

  * [ ► ](javascript:void\(0\)) [ 2008 ](https://unenumerated.blogspot.com/2008/) (55)
    * [ ► ](javascript:void\(0\)) [ December ](https://unenumerated.blogspot.com/2008/12/) (2)
    * [ ► ](javascript:void\(0\)) [ October ](https://unenumerated.blogspot.com/2008/10/) (2)
    * [ ► ](javascript:void\(0\)) [ September ](https://unenumerated.blogspot.com/2008/09/) (4)
    * [ ► ](javascript:void\(0\)) [ August ](https://unenumerated.blogspot.com/2008/08/) (9)
    * [ ► ](javascript:void\(0\)) [ July ](https://unenumerated.blogspot.com/2008/07/) (4)
    * [ ► ](javascript:void\(0\)) [ June ](https://unenumerated.blogspot.com/2008/06/) (6)
    * [ ► ](javascript:void\(0\)) [ May ](https://unenumerated.blogspot.com/2008/05/) (6)
    * [ ► ](javascript:void\(0\)) [ April ](https://unenumerated.blogspot.com/2008/04/) (4)
    * [ ► ](javascript:void\(0\)) [ March ](https://unenumerated.blogspot.com/2008/03/) (10)
    * [ ► ](javascript:void\(0\)) [ February ](https://unenumerated.blogspot.com/2008/02/) (5)
    * [ ► ](javascript:void\(0\)) [ January ](https://unenumerated.blogspot.com/2008/01/) (3)

  * [ ► ](javascript:void\(0\)) [ 2007 ](https://unenumerated.blogspot.com/2007/) (47)
    * [ ► ](javascript:void\(0\)) [ December ](https://unenumerated.blogspot.com/2007/12/) (1)
    * [ ► ](javascript:void\(0\)) [ October ](https://unenumerated.blogspot.com/2007/10/) (2)
    * [ ► ](javascript:void\(0\)) [ September ](https://unenumerated.blogspot.com/2007/09/) (8)
    * [ ► ](javascript:void\(0\)) [ August ](https://unenumerated.blogspot.com/2007/08/) (10)
    * [ ► ](javascript:void\(0\)) [ July ](https://unenumerated.blogspot.com/2007/07/) (4)
    * [ ► ](javascript:void\(0\)) [ June ](https://unenumerated.blogspot.com/2007/06/) (4)
    * [ ► ](javascript:void\(0\)) [ May ](https://unenumerated.blogspot.com/2007/05/) (8)
    * [ ► ](javascript:void\(0\)) [ April ](https://unenumerated.blogspot.com/2007/04/) (1)
    * [ ► ](javascript:void\(0\)) [ March ](https://unenumerated.blogspot.com/2007/03/) (2)
    * [ ► ](javascript:void\(0\)) [ February ](https://unenumerated.blogspot.com/2007/02/) (4)
    * [ ► ](javascript:void\(0\)) [ January ](https://unenumerated.blogspot.com/2007/01/) (3)

  * [ ► ](javascript:void\(0\)) [ 2006 ](https://unenumerated.blogspot.com/2006/) (130)
    * [ ► ](javascript:void\(0\)) [ December ](https://unenumerated.blogspot.com/2006/12/) (4)
    * [ ► ](javascript:void\(0\)) [ November ](https://unenumerated.blogspot.com/2006/11/) (7)
    * [ ► ](javascript:void\(0\)) [ October ](https://unenumerated.blogspot.com/2006/10/) (15)
    * [ ► ](javascript:void\(0\)) [ September ](https://unenumerated.blogspot.com/2006/09/) (15)
    * [ ► ](javascript:void\(0\)) [ August ](https://unenumerated.blogspot.com/2006/08/) (20)
    * [ ► ](javascript:void\(0\)) [ July ](https://unenumerated.blogspot.com/2006/07/) (5)
    * [ ► ](javascript:void\(0\)) [ June ](https://unenumerated.blogspot.com/2006/06/) (10)
    * [ ► ](javascript:void\(0\)) [ May ](https://unenumerated.blogspot.com/2006/05/) (4)
    * [ ► ](javascript:void\(0\)) [ April ](https://unenumerated.blogspot.com/2006/04/) (3)
    * [ ► ](javascript:void\(0\)) [ March ](https://unenumerated.blogspot.com/2006/03/) (11)
    * [ ► ](javascript:void\(0\)) [ February ](https://unenumerated.blogspot.com/2006/02/) (10)
    * [ ► ](javascript:void\(0\)) [ January ](https://unenumerated.blogspot.com/2006/01/) (26)

  * [ ► ](javascript:void\(0\)) [ 2005 ](https://unenumerated.blogspot.com/2005/) (44)
    * [ ► ](javascript:void\(0\)) [ December ](https://unenumerated.blogspot.com/2005/12/) (16)
    * [ ► ](javascript:void\(0\)) [ November ](https://unenumerated.blogspot.com/2005/11/) (5)
    * [ ► ](javascript:void\(0\)) [ October ](https://unenumerated.blogspot.com/2005/10/) (23)

|  
  
---|---  
  
Simple theme. Powered by [Blogger](https://www.blogger.com).

  *[10:16 AM]: 2014-12-11T10:16:00-08:00

