[![logo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAICAYAAAD5nd/tAAAACXBIWXMAAA7DAAAOwwHHb6hkAAABj0lEQVQoz12Sv0vDQBTHT0HrD4QWRJRLi3QQOojon1JxUhcFQQeViknrJjiIglgRhW4OTiLSWXB10MnJoToI0lp6ESu1TZNc/L7LFcGDD+8u4X3y3r0wKeUUeAqwEBVYZa9amhCb0bydjbdti/vAsy0jALPYp0EZSODq91W8W2AQPGqZg9CUvkvGUv08fSEywwGESDIaoAW+QQHJbWEq+Y+mqc8OCV3wASZBzP+qJJ8ZY2JrpKgqMvk8Yh8kvL6b6sZ+WZicki/BIBgFUVCk5ywsTr4ikvxI+l4F+w20e21bcQiNGUiZ2OZdSGLYr+jW9+hcw3NUx/DBY6pSCcELZCQ8RMtvOK+K9aErO5ugCqdJCDESVVzSwgMSQhLRwjMl1C1Xw+H4Mf/zPQFhxN5J3qrEbGJRmGMDwjIMYfF+yDNauK+FvVp4qlqG6F4PpY3goMIWxebdiVdbi1CiDC+dtwBdfmcA+X/CQqflFGQP6nf5+20C6blB4yYnRW7chcihCYbwFk0ZzAES9eiIq+DiFyR9m3ZUxiupAAAAAElFTkSuQmCC)![logo](/static/9c635c914229a850d1a9fd284014bdd0/65e33/eco_logo.png)](/)

  * [新闻资讯](/)

  *   * [零时学院](/c0llege)

  * [开发者门户](/develop)

  * [生态漫游](/ecos)

Ξ

Search by [](https://www.algolia.com/?utm_source=react-
instantsearch&utm_medium=website&utm_content=&utm_campaign=poweredby)

## 「HELLO, ETH 2.0」AMA精彩回顾

ETH2.0最受关注的问题谁来解答？这里有最前沿的技术开发者，最深入社区的Eth爱好者！来回顾大家的精彩发言吧！

* * *

E

ECN 2020-08-16

“能打败以太坊的，只有以太坊2.0。”——Vitalik  

作为全球市值排名第二的公链项目，以太坊规划完备的蓝图一直吸引着全球区块链社区的关注。迎来PoS机制后的以太坊2.0，又将为我们缔造怎样的惊喜和奇迹呢？

本着活跃国内以太坊社区，给中国以太坊社区用户更多的普及教育的初心，昨晚以太坊中国（ECN）与OKEx矿池合作，成功举办了双语版的“Hello, ETH
2.0”AMA直播活动，对话来自全球的以太坊社区领袖，带大家全方位、深度解读以太坊2.0。

本次AMA活动主题包括：以太坊2.0发布路线图/多客户端测试网/layer2扩容解决方案/PoS机制/社区建设

**嘉宾阵容：**

  * **Raul Jordan** , 以太坊2.0开发团队Prysmatic Labs联合创始人
  * **Afri Schoedon** , ETH2.0多客户端测试网的先锋开发者
  * **Steve Guo** , Loopring首席技术官
  * **阿剑** , EthFans总编
  * **Jason** , Unitimes社区合伙人

  

**问答环节第一部分：关于以太坊2.0的常见问题**

**Q1.作为全球市值排名第二的公链项目，以太坊一直吸引着海内外用户的广泛关注。以太坊2.0目前临近上线，呼声也是越来越高。各位嘉宾是否可以用简单通俗的语言向我们解释一下，什么是以太坊2.0？它和现在的以太坊相比，有哪些区别？**

**Rual:**
对我来说，eth2完全颠覆了以太坊区块链从前的设计，**旨在最大程度地同时实现去中心化、抗审查和扩容目标。**我们过去几年不断学习，为的就是寻找更加可靠的方法，来实现我们最初的目标——让以太坊成为一台连接世界的计算机，其中包括权益证明和分片机制。

