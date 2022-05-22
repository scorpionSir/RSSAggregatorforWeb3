#  [ Unenumerated ](https://unenumerated.blogspot.com/)

An unending variety of topics

## Thursday, October 18, 2012

###  Dead reckoning and the exploration explosion

Navigation is the art or science of combining information and reducing error
to _keep oneself on, or return oneself to, a route_ that will get you where
you want to go. Note what I did _not_ say here. Navigation is _not
necessarily_ the art or science of _locating where you are._ While answering
the latter question - i.e. locating oneself in a Euclidean space, or a space
reasonably projectable onto a Euclidean space - can usefully solve the
navigation problem, figuring out such a location often requires different, and
often more, information than you need to answer the questions of how to stay
on or return to your desired route. And indeed this is what dead reckoning
does - it gets you where you want to go with different information than what
you would need to draw or find yourself on a normal map. I hope to explain
more about this important incompatibility between the pilots' and
cosmographers' systems during most of the age of exploration in a future post,
but for now I will give an overview of the historical development of dead
reckoning.  
  
Between Italy of the late 13th century and the advent of GPS, dead reckoning
formed the basis of most modern navigation. Dead reckoning was in particular
the primary method of navigation used during the exploration explosion of the
late 15th and early 16th centuries - the startlingly unprecedented voyages
across unknown oceans of Dias, da Gama, Columbus, Magellan, and so on.  
  
Dead reckoning is based on a sequence of vectors. Each vector consists of two
essential pieces of information: direction and distance. Distance is typically
calculated from time and speed, so each vector typically consists of the tuple
{direction, time, speed}. With only speed and time, we have only a scalar
distance value - it could be in any direction. With time but not speed, or
speed but not time, we don't have enough information to determine the distance
covered.  
  
From the start of a voyage to the last docking at the home port, dead
reckoning was a strict regimen that never stopped: day and night, in calm and
in storm, its measurement, recording, and diagramming protocols were
rigorously followed.  
  
Measuring or estimating the speed of a ship was a craft mystery the nature of
which is still debated today, so I'll skip over that and focus on the two more
straightforward innovations in measurement, both of which occurred in or
reached Italy and were first combined there in the 13th century: in measuring
direction and in measuring time.  
  
