# Formal logic and parts of the Truth Tables

### Condition of the following statements :
1. All penguin are orange.<br>
2. All Orange animal live in countries are equator<br>
3. The equator animals live in countries on equator.<br>
4. South Africa is on equator.<br>
5. All penguin live in South Africa.<br>

- The statement from (1) to (5) are called proposition.<br>
- The statement from (1) to (4) are called premises.<br>
- The statement (5) is the conclusion if all premises are true.<br>

### Logical connection
| Connective  | Notation | Meaning in English    |
|-------------|----------|-----------------------|
| Negation    | ~p       | p is not true         |
| Conjunction | $p\land q$      | both p and q          |
| Disjunction | $p\lor q$    | either p or q         |
| Conditional | $p\rightarrow q$   | if p, then q          |
| Biconditional | $p\leftrightarrow q$ | if and only if p and q |

#### Negation
| $p$ | $\neg p$ |
|---|----|
| 0 |  1 |
| 1 |  0 |

#### Conjunction
| $p$ | $q$ | $p\land q$ |
|---|---|-------|
| 0 | 0 |   0   |
| 0 | 1 |   0   |
| 1 | 0 |   0   |
| 1 | 1 |   1   |


#### Disjunction
| $p$ | $q$ | $p\lor q$ |
|-----|-----|-----------|
|  0  |  0  |     0     |
|  0  |  1  |     1     |
|  1  |  0  |     1     |
|  1  |  1  |     1     |


#### Conditional
| $p$ | $q$ | $p\rightarrow q$|
|-----|-----|-----------------|
| 0   | 0   |   1             |
| 0   | 1   |   1             |
| 1   | 0   |   0             |
| 1   | 1   |   1             |

#### Biconditional
| $p$ | $q$ | $p\leftrightarrow q$  |
|-----|-----|-----------------------|
| 0 | 0 |          1            |
| 0 | 1 |          0            |
| 1 | 0 |          0            |
| 1 | 1 |          1            |

#### `Q`.Truth Table for $\neg(p \land q) \leftrightarrow (p \lor \neg q) .$
`ANSWER`:<br>

| $p$ | $q$ | $p\land q$ | $\neg p$ | $\neg q$ | $\neg(p \land q)$ | $\neg p \lor \neg q$ | $\neg(p \land q) \leftrightarrow (p \lor \neg q) $ |
|---|---|-------|----|----|---------|----------|---------------------------------------|
| 0 | 0 |   0   |  1 |  1 |    1    |    1     |                  1                    |
| 0 | 1 |   0   |  1 |  0 |    1    |    1     |                  1                    |
| 1 | 0 |   0   |  0 |  1 |    1    |    1     |                  1                    |
| 1 | 1 |   1   |  0 |  0 |    0    |    0     |                  1                    |
	
#### `Q`.Truth Table for $(p\rightarrow q) \leftrightarrow (\neg q\rightarrow \neg p).$
`ANSWER`:<br>
| $p$ | $q$ |$p\rightarrow q$| $\neg q$ | $\neg p$ | $\neg q \rightarrow \neg p$|$(p\rightarrow q) \leftrightarrow (\neg q\rightarrow \neg p)$ |
|---|---|-------------------|----|----|---------------------|-------------------------------------|
| 0 | 0 |         1         |  1 |  1 |          1          |                 1                   |
| 0 | 1 |         1         |  0 |  1 |          1          |                 1                   |
| 1 | 0 |         0         |  1 |  0 |          0          |                 1                   |
| 1 | 1 |         1         |  0 |  0 |          1          |                 1                   |

### Contrapositivity
1. if p then q.<br>
2. if negative of q, then negation of p.<br>

both are equivalent statement.

## Law of Transitivity
If p then q, and if q then r, then if p then r.

### Symbolic Representation
$(p\rightarrow q) ∧ (q \rightarrow r) → (p \rightarrow r)$

### XOR
#### XOR (Exclusive OR)
A $\oplus$ B = ( A ^ B)

| p | q | p $\oplus$ q |
|---|---|-------|
| 0 | 0 |   0   |
| 0 | 1 |   1   |
| 1 | 0 |   1   |
| 1 | 1 |   0   |

### NAND
##### NAND (Not AND)
| $p$ | $q$ | $\neg (p \land q)$ |
|---|---|----------|
| 0 | 0 |    1     |
| 0 | 1 |    1     |
| 1 | 0 |    1     |
| 1 | 1 |    0     |

- Similarity :
$A \rightarrow B = - A \lor B$<br>
$A \leftrightarrow B=(A\land B)\lor(\neg A\lor\neg B)$<br>
or<br>
$(A\lor-B)\lor(\neg A\lor\neg B)$<br>

### DNF(Disjuction normal form):
- A Bollean exprestion is called DNF if it is written as a disjuction $(\lor)$ of conjuction $(\land)$ of literas. <br>
Example :$$(A \land B) \lor (B \land C) \lor (\neg A \land C)$$<br>

