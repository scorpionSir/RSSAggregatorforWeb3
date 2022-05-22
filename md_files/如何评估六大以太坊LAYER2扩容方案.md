[![logo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAICAYAAAD5nd/tAAAACXBIWXMAAA7DAAAOwwHHb6hkAAABj0lEQVQoz12Sv0vDQBTHT0HrD4QWRJRLi3QQOojon1JxUhcFQQeViknrJjiIglgRhW4OTiLSWXB10MnJoToI0lp6ESu1TZNc/L7LFcGDD+8u4X3y3r0wKeUUeAqwEBVYZa9amhCb0bydjbdti/vAsy0jALPYp0EZSODq91W8W2AQPGqZg9CUvkvGUv08fSEywwGESDIaoAW+QQHJbWEq+Y+mqc8OCV3wASZBzP+qJJ8ZY2JrpKgqMvk8Yh8kvL6b6sZ+WZicki/BIBgFUVCk5ywsTr4ikvxI+l4F+w20e21bcQiNGUiZ2OZdSGLYr+jW9+hcw3NUx/DBY6pSCcELZCQ8RMtvOK+K9aErO5ugCqdJCDESVVzSwgMSQhLRwjMl1C1Xw+H4Mf/zPQFhxN5J3qrEbGJRmGMDwjIMYfF+yDNauK+FvVp4qlqG6F4PpY3goMIWxebdiVdbi1CiDC+dtwBdfmcA+X/CQqflFGQP6nf5+20C6blB4yYnRW7chcihCYbwFk0ZzAES9eiIq+DiFyR9m3ZUxiupAAAAAElFTkSuQmCC)![logo](/static/9c635c914229a850d1a9fd284014bdd0/65e33/eco_logo.png)](/)

  * [新闻资讯](/)

  *   * [零时学院](/c0llege)

  * [开发者门户](/develop)

  * [生态漫游](/ecos)

Ξ

Search by [](https://www.algolia.com/?utm_source=react-
instantsearch&utm_medium=website&utm_content=&utm_campaign=poweredby)

## 如何评估六大以太坊LAYER2扩容方案

这里是一份以太坊Layer-2扩容解决方案评估指南，从多个方面分析了ZK rollup、optimistic
rollup、侧链、支付通道、plasma以及validium，助您选择最适合自己的扩容解决方案！

* * *

AG

Alex Gluchowski 2020-06-19

来源 | [Matter Labs](https://medium.com/matter-labs/evaluating-
ethereum-l2-scaling-solutions-a-comparison-framework-b6b2f410f955)

  

随着越来越多的扩容方案崭露头角，以太坊第2层扩容生态系统对网络建设者来说已变得难以取舍。棘手的问题在于，每个解决方案都承诺向用户保证去信任、安全性、经济适用性以及易于使用，这不可避免地会让开发者们眼花缭乱，难以抉择。因此我们建议建设者不要轻易相信每个方案的一面之词，而是应该全面地调查比对清楚，然后在各种方案之间做出权衡。

为了让这项工作不那么复杂，我们整理了一系列问题，以帮助网络建设者评估不同的扩容解决方案，从而采用最适合其需求的解决方案。这些问题分为以下几类：

  * 安全性
  * 性能/经济适用性
  * 可用性
  * 其他方面

除了这些问题之外，我们还汇总了一张对照表，为读者搭建一座桥梁，让其能够窥探到不同扩容方案设计者的想法。尽管我们已尽最大的努力保持中立和公正，但想要简明扼要地比对不同方案的异同，仅靠一张表格是不够的。我们希望后文的补充问题与假设能够弥补表格的不足。

