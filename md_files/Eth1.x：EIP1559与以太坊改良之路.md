[![logo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAICAYAAAD5nd/tAAAACXBIWXMAAA7DAAAOwwHHb6hkAAABj0lEQVQoz12Sv0vDQBTHT0HrD4QWRJRLi3QQOojon1JxUhcFQQeViknrJjiIglgRhW4OTiLSWXB10MnJoToI0lp6ESu1TZNc/L7LFcGDD+8u4X3y3r0wKeUUeAqwEBVYZa9amhCb0bydjbdti/vAsy0jALPYp0EZSODq91W8W2AQPGqZg9CUvkvGUv08fSEywwGESDIaoAW+QQHJbWEq+Y+mqc8OCV3wASZBzP+qJJ8ZY2JrpKgqMvk8Yh8kvL6b6sZ+WZicki/BIBgFUVCk5ywsTr4ikvxI+l4F+w20e21bcQiNGUiZ2OZdSGLYr+jW9+hcw3NUx/DBY6pSCcELZCQ8RMtvOK+K9aErO5ugCqdJCDESVVzSwgMSQhLRwjMl1C1Xw+H4Mf/zPQFhxN5J3qrEbGJRmGMDwjIMYfF+yDNauK+FvVp4qlqG6F4PpY3goMIWxebdiVdbi1CiDC+dtwBdfmcA+X/CQqflFGQP6nf5+20C6blB4yYnRW7chcihCYbwFk0ZzAES9eiIq+DiFyR9m3ZUxiupAAAAAElFTkSuQmCC)![logo](/static/9c635c914229a850d1a9fd284014bdd0/65e33/eco_logo.png)](/)

  * [新闻资讯](/)

  *   * [零时学院](/c0llege)

  * [开发者门户](/develop)

  * [生态漫游](/ecos)

Ξ

Search by [](https://www.algolia.com/?utm_source=react-
instantsearch&utm_medium=website&utm_content=&utm_campaign=poweredby)

## Eth1.x：EIP1559与以太坊改良之路

以太坊费用市场亟待改变，我们应该如何看待EIP 1559与Escalator提案？

* * *

GI

Griffin Ichiba Hotchkiss 2020-06-22

