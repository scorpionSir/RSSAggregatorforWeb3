[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/8aec1a6f7e7b&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![ChainSecurity](https://miro.medium.com/fit/c/64/64/1*DQeE6Ua45H5MtGGv6WFVuA.png)](https://medium.com/chainsecurity?source=post_page
-----8aec1a6f7e7b--------------------------------)

Published in

[ChainSecurity

](https://medium.com/chainsecurity?source=post_page-----
8aec1a6f7e7b--------------------------------)

[![ChainSecurity](https://miro.medium.com/fit/c/96/96/2*IYEDevVjlqHJSXRJhxagdA.png)](/@chain_security?source=post_page
-----8aec1a6f7e7b--------------------------------)

[ChainSecurity](/@chain_security?source=post_page-----
8aec1a6f7e7b--------------------------------)

Follow

Jul 19, 2019

·

7 min read

# The Dispatcher — First Line Of Defense In Any EOS Smart Contract

## Back in September 2018, an attacker managed to steal US$200 000 worth of
EOS from the EOSBet contract. The attacker exploited a serious bug in a
designated entry function of the contract, called the dispatcher. Moreover,
the introduced fix only partially closed the security issue, leaving the
contract vulnerable. This incident highlights the need for education about
security critical details of the dispatcher function.

![](https://miro.medium.com/max/1400/1*AkQGRYc-5ECDi33qLYwJcg.png)

This blog post aims to help developers write secure dispatchers in their EOS
contracts and avoid such bugs, which put the funds of the smart contract at
risk.

# The Dispatcher Function

A dispatcher is the function that is executed first whenever the code of the
account is invoked. This function receives an action identifying the function
to be invoked, and it is the dispatcher’s responsibility to invoke the
intended function. Every EOS smart contract must provide an `apply` handler
that defines the behavior of the dispatcher function.

To implement the dispatcher, the contract development toolkit (eosio.cdt)
allows developers to generate the dispatcher automatically by executing the
macros inside a contract. All functions which are marked by
`[[eosio::action]]` will be callable by actions. However, for some projects
this is insufficient and the developer may need to customize the dispatcher,
e.g., to accept certain actions only upon a token transfer. While basic helper
functions are available, these only cover the invocation of the functions, not
the control logic enforcing the condition of when they may be invoked.

# Recap — EOS’ communication model

Before we dive in, we need to get up to speed with EOS’ communication model.

To execute a smart contract, actions need to be pushed to its account. During
the execution of a smart contract it may notify other accounts about this
action. Notifying another account is done by calling `require_recipient()`.
What happens is that after the execution of this smart contract's code, the
dispatcher of the notified account is invoked with a copy of this action.

Let us look at a simple dispatcher:

We see the implementation of `apply()`: If `code` is equal to `receiver`, the
passed action is called, the helper function `EOSIO_DISPATCH_HELPER` does this
for us. But what are these function parameters passed to `apply()` exactly? To
write secure dispatchers, it is vital to fully understand these parameters.

The following parameters are passed to the `apply` function: `uint64_t
receiver`, `uint64_t code` and `uint64_t action`. Let us have a look at the
EOS source code!

This is the function that invokes the dispatcher of the smart contract by
calling the `apply()` function and passing the following parameters:

  * `receiver` is `context.get_receiver()`, the account currently executing code
  * `code` is `context.get_action().account`, the account the action was sent to
  * `action` is `context.get_action().name`, the name of the action

But what exactly does that mean? It is important to understand the difference
between `code` and `receiver`. In short, `code` is always the first receiver
of the action, while `receiver` is the account currently executing the action.

# `code` and `receiver` \- aren't they the same?

Not necessarily! They may be equal, e.g. when an action is sent to an account
(= code) and this account’s code is currently executing (= receiver). In EOS’
communication model, contracts executing code can notify other accounts about
this action by calling `require_recipient()`. This invokes the code of the
recipient's account (= receiver changes) but the code stays constant, thus
`code` and `receiver` differ.

By using `code == receiver` the dispatcher knows that this contract has been
called by the action directly, while in the case of `code != receiver` the
action was originally destined for another account, but this account has been
notified about it.

# Most prominent use case — reacting to a token transfer

If your contract receives a transfer of EOS tokens for example, you may want
to execute a certain action. This functionality allows you to do so because
the `eosio.token` contract notifies the sender and the receiver about a
successful token transfer and gives them the opportunity to execute code. Note
that the transfer action, to transfer x funds from account a to b, was sent to
the `eosio.token` account, so `code` is equal to `eosio.token`. After a
successful transfer, the receiver is informed about it and its dispatcher is
invoked. Here `code` is `eosio.token` and `receiver` is `b`, because `b` is
currently executing.

Let us stop here for a moment. Assume we are within our dispatcher and `code`
is equal to `eosio.token` ( `receiver` is equal to our account), what exactly
do we know at this point? Did we just receive a token transfer?

Not necessarily! At this point we just know that the original action was sent
to the `eosio.token` contract (hence code is `eosio.token`), but we have
absolutely no other information about the actual details of the token
transfer! Most importantly we need to make sure that the transfer was to our
account (ensuring parameter `to` of the action is our account) and that the
amount is what we expect. If we don't do this (most importantly checking the
`to` field), attacks of the following kind are possible:

![](https://miro.medium.com/max/1400/0*hhoLughhX0SOFGBV.png)

A simple example: we have a trading contract and transfer some GoldTokens if
we received some EOS tokens. Our contract, however, only checks if `code ==
eosio.token` and the amount of tokens, it does not check if it was actually
the receiver of these tokens. Alice notices this and decides to get some
GoldTokens without actually transfering EOS to our contract.

All Alice needs is an account where she can deploy a simple contract. The only
thing this contract has to do is to implement a transfer action and inform our
trading contract about the transfer action. The attack works as follows:

  1. Alice sends a transaction to the `eosio.token` contract to transfer EOS from her account to the attacking contract she controls (where later she can reclaim these tokens).
  2. Upon executing the action, the `eosio.token` contract notifies the `sender` and the `receiver` about the action.
  3. The `receiver`, Alice's attacking contract, in turn just notifies our trading contract.
  4. Our trading contract gets a copy of the action, where `code` is equal to `eosio.token`.

Without doing any further checks our contract mistakenly thinks it just
received some EOS tokens and transfers GoldTokens to Alice.

This example highlights the importance of checking everything properly.

# How to ensure your contract actually received an (EOS-) token transfer

The following considerations are valid for the `eosio.token` contract, but
likely also applicable to other token contracts. The first important thing to
note is that you have to fully trust the token contract, especially that it
only notifies you about the transfer if the transfer actually happened and
succeeded. One of the token contracts you can trust to only notify you in case
of a successful transfer is the system's `eosid.token` contract.

First, a mandatory requirement is that `code` is equal to `eosio.token`. Why?
The `eosio.token` contract allows token transfers only when the action to
transfer is directly sent to its account. When the `eosio.token` contract
notifies you about a token transfer, your dispatcher gets a copy of the
action.

The name of the passed action must be equal to `transfer`. Furthermore, all
parameters, especially the field `to` and the quantity, need to be checked. A
check `if(to != self) return;` is often added at a later stage in the contract
to enforce this. Why is this done outside of the dispatcher? Inside the
dispatcher it is hard to access the fields of the function's argument, once
inside the function these parameters are easily accessible.

If you follow these guidelines you can be sure that your contract actually
received an EOS token transfer.

Ensure that you only invoke functions of your smart contract which depend on a
token transfer after these checks successfully passed. Please ensure that your
custom dispatcher does not allow to bypass these checks on invoking these
functions! Such mishaps happened in the past, let us walk through one well-
known example.

# What went wrong for EOSBet?

EOSBet allows you to bet EOS tokens. You transfer EOS tokens to their contract
which places your bet. Later, if you win, you can claim and withdraw your
prize. To state the obvious: one should only be able to place a bet after
having transferred EOS. What went wrong in the first version of their
dispatcher?

slightly simplified for readability

This dispatcher allows any action (if it exists) sent to the contract directly
to execute, including the `transfer` function which should only be invoked
after an actual transfer of EOS tokens to this contract. Thus an attacker was
able to place bets for free and cash out the winnings. All US$200 000 worth of
funds were drained from the contract.

EOSBet went ahead and fixed their code after the attack. The fixed code can be
found in their [Gitlab
repository](https://gitlab.com/EOSBetCasino/eosbetdice_public/blob/master/EOSBetDice.cpp).

slightly simplified for readability

The fix introduced checks verifying that the original recipient of the action
is `eosio.token` in case of a call to the transfer action. As described above,
this is insufficient to ensure that the EOSBet contract really received EOS
tokens. While this fix now ensures that the action `transfer` was directed to
the `eosio.token` contract, no checks have been added to the `transfer()`
function, which handles this action, to ensure that the `transfer.to` receiver
of the EOS tokens was the EOSBet smart contract. Please note that EOSBet is
aware of this and all their deployed contracts are not subject to this issue
anymore.

This blog post focuses on the most common use case, which is reacting to a
token transfer. Please note that the same or similar problems exist during
other interactions of smart contracts in EOS.

We hope this article raised your awareness, improved your understanding of the
dispatcher of EOS contracts and will help you write secure smart contracts!

# Need a security audit of your EOS contracts?

For an expert security review of your EOS contracts, reach out to us at
**contact@chainsecurity.com**.

 _Originally published at_[
_https://chainsecurity.com_](https://chainsecurity.com/the-dispatcher-first-
line-of-defense-in-any-eos-smart-contract/) _._

\--

\--

\--

## [More from ChainSecurity](/chainsecurity?source=post_page-----
8aec1a6f7e7b--------------------------------)

From the world of secure smart contracts

[Read more from ChainSecurity](/chainsecurity?source=post_page-----
8aec1a6f7e7b--------------------------------)

## Recommended from Medium

[[![Moby](https://miro.medium.com/fit/c/40/40/2*FhH3D58QJHE785Wo5AlNOQ.jpeg)](/@kyle8?source=post_internal_links
---------0----------------------------)

[Moby

](/@kyle8?source=post_internal_links---------0----------------------------)

## Daily analysis of cryptocurrencies 20191121(Market index 30 — Fear state)

![](https://miro.medium.com/focal/112/112/50/50/1*uf-
YkmKrzMb-4l1FddJhDg.jpeg)](/@kyle8/daily-analysis-of-
cryptocurrencies-20191121-market-index-30-fear-
state-2e2a02c4f558?source=post_internal_links---------
0----------------------------)

[[![Unmarshal](https://miro.medium.com/fit/c/40/40/1*yPTij_a2AGnjp_62oVQM3w.png)](/@unmarshal-
io?source=post_internal_links---------1----------------------------)

[Unmarshal

](/@unmarshal-io?source=post_internal_links---------
1----------------------------)

in

[unmarshal

](https://medium.com/unmarshal-io?source=post_internal_links---------
1----------------------------)

## Unmarshal forms a Strategic Partnership with Gourmet Galaxy to build a
Premium Yield Farming…

![](https://miro.medium.com/focal/112/112/50/50/0*SF9I5vY3yN0VDRrB)](/unmarshal-
io/unmarshal-forms-a-strategic-partnership-with-gourmet-galaxy-to-build-a-
premium-yield-farming-e7fdc6165b1b?source=post_internal_links---------
1----------------------------)

[[![Geco.one](https://miro.medium.com/fit/c/40/40/1*5KV9F0qsC0pg8C6ojAlTIw.png)](/@geco-
one?source=post_internal_links---------2----------------------------)

[Geco.one

](/@geco-one?source=post_internal_links---------2----------------------------)

## Weekly Crypto Market Analysis with Geco.one — 31.01.2022

![](https://miro.medium.com/focal/112/112/50/50/1*npW2OeCZpsJKNzMK6Z8XyQ.png)](/@geco-
one/weekly-crypto-market-analysis-with-geco-
one-31-01-2022-9de98df54464?source=post_internal_links---------
2----------------------------)

[[![Coinsandcoins](https://miro.medium.com/fit/c/40/40/1*THj766vMNwyH8lx1bqKWkQ.jpeg)](/@coinsandcoins1?source=post_internal_links
---------3----------------------------)

[Coinsandcoins

](/@coinsandcoins1?source=post_internal_links---------
3----------------------------)

## When and why did the word ‘altcoin’ lose its relevance?

](/@coinsandcoins1/when-and-why-did-the-word-altcoin-lose-its-
relevance-1b2079fa5a05?source=post_internal_links---------
3----------------------------)

[[![Seb \[ACOL\]
Pool](https://miro.medium.com/fit/c/40/40/1*9fV4RB4H3AjeDq1x_NUK_A.png)](/@seb-
acol-pool?source=post_internal_links---------4----------------------------)

[Seb [ACOL] Pool

](/@seb-acol-pool?source=post_internal_links---------
4----------------------------)

## Cardano NFTs, a simple howto,

![](https://miro.medium.com/freeze/focal/112/112/50/50/1*wsgF22S1uKKjpyKzRsiz-w.gif)](/@seb-
acol-pool/cardano-nfts-a-simple-howto-34aca62c948e?source=post_internal_links
---------4----------------------------)

[[![Gary Leland](https://miro.medium.com/fit/c/40/40/2*IdPGCAsZu_1iXwk-
TbdgBQ.jpeg)](/@garyleland?source=post_internal_links---------
5----------------------------)

[Gary Leland

](/@garyleland?source=post_internal_links---------
5----------------------------)

## ⏰ 4 MINUTE CRYPTO SHOW #546 Bitcoin Is Not a Toy Anymore

![](https://miro.medium.com/focal/112/112/50/50/1*hpqtdzKUF-
MW0H1a7y04sQ.jpeg)](/@garyleland/4-minute-crypto-show-546-bitcoin-is-not-a-
toy-anymore-4f016bb0b325?source=post_internal_links---------
5----------------------------)

[[![Jonathan
Poland](https://miro.medium.com/fit/c/40/40/1*5G1jk0Ek2VorTxBaEQwqig.jpeg)](/@mrpoland?source=post_internal_links
---------6----------------------------)

[Jonathan Poland

](/@mrpoland?source=post_internal_links---------6----------------------------)

## Trading Squid Game

](/@mrpoland/trading-squid-game-621979190094?source=post_internal_links
---------6----------------------------)

[[![DATA](https://miro.medium.com/fit/c/40/40/0*atkm0-f9Q06u6495.jpg)](/@blockchaindata?source=post_internal_links
---------7----------------------------)

[DATA

](/@blockchaindata?source=post_internal_links---------
7----------------------------)

## DATA(DTA) Project Summary: May 30th～June 12th

![](https://miro.medium.com/focal/112/112/50/50/1*d2E0FCnyW7cxB7msADQ5lw.jpeg)](/@blockchaindata/data-
dta-project-summary-may-30th-june-12th-9aa931a721af?source=post_internal_links
---------7----------------------------)

[](/?source=post_page-----8aec1a6f7e7b--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
8aec1a6f7e7b--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
8aec1a6f7e7b--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
8aec1a6f7e7b--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
8aec1a6f7e7b--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----8aec1a6f7e7b--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----8aec1a6f7e7b--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fchainsecurity%2Fhttps-
medium-com-chain-security-the-dispatcher-first-line-of-
defense-8aec1a6f7e7b&source=post_page--------------------------
nav_reg-----------)

[![ChainSecurity](https://miro.medium.com/fit/c/176/176/2*IYEDevVjlqHJSXRJhxagdA.png)](/@chain_security)

[

## ChainSecurity

](/@chain_security)

431 Followers

ChainSecurity provides security audits and conducts research and development
for blockchain platforms.

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Ff9fb56630e26&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fchainsecurity%2Fhttps-
medium-com-chain-security-the-dispatcher-first-line-of-
defense-8aec1a6f7e7b&newsletterV3=8b14ef67c636&newsletterV3Id=f9fb56630e26&user=ChainSecurity&userId=8b14ef67c636&source=--------------------------subscribe_user-----------)

## More from Medium

[[![TGM](https://miro.medium.com/fit/c/40/40/1*uqvobtMek_8PPq9H5MjLpg.png)](/@tgmeyer?source=read_next_recirc
---------0---------------------db099bfe_2f12_4ebf_b57a_2594f3220c96-------)

[TGM

](/@tgmeyer?source=read_next_recirc---------0---------------------
db099bfe_2f12_4ebf_b57a_2594f3220c96-------)

in

[Coinmonks

](https://medium.com/coinmonks?source=read_next_recirc---------0
---------------------db099bfe_2f12_4ebf_b57a_2594f3220c96-------)

## A Data Analyst’s Perspective on the fxhash Beta

![](https://miro.medium.com/focal/112/112/50/50/1*hDZbmVnrQG68Nu9PnHQ4Rw.jpeg)](/coinmonks/a-data-
analysts-perspective-on-the-fxhash-beta-52eb5c79e466?source=read_next_recirc
---------0---------------------db099bfe_2f12_4ebf_b57a_2594f3220c96-------)

[[![Balancer
Grants](https://miro.medium.com/fit/c/40/40/1*7Q30743IqU9w9NERZNNeDg.png)](/@BalancerGrants?source=read_next_recirc
---------1---------------------db099bfe_2f12_4ebf_b57a_2594f3220c96-------)

[Balancer Grants

](/@BalancerGrants?source=read_next_recirc---------1---------------------
db099bfe_2f12_4ebf_b57a_2594f3220c96-------)

## Balancer Grant Wave#4 has started!

![](https://miro.medium.com/focal/112/112/50/50/0*iNqYiM5__JI8GFpd.png)](/@BalancerGrants/balancer-
grant-wave-4-has-started-7fce8d59bbd2?source=read_next_recirc---------1
---------------------db099bfe_2f12_4ebf_b57a_2594f3220c96-------)

[[![Denver](https://miro.medium.com/fit/c/40/40/1*yXnkQdN5FAOTeFKPV0i0FQ.jpeg)](/@denverb?source=read_next_recirc
---------2---------------------db099bfe_2f12_4ebf_b57a_2594f3220c96-------)

[Denver

](/@denverb?source=read_next_recirc---------2---------------------
db099bfe_2f12_4ebf_b57a_2594f3220c96-------)

in

[Rubicon

](https://medium.com/rubicon-finance?source=read_next_recirc---------2
---------------------db099bfe_2f12_4ebf_b57a_2594f3220c96-------)

## Rubicon APIs Powered by The Graph

![](https://miro.medium.com/focal/112/112/50/50/1*lQ1jP8g9mAS0qx0BO1udtA.png)](/rubicon-
finance/rubicon-apis-powered-by-the-graph-93f3ef9b2332?source=read_next_recirc
---------2---------------------db099bfe_2f12_4ebf_b57a_2594f3220c96-------)

[[![Anjali
Young](https://miro.medium.com/fit/c/40/40/1*m7YUWoNlHFMo5LuqLF32HA.png)](/@anjaliyoung?source=read_next_recirc
---------3---------------------db099bfe_2f12_4ebf_b57a_2594f3220c96-------)

[Anjali Young

](/@anjaliyoung?source=read_next_recirc---------3---------------------
db099bfe_2f12_4ebf_b57a_2594f3220c96-------)

## The Collab.Land Command Center is Here!

![](https://miro.medium.com/focal/112/112/50/50/1*O_7sONgV2mABzFmGpruirw.jpeg)](/@anjaliyoung/the-
collab-land-command-center-is-here-6848b4c6ab25?source=read_next_recirc
---------3---------------------db099bfe_2f12_4ebf_b57a_2594f3220c96-------)

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

