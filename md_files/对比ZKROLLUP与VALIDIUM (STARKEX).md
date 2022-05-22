[![logo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAICAYAAAD5nd/tAAAACXBIWXMAAA7DAAAOwwHHb6hkAAABj0lEQVQoz12Sv0vDQBTHT0HrD4QWRJRLi3QQOojon1JxUhcFQQeViknrJjiIglgRhW4OTiLSWXB10MnJoToI0lp6ESu1TZNc/L7LFcGDD+8u4X3y3r0wKeUUeAqwEBVYZa9amhCb0bydjbdti/vAsy0jALPYp0EZSODq91W8W2AQPGqZg9CUvkvGUv08fSEywwGESDIaoAW+QQHJbWEq+Y+mqc8OCV3wASZBzP+qJJ8ZY2JrpKgqMvk8Yh8kvL6b6sZ+WZicki/BIBgFUVCk5ywsTr4ikvxI+l4F+w20e21bcQiNGUiZ2OZdSGLYr+jW9+hcw3NUx/DBY6pSCcELZCQ8RMtvOK+K9aErO5ugCqdJCDESVVzSwgMSQhLRwjMl1C1Xw+H4Mf/zPQFhxN5J3qrEbGJRmGMDwjIMYfF+yDNauK+FvVp4qlqG6F4PpY3goMIWxebdiVdbi1CiDC+dtwBdfmcA+X/CQqflFGQP6nf5+20C6blB4yYnRW7chcihCYbwFk0ZzAES9eiIq+DiFyR9m3ZUxiupAAAAAElFTkSuQmCC)![logo](/static/9c635c914229a850d1a9fd284014bdd0/65e33/eco_logo.png)](/)

  * [新闻资讯](/)

  *   * [零时学院](/c0llege)

  * [开发者门户](/develop)

  * [生态漫游](/ecos)

Ξ

Search by [](https://www.algolia.com/?utm_source=react-
instantsearch&utm_medium=website&utm_content=&utm_campaign=poweredby)

## 对比ZKROLLUP与VALIDIUM (STARKEX)

同样是以太坊二层扩容方案，zkRollup和Validium有何不同？各自的利弊是什么？本文将详细对比分析。

* * *

AG

Alex Gluchowski 2020-06-12

来源 | [Matter Labs](https://medium.com/matter-labs/zkrollup-vs-validium-
starkex-5614e38bc263)

  

译者按：Validium作为以太坊Layer-2的一项新增扩容方案，起名字当然不能含糊，社区各人员在推特热烈讨论过后，最终由V神确定下来。那么同样作为Layer-2扩容方案，与zkRollup有何不同呢？二者的利弊将在此文中一一揭晓。

