[![logo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAICAYAAAD5nd/tAAAACXBIWXMAAA7DAAAOwwHHb6hkAAABj0lEQVQoz12Sv0vDQBTHT0HrD4QWRJRLi3QQOojon1JxUhcFQQeViknrJjiIglgRhW4OTiLSWXB10MnJoToI0lp6ESu1TZNc/L7LFcGDD+8u4X3y3r0wKeUUeAqwEBVYZa9amhCb0bydjbdti/vAsy0jALPYp0EZSODq91W8W2AQPGqZg9CUvkvGUv08fSEywwGESDIaoAW+QQHJbWEq+Y+mqc8OCV3wASZBzP+qJJ8ZY2JrpKgqMvk8Yh8kvL6b6sZ+WZicki/BIBgFUVCk5ywsTr4ikvxI+l4F+w20e21bcQiNGUiZ2OZdSGLYr+jW9+hcw3NUx/DBY6pSCcELZCQ8RMtvOK+K9aErO5ugCqdJCDESVVzSwgMSQhLRwjMl1C1Xw+H4Mf/zPQFhxN5J3qrEbGJRmGMDwjIMYfF+yDNauK+FvVp4qlqG6F4PpY3goMIWxebdiVdbi1CiDC+dtwBdfmcA+X/CQqflFGQP6nf5+20C6blB4yYnRW7chcihCYbwFk0ZzAES9eiIq+DiFyR9m3ZUxiupAAAAAElFTkSuQmCC)![logo](/static/9c635c914229a850d1a9fd284014bdd0/65e33/eco_logo.png)](/)

  * [新闻资讯](/)

  *   * [零时学院](/c0llege)

  * [开发者门户](/develop)

  * [生态漫游](/ecos)

Ξ

Search by [](https://www.algolia.com/?utm_source=react-
instantsearch&utm_medium=website&utm_content=&utm_campaign=poweredby)

## Eth 1.x：无状态以太坊新思路“reGenesis”

reGenesis和静态状态网络为“无状态以太坊”目标提供了一种可行的新思路。

* * *

GI

Griffin Ichiba Hotchkiss 2020-08-28

来源 | [Ethereum Blog](https://blog.ethereum.org/2020/01/28/eth1x-files-the-
stateless-ethereum-tech-tree/)

  

