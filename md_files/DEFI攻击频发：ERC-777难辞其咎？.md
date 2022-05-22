[![logo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAICAYAAAD5nd/tAAAACXBIWXMAAA7DAAAOwwHHb6hkAAABj0lEQVQoz12Sv0vDQBTHT0HrD4QWRJRLi3QQOojon1JxUhcFQQeViknrJjiIglgRhW4OTiLSWXB10MnJoToI0lp6ESu1TZNc/L7LFcGDD+8u4X3y3r0wKeUUeAqwEBVYZa9amhCb0bydjbdti/vAsy0jALPYp0EZSODq91W8W2AQPGqZg9CUvkvGUv08fSEywwGESDIaoAW+QQHJbWEq+Y+mqc8OCV3wASZBzP+qJJ8ZY2JrpKgqMvk8Yh8kvL6b6sZ+WZicki/BIBgFUVCk5ywsTr4ikvxI+l4F+w20e21bcQiNGUiZ2OZdSGLYr+jW9+hcw3NUx/DBY6pSCcELZCQ8RMtvOK+K9aErO5ugCqdJCDESVVzSwgMSQhLRwjMl1C1Xw+H4Mf/zPQFhxN5J3qrEbGJRmGMDwjIMYfF+yDNauK+FvVp4qlqG6F4PpY3goMIWxebdiVdbi1CiDC+dtwBdfmcA+X/CQqflFGQP6nf5+20C6blB4yYnRW7chcihCYbwFk0ZzAES9eiIq+DiFyR9m3ZUxiupAAAAAElFTkSuQmCC)![logo](/static/9c635c914229a850d1a9fd284014bdd0/65e33/eco_logo.png)](/)

  * [新闻资讯](/)

  *   * [零时学院](/c0llege)

  * [开发者门户](/develop)

  * [生态漫游](/ecos)

Ξ

Search by [](https://www.algolia.com/?utm_source=react-
instantsearch&utm_medium=website&utm_content=&utm_campaign=poweredby)

## DEFI攻击频发：ERC-777难辞其咎？

前车之鉴，后事之师。

* * *

PT

Provable Things 2020-04-28

来源 | [pNetwork Team](https://medium.com/@provablethings?source=post_page-----
31c62e2bc799----------------------)

译者序：DeFi协议Uniswap及dForce于4月18、19日相继受到重入攻击，损失金额高达数千万美元。有惊无险的是，dForce已追回被盗资产并归还用户。一时之间，矛头直指ERC-777代币标准。然而，ERC777
本质上作为ERC-20的扩展，目的是增加新功能从而提升用户体验。我们是否真的要因噎废食？DeFi又应该如何突破安全瓶颈？

