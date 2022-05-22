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

[ Sign in ](/login?return_to=https%3A%2F%2Fgithub.com%2Fstarkware-
libs%2Fstarkex-contracts%2Freleases%2Ftag%2Fv2.0)

[ Sign up
](/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-
name%3E%2F%3Crepo-name%3E%2Freleases%2Fshow&source=header-
repo&source_repo=starkware-libs%2Fstarkex-contracts)

{{ message }}

##  [starkware-libs](/starkware-libs) / **[starkex-contracts](/starkware-
libs/starkex-contracts) ** Public

  * [ Notifications ](/login?return_to=%2Fstarkware-libs%2Fstarkex-contracts)
  * [ Fork 30 ](/login?return_to=%2Fstarkware-libs%2Fstarkex-contracts)
  * [ Star  132 ](/login?return_to=%2Fstarkware-libs%2Fstarkex-contracts)

  * [ Code ](/starkware-libs/starkex-contracts/tree/v2.0)
  * [ Issues 2 ](/starkware-libs/starkex-contracts/issues)
  * [ Pull requests 2 ](/starkware-libs/starkex-contracts/pulls)
  * [ Actions ](/starkware-libs/starkex-contracts/actions)
  * [ Projects 0 ](/starkware-libs/starkex-contracts/projects?type=beta)
  * [ Wiki ](/starkware-libs/starkex-contracts/wiki)
  * [ Security ](/starkware-libs/starkex-contracts/security)
  * [ Insights ](/starkware-libs/starkex-contracts/pulse)

More

  * [ Code ](/starkware-libs/starkex-contracts/tree/v2.0)
  * [ Issues ](/starkware-libs/starkex-contracts/issues)
  * [ Pull requests ](/starkware-libs/starkex-contracts/pulls)
  * [ Actions ](/starkware-libs/starkex-contracts/actions)
  * [ Projects ](/starkware-libs/starkex-contracts/projects?type=beta)
  * [ Wiki ](/starkware-libs/starkex-contracts/wiki)
  * [ Security ](/starkware-libs/starkex-contracts/security)
  * [ Insights ](/starkware-libs/starkex-contracts/pulse)

  1. [Releases](/starkware-libs/starkex-contracts/releases)
  2. [ v2.0 ](/starkware-libs/starkex-contracts/releases/tag/v2.0)

__Compare

Choose a tag to compare

Could not load tags

Nothing to show

[ {{ refName }} default ](/starkware-libs/starkex-contracts/compare/{{
urlEncodedRefName }}...v2.0)

[View all tags](/starkware-libs/starkex-contracts/tags)

# StarkEx v2.0

![@MichaelRiabzev-
StarkWare](https://avatars.githubusercontent.com/u/39152713?s=40&v=4)
[MichaelRiabzev-StarkWare](/MichaelRiabzev-StarkWare) released this

* [ 9 commits ](/starkware-libs/starkex-contracts/compare/v2.0...master) to master since this release 

[ v2.0  ](/starkware-libs/starkex-contracts/tree/v2.0)

[ `2799231` ](/starkware-libs/starkex-
contracts/commit/27992317365bc58c6efcd0efe274fd58a7d08e9a)

__Compare

Choose a tag to compare

Could not load tags

Nothing to show

[ {{ refName }} default ](/starkware-libs/starkex-contracts/compare/{{
urlEncodedRefName }}...v2.0)

[View all tags](/starkware-libs/starkex-contracts/tags)

StarkEx v2.0 is the first major update to StarkEx. Below are the main added
features, both functional and non-functional.  
Please note that the contract functions are not backward compatible and every
interaction needs to be updated with the new version ABI.

### Functional Features

  * `Conditional Transfer` \- Off-chain transfers conditioned on a predefined on-chain event 
    * Allows arbitrary on-chain logic to be defined as the condition, thus allowing complicated interactions between L2 and L1.
    * Specifically, this primitive is used to facilitate Fast Withdrawals.
  * `Deposit` \- L1 users can deposit to any L2 user. 
    * In v1.0 users could only deposit to their own account.
  * `Withdrawal` \- Users can withdraw to any recipient Ethereum address. 
    * In v1.0 users could withdraw their funds from the contract only to the Ethereum address registered with that vault’s owner stark key.
  * `Register`
    * Multiple StarkEx keys - Users can register many StarkEx keys to one Ethereum address. 
      * In v1.0 the contract allowed only 1:1 mapping between Ethereum addresses and StarkEx keys.
    * Simplified Registration - Registration can be done by any sender. 
      * In v1.0 the registered Ethereum address had to be the sender.
      * There is no need to own Ether in order to register.
    * Enhanced signature security - Added a prefix to the `userAdmin` signature. 
      * This protects the `userAdmin` signer from an unexpected interpretation of their signature.
      * The `userAdmin` signature now has the following structure:  
`bytes32 signedData = keccak256(abi.encodePacked("UserRegistration:", ethKey,
starkKey))`.

  * ERC721 support - StarkEx now supports trading ERC721 tokens.
  * Off-chain minting support - The StarkEx v2.0 contract supports off-chain minting of tokens of compatible ERC20MINTABLE / ERC721MINTABLE types.

### Non-Functional Features

  * [Cairo](https://medium.com/starkware/hello-cairo-3cb43b13b209) \- StarkEx v2.0 is fully implemented on top of Cairo - our Turing-complete framework for STARKs.
  * Optimised statement design, supporting more efficient transaction packing in batches - enabling more transactions in each batch.

### Assets

2

  * [ Source code (zip) ](/starkware-libs/starkex-contracts/archive/refs/tags/v2.0.zip)

  * [ Source code (tar.gz) ](/starkware-libs/starkex-contracts/archive/refs/tags/v2.0.tar.gz)

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

