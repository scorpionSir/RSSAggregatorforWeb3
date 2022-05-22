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

[Jan 21  
2019](https://blog.samouraiwallet.com/post/182192289762/staggered-ricochet-
utxo-tagging-paynym-ux)

### [Staggered Ricochet, UTXO tagging, PayNym UX upgrades, and Whirlpool
mixing prep](https://blog.samouraiwallet.com/post/182192289762/staggered-
ricochet-utxo-tagging-paynym-ux)

We are pleased to roll out Samourai Wallet update 0.99.05 available to [update
via Google Play for existing
testers](https://t.umblr.com/redirect?z=https%3A%2F%2Fplay.google.com%2Fstore%2Fapps%2Fdetails%3Fid%3Dcom.samourai.wallet&t=NGExMjk5YzNhMTIyOWZjYmM5YmMxNWQ3YzRmNzMzOGYyNjYxOWU2YyxaWGt4VlNrSw%3D%3D&b=t%3AgssRereQbaKEWqYj4_q6Mw&p=https%3A%2F%2Fblog.samouraiwallet.com%2Fpost%2F182192289762%2Fstaggered-
ricochet-utxo-tagging-paynym-ux&m=1&ts=1653240090),[ install from Google Play
for new
testers](https://t.umblr.com/redirect?z=https%3A%2F%2Fplay.google.com%2Fstore%2Fapps%2Fdetails%3Fid%3Dcom.samourai.wallet&t=NGExMjk5YzNhMTIyOWZjYmM5YmMxNWQ3YzRmNzMzOGYyNjYxOWU2YyxaWGt4VlNrSw%3D%3D&b=t%3AgssRereQbaKEWqYj4_q6Mw&p=https%3A%2F%2Fblog.samouraiwallet.com%2Fpost%2F182192289762%2Fstaggered-
ricochet-utxo-tagging-paynym-ux&m=1&ts=1653240090), or [build from source on
Github.](https://href.li/?https://github.com/Samourai-Wallet/samourai-wallet-
android/releases/tag/0.99.05)  **We will be releasing a direct download APK
including Stealth Mode on GitHub in the coming days.**

apk hash sha-256 of version 0.99.05 :
6bc4ad679d041e9d172fc2d91818c9335c0832d591864b617ff3c8b1fe49144f  
  

##  **Introducing Staggered Ricochet**

