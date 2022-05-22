[](/)

[Get unlimited access](/plans?source=upgrade_membership---
nav_full----------------------------------)

[Open in
app](https://rsci.app.link/?$canonical_url=https%3A%2F%2Fmedium.com/p/c2c78fce5638&~feature=LoOpenInAppButton&~channel=ShowPostUnderCollection&~stage=mobileNavBar)

[](/)

[Home](/)

[Notifications](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fnotifications&source=--------------------------notifications_sidenav-----------)[Lists](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Flists&source=--------------------------lists_sidenav-----------)[Stories](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fme%2Fstories%2Fdrafts&source=--------------------------stories_sidenav-----------)

* * *

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-
story&source=--------------------------new_post_sidenav-----------)

[![safenetwork](https://miro.medium.com/fit/c/64/64/1*oEy3kCG2HULiXdpEQdr6Nw.jpeg)](https://medium.com/safenetwork?source=post_page
-----c2c78fce5638--------------------------------)

Published in

[safenetwork

](https://medium.com/safenetwork?source=post_page-----
c2c78fce5638--------------------------------)

[![MaidSafe](https://miro.medium.com/fit/c/96/96/1*_aSR7-KPlJ-
loTqzHF1E1g.jpeg)](/@maidsafe?source=post_page-----
c2c78fce5638--------------------------------)

[MaidSafe](/@maidsafe?source=post_page-----
c2c78fce5638--------------------------------)

Follow

Sep 5, 2019

·

5 min read

#  **An Overview of Data Types on the SAFE Network**

![](https://miro.medium.com/max/1400/1*ojpVjYmO9f-rJUfBRNWxxg.png)

 _Photo by fabio on Unsplash_

One of the [SAFE Network Fundamentals](/safenetwork/founding-fundamentals-
part-1-4b2d096e1a1b) is that we must store data in
[perpetuity](/safenetwork/a-spotlight-on-the-perpetual-web-9850349fab0b). This
is a key part of creating a web that prevents the alteration, manipulation or
deletion of public data. Why? Because it means that it will then be impossible
to rewrite history.

But instead of taking a broad-brush approach and _only_ letting data be stored
in perpetuity, we’ve looked at different use cases and thought about
circumstances in which data needs to be stored differently. We have 8
different data types. Sounds overcomplicated? Don’t worry, it isn’t.

Let’s start breaking this down.

#  **Unpublished/Published**

First up, at a very basic level, data will either be private ( _unpublished_ )
or public ( _published_ ). Private data is information you want to keep
private on the Network or, perhaps, share on a very restricted basis. Private
data _can_ be deleted.

Public data is information that is published to the Network. Everyone can see
it. We call this [_The Perpetual Web_](/safenetwork/a-spotlight-on-the-
perpetual-web-9850349fab0b) and it _can’t_ be removed from the Network.
HOWEVER, there are various types of public data which show previous versions
(with different data types utilising a combination of edits and amends). Just
like the [Internet Archive](https://archive.org/) today stores versions of
websites even if they were published with mistakes, the whole life of websites
(which is by definition, public data) will be available to view to all.

The main thing to remember: anything that is **public is perpetual**. That is,
it can never be deleted.

So we have two categories, published and unpublished. But we’ve broken this
down even further and we’ll explore each data type below. As you will see,
some are exclusive to either public or private and some data types can have
either property.

#  **AppendOnly**

This data type can be either public or private. You can make changes or edits
to the data and it’ll result in a new version - but you _can’t_ change or edit
the existing one. Hence the name AppendOnly as you can _append_ the new
versions.

So if you published a research paper for the public as AppendOnly data, the
content of that paper could never be changed. BUT you _could_ create/upload a
new version that corrects or adds more information to the original paper. If
you wanted the ability to delete this additional information, you would have
to upload this as private data. This is a very important point to make. The
Perpetual Web ([Fundamental
8](https://safenetwork.tech/fundamentals/#edvoqj3uedt)) means data should live
in perpetuity…but, circumstances may require you to store _private_ data so
that you have the option of deleting it.

#  **ImmutableData**

Next up is ImmutableData. Again, this can be either Published or Unpublished
data — but ImmutableData cannot be changed in any way (hence the name
immutable). This would be perfect for storing files on the Network such as
public scientific reports where it is vital from a societal perspective that
these can not be changed or manipulated (public) or for storing private files
which can be deleted by the user if he or so chooses (private).

#  **MutableData**

Then we have Mutable. MutableData _can_ be altered, changed and manipulated.
So it has to be in the unpublished category (since published data by
definition cannot). It cannot be published on the Network. Perhaps you are a
researcher who needs to adapt your argument during the course of your
research. You need the ability to make alterations to your work. As this is
private data, it can only ever be viewed by you and anyone you give permission
to. You are also the only one who has the ability to make those changes.

#  **Sequenced/Unsequenced**

Not a data type _per se_ , but we also have Sequenced and Unsequenced data.
This lets data be versioned, or ordered. This design is pertinent in
understanding things like how online articles have been edited or corrected
over time. This applies to all the data _except_ for ImmutableData.

One more thing to note: within the unpublished data types, there is the
ability to store unpublished data on the network and share it with a selected
group of users. The user should be able to give permissions like read, write,
append based on the use case.

#  **So what does this look like?**

To help make sense of this, we’ve plotted the different data types in the
diagram with a brief description for each given below.

![](https://miro.medium.com/max/1400/1*sEZ3-8FZYxLMHqJOf73xWQ.png)

SequencedPublishedAppendOnlyData

  1.  **SequencedPublishedAppendOnlyData** : This is a data type that is ordered, public and only appends may be made — no edits and this data type cannot be deleted.
  2.  **UnsequencedPublishedAppendOnlyData** : This is a data type is public (therefore cannot be deleted) and no edits can be made.
  3.  **SequencedUnpublishedAppendOnlyData** : This is a data type that is versioned, private and no edits can be made.
  4.  **UnsequencedUnpublishedAppendOnlyData** : This is a data type that is not versioned, private and appends can be made.
  5.  **PublishedImmutableData** : This data is public and unable to be edited or altered or deleted.
  6.  **UnpublishedImmutableData** : All you can do with this data set is basically upload, read and delete.
  7.  **UnpublishedSequencedMutableData** : This is ordered data that is private and can be changed as much as the owner wants.
  8.  **UnpublishedUnsequencedMutableData** : This is the same as above, but not ordered.

#  **And what does that mean for a developer?**

All these data types are all well and good but what does this _actually mean_?
What does it enable a developer to do?

Let’s try some examples.

Say you wanted to create a music sharing or streaming application. You would
need it to be public so people could see it, so it would fall into the
Published bracket.

However, if you wanted a Snapchat-esque application in order to share messages
with a private group of friends, you could choose UnpublishedAppendableData
(so content can be deleted, just like SnapChat) or maybe MutableData.

So these are examples of one data type, the likelihood is the developer will
need to use a combination of data types. Staying on a similar theme, imagine
rebuilding Medium. You need somewhere to draft the post — so let’s use
MutableData to cover the various changes you’d make in the editing process.
You’d then need somewhere you can post the final content for the public: how
about PublishedImmutableData? And finally, you want a place where readers can
leave comments (so we’d suggest PublishedAppendableData).

Permissions play a big role here. So how can you create a forum with
PublishedAppend that others can add things onto it, or how is that with
UnpublishedAppendOnly my family can edit a doc even if it’s unpublished? This
all relies on the permissions and ownership of the data. We won’t go into too
much detail here, but for those of you who are interested in how this works,
we recommend you check this post out which details out one of our key Front
End milestones ([ _Take Control of Your Data_](/safenetwork/a-spotlight-on-
take-control-of-your-data-34d0a8e8ac64)).

These might be oversimplified examples, but generally any combination of the 8
data sets can be built — all you need is a good idea.

There we have it: one SAFE Network, eight data types. The entirely autonomous
network, which requires no human intervention where all published data on the
Network will be immutable and available on the Network in perpetuity.

\--

1

\--

\--

1

## [More from safenetwork](/safenetwork?source=post_page-----
c2c78fce5638--------------------------------)

Stories from around the SAFE Network

[Read more from safenetwork](/safenetwork?source=post_page-----
c2c78fce5638--------------------------------)

## Recommended from Medium

[[![Gayana K
N](https://miro.medium.com/fit/c/40/40/0*bHN_PpNGh4FVllER)](/@kngayana?source=post_internal_links
---------0----------------------------)

[Gayana K N

](/@kngayana?source=post_internal_links---------0----------------------------)

## APPLICATION OF PYTHON IN COVID SPREAD ANALYSIS

](/@kngayana/application-of-python-in-covid-spread-
analysis-b7fc7f113c08?source=post_internal_links---------
0----------------------------)

[[![Prithivi
Da](https://miro.medium.com/fit/c/40/40/1*15OXqrdeOS20LXou06_zdg@2x.jpeg)](/@prithivi?source=post_internal_links
---------1----------------------------)

[Prithivi Da

](/@prithivi?source=post_internal_links---------1----------------------------)

## How to tackle copy-paste text plagiarism efficiently at scale?

![](https://miro.medium.com/focal/112/112/50/50/1*PgBoYAhOFPcxLhWQfbIG6w.png)](/@prithivi/how-
to-tackle-copy-paste-text-plagiarism-efficiently-at-
scale-f63f47c48e23?source=post_internal_links---------
1----------------------------)

[[![Blogdolago](https://miro.medium.com/fit/c/40/40/0*4Z86_k0R1BzXxZ5X)](/@pequenosegrandes.blogdolago?source=post_internal_links
---------2----------------------------)

[Blogdolago

](/@pequenosegrandes.blogdolago?source=post_internal_links---------
2----------------------------)

## Datas comemorativas de hoje: 04 de Dezembro de 2021

![Datas comemorativas de hoje: 04 de Dezembro de
2021](https://miro.medium.com/focal/112/112/50/50/0*8Y-i4VFc8tBvI_Et.jpg)](/@pequenosegrandes.blogdolago/datas-
comemorativas-de-hoje-04-de-dezembro-
de-2021-178a97a50efd?source=post_internal_links---------
2----------------------------)

[[![Grecy
Jonson](https://miro.medium.com/fit/c/40/40/1*dmbNkD5D-u45r44go_cf0g.png)](/@grecyjonson09?source=post_internal_links
---------3----------------------------)

[Grecy Jonson

](/@grecyjonson09?source=post_internal_links---------
3----------------------------)

## Understanding the Five 3-D Visualization Elements In MATLAB

![](https://miro.medium.com/focal/112/112/50/50/1*R79PshhGCPqxrDC4MJ0EbQ.png)](/@grecyjonson09/understanding-
the-five-3-d-visualization-elements-in-
matlab-83b6121b7a3a?source=post_internal_links---------
3----------------------------)

[[![Reallemon](https://miro.medium.com/fit/c/40/40/1*rdMBfYc8z43vKo82lk4RSQ.png)](/@reallemon?source=post_internal_links
---------4----------------------------)

[Reallemon

](/@reallemon?source=post_internal_links---------
4----------------------------)

## Using Intensity to Measure A Character’s Strength

](/@reallemon/using-intensity-to-measure-a-characters-strength-
cec7f7f1b23e?source=post_internal_links---------4----------------------------)

[[![Millennial
Talks](https://miro.medium.com/fit/c/40/40/1*to9VxTet9TMc7quTiL_R-Q.jpeg)](/@millennial-
talks?source=post_internal_links---------5----------------------------)

[Millennial Talks

](/@millennial-talks?source=post_internal_links---------
5----------------------------)

## Gearing up with predictive modelling

![](https://miro.medium.com/focal/112/112/50/50/1*DfbS1rak1FCvOg0z1JsCgQ.jpeg)](/@millennial-
talks/gearing-up-with-predictive-
modelling-4b34758eb911?source=post_internal_links---------
5----------------------------)

[[![Angel
Das](https://miro.medium.com/fit/c/40/40/1*_z8D8aKbgePjyfBE5-bXnw.jpeg)](/@angeleastbengal?source=post_internal_links
---------6----------------------------)

[Angel Das

](/@angeleastbengal?source=post_internal_links---------
6----------------------------)

in

[Towards Data Science

](https://medium.com/towards-data-science?source=post_internal_links---------
6----------------------------)

## Hierarchical Clustering in Python using Dendrogram and Cophenetic
Correlation

![](https://miro.medium.com/focal/112/112/50/50/0*0hiNNFl-BCTfv7BC)](/towards-
data-science/hierarchical-clustering-in-python-using-dendrogram-and-
cophenetic-correlation-8d41a08f7eab?source=post_internal_links---------
6----------------------------)

[[![Nicola
Askham](https://miro.medium.com/fit/c/40/40/0*KU5khJIv5lR6CC9h)](/@nicola-76063?source=post_internal_links
---------7----------------------------)

[Nicola Askham

](/@nicola-76063?source=post_internal_links---------
7----------------------------)

## The Data Governance Clinic and how it could help you!

![](https://miro.medium.com/focal/112/112/50/50/1*49QxghvI_Q-7YR11fToEXA.jpeg)](/@nicola-76063/the-
data-governance-clinic-and-how-it-could-help-you-
cc2d0ceaf315?source=post_internal_links---------7----------------------------)

[](/?source=post_page-----c2c78fce5638--------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----
c2c78fce5638--------------------------------)[Help](https://help.medium.com/hc/en-
us?source=post_page-----
c2c78fce5638--------------------------------)[Terms](https://policy.medium.com/medium-
terms-of-service-9db0094a1e0f?source=post_page-----
c2c78fce5638--------------------------------)[Privacy](https://policy.medium.com/medium-
privacy-policy-f03bf92035c9?source=post_page-----
c2c78fce5638--------------------------------)

* * *

## Get the Medium app

[![A button that says 'Download on the App Store', and if clicked it will lead
you to the iOS App
store](https://miro.medium.com/max/270/1*Crl55Tm6yDNMoucPo1tvDg.png)](https://itunes.apple.com/app/medium-
everyones-stories/id828256236?pt=698524&mt=8&ct=post_page&source=post_page
-----c2c78fce5638--------------------------------)

[![A button that says 'Get it on, Google Play', and if clicked it will lead
you to the Google Play
store](https://miro.medium.com/max/270/1*W_RAPQ62h0em559zluJLdQ.png)](https://play.google.com/store/apps/details?id=com.medium.reader&source=post_page
-----c2c78fce5638--------------------------------)

[Get
started](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fsafenetwork%2Fan-
overview-of-data-types-on-the-safe-network-c2c78fce5638&source=post_page
--------------------------nav_reg-----------)

[![MaidSafe](https://miro.medium.com/fit/c/176/176/1*_aSR7-KPlJ-
loTqzHF1E1g.jpeg)](/@maidsafe)

[

## MaidSafe

](/@maidsafe)

1.1K Followers

Building the SAFE Network. The world’s first autonomous data network. Privacy,
security, freedom. Join us at <https://safenetforum.org/>

Follow

[](/m/signin?actionUrl=%2F_%2Fapi%2Fsubscriptions%2Fnewsletters%2F2fe910544d0b&operation=register&redirect=https%3A%2F%2Fmedium.com%2Fsafenetwork%2Fan-
overview-of-data-types-on-the-safe-
network-c2c78fce5638&newsletterV3=6876251327a7&newsletterV3Id=2fe910544d0b&user=MaidSafe&userId=6876251327a7&source=--------------------------subscribe_user-----------)

## More from Medium

[[![Giancarlo
Mori](https://miro.medium.com/fit/c/40/40/0*yflVkFC_4MTu0obW.jpg)](/@gcmori?source=read_next_recirc
---------0---------------------f43119b6_2521_451f_9a84_aec8886602ce-------)

[Giancarlo Mori

](/@gcmori?source=read_next_recirc---------0---------------------
f43119b6_2521_451f_9a84_aec8886602ce-------)

## Modern Information Wars

![](https://miro.medium.com/focal/112/112/50/50/1*wI7-rKAgR7dhoOEI71KEPg.jpeg)](/@gcmori/modern-
information-wars-ffb38a9b0bb2?source=read_next_recirc---------0
---------------------f43119b6_2521_451f_9a84_aec8886602ce-------)

[[![Brayleen
Blanchard](https://miro.medium.com/fit/c/40/40/0*X8vMyBlEAm9-ImnQ)](/@bblanchard19?source=read_next_recirc
---------1---------------------f43119b6_2521_451f_9a84_aec8886602ce-------)

[Brayleen Blanchard

](/@bblanchard19?source=read_next_recirc---------1---------------------
f43119b6_2521_451f_9a84_aec8886602ce-------)

## Big Data: Privacy

](/@bblanchard19/big-data-privacy-613c6fab60ca?source=read_next_recirc
---------1---------------------f43119b6_2521_451f_9a84_aec8886602ce-------)

[[![apotheca](https://miro.medium.com/fit/c/40/40/1*1e5erbzZtXPNTmzx8NLtQA.png)](/@apotheca?source=read_next_recirc
---------2---------------------f43119b6_2521_451f_9a84_aec8886602ce-------)

[apotheca

](/@apotheca?source=read_next_recirc---------2---------------------
f43119b6_2521_451f_9a84_aec8886602ce-------)

## Health 3.0: Populating a Snomed CT Property Graph with Synthetic Patient
Data

![](https://miro.medium.com/focal/112/112/50/50/0*dDZ4oWuIaF7rjAeA.png)](/@apotheca/health-3-0-populating-
a-snomed-ct-property-graph-with-synthetic-patient-
data-e6145a5d30d8?source=read_next_recirc---------2---------------------
f43119b6_2521_451f_9a84_aec8886602ce-------)

[[![Bhavin
Gandecha](https://miro.medium.com/fit/c/40/40/1*YLq67w564MaY_rP1w81TmQ@2x.jpeg)](/@bhavingandecha?source=read_next_recirc
---------3---------------------f43119b6_2521_451f_9a84_aec8886602ce-------)

[Bhavin Gandecha

](/@bhavingandecha?source=read_next_recirc---------3---------------------
f43119b6_2521_451f_9a84_aec8886602ce-------)

## The Vision (Capability) Of The Cloud

![](https://miro.medium.com/focal/112/112/50/50/1*phfC9Gc3_hNFejLW6VhNHA.png)](/@bhavingandecha/the-
vision-capability-of-the-cloud-251af9a64522?source=read_next_recirc---------3
---------------------f43119b6_2521_451f_9a84_aec8886602ce-------)

[Help

](https://help.medium.com/hc/en-us)

[Status

](https://medium.statuspage.io)

[Writers

](https://about.medium.com/creators/)

[Blog

](https://blog.medium.com)

[Careers

](/jobs-at-medium/work-at-medium-959d1a85284e)

[Privacy

](https://policy.medium.com/medium-privacy-policy-f03bf92035c9)

[Terms

](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f)

[About

](https://medium.com/about?autoplay=1)

[Knowable

](https://knowable.fyi)

