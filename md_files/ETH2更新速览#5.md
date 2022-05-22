[![logo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAICAYAAAD5nd/tAAAACXBIWXMAAA7DAAAOwwHHb6hkAAABj0lEQVQoz12Sv0vDQBTHT0HrD4QWRJRLi3QQOojon1JxUhcFQQeViknrJjiIglgRhW4OTiLSWXB10MnJoToI0lp6ESu1TZNc/L7LFcGDD+8u4X3y3r0wKeUUeAqwEBVYZa9amhCb0bydjbdti/vAsy0jALPYp0EZSODq91W8W2AQPGqZg9CUvkvGUv08fSEywwGESDIaoAW+QQHJbWEq+Y+mqc8OCV3wASZBzP+qJJ8ZY2JrpKgqMvk8Yh8kvL6b6sZ+WZicki/BIBgFUVCk5ywsTr4ikvxI+l4F+w20e21bcQiNGUiZ2OZdSGLYr+jW9+hcw3NUx/DBY6pSCcELZCQ8RMtvOK+K9aErO5ugCqdJCDESVVzSwgMSQhLRwjMl1C1Xw+H4Mf/zPQFhxN5J3qrEbGJRmGMDwjIMYfF+yDNauK+FvVp4qlqG6F4PpY3goMIWxebdiVdbi1CiDC+dtwBdfmcA+X/CQqflFGQP6nf5+20C6blB4yYnRW7chcihCYbwFk0ZzAES9eiIq+DiFyR9m3ZUxiupAAAAAElFTkSuQmCC)![logo](/static/9c635c914229a850d1a9fd284014bdd0/65e33/eco_logo.png)](/)

  * [新闻资讯](/)

  *   * [零时学院](/c0llege)

  * [开发者门户](/develop)

  * [生态漫游](/ecos)

Ξ

Search by [](https://www.algolia.com/?utm_source=react-
instantsearch&utm_medium=website&utm_content=&utm_campaign=poweredby)

## ETH2更新速览#5

本期内容包括多客户端公共测试网、Eth2浏览器、Eth2网络电话会议……

* * *

DR

Danny Ryan 2019-12-07

来源 | Ethereum Blog

  