**阿剑** ：Danny Ryan 说得好：“Eth2.0 is built for Ethereum, and finally it will
become Ethereum itself”。以太坊2.0 是为以太坊生态打造的下一代区块链底层，它跟现在的以太坊相比有两大区别：**一是使用
PoS（权益证明）算法来推动区块链的运行；二是使用 “信标链+多分片链” 的架构来提高可扩展性。**简单来说，以太坊2.0
不再由运行工作量证明算法的矿工来出块；而是各存储了保证金的验证者用数字签名来表达对区块的认可，由此确定主链并使状态获得终局性（finality）。这就是权益证明（PoS）的含义。

此外，信标链 + 多分片链的架构实际上是将 PoS
机制内部的状态与普通用户交易的状态分离了开来，信标链不再执行交易，交易的执行都交给分片链（可以理解为多个与当前的以太坊有同样复杂性的区块链），而信标链负责敲定状态并沟通各分片。

**Q2:以太坊2.0的研发和部署计划历时已久，国内外社区对于以太坊2.0的正式启动时间也是众说纷纭。两位是否可以分享一下以太坊2.0目前的开发进度和大致发布时间？研发工作面临哪些主要挑战？**

**Afri:**
谈ETH2发布路线图的时候最好不要提主网启动的具体日期。因为关于时间问题众说纷纭，有人说1月3日，有人又说7月30日。事实上，这两个时间都不合适。我们都没法说准主网的创世区块何时产生，因为ETH2实在是有太多变动因素了。

但是，对于启动ETH2这一重大里程碑，我可以给出真实的看法。首先，所有客户端都必须实现规范的最终版本v0.12.1。目前只有一个客户端实现了规范v0.12.1并发布了最新版本，而其他四个客户端仍朝着这个目标努力。我们的计划是，本月底多客户端测试网能够实现最终版本规范v0.12.1，这将是第一个达到该目标的多客户端测试网。

如果这运行顺利的话，**我们就可以准备在7月初启动具有主网配置的公共多客户端测试网了。**大家对此期待已久了，但准确来说这并不是所谓的“官方”多客户端测试网。但是如果最终规范版本实现运行得顺利的话，7月我们就可以启动最后的公共测试网了。

可能有别的小型开发者测试网正在运行中，但我们应该把重心放在公共测试网上。如果最终版本的公共多客户端测试网能够稳定运行两至三个月，那我们就可以开始准备ETH2的主网启动工作了。

**首先，启动ETH2之前需要实现存款合约**
。到时还得举办一个合约启动仪式，确定存款合约是将存款从ETH1向ETH2转移的唯一桥梁。启动仪式怎样设计还没决定，但我知道Carl正在为此做准备。我估计最早得到8月底，甚至9月中旬。

**举办了启动仪式且合约部署完成之后，从技术上来说，我们就正式进入ETH2了**
。到那时就算没有官方发布日期，用户也可以在ETH1链上质押第一笔存款，因为质押手续是完全无需许可的。

我的建议是，最快都要在正式的多客户端测试网产生创世区块的90天后，ETH2信标链主网才能产生创世区块。因为我们需要8周的测试时间和4周的缓冲时间，以防出现漏洞。

不管何时能够部署存款合约，我们到时视情况而定推迟主网的创世日期就可以了。但是考虑到上述步骤，主网创世时间可能最早要等到十月份。而且主网创世之前我们还需要达到至少1.6万的质押金额，这可能得额外花几周时间。

**最后我简单总结一下**
……如果一切顺利进行的话，ETH2会在11月上线。更加乐观的说法是，如果我们加快工作的话，10月就能上线。但也要做好心理准备，如果规范中有地方需要修复，并且所有客户端得再次实现新规范，那么可能就要等到2021才能上线了。我觉得ETH2不会在12月上线。

