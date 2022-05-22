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

![AWF - A Dev Team
Overview](/static/30c4160887b979d7ce418abc044ee532/2a43b/header.jpg)

[Dev](/blog/category/dev/)

## AWF - A Dev Team Overview

By [Sever Abibula](/blog/author/sever-abibula/), [Valentin
Cotea](/blog/author/valentin-cotea/) & [Marius Darila](/blog/author/marius-
darila/)

·

December 19, 2019

This year (2019) on World Press Freedom Day, we announced the AKASHA World
Framework (AWF) - a tool for the creation and cultivation of bespoke networks
- through the post [_AKASHA Reloaded: Three Spins Around The Sun
Later_](https://akasha.org/blog/2019/05/03/akasha-reloaded) _._

The main purpose of the AWF is to facilitate the development of what we're
calling [worlds](https://akasha.org/blog/2019/11/21/what-is-akasha-reloaded-
what-is-ethereum-world), so in our vision it should deliver:

  * a set of UI elements to be reused across all the worlds and apps;
  * a library for API, caching and data persistency; and
  * an application-loader system.

In order to check the first requirement, the UI elements, we started with an
idea that AWF will be used in-house, but also by other developers to build
their own web3 apps; in order to allow that to happen we embraced the
philosophy of [atomic design](https://bradfrost.com/blog/post/atomic-web-
design/).

**How does this translate into our technical choices?**

For building a scalable and modern UI there are so many options nowadays it
can feel overwhelming, but we wanted to make sure the choices we make now are
based on sound principles, and will be easy to maintain in the future.

## What we are using to build our UI

The stack that is the foundation of our UI is composed of
[react.js](https://reactjs.org/), [grommet](https://v2.grommet.io/), [styled
components](https://www.styled-components.com/), and
[storybook.js](https://storybook.js.org/). Our team was already experienced
with react, and it has a huge ecosystem around it, so this was an easy choice.

To make sure our UI components are as encapsulated and easy to use as possible
we decided to go for styled components, and this led us to adopt a component
library that is based on styled components.

Grommet is a library that we fell in love with, well documented and easy to
extend and adapt to our needs. This time we learned from our mistakes and
decided to use [typescript](https://www.typescriptlang.org/) on the front end
as well. Considering our big hopes for the growth of this project, typescript
provides the consistency needed to properly scale our framework.

And finally, we decided to use storybook to showcase our components, making it
easier for outside developers to check out the functionality of our
components, and making collaboration between the dev team and design team much
easier.

To follow the guidelines of atomic design we started by implementing the small
components first, such as buttons, basic cards, and modals and then composed
them into progressively more complex components that can be plugged directly
into the layout of a micro-app.

[ ![storybook](/static/decf6d467660e3230d66e6dada940f1c/fcda8/storybook.png)
](/static/decf6d467660e3230d66e6dada940f1c/9634a/storybook.png)

Another interesting choice on the frontend side was on what library to use for
our rich text editor. We wanted something open-source, lightweight and that
won't get in our way when we develop custom features for publishing. After a
few tries we went with [slate.js](https://www.slatejs.org/), a well-
documented, react-based, and very flexible editor framework.

## What we are using to build the API library (SDK)

Initially when we started to work following the AKASHA Reloaded initiative, we
tried to find an application architecture that would solve the extensibility
and isolation problem that we had for the beta version of AKASHA because the
majority of the work was being put into fixing regression bugs.

In an ideal scenario, each module of the application would have these
features:

  * doesn't have in its dependencies list other modules;
  * can access API methods from other modules without having to import the entire library;
  * can run isolated tests without too much boilerplate;
  * can be swapped easily without breaking the entire application; and
  * low overhead, is loaded only when needed.

Having this list in mind we came up with a solution which uses the [dependency
injection](https://en.wikipedia.org/wiki/Dependency_injection) pattern,
basically it's a container where you can register modules and their exported
methods as services.

For example, lets say that we have a service that looks like:

    
    
    const service = () => {
      const fullName = (firstName, lastName) => `${firstName} ${lastName}`;
      return { fullName }
    }
    // And it registers with:
    export default { service, name: "Utils" }
    // This is a service factory

This service can be used from other modules/services:

    
    
    const otherService = (invoke) => {
      const fullNameAndAge = (first, last) => {
        const { fullName } = invoke("Utils");
        return fullName(first, last) + "42";
      }
      return { fullNameAndAge }
    }
    
    
    export default { service: otherService, name: "UtilsExtra" }

This small example checks the first 3 items from the list of desired behavior:

  * the `UtilsExtra` module doesn't import explicit the `Utils` module;
  * it can access the `fullName` method through the invoker; and
  * it can run isolated tests without too much boilerplate, it would require just a mock of the invoked method:

    
    
    const invoker = function(moduleName) {
      return { fullName: () => {} }
    }
    
    
    // when registering the service we can pass the invoker
    const registeredService = service(invoker);
    
    
    // add isolated tests starting from here :

[ ![service invoker](/static/9e6b74895224a10952ef2a36bbd5160b/fcda8/service-
invoker.png) ](/static/9e6b74895224a10952ef2a36bbd5160b/084e2/service-
invoker.png)

## What we are using for the application management

When we started to draft the first specs of Ethereum World, we came up with an
architecture that allowed as to develop different parts of the app
independently from each other (kind of a "plugin" system). After a few
iterations on this concept we ended up with an architecture called "[micro-
frontends](https://micro-frontends.org/)" on which we started to develop a
system that will allow instantiation of different parts of the application
(micro-apps).

Even though the idea of micro-frontend is simple, we wanted to avoid isolating
ourselves behind some "not-so-popular" concepts and APIs like [Custom
Elements](https://developer.mozilla.org/en-
US/docs/Web/Web_Components/Using_custom_elements), and leverage the "popular"
frontend libraries (React, Angular, Vue, etc) instead.

So, after a little research, we have discovered an interesting library called
[Single-SPA](https://single-spa.js.org/) which we concluded would fit our
needs. Two of the main features that we inherit by using Single-SPA and that
we were interested in:

  * **Modularization.** Historically we spent a lot of time doing maintenance work over a monolithic web application (especially upgrading dependencies, state management, and redesign were getting harder as the application became bigger). We've learned a lot from our previous application (AKASHA Web dapp) and we wanted to avoid a monolithic app.
  * **Framework agnostic.** What if, in the future, we want to switch from one library/framework to another? Going with a monolithic app this would be almost impossible. Rewriting the whole app from scratch wouldn't be an option. Single-SPA would allow us to gradually migrate from one library to another. It would even let us develop micro-apps using different technologies (let's say React, Vue, Svelte) and use them in the same page.

Then we have started to build a micro-application loader on top of this
library which will allow us to instantiate/render a micro-app on specific
pages (routes), leading us to the current architecture:

[ ![single spa](/static/1d3a6704f57dd4269863c7ee856a98cc/fcda8/single-spa.png)
](/static/1d3a6704f57dd4269863c7ee856a98cc/d4c13/single-spa.png)

## How does it work?

The entire concept is based around a "world." A world is basically an
application that features a set of preinstalled micro-apps that are specific
to a community. For example, Ethereum World will have profiles and article
feed micro-apps preinstalled. Users are free to install any other app that is
available, locally, in their browser.

**This means that any developer can write a micro-app and then distribute it
inside any world.**

How will the design system fit into a micro-app? Just import from our design
library the component you need into the micro-app, pass it the required props
and you're good to go! It's easy to extend the styles of each component to
suit the specific need of the layout by leveraging [styled
components](https://www.styled-components.com/), and they come with theme-able
props, allowing the developer to easily customise the look of their micro-app.

In order to work, a micro-app needs to implement a simple API that will let
our SDK application loader register it on demand. The AKASHA SDK is a
collection of modules and services that can be used to create an
AKASHA`world`. It contains also the lookup/verify logic for packages (plugins)
and it also handles things like external API access, caching, data
persistency, and client-side routing; on top of this all the registered
service callbacks are transformed into `observables`.

For example, at the moment of writing the API looks like this:

    
    
    // app-register.js
    {
     // this micro-app will load when the route is
     // www.example.com/search
      activeWhen: {
        path: '/search',
      },
      // UI loading logic - currently managed by single-spa-react
      loadingFn: () => import('./components'),
      name: 'my-search-app', // app's internal name
      sdkModules: ["Search"], // sdk modules initialization (more on this later)
      title: 'My Search App', // Page title
    }

> Note: the API may change by the time we make it open-source
    
    
    // components.js
    import {SearchField, DropDown} from '@akasha/design-system';
    
    const MySearchPage = () => {
      handleSearch = (searchStr) => {
        // get some search results
        sdk.search.findName('John')
      }
      return (
        <div>
          <SearchField onSearch={handleSearch} />
          <Dropdown>
            ... show search results
          </Dropdown>
        </div>
      )
    }
    
    
    // sdk/search.service.js
    
    const service = () => {
      const findName = (startsWith) => "John Doe";
      return { findName }
    }
    export default { service, name: "Search" }

Now, whenever you visit Ethereum World/search, this micro-app will be loaded
and executed giving you a search functionality.

**If this post has inspired you;** if you are into self-sovereign technologies
to advance human agency; if you are driven to work with cryptonetworks for
societal good; if the concept of a collective mind blows your own; or if a
combination of any of the above resonates with you [check out our job
listings](https://akasha.org/careers/).

You could be just the puzzle piece we're looking for...

[Dev](/blog/category/dev/)

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

![tracker](https://akasha.matomo.cloud/piwik.php?idsite=2&rec=1&url=https://akasha.org/blog/2019/12/19/awf-
a-dev-team-overview)

