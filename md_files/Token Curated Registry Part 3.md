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

# Discovering TCR Part 3:  
The new mechanism

[research](https://outlierventures.io/research/)

Token Curated Registry Part 3

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

## They promise to leverage the wisdom of the crowd in curating lists of
things, any type of things, through economic incentives. They are, however,
still mostly theoretical. Little experimentation and formal research has been
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

### Our goal

With the basic design of the front end done, now we have to implement actual
functionality - we have to make it alive!

We sat down and had a chat, finally deciding we should set up a web API in the
backend to create and deploy TCRs, and call user actions from the front end.

But when the deadline approached, we realized it’s actually more direct for
admins to deploy from the frontend, since all the factory contracts (e.g.
RegistryFactory) are already deployed, and provide methods to deploy contracts
with custom parameters. By doing that, we can also take advantage of MetaMask
to make the process smoother.

![Token Curated Registry Part 3 Outlier
Ventures](https://outlierventures.io/wp-
content/uploads/2019/05/Screenshot-2019-05-31-at-16.10.51.png)

This week we decided to connect everything together, the Smart Contract
Factory, the Front End and the Ganache Server, such that the admin users are
able to create a new TCR and deploy it to the ganache, and players are able to
submit new songs  
to the corresponding TCR.

Connecting the front end and the ganache is very similar to what we did before
the change of our simulator. We kept the TCR Connection class and also the
constructor function that initialises a Web3 instance with the contract
address and ABI.

Learning how to call the contract’s functions on the Registry.sol of the
forked tcr repository was not as easy as we expected, as we were very new to
the Web3 interface, we did not understand the owner’s manual completely, which
led to lots of confusion when we wanted to call the functions correctly. We
were particularly confused about calling the commitVote function, because it
is not on the Registry.sol, we were unable to call it with merely the ABI of
the Registry.sol, also, according to the owner’s manual, it told us to call
the voting function before calling commitVote, which made us more confused as
there is not a function named voting on the Registry.sol. Then, there was this
“magical moment” when we read about the Web3 documentation again, we realised
we have misunderstood the voting function mentioned on the manual, the voting
function is actually not a function, but a global variable on the Registry.sol
which could be accessed by calling it as a function using web3 in the front
end.

We changed the front end to the back end bit a lot in the last minute.

### Our New TCR Mechanism

During this week, we thought of a new TCR mechanism as follows:

Instead of having a Challenge button under the Pending List, we thought of a
mechanism where the Challenge button would be under the Accepted List. In
other words, every song that is inputted by the player will go under Pending
List and the maintainer will vote for every song added to see whether the song
should be accepted. From here, in order to lessen the work of the maintainer,
we would like to set a maximum bound of the number of items that can currently
be on the pending list as well as a time frame someone can challenge a
specific song. If there are too many items on the pending list, it will
overwhelm the maintainers of the registry, and therefore may lead to poor
decision making. In addition, we thought that a time frame would be necessary
for the challenge, as it would be meaningless if someone challenges an item a
few seconds after the maintainers approved the song. (With our new mechanism,
the challenge button will appear on the Accepted List, rather than the Pending
List. Therefore, we will no longer need the expiry time for the song to move
automatically from the Pending List to the Accepted List as the maintainer
will have to vote on every song that is submitted.)

Under this idea, to incentivise the contributors, we thought that having a
reward system for the contributors would be beneficial. For contributors who
contribute good songs (i.e. their songs are on the TCR Registry), they will be
rewarded with some “points” which will later be equivalent to a certain amount
of actual tokens. We thought this would enhance the quality of the TCR. Adding
on, to limit the “spammers” from continuously contributing poor songs, we
thought of having a fining system. The maintainers will view the items and if
they deem inappropriate and it happens repetitively, that contributor will be
fined for their actions and their fines will be added to the token pool that
will be distributed amongst the maintainers once they reject their request.

### Next steps

We hope to be able to deploy a fully functional TCR where users are able to do
more than just submitting songs - they should also be able to challenge
listees, vote on challenges, receive rewards, etc. If time allows, we’d also
like to start implementing our new TCR mechanism that we have thought about as
mentioned above.



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

