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
desktop%2Freleases%2Ftag%2Fv0.7.0-beta)

[ Sign up
](/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-
name%3E%2F%3Crepo-name%3E%2Freleases%2Fshow&source=header-repo&source_repo=LN-
Zap%2Fzap-desktop)

{{ message }}

##  [LN-Zap](/LN-Zap) / **[zap-desktop](/LN-Zap/zap-desktop) ** Public

  * [ Notifications ](/login?return_to=%2FLN-Zap%2Fzap-desktop)
  * [ Fork 222 ](/login?return_to=%2FLN-Zap%2Fzap-desktop)
  * [ Star  1.2k ](/login?return_to=%2FLN-Zap%2Fzap-desktop)

  * [ Code ](/LN-Zap/zap-desktop/tree/v0.7.0-beta)
  * [ Issues 124 ](/LN-Zap/zap-desktop/issues)
  * [ Pull requests 22 ](/LN-Zap/zap-desktop/pulls)
  * [ Actions ](/LN-Zap/zap-desktop/actions)
  * [ Security ](/LN-Zap/zap-desktop/security)
  * [ Insights ](/LN-Zap/zap-desktop/pulse)

More

  * [ Code ](/LN-Zap/zap-desktop/tree/v0.7.0-beta)
  * [ Issues ](/LN-Zap/zap-desktop/issues)
  * [ Pull requests ](/LN-Zap/zap-desktop/pulls)
  * [ Actions ](/LN-Zap/zap-desktop/actions)
  * [ Security ](/LN-Zap/zap-desktop/security)
  * [ Insights ](/LN-Zap/zap-desktop/pulse)

  1. [Releases](/LN-Zap/zap-desktop/releases)
  2. [ v0.7.0-beta ](/LN-Zap/zap-desktop/releases/tag/v0.7.0-beta)

__Compare

Choose a tag to compare

Could not load tags

Nothing to show

[ {{ refName }} default ](/LN-Zap/zap-desktop/compare/{{ urlEncodedRefName
}}...v0.7.0-beta)

[View all tags](/LN-Zap/zap-desktop/tags)

# Zap 0.7.0 Beta