来源 | [Ethereum Blog](https://blog.ethereum.org/2020/06/16/eth1x-1559/)

  

![1.x封面.png](https://i.ibb.co/7gcsNnN/1-x-0d3dc30bff.png)

  

最近我的脑中总是浮现世界末日之后的荒原。就像电影《疯狂的麦克斯：狂暴之路》中的一个场景。主角们刚刚逃脱了第一波追捕，并领先于可能的追捕者。他们需要继续前进，但也需要对电影中的关键部分进行维护：一辆能够帮助他们逃出生天的巨型“战车”。因此，主角Charlize
Theron在途中爬到车底进行维修：

![1.x15.png](https://i.ibb.co/Xb3nysH/1-x15-35265727a5.png)

在行进过程中对一辆巨大的、复杂的卡车进行维修，太符合这部电影惊心动魄的剧情设置了。当我看到这个场景时，发觉正好可以用来比喻EIP修订过程与核心开发者工作之间的关系。

针对以太坊协议的更改是实时进行的，许多谨慎细致的工程实现会被纳入，以便所有事情、所有人 (如果可能的话)
都能在升级过程中继续前行。在区块链荒地的道路上仍有颠簸，但总的来说，以太坊仍然遥遥领先于其他劫掠车辆
(技术债务)——只要卡车保持前进步伐，不停止向地平线移动。新的提案在短期内可能会对现状造成一些破坏，但总体而言，它们通常是对协议有价值的改进。

**本文要讨论的升级属于“Eth1.x”的范畴，但却并不是无状态以太坊的一部分工作，而是一个全新的Gas费用市场/区块大小机制。**
EIP1559已经成为社区与开发者针对以太坊改良反馈的一个颇具趣味的案例研究。透过这个EIP的历史发展进程与关注度的提升，我认为我们可以从中窥探到许多针对以太坊发展的建设性讨论，并且希望获得一些明确的见解，能够指引无状态以太坊框架之外的重要发展。

之前在同系列文章中，我试图做到有条有理地抽丝剥茧，但在本文中，我不会深入讨论本EIP的技术细节，而是更多地关注提案内容本身，及其引发的讨论。在此之前，我们先来简单聊聊
EIP-1559 和‘Escalator’这两个提案的内容，围绕着这两个提案又产生了哪些讨论，目前现况如何。

#  

# EIP 1559

[EIP 1559](https://eips.ethereum.org/EIPS/eip-1559)的初衷是一个不错的切入点，其动机十分简单：

“以太坊目前的“最高价竞争”费用模式效率低下，并且伴随着不必要的高昂用户成本。此EIP提出了一个替代方案，即根据网络需求调整基本网络费用，从而提升费用价格效率，同时降低客户端软件为了避免支付非必要高费用所需的复杂度。”

**在当前系统中，新提交的交易必须等待被矿工打包进新区块，但交易方可以通过提高 gasPrice参数到网络平均水平之上，激励矿工优先打包自己的交易。**
按照理性的矿工逻辑，他们总是会倾向于打包高手续费的交易，以此最大化自己的收益，因此，我们可以推断首先被打包进新区块的交易伴随着最高的gas费。

**这种最高价竞争模式的问题在于，当交易需求膨胀时，局面很快就会失控。**
当区块即将达到最大容量时，将交易打包进下一个区块的费用可能会大幅攀升，因为用户希望通过付出高价使得自己的交易被优先打包。

尽管目前矿工们具备一定的能力来增加单个区块的交易容量，但并不能非常快速地改变上线，而且实际上矿工们更乐意通过将小容量区块来获取收益，而不是提高区块的gas上限
(考虑到叔块率，区块越大矿工面临的风险就越大)。

尤其是如果用户的钱包使用了价格算法以使自己的交易在一定期限内被打包，那么最终可能会支付[天价手续费](https://etherscan.io/txs/label/high-
transaction-fee)将交易打包进一个几乎快满了的区块。

EIP 1559引入了gas费用的 ‘base fee’ (基本费) 概念，该费用被设定为动态调整，使得区块中的gas总使用量接近当前的一千万gas上限。
**这笔基本费不会进入矿工的口袋，而是会被销毁。**

为了激励矿工打包交易，用户还能设定一个'Tip' (小费) 参数，并给出一个自己愿意为交易打包所支付的最高费用，矿工将获得这笔消费。

由于基本费不会因网络需求的即时变化而剧烈波动，因此用户在一定程度上避免了最高价竞争所带来的低效问题
(但小费模式延用最高价竞争)。此外，由于基本费会被销毁，而不是支付给矿工，如此一来矿工就没有动机尝试操纵费用了。更重要的是，该机制还试图解决钱包开发者的一大难题：通过使费用更具预测性，钱包就能自动估算网络费用。

如果读者想进一步了解EIP 1559，我建议阅读[Vitalik的EIP 1559
FAQ](https://notes.ethereum.org/Wjr1SnW-
QaST7phX9C5wkg?view)以及[Barnabe的Jupyter笔记](https://github.com/ethereum/rig/blob/9de2ecbba130fba13011eca2b229979b0adcba52/eip1559/eip1559.ipynb)。

#  

# Escalator: EIP 1559的新对手

当前以太坊交易费的最高价竞争机制存在低效问题，这是不争的事实，而且我们需要明确一点：当前费用机制还有优化空间，对此没有人有异议，制定最高价竞争机制的替代方案对整个以太坊网络来说是大有裨益的，开发者和终端用户最终都能从中受益。我们能够并且应该就此达成一致意见。

然而，EIP 1559中提出的新机制与当前的运行方式大相径庭，如果采用的话会引发一些问题，尤其是会影响为用户创建并提交以太坊交易的软件。
**钱包需要进行巨大的调整来适应这一新机制。**

虽然从长远来看，所有相关方都能从中受益，但就短期来说，为了适应新机制并且防止软件崩溃，采用该提案会对开发者造成巨大的工作负担。

EIP
1559保持其原始状态一段时间之后，以太坊社区开始权衡，包括受此提案影响最大的钱包开发者。钱包开发者们没有抵制此提案，而是从一个有趣的切入点来进行讨论。

他们重新衡量了此提案的核心动机 (即提升以太坊交易的用户体验)，并带在该语境中代入EIP
1559，他们表示“如果无论如何我们都要实现这些工作，那我们从一开始就应该了解这对用户来说会是怎样的，并且本着这个初衷来考虑提案内容。”

这就是[Dan Finlay提出EIP 1559替代方案的简要背景——The Escalator
Algorithm。](https://github.com/danfinlay/EIPs/blob/Escalator/EIPS/eip-x.md)此提案与EIP
1559中的机制有许多相似之处，动机和目标也大抵相同。但Escalator机制是作为替代改进提案提出的，使得大家围绕这两种机制进行更为细致的讨论。

为了推动社区针对gas费用市场进行更高效更具体的探讨，我认为给出一个明显优于现状的替代方案是有必要的，如此一来就可以将EIP
1559中涉及到的所有特性与另一个合理替代方案进行对比。

Escalator机制与当前的最高价竞争模式有些相似，但提出了一些重要改变：

  * 相比在提交交易时设定固定价格，用户可以给出 **“逐步上调”** 的价格，并设定一个他们愿意为了使交易被打包而支付的最高价。所有的出价都会被置于‘escalators’队列中，队列将 **按照同等速率逐步地、可预测地提高** 队列中的所有出价。矿工在查看所有escalators的队列时，会选择最高价格的交易，不管这些交易位于哪个escalator中。当某笔交易被打包进区块时，该用户不会按照当前出价进行支付，而是支付队列中的下一个最高价。

Escalator机制的主要优势是 **能够高效展现价格，同时通过收取队列中的第二高价格，防止用户支付过高费用** 。

该机制也有一些优势与EIP 1559相似： **即使发生网络堵塞，用户也能更简便地选择适当的价格**
。值得注意的是，Escalator机制本身不会对区块大小的决定机制产生任何影响。

![](https://i.ibb.co/pKHH1Vn/1-x16-1f80d547ce.gif)

Escalator Algorithm提案本身就很有意思，我强烈推荐阅读此提案的[‘user strategy’ (用户策略)
部分](https://news.ethereum.cn/eth1x-1559/#user-strategies-under-various-
conditions-and-algorithms)，以便对三种不同的交易处理模型进行高层次的比较。如果读者对这个话题感兴趣，这篇介绍Escalator
Algorithm的[论文](https://agoric.com/papers/incentive-engineering-for-
computational-resource-management/full-text/)也很值得深入研读，但我好像偏题了……

在一次EIP 1559实现者电话会议中，Dan给出了一些模板，展现钱包中的不同参数在用户看来是怎样的，他还强调了如何通过用户的需求隐藏或显示这些参数。

![1.x17.png](https://i.ibb.co/K982Xr5/1-x17-61ffe60187.png)

这些设计旨在为社区讨论提供参考，帮助我们从用户的角度衡量EIP 1559和escalator算法。

通过提出一个合理的替代提案，并且将开发者关于用户体验的意见重新纳入考虑，EIP
1559/Escalator的相关讨论非常巧妙地为优化费用市场这一最终目标创造了新的探索空间。费用市场还远远没有为下一次硬分叉做好准备，但它就像《疯狂的麦克斯》中的战车，仍然在前进。

#  

# 以太坊未来可期

我相信EIP
1559/Escalator对于以太坊社区来说是观察和学习的重要对象，尤其是这与无状态以太坊未来的一大变化有着许多相同的特征：[Oil/Karma EVM
semantic changes](https://ethresear.ch/t/meta-transactions-oil-and-karma-
megathread/7472).与费用市场类似，其中的一些提议 **对以太坊开发者和用户将产生重大的二级效应。** 如同EIP
1559，需要明确考虑到如何支持用户体验，因此也有机会和理解用户体验的开发者进行协作，确保提案有足够的动能支撑起成功的升级。

改进以太坊 (1.x)
以及其他公链是一段艰辛的旅程。有效的讨论路线应该是朝着有意义的改进建议，并且进一步保证听到受影响最大的开发者和用户的声音，将他们的顾虑纳入讨论。因为我们终将驾驶着同一辆战车驶向Serenity。要走在[以太坊状态膨胀问题](https://blog.ethereum.org/2019/12/10/eth1x-files-
fast-sync/)的前面，意味着我们要不断地提出有建设性的方案和批判，在保持动能的前提下进行改变，这是我们赖以生存的根基！

![1.x18.png](https://i.ibb.co/mtcfzSV/1-x18-1e38e7ff7f.png)

  
  

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

