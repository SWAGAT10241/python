# Combination using SciPy
We know cartesian product of two set $A={a_1,a_2},B ={b_1,b_2}$<br>
| |  a_1| a_2|
|--------------|--------------|---------------------------|
|  b_1         | (a₁, b₁)       | (a₂, b₁)
| b_2          | (a₁, b₂)         | (a₂, b₂)


So,$ A \times B = {(a_1,b_1),(a_2,b_1),(a_1,b_2),(a_2,b_2)}$<br>
So cardinality of $A \times B = |A\times B| = 2\times2 = \text{cardindlity of A }\times \text{cardindlity of B }= 4$<br>

`Q` . If A and B are two finite sets, then $|A\times B|=|A||B|$<br>
proof:<br>
Assume $|A| = m$, $|B| = 0$, then $|A \times B| = 0$<br>
Assume $A = \{a_1, a_2, \dots, a_n\}$ and $B = \{b_1\}$, then $A \times B = \{(a_1, b_1), (a_2, b_1), \dots, (a_n, b_1)\}$<br>
We suppose $A = \{a_1, a_2, \dots, a_n\}$, $|A| = n$ and $B = \{b_1, b_2, \dots, b_m\}$, $|B| = m$, so $|A \times B| = n \cdot m$<br>
Let $B = \{b_1\} \cup \{b_2, b_3, \dots, b_m\}$<br>

$|A \times B| = |A \times \{b_1\}| + |A \times (B - \{b_1\})| = n + |A \times (B - \{b_1\})|$<br>
$Similarly,|A \times B| = |A \times \{b_1, b_2\}| + |A \times (B - \{b_1, b_2\})| = 2n + |A \times (B - \{b_1, b_2\})$<br>
$|A \times B| = |A \times \{b_1, b_2, b_3\}| + |A \times (B - \{b_1, b_2, b_3\})| = 3n + |A \times (B - \{b_1, b_2, b_3\})$<br>
Repeat this process, and we will get:<br>
$|A \times B| = |A \times \{b_1, b_2, \dots, b_m\}| + |A \times \emptyset|$<br>
$= m \cdot n + 0$<br>
$= m \cdot n$

Theroem : $If\ A_1,A_2,\dots A_n \text{are finite sets, then} |A_1 \times A_2\times\dots A_n| = |A_1||A_2|\dots|A_n|$<br>
Bytes :<br>
A = {0,1}<br>
$A \times A \times A \times A \dots 8\ time \\
= 2 \times2 \times 2 \dots 8\ time \\
= 2^8 = 256$

`Q`.There are three basic color is computers,Red,Green and Blue.Each color id of 1 byte .We haver three byte space in computer memory to move this color and add new color .So how many unique color can be create using red,blue and green<br>
Answer:<br>
|Red| = 256<br>
|Blue| = 256<br>
|Green| = 256<br>
|$Red \times Blue \times  Green| = 256^3$<br>

-----------------
## Permutation
A permutation is a combination of a set <br>
Consider a set A = {1,2,3}<br>
so, the different permutation possible from this set we following,<br>

||
-----------------
123    |
132    |
231    $\text{total 6 permutation are possible} \ 6 = 3!$
312    |
321    |
213    |

`Q`.There are 20 different songs in your playlist .What will be possible distance orders we can play the songs?<br>
Answer : 20!

-------------
## K Permutation
- The number of k permutation possible from a set of n direct elements are,<br>
$A = \{a_1,a_2,\dots,a_n\} \\ = \frac{n!}{(n-k)!} , (k \leq n)$

When some elements are being repeated int the set from where we are drawing permutation , then the number of n size permutation from a n size set can be written as,<br>
$P = \frac{n!}{k_1!k_2!\dots,k_n!}$<br>
where n is the size of the set.<br>
$k_1!k_2!\dots,k_n!$ are frequency or number of nth elements in A.<br>
`Example`: {SWAGAT}<br>
ANSWER : $\{\frac{6!}{2!}\} = 360$<br>

1. Permutation without repetition <br>
```python
from math import factorial
def permutation (n,r):
    return factorial(n)//factorial(n-r)
print(permutation(5,3))

```
2. Permutation without repetition <br>
```python
from collections import Counter
def rep_permutation (word):
    from math import factorial
    counts = Counter(word)
    denominator = 1
    for count in counts.values():
        denominator *= factorial(count)
    return factorial(len(word)) // denominator
print(rep_permutation("SWAGAT"))
```
`Q`.A group of 10 people {A,B,C,D,E,F,G,H,I,J} are to the seated in a row with 10 chairs.The arrangement must having following constrains<br>
1. A and B must be to each other<br>
2. C and D must not sit next to each other<br>

What is possible number of such arrangement.<br>
Answer: $\{AB,C,D,E,\dots,F\} \Rightarrow  9! \times 2! \\ \{AB,CD,E,\dots,F\} \Rightarrow 8! \times 2! \times 2! \\ = (9! \times 2! )-(8! \times 2!\times 2!) \\ =564480 $

--------
## Combination of a set :-<br>
The number of combination of k out of n distinct elements or k-combination is <br>
$C_k = \binom{n}{k} = \frac{n!}{k!(n-k)!}$<br>
$A = \{a_1,a_2,\dots,a_n\}$

-----------------------
## Binomial Theorem

The binomial theorem states:

$$(x + y)^n = \sum_{k=0}^n \binom{n}{k} x^{n-k} y^k$$

