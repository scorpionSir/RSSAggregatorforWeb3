[![logo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAICAYAAAD5nd/tAAAACXBIWXMAAA7DAAAOwwHHb6hkAAABj0lEQVQoz12Sv0vDQBTHT0HrD4QWRJRLi3QQOojon1JxUhcFQQeViknrJjiIglgRhW4OTiLSWXB10MnJoToI0lp6ESu1TZNc/L7LFcGDD+8u4X3y3r0wKeUUeAqwEBVYZa9amhCb0bydjbdti/vAsy0jALPYp0EZSODq91W8W2AQPGqZg9CUvkvGUv08fSEywwGESDIaoAW+QQHJbWEq+Y+mqc8OCV3wASZBzP+qJJ8ZY2JrpKgqMvk8Yh8kvL6b6sZ+WZicki/BIBgFUVCk5ywsTr4ikvxI+l4F+w20e21bcQiNGUiZ2OZdSGLYr+jW9+hcw3NUx/DBY6pSCcELZCQ8RMtvOK+K9aErO5ugCqdJCDESVVzSwgMSQhLRwjMl1C1Xw+H4Mf/zPQFhxN5J3qrEbGJRmGMDwjIMYfF+yDNauK+FvVp4qlqG6F4PpY3goMIWxebdiVdbi1CiDC+dtwBdfmcA+X/CQqflFGQP6nf5+20C6blB4yYnRW7chcihCYbwFk0ZzAES9eiIq+DiFyR9m3ZUxiupAAAAAElFTkSuQmCC)![logo](/static/9c635c914229a850d1a9fd284014bdd0/65e33/eco_logo.png)](/)

  * [新闻资讯](/)

  *   * [零时学院](/c0llege)

  * [开发者门户](/develop)

  * [生态漫游](/ecos)

Ξ

Search by [](https://www.algolia.com/?utm_source=react-
instantsearch&utm_medium=website&utm_content=&utm_campaign=poweredby)

## Eth2更新速览#7

v0.10.0版本规范完成，下一步怎么走？阶段1.5又是什么？

* * *

DR

Danny Ryan 2020-01-18

来源 |Ethereum Blog

  

