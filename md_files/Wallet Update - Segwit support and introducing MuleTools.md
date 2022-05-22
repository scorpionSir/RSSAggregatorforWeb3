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

[Oct 25  
2017](https://blog.samouraiwallet.com/post/166778873402/wallet-update-segwit-
support-and-introducing)

### [Wallet Update - Segwit support and introducing
MuleTools](https://blog.samouraiwallet.com/post/166778873402/wallet-update-
segwit-support-and-introducing)

Last week we released Samourai Wallet version 0.96 on the [Google Play
store](https://t.umblr.com/redirect?z=https%3A%2F%2Fplay.google.com%2Fstore%2Fapps%2Fdetails%3Fid%3Dcom.samourai.wallet&t=ZTE0MzU0ZmJhZjIxMWU0M2JkMTNhYjdkMThlNDcxMmI0OTJhNjYzOCxtNWZqYnczMQ%3D%3D&b=t%3AgssRereQbaKEWqYj4_q6Mw&p=https%3A%2F%2Fblog.samouraiwallet.com%2Fpost%2F166778873402%2Fwallet-
update-segwit-support-and-introducing&m=1&ts=1653247315). The full list of
changes can be [viewed on
GitHub](https://href.li/?https://github.com/Samourai-Wallet/samourai-wallet-
android/compare/f48a498d21...cb046763c6) and includes many improvements and
fixes. However, we want to focus on two main areas in this post. One area you
all have heard of and been asking for, and one we want to introduce you to.  

## Segwit

