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

[Nov 09  
2017](https://blog.samouraiwallet.com/post/167306611667/wallet-
update-097-coin-control-dust-tx-alerts)

### [Wallet Update 0.97 - Coin Control, Dust TX alerts, Like-Type inputs and
more.](https://blog.samouraiwallet.com/post/167306611667/wallet-
update-097-coin-control-dust-tx-alerts)

It's that time again, a new Samourai Wallet update has just hit the [Google
Play
store](https://t.umblr.com/redirect?z=https%3A%2F%2Fplay.google.com%2Fstore%2Fapps%2Fdetails%3Fid%3Dcom.samourai.wallet&t=NDhmMTZmOTRlOTA2ZTdmYjM5YWUxODM2ZWZhNmQ3NjQ4NWIyNWNjNCxXRDBoNUhSVg%3D%3D&b=t%3AgssRereQbaKEWqYj4_q6Mw&p=https%3A%2F%2Fblog.samouraiwallet.com%2Fpost%2F167306611667%2Fwallet-
update-097-coin-control-dust-tx-alerts&m=1&ts=1653239633) and is available for
download on your Android device right now. As always the [full list of changes
is available on GitHub](https://href.li/?https://github.com/Samourai-
Wallet/samourai-wallet-android/compare/3cabee55f4...2770e086bd). We're really
excited about this release because it lays the foundation for a lot of
exciting features coming down the line.

## Coin Control

Coin Control is a powerful feature and nearly unheard of in most Bitcoin
wallet software. To understand coin control, you first have to understand a
little how your bitcoin wallet works under the hood. Samourai Wallet gives you
access to a list of _  'Unspent Outputs' _in your wallet. Unspent outputs, are
simply put, bitcoin in your wallet that can be spent as part of a new
transaction. The combined amount of unspent outputs is equal to your total
spendable balance. So if you have 2 Unspent Outputs of 0.5 BTC - your wallet
would have a total spendable balance of 1 BTC. Coin control refers to the user
having optional control over which unspent outputs get used when creating new
transactions.

 **As of version 0.97, users will be able to mark any unspent output in their
wallet as   _' Do Not Spend'_.** Any Do Not Spend output will not display as
part of the total balance of the wallet and will not be used to create new
transactions. The Do Not Spend tag is reversible at any time.

## Blockchain Fungibility with like-type inputs and outputs

In the last update ([v
0.96](http://blog.samouraiwallet.com/post/166778873402/wallet-update-segwit-
support-and-introducing)) we introduced the concept of matching like-type
**outputs** when creating transactions on the blockchain. This meant, that if
you were sent bitcoin to an address beginning with '3′ then the returning
'change' output will also be sent to an address in your wallet that begins
with a '3′.

 **As of version 0.97 released today Samourai now will always attempt to
create transactions with like-type inputs** in addition to like-type outputs.
This takes the anti fingerprinting measures a step further by making it
incredibly difficult to link the sending addresses to the receiving addresses
in a transaction on the blockchain, throwing a wrench in ways spies and snoops
track the blockchain.

## Dust Tracking Real Time Alerts

Speaking of blockchain snoops and spies… One of the methods in use to de
anonymise bitcoin users is through a process called 'Dusting'. When you're
_Dusted_ you'll receive a small bitcoin transaction into an address in your
wallet. Eventually your wallet will combine this small amount of BTC into a
larger transaction and reveal other addresses that can be linked to you with
certainty, building a network graph of your wallet and transaction history.