![](https://i.ibb.co/ss3j8D8/528b952e1b.png)

非常感谢Georgios Konstantopoulos（L2独立研究者）、John Adler（Fuel）、Ben Jones（Optimism）、JD
Kanani（Matic）、Patrick McCorry（any.sender）、Justin Drake（以太坊基金会）和Brecht
Devos（Loopring）对该表格的校对和更正。

##  

# 安全性

## 活性假设 (例如瞭望塔)

该协议需要用户活性吗？换句话说：用户需要自己监测扩容方案上所有链上 (比如Layer-1) 活动吗？还是说通过可信任的代理方 (瞭望塔) 来监测呢？

在某些情况下，可以通过一些措施激励可信任的各方负责保证链上活性，激励措施需要与其用户一致
(即担保)。然而，值得注意的是，这些可信任代表方会因为行为不当而承担经济损失，而损失的金额不超过他们成为委托方所提交的“押金”
(即保证金)。用户应该考虑委托方是否有机会攫取超过保证金金额的利益，以及对风险的承受度如何。

## 大规模提款退出假设

该扩容性方案的安全性假设允许所有用户在短时间内成功退出交易 (即提款) 并将资金转移到Layer-1上吗？

当某个Layer-2扩容方案出现安全漏洞时，所有用户需要在短时间内退出Layer-2，这便是大规模提款退出假设。如果用户选择留在Layer-2，则运营者可能会暗中操纵并没收Layer-2上剩下的资金。比如Matic支持大规模提款退出假设，留给用户提款的期限是一周。

但是由于网络堵塞和拒绝服务攻击 (Denial-of-Service,
DoS)，实现大规模提款退出假设相当困难。比方说，在给定用户退出Layer-2的时间范围内，以太坊网络可能会高度拥挤，因此交易也许无法及时打包。即使不会出现网络拥堵的情况，也可能会有攻击者操纵gas费或者对以太坊[日蚀节点](https://eprint.iacr.org/2018/236.pdf)
(eclipse nodes) 进行攻击，导致交易无法及时打包。该攻击向量值得我们深思。

## 托管

Layer-2的验证者若是达到一定数量，能否长期使用户无法访问自己的资金？他们可以窃取用户的资金吗？

如果你想要你的项目保持抗审查性的话，这一点尤其重要。

## 热钱包密钥易受攻击

layer-2解决方案中的资金安全性是否取决于运营者保障密钥安全性的能力？密钥是否必须保持在线才能维持系统运作（即热钱包密钥）？

有的密钥必须保存在线上以保持系统运作 (如热钱包密钥)。那么Layer-2解决方案上的资金安全性是否取决于运营者保障密钥安全性的能力？

[众所周知，保护热钱包是很难的。](https://www.bitdegree.org/tutorials/cold-wallet/)

## 易受加密经济攻击

解决方案应对加密经济攻击时脆弱性如何？以及方案设计是否基于博弈论的假设？

受加密经济激励诱发的攻击形式多样，包括[损害Layer-2上验证者（或他们的运营人员）的声誉](https://www.imperva.com/learn/application-
security/social-engineering-
attack/)，[贿赂Layer-1的矿工](https://ethresear.ch/t/nearly-zero-cost-attack-
scenario-on-optimistic-
rollup/6336)，建立[恶意DAO](https://slideslive.com/38911605/smart-contract-
security-incentives-beyond-the-
launch)等。这些攻击向量进化得非常快，并且经证实难以在基于博弈论假设架构的系统里消除这些向量。

这里还包括一些非技术性盗窃但产生同等后果的情况。例如[这种对Validium的双花攻击](https://twitter.com/the_matter_labs/status/1270093208727556108)：攻击者无法通过设计窃取其他人的资金，但仍然可以重复使用自己的资金。

## 密码学基元

解决方案是基于标准密码学还是较新的密码学研究，比如[SNARKs或STARKs](https://github.com/matter-
labs/awesome-zero-knowledge-proofs)？

通常来说，面世时间越长的加密学架构，越难被破解。如果使用的加密学技术越先进、越新颖，那么就需要能力更强的团队来对其进行实现和审计。

  

# 性能/经济适用性

## 最大吞吐量

在以太坊1.0的解决方案中，能实现的最大吞吐量是多少？以太坊2.0呢？

尽管某个解决方案的吞吐量在今天看来可能令人满意，但你自然会展望未来，对将来所需的额外吞吐量进行预测，考虑你计划采用的方案是否能满足未来的需求。

## 资本效率

扩容方案的资本效率如何？它需要锁定大量资金才能运作吗？

与其他解决方案相比，资金效率较低的系统用户成本会更高，并且可能由于缺乏即时的流动性而发生运行中断。比如，支付通道的资金效率相对较低，因为通道运营者必须锁定其通道平均交易量几倍的资金才能确保交易金额不超出容量上限。

## 开新账户的成本

新用户在Layer-2开账户时需要Layer-1的链上交易记录吗？

在对比图表里，我们展示的是每个系统在最好情况下的表现，但在个别实现里，效率可能没那么高。例如，zkSync和Loopring都用zkRollups，但Loopring要求用户用Layer-1的一笔交易来开新账户才可以使用支付功能，而zkSync则不需要。

  

# 可用性

## 提款时间

在Layer-1上提款需要多长时间？

为了解决纠纷，一些解决方案的提款期限可能要花上一周或更长的时间。为了缓解长时间等候的问题，有没有流动资金提供者可以为用户提供流动资金以换取风险溢价？由于快速提款需要支付一定的金额，那使用这个方案的真实价格是多少？

## 获得主观最终确定性的耗时

基于协议的安全性预设，一笔交易多快能够达到在Layer-1中无法被回滚的状态？

主观确定性的意思是，即使Layer1的智能合约还不能信赖该交易，但外部的观察者能信服交易的不可逆性。例如，在Optimistic
Rollups里，为了得到Layer-1的确定性，你需要一个以太坊上的证明，然而完全获得确定性需要大约1周时间。

## 客户端对主观确定性的可验证性

轻客户端（浏览器/移动钱包）可以验证主观确定性时间吗？

继续optimistic
rollups的例子，当你需要以太坊上的一个证明来得到Layer-1的确定性和验证你的交易不可更改时，你必须下载整个rollup状态并执行上周的所有交易，以确保打包的区块都是有效的。

## 即时交易确认

解决方案能否提供真正的即时交易确认？还是提供担保下的即时交易确认？

“即时表面确定性”可以在大多数Layer-2协议上实现，例如，交易会在用户交互中显示即时的确认。只有支付通道（状态通道）对这些证明提供完全的安全性保证，而在其他协议里，这些交易在Layer-1上被确认之前仍然可以被撤销。撤销这些交易不是没有代价的，无论成功与否，这些方案上的验证者都将失去他们的安全保证金（即存款）。

即时交易确认这一特性取决于扩容方案具体实现上的细节。

  

# 其他方面

## 智能合约

Layer-2支持任意可编程的智能合约还是仅限于使用[predicate](https://specs.counterfactual.com/en/latest/adjudication-
layer.html)实现的子集。

## 字节码的可移植性

你可以将以太坊合约上的既有EVM字节码几乎原封不动地移植吗？

## 本地隐私支持

协议提供本地隐私支持吗？

如果没有默认的低成本屏蔽交易，隐私保护将会[非常低效](https://twitter.com/VitalikButerin/status/1196468111995756544)，在关于在多个平台上去匿名化的大量研究里,
这一点已得到充分有力的证明（[1](https://cryptolux.org/images/d/d9/Zcash.pdf),[2](https://arxiv.org/pdf/2005.14051.pdf)）。

  

# P.S.对zkRollups的一个边注

现在有两个扩容方案是使用zkRollups的，现在可以试用——路印（主网上线）和[zkSync](https://zksync.io/) （Matter
Labs旗下平台，现已上线）。两者的主要区别在于对底层证明系统的选择。路印用的是Groth16
SNARK，配以一个特定应用信任设置，而zkSync使用了更新的PLONK，配以通用信任设置的证明系统。考虑到最近这个证明系统在设计上获得的突破，我们相信PLONK会成为促进zkRollups应用的一个主要因素，我会在即将发布的文章里详细说明。

我们希望这篇文章对读者在寻找扩容方案时会有所帮助，并且使你对这领域的未来感到兴奋。如果你有任何疑问，或你想就上面谈论到的内容进行讨论，欢迎随时通过邮件[hello@matter-
labs.io](mailto:hello@matter-
labs.io)、[Twitter](https://twitter.com/the_matter_labs)、[Telegram](https://t.me/zksync)联系我。

Matter
Labs致力于让更多的人参与到公共区块链上。我们正在构建[zkSync](https://zksync.io/)，这是以太坊上一个安全快速的扩容平台。

译者注：zkSync已于6月18日上线主网。

  
  

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

