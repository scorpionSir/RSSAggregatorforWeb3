[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/72637ffe58eb&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![bluewallet](https://miro.medium.com/fit/c/64/64/1*DN1s_rSbq322ReCPPox6ag.png)](https://medium.com/bluewallet?source=post_page
-----72637ffe58eb--------------------------------)

Published in

[bluewallet

](https://medium.com/bluewallet?source=post_page-----
72637ffe58eb--------------------------------)

[![Igor
Korsakov](https://miro.medium.com/fit/c/96/96/0*NeqAGkfF31rtTDfH.)](/@overtorment?source=post_page
-----72637ffe58eb--------------------------------)

[Igor Korsakov](/@overtorment?source=post_page-----
72637ffe58eb--------------------------------)

Follow

Dec 25, 2019

·

6 min read

 **Preparing for war — how was 2019 and a glimpse of the future**

2019 was a great year for BlueWallet. Although it is a new wallet and still in
its infancy, we did get some some [media
coverage](https://www.coindesk.com/bitcoins-lightning-comes-to-apple-
smartwatches-with-new-app), we did get some [recognition from industry
experts](https://docs.google.com/spreadsheets/d/1aZ1zbaUEzCo9NCctN8-eL2VLIiSdY009tTJvRXDUWEw/edit#gid=0)
and we did get [some users](https://t.me/bluewallet) to remind us how much we
suck and how much better it can still be. All that, working on the project on
our free time in a pure open source fashion.

This year blew away our wildest expectations on what we thought we could
achieve. To give you a bit of perspective, at this time last year we were
releasing the android version of the app and our Lightning wallets feature
right before Christmas. And probably, at that time, most of you hadn’t really
heard about Blue.

Talking about Lightning. While the Lightning Network slowly matures, and after
doing our part to put it on the spotlight and bringing the attention it
actually deserved. We decided to take a step back and work on the layer that
really matters. The base layer.

In the core, BlueWallet is (and always was) a non-custodial on-chain [bitcoin
wallet](https://bluewallet.io), born out of the frustration and ashes of the
2017 Bull market. When fees were high and the majority of wallets still had
not implemented segwit and flexible fees. Paying $20 in fees for a transaction
because your wallet’s fee estimation was broken? That was a real deal back
then.

The very first release of BlueWallet fixed exactly that: segwit, flexible fees
(starting from 1 sat/byte), and RBF (replace-by-fee).

During the next cycle of adoption (this is how I like to call the bull-run) I
expect to see exactly the same thing we saw in 2017: with that many people
discovering the advantages of Bitcoin and making their first happy
transactions. The block space will again be an extremely scarce commodity.

After another block reward halving, a more mature fee market will develop, and
we will witness a natural competition for block space. This is why I think it
is important to prepare for that in advance: your bitcoin wallet app (as a
customer-facing software) should be the one to act in your best interests,
trying to save as much pennies on transactions as possible and, at the same
time, give you the full control you need and should have.

In preparation for that, at BlueWallet we implemented:

  *  **CPFP — Bump transaction** (child-pays-for-parent) — a technique that allows you to spend incoming transaction that is unconfirmed by sending it to your another address, but with the total fees higher than the original transaction. This helps if it takes forever for your incoming transaction to confirm on the blockchain.
  *  **RBF — Bump transaction** (replace-by-fee) — if you sent a transaction and it’s still unconfirmed you can replace it with the one with higher fees, making it more attractive for miners to mine, thus, speeding up the confirmation.
  *  **RBF — Cancel transaction** — a technique similar to regular RBF, but where the replacement transaction’s output is the address you control, thus, paying yourself, effectively cancelling the transaction.
  *  **Batch send** — when creating a transaction add as many payees as you want. This helps to save on fees when having to pay multiple destinations. Making a nice UI/UX on this one was a challenge.
  *  **Flexible fees** (starting from 1 sat per byte) and fee recommendations fetched from a real up-to-date bitcoin node.
  * Finally, [from now on, we are **promoting BIP84 Native SegWit wallets as the default wallet**](https://twitter.com/bluewalletio/status/1207311114209497089) when users create a new wallet. We were warned and actually advised against that, as that triggers a stream of complaints from users who can’t withdraw coins from exchanges because exchanges still don’t recognize ‘bc1……’ addresses. But it’s time. Really. Users should take their complaints to obsolete exchanges. Native segwit will allow saving on fees even more.

I like to repeat that **BlueWallet is preparing for war** , and this war will
be for block space. Once another billion of Earth inhabitants realize the
benefits of hard, censorship-resistant and non-confiscatable money.

If this is the kind of fight you want to be part of, protecting the Bitcoin
user interests over miners and corporate players, [**you know where to
go**](https://github.com/BlueWallet/BlueWallet). And you are much welcomed!

![](https://miro.medium.com/max/1400/0*wzOrnxP3ajASE1jK)

Bluewallet vs Blockchain wallet

That was not the only features we were busy with. Among many, some **new and
also remarkable features** :

  * Connect to your own Bitcoin Node through Electrum server for maximum self-sovereignty, no SPVs, full node fashion.
  * Watch-only ZPUB wallets. Just scan the QR code with a ZPUB or input a ZPUB into the text field directly. XPUB and YPUB are supported as well.
  * With recent transition to PSBT under the hood, we added a workflow to have your transaction signed on your hardware wallet in a pure air-gapped fashion. Just mark your watch-only ZPUB wallet as working with an external HW wallet, then create a transaction and feed the QR code with the unsigned PSBT to your hardware wallet. Sign it on hardware wallet, scan it back to BlueWallet and broadcast it to the network. You have just conveniently made a transaction on your mobile device, while keeping your private keys on a secure hardware wallet, truly air-gapped! This is still in beta and only the[ CryptoAdvance device is 100% supported](https://twitter.com/StepanSnigirev/status/1209426608949465088), but we will work on testing and polishing the integration with other hardware wallets.

We still have a lot of work to do:

  * Ongoing integration with HodlHodl. Non-custodial fiat-to-btc trading is an important bitcoin infrastructure project. It’s a hedge against all regulated exchanges going bad with AML/KYC.
  * When LND will be stable enough we will include it as part of the wallet, allowing users to switch their lightning wallets into non-custodial mode, and gradually make it the default mode. But custodial lightning brought some unexpected benefits, such as practically unlimited incoming capacity, instant on, zero onchain footprint. It makes sense to maintain both and explore possible synergies here.
  * Multisig wallets are hard to tackle, mostly UI/UX wise. A proper joining ceremony is a hard task to design. The ceremony of creating a transaction and inviting all participants to sign it, can also be a challenge.
  * To reach maximum security, it makes sense to use only multisig wallets with all keys residing on your own devices, preferably hardware wallets from different manufacturers. Designing, implementing and testing this flow is not easy.
  * Sign message with your wallet/verify. I strongly feel that your private keys should help you with authentication on 3rd-party services, but what’s the proper way to do that we do not know, yet.
  * Provide-UTXO — when creating a transaction, supply UTXO to use in form of JSON document. This allows using the wallet on a completely offline/air-gapped device, provided you carry with you your up-to-date UTXO set. Then you sign it, broadcast via SMS/pigeons/whatever and congrats! You can transact even from a desert island.
  * Choose UTXO / UTXO spend strategies — when creating a transaction, choose which UTXO (or UTXO strategy) you want to use. For example, you could strive for the smallest fees (use higher-value outputs first), optimize for amounts used (sum of input amounts are close to total output amounts — might produce dust output), or you could consolidate (use all available inputs — yes this completely destroys privacy but helps to prepare for a period of high fees) etc.
  * Coinjoin — a proper coins mix service with other peers is tricky, but we might attempt it.
  * RBF-Service. A trustless server that broadcasts your replacement transactions with higher fees if previous transaction wasn’t confirmed in a timeframe you specified. You can start with 1 sat/byte transaction and gradually increase fee until it’s confirmed in a reasonable time (with the smallest fee possible). Automatically. This is only an idea at the moment.
  * NFC. Users will be able to ‘tap-to-share’ their receive address to other users, and other NFC-capable devices. This will eliminate the requirement for users to have to fiddle with their device’s display brightness, and having to move around their camera view in order to scan a QR Code. This feature will also be useful for our upcoming BTCPayServer integration.
  * Push notifications have been set aside for too long, but they will be eventually done.

And some [other more experimental consumer ideas](/bluewallet/work-in-
progress-building-a-bitcoin-wallet-e81ca6db82d7) that we are already sharing
with the community and putting it out there. The list doesn’t end there, but
one needs to keep some secrets as well :) Feel free to bring your ideas on!

Just some statistics of the year:

  *  **32 production releases**
  *  **738 commits**
  *  **27 contributors**

A special thanks to all the contributors, you guys rock! 🤘

To summarize, we are preparing for war! It will be a war about block space, it
will be a war about providing the users with the right tools to fight against
corporate interests trying to take advantage of Bitcoin. Join us, we promise
it won’t be a boring one!

[https://github.com/bluewallet/bluewallet](https://github.com/blueWallet/blueWallet)

Cheers!

\--

1

\--

\--

1

## [More from bluewallet](/bluewallet?source=post_page-----
72637ffe58eb--------------------------------)

Bitcoin wallet for iOS and android

[Read more from bluewallet](/bluewallet?source=post_page-----
72637ffe58eb--------------------------------)

## Recommended from Medium

[[![BondAppétit](https://miro.medium.com/fit/c/40/40/1*O8WQiyCKDw7FZjXfOu8wNg.png)](/@bondappetit?source=post_internal_links
---------0----------------------------)

[BondAppétit

](/@bondappetit?source=post_internal_links---------
0----------------------------)

in

[BondAppetit

](https://medium.com/bondappetit?source=post_internal_links---------
0----------------------------)

## How the Borrowing Process Works Under the BondAppetit Protocol

![](https://miro.medium.com/focal/112/112/50/50/1*zo5qLQyRo5xvP--
O7_nWnA.jpeg)](/bondappetit/how-the-borrowing-process-works-under-the-
bondappetit-protocol-9184d2ce0fdd?source=post_internal_links---------
0----------------------------)

[[![Derek
Kwok](https://miro.medium.com/fit/c/40/40/1*VUh7OW5t7scKyyddetKDHQ.jpeg)](/@dkwok94?source=post_internal_links
---------1----------------------------)

[Derek Kwok

](/@dkwok94?source=post_internal_links---------1----------------------------)

## Ethereum — How Virtual Fuel Powers a Vast Machine

![](https://miro.medium.com/focal/112/112/50/50/1*9zwYlcI1QAsb3E3-yjuglA.png)](/@dkwok94/ethereum-
how-virtual-fuel-powers-a-vast-machine-4b6d0d63c2ef?source=post_internal_links
---------1----------------------------)

[[![NIMERA](https://miro.medium.com/fit/c/40/40/1*gd9qepvGpIeuaEBI8kLxFQ.png)](/@nimera?source=post_internal_links
---------2----------------------------)

[NIMERA

](/@nimera?source=post_internal_links---------2----------------------------)

## What Is a BTC Address [2020 Guide] — Exscudo Blog

![](https://miro.medium.com/focal/112/112/50/50/0*f2UBLGSfu4SZRuod.png)](/@nimera/what-
is-a-btc-address-2020-guide-exscudo-
blog-3064f8553062?source=post_internal_links---------
2----------------------------)

[[![Oscar
Amstadt](https://miro.medium.com/fit/c/40/40/1*44cgwzb98GmbOS3ea0AWEA.jpeg)](/@oscaramstadt?source=post_internal_links
---------3----------------------------)

[Oscar Amstadt

](/@oscaramstadt?source=post_internal_links---------
3----------------------------)

## What is Bitcoin SV and Where to Buy it

![](https://miro.medium.com/focal/112/112/50/50/0*J3vPNFq5gSgtNH0e)](/@oscaramstadt/what-
is-bitcoin-sv-and-where-to-buy-it-9cdacc8a7d8f?source=post_internal_links
---------3----------------------------)

[[![The WhaleLend
Account](https://miro.medium.com/fit/c/40/40/1*8te4ZvSZwDBbnBYi4ycpAg.png)](/@whalelend.staff?source=post_internal_links
---------4----------------------------)

[The WhaleLend Account

](/@whalelend.staff?source=post_internal_links---------
4----------------------------)

in

[WhaleLend

](https://medium.com/whalelend?source=post_internal_links---------
4----------------------------)

## WHALELEND BOUNTY PROGRAM 2019

![](https://miro.medium.com/focal/112/112/50/50/1*U9ocY1tdLRFMM_y3yHBTyQ.jpeg)](/whalelend/whalelend-
bounty-program-2019-321cb4b3b144?source=post_internal_links---------
4----------------------------)

[[![Astronaut.to](https://miro.medium.com/fit/c/40/40/1*-YCD-
iwHZHRnPjuGyzjKOg.png)](/@astronautfinance?source=post_internal_links---------
5----------------------------)

[Astronaut.to

](/@astronautfinance?source=post_internal_links---------
5----------------------------)

## CHEESUS x ASTRONAUT

![](https://miro.medium.com/focal/112/112/50/50/1*OBuZxqhx52TlmXITNXnC3A.jpeg)](/@astronautfinance/cheesus-
x-astronaut-11b42062b6c3?source=post_internal_links---------
5----------------------------)

[[![BMV - Business
Metaverse](https://miro.medium.com/fit/c/40/40/1*bsuy46_x175kv26yCRw71A.png)](/@BMVnft?source=post_internal_links
---------6----------------------------)

[BMV - Business Metaverse

](/@BMVnft?source=post_internal_links---------6----------------------------)

## Business Metaverse

![](https://miro.medium.com/focal/112/112/50/50/1*ycenrvkwre-
uI3eKg0eXvQ.png)](/@BMVnft/business-
metaverse-2a25bfbca372?source=post_internal_links---------
6----------------------------)

[[![ThunderCore
Team](https://miro.medium.com/fit/c/40/40/1*Kuu4oBshweuPO5VvHXiwZA.png)](/@thundercoreofficial?source=post_internal_links
---------7----------------------------)

[ThunderCore Team

](/@thundercoreofficial?source=post_internal_links---------
7----------------------------)

in

[ThunderCore

](https://medium.com/thundercore?source=post_internal_links---------
7----------------------------)

## Why ThunderCore Outperforms Layer 2 Solutions

![](https://miro.medium.com/focal/112/112/50/50/1*g5mw3AmfigvR_bEOsVFcRA.jpeg)](/thundercore/why-
thundercore-outperforms-other-
layer-2-solutions-7849bacd1471?source=post_internal_links---------
7----------------------------)

[](/?source=post_page-----72637ffe58eb--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
72637ffe58eb--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
72637ffe58eb--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
72637ffe58eb--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
72637ffe58eb--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----72637ffe58eb--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----72637ffe58eb--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fbluewallet%2Fpreparing-
for-war-how-was-2019-and-a-glimpse-of-the-future-72637ffe58eb&source=post_page
--------------------------nav_reg-----------)

[![Igor
Korsakov](https://miro.medium.com/fit/c/176/176/0*NeqAGkfF31rtTDfH.)](/@overtorment)

[

## Igor Korsakov

](/@overtorment)

181 Followers

<http://igorkorsakov.com>

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fusers%2F4c10f682a52e%2Flazily-enable-
writer-
subscription&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fbluewallet%2Fpreparing-
for-war-how-was-2019-and-a-glimpse-of-the-
future-72637ffe58eb&user=Igor+Korsakov&userId=4c10f682a52e&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Carley
Montgomery](https://miro.medium.com/fit/c/40/40/1*rIpAIYHTwqXvn9JsYy1e1g.jpeg)](/@carleymontgomery?source=read_next_recirc
---------0---------------------433cb8c8_cf30_470f_bb1c_d5c7cef2c357-------)

[Carley Montgomery

](/@carleymontgomery?source=read_next_recirc---------0---------------------
433cb8c8_cf30_470f_bb1c_d5c7cef2c357-------)

## Who’s Really Behind Bitcoin Lake?

![](https://miro.medium.com/focal/112/112/50/50/0*ZXErFCGz_OzhyyOj)](/@carleymontgomery/whos-
really-behind-bitcoin-lake-fbdb17d96085?source=read_next_recirc---------0
---------------------433cb8c8_cf30_470f_bb1c_d5c7cef2c357-------)

[[![Mateusz
\(meshcode\)](https://miro.medium.com/fit/c/40/40/1*LEmO2tXssyUqX0hG5gER3Q.jpeg)](/@meshcode?source=read_next_recirc
---------1---------------------433cb8c8_cf30_470f_bb1c_d5c7cef2c357-------)

[Mateusz (meshcode)

](/@meshcode?source=read_next_recirc---------1---------------------
433cb8c8_cf30_470f_bb1c_d5c7cef2c357-------)

in

[Cyberpower Telenoia

](https://medium.com/cyberpower-telenoia?source=read_next_recirc---------1
---------------------433cb8c8_cf30_470f_bb1c_d5c7cef2c357-------)

## “The Cryptopians” (2022) audiobook review

![](https://miro.medium.com/focal/112/112/50/50/1*MNDq-y765OUcEMxbB2cd7w.jpeg)](/cyberpower-
telenoia/the-cryptopians-2022-audiobook-
review-6330a6e6da43?source=read_next_recirc---------1---------------------
433cb8c8_cf30_470f_bb1c_d5c7cef2c357-------)

[[![Markaveli](https://miro.medium.com/fit/c/40/40/1*nJTRJDONWFBZ9KKa-h8SYA@2x.jpeg)](/@gbxdvtwvm?source=read_next_recirc
---------2---------------------433cb8c8_cf30_470f_bb1c_d5c7cef2c357-------)

[Markaveli

](/@gbxdvtwvm?source=read_next_recirc---------2---------------------
433cb8c8_cf30_470f_bb1c_d5c7cef2c357-------)

## When people hear about Staking, most times what comes to mind is APRs or
APYs.

![](https://miro.medium.com/focal/112/112/50/50/1*AfeHEqTQ4fOi4qANHsGJNg@2x.jpeg)](/@gbxdvtwvm/when-
people-hear-about-staking-most-times-what-comes-to-mind-is-aprs-or-apys-
da98e3919658?source=read_next_recirc---------2---------------------
433cb8c8_cf30_470f_bb1c_d5c7cef2c357-------)

[[![Jesus
Bailey](https://miro.medium.com/fit/c/40/40/1*4s_ECgx02sUC_U980Pbreg.jpeg)](/@jesus-
bailey?source=read_next_recirc---------3---------------------
433cb8c8_cf30_470f_bb1c_d5c7cef2c357-------)

[Jesus Bailey

](/@jesus-bailey?source=read_next_recirc---------3---------------------
433cb8c8_cf30_470f_bb1c_d5c7cef2c357-------)

## Doug Ford Bitcoin Code — Review

![](https://miro.medium.com/focal/112/112/50/50/0*R1OTnBVluFWwlNCV.jpg)](/@jesus-
bailey/doug-ford-bitcoin-code-review-90003d0cbbd?source=read_next_recirc
---------3---------------------433cb8c8_cf30_470f_bb1c_d5c7cef2c357-------)

[Help

](https://help.medium.com/hc/en-us)

[Status

](https://medium.statuspage.io)

[Writers

](https://about.medium.com/creators/)

[Blog

](https://blog.medium.com)

[Careers

](/jobs-at-medium/work-at-medium-959d1a85284e)

[Privacy

](https://policy.medium.com/medium-privacy-policy-f03bf92035c9)

[Terms

](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f)

[About

](https://medium.com/about?autoplay=1)

[Knowable

](https://knowable.fyi)

