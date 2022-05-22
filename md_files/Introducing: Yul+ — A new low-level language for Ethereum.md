[ ![Fuel Labs](https://fuel-labs.ghost.io/content/images/2021/09/logo-
full-1.png) ](https://fuel-labs.ghost.io)

  * [Home](https://fuel-labs.ghost.io/)
  * [About](https://fuel-labs.ghost.io/about/)

[ ](https://twitter.com/fuellabs_ "Twitter")

Subscribe

[Ethereum](https://fuel-labs.ghost.io/tag/ethereum/)

# Introducing: Yul+ — A new low-level language for Ethereum

Today, Fuel Labs introduces Yul+, which adds various QoL features to Yul, a
low-level intermediate language for the Ethereum Virtual Machine.

  * [ ![Fuel Labs](/content/images/size/w100/2021/09/logo.svg) ](/author/fuel-labs/)

#### [Fuel Labs](/author/fuel-labs/)

Mar 24, 2020 • 4 min read

![Introducing: Yul+ — A new low-level language for
Ethereum](/content/images/size/w2000/2021/09/1_UODQtnszf0FhSwM7ZSEJ4Q.png)
Fuel Labs Inc. introduces Yul+ a new low-level language for Ethereum.

Yul is an incredible little language written by the Solidity Developers as a
compilation target for further optimizations. It features a simplistic and
functional low-level grammar. It allows the developer to get much closer to
raw EVM than Solidity, and with that comes the promise to drastically improved
gas usage.

[Fuel Labs](https://github.com/fuellabs) has implemented itsinitial open-beta
optimistic rollup contract largely with Yul, but we noticed that with the
addition of even a tiny number of basic language additions, our code could
become more legible and efficient.

 _ _Yul+ can be looked at as an experimental upgrade to Yul, and Yul might aim
to integrate some of its features natively at a later time.__

## Some Yul Basics

A basic Yul contract with a constructor and runtime

    
    
    object "EmptyContract" {
      code {
      
        // Your constructor code
        
        datacopy(0, dataoffset("Runtime"), datasize("Runtime"))
        return(0, datasize("Runtime"))
      }
      object "Runtime" {
        code {
        
           // Your runtime code
           
        }
      }
    }
    

Handling calldata

    
    
    // copy calldata to memory
    // this copies 36 bytes of transaction calldata to memory position 0
    
    calldatacopy(0, 0, 36)
    

Managing memory

    
    
    // store and read memory
    // store 0xaa at memory position 100
    
    mstore(100, 0xaa)
    
    // load 32 byte chunk from memory position 100 and assign to someVar
    
    let someVar := mload(100)
    

Hashing

    
    
    // hash memory position 0 to 0+32, assign result to someHash
    
    let someHash := keccak256(0, 32)
    

State storage

    
    
    // store value 0xaa in state storage slot 3
    
    sstore(3, 0xaa)
    
    // get value from state storage 3 and assign to someVar
    
    let someVar := sload(3)
    

Functions, conditions, loops, and switches

    
    
    // Functions and conditions
    
    function someMethod(someVar, someOther) -> someResult {
       if eq(someVar, someOther) {
          someResult := 0x45
       }
    }
    
    // Loops
    
    for { let i := 0 } lt(i, 100) { i := add(i, 1) } {
       // some loop code
    }
    
    // Switches
    
    switch someVar
    case 0 {
       // when someVar == 0
    }
    
    case 1 {
       // when someVar == 1
    }
    
    default {
       // default
    }
    

## Yul+ Features

  *  _ _All existing Yul language features__
  * Enums ( ** **enum**** )
  * Constants ( ** **const**** )
  * Ethereum standard ABI signature generation ( ** **sig”function …”**** )
  * Booleans ( ** **true**** , ****false**** )
  * Safe math by default (i.e. over/under flow protection for addition, subtraction, multiplication)
  * Injected methods ( ** **mslice**** and ****require**** )
  * Memory structures ( ** **mstruct**** )

## Usage

Enums, constants, and Booleans

    
    
    enum Colors (
       Red, // 0
       Blue, // 1
       Green // 2
    )
    
    // Constant someConst will equal 1
    
    const someColor := Colors.Blue
    
    // Constant someBool will equal 0x1
    
    const someBool := true
    
    

Ethereum standard ABI signature generation for method sigs and topics:

    
    
    // someVar will equal 4 byte method signature 0x6057361d
    
    let someVar := sig”function store(uint256 val)”
    
    // someTopic will equal 32 byte topic hash 0x69404ebde4a368ae324ed310becfefc3edfe9e5ebca74464e37ffffd8309a3c1
    
    let someTopic := topic”event Store(uint256 val)”
    

All maths are now safe by default, which can be disabled in the compiler if
desired.

    
    
    let someVar := add(3, sub(4, 2))
    
    // will compile to this, with safeAdd, safeSub methods injected
    
    let someVar := safeAdd(3, safeSub(4, 2))
    

We add for convenience a memory slice __mslice__ and __require__ if true

    
    
    mstore(300, 0xaabbccdd) // note, mstore left pads zeros by 28 bytes
    
    let someVal := mslice(328, 3) // will return 0xaabbcc
    
    require(gt(someVal, 0)) // someVal > 0 or revert(0, 0) nicely
    

Lastly, we enable memory structures. These are used to describe already-
existing structures in memory, such as calldata, hash data, or any data with
structure written to memory.

It offers a wide range of positioning, offset, hashing, indexing, and
organizational features to better handle memory with neat efficient pre-made
functions injected on-demand. We still keep to using a functional notation of
injected functions, which doesn’t break existing Yul grammer style.

    
    
    // Let’s assume we assign some calldata to memory position 0
    
    // this describes an abstract memory construction:
    
    mstruct SomeCalldata(
       signature: 4,
       value: 32,
    )
    
    let methodSig := SomeCalldata.signature(0) // slices out sig
    let someVal := SomeCalldata.value(0) // slices out value
    
    // we also get some nice indexing and offset features
    
    SomeCalldata.value.position(0) // equals 4 (i.e. 0 + 4)
    
    // Index ordering values as well
    
    SomeCalldata.signature.index() // equals 0
    
    SomeCalldata.value.index() // equal 1
    
    // Keccak hashing
    
    SomeCalldata.value.keccak256(0) // equals 32 byte hash of value
    
    // Calculate entire size of calldata structure
    
    SomeCalldata.size(0) // equals 36 (i.e. 4 + 32)
    

## Example: Yul+ SimpleStore Contract

    
    
    object “SimpleStore” {
       code {
          datacopy(0, dataoffset(“Runtime”), datasize(“Runtime”))
          return(0, datasize(“Runtime”))
       }
       object “Runtime” {
          code {
             calldatacopy(0, 0, 36) // copy calldata into memory
             
             mstruct Calldata( // mstruct describes calldata
                sig: 4,
                val: 32
             )
             
             switch Calldata.sig(0) // get signature at positive zero
             
             case sig”function store(uint256 val)” { // store method
                sstore(0, Calldata.val(0))
             }
             
             case sig”function get() returns (uint256)” { // get method
                mstore(100, sload(0))
                
                return (100, 32)
             }
          }
       }
    }
    

## Try it Now in Your Browser!

[Yul+ - Low-Level Ethereum DevepmentFuel is a trustless scalable Ethereum
side-chain implimentation which can quadratically scale to 2 million
TPS.![](https://yulp.fuel.sh/yulp.6e62bcb6.png)Low-Level Ethereum
DevepmentNick Dodson; John Adler](https://yulp.fuel.sh)

## Wrapping Up

In conclusion, the Fuel Labs team hopes to expand the possibilities for the
Ethereum Virtual Machine by creating more low-level alternatives which we use
everyday to build high-performance optimistic rollup scalability for the
ecosystem.

In the meantime, for more info and to keep up to date with our work:

Website: [https://fuel.sh](https://fuel.sh/)

Twitter: <https://twitter.com/FuelLabs_>

GitHub: <https://github.com/FuelLabs/yulp>

Gitcoin: <https://gitcoin.co/grants/199/fuel-labs>

## Sign up for more like this.

Enter your email Subscribe

[ ![Beyond Monolithic Online
Hackathon](/content/images/size/w600/2022/05/BeyondMonolithicHackathonLQ.png)
](/beyond-monolithic-hackathon/)

[

## Beyond Monolithic Online Hackathon

Be a part of the next generation of blockchain by building dapps using the
Sway smart contract language on Fuel, the Fastest Modular Execution Layer, for
a chance to win up to $100,000 in prizes!

](/beyond-monolithic-hackathon/)

  * [ ](/author/ruben/)
  * [ ![Fuel Labs](/content/images/size/w100/2021/09/logo.svg) ](/author/fuel-labs/)

[Ruben Amar](/author/ruben/), [Fuel Labs](/author/fuel-labs/) May 8, 2022 • 3
min read

[ ![Meet the team behind Fuel](/content/images/size/w600/2022/03/JohnA.png)
](/meet-the-team-episode-1/)

[

## Meet the team behind Fuel

For the first episode of our "Meet the team behind Fuel" series, we are
thrilled to hear from John Adler, Co-founder of Fuel Labs and Celestia Labs.

](/meet-the-team-episode-1/)

  * [ ](/author/ruben/)
  * [ ![Fuel Labs](/content/images/size/w100/2021/09/logo.svg) ](/author/fuel-labs/)

[Ruben Amar](/author/ruben/), [Fuel Labs](/author/fuel-labs/) May 4, 2022 • 2
min read

[ ![Introducing Fuel - The Fastest Modular Execution
Layer](/content/images/size/w600/2022/04/Fuel_Trailer_Still_10.jpeg)
](/introducing-fuel-the-fastest-modular-execution-layer/)

[

## Introducing Fuel - The Fastest Modular Execution Layer

Today, we introduce the fastest modular execution layer: Fuel, adding a new
chapter to the blockchain scalability story.

](/introducing-fuel-the-fastest-modular-execution-layer/)

  * [ ![Fuel Labs](/content/images/size/w100/2021/09/logo.svg) ](/author/fuel-labs/)

[Fuel Labs](/author/fuel-labs/) Apr 18, 2022 • 4 min read

[Fuel Labs](https://fuel-labs.ghost.io) (C) 2022

[Powered by Ghost](https://ghost.org/)

