[![logo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAICAYAAAD5nd/tAAAACXBIWXMAAA7DAAAOwwHHb6hkAAABj0lEQVQoz12Sv0vDQBTHT0HrD4QWRJRLi3QQOojon1JxUhcFQQeViknrJjiIglgRhW4OTiLSWXB10MnJoToI0lp6ESu1TZNc/L7LFcGDD+8u4X3y3r0wKeUUeAqwEBVYZa9amhCb0bydjbdti/vAsy0jALPYp0EZSODq91W8W2AQPGqZg9CUvkvGUv08fSEywwGESDIaoAW+QQHJbWEq+Y+mqc8OCV3wASZBzP+qJJ8ZY2JrpKgqMvk8Yh8kvL6b6sZ+WZicki/BIBgFUVCk5ywsTr4ikvxI+l4F+w20e21bcQiNGUiZ2OZdSGLYr+jW9+hcw3NUx/DBY6pSCcELZCQ8RMtvOK+K9aErO5ugCqdJCDESVVzSwgMSQhLRwjMl1C1Xw+H4Mf/zPQFhxN5J3qrEbGJRmGMDwjIMYfF+yDNauK+FvVp4qlqG6F4PpY3goMIWxebdiVdbi1CiDC+dtwBdfmcA+X/CQqflFGQP6nf5+20C6blB4yYnRW7chcihCYbwFk0ZzAES9eiIq+DiFyR9m3ZUxiupAAAAAElFTkSuQmCC)![logo](/static/9c635c914229a850d1a9fd284014bdd0/65e33/eco_logo.png)](/)

  * [新闻资讯](/)

  *   * [零时学院](/c0llege)

  * [开发者门户](/develop)

  * [生态漫游](/ecos)

Ξ

Search by [](https://www.algolia.com/?utm_source=react-
instantsearch&utm_medium=website&utm_content=&utm_campaign=poweredby)

## VITALIK：以ROLLUP为中心的以太坊路线图

Eth2未来的新可能性：执行分片+数据分片+Layer 2。

* * *

VB

Vitalik Buterin 2020-10-10

来源 | [ethereum-magicians.org](https://ethereum-magicians.org/t/a-rollup-
centric-ethereum-roadmap/4698)

  