![](https://i.ibb.co/HqyR97W/ERC-1-db029a5dcc.jpg)

  

仅仅只是一个周末的时间，智能合约帐户被盗金额高达数千万美元。

Uniswap的imBTC资金池[遭到黑客攻击，导致价值30万的代币丢失](https://twitter.com/tokenlon/status/1251423721476116480?s=20)。时隔不久，dForce也[遭到了类似的攻击](https://www.coindesk.com/attacker-
drains-decentralized-protocol-dforce-of-25m-in-weekend-
attack)，尽管大部分的失窃加密货币目前[已被归还](https://www.coindesk.com/dforce-hacker-returns-
almost-all-of-stolen-25m-in-crypto)。这两起事件都是利用重入攻击向量漏洞发起攻击。

有人声称ERC-777代币标准的某些函数存在漏洞是造成这两起攻击的原因。但是，重入攻击漏洞已司空见惯，尤其在[2016年的DAO攻击](https://www.coindesk.com/understanding-
dao-hack-journalists)发生期间名声大噪。因此实际上，攻击与ERC-777代币标准本身无关。

重要的是，随着这个新兴行业的发展，我们必须要认识到各种协议的优点和缺点，鼓励开放协作与争议，共同致力于提高行业标准。

怪罪于代币标准是无建设性的，并且会误导大众。旨在解决旧问题的新代币标准本身更具备安全性，却因此或许面临被质疑的风险。反之，我们要对这种不断演变的事实进行周全的分析并采取行动。

  

# ERC-777是什么？

以太坊代币即运行于以太坊之上的数字货币，在生态系统中发挥着独特而重要的作用。各个代币由其智能合约表示，其他DApp和用户与这些智能合约进行交互。

因此，以太坊引进了代币标准，以此来简化生态系统中的诸多DApp与代币之间的交互，从而提高可组合性。秉承着成为 “标准代币接口”
的目标，[ERC-20代币标准](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-20.md)最初于2015年投入开发。[此处](https://docs.ethhub.io/guides/a-straightforward-
guide-erc20-tokens/)是ERC20代币标准运作机制的相关指南。

![](https://i.ibb.co/xM5RBdY/ERC-2-328bc19fb2.png)

  

随着时间的推移，以太坊代币与生态系统建立起越来越多的联系，应用范围越来越广泛。代币的用例和应用日益增多，更加复杂的智能合约对基本ERC-20代币标准提出了更高的要求，因此其部分局限性也随之开始显现。

实际上，最初该标准是为处理基本功能性而设的，因此不适用于所有用例。

尽管当今大多数代币都遵循ERC-20标准，但仍有部分代币在此基础上根据自身需求添加自定义功能。结果，部分非标准功能 (称为 [“扩展功能
(extension)”](https://docs.openzeppelin.com/contracts/2.x/api/token/erc20) )
已添加到各个代币。

譬如，ERC-20标准不支持铸造和销毁功能，但事实上这些功能是必需的，于是便被添加为扩展功能。在某些情况下，功能需求部分重合，因此各种代币添加的扩展功能不尽相同。

ERC-20标准的这种分散性使DApp集成过程，甚至整体可组合性不必要地复杂化。为了解决这种分散性问题，社区试图就新标准达成共识。

![](https://i.ibb.co/x2Pwcjy/ERC-3-0cd7563e5e.png)

经过持续两年的[开放讨论](https://github.com/ethereum/eips/issues/777)，这项新的[ERC-777代币标准](https://eips.ethereum.org/EIPS/eip-777)于去年推出。ERC-777代币标准的功能更为强大，它
“试图对广泛使用的ERC20代币标准进行改良”，并成为其正式化的完全扩展版本。

它引入并
“明确了与代币交互所需的高级功能”，使代币持有者能够更好地控制其资产。所有ERC-777代币都向后兼容ERC-20标准，这意味着如果DApp或钱包支持ERC-777标准，那么也就支持ERC-20
标准。

ERC-20是一种简单的代币格式。正是得益于其简易性，目前已有众多项目和团队利用该标准相对轻松地构建了新的DApp，既促进了生态系统的发展，也激发了创新创造活力。
**然而，它的局限性也使其面临用户体验方面的持续挑战。**

  

# ERC-777标准旨在解决ERC-20标准固有的两个主要问题

1.ERC-20仅对以太币 (ETH)
交易做出响应。批准并转账需要进行两个步骤，这一缺点导致诸多用户体验问题。最明显的问题是，处理单个请求需要发起两笔独立的交易。
**ERC-777则能通过执行功能实现代币的转入，无需借助ETH作为媒介，从而简化了转账流程。**

  2. “用户操作失误” 导致价值数百万美元的代币丢失。用户通常将其代币发送到智能合约，而不是区块链目的地址。由于尚未界定在处理此类错误的情况下`transfer` 函数的标准行为，所以ERC-20合约无法检测到此类错误。ERC20代币标准的这一特征 “是一个软件bug，可归类为软件漏洞”。相比之下， **ERC-777智能合约能够检测到此类错误并拒绝错误的代币转账行为。**

  

# ERC-777标准与某些协议不兼容

ERC-777标准的特定函数是其独特的特征。这些函数实现了协议之间的互操作性，这对于扩展以太坊生态系统至关重要。

**但是，由于ERC-777代币标准是去年才引入的，所以这些特征可能与某些协议不相兼容，尤其是某些先前部署的智能合约。**

鉴于以太坊的快速发展以及新兴去中心化金融智能合约的日益复杂，存在不兼容性不足为奇。但重要的是，也要尽快解决协议中的这些问题，因为它们暴露在攻击向量的入侵之下。对于其他各种不兼容性来说也是一样的道理，不仅仅是针对ERC-777标准。

随着该新标准的采用率越来越高，其他项目也就必须支持ERC-777代币，或者以其他方式实施必要的安全措施，以保护自身项目免受此类攻击。不幸的是，许多项目并没有做到以上两点。

在某些情况下，例如，即使Uniswap团队公布了 V.1版本存在此问题，也只是不鼓励用户锁定其ERC-777代币到流动性池中。

Uniswap团队似乎还错误地以为，转账代币时受到重入攻击，合约仍处于安全状态。请注意，这种假设对于任何一种智能合约都不成立，但是某些协议还是将代币转账（不仅是ETH转账）错误地假定为比正常情况更安全。不幸的是，上上个周末发生的重入攻击正是操纵了此漏洞。

发起重入攻击即操纵智能合约中进行交互 (进行“交流”和互操作) 的函数对合约进行攻击。例如，用户兑换其代币时或许会涉及三个智能合约；智能合约A
(一种dApp或协议如Uniswap)与智能合约B (代币智能合约如imBTC，或另一种dApp或协议) 进行交互，然后智能合约B与智能合约C
(任何能够由黑客创建，只为盗取资金的智能合约) 进行交互。

![](https://i.ibb.co/VxnLG6J/ERC-4-dfb2699d8e.png)

如果智能合约C受攻击者劫持，它可以发送代币请求，但会伪造收到资金的确认信息。发送代币至智能合约C的请求仍然执行，但是攻击者可以继续假装从未收到代币。由于这是一个自动化过程，因此无法进行干预，除非用户意识到正在受到攻击并终止合约。

  

# 前车之鉴

这种攻击向量暴露在被攻击的风险下。作为以太坊互操作性的一项关键特征，它可以通过多种方式加以操纵。代币智能合约也是发起重入攻击的工具之一。最近发生的imToken/Uniswap和dForce攻击就是如此。

**我们不能因噎废食，攻击事件并不足以为DeFi时代划上句号，甚至不足以使我们质疑ERC-777代币标准的安全性。**

ERC-777代币的数量正在稳定增长。诸如Augur之类的团队正在决定将其代币格式从ERC-20升级为ERC-777。
**随着DeFi行业的发展，我们必须了解使用此类创新技术的风险以及如何将风险降至最低，这一点至关重要。**

这种漏洞的优点在于，它属于代码错误，而非传统金融行业中普遍存在的固有的系统性缺陷——腐败、过度监管和排斥性。通过DeFi，我们已经将信任从人类转移到代码身上。因此，尽管总会有人存心利用代码，但是至少代码本身并没有从人类身上获利的企图。当今的经济体系却并非如此。

作为DeFi行业的一份子，我们应该不断改进标准，使每次迭代都变得更强大、更安全。目前，ERC-777具有一系列优势，能为代币持有者和DApp带来价值。**我们应该始终致力于改进ERC-777标准以及今后所有的标准。**DeFi要脱颖而出，突破口正在于此。

![](https://i.ibb.co/vDSghk3/ERC-5-4404f1e47d.jpg)

  
  

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

