[![logo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAICAYAAAD5nd/tAAAACXBIWXMAAA7DAAAOwwHHb6hkAAABj0lEQVQoz12Sv0vDQBTHT0HrD4QWRJRLi3QQOojon1JxUhcFQQeViknrJjiIglgRhW4OTiLSWXB10MnJoToI0lp6ESu1TZNc/L7LFcGDD+8u4X3y3r0wKeUUeAqwEBVYZa9amhCb0bydjbdti/vAsy0jALPYp0EZSODq91W8W2AQPGqZg9CUvkvGUv08fSEywwGESDIaoAW+QQHJbWEq+Y+mqc8OCV3wASZBzP+qJJ8ZY2JrpKgqMvk8Yh8kvL6b6sZ+WZicki/BIBgFUVCk5ywsTr4ikvxI+l4F+w20e21bcQiNGUiZ2OZdSGLYr+jW9+hcw3NUx/DBY6pSCcELZCQ8RMtvOK+K9aErO5ugCqdJCDESVVzSwgMSQhLRwjMl1C1Xw+H4Mf/zPQFhxN5J3qrEbGJRmGMDwjIMYfF+yDNauK+FvVp4qlqG6F4PpY3goMIWxebdiVdbi1CiDC+dtwBdfmcA+X/CQqflFGQP6nf5+20C6blB4yYnRW7chcihCYbwFk0ZzAES9eiIq+DiFyR9m3ZUxiupAAAAAElFTkSuQmCC)![logo](/static/9c635c914229a850d1a9fd284014bdd0/65e33/eco_logo.png)](/)

  * [新闻资讯](/)

  *   * [零时学院](/c0llege)

  * [开发者门户](/develop)

  * [生态漫游](/ecos)

Ξ

Search by [](https://www.algolia.com/?utm_source=react-
instantsearch&utm_medium=website&utm_content=&utm_campaign=poweredby)

## 白话ETH2.0：你需要了解什么？

本文通俗地讲解了从当前以太坊主网向Eth2.0升级的各个概念，包括Pos、信标链、分片。

* * *

M

MyCrypto 2020-09-16

来源 | [MyCrypto](https://medium.com/mycrypto/eth2-0-everything-you-need-to-
know-eb32fbfe0bd)

  

# 前言

Eth2升级对以太坊网络来说是一次基础架构的更新。如果读者持有ETH或使用最流行的DeFi协议之一，无需做任何事，因为当前的以太坊网络将与Eth2兼容。现在的ETH不会发生任何变化，网络升级不会产生新代币。

以太坊的大规模网络升级正在进行中，大家正翘首以待。Eth2有许多东西需要考虑，包括从PoW向PoS的过渡、分片以及信标链的引入。本文简要介绍了以下各个方面：

  * 以太坊现状
  * Eth1: PoW(工作量证明)
  * Eth2: PoS(权益证明)
  * 引进：分片链
  * 引进：信标链
  * Eth2路线图
  * 总结

  

# 以太坊现状

当前的以太坊堵塞、运行缓慢且gas费过高。在8月份网络拥堵最严重的时候，如果用户在gas limit为21,000以及gas
费为440gwei时提交一笔标准的ETH交易，那么很可能在30分钟以内完成交易，需要4.35美元的成本。

