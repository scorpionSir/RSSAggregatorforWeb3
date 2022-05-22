[![logo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAICAYAAAD5nd/tAAAACXBIWXMAAA7DAAAOwwHHb6hkAAABj0lEQVQoz12Sv0vDQBTHT0HrD4QWRJRLi3QQOojon1JxUhcFQQeViknrJjiIglgRhW4OTiLSWXB10MnJoToI0lp6ESu1TZNc/L7LFcGDD+8u4X3y3r0wKeUUeAqwEBVYZa9amhCb0bydjbdti/vAsy0jALPYp0EZSODq91W8W2AQPGqZg9CUvkvGUv08fSEywwGESDIaoAW+QQHJbWEq+Y+mqc8OCV3wASZBzP+qJJ8ZY2JrpKgqMvk8Yh8kvL6b6sZ+WZicki/BIBgFUVCk5ywsTr4ikvxI+l4F+w20e21bcQiNGUiZ2OZdSGLYr+jW9+hcw3NUx/DBY6pSCcELZCQ8RMtvOK+K9aErO5ugCqdJCDESVVzSwgMSQhLRwjMl1C1Xw+H4Mf/zPQFhxN5J3qrEbGJRmGMDwjIMYfF+yDNauK+FvVp4qlqG6F4PpY3goMIWxebdiVdbi1CiDC+dtwBdfmcA+X/CQqflFGQP6nf5+20C6blB4yYnRW7chcihCYbwFk0ZzAES9eiIq+DiFyR9m3ZUxiupAAAAAElFTkSuQmCC)![logo](/static/9c635c914229a850d1a9fd284014bdd0/65e33/eco_logo.png)](/)

  * [新闻资讯](/)

  *   * [零时学院](/c0llege)

  * [开发者门户](/develop)

  * [生态漫游](/ecos)

Ξ

Search by [](https://www.algolia.com/?utm_source=react-
instantsearch&utm_medium=website&utm_content=&utm_campaign=poweredby)

## 解读：COMPOUND与YIELD FARMING

DeFi热议的Yield farming到底有何魔力让大家趋之若鹜？本文详细解读Compound以及其掀起的借贷浪潮。

* * *

JJ

Joel John 2020-07-02

