###### [![Samourai
Wallet](https://64.media.tumblr.com/avatar_36fa1c18c89f_64.pnj) Samourai
Wallet](/)

* * *

* * *

* * *

x

  * [Archive](/archive)
  * [RSS](https://blog.samouraiwallet.com/rss)
  * [Simplify](http://simplifytheme.tumblr.com) version 1.22. Theme Designed & Developed by [](http://amitjakhu.com)Amit Jakhu. Powered by [Tumblr](http://tumblr.com).

[Jul 11  
2019](https://blog.samouraiwallet.com/post/186208584657/introducing-09981-enter-
the-dojo)

### [Introducing 0.99.81 - Enter The
Dojo](https://blog.samouraiwallet.com/post/186208584657/introducing-09981-enter-
the-dojo)

This is an exciting one, so strap in. We are happy to announce 0.99.81 which
brings in many Quality of Life updates, some bug fixes, and the highlight
feature of pairing to your own self hosted Dojo node.

You can get the latest update from [Google
Play](https://t.umblr.com/redirect?z=https%3A%2F%2Fplay.google.com%2Fstore%2Fapps%2Fdetails%3Fid%3Dcom.samourai.wallet&t=NzNkY2YyNWQ1Yjk1YmRmY2JkZjI2MWRmMThlYzA4OTg0OWQ3NzQwNSxBZ0hxbldnVg%3D%3D&b=t%3AgssRereQbaKEWqYj4_q6Mw&p=https%3A%2F%2Fblog.samouraiwallet.com%2Fpost%2F186208584657%2Fintroducing-09981-enter-
the-dojo&m=1&ts=1653248361) as of today.  

> **apk hash sha-256 of version 0.99.81 :
> 073fa50552c07449538bc402519a237eb72f02ecf102bf8a415287a5dda05932**

##  Dojo Pairing

Early last month we Open Sourced our back end infrastructure allowing you to
[self host your own Dojo full
node](https://blog.samouraiwallet.com/post/185312260292/introducing-samourai-
dojo-10-open-source-and). Today, as of version 0.99.81 we have introduced the
ability to pair a newly created Samourai Wallet directly to your Dojo full
node over Tor, bypassing our servers entirely. This allows you to be entirely
sovereign and independent of Samourai operated servers.

![image](https://64.media.tumblr.com/29fca4d3a863099b5b08f61d4bab951d/d09f5c0dec9c1680-76/s640x960/89418f6fa2f5a208dc31b85054f02cea83c9811f.jpg)

Pairing is a simple process. Navigate to your fully synced Dojo maintenance
control panel with the Pairing QR code visible. In your Samourai Wallet tap
"Pair to existing Dojo"  and then scan the QR code. Once paired you will be
invited to create a new wallet.

It is important to keep in mind that the full Dojo pairing process will
include routines for restoring existing wallets, **but this update is
specifically for pairing newly created wallets**. Restoring your existing
wallet with Dojo is currently unsupported in this version.

##  Default Bech32 Addresses

Samourai Wallet was among the first to [deliver full bech32 support to users
in May 2018 ](https://blog.samouraiwallet.com/post/173544815052/full-
bech32-support-introducing-boltzmann-and), directly contributing to a
reduction in the miner fees that Samourai Wallet users pay when transacting.
In the 0.99.81 update we are happy to announce that bech32 addresses are now
the default address type used by the wallet. If you are looking for other
address types they are still available from the advanced toggle on the receive
screen.

##  Improved QR scanner

Lets face it, at Samourai we love QR codes. From simple receive addresses, to
Z85 encoded packet streams that ultimately get broadcast to space, we rely on
QR codes as a way to efficently transmit data in a peer-2-peer manner. We're
happy to roll out an updated QR scanner that is more responsive when dealing
with the denser QR codes that are being created. This doesn't sound like a big
deal, but you'll notice the difference when you use it.

##  Tor updates

We have continued to work hard on refining the built in Tor layer of Samourai
Wallet, with most users able to achieve stable performance with decent speed.
By the very nature of Tor, it will never be as fast as Clearnet, but with
continued investment in refining our implementation and contributing
improvements and code to the upstream maintainer we hope to increase the
stability of our Tor implementation. Along with stability improvements all Tor
connections are now via v3 .onion addresses. This includes connections to your
own Dojo and our own servers. Finally, you are also now able to manually
invoke a new Tor identity. This can be achieved from the status bar
notification or from the Network Dashboard in your wallet.

##  STONEWALL Updates

This one is a little technical, but the long and short of it is we have
strenghend STONEWALL even further with slight tweaks to the coin selection and
transaction composition rules.

We have made some changes to our STONEWALL algorithm to optimize against
deanonymization attacks. Previous iterations allowed for the miner fee of a
STONEWALL to be paid entirely from one of the two UTXO sets, as of this
version, STONEWALL miner fees are equally split between the two sets.

This change also applies for STONEWALLx2. From 0.99.81 onward both you and
your collaborator will split the miner fee equally, so in effect your
collaborator is paying a very small sum to mix with you.  

## Thank you  

As always we appreciate your continued support of the project.

We are available as always to answer any questions on
[support.samourai.io](https://href.li/?https://support.samourai.io) or by
email at support@samouraiwallet.com  

You can download Samourai Wallet from the [Google Play
Store](https://t.umblr.com/redirect?z=https%3A%2F%2Fplay.google.com%2Fstore%2Fapps%2Fdetails%3Fid%3Dcom.samourai.wallet&t=NzNkY2YyNWQ1Yjk1YmRmY2JkZjI2MWRmMThlYzA4OTg0OWQ3NzQwNSxBZ0hxbldnVg%3D%3D&b=t%3AgssRereQbaKEWqYj4_q6Mw&p=https%3A%2F%2Fblog.samouraiwallet.com%2Fpost%2F186208584657%2Fintroducing-09981-enter-
the-dojo&m=1&ts=1653248361)

Stop by our [active telegram
channel](https://href.li/?https://t.me/SamouraiWallet) of over 1,000 privacy
activists and say hello.  
  

  * [July 11, 2019](https://blog.samouraiwallet.com/post/186208584657/introducing-09981-enter-the-dojo)

  1. [![](https://64.media.tumblr.com/06144ecfa3533f1ca97f899e40d6a2a0/96bc706e4988d33b-f8/s16x16u_c1/35417a574aa6fd82ec0a220f660e0d4f30118799.pnj)](https://ehyowarrenzy.tumblr.com/ "Aloha ")[ehyowarrenzy](https://ehyowarrenzy.tumblr.com/ "Aloha") liked this 

  2. [![](https://64.media.tumblr.com/avatar_36fa1c18c89f_16.pnj)](https://blog.samouraiwallet.com/ "Samourai Wallet")[samouraiwallet](https://blog.samouraiwallet.com/ "Samourai Wallet") posted this 

[Older Post](https://blog.samouraiwallet.com/post/185312260292) [Newer
Post](https://blog.samouraiwallet.com/post/186458671552)
![](https://px.srvcs.tumblr.com/impixu?T=1653248361&J=eyJ0eXBlIjoidXJsIiwidXJsIjoiaHR0cDovL2Jsb2cuc2Ftb3VyYWl3YWxsZXQuY29tL3Bvc3QvMTg2MjA4NTg0NjU3L2ludHJvZHVjaW5nLTA5OTgxLWVudGVyLXRoZS1kb2pvIiwicmVxdHlwZSI6MCwicm91dGUiOiIvcG9zdC86aWQvOnN1bW1hcnkiLCJub3NjcmlwdCI6MX0=&U=ELHIIENDMA&K=59aab19f7eb1891a7342e8d036d01055b34722a33baf0c99d2b137e904614da8&R=)![](https://px.srvcs.tumblr.com/impixu?T=1653248361&J=eyJ0eXBlIjoicG9zdCIsInVybCI6Imh0dHA6Ly9ibG9nLnNhbW91cmFpd2FsbGV0LmNvbS9wb3N0LzE4NjIwODU4NDY1Ny9pbnRyb2R1Y2luZy0wOTk4MS1lbnRlci10aGUtZG9qbyIsInJlcXR5cGUiOjAsInJvdXRlIjoiL3Bvc3QvOmlkLzpzdW1tYXJ5IiwicG9zdHMiOlt7InBvc3RpZCI6IjE4NjIwODU4NDY1NyIsImJsb2dpZCI6MjM1MTUyNzczLCJzb3VyY2UiOjMzfV0sIm5vc2NyaXB0IjoxfQ==&U=PPIEABOMMO&K=0c4c8f362fb6ed550ef4473ac109a635731336afcfa4c7e42a2c03a56be16961&R=)

