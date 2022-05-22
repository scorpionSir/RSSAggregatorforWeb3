[](https://medium.com/)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/4c5f77bfddfa&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](https://medium.com/)

[Home](https://medium.com/)

[Notifications](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![Enigma](https://miro.medium.com/fit/c/64/64/1*aIQTqQDM97_LBgHTkHGqcA.png)](https://blog.enigma.co/?source=post_page
-----4c5f77bfddfa--------------------------------)

Published in

[Enigma

](https://blog.enigma.co/?source=post_page-----
4c5f77bfddfa--------------------------------)

[![Enigma
Project](https://miro.medium.com/fit/c/96/96/2*2SRmuGkTHWle_KyV3jfGhQ.png)](https://medium.com/@EnigmaMPC?source=post_page
-----4c5f77bfddfa--------------------------------)

[Enigma Project](https://medium.com/@EnigmaMPC?source=post_page-----
4c5f77bfddfa--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F4f5f09fa22fb&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fsafetrace-
april-2020-development-
update-4c5f77bfddfa&user=Enigma+Project&userId=4f5f09fa22fb&source=post_page-4f5f09fa22fb
----4c5f77bfddfa---------------------follow_byline-----------)

Apr 22, 2020

·

8 min read

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F4c5f77bfddfa&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fsafetrace-
april-2020-development-
update-4c5f77bfddfa&source=--------------------------bookmark_header-----------)

[

Save

](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F4c5f77bfddfa&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fsafetrace-
april-2020-development-
update-4c5f77bfddfa&source=--------------------------bookmark_header-----------)

# SafeTrace: April 2020 Development Update

## We’ve built an MVP demo and front-end integration, joined the TCN
Coalition, and will be hosting an upcoming webinar with Outlier Ventures.
Learn more on how you can get involved below!

![](https://miro.medium.com/max/1400/1*59iHLCJDp0bMSqGbrmknXg.png)

As the COVID-19 pandemic continues to disrupt global economies and daily life,
we at Enigma have continued our development work on **SafeTrace:** a privacy-
preserving data sharing and analytics platform for contact tracing.

Today we’re writing to share some major updates on our work since our [initial
SafeTrace announcement](/safetrace-privacy-preserving-contact-tracing-for-
covid-19-c5ae8e1afa93). This includes:

  * a **functional MVP demo** of SafeTrace, including full video
  * a basic **front-end integration** for user data ingestion
  * our new **collaboration with the**[ **TCN Coalition**](https://tcn-coalition.org/)
  * an upcoming explanatory [webinar](https://www.crowdcast.io/e/enigma/register) with the [Outlier Ventures](http://outlierventures.io) team

In this post we’ll recap some important notes about SafeTrace specifically and
digital contact tracing generally before getting into more details about all
these exciting developments and our next steps for scaling SafeTrace. Please
read to the end if you’d like to get involved with Enigma’s ongoing efforts to
fight COVID-19 while protecting user privacy!

 _Note: all our work is open-source and available on_[
_GitHub_](https://github.com/enigmampc/safetrace) _._

[

## enigmampc/SafeTrace

### Privacy preserving voluntary COVID-19 self-reporting platform for contact
tracing. Share your (encrypted) location…

github.com

](https://github.com/enigmampc/safetrace)

# An Overview of Digital Contact Tracing

Contact tracing has proven to be helpful in preventing the spread of
pandemics, but it has also historically been limited by the time and capacity
of health care workers trained in contact tracing. Smartphones, and the data
they collect, can dramatically improve contract tracing. Digital contact
tracing can be extremely valuable in these areas:

  *  **Individual awareness:** Users can know if they have been in close proximity with a diagnosed person, allowing them to self-quarantine.
  *  **Social awareness:** Digital contact tracing can be used for preemptive measures such as visualizing likely hotspots where individuals who test positive have recently congregated, such as grocery stores or community organizations. This can expedite the contact tracing process for healthcare professionals and inform decisions on which areas to clean and secure.
  *  **Contribution to research:** Users can share their data to advance epidemiology research. (This becomes more relevant further down the road, but there are techniques like[ differential privacy](https://en.wikipedia.org/wiki/Differential_privacy) that can help users safely share data for research.)

While digital contact tracing offers a lot of potential for COVID-19
prevention and mitigation, there are still real risks (such as threats to data
privacy) and difficult challenges (such as data silos) to overcome. Our work
on SafeTrace is meant to address these risks and challenges.

# The Advantages of SafeTrace

 **SafeTrace is an API which connects to a** **privacy-preserving storage and
private computation service**. This means that many different applications
(such as a web application or a mobile application) can enable its users to
submit encrypted user data via the SafeTrace API and receive results, without
ever revealing plaintext data to anyone, including the SafeTrace server
operator or the application. You can see how data is securely shared with
SafeTrace API [here on our Github
repo](https://github.com/enigmampc/SafeTrace).

SafeTrace stores encrypted data from users, performs analysis on that data,
and allows for two types of output: an **individual analysis** , which is
custom-generated and accessible only for each user, and a **global analysis**
, which all users can access. Users opt-in to share data with each analysis.

There are two other leading implementations of digital contact tracing that
come with tradeoffs: peer-to-peer bluetooth data exchange and sharing location
data of diagnosed patients with a centralized entity.

Peer-to-peer bluetooth data exchange means that two devices that are in close
proximity to each other exchange randomly generated device IDs with each
other. Once a user is diagnosed with COVID-19, she shares all of her randomly
generated user IDs with a centralized server, which can be queried by other
users to determine whether they’ve had high risk interactions. Centralized
approaches depend on diagnosed users to share their location and health
information in a way (plaintext, anonymized or hashed) that jeopardizes the
privacy of the infected user. These results are then shared with the general
public. The diagram below captures the main trade-offs of these approaches:

![](https://miro.medium.com/max/1400/1*-HfjeVjj_mP-F7r1D7gGcA.png)

A comparison of digital contact tracing solutions.

#  **Major SafeTrace Updates**

With this context, we can now proudly present the recent progress we’ve made
on SafeTrace — both independently and with our new partners!

##  _Functional MVP demo_

During the last few weeks, **we built a functional MVP for the SafeTrace
API.** This MVP allows users to share their location and infection status in a
privacy-preserving manner and receive individual reports showing whether they
have been in close spatiotemporal proximity with a diagnosed patient.

Users:

  * Encrypt location and infection status on their device
  * Share encrypted data with SafeTrace API and run query
  * Receive results from SafeTrace API that can only be accessed by the user

You can see a demo of SafeTrace MVP
[here](https://forum.enigma.co/t/safetrace-api-demo/1502) on our developers
forum.

[

## SafeTrace API Demo

### Hi everyone! As you may know, our team has been developing SafeTrace for
privacy-preserving contact tracing. Last week…

forum.enigma.co

](https://forum.enigma.co/t/safetrace-api-demo/1502)

##  _Front-end integration_

While SafeTrace is primarily an API for contact tracing applications, **we
also built a barebones web interface** to allow users to submit location data
and infection status leveraging Google Maps. This is currently only used for
testing purposes.

![](https://miro.medium.com/max/1400/1*UupNilf-qR6JbEzJ5RbKhw.png)

Front-end SafeTrace designs.

We’re currently seeking collaborators in a variety of areas, and welcome
contributions on our open-source repository. In particular we are looking for:

  * Existing contract tracing applications to Companies, products, or applications who have access to user location data and would be willing to enable their users to opt-in to SafeTrace participation
  * Companies, products, or applications who have access to user location data and would be willing to enable their users to opt-in to SafeTrace participation
  * Public health departments, research or medical institutions who would be interested in a limited trial of SafeTrace
  * Researchers or institutions who have epidemiological, disease spread modeling, or behavioral research projects that could benefit from access to highly detailed, granular, and private user location history data and could help design new analysis.

 _Big thanks to our friends at_[ _Protofire_](http://protofire.io) _for their
contributions!_

## Collaboration with TCN Coalition

Of course, all of this work requires partners and and collaborators in order
to scale and make a meaningful impact. For this reason, we’re excited to have
joined the [TCN Coalition](https://www.tcn-coalition.org), a global coalition
for privacy-first digital contact tracing protocols.

While TCN has focused primarily on Bluetooth-based methods for contact
tracing, the SafeTrace API can be complementary to Bluetooth models. Currently
the Bluetooth model doesn’t require location data in order to report
handshakes; however, integrating location data helps strengthen the model:

  *  **Scaling server to client (database to application) communication.** When a user needs to query the server for TCNs, should she get all TCNs or a subset of TCNs that’s relevant for her? One way to do this is by creating location based tags, which can reveal sensitive data. Here’s a [quick write up on how SafeTrace can be helpful here](https://docs.google.com/document/d/17kfcsSQr-EY5XOISScPBJP_eLVU0iexBfQuOGfjVFMM/edit).
  *  **Additional analysis geared towards authoritie** s — applications that integrate the TCN protocol could also allow their users to share location data in a privacy preserving manner to create risk heat-maps or similar analyses. These maps are extremely useful for research purposes such as environmental contamination analysis or for taking proactive measures and reducing the lag between infection reporting and containment response.

We are currently contributing to the Client to Server and Server to Server
working groups at TCN and look forward to expanding our efforts together!

# What’s Next for SafeTrace?

As we mentioned before, **all of the benefits of contact tracing are realized
when it is performed at scale.** As an API, SafeTrace aims to achieve scale by
working with digital contact tracing applications and other applications that
already collect user location and health data.

##  _Digital contact tracing applications_

Our team has been in close communication with several GPS location-based
contact tracing applications that are currently being built. We are working
with these teams to understand scalability and load requirements for the
SafeTrace API. Future work in this area will be aimed at improving
compatibility with a wider range of applications, and developing the planned
“global view” analysis.

In addition to these GPS efforts, we are seeing that SafeTrace API can also
help Bluetooth based contact tracing applications to effectively scale while
preserving privacy of sensitive user data.

##  _Mobile apps with location tracking_

Another way to reach scale is go directly to existing applications which have
required data, rather than starting data collection from scratch and trying to
achieve mass adoption. Most mobile applications already collect user location
data. These apps can contribute to digital contact tracing efforts in two
ways:

  * Allow users to download location data, similar to what is enabled by [Google Maps Timeline](https://www.google.com/maps/timeline?pb) and [Google Take-out](https://takeout.google.com/settings/takeout?pli=1). Users would then report their symptoms or test status and submit the data to SafeTrace API.
  *  _Native integration:_ Applications can build native survey tools to ask users about their symptoms and allow them to opt-in to sharing location and health data via an integration with the SafeTrace API. This ensures that users do not share any sensitive information with the application server.

We are in the process of getting feedback from mobile application developers
right now. _If you know people working on products that collect GPS location,
we would like to talk to them!_

##  _Other data sources_

A third, much more complex option is to use privacy-preserving computations to
merge data sets from different organizations like telcos and healthcare
clinics. While this approach would ensure a reliable way to collect data, the
coordination of large entities is not a trivial task.

We’re very excited about all this progress we have made and continue to make,
and we’re especially encouraged by our work within the [TCN
Coalition.](https://www.tcn-coalition.org) We are constantly looking for new
collaborators, including epidemiologists and health professionals, Rust
programmers **,** developers and engineers with Intel SGX experience, mapping
and visualization experts, and more.

If you are interested in getting involved in any capacity, please join us in
our primary channels:

  1. We encourage contributors to visit [CONTRIBUTE.MD](https://github.com/enigmampc/SafeTrace/blob/master/CONTRIBUTE.md) and open issues in our repo with questions and contributions.
  2. Join our team and community on the [Enigma Developers Forum](http://forum.enigma.co/) to discuss your ideas and feedback on our work so far, in particular [this thread](https://forum.enigma.co/t/safetrace-privacy-preserving-contact-tracing-for-covid-19/1476).
  3. Join our official [Enigma Discord](https://discord.gg/YH7f9Hx) and talk with us on the #safetrace channel.

If you’re interested in learning more about SafeTrace, **our team will be
holding a**[ **webinar**](https://www.crowdcast.io/e/enigma/register) **with
our friends at Outlier Ventures on April 30th.** We’ll be presenting our work
on SafeTrace as well as [APEX](https://outlierventures.io/research/enigma-
data-sharing-without-liability/), **** Outlier Ventures’ AI-powered analytics
platform built on Enigma.

Please join us for a live demo of privacy-preserving analytics and machine
learning for COVID-19 data, as well as a discussion between Outlier Ventures
and Enigma on the future of private compute in epidemiology. RSVP here!

[

## COVID-19 Contact Tracing with Enigma - Crowdcast

### Join us for a live demo of privacy-preserving analytics and machine
learning for COVID-19 data, and a discussion of the…

www.crowdcast.io

](https://www.crowdcast.io/e/enigma/register)

Together, we can build solutions that protect our universal right to privacy
as well as public health. Thank you for reading, and we look forward to
collaborating with you!

 _— The Enigma Team_

![](https://miro.medium.com/max/1400/0*yn0YDYHg_McquOFD.png)

 **To discuss the Enigma protocol or receive technical support:  
**[
_Forum_](http://forum.enigma.co/?source=post_page---------------------------)
_|_[
_Discord_](https://discord.gg/SJK32GY?source=post_page---------------------------)
_|_[
_Twitter_](https://twitter.com/enigmampc?source=post_page---------------------------)

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fenigmampc%2F4c5f77bfddfa&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fsafetrace-
april-2020-development-
update-4c5f77bfddfa&user=Enigma+Project&userId=4f5f09fa22fb&source=-----4c5f77bfddfa
---------------------clap_footer-----------)

\--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fenigmampc%2F4c5f77bfddfa&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fsafetrace-
april-2020-development-
update-4c5f77bfddfa&user=Enigma+Project&userId=4f5f09fa22fb&source=-----4c5f77bfddfa
---------------------clap_footer-----------)

\--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fenigmampc%2F4c5f77bfddfa&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fsafetrace-
april-2020-development-
update-4c5f77bfddfa&user=Enigma+Project&userId=4f5f09fa22fb&source=-----4c5f77bfddfa
---------------------clap_footer-----------)

\--

[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F4c5f77bfddfa&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fsafetrace-
april-2020-development-
update-4c5f77bfddfa&source=--------------------------bookmark_footer-----------)

## [More from Enigma](https://blog.enigma.co/?source=post_page-----
4c5f77bfddfa--------------------------------)

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fcollection%2Fenigmampc%2F4c5f77bfddfa&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fsafetrace-
april-2020-development-
update-4c5f77bfddfa&collection=Enigma&collectionId=6cb5d792f282&source=post_page
-----4c5f77bfddfa---------------------follow_footer-----------)

Official Blog of Enigma - Securing the Decentralized Web.

[Read more from Enigma](https://blog.enigma.co/?source=post_page-----
4c5f77bfddfa--------------------------------)

## Recommended from Medium

[[![Abass
Sesay](https://miro.medium.com/fit/c/40/40/2*3owGTU0vmNuUrKpH84kGbg.jpeg)](https://bascoe10.medium.com/?source=post_internal_links
---------0----------------------------)

[Abass Sesay

](https://bascoe10.medium.com/?source=post_internal_links---------
0----------------------------)

## Book Write-up — Hack The Box

![](https://miro.medium.com/focal/112/112/50/50/1*FvMUSVz5v0KAApgcuo_dMg.png)](https://bascoe10.medium.com/book-
write-up-hack-the-box-d3287644039a?source=post_internal_links---------
0----------------------------)

[[![Irma
Victoria](https://miro.medium.com/fit/c/40/40/1*dmbNkD5D-u45r44go_cf0g.png)](https://humankinds2010.medium.com/?source=post_internal_links
---------1----------------------------)

[Irma Victoria

](https://humankinds2010.medium.com/?source=post_internal_links---------
1----------------------------)

## {UPDATE} Hebrew Talk Hack Free Resources Generator

](https://humankinds2010.medium.com/update-hebrew-talk-hack-free-resources-
generator-11b2ecca3891?source=post_internal_links---------
1----------------------------)

[[![Ralina
Guinevere](https://miro.medium.com/fit/c/40/40/1*dmbNkD5D-u45r44go_cf0g.png)](https://separativeness1978.medium.com/?source=post_internal_links
---------2----------------------------)

[Ralina Guinevere

](https://separativeness1978.medium.com/?source=post_internal_links---------
2----------------------------)

## {UPDATE} PathPix Wild Hack Free Resources Generator

](https://separativeness1978.medium.com/update-pathpix-wild-hack-free-
resources-generator-7c02f670a89?source=post_internal_links---------
2----------------------------)

[[![Nelly](https://miro.medium.com/fit/c/40/40/1*vieC6TKbz9nCXVcWYWVDSA.png)](https://medium.com/@discordnelly?source=post_internal_links
---------3----------------------------)

[Nelly

](https://medium.com/@discordnelly?source=post_internal_links---------
3----------------------------)

in

[Discord Blog

](https://medium.com/discord-engineering?source=post_internal_links---------
3----------------------------)

## Discord Transparency Report: Jan 1 — April 1

![](https://miro.medium.com/focal/112/112/50/50/1*PjyKrghcrRehW3Q4w8jFYg.png)](https://medium.com/discord-
engineering/discord-transparency-report-
jan-1-april-1-4f288bf952c9?source=post_internal_links---------
3----------------------------)

[[![Paper](https://miro.medium.com/fit/c/40/40/2*XxHOd6nEmhhEcfT3lzdREg.jpeg)](https://medium.com/@paper_?source=post_internal_links
---------4----------------------------)

[Paper

](https://medium.com/@paper_?source=post_internal_links---------
4----------------------------)

## Data Protection and Privacy: European and US Perspectives — Balancing the
rights of privacy and…

](https://medium.com/@paper_/data-protection-and-privacy-european-and-us-
perspectives-balancing-the-rights-of-privacy-
and-4470def6fa19?source=post_internal_links---------
4----------------------------)

[[![Nathan
Kinch](https://miro.medium.com/fit/c/40/40/1*bIDwLshAnUEz_FJCjdffSg.png)](https://nathankinch.medium.com/?source=post_internal_links
---------5----------------------------)

[Nathan Kinch

](https://nathankinch.medium.com/?source=post_internal_links---------
5----------------------------)

in

[Greater Than Experience Design

](https://medium.com/greater-than-experience-design?source=post_internal_links
---------5----------------------------)

## Data sharing and trust: What’s the relationship?

![](https://miro.medium.com/focal/112/112/50/50/0*kULjFrEjDK3UPjKy)](https://medium.com/greater-
than-experience-design/data-sharing-and-trust-whats-the-
relationship-a7c494c9c163?source=post_internal_links---------
5----------------------------)

[[![Amaya
Alviz](https://miro.medium.com/fit/c/40/40/0*06SHbextH1_g2bU-)](https://medium.com/@amaya.alviz?source=post_internal_links
---------6----------------------------)

[Amaya Alviz

](https://medium.com/@amaya.alviz?source=post_internal_links---------
6----------------------------)

## How is cybersecurity affecting the music industry?

![](https://miro.medium.com/focal/112/112/50/50/1*v-KQU7-TGOs9UQuRleVNFA.jpeg)](https://medium.com/@amaya.alviz/how-
is-cybersecurity-affecting-the-music-
industry-53caba2811eb?source=post_internal_links---------
6----------------------------)

[[![amrkt tike8](https://miro.medium.com/fit/c/40/40/0*uEVYCWus-
OGDyK-8.jpg)](https://medium.com/@amrkttike5?source=post_internal_links
---------7----------------------------)

[amrkt tike8

](https://medium.com/@amrkttike5?source=post_internal_links---------
7----------------------------)

## CYB 100 CYB100 All Discussions

](https://medium.com/@amrkttike5/cyb-100-cyb100-all-discussions-
ef55b08a1767?source=post_internal_links---------7----------------------------)

[](https://medium.com/?source=post_page-----
4c5f77bfddfa--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
4c5f77bfddfa--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
4c5f77bfddfa--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
4c5f77bfddfa--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
4c5f77bfddfa--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----4c5f77bfddfa--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----4c5f77bfddfa--------------------------------)

[Get
started](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fsafetrace-
april-2020-development-update-4c5f77bfddfa&source=post_page
--------------------------nav_reg-----------)

[![Enigma
Project](https://miro.medium.com/fit/c/176/176/2*2SRmuGkTHWle_KyV3jfGhQ.png)](https://medium.com/@EnigmaMPC)

[

## Enigma Project

](https://medium.com/@EnigmaMPC)

6.5K Followers

Enigma is securing the decentralized web. We solve for privacy with “secret”
smart contracts, allowing dApps and blockchains to use private/sensitive data.

[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F4f5f09fa22fb&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fsafetrace-
april-2020-development-
update-4c5f77bfddfa&user=Enigma+Project&userId=4f5f09fa22fb&source=post_page-4f5f09fa22fb
-------------------------follow_profile-----------)

[](https://medium.com/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2Ffcc87216ce8e&operation=register&redirect=https%3A%2F%2Fblog.enigma.co%2Fsafetrace-
april-2020-development-
update-4c5f77bfddfa&newsletterV3=4f5f09fa22fb&newsletterV3Id=fcc87216ce8e&user=Enigma+Project&userId=4f5f09fa22fb&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Nicholas
Bolton](https://miro.medium.com/fit/c/40/40/1*6ZIlzIOpgmadO2tCykvTVQ.jpeg)](https://medium.com/@nicholas.bolton?source=read_next_recirc
---------0---------------------4287e95e_b065_4bed_99c3_775da8f7d3d9-------)

[Nicholas Bolton

](https://medium.com/@nicholas.bolton?source=read_next_recirc---------0
---------------------4287e95e_b065_4bed_99c3_775da8f7d3d9-------)

in

[Wing Builders

](https://medium.com/hangar-worldwide?source=read_next_recirc---------0
---------------------4287e95e_b065_4bed_99c3_775da8f7d3d9-------)

## Hilda Briceno. The “Techie Girl.”

![](https://miro.medium.com/focal/112/112/50/50/1*eG8KNldq3kBfjHP2lfGdDA.jpeg)](https://medium.com/hangar-
worldwide/hilda-briceno-the-techie-girl-478abe015a90?source=read_next_recirc
---------0---------------------4287e95e_b065_4bed_99c3_775da8f7d3d9-------)

[[![ORDANO.IO](https://miro.medium.com/fit/c/40/40/1*t5ybJ6PIGeTI_pjEE05Vwg.png)](https://medium.com/@Ordano.io?source=read_next_recirc
---------1---------------------4287e95e_b065_4bed_99c3_775da8f7d3d9-------)

[ORDANO.IO

](https://medium.com/@Ordano.io?source=read_next_recirc---------1
---------------------4287e95e_b065_4bed_99c3_775da8f7d3d9-------)

## About ORDANO.IO

![](https://miro.medium.com/focal/112/112/50/50/1*10xOYVQH0w_BhyDtG-
ovHg.png)](https://medium.com/@Ordano.io/about-ordano-
io-1139b1a7eefc?source=read_next_recirc---------1---------------------
4287e95e_b065_4bed_99c3_775da8f7d3d9-------)

[[![Judithosarumen](https://miro.medium.com/fit/c/40/40/0*SnZDGtQ6UUM-
fcaz)](https://medium.com/@judithebengho?source=read_next_recirc---------2
---------------------4287e95e_b065_4bed_99c3_775da8f7d3d9-------)

[Judithosarumen

](https://medium.com/@judithebengho?source=read_next_recirc---------2
---------------------4287e95e_b065_4bed_99c3_775da8f7d3d9-------)

## The In and Out of a Year Planner

](https://medium.com/@judithebengho/the-in-and-out-of-a-year-
planner-b55f9e490b65?source=read_next_recirc---------2---------------------
4287e95e_b065_4bed_99c3_775da8f7d3d9-------)

[[![Eric
Nahm](https://miro.medium.com/fit/c/40/40/0*QFnVfLKetA6zIfi9)](https://medium.com/@ericnahm?source=read_next_recirc
---------3---------------------4287e95e_b065_4bed_99c3_775da8f7d3d9-------)

[Eric Nahm

](https://medium.com/@ericnahm?source=read_next_recirc---------3
---------------------4287e95e_b065_4bed_99c3_775da8f7d3d9-------)

## Random NFT Thoughts

](https://medium.com/@ericnahm/random-nft-
thoughts-6b7377fd343d?source=read_next_recirc---------3---------------------
4287e95e_b065_4bed_99c3_775da8f7d3d9-------)

[Help

](https://help.medium.com/hc/en-us)

[Status

](https://medium.statuspage.io)

[Writers

](https://about.medium.com/creators/)

[Blog

](https://blog.medium.com)

[Careers

](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e)

[Privacy

](https://policy.medium.com/medium-privacy-policy-f03bf92035c9)

[Terms

](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f)

[About

](https://medium.com/about?autoplay=1)

[Knowable

](https://knowable.fyi)