![](https://i.ibb.co/1zZXmfn/ZKROLLUP-VALIDIUM-1-f497bfbf5b.png)

“StarkEx提高了交易所的安全性——但用户的资金仍可能会被冻结、没收或盗窃。”

最近，DeversiFi推出了其[新版本交易所](https://blog.deversifi.com/introducing-
deversifi2-0/)，由StarkEx交易引擎提供支持。这是一项不可思议的技术成就，进一步满足了用户对加密货币交易的安全需求。这也标志着一个历史性转折点：这是[STARK](https://github.com/matter-
labs/awesome-zero-knowledge-proofs#starks) (去信任的简洁化零知识证明) 在生产系统中首次得以应用。

至于背景，StarkEx采用以太坊的二层扩容解决方案
Validium，其中所有交易的有效性都强制使用零知识证明来验证，而数据可用性在链下进行处理。这可以防止Validium中的资金被盗，因为每次资金转移都必须得到转出用户的授权。

![](https://i.ibb.co/GVfDV3V/ZKROLLUP-VALIDIUM-2-0e72b7837d.png)

Validium的机制与[zkRollup](https://zksync.io/faq/tech.html#zkrollup-
architecture)非常相似，唯一的区别是zkRollup中的数据可用性保存于链上，而Validium则保存于链下。因此，Validium的吞吐量会高许多——但这是有代价的。

  

# StarkEx Validium 的运营者可以冻结用户资金

“能够摧毁某个事物的人，必定控制着它。”——《沙丘》，弗兰克·赫伯特著

由于不像 zkRollup 那样具有链上数据可用性保障，Validium 的运营者 (或者更准确来说，数据可用性的管理者) 有权拒绝任意一个用户转移其资金。

具体操作：运营者在没有告知用户的情况下对其默克尔状态做了细小的改动。由于缺少此信息，用户无法创建默克尔证明 (Merkle proofs)
来验证其对账号的所有权。

如上图所示：如果运营者更改了帐户d3，则帐户d1的所有者将无法证明其帐户所有权，因为丢失了证明过程中所需的节点m的信息。

![](https://i.ibb.co/8BB731s/ZKROLLUP-VALIDIUM-3-fb74b2bca8.png)

有没有一种方法可以防止Validium中的数据扣留攻击？自2016年Plasma的概念诞生以来，该问题已有过广泛讨论，并且研究得出了zkRollups这一技术成果。如果尝试通过非rollup方案，以去信任的方式保障数据可用性，那么[Validium将丧失大部分竞争优势](https://twitter.com/VitalikButerin/status/1267566253780226048)。

虽然问题不能完全解决，但StarkEx通过引入一种许可型数据可用性委员会 (DAC)
缓解了该问题。每次状态更新，都必须需要一定数量的DAC成员签名来确认DAC已接收到数据。在StarkEx中，DAC由[8位成员](https://medium.com/starkware/data-
availability-e5564c416424)组成（太多成员会损害系统的活性）。这些都是由法律监管的声誉卓著的组织，他们不太可能滥用权力——至少理论上如此。

矛盾的是，知名度和声望高，以及受强大的法律权威监管[正是其弱点所在](https://vitalik.ca/general/2019/05/09/control_as_liability.html)。一种可能发生的失控情况是：运营商被要求执行KYC
/ AML法规 (即了解客户身份信息和反洗钱措施)，并有义务冻结交易记录超过1万美元的帐户中的所有资金 (可能会永久冻结)。

随着我们深入研究，便发觉其更加有趣。StarkEx实行[验证者合约升级机制](https://medium.com/starkware/contract-
upgradability-d3a4451877c)，该机制允许运营者立即将新的验证者添加到验证者合约上。这一机制不能使任何旧的合约代码逻辑无效。例如，平台无法删除用户签名检查。但是它允许添加其他限制条件
(以编程语言Solidity为例，可以将限制条件表示为`require()`语句)。

这是一个很好的安全功能：如果StarkEx在其STARK电路逻辑中发现缺失任何限制条件，StarkEx可以快速修复漏洞，且不会造成新的漏洞出现。但是，此功能可能会被滥用，成为一种
**潜规则的审查机制**
。简单来说，StarkEx运营商始终可以在合约逻辑上部署扩展逻辑，没有提前警告用户便引入黑名单。StarkEx的官方文档里没有明确说明，但是似乎执行新规则不需要获得DAC成员的同意。

把StarkEx当成一种完全去中心化的交易协议其实不太准确。**不妨类比想象一下Vitalik
Buterin拥有一个开关，可以立即冻结任何以太坊账户。**然而另一方面，StarkEx确实可以提高加密交易所的安全性
(StarkEx创建者当然会这么做)。

#  

# StarkEx Validium运营者可没收用户的资金

让我们再发散一下我们的思维。我们设想一下不管是什么原因
(很有可能是运营者无法控制的情况)，导致一大部分用户的资产现被冻结。那用户存在StarkEx的资金也被没收了吗？

事实上，这是有可能发生的。

就像许多其他加密项目一样，StarkEx实现了最新的[合约升级机制](https://medium.com/starkware/contract-
upgradability-d3a4451877c)。在部署新版本之前，用户会提前28天收到通知，而任何不愿意接受新版本的用户都可以退出StarkEx平台。

除了那些资金被冻结的用户。

宽限期 (即留给用户考虑是否接受新合约部署的28天时间)
结束后，StarkEx将部署新的合约代码逻辑，将冻结的资金转移至指定方保管。不幸的是，受影响的用户中无法对此进行反抗。

合约升级还存在着一些[合理的忧虑](https://twitter.com/jadler0/status/1268920716944162816)，“升级通知期限”本身时长可能不足以允许每个不同意合约升级方案的用户退出Validium
(所谓的“批量退出”(mass exit)方案)。但是，此问题并非Validium独有,而是普遍存在的合约可升级性问题。

#  

# 2020/07/06更新：

# Justin Drake描述了Validium上的密码学经济攻击。

在后续讨论中，Justin
Drake[指出](https://twitter.com/drakefjustin/status/1269309163995303936)Validium的数据可用性方案可能会导致意外攻击：如果数据可用性委员会
(DAC) 中的有效票的签名密钥被盗
(并且这些密钥在线上保存，因此极易受到安全攻击)，攻击者可以将Validium的状态转换为仅自己可知，从而冻结所有资产，并向用户勒索解锁赎金。

从理论上讲，合约升级机制应该可以缓解这种攻击。Validium的运营商可以启动新版本的部署，为期28天的合约升级通知期过后，状态会恢复到上一个已知版本。资金将会被锁定一个月
(成本当然会相当高)，但是如果DAC拒绝谈判，攻击者将颗粒无收。

然而，事实证明，攻击者可以通过一种方法迫使运营者在损失所有资金或允许攻击者发起双花之间做出决定。我们可以通过以下示例进行说明：

想象一下，某用户可以这样黑进ATM：取款完成后删除整个银行的数据库。用户只能从自己的账户中取款，但是当银行的数据库丢失之后，该用户的操作记录也会被删除掉。(译者注：该操作行为即双花。)

银行员工可以在一个月内完成一系列复杂流程，恢复数据库。但是，由于他们不知道是谁取款的，只能将状态恢复至上一个检查点，也就意味着取过款的账户余额也恢复了！

当然，双花的金额仅限于攻击者的账户余额。然而，如此一来，构建一个去信任的合约，并从暗网中的某个邪恶匿名巨鲸里借到必要的资金就显得十分容易了。这就留给我们的读者思考了。

从该攻击我们可以看出Validium与PoA网络的安全模型相对相似。然而实际上，PoA网络有20个节点且需要至少51％的签名者签名，而Validium有8个节点，需要所有签名者签名。比较而言，
**PoA网络更加安全** 。

#  

# zkRollup的数据可用性保护用户的资金不被没收、审查、攻击，代价是降低吞吐量

只要有一个以太坊全节点在线，zkRollup的用户就可以同步rollup的状态。

zkRollup 如何运作：对于每个 zkRollup 区块来说，重建系统状态所需的信息必须作为以太坊交易的调用数据提交上去。否则，zkRollup
智能合约将拒绝状态转换。zkRollup上进行状态转换时，每笔交易需花费少量gas费，成本随交易总数呈线性增长。

有了默克尔树数据，被审查的用户便可以直接将自己的资金从主网上的zkRollup合约中取出。用户只需要提供默克尔证明，验证其账户所有权。因此，链上数据可用性可以
**保障用户的资金不被冻结或没收 (连zkRollup运营者也没有权力)。**

然而链上数据可用性会限制网络吞吐量。目前，zkRollup在以太坊上每秒至多可处理交易量2000笔，而StarkEx
Validium声称其每秒可处理交易量9000多笔。两者的差异决定了其应用领域的不同。例如zkRollup尤其适用于增强去中心化加密支付的可扩展性
(VISA的全球平均每秒交易处理量为 2000笔)
以及严格要求去信任的不可篡改型智能合约。而另一方面，Validium可能更适用于传统的高频交易，或对去信任需求较低的游戏。

#  

# 总结

本文阐释了zkRollups和Validium (StarkEx) 在运作上有何相似之处，以及两者的主要差异
(即链上和连下数据可用性)，这对我们理解这两种技术以及它们的适用场景起到关键作用。两者的主要差异：zkRollup 是完全去信任的去中心化扩容协议；而
Validium的性能更符合托管式的PoA系统 (从其吞吐量和风险预测来看)，但是其拥有较高的安全性。

每一次旨在完善去信任和增强用户管理自身资产的权力的技术更新，都是为了推动用户实现自主性。为了继续前进，我们总是需要权衡利弊，学会取舍。

然而，在加密社区中，越来越多人意识到区块链技术已经过了 “不要作恶” (don’t be evil) 的阶段，现在是时候过渡到“无法作恶”(can’t be
evil) 的阶段了。我们可以通过自主托管技术、提高抗审查性和隐私性、消除单点故障来实现这一目标。我们正在奋力构建的系统，其基本价值观就是由这些理念构成。

完全去信任的扩容时代即将到来。让我们等待 Matter Labs
的官宣吧，[敬请关注](https://twitter.com/the_matter_labs)！

  
  

ECN的翻译工作旨在为中国以太坊社区传递优质资讯和学习资源，文章版权归原作者所有，转载须注明原文出处以及ethereum.cn，若需长期转载，请联系[ethereumcn@gmail.com](mailto:ethereumcn@gmail.com)进行授权。

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

