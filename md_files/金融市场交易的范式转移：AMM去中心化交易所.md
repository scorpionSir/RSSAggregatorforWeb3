[![logo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAICAYAAAD5nd/tAAAACXBIWXMAAA7DAAAOwwHHb6hkAAABj0lEQVQoz12Sv0vDQBTHT0HrD4QWRJRLi3QQOojon1JxUhcFQQeViknrJjiIglgRhW4OTiLSWXB10MnJoToI0lp6ESu1TZNc/L7LFcGDD+8u4X3y3r0wKeUUeAqwEBVYZa9amhCb0bydjbdti/vAsy0jALPYp0EZSODq91W8W2AQPGqZg9CUvkvGUv08fSEywwGESDIaoAW+QQHJbWEq+Y+mqc8OCV3wASZBzP+qJJ8ZY2JrpKgqMvk8Yh8kvL6b6sZ+WZicki/BIBgFUVCk5ywsTr4ikvxI+l4F+w20e21bcQiNGUiZ2OZdSGLYr+jW9+hcw3NUx/DBY6pSCcELZCQ8RMtvOK+K9aErO5ugCqdJCDESVVzSwgMSQhLRwjMl1C1Xw+H4Mf/zPQFhxN5J3qrEbGJRmGMDwjIMYfF+yDNauK+FvVp4qlqG6F4PpY3goMIWxebdiVdbi1CiDC+dtwBdfmcA+X/CQqflFGQP6nf5+20C6blB4yYnRW7chcihCYbwFk0ZzAES9eiIq+DiFyR9m3ZUxiupAAAAAElFTkSuQmCC)![logo](/static/9c635c914229a850d1a9fd284014bdd0/65e33/eco_logo.png)](/)

  * [新闻资讯](/)

  *   * [零时学院](/c0llege)

  * [开发者门户](/develop)

  * [生态漫游](/ecos)

Ξ

Search by [](https://www.algolia.com/?utm_source=react-
instantsearch&utm_medium=website&utm_content=&utm_campaign=poweredby)

## 金融市场交易的范式转移：AMM去中心化交易所

AMM自动做市商模式给DeFi带来了巨大流动性，然这种模式下又会有怎样的风险？

* * *

C

Chainlink 2020-08-25

来源 | [Chainlink](https://medium.com/bollinger-investment-group/constant-
function-market-makers-defis-zero-to-one-innovation-968f77022159)

前言：流动性问题一直以来都困扰着去中心化交易所，自动做市商模式的不断创新，给DEXs带来了新的机遇和挑战。本文介绍了几种AMM类型，以及他们所具有的优缺点。

![AutomatedMarketMakerDEXs.png](https://i.ibb.co/v43Dwr1/Automated-Market-
Maker-DE-Xs-993a0729a5.png)

基于自动做市商制度 (AMM) 的去中心化交易所已成为DeFi领域里最有影响力的创新之一。这些交易所为各种不同的代币提供开放的链上流动性。

AMM从根本上改变了用户交换加密货币的方式。交易双方都没有使用传统的买/卖订单簿，而是采用链上流动资金池预先融资的资金。流动资金池允许用户以完全去中心化和非托管的方式实现无缝交换链上代币。流动性提供者
(LP) 根据其在资金池中所占份额的百分比，获得一定的被动收入，即交易费用。

在本文中，我们将探讨AMM的工作原理，仔细分析其固有的问题，以及研究解决这些主要障碍的解决方案。以下是一些关键要点：

  * 有几种AMM类型：恒定总和做市商 (Constant Sum Market Maker，简称CSMM)，恒定平均值做市商 (Constant Mean Market Maker，简称CMMM)，以及先进的混合常数函数做市商 (Constant Function Market Makers，简称CFMM)。

  * 而AMM面临的挑战包括：无常损失 (impermanent loss)、多代币敞口、低资本效率。

  * Bancor、Uniswap、Curve等交易所通过提高资本效率、降低波动风险以及提供更多的资本部署选项，来使得AMM对大型的流动性提供者更加有吸引力。

  * 借用Chainlink预言机，Bancor即将发布的v2版本，旨在首次解决波动性代币的无常损失问题。

