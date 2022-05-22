[![logo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAICAYAAAD5nd/tAAAACXBIWXMAAA7DAAAOwwHHb6hkAAABj0lEQVQoz12Sv0vDQBTHT0HrD4QWRJRLi3QQOojon1JxUhcFQQeViknrJjiIglgRhW4OTiLSWXB10MnJoToI0lp6ESu1TZNc/L7LFcGDD+8u4X3y3r0wKeUUeAqwEBVYZa9amhCb0bydjbdti/vAsy0jALPYp0EZSODq91W8W2AQPGqZg9CUvkvGUv08fSEywwGESDIaoAW+QQHJbWEq+Y+mqc8OCV3wASZBzP+qJJ8ZY2JrpKgqMvk8Yh8kvL6b6sZ+WZicki/BIBgFUVCk5ywsTr4ikvxI+l4F+w20e21bcQiNGUiZ2OZdSGLYr+jW9+hcw3NUx/DBY6pSCcELZCQ8RMtvOK+K9aErO5ugCqdJCDESVVzSwgMSQhLRwjMl1C1Xw+H4Mf/zPQFhxN5J3qrEbGJRmGMDwjIMYfF+yDNauK+FvVp4qlqG6F4PpY3goMIWxebdiVdbi1CiDC+dtwBdfmcA+X/CQqflFGQP6nf5+20C6blB4yYnRW7chcihCYbwFk0ZzAES9eiIq+DiFyR9m3ZUxiupAAAAAElFTkSuQmCC)![logo](/static/9c635c914229a850d1a9fd284014bdd0/65e33/eco_logo.png)](/)

  * [新闻资讯](/)

  *   * [零时学院](/c0llege)

  * [开发者门户](/develop)

  * [生态漫游](/ecos)

Ξ

Search by [](https://www.algolia.com/?utm_source=react-
instantsearch&utm_medium=website&utm_content=&utm_campaign=poweredby)

## Vitalik：Gitcoin Grants第六轮回顾

本轮总计捐赠和匹配金额超40万美元，日趋成熟的二次方融资又面临怎样的挑战？

* * *

VB

Vitalik Buterin 2020-08-03

