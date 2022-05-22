[![logo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAICAYAAAD5nd/tAAAACXBIWXMAAA7DAAAOwwHHb6hkAAABj0lEQVQoz12Sv0vDQBTHT0HrD4QWRJRLi3QQOojon1JxUhcFQQeViknrJjiIglgRhW4OTiLSWXB10MnJoToI0lp6ESu1TZNc/L7LFcGDD+8u4X3y3r0wKeUUeAqwEBVYZa9amhCb0bydjbdti/vAsy0jALPYp0EZSODq91W8W2AQPGqZg9CUvkvGUv08fSEywwGESDIaoAW+QQHJbWEq+Y+mqc8OCV3wASZBzP+qJJ8ZY2JrpKgqMvk8Yh8kvL6b6sZ+WZicki/BIBgFUVCk5ywsTr4ikvxI+l4F+w20e21bcQiNGUiZ2OZdSGLYr+jW9+hcw3NUx/DBY6pSCcELZCQ8RMtvOK+K9aErO5ugCqdJCDESVVzSwgMSQhLRwjMl1C1Xw+H4Mf/zPQFhxN5J3qrEbGJRmGMDwjIMYfF+yDNauK+FvVp4qlqG6F4PpY3goMIWxebdiVdbi1CiDC+dtwBdfmcA+X/CQqflFGQP6nf5+20C6blB4yYnRW7chcihCYbwFk0ZzAES9eiIq+DiFyR9m3ZUxiupAAAAAElFTkSuQmCC)![logo](/static/9c635c914229a850d1a9fd284014bdd0/65e33/eco_logo.png)](/)

  * [新闻资讯](/)

  *   * [零时学院](/c0llege)

  * [开发者门户](/develop)

  * [生态漫游](/ecos)

Ξ

Search by [](https://www.algolia.com/?utm_source=react-
instantsearch&utm_medium=website&utm_content=&utm_campaign=poweredby)

## Eth2更新速览#8

存款合约的审计和形式化验证完成、阶段2研究团队、libp2p gossipsub 测试结果...

* * *

DR

Danny Ryan 2020-02-05

来源 | [Ethereum Blog](https://blog.ethereum.org/2020/02/04/eth2-quick-update-
no-8/)

  