![以太坊周刊更新速览开头.png](https://i.ibb.co/SdPYLS4/8becff9df1-png-8703fb498c.png)

  

2020年的首篇eth2更新速览来啦！今年将是激动人心的一年！

  

# 要点速览

🔸
[v0.10.0版本规范](https://github.com/ethereum/eth2.0-specs/releases/tag/v0.10.0)发布，将作为多客户端测试网与安全审计的稳定性目标

🔸
@paulhauner与@sigp_io团队共同致力于开发[Lighthouse客户端](https://twitter.com/paulhauner/status/1217349576278999041)

🔸 [Prysm测试网](https://prylabs.net/)[重启](https://medium.com/prysmatic-
labs/eth-2-0-dev-update-42-mainnet-capable-testnet-now-
hiring-53d4d08d3901)，现已加入聚合器并运行主网配置

🔸 加速eth1链与eth2链合并的[新提案](https://ethresear.ch/t/alternative-proposal-for-early-
eth1-eth2-merge/6666)（也被称为阶段1.5）

  

# v0.10.0版本规范

v0.10.0版本规范发布，将作为多客户端测试网与安全审计的稳定性目标。

[v0.10.0](https://github.com/ethereum/eth2.0-specs/releases/tag/v0.10.0)（代号404
Not Found）已于上周发布。技术细节参见[issue
notes](https://github.com/ethereum/eth2.0-specs/releases/tag/v0.10.0)，如**集成IETF
BLS签名标准以及简化eth1缓存等。**然而本次规范更新对于eth2来说究竟意味着什么呢？

阶段0规范曾在Devcon5之后解冻，以引入一些新的更改。而v0.10.0则是这一系列更新的终点，并且集成了新IETF BLS标准。

曾几何时，这些变更扰乱了eth2客户端顺利的开发节奏，准备就绪的测试网也受影响延迟上线。然而随着v0.10.0的发布，现在我们的工作回到了正轨。

  

🔻 **资源新增及更新**

随着v0.10.0规范的发布，客户端测试网和第三方安全审计又有了明确的方向。

因此，我们最近更新了许多入门级资源，也创建了一些新资源。如果想进一步了解eth2 阶段0规范，那以下资源绝对不容错过！

▫[易读版阶段0](https://notes.ethereum.org/@djrtwo/Bkn3zpwxB)

▫ [Eth2设计理念](https://notes.ethereum.org/@vbuterin/rkhCgQteN)

▫[阶段0设计备忘录](https://notes.ethereum.org/EbCbXn_BTuuUYqOaLE3iGA?view)

▫[验证者生命周期文档](https://notes.ethereum.org/@hww/lifecycle)

▫ [规范优化后的状态转换和SSZ图解](https://github.com/protolambda/eth2-docs#timeline-
concept)

▫ [证明聚合策略的相关讨论](https://notes.ethereum.org/@hww/aggregation)

  

🔻 **审计进行时**

Least Authority已于本周一开始安全审计工作，目前正在继续深入。我们对他们的工作抱有很高的期待，并且对于能和这样高水准的团队合作感到兴奋！

另一条激动人心的消息是阶段0加密经济学的审计和形式化工作将由一支新的以太坊基金会团队负责，他们是Robust Incentives Group (RIG)。

RIG已经搭建了一个[cadCAD](https://github.com/BlockScience/cadCAD)环境来模拟eth2的经济模型，同时对不同形式的攻击进行探索，包括时序攻击、不同规模卡特尔（cartels）的潜在效应等等。

RIG将其核心工作内容编写成了简明易懂的[python笔记](https://github.com/ethereum/rig/blob/master/eth2economics/code/beaconrunner/beacon_runner.ipynb)，有兴趣不妨一读。

  

🔻 **接下来是什么？**

虽然在这里我不会深入讨论，但我会在今后的系列文章中加入更多细节信息。

在进行审计的同时，eth2客户端会更新代码至v0.10.0版本规范，集成新的BLS标准，并且保持测试网稳定运行。
**一旦v0.10.0版本规范初步实现了稳定性，多客户端工作就会随之开始进行。**

关于这方面的工作，我的预期是首先在大型单客户端测试网中进行少量的多客户端测试。具体来说，我希望看到一些客户端作为少数节点加入既有的单客户端测试网，从而针对最初的互操作性进行测试。

一旦互操作性测试成功，在开始时我们会安排两个以上客户端共同参与到创世过程。我估计在这个阶段会有一些混乱状况，我们也还需要从中学习。随着细微规范的整合，规范中的含糊之处也许会被厘清。我们甚至还可能会发现一些意料之外的问题，大型测试网的运行本身就能完成自我审计。

审计结果会在二月陆续公布，到时我们预计会再对阶段0规范进行一些修改。规范变动程度，以及这些变动对客户端开发和时间线的影响还有待确定。无论如何，
**审计后的v0.11.0版本将在3月初前后发布。**

如果变动不大，客户端将会集成修改，同步测试网，然后按照计划推进。如果变动较大，那么集成工作可能会耗时更久，并且需要进行额外测试，然后完全重启现存的测试网。

**在v0.11.x版本稳定之后，我们将会发布最终主网版本（v1.0.0）：实际耗时需要视变动深度而定。**

以上是对将来几个月工作的高度概括。接下来我会保持更新，告知大家我们的最新进度。

  

# Eth2客户端与测试网

🔻 **不断优化中的Lighthouse**

Sigma
Prime在[关闭](https://lighthouse.sigmaprime.io/update-20.html)其首个公开测试网之后一直显得比较沉寂，但他们在低调做实事。Lighthouse客户端的主要负责人Paul
Hauner最近发布了一个[推特系列](https://twitter.com/paulhauner/status/1217349576278999041)，其中公布了团队近来针对eth2客户端进行的优化以及取得的成果。

很明显在过去四周里，他们一直在低调运行一个[公共测试网](https://twitter.com/paulhauner/status/1217349579579916288)，并且在BLS集成、区块处理、数据库读/写等各个方面取得了不错的成绩。还不[安装](https://lighthouse-
book.sigmaprime.io/become-a-validator.html)一个亲自试试吗！

对了，Sigma Prime最近发布了针对Lighthouse用户界面的[RfP](https://lighthouse.sigmaprime.io/ui-
rfp.html)（需求建议书），如果你有不错的前端技能，并且想要参与进来，不妨小试牛刀。这类工作十分有利于促进多元化用户参与验证工作。

  

🔻 **Prysmatic测试网重启，运行主网配置和聚合器**

Prysmatic Labs最近重启了他们的[公共测试网](https://medium.com/prysmatic-labs/eth-2-0-dev-
update-42-mainnet-capable-testnet-now-
hiring-53d4d08d3901)，现在运行了主网配置和证明聚合策略。正如在前序文章中所谈到的，主网配置具备更大的缓存、更长的epoch，通常还要比最初使用的最低配置复杂一些。运行一个主网配置的、涵盖上万个验证者的稳定测试网，这是Prysmatic目前在攻克的重要里程碑。

如果你想要参与其中，可以尝试[成为一名验证者](https://prylabs.net/)或者加入[discord聊天室](https://discord.gg/upbrAU7)。

对了，Prysmatic
Labs也在[招募](https://twitter.com/raulitojordan/status/1215689700150775808)。如果你是经验颇丰的开发者，与Prysm远程协作无疑是一次难得的机会。一起开创未来吧！

  

# 阶段1.5：加速合并eth1&eth2

在假期期间，Vitalik发布了一个[新提案](https://ethresear.ch/t/alternative-proposal-for-early-
eth1-eth2-merge/6666)，关于如何加速合并eth1和eth2，如何尽快从eth2新基础设施中受益。该提议建议**在阶段1基础设施（分片数据链）就位之后，在完全的阶段2（可扩展的执行环境和所有跨分片技术）到来之前，将eth1作为一个分片迁移到eth2中。**因此，这个过程被称为阶段
1.5。

**对于以太坊协议、开发者和用户来说，阶段1.5会带来许多潜在益处。**

▫如果eth1成为eth2的一部分，就允许eth1以原生方式获取可扩展的分片数据层。目前以太坊上一些最震撼的结构是将数据放在layer1上进行扩展的layer2协议。这些协议将与eth2完美契合，即便是仅仅作为一条具有本地计算能力的链（即作为分片的eth1链）。广义来说，这些结构被称为“rollups”。Rollups中有许多不同的种类，我希望这个设计研究领域能够继续扩张并且获得丰硕的成果。

▫将eth1作为eth2 的一个分片就从协议中剔除了PoW，这将在很大程度上减少发行率，并且一次性叫停以太坊上的能源密集型挖矿。

▫最后，尽快将eth1迁移到eth2中，能够减少各个部分的不协调性，将系统、社区以及核心协议的开发统一起来。尽管eth2的基础架构与当前的以太坊链是并行开发，但尽早将eth1整合进eth2之中，不仅是技术上的成就，更有利于将协议开发者、应用开发者、所有贡献者和用户维护在一个统一的、团结的以太坊社区中。

根据目前的讨论和反响来看，开发者和社区成员对这个新提案感到很兴奋。要实现当前的阶段1.5，很大程度上依赖于两个独立组件的成功：**eth2的阶段1和eth1上的无状态以太坊。**我们能从这两个组件的大致路线图中按图索骥，得到一些如何以及何时实现该新提案的线索。

接下来的几个月，我们会尽责推动规范完善并识别技术上的挑战，以便能够在时机成熟时做好充分准备🚀

  
  

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

