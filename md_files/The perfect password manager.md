_TL;DR: Use a Yubikey 4 with touch-to-sign to store your GPG keys, and use
these keys for SSH authentication and storing your secrets with password-
store._

## The problem

For a long time, I’ve been searching for a robust and secure way to store my
passwords, and secrets in general (SSH and GPG keys, personal files…)

There is one thing that bothered me in all the solutions I knew about, be it a
software like KeePass, or a cloud solution like LastPass: if my computer is
compromised at some point in time, it will be possible to extract _all_ of my
secrets when I open my vault to access _one_.

In that regard, a piece of paper in my wallet would be much more secure, as my
computer would only know the secrets I copy over when I need them.

The only device solving that problem is the
[mooltipass](https://www.themooltipass.com), an external device containing all
your passwords that can simulate a keyboard and type them when you need them.
It’s an interesting device, completely open source, and you should definitely
check it out.

But there is an alternative I want to talk about, based on the well-known
Yubikey, plus a combination of tools that fit all my needs, not only for
storing password but also to connect to remote SSH servers and decrypt/sign
PGP messages, while giving me strong security guarantees.

## The solution

In the true Unix fashion, I use a combination of tools doing a simple job
each. Let’s start with the password manager:

### GPG for your password manager: password-store

As you probably guessed in the title, it all rests on GPG and we’ll see later
how we secure these GPG keys.

But for now, let’s introduce a tool called [password-
store](https://www.passwordstore.org/).

It’s a pretty simple wrapper around GPG (a bash script, in fact) that allows
you to store each of your secret in a GPG-encrypted file.

The GPG key that you use for storing your password will be required each time
that you access a password. Because it’s public key cryptography, it means
that you can create new passwords without needing to access your key!

In term of security, well, it’s GPG. Each of your secret is stored in a file
in your home directory, so it’s up to you to do backups. But it’s all neat and
simple :)

    
    
    zx2c4@laptop ~ $ pass
    Password Store
    ├── Business
    │   ├── some-silly-business-site.com
    │   └── another-business-site.net
    ├── Email
    │   ├── donenfeld.com
    │   └── zx2c4.com
    └── France
        ├── bank
        ├── freebox
        └── mobilephone
    

There are even browser extensions ([firefox](https://addons.mozilla.org/en-
US/firefox/addon/passff/),
[chrome](https://chrome.google.com/webstore/detail/chrome-pass-
zx2c4/oblajhnjmknenodebpekmkliopipoolo)), to integrate password-store!

### GPG for your SSH keys: gpg-agent

I also want to do a quick disgression, and tell you that you can use GPG not
only to store your password, but to authenticate to remote servers.

Moreover, you can use key forwarding (so that in these servers, you can access
the SSH keys from your local machine and connect to other machines in turn)
without much risk of the server using them in your back: all the uses will
require you to touch your Yubikey!

For example, I connect to my server using my Yubikey, and on that remote
server I can copy files to another server, or push code to my git repository
by touching my Yubikey too. For all that, I don’t have to type a single
password.

For that you need to replace your SSH agent by gpg-agent, it’s all explained
in the appendix.

### Secure GPG key storage: Yubikey

![_images/yubikey.png](https://www.palkeo.com/en/blog/_images/yubikey.png)

Some of you may already have heard of [Yubikeys](https://www.yubico.com). The
idea is to have a Yubikey storing GPG keys that you generated on an air-gapped
computer.

It primarily serve for second-factor authentication, but here we will only
focus on its GPG smartcard function.

Once you set it up, GPG will connect to your Yubikey each time it needs to
access to your secret key. The Yubikey will do all the cryptographic work, so
that your secret key never leaves it. In case your computer is compromised, an
attacker can only use your secret key if your Yubikey is connected and
unlocked.

This was not satisfying for me yet, because it meant that if I connect and
unlock my Yubikey, a compromised computer can tell the Yubikey to decrypt all
my secret files, connect to all my servers… without me noticing: pretty bad.

That’s where the last generation of Yubikeys (Yubikey 4) have a feature that
went relatively unpublicized: you can have them require the user to **touch
it** everytime an operation on the secret key is requested. This means that
it’s impossible to access your secrets without you physically allowing it!

When combined with the tools above you will need to touch your Yubikey every
time you want to access one of your password, decrypt or sign a GPG message,
or connect to your server. Without you having unlocked, and touching your
Yubikey, it becomes _impossible_ to connect to your servers or access your
passwords. Even if your computer is fully compromised.

## Conclusion

I find this solution very secure, and quite easy to use and non-intrusive.

Also, to contradict the title of this article, here are a few security caveats
I could think of:

  * Even though it’s not possible to access your secrets, it’s still possible to replace them, because the public key encryption doesn’t require any secret. This could be fixed by forcing all your secret files to be signed by your secret key.

  * In case your computer is compromised, it could be possible to ask your Yubikey to do something else than what you intented, but then you would need to touch it twice, and will probably notice it :)

  * Oh, and sadly, the newer version of the Yubikey (the 4, with touch-to-sign) doesn’t have an open source firmware…

But compared to the other solutions I know, I think these are quite minor, and
that there is a much better security overall.

## Appendix: let’s do it!

### Generate your PGP keys

#### Master key

For this scheme to be secure, you need to generate your GPG keys on a secure
computer, disconnected from the internet. Or at least from a live CD, or
something you can trust better than your day-to-day computer.

Once you are on this secure, throwaway system, use gpg to generate a master
key (if you don’t have one already).

    
    
    $ gpg --gen-key
    

Generate a **sign only** key (the rest will go into our subkeys).

I suggest that you use all the defaults, but that you set an expiration date
in case you would loose your key (a few years into the future).

As long as you are in a secure system and you don’t plan to copy your secret
key anywhere (except to an encrypted, offline storage, as explained below),
you can leave the password used to protect the key empty.

#### Sub-keys

Now that you have your master key, let’s add three sub-keys: these will go to
your Yubikey.

    
    
    $ gpg --expert --edit-key palkeo
    

Replace “palkeo” by the name that you provided for your master key, or the key
ID you can see by doing `gpg --list-secret-keys`.

You should now have GPG prompt: `gpg>`. You will use this prompt to create
three subkeys.

  * One for **encryption** : to decrypt GPG messages you receive, including your secrets in password-store.

  * One for **signature** : to sign GPG messages you send.

  * One for **authentication** : mainly for SSH authentication.

Let’s see how to create the encryption key, for example:

    
    
    gpg> addkey
    
    Please select what kind of key you want:
    (3) DSA (sign only)
    (4) RSA (sign only)
    (5) Elgamal (encrypt only)
    (6) RSA (encrypt only)
    (7) DSA (set your own capabilities)
    (8) RSA (set your own capabilities)
    Your selection? 8
    
    Possible actions for a RSA key: Sign Encrypt Authenticate
    Current allowed actions: Sign Encrypt
    
    (S) Toggle the sign capability
    (E) Toggle the encrypt capability
    (A) Toggle the authenticate capability
    (Q) Finished
    
    Your selection? s
    
    Possible actions for a RSA key: Sign Encrypt Authenticate
    Current allowed actions: Encrypt
    
    (S) Toggle the sign capability
    (E) Toggle the encrypt capability
    (A) Toggle the authenticate capability
    (Q) Finished
    
    Your selection? q
    RSA keys may be between 1024 and 4096 bits long.
    What keysize do you want? (2048)
    Requested keysize is 2048 bits
    Please specify how long the key should be valid.
            0 = key does not expire
        <n>  = key expires in n days
        <n>w = key expires in n weeks
        <n>m = key expires in n months
        <n>y = key expires in n years
    Key is valid for? (0) 5y
    Key expires at Wed Dec  8 22:56:10 2021 UTC
    Is this correct? (y/N) y
    Really create? (y/N) y
    
    ...
    
    pub  2048R/A41164CD  created: 2016-12-09  expires: never       usage: SC
                         trust: ultimate      validity: ultimate
    sub  2048R/D7857578  created: 2016-12-09  expires: 2021-12-08  usage: E
    gpg>
    

You can see that I toggled the capabilities until there is only encryption
left:

    
    
    Possible actions for a RSA key: Sign Encrypt Authenticate
    Current allowed actions: Encrypt
    

Repeat the process with the `addkey` command again, but this time leaving the
`Sign` capability left. Do it one last time, for the `Authenticate`
capability.

You should now have three sub-keys. These will go to your Yubikey soon.

#### Backup time

Now is backup time, don’t neglect this step!

Export your secret key and subkeys, like that:

    
    
    $ gpg -a --export-secret-keys A41164CD > key.txt
    $ gpg -a --export-secret-subkeys A41164CD > subkeys.txt
    

Now copy these files to a secure storage. It should be offline, so that your
computer can’t access it, and you probably also want to encrypt it. But you
should be able to access it in case you lose your Yubikey, and want to export
the keys to a new one.

I also recommend that you make a copy of the `~/.gnupg` directory that you
used to generate these keys.

### Setup your Yubikey

Once you have your Yubikey, it’s time to set it up:

#### Smartcard setup

Note

Because you are accessing/copying your secret keys, this is to be done on an
offline/secure computer again. I recommend you generate the keys and copy them
at once, when you have your Yubikey.

First of all, most of the articles I could find mention the use of
`ykpersonalize` to enable GPG on the Yubikey. I found out it’s not needed (at
least for the Yubikey 4), as it’s enabled by default (U2F too).

You now need to install the smartcard support in GPG:

    
    
    $ sudo apt-get install scdaemon pcscd gnupg-agent
    

Now you can plug your Yubikey, and execute `gpg --card-status`. You should see
something like:

    
    
    Reader ...........: 1050:0407:X:0
    Application ID ...: D2760001240102010006050314690000
    Version ..........: 2.1
    Manufacturer .....: Yubico
    Serial number ....: 05031469
    Name of cardholder: [not set]
    Language prefs ...: [not set]
    Sex ..............: unspecified
    URL of public key : [not set]
    Login data .......: [not set]
    Signature PIN ....: not forced
    Key attributes ...: rsa2048 rsa2048 rsa2048
    Max. PIN lengths .: 127 127 127
    PIN retry counter : 3 0 3
    Signature counter : 0
    Signature key ....: [none]
    Encryption key....: [none]
    Authentication key: [none]
    General key info..: [none]
    

Let’s set it up:

    
    
    $ gpg --card-edit
    
    ... (same as above) ...
    
    gpg/card> admin
    Admin commands are allowed
    
    gpg/card> passwd
    
    1 - change PIN
    2 - unblock PIN
    3 - change Admin PIN
    4 - set the Reset Code
    Q - quit
    
    Your selection? 3
    PIN changed.
    
    1 - change PIN
    2 - unblock PIN
    3 - change Admin PIN
    4 - set the Reset Code
    Q - quit
    
    Your selection? 1
    PIN changed.
    
    1 - change PIN
    2 - unblock PIN
    3 - change Admin PIN
    4 - set the Reset Code
    Q - quit
    
    Your selection? q
    gpg/card> quit
    

You will be asked for the original admin PIN, which is 12345678. Same for the
original PIN, which is 123456.

Make sure that your new admin PIN is secret/unguessable. You can store a
backup along with your GPG keys. It’s only used to administrate the Yubikey
GPG smartcard.

The “normal” PIN is the one you will have to type to unlock your Yubikey, when
you connect it to your computer. The goal is to prevent someone stealing your
Yubikey to impersonate you.

#### GPG keys setup

Now, let’s move the keys to your Yubikey:

    
    
    $ gpg --edit-key palkeo
    
    pub  2048R/A41164CD  created: 2016-12-09  expires: 2021-12-08  usage: SC
                         trust: ultimate      validity: ultimate
    sub  2048R/486B21CF  created: 2016-12-09  expires: 2021-12-08  usage: S
    sub  2048R/D7857578  created: 2016-12-09  expires: 2021-12-08  usage: E
    sub  2048R/DA1E5137  created: 2016-12-09  expires: 2021-12-08  usage: A
    [ultimate] (1). palkeo
    
    gpg> toggle
    
    sec  3744R/1C5C4717  created: 2016-12-09  expires: 2021-12-08
    ssb  2048R/486B21CF  created: 2016-12-09  expires: 2021-12-08
    ssb  2048R/A11F46D2  created: 2016-12-09  expires: 2021-12-08
    ssb  2048R/DA1E5137  created: 2016-12-09  expires: 2021-12-08
    (1)  palkeo
    
    gpg> key 1
    
    sec  3744R/1C5C4717  created: 2016-12-09  expires: 2021-12-08
    ssb* 2048R/486B21CF  created: 2016-12-09  expires: 2021-12-08
    ssb  2048R/A11F46D2  created: 2016-12-09  expires: 2021-12-08
    ssb  2048R/DA1E5137  created: 2016-12-09  expires: 2021-12-08
    (1)  palkeo
    
    gpg> keytocard
    Signature key ....: [none]
    Encryption key....: [none]
    Authentication key: [none]
    
    Please select where to store the key:
    (1) Signature key
    (3) Authentication key
    Your selection? 1
    
    sec  3744R/1C5C4717  created: 2016-12-09  expires: 2021-12-08
    ssb* 2048R/486B21CF  created: 2016-12-09  expires: 2012-12-08
                         card-no: 0060 00000042
    ssb  2048R/A11F46D2  created: 2016-12-09  expires: 2012-12-08
    ssb  2048R/DA1E5137  created: 2016-12-09  expires: 2012-12-08
    (1)  palkeo
    
    gpg>
    

This is an example moving my signature key to my Yubikey. Note that the key is
**moved** (that’s why you need to have done backups before!), and replaced by
a stub pointing to unique identifier of the smartcard.

You need to reproduce that process again two times, to move the two other keys
too (use the `key` command to deselect the key 1, select the key 2…).

Once it’s done, do a `gpg --card-status` to check that your keys were
sucessfully moved to your Yubikey.

#### Touch-to-sign setup

We also need to enable the functionality forcing you to touch your Yubkey when
a cryptographic operation is requested.

It’s quite granular, as this flag is set per key slot. But I recommend that
you set it to all your three keys.

[This link](https://developers.yubico.com/PGP/Card_edit.html) contains all the
information you need. It points to a `yubitouch.sh` script that you have to
download and run to enable this feature.

#### Have your machines use the Yubikey

For your machines to use your Yubikey, you need to export your public keys on
your offline system:

    
    
    $ gpg -a --export palkeo > public-key.txt
    

Move that file (and only this one, not your secret keys!) to your day-to-day
machine, and import it like that:

    
    
    $ gpg --import < public-key.txt
    

That’s it, you are all set, and you should now be able to transparently use
your Yubikey to encrypt/sign GPG messages :)

### Setup password-store

Once you have GPG set up to use your Yubikey, password-store is trivial to
use:

First, you have to initialize it, by passing the ID of your master key:

    
    
    pass init 1C5C4717
    

Then, you are free to add new passwords with `pass insert`. Remember that it
won’t ask you for your Yubikey when you add passwords (only when you access
them).

Note

If you use `pass edit` to edit your secrets in your preferred text editor, be
aware that they are unencrypted to a temporary directory and that your text
editor may backup the file elsewhere, while it’s unencrypted! If you use vim,
there is [a plugin](https://git.zx2c4.com/password-
store/tree/contrib/vim/redact_pass.vim) that you can install to avoid that.
There are also other interesting scripts in the [contrib/
directory](https://git.zx2c4.com/password-store/tree/contrib) of password-
store.

### Use your key for SSH authentication

We will use the GPG agent to replace the SSH agent.

First, you have to enable that support in the GPG agent:

    
    
    echo enable-ssh-support >> $HOME/.gnupg/gpg-agent.conf
    

Then, start the agent:

    
    
    eval `gpg-agent --daemon`
    

This has the side-effect of setting environment variables like
`SSH_AUTH_SOCK`.

You will also have to make sure you start it at the beginning of each session,
or at each login if it’s not started already.

You should see your shiny new SSH key by doing `ssh-add -l`.

Note that using `ssh-add -L` will give it in a format that’s ready to add to
the `authorized_keys` file on a remote host.

### An important reminder

I just wanted to remind you these two things, that are on the basis of all
this:

  * Make sure that the admin PIN of your Yubikey is set up and stored offline with your secret keys: with it, it become possible to disable touch-to-sign.

  * You need to make sure that you always have an offline backup of the secret key that’s on your Yubikey, so that if you lose it you still have a way to copy that secret key to a new Yubikey, and access your encrypted passwords securely again.

