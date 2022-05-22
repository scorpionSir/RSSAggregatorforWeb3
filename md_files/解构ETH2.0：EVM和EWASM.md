[![logo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAICAYAAAD5nd/tAAAACXBIWXMAAA7DAAAOwwHHb6hkAAABj0lEQVQoz12Sv0vDQBTHT0HrD4QWRJRLi3QQOojon1JxUhcFQQeViknrJjiIglgRhW4OTiLSWXB10MnJoToI0lp6ESu1TZNc/L7LFcGDD+8u4X3y3r0wKeUUeAqwEBVYZa9amhCb0bydjbdti/vAsy0jALPYp0EZSODq91W8W2AQPGqZg9CUvkvGUv08fSEywwGESDIaoAW+QQHJbWEq+Y+mqc8OCV3wASZBzP+qJJ8ZY2JrpKgqMvk8Yh8kvL6b6sZ+WZicki/BIBgFUVCk5ywsTr4ikvxI+l4F+w20e21bcQiNGUiZ2OZdSGLYr+jW9+hcw3NUx/DBY6pSCcELZCQ8RMtvOK+K9aErO5ugCqdJCDESVVzSwgMSQhLRwjMl1C1Xw+H4Mf/zPQFhxN5J3qrEbGJRmGMDwjIMYfF+yDNauK+FvVp4qlqG6F4PpY3goMIWxebdiVdbi1CiDC+dtwBdfmcA+X/CQqflFGQP6nf5+20C6blB4yYnRW7chcihCYbwFk0ZzAES9eiIq+DiFyR9m3ZUxiupAAAAAElFTkSuQmCC)![logo](/static/9c635c914229a850d1a9fd284014bdd0/65e33/eco_logo.png)](/)

  * [新闻资讯](/)

  *   * [零时学院](/c0llege)

  * [开发者门户](/develop)

  * [生态漫游](/ecos)

Ξ

Search by [](https://www.algolia.com/?utm_source=react-
instantsearch&utm_medium=website&utm_content=&utm_campaign=poweredby)

## 解构ETH2.0：EVM和EWASM

摘要：技术小白也能读懂EVM和eWASM。

* * *

Ivan on Tech 2020-07-16

来源 | [Ivan on Tech](https://academy.ivanontech.com/blog/breaking-down-
eth-2-0-ewasm-and-evm-explained)

  

