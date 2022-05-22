[![logo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAICAYAAAD5nd/tAAAACXBIWXMAAA7DAAAOwwHHb6hkAAABj0lEQVQoz12Sv0vDQBTHT0HrD4QWRJRLi3QQOojon1JxUhcFQQeViknrJjiIglgRhW4OTiLSWXB10MnJoToI0lp6ESu1TZNc/L7LFcGDD+8u4X3y3r0wKeUUeAqwEBVYZa9amhCb0bydjbdti/vAsy0jALPYp0EZSODq91W8W2AQPGqZg9CUvkvGUv08fSEywwGESDIaoAW+QQHJbWEq+Y+mqc8OCV3wASZBzP+qJJ8ZY2JrpKgqMvk8Yh8kvL6b6sZ+WZicki/BIBgFUVCk5ywsTr4ikvxI+l4F+w20e21bcQiNGUiZ2OZdSGLYr+jW9+hcw3NUx/DBY6pSCcELZCQ8RMtvOK+K9aErO5ugCqdJCDESVVzSwgMSQhLRwjMl1C1Xw+H4Mf/zPQFhxN5J3qrEbGJRmGMDwjIMYfF+yDNauK+FvVp4qlqG6F4PpY3goMIWxebdiVdbi1CiDC+dtwBdfmcA+X/CQqflFGQP6nf5+20C6blB4yYnRW7chcihCYbwFk0ZzAES9eiIq+DiFyR9m3ZUxiupAAAAAElFTkSuQmCC)![logo](/static/9c635c914229a850d1a9fd284014bdd0/65e33/eco_logo.png)](/)

  * [新闻资讯](/)

  *   * [零时学院](/c0llege)

  * [开发者门户](/develop)

  * [生态漫游](/ecos)

Ξ

Search by [](https://www.algolia.com/?utm_source=react-
instantsearch&utm_medium=website&utm_content=&utm_campaign=poweredby)

## DEFI护航员：预言机的重要性

本文分析了目前预言机存在的优缺点，并提出构建公平预言机生态的建议。

* * *

CJ

Charles J Read 2020-09-14

来源 |[ hackernoon](https://hackernoon.com/the-importance-of-oracles-in-
decentralised-finance-cannot-be-undermined-qp213xi1)

