[![logo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAICAYAAAD5nd/tAAAACXBIWXMAAA7DAAAOwwHHb6hkAAABj0lEQVQoz12Sv0vDQBTHT0HrD4QWRJRLi3QQOojon1JxUhcFQQeViknrJjiIglgRhW4OTiLSWXB10MnJoToI0lp6ESu1TZNc/L7LFcGDD+8u4X3y3r0wKeUUeAqwEBVYZa9amhCb0bydjbdti/vAsy0jALPYp0EZSODq91W8W2AQPGqZg9CUvkvGUv08fSEywwGESDIaoAW+QQHJbWEq+Y+mqc8OCV3wASZBzP+qJJ8ZY2JrpKgqMvk8Yh8kvL6b6sZ+WZicki/BIBgFUVCk5ywsTr4ikvxI+l4F+w20e21bcQiNGUiZ2OZdSGLYr+jW9+hcw3NUx/DBY6pSCcELZCQ8RMtvOK+K9aErO5ugCqdJCDESVVzSwgMSQhLRwjMl1C1Xw+H4Mf/zPQFhxN5J3qrEbGJRmGMDwjIMYfF+yDNauK+FvVp4qlqG6F4PpY3goMIWxebdiVdbi1CiDC+dtwBdfmcA+X/CQqflFGQP6nf5+20C6blB4yYnRW7chcihCYbwFk0ZzAES9eiIq+DiFyR9m3ZUxiupAAAAAElFTkSuQmCC)![logo](/static/9c635c914229a850d1a9fd284014bdd0/65e33/eco_logo.png)](/)

  * [新闻资讯](/)

  *   * [零时学院](/c0llege)

  * [开发者门户](/develop)

  * [生态漫游](/ecos)

Ξ

Search by [](https://www.algolia.com/?utm_source=react-
instantsearch&utm_medium=website&utm_content=&utm_campaign=poweredby)

## 手把手教程：如何成为ETH2 MEDALLA测试网验证者

跟着本文学习如何参与Medalla测试网，为Eth2.0质押做准备！

* * *

RS

Ryan Sean Adams 2020-09-08

来源 | [Bankless](https://bankless.substack.com/p/guide-becoming-a-validator-on-
the)

  

