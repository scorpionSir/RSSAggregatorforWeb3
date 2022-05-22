  * [Home](/)
  * [Contact](/contact)
  * [Services](/services)
  * [Projects](/projects)
  * [Community](/community)
  * [Blog](/blog)

Menu

#  [![ScopeLift](//images.squarespace-
cdn.com/content/v1/54b81e72e4b0fee4b01a42e9/1581018368646-GMT0JDHOVLSGDECYFQVQ/SCOPELIFT-
long-cropped.png?format=1500w)](/)

Street Address

Philadelphia, PA

Phone Number

Your Custom Text Here

# [![ScopeLift](//images.squarespace-
cdn.com/content/v1/54b81e72e4b0fee4b01a42e9/1581018368646-GMT0JDHOVLSGDECYFQVQ/SCOPELIFT-
long-cropped.png?format=1500w)](/)

  * [Home](/)
  * [Contact](/contact)
  * [Services](/services)
  * [Projects](/projects)
  * [Community](/community)
  * [Blog](/blog)

#  [The Developer Hiring Process is (Literally) Over Engineered](/blog/hiring-
is-over-engineered)

October 17, 2016 [Ben DiFrancesco](/blog?author=54b81e71e4b06e38ad58f2f2)

Widely used techniques for hiring, motivating, and measuring developers aren’t
just ineffective- they’re very likely counterproductive to building a healthy
team. To hire better developers, we need to stop fixating on technical skills
in isolation from other factors. I’ve come this conclusion over the course of
my career, but if you’ll bear with me, I have a particular anecdote from my
first job out of school that helps explain why.

##  **A Million Dollar Meeting**

My group at Boeing maintained product data management software: imagine it as
GitHub for collaborating on 3D aircraft designs. It was critical for the
workflows of hundreds of engineers (the kind who work with atoms, not bits). I
worked on a small subteam that focused on data visualization. Our software
extracted heavyweight design data and rendered it in lightweight formats. You
could view an entire aircraft, twirl it around in 3D space, then zoom in on a
single bolt all with reasonable performance. Engineers used these for frequent
“design review” meetings, which were something like a daily standup.

All of this was in place when I started there, but there was a problem:
renderings were often wrong. Engineers reported parts were out of place,
overlapping, or floating off in space. This wasn’t because the people I worked
with weren’t capable programmers. On the contrary, they were very smart and
far better programmers than I was as a fresh college grad. This was just a
**really**  challenging technical problem. Each aircraft was was organized in
a huge tree structure, with millions of nodes and thousands of levels, and was
being updated throughout the day. If we rendered the entire assembly from the
top down, we could be sure everything was positioned correctly. But doing so
took 12+ hours per aircraft.

One developer had written impressive algorithms to detect what parts needed to
be re-rendered when something changed. This allowed us to keep the renderings
up to date while doing the minimal processing work needed. It worked amazingly
well given the complexity of the problem, but there were too many edge cases.
Every week, our manager would hear from some engineering group that had been
unable to complete their design review. Dozens of engineers, who had all
stopped their work for the meeting, would have to go back to their desks
having not completed the task. Each time, we would try to figure out where the
system had fallen down, then code around that case.

I was woefully unprepared to contribute in a technical way to this issue at
this point in my career. I was also new and naive enough to lack “proper”
respect for the company’s hulking bureaucracy. Without asking anyone’s
permission, I talked about the issue to another employee whom I’d gotten to
know. He worked in the group that helped train and support the engineers on
software tools. I asked some questions and he took them to various engineering
groups to do some poking around. This started a dialog that eventually
resulted in a startling conclusion: the engineers didn’t need the renderings
to be updated in realtime. Renders which included changes completed the
previous day were sufficient.

We threw out a pile of technically-impressive but hard to maintain code. It
was replaced by a few nightly cron jobs running programs that were basically
one liners: `rootNode.render(path)`! The engineers were happy and my manager
stopped hearing complaints. He couldn’t have cared less how technically
unimpressive the solution was.

I don’t think it’s an exaggeration to say that this issue was costing Boeing
seven figures a year in salary time. That’s without considering the
opportunity costs or the effects of increased tension between the groups. If
I’d never done another piece of work at Boeing for the nearly three years I
was there, they would still have gotten a good return for my salary. _Yet
there is literally no existing metric for measuring programmer productivity
that would have incentivized or recognized this contribution._

##  **In the Weeds**

Our industry fetishizes developers who “love digging into challenging
technical problems.” I’m one of those developers. Luckily, stumbling into this
and other experiences in my career have taught me an important lesson.

 _ **If we want to increase our value as software engineers to employers or
clients, the single biggest lever available to us is almost never purely
technical. Rather, it’s taking our technical knowledge and putting it in the
context of the business problems we are being asked to solve.**_

This isn’t management’s responsibility. It’s ours. The business will
inevitably come to us with implementation details. It's our job to elevate the
discussion back to the level of actual goals. We must be comfortable
conversing at that level and able to determine the real organizational needs.
Then, and only then, is our task to find the simplest technical solution to
meet those needs.

So what does all this have to do with hiring? Simply put, you want to be
finding candidates who are willing and able to do this. You don’t want a
software engineer who blindly does what she’s told, nor one who just dives
head first into technical challenges because she loves them. You want one who
distills those technical challenges into actual business tradeoffs and
communicates these with empathy and patience to her colleagues who aren’t
developers.

Testing for this isn’t easy, but having candidates whiteboard algorithms, for
example, doesn’t even come close. In fact, these and other common practices
are probably filtering out exactly the kind of engineers we want. Those left
are likely: 1) too eager to jump into a complex technical solution when a
simple business fix exists, or 2) so conformist that they’ll do what they’re
told even if they suspect it’s not best for the organization. We think we're
weeding out weak candidates. We're actually pulling out the best seedlings.

On second thought, maybe **asking**  a candidate to whiteboard algorithms
isn’t a bad idea after all. If she politely protests, and provides a
thoughtful explanation as to why it’s not a useful exercise, hire her on the
spot.

* * *

**Important footnote** : I was inspired to finally write this blog post by two
events. The first was seeing Janie Clayton (aka
[@RedQueenCoder](https://twitter.com/RedQueenCoder)) tweeting and podcasting
about her experience interviewing for iOS positions. I was disappointed, if
unsurprised, by some of the responses she received. The second was the
penultimate [CocoaLove](https://cocoalove.org/) conference, which I attended
this past weekend. There were several great talks about motivating and
measuring teams of developers, especially those by[ Lydia
Martin](http://www.lydiafmartin.com/) and [David
Starke](https://twitter.com/dstarke), which sparked some great conversations
with other attendees. Much of what I’ve written here crystallized during those
tweets, talks, and conversations. Thanks to those folks!

[<- 360|iDev 2017: Swifty By Default](/blog/360idev-2017-swifty-by-
default)[Life After Git: Spitballing the Next Generation of Source Control
->](/blog/life-after-git)

[ ](https://twitter.com/BenDiFrancesco)[ ](https://github.com/apbendi)[
](https://www.linkedin.com/pub/ben-difrancesco/9b/426/680)

[ ](https://twitter.com/BenDiFrancesco) [ ](https://github.com/apbendi) [
](https://www.linkedin.com/pub/ben-difrancesco/9b/426/680)

© ScopeLift 2021