来源 | [Vitalik Buterin’s
website](https://vitalik.ca/general/2020/07/21/round6.html)

  

Gitcoin Grants第六轮已经结束，总计 **695个项目** 接收到来自 **1,526位捐赠者** 的 **227,847美元** 以及
**175,000美元** 的匹配金额。本轮的参与项目主要分为三个类型：常规类型包括技术和社区
(更名自“媒体”以覆盖更大范围)，以及第六轮的特殊类别Crypto For Black Lives。

以下是本轮Grants的结果，我们先来看看技术和社区项目的收获：

![](https://i.ibb.co/9gS21ds/git1-77a6d35072.jpg)

![](https://i.ibb.co/ngMVZkw/git2-a90f16a4e9.jpg)

##  

# 收入稳定性

在上一轮中，我提出的一[个顾虑](https://vitalik.ca/general/2020/04/30/round5.html)就是
**获赠方如何维持稳定的收入**
。试图通过二次方融资维持生计的参与者希望在收入稳定性方面得到一定保障，即他们不会因为捐赠者们突然集体“移情别恋”而在下一轮捐赠中颗粒无收。

第六轮采用了两种机制，尝试为获赠方提供稳定收入：

  1. 添加“购物车”界面，能够同时进行多笔捐赠，其中附带显眼的“重复上一轮捐赠”功能
  2. 增加一条规则，匹配金额不仅仅以该轮所获得的赠款来计算，而会“结转”上一轮赠款的1/3。(假如你上一轮捐赠了10美元，那么匹配计算公式就会假设你在上一轮中捐赠10美元并且将在本轮捐赠33美元)

很显然，第一点成功达成了增加捐赠总量的目标，但很难去衡量其是否保障了获赠方的收入稳定性。而第二点则比较容易衡量，因为我们能看到实际的匹配金额数据，也能看到结转1/3之前的匹配金额本应是多少。

技术类别：

![](https://i.ibb.co/x7fBwRf/git3-5f3c0397f1.png)

社区类别：

![](https://i.ibb.co/Jdk94ZX/git4-20466d8e6f.png)

很显然，与我们预想得差不多，规则有助于减弱波动性。尽管如此，也会有人反驳说这个结果微不足道：也会有人说这与从第N轮中获得部分收益然后将其转移至N+1轮没有什么区别
(例如新的EIP-1559社区基金获得的捐赠比预期要少)。当然，从数字上来看，收入确实更加“稳定”，但是项目可以通过每轮2/3的收入来为自己提供稳定性，继而在之后收入陡降时能够使用剩余的1/3。既然项目有能力为自己提供稳定性，为什么二次方融资
(quadratic funding) 机制为什么还要煞费苦心提升设计复杂性来为项目提供稳定性？

我的直觉是可能在下一轮中沿用“重复上一轮捐赠”，然后停用1/3结转功能，看看结果如何。数据显示，即使没有结转功能，媒体分类也能维持足够的稳定性。而技术部分波动性较大，仅仅是因为EIP
1559社区基金的突然加入；弄清楚这种情况的普适性也是试验的一部分。

##  

# EIP 1559社区基金

本轮中一大出乎意料的赢家当属EIP 1559社区基金。 **EIP 1559
([EIP提案](https://github.com/ethereum/EIPs/issues/1559)/[FAQ](https://notes.ethereum.org/Wjr1SnW-
QaST7phX9C5wkg?view)/[原始论文](https://ethresear.ch/t/draft-position-paper-on-
resource-pricing/2838))
是一个重要且意义深远的费用市场改革提案**，旨在提升用户在以太坊上的交易体验、提高经济效率、提供协议内gas费预言机并且销毁部分手续费。

这个提案令许多以太坊社区成员感到激动，而现状是目前用于实现该提案的资金非常之少。这个Gitcoin grant就是社区为解决这个问题所作出的努力。

这项grant收获了一些大额赠款，包括我和Eric Conner各自捐出的2400美元。在本轮的早期，很明显能看出EIP
1559社区基金匹配额和捐赠额的比例异常之低，2万美元的赠款约匹配到4千美元资金。这是因为由于个人捐赠数额越大，说明赠款来自于少数富有的捐赠者，因此匹配资金会少于同等捐赠数量但来自更多捐赠者的项目，这是二次方融资公式的设定。

##  

# 二次方“信号”

出人意料的是，EIP 1559 grant起到了一举两得的作用。首先，EIP
1559获得了实现所需的65473美元资金。其次，**这为社区释放了一个可靠信号：**我们对于EIP
1559的需求程度究竟如何。[长久以来](https://vitalik.ca/general/2017/12/17/voting.html)，以太坊社区都没有探索到一个有效的方式来判断“社区”的需求，尤其是在面临争议的时候。

虽然[存在](https://www.etherchain.org/coinvote)代币投票这种方式，好处在于能够判断谁是“真正的社区成员”，但缺点是你在以太坊社区中的权重取决于你持有多少ETH。这是一种富人治理形式，在津津乐道的DAO代币投票中，一个持有更多ETH的成员其投票权重高于所有对立方投票者的总和
(约占20%)。

![](https://i.ibb.co/k8VgZ7s/git5-78f911fc07.png)

另一种形式则是github、reddit和twitter的评论的和投票 (也被称谑称为“proof of social
media”社交媒体证明)，这种形式虽然较为平等，但是极易操纵，没有办法证明社区成员的身份，并且经常受到“外围干涉”的诟病
(那些表示反对的用户究竟是真正的以太坊成员还是只是来搅局的bitcoiners?)。

**二次方融资则恰到好处地取长补短**
：投票需要投入一定资本，这就确保了项目的真实拥护者的投票权重高于路人，而平方根公式则确保了个别超级富豪“巨鲸”无法压倒资本较少但更为广泛的联盟。

![](https://i.ibb.co/dcG26Qr/git6-81e3f56541.png)

这也向我们抛出了一个问题：在评断社区对于以太坊协议提案的情绪时，直接使用二次方投票 (quadratic voting) 机制
(能有对提案投出赞成或反对票) 是否有意义？

###  

# “临时类别”的表现

自第五轮以来，Gitcoin Gratns每轮都设置了三个种类：技术、社区 (更名自媒体分类) 以及一些仅适用于当轮的临时类别 (guest
categories)。第五轮的临时类别是COVID relief，第六轮为Crypto For Black Lives。

![](https://i.ibb.co/Qmfjzw2/git7-d50a6f0369.jpg)

获赠最多的是Black Girls CODE，收获了匹配池中超80%的金额。我认为其原因很简单：Black Girls
CODE已经持续参与了几轮融资，存在感相比其他新进项目都要强，并且为更多的以太坊社区成员所熟知。另外，比起商业和融资，以太坊社区更“理解”帮助人们编程的重要性。

对此有一个问题是，Gitcoin当前在每轮设置一个临时分类的方式是否发挥了作用？如果答案是“没有”的话，那原因大概是：设置这些类别的初衷是非常令人钦佩的
(助力黑人社区、抗击COVID疫情)，但总的来说以太坊社区并不是这些议题的专家，我们当然也不是致力于解决这些挑战的项目的专业人士。

如果我们的目标是将二次方融资引入以太坊之外的领域，那么最合适的替代方案是设立针对这些社区的单独融资轮，<https://downtownstimulus.com/>
就是一个很好的例子。如果目标是引发以太坊社区对这些议题的关注，那么可能持续多轮会起到更大的作用。比如说“临时类别”可以持续三轮
(约六个月)，每轮8333美元的匹配资金 (同时可能会同时设立2-3个临时类别)。无论如何，我们需要对这个模型进行优化设计。

##  

# 合谋

现在我们要来看看本轮不光彩的地方了。 **在本轮中出现了前所未有的蓄意合谋以及其他形式的欺诈** 。以下是极度离谱的一些例子：

明目张胆的贿赂行为：

![](https://i.ibb.co/GTrWVLq/git8-65672295de.jpg)

冒名申请：

![](https://i.ibb.co/Vq832fg/git9-d502a4a3e5.png)

多笔捐款明显来自同一个地址：

![](https://i.ibb.co/09f2fq2/git10-a5b16387d9.png)

最大的问题在于，在不需要对每个项目进行逐例分析的情况下，通过全自动或是技术方式能够预防多少欺诈活动？如果二次方融资必须要进行成本高昂的逐项审查才能防止欺诈，那么无论在理想世界中它能带来多少益处，在现实世界中也称不上是一个很好的机制。

所幸的是，我们还是可以采取许多潜在措施来减少恶意合谋和欺诈行径。例如 **加强身份认证系统**
。在本轮中，Gitcoin增加了非强制性SMS验证，而本轮被揭露的合谋案例都是通过github认证账号产生的
(而并非SMS认证账号)。在下一轮中，增加除了github之外的验证方式 (SMS验证或是其他更去中心化的形式，例如BrightID)
是可行的。针对贿赂方面，[MACI](https://github.com/appliedzkp/maci)能够有一定的遏制作用，这使得行贿者无法得知某个项目的真实捐赠者。

冒名申请不仅仅是二次方融资面临的挑战，而这可以通过手动验证来解决。如果青睐更去中心化的解决方案，那么可以试试[Kleros](https://kleros.io/)这类系统。我们甚至都可以想象到其激励机制：每个人都可以存入一笔押金，然后将某个项目标记为欺诈，从而引发调查；如果该项目被证明是正当的，那么举报者就会失去押金，如果项目确实存在欺诈行为，那么举报者就能获得该项目所收到的一半资金。

##  

# 结语

我们还没提到本轮展露出的向好迹象：许多二次方融资中的积极行为已经稳定下来。
**我们看到有价值的技术和社区项目获得了融资；与之前几轮相比，本轮社交媒体板块的争议有所缓和；人们也越来越了解二次方融资的机制和参与方式。**

也就是说，目前该机制向我们暴露出了多种弱点和挑战，而我们也会在未来的发展中实际面临这些问题。目前还有一些挑战尚待解决，我个人尤其关注的问题是
**社区对于匹配资金流向的争议** 。总的来说，二次方融资发展至今遇到的问题比我预计得要少。

在接下来的几轮中，我建议大家对 **安全性和扩容性方面** 保持稳定关注，并寻求扩大匹配资金池规模的方式。我仍然非常期待看到有意义的公共产品获得支持！

  
  

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