![](https://i.ibb.co/xqXWkXJ/1-d2ad0d5feb.png)

大多数关注区块链的人应该都听说过DeFi，且那些懂得如何使用它的人都明白DeFi意味着什么——但还有一方面的内容未被充分研究，那就是价格预言机以及它们对DeFi应用的影响。

> 预言机是一种第三方服务，它为智能合约提供执行所需的数据，通常与价格相关。

在探索一些新兴解决方案之前，我会先分析一些受欢迎的DeFi项目以及它们正在使用的预言机系统，比如它们的优缺点，然后给出一些关于如何构建一个公平的预言机/数据检索生态系统的建议。

传统的金融系统需要中介机构，因此会出现单点故障。他们容易滋生腐败、诈骗、安全事故等。而智能合约和去中心化网络给了我们重建这些系统的机会，它们是普通人可以企及的，且能改善建在这些系统之上的传统金融产品，尤其是借贷方面的。

  

# DeFi给我们提供新的、透明的、无须依赖中介机构的金融系统

DeFi产品的一个常见主题是它的 **混合协议**
，这些协议一方面将不稳定性排除在外，另一方面提供去中心化网络的优势。这是通过将加密资产与传统资产结合来实现的，特别是那些与锚定美元相关的。

**MakerDao**
是最为人熟知的例子，它使用混合系统来维持平均1DAI=1的比率，并要求通过锁定不稳定资产来挖DAI（价值1的比率，并要求通过锁定不稳定资产来挖DAI（价值1的比率，并要求通过锁定不稳定资产来挖DAI（价值1的代币）。还有其他混合系统使用了像“弹性供应”（supply
elasticity）这样的概念，比如Ampleforth或现在听起来有点久远的Diameter Base
Protocol。在应对需求变化上，它们通过Rebase (回基) 机制来调整流通供应量。

使用Rebase机制的目的是通过循环供给来不断平衡需求，从而保持价格稳定，但在市场处于狂热状态下，这套机制不怎么行得通，就如我们最近所经历的。Ampleforth的价格狂飙到历史最高，由于受到一堆积极的rebase措施
(即空投代币给持有者) 所影响，一旦价格开始下坡，便下跌得又快又猛。

> 预言机是整个生态的基础，因为所有的应用都依赖于精确的数据。

**Compound** 是另一种DeFi产品，它允许通过抵押品来借入和借出资产，并根据借/贷方的需求调整利率。

Compound网络由COMP持有者来治理，他们可以通过一个提议系统对网络的未来发展进行投票——持有的代币越多，投票的权重越大。这将随管理员数量的变化产生有趣的结果。

它有时基于多份预言机报告来计算平均值，如果没有那么多管理员提供数据，它可能会计算出一个错误的价格，给大量借款者/贷款者带来严重影响。

  

# 随着DeFi产品的兴起，ChainLink无疑成为了赢家

在过去的18个月里，预言机的使用出现急速的增长，一些最有影响力的DeFi团队也正在使用，包括Kyber Network、Fulcrum、Opium
Network、 Synthetix等。Chainlink的一个关键优势在于它是参考多个预言机得出价格的。Bzrx最近发生了事故，因为它只依赖Kyber
Network提供的价格数据。
这意味着，Kyber的突然下跌会造成Bzrx清算头寸的情况。而用Chainlink的话，有分散的价格数据供应，可以避免这种情况的发生。

**尽管如此，根据新加坡科技与设计大学的Bowen Liu和Pawel
Szalachowski发表的[研究报告](https://arxiv.org/pdf/2005.04377.pdf?ref=hackernoon.com)，Synthetix的ETH/USD预言机数据存在平均2%的常规价格偏差。**

虽然对目前来说这是一个高标准，但我们必须朝着更准确的价格信息和更有活力的系统努力，当然这是Chainlink正在做的事，但有良性竞争的话不是更好吗？

目前，大多数的价格流预言机都经常出现偏离实际的数据的情况。

几个百分点的偏差看上去不多，但当我们架构一个提供借贷、清算事件和利率方面信息的金融系统时，我们需要准确的数据。

  

# DeFi产品中臭名昭著的“闪电贷”或快速平仓事件经常与价格预言机有关

如果我有一个DeFi产品并将它的价格拉到，比如说是BAT在某交易所的价格，且人们正以BAT的价格借入这个DeFi产品，那么只需要在该交易所有一笔大额抛售即可清算任何杠杆BAT的头寸。

而使用多种数据流和聚合器可以大大降低有能力推动市场快速运转的捣事者带来的风险。

  

# 在DeFi预言机领域有一些新的竞争者

DIA在打造一个为智能合约提供开放金融数据的生态，并因此而闻名。它提供多种价格流，并从多个信息源获取数据，包括交易所、其他区块链、欧洲中央银行的外汇利率、ITINs
（国际代币识别代码）、[SONIA](https://www.bankofengland.co.uk/markets/sonia-
benchmark?ref=hackernoon.com)、[SOFR](https://www.investopedia.com/secured-
overnight-financing-rate-sofr-4683954) & €STR Overnight
Rates（美元的有抵押隔夜融资利率和欧元隔夜无风险利率）。

他们旨在成为“金融数据的维基百科”，这意味着社区可以以开源的形式对数据进行投票，而不是由中心委员会决定。DIA不会在内部管理、获取或验证数据，相反，这些活动都由它的持币者，通过加密经济学激励和质押它的治理币来进行。这个设计大大提升了透明度，是一个由下而上的系统，用来清理、汇总和传送金融数据给API和以太坊的预言机系统。

![](https://i.ibb.co/QJpNfBW/2-3f5bf8fcf3.png)

这个数据库可以处理各种不同的数据流，从高频交易的API，一直到高性能键值数据库中永不改变和无法访问的数据。

DIA有趣的地方在于它同时支持多种传统金融数据和加密市场数据，且能根据用户的要求定制专属的价格数据。

上文提到的由Bowen Liu和Pawal
Szalachowski发表的论文指出，像Synthetix和Compound这些应用在用的预言机系统都缺乏透明度，这导致它们难以检测出不当操作。当在一场[CryptoDiffer
](https://cryptodiffer.com/?ref=hackernoon.com)AMA中被直接问到与其他竞争者相比，DIA有什么优势时，DIA数据团队的Paul
Claudius回答：

>
> **“我们不是一个新的提供复杂价格模型的数据库，相反，我们专注于一个维基百科式的方法——每个人都可以为了社区的发展而参与和评价社区的工作。我们为数据提供者和深挖数据来源的社区成员发放我们的治理币以作激励。”**

在未来几个月里，它将会变成一个由社区来运营的DAO。我们的团队（或者更广的社区）到时可以开始基于这个数据生态创造DeFi产品，他们使用的价格流会经常接受社区的审计。

  

# 但怎么样才算是一个好的预言机呢？以下是一些评价指标

我想文章写作至此，是时候谈谈“好的预言机是怎样的”以及“我们可以怎样构建好的数据系统”。这里列举的不是全部的因素，但可以帮助读者更好地了解我们应该往哪些方向发展。

### 治理

  * **内部 vs外部** ：这款预言机是专门为某协议/应用而造的，因此受该社区的治理？还是随时可为任意一个第三方所用？

  * **计算的选择** ：谁来选择计算预言机数值的方法论？预言机的计算模型通常各不相同，根据我之前的研究，由管理员或囤票者决定预言机逻辑是有风险的。用户是否可以选择多个链上价格流，然后将它们聚合使用？

  * **预言机的变化** ：预言机本身的变化是如何被决定的？这包括新合约的发布、聚合数据方法论的改变、以及有时候会完全删除一些数据来源。有些预言机要求“管理员”来做决定。这样公平吗？

  * **数据来源** ：预言机的文档是否足够透明，用户是否可以很容易检索到预言机数据的来源？有时候这些信息可以在白皮书找到，但实时数据经常是缺失的。

  * **方法论** ：关于计算方式、数据搜寻和数据聚合的确切方法论是否可以容易检索到和是否有文档清晰说明？通常这方面的信息都很含糊。

### 透明度

  * **数据来源** ：预言机的文档是否足够透明，用户是否可以很容易检索到预言机数据的来源？有时候这些信息可以在白皮书找到，但实时数据经常是缺失的。

  * **方法论** ：关于计算方式、数据搜寻和数据聚合的确切方法论是否可以容易检索到和是否有文档清晰说明？通常这方面的信息都很含糊。

### 数据操作

  * **数据更新频率** ：预言机的数据多久更新一次？市场变化可是很快的。
  * **数据延迟** ：被测数据点以及其并入数据流之间的延迟是多久？
  * **许可证追踪** ：有关基础原始数据的许可证信息是否可用？（比如，交易所的价格数据）
  * **Gas模型** ：谁来支付gas费用以维持预言机的运行？

尽管还有许多需要考虑的因素，但当你在为你的项目选择预言机时，以上提到的都是很好的借鉴方向。预言机的生态值得我们持续关注，因为随着DeFi应用的崛起，预言机将接受更多的审查，毕竟，这些DeFi应用都要求准确可靠的数据。否则，人们可能会损失惨重。

但我鼓励人们去真正理解预言机产生的影响，并且去了解他们正在使用的应用在依赖哪些预言机的数据。

  
  

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

