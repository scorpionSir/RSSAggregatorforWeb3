[![esprezzo-logo@2x](https://blog.esprezzo.io/hs-fs/hubfs/esprezzo-
logo@2x.png?width=261&name=esprezzo-logo@2x.png)](https://esprezzo.io)

  * [Products](https://esprezzo.io/products)
  * [Developers](https://esprezzo.io/developers)
  * [About](https://esprezzo.io/about)
  * [Blog](https://blog.esprezzo.io)
  * [GET AN INVITE](https://esprezzo.io/invite)

##  [The Esprezzo Blog](https://blog.esprezzo.io)

# How to Use Perkle with MyEtherWallet (MEW v5, new interface)

by [Jialin Luh](https://blog.esprezzo.io/author/jialin-luh) on November 19,
2019

  * [Tweet](https://twitter.com/share)
  *   * 

**Update** : _Since this blog post was published, Perkle has been officially
integrated with MEW![Check out the new guide here.](/perkle-prkl-
myetherwallet-mew-integration)_

Last month MyEtherWallet (MEW) [discontinued their original
wallet](https://kb.myetherwallet.com/en/migration/importing-vintagemew-to-
mew/) (Vintage MEW) forcing everyone to switch over to the new interface (MEW
v5), which means it's time to update our guide! If you're wondering how to set
up a [Perkle (PRKL)](/what-is-perkle-prkl) wallet using MEW v5, you've come to
the right place. Let's jump right in.

Here's what you will need to get started:

  * [MEWconnect](https://mewconnect.myetherwallet.com/#/) mobile app installed on your iPhone or Android smartphone
  * A MEW wallet set up on your smartphone via MEWconnect
  * A laptop or desktop computer

This guide is written for those of you who already have a MEW wallet set up.
If you haven't created one yet, you will need to [create a new
wallet](https://www.myetherwallet.com/create-wallet).

For security purposes, MEW suggests accessing your wallet via the
**[MEWconnect mobile app](https://mewconnect.myetherwallet.com/#/)** , which
basically [turns your smartphone into a hardware
wallet](https://medium.com/myetherwallet/mewconnect-a-new-hardware-wallet-
without-all-the-hardware-fc3b83c6c0df). If you are creating a new wallet, MEW
recommends doing so directly from the mobile app. Our guide is going to focus
on this method; if you haven't yet, take a few minutes to install MEWconnect
on your phone, and use the app to generate a new wallet before proceeding.
Even if you created a MEW address previously, they recommend starting from
scratch using MEWconnect on your smartphone.

Here's a link to the [MEWconnect User
Guide](https://kb.myetherwallet.com/en/mewconnect/mewconnect-user-guide/) just
in case you need some help getting set up. We recommend generating and saving
your MEWconnect password in a secure password manager such as
[1Password](https://1password.com/).

## Connecting to the Perkle Blockchain

To begin, go to the [MyEtherWallet website](https://www.myetherwallet.com/)
from your laptop or desktop computer. As a reminder, it's a best practice to
inspect the URL in your browser and ensure you see the padlock next to the
URL, ensuring you're not on a phishing site:

![myetherwallet-url](https://blog.esprezzo.io/hs-fs/hubfs/myetherwallet-
url.jpg?width=552&name=myetherwallet-url.jpg)

If you're new to blockchain technology or are not familiar with MEW, we highly
recommend reading [MyEtherWallet's
introduction](https://kb.myetherwallet.com/en/getting-started/myetherwallet-
an-introduction/) to understand what you can do with MEW, how your funds are
stored and how to keep your wallet secure.

Step 1. From MEW's homepage, click "Access My Wallet":

![MyEtherWallet-homepage-1](https://blog.esprezzo.io/hs-
fs/hubfs/MyEtherWallet-homepage-1.jpg?width=800&name=MyEtherWallet-
homepage-1.jpg)

Step 2. On the "Access My Wallet" screen, click on "MEWconnect":

![MyEtherWallet_Access-my-wallet-1](https://blog.esprezzo.io/hs-
fs/hubfs/MyEtherWallet_Access-my-
wallet-1.jpg?width=724&name=MyEtherWallet_Access-my-wallet-1.jpg)

Which brings up this screen:

![MyEtherWallet-Access-by-MEWconnect-1](https://blog.esprezzo.io/hs-
fs/hubfs/MyEtherWallet-Access-by-
MEWconnect-1.jpg?width=724&name=MyEtherWallet-Access-by-MEWconnect-1.jpg)Step
3. Open MEWconnect on your smartphone and enter your password, which takes you
to your public Ethereum address screen:

![MEWconnect-ETHmainnet](https://blog.esprezzo.io/hs-fs/hubfs/MEWconnect-
ETHmainnet.jpg?width=300&name=MEWconnect-ETHmainnet.jpg)

Step 4. From here, press the "Scan to Connect" button and use your phone
camera to scan the QR code displayed on MEW on your laptop or desktop (that's
the screen with the QR code referenced above). Then you should see this:

![MEWconnect_Local-MEW-connection-screens-1](https://blog.esprezzo.io/hs-
fs/hubfs/MEWconnect_Local-MEW-connection-
screens-1.jpg?width=724&name=MEWconnect_Local-MEW-connection-screens-1.jpg)

Your phone wallet has now made a local connection to MEW, and you should see
the MEW page in your browser change from the QR code to your wallet dashboard,
which should look something like this:

![MyEtherWallet-Dashboard](https://blog.esprezzo.io/hs-fs/hubfs/MyEtherWallet-
Dashboard.jpg?width=2400&name=MyEtherWallet-Dashboard.jpg)

> Your address is in the upper right corner is where you'll send or receive
> PRKL, ETH, or other ERC-20 tokens.

From here, you'll be doing the rest from the MyEtherWallet website on your
laptop or desktop computer.

Step 5. Click the "change" button in the Network box in the upper right
corner:

![MyEtherWallet-Dashboard_Change-Network](https://blog.esprezzo.io/hs-
fs/hubfs/MyEtherWallet-Dashboard_Change-
Network.jpg?width=2400&name=MyEtherWallet-Dashboard_Change-Network.jpg)

Which will bring up this modal:

![MyEtherWallet-Dashboard_Change-Network_Custom-Node-
Off](https://blog.esprezzo.io/hs-fs/hubfs/MyEtherWallet-Dashboard_Change-
Network_Custom-Node-Off.jpg?width=2400&name=MyEtherWallet-Dashboard_Change-
Network_Custom-Node-Off.jpg)

Click the toggle for "Add Custom Network/Node":

![MyEtherWallet-Dashboard_Change-Network_Custom-Node-
On-1](https://blog.esprezzo.io/hs-fs/hubfs/MyEtherWallet-Dashboard_Change-
Network_Custom-Node-On-1.jpg?width=2400&name=MyEtherWallet-Dashboard_Change-
Network_Custom-Node-On-1.jpg)

Select "CUS - Custom" from the dropdown (where it says ETH - Ethereum), which
updates the fields:

![MyEtherWallet-Dashboard_Change-Network_Custom-Node-On-
CUS](https://blog.esprezzo.io/hs-fs/hubfs/MyEtherWallet-Dashboard_Change-
Network_Custom-Node-On-CUS.jpg?width=2400&name=MyEtherWallet-Dashboard_Change-
Network_Custom-Node-On-CUS.jpg)

If you're not super familiar with Ethereum or ERC-20 tokens, some of these
fields may be puzzling since they don't have labels. That's why we've put this
guide together for you!

Step 6. Fill out the form in the Network pop-up

In the **ETH Node Name** field, enter " **perklepub** " (without the quotation
marks).

In the **URL** field, enter **https://perkle-pub.esprezzo.io**

Replace **443** with **8501** \-- this is the port.

In the next field, paste the URL for a Perkle transaction (tx) hash from the
block explorer:

**https://explorer.esprezzo.io/transactions/[[txHash]]**

Replace **1** with  **667** \-- this is the Chain ID.

In the last field, paste the URL for a Perkle address from the block explorer:
**https://explorer.esprezzo.io/addresses/[[address]]**

Like so:

![MyEtherWallet-Dashboard_Change-Network_Custom-Node_Fields-
Completed_2.1](https://blog.esprezzo.io/hs-fs/hubfs/MyEtherWallet-
Dashboard_Change-Network_Custom-Node_Fields-
Completed_2.1.jpg?width=2400&name=MyEtherWallet-Dashboard_Change-
Network_Custom-Node_Fields-Completed_2.1.jpg)

Press **Save**.

Step 7. Scroll to the bottom of the modal and you'll see Perkle at the very
bottom:

![MyEtherWallet_Perkle-Network_2](https://blog.esprezzo.io/hs-
fs/hubfs/MyEtherWallet_Perkle-
Network_2.jpg?width=724&name=MyEtherWallet_Perkle-Network_2.jpg)

Click on **perklepub (CUS)**!

You should now see Perkle as the network on your dashboard in the upper left
corner, and perklepub as the network in the upper right:

![MyEtherWallet_Perkle-Network_connected-2](https://blog.esprezzo.io/hs-
fs/hubfs/MyEtherWallet_Perkle-
Network_connected-2.jpg?width=2400&name=MyEtherWallet_Perkle-
Network_connected-2.jpg)

It would be nice if MEW would allow us to enter the PRKL abbreviation so that
the Balance would show as PRKL instead of CUS — a desirable future feature for
MEW!

## How to Check PRKL Balance

From the dashboard, as you may have guessed, you will be able to see your
Balance in the middle box; after sending a few PRKL from my Discord wallet to
MEW:

![MyEtherWallet_PRKL-balance](https://blog.esprezzo.io/hs-
fs/hubfs/MyEtherWallet_PRKL-balance.jpg?width=2400&name=MyEtherWallet_PRKL-
balance.jpg)

## How to Send PRKL

To send PRKL to another address:

  1. Make sure your MEWconnect is connected on your smartphone. Reminder: MEWconnect should look like this when you are connected to Perkle:  
![MEWconnect_connected](https://blog.esprezzo.io/hs-
fs/hubfs/MEWconnect_connected.jpg?width=2400&name=MEWconnect_connected.jpg)

  2. On the sidebar of MEW in your browser, select **Send**. You can also press the **Send Transaction** panel with the astronaut under "Actions", which brings up a form below the 3 boxes:  
![MyEtherWallet_Send-1](https://blog.esprezzo.io/hs-
fs/hubfs/MyEtherWallet_Send-1.jpg?width=2400&name=MyEtherWallet_Send-1.jpg)

  3. Enter the amount of PRKL you wish to send
  4. Enter the address you wish to send PRKL to
  5. Press the  **Send Transaction** button  
![MyEtherWallet_Send-2](https://blog.esprezzo.io/hs-
fs/hubfs/MyEtherWallet_Send-2.jpg?width=2400&name=MyEtherWallet_Send-2.jpg)

  6. You will then see the modal below. MEW neglects to state that you will need to confirm and sign the transaction using MEWconnect using your smartphone. So that's what we're going to do!  
![MyEtherWallet_Send-3](https://blog.esprezzo.io/hs-
fs/hubfs/MyEtherWallet_Send-3.jpg?width=2400&name=MyEtherWallet_Send-3.jpg)

  7. Once you see the above screen, look at MEWconnect on your smartphone. Verify the details (make sure the recipient address and quantity are correct!) and click to check the round checkboxes to sign the transaction:   
![MEWconnect verify and sign-transaction iOS app screen
shots](https://blog.esprezzo.io/hs-fs/hubfs/MEWconnect_verify_sign-
transaction.jpg?width=2400&name=MEWconnect_verify_sign-transaction.jpg)

  8. Now turn your attention back to MEW in your browser on your computer. You will see that the  **Confirm and Send** button is green now that you've verified and signed the transaction from your smartphone; press the button!  
![MyEtherWallet_Send-4](https://blog.esprezzo.io/hs-
fs/hubfs/MyEtherWallet_Send-4.jpg?width=2400&name=MyEtherWallet_Send-4.jpg)

  9. As long as you're not trying to send more PRKL than your wallet's balance and you have configured your connection to Perkle with the correct port and chain ID, you should see the following success screen once the transaction is successfully broadcasted to the network:  
![MyEtherWallet_Send-Success](https://blog.esprezzo.io/hs-
fs/hubfs/MyEtherWallet_Send-Success.jpg?width=2400&name=MyEtherWallet_Send-
Success.jpg)

  10. Clicking on the  **Check Status on Esprezzo.io** button will take you to the [transaction on the block explorer](https://explorer.esprezzo.io/transactions/). It may take a few seconds for the transaction to appear once you refresh. Here's an example transaction on the block explorer:  
![Esprezzo_official-Perkle-block-
explorer_transaction](https://blog.esprezzo.io/hs-fs/hubfs/Esprezzo_official-
Perkle-block-explorer_transaction.jpg?width=2400&name=Esprezzo_official-
Perkle-block-explorer_transaction.jpg)

**Note** : As of publishing time, MEWconnect does NOT display the balance of
PRKL or other custom tokens; it only displays ETH and officially supported
tokens.

Finally, here are some helpful links if you'd like to explore our other PRKL
wallets:

  * [Command line wallet](https://github.com/esprezzo/perkle/releases/tag/v0.1.0)
  * [Perkle wallet for Discord via PerkleBot](/esprezzo-libraries-perklebot-blockchain-discord-bot-smart-contract-perkle-tokens)

We hope you find this guide useful! If you have any questions or need further
assistance, please [ **join our Discord server**](https://discord.gg/uuCT89F)
and hit us up in the  **#support  **channel!

Topics: [News](https://blog.esprezzo.io/tag/news),
[Perkle](https://blog.esprezzo.io/tag/perkle)

![Jialin Luh](https://blog.esprezzo.io/hubfs/Jialin.png)

###### [Jialin Luh](https://blog.esprezzo.io/author/jialin-luh)

Jialin is a UX designer at Esprezzo, where she's bringing her passion for user
experience to blockchain tools. She's launched popular B2B and B2C products at
companies including Evernote and Speck Products.

[LinkedIn](https://www.linkedin.com/in/jialin/)

## Esprezzo and blockchain-related news for developers and business leaders

Best practices and industry news for growing your business with decentralized
and blockchain-integrated applications

### Subscribe Here!

### Recent Posts

### Posts by Tags

  * [News (14)](https://blog.esprezzo.io/tag/news)
  * [Events (12)](https://blog.esprezzo.io/tag/events)
  * [Product Updates (10)](https://blog.esprezzo.io/tag/product-updates)
  * [Perkle (9)](https://blog.esprezzo.io/tag/perkle)
  * [Research & Analysis (7)](https://blog.esprezzo.io/tag/research-analysis)
  * [Education (6)](https://blog.esprezzo.io/tag/education)
  * [Partnerships (5)](https://blog.esprezzo.io/tag/partnerships)
  * [Blockchain 101 (4)](https://blog.esprezzo.io/tag/blockchain-101)
  * [Press Release (1)](https://blog.esprezzo.io/tag/press-release)

See all

### Technology

[Perkle Protocol](https://esprezzo.io/perkle)

[GitHub](https://github.com/esprezzo)

### Company

[About](https://esprezzo.io/about)

[Blog](https://blog.esprezzo.io)

[Contact](https://esprezzo.io/about#contact)

### Connect

[Discord](https://discord.gg/uuCT89F)

[Twitter](https://twitter.com/esprezzoapp)

[LinkedIn](https://www.linkedin.com/company/esprezzo-app/)

**Stay in the know**

Get news and product updates from Esprezzo

[![esprezzo_logo_red-white_sept2020@2x](https://blog.esprezzo.io/hs-
fs/hubfs/esprezzo_logo_red-
white_sept2020@2x.png?width=263&name=esprezzo_logo_red-
white_sept2020@2x.png)](https://esprezzo.io)

©2020 Esprezzo. All rights reserved.

