# Elements of discrete probability

`Random experiment` :<br>
A random experiment is any process that has uncertain outcome.<br>
Tossing of a coin : {H,T} <br>
Rolling of dice - {1,2,3,4,5,6}<br>

<b>`Outcomes`</b>: Each possible result of a random experiment is called outcome.<br>
`Sample space` : Set of all outcomes of a random experiment.<br>
`Event` : any subset of a sample space.<br>
$C_1 = \{H,T\} \\
C_2 = \{H,T\} \\
C_3 = \{H,T\}$<br>
$C_1 \times C_2 \times C_3 = \{HHH,HHT,HTH,HTT,THH,THT,TTH,TTT\} -- \text{Sample space}$<br>
{HHH,HTH,THH} = only two heads are there<br>
$\binom{8}{0} + \binom{8}{1} + \binom{8}{2} + \dots + \binom{8}{8}$<br>

$$(x+y)^n = \sum_{k=0}^n {^nC_r} x^k y^{n-k} $$

----
## Probability Measurement
A probability measurement is a function P : {set of all elements}->[0,1] that maps any events to a number between 0 to 1 and has the following properties,<br>
i) P(s) = 1<br>
ii) P holds the countable additive i.e if $A_1,A_2,\dots,A_n $ are mutually disjoint event then $P(A_1,A_2,\dots,A_n) = P(A_1)+P(A_2)+P(A_3) + \dots $<br>
$Q = \{\frac{m}{n} , gcd (m,n) = 1 , n = m , m = 1,\dots\}$<br>
$Q^c$ = uncountable infinite<br>

## Probability Measurement
A PM is a function P = {set of all events} --> [0,1] such that P(s) = 1 [Probability of whole sample space is 1] and if $A_1,A_2,\dots,A_n$ are countable mutual disjoint events then, $P(A_1 \cup A_2 \cup A_3\dots) = P(A_1)+P(A_2)\dots$<br>

### Theorms based on this definition
Let A and B are two events the $P(A\cup B) = P(A)+P(B)\dots$ if A and B disjoints . And<br>
i. A and B are disjointed<br>
ii. $P(\phi) = 0$<br>
iii.$P(A^c)=i - P(A)$<br>

Proof 1 <br>
P(s) = 1<br>
$P(S \cup \phi) = 1 \hspace{1cm} [s \cup \phi = s]$<br>
$P(S) + P(\phi) = 1 \hspace{1cm} [s \cap \phi = s]$<br>
$1 + P(\phi) = 1 \hspace{1cm} P(S \cup \phi) = P(s) + P(\phi)$<br>
$P(\phi) = 0$

Proof 2<br>
P(s) = 1<br>
$P(A \cup A^c) = 1$<br>
$P(A) + P(A^c) = 1$<br>
$P(A^c) = 1 - P(A)$<br>

### Monotonicity
If $A \subset B $ then P(A) $\le$ P(B)<br>
$B = A \cup (B-A)$<br>
$P(B) = P(A)+P(B-A)$<br>
$P(B) \ge P(A)$<br>

Q. A football match will take place between Real Madrid CF and FC Barcelora .A sport analysis has forcast that Madrid has 40 % winning chance and Barcrlona has 50% winning chance what is probability that a draw occur<br>
Answer : <br>
P(M) = 40%<br>
P(B) = 50% <br>
P(d) = ?<br>
$M \cup B \cup d = S $<br>
$P(M \cup B \cup d) = 1$<br>
$P(M)+P(B)+P(d) = 1$<br>
0.4+0.5+P(d) = 1<br>
p(d) = 0.1<br>

### Classification probability or Laplacian probability
Laplacian Random experiment:<br>
A LRE is an experiment where every possible outcome has the same probability<br>
Example: Tossing of coin(Fair coin)<br>
Rolling of 6 face dice<br>
#### Theorem:
1. The sample space is finite,$|S| = |{S_1,S_2,\dots,S_n}| = n< \infin $<br>
2. The probability of each outcome is 1/n where n = |S|.<br>
3. The probability of any event $ E \subseteq
 is \frac{|E|}{|s|}$<br>

Q1. Suppose, the sample space is infinite i.e there are infinite many outcome in the sample space say ${S_1,S_2,\dots,S_n}$ <br>
Now by definition of probability measure <br>
$P({S_1,S_2,\dots,S_n}) = 1\\
\Rightarrow P({S_1})+P({S_2})+P({S_3})\dots = 1 $<br>
Since every outcome has same probability <br>
Assume $P(S_j) = C $ for all j.<br>
$C_1 + C_2 + \dots \infin \neq 1 $(not possible)<br>
So, the sample space is finite.

## Monotonicity
If $A \subseteq B$ then $P(A) \le P(B)$<br>
$B = A \cup (B - A)$<br>
$P(B) = P(A) + P(B-A)$<br>
$P(B) \geq P(A)$



## Condition Probability
For two events A and B where P(B) > 0 , the conditional probability of A given B is defined as,<br>
$P(\frac {A}{B}) = \frac {P(A \cap B)}{P(B)} $<br>
$P(\frac {A}{B}) \Rightarrow $ Probability of A when there is a condition that B has already happen } A is given B.<br>
$P(A \cap B)\Rightarrow$ is the joint probability of occuring A and B together.<br>
P(B) is the probability of event B.<br>

|Temperature |Frequency| Rain - frequency|
-------------|---------|--------------------|
|51 - 60(in F)| 4 |1|
|61 - 70| 12 |5|
|71 - 80| 13 |10|
|81 - 90| 20 |8|
|91 - 100| 1 |1|
|Total| 50 | 25 |

B = {it rains}<br>
$P = \{51 <= T <= 60|B\} = ? $<br>
$P(\frac{T}{B}) =\frac {P(T \cap B)}{P(B)}$<br>
$P(B) = \frac{25}{50}$<br>
${P(T \cap B)} = \frac{1}{50}$<br>
$P (\frac {T}{B}) = \frac {\frac {1}{50}}{\frac {25}{50}}$<br>
For condition probability ,<br>
we know<br>
$P(A \cap B ) = \frac {P(A \cap B)}{P(B)}$<br>
$\Rightarrow P(A \cap B ) = P(B)P(A|B) \rightarrow 1$<br>
Similary,<br>
$P(B | A ) = \frac {P(B \cap A)}{P(A)} $<br>
$\Rightarrow P(A \cap B ) = P(A)P(B|A)$<br>
So, $P(A \cap B ) = P(A)P(B|A) = P(B)P(A|B)$ it is call multiplication rule<br>

## The law of Total Probability
Let , $A_1,A_2,\dots $ be a partition of a sample space s. Let B be an event , then <br>

$P(B) = \sum_{n=1}^\infin P(A_m \cap B) = \sum_{n=1}^\infin P(B|A_n)P(A_m) $<br>

Proof:<br>

since $ S = A_1 \cup A_2 \cup A_3 \cup \dots $<br>
$B \cap S = (B )$
