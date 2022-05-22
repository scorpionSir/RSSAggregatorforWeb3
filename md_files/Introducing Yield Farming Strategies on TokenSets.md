[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/60d114e0172c&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Set
Labs](https://miro.medium.com/fit/c/64/64/1*z_Dy4ahAIeEQC7bguxrRPA.png)](https://medium.com/set-
protocol?source=post_page-----60d114e0172c--------------------------------)

Published in

[Set Labs

](https://medium.com/set-protocol?source=post_page-----
60d114e0172c--------------------------------)

[![Anthony
Sassano](https://miro.medium.com/fit/c/96/96/1*jdMf10Tdlr17rBVVQVyUbg.png)](/@AnthonySassano?source=post_page
-----60d114e0172c--------------------------------)

[Anthony Sassano](/@AnthonySassano?source=post_page-----
60d114e0172c--------------------------------)

Follow

Sep 22, 2020

·

7 min read

#  **Introducing Yield Farming Strategies on TokenSets**

## The first yield farming strategies are now live on TokenSets!

![](https://miro.medium.com/max/1400/1*pKd3_sqJYV63PobPga8rXQ.png)

Today, we’re excited to announce the launch of our new line of products, yield
farming strategies! Like the [recently launched](/set-protocol/introducing-
the-defi-pulse-index-on-tokensets-79f87c6b295b) DeFi Pulse Index, these
strategies are built on Set Protocol’s new v2 infrastructure and they are part
of the second phase of the [Set v2 rollout plan](/set-protocol/the-
set-v2-rollout-explained-308f4859fb12).

The first Yield Strategy going live today is the [ETH USD Yield
Farm](https://www.tokensets.com/portfolio/usdapy) which automatically farms
the $UNI token by providing liquidity to the ETH/DAI pair on
[Uniswap](https://app.uniswap.org/#/uni). In the future, the strategy may
expand to all ETH/Stablecoin and ETH/Bitcoin pairs.

We take security seriously at Set and we always strive to ensure that our
smart contracts are as safe as they can be thorough external audits. However,
these new strategies have only had the critical parts of the system audited,
with the Uniswap strategy contract managing the Set only internally audited.
Users should be aware of this and exercise caution when depositing funds.

##  **Key points**

  * The ETH USD Yield Farm is now [available on TokenSets](https://www.tokensets.com/portfolio/usdapy)
  * This strategy will automatically farm $UNI tokens and reinvest the proceeds back into the strategy
  * More yield farming products are coming soon

# LP Yield Farming on TokenSets

There is currently no way to automatically rebalance between the best LP
(liquidity provider) pair yield opportunities on Ethereum (e.g. take a Uniswap
liquidity provider position and put it in the best yielding pools). The ETH
USD Yield Set that we launched today will allow users to pay with a single
asset and get access to a strategy that automatically claims tokens from an LP
farm, sells it for the underlying assets, and reinvests it into the farm.

# How the LP Yield Strategies Work

The LP Yield strategies aim to make yield farming accessible to everyone — not
just those who can afford Ethereum’s high network fees or those who have
specialized or insider knowledge. To that end, we’ve designed the LP Yield
strategies to be as simple as possible — here is how they work.

  1.  **Deposit** — ETH and USD is deposited into the [Uniswap ETH/USD LP](https://app.uniswap.org/#/uni) pool staked in $UNI rewards.
  2.  **Claim** — The farmed $UNI is claimed and reinvested into the ETH/USD LP pool to farm more rewards.
  3.  **Repeat** — The strategy repeats this process until it rotates to a new pool to farm.

##  **Issuance**

Users can simply deposit either ETH or DAI into one of the strategies. In
return, the user receives a corresponding ownership of the pool based on its
net asset value. This innovative issuance design we call ‘net asset value
issuance’ or ‘ **NAV issuance** ’, enables users to deposit any allowed ERC20
token to issue new Sets without needing to replicate the Set’s positions. This
means **big gas savings** for you on issuance and redemption.

There is a 0.35% premium that the user pays when entering the strategy which
is distributed to existing members of the pool to disincentivize oracle
mismatch arbitrage. This mechanism can be compared to an insurance deposit,
where users receive this deposit back as more people transact afterwards. This
effectively **boosts APY** for long-term holders of the strategy.

##  **Redemption**

When a user wants to exit one of these strategies, they can simply withdraw
from their position on TokenSets which utilizes what we call ‘ **NAV redeem**
’ to exit the position to ETH or stablecoins. In doing this, the user incurs a
0.3% withdrawal fee and a 0.35% premium that is redistributed back into the
pool and effectively **boosts APY** for long-term holders of the strategy.

There is also a limit of 500 WETH or $200,000 in stablecoins for what a user
can redeem in a single transaction. This is to make sure there is enough
capital as reserves to help facilitate other redemptions.

The pool targets a 1% of all capital allocated to the reserves in order to
redeem out of the pool which rebalances anytime the reserve assets go below
0.5% of the total pool’s value. This pool of reserves is what’s used to
provide redemption liquidity, meaning that redeems greater than what’s
available in the reserves will not go through.

As the pool of capital in the Set grows, so too will the size of the reserves
and size of redemptions available to take out. While the reserves are low,
it’s recommended that users redeem in smaller amounts over time as the pool
continues to rebalance its reserves to provide exit liquidity.

## Claim Fee

The ETH USD Yield Farm claims LP rewards and stakes ETH/USD every 24 hours. A
5% fee is applied to all claimed LP rewards which is paid out to the Set
Manager. This fee is used to pay gas costs required to claim, sell, and stake
the yield farm LP rewards.

When you deposit your funds, you receive an ERC20 token called ‘Sets’. These
can be stored in any Ethereum wallet that supports these tokens such as
MetaMask, Coinbase Wallet, Trust Wallet, Argent and many more.

# Impermanent Loss Risk

The ETH USD Yield Farm utilizes Uniswap which is an automated market maker
(AMM). Due to this, there is a risk of what is known as “impermanent loss”
associated with this strategy. Don’t let the name fool you though — losses can
become permanent depending on when you enter or exit a liquidity provider (LP)
position. If you enter into the ETH USD Yield Farm, you will be exposed to
impermanent loss risk and you should be aware of what this means for you.

We highly recommend learning about impermanent loss. You can get a detailed
understanding on what impermanent loss is through this
[article](/@pintail/uniswap-a-good-deal-for-liquidity-providers-104c0b6816f2).

# How to Buy

Entering into the ETH USD Yield Farm is easy as you only need ETH or the
currently weighted stablecoin to get started. Let’s walk through a guide on
how to start farming $UNI tokens using the ETH USD Yield Farm on TokenSets.
[Click here](https://www.tokensets.com/portfolio/usdapy) to get started.

![](https://miro.medium.com/max/1400/1*7fiZE16WSGZQrp_eqS3-WA.png)

On this page, you can find all of the relevant information about the ETH USD
Yield Farm including performance history, current composition and technical
details like its associated Ethereum address.

Once you’re logged into your account, feel free to hit the **Buy** button
which will bring up the buy window. From here, input the amount of the ETH or
stablecoins that you wish to use.

![](https://miro.medium.com/max/994/1*57hkdjW9i4QoNJYTK6Rh9Q.png)

Now you can click the **Preview Buy** button which will display the summary of
your order. If you’re comfortable with the order, hit **Submit Buy** and then
confirm the transaction on your Ethereum wallet. This will automatically
convert your ETH or stablecoins into Uniswap LP tokens and stake them in the
strategy.

![](https://miro.medium.com/max/988/1*TJf_hdTpiJzWBzzHTFDZrw.png)

Congratulations — you are now automatically yield farming the $UNI token with
all proceeds reinvested to farm even more! You can store this Set anywhere
that you usually store your ERC20 tokens — be that in your favorite desktop or
mobile wallet or in your TokenSets account.

# Keeping Pace with DeFi

The DeFi ecosystem is evolving at an incredible pace with new and innovative
products going live every single week. At Set, we’ve been heads down building
out v2 for a couple of months now and it will enable us to ship products
faster than we ever have before.

We have many more exciting releases coming as we continue to execute on the
[Set v2 rollout plan](/set-protocol/the-set-v2-rollout-explained-308f4859fb12)
and beyond.

If you have any interesting product ideas you want to see come live on Set,
message us on [Discord](https://discord.gg/kNsYA6A) or email us at
hello@setprotocol.com. We’d love to hear your thoughts.

# Frequently Asked Questions

## Are more yield farming strategies coming to TokenSets?

You bet! We have plans to release new yield farming strategies to the
TokenSets platform in the near future.

## Are there any fees associated with the yield farming strategies?

Yes, there is a 0.3% withdrawal fee that is also paid to the manager upon
redemption of funds from a strategy, and a 5% fee on the APY gained.

## What is the issuance premium?

The 0.35% NAV issuance and redemption premium protects against oracle-related
arbitrage attacks and is accrued to existing strategy holders upon depositing
or withdrawing funds into a strategy.

## Have the new contracts been audited?

We take security seriously at Set and ensure the base protocol smart contracts
follow security best practices and are externally audited. In saying that, the
[Uniswap strategy
contract](https://etherscan.io/address/0xca64426a1683610C494EAFf712E922608205f432)
managing the Set is currently unaudited at launch so users should be aware of
this and exercise caution when depositing funds.

If you have any suggestions for other Yield Farming strategies or general V2
products, let us know [here](https://setlabs.typeform.com/to/jpi4nDuF).

# Learn more about Set and join our community

[ **Newsletter**](https://cdn.forms-content.sg-
form.com/ec247aa9-142e-11ea-905e-eaa9a3ed73b8) **|**[
**TokenSets**](http://tokensets.com/) **|**[
**Website**](http://setprotocol.com/) **|**[
**Medium**](https://medium.com/set-protocol) **|**[
**Twitter**](https://twitter.com/setprotocol) **|**[
**Discord**](https://discord.gg/ZWY66aR)

\--

3

\--

\--

3

## [More from Set Labs](/set-protocol?source=post_page-----
60d114e0172c--------------------------------)

Set Protocol is an open-source protocol that leverages DeFi enabling everyone
to build market-leading, innovative structured products. TokenSets is a
seamless portal into Set Protocol, allowing users, through Web3, to build and
get exposure to structured products.

[Read more from Set Labs](/set-protocol?source=post_page-----
60d114e0172c--------------------------------)

## Recommended from Medium

[[![Decentralized
Club](https://miro.medium.com/fit/c/40/40/0*_gEwFBg2-30dEFXt)](/@decentralizedclub?source=post_internal_links
---------0----------------------------)

[Decentralized Club

](/@decentralizedclub?source=post_internal_links---------
0----------------------------)

## The Sandbox AMA Summary with ecentralized Club✔️

![](https://miro.medium.com/focal/112/112/50/50/1*348nnFktZHMEIxDs-a2viw.jpeg)](/@decentralizedclub/the-
sandbox-ama-summary-with-ecentralized-
club-️-8f9a4109bad5?source=post_internal_links---------
0----------------------------)

[[![Knownsec Blockchain
Lab](https://miro.medium.com/fit/c/40/40/1*KpGO_rBfzpfEn1vuPqgxoA.png)](/@Knownsec_Blockchain_Lab?source=post_internal_links
---------1----------------------------)

[Knownsec Blockchain Lab

](/@Knownsec_Blockchain_Lab?source=post_internal_links---------
1----------------------------)

## Knowsec Blockchain Lab | “JEPG” to “TXT”, a magic Loot

![](https://miro.medium.com/focal/112/112/50/50/1*eHjk7icXTag19Znf4qgwQg.png)](/@Knownsec_Blockchain_Lab/jepg-
to-txt-a-magic-loot-35bedbe88e2a?source=post_internal_links---------
1----------------------------)

[[![Aviv
Zohar](https://miro.medium.com/fit/c/40/40/1*Fjdz8TvS7com8QFz8OxCnQ.jpeg)](/@avivzohar?source=post_internal_links
---------2----------------------------)

[Aviv Zohar

](/@avivzohar?source=post_internal_links---------
2----------------------------)

in

[Blockchains @ HUJI

](https://medium.com/blockchains-huji?source=post_internal_links---------
2----------------------------)

## Rethinking Bitcoin’s Fee Market

![](https://miro.medium.com/focal/112/112/50/50/0*tG88y9xrci6Asaf7.jpg)](/blockchains-
huji/rethinking-bitcoins-fee-market-ea9319e4ea57?source=post_internal_links
---------2----------------------------)

[[![Best
John](https://miro.medium.com/fit/c/40/40/0*pDnZZCTJmMWJeZ4j)](/@timesnewswire?source=post_internal_links
---------3----------------------------)

[Best John

](/@timesnewswire?source=post_internal_links---------
3----------------------------)

## STRATOS, The Next Generation of Decentralized Data Mesh , to List on
BitMart Exchange

![](https://miro.medium.com/focal/112/112/50/50/0*3kuBPDxH0xK5k2PZ.png)](/@timesnewswire/stratos-
the-next-generation-of-decentralized-data-mesh-to-list-on-bitmart-
exchange-7024ec780270?source=post_internal_links---------
3----------------------------)

[[![Elementos](https://miro.medium.com/fit/c/40/40/1*sBv_XcO-
ODXWxUEExhTc-g.jpeg)](/@elementos?source=post_internal_links---------
4----------------------------)

[Elementos

](/@elementos?source=post_internal_links---------
4----------------------------)

## Fight The Nature Or Face Them All

![](https://miro.medium.com/focal/112/112/50/50/1*Ge-3lxDMg-
JyPJoqorktxA.jpeg)](/@elementos/fight-the-nature-or-face-them-
all-1eb5c25154b2?source=post_internal_links---------
4----------------------------)

[[![GEMMA](https://miro.medium.com/fit/c/40/40/1*im2XLelUk1uHdGTzk4-KnA.jpeg)](/@gxtmanager?source=post_internal_links
---------5----------------------------)

[GEMMA

](/@gxtmanager?source=post_internal_links---------
5----------------------------)

## Trade GXT Token on PancakeSwap, the top Binance Dapps by transaction volume
last week

![](https://miro.medium.com/focal/112/112/50/50/1*dCkTmL-U87Q_Z2q_uEz-
Bw.png)](/@gxtmanager/trade-gxt-token-on-pancakeswap-the-top-binance-dapps-by-
transaction-volume-last-week-eccd01f578bd?source=post_internal_links---------
5----------------------------)

[[![Bitcoin
Support](https://miro.medium.com/fit/c/40/40/1*UQ5KcTYk3yWq2KRK9BE48Q.png)](/@bitcoinguidance?source=post_internal_links
---------6----------------------------)

[Bitcoin Support

](/@bitcoinguidance?source=post_internal_links---------
6----------------------------)

in

[Coinmonks

](https://medium.com/coinmonks?source=post_internal_links---------
6----------------------------)

## Polkadot-powered Start-ups Triggers Latest Developments in interoperability

![Polkadot-powered Start-ups Triggers Latest Developments in
interoperability](https://miro.medium.com/focal/112/112/50/50/0*fcPSPcs9ucmURTXl.png)](/coinmonks/polkadot-
powered-start-ups-triggers-latest-developments-in-
interoperability-d80e2a54d75e?source=post_internal_links---------
6----------------------------)

[[![Quoth](https://miro.medium.com/fit/c/40/40/1*nMuBbUBxlUX5PMEYLqz0bg.png)](/@quothinc?source=post_internal_links
---------7----------------------------)

[Quoth

](/@quothinc?source=post_internal_links---------7----------------------------)

## NFTs Have Changed Artists. Have They Changed Art?

![](https://miro.medium.com/focal/112/112/50/50/1*nUZjZHoDAS1ikNOPDPXSvg.png)](/@quothinc/nfts-
have-changed-artists-have-they-changed-
art-10fc1931033?source=post_internal_links---------
7----------------------------)

[](/?source=post_page-----60d114e0172c--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
60d114e0172c--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
60d114e0172c--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
60d114e0172c--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
60d114e0172c--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----60d114e0172c--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----60d114e0172c--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fset-
protocol%2Fintroducing-yield-farming-strategies-on-
tokensets-60d114e0172c&source=post_page--------------------------
nav_reg-----------)

[![Anthony
Sassano](https://miro.medium.com/fit/c/176/176/1*jdMf10Tdlr17rBVVQVyUbg.png)](/@AnthonySassano)

[

## Anthony Sassano

](/@AnthonySassano)

1.6K Followers

Marketing at <https://www.setprotocol.com/> | Co-Founder of
<https://ethhub.io> & Co-host of the Into the Ether podcast | Founder
<https://thedailygwei.substack.co>

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Fc07a50d767be&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fset-
protocol%2Fintroducing-yield-farming-strategies-on-
tokensets-60d114e0172c&newsletterV3=473a5c521558&newsletterV3Id=c07a50d767be&user=Anthony+Sassano&userId=473a5c521558&source=--------------------------subscribe_user-----------)

## More from Medium

[[![EverythingWeb3](https://miro.medium.com/fit/c/40/40/1*YqHxHNRrIREkRO1ib87nQA.jpeg)](/@everythinngweb3?source=read_next_recirc
---------0---------------------b5dc545e_e5e2_4ed1_8176_a53332b7b4c1-------)

[EverythingWeb3

](/@everythinngweb3?source=read_next_recirc---------0---------------------
b5dc545e_e5e2_4ed1_8176_a53332b7b4c1-------)

in

[Coinmonks

](https://medium.com/coinmonks?source=read_next_recirc---------0
---------------------b5dc545e_e5e2_4ed1_8176_a53332b7b4c1-------)

## How to earn 20% APY on stablecoins

![](https://miro.medium.com/focal/112/112/50/50/1*jDVdNfCIutFgyBTmj85iWA.png)](/coinmonks/how-
to-earn-20-apy-on-stablecoins-d2b2fbde4f4c?source=read_next_recirc---------0
---------------------b5dc545e_e5e2_4ed1_8176_a53332b7b4c1-------)

[[![J. Mason Bump](https://miro.medium.com/fit/c/40/40/1*K3D8sPX-
GBg3wNtnc31VdA.jpeg)](/@jmasonbump?source=read_next_recirc---------1
---------------------b5dc545e_e5e2_4ed1_8176_a53332b7b4c1-------)

[J. Mason Bump

](/@jmasonbump?source=read_next_recirc---------1---------------------
b5dc545e_e5e2_4ed1_8176_a53332b7b4c1-------)

## The World of Terra: Staking, UST, and Native Projects

![](https://miro.medium.com/focal/112/112/50/50/0*mf8etv0bIm6HgYcp.png)](/@jmasonbump/the-
world-of-terra-staking-ust-and-native-
projects-9077df601f8b?source=read_next_recirc---------1---------------------
b5dc545e_e5e2_4ed1_8176_a53332b7b4c1-------)

[[![SCIFI Finance](https://miro.medium.com/fit/c/40/40/1*SasfEmLqFJCBC_I1Wz-
gIg.png)](/@scifinance?source=read_next_recirc---------2---------------------
b5dc545e_e5e2_4ed1_8176_a53332b7b4c1-------)

[SCIFI Finance

](/@scifinance?source=read_next_recirc---------2---------------------
b5dc545e_e5e2_4ed1_8176_a53332b7b4c1-------)

## SCIFI Index Report — March 2022

![](https://miro.medium.com/focal/112/112/50/50/1*e7lD7wlIDe1QE5aWvtWBHQ.jpeg)](/@scifinance/scifi-
index-report-march-2022-70f3d4310e58?source=read_next_recirc---------2
---------------------b5dc545e_e5e2_4ed1_8176_a53332b7b4c1-------)

[[![AlfaDAO](https://miro.medium.com/fit/c/40/40/1*zODTdlgxTWQDk_7bu5f9cw.jpeg)](/@AlfaDAO_money?source=read_next_recirc
---------3---------------------b5dc545e_e5e2_4ed1_8176_a53332b7b4c1-------)

[AlfaDAO

](/@AlfaDAO_money?source=read_next_recirc---------3---------------------
b5dc545e_e5e2_4ed1_8176_a53332b7b4c1-------)

## Defi Economics

![](https://miro.medium.com/focal/112/112/50/50/1*vZqwerrrno0u0gm6qxiZQg.jpeg)](/@AlfaDAO_money/defi-
economics-5e388b253590?source=read_next_recirc---------3---------------------
b5dc545e_e5e2_4ed1_8176_a53332b7b4c1-------)

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