![以太坊周刊更新速览开头.png](https://i.ibb.co/SdPYLS4/8becff9df1-png-8703fb498c.png)

  

# 要点首看：

  * Parity团队的[Shasper客户端加入](https://twitter.com/sorpaas/status/1202651945430929409)Prysmatic团队的Sapphire测试网（首个以太坊多客户端公共测试网）
  * 两个eth2区块浏览器上线 – Bitfly的[beaconcha.in](https://beaconcha.in/)与[Etherscan浏览器](https://beacon.etherscan.io/)
  * 开展首次eth2网络电话会议，以解决所有网络问题 – [Ben的笔记](https://hackmd.io/@benjaminion/BJ3YqrSTr)、[Mamy的笔记](https://gist.github.com/mratsim/fef2b0a7c5a335ac6bc61c01592b3fea)
  * 开展首次[eth2阶段2社区电话会议](https://github.com/ethereum/eth2.0-pm/issues/103)，以整合研究成果
  * 为分叉选择规则提供[解决方案](https://github.com/ethereum/eth2.0-specs/pull/1495)，确保分叉选择区块头状态与FFG最终确定信息相匹配
  * 新BLS签名标准的[演示](https://www.youtube.com/watch?v=dMFgaeRdsfU&feature=youtu.be&t=1009)、[规格](https://github.com/ethereum/eth2.0-specs/pull/1499)与[实现](https://github.com/ethereum/py_ecc/pull/79)

###  

# Shasper加入Prysmatic团队的测试网

Parity团队研发的eth2
[Shasper客户端](https://github.com/paritytech/shasper)成功在Prysmatic的Sapphire
测试网上运行，标志着第一个eth2公共多客户端测试网的诞生。这是一个激动人心的开始，下个月将陆续出现更多多客户端测试网。

现在就可以通过拉取Shasper代码库，使用命令，连接到Sapphire测试网上。如果想尝试连接，请按照[此处的说明](https://github.com/paritytech/shasper/pull/191)进行操作。

###  

# Eth2区块浏览器上线

最近已经上线了两个区块浏览器了！目前，这两个区块浏览器都在追踪[Prysmatic Labs团队Sapphire
测试网](https://prylabs.net/)的动向，为构建信标链的验证者提供每个slot的信息。

几周前，Bitfly上线了beaconcha.in区块浏览器，并不断添加[令人感到兴奋的功能](https://twitter.com/etherchain_org/status/1202506562746638336)。
Etherscan前天也上线了他们的区块浏览器，功能和数据展示页面看起来都很酷。两者都是在线监测Prysmatic的测试网及其他测试网的绝佳选择。

我们很高兴见到越来越多适用于eth2客户端和测试网的用户/开发者工具投入建设当中：)

###  

# 首次eth2网络专题电话会议

到目前为止，我们一直依赖于以github上的问题/代码请求(pull-
requests)、临时聊天、主要eth2电话会议以及面对面会议的形式来组织有关eth2规范网络组件的工作。这些方式在很大程度上已经起到了足够好的作用，但是对分片式区块链协议网络的研究和建设，还应得到越来越多的关注与资源支持。

为此，我们本周进行了首次[eth2网络专题电话会议](https://github.com/ethereum/eth2.0-pm/issues/106)。尽管此次电话会议没有像eth2常规电话会议那样进行实时直播，但它是公开的，向所有贡献者开放。感谢促成此次电话会议举行的各个eth2团队的p2p网络专家。由于额外的协调工作，我本来很抗拒参加此次电话会议，但首次电话会议卓有成效，我期待下一次的会议。

和往常一样，由Ben Edgington（[会议笔记](https://hackmd.io/@benjaminion/BJ3YqrSTr)）和Mamy
Ratsimbazafy（[会议笔记](https://gist.github.com/mratsim/fef2b0a7c5a335ac6bc61c01592b3fea)）来做好会议记录。由于仍然有很多值得我们去研究的地方，所以下次的电话会议时间大约定在2周内。

###  

# 首次eth2阶段2社区电话会议

感谢Quilt团队的Will Villanueva组织了首次[eth2
阶段2社区电话会议](https://github.com/ethereum/eth2.0-pm/issues/103)。与新提上日程的网络和轻客户端专题电话会议一样，阶段2的相关内容足以确保电话会议的定期进行，以使研发工作的开展更有条理。

首次电话会议内容主要是对涉及的众多团队和个人工作的常规更新及各种正在进行的线程调查。可以在[此处](https://github.com/ethereum/eth2.0-pm/issues/103#issuecomment-561938586)查阅笔记。接下来的电话会议旨在更深入探讨有关特定技术问题。

阶段2的主要目标是进行第一轮无状态协议研究，并将研究发现范围缩小，以得到一个能在2020年实施的更具体计划中。这些阶段2电话会议是实现这一目标的重要一步。

###  

# 分叉选择状态修复

由Yan X Zhang领导的圣何塞州立大学研究人员致力于形式化eth2共识机制（Casper FFG）和分叉选择规则（LMD GHOST）的共同属性。
在公布工作进度之前，他们在FFG +
GHOST的互通方面中发现了一个极端案例，即区块树的分支可能包含最新的已验证/已确认的区块，但实际上这些区块在链上的状态并未显示为已验证/已确认。在分叉选择中留下这样的“不可行”分支可能会导致验证者的投票与本地最终确定信息不一致的情况，并且在某些情况下可能导致信标链活性的丧失。可以在[此处](https://notes.ethereum.org/@djrtwo/HynY6CthS)阅读有关此特定情况和建议解决方案的更多信息。

在我们的规范存储库中[有一个修复正在审核当中](https://github.com/ethereum/eth2.0-specs/pull/1495)，它能够解决这种情况。我们希望此修复将在一周内发布。

###  

# 新BLS标准的规范与实现

期待已久的BLS标准最近在[IETF第106次会议](https://www.ietf.org/how/meetings/106/)上亮相以征求公众意见。可以自行查看此次演示和幻灯片。该演示按计划进行，新BLS标准有望被许多区块链项目采用，并（最终）被IETF社区采用。在漫长的IETF征求意见过程结束之前，我希望以太坊基金会和其他许多项目能尽快更正式地宣布这一标准的预期用途。

规范存储库中有两个正在审核的代码请求草稿（[1][https://github.com/ethereum/eth2.0-specs/pull/1398
](https://github.com/ethereum/eth2.0-specs/pull/1398)[2][https://github.com/ethereum/eth2.0-specs/pull/1499）以及[正在py_ecc库中审核](https://github.com/ethereum/py_ecc/pull/79)的新标准实现。审核完成后，我们将生成新的BLS测试向量，供eth2客户端常规使用，目的是为了将测试网切换到实施一月份面世的修改后BLS方案。](https://github.com/ethereum/eth2.0-specs/pull/1499%EF%BC%89%E4%BB%A5%E5%8F%8A%5B%E6%AD%A3%E5%9C%A8py_ecc%E5%BA%93%E4%B8%AD%E5%AE%A1%E6%A0%B8%5D\(https://github.com/ethereum/py_ecc/pull/79\)%E7%9A%84%E6%96%B0%E6%A0%87%E5%87%86%E5%AE%9E%E7%8E%B0%E3%80%82%E5%AE%A1%E6%A0%B8%E5%AE%8C%E6%88%90%E5%90%8E%EF%BC%8C%E6%88%91%E4%BB%AC%E5%B0%86%E7%94%9F%E6%88%90%E6%96%B0%E7%9A%84BLS%E6%B5%8B%E8%AF%95%E5%90%91%E9%87%8F%EF%BC%8C%E4%BE%9Beth2%E5%AE%A2%E6%88%B7%E7%AB%AF%E5%B8%B8%E8%A7%84%E4%BD%BF%E7%94%A8%EF%BC%8C%E7%9B%AE%E7%9A%84%E6%98%AF%E4%B8%BA%E4%BA%86%E5%B0%86%E6%B5%8B%E8%AF%95%E7%BD%91%E5%88%87%E6%8D%A2%E5%88%B0%E5%AE%9E%E6%96%BD%E4%B8%80%E6%9C%88%E4%BB%BD%E9%9D%A2%E4%B8%96%E7%9A%84%E4%BF%AE%E6%94%B9%E5%90%8EBLS%E6%96%B9%E6%A1%88%E3%80%82)

BLS标准还消除了发布eth2质押合同的最终障碍之一。Runtime
Verification团队当前正在完成关于质押合同字节码的正式验证和分析的报告。预计该报告将在本月底公布，以供公众审查，之后我们就真的可以启动新BLS标准了🚀。

  
  

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

