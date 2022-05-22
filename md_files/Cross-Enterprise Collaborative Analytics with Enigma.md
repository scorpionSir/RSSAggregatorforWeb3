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

# Cross-Enterprise Collaborative Analytics with Enigma

[research](https://outlierventures.io/research/)

Cross-Enterprise Collaborative Analytics with Enigma

![](https://outlierventures.io/wp-
content/themes/ov/assets/images/ovweekly.svg)

![](https://outlierventures.io/wp-
content/uploads/2018/11/155844779614799575-150x150.jpeg)

January 2020

Posted by

Theo Turner

Technology Analyst

Theo is an R&D software developer working with blockchain, machine learning
and the internet of things. In addition to building applications for internal
use, Theo completes technical due diligence on new projects and assists
Outlier’s portfolio companies with technical capabilities....[read
more](https://outlierventures.io/?post_type=team&p=3187)

### Imagine being able to send your data to someone else to analyse and gain
insights from without that data actually being revealed. Enigma, springing to
life from MIT’s D-Lab, makes that promise not only possible, but practical
today. Read on to find out how we have used Enigma’s technology to create a
collaborative analytics PoC for customer location data - all while preserving
the privacy of consumers _and_ the enterprises they buy from.

Posted by Theo Turner - January 2020

![](https://outlierventures.io/wp-
content/uploads/2018/11/155844779614799575-150x150.jpeg)

January 2020

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

Homomorphic encryption and multi-party computation have long been heralded as
the advent of privacy-preserving outsourced compute, however, for practical
applications, these technologies have been in research limbo since the 1970s.
Leveraging a new technology from Intel chipsets known as SGX, Enigma has
created a practical implementation of private compute in the Rust programming
language.

Rust, an emerging systems-level language, drives the core compute logic of
Enigma’s private compute, as well as the platform’s user-defined logic. Rust
is focused on safety and speed, rivaling functional languages in the former
and C/C++ in the latter. Enigma makes use of blockchain to co-ordinate and
mediate trust between its actors, with compute tasks deployed in privacy-
preserving smart contracts known as _secret contracts_.

Secret contracts encapsulate a program state that cannot be viewed by anyone
but the contract itself. This allows multiple parties to input data to a
secret contract and compute to take place across all those inputs without any
individual party’s data being revealed to any other party. Enigma enables
collaborative analytics: self-interested parties may safely contribute any and
all information they hold, without any chance of it being revealed, in the
knowledge that secret contracts will output to them insights based on not only
their own data, but the data of all other collaborating enterprises as well.

So what exactly can be done, in code, today? Turning our attention to modern
analytics, we aimed to implement machine learning models for collaborative
analytics using secret contracts. The results were highly successful: with a
focus on customer location data, we were able to implement both clustering and
classification models in a working PoC.

The first step in implementing our models was making them practical for large-
scale competing enterprises to use. This demanded serialisation and
deserialisation of large inputs, so databases can be contributed, rather than
single data points. Enigma’s secret contract environment is unrestrictive
compared with the vast majority of smart contract systems, and allowed us to
derive the serialisation and deserialisation traits when implementing our data
structures. With a small amount of additional input sanitisation, we were
quickly able to create a data input mechanism for multiple collaborating
enterprises.

With location data from multiple parties safely in a secret contract, we
turned our attention to the first machine learning model: classification.
Secret contracts allow the use of external libraries, a rarity in smart
contract environments, making this a straightforward exercise with Enigma. The
complexity of achieving the same task using competing solutions cannot be
understated: Enigma is leading the charge in the private smart contract space.
With an import of cogset, we quickly had a k-means clustering model
functional. Given the location-focused nature of the data, we employed
Enigma’s capable JavaScript libraries and a React.JS front-end to draw our
outputs on a Google map.

So how can this be applied to the real world? Consider a competitive customer-
focused environment, such as telecommunications. Customers frequently move
between providers, so infrastructure and budgeting requirements have large,
often unpredictable variance. Collaborative analytics significantly mitigates
this problem: each provider can contribute their customer data without any
fear of it being revealed, and the clustering algorithm can be used to
optimally place cell phone towers or retail stores. The algorithm analyses the
data from all of the collaborating parties, so insights cover the entire
addressable market, not just the customers that the individual providers are
aware of.

Having covered a fundamental unsupervised learning technique with clustering,
we chose to implement a supervised learning model: classification.
Classification is useful for determining set membership, for example the type
of phone an individual tends to prefer, or the elevation a customer spends
most of their time at. Unlike unsupervised learning techniques, supervised
learning involves the _training_ of a model to improve the accuracy of its
outputs. This presents a unique opportunity for enterprises using Enigma:
collaborative model training, where the expertise of each collaborating party
can be combined into a single entity with all of the knowledge of an entire
industry, all without revealing any of the individual parties’ data. Thanks to
Enigma’s unrestrictive secret contracts, we were quickly able to implement a
collaborative classifier, again with serialisation / deserialisation of
inputs, external library support and outputs rendered in a React.JS UI.

The code for [Enigma](https://github.com/enigmampc) as well as our [cross-
enterprise collaborative analytics
PoC](https://github.com/OutlierVentures/Enigma-Collaborative-Analytics) are
open-source and available on GitHub. While the private and collaborative
compute space is still largely in the research stage, Enigma is live and
working today, allowing competing enterprises to gain insights through
collaboration that have not been possible until now. To learn more about
Enigma, take a look at their [website](https://enigma.co/), and to get started
with your own private compute application, check out the excellent [quick
start guide](https://enigma.co/discovery-documentation/Walkthrough/).



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

