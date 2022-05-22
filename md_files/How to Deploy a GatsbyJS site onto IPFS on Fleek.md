[Go Back](../../)[Fleek.co](https://Fleek.co)

# How to Deploy a GatsbyJS site onto IPFS on Fleek

![](https://fleek-team-bucket.storage.fleek.co/thumbnails-
blog/GatsbySocialimage.png)

Gatsby allows for the creation of static sites in a simple, straightforward
manner. In this tutorial, we will show you how to create a Gatsby project and
deploy it to IPFS thanks to Fleek.

## Creating a Gatsby Project

Let’s start by installing the Gatsby CLI.

`npm i -g gatsby-cli`

Now we can create a Gatsby project.

`Gatsby new name_of_project`

This will create a new sample gatsby project which can be modified according
to your needs. You can run `npm run develop` to see the page in the browser by
going to <http://localhost:8000>.

For now, let’s make some changes to the basic starter site.

[ ![gatsby1](../../static/66cc01f4441adf94eb6fc990cce2cc5a/d9199/gatsby1.png)
](../../static/66cc01f4441adf94eb6fc990cce2cc5a/985a9/gatsby1.png)

Beautiful!

## Deploying Through Fleek

We must create a GitHub repository to store our site so Fleek can pick it up.
For this tutorial, we will use the following repo:
<https://github.com/SamueleA/gatsby-fleek>

Now, we must log to Fleek and add a new site.

[ ![gatsby2](../../static/6f10fe25639ab703c85ffc979e23c453/d9199/gatsby2.png)
](../../static/6f10fe25639ab703c85ffc979e23c453/07a9c/gatsby2.png)

We select the GitHub repo containing the Gatsby project.

[ ![gatsby3](../../static/59fc832591fb535af25b7685aac86e4b/d9199/gatsby3.png)
](../../static/59fc832591fb535af25b7685aac86e4b/00d43/gatsby3.png)

Fleek will determine which build settings to use. It has automatically
detected the Gatsby framework and filled the docker image with `fleek/gatsby`.
This image has Gatsby installed with the latest node.js version. However, my
gatsby app requires node 11, therefore I changed the docker image to
`fleek/gatsby:node-11`.

Click on “DEPLOY SITE” to proceed to the next step.

[ ![gatsby4](../../static/1181f1c7c807ae49a6c8e4588eb9004c/96e92/gatsby4.png)
](../../static/1181f1c7c807ae49a6c8e4588eb9004c/96e92/gatsby4.png)

You will be redirected to the site’s page. We must now wait for the site to be
built and deployed.

[ ![gatsby5](../../static/5d8b3a27661022ca08c85d63196ce824/d9199/gatsby5.png)
](../../static/5d8b3a27661022ca08c85d63196ce824/010c2/gatsby5.png)

Once the deployment is over the site can be accessed and shared. For this
tutorial, the site can be seen here: <https://aged-paper-1829.on.fleek.co/>

[ ![gatsby6](../../static/58d9f54fd6f238ce9d49efccc743d141/d9199/gatsby6.png)
](../../static/58d9f54fd6f238ce9d49efccc743d141/9de76/gatsby6.png)

Note: You might run into pathing issues if you try to view the site through an
IPFS gateway which has the IPFS hash in the url path. EG: ipfs.io/ipfs/qm…  
The simple solution for this is to use a [Gatsby
plugin](https://www.gatsbyjs.org/packages/gatsby-plugin-ipfs/ "Gatsby
plugin").

## Explore more

… and that’s it! Deploying a Gatsby site to Fleek is quick and easy.

As mentioned previously, Gatsby is very useful, among other things, for blog
creation. In the documentation section at the bottom of this post, we have
left some links to learn more about this aspect and what other features Gatsby
has to offer.

Once you are done, come back to Fleek to share your work!

### Documentation

  * [Gatsby video tutorial](https://www.youtube.com/watch?v=8t0vNu2fCCM)
  * [Gatsby docs](https://www.gatsbyjs.org/docs/)
  * [Fleek docs](https://docs.fleek.co/)

Published 19 Mar 2020

  * [Tutorial](../../tag/tutorial/)
  * [Guide](../../tag/guide/)
  * [Gatsby](../../tag/gatsby/)

Fleek is all you need to build websites and apps on the new Open Web:
permissionless, trustless, censorship resistant, and free of centralized
gatekeepers. Welcome to the new internet.[](https://www.twitter.com/FleekHQ)

