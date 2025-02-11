[![logo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAICAYAAAD5nd/tAAAACXBIWXMAAA7DAAAOwwHHb6hkAAABj0lEQVQoz12Sv0vDQBTHT0HrD4QWRJRLi3QQOojon1JxUhcFQQeViknrJjiIglgRhW4OTiLSWXB10MnJoToI0lp6ESu1TZNc/L7LFcGDD+8u4X3y3r0wKeUUeAqwEBVYZa9amhCb0bydjbdti/vAsy0jALPYp0EZSODq91W8W2AQPGqZg9CUvkvGUv08fSEywwGESDIaoAW+QQHJbWEq+Y+mqc8OCV3wASZBzP+qJJ8ZY2JrpKgqMvk8Yh8kvL6b6sZ+WZicki/BIBgFUVCk5ywsTr4ikvxI+l4F+w20e21bcQiNGUiZ2OZdSGLYr+jW9+hcw3NUx/DBY6pSCcELZCQ8RMtvOK+K9aErO5ugCqdJCDESVVzSwgMSQhLRwjMl1C1Xw+H4Mf/zPQFhxN5J3qrEbGJRmGMDwjIMYfF+yDNauK+FvVp4qlqG6F4PpY3goMIWxebdiVdbi1CiDC+dtwBdfmcA+X/CQqflFGQP6nf5+20C6blB4yYnRW7chcihCYbwFk0ZzAES9eiIq+DiFyR9m3ZUxiupAAAAAElFTkSuQmCC)![logo](/static/9c635c914229a850d1a9fd284014bdd0/65e33/eco_logo.png)](/)

  * [新闻资讯](/)

  *   * [零时学院](/c0llege)

  * [开发者门户](/develop)

  * [生态漫游](/ecos)

Ξ

Search by [](https://www.algolia.com/?utm_source=react-
instantsearch&utm_medium=website&utm_content=&utm_campaign=poweredby)

## VITALIK：区块链“验证”的哲学

关于区块链验证，为什么协和派比定义派更优？基于协和派的观点，区块链验证有哪些发展，以及可以如何有效抵抗51%攻击？

* * *

VB

Vitalik Buterin 2020-08-27

