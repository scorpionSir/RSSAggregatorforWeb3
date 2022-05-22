[![logo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAICAYAAAD5nd/tAAAACXBIWXMAAA7DAAAOwwHHb6hkAAABj0lEQVQoz12Sv0vDQBTHT0HrD4QWRJRLi3QQOojon1JxUhcFQQeViknrJjiIglgRhW4OTiLSWXB10MnJoToI0lp6ESu1TZNc/L7LFcGDD+8u4X3y3r0wKeUUeAqwEBVYZa9amhCb0bydjbdti/vAsy0jALPYp0EZSODq91W8W2AQPGqZg9CUvkvGUv08fSEywwGESDIaoAW+QQHJbWEq+Y+mqc8OCV3wASZBzP+qJJ8ZY2JrpKgqMvk8Yh8kvL6b6sZ+WZicki/BIBgFUVCk5ywsTr4ikvxI+l4F+w20e21bcQiNGUiZ2OZdSGLYr+jW9+hcw3NUx/DBY6pSCcELZCQ8RMtvOK+K9aErO5ugCqdJCDESVVzSwgMSQhLRwjMl1C1Xw+H4Mf/zPQFhxN5J3qrEbGJRmGMDwjIMYfF+yDNauK+FvVp4qlqG6F4PpY3goMIWxebdiVdbi1CiDC+dtwBdfmcA+X/CQqflFGQP6nf5+20C6blB4yYnRW7chcihCYbwFk0ZzAES9eiIq+DiFyR9m3ZUxiupAAAAAElFTkSuQmCC)![logo](/static/9c635c914229a850d1a9fd284014bdd0/65e33/eco_logo.png)](/)

  * [新闻资讯](/)

  *   * [零时学院](/c0llege)

  * [开发者门户](/develop)

  * [生态漫游](/ecos)

Ξ

Search by [](https://www.algolia.com/?utm_source=react-
instantsearch&utm_medium=website&utm_content=&utm_campaign=poweredby)

## Eth1.x 研究进展速览

Eth1.x 研究新方向重点是将当前的以太坊链转移到“无状态客户端”。

* * *

GI

Griffin Ichiba Hotchkiss 2019-12-12

来源 | [Ethereum Blog](https://blog.ethereum.org/2019/12/10/eth1x-files-fast-
sync/)

