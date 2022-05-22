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

[Jul 29  
2018](https://blog.samouraiwallet.com/post/176412126502/the-road-to-10-ui-
update)

### [The Road to 1.0 - UI
Update](https://blog.samouraiwallet.com/post/176412126502/the-road-to-10-ui-
update)

We are very pleased to roll out Samourai Wallet update 0.98.75 available to
update via Google Play for existing testers, install from [Google
Play](https://href.li/?https://samouraiwallet.com/alpha/signup.html) for new
testers, or build from source on
[Github](https://href.li/?https://github.com/Samourai-Wallet/samourai-wallet-
android). This update includes two important UI changes and very important
under the hood changes for the future.

apk hash sha-256 of version 0.98.75 :
70d609cdf5a9bd130543b30853268b6783f8b90ed38fd48838e942ad5b1fff6c

These UI and UX modifications are the first of many to help prepare Samourai
Wallet for 1.0 release later this year.

## Real-time transaction state

![image](https://64.media.tumblr.com/6b061c7846259dd7a0da8683187b7f17/tumblr_inline_pch8f0YDeT1tu47rq_640.gifv)

After a normal spend, a [STONEWALL
spend](https://blog.samouraiwallet.com/post/173544815052/full-bech32-support-
introducing-boltzmann-and), or [a batch
spend](https://blog.samouraiwallet.com/post/170574017907/introducing-batch-
spending-for-cheaper-more) you will now see a full screen overlay of the
current state of the transaction in real-time. Our valued Ricochet users will
see a modified animation specific to Ricochet in a future update.

  1.  **Creating transaction  
** The wallet is gathering the needed inputs to cover the full amount to be
spent and composing an unsigned transaction.  

  2.  **Signing transaction  
** The wallet is signing the transaction it just created with the necessary
private keys of the selected inputs.  

  3.  **Broadcasting transaction  
** The wallet is broadcasting the signed transaction either via our Iceland
based Bitcoin Core node or your own Trusted Node.  

  4.  **Transaction Sent  
** The transaction has been submitted to the bitcoin network for inclusion in
the blockchain.

This screen becomes even more important as we begin to roll out **[Offline
Mode](https://twitter.com/SamouraiWallet/status/1014463579620290560)**  where
user intervention needs to take place between Transaction Signing and
Broadcasting. Consider this new real time status animation this a nice visual
treat with a deeper future purpose.

## Simplified Receive Screen

![image](https://64.media.tumblr.com/98045d6a59d530847ff53fdaa01b3f22/tumblr_inline_pch8wuCEKL1tu47rq_640.gifv)

The other change you will immediately notice is the simplified receive screen.

The current address is now directly at the top of the screen. You can still
tap this address to copy it to your clipboard, and you can share the address
using a variety of methods using the Share icon in the toolbar.

Tap the advanced toggle to create a QR code with a BTC amount encoded within
it or to change the type of address to use. By default, Segwit Compatibility
addresses are displayed. Allowing you the benefits of Segwit, while still
producing addresses that older wallets understand.  

Samourai Wallet users can produce Legacy addresses that begin with a "1″,
Segwit Compatibility addresses that begin with a "3″, or Segwit Native
addresses that begin with a "bc1″.

We have also added in the derivation path of the displayed address for our
power users.

## Send Screen

We have made a minor change to the send screen in this update after receiving
a lot of feedback from our regular Ricochet users. The Ricochet toggle will
now remember the last state it was in. This means, if you enable Ricochet, the
next time you visit the send screen, Ricochet will be enabled.

The next UI update will include significant UI changes to the existing send
screen.

## Unseen Changes

An important under the hood change in the way your wallet keeps track of
PayNym's means your[ PayNym bot](https://href.li/?https://paynym.is/about)
will very soon generate Segwit Native (bech32) addresses by default instead of
legacy addresses. This change, in combination with many more planned updates
will make using PayNym's cheaper, faster, and easier than ever.

We hope you enjoy this update and the new UI changes.The latest version of
Samourai Wallet can be [installed onto your Android device from the Google
Play Store](https://href.li/?https://samouraiwallet.com/alpha/signup.html).

We are available to provide support at [support.samourai.io
](https://t.umblr.com/redirect?z=http%3A%2F%2Fsupport.samourai.io&t=OGFhMmNjM2QxNDZjODI1ODQ1Njk4OTRlMmY5MGNiZTMxY2VkODNiYyxTclIyejNjdA%3D%3D&b=t%3AgssRereQbaKEWqYj4_q6Mw&p=https%3A%2F%2Fblog.samouraiwallet.com%2Fpost%2F170574017907%2Fintroducing-
batch-spending-for-cheaper-more&m=1)or by email at support@samouraiwallet.com

  * [July 29, 2018](https://blog.samouraiwallet.com/post/176412126502/the-road-to-10-ui-update)

  1. [![](https://64.media.tumblr.com/avatar_0a1e9c7e55f6_16.pnj)](https://leon-gerard-vandenberg.tumblr.com/ "Leon Gerard Vandenberg")[leon-gerard-vandenberg](https://leon-gerard-vandenberg.tumblr.com/post/176412153438 "Leon Gerard Vandenberg") reblogged this from [samouraiwallet](https://blog.samouraiwallet.com/ "Samourai Wallet")

  2. [![](https://64.media.tumblr.com/avatar_0a1e9c7e55f6_16.pnj)](https://leon-gerard-vandenberg.tumblr.com/ "Leon Gerard Vandenberg ")[leon-gerard-vandenberg](https://leon-gerard-vandenberg.tumblr.com/ "Leon Gerard Vandenberg") liked this 

  3. [![](https://64.media.tumblr.com/avatar_36fa1c18c89f_16.pnj)](https://blog.samouraiwallet.com/ "Samourai Wallet")[samouraiwallet](https://blog.samouraiwallet.com/ "Samourai Wallet") posted this 

[Older Post](https://blog.samouraiwallet.com/post/173544815052) [Newer
Post](https://blog.samouraiwallet.com/post/178536644472)
![](https://px.srvcs.tumblr.com/impixu?T=1653247573&J=eyJ0eXBlIjoidXJsIiwidXJsIjoiaHR0cDovL2Jsb2cuc2Ftb3VyYWl3YWxsZXQuY29tL3Bvc3QvMTc2NDEyMTI2NTAyL3RoZS1yb2FkLXRvLTEwLXVpLXVwZGF0ZSIsInJlcXR5cGUiOjAsInJvdXRlIjoiL3Bvc3QvOmlkLzpzdW1tYXJ5Iiwibm9zY3JpcHQiOjF9&U=PAGHHOJANO&K=124769a6c19aefb17f405d017d2a51c027fcbce4523f3e26da93b25b8d7c624e&R=)![](https://px.srvcs.tumblr.com/impixu?T=1653247573&J=eyJ0eXBlIjoicG9zdCIsInVybCI6Imh0dHA6Ly9ibG9nLnNhbW91cmFpd2FsbGV0LmNvbS9wb3N0LzE3NjQxMjEyNjUwMi90aGUtcm9hZC10by0xMC11aS11cGRhdGUiLCJyZXF0eXBlIjowLCJyb3V0ZSI6Ii9wb3N0LzppZC86c3VtbWFyeSIsInBvc3RzIjpbeyJwb3N0aWQiOiIxNzY0MTIxMjY1MDIiLCJibG9naWQiOjIzNTE1Mjc3Mywic291cmNlIjozM31dLCJub3NjcmlwdCI6MX0=&U=ALIIIENICG&K=975ee96c07ea9066b5217de1404e2203f24feea536ab04c7bd63aa7f197f72e7&R=)