![以太坊周刊更新速览开头.png](https://i.ibb.co/SdPYLS4/8becff9df1-png-8703fb498c.png)

  

# **要点速览**

🔹完成对存款合约（deposit contract）字节码的审计和[形式化验证](javascript:void\(0\))

🔹本月关键词：最优化

🔹公布gossipsub[测试结果](https://github.com/whiteblock/gossipsub-testing)

🔹春季活动来袭！会议、黑客马拉松、赏金任务等你参与！

  

# 存款合约的审计和验证

Runtime
Verification最近完成了对eth2[存款合约](https://github.com/ethereum/eth2.0-specs/blob/dev/deposit_contract/contracts/validator_registration.vy)（deposit
contract）字节码的审计和[形式化验证](https://github.com/runtimeverification/verified-smart-
contracts/blob/master/deposit/bytecode-verification/deposit-
spec.ini)。这是通向eth2阶段0主网之路上的一个重要里程碑。这项工作已经完成，我希望社区能对此进行反馈。如果在正式规范中发现任何漏洞或错误，请在[eth2规范库](https://github.com/ethereum/eth2.0-specs)中发起issue。

[K框架](http://www.kframework.org/index.php/Main_Page)中指定的形式语义明确定义了EVM字节码对应的行为，并证明这些行为成立，其中包括输入验证、对默克尔树迭代的更新、日志等等。**[这里](https://github.com/runtimeverification/verified-
smart-contracts/blob/master/deposit/bytecode-verification/deposit-
spec.ini.md)**是指定内容的（半）高级讨论，在[这里](https://github.com/runtimeverification/verified-
smart-contracts/blob/master/deposit/bytecode-verification/deposit-
spec.ini)进一步了解完整的正式K规范。

在这里我要感谢Daejun Park（Runtime Verification成员）所付出的努力，以及Martin Lundfall和Carl
Beekhuizen在此过程中提供的许多反馈和评论。

我还是想说，如果形式化验证是你感兴趣或擅长的领域，那么请不吝提供意见和反馈。

  

# 上月关键词：最优化

过去一个月的主要工作就是进行优化。

尽管在目前看来，进行10倍优化或100倍优化对以太坊社区来说不太切实，但是要抵达终点，这一阶段的进展也至关重要。

  

## 🔻信标链优化的重要性

（要使信标链向下兼容，而非提升设备性能）

信标链作为eth2的核心，是分片系统不可或缺的组件。要同步分片，无论是单个分片还是多个分片，客户端都必须同步信标链。因此，要在普通计算机设备上运行信标链和少量分片，最重要的是，
**即使在验证者高参与度（约30万以上验证者）的情况下，信标链的资源消耗也要相对较低。**

为此，过去一个月eth2客户端团队的主要工作都集中在优化方面，减少了阶段0（信标链）的资源需求。

值得高兴的是，我们正在取得显著的进展。以下概述性内容并不详尽，但有助于读者了解我们的工作。

  

## 🔻10万验证者？Lighthouse：轻而易举

几周前，由于出现证明传播中继循环问题，导致节点自身出现DoS错误，Lighthouse关闭了测试网（约1.6万验证者）。Sigma
Prime迅速修复了这个漏洞，并且寻求更大更强的测试网，可容纳10万验证者。过去的两周，他们一直致力于优化工作，以期实现这种规模的测试网。

Lighthouse测试网的每次改进，目的是确保成千上万个验证者可以轻松地在小型VPS上运行, 配备2个CPU和8GB
RAM。在10万验证者规模的初始测试中，客户端一致使用8GB RAM，然而经过几天的优化，Paul设法将其降低到稳定的2.5GB，并且还有进一步降低的计划。
**Lighthouse在状态哈希方面也取得了很大进步，而BLS签名验证被证明是eth2客户端中的主要计算瓶颈。**

新的Lighthouse测试网发布在即。可以进入他们的[discord聊天室](https://discordapp.com/invite/cyAszAh)了解最新进度。

  

## 🔻Prysmatic测试网规模持续扩大，同步速度显著提升

几周前，当前运行中的Prysm测试网庆祝了其[第10万个slot](https://twitter.com/terencechain/status/1220456877626220544)，验证者数量超过2.8万个。目前，测试网已经超越了18万个slot，活跃验证者数量超3.5万。在维持公共测试网运行的同时，团队还能进行更新、优化、稳定性提升工作是一件非常了不起的事。

Prysm目前正在取得许多实质性进展。在过去的几个月中，我与许多验证者进行了沟通，据他们的体验，客户端一直在显著进步，其中一个令人兴奋的进步是同步速度的提升。
**Prysmatic团队将其客户端同步速度从约0.3区块/秒优化到了约20区块/秒，极大地优化了验证者用户体验，使得验证者能够更快地连接并参与到网络中。**

Prysm测试网的另一个优化是加入了[alethio](https://aleth.io/)的新eth2节点监测器，[eth2stats.io](https://eth2stats.io/sapphire-
testnet)。这是一项选择性服务，以便节点能够在某个位置汇总统计信息。这将有助于我们更好地了解测试网（或将来eth2主网）的状态。

眼见为实！快来[亲自尝试](https://prylabs.net/)一下吧。

  

## 🔻proto_array 备受喜爱

Eth2核心规范经常有意明确预期的非最佳行为。可见，优化规范代码的目的是增强可读性，而不是提升性能。

规范规定了系统的正确行为，而算法则是执行指定行为的过程。多种不同的算法都能一直执行相同的规范。因此eth2规范支持各个组件的多种不同实现，因为客户端团队往往会权衡多方因素（例如计算复杂度、内存占用量及实现复杂度等等）。

[分叉选择](https://github.com/ethereum/eth2.0-specs/blob/v0.10.0/specs/phase0/fork-
choice.md)（fork
choice）就是其中一个例子，此规范用于查找区块链头。eth2规范通过一种简单算法来明确这种行为，以清楚地显示运行部分与边缘情况，例如，当新证明出现时如何更新投票权重，新区块被最终确定后该做什么等等。然而，只是直接实现规范的算法将永远无法满足eth2的生产需求。因此，客户端团队必须在维护客户端运行时思考计算权衡，并且实现更为复杂的算法以满足需求。

对于客户端团队来说，所幸一年前的文件里就有所参考。当时，Protolambda实现了[一系列不同的分叉选择算法](https://github.com/protolambda/lmd-
ghost)，并列出了每种算法的优势与权衡取舍。最近，Sigma
Prime的Paul发现了Lighthouse分叉选择算法中的一个重大瓶颈，于是就去寻找对策。最后，他在Protolambda的成果中发现了
**proto_array** 算法。

虽然为了移植 **proto_array** 以适应最新规范耗费了一些精力，但集成之后， **proto_array**
便被证实能够使“运行时间缩短几个数量级，数据库读取也大大减少”。自首次集成到Lighthouse之后，proto_array
很快也被Prysmatic应用到其最新版本中。与其他算法相比，这种算法具备更加明显的优势，proto_array也就迅速成为大家的宠儿。我非常希望未来会有更多其他团队应用起来！

  

# 阶段2研究进行时：Quilt、eWASM、TXRX团队

阶段2会将状态和执行添加进分片后的eth2中。尽管阶段2的一些核心原则是相对确定的（例如分片之间通过交联与默克尔证明进行通信），但阶段2的设计仍然保持一定的开放性。在过去的一年里，Quilt（ConsenSys研究团队）和
[eWASM](https://github.com/ewasm)（以太坊基金会研究团队）一直在致力于阶段2研究工作，以期在这个开放的设计领域进行探索，与阶段0和阶段1的规范和构建工作并行。

为此，最近将举办大量的公开电话会议来进行讨论，ethresear.ch上也发布了相关的帖子。现在有一些不错的资源能够提供认知帮助，以下仅选取部分：

  * [状态提供者模式的概述](https://ethresear.ch/t/state-provider-models-in-ethereum-2-0/6750)
  * [有关状态提供者的问题](https://ethresear.ch/t/remaining-questions-on-state-providers-and-stateless-networks-in-eth2/6585)
  * [在分片之间转移ETH：问题陈述](https://ethresear.ch/t/moving-eth-between-shards-the-problem-statement/6597)
  * [跨分片转移的路线图](https://notes.ethereum.org/fkPBDSV_QiSePrrk5u-0Qg)（及[Vitalik关于ETH元执行环境博文解析](https://ethresear.ch/t/an-even-simpler-meta-execution-environment-for-eth/6704)）
  * [阶段1分片数据费用市场的相关讨论](https://ethresear.ch/t/phase-1-fee-market-and-eth1-eth2-bridging/6775)

除了Quilt与eWASM团队外，
**新加入的[TXRX](https://twitter.com/TXRXResearch)（ConsenSys研究团队）也将部分精力投入到阶段2研究中，该团队最初的工作重点是增进对跨分片交易复杂性的理解，研究将eth1集成到eth2的可能途径，并对这些途径进行原型化。**

阶段2的所有研发领域都是相对新颖的，因此是深入研究并取得成果的好时机。在今年内，将有更多具体的规范面世，也为开发者提供施展拳脚的空间。

  

# Whiteblock 发布libp2p gossipsub 测试结果

本周，[Whiteblock](https://whiteblock.io/)发布了[libp2p
gossipsub测试结果](https://github.com/whiteblock/gossipsub-
testing)，这是[ConsenSys](https://blog.ethereum.org/2020/02/04/eth2-quick-update-
no-8/consensys.net/)和以太坊基金会共同资助下的结晶。
**这项工作旨在验证用于eth2的gossipsub算法，并为性能边界提供参考，以辅助后续的测试与算法强化工作。**

概括来说，这一系列测试的结果看起来是可靠的，但还需要进一步测试以更好地观察消息传播如何随网络规模而变化。[此处](https://github.com/whiteblock/gossipsub-
testing)参见完整报告，其中详细介绍了他们采用的方法、拓扑结构、实验和结果！

  

# 百花齐放的春天！

今年春季迎来了许多激动人心的会议、黑客马拉松，eth2赏金等等活动！每一场活动中都会有一组eth2研究者和工程师出席。赶快来感受思维的碰撞吧！我们很期待与大家交流，包括工作进度、测试网验证工作、2020值得期待的事等等大家可能感兴趣的话题。

现在不参与更待何时？多个客户端都处于测试网阶段，因此大显身手的时候到了！我们有各种开发工具，可以进行各种尝试，快来找找乐子吧！

以下列出了其中一些与eth2相关的活动：

  * [**ETHDenver** ](https://github.com/whiteblock/gossipsub-testing)— 美国丹佛，2月14至16日，准备了Eth2专项赏金！
  * [**Stanford Blockchain Conference**](https://www.ethdenver.com/) — 美国斯坦福，2月19至21日
  * [**Eth 222**](https://cbr.stanford.edu/sbc20/) — 美国斯坦福，2月22日
  * [**ETHLondonUK**](https://ethlondon.com/) — 英国伦敦，2月28日至3月1日
  * [**ETHCC**](https://ethcc.io/) — 法国巴黎，3月3至5日
  * [**EDCON**](https://www.edcon.io/) — 奥地利维也纳， 4月3至7日
  * [**Ethereal Summit** ](https://www.etherealsummit.com/)— 美国纽约， 5月8至9日
  * [**ETHNewYork**](https://ethglobal.co/) — 美国纽约，日期待定

🚀🚀🚀

  
  

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

