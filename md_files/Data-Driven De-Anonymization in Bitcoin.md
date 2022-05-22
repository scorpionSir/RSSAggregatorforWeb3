[![](https://jonasnick.github.io/images/zurich-
youtube.png)](https://www.youtube.com/watch?v=HScK4pkDNds)

[**Slides**](https://jonasnick.github.io/slides/2016-zurich-meetup.pdf)

**Abstract**

We analyse the performance of several clustering algorithms in the digital
peer- to-peer currency Bitcoin. Clustering in Bitcoin refers to the task of
finding addresses that belongs to the same wallet as a given address. In order
to assess the effectiveness of clustering strategies we exploit a vulner-
ability in the implementation of Connection Bloom Filtering to capture ground
truth data about 37,585 Bitcoin wallets and the addresses they own. In
addition to well-known clustering techniques, we introduce two new strategies,
apply them on addresses of the collected wallets and evaluate precision and
recall using the ground truth. Due to the nature of the Connection Bloom
Filtering vulnerability the data we collect is not without errors. We present
a method to correct the performance metrics in the presence of such
inaccuracies. Our results demonstrate that even modern wallet software can not
protect its users properly. Even with the most basic clustering technique
known as multi- input heuristic, an adversary can guess on average 68.59%
addresses of a victim. We show that this metric can be further improved by
combining several more sophisticated heuristics.

[**Read full thesis**](https://jonasnick.github.io/papers/thesis.pdf)

