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

[ Sign in ](/login?return_to=https%3A%2F%2Fgithub.com%2FLN-Zap%2Fzap-
desktop%2Freleases%2Ftag%2Fv0.6.1-beta)

[ Sign up
](/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-
name%3E%2F%3Crepo-name%3E%2Freleases%2Fshow&source=header-repo&source_repo=LN-
Zap%2Fzap-desktop)

{{ message }}

##  [LN-Zap](/LN-Zap) / **[zap-desktop](/LN-Zap/zap-desktop) ** Public

  * [ Notifications ](/login?return_to=%2FLN-Zap%2Fzap-desktop)
  * [ Fork 222 ](/login?return_to=%2FLN-Zap%2Fzap-desktop)
  * [ Star  1.2k ](/login?return_to=%2FLN-Zap%2Fzap-desktop)

  * [ Code ](/LN-Zap/zap-desktop/tree/v0.6.1-beta)
  * [ Issues 124 ](/LN-Zap/zap-desktop/issues)
  * [ Pull requests 22 ](/LN-Zap/zap-desktop/pulls)
  * [ Actions ](/LN-Zap/zap-desktop/actions)
  * [ Security ](/LN-Zap/zap-desktop/security)
  * [ Insights ](/LN-Zap/zap-desktop/pulse)

More

  * [ Code ](/LN-Zap/zap-desktop/tree/v0.6.1-beta)
  * [ Issues ](/LN-Zap/zap-desktop/issues)
  * [ Pull requests ](/LN-Zap/zap-desktop/pulls)
  * [ Actions ](/LN-Zap/zap-desktop/actions)
  * [ Security ](/LN-Zap/zap-desktop/security)
  * [ Insights ](/LN-Zap/zap-desktop/pulse)

  1. [Releases](/LN-Zap/zap-desktop/releases)
  2. [ v0.6.1-beta ](/LN-Zap/zap-desktop/releases/tag/v0.6.1-beta)

__Compare

Choose a tag to compare

Could not load tags

Nothing to show

[ {{ refName }} default ](/LN-Zap/zap-desktop/compare/{{ urlEncodedRefName
}}...v0.6.1-beta)

[View all tags](/LN-Zap/zap-desktop/tags)

# Zap 0.6.1 Beta

