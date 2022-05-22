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
contracts%2Freleases%2Ftag%2F1.6.0)

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

  * [ Code ](/argentlabs/argent-contracts/tree/1.6.0)
  * [ Issues 1 ](/argentlabs/argent-contracts/issues)
  * [ Pull requests 0 ](/argentlabs/argent-contracts/pulls)
  * [ Actions ](/argentlabs/argent-contracts/actions)
  * [ Projects 0 ](/argentlabs/argent-contracts/projects?type=beta)
  * [ Wiki ](/argentlabs/argent-contracts/wiki)
  * [ Security ](/argentlabs/argent-contracts/security)
  * [ Insights ](/argentlabs/argent-contracts/pulse)

More

  * [ Code ](/argentlabs/argent-contracts/tree/1.6.0)
  * [ Issues ](/argentlabs/argent-contracts/issues)
  * [ Pull requests ](/argentlabs/argent-contracts/pulls)
  * [ Actions ](/argentlabs/argent-contracts/actions)
  * [ Projects ](/argentlabs/argent-contracts/projects?type=beta)
  * [ Wiki ](/argentlabs/argent-contracts/wiki)
  * [ Security ](/argentlabs/argent-contracts/security)
  * [ Insights ](/argentlabs/argent-contracts/pulse)

  1. [Releases](/argentlabs/argent-contracts/releases)
  2. [ 1.6.0 ](/argentlabs/argent-contracts/releases/tag/1.6.0)

__Compare

Choose a tag to compare

Could not load tags

Nothing to show

[ {{ refName }} default ](/argentlabs/argent-contracts/compare/{{
urlEncodedRefName }}...1.6.0)

[View all tags](/argentlabs/argent-contracts/tags)

# New MakerManager, Transfer ownership and approveAndCall transfers

![@elenadimitrova](https://avatars.githubusercontent.com/u/703848?s=40&v=4)
[elenadimitrova](/elenadimitrova) released this

* [ 1275 commits ](/argentlabs/argent-contracts/compare/1.6.0...master) to master since this release 

[ 1.6.0  ](/argentlabs/argent-contracts/tree/1.6.0)

[ `a450798` ](/argentlabs/argent-
contracts/commit/a450798286a3f74a0965ed69093f2fb6565906d7)

__Compare

Choose a tag to compare

Could not load tags

Nothing to show

[ {{ refName }} default ](/argentlabs/argent-contracts/compare/{{
urlEncodedRefName }}...1.6.0)

[View all tags](/argentlabs/argent-contracts/tags)

## Functional updates

**Added`MakerV2Manager` module** [#50](https://github.com/argentlabs/argent-
contracts/pull/50) which enables:

  * Borrowing DAI via MCD Vaults
  * DAI investments into the DSR pot

The `MakerManager` module will be replaced in the next release by the
`MakerV2Manager` module.

**Added`RecoveryManager` module - Transfer ownership logic**
[#63](https://github.com/argentlabs/argent-contracts/pull/63) to allow for
instant wallet recovery using owner + `ceil (n/2)` guardian signatures.

**Updated`RecoveryManager` module - Recovery logic**
[#63](https://github.com/argentlabs/argent-contracts/pull/63) to:

  * recovery needs to be signed by ceil(N/2) guardians
  * cancel needs to be signed by owner + floor(n/2) guardians

**Updated`ApprovedTransfer` and `TransferManager` modules -
`approveTokenAndCallContract`** [#73](https://github.com/argentlabs/argent-
contracts/pull/73) [#84](https://github.com/argentlabs/argent-
contracts/pull/84) to approve an amount of tokens and call a contract that
consumes these tokens in one atomic transaction. This function existed in
`TransferManager` but not in `ApprovedTransfer` prior to this release.
Additionally this method now enables a different contract address for the
approved spender and the called contract.  
Also in this method we've changed the logic to restore the original approved
amount.

## Maintenance

  * Expose `getRequiredSignatures` as public on `RelayerModuleV2`
  * Disable the `UniswapManager` module [#71](https://github.com/argentlabs/argent-contracts/pull/71)
  * Set the `kyberNetwork` variable to `address(0)` in `TokenPriceProvider` since we are no longer using it to sync prices. [#77](https://github.com/argentlabs/argent-contracts/pull/77)
  * Remove `LegacyUpgrader` \- limit backward compatibility to 1 to force rolling upgrades. [#91](https://github.com/argentlabs/argent-contracts/pull/91)
  * Refactoring of the `RelayerModule` `validateSignatures` [#76](https://github.com/argentlabs/argent-contracts/pull/76)
  * Makes gas price configurable and consistent on deployments [#87](https://github.com/argentlabs/argent-contracts/pull/87)
  * Restructuring of the contracts folder structure in the repo [#86](https://github.com/argentlabs/argent-contracts/pull/86)
  * Add JavaScript linting to the CI checks [#62](https://github.com/argentlabs/argent-contracts/pull/62)

### Assets

2

  * [ Source code (zip) ](/argentlabs/argent-contracts/archive/refs/tags/1.6.0.zip)

  * [ Source code (tar.gz) ](/argentlabs/argent-contracts/archive/refs/tags/1.6.0.tar.gz)

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