We are very happy to release a long awaited upgrade to [Ricochet
](https://href.li/?https://samouraiwallet.com/ricochet)_\- our premium
transaction designed to increase the plausible deniability of your
transactions by adding additional hops of history before the transaction
reaches the final destination -  _ This upgrade is called Staggered Ricochet
and helps decrease the fingerprint of Ricochet use by hostile exchanges and
coin scoring platforms (currently not a known threat, but certainly a possible
threat). Staggered Ricochet works by following two simple rules.

 **Rule 1 - Each Ricochet hop must be in a different block.  
** Unlike a standard Ricochet which is broadcast using a time based delay, a
Staggered Ricochet will broadcast a single transaction hop per block. This
means a Staggered Ricochet can take up to two hours before reaching the final
destination (depending on the time variance of blocks discovered).

 **Rule 2 - No transaction in the hop can be broadcast to the mempool at the
same time.  
** One of the clever ways of fingerprinting transactions that blockchain spies
have been known to use is monitoring the mempool and using associated metadata
including time first broadcast to assist in their address clustering
heuristics. To help break that method Staggered Ricochet transactions will not
be exposed to the public mempool until they are ready to be broadcast.

![image](https://64.media.tumblr.com/34085124c4100baa9a77e015cbe34815/tumblr_inline_ploup9Jcbw1tu47rq_500.png)

Staggered Ricochet is completely non custodial, just like standard Ricochet
(you can recreate the private keys of the hops at any time) and is available
to enable for no additional charge to any Ricochet transaction. **Please be
aware that Staggered Ricochet will take significantly longer to arrive at the
final destination, so time sensitive transactions should continue to use
standard Ricochet.**

##  **PayNym helper actions**

One of the great benefits of using our [PayNym
](https://href.li/?https://samouraiwallet.com/paynym)technology is the
reliable way to avoid reusing addresses (a privacy concern) with the ability
to cryptographically generate addresses on behalf of your counterparty
without needing to communicate with them (a user experience concern). We have
started to explore these concepts by adding convenience actions to the newly
added Transaction Details screen for PayNym based transactions.

![image](https://64.media.tumblr.com/d414d030c61f865f3118c49606e3501d/tumblr_inline_ploufi0lw71tu47rq_640.png)

 **" Pay Again"**

For outgoing PayNym transactions from your wallet - transactions you have sent
- you will be able to initiate direct payment to the wallet with the address
pre-filled. You can see how this type of functionality can be developed to
encompass reoccurring non custodial payments without impacting your privacy.

 **" Refund"**

For incoming PayNym transactions into your wallet - transactions you have
received - you will be able to initiate a return payment back to the sender
wallet with the amount and address pre-filled. You can see the power such a
feature can enable with a little development, especially for dynamic street
merchant use.

## UTXO Tagging and Whirlpool prep

We have added the ability to tag any UTXO with a custom value. This can be
useful for noting UTXOs that you may want to avoid spending, or the need to
add any additional meta data. These tags are local and will be lost if you
restore from mnemonic + passphrase, so you should restore via your automatic
encrypted backup whenever possible. You can currently tag UTXOs from the
Unspent Output list and will be expanded upon in coming updates.

For TestNet users: we have added in PSBT support to compliment upcoming
Whirlpool mixing and other post-mix transaction types such as 2-Person
STONEWALL and Stowaway. Bleeding edge testers will be able to manually compose
collaborative testnet Stowaway transactions using the tools found in Settings.
We anticipate advancing this to MainNet in the next releases.

 **As always we appreciate your continued support of the project.**

We are available as always to answer any questions on
[support.samourai.io](https://href.li/?https://support.samourai.io) or by
email at [support@samouraiwallet.com ](mailto:support@samouraiwallet.com)  

You can download Samourai Wallet from the [Google Play
Store](https://t.umblr.com/redirect?z=https%3A%2F%2Fplay.google.com%2Fstore%2Fapps%2Fdetails%3Fid%3Dcom.samourai.wallet&t=NGExMjk5YzNhMTIyOWZjYmM5YmMxNWQ3YzRmNzMzOGYyNjYxOWU2YyxaWGt4VlNrSw%3D%3D&b=t%3AgssRereQbaKEWqYj4_q6Mw&p=https%3A%2F%2Fblog.samouraiwallet.com%2Fpost%2F182192289762%2Fstaggered-
ricochet-utxo-tagging-paynym-ux&m=1&ts=1653240090)

  * [January 21, 2019](https://blog.samouraiwallet.com/post/182192289762/staggered-ricochet-utxo-tagging-paynym-ux)

[Older Post](https://blog.samouraiwallet.com/post/181821635197) [Newer
Post](https://blog.samouraiwallet.com/post/183378923792)
![](https://px.srvcs.tumblr.com/impixu?T=1653240090&J=eyJ0eXBlIjoidXJsIiwidXJsIjoiaHR0cDovL2Jsb2cuc2Ftb3VyYWl3YWxsZXQuY29tL3Bvc3QvMTgyMTkyMjg5NzYyL3N0YWdnZXJlZC1yaWNvY2hldC11dHhvLXRhZ2dpbmctcGF5bnltLXV4IiwicmVxdHlwZSI6MCwicm91dGUiOiIvcG9zdC86aWQvOnN1bW1hcnkiLCJub3NjcmlwdCI6MX0=&U=OBHNADIPMA&K=821132d03f34aeda23a1950139623755ad54e66347207721679da7850a06bc79&R=)![](https://px.srvcs.tumblr.com/impixu?T=1653240090&J=eyJ0eXBlIjoicG9zdCIsInVybCI6Imh0dHA6Ly9ibG9nLnNhbW91cmFpd2FsbGV0LmNvbS9wb3N0LzE4MjE5MjI4OTc2Mi9zdGFnZ2VyZWQtcmljb2NoZXQtdXR4by10YWdnaW5nLXBheW55bS11eCIsInJlcXR5cGUiOjAsInJvdXRlIjoiL3Bvc3QvOmlkLzpzdW1tYXJ5IiwicG9zdHMiOlt7InBvc3RpZCI6IjE4MjE5MjI4OTc2MiIsImJsb2dpZCI6MjM1MTUyNzczLCJzb3VyY2UiOjMzfV0sIm5vc2NyaXB0IjoxfQ==&U=MKIMLJLKEF&K=52ef5be7b68433b27a6c353e66f416953d97bbe199d8a27262b149ec4b5915a5&R=)

