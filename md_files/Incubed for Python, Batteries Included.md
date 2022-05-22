[](https://medium.com/)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/63b79368d58e&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](https://medium.com/)

[Home](https://medium.com/)

[Notifications](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![slock.it Blog](https://miro.medium.com/fit/c/64/64/1*ESYB-
YgQa2FKWPo2ofqCiQ.png)](https://blog.slock.it/?source=post_page-----
63b79368d58e--------------------------------)

Published in

[slock.it Blog

](https://blog.slock.it/?source=post_page-----
63b79368d58e--------------------------------)

[![J. Paul R.
Depraz](https://miro.medium.com/fit/c/96/96/0*t6h22joY7Q7QOVfa.jpg)](https://medium.com/@deprazz?source=post_page
-----63b79368d58e--------------------------------)

[J. Paul R. Depraz](https://medium.com/@deprazz?source=post_page-----
63b79368d58e--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F26ff11bf9c6d&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fincubed-
for-python-batteries-
included-63b79368d58e&user=J.+Paul+R.+Depraz&userId=26ff11bf9c6d&source=post_page-26ff11bf9c6d
----63b79368d58e---------------------follow_byline-----------)

May 15, 2020

·

8 min read

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F63b79368d58e&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fincubed-
for-python-batteries-
included-63b79368d58e&source=--------------------------bookmark_header-----------)

[

Save

](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F63b79368d58e&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fincubed-
for-python-batteries-
included-63b79368d58e&source=--------------------------bookmark_header-----------)

# Incubed for Python, Batteries Included

 _Python gets the lightest blockchain client out there._

A comprehensive standard library powered Python’s “batteries included” motto
in the 90s; 10 years later, the scientific community project
[SciPy](https://www.scipy.org/) rose in popularity by hosting Pandas, Numpy
and other broadly adopted tools. More recently, AI and data mining demands
inspired the creation of [Jupyter](https://jupyter.org/), an interactive
notebook that combines SciPy with gorgeous graphics and simulations.

In the Ethereum ecosystem, the language is also well-regarded: used for the
[first](https://github.com/ethereum/pyethereum) reference-implementation of
its virtual machine, and now for its second, Trinity client for version
[2.0](https://github.com/ethereum/trinity) of the protocol. It inspired
[Vyper](https://github.com/vyperlang/vyper), a pythonic smart contract
language; it’s used in [Casper](https://github.com/ethereum/casper), the
proof-of-stake consensus algorithm; and continues to be
[Vitalik](https://medium.com/@VitalikButerin)’s weapon of choice.

>  **Python is the** **№1 Googled programming language,** according to
> [Github’s “PYPL PopularitY of Programming
> Language.”](http://pypl.github.io/PYPL.html) **** When all search engines
> are considered, it is in the **top three,** along with C and Java, in the
> [TIOBE](https://www.tiobe.com/tiobe-index/) index.

The [Incubed](/incubed-stable-release-c35b3a4ec10a) network is designed to
empower battery-powered devices, like smart phones and [IoT](/incubed-secure-
blockchain-access-for-iot-db4687b3dfa1) devices, to efficiently transact on-
chain as trustless as if operating a blockchain client onboard. It encourages
dApp developers to run the Incubed Server, become part of the network, and
contribute to the whole community that needs a stable blockchain API.

# Incubed is the first blockchain client of its kind, supporting the
decentralization of APIs by incentivizing the users to host them and help
provide the community with access to reliable infrastructure.

![](https://miro.medium.com/max/1400/1*sDeJoJ6ITYkP0FokG5SsMg.png)

Incubed adds a user maintained access layer for applications to send and
gather verifiable data from Ethereum based blockchain networks and will
provide access to other financial services in the future.

Participating in the network will not only guarantee extra security for
decentralized applications, but help a myriad of other companies, individuals,
devices, and systems to access verifiable blockchain data on demand.

The client is developed in C and ported to multiple platforms, including ARM
and operating systems like Linux, Windows, and MacOS. The shared libraries
contain an API for RPC that makes it easy for writing tools in higher-level
programming languages, as we did with Java, C#, Javascript, and Python.

> This means that with Python you can use Incubed on a Raspberry Pi the same
> way you would in a Windows machine — not a single additional line of code!

Well, I guess it became self-evident that we love both Python and Incubed, now
let’s see get down to business!

> For advanced Python and blockchain users,
> [ReadTheDocs](https://in3.readthedocs.io/en/develop/api-python.html) has the
> complete technical documentation of the tool.

Install Incubed for Python and run the Python interpreter:

system-wide:  
`pip3 install in3  
python3`

project-scope only:  
`virtualenv -p python3 venv  
source venv/bin/activate  
pip install in3  
python`

The library files are now installed, and the ominous `>>>` on the interpreter
is waiting for a command.

> Commands will be displayed as though they were written in the Python
> interpreter. Real scenarios would be wrapped in try-catch blocks, respect
> pep8 style guidelines, and so forth. We will keep it simple.

Next, import the Incubed library and initiate the client. It will load the
Incubed shared library for the host system and configure it to communicate
with the Ethereum main network.

    
    
    import in3  
    client = in3.Client()

No error messages means it supports the host system. The client has yet to
make a network request until now, however, there are some important things to
consider before we move on to executing more commands.

Every time a new instance of the client is created, it will check for a
previously cached index of network nodes to keep in memory. Nodes are
community maintained and can be in downtime, misconfigured, or off sync;
therefore, every client must administer its own list telling how much they are
inclined to ask for an individual node to attest blockchain data.

From time-to-time (and certainly the first time you ask for ‘live’ data from
the network), the client will request an updated list of nodes in the Incubed
registrar smart contract. This is the decentralized source-of-truth for who
can participate in the Incubed network. You can check the client’s known nodes
by executing `client.config()`or by requesting an updated node list with
`client.refresh_node_list()`.

Let’s continue to request the latest block and print it on the console.

    
    
    block: in3.eth.Block = client.eth.block_by_number('latest')  
    import json  
    print(json.dumps(block.to_dict(), indent=4, sort_keys=True))

An Ethereum block is beautifully printed with a long list of transaction
hashes on your terminal. If it fails the first time, worry not, simply try
again. The reason being, as the network gets larger and the client instance
continues to blacklist unresponsive nodes, it gets more stable — that is the
goal!

> We used a Python3 feature called `_annotation_` __ to inform the user and
> the IDE that the object type return is an Ethereum block. An advanced tool
> like PyCharm would already know the return type of this variable as it is
> already annotated in the function declaration.

All Ethereum API calls are available over `client.eth `for general network
data,`client.eth.account` for creating accounts and sending transactions, and
`client.eth.contract` for smart contract interactions.

Time to send our first transaction in the Görli Test Network:

    
    
    import in3  
    client = in3.Client('goerli')  
    sender = client.eth.account.create()  
    print(sender)

> Alternatively, use your own account (i.e.from Metamask) by pasting the
> private key in the `_secret_` field. Be sure it contains the `0x` prefix.
>
> ` _secret= '0xbeef'  
> sender=client.eth.account.recover_account(secret)_`

This first bit will create a new account locally. Copy the printed value and
get you some Test Eth funds from our [Görli Faucet](https://goerli-
faucet.slock.it/).

Now execute `print(client.eth.account.balance(str(sender)))` until the balance
is positive. We’ve provided you with test ETH to spend, let’s do it!

    
    
    receiver = "0x0b56Ae81586D2728Ceaf7C00A6020C5D63f02308"  
    tx = in3.eth.NewTransaction(to=receiver, value=1463926659)  
    tx_hash = client.eth.account.send_transaction(sender, tx)  
    print('https://goerli.etherscan.io/tx/{}'.format(tx_hash))

You’ll know the transaction was accepted by the network, including both
Incubed and Görli, if it printed the transaction link, but this doesn’t mean
that the funds left the account. We must wait for the transaction receipt that
confirms it was mined and tells us how much gas it spent, along with other
important details.

Follow the link, or repeatedly try getting the transaction receipt via
Incubed:

    
    
    receipt = client.eth.transaction_receipt(tx_hash)  
    print(json.dumps(receipt.to_dict(), indent=4, sort_keys=True))

> Görli is pretty fast, but Ethereum transactions can take several minutes to
> be mined, depending on how much additional gas is set as transaction fee.
> The `send_transaction` command sets it automatically for the user.

# That was your first Ethereum transaction over Incubed, or at least with
Python. Congratulations!

You’ve seen how creating a new account and casually sending funds is very fun.
Still, the _crème de la crème_ of blockchain are **smart contracts** and all
the possibilities it brings to financial services and internet
decentralization. To start, let’s take a loot at ENS.

ENS stands for the _Ethereum Name Service_ and is the community-driven version
of DNS, available in the Ethereum main network and some of the test chains.
The main registry smart contract resolves a domain name to its delegated
resolver contract that can be customized by the domain owner. See UML diagram
for an example.

> To register a name in Görli, just get more funds from the
> [faucet](https://goerli-faucet.slock.it/) in a
> [Metamask](https://metamask.io/) account, and use the [ENS
> ](https://app.ens.domains/)[dApp](https://app.ens.domains/) to get your own
> domain.

![](https://miro.medium.com/max/1400/1*txco_IQn1uqaNTSNLy0lEQ.png)

UML sequence diagram of how Ethereum Name Service (ENS) resolves a name.

 _source:_[ _https://docs.ens.domains/_](https://docs.ens.domains/)

Back to the terminal, let’s use Incubed `client.eth.contract` module to print
the registered resolver contract address of a valid ENS registry. If you
already registered a domain, replace `depraz.eth` with your domain name, and
check if the resolver contract address match.

    
    
    client = in3.Client('goerli')domain_name = client.ens_namehash('depraz.eth')  
    ens_registry_addr = '0x00000000000c2e074ec69a0dfb2997ba6c7d2e1e'  
    ens_resolver_abi = 'resolver(bytes32):address'  
    tx_data = client.eth.contract.encode(ens_resolver_abi, domain_name)  
    resolver_tx = {  
        "to": ens_registry_addr,  
        "data": tx_data  
    }  
    tx = in3.eth.NewTransaction(**resolver_tx)  
    encoded_resolver_addr = client.eth.contract.call(tx)  
    client.eth.contract.decode(ens_resolver_abi, encoded_resolver_addr)

This piece of code is a bit complex, so let’s break it down.

All actions in a blockchain happen by sending transactions. When a transaction
triggers a state change, like moving funds, storing data, or changing smart
contract code, there is a cost to do so. However, there is no cost to retrieve
data, that is why the transaction value is blank.

When executing code in a remote application, we need to know the function name
we will call, the parameters it expects to receive, as well as whatever it may
return. That is what the `ens_resolver_abi` describes.

The `encode` and `decode` methods use this function descriptor to translate
data sent to and from the Ethereum Virtual Machine (EVM). The EVM is one of
the main components of Incubed; whenever the user calls a smart contract
function, the client will ask the network for an attested copy of that code,
execute it with given parameters, and return the calculated value.

# Incubed does not trust the network response, but gathers all necessary
information to execute the EVM code and verify that the answer is correct.

ENS is an essential part of the Ethereum ecosystem, and Incubed wouldn’t be a
great tool if you had to write all that code to resolve names, right?

    
    
    client.ens_resolver('depraz.eth')

 _Voilá!_ Find the domain name owner by calling `client.ens_owner`, and the
account address that the domain points to with `client.ens_address`.

> The ENS smart contract snippet is part of the
> [example](https://in3.readthedocs.io/en/develop/api-python.html#examples)s.
> Try them out!

Another great feature of the client that Python enhances is the modular
transport function. The network of Incubed nodes only listens to HTTP
requests, but maybe you’re running the client on a smartwatch and can only
connect over Bluetooth to a smartphone. We’ve got you covered! Simply write a
transport function that will handle the Bluetooth communication and pass it to
the client.

`client = in3.Client(transport=bluetooth_transport)`

On the smartphone watch app you wrote, the messages received from the
smartwatch must have all information needed to make the HTTP requests to the
Incubed network over the internet and route back the responses over Bluetooth
to the Incubed client in the smartwatch.

## You can now set up your smartwatch to pay yourself some ETH each time you
complete that morning exercise you committed yourself to doing. Incentivized
workout could be a revolution!

This Python distribution was developed with
[PEP20](https://www.python.org/dev/peps/pep-0020/), the Zen of Python, in
mind, and we plan to refine and enhance it while maintaining our respect for
this philosophy. If you have suggestions and feedback, we’d love to hear it!

    
    
    The Zen of PythonBeautiful is better than ugly.  
    Explicit is better than implicit.  
    Simple is better than complex.  
    Complex is better than complicated.  
    Flat is better than nested.  
    Sparse is better than dense.  
    Readability counts.  
    ...

# Thank you for hanging until the end of the tutorial! We appreciate it and
hope you had fun learning about our Ethereum tools.

# We are planning new releases of the Python bindings with new features,
facilitators, a more intuitive account and smart contract interfaces, Bitcoin
support, and more. Stay tuned!

> For the complete Incubed technical documentation visit
> [ReadTheDocs](https://in3.readthedocs.io/en/develop/index.html).
>
> To push Web3.0 further, we also maintain a [WASM](https://webassembly.org/)
> distribution. [_Try it_](https://github.com/slockit/in3/releases) _!_
>
> If you simply want to fiddle with Incubed before adding it to your project,
> we highly recommend trying the [command-line tool](/blockchain-in-a-
> shell-45b6626dc2c0).
>
> We also support other Incubed releases, check them on
> [Github](https://github.com/slockit/in3-c/releases).

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fslock-
it-
blog%2F63b79368d58e&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fincubed-
for-python-batteries-
included-63b79368d58e&user=J.+Paul+R.+Depraz&userId=26ff11bf9c6d&source=-----63b79368d58e
---------------------clap_footer-----------)

\--

1

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fslock-
it-
blog%2F63b79368d58e&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fincubed-
for-python-batteries-
included-63b79368d58e&user=J.+Paul+R.+Depraz&userId=26ff11bf9c6d&source=-----63b79368d58e
---------------------clap_footer-----------)

\--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fslock-
it-
blog%2F63b79368d58e&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fincubed-
for-python-batteries-
included-63b79368d58e&user=J.+Paul+R.+Depraz&userId=26ff11bf9c6d&source=-----63b79368d58e
---------------------clap_footer-----------)

\--

1

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F63b79368d58e&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fincubed-
for-python-batteries-
included-63b79368d58e&source=--------------------------bookmark_footer-----------)

## [More from slock.it Blog](https://blog.slock.it/?source=post_page-----
63b79368d58e--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Fslock-
it-
blog%2F63b79368d58e&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fincubed-
for-python-batteries-
included-63b79368d58e&collection=slock.it+Blog&collectionId=15115b6d917a&source=post_page
-----63b79368d58e---------------------follow_footer-----------)

IoT + Blockchain

[Read more from slock.it Blog](https://blog.slock.it/?source=post_page-----
63b79368d58e--------------------------------)

## Recommended from Medium

[[![Alberto
Cevallos](https://miro.medium.com/fit/c/40/40/2*yhVzoSJlW038mmTLQJCbHg.jpeg)](https://albertocevallos.medium.com/?source=post_internal_links
---------0----------------------------)

[Alberto Cevallos

](https://albertocevallos.medium.com/?source=post_internal_links---------
0----------------------------)

in

[HackerNoon.com

](https://medium.com/hackernoon?source=post_internal_links---------
0----------------------------)

## A (Short) Intro to Cryptoeconomic Modelling (1/2)

![](https://miro.medium.com/focal/112/112/50/50/1*241yt5qGzbVEKRZ-W1uMPA.jpeg)](https://medium.com/hackernoon/a-short-
intro-to-cryptoeconomic-modelling-1-2-a840fa55bd18?source=post_internal_links
---------0----------------------------)

[[![Tecmeup](https://miro.medium.com/fit/c/40/40/1*OcB-dyB-
nQXjXtixGqR43A.png)](https://untilwefall.medium.com/?source=post_internal_links
---------1----------------------------)

[Tecmeup

](https://untilwefall.medium.com/?source=post_internal_links---------
1----------------------------)

in

[Coinmonks

](https://medium.com/coinmonks?source=post_internal_links---------
1----------------------------)

## Cardano Tokens Being Airdropped

![](https://miro.medium.com/focal/112/112/50/50/1*cgwiKbWAoAy1ASor1k7-FA.jpeg)](https://medium.com/coinmonks/cardano-
tokens-being-airdropped-1216b189929d?source=post_internal_links---------
1----------------------------)

[[![Daniel
Wu](https://miro.medium.com/fit/c/40/40/1*--KZtdQe0VoLEamelOfwZg.jpeg)](https://medium.com/@gcc2ge?source=post_internal_links
---------2----------------------------)

[Daniel Wu

](https://medium.com/@gcc2ge?source=post_internal_links---------
2----------------------------)

in

[ppio

](https://medium.com/ppio?source=post_internal_links---------
2----------------------------)

## Ethereum 2.0: The Road to Being the World’s Computer

![](https://miro.medium.com/focal/112/112/50/50/0*YNokJrcCHKRNOhW1)](https://medium.com/ppio/ethereum-2-0-the-
road-to-being-the-worlds-computer-663d4e6a90f1?source=post_internal_links
---------2----------------------------)

[[![Michael
Oluseye](https://miro.medium.com/fit/c/40/40/0*us5SZxHsUz_T7iUq.jpg)](https://michlany.medium.com/?source=post_internal_links
---------3----------------------------)

[Michael Oluseye

](https://michlany.medium.com/?source=post_internal_links---------
3----------------------------)

## EPNS: USER’S NOTIFICATION SERVICE PROVIDER

](https://michlany.medium.com/epns-users-notification-service-
provider-d1fd525f6bcf?source=post_internal_links---------
3----------------------------)

[[![Blockchain Files](https://miro.medium.com/fit/c/40/40/1*jKdT9p0yk1cZOYs-
MvKxLg.png)](https://blockchainfiles.medium.com/?source=post_internal_links
---------4----------------------------)

[Blockchain Files

](https://blockchainfiles.medium.com/?source=post_internal_links---------
4----------------------------)

in

[Coinmonks

](https://medium.com/coinmonks?source=post_internal_links---------
4----------------------------)

## What Do You Get When You Buy a Digital Art NFT?

![](https://miro.medium.com/focal/112/112/50/50/1*mpCcj8SuO3FqGd-
Yn93h0A.png)](https://medium.com/coinmonks/what-do-you-get-when-you-buy-a-
digital-art-nft-a13209c88119?source=post_internal_links---------
4----------------------------)

[[![Lajos
Deme](https://miro.medium.com/fit/c/40/40/1*40Pcdk5YkcCOWF0OusV6DQ.jpeg)](https://medium.com/@ldeme?source=post_internal_links
---------5----------------------------)

[Lajos Deme

](https://medium.com/@ldeme?source=post_internal_links---------
5----------------------------)

in

[Coinmonks

](https://medium.com/coinmonks?source=post_internal_links---------
5----------------------------)

## Comparison of the most popular ERC721 templates

![](https://miro.medium.com/focal/112/112/50/50/1*a0UT5Ooc2nQtDUaJnB4jJg.png)](https://medium.com/coinmonks/comparison-
of-the-most-popular-erc721-templates-b3614353e31e?source=post_internal_links
---------5----------------------------)

[[![NAOS Finance
Editor](https://miro.medium.com/fit/c/40/40/1*3D2yQ_m87aui9qcW82-DZg.png)](https://naosfin.medium.com/?source=post_internal_links
---------6----------------------------)

[NAOS Finance Editor

](https://naosfin.medium.com/?source=post_internal_links---------
6----------------------------)

in

[NAOS Finance — Official Publications

](https://medium.com/naos-finance?source=post_internal_links---------
6----------------------------)

## Our first MIP6 application on MakerDao is live!

![](https://miro.medium.com/focal/112/112/50/50/1*VVKXGRarbUVXK4YztJ2wNQ.jpeg)](https://medium.com/naos-
finance/our-first-mip6-application-on-makerdao-is-
live-d533e83b5b0c?source=post_internal_links---------
6----------------------------)

[[![MVL
Blockchain](https://miro.medium.com/fit/c/40/40/1*IHaTPXcIS9bnUWwmBxlabw.jpeg)](https://medium.com/@mvlchain?source=post_internal_links
---------7----------------------------)

[MVL Blockchain

](https://medium.com/@mvlchain?source=post_internal_links---------
7----------------------------)

in

[MVL Blockchain

](https://medium.com/mvl-ecosystem?source=post_internal_links---------
7----------------------------)

## Weekly News — Feb 21

![](https://miro.medium.com/focal/112/112/50/50/1*GKKJZT18HoUoqkoVLM9daw.jpeg)](https://medium.com/mvl-
ecosystem/weekly-news-feb-21-5d542ab20f36?source=post_internal_links---------
7----------------------------)

[](https://medium.com/?source=post_page-----
63b79368d58e--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
63b79368d58e--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
63b79368d58e--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
63b79368d58e--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
63b79368d58e--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----63b79368d58e--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----63b79368d58e--------------------------------)

[Get
started](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fincubed-
for-python-batteries-included-63b79368d58e&source=post_page
--------------------------nav_reg-----------)

[![J. Paul R.
Depraz](https://miro.medium.com/fit/c/176/176/0*t6h22joY7Q7QOVfa.jpg)](https://medium.com/@deprazz)

[

## J. Paul R. Depraz

](https://medium.com/@deprazz)

14 Followers

Engineer and Techincal Lead @ [Slock.it](http://Slock.it)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F26ff11bf9c6d&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fincubed-
for-python-batteries-
included-63b79368d58e&user=J.+Paul+R.+Depraz&userId=26ff11bf9c6d&source=post_page-26ff11bf9c6d
-------------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fusers%2F26ff11bf9c6d%2Flazily-
enable-writer-
subscription&operation=register&redirect=https%3A%2F%2Fblog.slock.it%2Fincubed-
for-python-batteries-
included-63b79368d58e&user=J.+Paul+R.+Depraz&userId=26ff11bf9c6d&source=--------------------------subscribe_user-----------)

## More from Medium

[[![codeforests](https://miro.medium.com/fit/c/40/40/1*95EPLIhm76FT95BJW1dEzw.png)](https://codeforests.medium.com/?source=read_next_recirc
---------0---------------------223ff823_cf5f_4d6f_a886_5a95fab407d4-------)

[codeforests

](https://codeforests.medium.com/?source=read_next_recirc---------0
---------------------223ff823_cf5f_4d6f_a886_5a95fab407d4-------)

## All You Need To Know About Python Brownie Network Setup

![](https://miro.medium.com/focal/112/112/50/50/1*UpRrJC7HtK9zZzavnUUcCw.jpeg)](https://codeforests.medium.com/all-
you-need-to-know-about-python-brownie-network-setup-
bd8002ef227c?source=read_next_recirc---------0---------------------
223ff823_cf5f_4d6f_a886_5a95fab407d4-------)

[[![Michael
Aye](https://miro.medium.com/fit/c/40/40/1*liSonpEJbn5T32PGikkUAw.jpeg)](https://medium.com/@michael.aye?source=read_next_recirc
---------1---------------------223ff823_cf5f_4d6f_a886_5a95fab407d4-------)

[Michael Aye

](https://medium.com/@michael.aye?source=read_next_recirc---------1
---------------------223ff823_cf5f_4d6f_a886_5a95fab407d4-------)

## Code-linting in JupyterLab using conda

](https://medium.com/@michael.aye/code-linting-in-jupyterlab-using-
conda-495aa5c115?source=read_next_recirc---------1---------------------
223ff823_cf5f_4d6f_a886_5a95fab407d4-------)

[[![Lena
Tyson](https://miro.medium.com/fit/c/40/40/1*BkmHhvGYmbP3Zw5UPenT1w.jpeg)](https://medium.com/@lenaztyson?source=read_next_recirc
---------2---------------------223ff823_cf5f_4d6f_a886_5a95fab407d4-------)

[Lena Tyson

](https://medium.com/@lenaztyson?source=read_next_recirc---------2
---------------------223ff823_cf5f_4d6f_a886_5a95fab407d4-------)

## The Decade of AI Development: The Most Noteworthy Moments of the 2010s

![](https://miro.medium.com/focal/112/112/50/50/1*yLikolBZMl4hEEUFLuo-1A.jpeg)](https://medium.com/@lenaztyson/the-
decade-of-ai-development-the-most-noteworthy-moments-of-
the-2010s-983d2f299d49?source=read_next_recirc---------2---------------------
223ff823_cf5f_4d6f_a886_5a95fab407d4-------)

[[![Yitaek
Hwang](https://miro.medium.com/fit/c/40/40/1*3w8ymifOsZMG8cInulebsg.jpeg)](https://yitaek.medium.com/?source=read_next_recirc
---------3---------------------223ff823_cf5f_4d6f_a886_5a95fab407d4-------)

[Yitaek Hwang

](https://yitaek.medium.com/?source=read_next_recirc---------3
---------------------223ff823_cf5f_4d6f_a886_5a95fab407d4-------)

in

[CoinsBench

](https://coinsbench.com/?source=read_next_recirc---------3
---------------------223ff823_cf5f_4d6f_a886_5a95fab407d4-------)

## Exploring Crypto Prices with QuestDB and Pandas

![](https://miro.medium.com/focal/112/112/50/50/0*OyarwlijR0zWubq1)](https://coinsbench.com/exploring-
crypto-prices-with-questdb-and-pandas-7084c1308755?source=read_next_recirc
---------3---------------------223ff823_cf5f_4d6f_a886_5a95fab407d4-------)

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