本文转载自[unitimes.pro](http://www.unitimes.pro/p/4c5071804cb245478f56bf200efe2dec)

  

![1.x封面.png](https://i.ibb.co/7gcsNnN/1-x-0d3dc30bff.png)

  

[Eth1.x 研究的新方向](https://medium.com/@pipermerriam/stateless-clients-a-new-
direction-for-
ethereum-1-x-e70d30dc27aa)已经开始了，重点是将当前的以太坊链转移到“无状态客户端”范式，最终目标是顺利过渡成为 Eth 2.0
中的一个执行环境 (Executive Environment)。

下一次电话会议将集中在收集和组织研究主题和规划一个更结构化的相关路线图。此电话会议是开放的，任何人都可以参加，预定在12月17日下午16:00。如果你想加入，请在
[ethresear.ch](https://ethresear.ch/t/eth1-x-call-2-tuesday-dec-17th-next-
steps-and-collecting-research-topics/6512)论坛上直接发信息给 Piper Merriam 或 James
Hancock。

本文是对我们做过的所有努力的回顾。对那些最近加入以太坊社区，并且错过了 Eth1.x 讨论，或是想要稍微回顾一下的人而言，可能会有所帮助。本着
“–sync-mode=fast” 的精神，我们将在本文中谈及大部分的历史研究主题，并将对无状态客户端和当前研究的深入讲解留到后续文章中讨论。

首先，我们的核心开发者们意识到，以太坊路线图的最后阶段——“Serenity”，不会如最初设想的一样，那么早就准备继续。一个完全的 “Eth2.0”
的诞生，可能需要数年时间。我们需要对目前的 Eth1.0
链做出改进，以确保在一个完全的协议升级实现之前，不会出现导致以太坊无法运行的更大问题。因此，“Eth1.x”——对当前 “Eth (1.0)”
进行的更小的、 递进的升级所做的研究——应时而生，其目标是额外延长当前以太坊链的寿命至少3-5年，直到一个更为重大的 Serenity (Eth2.0)
升级的到来。

  

# **当前以太坊区块链有什么问题？**

问题很复杂。它不似一个安全漏洞或一个重大设计缺陷，原因是 Eth1.0
并不存在某个亟待解决的问题，可以让我们投入专门的资源进行解决。同样地，如果完全不对当前的链进行更改，那也不太可能会出现导致以太坊网络停止运行或是“着火” 🔥

然而，可能给当前以太坊网络带来灾难性情况的是，随着链状态的自然增长，其结果是对网络的性能带来细微的衰退和网络健康的损害。倘若不进行 Eth1.x
的工作，长此以往，以太坊将会面临风险。随着越来越难运行全节点，这一网络可能会变得越来越中心化；随着网络延迟的增加，它的速度可能会越来越慢；随着“状态膨胀”的出现，区块验证可能变得越发困难。
**最终，随着交易吞吐量达到上限，且客户端改进越来越难以实现，终端用户与核心开发者都将非常受挫。**

我们的目标是避免以太坊遭遇一场千刀万剐的局面，即便这场局面需要好几年才会到来，但那时即便是开始立即采取措施也是为时已晚了，因此早在布拉格 Devcon4
期间就已经开始有关 Eth1.x 的讨论 (🦄>💀)。

广义地说，我们面临的问题是一个非常根本而明显的显示： **以太坊区块链正变得越来越大** ，但其中有一些细微的差别，当我们讨论“区块链的大小” (the
size of the blockchain)
的时候，我们实际上是真的在讨论一些不同的子组件的大小，且更重要的是关于这些组件的大小会如何影响整个网络的性能。这些子组件包括：

  

## **01\. 链的存储需求**

“如果有人提到‘区块链的存储成本’”，只需跟他们说说 Amazon Black Friday 的网页：8TB
的存储需要花费125美元。区块链面临着一些真正的问题，但存储的成本并不是其中之一。”——Emin Gün Sirer
([@el33th4xor](https://twitter.com/el33th4xor/status/1200477778463907841))

在一个全节点成为以太坊的“头等公民”之前，它必须同步以太坊区块链的整个历史记录。历史记录的时间越长，要存储的数据就越多。目前，对于一个“标准的”
Parity 或者 Geth 全节点来说，其存储需求约为219GB，并且每月增长10-15GB。

从绝对的存储成本的角度来看，这还不算太糟糕。完全地在消费类硬件上运行一直都是以太坊的愿景
(存档节点除外，因为存档节点需要大约3.5TB的存储)，低于500GB的消费类硬件就在一个合理的阈值范围内，因此运行一个全节点将在今后的几年内并非遥不可及。

但更强有力的论据来源于启动新的全节点的 **边际成本：存储需求和同步时间的增加会导致全节点的减少，而这将进一步导致同步时间的增加和节点数量的减少。**

这样的结果是，随着时间的推移，开发者们将越来越依赖 Infura
等服务，而“真正的”区块链将越来越多地受困于云端，令普通爱好者、研究人员与业余开发者们无法触及。

  

## **02\. 区块大小与交易吞吐量**

增长的另一个方面是 **单个区块大小的增长及其与整个网络交易吞吐量的关系** 。与比特币不同，以太坊不会明确地按内存限制每个区块的大小，而是通过燃料限制
(gas limit) 强制规定区块大小。以太坊的 Gas 限制有效地限制了可以包含在一个区块中的交易量。这个 Gas
限制并由矿工集体决定，即通过投票的方式来动态地增加或降低 Gas 限制。最近，矿工们集体同意将以太坊的区块 Gas 限制提高至约1,000万个 Gas
单位，使每个区块比1月18日以来的大小增加了25%左右，这从理论上提高了系统的交易吞吐量。

区块 Gas 限制与矿工就新区块达成共识的能力之间存在制衡。 **从理论上讲，更高的 Gas 限制会增加区块的叔块率**
(叔块不能迅速传播给其他矿工，因此叔块是无法被大多数矿工接受的有效区块)。我们需要搜集更多有关“安全的”区块大小上限是多少的数据，但人们普遍认为，提高
Gas 限制带来的吞吐量提升不足以在未来 5 年内实现以太坊的发展。此外，更大的区块还会加剧链存储需求问题。

  

## **03\. 状态大小与网络性能**

以太坊是一台[随着区块数量的增加而向前移动的状态机](https://medium.com/@preethikasireddy/how-does-
ethereum-work-anyway-22d1df506369)。在任何给定时刻，以太坊的完整“状态”都包括 EVM
中部署和运行的所有智能合约的集体存储，以及所有帐户和余额的当前状态。当交易被添加到一个区块时，它们通过更改帐户余额、部署新的智能合约代码或让智能合约执行自己的某些代码来更改以太坊的状态。

当前以太坊的状态大小大约是10GB。按理说，状态会随着网络上的总交易量的增长而按比例增长。因此，如果我们期望以太坊继续获得主流采纳，那么这个数字在未来几年可能会出现巨大增长。

较大的状态会影响所有客户端的两个主要性能点：

  * 客户端读取状态的速度将受到限制，因此交易处理速度会变慢。处理一笔交易需要读取存储在客户端数据库中状态的相关部分。状态越大，查找交易所需的时间就越长。更重要的是，在使用 trie 结构来表示状态的客户端 (比如 Parity、Geth 和 Trinity) 中，这种减速的情况会因为底层数据库的查找 (其中实现了 trie 结构) 而变得更加严重。

  * 由于需要通过更改状态来构建新的状态，较大的状态将意味着区块的验证速度将更慢。与上述推理路线相同，当验证一个新区块时，客户端必须对状态的更改进行重新计算；这涉及到了搭建一个新的状态 trie 结构和计算新的根哈希 (root hash)。从计算的角度来说，构建一个新的状态 trie 结构要比简单地查找需要更多的计算，因此与处理单笔交易相比，状态的增长对这一操作的影响更大。

基于状态驱动的性能下降是最令人担忧的。以太坊是点对点网络，这意味着细微的变化可能会对网络运行状况产生连锁反应。此外，状态的存储与更改是让客户端开发者团队更头疼的事情之一。编写和维护客户端已经够难了，而状态增长则进一步加剧了这一负担。随着状态的增长，客户的多样性和性能将会下降，这对每个人都不利。

  

# **潜在的解决方案是什么？**

从 Devcon4 布拉格时的启动会议开始，一直持续到2019年，很多核心开发人员、贡献者和魔法师们聚集在一起，讨论如何延长 Eth1.0链
的生命。以下是讨论过的最重要的提议及相关的内容：

  

## **01\. 适度的优化和缓解**

更为激进的删减。管理存储需求的一种方法是主动删除不再需要的部分，比如交易收据、日志和较早的历史区块。可以就全节点保存历史数据的期限达成共识
(比如3-9个月)，过期后删除，从而能够有效地降低运行节点所需的总存储。Péter Szilágyi
已经就链删减对于Eth1.0链的长期存活性进行了[全面的概述](https://gist.github.com/karalabe/60be7bef184c8ec286fc7ee2b35b0b5b#decentralized-
archives)。概况起来就是，这种方式存在一些权衡，且其中一个未解决的需求是历史数据需要 (在某个地方)
可以获取，且取代了链存储所有历史记录就意味着节点必须保留被删减部分的证明 (proofs)。

区块提前公布 &
状态缓存。这与减轻网络延迟带来的影响有关。提前发布区块，其中的想法是在区块被验证之前，矿工提前将该区块公布出去，这将使监听客户端有机会去猜测哪部分状态将受影响，并为下个状态对这些缓存进行预先警告。同样地，客户端可以在内存中保存部分状态，这样在同步状态失败时就不必从头开始。这些优化目前是可以实现的，且
turbo-geth 已经使用了这类优化的一些变体形式来提高性能。

  

## **02\. 通过大型硬分叉进行改变**

操作码重新定价 & ETH
锁定。通常，这意味着简单地调整操作码的成本以阻止状态的进一步增长。从广义上讲，这意味着增加导致状态增长的操作的成本，和/或增加带来状态缩减的操作的奖励。但退款的方式有些棘手，因为退款一定是来自于包含在交易中的
Gas，这意味着那些仅清除内存或销毁合约的交易实际上不能按比例地获得退款。为了使交易在 Gas
方面的收入比支出更多，有可能要求合约在部署时锁定一定数量的、足以支付那些退款的 ETH。

状态租金和‘收回’。比上述重新定价操作码的方式更引人注目的是，状态租金 (state rent)
的方式通过要求合约按其占用的状态大小来成比例地支付一笔经常性费用。在支付这笔费用之前，合约将被删除或中止。对于智能合约和 Dapp
开发者来说，这种方式将是一个重大的变化，且这将需要不止一次硬分叉来实现。这种方式迄今仍是 Eth1.x
领域中讨论最广泛的提议，也是最受争议的提议。因此，关于 Eth1.0 链的状态租赁的研究已经暂停了。

  

# 圣杯：✨无状态客户端✨

如果状态的大小对网络的健康带来重大的问题，那么终极方案将是完全消除对状态的需求。简而言之，无状态客户端 (stateless client) 使用区块见证
(block witness)
来证明某个特定的状态更改相对于前一个状态的有效性。也就是说，客户端将只会计算新区块的状态更改，然后证明这些状态更改与前一个状态是一致的，而不会计算每个新区块的完整状态。

矿工和一些全节点将依旧需要保存完整的状态副本，这样才能从中生成区块见证。虽然对于客户端来说，在整个网络中传播区块见证会带来一些新的挑战，但这种方式的潜在益处是非常巨大的。

[无状态客户端的概念](https://ethresear.ch/t/the-stateless-client-concept/172)是最先由
Vitalik在探索 Sharding (分片) 的情况下提出来的，但之后在围绕 Eth1.x 的讨论中也被探讨。起初这种方式被认为太过复杂，但最近，随着
[Trinity 的 bean sync](https://medium.com/@jason.carver/intro-to-beam-
sync-a0fd168be14a) 方式展现了 semi-statelessness (半无状态性)
对于轻客户端的可行性，无状态客户端的概念获得了很多支持。

重要的是，转向无状态或半无状态范式对现有 Eth1.0
网络的破坏要小于状态租金之类的方式，因为这种方式不会对现有客户端带来重大的更改。有状态节点和无状态轻客户端可以同时共存，且 semi-stateless
(半无状态) 的以太坊将为试验不同的客户端实现提供了更多的机遇。同时， **Eth2.0 中的分片 (shards)
几乎可以肯定会是无状态的，因此当时机成熟时，这将为 Eth1.0 最终向 Serenity 过渡开辟出一条新的道路。**

我们将在另一篇文章中更深入地探讨无状态客户端。如果你已经读到此处了，你现在就赶上了 Eth1.x 研究的当前状态，并且能够跟随和加入相关的新进展！通过
ethresear.ch 加入我们吧，或者继续关注基金会发布的有关 Eth1.x 的更新文章。

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