![](https://i.ibb.co/jTFFP5P/EVM-p1-3acda284cf.jpg)

  

# 以太坊2.0之eWASM

eWASM是以太坊迈向2.0时代的又一创新之举。主流看法是，eWASM能够促进网络的速度、可扩展性和灵活性，也使得开发者能够基于以太坊2.0的协议构建更为复杂的智能合约。除此之外，我们之前的文章还对Eth
2.0的许多不同方面进行了解释，如[Staking](https://academy.ivanontech.com/blog/breaking-down-
eth-2-0-staking-
explained)、[Sharding](https://academy.ivanontech.com/blog/breaking-down-
eth-2-0-sharding-
explained)、[以太坊Layer-2](https://academy.ivanontech.com/blog/breaking-down-
eth-2-0-ethereum-layer-2-and-scalability-explained)、[zk-
snark](https://academy.ivanontech.com/blog/breaking-down-eth-2-0-zk-snarks-
and-zk-rollups)等。在探讨eWASM之前，我们再过一遍以太坊2.0的基本路线。

  

# 什么是以太坊2.0？

以太坊2.0包含一系列升级，将对协议进行颠覆性的改进，扩容以太坊网络，使其更加高效。其中的升级包括：使用Casper协议的Proof of Stake
(权益证明) 机制、分片、Raiden
(雷电网络)、Plasma以及Rollups等等。这些升级将会在[以太坊不同的阶段](https://academy.ivanontech.com/blog/eth-2-0-exploring-
the-phases-of-eth-2-0)中实现，以确保合理地部署和执行。

  * 阶段0：启动信标链，转向PoS权益证明机制
  * 阶段1：加入分片
  * 阶段2：使用以太坊0 eWASM替代现有的以太坊虚拟机 (EVM)

![](https://i.ibb.co/Jk9pgFR/EVM-p2-bef5c69ef1.jpg)

本文将主要探讨阶段2，如果读者对以太坊2.0有一些了解，那么应该知道从EVM到eWASM的转变是非常宏大的工作。在我们进入eWASM之前，先来看看EVM到底是什么。

  

# 以太坊虚拟机是什么？

每条去中心化的区块链都需要一个虚拟机来处理并执行操作。比特币的虚拟机相对简单，因为它只需要处理交易。然而，由于以太坊支持图灵完备的智能合约，其复杂度也就更高。因此，我们需要思考另一个重要问题。

既然智能合约要满足不可篡改性，并且即使历经多个节点也能无损运行，那么以太坊虚拟机 (EVM) 需要拥有哪些主要特性？

![](https://i.ibb.co/jkcvrkH/EVM-p3-f3fe5b5da0.png)

  * 确定性
  * 可终止性
  * 独立性

###

## 确定性

如果针对相同的一组输入，无论其执行了多少次代码，程序都给出相同的输出，那么就可以说是该程序具有确定性。确定性函数的一个完美示例就是数学运算。例如，假定所有数字都以10为底，则无论重复运算多少次，1
+ 4始终等于5。

DApps往往需要同时处理大量金额，所以用户需要清楚知道代码在每个执行阶段如何响应。

###

## 可终止性

我们需要谨记一点，以太坊智能合约是图灵完备的。如果有充足的时间和资源，那么理论上来说智能合约可以解决任何问题。然而，我们无法判断合约是否能在给定的时间限制内完成所有操作。这就是为什么智能合约需要有终止机制。以太坊智能合约借助“gas”来定义其使用期限。当合约达到gas上限，则无法继续进行操作。

###

## 独立性

最后，智能合约应该在一个完全独立的环境中运行。如果合约发生什么意外情况 (例如被攻击或是出现漏洞)，那么其影响不应该波及到其他底层协议。

要满足以上三个特性，有两种系统可以供智能合约使用——虚拟机和Docker容器。由于Docker的合约默认设计不具备确定性，以太坊决定采用虚拟机。

  

# 以太坊虚拟机：如何运作？

当我们说到“虚拟机” (virtual machine) 的时候，到底是什么意思？

传统的操作系统 (Windows/iOS) 一次只需要在一个系统中运行。而虚拟机 (VM) 是基于本地操作系统所创建更高级抽象，可用于复制物理机的功能。

虚拟机使得用户能够在不同的硬件架构和操作系统中同时运行同一平台。这就是为什么虚拟机非常适合像以太坊这样的去中心化网络的原因。以太坊的主要目标是成为一台全球超级计算机，使得开发者能够借助其计算资源构建自己的智能合约和去中心化应用程序。以太坊虚拟机
(EVM) 的功能就类似世界计算机，遍布全球的节点都能进行访问。

![](https://i.ibb.co/cc61r9C/EVM-p4-bcc1a1a79b.jpg)

###

## 堆栈和状态机

相较于普通的虚拟机，EVM还具备两个额外特性。首先，作为状态机的EVM可以读取输入然后相应地更新其状态。其次，EVM还是堆栈式，其内存结构能够以堆栈形式进行组织和访问。

如果读者熟悉数据结构，那么应该对堆栈并不陌生。堆栈是线性数据结构，其中的操作是通过LIFO (后进先出) 来执行的。

下面举个例子：

![](https://i.ibb.co/FBpqGpb/EVM-p5-04e6aa9506.png)

在上图的堆栈中，第一条插入的数据是Orange，最后一条数据是Apple。根据LIFO的逻辑，我们取出的第一条数据应该是Apple，最后才是Orange。

现在我们再来看看堆栈操作：Push和Pop。

  * Push：向堆栈中加入数据
  * Pop：使用LIFO逻辑将数据从堆栈中移除

###

## EVM中的堆栈操作

在堆栈式虚拟机中，操作执行如下：

  * 首先移除数据和操作数
  * 相应操作被执行
  * 执行结果被加入堆栈

参考以下图表：

  * 我们首先移除两个数字：20和7
  * 将这两个数字相加，我们得到27
  * 最后，结果被重新加入堆栈

![](https://i.ibb.co/syHn2Dd/EVM-p6-4e8e455b83.png)

**EVM堆栈式系统的优势**

  * 堆栈结构可确保EVM不需要获取操作数的确切地址。堆栈结构会始终且必然将VM指向下一个操作数。降低大量操作开销的同时提高了整体效率。
  * EVM拥有：世界状态(world state)、机器状态 (machine state) 和虚拟ROM。世界状态将所有帐户存储在网络中，机器状态包括程序计数器、可用gas、堆栈和内存等数据。最后，虚拟ROM读取名为“ EVM字节码”的机器级代码。这是只有EVM才能理解的独特语言。

###

## EVM – 读取字节码

![](https://i.ibb.co/drgR35y/EVM-p7-57e6798089.png)

编程语言分为高级和低级语言。低级语言 (如字节码)
能够轻松被机器读取，但人类却难以理解。这也是为什么大多数编程语言都是高级形式的原因。那么，在智能合约中程序是如何运作的呢？

  * Solidity/Vyper语言的智能合约被编译为字节码，使用到的编译器叫做“solc”
  * 字节码由网络读取并处理
  * 字节码是Solidity操作码的二进制形式。从EVM转向eWASM的过程中，编译器是非常重要的一个部分，因为EVM无法理解除了字节码之外的任何语言。
  * 每个操作码在规范中都被赋予了易于理解的名称，并由数字代码表示。例如，数字0X01代表ADD操作码。

###

## EVM的功能性

  * EVM是以太坊网络中的去中心化处理单元。每笔交易、交互和智能合约执行只能通过EVM进行。
  * 负责所有不同的数据结构，包括指令、操作数以及已经处理的数据。
  * EVM通过指令分配器获取并执行指令，对操作码进行解码。
  * EVM还会跟踪多个网络组件，例如世界状态、存储状态以及区块信息。
  * 在以太坊网络中为智能合约创建一个运行时环境。该环境包含需要用以执行具体交易的信息，例如gas价格 (最新gas价格)、代码大小、Caller (交易接收方地址) 以及Origin (交易发送方地址)。

###

## EVM的缺点

虽然EVM具备许多优势，但也存在四个主要问题，导致网络的整体吞吐量受限：

  * 由于EVM需要处理大量各种各样的操作，其速度便不尽人意。EVM的操作码规范没有进行更新，也没有针对不同的硬件平台做出优化。
  * 第一点提到由于EVM需要处理大量不同操作，就会容易成为运转瓶颈。其结果就是严重损害整个网络的效率。
  * 自从发布初始规范以来，EVM并没有进行太多优化，导致编写合约所需的工具和语言极大受限。

假如底层工作环境本身存在巨大缺陷，那么引入一系列新颖机制 (分片/rollups/Casper)
的意义何在？以太坊之所以寻求从EVM转向使用eWASM，也出于对以上缺陷的衡量。

那么什么是eWASM呢？在此之前，我们需要先理解什么是WebAssembly。

##

  

# 什么是WebAssembly (WASM)？

![](https://i.ibb.co/0CJLVRz/genesis-2-72557e9e97.png)

WebAssembly最近获得了许多关注。WebAssembly是由World Wide Web Consortium (W3C, 万维网联盟)
创造并定义的新代码类型，能够在现代浏览器中高效执行。

WebAssembly凭什么独树一帜？

由于WASM具备基于堆栈的低级二进制格式，且在默认情况下很小，从而可以实现快速加载和执行。浏览器下载WASM代码后，便可以快速将其转换为任何计算机的程序集。

**WebAssembly**

  * 受多个JavaScript引擎和运行时环境的支持，可以在大多数现代浏览器中执行。
  * Go/Rust/C/C++语言可以直接编译为WASM
  * 能够快速适应所有机器级架构，具备极高性能
  * 附带与大多数现代硬件架构兼容的指令集
  * 在大多数平台上趋近于本地运行速度

##

  

# 以太坊2.0 eWASM

读到这里大家可能已经发现了，eWASM (Ethereum WebAssembly) 就是以太坊2.0版的WebAssembly。

根据相关团队的说法：

**eWASM = WASM –非确定性(浮点) +计量+ EEI路径(用以与以太坊交互)**

eWASM团队已经给出其具体的设计目标：

  * 构建EVM转译器，并且以eWASM合约形式添加计量注入器
  * 发布明确详细的规范：以太坊接口、eWASM合约语义以及细节
  * 为solc编译器构建一个eWASM后端
  * 提供C语言和Rust语言的相应指令和库，以支持智能合约编写

诸如EOS、Tron以及Cardano等项目已经或者准备采用WASM，实现eWASM之后，以太坊也将成为其中之一。

#

  

# eWASM vs EVM

EVM的主要设计目标就是要保证正确性，即使可能会因此牺牲一定的效率。以太坊开发者Lane
Rettig认为EVM是基于理论设计而非实用设计，因此可能无法完美支持现实应用。EVM中的每个节点都必须完整正确地运行EVM，而WASM是为现实应用而生的，能够翻译轻松实际的代码逻辑，因此在效率和速度上更具优势。

现在有了大概的认识，我将进一步对比eWASM和EVM。

![](https://i.ibb.co/HgHbhm4/EVM-p9-27b11f93f3.jpg)

###

## eWASM vs EVM #1:速度

简单来说，EVM可以看作是“万精油”，但没有达到理想效果。就拿代码编译来说吧。

EVM经常无法有效编译大量代码。而浏览器的本地JS引擎通常需要大量工作来为某些操作的执行匹配最佳路径，而这对EVM的整体吞吐量来说会产生巨大影响。此外，EVM只能处理256位的字节码，因此小于256位的字节码必须转换为256位格式。

![](https://i.ibb.co/BcztR01/EVM-p10-4ef296665e.jpg)

EVM的设计极大限制了以太坊的速度和可扩展性，使其每秒最多只能处理25笔交易。而这对于现实世界和现实需求来说是非常不切实际的。

eWASM可以直接转换为编译代码，从而提高加载速度，并且大幅提升每个区块能够处理的交易量。除此之外，有了分片和layer2解决方案的加持，以太坊2.0的速度会显著提升。

###

## eWASM vs EVM #2:预编译

eWASM还能消除以太坊对预编译的依赖。预编译是EVM字节码的特殊位，好处在于能够节省gas成本，进行高效的密码运算。大多数情况下，如果不进行预编译，那么几乎不可能将创建合约所需的gas控制在上限范围内。而eWASM的gas效率非常之高，以至于能够省去大部分甚至全部的预编译。

然而，预编译也有不足之处。引入新的预编译往往需要网络进行系统范围的硬分叉。根据历史经验，因为可能导致社区分裂，硬分叉多少具有争议性。

而这些意味着什么？

eWASM能够帮助开发者又快又省地创建智能合约，并且没有硬分叉的顾虑。

###

### eWASM vs EVM #3:灵活性

最后，相较于标准的EVM，eWASM最显著的优势就是代码灵活性。要编写智能合约，以太坊开发者必须特地学习Solidity语言，而这就成为了开发者的知识瓶颈。

eWASM能够与多种语言进行交互，并且拥有更为广泛的开发者工具集。eWASM将支持C/C++/Rust语言。

![](https://i.ibb.co/v4dK84m/EVM-p11-e2b375c44d.jpg)

eWASM将获得所有主流JavaScript引擎的支持，例如：

  * Microsoft的Chakra引擎 (Microsoft Edge)

  * Google的V8 engine (Node.js及基于Chromium的浏览器)

  * Mozilla的Spidermonkey引擎(Firefox及Thunderbird)

eWASM还将获得以下非浏览器实现的支持，例如：

  * ml-proto (OCaml引用解释器)

  * wasm-jit-prototype (使用LLVM后端的独立虚拟机)

  * wabt (基于堆栈的解释器)

EWASM还具有以下的开创性优势，这些优势是之前的EVM不可能拥有的：

  * 对于以太坊轻客户端，得到浏览器支持会更简单，因为eWASM是根据W3C标准架构的
  * eWASM有更多编译器和更多种类的开发者工具
  * 由于大量的项目已经在使用eWASM了，它已聚集了一个健康、多元的开发者社区

##

  

# 结语：eWASM能否助Eth 2.0更上一层楼？

关于eWASM，以太坊社区感到非常兴奋。然而，相关讨论也总是伴随着天花乱坠的说法，我们还需要听到不同的声音。一位资深以太坊开发者Greg
Colvin就对eWASM智能合约持疑，其主要观点是：

  * eWASM无法消除预编译
  * eWASM过渡依赖编译器，可能会导致单点故障

其实绝大多数以太坊开发者都相信eWASM将对协议的整体性能和吞吐量造成巨大影响。

结果究竟会如何呢？让我们拭目以待吧！

  
  

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