### CNF:
- A bollean expression is called Conjuction normal from or CNF if it is written as conjuction at disjuction of literals.<br>
Example : $$(A \lor \neg B) \land (B \lor C)$$<br>

`PROVE`:<br>
$$(\neg A \land B)\lor(\neg(A \lor C))\lor(\neg B \land C) = \neg A$$
#### Proof:
$$(\neg A \land B) \lor (\neg (A \lor C)) \lor (\neg B \land C) = \neg A$$

1. Distribute the negation inside the parentheses:<br>
    $(\neg A \land B) \lor (\neg A \land \neg C) \lor (\neg B \land C)$

2. Apply the distributive property:<br>
    $\neg A \land (B \lor \neg C) \lor (\neg B \land C)$

3. Distribute again:<br>
    $\neg A \land (B \lor \neg C \lor \neg B \lor C)$

4. Simplify the expression inside the parentheses:<br>
    $B \lor \neg B \lor \neg C \lor C = \text{True}$

5. Therefore:<br>
    $\neg A\land \text{True} = \neg A$

Hence, the given expression simplifies to:<br>
$\neg A$

`Q`<br>
1. $(\neg A\land B)\lor(\neg (A\lor C))\lor(\neg B\land C) = \neg A$<br>
$ A_{NSWER}$:<br>
#### Proof:
$$(\neg A \land B) \lor (\neg (A \lor C)) \lor (\neg B \land C) = \neg A$$

1. Distribute the negation inside the parentheses:<br>
    $$(\neg A \land B) \lor (\neg A \land \neg C) \lor (\neg B \land C)$$

2. Apply the distributive property:<br>
    $$\neg A \land (B \lor \neg C) \lor (\neg B \land C)$$

3. Distribute again:<br>
    $$\neg A \land (B \lor \neg C \lor \neg B \lor C)$$

4. Simplify the expression inside the parentheses:<br>
    $$B \lor \neg B \lor \neg C \lor C = \text{True}$$

5. Therefore:<br>
    $$\neg A \land \text{True} = \neg A$$

Hence, the given expression simplifies to:<br>
$$\neg A$$


2. $G(A, B, C) = (A\oplus B)\lor (B\Rightarrow C) \land (\neg A\lor C) = \neg A\land\neg B\lor C$<br>
$ A_{NSWER}$:<br>
#### Proof:
$G(A, B, C) = (A \oplus B) \lor (B \rightarrow C) \land (\neg A \lor C)$

1. Expand $A \oplus B$ using its definition:<br>
    $A \oplus B = (A \land \neg B) \lor (\neg A \land B)$<br>
    So,<br>
    $G(A, B, C) = [(A \land \neg B) \lor (\neg A \land B)] \lor [(B \rightarrow C) \land (\neg A \lor C)]$

2. Expand $B \rightarrow C$ using its definition:<br>
    $B \rightarrow C = \neg B \lor C$<br>
    Substituting this,<br>
    $G(A, B, C) = [(A \land \neg B) \lor (\neg A \land B)] \lor [(\neg B \lor C) \land (\neg A \lor C)]$

3. Apply the distributive property to the second term:<br>
    $[(\neg B \lor C) \land (\neg A \lor C)] = (\neg B \land \neg A) \lor (\neg B \land C) \lor (C \land \neg A) \lor (C \land C)$<br>
    Simplify:<br>
    $(\neg B \land \neg A) \lor (\neg B \land C) \lor (C \land \neg A) \lor C$

4. Substitute back into $G(A, B, C)$:
    $G(A, B, C) = [(A \land \neg B) \lor (\neg A \land B)] \lor [(\neg B \land \neg A) \lor (\neg B \land C) \lor (C \land \neg A) \lor C]$

5. Combine terms and simplify:
    $G(A, B, C) = (\neg A \land \neg B) \lor C$

Hence,<br>
$G(A, B, C) = \neg A \land \neg B \lor C$

3. $H(A, B, C) = (A\land B)\land(\neg A\land B)\land (A\lor\neg B\lor C) =\text{Convert it into the normal form.}$<br>
$ A_{NSWER}$:<br>
#### Proof:
$H(A, B, C) = (A \land B) \land (\neg A \land B) \land (A \lor \neg B \lor C)$

1. Simplify $(A \land B) \land (\neg A \land B)$:
    - $(A \land B) \land (\neg A \land B) = (B \land A \land \neg A)$
    - Since $A \land \neg A = \text{False}$:
      - $(B \land A \land \neg A) = \text{False}$

2. Combine with the remaining term:
    - $\text{False} \land (A \lor \neg B \lor C) = \text{False}$

Hence, the normal form of $H(A, B, C)$ is:
$$H(A, B, C) = \text{False}$$