通过给大家提供一个更加全面的分析，希望DeFi用户们可以从中获益，更好地了解AMM面临的挑战以及其带来的创新，使得去中心化流动性充分发挥其潜力，为DeFi以及未来更加广阔的金融世界打好地基。

  

# 概述何为自动做市商 (AMMs)

做市商 (Market Makers)
指的是负责在交易所上提供报价行为的实体，否则，如果没有交易活动，交易所将会失去流动性。做市商为了赚取收益，从自己的账户买入和卖出资产。他们的交易活动为其他交易方创造流动性，降低大型交易的滑点。

自动做市商 (Automated Market Makers) 则使用“Money
Robots”这一算法，在像DeFi这样的电子市场内模仿做市商的报价行为。尽管不同的去中心化交易所设计不同，但基于AMM制度的去中心化交易所一直以来都具有最高的流动性和日均交易量。

常数函数做市商 (CFMMs)
是最受欢迎的AMM类别，专门为实现数字资产的去中心化交易而设计。这些使用AMM的交易所基于一个常数函数的原理实现，即资金池里交易对的总资产储备要保持不变。在非托管的AMM中，用户将交易对通过智能合约存入池中，从而交易方可以利用池中的流动性来进行代币转换。因此，不同于订单簿交易所中交易双方直接交易的模式，AMM中的交易方是与智能合约
(即存入池中的资产) 进行交易。

自2017以来，就有3种主要的常数函数做市商模式出现。

第一种类型是恒定乘积做市商 (CPMM)，并在首代基于AMM的去中心化交易所 (Bancor和Uniswap)
中得到广泛应用。CPMM基于函数x*y=k，该函数根据每个代币的可用数量 (流动性)
来确定两个代币的价格范围。如果X代币的供应量增加，那么Y代币的供应量必须减少，反之亦然，以保持乘积K恒定不变。如果将该函数绘制出来，发现这是一个双曲线，其中流动性总是可用的，但是价格会越来越高，并在两端接近无穷大。

