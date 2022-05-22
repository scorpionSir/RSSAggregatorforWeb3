[ ![](https://outlierventures.io/wp-
content/themes/ov/assets/images/outlierventureslogo.svg) ](/)

  * [Base Camp Accelerator](https://outlierventures.io/base-camp/)
  * [Ascent Scaling Program](https://outlierventures.io/ascent/ "Ascent")
  * [Our Portfolio](/portfolio/)
  * [News & Reports](https://outlierventures.io/news/)
  * [Diffusion Live](https://diffusion.events/)

![](https://outlierventures.io/wp-content/themes/ov/assets/images/close.svg)

  * [Base Camp Accelerator](https://outlierventures.io/base-camp/)
    * [DeFi Base Camp](https://outlierventures.io/base-camp/defi-base-camp)
    * [Filecoin Base Camp](https://outlierventures.io/filecoin-base-camp/)
    * [Hedera Base Camp](https://outlierventures.io/base-camp/hedera-base-camp)
    * [Polkadot Base Camp](https://outlierventures.io/base-camp/polkadot-base-camp)
    * [Polygon Base Camp](https://outlierventures.io/base-camp/polygon-base-camp)
  * [Ascent Scaling Program](https://outlierventures.io/ascent/)
  * [News & Reports](https://outlierventures.io/intelligence/ "Intelligence")
    * [Open Metaverse Thesis](https://outlierventures.io/research/the-open-metaverse-os/)
    * [Newsletter Signup](https://outlierventures.io/sign-up/ "Sign Up")
    * [Special Reports](https://outlierventures.io/reports/ "Reports")
    * [Research Articles](/research/ "Research")
    * [Company News](/news/ "News")
    * [Metaverse Podcast](/podcast-overview/ "Podcasts")
  * [About Us](https://outlierventures.io/about-us/ "About us")
    * [Our Portfolio](/portfolio/ "Portfolio")
    * [Team](/team/ "Team")
    * [Press](https://outlierventures.io/press/ "Press")
    * [Offices](https://outlierventures.io/offices/ "Offices")
    * [OV Careers](https://outlierventures.io/careers/)
    * [Portfolio Jobs](https://jobs.outlierventures.io/jobs)

[__](https://www.linkedin.com/company/OutlierVentures)[__](https://twitter.com/oviohq)[__](https://t.me/outlierventures)[![](https://ovio.wpengine.com/wp-
content/themes/ov/assets/images/crunchbase.svg)](https://angel.co/outlierventures-
io/)[__](https://github.com/OutlierVentures)[__](https://www.youtube.com/channel/UCd_K-
AgiS2XV8_iuRQ7JyNQ)[__](https://discord.gg/qjcZKsfXXM)

[research](https://outlierventures.io/research/)

# ArBot, a Fetch-Ocean integration

[research](https://outlierventures.io/research/)

ArBot, a Fetch.AI-Ocean integration

![](https://outlierventures.io/wp-
content/themes/ov/assets/images/ovweekly.svg)

![](https://outlierventures.io/wp-
content/uploads/2018/11/155844779614799575-150x150.jpeg)

September 2019

Posted by

Theo Turner

Technology Analyst

Theo is an R&D software developer working with blockchain, machine learning
and the internet of things. In addition to building applications for internal
use, Theo completes technical due diligence on new projects and assists
Outlier’s portfolio companies with technical capabilities....[read
more](https://outlierventures.io/?post_type=team&p=3187)

## In the lead-up to the Diffusion DevCon, we at Outlier Ventures continue
expanding and developing The Convergence Stack to make it as easy as possible
for developers to use. Today, we’re releasing ArBot, a data arbitrage bot and
tool for moving datasets between the Fetch.AI and Ocean Protocol marketplaces.
Read on to learn how you can perform arbitrage with data as an asset.

Posted by Theo Turner - September 2019

![](https://outlierventures.io/wp-
content/uploads/2018/11/155844779614799575-150x150.jpeg)

September 2019

Posted by

Theo Turner

Technology Analyst

Theo is an R&D software developer working with blockchain, machine learning
and the internet of things. In addition to building applications for internal
use, Theo completes technical due diligence on new projects and assists
Outlier’s portfolio companies with technical capabilities....[read
more](https://outlierventures.io/?post_type=team&p=3187)

## Related Posts

[ ![](https://outlierventures.io/wp-content/uploads/2022/05/the-illusion-of-a-
decentralised-metaverse-
thumbnail-800x600.jpg)](https://outlierventures.io/research/the-illusion-of-a-
decentralized-metaverse/) [The Illusion of a Decentralized
Metaverse](https://outlierventures.io/research/the-illusion-of-a-
decentralized-metaverse/)

May 2022  
Karim Halabi

[ ![DAO Governance Article](https://outlierventures.io/wp-
content/uploads/2022/04/DAO-
Thumb.png)](https://outlierventures.io/research/governance-in-the-age-of-the-
dao-tooling-and-frameworks/) [Governance in the Age of the DAO: Tooling and
Frameworks](https://outlierventures.io/research/governance-in-the-age-of-the-
dao-tooling-and-frameworks/)

April 2022  
Martin Saps

### ![ArBot, a Fetch.AI-Ocean integration Outlier
Ventures](https://outlierventures.io/wp-content/uploads/2019/09/Screen-
Shot-2019-09-16-at-11.23.21.png)

###

###



### **Introducing ArBot**

Ocean Protocol is a data marketplace. On the platform, datasets carry value
according to their usefulness. Fetch.AI, in contrast, is an IoT economy which
routes data to those who find it most useful. Through this routing, the data
provider is paid by the data consumer for their services. Both Ocean Protocol
and Fetch.AI wish to leverage IoT datasets, with a focus on performance in
training machine learning algorithms.

There is a clear opportunity for bridging the marketplaces of Fetch.AI and
Ocean Protocol. This is where the back-end of ArBot shines: through a easy-to-
use pip module, anyone can move datasets between the two marketplaces,
establishing a single, liquid data economy for the Convergence Stack.

Any given dataset may carry one price on Ocean Protocol and another on
Fetch.AI. This opens up the opportunity to perform arbitrage with data as an
asset. ArBot does exactly this: by translating the token value to an
independent measure of value, it is possible to identify profit-making
opportunities. After accounting for network fees, ArBot executes trades only
in cases where profit can be made.

ArBot is a tool for triangular arbitrage with Fetch tokens, Ocean tokens and
_data_. Where things get complicated is judging the value of datasets: in
contrast to the tokens, datasets are non-fungible. To make matters worse, two
completely different datasets could be equally valuable. Consider a plant-
identifying AI which could use either a daffodil dataset or a tulip dataset to
improve its accuracy by 2%. To the AI, both are equally valuable, however it
would not be immediately clear to a human which is worth more.



### **Managing Data Arbitrage Risk with Specificity**

The key parameter for executing execution risk in data arbitrage is
_specificity_. By limiting ArBot’s search space, we get stronger guarantees
that the consumer it is selling to is receiving what they expect. Thus,
specificity allows users of ArBot to choose their own appetite for risk. At
low levels of specificity, there is a high risk that the consumer will reject
the dataset offering, but there are far more opportunities available. At high
levels of specificity, there are fewer opportunities, but the consumer is much
more likely to buy.

An example of a high-risk strategy for ArBot is feeding it the query ‘daffodil
flowers.’ There may be a seller of data labelled _daffodil flowers_ on Ocean
Protocol and a buyer looking for _daffodil flowers_ on Fetch.AI, however their
uses for the data might be different. The seller could be in possession of
art, and the buyer may want to train their flower-identifying AI with many
pictures of daffodils. In this case, provided the seller’s price is lower than
the buyer’s (factoring in network fees), ArBot will take the risk of the buyer
not wanting to follow through with the transaction. The benefit of this
strategy, however, is that there will likely be a multitude of results for the
query _daffodil flowers_ , many of which will result in successful arbitrage.

In contrast, a low-risk strategy would be to feed ArBot the query ‘1000
daffodil flowers classification AI dataset.’ In this case, there will likely
be few results, however, the buyer and seller likely refer to the exact same
thing. With a low-risk strategy, the probability of failed arbitrage is low.



### **Getting Started**

ArBot is open-source and available on the [Outlier Ventures
GitHub](https://github.com/OutlierVentures). It is one of The Convergence
Stack _bridges_ , joining the ANVIL and H2O family. As an integration of
Convergence Stack technologies, ArBot is an example of what we will be looking
for in the Integration Track of the [Diffusion
DevCon](https://diffusion.events/). If you think you can do better, [sign up
for our Diffusion DevCon](https://diffusion.events/) and prove it!

Sign up to

![](https://outlierventures.io/wp-
content/themes/ov/assets/images/ovweekly.svg)

![](https://outlierventures.io/wp-
content/themes/ov/assets/images/outlierventureslogo-dark.svg)

  * [Diffusion](https://outlierventures.io/diffusion/ "Diffusion")
    * [Events](/events/ "Events")
    * [Podcasts](/podcasts/ "Podcasts")
  * [About us](https://outlierventures.io/about-us/ "About us")
    * [Team](/team/ "Team")
    * [Press](https://outlierventures.io/press/ "Press")
    * [Offices](https://outlierventures.io/offices/ "Offices")
    * [Sitemap](https://outlierventures.io/sitemap/ "Sitemap")
  * [Terms and conditions](https://outlierventures.io/terms-and-conditions/ "Terms and conditions")
  * [Privacy Policy](https://outlierventures.io/privacy-policy/ "Privacy policy")
  * [Security Procedures](https://outlierventures.io/security-procedures/ "Security Procedures")

  * [The Open Metaverse Thesis](https://outlierventures.io/research/the-open-metaverse-os/)
    * [Base Camp Accelerator](https://outlierventures.io/base-camp/)
    * [Ascent Scaling Program](https://outlierventures.io/ascent/)
    * [Portfolio](/portfolio)
  * [News](https://outlierventures.io/intelligence/)
    * [Industry Reports](/reports/)
    * [Research Articles](/research/)
    * [Company News](/news/)
    * [OV Weekly Newsletter](/sign-up/)

[__](https://www.linkedin.com/company/OutlierVentures)[__](https://twitter.com/oviohq)[__](https://t.me/outlierventures)[![](https://ovio.wpengine.com/wp-
content/themes/ov/assets/images/crunchbase.svg)](https://angel.co/outlierventures-
io/)[__](https://github.com/OutlierVentures)[__](https://www.youtube.com/channel/UCd_K-
AgiS2XV8_iuRQ7JyNQ)[__](https://discord.gg/qjcZKsfXXM)

![](https://outlierventures.io/wp-content/uploads/2019/05/UKBAA-full-
logo_50px.png) ![](https://outlierventures.io/wp-
content/uploads/2019/05/chamber-logo-white_55px.png)
![](https://outlierventures.io/wp-content/uploads/2019/05/BVCA.png)
![](https://outlierventures.io/wp-content/uploads/2019/04/WSBA.png)

Outlier Ventures Operations Limited is registered in England and Wales with
company registration number 10722638.

![](https://outlierventures.io/wp-
content/themes/ov/assets/images/ovweekly.svg)

