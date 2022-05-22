[Go Back](../../)[Fleek.co](https://Fleek.co)

# Fleek + IPFS: Web3 Deployment Simplified

![](https://fleek-team-bucket.storage.fleek.co/thumbnails-blog/fleek-plus-
ipfs.png)

## Overview

[Fleek.co](https://Fleek.co/) offers a seamless workflow. It offers all the
tools needed to deploy and manage sites on IPFS. Focus on content and code.
Fleek handles the rest.

## IPFS & Data Integrity

IPFS stands for Interplanetary File System. It’s a distributed file system
used for storing and sharing files, data and websites. The system has unique
benefits such as decentralization and data integrity. More information
[here](https://docs.ipfs.io/introduction/overview/).

[ ![Photo by Nicolas Picard on
Unsplash](../../static/48e5b451bba2dc259756981e807b4d37/6a068/unsplash_1.jpg)
](../../static/48e5b451bba2dc259756981e807b4d37/93719/unsplash_1.jpg)

IPFS is decentralized by creating a peer-to-peer network that can be hosted
anywhere. It provides data integrity _by linking to its content_ instead of
location. For example:

<https://ipfs.io/ipfs/QmWATWQ7fVPP2EFGu71UkfnqhYXDYH566qy47CnJDgvs8u>

[
![ipfshashbrowser](../../static/f721234c488a53da1cc6c8da22a22787/d9199/ipfshashbrowser.png)
](../../static/f721234c488a53da1cc6c8da22a22787/d69c4/ipfshashbrowser.png)

The QmWAT… is the hash of the content “Hello World”.

If someone were to change “Hello World” to “Goodbye World”, the hash **and
thus** the link will change.

<https://ipfs.io/ipfs/QmP8CvqzGRgH3WyeVKm8F1Pr6S4PGfuaCx6NVWuc929HWf>

[ ![goodbye
world](../../static/9ab1831e11aeb9cdcbb684bd84c8d206/d9199/goodbye_world.png)
](../../static/9ab1831e11aeb9cdcbb684bd84c8d206/d69c4/goodbye_world.png)

It’ll be impossible to change the content without changing the link, which is
great for data integrity. But…

## What if the content changes?

If the content changes, the hash will change and the link will change.

[ ![new content -> new hash -> new
link](../../static/0a98a23becbf96506ef78c297d0c6e2b/914ae/newcontent-
newhash.png) ](../../static/0a98a23becbf96506ef78c297d0c6e2b/914ae/newcontent-
newhash.png)

This can be a headache if you‘re adding/updating content. Imagine a blog with
new articles everyday. You’ll have to generate a new hash every time something
changes.

Everything downstream will also be changed. If you have a domain name
(myawesomeipfswebsiteblog.com), then you’ll have to update the[
values](https://medium.com/coinmonks/how-to-host-a-website-on-ipfs-with-
dns-82f1f2fe6361) to the new hash.

[ ![Photo by Aditya Chinchure on
Unsplash](../../static/d3823ca0cccdd57b9e60a7269a48d89c/6a068/waterfall.jpg)
](../../static/d3823ca0cccdd57b9e60a7269a48d89c/93719/waterfall.jpg)

## Fleek

Fleek aims to simplify web development into one seamless workflow. Simply push
changes to Git and Fleek will automatically update, pin and deploy changes
downstream.

[
![terminalsupplychain](../../static/985212aeb4967052a896161b35c1a1f7/d9199/terminalsupplychain.png)
](../../static/985212aeb4967052a896161b35c1a1f7/4ef40/terminalsupplychain.png)

Some features:

  * Fleek accommodates many frameworks such as gatsby, jekyll, create-react-app etc.
  * Fleek also handles DNS records. Either purchase a domain from them or point it to a domain you purchased elsewhere.
  * No need to manually update hashes, TXT values etc.
  * Fleek provides a [CID](https://docs.ipfs.io/guides/concepts/cid/)(content identifier) for more IPFS features such as verification and self hosting.

[
![deploypage](../../static/c8dc01a91bd67fbe46e9fbf7ca21ef9c/d9199/deploypage.png)
](../../static/c8dc01a91bd67fbe46e9fbf7ca21ef9c/5440e/deploypage.png)

## More Info

  * Join our [Community Chat](https://slack.fleek.co/)
  * Follow us on [Twitter](https://twitter.com/FleekHQ)
  * Contact us at support@fleek.co

Check out [Tech Docs](https://docs.fleek.co/)

Published 3 Mar 2020

  * [Informational](../../tag/informational/)
  * [Guide](../../tag/guide/)

Fleek is all you need to build websites and apps on the new Open Web:
permissionless, trustless, censorship resistant, and free of centralized
gatekeepers. Welcome to the new internet.[](https://www.twitter.com/FleekHQ)