![@mrfelton](https://avatars.githubusercontent.com/u/200251?s=40&v=4)
[mrfelton](/mrfelton) released this

* [ 262 commits ](/LN-Zap/zap-desktop/compare/v0.7.0-beta...master) to master since this release 

[ v0.7.0-beta  ](/LN-Zap/zap-desktop/tree/v0.7.0-beta)

[ `5d2ad32` ](/LN-Zap/zap-
desktop/commit/5d2ad32857f059acdf439a436ce26dc9257702ec)

__Compare

Choose a tag to compare

Could not load tags

Nothing to show

[ {{ refName }} default ](/LN-Zap/zap-desktop/compare/{{ urlEncodedRefName
}}...v0.7.0-beta)

[View all tags](/LN-Zap/zap-desktop/tags)

## Release notes

This release contains several new features including support for lnd v0.10,
keysend, multi part payment, payment probes, Tor and more. As usual, this
release also contains a number of optimisations and bug fixes.

## LND 0.10

We now ship with [LND
0.10.2-beta](https://github.com/lightningnetwork/lnd/releases/tag/v0.10.2-beta)
which delivers many improvements and enhancements. We continue to support
connecting to external LND nodes that are running prior versions of LND,
though we encourage all users to update their nodes.

## Payment Probes

We now use payment probes to get an accurate fee estimate prior to making a
lightning payment.

This is done by sending a payment with an unknown payment hash and inspecting
the returned failure. If it originates from the final destination, the route
is deemed to be valid.

Following through with the real payment after a successful probe is very
likely to succeed and by using the route returned from the probe we can be
sure of the exact route and associated fees that will be used.

## Multi Part Payments (MPP)

If we are unable to send your payment using a single route we will try to
leverage MPP - splitting the payment over multiple parts - in order to improve
chances of delivery.

## Spontaneous Payments (keysend)

We now support keysend payments. This lets you send Lightning payments without
the need for the recipient to provide you with a bolt11 invoice first. All you
need is the pubkey of the node you want to send to.

Using keysend you can send any amount of sats, any number of times to the same
address (within your channel limits). The node pubkey acts like like a static
reusable receive address.

## gRPC over Tor

In this release, we have added support for connecting to your LND node's gRPC
interface over [Tor](https://www.torproject.org/) (via a `.onion` address)
which enables you to connect to and control your node without exposing it to
the internet.

## LNURL Channel

As part of our continued rollout of the [LNURL
protocol](https://github.com/btcontract/lnurl-rfc) we've added support for
[`lnurl-channel`](https://github.com/btcontract/lnurl-rfc/blob/master/lnurl-
channel.md) which makes it possible to use services like
[LNBIG](https://lnbig.com/) or [Bitrefill's
Thor](https://www.bitrefill.com/thor) to request inbound liquidity without
worrying about manually opening channels.

This adds to our existing support for [`lnurl-
withdraw`](https://github.com/btcontract/lnurl-rfc/blob/master/lnurl-
withdraw.md) which enables you to quickly and easily withdraw funds to your
wallet without needing to create an invoice.

## Hold Invoices

Hodl Invoices allow you to have manual control over the invoice settlement
process - once payment has been received you can choose to accept or cancel
back the payment.

### Bug Fixes

  * **app:** ensure app restarts during autoupdate ([8346450](https://github.com/LN-Zap/zap-desktop/commit/834645025cb83e95ed3de5c04076d6cf534bb5c6)), closes [#3198](https://github.com/LN-Zap/zap-desktop/issues/3198)
  * **app:** whitelist docs.zaphq.io domain ([0de7709](https://github.com/LN-Zap/zap-desktop/commit/0de77099061718a0c69e6256a8e4f93cf90a5f5c))
  * **backup:** set user-agent to `Chrome` for google oauth ([d9945a5](https://github.com/LN-Zap/zap-desktop/commit/d9945a520e9b5aa4040962ee15ff7287ecca8dc2)), closes [#3342](https://github.com/LN-Zap/zap-desktop/issues/3342)
  * **grpc:** use grpc error details if available ([c278f3a](https://github.com/LN-Zap/zap-desktop/commit/c278f3a8743654032d581de58e97f10ee42980f3))
  * **lnd:** correctly set initWallet props on restore ([22b92e9](https://github.com/LN-Zap/zap-desktop/commit/22b92e994855c60f55f0d67b84ca90703732b9e7))
  * **lnd:** do not pass paymentHash when sending via paymentRequest ([5fcc25c](https://github.com/LN-Zap/zap-desktop/commit/5fcc25c45f7ab91add07ae43eae0983bd4994856))
  * **lnd:** ensure fee limit is correctly set ([762c137](https://github.com/LN-Zap/zap-desktop/commit/762c13789ebb49612c71e588a77676f9126cad0b))
  * **lnd:** fetch dest pubkey from payment htlcs list ([dc41030](https://github.com/LN-Zap/zap-desktop/commit/dc410305078d85b5310f4cc933ea12ec711ca97c))
  * **lnd:** handle early walletunlocker disconnect ([245c28b](https://github.com/LN-Zap/zap-desktop/commit/245c28be58397d13ee1c0528bfc280bf5f8c88c0))
  * **lnd:** increasing default fee limit to 5000 sats ([49cea65](https://github.com/LN-Zap/zap-desktop/commit/49cea659a373f219580f0065d461911a9b867cd4))
  * **lnd:** properly handle node updates from chan graph sub ([b7a84ff](https://github.com/LN-Zap/zap-desktop/commit/b7a84ff5c253055f5f49885c40f05de487499ab2))
  * **lnd:** support probing in lnd v0.10.0 ([32bd2be](https://github.com/LN-Zap/zap-desktop/commit/32bd2bea53f689ce6565bc6bcdcb8f5635c3ed52))
  * **lnd:** use default cltv expired if not set in invoice ([ecc22a8](https://github.com/LN-Zap/zap-desktop/commit/ecc22a83eee8e77c4582c53d310c43e9bd4b2f8a))
  * **lnd:** use route hints from invoice when probing ([f46938b](https://github.com/LN-Zap/zap-desktop/commit/f46938b9ea4f501637b93bd988d1c70df2d891a8))
  * **lnurl:** show notification on success / error ([e68c8f5](https://github.com/LN-Zap/zap-desktop/commit/e68c8f5b5147e23f6b966f628c4e7d33fe3301d2))
  * **ui:** add zero amount payment request error ([#3385](https://github.com/LN-Zap/zap-desktop/issues/3385)) ([6759be0](https://github.com/LN-Zap/zap-desktop/commit/6759be05de6fcb5235426bad626e5c09cb51a84e)), closes [#1510](https://github.com/LN-Zap/zap-desktop/issues/1510)
  * **ui:** always display crypto amounts as positive numbers ([a203b15](https://github.com/LN-Zap/zap-desktop/commit/a203b15a2b28dc147aa6926e9e0c3497795803a7))
  * **ui:** correct wording for channel open/close error ([626ba70](https://github.com/LN-Zap/zap-desktop/commit/626ba708dc56b570f49a398e031a0657e2401383))
  * **ui:** correctly calculate chan activity ([1330a4b](https://github.com/LN-Zap/zap-desktop/commit/1330a4b4525dba7369bd950cbce5707901907d16))
  * **ui:** disable address field overflow on amount form ([bfafa3c](https://github.com/LN-Zap/zap-desktop/commit/bfafa3c674d9693bb410fcdc2005f65d3a98a49d))
  * **ui:** display correct fee from probing ([64a006a](https://github.com/LN-Zap/zap-desktop/commit/64a006ae13ba30c2cc822362dbf926fdb3265f12))
  * **ui:** display destination when sending keysend payments ([5572048](https://github.com/LN-Zap/zap-desktop/commit/557204897a6fe1ecc66abdaad0e496023812b0c5))
  * **ui:** display total amount as unknown when no route found ([7422b56](https://github.com/LN-Zap/zap-desktop/commit/7422b56b66f4aa8be1b1f26fc603ba976eadbe85))
  * **ui:** do not show qr code for keysend payments ([2e11bc5](https://github.com/LN-Zap/zap-desktop/commit/2e11bc53e2285e6b91f6e876fc1aea60147118ff))
  * **ui:** ensure destination is displayed during sending payments ([e2d5e7e](https://github.com/LN-Zap/zap-desktop/commit/e2d5e7e790a1633861cb19c58d98ff01da8304fc))
  * **ui:** ensure loading messages display correctly ([ad6e5f5](https://github.com/LN-Zap/zap-desktop/commit/ad6e5f552119d1d1b2b39d2b4a6ddf136665c993))
  * **ui:** ensure skip backup checkbox is clickable ([f25cc02](https://github.com/LN-Zap/zap-desktop/commit/f25cc025f4b2fccaca58d7b7cfc7e11fbee08ebf))
  * **ui:** ensure wallet settings initial values correct ([53389d0](https://github.com/LN-Zap/zap-desktop/commit/53389d00a1399c68a1767cbc4ee75d673b24b02e))
  * **ui:** improve keysend receive message ([2130610](https://github.com/LN-Zap/zap-desktop/commit/21306101cfef1c1ac891257c8febc1009969294a))
  * **ui:** improve lnurl success/error handling ([5debf94](https://github.com/LN-Zap/zap-desktop/commit/5debf9465dd538af762abeda5dcde41763779dbd))
  * **ui:** map send payment error codes to messages ([1974463](https://github.com/LN-Zap/zap-desktop/commit/1974463c8d457e275d0debef34ed224aff1c2c79))
  * **ui:** only show crypto selector when total is known ([0e30609](https://github.com/LN-Zap/zap-desktop/commit/0e306094e7a3717f5872052d47b793fc14d6114e))
  * **ui:** pay form next button disabled state ([aa6eb53](https://github.com/LN-Zap/zap-desktop/commit/aa6eb536a82f6fa7c21611474be7a8e751ca834a)), closes [#3176](https://github.com/LN-Zap/zap-desktop/issues/3176)
  * **ui:** reload existing activity history on refresh ([7029ba1](https://github.com/LN-Zap/zap-desktop/commit/7029ba156871ebbbfa2898237eda0d3a5a6e6f59)), closes [#3174](https://github.com/LN-Zap/zap-desktop/issues/3174)
  * **ui:** remove channel from closing list on error ([9cc1999](https://github.com/LN-Zap/zap-desktop/commit/9cc19995f2fbcef8011ff3d0ca2b649c06b3ea89))
  * **ui:** show liquidity warning on all but address step ([ec6fa2a](https://github.com/LN-Zap/zap-desktop/commit/ec6fa2ac26586e1b0c848f76af25e37170742198))
  * **ui:** trim host from keysend pubkey ([010661c](https://github.com/LN-Zap/zap-desktop/commit/010661c63365b676df25b5f0b05d967682d92d37))
  * **ui:** update default window width to 950px ([8ca422b](https://github.com/LN-Zap/zap-desktop/commit/8ca422bfa5b96f314480fceea9994a642859919a))
  * **ui:** update transaction on stream update ([4a10e8e](https://github.com/LN-Zap/zap-desktop/commit/4a10e8e956e7c14dbdedcaf04bdcfef2011165ae))
  * **ui:** show correct heading for received payment in modal ([df0b4bb](https://github.com/LN-Zap/zap-desktop/commit/df0b4bbbf11d93c042b711f413107ca3f195bf21)), closes [#539](https://github.com/LN-Zap/zap-desktop/issues/539)
  * **ui:** update pay form fiat value on initial set ([26dc40c](https://github.com/LN-Zap/zap-desktop/commit/26dc40c))
  * **wallet:** convert bip21 amount to active crypto unit ([1bc4d68](https://github.com/LN-Zap/zap-desktop/commit/1bc4d680c7f2c9a1f6912612cc4ac6785b6f672f))
  * **wallet:** correct system notification for received transaction ([70430ef](https://github.com/LN-Zap/zap-desktop/commit/70430ef4b5c63691e0a15fa864c22645e3654498))
  * **wallet:** correctly sort channels by activity ([7c35b2a](https://github.com/LN-Zap/zap-desktop/commit/7c35b2aa3cde6b5f78cd1b745b45b97f437e9207))
  * **wallet:** ensure activity items get date header rows ([be47b82](https://github.com/LN-Zap/zap-desktop/commit/be47b82b71036e07eb96f1a5cb75b334a937ce95))
  * **wallet:** ensure fee displayed for slow confirmations ([dc69302](https://github.com/LN-Zap/zap-desktop/commit/dc69302e5cfbcecb6a0f336b26f5e040d046c70a))
  * **wallet:** ensure received transactions show in filter ([09860e2](https://github.com/LN-Zap/zap-desktop/commit/09860e22772c924ead0a22ca4651e984591fe432))
  * **wallet:** ensure transactions update on confirm ([fbe93c6](https://github.com/LN-Zap/zap-desktop/commit/fbe93c6d2fa873da8347a582bb134e717d4ec2d1))
  * **wallet:** handle fee as string in TransactionFeeInput ([a188b94](https://github.com/LN-Zap/zap-desktop/commit/a188b949ca0547f5d80bcb3ae87b97e3050a9c69))
  * **wallet:** log error if an activity paginator fails to load ([75c928d](https://github.com/LN-Zap/zap-desktop/commit/75c928d1ee8fa06027aa3cbfb70c3432740fe043))
  * **wallet:** no desktop notification for channel open or close ([1e6165f](https://github.com/LN-Zap/zap-desktop/commit/1e6165f12caf0f0e2a01539a299fddbc2e0e91dc))
  * **wallet:** only generate new address after use ([4fd938d](https://github.com/LN-Zap/zap-desktop/commit/4fd938d91a8680e576d5017fc0efdea5d5529066))
  * **wallet:** prevent double count of unconfirmed force close balance ([d06657a](https://github.com/LN-Zap/zap-desktop/commit/d06657a6b7b305b3f265f1305c668f0e28831ed9))
  * **wallet:** properly decode invoice in getTag ([2f49899](https://github.com/LN-Zap/zap-desktop/commit/2f49899874433ecf1ed356630b315999f0d21adf))
  * **wallet:** store payment hash of sending payment ([d3d5e23](https://github.com/LN-Zap/zap-desktop/commit/d3d5e2379b399fd9d05000014b519f9390cb0b9b))
  * **wallet:** use uppercase for bolt11 qrcodes ([9a9ab14](https://github.com/LN-Zap/zap-desktop/commit/9a9ab14103c1d638dbf15ed29847e3b03e1e4d18))
  * **wallet:** ensure activity items correctly sorted ([e96a8d5](https://github.com/LN-Zap/zap-desktop/commit/e96a8d5d456d76e1b244c6c6ac82f97c05cce34d))
  * **wallet:** shorten timeout for lnurl processing notifications ([340d170](https://github.com/LN-Zap/zap-desktop/commit/340d170d0ac32b1b6387511231dcfaf2cde3c346))
  * **wallet:** handle amounts as bignumber ([fa894ba](https://github.com/LN-Zap/zap-desktop/commit/fa894ba4e0e4f9a700089b256b6088149b84ec97))
  * **wallet:** send correct payment request ([a5d7d5c](https://github.com/LN-Zap/zap-desktop/commit/a5d7d5c391ba98305d8754d32d4005324dba9269))
  * **wallet:** set payment probe fee limit to 100000 sats ([ed23de0](https://github.com/LN-Zap/zap-desktop/commit/ed23de01025c3ee0273cbf5943d59e11959dd9cd))
  * **wallet:** display transaction as unconfirmed if confs less than min finality ([ffffd88](https://github.com/LN-Zap/zap-desktop/commit/ffffd8826ccf55f551819a755067a1e9f0993243))
  * **wallet:** error handling for failed invoice payments ([8685ea6](https://github.com/LN-Zap/zap-desktop/commit/8685ea6df65a0d433148ff0bb9d8c0f3854b7bad))
  * **wallet:** strip unsupported props from db wallet entries ([d058956](https://github.com/LN-Zap/zap-desktop/commit/d0589566621685ce8c29e060f7e148936b00dc0d))
  * **wallet:** update help page link ([1f480b6](https://github.com/LN-Zap/zap-desktop/commit/1f480b6cc77f4f46641154722d3f4c2c66212b1a))

### Features

  * **lnd:** enable keysend for neutrino clients ([954b77c](https://github.com/LN-Zap/zap-desktop/commit/954b77c4f7c85d3bd53d7d12fce142c2b053e552))
  * **lnd:** increase one time send/receive limits for mpp ([3ee7c73](https://github.com/LN-Zap/zap-desktop/commit/3ee7c73b4222167b647ca46f82594324b5c676d8))
  * **lnd:** support multi part payments ([88b4bcc](https://github.com/LN-Zap/zap-desktop/commit/88b4bccdf444d57fdb0b449e630c77503c40ea91))
  * **lnd:** support route probing for keysend payments ([e4d9438](https://github.com/LN-Zap/zap-desktop/commit/e4d943879fee40225857a8554b98923ba83bf416))
  * **lnd:** update lnd to 0.10.2-beta ([42eff0c](https://github.com/LN-Zap/zap-desktop/commit/42eff0c271b724daa0154c2a985b7906463ce685))
  * **lnd:** use new Router api for sending payments ([13a2ed7](https://github.com/LN-Zap/zap-desktop/commit/13a2ed74e4c841a9fc462ea57a373ff2730e6b08))
  * **lnd:** use payment probing to get fee estimate ([5c3aabd](https://github.com/LN-Zap/zap-desktop/commit/5c3aabdb1875061efc922b6298f36d06a7ba70a9))
  * **lnd:** attempt sendToRoute for first payment attempt ([1bce811](https://github.com/LN-Zap/zap-desktop/commit/1bce8118de744d8d9a2c08dfb4bf7c7fbfae12e2))
  * **ui:** ability to edit fee limit from pay summary ([62c4e3d](https://github.com/LN-Zap/zap-desktop/commit/62c4e3dbc8c617845ee8bd3180eb02b4dc722a4c))
  * **ui:** add node pubkey into send address field label ([8d356c5](https://github.com/LN-Zap/zap-desktop/commit/8d356c5dffecb5075a48e7598fe607a99ad7f5fe))
  * **ui:** add note to request summary for keysend payments ([1690f91](https://github.com/LN-Zap/zap-desktop/commit/1690f91816b25ddc3673d0faedb85e408cc1227f))
  * **ui:** display destination address in payment modal ([9a1d93a](https://github.com/LN-Zap/zap-desktop/commit/9a1d93a330321d5108e025fd4ad0f4d91504ecb4))
  * **ui:** display fee limit when fee is unknown ([88a9bf2](https://github.com/LN-Zap/zap-desktop/commit/88a9bf2e96f9699a3ce75080b5d63757fd5bd3ad))
  * **ui:** display htlc summary in payment modal ([5a4a02e](https://github.com/LN-Zap/zap-desktop/commit/5a4a02ebb815d1a5319671adca086f9d131af35b))
  * **ui:** display loading message when starting tor proxy ([cd490d6](https://github.com/LN-Zap/zap-desktop/commit/cd490d64d0c5ac25368d9b4b4321575194683962))
  * **ui:** show multiple node uris if there are more than one ([8a418d9](https://github.com/LN-Zap/zap-desktop/commit/8a418d94c913a250b5d232b1b672312e36b9dae6)), closes [#3150](https://github.com/LN-Zap/zap-desktop/issues/3150)
  * **ui:** show tooltip when fee limit is unknown ([8410149](https://github.com/LN-Zap/zap-desktop/commit/84101495a0e89f41bbc15d3edd90b9c6ef3aae7a)), closes [#2676](https://github.com/LN-Zap/zap-desktop/issues/2676)
  * **ui:** show total as spinner whilst probing ([002c676](https://github.com/LN-Zap/zap-desktop/commit/002c6766b63592161a5df2eec446f29e6b51b5ca))
  * **ui:** show transactions paid to self as sent to self ([e498612](https://github.com/LN-Zap/zap-desktop/commit/e498612c92c14bdfd1eac02e3d562813b4633480))
  * **ui:** add tooltip to the Home.Autopilot section describing its function ([7342a60](https://github.com/LN-Zap/zap-desktop/commit/7342a607c2f384768212be40164de162bc04aba7))
  * **ui:** display paylock icon for private channels ([ef16141](https://github.com/LN-Zap/zap-desktop/commit/ef1614181579ec5706ad186fb77e3241c3afb17a))
  * **walet:** expose payment config via preferences page ([9e4d1e4](https://github.com/LN-Zap/zap-desktop/commit/9e4d1e485a23a33d5d555df078c9ae10117f3102))
  * **wallet:** add ability to cancel invoices ([669e716](https://github.com/LN-Zap/zap-desktop/commit/669e71609930fccf977eae83574d8cf70f3eafb7))
  * **wallet:** add ability to create hold invoices ([248d86c](https://github.com/LN-Zap/zap-desktop/commit/248d86cf07475a8d4228d2be2237ef59f5d11267))
  * **wallet:** add ability to settle invoices ([fe2cbad](https://github.com/LN-Zap/zap-desktop/commit/fe2cbada837e7abbd1f8b2c043e9ab038b46e7ad))
  * **wallet:** add support for lnurl-channel ([bad6762](https://github.com/LN-Zap/zap-desktop/commit/bad6762025a71142df7c776f5c500bc8b1b81625))
  * **wallet:** basic keysend support ([8621eb6](https://github.com/LN-Zap/zap-desktop/commit/8621eb68cae14ef53dfea8047f1033c4c860f52f)), closes [#3333](https://github.com/LN-Zap/zap-desktop/issues/3333) [#3338](https://github.com/LN-Zap/zap-desktop/issues/3338)
  * **wallet:** lnurl-auth support ([d9e281a](https://github.com/LN-Zap/zap-desktop/commit/d9e281a658c6e41ee56f0b8beff74933ea6d0a28))
  * **wallet:** handle fees using msats ([01ac7fc](https://github.com/LN-Zap/zap-desktop/commit/01ac7fced743961ea235f75e7b7b77711f0b455d))
  * **wallet:** show exact fee when possible ([d202202](https://github.com/LN-Zap/zap-desktop/commit/d2022022ba183efbb32272ca953956f5cdaadac2))
  * **wallet:** support connecting to .onion domains ([a99482b](https://github.com/LN-Zap/zap-desktop/commit/a99482b5a81c07c32654c0f856c7cf74796441b2))
  * **wallet:** use pagination when fetching payments ([d8106ec](https://github.com/LN-Zap/zap-desktop/commit/d8106ecb7f249ec7be20bf1c029963f88e1dc452))
  * **wallet:** parse bip21 uris in pay address form ([8e56936](https://github.com/LN-Zap/zap-desktop/commit/8e56936))

### Changelog

The full list of changes since 0.6.2-beta can be found here:

[`v0.6.2-beta...v0.7.0-beta`](https://github.com/LN-Zap/zap-
desktop/compare/v0.6.2-beta...v0.7.0-beta)

## Verifying the Release

Please refer to [our documentation](https://github.com/LN-Zap/zap-
desktop#documentation) for [instructions on how to verify the
release](https://github.com/LN-Zap/zap-
desktop/blob/master/docs/SIGNATURES.md).

### Assets

12

  * [ latest-linux.yml ](/LN-Zap/zap-desktop/releases/download/v0.7.0-beta/latest-linux.yml)

400 Bytes

  * [ latest-mac.yml ](/LN-Zap/zap-desktop/releases/download/v0.7.0-beta/latest-mac.yml)

524 Bytes

  * [ latest.yml ](/LN-Zap/zap-desktop/releases/download/v0.7.0-beta/latest.yml)

347 Bytes

  * [ SHASUMS256.txt.asc ](/LN-Zap/zap-desktop/releases/download/v0.7.0-beta/SHASUMS256.txt.asc)

1.68 KB

  * [ Zap-linux-x86_64-v0.7.0-beta.AppImage ](/LN-Zap/zap-desktop/releases/download/v0.7.0-beta/Zap-linux-x86_64-v0.7.0-beta.AppImage)

91.1 MB

  * [ Zap-mac-v0.7.0-beta.dmg ](/LN-Zap/zap-desktop/releases/download/v0.7.0-beta/Zap-mac-v0.7.0-beta.dmg)

86.5 MB

  * [ Zap-mac-v0.7.0-beta.dmg.blockmap ](/LN-Zap/zap-desktop/releases/download/v0.7.0-beta/Zap-mac-v0.7.0-beta.dmg.blockmap)

94.9 KB

  * [ Zap-mac-v0.7.0-beta.zip ](/LN-Zap/zap-desktop/releases/download/v0.7.0-beta/Zap-mac-v0.7.0-beta.zip)

83.7 MB

  * [ Zap-win-v0.7.0-beta.exe ](/LN-Zap/zap-desktop/releases/download/v0.7.0-beta/Zap-win-v0.7.0-beta.exe)

64 MB

  * [ Zap-win-v0.7.0-beta.exe.blockmap ](/LN-Zap/zap-desktop/releases/download/v0.7.0-beta/Zap-win-v0.7.0-beta.exe.blockmap)

69.8 KB

  * [ Source code (zip) ](/LN-Zap/zap-desktop/archive/refs/tags/v0.7.0-beta.zip)

  * [ Source code (tar.gz) ](/LN-Zap/zap-desktop/archive/refs/tags/v0.7.0-beta.tar.gz)

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

