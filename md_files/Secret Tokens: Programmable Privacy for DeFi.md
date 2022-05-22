[](https://medium.com/)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/d5fd048819e2&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](https://medium.com/)

[Home](https://medium.com/)

[Notifications](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Enigma](https://miro.medium.com/fit/c/64/64/1*aIQTqQDM97_LBgHTkHGqcA.png)](https://blog.enigma.co/?source=post_page
-----d5fd048819e2--------------------------------)

Published in

[Enigma

](https://blog.enigma.co/?source=post_page-----
d5fd048819e2--------------------------------)

[![Guy
Zyskind](https://miro.medium.com/fit/c/96/96/0*ZpHXQNqEJWmyw2ZF.jpg)](https://medium.com/@GuyZ?source=post_page
-----d5fd048819e2--------------------------------)

[Guy Zyskind](https://medium.com/@GuyZ?source=post_page-----
d5fd048819e2--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Faa3e19d25a6f&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fsecret-
tokens-programmable-privacy-for-
defi-d5fd048819e2&user=Guy+Zyskind&userId=aa3e19d25a6f&source=post_page-
aa3e19d25a6f----d5fd048819e2---------------------follow_byline-----------)

Aug 12, 2020

·

8 min read

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fd5fd048819e2&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fsecret-
tokens-programmable-privacy-for-
defi-d5fd048819e2&source=--------------------------bookmark_header-----------)

[

Save

](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fd5fd048819e2&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fsecret-
tokens-programmable-privacy-for-
defi-d5fd048819e2&source=--------------------------bookmark_header-----------)

# Secret Tokens: Programmable Privacy for DeFi

## How Secret Network can create network effects for privacy, providing the
missing piece for DeFi mass adoption.

![](https://miro.medium.com/max/1400/1*40zdJt8QIC8_DVUhG6motw.png)

 _Part of the “Secret Solutions” series, this post explores how solving for
privacy with_[ _Secret Network_](https://scrt.network) _(for which Enigma is a
core contributor) helps with adoption and growth of decentralized
technologies._

 _Today, Enigma CEO_[ _Guy Zyskind_](https://twitter.com/guyzys) _writes
about_[ _programmable privacy_](https://blog.scrt.network/programmable-
privacy/) _for decentralized finance and introduces the concept of “secret
tokens”, which creates network effects for privacy._ ** _Read on to learn
about our vision,_**[ ** _see the
code_**](https://github.com/enigmampc/secret-secret) ** _for “secret tokens,”
(currently working on public testnet) and find out how you can start building
alongside us!_**

![](https://miro.medium.com/max/1000/0*B_UKBzkSb0aix8T0.png)

As builders in the blockchain space, we believe in the promise of open
protocols and economies. Decentralized finance (DeFi) can form a [superior
financial system](https://www.placeholder.vc/blog/2020/6/13/a-superior-
financial-system) both for users and innovators. Users can now opt-in to
services they want to use at low cost, easily switch between services, and
even become owners and earn voting rights for the products they use — all
built on an interconnected system of blockchains. What have historically been
passive assets now become productive assets. Creative minds can develop a
practically unlimited list of financial instruments and services, all
controlled by a series of smart contracts meant to ensure fair dealing and
safety of funds.

Thanks to smart contract composability, the possibilities for DeFi appear
endless, “compounding” on an almost daily basis. Why not make your ETH work
for you by locking it on Maker to get Dai in return, then lending that Dai to
earn interest on Compound, all while earning COMP tokens that can be used for
governance, or sold for an additional gain? Even with all its recent growth,
we’ve only scratched the surface of what’s possible with decentralized
finance.

However, we are currently well short of achieving the actual promise of
decentralized finance and open economies. Unfortunately, DeFi has inherited
the same shortcoming of all blockchains **— there is no privacy for users, and
data is public by default**. DeFi cannot hope to eventually reach mass
adoption as a complex and complete open financial system if financial privacy
must be sacrificed.

We are still in the bleeding-edge “innovators” phase of the adoption curve for
DeFi. [Recently we reached $4 billion of “total value locked” in
DeFi.](https://cointelegraph.com/news/total-value-locked-in-defi-hits-new-ath-
of-4b) While that’s an impressive milestone, **we should aspire to “cross the
chasm” and reach a $4 trillion AUM target for DeFi.** This target is more than
10x the current market cap of the crypto ecosystem and [~10% of AUM in
traditional financial
markets](https://www.ussif.org/files/2018%20_Trends_OnePager_Overview\(2\).pdf).

![](https://miro.medium.com/max/1400/0*hvQbHd9OLUfdM-_W)

To reach trillions in value, **we need meaningful retail and institutional
adoption — and for that we need _privacy._** We are already seeing
institutional players building consortium chains with privacy features and
eschewing public chains. We cannot expect the vast majority institutional or
retail users to adopt DeFi products when all their financial history is
publicly visible.

 **While there has been some progress, privacy solutions in DeFi today haven’t
gone far enough.** “Transactional privacy” **** is the case of simple peer-to-
peer transactions where the goal is to protect the privacy of individuals by
hiding the sender and recipient of a transaction (anonymity) and the amount
sent (confidentiality) **.** Many potential solutions have emerged in recent
years (zero knowledge proofs, ring signatures, Mimblewimble, coin mixers,
etc.), illustrating how crucial solving the transactional privacy problem is
for blockchains.

However, solving for this narrow transactional use case won’t be the
sustainable long-term solution. More elaborate and flexible use cases will
appear in time that utilize the full programmable potential of smart
contracts. DeFi is beginning to prove this point at scale. **Solving the
privacy problem for _any smart contract_** **is the promise of Secret Network,
which allows privacy to be fully baked into any smart contract, thus**[
**turning it into a Secret Contract**](https://blog.scrt.network/programmable-
privacy/) **.**

It’s Secret Network’s capacity for programmable privacy can provide the major
missing piece for explosive DeFi growth. Read on to see how it works.

> See our [July Ecosystem Update](https://blog.scrt.network/secret-network-
> ecosystem-update-july-2020/) for more info on Secret Network!

![](https://miro.medium.com/max/1000/0*zAkaQPmM039FMbw7.png)

# Introducing network effects for privacy in DeFi

Imagine a system where any operation you do, across any DeFi service (be it
trading, staking, lending, providing liquidity, issuing synthetic tokens,
etc.) happens with complete privacy. **That’s the vision of programmable
privacy and Secret Network.** This is obviously great for data privacy, but
actually, there’s something even bigger at play here.

 **Each DeFi user actually gains more privacy with each additional DeFi
service and every dollar worth of additional value locked in the ecosystem,
leading to privacy network effects.** The reason for this is that the
aggregate liquidity across _all DeFi applications_ directly quantifies the
level of privacy you obtain (this is also known as the _anonymity set_ ).
Think about these privacy gains like vaccination: the more people who
inoculate themselves by using Secret Network to protect their privacy, the
more benefits everyone else in the Secret DeFi ecosystem can gain.

![](https://miro.medium.com/max/1400/0*Ic4dgb6J7xnLdSWu.png)

Many people already care about privacy — enough to use dedicated services like
mixers. But mixers require users to come up with separate liquidity pools,
failing to achieve network effects. **Secret DeFi can combine the enthusiastic
pioneers of DeFi with those who passionately believe in the necessity of
privacy.** Privacy enthusiasts would enter DeFi because the higher liquidity
means more privacy. Conversely, DeFi enthusiasts would see more liquidity
coming from both themselves and their privacy-aware peers.

So how can this work?

# Step 1: Secret Tokens

It all starts with **Secret Tokens** , which is a token mimicking the ERC-20
standard that has the benefit of:

  1. Having all balances be encrypted
  2. Having the arguments into a transfer operation be encrypted

Simply put, this ensures that any transaction and all rolling balances are
forever kept encrypted. Each person can still query their own (and only their
own) balance, as well as send tokens to others, privately. With very small
changes, **Secret Network can take a normal implementation of a token standard
(like ERC-20, but WASM-compatible) and turn it into Secret Token standard.**

Excitingly, a functioning prototype of secret tokens is already [available
here](https://github.com/enigmampc/secret-secret) and live on our public
testnet!

![](https://miro.medium.com/max/1400/0*-cFnypP931r7GPZN.png)

# Step 2: Non-private Collateral

With this reference implementation of a “Secret Token” standard, the next step
is to allow depositing a regular (public) coin/token (e.g., ATOM, SCRT) and
obtaining in return a synthetic Secret Token. [Our reference
implementation](https://github.com/enigmampc/secret-secret) does this for SCRT
— it allows you to deposit X amount of SCRT (which is not private by itself)
and instead obtain X amount of “secretSCRT” — the privacy-preserving Secret
Token version of SCRT. **The same can be done for any asset in the Cosmos
ecosystem (with IBC) — and in the future from Ethereum and other ecosystems as
well**.

# Step 3: Use privately in DeFi

Now that you have a Secret Token version of your asset, you can use it on a
variety of DeFi services that are built on the Secret Network ecosystem.
Imagine a Secret Swap that works similarly to [Uniswap](https://uniswap.org/),
allowing users to add liquidity to a pool and trade against that pool. The
balances of the Secret Tokens in the pool would be publicly available. This is
essential to set the price for the trading pair. However, the individual
contributors to the pool would remain anonymous because the contract state
would remain encrypted. Users can then swap Secret Tokens privately and no one
but the user themselves would be able to see their balance. This is because
the state of the Secret Tokens contract, where all the balances and token
holders are listed, would again be encrypted.

![](https://miro.medium.com/max/1400/0*V31sX33JTVRdH4T1.png)

Similarly to secret swaps, users can lend Secret Tokens like they do today on
[Compound](https://compound.finance/), contribute to different Automated
Market Making (AMM) liquidity pools like
[Balancer](https://balancer.finance/), participate in auctions or order book
based trading like in [0x](https://0x.org/), and participate in the governance
of secret DeFi.

In addition, programmable privacy in DeFi solves the problem of front-running.
Since orders are never visible on the mempool, no attacker or malicious miner
can front-run orders and profit at users’ expense. _(See the Enigma blog for
our previous writing on_[ _DeFi front-running_](/preventing-dex-front-running-
with-enigma-df3f0b5b9e78) _.)_

Furthermore, programmable privacy can help preserve fair markets. Projects
like Strike Protocol are looking into introducing AMM model to manage
positions (clearing house) in a [Leveraged PerpetualSwap
product](https://docs.strike.network/getting-started/how-it-works). However,
this type of product can be exploited if all positions are public. If Alice
publicly creates a positon at t = 1, and Bob (seeing this) publicly creates a
position that’s public to the network (and therefore Alice as well) at t = 2,
Alice can see this and strategically close her position to profit at the
direct expense of Bob. With Secret DeFi, these positions would be private
(part of the encrypted state) and impossible to directly exploit.

> For more on this, you can refer to the “[How It
> Works](https://docs.strike.network/getting-started/how-it-works)” section in
> the Strike Protocol documentation linked above.

# Step 4: Withdraw

Once you’re done, you can withdraw the underlying assets by burning the
corresponding synthetic Secret Tokens that make up your position. In the
process, you may have taken a lot of actions (e.g., you may have started with
SCRT, but ended up with ATOM, KAVA, LUNA, or even a synthetic version of BTC /
ETH / ERC-20 tokens), but no one would be able to track the movement from the
original deposit to the end result. **You have gained privacy proportional to
all the users using all DeFi services and all types of Secret Tokens that
exist in the ecosystem**. With Secret Network, privacy enjoys the benefit of
network effects.

# How can you help?

This all sounds pretty good — but we’re builders, not bloggers. Right now the
entire [Secret community](https://scrt.network/about) is working together to
set a direction for protocol development, educational and awareness
initiatives, node runner adoption, governance, and perhaps most importantly,
**key use cases and applications like what we’ve described here.**

[With our incentivized testnets for secret contracts already
active](https://blog.scrt.network/secret-games-update-testnet-phase-1/) and
the secret contract mainnet upgrade tentatively scheduled for early October,
we are rapidly approaching the launch of these applications. Before (and when)
this occurs, we are looking for [developers](https://bit.ly/secretdeveloper),
partners, and early users to help scale key applications like Secret Tokens.

In the meantime, we’d love your feedback on this post and your ideas on how to
expand this vision for privacy-preserving open economies that gain from
network effects! Please post here on the [Secret Forum](https://bit.ly/secret-
forum) — we’d be happy to hear your thoughts and connect.

# Onwards and upwards!

 _~ Guy Zyskind, Enigma CEO and cofounder_

> Thanks to Can Kisagun, Tom Schmidt, Avichal Garg, Ash Egan, and Zaki Manian
> for their comments and review of this article and concepts.

![](https://miro.medium.com/proxy/1*1kydiFy8MJU-Fp16vT_zZw.png)

 _To discuss Secret Network and join the community, visit our official
channels:_  
[Forum](https://forum.scrt.network/) |
[RocketChat](https://chat.scrt.network/) |
[Twitter](https://twitter.com/SecretNetwork) |
[Telegram](https://t.me/scrtnetwork) |
[Discord](https://blog.enigma.co/enigma.co/discord)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fenigmampc%2Fd5fd048819e2&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fsecret-
tokens-programmable-privacy-for-
defi-d5fd048819e2&user=Guy+Zyskind&userId=aa3e19d25a6f&source=-----d5fd048819e2
---------------------clap_footer-----------)

\--

2

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fenigmampc%2Fd5fd048819e2&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fsecret-
tokens-programmable-privacy-for-
defi-d5fd048819e2&user=Guy+Zyskind&userId=aa3e19d25a6f&source=-----d5fd048819e2
---------------------clap_footer-----------)

\--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fenigmampc%2Fd5fd048819e2&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fsecret-
tokens-programmable-privacy-for-
defi-d5fd048819e2&user=Guy+Zyskind&userId=aa3e19d25a6f&source=-----d5fd048819e2
---------------------clap_footer-----------)

\--

2

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fd5fd048819e2&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fsecret-
tokens-programmable-privacy-for-
defi-d5fd048819e2&source=--------------------------bookmark_footer-----------)

## [More from Enigma](https://blog.enigma.co/?source=post_page-----
d5fd048819e2--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Fenigmampc%2Fd5fd048819e2&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fsecret-
tokens-programmable-privacy-for-
defi-d5fd048819e2&collection=Enigma&collectionId=6cb5d792f282&source=post_page
-----d5fd048819e2---------------------follow_footer-----------)

Official Blog of Enigma - Securing the Decentralized Web.

[Read more from Enigma](https://blog.enigma.co/?source=post_page-----
d5fd048819e2--------------------------------)

## Recommended from Medium

[[![Lumerin
Protocol](https://miro.medium.com/fit/c/40/40/1*VMF6PHZhDqW9xu0Wm3vQEg.png)](https://lumerinprotocol.medium.com/?source=post_internal_links
---------0----------------------------)

[Lumerin Protocol

](https://lumerinprotocol.medium.com/?source=post_internal_links---------
0----------------------------)

in

[Lumerin Blog

](https://medium.com/lumerin-blog?source=post_internal_links---------
0----------------------------)

## Demystifying Bitcoin’s energy consumption: How much does it really use?

![](https://miro.medium.com/focal/112/112/50/50/0*sCVJQ0G-ZvuGLG7t)](https://medium.com/lumerin-
blog/demystifying-bitcoins-energy-consumption-how-much-does-it-really-
use-130f5c98290b?source=post_internal_links---------
0----------------------------)

[[![TradeKax
Exchange](https://miro.medium.com/fit/c/40/40/2*V_MfVeuaGjG4g30n1bOXUw.png)](https://medium.com/@TradeKax?source=post_internal_links
---------1----------------------------)

[TradeKax Exchange

](https://medium.com/@TradeKax?source=post_internal_links---------
1----------------------------)

## The criteria to choose a safe and reputable cryptocurrency exchange

![](https://miro.medium.com/focal/112/112/50/50/1*L8Ve1QPAFGcPvv7W2wisHQ.png)](https://medium.com/@TradeKax/the-
criteria-to-choose-a-safe-and-reputable-cryptocurrency-
exchange-6902ac21c74?source=post_internal_links---------
1----------------------------)

[[![Mick
Tsai](https://miro.medium.com/fit/c/40/40/1*s8pMbDgAcJs6vMcQoCylFQ.png)](https://contentosmicktsai.medium.com/?source=post_internal_links
---------2----------------------------)

[Mick Tsai

](https://contentosmicktsai.medium.com/?source=post_internal_links---------
2----------------------------)

in

[Contentos

](https://medium.com/contentos-io?source=post_internal_links---------
2----------------------------)

## Libra Offers Growth Opportunities for Contentos

![](https://miro.medium.com/focal/112/112/50/50/0*Cq0aqlEZyZJ1dCTO.jpg)](https://medium.com/contentos-
io/libra-offers-growth-opportunities-for-contentos-
bc4593112b8f?source=post_internal_links---------2----------------------------)

[[![ULAND](https://miro.medium.com/fit/c/40/40/1*I4vvLDQKu_s6qkoIPOcerA.png)](https://ulanders.medium.com/?source=post_internal_links
---------3----------------------------)

[ULAND

](https://ulanders.medium.com/?source=post_internal_links---------
3----------------------------)

## Special Announcement: ULAND Security Audit — In Progress

![](https://miro.medium.com/focal/112/112/50/50/1*SXqIr31IPfVxLXLNaUeRPA.png)](https://ulanders.medium.com/special-
announcement-uland-security-audit-in-
progress-908ff00de756?source=post_internal_links---------
3----------------------------)

[[![Richard
Draper](https://miro.medium.com/fit/c/40/40/0*Bo6T7ZfloipckZUh.)](https://medium.com/@dickiedraper?source=post_internal_links
---------4----------------------------)

[Richard Draper

](https://medium.com/@dickiedraper?source=post_internal_links---------
4----------------------------)

## NFT lending — moving beyond blue-chip projects

![](https://miro.medium.com/focal/112/112/50/50/1*S2c7YcmGOvTAhqve6j0Dcg.png)](https://medium.com/@dickiedraper/nft-
lending-moving-beyond-blue-chip-
projects-508f0b562b68?source=post_internal_links---------
4----------------------------)

[[![Neptuneprotocol](https://miro.medium.com/fit/c/40/40/1*gELDXGMZh54oZBA-
KKR6PA.jpeg)](https://medium.com/@NeptuneOfficial?source=post_internal_links
---------5----------------------------)

[Neptuneprotocol

](https://medium.com/@NeptuneOfficial?source=post_internal_links---------
5----------------------------)

## Tokenomics

![](https://miro.medium.com/focal/112/112/50/50/1*1DSUVROSnToDDJqdi7_GiQ.jpeg)](https://medium.com/@NeptuneOfficial/tokenomics-7308e2e4268d?source=post_internal_links
---------5----------------------------)

[[![Andrej](https://miro.medium.com/fit/c/40/40/2*4yTLlkWZc83NeztCvpDXSg.jpeg)](https://andrej-
rakic.medium.com/?source=post_internal_links---------
6----------------------------)

[Andrej

](https://andrej-rakic.medium.com/?source=post_internal_links---------
6----------------------------)

## Facebook’s Libra Blockchain Programming Tutorial

![](https://miro.medium.com/focal/112/112/50/50/1*BtIbt09xN5WbuA6CU-
trnQ.png)](https://andrej-rakic.medium.com/facebooks-libra-blockchain-
programming-tutorial-e54e91b3efb3?source=post_internal_links---------
6----------------------------)

[[![Richard
Appiah](https://miro.medium.com/fit/c/40/40/1*gy4HYu7nGUQkGf4RirseJA.png)](https://appiahr88.medium.com/?source=post_internal_links
---------7----------------------------)

[Richard Appiah

](https://appiahr88.medium.com/?source=post_internal_links---------
7----------------------------)

in

[ILLUMINATION

](https://medium.com/illumination?source=post_internal_links---------
7----------------------------)

## 5 Easy Step Guide To Make Money With NFTs In 2022(For Beginners)

![](https://miro.medium.com/focal/112/112/50/50/1*k_-
Ns_u1n09UbpfNkiH6IQ.jpeg)](https://medium.com/illumination/5-easy-step-guide-
to-make-money-with-nfts-in-2022-for-
beginners-e2ec67d3c3fe?source=post_internal_links---------
7----------------------------)

[](https://medium.com/?source=post_page-----
d5fd048819e2--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
d5fd048819e2--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
d5fd048819e2--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
d5fd048819e2--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
d5fd048819e2--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----d5fd048819e2--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----d5fd048819e2--------------------------------)

[Get
started](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fsecret-
tokens-programmable-privacy-for-defi-d5fd048819e2&source=post_page
--------------------------nav_reg-----------)

[![Guy
Zyskind](https://miro.medium.com/fit/c/176/176/0*ZpHXQNqEJWmyw2ZF.jpg)](https://medium.com/@GuyZ)

[

## Guy Zyskind

](https://medium.com/@GuyZ)

770 Followers

Founder & CEO at @EnigmaMPC — building a new decentralized ecosystem.
Previously @MIT @medialab

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Faa3e19d25a6f&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fsecret-
tokens-programmable-privacy-for-
defi-d5fd048819e2&user=Guy+Zyskind&userId=aa3e19d25a6f&source=post_page-
aa3e19d25a6f-------------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fb5e8570f77d0&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fsecret-
tokens-programmable-privacy-for-
defi-d5fd048819e2&newsletterV3=aa3e19d25a6f&newsletterV3Id=b5e8570f77d0&user=Guy+Zyskind&userId=aa3e19d25a6f&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Spectre
Protocol](https://miro.medium.com/fit/c/40/40/1*S0zDriOVvWKmuBfqHXhBXQ.jpeg)](https://spectre-
protocol.medium.com/?source=read_next_recirc---------0---------------------
281987d3_0209_445e_92f5_885a1b029061-------)

[Spectre Protocol

](https://spectre-protocol.medium.com/?source=read_next_recirc---------0
---------------------281987d3_0209_445e_92f5_885a1b029061-------)

## Spectre Protocol - Ghostpaper v1 A completely anonymous cryptocurrency
asset management &…

](https://spectre-protocol.medium.com/spectre-protocol-
ghostpaper-v1-a-completely-anonymous-cryptocurrency-asset-
management-231d2a685b5e?source=read_next_recirc---------0---------------------
281987d3_0209_445e_92f5_885a1b029061-------)

[[![OolongSwap](https://miro.medium.com/fit/c/40/40/1*DWhVhSrlzIZ2zHtNG5TZwQ@2x.jpeg)](https://oolongswap.medium.com/?source=read_next_recirc
---------1---------------------281987d3_0209_445e_92f5_885a1b029061-------)

[OolongSwap

](https://oolongswap.medium.com/?source=read_next_recirc---------1
---------------------281987d3_0209_445e_92f5_885a1b029061-------)

## Oolong Welcomes Olympus DAO to Multea Farm (and more!)

![](https://miro.medium.com/focal/112/112/50/50/1*ORJpD0PeajczDIdAdoZJYw.png)](https://oolongswap.medium.com/oolong-
welcomes-olympus-dao-to-multea-farm-and-
more-2cf25d324bb4?source=read_next_recirc---------1---------------------
281987d3_0209_445e_92f5_885a1b029061-------)

[[![ShineDAO](https://miro.medium.com/fit/c/40/40/1*CkcdzIYbr7c2S2w6dX1SfQ.png)](https://shinedao.medium.com/?source=read_next_recirc
---------2---------------------281987d3_0209_445e_92f5_885a1b029061-------)

[ShineDAO

](https://shinedao.medium.com/?source=read_next_recirc---------2
---------------------281987d3_0209_445e_92f5_885a1b029061-------)

## Introducing veSHN

![](https://miro.medium.com/focal/112/112/50/50/1*Z8MDk14bUiVr7qTwBlNPpQ.png)](https://shinedao.medium.com/introducing-
veshn-6e9786de2550?source=read_next_recirc---------2---------------------
281987d3_0209_445e_92f5_885a1b029061-------)

[[![NewB.Farm](https://miro.medium.com/fit/c/40/40/1*RWcphtzpJ5mmDlQ4kzudhA.png)](https://newbfarm.medium.com/?source=read_next_recirc
---------3---------------------281987d3_0209_445e_92f5_885a1b029061-------)

[NewB.Farm

](https://newbfarm.medium.com/?source=read_next_recirc---------3
---------------------281987d3_0209_445e_92f5_885a1b029061-------)

## The Decentralized Currency & the Rise of DEFI & DEX! [Explained]

![Rise of Crypto, DeFi, and
DEX](https://miro.medium.com/focal/112/112/50/50/1*wq8btpaP0iV1q2pRghZIeg.jpeg)](https://newbfarm.medium.com/the-
decentralized-currency-the-rise-of-defi-dex-
explained-88d7e5b5ce7d?source=read_next_recirc---------3---------------------
281987d3_0209_445e_92f5_885a1b029061-------)

[Help

](https://help.medium.com/hc/en-us)

[Status

](https://medium.statuspage.io)

[Writers

](https://about.medium.com/creators/)

[Blog

](https://blog.medium.com)

[Careers

](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e)

[Privacy

](https://policy.medium.com/medium-privacy-policy-f03bf92035c9)

[Terms

](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f)

[About

](https://medium.com/about?autoplay=1)

[Knowable

](https://knowable.fyi)

