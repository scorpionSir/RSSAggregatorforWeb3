[![logo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAICAYAAAD5nd/tAAAACXBIWXMAAA7DAAAOwwHHb6hkAAABj0lEQVQoz12Sv0vDQBTHT0HrD4QWRJRLi3QQOojon1JxUhcFQQeViknrJjiIglgRhW4OTiLSWXB10MnJoToI0lp6ESu1TZNc/L7LFcGDD+8u4X3y3r0wKeUUeAqwEBVYZa9amhCb0bydjbdti/vAsy0jALPYp0EZSODq91W8W2AQPGqZg9CUvkvGUv08fSEywwGESDIaoAW+QQHJbWEq+Y+mqc8OCV3wASZBzP+qJJ8ZY2JrpKgqMvk8Yh8kvL6b6sZ+WZicki/BIBgFUVCk5ywsTr4ikvxI+l4F+w20e21bcQiNGUiZ2OZdSGLYr+jW9+hcw3NUx/DBY6pSCcELZCQ8RMtvOK+K9aErO5ugCqdJCDESVVzSwgMSQhLRwjMl1C1Xw+H4Mf/zPQFhxN5J3qrEbGJRmGMDwjIMYfF+yDNauK+FvVp4qlqG6F4PpY3goMIWxebdiVdbi1CiDC+dtwBdfmcA+X/CQqflFGQP6nf5+20C6blB4yYnRW7chcihCYbwFk0ZzAES9eiIq+DiFyR9m3ZUxiupAAAAAElFTkSuQmCC)![logo](/static/9c635c914229a850d1a9fd284014bdd0/65e33/eco_logo.png)](/)

  * [新闻资讯](/)

  *   * [零时学院](/c0llege)

  * [开发者门户](/develop)

  * [生态漫游](/ecos)

Ξ

Search by [](https://www.algolia.com/?utm_source=react-
instantsearch&utm_medium=website&utm_content=&utm_campaign=poweredby)

## Eth1.x：如何通向无状态以太坊

本文将列举并阐释Eth1.x主要工作，最终目标指向无状态以太坊。

* * *

GI

Griffin Ichiba Hotchkiss 2020-02-07

来源 | [Ethereum Blog](https://blog.ethereum.org/2020/01/28/eth1x-files-the-
stateless-ethereum-tech-tree/)

  