![image](https://64.media.tumblr.com/90400e7cde10287f383269edaef9ccba/tumblr_inline_oz5qgcF8Mz1tu47rq_640.jpg)

 **In this version of Samourai Wallet, we have added real time Dust
Alerting.** If you wallet receives a low value transaction (anything less than
1000 satoshis) you will be alerted and given the choice to mark the dust
output as 'Unspendable'. If you see this alert and you weren't expecting the
incoming deposit we recommend blocking the transaction for your privacy. As
always, the Unspendable tag is reversible if you decide to change your mind
later.

## Gifts for our power users

Some new tools our dedicated power users may find useful:

  *  **Raw PushTX**  
Push any signed transaction (hex format) to the bitcoin network - Available in
_Settings > Transactions > Broadcast Transaction Hex  
_  

  *  **Sign message with Segwit address**  
Sign any message with an active segwit (P2SH-P2WPKH) utxo privkey  
  

  *  **Show redeem script of Segwit utxo      
**  

For our users who are keeping track, the SHA-256 APK hash for this release is:
**2270e7c9b402447e5cc881f9d3eea4e5c72c08c55c47c70df0d3bf16cb5a6123  **You can
verify this matches the hash of your own wallet by navigating to the _Settings
> About > APK_ Hash screen

You can get help and support from
[support.samourai.io](https://href.li/?https://support.samourai.io) or by
emailing support@samouraiwallet.com

  * [November 09, 2017](https://blog.samouraiwallet.com/post/167306611667/wallet-update-097-coin-control-dust-tx-alerts)

  1. [![](https://64.media.tumblr.com/avatar_7c8acd856cf5_16.pnj)](https://kryptokidz-blog.tumblr.com/ "KryptoKidz")[kryptokidz-blog](https://kryptokidz-blog.tumblr.com/post/167306886764 "KryptoKidz") reblogged this from [samouraiwallet](https://blog.samouraiwallet.com/ "Samourai Wallet")

  2. [![](https://64.media.tumblr.com/avatar_7c8acd856cf5_16.pnj)](https://kryptokidz-blog.tumblr.com/ "KryptoKidz ")[kryptokidz-blog](https://kryptokidz-blog.tumblr.com/ "KryptoKidz") liked this 

  3. [![](https://64.media.tumblr.com/avatar_36fa1c18c89f_16.pnj)](https://blog.samouraiwallet.com/ "Samourai Wallet")[samouraiwallet](https://blog.samouraiwallet.com/ "Samourai Wallet") posted this 

[Older Post](https://blog.samouraiwallet.com/post/166778873402) [Newer
Post](https://blog.samouraiwallet.com/post/168785913782)
![](https://px.srvcs.tumblr.com/impixu?T=1653239633&J=eyJ0eXBlIjoidXJsIiwidXJsIjoiaHR0cDovL2Jsb2cuc2Ftb3VyYWl3YWxsZXQuY29tL3Bvc3QvMTY3MzA2NjExNjY3L3dhbGxldC11cGRhdGUtMDk3LWNvaW4tY29udHJvbC1kdXN0LXR4LWFsZXJ0cyIsInJlcXR5cGUiOjAsInJvdXRlIjoiL3Bvc3QvOmlkLzpzdW1tYXJ5Iiwibm9zY3JpcHQiOjF9&U=PGAOJLAFPN&K=acb44d7816ee2e496c2e6f3a5bd641313fc021caa9d74c3694b816b308a016b1&R=)![](https://px.srvcs.tumblr.com/impixu?T=1653239633&J=eyJ0eXBlIjoicG9zdCIsInVybCI6Imh0dHA6Ly9ibG9nLnNhbW91cmFpd2FsbGV0LmNvbS9wb3N0LzE2NzMwNjYxMTY2Ny93YWxsZXQtdXBkYXRlLTA5Ny1jb2luLWNvbnRyb2wtZHVzdC10eC1hbGVydHMiLCJyZXF0eXBlIjowLCJyb3V0ZSI6Ii9wb3N0LzppZC86c3VtbWFyeSIsInBvc3RzIjpbeyJwb3N0aWQiOiIxNjczMDY2MTE2NjciLCJibG9naWQiOjIzNTE1Mjc3Mywic291cmNlIjozM31dLCJub3NjcmlwdCI6MX0=&U=DLHJCBJEMB&K=1f174beb1db2a87cb29ebbd1f8bcb1b4e61b608c4e1ea3c0c209d435f1c0b7ad&R=)