**Q3:
(1/3)互操作性一直是以太坊的独特优势之一。去年九月，以太坊主要的七个客户端团队经历了为期一周的“互操作性封闭营”，在客户端之间的通信和同步方面取得了巨大进展。多客户端测试网作为以太坊2.0正式上线之前的终极试炼，目前我们迎来了第二个多客户端测试网Witti。所以我想请问Raul，到目前为止，客户端互操作性进展如何？客户端之间实现互操作性对以太坊2.0的意义为什么如此重大?**

**Raul:**
客户端互操作性至关重要，因为它帮助我们在单个实现过程中发现关键漏洞。例如，当所有eth2节点都通过Prysm客户端实现运行时，如果没有客户端互操作性，那么我们不可能发现验证者奖惩机制的相关漏洞。

例如，当所有eth2节点都通过Prysm客户端实现运行时，如果没有客户端互操作性，那么我们不可能发现验证者奖惩机制的相关漏洞。如果没有互操作性的话，可能会影响到主网用户，甚至是整个ETH2的发展。

Afri在不同eth2客户端团队之间做了很多协调工作。

**Q3:
(2/3)请问Afri，作为多客户端测试网Schlesi和Witti测试网的倡导者和开发者，请您简单介绍一下多客户端测试网的主要任务是什么？Witti多客户端测试网目前的现状如何？**

**Afri:**
Eth2.0的第一个阶段，阶段0，即信标链。ETH1的客户端无法运行信标链节点。各种新实现的客户端将首次共同协作，采取全新的独特方法达成共识，一起构建一个新的区块链。

在ETH2主网启动之前，我们需要测试网尽可能地模拟主网状态。也就是说，我们需要运行一些长期运行的稳定测试网，并且支持多个客户端运行，理想情况是能够支持所有客户端。多客户端测试网Schlesi已退休，现正运行Witti，不久之后我们将启动Altona。

**Witti正平稳运行中。目前约有15万个slots，网络活性也不错**
。验证者参与率徘徊在71%左右。所有客户端都还会遇到漏洞且需要更新优化。我估计我们还要进行好几次多客户端测试。

**Q3:
(3/3)还有一个问题就是，多客户端测试网在以太坊2.0上线之前需要平稳运行2-3个月，那么考量测试网平稳运行的标准有哪些？预计何时上线正式的多客户端测试网？**

**Afri:** 怎样才算平稳运行呢？ **其中一点就是测试网上没有出现共识问题，不会发生永久性分叉，并且所有客户端都应该对主链达成共识**
。再者，不同的客户端之间存在着一些不兼容的情况，所以我们需要保证客户端之间实现良好的网络通信。我希望在启动最终多客户端测试网之前不在客户端后端中加入ENR（以太坊节点记录），并能够为线路节点提供适当的多地址格式。

**还有就是要看证明和验证者活跃度的状态。**如果活跃度可以维持在80%-90%以上，区块链的活性良好，并且能够持续敲定区块，那就差不多了。

至于最终多客户端测试网的发布时间，我之前有提到最快会在7月中旬启动。我非常期待这一天的到来！

**Q4:
(1/2)在以太坊2.0进展如火如荼的同时，近来，以太坊第二层扩容解决方案也成果颇丰。以太坊2.0逐步上线之后，有了PoS和分片的加持，以太坊生态即将步入扩容时代。Loopring（路印）作为首个且目前唯一一个成功采用ZK-
Rollup的去中心化协议，您可以简单介绍一下ZK-Rollup是如何实现优良用户体验的吗？**

**Steve** : zkRollup是一种用于以太坊的可扩展性方案，通常是被定义为layer
2的解决方案。它能处理更多交易，更快速并且成本更低。它在链下批量执行所有计算，并且只向以太坊提交一个小的零知识证明（不能是伪造的证明）进行验证。由于以太坊会验证这些证明，并且存储足够的数据来准确判断链下账户的状态，因此zkRollup拥有以太坊层级的安全性。

