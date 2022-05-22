Skip to content

[ ](https://github.com/)

[ Sign up
](/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-
name%3E%2F%3Crepo-name%3E%2Freleases%2Fshow&source=header-repo)

  * Product 

    * [ Features ](/features)
    * [ Mobile ](/mobile)
    * [ Actions ](/features/actions)
    * [ Codespaces ](/features/codespaces)
    * [ Packages ](/features/packages)
    * [ Security ](/features/security)
    * [ Code review ](/features/code-review)
    * [ Issues ](/features/issues)
    * [ Integrations ](/features/integrations)
    * [ GitHub Sponsors ](/sponsors)
    * [ Customer stories ](/customer-stories)

  * [Team](/team)
  * [Enterprise](/enterprise)
  * Explore 

    * [ Explore GitHub ](/explore)
    * Learn and contribute
    * [ Topics ](/topics)
    * [ Collections ](/collections)
    * [ Trending ](/trending)
    * [ Learning Lab ](https://lab.github.com/)
    * [ Open source guides ](https://opensource.guide)
    * Connect with others
    * [ The ReadME Project ](/readme)
    * [ Events ](/events)
    * [ Community forum ](https://github.community)
    * [ GitHub Education ](https://education.github.com)
    * [ GitHub Stars program ](https://stars.github.com)

  * [Marketplace](/marketplace)
  * Pricing 

    * [ Plans ](/pricing)
    * [ Compare plans ](/pricing#compare-features)
    * [ Contact Sales ](https://github.com/enterprise/contact)
    * [ Education ](https://education.github.com)

  * [ ![]() In this repository  All GitHub  ↵ Jump to ↵ ]()

  * No suggested jump to results

  * [ ![]() In this repository  All GitHub  ↵ Jump to ↵ ]()
  * [ ![]() In this organization  All GitHub  ↵ Jump to ↵ ]()
  * [ ![]() In this repository  All GitHub  ↵ Jump to ↵ ]()

[ Sign in ](/login?return_to=https%3A%2F%2Fgithub.com%2Fargentlabs%2Fargent-
contracts%2Freleases%2Ftag%2F2.1)

[ Sign up
](/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-
name%3E%2F%3Crepo-name%3E%2Freleases%2Fshow&source=header-
repo&source_repo=argentlabs%2Fargent-contracts)

{{ message }}

##  [argentlabs](/argentlabs) / **[argent-contracts](/argentlabs/argent-
contracts) ** Public

  * [ Notifications ](/login?return_to=%2Fargentlabs%2Fargent-contracts)
  * [ Fork 119 ](/login?return_to=%2Fargentlabs%2Fargent-contracts)
  * [ Star  339 ](/login?return_to=%2Fargentlabs%2Fargent-contracts)

  * [ Code ](/argentlabs/argent-contracts/tree/2.1)
  * [ Issues 1 ](/argentlabs/argent-contracts/issues)
  * [ Pull requests 0 ](/argentlabs/argent-contracts/pulls)
  * [ Actions ](/argentlabs/argent-contracts/actions)
  * [ Projects 0 ](/argentlabs/argent-contracts/projects?type=beta)
  * [ Wiki ](/argentlabs/argent-contracts/wiki)
  * [ Security ](/argentlabs/argent-contracts/security)
  * [ Insights ](/argentlabs/argent-contracts/pulse)

More

  * [ Code ](/argentlabs/argent-contracts/tree/2.1)
  * [ Issues ](/argentlabs/argent-contracts/issues)
  * [ Pull requests ](/argentlabs/argent-contracts/pulls)
  * [ Actions ](/argentlabs/argent-contracts/actions)
  * [ Projects ](/argentlabs/argent-contracts/projects?type=beta)
  * [ Wiki ](/argentlabs/argent-contracts/wiki)
  * [ Security ](/argentlabs/argent-contracts/security)
  * [ Insights ](/argentlabs/argent-contracts/pulse)

  1. [Releases](/argentlabs/argent-contracts/releases)
  2. [ 2.1 ](/argentlabs/argent-contracts/releases/tag/2.1)

__Compare

Choose a tag to compare

Could not load tags

Nothing to show

[ {{ refName }} default ](/argentlabs/argent-contracts/compare/{{
urlEncodedRefName }}...2.1)

[View all tags](/argentlabs/argent-contracts/tags)

# Re-architecture and upgrade to Solidity 0.6

![@elenadimitrova](https://avatars.githubusercontent.com/u/703848?s=40&v=4)
[elenadimitrova](/elenadimitrova) released this

* [ 771 commits ](/argentlabs/argent-contracts/compare/2.1...master) to master since this release 

[ 2.1  ](/argentlabs/argent-contracts/tree/2.1)

[ `91e0dcf` ](/argentlabs/argent-
contracts/commit/91e0dcf576f07c7d5ff7fb4255ad410a607e625d)

__Compare

Choose a tag to compare

Could not load tags

Nothing to show

[ {{ refName }} default ](/argentlabs/argent-contracts/compare/{{
urlEncodedRefName }}...2.1)

[View all tags](/argentlabs/argent-contracts/tags)

This major release abstracts the wallet modules one layer away behind the new
`VersionManager` module [#151](https://github.com/argentlabs/argent-
contracts/pull/151) It also focusses on the upgrade of all features and parts
of the infrastructure contracts to Solidity v0.6.12 .

Upgraded features: `ApprovedTransfer`, `CompoundManager`, `GuardianManager`,
`LockManager`, `NftTransfer`, `RecoveryManager`, `TokenExchanger`,
`MakerV2Manager`, `TransferManager` and the new `RelayerManager`. Additionally
disables the `MakerManager` which is the now legacy Maker logic.

Upgraded infrastructure and wallet contracts: `WalletFactory`, `BaseWallet`
and `Proxy` in addition to decommissioning the `TokenPriceProvider` and
introducing `TokenPriceRegistry` instead.

## Functional updates

**RelayerManager**  
Extracted into a standalone module. All meta-transactions must be sent to its
`execute` method which will verify them and relay the call to the target
module.

Enable refunds in ETH and ERC20. All refunds are counted towards the daily
limit, unless that target action is approved by the owner and a majority of
guardians. [#131](https://github.com/argentlabs/argent-contracts/pull/131)

Failures of the sub-call in `execute` method are logged in the extended
`TransactionExecuted` event. [#97](https://github.com/argentlabs/argent-
contracts/pull/97)

**Transfer modules:`ApprovedTransfer` and `TransferManager`**  
Add two new methods to `ApprovedTransfer` to simplify the management of the
daily limit:

  * `changeLimit` updates the current value of the daily limit immediately when approved by guardians
  * `resetLimit` to reset the daily consumption to 0 immediately when approved by guardians

Every action in `ApprovedTransfer` resets the daily spent amount to 0.

In `TransferManager` decreasing the daily limit becomes immediate, while
increasing the limit remains pending for the duration of the security period.
[#138](https://github.com/argentlabs/argent-contracts/pull/138)

Allows whitelisted tokens to be called in `TransferManager`
[#133](https://github.com/argentlabs/argent-contracts/pull/133)

Adds `approveWethAndCallContract` method to both transfer modules which wraps
ETH into WETH -> approve WETH -> call a contract
[#140](https://github.com/argentlabs/argent-contracts/pull/140)

**TokenExchanger**  
Integrates with Paraswap instead of Kyber.
[#121](https://github.com/argentlabs/argent-contracts/pull/121)

**WalletFactory**  
ENS label is now optional when creating a wallet.
[#135](https://github.com/argentlabs/argent-contracts/pull/135)

Wallets can only be created with a guardian. Removed factory methods that
allow an empty guardian in wallet creation.
[#132](https://github.com/argentlabs/argent-contracts/pull/132)

`createCounterfactualWallet` method returns the address of the wallet.
[#132](https://github.com/argentlabs/argent-contracts/pull/132)

**TokenPriceProvider**  
Split into a managed storage contract - `TokenPriceRegistry` while the
`getEtherValue` logic is included in a wider `LimitUtils` library. The new
design relies on prices set to be that of `price per token * 10^(18- token
decimals)`. This allows us to eliminate the reliance on `decimals` property of
tokens which is an optional ERC20 property that can't be relied on. e.g. DGD
token. Additionally we've agreed to remove the DGD token from the token price
provider. [#120](https://github.com/argentlabs/argent-contracts/pull/120)

## Non-functional improvements

Upgrade contracts to solidity 0.6.12
[#114](https://github.com/argentlabs/argent-contracts/pull/114)
[#142](https://github.com/argentlabs/argent-contracts/pull/142)

Separate daily limits state out of `TransferManager` and into `LimitStorage`
contract. [#122](https://github.com/argentlabs/argent-contracts/pull/122)

More robust `CompoundManager` which now has added success checks to `CToken`
methods. These do not revert when failing but return a non-zero error code
instead. We add checks to ensure that the expected token balance changes have
occurred after a Compound method is executed.
[#134](https://github.com/argentlabs/argent-contracts/pull/134)

Lighter `CompoundManager` module since we removed `Invest` and `Loan` contract
dependencies. [#108](https://github.com/argentlabs/argent-contracts/pull/108)

More robust `approveTokenAndCallContract` ensures there is sufficient token
balance before executing [#136](https://github.com/argentlabs/argent-
contracts/pull/136)

Improve the required signatures logic in relayer where we add an entry in the
`OwnerSignature` enum called `Anyone` to make the intention clearer that there
are cases where no mandated signatures are required
[#130](https://github.com/argentlabs/argent-contracts/pull/130)

Disabled the ability to add a module (and therefore upgrade) when a wallet is
locked. A wallet can be locked either explicitly by a guardian or during a
wallet recovery. [#128](https://github.com/argentlabs/argent-
contracts/pull/128)

Enables recovery of non-compliant tokens in the `BaseModule.`
[#125](https://github.com/argentlabs/argent-contracts/pull/125)

Ensure a module is registered before upgrading
[#119](https://github.com/argentlabs/argent-contracts/pull/119)

Consistent `SafeMath` library use [#100](https://github.com/argentlabs/argent-
contracts/pull/100)

## Maintenance updates

Add static contract analysis using `slither` to a nightly job in CI.
[#93](https://github.com/argentlabs/argent-contracts/pull/93)
[#126](https://github.com/argentlabs/argent-contracts/pull/126)

Replace `ethlint` with `solhint` [#137](https://github.com/argentlabs/argent-
contracts/pull/137)

Introduced `bn-chai` to easily compare big numbers in unit tests.

## Production contracts

    
    
    WalletFactory 0x9ae0AcdB750bFcF694675f46B580847fC49A48bF
    ENSResolver 0xDa1756Bb923Af5d1a05E277CB1E54f1D0A127890
    ENSManager 0xC4BaAbB5b7DFF84Aa8023183E3Ca0bA3B2Fee519
    TokenPriceProvider 0xE8a76D2f37Fe50B6A95d27FB92291Fe0B57407d3
    ModuleRegistry 0xc17D432Bd8e8850Fd7b32B0270f5AfAc65DB0105
    BaseWallet 0x29b94b045a0b828d9eb99136A16d97c7fF3d2600
    CompoundRegistry 0xC43472062B4e3763C775956988CC883d4b863d91
    MakerRegistry 0x7383757C8a2F4cbc6A21a26e1F33a0fd95e7bb77
    DexRegistry 0x38AEED2AF853FCCF5c246E3aEE8bCCcbb5826d87
    GuardianStorage 0x44DA3A8051bA88EAB0440DB3779cAB9D679ae76f
    TransferStorage 0x391f0e86dA951C03b1183C60b195090671ADea88
    ModuleManager 0x4DD68a6C27359E5640Fa6dCAF13631398C5613f1
    GuardianManager 0x95F6f73484b37Fcc36a75BD5d96D861CF855e85d
    LockManager 0x42EaA6F456Ce8ee9292C0fdD9af40C389CAB48b0
    RecoveryManager 0x5FC48Bc1B54F718d6B307C8027207cD7c3bcc0EF
    ApprovedTransfer 0x321b3A051504B0f36b40082275090ffE5838a77E
    TokenExchanger 0xC4B25cc5633a7079690b6DD87135e18a82C707FE
    NftTransfer 0x7531F4d6b7DFD84ab84f9f56Ef75515bd03F800c
    MakerManager 0x963F86DA34Cf2CE619d4B8e5cE96577943f95B6b
    CompoundManager 0x18CfB667F10c004f9534eA3C928b864d14c8fc11
    TransferManager 0xB2135c6bd950e197982FA4b02f45018bDB8bEDDa
    MakerV2Manager 0x2Bf38de07042240b52B7C40F044ABEfD7b01A5BE
    LimitStorage 0x045B32efA0D97a681Cc415f1B37C972Ad7299a55
    TokenPriceRegistry 0xe4db5b456282Eff5fE9f1eb53A3a536Bf56AEffA
    LockStorage 0xF657BB6bc979bf34d49e38AfBA34D5FD2A45B0Ca
    RelayerManager 0x5f822140F77ae228E0838FeA425Adfa9Cba0Bb73
    VersionManager 0x4B3fBe6d554c540C2672eB7A501018a1A39f7F53
    

All contracts are verified on Etherscan except for the following:
`ApprovedTransfer`, `TokenExchanger`, `TransferManager`, `LimitStorage` and
`RelayerManager` due to an issue verifying contracts using the `ABIEncoderV2`.
These can however still be verified locally.

### Assets

2

  * [ Source code (zip) ](/argentlabs/argent-contracts/archive/refs/tags/2.1.zip)

  * [ Source code (tar.gz) ](/argentlabs/argent-contracts/archive/refs/tags/2.1.tar.gz)

  * [ ](https://github.com "GitHub") (C) 2022 GitHub, Inc. 

  * [Terms](https://docs.github.com/en/github/site-policy/github-terms-of-service)
  * [Privacy](https://docs.github.com/en/github/site-policy/github-privacy-statement)
  * [Security](https://github.com/security)
  * [Status](https://www.githubstatus.com/)
  * [Docs](https://docs.github.com)
  * [Contact GitHub](https://support.github.com?tags=dotcom-footer)
  * [Pricing](https://github.com/pricing)
  * [API](https://docs.github.com)
  * [Training](https://services.github.com)
  * [Blog](https://github.blog)
  * [About](https://github.com/about)

You can’t perform that action at this time.

You signed in with another tab or window. [Reload]() to refresh your session.
You signed out in another tab or window. [Reload]() to refresh your session.

