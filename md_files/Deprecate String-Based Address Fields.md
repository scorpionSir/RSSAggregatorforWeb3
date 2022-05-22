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

[ Sign in ](/login?return_to=https%3A%2F%2Fgithub.com%2Fcoinbase%2Frosetta-
specifications%2Freleases%2Ftag%2Fv1.4.4)

[ Sign up
](/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-
name%3E%2F%3Crepo-name%3E%2Freleases%2Fshow&source=header-
repo&source_repo=coinbase%2Frosetta-specifications)

{{ message }}

##  [coinbase](/coinbase) / **[rosetta-specifications](/coinbase/rosetta-
specifications) ** Public

  * [ Notifications ](/login?return_to=%2Fcoinbase%2Frosetta-specifications)
  * [ Fork 72 ](/login?return_to=%2Fcoinbase%2Frosetta-specifications)
  * [ Star  250 ](/login?return_to=%2Fcoinbase%2Frosetta-specifications)

  * [ Code ](/coinbase/rosetta-specifications/tree/v1.4.4)
  * [ Issues 8 ](/coinbase/rosetta-specifications/issues)
  * [ Pull requests 2 ](/coinbase/rosetta-specifications/pulls)
  * [ Discussions ](/coinbase/rosetta-specifications/discussions)
  * [ Actions ](/coinbase/rosetta-specifications/actions)
  * [ Security ](/coinbase/rosetta-specifications/security)
  * [ Insights ](/coinbase/rosetta-specifications/pulse)

More

  * [ Code ](/coinbase/rosetta-specifications/tree/v1.4.4)
  * [ Issues ](/coinbase/rosetta-specifications/issues)
  * [ Pull requests ](/coinbase/rosetta-specifications/pulls)
  * [ Discussions ](/coinbase/rosetta-specifications/discussions)
  * [ Actions ](/coinbase/rosetta-specifications/actions)
  * [ Security ](/coinbase/rosetta-specifications/security)
  * [ Insights ](/coinbase/rosetta-specifications/pulse)

  1. [Releases](/coinbase/rosetta-specifications/releases)
  2. [ v1.4.4 ](/coinbase/rosetta-specifications/releases/tag/v1.4.4)

__Compare

Choose a tag to compare

Could not load tags

Nothing to show

[ {{ refName }} default ](/coinbase/rosetta-specifications/compare/{{
urlEncodedRefName }}...v1.4.4)

[View all tags](/coinbase/rosetta-specifications/tags)

# Deprecate String-Based Address Fields

![@patrick-ogrady](https://avatars.githubusercontent.com/u/13023275?s=40&v=4)
[patrick-ogrady](/patrick-ogrady) released this

* [ 95 commits ](/coinbase/rosetta-specifications/compare/v1.4.4...master) to master since this release 

[ v1.4.4  ](/coinbase/rosetta-specifications/tree/v1.4.4)

[ `a399adf` ](/coinbase/rosetta-
specifications/commit/a399adf75a2dfbbb3e306574fb912f8bf6f5f500)

This commit was created on GitHub.com and signed with GitHub’s **verified
signature**.

GPG key ID: 4AEE18F83AFDEB23

[Learn about vigilant mode](https://docs.github.com/github/authenticating-to-
github/displaying-verification-statuses-for-all-of-your-commits).

__Compare

Choose a tag to compare

Could not load tags

Nothing to show

[ {{ refName }} default ](/coinbase/rosetta-specifications/compare/{{
urlEncodedRefName }}...v1.4.4)

[View all tags](/coinbase/rosetta-specifications/tags)

**THIS RELEASE IS BACKWARDS-COMPATIBLE WITH ALL PREVIOUS RELEASES.**

This release deprecates all string-based `Address` fields and replaces them
with `AccountIdentifier-based` fields. This empowers blockchains that support
associating multiple keys with an account to provide expressive interaction
using the Construction API.

### Backwards Compatibility

When the `AccountIdentifier-based` fields are not populated, clients assume
that the string-based `Address` field is equal to:

    
    
    {
      "address": {{Address}},
    }
    

### Changelog

  * Deprecate string-based Address Fields [`#48`](https://github.com/coinbase/rosetta-specifications/pull/48)

### Assets

3

  * [ api.json ](/coinbase/rosetta-specifications/releases/download/v1.4.4/api.json)

73.4 KB

  * [ Source code (zip) ](/coinbase/rosetta-specifications/archive/refs/tags/v1.4.4.zip)

  * [ Source code (tar.gz) ](/coinbase/rosetta-specifications/archive/refs/tags/v1.4.4.tar.gz)

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

