[![logo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAICAYAAAD5nd/tAAAACXBIWXMAAA7DAAAOwwHHb6hkAAABj0lEQVQoz12Sv0vDQBTHT0HrD4QWRJRLi3QQOojon1JxUhcFQQeViknrJjiIglgRhW4OTiLSWXB10MnJoToI0lp6ESu1TZNc/L7LFcGDD+8u4X3y3r0wKeUUeAqwEBVYZa9amhCb0bydjbdti/vAsy0jALPYp0EZSODq91W8W2AQPGqZg9CUvkvGUv08fSEywwGESDIaoAW+QQHJbWEq+Y+mqc8OCV3wASZBzP+qJJ8ZY2JrpKgqMvk8Yh8kvL6b6sZ+WZicki/BIBgFUVCk5ywsTr4ikvxI+l4F+w20e21bcQiNGUiZ2OZdSGLYr+jW9+hcw3NUx/DBY6pSCcELZCQ8RMtvOK+K9aErO5ugCqdJCDESVVzSwgMSQhLRwjMl1C1Xw+H4Mf/zPQFhxN5J3qrEbGJRmGMDwjIMYfF+yDNauK+FvVp4qlqG6F4PpY3goMIWxebdiVdbi1CiDC+dtwBdfmcA+X/CQqflFGQP6nf5+20C6blB4yYnRW7chcihCYbwFk0ZzAES9eiIq+DiFyR9m3ZUxiupAAAAAElFTkSuQmCC)![logo](/static/9c635c914229a850d1a9fd284014bdd0/65e33/eco_logo.png)](/)

  * [新闻资讯](/)

  *   * [零时学院](/c0llege)

  * [开发者门户](/develop)

  * [生态漫游](/ecos)

Ξ

Search by [](https://www.algolia.com/?utm_source=react-
instantsearch&utm_medium=website&utm_content=&utm_campaign=poweredby)

## Eth 1.x：无状态以太坊路线图更新

巴黎Eth1.x峰会之后，无状态以太坊路线图有所更新。

* * *

GI

Griffin Ichiba Hotchkiss 2020-04-03

来源 | [Ethereum Blog](https://blog.ethereum.org/2020/04/02/eth1x-stateless-
tech-tree/)

  

