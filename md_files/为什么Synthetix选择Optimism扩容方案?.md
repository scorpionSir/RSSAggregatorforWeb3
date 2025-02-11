[![logo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAICAYAAAD5nd/tAAAACXBIWXMAAA7DAAAOwwHHb6hkAAABj0lEQVQoz12Sv0vDQBTHT0HrD4QWRJRLi3QQOojon1JxUhcFQQeViknrJjiIglgRhW4OTiLSWXB10MnJoToI0lp6ESu1TZNc/L7LFcGDD+8u4X3y3r0wKeUUeAqwEBVYZa9amhCb0bydjbdti/vAsy0jALPYp0EZSODq91W8W2AQPGqZg9CUvkvGUv08fSEywwGESDIaoAW+QQHJbWEq+Y+mqc8OCV3wASZBzP+qJJ8ZY2JrpKgqMvk8Yh8kvL6b6sZ+WZicki/BIBgFUVCk5ywsTr4ikvxI+l4F+w20e21bcQiNGUiZ2OZdSGLYr+jW9+hcw3NUx/DBY6pSCcELZCQ8RMtvOK+K9aErO5ugCqdJCDESVVzSwgMSQhLRwjMl1C1Xw+H4Mf/zPQFhxN5J3qrEbGJRmGMDwjIMYfF+yDNauK+FvVp4qlqG6F4PpY3goMIWxebdiVdbi1CiDC+dtwBdfmcA+X/CQqflFGQP6nf5+20C6blB4yYnRW7chcihCYbwFk0ZzAES9eiIq+DiFyR9m3ZUxiupAAAAAElFTkSuQmCC)![logo](/static/9c635c914229a850d1a9fd284014bdd0/65e33/eco_logo.png)](/)

  * [新闻资讯](/)

  *   * [零时学院](/c0llege)

  * [开发者门户](/develop)

  * [生态漫游](/ecos)

Ξ

Search by [](https://www.algolia.com/?utm_source=react-
instantsearch&utm_medium=website&utm_content=&utm_campaign=poweredby)

## 为什么Synthetix选择Optimism扩容方案?

Synthetix创始人详析选择Optimism的原因、为社区释虑、并提出执行计划。

* * *

KW

Kain Warwick 2020-10-26