来源| [vitalik.ca](https://vitalik.ca/general/2020/08/17/philosophy.html)

可以结合这些文章一起看:

  * [A Proof of Stake Design Philosophy](https://medium.com/@VitalikButerin/a-proof-of-stake-design-philosophy-506585978d51)
  * [The Meaning of Decentralization](https://medium.com/@VitalikButerin/the-meaning-of-decentralization-a0c92b76a274)
  * [Engineering Security through Coordination Problems](https://vitalik.ca/general/2017/05/08/coordination_problems.html)

区块链的一个强大特性是链上每一部分的操作都可以被独立验证。即使区块链上绝大部分的矿工（或PoS机制下的验证者）被攻击者控制了，且该攻击者尝试推动无效区块的敲定，网络也可以轻易拒绝。甚至那些当时并不在验证区块的用户也（可能会自动）收到其他正在验证的用户发出的警报，他们可以确认攻击者的区块链是无效的，然后自动拒绝该链，并且进行协调以接受遵循规则的链。

但我们真正需要多少验证呢？我们是需要100个还是1000个独立验证节点？我们是否需要创造一种文化使得全世界的普通用户都运行软件来验证交易？这些问题本身就很困难，虽然区块链领域发轫于一条“Nakamoto”工作量证明式的区块链，但如果我们想架构基于更优共识机制的区块链，这些问题是我们需要解决的关键挑战。

  

# 为什么要“验证”？

![](https://i.ibb.co/S5C7Yyj/1-50698b31fb.png)

51%攻击正推进无效区块的敲定。我们需要网络拒绝这条链！  

用户验证区块链主要有两点好处：首先，它能最大程度提高节点对 **权威链**
（社区成员普遍认为有效的链）做出正确判断并维持该链的几率。通常，有最多矿工/验证者支持认为有效的链被定义为权威链（比如，比特币里的“最长链”）。由此，无效链就自然被拒绝了。如果需要在多条有效链中选择，那么有最多矿工/验证者支持的链胜出。所以，如果你的节点可以验证所有的有效状态，也就可以检测出哪些链是有效、哪些链是无效的，从而最大程度提高你正确判断哪条是权威链的几率。

但关于为什么验证区块链是有利的，还有另一个更深层次的原因。假设一个能力很强的攻击者试图推动协议的改变（比如，改变发行量），并得到大多数矿工的支持。如果没有其他人验证这条链，这次攻击就很容易成功了：默认情况下，每个人的客户端都会接受这条新链。等到大家都知道发生什么事了，这将取决于是否有异议者试图协调其他人来反对这条链。
**但如果一般的用户都在验证，那么协调的问题就落在了另一边：这成了想要改变协议的人的责任去说服用户自行下载软件补丁，接受协议的更改。**

如果有足够多的用户在验证， **那么改变协议的尝试并不会在默认情况下成功 (default to
victory)。相反，试图改变协议的这一举动会变得有争议，并在默认情况下陷入混乱 (default to chaos)。
**混乱会中断很多工作，且需要带外的社会协作来解决，但这会给攻击者带来更大的阻碍，削弱攻击者认为他们能够轻易成功并脱身的信心，甚至打消他们尝试发起攻击的念头。如果大多数用户都在验证（直接或间接），而攻击只得到大部分矿工的支持，那么这样的攻击将会**
默认走向失败 (default to failure)**，这是最好的结果。

  

# 定义派 (definition) vs 协和派 (coordination)

请注意，这个论证逻辑与我们经常听到的非常不一样：当一条区块链的规则发生了改变，从“定义”上来说，这条链就不再是正确链了，无论有多少用户认同这些新的规则，重要的是你个人可以选择留在那条你所赞同的旧链上。

这是[Gavin Anderson](http://gavinandresen.ninja/a-definition-of-
bitcoin)提出的定义派的一个典型观点：

![](https://i.ibb.co/5B06JZM/2-3ddcbbce35.png)

（译者注：翻译如下）

我想提出一个比特币宏观上的技术定义：

“比特币是一个记录唯一的、经过有效签名的交易的账本，这些交易都被打包进由区块组成的链上，这条链始于创世区块（哈希值为0x000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f）。这条区块链遵循2100万个比特币的发行计划，有着累计最高的双重SHA256工作量证明。

如果要阐释全节点的价值，另外一个来自t[he Wasabi wallet](https://news.ethereum.cn/vitalik-ca-
general-2020-08-17-philosophy/#the-importance-of-running-a-full-
node)的观点表达得更加直接。

![](https://i.ibb.co/QQyNLqM/3-86333b36b6.png)

(译者注：翻译如下)

当运行比特币全节点时，你可以界定自己自愿同意的精确货币规则，没有人可以将这一选择强加在你身上。因此，任何自主个体想要获得财务独立，都必须运行全节点。一旦你自己的规则切实设立了，你的软件会在比特币的点对点网络里发现与你的规则不冲突的其他节点。这些对等节点会给你发送符合他们规则的有效交易和区块，你可以自己验证这些交易和区块是否符合你的规则。如果被提议的交易中有一笔与你的规则相冲突，那么可以标记它为无效，然后切断与该节点的连接并禁止该节点给你发送恶意交易。

**确立你的货币主权**

通过全节点，你可以对比特币这种可靠货币的规则进行界定、验证和执行。

请留意这个观点的两个核心点：

  * 如果区块链的一个版本不接受你认为是基本的且不可商榷的规则，那么从定义上来说它就不是比特币区块链（在其他情况下也不是以太坊或其他任何链），无论有多少人承认该链。
  * 重要的是你所在的区块链上的规则是你认为可接受的。

但是，我认为这种“个人主义”的看法是非常错误的。为什么呢，让我们来看一下会引起顾虑的一个情景：绝大多数的参与者都接受对协议规则的某些改变，而只有你觉得无法接受。比如，如果未来交易费变得非常低，那么为了保持链的安全性，差不多所有人都同意采用一些新规则来增加发行量。而你坚持要继续执行旧的规则来运行你的节点，然后对大多数人所在的链进行分叉。

从你的观点来看，你的币仍然保持在以你认同的规则来运行的系统中。但这又如何呢？其他人不会接受你的代币；交易所不会接受你的代币；网站会展示新币的一些高峰值，但所指代的是多数人所在链的代币。你的代币没有“价值”。加密货币和区块链从根本上来说是社会建构的，如果没有其他人相信它们的话，它们什么都不是。

![](https://i.ibb.co/ZW49bVc/4-696aecfad2.png)

所以，那另一派的观点是什么呢？它的核心理念是[ **用协和谬误 (coordination problem)
的方法来解决区块链的工程安全问题**](https://vitalik.ca/general/2017/05/08/coordination_problems.html)。

通常来说，现实世界中的协和谬误是很糟糕的事：如果英语这门语言可以摆脱它高度复杂性和不规则的拼写系统，仅仅保留发音，或如果美国转用公制，或如果我们可以在一次经济萧条中把物价和工资都下调10个百分点，这些对大多数人来说都是好事。然而，在现实中，这些转变都需要得到每个人的同意才可行，这经常是非常非常困难的。

但是， **在区块链应用上，我们将协和谬误转化为优势。我们将协和谬误创造的摩擦作为抵挡中心化攻击者发起的不当行为的壁垒**
。我们建构具有特性X的系统，并保证会保持特性X，因为将规则从X改为非X需要所有人都同意并且同时升级他们的软件。即使有攻击者可以强推改变，这样做也是非常难的，尤其是当用户负责积极协调异议以抵抗改变的时候，难度会更大。

请注意协和派观点的特别之处在于：完全不同于上述所说运行全节点的目的只是为了独善其身，且在出现争议性强的硬分叉时，只有运行全节点的人才是安全的。而协和派观点更像是群体免疫：越多的人参与验证，每个人就越安全，且即使只有一部分人在验证，每个人也能得到高度保障。

  

# 进一步分析“验证”

我们现在进入下一个话题，它与轻客户端和分片这些话题的相关性很强：通过验证我们实际上实现了什么呢？要理解这一点，让我们先回到前文所述，即如果攻击发生了，对于攻击的发展方向，我们有以下的偏向排序：

**默认失败** > **默认混乱** > **默认成功**

符号“>”在这里当然表示“优于”。最好的情况是攻击直接失败；稍次的情况是攻击引起混乱，大家对什么是正确链莫衷一是；最坏的情况是攻击轻易成功。为什么陷入混乱比攻击成功要好得多？这个问题与动机有关：混乱增加了攻击者的成本，抵消他们最终能成功的胜算，从一开始削弱他们发起攻击的信心。
**“默认混乱” (default-to-chaos)
的设定意味着攻击者不仅需要成功对区块链发起51%攻击，还需要赢得使整个社区信服、跟随改变的“社会战”。成功发起51%攻击并不代表最终的胜利，随后“社会战”的难度远大于此，因此攻击行为也变得没有那么诱人。**

验证机制的目的就是将攻击结果从“默认成功”偏移向“默认失败” (理想情况下)，或“默认混乱”
(没那么理想的情况下)。如果大家都有一个能充分验证的节点，当有攻击者试图改变区块链的一些规则时，这样的攻击会失败。如果部分人有能充分验证的节点，但大部分其他人都没有，这种情况下攻击会导向混乱。但现在我们还可以思考：有没有其他方法可以实现同样的效果？

## 轻客户端和欺诈证明

顺着这个逻辑，自然发展出 **有欺诈证明 (fraud proof) 的轻客户端**
。今天大多数区块链的轻客户端只对由大部分矿工支持的一个特定区块做简单的验证工作，而不费心去查看其他协议规则是否被执行。这些客户端的运行都基于大多数的矿工是诚实的的假定。如果有争议性的分叉发生了，客户端默认跟随链上的大多数，那就变成了是由用户来主动选择是否要留在以旧规则运行的少数人所在的链上。因此，在今天轻客户端的机制下，攻击是默认成功的。但如果加上欺诈证明的话，情况会变得不一样。

下图是欺诈证明最简化的运作形式。通常，区块链上的一个区块只会影响一小部分的区块“状态”（包含账户余额、智能合约代码……）。如果一个充分验证的节点在验证一个区块时发现它是无效的，他们可以生成一个数据包（欺诈证明），这个数据包是从区块状态获得的，包含刚好能验证这个区块的数据。他们向轻客户端广播这个数据包。这样，即使他们没有链上的其他数据，轻客户可以使用这个数据包的数据自行验证区块。

![](https://i.ibb.co/9bCgqhv/5-ae0c3956d9.png)

区块链上的一个区块只会影响一小部分的账户

欺诈证明会包含这些账户的数据以及证明数据正确性的默克尔证明

这项技术有时也以[“ **无状态验证** ”](https://ethresear.ch/t/the-stateless-client-
concept/172)为人所知：与保存一份完整的区块链状态数据不同，客户端可以只保存区块头，客户端可以通过向其他节点请求区块验证所需的状态的默克尔证明来进行实时验证。

这种技术的优势在于 **轻客户端可以只在它们收到警报时才对个别区块进行验证**
，警报是可验证的，所以如果轻客户端接收到一个错误的警报，它们可以停止接收该节点的警报。因此，正常情况下轻客户端仍然是轻量的，只需要验证由大多数矿工/验证者支持的区块。但在一些特殊情况下，大多数人支持的链会包含轻客户端不接受的区块，
**只要有至少一个诚实节点在验证欺诈区块，那个节点会将其视为无效，广播欺诈证明，由此导致网络的其他节点都拒绝这个欺诈区块。**

## 分片

分片是协和派观点的一种自然延展：在分片系统里，交易数量太多了，要求大多数人一直在线直接验证是不现实的。但如果经过合理设计，系统里任何无效的单独区块都可以被检测到，且可以用欺诈证明来证明其无效性，然后在整个网络广播。
**一个使用分片系统的网络可以理解为其中的每个人都是一个轻客户端。只要每个分片上的参与者人数达到了一个最低门槛，那么整个网络都有了群体免疫。**

另外，在分片系统里，区块生成 (不只是区块验证)
是相当方便的，且可以通过消费型笔记本电脑完成，这一点是非常重要的。当网络的核心不再需要依赖高性能硬件时，可以降低拒绝少数人所在链的门槛，同时使得大多数人所驱动的协议改变更难“默认成功”并迫使所有其他人接受。

这就是可审查性在现实世界的意思：并不是一切都需要一直经过所有人的验证，而是 (1) 每个部分都有足量的人进行验证，只要有错误发生都会被检测到；(2)
当错误被检测到，且对所有人都清晰可见。

也就是说，长期来看，区块链肯定可以改善这种情况。 **ZK–SNARKs（或validity proofs，即“有效性证明”）就是其中一种方式**
：这是一种高效可验证的密码学证明，它使区块矿工可以向客户端证明区块是否满足一些任意的、复杂的有效性条件。
**[有效性证明比欺诈证明更好](https://medium.com/starkware/validity-proofs-vs-fraud-
proofs-4ef8b4d3d87a)** ，因为它们不依赖于交互博弈发现欺诈。另一项重要的技术是[ **数据可用性 (data
availability)
检测**](https://arxiv.org/pdf/1809.09044.pdf)，它可以用来保护网络不受那些数据没有完全公开的区块的影响。数据可用性检测是基于一个非常保守的假定，那就是网络上至少有少量的诚实节点在继续运行，好的方面是诚实节点的数量门槛并不高，且即使在有大量攻击者的情况下门槛也不需要提高。

  

# 实时性与51%攻击

现在我将对“默认混乱” (default to chaos)
这种情况的最严重后果进行论述：51%攻击。在众多社区中，现行的常态是如果51%攻击成功了，那么51%攻击的链就必然成为有效链。现实通常都高度遵循这种常态，在最近[以太经典
(ETC) 遭遇的51%攻击](https://blog.bitquery.io/attacker-stole-807k-etc-in-ethereum-
classic-51-attack)中得到充分体现。攻击者对3000多个区块进行回滚
(期间通过双花窃取了807,260个ETC)，他将链的交易往前回溯得很远，而这对于ETC的两个客户端之一OpenEthereum来说，在技术上是无法实现的；结果就是，Geth的节点跟随了攻击者的链，而OpenEthereum的节点留在了原来的链上。

即使这次意外并不是ETC社区计划内的设计，我们可以说这次攻击事实上的确是“默认混乱”的走向。不幸的是，社区随后通过投票决定接受更长的攻击链成为权威链，ETC在[推特](https://twitter.com/eth_classic/status/1289637659351031809)上将这一举动形容为“一如既往，遵循工作量证明”。因此，社区规范主动地帮助攻击者获得胜利。

但其实我们可以对权威链进行不同的定义并达成共识。试想这样一条规则，一旦一个客户端把某个区块打包到权威链，而该区块有超过100个后续区块，从那时起该客户端将拒绝任何不包含该区块的链。或者，在一个以最终确定性为导向的权益证明机制设定里
（比如以太坊2.0)，试想这样一条规则，当一个区块被最终敲定了，它就永远不能被回滚了。

![](https://i.ibb.co/b1660q1/6-552c88d2df.png)

为了方便说明，以5个区块为回滚上限为例；

实际上回滚上限可以更长，如100—1000个区块

也就是说，这实际上对权威链的定义作出了重大的改变：与客户端只看他们接收到的数据本身不同，客户端还要看数据是什么时候收到的。这可能会因为网络延迟出现客户端间产生分歧的情况：如果出现由于大型攻击，互相冲突的区块A和区块B在同一时间被敲定了，且一些客户端先看到A，一些先看到B的情况，怎么办？但我会说这是好事，因为这意味着****试图回滚交易的51%攻击不会“默认成功”，而是“默认混乱”****，然后带外的应急响应机制可以在两个区块间选择哪个被打包到链上。如果协议设计合理的话，强制升级到带外应急响应的成本是很高的：在权益证明机制里，这种情况会要求1/3的验证者牺牲他们的存款，接受被罚没的后果。

我们可以将这个方法拓展到其他方面。我们也可以尝试使[审查交易的51%攻击](https://ethresear.ch/t/censorship-
detectors-via-99-fault-tolerant-consensus/2878)走向“默认混乱”。对实时检测器 ([ **timeliness
detectors**](https://ethresear.ch/t/timeliness-detectors-and-51-attack-
recovery-in-blockchains/6925))
的研究将各种类型的攻击都默认走向失败这个方向推进，尽管还会有一些混乱的情况，因为对于连接不稳定或不在线的节点，实时检测器没有多大作用。

**对于重视不可篡改性的区块链社区，采用这种回滚限制可能是更优的发展方向。**说实话，无论一笔交易已经被打包到链上多长时间，也很难说这条区块链是不可篡改的，总是可能有一些很强的攻击者发起无法预料的攻击，让区块链上的交易发生回滚。当然，我知道即使是BTC和ETC，在极端情况下都已经设有回滚限制。如果发生回滚几周交易的攻击，社区可能会采用用户发起的软分叉来拒绝攻击者的链。但社区如果能更确切地在这件事上达成共识并将其形式化，会是向前迈出的一大步。

  

# 结论

这篇文章其实有几点启示。首先，如果我们承认社会协和的正当性，以及我们承认有关“1/N”信任模型
(即假设在网络的某处存在一个诚实的人；不同于假设某特定一方，比如Infura，是诚实的) 间接验证的合理性，那么我们能够创建扩容性更强的区块链。

最后，如果我们把实时性也列入到定义权威链的影响因素，我们就为提高拒绝51%攻击的能力引入了很多的可能性。其中，最容易获得的特性是[弱主观性 (weak
subjectivity)](https://blog.ethereum.org/2014/11/25/proof-stake-learned-love-
weak-
subjectivity/)：如果客户端被要求至少每三个月上线一次，并拒绝回滚三个月以上的交易，那么我们可以把罚没添加到权益证明机制里，使攻击的成本变得非常高。但是我们可以再进一步：我们可以拒绝回滚被敲定区块的区块链，并由此维持不可篡改性，甚至是抗审查性。由于网络是不可预测的，在某些情况下依赖实时性的确意味着攻击会默认走向混乱，但其利大于弊。

当能理解以上这些观点，我们就能避开以下这些陷阱：(1) 过度中心化；(2) 验证过剩导致低效；以及 (3)
非明智的规范意外使得攻击更加容易。除此之外，这些思维还能帮助我们构建更有韧性、性能更好、更安全的区块链。

  
  

声明：ECN的翻译工作旨在为中国以太坊社区传递优质资讯和学习资源，文章版权归原作者所有，转载须注明原文出处以及ethereum.cn，若需长期转载，请联系[ethereumcn@gmail.com](mailto:ethereumcn@gmail.com)进行授权。

* * *

Ethereum Community Network

以太坊社区网络

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAIAAAAC64paAAAACXBIWXMAABcRAAAXEQHKJvM/AAADm0lEQVQ4yyWU1yv9YRzHnzulKLkR5QLxS1aJyDw2WdkS4Zinc+yRvcLJ3nvvHSG7jBtKVi7IhaRcuBDlD/i9vs734uv7eD6f53mvzxHm5uZRUVHBwcEREREODg6Ojo7W1tb6+voWFhYeHh7//h49PT0bGxsvLy9TU9Po6GiKaaFR8GdycrK9vX1ubi4zMzM9Pb2np6epqamoqIgPuVy+urra2dm5vb39/Pzc3Nw8MDDQ0dGxuLgYExMjOKatre3p6amvr0+hUOTn5+fm5t7d3ZWXl/f393d3d3M074KCgq2tLbVaXVtbyylDQ0Ph4eHSzbOzs2xPTU1lZ2fX1dXV1NS8v78XFxfX19fPzMwolcqWlhb+T1l1dfX4+DiHLi8vR0ZGCmgAtaSkpLW1lYNcXFzc3d0BNj8/PzExwSWfn5+3t7egY8k7NDQ0KysLdM7OzkJHR2dwcPDj44PqjIyMhISEtLS00tLSiooK6r6+vg4ODqCwsLCAVFDw9/dPTEzc3d2VYNvZ2alUqunp6f39/evra5hTWllZaWRkFBISAjy2KLi/v2cJOnahvbOzw1kiMDAQSkgXFha2tra2vr6OkrCCv/rvgbaTk1NycjLSaqAh3uvrq6Q2DBsbG4+OjmDC+uLiguXw8HB8fLxMJmP38vIS28bGxjgXztAJCgpCFIIgdHV1CwsLQcIGp4IiLi6ut7eXbXTOy8sDCEbExsb6+fmdnJxAAXXOz8/d3NyElpYW2EgCYGjQ6KmRwNXVlXNfXl7oIWGUQRVHUlJScCEpKUkYGxuTjaurK7hRBH7aNjc3AUl1Q0MDgfn9/YUF+cVRX19f+IPUyspKYBeSHh8fQ4w2slFWVoZgYPv+/iaYaPH29sYpNFND8kkxIZWaCQnubWxsoIS3tzcosLSqqgrywFlaWgLF2dkZIPEPdra2thRgKsUCG4jL3t7ew8MDAeRaTkUwyFPEN8YyFSzR7+bmhg/yix3gF/b29iyo4M3loPj5+UFMDMvJyUEeJglSpIA7OJScIDhZkpphwogwg1xC/+joKMaenp5SzTZUierh4eHj4yOR7Orqopli0ib5rBlJpGewwAxbPGNUAgICcJIPS0tLEGHEysrKyMgIbYSfnw3yK40k3JgNxEBGAwMD3GZOmEe0ZQYxiR62IKxJHg/3kz/BrwnpYUR4o7y2tranp2dqaqqPj4+ZmRk3mJiYICyOahJONg0NDUkbsP8DL00/zmMjxB8AAAAASUVORK5CYII=)![](/static/57048268f8823dd1ea147faa8e568647/d786d/footer_wechat.png)

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAACXBIWXMAAAsTAAALEwEAmpwYAAAEtUlEQVQ4y01VbUxbZRQ+t1Bm2PicA+0Q2WJM/O0vE5f9848mYIxEcB1Q+knbe/t5u5aWFkrRaGewuFDiNhHovW35LISPwIKDZTJjtE4xkWQON2d0mgyny9iI83rObTU2Obk3773vc5/zPs9zCu2sAO1sAuiqtoyClu65hLKdEyq1NuEwVq3WlqzT2sS63L2gwmfl+E4BFhjsSdDgHk0eIw+GC1YBAqFlBBMOajnhaZ1drNE7xEMGZ7Lc5EyVYpXhfQWuVels4lP0Du4r03EinOwYywMmQEbVWBPQZhYZBFPpkIXBkazocKeKWX68yOWbVvq7M4W+YKbQ6Z1SWvnxfR2u1H4EPohs63BPlcE5Aq1mxCGGassIBLtXiJkKX6gxupIHOM9EUSi8VDA1scncuHYPYkNZZjS5Bdtbv0MikWX8ofkCAjY6k6UyU044hFfQ20QALZeQ2yRmJgSzecaVQ4OfKXbvPwJJksAamAd3eB3CA1ng+y7Ia7/8vAvvnV5TsHy6CEHLZKasUII4QGBK+gq1ScwIjDZRWTqXGT6yBu7e9aP+6EZ5IHoFLP5VeCDdgd3dPYhG1xTEVO9IEsNaFIkhwEoSgM6M2nz44G+YXr0IbdwMnLTMwqstaQXbuWB39yy+4gjNA+ubZPb2UrAn3YWbP/wBp7pmC02u1AEUCgGFEiBrkJokwNTEN0yO3R0wudOM0TWO18ljBmcqrLcPe03uhKrNHAeNZYj5t4uh+KcKizv9GJJ6ErGqCbCWrEFqfre5A9sXJDA4xhidbQSfjVYYHILbzCd9J/Sx4Gtv9jWzgQnYQaCXGwIA4IWVpe8ZzjNZhKQeJ3JApiWf+UOZwuvfPoJnjreD1SMwJrSC0fFRA+sV3vL2zvr4nkygxTgQqW8MPFff2AWN6j5GeijB1c9vgts3pTQ6UhVo/iNACSDTks+uIWDtcQ3wARECfXNwqifzAssPN+vZQZeO+9Bs7xyv9/YuPOuLLIKnZw6kHQm+2LgF5E8SNQ+YMzItbn71G8y0SND1zgoTiq5CJHb5Cf/bS2ozP/yiMzhzLNx/+Y3+s5ulp+NZiLx/RT7DhbkthtxBOuRbFlQUJ5JfSHwpHzb9PN3TjDc8B85A+iVX10TQG1kMYT0fjF6E4Lur/4kyMHAJRUmRKCq0ThXZppyySXGiBNxG0/4l3YPX1f3QpO6BXdxksp+1WD1ik70zDb7wLH6uQQb7Ovsrw/szhWjuEiRGidkPGpwaZGzKJrGkBNxH09IGte4DRtNxBlpNscPtlnglFjRr4/Kzn279Cb2RFdkyertYjRg1Tdx5Soo8duT4UDYpTpSAG9fv5tLCnwNNRwx0liFwBQV57Wr2NkNgVnd6n8EpohjCEcQolqcNzTNsmVqvIqaUTWLqxQTE4xuKS5/8yJwZXGLOnV9nVpe3mRieGbVJzGQwTp44FVqcNDQg5DlG88zo/BjkqYFMSTGKE20i05LPyAWkJglAZya3ScwIjBvDc05AK5sHpGoxi/IXaGpQ0MlOFCdKAJmWrEUfktVEAejMsMViYkZgbTKOkB+w+dLbksSSioYtKVed+xsQj5Jp5Xs8GlLzhD03obU4sdv+h/EPsbi7Iqfeg68AAAAASUVORK5CYII=)![](/static/1b87ba5dd8a4dda4d8d17e472bd9cefb/002c1/footer_ethereum.png)

订阅

[ ](https://twitter.com/EthereumCN)[ ](https://discord.gg/KUywx3JJJU)[
](https://i.ibb.co/mBgmDgF/footer-wechat.webp)[
](https://github.com/EthereumCN)[ ](Mailto:eth@ecn.co)[
](https://www.ethereum.cn/rss.xml)

蜀ICP备2021001286号 ](https://beian.miit.gov.cn/)

Ethereum Community Network

以太坊社区网络

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAIAAAAC64paAAAACXBIWXMAABcRAAAXEQHKJvM/AAADm0lEQVQ4yyWU1yv9YRzHnzulKLkR5QLxS1aJyDw2WdkS4Zinc+yRvcLJ3nvvHSG7jBtKVi7IhaRcuBDlD/i9vs734uv7eD6f53mvzxHm5uZRUVHBwcEREREODg6Ojo7W1tb6+voWFhYeHh7//h49PT0bGxsvLy9TU9Po6GiKaaFR8GdycrK9vX1ubi4zMzM9Pb2np6epqamoqIgPuVy+urra2dm5vb39/Pzc3Nw8MDDQ0dGxuLgYExMjOKatre3p6amvr0+hUOTn5+fm5t7d3ZWXl/f393d3d3M074KCgq2tLbVaXVtbyylDQ0Ph4eHSzbOzs2xPTU1lZ2fX1dXV1NS8v78XFxfX19fPzMwolcqWlhb+T1l1dfX4+DiHLi8vR0ZGCmgAtaSkpLW1lYNcXFzc3d0BNj8/PzExwSWfn5+3t7egY8k7NDQ0KysLdM7OzkJHR2dwcPDj44PqjIyMhISEtLS00tLSiooK6r6+vg4ODqCwsLCAVFDw9/dPTEzc3d2VYNvZ2alUqunp6f39/evra5hTWllZaWRkFBISAjy2KLi/v2cJOnahvbOzw1kiMDAQSkgXFha2tra2vr6OkrCCv/rvgbaTk1NycjLSaqAh3uvrq6Q2DBsbG4+OjmDC+uLiguXw8HB8fLxMJmP38vIS28bGxjgXztAJCgpCFIIgdHV1CwsLQcIGp4IiLi6ut7eXbXTOy8sDCEbExsb6+fmdnJxAAXXOz8/d3NyElpYW2EgCYGjQ6KmRwNXVlXNfXl7oIWGUQRVHUlJScCEpKUkYGxuTjaurK7hRBH7aNjc3AUl1Q0MDgfn9/YUF+cVRX19f+IPUyspKYBeSHh8fQ4w2slFWVoZgYPv+/iaYaPH29sYpNFND8kkxIZWaCQnubWxsoIS3tzcosLSqqgrywFlaWgLF2dkZIPEPdra2thRgKsUCG4jL3t7ew8MDAeRaTkUwyFPEN8YyFSzR7+bmhg/yix3gF/b29iyo4M3loPj5+UFMDMvJyUEeJglSpIA7OJScIDhZkpphwogwg1xC/+joKMaenp5SzTZUierh4eHj4yOR7Orqopli0ib5rBlJpGewwAxbPGNUAgICcJIPS0tLEGHEysrKyMgIbYSfnw3yK40k3JgNxEBGAwMD3GZOmEe0ZQYxiR62IKxJHg/3kz/BrwnpYUR4o7y2tranp2dqaqqPj4+ZmRk3mJiYICyOahJONg0NDUkbsP8DL00/zmMjxB8AAAAASUVORK5CYII=)![](/static/57048268f8823dd1ea147faa8e568647/d786d/footer_wechat.png)

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAACXBIWXMAAAsTAAALEwEAmpwYAAAEtUlEQVQ4y01VbUxbZRQ+t1Bm2PicA+0Q2WJM/O0vE5f9848mYIxEcB1Q+knbe/t5u5aWFkrRaGewuFDiNhHovW35LISPwIKDZTJjtE4xkWQON2d0mgyny9iI83rObTU2Obk3773vc5/zPs9zCu2sAO1sAuiqtoyClu65hLKdEyq1NuEwVq3WlqzT2sS63L2gwmfl+E4BFhjsSdDgHk0eIw+GC1YBAqFlBBMOajnhaZ1drNE7xEMGZ7Lc5EyVYpXhfQWuVels4lP0Du4r03EinOwYywMmQEbVWBPQZhYZBFPpkIXBkazocKeKWX68yOWbVvq7M4W+YKbQ6Z1SWvnxfR2u1H4EPohs63BPlcE5Aq1mxCGGassIBLtXiJkKX6gxupIHOM9EUSi8VDA1scncuHYPYkNZZjS5Bdtbv0MikWX8ofkCAjY6k6UyU044hFfQ20QALZeQ2yRmJgSzecaVQ4OfKXbvPwJJksAamAd3eB3CA1ng+y7Ia7/8vAvvnV5TsHy6CEHLZKasUII4QGBK+gq1ScwIjDZRWTqXGT6yBu7e9aP+6EZ5IHoFLP5VeCDdgd3dPYhG1xTEVO9IEsNaFIkhwEoSgM6M2nz44G+YXr0IbdwMnLTMwqstaQXbuWB39yy+4gjNA+ubZPb2UrAn3YWbP/wBp7pmC02u1AEUCgGFEiBrkJokwNTEN0yO3R0wudOM0TWO18ljBmcqrLcPe03uhKrNHAeNZYj5t4uh+KcKizv9GJJ6ErGqCbCWrEFqfre5A9sXJDA4xhidbQSfjVYYHILbzCd9J/Sx4Gtv9jWzgQnYQaCXGwIA4IWVpe8ZzjNZhKQeJ3JApiWf+UOZwuvfPoJnjreD1SMwJrSC0fFRA+sV3vL2zvr4nkygxTgQqW8MPFff2AWN6j5GeijB1c9vgts3pTQ6UhVo/iNACSDTks+uIWDtcQ3wARECfXNwqifzAssPN+vZQZeO+9Bs7xyv9/YuPOuLLIKnZw6kHQm+2LgF5E8SNQ+YMzItbn71G8y0SND1zgoTiq5CJHb5Cf/bS2ozP/yiMzhzLNx/+Y3+s5ulp+NZiLx/RT7DhbkthtxBOuRbFlQUJ5JfSHwpHzb9PN3TjDc8B85A+iVX10TQG1kMYT0fjF6E4Lur/4kyMHAJRUmRKCq0ThXZppyySXGiBNxG0/4l3YPX1f3QpO6BXdxksp+1WD1ik70zDb7wLH6uQQb7Ovsrw/szhWjuEiRGidkPGpwaZGzKJrGkBNxH09IGte4DRtNxBlpNscPtlnglFjRr4/Kzn279Cb2RFdkyertYjRg1Tdx5Soo8duT4UDYpTpSAG9fv5tLCnwNNRwx0liFwBQV57Wr2NkNgVnd6n8EpohjCEcQolqcNzTNsmVqvIqaUTWLqxQTE4xuKS5/8yJwZXGLOnV9nVpe3mRieGbVJzGQwTp44FVqcNDQg5DlG88zo/BjkqYFMSTGKE20i05LPyAWkJglAZya3ScwIjBvDc05AK5sHpGoxi/IXaGpQ0MlOFCdKAJmWrEUfktVEAejMsMViYkZgbTKOkB+w+dLbksSSioYtKVed+xsQj5Jp5Xs8GlLzhD03obU4sdv+h/EPsbi7Iqfeg68AAAAASUVORK5CYII=)![](/static/1b87ba5dd8a4dda4d8d17e472bd9cefb/002c1/footer_ethereum.png)

订阅

[ ](https://twitter.com/EthereumCN)[ ](https://discord.gg/KUywx3JJJU)[
](https://i.ibb.co/mBgmDgF/footer-wechat.webp)[
](https://github.com/EthereumCN)[ ](Mailto:eth@ecn.co)[
](https://www.ethereum.cn/rss.xml)

[ 蜀ICP备2021001286号 ](https://beian.miit.gov.cn/)

