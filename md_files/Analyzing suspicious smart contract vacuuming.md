# Analyzing suspicious smart contract vacuuming¶

This is the counterpart of [Blockchain Autopsies - Analyzing Ethereum Smart
Contract
Deaths](https://github.com/trailofbits/publications/tree/master/presentations/Blockchain%20Autopsies%20-%20Analyzing%20Smart%20Contract%20Deaths),
looking at suspicious patterns in the history of Ethereum, where contracts
would not be killed but simply emptied by attackers.

And, unlike [my other article about scanning smart contracts code for
bugs](stealing_ether.html), this one is about going through the history of the
blockchain to find suspicious patterns of transactions.

## Analysis¶

I ran a program to go through the full history of Ethereum, looking for
contracts with this pattern of transactions:

>   * contract creation
>
>   * various transactions from addresses in set A…
>
>   * _contract balance is now >0_
>
>   * period of inactivity
>
>   * one or multiple transactions from new address `b`, not in set A
>
>   * _contract balance is now ~0_
>
>

Where A is a set of addresses that interacted with the contract at the
beginning, and `b` is the attacker address that only interacted much later,
after a period of inactivity and caused the contract balance to decrease a
lot.

That’s all. My program took around a month to run, because it needed to go
through all the blocks in the history.

I found a lot of false positives. Most of them were multisig wallets or ICO
contracts, where a new (whitelisted) address collected all the money later on
An improvement would be to check that the address that empty the contract is
not mentionned somewhere in the contract code or storage: in that case it’s
pretty obvious it was whitelisted.

I went through all the matches to clean them up, and kept only the matches
that looked clearly suspicious after some reverse engineering and analysis on
Etherscan.

## Results¶

I found quite a few addresses that seem to siphon all the vulnerable contracts
they can find. Some of them even seem to use proxy contracts to revert the
transaction if the hack didn’t work.

Here are a few noticeable adresses I found:

>   *
> [0x80028f80C7d5959C3Eaf45A95bf3a1A0724352f6](https://etherscan.io/address/0x80028f80c7d5959c3eaf45a95bf3a1a0724352f6):
> I didn’t compute how much it made, but it’s the one I think siphoned the
> most accounts.
>
> Example: [a casino
> contract](http://eveem.com/code/0xEA1B4943F31777807Cdcd55b68D2Ba070E4A2d34).
>
>   *
> [0x90a0c432DA9d200f496FCDa91F4A3D42Ea3A6089](https://etherscan.io/address/0x90a0c432da9d200f496fcda91f4a3d42ea3a6089):
> This one has been active for a long time, and seems to have made more than
> 50 ETH!
>
> Example: [a
> contract](http://eveem.com/code/0x04b2582c70a1537202033e7F3265D38f4680109e)
> that sends 2x the amount it received (to the sender, and to a custom
> address).
>
>   *
> [0xC54100Fc034D412C21ba92Ccf2D916374AC22555](https://etherscan.io/address/0xc54100fc034d412c21ba92ccf2d916374ac22555):
> Experimented a lot but also emptied some contracts.
>
> Example: [a sort of a ponzi
> scheme](https://etherscan.io/address/0x8c720e5d2ee8AfBeE106cE48C9454150798B4234)
> that it emptied after years of inactivity.
>
>   *
> [0xACc6297e88D1de7d820F853D28453435dC000000](https://etherscan.io/address/0xacc6297e88d1de7d820f853d28453435dc000000):
> I already talked about this one in my [other article](stealing_ether.html).
> This one finds contract that it can take ownership of.
>
> Example:
> [Hotto_Old](https://etherscan.io/address/0x612f1BDbe93523b7f5036EfA87493B76341726E3).
>
>

You can find more in the raw results below.

These raw results also contained lots of instances of the same “quiz”
honeypot. This honeypot seems to have scammed lots of would-be blackhats, and
got money from them. I estimate that amount to at least thousands of dollars!

### Comparison with “Finding the Greedy, Prodigal and Suicidal Contracts at
Scale”¶

Here is an extract from [Finding The Greedy, Prodigal, and Suicidal Contracts
at Scale](https://arxiv.org/abs/1802.06038) :

> Furthermore, the maximal amount of Ether that could have been withdrawn from
> prodigal and suicidal con- tracts, before the block height BH, is nearly
> 4,905 Ether, or 5.9 million US dollars according to the exchange rate at the
> time of this writing.

If we look at the transaction history of the attackers I flagged (some of them
have been active for a few years already), there is `0xa0…` that made 50 ETH.
For the others it seems to be much lower. Because I also ran my tool Pakala to
[flag buggy contracts](stealing_ether.html), and these two approaches are
complimentary, I think I didn’t miss too much malicious activity.

It’s interesting to see how this picture differs with the quote in that paper:
I don’t think that more than 100 ETH was siphoned, in total. That’s very
different from the 4905 ETH they were talking about.

However, I measured the amount that got in the hands of the attackers. They
measured the amount that was contained in buggy contracts.

Still, that’s yet another proof that some addresses are actively scanning the
network and exploiting the contracts they can find.

## Appendix: raw results¶

This is the notepad where I triaged all of the suspicious activity I found. It
contains the output of my tool `0xaddr could have been hijacked by 0xaddr` and
comments from me.

    
    
    # Lots of people tried to interact with this contract, in the hope of getting
    # all its ethers:
    0x96E423291765C60e0Fbc2cFB2BC538Fb6CCdAdd9
    
    # An arithmethics puzzle, if you could solve it you would get 4 ETH :)
    0x3ac26f27595EffeB5e426BD093081EC30eBdD545 could have been hijacked by 0x00Ff6361b5727432c06bc186C29481BC9c290598
    
    # proxy contract: 0xCDc23a47c9e0Dc2D73a41E74beBEf5FE85842bE8. UselessReserveBank.
    0x7A83dB2d2737C240C77C7C5D8be8c2aD68f6FF23 could have been hijacked by 0x02B8C08c39AB43B1B2987ae98DF499F4EC833947
    
    # Rock-paper-scissors game.
    0x1d77340D3819007BbfD7fdD37C22BD3b5c311350 could have been hijacked by 0x04528fb91840ce4bCFC7390919a455D530da8ecb
    
    # 0.01 ETH. Anybody could withdraw.
    0xC8CE829C5D26c2F94E5bf64F90DbDf576b24213B could have been hijacked by 0x406c6cA639c42F038dDa19dF4897945006AB9aAB
    
    # Unicorn Meat Grinder DAO.
    # Timing is suspicious, but I think 0x517... needs to have been a member of the DAO.
    0xc7e9dDd5358e08417b1C88ed6f1a73149BEeaa32 could have been hijacked by 0x5175b2806a72f5c6553A8d32a6ECbb1A33cdD51d
    
    # proxy contract: 0xC798D5Ed657adeF1cA7bc6090c590319dfFE8979 that do the call and can revert if balance didn't increase (?)
    # used by 0x541fB7476aab8d6E19904461932Cc9C9cf0F8d7C (funded by 0x61fc...)
    # They are pretty active.
    # Cash stash: 0x4743958d9b4Ad675ED3bd6609Efff0271FF87f6E
    0x6E1f0aEf52b7b4b341ad27e00e394bd1C7F8B888 could have been hijacked by 0x541fB7476aab8d6E19904461932Cc9C9cf0F8d7C
    
    # Started September 7, 2017.
    # 0x8002... is also in the CryptoKitties business (having proxy contracts).
    # ~0.4 ETH. Seems like a flawed casino.
    0x22b8E9c359f7764bBaeA3B41fC794CBA04d4Ff32 could have been hijacked by 0x80028f80C7d5959C3Eaf45A95bf3a1A0724352f6
    # 0.1 ETH
    0x2e647Fd86c7EA77141d756f5442eB8b2947D5903 could have been hijacked by 0x80028f80C7d5959C3Eaf45A95bf3a1A0724352f6
    # 0.2 ETH
    0xA965db45248E737aEEf91243eB0bFf9F30F91B74 could have been hijacked by 0x80028f80C7d5959C3Eaf45A95bf3a1A0724352f6
    # 1.2 ETH
    0xf9938B7213eF1ffD15Aea74370d420FA41957cdf could have been hijacked by 0x80028f80C7d5959C3Eaf45A95bf3a1A0724352f6
    # 0.04+ ETH (not sure), attacker used multiple proxy contracts.
    0xa96f7d29dc792359B1Ce24C7c54230882deE1Be2 could have been hijacked by 0x80028f80C7d5959C3Eaf45A95bf3a1A0724352f6
    # 0.1 ETH.
    0xd4A02ad632a73480E53F5182EFD144FbEcC3D943 could have been hijacked by 0x80028f80C7d5959C3Eaf45A95bf3a1A0724352f6
    # 1.1 ETH.
    0xEA1B4943F31777807Cdcd55b68D2Ba070E4A2d34 could have been hijacked by 0x80028f80C7d5959C3Eaf45A95bf3a1A0724352f6
    # Using 0x49d654085C270B7e39be4c0023B67220F9404b5f as a proxy contract. 0.5 ETH.
    0xBC61561102d43Af2450c4F37a372d36878ce151F could have been hijacked by 0x80028f80C7d5959C3Eaf45A95bf3a1A0724352f6
    # 0.9 ETH. Lottery where the tickets cost 1/10 wei (which is 0) so they are free.
    0xe120100349a0b1BF826D2407E519D75C2Fe8f859 could have been hijacked by 0x80028f80C7d5959C3Eaf45A95bf3a1A0724352f6
    # 0.5 ETH. You can put your address in storage, then you get 0.1 ETH sent and you do it all again.
    0x4d498b18aBCF83A15D3364D7419A4eF382982c7d could have been hijacked by 0x80028f80C7d5959C3Eaf45A95bf3a1A0724352f6
    # 0.1 ETH.
    0x108ef05A9FDf103D1Da778aC9373308D0FE59B32 could have been hijacked by 0x80028f80C7d5959C3Eaf45A95bf3a1A0724352f6
    # 0.1 ETH.
    0x6e852Ba3CBC51D6fdf83AF554E1D2e633bE3f3c1 could have been hijacked by 0x80028f80C7d5959C3Eaf45A95bf3a1A0724352f6
    # 1 ETH. Anybody can "setPrices" then sell at whatever price they want.
    0xc1Df020c9D294EF98093607d98cFe14B9494BbeA could have been hijacked by 0x80028f80C7d5959C3Eaf45A95bf3a1A0724352f6
    # The 0x125... addresses are controlled by 0x8002...
    # 0.6 ETH. Anybody can set owner then withdraw.
    0xA820487E57656771b21AB533cB99e8d347Aa20EF could have been hijacked by 0x125D657d5Cd16Bf4864a2850D3F2541d9a0F3b50
    # 0.6 ETH. Anybody can withdraw.
    0x329219bE8810602a59b76dF9Ed7d52Dc3AFc3e8B could have been hijacked by 0x125D657d5Cd16Bf4864a2850D3F2541d9a0F3b50
    # 0.1 ETH. Used a proxy contract 0xC2045c4C23FC214199b3a82C6a5708642C2ad47b
    0x510467f65a600926Af2ed565419aD98CF1F706ED could have been hijacked by 0x125D657d5Cd16Bf4864a2850D3F2541d9a0F3b50
    # 0x8002 tried this quiz honeypot.
    0x4d200a0A7066Af311baBA7A647B1CCe54AE2f9A5 could have been hijacked by 0x2b122eAd009e73de6D76eae0bcc5D9CC52e67f08
    
    # 0x0x8cE169a578Ef4700743802412eAa91dc624Cd737 seems to have been quite active
    # 0.25 ETH. Anybody can get a refund() for 90% of the contract balance.
    0x5389c89F8a136dC7896F18B93C00F716A3E7E3A0 have been hijacked by 0x0x8cE169a578Ef4700743802412eAa91dc624Cd737
    # 0.1 ETH. Anybody can set owner and then withdraw.
    0x40a066c5eCe5B2cE2d0F15ad96c459C94C1a0416 could have been hijacked by 0x8cE169a578Ef4700743802412eAa91dc624Cd737
    # 0.1 ETH. Anybody can set owner and then withdraw.
    0x664a025E46043207b9609095CE643a8442FeA8a3 could have been hijacked by 0x8cE169a578Ef4700743802412eAa91dc624Cd737
    
    # 0x90a0c432DA9d200f496FCDa91F4A3D42Ea3A6089 started 2+ years ago. Active recently.
    # 9 ETH. Casino. 0x90a... used an intermediary contract: 0x5f4Ab4E2775c3DfF5B16635E1917c1FF5A8a9DB1
    0x3688C31568B011B541701311a0D31D41fffd8bdf could have been hijacked by 0x90a0c432DA9d200f496FCDa91F4A3D42Ea3A6089
    # 12 ETH! Allow anybody to withdraw (calls the caller once, and a supplied address once, each with the call value)
    0x04b2582c70a1537202033e7F3265D38f4680109e could have been hijacked by 0x90a0c432DA9d200f496FCDa91F4A3D42Ea3A6089
    # 24 ETH! Allow anybody to withdraw (calls the caller once, and a supplied address once, each with the call value)
    0xa1Bb86b79627a985Dfa1Ea9B0f655859d3Dc109B could have been hijacked by 0x90a0c432DA9d200f496FCDa91F4A3D42Ea3A6089
    # 1.9 ETH. A deposit() that increase your balance by 0.1 ETH. A withdraw() to withdraw your balance.
    0xF01FE1A15673A5209C94121C45E2121FE2903416 could have been hijacked by 0x90a0c432DA9d200f496FCDa91F4A3D42Ea3A6089
    # 2 ETH. Anybody could withdraw.
    0x8412AB39FC267f37249A4380f00cA19C8219b124 could have been hijacked by 0x90a0c432DA9d200f496FCDa91F4A3D42Ea3A6089
    # 5 ETH siphoned. Seems to be a casino but there is no intermediate contract to send the tx only if it will be won...
    0x671FA333efCdc8dCE84f6381c39796e4AF4feD75 could have been hijacked by 0x90a0c432DA9d200f496FCDa91F4A3D42Ea3A6089
    # 1 ETH, sent to an invalid address (wrong padding), and lost.
    0xC4520E8eFbd538b20063033959599b32B8a31d67 could have been hijacked by 0x90a0c432DA9d200f496FCDa91F4A3D42Ea3A6089
    
    # 0xACc6297e88D1de7d820F853D28453435dC000000 was actively exploiting as well.
    # change owner -> withdraw, 1.3 ETH
    0x612f1BDbe93523b7f5036EfA87493B76341726E3 could have been hijacked by 0xACc6297e88D1de7d820F853D28453435dC000000
    # change owner -> withdraw, 0.5 ETH
    0xcEaE314D493855918AB12705D944D3aF81beEB3D could have been hijacked by 0xACc6297e88D1de7d820F853D28453435dC000000
    # change owner -> withdraw, 0.1 ETH
    0xC8A074De1C6bF01a75cD29892c91B6C354200f75 could have been hijacked by 0xACc6297e88D1de7d820F853D28453435dC000000
    
    # hijacker got money from 0xe9f... 0x2ca... 0x4469...
    # 0.2 ETH
    0x8c720e5d2ee8AfBeE106cE48C9454150798B4234 could have been hijacked by 0xC54100Fc034D412C21ba92Ccf2D916374AC22555
    # 0.4 ETH
    0x89392Ecd850BDe121F5d75aE0157A99808e0C288 could have been hijacked by 0xC54100Fc034D412C21ba92Ccf2D916374AC22555
    # 0.4 ETH
    0x7e54d7dC4A941901A58Bab838FcF10537Fef6F0C could have been hijacked by 0xC54100Fc034D412C21ba92Ccf2D916374AC22555
    # 0.3 ETH
    0xA34f75BD76b044b18C16DbF5481b05fdf75277AF could have been hijacked by 0xC54100Fc034D412C21ba92Ccf2D916374AC22555
    # 0.3 ETH
    0x1F512db6A4b92D0bF29b33826734D630Ed3D531C could have been hijacked by 0xC54100Fc034D412C21ba92Ccf2D916374AC22555
    # <1 ETH
    # proxy used by 0xC54100Fc034D412C21ba92Ccf2D916374AC22555: 0x57A2a07F3025ffa5B8c099Ce568801a67c86c44e
    0x0E6277c95F97b4C71b6864ce94Ab617d6784c4bc could have been hijacked by 0xC54100Fc034D412C21ba92Ccf2D916374AC22555
    # ~0.2 ETH
    # proxy used by 0xC54100Fc034D412C21ba92Ccf2D916374AC22555: 0x57A2a07F3025ffa5B8c099Ce568801a67c86c44e
    0xd05dc25d8dad48fb9cF242D812D8Fb4A653aDB95 could have been hijacked by 0xC54100Fc034D412C21ba92Ccf2D916374AC22555
    
    # 0.2 ETH
    0x9279d4d65Dca0744365C4424c4023DC21897A80a could have been hijacked by 0xca99cA990a0FC75158F87340a7Cb07738F644cb4
    
    # 0.5 ETH, called a function to empty the contract that anybody could call
    0xa645ab04933aE56cfD93d905BD40Aa1150e0E4Fd could have been hijacked by 0xEA4c732d337A61677518a5483fF4B57bDE2B9097
    
    
    
    # Couldn't decompile this one. Not sure what happened.
    0x6CFD5Cb1d9145513D767bAA3eADBEDa0e1A5E605 could have been hijacked by 0x26D7d53F7bc0bD78199A1362f6A0787a391BA58c
    # flawed casinos, I think
    0xAA90725a3fC3432B3dbf2d6d050b2265F2c5c5d2 could have been hijacked by 0x90a0c432DA9d200f496FCDa91F4A3D42Ea3A6089
    0xE61f6b6B20B54261002668cF6B81DE9A6AC0Cb3A could have been hijacked by 0x90a0c432DA9d200f496FCDa91F4A3D42Ea3A6089
    
    # quiz
    0x4d200a0A7066Af311baBA7A647B1CCe54AE2f9A5 could have been hijacked by 0x2b122eAd009e73de6D76eae0bcc5D9CC52e67f08
    0x8bBF2d91E3c601DF2C71c4EE98e87351922F8AA7 could have been hijacked by 0x65E48FF0A4E9a920422049d8C8E3E34D577A6d36
    0x7b3c3A05FCbf18dB060EF29250769CEe961D75aC could have been hijacked by 0x6b35C9f9670C0641e3d5e80642992223D1FFec7b
    0x0D74fb34583D4E14BF9634bFd1887E86d3C1F139
    0x9d81AdbAd5DC8C4D474E080466D4741bEC89dF62
    0x455729Af8890A334b4F6cd6bb72c778922e42aD7 could have been hijacked by 0x825D5D0dF3B2D59f69CC673F041ca91A296b8183
    0x137e531680b5D1F5645Cd73a450323f1645d5034 could have been hijacked by 0x910510E16Bd5f75BA754436c915b2B29C56691be
    0xdDa2044b39FDB4dB77Ac085866179C548e5d0f15 could have been hijacked by 0x3D6eCe242b1696ab8Be17bF1A30EA9e98978eA64
    0x5E521B660fe8Ac575F1d7201F2237724EE531F1D could have been hijacked by 0x701EAF444308ee377527ec3F4685Fe0E1Bc13b52
    0xce6B1AFf0fE66da643D7A9A64d4747293628D667 could have been hijacked by 0x8a1f32676BD197E6E97945B646f2979d521Ca8eB
    0x5b39AfA22A9dEBd9247bF84B68A79b8736c2Ba4E could have been hijacked by 0xB26A4D2B72CB161DCBBC33d1198B1795BD2E5b2d
    0x3fAb284a3cD0A6d88d18D0fdA4bc1a76cdacd68A could have been hijacked by 0xA537A25A9F9058e533CF27D9EA84B63f38b70953
    0xbC272B58E7cD0a6002c95aFD1F208898D756C580 could have been hijacked by 0xfcb6B730e88Cb61C0c36446342FC999f71b4126e
    0xa630823Bd70AB8E8e2d6E62089d3837dB1887Bf6 could have been hijacked by 0x86Fa50F8E1CE0798a7502a88941610AE61D396F3
    0xC5ce9C06a0CAF0E4cbd90572b6550FeAFd69b740 could have been hijacked by 0xa0a839BaCFCf680E43a863Fc6B17ee3f44E0EE24
    0xC304349d7Cc07407B7844d54218D29D1A449b854 could have been hijacked by 0xc958073a27CdE5c020ca3F399241b769dbB25977
    0xEFBfc3f373c9cc5c0375403177d71Bcc387D3597 could have been hijacked by 0x71121335Da3b7AABDbCE3515959e0B74ffD7Cff7
    # the following is another kind of quiz
    0x2E4eB4585cB949E53212e796cEF13d562C24374B could have been hijacked by 0x04cCB24C5Ad2357681Ae1c19B4aA16D77d8a414c
    0x1fBf025AD94ddE79f88732F79966A9A435F2772f could have been hijacked by 0x4ad610b4A338c9d1c4820ecc53ebC68d35b35962
    0xcEA86636608BaCB632DfD1606A0dC1728b625387 could have been hijacked by 0x1D971732EC0fc7223204A34D5e915Fa502c893Ed
    0x70bf9Df6967Dc96156e76Cc43b928A7eF02E159a could have been hijacked by 0x0ae9c6bea2EBfa7657d19ee7A7fCD7939E024c20
    0x403F614Ea176BDd865Ab0377831f487987179cEa could have been hijacked by 0x9196d74440f6C254cB5861c9076653FA6243670a
    0x97D25094830592B0f9FA32F427779a722Ed04b34 could have been hijacked by 0x6B7e7BD7410F1bB9105c6D55176a52Bc94c4B35a
    0x59434a7b9aEEbE94045D3715aa020F6a1d7875aD could have been hijacked by 0xE6FBe6582648dD4dAD45cd00392e84BfB179Ee6B
    0x4AeC37ae465E1D78649aFF117baB737c5fb4F214 could have been hijacked by 0x3535cdC4f9451aaa9F1aCdf92a83167028C449e0
    0x4a73D9fe078fA67601047F88C3e6C270602E5709 could have been hijacked by 0x2A7d6545daA76bF35140FC023c8Ea82C71E57EAd
    0xBD53a4Db4003C59070aBbFa4E6C31aFBF0B26843 could have been hijacked by 0x123456aD3796fd93f29ce21E513D375784869174
    0x5DAC036595568Ff792f5064451b6B37e801ecaB9 could have been hijacked by 0x003be5Df5FeF651EF0C59cD175c73ca1415f53eA
    0x8D4EB49f0eD7EE6d6E00fc76eA3E9C3898bf219D could have been hijacked by 0xCBd8E8675A020015D6Cd6E97a15ee74b4f889EC7
    0x0cfA149c0a843e1f8d9bC5C6e6bebf901845CeBE could have been hijacked by 0x780F42557E6fbA598aC22D0A477831248D927DDB
    0x75658ed3DbA1E12644d2CD9272BA9ee888f4c417 could have been hijacked by 0x4F074B3C397e8645F9714B27c3b60C79423ED7F4
    0xF0344800bd3Ffa687e4D780357961B28995a5F46 could have been hijacked by 0xebef930796883E0A1D2f8964AEd7a59FE64e68E6
    0x13c547Ff0888A0A876E6F1304eaeFE9E6E06FC4B could have been hijacked by 0xF3A7c0Ce518FDbA4a02D01A80108D5F250044363
    

Previous: [ How to steal Ethers: scanning for vulnerable contracts
](stealing_ether.html)   Next: [ The bZx attacks explained ](bzx.html)

### [palkeo](../../index.html)

  * [Projects](../index.html)
  * [Blog articles](../../blog/index.html)
  * [Links](http://links.palkeo.com)
  * [Repository](http://repo.palkeo.com/)
  * [About](../../about.html)

##  18 February 2019

  * Language: [English](../../blog/language/english.html)
  * Tags:  [ethereum](../../blog/tag/ethereum.html) [pakala](../../blog/tag/pakala.html)

### [Table of Contents](../../index.html)

  * Analyzing suspicious smart contract vacuuming
    * Analysis
    * Results
      * Comparison with “Finding the Greedy, Prodigal and Suicidal Contracts at Scale”
    * Appendix: raw results

### Related Topics

  * [Projects](../index.html)
    * [Ethereum: hunting for buggy smart contracts](index.html)
      * Previous: [The bZx attacks explained](bzx.html "previous chapter")
      * Next: [How to steal Ethers: scanning for vulnerable contracts](stealing_ether.html "next chapter")

(C)2020, palkeo.