来源 | [blog.synthetix.io](https://blog.synthetix.io/why-optimism/)

  

![](https://i.ibb.co/dLzJPbB/Why-Optimism.png)

Defi的兴起发出了一个清晰的信号：以太坊需要在ETH2.0之前实现扩容，但要在DeFi生态内保持可组合性还需要在同一个扩容方案上协调。

幸好，市场是非常擅长预测和解决这样的困难的，我们现在已经有非常多的扩容技术上线了。我们与多个主要扩容技术变体的团队进行了对话，且经过对它们逐一评估，我相信Optimistic
Ethereum是在社区里最可能达成共识的扩容方案。

这篇文章会详述我为何如此相信，且社区里对上线Optimistic
Ethereum的忧虑，我也将进行回应。它还将给出在主网实现OVM的Synthetix变体所需的治理过程设计，以及说明何种情况下另一种扩容技术可以替代Optimistic
Ethereum。本文旨在确保就Synthetix迁移到Optimistic Ethereum，社区成员能有达成共识所需的信息。

[如果你还未阅读Vitalik的文章《以rollup为中心的以太坊路线图》（[ **A rollup-centric ethereum
roadmap**](https://ethereum-magicians.org/t/a-rollup-centric-ethereum-
roadmap/4698/2)），本文是围绕它的论述展开的，但Vitalik的是自顶向下的，而我这篇是自底而上的，着眼于DeFi项目需要扩展什么，以及为什么Optimistic
Ethereum能满足这些要求。]

###  

# 社会共识

我感觉“不停做出权衡取舍”好像变成了我的新口头禅。但它是对的——完美的扩容解决方案是不存在的。每种方法都有其重要的权衡，而每种扩容技术的具体实现又有进一步的低层次权衡。所有这些都以一个高风险的元协作机制为基础，因为光是选择正确的设计和权衡是不够的，我们还必须对其他人最有可能选择的方案进行优化。因此，扩展变成不只是一个技术上的难题，它还是一个社会协作博弈。

当我第一次阅读关于Optimistic
Rollups的内容时，当时我们的gas费还没有很高。无论是对于技术还是社会上的难题，它看上去都像是个优雅的解决方案，但我已经意识到，无论我们选择哪种扩容方案，我们都需要与其他项目合作。Uniswap的Unipig演示给了Optimism收获社区共识一个很好的机会，因为它与以太坊上最知名的项目之一合作了。因此，我选择参与这个解决方案，不仅在如何解决DeFi特有的困难上给Optimism提供反馈，还协助他们在社区里引导社会协作。

![](https://i.ibb.co/gj5jgVV/why-optimism2.png)

###  

# 技术因素

对于Synthetix来说，Justin
Moses既是它的幸运也是它的诅咒。他为Synthetix树立了不轻易妥协的、严谨的工程文化，但他对认知负载的讨厌程度是在软体动物界外少见的。这意味着，把Synthetix部署到Layer2上需要在最小化风险与减少对代码库的任何修改之间达成微妙的平衡。迁移期间在Layer1和Layer2上运行两个并行的、不同的代码库，这种做法我们是绝不会同意的，因为迁移甚至都不会实现；而如果这意味着用另一种语言重写合约的话，就更加不可能发生了。

Synthetix是建在Ethereum上最复杂的智能合约之一，这无疑增加了维持不同代码库的难度。这是我们在将Havven
network移植到EOS.[https://twitter.com/kaiynne/status/1166234541616316417?s=21的失败尝试中首先发现的。](https://twitter.com/kaiynne/status/1166234541616316417?s=21%E7%9A%84%E5%A4%B1%E8%B4%A5%E5%B0%9D%E8%AF%95%E4%B8%AD%E9%A6%96%E5%85%88%E5%8F%91%E7%8E%B0%E7%9A%84%E3%80%82)

我们还需要向社区证明这项技术是可行的，且是值得我们进一步投放资源的，然后再尝试围绕它作为我们的扩容方案构建共识，OVM的交易演示也有助于加强这点。但仍有社区成员对这个方法保有忧虑也是在理的，因此即使社区共识已经非常明显偏向Optimistic
Ethereum，我们还没到可以用SIP来测试它的地步。

但在我开始讨论具体的权衡之前，我想对用于执行智能合约的、现有的扩容方向提供概述：

  1. 快速区块链，即“以太坊杀手”，其他Layer 1架构，非常快速的区块链

  2. ETH 2.0，即2032年见 (开个玩笑)

  3. 状态/支付通道，即“都能发送代币了，你还想要啥？”

  4. 侧链，即xDAI那一套

  5. Plasma，以Omisego为代表，也叫“虽迟但到”

  6. 使用零知识的ZKrollup和其他解决方案，即你是否solidity的真爱。

  7. Optimistic EthereumOptimistic Rollup，高能预警

  8. Lightning，笑而不语

如果还有其他解决方案是我漏了的，我很抱歉，我非常期待在twitter上看到它们的消息。

由于在迁移阶段需要保持使用同一个代码库，上述的大部分解决方案都被排除了。当然，很多解决方案都声称与EVM兼容，但这并非听上去这般简单——虽然Optimism突破了这个限制，也还需要对合约进行少量修改。但基于这点我们可以很快排除这些方案：快速区块链、ZKrollups、Lightning、状态通道、和Plasma。即使ZKrollup取得快速进展，目前的所有变体都需要用一种新语言来重写合约。这并不是不可克服的，只是这些语言的工具还非常不成熟，这会大大增加实现风险。

可能会有一些快速区块链支持者读这篇文章时会情绪激动，的确其中有些项目是与EVM兼容的，允许solidity合约在上面部署，但它们大多数有其他问题，使我们感觉会削弱它们的可行性。包括那些十分新颖的共识机制也还没经过反复测试来证明其可行性，或安全性大打折扣。

目前来说，普适性计算是状态/支付通道和Plasma第二个难以达到的要求。

那就只剩下侧链和Optimistic
Rollup了。我们排除了像xDAI这样的侧链，因为我们需要为价值上亿美元的资产提供保障，在未来还会再增加几个数量级。如果有异议，feel free to
掰头 with me

看完了全部的选项后，我们觉得Optimistic Ethereum呈现的权衡是最佳的，而且他们团队也非常有能力执行他们的路线图。

###  

# 分阶段的Optimism

很明显Optimistic
Ethereum还没有上线，因此还存在重大的执行风险，这也是为什么我还没提交关闭Layer1上的Synthetix的SIP。但是，在上述的选项中，结合权衡与风险来看，我们认为Optimism证明了它不仅值得Synthetix投入大量工作做迁移，还要带动DeFi的其他项目一起参与。这就是为什么我决定我们需要利用我们作为最老牌的DeFi协议之一的地位并承担早期实现的风险。我知道这会有利于在社区建立共识。到目前为止，社区的普遍接受程度很高，且还没有人反对给Optimistic
Ethereum分配资源。

但是，随着我们越来越接近可能的主网迁移，我们提出了三大忧虑。

1）欺诈证明

2）中心化

3）提款延迟

最关键的技术问题是欺诈状态转变。有人说目前的实现阶段不包含欺诈证明，实际上，欺诈证明是包含在内的，但尚不支持自动生成的欺诈提交。Optimism团队选择了分阶段顺序的方法，以便在增加复杂性之前测试像储存与提款这样的特定功能。但是，这一点可以在测试网路线图里就声明，以避免用户疑惑。尽管在主网上线之前，自动提交欺诈证明这项功能就会上线。在欺诈证明功能不完备

的情况下，很明显是不会有主网上的资金可以存进Optimistic
Ethereum网络的。对于任何提议迁移到一个低安全保障网络的SIP，我个人是会投反对票的，我也鼓励社区里的每个人都这样做。这也是为什么xDAI和其他POA
(权威证明) 网络被认为不可用的原因之一，即安全性低。

另一个主要忧虑是Optimistic
Ethereum呈现出来是去中心化的，但它有中心化的部分。我相信这个看法是被误导的，但它当然是有道理的。在过去几年，社区为提高协议的去中心化程度投入了大量的时间和资源，现在如果为了gas费和吞吐量而往后退，会是个糟糕的取舍。但事情不是这样的，排序者
(sequencer) 是在最少牺牲的前提下大幅提高用户体验的。

这些忧虑源自人们对Optimistic Ethereum网络中排序者的误解。大家需要知道排序者并不是必须访问Optimistic
Ethereum的，它的存在是为了提高用户体验的。很多人还以为一个排序者意味着一个单点故障，这样的情况很不理想，但其实这种故障在L1的糟糕UX里早就存在了。当然，退回到Layer1的区块时间并不理想，但还有很多潜在的解决方案，包括如果活跃排序者出故障或被攻击，后备排序者可以替补上。所有这些忧虑都只是暂时的，因为目标始终是尽快转移到一个有排序者的网络里。

最后一个主要忧虑是提款延迟对跨层可组合性的影响——这个忧虑除了其他Layer1架构，其他所有扩容方案都会面临。这些延迟意味着在挑战期，资金都会锁在Layer2的网络，但还是有几种可变通的处理方法的。一种是搭建一个验证者网络，为桥的两边提供资金，并承担提供及时提款的风险以赚取费用。实际上，Connext已经开始往这方面开展工作了，这里有更多的细节。这并不能彻底解决可组合性问题，因为资金仍然需要在另一笔交易得以启动之前在主网上得到确认，但这基本上对所有扩容方案来说都是至关重要的，我们无法逃避。这也是为什么我认为所有的主要DeFi协议都应该尽早在Optimistic
Ethereum上上线它们的并行版本。这会使得几乎所有目前的DeFi交易都在Layer2上发生。很有可能质押会完全迁移到Layer2，而交易合约将继续在Layer1和Layer2上平行运行。

需要明确的是，在“开始Optimistic
Ethereum主网迁移”的SIP被提出之前，关于功能完备的主网的所有信息都需要公开。我个人有信心，这个条件在未来数月内会得到满足。

###  

# 主网迁移后

关于Synthetix该如何迁移到Optimistic
Ethereum仍然需要在社区内进行辩论。首先，我们必须在是否需要有一个并行且有限版本的网络在Layer2主网里发布这个问题上达成共识。一旦我们在此达成了共识，我们需要评估此次主网发布的结果并对迁移的其他部分进行形式化。

尽管Synthetix的DAO很可能在主网迁移后的前几周提供资金，但我们将需要一份SIP提议把最终协议奖励的1%分给Optimistic
Ethereum。如果我们将部分的协议奖励分给这个并行网络，我们可以监测采纳情况和使得市场可以对迁移风险进行定价。预计收益会因为下降的gas费而比在Optimistic
Ethereum低，但也有可能平台风险会导致更高的收益，因为大多数的SNX持有者会选择晚点迁移。

我的看法是通过抵押Optimistic
Ethereum上的SNX铸造sUSD与当前通过抵押托管的SNX铸造sUSD差别不大。我们决定允许通过托管的SNX来铸造sUSD以最大化可用抵押品的价值。对于那些已经迁移到Layer2的SNX，如果想将它们迁回到某个点，这是可以实现的，这意味着这些SNX在网络里都会被视为有效抵押品，只是与在Layer1上的SNX状态不同。因此，在Layer2铸造的sUSD与Layer1上的sUSD应该是可以互相置换的。对此当然有反对声音，理由包括这个实现会是非常复杂的。我们必须采用对整个社区来说最合理的方法。

如果此次的迁移是有效的，我们就会有一个相当有力的杠杆可以影响其他部分的迁移：只需要继续转移更大比例的通胀奖励，直到全部都发送到Layer2以及所有活跃的、质押的SNX都发生在Layer2上。到时我们当然需要支持在Layer1和Layer2上Synth的兑换。因此，在这个过程里有大量相互关联的依赖关系需要处理。

我曾公开表示我相信Optimistic
Ethereum将是现在与Eth2.0上线之间DeFi的出路。如果Synthetix社区的其他人都如此相信，我们需要计划如何加入这个网络并完全从Layer1迁移过去。我们当然应该谨慎为之，但Synthetix的勇士们从未在没十足把握的对赌中退缩过，我相信这是我们遇到的最大挑战之一。

为了执行这项工作，我们将需要一系列SIP和SCCP，列明每次发布里提议的变化以及背后的理由。这将确保最大限度的透明度以及得到所有持币者的同意。

###  

# 后备方案

一般而言，以太坊扩容方案以及智能合约平台的竞争是动辄上几十亿美元的事业。在这个高风险游戏里，有非常多的竞争团队，因此尽管我们对Optimism有信心，还是可能有其他团队推出比他们优秀的方案。如果真的发生这种情况，我们必须做好将我们的工作中心转移到这项更有竞争力的技术的准备，特别是如果我们发现多个DeFi项目已取得了社会共识，决定从Optimistic
Ethereum转到另一个方案。

我们必须为最差的情况做准备，即Optimistic
Ethereum的发布失败了或中止了。在这种情况下，我们必须快速将资源转移到认真调研其他解决方案上，同时还要优化现存的Layer1系统。实际上，我们已经开始了应对紧急情况的准备工作。债务快照
(debt snapshot)
那份SIP的快速实现就是一个优化的例子，这个优化已经被搁置了很多个月，但为了解决在Layer1上迫切的gas问题，我们加快了这个实现。庆幸的是，我们得到了暂时的缓和，但它不能持续很久。如果因为任何原因我们无法就迁移到Optimistic
Ethereum达成共识，我认为我们社区必须聚集起来一起选出另一个扩容方案，并团结起来推进它。虽然我认为可能性不大，但假装这是不可能的就过于轻率了。

###  

# 结论

本文旨在解答一些社区提出的问题，但同时希望可以解释在整个迁移过程中，我们是如何走到现在的，以及现在是处于什么阶段。没有什么是不可更改的，即使是一份已通过且实现了的SIP也可能因为情况改变而回滚。但是，我坚信如果我们就SIP达成了共识，并希望为DeFi扩容构建一个最可行的网络，整个社区都需要尽力推进它。我有信心我们的社区可以实现这点，我们比任何时候都更强大，并对2021充满期待，其中当然包括Synthetix得以在一个功能齐全的Optimistic
Ethereum主网上运行。

  
  

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

