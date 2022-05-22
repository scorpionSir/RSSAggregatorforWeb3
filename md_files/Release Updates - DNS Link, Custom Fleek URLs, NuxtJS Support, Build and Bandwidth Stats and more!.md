[Go Back](../../)[Fleek.co](https://Fleek.co)

# Release Updates - DNS Link, Custom Fleek URLs, NuxtJS Support, Build and
Bandwidth Stats and more!

![](https://fleek-team-bucket.storage.fleek.co/thumbnails-blog/Release-Update-
UI-rebrand.png)

We’re happy to bring you another release! This one is special because of all
the request for DNS Link Support in particular. We have also released Custom
Fleek URLs and custom naming of your site, NuxtJS framework auto detection,
some stats on your build minutes and bandwidth, and more!

# Features

## DNS Link Support

You can now set up a DNS Link on your domain or subdomain in just a few
clicks. The flow is quick and will make your domain immediately searchable on
any public IPFS gateway. [Here’s](https://ipfs.io/ipns/fleek.co/) our Homepage
using DNS link being shown off at the ipfs.io gateway!

[ ![DNS](../../static/72016a995912edc60d26be74d05f17be/d9199/DNS.png)
](../../static/72016a995912edc60d26be74d05f17be/a878e/DNS.png)

## Custom Fleek URLs

Change your site’s name and its corresponding on.fleek URL to a more memorable
name. You can change your site easily in the site’s general settings, it will
update the sites name in the site overview page to help organize yourself. It
also makes it easier to remember the url to preview it and make it more
presentable to share!

[ ![Custom Fleek
URL](../../static/3f018129f520f3503308a63950f14f21/d9199/Custom%20Fleek%20URL.png)
](../../static/3f018129f520f3503308a63950f14f21/a878e/Custom%20Fleek%20URL.png)

## NuxtJS Framework Support

VueJS is very popular and NuxtJS is one of its most popular static site
generators. We’re excited to make it super easy to deploy for their users by
auto detecting the framework and having docker images to support any versions.

[ ![Nuxt](../../static/a1afc7ed3e2b3239b766f72f27d09b7c/d9199/Nuxt.png)
](../../static/a1afc7ed3e2b3239b766f72f27d09b7c/a878e/Nuxt.png)

## Build Minutes and Bandwidth Statistics

Keep track of how many build minutes and how much bandwidth the sites in your
team have used throughout the month. If you’re getting close to running out
you can upgrade to the pro plan!

[
![BuildBandwidth](../../static/fabf1dfcbe72930101d20c9635ba1dd3/d9199/BuildBandwidth.png)
](../../static/fabf1dfcbe72930101d20c9635ba1dd3/a878e/BuildBandwidth.png)

# Enhancements

## Support for Git Submodules

We modified and improved the way we clone git repos to account for any
submodules and include them in the deployment successfully.

## DNS Verification UX

We improved the flow of verifying your external subdomain or root domain with
Fleek. The instructions are very clear and it only takes one click. You can
also add a DNS Link to each domain optionally whenever you want.

# Bugs Fixes

## HTTPS redirect

Before if you clicked on a link to a fleek url without https explicit within
the url the user would be redirected to a non secure site. Now the user is
always directed to the secured https site.

## Safari Sign Up

We incurred a Safari sign up error where the user would loop with refreshing
authorization tokens indefinitely. It’s fixed now and we also made sure to
polish up some UI differences across browsers.

## Redirecting Away

During the add a site, create a team, and add a custom domain flows if the
user refreshed the page or was redirected the user would have to start over.
Now you should never lose the page you were on.

## Inviting Team Members

If you invited a team member that had not signed up with Fleek before and
accepted the invite to sign up with a different email, they saw an error. Now
it’s as smooth as butter.

## Reset Password

After you reset your password you are now redirected back to login

# Thanks for Reading

Thanks so much for reading the updates! Sign back in and check out the new
features, enhancements, and bug fixes.

  * [Sign up](https://app.fleek.co) to try for yourself
  * [Join](https://slack.fleek.co/) our Community Chat
  * [Follow](https://twitter.com/FleekHQ) us on Twitter
  * [Read](https://docs.fleek.co/) out our Tech Docs
  * Contact us at support@fleek.co

Published 15 Apr 2020

  * [Announcement](../../tag/announcement/)
  * [Release Update](../../tag/release-update/)

Fleek is all you need to build websites and apps on the new Open Web:
permissionless, trustless, censorship resistant, and free of centralized
gatekeepers. Welcome to the new internet.[](https://www.twitter.com/FleekHQ)

