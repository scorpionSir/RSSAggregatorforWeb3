  * [Home](/)
  * [Contact](/contact)
  * [Services](/services)
  * [Projects](/projects)
  * [Community](/community)
  * [Blog](/blog)

Menu

#  [![ScopeLift](//images.squarespace-
cdn.com/content/v1/54b81e72e4b0fee4b01a42e9/1581018368646-GMT0JDHOVLSGDECYFQVQ/SCOPELIFT-
long-cropped.png?format=1500w)](/)

Street Address

Philadelphia, PA

Phone Number

Your Custom Text Here

# [![ScopeLift](//images.squarespace-
cdn.com/content/v1/54b81e72e4b0fee4b01a42e9/1581018368646-GMT0JDHOVLSGDECYFQVQ/SCOPELIFT-
long-cropped.png?format=1500w)](/)

  * [Home](/)
  * [Contact](/contact)
  * [Services](/services)
  * [Projects](/projects)
  * [Community](/community)
  * [Blog](/blog)

#  [Introducing Umbra – Privacy Preserving Stealth Payments On The Ethereum
Blockchain](/blog/introducing-umbra)

May 27, 2020 [Ben DiFrancesco](/blog?author=54b81e71e4b06e38ad58f2f2)

On March 31st, 2020, Vitalik Buterin tweeted about the need for a stealth
address scheme in the Ethereum ecosystem. **Less than two months later, we’re
excited to announce Umbra, a protocol for simple stealth payments on
Ethereum.**



> Next step in improving ethereum's privacy (in addition to ongoing
> improvements to <https://t.co/f8JT3wFmD4> and the like): some clean easy-to-
> use stealth-address-like scheme to send coins to an ENS name without
> publishing to the world that they got coins.
>
> — vitalik.eth (@VitalikButerin) [April 1,
> 2020](https://twitter.com/VitalikButerin/status/1245149156043350016?ref_src=twsrc%5Etfw)



## HackMoney 2020

Umbra was developed by [Matt Solomon ](https://twitter.com/msolomon44)and [Ben
DiFrancesco](https://twitter.com/bendifrancesco) for the [HackMoney
2020](https://hackathon.money/) virtual hackathon. The MVP was built in 23
days and is available on the Ropsten Testnet. You can play with it by visiting
<https://ropsten.umbra.cash>. _(Note: the interface does not render correctly
in Firefox at this time. A fix is coming soon!)_

To learn more, and to see Umbra in action, you can also check out our
hackathon submission video.

## How Does Umbra Work?

As a protocol, Umbra defines a simple set of standards, coupled with a
singleton smart contract instance, to enable stealth addresses on Ethereum.

With a stealth address, a payer can send Ether or ERC20 tokens to an address
controlled by the receiver, but no one except the two parties know who that
receiver is.



View fullsize

![Image via @IoTeX hackernoon.](https://images.squarespace-
cdn.com/content/v1/54b81e72e4b0fee4b01a42e9/1590529474706-KFRWTJ0KT5A715P1HT9H/stealth-
addrs+%281%29.png)

Image via [@IoTeX hackernoon](https://hackernoon.com/blockchain-privacy-
enhancing-technology-series-stealth-address-i-c8a3eb4e4e43).



On chain, the transaction looks like a simple transfer to an otherwise unused
address on the Ethereum network.



View fullsize

![View of an Umbra ETH send &amp; withdraw on Etherscan. On chain, stealth
address looks like a normal EOA.](https://images.squarespace-
cdn.com/content/v1/54b81e72e4b0fee4b01a42e9/1590594949741-OWGCPVNE386RSRCPGIHO/etherscan-
umbra.jpg)

View of an Umbra ETH send & withdraw on
[Etherscan](https://ropsten.etherscan.io/address/0xa1f0c5eaca7da7ae03f95700db2b330a13bc5a99).
On chain, stealth address looks like a normal EOA.



Off chain, the sender has used a public key published by the receiver using
ENS to generate the new address. By encrypting the data used to generate the
address, and announcing it via the Umbra smart contract, the sender can let
the receiver know they’ve sent them a payment to a new stealth address. Only
the receiver can generate the private key needed to withdraw the funds.



![The Umbra interface, available at
https://ropsten.umbra.cash](https://images.squarespace-
cdn.com/content/v1/54b81e72e4b0fee4b01a42e9/1590578143163-QVJ3WADVJJGBZHESLM7O/umbra-
interface.png)

The Umbra interface, available at <https://ropsten.umbra.cash>



By leveraging Gas Station Network and Uniswap, Umbra enables withdrawers to
pay for gas using the tokens they’ve received. This avoids the need to fund
stealth addresses with Ether before withdrawing.

To learn more about how Umbra works, checkout the information available on our
[GitHub repository](https://github.com/ScopeLift/umbra-protocol).

## What’s Next?

We plan on finalizing version one of the Umbra protocol and getting it to
mainnet soon. Our number one priority is security and safety of user funds,
which can’t be rushed.

If you’re interested in using Umbra, or integrating it into your DApp or
service, sign up below to be notified when Umbra goes live.



Sign up to be notified when Umbra launches.

Email Address

Notify Me

We won’t use your email for anything other than updates about Umbra’s launch.
We’ll never share it with third parties.

📮You’re all set! Thanks for signing up for updates about Umbra.



Tags [umbra](/blog/tag/umbra)

[<- An Update on Umbra's Funding and Future](/blog/umbra-update)[FakerDAO: An
Exploration Of MakerDAO’s Governance Incentives ->](/blog/fakerdao)

[ ](https://twitter.com/BenDiFrancesco) [ ](https://github.com/apbendi) [
](https://www.linkedin.com/pub/ben-difrancesco/9b/426/680)

© ScopeLift 2021