![eth2手把手1.png](https://i.ibb.co/XLkgy2L/eth2-1-8c9e26184f.png)

  

作者Ryan Sean Adams寄语：我们对即将到来的Eth2感到十分期待，因此我们为想在Eth2当前测试网中跑验证者节点的读者整理了一份详细的教程。

感谢来自[ConsenSys](https://consensys.net/)
[CodeFi](https://codefi.consensys.net/)的[Collin
Myers](https://twitter.com/StakeETH)和[Mara
Schmiedt](https://twitter.com/MaraSchmiedt)的整理，我们希望本教程能够为想要参与Eth2的以太坊社区成员提供帮助。

测试网已经来了，主网还会远吗？

##  

# 本文主要内容：

  1. 推荐硬件
  2. 选择并安装客户端
  3. 设置Eth1节点
  4. 使用Eth2 Launchpad
  5. 附加内容和资源

##

![eth2手把手2.jpeg](https://i.ibb.co/Svt4FCg/eth2-2-7dedb116c8.jpg)

  

# 1\. 硬件要求

基于Eth2的去中心化设计目标，验证者预计能够使用多种不同的基础设施设置 (本地或云端等)。

_参与测试网不仅能够实战演练，还能给自己充裕的时间来选择哪种设备和方式最为适宜，拥有最可靠的性能。而目前这也是我们唯一能做的事。_

以下是一些硬件配置、资源链接以及有参考意义的教程。

## 推荐配置：

**操作系统** ：64位Linux、Mac OS X、Windows

**处理器** ：Intel Core i7-4770或AMD FX-8310 (及以上)

**内存** ：8GB RAM

**容量** ：100GB可用空间SSD

**网络** ：宽带网络 (10 Mbps)

**电源** ：不间断电源 (UPS)

**Digital Ocean** **( ** **满足条件的云服务商**** )**

**标准Droplet**

  * **内存** ：8GB RAM
  * **容量** ：160GB可用空间SS
  * **运行时间** ：99.99%
  * **可用性** ：8个数据中心
  * **费用** ：0.060美元/小时；40美元/月

**符合条件的硬件设备：**

  * [ZOTAC ZBOX CI662 Nano Silent Passive-Cooled Mini PC 10th Gen Intel Core i7](https://www.amazon.com/ZOTAC-Passive-Cooled-Quad-core-Barebones-ZBOX-CI662NANO-U/dp/B08CVW7ZTC/ref=sr_1_14?crid=3H3C58N0E4ADZ&dchild=1&keywords=mini+pc+barebones+i7&qid=1598263033&sprefix=mini+PC+barebones+,aps,767&sr=8-14)
  * [SanDisk Ultra 3D NAND 2TB Internal SSD](https://www.amazon.com/SanDisk-Ultra-NAND-Internal-SDSSDH3-2T00-G25/dp/B071KGS72Q/ref=sr_1_2?crid=1KNWA41H1VO9Q&dchild=1&keywords=sandisk+ssd+plus+2tb+internal+ssd+-+sata+iii+6&qid=1598262732&sprefix=sandisk+SSD+plus+2TB,aps,790&sr=8-2)
  * [Corsair Vengeance Performance SODIMM Memory 16GB (2x8GB)](https://www.amazon.com/Corsair-Vengeance-Performance-Unbuffered-Generation/dp/B08BLVHWXD/ref=sr_1_2?dchild=1&keywords=CORSAIR+VENGEANCE+SODIMM+16GB+\(2x8GB\)&qid=1598262850&sr=8-2)

## 最低要求配置：

**操作系统** ：64位Linux、Mac OS X、Windows

**处理器** ：Intel Core i5-760或AMD FX-8110 (及以上)

**内存** ：4GB RAM

**容量** ：20GB可用空间SSD

**网络** ：宽带网络 (10Mbps)

**电源** ：不间断电源 (UPS)

**Digital Ocean (满足条件的云服务商)**

**标准Droplet**

  * **内存** ：4GB RAM
  * **容量** ：80GB可用空间SSD
  * **运行时间** ：99.99%
  * **可用性** ：8个数据中心
  * **费用** ：0.030美元/小时；20美元/月

**符合条件的硬件设备：**

  * [ZOTAC ZBOX CI642 Nano Silent Passive-Cooled Mini PC 10th Gen Intel Core i5](https://www.amazon.com/ZOTAC-Passive-Cooled-Quad-core-Barebones-ZBOX-CI642NANO-U/dp/B08BBN3LS5/ref=sr_1_41?dchild=1&keywords=mini+pc+barebones+i5&qid=1598263166&sr=8-41)
  * [SanDisk Ultra 3D NAND 2TB Internal SSD](https://www.amazon.com/SanDisk-Ultra-NAND-Internal-SDSSDH3-2T00-G25/dp/B071KGS72Q/ref=sr_1_2?crid=1KNWA41H1VO9Q&dchild=1&keywords=sandisk+ssd+plus+2tb+internal+ssd+-+sata+iii+6&qid=1598262732&sprefix=sandisk+SSD+plus+2TB,aps,790&sr=8-2)
  * [Corsair Vengeance Performance SODIMM Memory 8GB](https://www.amazon.com/Corsair-Vengeance-Performance-CMSX8GX4M1A2400C16-2400MHz/dp/B077SB72QN/ref=sr_1_1?dchild=1&keywords=CORSAIR+VENGEANCE+SODIMM+8GB&qid=1598263273&sr=8-1)

##  

# 2.选择并安装客户端

作为Eth2第一个多客户端大型公共测试网，Medalla的发布给验证者提供了不同的客户端选择，来运行他们的节点。

在Medalla测试网中，有4个客户端团队提供了可供试用的产品实现:

![eth2手把手3.png](https://i.ibb.co/tJXHtqQ/eth2-3-bb4ab281fe.png)

## 客户端团队

### 1\. Prysmatic Labs的Prysm ([Discord](https://discord.gg/KSA7rPr))

[Prysm](https://github.com/prysmaticlabs/prysm)是基于Go语言对Eth2.0协议的实现，专注于可用性、安全性和可靠性。

Prysm使用Go语言编写，并在GPL-3.0的许可下发布。

  * _使用说明_ : <https://docs.prylabs.network/docs/testnet/medalla>
  * _Github_ : <https://github.com/prysmaticlabs/prysm/>

### 2\. Sigma Prime的Lighthouse ([Discord](https://discord.gg/cyAszAh))

[Lighthouse](https://github.com/sigp/lighthouse)是使用Rust语言的Eth2.0客户端，专注于速度和安全性。Lighthouse的研究团队为[Sigma
Prime](https://sigmaprime.io/)，是一家信息安全和软件工程公司。Lighthouse基于Apache 2.0许可下实现。

  * _使用说明_ : <https://lighthouse-book.sigmaprime.io/become-a-validator.html>
  * _Github_ : <https://github.com/sigp/lighthouse>

### 3\. ConsenSys的Teku ([Discord](https://discord.gg/7hPv2T6))

[PegaSys
Teku](https://pegasys.tech/teku/)是一款基于Java的Eth2.0客户端，旨在满足机构需求与安全要求。Teku基于Apache
2的许可，用Java编写，一种以其成熟度和普遍性而闻名的语言。

  * *使用说明：*<https://docs.teku.pegasys.tech/en/latest/HowTo/Get-Started/Install-Binaries/>
  * _Github:_ <https://github.com/PegaSysEng/teku>

### 4\. Status的Nimbus ([Discord](https://discord.gg/XRxWahP))

研究项目[Nimbus](https://our.status.im/tag/nimbus/)也是Eth
2.0的客户端实现，设计用于嵌入式系统和个人移动设备，包括硬件资源受限的老式智能手机。

  * _使用说明:<https://nimbus.team/docs/>_
  * _Github:<https://github.com/status-im/nim-beacon-chain>_

##  

# 3\. 设置一个Eth1节点

验证者在Eth2上运行节点，需要先运行Eth1节点，以便监视32个ETH的验证者存款。在运行Eth1节点时，用户有多种选择，以下是一些最常用的工具。

**自托管：**

[OpenEthereum](https://www.parity.io/ethereum/)

[Geth](https://geth.ethereum.org/)

[Besu](https://besu.hyperledger.org/en/stable/)

[Nethermind](https://www.nethermind.io/)

**第三方托管：**

[Infura](https://infura.io/)

##  

# 4.在Medalla上运行Eth2验证者节点

## 第一步：在Goerli测试网上质押ETH

如果读者刚接触以太坊，那么加入网络的主要方式就是参与质押。Eth2的Medalla测试网需要每位验证者质押32个GöETH
(除了使用Goerli测试币，其他步骤与真正的Eth2没什么不一样！)

如果用户想要参与测试网，以下是一些十分有用的工具以简化参与流程。

  1. Prysmatic的 D[iscord](https://discord.gg/KSA7rPr) (获得goerli测试币的通道)

  * Prysmatic团队已经自动化该过程
  * 只需在discord里留言“!send (你的以太坊地址)”即可

  2. EthStaker的[Discord](https://discord.gg/) (获得goerli测试币的通道)

  * 该自动程序由[Beaconcha.in](https://beaconcha.in/)运行和维护
  * 只需留言“!goerliEth (你的以太坊地址)”即可

  3. Goerli认证水龙头 ([Goerli Authenticated Faucet](https://faucet.goerli.mudit.blog/))

  * 只需复制粘贴你的ETH地址，然后选择‘请求’即可

## 第二步：前往[Eth2 Launchpad](https://medalla.launchpad.ethereum.org/)

过去几个月以来，[以太坊基金会](https://ethereum.org/en/foundation/)、Codefi Activate以及Deep
Work Studio都在研究开发一个界面，使得用户更简单地参与质押并且成为Eth2.0的验证者。

研究结果就是[Eth2 Launch
Pad](https://medalla.launchpad.ethereum.org/)，该应用可以让用户安全地完成以下步骤：生成Eth2密钥对，在Eth2测试网和主网上的正式存款合约里质押32个ETH。

Launch Pad专门为在家中运行节点的验证者设计。这些以太坊爱好者想要运行自己的节点，并且在自己的电脑终端屏幕上轻松地运行指令。

![eth2手把手4.png](https://i.ibb.co/QCjdQct/eth2-4-e004051e16.png)

### 第二步a：尽职调查 ( _概述部分_ )

在参与质押之前，应该花点时间来读读这些内容。“概述部分”提供了一些教育信息，关于质押ETH所面临的一些风险。

####

![eth2手把手5.png](https://i.ibb.co/p1rptZq/eth2-5-d7d8ca3182.png)

## 第三步：生成密钥对以及助记词

每一个验证者节点，都要生成自己的验证者密钥对和助记词，以便之后生成提款密钥。

第一步，用户需要选择想要运行的验证者节点数量，以及在哪个操作系统运行。

![eth2手把手6.png](https://i.ibb.co/hRqZqPw/eth2-6-710134b70e.png)

Launchpad会给提供两种选择来生成用户自己的存款密钥。点进此[链接](https://github.com/ethereum/eth2.0-deposit-
cli/blob/master/README.md)，获取用户操作系统的更多说明细节：

<https://github.com/ethereum/eth2.0-deposit-cli/blob/master/README.md>

第一种选择是使用从[ethereum/eth2.0-deposit-
cli页面下载的二进制可执行文件，在自己的终端运行./deposit指令](https://github.com/ethereum/eth2.0-deposit-
cli/releases/)。

![eth2手把手7.png](https://i.ibb.co/Jynw8BY/eth2-7-1bcbad94df.png)

第二种选择是从Python源代码中构建deposit-CLI工具。参与者需要按照以下说明操作，以确保安装了所有必需的开发库和deposit-CLI工具。

完成之后，在自己的终端运行.\eth2deposit\deposit.py指令。

![eth2手把手8.png](https://i.ibb.co/jGFkJFk/eth2-8-aab3adb5fc.png)

当用户安装了deposit-CLI工具并在终端窗口中运行它后，将收到以下提示:

  1. 确定要运行的验证者节点数量
  2. 确定使用哪个语言来生成助记词
  3. 确定在哪个测试网来运行验证者节点

**请选择 Medalla 测试网，作为本次教程。**

现在用户将被要求设置密码，一旦密码确认，用户的助记词将生成。 **确保把它记在一个安全的地方，并离线存储。**

如果用户顺利完成这一步了，将会看到下图所示的屏幕：

![eth2手把手9.png](https://i.ibb.co/6cKGPtT/eth2-9-fc5eb66177.png)

如果大家对deposit-
cli有任何问题，请访问下面的GitHub库：<https://github.com/ethereum/eth2.0-deposit-cli>

## 第四步：上传你的存款文件

就快成功啦！下一步就是上传你在前一个步骤中生成的存款json文件。

该文件位于/eth2.0-deposit-cli/validator_keys目录中，标题为deposit-data-[timestamp].json。

![eth2手把手10.png](https://i.ibb.co/K6qM33n/eth2-10-526f777a8d.png)

## 第五步：连接自己的钱包

下一步是连接你的Web3钱包并点击继续。 **确保在钱包设置中选择了Goerli测试网。**

不要发送真的ETH到Medalla测试网的存款合约上。

![eth2手把手11.png](https://i.ibb.co/Th6gjYS/eth2-11-bd9457185f.png)

  

![eth2手把手12.png](https://i.ibb.co/tQ4Fy2y/eth2-12-a277141758.png)

## 第六步：确认交易&启动存款

连接并确认了你的钱包地址之后，接下来会去到一个总结页面，该页面显示了需要发送到存款合约的GoETH总额，这个总额基于用户运行的验证者的数量。

“同意”警告选项，单击确认导航到最后一步——实际存款。

点击“启动交易”将你的GoETH存入Medalla测试网合约中。

接下来需要通过钱包确认自己的GoETH存款，每个验证者节点需确认32个GoETH。交易一旦被确认，就代表你质押成功了！可以在最具有纪念意义的Web3测试网上称自己为正式的质押者了!

![eth2手把手13.png](https://i.ibb.co/gtrJxL3/eth2-13-710d1962c6.png)

##  

# 6.额外内容&资源

在回顾了上述的步骤之后，我们建议验证者在开始质押之前，查看以下每个客户端的指南。根据选择的不同的客户端，上述的步骤将会有不同的操作顺序。

下面是我在这个行业中见过的最深入的指南，让读者们了解到这个过程中的细微差别。

**给Eth2验证者的额外资源**

_一旦决定使用哪个客户端之后，强烈推荐大家查看下列的资源整理：_

**Eth2区块浏览器：**

  * [Eth2Stats](https://eth2stats.io/medalla-testnet)
  * [Beaconcha.in](https://beaconcha.in/)
  * [BeaconScan](https://beaconscan.com/)

**基础设施硬件**

  * [Hudson Jameson (在去中心化应用节点中运行Eth2)](https://hudsonjameson.com/2020-05-18-eth-2-0-staking-and-more-with-topaz-and-dappnode-for-under-750/)
  * [Quantstamp的文章](https://quantstamp.com/blog/how-to-be-an-eth-2-0-validator-on-the-topaz-testnet)

**CoinCashew系列:**

  * [如何在Ubuntu上使用Prysm参与Eth2 Medalla测试网质押](https://www.coincashew.com/coins/overview-eth/guide-how-to-stake-on-eth2)
  * [如何在Ubuntu上使用Lighthouse参与Eth2 Medalla测试网质押](https://www.coincashew.com/coins/overview-eth/guide-how-to-stake-on-eth2-with-lighthouse)
  * [如何在Ubuntu上使用Teku参与Eth2 Medalla测试网质押](https://www.coincashew.com/coins/overview-eth/guide-how-to-stake-on-eth2-with-teku-on-ubuntu)
  * [如何在Ubuntu上使用Nimbus参与Eth2 Medalla测试网质押](https://www.coincashew.com/coins/overview-eth/guide-how-to-stake-on-eth2-with-nimbus)

**Somer Esat 指南:**

  * [Eth2.0质押指南 (Ubuntu/Medalla/Lighthouse)](https://medium.com/@SomerEsat/guide-to-staking-on-ethereum-2-0-ubuntu-medalla-lighthouse-c6f3c34597a8)
  * [Eth2.0质押指南 (Ubuntu/Medalla/Prysm)](https://medium.com/@SomerEsat/guide-to-staking-on-ethereum-2-0-ubuntu-medalla-prysm-4d2a86cc637b)

**保持更新Eth2的最新发展:**

  * [What’s New in Eth2 (Ben Edgington)](https://hackmd.io/@benjaminion/eth2_news/https:/hackmd.io/@benjaminion/wnie2_200817)
  * [Ethereum Blog (Danny Ryan的快速更新)](https://blog.ethereum.org/)
  * [Ben Edgington (Eth2规范注释)](https://benjaminion.xyz/eth2-annotated-spec/phase0/beacon-chain/#introduction)
  * [Jim Mcdonald (Attestant里的文章)](https://www.attestant.io/posts/)

**关于密钥:**

  * [Ledger Nano X (BLS Firmware更新)](https://www.ledger.com/first-ever-firmware-update-coming-to-the-ledger-nano-x)
  * [Attestant: ](https://www.attestant.io/posts/protecting-validator-keys/)《保护验证者密钥》

  
  

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

