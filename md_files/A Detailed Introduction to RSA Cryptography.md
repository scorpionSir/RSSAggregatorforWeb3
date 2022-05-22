Close

Menu

  * [About Us](https://blog.sigmaprime.io/pages/about-us.html)

[![Blog Logo](./imgs/blog/sigp-logo-black.png)](https://blog.sigmaprime.io/)
__Menu

# A Detailed Introduction to RSA Cryptography

[Kristian Mcdonald](https://blog.sigmaprime.io/author/kristian-mcdonald.html)
| Mon 27 August 2018 Updated on Mon 27 August 2018 Estimated read time: 42 min

## Table of Contents

  * Introduction
  * Basic Overview of RSA
  * Background Mathematics
    * Bezout's Identity
    * Elements in \\(\mathrm{Z_n^\times}\\)
    * \\(\mathrm{Z_n^\times}\\) is a Group
    * Properties of the Totient Function
    * An Interim Result
    * Fermat's Little Theorem
    * A Version of the Chinese Remainder Theorem
  * RSA Cryptography
    * Key Generation
    * Message Encryption and Decryption
    * Verifying that RSA Encryption/Decryption Works
    * Multiplicative Homomorphicity in RSA
    * Why Does RSA Work?
    * Why Is RSA Constructed the Way It Is?
    * Generalising RSA: Are More Primes Better?
  * Conclusion
  * References

## Introduction

Whether in the form of our basic communications, our banking transactions, or
even driving our cars, the transmission of digital information has a
significant impact on the way we live our lives. As more information from our
daily life is digitised, access to secure means of privately transmitting
information becomes increasingly important. In effect, the commercialisation
of our digital footprint has turned information into a kind of currency - and
if information is a currency, privacy is the difference between keeping your
money in the bank versus freely giving it away.

The history of cryptography has involved a relatively small number of major
breakthroughs as it turns out that robust cryptographic techniques that may
realistically be implemented are not easy to discover. Thus, when
breakthroughs happen, they garner a lot of attention. Though RSA is now
considered an older technique and is often replaced by newer methods using
elliptical curves, It's fair to say that the discovery of RSA cryptography
ranks among the most important breakthroughs in cryptography. Whether you're
interested in how blockchains function, the general history of cryptography,
or even the practical utility of seemingly esoteric number theoretic results,
learning how RSA cryptography works is a useful exercise that will expand your
toolkit and improve your understanding of the modern world.

The purpose of this article is to provide a relatively self-complete
presentation of the inner workings of RSA. It's hoped that readers interested
in RSA can make their way through the article and emerge confident that they
understand how RSA works. The proof that RSA cryptography is valid relies on
multiple interesting mathematical results. This article aims to collect the
necessary background mathematics in one place, including explicit proofs for
key results, to provide readers with a self-complete account of RSA.

A reader hoping to understand RSA without delving into mathematical details
may find the article overly complex, though may still benefit from reading the
summary content. Similarly, an expert in number theory will likely find the
details in some proofs "too comprehensive". However, readers who lack
expertise in these matters, but are willing to ``get their feet dirty,'' will
hopefully benefit from the explicit details provided in the article and the
self-complete nature of the presentation. Readers who would prefer to minimise
their exposure to technical details can find other elementary introductions to
RSA elsewhere online. There are also a number of good technical articles
online, though often a reader must trust the results of theorems that are not
explicitly (or incompletely) proven within the article and/or search further
afield to fill in details. Perusing a number of online articles, it appeared
that many were insufficient for a reader who sought to understand every detail
regarding how RSA works. This observation formed the motivation for the
present article.

## Basic Overview of RSA

RSA cryptography was the first1 viable implementation of what is known as
_public key cryptography_. Public key cryptography is both a powerful and
useful form of cryptography that allows anyone to send an encrypted message to
another individual. The basic idea is that an individual who wants to send a
private message must first encrypt the message with the receiver's public key.
An individual's public key may be openly broadcast to any interested party,
allowing anyone to send an encrypted message. Importantly, knowledge of the
public key does not compromise the security of encrypted messages. Upon
receipt of an encrypted message, the receiver uses their private key to
decrypt the message. Provided the receiver doe not share their private key
with anyone else, they alone possess the ability to easily decrypt messages
encrypted with their public key. Attackers seeking to decrypt a sender's
message must use brute force to try and "crack the code". RSA cryptography
relies on a number of parameters, including the length of the keys. For
appropriately chosen parameters, it is technologically infeasible to implement
a successful brute force attack on an encrypted message. Consequently an
attacker is highly unlikely to access the content of an encrypted message.

The mathematics that underlines RSA encryption and decryption is described in
detail in subsequent sections of this article. Here, we merely note that a
user's public key is specified by a pair of integers \\((e,n)\\), while their
private key is specified by a related pair \\((d,n)\\). To encrypt a message,
a sender first converts the message into a numerical form (call this \\(M\\)),
and subsequently transforms the message into a cipher using the following
relationship:

$$\begin{eqnarray} C\ =\ M^e~(\mathrm{mod}~n). \end{eqnarray}$$

The cipher \\(C\\) is the encrypted form of the message and is sent to the
message receiver. Upon receipt of the cipher, the receiver decrypts the
message with their private key via

$$\begin{eqnarray} M\ =\ C^d~(\mathrm{mod}~n). \end{eqnarray}$$

The remarkable feature here is that the sender _does not send the entire
manipulated message_ (namely \\(M^e\\)), but rather only sends the cipher
\\(C\\), which is _merely a remainder_ , obtained by dividing \\(M^e\\) by
\\(n\\). Despite the evident loss of information entailed by only sending the
remainder, _the receiver still possesses sufficient information to reconstruct
the entire message_. This seemingly miraculous feature of RSA cryptography is
the result of underlying mathematical constructs that are both profoundly
powerful and relatively simple. Explaining this mathematics in detail is the
purpose of this article. We begin by covering the background maths necessary
to understand RSA.

## Background Mathematics

We start with some formal definitions. Note that it's not necessary to
understand every definition provided here, though doing so will provide
context for the mathematical tools that underlie RSA. A ring is a set \\(R\\)
with two operations called addition and multiplication. A ring is said to
commutative if the multiplication operation is commutative, namely

$$\begin{eqnarray} a\times b = b\times a, \quad \forall\; a, b\in R.
\end{eqnarray}$$

A field is a commutative ring for which every nonzero element possesses a
multiplicative inverse:

$$\begin{eqnarray} \forall a\in R,\ \exists\ b\in R, \ \ \mathrm{such\ that}\
\ a\times b =1. \end{eqnarray}$$

More precisely, a field is a set of numbers with four operations (addition,
subtraction, multiplication and division) which satisfy a set of arithmetic
rules called the field axioms. 2 A finite field is simply a field with a
finite number of elements.

Denote the set of integers less than \\(n\\) as
\\(Z_n=\\{0,1,2,\dots,n-1\\}\\). Addition and multiplication operations can be
defined on this set using modular arithmetic, namely

$$ \begin{eqnarray} a&=& b~(\mathrm{mod}~n) \quad\Longrightarrow \quad a = m_a
n +b, \quad\mathrm{for~integers}~m_a~\mathrm{and}~b<n, \end{eqnarray}$$

where \\(b\\) is the remainder after dividing \\(a\\) by \\(n\\).
Relationships such as \\(a=b~(\mathrm{mod}~n)\\) are referred to as congruence
relationships, and for \\(a=b~(\mathrm{mod}~n)\\), we say that \\(a\\) is
congruent to \\(b\\), meaning they share the same remainder when divided by
\\(n\\).

Addition and multiplication for \\(Z_n\\) take the usual modular form. For
example, in \\(Z_6\\) one has \\(3\times 4 = 0~(\mathrm{mod}~6)\\) and
\\(3+5=2~(\mathrm{mod}~6)\\). More generally, if \\(a=b~(\mathrm{mod}~n)\\),
one has

$$ \begin{eqnarray} a+c&=& b+c~(\mathrm{mod}~n),\nonumber\\\ a\times c&=&
b\times c~(\mathrm{mod}~n),\nonumber\\\ a^c&=& b^c~(\mathrm{mod}~n).
\end{eqnarray}$$

To prove these results, we write \\(a = m_an+b\\), so that

$$\begin{eqnarray} a+c&=& (m_a n + b) + c \ =\ b+c~(\mathrm{mod}~n),
\end{eqnarray}$$

since \\(m_a n =0~(\mathrm{mod}~ n)\\). Similarly, multiplying \\(a\\) and
\\(c\\) gives

$$\begin{eqnarray} a\times c\ =\ (m_a\,c)\times n + b\times c\ =\ b\times c
~(\mathrm{mod}~n), \end{eqnarray}$$

whilst raising \\(a\\) to the power of \\(c\\) gives

$$\begin{eqnarray} a^c\ =\ (m_a n +b)^c\ =\ [b^c+\mathcal{F}(n)]\ =\
b^c~(\mathrm{mod}~n), \end{eqnarray}$$

where all terms in the function \\(\mathcal{F}(n)\\) contain the integer
\\(n\\), giving \\(\mathcal{F}(n)=0~(\mathrm{mod}~n)\\). Note that we merely
expanded the brackets and lumped all terms containing \\(n\\) together into an
arbitrary function called \\(\mathcal{F}(n)\\).

Another useful result is the ability to cancel factors from congruence
relationships when they are co-prime with the modulus. Specifically, if
\\(k\\) and \\(n\\) are co-prime (namely their greatest common divisor is one,
\\(\mathrm{gcd}(k,n)=1\\)), and

$$\begin{eqnarray} k\, a \ =\ k\, b~(\mathrm{mod}~n),\label{eq:cancel_factor}
\end{eqnarray}$$

then \\(a\\) and \\(b\\) are congruent, meaning \\(a=b~(\mathrm{mod}~n)\\). To
prove this result, note that if \\(\mathrm{gcd}(k,n)=1\\), there always exists
an integer \\(x\\), which is the multiplicative inverse of \\(k\\) modulo
\\(n\\) (this result is proven below),

$$\begin{eqnarray} \mathrm{gcd}(k,n)\ =\ 1\quad \Longrightarrow \quad \exists
\,x, \ ~\mathrm{such\ that}~ \ x\times k\ =\ 1~(\mathrm{mod}~n).
\end{eqnarray}$$

For completeness, note that the statement \\(xk=1~(\mathrm{mod}~n)\\) means we
may write \\(xk\\) as \\(xk = m_kn+1\\), for integer \\(m_k\\). Multiplying
Eq. \eqref{eq:cancel_factor} by \\(x\\) gives:

$$\begin{eqnarray} x\,k\,a\ =\ x\,k\,b~(\mathrm{mod}~n). \end{eqnarray}$$

Consider the left hand side of this expression:

$$\begin{eqnarray} x\,k\,a\ =\ (m_k n+1)\times a\ =\ a~(\mathrm{mod}~n.)
\end{eqnarray}$$

Similarly, one can show that \\(xkb=b~(\mathrm{mod}~n)\\). Putting these
results together gives the \\(a=b~(\mathrm{mod}~n)\\), as required. This
demonstrates that a common factor can be cancelled from a congruence
relationship if the factor is co-prime with the modulus.

The set of integers modulo \\(n\\) is a commutative ring, which we also denote
as \\(Z_n\\).3 For every element \\(a\in Z_n\\), the element \\((n-a)\in
Z_n\\) satisfies

$$\begin{eqnarray} a+(n-a) &=& 0~(\mathrm{mod}~n), \end{eqnarray}$$

and is therefore the additive inverse of \\(a\\). For any element \\(a\in
Z_n\\), the multiplicative inverse of \\(a\\) is the element \\(b=a^{-1}\\),
which satisfies \\(a\times b =1~(\mathrm{mod}~n)\\). In general, however, a
commutative ring \\(Z_n\\) may contain elements for which no multiplicative
inverse exists. For example, in \\(Z_8\\) there is no multiplicative inverse
for the element 4. Note also that the product \\(4\times
4=0~(\mathrm{mod}~8)\\). These two properties are related: If there exists a
non-zero element \\(b\in Z_n\\), such that \\(a\times b=0~(\mathrm{mod}~n)\\),
the element \\(a\\) does not contain a multiplicative inverse in \\(Z_n\\)
(more formally, zero-divisors in \\(Z_n\\) do not possess multiplicative
inverses in \\(Z_n\\)).

For the set \\(Z_n\\), it is always possible to define a subset
\\(Z_n^\times\\) such that every element \\(a\in Z_n^\times\\) possesses a
multiplicative inverse in \\(Z_n^\times\\). Formally, we define
\\(Z_n^\times\\) as

$$\begin{eqnarray} Z_n^\times&\equiv & \\{a\in Z_n~|~\exists\, b\in
Z_n,~\mathrm{such~that}~a\times b=1~(\mathrm{mod}~n)\\}. \end{eqnarray}$$

When does an element in \\(Z_n\\) possess a multiplicative inverse in
\\(Z_n\\)? It turns out that if \\(a\in Z_n\\) is co-prime with \\(n\\), i.e.
\\(\mathrm{gcd}(a,n)=1\\), then \\(a\\) will have a multiplicative inverse in
\\(Z_n\\). The proof of this statement uses Bezout's identity, which we now
prove.

### Bezout's Identity

Bezout's identity asserts that, given two integers \\(a\\) and \\(n\\), with
greatest common divisor \\(d\\), namely \\(\mathrm{gcd}(a,n)=d\\), one can
always find integers \\(m_a\\) and \\(m_n\\) satisfying

$$\begin{eqnarray} m_a a+m_n n =d. \end{eqnarray}$$

The standard proof of Bezout's identity proceeds as follows. For any two
integers \\(a\\) and \\(n\\), define the following set of integers:

$$\begin{eqnarray} \mathcal{S} &=& \\{m_a a +m_n n ~|~ m_{a},\,m_{n}\in
Z,~\mathrm{and}~m_a a+m_n n >0\\}. \end{eqnarray}$$

This non-empty set is comprised solely of positive integers and therefore
contains a minimum element, which can be denoted as \\(d=m_{d,a} a+
m_{d,n}n\\), for integers \\(m_{d,a}\\) and \\(m_{d,n}\\). One can prove that
\\(d\\) is a divisor of \\(a\\) as follows. Write \\(a= n_a d+r_a\\), for
integer \\(n_a\\) and remainder \\(r_a\\). Rearranging this expression gives:

$$\begin{eqnarray} r_a&=& a-n_a d\ =\ (1-n_a m_{d,a})\times a -
(n_am_{d,a})\times n, \end{eqnarray}$$

which shows that either \\(r_a\in \mathcal{S}\\) or \\(r_a=0\\). However, by
definition, the remainder \\(r_a\\) satisfies \\(0\le r_a<d\\), and,
furthermore, \\(d\\) is the smallest element in \\(\mathcal{S}\\). Hence
\\(r_a=0\\), and \\(d\\) is a divisor of \\(a\\). A similar proof demonstrates
that \\(d\\) is also a divisor of \\(n\\).

To show that \\(d\\) is the greatest common divisor of \\(a\\) and \\(n\\),
assume that there exists an integer \\(d'\\) which is also a common divisor of
\\(a\\) and \\(n\\), such that \\(a=m_a' d'\\) and \\(n = m_n' d'\\). Using
the expression for \\(d\\), one has

$$\begin{eqnarray} d&=& m_{d,a}a + m_{d,n}n \ =\ (m_{d,a} m_a' + m_{d,n}
m_n')\times d', \end{eqnarray}$$

demonstrating that \\(d\\) is divisible by \\(d'\\), so that \\(d\ge d'\\).
Hence \\(\mathrm{gcd}(a,n)=d\\), as anticipated, and Bezout's identity
follows.

### Elements in \\(\mathrm{Z_n^\times}\\)

Next, we make use of Bezout's identity to show that \\(Z_n^\times\\) is
comprised of elements from \\(Z_n\\) satisfying \\(\mathrm{gcd}(a,n)=1\\).
Consider any element \\(a\in Z_n\\) that is co-prime to \\(n\\) (i.e.
\\(\mathrm{gcd}(a,n)=1\\)). According to Bezout's identity, there exists
integers \\(x\\) and \\(y\\) that satisfy \\(ax+ny =1\\). Rearranging gives
\\(ax = -ny +1\\), which can be written as

$$\begin{eqnarray} a\times x&=& 1~(\mathrm{mod}~n). \end{eqnarray}$$

Thus, any element of \\(Z_n\\), that is co-prime to \\(n\\), possesses a
multiplicative inverse (modular \\(n\\)) in the set \\(Z_n\\). However,
\\(Z_n^\times\\) was defined as the subset of elements of \\(Z_n\\) that
contain a multiplicative inverse in \\(Z_n\\). Hence, \\(Z_n^\times\\) is
comprised of the elements \\(a\in Z_n\\) that satisfy
\\(\mathrm{gcd}(a,n)=1\\).

### \\(\mathrm{Z_n^\times}\\) is a Group

The set \\(Z_n^\times\\) is well behaved under multiplication and, in
particular, every element \\(a\in Z_n^\times\\) has a modular multiplicative
inverse \\(a^{-1}\in Z_n^\times\\). Furthermore, the elements in
\\(Z_n^\times\\) always define a group (as discussed momentarily), where group
multiplication is identified as the standard integer multiplication modulo
\\(n\\). Note that the set \\(Z_n\\) does not always define a group under
multiplication modulo \\(n\\), for arbitrary \\(n\\).4 In cases where
\\(n=p\\) is a prime number, one has \\(\mathrm{gcd}(a,p)=1\\) for all non-
zero \\(a\in Z_p\\), and \\(Z_p^\times = Z_p/\\{0\\}\\). That is,
\\(Z_p^\times\\) contains all non-zero elements of \\(Z_p\\), as all integers
less than a prime number \\(p\\) are co-prime with \\(p\\). More generally,
for non-prime \\(n\\) one has \\(Z_n^\times \ne Z_n/ \\{0\\}\\), and the
number of elements in \\(Z_n^\times\\) is equal to the number of integers less
than \\(n\\) that are co-prime with \\(n\\). However, note that Euler's
totient function, \\(\phi(n)\\), is defined as the number of integers less
than \\(n\\) that are co-prime with \\(n\\). Consequently the number of
elements in \\(Z_n^\times\\) (called the order of \\(Z_n^\times\\)) is always
given by \\(|Z_n^\times| = \phi(n)\\).

It is straight-forward to show that the elements of \\(Z_n^\times\\) satisfy
the four conditions necessary to define a group:

  * **Group Associativity** : Given any three elements \\(a,\,b,\,c\in Z_n^\times\\), one trivially has 

$$ \begin{eqnarray} a\times (b\times c) ~(\mathrm{mod}~n)=(a\times b)\times
c~(\mathrm{mod}~n). \end{eqnarray}$$

  * **Group Inverse** : All elements in \\(a\in Z_n^\times\\) satisfy \\(\mathrm{gcd}(a,n)=1\\), and therefore have a modular multiplicative inverse in \\(Z_n^\times\\), by Bezout's identity.
  * **Group Closure** : For any two elements \\(a,\,b\in Z_n^\times\\), one has \\(\mathrm{gcd}(b,n)=\mathrm{gcd}(a,n)=1\\), and Bezout's identity asserts that one can write 

$$ \begin{eqnarray} x_aa+y_a n\ =\ 1~\qquad\mathrm{and}~\qquad x_bb+y_bn\ =\
1, \end{eqnarray}$$

for some integers \\(x_{a,b}\\) and \\(y_{a,b}\\). Multiplying these
expressions gives

$$ \begin{eqnarray} ab(x_ax_b) + n(x_a y_ba + x_b y_a b +y_ay_b n)=1,
\end{eqnarray}$$

which, in accordance with Bezout's identity, implies that
\\(\mathrm{gcd}(ab,n)=1\\). This demonstrates closure under group
multiplication as \\(ab\in Z_n^\times\\).

  * **Group Identity** : The set \\(Z_n^\times\\) always contains the element \\(1\\), which satisfies 

$$ \begin{eqnarray} 1\times a\ =\ a\times1\ =\ a \in Z_n^\times,
\end{eqnarray}$$

for any element \\(a\in Z_n^\times\\).

Thus, \\(Z_n^\times\\) forms a group. More precisely, \\(Z_n^\times\\) is an
Abelian group as group multiplication is commutative.

As noted earlier, every element \\(a\in Z_n\\) contains an additive inverse
(modulo \\(n\\)), namely \\((n-a)\in Z_n\\), which satisfies
\\(a+(n-a)=0~(\mathrm{mod}~n)\\). For any element \\(a\in Z_n^\times\\), the
additive inverse from \\(Z_n\\) also appears in \\(Z_n^\times\\), namely
\\((n-a)\in Z_n^\times\\). This is shown as follows. For all \\(a\in
Z_n^\times\\), one has \\(\mathrm{gcd}(a, n)=1\\), and it is possible to write
\\(x_aa+ y_a n=1\\), for integers \\(x_a,\,y_a\\). Rearranging this expression
gives

$$ \begin{eqnarray} x_aa+ y_a n\ =\ (-x_a)(-a) +y_an \ =\ (-x_a)(n-a) +
(x_a+y_a)n\ =\ 1. \end{eqnarray}$$

Thus, \\(\mathrm{gcd}((n-a),n)=1\\), and \\(\forall a\in Z_n^\times\\), there
exists an element \\((n-a)\in Z_n^\times\\), such that

$$ \begin{eqnarray} a+(n-a)=0~(\mathrm{mod}~n). \end{eqnarray}$$

Note, however, that \\( Z_n^\times\\) does not contain a zero element, so
addition is not well defined within \\(Z_n^\times\\) itself. This raises an
important point - whereas addition modulo \\(n\\) is always well-defined for
\\(Z_n\\) but multiplication modulo \\(n\\) is not (due to the presence of
zero divisors), the converse is true for \\(Z_n^\times\\), where
multiplication is well- defined but addition is not.

### Properties of the Totient Function

Euler's totient function plays a role in the discussion of RSA below. It is
useful to note the following properties of the totient function:

  * For prime \\(p\\), one has \\(\phi(p)=p-1\\). 
  * If \\(a\\) and \\(b\\) are co-prime, \\(\phi(ab)=\phi(a)\phi(b)\\).
  * Thus, for prime numbers \\(p\\) and \\(q\\), one has \\(\phi(pq)=\phi(p)\phi(q)=(p-1)(q-1)\\).

The first statement follows from the definition of a prime number, as all
integers less than \\(p\\) are co-prime with \\(p\\). The last two statements
are proved as follows. First, consider a number \\(N_2=p^2\\), for some prime
\\(p\\). We wish to determine the value of \\(\phi(n_2)\\). Note that there
are \\(p^2-1\\) numbers to be considered as candidates that may be co-prime
with \\(N_2\\) and thus counted by \\(\phi(n_2)\\). Of these \\(p^2-1\\)
numbers, all will be co-prime with \\(N_2\\), unless the number is divisible
by \\(p\\). There are \\(p-1\\) numbers less than \\(N_2\\) that are divisible
by \\(p\\). This gives

$$\begin{eqnarray} \phi(p^2)&=& p^2-1 - (p-1)\ =\ p^2-p. \end{eqnarray}$$

Similar arguments hold for a number \\(N_m=p^m\\), for an arbitrary positive
integer \\(m\\), giving

$$\begin{eqnarray} \phi(p^m)&=& p^m-p^{m-1}. \end{eqnarray}$$

This gives the value of Euler's totient function for any number that may be
written as \\(N_m=p^m\\), for prime number \\(p\\).

Next, consider numbers of the form \\(N_{m,n}= p^m q^n\\), for prime numbers
\\(p\\) and \\(q\\), and positive integers \\(m\\) and \\(n\\). There are \\(
p^mq^n-1\\) numbers to consider as candidate co-primes to \\(N_{m,n}\\). Of
these, we should not count the numbers that are divisible by \\(p\\), of which
there are \\(p^{(m-1)}q^n-1\\). Similarly we should not count the
\\(p^mq^{(n-1)}-1\\) numbers that are divisible by \\(q\\). However, moving
these two groups of numbers double-counts the numbers that are divisible by
\\(pq\\). Thus, we should add back the numbers that are divisible by \\(pq\\),
of which there are \\(p^{(m-1)}q^{(n-1)}-1\\). Putting this altogether gives

$$\begin{eqnarray} \phi(p^mq^n)&=& p^mq^n - p^mq^{n-1}- p^{m-1}q^n +
p^{m-1}q^{n-1}\nonumber\\\ &=& (p^m-p^{m-1})(q^n-q^{n-1})\nonumber\\\
&=&\phi(p^m)\,\phi(q^n). \end{eqnarray}$$

This result generalises for an arbitrary number of the form

$$\begin{eqnarray} N\ =\ p_i^{m_1}\times p_2^{m_2}\times \ldots \times
p_n^{m_n}\ =\ \Pi_{i=1}^n \,p_i^{m_i},\label{eq:prime_decomp} \end{eqnarray}$$

for integers \\(m_i\\), and distinct primes \\(p_i\\), where \\(i=1,2,..,n\\).
The generalisation is readily proven either using the same counting methods as
above, or by induction. The resulting totient function is

$$\begin{eqnarray} \phi(\Pi_{i=1}^n\, p_i^{m_i})&=& \Pi_{i=1}^n
\left(p_i^{m_i}-p_i^{m_i-1}\right). \end{eqnarray}$$

This gives

$$\begin{eqnarray} \phi(\Pi_i\, p_i^{m_i})&=& \Pi_i
\,\phi(p_i^{m_i})\label{eq:totient_product_primes} \end{eqnarray}$$

These results are sufficient to prove the claim that
\\(\phi(ab)=\phi(a)\phi(b)\\) for co-prime integers \\(a\\) and \\(b\\). The
Fundamental Theorem of Arithmetic specifies that any integer may be written as
a unique product of primes, as in Eq.~\eqref{eq:prime_decomp}. Further, any
pair of co-prime integers can be written as \\(a=\Pi_i\, p_i^{m_i}\\), and
\\(b=\Pi_j\,q_j^{n_j}\\), for some sets of primes \\(\\{p_i\\}\\) and
\\(\\{q_j\\}\\), where the sets are disjoint, namely \\(\\{p_i\\} \cap
\\{q_j\\}= \emptyset\\). Combining the above results gives

$$\begin{eqnarray} \phi(ab)&=&
\phi\left(\left[\Pi_{i}\,p_i^{m_i}\right]\left[\Pi_j\,q_j^{n_j}\right]\right)\nonumber\\\
&=&\left[\Pi_{i}(p_i^{m_i}-p_i^{m_i-1})\right]\times\left[
\Pi_j(q_j^{n_j}-q_j^{n_j-1})\right]\nonumber\\\ &=&\phi(a)\,\phi(b),
\end{eqnarray}$$

as required. Note that the second equality follows from Eq.
\eqref{eq:totient_product_primes}.

### An Interim Result

In this subsection we prove the following result: If \\(a\\) is co-prime with
a prime number \\(p\\), then for each non-zero \\(b\in Z_p\\), there exists a
unique \\(x_b\in Z_p\\) such that \\(a x_b = b~(\mathrm{mod}~p)\\).

A proof of this result proceeds as follows. The integers \\(a\\) and \\(p\\)
satisfy \\(\mathrm{gcd}(a,p)=1\\), so Bezout's identity asserts that one can
find integers \\(x_1\\) and \\(m_1\\) such that \\(ax_1+p m_1=1\\).
Furthermore, \\(x_1\\) is unique. To prove this, assume that \\(y_1\\) also
satisfies \\(a y_i=1~(\mathrm{mod}~p)\\). It follows that \\(ax_1 = ay_1 =
1~(\mathrm{mod}~p)\\). Hence,

$$\begin{eqnarray} x_1 \ =\ (ay_1) x_1\ =\ (ax_1) y_1\ =\
y_1~(\mathrm{mod}~p). \end{eqnarray}$$

Thus, \\(y_1=x_1\\) is the unique modular multiplicative inverse of \\(a\\) in
\\(Z_p\\). This result implies that, for each non-zero \\(b\in Z_p\\), there
exists a unique element \\(x_b\in Z_p\\), such that \\(a x_b =
b~(\mathrm{mod}~p)\\). To prove this claim, multiply the expression \\(a x_1 +
p m_1=1\\) by \\(b\\) and define \\(x_b = b\times x_1\\) and \\(m_b= b\times
m_1\\), to obtain

$$\begin{eqnarray} a x_b +p m_b = b. \end{eqnarray}$$

Consequently \\(a x_b = b~(\mathrm{mod}~p)\\), as required. The uniqueness of
\\(x_b\\) follows from the uniqueness of \\(x_1\\).

It follows that, for each non-zero element \\(b\in Z_p\\), the product
\\(b\times a\\) is unique (modulo~\\(p\\)). Thus, there is a one-to-one
correspondence between the non-zero elements of \\(Z_p\\),

$$\begin{eqnarray} Z_p/\\{0\\}\ =\ \\{1,\,2,\,3,\,\ldots,\,(p-1)\\},
\end{eqnarray}$$

and the set of numbers

$$\begin{eqnarray} A_p\ =\ \\{ a,\, 2a,\, 3a,\,\ldots,\, (p-1)\,a\\}.
\label{eq:set_Ap} \end{eqnarray}$$

This result is used in the proof of Fermat's Little theorem.

### Fermat's Little Theorem

Fermat's Little theorem states that, given any non-zero integer \\(a\in
Z_p\\), for prime number \\(p\\), one has
\\(a^{\phi(p)}=1~(\mathrm{mod}~p)\\). To prove this theorem, recall the one-
to-one correspondence between the non-zero elements of \\(Z_p\\) and the set
of numbers \\(A_p\\) given in Eq. \eqref{eq:set_Ap}. Taking the product of all
elements in the set \\(A_p\\), it follows that

$$\begin{eqnarray} a\times 2a\times \ldots\times (p-1)a =
(p-1)!~(\mathrm{mod}~p), \end{eqnarray}$$

which can be written as

$$\begin{eqnarray} a^{(p-1)} (p-1)! = (p-1)!~(\mathrm{mod}~p).
\end{eqnarray}$$

The factorial factor can be cancelled from each side of this congruence
expression as \\(p\\) and \\((p-1)!\\) are co-prime. Thus, one has
\\(a^{(p-1)} = 1~(\mathrm{mod}~p)\\), or, equivalently,
\\(a^{\phi(p)}=1~(\mathrm{mod}~p)\\), as anticipated.

### A Version of the Chinese Remainder Theorem

Given two co-prime integers \\(p\\) and \\(q\\), and an integer \\(x\\) that
satisfies \\(x=a~(\mathrm{mod}~p)\\) and \\(x= a~(\mathrm{mod}~q)\\), one can
show that \\(x= a~(\mathrm{mod}~pq)\\). To prove this statement, assume that
\\(x=b~(\mathrm{mod}~pq)\\) for some \\(b\\). We will show that \\(b=a\\). By
definition, one has the following relationships

$$\begin{eqnarray} x \ =\ n_{pq}\, (pq) +b,~\quad x\ =\ n_p\, p +a,
~\quad\mathrm{and}\quad x\ =\ n_q\,q +a. \end{eqnarray}$$

Combining the first two expressions, one obtains

$$\begin{eqnarray} b\ =\ a +(n_{pq}\,q+n_p)\,p, \end{eqnarray}$$

which shows that \\(b=a~(\mathrm{mod}~p)\\). One may similarly show that
\\(b=a~(\mathrm{mod}~q)\\). Equating these expressions gives

$$\begin{eqnarray} b\ =\ a + m_p\, p\ =\ a +m_q\, q, \end{eqnarray}$$

for some integers \\(m_p\\) and \\(m_q\\). Therefore the number \\(X\equiv
m_p\,p=m_q\, q\\) is divisible by both \\(p\\) and \\(q\\). However, \\(p\\)
and \\(q\\) are co-prime, so that \\(X\ge pq\\), which contradicts the
assertion that \\(0\le b< pq\\) is the remainder obtained after dividing
\\(x\\) by \\(pq\\). Hence, \\(m_p=m_q=0\\) and \\(b=a\\), giving \\(x=
a~(\mathrm{mod}~pq)\\), as claimed.

## RSA Cryptography

We now have all the necessary background mathematics to prove the validity of
RSA cryptography - if you made it this far, well done! Our discussion of RSA
is broken up into a number of parts. As mentioned earlier, RSA encryption and
decryption relies on a set of public and private keys. In the first section
below, we describe the generation of RSA keys. Subsequently we turn our
attention to the RSA encryption and decryption procedures, and then
mathematically prove that RSA cryptography is valid. Additional useful results
and discussion are then presented. Firstly, it's shown that RSA cryptography
is multiplicatively holomorphic. We then discuss why RSA works and why the
algorithm is constructed the way it is. Finally we prove that a generalisation
of RSA cryptography, involving more prime numbers (multi-prime RSA), also
provides a valid cryptographic protocol.

### Key Generation

Any individual wishing to send and receive messages encoded via RSA encryption
must generate a pair of keys, namely a public key and a private key. The
public key may be freely shared with other individuals who may, in turn, use
the key to encode messages. Once a message is encrypted with the public key,
only the holder of the corresponding private key can (feasibly) decrypt the
message. Thus, the public and private keys play a central role in RSA
encryption. Here we describe how these keys are generated.

The algorithm for generating RSA encryption keys proceeds as follows.

  * Step 1: Randomly select two (large) prime numbers, \\(p\\) and \\(q\\).
  * Step 2: Calculate the modulus \\(n=p\times q\\).
  * Step 3: Calculate the number of integers less than \\(n\\) that are co-prime with \\(n\\), which is equivalent to calculating the value of Euler's totient function: 

$$\begin{eqnarray} \phi(n) \ =\ \phi(pq)\ =\ \phi(p)\,\phi(q)\ =\ (p-1)(q-1).
\end{eqnarray}$$

  * Step 4: Select a large integer \\(e\\) such that \\(e\in[2,\phi(n))\\) and \\(e\\) is co-prime with \\(\phi(n)\\)
  * Step 5: Compute the modular multiplicative inverse of \\(e\\), namely the integer \\(d\in[2,\phi(n))\\), that satisfies 

$$\begin{eqnarray} e\times d\ =\ 1~(\mathrm{mod}~\phi(n)).\label{eq:d_defined}
\end{eqnarray}$$

The integer \\(d\\) is unique and, furthermore, \\(d\\) is co-prime with
\\(\phi\\).

The RSA _public key_ is given by the pair of numbers \\((e,n)\\), while the
pair \\((d,n)\\) constitutes the _private key_. An individual may freely share
the public key with others but the private key should kept secret. In
addition, the numbers \\(p\\) and \\(q\\) should not be revealed as knowledge
of these primes allows an arbitrary individual to decrypt RSA encrypted
messages.

In Step 5, the uniqueness of \\(d\\) follows from the earlier proof that the
multiplicative modular inverse of a number \\(a\\), is unique when \\(a\\) is
co-prime with the modulus \\(p\\). By construction, \\(e\\) and \\(\phi(n)\\)
are co-prime, meaning the multiplicative modular inverse \\(d\\) is unique. To
see that \\(d\\) and \\(\phi(n)\\) are co-prime, let
\\(s=\mathrm{gcd}(d,\phi(n))\\), such that \\(d= c_d s\\) and
\\(\phi(n)=c_\phi s\\) for some integers \\(c_s\\) and \\(c_\phi\\). Using
Eq.~\eqref{eq:d_defined} we can write \\(e\times d = c_{ed}\,\phi(n)+1\\), for
an integer \\(c_{ed}\\). Combining these expressions gives

$$\begin{eqnarray} e \times (c_d s)\ =\ c_{ed}\,c_\phi\,s +1, \end{eqnarray}$$

which can be cast as

$$\begin{eqnarray} s\times (e c_d- c_{ed}\,c_\phi)\ =\ 1. \end{eqnarray}$$

This last expression implies that \\(s=1\\) (all the numbers in brackets are
integers), verifying that \\(\mathrm{gcd}(d,\phi(n))=1\\), such that \\(d\\)
and \\(\phi(n)\\) are co-prime, as claimed.

### Message Encryption and Decryption

Consider two individuals, Alice and Bob. Let Bob declare that his public key
is \\((e,n)\\). Alice decides that she wishes to send a message \\(M\\) to
Bob. For the moment, assume that \\(M< n\\) is an integer (we shall discuss
arbitrary messages below). Alice converts the message \\(M\\) to the cipher
\\(C\\) as follows:

$$\begin{eqnarray} C\ =\ M^{e}~(\mathrm{mod}~n).\label{eq:encryptionRSA}
\end{eqnarray}$$

Upon receiving the encrypted message, Bob uses his private key \\((d,n)\\) to
decrypt the cipher \\(C\\) and obtain Alice's message by computing

$$\begin{eqnarray} M\ =\ C^{d}~(\mathrm{mod}~n). \end{eqnarray}$$

Note that any individual intending to receive RSA encrypted messages requires
a set of keys - their own public key, which allows other individuals to
encrypt messages, and the corresponding private key, used to decrypt messages.
Thus, in the above, it would be appropriate to label Bob's keys as \\((e_b,
n_b)\\) and \\((d_b,n_b)\\). To send a reply to Alice, Bob must use Alice's
public key \\((e_a,n_a)\\) to encrypt his reply, creating a new cipher that
can only be decrypted by Alice, using her private key \\((d_a,n_a)\\).

### Verifying that RSA Encryption/Decryption Works

How do we know that the RSA algorithm works? Can we be sure that Bob does
indeed return Alice's message \\(M\\) after calculating
\\(C^{d}~(\mathrm{mod}~n)\\)? To prove that the Algorithm works, one must show
that \\(M=C^d~(\mathrm{mod}~n)\\). Recall that the Chinese Remainder Theorem
tells us that if \\(x=a~(\mathrm{mod}~p)\\) and \\(x=b~(\mathrm{mod}~q)\\),
then \\(x=a~(\mathrm{mod}~pq)\\). Thus, to prove that RSA works, it suffices
to prove that \\(M=C^d~(\mathrm{mod}~p)\\) and \\(M=C^d~(\mathrm{mod}~q)\\),
as the result \\(M=C^d~(\mathrm{mod}~pq)\\) automatically follows.

First consider \\(M=C^d~(\mathrm{mod}~q)\\). Equation \eqref{eq:encryptionRSA}
implies that the cipher \\(C\\) and the message \\(M\\) are related as follows

$$\begin{eqnarray} M^e\ =\ m\,n+ C, \end{eqnarray}$$

where \\(m\\) is an integer. Using this result, one may write

$$\begin{eqnarray} C^d~(\mathrm{mod}~q)&=&
(M^e-mn)^d~(\mathrm{mod}~q)\nonumber\\\ &=& M^{ed}~(\mathrm{mod}~q),
\end{eqnarray}$$

as \\(n\\) is divisible by \\(q\\). By definition, \\(d\\) is the modular
multiplicative inverse of \\(e\\), which satisfies

$$\begin{eqnarray} ed=1~(\mathrm{mod}~\phi(n)), \end{eqnarray}$$

so we can always write

$$\begin{eqnarray} ed\ =\ s\, (p-1)(q-1) +1, \end{eqnarray}$$

for integer \\(s\\). Using this expression gives

$$\begin{eqnarray} M^{ed}~(\mathrm{mod}~q)&=&
M^{s(p-1)(q-1)+1}~(\mathrm{mod}~q)\nonumber\\\ &=& M\times
\left(M^{(q-1)}\right)^{s(p-1)}~(\mathrm{mod}~q).\label{eq:rsa_proof1}
\end{eqnarray}$$

Next, we apply Fermat's Little Theorem, \\(a^{(q-1)}=1~(\mathrm{mod}~q)\\),
for \\(a=M\\), to obtain

$$\begin{eqnarray} M^{(q-1)}\ =\ m_q q+1, \end{eqnarray}$$

for integer \\(m_q\\). In turn, this result is used to simplify Eq.
\eqref{eq:rsa_proof1} as follows

$$\begin{eqnarray} M\times\left(M^{(q-1)}\right)^{s(p-1)}~(\mathrm{mod}~q)&=&
M\times\left(1+m_qq\right)^{s(p-1)}~(\mathrm{mod}~q)\nonumber\\\ &=&\left[
M\times(1)^{s(p-1)} +\ldots\right]~(\mathrm{mod}~q)\nonumber\\\ &=&
M~(\mathrm{mod}~q).\label{eq:fermatLT_in_rsa_proof} \end{eqnarray}$$

The dots in the second line denote terms containing powers of \\(m_qq\\),
which are always divisible by \\(q\\). Making use of Eq.
\eqref{eq:fermatLT_in_rsa_proof} in Eq. \eqref{eq:rsa_proof1} finally gives

$$ \begin{eqnarray} M^{ed}~(\mathrm{mod}~q) &=& M~(\mathrm{mod}~q),
\end{eqnarray}$$

as required. The same procedure can be used to prove that
\\(M^{ed}~(\mathrm{mod}~p)=M~(\mathrm{mod}~p)\\). Hence, via the Chinese
remainder Theorem we obtain the desired result:

$$\begin{eqnarray} C^d~(\mathrm{mod}~n)\ =\ M^{ed}~(\mathrm{mod}~n)\ =\
M~(\mathrm{mod}~n), \end{eqnarray}$$

proving that the RSA encryption/decryption procedure works - when Bob decrypts
the cipher \\(C\\) he obtains Alice's message \\(M\\). The remarkable feature
of RSA cryptography is that Alice need only send the remainder \\(C\\) to Bob,
and yet Bob is able to reconstruct Alice's entire message, as can be
mathematically proven in just a few lines!

In the above we assumed that the original message was an integer \\(M<n\\).
However, these result readily generalise for arbitrary messages. To encode an
arbitrary message string, one first converts the string to a numerical form
(for example, one can could crudely convert the string to a bit array, then
convert the bit array to standard numeric form). If the resultant numerical
message, \\(M\\), is larger than \\(n\\), one simply breaks the message up
into discrete chunks \\(M_i<n\\), such that \\(M=\sum _i M_i\\). Each of the
chunks can then be encrypted and sent to the message recipient, who may
decrypt them. In this way, arbitrary messages may be encrypted, transmitted,
and decrypted.

### Multiplicative Homomorphicity in RSA

Denote by \\(E\\) an encryption function that encodes a message \\(M\\) to
generate a cipher \\(C\\), namely \\(E(M)=C\\). Similarly, let \\(D\\) denote
the decryption function that returns the original message from the cipher,
namely \\(D(C)=D(E(M))=M\\). An encryption protocl is said to be homomorphic
if operations performed on the message \\(M\\) also apply to the cipher
\\(C\\). For example, an encryption scheme is homomorphic under addition if
the encryption of two messages \\(M_1\\) and \\(M_2\\) satisfies

$$\begin{eqnarray} C_1+C_2\ =\ E(M_1)+E(M_2)\ =\ E(M_1+M_2)\ =\ C_{12}.
\end{eqnarray}$$

Homomorphism is a powerful property as it allows individuals to perform
operations on encrypted data sets without actually seeing the underlying data.
Consequently one could encrypt multiple messages, send the ciphers to a
receiver, who performs some operations on the ciphers to generate an output
which is sent back and decrypted. The individual manipulating the data set
never sees the actual data yet successfully performs operations of interest.

Complete homomorphism under arbitrary mathematical operations is highly non-
trivial and most realistic encryption schemes achieve partial homomorphism at
best. It turns out that RSA encryption is homomorphic under multiplication,
which is seen as follows. Consider two messages \\(M_1\\) and \\(M_2\\), which
may be encrypted to produce two ciphers:

$$\begin{eqnarray} C_i\ =\ M_i^e~(\mathrm{mod}~n)\qquad\mathrm{for}\qquad
i=1,2.\label{eq:homo_ciphers} \end{eqnarray}$$

The product of these messages, \\(M_{12}=M_1M_2\\), may also be encrypted:

$$\begin{eqnarray} C_{12}\ =\ (M_{1}M_2)^e~(\mathrm{mod}~n). \end{eqnarray}$$

To show that RSA encryption is multiplicatively homomorphic we must show that
\\(C_{12}=C_1C_2\\). According to Eq. \eqref{eq:homo_ciphers} one has

$$\begin{eqnarray} C_i\ =\ M_{i}^e-x_i n, \end{eqnarray}$$

for integers \\(x_i\\). Multiplying the ciphers gives

$$\begin{eqnarray} C_1\times C_2&=& (M_1^e-x_1n) (M_2^e - x_2n)\nonumber\\\
&=& M_1^eM_2^e +F(n), \end{eqnarray}$$

where the function \\(F(n)\\) is divisible by \\(n\\). Consequently we have

$$ \begin{eqnarray} C_1C_2\ =\ M_1^e M_2^e~(\mathrm{mod}~n)\ =\
(M_1M_2)^e~(\mathrm{mod}~n)\ =\ C_{12}, \end{eqnarray}$$

proving that RSA encryption is multiplicatively homomorphic.

### Why Does RSA Work?

The RSA algorithm is reliant upon a set of keys, \\((e,n)\\) and \\((d,n)\\),
for each individual user. The public key \\((e,n)\\) may be widely
disseminated, whereas \\((d,n)\\) should be kept secret. It may naively appear
that it should be possible to calculate the private key, as \\(n\\) and
\\(e\\) are public, and the sole unknown (\\(d\\)) is the multiplicative
modular inverse of \\(e\\). These statements are true and, in principle,
knowledge of \\((e,n)\\) can be used to determine the private key \\(d\\).
However, the process is (believed to be) computationally "hard", making the
implementation impractical to the point of being infeasible, provided the
parameters are chosen appropriately.

The difficulty of "cracking the RSA code" from the use of the primes \\(p\\)
and \\(q\\) to calculate the modulus \\(n\\). Although an arbitrary individual
may have access to the value of \\(n\\), they do not know the factors \\(p\\)
and \\(q\\), and therefore cannot directly calculate the modulus \\(\phi(n)\\)
via \\(\phi(n)=(1-p)(1-q)\\). Absent knowledge of \\(\phi(n)\\), an individual
does not know the modulus with respect to which \\(d\\) is the multiplicative
inverse of \\(e\\) \- it's therefore difficult to calculate \\(d\\) as it's
not clear where to start.

To avoid using brute force to calculate \\(\phi(n)\\) directly, an individual
must determine the prime factors \\(p\\) and \\(q\\). However, although it is
easy to multiply two numbers together and obtain their product, it is believed
to be computationally hard to find the factors. This is the secret to the
success of the RSA algorithm - _factoring numbers is computationally
difficult, so provided very large prime numbers \\(p\\) and \\(q\\) are used
to generate the modulus \\(n=pq\\), it is infeasible for others to extract
\\(p\\) and \\(q\\) from \\(n\\) by brute force_.

The definition of "computationally hard" here is somewhat ambiguous as there
is no proof demonstrating that it is in fact hard to factor large numbers -
the discovery of a new algorithm could potentially render RSA ineffective.
Also, the definition of "infeasible" is a function of time - as computational
systems advance, our capacity to factor numbers by brute force improves. For
example, it (famously) appeared unlikely to Ron Rivest that RSA-125 could be
cracked in 1977 (Ron estimated it would take 40 quadrillion years!) but by
1993 a team using 1600 computers was able to crack a 426-bit message in 6
months. By 2009, RSA-768 (768-bits) was successfully factored after a two year
effort. Thus, as technology advances, the definition of "large primes" must
increase or RSA becomes ineffective. In addition, although factoring large
numbers is a hard problem using classical computation techniques, a quantum
computer would be able to rapidly accelerate the factorisation of large
numbers. Therefore the successful construction of a quantum computer would, in
effect, break RSA.

### Why Is RSA Constructed the Way It Is?

It is interesting to think about how and why RSA works the way it does. At its
core, RSA encrypts a message \\(M\\) by raising it to the power of \\(e\\).
Decryption works by raising the encrypted message to the power of \\(d\\),
which is the inverse of \\(e\\). If you made a first effort to construct an
encryption scheme utilising just this property, you might try something crude
like the following: To encrypt a message, one simply raises it to \\(e\\),
giving \\(C=M^e\\). Decryption proceeds by applying the inverse of \\(e\\),
giving \\(C^d = M^{ed} = M\\). This seems to provide a crude encryption
scheme, right? There is a problem, of course, as an individual must know
\\(e\\) to encrypt the message, which means \\(e\\) should be public. However,
knowledge of \\(e\\) automatically allows one to calculate \\(d=e^{-1}\\) and
decrypt the message. So a scheme like this cannot provide a viable public-key
cryptographic system.

A sensible next step, when attempting to develop an encryption scheme, would
be to incorporate modular arithmetic. Modular mathematics introduces more
parameters into the protocol (such as the modulus) which seems to complicate
the procedure, yet has the desirous advantage of making it more difficult to
decrypt messages. So lets combine the use of powers and modular arithmetic to
encrypt our message \\(M\\). First we choose a modulus, \\(n\\), then express
\\(M^e\\) in terms of the modulus:

$$\begin{eqnarray} M^e\ = \ m n+C, \end{eqnarray}$$

for integer \\(m\\) and remainder \\(C\\). This is simply the statement \\(C =
M^e~(\mathrm{mod}~n)\\). Note that \\(C\\) now contains (or hides) two inputs,
namely the operation of raising \\(M\\) to the power of \\(e\\), and the
division by \\(n\\). This appears promising and perhaps we could use \\(C\\)
as a cipher. To encrypt a message, an individual now requires both \\(e\\) and
\\(n\\), so the public key is the pair \\((e,n)\\). If an attacker knows
\\(n\\) and \\(e\\), and they intercept the cipher \\(C\\), they still cannot
determine the message \\(M\\), as the single equation above contains two
unknowns, \\(M\\) and \\(m\\) \- this seems promising. What about decryption?
Clearly we need to "undo" the power of \\(e\\) used during encryption. The
obvious option is to use the multiplicative inverse of \\(e\\), namely \\(d\\)
such that \\(d\times e =1~(\mathrm{mod}~n)\\). Writing symbolically, the logic
here is

$$\begin{eqnarray} C^d~(\mathrm{mod}~n)\ \rightarrow\
M^{ed}~(\mathrm{mod}~n)\rightarrow\ M, \end{eqnarray}$$

where we assume \\(M<n\\). However, we again have a problem. If an attacker
knows \\(e\\) and \\(n\\), as required to encrypt the message, they have
enough information to calculate the inverse \\(d\\). Thus, an attacker may
readily decrypt any cipher \\(C\\) and the scheme is useless.

Now we have enough information to make the key breakthrough and arrive at RSA.
We retain a public key \\((e,n)\\), such that encryption involves the use of
both powers and modular arithmetic, but we want to choose an inverse \\(d\\)
that is not readily accessible to attackers. The most obvious modification to
the last scheme is to change the definition of the inverse \\(d\\) to
\\(d\times e=1~(\mathrm{mod}~\phi)\\), where \\(\phi\\) is an as-yet
undetermined integer. Lets look at what happens if we apply this scheme. First
we encrypt our message \\(M\\) as \\(C= M^e~(\mathrm{mod}~n)\\), as before. To
decrypt the message, we undo the power \\(e\\),

$$\begin{eqnarray} C^d\ =\ [M^e-mn]^d\ =\ M^{ed}+ \mathcal{F}(n),
\end{eqnarray}$$

where every term in \\(\mathcal{F}(n)\\) contains \\(n\\). We can therefore
divide by \\(n\\) and obtain

$$\begin{eqnarray} C^d\ =\ M^{ed}~(\mathrm{mod}~n)\ =\ M^{s\phi
+1}~(\mathrm{mod}~n)i, \end{eqnarray}$$

where \\(s\\) is an integer. We see that we are almost there - if we choose
\\(\phi\\) such that \\(M^\phi=1~(\mathrm{mod}~n)\\), we have a functioning
encryption scheme.

At this point, one needs knowledge of number theory to progress. So, drawing
on your expertise in number theory (or, more likely, doing lots of reading)
you may remember that Fermat's Little Theorem looks remarkably like what we're
after. Fermat's Little theorem tells us that
\\(M^{(p-1)}=1~(\mathrm{mod}~p)\\) for prime \\(p\\), which appears perfect!
Lets choose \\(\phi=(p-1)\\) and restrict \\(n=p\\) to be a prime number.
Unfortunately this is insufficient as we encounter the same problem as before
- once an individual knows \\(n=p\\), they automatically know
\\(\phi(p)=(p-1)\\) and can solve for the key \\(d\\), breaking the scheme. So
this doesn't quite work, yet it appears very close to something viable. The
trick (and key insight) is to somewhat decouple \\(\phi\\) from \\(n\\), so
that knowledge of \\(n\\) does not automatically entail knowledge of
\\(\phi\\) (and thus knowledge of \\(d\\)). We need \\(n\\) and \\(\phi\\) to
be related, to benefit from Fermat's Little theorem, but we also need to use
prime numbers and make it difficult to determine \\(n\\). Combining these
properties, and guided by the knowledge that it is difficult to factorise
numbers, a sensible first guess is to consider \\(n=pq\\) to be the product of
two prime numbers. Remarkably, if \\(\phi\equiv \phi(n)=(p-1)(q-1)\\) is taken
to be Euler's totient function, RSA cryptography follows. It takes some effort
to prove that this scheme works (thus the earlier proofs) but nonetheless the
resulting protocol is viable.

The result is a cryptographic protocol with public key \\((e,n)\\), and
private key \\((d,n)\\), which satisfy \\(d\times
e=1~(\mathrm{mod}~\phi(n))\\). This scheme has the desirous properties of
encrypting by applying both a power and modular arithmetic, whilst also
permitting a decryption procedure that is incredibly difficult to break for an
attacker. To top it all off, the proof of that the scheme works relies upon a
number of interesting number theory results, generating unanticipated
practical uses for results such as Fermat's Little theorem. No doubt Fermat
would be both surprised and delighted!

### Generalising RSA: Are More Primes Better?

The time required to factor \\(n\\) by brute force increases with increasing
\\(n\\). Consequently the use of a larger modulus \\(n\\) generates a more
secure implementation of RSA than the use of a smaller modulus. Regarding the
use of primes \\(p\\) and \\(q\\), some obvious question arise. Why use just
two prime numbers \\(p\\) and \\(q\\)? Is it possible to generalise the scheme
for more prime numbers? The answer to the latter question is a resounding yes
- generalising the results proved earlier, it is simple to show that RSA
cryptography can be generalised to the case where the modulus is the product
of an arbitrary number of prime numbers, namely i

$$\begin{eqnarray} N\ = \ \Pi_{i=1}^n p_i, \end{eqnarray}$$

where \\(N\\) denotes our generalised modulus. The procedure for generating
encryption keys in the family of generalised RSA cryptography schemes is as
follows.

  * Step 1: Randomly select a set of \\(n\\) (large) prime numbers, \\(p_i\\), where \\(i\in\\{1,2,\ldots,n\\}\\) .
  * Step 2: Calculate the modulus \\(N=\Pi_{i=1}^n \,p_i\\).
  * Step 3: Calculate Euler's totient function: 

$$ \begin{eqnarray} \phi(N) \ =\ \phi(\Pi_i \,p_i)\ =\ \Pi_i\, \phi(p_i)\ =\
\Pi_i\,(p_i-1). \end{eqnarray}$$

  * Step 4: Select a large integer \\(e\\) such that \\(e\in[2,\phi(N))\\) and \\(e\\) is co-prime with \\(\phi(N)\\)
  * Step 5: Compute the modular multiplicative inverse \\(d\in[2,\phi(N))\\), which satisfies 

$$ \begin{eqnarray} e\times d\ =\
1~(\mathrm{mod}~\phi(N)).\label{eq:general_d_defined} \end{eqnarray}$$

The integer \\(d\\) is unique and, furthermore, \\(d\\) is co-prime with
\\(\phi\\).

The public key is again given by the pair \\((e,N)\\), and the private key is
\\((d,N)\\).

Message encryption and decryption proceeds exactly as in the standard RSA
cryptography. A message \\(M\\) is encrypted as

$$\begin{eqnarray} C\ =\
M^{e}~(\mathrm{mod}~N),\label{eq:General_encryptionRSa} \end{eqnarray}$$

and the cipher is decrypted via

$$\begin{eqnarray} M\ =\ C^{d}~(\mathrm{mod}~N). \end{eqnarray}$$

Using results reported already, it is easy to prove that this scheme works.
First, using the Chinese Remainder Theorem, one can show that if
\\(x=a~(\mathrm{mod}~p_i)\,\, \forall i\\), then \\(x = a~(\mathrm{mod}~\Pi_i
\, p_i).\\) Specifically, we have already proven the case with two primes,
\\(p_1\\) and \\(p_2\\), giving \\(x = a~(\mathrm{mod}~p_1p_2)\\). Next
consider three primes, such that \\(p_3\\) is co-prime to \\(N_{12}=p_1p_2\\).
For \\(x=a~(\mathrm{mod}~p_3)\\) and \\(x=a~(\mathrm{mod}~p_1p_2)\\), the
Chinese Remainder Theorem gives \\(x=a~(\mathrm{mod}~p_1p_2p_3)\\). This
process can be repeated to show that \\(x=a~(\mathrm{mod}~N)\\). Thus, to
prove that the generalised RSA cryptography works, it is sufficient to show
that

$$\begin{eqnarray} C^d \ =\ M~(\mathrm{mod}~p_i)\, \quad \forall i.
\end{eqnarray}$$

The proof is straightforward:

$$\begin{eqnarray} C^d&=& M^{ed}~(\mathrm{mod}~p_i)\nonumber\\\ &=&
M^{\phi(N)}~(\mathrm{mod}~p_i)\nonumber\\\ &=&M\times
\left(M^{(p_i-1)}\right)^{s\Pi_{j\ne i}(p_j-1)}~(\mathrm{mod}~p_i)\nonumber\\\
&=& M~(\mathrm{mod}~p_i), \end{eqnarray}$$

where \\(s\\) is an integer and the last line follows from Fermat's Little
Theorem. By symmetry, a similar result holds for all \\(p_i\\), and by the
Chinese Remainder Theorem the desired result of \\(M=C^d~(\mathrm{mod}~N)\\)
follows. Hence, from the theoretical perspective the generalised RSA scheme
with modulus \\(N=\Pi_i p_i\\) provides a viable cryptography.

I was "playing around" when I first derived these results but a quick search
reveals that the authors of the original RSA paper briefly mentioned this
possibility. The generalised version has received some attention and, in fact,
a couple of patents were filed to register the generalised RSA. This perhaps
seems a little strange, given that the inventors of RSA cryptography mention
the generalised scheme in their original paper. Nonetheless the existence of
the patents has caused some caution regarding the use of the generalised
scheme. There are also important practical considerations as the use of more
primes does not necessarily make the procedure more secure. It appears that
for sufficiently large \\(N\\), using \\(n=3\\) does not compromise the
security of the system and has the practical benefit of simplifying the
decryption calculations, via the generalised version of RSA-CRT.5 For larger
values of \\(n\\), it may be simpler to factor the large number \\(N\\),
though the details depend on the particular factoring algorithm used and the
rate at which different algorithms become more powerful as technology advances
(which varies for different algorithms).

## Conclusion

This article provided a detailed account of RSA cryptography. The presentation
was largely complete and self-contained, though there are a few instances
where, e.g., special cases in derivations were not discussed (these minor
details are left as exercises for the reader). RSA cryptography was a
trailblazing discovery that laid the path for modern public key cryptography.
It was truly non- trivial to discover that RSA encryption allows anyone to
send an encrypted message to another individual such that the receiver may
recover the original message in its entirety despite only receiving a
truncated (i.e. remainder) cipher \\(C\\).

If you've made it this far, congratulations - it no doubt took some effort!
Hopefully you've acquired an improved understanding of how RSA works and
developed an appreciation for the powerful yet simple mathematics that
underlies the scheme. Understanding RSA provides a good basis for further
studies of newer techniques such as elliptic curve cryptography and zero-
knowledge approaches like zk-SNARKs. More generally, a detailed study of RSA
provides basic insights into how modern cryptographic systems work and
highlights the utility of seemingly abstract areas of mathematics, such as
number theory.

## References

[1] Rivest, R., Shamir, A., & Adleman, L. (1978). A Method for Obtaining
Digital Signatures and Public-Key Cryptosystems. _Communications of the ACM_ ,
21( _2_ ), 120-126. [DOI:
10.1145/359340.359342](https://doi.org/10.1145/359340.359342).

* * *

  1. The original discovery of RSA by [Cocks](https://en.wikipedia.org/wiki/Clifford_Cocks), following ideas of Ellis, was classified and occurred within the GCHQ. By the time that Rivest, Shamir, and Adleman made the public discovery of RSA in 1977, Diffie-Hellman cryptography was already known, though both were publicly discovered after the earlier work of Ellis and Cocks. ↩

  2. The field axioms specify the following properties: associativity, commutativity, additive and multiplicative identities, additive and multiplicative inverses, and distributivity of multiplication over addition. ↩

  3. Note that the set of integers less than \\(n\\) is topologically equivalent to the set of integers modulo \\(n\\). Specifically, the integer elements of the former set are in a direct one-to-one correspondence to the equivalence classes that define the elements of the latter set. ↩

  4. Though \\(Z_n\\) can be given a group structure by defining the group multiplication operation as integer addition modulo \\(n\\). ↩

  5. RSA CRT is an implementation of RSA that uses the Chinese Remainder Theorem to accelerate the decryption process. The underlying protocol is identical aside from the use of mathematical identities to optimise message decryption. ↩

[ __Twitter ](https://twitter.com/share?text=A Detailed Introduction to RSA
Cryptography&url=https://blog.sigmaprime.io/introduction-to-rsa.html) [
__Facebook
](https://www.facebook.com/sharer/sharer.php?u=https://blog.sigmaprime.io/introduction-
to-rsa.html) [ __Google+
](https://plus.google.com/share?url=https://blog.sigmaprime.io/introduction-
to-rsa.html)

[RSA](https://blog.sigmaprime.io/tag/rsa.html)[number
theory](https://blog.sigmaprime.io/tag/number-theory.html)[Fermat's Little
Theorem](https://blog.sigmaprime.io/tag/fermats-little-theorem.html)[multi-
prime RSA](https://blog.sigmaprime.io/tag/multi-prime-rsa.html)[Euler's
totient function](https://blog.sigmaprime.io/tag/eulers-totient-function.html)