![1.x封面.png](https://i.ibb.co/7gcsNnN/1-x-0d3dc30bff.png)

  

当我开始着手撰写一篇文章，意图详细介绍以太坊1.x研究的“路线图”，以及如何通向无状态以太坊，却意识到严格来说，这完全不能被定义为传统意义上的路线图。
虽然1.x团队有着共同的目标，但却是一个兼收并蓄的集体，开发者和研究者独立地进行着错综复杂的工作。因此，也不存在“官方”路线图一说，但这并不意味着混乱无序。团队工作遵循一种默认的“次序”，例如某些工作必须要优先进行，某些解决方案是互斥的，还有一些工作可能有所裨益但却不是必要的。

如果不用“路线图”来描述通向无状态以太坊的过程，那么是否有更好的比喻呢？要找到一个合适的比喻确实不容易，但我觉得无状态以太坊就像是[科技树（tech
tree）](https://en.wikipedia.org/wiki/Technology_tree)中的“全属性”。

有些读者可能会立即明白这个类比，那么接下来的几段可以跳过。有些读者可能不是游戏爱好者，我会稍作解释： **科技树（tech
tree）是游戏中的一种常见机制，玩家能够解锁和升级新的符咒、技术或技能，通常以松散的层次或树状结构展现分类。**

  

![1.x6.png](https://i.ibb.co/c1TnhrX/1-x6-4109e0d74b.png)

  

通常来说，可以通过“耗费”某种XP（经验点）来获取树中的元素（属性），进而解锁更多高级元素。有时需要获取两个不相关的基本元素才能解锁第三个更高级的元素，有时解锁一个基本技能会为下次升级开放更多新的选择。对于玩家来说，游戏的乐趣有一半是来自于在科技树中选择了与自身角色能力、目标和偏好相匹配的正确路径。

这准确地诠释了1.x团队的状态：不同的技术主题按照松散的层次结构安排，将有限的资源投入研究、实现和测试。就如同在一个好的RPG（角色扮演类游戏）中，经验点是有限的，只有少数有能力的、有干劲的人才能在一两年内点满解锁所有技能。每个人都朝着同样的终点进发，但是到达终点的路径将取决于哪种解决方案得到了完全的研究和采用。

以下是我自制的粗略科技树图。针对排列方式、每个升级及其与整体的关联性，我会稍作阐释。科技树中最终的“全属性”升级就是“无状态以太坊”。也即是指，一个功能齐备的以太坊主网将支持全状态、部分状态和零状态节点，将高效可靠地传递见证（witnesses）和状态信息，并且从原则上来说，对于后续的扩展性也要准备就绪，直到eth2的桥接建设完成且能够登陆eth1链。

  

![1.x8.jpg](https://i.ibb.co/55X3Fmq/1-x8-72a3ad01e9.jpg)

  

_注意：就像之前提到的，这不是“官方”的工作路线。这是我所整理和组织的1.x团队必须解决的关键难题、里程碑和决策，目标是最终实现无状态以太坊。欢迎提供反馈，随着研究的推进，该计划也会随之更新和修订。_

阅读顺序是从左至右，左侧的 **紫色** 信息是“基本”要素，必须首先进行开发和确定，才能继续推进右侧的要素。 **绿色**
部分表明这些元素在某种意义上算是“增益”项目，尽管在过渡过程中不是必需，并且在研究方面还不够具体，但还是有可取之处。较大的 **粉色**
形状代表无状态以太坊的重要里程碑。要完全过渡到无状态以太坊，必须“解锁”图中所有四个主要里程碑。

  

# 见证范式

在无状态以太坊的语境下，关于见证（witness）的讨论有很多。因此，我提出的第一个主要里程碑是最终的见证范式。这意味着一定要确定状态树和相关见证的结构。可以将规范创建或参考实现视作eth
1.x研究“升级”的地方；围绕状态的新形式展开工作将有助于厘清和集中完成其他亟待解决的问题。

  

![1.x9.jpg](https://i.ibb.co/xD2t1rQ/1-x9-9167bdb761.jpg)

  

## 二叉树

将以太坊的状态切换为二叉树结构非常关键，这可以使得见证足够小，在进行网络通讯时避免带宽/延迟问题。在[上次的研究者会议中](https://blog.ethereum.org/2020/01/17/eth1x-files-
digest-no-2/)，转换为二叉树结构将需要保证以下两种互斥策略之一：

💫
渐进式。如同[忒修斯之船](https://en.wikipedia.org/wiki/Ship_of_Theseus)，当前的十六叉状态树将在很长一段时间内逐段进行转换。通过这种方式，任何涉及状态部分的事务或EVM执行都会自动将状态更改编码为新的二进制形式。这意味着采用“混合”树结构，休眠的状态部分依然保留当前的十六进制形式。该过程实际上永远不会完成，并且对于客户端开发者来说实施难度很大，但是在很大程度上将使用户和更高层的开发人员免受第0层幕后发生的更改的影响。

💫
干净利落。也许这种策略更切合状态数变更的重要性，该策略将通过规划多次硬分叉为过渡过程制定清晰的时间线，计算状态的二进制树新表现形式，一旦新的状态计算完成就持续以二进制形式表示。尽管从实现的角度来看没那么复杂，但是需要协调所有节点运行者，并且几乎可以肯定会给网络带来一些（有限的）中断，这可能会影响过渡期间开发者和用户的体验。另一方面，对于更长远的eth2过渡计划来说，该过程具有一定的参考价值。

不管选择哪种过渡策略，二进制树都会是见证的基础结构，即构成状态树的哈希的顺序和层次。如果不进行优化，通过粗略计算（2020年1月），十六进制树结构中见证的大小将从约800—3400
kB减小到约300—1400 kB。

  

## 代码分块 (merkleization)

见证的一个主要组成部分就是代码。如果不进行代码分块，包含合约调用的事务将需要该合约的完整字节码，以验证其codeHash。代码大小取决于合约，可能会是非常庞大的。**代码的‘merkleization’是一种拆分合约字节码的方法，只需要生成代码的一部分即可生成并验证交易的见证，这是一种大大减小见证平均大小的技术。**拆分合约代码有两种方法，目前还不清楚两者是否互斥。

​ 🔷 “静态”分块。将合约代码拆分为固定大小（约32个字节）。为了使分块后的代码正确运行，这种方法还需要在每个代码块中包含一些额外的元数据。

​ 🔷“动态”分块。根据代码本身的内容将合约代码拆分成多块，并按照其中包含的特定指令（JUMPDEST）进行分割。

乍一看，“静态”分块方式似乎更可取，以避免抽象泄漏，即防止拆分后的代码内容影响较低级别的代码块，这种情况在“动态”分块方式中也可能出现。话虽如此，这两种方式还尚待完全测试，因此都只是作为考虑选项。

  

## 零知识(ZK)见证压缩

大约70％的见证都是哈希。也许可以使用ZK-
STARK证明技术来压缩和验证那些中间哈希。目前有许多关于零知识相关的研究，但是它到底如何起作用，或者甚至会否起作用都还无法得到明确的答案。因此，从某种意义上讲，这在主要的技术开发路线中属于支线，或者说是不必要的升级。

  

# EVM语义

我们之前简单谈到了避免“抽象泄漏”，由于它与EVM语义这一里程碑最为相关，因此在这里我将展开阐释一下为何这个概念如此重要。EVM是大型以太坊协议的
**抽象**
组成部分。从理论上讲，EVM内部运作的细节对于整个大型系统的运作来说应该是不会产生任何影响的，并且反之亦然，系统发生的变动也不应该对抽象的EVM内部产生任何影响。

然而实际上，协议的某些方面的确会直接影响EVM的内部运作。Gas成本就是一个明显的表现。智能合约（EVM抽象内）已通过GAS操作码暴露了各种堆栈操作（EVM抽象外）的gas成本。Gas调度的变动可能会直接影响某些合约的性能，但它取决于具体情况以及合约如何利用其可以访问的信息。

由于存在“泄漏”，因此必须谨慎变动gas调度和EVM执行，避免对智能合约产生意料之外的影响。这使我们必须面对和解决的现实问题，要设计零抽象泄漏的系统非常困难，并且1.x的研究者没有从头重新设计的时间和精力，他们需要在当前的以太坊协议范围内进行工作，目前的虚拟状态机抽象中只存在极少的泄漏现象。

回到我们的主题：见证的介绍将需要更改gas调度。见证需要在网络上生成和传播，并且该活动需要囊括在EVM操作中。EVM语义里程碑的相关主题都与这些成本和激励措施是什么有关，又要如何对其进行估算，以及如何在对其他较高layers影响最小的情况下实现。

  

![1.x10.jpg](https://i.ibb.co/9h7WfHW/1-x10-ac7ae3135c.jpg)

  

## 见证索引/Gas计算

本节可能有许多细枝末节，几句话可能无法解释清楚，在之后我会更详细地进行说明。目前，只需要知道每笔交易都只对区块见证的一小部分负责。生成区块的见证需要进行一些计算，计算由该区块的矿工执行，因此就会产生相关的gas成本，由交易的发起方支付。

由于多个交易可能涉及到状态的同一部分，因此尚不清楚如何最好地估算在广播交易时生成见证的gas成本。如果交易方支付了见证生成的全部费用，我们可以想象这种情况：交易重叠时，区块见证的同一部分可能会被多次支付。需要注意的是，这显然不是一件坏事，只是需要更好地理解这种情况如何为gas激励带来真正的改变。

无论相关的gas成本是多少，见证本身都将需要成为以太坊协议的一部分，并且可能需要并入每个区块成为标准组成部分，就像在每个区块头中加入witnessHash这一条信息。

  

## UNGAS/无版本以太坊

这一类别主要是与无状态以太坊正交的升级，与EVM中的gas成本有关，并且可以弥补我提到的抽象泄漏。
**UNGAS指“无法观测的gas”(unobservable gas)，这是一项修改，明确禁止合约使用**
GAS操作码，以防止智能合约开发者对gas成本进行任何预测。UNGAS是[以太坊核心文件](https://corepaper.org/ethereum/#proposals)中的建议之一，以弥补部分泄漏，使将来对gas调度的更改更易于实施，尤其是与见证和无状态以太坊有关的更改。

  

# 状态可用性

无状态的以太坊不会完全消除状态，而是使状态成为可选项，从而在跟踪和计算的状态量方面赋予客户端一定程度的自由。因此，必须在某个地方提供完整状态，如此一来节点就可以从完整状态中下载部分状态。

从某种意义上来说，现有的范例（例如快速同步）已经提供了此功能。但是零状态节点和部分状态节点的加入使新节点的速度问题变得更加复杂。目前，由于所有节点都保留了当前状态的副本，因此新节点可以从其连接的任何正常节点处下载状态。但是，如果某些节点是零状态节点或部分状态节点，该假设就不再成立。

达成状态可用性里程碑的前提条件与这些因素相关： **节点如何相互告知对方拥有哪些状态；如何在持续变化的点对点网络中可靠地传递这些状态。**

  

![1.x11.jpg](https://i.ibb.co/zNt5P5R/1-x11-0856e8279e.jpg)

  

## 网络传播规则

下图展示了无状态以太坊中可能存在的网络拓扑假设。 **在该网络中，节点将需要具备这样一种能力：根据其想要保留的状态的部分（如果有的话）来对自己进行定位。**

  

![1.x12.jpg](https://i.ibb.co/d2GpT5j/1-x12-883e60575f.jpg)

  

诸如[EIP
2465](https://github.com/ethereum/EIPs/issues/2465)之类的改进属于网络传播规则的一般类别：网络协议中的新消息类型，可表明节点拥有哪些信息，并定义如何将该信息传递给其他节点，而这些节点可能处于较差或有限的网络中。

  

## 数据传递模型/DHT路由

如果上述消息类型之类的改进被接受并实现，节点将能够轻松判断其他节点保留了哪些状态部分。如果所有连接的节点都不具有该节点所需的状态怎么办？

数据传递是一个开放性问题，有许多潜在的解决方案。 **一个“主流”的解决方案** 就是通过云服务器的HTTP请求提供部分或全部状态。
**一个更有野心的解决方案**
是采用相关点对点数据传递方案中的功能，允许对部分状态的请求由连接的节点代理，并通过分布式[哈希表](https://en.wikipedia.org/wiki/Distributed_hash_table)查找正确的归属地。

这两个极端方案在本质上并非不兼容，所以鱼与熊掌为何不能兼得？

  

## 状态切片(tiling)排布

改善状态分布的一种方法是将完整状态分解为多个可管理的部分（切片），将其存储在网络缓存中，这些缓存可以为网络中的节点提供状态，从而减轻了全节点的负担。即使是相对较大的状态切片，区块之间的部分状态切片可能会保持不变。

Geth团队对此进行了一些实验，实验表明状态切片有助于改进状态截图的可用性。

  

## 链修剪(pruning)

[目前已经有许多关链修剪的文章](https://gist.github.com/karalabe/60be7bef184c8ec286fc7ee2b35b0b5b)，此处就不再赘述。但还是要明确一点，只有通过状态切片和/或DHT路由方案这类解决方案，使新的全节点随时可以使用历史状态截图的情况下，全节点才能安全地修剪历史数据，例如交易收据、日志和历史区块。

  

# 网络协议规范

最后，无状态以太坊的完整版图将成为关注焦点。见证范式、EVM语义和状态可用性这三个里程碑共同构成了网络协议规范的完整描述：定义明确的升级应编码到每个客户端实现中，并在接下来的硬分叉中进行部署，以使网络进入无状态范例。

本文已经包含了很多背景知识，但图中还有一些细微之处需要解释：

**♦️ 正式的无状态规范**

总言之，我们并不必对完整的无状态协议进行正式定义。直接将参考实现编码，并用作所有客户端重新实现的基础，这也是合理的。**但是，为见证和无状态客户端创建“正式”规范有着不可置否的好处。**这实际上可以作为以太坊黄皮书的扩展或附录，因为规范将精确详细地描述以太坊无状态客户端实现的预期行为。

♦️ **优化Beam Sync、Red Queen’s Sync及其他状态同步方式**

同步方式不是网络协议的关键部分，但却是影响有效节点如何执行协议的细节。Beam Sync和Red Queen’s
Sync有助于创建来自见证的状态的本地副本。在决定并实施网络协议的最终版本时，我们需要改进同步方式，以使其适应网络协议。

目前，这还是科技树中的“增益”项目，因其可以独立于其他主题进行开发，并且其实现细节取决于更基础的因素，例如见证范式。
**值得注意的是，由于这些协议外的主题无关于“核心”更改，因此有助于实施和测试科技树左侧的根本改进项。**

  

# 结语

看到这里，我们把科技树从左到右都梳理了一遍。我希望“科技树”中的主题，里程碑以及总体思路有助于厘清“无状态以太坊”的研究范围。

我希望能根据实际进展来更新科技树的结构。正如之前所说，这不是“官方”或“最终”的工作范围，只是目前最为准确的草图。如果您有任何改进意见，请与我联系。

如果您有疑问，希望提出新主题或加入无状态以太坊的研究工作，请在ethresear.ch上进行自我介绍，或在Twitter上联系@gichiba或@JHancock。

  
  

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