![1.x封面.png](https://i.ibb.co/7gcsNnN/1-x-0d3dc30bff.png)

  

这周我们将对[技术树 (tech tree)](https://github.com/ethereum/stateless-ethereum-
specs/blob/master/techTree.md)
进行更新，为以太坊1.x研发添加一些新的主要里程碑，这些里程碑并不算是无状态以太坊的完整实现，而是我们在中期能够合理实现的目标。

其中最重要的更新是Alexey的reGenesis提案。虽然这是远未规范化的更新，但是从研发的角度来看，
**reGenesis为“完全无状态”的终极目标提供了一种更保守更切实可行的路径。** 在其他方面与reGenesis互补的技术是 **静态状态网络**
，能够帮助在比特流 (bittorrent) 式的基于DHT的网络中传播状态快照和历史链数据。

同时，一些距离我们比较近的目标已经在为EIP化做准备，例如 **代码分块 (code merkleization) 和状态二进制树。**
在本文中，我会为大家阐明已经实现的进展，并且附上链接，以便读者深入了解感兴趣的领域。

![1.x19.png](https://i.ibb.co/pjLWzmk/1-x19-dad107bd13.png)

##  

# 二进制树

目前以太坊使用十六叉[Patricia默克尔树](https://eth.wiki/en/fundamentals/patricia-
tree)来编码状态，但如果 **转变为二进制式会带来显著的效率提升，**
尤其是在见证大小这个方面。对以太坊状态进行完全重新编码需要制定新范式，以及清晰的过渡策略。最后，还需要决定是否将智能合约代码分块，并且将该过程合并到二进制树过渡中还是作为独立更新。

###  

## 二进制树范式

与当前的十六叉树结构相比，二进制树的概念要简单一些。十六叉树从树根遍历到子节点有十六条可能路径，二进制树只有两条。
**随着状态树的重新规范，我们有机会解决以太坊运行五年以来显著的低效问题。** 此外，我们也有机会使状态更适应现实世界中数据库编码的性能挑战
(在[上一篇有关状态增长的文章](https://blog.ethereum.org/2019/12/30/eth1x-files-state-of-
stateless-ethereum/)中有提到)。

有关正式二进制树规范和分块规则的讨论可以参见[ethresearch](https://ethresear.ch/t/binary-trie-
format/7621).

###  

## 过渡到二进制树

重要的不仅仅是二进制树范式这个目的地，旅途本身也非常有价值！在理想的过渡过程中，不会对网络的交易处理产生干扰，也就是说客户端将需要在处理每十五秒出现的新区块的同时构建新的二进制树。

目前看起来最有希望的过渡策略被称为[ **“覆盖”法**](https://ethresear.ch/t/overlay-method-for-hex-
bin-tree-
conversion/7104)，该方法部分基于geth的新快照同步协议。总的来说，新的状态改变会以二进制范式被添加到现有的十六叉树中，也就是说在过渡过程中会存在二进制和十六进制混合体。不受影响的状态会被转换为后台处理。一旦完成转换，这两层会被合并到一个二进制树中。

请务必注意，客户端多样性在二进制转换过程中也起到了非常重要的作用。每个客户端将需要实现自己的过渡版本，或是依靠其他客户端进行转换，然后在另一端等待新的树。

这需要我们“三思而后行”，所有客户端需要协同工作来进行测试并协调转换。出于安全性的考量，在过渡过程中网络有可能需要短暂停止服务
(例如挖出一些空块)，但是目前就任何具体计划达成共识还为时尚早。

  

## 代码分块

以太坊状态树的很大一部分由智能合约代码组成，约占50GB状态的1GB左右。所有用于智能合约交互的见证 (witness)
都必须提供其交互的代码，以计算codeHash, 而这可能产生大量额外数据。

**代码分块 (Code Merkleization) 旨在将合约代码切分为较小的块，然后将codeHash替换为另一个默克尔树根。**
这种方式使得我们可以使用参考哈希来替代见证中潜在的大部分智能合约代码，从而省去数千字节的见证数据。

进行代码分块有多种方式，按复杂度来看，比较简单的就是通用分块 (例如每块大小64字节)，而较为复杂的方式就是基于Solidity
functionId或JUMPDEST指令的静态分析。最优的代码分块策略最终还是取决于是否适用于从主网收集到的真实数据。

  

# reGenesis

要了解reGenesis提案的最佳去处是[@mandrigin给出的解释](https://medium.com/@mandrigin/regenesis-
explained-97540f457807)，以及[@realLedgerwatch提交的完整提案](https://ledgerwatch.github.io/regenesis_plan.html)，概括来说reGenesis基本可以说是“区块链的大扫除”。
**完整的状态将从概念上分为“活跃”和“非活跃”状态** 。整体“活跃”状态会按一定周期被停用，然后新的交易会再次几乎从零开始建立新的活跃状态
(因此被称作“reGenesis”)。

如果交易需要之前的状态，将会提供一个见证，这非常类似于无状态以太坊所需的证明：证明状态更改与某个非活跃状态相一致的默克尔证明。如果一笔交易需要状态的“非活跃”部分，它将自动将其转变为为“活跃”状态
(无论交易是否成功)，这该部分将会留至下一次reGenesis发生。

这样做的一个好处在于，在使用状态时创建一些经济限制，而实际上不会删除任何状态。其次，如果交易发送方盲目地反复试图交易，则无法生成见证。

关于reGenesis的意义，它使得以太坊朝着终极的无状态目标跨进了一大步，并且避开了要实现无状态面临的最大挑战，即
**EVM执行时如何计算见证的gas。**
同时它还使得某个版本的交易见证能够在网络中传播，让更轻量级的客户端和dapp开发者能够有更多机会熟悉无状态范式和见证生成。

reGenesis之后“真正的”无状态性就只是程度上的问题了：无状态以太坊其实只是每个区块之后的reGenesis。

  

# 状态网络

![1.x20.jpeg](https://i.ibb.co/9vqHffc/1-x20-ae3f0c21f9.jpg)

从一开始，网络协议的优化只是技术树中的一个“支线任务”，但随着reGenesis进入无状态以太坊的版图，为分享以太坊链数据 (包括状态)
探索替代的网络原语也成为了主线任务。以太坊当前的网络协议是一个整体，但事实上有多种类型的数据能够通过不同的“子网络”来进行共享，而这些“子网络”能够满足不同的需求。

之前在无状态会议中讨论到这个话题时，我们称其为[“三个网络”](https://ethresear.ch/t/stateless-ethereum-
may-15-call-digest/7420)，[基于DHT](https://ethresear.ch/t/stateless-ethereum-
may-15-call-
digest/7420)的网络能够更高效地服务于不常改变的数据类型。随着reGenesis的引入，“非活跃”状态能够被纳入这类不常变化的数据，从理论上来说也就能够适用于
**比特流式的swarm网络** ，而不是当前由全节点进行逐条广播。

自上一次reGenesis之后，在网络中传播不变状态的网络就是静态状态网络 (static state network)，可以[基于devp2p库
(以太坊网络协议) 中新的Discovery
v5.1规范](https://github.com/ethereum/devp2p/pull/157)进行延展。

之前类似[Merry-go-Round sync](https://ethresear.ch/t/merry-go-round-
sync/7158)和更为成熟的[SNAP protocol](https://blog.ethereum.org/2020/07/17/ask-
about-geth-snapshot-
acceleration/)，可用于同步活跃状态，是迈向完全分布式动态状态网络的重要步骤，使得客户端能够快速同步完整状态。

  

# 结语

关于无状态以太坊技术树每个分支更为细致和技术化的说明，读者可以参阅[无状态以太坊规范库](https://ethresear.ch/t/merry-go-
round-sync/7158)，也能在Eth1x/2 R&D
Discord中对所有这些话题进行讨论，如果想加入可以在ethresear.ch上要取邀请。如果有任何反馈和建议，请在推特联系@gichiba或@JHancock。

  
  

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

