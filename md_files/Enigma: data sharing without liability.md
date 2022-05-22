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

# Enigma: data sharing without liability

[research](https://outlierventures.io/research/)

Enigma: data sharing without liability

![](https://outlierventures.io/wp-
content/themes/ov/assets/images/ovweekly.svg)

![](https://outlierventures.io/wp-
content/uploads/2018/11/155844779614799575-150x150.jpeg)

April 2020

Posted by

Theo Turner

Technology Analyst

Theo is an R&D software developer working with blockchain, machine learning
and the internet of things. In addition to building applications for internal
use, Theo completes technical due diligence on new projects and assists
Outlier’s portfolio companies with technical capabilities....[read
more](https://outlierventures.io/?post_type=team&p=3187)

In 2020's economy, business decisions are driven by data. Demand for data is
higher than ever, with organizations increasingly relying on external data
sources and data sharing to capture value. However, in the GDPR era, data
liability is a substantial risk, leading to a wealth of missed opportunities
in data due to privacy concerns. Read on to learn about our continued work
with Enigma, who are rethinking data security to encourage data sharing while
eliminating data liability risk.

Enigma is developing a blockchain-based protocol for sharing data responsibly
by preserving privacy not only during transmission but also at compute time.
We're excited to work with Enigma, as they are leveraging Trusted Execution
Environments (TEEs) that allow organisations to share data without risk of it
being revealed, even to the parties they choose to share their data with. With
Enigma, enterprises can gain insights about data shared between their partners
without direct access to any of the data.

In a previous blog post, we detailed a collaborative analytics product we have
been building on Enigma, which we have dubbed APEX (Analytics from Private
Execution). Machine learning, which is increasingly helping us to make better
business decisions, is the core focus of the software. The added ability to
share data without liability allows us to further improve these business
decisions, and we're now opening up what we've built to the world. To expand
on our previous post, we'll cover the data privacy aspects of the software,
enterprise use cases, as well as updates to the software, including a slick
new UI.

The Enigma network enables cryptographic guarantees of privacy by encrypting
data before it leaves enterprise premises. When inputting any data to the
network, it is first encrypted client-side, so we can be confident that there
is no way for the data to be read in transport. The data is decrypted in a
secret contract, a piece of publicly verifiable code at a public, immutable
address on a blockchain. Enterprises can be entirely confident that their data
is not able to be viewed by anyone, or that it can be intercepted by man-in-
the middle attacks.

Multiple enterprises can send their data into the same secret contract to
share data without revealing it. The contract, with publicly verifiable
compute logic, can output results based on the sum of all shared data without
revealing any individual particpant's dataset. With APEX, we have written
secret contracts which enable enterprises to perform machine learning on
shared data. We're opening up the tooling that has helped us make better
business decisions to the wider corporate space, and supercharging it by
allowing computation on shared datasets. All of this without data liability
risk, thanks to Enigma.

APEX allows enterprises to perform two different forms of machine learning on
shared data, as well as collaborative model training. The first form of
machine learning we chose to include is clustering, a way of grouping data
according to their closeness to relative density centers. A simple example are
the inhabitants of various cities in a country, which may be clustered into,
or grouped by, their respective cities. Each cluster comes with a centroid, a
relative center of density, which in our example corresponds to the center of
each city. Clustering is a powerful form of machine learning for grouping a
variety of data types, but is particularly potent when it comes to geographic
customer data. Our analytics platform allows clustering to be performed on
latitude/longitude data, with the flagship use case for telecommunications
infrastructure placement: by clustering customer locations, telco providers
learn the optimal placements of cell phone towers to guarantee coverage across
their networks, or optimal retail store locations to be as close to as many
customers as possible. With multiple enterprises sharing data, businesses get
analytics for customers they don't even know about, all without those
customers being revealed to them, thanks to Enigma. The clustering in APEX can
be generalized to a range of other geographic optimisation challenges, such as
car routing for ride sharing applications, and even non-geographic problems
such as identifying fraudulent transactions.

The second form of machine learning available in APEX is classification.
Classification allows for concrete segmentation of data points into classes,
as the name implies. Unlike clustering, classification does not judge by
relative density of data, but by training data input by its users. In the case
of our software, that training data may be contributed by enterprises,
allowing them to classify customers according to any metric of their choice,
such as jurisdiction. A particularly strong point of Enigma's data sharing
without liability is the possibility to train machine learning models
collaboratively. This allows enterprises to create more powerful AI than what
has been possible previously, as the AI is able to learn from the sum of all
knowledge of the enterprises contributing their data. This allows enterprises
to gain insights about all of the potential customers in an industry, rather
than just their own customers. For example, our software allows telco
providers to know the total size of the addressable market in different
countries far more accurately than before, as the result is based on real
data, rather than estimations. Collaborative model training can be further
extended to a myriad of use cases for machine learning, such as crop yield
predictions and insurance fraud identification, featuring significantly
improved accuracy and quality of insights thanks to Enigma data sharing.

[Sign up for the launch event of APEX
here.](https://www.crowdcast.io/e/enigma)

Posted by Theo Turner - April 2020

![](https://outlierventures.io/wp-
content/uploads/2018/11/155844779614799575-150x150.jpeg)

April 2020

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

