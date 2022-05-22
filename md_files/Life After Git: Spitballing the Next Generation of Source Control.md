What kind of version control system will eventually replace Git? When I pose
this question to fellow developers, I get one of two responses. Some are
shocked by the idea that **anything**  will ever replace Git. “Version control
is a solved problem and Git is the solution!” Others imagine what I call
Git++, a system that is essentially the same as Git, but with some of the
common problems and annoyances resolved. Neither of these are likely to be the
case.

 **> Why Git Won**

To imagine what might come after Git, we have to remember what Git replaced
and why. Git supplanted
[Subversion](https://en.wikipedia.org/wiki/Apache_Subversion) not by improving
upon it, but by rethinking one of Subversion’s core assumptions. Subversion
assumed that revision control had to be centralized. How else could it work,
after all? The result of this assumption was a tool where branching was
discouraged, merging was painful, and forking was unimaginable.

Git flipped this on its head. “Version control should be distributed! Anyone
should be able to clone a repo, modify it locally, and propose the changes to
others!” Because of this inversion, we got a tool where branching is trivial,
merging is manageable, and forking is a feature. Git isn’t an easy tool to
grok at first exposure, but it gained widespread adoption in spite of this
specifically because of these characteristics. Git offered benefits to solo
developers, in stark contrast to SVN, but it made **teams**  orders of
magnitude more productive.

Cause and effect are hard to tease apart, but it’s no coincidence that Git’s
adoption corresponded with a Cambrian explosion of mainstream open source
projects.

 **> Whats Next?**

Whatever replaces Git, be it next year or next decade, will follow a similar
path in doing so. It will not be a small improvement over the model Git
already provides. Instead, it will succeed by rethinking one of Git’s
foundational principles. In doing so, it will provide orders of magnitude
greater productivity for it’s adopters.

 **> Just Text?**

Git assumes code, and everything else, is just diffable text. Git is really
good, and really really fast, at diffing text. This is what makes Git great,
but it’s also the assumption that gives a future system an opportunity. Code
is not **just**  text. Code is highly structured text, conforming to specific
lexical grammars. Even in weakly, dynamically typed languages, there is a ton
of information in that code a computer can know about statically.

 _ **What would a version control system look like that knew something about
your code, beyond just textual diffing?**_

Git will happily check in a syntax error: what if it didn’t? A commit in Git
is just a commit, regardless of whether you added a code comment, tweaked a
unit test, refactored a method name, added a small bit of functionality, or
completely changed the behavior of your entire program. What if these kinds of
changes were represented differently?

Git doesn’t know anything about your package manager or semantic versioning.
Instead, you check in some kind of configuration file for your package manager
of choice. That defines dependencies and declares a version, and it’s your job
to keep these things in sync and to make judgement calls about version bumps.
In a any given language you may have 2 or 3 or 12 package managers to choose
from and support, each with their own config file, which also has to be
checked in and kept in sync.

What if, instead, our version control system was also our package manager, and
it understood and tracked our dependencies and their versions? What if, since
it knew about the nature of the changes made to code, it automatically
enforced actual distinctions between bugfix, patch, and breaking changes? Or
maybe, if this is being analyzed and enforced by computers rather than humans,
those distinctions become less meaningful.

Imagine a library your app depended on released a new version. In that
version, they refactored a method name, but didn’t make any changes to
behavior. Our hypothetical next gen system would **provably** know this. Is
that still a breaking change? What if the system automatically refactored
**your**  code, updating to the new method name, in conjunction to the commit
representing the update to the dependency? Sounds scary, but in reality, this
is much safer than what we accept today. Sure, a library owner may have kept
the public interface the same. “Not a breaking change!” Your code may still
compile or run without a source change. “See, non-breaking!” But...if they’ve
completely changed the method’s behavior….you’re still screwed, and nothing is
enforcing that they didn’t except social contract.

 **> Stay Tuned**

These ideas just scratch the surface of what a more context aware version
control system could do, but as the title suggests, I’m just spitballing here.
There are lots of challenges to implementing a system like this, many with
non-obvious solutions that may take years to develop. Ultimately, though, you
can bet on one thing being true: something radically different, and radically
better, will eventually come along to replace Git.