![](https://i.ibb.co/nMQSFVd/AMM-1-aa9e9cb2d3.png)

来源：Dmitriy Berenzon

第二种类型是恒定总和做市商
(CSMM)，这是零滑点交易的理想模式，但是不能提供无限的流动性。CSMM的公式为****x+y=k****，绘制出来是一条直线。不幸的是，当这两种代币的链下参考价格不是1:1时，这种设计会使得套利者有机会耗尽其中一个资金池。该情况会破坏其中一个流动资金池，迫使流动性提供者承担损失，而交易方则不再有可用的流动性。因此，CSMM这种AMM模式并不常见。

![](https://i.ibb.co/n0hLFyR/AMM-2-316199490b.png)

来源: [Dmitriy Berenzon ](https://medium.com/bollinger-investment-
group/constant-function-market-makers-defis-zero-to-one-
innovation-968f77022159)

第三种类型是恒定平均值做市商
(CMMM)，基于这一模式的AMM可以创建两种以上的代币，并在标准的50/50分布之外进行加权。在该模型中，每个代币资金储备池的加权几何平均值保持不变。对于一个包含三种资产的流动资金池，公式如下：
_ ***(x*y*z)^(⅓)=k***_ ****。****这种模式会给池内资产带来多变的风险敞口，并可以在池内任意资产之间进行交换。

随着基于AMM模式的流动性的发展，先进的混合恒定函数做市商 (CFMM)
出现了，它结合了多种功能和参数，以达到特定的目的。如调整流动性提供者的风险敞口，或者降低交易者的价格滑点。

例如，Curve的AMM结合了CPMM和CSMM，以提供资金池的流动性，从而降低给定交易范围内的滑点。其结果是一条双曲线
(见图蓝线)，对大多数交易返回线性兑换率，而只针对大额的交易返回指数价格。

![](https://i.ibb.co/ZmjMXyg/AMM-3-d5af950307.png)

Curve 白皮书

本文其余部分将主要关注不同的AMM为了解决其关键问题会有什么不同的设计。尽管DeFi
中的第一代AMM资金池在过去两年中经历了爆炸增长，但仍然有一些障碍，影响了他们的广泛应用， **包括无常损失、低资本效率和多代币敞口等问题。**

  

# 阻碍AMM发展的一些固有问题

## 无常损失(Impermanent Loss)

流动性提供者所面临的最主要、最常见的未知风险是无常损失
(即随着时间变化，在AMM池中直接存入代币和仅仅在钱包里持有代币之间存在价值差)。只要AMM池内的代币的市场价格往任意一方偏离，就会产生无常损失。由于AMM池不能自动调整兑换率，因而需要套利者通过买入价格偏低的资产或者卖出价格偏高的资产，直到AMM提供的价格与外部市场价格相匹配。而套利者获得的利润是从流动性提供者的口袋中抽走的，给流动性提供者带来了损失。

![](https://i.ibb.co/QCC662g/AMM-4-2f9598466f.png)

  
图示：当池中交易对在价值上相对不平等时，AMM池是如何产生无常损失的。

在上面的图示中，由于其他交易所的交易活动导致了ETH的市场价格发生变化，AMM资金池中产生无常损失。而对于这种外部价格变化，AMM的内部反应是：重新调整池中的兑换率以匹配外部市场的兑换率。在这个重新调整
(即将池中的ETH换成BNT) 的过程中，AMM池中的总储备金略有下降。

之所以称之为“无常”损失，是因为只要AMM内的代币的相对价格恢复到原来那样，亏损便消失，流动性提供者将赚得的交易费作为收益保留下来。然而，这种情况十分罕见，意味着大多数流动性提供者遭受的无常损失超过他们所获得的交易费。下图显示了在考虑交易费之前，ETH/DAI
AMM池中的流动性提供者遭受的无常损失。

![](https://i.ibb.co/82yCmWC/AMM-5-ca6a38f7a1.png)

  
ETH价格从低于100美元开始，开始产生的无常损失

AMM通常要求流动性提供者存入两种不同的代币，旨在为交易双方提供相等的流动性。也就是说，流动性提供者不得不持有额外的ERC20储备资产，这意味着他们无法保持对单一代币的长期风险敞口，而是增加了多代币风险敞口。如此一来，拥有大量单一代币的团队和想要提供流动性的个人被迫购买其他资产，才能为资金池提供流动性。从而减少了他们在池中对基础代币的持有量，并且增加了另一资产的风险敞口。

## 多代币敞口(Multi-Token Exposure)

AMM通常要求流动性提供者存入两种不同的代币，旨在为交易双方提供相等的流动性。也就是说，流动性提供者不得不持有额外的ERC20储备资产，这意味着他们无法保持对单一代币的长期风险敞口，而是增加了多代币风险敞口。如此一来，拥有大量单一代币的团队和想要提供流动性的个人被迫购买其他资产，才能为资金池提供流动性。从而减少了他们在池中对基础代币的持有量，并且增加了另一资产的风险敞口。

###

## 低资本效率

AMM需要大量的流动性，才能达到基于订单簿 (order book)
模式的交易所那样的滑点水平，在这一点上其饱受诟病。这是由于AMM里大部分流动性仅在定价曲线开始转向指数曲线时可用。因此，由于滑点较高，理性的交易者不会使用大部分流动性。

AMM流动性提供者无法决定提供给交易方的价格，这使得有些人把AMM称为“懒惰的流动性”，因其利用率低且供应不足。然而，订单簿交易所的做市商可以精确控制他们想要购买和出售代币的价格点位。这带来了高资本效率，但同时要求其积极参与以及监督流动性的供给。

## 改善MM的先进解决方案

现在一些创新项目的新设计模式正解决着第一代AMM所具有的大多数局限。

## 高资本效率和低滑点的AMM

正如前面部分所提到的那样，混合常数函数做市商 (CFMM) 只有在流动资金池到达界限时，滑点才能达到极低值，通过兑换率曲线 (大多数是线性和抛物线的)
表现出来。尽管这种模式下，由于资本利用率提高了，流动性提供者可以赚更多的费用 (尽管每笔交易的费用较低)，但是套利者仍然可以在资金池重新调整的过程中获益。

Curve交易所内提供代币之间的低滑点交换，这些代币具有相对稳定的1：1兑换率。这意味着它的解决方案主要是为了稳定币设计的，尽管他们最近上线了一些可以进行稳定交易的代币对，比如打包版本的比特币
(renBTC和wBTC)。

Bancor
V2通过类似的机制将这种低滑点模型扩展至波动性资产，该机制可动态地更新池的储备权重，以保持储备池的价值为1：1的比率。此解决方案可在相同价格区域内扩大流动性，同时保持激励套利者采取行动重新平衡资金池。

## 减少无常损失

Bancor想要在其即将发布的V2版本中首次解决波动性代币的无常损失问题。Bancor
V2通过使用锚定的流动性储备，保持其AMM储备的相对价值不变，从而降低了出现无常损失的风险。直到最近，这都是通过保持恒定1：1价格比率的镜像资产来实现的。但是Bancor
V2使用Chainlink的预言机将这种概念应用到兑换率多变的资产。这种解决方案将成为AMM利用非稳定币数字资产的重大突破，因为它可以降低流动性提供者的风险。

通过使用Chainlink预言机，Bancor
V2池能够保持准确的兑换率，即使代币的定价受外部市场价格变化影响而偏离。有了预言机，兑换率不再由套利者决定，而是由预言机提供价格更新，调整AMM的权重，因而内部兑换率与外部市场价格相匹配。这样做的好处是，套利者不再以“无常损失”的形式从流动性提供者的口袋里抽走利润。

![](https://i.ibb.co/QQ3Zw3D/AMM-6-f94eccf4e9.png)

图示：市场价格改变后，Bancor V2如何使用Chainlink预言机来避免无常损失。

相反，套利者只需在AMM池中平衡代币分配，以应对代币交易。Bancor
V2始终鼓励流动资金池恢复平衡，因为权重较低的储备池的流动性提供者赚取更高的投资回报率，直到AMM池调整到50/50的权重便恢复正常。总的来说，用户和代币团队都对其存入的流动性资金更有信心，相信其能够通过交易费用产生利润，并且不会常规的市场价格波动而贬值。

## 多代币敞口

Uniswap
V2允许任意的ERC20代币和其他任意ERC20代币配对，流动性提供者不再必须面临ETH风险敞口。这使得流动性提供者灵活地保持更加多样化的ERC20代币头寸组合，并为交易创造更多潜在的流动性池组合，以从中获得流动性。

Bancor
V2更进一步，它去掉了必须存入两种流动性资产的硬性要求，使得流动性提供者保持了单一代币的风险敞口。通过Chainlink预言机来追溯流动性储备池的价格，用户可以在AMM中保持对任意单个代币的风险敞口，即保持对任意ERC20代币的100%的风险敞口，或对BNT代币100%的风险敞口，或这两者之间的任意分配。

对于那些希望对其首选资产拥有100%的风险敞口的加密货币投资者来说，这是最理想的选择，尤其是在想要减轻无常损失的情况下。这可能会吸引想要在AMM上提供低风险流动性且无需购买额外资产的代币团队和投资基金。

  

# AMM的未来创新

从Bancor到Uniswap再到Curve等等，AMM技术正在为获得任意数字资产的即时流动性带来了新的可能性。AMM不仅为缺乏流动性的市场提供了报价，而且还是以一种高度安全、全球可访问以及非托管的方式进行的。

尽管AMM已经经历过了爆炸式的增长，但是这些围绕提高资本效率、改善多资产池和减少无常损失的创新，为吸引传统市场里更庞大的流动性提供者提供了基本的基础设施。随着资本利用风险越低以及更加符合用户要求，DeFi已准备好进行大规模的融资行为。

  

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