**ZK-Rollup中的ZK意思就是零知识证明，Rollup大家可以把其看成是汇聚打包**
。零知识证明框架目前有好多种，路印协议最终选定了zkSnark作为背后的零知识证明框架，主要是因为zkSnark的证明数据大小是目前最小的，这就意味着链上成本能做到最低，同时生成证明所必须的链下计算成本也不算高，技术框架本身也已经过ZCash多年的实践考验过的。

![](https://i.ibb.co/WDtHXTQ/AMA-1-19a5159578.png)

cr：Loopring

**ZK-Rollup技术中是会有一个中继系统**
。首先，中继在链下把所有账号信息组织成一颗Merkl树，Merkle树的计算过程是两两配对计算哈希，直到算出树根的哈希值，该树根的哈希值就能唯一的代表整颗树当前的状态，因为任意叶子节点上值的变化必然会导致树根的哈希值不一致。

然后中继在链下收集一组用户发起的交易（可以是转账，也可以是买卖），之后就可以为这些交易生成零知识证明。其证明包括如下内容：

  * 前一次区块链上保存的根哈希值是R1；
  * 每一笔用户的交易是经过用户签名的；
  * 按照用户的每笔交易去更新Merkle树，验证更改是否有效；
  * 本次更新之后的根哈希值是R2；

最后，中继把交易的一些关键数据（比如余额）、生成的零知识证明和新的根哈希值R2递交到区块链上，区块链上预先部署的一个智能合约会根据其记录的历史根哈希值R1和输入的交易关键数据去检查这个证明是不是有效的。如果证明有效，那么说明中继后台是诚实的更改了链下保存的Merkle树，从而更新Merkle树哈希值R2。

整个方案的关键点就在于：
**区块链上只是负责存储数据和验证零知识证明，其余的计算处理都是通过在链下更改Merkle树的方式来实现，从而极大的减小对区块链资源的消耗，提升区块链的整体性能。**

又因为链下部分有链上验证的辅助，所以也能确保链下处理资产的安全性和正确性。从而达到在不牺牲区块链带来的安全前提下，提升区块链的整体性能。理论上我们能在保持和以太坊主网同样安全的前提下，达到每秒2025笔交易，每百万笔交易大约150美金的成本。

**Q4:
(2/2)Steve和Jason是否可以继续分享一下，以太坊生态将如何受益于layer1和layer2未来在扩容性方面的结合？又会对DeFi产生怎样的推动力？首先有请Steve。**

**Steve:**
Layer2扩容技术的真实落地应用对以太坊生态来说非常重要，大家也都知道，因为一些传销盘的原因，近期以太坊网络特别拥堵，转账费用暴增，这些都对以太坊的大规模应用会造成影响，比如Reddit已经选定以太坊作为其Token的分发平台，Reddit的用户基数特别庞大，这个一旦大规模应用起来，以太坊会变得越来越拥堵。

恰好我们路印也已实现了基于zkRollup技术的支付系统，6月7号我们路印支付正式上线，目前已支持了10几种Token的二层转账，二层转账秒到，零手续费，大家再也不用为以太坊拥堵，转账费用高而烦恼。对Layer1上DeFi产品来说，如果我们把转账功能都移到了Layer2去的话，那么Layer1的带宽就会变得更充足一些。

**Jason**
：首先是选择性的问题。以太坊layer2方案的繁荣给予开发者和用户更多的选择，同时规避了单一layer2所带来的潜在的风险和垄断。比如大家讨论得热火朝天的ZK-
Rollup和Optimistic Rollup，从token交易的角度来看，ZK-
Rollup的交易速度更快，结算时间更短，对于DEX类应用更加友好，体验更加丝滑，所以Loopring选择了ZK-Rollup。

而Optimistic
Rollup对智能合约逻辑实现的支持更加友好，允许开发者去构建更加复杂的DeFi应用，所以你看Synthetix选择了Optimistic
Rollup。这是第一个好处，生态内有了更加丰富的选择，然后这些选择反哺生态，让生态变得更加繁荣。

第二个是从整体的角度来看，以太坊的安全性和可扩展性都得到了提升。我们知道，layer1，也就是我们所说的主链，是以太坊数据最终的安全性保障。
**一方面，layer1的扩展提升了链上数据处理的效率，同时也极大地降低了发生垃圾交易攻击的可能性。**

**另一方面，layer2方案的部署以及繁荣，降低了用户对layer1可扩展性的需求，layer1可以更侧重于保证自身的安全性**
。这意味着，在保证用户体验的同时，以太坊数据更加安全可靠，从而吸引更多地用户基于以太坊构建应用生态，包括DeFi生态，因为金融应用的第一需求就是要保证安全性。

第三个是价值捕获和网络效应。layer1和layer2的结合使得以太坊可以满足绝大多数的金融以及其他领域的应用需求。随着PoS的到来以及DeFi的繁荣，以太坊上质押的资产形式会越来越多，最终也许真的就成为了大家梦寐以求的“结算层”。同时，这种金融繁荣会带来更大的网络效应，推动包括DeFi在内的以太坊生态进一步发展，这是一个强正反馈。

**Q5:以太坊2.0上线后，以太坊将由目前的PoW机制转为PoS机制。PoS机制的以太坊2.0，Staking经济将作为其中举足轻重的一环。各位嘉宾如何看待以太坊2.0中的Staking经济？对于矿工、矿池、开发者和普通投资者等，各方又该如何参与进以太坊的Staking呢？**

**Raul** ：
我认为质押经济能够保障以太坊的安全性。我们希望用最通俗的语言向大部分用户解释staking，包括那些想要在家运行节点的以太坊爱好者。如果只有少部分的中心化交易所能够参与质押，那么以太坊还是无法像我们所设想的那么安全，并且无法实现去信任化。

而现在，大部分质押者都能通过参加其中一个公共测试网，参与eth2运行测试。Prysmatic
Labs正运行一个eth2公共测试网Onyx，点击次网站参与测试：[https://prylabs.net](https://prylabs.net/)。也可以访问该网站对节点进行监测：[https://beaconcha.in](https://beaconcha.in/)

**阿剑** ：因为协议的特殊性，以太坊 2.0 的 Staking 会跟现有的 Staking 形态有很大区别。为了去中心化，协议层对 Staking
的参与做了很多限制，这些限制其实也是不同的服务商可以发力的地方。

另外，当前的以太坊 2.0 才刚刚要开始 Phase 0
阶段，因此不至于说是立刻就会对整个生态产生天翻地覆的影响，所以大家要观望一下也完全没问题。毕竟现阶段协议层的限制还是比较多的。

最重要的是，想尝鲜以太坊 PoS 的朋友，最先应该做的是了解以太坊 2.0 的协议设计。这样不管是自己动手参与，还是使用第三方服务，心里会更有数。

**Jason**
：关于Staking经济，首先从投机市场的角度来说，Staking减少了市场上ETH的流通量，肯定会刺激币价上升，这对于所有ETH的持有者来说都是喜闻乐见的。这是一个很现实的问题，绝大多数普通投资者、矿工、矿池等都是以盈利为目的的，他们是以太坊生态不可或缺的一环，你不能指望光靠一个天天亏本的信仰以太坊就能发展壮大了。

那么有了利益的捆绑，整个以太坊生态里面的参与者就构成了一个利益共同体。大家都希望以太坊生态能够更加安全地繁荣发展，而不是走向衰败，这种期望无形中会进一步加强以太坊的安全性，并推动其发展。有一个不太合适的词，叫“大而不倒”，这个词很形象地概括了Staking经济给以太坊带来的影响。

普通投资者最快捷地就是直接购买ETH，或者在未来会有交易所和钱包提供Staking服务，普通投资者也可以通过这样的渠道间接地参与Staking。当然啦，自己跑PoS节点也并不难。

DeFi项目方可能要乐开花，因为过去实行部分准备金制度并不容易，一方面在这个圈子里理财暴雷的风险还是很高的，另一方面是其他公链的体量比较小，Staking的收益很多时候无法覆盖币价下跌的损失。但是未来DeFi项目方可以把资金池子里多余的资金用作Staking，实现更加稳定的“躺赚”。

**Steve** ：我个人是很看好2.0的Staking模型可能会带来以太坊币价的上涨，有机会能锁定超过千万的以太坊到2.0的Staking中去。

根据Consensys一次287人的调研结果表明： **有32.8%的人准备自己跑Staking节点，33.1%准备用第三方节点做Staking。**

![AMA2.png](https://i.ibb.co/WDtHXTQ/AMA-1-19a5159578.png)

cr: ConsenSys

我们路印交易所也在考虑Stake池的事情，因为毕竟用户资产躺在智能合约里面是不能再给用户带来超额收益的，但如果能用于Stake的话则会有更多的收益。但我们会用智能合约来保证是在用户拥有知情和控制权的前提下来做这件事情，也就是保证资产的非托管性。

**Q6:阿剑和Jason分别来以太坊中文社区EthFans和Unitimes，对以太坊在国内的用户教育和普及方面作出了卓越的贡献。在转向以太坊2.0的关口，两位认为作为社区方面临的挑战是什么？如何推动社区成员，甚至是更主流人群对以太坊2.0的关注和参与？对此我们能做些什么？**

**阿剑** ：一个蛮大的挑战是 Eth2.0
整个系统比较复杂，而且战线也比较长。这种长使得我们要花更多的心思去判断生态里面哪些事情是现阶段比较重要的、哪些东西是长远来看有价值的。当然长也有长的好处，我们可以花更多时间去普及这个复杂的系统，事情可以做得更细。

我觉得社区要做的事情是多关注整个生态的变化，要始终让大家觉得这是个很好玩的生态。因为技术可能是枯燥的，但生态会有精彩的、有想象力的地方；生态中的一个东西可能是单调的，但看到整个生态，就会觉得是多样而有趣的。

**Jason**
：关于社区面临最大的挑战是，目前整个区块链开源技术，也包含以太坊的中文社区的真实受众和贡献者依然较少。一方面因为技术门槛也偏高，需要学习和研究很多门学科才能够更好的理解区块链技术；另一方面是技术还比较新，很多人对技术的认识还不多，有些甚至有一些偏见。

就比如以太坊，目前以太坊已经是全球公有链里技术社区最大最健康的项目了，但在中文社区建设上依然任重而道远，过去的几年时间，很多人更倾向于在二级市场投机赚取收益，并没有参与到以太坊生态的建设中，他们对以太坊大多停留在对于投机的调研或兴趣；另一方面，以太坊中文社区发展起来的时间要比国外晚一些，语言方面也是中国开发者学习新技术的一道障碍，所以对于一些潜在的想学习以太坊的受众来说，他们可能还没搞清楚以太坊1.0的原理，就又来了1.x、2.0，所以从这个层面来将，以太坊中文社区还要继续强化科普教育以及开发者社区建设。

至于推动更多人对以太坊2.0的关注和参与，目前像EthFans还有Unitimes，当然还有ECN、ethplanet等等很多的以太坊中文社区都在努力。以太坊2.0是一个新的起点，也是以太坊中文社区弯道超车的机会，我们可以做的有很多，比如线上线下的研讨会、workshop以及科普教程的开发等等。

  

**问答环节第二部分：自由问答**

**Q1： ETH2.0 信标链采用 Casper
共识机制，这种共识机制具体而言有什么优势，它解决了什么问题？从现在情况来看，相较于2017年以太坊的高价格，现在的以太坊是不是被低估了？**

**Raul:**
Casper要解决的一个具体问题是，与现有共识相比，可以提供更为安全的权益证明共识。PoS链的大多数其他证都妥协于委托权益证明（DPoS）。也就是说，该协议仅支持少量验证者（可能是20-100）。
**以太坊2.0的Casper机制最多容纳400万验证者，这在促进去中心化的同时提高了安全性。**

其他协议无法支持这么大数量的验证者，因为彼时将无法扩展共识协议。以太坊2.0 Casper能够在支持大量验证者的情况下实现扩容性。

**阿剑** ：Eth2.0 的共识其实可以分成两个部分，一个部分是 LMD-GHOST
分叉选择规则，它将各验证者最新签名视为对分叉链的支持，然后选择最多签名的分叉作为主链，确定出新块的位置；另一个部分是 Casper
FFG，该共识算法的意义是一方面是出块共识的问题，另一方面是长程攻击问题，因为它是通过奖惩机制的设计使得网络能定期敲定信标链的状态，可以理解为定期刷新创世状态（因此
GHOST 也不必回溯太深来确定主链）。。 **整体效果就像 Raul 所说的，以太坊的 PoS 机制比起其它的 PoS
机制，可以支持百倍千倍的验证者数量。**

**Q2: 如何解决中心化交易所staking可能带来的集中化风险?**

**Rual:**
我们可以通过使运行自己的节点变得更简单来解决这个问题。Eth2.0的节点要比Eth1.0或EOS节点更容易运行。这有助于提高去中心化程度和减少大交易所垄断。

**Q3: 关于ETH2.0 的Layer 2解决方案有考虑过
Bitcoin采用的LightingNetwork吗？相比LN，zkRollup有什么具体的优势？**

**Steve** : 可以这么理解，zkrollup是比闪电网络更高效，更快时间能达到资产的最终一致性的解决方案.
闪电网络给不同人转账得有中间跳板，而zkrollup只需要自己的一个中继系统。但zkrollup需要有智能合约，特定椭圆曲线运算的支持，所以比特币上估计是没法部署。

**Q4: 目前除了TxRx团队在做2.0研究，还有哪些团队在做研究，分别具体分工是？**

**阿剑** ：以太坊的研究团队挺多的。我所知的至少有三个。一个是基金会的研究团队，Vitalik 和 Danny Ryan，Justin Drake
等等；一个是 ewasm 团队，他们也做一些跟 Phase 2 有关的研究。还比如 ConsenSys 公司也有一个 Quilt 团队做 Eth2.0
相关的研究。但具体分工，我不太了解。多看 ethresearch 论坛应该会有眉目

**追问：研究进度信息非常碎片，ethresearch网站提问主要以个人形式为主，所以难于确定属于哪个团队。**

**阿剑**
：是的，你说的这个现象确实存在。所以如果自己没有对背景了解得非常清楚的话，可以等一段时间再去回顾或者看有没有总结出来。非专业人员一一跟进其中的进展是比较困难的

**Q5:
以太坊是公链龙头，这点毋庸置疑；以后波卡上线后，实现了多条公链的互通，那么以太坊会如何定位呢？保持独立还是加入互联互通？这会对以太坊地龙头造成影响吗？**

**Jason** :
首先明确一个问题，未来以太坊不会也不可能一家独大，跨链互通和相互合作是包括以太坊在内的所有区块链的必然趋势。现阶段而言，Polkadot最大的问题是，他的设计过于理想化，但是并没有经过实际的考验。区块链是一个复杂的组合式工程，任何一个细节出了问题，都有可能导致整个系统被破坏，而以太坊最大的优势恰恰在于，它是目前经过现实检验的最安全、最稳定、最繁荣的区块链系统。

  

*注：Raul以及Afri的原回答为英文，由ECN翻译为中文，以英文原版为准。详情[点击](https://news.ethereum.cn/hello-eth2-ama/)阅读原文。

以太坊生态的繁荣离不开每一位建设者和拥护者。我们衷心感谢各位嘉宾耐心细致的分享，也感谢观众朋友们对以太坊的关注🙏

源于理想，始于社区，ECN不会停下脚步，期待下次再会。

  
  

声明：ECN的翻译工作旨在为中国以太坊社区传递优质资讯和学习资源，文章版权归原作者所有，转载须注明原文出处以及ethereum.cn/
若需长期转载，请联系[ethereumcn@gmail.com](mailto:ethereumcn@gmail.com)进行授权。

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

