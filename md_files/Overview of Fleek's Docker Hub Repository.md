[Go Back](../../)[Fleek.co](https://Fleek.co)

# Overview of Fleek's Docker Hub Repository

![](https://fleek-team-bucket.storage.fleek.co/thumbnails-blog/docker-hub-
overview.png)

Fleek has an official Docker Hub repo! We store all our official Docker Images
there. In this post, we’ll introduce you to its content so you can use it to
create the best site ever.

## What is Docker Hub

Docker Hub is like Github, but for Docker Images. When you deploy a site
through Fleek and are filling the build settings, the docker images field
corresponds to a docker image resting in Docker Hub.

[ ![1 build
settings](../../static/09e3b04624811d282e40836bbdce859c/d6331/1-build-
settings.png) ](../../static/09e3b04624811d282e40836bbdce859c/d6331/1-build-
settings.png)

## Our Repositories

[ ![2 list of
repos](../../static/3815147350018f14461b3e681769f840/d9199/2-list-of-
repos.png) ](../../static/3815147350018f14461b3e681769f840/20785/2-list-of-
repos.png)

Fleek’s repositories can be found
[here](https://hub.docker.com/orgs/fleek/repositories). You will find images
for all the frameworks we are officially supporting such as Gatsby, Hugo, etc…

When creating a site, you can specify one of those images by filling the
docker image field in the build settings to the corresponding image. For
instance, to use the Gatsby docker image enter `fleek/gatsby`.

## Specifying the Node version

[ ![3 gatsby
builds](../../static/24a8baa0551b0c8a04e03bfbd16e1da8/c391c/3-gatsby-
builds.png) ](../../static/24a8baa0551b0c8a04e03bfbd16e1da8/c391c/3-gatsby-
builds.png)

Many frameworks rely on a specific Node.js version, otherwise, the build
fails. By default, our docker images will use the latest Node.js version
available.

You can specify a specific Node version through the Docker tag. For example,
look at the [repository for
Gatsby](https://hub.docker.com/repository/docker/fleek/gatsby).

As you can see in the tags section, many node versions are available. For
example, if we need Gatsby and Node 10, we would use the image
`fleek/gatsby:node-10`.

## The images’ Cource Code

If you wish to consult the Dockerfile from which those images are built, you
can consult the Github repository with all the Dockerfiles from which the
images built.

<https://github.com/FleekHQ/site-builder-docker-images>

## Farewell!

We hope you enjoyed this tour through Fleek’s Docker Hub! If you feel we are
missing docker images or have suggestions, do not hesitate to contact us!

  * [Sign up](https://app.fleek.co) to try for yourself
  * [Join](https://slack.fleek.co/) our Community Chat
  * [Follow](https://twitter.com/FleekHQ) us on Twitter
  * [Read](https://docs.fleek.co/) out our Tech Docs
  * Contact us at support@fleek.co

Published 4 Apr 2020

  * [Docker](../../tag/docker/)
  * [Resource](../../tag/resource/)

Fleek is all you need to build websites and apps on the new Open Web:
permissionless, trustless, censorship resistant, and free of centralized
gatekeepers. Welcome to the new internet.[](https://www.twitter.com/FleekHQ)