![@mrfelton](https://avatars.githubusercontent.com/u/200251?s=40&v=4)
[mrfelton](/mrfelton) released this

* [ 1140 commits ](/LN-Zap/zap-desktop/compare/v0.6.1-beta...master) to master since this release 

[ v0.6.1-beta  ](/LN-Zap/zap-desktop/tree/v0.6.1-beta)

[ `ce26ba2` ](/LN-Zap/zap-
desktop/commit/ce26ba2f7c6e61719c42bd90ddcba35f7faa97b1)

__Compare

Choose a tag to compare

Could not load tags

Nothing to show

[ {{ refName }} default ](/LN-Zap/zap-desktop/compare/{{ urlEncodedRefName
}}...v0.6.1-beta)

[View all tags](/LN-Zap/zap-desktop/tags)

## Release notes

Zap 0.6.1 adds a ton of new features and improvements to existing ones...

## LND

We now ship with [LND
0.8.0-beta](https://github.com/lightningnetwork/lnd/releases/tag/v0.8.0-beta)
which delivers many improvements and enhancements. We continue to support
connecting to external LND nodes that are running prior versions of LND,
though we encourage all users to update their nodes.

For users running the built-in LND Neutrino client, we now allow you to
specify your own list of bitcoin nodes to pull blockchain data from. For
maximum privacy, you can choose whether you want to connect exclusively or
inclusively to your custom node whitelist. We continue to provide our own
nodes for you to use and by default, the app will connect to these.

## lnurl support

[Lnurl](https://github.com/btcontract/lnurl-rfc/blob/master/spec.md) is an
emerging standard that defines processes to simplify a number of standard
scenarios such as requesting incoming channels, withdrawing funds, doing
atomic swaps, etc.

In this release, we have added support for [lnurl-
withdraw](https://github.com/btcontract/lnurl-rfc/blob/master/spec.md#3-lnurl-
withdraw) which enables automated withdrawals directly to your wallet from
services that support the standard without the need for you to manually create
an invoice and supply to the service in question.

If you'd like to try out this feature, the excellent
[lightning.gifts](http://lightning.gifts/) service which supports this feature
might be a good place to start.

## Passwords and Security

We have added application-wide password protection that allows you to lock
your app and protect against unwanted access to your wallets. When enabled,
you will be required to enter your app password in order to open the app. This
password is currently separate from and in addition to your individual wallet
unlock passwords although in the future we plan to consolidate these so that
you can have a single password to remember. This setting is disabled by
default and can be enabled in the preferences page. We currently only support
this on Mac and Linux.

When setting passwords for the app or for your individual wallets you can now
click to show/hide the password in clear text so that you can verify that you
haven't made any typos. Additionally will ask you to enter the password twice
as a further safety net to help ensure that you haven't made any typos when
setting your password.

## Invoicing and Activity history

We now support lightning invoice fallback addresses. When enabled, a new on-
chain address will be generated and used set as the fallback address for each
new lightning invoice that you create. This feature is disabled by default and
can be enabled in the preferences page.

We've added some additional sanity checks to our invoice creation and payment
forms that provide instant feedback if you try to pay or create an invoice
that can not be paid due to network liquidity issues.

The main wallet activity list now also features infinite scrolling, ensuring
that you can view details of invoices and other activity items as far back in
time as you need to (previously we would only fetch and display up to 2500
invoices). We've also improved the filtering abilities so that you can be more
selective about which items you would like to see.

We've also added the ability to export a pdf receipt for your transactions
which we hope will be useful for merchants using Zap to control their store's
lightning nodes.

## Message signing

We now support message signing and message signature verification, accessible
from your wallet profile page. You can use this to sign messages with your
public key as well as to verify the authenticity of messages that have been
signed with another node's public key.

## Channel Management

In the channel management page, we now include the channel reserve amounts in
the channel detail view to help you better understand the current state of
your channels. We've also made a few minor adjustments to the header display
to make it easier to use the search and filter features.

## Other noteworthy changes

We have tidied up the interface a little and now show a skeleton loading
screen as your wallet loads. We hope that this will make the application feel
a little more responsive when connecting to remote nodes.

The seed restores form now features auto-complete which will suggest words
from the bip39 word list as you type. This greatly speeds up the time to enter
your 24 words seed phrase in the event that you need to restore from seed.

We've added error boundaries throughout the app so that in the event of a
critical error the application will no longer crash. Instead, we will show you
details of the error as well as a quick link that you can use to report the
error directly to us.

For any developers out there - you can now connect to and control lightning
nodes that are running on the bitcoin Regtest and Simnet networks.

A nice little nugget for our power users - all modal screens can now be closed
by pressing the escape key.

### Bug Fixes

  * **app:** store temp wallets in os tmpdir ([91060e0](https://github.com/LN-Zap/zap-desktop/commit/91060e002da99c05bd2d939d4dee62b8c734f6d1))
  * **checkbox:** react unctrolled component warning ([e6bc8d9](https://github.com/LN-Zap/zap-desktop/commit/e6bc8d9319b5e0409b30d6305b3eea43f3a35187)), closes [#2828](https://github.com/LN-Zap/zap-desktop/issues/2828)
  * **db:** wallet table sanitize routine ([02ec893](https://github.com/LN-Zap/zap-desktop/commit/02ec893e14447e0f11097a632b52b56f6524c624))
  * **modals:** crash when opening multiple modals ([a5ae322](https://github.com/LN-Zap/zap-desktop/commit/a5ae3227ce5d2c94a34ab65841450f5394c7f99f)), closes [#2823](https://github.com/LN-Zap/zap-desktop/issues/2823)
  * **modals:** move root modals higher in DOM tree ([34a20ed](https://github.com/LN-Zap/zap-desktop/commit/34a20edfd99a54a63c0ea29866ac574b18af76ee))
  * **ui:** add intl support to pdf invoice notifications ([6832e25](https://github.com/LN-Zap/zap-desktop/commit/6832e2532fd6cbf372a2a9bf97eaf0f16e686d7c))
  * **ui:** center seed confirm inputs ([72299f7](https://github.com/LN-Zap/zap-desktop/commit/72299f7442cfb281526a941e500065c7d20e69e2)), closes [#2730](https://github.com/LN-Zap/zap-desktop/issues/2730)
  * **ui:** ensure request form amount autofocus ([cb9ccb6](https://github.com/LN-Zap/zap-desktop/commit/cb9ccb6c9399d02e1e29c1c75f933758ab320b32))
  * **ui:** ensure select value from items list ([f3423d4](https://github.com/LN-Zap/zap-desktop/commit/f3423d432fd557e0dc05d7234a6c5aa5543626c5))
  * **ui:** make sure connection string visibility toggle is respected ([ba4bd3a](https://github.com/LN-Zap/zap-desktop/commit/ba4bd3ad0c66c3b05e5ab827d6f4ec3dec1f89f0)), closes [#2785](https://github.com/LN-Zap/zap-desktop/issues/2785)
  * **ui:** prevent Dropdown from overflowing bottom screen bound ([79a8efe](https://github.com/LN-Zap/zap-desktop/commit/79a8efe5ffd5c34bacd9cff001e2c64642424e61))
  * **ui:** prevent Dropmenu from overflowing bottom screen bound ([9017473](https://github.com/LN-Zap/zap-desktop/commit/9017473d68f8156f61d916a729dff4e8f01b2e21))
  * **ui:** prevent Select from overflowing bottom screen bound ([0c0e7e6](https://github.com/LN-Zap/zap-desktop/commit/0c0e7e6848a33292f592fd6a16025a1705a649fe))
  * **ui:** smaller processing button spinner ([0bab91a](https://github.com/LN-Zap/zap-desktop/commit/0bab91a87b50ee1516e356b6c2c1af3eb9b8f193))
  * **ui:** use gray color for input placeholder ([97aabfd](https://github.com/LN-Zap/zap-desktop/commit/97aabfd7cd425bdef5da87a0ee849c0248ce6d3d))
  * **wallet:** ensure address generation works ([64af2da](https://github.com/LN-Zap/zap-desktop/commit/64af2da015c32bfc974106d64dd97fbbeb2b43d6))
  * issue with adding new LN invoice ([74c5a08](https://github.com/LN-Zap/zap-desktop/commit/74c5a087f0cbf08ee4c168f1e245eb19de65d61a))
  * add App specific modalstack ([8b7d3b2](https://github.com/LN-Zap/zap-desktop/commit/8b7d3b2f491199f6b67240f546fe563a8011fb24))
  * **devtools:** don't mutate frozen object ([5f886ec](https://github.com/LN-Zap/zap-desktop/commit/5f886ecdb5c65a6a0660db38aa2fe846dba6dacb))
  * **grpc:** ensure that protobuf has Long support ([810c343](https://github.com/LN-Zap/zap-desktop/commit/810c343614795dd732a4ea8e97fe643fb73c97a1))
  * **grpc:** remove redundant openChannel.data and closeChannel.data subs ([48b71b0](https://github.com/LN-Zap/zap-desktop/commit/48b71b073cb91c1a33bc3ef83a0482e6e04d1ae4)), closes [#2920](https://github.com/LN-Zap/zap-desktop/issues/2920)
  * **i18n:** add missing memo translation ([f89cda9](https://github.com/LN-Zap/zap-desktop/commit/f89cda9a6f605fcbe72125c1192e0521c2ee67b7))
  * **i18n:** change open channel status label to "online" ([5dbbe1c](https://github.com/LN-Zap/zap-desktop/commit/5dbbe1c4ab1f2fe763587469115ef36891af4ceb)), closes [#3045](https://github.com/LN-Zap/zap-desktop/issues/3045)
  * **i18n:** enable jsx-no-hardcoded-content lint rule ([de51b9d](https://github.com/LN-Zap/zap-desktop/commit/de51b9d897620bb1d5068c42b6351ee6560306d3)), closes [#3065](https://github.com/LN-Zap/zap-desktop/issues/3065)
  * **i18n:** externalize hardcoded UI strings into localization files ([faf6fa3](https://github.com/LN-Zap/zap-desktop/commit/faf6fa3321aa936ebf2f91fe2ee28458474ac367)), closes [#3065](https://github.com/LN-Zap/zap-desktop/issues/3065)
  * **i18n:** extract pay form amount labels into own localizable string ([c74ebef](https://github.com/LN-Zap/zap-desktop/commit/c74ebef49a2c689eff9636e908fce0933aae4612)), closes [#3045](https://github.com/LN-Zap/zap-desktop/issues/3045)
  * **i18n:** remove hardcoded string from connection details view ([e876168](https://github.com/LN-Zap/zap-desktop/commit/e8761687825128809d9a8f828458117fb9fded7c)), closes [#3045](https://github.com/LN-Zap/zap-desktop/issues/3045)
  * **i18n:** replace hardcoded "Channels" dropdown title ([ceafccf](https://github.com/LN-Zap/zap-desktop/commit/ceafccff17b4041be93a460643f6a31c9b3ef871)), closes [#3045](https://github.com/LN-Zap/zap-desktop/issues/3045)
  * **i18n:** replace hardcoded labels in pay form ([01563df](https://github.com/LN-Zap/zap-desktop/commit/01563df8d7a343c7d035cccfedf3d421f7c0aef5)), closes [#3045](https://github.com/LN-Zap/zap-desktop/issues/3045)
  * **lint:** refactor eqeqeq issues ([b791b2f](https://github.com/LN-Zap/zap-desktop/commit/b791b2fc99ac65da6f72395d34760dc1a1b78954))
  * **lnurl:** handle lnurl processing errors ([a7e5e0d](https://github.com/LN-Zap/zap-desktop/commit/a7e5e0d2c4b82f936413a3683daa5e9ab2df8d80))
  * **onboarding:** retain wallet addresses in state ([9742591](https://github.com/LN-Zap/zap-desktop/commit/9742591e116c5e3c9ba533fd32f02c9e0eca2e33)), closes [#3182](https://github.com/LN-Zap/zap-desktop/issues/3182)
  * **scheduler:** correctly search function tasks ([138ae63](https://github.com/LN-Zap/zap-desktop/commit/138ae63a47644ca1fa9993b2893a09e405fbc3a7))
  * **ui:** add ability to submit onboarding steps with Return key ([9b05d5e](https://github.com/LN-Zap/zap-desktop/commit/9b05d5e284240cac416c4fe248cc7bc46d889ef0)), closes [#3172](https://github.com/LN-Zap/zap-desktop/issues/3172)
  * **ui:** add error handler for create invoice ([dec8bfe](https://github.com/LN-Zap/zap-desktop/commit/dec8bfeb02c53b560acb5ca415cc83d1bf05832e))
  * **ui:** add margins to labels in wallet settings and node info panel ([4416f62](https://github.com/LN-Zap/zap-desktop/commit/4416f62958a1c3d42d6f031ff51a9cf5ff7077a5)), closes [#3046](https://github.com/LN-Zap/zap-desktop/issues/3046)
  * **ui:** add password field tooltip ([a94fb9d](https://github.com/LN-Zap/zap-desktop/commit/a94fb9dd4dc3132eb1e8274c8d682842fa76a81a))
  * **ui:** add scroll to onboarding screen if needed ([12cd50a](https://github.com/LN-Zap/zap-desktop/commit/12cd50a1fce7556b573c9a915010059d1756b9f1))
  * **ui:** center align dialog header headings ([9451bce](https://github.com/LN-Zap/zap-desktop/commit/9451bce7251f6814488aca1c0d6673987b6e4f40)), closes [#3046](https://github.com/LN-Zap/zap-desktop/issues/3046)
  * **ui:** center failed payment error modal dialog ([b08353c](https://github.com/LN-Zap/zap-desktop/commit/b08353c116779019752207fab16e3a20cb569608)), closes [#3183](https://github.com/LN-Zap/zap-desktop/issues/3183)
  * **ui:** center WalletCreate content ([c8795b0](https://github.com/LN-Zap/zap-desktop/commit/c8795b0e5f12c4207d190638eae89076dd3b5881)), closes [#2918](https://github.com/LN-Zap/zap-desktop/issues/2918)
  * **ui:** center-align wallet create card headers ([7db59a9](https://github.com/LN-Zap/zap-desktop/commit/7db59a977705c0b40ffe69621a5f8975e9144654)), closes [#3046](https://github.com/LN-Zap/zap-desktop/issues/3046)
  * **ui:** close channel modal on channel open completion ([56fcafe](https://github.com/LN-Zap/zap-desktop/commit/56fcafe092f4db9694216655f5ad8c56b557094a))
  * **ui:** correct expire date for invoices with far future expiry ([0121b5d](https://github.com/LN-Zap/zap-desktop/commit/0121b5d9ec480e8e86a1305805b6a1bdaf1f272d)), closes [#3144](https://github.com/LN-Zap/zap-desktop/issues/3144)
  * **ui:** correctly isWinPlatformSupported flag ([b8867b9](https://github.com/LN-Zap/zap-desktop/commit/b8867b998ba3c556825bbebccf016ed0a7facb3d))
  * **ui:** crash when trying to save remote node updates ([ac4936a](https://github.com/LN-Zap/zap-desktop/commit/ac4936a341918cf75986117b52d7c3338d8908e8))
  * **ui:** disable app password on windows platform ([31d1695](https://github.com/LN-Zap/zap-desktop/commit/31d1695e35e9f1e05ad6013b0df4554d0c785ce6))
  * **ui:** disable sign message functionality for local wallets ([d05c6ef](https://github.com/LN-Zap/zap-desktop/commit/d05c6ef425ebcfd205ddb49064ded1ac86023247))
  * **ui:** don't disable sent filter after sending payment ([32cb6c9](https://github.com/LN-Zap/zap-desktop/commit/32cb6c93cce6e6e7a9937cd21110b290394e8a31))
  * **ui:** don't open channel management modal when not needed ([2dd0f10](https://github.com/LN-Zap/zap-desktop/commit/2dd0f10f0bbbdd95b964899cdc23b84e68d5fe48)), closes [#3035](https://github.com/LN-Zap/zap-desktop/issues/3035)
  * **ui:** ensure failed payments marked as failed ([c734b87](https://github.com/LN-Zap/zap-desktop/commit/c734b87f9b5b7e5f82962f89ae1863055938f610)), closes [#3142](https://github.com/LN-Zap/zap-desktop/issues/3142)
  * **ui:** ensure onboarding dialogs on top ([14ebf05](https://github.com/LN-Zap/zap-desktop/commit/14ebf057c552e2d34fd32b2a49addd4c1dc410f3)), closes [#3119](https://github.com/LN-Zap/zap-desktop/issues/3119)
  * **ui:** ensure pay form amount autofocus ([07c6d7e](https://github.com/LN-Zap/zap-desktop/commit/07c6d7e73f8db628be84eaa3717b14f0be3fd33c))
  * **ui:** incorrect open btn placement in OpenDialogInput errorneus state ([d12b5c6](https://github.com/LN-Zap/zap-desktop/commit/d12b5c611fdd8ab04bba607206f4fb5ff10e430c)), closes [#2987](https://github.com/LN-Zap/zap-desktop/issues/2987)
  * **ui:** keep autocomplete within screen bounds ([a2cec09](https://github.com/LN-Zap/zap-desktop/commit/a2cec0923bbd0e300ae4e231fe743cf17ee7d611))
  * **ui:** lightning invoice validation in Pay view ([9aa6125](https://github.com/LN-Zap/zap-desktop/commit/9aa6125510734cd00d825763f4f2ed376a40297d))
  * **ui:** make sure activity filter label doesn't wrap on two lines ([71e81ca](https://github.com/LN-Zap/zap-desktop/commit/71e81ca6e6ed2441544c3eb810809266be58df0b)), closes [#3046](https://github.com/LN-Zap/zap-desktop/issues/3046)
  * **ui:** make sure crypto amount values stay on one line ([170fd90](https://github.com/LN-Zap/zap-desktop/commit/170fd905d8a0f1c816b13addc0f70459c6c63a0e)), closes [#3065](https://github.com/LN-Zap/zap-desktop/issues/3065)
  * **ui:** next button state after going back in Pay form ([938ebdb](https://github.com/LN-Zap/zap-desktop/commit/938ebdb9abfd92bb6f0a7f8d054a0f8dcd7ed95e)), closes [#3176](https://github.com/LN-Zap/zap-desktop/issues/3176)
  * **ui:** no form error when form is empty ([d029992](https://github.com/LN-Zap/zap-desktop/commit/d0299929d897116fc12944afa056b0f46dfb9701)), closes [#3016](https://github.com/LN-Zap/zap-desktop/issues/3016)
  * **ui:** only focus elements when they receive it through tab ([f9b5da1](https://github.com/LN-Zap/zap-desktop/commit/f9b5da1b2f3bfb909a6bd5d042aefd5c748d11d3)), closes [#3127](https://github.com/LN-Zap/zap-desktop/issues/3127)
  * **ui:** open dialog inputs ([ef5e6ff](https://github.com/LN-Zap/zap-desktop/commit/ef5e6fff20add1f5ea4fe1d9ae1f0c5e4ea8de0e))
  * **ui:** remove sending avtivity from sent filter ([79e471e](https://github.com/LN-Zap/zap-desktop/commit/79e471eee68ea576f96a216f8012c3154d1da894))
  * **ui:** restore RadioGroup label mb ([5427353](https://github.com/LN-Zap/zap-desktop/commit/5427353097faeb994f50338ce318c0fa81781ef4)), closes [#2919](https://github.com/LN-Zap/zap-desktop/issues/2919)
  * **ui:** show all activity by default ([74d6cab](https://github.com/LN-Zap/zap-desktop/commit/74d6cab94080e0f18a0e21f65f794ecd0fe2f1b6))
  * **ui:** trim LN prs and onchain addresses in LightningInvoiceInput ([44a028f](https://github.com/LN-Zap/zap-desktop/commit/44a028f1225d426d0a5aa12367bb9fd3d6711119))
  * **ui:** update misleading wallet unlock description ([9625116](https://github.com/LN-Zap/zap-desktop/commit/9625116d6a47616907e842bffd215f410a7da0bb)), closes [#2978](https://github.com/LN-Zap/zap-desktop/issues/2978)
  * **ui:** update settings menu icon ([cb90c01](https://github.com/LN-Zap/zap-desktop/commit/cb90c0168e17b11a51dd1af537634194c0fe873c))
  * **ui:** update user profile menu icon ([35b7a40](https://github.com/LN-Zap/zap-desktop/commit/35b7a40a6faf44afc9aa5ee576130c462105d338))
  * **wallet:** ensure transaction sending error handled ([b1722c6](https://github.com/LN-Zap/zap-desktop/commit/b1722c662e44fd0ba777387c1ddbefb2d7ab2576))
  * **wallet:** factor sent and received in channel capacity ([3304ccb](https://github.com/LN-Zap/zap-desktop/commit/3304ccb12354bd7ca36d1412599f7fadcd071ac6))
  * add Home error boundary ([919be24](https://github.com/LN-Zap/zap-desktop/commit/919be24254c05048b69a1bad3a7ed274b7b079cb))
  * add intl support to notifications ([7978ad8](https://github.com/LN-Zap/zap-desktop/commit/7978ad8487dff138074b16c90ccda3111cbda93a))
  * add intl support to system notifications ([369188e](https://github.com/LN-Zap/zap-desktop/commit/369188e945d8112ccdd53925de56c7b4c790e469))
  * add Onboarding error boundary ([2a7e559](https://github.com/LN-Zap/zap-desktop/commit/2a7e5599f183940936788122610469dab915dd6a))
  * add Syncing error boundary ([5cfc725](https://github.com/LN-Zap/zap-desktop/commit/5cfc725001d7beea6475b5f477231bb41b4cb34b))
  * cornercase of initial sync status polling ([1618567](https://github.com/LN-Zap/zap-desktop/commit/1618567d2a93fc17c4a010e8e07bc89a3479d564))
  * dropmenu arrow layout ([de2ced7](https://github.com/LN-Zap/zap-desktop/commit/de2ced7f1a031f2e92be9a28a069baaac40fad88))
  * ensure max and min fees are set or null ([acfc2c8](https://github.com/LN-Zap/zap-desktop/commit/acfc2c8f1e4ccf3146ccca80b6a747dd510d6738))
  * **deps:** update dependency rebass to v3.2.2 ([c20b60c](https://github.com/LN-Zap/zap-desktop/commit/c20b60cffc8caa5c2bd1ebf8b272cd3b8499e2a3))
  * **ui:** use static positioning for dialogs ([d69015e](https://github.com/LN-Zap/zap-desktop/commit/d69015ef36af0eab62316c07db9fa44f470a982d))
  * **wallet:** correctly handle protocol links on windows ([11b7106](https://github.com/LN-Zap/zap-desktop/commit/11b7106c7ac208d9750489e0de74fd0557502a45))
  * **wallet:** improve address generation ([579554e](https://github.com/LN-Zap/zap-desktop/commit/579554e4f3c26f33026b9c6b4786657d0e0fd47e)), closes [#3116](https://github.com/LN-Zap/zap-desktop/issues/3116)
  * **wallet:** increase fee limit on payment retries ([b14d785](https://github.com/LN-Zap/zap-desktop/commit/b14d785d37ba5a803e851563146d272f021473fa))
  * **wallet:** no lndconnect links for tmp wallets ([c9f80d9](https://github.com/LN-Zap/zap-desktop/commit/c9f80d9647be1fece3e5968c8298526ec636ab0b))
  * extract-messages issue introduced by [`7b6a796`](https://github.com/LN-Zap/zap-desktop/commit/7b6a7966413dc72e10bc873fb56982dcc8fa3310) ([d340171](https://github.com/LN-Zap/zap-desktop/commit/d3401716170f8051a62d08ba7096ba46f212ca80))
  * rebass imports ([cdfe62e](https://github.com/LN-Zap/zap-desktop/commit/cdfe62e001ac0507ab3037c0acccff2730012c7f))
  * store font files locally ([dc2f485](https://github.com/LN-Zap/zap-desktop/commit/dc2f4859ed08ad036f922004bed16d7e49e886aa)), closes [#2984](https://github.com/LN-Zap/zap-desktop/issues/2984)
  * **ui:** add support for intl in reducers ([4bbd0a3](https://github.com/LN-Zap/zap-desktop/commit/4bbd0a37923d89216a3233cb418a9650a4beaa40))
  * **ui:** disable html5 form validation ([fa19987](https://github.com/LN-Zap/zap-desktop/commit/fa199872405badaa3ae164dc2ddba65009111f95))
  * **ui:** display correct channel count when search or filter is applied ([187dd5c](https://github.com/LN-Zap/zap-desktop/commit/187dd5c02a4ba476a0f4c7f7ce99768eab5a50a1))
  * **ui:** ensure fiat and crypto inputs in agroup are always updated ([537c447](https://github.com/LN-Zap/zap-desktop/commit/537c447afb0e8a44569cbae626ddbf049d5daa4b)), closes [#2602](https://github.com/LN-Zap/zap-desktop/issues/2602)
  * **ui:** ensure notifications are visible when modal is active ([9f07a74](https://github.com/LN-Zap/zap-desktop/commit/9f07a7487f24f3510fdafa61c427e06e50c28f70))
  * **ui:** prevent Toggle from selecting text when clicked ([8d15568](https://github.com/LN-Zap/zap-desktop/commit/8d155688c88443475cf97c80633085a8907e063a))
  * **ui:** update fees when send all is used ([29e4b81](https://github.com/LN-Zap/zap-desktop/commit/29e4b81a1b04aab3ec0a342e6b954aa959b87f06))
  * **ui:** use desc instead of placeholder in invoice input ([cd4097a](https://github.com/LN-Zap/zap-desktop/commit/cd4097ac23aed68c5674af14a8855028ada320f9))
  * **wallet:** present correct fee when no route ([8b0a351](https://github.com/LN-Zap/zap-desktop/commit/8b0a351f52b8fe251ee0a84528ce649c063fb75a)), closes [#3154](https://github.com/LN-Zap/zap-desktop/issues/3154)
  * return result from producer ([31830ad](https://github.com/LN-Zap/zap-desktop/commit/31830adb2b53cfb3dd97dcb246e5ce254d7d3cb6))
  * update channel search input if state changes ([cb7c69d](https://github.com/LN-Zap/zap-desktop/commit/cb7c69dafe0a962f16aad8b7d48edbc6cc344987))
  * update download icon in TransactionModal ([c5526c0](https://github.com/LN-Zap/zap-desktop/commit/c5526c0374f622bcd11eaa1a65a109ab8d3ef5d3))
  * verify message box layout ([e33dab0](https://github.com/LN-Zap/zap-desktop/commit/e33dab0c133086d387f9baa05eecb27bb5418fe2))

### Features

  * **app:** basic password authentication ([ef9e1ec](https://github.com/LN-Zap/zap-desktop/commit/ef9e1eced6d0fdb0a114830b833dc6332e779185)), closes [#1387](https://github.com/LN-Zap/zap-desktop/issues/1387)
  * **autopay:** auto pay invoices based on autopay config ([0726a3a](https://github.com/LN-Zap/zap-desktop/commit/0726a3a0874aa8955ddbf2710d0c9945439aa639))
  * **autopay:** show system notification when doing autopay ([a3f30f4](https://github.com/LN-Zap/zap-desktop/commit/a3f30f4ceb269791a5b14c263672d00a6847bc97))
  * **lnd:** ability to enforce connection only to whitelisted peers ([480f5f4](https://github.com/LN-Zap/zap-desktop/commit/480f5f49d4b054cfc8632d413bda9d35c77cef31)), closes [#3025](https://github.com/LN-Zap/zap-desktop/issues/3025)
  * **ui:** add "show/hide password" buttons ([e1435a1](https://github.com/LN-Zap/zap-desktop/commit/e1435a194f46d324cb92caac1e383e4440b8cd57)), closes [#2731](https://github.com/LN-Zap/zap-desktop/issues/2731)
  * **ui:** add ability to configure neutrino nodes for local wallets ([eb9aee5](https://github.com/LN-Zap/zap-desktop/commit/eb9aee53b43f72304abf622b2facae8993839e2c))
  * **ui:** add ability to restore neutrino url defaults ([b960781](https://github.com/LN-Zap/zap-desktop/commit/b96078184f7e43118f80ac6a6ffa57e39038356b))
  * **ui:** add ability to specify fallback address in LN invoices ([5960463](https://github.com/LN-Zap/zap-desktop/commit/596046350f0d920b3c0fb2fa65032d7d8b54f822)), closes [#2021](https://github.com/LN-Zap/zap-desktop/issues/2021)
  * **ui:** add autosuggest for seed recovery ([c9c175d](https://github.com/LN-Zap/zap-desktop/commit/c9c175dc687c732848e3931835cdc839ea32deff)), closes [#2765](https://github.com/LN-Zap/zap-desktop/issues/2765)
  * **ui:** add fallback address to RequestSummary ([8095268](https://github.com/LN-Zap/zap-desktop/commit/80952683e4b71a648b8d5e267bfc952f122b225d))
  * **ui:** add lnurl withdraw prompt setting ([f451eda](https://github.com/LN-Zap/zap-desktop/commit/f451eda1b06aef846ae4f947410d2d91ced8a14b))
  * **ui:** add password confirmation input to set password dialog ([1a7ce72](https://github.com/LN-Zap/zap-desktop/commit/1a7ce72e7ddf4222d519b04ef689881bff7f946d)), closes [#2969](https://github.com/LN-Zap/zap-desktop/issues/2969)
  * **ui:** add PasswordInput component and use it ([b311fa9](https://github.com/LN-Zap/zap-desktop/commit/b311fa98ef4ec8cff3f05717c28180493f587633))
  * **ui:** add sign message capability ([0657932](https://github.com/LN-Zap/zap-desktop/commit/06579324e45366bd8cd0e404bd2df24c18b94105)), closes [#2023](https://github.com/LN-Zap/zap-desktop/issues/2023)
  * **ui:** add verify message capability ([ec37abb](https://github.com/LN-Zap/zap-desktop/commit/ec37abbac1d9c7456748c88a70776d83f40b7d85))
  * **ui:** allow changing and toggling app password via dialogs ([892d592](https://github.com/LN-Zap/zap-desktop/commit/892d592621bbdc6ff637e1e524ca1b2e783277e0))
  * **ui:** close dialogs with Escape key ([45e771f](https://github.com/LN-Zap/zap-desktop/commit/45e771f8afc9309a9c77410a8425a36d42a1954a)), closes [#2677](https://github.com/LN-Zap/zap-desktop/issues/2677)
  * **ui:** confirm password on wallet create ([11f03c3](https://github.com/LN-Zap/zap-desktop/commit/11f03c3c6ef12b84bc6c6ef38a5dd73773e3fafc))
  * **ui:** display non-mainnet node network name ([a637467](https://github.com/LN-Zap/zap-desktop/commit/a637467b789ace8c53008e270d017da6a5238c63))
  * **ui:** highlight activity filter icon in non default state ([1757bf5](https://github.com/LN-Zap/zap-desktop/commit/1757bf573f60fd1a081e3ac877acfc29796e5455))
  * **ui:** implement activity item error dialog ([c3b55ba](https://github.com/LN-Zap/zap-desktop/commit/c3b55ba0dd2d52df4d4eaba28abf83b9670c6a51)), closes [#2580](https://github.com/LN-Zap/zap-desktop/issues/2580)
  * **ui:** implement better activity filtering ([52d6a6b](https://github.com/LN-Zap/zap-desktop/commit/52d6a6b2e1fd013942389d36bf26f7a54944b0ad)), closes [#2278](https://github.com/LN-Zap/zap-desktop/issues/2278)
  * **ui:** implement better channels filtering ([86b57e8](https://github.com/LN-Zap/zap-desktop/commit/86b57e89f9240479bd6530b8dc26d06254601895))
  * **ui:** implement lnurl withdrawal request handling ([4cc1419](https://github.com/LN-Zap/zap-desktop/commit/4cc1419b92cb8851f9f0c50a0bced539b0fb369d))
  * **ui:** implement neutrino nodes sanity check ([6e06104](https://github.com/LN-Zap/zap-desktop/commit/6e061041706c2d47fd04cedb2ffc73456782f940))
  * **ui:** implement skeleton loading screen ([d1d5432](https://github.com/LN-Zap/zap-desktop/commit/d1d54321639c5a7b59dbb0cd92af259beca5862d)), closes [#2654](https://github.com/LN-Zap/zap-desktop/issues/2654)
  * **ui:** implement unexpected error UI ([e0631f7](https://github.com/LN-Zap/zap-desktop/commit/e0631f7239366cf3c6378b6e671b74ad242ee718))
  * **ui:** prefill gh uncaught error issues ([be85bf4](https://github.com/LN-Zap/zap-desktop/commit/be85bf4b55862deae2639c53643b1f5fcb610ff0)), closes [#1828](https://github.com/LN-Zap/zap-desktop/issues/1828)
  * **ui:** prohibit login if secure storage is not available ([56f2169](https://github.com/LN-Zap/zap-desktop/commit/56f2169d0edd2308909dba3a1f4b4345c2b163de))
  * **ui:** set password from preferences page ([73422cd](https://github.com/LN-Zap/zap-desktop/commit/73422cd9483dd443e9081c958f318b2df8c92d1f))
  * **ui:** show channel reserve amount in channel details view ([dbb0581](https://github.com/LN-Zap/zap-desktop/commit/dbb058188c6f5ad8d2e95873f4167bd8d96c01d5)), closes [#2910](https://github.com/LN-Zap/zap-desktop/issues/2910)
  * **ui:** show memo in sent details if available ([5880062](https://github.com/LN-Zap/zap-desktop/commit/58800622f10481d05fe34de75d0bd39c9f29f513)), closes [#2715](https://github.com/LN-Zap/zap-desktop/issues/2715)
  * **ui:** show number of confs for incoming onchain txs in activity list ([191ca76](https://github.com/LN-Zap/zap-desktop/commit/191ca76d49381e1f29628e5468efd3e844fe79e3)), closes [#1685](https://github.com/LN-Zap/zap-desktop/issues/1685)
  * **ui:** warn of potential liquidity issues when creating an invoice ([5fa0e5a](https://github.com/LN-Zap/zap-desktop/commit/5fa0e5a8bc28524a4dbc49456baf524cfec33aaf))
  * **ui:** warn of potential liquidity issues when paying an invoice ([7e02644](https://github.com/LN-Zap/zap-desktop/commit/7e02644defab6e8a183e938db6a55d988d0319ec))
  * **wallet:** add ability to export on-chain tx invoices ([8976efb](https://github.com/LN-Zap/zap-desktop/commit/8976efb4607e1d99830d67052168b87a21d988a6)), closes [#1290](https://github.com/LN-Zap/zap-desktop/issues/1290)
  * **wallet:** bolt11 invoices encoded in bip21 uri ([1ebdb98](https://github.com/LN-Zap/zap-desktop/commit/1ebdb98b0d2580bcc82474697e0da24bf928065a)), closes [#200](https://github.com/LN-Zap/zap-desktop/issues/200)
  * **wallet:** regtest support ([56e7e26](https://github.com/LN-Zap/zap-desktop/commit/56e7e2666267c5f19b25f36a1642b5ee5f423f43))
  * **wallet:** simnet support ([dec20f6](https://github.com/LN-Zap/zap-desktop/commit/dec20f6223e7f844e106ce35baf7b42cd6c26795))
  * add LN invoice creation date to summary modal ([9802ddd](https://github.com/LN-Zap/zap-desktop/commit/9802ddd0468f57dcb06584c6751340c2c09e9dd8))
  * improve channel search header ([ea69bf9](https://github.com/LN-Zap/zap-desktop/commit/ea69bf9e8d9f2b0c6ffc0c0764ef2adc3d4b5373))

### Performance Improvements

  * don't fetch onchain fees when paying LN invoice ([d346f9f](https://github.com/LN-Zap/zap-desktop/commit/d346f9fc0f3f185f9b6d0335c2006816ea4f0fcb)), closes [#3175](https://github.com/LN-Zap/zap-desktop/issues/3175)
  * **wallet:** prevent excessive getInfo calls ([0062535](https://github.com/LN-Zap/zap-desktop/commit/0062535c5cea9a745741ee32681b0b20d0b48044))
  * don't re-render SeedConfirm on mount ([b9a54e2](https://github.com/LN-Zap/zap-desktop/commit/b9a54e2693fa1a7427a1c5bad5406437ad43eb5f)), closes [#2792](https://github.com/LN-Zap/zap-desktop/issues/2792)
  * only update known/add fresh txs when polling ([09454b6](https://github.com/LN-Zap/zap-desktop/commit/09454b6944371d8ada1164aab946921442edeb39))
  * update only sending requests on completion ([d657666](https://github.com/LN-Zap/zap-desktop/commit/d657666c559bfa11f9909094e943b7c7e0dd5280))
  * **activity:** implement activity list pagination ([f994d04](https://github.com/LN-Zap/zap-desktop/commit/f994d0433b6c5f15aa996f9aa6ca4fe6a12a9a0e)), closes [#2404](https://github.com/LN-Zap/zap-desktop/issues/2404)
  * simplify activity list renderer ([01584f9](https://github.com/LN-Zap/zap-desktop/commit/01584f9cbc769c2f1ebef4c35ee4d4f5d6ba65a7))

### Changelog

The full list of changes since 0.5.4-beta can be found here:

[`v0.5.4-beta...v0.6.1-beta`](https://github.com/LN-Zap/zap-
desktop/compare/v0.5.4-beta...v0.6.1-beta)

## Verifying the Release

Please refer to [our documentation](https://github.com/LN-Zap/zap-
desktop#documentation) for [instructions on how to verify the
release](https://github.com/LN-Zap/zap-
desktop/blob/master/docs/SIGNATURES.md).

### Assets

11

  * [ latest-linux.yml ](/LN-Zap/zap-desktop/releases/download/v0.6.1-beta/latest-linux.yml)

399 Bytes

  * [ latest-mac.yml ](/LN-Zap/zap-desktop/releases/download/v0.6.1-beta/latest-mac.yml)

524 Bytes

  * [ latest.yml ](/LN-Zap/zap-desktop/releases/download/v0.6.1-beta/latest.yml)

347 Bytes

  * [ Zap-linux-x86_64-v0.6.1-beta.AppImage ](/LN-Zap/zap-desktop/releases/download/v0.6.1-beta/Zap-linux-x86_64-v0.6.1-beta.AppImage)

87.1 MB

  * [ Zap-mac-v0.6.1-beta.dmg ](/LN-Zap/zap-desktop/releases/download/v0.6.1-beta/Zap-mac-v0.6.1-beta.dmg)

87.5 MB

  * [ Zap-mac-v0.6.1-beta.dmg.blockmap ](/LN-Zap/zap-desktop/releases/download/v0.6.1-beta/Zap-mac-v0.6.1-beta.dmg.blockmap)

94.6 KB

  * [ Zap-mac-v0.6.1-beta.zip ](/LN-Zap/zap-desktop/releases/download/v0.6.1-beta/Zap-mac-v0.6.1-beta.zip)

84.9 MB

  * [ Zap-win-v0.6.1-beta.exe ](/LN-Zap/zap-desktop/releases/download/v0.6.1-beta/Zap-win-v0.6.1-beta.exe)

63.3 MB

  * [ Zap-win-v0.6.1-beta.exe.blockmap ](/LN-Zap/zap-desktop/releases/download/v0.6.1-beta/Zap-win-v0.6.1-beta.exe.blockmap)

68.6 KB

  * [ Source code (zip) ](/LN-Zap/zap-desktop/archive/refs/tags/v0.6.1-beta.zip)

  * [ Source code (tar.gz) ](/LN-Zap/zap-desktop/archive/refs/tags/v0.6.1-beta.tar.gz)

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

