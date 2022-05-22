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

[May 03  
2018](https://blog.samouraiwallet.com/post/173544815052/full-bech32-support-
introducing-boltzmann-and)

### [Full bech32 support, introducing Boltzmann and STONEWALL, enhanced
Ricochet transactions, and
more..](https://blog.samouraiwallet.com/post/173544815052/full-bech32-support-
introducing-boltzmann-and)

We are very happy to announce the release of Samourai 0.98.5 available to
update via Google Play for existing testers, install from [Google
Play](https://t.umblr.com/redirect?z=https%3A%2F%2Fplay.google.com%2Fstore%2Fapps%2Fdetails%3Fid%3Dcom.samourai.wallet&t=ZTEyNTNjMDAzZTUxN2M3MmUyMzJmNzcyMDA2ZTAwNTllMTAxMzUyZixTTXpoMFkzOA%3D%3D&b=t%3AgssRereQbaKEWqYj4_q6Mw&p=https%3A%2F%2Fblog.samouraiwallet.com%2Fpost%2F173544815052%2Ffull-
bech32-support-introducing-boltzmann-and&m=1&ts=1653247495) for new testers,
or build from source on [Github](https://href.li/?https://github.com/Samourai-
Wallet/samourai-wallet-android/releases/tag/0.98.50). This update is filled
with new functionality and improvements, so let's get right into it.

> sha-256: da8f64dab248447e1acc02a6f41d91a0570a7990de724987be992720838e1511

##  Full bech32 support

Bech32 is the native way of encoding segwit bitcoin addresses. Samourai Wallet
is now fully compliant with BIP84 - which means you are now able to send
externally to bech32 encoded addresses as well as receive to your own bech32
encoded addresses.  A bitcoin address encoded with bech32 starts with bc1 and
is not backwards compatible with older/unmaintained software and wallets. It
may take a while for bech32 support to fully roll out across other wallets and
services. For this reason, your Samourai wallet will still generate segwit
addresses that are backwards compatible with all bitcoin wallets (these
addresses start with a 3) by default. You can easily reveal a bech32 address
directly from the wallet Receive screen.