![image](https://64.media.tumblr.com/7334bce7a982d99d6e90b32f69d121be/tumblr_inline_oydq86gXT91tu47rq_500.png)

Samourai Wallet has now fully integrated the changes needed to implement
support for the latest bitcoin upgrade, _Segregated Witnesses_. By default all
addresses you reveal through the receive screen will be _P2SH-P2WPKH_ as
defined by
[BIP141](https://href.li/?https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki#p2wpkh-
nested-in-bip16-p2sh) and
[BIP49](https://href.li/?https://github.com/bitcoin/bips/blob/master/bip-0049.mediawiki).
We'll refer to these as _ 'segwit addresses' _for simplicity sake, but make no
mistake, these are normal bitcoin addresses and are compatible with the
Bitcoin reference client since version 0.6.0. These addresses are more
efficient to transact with and users can expect to pay lower fees when
spending from segwit addresses. Segwit support is enabled by default but can
be disabled within the wallet settings or on a one-off basis with a convenient
toggle switch directly on the Receive screen.

For the more technical users, your _P2SH-P2WPKH_ and your _P2SH_ inputs remain
in a single HD account and can be mixed together in a transaction thanks to
the wallet being able to sign mixed inputs. Your wallet will now have two
_Extended public keys_ ( _xpub_ ) - so, if you are a Sentinel user you will
need to add your BIP49 xpub along with your BIP44 xpub. Both of your xpub's
can be found  in the settings. Samourai will manage the creation of either
P2SH or P2SH-P2WPKH change outputs depending on the type of output being spent
to. This is to decrease the fingerprint of the transaction on the block chain.

![image](https://64.media.tumblr.com/bb2795760b66c12a73b3f90e9633a9b9/tumblr_inline_oydulyTE1u1tu47rq_500.png)

## MuleTools

![image](https://64.media.tumblr.com/9bd864d40a068728c446797cd67b92b3/tumblr_inline_oydq7f74eO1tu47rq_500.png)

We're happy to make public an initiative we have been thinking about for some
time. Inspired by the [Blockstream
satellite](https://href.li/?https://blockstream.com/2017/08/15/announcing-
blockstream-satellite.html) and the 2003 essay by Nick Szabo, [Advances in
Distributed Security](https://href.li/?http://nakamotoinstitute.org/advances-
in-distributed-security/)
[MuleTools](https://href.li/?https://github.com/MuleTools) is the umbrella
term for the open repository of community ideas and open source code that
promotes alternative routes for bitcoin broadcasts and block retrieval. Having
many different options for interacting with the bitcoin network greatly
increases the censorship resistance of the network and the financial autonomy
of the user.

Samourai is interested in assisting with the development of any alternative
paths for bitcoin pushTx and block retrieval and will consider all submitted
projects for possible inclusion within Samourai Wallet.

[Pavol Rusnak](https://href.li/?https://github.com/prusnak) developed a simple
[PushTx server](https://href.li/?https://github.com/prusnak/smspushtx) to push
transactions to the bitcoin network via SMS and [Andrew
LeCody](https://href.li/?https://github.com/aceat64) created a proof of
concept [APRS pushTx
server](https://href.li/?https://github.com/aceat64/bitcoin_aprs) for pushing
transactions over shortwave radio. We think these both are a great example of
an alternative method of pushing transactions. Inspired by the work of these
developers, [Samourai Wallet](https://href.li/?https://www.samouraiwallet.com)
now includes the ability to export a signed raw bitcoin transaction hex or QR
code that can be fed by the user to any pushTx server.

![image](https://64.media.tumblr.com/859f0453e8403341296ae49322ab2af3/tumblr_inline_oydq1bI3ex1tu47rq_500.png)

We look forward to exploring this concept further, hopefully with community
feedback and support. Please feel free to check out the [MuleTools
readme](https://href.li/?https://github.com/MuleTools/MuleTools), submit
issues, ideas, pull requests, or documentation on the repositories. Any
individual or company who wishes to collaborate is encouraged to reach out.

  * [October 25, 2017](https://blog.samouraiwallet.com/post/166778873402/wallet-update-segwit-support-and-introducing)

  1. [![](https://64.media.tumblr.com/avatar_7c8acd856cf5_16.pnj)](https://kryptokidz-blog.tumblr.com/ "KryptoKidz ")[kryptokidz-blog](https://kryptokidz-blog.tumblr.com/ "KryptoKidz") liked this 

  2. [![](https://64.media.tumblr.com/avatar_36fa1c18c89f_16.pnj)](https://blog.samouraiwallet.com/ "Samourai Wallet")[samouraiwallet](https://blog.samouraiwallet.com/ "Samourai Wallet") posted this 

[Older Post](https://blog.samouraiwallet.com/post/166464385507) [Newer
Post](https://blog.samouraiwallet.com/post/167306611667)
![](https://px.srvcs.tumblr.com/impixu?T=1653247315&J=eyJ0eXBlIjoidXJsIiwidXJsIjoiaHR0cDovL2Jsb2cuc2Ftb3VyYWl3YWxsZXQuY29tL3Bvc3QvMTY2Nzc4ODczNDAyL3dhbGxldC11cGRhdGUtc2Vnd2l0LXN1cHBvcnQtYW5kLWludHJvZHVjaW5nIiwicmVxdHlwZSI6MCwicm91dGUiOiIvcG9zdC86aWQvOnN1bW1hcnkiLCJub3NjcmlwdCI6MX0=&U=JHBLFIAOCD&K=89a607c4750ac5663fce90a9040b96765b911b21e7c701b531ef47a964992462&R=)![](https://px.srvcs.tumblr.com/impixu?T=1653247315&J=eyJ0eXBlIjoicG9zdCIsInVybCI6Imh0dHA6Ly9ibG9nLnNhbW91cmFpd2FsbGV0LmNvbS9wb3N0LzE2Njc3ODg3MzQwMi93YWxsZXQtdXBkYXRlLXNlZ3dpdC1zdXBwb3J0LWFuZC1pbnRyb2R1Y2luZyIsInJlcXR5cGUiOjAsInJvdXRlIjoiL3Bvc3QvOmlkLzpzdW1tYXJ5IiwicG9zdHMiOlt7InBvc3RpZCI6IjE2Njc3ODg3MzQwMiIsImJsb2dpZCI6MjM1MTUyNzczLCJzb3VyY2UiOjMzfV0sIm5vc2NyaXB0IjoxfQ==&U=DKODBGFIIO&K=6512fed9ab0f4c265907a310bfb0bcc37e79e5da77a3479809236a92499fb723&R=)