Optimism团队不久前[发布](https://medium.com/@optimismPBC/light-at-the-end-of-the-
tunnel-c390a05bbcb8)了其测试网的第一阶段，及其通向主网的路线图。除此之外，[Fuel](https://medium.com/@fuellabs/announcing-
the-fuel-v0-open-
beta-565a2d340fc3)也在推进测试网进程，[Arbitrum](https://medium.com/offchainlabs/arbitrum-
rollup-is-live-on-testnet-c5fed0d0a266)也已经登陆测试网。在ZK
rollup领域中，[Loopring](https://loopring.org/)、[Zksync](http://wallet.zksync.io/)以及基于Starkware技术的[Deversifi](https://www.deversifi.com/)已经正式在主网上线，并且聚集了一定的用户。随着[OMG
network](https://webwallet.mainnet.v1.omg.network/)推出其主网bata版本，plasma也有所进展。与此同时，eth1链上的gas费已经达到了新高，以至于[非金融类dapps被迫停止运行](https://medium.com/universal-
ethereum/out-of-gas-were-shutting-down-
unilogin-3b544838df1a)，[其他](https://zkga.me/)应用也只能在测试网中运行。

Eth2的发展目标之一就是增强扩容性，我们已经非常接近eth2前期阶段了，但要为应用提供基础层扩容性，我们还需要等到数年之后eth2最后一个主要阶段
(译者注：即阶段2)
的实现。讽刺的是，eth2作为rollups数据可用性层的可用性在阶段1就能实现，而在许久之后eth2才能真正用于“传统”的L1应用。将这些事实结合起来，我们可以得出一个结论：
**以应对近期和中期的扩容性需求，整个以太坊生态系统需要将发力点集中到rollups上 (以及plasma和通道技术)。**

如果以此为前提，我们就能得知以太坊中心开发和生态系统发展应该优先考虑的问题，而这多多少少与当前的发展路径有所不同。那么我们应该优先考虑哪些问题呢？

###  

## 短期：推进Eth1基础建设以支持Rollups

在短期内，这样做的一个主要结果在于： **针对以太坊基础层的扩容工作将主要集中于扩大区块的数据容量，而不是优化链上计算或IO操作的效率**
。Rollup扩容性的决定性因素在于该链能包含多少数据，如果能够在当前约60 kB/秒的基础上有所提升，rollups的扩容性则能得到进一步优化。

在基础层上，以下因素需要持续重视：

  * [EIP 2929](https://ethereum-magicians.org/t/eip-2929-gas-cost-increases-for-state-access-opcodes/4558)：在当前gas情况下保证以太坊区块链能够抵御DoS攻击
  * [EIP 1559](https://notes.ethereum.org/@vbuterin/BkSQmQTS8)：一是推动ETH销毁，二是优化交易效率，并且几乎能够确保交易被打包到下一个区块中 (rollups仍然需要等待确认)
  * 新的椭圆曲线预编译，以实现对ZK rollups编程的完全支持
  * 无状态客户端的相关工作，包括从十六进制树转换为二进制树等 (无论我们如何使用以太坊区块链，无状态客户端都非常有意义)

账户抽象 (account abstraction)
不太迫切，因为无论L1是否支持，我们都能在L2上实现。还有其他“巧妙的基础层功能”目前相对来说都没那么重要。

**Eth1客户端可以被重新定义为optimistic rollup客户端** 。Optimistic
rollups仍然需要全节点，并且如果rollup的内部状态转换规则本质上仍然是以太坊式的，只是进行了一些修改
(例如Optimism的目标)，那么我们可以使用现有代码来运行全节点。目前[eth1+eth2合并工作](https://github.com/txrx-
research/eth1-shard-
demo)已经实现将共识引擎从状态转换引擎中分离出来，而这项工作也有助于达成该目标。请注意，这也意味着类似TurboGeth的项目仍然非常重要，高吞吐量的rollup客户端
(而非eth1客户端) 将成为最大受益者。

###  

## 短期：调整基础设施以支持Rollups

目前，用户的账户、ENS域名、以及应用等等都在L1上，这些都需要改变。我们要将用户的主要账户、余额、资产等等都放在L2中。随之而来的是以下几个需求：

  * **ENS needs to support names being registered and transferred on L2** ; see [here 54](https://medium.com/the-ethereum-name-service/general-purpose-layer-2-static-calls-proposal-presentation-by-vitalik-buterin-at-ens-online-2d752906719e)for one possible proposal of how to do this.
  * **ENS需要对在L2上注册和转移的域名提供支持** ，[此处](https://medium.com/the-ethereum-name-service/general-purpose-layer-2-static-calls-proposal-presentation-by-vitalik-buterin-at-ens-online-2d752906719e)是一个可能的相关提案。
  * **Layer 2协议应该被集成到钱包中** ，而不是网页版的dapp中。目前，集成了L2的dapp或是类dapp (例如集成zksync的Gitcoin) 都要求用户完全信任该dapp，这导致安全性大打折扣。要维持当前的信任模型，L2成为钱包本身的一部分 (metamask, status等等) 是最理想的情况。这类支持应该进行标准化，因此支持zksync支付的应用也能随即兼容内置zksync的钱包。
  * **加大跨L2转移的工作力度** ，目标是能够即时、无缝进行跨L2链的资产转移。
  * 对Yul或其他中间编译语言进行更加明确的标准化。以太坊的基础层EVM和Optimism rollup所使用的OVM作为编译目标稍有不同，但都可以由Solidity编译而成。为了使生态系统存在不同的编译目标，但同时还要接受不同的语言，避免Solidity的单一化使用，因此更明确地对所有高级语言都能编译的中间语言 (例如Yul) 进行标准化或许是有意义的。我们也可以考虑对形式验证友好的中间语言，能够处理诸如变量之类的概念，还能保证基本不变量，从而使所有被编译的高级语言都更易进行形式验证。

###  

## 以Rollup为中心带来的经济可持续性

加密货币项目必须具备经济上的可持续性，这是无法回避的事实，在2020年这意味着数百万甚至数千万的融资金额。其中的一部分能够由公共物品募资平台提供
(如Gitcoin Grants或以太坊基金会)，但这些机制的规模不足以覆盖这个等级的融资。但是Layer
2项目能够通过发布自己的代币来解决这个问题，前提是其代币具备真正的经济价值，即未来L2所捕获到的价值。

如果路线图以rollup为中心，随之而来的另一个好处是为L2协议留出了开阔的空间，这些L2协议有能力通过收费或是[MEV](https://ethresear.ch/t/mev-
auction-auctioning-transaction-ordering-rights-as-a-solution-to-miner-
extractable-value/6788)形式来获取发展资金，无论是直接还是间接地
(即代币发行)。以太坊基础层非常需要保持中立，这就使得在协议内进行公共物品募资 (public good funding)
变得十分困难，但L2具备自己的公共物品募资机制，这样一来争议就会大大减少。因此，在这个方面留出空间对于整个以太坊长期的经济可持续性来说可能是一个不错的战略举措。

除了募资问题，具有创造力的研发人员通常都倾向于在他们自己的领域中拥有影响力，而不是针对以太坊的整体协议进行无足轻重的争辩。此外，有许多现有的项目正在尝试创建各种平台。以rollup为中心的路线图使得所有这些项目有机会成为以太坊生态系统的一部分，同时仍能保留高度的经济和技术自主权。

###  

## **长期视野**

除了上文提到的短期考虑外，路线图以rollup为中心还可能意味着我们要重新构想eth2的长远未来：
**每个人都可以进行处理的强安全性单一执行分片，以及可扩容的数据可用性层。**

要理解为什么是这样，需考虑以下因素：

  * 当前以太坊的TPS约为15
  * 如果大家都迁移到rollups上，TPS很快可以达到3000
  * 一旦阶段1到来，rollups的数据存储迁移到eth2分片链上，理论上TPS最高能达到10万左右
  * 最后，阶段2实现之后为eth2分片链提供本地计算，TPS达到……1000-5000

**这意味着eth2的“[phase 1.5 and done](https://ethresear.ch/t/phase-one-and-done-
eth2-as-a-data-availability-engine/5269)”道路，精简基础层并且工作有所侧重，即共识和数据可用性。**

实际上这对于eth2来说是更好的发展方向，因为**分片数据可用性相对分片EVM计算要安全得多。**虽然分片EVM计算的不诚实多数证明 (dishonest-
majority-proof) 验证需要欺诈证明，这需要有潜在风险且严格的2 epoch同步假设，但在异步情况下，数据可用性采样
(如果使用ZKP或多项式承诺) 是安全的。

这将有助于以太坊拥有比其他分片型L2链更强壮的安全模型，而这些分片型L2链都朝着某种形式的分片执行方向发展；[eth2将是功能强大的基础层，强大到足以提供功能逃逸速度
(functionality escape velocity)
就足够了](https://vitalik.ca/general/2019/12/26/mvb.html)。

##  

## **长期来看eth2的工作重点有哪些？**

  * 将不同分片的出块时间错开，从而保证每几百毫秒内都会有某个分片提议区块。这使得在多个分片上运行的rollups拥有极低的延迟性，而链本身没有超低延迟的风险
  * 优化并巩固共识算法
  * 对EVM进行改动，使其对欺诈证明验证更加友好 (例如，这可能意味着某种“框架”功能，可防止代码脱离沙盒，或允许将SLOAD / SSTORE重新映射，使其能够使用除账户存储之外的其他数据源)
  * 对一切进行ZK-SNARK

##  

## **折衷方案**

如果你并没有被说服接受“phase 1.5 and done”这个发展方向，也有自然的折衷方案：使用少量分片作为执行层
(例如4-8个)，其他的分片则作为数据层。目标是使执行分片的数量足够低，以至于在特殊情况下，常规计算机将能够对所有分片进行完全验证，但是与当前的基础层相比，其空间仍然要大得多。

基础层空间不能被最小化太多，因为用户和应用程序仍然有需求，例如：在rollups之间切换、提交欺诈证明、在ZK
rollups中提交零知识证明、发布ERC20代币根合约
(确保大多数用户将在rollups中活动，但基础合约必须有安放之处)。如果每笔交易的成本为140美元，则大大破坏了用户体验。因此，如果有必要的话，使用4-8个执行分片可以显著减轻负担。一台计算机设备仍然可以验证所有分片。如今，验证每13秒产生的eth1区块大约需要200-500毫秒，因此在短时间内验证这种执行的八个线程是完全可行的。我们可以想象客户端采取这些规则：如果网络延迟很低，或者委员会人数>
80％，则可以依靠欺诈证明和委员会，而在特殊情况下直接验证所有分片。

**参考资料：**

Vitalik
Buterin在ETHOnline上的[相关演讲](https://www.youtube.com/watchv=r0jtV9mxdI0&list=PLXzKMXK2aHh4sF0ZlCE49Frl4VJq3ME_V&index=12)：

**往期荐读：**

[《简谈Eth 2.0的未来：将分片作为数据可用性层》](https://news.ethereum.cn/shards-as-data-
availability-layers/)

[《如何评估六大以太坊Layer-2扩容方案》](https://news.ethereum.cn/evaluating-l2-scaling-
solutions/)

[《对比zk-Rollup与Validium》](https://news.ethereum.cn/zkrollup-vs-validium-
starkex/)

  
  

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