Where:
- $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ is the binomial coefficient.
- $n$ is a non-negative integer.
```python
from scipy import special
print(special.comb(20, 4))
```
OUTPUT : <br>
4845.0<br>
using scipy , doing this is more effecitive because it's optimaiged(for large computatuional it will take less time).<br>

`With pre - allocation`
```python
import time
number = 1000000
start = time.time()
list = [None]*number
for i in range(number):
    list[i] = i
print(time.time() - start)
```
Output:<br>
0.05968904495239258

`Without pre - allocation`
```python
import time
number = 1000000
structure = time.time()
list = []
for i in range(number):
    list.append(i)
print(time.time() - structure)
```
Output:<br>
0.047866106033325195

`Q`.A salemanes has to travell from home city A and deliver parcel to all the other city B,C,D,E,F and has to return to A again .<br>
The distasnce bertween every two cities are given to above the distance we need .<br>
Answer : $^{6}C_{2} = \frac{5!}{2} \text{ memory allocation .}$<br>

---
## Encrypted message
```python
Codedmessage = 'nzohfu gur rarzl nz avtug'
for counter in range(26):
    guessmessage = ''
    for x in Codedmessage:
        if x != ' ':
            if ord(x) + counter <= 122:
                x = chr(ord(x) + counter)
            else:
                x = chr(ord(x) + counter - 26)
        guessmessage += x
    print(counter, guessmessage)
```
Output : <br>
0 nzohfu gur rarzl nz avtug<br>
1 oapigv hvs sbsam oa bwuvh<br>
2 pbqjhw iwt tctbn pb cxvwi<br>
3 qcrkix jxu uduco qc dywxj<br>
4 rdsljy kyv vevdp rd ezxyk<br>
5 setmkz lzw wfweq se fayzl<br>
6 tfunla max xgxfr tf gbzam<br>
7 ugvomb nby yhygs ug hcabn<br>
8 vhwpnc ocz zizht vh idbco<br>
9 wixqod pda ajaiu wi jecdp<br>
10 xjyrpe qeb bkbjv xj kfdeq<br>
11 ykzsqf rfc clckw yk lgefr<br>
12 zlatrg sgd dmdlx zl mhfgs<br>
13 ambush the enemy am night<br>
14 bncvti uif fofnz bn ojhiu<br>
15 codwuj vjg gpgoa co pkijv<br>
16 dpexvk wkh hqhpb dp qljkw<br>
17 eqfywl xli iriqc eq rmklx<br>
18 frgzxm ymj jsjrd fr snlmy<br>
19 gshayn znk ktkse gs tomnz<br>
20 htibzo aol lultf ht upnoa<br>
21 iujcap bpm mvmug iu vqopb<br>
22 jvkdbq cqn nwnvh jv wrpqc<br>
23 kwlecr dro oxowi kw xsqrd<br>
24 lxmfds esp pypxj lx ytrse<br>
25 mynget ftq qzqyk my zustf<br>

## Constant of this algorithm
1. The set of possible solution or solution space is sufficent small.<br>
2. It must be possible to determine the correct solution given otput from each possible solution.<br>
---
## 2S Complement
It is a method use in computing to represent signed integers(both postive and negative) in binary.It is the most common way to represent the negative number in binary system.<br>
***work- principle of 2's component***<br>
1. For postive number 2's components just normal binary represent.
2. For negative number 2's component form is calculate by : <br>
a. writing the number in binary.<br>
b. Inverting the bit(Converting 0 to 1, 1 to 0).<br>
c. add 1 to the right most bit of the invert bit.<br>

`Example` : +5 binary representation (4-bit representation)<br>
0101<br>
-5 in 2's complement representation<br>
convert 5 in binary $\rightarrow$ 0101<br>
invert the bits $\rightarrow$ 1010 (1's complement)<br>
add 1 $\rightarrow$ 1010 + 1 = 1011 $\rightarrow$ 2's complement form or, -5 in 4 bit <br>

`Q`. A University commision consists of 10 members inscluding 6 men and 4 woman .In how many ways can a 5 member and commited can be formed where at least 2 men and atleast 2 women exist.<br>

Answer : $\binom{6}{2} \times \binom{4}{3} + \binom{6}{3} \times \binom{4}{2}$


`Q`.How many such subcommited can be formed if a spefic person (men/women) must be include in every solution?<br>

Answer : $\binom{5}{1} \times \binom{4}{3} + \binom{5}{2} \times \binom{4}{2} + \binom{6}{2} \times \binom{3}{2} + \binom{6}{2} \times \binom{3}{1}$

`Q`.Write Python program of each with Scipy or Math modele.<br>
Answer :<br>
Code for question number 1 <br>
```python
from scipy.special import comb
men, women, committee_size = 6, 4, 5
total_ways = sum(
    comb(men, men_count, exact=True) * comb(women, committee_size - men_count, exact=True)
    for men_count in range(2, min(committee_size, men) + 1)
    if 2 <= committee_size - men_count <= women
)
print(total_ways)
```
Code for question number 2<br>
```python
from math import comb

specific_person_included_ways = sum(
    comb(men - 1, men_count) * comb(women, (committee_size - 1) - men_count)
    for men_count in range(1, min(committee_size - 1, men - 1) + 1)
    if 1 <= (committee_size - 1) - men_count <= women
)
print(specific_person_included_ways)

```
