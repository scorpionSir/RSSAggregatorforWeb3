[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/c89a874c5d09&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![ChainSecurity](https://miro.medium.com/fit/c/64/64/1*DQeE6Ua45H5MtGGv6WFVuA.png)](https://medium.com/chainsecurity?source=post_page
-----c89a874c5d09--------------------------------)

Published in

[ChainSecurity

](https://medium.com/chainsecurity?source=post_page-----
c89a874c5d09--------------------------------)

[![ChainSecurity](https://miro.medium.com/fit/c/96/96/2*IYEDevVjlqHJSXRJhxagdA.png)](/@chain_security?source=post_page
-----c89a874c5d09--------------------------------)

[ChainSecurity](/@chain_security?source=post_page-----
c89a874c5d09--------------------------------)

Follow

Dec 23, 2019

·

5 min read

# PolPatrol — Validator for Polkadot Runtimes

![](https://miro.medium.com/max/1400/1*EFjBWuYVLJaqqYpDz6TrLw.png)

ChainSecurity is happy to release PolPatrol, an **automated validator for
testing the stability and security of Polkadot relay chain runtimes with
respect to generic security and performance properties**. Since Polkadot’s
relay chain runtime lies at the core of the Polkadot network, the current
version of PolPatrol focuses on ensuring that relay chain runtimes are secure
and functionally correct.

Peter Czaban, Executive Director of Web3 Foundation, said:

> “Polkadot Runtimes make it easier than ever before to flexibly describe and
> deploy blockchain logic. To ensure that this richness of capabilities leads
> to secure developments, we are committed to funding tools which can support
> developers during their creation. We are excited to work with a leading
> blockchain security firm ChainSecurity to research and develop new
> approaches to automated blockchain logic analysis”.

Petar Tsankov, Chief Scientist of ChainSecurity, said:

> “We are dedicated to bringing to Polkadot’s developers and users practical
> and useful security tools that enable them to easily assess the safety and
> security of Polkadot. Starting with manual testing and random fuzzing of
> Polkadot Runtimes, we are looking forward to building further tools capable
> of deep security fuzzing and verification. We are grateful to Web3
> Foundation for their support in this project”.

# Who is PolPatrol for?

Two user groups will primarily use PolPatrol:

  * Developers of new relay chain runtimes who would like to test the correctness of their code.
  * DOT token holders who can vote on newly proposed relay chain runtimes and would like to check whether a proposed runtime is safe and secure.

For both user groups, PolPatrol automatically analyzes any given relay chain
Web assembly binary (or, a Wasm blob) and warns users upon violation of
important security and performance properties.

# How can I use PolPatrol?

The source code of PolPatrol is available at
<https://github.com/chainsecurity/polpatrol>.

To learn how to install PolPatrol and how to run it on a custom relay chain
runtime, please refer to the official documentation at
<https://polpatrol.ch/>.

# How does it work?

PolPatrol uses an instrumented Polkadot runtime environment to run the
provided relay chain runtime and log all calls that it makes to the
environment. In addition to the calls, it also monitors essential performance
metrics, such as execution time and memory usage. This enables PolPatrol to
check relevant trace and performance properties. PolPatrol aggregates the
collected runtime information to let developers draw conclusions on the
overall behavior of the runtime and compare different implementations.

# What properties does PolPatrol check?

The focus of PolPatrol is on performance and safety properties.

## Performance of runtime entries

PolPatrol collects statistics about all calls to runtime entries and reports
the total number of calls made while testing the run-time, the maximum
execution time (in seconds), the maximum memory usage (in MB), and the maximum
number of storage-related calls to the environment:

    
    
    ====================================================================  
    Entry Name            | # Calls | Max Time | Max Mem | Max #Storage  
    --------------------------------------------------------------------  
    initialize_block      |      31 |   0.0324 |  68.294 |         59  
    execute_block         |      31 |   0.9438 |  72.484 |        341  
    inherent_extrinsics   |      31 |   0.0404 |  68.290 |          1  
    apply_extrinsic       |     109 |   0.6399 |  71.959 |         79  
    finalize_block        |      31 |   0.3210 |  69.862 |        110  
    ====================================================================

For example, the above sample output identifies that the initialize_block
entry was called 31 times, each call took at most 0.0324 seconds and consumed
at most 68.294 MB of memory, making at most 59 storage-related calls. We note
that PolPatrol outputs additional metrics (not shown above), such as the mean
execution time and mean memory usage.

# Performance of extrinsics

PolPatrol also reports statistics about applied extrinsics, reporting the same
metrics as the ones reported for environment entries:

    
    
    ====================================================================  
    Entry Name               Max Time | Max Mem | Max Storage| Weight  
    --------------------------------------------------------------------  
    Balances::force_transf   0.031489 |  68.296 |         57 |  1000000  
    Balances::transfer       0.031372 |  68.296 |         66 |  1000000  
    Democracy::propose       0.028740 |  68.290 |         39 |  5000000  
    Council::execute         0.029009 |  68.290 |         47 |   100000  
    Slots::fix_deploy_data   0.028606 |  68.290 |         38 |   500000  
    Democracy::fast_track    0.028877 |  68.290 |         39 |   200000  
    ImOnline::heartbeat      0.026807 |  68.289 |         13 |    10000  
    Democracy::undelegate    0.029554 |  68.289 |         54 |   500000  
    Balances::set_balance    0.029181 |  68.290 |        102 |        0  
    Democracy::resign_proxy  0.028444 |  68.289 |         40 |   100000  
    Council::vote            0.030299 |  68.290 |        107 |   200000  
    Parachains::set_heads    0.028418 |  68.289 |         13 |  1000000  
    Democracy::set_proxy     0.028941 |  68.290 |         41 |   100000  
    Democracy::cancel_queu   0.028394 |  68.289 |         39 |    10000  
    Council::propose         0.029840 |  68.290 |         95 |  5000000  
    Democracy::external_pro  0.028710 |  68.290 |         39 |  5000000  
    Claims::claim            0.027391 |  68.289 |         11 |  1000000  
    Slots::new_auction       0.028643 |  68.290 |         56 |        0  
    Democracy::second        0.028793 |  68.289 |         40 |  5000000  
    Democracy::delegate      0.029207 |  68.290 |         52 |   500000  
    Democracy::vote          0.028790 |  68.289 |         40 |   200000  
    FinalityTracker::final   0.026426 |  68.289 |         13 |    10000  
    Democracy::cancel_refe   0.028563 |  68.289 |         39 |    10000  
    Democracy::remove_proxy  0.028664 |  68.290 |         41 |   100000  
    Council::set_members     0.029432 |  68.290 |         51 |        0  
    Democracy::emergency     0.028735 |  68.289 |         39 |   500000  
    Slots::elaborate_deploy  0.659817 |  71.959 |         51 |  5000000  
    Timestamp::set           0.028862 |  68.289 |         29 |    10000  
    Democracy::proxy_vote    0.028574 |  68.289 |         41 |   200000  
    Democracy::veto_external 0.028529 |  68.290 |         39 |   200000  
    Slots::bid               0.029268 |  68.289 |         57 |   500000  
    Democracy::external_prop 0.028528 |  68.290 |         39 |  5000000  
    ====================================================================

In addition to reporting the execution time, memory usage, and storage calls,
PolPatrol also reports the assigned weight of each extrinsic. This allows
developers and users to judge whether the weights are adequately defined based
on the actual performance of the extrinsic.

## Safety properties

Based on the performance information, PolPatrol checks several safety
properties, such as:

    
    
    ====================================================================  
    Maximum block execution time:   0.944 s   - OK  
    Maximum block memory:          72.484 MB  - OK  
    Maximum block length:           0.375 MB  - OK  
    ====================================================================

In particular, PolPatrol ensures that the maximum block execution time is
below 2 seconds, the maximum block memory is below 10,000 MB and the block
length does not exceed 10,000 MB (measured as bytes of a block, scale-
encoded). Further safety properties can be easily added.

# Acknowledgments

ChainSecurity would like to thank the Web3 Foundation for supporting the
research and development of PolPatrol with a research grant.

## About Polkadot

Polkadot is the first interoperability protocol that enables blockchain
networks to work together under the protection of shared security.

For more information on Polkadot, visit
[polkadot.network](https://polkadot.network).

## About Web3 Foundation

Established in Zug, Switzerland by Ethereum co-founder and Chief Technology
Officer Dr. Gavin Wood, Web3 Foundation funds research and development teams
building the stack of technologies behind the decentralized web.

For more information on Web3 Foundation, visit
[web3.foundation](https://web3.foundation).

## About ChainSecurity

ChainSecurity provides security services and develops custom security
solutions for blockchain projects.

Learn more about ChainSecurity at
[chainsecurity.com](https://chainsecurity.com).

 _Originally published at_[
_https://chainsecurity.com_](https://chainsecurity.com/polpatrol-validator-
for-polkadot-runtimes/) _._

\--

\--

\--

## [More from ChainSecurity](/chainsecurity?source=post_page-----
c89a874c5d09--------------------------------)

From the world of secure smart contracts

[Read more from ChainSecurity](/chainsecurity?source=post_page-----
c89a874c5d09--------------------------------)

## Recommended from Medium

[[![Pablo Penny](https://miro.medium.com/fit/c/40/40/1*1oll9Gp5v2shT-
WwzvCbGA.png)](/@pablopenny?source=post_internal_links---------
0----------------------------)

[Pablo Penny

](/@pablopenny?source=post_internal_links---------
0----------------------------)

## Using the Keyword Optimization Cycle to Increase App & Play Store
Visibility

![](https://miro.medium.com/focal/112/112/50/50/1*D6vzaVURaiSqw81_R-
aRqg.jpeg)](/@pablopenny/keyword-optimization-
cycle-5f47388c2b5?source=post_internal_links---------
0----------------------------)

[[![Yves
Callaert](https://miro.medium.com/fit/c/40/40/0*K5NA92Qqe3JSWqSU.)](/@yvescallaert?source=post_internal_links
---------1----------------------------)

[Yves Callaert

](/@yvescallaert?source=post_internal_links---------
1----------------------------)

## Azure Event Hubs: The good, the bad and the ugly

![](https://miro.medium.com/focal/112/112/50/50/1*v8CqRyFD8tHoM2UsZExtQg.png)](/@yvescallaert/azure-
event-hubs-the-good-the-bad-and-the-
ugly-5b1120b8b9c2?source=post_internal_links---------
1----------------------------)

[[![Dan Lines](https://miro.medium.com/fit/c/40/40/0*bUCuOK-
uCLPAs0eu.jpg)](/@danlines?source=post_internal_links---------
2----------------------------)

[Dan Lines

](/@danlines?source=post_internal_links---------2----------------------------)

in

[LinearB

](https://medium.com/linear-b?source=post_internal_links---------
2----------------------------)

## 5 Ways to Deliver and Accelerate Engineering Velocity

![](https://miro.medium.com/focal/112/112/50/50/0*zqpKe_GzSPPvw8Ee.png)](/linear-b/5-ways-
to-deliver-and-accelerate-engineering-
velocity-e8e6f4012373?source=post_internal_links---------
2----------------------------)

[[![DOLPHINS
FINANCE](https://miro.medium.com/fit/c/40/40/0*MlKyVe0VxsSbsAmc.jpg)](/@dolphinsfinance_78236?source=post_internal_links
---------3----------------------------)

[DOLPHINS FINANCE

](/@dolphinsfinance_78236?source=post_internal_links---------
3----------------------------)

## ✅ Recently our smartcontracts were audited by TechRate and no critical
flaws were found.

![](https://miro.medium.com/focal/112/112/50/50/1*hCtYmi28NoKyp6ltMbvaJA.jpeg)](/@dolphinsfinance_78236/recently-
our-smartcontracts-were-audited-by-techrate-and-no-critical-flaws-were-
found-588756077b0e?source=post_internal_links---------
3----------------------------)

[[![Raizel
Bernstein](https://miro.medium.com/fit/c/40/40/1*4RjkANaHzwrZEr3eFTV0-A.png)](/@raizelb?source=post_internal_links
---------4----------------------------)

[Raizel Bernstein

](/@raizelb?source=post_internal_links---------4----------------------------)

in

[Analytics Vidhya

](https://medium.com/analytics-vidhya?source=post_internal_links---------
4----------------------------)

## Lay the Foundation Before “Just Google It”

![](https://miro.medium.com/focal/112/112/50/50/1*07hdpfLDrYhj0FSN0Br-
dg.jpeg)](/analytics-vidhya/lay-the-foundation-before-just-google-
it-9f736b3ea30a?source=post_internal_links---------
4----------------------------)

[[![James
Liang](https://miro.medium.com/fit/c/40/40/0*takLw2DsOM0d7Jgv.)](/@lalalili?source=post_internal_links
---------5----------------------------)

[James Liang

](/@lalalili?source=post_internal_links---------5----------------------------)

## CertBot 我又來了

![](https://miro.medium.com/focal/112/112/50/50/1*JadgOwMlrTHts7pPx7JPuw.png)](/@lalalili/certbot-
我又來了-52c45ce8c2e5?source=post_internal_links---------
5----------------------------)

[[![Raman
Bhadauria](https://miro.medium.com/fit/c/40/40/1*DOZJOeWOLQEu694Kv9ROAg.jpeg)](/@257ramanrb?source=post_internal_links
---------6----------------------------)

[Raman Bhadauria

](/@257ramanrb?source=post_internal_links---------
6----------------------------)

## Introduction to GraphQL

![](https://miro.medium.com/focal/112/112/50/50/0*_6u-GumXiNP1KQDe.jpg)](/@257ramanrb/introduction-
to-graphql-c78969ff44be?source=post_internal_links---------
6----------------------------)

[[![Kendell
Patrice](https://miro.medium.com/fit/c/40/40/1*RFXmzhbsuzTj5NcmjuJEDQ.jpeg)](/@kendell.patrice?source=post_internal_links
---------7----------------------------)

[Kendell Patrice

](/@kendell.patrice?source=post_internal_links---------
7----------------------------)

## Flutter State Management by Example

![Image result for state management
flutter](https://miro.medium.com/focal/112/112/50/50/1*JVWWKVOoQ6ZmGFXWN7iRjA.png)](/@kendell.patrice/flutter-
state-management-by-example-236f24ac2deb?source=post_internal_links---------
7----------------------------)

[](/?source=post_page-----c89a874c5d09--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
c89a874c5d09--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
c89a874c5d09--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
c89a874c5d09--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
c89a874c5d09--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----c89a874c5d09--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----c89a874c5d09--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fchainsecurity%2Fpolpatrol-
validator-for-polkadot-runtimes-c89a874c5d09&source=post_page
--------------------------nav_reg-----------)

[![ChainSecurity](https://miro.medium.com/fit/c/176/176/2*IYEDevVjlqHJSXRJhxagdA.png)](/@chain_security)

[

## ChainSecurity

](/@chain_security)

431 Followers

ChainSecurity provides security audits and conducts research and development
for blockchain platforms.

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Ff9fb56630e26&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fchainsecurity%2Fpolpatrol-
validator-for-polkadot-
runtimes-c89a874c5d09&newsletterV3=8b14ef67c636&newsletterV3Id=f9fb56630e26&user=ChainSecurity&userId=8b14ef67c636&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Livetree](https://miro.medium.com/fit/c/40/40/1*xRu7010Dea45cs_H42JMaA.png)](/@livetree-
stories?source=read_next_recirc---------0---------------------
68644db8_1113_4410_9485_8603b3a263ed-------)

[Livetree

](/@livetree-stories?source=read_next_recirc---------0---------------------
68644db8_1113_4410_9485_8603b3a263ed-------)

in

[livetree_network

](https://medium.com/livetreehq?source=read_next_recirc---------0
---------------------68644db8_1113_4410_9485_8603b3a263ed-------)

## What is Blockchain and what do we use?

![](https://miro.medium.com/focal/112/112/50/50/1*lXXWLwwc8GsHanHcLCpXAw.png)](/livetreehq/what-
is-blockchain-and-what-do-we-use-c41f62ac566f?source=read_next_recirc---------
0---------------------68644db8_1113_4410_9485_8603b3a263ed-------)

[[![digi](https://miro.medium.com/fit/c/40/40/1*wipT_VD8UqmbQnv-
BQYSBA.jpeg)](/@igtigtt?source=read_next_recirc---------1---------------------
68644db8_1113_4410_9485_8603b3a263ed-------)

[digi

](/@igtigtt?source=read_next_recirc---------1---------------------
68644db8_1113_4410_9485_8603b3a263ed-------)

## Archway Effect

](/@igtigtt/archway-effect-c0e3744bbec9?source=read_next_recirc---------1
---------------------68644db8_1113_4410_9485_8603b3a263ed-------)

[[![Jay
Malaney](https://miro.medium.com/fit/c/40/40/1*D7hJ-9vLZkI8cI_qWlEy7A.jpeg)](/@jaymalaney10?source=read_next_recirc
---------2---------------------68644db8_1113_4410_9485_8603b3a263ed-------)

[Jay Malaney

](/@jaymalaney10?source=read_next_recirc---------2---------------------
68644db8_1113_4410_9485_8603b3a263ed-------)

in

[Coinmonks

](https://medium.com/coinmonks?source=read_next_recirc---------2
---------------------68644db8_1113_4410_9485_8603b3a263ed-------)

## The Graph (GRT)

![](https://miro.medium.com/focal/112/112/50/50/1*d8MhxUoRk_yukzSFki0scw.png)](/coinmonks/the-
graph-grt-9e224c8ed8d9?source=read_next_recirc---------2---------------------
68644db8_1113_4410_9485_8603b3a263ed-------)

[[![Glodao](https://miro.medium.com/fit/c/40/40/0*4PXnl2P66p6LjZBr)](/@glodao-
official?source=read_next_recirc---------3---------------------
68644db8_1113_4410_9485_8603b3a263ed-------)

[Glodao

](/@glodao-official?source=read_next_recirc---------3---------------------
68644db8_1113_4410_9485_8603b3a263ed-------)

## DAOs and Web3 Governance: The Promise, Implications and Challenges Ahead

![](https://miro.medium.com/focal/112/112/50/50/1*OBgh7TIk26xcRYQrYH3iEA.jpeg)](/@glodao-
official/daos-and-web3-governance-the-promise-implications-and-challenges-
ahead-fd938484ca7b?source=read_next_recirc---------3---------------------
68644db8_1113_4410_9485_8603b3a263ed-------)

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