![](https://i.ibb.co/w0sr0Rq/eth2-everything-1-82b741de01.jpg)

网络拥堵情况如图所示  

假设读者现在想要尝试一些热门的、新的DeFi协议，但只想投入较小的数额的话，实际上没什么意义。因为交易费可能要比用户想要投入的ETH或者其他代币的价格要更高。

## 目前的局限性

目前，以太坊网络每秒大概只能处理15笔交易，相较于网络的庞大需求，每秒交易处理量实在是太少了。除此之外，当前的区块生成以及交易验证方式是不可持续的——据估计，以太坊网络的年电力消耗都快[赶得上哥斯达黎加](https://digiconomist.net/ethereum-
energy-consumption/)了。

Eth2这一网络的巨大升级，也被称作Serenity，旨在解决以上提到的问题，并将其视为长期目标。这次大规模升级包括多个阶段，将逐个部署，旨在以一种安全、高度去中心化的方式对区块链进行扩容。

  

# Eth1:PoW (工作量证明)

当前，以太坊网络使用PoW共识机制，许多其他区块链如比特币也采用该共识。矿工们处理待定交易并且因此获得奖励。由于以太坊网络难度设置，矿工通过生成区块来处理这些交易需要大量的算力。

## 为什么这种系统不是最好的

从本质上说，只要愿意，每个人都可以成为网络上的一名矿工，但从中获利的机会微乎其微。想要在以太坊网络上挖矿获利需要购买足够多的硬件，而其价格远超过挖矿提供的激励。因为要考虑许多成本，例如电力成本、硬件的初始成本、矿池的费用，甚至在一些司法管辖区还要缴税。

PoW系统的意义在于使得网络的安全性得以保障，因为攻击者往往需要无比庞大的算力才能对网络造成损害，也就是说需要更加高的成本来购买硬件。然而，考虑到以太坊的价值，攻击网络的动机仍然存在。

![](https://i.ibb.co/NNw2K25/eth2-everything-2-40ccf8a982.png)

莱斯利犀牛，Eth2 launchpad吉祥物 来源: https://medalla.launchpad.ethereum.org/  

# Eth2:PoS (权益证明)

PoS并不需要像PoW那样需要庞大的算力才能保障网络安全。

Staking指的是ETH持有者通过质押一笔ETH来成为网络的验证者。验证者通过软件客户端运行节点，工作包括确认和验证交易，以及如果被选择了，验证者将在区块链上创建新的块。

验证者能否验证新的区块或者交易，取决于各种因素，比如该节点质押了多少的ETH以及质押了多长时间。

在PoS共识下，只要有32个ETH，任何人都可以参与运行网络。即便用户不够32个ETH，也可以使用消费级的电脑，加入质押池，参与网络运行。

## 如果算力不那么重要，如何保障网络安全？

为了防止网络被攻击，当验证者试图通过提出新的无效交易来破坏或攻击区块链时，质押的资金会因此丢失。这一过程被称为“罚没”，攻击者的大部分ETH
(可能是他们质押的所有资金) 将被罚没。一名验证者节点至少质押32个ETH，如果攻击失败的话，将会损失一笔很大的资金。

经常用于类比当前PoW系统的一种描述是：攻击者发起攻击时，以免攻击失败，必须得消耗他们整个挖矿设施，而不只是消耗平常挖矿时的电力成本。

![](https://i.ibb.co/Vt4QhhN/eth2-everything-3-15691dcc07.png)

图示：PoS vs PoS 来源：seekingalpha.com  

# 引进：分片链

简单来说，分片链就是可以在以太坊内操作的区块链。现在，每个以太坊节点在处理一笔新的交易之前都要同步整个以太坊区块链的信息。这要比实际需要更多的算力和存储空间。

## 分片的好处？

使用分片，节点可以集中关注一个分片子集，它们只需要同步这些分片的内容。也就是说，通过这种方式，节点不必存储整个以太坊区块链的内容，可以更有效地使用它们的算力，释放出更庞大的网络容量。

区块链上会有许多分片，它们以不同的方式运行着。比如，分片可以在以太坊网络中运行的情况上，同时基本遵循比特币的系统。虽然这种设计过于草率，但是可能性却无限。

## 安全性如何？

每个分片将独立运行，尽管每个分片与其他分片具有相同的安全性。这使得攻击单个分片变得非常困难，因为攻击者还得攻击其他分片。虽然分片独立运行，但它们能够彼此通信，这便是信标链从中作用的结果。

  

# 引进：信标链

在当前的以太坊网络中只有一条链，每个以太坊节点都与这条单一的链通信。然而，一旦分片上线，主网上就会有许多不同的区块链
(即分片链)，它们相互并行工作着。信标链起支配作用，确保网络中的每个分片同步相同的信息与数据——它为所有分片链提供共识。

如前所述，验证者可以验证交易，并且如果他们被选择，也可以提议新的分片区块。如果没有被选择提议新区块，验证者的工作是确保已被提议的区块无异常——对已提议的分片区块进行验证或证明。

## 共识是如何形成的？

至少需要128名验证者验证每个分片区块，这群验证者组成一个委员会。而提议以及验证每个分片区块的时帧为一个slot。该委员会每次对32个slot进行提议以及验证区块，合起来为一个epoch，之后该委员会将被解散，并将选出一组新的验证者。这样做是为了让恶意验证者无法控制新一组提议区块的最终结果。

当一个提议的分片区块从委员会中获得了足够的证明，交联 (crosslink) 将向信标链共享分片的状态，包括新区块以及其交易数据。

## 信标链的作用是什么？

信标链记录着上述全过程的所有事情，给分片区块提议者奖励ETH，并对作恶者进行惩罚
(即罚没)。当区块准备就绪且一切都运行良好时，仍然需要对其进行敲定，以防止作恶者对其进行复原。

信标链区块也被敲定之后，则认为分片区块已被敲定。完成此操作之后，其他分片将能够读取与该分片区块相关的数据。

  

# Eth2路线图

由于Eth2对以太坊来说是一次重大升级，因此将分几个阶段进行部署。尽管每一阶段都有发布的时间安排，但要注意的是，这仍需要许多不同的团队进行大量的研究工作，因此可能会比预期时间要长。

![](https://i.ibb.co/t3yxJPF/eth2-everything-4-1b75b35402.png)

Eth2路线图 来源: https://medalla.launchpad.ethereum.org/

## 阶段0：信标链

信标链是Eth2的第一个阶段。请记住：信标链本身是没有用处的，因为它主要的工作是同步分片链，而那时分片链还没有上线。

但是，信标链还负责协调验证者的质押资产。到那时已经可以通过发送ETH到智能合约中来开始质押了，但是要等到阶段1才能提款。

**这一阶段预计将于2020年 ** **发布**** 。**

## 阶段1：分片链

阶段1将实现分片链，然后可以与在阶段0中已经实现的信标链交互。这还不是分片的完整实现，因此帐户或智能合约直到第2阶段才能使用。按照预期，阶段1先有64个分片。

**该阶段预计将于2021年发布。**

## 阶段1.5：主网变为分片

到了这个阶段，系统将仍会采用PoW共识。而阶段1.5之后，以太坊网络将会成为分片，以及向PoS转变。这意味着网络上不再有矿工，取而代之的是质押ETH。

**该阶段预计将于2021年发布。**

## 阶段2：功能齐全的分片

到了阶段2，一切开始变得完整。分片能够运行智能合约，并且通过使用执行环境，能够以不同的方式构建分片。

阶段2仍处于研究阶段，许多方面仍开放讨论。该阶段的设置可能会有所改变，并且欢迎所有人参与讨论。

**该阶段预计将于2021发布，或者有可能会推迟。**

##

![](https://i.ibb.co/4J47f29/eth2-everything-5-0b87cbe439.png)

[推特链接](https://twitter.com/VitalikButerin/status/1240365047421054976?s=20)  

# 结论

Eth2发布后，网络将会更快、成本更低，为区块链带来更多的可能性。任何人都有可能成为验证者，并通过质押他们持有的ETH赚取收益，同时维持网络的稳定与安全。

这是以太坊的重大升级，我们非常建议大家参与其中。读者现在就可以参与Eth2的测试网版本了，质押测试币成为验证者。了解更多信息请访问[Medalla
launchpad](https://medalla.launchpad.ethereum.org/)。

  
  

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

