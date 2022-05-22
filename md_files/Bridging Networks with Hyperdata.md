[

# Akasha

](/)

[About](/about/)

[Blog](/blog/)

[Careers](/careers/)

[Contact us](/contact/)

![Open
search](data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjE4IiB3aWR0aD0iMTgiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGcgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIiBzdHJva2U9IiM1MzYyN2MiIHN0cm9rZS13aWR0aD0iMS4yIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxIDEpIj48Y2lyY2xlIGN4PSI2LjIyMiIgY3k9IjYuMjIyIiByPSI2LjIyMiIvPjxwYXRoIGQ9Im0xNiAxNi01LjMyOC01LjMyOCIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIi8+PC9nPjwvc3ZnPg==)

[

# Akasha

](/)

Projects

[Ethereum.world](https://ethereum.world/)

[AKASHA.world](https://akasha.world/)

[AKASHA Hubs](/hubs)

The Foundation

[About](/about/)

[Blog](/blog/)

[Careers](/careers/)

[Contact us](/contact/)

[Events](/events/)

[Friends](/friends/)

[Press](/press)

Resources

[Style Guide](https://style.akasha.org/)

[Glossary](/glossary/)

Get in touch, we are friendly people

[](https://discordapp.com/invite/JqqKasJ)

[](https://twitter.com/AKASHAorg)

[](https://www.facebook.com/AKASHAorg)

[](https://github.com/AKASHAorg/)

[](https://www.reddit.com/r/AkashaProject)

[](https://www.linkedin.com/company/akashaorg/)

[](https://www.youtube.com/c/Akashaorg)

[Legal](/legal/) ·

[Privacy Policy](/privacy-policy/)

CC BY-SA 4.0 AKASHA Foundation

![Open
search](data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjE4IiB3aWR0aD0iMTgiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGcgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIiBzdHJva2U9IiM1MzYyN2MiIHN0cm9rZS13aWR0aD0iMS4yIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxIDEpIj48Y2lyY2xlIGN4PSI2LjIyMiIgY3k9IjYuMjIyIiByPSI2LjIyMiIvPjxwYXRoIGQ9Im0xNiAxNi01LjMyOC01LjMyOCIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIi8+PC9nPjwvc3ZnPg==)

![Bridging Networks with
Hyperdata](/static/ac1dd9bc7972fdd40c31f02ee0880b12/2a43b/hero.jpg)

[Thoughts & Ideas](/blog/category/thoughts-ideas/)

[Research](/blog/category/research/)

[Hyperdata](/blog/category/hyperdata/)

## Bridging Networks with Hyperdata

By [Andrei Sambra](/blog/author/andrei-sambra/)

·

March 04, 2019

We are excited to share with you a new idea that we hope will help bridge
existing decentralization efforts. By writing about it, we hope to start a
conversation that will enable cooperation among existing projects. To this end
we propose _Hyperdata_ , a storage & network-agnostic data model and schema(s)
for linking data across different networks and platforms.

We understand that achieving decentralization on the Web today is not easy.
Although the Web itself is already decentralized, the services operating on
top of it are not. I admit that while it's great to have a lot of teams and
projects working on decentralized services, in most cases it works against
decentralization in the long term as they introduce more network
fragmentation.

Typically what happens is that when Project A releases their software, it is
only able to interact with other instances of Project A (e.g.
[Diaspora](https://diasporafoundation.org/),
[MaidSafe](https://maidsafe.net/), [Matrix](https://matrix.org), etc.).
Blockchain projects are also in a similar situation, while still operating at
the same application layer as the Web -- developers can build applications
that utilize the underlying network (e.g. [uPort](https://www.uport.me/),
[Blockstack](https://blockstack.org/)). However, the biggest difference
between the Web and blockchain networks is that the Web is driven by a common
set of standards as well as a non-profit [standards
body](https://www.w3.org/), whereas blockchain projects are very fragmented
and each come out with their own standards and self-governance. This
translates into a higher risk of seeing the network collapse due to financial
reasons, bad management, or simply because the project has become obsolete.

Being realistic, we should face the fact that pretty much no project is
guaranteed to last forever. Therefore if we plan to build something that
lasts, we need to look at the big picture and find solutions that should not
depend on any one network in particular. To be more precise, we should aim to
develop a storage-agnostic data model and schema(s) for linking data across
different domains and platforms. For example, this means that a piece of data
hosted on the Web could link to another one hosted on the InterPlanetary File
System ([IPFS](https://ipfs.io/)), which in turn could potentially link to
data hosted even on your local file system.

## Why hyperdata?

An immediate advantage of being storage/network-agnostic is that developers
can build software that transcends specific network constraints, while still
taking advantage of everything each network has to offer. For example, by
default IPFS does not offer any support for identity and authorship. Hyperdata
would allow payloads to be signed, making sure that authors will always have a
way to prove who created the content. At the same time, the signatures (i.e.
cryptographic proofs) can also be computed independently from the network and
in some cases even the identity provider (more in the example below). In fact,
proving a signature may not even require network access at all, if the device
has been provisioned with the right keys (similar to
[PGP](https://en.wikipedia.org/wiki/Pretty_Good_Privacy)).

Identity is in most cases tightly coupled with the application and always
coupled with the network. Today _uPort_ and _Blockstack_ claim to offer
decentralized identity that can be reused in apps running on their networks.
While this is definitely a step forward, it would be great to find a solution
that goes beyond any given network. Hyperdata does not mandate nor does it
even offer an identity solution. It encourages however the use of
Decentralized Identifiers ([DIDs](https://w3c-ccg.github.io/did-spec/)). We
feel that DIDs fit very well with hyperdata, since it allows arbitrary parties
to resolve DIDs to an endpoint and keys, even if they are not on the same
network.

Last but not least is data portability, especially in light of EU's new
General Data Protection Regulation (GDPR). Data can be stored anywhere, since
it is no longer tightly coupled with the network. It can also be stored on
multiple networks at the same time, to offer increased redundancy.

## How does hyperdata work?

The concept itself is very straightforward. We have a _payload_ and a
_signature_ over the whole payload. Please remember this is still very early
stuff and will definitely evolve in time.

The payload contains the metadata as well as the actual content.

  * **type field** [optional] - can be added by applications that generate the content.
  * **reference field** \- either a URI or another nested piece of hyperdata
  * **created field** \- a timestamp when the content was created
  * **author field** \- preferably a DID
  * **body field** \- the actual content

    
    
    {
        "type": "AKASHAComment",
        "ref": "https://twitter.com/AkashaProject/status/1085598391827120130",
        "created": "2019-01-14T05:34:22Z",
        "author": "did:muport:QmYiEMtYauiPrak1uPN8UV82wztgF9cgL4gkCMtDUxUbao",
        "body": "Awesome post by AKASHA."
    }

In the example above, user identities are expressed using DIDs, in this case a
[3Box](https://3box.io) identity.

The signature is computed over a binary serialization of the payload, and it
contains all the necessary information to allow proof computation. The fields
are based on the [Security Vocabulary](https://web-
payments.org/vocabs/security#) schema.

    
    
    {
        "type": "Web3Signature",
        "creator": "did:muport:QmYiEMtYauiPrak1uPN8UV82wztgF9cgL4gkCMtDUxUbao",
        "digestAlgorithm": "https://www.ietf.org/assignments/jwa-parameters#SHA256",
        "signatureValue": "0x1ba149b9...e461c"
    }

To perform the signature step above, we've used our Ethereum keys (through
MetaMask) to create a 3Box DID and corresponding profile page, without
exposing our private key at any point during the process. Next, we used the
`web3` library (through MetaMask) to personally sign the payload. Here is how
the whole document looks once we've added the corresponding `context` links.

    
    
    {
      "@context": [
        "https://w3id.org/identity/v1",
        "https://akasha.org/contexts/comments.jsonld"
      ],
      "payload": {
        "type": "AKASHAComment",
        "ref": "https://twitter.com/AkashaProject/status/1085598391827120130",
        "created": "2019-01-14T05:34:22Z",
        "author": "did:muport:QmYiEMtYauiPrak1uPN8UV82wztgF9cgL4gkCMtDUxUbao",
        "body": "Awesome post by AKASHA."
      },
      "signature": {
        "type": "Web3Signature",
        "creator": "did:muport:QmYiEMtYauiPrak1uPN8UV82wztgF9cgL4gkCMtDUxUbao",
        "digestAlgorithm": "https://www.ietf.org/assignments/jwa-parameters#SHA256",
        "signatureValue": "0x1ba149b9...e461c"
      }
    }

## Let's look at an example!

Let’s consider the following use case of an application (we may call it
comments.com) through which a group of people start a conversation based on
any link (in this case a Tweet). Additionally, comments can be stored on IPFS
to make them decentralized but also resistant to censorship. We can see
already that our application will have to be able to resolve links coming from
the Web (Twitter in this example) but also from IPFS. Perhaps we might also
want to store drafts locally or integrate Slack?

### Starting a discussion

First we need to model the initial comment containing the Tweet link. The
author is someone having a decentralized identity provider (using
[3Box](https://3box.io)) that has created the following user identifier --
_`did:muport:QmYiEMtYauiPrak1uPN8UV82wztgF9cgL4gkCMtDUxUbao`_.

Let's see how this bit of hyperdata would look, using a signed JSON-LD
representation.

    
    
    {
      "@context": [
        "https://w3id.org/identity/v1",
        "https://akasha.org/contexts/comments.jsonld"
      ],
      "payload": {
        "type": "AKASHAComment",
        "ref": "https://twitter.com/AkashaProject/status/1085598391827120130",
        "created": "2019-01-14T05:34:22Z",
        "author": "did:muport:QmYiEMtYauiPrak1uPN8UV82wztgF9cgL4gkCMtDUxUbao",
        "body": "Awesome post by AKASHA."
      },
      "signature": {
        "type": "Web3Signature",
        "creator": "did:muport:QmYiEMtYauiPrak1uPN8UV82wztgF9cgL4gkCMtDUxUbao",
        "digestAlgorithm": "https://www.ietf.org/assignments/jwa-parameters#SHA256",
        "signatureValue": "0x1ba149b9...e461c"
      }
    }

You might have noticed that in the `@context` property, we have added a
placeholder for `"https://akasha.org/contexts/comments.jsonld"`. This
particular context document will contain the missing property definitions that
are relevant for our application -- such as `comment`, `ref`, `author`,
`body`, and `scope`.

Finally, because the [JSON-LD](https://www.w3.org/TR/json-ld/) document is
fully self-describing and it contains a signature that doesn't mandate _where_
the data should be stored, we can safely add it to IPFS resulting then in the
following CID `QmUEpVDGumYocPtX9iqSMf1Czpf7qHN9W8Xe5KjaDstRPn`.

### Adding replies to comments

Replies are almost identical to comments, with the exception that they are of
a different type and they refer to another comment instead of the post. Let's
take a look!

    
    
    {
      "@context": [
        "https://w3id.org/identity/v1",
        "https://akasha.org/contexts/comments.jsonld"
      ],
      "payload": {
        "type": "AKASHAReply",
        "ref": "ipfs://QmUEpVDGumYocPtX9iqSMf1Czpf7qHN9W8Xe5KjaDstRPn",
        "created": "2019-01-15T09:21:44Z",
        "author": "did:sov:WRfXPg8dantKVubE3HX8pw",
        "body": "Thanks for sharing, I also love AKASHA."
      },
      "signature": {
        "type": "RsaSignature2018",
        "creator": "did:sov:WRfXPg8dantKVubE3HX8pw/keys/1",
        "digestAlgorithm": "https://www.ietf.org/assignments/jwa-parameters#SHA256",
        "signatureValue": "9feAlB0L2..Z2JF29="
      }
    }

### Adding comments that are not on IPFS

We can also add comments that can be hosted on the Web. What matters in the
end is just the content itself, the raw data.

    
    
    {
      "@context": [
        "https://w3id.org/identity/v1",
        "https://akasha.org/contexts/comments.jsonld"
      ],
      "payload": {
        "type": "AKASHAComment",
        "ref": "ipfs://QmUEpVDGumYocPtX9iqSMf1Czpf7qHN9W8Xe5KjaDstRPn",
        "created": "2019-01-15T12:11:54Z",
        "author": "did:uport:1690e4b1adb3GYTBaaKAgr76uY7iSe1Uf28",
        "body": "Cool stuff, I'm going to follow @AKASHA now."
      },
      "signature": {
        "type": "RsaSignature2018",
        "creator": "did:uport:1690e4b1adb3GYTBaaKAgr76uY7iSe1Uf28/keys/6",
        "digestAlgorithm": "https://www.ietf.org/assignments/jwa-parameters#SHA256",
        "signatureValue": "BavEll0/I1..W3JT24="
      }
    }

This comment can be published on Web 2.0 servers (in this case on Github
pages), since we know it will be served with the right content type -- for
example <https://deiu.github.io/cdn/comment-ab019f3.jsonld>.

### Displaying comments in the app

Now the "magic" happens. As per above, the app at comments.com maintains an
index of comments for a given resource (i.e. the initial tweet). In order for
the app to display the comments it needs to fetch all of them before anything
else happens. To do so, it looks at the index to find a corresponding protocol
handler/fetcher for each comment (ipfs:// or https:// in this case).
Dereferencing the URI of each comment from the index results in a document
containing machine-readable information expressed as JSON-LD. All comments
then could be ordered based on the time when they were created.

Also, _Comments.com_ has been used here as an example application of
hyperdata. We haven’t attempted to address the question of comment moderation,
decoupled as it is from the hyperdata model, but rest assured we appreciate
the balance between censorship and allowing a community to keep things
civilized.

#### Things to consider

One issue that is easy to spot right away is that we cannot discover and list
all comments for a post unless we aggregate everything ourselves,
independently from the main post. This means the application provider (i.e.
comments.com) has to maintain an index of all the comments in a transparent
way that can be reproduced by others in order to avoid censorship issues. We
are still investigating different solutions to help us with data discovery in
a decentralized way.

[Thoughts & Ideas](/blog/category/thoughts-ideas/)

[Research](/blog/category/research/)

[Hyperdata](/blog/category/hyperdata/)

# Previous blog posts.

[View all blog posts](/blog)

[![AKASHA Conversations #5 — Intentional Culture Design for
Moderating](/static/c3d734e207288654ade010406c34342a/14b42/header.jpg)](/blog/2022/05/02/akasha-
conversation-05-decentralized-moderation)

[Moderation](/blog/category/moderation/)

[Governance](/blog/category/governance/)

[Conversation](/blog/category/conversation/)

[Events](/blog/category/events/)

[

### AKASHA Conversations #5 — Intentional Culture Design for Moderating

What is the culture of your workplace? Your education establishment? Your
neighbourhood? If we adopt…

](/blog/2022/05/02/akasha-conversation-05-decentralized-moderation)

By [Philip Sheldrake](/blog/author/philip-sheldrake/)

May 02, 2022

[![The AKASHA Foundation team at OFFSCRIPT
2022](/static/15c6e612bdcbb47badfb90416ab21ae8/14b42/Comporta%20Villa.jpg)](/blog/2022/04/29/the-
akasha-foundation-at-offscript-2022)

[Events](/blog/category/events/)

[Design](/blog/category/design/)

[Conversation](/blog/category/conversation/)

[Moderation](/blog/category/moderation/)

[

### The AKASHA Foundation team at OFFSCRIPT 2022

María Sanmartín and Martin Etzrodt gathered for Offscript - a conference
focused on Web 3 UX and…

](/blog/2022/04/29/the-akasha-foundation-at-offscript-2022)

By [Martin Etzrodt & Maria Sanmartin](/blog/author/martin-etzrodt-maria-
sanmartin/)

April 29, 2022

[![AKASHA Conversations #4 — Designing legitimate moderation in decentralized
social
networking](/static/62859025e753772da19e08c60e815e54/ee604/header.png)](/blog/2022/03/25/akasha-
conversation-04-decentralized-moderation)

[Moderation](/blog/category/moderation/)

[Governance](/blog/category/governance/)

[Conversation](/blog/category/conversation/)

[Events](/blog/category/events/)

[

### AKASHA Conversations #4 — Designing legitimate moderation in decentralized
social networking

AKASHA Conversations is a monthly event where we explore the critical aspects
of decentralized…

](/blog/2022/03/25/akasha-conversation-04-decentralized-moderation)

By [Martin Etzrodt](/blog/author/martin-etzrodt/)

March 25, 2022

## Keep in the loop.

Subscribe to our newsletter.

Subscribe to newsletter

![Keep in the
loop.](/static/0861535edb53edfcb9578bdc137e3d45/47498/newsletter.jpg)

[

# Akasha

](/)

Get in touch, we are friendly people

[](https://discordapp.com/invite/JqqKasJ)[](https://twitter.com/AKASHAorg)[](https://www.facebook.com/AKASHAorg)[](https://github.com/AKASHAorg/)[](https://www.reddit.com/r/AkashaProject)[](https://www.linkedin.com/company/akashaorg/)[](https://www.youtube.com/c/Akashaorg)

Projects

[Ethereum.world](https://ethereum.world/)

[AKASHA.world](https://akasha.world/)

[AKASHA Hubs](/hubs)

The Foundation

[About](/about/)

[Blog](/blog/)

[Careers](/careers/)

[Contact us](/contact/)

[Events](/events/)

[Friends](/friends/)

[Press](/press)

Resources

[Style Guide](https://style.akasha.org/)

[Glossary](/glossary/)

[Legal](/legal/) ·

[Privacy Policy](/privacy-policy/)

CC BY-SA 4.0 AKASHA Foundation

![tracker](https://akasha.matomo.cloud/piwik.php?idsite=2&rec=1&url=https://akasha.org/blog/2019/03/04/bridging-
networks-with-hyperdata)