来源 | [The Cipher](https://cipher.substack.com/p/contextualising-compound)

如果读者有一直密切关注市场，便会注意到**Compound和“收益
(yield)”**近期已然成为加密市场的爆点。我会在此文探讨yield的概念，它又是如何应用于DeFi的？以及如何适应当今大环境下的市场趋势？由于这部分内容面向的是更广泛的受众，如果读者对金融知识比较熟悉，可以略过下面的普及部分。

  

# 了解Yield (收益)

![](https://i.ibb.co/25ZCN6S/Compound1-cb91c00094.png)

在金融投资领域， **收益 (yield)**
是指投入一定的成本而获得的回报，通常以百分比来表示年回报在初始投资中的占比。收益还包括一年中所获得的复利。以下是一些获得收益的常见例子：

  1. 假设您投入10万美元购买房屋并出租。在一年中，能获得约1.2万美元的租金收益。扣除了维护费用和其他费用共2000美元后，您的净利润为1万美元，因此收益率为10%。而这并不包含基础资产本身的升值。

  2. 收益的另一种常见形式是投资股票产生的股息。股票的市盈率 (price to earnings) 是决定股票估值的关键因素，因为在可以用股票进行交易之前，投资者通常是依靠所持股的股利来满足日常花销。只要股息高于银行存款的收益，投资者何乐而不为。最近，由于股息下跌，股票回购已成为常态。

简而言之，“收益”(yield)
是指个人将资本存放在实体中而获得的回报。收益的高低受许多因素影响，比如投资所涉及的风险、向经纪人支付的业绩报酬、税收以及投资行为所处的法律环境。收益还受通货膨胀的影响。在印度，银行存款的存款利率约6％，且几乎没有任何风险。相比之下，新加坡的银行存款利率低于1％。造成这种差距的原因是，印度货币每年趋向于贬值。这也是资本外逃在新兴经济体中如此普遍的原因之一。

如果读者想要进一步了解资本和网络作用，我强烈建议阅读以下书籍：

  1. 《广场与高塔》 （ _Square and The Tower_ ）
  2. 《金融之王》 （ _Lords of Finance_ ）
  3. 《金钱关系》 （ _The Cash Nexus_ ）

了解了以上知识之后，我们一起来看看DeFi里的“yield”是指什么。

  

# 加密货币中的Yield (收益)

目前，所有在早期就持有大量加密货币的参与者都面临着如下挑战（i）代币可能会贬值，（ii）如何从所持代币中赚取收益。DeFi里的“收益”(yield)
就有一石二鸟的效果。大约有75％的ETH在一年内没有发生转移。一些巨鲸通常会收购大量ETH并持币观望，因为在他们的预期中基础资产本身会随着时间增值。那么可以如何变现闲置资产呢？这就是智能合约发挥作用的地方。

根据历史经验，任何基于加密货币的借贷活动都具有一定挑战性，因为一旦抵押加密货币而借出法币，赎回抵押资产的可能性极低。如果读者想了解更多背景资料，可以阅读我于2017年写下的[这篇文章](https://medium.com/outlier-
ventures-io/how-to-realize-the-potential-of-blockchain-in-developing-
economies-b94b24d6ce7c)。智能合约之所以助推了借贷和链上交易活动，是因为其能够

(i) 借助预言机跟踪价格来源，以及

(ii) 在没有人为干预的情况下实行清算。

**这意味着什么？** (i)
当MakerDAO上的贷款没有足额抵押品时，没有人会提醒借款方并要求其补充抵押品。而是系统会自动跟踪价格，并通过激励网络的用户来对借款方进行清算。

(ii) 在Curve.fi、Kyber和0x上并没有业务人员跟踪借贷订单的进行，系统会自动核对订单细节。

系统自动跟单这一功能还不够让人眼前一亮。**DeFi的强大之处在于，其能够 ** **验证货币流向以及****
决定清算价格。**而我们能够以目前的速度追踪黑客，DeFi的这一功能功不可没。那么这和收益有什么关系呢？我们还需要考虑三种推动力。

  1. 当前，加密生态系统中有大量闲置资金正期望投入使用。
  2. 用于处理交易的知识层和基础设施层已经就绪，因为最近两年来，像Maker和0x这样的团队已经对他们的系统进行了充分测试和扩容。
  3. 应用层已经趋于成熟，而应用层的活动最为频繁（我在稳定币相关文章中有所提及）

闲置资产、成熟的基础设施以及各种获得充足投资的新兴应用，三者的结合就像一场完美风暴，催生新一轮加密应用浪潮。从某种意义上说，我们正处于这场风暴中。而收益则起到吸引大众参与DeFi的作用。

![](https://i.ibb.co/dWLhyNW/Compound2-f2c013dc54.png)

当前，DeFi收益主要基于交易活动。市场始终会有以下两种需求：

（i）增加去中心化交易的流动性

（ii）从交易中获得利润。

只要DeFi可以提供有竞争力的价差 (即买入和卖出价格之间的差额) 和优于中心化交易所的贷款利率
(例如Bitmex贷款利率)，就会有寻求交易的用户需求。与中心化交易平台比如币安相比，使用DeFi可能成本会更高，因其不需要严格遵守AML / KYC规则
(即反洗钱和用户信息规则) 并且资金出入耗时更短。一旦利率或利差远高于中心化平台，考虑到其中的智能合约风险，资本巨鲸就不会继续使用DeFi了。

为什么用户接受代币贷款？最轻而易举的方式是通过做空个人借贷的资产而获得利润。当资本巨鲸贷了一笔以美元计价的BAT时，假设BAT的价格将在未来几周内下跌。也就是说，他们抵押了美元而贷出一笔加密货币，然后在去中心化交易所卖出，一旦该加密货币价格下跌，就立马回购并归还贷款。如果把贷款利率也考虑在内，贷款价格和还款价格之间的差价就是做空所得的利润。

如果碰到Maker这类包含治理的代币，还会出现活跃投资者通过出借基础资产增加投票权重。换句话说，当前加密货币贷款既可以用于治理，也可以用于价格预测。

  

## Compound浪潮

看到这里相信读者已经了解什么是收益、其在DeFi中如何运作以及获得收益的常见手段，那么现在我们就可以探讨一下为何上周大家如此关注yield
farming。自2018年以来，Compound就是一个出色的借贷平台，其代币经济模型经历了多次迭代。Compound一直以来都是MakerDAO最大的竞争对手，并在上周逐步发布了其代币。

两者的关键区别在于，Compound激励借贷双方进入compound的代币池，每天都会有代币产生，而产生的代币作为用户的奖励。与之相比，Maker代币的主要用途是投票
(而不是作为奖励)，而Aave代币主要用于减少利息支付金额。

Compound每天分发的代币价值约为86万美元 (假设[2880个代币，每个价值300美元](https://medium.com/compound-
finance/expanding-compound-governance-
ce13fcd4fe36))。由于用户个人几乎可以立即兑换compound代币并出售，因此用户普遍将大量资金转移到Compound的借贷市场以赚取收益和代币奖励。Compound的激励机制主要以
**两种关键方式** 起作用：

  1. 巨鲸可以将其闲置的USDT / USDC存入Compound平台几天，以获得Comp代币，然后可以卖出获取利润。

2.鉴于借贷双方都大量增加，小型用户也可以在几天内获得高达1％的收益。相比之下，某些国家/地区的年化收益率仅为0.1％，读者这下能明白Compound流动性挖矿现象为什么能够像火一样迅速蔓延开了吧。

下图可以或多或少地解释Compound上的用户行为。图表受Nir Eyal的《Hooked》启发。其运作方式如下：

A.巨鲸在Compound进行大额贷款/借款 B. 获得大量代币后，待其价格上涨后出售 C.
价格上涨加上大量借贷活动，随之而来的高年利率吸引了更多用户使用山寨币参与借贷 D. 由于大量借款人以期通过交易赚取利润，供应量很快就被耗光
旁注：我希望Nir Eyal不要因为盗图而起诉我。建议读者购买他最新的书[
_Indistractable_](https://www.nirandfar.com/indistractable/)，这是一本好书。

![](https://i.ibb.co/hM4yjr4/Compound3-c08b97ced7.png)

如果读者想知道这会对Compound产生什么样的影响，可以参考这段时间以来Compound平台借出的金额，并大胆猜测一下Compound是什么时候发布的代币。

![Compound4.png](https://i.ibb.co/4JrcctF/Compound4-dd09ae3850.png)

在大约两周的时间里，该协议的资产管理规模 (AUM) 增加了约3.4亿美元。有趣的是， **需求方 (借款人) 似乎大部分来自机构参与者**
。为了了解其中原因，可以看看这张图表，分析了Compound的用户类型。此代币分发机制已经吸引到大约800名借款用户 (他们必须借出3.3亿美元)
和5000多名新的贷款用户。

![](https://i.ibb.co/g7j3Rk6/Compound5-0b0a9fde9f.png)

**Comp代币的分发多多少少看起来也像是巨鲸们的游戏**
。下面分享的图表标记了主要的Comp代币奖励获得者。大约20个地址共获得了所有Comp代币的一半。而参与Comp代币分发的钱包所获得的Comp总值中位数为0.07个
Comp，约20美元。

![](https://i.ibb.co/DpB3Vh9/Compound6-a248cda645.png)

在我看来，其中的关键点显而易见：

  * 机构投资者对DeFi借贷仍有庞大的需求，并将持续维持其需求。而Compound正是瞄准了其需求。
  * 当前，Compound上的借贷激励是分发Compound代币。随着代币供应的增加，价格将暴跌。而这也将导致Compound平台的借出金额减少。
  * 到至6/23日为止，仅约16％的代币供应流向交易所。其代币估值可能虚高。
  * 这疯狂的奖励机制是Compound借贷激增的主要推手。目前Compound面临的挑战是提供多样化的借贷方式 (例如基于零售、法币的借贷) ，以及如何继续将其代币应用于社区治理的核心方面。
  * 资本巨鲸是游戏主要玩家。

我确实倾向于认为，“yield
farming”的概念对于普通用户而言被高估了。风险在于，在接下来的日子里，用户既可能无法维持高收益，又可能无法获得Comp代币奖励。奇怪的是，当前流行的Compound借贷使人们联想起一年前中心化交易所引发的流动性挖矿行为。我指出这些并不是暗示项目本身注定要失败，而是要强调一个事实，即多元化的形式至关重要，因为代币价格的下跌可能会导致其自身的螺旋式循环。如果Compound选择增发代币，我们可以等着看会发生什么。

然而，这确实证明了基于代币的激励措施可以在短时间内吸引大量流动性。Synthetix开创了代币激励的先河，而Compound则发挥得淋漓尽致。在未来几个月，我们很可能会看到各种各样的DeFi项目在代币经济和产品效率方面相互竞争，以吸引更多用户。从这个角度来看，DeFi会为普通用户呈现更好的产品。DeFi项目之间的竞争热，让我们拭目以待。

  
  

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