4. $M(A, B, C) = (A \land B) \lor (B\land C)\lor(A \land C) = \text{Converted into the minimal form}$<br>
$ A_{NSWER}$:<br>
#### Proof:
$M(A, B, C) = (A \land B) \lor (B \land C) \lor (A \land C)$

1. Apply the distributive property to group terms:
    $M(A, B, C) = (A \land B) \lor (A \land C) \lor (B \land C)$

2. Observe that the expression is already in its minimal form, as no further simplification can be made without altering the logical equivalence.

Hence, the minimal form of $M(A, B, C)$ is:
$$(A \land B) \lor (B \land C) \lor (A \land C)$$

#### Application of logical in Theoretical mathematics

`Q`. Statement to proved :<br>
if $n^2$ is even , n is also even<br>
Contrapostivity:<br>
$p\ \underline{\rightarrow}\ q \\
\neg q \rightarrow \neg p $

n is odd, then $n^2$ is also odd.
Let say, n be an odd number.<br>
So, n = 2n + 1<br>
$\implies n^2 = (2n+1)^2$<br>
$\implies n^2 = 4n^2 +4n +1$<br>
$\implies n^2 = 2(2n^2+2n)+1\rightarrow$ odd number<br>
So, $n^2$ is odd $\implies$ n is also odd <br>
$n^2$ is even $\implies$ n is even.<br>

`Q`. Prove that $\sqrt2$ is an irrational number.<br>
Let us consider<br>
$\sqrt2 = \frac{p}{q}$ where GCD (a,b) = 1<br>
$\implies 2 = \frac{p^2}{q^2}$<br>
$\implies a^2 = 2b^2$<br>
So, $a^2$ is an even number, so a is also even<br>
$2b^2 = (2n)^2 [a\ is\ even \Rightarrow a = 2n ]$<br>
$\implies 2b^2 = 4n^2$<br>
$\implies b^2 = 2n^2$<br>
So, $b^2$ is an even number so b is called even.<br>

`Q`. Proof by Mathematical induction.<br>
Mathematical induction allows us to proved each of an infinite sequence of logical statement  $p_1,p_2$....is true.This argument involve to following .<br>

#### Step:<br>
* Basic steps : Prove $P_i$ is true <br>
* Inductive : for a fixed i $\ge$ 2 value, consider $P_i$ is true and then prove $P_{i+1}$ is true.<br>

Sum of n natural number is $\frac{n(n+1)}{2}$<br>
$P_1 = \frac{1(1+1)}2 = 1\ \ [P_1\ \text{is true}]$<br>
$P_2 = \frac{2(2+1)}2 = 3\ \ [P_2\ \text{is true}]$<br>
suppose $P_n$ is true<br>
$P_{n+1} = (n+1)+\frac{n(n+1)}2 = \frac{2n + 2 + n^2 + n}2 = \frac{(n+1)(n+2)}2 = \frac{(n+1)((n+1)+1)}2$<br>
So by induction $P_n$ is true for all n.<br>

`Q`. By Mathematical induction prove that<br>
$i ! > 2^i \ for\ i \geq 4$<br>
$(i! > 2^i)$<br>
$\implies (i+1)! > 2^{i(i+1)}$<br>
$\implies (i+1)!>2^i\times i + 2^i > 2^i.2 + 2^i > 2^{(i+1)}$<br>
$\implies (i+1)! > 2^{(i+1)}$<br>

Prove the following statement using Mathematic induction<br>
`1`. $\frac{1}{1.2}+\frac{1}{2.3}+\frac{1}{3.4}+...+\frac{1}{n(n+1)} = \frac{n}{n+1}$<br>

proof :<br>
$P_1 = \frac{1}{2} \ \ P_2 = \frac{1}{6} P_3 = \frac{1}{12} \\ P_t = \frac{1}{2} +\frac{1}{6} +\frac{1}{12}  \\ \hspace{0.45cm} = \frac{6+2+1}{12} = \frac{9}{12} = \frac{3} {4} = LHS \\ \text{Let n = 3} \\ RHS = \frac{3}{3+1} = \frac{3}{4}\\LHS = RHS \\ \text{Hence prove...} $


`2`. $2+2^2+2^3+...+2^n = 2(2^n-1)$<br>

proof :<br>
$LHS = P_1 = 2 \ \ P_2 = 2+2^2 = 6 \ \ P_3 = 2+2^2+2^3 =14 \\\text{Let n = 3} \\RHS = 2(2^3-1) =2(8-1) =2(7)=14 \\LHS = RHS \\ \text{Hence prove...} $


`3`. $4^n-1$ is divisible by 3.

proof :<br>
$\text{Let n = 2} \\ 4^2 - 1 = 16-1 = 15 \\ \text{Let n = 1} \\ 4^1 -1 =4 -1 = 3 \\ \text{Hence prove it is divisible by 3.}$