![image](https://64.media.tumblr.com/f731bafc47c54ae32a16a5407697f21a/tumblr_inline_p85mjeQjqM1tu47rq_500.jpg)

##  Introducing Boltzmann and STONEWALL

Since December 2017, when  [Samourai acquired the OXT block exploration
platform](https://blog.samouraiwallet.com/post/168785913782/samourai-oxt), we
have been working closely with OXT privacy and fungibility engineers to audit
the transactions that Samourai Wallet creates, looking for fingerprints and
metadata that could be extracted from public transaction data by blockchain
analysis companies. One part of this audit process involves running
transactions through a script called
[**Boltzmann**](https://href.li/?https://github.com/Samourai-Wallet/boltzmann)
\- Boltzmann returns the entropy of the transaction which measures the
linkability of inputs to outputs of a given transaction by determining the
number of individual mappings of the inputs to outputs used in the
transaction. The higher the entropy of a transaction, the more resistant to
address/identity clustering techniques used by Blockchain analysis companies -
as the element of doubt connecting ownership of addresses by any entity is too
great, and may pollute the entire cluster.

More in depth information about Boltzmann can be found in three parts by the
author and maintainer of the project:[ Part
1](https://href.li/?https://gist.github.com/LaurentMT/e758767ca4038ac40aaf),
[Part
2](https://href.li/?https://gist.github.com/LaurentMT/d361bca6dc52868573a2),
and [Part
3](https://href.li/?https://gist.github.com/LaurentMT/e8644d5bc903f02613c6).  

![image](https://64.media.tumblr.com/112cbeacfe2f68e4bec6751ab44701dd/tumblr_inline_p85mtmq4EP1tu47rq_500.png)

As part of the ongoing audit we identified a potential shortcoming which may
lead to less entropy than expected when sending via BIP126. BIP126 was
inspired by the Samourai Alpha 1 "decoy change addresses" feature and
introduced refinements to improve efficiency of the feature. As our
understanding of the latest analysis techniques further evolves, the need to
stay on the cutting edge of careful coin selection and transaction
manipulation increases in importance.

As such, we are retiring BIP126 from Samourai Wallet and we are happy to
introduce STONEWALL in replacement.. STONEWALL is a new send type available at
no extra charge to all Samourai users, enabled by default - it can be disabled
in the Transaction Settings. Whenever possible your wallet will create
transactions that simulates a CoinJoin transaction and obtains a Boltzmann
score greater than 0. Transactions will appear on the blockchain as if there
are multiple unrelated counterparties involved. STONEWALL improves on BIP126
in a number of ways. Primarily, STONEWALL activates more frequently than
BIP126 did, meaning more of your transactions will benefit from this type of
protection. Additionally, the entropy of STONEWALL transactions have been
consistently higher than BIP126 transactions during our testing. Specific
STONEWALL Algorithm information can be [reviewed
here](https://href.li/?https://gist.github.com/SamouraiDev/4ced85a29996dd56781e2bf319b93aaf).  

![image](https://64.media.tumblr.com/845e9af164934968b1af6c3c5c53960b/tumblr_inline_p85mwukB5B1tu47rq_500.png)

Samourai is committed to continuing the investment and development of
STONEWALL,  Boltzmann and other open source research and development projects
maximising privacy and fungibility of bitcoin users. Samourai users will see
further integration with Boltzmann in the near future, including the ability
to measure the entropy of transactions before they are broadcast directly in
the wallet. You can review the entropy of your bitcoin transactions today by
searching for your transaction using the [OXT Block
Explorer](https://href.li/?http://oxt.me). We look forward to polluting the
datasets of blockchain analysis companies and stone-walling their efforts to
debase the fungibility of the bitcoin token and the privacy of the bitcoin
user.  

## Ricochet Enhanced

Ricochet is one of our most popular features, and with good reason. Ricochet
provides a good layer of protection from "blanket blacklists". Blanket
blacklists are a very primitive - and stupid - form of blockchain analysis
relied upon by many exchanges that deal with Fiat currency. The blacklists are
informed by looking at the "history" of coins going back 4-5 hops, and marking
those coins "High risk" if someone at some point in time did something the
company 'analyzing' disagrees with. This form of blanket blacklisting results
in many innocent users having their accounts shut down for seemingly no
reason. Ricochet adds additional "hops" of address history between your
initial sending address and the final destination address. Today we are happy
to announce that we have updated Ricochet to use native segwit bech32
addresses for all the hop transactions. This results in lower total miner fees
for Ricochet users.  

Ricochet users who have taken the additional step of connecting to the
Samourai Donations PayNym will see increased privacy benefits when sending via
Ricochet with the introduction of a new algorithm that reduces the fingerprint
of the ricochet transaction on the blockchain. It is highly encouraged to
connect to the Samourai Donations PayNym for a big Ricochet privacy boost and
enhanced protection from blanket blacklists.  

## Stability and Android battery warning

Last but not least, we have made many modifications to the underlying Samourai
architecture to improve the stability of the wallet. Specifically, loading
times and the responsiveness after sending and receiving should be improved
for all users.  

Due to recent changes in Android 8, some users were impacted by force closes
and general stability issues. This update includes significant refactoring of
core services, which should clear up a lot of issues Android 8 users were
experiencing. This is a work in progress, if you experience any issues please
do not hesitate to contact
[support@samouraiwallet.com](mailto:support@samouraiwallet.com) for help,
support, or to report a bug.  

Another Android 8 specific issue is a persistent (and incorrect) warning that
Samourai is using too much battery impacting some users. This is again due to
changes in Android 8 which target background services. We are making the
needed changes as requested by the new Android guidelines, but they will not
be ready until the next update. You can confirm the battery warning is
erroneous by viewing more details and verifying the battery usage amount since
the last full charge of the device.  

  * [May 03, 2018](https://blog.samouraiwallet.com/post/173544815052/full-bech32-support-introducing-boltzmann-and)

  1. [![](https://assets.tumblr.com/images/default_avatar/cone_open_16.png)](https://trulife1234.tumblr.com/ "Sharing Love ")[trulife1234](https://trulife1234.tumblr.com/ "Sharing Love") liked this 

  2. [![](https://64.media.tumblr.com/avatar_36fa1c18c89f_16.pnj)](https://blog.samouraiwallet.com/ "Samourai Wallet")[samouraiwallet](https://blog.samouraiwallet.com/ "Samourai Wallet") posted this 

[Older Post](https://blog.samouraiwallet.com/post/170574017907) [Newer
Post](https://blog.samouraiwallet.com/post/176412126502)
![](https://px.srvcs.tumblr.com/impixu?T=1653247495&J=eyJ0eXBlIjoidXJsIiwidXJsIjoiaHR0cDovL2Jsb2cuc2Ftb3VyYWl3YWxsZXQuY29tL3Bvc3QvMTczNTQ0ODE1MDUyL2Z1bGwtYmVjaDMyLXN1cHBvcnQtaW50cm9kdWNpbmctYm9sdHptYW5uLWFuZCIsInJlcXR5cGUiOjAsInJvdXRlIjoiL3Bvc3QvOmlkLzpzdW1tYXJ5Iiwibm9zY3JpcHQiOjF9&U=OPNFDCPPCB&K=bd6349687714074b3bfe5ac9eda1393af848fa1e2024b66973e51baf2beff142&R=)![](https://px.srvcs.tumblr.com/impixu?T=1653247495&J=eyJ0eXBlIjoicG9zdCIsInVybCI6Imh0dHA6Ly9ibG9nLnNhbW91cmFpd2FsbGV0LmNvbS9wb3N0LzE3MzU0NDgxNTA1Mi9mdWxsLWJlY2gzMi1zdXBwb3J0LWludHJvZHVjaW5nLWJvbHR6bWFubi1hbmQiLCJyZXF0eXBlIjowLCJyb3V0ZSI6Ii9wb3N0LzppZC86c3VtbWFyeSIsInBvc3RzIjpbeyJwb3N0aWQiOiIxNzM1NDQ4MTUwNTIiLCJibG9naWQiOjIzNTE1Mjc3Mywic291cmNlIjozM31dLCJub3NjcmlwdCI6MX0=&U=EFGHDCHGFB&K=bcfcd9e5f5bcb78e3a68662979cc847b8bd0e802f186a27c06ac871dcc57cc22&R=)

