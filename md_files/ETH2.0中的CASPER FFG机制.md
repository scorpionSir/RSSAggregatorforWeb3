[![logo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAICAYAAAD5nd/tAAAACXBIWXMAAA7DAAAOwwHHb6hkAAABj0lEQVQoz12Sv0vDQBTHT0HrD4QWRJRLi3QQOojon1JxUhcFQQeViknrJjiIglgRhW4OTiLSWXB10MnJoToI0lp6ESu1TZNc/L7LFcGDD+8u4X3y3r0wKeUUeAqwEBVYZa9amhCb0bydjbdti/vAsy0jALPYp0EZSODq91W8W2AQPGqZg9CUvkvGUv08fSEywwGESDIaoAW+QQHJbWEq+Y+mqc8OCV3wASZBzP+qJJ8ZY2JrpKgqMvk8Yh8kvL6b6sZ+WZicki/BIBgFUVCk5ywsTr4ikvxI+l4F+w20e21bcQiNGUiZ2OZdSGLYr+jW9+hcw3NUx/DBY6pSCcELZCQ8RMtvOK+K9aErO5ugCqdJCDESVVzSwgMSQhLRwjMl1C1Xw+H4Mf/zPQFhxN5J3qrEbGJRmGMDwjIMYfF+yDNauK+FvVp4qlqG6F4PpY3goMIWxebdiVdbi1CiDC+dtwBdfmcA+X/CQqflFGQP6nf5+20C6blB4yYnRW7chcihCYbwFk0ZzAES9eiIq+DiFyR9m3ZUxiupAAAAAElFTkSuQmCC)![logo](/static/9c635c914229a850d1a9fd284014bdd0/65e33/eco_logo.png)](/)

  * [新闻资讯](/)

  *   * [零时学院](/c0llege)

  * [开发者门户](/develop)

  * [生态漫游](/ecos)

Ξ

Search by [](https://www.algolia.com/?utm_source=react-
instantsearch&utm_medium=website&utm_content=&utm_campaign=poweredby)

## ETH2.0中的CASPER FFG机制

由近及远，阐明Casper FFG机制细节概念与分叉选择规则。

* * *

AA

Aditya Asgaonkar 2020-04-23

