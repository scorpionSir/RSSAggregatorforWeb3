[Go Back](../../)[Fleek.co](https://Fleek.co)

# What Can Be Deployed on Fleek?

![](https://fleek-team-bucket.storage.fleek.co/thumbnails-
blog/CanDeployCover.png)

What kind of apps and sites can be deployed on Fleek? Can you deploy static
sites? What about dynamic sites? Maybe you are wondering if Fleek would be a
good fit for your project.

Then you are at the right place! In the next few minutes, we’ll discuss what
types of site you can deploy with Fleek.

Oh, and we’ll even showcase some examples to inspire you!

# Static vs Dynamic

You can deploy either a static or a dynamic website on Fleek.

But what’s the difference between the two?

Static websites are read-only. A good example that would be a portfolio site
or a statically-generated blog like the one you are reading right now.

Dynamic sites, on the other hand, are both read and write. Generally, such
sites fetch information from a database to populate its content. Think of the
likes of Twitter and Facebook where you login and the app displays posts or
tweets that are unique to your account.

But if you host a dynamic site you might wonder…

# Dynamic Sites: What about my Backend?

[ ![FEvsBE](../../static/bbe11ed4ccafbddd58190f0110949bf5/25044/FEvsBE.jpg)
](../../static/bbe11ed4ccafbddd58190f0110949bf5/25044/FEvsBE.jpg)

Fleek only hosts your files on IPFS, thus it’s very appropriate for frontends
of all kinds. In many cases, however, the frontend needs to talk to a backend
server.

If that is the case, you must maintain _your own server_. In other words, we
handle the frontend, you handle the backend.

It also means that we do not support server-side rendering…because that would
require a server!

# But what about SPAs?

SPAs, short for Single Page Applications, are a great fit for Fleek. Files
such as Javascript bundles, CSS files and static assets can all rest on IPFS.

SPAs can be either static or dynamic, if they talk to a backend. Either way
Fleek can handle it.

Also, it is worth noting that since we support npm packages, we support any
bundler such as webpack, parcel, etc…

# What about [INSERT EXOTIC FRAMEWORK HERE] ?

[ ![frameworks
everywhere](../../static/d4ad196dac7552500b590db8c0aa29d4/41d8b/frameworks-
everywhere.jpg)
](../../static/d4ad196dac7552500b590db8c0aa29d4/41d8b/frameworks-
everywhere.jpg)

Frontend development is notorious for its enormous arsenal of frameworks of
all kind, from popular to obscure. Don’t believe me? Here’s a [list of over
100 javascript frameworks](https://cssauthor.com/javascript-frameworks/)…

Fleek auto-detects certain frameworks and automatically applies the correct
build settings for you. We will find the correct docker image from our
[dockerhub organization](https://hub.docker.com/orgs/fleek) depending on the
detected framework.

[
![autodetectFramework](../../static/7542c37cd246d3d12da1954d27a5cabb/0ec92/autodetectFramework.png)
](../../static/7542c37cd246d3d12da1954d27a5cabb/0ec92/autodetectFramework.png)
_Some of the frameworks autodetected by Fleek_

That being said, we support many more frameworks than that. _Any_ framework
which is a dependency as an npm package will be supported since we apply a
node-based docker image by default when none is selected.

In addition, if you are using a framework which is neither officially
supported by Fleek nor an npm dependency, there is always the possibility of
creating your own docker image to house your app.

# Real-World Examples Right in Front of Your Eyes

[ ![frontend fleek
app](../../static/8dc6b2ad546e29da5db1e37f814c9c02/d9199/frontend-fleek-
app.png) ](../../static/8dc6b2ad546e29da5db1e37f814c9c02/91b67/frontend-fleek-
app.png) _Our own frontend app is an excellent example of the type of
enterprise-level product you can deploy on Fleek_

Did you know the [Fleek patform was deployed on
Fleek](https://blog.fleek.co/posts/Fleek-On-Fleek)?

This includes this very [blog](https://blog.fleek.co/) you are reading right
now, our [docs](https://docs.fleek.co/) and our [homepage](https://fleek.co/).
So if you have a static site such as a homepage, blog or documentation, you
can deploy it on Fleek just like us!

Do you want to deploy a dynamic site in the form of a complex frontend
application? You can also do it on Fleek, just like we are doing with our own
[app](https://app.fleek.co/).

# Your Turn to Build!

As you can see, we support a wide range of sites. The limit is your
creativity!

Just bring us your app and we take care of the rest!

  * [Sign up](https://app.fleek.co) to try for yourself
  * [Join](https://slack.fleek.co/) the #community slack channel
  * [Follow](https://twitter.com/FleekHQ) us on Twitter
  * [Read](https://docs.fleek.co/) our Tech Docs
  * Contact us at support@fleek.co

Published 11 May 2020

  * [General](../../tag/general/)

Fleek is all you need to build websites and apps on the new Open Web:
permissionless, trustless, censorship resistant, and free of centralized
gatekeepers. Welcome to the new internet.[](https://www.twitter.com/FleekHQ)

