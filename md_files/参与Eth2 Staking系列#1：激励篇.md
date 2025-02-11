[![logo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAICAYAAAD5nd/tAAAACXBIWXMAAA7DAAAOwwHHb6hkAAABj0lEQVQoz12Sv0vDQBTHT0HrD4QWRJRLi3QQOojon1JxUhcFQQeViknrJjiIglgRhW4OTiLSWXB10MnJoToI0lp6ESu1TZNc/L7LFcGDD+8u4X3y3r0wKeUUeAqwEBVYZa9amhCb0bydjbdti/vAsy0jALPYp0EZSODq91W8W2AQPGqZg9CUvkvGUv08fSEywwGESDIaoAW+QQHJbWEq+Y+mqc8OCV3wASZBzP+qJJ8ZY2JrpKgqMvk8Yh8kvL6b6sZ+WZicki/BIBgFUVCk5ywsTr4ikvxI+l4F+w20e21bcQiNGUiZ2OZdSGLYr+jW9+hcw3NUx/DBY6pSCcELZCQ8RMtvOK+K9aErO5ugCqdJCDESVVzSwgMSQhLRwjMl1C1Xw+H4Mf/zPQFhxN5J3qrEbGJRmGMDwjIMYfF+yDNauK+FvVp4qlqG6F4PpY3goMIWxebdiVdbi1CiDC+dtwBdfmcA+X/CQqflFGQP6nf5+20C6blB4yYnRW7chcihCYbwFk0ZzAES9eiIq+DiFyR9m3ZUxiupAAAAAElFTkSuQmCC)![logo](/static/9c635c914229a850d1a9fd284014bdd0/65e33/eco_logo.png)](/)

  * [新闻资讯](/)

  *   * [零时学院](/c0llege)

  * [开发者门户](/develop)

  * [生态漫游](/ecos)

Ξ

Search by [](https://www.algolia.com/?utm_source=react-
instantsearch&utm_medium=website&utm_content=&utm_campaign=poweredby)

## 参与Eth2 Staking系列#1：激励篇

以太坊基金会博文详解eth2验证者的惩罚和激励机制。

* * *

CB

Carl Beekhuizen 2020-01-17

来源 | [Ethereum Blog](https://blog.ethereum.org/2020/01/13/validated-staking-
on-eth2-1-incentives/)

  

