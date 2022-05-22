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

![Authentication on Ethereum
World](/static/f6231907297f8ea9cc96a836d48db6fd/2a43b/header.jpg)

[Dev](/blog/category/dev/)

## Authentication on Ethereum World

By [Marius Darila](/blog/author/marius-darila/)

·

February 28, 2020

The release of [Ethereum World](https://ethereum.world/) v0.1 will include a
lot of improvements in terms of UX when compared with the current
beta.akasha.world application. This will be possible because of specialized
web services that handle complex tasks which previously were executed only on
the client-side (e.g. search indexing).

Some of these services will require user authentication. One example would be
a service that stores the user's preferences on a database which is
synchronized afterwards on all the devices used to access Ethereum World.

For v0.1 of Ethereum World all the visitors will be able to authenticate using
only their Ethereum key without having the need to go through the process of
registration or having to remember a username/password combination.

The way it works:

  * the user's Ethereum key is used to create a signature from an authentication message;

    
    
    // signer https://docs.ethers.io/ethers.js/html/api-wallet.html#signer-api
    // the message can be something like
    // 'authenticate on ethereum.world on 2020/02/29'
     const sig = signer.signMessage(AUTH_MESSAGE)

  * the signature `sig` is sent afterwards to a web service which validates it and generates a [JWT](https://en.wikipedia.org/wiki/JSON_Web_Token)
  * the JWT is used to store claims, for v0.1 of Ethereum World we're using the [standard claims](https://tools.ietf.org/html/rfc7519#section-4)
  * the web service uses also an Ethereum key to sign the JWT and is saved as the Issuer in the standard claims list

    
    
    {
     Issuer: "0x0A93720048a3E25cD72346bD802DeF4Dc7316b5" // ewa.akasha.eth
     Subject: "0x0A93720048a3E25cD72346bD802DeF4Dc7316b2" // user's public eth address
     Audience: "ethereum.world"
    ...
    }

  * the user receives a token that can be used for 24h to authenticate on all web services that Ethereum World uses, this must be specified in the [bearer](https://tools.ietf.org/html/rfc6750) authorization format on the [request header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization) , e.g.: `Authorization: Bearer eyJhbGciOiJFUzI1.eyJzaWciOiI.-CYOci_mOfR`

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

![tracker](https://akasha.matomo.cloud/piwik.php?idsite=2&rec=1&url=https://akasha.org/blog/2020/02/28/authentication-
on-ewa)

