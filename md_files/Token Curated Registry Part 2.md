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

#  Discovering TCR Part 2:  
Redesigning the TCR Stimulator

[research](https://outlierventures.io/research/)

Token Curated Registry Part 2

![](https://outlierventures.io/wp-
content/themes/ov/assets/images/ovweekly.svg)

![](https://outlierventures.io/wp-content/uploads/2018/02/ov_aron-150x150.jpg)

June 2019

Posted by

Aron van Ammers

CTO and Founding Partner

Before Outlier Ventures, Aron completed an MSc in Business Information
Technology and has over 15 years of experience in software development in the
roles of CTO, architect, designer, consultant, developer and systems engineer
in both start-up and enterprise environments. He has extensive knowledge and
hands-on experience with full stack software development, decentralised
systems and smart contracts....[read
more](https://outlierventures.io/team/aron-van-ammers/)

# Token curated registries are an exciting crypto-economic building block.

## By Aron van Ammers

Posted by Aron van Ammers - June 2019

![](https://outlierventures.io/wp-content/uploads/2018/02/ov_aron-150x150.jpg)

June 2019

Posted by

Aron van Ammers

CTO and Founding Partner

Before Outlier Ventures, Aron completed an MSc in Business Information
Technology and has over 15 years of experience in software development in the
roles of CTO, architect, designer, consultant, developer and systems engineer
in both start-up and enterprise environments. He has extensive knowledge and
hands-on experience with full stack software development, decentralised
systems and smart contracts....[read
more](https://outlierventures.io/team/aron-van-ammers/)

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

They promise to leverage the wisdom of the crowd in curating lists of things,
any type of things, through economic incentives. They are, however, still
mostly theoretical. Little experimentation and formal research has been
carried out into different forms and configurations of TCRs.

In this project, as part of Outlier Ventures’ Research Programme with the
Imperial Centre for Cryptocurrency Research and Engineering and in
collaboration with [Ocean Protocol](https://oceanprotocol.com/) and[
MusicMap](https://musicmap.info/), a group of six students from Imperial
College took on the task of building a TCR Simulator that allows for
experimentation in an isolated framework to learn what works and what doesn't.
We have been impressed with their results, which included a working product
with smart contracts deployed on Ethereum-compatible blockchains, field
testing with a small group of users and a proposal for a new TCR mechanism. If
you want to have a look at their work, you can use a[ live version of the TCR
simulator](https://tcrsim.outlierventures.io/) and[ run the code
yourself](https://github.com/OutlierVentures/Token-Curated-Registry-
Simulator).

This project is a great example of our aim at Outlier Ventures to advance best
practices in cutting edge technology through applied research.

In a series of four blogs, Matthew, Emma, Hailey, Ece, Yoon and Noel give a
candid look into how they executed the project and the results they produced.

### Plot twist

After hours of discussion amongst ourselves, we came to a conclusion - let’s
start over! Of course, we would need our supervisor’s input on this, so we
wrote him a 2-page Slack message (which really was 5 messages because of
Slack’s 2000 character limit).

_Hi Dominik,_

_After the meeting today with you and the Ocean protocol guys, we had a
thorough discussion about our current simulator implementation. With the
expectations of the Ocean Protocol guys in mind, we came to a new thought and
we wanted to ask for your opinion about our next choice of action._

_As you may have too, we noticed that the Ocean Protocol guys had a different
idea of our simulator and it was quite clear to us today that the Ocean
Protocol guys were more interested in the different TCR mechanisms rather than
the behaviours of the three agents. Therefore, we are considering switching to
what they had mentioned in the meeting, i.e. no longer simulating human
behaviours. We have noted your concerns in the case that we make this change,
then our simulator will not have a lot of elements to demonstrate, but as
there are pros and cons for both ideas, we wanted to discuss it with you._

_**Option 1:** Continuing our current work- Simulating the agents with
different behaviours, generating different actions and test the behaviours
against different TCR parameters/ a whole new TCR mechanism. _

_Pros:_

  * _wouldn’t have to scrap the whole thing;_
  * _able to compare different TCRs fairly;_
  * _active demonstrations possible with different results for our presentation._

_Cons:_

  * _the backend has to be very actively maintained;_
  * _any fundamental changes to the actions of the agents would lead to changes to the backend e.g. if the maintainer is allowed to propose one of the listees to become a maintainer;_
  * _group/time management would be difficult;_
  * _Simulating human behaviours is really challenging and not feasible within this time frame. Therefore we will implement basic human behaviours but we can’t guarantee that the end product will accurately reflect real-life scenario and therefore may not give concise results._
  * _Time-consuming, we do not believe that we will implement a good enough software engineer project in time_

_**Option 2:** A new approach with the suggestion of what Ocean guys said in
mind - Making a platform where (admins) can deploy TCRs with different
parameters. We will then let different users interact with the deployed TCRs
and let them ‘play’ with it and observe and analyse the different outcomes.
The focus would be on the Frontend for different user interactions. _

_Pros:_

  * _We can focus on the TCR mechanism design (which in the long run might be better for future TCR implementations), which would lead to less work at the backend as it only acts as an interface between the frontend and the TCR._
  * _As there seems to be always confusion whenever we have a call with the Ocean Protocol guys, this would allow us to be more on the same page with them._

_Cons:_

  * _Need to redesign the whole front end_
  * _Have to wait a long time for observations/results because no one would actually use it and there would be no fair comparison between the different TCRs hence leading to less demonstrative materials._

_We noticed that even though we try to devote a lot of time to this project,
due to upcoming courseworks in other modules and the exams that are coming up,
we realised that we have very limited time. It would be very ideal if all of
our goals for each checkpoints could be met, but as the project progressed, we
noticed that we were stuck on a lot of small decisions, and that took longer
than expected, which made us think about the new option more especially after
the meeting today._

_As mentioned under the cons of Option 1, if we were to continue our simulator
implementations, e.g. introducing new actions for the different type of agents
etc, it would cost us so much time updating the frontend and maintaining the
backend at the same time as we would continuously need to update both ends if
we decide to modify one of them. However, this “new idea” is completely
different from what have agreed on so far with you, so we would like to know
what you think of this idea and see if it is worth changing the plan now._

_If in the case we decide to take up on the new approach, we will think of a
way to accentuate our demonstration more so that the simulator users can
actually see and compare different mechanisms._

_Thank you for reading, we hope you will help us and share your thoughts! It
was a really long message, but it was worth it because we got the approval in
the end!_

### Re-designing

So after getting approval from Dominik, we set about re-designing our whole
front end. There are two main users of the system:

  * Players - the maintainers, contributors and users
  * Admin - the users who will define the rules of the TCR and observe the results of the players’ interactions

From this, we decided we needed to have 2 main screens for our different
users, so we split and programmed a brand new front end.

### Our progress

![Token Curated Registry Part 2 Outlier
Ventures](https://outlierventures.io/wp-
content/uploads/2019/05/Screenshot-2019-05-31-at-16.04.14.png)

Therefore, for this Friday, we designed our new frontend. The basic mockup
looks like the figure above. We have separate pages for the Admin and the
Players, and each Player will get their own profile with their account
informations.

Redesigning our frontend and changing our project allowed us to incorporate
music into our project. We have designed the frontend so that the players will
be able to submit the music of their choice to the TCR and also challenge and
withdraw their music if they wish to. Based on the amount of tokens the
players hold, they could become maintainers of the registry as well. We
thought of this as a type of a game; the players would be trying to maintain a
good list of music and also trying to getting their choice of music onto the
list while the admins who are interested in seeing the results of the
different TCR mechanisms will be able to do so as the players are actively
adding their music onto the TCR!

We think that our decision to change our project direction has made the
simulator more interactive. We also believe that it is better because the
general public may not be interested in seeing all the statistics for the
different TCR mechanisms but may be interested in being part of the different
agents of the TCR and also see good lists of music.

We still have a very long way to go as we actually need to implement different
TCR mechanisms and connect the TCR to our frontend. It was a really bold move
for us to scrap out everything we’ve done so far and to start over, but we
hope that this will be better in the long-run.



_This article is for information purposes only and does not constitute
investment advice. This article does not amount to an invitation or inducement
to buy or sell an investment nor does it solicit any such offer or invitation
in any jurisdiction._

_In all cases, readers should conduct their own investigation and analysis of
the data in the article. All statements of opinion and/or belief contained in
this article and all views expressed and all projections, forecasts or
statements relating to expectations regarding future events represent Outlier
Ventures Operation Limited own assessment and interpretation of information
available as at the date of this article._

___No responsibility or liability is accepted by Outlier Ventures Operations
Limited or Sapia Partners LLP for reliance on the contents of this article._

_Outlier Ventures is an Appointed Representative of Sapia Partners LLP, a firm
authorised and regulated by the Financial Conduct Authority (FCA)._

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