![1.x封面.png](https://i.ibb.co/7gcsNnN/1-x-0d3dc30bff.png)

  

很抱歉这篇文章发布得晚了些。最近，我的生活中不可避免地出现了一些干扰，读者朋友应该也有类似的经历。我祝愿大家能排除万难，也恳请大家在接下来的几个月中保留最大程度的同理心，尽己所能援助社区中面临危难的同伴。

话虽如此，还是让我们进入无状态以太坊主题，谈谈技术树的变动。

单从图形上来看，这棵树已被完全重塑，但如果将其与[原始版本](https://news.ethereum.cn/eth1x-files-the-
stateless-ethereum-tech-
tree/)进行比较，则会注意到很多内容其实是相同的。为了保证内容完整性并避免混淆，虽然之前已经作过解释，但我们仍然会仔细过一遍图中的所有内容。以下是更新之后的无状态技术树：

![1.x14.png](https://i.ibb.co/yQwvFTb/1-x14-a1022e51ef.png)

粉色的每个主要里程碑代表一个大致类别，必须在进行下一步之前“解决”。此处有意进行了模糊化处理，不代表特定EIP或集成功能，尽管其中一些主题最终可能会归于这类形式。

较小的紫色元素则是更具体的从属部分，是“解锁”主要里程碑的必需条件。紫色元素虽然是必需的，但并不一定需要被接受或实现。例如，经过充分研究我们可能会发现代码分块
(code merkleization)
并不能充分缩减见证的大小，实现效果或许并不匹配我们所投入的工作量；然后我们可以将其视为“已完成”，因为不会再做进一步研究。

大家可能已经猜到了，绿色的项目是“支线任务”(side
quests)，从理论上来看可能对无状态以太坊有所帮助，但不能过多占用研究人员有限的时间和精力。在以太坊工作进程中，可能还会出现更多的支线，有需要的话我会继续更新科技树。

此外，黄色元素属于工具类。这些尚未创建的软件工具将有助于验证假设、测试实现并且提高工作效率。理想情况下，这些工具的质量要足够高，并且要得到合理的维护，才足以支持无状态以太坊之外的更大的开发者生态系统。

  

# 同步协议替代方案

巴黎Eth1x峰会的重要共识之一是同步将成为无状态以太坊的首个里程碑。我们必须使得新节点无需依赖网络原语GetNodeData即可获取当前状态树。除非我们找到该原语的可靠替代项（beam
sync和fast sync均基于此），否则将成为无状态工作的阻碍，甚至可能会起反作用。

这里有必要稍微解释一下为什么会出现这种问题。如果不具备以太坊状态的基础认识，建议阅读本系列的[另一篇同主题文章](https://news.ethereum.cn/eth1x-files-
state-of-stateless-ethereum/)。

让我们先了解一下术语。在此处的语境中，“网络原语”(network primitive)
一词并没有特殊的技术性定义，只是对“以太坊网络通信的基本语法”的一种流行叫法。想象一个客户端问道“哈希为0xfoo的节点的数据是什么？”那么节点可以回答说“是0xbeef”。

在大多数情况下，其响应将额外包含状态树中子节点哈希，因为之后可能会以同样的方式对子节点进行询问。这种游戏将一直持续到请求者满意为止，通常会分别请求当前状态树中的约4亿个节点。

即使按照这种方式，也可以迅速进行同步，毕竟客户端可以执行多任务，并且可以同时向多个全节点请求状态的不同部分。

然而，原语的工作方式存在一个根本问题：“获取方”(leechers) 必须按照自己的条件进行，而他们只能从“资源方”(seeders,
即具备完整状态的全节点) 处获得所需的状态。

目前的运行方式就是基于这种不对称关系，但由于两个关联条件，网络仍然可以正常运行：首先，有足够的全节点根据请求主动提供状态。其次，任何请求状态的节点最终都会成为全节点，因此对于状态的需求是自限性的
(self-limiting)。

现在我们就明白了为什么无状态以太坊会出现状态同步问题：在无状态范例中，不保留请求到的状态数据的节点，会无限地请求数据。如果运行无状态节点比全节点要轻松许多（确实如此），那么会出现无状态节点增长速度快于全节点的局面，最终导致状态无法在网络中正常传播。这是我们不愿看到的。

在这里我们不会继续深入细节，推荐大家阅读[Piper关于该问题的详细文章](https://ethresear.ch/t/the-data-
availability-problem-under-stateless-
ethereum/6973)。接下来我们便可以继续讨论新的解决方案，这些方案殊途同归，目的皆是为了优化同步协议，能够在一定程度上减轻问题严重性甚至是完全解决同步问题。以下是最有希望的三种替代方案：

  * **以太坊快照协议** (Ethereum Snapshot Protocol, SNAP)。这个我们之前已经讨论过，我将称其为“状态切片排布”(state tiling)。最近，Peter在devp2p库中[对此进行了更详细的描述](https://github.com/ethereum/devp2p/blob/8679dbd339ad0dcad6929b37be0e7eede7b3d1cd/caps/snap.md)。

Snap将状态分割为多个大数据块和证明
(约一万个树节点)，并且可以将其重新拼凑为完整状态。同步节点会从多个节点请求状态的子部分，并且在短时间内从大约100个不同的相似状态根中得出几近有效的状态图片。最后，客户端获得有效状态后，通过切换回getNodeData将数据块“拼凑”起来。

  * **火皇后同步** (Fire Queen’s Sync)。这个主题在最初的技术树文章中讨论过，除了名称之外 ([“firehose”](https://notes.ethereum.org/0v_W4E8lROazqYymPAF7Ew)和[“Red Queen’s sync”](https://github.com/yperbasis/silkworm/blob/master/doc/sync_protocol_v1.pdf)的结合)，并没有太大变化。这类建议十分相似，都是针对状态的各个方面使用一组不同的原语替代getNodeData。

  * **旋转木马** (Merry-go-round) 同步。这是一个新的同步概念，[在ethresear.ch中有高阶的阐释](https://ethresear.ch/t/merry-go-round-sync/7158)，[注释中的描述更为具体](https://notes.ethereum.org/n2bIgRe5SReOM7BZle4jaQ)。在旋转木马同步 (merry-go-round sync) 中，整体状态以预定顺序传递，因此所有参与者都同时传播相同的状态部分。要同步整个状态，必须在旋转木马同步中完成一次完整的“旋转”，涵盖状态的所有部分。

此设计具备一些有用的特性。首先，该同步允许新节点一加入就能立即参与状态传播，而不需要经过完整同步后才能进行工作。其次，它会颠覆当前“由获取方驱动同步”的模式，那些没有数据的节点也能从全节点处请求部分状态。

确切地说，旋转木马同步中的新同步节点知道在某个时间点会提供状态的哪些部分，并相应地进行调整。

值得提及的最后一种同步方式是[beam同步](https://medium.com/@jason.carver/intro-to-beam-
sync-a0fd168be14a)，目前受到两个备选客户端的支持。Beam同步仍然依赖于getNodeData，但是它为这些同步替代方案提供了实验和数据收集的理想入口。

请务必注意，目前关于同步方面仍有很多未知数，因此采用这些独立开发的同步解决方案更为合适。

接下来的几个月，可以看作是各式各样的同步主题黑客松，将对这些想法进行原型化和测试。理想情况下，对于这些同步协议的替代方案，我们可以取其精华，为无状态以太坊设计出一个新标准。

  

# 见证规范原型化

目前无状态以太坊规范库中有一个[规范草稿](https://github.com/ethereum/stateless-ethereum-
specs/blob/master/witness.md)，从高层次描述了一个区块见证 (block witness)
的结构，以及从状态树中构建和修改一个见证的语义。草稿规范的目的是给出一个无歧义的见证定义，以便实现者 (不限客户端或编程语言)
可以编写自己的实现，并有理由确定其实现与其他不同的形式实现是相同的。

如[最新的会议摘要](https://ethresear.ch/t/stateless-ethereum-march-25th-call-
digest/7202)所述，写出区块见证的参考实现并将其引入现有客户进行测试似乎没有不利之处。客户端中的见证原型功能将类似于可启用的可选标志，而且如果网络中有少量测试者产生并中继见证，能够为研究人员提供有价值的资源，从而将其观察纳入后续改进中。

在见证足够强韧并考虑投入广泛使用之前，我们需要“解决”两件事。

  * 见证索引 (Witness Indexing)。这一点相对简单：我们需要一种可靠的方式来确定见证对应哪个区块以及相关联的状态。实现方式可能很简单，例如将一个witnessHash字段放入区块头中。

  * 无状态交易验证 (Stateless Tx Validation)。这个有趣的问题较早之前就被提出，并且[在ethresearch论坛中进行了全面的总结](https://ethresear.ch/t/the-current-transaction-validation-rules-require-access-to-the-account-trie/7046)。总而言之，客户端需要快速检查传入的交易 (等待被打包到之后的区块中) 是否具备被打包到区块中的资格，这样可以防止攻击者向网络发送虚假交易。

但是，当前检测需要访问状态的部分数据，即发送方的nonce和帐户余额。如果是无状态客户端，则无法执行此检查。

要构建有效的见证原型，我们需要实现的工作肯定不止于以上两点，但要为beam同步节点提供一个可用的原型，这两件事是必须要解决的。

  

# EVM

如同技术树的原始版本，我们需要在EVM抽象内部进行一些更改。确切地说，见证需要在网络中生成和传播，并且该活动需要被纳入EVM操作范围中。EVM的关联主题与成本和激励息息相关，以及如何对其进行估算，在实现过程中如何将其对更高层的影响降到最低。

  * 见证gas计算 (Witness gas accounting)。这一点保留之前文章中的陈述：每笔交易将只对整个交易见证的一小部分负责。生成区块见证需要该区块的矿工进行一些计算，因此会产生相应的gas成本，由交易的发送方支付。

  * 代码分块 (Code Merkleization)。见证的主要组件之一是随附的代码。如果没有此功能，包含合约调用的事务将需要该合约的完整字节码以验证其codeHash。代码大小取决于合约，可能会是非常庞大的。

代码的‘merkleization’是一种拆分合约字节码的方法，只需要生成代码的一部分即可生成并验证交易的见证，这是一种大大减小见证平均大小的技术，但目前暂未进行全面研究。

UNGAS/无版本以太坊已从无状态以太坊的“关键路径”中移除。对以太坊来说，这仍然是潜在的有益性能，但在巴黎峰会期间我们明确了一点：其优点和特性可以并且应该独立于“无状态”目标进行讨论。

  

# 二进制树转换

将以太坊状态切换为二进制树结构对于缩小见证大小来说至关重要，见证是否能被缩减到足够小，从而在网络中传播时避免受带宽/延迟影响。

理论上来看，见证大小应缩小三倍以上，但实际情况不需要缩小这么多 (视见证中的合约代码大小而定，这也强调了代码分块的重要性)。

转向完全不同的数据表示形式是一个相当重大的变化，而通过硬分叉实现过渡又将是一个巧妙的过程。上一篇文章中提到的两种过渡策略将保持不变：

  * 渐进式。当前的十六叉状态树将在很长一段时间内逐段进行转换。通过这种方式，任何涉及状态部分的事务或EVM执行都会自动将状态更改编码为新的二进制形式。

这意味着采用“混合”树结构，休眠的状态部分依然保留当前的十六进制形式。该过程实际上永远不会完成，并且对于客户端开发者来说实施难度很大，但是在很大程度上将使用户和更高层的开发者免受第0层改动的影响。

  * 干净利落。该策略将在预定时间计算状态的新二进制树表示，一旦新的状态计算完成就持续以二进制形式表示。尽管从实现的角度来看没那么复杂，但是需要协调所有节点运行者，并且几乎可以肯定会给网络带来一些（有限的）中断，这可能会影响过渡期间开发者和用户的体验。

目前产生了一个新的过渡建议，在渐进式策略和简洁策略之间提供了折中方式。[ethresearch论坛上有该建议的完整概述。](https://ethresear.ch/t/overlay-
method-for-hex-bin-tree-conversion/7104/7)

  * 覆盖。事务的新数据在一定时间之后将直接存储在十六进制顶部的二叉树中，而“历史”十六进制树则在后台进行转换。当基础层实现完全转换之后，可以将两者合并。

过渡到二进制树的另一个考虑因素是客户端的数据库布局。当前，所有客户端都对状态树采用了较为简单的方法，将树中的每个节点存储为[key，value]对，其中的key是节点哈希。根据turbo-
geth的例子来看，过渡策略可能会为客户端提供转换数据库结构的机会。

  

# 敬请继续关注，安全第一！

感谢阅读，也感谢大家针对Eth 1.x进展积极给出的暖心评论。对于后续有关无状态以太坊研究的文章，我还有许多[计划](https://ethereum-
magicians.org/t/the-scrolls-of-stateless-ethereum/4155)，将不定时发布在Ethereum
Magician论坛或者适时发布在以太坊博客中！大家要注意保持社交距离，洗手常放心上！

一如既往，如果大家有任何反馈和问题，或是想要提出新主题，请在推特上@gichiba或@JHancock。

  
  

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

