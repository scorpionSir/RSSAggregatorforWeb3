[Go Back](../../)[Fleek.co](https://Fleek.co)

# No Coding Required: Make a Website With the Forestry CMS and Fleek!

![](https://fleek-team-bucket.storage.fleek.co/thumbnails-blog/NoCode.png)

Fleek is the easiest way to deploy a website… but what about actually _making_
one? Whether you do not know how to code, or you _do_ know but lack the time,
the solution boils down to three letters:

CMS

CMS stands for Content Management System. A CMS allows you to focus more on
the _content_ of your website and less on the technicalities involved in
getting it running, which is very useful for those who want a simple blog or
portfolio website.

In this post, we will learn about the Forestry CMS and how you can use it to
create a site quickly, without even knowing how to code. Then, we’ll use Fleek
to share it with the world.

# What is Forestry

[ ![cms meme](../../static/2ac2c4cccc392b265677166050d7c23c/9453e/cms-
meme.jpg) ](../../static/2ac2c4cccc392b265677166050d7c23c/9453e/cms-meme.jpg)

The [Forestry CMS](https://forestry.io/) can spring a website into existence
from beautifully made templates. An intuitive UI allows users to create
content in a visual manner. The entire process doesn’t require any coding
knowledge.

The benefits of such an approach include both simplicity and speed of
delivery.

# Workflow Development Overview

Ok, so there’s the Forestry CMS to make a website easily, but how do we share
it with the world? The diagram below will enlighten you on the process.

[ ![forestry fleek
diagram](../../static/eda8e35da7947a6b69088ed7c8cb14e8/d9199/forestry-fleek-
diagram.png) ](../../static/eda8e35da7947a6b69088ed7c8cb14e8/68947/forestry-
fleek-diagram.png)

We will use the Forestry CMS to create the website, add content such as blog
posts or new pages, and push any updates to a Github repository. Then, we will
set up Fleek to listen to changes to the Github repository and deploy our
website.

In other words, once the workflow is set up, the only thing the user needs to
do is to write content, and the combination of Forestry and Fleek will take
care of the rest automatically.

# Step By Step

Below is a step by step guide on how to create a simple blog on Forestry and
deploy it on Fleek. Once everything is set up, any changes to your site
through the CMS will reflect on the Github repository and update the site.

## 1\. Create a Site with Forestry

Forestry has several templates for portfolios and blogs. As an example we’ll
create a blog and we will use the `brevifolia` template to get us started.

Forestry will ask what framework to use for the site. The choices include
Gatsby, Hugo, Jekyll. Any of these frameworks will work with Fleek, but we
will choose Gatsby for this guide. In the end, the framework doesn’t matter
that much since we will use the CMS to create the content.

[ ![template
select](../../static/697c4e7afe2539f6fd0c59bf6f5d724a/d9199/template-
select.png) ](../../static/697c4e7afe2539f6fd0c59bf6f5d724a/2130b/template-
select.png)

On the site creation screen, we must specify that we want to use Github. As
explained previously, we want Forestry to push any changes made to the site to
Github so Fleek can make the deployment.

Finally, select `Github` as the Git Provider, specify a name for the github
repository and create the site.

[ ![github select](../../static/e8ee89d362af6a9ade8bac73bdf772b8/d9199/github-
select.png) ](../../static/e8ee89d362af6a9ade8bac73bdf772b8/bc3ae/github-
select.png)

Congratulations! You have created your site!

## 2\. Create Content

[ ![content
create](../../static/f086e3ef180878f702a59784a2a0ed8c/d9199/content-
create.png) ](../../static/f086e3ef180878f702a59784a2a0ed8c/f2331/content-
create.png)

Creating new content is fairly straightforward. There are three components to
this template: `Blog Posts`, `Author List` and `Info Page`. You can add more
sections if needed in `Settings` => `Sidebar`.

You can modify those to your liking. In particular, you might want to delete
the default blog posts and create your own. The interface is similar to
writing an email so there’s no coding knowledge required to add content. All
that you need to focus on is writing the content for the blog!

Take some time to familiarize yourself with the interface since it will allow
you to further customize the site.

What do you do once you are ready to share your site with the world?

Host it on Fleek, of course!

## 3\. Deploy With Fleek!

First, create a new Site.

The Fleek new site creation flow will ask for the Github repository containing
the site. Select the repository we have been using with Forestry.

[ ![select repo
fleek](../../static/5f5abefb1868fa5b7d9b8e2394ce4f51/d9199/select-repo-
fleek.png) ](../../static/5f5abefb1868fa5b7d9b8e2394ce4f51/68947/select-repo-
fleek.png)

Then, we must select the Build settings. Luckily, Fleek wil auto-detect the
fact that we are using Gatsby. The only problem is that Forestry is using node
10 instead of the most recent node version. Therefore, simply change the
Docker Image to `fleek/gatsby:node-10`.

If you are using another framework and it doesn’t work and you don’t
understand why, it is likely that the node version is the issue.

Clicking on `Deploy Site` will start the deployment process.

[ ![new site](../../static/1e95663a11e41c1beed7cd14aceeeb7c/8ce22/new-
site.png) ](../../static/1e95663a11e41c1beed7cd14aceeeb7c/8ce22/new-site.png)

Fleek will provide a free domain name which you can modify in the settings.
You can also use your own domain name.

And that’s it! Your workflow is now set up.

The next time you log in to Forestry and make an update to your blog, Forestry
will push the changes to Github, Fleek will pick up on it and update your
site.

# No More Excuses!

We’ve just seen how it was possible to make an awesome website _without
writing a single line of code_!

It’s pretty amazing that web development tooling has come this far so that
literally anyone can have his voice heard on the internet. It’s so amazing, in
fact, that it brushes away any excuses for _not_ making that awesome blog of
portfolio site you always dreamed of.

The great tools are out there. They are only awaiting your special touch!

  * [Sign up](https://app.fleek.co) to try for yourself
  * [Join](https://slack.fleek.co/) the #community slack channel
  * [Follow](https://twitter.com/FleekHQ) us on Twitter
  * [Read](https://docs.fleek.co/) our Tech Docs
  * Contact us at support@fleek.co

Published 1 Jun 2020

  * [Tutorial](../../tag/tutorial/)
  * [CMS](../../tag/cms/)

Fleek is all you need to build websites and apps on the new Open Web:
permissionless, trustless, censorship resistant, and free of centralized
gatekeepers. Welcome to the new internet.[](https://www.twitter.com/FleekHQ)