来源 | [adiasg.me](https://www.adiasg.me/)

  

感谢Danny Ryan与笔者共同讨论及审阅文章。

我[上一篇文章](https://www.adiasg.me/2020/03/31/casper-ffg-
explainer.html)讨论的是关于Casper Friendly Finality Gadget （Casper
FFG）的基础知识，那么这篇文章的第一部分将重点介绍信标链Casper FFG机制实现的高层级细节，第二部分将讨论分叉选择规则（fork choice
rule）和活性的其他相关因素。

这篇文章解释的是直接从Eth2.0规范中挑选的概念，我会尽可能地提供规范中参数与函数的相关链接。这些链接仅供参考，因此无需查阅这些链接也能读懂这篇文章。

  

# Casper FFG 机制

## Slots、 Epochs 及 Attestations

**Slots（时隙）** ：区块链上的时间是按照 slot
来划分的，每个slot期间有一个新区块被提议。每个slot为12秒，[一个slot分配一个验证者提议产生一个新区块](https://github.com/ethereum/eth2.0-specs/blob/dev/specs/phase0/beacon-
chain.md#get_beacon_proposer_index)。

**Epochs** （时段）：Casper
FFG机制无需在完整的区块树上运行，仅处理投票所需的某些特定slot的区块即可。因此，在通过查看投票情况以对区块进行最终确定时，能够免于查看过多来源区块 –
目标区块对，从而减少了成本。由于这些特殊slot为验证者提供了足够的投票时间，因此当每次进行FFG最终确定性检查时，预计将看到绝大多数验证者的新投票结果。每个epoch由32个slot组成，所以每个epoch的时间长度为6.4分钟，即1
epoch = 32 slots * 12s =
6.4mins。FFG机制只处理这些epoch的边界区块（称为”检查点（checkpoints）”或“epoch边界区块（EBB）”）。

![](https://i.ibb.co/gM9F7Cn/1.png)

**假设每个epoch由3个slot组成，Slots和Epochs之间的关系示意图，其中区块A、D、G是检查点**

[**Attestations证明**](https://github.com/ethereum/eth2.0-specs/blob/dev/specs/phase0/beacon-
chain.md#attestationdata)：指的是Casper
FFG投票，其中包含诸如来源区块、目标区块、进行证明时的slot编号及验证者的标识符等信息。证明由验证者广播到p2p网络，最终再由区块生产者打包进区块。

  

## Casper FFG 机制的变化

与我以前的文章中提到的相比较，最终确定性的定义有所改变。

**Finalization（最终确定性）** ：区块B已最终确定的条件如下：

  * 或是充当创世区块
  * 或是B_0已被证明，条件如下： 
    * slot编号按顺序递增，检查点也随之按[B_0, B_1, … , B_n]顺序排列，其中n >= 1，这些检查点区块位于同一条链上且已被证明。
    * 同时超过2/3的验证者已将票投给 (B_0, B_n)

![ffg2.png](https://i.ibb.co/HpZ86MH/2.png)

**黄色区块处于已证明状态，红色区块处于最终确定性状态**

更改后的定义仍然保留了上一篇文章中Casper
FFG安全证明的概要。关于完整证明的内容，请参见[本文](https://arxiv.org/pdf/2003.03052.pdf)的“安全性”部分。

#### **Casper FFG 最终确定性检查**

信标链采用链上FFG机制来处理区块与证明，以检测最终确定性。在每个epoch边界，该机制都会处理新的证明，并更新已证明与已最终确定区块的信息。

为了尽可能降低任何来源区块-目标区块对之间证明的处理成本，链上FFG机制仅处理特定的来源区块-
目标区块对，即只处理当前与上一个epoch的证明[（事实上还要满足更多条件）](https://github.com/ethereum/eth2.0-specs/blob/dev/specs/phase0/beacon-
chain.md#attestations)。这种特性导致链上FFG机制无法检测所有最终确定性实例！简而言之，这种链上机制是合理的，但并不完善。

另外，由于仅处理最后两个epoch的证明，该机制还引入了网络同步假设（network synchrony
assumption），假设证明在两个epoch的时间内广播到全网。

[链上FFG机制规范](https://github.com/ethereum/eth2.0-specs/blob/dev/specs/phase0/beacon-
chain.md#justification-and-finalization)十分简单：

  * **第一步要检查区块合理性** 。采用最后两个epoch的新证明来检查它们的边界区块是否合理。
  * **下一步要检查区块最终确定性** ，检查对象是最后两个epoch的边界区块。仅对四组来源区块-目标区块对进行最终确定性检查，以求提高性能和简化规范。

![](https://i.ibb.co/hdXB2sF/ffg3-cf760ec51a.png)

  

![](https://i.ibb.co/gy6MFBB/4.png)

**此图展示最终确定性检查涉及的检查点** ，黄色区块为已证明状态，红色区块为已最终确定区块

  

# 分叉选择与验证者计划

尽管Casper FFG机制对区块最终确定保证规则进行了概述，但并未提及在实践中如何保证网络活性。
_（注意：本文并非试图证明网络活性，而是概述有望保证活性的过程。相关严谨分析，请参阅[此文](https://github.com/ethereum/eth2.0-specs/blob/dev/specs/phase0/beacon-
chain.md#justification-and-finalization)。）_

本文这部分将重点关注两个主要的活性相关因素：

  * 验证者用来查找区块链头所执行的分叉选择规则
  * 验证者遵循的区块生成与证明计划

  

## HLMD GHOST 分叉选择规则

提议区块的验证者首先必须找到本地区块链头，为此，他们要遵循Hybrid Latest Message Driven (HMLD)GHOST作为分叉选择规则。

[分叉选择规范](https://github.com/ethereum/eth2.0-specs/blob/dev/specs/phase0/fork-
choice.md#get_head)如下：

  1. 在每个epoch开始的时候，验证者确定当前视图下的最新已证明区块。这一变量会在该epoch内被冻结，并在下一个epoch开始时再次更新。
  2. 筛选并排除出没有把步骤1确定的已证明区块作为此区块链中最新已证明区块的区块。
  3. 遵循[一般LMD GHOST规则](https://vitalik.ca/general/2018/12/05/cbc_casper.html)，由上至下遍历区块树，直到找到叶节点为止。

分叉选择的更多相关信息，请参见[此文](https://arxiv.org/pdf/2003.03052.pdf)的“Hybrid HLMD
GHOST”部分。

  

## 验证者计划

每个验证者对网络负有两大主要责任：提议新区块和在其本地视图中证明最佳区块，为此制定了验证者计划，以防止产生混乱和简化网络中的消息传递。[此计划由每个验证者利用从当前信标链状态获取的随机性计算而得](https://github.com/ethereum/eth2.0-specs/blob/dev/specs/phase0/validator.md#validator-
assignments)，以免攻击者支配验证者计划。

**提议计划（Proposal Schedule）**
：在每个epoch中的每个slot，[都会有一位验证者被分配为提议者](https://github.com/ethereum/eth2.0-specs/blob/dev/specs/phase0/beacon-
chain.md#get_beacon_proposer_index)。该验证者遵循分叉选择规则在区块树的本地视图中找到链头，并为该链头生成一个新的子块。验证者将其见到的证明打包到区块中并获取奖励。当进行最终确定性检查时，这些证明将输入到链上FFG机制。

**证明计划（Attestation Schedule）**
：每个epoch中的每个slot中的每个验证者都要生成证明。实际上，对于每个epoch，整个验证者集被随机划分为SLOTS_PER_EPOCH个等同大小的委员会，这些委员分别被分配到一个特定的slot，然后生成证明。在生成证明时，验证者将根据其本地视图，以最后一个已证明区块作为来源区块，以链头后的最新检查点作为目标区块。

验证者计划的更多相关信息，请参阅Eth2.0规范中的[验证者指南](https://github.com/ethereum/eth2.0-specs/blob/dev/specs/phase0/validator.md)。

  
  

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