For measuring time mariners used the _sand glass,_ invented in Western Europe
during that same century. I have discussed this invention
[here](http://szabo.best.vwh.net/synch.html). A strict regimen of turning the
glasses was kept non-stop throughout a voyage.  
  
For measuring direction, the ships of the exploration explosion typically had
at least two _magnetic compasses_ , usually built into the ship to maintain a
fixed orientation with the ship. Typically one compass was used by the
helmsman, in charge of steering the ship, and the other by the pilot, in
charge of ordering both the sail rigging and the general direction for the
helmsman to keep.  
  
The magnetic compass was probably first invented in China, used first for
_feng shui_ and then for navigation by the early 12th century. Somehow,
without any recorded intermediaries, it appears in the writings of authors in
the region of the English Channel in the late 12th century where it was quite
likely being used for navigation in that often cloudy region. Its first use in
Italy was associated with the then-thriving port city of Amalfi. As both
Amalfi and the English Channel were at the time controlled by the Normans,
this suggests to me either a Norman innovation, or arrival via Norse trade
connections to the Orient via Russia combined with now unknown Chinese trade
routes. This is conjectural. Neither the Norse sagas nor writings about the
Normans during earlier periods mention a magnetic compass, nor do Arab sources
mention it until the late 13th century in the Mediterranean. In any case, it
is the Italians who made the magnetic compass part of a rigorous system of
dead reckoning.  
  
[![](//1.bp.blogspot.com/-WxE-VGeJQ6w/UH_CidNj2rI/AAAAAAAAAOU/picdBtS-
aAU/s1600/CompassMentions12thAndEarly13thCenturies_NormanHoldings1130.jpg)](//1.bp.blogspot.com/-WxE-
VGeJQ6w/UH_CidNj2rI/AAAAAAAAAOU/picdBtS-
aAU/s1600/CompassMentions12thAndEarly13thCenturies_NormanHoldings1130.jpg)  
---  
  
_Green dots indicate, in the case of northern Europe, the location of authors
who mention use of the magnetic compass for navigation in the late 12th and
13th centuries, and for Italy, the traditional Italian association of the
invention of the compass with Amalfi in the 13th century. Red indicates areas
controlled by the Normans._  
  
  
  
A dead reckoning itinerary can be specified as a sequence of tuples {
direction, speed, time }. It can be drawn as a diagram of vectors laid down
head-to-tail. However, as mentioned above, this diagram by itself, for
nontrivial sea and ocean voyages, contains insufficient information to map the
arrows accurately onto a Ptolemaic map (i.e. maps as we commonly understand
them, based on celestial latitudes and longitudes), yet sufficient at least in
theory to guide a pilot following such directions to their destination.  
  

[![](//1.bp.blogspot.com/-hwrQNZ2Op-k/UH-8zNlbYDI/AAAAAAAAANw/UxKWGHP4Sz0/s320/DeadReckoningBasic.png)](//1.bp.blogspot.com/-hwrQNZ2Op-k/UH-8zNlbYDI/AAAAAAAAANw/UxKWGHP4Sz0/s1600/DeadReckoningBasic.png)

For recording speed and direction for each sand glass time interval (e.g. half
hour), pilots used some variation of the _traverse board_ , in which these
values were specified by the locations of pegs in the board.  
  
[![](//4.bp.blogspot.com/-SvsapDVgOyU/UH-90y5bmtI/AAAAAAAAAOA/8c1givzy8a8/s1600/Traverse_Board.jpg)](//4.bp.blogspot.com/-SvsapDVgOyU/UH-90y5bmtI/AAAAAAAAAOA/8c1givzy8a8/s1600/Traverse_Board.jpg)  
---  
  
_Traverse board. Pins on the upper (circular) portion indicate compass heading
and (via distance from the center) for each half hour. Pins on the lower
(rectangular) portion indicate estimated speed during each hour. The board
thus allows an a pilot on a wet deck unsuitable for a paper log to record an
equivalent of a sequence of tuples { direction, speed, time } over four hours,
after which time this information is transferred to the ship 's written
log(normally kept indoors), the progress is plotted as a head-to-tail diagram
on a chart (also kept indoors), and the traverse board is reset. Note that the
direction is read directly off the magnetic compass: thus north (the fleur-de-
lis) is magnetic north, not geographic (celestial) north._  
  
In a future post I hope to discuss more about dead reckoning directions and
explain how the errors that can accumulate in such directions over long
distances were corrected. I will also explain why neither the directions nor
even the corrections could be accurately drawn on a normal (Ptolemaic or
celestial coordinate) map, and yet such dead reckoning directions are
sufficient at least in theory for the pilot to guide his ship from the
starting port to the intended destination port. In practice, pilots "fixed"
errors in their dead reckoning using landmarks and sounding, which I will also
describe. And I hope to describe how this resulted in two incompatible systems
of "navigation" (broadly speaking) during exploration explosion -- the pilot's
dead reckoning methods versus the cosmographers' maps and globes based on
latitude and longitude.  
  
I also hope to someday figure out just why the exploration explosion occurred
when it did. The advent of rigorous dead reckoning -- combining the compass,
the sand glass, and decent estimates of speed with rigorous log-keeping -- did
not occur in Asia (where the Chinese, lacking the sand glass at least, made a
less systematic use of the compass), nor with the Arabs (who seldom used
either sand glass or compass), which along with naval superiority explains why
the exploration explosion occurred from western Europe. The puzzle of why the
explosion started specifically in the 1480s, and not sooner or later, however,
remains a mystery to be solved.

Posted by  [ Nick Szabo ](https://www.blogger.com/profile/16820399856274245684
"author profile") at  [2:18
AM](https://unenumerated.blogspot.com/2012/10/dead-reckoning-and-exploration-
explosion.html "permanent link") [
![](https://resources.blogblog.com/img/icon18_email.gif)
](https://www.blogger.com/email-
post.g?blogID=17908317&postID=674940749077683234 "Email Post") [
![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)
](https://www.blogger.com/post-
edit.g?blogID=17908317&postID=674940749077683234&from=pencil "Edit Post")

[Email This](https://www.blogger.com/share-
post.g?blogID=17908317&postID=674940749077683234&target=email "Email
This")[BlogThis!](https://www.blogger.com/share-
post.g?blogID=17908317&postID=674940749077683234&target=blog
"BlogThis!")[Share to Twitter](https://www.blogger.com/share-
post.g?blogID=17908317&postID=674940749077683234&target=twitter "Share to
Twitter")[Share to Facebook](https://www.blogger.com/share-
post.g?blogID=17908317&postID=674940749077683234&target=facebook "Share to
Facebook")[Share to Pinterest](https://www.blogger.com/share-
post.g?blogID=17908317&postID=674940749077683234&target=pinterest "Share to
Pinterest")

#### 2 comments:

[![](https://resources.blogblog.com/img/blank.gif)
![](//3.bp.blogspot.com/-lHnuJx6W5Kg/Tkc6QD7hAeI/AAAAAAAAAEI/fuodDvO7iig/s35/logo-
whitebg.png)](https://www.blogger.com/profile/18349479103216755952)

[gwern](https://www.blogger.com/profile/18349479103216755952) said...

    

I don't understand the traverse board: there are 4 pegs placed in the top half
giving compass headings, OK, but if there are 4 there, why are there only 2
pegs placed in the rectangular bottom-left section? Where are the speeds for
the other 2 time periods? (And what's that 1 peg in the small square section
bottom-right?)

     [ 7:41 AM ](https://unenumerated.blogspot.com/2012/10/dead-reckoning-and-exploration-explosion.html?showComment=1350571277465#c5895536073353245476 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/delete-comment.g?blogID=17908317&postID=5895536073353245476 "Delete Comment")

![](//resources.blogblog.com/img/blank.gif)

nick said...

    

Each half covers four hours. The top half covers eight half-hour intervals and
the bottom half covers four one-hour intervals. So far two hours have elapsed.  
  
The bottom half shows the speed was six knots the first hour and eight and
one-half knots the second hour. (The bottom right peg shows the fraction).

     [ 12:47 PM ](https://unenumerated.blogspot.com/2012/10/dead-reckoning-and-exploration-explosion.html?showComment=1350589648942#c947204343689636801 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/delete-comment.g?blogID=17908317&postID=947204343689636801 "Delete Comment")

[Post a
Comment](https://www.blogger.com/comment.g?blogID=17908317&postID=674940749077683234)

[Newer Post](https://unenumerated.blogspot.com/2012/10/dead-reckoning-maps-
and-errors.html "Newer Post") [Older
Post](https://unenumerated.blogspot.com/2012/08/authority-and-ad-hominem.html
"Older Post") [Home](https://unenumerated.blogspot.com/)

Subscribe to: [Post Comments
(Atom)](https://unenumerated.blogspot.com/feeds/674940749077683234/comments/default)

## Pages

  * [Home](https://unenumerated.blogspot.com/)

## About Me

[ Nick Szabo ](https://www.blogger.com/profile/16820399856274245684)

    "A premier thinker about history, law and economics, and the lessons they have for security." -- Adam Shostack, [Emergent Chaos ](http://www.emergentchaos.com/archives/2005/12/nick_szabo_blog.html)   
  
"Szabo comes out with these essays that leave me in awe." -- [Brian
Dunbar](http://space4commerce.blogspot.com/2011/06/tab-clearing_14.html)  
  
"Reading material that is eclectic, challenging and endlessly fascinating."
\-- Sean McGrath,
[Propylon](http://seanmcgrath.blogspot.com/2004_05_09_seanmcgrath_archive.html)  
  
"Like most blogs worth my attention, this blog is updated only infrequently.
That is because the authors of blogs worth my attention only post when they
have something to say that is true, relevant and not already known by their
audience. Most of the human race does not have the skill to know when an idea
has these three properties. The skill is particularly rare in the fields of
politics and economics, which is why this blog is such a rare and valuable
thing." \-- [Richard Hollerith](http://dl4.jottit.com/)  
  

[View my complete
profile](https://www.blogger.com/profile/16820399856274245684)

## Blog Archive

  * [ ► ](javascript:void\(0\)) [ 2018 ](https://unenumerated.blogspot.com/2018/) (1)
    * [ ► ](javascript:void\(0\)) [ March ](https://unenumerated.blogspot.com/2018/03/) (1)

  * [ ► ](javascript:void\(0\)) [ 2017 ](https://unenumerated.blogspot.com/2017/) (3)
    * [ ► ](javascript:void\(0\)) [ March ](https://unenumerated.blogspot.com/2017/03/) (1)
    * [ ► ](javascript:void\(0\)) [ February ](https://unenumerated.blogspot.com/2017/02/) (2)

  * [ ► ](javascript:void\(0\)) [ 2016 ](https://unenumerated.blogspot.com/2016/) (4)
    * [ ► ](javascript:void\(0\)) [ December ](https://unenumerated.blogspot.com/2016/12/) (1)
    * [ ► ](javascript:void\(0\)) [ July ](https://unenumerated.blogspot.com/2016/07/) (1)
    * [ ► ](javascript:void\(0\)) [ March ](https://unenumerated.blogspot.com/2016/03/) (1)
    * [ ► ](javascript:void\(0\)) [ February ](https://unenumerated.blogspot.com/2016/02/) (1)

  * [ ► ](javascript:void\(0\)) [ 2015 ](https://unenumerated.blogspot.com/2015/) (3)
    * [ ► ](javascript:void\(0\)) [ October ](https://unenumerated.blogspot.com/2015/10/) (1)
    * [ ► ](javascript:void\(0\)) [ July ](https://unenumerated.blogspot.com/2015/07/) (1)
    * [ ► ](javascript:void\(0\)) [ May ](https://unenumerated.blogspot.com/2015/05/) (1)

  * [ ► ](javascript:void\(0\)) [ 2014 ](https://unenumerated.blogspot.com/2014/) (3)
    * [ ► ](javascript:void\(0\)) [ December ](https://unenumerated.blogspot.com/2014/12/) (1)
    * [ ► ](javascript:void\(0\)) [ October ](https://unenumerated.blogspot.com/2014/10/) (1)
    * [ ► ](javascript:void\(0\)) [ July ](https://unenumerated.blogspot.com/2014/07/) (1)

  * [ ► ](javascript:void\(0\)) [ 2013 ](https://unenumerated.blogspot.com/2013/) (3)
    * [ ► ](javascript:void\(0\)) [ November ](https://unenumerated.blogspot.com/2013/11/) (1)
    * [ ► ](javascript:void\(0\)) [ August ](https://unenumerated.blogspot.com/2013/08/) (1)
    * [ ► ](javascript:void\(0\)) [ July ](https://unenumerated.blogspot.com/2013/07/) (1)

  * [ ▼ ](javascript:void\(0\)) [ 2012 ](https://unenumerated.blogspot.com/2012/) (8)
    * [ ▼ ](javascript:void\(0\)) [ October ](https://unenumerated.blogspot.com/2012/10/) (2)
      * [Dead reckoning, maps, and errors](https://unenumerated.blogspot.com/2012/10/dead-reckoning-maps-and-errors.html)
      * [Dead reckoning and the exploration explosion](https://unenumerated.blogspot.com/2012/10/dead-reckoning-and-exploration-explosion.html)
    * [ ► ](javascript:void\(0\)) [ August ](https://unenumerated.blogspot.com/2012/08/) (2)
    * [ ► ](javascript:void\(0\)) [ July ](https://unenumerated.blogspot.com/2012/07/) (4)

  * [ ► ](javascript:void\(0\)) [ 2011 ](https://unenumerated.blogspot.com/2011/) (12)
    * [ ► ](javascript:void\(0\)) [ December ](https://unenumerated.blogspot.com/2011/12/) (1)
    * [ ► ](javascript:void\(0\)) [ July ](https://unenumerated.blogspot.com/2011/07/) (1)
    * [ ► ](javascript:void\(0\)) [ June ](https://unenumerated.blogspot.com/2011/06/) (2)
    * [ ► ](javascript:void\(0\)) [ May ](https://unenumerated.blogspot.com/2011/05/) (2)
    * [ ► ](javascript:void\(0\)) [ February ](https://unenumerated.blogspot.com/2011/02/) (2)
    * [ ► ](javascript:void\(0\)) [ January ](https://unenumerated.blogspot.com/2011/01/) (4)

  * [ ► ](javascript:void\(0\)) [ 2010 ](https://unenumerated.blogspot.com/2010/) (9)
    * [ ► ](javascript:void\(0\)) [ December ](https://unenumerated.blogspot.com/2010/12/) (1)
    * [ ► ](javascript:void\(0\)) [ October ](https://unenumerated.blogspot.com/2010/10/) (4)
    * [ ► ](javascript:void\(0\)) [ September ](https://unenumerated.blogspot.com/2010/09/) (2)
    * [ ► ](javascript:void\(0\)) [ February ](https://unenumerated.blogspot.com/2010/02/) (2)

  * [ ► ](javascript:void\(0\)) [ 2009 ](https://unenumerated.blogspot.com/2009/) (29)
    * [ ► ](javascript:void\(0\)) [ November ](https://unenumerated.blogspot.com/2009/11/) (3)
    * [ ► ](javascript:void\(0\)) [ October ](https://unenumerated.blogspot.com/2009/10/) (6)
    * [ ► ](javascript:void\(0\)) [ September ](https://unenumerated.blogspot.com/2009/09/) (3)
    * [ ► ](javascript:void\(0\)) [ August ](https://unenumerated.blogspot.com/2009/08/) (1)
    * [ ► ](javascript:void\(0\)) [ July ](https://unenumerated.blogspot.com/2009/07/) (1)
    * [ ► ](javascript:void\(0\)) [ June ](https://unenumerated.blogspot.com/2009/06/) (3)
    * [ ► ](javascript:void\(0\)) [ May ](https://unenumerated.blogspot.com/2009/05/) (6)
    * [ ► ](javascript:void\(0\)) [ April ](https://unenumerated.blogspot.com/2009/04/) (3)
    * [ ► ](javascript:void\(0\)) [ January ](https://unenumerated.blogspot.com/2009/01/) (3)

  * [ ► ](javascript:void\(0\)) [ 2008 ](https://unenumerated.blogspot.com/2008/) (55)
    * [ ► ](javascript:void\(0\)) [ December ](https://unenumerated.blogspot.com/2008/12/) (2)
    * [ ► ](javascript:void\(0\)) [ October ](https://unenumerated.blogspot.com/2008/10/) (2)
    * [ ► ](javascript:void\(0\)) [ September ](https://unenumerated.blogspot.com/2008/09/) (4)
    * [ ► ](javascript:void\(0\)) [ August ](https://unenumerated.blogspot.com/2008/08/) (9)
    * [ ► ](javascript:void\(0\)) [ July ](https://unenumerated.blogspot.com/2008/07/) (4)
    * [ ► ](javascript:void\(0\)) [ June ](https://unenumerated.blogspot.com/2008/06/) (6)
    * [ ► ](javascript:void\(0\)) [ May ](https://unenumerated.blogspot.com/2008/05/) (6)
    * [ ► ](javascript:void\(0\)) [ April ](https://unenumerated.blogspot.com/2008/04/) (4)
    * [ ► ](javascript:void\(0\)) [ March ](https://unenumerated.blogspot.com/2008/03/) (10)
    * [ ► ](javascript:void\(0\)) [ February ](https://unenumerated.blogspot.com/2008/02/) (5)
    * [ ► ](javascript:void\(0\)) [ January ](https://unenumerated.blogspot.com/2008/01/) (3)

  * [ ► ](javascript:void\(0\)) [ 2007 ](https://unenumerated.blogspot.com/2007/) (47)
    * [ ► ](javascript:void\(0\)) [ December ](https://unenumerated.blogspot.com/2007/12/) (1)
    * [ ► ](javascript:void\(0\)) [ October ](https://unenumerated.blogspot.com/2007/10/) (2)
    * [ ► ](javascript:void\(0\)) [ September ](https://unenumerated.blogspot.com/2007/09/) (8)
    * [ ► ](javascript:void\(0\)) [ August ](https://unenumerated.blogspot.com/2007/08/) (10)
    * [ ► ](javascript:void\(0\)) [ July ](https://unenumerated.blogspot.com/2007/07/) (4)
    * [ ► ](javascript:void\(0\)) [ June ](https://unenumerated.blogspot.com/2007/06/) (4)
    * [ ► ](javascript:void\(0\)) [ May ](https://unenumerated.blogspot.com/2007/05/) (8)
    * [ ► ](javascript:void\(0\)) [ April ](https://unenumerated.blogspot.com/2007/04/) (1)
    * [ ► ](javascript:void\(0\)) [ March ](https://unenumerated.blogspot.com/2007/03/) (2)
    * [ ► ](javascript:void\(0\)) [ February ](https://unenumerated.blogspot.com/2007/02/) (4)
    * [ ► ](javascript:void\(0\)) [ January ](https://unenumerated.blogspot.com/2007/01/) (3)

  * [ ► ](javascript:void\(0\)) [ 2006 ](https://unenumerated.blogspot.com/2006/) (130)
    * [ ► ](javascript:void\(0\)) [ December ](https://unenumerated.blogspot.com/2006/12/) (4)
    * [ ► ](javascript:void\(0\)) [ November ](https://unenumerated.blogspot.com/2006/11/) (7)
    * [ ► ](javascript:void\(0\)) [ October ](https://unenumerated.blogspot.com/2006/10/) (15)
    * [ ► ](javascript:void\(0\)) [ September ](https://unenumerated.blogspot.com/2006/09/) (15)
    * [ ► ](javascript:void\(0\)) [ August ](https://unenumerated.blogspot.com/2006/08/) (20)
    * [ ► ](javascript:void\(0\)) [ July ](https://unenumerated.blogspot.com/2006/07/) (5)
    * [ ► ](javascript:void\(0\)) [ June ](https://unenumerated.blogspot.com/2006/06/) (10)
    * [ ► ](javascript:void\(0\)) [ May ](https://unenumerated.blogspot.com/2006/05/) (4)
    * [ ► ](javascript:void\(0\)) [ April ](https://unenumerated.blogspot.com/2006/04/) (3)
    * [ ► ](javascript:void\(0\)) [ March ](https://unenumerated.blogspot.com/2006/03/) (11)
    * [ ► ](javascript:void\(0\)) [ February ](https://unenumerated.blogspot.com/2006/02/) (10)
    * [ ► ](javascript:void\(0\)) [ January ](https://unenumerated.blogspot.com/2006/01/) (26)

  * [ ► ](javascript:void\(0\)) [ 2005 ](https://unenumerated.blogspot.com/2005/) (44)
    * [ ► ](javascript:void\(0\)) [ December ](https://unenumerated.blogspot.com/2005/12/) (16)
    * [ ► ](javascript:void\(0\)) [ November ](https://unenumerated.blogspot.com/2005/11/) (5)
    * [ ► ](javascript:void\(0\)) [ October ](https://unenumerated.blogspot.com/2005/10/) (23)

|  
  
---|---  
  
Simple theme. Powered by [Blogger](https://www.blogger.com).

  *[2:18 AM]: 2012-10-18T02:18:00-07:00

