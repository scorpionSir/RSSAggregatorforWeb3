  * [Home](/)
  * [Contact](/contact)
  * [Services](/services)
  * [Projects](/projects)
  * [Community](/community)
  * [Blog](/blog)

Menu

#  [![ScopeLift](//images.squarespace-
cdn.com/content/v1/54b81e72e4b0fee4b01a42e9/1581018368646-GMT0JDHOVLSGDECYFQVQ/SCOPELIFT-
long-cropped.png?format=1500w)](/)

Street Address

Philadelphia, PA

Phone Number

Your Custom Text Here

# [![ScopeLift](//images.squarespace-
cdn.com/content/v1/54b81e72e4b0fee4b01a42e9/1581018368646-GMT0JDHOVLSGDECYFQVQ/SCOPELIFT-
long-cropped.png?format=1500w)](/)

  * [Home](/)
  * [Contact](/contact)
  * [Services](/services)
  * [Projects](/projects)
  * [Community](/community)
  * [Blog](/blog)

#  [Phoenix on Heroku: Our Experience Getting CoinRecap.io
Deployed](/blog/2018/3/1/phoenix-on-heroku-our-experience-getting-coinrecapio-
deployed)

March 1, 2018 [Ben DiFrancesco](/blog?author=54b81e71e4b06e38ad58f2f2)

Heroku is a powerful service that abstracts away most of the typical DevOps
work one must do to deploy a modern web app to the cloud. It’s therefore ideal
for getting a service off the ground quickly. But is it a good fit for Elixir
and Phoenix?

In this short post, we’ll discuss our experience contributing to the
development of [CoinRecap.io](https://coinrecap.io), a daily email service
that analyzes and summarizes cryptocurrency market trends. CoinRecap is built
with Elixir and Phoenix and is deployed on Heroku.

Though you might find some resources online that suggest Heroku doesn’t pair
well with Phoenix, this has not been our experience. In fact, Heroku works
perfectly for deploying a Phoenix app as long as you’re aware of a few minor
caveats, and can live with them.

### Caveat One: Dyno Restarts

Because Heroku restarts its [dynos](https://www.heroku.com/dynos) nightly,
you’ll want to make sure your app does not rely on long running, in memory
processes. In particular, if you’re persisting data in ETS tables, Agents, or
GenServers, you’ll have to live with the fact these will be cleared nightly.
This is the caveat that is most likely to be a deal breaker for a Phoenix app
that is just getting started. These are powerful tools in an Elixirist’s tool
belt, and having to eschew them might be painful, even for a young app. In
CoinRecap’s case, this limitation did not present a problem. If it does for
yours, you’ll have to consider working around it or using a different hosting
service.

### Caveat Two: Dyno Connections

The remaining caveats are less likely to impact an app that is just getting
off the ground, though they might have an impact as it scales. Heroku limits
the number of simultaneous connections to about 50 per dyno and does not allow
dynos to communicate directly with each other. This first limitation puts an
artificial cap on the real-time channels your app can utilize, one far below
what Phoenix is capable of. The second curtails your ability to utilize
distributed clustering, which is a powerful feature of the BEAM which allows
you to scale your app across systems without rearchitecting it into micro
services.

For a product like [CoinRecap](https://coinrecap.io), which is still in the
early phase of scaling, these limitations are acceptable. Simply adding Heroku
dynos gives plenty of headroom to grow the app while allowing the team to
focus on developing the products core functionality: summarizing and surfacing
insights in the dynamic cryptocurrency market. In fact, because Elixir is so
performant, we’ve found dyno memory loads to be minuscule and our throughput
to be extremely high. So while you might eventually have to part with Heroku
to scale your app up, you’ll likely find you have more headroom than you
expect with just a few dynos, unless your app absolutely requires lots of
persistent connections.

### Practical Tips

Before wrapping up, we’ll offer a few practical tips for deploying to Heroku
that should make the experience even more seamless.

  *  **Use the[HashNuke Elixir build pack](https://github.com/HashNuke/heroku-buildpack-elixir)**. While it’s not provided by Heroku first party, it works great, has been well maintained, and has everything you need to get your app running on Heroku in minutes.
  *  **Always rebuild on deploy**. For various reasons related to dependency management and the compilation process, we’ve found it’s best to always rebuild the app on deploy. Your deploy times will be a bit longer, on the order of 5 minutes for CoinRecap, but you’ll save yourself headaches down the road debugging mysterious compilation errors. To do this, add "always_rebuild=true" to your "elixir_buildpack.config" file.
  *  **Use[DNSimple](https://dnsimple.com) for your DNS config**. If you want SSL (and in 2018, you absolutely should!) then you’ll find it surprisingly hard to set up DNS properly with Heroku using a standard domain registrar’s DNS services.  This is because most registrars don’t support more advanced DNS features like ANAME or ALIAS records. Note that you can keep your domain registration with a service like Hover or Namecheap while still using DNSimple for DNS. Their plans start at 5 dollars a month and work great with Heroku and SSL.

If you’re getting a new app off the ground using Elixir and Phoenix, Heroku is
a great choice. It simplifies hosting and deployment and allows you to focus
on what matters to you: building your app! While Phoenix may not be a first
party target for the platform, it's still great fit for a young app, as long
as you're aware of the tradeoffs we've covered and able to deal with them.

 _For more nuts and bolts on deployment to Heroku, check out[this awesome
guide](https://hexdocs.pm/phoenix/heroku.html) on HexDocs. It covers the setup
process in detail and also touches on some of the tradeoffs we’ve discussed
here._

[<- All In On Crypto: ScopeLift's Next Chapter](/blog/all-in-on-crypto-
scopelifts-next-chapter)[360|iDev 2017: Swifty By Default
->](/blog/360idev-2017-swifty-by-default)

[ ](https://twitter.com/BenDiFrancesco) [ ](https://github.com/apbendi) [
](https://www.linkedin.com/pub/ben-difrancesco/9b/426/680)

© ScopeLift 2021