![质押1.png](https://i.ibb.co/WyP26VY/1-8cf3398852.png)

  

感谢Joseph Schweitzer和Danny Ryan的审校。

又见面了！在[上期开篇文章](https://news.ethereum.cn/validated-staking-on-
eth2-0/)中我们讨论了eth2的设计理念，本文将透过设计理念主要谈谈eth2的激励机制。更确切地说，我们将探析在eth2中举足轻重的激励机制，以及如何通过奖励、惩罚和罚没
(slashings)的形式得以实现。

之后我们会再谈到如何以及为何激励验证者保持在线，为何验证者离线不会被罚没等等话题。我们开始吧！

  

# 如果不是因为离线，那什么情况下会被罚没(slashings)？

罚没主要出于 **两个目的** ：(1) 使得攻击eth2的成本难以负担 (2) 查核验证者是否真正履行了职责，防止验证者消极怠惰。

对验证者进行罚没，是指如果验证者被证实存在破坏行为，其（部分）质押金将被销毁。在eth2阶段0时期，验证者主要会因为两种恶意行为被罚没：
**双重投票（double voting）和环绕投票（surround voting）** ，有关细节参见Casper FFG运行机制的论文[1]。

双重投票，即验证者在同一个epoch中对两个不同区块进行投票，这也就意味着验证者对两种不同的现实版本表示了支持。需要禁止该行为最直观的原因就是，假如验证者在区块A中发送了一笔交易a，在区块B中发送了一笔交易b，且交易a和交易b花费了等值的ETH。因此
**双重投票可以被看做是PoS版本的双花攻击** （double-spend attack）。

环绕投票也是通过罚没来惩罚恶意投票的验证者，以防止其同时创造多个不同的现实版本，避免了两个不同的链被最终确认（finalize）。具体地说，当验证者对某个现实版本进行投票，然后又对另一个版本进行投票，但并没有表明他们不再信任第一个版本，那么该验证者的这些证明（attestations）就是环绕投票。

在阶段0中，双重投票和环绕投票行为是唯一会导致验证者被罚没的情况，但之后的阶段中会增加其他规则，以确保验证者真正履行其职责，存储其签署的分片数据且使数据可用，防止验证者消极怠惰或隐瞒信息。

正确遵循协议且操作正常的验证者不会创建可能导致罚没的投票。如果出现罚没，却并未存在蓄意作恶行为，那么只会是因为bug或意外。那么出现这种情况怎么办？

为了将这种意外损失降低到最小，**被销毁的质押金会与同时段被罚没的验证者数量成一定比例。**因为如果只有数量很少的验证者进行了被罚没的行为，那么就不太可能是试图对eth2链发起攻击，而攻击成功需要大量的验证者。

因此，如果只有少数验证者被罚没，那么其行为会被认定为无心之过，惩罚力度也不会很大（最低罚没金额为1
ETH）。反之，如果大量验证者几乎同时产生不当行为，那么他们的质押金很大一部分则会被销毁（最高罚没金额为全部余额），因为这种情况会被视作针对网络的攻击行为。

被罚没的验证者将被停止继续参与协议，并且会被强制退出。如果验证者是无心之过，那么这种措施可以防止犯错的验证者一错再错，被重复罚没；如果是网络攻击的情况，则可以将恶意的验证者从协议中剔除。

  

# 离线的验证者又会怎样？

在本应该参与协议进行验证工作的时候，离线的验证者会被惩罚，而在正常情况下，离线只会使得验证者失去他们本可以通过验证工作所获取的奖励。也就是说，
**如果验证者50%以上的时间在线，他们的质押金额会随时间推移增加。**

这种机制带来的结果是，对于需要离线进行维护等工作的验证者客户端，最好是选择短时间离线，而不是采取退出协议再重新加入的方式（因为退出和进入都存在相关延迟性）。

这也就意味着，减轻了验证者在客户端备份和网络延迟上的负担，因为离线的惩罚并不那么严重。实际上，如果系统中有两个实体可以对消息进行签名，可能会带来负面影响，因为主客户端和备份客户端有可能同时在线，进而导致创建可能导致罚没的投票（即上文提及的双重投票），Cosmos的首个罚没案例[2]就是这样发生的。

这种离线惩罚机制能够成立的前提是区块正在被最终确认，即有2/3的验证者（按权益加权）在线并且其投票正在被计数。这是eth2在正常情况下应该达到的预期状态。**如果少于2/3的验证者在线，就说明eth2中发生了灾难性的错误。**在此类情况下，以太坊的共识协议（包括Casper）则无法达成共识。

  

# 如果超过1/3的验证者离线，Eth2会作何反应？

如果发生这种情况，那么这些离线的验证者就会面临inactivity leak（消极）惩罚。随着离线时间推移， **受到inactivity
leak惩罚的离线节点会被扣减余额** ，如此一来，在线验证者占验证者总数（权益加权）的比例就能够再次超过2/3，使得eth2得以继续运行协议。

诸如Inactivity
leak此类的设计，使得eth2具备从灾难性事件中幸存下来的能力。如果这种灾难性状况导致超过1/3的验证者离线，那么这些离线验证者会发现他们的余额不断被扣减至某个程度（16个ETH），到那时eth2的运行将不再需要他们的参与。

  

# 反相关性&去中心化

罚没机制和inactivity
leak（消极惩罚）机制促使验证者做出与其他验证者不同的使自身节点失效的决策。也就是说，为了确保自己受到尽可能轻微的罚没和不受到inactivity
leak惩罚，验证者应该会努力尝试和其他验证者不同的客户端失效形式。

这给所有验证者施加了压力，他们需要将作为验证者的方方面面进行去中心化，例如，如果验证者都依赖于相同的现实来源（如Infura）或是都借助AWS来托管客户端，一旦这些方面发生什么错误，验证者们会面临更为严厉的惩罚。

  

# 有这么多惩罚机制，那验证者是否吃力不讨好？

正如在上期文章中所说，**“eth2假设验证者怠惰、收受贿赂、攻击系统的情况，除非采取措施对验证者进行激励。”**上文讨论到的惩罚机制是为了防止作恶行为，但同时也需要通过奖励来激励验证者为eth2进行有益工作。验证者奖励主要分为三类：

✅ **检举者奖励**

通过提供证明，发起其他验证者罚没行为的警告，这些验证者能够因其为eth2扫除不利而获得奖励。

✅ **区块提议者奖励**

验证者会被随机地分配产生区块的任务，被选中的验证者就是“区块提议者”（proposer）。区块提议者能够通过以下方式获得奖励：

▫打包一份来自检举者的证明，且该证明证实某个验证者被罚没；

▫打包来自其他验证者的证明（attestations）

当验证者被选中提议区块时，奖励能够鼓励其向区块链提供有用信息。

✅ **证明者奖励**

证明（attestations）是表明验证者同意eth2中某个决定的投票。这类信息构成了eth2的共识基础，主要通过以下5种途径获得奖励：

  * 获取链上证明
  * 与验证者就区块链历史记录达成共识
  * 与验证者就区块链最前部分达成共识
  * 快速使证明上链
  * 在指定分片中指向正确区块

  

# 开拓验证者收益

在PoS系统中，有两种常见的验证者奖励模式： **固定奖励** （fixed rewards）和 **固定通胀** （fixed inflation）。

在固定奖励模式中，验证者通过履行职责获得固定数额的奖励，而通胀率取决于验证者数量。这种模式需要解决的问题在于如何设置回报率（reward
rate）。如果回报率过低。验证者数量会过少；如果回报率太高，则会衍生出安全性需求之外的验证行为，并且浪费资金。

因此，拥有固定通胀率的模式更受欢迎。在这种模式中，既定数额的奖励由所有的活跃验证者瓜分。这种模式的好处在于利用市场的力量来寻求合适的奖励数额，因为验证者可以根据当下的收益自行选择是否参与验证。

但这种模式也存在一定缺陷。验证者奖励有可能是不稳定的，这使得对于个人验证者来说，很难做出盈利性决策；这种模式还使得协议容易暴露在“泄气攻击”（discouragement
attack）[3]之下，受到这种攻击时，验证者会试图阻止其他验证者参与进来，以此提高自己的奖励（即便自己会受到暂时的损失）。

Eth2旨在结合两种模式的优点：**验证者的奖励与ETH质押总量的平方根成正比。**这种混合奖励模式的好处是在抑制通胀变化和验证者回报率的同时，依然能够借助市场力量来决定验证者的奖励金额。

  

# 抱最大希望，做最坏打算

Eth2激励机制的方方面面都遵循了上期文章中所阐述的协议设计理念。例如，反相关性机制有助于去中心化，inactivity
leaks（消极）惩罚有助于eth2具备从灾难性事件中幸存下来的能力……但支撑起eth2激励机制的主要理念还是：eth2假设验证者怠惰、收受贿赂、攻击系统的情况，除非采取措施对验证者进行激励。

如果有人试图用本文中提到的任何一种方式来攻击eth2，那最好做足损失大量ETH的准备，因为无论如何，攻击者都会输得一无所有。

  
  

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

