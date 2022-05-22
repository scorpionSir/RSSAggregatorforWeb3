Navigation is the art or science of combining information and reducing error
to _keep oneself on, or return oneself to, a route_ that will get you where
you want to go. Note what I did _not_ say here. Navigation is _not
necessarily_ the art or science of _locating where you are._ While answering
the latter question – i.e. locating oneself in a Euclidean space, or a space
reasonably projectable onto a Euclidean space – can usefully solve the
navigation problem, figuring out such a location often requires different, and
often more, information than you need to answer the questions of how to stay
on or return to your desired route. And indeed this is what dead reckoning
does – it gets you where you want to go with different information than what
you would need to draw or find yourself on a normal map. I hope to explain
more about this important incompatibility between the pilots’ and
cosmographers’ systems during most of the age of exploration in a future post,
but for now I will give an overview of the historical development of dead
reckoning.  
  
Between Italy of the late 13th century and the advent of GPS, dead reckoning
formed the basis of most modern navigation. Dead reckoning was in particular
the primary method of navigation used during the exploration explosion of the
late 15th and early 16th centuries – the startlingly unprecedented voyages
across unknown oceans of Dias, da Gama, Columbus, Magellan, and so on.  
  
Dead reckoning is based on a sequence of vectors. Each vector consists of two
essential pieces of information: direction and distance. Distance is typically
calculated from time and speed, so each vector typically consists of the tuple
{direction, time, speed}. With only speed and time, we have only a scalar
distance value – it could be in any direction. With time but not speed, or
speed but not time, we don’t have enough information to determine the distance
covered.  
  
From the start of a voyage to the last docking at the home port, dead
reckoning was a strict regimen that never stopped: day and night, in calm and
in storm, its measurement, recording, and diagramming protocols were
rigorously followed.  
  
Measuring or estimating the speed of a ship was a craft mystery the nature of
which is still debated today, so I’ll skip over that and focus on the two more
straightforward innovations in measurement, both of which occurred in or
reached Italy and were first combined there in the 13thcentury: in measuring
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
_feng shui_ and then for navigation by the early 12thcentury. Somehow, without
any recorded intermediaries, it appears in the writings of authors in the
region of the English Channel in the late 12thcentury where it was quite
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
  
[![](http://1.bp.blogspot.com/-WxE-VGeJQ6w/UH_CidNj2rI/AAAAAAAAAOU/picdBtS-
aAU/s1600/CompassMentions12thAndEarly13thCenturies_NormanHoldings1130.jpg)](http://1.bp.blogspot.com/-WxE-
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
  

[![](http://1.bp.blogspot.com/-hwrQNZ2Op-k/UH-8zNlbYDI/AAAAAAAAANw/UxKWGHP4Sz0/s320/DeadReckoningBasic.png)](http://1.bp.blogspot.com/-hwrQNZ2Op-k/UH-8zNlbYDI/AAAAAAAAANw/UxKWGHP4Sz0/s1600/DeadReckoningBasic.png)

For recording speed and direction for each sand glass time interval (e.g. half
hour), pilots used some variation of the _traverse board_ , in which these
values were specified by the locations of pegs in the board.  
  
[![](http://4.bp.blogspot.com/-SvsapDVgOyU/UH-90y5bmtI/AAAAAAAAAOA/8c1givzy8a8/s1600/Traverse_Board.jpg)](http://4.bp.blogspot.com/-SvsapDVgOyU/UH-90y5bmtI/AAAAAAAAAOA/8c1givzy8a8/s1600/Traverse_Board.jpg)  
---  
  
 _Traverse board. Pins on the upper (circular) portion indicate compass
heading and (via distance from the center) for each half hour. Pins on the
lower (rectangular) portion indicate estimated speed during each hour. The
board thus allows an a pilot on a wet deck unsuitable for a paper log to
record an equivalent of a sequence of tuples { direction, speed, time } over
four hours, after which time this information is transferred to the ship’s
written log(normally kept indoors), the progress is plotted as a head-to-tail
diagram on a chart (also kept indoors), and the traverse board is reset. Note
that the direction is read directly off the magnetic compass: thus north (the
fleur-de-lis) is magnetic north, not geographic (celestial) north._  
  
In a future post I hope to discuss more about dead reckoning directions and
explain how the errors that can accumulate in such directions over long
distances were corrected. I will also explain why neither the directions nor
even the corrections could be accurately drawn on a normal (Ptolemaic or
celestial coordinate) map, and yet such dead reckoning directions are
sufficient at least in theory for the pilot to guide his ship from the
starting port to the intended destination port. In practice, pilots "fixed"
errors in their dead reckoning using landmarks and sounding, which I will also
describe. And I hope to describe how this resulted in two incompatible systems
of “navigation” (broadly speaking) during exploration explosion -- the pilot’s
dead reckoning methods versus the cosmographers’ maps and globes based on
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

