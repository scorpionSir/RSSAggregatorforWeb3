[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/aeb6487b8bb0&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![ChainSecurity](https://miro.medium.com/fit/c/64/64/1*DQeE6Ua45H5MtGGv6WFVuA.png)](https://medium.com/chainsecurity?source=post_page
-----aeb6487b8bb0--------------------------------)

Published in

[ChainSecurity

](https://medium.com/chainsecurity?source=post_page-----
aeb6487b8bb0--------------------------------)

[![ChainSecurity](https://miro.medium.com/fit/c/96/96/2*IYEDevVjlqHJSXRJhxagdA.png)](/@chain_security?source=post_page
-----aeb6487b8bb0--------------------------------)

[ChainSecurity](/@chain_security?source=post_page-----
aeb6487b8bb0--------------------------------)

Follow

Jun 5, 2019

·

6 min read

# Zero Gas Price Transactions — what they do, who creates them, and why they
might impact Scalability

![](https://miro.medium.com/max/1400/1*j15_cENAw205KstAsT-P6w.jpeg)

From time to time it is important to question some fundamental assumptions
about a system, especially as auditors. Today we look at the following
assumption:

> Every transaction on Ethereum costs some Ether

It turns out that this assumption is _not completely true_.

Source: <http://gph.is/1MNW8he>

A quick recap: On Ethereum, transactions cost `Gas` depending on their
complexity. Transaction creators can set a `Gas Price` which, multiplied with
the `Gas` needed, determines the `Gas Cost` which has to be paid in Ether. Why
is paying for transactions important in Ethereum? It **limits spam attacks**
as the originator of a transaction actually needs to pay for the transaction.
It **incentivizes miners** to include transactions. A third benefit is a
little more indirect: it **prevents certain attacks against smart contracts**
as the attack cost is higher than the economic gain. As an example, integer
rounding errors in dividend-emitting contracts can give attackers very small
advantages, which in practice are made infeasible due to the much higher gas
cost of those transactions.

So why is it not completely true? In 0.5% of all blocks of the Ethereum main
chain in Q1 2019 there are transactions with an actual `Gas Price` of `0`. We
call these going forward “Zero Gas Price Transactions”.

# What they do

In the following we will analyze three different Zero Gas Price Transactions
and the purpose of these transactions.

## First transaction — Minereum token mining

Let us start by looking at
[this](https://etherscan.io/tx/0x4f719da4e138bd8ab929f4110e84d773b57376b37d1c635d26cd263d65da99cb)
transaction:

![](https://miro.medium.com/max/1400/1*9_Vtl-0T5mP5BOAD0YWIsA.png)

<https://etherscan.io/tx/0x4f719da4e138bd8ab929f4110e84d773b57376b37d1c635d26cd263d65da99cb>

This transaction was signed by account
`0x4554984fa368c745616bba60a28eb65b0976d38b` which is one of the
`[Minereum](https://www.minereum.com/)` genesis addresses. The important thing
to understand is that the _private key_ of this address is [publicly
known](https://www.reddit.com/r/Minereum/comments/6mgh6y/developer_updates/).
`Minereum` was [designed](https://www.minereum.com/mining) to have people
compete with high `Gas Price` transactions to be the first to withdraw newly
minted tokens from this address. To transfer tokens from an address, that
address needs to hold some _Ether_ to pay for the gas. In the case of this
address it is not possible as any _Ether_ sent to it will immediately be
transferred away by sweeper bots with very high `Gas Price` transactions,
effectively making any other transaction, which all have higher `Gas`
requirements, impossible. In this case the attackers succeeded because they
managed to get a transaction included where they actually did not have to pay
any Ether! There is a nice write-up of this activity here: [A Christmas
Mystery: sweepers and zero gas price
transactions](https://www.reddit.com/r/ethereum/comments/7lx1do/a_christmas_mystery_sweepers_and_zero_gas_price/).
The address used here to receive the tokens is
`0xe386e3372e3d316ae063af50c38704ec6fba5149`which is an address used in [hacks
of users](https://forum.ethereumclassic.org/t/security-issue-in-geth-console-
transfer-etc/2979).

## Second Transaction — GasToken mining

Let us look at
[another](https://etherscan.io/tx/0x7f68d647a206943eb8aa782728be58cee728c7682c9b8b1cdca7fa3a8d8ace17)
similar transaction, but this time against the
`[GasToken2](https://etherscan.io/token/0x0000000000b3f879cb30fe243b4dfee438691c04)`
contract:

![](https://miro.medium.com/max/1400/1*qNuB-nUdxTYsS45liTeAug.png)

<https://etherscan.io/tx/0x7f68d647a206943eb8aa782728be58cee728c7682c9b8b1cdca7fa3a8d8ace17>

At first sight, this looks like someone creating
`[GasTokens](https://gastoken.io)` without paying anything, which can later be
used to save gas cost, e.g. when gas prices are high. Why would a miner
include this transaction? The first reason we though of is that there were not
any pending transactions in the network at that time and the miner was simply
optimizing their profits by mining `[GasTokens](https://gastoken.io)`. But
there are several question marks behind this assumption. A miner doesn’t have
to use Zero Gas Price Transactions in the first place as they are receiving
the mining fee anyways. Also, the following block was full and paid out
roughly 5x in transaction fees, which might have been lucky, but is more
likely to indicate that the miner didn’t include all transactions on purpose.
Nevertheless, the biggest question mark by far is something else, the use of
_0x00a329c0648769a73afac7f9381e08fb43dbea72_ as the from-address which
received the mined tokens. This address is another well-known address where
the private key is publicly known: the “empty passphrase” parity address.  
Why would a miner mine tokens to this address instead of a private one?

## Third Transaction — Failing Token Transfer

Now let us look at a
[third](https://etherscan.io/tx/0x0a09242cf39152002e294b3129770ae629a239728ba4626d2b57506ec0d0975e)
type of transaction:

![](https://miro.medium.com/max/1400/1*wmrXBQzYTHjQ6J8aGLvIzA.png)

<https://etherscan.io/tx/0x0a09242cf39152002e294b3129770ae629a239728ba4626d2b57506ec0d0975e>

This transaction is _failing._ It turns out that _a lot_ of transactions with
a zero gas price are failing. In this case, a transfer of the well known
Beauty Chain Token is attempted. This project was [hacked in
2018](https://blog.peckshield.com/2018/04/22/batchOverflow/) and has paused
all trading activity since that day, causing all `transfer` calls to fail. It
is also notable that the from-address used here is very likely another address
with a known private key given that the account shows the usual sweeper bot
activity whenever Ether is transferred into it.

# Who creates them

Analyzing all of these different types of transactions leads us to the
following assumption: this activity originates very likely from a single actor
who is trying to transfer tokens away from compromised accounts. The script
used is not very sophisticated as it tries again and again to transfer tokens
which are permanently locked up. Mining tokens into these addresses might
serve as a honeypot to incentivize others to try and steal those tokens, but
given that there are easier ways it is not yet clear why the actor follows
this strategy.

There is another important component. Zero Gas Price Transactions are usually
not propagated in the network, and clients like `geth` and `parity` do not
accept them by default. Even after we configured our nodes to accept all
transactions including those with zero gas prices, we couldn’t find any such
transactions being propagated on the Ethereum P2P network. The only way
someone can include these transaction is by mining directly or by sending them
to supportive mining pools without using the Ethereum P2P layer. If you know
of a way to make a mining pool include **only** your transaction, please let
us know in the comments.

# Why it will impact scalability

So the big question is: what is the impact on the Ethereum network?

Currently, the absolute numbers of blocks containing these Zero Gas Price
Transactions are relatively minor. Only `0.5%` of all blocks mined in Q1 2019
on Ethereum Mainnet contain these types of transactions. More worrying is that
the total mining power which colludes with this actor is, while still small at
`4.3%,`not negligible. Among the mining pools who include these transactions
are well-known names like [DwarfPool](https://etherscan.io/txs?block=7408013)
and [uupool](https://etherscan.io/txs?block=7406264).

So why is this something to keep a close eye on? It is clear that miners can
increase their profits by creating transactions and include them in their
blocks, be it by design like in the case of `GasTokens` or `Minereum` or by
activity like transferring tokens from addresses which are otherwise unusable.
Currently most blocks in Ethereum are full and paid for by users with `Gas`,
which in most cases gives the mining pools more profit than to include these
transactions.

With higher maximal network throughput, which is the primary goal of Ethereum
scalability, it is to be expected that in off-peak times half-full or even
mostly empty blocks will become the norm. What would happen to the network if
miners start to fill up these blocks with transactions e.g. mining for
`GasTokens` to optimize their profits?

> Compared to mostly empty blocks, full blocks greatly increase the load on
> all participants and have the potential to cause long-term harm.

The effects of this long-term harm can already be observed [in the growing
effective costs for
](https://github.com/holiman/vmstats)`[SLOAD](https://github.com/holiman/vmstats)`[
operations](https://github.com/holiman/vmstats).

Is it enough to trust miners to not harm the network out of self-interest? How
will that change if the mining rewards for new blocks go down even more and
the transaction fees become a sizeable part of their income? Let us know what
you think in the comments!

# A short comment on EIP 1559

How will a new fee model like the one proposed by [Vitalik Buterin and Eric
Conner in EIP 1559](https://eips.ethereum.org/EIPS/eip-1559) change this? It
introduces a `BASEFEE`which gets burned, which can prevent Zero Gas Price
Transactions on the network layer (as long as the `BASEFEE` is above zero) and
by that prevent the attacks described here. While Zero Gas Price Transactions
aren’t mentioned in the motivation for the EIP, a [broad band of other
attacks](https://eips.ethereum.org/EIPS/eip-1559#motivation) are:

> […] incentivizing mining “sister blocks” that steal transaction fees,
> opening up much stronger selfish mining attack vectors, and more.

\--

2

\--

\--

2

## [More from ChainSecurity](/chainsecurity?source=post_page-----
aeb6487b8bb0--------------------------------)

From the world of secure smart contracts

[Read more from ChainSecurity](/chainsecurity?source=post_page-----
aeb6487b8bb0--------------------------------)

## Recommended from Medium

[[![Presearch Community \(NO ETH
GIVEAWAYS\)](https://miro.medium.com/fit/c/40/40/0*zDVvRrQSEFD2xs0p.png)](/@TeamPresearch?source=post_internal_links
---------0----------------------------)

[Presearch Community (NO ETH GIVEAWAYS)

](/@TeamPresearch?source=post_internal_links---------
0----------------------------)

## PRESEARCH COMMUNITY INTERVIEW #3

![](https://miro.medium.com/focal/112/112/50/50/1*YxjlyaDVEBv-
zU1ZgR7q6A.png)](/@TeamPresearch/presearch-community-
interview-3-5dc8e375c531?source=post_internal_links---------
0----------------------------)

[[![Augmented
Finance](https://miro.medium.com/fit/c/40/40/1*pIcsAqtVI1H49LaoEZTFDg.jpeg)](/@augmentedfinance?source=post_internal_links
---------1----------------------------)

[Augmented Finance

](/@augmentedfinance?source=post_internal_links---------
1----------------------------)

## Augmented Roadmap

![](https://miro.medium.com/focal/112/112/50/50/1*WkuwnOAXhtU_lY3nobhRJw.png)](/@augmentedfinance/augmented-
roadmap-df58919fb928?source=post_internal_links---------
1----------------------------)

[[![AADA](https://miro.medium.com/fit/c/40/40/1*nFOEUpVfutLeNfcpNKXM4A.jpeg)](/@aada.finance?source=post_internal_links
---------2----------------------------)

[AADA

](/@aada.finance?source=post_internal_links---------
2----------------------------)

## Aada Finance Golden IDO Round lasted only for 87 minutes

![](https://miro.medium.com/focal/112/112/50/50/1*FBhXUL-O57FB2u7lEvBmzg.png)](/@aada.finance/aada-
finance-golden-ido-round-lasted-only-
for-87-minutes-5409f3d5f280?source=post_internal_links---------
2----------------------------)

[[![Pepe
Mbon](https://miro.medium.com/fit/c/40/40/1*wlKzQBl9IzYm5QFOc5jnOQ.jpeg)](/@freitag04?source=post_internal_links
---------3----------------------------)

[Pepe Mbon

](/@freitag04?source=post_internal_links---------
3----------------------------)

## #Polygon #NFTs #Metaverse

![](https://miro.medium.com/focal/112/112/50/50/1*p8ngTrbgusJJrhCco5Hodw.jpeg)](/@freitag04/polygon-
nfts-metaverse-b9c70745106e?source=post_internal_links---------
3----------------------------)

[[![Contractium
Network](https://miro.medium.com/fit/c/40/40/1*08PpWKnuISg844AaJqma3A.jpeg)](/@contractium.io?source=post_internal_links
---------4----------------------------)

[Contractium Network

](/@contractium.io?source=post_internal_links---------
4----------------------------)

## Contractium Network: The First Global Commercial Smart Contracts Platform
Launching Its’ ICO

![](https://miro.medium.com/focal/112/112/50/50/1*xNa8TwyO4UWaBNCLGLdOJg.jpeg)](/@contractium.io/contractium-
network-the-first-global-commercial-smart-contracts-platform-launching-its-
ico-b1e6793baba6?source=post_internal_links---------
4----------------------------)

[[![CrypCade Entertainment
Systems.](https://miro.medium.com/fit/c/40/40/2*ne1dkK220D9I92Wh9KT73A.jpeg)](/@crypcade?source=post_internal_links
---------5----------------------------)

[CrypCade Entertainment Systems.

](/@crypcade?source=post_internal_links---------5----------------------------)

## CrypCade.io X Matic.Network

![](https://miro.medium.com/focal/112/112/50/50/1*LKOT6Qj9mmRFZk4YN1hHtQ.jpeg)](/@crypcade/crypcade-
io-x-matic-network-4ee6c4cc158?source=post_internal_links---------
5----------------------------)

[[![Roy
Lai](https://miro.medium.com/fit/c/40/40/1*ILsxNNu6VjRgsKU3TWzpIg.jpeg)](/@roy.lai?source=post_internal_links
---------6----------------------------)

[Roy Lai

](/@roy.lai?source=post_internal_links---------6----------------------------)

in

[Sentinel Chain

](https://medium.com/sentinelchain?source=post_internal_links---------
6----------------------------)

## Important Announcement: InfoCorp Foundation Appoints Roy Lai as New
Chairman

![](https://miro.medium.com/focal/112/112/50/50/1*Tq8qhXNI8FZNSYrycoDxsQ.jpeg)](/sentinelchain/important-
announcement-infocorp-foundation-appoints-roy-lai-as-new-
chairman-3dcac257a4e9?source=post_internal_links---------
6----------------------------)

[[![Pink Sky
Research](https://miro.medium.com/fit/c/40/40/1*XHDIA0orsgOPNXSHTQ-0yA.jpeg)](/@jpittman_77486?source=post_internal_links
---------7----------------------------)

[Pink Sky Research

](/@jpittman_77486?source=post_internal_links---------
7----------------------------)

in

[Pink Sky Group

](https://medium.com/pink-sky-group?source=post_internal_links---------
7----------------------------)

## SEC Pursues AirFox and Paragon

![](https://miro.medium.com/focal/112/112/50/50/1*DcvUK7grbFH2vAafbpBZSw.png)](/pink-
sky-group/sec-pursues-airfox-and-paragon-
ac1218dd59ca?source=post_internal_links---------7----------------------------)

[](/?source=post_page-----aeb6487b8bb0--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
aeb6487b8bb0--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
aeb6487b8bb0--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
aeb6487b8bb0--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
aeb6487b8bb0--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----aeb6487b8bb0--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----aeb6487b8bb0--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fchainsecurity%2Fzero-
gas-price-transactions-what-they-do-who-creates-them-and-why-they-might-
impact-scalability-aeb6487b8bb0&source=post_page--------------------------
nav_reg-----------)

[![ChainSecurity](https://miro.medium.com/fit/c/176/176/2*IYEDevVjlqHJSXRJhxagdA.png)](/@chain_security)

[

## ChainSecurity

](/@chain_security)

431 Followers

ChainSecurity provides security audits and conducts research and development
for blockchain platforms.

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Ff9fb56630e26&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fchainsecurity%2Fzero-
gas-price-transactions-what-they-do-who-creates-them-and-why-they-might-
impact-scalability-
aeb6487b8bb0&newsletterV3=8b14ef67c636&newsletterV3Id=f9fb56630e26&user=ChainSecurity&userId=8b14ef67c636&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Balancer
Grants](https://miro.medium.com/fit/c/40/40/1*7Q30743IqU9w9NERZNNeDg.png)](/@BalancerGrants?source=read_next_recirc
---------0---------------------9ff49b67_8b4a_4f37_a894_bc87caa824bc-------)

[Balancer Grants

](/@BalancerGrants?source=read_next_recirc---------0---------------------
9ff49b67_8b4a_4f37_a894_bc87caa824bc-------)

## Balancer Grant Wave#4 has started!

![](https://miro.medium.com/focal/112/112/50/50/0*iNqYiM5__JI8GFpd.png)](/@BalancerGrants/balancer-
grant-wave-4-has-started-7fce8d59bbd2?source=read_next_recirc---------0
---------------------9ff49b67_8b4a_4f37_a894_bc87caa824bc-------)

[[![Superfluid](https://miro.medium.com/fit/c/40/40/1*JINdTrpldrRv2LcYpoW0Vg.gif)](/@superfluid_HQ?source=read_next_recirc
---------1---------------------9ff49b67_8b4a_4f37_a894_bc87caa824bc-------)

[Superfluid

](/@superfluid_HQ?source=read_next_recirc---------1---------------------
9ff49b67_8b4a_4f37_a894_bc87caa824bc-------)

in

[Superfluid Blog

](https://medium.com/superfluid-blog?source=read_next_recirc---------1
---------------------9ff49b67_8b4a_4f37_a894_bc87caa824bc-------)

## Announcing Superfluid Prizes for ETHDenver 2022 Virtual #BUIDLATHON

![](https://miro.medium.com/focal/112/112/50/50/1*0nmEea4SDHU8hY0CZyhvxw.png)](/superfluid-
blog/announcing-superfluid-prizes-for-ethdenver-2022-virtual-
buidlathon-523757fd94d6?source=read_next_recirc---------1---------------------
9ff49b67_8b4a_4f37_a894_bc87caa824bc-------)

[[![Phil
Ngo](https://miro.medium.com/fit/c/40/40/2*qKedcCj26yPzaiDJniR_Jg.jpeg)](/@philknows?source=read_next_recirc
---------2---------------------9ff49b67_8b4a_4f37_a894_bc87caa824bc-------)

[Phil Ngo

](/@philknows?source=read_next_recirc---------2---------------------
9ff49b67_8b4a_4f37_a894_bc87caa824bc-------)

in

[ChainSafe

](https://medium.com/chainsafe-systems?source=read_next_recirc---------2
---------------------9ff49b67_8b4a_4f37_a894_bc87caa824bc-------)

## A Lodestar for Ethereum Consensus #3

![](https://miro.medium.com/focal/112/112/50/50/0*bvOGvQrVQMbppMPw)](/chainsafe-
systems/a-lodestar-for-ethereum-
consensus-3-cfa66d2b5834?source=read_next_recirc---------2
---------------------9ff49b67_8b4a_4f37_a894_bc87caa824bc-------)

[[![0xkrg](https://miro.medium.com/fit/c/40/40/0*dMc63Pu-x3eJJqMw.)](/@wanghs.thu?source=read_next_recirc
---------3---------------------9ff49b67_8b4a_4f37_a894_bc87caa824bc-------)

[0xkrg

](/@wanghs.thu?source=read_next_recirc---------3---------------------
9ff49b67_8b4a_4f37_a894_bc87caa824bc-------)

## Poseidon gate in Plonky2

](/@wanghs.thu/poseidon-gate-in-plonky2-1f5a39865b82?source=read_next_recirc
---------3---------------------9ff49b67_8b4a_4f37_a894_bc87caa824bc-------)

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

