
# Linear Algebra I  

Peter Philip\*  

Lecture Notes  

Originally Created for the Class of Winter Semester 2018/2019 at LMU Munich Includes Subsequent Corrections and Revisions  

# Contents  

## 1 Foundations: Mathematical Logic and Set Theory 5  

1.1 Introductory Remarks 5   
1.2 Propositional Calculus 6   
1.2.1 Statements 6   
1.2.2 Logical Operators 7   
1.2.3 Rules . 9   
1.3 Set Theory. 14   
1.4 Predicate Calculus 18  

## 2 Functions and Relations 25  

2.1 Functions 25   
2.2 Relations 34   
2.2.1 Definition and Properties . 34   
2.2.2 Order Relations 36   
2.2.3 Equivalence Relations 39  

## 3 Natural Numbers, Induction, and the Size of Sets 44  

3.1 Induction and Recursion 44   
3.2 Cardinality: The Size of Sets . 50   
3.2.1 Definition and General Properties 50   
3.2.2 Finite Sets 53   
3.2.3 Countable Sets 58  

## 4 Basic Algebraic Structures 60  

4.1 Magmas and Groups 60   
4.2 Rings and Fields 79  

## 5 Vector Spaces 91  

5.1 Vector Spaces and Subspaces .. 91   
5.2 Linear Independence, Basis, Dimension 98  

## 6 Linear Maps 113  

6.1 Basic Properties and Examples 113   
6.2 Quotient Spaces . 122   
6.3 Vector Spaces of Linear Maps 126  

## 7 Matrices 130  

7.1 Definition and Arithmetic 130   
7.2 Matrices as Representations of Linear Maps 135   
7.3 Rank and Transpose 141   
7.4 Special Types of Matrices. 145   
7.5 Blockwise Matrix Multiplication .. 151  

## 8 Linear Systems 153  

8.1 General Setting 153   
8.2 Abstract Solution Theory 155   
8.3 Finding Solutions . 157   
8.3.1 Echelon Form, Back Substitution. 157   
8.3.2 Elementary Row Operations, Variable Substitution 162   
8.3.3 Gaussian Elimination . 164   
8.4 LU Decomposition 169   
8.4.1 Definition and Motivation. 169   
8.4.2 Elementary Row Operations Via Matrix Multiplication . . 170   
8.4.3 Existence 179   
8.4.4 Algorithm 181  

## A Axiomatic Set Theory 185  

A.1 Motivation, Russell's Antinomy. 185   
A.2 Set-Theoretic Formulas .. 186   
A.3 The Axioms of Zermelo-Fraenkel Set Theory 188   
A.3.1  Existence, Extensionality, Comprehension 189   
A.3.2 Classes 192   
A.3.3 Pairing, Union, Replacement .. 193   
A.3.4 Infinity, Ordinals, Natural Numbers. 197   
A.3.5 Power Set 205   
A.3.6 Foundation 206   
A.4 The Axiom of Choice. 207   
A.5 Cardinality 213  

## B Associativity and Commutativity 221  

B.1 Associativity . 221   
B.2 Commutativity 224  

C Groups 225  

D Number Theory 227  

E Vector Spaces 231  

E.1 Cardinality and Dimension 231   
E.2 Cartesian Products. 232  

## F Python Source Code of Implemented Algorithms 233  

F.1Linear Systems 234   
F.1.1 Back and Forward Substitution. 234   
F.1.2 Gaussian Elimination and LU Decomposition 235   
F.1.3 Examples 238  

References  

240  

## 1 Foundations: Mathematical Logic and Set Theory  

### 1.1 Introductory Remarks  

The task of mathematics is to establish the truth or falsehood of (formalizable) statements using rigorous logic, and to provide methods for the solution of classes of (e.g. applied) problems, ideally including rigorous logical proofs verifying the validity of the methods (proofs that the method under consideration will, indeed, provide a correct solution).  

The topic of this class is linear algebra, a subfield of the field of algebra. Algebra. in the sense of this class is also called abstract algebra and constitutes the study of. mathematical objects and rules for combining them (one sometimes says that these rules form a structure on the underlying set of objects). An important task of algebra. is the solution of equations, where the equations are formulated in some set of objects. with a given structure. In linear algebra, the sets of objects are so-called vector spaces. (the objects being called vectors) and the structure consists of an addition, assigning two vectors $v,w$ their sum vector $v+w$ , together with a scalar multiplication, assigning a. scalar (from a so-called scalar field, more about this later). $\lambda$ and a vector $\upsilon$ the product vector $\lambda v$ . In linear algebra, one is especially interested in solving linear equations, i.e. equations of the form $A(x)=b$ , where $A$ is a linear function, i.e. a function, satisfying.  

$$
A(\lambda v+\mu w)=\lambda A(v)+\mu A(w)
$$  

for all vectors $v,w$ and all scalars $\lambda,\mu$ . Before we can properly define and study vector spaces and linear equations, it still needs some preparatory work. In modern mathematics, the objects under investigation are almost always so-called sets. So one aims at deriving (i.e. proving) true (and interesting and useful) statements about sets from other statements about sets known or assumed to be true. Such a derivation or proof means applying logical rules that guarantee the truth of the derived (i.e. proved) statement.  

However, unfortunately, a proper definition of the notion of set is not easy, and neither is an appropriate treatment of logic and proof theory. Here, we will only be able to briefly touch on the bare necessities from logic and set theory needed to proceed to the core matter of this class. We begin with logic in Sec. 1.2, followed by set theory in Sec. 1.3, combining both in Sec. 1.4. The interested student can find an introductory. presentation of axiomatic set theory in Appendix A and he/she should consider taking a separate class on set theory, logic, and proof theory at a later time..  

### 1.2 Propositional Calculus  

#### 1.2.1 Statements  

Mathematical logic is a large field in its own right and, as indicated above, a thorough introduction is beyond the scope of this class - the interested reader may refer to [EFT07] [Kun12], and references therein. Here, we will just introduce some basic concepts using common English (rather than formal symbolic languages - a concept touched on in Sec. A.2 of the Appendix and more thoroughly explained in books like [EFT07]).  

As mentioned before, mathematics establishes the truth or falsehood of statements. By. a statement or proposition we mean any sentence (any sequence of symbols) that can reasonably be assigned a truth value, i.e. a value of either true, abbreviated T, or false, abbreviated F. The following example illustrates the difference between statements and sentences that are not statements:  

Example 1.1. (a) Sentences that are statements:  

Every dog is an animal. (T)   
Every animal is a dog. (F)   
The number 4 is odd. (F).   
$2+3=5$ . (T)   
$\sqrt{2}<0$ . (F)   
$x+1>0$ holds for each natural number $x$ .(T)  

(b) Sentences that are not statements:  

Let's study calculus!.   
Who are you?.   
$3\cdot5+7$   
$x+1>0$   
All natural numbers are green.  

The fourth sentence in Ex. 1.1(b) is not a statement, as it can not be said to be either. true or false without any further knowledge on. $x$ .The fifth sentence in Ex. 1.1(b) is. not a statement as it lacks any meaning and can, hence, not be either true or false. It would become a statement if given a definition of what it means for a natural number to be green.  

#### 1.2.2 Logical Operators  

The next step now is to combine statements into new statements using logical operators,. where the truth value of the combined statements depends on the truth values of the original statements and on the type of logical operator facilitating the combination.  

The simplest logical operator is negation, denoted $\neg$ . It is actually a so-called unary. operator, i.e. it does not combine statements, but is merely applied to one statement. For example, if. $A$ stands for the statement "Every dog is an animal.", then $\neg A$ stands for the statement "Not every dog is an animal."; and if $B$ stands for the statement "The. number 4 is odd.", then. $\neg B$ stands for the statement "The number 4 is not odd.", which can also be expressed as "The number 4 is even."  

To completely understand the action of a logical operator, one usually writes what is known as a truth table. For negation, the truth table is.  

$$
\frac{A\mid\neg A}{\mathrm{~T~}\left|\begin{array}{c}{\mathrm{F}}\ {\mathrm{T}}\end{array}\right|}
$$  

that means if the input statement. $A$ is true, then the output statement. $\neg A$ is false; if.   
the input statement. $A$ is false, then the output statement $\neg A$ is true.  

We now proceed to discuss binary logical operators, i.e. logical operators combining precisely two statements. The following four operators are essential for mathematical reasoning:  

Conjunction: $A$ and $B$ , usually denoted $A\wedge B$  

Disjunction:. $A$ or $B$ , usually denoted $A\lor B$  

Implication: $A$ implies $B$ , usually denoted $A\Rightarrow B$  

Equivalence: $A$ is equivalent to $B$ , usually denoted $A\Leftrightarrow B$  

Here is the corresponding truth table:  

$$
{\begin{array}{r l}&{{\frac{A\mid B}{\textrm{T}}}{\Big|}{\frac{A\land B}{\textrm{T}}}{\Big|}{\frac{A\lor B}{\textrm{T}}}{\Big|}{\begin{array}{c}{A\lor B}\ {\textrm{T}}\ {\textrm{F}}\ {\textrm{F}}\ {\textrm{F}}\end{array}}{\Big|}{\begin{array}{c}{A\lor B}\ {\textrm{T}}\ {\textrm{F}}\ {\textrm{F}}\end{array}}{\Big|}{\begin{array}{c}{A\Rightarrow B}\ {\textrm{T}}\ {\textrm{F}}\ {\textrm{T}}\ {\textrm{T}}\end{array}}{\Big|}{\begin{array}{c}{A\leftrightarrow B}\ {\textrm{T}}\ {\textrm{F}}\ {\textrm{F}}\ {\textrm{T}}\end{array}}}\ &{{\textrm{F}}{\Big|}{\begin{array}{c}{\textrm{F}}\ {\textrm{F}}\ {\textrm{F}}\end{array}}}
$$  

When first seen, some of the assignments of truth values in (1.2) might not be completely. intuitive, due to the fact that logical operators are often used somewhat differently in common English. Let us consider each of the four logical operators of (1.2) in sequence:.  

For the use in subsequent examples, let $A_{1},\ldots,A_{6}$ denote the six statements from Ex..   
1.1(a).  

Conjunction: Most likely the easiest of the four, basically identical to common language use: $A\wedge B$ is true if, and only if, both. $A$ and $B$ are true. For example, using Ex. 1.1(a),. $A_{1}\wedge A_{4}$ is the statement "Every dog is an animal and. $2+3=5$ ", which is true since both $A_{1}$ and $A_{4}$ are true. On the other hand,. $A_{1}\wedge A_{3}$ is the statement "Every dog is. an animal and the number 4 is odd.", which is false, since $A_{3}$ is false.  

Disjunction: The disjunction $A\lor B$ is true if, and only if, at least one of the statements. $A,B$ is true. Here one already has to be a bit. $\mathrm{careful}-A\lor B$ defines the inclusive or,. whereas "or' in common English is often understood to mean the exclusive or (which is false if both input statements are true). For example, using Ex. 1.1(a), $A_{1}\lor A_{4}$ is the statement "Every dog is an animal or. $2+3=5$ ", which is true since both. $A_{1}$ and $A_{4}$ are true. The statement $A_{1}\lor A_{3}$ , i.e. "Every dog is an animal or the number 4 is odd." is also true, since. $A_{1}$ is true. However, the statement. $A_{2}\vee A_{5}$ , i.e. "Every animal is a dog or $\sqrt{2}<0$ " is false, as both $A_{2}$ and $A_{5}$ are false.  

As you will have noted in the above examples, logical operators can be applied to. combine statements that have no obvious contents relation. While this might seem strange, introducing contents-related restrictions is unnecessary as well as undesirable, since it is often not clear which seemingly unrelated statements might suddenly appear. in a common context in the future. The same occurs when considering implications and equivalences, where it might seem even more obscure at first..  

Implication: Instead of. $A$ implies $B$ , one also says if. $A$ then $B$ $B$ is a consequence of $A$ $B$ is concluded or inferred from $A$ $A$ is sufficient for. $B$ , or $B$ is necessary for. $A$ . The implication $A\Rightarrow B$ is always true, except if. $A$ is true and $B$ is false. At first. glance, it might be surprising that $A\Rightarrow B$ is defined to be true for. $A$ false and $B$ true, however, there are many examples of incorrect statements implying correct statements. For instance, squaring the (false) equality of integers $-1=1$ , implies the (true) equality. of integers $1=1$ . However, as with conjunction and disjunction, it is perfectly valid to combine statements without any obvious context relation: For example, using Ex. 1.1(a), the statement $A_{1}\Rightarrow A_{6}$ , i.e. "Every dog is an animal implies $x+1>0$ holds for each natural number $x$ " is true, since $A_{6}$ is true, whereas the statement $A_{4}\Rightarrow A_{2}$ , i.e. $2+3=5$ implies every animal is a dog." is false, as $A_{4}$ is true and $A_{2}$ is false.  

Of course, the implication $A\Rightarrow B$ is not really useful in situations, where the truth values of both $A$ and $B$ are already known. Rather, in a typical application, one tries to establish the truth of $A$ to prove the truth of $B$ (a strategy that will fail if $A$ happens to be false).  

Example 1.2. Suppose we know Sasha to be a member of a group of students, taking a class in Linear Algebra. Then the statement $A$ "Sasha has taken a class in Linear  

Algebra before." implies the statement $B$ "There is at least one student in the group, who has taken the class before'. A priori, we might not know if Sasha has taken the Linear Algebra class before, but if we can establish that Sasha has, indeed, taken the class before, then we also know $B$ to be true. If we find Sasha to be taking the class for the first time, then we do not know, whether $B$ is true or false.  

Equivalence: $A\Leftrightarrow B$ means $A$ is true if, and only if, $B$ is true. Once again, using input statements from Ex. 1.1(a), we see that. $A_{1}\Leftrightarrow A_{4}$ , i.e. "Every dog is an animal is equivalent to $2+3=5$ .", is true as well as $A_{2}\Leftrightarrow A_{3}$ , i.e. "Every animal is a dog is equivalent to the number 4 is odd.". On the other hand, $A_{4}\Leftrightarrow A_{5}$ , i.e. $2+3=5$ is equivalent to $\sqrt{2}<0$ , is false.  

Analogous to the situation of implications, $A\Leftrightarrow B$ is not really useful if the truth values of both $A$ and $B$ are known a priori, but can be a powerful tool to prove $B$ to be true or false by establishing the truth value of $A$ . It is obviously more powerful than the implication as illustrated by the following example (compare with Ex. 1.2):  

Example 1.3. Suppose we know Sasha has obtained the highest score among the students registered for the Linear Algebra class. Then the statement $A$ "Sasha has taken the Linear Algebra class before." is equivalent to the statement $B$ "The student with the highest score has taken the class before." As in Ex. 1.2, if we can establish Sasha to have taken the class before, then we also know $B$ to be true. However, in contrast to Ex. 1.2, if we find Sasha to have taken the class for the first time, then we know $B$ to be false.  

Remark 1.4. In computer science, the truth value T is often coded as 1 and the truth value F is often coded as 0.  

#### 1.2.3 Rules  

Note that the expressions in the first row of the truth table (1.2) (e.g. $A\wedge B$ ) are not statements in the sense of Sec. 1.2.1, as they contain the statement variables (also known. as propositional variables) $A$ or $B$ . However, the expressions become statements if all. statement variables are substituted with actual statements. We will call expressions of. this form propositional formulas. Moreover, if a truth value is assigned to each statement. variable of a propositional formula, then this uniquely determines the truth value of the. formula. In other words, the truth value of the propositional formula can be calculated. from the respective truth values of its statement variables - a first justification for the name propositional calculus.  

Example 1.5. (a) Consider the propositional formula $(A\land B)\lor(\neg B)$ . Suppose $A$ is true and $B$ is false. The truth value of the formula is obtained according to the following truth table:  

$$
{\frac{A\mid B\mid A\land B\mid\neg B\mid(A\land B)\lor(\neg B)}{\operatorname{T}\mid\operatorname{F}\mid\operatorname{F}\mid\operatorname{T}}}
$$  

(b) The propositional formula $A\lor(\neg A)$ , also known as the law of the excluded middle, has the remarkable property that its truth value is T for every possible choice of truth values for $A$  

$$
\frac{A\mid\neg A\mid A\lor(\neg A)}{\mathrm{T}\mid\mathrm{~F~}\mathrm{~T~}}
$$  

Formulas with this property are of particular importance.  

Definition 1.6. A propositional formula is called a tautology or universally true if, and only if, its truth value is T for all possible assignments of truth values to all the statement variables it contains.  

Notation 1.7. We write. $\phi(A_{1},\ldots,A_{n})$ if, and only if, the propositional formula $\phi$ contains precisely the. $n$ statement variables $A_{1},\ldots,A_{n}$  

Definition 1.8. The propositional formulas $\phi(A_{1},\ldots,A_{n})$ and $\psi(A_{1},\dots,A_{n})$ are called equivalent if, and only if, $\phi(A_{1},\ldots,A_{n})\Leftrightarrow\psi(A_{1},\ldots,A_{n})$ is a tautology.  

Lemma 1.9. The propositional formulas $\phi(A_{1},\ldots,A_{n})$ and $\psi(A_{1},\dots,A_{n})$ are equiva lent if, and only if, they have the same truth value for all possible assignments of truth values to $A_{1},\ldots,A_{n}$  

Proof. If $\phi(A_{1},\ldots,A_{n})$ and $\psi(A_{1},\dots,A_{n})$ are equivalent and $A_{i}$ is assigned the truth value $t_{i}$ $i=1,\ldots,n$ , then $\phi(A_{1},\ldots,A_{n})\Leftrightarrow\psi(A_{1},\ldots,A_{n})$ being a tautology implies it has truth value T. From (1.2) we see that either $\phi(A_{1},\ldots,A_{n})$ and $\psi(A_{1},\dots,A_{n})$ both have truth value T or they both have truth value $\mathrm{F}$  

If, on the other hand, we know $\phi(A_{1},\ldots,A_{n})$ and $\psi(A_{1},\dots,A_{n})$ have the same truth value for all possible assignments of truth values to $A_{1},\ldots,A_{n}$ , then, given such an assignment, either $\phi(A_{1},\ldots,A_{n})$ and $\psi(A_{1},\dots,A_{n})$ both have truth value T or both have truth value $\mathrm{F}$ , i.e. $\phi(A_{1},\dots,A_{n})\Leftrightarrow\psi(A_{1},\dots,A_{n})$ has truth value T in each case, showing it is a tautology.  

For all logical purposes, two equivalent formulas are exactly the same - it does not matter if one uses one or the other. The following theorem provides some important equivalences of propositional formulas. As too many parentheses tend to make formulas less readable, we first introduce some precedence conventions for logical operators:  

Convention 1.10. $\neg$ takes precedence over $\wedge,\vee$ , which take precedence over $\Rightarrow,\Leftrightarrow$ So, for example,  

$$
(A\lor\neg B\Rightarrow\neg B\land\neg A)\Leftrightarrow\neg C\land(A\lor\neg D)
$$  

is the same as  

$$
{\Big(}{\big(}A\lor(\neg B){\big)}\Rightarrow{\big(}(\neg B)\land(\neg A){\big)}{\Big)}\Leftrightarrow{\Big(}(\neg C)\land{\big(}A\lor(\neg D){\big)}{\Big)}{\Big)}.
$$  

Theorem 1.11. (a) $(A\Rightarrow B)\Leftrightarrow\neg A\lor B$ . This means one can actually define implication via negation and disjunction.  

(b) $(A\Leftrightarrow B)\Leftrightarrow{\big(}(A\Rightarrow B)\land(B\Rightarrow A){\big)}$ , i.e. $A$ and $B$ are equivalent if, and only if, $A$ is both necessary and sufficient for $B$ .One also calls the implication $B\Rightarrow A$ the converse of the implication. $A\Rightarrow B$ .Thus, $A$ and $B$ are equivalent if, and only if,. both $A\Rightarrow B$ and its converse hold true..  

(c) Commutativity of Conjunction: $A\land B\Leftrightarrow B\land A$ (d) Commutativity of Disjunction: $A\lor B\Leftrightarrow B\lor A$ (e) Associativity of Conjunction: $(A\land B)\land C\Leftrightarrow A\land(B\land C)$  

(f) Associativity of Disjunction: $(A\lor B)\lor C\Leftrightarrow A\lor(B\lor C)$  

(g) Distributivity I: $A\land(B\lor C)\Leftrightarrow(A\land B)\lor(A\land C)$  

(h) Distributivity II: $A\lor(B\land C)\Leftrightarrow(A\lor B)\land(A\lor C)$  

(i) De Morgan's Law I: $\neg(A\land B)\Leftrightarrow\neg A\lor\neg B$ (j) De Morgan's Law II: $\neg(A\lor B)\Leftrightarrow\neg A\land\neg B$ (k) Double Negative: $\neg\neg A\Leftrightarrow A$ (1) Contraposition: $(A\Rightarrow B)\Leftrightarrow(\neg B\Rightarrow\neg A)$  

Proof. Each equivalence is proved by providing a truth table and using Lem. 1.9. (a):  

$$
\begin{array}{r l}&{\frac{A\textrm{\j}B\textrm{\j}\textrm{\j}\textrm{\j}A\textrm{\j}A\Rightarrow B\textrm{\j}\neg A\textrm{\forall}B}{\textrm{T}}}\ &{\textrm{T}\left[\textrm{F}\right]\textrm{\ensuremath{\left[\begin{array}{l}{\textrm{F}}\ {\textrm{F}}\ {\textrm{T}}\ {\textrm{T}}\end{array}\right]}}\textrm{\quad\stackrel{T}{F}}\textrm{\quad\stackrel{F}{T}}}\ &{\textrm{F}\left[\textrm{\j}\textrm{\j}\textrm{\j}\textrm{\j}\textrm{\j}\textrm{\j}\textrm{\j}\textrm{\j}\textrm{\phantom{-}}\textrm{T}\right]}\end{array}
$$  

(b) - (h): Exercise.  

(i):  

<html><body><table><tr><td>A</td><td>B</td><td>-A</td><td>-B</td><td>A^B</td><td>-(A ^ B)</td><td>-AV-B</td></tr><tr><td>T</td><td>T</td><td>F</td><td>F</td><td>T</td><td>F</td><td>F</td></tr><tr><td>T</td><td>F</td><td>F</td><td>T</td><td>F</td><td>T</td><td>T</td></tr><tr><td>F</td><td>T</td><td>T</td><td>F</td><td>F</td><td>T</td><td>T</td></tr><tr><td>F</td><td>F</td><td>T</td><td>T</td><td>F</td><td>T</td><td>T</td></tr></table></body></html>  

(j): Exercise.  

(k):  

$$
\begin{array}{r l}{~}&{{}\frac{A~\left\|~\neg A~\right\|\neg\neg A~}{\mathrm{T}}}\ {~}&{{}\mathrm{F}~}\end{array}
$$  

(1):  

<html><body><table><tr><td>A</td><td>B</td><td>-A</td><td>-B</td><td>A→ B</td><td>-B →A</td></tr><tr><td>T</td><td>T</td><td>F</td><td>F</td><td>T</td><td>T</td></tr><tr><td>T</td><td>F</td><td>F</td><td>T</td><td>F</td><td>F</td></tr><tr><td>F</td><td>T</td><td>T</td><td>F</td><td>T</td><td>T</td></tr><tr><td>F</td><td>F</td><td>T</td><td>T</td><td>T</td><td>T</td></tr></table></body></html>  

Having checked all the rules completes the proof of the theorem.  

The importance of the rules provided by Th. 1.11 lies in their providing proof techniques,. i.e. methods for establishing the truth of statements from statements known or assumed to be true. The rules of Th. 1.11 will be used frequently in proofs throughout this class.  

Remark 1.12. Another important proof technique is the so-called proof by contradiction, also called indirect proof. It is based on the observation, called the principle of contradiction, that $A\land\neg A$ is always false:  

$$
\begin{array}{l}{{\frac{A\enspace\vert\enspace\neg A\enspace\Vert\enspace A\wedge\neg A}{\mathrm{T}}}}\ {{\mathrm{~F~}}\enspace{\left[\begin{array}{l}{\mathrm{~F~}}\ {\mathrm{~T~}}\end{array}\right]}\enspace{\left[\begin{array}{l}{\mathrm{~F~}}\ {\mathrm{~F~}}\end{array}\right]}\enspace}}\end{array}
$$  

Thus, one possibility of proving a statement $B$ to be true is to show $\neg B\Rightarrow A\land\neg A$ for some arbitrary statement $A$ . Since the right-hand side of the implication is false, the left-hand side must also be false, proving $B$ is true.  

Two more rules we will use regularly in subsequent proofs are the so-called transitivity. of implication and the transitivity of equivalence (we will encounter equivalence again in the context of relations in Sec. 1.3 below). In preparation for the transitivity rules, we generalize implication to propositional formulas:.  

Definition 1.13. In generalization of the implication operator defined in (1.2), we say the propositional formula $\phi(A_{1},\ldots,A_{n})$ implies the propositional formula $\psi(A_{1},\dots,A_{n})$ (denoted $\phi(A_{1},\ldots,A_{n})\Rightarrow\psi(A_{1},\ldots,A_{n}))$ if, and only if, each assignment of truth values. to the. $A_{1},\ldots,A_{n}$ that makes. $\phi(A_{1},\ldots,A_{n})$ true, makes $\psi(A_{1},\dots,A_{n})$ true as well..  

Theorem 1.14. (a) Transitivity of Implication: $(A\Rightarrow B)\land(B\Rightarrow C)\Rightarrow(A\Rightarrow C)$  

(b) Transitivity of Equivalence: $(A\Leftrightarrow B)\land(B\Leftrightarrow C)\Rightarrow(A\Leftrightarrow C)$  

Proof. According to Def. 1.13, the rules can be verified by providing truth tables that show that, for all possible assignments of truth values to the propositional formulas on the left-hand side of the implications, either the left-hand side is false or both sides are true. (a):  

<html><body><table><tr><td>A</td><td>B</td><td>C</td><td></td><td>A=B</td><td>B=C</td><td>[(A=B)>(B→C)</td><td></td><td>A>C</td></tr><tr><td>T</td><td>T</td><td>T</td><td></td><td>T</td><td>T</td><td></td><td>T</td><td>T</td></tr><tr><td>T</td><td>F</td><td>T</td><td></td><td>F</td><td>T</td><td>F</td><td></td><td>T</td></tr><tr><td>F</td><td>T</td><td>T</td><td></td><td>T</td><td>T</td><td>T</td><td></td><td>T</td></tr><tr><td>F</td><td>F</td><td>T</td><td></td><td>T</td><td>T</td><td></td><td>T</td><td>T</td></tr><tr><td>T</td><td>T</td><td>F</td><td></td><td>T</td><td>F</td><td></td><td>F</td><td>F</td></tr><tr><td>T</td><td>F</td><td>F</td><td></td><td>F</td><td>T</td><td>F</td><td></td><td>F</td></tr><tr><td>F</td><td>T</td><td>F</td><td></td><td>T</td><td>F</td><td></td><td>F</td><td>T</td></tr><tr><td>F</td><td>F</td><td>F</td><td></td><td>T</td><td>T</td><td></td><td>T</td><td>T</td></tr></table></body></html>  

b)  

<html><body><table><tr><td>A</td><td>B</td><td>C</td><td>A☆ B</td><td>BC</td><td>(AB)^(BC)</td><td></td><td>A☆ >C</td></tr><tr><td>T</td><td>T</td><td>T</td><td>T</td><td></td><td>T</td><td>T</td><td>T</td></tr><tr><td>T</td><td>F</td><td>T</td><td>F</td><td></td><td>F</td><td>F</td><td>T</td></tr><tr><td>F</td><td>T</td><td>T</td><td>F</td><td></td><td>T</td><td>F</td><td>F</td></tr><tr><td>F</td><td>F</td><td>T</td><td>T</td><td></td><td>F</td><td>F</td><td>F</td></tr><tr><td>T</td><td>T</td><td>F</td><td>T</td><td></td><td>F</td><td>F</td><td>F</td></tr><tr><td>T</td><td>F</td><td>F</td><td>F</td><td></td><td>T</td><td>F</td><td>F</td></tr><tr><td>F</td><td>T</td><td>F</td><td>F</td><td></td><td>F</td><td>F</td><td>T</td></tr><tr><td>F</td><td>F</td><td>F</td><td>T</td><td></td><td>T</td><td>T</td><td>T</td></tr></table></body></html>  

Having checked both rules, the proof is complete.  

Definition and Remark 1.15. A proof of the statement $B$ is a finite sequence of. statements $A_{1},A_{2},\ldots,A_{n}$ such that $A_{1}$ is true; for. $1\leq i<n$ $A_{i}$ implies $A_{i+1}$ , and $A_{n}$ implies $B$ . If there exists a proof for. $B$ , then Th. 1.14(a) guarantees that $B$ is truel.  

Remark 1.16. Principle of Duality: In Th. 1.11, there are several pairs of rules that have an analogous form: (c) and (d), (e) and (f), (g) and (h), (i) and (j). These analogies are due to the general law called the principle of duality: If $\phi(A_{1},\ldots,A_{n})\Rightarrow$ $\psi(A_{1},\dots,A_{n})$ and only the operators $\Lambda,\vee,\lnot$ occur in $\phi$ and $\psi$ , then the reverse implication $\Phi(A_{1},\ldots,A_{n})\Leftarrow\Psi(A_{1},\ldots,A_{n})$ holds, where one obtains $\Phi$ from $\phi$ and $\Psi$ from $\psi$ by replacing each. $\wedge$ with $\vee$ and each V with. $\wedge$ . In particular, if, instead of an implication, we start with an equivalence (as in the examples from Th. 1.11), then we obtain another equivalence.  

### 1.3 Set Theory  

In the previous section, we have had a first glance at statements and corresponding truth values. In the present section, we will move our focus to the objects such statements are about. Reviewing Example 1.1(a), and recalling that this is a mathematics class rather than one in zoology, the first two statements of Example 1.1(a) are less relevant for us than statements 3-6. As in these examples, we will nearly always be interested in statements involving numbers or collections of numbers or collections of such collections etc.  

In modern mathematics, the term one usually uses instead of "collection" is "set'. In 1895, Georg Cantor defined a set as "any collection into a whole $M$ of definite and. separate objects $m$ of our intuition or our thought". The objects $m$ are called the elements of the set. $M$ . As explained in Appendix A, without restrictions and refinements, Cantor's set theory is not free of contradictions and, thus, not viable to be used in the foundation of mathematics. Axiomatic set theory provides these necessary restrictions and refinements and an introductory treatment can also be found in Appendix A. However, it is possible to follow and understand the rest of this class, without having studied Appendix A.  

Notation 1.17. We write $m\in M$ for the statement " $m$ is an element of the set $M^{\gamma}$  

Definition 1.18. The sets $M$ and $N$ are equal, denoted $M=N$ , if, and only if, $M$ and $N$ have precisely the same elements.  

Definition 1.18 means we know everything about a set $M$ if, and only if, we know all its.   
elements.  

Definition 1.19. The set with no elements is called the empty set; it is denoted by the symbol $\varnothing$  

Example 1.20. For finite sets, we can simply write down all its elements, for example $A:=\{0\}$ $B:=\{0,17.5\}$ $C:=\{5,1,5,3\}$ $D:=\{3,5,1\}$ $E:=\{2,{\sqrt{2}},-2\}$ , where the symbolism ":=" is to be read as "is defined to be equal to".  

Note $C=D$ , since both sets contain precisely the same elements. In particular, the. order in which the elements are written down plays no role and a set does not change if an element is written down more than once..  

If a set has many elements, instead of writing down all its elements, one might use abbreviations such as $F:=\{-4,-2,\ldots,20,22,24\}$ , where one has to make sure the. meaning of the dots is clear from the context..  

Definition 1.21. The set $A$ is called a subset of the set $B$ (denoted $A\subseteq B$ and also referred to as the inclusion of. $A$ in $B$ ) if, and only if, every element of. $A$ is also an element of $B$ (one sometimes also calls $B$ a superset of. $A$ and writes. $B\supseteq A$ ). Please note that $A=B$ is allowed in the above definition of a subset. If $A\subseteq B$ and $A\neq B$ then $A$ is called a strict subset of $B$ , denoted $A\subsetneq B$  

If $B$ is a set and $P(x)$ is a statement about an element $x$ of $B$ (i.e., for each $x\in B$ $P(x)$ is either true or false), then we can define a subset $A$ of $B$ by writing  

$$
A:=\{x\in B:P(x)\}.
$$  

This notation is supposed to mean that the set. $A$ consists precisely of those elements of.   
$B$ such that $P(x)$ is true (has the truth value T in the language of Sec. 1.2).  

Example 1.22. (a) For each set $A$ , one has. $A\subseteq A$ and $\emptyset\subseteq A$ (b) If $A\subseteq B$ , then $A=\{x\in B:x\in A\}$  

(c) We have $\{3\}\subseteq\{6.7,3,0\}$ . Letting $A:=\{-10,-8,\ldots,8,10\}$ , we have $\{-2,0,2\}=$ $\{x\in A:x^{3}\in A\}$ $\varnothing=\{x\in A:x+21\in A\}$  

Remark 1.23. As a consequence of Def. 1.18, the sets. $A$ and $B$ are equal if, and only if, one has both inclusions, namely $A\subseteq B$ and $B\subseteq A$ . Thus, when proving the equality of sets, one often divides the proof into two parts, first proving one inclusion, then the other.  

Definition 1.24. (a) The intersection of the sets $A$ and $B$ , denoted $A\cap B$ , consists of all elements that are in. $A$ and in $B$ . The sets $A,B$ are said to be disjoint if, and. only if, $A\cap B=\emptyset$  

(b) The union of the sets. $A$ and $B$ , denoted $A\cup B$ , consists of all elements that are in $A$ or in $B$ (as in the logical disjunction in (1.2), the or is meant nonexclusively). If $A$ and $B$ are disjoint, one sometimes writes. $A\dot{\cup}B$ and speaks of the disjoint union. of $A$ and $B$  

(c) The difference of the sets $A$ and $B$ , denoted $A\backslash B$ (read " $A$ minus $B^{\mathfrak{N}}$ or " $A$ without $B^{\mathfrak{N}}$ ), consists of all elements of $A$ that are not elements of $B$ , i.e. $A\setminus B:=\{x\in$ $A:x\notin B\}$ . If $B$ is a subset of a given set $A$ (sometimes called the universe in this context), then $A\backslash B$ is also called the complement of $B$ with respect to $A$ In that case, one also writes $B^{\mathrm{c}}:=A\setminus B$ (note that this notation suppresses the dependence on $A$  

Example 1.25. (a) Examples of Intersections:  

$$
\begin{array}{r}{\{1,2,3\}\cap\{3,4,5\}=\{3\},}\ {\{\sqrt{2}\}\cap\{1,2,\ldots,10\}=\emptyset,}\ {\{-1,2,-3,4,5\}\cap\{-10,-9,\ldots,-1\}\cap\{-1,7,-3\}=\{-1,-3\}.}\end{array}
$$  

(b) Examples of Unions:  

$$
\begin{array}{c}{{\{1,2,3\}\cup\{3,4,5\}=\{1,2,3,4,5\},}}\ {{\{1,2,3\}\cup\{4,5\}=\{1,2,3,4,5\},}}\ {{\{-1,2,-3,4,5\}\cup\{-99,-98,\ldots,-1\}\cup\{-1,7,-3\}}}\ {{=\{-99,-98,\ldots,-2,-1,2,4,5,7\}.}}\end{array}
$$  

(c) Examples of Differences:  

$$
\begin{array}{l}{{\{1,2,3\}\setminus\{3,4,5\}=\{1,2\},}}\ {{\{1,2,3\}\setminus\{3,2,1,\sqrt{5}\}=\emptyset,}}\ {{\{-10,-9,\ldots,9,10\}\setminus\{0\}=\{-10,-9,\ldots,-1\}\cup\{1,2,\ldots,9,10\}.}}\end{array}
$$  

With respect to the universe $\{1,2,3,4,5\}$ , it is  

$$
\{1,2,3\}^{\mathrm{c}}=\{4,5\};
$$  

with respect to the universe $\{0,1,\ldots,20\}$ , it is  

$$
\{1,2,3\}^{\mathrm{c}}=\{0\}\cup\{4,5,\ldots,20\}.
$$  

As mentioned earlier, it will often be unavoidable to consider sets of sets. Here are first examples: $\{\varnothing,\{0\},\{0,1\}\}$ $\{\{0,1\},\{1,2\}\}$  

Definition 1.26. Given a set. $A$ , the set of all subsets of $A$ is called the power set of $A$ denoted $\mathcal{P}(A)$ (for reasons explained later (cf. Prop. 2.18), the power set is sometimes also denoted as $2^{A}$  

Example 1.27. Examples of Power Sets:  

$$
\begin{array}{r l r}&{}&{\mathcal{P}(\emptyset)=\{\emptyset\},}\ &{}&{\mathcal{P}(\{0\})=\{\emptyset,\{0\}\},}\ &{}&{\mathcal{P}\big(\mathcal{P}(\{0\})\big)=\mathcal{P}\big(\{\emptyset,\{0\}\}\big)=\big\{\emptyset,\{\emptyset\},\{\{0\}\},\mathcal{P}(\{0\})\big\}.}\end{array}
$$  

So far, we have restricted our set-theoretic examples to finite sets. However, not surprisingly, many sets of interest to us will be infinite (we will have to postpone a mathematically precise definition of finite and infinite to Sec. 3.2). We will now introduce the most simple infinite set.  

Definition 1.28. The set $\mathbb{N}:=\{1,2,3,\dots\}$ is called the set of natural numbers (for a more rigorous construction of N, based on the axioms of axiomatic set theory, see Sec. A.3.4 of the Appendix, where Th. A.46 shows N to be, indeed, infinite). Moreover, we define $\ensuremath{\mathbb{N}}_{0}:=\{0\}\cup\ensuremath{\mathbb{N}}$  

The following theorem compiles important set-theoretic rules:  

Theorem 1.29. Let $A,B,C,U$ be sets.  

(a) Commutativity of Intersections: $A\cap B=B\cap A$ (b) Commutativity of Unions: $A\cup B=B\cup A$ (c) Associativity of Intersections: $(A\cap B)\cap C=A\cap(B\cap C)$ (d) Associativity of Unions: $(A\cup B)\cup C=A\cup(B\cup C)$ (e) Distributivity I: $A\cap(B\cup C)=(A\cap B)\cup(A\cap C)$ (f) Distributivity II: $A\cup(B\cap C)=(A\cup B)\cap(A\cup C)$ (g) De Morgan's Law I: $U\setminus(A\cap B)=(U\setminus A)\cup(U\setminus B).$  

(h) De Morgan's Law II: $U\setminus(A\cup B)=(U\setminus A)\cap(U\setminus B)$ (i) Double Complement: If $A\subseteq U$ , then $U\setminus(U\setminus A)=A$  

Proof. In each case, the proof results from the corresponding rule of Th. 1.11: (a):  

$$
x\in A\cap B\Leftrightarrow x\in A\land x\in B{\overset{\mathrm{Th.1.11}(\mathrm{c})}{\Longleftrightarrow}}x\in B\land x\in A\Leftrightarrow x\in B\cap A.
$$  

(g): Under the general assumption of $x\in U$ , we have the following equivalences:  

$$
{\begin{array}{r l}&{\mathbf{\int}_{\mathbf{\theta}}(A\cap B)\Leftrightarrow\neg(x\in A\cap B)\Leftrightarrow\neg\left(x\in A\land x\in B\right)\land\bigoplus_{\mathbf{\alpha}\iff\mathbf{\alpha}}(x\in A)\lor\neg(x\in B)}\ &{U\setminus A\lor x\in U\setminus B\Leftrightarrow x\in(U\setminus A)\cup(U\setminus B).}\end{array}}
$$  

The proofs of the remaining rules are left as an exercise.  

Remark 1.30. The correspondence between Th. 1.11 and Th. 1.29 is no coincidence. One can actually prove that, starting with an equivalence of propositional formulas $\phi(A_{1},\dots,A_{n})\Leftrightarrow\psi(A_{1},\dots,A_{n})$ , where both formulas contain only the operators $\Lambda,\vee,\lnot$ one obtains a set-theoretic rule (stating an equality of sets) by reinterpreting all statement variables $A_{1},\ldots,A_{n}$ as variables for sets, all subsets of a universe. $U$ , and replacing. $\wedge$ by $\left(~\right)$ $\vee$ by $\cup$ , and $\neg$ by $U\backslash$ (if there are no multiple negations, then we do not need. the hypothesis that. $A_{1},\ldots,A_{n}$ are subsets of. $U$ ). The procedure also works in the opposite direction  one can start with a set-theoretic formula for an equality of sets and translate it into two equivalent propositional formulas..  

### 1.4 Predicate Calculus  

Now that we have introduced sets in the previous section, we have to return to the subject of mathematical logic once more. As it turns out, propositional calculus, which. we discussed in Sec. 1.2, does not quite suffice to develop the theory of calculus (nor most other mathematical theories). The reason is that we need to consider statements such as  

$x+1>0$ holds for each natural number $x$ .(T) (1.11a) All real numbers are positive. (F) (1.11b) There exists a natural number bigger than 10. (T) (1.11c) There exists a real number. $x$ such that $x^{2}=-1$ . (F) (1.11d) For all natural numbers. $n$ , there exists a natural number bigger than $n$ . (T) (1.11e)  

That means we are interested in statements involving universal quantification via the quantifier "for all' (one also often uses "for each" or "for every" instead), existential quantification via the quantifier "there exists', or both. The quantifier of universal quantification is denoted by. $\forall$ and the quantifier of existential quantification is denoted by $\exists$ .Using these symbols as well as. $\mathbb{N}$ and $\mathbb{R}$ to denote the sets of natural and real numbers, respectively, we can restate (1.11) as  

$$
\begin{array}{r l}&{\underset{x\in\mathbb{R}}{\forall}x+1>0.(\Gamma)}\ &{\underset{x\in\mathbb{R}}{\forall}x>0.(\mathrm{F})}\ &{\underset{x\in\mathbb{R}}{\forall}x>0.(\mathrm{F})}\ &{\underset{n\in\mathbb{R}}{\exists}n>10.(\mathrm{T})}\ &{\underset{x\in\mathbb{R}}{\exists}x^{2}=-1.(\mathrm{F})}\ &{\underset{n\in\mathbb{N}}{\forall}\underset{m\in\mathbb{N}}{\bigcup}m>n.(\mathrm{T}}\end{array}
$$  

Definition 1.31. A universal statement has the form  

$$
\forall_{x\in A}P(x),
$$  

whereas an existential statement has the form  

$$
\underset{x\in A}{\exists}P(x).
$$  

In (1.13), $A$ denotes a set and $P(x)$ is a sentence involving the variable $x$ , a so-called predicate of $x$ , that becomes a statement (i.e. becomes either true or false) if $x$ is substituted with any concrete element of the set $A$ (in particular, $P(x)$ is allowed to contain further quantifiers, but it must not contain any other quantifier involving $x$ one says $x$ must be a free variable in $P(x)$ , not bound by any quantifier in $P(x)$ :  

The universal statement (1.13a) has the truth value T if, and only if, $P(x)$ has the truth value T for all elements $x\in A$ ; the existential statement (1.13b) has the truth value T if, and only if, $P(x)$ has the truth value T for at least one element $x\in A$  

Remark 1.32. Some people prefer to write $\Lambda$ instead of $\forall$ and V instead of 3.. $x\in A$ $x\in A$ $x\in A$ $x\in A$ Even though this notation has the advantage of emphasizing that the universal statement can be interpreted as a big logical conjunction and the existential statement can be interpreted as a big logical disjunction, it is significantly less common. So we will stick to $\forall$ and $\exists$ in this class.  

Remark 1.33. According to Def. 1.31, the existential statement (1.13b) is true if, and only if, $P(x)$ is true for at least one. $x\in A$ .So if there is precisely one such. $x$ , then (1.13b) is true; and if there are several different. $x\in A$ such thate $P(x)$ is true, then (1.13b) is still true. Uniqueness statements are often of particular importance, and one sometimes writes  

$$
\exists!P(x)
$$  

for the statement "there exists a unique $x\in A$ such that $P(x)$ is true'. This notation can be defined as an abbreviation for  

$$
\underset{x\in A}{\exists}\left(P(x)\wedge\underset{y\in A}{\forall}\big(P(y)\Rightarrow x=y\big)\right).
$$  

Example 1.34. Here are some examples of uniqueness statements:  

$$
\begin{array}{r l}&{\underset{n\in\mathbb{N}}{\exists!}n>10.(\mathrm{F})}\ &{\underset{n\in\mathbb{N}}{\exists!}12>n>10.(\mathrm{T})}\ &{\underset{n\in\mathbb{N}}{\exists!}11>n>10.(\mathrm{F})}\ &{\underset{n\in\mathbb{N}}{\exists!}x^{2}=-1.(\mathrm{F})}\ &{\underset{x\in\mathbb{N}}{\exists!}x^{2}=1.(\mathrm{F})}\ &{\underset{x\in\mathbb{N}}{\exists!}x^{2}=0.(\mathrm{T})}\end{array}
$$  

Remark 1.35. As for propositional calculus, we also have some important rules for predicate calculus:  

(a) Consider the negation of a universal statement, $\lnot\forall_{x\in A}P(x)$ , which is true if, and only if, $P(x)$ does not hold for each. $x\in A$ , i.e. if, and only if, there exists at least. one $x\in A$ such that $P(x)$ is false (such that $\neg P(x)$ is true). We have just proved. the rule  

$$
\lnot\forall_{x\in A}P(x)\Leftrightarrow\exists_{x\in A}\neg P(x).
$$  

Similarly, consider the negation of an existential statement. We claim the corresponding rule is  

$$
\lnot\exists_{x\in A}P(x)\Leftrightarrow\forall_{x\in A}\lnot P(x).
$$  

Indeed, we can prove (1.17b) from (1.17a):  

$$
\lnot\lnot\exists_{x\in A}P(x)\overset{\mathrm{\tiny~Th.1.11(k)}}{\iff}\lnot\exists\lnot\lnot P(x)\overset{\mathrm{\tiny~(1.17a)}}{\iff}\lnot\lnot\lnot P(x)\overset{\mathrm{\tiny~Th.1.1(k)}}{\iff}\lnot\lnot P(x)\overset{\mathrm{\tiny~Th.1.1(k)}}{\iff}\lnot\lnot P(x)
$$  

One can interpret (1.17) as a generalization of the De Morgan's laws Th. 1.11(i),(j).  

One can actually generalize (1.17) even a bit more: If a statement starts with several quantifiers, then one negates the statement by replacing each V with $\exists$ and vice versa plus negating the predicate after the quantifiers (see the example in (1.21e) below).  

(b) If $A,B$ are sets and $P(x,y)$ denotes a predicate of both. $x$ and $y$ , then $\underset{x\in A}{\forall}\forall\underset{y\in B}{}P(x,y)$ and YR Y4 P(x,y) both hold true if, and only if, $P(x,y)$ holds true for each. $x\in A$ and each $y\in B$ , i.e. the order of two consecutive universal quantifiers does not matter:  

$$
\forall_{x\in A}\forall_{y\in B}P(x,y)\Leftrightarrow\forall_{y\in B}\forall_{x\in A}P(x,y)
$$  

In the same way, we obtain the following rule:  

$$
\exists_{x\in A}{\exists}_{y\in B}P(x,y)\Leftrightarrow\exists_{y\in B}{\underset{x\in A}{\exists}}P(x,y).
$$  

If $A=B$ , one also uses abbreviations of the form  

$$
\begin{array}{r l r}{\underset{x,y\in A}{\forall}P(x,y)}&{{}\mathrm{for}}&{\underset{x\in A}{\forall}\underset{y\in A}{\forall}P(x,y),}\ {\underset{x,y\in A}{\exists}P(x,y)}&{{}\mathrm{for}}&{\underset{x\in A}{\exists}\underset{y\in A}{\exists}P(x,y).}\end{array}
$$  

Generalizing rules (1.19), we can always commute identical quantifiers. Caveat: Quantifiers that are not identical must not be commuted (see Ex. 1.36(d) below).  

Example 1.36. (a) Negation of universal and existential statements:  

$$
\begin{array}{l l}{{\mathrm{Negation~of~(1.12a):}}}&{{{\frac{-(x+1.50)}{x+1}}}}\ {{\mathrm{Negation~of~(1.12a):}}}&{{{\frac{-(x-0.0)}{x\in B_{x}}~.}}}\ {{\mathrm{Negation~of~(1.12b):}}}&{{{\frac{-(x-0.0)}{x\in B_{x}}~.}}}\ {{\mathrm{Negation~of~(1.12e):}}}&{{{\mathrm{Ne}}^{-}{\frac{(x-1.1)}{x\in B_{x}}}~.}}\ {{\mathrm{Negation~of~(1.12e):}}}&{{{\mathrm{Ne}}^{-}{\frac{(x-0.1)}{x\in B_{x}}}~.}}\ {{\mathrm{Negation~of~(1.12d):}}}&{{{\frac{-(x-1.1)}{x\in B_{x}}}~.}}\ {{\mathrm{Negation~of~(1.12e):}}}&{{{\frac{-(x-1.1)}{x\in B_{x}}}~.}}\end{array}
$$  

(b) As a more complicated example, consider the negation of the uniqueness statement (1.14), i.e. of (1.15):  

$$
\begin{array}{r l}{\gamma_{x\in A}^{\supset1}P(x)}&{\Leftrightarrow\quad\to\frac{\breve{\gamma}}{x\in A}\left(P(x)\wedge\underset{y\in A}{\overset{\vee}{\cup}}\left(P(y)\Rightarrow x=y\right)\right)}\ &{(1.17b),\underset{y\in A}{\overset{\wedge}{\cup}},1.11(a)}&{\underset{x\in A}{\overset{\vee}{\cup}}-\left(P(x)\wedge\underset{y\in A}{\overset{\vee}{\cup}}\left(-P(y)\vee x=y\right)\right)}\ &{\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\mathrm{Th}\underset{x\in A}{\overset{\scriptscriptstyle{\mathrm{II}}}{\prod}}(1)}&{\underset{x\in A}{\overset{\vee}{\cup}}\left(-P(x)\vee\underset{y\in A}{\overset{\vee}{\cup}}\left(-P(y)\vee x=y\right)\right)}\ &{(1.17a)}&{\underset{x\in A}{\overset{\vee}{\cup}}\left(-P(x)\vee\underset{y\in A}{\overset{\vee}{\cup}}-\left(-P(y)\vee x=y\right)\right)}\ &{\quad\quad\quad\quad\quad\quad\quad\quad\quad\mathrm{Th},\underset{x\in A}{\overset{\scriptscriptstyle{\mathrm{II}}}{\prod}}(0),(1.11(a))}&{\underset{x\in A}{\overset{\vee}{\cup}}\left(-P(x)\vee\underset{y\in A}{\overset{\rightarrow}{\cup}}\left(P(y)\wedge x\neq y\right)\right)}\ &{\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\mathrm{Th}\underset{x\in A}{\overset{\scriptscriptstyle{\mathrm{II}}}{\prod}}(0)}&{\underset{x\in A}{\overset{\vee}{\cup}}\left(P(x)\Rightarrow\underset{y\in A}{\overset{\scriptscriptstyle{\mathrm{II}}}{\prod}}(P(y)\wedge x\neq y)\right).}\end{array}
$$  

So how to decode the expression, we have obtained at the end? It states that if $P(x)$ holds for some $x\in A$ , then there must be at least a second, different, element $y\in A$ such that $P(y)$ is true. This is, indeed, precisely the negation of $\exists_{\cdot}^{!}P(x)$  

(c) Identical quantifiers commute:  

$$
\begin{array}{r l}&{\underset{x\in\mathbb{R}}{\forall}~\forall~x^{2n}\geq0\iff\underset{n\in\mathbb{N}}{\forall}~\forall~x^{2n}\geq0,}\ &{\underset{x\in\mathbb{R}}{\forall}~\underset{y\in\mathbb{R}}{\exists}~\underset{n\in\mathbb{N}}{\exists}~n y>x^{2}\iff\underset{x\in\mathbb{R}}{\forall}~\underset{n\in\mathbb{N}}{\exists}~\underset{y\in\mathbb{R}}{\exists}~n y>x^{2}.}\end{array}
$$  

(d) The following example shows that different quantifiers do, in general, not commute (i.e. do not yield equivalent statements when commuted): While the statement  

$$
\forall\exists\operatorname{\Pi}_{x\in\mathbb{R}}x\in\mathbb{R}\operatorname{\Pi}_{y\in\mathbb{R}}y>x
$$  

is true (for each real number. $x$ , there is a bigger real number. $y$ , e.g. $y:=x+1$ will do the job), the statement  

$$
\exists\quad\forall\quad y>x
$$  

is false (for example, since. $y>y$ is false). In particular, (1.24a) and (1.24b) are not equivalent.  

(e) Even though (1.14) provides useful notation, it is better not to think of. $\exists$ ! as a quantifier. It is really just an abbreviation for (1.15), and it behaves very differently from $\exists$ and $\forall$ : The following examples show that, in general,. $\exists!$ commutes neither with $\exists$ , nor with itself:  

$$
\exists_{n\in\mathbb{N}}\exists_{m\in\mathbb{N}}^{!}m<n\not\Leftrightarrow\exists_{m\in\mathbb{N}}^{!}\exists_{n\in\mathbb{N}}m<n
$$  

(the statement on the left is true, as one can choose $n=2$ , but the statement on the right is false, as $\exists_{n\in\mathbb{N}}m<n$ holds for every $m\in\mathbb{N}$ ). Similarly,  

$$
\exists_{n\in\mathbb{N}}^{!}\exists_{m\in\mathbb{N}}^{!}m<n\not\Leftrightarrow\exists_{m\in\mathbb{N}}^{!}\exists_{n\in\mathbb{N}}^{!}m<n
$$  

(the statement on the left is still true and the statement on the right is still false (there is no $m\in\mathbb{N}$ such that $\exists!\operatorname{m}<n)$  

Remark 1.37. One can make the following observations regarding the strategy for proving universal and existential statements:.  

(a) To prove that $\forall_{x\in A}P(x)$ is true, one must check the truth of $P(x)$ for every element $x\in A$ examples are not enough!  

(b) To prove that $\forall_{x\in A}P(x)$ is false, it suffices to find one $x\in A$ such that. $P(x)$ is false - such an $x$ is then called a counterexample and one counterexample is always enough to prove $\underset{x\in A}{\forall}P(x)$ is false!.  

(c) To prove that $\exists_{x\in A}P(x)$ is true, it suffices to find one. $x\in A$ such that. $P(x)$ is true - such an $x$ is then called an example and one example is always enough to prove $\exists_{x\in A}P(x)$ is true!.  

The subfield of mathematical logic dealing with quantified statements is called predicate calculus. In general, one does not restrict the quantified variables to range only over elements of sets (as we have done above). Again, we refer to [EFT07] for a deeper treatment of the subject.  

As an application of quantified statements, let us generalize the notion of union and intersection:  

Definition 1.38. Let. $I\neq\emptyset$ be a nonempty set, usually called an index set in the present context. For each. $i\in I$ , let $A_{i}$ denote a set (some or all of the. $A_{i}$ can be identical).  

(a) The intersection  

$$
\bigcap_{i\in I}A_{i}:=\left\{x:\forall_{i\in I}x\in A_{i}\right\}
$$  

consists of all elements $x$ that belong to every $A_{i}$  

(b) The union  

$$
\bigcup_{i\in I}A_{i}:=\left\{x:\exists_{i\in I}x\in A_{i}\right\}
$$  

consists of all elements. $x$ that belong to at least one $A_{i}$ . The union is called disjoint if, and only if, for each. $i,j\in I$ $i\neq j$ implies $A_{i}\cap A_{j}=\emptyset$  

Proposition 1.39. Let. $I\neq\emptyset$ be an index set, let. $M$ denote a set, and, for each. $i\in I$ let $A_{i}$ denote a set. The following set-theoretic rules hold:  

$$
\left(\bigcap_{i\in I}A_{i}\right)\cap M=\bigcap_{i\in I}(A_{i}\cap M).
$$  

$$
{\biggl(}\bigcup A_{i}{\biggr)}\cup M=\bigcup_{i\in I}(A_{i}\cup M).
$$  

$$
{\biggl(}\bigcap_{i\in I}A_{i}{\biggr)}\cup M=\bigcap_{i\in I}(A_{i}\cup M).
$$  

$$
\left(\bigcup_{i\in I}A_{i}\right)\cap M=\bigcup_{i\in I}(A_{i}\cap M).
$$  

Proof. We prove (c) and (e) and leave the remaining proofs as an exercise.  

(c):  

$$
\begin{array}{r l}&{x\in\left(\displaystyle\bigcap_{i\in I}A_{i}\right)\cup M\iff x\in M\vee\vee_{i\in I}x\in A_{i}\overset{(*)}{\circledast}\underbrace{\forall}_{i\in I}\left(x\in A_{i}\vee x\in M\right)}\ &{\qquad\Leftrightarrow x\in\displaystyle\bigcap_{i\in I}(A_{i}\cup M).}\end{array}
$$  

To justify the equivalence at $(*)$ , we make use of Th. 1.11(b) and verify $\Rightarrow$ and $\Leftarrow$ . For $\Rightarrow$ note that the truth of $x\in M$ implies $x\in A_{i}\lor x\in M$ is true for each $i\in I$ . If $x\in A_{i}$ is true for each $i\in I$ , then $x\in A_{i}\lor x\in M$ is still true for each $i\in I$ . To verify $\Leftarrow$ , note that the existence of $i\in I$ such that $x\in M$ implies the truth of $x\in M\lor\forall_{i\in I}x\in A_{i}$ $i\in I$ If $x\in M$ is false for each $i\in I$ , then $x\in A_{i}$ must be true for each $i\in I$ , showing $x\in M\vee_{i\in I}\forall_{}x\in A_{i}$ is true also in this case.  

e  

$$
\begin{array}{c}{{x\in M\setminus\bigcap_{i\in I}A_{i}\Leftrightarrow x\in M\land\neg\bigforall\downarrow~x\in A_{i}~\Leftrightarrow x\in M\land\exists~x\not\in A_{i}}}\ {{\qquad\Leftrightarrow\bigcup_{i\in I}x\in M\setminus A_{i}~\Leftrightarrow x\in\bigcup_{i\in I}(M\setminus A_{i}),}}\end{array}
$$  

completing the proof.  

Example 1.40. We have the following identities of sets:  

$$
\begin{array}{c}{{\displaystyle\bigcap_{x\in\mathbb{R}}\mathbb{N}=\mathbb{N},}}\ {{\displaystyle\bigcap_{n\in\mathbb{N}}\{1,2,\ldots,n\}=\{1\},}}\ {{\displaystyle n\mathrm{erit}~\ldots~\cup}}\ {{\displaystyle\bigcup_{x\in\mathbb{R}}\mathbb{N}=\mathbb{N},}}\ {{\displaystyle\bigcup_{x\in\mathbb{R}}\mathbb{N}=\mathbb{N},}}\ {{\displaystyle\bigcup_{n\in\mathbb{N}}\{1,2,\ldots,n\}=\mathbb{N},}}\ {{\displaystyle\mathbb{N}\setminus\bigcup_{n\in\mathbb{N}}\{2n\}=\{1,3,5,\ldots\}=\bigcap_{n\in\mathbb{N}}\left(\mathbb{N}\setminus\{2n\}\right);}}\end{array}
$$  

Comparing with the notation of Def. 1.38, in (1.26a), for example, we have $I=\mathbb{R}$ and $A_{i}=\mathbb{N}$ for each $i\in I$ (where, in (1.26a), we have written. $x$ instead of $\imath$ ). Similarly, in (1.26b), we have $I=\mathbb{N}$ and $A_{n}=\{1,2,\dots,n\}$ for each $n\in{\cal I}$  

## 2 Functions and Relations  

### 2.1 Functions  

Definition 2.1. Let $A,B$ be sets. Given $x\in A$ $y\in B$ , the set  

$$
(x,y):={\Big\{}\{x\},\{x,y\}{\Big\}}
$$  

is called the ordered pair (often shortened to just pair) consisting of $x$ and $y$ . The set of all such pairs is called the Cartesian product. $A\times B$ , i.e.  

$$
A\times B:=\{(x,y):x\in A\land y\in B\}.
$$  

Example 2.2. Let $A$ be a set.  

$$
\begin{array}{c}{A\times\varnothing=\varnothing\times A=\varnothing,}\ {\{1,2\}\times\{1,2,3\}=\{(1,1),(1,2),(1,3),(2,1),(2,2),(2,3)\}}\ {\neq\{1,2,3\}\times\{1,2\}=\{(1,1),(1,2),(2,1),(2,2),(3,1),(3,2)\}.}\end{array}
$$  

Also note that, for $x\neq y$  

$$
(x,y)=\left\{\{x\},\{x,y\}\right\}\neq\left\{\{y\},\{x,y\}\right\}=(y,x).
$$  

Definition 2.3. Given sets $A,B$ , a function or map. $f$ is an assignment rule that assigns. to each $x\in A$ a unique $y\in B$ . One then also writes. $f(x)$ for the element. $y$ . The set $A$ is called the domain of $f$ , denoted $\operatorname{dom}(f)$ , and $B$ is called the codomain of $f$ , denoted $\operatorname{codom}(f)$ . The information about a map. $f$ can be concisely summarized by the notation  

$$
f:A\longrightarrow B,\quad x\mapsto f(x),
$$  

where $x\mapsto f(x)$ is called the assignment rule for $f$ $f(x)$ is called the image of $x$ , and $x$ is called a preimage of $f(x)$ (the image must be unique, but there might be several preimages). The set  

$$
\mathrm{graph}(f):=\big\{(x,y)\in A\times B:y=f(x)\big\}
$$  

is called the graph of $f$ (not to be confused with pictures visualizing the function $f$ which are also called graph of $f$ ). If one wants to be completely precise, then one. identifies the function $f$ with the ordered triple $(A,B,\operatorname{graph}(f))$  

The set of all functions with domain $A$ and codomain $B$ is denoted by. ${\mathcal{F}}(A,B)$ or $B^{A}$ i.e.  

$$
{\mathcal{F}}(A,B):=B^{A}:=\big\{(f:A\longrightarrow B):A=\operatorname{dom}(f)\wedge B=\operatorname{codom}(f)\big\}.
$$  

Caveat: Some authors reserve the word map for continuous functions, but we use function and map synonymously..  

Definition 2.4. Let $A,B$ be sets and $f:A\longrightarrow B$ a function.  

(a) If $^{\prime}I^{\prime}$ is a subset of $A$ , then  

$$
f(T):=\{f(x)\in B:x\in T\}
$$  

is called the image of $^{\prime}I^{\prime}$ under $f$  

(b) If $U$ is a subset of $B$ , then  

$$
f^{-1}(U):=\{x\in A:f(x)\in U\}
$$  

is called the preimage or inverse image of $U$ under $f$  

(c) $f$ is called injective or one-to-one if, and only if, every. $y\in B$ has at most one preimage, i.e. if, and only if, the preimage of $\{y\}$ has at most one element:  

$$
{\begin{array}{r l}{f{\mathrm{~injective}}\quad}&{\Leftrightarrow\quad\underset{y\in B}{\forall}}\ &{\Leftrightarrow\quad\underset{x_{1},x_{2}\in A}{\forall}\left(f^{-1}\{y\}=\varnothing\vee\underset{x\in A}{\exists!}f(x)=y\right)}\end{array}}
$$  

(d) $f$ is called surjective or onto if, and only if, every element of the codomain of $f$ has a preimage:  

$$
f{\mathrm{~surjective}}\quad\Leftrightarrow\quad\underset{y\in B}{\forall}\underset{x\in A}{\exists}y=f(x)\quad\Leftrightarrow\quad\underset{y\in B}{\forall}f^{-1}\{y\}\neq\emptyset.
$$  

(e) $f$ is called bijective if, and only if, $f$ is injective and surjective.  

Example 2.5. Examples of Functions:  

$$
\begin{array}{r l r l}&{f:\{1,2,3,4,5\}\longrightarrow\{1,2,3,4,5\},}&&{f(x):=-x+6,}\ &{g:\mathbb{N}\longrightarrow\mathbb{N},}&&{g(n):=2n,}\ &{h:\mathbb{N}\longrightarrow\{2,4,6,...\},}&&{h(n):=2n,}\ &{\tilde{h}:\mathbb{N}\longrightarrow\{2,4,6,...\},}&&{\tilde{h}(n):=\left\{\begin{array}{l l}{n}&{\mathrm{for~}n\mathrm{~even},}\ {n+1}&{\mathrm{for~}n\mathrm{~odd},}\end{array}\right.}\ &{G:\mathbb{N}\longrightarrow\mathbb{R},}&&{G(n):=n/(n+1),}\ &{F:\mathcal{P}(\mathbb{N})\longrightarrow\mathcal{P}(\mathcal{P}(\mathbb{N})),}&&{F(A):=\mathcal{P}(A).}\end{array}
$$  

Instead of. $f(x):=-x+6$ in (2.12a), one can also write $x\mapsto-x+6$ and analogously in the other cases. Also note that, in the strict sense, functions $g$ and $h$ are different, since their codomains are different (however, using the following Def. 2.4(a), they have the same image in the sense that $g(\mathbb{N})=h(\mathbb{N})$ ). Furthermore,  

$$
f(\{1,2\})=\{5,4\}=f^{-1}(\{1,2\}),\quad\tilde{h}^{-1}(\{2,4,6\})=\{1,2,3,4,5,6\},
$$  

$f$ is bijective;. $g$ is injective, but not surjective; $h$ is bijective;. $\tilde{h}$ is surjective, but not. injective. Can you figure out if $G$ and $F$ are injective and/or surjective?  

Example 2.6. (a) For each nonempty set. $A$ , the map I. $\mathrm{d}:A\longrightarrow A$ $\operatorname{Id}(x):=x$ , is called the identity on $A$ . If one needs to emphasize that Id operates on $A$ , then one. also writes. $\operatorname{Id}_{A}$ instead of Id. The identity is clearly bijective.  

(b) Let $A,B$ be nonempty sets. A map $f:A\longrightarrow B$ is called constant if, and only if, there exists $c\in B$ such that $f(x)=c$ for each $x\in A$ . In that case, one also writes $f\equiv c$ , which can be read as $^{\circ\circ}f$ is identically equal to $c^{\gamma}$ . If $f\equiv c$ $\varnothing\neq T\subseteq A$ , and $U\subseteq B$ , then  

$$
f(T)=\{c\},\quad f^{-1}(U)={\left\{\begin{array}{l l}{A}&{{\mathrm{for~}}c\in U,}\ {\varnothing}&{{\mathrm{for~}}c\notin U.}\end{array}\right.}
$$  

$f$ is injective if, and only if, $A=\{x\}$ $f$ is surjective if, and only if, $B=\{c\}$  

(c) Given $A\subseteq X$ , the map  

$$
\iota:A\longrightarrow X,\quad\iota(x):=x,
$$  

is called inclusion (also embedding or imbedding). An inclusion is always injective; it is surjective if, and only if $A=X$ , i.e. if, and only if, it is the identity on $A$  

(d) Given $A\subseteq X$ and a map $f:X\longrightarrow B$ , the map $g:A\longrightarrow B$ $g(x)=f(x)$ , is called the restriction of $f$ to $A$ $f$ is called an extension of $g$ to $X$ . In this situation, one also uses the notation $f\upharpoonright A$ for $g$ (some authors prefer the notation $f|_{A}$ or $f|A)$  

Theorem 2.7. Let $f\colon A\to B$ be a map, let $\emptyset\neq I$ be an index set, and assume. $S,T,S_{i}$ $i\in I$ ,are subsets of $A$ ,whereas $U,V,U_{i}$ $i\in I$ , are subsets of $B$ .Then we have the. following rules concerning functions and set-theoretic operations:  

$$
\begin{array}{r l}{f(S\cap T)}&{\subseteq f(S)\cap f(T),}\ {f\left(\bigcap S_{i}\right)}&{\subseteq\bigcap f(S),}\ {f\left(S\cup I\right)}&{=\overbrace{f(S)}^{\neg}|f(S),}\ {f\left(\bigcup S\cup T\right)}&{=\overbrace{f(S)}^{\neg}|f(T),}\ {f\left(\bigcup S_{i}\right)}&{=\underbrace{\bigcup f(S)}_{\u\in I},}\ {f^{-1}(U\cap V)}&{=f^{-1}(U)\cap f^{-1}(V),}\ {f^{-1}\left(\bigcap U_{i}\right)}&{=\bigcap f^{-1}(U),}\ {f^{-1}(U\cup V)}&{=\overbrace{f^{-1}(U)}^{\neg}|f^{-1}(V),}\ {f^{-1}\left(\bigcup U_{i}\right)}&{=\underbrace{f^{-1}(U)}_{\u\in I},}\end{array}
$$  

$$
\begin{array}{r c l}{{f(f^{-1}(U))}}&{{\subseteq}}&{{U,\quad f^{-1}(f(S))\supseteq S,}}\ {{f^{-1}(U\setminus V)}}&{{=}}&{{f^{-1}(U)\setminus f^{-1}(V).}}\end{array}
$$  

Proof. We prove (2.16b) (which includes (2.16a) as a special case) and the second part of (2.16i), and leave the remaining cases as exercises..  

For (2.16b), one argues  

$$
\Xi~f~\left(\bigcap_{i\in I}S_{i}\right)~\Leftrightarrow~\underbrace{\exists}_{x\in A}~\forall_{i\in I}~{\bigl(}x\in S_{i}\land y=f(x){\bigr)}~\Rightarrow~\forall~y\in f(S_{i})~\Leftrightarrow~y\in\bigcap_{i\in I}f(S_{i})
$$  

The observation  

$$
x\in S\Rightarrow f(x)\in f(S)\Leftrightarrow x\in f^{-1}(f(S)).
$$  

establishes the second part of (2.16i).  

It is an exercise to find counterexamples that show one can not, in general, replace the four subset symbols in (2.16) by equalities (it is possible to find examples with sets that. have at most 2 elements).  

Definition 2.8. The composition of maps $f$ and $g$ with $f:A\longrightarrow B$ $g:C\longrightarrow D$ , and $f(A)\subseteq C$ is defined to be the map.  

$$
g\circ f:A\longrightarrow D,\quad(g\circ f)(x):=g{\big(}f(x){\big)}.
$$  

The expression $g\circ f$ is read as $^{\circ\circ}g$ after $f^{\gamma}$ or $^{\circ\circ}g$ composed with $f^{\gamma}$  

Example 2.9. Consider the maps  

$$
\begin{array}{r l}{f:\mathbb{N}\longrightarrow\mathbb{R},\qquad}&{{}n\mapsto n^{2},}\ {g:\mathbb{N}\longrightarrow\mathbb{R},\qquad}&{{}n\mapsto2n.}\end{array}
$$  

We obtain $f(\mathbb{N})=\{1,4,9,\dots\}\subseteq\operatorname{dom}(g)$ $g(\mathbb{N})=\{2,4,6,\dots\}\subseteq\mathrm{dom}(f)$ , and the compositions  

$$
\begin{array}{r l r}&{(g\circ f):\mathbb{N}\longrightarrow\mathbb{R},\qquad}&{(g\circ f)(n)=g(n^{2})=2n^{2},}\ &{(f\circ g):\mathbb{N}\longrightarrow\mathbb{R},\qquad}&{(f\circ g)(n)=f(2n)=4n^{2},}\end{array}
$$  

showing that composing functions is, in general, not commutative, even if the involved functions have the same domain and the same codomain..  

Proposition 2.10. Consider maps $f:A\longrightarrow B$ $g:C\longrightarrow D$ $h:E\longrightarrow F$ , satisfying $f(A)\subseteq C$ and $g(C)\subseteq E$  

(a) Associativity of Compositions:  

$$
h\circ(g\circ f)=(h\circ g)\circ f.
$$  

(b) One has the following law for forming preimages:  

$$
\underset{W\in\mathcal{P}(D)}{\forall}~(g\circ f)^{-1}(W)=f^{-1}(g^{-1}(W)).
$$  

Proof. (a): Both $h\circ(g\circ f)$ and $(h\circ g)\circ f$ map $A$ into $F$ . So it just remains to prove ${\bigl(}h\circ(g\circ f){\bigr)}(x)={\bigl(}(h\circ g)\circ f{\bigr)}(x)$ for each $x\in A$ . One computes, for each $x\in A$  

$$
\begin{array}{r l}&{\big(h\circ(g\circ f)\big)(x)=h\big((g\circ f)(x)\big)=h\big(g(f(x))\big)=(h\circ g)(f(x))}\ &{\qquad=\big((h\circ g)\circ f\big)(x),}\end{array}
$$  

establishing the case.  

(b): Exercise.  

Definition 2.11. A function $g:B\longrightarrow A$ is called a right inverse (resp. left inverse) of a function. $f:A\longrightarrow B$ if, and only if,. $f\circ g=\operatorname{Id}_{B} $ (resp. $g\circ f=\operatorname{Id}_{A}$ ). Moreover, $g$ is called an inverse of $f$ if, and only if, it is both a right and a left inverse. If $g$ is an inverse of $f$ , then one also writes. $f^{-1}$ instead of $g$ . The map $f$ is called (right, left). invertible if, and only if, there exists a (right, left) inverse for $f$  

Example 2.12. (a) Consider the map  

$$
f:\mathbb{N}\longrightarrow\mathbb{N},\quad f(n):=2n.
$$  

The maps  

$$
\begin{array}{r}{g_{1}:\mathbb{N}\longrightarrow\mathbb{N},\quad g_{1}(n):=\left\{\begin{array}{l l}{n/2}&{\mathrm{if~}n\mathrm{~even},}\ {1}&{\mathrm{if~}n\mathrm{~odd},}\end{array}\right.}\ {g_{2}:\mathbb{N}\longrightarrow\mathbb{N},\quad g_{2}(n):=\left\{\begin{array}{l l}{n/2}&{\mathrm{if~}n\mathrm{~even},}\ {2}&{\mathrm{if~}n\mathrm{~odd},}\end{array}\right.}\end{array}
$$  

both constitute left inverses of. $f$ . It follows from Th. 2.13(c) below that $f$ does not have a right inverse..  

(b) Consider the map  

$$
f:\mathbb{N}{\longrightarrow}\mathbb{N},\quad f(n):={\left\{\begin{array}{l l}{n/2}&{{\mathrm{for~}}n{\mathrm{~even}},}\ {(n+1)/2}&{{\mathrm{for~}}n{\mathrm{~odd}}.}\end{array}\right.}
$$  

The maps  

$$
\begin{array}{r l}&{g_{1}:\mathbb{N}\longrightarrow\mathbb{N},\quad g_{1}(n):=2n,}\ &{g_{2}:\mathbb{N}\longrightarrow\mathbb{N},\quad g_{2}(n):=2n-1,}\end{array}
$$  

both constitute right inverses of. $f$ . It follows from Th. 2.13(c) below that $f$ does not have a left inverse..  

(c) The map  

$$
f:\mathbb{N}{\longrightarrow}\mathbb{N},\quad f(n):={\left\{\begin{array}{l l}{n-1}&{{\mathrm{for~}}n{\mathrm{~even}},}\ {n+1}&{{\mathrm{for~}}n{\mathrm{~odd}},}\end{array}\right.}
$$  

is its own inverse, i.e. $f^{-1}=f$ . For the map  

the inverse is  

$$
g:\mathbb{N}\longrightarrow\mathbb{N},\quad g(n):={\left\{\begin{array}{l l}{2}&{{\mathrm{for~}}n=1,}\ {3}&{{\mathrm{for~}}n=2,}\ {1}&{{\mathrm{for~}}n=3,}\ {n}&{{\mathrm{for~}}n\not\in\{1,2,3\},}\end{array}\right.}
$$  

$$
g^{-1}:\mathbb{N}\longrightarrow\mathbb{N},\quad g^{-1}(n):={\left\{\begin{array}{l l}{3}&{{\mathrm{for~}}n=1,}\ {1}&{{\mathrm{for~}}n=2,}\ {2}&{{\mathrm{for~}}n=3,}\ {n}&{{\mathrm{for~}}n\not\in\{1,2,3\}.}\end{array}\right.}
$$  

While Examples 2.12(a),(b) show that left and right inverses are usually not unique, they are unique provided. $f$ is bijective (see Th. 2.13(c)).  

Theorem 2.13. Let $A,B$ be nonempty sets.  

(a) $f:A\longrightarrow B$ is right invertible if, and only if,. $f$ is surjective (where the implication. "" makes use of the axiom of choice (AC), see Appendix A.4).  

(b) $f:A\longrightarrow B$ is left invertible if, and only if, $f$ is injective.  

(c) $f:A\longrightarrow B$ is invertible if, and only if,. $f$ is bijective. In this case, the right inverse. and the left inverse are unique and both identical to the inverse.  

Proof. (a): If $f$ is surjective, then, for each $y\in B$ , there exists $x_{y}\in f^{-1}\{y\}$ such that $f(x_{y})=y$ . By AC, we can define the choice function  

$$
g:B\longrightarrow A,\quad g(y):=x_{y}.
$$  

Then, for each. $y\in B$ $f(g(y))=y$ , showing $g$ is a right inverse of $f$ .Conversely, if. $g:B\longrightarrow A$ is a right inverse of $f$ , then, for each. $y\in B$ , it is $y=f(g(y))$ , showing that $g(y)\in A$ is a preimage of $y$ , i.e. $f$ is surjective.  

(b): Fix $a\in A$ . If $f$ is injective, then, for each $y\in B$ with $f^{-1}\{y\}\ne\emptyset$ , let $x_{y}$ denote the unique element in. $A$ satisfyinge $f(x_{y})=y$ . Define  

$$
g:B\longrightarrow A,\quad g(y):=\left\{{x_{y}\quad\mathrm{for}\:f^{-1}\{y\}\ne\emptyset},\atop{a\quad\mathrm{otherwise}.}\right.
$$  

Then, for each $x\in A$ $g(f(x))=x$ , showing $g$ is a left inverse of $f$ .Conversely, if $g:B\longrightarrow A$ is a left inverse of $f$ and $x_{1},x_{2}\in A$ with $f(x_{1})=f(x_{2})=y$ , then $x_{1}=(g\circ f)(x_{1})=g(f(x_{1}))=g(f(x_{2}))=(g\circ f)(x_{2})=x_{2},$ showing $y$ has precisely one preimage and $f$ is injective.  

The first part of (c) follows immediately by combining (a) and (b) (and, actually, without using AC, since, if $f$ is both injective and surjective, then, for each $y\in B$ , the element $x_{y}\in f^{-1}\{y\}$ is unique, and (2.26) can be defined without AC). It merely remains to verify the uniqueness of right and left inverse for bijective maps. So let $g$ be a left inverse of $f$ , let $h$ be a right inverse of $f$ , and let $f^{-1}$ be an inverse of $f$ . Then, for each $y\in B$  

$$
\begin{array}{r}{g(y)=\big(g\circ(f\circ f^{-1})\big)(y)=\big((g\circ f)\circ f^{-1}\big)(y)=f^{-1}(y),}\ {h(y)=\big((f^{-1}\circ f)\circ h\big)(y)=\big(f^{-1}\circ(f\circ h)\big)(y)=f^{-1}(y),}\end{array}
$$  

thereby proving the uniqueness of left and right inverse for bijective maps.  

Theorem 2.14. Consider maps $f:A\longrightarrow B$ $g:B\longrightarrow C$ . If $f$ and $g$ are both injective. (resp. both surjective, both bijective), then so is $g\circ f$ . Moreover, in the bijective case, one has.  

$$
(g\circ f)^{-1}=f^{-1}\circ g^{-1}.
$$  

Proof. Exercise.  

Definition 2.15. (a) Given an index set $I$ and a set $A$ , a map $f:I\longrightarrow A$ is sometimes called a family (of elements in $A$ ), and is denoted in the form $f~=~(a_{i})_{i\in{I}}$ with $a_{i}:=f(i)$ . When using this representation, one often does not even specify $f$ and $A$ , especially if the $a_{i}$ are themselves sets.  

(b) A sequence in a set $A$ is a family of elements in $A$ , where the index set is the set of natural numbers N. In this case, one writes $(a_{n})_{n\in\mathbb{N}}$ or $(a_{1},a_{2},\ldots)$ . More generally, a family is called a sequence, given a bijective map between the index set $I$ and a subset of $\mathbb{N}$  

(c) Given a family of sets $(A_{i})_{i\in I}$ , we define the Cartesian product of the $A_{i}$ to be the set of functions  

$$
\prod_{i\in I}A_{i}:=\left\{\left(f:I\longrightarrow\bigcup_{j\in I}A_{j}\right):\forall_{i\in I}f(i)\in A_{i}\right\}.
$$  

If $I$ has precisely $n$ elements with $n\in\mathbb N$ , then the elements of the Cartesian product $\textstyle{\prod_{i\in I}A_{i}}$ are called (ordered) $n$ -tuples, (ordered) triples for $n=3$  

Example 2.16. (a) Using the notion of family, we can now say that the intersection $\textstyle{\bigcap_{i\in{I}}A_{i}}$ and union $\textstyle\bigcup_{i\in I}A_{i}$ as defined in Def. 1.38 are the intersection and union of the family of sets $(A_{i})_{i\in I}$ , respectively. As a concrete example, let us revisit (1.26b), where we have  

$$
(A_{n})_{n\in\mathbb{N}},\quad A_{n}:=\{1,2,\dots,n\},\quad\bigcap_{n\in\mathbb{N}}A_{n}=\{1\}.
$$  

(b) Examples of Sequences:  

$$
{\begin{array}{r l r l}&{{\mathrm{Sequence~in~}}\{\mathbf{0},1\}:}&&{(1,0,1,0,1,0,\dots),}\ &{{\mathrm{Sequence~in~}}\mathbb{N}:}&&{(n^{2})_{n\in\mathbb{N}}=(1,4,9,16,25,\dots),}\ &{{\mathrm{Sequence~in~}}\mathbb{R}:}&&{((-1)^{n}{\sqrt{n}})_{n\in\mathbb{N}}=\left(-1,{\sqrt{2}},-{\sqrt{3}},\dots\right),}\ &{{\mathrm{Sequence~in~}}\mathbb{R}:}&&{(1/n)_{n\in\mathbb{N}}=\left(1,{\frac{1}{2}},{\frac{1}{3}},\dots\right),}\ &{{\mathrm{Finite~Sequence~in~}}\mathcal{P}(\mathbb{N}):}&&{(\{3,2,1\},\{2,1\},\{1\},\emptyset).}\end{array}}
$$  

(c) The Cartesian product $\textstyle\prod_{i\in I}A$ , where all sets $A_{i}=A$ , is the same as $A^{I}$ , the set of all functions from $I$ into $A$ .So, for example, $\textstyle\prod_{n\in\mathbb{N}}\mathbb{R}=\mathbb{R}^{\mathbb{N}}$ is the set of all sequences in $\mathbb{R}$ . If $I=\{1,2,\dots,n\}$ with $n\in\mathbb N$ , then  

$$
\prod_{i\in I}A=A^{\{1,2\ldots,n\}}=:\prod_{i=1}^{n}A=:A^{n}
$$  

is the set of all $n$ -tuples with entries from $A$  

In the following, we explain the common notation. $2^{A}$ for the power set $\mathcal{P}(A)$ of a set $A$ . It is related to a natural identification between subsets and their corresponding characteristic function.  

Definition 2.17. Let $A$ be a set and let $B\subseteq A$ be a subset of $A$ . Then  

$$
\chi_{B}:A\longrightarrow\{0,1\},\quad\chi_{B}(x):=\left\{{1\atop0}\quad{\mathrm{if~}x\not\in B},\right.
$$  

is called the characteristic function of the set $B$ (with respect to the universe $A$ ). One also finds the notations. $1_{B}$ and $\mathbb{1}_{B}$ instead of $\chi_{B}$ (note that all the notations supress the dependence of the characteristic function on the universe $A$  

Proposition 2.18. Let $A$ be a set. Then the map  

$$
\chi:{\mathcal{P}}(A)\longrightarrow\{0,1\}^{A},\quad\chi(B):=\chi_{B},
$$  

is bijective (recall that $\mathcal{P}(A)$ denotes the power set of $A$ and $\{0,1\}^{A}$ denotes the set of all functions from $A$ into $\{0,1\}$  

Proof. $\chi$ is injective: Let $B,C\in{\mathcal{P}}(A)$ with $B\neq C$ . By possibly switching the names of $B$ and $C$ , we may assume there exists $x\in B$ such that $x\notin C$ . Then $\chi_{B}(x)=1$ whereas $\chi_{C}(x)=0$ , showing $\chi(B)\neq\chi(C)$ , proving $\chi$ is injective.  

$\chi$ is surjective: Let $f:A\longrightarrow\{0,1\}$ be an arbitrary function and define $B:=\{x\in A:$ $f(x)=1\}$ . Then $\chi(B)=\chi_{B}=f$ , proving $\chi$ is surjective.  

Proposition 2.18 allows one to identify the sets $\mathcal{P}(A)$ and $\{0,1\}^{A}$ via the bijective map $\chi$ . This fact together with the common practice of set theory to identify the number 2 with the set $\{0,1\}$ explains the notation $2^{A}$ for $\mathcal{P}(A)$  

### 2.2 Relations  

#### 2.2.1 Definition and Properties  

Definition 2.19. Given sets $A$ and $B$ , a relation is a subset. $R$ of $A\times B$ (if one wants to be completely precise, a relation is an ordered triple $(A,B,R)$ , where $R\subseteq A\times B$ : If $A=B$ , then we call. $R$ a relation on $A$ .One says that. $a\in A$ and $b\in B$ are related according to the relation. $R$ if, and only if,. $(a,b)\in R$ . In this context, one usually writes $a R b$ instead of $(a,b)\in R$  

Example 2.20. (a) The relations we are probably most familiar with $\mathrm{are}=\mathrm{and}\leq$ The relation $R$ of equality, usually denoted $=$ , makes sense on every nonempty set $A$  

$$
R:=\Delta(A):=\{(x,x)\in A\times A:x\in A\}.
$$  

The set $\Delta(A)$ is called the diagonal of the Cartesian product, i.e., as a subset of $A\times A$ , the relation of equality is identical to the diagonal:.  

$$
x=y\Leftrightarrow x R y\Leftrightarrow(x,y)\in R=\Delta(A).
$$  

Similarly, the relation $\leq$ on $\mathbb{R}$ is identical to the set  

$$
R_{\leq}:=\{(x,y)\in\mathbb{R}^{2}:x\leq y\}.
$$  

(b) Every function. $f:A\longrightarrow B$ is a relation, namely the relation  

$$
R_{f}=\left\{(x,y)\in A\times B:y=f(x)\right\}=\mathrm{graph}(f).
$$  

Conversely, if $B\neq\emptyset$ , then every relation $R\subseteq A\times B$ uniquely corresponds to the function  

$$
f_{R}:A\longrightarrow\mathcal{P}(B),\quad f_{R}(x)=\{y\in B:x R y\}.
$$  

Definition 2.21. Let $R$ be a relation on the set $A$  

(a) $R$ is called reflexive if, and only if,  

$$
\varprojlim_{x\in A}x R x,
$$  

i.e. if, and only if, every element is related to itself.  

(b) $R$ is called symmetric if, and only if,  

$$
 \underset{x,y\in A}{\forall}\left(x R y\Rightarrow y R x\right),
$$  

i.e. if, and only if, each $x$ is related to. $y$ if, and only if,. $y$ is related to. $x$  

(c) $R$ is called antisymmetric if, and only if,  

$$
\underset{x,y\in A}{\forall}\left((x R y\land y R x)\Rightarrow x=y\right),
$$  

.e. if, and only if, the only possibility for $x$ to be related to $y$ at the same time that $y$ is related to $x$ is in the case $x=y$  

(d) $R$ is called transitive if, and only if,  

$$
{\underset{x,y,z\in A}{\forall}}{\left((x R y\wedge y R z)\right.}\Rightarrow x R z{\big)},
$$  

i.e. if, and only if, the relatedness of $x$ and $y$ together with the relatedness of $y$ and $\mathcal{Z}$ implies the relatedness of. $x$ and $\mathcal{Z}$  

Example 2.22. The relations $-$ and $\leq$ on $\mathbb{R}$ (or $\mathbb{N}$ ) are reflexive, antisymmetric, and transitive; = is also symmetric, whereas $\leq$ is not; $<$ is antisymmetric (since $x<y\land y<x$ is always false) and transitive, but neither reflexive nor symmetric. The relation  

$$
R:=\left\{(x,y)\in\mathbb{N}^{2}:(x,y{\mathrm{~are~both~even}})\vee(x,y{\mathrm{~are~both~odd}})\right\}
$$  

on $\mathbb{N}$ is not antisymmetric, but reflexive, symmetric, and transitive. The relation  

$$
S:=\{(x,y)\in\mathbb{N}^{2}:y=x^{2}\}
$$  

is not transitive (for example, $2S4$ and $4S16$ , but not $2S16$ ), not reflexive, not symmetric; it is only antisymmetric.  

#### 2.2.2 Order Relations  

Definition 2.23. A relation. $R$ on a set $A$ is called a partial order if, and only if,. $R$ is reflexive, antisymmetric, and transitive. If $R$ is a partial order, then one usually writes $x\leq y$ instead of $x R y$ . A partial order. $\leq$ is called a total or linear order if, and only if, for each $x,y\in A$ , one has $x\leq y$ or $y\leq x$  

Notation 2.24. Given a (partial or total) order $\leq$ on $A\neq\emptyset$ , we write $x<y$ if, and only if, $x\leq y$ and $x\neq y$ , calling $<$ the strict order corresponding to $\leq$ (note that the strict order is never a partial order).  

Definition 2.25. Let $\leq$ be a partial order on $A\neq\emptyset$ $\varnothing\neq B\subseteq A$ (a) $x\in A$ is called lower (resp. upper) bound for. $B$ if, and only if,. $x\leq b$ (resp. $b\leq x$ for each $b\in B$ . Moreover, $B$ is called bounded from below (resp. from above) if, and only if, there exists a lower (resp. upper) bound for $B$ $B$ is called bounded if, and. only if, it is bounded from above and from below..  

(b) $x\in B$ is called minimum or just min (resp. maximum or max) of $B$ if, and only if, $x$ is a lower (resp. upper) bound for $B$ . One writes $x=\operatorname*{min}B$ if $x$ is minimum and $x=\operatorname*{max}B$ if $x$ is maximum.  

(c) A maximum of the set of lower bounds of $B$ (i.e. a largest lower bound) is called infimum of. $B$ , denoted $\operatorname{inf}B$ ; a minimum of the set of upper bounds of. $B$ (i.e. a smallest upper bound) is called supremum of $B$ , denoted $\operatorname{sup}B$  

Example 2.26. (a) For each $A\subseteq\mathbb{R}$ , the usual relation $\leq$ defines a total order on $A$ For $A=\mathbb{R}$ , we see that $\mathbb{N}$ has $0$ and $^{1}$ as lower bound with $1=\operatorname*{min}\mathbb{N}=\operatorname*{inf}\mathbb{N}$ . On the other hand, $\mathbb{N}$ is unbounded from above. The set $M:=\{1,2,3\}$ is bounded with $\operatorname*{min}M=1$ $\operatorname*{max}M=3$ . The positive real numbers $\mathbb{R}^{+}:=\{x\in\mathbb{R}:x>0\}$ have inf $\mathbb R^{+}=0$ , but they do not have a minimum (if $x>0$ , then $0<x/2<x$  

(b) Consider $A:=\mathbb{N}\times\mathbb{N}$ . Then  

$$
(m_{1},m_{2})\leq(n_{1},n_{2})\Leftrightarrow m_{1}\leq n_{1}\land m_{2}\leq n_{2},
$$  

defines a partial order on. $A$ that is not a total order (for example, neither $(1,2)\leq$ $(2,1)$ nor $(2,1)\leq(1,2)$ ). For the set  

$$
B:=\{(1,1),(2,1),(1,2)\},
$$  

we have inf $B=\operatorname*{min}B=(1,1)$ $B$ does not have a max, but $\operatorname*{sup}B=(2,2)$ (if $(m,n)\in A$ is an upper bound for $B$ , then $(2,1)\leq(m,n)$ implies $2\leq m$ and $(1,2)\leq(m,n)$ implies $2\leq n$ , i.e. $(2,2)\leq(m,n)$ ; since $(2,2)$ is clearly an upper bound for $B$ , we have proved $\operatorname*{sup}B=(2,2)$  

A different order on. $A$ is the so-called lexicographic order defined by  

$$
(m_{1},m_{2})\leq(n_{1},n_{2})\Leftrightarrow m_{1}<n_{1}\lor(m_{1}=n_{1}\land m_{2}\leq n_{2}).
$$  

In contrast to the order from (2.47), the lexicographic order does define a total order on $A$  

Lemma 2.27. Let $\leq$ be a partial order on $A\neq\emptyset,\emptyset\neq B\subseteq A$ . Then the relation $\geq$ defined by  

$$
x\geq y\Leftrightarrow y\leq x,
$$  

is also a partial order on $A$ . Moreover, using obvious notation, we have, for each $x\in A$  

$x\leq$ -lower bound for $B$ $\begin{array}{r l}{\Leftrightarrow}&{{}\quad x\geq-u p p e r b o u n d f o r B,}\ {\Leftrightarrow}&{{}\quad x\geq-l o w e r b o u n d f o r B,}\ {\Leftrightarrow}&{{}\quad x=\operatorname*{max}_{\geq}B,}\ {\Leftrightarrow}&{{}\quad x=\operatorname*{min}_{\geq}B,}\ {\Leftrightarrow}&{{}\quad x=\operatorname*{sup}_{\geq}B,}\ {\Leftrightarrow}&{{}\quad x=\operatorname*{inf}_{>}B.}\end{array}$ (2.51a)   
$x\leq$ -upper bound for $B$ (2.51b)   
$\begin{array}{l}{x=\operatorname*{min}_{\leq}B}\ {x=\operatorname*{max}_{\leq}B}\ {x=\operatorname*{inf}_{\leq}B}\ {x=\operatorname*{sup}_{\leq}B}\end{array}$ (2.51d) (2.51c) (2.51e) (2.51f)  

Proof. Reflexivity, antisymmetry, and transitivity of $\leq$ clearly imply the same properties for $\geq$ , respectively. Moreover  

proving (2.51a). Analogously, we obtain (2.51b). Next, (2.51c) and (2.51d) are implied by (2.51a) and (2.51b), respectively. Finally, (2.51e) is proved by  

$$
\begin{array}{r l}&{x=\operatorname*{inf}_{\leq{B}}\Leftrightarrow x=\operatorname*{max}_{\leq}\{y\in A:y\leq\mathrm{-lower~bound~for~}B\}}\ &{\Leftrightarrow x=\operatorname*{min}_{\geq}\{y\in A:y\geq\mathrm{-upper~bound~for~}B\}\Leftrightarrow x=\operatorname*{sup}_{\geq}B,}\end{array}
$$  

and (2.51f) follows analogously.  

Proposition 2.28. Let $\leq$ be a partial order on. $A\neq\emptyset$ $\emptyset\neq B\subseteq A$ .The elements max $B$ $\operatorname*{min}B$ $\operatorname{sup}B$ , inf $B$ are all unique, provided they exist.  

Proof. Exercise.  

Definition 2.29. Let $A,B$ be nonempty sets with partial orders, both denoted by $\leq$ (even though they might be different). A function $f:A\longrightarrow B$ , is called (strictly) isotone, order-preserving, or increasing if, and only if,  

$$
\begin{array}{r}{\underset{x,y\in A}{\forall}\left(x<y\Rightarrow f(x)\leq f(y)\mathrm{~}(\mathrm{resp.~}f(x)<f(y))\right);}\end{array}
$$  

$f$ is called (strictly) antitone, order-reversing, or decreasing if, and only if,  

$$
{\underset{x,y\in A}{\forall}}\left(x<y\Rightarrow f(x)\geq f(y){\mathrm{~}}({\mathrm{resp.~}}f(x)>f(y))\right).
$$  

Functions that are (strictly) isotone or antitone are called (strictly) monotone.  

Proposition 2.30. Let $A,B$ be nonempty sets with partial orders, both denoted by $\leq$  

(a) A (strictly) isotone function $f:A\longrightarrow B$ becomes a (strictly) antitone function and vice versa if precisely one of the relations $\leq$ is replaced by .   
(b) If the order $\leq$ on $A$ is total and $f:A\longrightarrow B$ is strictly isotone or strictly antitone, then $f$ is one-to-one.   
(c) If the order $\leq$ on A is total and $f:A\longrightarrow B$ is invertible and strictly isotone (resp.. antitone), then $f^{-1}$ is also strictly isotone (resp. antitone).  

Proof. (a) is immediate from (2.52).  

(b): Due to (a), it suffices to consider the case that $f$ is strictly isotone. If. $f$ is strictly isotone and $x\neq y$ , then $x<y$ or $y<x$ since the order on. $A$ is total. Thus,. $f\left(x\right)<f\left(y\right)$ or $f\left(y\right)<f\left(x\right)$ , i.e. $f\left(x\right)\neq f\left(y\right)$ in every case, showing. $f$ is one-to-one.  

(c): Again, due to (a), it suffices to consider the isotone case. If $u,v\in B$ such that $u<v$ then $u=f(f^{-1}(u))$ $v=f(f^{-1}(v))$ , and the isotonicity of. $f$ imply $f^{-1}(u)<f^{-1}(v)$ (we are using that the order on $A$ is total  otherwise,. $f^{-1}(u)$ and $f^{-1}(v)$ need not be. comparable).  

Example 2.31. (a) $f:\mathbb{N}\longrightarrow\mathbb{N}$ $f(n):=2n$ , is strictly increasing, every constant map. on $\mathbb{N}$ is both increasing and decreasing, but not strictly increasing or decreasing. All maps occurring in (2.25) are neither increasing nor decreasing..  

(b) The map $f:\mathbb{R}\longrightarrow\mathbb{R}$ $f(x):=-2x$ , is invertible and strictly decreasing, and so is $f^{-1}:\mathbb{R}\longrightarrow\mathbb{R}$ $f^{-1}(x):=-x/2$  

(c) The following counterexamples show that the assertions of Prop. 2.30(b),(c) are no longer correct if one does not assume the order on $A$ is total. Let $A$ be the set from (2.48) (where it had been called $B$ ) with the (nontotal) order from (2.47). The map  

$$
\begin{array}{r}{f:A\longrightarrow\mathbb{N},\quad\left\{{f(1,1):=1,\atop f(1,2):=2,\atop f(2,1):=2,\quad}\right.}\end{array}
$$  

is strictly isotone, but not one-to-one. The map  

$$
f:A\longrightarrow\{1,2,3\},\quad\left\{{\begin{array}{l}{f(1,1):=1,}\ {f(1,2):=2,}\ {f(2,1):=3,}\end{array}}\right.
$$  

is strictly isotone and invertible, however $f^{-1}$ is not isotone (since. $2\:<\:3$ , but $f^{-1}(2)=(1,2)$ and $f^{-1}(3)=(2,1)$ are not comparable, i.e. $f^{-1}(2)\le f^{-1}(3)$ is not true).  

#### 2.2.3 Equivalence Relations  

Definition 2.32. Let $R$ be a relation on a set $A$  

(a) $R$ is called an equivalence relation if, and only if, $R$ is reflexive, symmetric, and transitive. If $R$ is an equivalence relations, then one often writes $x\sim y$ instead of $x R y$  

(b) Let $\sim:=R$ be an equivalence relation on $A$ . For each $x\in A$ , define  

$$
[x]:=\{y\in A:x\sim y\}
$$  

and call $[x]$ the equivalence class of $x$ . Moreover, each. $y\in[x]$ is called a represen-. tative of $[x]$ . The set of all equivalence classes $A/\sim:=\{[x]:x\in A\}$ is called the quotient set of $A$ by $\sim$ , and the map  

$$
\pi:A\longrightarrow A/\sim,\quad x\mapsto[x],
$$  

is called the corresponding quotient map, canonical map, or canonical projection.  

The following Th. 2.33 shows that the equivalence classes of an equivalence relation on a nonempty set. $A$ decompose $A$ into disjoint sets and, conversely, that a given. decomposition of a nonempty set $A$ into disjoint nonempty sets. $A_{i}$ $i\in I$ , gives rise to a unique equivalence relation $\sim$ on $A$ such that the $A_{i}$ are precisely the equivalence. classes corresponding to. $\sim$ ..  

Theorem 2.33. Let $A$ be a nonempty set.  

(a) Given a disjoint union $\textstyle A=\dot{\bigcup_{i\in I}A_{i}}$ with every. $A_{i}\neq\emptyset$ (a so-called decomposition: of $A$ ), an equivalence relation on $A$ is defined by.  

$$
x\sim y:\Leftrightarrow\underset{i\in I}{\exists}\left(x\in A_{i}\land y\in A_{i}\right).
$$  

Moreover, for the equivalence classes given by $\sim$ , one then has  

$$
\forall_{x\in A}\quad\forall_{i\in I}\quad{\Big(}x\in A_{i}\Leftrightarrow A_{i}=[x]{\Big)}.
$$  

(b) Given an equivalence relation $\sim$ on a nonempty set. $A$ , the equivalence classes given. by $\sim$ form a decomposition of. $A$ : One has  

$$
\begin{array}{r l}{\underset{x,y\in A}{\forall}}&{{}\Big(\big([x]=[y]\Leftrightarrow x\sim y\big)\quad\land\quad\big([x]\cap[y]=\emptyset\Leftrightarrow\neg(x\sim y)\big)\Big)}\end{array}
$$  

and  

$$
A=\dot{\bigcup_{i\in I}}A_{i},
$$  

where $I:=A/\sim$ is the quotient set of Def. 2.32(b) and $A_{i}:=i$ for each $i\in I$  

Proof. (a): That $\sim$ is symmetric is immediate from (2.55). If $x\in A$ , then, as $A$ is the union of the $A_{i}$ , there exists $i\in I$ with $x\in A_{i}$ , showing $x\sim x$ , i.e. $\sim$ is reflexive. If $x,y,z\in A$ with $x\sim y$ and $y\sim z$ , then there exist $i,j\in I$ with $x,y\in A_{i}$ and $y,z\in A_{j}$ Then $y\in A_{i}\cap A_{j}$ , implying $i=j$ (as the union is disjoint) and $x\sim z$ , showing $\sim$ to be transitive as well. Thus, we have shown $\sim$ to be an equivalence relation. Now consider $x\in A$ and $i\in I$ . If $A_{i}=[x]$ , then $x\sim x$ implies $x\in[x]=A_{i}$ . Conversely, assume $x\in A_{i}$ . Then  

$$
y\in A_{i}\quad{\stackrel{(2,3)}{\iff}}\quad x\sim y\quad\Leftrightarrow\quad y\in[x],
$$  

proving $A_{i}=[x]$ . Hence, we have verified (2.56) and (a).  

(b): Let $x,y\in A$ . If $[x]=[y]$ , then (as $y\sim y$ $y\in[y]=[x]$ , implying $x\sim y$ . Conversely, assume $x\sim y$ . Then $z\in[y]$ implies $y\sim z$ , implying $x\sim z$ (since $\sim$ is transitive) and, thus, $z\in[x]$ and $[y]\subseteq[x]$ . From this, and the symmetry of. $\sim$ , we also obtain $x\sim y$ implies $y\sim x$ , which implies $[x]\subseteq[y]$ . Altogether, we have $[x]=[y]$ . Thus, we have established the first equivalence of (2.57). In consequence, we also have  

$$
[x]\neq[y]\Leftrightarrow\neg(x\sim y).
$$  

To prove the second equivalence of (2.57), we now show $[x]\neq[y]\Leftrightarrow[x]\cap[y]=\emptyset$ : If $[x]\cap[y]=\emptyset$ , then $[x]=[y]$ could only hold for $[x]=[y]=\emptyset$ .However, $x\in[x]$ and $y\in[y]$ , showing $[x]\neq[y]$ . For the converse, we argue via contraposition and assume $z\in[x]\cap[y]$ . Then $x\sim z$ and $y\sim z$ and, by symmetry and transitivity of $\sim$ $x\sim y$ and $[x]=[y]$ , proving the second equivalence of (2.57). It remains to verify (2.58). From (2.57), we know the elements of $A/\sim$ to be disjoint. On the other hand, if $x\in A$ , then $x\in[x]\in A/\sim$ , showing $A$ to be the union of the $A_{i}$ , thereby proving (2.58) and the theorem.  

Example 2.34. (a) The equality relation = is an equivalence relation on each $A\neq\emptyset$ where, for each $x\in A$ , one has $[x]=\left\{x\right\}$  

(b) The relation $R$ defined in (2.45) is an equivalence relation on. $\mathbb{N}$ .Here, $R$ yields pre cisely two equivalence classes, one consisting of all even numbers and one consisting of all odd numbers..  

Remark 2.35. If $\sim$ is an equivalence relation on a nonempty set $A$ , then, clearly, the quotient map $\pi:A\longrightarrow A/\sim$ $x\mapsto[x]$ , is always surjective. It is injective (and, thus, bijective) if, and only if, every equivalence class has precisely one element, i.e. if, and only if, $\sim$ is the equality relation $=$  

Example 2.36. (a) An important application of equivalence relations and quotient sets is the construction of the set $\mathbb{Z}=\{\cdot\cdot\cdot,-2,-1,0,1,2,\cdot\cdot\cdot\}$ of integers from the set $\ensuremath{\mathbb{N}}_{0}$ of natural numbers (including $0$ ) of Def. 1.28: One actually defines $\mathbb{Z}$ as the quotient set with respect to the following equivalence relation $\sim$ on $\mathbb{N}_{0}\times\mathbb{N}_{0}$ , where the relation $\sim$ on $\mathbb{N}_{0}\times\mathbb{N}_{0}$ is defined $^2$ by  

$$
(a,b)\sim(c,d)\quad:\Leftrightarrow\quad a+d=b+c.
$$  

We verify that (2.59) does, indeed, define an equivalence relation on $\mathbb{N}_{0}\times\mathbb{N}_{0}$ : If $a,b\in\ensuremath{\mathbb{N}}_{0}$ , then $a+b=b+a$ shows $(a,b)\sim(a,b)$ , proving $\sim$ to be reflexive. If $a,b,c,d\in\ensuremath{\mathbb{N}}_{0}$ , then  

$$
a,b)\sim(c,d)\quad\Rightarrow\quad a+d=b+c\quad\Rightarrow\quad c+b=d+a\quad\Rightarrow\quad(c,d)\sim(a,b),
$$  

proving $\sim$ to be symmetric. If $a,b,c,d,e,f\in\mathbb{N}_{0}$ , then.  

$$
\begin{array}{r l}&{\imath,b)\sim(c,d)\wedge(c,d)\sim(e,f)\quad\Rightarrow\quad a+d=b+c\wedge c+f=d+e}\ &{\Rightarrow\quad a+d+c+f=b+c+d+e\quad\Rightarrow\quad a+f=b+e\quad\Rightarrow\quad(a,b)\sim(e,f),}\end{array}
$$  

proving $\sim$ to be transitive and an equivalence relation. Thus, we can, indeed, define  

$$
\mathbb{Z}:=(\mathbb{N}_{0}\times\mathbb{N}_{0})/\sim~=~\left\{[(a,b)]:(a,b)\in\mathbb{N}_{0}\times\mathbb{N}_{0}\right\}.
$$  

To simplify notation, in the following, we will write  

$$
[a,b]:=[(a,b)]
$$  

for the equivalence class of $(a,b)$ with respect to. $\sim$ . The map  

$$
\iota:\mathbb{N}_{0}\longrightarrow\mathbb{Z},\quad\iota(n):=[n,0],
$$  

is injective (since. $\iota(m)=[m,0]=\iota(n)=[n,0]$ implies $m+0=0+n$ , i.e. $m=n$ ). It is customary to identify $\ensuremath{\mathbb{N}}_{0}$ with $\iota(\mathbb{N}_{0})$ , as it usually does not cause any confusion. One then just writes. $n$ instead of. $\lfloor n,0\rfloor$ and $-n$ instead of. $[0,n]=-[n,0]$ (we will come back to the addition on. $\mathbb{Z}$ later and then this equation will make more sense, cf. Th. 4.15).  

(b) Having constructed the set if integers. $\mathbb{Z}$ in (a), in a next step, one can perform a. similar construction to obtain the set of rational numbers $\mathbb{Q}$ . One defines $\mathbb{Q}$ as the quotient set with respect to the following equivalence relation $\sim$ on $\mathbb{Z}\times(\mathbb{Z}\setminus\{0\})$ where the relation $\sim$ on $\mathbb{Z}\times(\mathbb{Z}\setminus\{0\})$ is defined $^3$ by  

$$
(a,b)\sim(c,d)\quad:\Leftrightarrow\quad a\cdot d=b\cdot c.
$$  

Noting that (2.63) is precisely the same as (2.59) if $^+$ is replaced by. $\cdot$ , the proof from (a) also shows that (2.63) does, indeed, define an equivalence relation on $\mathbb{Z}\times(\mathbb{Z}\setminus\{0\})$ : One merely replaces each. $^+$ with . and each. $\ensuremath{\mathbb{N}}_{0}$ with $\mathbb{Z}$ or $\mathbb{Z}\setminus\{0\}$ respectively. The only modification needed occurs for $0\in\{a,c,e\}$ in the proof of. transitivity (in this case, the proof of (a) yields $a d c f=0=b c d e$ , which does not. imply $a f=b e$ ), where one now argues, for $a=0$  

$$
\begin{array}{l}{{(a,b)\sim(c,d)\wedge(c,d)\sim(e,f)\quad\Rightarrow\quad a d=0=b c\wedge c f=d e}}\ {{\overset{b\neq0}{\Rightarrow}\quad c=0\quad\overset{d\neq0}{\Rightarrow}\quad e=0\quad\Rightarrow\quad a f=0=b e\quad\Rightarrow\quad(a,b)\sim(e,f),}}\end{array}
$$  

for $c=0$  

$$
\begin{array}{r l}&{(a,b)\sim(c,d)\wedge(c,d)\sim(e,f)\quad\Rightarrow\quad a d=0=b c\wedge c f=0=d e}\ &{\overset{d\to0}{\Rightarrow}\quad a=e=0\quad a f=0=b e\quad\Rightarrow\quad(a,b)\sim(e,f),}\end{array}
$$  

and, for $e=0$  

$$
\begin{array}{r l}&{(a,b)\sim(c,d)\wedge(c,d)\sim(e,f)\quad\Rightarrow\quad a d=b c\wedge c f=0=d e}\ &{\xrightarrow{f\neq0}\quad c=0\quad\xrightarrow{d\neq0}\quad a=0\quad\Rightarrow\quad a f=0=b e\quad\Rightarrow\quad(a,b)\sim(e,f).}\end{array}
$$  

Thus, we can, indeed, define  

$$
\mathbb{Q}:=\left(\mathbb{Z}\times(\mathbb{Z}\setminus\{0\})\right)/\sim~=~\{[(a,b)]:~(a,b)\in\mathbb{Z}\times(\mathbb{Z}\setminus\{0\})\}.
$$  

As is common, we will write  

$$
\frac{a}{b}:=a/b:=[(a,b)]
$$  

for the equivalence class of $(a,b)$ with respect to $\sim$ . The map  

$$
\iota:\mathbb{Z}\longrightarrow\mathbb{Q},\quad\iota(k):=\frac{k}{1},
$$  

is injective (since $\iota(k)=k/1=\iota(l)=l/1$ implies $k\cdot1=l\cdot1$ , i.e. $k=l$ ). It is customary to identify. $\mathbb{Z}$ with $\iota(\mathbb{Z})$ , as it usually does not cause any confusion. One then just writes. $k$ instead of $\textstyle{\frac{k}{1}}$  

While the set of real numbers $\mathbb{R}$ can now also be constructed from the set $\mathbb{Q}$ , making use of the notions of equivalence relation and quotient set, the construction is more complicated and it also makes use of additional notions from the field of Analysis. Thus, this construction is not within the scope of this class and the interested reader is referred to [Phi16, Sec. D.5].  

## 3 Natural Numbers, Induction, and the Size of Sets  

### 3.1 Induction and Recursion  

One of the most useful proof techniques is the method of induction - it is used in situations, where one needs to verify the truth of statements $\phi(n)$ for each $n\in\mathbb{N}$ , i.e. the truth of the statement  

$$
\forall_{n\in\mathbb{N}}\phi(n).
$$  

Induction is based on the fact that $\mathbb{N}$ satisfies the so-called Peano axioms:  

P1: N contains a special element called one, denoted 1.  

P2: There exists an injective map $S:\mathbb{N}\longrightarrow\mathbb{N}\backslash\{1\}$ , called the successor function (for each $n\in\mathbb N$ $S(n)$ is called the successor of $n$  

P3: If a subset $A$ of $\mathbb{N}$ has the property that. $1\in A$ and $S(n)\in A$ for each $n\in A$ , then $A$ is equal to $\mathbb{N}$ . Written as a formula, the third axiom is:  

$$
\sharp_{A\in\mathcal{P}(\mathbb{N})}\left(1\in A\wedge S(A)\subseteq A\Rightarrow A=\mathbb{N}\right).
$$  

Remark 3.1. In Def. 1.28, we had introduced the natural numbers $\mathbb{N}:=\{1,2,3,\dots\}$ The successor function is. $S(n)=n+1$ . In axiomatic set theory, one starts with the Peano axioms and shows that the axioms of set theory allow the construction of a set $\mathbb{N}$ which satisfies the Peano axioms. One then defines $2:=S(1)$ $3:=S(2)$ , ... $n+1:=S(n)$ . The interested reader can find more details in [Phi16, Sec. D.1].  

Theorem 3.2 (Principle of Induction). Suppose, for each $n\in\mathbb{N}$ $\phi(n)$ is a statement (i.e. a predicate of n in the language of Def. 1.31). If (a) and (b) both hold, where  

(a) $\phi(1)$ is true,  

$$
\operatorname*{\forall}_{n\in\mathbb{N}}\big(\phi(n)\Rightarrow\phi(n+1)\big),
$$  

then (3.1) is true, i.e. $\phi(n)$ is true for every. $n\in\mathbb N$  

Proof. Let $A:=\{n\in\mathbb{N}:\phi(n)\}$ . We have to show $A=\mathbb{N}$ . Since $1\in A$ by (a), and  

$$
n\in A\Rightarrow\phi(n)\stackrel{\mathrm{(b)}}{\Rightarrow}\phi(n+1)\Rightarrow S(n)=n+1\in A,
$$  

i.e. $S(A)\subseteq A$ , the Peano axiom P3 implies $A=\mathbb{N}$  

Remark 3.3. To prove some $\phi(n)$ for each $n\in\mathbb{N}$ by induction according to Th. 3.2 consists of the following two steps:  

(a) Prove $\phi(1)$ , the so-called base case.  

(b) Perform the inductive step, i.e. prove that $\phi(n)$ (the induction hypothesis) implies $\phi(n+1)$  

Example 3.4. We use induction to prove the statement  

$$
\underset{n\in\mathbb{N}}{\underbrace{\forall}}\underbrace{\left(1+2+\cdots+n=\frac{n(n+1)}{2}\right)}_{\phi(n)}:
$$  

Base Case ( $n=1$ ): $\textstyle1={\frac{1\cdot2}{2}}$ , i.e. $\phi(1)$ is true.  

Induction Hypothesis: Assume $\phi(n)$ , i.e. $1+2+\cdots+n={\frac{n(n+1)}{2}}$ holds. Induction Step: One computes  

$$
\begin{array}{l c l}{{1+2+\cdots+n+(n+1)}}&{{\stackrel{\left(\phi(n)\right)}{=}}}&{{\frac{n(n+1)}{2}+n+1=\frac{n(n+1)+2n+2}{2}}}\ {{}}&{{}}&{{=}}&{{\frac{n^{2}+3n+2}{2}=\frac{(n+1)(n+2)}{2},}}\end{array}
$$  

i.e. $\phi(n+1)$ holds and the induction is complete.  

Corollary 3.5. Theorem 3.2 remains true if (b) is replaced by  

$$
\begin{array}{r}{\underset{n\in\mathbb{N}}{\forall}~\left(\left(\underset{1\leq m\leq n}{\forall}\phi(m)\right)\right.\Rightarrow\phi(n+1)\right).}\end{array}
$$  

Proof. If, for each. $n\in\mathbb N$ , we use $\psi(n)$ to denote $\underset{1\leq m\leq n}{\forall}\phi(m)$ , then (3.5) is equivalent to $\operatorname*{\forall}_{n\in\mathbb{N}}\left(\psi(n)\Rightarrow\psi(n+1)\right)$ , i.e. to Th. 3.2(b) with. $\phi$ replaced by $\psi$ . Thus, Th. 3.2 implies. $\psi(n)$ holds true for each. $n\in\mathbb N$ , i.e. $\phi(n)$ holds true for each. $n\in\mathbb N$ $\vert$  

Corollary 3.6. Let $I$ be an index set. Suppose, for each $i\in I$ $\phi(i)$ is a statement. If there is a bijective map $f:\mathbb{N}\longrightarrow I$ and (a) and (b) both hold, where  

(a) $\phi\big(f(1)\big)$ is true,  

$$
\underset{n\in\mathbb{N}}{\forall}\Big(\phi\big(f(n)\big)\Rightarrow\phi\big(f(n+1)\big)\Big),
$$  

then $\phi(i)$ is true for every $i\in I$  

Finite Induction: The above assertion remains true if $f:\{1,\dots,m\}\longrightarrow I$ is bijective for some $m\in\mathbb{N}$ and $\mathbb{N}$ in (b) is replaced by $\{1,\dots,m-1\}$  

Proof. If, for each $n\in\mathbb{N}$ , we use $\psi(n)$ to denote $\phi(f(n))$ , then Th. 3.2 shows $\psi(n)$ is true for every. $n\in\mathbb N$ . Given $i\in I$ , we have $n:=f^{-1}(i)\in\mathbb{N}$ with $f(n)=i$ , showing that. $\phi(i)=\phi\bigl(f(n)\bigr)=\psi(n)$ is true.  

For the finite induction, let $\psi(n)$ denote $\big(n\leq m\land\phi\big(f(n)\big)\big)\lor n>m$ . Then, for $1\leq$ $n<m$ , we have $\psi(n)\Rightarrow\psi(n+1)$ due to (b). For $n\geq m$ , we also have $\psi(n)\Rightarrow\psi(n+1)$ due to $n\geq m\Rightarrow n+1>m$ .Thus, Th. 3.2 shows $\psi(n)$ is true for every $n\in\mathbb N$ . Given $i\in I$ , it is $n:=f^{-1}(i)\in\{1,\dots,m\}$ with $f(n)=i$ . Since $n\leq m\land\psi(n)\Rightarrow\phi\big(f(n)\big)$ , we obtain that $\phi(i)$ is true.  

Apart from providing a widely employable proof technique, the most important application of Th. 3.2 is the possibility to define sequences (i.e. functions with domain $\mathbb{N}$ , Cf. Def. 2.15(b)) inductively, using so-called recursion:  

Theorem 3.7 (Recursion Theorem). Let $A$ be a nonempty set and $x\in A$ .Given a sequence of functions $(f_{n})_{n\in\mathbb{N}}$ , where $f_{n}:A^{n}\longrightarrow A$ , there exists a unique sequence $(x_{n})_{n\in\mathbb{N}}$ in $A$ satisfying the following two conditions:.  

i $x_{1}=x$ (ii) $\operatorname*{\forall}_{n\in\mathbb{N}}x_{n+1}=f_{n}(x_{1},\ldots,x_{n}).$  

The same holds if $\mathbb{N}$ is replaced by an index set I as in Cor. 3.6.  

Proof. To prove uniqueness, let $(x_{n})_{n\in\mathbb{N}}$ and $(y_{n})_{n\in\mathbb{N}}$ be sequences in. $A$ , both satisfying.   
(i) and (ii), i.e..  

$$
\begin{array}{c}{x_{1}=y_{1}=x\quad\mathrm{and}}\ {\underset{n\in\mathbb{N}}{\forall}\left(x_{n+1}=f_{n}(x_{1},\dots,x_{n})\wedge y_{n+1}=f_{n}(y_{1},\dots,y_{n})\right).}\end{array}
$$  

We prove by induction (in the form of Cor. 3.5) that $(x_{n})_{n\in\mathbb{N}}=(y_{n})_{n\in\mathbb{N}}$ , i.e.  

$$
\underbrace{\forall}_{n\in\mathbb{N}}\underbrace{x_{n}=y_{n}}_{\phi(n)}:
$$  

Base Case ( $n=1$ ): $\phi(1)$ is true according to (3.6a).  

Induction Hypothesis: Assume $\phi(m)$ for each $m\in\{1,\ldots,n\}$ , i.e. $x_{m}=y_{m}$ holds for. each $m\in\{1,\ldots,n\}$  

Induction Step: One computes  

$$
x_{n+1}\overset{(3.6\mathrm{b})}{=}f_{n}(x_{1},\ldots,x_{n})\overset{\left(\phi(1),\ldots,\phi(n)\right)}{=}f_{n}(y_{1},\ldots,y_{n})\overset{(3.6\mathrm{b})}{=}y_{n+1},
$$  

i.e. $\phi(n+1)$ holds and the induction is complete.  

To prove existence, we have to show that there is a function $F:\mathbb{N}\longrightarrow A$ such that the following two conditions hold:.  

$$
\begin{array}{r}{F(1)=x,\qquad}\ {\underset{n\in\mathbb{N}}{\forall}F(n+1)=f_{n}\big(F(1),\dots,F(n)\big).}\end{array}
$$  

To this end, let  

$$
\begin{array}{r}{F:=\left\{B\subseteq\mathbb{N}\times A:(1,x)\in B\land\underset{(1,a_{1}),\ldots,(n,a_{n})\in B}{\forall}\left(n+1,f_{n}(a_{1},\ldots,a_{n})\right)\in B\right\}}\end{array}
$$  

and  

$$
G:=\bigcap_{B\in\mathcal{F}}B.
$$  

Note that. $G$ is well-defined, as $\mathbb{N}\times A\in\mathcal{F}$ .Also, clearly, $G\in{\mathcal{F}}$ .We would like to define $F^{\prime}$ such that $G=\operatorname{graph}(F)$ . For this to be possible, we will show, by induction,  

$$
\underbrace{\forall\qquad\exists!\quad(n,x_{n})\in G}_{\phi(n)}.
$$  

Base Case ( $n=1$ ): From the definition of $G$ , we know $(1,x)\in G$ . If $(1,a)\in G$ with $a\neq x$ , then $H:=G\backslash\{(1,a)\}\in{\mathcal{F}}$ , implying. $G\subseteq H$ in contradiction to $(1,a)\notin H$ This shows. $a=x$ and proves $\phi(1)$  

Induction Hypothesis: Assume $\phi(m)$ for each $m\in\{1,\ldots,n\}$  

Induction Step: From the induction hypothesis, we know  

$$
\exists_{\{x_{1},\ldots,x_{n}\}\in A^{n}}^{\downarrow}\left(1,x_{1}\right),\ldots,(n,x_{n})\in G.
$$  

Thus, if we let. $x_{n+1}:=f_{n}(x_{1},\ldots,x_{n})$ , then $(n+1,x_{n+1})\in G$ by the definition of $G$ . If $(n+1,a)\in G$ with $a\neq x_{n+1}$ , then $H:=G\setminus\{(n+1,a)\}\in\mathcal{F}$ (using the uniqueness of the $(1,x_{1}),\dots,(n,x_{n})\in G)$ , implying. $G\subseteq H$ in contradiction to $(n+1,a)\notin H$ . This shows $a=x_{n+1}$ , proves $\phi(n+1)$ , and completes the induction.  

Due to (3.12), we can now define $F:\mathbb{N}\longrightarrow A$ $F(n):=x_{n}$ , and the definition of $G$ then guarantees the validity of (3.9).  

Example 3.8. In many applications of Th. 3.7, one has functions $g_{n}:A\longrightarrow A$ and uses  

$$
\forall_{n\in\mathbb{N}}\left(f_{n}:A^{n}\longrightarrow A,\quad f_{n}(x_{1},\dots,x_{n}):=g_{n}(x_{n})\right).
$$  

Here are some important concrete examples:  

(a) The factorial function $F:\mathbb{N}_{0}\longrightarrow\mathbb{N}$ $n\mapsto n!$ , is defined recursively by  

$$
0!:=1,\quad1!:=1,\quad\forall_{n\in\mathbb{N}}(n+1)!:=(n+1)\cdot n!,
$$  

i.e. we have $A=\mathbb{N}$ and $g_{n}(x):=(n+1)\cdot x$ . So we obtain  

$$
(n!)_{n\in\mathbb{N}_{0}}=(1,1,2,6,24,120,\dots).
$$  

(b) Summation Symbol: On $A=\mathbb{R}$ (or, more generally, on every set. $A$ , where an. addition $+:A\times A\longrightarrow A$ is defined), define recursively, for each given (possibly finite) sequence. $(a_{1},a_{2},\ldots)$ in $A$  

$$
\sum_{i=1}^{1}a_{i}:=a_{1},\quad\sum_{i=1}^{n+1}a_{i}:=a_{n+1}+\sum_{i=1}^{n}a_{i}{\mathrm{~for~}}n\geq1,
$$  

i.e. we have  

$$
g_{n}:A\longrightarrow A,\quad g_{n}(x):=x+a_{n+1}.
$$  

In (3.15a), one can also use other symbols for $i$ , except $a$ and $n$ ; for a finite sequence, $n$ needs to be less than the maximal index of the finite sequence.  

More generally, if. $I$ is an index set and $\phi:\{1,\dots,n\}\longrightarrow I$ a bijective map, then define  

$$
\sum_{i\in I}a_{i}:=\sum_{i=1}^{n}a_{\phi(i)}.
$$  

The commutativity of addition implies that the definition in (3.15c) is actually independent of the chosen bijective map. $\phi$ (cf. Th. B.4 in the Appendix). Also. define  

$$
\sum_{i\in\emptyset}a_{i}:=0
$$  

(for a general $A$ $0$ is meant to be an element such that $a+0=0+a=a$ for each $a\in A$ and we can even define this if $0\not\in A$  

(c) Product Symbol: On $A=\mathbb{R}$ (or, more generally, on every set $A$ , where a multiplication $\cdot:A\times A\longrightarrow A$ is defined), define recursively, for each given (possibly finite) sequence $(a_{1},a_{2},\ldots)$ in $A$  

$$
\prod_{i=1}^{1}a_{i}:=a_{1},\quad\prod_{i=1}^{n+1}a_{i}:=a_{n+1}\cdot\prod_{i=1}^{n}a_{i}{\mathrm{~for~}}n\geq1,
$$  

i.e. we have  

$$
g_{n}:A\longrightarrow A,\quad g_{n}(x):=a_{n+1}\cdot x.
$$  

In (3.16a), one can also use other symbols for. $i$ , except $a$ and $n$ ; for a finite sequence,.   
$n$ needs to be less than the maximal index of the finite sequence.  

More generally, if $I$ is an index set and $\phi:\{1,\dots,n\}\longrightarrow I$ a bijective map, then define  

$$
\prod_{i\in I}a_{i}:=\prod_{i=1}^{n}a_{\phi(i)}.
$$  

The commutativity of multiplication implies that the definition in (3.16c) is actually independent of the chosen bijective map. $\phi$ (cf. Th. B.4 in the Appendix); however,. we will see later that, for a general multiplication on a set. $A$ , commutativity will not always hold (an important example will be matrix multiplication), and, in that case, the definition in (3.16c) does, in general, depend on the chosen bijective map $\phi$ . Also define  

$$
\prod_{i\in\emptyset}a_{i}:=1
$$  

(for a general $A$ $1$ is meant to be an element such that $a\cdot1=1\cdot a=a$ for each $a\in A$ and we can even define this if $1\not\in A$  

Example 3.9. As an (academic) example, where, in each step, the recursive definition does depend on all previously computed values, consider the sequence $(x_{n})_{n\in\mathbb{N}}$ , defined by  

$$
x_{1}:=1,\quad\forall_{n\in\mathbb{N}}\quad x_{n+1}:=\frac{1}{n}\prod_{i=1}^{n}x_{i},
$$  

i.e. by setting $A:=\mathbb{N}$ and  

$$
f_{n}:A^{n}\longrightarrow A,\quad f_{n}(x_{1},\dots,x_{n}):={\frac{1}{n}}\prod_{i=1}^{n}x_{i}.
$$  

One obtains  

$$
\begin{array}{l}{{x_{1}=1,\quad x_{2}=f_{1}(1)=1,\quad x_{3}=f_{2}(1,1)=\displaystyle\frac{1}{2},\quad x_{4}=f_{3}\left(1,1,\displaystyle\frac{1}{2}\right)=\displaystyle\frac{1}{6},}}\ {{\qquadx_{5}=f_{4}\left(1,1,\displaystyle\frac{1}{2},\displaystyle\frac{1}{6}\right)=\displaystyle\frac{1}{48},\quad x_{6}=f_{5}\left(1,1,\displaystyle\frac{1}{2},\displaystyle\frac{1}{6},\displaystyle\frac{1}{48}\right)=\displaystyle\frac{1}{2880},\quad\cdots}}\end{array}
$$  

In the above recursive definitions, we have always explicitly specified $A$ and the $g_{n}$ or $f_{n}$ . However, in the literature as well as in the rest of this class, most of the time, the $g_{n}$ or $f_{n}$ are not provided explicitly.  

### 3.2 Cardinality: The Size of Sets  

Cardinality measures the size of sets. For a finite set $A$ , it is precisely the number of elements in $A$ . For an infinite set, it classifies the set's degree or level of infinity (it turns out that not all infinite sets have the same size).  

#### 3.2.1 Definition and General Properties  

Definition 3.10. (a) The sets. $A,B$ are defined to have the same cardinality or the. same size if, and only if, there exists a bijective map. $\varphi:A\longrightarrow B$ .According to Th. 3.11 below, this defines an equivalence relation on every set of sets.  

(b) The cardinality of a set $A$ is $n\in\mathbb{N}$ (denoted $\#A=n$ ) if, and only if, there exists a bijective map $\varphi:A\longrightarrow\{1,\dots,n\}$ .The cardinality of $\varnothing$ is defined as 0, i.e. $\#\emptyset:=0$ .A set $A$ is called finite if, and only if, there exists $n\in\ensuremath{\mathbb{N}}_{0}$ such that $\#A=n$ $A$ is called infinite if, and only if,. $A$ is not finite, denoted $\#A=\infty$ (in the strict sense, this is an abuse of notation, since. $\infty$ is not a cardinality - for example $\#\mathbb{N}=\infty$ and $\#\mathcal{P}(\mathbb{N})=\infty$ , but $\mathbb{N}$ and $\mathcal{P}(\mathbb{N})$ do not have the same cardinality, since the power set $\mathcal{P}(A)$ is always strictly bigger than $A$ (see Th. 3.16 below) $-\#A=\infty$ is merely an abbreviation for the statement $A$ is infinite"). The interested student finds additional material regarding characterizations of infinite sets in Th. A.54 of the Appendix.  

(c) The set $A$ is called countable if, and only if, $A$ is finite or. $A$ has the same cardinality as $\mathbb{N}$ . Otherwise,. $A$ is called uncountable.  

Theorem 3.11. Let $\mathcal{M}$ be a set of sets. Then the relation $\sim$ on $\mathcal{M}$ , defined by.  

$A\sim B:\Leftrightarrow A$ and $B$ have the same cardinality, constitutes an equivalence relation on $\mathcal{M}$  

Proof. According to Def. 2.32, we have to prove that $\sim$ is reflexive, symmetric, and. transitive. According to Def. 3.10(a), $A\sim B$ holds for $A,B\in{\mathcal{M}}$ if, and only if, there exists a bijective map $f:A\longrightarrow B$ . Thus, since the identity Ic. ${\mathrm{l~}}\colon A\longrightarrow A$ is bijective, $A\sim A$ , showing $\sim$ is reflexive. If. $A\sim B$ , then there exists a bijective map. $f:A\longrightarrow B$ and $f^{-1}$ is a bijective map. $f^{-1}:B\longrightarrow A$ , showing $B\sim A$ and that $\sim$ is symmetric. If $A\sim B$ and $B\sim C$ , then there are bijective maps. $f:A\longrightarrow B$ and $g:B\longrightarrow C$ Then, according to Th. 2.14, the composition $(g\circ f):A\longrightarrow C$ is also bijective, provinge $A\sim C$ and that $\sim$ is transitive.  

Theorem 3.12 (Schroder-Bernstein). Let $A,B$ be sets. The following statements are equivalent (even without assuming the axiom of choice):  

(i) The sets $A$ and $B$ have the same cardinality (i.e. there exists a bijective map $\phi:A\longrightarrow B$  

(ii) There exist an injective map $f:A\longrightarrow B$ and an injective map $g:B\longrightarrow A$  

We will base the proof of the Schroder-Bernstein theorem on the following lemma (for an alternative proof, see [Phi16, Th. A.56]):  

Lemma 3.13. Let $A$ be a set.Consider. $\mathcal{P}(A)$ to be endowed with the partial order. given by set inclusion, i.e., for each. $X,Y\in{\mathcal{P}}(A)$ $X\le Y$ if, and only if,. $X\subseteq Y$ .If $F:{\mathcal{P}}(A)\longrightarrow{\mathcal{P}}(A)$ is isotone with respect to that order, then $F$ has a fixed point, i.e.. $F(X_{0})=X_{0}$ for some $X_{0}\in{\mathcal{P}}(A)$  

Proof. Define  

$$
\mathcal A:=\{X\in\mathcal P(A):F(X)\subseteq X\},\quad X_{0}:=\bigcap_{X\in\mathcal A}X
$$  

$X_{0}$ is well-defined, since $F(A)\subseteq A$ ). Suppose $X\in{\mathcal{A}}$ , i.e. $F(X)\subseteq X$ and $X_{0}\subseteq X$ Then $F(X_{0})\subseteq F(X)\subseteq X$ due to the isotonicity of $F^{\prime}$ .Thus, $F(X_{0})\subseteq X$ for every $X\in{\mathcal{A}}$ , i.e. $F(X_{0})\subseteq X_{0}$ . Using the isotonicity of $F$ again shows $F(F(X_{0}))\subseteq F(X_{0})$ implying $F(X_{0})\in{\mathcal{A}}$ and $X_{0}\subseteq F(X_{0})$ , i.e. $F(X_{0})=X_{0}$ as desired.  

Proof of Th. 3.12. (i) trivially implies (ii), as one can simply set $f:=\phi$ and $g:=\phi^{-1}$ It remains to show (ii) implies (i). Thus, let $f:A\longrightarrow B$ and $g:B\longrightarrow A$ be injective. To apply Lem. 3.13, define.  

$$
F:{\mathcal{P}}(A)\longrightarrow{\mathcal{P}}(A),\quad F(X):=A\setminus g{\big(}B\setminus f(X){\big)},
$$  

and note  

$$
\begin{array}{r l}{X\subseteq Y\subseteq A\Rightarrow f(X)\subseteq f(Y)\Rightarrow B\setminus f(Y)\subseteq B\setminus f(X)}\ {\Rightarrow g\big(B\setminus f(Y)\big)\subseteq g\big(B\setminus f(X)\big)\Rightarrow F(X)\subseteq F(Y).}\end{array}
$$  

Thus, by Lem. 3.13, $F^{\prime}$ has a fixed point $X_{0}$ . We claim that a bijection is obtained via setting  

$$
\phi:A\longrightarrow B,\quad\phi(x):={\left\{\begin{array}{l l}{f(x)}&{{\mathrm{for~}}x\in X_{0},}\ {g^{-1}(x)}&{{\mathrm{for~}}x\not\in X_{0}.}\end{array}\right.}
$$  

First, $\phi$ is well-defined, since $x\notin{X_{0}}=F(X_{0})$ implies $x\in g\big(B\setminus f(X_{0})\big)$ . To verify that $\phi$ is injective, let $x,y\in A$ $x\ne y$ .If $x,y\in X_{0}$ , then $\phi(x)~\neq~\phi(y)$ , as $f$ is injective. If $x,y\in A\setminus X_{0}$ , then $\phi(x)\neq\phi(y)$ , as $g^{-1}$ is well-defined. If $x\in X_{0}$ and $y\notin X_{0}$ , then $\phi(x)\in f(X_{0})$ and $\phi(y)\in B\setminus f(X_{0})$ , once again, implying $\phi(x)\neq\phi(y)$ . If remains to prove surjectivity. If $b\in f(X_{0})$ , then $\phi(f^{-1}(b))=b$ . If $b\in B\setminus f(X_{0})$ , then $g(b)\notin X_{0}=F(X_{0})$ , i.e. $\phi(g(b))=b$ , showing $\phi$ to be surjective.  

Theorem 3.14. Let $A,B$ be nonempty sets. Then the following statements are equivalent (where the implication ${}^{66}(\mathrm{ii})\Rightarrow(\mathrm{i}){}^{,}$ makes use of the axiom of choice $(A C)$  

(i) There exists an injective map $f:A\longrightarrow B$ (ii) There exists a surjective map. $g:B\longrightarrow A$  

Proof. According to Th. 2.13(b), (i) is equivalent to $f$ having a left inverse $g:B\longrightarrow A$ (i.e. $g\circ f=\operatorname{Id}_{A}$ ), which is equivalent to $g$ having a right inverse, which, according to Th. 2.13(a), is equivalent to (ii) (AC is used in the proof of Th. 2.13(a) to show each surjective map has a right inverse).  

Corollary 3.15. Let $A,B$ be nonempty sets. Using AC, we can expand the two equivalent statements of Th. 3.12 to the following list of equivalent statements:  

(i) The sets $A$ and $B$ have the same cardinality (i.e. there exists a bijective map $\phi:A\longrightarrow B$ (ii) There exist an injective map $f:A\longrightarrow B$ and an injective map. $g:B\longrightarrow A$ (ii) There exist a surjective map $f:A\longrightarrow B$ and a surjective map. $g:B\longrightarrow A$ (iv) There exist an injective map $f_{1}:A\longrightarrow B$ and a surjective map. $f_{2}:A\longrightarrow B$ (v) There exist an injective map $g_{1}:B\longrightarrow A$ and a surjective map. $g_{2}:B\longrightarrow A$  

Proof. The equivalences are an immediate consequence of combining Th. 3.12 with Th.   
3.14.  

Theorem 3.16. Let $A$ be a set. There can never exist a surjective map from $A$ onto $\mathcal{P}(A)$ (in this sense, the size of. $\mathcal{P}(A)$ is always strictly bigger than the size of. $A$ ; in particular, $A$ and $\mathcal{P}(A)$ can never have the same size)..  

Proof. If $A~=~\emptyset$ , then there is nothing to prove. For nonempty. $A$ , the idea is to. conduct a proof by contradiction. To this end, assume there does exist a surjective map $f:A\longrightarrow{\mathcal{P}}(A)$ and define  

$$
B:=\{x\in A:x\not\in f(x)\}.
$$  

Now $B$ is a subset of $A$ , i.e. $B\in{\mathcal{P}}(A)$ and the assumption that. $f$ is surjective implies the existence of $a\in A$ such that $f(a)=B$ . If $a\in B$ , then $a\not\in f(a)=B$ , i.e. $a\in B$ implies $a\in B\land\neg(a\in B)$ , so that the principle of contradiction tells us. $a\notin B$ must be true. However, $a\notin B$ implies $a\in f(a)=B$ , i.e., this time, the principle of contradiction. tells us $a\in B$ must be true. In conclusion, we have shown our original assumption that there exists a surjective map. $f:A\longrightarrow{\mathcal{P}}(A)$ implies $a\in B\land\neg(a\in B)$ , i.e., according to the principle of contradiction, no surjective map from $A$ into $\mathcal{P}(A)$ can exist.  

#### 3.2.2 Finite Sets  

While many results concerning cardinalities of finite sets seem intuitively clear, as a. mathematician, one still has to provide a rigorous proof. Providing such proofs in the present section also provides us with the opportunity to see more examples of induction proofs. We begin by showing finite cardinalities to be uniquely determined. The key is. the following theorem:  

Theorem 3.17. If $m,n\in\mathbb{N}$ and the map. $f:\{1,\dots,m\}\longrightarrow\{1,\dots,n\}$ is bijective,. then $m=n$  

Proof. We conduct the proof via induction on $m$  

Base Case ( $m=1$ ): If $m=1$ , then the surjectivity of $f$ implies $n=1$ Induction Step: Let $m>1$ . From the bijective map $f$ , we define the map  

$$
g:\{1,\ldots,m\}\longrightarrow\{1,\ldots,n\},\quad g(x):=\left\{{n\atop f(m)}\quad{\mathrm{for~}}x=f^{-1}(n),\atop{\mathrm{fotherwise}.}\right.
$$  

Then $g$ is bijective, since it is the composition $g=h\circ f$ of the bijective map $f$ with the bijective map  

$$
h:\{f(m),n\}\longrightarrow\{f(m),n\},\quad h(f(m)):=n,\quad h(n):=f(m).
$$  

Thus, the restriction $g\lceil_{\left\{1,\ldots,m-1\right\}}$ $\{1,\dots,m{-}1\}\longrightarrow\{1,\dots,n{-}1\}$ must also be bijective, such that the induction hypothesis yields $m-1=n-1$ , which, in turn, implies $r n=n$ as desired.  

Corollary 3.18. Let $m,n\in\mathbb{N}$ and let $A$ be a set. If. $\#A=m$ and $\#A=n$ , then $m=n$  

Proof. If $\#A=m$ , then, according to Def. 3.10(b), there exists a bijective map $f:$ $A\longrightarrow\{1,\ldots,m\}$ .Analogously, if. $\#A=n$ , then there exists a bijective map $\textit{g}:$ $A\longrightarrow\{1,\dots,n\}$ . In consequence, we have the bijective map $(g\circ f^{-1}):\{1,\dots,m\}\longrightarrow$ $\{1,\ldots,n\}$ , such that Th. 3.17 yields. $m=n$  

Theorem 3.19. Let $A\neq\emptyset$ be a finite set..  

(a) If $B\subseteq A$ with $A\neq B$ , then $B$ is finite with $\#B<\#A$ (b) If $a\in A$ , then $\#(A\setminus\{a\})=\#A-1$  

Proof. For $\#A=n\in\mathbb{N}$ , we use induction to prove (a) and (b) simultaneously, i.e. we show  

$$
\mathbf{\Sigma}_{\mathrm{{N}}}^{\prime}\left(\#A=n\Rightarrow\underset{B\in\mathcal{P}(A)\setminus\{A\}}{\forall}\underset{a\in A}{\forall}\#B\in\{0,\ldots,n-1\}\land\#\big(A\setminus\{a\}\big)=n-1\right).
$$  

Base Case ( $n=1$ ): In this case,. $A$ has precisely one element, i.e. $B=A\setminus\{a\}=\emptyset$ , and $\#\emptyset=0=n-1$ proves $\phi(1)$  

Induction Step: For the induction hypothesis, we assume $\phi(n)$ to be true, i.e. we assume. (a) and (b) hold for each. $A$ with $\#A=n$ . We have to prove. $\phi(n+1)$ , i.e., we consider. $A$ with $\#A=n+1$ . From $\#A=n+1$ , we conclude the existence of a bijective map $\varphi:$ $A\longrightarrow\{1,\dots,n+1\}$ . We have to construct a bijective map $\psi:A\setminus\{a\}\longrightarrow\{1,\dots,n\}$ To this end, set $k:=\varphi(a)$ and define the auxiliary function.  

$$
f:\{1,\ldots,n+1\}\longrightarrow\{1,\ldots,n+1\},\quad f(x):={\left\{\begin{array}{l l}{n+1}&{{\mathrm{for~}}x=k,}\ {k}&{{\mathrm{for~}}x=n+1,}\ {x}&{{\mathrm{for~}}x\not\in\{k,n+1\}.}\end{array}\right.}
$$  

Then $f\circ\varphi:A\longrightarrow\{1,\dots,n+1\}$ is bijective by Th. 2.14, and  

$$
(f\circ\varphi)(a)=f(\varphi(a))=f(k)=n+1.
$$  

Thus, the restriction $\psi:=(f\circ\varphi)\upharpoon_{A\setminus\{a\}}$ is the desired bijective map. $\psi:A\backslash\{a\}\rightarrow$ $\{1,\ldots,n\}$ , proving $\#(A\setminus\{a\})=n$ . It remains to consider the strict subset $B$ of $A$ Since $B$ is a strict subset of. $A$ , there exists $a\in A\setminus B$ .Thus, $B\subseteq A\setminus\{a\}$ and, as we have already shown. $\#(A\backslash\{a\})=n$ , the induction hypothesis applies and yields $B$ is finite with $\#B\leq\#(A\setminus\{a\})=n$ , i.e. $\#B\in\{0,\ldots,n\}$ , proving $\phi(n+1)$ , thereby completing the induction..  

Theorem 3.20. For $\#A=\#B=n\in\mathbb{N}$ and $f:A\longrightarrow B$ , the following statements are equivalent:  

(i) $f$ is injective.   
(ii) $f$ is surjective.   
(ii) $f$ is bijective.  

Proof. Exercise.  

Lemma 3.21. For each finite set $A$ (i.e. $\#A=n\in\mathbb{N}_{0} $ ) and each $B\subseteq A$ , one has. $\#(A\setminus B)=\#A-\#B$  

Proof. For $B=\emptyset$ , the assertion is true since $\#(A\setminus B)=\#A=\#A-0=\#A-\#B$  

For $B\neq\emptyset$ , the proof is conducted over the size of $B$ , i.e. as a finite induction (cf. Cor.. 3.6) over the set $\{1,\ldots,n\}$ , showing  

$$
\stackrel{\forall}{m}\in\{1,...,n\}\underbrace{\left(\#B=m\Rightarrow\#(A\setminus B)=\#A-\#B\right)}_{\phi(m)}.
$$  

Base Case ( $m=1$ ): $\phi(1)$ is precisely the statement provided by Th. 3.19(b).  

Induction Step: For the induction hypothesis, we assume $\phi(m)$ with $1\leq m<n$ .To prove $\phi(m+1)$ , consider $B\subseteq A$ with $\#B=m+1$ .Fix an element $b\in B$ and set $B_{1}:=B\setminus\{b\}$ . Then $\#B_{1}=m$ by Th. 3.19(b), $A\setminus B=(A\setminus B_{1})\setminus\{b\}$ , and we compute  

$$
{\begin{array}{r l}&{\#(A\setminus B)=\#{\big(}(A\setminus B_{1})\setminus\{b\}{\big)}\stackrel{\mathrm{Th.3.1}9(\mathrm{b})}{=}\#(A\setminus B_{1})-1\stackrel{{\binom{{\phi}(m)}{}}}{=}\#A-\#B_{1}-1}\ &{\qquad=\#A-\#B,}\end{array}}
$$  

proving $\phi(m+1)$ and completing the induction.  

Theorem 3.22. If $A,B$ are finite sets, then $\#(A\cup B)=\#A+\#B-\#(A\cap B).$  

Proof. The assertion is clearly true if $A$ or $B$ is empty. If $A$ and $B$ are nonempty, then there exist $m,n\in\mathbb{N}$ such that $\#A=m$ and $\#B=n$ , i.e. there are bijective maps $f:A\longrightarrow\{1,\dots,m\}$ and $g:B\longrightarrow\{1,\dots,n\}$  

We first consider the case. $A\cap B=\emptyset$ . We need to construct a bijective map $h:A\cup B\longrightarrow$ $\{1,\dots,m+n\}$ . To this end, we define.  

$$
h:A\cup B\longrightarrow\{1,\ldots,m+n\},\quad h(x):={\left\{\begin{array}{l l}{f(x)}&{{\mathrm{for~}}x\in A,}\ {g(x)+m}&{{\mathrm{for~}}x\in B.}\end{array}\right.}
$$  

The bijectivity of $f$ and $g$ clearly implies the bijectivity of $h$ , proving $\#(A\cup B)=$ $m+n=\#A+\#B$  

Finally, we consider the case of arbitrary. $A,B$ . Since $A\cup B=A\cup(B\setminus A)$ and $B\backslash A=$ $B\setminus(A\cap B)$ , we can compute  

$$
\begin{array}{r l}&{\#(A\cup B)=\#\big(A\cup(B\setminus A)\big)=\#A+\#(B\setminus A)}\ &{\qquad=\#A+\#\big(B\setminus(A\cap B)\big)\stackrel{\mathrm{Lem.}3.21}{=}\#A+\#B-\#(A\cap B),}\end{array}
$$  

thereby establishing the case.  

Theorem 3.23. If $(A_{1},\ldots,A_{n})$ $n\in\mathbb N$ , is a finite sequence of finite sets, then  

$$
\#\prod_{i=1}^{n}A_{i}=\#{\bigl(}A_{1}\times\cdots\times A_{n}{\bigr)}=\prod_{i=1}^{n}\#A_{i}.
$$  

Proof. If at least one. $A_{i}$ is empty, then (3.17) is true, since both sides are $0$  

The case where all $A_{i}$ are nonempty is proved by induction over $n$ , i.e. we know $k_{i}:=$ $\#A_{i}\in\mathbb{N}$ for each $i\in\{1,\ldots,n\}$ and show by induction  

$$
\underbrace{\forall}_{n\in\mathbb{N}}\underbrace{\#\prod_{i=1}^{n}A_{i}}_{\phi(n)}=\prod_{i=1}^{n}k_{i}.
$$  

Base Case ( $n=1$ ): $\begin{array}{r}{\prod_{i=1}^{1}A_{i}=\#A_{1}=k_{1}=\prod_{i=1}^{1}k_{i}}\end{array}$ , i.e. $\phi(1)$ holds.  

Induction Step: From the induction hypothesis $\phi(n)$ , we obtain a bijective map $\varphi:$ $A\longrightarrow\{1,\dots\cdot,N\}$ , where $\textstyle A:=\prod_{i=1}^{n}A_{i}$ and $\textstyle N:=\prod_{i=1}^{n}k_{i}$ . To prove $\phi(n+1)$ , we need to construct a bijective map $h:A\times A_{n+1}\longrightarrow\{1,\dots,N\cdot k_{n+1}\}$ . Since $\#A_{n+1}=k_{n+1}$ there exists a bijective map $f:A_{n+1}\longrightarrow\{1,\dots,k_{n+1}\}$ . We define  

$$
\begin{array}{c}{{h:A\times A_{n+1}\longrightarrow\{1,\dots,N\cdot k_{n+1}\},}}\ {{\qquad}}\ {{h(a_{1},\dots,a_{n},a_{n+1}):=\bigl(f(a_{n+1})-1\bigr)\cdot N+\varphi(a_{1},\dots,a_{n}).}}\end{array}
$$  

Since $\varphi$ and $f$ are bijective, and since every $m\in\{1,\ldots,N\cdot k_{n+1}\}$ has a unique representation in the form $m=a\cdot N+r$ with $a\in\{0,\ldots,k_{n+1}-1\}$ and $r\in\{1,\ldots,N\}$ (see Th. D.1 in the Appendix), $h$ is also bijective. This proves $\phi(n+1)$ and completes the induction.  

Theorem 3.24. For each finite set $A$ with $\#A=n\in\mathbb{N}_{0}$ , one has. $\#{\mathcal{P}}(A)=2^{n}$  

Proof. The proof is conducted by induction by showing  

$$
\forall_{n\in\mathbb{N}_{0}}\underbrace{\left(\#A=n\Rightarrow\#\mathcal{P}(A)=2^{n}\right)}_{\phi(n)}.
$$  

Base Case ( $n=0$ ): For $n=0$ , we have $A=\emptyset$ , i.e. ${\mathcal{P}}(A)=\{\emptyset\}$ . Thus, $\#\mathcal{P}(A)=1=2^{0}$ proving $\phi(0)$  

Induction Step: Assume $\phi(n)$ and consider $A$ with $\#A=n+1$ . Then $A$ contains at least one element $a$ . For $B:=A\setminus\{a\}$ , we then know $\#B=n$ from Th. 3.19(b). Moreover, setting ${\mathcal{M}}:=\left\{C\cup\{a\}:C\in{\mathcal{P}}(B)\right\}$ , we have the disjoint decomposition $\mathcal{P}(A)=\mathcal{P}(B)\cup\mathcal{M}$ . As the map $\varphi:\mathcal{P}(B)\longrightarrow\mathcal{M}$ $\varphi(C):=C\cup\{a\}$ , is clearly bijective, $\mathcal{P}(B)$ and $\mathcal{M}$ have the same cardinality. Thus,  

$$
\#\mathcal{P}(A)\stackrel{\mathrm{Th}.3.22}{=}\#\mathcal{P}(B)+\#\mathcal{M}=\#\mathcal{P}(B)+\#\mathcal{P}(B)\stackrel{\left(\phi(n)\right)}{=}2\cdot2^{n}=2^{n+1},
$$  

thereby proving $\phi(n+1)$ and completing the induction.  

#### 3.2.3 Countable Sets  

In this section, we present a number of important results regarding the natural numbers and countability.  

Theorem 3.25. (a) Every nonempty finite subset of a totally ordered set has a minimum and a maximum.  

(b) Every nonempty subset of N has a minimum.  

Proof. Exercise.  

Proposition 3.26. Every subset A of $\mathbb{N}$ is countable.  

Proof. Since $\varnothing$ is countable, we may assume. $A\neq\emptyset$ . From Th. 3.25(b), we know that. every nonempty subset of. $\mathbb{N}$ has a min. We recursively define a sequence in $A$ by  

$$
a_{1}:=\operatorname*{min}A,\quad a_{n+1}:={\left\{\begin{array}{l l}{\operatorname*{min}A_{n}}&{{\mathrm{if~}}A_{n}:=A\setminus\{a_{i}:1\leq i\leq n\}\neq\varnothing,}\ {a_{n}}&{{\mathrm{if~}}A_{n}=\varnothing.}\end{array}\right.}
$$  

This sequence is the same as the function $f:\mathbb{N}\longrightarrow A$ $f(n)=a_{n}$ . An easy induction. shows that, for each $n\in\mathbb{N}$ $a_{n}\neq a_{n+1}$ implies the restriction $f\mid_{\{1,\ldots,n+1\}}$ is injective. Thus, if there exists. $n\in\mathbb{N}$ such that $u_{n}=u_{n+1}$ , then $f\mid_{\{1,...,k\}}$ .. $\{1,\dots,k\}\longrightarrow A$ is bijective, where $k:=\operatorname*{min}\{n\in\mathbb{N}:a_{n}=a_{n+1}\}$ , showing $A$ is finite, i.e. countable. If. there does not exist $n\in\mathbb N$ with $u_{n}=u_{n+1}$ , then $f$ is injective. Another easy induction shows that, for each. $n\in\mathbb{N}$ $f(\{1,\dots,n\})~{\supseteq}~\{k~\in~A~:~k~\leq~n\}$ , showing $f$ is also surjective, proving. $A$ is countable.  

Proposition 3.27. For each set. $A\neq\emptyset$ , the following three statements are equivalent:  

(i) A is countable. (ii) There exists an injective map $f:A\longrightarrow\mathbb{N}$ (iii) There exists a surjective map $g:\mathbb{N}\longrightarrow A$  

Proof. Directly from the definition of countable in Def. 3.10(c), one obtains (i)=>(ii) and (i)=>(iii). To prove (ii)=>(i), let $f:A\longrightarrow\mathbb{N}$ be injective. Then $f:A\longrightarrow f(A)$ is bijective, and, since. $f(A)\subseteq\mathbb{N}$ $f(A)$ is countable by Prop. 3.26, proving $A$ is countable as well. To prove (iii). $\Rightarrow$ (i), let $g:\mathbb{N}\longrightarrow A$ be surjective. Then. $g$ has a right inverse $f:A\longrightarrow\mathbb{N}$ . One can obtain this from Th. 2.13(a), but, here, we can actually construct $f$ without the axiom of choice: For $a\in A$ , let $f(a):=\operatorname*{min}g^{-1}(\{a\})$ (recall Th. 3.25(b)). Then, clearly, $g\circ f=\operatorname{Id}_{A}$ . But this means $g$ is a left inverse for. $f$ , showing $f$ is injective according to Th. 2.13(b). Then $A$ is countable by an application of (ii).  

Theorem 3.28. If $(A_{1},\ldots,A_{n})$ $n\in\mathbb N$ , is a finite family of countable sets, then $\textstyle\prod_{i=1}^{n}A_{i}$ is countable.  

Proof. We first consider the special case $n=2$ with $A_{1}=A_{2}=\mathbb{N}$ and show the map.  

$$
\varphi:\mathbb{N}\times\mathbb{N}\longrightarrow\mathbb{N},\quad\varphi(m,n):=2^{m}\cdot3^{n},
$$  

is injective: If $\varphi(m,n)=\varphi(p,q)$ , then $2^{m}\cdot3^{n}=2^{p}\cdot3^{q}$ . Moreover $m\leq p$ or $p\leq m$ If $m\leq p$ , then $3^{n}=2^{p-m}\cdot3^{q}$ . Since $3^{n}$ is odd, $2^{p-m}\cdot3^{q}$ must also be odd, implying $p-m=0$ , i.e. $\mathit{m}=\mathit{p}$ .Moreover, we now have $3^{n}=3^{q}$ , implying $n=q$ , showing $(m,n)=(p,q)$ , i.e. $\varphi$ is injective.  

We now come back to the general case stated in the theorem. If at least one of the $A_{i}$ is empty, then $A$ is empty. So it remains to consider the case, where all. $A_{i}$ are nonempty. The proof is conducted by induction by showing.  

Base Case ( $n=1$ ): $\phi(1)$ is merely the hypothesis that $A_{1}$ is countable.  

Induction Step: Assuming. $\phi(n)$ , Prop. 3.27(ii) provides injective maps $f_{1}:\textstyle\prod_{i=1}^{n}A_{i}\longrightarrow$ $\mathbb{N}$ and $f_{2}:A_{n+1}\longrightarrow\mathbb{N}$ . To prove $\phi(n+1)$ , we provide an injective map. $h:\Pi_{i=1}^{n+1}A_{i}\longrightarrow$ N: Define  

$$
h:\prod_{i=1}^{n+1}A_{i}\longrightarrow\mathbb{N},\quad h(a_{1},\ldots,a_{n},a_{n+1}):=\varphi{\big(}f_{1}(a_{1},\ldots,a_{n}),f_{2}(a_{n+1}){\big)}.
$$  

The injectivity of. $f_{1},f_{2}$ , and $\varphi$ clearly implies the injectivity of $h$ , thereby proving $\phi(n+1)$ and completing the induction.  

Theorem 3.29. If. $(A_{i})_{i\in I}$ is a countable family of countable sets (i.e. $\emptyset\neq I$ is countable and each $A_{i}$ $i\in I$ , is countable), then the union. $\textstyle A:=\bigcup_{i\in I}A_{i}$ is also countable (this result makes use of $A C$ ,cf. Rem. 3.30 below).  

Proof. It suffices to consider the case that all $A_{i}$ are nonempty. Moreover, according to. Prop. 3.27(iii), it suffices to construct a surjective map $\varphi:\mathbb{N}\longrightarrow A$ . Also according to Prop. 3.27(iii), the countability of. $I$ and the $A_{i}$ provides us with surjective maps. $f:\mathbb{N}\longrightarrow I$ and $g_{i}:\mathbb{N}\longrightarrow A_{i}$ (here AC is used to select each. $g_{i}$ from the set of all surjective maps from N onto $A_{i}$ ). Define  

$$
F:\mathbb{N}\times\mathbb{N}\longrightarrow A,\quad F(m,n):=g_{f(m)}(n).
$$  

Then $F^{\prime}$ is surjective: Given $x\in A$ , there exists $i\in I$ such that $x\in A_{i}$ . Since $f$ is surjective, there is $m\in\mathbb{N}$ satisfying $f(m)=i$ . Moreover, since $g_{i}$ is surjective, there exists $n\in\mathbb N$ with $g_{i}(n)=x$ . Then $F(m,n)=g_{i}(n)=x$ , verifying that $F^{\prime}$ is surjective. As $\mathbb{N}\times\mathbb{N}$ is countable by Th. 3.28, there exists a surjective map $h:\mathbb{N}\longrightarrow\mathbb{N}\times\mathbb{N}$ . Thus, $F\circ h$ is the desired surjective map from. $\mathbb{N}$ onto $A$  

Remark 3.30. The axiom of choice is, indeed, essential for the proof of Th. 3.29. It is shown in [Jec73, Th. 10.6] that it is consistent with the axioms of ZF (i.e. with the axioms of Sec. A.3 of the Appendix) that, e.g., the uncountable sets. $\mathcal{P}(\mathbb{N})$ and $\mathbb{R}$ (cf. [Phi16, Th. F.2]) are countable unions of countable sets..  

## 4 Basic Algebraic Structures  

We are now in a position to conduct some actual algebra, that means we will start to study sets $A$ that come with a composition law $\circ:A\times A\longrightarrow A$ $(a,b)\mapsto a\circ b$ , assumed to satisfy a number of rules, so-called axioms. One goal is to prove further rules as a consequence of the axioms. A main benefit of this method is the fact that these proved rules are then known to hold in every structure, satisfying the axioms. Perhaps the most simple structure that still occurs in a vast number of interesting places throughout mathematics is that of a group (see Def. 4.5(b) below), examples including the set of real numbers $\mathbb{R}$ with the usual addition as well as. $\mathbb{R}\setminus\{0\}$ with the usual multiplication. So every rule we will prove as a consequence of the group axioms will hold in these two. groups as well as in countless other groups. We note that vector spaces, the structures. of central interest to linear algebra, are, in particular, always groups, so that everything. we prove about groups in the following is, in particular, true in every vector space.  

### 4.1 Magmas and Groups  

Definition 4.1. Let. $A$ be a nonempty set. A map  

$$
\circ:A\times A\longrightarrow A,\quad(x,y)\mapsto x\circ y,
$$  

is called a composition on $A$ ; the pair. $(A,\circ)$ is then called a magma. It is also common to call a composition a multiplication and to write $x\cdot y$ or just $x y$ instead of. $x\circ y$ . In this situation, the product symbol $\prod$ is defined as in Ex. 3.8(c). If the composition is called an addition and $x+y$ is written instead of $x\circ y$ , then it is assumed that it is commutative, that means it satisfies the law of Def. 4.2(a) below (a multiplication might or might now satisfy commutativity). For an addition, the summation symbol $\displaystyle\sum$ is defined as in Ex. 3.8(b).  

#### Definition 4.2. Let $(A,\circ)$ be a magma.  

(a) $\cup$ is called commutative or abelian if, and only if, $x\circ y=y\circ x$ holds for all $x,y\in A$ (b) $\cup$ is called associative if, and only if, $x\circ(y\circ z)=(x\circ y)\circ z$ holds for all $x,y,z\in A$ (c) An element $e\in A$ is called left neutral (resp. right neutral) if, and only if,  

$$
\forall_{x\in A}\quad e\circ x=x\quad({\mathrm{resp.~}}x\circ e=x).
$$  

$e\in A$ is called neutral if, and only if, it is both left neutral and right neutral.  

If associativity holds for each triple of elements, then it also holds for each finite tuple. of elements; if the composition is associative and commutativity holds for each pair of. elements, then it also holds for each finite tuple of elements (see Th. B.3 and Th. B.4 in the Appendix).  

Lemma 4.3. Let $(A,\circ)$ be a magma with $l,r\in A$ .If $l$ is left neutral and. $r$ is right neutral, then $l=r$ (in particular, $A$ contains at most one neutral element).  

Proof. As. $l$ is left neutral and. $r$ is right neutral, we obtain $r=l\circ r=l$  

Notation 4.4. If a composition on a set $A$ is written as a multiplication :, then it is common to write a neutral element as 1 and to also call it a unit or one. If a (commutative) composition on a set $A$ is written as an addition $^+$ , then it is common to write a neutral element as O and to also call it zero.  

Definition 4.5. Let $(A,\circ)$ be a magma.  

(a) $(A,\circ)$ is called a semigroup if, and only if, $\cup$ is associative.  

(b) $(A,\circ)$ is called a group if, and only if, it is a semigroup with the additional property that $A$ contains a right neutral $^4$ element $e\in A$ and, for each $x\in A$ , there exists an inverse element ${\overline{{x}}}\in A$ , i.e. an element ${\overline{{x}}}\in A$ such that  

$$
x\circ{\overline{{x}}}=e.
$$  

A group is called commutative or abelian if, and only if, $\cup$ is commutative.  

Before considering examples of magmas $(A,\circ)$ in Ex. 4.9 below, we prove some first rules and introduce some more notation.  

Theorem 4.6. Let $(G,\circ)$ be a group with right neutral element $e\in G$ .Then the following statements and rules are valid in $G$  

(a) e is a neutral element (thus, in particular, it is uniquely determined according to Lem. 4.3).  

(b) If $x,a\in G$ , then $x\circ a=e$ if, and only if,. $a\circ x=e$ (i.e. an element is right inverse. if, and only if, it is left inverse). Moreover, inverse elements are unique (for each $x\in G$ , the unique inverse is then denoted by $x^{-1}$  

(c) $(x^{-1})^{-1}=x$ holds for each $x\in G$  

(d) $y^{-1}\circ x^{-1}=(x\circ y)^{-1}$ holds for each $x,y\in G$  

(e) Cancellation Laws: For each $x,y,a\in G$ , one has.  

$$
\begin{array}{r}{x\circ a=y\circ a\Rightarrow x=y,}\ {a\circ x=a\circ y\Rightarrow x=y.}\end{array}
$$  

Proof. (a): Let $x\in G$ .By Def. 4.5(b), there exists $y\in G$ such that $x\cup y=e$ and, in turn, $z\in G$ such that $y\circ z=e$ . Thus, as $e$ is right neutral..  

$$
e\circ z=(x\circ y)\circ z=x\circ(y\circ z)=x\circ e=x,
$$  

implying  

$$
x=e\circ z=(e\circ e)\circ z=e\circ(e\circ z)=e\circ x,
$$  

showing. $e$ to be left neutral as well.  

(b): To $a$ choose $b\in G$ such that $a\circ b=e$ . If $x\circ a=e$ , then  

$$
\begin{array}{l}{{e=a\circ b=(a\circ e)\circ b=(a\circ(x\circ a))\circ b=a\circ((x\circ a)\circ b)=a\circ(x\circ(a\circ b))}}\ {{\mathrm{~}=a\circ(x\circ e)=a\circ x.}}\end{array}
$$  

Interchanging the roles of $x$ and $a$ now proves the converse. To prove uniqueness, let $a,b$ be inverses to. $x$ . Then $a=a\circ e=a\circ x\circ b=e\circ b=b$  

(c): $\boldsymbol{x}^{-1}\circ\boldsymbol{x}=\boldsymbol{e}$ holds according to (b) and shows that $x$ is the inverse to $x^{-1}$ . Thus, $(x^{-1})^{-1}=x$ as claimed.  

(d) is due to $y^{-1}\circ x^{-1}\circ x\circ y=y^{-1}\circ e\circ y=e$  

(e): If $x\circ a=y\circ a$ , then $x=x\circ a\circ a^{-1}=y\circ a\circ a^{-1}=y$ as claimed; if $a\circ x=a\circ y$ then $x=a^{-1}\circ a\circ x=a^{-1}\circ a\circ y=y$ as well.  

Notation 4.7. Exponentiation with Integer Exponents: Let $(A,\cdot)$ be a magma with neutral element $1\in A$ . Define recursively for each $x\in A$ and each $n\in\ensuremath{\mathbb{N}}_{0}$  

$$
\begin{array}{r}{x^{0}:=1,\quad\forall\quad x^{n+1}:=x\cdot x^{n}.}\end{array}
$$  

Moreover, if $(A,\cdot)$ constitutes a group, then also define for each $x\in A$ and each $n\in\mathbb N$  

$$
x^{-n}:=(x^{-1})^{n}.
$$  

Theorem 4.8. Exponentiation Rules: Let $(G,\cdot)$ be a semigroup with neutral element $1\in G$ .Let $x,y\in G$ . Then the following rules hold for each $m,n\in\ensuremath{\mathbb{N}}_{0}$ .If $\left(G,\cdot\right)$ is $a$ group, then the rules even hold for every $m,n\in\mathbb{Z}$  

a) xm+n=xm.xn  

(b) $(x^{m})^{n}=x^{m n}$  

(c) If the composition is also commutative, then $x^{n}y^{n}=(x y)^{n}$  

Proof. (a): First, we fix. $n\in\ensuremath{\mathbb{N}}_{0}$ and prove the statement for each. $m\in\ensuremath{\mathbb{N}}_{0}$ by induction: The base case ( $m=0$ ) is $x^{n}=x^{n}$ , which is true. For the induction step, we compute  

$$
\boldsymbol{x}^{m+1+n}\stackrel{(4.5\mathrm{a})}{=}\boldsymbol{x}\cdot\boldsymbol{x}^{m+n}\stackrel{\mathrm{ind.}}{=}\boldsymbol{\stackrel{\mathrm{hyp.}}{x}}\boldsymbol{\cdot}\boldsymbol{x}^{m}\cdot\boldsymbol{x}^{n}\stackrel{(4.5\mathrm{a})}{=}\boldsymbol{x}^{m+1}\boldsymbol{x}^{n},
$$  

completing the induction step. Now assume $G$ to be a group. Consider $m\geq0$ and $n<0$ . If $m+n\geq0$ , then, using what we have already shown,  

$$
x^{m}x^{n}{\overset{(4.5\mathrm{b})}{=}}x^{m}(x^{-1})^{-n}=x^{m+n}x^{-n}(x^{-1})^{-n}=x^{m+n}.
$$  

Similarly, if $m+n<0$ , then  

$$
x^{m}x^{n}{\overset{(4.5{\mathrm{b}})}{=}}x^{m}(x^{-1})^{-n}=x^{m}(x^{-1})^{m}(x^{-1})^{-n-m}{\overset{(4.5{\mathrm{b}})}{=}}x^{m+n}.
$$  

The case $m<0$ $n\geq0$ is treated completely analogously. It just remains to consider $m<0$ and $n<0$ . In this case,  

$$
x^{m+n}=x^{-(-m-n)}{\overset{(4.5\mathrm{b})}{=}}(x^{-1})^{-m-n}=(x^{-1})^{-m}\cdot(x^{-1})^{-n}{\overset{(4.5\mathrm{b})}{=}}x^{m}\cdot x^{n}.
$$  

(b): First, we prove the statement for each $n\in\ensuremath{\mathbb{N}}_{0}$ by induction (for. $m<0$ , we assume $G$ to be a group): The base case ( $n=0$ ) is $(x^{m})^{0}=1=x^{0}$ , which is true. For the. induction step, we compute.  

$$
(x^{m})^{n+1}{\overset{(4.5\mathrm{a})}{=}}x^{m}\cdot(x^{m})^{n}{\overset{\mathrm{ind.}}{=}}{\overset{\mathrm{hyp.}}{=}}x^{m}\cdot x^{m n}{\overset{\mathrm{(a)}}{=}}x^{m n+m}=x^{m(n+1)},
$$  

completing the induction step. Now, let $G$ be a group and $n<0$ .We already know $(x^{m})^{-1}=x^{-m}$ . Thus, using what we have already shown,  

$$
(x^{m})^{n}{\overset{(4.5\mathrm{b})}{=}}\left((x^{m})^{-1}\right)^{-n}=(x^{-m})^{-n}=x^{(-m)(-n)}=x^{m n}.
$$  

(c): For $n\in\mathbb{N}_{0}$ , the statement is proved by induction: The base case ( $n=0$ ) is $x^{0}y^{0}=1=(x y)^{0}$ , which is true. For the induction step, we compute.  

$$
x^{n+1}y^{n+1}{\overset{(4.5\mathrm{a})}{=}}x\cdot x^{n}\cdot y\cdot y^{n}{\overset{\mathrm{ind.}}{=}}x y\cdot(x y){\overset{n}{=}}(x y)^{n+1},
$$  

completing the induction step. If $G$ is a group and. $n<0$ , then, using what we have.   
already shown,.  

$$
x^{n}y^{n}{\overset{(4.5{\mathrm{b}})}{=}}(x^{-1})^{-n}(y^{-1})^{-n}=(x^{-1}y^{-1})^{-n}{\overset{\mathrm{Th.}}{=}}{\overset{\mathrm{Th.}}{=}}(\left(x y\right)^{-1})^{-n}{\overset{(4.5{\mathrm{b}})}{=}}(x y)^{n},
$$  

which completes the proof.  

Example 4.9. (a) Let $M$ be a set. Then $(\mathcal{P}(M),\cap)$ and $(\mathcal{P}(M),\cup)$ are magmas with neutral elements, where $M$ is neutral for $\left(~\right)$ and $\varnothing$ is neutral for $\cup$ . From Th. 1.29, we also know. $\left(~\right)$ and $\cup$ to be associative and commutative, showing $(\mathcal{P}(M),\cap)$ and $(\mathcal{P}(M),\cup)$ to form abelian semigroups. However, if $M\neq\emptyset$ , then neither structure forms a group, due to the lack of inverse elements: If $N\subsetneq M$ , then there does not exist $B\subseteq M$ such that $N\cap B=M$ ; if $\emptyset\neq N\subseteq M$ , then there does not exist $B\subseteq M$ such that $N\cup B=\emptyset$ . If $M=\emptyset$ , then $\mathcal{P}(M)=\{\emptyset\}$ and $(\mathcal{P}(M),\cap)$ and $(\mathcal{P}(M),\cup)$ both constitute the group with one element ( $\varnothing$ being inverse to itself in both cases).  

(b) Let $M$ be a set and define  

$$
S_{M}:=\big\{(\pi:M\longrightarrow M):\pi\mathrm{~is~bijective}\big\},
$$  

where the elements of $S_{M}$ are also called permutations on $M$ . Then $(S_{M},\circ)$ , where $\cup$ is given by composition of maps according to Def. 2.8, forms a group, the so-called symmetric group or permutation group on $M$ .We verify $(S_{M},\circ)$ to be a group: $\cup$ is well-defined on $S_{M}$ , since the composition of bijective maps is bijective by Th. 2.14. Moreover, $\cup$ is associative by Th. 2.10(a). The neutral element is given by the.  

identity map Id $:M\longrightarrow M$ $\operatorname{Id}(a):=a$ , and, if $\pi\in S_{M}$ , then its inverse map. $\pi^{-1}$ is also its inverse element in the group. $S_{M}$ . We claim that $\cup$ is commutative on $S_{M}$ if, and only if, $\#M\leq2$ : While commutativity is clear for $\#M\leq2$ , if $\{a,b,c\}\subseteq M$ with $\#\{a,b,c\}=3$ and we define $f,g\in S_{M}$ by letting  

$$
\begin{array}{r}{f(x):=\left\{\begin{array}{l l}{a}&{\mathrm{for~}x=a,}\ {c}&{\mathrm{for~}x=b,}\ {b}&{\mathrm{for~}x=c,}\ {x}&{\mathrm{for~}x\not\in\{a,b,c\},}\end{array}\right.\quad g(x):=\left\{\begin{array}{l l}{b}&{\mathrm{for~}x=a,}\ {a}&{\mathrm{for~}x=b,}\ {c}&{\mathrm{for~}x=c,}\ {x}&{\mathrm{for~}x\not\in\{a,b,c\}.}\end{array}\right.}\end{array}
$$  

Then $(f\circ g)(a)=c\neq b=(g\circ f)(a)$ , showing. $\cup$ is not commutative.  

The case $M=\{1,\dots,n\}$ $n\in\mathbb{N}$ , is often of particular interest and, in this case, one also writes $S_{n}$ for $S_{M}$  

(c) $(\mathbb{N}_{0},+)$ and $\left(\mathbb{N}_{0},\cdot\right)$ , where. $^+$ and $\cdot$ denote the usual addition and multiplication on. $\ensuremath{\mathbb{N}}_{0}$ , respectively (see [Phi16, Def. D.1] for a definition via recursion), form commu-. tative semigroups (see [Phi16, Th. D.2]), but no groups due to the lack of inverse elements. From $\ensuremath{\mathbb{N}}_{0}$ , one can then construct the sets of integers $\mathbb{Z}$ (see Ex. 2.36(a)), rational numbers. $\mathbb{Q}$ (see Ex. 2.36(b)), real numbers $\mathbb{R}$ (see [Phi16, Def. D.36]), and complex numbers $\mathbb{C}$ (see [Phi16, Def. 5.1]). One can extend $^+$ and . to each of these sets (see Th. 4.15, Ex. 4.33, and Ex. 4.39 below, [Phi16, Def. D.36], and [Phi16, Def. 5.1]) and show that $(\mathbb{Z},+)$ $(\mathbb{Q},+)$ $(\mathbb{R},+)$ $\left(\mathbb{C},+\right)$ are commutative groups (see Th. 4.15, Ex. 4.33(b), and Ex. 4.39 below, [Phi16, Th. D.39], and [Phi16, Th. 5.2]) as well as. $\left(\mathbb{Q}\setminus\left\{0\right\},\cdot\right)$ $\left(\mathbb{R}\setminus\left\{0\right\},\cdot\right)$ $\left(\mathbb{C}\setminus\left\{0\right\},\cdot\right)$ (see Ex. 4.39 below, [Phi16, Th. D.39], and [Phi16, Th. 5.2]).  

(d) Let $(A,\circ)$ be a magma. We define another magma $(\mathcal{P}(A),\circ)$ by letting  

$$
\underset{B,C\in\mathcal{P}(A)}{\forall}B\circ C:=\left\{b\circ c:b\in B\wedge c\in C\right\}\subseteq A.
$$  

The case, where $B$ or $C$ is a singleton set is of particular interest and one then uses the following simplified notation:  

$$
\begin{array}{r l}{\underset{B\in\mathcal{P}(A)}{\forall}\quad\underset{a\in A}{\forall}}&{{}\Big(a\circ B:=\{a\}\circ B,\quad B\circ a:=B\circ\{a\}\Big).}\end{array}
$$  

Sets of the form. $a\circ B$ are called left cosets, sets of the form $B\circ a$ are called right cosets. If $(A,\circ)$ is commutative, then. $B\circ C=C\circ B$ for each $B,C\in{\mathcal{P}}(A)$ , since $a=b\circ c$ with $b\in B$ $c\in C$ if, and only if,. $a=c\circ b$ . In the same manner, one sees that, if $\cup$ is associative on. $A$ , then it is also associative on $\mathcal{P}(A)$ . If $e\in A$ is left (resp. right) neutral, then, clearly, $\{e\}$ is left (resp. right) neutral for $\cup$ on $\mathcal{P}(A)$ . In general, one can not expect $(\mathcal{P}(A),\circ)$ to be a group, even if $(A,\circ)$ is a group, due to the lack of inverse elements: For example, while $(\mathbb{Z},+)$ is a group,. $(\mathcal{P}(\mathbb{Z}),+)$ is not: For example, $B:=\{0,1\}$ has no inverse: If $C$ were inverse to $B$ , then $-1\in C$ implying $-1=0+(-1)\in B+C$ , i.e. $B+C\neq\{0\}$ , in contradiction to $C$ being inverse to. $B$  

(e) Let $(A,\cdot)$ be a magma and let $M$ be a set. We consider the set $\mathcal{F}(M,A)=A^{M}$ of functions, mapping $M$ into $A$ . We make $A^{M}$ into a magma by defining - pointwise on $A^{M}$ : Define  

$$
\begin{array}{r l}{\underset{f,g\in A^{M}}{\forall}}&{{}f\cdot g:M\longrightarrow A,\quad(f\cdot g)(x):=f(x)\cdot g(x).}\end{array}
$$  

We then have  

$$
\begin{array}{r l}{\left(A,\cdot\right)\mathrm{commutative}}&{\Rightarrow\quad\left(A^{M},\cdot\right)\mathrm{commutative},}\ {\left(A,\cdot\right)\mathrm{associative}}&{\Rightarrow\quad\left(A^{M},\cdot\right)\mathrm{associative},}\ {e\in A\mathrm{left/rightneutral}}&{\Rightarrow\quad f\in A^{M},f\equiv e\mathrm{left/rightneutral},}\ {\left(A,\cdot\right)\mathrm{group}}&{\Rightarrow\quad\left(A^{M},\cdot\right)\mathrm{group},}\end{array}
$$  

where (4.11a) - (4.11c) are immediate from (4.10). To verify (4.11d), let $(A,\cdot)$ be a group with $e\in A$ being neutral. If. $f\in A^{M}$ , then let  

$$
g:M\longrightarrow A,\quad g(x):=(f(x))^{-1}.
$$  

Then  

$$
\begin{array}{r l}{\underset{x\in M}{\forall}}&{{}(f\cdot g)(x)=f(x)\cdot(f(x))^{-1}=e,}\end{array}
$$  

showing $g$ to be inverse to $f$ in $A^{M}$ , i.e. $(A^{M},\cdot)$ forms a group.  

The, perhaps, most important notion when studying structures is that of the composi-. tion-respecting map. The technical term for such a map is homomorphism, which we define next:  

Definition 4.10. Let. $(A,\circ)$ and $(B,\circ)$ be magmas (caveat: to simplify notation, we denote both compositions by. $\cup$ ; however, they might even denote different compositions on the same set. $A=B$ ). A map $\phi:A\longrightarrow B$ is called homomorphism if, and only if,  

$$
\begin{array}{r l}{\forall}&{{}\phi(x\circ y)=\phi(x)\circ\phi(y).}\end{array}
$$  

If $\phi$ is a homomorphism, then it is called monomorphism if, and only if, it is injective; epimorphism if, and only if, it is surjective; isomorphism if, and only if, it is bijective, endomorphism if, and only if, $(A,\circ)=(B,\circ)$ ; automorphism if, and only if, it is both. endomorphism and isomorphism. Moreover, $(A,\circ)$ and $(B,\circ)$ are called isomorphic (denoted $(A,\circ)\cong(B,\circ),$ if, and only if, there exists an isomorphism $\phi:{\cal A}\longrightarrow{\cal B}$ . If $A$ and $B$ have neutral elements $e\in A$ $e^{\prime}\in B$ , then a homomorphism $\phi:{\cal A}\longrightarrow{\cal B}$ is called unital if, and only if, $\phi(e)=e^{\prime}$  

If $(A,\circ)$ and $(B,\circ)$ are isomorphic, then, from an algebraic perspective, the two structures are the same, except that the elements of the underlying set have been "renamed" (where the isomorphism provides the assignment rule for obtaining the new names).  

Proposition 4.11. Let $(A,\circ)$ $(B,\circ)$ $(C,\circ)$ be magmas.  

(a) If $\phi:A\longrightarrow B$ and $\psi:B\longrightarrow C$ are homomorphisms, then so is $\psi\circ\phi$ . If $\phi$ $\psi$ are unital, so is. $\psi\circ\phi$  

(b) If $\phi:A\longrightarrow B$ is an isomorphism, then $\phi^{-1}$ is an isomorphism as well.  

(c) Let $\phi:A\longrightarrow B$ be an epimorphism. Then the following implications hold:  

$$
\begin{array}{r l}{(A,\circ)c o m m u t a t i v e}&{\Rightarrow\phantom{-}(B,\circ)c o m m u t a t i v e,}\ {(A,\circ)s e m i g r o u p}&{\Rightarrow\phantom{-}(B,\circ)s e m i g r o u p,}\ {(A,\circ)g r o u p}&{\Rightarrow\phantom{-}(B,\circ)g r o u p.}\end{array}
$$  

If $\phi$ is even an isomorphism, then the above implications become equivalences.  

(d) Let $\phi:A\longrightarrow B$ be an epimorphism. If $e\in A$ is neutral, then $B$ contains a neutral element and $\phi$ is unital.  

(e) If $(A,\circ)$ $(B,\circ)$ are groups and. $\phi:A\longrightarrow B$ is a homomorphism, then $\phi$ is unital and $\phi(a^{-1})=(\phi(a))^{-1}$ for each $a\in A$  

Proof. (a): If $\phi$ and $\psi$ are homomorphisms and $x,y\in A$ , then  

$$
(\psi\circ\phi)(x\circ y)=\psi\big(\phi(x)\circ\phi(y)\big)=\psi(\phi(x))\circ\psi(\phi(y)),
$$  

showing $\psi\circ\phi$ to be a homomorphism. If $e\in A$ $e^{\prime}\in B$ $e^{\prime\prime}\in C$ are neutral and $\phi$ and $\psi$ are unital, then  

$$
(\psi\circ\phi)(e)=\psi(e^{\prime})=e^{\prime\prime},
$$  

showing $\psi\circ\phi$ to be unital.  

(b): If $\phi$ is an isomorphism and $x,y\in B$ , then  

$$
\begin{array}{c}{{\phi^{-1}(x\circ y)=\phi^{-1}\Big(\phi\big(\phi^{-1}(x)\big)\circ\phi\big(\phi^{-1}(y)\big)\Big)=\phi^{-1}\Big(\phi\big(\phi^{-1}(x)\circ\phi^{-1}(y)\big)\Big)}}\ {{=\phi^{-1}(x)\circ\phi^{-1}(y),}}\end{array}
$$  

showing $\phi^{-1}$ to be an isomorphism.  

(c): Exercise.  

(d): It suffices to show, $e^{\prime}:=\phi(e)$ is neutral. Let $b\in B$ and $a\in A$ such that $\phi(a)=b$ Then  

$$
\begin{array}{r}{b\circ e^{\prime}=\phi(a)\circ\phi(e)=\phi(a\circ e)=\phi(a)=b,}\ {e^{\prime}\circ b=\phi(e)\circ\phi(a)=\phi(e\circ a)=\phi(a)=b,}\end{array}
$$  

proving $e^{\prime}$ to be neutral as desired.  

(e): Let $(A,\circ)$ $(B,\circ)$ be groups with neutral elements $e\in A$ $e^{\prime}\in B$ , and let. $\phi:A\longrightarrow B$ be a homomorphism. Then  

$$
\phi(e)\circ e^{\prime}=\phi(e)=\phi(e\circ e)=\phi(e)\circ\phi(e).
$$  

Applying $(\phi(e))^{-1}$ to both sides of the above equality proves $\phi(e)=e^{\prime}$ . Moreover, for each $a\in A$  

$$
\phi(a^{-1})\circ\phi(a)=\phi(a^{-1}\circ a)=\phi(e)=e^{\prime},
$$  

proving (e).  

Example 4.12. (a) If $(A,\circ)$ is a magma, then it is immediate that the identity Id : $A\longrightarrow A$ is an automorphism.  

(b) If $(A,\circ)$ $(B,\circ)$ are magmas, where $e\in B$ is neutral, then the constant map $\phi\equiv e$ is a homomorphism: Indeed,  

$$
\begin{array}{r l}{\underset{x,y\in A}{\forall}}&{{}\phi(x\circ y)=e=e\circ e=\phi(x)\circ\phi(y).}\end{array}
$$  

(c) If $(A,\cdot)$ is a semigroup with neutral element $1\in A$ , then, for each fixed. $a\in A$  

$$
\phi_{a}:\mathbb{N}_{0}\longrightarrow A,\quad\phi_{a}(n):=a^{n},
$$  

is a homomorphism from $(\mathbb{N}_{0},+)$ into $(A,\cdot)$ ; if $(A,\cdot)$ is a group, we may extend $\phi_{a}$ to $\mathbb{Z}$ and it becomes a homomorphism from $(\mathbb{Z},+)$ into $(A,\cdot)$ : These statements are immediate from Th. 4.8(a). Note that, if $A=\mathbb{N}_{0},\mathbb{Z},\mathbb{Q},\mathbb{R},\mathbb{C}$ and $(A,\cdot)=(A,+)$ then $\phi_{a}(n)=n a$  

(d) If $\left(G,\cdot\right)$ is an abelian group, then for each fixed $k\in\mathbb{Z}$  

$$
\phi_{k}:G\longrightarrow G,\quad\phi_{k}(a):=a^{k},
$$  

is an endomorphism due to Th. 4.8(c) (the case $k=-1$ , where $a\mapsto a^{-1}$ is of particular interest). Note that, if $G=\mathbb{N}_{0},\mathbb{Z},\mathbb{Q},\mathbb{R},\mathbb{C}$ and $(G,\cdot)=(G,+)$ , then $\phi_{k}(a)=k a$  

Notation 4.13. A composition $\cup$ on a nonempty finite set $A$ can be defined by means of a composition table (also known as a multiplication table or Cayley table: For each element $a\in A$ , the table has a row labeled by $a$ and it has a column labeled by $a$ ; if $a,b\in A$ , then the entry at the intersection of the row labeled $a$ and the column labeled $b$ is $a\circ b$ (see Ex. 4.14 below, for examples).  

Example 4.14. (a) The most trivial groups are the group with one element and the group with two elements, which can be defined by the following Cayley tables (where $e,a$ are distinct elements):  

$$
{\frac{\circ\left|e\right.}{\left.e\right|e}},\qquad{\frac{\circ\left|e\right.}{\left.e\right|e}}{\frac{a}{a}}
$$  

Both structures are abelian groups, which is immediate for the group with one. element and is easily verified for the group with two elements. We will see later that they are isomorphic to the groups we will denote. $\mathbb{Z}_{1}$ and $\mathbb{Z}_{2}$ (which, in light of. Prop. 4.11(c), shows again that the structure with two elements is a group).  

(b) The following examples show that, in non-groups, left and right neutral elements need not be unique: For $a\neq b$ , let  

$$
{\begin{array}{l l l l}{{\frac{\circ{\left|\begin{array}{l l l l l l}{a}&{b}\ {a}\ {b}\end{array}\right|}}{b}}}&{{}}&{{{\begin{array}{l}{\qquad\circ{\left|\begin{array}{l l}{a}&{b}\ {a}\end{array}\right|}}\end{array}}}}\ {{\begin{array}{l}{b}\ {b}\end{array}}{\left|\begin{array}{l l l l l}{a}&{b}\end{array}\right|}}&{{}}&{{}}&{{b}{\left|\begin{array}{l l}{a}&{b}\ {a}&{a}\ {b}&{b}\end{array}\right|}}\end{array}}
$$  

One easily verifies these structures to be associative, but they are not groups: The. magma on the left has no right neutral element, the magma on the right does not have inverses to both. $a$ and $b$  

Theorem 4.15. Let $(A,+)$ be an abelian semigroup with neutral element $0\in A$ and assume $(A,+)$ to satisfy the cancellation laws (4.4) (with $\bigcirc$ replaced by $^+$ ).Consider the quotient set.  

$$
G:=(A\times A)/\sim~=~\{[(a,b)]:(a,b)\in A\times A\}
$$  

with respect to the equivalence relation defined by  

$$
(a,b)\sim(c,d)\quad:\Leftrightarrow\quad a+d=b+c.
$$  

Introducing the simplified notation $[a,b]:=[(a,b)]$ , we define addition and subtraction on $G$ by  

$$
\begin{array}{r l}{+:G\times G\longrightarrow G,}&{\left([a,b],[c,d]\right)\mapsto[a,b]+[c,d]:=[a+c,b+d],}\ {-:G\times G\longrightarrow G,}&{\left([a,b],[c,d]\right)\mapsto[a,b]-[c,d]:=[a,b]+[d,c].}\end{array}
$$  

Then addition and subtraction on $G$ are well-defined, $(G,+)$ forms an abelian group, where $[0,0]$ is the neutral element, $[b,a]$ is the inverse element of $[a,b]$ for each $a,b\in A$ and, denoting the inverse element of $[a,b]$ by $-[a,b]$ in the usual way, $[a,b]-[c,d]=$ $[a,b]+(-[c,d])$ for each $a,b,c,d\in A$ . Moreover, the map  

$$
\iota:A\longrightarrow G,\quad\iota(a):=[a,0],
$$  

is a monomorphism, where it is customary to identify $A$ with $\iota(A)$ .One then just writes a instead of. $[a,0]$ and $-a$ instead of. $[0,a]=-[a,0]$ . The most important application is the case $A=\ensuremath{\mathbb{N}}_{0}$ , which yields that addition on $\mathbb{Z}=G$ forms an abelian group (cf. Ex. 2.36(a), [Phi16, Th. D.2], [Phi16, Th. D.7(c)]).  

Proof. If one reexamines Ex. 2.36(a), replacing $\ensuremath{\mathbb{N}}_{0}$ by $A$ and $\mathbb{Z}$ by $G$ , then one sees it shows $\sim$ to constitute an equivalence relation, where the proof makes use of commutativity, associativity, and the cancellation law. To verify $^+$ and $-$ are well-defined on $G$ we need to check the above definitions do not depend on the chosen representatives, i.e.  

an  

$$
\begin{array}{r l}{\forall_{\substack{b,c,d,\tilde{a},\tilde{b},\tilde{c},\tilde{d}\in A}}\left([a,b]=[\tilde{a},\tilde{b}]\wedge[c,d]=[\tilde{c},\tilde{d}]\quad\Rightarrow\quad[a+c,b+d]=[\tilde{a}+\tilde{c},\tilde{b}+\tilde{d}]\right)}\ {\textnormal{d}}\ {\textnormal{d}}\ {\forall_{\substack{b,c,d,\tilde{a},\tilde{b},\tilde{c},\tilde{d}\in A}}\left([a,b]=[\tilde{a},\tilde{b}]\wedge[c,d]=[\tilde{c},\tilde{d}]\quad\Rightarrow\quad[a,b]-[c,d]=[\tilde{a},\tilde{b}]-[\tilde{c},\tilde{d}]\right).}\end{array}
$$  

Indeed, $[a,\underline{{b}}]=[\tilde{a},\tilde{b}]$ means $a+{\tilde{b}}=b+{\tilde{a}}$ $[c,d]=[\tilde{c},\tilde{d}]$ means $c+\tilde{d}=d+\tilde{c}$ , implying $a+c+{\tilde{b}}+{\tilde{d}}=b+{\tilde{a}}+d+{\tilde{c}}$ , i.e. $[a+c,b+d]=[\tilde{a}+\tilde{c},\tilde{b}+\tilde{d}]$ , proving (4.19a). Now (4.19b) is just (4.17b) combined with (4.19a). To verify commutativity and associativity on $G$ let $a,b,c,d,e,f\in A$ .Then  

$$
[a,b]+[c,d]=[a+c,b+d]=[c+a,b+d]=[c,d]+[a,b],
$$  

proving commutativity, and  

$$
\begin{array}{r l}&{[a,b]+\bigl([c,d]+[e,f]\bigr)=[a,b]+[c+e,d+f]=[a+(c+e),b+(d+f)]}\ &{\qquad=[(a+c)+e,(b+d)+f]=[a+c,b+d]+[e,f]}\ &{\qquad=\bigl([a,b]+[c,d]\bigr)+[e,f],}\end{array}
$$  

proving associativity. For every $a,b\in A$ , one obtains $[a,b]+[0,0]=[a+0,b+0]=[a,b]$ proving neutrality of $[0,0]$ , whereas $[a,b]+[b,a]=\left\lfloor a+b,b+a\right\rfloor=\left\lfloor a+b,a+b\right\rfloor=\left\lfloor0,0\right\rfloor$ (since $(a+b,a+b)\sim(0,0))$ shows $[b,a]=-[a,b]$ . Now $[a,b]-[c,d]=[a,b]+(-[c,d])$ is immediate from (4.17b). The map $\iota$ is injective, as, for each $a,b\in A$ $\iota(a)=[a,0]=$ $\iota(b)=[b,0]$ implies $a+0=0+b$ , i.e. $a=b$ . The map $\iota$ is a homomorphism, as  

$$
\begin{array}{r l}{\underset{a,b\in A}{\forall}}&{{}\iota(a+b)=[a+b,0]=[a,0]+[b,0]=\iota(a)+\iota(b),}\end{array}
$$  

completing the proof of the theorem.  

Definition 4.16. Let $(G,\circ)$ be a group, $0\neq U\subseteq G$ .We call $U$ a subgroup of $G$ (denoted $U\leq G$ ) if, and only if, $(U,\circ)$ forms a group, where the composition on $U$ is the restriction of the composition on $G$ , i.e. $\circ\lceil\tau\times U$  

Theorem 4.17. Let $(G,\circ)$ be a group, $\varnothing\neq U\subseteq G$ . Then $U\leq G$ if, and only if, (i) and (ii) hold, where  

(i) For each $u,v\in U$ , one has $u\circ v\in U$ (ii) For each $u\in U$ , one has $u^{-1}\in U$  

If $U$ is finite, then. $U\leq G$ is already equivalent to (i).  

Proof. Exercise.  

Example 4.18. (a) If. $(G,\circ)$ is an arbitrary group with neutral element $e\in G$ , then it is immediate from Th. 4.17, that. $\{e\}$ and $G$ are always subgroups.  

(b) We use Th. 4.17 to verify that, for each $k\in\mathbb{Z}$ $k\mathbb{Z}=\{k l\colon l\in\mathbb{Z}\}$ is a subgroup of. $(\mathbb{Z},+)$ : As $0\in k\mathbb{Z}$ $k\mathbb{Z}\neq\emptyset$ . If $l_{1},l_{2}\in\mathbb{Z}$ , then $k l_{1}+k l_{2}=k(l_{1}+l_{2})\in k\mathbb{Z}$ If $l\in\mathbb Z$ then $-k l=k(-l)\in k\mathbb{Z}$ . Thus, Th. 4.17 applies, showing. $k\mathbb{Z}\leq\mathbb{Z}$  

(c) As N is no subgroup of. $\mathbb{Z}$ , even though Th. 4.17(i) holds for. $\mathbb{N}$ , we see that, in. general, Th. 4.17(ii) can not be omitted for infinite subsets.  

(d) If $(G,\circ)$ is a group with neutral element $e\in G$ $I\neq\emptyset$ is an index set, and $(U_{i})_{i\in I}$ is a family of subgroups, then $\begin{array}{r}{U:=\bigcap_{i\in I}U_{i}}\end{array}$ is a subgroup as well: Indeed, $e\in U$ since $e\in U_{i}$ for each $i\in I$ .If $a,b\in U$ , then $a,b\in U_{i}$ for each $i\in I$ , implying $a\circ b\in U_{i}$ for each $i\in I$ , i.e. $a\circ b\in U$ . Moreover $a^{-1}\in U_{i}$ for each $i\in I$ as well, showing $a^{-1}\in U$ . Thus, $U$ is a subgroup by Th. 4.17.  

(e) In contrast to intersections, unions of subgroups are not necessarily subgroups (however, cf. (f) below): We know from (b) that $2\mathbb{Z}$ and $3\mathbb{Z}$ are subgroups of $(\mathbb{Z},+)$ However, $2\in2\mathbb{Z}$ $3\in3\mathbb{Z}$ , but $5=2+3\not\in(2\mathbb{Z})\cup(3\mathbb{Z})$ , showing $({\mathrm{2\mathbb{Z}}})\cup({\mathrm{3\mathbb{Z}}})$ is not a subgroup of $(\mathbb{Z},+)$  

(f) While (e) shows that unions of subgroups are not necessarily subgroups, if $(G,\circ)$ is a group with neutral element $e\in G$ $I\neq\emptyset$ is an index set, partially ordered by $\leq$ in a way such that, for each $i,j\in I$ , there exists. $k\in{I}$ with $i,j\leq k$ (if $I$ is totally ordered by. $\leq$ , then one can use. $k:=\operatorname*{max}\{i,j\})$ , and $(U_{i})_{i\in I}$ is an increasing family of subgroups (i.e., for each $i,j\in I$ with $i\leq j$ , one has $U_{i}\subseteq U_{j}$ ), then $U:=\cup_{i\in I}U_{i}$ is a subgroup as well: Indeed, if $i\in I$ , then $e\in U_{i}\subseteq U$ . If $a,b\in U$ , then there exist. $i,j\in I$ such that. $a\in U_{i}$ and $b\in U_{j}$ . If $k\in{I}$ with $i,j\leq k$ , then $a\circ b\in U_{k}\subseteq U$ Moreover, $a^{-1}\in U_{i}\subseteq U$ . Thus, $U$ is a subgroup by Th. 4.17.  

(g) One can show that every group. $G$ is isomorphic to a subgroup of the permutation. group $S_{G}$ (see Sec. C of the Appendix, in particular, Cayley's Th. C.2).  

Definition 4.19. Let. $G$ and $H$ be groups and let. $\phi:G\longrightarrow H$ be a homomorphism. Let $e^{\prime}\in H$ be neutral. Define the sets  

$$
\begin{array}{r l}&{\ker\phi:=\phi^{-1}\{e^{\prime}\}=\{a\in G:\phi(a)=e^{\prime}\},}\ &{\operatorname{Im}\phi:=\phi(G)=\{\phi(a):a\in G\},}\end{array}
$$  

where $\ker\phi$ is called the kernel of $\phi$ and $\operatorname{Im}\phi$ is called the image of $\phi$  

Theorem 4.20. Let $(G,\cdot)$ and $(H,\cdot)$ be groups and let $\phi:G\longrightarrow H$ be a homomorphism. Let $e\in G$ and $e^{\prime}\in H$ be the respective neutral elements. Also assume $U\leq G$ $V\leq H$ Then the following statements hold true:  

(a) $\phi^{-1}(V)\leq G.$  

(b) $\ker\phi\le G$  

(c) $\operatorname{Im}\phi\leq H.$  

(d) $\phi(U)\leq H$  

(e) $\phi$ is a monomorphism (i.e. injective) if, and only if, $\ker\phi=\{e\}$  

(f) It holds true that  

$$
\begin{array}{r l}{\underset{a\in G}{\forall}}&{{}\phi^{-1}\big(\{\phi(a)\}\big)=a(\ker\phi)=(\ker\phi)a,}\end{array}
$$  

i.e. the nonempty preimages of elements of $H$ are cosets of the kernel of $\phi$ (cf. Ex.   
4.9(d)).  

Proof. (a): Since $V\leq H$ , we have $e^{\prime}\in V$ . From Prop. 4.11(e), we know $\phi(e)=e^{\prime}$ , i.e. $e\in\phi^{-1}(V)$ and $\phi^{-1}(V)\neq\emptyset$ . If $a,b\in\phi^{-1}(V)$ , then $\phi(a),\phi(b)\in V$ and, since $V\leq H$  

$$
\begin{array}{c c c}{\phi(a b)}&{=}&{\phi(a)\phi(b)\in V,}\ {\phi(a^{-1})}&{\stackrel{\mathrm{Prop.~}\underline{{4.11}}(\mathrm{e})}{=}}&{(\phi(a))^{-1}\in V,}\end{array}
$$  

showing $a b\in\phi^{-1}(V)$ and $a^{-1}\in\phi^{-1}(V)$ . Thus, $\phi^{-1}(V)\leq G$ by Th. 4.17.  

(b) is now immediate by applying (a) with $V:=\{e^{\prime}\}\leq H$  

(c): As $\phi(e)=e^{\prime}$ , we have $e^{\prime}\in\operatorname{Im}\phi$ and $\operatorname{Im}\phi\neq\emptyset$ .If $x,y\in\operatorname{Im}\phi$ , then there exist $a,b\in G$ such that $\phi(a)=x$ $\phi(b)=y$ . Thus,  

$$
\begin{array}{r c l}{{\phi(a b)}}&{{=}}&{{\phi(a)\phi(b)=x y,}}\ {{\phi(a^{-1})}}&{{=}}&{{(\phi(a))^{-1}=x^{-1},}}\end{array}
$$  

showing $x y\in\operatorname{Im}\phi$ and $x^{-1}\in\operatorname{Im}\phi$ . Once again,. $\operatorname{Im}\phi\leq H$ now follows from Th. 4.17.. (d) is now immediate by applying (c) with $\phi$ replaced by $\phi\left\lceil\tau\right\rceil$ (then $\phi(U)=\operatorname{Im}\phi\lceil_{U}\leq H)$ (e): If $\phi$ is injective, then. $e$ is the unique preimage of. $e^{\prime}$ , showing $\ker\phi=\{e\}$ . Conversely, assume $\ker\phi=\{e\}$ . If $a,b\in G$ with $\phi(a)=\phi(b)$ , then  

$$
\phi(a^{-1}b)=(\phi(a))^{-1}\phi(b)=e^{\prime},
$$  

showing $a^{-1}b\in\ker\phi$ , i.e. $a^{-1}b=e$ , i.e. $b=a$ , and $\phi$ is injective.  

(f): Fix $a\in G$ .Suppose $b\in\phi^{-1}\big(\{\phi(a)\}\big)$ . Then $\phi(a)=\phi(b)$ , implying $\phi(a^{-1}b)=$ $(\phi(a))^{-1}\phi(b)=e^{\prime}$ and $a^{-1}b\in\ker\phi$ : Thus, $b\in a(\ker\phi)$ and $\phi^{-1}\bigl(\{\phi(a)\}\bigr)\subseteq a(\ker\phi)$ Similarly, $\phi(b a^{-1})~=~\phi(b)(\phi(a))^{-1}~=~e^{\prime}$ , showing $b\in(\ker\phi)a$ and $\phi^{-1}\left(\{\phi(a)\}\right)~\subseteq$ $(\ker\phi)a$ .Conversely, suppose $b\in a(\ker\phi)$ (resp. $b\in(\ker\phi)a)$ . Then $a^{-1}b\in\ker\phi$ (resp. $b a^{-1}\in\ker\phi$ ), implying  

$$
e^{\prime}=\phi(a^{-1}b)=\phi(a^{-1})\phi(b)\quad(\mathrm{resp.}\quad e^{\prime}=\phi(b a^{-1})=\phi(b)\phi(a^{-1})).
$$  

In both cases, we conclude $\phi(a)~=~\phi(b)$ , i.e. $b\in\phi^{-1}\big(\{\phi(a)\}\big)$ .Thus $a(\ker\phi)\subseteq$ $\phi^{-1}\bigl(\{\phi(a)\}\bigr)$ as well as $(\ker\phi)a\subseteq\phi^{-1}{\big(}\{\phi(a)\}{\big)}$ , thereby establishing the case.  

Example 4.21. According to Ex. 4.12(c), if. $k\in\mathbb{Z}$ , then the map. $\phi_{k}:\mathbb{Z}\longrightarrow\mathbb{Z}$ $\phi_{k}(l):=k l$ , is a homomorphism of. $(\mathbb{Z},+)$ into itself. Clearly,. $\operatorname{Im}\phi_{k}=k\mathbb{Z}$ , showing, once again, $k\mathbb{Z}\leq\mathbb{Z}$ (cf. Ex. 4.18(b)). For another example, let. $G:=\{e,a\}$ be the group with two elements of Ex. 4.14(a). According to Ex. 4.12(c), the map $\phi:\mathbb{Z}\longrightarrow G$ $\phi(n):=a^{n}$ , is a homomorphism. Clearly, $\phi$ is an epimorphism with. $\ker\phi=2\mathbb{Z}$ (i.e. the set of all even numbers)..  

In Ex. 4.9(d), we have defined cosets for a given subset of a magma. For a group. $G$ cosets of subgroups are of particular interest: We will see in Prop. 4.22 that, if $U\leq G$ then the cosets of. $U$ form a partition of. $G$ , giving rise to an equivalence relation on. $G$ according to Th. 2.33(a). Thus, the cosets form the quotient set with respect to this equivalence relation and, if the subgroup is sufficiently benign (namely what we will call. a normal subgroup in Def. 4.23 below), then we can make this quotient set itself into another group, the so-called quotient group or factor group. $G/U$ (cf. Def. 4.26 and Th. 4.27(a) below).  

Proposition 4.22. Let $\left(G,\cdot\right)$ be a group,. $U\leq G$ . Then  

$$
\begin{array}{r}{G=\underset{a\in G}{\bigcup}a U,\quad\underset{a,b\in G}{\forall}\Big(a U=b U\lor a U\cap b U=\emptyset\Big),}\ {G=\underset{a\in G}{\bigcup}U a,\quad\underset{a,b\in G}{\forall}\Big(U a=U b\lor U a\cap U b=\emptyset\Big),}\end{array}
$$  

i.e. both the left cosets and the right cosets of $U$ form decompositions of $G$  

Proof. We conduct the proof for left cosets - the proof for right cosets is completely analogous.For each $a\in G$ , we have $a\in a U$ (since $e\in U$ ), already showing $G=$ $\textstyle\bigcup_{a\in G}a U$ . Now let $a,b,x\in G$ with $x\in a U\cap b U$ .We need to prove $a U=b U$ . From $x\in a U\cap b U$ , we obtain  

$$
\exists_{u_{1},u_{2}\in U}\quad x=a u_{1}=b u_{2}.
$$  

Now let $a u\in a U$ (i.e. $u\in U$ ). As (4.22) implies $a=b u_{2}u_{1}^{-1}$ , we obtain $a u=b u_{2}u_{1}^{-1}u\in$ $b U$ , using $u_{2}u_{1}^{-1}u\in U$ , due to $U$ being a subgroup. This shows $a U\subseteq b U$ . Analogously, if $b u\in b U$ , then $b u=a u_{1}u_{2}^{-1}u\in a U$ , where we used $b=a u_{1}u_{2}^{-1}$ due to (4.22) and $u_{1}u_{2}^{-1}u\in U$ . This shows $b U\subseteq a U$ , completing the proof.. $\vert$  

Definition 4.23. Let $\left(G,\cdot\right)$ be a group with subgroup $U\leq G$ . Then $U$ is called normal if, and only if,  

$$
\begin{array}{r}{\forall\quad a U=U a,}\ {a\in G}\end{array}
$$  

i.e. if, and only if, left and right cosets with respect to. $U$ are the same.  

Theorem 4.24. Let $(G,\cdot)$ and $(H,\cdot)$ be groups and let $\phi:G\longrightarrow H$ be a homomorphism.  

(a) If $V$ is a normal subgroup of $H$ , then. $U:=\phi^{-1}(V)$ is a normal subgroup of $G$  

(b) $\ker\phi$ is a normal subgroup of $G$  

Proof. (a): As we already know from Th. 4.20(a) that $U$ is a subgroup of $G$ , it merely remains to show $U$ is normal. If $a\in G$ and $u\in U$ , then $\phi(u)\in V$ . Since $V$ is normal, we have $\phi(a)V=V\phi(a)$ . Thus, there exists $v\in V$ such that $\phi(a)\phi(u)=v\phi(a)$ , namely  

$$
v=\phi(a)\phi(u)(\phi(a))^{-1}=\phi(a)\phi(u)\phi(a^{-1})=\phi(a u a^{-1}),
$$  

showing $u^{\prime}:=a u a^{-1}\in U$ . Thus, $a u=a u a^{-1}a=u^{\prime}a$ , proving $a U=U a$ , as desired.  

(b) is now immediate by applying (a) with $\textit{V}:=\{e\}$ , where $e$ denotes the neutral. element of $H$ . Alternatively, one also obtains $\ker\phi$ to be a normal subgroup of. $G$ as a direct consequence of Th. 4.20(f).  

Example 4.25. (a) If $G$ is an abelian group, then every subgroup of $G$ is normal.  

(b) In Ex. 4.9(b), we defined the symmetric groups $S_{2}$ and $S_{3}$ . Clearly, the map.  

$$
\phi:S_{2}\longrightarrow S_{3},\quad f\mapsto\phi(f),\quad\phi(f)(n):=\left\{\begin{array}{l l}{{f(n)}}&{{\mathrm{for~}n\in\{1,2\},}}\ {{3}}&{{\mathrm{for~}n=3,}}\end{array}\right.
$$  

constitutes a monomorphism. By identifying $S_{2}$ with $\phi(S_{2})$ , we may consider $S_{2}$ as a subgroup of $S_{3}$ .We claim that $S_{2}$ is not a normal subgroup of $S_{3}$ . Indeed, one checks that  

$$
(23)S_{2}=(23)\{\mathrm{Id},(12)\}=\{(23),(132)\}\neq S_{2}(23)=\{(23),(123)\},
$$  

where we made use of a notation, commonly used for permutations (we will need to study it more thoroughly later): (12) is the map that permutes 1 and 2 and leaves 3 fixed, (23) permutes 2 and 3 and leaves 1 fixed, (132) maps 1 into 3, 3 into 2, 2 into 1, (123) maps 1 into 2, 2 into 3, 3 into 1.  

Definition 4.26. Let $\left(G,\cdot\right)$ be a group and let $N\leq G$ be a normal subgroup. According to Prop. 4.22, the cosets of $N$ form a partition of $G$ . According to Th. 2.33(a), the cosets are precisely the equivalence classes of the equivalence relation $\sim$ on $G$ , defined by  

$$
a\sim b:\Leftrightarrow a N=b N.
$$  

Define  

$$
G/N:=G/\sim,
$$  

i.e. $G/N$ is the set of all cosets of. $N$ . We define a composition on $G/N$ by letting  

$$
\begin{array}{r l}{\underset{a,b\in G}{\forall}}&{{}(a\boldsymbol{N})\cdot(b\boldsymbol{N}):=a b\boldsymbol{N}}\end{array}
$$  

(note that we already know the forming of cosets to be associative by Ex. 4.9(d)). We call $(G/N,\cdot)$ the quotient group of $G$ by $N$ or the factor group of $G$ with respect to $N$ (cf. Th. 4.27(a) below).  

Theorem 4.27. (a) Let $\left(G,\cdot\right)$ be a group and let. $N\leq G$ be a normal subgroup. Then (4.24) well-defines a composition on $G/N$ that makes. $G/N$ into a group with neutral. element $N$ . Moreover, the map.  

$$
\phi_{N}:G\longrightarrow G/N,\quad\phi_{N}(a):=a N,
$$  

is an epimorphism, called the canonical or natural homomorphism from $G$ onto $G/N$ (comparing with Def. 2.32(b), we see that $\phi_{N}$ is precisely the quotient map with respect to the equivalence relation $\sim$ of Def. 4.26).  

(b) Isomorphism Theorem: If $(G,\cdot)$ and $(H,\cdot)$ are groups and $\phi:{\cal G}\longrightarrow{\cal H}$ is a homomorphism, then  

$$
G/\ker\phi\cong\operatorname{Im}\phi
$$  

(recall from Th. 4.24(b) that $\ker\phi$ is always a normal subgroup of $G$ ). More precisely, the map  

$$
f:G/\ker\phi\longrightarrow\mathrm{Im}\phi,\quad f(a\ker\phi):=\phi(a),
$$  

is well-defined and constitutes an isomorphism. If $f_{\mathrm{e}}:G\longrightarrow G/\ker\phi$ denotes the natural epimorphism according to (a) and. $\iota:\operatorname{Im}\phi\longrightarrow H$ $\iota(a):=a$ , denotes the embedding, then $f_{\mathrm{m}}:G/\ker\phi\longrightarrow H$ $f_{\mathrm{m}}:=\iota\circ f$ , is a monomorphism such that  

$$
\phi=f_{\mathrm{m}}\circ f_{\mathrm{e}}.
$$  

Proof. (a): To see that (4.24) well-defines a composition on $G/N$ , we need to show that the definition is independent of the chosen coset representatives $a,b$ : To this end, suppose $a,b,a^{\prime},b^{\prime}\in G$ are such that $a N=a^{\prime}N$ and $b N=b^{\prime}N$ .We need to show $a b N=a^{\prime}b^{\prime}N$ . There exist $n_{a},n_{b}\in N$ such that $a^{\prime}=a n_{a}$ $b^{\prime}=b n_{b}$ . Since $N$ is a normal subgroup of $G$ , we have $b N=N b$ and there exists $n\in N$ such that $n_{a}b=b n$ . Then, as $n n_{b}N=N$ , we obtain  

$$
a^{\prime}b^{\prime}N=a n_{a}b n_{b}N=a b n n_{b}N=a b N,
$$  

as needed. That $\phi_{N}$ is surjective is immediate from (4.25). Moreover, the computation  

$$
\begin{array}{r l}{\underset{a,b\in G}{\forall}}&{{}\phi_{N}(a b)=a b N=(a N)\cdot(b N)=\phi_{N}(a)\cdot\phi_{N}(b)}\end{array}
$$  

verifies $\phi_{N}$ to be a homomorphism. That. $(G/N,\cdot)$ forms a group is now an immediate consequence of Prop. 4.11(c),(d).  

(b): We conduct the proof by showing $f(a\ker\phi)$ does not depend on the chosen coset representative $a\in G$ : Let $e^{\prime}\in H$ be neutral and suppose $a^{\prime}\in G$ is such that $a^{\prime}\ker\phi=$ $a\ker\phi$ . Then there exists $x\in\ker\phi$ such that $a^{\prime}=a x$ , implying  

$$
f(a^{\prime}\ker\phi)=\phi(a^{\prime})=\phi(a x)=\phi(a)\phi(x)=\phi(a)\cdot e^{\prime}=\phi(a)=f(a\ker\phi),
$$  

as desired. To prove $f$ to be a homomorphism, let $a,b\in G$ . Then  

$$
f{\bigl(}(a\ker\phi)\cdot(b\ker\phi){\bigr)}=f(a b\ker\phi)=\phi(a b)=\phi(a)\phi(b)=f(a\ker\phi)f(b\ker\phi),
$$  

i.e. $f$ is a homomorphism.If $x\in\operatorname{Im}\phi$ , then there exists $a\in G$ with $x=\phi(a)$ Thus, $f(a\ker\phi)=\phi(a)=x$ , showing $f$ to be surjective. Now suppose $a\in G$ is such that $f(a\ker\phi)=e^{\prime}$ . Then $\phi(a)=e^{\prime}$ , i.e. $a\in\ker\phi$ .Thus, $a\ker\phi=\ker\phi$ , showing $\ker f=\{\ker\phi\}$ , i.e. $f$ is injective, completing the proof that $f$ is an isomorphism. Since $f$ and $\iota$ are monomorphisms, so is $f_{\mathrm{m}}=\iota\circ f$ . Moreover, if $a\in G$ , then  

$$
(f_{\mathrm{m}}\circ f_{\mathrm{e}})(a)=f_{\mathrm{m}}(a\ker\phi)=f(a\ker\phi)=\phi(a),
$$  

thereby proving (4.28).  

Example 4.28. (a) Consider $(\mathbb{Z},+)$ and let $n\in\mathbb{N}$ .We know from Ex. 4.18(b) that $n\mathbb{Z}\leq\mathbb{Z}$ . As $(\mathbb{Z},+)$ is also commutative, $n\mathrm{Z}$ is a normal subgroup of. $\mathbb{Z}$ and we can. form the quotient group  

$$
\mathbb{Z}_{n}:=\mathbb{Z}/n\mathbb{Z}.
$$  

The elements of $\mathbb{Z}_{n}$ are the cosets $r+n\mathbb{Z}$ $r\in\mathbb{Z}$ . For $r\in\mathbb{Z}$ ,  we have.  

$$
{\bar{r}}:=r+n\mathbb{Z}=\{r+m n:m\in\mathbb{Z}\}.
$$  

Note that $r+m n+n\mathbb{Z}=r+n\mathbb{Z}$ . For integers $k,l\in\mathbb{Z}$ , one says $k$ is congruent $l$ modulo $n$ if, and only if, there exists $m\in\mathbb{Z}$ such that $k-l=m n$ and, in this case, one writes $k\equiv l$ (mod $n$ ). If $k=r+m n$ with $m\in\mathbb{Z}$ , then $k-r=m n$ , implying  

$$
r+n\mathbb{Z}=\{k\in\mathbb{Z}:k\equiv r(\mathrm{mod}n)\}.
$$  

For this reason, one also calls the elements of $\mathbb{Z}_{n}$ congruence classes. If $k=r+m n$ as above, one also says that. $r$ is the residue (or remainder) when dividing $k$ by $n$ and, thus, one also calls the elements of $\mathbb{Z}_{n}$ residue classes. Here, the canonical homomorphism of Th. 4.27(a) takes the form  

$$
\phi:\mathbb{Z}\longrightarrow\mathbb{Z}_{n},\quad\phi(r):=\bar{r}=r+n\mathbb{Z}.
$$  

We also note that  

$$
\mathbb{Z}=\bigcup_{r=0}^{n-1}\bar{r}.
$$  

Now consider. $G:=\{0,\ldots,n-1\}$ and define an addition $\bigoplus$ on $G$ by letting  

$$
\begin{array}{r l}{\underset{r,s\in G}{\forall}}&{r\oplus s:=\left\{{r+s\mathrm{~for~}r+s\leq n-1},\atop{r+s-n}}\right.}\end{array}
$$  

which is commutative due to $(\mathbb{Z},+)$ being commutative. We claim $(G,\oplus)\cong(\mathbb{Z}_{n},+)$ due to the isomorphism $f:G\longrightarrow\mathbb{Z}_{n}$ $f(r):={\bar{r}}$ . If $r,s\in G$ , then.  

$$
{\begin{array}{r l}&{f(r\oplus s)=f(r+s)={\overline{{r+s}}}={\bar{r}}+{\bar{s}}=f(r)+f(s)\quad{\mathrm{for~}}r+s\leq n-1,}\ &{f(r\oplus s)=f(r+s-n)={\overline{{r+s-n}}}={\overline{{r+s}}}={\bar{r}}+{\bar{s}}}\ &{\qquad=f(r)+f(s)\quad{\mathrm{for~}}n\leq r+s\leq2n-2,}\end{array}}
$$  

showing $f$ to be a homomorphism. Moreover, if $r\neq s$ , then $\bar{r}\neq\bar{s}$ , i.e. $f$ is injective, while (4.30) shows $f$ to be surjective, completing the proof that $f$ is an isomorphism. In particular, $(G,\oplus)$ is a group, due to Th. 4.11(c). Even though it constitutes a slight abuse of notation, we will tend to use the isomorphism $f$ to identify $G$ with $\mathbb{Z}_{n}$ , where we write simply $^+$ instead of $\bigoplus$ and write $r$ instead of $r$ , identifying $r$ with its standard representative $r\in r$ . The Cayley tables for $(\mathbb{Z}_{1},+)$ and $(\mathbb{Z}_{2},+)$ are  

$$
{\frac{+\mid0}{0\mid0}},\qquad{\frac{+\mid0\quad1}{0\mid0\mid}},
$$  

respectively. Comparing with Ex. 4.14(a), we see that $\phi_{1}:\mathbb{Z}_{1}\longrightarrow\{e\}$ $\phi_{1}(0):=e$ and $\phi_{2}:\mathbb{Z}_{2}\longrightarrow\{e,a\}$ $\phi_{2}(0):=e$ $\phi_{2}(1):=a$ , are isomorphisms.  

(b) Let $m,n\in\mathbb{N}$ . As example for an application of the isomorphism theorem of Th. 4.27(b), we show  

$$
m\mathbb{Z}/m n\mathbb{Z}\cong\mathbb{Z}_{n}:
$$  

Consider the map  

$$
\phi:m\mathbb{Z}\longrightarrow\mathbb{Z}_{n},\quad\phi(m r):=r+n\mathbb{Z}.
$$  

Then $\phi$ is a homomorphism, since  

$\begin{array}{r l}{\underset{\mathcal{A}^{-}}{\bigtriangledown}}&{{}\phi(m r+m s)=\phi(m(r+s))=r+s+n\mathbb{Z}=(r+n\mathbb{Z})+(s+n\mathbb{Z})=\phi(m r)+\phi(m+n\mathbb{Z})=\mathbb{Z}(m+n\mathbb{Z}).}\end{array}$ (s). r,sEZ  

Clearly, $\phi$ is surjective, i.e. $\operatorname{Im}\phi=\mathbb{Z}_{n}$ . Moreover,  

$$
m r\in\ker\phi\quad\Leftrightarrow\quad r\in n\mathbb{Z}\quad\Leftrightarrow\quad\enspace\enspace\underline{{\exists}}\enspace r=k n\quad\Leftrightarrow\quad\:m r=m k n\in m n\mathbb{Z},
$$  

showing $\ker\phi=m n\mathbb{Z}$ . In consequence,. $m\mathbb{Z}/m n\mathbb{Z}\cong\mathbb{Z}_{n}$ holds due to Th. 4.27(b).  

### 4.2 Rings and Fields  

While groups are already sufficiently rich to give rise to the vast algebraic discipline. called group theory, before we can define vector spaces, we still need to consider structures called rings and fields (where fields are rings that are especially benign). Rings. are richer and, in general, more complicated than groups, as they always come with two compositions instead of just one..  

Definition 4.29. Let. $R$ be a nonempty set with two composition maps  

$$
\begin{array}{r l}{+\colon R\times R\longrightarrow R,}&{{}(x,y)\mapsto x+y,}\ {\cdot\colon R\times R\longrightarrow R,}&{{}(x,y)\mapsto x\cdot y}\end{array}
$$  

- $^+$ is called addition and : is called multiplication; as before, one often writes $x y$ instead of $x\cdot y$ ). Then $(R,+,\cdot)$ (or just $R$ , if $^+$ and : are understood) is called a ring if, and only if, the following three conditions are satisfied:  

(i) $(R,+)$ is a commutative group (its neutral element is denoted by 0).  

(ii) Multiplication is associative.  

(iii) Distributivity:  

$$
\begin{array}{r}{\forall_{x\cdot(y+z)=x\cdot y+x\cdot z,}}\ {\forall_{x,y,z\in R}\left(y+z\right)\cdot x=y\cdot x+z\cdot x.}\end{array}
$$  

A ring $R$ is called commutative if, and only if, its multiplication is commutative. Moreover, a ring is called a ring with unity if, and only if, $R$ contains a neutral element with respect to multiplication (i.e. there is $1\in R$ such that $1\cdot x=x\cdot1=x$ for each $x\in R$ - some authors always require a ring to have a neutral element with respect to multiplication. Finally,. $(R,+,\cdot)$ is called a field if, and only if, it is a ring and, in addition, $(R\backslash\{0\},\cdot)$ constitutes a commutative group (its neutral element is denoted by 1). For each $x,y$ in a ring $R$ , define $y-x:=y+(-x)$ , where $-x$ is the additive inverse of. $x$ . If $R$ is a field, then, for. $x\neq0$ , also define the fractions. $\textstyle{\frac{y}{x}}:=y/x:=y x^{-1}$ with numerator $y$ and denominator $x$ , where $x^{-1}$ denotes the multiplicative inverse of $x$  

Like group theory, ring theory and field theory are vast important subdisciplines of algebra. Here we will merely give a brief introduction to some elementary notions and results, before proceeding to vector spaces, which are defined, building on the notion of a field. Before we come to examples of rings and fields, we will prove a number of basic rules. However, it might be useful to already know that, with the usual addition and multiplication, $\mathbb{Z}$ is a ring (but not a field), and $\mathbb{Q}$ $\mathbb{R}$ $\mathbb{C}$ all are fields.  

Theorem 4.30. The following statements and rules are valid in every ring $(R,+,\cdot)$ (let 0 denote the additive neutral element and let. $x,y,z\in R$  

(a) $x\cdot0=0=0\cdot x$  

(b) $x(-y)=-(x y)=(-x)y$ (c) $(-x)(-y)=x y$ (d) $x(y-z)=x y-x z,(y-z)x=y x-z x.$  

Proof. (a): One computes  

$$
\begin{array}{r}{x\cdot0+x\cdot0\stackrel{(4.32\mathrm{a})}{=}x\cdot(0+0)=x\cdot0=0+x\cdot0,}\end{array}
$$  

i.e. $x\cdot0=0$ follows since $(R,+)$ is a group. The second equality follows analogously using (4.32b).  

(b): $x y+x(-y)=x(y-y)=x\cdot0=0$ , where we used (4.32a) and (a). This shows. $x(-y)$ is the additive inverse to. $x y$ . The second equality follows analogously using (4.32b). (c): $x y=-(-(x y))=-(x(-y))=(-x)(-y)$ , where (b) was used twice.. (d): $x(y-z)=x(y+(-z))=x y+x(-z)=x y-x z$ and $(y-z)x=(y+(-z))x=$ $y x+(-z)x=y x-z x$  

Theorem 4.31. The following statement and rules are valid in every field $(F,+,\cdot)$  

(a) $x y=0\Rightarrow x=0\lor y=0.$  

(b) Rules for Fractions:  

$$
{\frac{a}{c}}+{\frac{b}{d}}={\frac{a d+b c}{c d}},{\frac{a}{c}}\cdot{\frac{b}{d}}={\frac{a b}{c d}},{\frac{a/c}{b/d}}={\frac{a d}{b c}},
$$  

where all denominators are $a s s u m e d\ne0$  

Proof. (a): If $x y=0$ and $x\neq0$ , then $y=1\cdot y=x^{-1}x y=x^{-1}\cdot0=0.$  

(b): One computes  

$$
{\frac{a}{c}}+{\frac{b}{d}}=a c^{-1}+b d^{-1}=a d d^{-1}c^{-1}+b c c^{-1}d^{-1}=(a d+b c)(c d)^{-1}={\frac{a d+b c}{c d}}
$$  

and  

and  

$$
{\frac{a}{c}}\cdot{\frac{b}{d}}=a c^{-1}b d^{-1}=a b(c d)^{-1}={\frac{a b}{c d}}
$$  

$$
{\frac{a/c}{b/d}}=a c^{-1}(b d^{-1})^{-1}=a c^{-1}b^{-1}d=a d(b c)^{-1}={\frac{a d}{b c}},
$$  

completing the proof.  

Definition and Remark 4.32. Let $(R,+,\cdot)$ be a ring and $a\in R$ . Then $a$ is called a left (resp. right) zero divisor if, and only if, there exists $x\in R\setminus\{0\}$ such that $a x=0$ (resp. $x a=0$ ). If $a\neq0$ is a zero divisor, then it is called a nonzero or nontrivial zero divisor. According to Th. 4.30(a), 0 is always a zero divisor, except for $R=\left\{0\right\}$ .According to Th. 4.31(a), in a field, there do not exist any nontrivial zero divisors. However, in general, rings can have nontrivial zero divisors (see, e.g. Ex. 4.38 and Ex. 4.42(a) below).  

Example 4.33 (Ring of Integers. $\mathbb{Z}$ ). Even though we have occasionally already used multiplication on $\mathbb{Z}$ in examples, so far, we have not provided a mathematically precise. definition. The present example, will remedy this situation. Recall from Ex. 2.36(a) and Th. 4.15 the definition of $\mathbb{Z}$ as a set of equivalence classes of elements of. $\mathbb{N}_{0}\times\mathbb{N}_{0}$ with addition (and subtraction) on. $\mathbb{Z}$ defined according to (4.17). To obtain the expected laws of arithmetic, multiplication on. $\mathbb{Z}$ needs to be defined such that $(a-b)\cdot(c-d)=$ $(a c+b d)-(a d+b c)$ , which leads to the following definition: Multiplication on. $\mathbb{Z}$ is defined by  

$$
\cdot:\mathbb{Z}\times\mathbb{Z}\longrightarrow\mathbb{Z},\quad([a,b],[c,d])\mapsto[a,b]\cdot[c,d]:=[a c+b d,a d+b c].
$$  

(a) It is an exercise to show the definition in (4.33) does not depend on the chosen representatives, i.e.  

$$
\operatorname*{\forall}_{\substack{\{b,c,d,\tilde{a},\tilde{b},\tilde{c},\tilde{d}\in\mathbb{N}_{0}}}}\left([a,b]=[\tilde{a},\tilde{b}]\wedge[c,d]=[\tilde{c},\tilde{d}]\Rightarrow[a c+b d,a d+b c]=[\tilde{a}\tilde{c}+\tilde{b}\tilde{d},\tilde{a}\tilde{d}+\tilde{b}\tilde{d}]\right).
$$  

(b) It is an exercise to show. $(\mathbb{Z},+,\cdot)$ is a commutative ring with unity, where. $[1,0]$ is the neutral element of multiplication, and there are no nontrivial zero divisors i.e.  

$$
\begin{array}{r}{\underset{\substack{,b,c,d\in\mathbb{N}_{0}}}{\forall}\quad\left([a,b]\cdot[c,d]=[a c+b d,a d+b c]=[0,0]\quad\Rightarrow\quad[a,b]=[0,0]\vee[c,d]=[0,0]\wedge[0,1]\right).}\end{array}
$$  

(c) $(\mathbb{Z},+,\cdot)$ is not a field, since, e.g., there is no multiplicative inverse for $2\in\mathbb Z$ : While $0\cdot2=0$ , one has $n\cdot2\geq2$ for each $n\in\mathbb N$ and $-n\cdot2\leq-2$ for each $n\in\mathbb N$ , showing $k\cdot2\ne1$ for each $k\in\mathbb{Z}$  

Definition 4.34. (a) Let $(R,+,\cdot)$ be a ring (resp. a field), $\varnothing\ne U\subseteq R$ .We call $U$ a subring (resp. a subfield) of $R$ if, and only if,. $(U,+,\cdot)$ forms a ring (resp. a field), where the compositions on $U$ are the respective restrictions of the compositions on $R$ , i.e. $+\lceil\upsilon\times U$ and $\cdot\left\lceil\boldsymbol{U}\times\boldsymbol{U}\right\rceil$  

(b) Let $(R,+,\cdot)$ and $(S,+,\cdot)$ be rings (caveat: to simplify notation, we use the same. symbols to denote the compositions on. $R$ and $S$ , respectively; however, they might even denote different compositions on the same set. $R=S$ ). A map $\phi:R\longrightarrow S$ is called ring homomorphism if, and only if, $\phi$ is a homomorphism in the sense of. Def. 4.10 with respect to both $^+$ and : (caveat: Ex. 4.36(a) below shows that a ring homomorphism is not necessarily unital with respect to multiplication). The. notions ring monomorphism, epimorphism, isomorphism, endomorphism, automorphism are then defined as in Def. 4.10. Moreover, $(R,+,\cdot)$ and $(S,+,\cdot)$ are called isomorphic (denoted $(R,+,\cdot)\cong(S,+,\cdot))$ if, and only if, there exists a ring isomor-. phism $\phi:R\longrightarrow S$  

Theorem 4.35. (a) Let $(R,+,\cdot)$ be a ring, $\varnothing\neq U\subseteq R$ . Then $U$ is a subring of $R$ if, and only if, (i) and (ii) hold, where (i) $(U,+)$ is a subgroup of $(R,+)$ (ii) For each $a,b\in U$ , one has $a b\in U$   
(b) Let $(F,+,\cdot)$ be a field, $\varnothing\neq U\subseteq F$ . Then $U$ is a subfield of $F^{\prime}$ if, and only if, (i) and (ii) hold, where (i) $(U,+)$ is a subgroup of $(F,+)$ (ii) $(U\setminus\{0\},\cdot)$ is a subgroup of $(F\backslash\{0\},\cdot)$  

Proof. In both cases, it is clear that (i) and (ii) are necessary. That (i) and (ii) are also sufficient in both cases is due to the fact that, if associativity (resp. commutativity, resp. distributivity) hold on $R$ (resp. $F$ ), then it is immediate that the same property holds on $U$  

Example 4.36. (a) Clearly, the trivial ring. $(\{0\},+,\cdot)$ $\cong(\mathbb{Z}_{1},+,\cdot)$ , see Ex. 4.38 below) is a subring of every ring (it is not a field, since. $\{0\}\setminus\{0\}=\emptyset$ is not a group). If $R$ and $S$ are arbitrary rings, then, clearly, the constant map. $\phi_{0}:R\longrightarrow S$ $\phi_{0}\equiv0$ , is always a ring homomorphism (this shows that a ring homomorphism is not necessarily unital with respect to multiplication). Also note that Th. 4.30(a) implies that any ring that has. $0=1$ (in the sense that the neutral elements for addition and multiplication are the same) has necessarily precisely one element, i.e. it is (isomorphic to). $(\{0\},+,\cdot)$  

(b) Let $n\in\mathbb{N}$ . It is clear from Th. 4.35(a) that. $n\mathbb{Z}$ is a subring of. $\mathbb{Z}$ (note that, for. $n>1$ $n\mathbb{Z}$ is not a ring with unity). Moreover, for $n>1$ $\phi:\mathbb{Z}\longrightarrow n\mathbb{Z}$ $\phi(k):=n k$ is not a ring homomorphism, since, e.g. $\phi(1\cdot1)=n\neq n^{2}=\phi(1)\phi(1)$  

(c) If $R,S$ are arbitrary rings and $\phi:R\longrightarrow S$ is a ring homomorphism, then it is clear from Th. 4.35(a) that $\operatorname{Im}\phi$ is a subring of. $S$ . Moreover, $\ker\phi:=\phi^{-1}(\{0\})$ is a subring of. $R$ : This is also due to Th. 4.35(a), since $(\ker\phi,+)\leq(R,+)$ and, if $a,b\in\ker\phi$ , then $\phi(a b)=\phi(a)\phi(b)=0$ , showing $a b\in\ker\phi$ . However, if. $R$ and $S$ are rings with unity, and $\phi(1)=1$ , then $\ker\phi$ is a ring with unity if, and only if, $S=\{0\}$ : Indeed, if $1\in\ker\phi$ , then $0=\phi(1)=1$ in $S$  

(d) Let $(R,+,\cdot)$ be a ring with unity. We claim that the group homomorphism $\phi_{1}$ of Ex. 4.12(c) extends to a unital ring homomorphism.  

$$
\phi_{1}:\mathbb{Z}\longrightarrow R,\quad\phi_{1}(n):={\left\{\begin{array}{l l}{n\cdot1=\sum_{i=1}^{n}1}&{{\mathrm{for~}}n\geq1,}\ {0}&{{\mathrm{for~}}n=0,}\ {-((-n)\cdot1)}&{{\mathrm{for~}}n\leq-1}\end{array}\right.}
$$  

(note that this is precisely the definition from Not. 4.7 (setting. $x:=1$ in Not. 4.7), except that, in Not. 4.7, the composition was written as multiplication, i.e. $x^{n}$ Of Not. 4.7 here becomes $\textstyle n\cdot x=\sum_{i=1}^{n}x)$ : Indeed,  

$$
\forall_{\stackrel{n\in\mathbb{Z}}{n\in\mathbb{Z}}}\phi_{1}(m n)=(m n)\cdot1^{\mathrm{\tiny~Th}}\stackrel{4.8(\cdot)}{=}n\cdot(m\cdot1)=\sum_{i=1}^{n}\phi_{1}(m)=\phi_{1}(m)\sum_{i=1}^{n}1=\phi_{1}(m)\phi_{1}(m).
$$  

(e) Let $(R,+,\cdot)$ be a ring (resp. a ring with unity, resp. a field), let $I\neq\emptyset$ be an index set, and let. $(U_{i})_{i\in I}$ be a family of subrings (resp. of subrings with unity, resp. of subfields). It is then an exercise to show $\begin{array}{r}{U:=\bigcap_{i\in I}U_{i}}\end{array}$ is a subring (resp. a subring. with unity, resp. a subfield)..  

(f) In contrast to intersections, unions of rings are not necessarily rings (however, cf. (g) below): We know from (b) that $2\mathbb{Z}$ and $3\mathbb{Z}$ are subrings of $\mathbb{Z}$ . But we already. noted in Ex. 4.18(e) that $({\mathrm{2\mathbb{Z}}})\cup({\mathrm{3\mathbb{Z}}})$ is not even a subgroup of $(\mathbb{Z},+)$ . To show that the union of two fields is not necessarily a field (not even a ring, actually), needs slightly more work: We use that $\mathbb{Q}$ is a subfield of. $\mathbb{R}$ (cf. Rem. 4.40 below) and show that, for each $x\in\mathbb R$ with $x^{2}\in\mathbb{Q}$ $\mathbb{Q}(x):=\{r+s x\colon r,s\in\mathbb{Q}\}$ is a subfield of $\mathbb{R}$ (clearly, $\mathbb{Q}(x)=\mathbb{Q}$ if, and only if, $x\in\mathbb{Q}$ ): Setting $r=s=0$ , shows $0\in\mathbb{Q}(x)$  

Setting $r=1$ $s=0$ , shows $1\in\mathbb{Q}(x)$ . If $r_{1},s_{1},r_{2},s_{2}\in\mathbb{Q}$ , then  

$$
\begin{array}{r l}&{r_{1}+s_{1}x+r_{2}+s_{2}x=r_{1}+r_{2}+(s_{1}+s_{2})x\in\mathbb{Q}(x),}\ &{(r_{1}+s_{1}x)(r_{2}+s_{2}x)=r_{1}r_{2}+s_{1}s_{2}x^{2}+(s_{1}r_{2}+r_{1}s_{2})x\in\mathbb{Q}(x),}\ &{\qquad-(r_{1}+s_{1}x)=-r_{1}-s_{1}x\in\mathbb{Q}(x),}\ &{\qquad(r_{1}+s_{1}x)^{-1}=\displaystyle\frac{r_{1}-s_{1}x}{r_{1}^{2}-s_{1}^{2}x^{2}}\in\mathbb{Q}(x),}\end{array}
$$  

showing $\mathbb{Q}(x)$ to be a subfield of. $\mathbb{R}$ by Th. 4.35(b). However, e.g., $U:=\mathbb{Q}({\sqrt{2}})\cup$ $\mathbb{Q}({\sqrt{3}})$ is not even a ring, since. $\alpha:={\sqrt{2}}+{\sqrt{3}}\notin U$ .. $\alpha\not\in\mathbb{Q}({\sqrt{2}})$ since, otherwise,. there are $r,s\in\mathbb{Q}$ with $\alpha=r+s\sqrt{2}$ , i.e. $\sqrt{3}=r+(s-1)\sqrt{2}$ , and $3=r^{2}+2r(s-$ $1){\sqrt{2}}+2(s-1)^{2}$ , implying the false statement  

$$
3=0\vee{\sqrt{3}}\in\mathbb{Q}\vee{\sqrt{3/2}}\in\mathbb{Q}\vee{\sqrt{2}}\in\mathbb{Q}.
$$  

Switching the roles of $\sqrt{2}$ and $\sqrt{3}$ , shows. $\alpha\not\in\mathbb{Q}(\sqrt{3})$ , i.e. $\alpha\notin U$ (g) While (f) shows that unions of subrings (or even subfields) are not necessarily. subrings, if $(R,+,\cdot)$ is a ring (resp. a ring with unity, resp. a field),. $I\neq\emptyset$ is an index set, partially ordered by. $\leq$ in a way such that, for each. $i,j\in I$ , there exists $k\in I$ with $i,j\leq k$ (if $I$ is totally ordered by $\leq$ , then one can use. $k:=\operatorname*{max}\{i,j\})$ and $(U_{i})_{i\in I}$ is an increasing family of subrings (resp. of subrings with unity, resp. of subfields) (i.e., for each $i,j\in I$ with $i\leq j$ , one has $U_{i}\subseteq U_{j}$ ), then $U:=\cup_{i\in I}U_{i}$ is a subgroup (resp. a subring with unity, resp. a subfield) as well: Indeed, according to Ex. 4.18(f), $(U,+)\leq(R,+)$ . If $a,b\in U$ , then there exist $i,j\in I$ such that $a\in U_{i}$ and $b\in U_{j}$ . If $k\in{I}$ with $i,j\leq k$ , then $a b\in U_{k}\subseteq U$ , i.e. $U$ is a ring by Th. 4.35(a). If $1\in U_{i}$ , then $1\in U$ . If each $\left(U_{i}\backslash\{0\},\cdot\right)$ is a group, then. $(U\backslash\{0\},\cdot)$ is a group by Ex. 4.18(f), showing. $U$ to be a subfield by Th. 4.35(b).  

We can extend Prop. 4.11(c) to rings and fields:  

Proposition 4.37. Let A be a nonempty set with compositions $^+$ and ., and let $B$ be a nonempty set with compositions. $^+$ and . (caveat: to simplify notation, we use the. same symbols to denote the compositions on. $R$ and $S$ ,respectively; however, they might even denote different compositions on the same set. $A=B$ ).If $\phi:{\cal A}\longrightarrow{\cal B}$ is an epimorphism with respect to both $^+$ and :, then  

$$
\begin{array}{r c l}{{(A,+,\cdot)s a t i s f e s~(4.32a)}}&{{\Rightarrow}}&{{(B,+,\cdot)~s a t i s f e s~(4.32a),}}\ {{(A,+,\cdot)s a t i s f e s~(4.32b)}}&{{\Rightarrow}}&{{(B,+,\cdot)~s a t i s f t e s~(4.32b),}}\ {{(A,+,\cdot)~r i n g}}&{{\Rightarrow}}&{{(B,+,\cdot)~r i n g,}}\ {{(A,+,\cdot)r i n g~w i t h~u n i t y}}&{{\Rightarrow}}&{{(B,+,\cdot)~r i n g~w i t h~u n i t y,}}\ {{(A,+,\cdot)~f i e l d}}&{{\Rightarrow}}&{{(B,+,\cdot)~f i e l d~i f B\neq\{0\}.}}\end{array}
$$  

If $\phi$ is even an isomorphism with respect to $b o t h+\:a n d$ :, then the above implications become equivalences.  

Proof. Let $b_{1},b_{2},b_{3}\in B$ with preimages $a_{1},a_{2},a_{3}\in A$ , respectively. If $(A,+,\cdot)$ satisfies (4.32a), then  

$$
\begin{array}{r l}&{\mathrm{\i}_{1}\cdot(b_{2}+b_{3})=\phi(a_{1})\cdot\big(\phi(a_{2})+\phi(a_{3})\big)=\phi\big(a_{1}\cdot(a_{2}+a_{3})\big)=\phi(a_{1}\cdot a_{2}+a_{1}\cdot a_{3})}\ &{\mathrm{\it~=~}\phi(a_{1})\cdot\phi(a_{2})+\phi(a_{1})\cdot\phi(a_{3})=b_{1}\cdot b_{2}+b_{1}\cdot b_{3},}\end{array}
$$  

showing $(B,+,\cdot)$ satisfies (4.32a) as well. If $(A,+,\cdot)$ satisfies (4.32b), then  

$$
\begin{array}{r l}&{\mathbf{\ddot{\rho}}_{b_{2}}+b_{3})\cdot b_{1}=\left(\phi(a_{2})+\phi(a_{3})\right)\cdot\phi(a_{1})=\phi\big((a_{2}+a_{3})\cdot a_{1}\big)=\phi(a_{2}\cdot a_{1}+a_{3}\cdot a_{1})}\ &{\qquad=\phi(a_{2})\cdot\phi(a_{1})+\phi(a_{3})\cdot\phi(a_{1})=b_{2}\cdot b_{1}+b_{3}\cdot b_{1},}\end{array}
$$  

showing $(B,+,\cdot)$ satisfies (4.32b) as well. If $(A,+,\cdot)$ is a ring, then we know from Prop. $4.11(\mathrm{c})$ that $(B,+)$ is a commutative group and that $(B,\cdot)$ is associative, showing that $(B,+,\cdot)$ is a ring as well. If $(A,+,\cdot)$ is a ring with unity, then the above and Prop. 4.11(d) imply $(B,+,\cdot)$ to be a ring with unity as well. If $(A,+,\cdot)$ is a field, then, as $B\setminus\{0\}\ne\emptyset$ $(B\setminus\{0\},\cdot)$ must also be a group, i.e. $(B,+,\cdot)$ is a field. Finally, if $\phi$ is an isomorphism, then the implications become equivalences, as both $\phi$ and $\phi^{-1}$ are epimorphisms by Prop. 4.11(b) (and since $\phi(0)=0$ : $\vert$  

Example 4.38. Let $n\in\mathbb N$ . In Ex. 4.28(a), we considered the group. $(\mathbb{Z}_{n},+)$ , where $\mathbb{Z}_{n}$ was defined as the quotient group $\mathbb{Z}_{n}:=\mathbb{Z}/n\mathbb{Z}$ . We now want to define a multiplication. on $\mathbb{Z}_{n}$ that makes. $\mathbb{Z}_{n}$ into a ring with unity (and into a field if, and only if, $n$ is prime, cf. Def. D.2(b)). This is accomplished by letting.  

$$
\begin{array}{r l}{\underset{r,s\in\mathbb{Z}}{\forall}}&{{}\bar{r}\cdot\bar{s}=(r+n\mathbb{Z})\cdot(s+n\mathbb{Z}):=\overline{{r s}}=r s+n\mathbb{Z}:}\end{array}
$$  

First, we check that the definition does not depend on the chosen representatives: Let $r_{1},r_{2},s_{1},s_{2}\in\mathbb{Z}$ .If $r_{1}~=~r_{2}$ and $s_{1}~=~s_{2}$ , then there exist $m_{r},m_{s}\in\mathbb{Z}$ such that $r_{1}-r_{2}=m_{r}n$ and $s_{1}-s_{2}=m_{s}n$ , implying  

$$
\begin{array}{r l}&{\bar{r}_{1}\cdot\bar{s}_{1}=r_{1}s_{1}+n\mathbb{Z}=(r_{2}+m_{r}n)(s_{2}+m_{s}n)+n\mathbb{Z}}\ &{\qquad=r_{2}s_{2}+(m_{r}s_{2}+m_{s}r_{2}+m_{r}m_{s}n)n+n\mathbb{Z}=r_{2}s_{2}+n\mathbb{Z}=\bar{r}_{2}\cdot\bar{s}_{2},}\end{array}
$$  

as desired. We already know the canonical homomorphism  

$$
\phi:\mathbb{Z}\longrightarrow\mathbb{Z}_{n},\quad\phi(r)=\bar{r}=r+n\mathbb{Z}
$$  

to be a homomorphism with respect to addition. Since  

$$
\begin{array}{r l}{\underset{r,s\in\mathbb{Z}}{\forall}}&{{}\phi(r s)=\overline{{r s}}=\bar{r}\cdot\bar{s}=\phi(r)\cdot\phi(s),}\end{array}
$$  

it is also a homomorphism with respect to the above-defined multiplication. Since $\phi$ is also surjective, $(\mathbb{Z}_{n},+,\cdot)$ is a ring with unity by Prop. 4.37. Now suppose that $n$ is not prime. If $n=1$ , then $\#\mathbb{Z}_{1}=1$ , i.e. it is (isomorphic) to the trivial ring of Ex. 4.36(a). If $n=a b$ with $a,b\in\mathbb{N}$ $1<a,b<n$ , then  

$$
\bar{a}\cdot\bar{b}=\bar{n}=\bar{0},
$$  

showing $a$ and $b$ to be nontrivial divisors of $0$ (in $\mathbb{Z}_{n}$ ). In particular, $(\mathbb{Z}_{n},+,\cdot)$ is not a field. Now consider the case that $n$ is prime. If $r\in\mathbb{Z}$ and $\bar{r}\neq0$ , then $\operatorname*{gcd}(r,n)=1$ (cf. Def. D.2(c)) and, by (D.6) of the Appendix, there exist $x,y\in\mathbb{Z}$ with $x n+y r=1$ Then  

$$
{\bar{y}}\cdot{\bar{r}}={\overline{{y r}}}={\overline{{1-x n}}}={\overline{{1}}},
$$  

showing $y$ to be the multiplicative inverse to $r$ . Thus, $\left(\mathbb{Z}_{n}\backslash\{0\},\cdot\right)$ is a group and $(\mathbb{Z}_{n},+,\cdot)$ is a field. For the rest of the example, we, once again, allow an arbitrary. $n\in\mathbb{N}$ .In Ex. 4.28(a), we showed that, letting $G:=\{0,\ldots,n-1\}$ , we had $(G,+)\cong(\mathbb{Z}_{n},+)$ We now want to extend this isomorphism to a ring isomorphism. To this end, define a multiplication $\bigotimes$ on $G$ by letting  

$$
\begin{array}{r}{\underset{r,s\in G}{\forall}\quad r\otimes s:=p,\quad\mathrm{where~}r s=q n+p\mathrm{~with~}q,p\in\ensuremath{\mathbb{N}}_{0}\mathrm{~and~}0\leq p<n(\mathrm{cf.~}\ensuremath{\mathbb{N}})}\end{array}
$$  

which is commutative due to $(\mathbb{Z},+)$ being commutative. We claim the additive isomorphism $f:G\longrightarrow\mathbb{Z}_{n}$ $f(r):={\bar{r}}$ , of Ex. 4.28(a) to be a multiplicative isomorphism as well: If $r,s\in G$ , then, using $q,p$ as above,  

$$
f(r\otimes s)=f(p)={\bar{p}}={\overline{{r s-q n}}}={\overline{{r s}}}={\bar{r}}\cdot{\bar{s}}=f(r)f(s),
$$  

showing $f$ to be a multiplicative homomorphism. As we know $f$ to be bijective,. $(G,+,\cdot)$ is a ring by Prop. 4.37, yielding. $(G,+,\otimes)\cong(\mathbb{Z}_{n},+,\cdot)$ . As stated in Ex. 4.28(a) in the. context of $(\mathbb{Z}_{n},+)$ , one tends to use the isomorphism. $f$ to identify $G$ with $\mathbb{Z}_{n}$ . One does the same in the context of. $(\mathbb{Z}_{n},+,\cdot)$ , also simply writing . for the multiplication on $G$  

Example 4.39 (Field of Rational Numbers $\mathbb{Q}$ ). In Ex. 2.36(b), we defined the set of.   
rational numbers $\mathbb{Q}$ as the quotient set of. $\mathbb{Z}\times(\mathbb{Z}\setminus\{0\})$ with respect to the equivalence.   
relation defined by.  

$$
(a,b)\sim(c,d)\quad:\Leftrightarrow\quad a\cdot d=b\cdot c.
$$  

We now want to define "the usual' addition and multiplication on $\mathbb{Q}$ and then verify that these make $\mathbb{Q}$ into a field (recall the notation. $\begin{array}{r}{\frac{a}{b}:=a/b:=[(a,b)])}\end{array}$  

Addition on $\mathbb{Q}$ is defined by  

$$
+:\mathbb{Q}\times\mathbb{Q}\longrightarrow\mathbb{Q},\quad\left({\frac{a}{b}},{\frac{c}{d}}\right)\mapsto{\frac{a}{b}}+{\frac{c}{d}}:={\frac{a d+b c}{b d}}.
$$  

Multiplication on $\mathbb{Q}$ is defined by  

$$
\quad\cdot:\mathbb{Q}\times\mathbb{Q}\longrightarrow\mathbb{Q},\quad\left({\frac{a}{b}},{\frac{c}{d}}\right)\mapsto{\frac{a}{b}}\cdot{\frac{c}{d}}:={\frac{a c}{b d}}.
$$  

We will now show that $(\mathbb{Q},+,\cdot)$ forms a field, where $0/1$ and $1/1$ are the neutral elements with respect to addition and multiplication, respectively, $\left(-a/b\right)$ is the additive inverse. to $a/b$ , whereas $b/a$ is the multiplicative inverse to. $a/b$ with $a\neq0$ .We already know from Ex. 2.36(b) that the map  

$$
\iota:\mathbb{Z}\longrightarrow\mathbb{Q},\quad\iota(k):=\frac{k}{1},
$$  

is injective. We will now also show it is a unital ring monomorphism, i.e. it satisfies $\iota(1)={\textstyle{\frac{1}{1}}}$  

$$
\begin{array}{r l}{\underset{k,l\in\mathbb{Z}}{\forall}}&{\iota(k+l)=\iota(k)+\iota(l),}\ {\underset{k,l\in\mathbb{Z}}{\forall}}&{\iota(k l)=\iota(k)\cdot\iota(l).}\end{array}
$$  

We begin by showing that the definitions in (4.37) and (4.38) do not depend on the chosen representatives, i.e.  

$$
\forall_{a,c,\tilde{a},\tilde{c}\in\mathbb{Z}}\quad\underset{b,d,\tilde{b},\tilde{d}\in\mathbb{Z}\backslash\{0\}}{\forall}\quad\left(\frac{a}{b}=\frac{\tilde{a}}{\tilde{b}}\wedge\frac{c}{d}=\frac{\tilde{c}}{\tilde{d}}\quad\Rightarrow\quad\frac{a d+b c}{b d}=\frac{\tilde{a}\tilde{d}+\tilde{b}\tilde{c}}{\tilde{b}\tilde{d}}\right)
$$  

and  

$$
\bigvee_{a,c,\tilde{a},\tilde{c}\in\mathbb{Z}\quad b,d,\tilde{b},\tilde{d}\in\mathbb{Z}\backslash\{0\}}\quad\left(\frac{a}{b}=\frac{\tilde{a}}{\tilde{b}}\wedge\frac{c}{d}=\frac{\tilde{c}}{\tilde{d}}\quad\Rightarrow\quad\frac{a c}{b d}=\frac{\tilde{a}\tilde{c}}{\tilde{b}\tilde{d}}\right).
$$  

Furthermore, the results of both addition and multiplication are always elements of $\mathbb{Q}$ (4.40) and (4.41): $a/b=\tilde{a}/\tilde{b}$ means $\boldsymbol{a}\boldsymbol{\tilde{b}}=\boldsymbol{\tilde{a}}\boldsymbol{b}$ $c/d=\tilde{c}/\tilde{d}$ means $c\tilde{d}=\tilde{c}d$ , implying  

$$
(a d+b c)\tilde{b}\tilde{d}=b d(\tilde{a}\tilde{d}+\tilde{b}\tilde{c}),\quad\mathrm{i.e.}\quad\frac{a d+b c}{b d}=\frac{\tilde{a}\tilde{d}+\tilde{b}\tilde{c}}{\tilde{b}\tilde{d}}
$$  

and  

$$
a c\tilde{b}\tilde{d}=b d\tilde{a}\tilde{c},\quad\mathrm{i.e.}\quad\frac{a c}{b d}=\frac{\tilde{a}\tilde{c}}{\tilde{b}\tilde{d}}.
$$  

That the results of both addition and multiplication are always elements of $\mathbb{Q}$ follows from (4.35), i.e. from the fact that $\mathbb{Z}$ has no nontrivial zero divisors. In particular, if $b,d\neq0$ , then $b d\neq0$ , showing. $(a d+b c)/(b d)\in\mathbb{Q}$ and $(a c)/(b d)\in\mathbb{Q}$  

Next, we verify. $^+$ and : to be commutative and associative on $\mathbb{Q}$ : Let $a,c,e\in\mathbb{Z}$ and $b,d,f\in\mathbb{Z}\setminus\{0\}$ . Then, using commutativity on. $\mathbb{Z}$ , we compute  

$$
{\frac{c}{d}}+{\frac{a}{b}}={\frac{c b+d a}{d b}}={\frac{a d+b c}{b d}}={\frac{a}{b}}+{\frac{c}{d}},\qquad{\frac{c}{d}}\cdot{\frac{a}{b}}={\frac{c a}{d b}}={\frac{a c}{b d}}={\frac{a}{b}}\cdot{\frac{c}{d}},
$$  

showing commutativity on. $\mathbb{Q}$ . Using associativity and distributivity on $\mathbb{Z}$ , we compute  

$$
\begin{array}{r l}&{\frac{a}{b}+\left(\frac{c}{d}+\frac{e}{f}\right)=\frac{a}{b}+\frac{c f+d e}{d f}=\frac{a d f+b(c f+d e)}{b d f}=\frac{(a d+b c)f+b d e}{b d f}}\ &{\hphantom{\frac{a}{b}+\bigg(\frac{c}{d}+\frac{e}{f}\bigg)}=\frac{a d+b c}{b d}+\frac{e}{f}=\left(\frac{a}{b}+\frac{c}{d}\right)+\frac{e}{f},}\ &{\frac{a}{b}\cdot\left(\frac{c}{d}\cdot\frac{e}{f}\right)=\frac{a(c e)}{b(d f)}=\frac{(a c)e}{(b d)f}=\left(\frac{a}{b}\cdot\frac{c}{d}\right)\cdot\frac{e}{f},}\end{array}
$$  

showing associativity on. $\mathbb{Q}$ . We proceed to checking distributivity on. $\mathbb{Q}$ : Using commutativity, associativity, and distributivity on $\mathbb{Z}$ , we compute  

$$
{\frac{\imath}{\cdot}}\left({\frac{c}{d}}+{\frac{e}{f}}\right)={\frac{a(c f+d e)}{b d f}}={\frac{a c f+d a e}{b d f}}={\frac{a c b f+b d a e}{b d b f}}={\frac{a c}{b d}}+{\frac{a e}{b f}}={\frac{a}{b}}\cdot{\frac{c}{d}}+{\frac{a}{b}}
$$  

proving distributivity on $\mathbb{Q}$ .We now check the claims regarding neutral and inverse elements:  

$$
\begin{array}{l}{{\displaystyle\frac{a}{b}+\frac{0}{1}=\frac{a\cdot1+b\cdot0}{b\cdot1}=\frac{a}{b}\mathrm{,}}}\ {{\displaystyle\frac{a}{b}+\frac{-a}{b}=\frac{a b+b(-a)}{b^{2}}=\frac{(a-a)b}{b^{2}}=\frac{0}{b^{2}}=\frac{0}{1}\mathrm{,}}}\ {{\displaystyle\frac{a}{b}\cdot\frac{1}{1}=\frac{a\cdot1}{b\cdot1}=\frac{a}{b}\mathrm{,}}}\ {{\displaystyle\frac{a}{b}\cdot\frac{b}{a}=\frac{a b}{b a}=\frac{1}{1}\mathrm{.}}}\end{array}
$$  

Thus,e $(\mathbb{Q},+,\cdot)$ is a ring and. $(\mathbb{Q}\setminus\{0\},\cdot)$ is a group, implying $\mathbb{Q}$ to be a field. Finally  

$$
\begin{array}{l}{\displaystyle\iota(k)+\iota(l)=\frac{k}{1}+\frac{l}{1}=\frac{k\cdot1+1\cdot l}{1}=\frac{k+l}{1}=\iota(k+l),}\ {\displaystyle\iota(k)\cdot\iota(l)=\frac{k}{1}\cdot\frac{l}{1}=\frac{k l}{1}=\iota(k l),}\end{array}
$$  

proving (4.39).  

Remark 4.40. With the usual addition and multiplication, $(\mathbb{R},+,\cdot)$ and $\left(\mathbb{C},+,\cdot\right)$ are fields (see [Phi16, Th. D.39] and and [Phi16, Th. 5.2], respectively). In particular, $\mathbb{R}$ is a subfield of $\mathbb{C}$ and $\mathbb{Q}$ is a subfield of both $\mathbb{R}$ and $\mathbb{C}$  

Definition and Remark 4.41. Let $(R,+,\cdot)$ be a ring with unity. We call $x\in R$ invertible if, and only if, there exists ${\overline{{x}}}\in R$ such that $x\overline{{x}}=\overline{{x}}x=1$ .We call $(R^{*},\cdot)$ where $R^{*}:=\{x\in R:x\mathrm{~i~}$ nvertible} the group of invertible elements of $R$ .We verify $(R^{*},\cdot)$ to be a group: If $x,y\in R^{*}$ , then $x y\bar{y}\bar{x}=1$ and $\bar{y}\bar{x}x y=1$ , showing $x y\in R^{*}$ Moreover, $R^{*}$ inherits associativity from $R$ $1\in R^{*}$ and each $x\in R^{*}$ has a multiplicative inverse by definition of $R^{*}$ , proving $(R^{*},\cdot)$ to be a group. We also note that, if $R\neq\{0\}$ then $0\not\in R^{*}$ and $(R^{*},+)$ is not a group (in particular, $R^{*}$ is then not a subring of $R$  

Example 4.42. (a) Let $(R,+,\cdot)$ be a ring and let $M$ be a set. As in Ex. 4.9(e), we can define $^+$ and : pointwise on $R^{M}$ , i.e.  

$$
\begin{array}{r l}{{\forall~}}&{{f+g:~M\longrightarrow R,~(f+g)(x):=f(x)+g(x),}}\ {{\forall~}}&{{f\cdot g\in R^{M}~f\cdot g:~M\longrightarrow R,~(f\cdot g)(x):=f(x)\cdot g(x).}}\end{array}
$$  

As with commutativity and associativity, it is immediate that $R^{M}$ inherits distributivity from $R$ . Thus, $(R^{M},+,\cdot)$ is a ring as well; if. $(R,+,\cdot)$ is a ring with unity,. then so is $(R^{M},+,\cdot)$ , where $f\equiv1$ is neutral for : in $R^{M}$ , and, using the notation of Def. and Rem. 4.41, $(R^{M})^{*}=(R^{*})^{M}$ . We point out that, if $M$ and $R$ both have at least two distinct elements, then $R^{M}$ always has nontrivial divisors of $0$ , even if $R$ has none: Let $x,y\in M$ with $x\neq y$ , and $0\neq a\in R$ . Define  

$$
f_{x},f_{y}:M\longrightarrow R,\quad f_{x}(z):={\left\{\begin{array}{l l}{a}&{{\mathrm{if}}z=x,}\ {0}&{{\mathrm{if}}z\neq x,}\end{array}\right.}\quad f_{y}(z):={\left\{\begin{array}{l l}{a}&{{\mathrm{if}}z=y,}\ {0}&{{\mathrm{if}}z\neq y.}\end{array}\right.}
$$  

Then $f_{x}\not\equiv0$ $f_{y}\not\equiv0$ , but $f_{x}\cdot f_{y}\equiv0$  

(b) Let $(G,+)$ be an abelian group and let. $\operatorname{End}(G)$ denote the set of (group) endomorphisms on. $G$ . Define addition and multiplication on $\operatorname{End}(G)$ by letting, for each. $f,g\in\operatorname{End}(G)$  

$$
\begin{array}{r l}{{(f+g)\colon G\longrightarrow G,}}&{{(f+g)(a):=f(a)+g(a),}}\ {{(f\cdot g)\colon G\longrightarrow G,}}&{{(f\cdot g)(a):=f(g(a)).}}\end{array}
$$  

We claim that $(\operatorname{End}(G),+,\cdot)$ forms a ring with unity (the so-called ring of endo. morphisms on $G$ ): First, we check $^+$ to be well-defined (which is clear for -): For each $a,b\in G$ , we compute, using commutativity of $^+$ on $G$  

$$
f+g)(a+b)=f(a+b)+g(a+b)=f(a)+f(b)+g(a)+g(b)=(f+g)(a)+(f+g)(a)+g(a).
$$  

showing $f+g\in\operatorname{End}(G)$ . As we then know $(\operatorname{End}(G),+)\leq({\mathcal{F}}(G,G),+)$ , we know : to be associative, and Id is clearly neutral for $\cdot$ , it remains to check distributivity:. To this end, let $f,g,h\in\operatorname{End}(G)$ . Then, for each $a\in G$  

$$
\begin{array}{r l}&{\big(f\cdot(g+h)\big)(a)=f\big(g(a)+h(a)\big)=(f g)(a)+(f h)(a)=(f g+f h)(a),}\ &{\big((g+h)\cdot f\big)(a)=(g+h)(f(a))=(g f)(a)+(h f)(a)=(g f+h f)(a),}\end{array}
$$  

proving distributivity and that $(\operatorname{End}(G),+,\cdot)$ forms a ring with unity. Moreover, the. set $\operatorname{Aut}(G):=\operatorname{End}(G)\cap S_{G}$ of automorphisms on. $G$ is a subgroup of the symmetric group $S_{G}$ and, comparing with Def. and Rem. 4.41, we also have $\operatorname{Aut}(G)=\operatorname{End}(G)^{*}$  

Definition and Remark 4.43. Let $(F,+,\cdot)$ be a field. We recall the unital ring homomorphism $\phi_{1}:\mathbb{Z}\longrightarrow F$ from Ex. 4.36(d), where  

$$
\forall_{n\in\mathbb{N}}\phi_{1}(n)=\sum_{i=1}^{n}1=:n\cdot1.
$$  

We say that the field $F^{\prime}$ has characteristic 0 (denoted char $F=0$ ) if, and only if, $n\cdot1\ne0$ for each $n\in\mathbb N$ . Otherwise, we define the field's characteristic to be the number  

$$
\operatorname{char}F:=\operatorname*{min}\{n\in\mathbb{N}:n\cdot1=0\}.
$$  

With this definition, we have char $\mathbb{Q}=\operatorname{char}\mathbb{R}=\operatorname{char}\mathbb{C}=0$ and, for each prime number $p$ $\operatorname{char}\mathbb{Z}_{p}=p$  

The examples above show that. $0$ and each prime number occur as characteristic of fields. It is not difficult to prove that no other numbers can occur:  

Theorem 4.44. Let $F^{\prime}$ be a field. If char $F\neq0$ , then. $p:=\mathrm{char}F$ is a prime number.  

Proof. Suppose $p=a b$ with $a b\in\mathbb{N}$ . As before, we apply the unital ring homomorphism $\phi_{1}:\mathbb{Z}\longrightarrow F$ of Ex. 4.36(d). Since $\phi_{1}$ is a homomorphism, we obtain.  

$$
0=\phi_{1}(p)=\phi_{1}(a b)=\phi_{1}(a)\cdot\phi_{1}(b).
$$  

As the field $F$ has no nontrivial zero divisors, we must have $\phi_{1}(a)=0$ or $\phi_{1}(b)=0$ . But $p=\operatorname*{min}\{n\in\mathbb{N}:\phi_{1}(n)=0\}$ , implying $a=p$ or $b=p$ , showing $p$ to be prime.  

Lemma 4.45. If $(F,+,\cdot)$ is a field and $K\subseteq F$ is a subfield, then char $K=\operatorname{char}F$ (in particular, if char $F=0$ (e.g. $F=\mathbb{Q}$ or $F=\mathbb{R}$ or $F=\mathbb{C}$ ), then $F^{\prime}$ does not have any finite subfields).  

Proof. Suppose $K\subseteq F$ is a subfield. If char. $K=n\in\mathbb{N}$ , then $\textstyle\sum_{i=1}^{n}1=0$ in $K$ and, thus, in $F$ , since addition on. $K$ is the restriction of the addition on $F^{\prime}$ . If char $K=0$ then $\textstyle\sum_{i=1}^{n}1\neq0$ in $K$ for each $n\in\mathbb{N}$ . Thus, again, the same must hold in. $F$ , since addition on $K$ is the restriction of the addition on $F^{\prime}$  

Remark and Definition 4.46. Let $(F,+,\cdot)$ be a field. Let $P$ be the intersection of. all subfields of $F$ .As a consequence of Ex. 4.36(e), $P$ is a subfield of $F$ . The field $P$ is called the prime field of. $F^{\prime}$ and is, clearly, the smallest subfield contained in $F^{\prime}$ . One can show that $P\cong\mathbb Z_{p}$ if, and only if, char $F=p\in\mathbb{N}$ (these prime fields are often also. denoted as $\mathbb{F}_{p}$ in the algebraic literature);. $P\cong\mathbb{Q}$ if, and only if, char $F=0$ (cf. [Phi19, Th. D.14]).  

## 5 Vector Spaces  

### 5.1 Vector Spaces and Subspaces  

Definition 5.1. Let. $F^{\prime}$ be a field and let. $V$ be a nonempty set with two maps  

$$
\begin{array}{r l}{+\colon V\times V\longrightarrow V,}&{(x,y)\mapsto x+y,}\ {\quad\cdot\colon F\times V\longrightarrow V,}&{(\lambda,x)\mapsto\lambda\cdot x}\end{array}
$$  

$^+$ is called (vector) addition and . is called scalar multiplication; as with other multiplications before, often one writes $\lambda x$ instead of. $\lambda\cdot x$ take care not to confuse the vector addition on $V$ with the addition on $F$ and, likewise, not to confuse the scalar. multiplication with the multiplication on. $F^{\prime}$ , the symbol. $^+$ is used for both additions and : is used for both multiplications, but you can always determine from the context which addition or multiplication is meant). Then. $V$ is called a vector space or a linear space over $F$ (sometimes also an $F$ -vector space) if, and only if, the following conditions. are satisfied:  

(i) $(V,+)$ is a commutative group. The neutral element with respect to $^+$ is denoted $0$ (do not confuse $0\in V$ with $0\in F$ once again, the same symbol is used for different objects (both objects only coincide for $F=V$ )).  

(ii) Distributivity:  

$$
\begin{array}{r l r}{\bigforall}&{{}\bigforall_{\lambda\in F}}&{\lambda(x+y)=\lambda x+\lambda y,}\ {\lambda\in F}&{{}x,y\in V}&{}\ {\bigforall}&{{}\bigforall_{\lambda\in F}}&{(\lambda+\mu)x=\lambda x+\mu x.}\end{array}
$$  

(iii) Compatibility between Multiplication on $F^{\prime}$ and Scalar Multiplication:.  

$$
\forall_{\lambda,\mu\in F}\quad\forall_{x\in V}\quad(\lambda\mu)x=\lambda(\mu x).
$$  

(iv) The neutral element with respect to the multiplication on $F^{\prime}$ is also neutral with. respect to the scalar multiplication:.  

$$
\forall_{x\in V}\quad1x=x.
$$  

If $V$ is a vector space over $F$ , then one calls the elements of $V$ vectors and the elements of $F^{\prime}$ scalars.  

Example 5.2. (a) Every field. $F^{\prime}$ is a vector space over itself if one uses the field addition in. $F$ as the vector addition and the field multiplication in $F$ as the scalar. multiplication (as important special cases, we obtain that $\mathbb{R}$ is a vector space over. $\mathbb{R}$ and $\mathbb{C}$ is a vector space over. $\mathbb{C}$ ): All the vector space laws are immediate consequences of the corresponding field laws: Def. 5.1(i) holds as every field is a commutative group with respect to addition; Def. 5.1(ii) follows from field distributivity and multiplicative commutativity on. $F$ ; Def. 5.1(iii) is merely the multiplicative associativity on $F^{\prime}$ ; and Def. 5.1(iv) holds, since scalar multiplication coincides with field multiplication on $F$  

(b) The reasoning in (a) actually shows that every field $F$ is a vector space over every subfield $E\subseteq F$ . In particular, $\mathbb{R}$ is a vector space over. $\mathbb{Q}$  

(c) In a further generalization of (b), let $V$ be a vector space over the field $F$ and let $E\subseteq F$ be a subfield of $F^{\prime}$ . Then $V$ is also a vector space over $E$ : If the laws of Def. 5.1 hold for all elements of $F^{\prime}$ , then, in particular, they also hold for all elements of $E$  

(d) If $A$ is any nonempty set,. $F^{\prime}$ is a field, and $Y$ is a vector space over the field $F^{\prime}$ then we can make. $V:=\mathcal{F}(A,Y)=Y^{A}$ (the set of functions from. $A$ into $Y$ ) into a vector space over $F^{\prime}$ by defining for each. $f,g:A\longrightarrow Y$  

$$
\begin{array}{r l}&{(f+g):A\longrightarrow Y,\qquad(f+g)(x):=f(x)+g(x),}\ &{(\lambda\cdot f):A\longrightarrow Y,\qquad(\lambda\cdot f)(x):=\lambda\cdot f(x)\quad\mathrm{for~each~}\lambda\in F:}\end{array}
$$  

To verify that. $(V,+,\cdot)$ is, indeed, a vector space, we begin by checking Def. 5.1(i), i.e. by showing. $(V,+)$ is a commutative group: Since (5.5a) is precisely the pointwise definition of Ex. 4.9(e), we already know. $(V,+)$ to be a commutative group due to. (4.11d).  

To verify Def. 5.1(ii), one computes  

$$
\begin{array}{r l}{\underset{\lambda\in F}{\forall}}&{\underset{f,g\in V}{\forall}\quad\underset{x\in A}{\forall}}&{\big(\lambda(f+g)\big)(x)=\lambda\big(f(x)+g(x)\big)\overset{(*)}{=}\lambda f(x)+\lambda g(x)}\ &{=\big(\lambda f+\lambda g\big)(x),}\end{array}
$$  

where distributivity in the vector space $Y$ was used at $(*)$ , proving $\lambda(f+g)=\lambda f+\lambda g$ and, thus, (5.2a). Similarly,.  

$$
\begin{array}{r l}{\forall~}&{{}\forall~\forall~\forall~{\bigl(}(\lambda+\mu)f{\bigr)}(x)=(\lambda+\mu)f(x)\stackrel{(*)}{=}\lambda f(x)+\mu f(x)}\ {\lambda,\mu\in F}&{{}f\in V\quad x\in A}\end{array}
$$  

where, once more, distributivity in the vector space $Y$ was used at $(*)$ , proving $(\lambda+\mu)f=\lambda f+\mu f$ and, thus, (5.2b).  

The proof of Def. 5.1(iii), is given by  

$$
\begin{array}{r}{\underset{\lambda,\mu\in F}{\forall}\quad\underset{f\in V}{\forall}\quad\underset{x\in A}{\forall}\quad\left((\lambda\mu)f\right)(x)=(\lambda\mu)f(x)\stackrel{(*)}{=}\lambda(\mu f(x))=\big(\lambda(\mu f)\big)(x),}\end{array}
$$  

where the validity of Def. 5.1(iii) in the vector space $Y$ was used at $(*)$  

Finally, to prove Def. 5.1(iv), one computes  

$$
\forall_{f\in V}\quad\forall_{x\in A}\quad(1\cdot f)(x)=1\cdot f(x){\overset{(*)}{=}}f(x),
$$  

where the validity of Def. 5.1(iv) in the vector space $Y$ was used at $(*)$  

(e) Let $F^{\prime}$ be a field (e.g. $F=\mathbb{R}$ or $F=\mathbb{C}$ ) and $n\in\mathbb{N}$ . For $x=(x_{1},\ldots,x_{n})\in F^{n}$ $y=(y_{1},\ldots,y_{n})\in F^{n}$ , and $\lambda\in F$ , define componentwise addition  

$$
x+y:=(x_{1}+y_{1},\ldots,x_{n}+y_{n}),
$$  

and componentwise scalar multiplication  

$$
\lambda x:=(\lambda x_{1},...,\lambda x_{n}).
$$  

Then $(F^{n},+,\cdot)$ constitutes a vector space over $F^{\prime}$ . The validity of Def.. $5.1(\mathrm{i})\textrm{--}\mathrm{Def}$ 5.1(iv) can easily be verified directly, but. $(F^{n},+,\cdot)$ can also be seen as a special. case of (d) with. $A=\{1,\ldots,n\}$ and $Y=F$ : Recall that, according to Ex. 2.16(c), $F^{n}=F^{\{1,\ldots,n\}}={\mathcal{F}}{\big(}\{1,\ldots,n\},F{\big)}$ is the set of functions from. $\{1,\ldots,n\}$ into $F$ Then $x=(x_{1},\ldots,x_{n})\in F^{n}$ is the same as the function $f:\{1,\dots,n\}\longrightarrow F$ $f(j)=x_{j}$ . Thus, (5.6a) is, indeed, the same as (5.5a), and (5.6b) is, indeed, the same as (5.5b).  

Proposition 5.3. The following rules hold in each vector space $V$ over the field $F^{\prime}$ (here, even though we will usually use the same symbol for both objects, we write O for the additive neutral element in $F$ and $\vec{0}$ for the additive neutral element in $V$  

(a) $\lambda\cdot\vec{0}=\vec{0}$ for each $\lambda\in F$  

(b) $0\cdot v={\vec{0}}$ for each $v\in V$ (c) $\lambda\cdot(-v)=(-\lambda)\cdot v=-(\lambda\cdot v)$ for each $\lambda\in F$ and each $v\in V$ (d) If $\lambda\cdot v={\vec{0}}$ with $\lambda\in F$ and $v\in V$ , then $\lambda=0$ or $v={\vec{0}}$  

Proof. Exercise.  

Definition 5.4. Let. $(V,+,\cdot)$ be a vector space over the field $F^{\prime}$ $\varnothing\neq U\subseteq V$ . We call $U$ a subspace of $V$ if, and only if,. $(U,+,\cdot)$ forms a vector space over $F$ with respect to the. operations $^+$ and - it inherits from. $V$ , i.e. with respect to. $+\lceil\upsilon\times\upsilon$ and $\cdot\left\lceil\boldsymbol{\mathbf{\mathit{F}}}\times\boldsymbol{U}\right\rceil$  

Theorem 5.5. Let $(V,+,\cdot)$ be a vector space over the field. $F^{\prime}$ $\emptyset\neq U\subseteq V$ . Then the following statements are equivalent:  

(i) $U$ is a subspace of $V$ (ii) One has  

$$
\begin{array}{r l r}&{}&{\forall~x+y\in U,}\ &{}&{x,y\in U}\ &{\land\quad\forall~\bigtriangledown_{x\in U}\quad\lambda x\in U.}\end{array}
$$  

(iii) One has  

$$
\forall_{\lambda,\mu\in F}\quad\forall_{x,y\in U}\quad\lambda x+\mu y\in U.
$$  

Proof. From the definition of a vector space, it is immediate that (i) implies (ii) and (iii).  

"(ii)=(ii)": One obtains (5.7a) from (5.8) by setting $\lambda:=\mu:=1$ , and one obtains.   
(5.7b) from (5.8) by setting $y:=0$ (and $\mu$ arbitrary, e.g.,. $\mu:=1$  

"(ii)=>(i)": Clearly, $U$ inherits commutativity and distributivity as well as the validity of (5.3) and (5.4) from $V$ . Moreover, if $x\in U$ , then, setting $\lambda:=-1$ in (5.7b), shows $-x\in U$ . This, together with (5.7a), proves $(U,+)$ to be a subgroup of $(V,+)$ , thereby completing the proof of (i).  

Example 5.6. (a) As a consequence of Th. 5.5, if $V$ is a vector space over the field $F^{\prime}$ then $\{0\}\subseteq V$ is always a subspace of. $V$ (sometimes called the trivial or the zero vector space over. $F$  

(b) $\mathbb{Q}$ is not a subspace of. $\mathbb{R}$ if $\mathbb{R}$ is considered as a vector space over $\mathbb{R}$ (for example, ${\sqrt{2}}\cdot2\not\in\mathbb{Q},$ . However, $\mathbb{Q}$ is a subspace of $\mathbb{R}$ if $\mathbb{R}$ is considered as a vector space. over $\mathbb{Q}$  

(c) Consider the vector space $V:=\mathbb{R}^{3}$ over $\mathbb{R}$ and let  

$$
U:=\{(x,y,z)\in V:3x-y+7z=0\}.
$$  

We use Th. 5.5 to show. $U$ is a subspace of. $V$ : Since $(0,0,0)\in U$ , we have $U\neq\emptyset$ Moreover, if $u_{1}=(x_{1},y_{1},z_{1})\in U$ $u_{2}=(x_{2},y_{2},z_{2})\in U$ , and $\lambda,\mu\in\mathbb{R}$ , then  

$$
\lambda u_{1}+\mu u_{2}=(\lambda x_{1}+\mu x_{2},\lambda y_{1}+\mu y_{2},\lambda z_{1}+\mu z_{2})
$$  

and  

$$
\begin{array}{r l}&{3(\lambda x_{1}+\mu x_{2})-(\lambda y_{1}+\mu y_{2})+7(\lambda z_{1}+\mu z_{2})}\ &{\quad=\lambda(3x_{1}-y_{1}+7z_{1})+\mu(3x_{2}-y_{2}+7z_{2})\overset{u_{1},u_{2}\in U}{=}\lambda\cdot0+\mu\cdot0=0,}\end{array}
$$  

showing $\lambda u_{1}+\mu u_{2}$ and proving $U$ to be a subspace of $V$ (d) It is customary to write $\mathbb{K}$ if $\mathbb{K}$ may stand for $\mathbb{R}$ or $\mathbb{C}$ , and, from now on, we will occasionally use this notation. From Ex. 5.2(d), we know that, for each $\emptyset\neq A$ ${\mathcal{F}}(A,\mathbb{K})$ constitutes a vector space over $\mathbb{K}$ .Thus, as a consequence of Th. 5.5, a subset of $\mathcal{F}(A,\mathbb{K})$ is a vector space over $\mathbb{K}$ if, and only if, it is closed under addition and scalar multiplication. By using results from Calculus, we obtain the following. examples:  

(i) The set ${\mathcal{P}}(\mathbb{K})$ of all polynomial functions mapping from $\mathbb{K}$ into $\mathbb{K}$ is a vector space over $\mathbb{K}$ by [Phi16, Rem. 6.4]; for each $n\in\ensuremath{\mathbb{N}}_{0}$ , the set ${\mathcal{P}}_{n}(\mathbb{K})$ of all such polynomial functions of degree at most $n$ is also a vector space over $\mathbb{K}$ by [Phi16, Rem. (6.4a),(6.4b)].  

(ii) If ${\emptyset}\neq{M}\subseteq\mathbb{C}$ , then the set of continuous functions from $M$ into $\mathbb{K}$ , i.e. $C(M,\mathbb{K})$ , is a vector space over. $\mathbb{K}$ by [Phi16, Th. 7.38].  

(iii) If $a,b\in\mathbb{R}\cup\{-\infty,\infty\}$ and $a<b$ , then the set of differentiable functions from. $I:=\mathrm{j}a,b[$ into $\mathbb{K}$ is a vector space over $\mathbb{K}$ by [Phi16, Th. 9.7(a),(b)]. Moreover, [Phi16, Th. 9.7(a),(b)] also implies that, for each. $k\in\mathbb N$ , the set of $k$ times differentiable functions from. $I$ into $\mathbb{K}$ is a vector space over. $\mathbb{K}$ , and so is each set $C^{k}(I,\mathbb{K})$ of $k$ times continuously differentiable functions ([Phi16, Th. 7.38] is also needed for the last conclusion). The set $\begin{array}{r}{C^{\infty}(I,\mathbb{K}):=\bigcap_{k\in\mathbb{N}}C^{k}(I,\mathbb{K})}\end{array}$ is also a vector space over. $\mathbb{K}$ by Th. 5.7(a) below..  

Theorem 5.7. Let. $V$ be a vector space over the field $F^{\prime}$ (a) Let $I\neq\emptyset$ be an index set and $(U_{i})_{i\in I}$ a family of subspaces of $V$ . Then the intersection $\begin{array}{r}{U:=\bigcap_{i\in I}U_{i}}\end{array}$ is also a subspace of $V$  

(b) In contrast to intersections, unions of subspaces are almost never subspaces (how ever, cf. (c) below). More precisely, if $U_{1}$ and $U_{2}$ are subspaces of $V$ , then  

$$
U_{1}\cup U_{2}i s s u b s p a c e o f V\quad\Leftrightarrow\quad\Big(U_{1}\subseteq U_{2}\lor U_{2}\subseteq U_{1}\Big).
$$  

(c) While (b) shows that unions of subspaces are not necessarily subspaces, if $I\neq\emptyset$ is an index set, partially ordered. $b y\leq$ in a way such that, for each. $i,j\in I$ , there exists $k\in{I}$ with $i,j\leq k$ (if $I$ is totally ordered by. $\leq$ , then one can use $k:=\operatorname*{max}\{i,j\})$ and $(U_{i})_{i\in I}$ is an increasing family of subspaces (i.e., for each. $i,j\in I$ with $i\leq j$ one has $U_{i}\subseteq U_{j}$ ), then $U:=\cup_{i\in I}U_{i}$ is a subspace as well.  

Proof. (a): Since $0\in U$ , we have. $U\neq\emptyset$ . If $x,y\in U$ and $\lambda,\mu\in F$ , then $\lambda x+\mu y\in U_{i}$ for each $i\in I$ , implying $\lambda x+\mu y\in U$ . Thus, $U$ is a subspace of $V$ by Th. 5.5..  

(b): Exercise.  

(c): Since $0\in U_{i}\subseteq U$ , we have $U\neq\emptyset$ . If $x,y\in U$ and $\lambda,\mu\in F$ , then there exist $i,j\in I$ such that $x\in U_{i}$ and $y\in U_{j}$ . If $k\in{I}$ with $i,j\leq k$ , then $\lambda x+\mu y\in U_{k}\subseteq U$ . Thus, $U$ is a subspace of $V$ by Th. 5.5.  

While the union of two subspaces. $U_{1},U_{2}$ is typically not a subspace, Th. 5.7(a) implies there is always a smallest subspace containing $U_{1}\cup U_{2}$ and we will see below that this. subspace is always the so-called sum. $U_{1}+U_{2}$ of the two subspaces (this is a special case of Prop. 5.11). As it turns out, the sum of vector spaces is closely connected with two other essential notions of vector space theory, namely the notions linear combination and span, which we define first:.  

Definition 5.8. Let $V$ be a vector space over the field $F^{\prime}$ (a) Let $n\in\mathbb{N}$ and $v_{1},\ldots,v_{n}\in V$ . A vector $v\in V$ is called a linear combination of $v_{1},\ldots,v_{n}$ if, and only if, there exist $\lambda_{1},\dots,\lambda_{n}\in F$ (often called coefficients in this context) such that  

$$
v=\sum_{i=1}^{n}\lambda_{i}v_{i}.
$$  

(b) Let $A\subseteq V$ , and  

$$
\mathcal{U}:=\big\{U\in\mathcal{P}(V):A\subseteq U\wedge U\mathrm{~is~subspace~of~}V\big\}.
$$  

Then the set  

$$
\langle A\rangle:=\operatorname{span}A:=\bigcap_{U\in\mathcal{U}}U
$$  

is called the span of $A$ . Moreover $A$ is called a spanning set or a generating set of $V$ if, and only if, $\langle A\rangle=V$  

Proposition 5.9. Let $V$ be a vector space over the field $F$ and $A\subseteq V$  

(a) $\langle A\rangle$ is a subspace of. $V$ , namely the smallest subspace of $V$ containing $A$  

(b) If $A=\emptyset$ , then $\langle A\rangle=\{0\}$ ; if $A\neq\emptyset$ , then $\langle A\rangle$ is the set of all linear combinations of elements from $A$ , i.e.  

$$
\langle A\rangle=\left\{\sum_{i=1}^{n}\lambda_{i}a_{i}:n\in\mathbb{N}\wedge\lambda_{1},\ldots,\lambda_{n}\in F\wedge a_{1},\ldots,a_{n}\in A\right\}.
$$  

(c) If $A\subseteq B\subseteq V$ , then $\langle A\rangle\subseteq\langle B\rangle$ (d) $A=\langle A\rangle$ if, and only if, $A$ is a subspace of $V$  

Proof. (a) is immediate from Th. 5.7(a).  

(b): For the case $A=\emptyset$ , note that $\{0\}$ is a subspace of $V$ , and that $\{0\}$ is contained in every subspace of. $V$ . For $A\neq\emptyset$ , let $W$ denote the right-hand side of (5.13), and recall from (5.12) that $\langle A\rangle$ is the intersection of all subspaces $U$ of $V$ that contain $A$ . If $U$ is a subspace of $V$ and $A\subseteq U$ , then $W\subseteq U$ , since $U$ is closed under vector addition and scalar multiplication, showing $W\subseteq\langle A\rangle$ . On the other hand,. $W$ is clearly a subspace of. $V$ that contains $A$ , showing $\langle A\rangle\subseteq W$ , completing the proof of. $\langle A\rangle=W$  

(c) is immediate from (b).  

(d): If $A=\langle A\rangle$ , then $A$ is a subspace by (a). For the converse, while it is clear that $A\subseteq\langle A\rangle$ always holds, if $A$ is a subspace, then $A\in{\mathcal{U}}$ , where $\mathcal{U}$ is as in (5.11), implying $\langle A\rangle\subseteq A$  

(e) now follows by combining (d) with (a).  

Definition 5.10. Let $V$ be a vector space over the field $F^{\prime}$ , let $I$ be an index set and let $(U_{i})_{i\in I}$ be a family of subspaces of. $V$ . For $I=\emptyset$ , define  

$$
\sum_{i\in I}U_{i}:=\{0\}.
$$  

If $\#I=n\in\mathbb{N}$ , then let. $\phi:\{1,\dots,n\}\longrightarrow I$ be a bijection and define  

$$
\sum_{i\in I}U_{i}:=\sum_{k=1}^{n}U_{\phi(k)}:=\left\{\sum_{k=1}^{n}u_{k}:\underset{k\in\{1,\ldots,n\}}{\forall}u_{k}\in U_{\phi(k)}\right\},
$$  

where the commutativity of addition guarantees the definition is independent of the chosen bijection (note that this definition is consistent with the definition in Ex. 4.9(d)). For a general, not necessarily finite. $I$ , let $\mathcal{I}:=\{J\subseteq I:J$ is finite} and define  

$$
\sum_{i\in I}U_{i}:=\bigcup_{J\in\mathcal{J}}\sum_{j\in J}U_{j}.
$$  

In each case, we call. $\textstyle\sum_{i\in I}U_{i}$ the sum of the subspaces $U_{i}$ $i\in I$  

Proposition 5.11. Let $V$ be a vector space over the field $F^{\prime}$ , let $I$ be an index set and let $(U_{i})_{i\in I}$ be a family of subspaces of $V$ . Then  

$$
\sum_{i\in I}U_{i}=\left\langle\bigcup_{i\in I}U_{i}\right\rangle
$$  

(in particular, $\textstyle\sum_{i\in I}U_{i}$ is always a subspace of $V$  

Proof. Let $\begin{array}{r}{A:=\sum_{i\in I}U_{i}}\end{array}$ $B:=\langle\cup_{i\in I}U_{i}\rangle$ . If $I=\emptyset$ , then both sides of (5.15) are $\{0\}$ i.e. the statement holds in this case. Now assume $I\neq\emptyset$ .If $v\in A$ , then there are. $i_{1},\ldots,i_{n}\in I$ $n\in\mathbb{N}$ , such that $\begin{array}{r}{v=\sum_{k=1}^{n}u_{i_{k}}}\end{array}$ $u_{i_{k}}\in U_{i_{k}}$ , showing $v\in B$ , since $B$ is a subspace of $V$ . Thus, $A\subseteq B$ . To prove $B\subseteq A$ , it suffices to show $A$ is a subspace of $V$ that contains each $\boldsymbol{U}_{i}$ $i\in I$ . If $i\in I$ and $v\in U_{i}$ , then $v\in A$ is clear from (5.14c) (set $J:=\{i\}$ ). Let $v,w\in A$ , where $\upsilon$ is as above and there exist $j_{1},\ldots,j_{m}\in I$ $m\in\mathbb{N}$ , such that $\begin{array}{r}{w=\sum_{k=1}^{m}w_{j_{k}}}\end{array}$ $w_{j_{k}}\in U_{j_{k}}$ . Then $\textstyle v+w=\sum_{k=1}^{n}u_{i_{k}}+\sum_{k=1}^{m}u_{j_{k}}\in A$ and, for each $\lambda\in F$ $\textstyle\lambda v=\sum_{k=1}^{n}(\lambda u_{i_{k}})\in A$ , proving $A$ to be a subspace of $V$ . Thus, $B\subseteq A$ , thereby concluding the proof.  

### 5.2 Linear Independence, Basis, Dimension  

The notions introduced in the present section are of central importance to the theory of vector spaces. In particular, we will see that the structure of many interesting vector  

spaces (e.g. $\mathbb{K}^{n}$ ) is particularly simple, as every vector can be written as a so-called linear combination of a fixed finite set of linearly dependent vectors (we will see this is the case if, and only if, the vector space is finite-dimensional, cf. Th. 5.23 below).  

Definition 5.12. Let. $V$ be a vector space over the field $F^{\prime}$  

(a) A vector. $v\in V$ is called linearly dependent on a subset $U$ of $V$ (or on the vectors in $U$ ) if, and only if,. $v=0$ or there exists. $n\in\mathbb N$ and $u_{1},\ldots,u_{n}\in U$ such that $v$ is a linear combination of $u_{1},\ldots,u_{n}$ . Otherwise, $\upsilon$ is called linearly independent of. $U$  

(b) A subset $U$ of $V$ is called linearly independent if, and only if, whenever. $0\in V$ is written as a linear combination of distinct elements of $U$ , then all coefficients must be $0\in F$ , i.e. if, and only if,  

$$
\begin{array}{r l c c c l l}{{}}&{{\displaystyle\left(n\in{\mathbb{N}}\quad\wedge\quad W\subseteq U\quad\wedge\quad\#W=n\quad\wedge\quad\displaystyle\sum_{u\in W}\lambda_{u}u=0}}&{{\wedge}}&{{\displaystyle\forall\quad\lambda_{u}\in F}}\ {{}}&{{}}&{{}}&{{}}&{{}}&{{}}\ {{\Rightarrow}}&{{\displaystyle\forall\quad\lambda_{u}=0.}}&{{}}&{{}}&{{(5.1\hdots}}\end{array}\right)_{u\in W},}}\end{array}
$$  

Occasionally, one also wants to have the notion available for families of vectors instead of sets, and one calls a family $(u_{i})_{i\in I}$ of vectors in $V$ linearly independent if, and only if,  

$$
\begin{array}{r l r l r l r}&{\displaystyle\left(n\in{\mathbb{N}}\quad\land\quad J\subseteq I\quad\land\quad\#J=n}&{\land}&{\sum_{j\in J}\lambda_{j}u_{j}=0}&{\land}&{\underbrace{\forall}_{j\in J}\lambda_{j}\in F\right)}&\ &{\Rightarrow\quad\underset{j\in J}{\forall}}&{\lambda_{j}=0.}&{(5.1}&\end{array}
$$  

Sets and families that are not linearly independent are called linearly dependent.  

Example 5.13. Let $V$ be a vector space over the field $F$ (a) $\varnothing$ is linearly independent: Indeed, if $U=\emptyset$ , then the left side of the implication in (5.16a) is always false (since $W\subseteq U$ means $\#W=0$ ), i.e. the implication is true. Moreover, by Def. 5.12(a), $v\in V$ is linearly dependent on $\varnothing$ if, and only if, $v=0$ (this is also consistent with $\textstyle\sum_{u\in\emptyset}\lambda_{u}u=0$ (cf. (3.15d)).  

(b) If $0\in U\subseteq V$ , then $U$ is linearly dependent (in particular, $\{0\}$ is linearly dependent), due to $1\cdot0=0$  

(c) If $0\not=v\in V$ and $\lambda\in F$ with $\lambda v=0$ , then $\lambda=0$ by Prop. 5.3(d), showing. $\{v\}$ to be linearly independent. However, the family $(v,v)$ is always linearly dependent, since $1v+(-1)v=0$ (also for $v=0$ ). Moreover, $1v=v$ also shows that every. $v\in V$ is linearly dependent on itself..  

(d) The following example is of some general importance: Let $I$ be a set and $V=F^{I}$ (cf. Ex. 5.2(d),(e)). Define  

$$
\begin{array}{r}{\underset{i\in I}{\forall}\quad e_{i}:I\longrightarrow F,\quad e_{i}(j):=\delta_{i j}:=\left\{\begin{array}{l l}{1}&{\mathrm{if~}i=j,}\ {0}&{\mathrm{if~}i\neq j.}\end{array}\right.}\end{array}
$$  

Then $\delta$ is known as the Kronecker delta (which can be seen as a function $\delta:$ $I\times I\longrightarrow\{0,1\}.$ ). If $n\in\mathbb N$ and $V=F^{n}$ , i.e. $I=\{1,\dots,n\}$ , then one often writes the $e_{i}$ in the form $e_{1}=(1,0,\ldots,0)$ $e_{2}=(0,1,0,\dots,0)$ ,..., $e_{n-1}=(0,\ldots,0,1,0)$ $e_{n}=(0,\ldots,0,1)$ ; for example in $\mathbb{R}^{3}$ (or, more generally, in $F^{3}$ ), $e_{1}~=~(1,0,0)$ $e_{2}=(0,1,0)$ $e_{3}=(0,0,1)$ . Returning to the case of a general $I$ , we check that the set  

$$
B:=\{e_{i}:i\in I\}
$$  

is linearly independent: Assume  

$$
\sum_{j\in J}\lambda_{j}e_{j}=0\in V,
$$  

where $J\subseteq I$ $\#J=n\in\mathbb{N}$ , and $\lambda_{j}\in F$ for each $j\in J$ . Recalling that. $0\in V$ is the function that is constantly equal to $0\in F^{\prime}$ , we obtain  

$$
\forall_{k\in J}0=\left(\sum_{j\in J}\lambda_{j}e_{j}\right)(k)=\sum_{j\in J}\lambda_{j}e_{j}(k)=\sum_{j\in J}\lambda_{j}\delta_{j k}=\lambda_{k},
$$  

thereby proving the linear independence of $B$  

(e) For a Calculus application, we let  

$$
\begin{array}{r l}{\forall}&{{}f_{k}:\mathbb{R}\longrightarrow\mathbb{K},\quad f_{k}(x):=e^{k x},}\end{array}
$$  

and show that  

$$
U:=\{f_{k}:k\in\mathbb{N}_{0}\}
$$  

is linearly independent as a subset of the vector space $V:=C(\mathbb{R},\mathbb{K})$ over $\mathbb{K}$ of differentiable functions from $\mathbb{R}$ into $\mathbb{K}$ (cf. Ex. 5.6(d)(iii)), by showing each set $U_{n}:=\{f_{k}:k\in\{0,\ldots,n\}\}$ $n\in\ensuremath{\mathbb{N}}_{0}$ , is linearly independent, using an induction on $n$ : Since, for $n=0$ $f_{n}\equiv1$ , the base case holds. Now let $n\geq1$ and assume $\lambda_{0},\dots,\lambda_{n}\in\mathbb{K}$ are such that  

$$
\underset{x\in\mathbb{R}}{\bigforall}\quad\sum_{k=0}^{n}\lambda_{k}e^{k x}=0.
$$  

Multiplying (5.19) by $n$ yields  

$$
\forall_{x\in\mathbb{R}}n\sum_{k=0}^{n}\lambda_{k}e^{k x}=0,
$$  

whereas differentiating (5.19) with respect to $x$ yields  

$$
\forall\sum_{x\in\mathbb{R}}^{n}k\lambda_{k}e^{k x}=0.
$$  

By subtracting (5.21) from (5.20), we then obtain  

$$
\forall_{x\in\mathbb{R}}\quad\sum_{k=0}^{n-1}(n-k)\lambda_{k}e^{k x}=0,
$$  

implying $\lambda_{0}=\cdot\cdot\cdot=\lambda_{n-1}=0$ due to the induction hypothesis. Using this in (5.19), then yields.  

$$
\underset{x\in\mathbb{R}}{\forall}\quad\lambda_{n}e^{n x}=0
$$  

and, thus,. $\lambda_{n}=0$ as well, completing the induction proof.  

Proposition 5.14. Let. $V$ be a vector space over the field $F^{\prime}$ and $U\subseteq V$  

(a) $U$ is linearly dependent if, and only if, there exists $u_{0}\in U$ such that $u_{0}$ is linearly. dependent on. $U\setminus\{u_{0}\}$   
(b) If $U$ is linearly dependent and $U\subseteq M\subseteq V$ , then $M$ is linearly dependent as well.   
(c) If $U$ is linearly independent and $M\subseteq U$ , then $M$ is linearly independent as well.   
(d) Let $U$ be linearly independent. If $U_{1},U_{2}\subseteq U$ and $V_{1}:=\langle U_{1}\rangle$ $V_{2}:=\langle U_{2}\rangle$ , then $V_{1}\cap V_{2}=\langle U_{1}\cap U_{2}\rangle$  

Proof. (a): Suppose,. $U$ is linearly dependent. Then there exists $W\subseteq U$ $\#W=n\in\mathbb{N}$ such that $\textstyle\sum_{u\in W}\lambda_{u}u=0$ with $\lambda_{u}\in F$ and there exists $u_{0}\in W$ with $\lambda_{u_{0}}\neq0$ . Then  

$$
u_{0}=-\lambda_{u_{0}}^{-1}\sum_{u\in W\backslash\{u_{0}\}}\lambda_{u}u=\sum_{u\in W\backslash\{u_{0}\}}(-\lambda_{u_{0}}^{-1}\lambda_{u})u,
$$  

showing $u_{0}$ to be linearly dependent on $U\setminus\{u_{0}\}$ .Conversely, if $u_{0}\in U$ is linearly. dependent on. $U\backslash\{u_{0}\}$ , then. $u_{0}=0$ , in which case. $U$ is linearly dependent according to  

Ex. 5.13(b), or $u_{0}\neq0$ , in which case, there exists $n\in\mathbb N$ , distinct $u_{1},\ldots,u_{n}\in U\backslash\{u_{0}\}$ and $\lambda_{1},\dots,\lambda_{n}\in F$ such that.  

$$
u_{0}=\sum_{i=1}^{n}\lambda_{i}u_{i}\quad\Rightarrow\quad-u_{0}+\sum_{i=1}^{n}\lambda_{i}u_{i}=0,
$$  

showing $U$ to be linearly dependent, since the coefficient of $u_{0}$ is $-1\neq0$ (b) and (c) are now both immediate from (a).  

(d): Since $V_{1}\cap V_{2}$ is a vector space with $U_{1}\cap U_{2}\subseteq V_{1}\cap V_{2}$ , we already have. $\langle U_{1}\cap U_{2}\rangle\subseteq$ $V_{1}\cap V_{2}$ . Now let $u\in V_{1}\cap V_{2}$ . Then there exist distinct $z_{1},\dots,z_{k}\in U_{1}\cap U_{2}$ and distinct $x_{k+1},\ldots,x_{k+n}\in U_{1}\backslash U_{2}$ and distinct $y_{k+1},\ldots,y_{k+m}\in U_{2}\backslash U_{1}$ with $k\in\ensuremath{\mathbb{N}}_{0}$ $m,n\in\mathbb{N}$ as well as $\lambda_{1},\dots,\lambda_{k+n},\mu_{1},\dots,\mu_{k+m}\in F$ such that  

$$
u=\sum_{i=1}^{k}\lambda_{i}z_{i}+\sum_{i=k+1}^{k+n}\lambda_{i}x_{i}=\sum_{i=1}^{k}\mu_{i}z_{i}+\sum_{i=k+1}^{k+m}\mu_{i}y_{i},
$$  

implying  

$$
0=\sum_{i=1}^{k}(\lambda_{i}-\mu_{i})z_{i}+\sum_{i=k+1}^{k+n}\lambda_{i}x_{i}-\sum_{i=k+1}^{k+m}\mu_{i}y_{i}.
$$  

The linear independence of $U$ then yields $\lambda_{1}=\mu_{1},\ldots,\lambda_{k}=\mu_{k}$ as well as $\lambda_{k+1}=$ $\cdot\cdot=\lambda_{k+n}=\mu_{k+1}=\cdot\cdot\cdot=\mu_{k+m}=0$ . Thus, in particular, $u\in\langle U_{1}\cap U_{2}\rangle$ , proving $V_{1}\cap V_{2}\subseteq\langle U_{1}\cap U_{2}\rangle$ as desired.  

Definition 5.15. Let. $V$ be a vector space over the field $F$ and $B\subseteq V$ . Then $B$ is called a basis of. $V$ if, and only if, $B$ is a generating set for. $V$ (i.e. $V=\langle B\rangle$ ) that is also linearly independent..  

Example 5.16. (a) Due to Ex. 5.13(a), in each vector space $V$ over a field $F$ , we have that $\varnothing$ is linearly independent with $\langle\emptyset\rangle=\{0\}$ , i.e. $\varnothing$ is a basis of the trivial space $\{0\}$  

(b) If one considers a field. $F^{\prime}$ as a vector space over itself, then, clearly, every. $\{\lambda\}$ with $0\not=\lambda\in F$ is a basis.  

(c) We continue Ex. 5.13(d), where we showed that, given a field $F^{\prime}$ and a set $I$ $B=$ $\{e_{i}:i\in I\}$ with the $e_{i}$ defined by (5.17) constitutes a linearly independent subset. of the vector space $F^{I}$ over $F$ . We will now show that. $\left<B\right>=F_{\mathrm{fin}}^{I}$ (i.e. $B$ is a basis of $F_{\mathrm{fin}}^{I}$ ), where $F_{\mathrm{fin}}^{I}$ denotes the set of functions $f:I\longrightarrow F$ such that there exists a finite set $I_{f}\subseteq I$ , satisfying  

$$
\begin{array}{r l}{f(i)=0}&{\mathrm{for~each}i\in I\setminus I_{f},}\ {f(i)\neq0}&{\mathrm{for~each}i\in I_{f}}\end{array}
$$  

(then $F_{\mathrm{fin}}^{I}=F^{I}$ if, and only if, $I$ is finite (for example $F_{\mathrm{fin}}^{n}=F^{n}$ for $n\in\mathbb N$ ); but, in general, $F_{\mathrm{fin}}^{I}$ is a strict subset of $F^{I}$ ). We first show that $F_{\mathrm{fin}}^{I}$ is always a subspace of $F^{I}$ : Indeed, if $f,g\in F_{\mathrm{fin}}^{I}$ and $\lambda\in F$ , then $I_{\lambda f}=I_{f}$ for $\lambda\neq0$ $I_{\lambda f}=\emptyset$ for $\lambda=0$ and $I_{f+g}\subseteq I_{f}\cup I_{g}$ , i.e. $\lambda f\in F_{\mathrm{fin}}^{I}$ and $f+g\in F_{\mathrm{fin}}^{I}$ ' We also note $B\subseteq F_{\mathrm{fin}}^{I}$ , since $I_{e_{i}}=\{i\}$ for each $i\in I$ . To see $\left<B\right>=F_{\mathrm{fin}}^{I}$ , we merely note that  

$$
\boxed{\zeta}_{f\in F_{\mathrm{fn}}^{I}}\quad f=\sum_{i\in I_{f}}f(i)e_{i}.
$$  

Thus, $B$ is a basis of $F_{\mathrm{fin}}^{I}$ as claimed $-\textit{B}$ is often referred to as the standard basis of $F_{\mathrm{fin}}^{I}$ . In particular, we have shown that, for each $n\in\mathbb N$ , the set $\{e_{j}:j=1,\dots,n\}$ where $e_{1}=(1,0,\ldots,0)$ $e_{2}=(0,1,0,\dots,0)$ $\cdot\cdot\cdot$ $e_{n}=(0,\ldots,0,1)$ , forms a basis of $F^{n}$ (of $\mathbb{R}^{n}$ if $F=\mathbb{R}$ and of $\mathbb{C}^{n}$ if $F=\mathbb{C}$ ). If $I=\mathbb{N}$ , then $F_{\mathrm{fin}}^{I}$ is the space of all sequences in $F$ that have only finitely many nonzero entries. We will see later that, actually, every vector space is isomorphic to some suitable $F_{\mathrm{fin}}^{I}$ (cf. Rem. 5.25 and Th. 6.9).  

(d) In Ex. $5.6(\mathrm{d})(\mathrm{i})$ , we noted that the set ${\mathcal{P}}(\mathbb{K})$ of polynomial functions with coefficients in $\mathbb{K}$ is a vector space over $\mathbb{K}$ .We show the set $B:=\{e_{j}:j\in\mathbb{N}_{0}\}$ of monomial functions $e_{j}:\mathbb{K}\longrightarrow\mathbb{K}$ $e_{j}(x):=x^{j}$ , to be a basis of. ${\mathcal{P}}(\mathbb{K})$ : While $\langle B\rangle=\mathcal{P}(\mathbb{K})$ is immediate from the definition of ${\mathcal{P}}(\mathbb{K})$ , linear independence of $B$ can be shown. similarly to the linear independence of the exponential functions in Ex. 5.13(e): As in that example, we use the differentiability of the considered functions (here, the $e_{j}$ ) to show each set. $U_{n}:=\{e_{j}:j\in\{0,\dots,n\}\}$ $n\in\ensuremath{\mathbb{N}}_{0}$ , is linearly independent, using an induction on $n$ : Since, for $n=0$ $e_{n}\equiv1$ , the base case holds. Now let $n\geq1$ and assume $\lambda_{0},\dots,\lambda_{n}\in\mathbb{K}$ are such that  

$$
\underset{x\in\mathbb{R}}{\bigforall}\quad\sum_{j=0}^{n}\lambda_{j}x^{j}=0.
$$  

Differentiating (5.24) with respect to $x$ yields  

$$
\forall_{x\in\mathbb{R}}\quad\sum_{j=1}^{n}j\lambda_{j}x^{j-1}=0,
$$  

implying $\lambda_{1}=\dots=\lambda_{n}=0$ due to the induction hypothesis. Using this in (5.24), then yields $\lambda_{0}=\lambda_{0}x^{0}=0$ , completing the induction proof. We will see later that ${\mathcal{P}}(\mathbb{K})$ is, act uall, isomorphic, to $(\mathbb{K})_{\mathrm{fin}}^{\mathbb{N}}$  

Theorem 5.17. Let $V$ be a vector space over the field $F^{\prime}$ and $B\subseteq V$ . Then the following statements (i) - (ii) are equivalent:  

#### (i) $B$ is a basis of $V$  

(ii) $B$ is a maximal linearly independent subset of $V$ , i.e. $B$ is linearly independent and each set. $A\subseteq V$ with $B\subsetneq A$ is linearly dependent.  

(iii) $B$ is a minimal generating set for $V$ , i.e. $\langle B\rangle=V$ and $\langle A\rangle\subsetneq V$ for each $A\subsetneq B$ Proof. "(i)=(ii): Let $B\subseteq A\subseteq V$ and $a\in A\setminus B$ .Since $\langle B\rangle\:=\:V$ , there exist $\lambda_{1},\dots,\lambda_{n}\in F$ $b_{1},\ldots,b_{n}\in B$ $n\in\mathbb N$ , such that  

$$
a=\sum_{i=1}^{n}\lambda_{i}b_{i}\quad\Rightarrow\quad(-1)a+\sum_{i=1}^{n}\lambda_{i}b_{i}=0,
$$  

showing $A$ to be linearly dependent.  

"(ii)=>(i)": Suppose $B$ to be a maximal linearly independent subset of $V$ . We need to show $\langle B\rangle=V$ . Since $B\subseteq\langle B\rangle$ , let $v\in V\backslash B$ . Then $A:=\{v\}\cup B$ is linearly dependent,. i.e.  

$$
\begin{array}{r l}{\small\begin{array}{l}{\mathrm{\boldmath~\displaystyle\frac{1}{\mu_{u}}~}}\end{array}\left(\#W=n\in{\mathbb N}\quad\wedge\quad\sum_{u\in W}\lambda_{u}u=0\quad\wedge\quad\forall\quad\lambda_{u}\in F\quad\wedge\quad\underset{u\in W}{\exists}\lambda_{u}\neq0\right)}\end{array}
$$  

where the linear independence of $B$ implies $v\in W$ and $\lambda_{v}\neq0$ . Thus,  

$$
v=-\sum_{u\in W\backslash\{v\}}\lambda_{v}^{-1}\lambda_{u}u
$$  

showing. $v\in\langle B\rangle$ , since. $W\backslash\{v\}\subseteq B$  

"(i) $\Rightarrow$ (ii)" : Let $A\subsetneq B$ and $b\in B\setminus A$ . Since $B$ is linearly independent, Prop. 5.14(a) implies $b$ not to be a linear combination of elements in $A$ , showing $\langle A\rangle\subsetneq V$  

"(iii)=>(i)": We need to show that a minimal generating set for $V$ is linearly independent.. Arguing by contraposition, we let. $B$ be a generating set for. $V$ that is linearly dependent. and show $B$ is not minimal: Since. $B$ is linearly dependent, (5.25) holds with $A$ replaced by $B$ and there exists $b_{0}\in W$ with $\lambda_{b_{0}}\neq0$ , yielding  

$$
b_{0}=-\sum_{u\in W\backslash\{b_{0}\}}\lambda_{b_{0}}^{-1}\lambda_{u}u.
$$  

We show $A:=B\setminus\{b_{0}\}$ to be a generating set for $V$ : If $v\in V$ , since $\langle B\rangle=V$ , there exist $\lambda_{0},\lambda_{1},\ldots,\lambda_{n}\in F$ and $b_{1},\ldots,b_{n}\in A$ $n\in\mathbb N$ , such that  

$$
v=\lambda_{0}b_{0}+\sum_{i=1}^{n}\lambda_{i}b_{i}\stackrel{(5.26)}{=}-\sum_{u\in W\setminus\{b_{0}\}}\lambda_{0}\lambda_{b_{0}}^{-1}\lambda_{u}u+\sum_{i=1}^{n}\lambda_{i}b_{i}.
$$  

Since $u\in W\backslash\{b_{0}\}\subseteq A$ and $b_{1},\ldots,b_{n}\in A$ , this proves $A$ to be a generating set for $V$ i.e. $B$ is not minimal.  

Proposition 5.18. Let $V$ be a vector space over the field $F$ and $U\subseteq V$ a finite subset, $\#U=n\in\mathbb{N}$ $u_{0}\in U$ $\begin{array}{r}{v_{0}:=\sum_{u\in U}\lambda_{u}u}\end{array}$ with $\lambda_{u}~\in~F$ for each $u\in U$ and $\lambda_{u_{0}}~\neq~0$ $\tilde{U}:=\{v_{0}\}\cup(U\setminus\{u_{0}\})$  

(a) If $\langle U\rangle=V$ , then $\langle\tilde{U}\rangle=V$  

(b) If $U$ is linearly independent, then so is $\tilde{U}$  

(c) If $U$ is a basis of $V$ , then so is $\tilde{U}$  

Proof. Under the hypothesis, we have  

$$
u_{0}=\lambda_{u_{0}}^{-1}v_{0}-\lambda_{u_{0}}^{-1}\sum_{u\in U\backslash\{u_{0}\}}\lambda_{u}u.
$$  

(a): If $v\in V$ , then there exist $\mu_{u}\in F$ $u\in U$ , such that  

$$
\gamma=\sum_{u\in U}\mu_{u}u=\mu_{u_{0}}u_{0}+\sum_{u\in U\setminus\{u_{0}\}}\mu_{u}u\stackrel{(5.27)}{=}\mu_{u_{0}}\lambda_{u_{0}}^{-1}v_{0}+\sum_{u\in U\setminus\{u_{0}\}}\big(\mu_{u}-\mu_{u_{0}}\lambda_{u_{0}}^{-1}\lambda_{u}\big)u,
$$  

showing $\langle\tilde{U}\rangle=V$  

(b): Suppose $\mu_{0}\in{\cal F}$ and $\mu_{u}\in F$ $u\in U\setminus\{u_{0}\}$ , are such that  

$$
0=\mu_{0}v_{0}+\sum_{u\in U\backslash\{u_{0}\}}\mu_{u}u\overset{(5.27)}{=}\mu_{0}\lambda_{u_{0}}u_{0}+\sum_{u\in U\backslash\{u_{0}\}}(\mu_{0}\lambda_{u}+\mu_{u})u.
$$  

Since $U$ is linearly independent, we obtain $\mu_{0}\lambda_{u_{0}}=0=\mu_{0}\lambda_{u}+\mu_{u}$ for each $u\in U\backslash\{u_{0}\}$ Since $\lambda_{u_{0}}\neq0$ , we have $\mu_{0}=0$ , then also implying $\mu_{u}=0$ for each $u\in U\backslash\{u_{0}\}$ , showing $\tilde{U}$ to be linearly independent.  

(c) is now immediate from combining (a) and (b).  

Theorem 5.19 (Coordinates). Let $V$ be a vector space over the field. $F$ and assume $B\subseteq V$ is a basis of. $V$ .Then each vector. $v\in V$ has unique coordinates with respect to the basis $B$ , i.e., for each. $v\in V$ , there exists a unique finite subset $B_{v}$ of $B$ and $a$ unique map $c:B_{v}\longrightarrow F\backslash\{0\}$ such that  

$$
v=\sum_{b\in B_{v}}c(b)b.
$$  

Note that, for. $v=0$ , one has. $B_{v}=\emptyset$ $c$ is the empty map, and (5.28) becomes $0~=$ $\textstyle\sum_{b\in\emptyset}c(b)b$  

Proof. The existence of. $B_{v}$ and the map $c$ follows from the fact that the basis. $B$ is a generating set, $\langle B\rangle=V$ . For the uniqueness proof, consider finite sets $B_{v},\tilde{B}_{v}\subseteq B$ and maps $c:B_{v}\longrightarrow F\backslash\{0\}$ $\tilde{c}:\tilde{B}_{v}\longrightarrow F\backslash\{0\}$ such that  

$$
v=\sum_{b\in B_{v}}c(b)b=\sum_{b\in\tilde{B}_{v}}\tilde{c}(b)b.
$$  

Extend both $c$ and $\ddot{c}$ to $A:=B_{v}\cup\tilde{B}_{v}$ by letting $c(b):=0$ for $b\in\tilde{B}_{v}\backslash B_{v}$ and $\tilde{c}(b):=0$ for $b\in B_{v}\backslash\tilde{B}_{v}$ . Then  

$$
0=\sum_{b\in A}\left(c(b)-\tilde{c}(b)\right)b,
$$  

such that the linear independence of $A$ implies $c(b)={\tilde{c}}(b)$ for each $b\in A$ , which, in turn, implies $B_{v}=\tilde{B}_{v}$ and $c=\widetilde c$ $\vert$  

Remark 5.20. If the basis. $B$ of $V$ has finitely many elements, then one often enumerates. the elements $B=\{b_{1},\ldots,b_{n}\}$ $n=\#B\in\mathbb{N}$ , and writes $\lambda_{i}:=c(b_{i})$ for $b_{i}\in B_{v}$ $\lambda_{i}:=0$ for $b_{i}\notin B_{v}$ , such that (5.28) takes the, perhaps more familiar looking, form  

$$
v=\sum_{i=1}^{n}\lambda_{i}b_{i}.
$$  

In Ex. 5.16(c), we have seen that the vector space $F^{n}$ $n\in\mathbb{N}$ , over $F$ has the finite basis $\{e_{1},\ldots,e_{n}\}$ and, more generally, that, for each set. $I$ $B=\{e_{i}:i\in I\}$ is a basis for the vector space $F_{\mathrm{fin}}^{I}$ over $F$ . Since, clearly, $B$ and $I$ have the same cardinality (via the bijective map $i\mapsto e_{i}$ ), this shows that, for each set. $I$ , there exists a vector space,. whose basis has the same cardinality as. $I$ . In Th. 5.23 below, we will show one of the fundamental results of vector space theory, namely that every vector space has a basis and that two bases of the same vector space always have the same cardinality (which is referred to as the dimension of the vector space, cf. Def. 5.24).  

As some previous results of this class, the proof of Th. 5.23 makes use of the axiom of choice (AC) of Appendix A.4, which postulates, for each nonempty set $\mathcal{M}$ , whose elements are all nonempty sets, the existence of a choice function, that means a function that assigns, to each. $M\in\mathcal{M}$ , an element $m\in M$ . Somewhat surprisingly, AC can not. be proved (or disproved) from ZF, i.e. from the remaining standard axioms of set theory (see Appendix A.4 for a reference). Previously, when AC was used, choice functions were employed directly. However, in the proof of Th. 5.23, AC enters in the form of Zorn's lemma. While Zorn's lemma turns out to be equivalent to AC, the equivalence is not obvious (see Th. A.52(iii)). However, Zorn's lemma provides an important technique for conducting existence proofs that is encountered frequently throughout mathematics, and the proof of existence of a basis in a vector space is the standard place to first encounter and learn this technique (as it turns out, the existence of bases in vector spaces is, actually, also equivalent to AC - see the end of the proof of Th. A.52 for a reference).  

The following Def. 5.21 prepares the statement of Zorn's lemma:  

Definition 5.21 (Same as Part of Appendix Def. A.50). Let $X$ be a set and let $\leq$ be a partial order on. $X$  

(a) An element $m\in X$ is called maximal (with respect to. $\leq$ ) if, and only if, there exists. no $x\in X$ such that $m\leq x$ (note that a maximal element does not have to be a max and that a maximal element is not necessarily unique).  

(b) A nonempty subset. $C$ of $X$ is called a chain if, and only if, $C$ is totally ordered by. $\leq$  

Theorem 5.22 (Zorn's Lemma). Let $X$ be a nonempty partially ordered set. If every. chain $C\subseteq X$ (i.e. every nonempty totally ordered subset of. $X$ ) has an upper bound in. $X$ (such chains with upper bounds are sometimes called inductive), then $X$ contains a maximal element (cf. Def. 5.21(a)).  

Proof. According to Th. A.52(iii), Zorn's lemma is equivalent to the axiom of choice.  

Theorem 5.23 (Bases). Let $V$ be a vector space over the field $F^{\prime}$  

(a) If $U\subseteq V$ is linearly independent, then there exists a basis of $V$ that contains $U$   
(b) $V$ has a basis $B\subseteq V$   
(c) Bases of $V$ have a unique cardinality, i.e. if $B\subseteq V$ and $\tilde{B}\subseteq V$ are both bases of $V$ , then there exists a bijective map $\phi:B\longrightarrow{\tilde{B}}$ . In particular, if $\#B=n\in\mathbb{N}_{0}$ then $\#{\tilde{B}}=n$   
(d) If $B$ is a basis of $V$ and $U\subseteq V$ is linearly independent, then there exists $C\subseteq B$ such that $\tilde{B}:=U\cup C$ is a basis of $V$ . In particular, if $\#B=n\in\mathbb{N}$ $B=\{b_{1},\ldots,b_{n}\}$ then $\#U=m\in\mathbb{N}$ with $m\leq n$ , and, if $U=\{u_{1},\ldots,u_{m}\}$ , then there exist distinct $u_{m+1},\dotsc,u_{n}\in B$ such that $\tilde{B}=\{u_{1},\ldots,u_{n}\}$ is a basis of $V$  

Proof. If. $V$ is generated by finitely many vectors, then the proof does not need Zorn's lemma and, thus, we treat this case first: If. $V=\{0\}$ , then (a) - (d) clearly hold. Thus, we also assume $V\neq\{0\}$ . To prove (d), assume. $B=\{b_{1},\ldots,b_{n}\}$ is a basis of. $V$ with $\#B=n\in\mathbb{N}$ .We first show, by induction on $m\in\{1,\ldots,n\}$ that, if $U$ is linearly independent, $\#U=m$ $U=\{u_{1},\ldots,u_{m}\}$ , then there exist distinct $u_{m+1},\ldots,u_{n}\in B$ such that $\dot{B}=\{u_{1},\ldots,u_{n}\}$ is a basis of $V$ : If $m=1$ , we write $\textstyle u_{1}=\sum_{i=1}^{n}\lambda_{i}b_{i}$ with $\lambda_{i}\in F$ .Since $u_{1}\neq0$ , there exists $i_{0}\in\{1,\ldots,n\}$ such that $\lambda_{i_{0}}~\neq~0$ . Then $\tilde{B}:= $ $\{u_{1}\}\cup(B\setminus\{b_{i_{0}}\})$ is a basis of $V$ by Prop. 5.18(c), thereby establishing the base case. If $1<m\le n$ , then, by induction hypothesis, there exist distinct $c_{m},c_{m+1},\dots,c_{n}\in B$ such that $\{u_{1},\dots,u_{m-1}\}\cup\{c_{m},c_{m+1},\dots,c_{n}\}$ forms a basis of $V$ . Then there exist $\mu_{i}\in{\cal F}$ such that  

$$
u_{m}=\sum_{i=1}^{m-1}\mu_{i}u_{i}+\sum_{i=m}^{n}\mu_{i}c_{i}.
$$  

There then must exist $i_{0}\in\{m,\dots,n\}$ such that $\mu_{i_{0}}\mathrm{~\ensuremath~{~\neq~0~}~}$ , since, otherwise, $U$ were linearly dependent. Thus, again, by Prop. 5.18(c),. $B:=U\cup(\{c_{m},c_{m+1},\ldots,c_{n}\}\setminus\{c_{i_{0}}\})$ forms a basis of $V$ , completing the induction. Now suppose $m>n$ . Then the above shows $\{u_{1},\ldots,u_{n}\}$ to form a basis of $V$ , in contradiction to the linear independence of. $U$ . This then also implies that $U$ can not be infinite. Thus, we always have. $\#U=m\leq n$ and $\#(B\setminus\{u_{m+1},\dots,u_{n}\})=m$ , completing the proof of (d). Now if $U$ is not merely. linearly independent, but itself a basis of. $V$ , then we can switch the roles of $B$ and $U$ obtaining $\mathit{\Delta}_{T I l}=\mathit{\Delta}_{n}$ , proving (c). Since we assume $V$ to be generated by finitely many vectors, there exists $C\subseteq V$ with $\langle C\rangle=V$ and $\#C=k\in\mathbb{N}$ . Then $C$ is either a basis or it is not minimal, in which case there exists $c\in C$ such that ${\ddot{C}}:=C\setminus\{c\}$ still generates. $V$ $\#\tilde{C}=k-1$ . Proceeding inductively, we can remove vectors until we obtain a basis of $V$ , proving (b). Combining (b) with (d), now proves (a).  

General Case: Here, we prove (a) first, making use of Zorn's lemma: Given a linearly independent set $U\subseteq V$ , define  

$$
{\mathcal{M}}:=\left\{M\subseteq V:U\subseteq M{\mathrm{~and~}}M{\mathrm{~is~linearly~independent}}\right\}
$$  

and note that set inclusion $\subseteq$ constitutes a partial order on $\mathcal{M}$ . Moreover, $U\in\mathcal{M}$ , i.e $\mathcal{M}\neq\emptyset$ . Let $\mathcal{C}\subseteq\mathcal{M}$ be a chain, i.e. assume ${\mathcal{C}}\neq\emptyset$ to be totally ordered by. $\subseteq$ . Define  

$$
C_{0}:=\bigcup_{C\in\mathcal{C}}C.
$$  

It is then immediate that $C\in{\mathcal{C}}$ implies $C\subseteq C_{0}$ , i.e. $C_{0}$ is an upper bound for $\mathit{c}$ Moreover, $C_{0}~\in~\mathcal{M}$ : Indeed, if $C\in{\mathcal{C}}$ , then $U\subseteq C\subseteq C_{0}$ .To verify $C_{0}$ is linearly independent, let $c_{1},\ldots,c_{n}\in C_{0}$ be distinct and $\lambda_{1},\dots,\lambda_{n}\in F$ $n\in\mathbb N$ , with  

$$
0=\sum_{i=1}^{n}\lambda_{i}c_{i}.
$$  

Then, for each $i\in\{1,\ldots,n\}$ , there exists $C_{i}\in{\mathcal{C}}$ with $c_{i}\in C_{i}$ . Since  

$$
\mathcal{D}:=\{C_{1},...,C_{n}\}\subseteq\mathcal{C}
$$  

is totally ordered by. $\subseteq$ , by Th. 3.25(a), there exist $i_{0}\in\{1,\ldots,n\}$ such that $C_{i_{0}}=\operatorname*{max}{\mathcal{D}}$ i.e. $C_{i}\subseteq C_{i_{0}}$ for each $i\in\{1,\ldots,n\}$ , implying $c_{i}\in C_{i_{0}}$ for each $i\in\{1,\ldots,n\}$ as well. As $C_{i_{0}}$ is linearly independent, $\lambda_{1}=\dots=\lambda_{n}=0$ , showing $C_{0}$ is linearly independent, as desired. Having, thus, verified all hypotheses of Zorn's lemma, Th. 5.22 provides a maximal element $B\in{\mathcal{M}}$ . By Th. 5.17(ii),. $B$ is a basis of $V$ . As $U\subseteq B$ also holds, this proves (a) and, in particular, (b).  

To prove (c), let $B_{1},B_{2}$ be bases of $V$ . As we have shown above that (c) holds, provided $B_{1}$ or $B_{2}$ is finite, we now assume $B_{1}$ and $B_{2}$ both to be infinite. We show the existence of an injective map $\phi_{1}:B_{2}\longrightarrow B_{1}$ : To this end, for each $v\in B_{1}$ , let $B_{2,v}$ be the finite subset of $B_{2}$ given by Th. 5.19, consisting of all $b\in B_{2}$ such that the coordinate of $v$ with respect to $b$ is nonzero. Let $\psi_{v}:B_{2,v}\longrightarrow\{1,...,\#B_{2,v}\}$ be bijective. Also define  

$$
E:=\bigcup_{v\in B_{1}}B_{2,v}.
$$  

Then, since. $V=\langle B_{1}\rangle$ , we also have. $V=\langle E\rangle$ . Thus, as $E\subseteq B_{2}$ and the basis. $B_{2}$ is a minimal generating set, we obtain $E=B_{2}$ . In particular, for each. $b\in B_{2}$ , we may choose some $v(b)\in B_{1}$ such that $b\in B_{2,v(b)}$ . The map  

$$
f:B_{2}\longrightarrow B_{1}\times\mathbb{N},\quad f(b):=\big(v(b),\psi_{v(b)}(b)\big),
$$  

is then, clearly, well-defined and injective. Moreover, Th. A.57 of the Appendix provides us with a bijective map $\phi_{B_{1}}:B_{1}\times\mathbb{N}\longrightarrow B_{1}$ .In consequence, $\phi_{1}:\:\:B_{2}\longrightarrow B_{1}$ $\phi_{1}:=\phi_{B_{1}}\circ f$ is injective as well. Since $B_{1},B_{2}$ were arbitrary bases, we can interchange the roles of. $B_{1}$ and $B_{2}$ to also obtain an injective map $\phi_{2}:B_{1}\longrightarrow B_{2}$ . According to the Schroder-Bernstein Th. 3.12, there then also exists a bijective map $\phi:B_{1}\longrightarrow B_{2}$ completing the proof of (c).  

To prove (d), let $B$ be a basis of $V$ and let $U\subseteq V$ be linearly independent. Analogously. to the proof of (a), apply Zorn's lemma, but this time with the set  

$$
{\mathcal{M}}:=\{M\subseteq V:M=U\dot{\cup}C,C\subseteq B,M\mathrm{~is~linearly~independent}\},
$$  

such that the maximal element $\tilde{B}\in\mathcal{M}$ , obtained from Th. 5.22, has the form $\tilde{B}=U\dot{\cup}C$ with $C\subseteq B$ . We claim $\tilde{B}$ to be a basis of $V$ : Linear independence is clear, since $\tilde{B}\in\mathcal{M}$ and it only remains to check $\langle\tilde{B}\rangle=V$ . Due to the maximality of $\tilde{B}$ , if $b\in B$ , there exist a finite set $\tilde{B}_{b}\subseteq\tilde{B}$ and $\lambda_{b u}\in F$ $u\in\tilde{B}_{b}$ , such that  

$$
b=\sum_{u\in\tilde{B}_{b}}\lambda_{b u}u.
$$  

Now let. $v\in V$ be arbitrary. As $B$ is a basis of.. $V$ , there exist. $b_{1},\ldots,b_{n}\in B$ and  

$\lambda_{1},\dots,\lambda_{n}\in F$ $n\in\mathbb N$ , such that  

$$
v=\sum_{i=1}^{n}\lambda_{i}b_{i}\stackrel{(5.35)}{=}\sum_{i=1}^{n}\sum_{u\in\tilde{B}_{b_{i}}}\lambda_{i}\lambda_{b_{i}u}u,
$$  

proving $\langle\tilde{B}\rangle=V$ as desired.  

Definition 5.24. According to Th. 5.23, for each vector space $V$ over a field $F^{\prime}$ , the cardinality of its bases is unique. This unique cardinality is called the dimension of $V$ and is denoted $\mathrm{dim}V$ . If $\dim V<\infty$ (i.e. $\dim V\in\mathbb{N}_{0}$ ), then $V$ is called finite-dimensional, otherwise infinite-dimensional.  

Remark 5.25. Let $F^{\prime}$ be a field. In Ex. 5.16(c), we saw that $B=\{e_{i}:i\in I\}$ with  

$$
\begin{array}{r}{\underset{i\in I}{\forall}\quad e_{i}:I\longrightarrow F,\quad e_{i}(j)=\delta_{i j}:=\left\{\begin{array}{l l}{1}&{\mathrm{if~}i=j,}\ {0}&{\mathrm{if~}i\neq j,}\end{array}\right.}\end{array}
$$  

is a basis of $F_{\mathrm{fin}}^{I}$ . Since $\#B=\#I$ , we have shown  

$$
\dim{\cal F}_{\mathrm{fin}}^{I}=\#I,
$$  

and, in particular, for $I=\{1,\dots,n\}$ $n\in\mathbb N$  

$$
\dim{\cal F}^{n}=\dim\mathbb{R}^{n}=\dim\mathbb{C}^{n}=n.
$$  

We will see in Th. 6.9 below that, in a certain sense, $F_{\mathrm{fin}}^{I}$ is the only vector space of. dimension $\#I$ over $F$ . In particular, for. $n\in\mathbb{N}$ , one can think of $F^{n}$ as the standard model of an. $n$ -dimensional vector space over. $F$  

Remark 5.26. Bases of vector spaces are especially useful if they are much smaller than the vector space itself, as in the case of finite-dimensional vector spaces over infinite fields, ${\mathbb R}^{n}$ and $\mathbb{C}^{n}$ being among the most important examples. For infinite-dimensional vector spaces $V$ , one often has $\dim V=\#V$ (cf. Th. E.1 and Cor. E.2 in the Appendix). such that vector space bases are not as helpful in such situations. On the other hand, infinite-dimensional vector spaces might come with some additional structure, providing a more useful notion of basis (e.g., in infinite-dimensional Hilbert spaces, one typically uses so-called orthonormal bases rather than vector space bases).  

In the rest of the section, we investigate relations between bases and subspaces; and we introduce the related notions direct complement and direct sum..  

Theorem 5.27. Let. $V$ be a vector space over the field $F^{\prime}$ and let. $U$ be a subspace of. $V$ (a) If $B_{U}$ is a basis of $U$ , then there exists a basis $B$ of $V$ with $B_{U}\subseteq B$ (b) $\dim U\leq\dim V$ , i.e. if $B_{U}$ is a basis of $U$ and $B$ is a basis of $V$ , then there exists an injective map $\phi:B_{U}\longrightarrow B$  

(c) There exists a subspace $U^{\prime}$ of $V$ such that $V=U+U^{\prime}$ and $U\cap U^{\prime}=\{0\}$  

(d) I $f\dim V=n\in\mathbb{N}_{0}$ , then  

$$
\dim U=\dim V\quad\Leftrightarrow\quad U=V.
$$  

Proof. (a): Let $B_{U}$ be a basis of $U$ . Since $B_{U}$ is a linearly independent subset of $V$ , we can employ Th. 5.23(a) to obtain $C\subseteq V$ such that $B:=B_{U}\dot{\cup}C$ is a basis of $V$  

(b): Let $B_{U}$ and $B$ be bases of $U$ and $V$ , respectively. As in the proof of (a), choose $C\subseteq V$ such that $\tilde{B}:=B_{U}\dot{\cup}C$ is a basis of $V$ . According to Th. 5.23(c), there exists a bijective map $\phi_{V}:\tilde{B}\longrightarrow B$ . Then the map $\phi:=\phi_{V}\lceil_{B_{U}}$ is still injective.  

(c): Once again, let $B_{U}$ be a basis of $U$ and choose $C\subseteq V$ such that $B:=B_{U}\dot{\cup}C$ is a basis of $V$ . Define $U^{\prime}:=\langle C\rangle$ . Since $B=B_{U}\dot{\cup}C$ is a basis of $V$ , it is immediate that $V=U+U^{\prime}$ . Now suppose $u\in U\cap U^{\prime}$ . Then there exist $\lambda_{1},\dots,\lambda_{m},\mu_{1},\dots,\mu_{n}\in F$ with $m,n\in\mathbb{N}$ , as well as distinct $b_{1},\dots,b_{m}\in B_{U}$ and distinct $c_{1},\ldots,c_{n}\in C$ such that  

$$
u=\sum_{i=1}^{m}\lambda_{i}b_{i}=\sum_{i=1}^{n}\mu_{i}c_{i}\quad\Rightarrow\quad0=\sum_{i=1}^{m}\lambda_{i}b_{i}-\sum_{i=1}^{n}\mu_{i}c_{i}.
$$  

Since $\{b_{1},\ldots,b_{m},c_{1},\ldots,c_{n}\}\subseteq B$ is linearly independent, this implies $0=\lambda_{1}=\cdots=$ $\lambda_{m}=\mu_{1}=\cdots=\mu_{n}$ and $u=0$  

(d): Let $\dim U=\dim V=n\in\mathbb{N}_{0}$ . If $B_{U}$ is a basis of $U$ , then $\#B_{U}=n$ and, by (a), $B_{U}$ must also be a basis of $V$ , implying $U=\langle B_{U}\rangle=V$  

Definition 5.28. Let $V$ be a vector space over the field $F$ and let $U,W$ be subspaces of $V$ . Then $W$ is called a direct complement of $U$ if, and only if,. $V=U+W$ and $U\cap W=\{0\}$ . In that case, we also write $V=U\oplus W$ and we say that. $V$ is the direct. sum of $U$ and $W$  

Caveat: While set-theoretic complements. $A\backslash B$ are uniquely determined by. $A$ and $B$ nontrivial direct complements of vector subspaces are never unique, as shown in the following proposition:  

Proposition 5.29. Let $V$ be a vector space over the field $F^{\prime}$ and let $U,W$ be subspaces of $V$ such that $V=U\oplus W$ . If there exist. $0\neq u\in U$ and $0\neq w\in W$ , then there exists. a subspace $\tilde{W}\neq W$ of $V$ with $V=U\oplus{\tilde{W}}$  

Proof. According to Th. 5.23(d), there exist bases $B_{U}$ of $U$ and $B_{W}$ of $W$ with $u\in B_{U}$ and $w\in B_{W}$ . Then $v:=u+w\notin W$ , since, otherwise $u=(u+w)-w\in W$ , in contradiction to $U\cap W=\{0\}$ . Let ${\tilde{B}}:=\{v\}\cup(B_{W}\setminus\{w\})$ and $\tilde{W}:=\langle\tilde{B}\rangle$ . Suppose, $x\in U\cap{\tilde{W}}$ . Then there exist distinct $w_{1},\hdots,w_{n}\in B_{W}\backslash\{w\}$ and $\lambda_{0},\lambda_{1},\dots,\lambda_{n}\in F$ $n\in\mathbb N$ , such that  

$$
x=\lambda_{0}(u+w)+\sum_{i=1}^{n}\lambda_{i}w_{i}.
$$  

Since $x\in U$ , we also obtain $x-\lambda_{0}u\in U$ .Also $\begin{array}{r}{x-\lambda_{0}u=\lambda_{0}w+\sum_{i=1}^{n}\lambda_{i}w_{i}\in W}\end{array}$ implying  

$$
0=x-\lambda_{0}u=\lambda_{0}w+\sum_{i=1}^{n}\lambda_{i}w_{i}.
$$  

However, $w,w_{1},\dots,w_{n}\in B_{W}$ are linearly independent, yielding $0=\lambda_{0}=\cdots=\lambda_{n}$ and, thus, $x=0$ , showing $U\cap\tilde{W}=\{0\}$ . To obtain $V=U\oplus W$ , it remains to show $w\in U+\tilde{W}$ (since $V=U\oplus W$ $U\subseteq U+{\tilde{W}}$ , and $B_{W}\backslash\{w\}\subseteq\tilde{W}\subseteq U+\tilde{W}\}$ . Since $w=-u+(u+w)\in U+\dot{W}$ , the proof is complete.  

Theorem 5.30. Let. $V$ be a vector space over the field $F^{\prime}$ and let. $U,W$ be subspaces of $V$ . Moreover, let. $B_{U},B_{W},B_{+},B_{\cap}$ be bases of. $U,W,U+W,U\cap W$ , respectively.  

(a) $U+W=\langle B_{U}\cup B_{W}\rangle.$  

(b) If $U\cap W=\{0\}$ , then $B_{U}\dot{\cup}B_{W}$ is a basis of $U\oplus W$  

(c) It holds that  

$$
\dim(U+W)+\dim(U\cap W)=\dim U+\dim W,
$$  

by which we mean that there exists a bijective map  

$$
\phi:(B_{U}\times\{0\})\dot{\cup}(B_{W}\times\{1\})\longrightarrow(B_{+}\times\{0\})\dot{\cup}(B_{\cap}\times\{1\}).
$$  

(d) Suppose $B:=B_{U}\dot{\cup}B_{W}$ is a basis of $V$ . Then $V=U\oplus W$  

Proof. (a): Let $B:=B_{U}\cup B_{W}$ . If $v=u+w$ with $u\in U$ $w\in W$ , then there exist distinct $u_{1},\dotsc,u_{n}\in B_{U}$ , distinct $w_{1},\dotsc,w_{m}\in B_{W}$ $m,n\in\mathbb{N})$ , and $\lambda_{1},\dots,\lambda_{n},\mu_{1},\dots,\mu_{m}\in F$ such that  

$$
v=u+w=\sum_{i=1}^{n}\lambda_{i}u_{i}+\sum_{i=1}^{m}\mu_{i}w_{i},
$$  

showing $U+W=\langle B\rangle$  

(b): Let $B:=B_{U}\cup B_{W}$ .We know $U\oplus W=\langle B\rangle$ from (a). Now consider (5.39) with $u+w=0$ . Then $u=-w\in U\cap W=\{0\}$ , i.e. $u=0$ . Then $w=0$ as well and $0=\lambda_{1}=\dots=\lambda_{n}=\mu_{1}=\dots=\mu_{m}$ , due to the linear independence of the $u_{1},\ldots,u_{n}$ and the linear independence of the $w_{1},\ldots,w_{m}$ . In consequence, $B$ is linearly independent as well and, thus, a basis of $U\oplus W$  

(c): According to Th. 5.27(a), we may choose $B_{U}$ and $B_{W}$ such that $B_{\cap}\subseteq B_{U}$ and $B_{\cap}\subseteq B_{W}$ . Let $B_{0}:=B_{U}\setminus B_{\cap}$ $U_{0}:=\langle B_{0}\rangle$ $B_{1}:=B_{W}\setminus B_{\cap}$ $U_{1}:=\langle B_{1}\rangle$ . Then  

$$
B:=B_{U}\cup B_{W}=B_{0}\cup B_{1}\cup B_{\cap}
$$  

is linearly independent: Consider, once again, the situation of the proof of (b), with $v=0$ and, this time, with $u_{1},\ldots,u_{n}\in B_{0}$ . Again, we obtain $u=-w\in W$ , i.e.  

$$
u\in U_{0}\cap(U\cap W)=\langle B_{0}\rangle\cap\langle B_{\cap}\rangle\stackrel{\mathrm{Prop.}\ni.14(\mathrm{d})}{=}\langle B_{0}\cap B_{\cap}\rangle=\{0\}.
$$  

Thus, $0=\lambda_{1}=\dots=\lambda_{n}=0$ , due to the linear independence of $B_{0}$ . This then implies $w=0$ and $0=\mu_{1}=\cdots=\mu_{m}$ due to the linear independence of $B_{W}$ , yielding the. claimed linear independence of $B$ . According to (a), we also have $U+W=\langle B\rangle$ , i.e. $B$ is a basis of. $U+W$ . Now we are in a position to define  

$$
\begin{array}{r l}&{\phi:(B_{U}\times\{0\})\dot{\cup}(B_{W}\times\{1\})\longrightarrow(B\times\{0\})\dot{\cup}(B_{\cap}\times\{1\}),}\ &{\phi(b,\alpha):=\left\{\begin{array}{l l}{(b,0)}&{\mathrm{for~}b\in B_{U}\mathrm{~and~}\alpha=0,}\ {(b,0)}&{\mathrm{for~}b\in B_{1}\mathrm{~and~}\alpha=1,}\ {(b,1)}&{\mathrm{for~}b\in B_{\cap}\mathrm{~and~}\alpha=1,}\end{array}\right.}\end{array}
$$  

which is, clearly, bijective. Bearing in mind Th. 5.23(c), this proves (c)  

(d): As $B=B_{U}\dot{\cup}B_{W}$ is a basis of $V$ , we can write each $v\in V$ as $v=u+w$ with $u\in U$ and $w\in W$ , showing $V=U+W$ . On the other hand,  

$$
{\cal U}\cap{\cal V}=\langle B_{U}\rangle\cap\langle B_{V}\rangle\stackrel{\mathrm{Prop.}~5.14(\mathrm{d})}{=}\langle B_{U}\cap B_{V}\rangle=\{0\},
$$  

proving $V=U\oplus W$  

## 6 Linear Maps  

### 6.1 Basic Properties and Examples  

In previous sections, we have studied structure-preserving maps, i.e. homomorphisms, in the context of magmas (in particular, groups) and rings (in particular, fields), cf. Def..  

4.10 and Def. 4.34(b). In the context of vector spaces, the homomorphisms are so-called linear maps, which we proceed to define and study next.  

Definition 6.1. Let $V$ and $W$ be vector spaces over the field. $F^{\prime}$ . A map $A:V\longrightarrow W$ is called vector space homomorphism or $F^{\prime}$ -linear (or merely linear if the field. $F^{\prime}$ is understood) if, and only if,  

$$
\begin{array}{r l}&{\underset{{\boldsymbol{v}}_{1},{\boldsymbol{v}}_{2}\in V}{\forall}\quad A({\boldsymbol{v}}_{1}+{\boldsymbol{v}}_{2})=A({\boldsymbol{v}}_{1})+A({\boldsymbol{v}}_{2}),}\ {\underset{\lambda\in F}{\underset{\boldsymbol{v}}{\rightleftharpoons}}\underset{{\boldsymbol{v}}\in V}{\forall}\quad A(\lambda{\boldsymbol{v}})=\lambda A({\boldsymbol{v}})}\end{array}
$$  

or, equivalently, if, and only if,  

$$
\begin{array}{r l}{\bigforall}&{{}\quad\forall_{\lambda,\mu\in F}\quad v_{1,v_{2}\in V}\quad A(\lambda v_{1}+\mu v_{2})=\lambda A(v_{1})+\mu A(v_{2})}\end{array}
$$  

(note that, in general, vector addition and scalar multiplication will be different on the left-hand sides and right-hand sides of the above equations). Thus, $A$ is linear if, and only if, it is a group homomorphism with respect to addition and also satisfies (6.1b). In particular, if $A$ is linear, then $\ker A$ and $\operatorname{Im}A$ are defined by Def. 4.19, i.e.  

$$
\begin{array}{l}{\ker A=A^{-1}\{0\}=\{v\in V:A(v)=0\},}\ {\operatorname{Im}A=A(V)=\{A(v):v\in V\}.}\end{array}
$$  

We denote the set of all $F$ -linear maps from $V$ into $W$ by $\mathcal{L}(V,W)$ .The notions vector space (or linear) monomorphism, epimorphism, isomorphism, endomorphism, automorphism are then defined as in Def. 4.10. Moreover, $V$ and $W$ are called isomorphic (denoted $V\cong W$ ) if, and only if, there exists a vector space isomorphism $A:V\longrightarrow W$  

Before providing examples of linear maps in Ex. 6.7 below, we first provide and study some basic properties of such maps..  

Notation 6.2. For the composition of linear maps $A$ and $B$ , we often write $B A$ instead of $B\circ A$ . For the application of a linear map, we also often write $A v$ instead of $A(v)$  

Proposition 6.3. Let. $V,W,X$ be vector spaces over the field $F$ (a) If $A:V\longrightarrow W$ and $B:W\longrightarrow X$ are linear, then so is $B A$ (b) If $A:V\longrightarrow W$ is a linear isomorphism, then. $A^{-1}$ is a linear isomorphism as well. (i.e. $A^{-1}$ is not only bijective, but also linear).  

(c) Let $A\in{\mathcal{L}}(V,W)$ .If $U_{W}$ is a subspace of $W$ and $U_{V}$ is a subspace of $V$ , then $A^{-1}(U_{W})$ is a subspace of $V$ and $A(U_{V})$ is a subspace of $W$ .The most important special cases are that $\ker A=A^{-1}(\{0\})$ is a subspace of $V$ and $\operatorname{Im}A=A(V)$ is $a$ subspace of $W$  

(d) $A\in{\mathcal{L}}(V,W)$ is injective if, and only if, $\ker A=\{0\}$  

Proof. (a): We note $B A$ to be a homomorphism with respect to addition by Prop. 4.11(a). Moreover, if $v\in V$ and $\lambda\in F$ , then  

$$
(B A)(\lambda v)=B(A(\lambda v))=B(\lambda(A v))=\lambda(B(A v))=\lambda((B A)(v)),
$$  

proving the linearity of $B A$  

(b): $A^{-1}$ is a homomorphism with respect to addition by Prop. 4.11(b). Moreover, if $w\in W$ and $\lambda\in F$ , then  

$$
A^{-1}(\lambda w)=A^{-1}\Bigl(\lambda\bigl(A(A^{-1}w)\bigr)\Bigr)=A^{-1}\Bigl(A\bigl(\lambda(A^{-1}w)\bigr)\Bigr)=\lambda(A^{-1}w),
$$  

proving the linearity of $A^{-1}$  

(c): According to Th. 4.20(a),(d), $A^{-1}(U_{W})$ is a subgroup of $V$ and $A(U_{V})$ is a subgroup of $W$ .Since $0~\in~U_{W}$ $0\in A^{-1}(U_{W})$ .Moreover, if $\lambda\in F$ and $v\in A^{-1}(U_{W})$ , then $A v\in U_{W}$ and, thus  

$$
A(\lambda v)=\lambda(A v)\in U_{W},
$$  

since $U_{W}$ is a subspace of. $W$ . This shows. $\lambda v\in A^{-1}(U_{W})$ and that $A^{-1}(U_{W})$ is a subspace of $V$ . If $w\in\operatorname{Im}A$ , then there exists $v\in V$ with $A v=w$ . Thus, if. $\lambda\in F$ , then  

$$
A(\lambda v)=\lambda(A v)=\lambda w,
$$  

showing. $\lambda w\in\operatorname{Im}A$ and that $\operatorname{Im}A$ is a subspace of. $W$ . In particular ${\cal A}(U_{V})=\mathrm{Im}\big({\cal A}\vert_{U_{V}}\big)$ is a subspace of $W$  

(d) is merely a restatement of Th. 4.20(e) for the current situation.  

Proposition 6.4. Let $V$ be a vector space over the field $F^{\prime}$ and let $W$ be a set with compositions $+:W\times W\longrightarrow W$ and : : $F\times W\longrightarrow W$ .If $A:V\longrightarrow W$ is an epimorphism with respect to $^+$ that also satisfies (6.1b), then $W$ $(w i t h+a n d\cdot)$ , is a vector space over $F^{\prime}$ as well.  

Proof. Exercise.  

Proposition 6.5. Let. $V$ and $W$ be vector spaces over the field $F$ , and let. $A:V\longrightarrow W$   
be linear..  

(a) A is injective if, and only if, for each linearly independent subset $S$ of $V$ $A(S)$ is a linearly independent subset of $W$  

(b) A is surjective if, and only if, for each generating subset $S$ of $V$ $A(S)$ is a generating subset of W.  

(c) A is bijective if, and only if, for each basis $B$ of $V$ $A(B)$ is a basis of. $W$  

Proof. Exercise.  

Theorem 6.6. Let $V$ and $W$ be vector spaces over the field $F^{\prime}$ . Then each linear map $A:V\longrightarrow W$ is uniquely determined by its values on a basis of $V$ . More precisely, if $B$ is a basis of. $V$ $(w_{b})_{b\in B}$ is a family in. $W$ , and, for each $v\in V$ $B_{v}$ and $c_{v}:B_{v}\longrightarrow F\backslash\{0\}$ are as in Th. 5.19 (we now write $c_{v}$ instead of c to underline the dependence of c on $\upsilon$ then the map.  

$$
A:V\longrightarrow W,\quad A(v)=A\left(\sum_{b\in B_{v}}c_{v}(b)b\right):=\sum_{b\in B_{v}}c_{v}(b)w_{b},
$$  

is linear, and $\tilde{A}\in\mathcal{L}(V,W)$ with  

$$
\underset{b\in B}{\forall}\quad\tilde{A}(b)=w_{b},
$$  

implies $A={\tilde{A}}$  

Proof. We first verify $A$ is linear. Let $v\in V$ and $\lambda\in F$ . If $\lambda=0$ , then $A(\lambda v)=A(0)=$ $0=\lambda A(v)$ . If $\lambda\neq0$ , then $B_{\lambda v}=B_{v},c_{\lambda v}=\lambda c_{v}$ , and  

$$
A(\lambda v)=A\left(\sum_{b\in B_{\lambda v}}c_{\lambda v}(b)b\right)=\sum_{b\in B_{v}}\lambda c_{v}(b)w_{b}=\lambda A\left(\sum_{b\in B_{v}}c_{v}(b)b\right)=\lambda A(v).
$$  

Now let. $u,v\in V$ .If $u~=~0$ , then. $A(u+v)=A(v)=0+A(v)=A(u)+A(v)$ and analogously if $v~=~0$ .So assume $u,v\ne0$ .If $u+v=0$ , then. $\textit{v}=-\mathcal{u}$ and $A(u+v)=A(0)=0=A(u)+A(-u)=A(u)+A(v)$ . If $u+v\ne0$ , then $B_{u+v}\subseteq B_{u}\cup B_{v}$ and  

$$
\begin{array}{l}{{\displaystyle{\cal A}(u+v)={\cal A}\left(\sum_{b\in{\cal B}_{u+v}}c_{u+v}(b)b\right)=\sum_{b\in{\cal B}_{u+v}}c_{u+v}(b)w_{b}}}\ {{\displaystyle~=\sum_{b\in{\cal B}_{u}}c_{u}(b)w_{b}+\sum_{b\in{\cal B}_{v}}c_{v}(b)w_{b}={\cal A}(u)+{\cal A}(v)}.}\end{array}
$$  

If $v\in V$ and $B_{v}$ and $c_{v}$ are as before, then the linearity of $\tilde{A}$ and (6.5) imply  

$$
\tilde{A}(v)=\tilde{A}\left(\sum_{b\in B_{v}}c_{v}(b)b\right)\tilde{\overset{A}{\rightleftharpoons}}\tilde{\underset{\mathrm{=}}{\ell}}\tilde{\underset{\mathrm{=}}{\ell}}(V,W)\sum_{b\in B_{v}}c_{v}(b)\tilde{A}(b)=\sum_{b\in B_{v}}c_{v}(b)w_{b}=A(v).
$$  

Since (6.7) establishes ${\tilde{A}}=A$ , the proof is complete.  

Example 6.7. (a) Let $V$ and $W$ be finite-dimensional vector spaces over the field $F$ $\dim V=n$ $\dim W=m$ , where $m,n\in\ensuremath{\mathbb{N}}_{0}$ . From Th. 6.6, we obtain a very useful characterization of the linear maps between $V$ and $W$ : If $V=\{0\}$ or $W=\{0\}$ then $A\equiv0$ is the only element of $\mathcal{L}(V,W)$ . Now let $b_{1},\dots,b_{n}\in V$ form a basis of $V$ and let $c_{1},\dots,c_{m}\in W$ form a basis of $W$ . Given $A\in{\mathcal{L}}(V,W)$ , define  

$$
\underset{i\in\{1,\ldots,n\}}{\forall}\quad w_{i}:=A(b_{i}).
$$  

Then, by Th. 5.19, there exists a unique family $\big(a_{j i}\big)_{(j,i)\in\{1,\dots,m\}\times\{1,\dots,n\}}$ in $F^{\prime}$ such that  

$$
\operatorname*{\forall}_{i\in\{1,\ldots,n\}}w_{i}=A(b_{i})=\sum_{j=1}^{m}a_{j i}c_{j}.
$$  

Thus, given $\textstyle v=\sum_{i=1}^{n}\lambda_{i}b_{i}\in V$ $\lambda_{1},\dots,\lambda_{n}\in F$ , we find  

$$
{\begin{array}{r l}&{A(v)=A\left(\displaystyle\sum_{i=1}^{n}\lambda_{i}b_{i}\right)=\displaystyle\sum_{i=1}^{n}\lambda_{i}w_{i}=\displaystyle\sum_{i=1}^{n}\sum_{j=1}^{m}\lambda_{i}a_{j i}c_{j}=\displaystyle\sum_{j=1}^{m}\left(\sum_{i=1}^{n}a_{j i}\lambda_{i}\right)c_{j}}\ &{\qquad=\displaystyle\sum_{j=1}^{m}\mu_{j}c_{j},\quad{\mathrm{where~}}\mu_{j}:=\displaystyle\sum_{i=1}^{n}a_{j i}\lambda_{i}.}\end{array}}
$$  

Thus, from Th. 6.6, we conclude that the map, assigning to each vector $v=$ $\textstyle\sum_{i=1}^{n}\lambda_{i}b_{i}\in V$ the vector $\textstyle\sum_{j=1}^{m}\mu_{j}c_{j}$ with $\textstyle\mu_{j}:=\sum_{i=1}^{n}a_{j i}\lambda_{i}$ is precisely the unique linear map $A:V\longrightarrow W$ , satisfying (6.8).  

(b) Let $V$ be a vector space over the field $F^{\prime}$ , let $B$ be a basis of $V$ . Given $v\in V$ , let $B_{v}$ and $c_{v}:B_{v}\longrightarrow F\setminus\{0\}$ be as in Th. 5.19. For each $c\in B$ , define  

$$
\pi_{c}:V\longrightarrow F,\quad\pi_{c}(v):=\left\{c_{v}(c)\quad{\mathrm{for~}}c\in B_{v},\right.
$$  

calling $\pi_{c}$ the projection onto the coordinate with respect to $c$ .Comparing with (6.4), we see that $\pi_{c}$ is precisely the linear map. $A:V\longrightarrow W:=F$ , determined by the family $(w_{b})_{b\in B}$ in $F^{\prime}$ with  

$$
\begin{array}{r l}{\underset{b\in B}{\forall}}&{{}w_{b}:=\delta_{b c}:=\left\{{1}&{{}\mathrm{for}b=c,}\ {0}&{{}\mathrm{for}b\neq c,}\end{array}\right.}\end{array}
$$  

as this yields  

$$
\underset{\neq V}{\forall}\quad A(v)=A\left(\sum_{b\in B_{v}}c_{v}(b)b\right)=\sum_{b\in B_{v}}c_{v}(b)w_{b}=\sum_{b\in B_{v}}c_{v}(b)\delta_{b c}=\left\{c_{v}(c)\quad{\mathrm{for~}}c\in B_{v}\quad||<1\right\}.
$$  

In particular,. $\pi_{c}$ is linear. Moreover, for each $c\in B$ , we have  

$$
\mathrm{Im}\pi_{c}=F,\quad\mathrm{ker}\pi_{c}=\langle B\setminus\{c\}\rangle,\quad V=\langle c\rangle\oplus\mathrm{ker}\pi_{c}.
$$  

(c) Let $I$ be a nonempty set and let $Y$ be a vector space over the field $F^{\prime}$ .We then know from Ex. 5.2(d) that $V:=\mathcal{F}(I,Y)=Y^{I}$ is a vector space over $F$ . For each $i\in I$ , define.  

$$
\pi_{i}:V\longrightarrow Y,\quad\pi_{i}(f):=f(i),
$$  

calling $\pi_{i}$ the projection onto the $i$ th coordinate (note that, for $I=\{1,\dots,n\}$ $n\in\mathbb N$ $Y=F$ , one has $V=F^{n}$ $\pi_{i}(v_{1},\ldots,v_{n})=v_{i}$ . We verify $\pi_{i}$ to be linear: Let $\lambda\in F$ and $f,g\in V$ . Then  

$$
\begin{array}{c}{{\pi_{i}(\lambda f)=(\lambda f)(i)=\lambda(f(i))=\lambda\pi_{i}(f),}}\ {{\pi_{i}(f+g)=(f+g)(i)=f(i)+g(i)=\pi_{i}(f)+\pi_{i}(g),}}\end{array}
$$  

proving $\pi_{i}$ to be linear. Moreover, for each $i\in I$ , we have  

$$
\mathrm{Im}\pi_{i}=Y,\quad\ker\pi_{i}=\{(f:I\longrightarrow Y):f(i)=0\}\cong Y^{I\backslash\{i\}},\quad V=Y\oplus\ker\pi_{i},
$$  

where, for the last equality, we identified  

$$
Y\cong\{(f:I\longrightarrow Y):f(j)=0\mathrm{for}\mathrm{each}j\neq i\}.
$$  

A generalization of the present example to general Cartesian products of vector spaces can be found in. $\mathrm{Ex}$ . E.4 of the Appendix. To investigate the relation between the present projections and the projections of (b), let $Y=F$ .We know from Ex. $5.16(\mathrm{c})$ that $B=\{e_{i}:i\in I\}$ with  

$$
\begin{array}{r}{\underset{i\in I}{\forall}\quad e_{i}:I\longrightarrow F,\quad e_{i}(j)=\delta_{i j}:=\left\{\begin{array}{l l}{1}&{\mathrm{if~}i=j,}\ {0}&{\mathrm{if~}i\neq j,}\end{array}\right.}\end{array}
$$  

Now, if. is a basis of $\begin{array}{r}{f=\sum_{j=1}^{n}\lambda_{i_{j}}e_{i_{j}}}\end{array}$ $F_{\mathrm{fin}}^{I}$ which is a subspace of with $\lambda_{1},\dots,\lambda_{n}\in F$ $F^{I}$ , such that the $i_{1},\ldots,i_{n}\in I$ $\pi_{i}$ are defined on $n\in\mathbb{N}$ and $\pi_{e_{i_{k}}}$ $F_{\mathrm{fin}}^{I}$ defined as in (b) $\langle k\in\{1,\ldots,n\}\rangle$ , then  

$$
\pi_{i_{k}}(f)=f(i_{k})=\sum_{j=1}^{n}\lambda_{i_{j}}e_{i_{j}}(i_{k})=\sum_{j=1}^{n}\lambda_{i_{j}}\delta_{j k}=\lambda_{i_{k}}=\pi_{e_{i_{k}}}(f),
$$  

showing Tik FIn= Teik  

(d) We consider the set of complex numbers $\mathbb{C}$ as vector space over $\mathbb{R}$ with basis $\{1,i\}$ Then the map of complex conjugation  

$$
A:\mathbb{C}\longrightarrow\mathbb{C},\quad A(z)=A(x+i y)=\bar{z}=x-i y,
$$  

is $\mathbb{R}$ -linear, since, for each $z=x+i y,w=u+i v\in\mathbb{C}$  

$$
\begin{array}{r}{\overline{{z+w}}=x+u-i y-i v=\overline{{z}}+\overline{{w}}\quad\wedge\quad\overline{{z w}}=x u-y v-(x v+y u)i=(x-i y)(u-i v)=}\end{array}
$$  

and $z=z$ for $z\in\mathbb{R}$ . As $A$ is bijective with $A=A^{-1}$ $A$ is even an automorphism. However, complex conjugation is not $\mathbb{C}$ -linear (now considering $\mathbb{C}$ as a vector space over itself), since, e.g., $\overline{{i\cdot1}}=-i\neq i\cdot\bar{1}=i$  

(e) By using results from Calculus, we obtain the following examples:  

(i) Let $V$ be the set of convergent sequences in. $\mathbb{K}$ .According to [Phi16, Th. $7.13(\mathrm{a})]$ , scalar multiples of convergent sequences are convergent and sums of convergent sequences are convergent, showing. $V$ to be a subspace of ${\mathbb K}^{\mathbb N}$ , the vector space over $\mathbb{K}$ of all sequences in $\mathbb{K}$ . If $(z_{n})_{n\in\mathbb{N}}$ and $(w_{n})_{n\in\mathbb{N}}$ are elements of $V$ and $\lambda\in\mathbb{K}$ , then, using [Phi16, Th. 7.13(a)] once again, we know.  

$$
\operatorname*{lim}_{n\to\infty}(\lambda z_{n})=\lambda\operatorname*{lim}_{n\to\infty}z_{n},\quad\operatorname*{lim}_{n\to\infty}(z_{n}+w_{n})=\operatorname*{lim}_{n\to\infty}z_{n}+\operatorname*{lim}_{n\to\infty}w_{n},
$$  

showing the map  

$$
A:V\longrightarrow\mathbb{K},\quad A(z_{n})_{n\in\mathbb{N}}:=\operatorname*{lim}_{n\rightarrow\infty}z_{n},
$$  

to be linear. Moreover, we have  

$$
\operatorname{Im}A=\mathbb{K},\quad\ker A=\{(z_{n})_{n\in\mathbb{N}}\in V:\operatorname*{lim}_{n\to\infty}z_{n}=0\},\quad V=\langle(1)_{n\in\mathbb{N}}\rangle\oplus\ker A,
$$  

where the last equality is due to the fact that, if $(z_{n})_{n\in\mathbb{N}}\in V$ with $\scriptstyle\operatorname*{lim}_{n\to\infty}z_{n}=$ $\lambda$ , then $\begin{array}{r}{\operatorname*{lim}_{n\to\infty}(z_{n}-\lambda\cdot1)=0}\end{array}$ , i.e. $(z_{n})_{n\in\mathbb{N}}-\lambda(1)_{n\in\mathbb{N}}\in\ker A$  

(ii) Let $a,b\in\mathbb{R}$ $a<b$ $I:=\rfloor a,b\lfloor$ , and let $V:\{(f:I\longrightarrow\mathbb{K}):f$ is differentiable $\}$ According to [Phi16, Th. 9.7], scalar multiples of differentiable functions are differentiable and sums of differentiable functions are differentiable, showing $V$ to be a subspace of $\mathbb{K}^{I}$ , the vector space over $\mathbb{K}$ of all functions from $I$ into $\mathbb{K}$ . Using [Phi16, Th. 9.7] again, we know the map  

$$
\begin{array}{r}{A:V\longrightarrow\mathbb{K}^{I},\quad A(f):=f^{\prime},}\end{array}
$$  

to be linear. While ker. $A=\{f\in V:f$ constant} (e.g. due to the fundamental theorem of calculus in the form [Phi16, Th. 10.20(b)]), $\operatorname{Im}A$ is not so simple to characterize (cf. [Phi17, Th. 2.11]).  

(iii) Let $a,b\in\mathbb{R}$ $a\leq b$ $I:=[a,b]$ , and let $W:=\mathcal{R}(I,\mathbb{K})$ be the set of all $\mathbb{K}$ -valued Riemann integrable functions on. $I$ . According to [Phi16, Th. 10.11(a)], scalar multiples of Riemann integrable functions are Riemann integrable and sums of Riemann integrable functions are Riemann integrable, showing $W$ to be another subspace of $\mathbb{K}^{I}$ . Using [Phi16, Th. 10.11(a)] again, we know the map.  

$$
B:W\longrightarrow\mathbb{K},\quad B(f):=\int_{I}f,
$$  

to be linear. Moreover, for $a<b$ , we have  

$$
\mathrm{Im}B=\mathbb{K},\quad\ker B=\left\{f\in W:\int_{I}f=0\right\},\quad W=\left\langle1\right\rangle\oplus\ker B,
$$  

where the last equality is due to the fact that, if $f\in W$ with $\textstyle{\int_{I}f=\lambda}$ , then $\begin{array}{r}{\int_{I}(f-\frac{\lambda}{b-a}\cdot1)=0}\end{array}$ , i.e. $\begin{array}{r}{f-\frac{\lambda}{b-a}\cdot1\in\ker B}\end{array}$  

For some of the linear maps investigated in Ex. 6.7 above, we have provided the respective kernels, images, and direct complements of the kernels. The examples suggest relations between the dimensions of domain, image, and kernel of a linear map, which are stated an proved in the following theorem:  

Theorem 6.8 (Dimension Formulas). Let $V$ and $W$ be vector spaces over the field $F^{\prime}$ and let $A:V\longrightarrow W$ be linear. Moreover, let $B_{V}$ be a basis of $V$ , let $B_{\mathrm{ker}}$ be a basis of $\ker A$ , let $B_{\mathrm{Im}}$ be a basis of $\operatorname{Im}A$ , and let $B_{W}$ be a basis of $W$  

(a) If $U$ is a direct complement of ker $A$ (i.e. if $V=U\oplus\ker A,$ ), then $A{\upharpoonright_{U}}$ .. $U\longrightarrow\operatorname{Im}A$ is bijective.In consequence, $\dim V=\dim\ker A+\dim\operatorname{Im}A$ ,i.e. there exists $a$ bijective map $\phi:B_{V}\longrightarrow(B_{\mathrm{ker}}\times\{0\})\dot{\cup}(B_{\mathrm{Im}}\times\{1\})$  

(b) $\dim\operatorname{Im}A\leq\dim V$ , i.e. there exists an injective map from $B_{\mathrm{Im}}$ into $B_{V}$ (c) $\dim\operatorname{Im}A\leq\dim W$ , i.e. there exists an injective map from $B_{\mathrm{Im}}$ into $B_{W}$  

Proof. (a): If $u\in\ker A\mid_{U}$ , then $u\in U\cap\ker A$ , i.e. $u~=~0$ , i.e. $\textit{A}\left\lceil\boldsymbol{U}\right\rceil$ is injective. If $w\in\operatorname{Im}A$ and $A v=w$ , then $\boldsymbol{v}~=~\boldsymbol{v}_{0}+\boldsymbol{u}$ with $v_{0}\in\ker A$ and $u\in U$ . Then $A u=A(v)-A(v_{0})=w-0=w$ , showing $A{\upharpoonright_{U}}$ is surjective. According to Th. 5.30(b),. if $B_{U}$ is a basis of $U$ , then $B:=B_{\mathrm{ker}}\cup B_{U}$ is a basis of $V$ . Moreover, by Prop. 6.5(c), $A(B_{U})$ is a basis of $\operatorname{Im}A$ . Thus, by Th. 5.23(c), it suffices to show there exists a bijective map $\psi:B\longrightarrow(B_{\mathrm{ker}}\times\{0\})\dot{\cup}(A(B_{U})\times\{1\})$ . If we define  

$$
\psi:B\longrightarrow(B_{\mathrm{ker}}\times\{0\})\dot{\cup}(A(B_{U})\times\{1\}),\quad\psi(b):=\left\{\begin{array}{l l}{{(b,0)}}&{{\mathrm{for~}b\in B_{\mathrm{ker}},}}\ {{(A(b),1)}}&{{\mathrm{for~}b\in B_{U},}}\end{array}\right.
$$  

then $\psi$ is bijective due to the bijectivity of $A{\upharpoonright_{U}}$ (b) is immediate from (a).  

(c) is due to Th. 5.27(b), since $\operatorname{Im}A$ is a subspace of $W$  

The following theorem is one of the central results of Linear Algebra: It says that vector spaces are essentially determined by the size of their bases:  

Theorem 6.9. Let $V$ and $W$ be vector spaces over the field $F^{\prime}$ . Then $V\cong W$ (i.e. $V$ and $W$ are isomorphic) if, and only if, $\dim V=\dim W$  

Proof. Suppose $\dim V=\dim W$ . If $B_{V}$ is a basis of $V$ and $B_{W}$ is a basis of $W$ , then there exists a bijective map $\phi:B_{V}\longrightarrow B_{W}$ . According to Th. 6.6, $\phi$ defines a unique linear map $A:V\longrightarrow W$ with $A(b)=\phi(b)$ for each $b\in B_{V}$ .More precisely, letting, once again, for each $v\in V$ $B_{v}$ and $c_{v}:B_{v}\longrightarrow F\setminus\{0\}$ be as in Th. 5.19 (writing $c_{v}$ instead of $c$ to underline the dependence of $c$ on $\upsilon$  

$$
\forall_{v\in V}A(v)=A\left(\sum_{b\in B_{v}}c_{v}(b)b\right)=\sum_{b\in B_{v}}c_{v}(b)\phi(b).
$$  

It remains to show $A$ is bijective. If $v\neq0$ , then $B_{v}\neq\emptyset$ and $\begin{array}{r}{A(v)=\sum_{b\in B_{v}}c_{v}(b)\phi(b)\neq0}\end{array}$ since $c_{v}(b)\neq0$ and $\{\phi(b):b\in B_{v}\}\subseteq B_{W}$ is linearly independent, showing $A$ is injective by Prop. 6.3(d). If $w\in W$ , then there exists a finite set. ${\tilde{B}}_{w}\subseteq B_{W}$ and $\tilde{c}_{w}:\tilde{B}_{w}\longrightarrow F\setminus\{0\}$ such thate $\begin{array}{r}{w=\sum_{\tilde{b}\in\tilde{B}_{w}}\tilde{c}_{w}(\tilde{b})\tilde{b}}\end{array}$ . Then  

$$
\begin{array}{r l r}{\left(\displaystyle\sum_{\tilde{b}\in\tilde{B}_{w}}\tilde{c}_{w}(\tilde{b})\phi^{-1}(\tilde{b})\right)}&{{}\overset{A\in\mathcal{L}(V,W)}{=}}&{\displaystyle\sum_{\tilde{b}\in\tilde{B}_{w}}\tilde{c}_{w}(\tilde{b})A\left(\phi^{-1}(\tilde{b})\right)\overset{\phi^{-1}(\tilde{b})\in B_{V}}{=}\displaystyle\sum_{\tilde{b}\in\tilde{B}_{w}}\tilde{c}_{w}(\tilde{b})\phi\left(\phi^{-1}(\tilde{b})\right)}\ {=}&{{}}&{\displaystyle\sum_{\tilde{b}\in\tilde{B}_{w}}\tilde{c}_{w}(\tilde{b})\tilde{b}=w,}\end{array}
$$  

showing $\operatorname{Im}A=W$ , completing the proof that $A$ is bijective.  

If $A:V\longrightarrow W$ is a linear isomorphism and $B$ is a basis for $V$ , then, by Prop. 6.5(c), $A(B)$ is a basis for $W$ . As $A$ is bijective, so is $A{\upharpoonright_{B}}$ , showing $\dim V=\#B=\#A(B)=$ $\dim W$ as claimed.  

Theorem 6.10. Let $V$ and $W$ be finite-dimensional vector spaces over the field $F^{\prime}$ $\dim V=\dim W=n\in\mathbb{N}_{0}$ .Then, given $A\in{\mathcal{L}}(V,W)$ , the following three statements are equivalent:  

(i) A is an isomorphism.  

(ii) A is an epimorphism.  

(iii) A is a monomorphism.  

Proof. If suffices to prove the equivalence between (ii) and (iii)  

"(ii) $\Rightarrow$ (iii): If $A$ is an epimorphism, then $W=\operatorname{Im}A$ , implying.  

$$
\operatorname*{lim}\ker A^{\dim V}\stackrel{<\infty,\mathrm{{Th.6.8(a)}}}{=}\dim V-\dim\mathrm{{Im}}A=\dim V-\dim W=n-n=0,
$$  

showing $\ker A=\{0\}$ , i.e. $A$ is a monomorphism.  

"(iii)=>(ii)": If $A$ is a monomorphism, then $\ker A=\{0\}$ .Thus, by Th. 6.8(a), $n=$ $\dim W=\dim V=\dim\ker A+\dim\mathrm{Im}A=0+\dim\mathrm{Im}A=\dim\mathrm{Im}A$ . From Th. 5.27(d), we then obtain. $W=\operatorname{Im}A$ , i.e.. $A$ is an epimorphism. $\vert$  

Example 6.11. The present example shows that the analogue of Th. 6.10 does not hold for infinite-dimensional vector spaces: Let $F^{\prime}$ be a field and $V:=F^{\mathbb{N}}$ (the vector space of sequences in $F\mathrm{~-~t~}$ he example actually still works in precisely the same way over the. simpler space $F_{\mathrm{fin}}^{\mathbb{N}}$ ). Define the maps  

$$
\begin{array}{r l}{R:V\longrightarrow V,}&{R(\lambda_{1},\lambda_{2},\ldots,):=(0,\lambda_{1},\lambda_{2},\ldots,),}\ {L:V\longrightarrow V,}&{L(\lambda_{1},\lambda_{2},\ldots,):=(\lambda_{2},\lambda_{3},\ldots)}\end{array}
$$  

$R$ is called the right shift operator,. $L$ is called the left shift operator). Clearly, $R$ and $L$ are linear and.  

$$
L\circ R=\operatorname{Id},
$$  

i.e. $L$ is a left inverse for $R$ $R$ is a right inverse for $L$ .Thus, according to Th. 2.13, $R$ is injective and $L$ is surjective (which is also easily seen directly from the respective definitions of. $R$ and $L$ ). However,.  

$$
{\begin{array}{r l r}&{\operatorname{n}R=\left\{(f:\mathbb{N}\longrightarrow F):f(1)=0\right\}\neq V}&{{\mathrm{(e.g.~}}(1,0,0,\ldots,)\not\in\operatorname{Im}R{\mathrm{)}}}\ &{\operatorname{x}L=\left\{(f:\mathbb{N}\longrightarrow F):f(k)=0{\mathrm{~for~}}k\neq1\right\}\neq\{0\}}&{{\mathrm{(e.g.~}}0\neq(1,0,0,\ldots,)\in\Bbbk\circ(\Bbbk),}\end{array}}
$$  

showing. $R$ is not surjective, $L$ is not injective.  

### 6.2 Quotient Spaces  

In Def. 4.26, we defined the quotient group $G/N$ of a group. $G$ with respect to a normal subgroup $N$ . Now, if. $V$ is a vector space over a field $F^{\prime}$ , then, in particular, $(V,+)$ is a commutative group. Thus, every subgroup of $V$ is normal. Thus, if $U$ is a subspace of  

$V$ , then we can always form the quotient group $V/U$ .We will see below that we can even make $V/U$ into a vector space over $F^{\prime}$ , called the quotient space or factor space of $V$ with respect to $U$ . As we write $(V,+)$ as an additive group, we write the respective cosets (i.e. the elements of $V/U$ ) as $v+U$ $v\in V$  

Theorem 6.12. Let $V$ be a vector space over the field $F^{\prime}$ and let $U$ be a subspace of $V$  

(a) The compositions  

$$
\begin{array}{r l r}&{+:V/U\times V/U\longrightarrow V/U,\qquad}&{(v+U)+(w+U):=v+w+U,}\ &{\mathrm{\boldmath~\sigma~}\cdot:F\times V/U\longrightarrow V/U,\qquad}&{\lambda\cdot(v+U):=\lambda v+U,}\end{array}
$$  

are well-defined, i.e. the results do not depend on the chosen representatives of the respective cosets.  

(b) The natural (group) epimorphism of Th. 4.27(a),  

$$
\phi_{U}:V\longrightarrow V/U,\quad\phi_{U}(v):=v+U,
$$  

satisfies  

$$
\begin{array}{r l}&{\underset{v,w\in V}{\forall}\quad\phi_{U}(v+w)=\phi_{U}(v)+\phi_{U}(w),}\ &{\underset{\lambda\in F}{\forall}\quad\underset{v\in V}{\forall}\quad\phi_{U}(\lambda v)=\lambda\phi_{U}(v).}\end{array}
$$  

(c) $V/U$ with the compositions of (a) forms a vector space over $F$ and $\phi_{U}$ of (b) constitutes a linear epimorphism.  

Proof. (a): The composition $^+$ is well-defined by Th. 4.27(a). To verify that . is welldefined as well, let $v,w\in V$ $\lambda\in F$ , and assume. $v+U=w+U$ .We need to show $\lambda v+U=\lambda w+U$ . If $x\in\lambda v+U$ , then there exists $u_{1}\in U$ such that $x=\lambda v+u_{1}$ . Since $v+U=w+U$ , there then exists. $u_{2}\in U$ such that $v+u_{1}=w+u_{2}$ and $v=w+u_{2}-u_{1}$ Thus, $x=\lambda v+u_{1}=\lambda w+\lambda(u_{2}-u_{1})+u_{1}$ . Since $U$ is a subspace of. $V$ $\lambda(u_{2}-u_{1})+u_{1}\in U$ showing $x\in\lambda w+U$ and $\lambda v+U\subseteq\lambda w+U$ . As we can switch the roles of $\upsilon$ and $w$ in the above argument, we also have $\lambda w+U\subseteq\lambda v+U$ and $\lambda v+U=\lambda w+U$ , as desired.  

(b): (6.23a) holds, as $\phi_{U}$ is a homomorphism with respect to $^+$ by Th. 4.27(a). To verify (6.23b), let $\lambda\in F$ $v\in V$ . Then  

$$
\phi_{U}(\lambda v)=\lambda v+U\stackrel{\mathrm{\tiny~(6.21b)}}{=}\lambda(v+U)=\lambda\phi_{U}(v),
$$  

establishing the case.  

(c) is now immediate from (b) and Prop. 6.4.  

One can sometimes obtain information about a vector space $V$ by studying a subspace $U$ and the corresponding quotient space. $V/U$ , both of which are "smaller' spaces in the. sense of the following Cor. 6.13:.  

Corollary 6.13. Let $V$ be a vector space over the field. $F$ and let $U$ be a subspace of. $V$   
Let $\phi:V\longrightarrow V/U$ $\phi(v):=v+U$ , denote the natural epimorphism.  

(a) If $B$ is a basis of $V$ and $B_{U}\subseteq B$ is a basis of $U$ , then $B_{/}:=\{b+U:b\in B\backslash B_{U}\}$ is a basis of $V/U$  

(b) Let $B_{U}$ be a basis of $U$ and let $W$ be another subspace of $V$ with basis $B_{W}$ .If $\phi\lceil_{W}:W\longrightarrow V/U$ is bijective, then $B_{U}\dot{\cup}B_{W}$ forms a basis of $V$  

(c) $\dim V=\dim U+\dim V/U$ (cf. Th. 6.8(a)).  

Proof. (a): Letting $W:=\langle B\backslash B_{U}\rangle$ , we have $V=U\oplus W$ by Th. 5.30(d). Since $U=\ker\phi$ we have $V=\ker\phi\oplus W$ and $\phi\mid_{W}$ .. $W\longrightarrow V/U$ is bijective by Th. 6.8(a) and, thus, $B_{/}=\phi{\mid}_{W}\left(B\setminus B_{U}\right)$ is a basis of $V/U$  

(b): Let $v\in V$ . Then there exists $w\in W$ with $v+U=\phi(v)=\phi(w)=w+U$ , implying $v-w\in U$ . Thus, $v=w+v-w\in W+U$ , showing $V=W+U$ . On the other hand, if $v\in U\cap W$ , then $\phi(v)=v+U=U=\phi(0)$ and, thus, $v=0$ , showing $V=W\oplus U$ Then $B_{U}\cup B_{W}$ forms a basis of $V$ by Th. 5.30(b).  

(c): Since $U=\ker\phi$ and $V/U=\operatorname{Im}\phi$ , (c) is immediate from Th. 6.8(a).  

From Def. 4.26 and Th. 4.27(a), we already know that the elements of $V/U$ are precisely the equivalence classes of the equivalence relation defined by  

$$
\begin{array}{r}{\underset{v,w\in V}{\forall}\quad\Big(v\sim w\quad:\Leftrightarrow\quad v+U=w+U\quad\Leftrightarrow\quad v-w\in U\Big).}\end{array}
$$  

Here, in the context of vector spaces, it turns out that the equivalence relations on $V$ that define quotient spaces, are precisely so-called linear equivalence relations:  

Definition 6.14. Let $V$ be a vector space over the field $F^{\prime}$ and let $R\subseteq V\times V$ be a relation on $V$ . Then $R$ is called linear if, and only if, it has the following two properties:  

(i) If $v,w,x,y\in V$ with $v R w$ and $x R y$ , then $(v+x)R(w+y)$  

(ii) If $v,w\in V$ and $\lambda\in F$ with $v R w$ , then $(\lambda v)R(\lambda w)$  

Proposition 6.15. Let. $V$ be a vector space over the field $F^{\prime}$ (a) If $U$ is a subspace of $V$ , then the equivalence relation defined by (6.24) is linear.  

(b) Let $\sim$ be a linear equivalence relation on $V$ .Then $U:=\{v\in V:v\sim0\}$ is a subspace of $V$ and $\sim$ satisfies (6.24).  

Proof. (a): The linearity of $\sim$ defined by (6.24) is precisely the assertion that the compositions $^+$ and : of Th. 6.12(a) are well-defined.  

(b): We have $0\in U$ , as $\sim$ is reflexive. If $v,w\in U$ and $\lambda\in F$ , then the linearity of $\sim$ implies $v+w\sim0+0=0$ and $\lambda v\sim\lambda0=0$ , i.e. $v+w\in U$ and $\lambda v\in U$ , showing $U$ to be a subspace. Now suppose $v,w\in V$ with $v\sim w$ . Then the linearity of $\sim$ yields $v-w\sim0$ i.e. $v-w\in U$ . If $x=v+u$ with $u\in U$ , then $x=w+(x-w)=w+(v+u-w)\in w+U$ showing $v+U\subseteq w+U$ .As $\sim$ is symmetric, we then have $w+U\subseteq v+U$ as well. Conversely, if $v,w\in V$ with $v+U=w+U$ , then $v-w\in U$ , i.e. $v-w\sim0$ and the linearity of $\sim$ implies $v\sim w$ , proving $\sim$ satisfies (6.24).  

In Th. 4.27(b), we proved the isomorphism theorem for groups: If $G$ and $H$ are groups and $\phi:G\longrightarrow H$ is a homomorphism, then. $G/\ker\phi\cong\operatorname{Im}\phi$ . Since vector spaces. $V$ and $W$ are, in particular, groups, if. $A:V\longrightarrow W$ is linear, then. $V/\ker A\cong\operatorname{Im}A$ as groups, and it is natural to ask, whether $V/\ker A$ and $\operatorname{Im}A$ are isomorphic as vector spaces. In Th. 6.16(a) below we see this, indeed, to be the case.  

Theorem 6.16 (Isomorphism Theorem). Let $V$ and $X$ be vector spaces over the field $F^{\prime}$ , let $U,W$ be subspaces of $V$  

(a) If $A:V\longrightarrow X$ is linear, then  

$$
V/\ker A\cong\operatorname{Im}A.
$$  

More precisely, the map  

$$
f:V/\ker A\longrightarrow\operatorname{Im}A,\quad f(v+\ker A):=A(v),
$$  

is well-defined and constitutes an linear isomorphism. If $f_{\mathrm{e}}:V\longrightarrow V/\ker A$ denotes the natural epimorphism and $\iota:\operatorname{Im}A\longrightarrow X$ $\iota(v):=v$ , denotes the embedding, then $f_{\mathrm{m}}:V/\ker A\longrightarrow X$ $f_{\mathrm{m}}:=\iota\circ f$ , is a linear monomorphism such that  

$$
A=f_{\mathrm{m}}\circ f_{\mathrm{e}}.
$$  

(b) One has  

$$
(U+W)/W\cong U/(U\cap W).
$$  

(c) If $U$ is a subspace of $W$ , then.  

$$
(V/U)/(W/U)\cong V/W.
$$  

Proof. (a): All assertions, except the linearity assertions, were already proved in Th. 4.27(b). Moreover, $f_{\mathrm{e}}$ is linear by Th. 6.12(b). Thus, it merely remains to show  

$$
f\bigl(\lambda(v+\ker A)\bigr)=\lambda f(v+\ker A)
$$  

for each $\lambda\in F$ and each $v\in V$ (then $f_{\mathrm{m}}$ is linear, as both $f$ and $\iota$ are linear). Indeed, if $\lambda\in F$ and $v\in V$ , then  

$$
f{\bigl(}\lambda(v+\ker A){\bigr)}=f(\lambda v+\ker A)=A(\lambda v)=\lambda A(v)=\lambda f(v+\ker A),
$$  

as desired.  

(b): According to (a), it suffices to show that  

$$
A:U+W\longrightarrow U/(U\cap W),\quad A(u+w):=u+(U\cap W)\quad{\mathrm{for~}}u\in U,w\in W
$$  

well-defines a linear map with $\ker A=W$ . To verify that $A$ is well-defined, let $u,u_{1}\in U$ and $w,w_{1}\in W$ with $u+w=u_{1}+w_{1}$ . Thens $u-u_{1}=w_{1}-w\in U\cap W$ and, thus,.  

$$
4(u+w)=u+(U\cap W)=u_{1}+w_{1}-w+(U\cap W)=u_{1}+(U\cap W)=A(u_{1}+w)=u_{1}+(U\cap W)=u_{2}.
$$  

proving $A$ to be well-defined by (6.30). To prove linearity, we no longer assume $u+w=$ $u_{1}+w_{1}$ and calculate  

$$
\begin{array}{r l}&{A\big((u+w)+(u_{1}+w_{1})\big)=A\big((u+u_{1})+(w+w_{1})\big)=u+u_{1}+(U\cap W)}\ &{\qquad=\big(u+(U\cap W)\big)+\big(u_{1}+(U\cap W)\big)}\ &{\qquad=A(u+w)+A(u_{1}+w_{1}),}\end{array}
$$  

as well as, for each $\lambda\in F$  

$$
\begin{array}{r}{\mathrm{l}\big(\lambda(u+w)\big)=A(\lambda u+\lambda w)=\lambda u+(U\cap W)=\lambda\big(u+(U\cap W)\big)=\lambda A(u+w),}\end{array}
$$  

as needed. If $w\in W$ , then $A(w)=A(0+w)=U\cap W$ , showing $w\in\ker A$ and $W\subseteq\ker A$ Conversely, let $u+w\in\ker A$ $u\in U$ $w\in W$ . Then $A(u+w)=u+(U\cap W)=U\cap W$ i.e. $u\in U\cap W$ and $u+w\in W$ , showing $\ker A\subseteq W$  

(c): Exercise.  

### 6.3 Vector Spaces of Linear Maps  

Definition 6.17. Let $V$ and $W$ be vector spaces over the field $F^{\prime}$ . We define an addition and a scalar multiplication on $\mathcal{L}(V,W)$ by  

$$
\begin{array}{r l}{(A+B):V\longrightarrow W,\qquad}&{(A+B)(x):=A(x)+B(x),}\ {(\lambda\cdot A):V\longrightarrow W,\qquad}&{(\lambda\cdot A)(x):=\lambda\cdot A(x)\quad\mathrm{for~each~}\lambda\in F.}\end{array}
$$  

Theorem 6.18. Let $V$ and $W$ be vector spaces over the field $F^{\prime}$ . The addition and scalar multiplication on $\mathcal{L}(V,W)$ given by (6.31) are well-defined in the sense that, if $A,B\in{\mathcal{L}}(V,W)$ and $\lambda\in F$ , then. $A+B\in{\mathcal{L}}(V,W)$ and $\lambda A\in\mathcal{L}(V,W)$ . Moreover, with the operations defined in (6.31), $\mathcal{L}(V,W)$ forms a vector space over $F^{\prime}$  

Proof. Exercise.  

Theorem 6.19. Let $V$ and $W$ be vector spaces over the field. $F$ , let $B_{V}$ and $B_{W}$ be bases of $V$ and $W$ , respectively. Using Th. 6.6, define maps $A_{v w}\in\mathcal{L}(V,W)$ by letting  

$$
\begin{array}{r}{\forall}\ {\forall\quad\quad\quad\quad\quad\quad\quad\quad\boldsymbol{w},v\tilde{v}\in{\boldsymbol B_{W}}\times{\boldsymbol B_{V}}\times{\boldsymbol B_{V}}}\end{array}\quad\boldsymbol{A_{v w}}(\tilde{v}):=\left\{\begin{array}{c c}{w}&{f o r v=\tilde{v},}\ {0}&{f o r v\neq\tilde{v}.}\end{array}\right.
$$  

efine  

$$
\begin{array}{r}{\mathinner{|{B:=\left\{A_{v w}:(v,w)\in B_{V}\times B_{W}}\right\}}.}\end{array}
$$  

(a) $\boldsymbol{\mathcal{B}}$ is linearly independent.  

(b) If $V$ is finite-dimensional, $\dim V=n\in\mathbb{N}$ $B_{V}=\{v_{1},\ldots,v_{n}\}$ , then $\boldsymbol{\mathcal{B}}$ constitutes $a$ basis for $\mathcal{L}(V,W)$ . If, in addition, $\dim W=m\in\mathbb{N}$ $B_{W}=\{w_{1},\dots,w_{m}\}$ , then we can write  

$$
\dim{\mathcal{L}}(V,W)=\dim V\cdot\dim W=n\cdot m.
$$  

(c) If $\operatorname{dim}V=\infty$ and $\dim W\geq1$ , then $\langle B\rangle\subsetneq\mathcal{L}(V,W)$ and, in particular, $\boldsymbol{\mathcal{B}}$ is not $a$ basis of $\mathcal{L}(V,W)$  

Proof. (a): Let. $N,M\in\mathbb{N}$ . Let $v_{1},\dots,v_{N}\in B_{V}$ be distinct and let $w_{1},\dotsc,w_{M}\in B_{W}$ be distinct as well. If $\lambda_{j i}\in F$ $(j,i)\in\{1,\dots,M\}\times\{1,\dots,N\}$ , are such that.  

$$
A:=\sum_{j=1}^{M}\sum_{i=1}^{N}\lambda_{j i}A_{v_{i}w_{j}}=0,
$$  

then, for each $k\in\{1,\ldots,N\}$  

$$
0=A(v_{k})=\sum_{j=1}^{M}\sum_{i=1}^{N}\lambda_{j i}A_{v_{i}w_{j}}(v_{k})=\sum_{j=1}^{M}\sum_{i=1}^{N}\lambda_{j i}\delta_{i k}w_{j}=\sum_{j=1}^{M}\lambda_{j k}w_{j}
$$  

implies $\lambda_{1k}=\dots=\lambda_{M k}=0$ due to the linear independence of the. $w_{j}$ . As this holds for. each $k\in\{1,\ldots,N\}$ , we have established the linear independence of $\boldsymbol{\mathcal{B}}$  

(b): According to (a), it remains to show $\langle\boldsymbol{B}\rangle~=~\mathcal{L}(V,W)$ .Let $A\in{\mathcal{L}}(V,W)$ and $i\in\{1,\ldots,n\}$ . Then there exists a finite set $B_{i}\subseteq B_{W}$ such that $\begin{array}{r}{A v_{i}=\sum_{w\in B_{i}}\lambda_{w}w}\end{array}$ with  

$\lambda_{w}\in F$ . Now let $w_{1},\dots,w_{M}$ $M\in\mathbb{N}$ , be an enumeration of the finite set $B_{1}\cup\cdots\cup B_{n}$ Then there exist $a_{j i}\in F$ $(j,i)\in\{1,\ldots,M\}\times\{1,\ldots,n\}$ , such that  

$$
\underset{i\in\{1,\ldots,n\}}{\forall}A(v_{i})=\sum_{j=1}^{M}a_{j i}w_{j}.
$$  

Letting $\begin{array}{r}{L:=\sum_{j=1}^{M}\sum_{i=1}^{n}a_{j i}A_{v_{i}w_{j}}}\end{array}$ , we claim $A=L$ . Indeed,  

$$
\begin{array}{r l}{\underset{\substack{\mathrm{\tiny~\backslash~}\mathrm{\tiny~\in\left\{1,\dots,}~}n\right\}}{\forall}}&{{}L(v_{k})=\displaystyle{\sum_{j=1}^{M}}\sum_{i=1}^{n}a_{j i}A_{v_{i}w_{j}}(v_{k})=\displaystyle{\sum_{j=1}^{M}}\sum_{i=1}^{n}a_{j i}\delta_{i k}w_{j}=\sum_{j=1}^{M}a_{j k}w_{j}=A(v_{k}),}\end{array}
$$  

proving $L=A$ by Th. 6.6. Since. $L\in\langle B\rangle$ , the proof of (b) is complete.  

(c): As $\dim W\geq1$ , there exists $w\in B_{W}$ . If $A\in\langle B\rangle$ , then $\{v\in B_{V}:A v\neq0\}$ is finite. Thus, if $B_{V}$ is infinite, then the map $A\in{\mathcal{L}}(V,W)$ with $A(v):=w$ for each $v\in B_{V}$ is not in $\langle B\rangle$ , proving (c).  

Lemma 6.20. Let $V,W,X$ be vector spaces over the field $F$ .Recalling Not. 6.2, we have:  

(a) If $A\in{\mathcal{L}}(W,X)$ and $B,C\in{\mathcal{L}}(V,W)$ , then  

$$
A(B+C)=A B+A C.
$$  

(b) If $A,B\in{\mathcal{L}}(W,X)$ and $C\in\mathcal{L}(V,W)$ , then  

$$
(A+B)C=A C+B C.
$$  

Proof. (a): For each $v\in V$ , we calculate  

$$
{\stackrel{\prime}{A}}(B+C)\Bigl)v=A(B v+C v)=A(B v)+A(C v)=(A B)v+(A C)v=(A B+A C)v
$$  

proving (6.35).  

(b): For each $v\in V$ , we calculate  

$$
(A+B)C)v=(A+B)(C v)=A(C v)+B(C v)=(A C)v+(B C)v=(A C+B
$$  

proving (6.36).  

Theorem 6.21. Let $V$ be a vector space over the field $F^{\prime}$ .Then $R:=\mathcal{L}(V,V)$ constitutes a ring with unity with respect to pointwise addition and map composition as multiplication. If $\dim V>1$ , then $R$ is not commutative and it has nontrivial divisors of $0$  

Proof. Since $(V,+)$ is a commutative group, $R$ is a subring (with unity Id $\in\textit{R}$ ) of the ring with unity of group endomorphisms. $\operatorname{End}(V)$ of Ex. 4.42(b) (that $R$ constitutes a ring can, alternatively, also be obtained from Lem. 6.20 with $V=W=X$ ). Now let $v_{1},v_{2}\in V$ be linearly independent and. $B$ a basis of $V$ with $v_{1},v_{2}\in B$ . Define $A_{1},A_{2}\in R$ by letting, for $v\in B$  

$$
A_{1}v:=\left\{v_{2}\quad\mathrm{for~}v=v_{1},\quad\quad A_{2}v:=\left\{v_{1}\quad\mathrm{for~}v=v_{2},\right.\quad}
$$  

Then $A_{1}A_{2}v_{1}=0$ , but $A_{2}A_{1}v_{1}=A_{2}v_{2}=v_{1}$ , showing. $A_{1}A_{2}\neq A_{2}A_{1}$ .Moreover, $A_{1}^{2}v_{1}=A_{1}v_{2}=0$ and $A_{2}^{2}v_{2}=A_{2}v_{1}=0$ , showing. $A_{1}^{2}\equiv0$ and $A_{2}^{2}\equiv0$ . In particular, both $A_{1}$ and $A_{2}$ are nontrivial divisors of $0$  

Definition 6.22. Let. $V$ be a vector space over the field $F$ (a) A linear endomorphism $A\in{\mathcal{L}}(V,V)$ is called regular if, and only if, it is an au-. tomorphism (i.e. if, and only if, it is bijective/invertible). Otherwise, $A$ is called singular.  

(b) The set $\operatorname{GL}(V):=\{A\in{\mathcal{L}}(V,V):A$ is regular} = L(V, V)\* (cf. Def. and Rem. 4.41) is called the general linear group of $V$ (cf. Cor. 6.23 below).  

Corollary 6.23. Let $V$ be a vector space over the field. $F$ .Then the general linear. group $\operatorname{GL}(V)$ is, indeed, a group with respect to map composition. For $V\neq\{0\}$ , it is not a group with respect to addition (note $0\not\in\operatorname{GL}(V)$ in this case). If. $\dim V\geq3$ or $F\neq\{0,1\}$ and $\dim V\geq2$ , then the group $\operatorname{GL}(V)$ is not commutative.  

Proof. Since $\mathcal{L}(V,V)$ is a ring with unity, we know $\operatorname{GL}(V)={\mathcal{L}}(V,V)^{*}$ to be a group by Def. and Rem. 4.41 - since the composition of linear maps is linear, $\operatorname{GL}(V)$ is also a subgroup of the symmetric group $S_{V}$ (cf. Ex. 4.9(b)). If $\dim V\geq3$ , then the noncommutativity of $\operatorname{GL}(V)$ follows as in Ex. 4.9(b), where the elements $a,b,c$ of (4.7) are now taken as distinct elements of a basis of $V$ . Now let $v_{1},v_{2}\in V$ be linearly independent and $B$ a basis of $V$ with $v_{1},v_{2}\in B$ . Define $A_{1},A_{2}\in{\mathcal{L}}(V,V)$ by letting, for $v\in B$  

$$
A_{1}v:={\left\{\begin{array}{l l}{v_{2}}&{{\mathrm{for~}}v=v_{1},}\ {v_{1}}&{{\mathrm{for~}}v=v_{2},\quad A_{2}v:={\left\{\begin{array}{l l}{-v_{1}}&{{\mathrm{for~}}v=v_{1},}\ {v_{2}}&{{\mathrm{for~}}v=v_{2},}\ {v}&{{\mathrm{otherwise}},}\end{array}\right.}}\end{array}\right.}
$$  

Clearly, $A_{1},A_{2}\in\operatorname{GL}(V)$ with $A_{1}^{-1}=A_{1}$ and $A_{2}^{-1}=A_{2}$ . Moreover, $A_{1}A_{2}v_{1}=-A_{1}v_{1}=$ $-v_{2}$ $A_{2}A_{1}v_{1}=A_{2}v_{2}=v_{2}$ . If $F\neq\{0,1\}$ , then $v_{2}\neq-v_{2}$ , showing $A_{1}A_{2}\neq A_{2}A_{1}$  

## 7 Matrices  

### 7.1 Definition and Arithmetic  

Matrices provide a convenient representation for linear maps $A$ between finite-dimensional vector spaces $V$ and $W$ over the field $F^{\prime}$ . Recall the basis $\left\{A_{v_{i}w_{j}}:(j,i)\in\{1,\dots,m\}\times\right.$ $\{1,\ldots,n\}\}$ of $\mathcal{L}(V,W)$ that, in Th. 6.19, was shown to arise from bases $\{v_{1},\ldots,v_{n}\}$ and $\{w_{1},\ldots,w_{m}\}$ of $V$ and $W$ , respectively; $m,n\in\mathbb{N}$ . Thus, each $A\in{\mathcal{L}}(V,W)$ can be written in the form  

$$
A=\sum_{j=1}^{m}\sum_{i=1}^{n}a_{j i}A_{v_{i}w_{j}},
$$  

with coordinates $\big(a_{j i}\big)_{(j,i)\in\{1,\dots,m\}\times\{1,\dots,n\}}$ in $F^{\prime}$ (also cf. Ex. 6.7(a)). This motivates the following definition of matrices, where, however, instead of a field, we allow $F$ to be an arbitrary nonempty set $S$ , as it turns out to be sometimes useful to have matrices with entries that are not necessarily elements of a field.  

Definition 7.1. Let S be a nonempty set and m, n E N. A family (aji)(,t)e{1,.,m}{1,,n} in $S$ is called an $m$ by- $n$ or an $m\times n$ matrix over $S$ , where $m\times n$ is called the size, dimension or type of the matrix. The $a_{j i}$ are called the entries or elements of the matrix. One also writes just $(a_{j i})$ instead of $\big(a_{j i}\big)_{(j,i)\in\{1,\dots,m\}\times\{1,\dots,n\}}$ if the size of the matrix is understood. One usually thinks of the $m\times n$ matrix $(a_{j i})$ as the rectangular array  

$$
(a_{j i})={\left(\begin{array}{l l l}{a_{11}}&{\ldots}&{a_{1n}}\ {\vdots}&{\vdots}&{\vdots}\ {a_{m1}}&{\ldots}&{a_{m n}}\end{array}\right)}
$$  

with $m$ rows and $n$ columns. One therefore also calls $1\times n$ matrices row vectors and $m\times1$ matrices column vectors, and one calls $n\times n$ matrices quadratic. One calls the elements $a_{k k}$ the (main) diagonal elements of $(a_{j i})$ and one also says that these elements lie on the (main) diagonal of the matrix and that they form the (main) diagonal of the matrix. The set of all $m\times n$ matrices over $S$ is denoted by $\mathcal{M}(\boldsymbol{m},\boldsymbol{n},S)$ , and for the set of all quadratic $n\times n$ matrices, one uses the abbreviation $\mathcal{M}(n,S):=\mathcal{M}(n,n,S)$  

Definition 7.2 (Matrix Arithmetic). Let $F^{\prime}$ be a field and. $m,n,l\in\mathbb{N}$ . Let $S$ be a ring.   
or a vector space over $F$ (e.g. $S=F$  

(a) Matrix Addition: For $m\times n$ matrices $(a_{j i})$ and $\left(b_{j i}\right)$ over $S$ , define the sum.  

$$
(a_{j i})+(b_{j i}):=(a_{j i}+b_{j i})\in\mathcal{M}(m,n,S).
$$  

(b) Scalar Multiplication: Let $(a_{j i})$ be an $m\times n$ matrix over $S$ . If $S$ is a ring, then let $\lambda\in S$ ; if $S$ is a vector space over $F^{\prime}$ , then let $\lambda\in F$ . Define  

$$
\lambda\left(a_{j i}\right):=(\lambda a_{j i})\in\mathcal{M}(m,n,S).
$$  

(c) Matrix Multiplication: Let $S$ be a ring. For each $m\times n$ matrix $(a_{j i})$ and each $n\times l$ matrix $\left(b_{j i}\right)$ over $S$ , define the product  

$$
(a_{j i})(b_{j i}):=\left(\sum_{k=1}^{n}a_{j k}b_{k i}\right)_{(j,i)\in\{1,\dots,m\}\times\{1,\dots,l\}}\in\mathcal{M}(m,l,S),
$$  

i.e. the product of an $m\times n$ matrix and an. $n\times l$ matrix is an. $m\times{\mathit{l}}$ matrix (cf. Th.) 7.13 below).  

Example 7.3. As an example of matrix multiplication, we compute  

$$
\begin{array}{r l}&{\mathrm{\quad\left(\begin{array}{l l l}{1}&{-1}&{0}\ {1}&{0}&{-2}\end{array}\right)}\left(\begin{array}{l l}{-3}&{0}\ {1}&{1}\ {0}&{-1}\end{array}\right)=\left(\begin{array}{l}{1\cdot(-3)+(-1)\cdot1+0\cdot0}&{1\cdot0+(-1)\cdot1+0\cdot(-1)\cdot1+0\cdot(-1)\cdot1+0\cdot(-1)\cdot1+0\cdot(-1)\cdot1}\ {2\cdot(-3)+0\cdot1+(-2)\cdot0}&{2\cdot0+0\cdot1+(-2)\cdot(-1)\cdot1+0\cdot1}\end{array}\right)}\ &{\qquad=\left(\begin{array}{l l}{-4}&{-1}\ {-6}&{2}\end{array}\right).}\end{array}
$$  

Remark 7.4. Let $S$ be a nonempty set and $m,n\in\mathbb{N}$ (a) An $m\times n$ matrix $A:=(a_{j i})_{(j,i)\in\{1,\ldots,m\}\times\{1,\ldots,n\}}$ is defined as a family in. $S$ , i.e., recalling Def. 2.15(a), $A$ is defined as the function. $A:\{1,\dots,m\}\times\{1,\dots,n\}\longrightarrow S$ $A(j,i)=a_{j i}$ ; and ${\cal M}(m,n,S)={\mathcal F}\big(\{1,...,m\}\times\{1,...,n\},S\big)$ (so we notice that matrices are nothing new in terms of objects, but just a new way of thinking about functions from $\{1,\dots,m\}\times\{1,\dots,n\}$ into $S$ , that turns out to be convenient in certain contexts). Thus, if. $F^{\prime}$ is a field and $S=Y$ is a vector space over. $F^{\prime}$ , then the operations defined in Def. 7.2(a),(b) are precisely the same operations that were defined in (5.5) and ${\mathcal{M}}(m,n,Y)$ is a vector space according to Ex. 5.2(d). Clearly,. the map  

$$
I:{\mathcal{M}}(m,n,Y)\longrightarrow Y^{m\cdot n},\quad(a_{j i})\mapsto(y_{1},\dots,y_{m\cdot n}),
$$  

constitutes a linear isomorphism. For $Y=F$ , other important linear isomorphisms between ${\mathcal{M}}(m,n,F)$ and vector spaces of linear maps will be provided in Th. 7.10(a) below.  

(b) Let $A:=(a_{j i})_{(j,i)\in\{1,\ldots,m\}\times\{1,\ldots,n\}}$ be an $m\times n$ matrix over $S$ . Then, for each $i\in$ $\{1,\ldots,n\}$ , the $i$ th column of $A$  

$$
c_{i}:=c_{i}^{A}:=\left(\begin{array}{c}{{a_{1i}}}\ {{\vdots}}\ {{a_{m i}}}\end{array}\right)
$$  

can be considered both as an $m\times1$ matrix and as an element of $S^{m}$ . In particular, if $S=F$ is a field, then one calls $c_{i}$ the $i$ th column vector of $A$ . Analogously, for each $j\in\{1,\ldots,m\}$ , the $j$ th $r o w$ of $A$  

$$
r_{j}:=r_{j}^{A}:=\left(a_{j1}\quad...\quad a_{j n}\right)
$$  

can be considered both as a. $1\times n$ matrix and as an element of $S^{n}$ . In particular, if.   
$S=F$ is a field, then one calls r, the $j$ th row vector of. $A$  

It can sometimes be useful to think of matrix multiplication in terms of the matrix columns and rows of Rem. 7.4(b) in a number of different ways, as compiled in the following lemma:  

Lemma 7.5. Let $S$ be a ring, let $l,m,n\in\mathbb{N}$ , let $A:=(a_{j i})$ be an $m\times n$ matrix over $S$ , and let $B:=(b_{j i})$ be an $n\times l$ matrix over $S$ . Moreover, let $c_{1}^{A},\ldots,c_{n}^{A}$ and $r_{1}^{A},\ldots,r_{m}^{A}$ denote the columns and rows of $A$ , respectively, let $c_{1}^{B},\ldots,c_{l}^{B}$ and $r_{1}^{B},\ldots,r_{n}^{B}$ denote the columns and rows of $B$ (cf. Rem. 7.4(b)), i.e.  

$$
A=(a_{j i})=(c_{1}^{A}\quad...\quad c_{n}^{A})=\left(\begin{array}{l}{{r_{1}^{A}}}\ {{\vdots}}\ {{r_{m}^{A}}}\end{array}\right),\quad B=(b_{j i})=\left(c_{1}^{B}\quad...\quad c_{l}^{B}\right)=\left(\begin{array}{l}{{r_{1}^{B}}}\ {{\vdots}}\ {{r_{n}^{B}}}\end{array}\right).
$$  

(a) Consider  

$$
v:={\binom{v_{1}}{\vdots}}\in{\mathcal{M}}(n,1,S)\cong S^{n},\quad w:={\big(}w_{1}\dotsm w_{n}{\big)}\in{\mathcal{M}}(1,n,S)\cong S^{n}.
$$  

Then  

$$
A v=\sum_{k=1}^{n}c_{k}^{A}v_{k}\in\mathcal{M}(m,1,S),\quad w B=\sum_{k=1}^{n}w_{k}r_{k}^{B}\in\mathcal{M}(1,l,S),
$$  

where we wrote $c_{k}^{A}v_{k}$ , as we do not assume $S$ to be a commutative ring - if. $S$ is commutative (e.g. a field), then the more familiar form $v_{k}c_{k}^{A}$ is also admissible.  

(b) Columnwise Matrix Multiplication: One has  

$$
\underset{i\in\{1,\ldots,l\}}{\forall}\quad c_{i}^{A B}=A c_{i}^{B}.
$$  

(c) Rowwise Matrix Multiplication: One has  

$$
\begin{array}{r l}{\forall}&{{}r_{j}^{A B}=r_{j}^{A}B.}\end{array}
$$  

Proof. (a): Let $x:=A v$ $y:=w B$ . We then have  

$$
\begin{array}{r}{x={\small\left(\begin{array}{c}{x_{1}}\ {\vdots}\ {x_{m}}\end{array}\right)},\quad c_{k}^{A}={\small\left(\begin{array}{c}{a_{1k}}\ {\vdots}\ {a_{m k}}\end{array}\right)},\quad y=\left(y_{1}\ldots y_{l}\right),\quad r_{k}^{B}=\left(b_{k1}\ldots b_{k l}\right),}\end{array}
$$  

yielding  

$$
\begin{array}{c l}{{\displaystyle\forall\atop j\in\{1,\dots,m\}}}&{{x_{j}=\displaystyle\sum_{k=1}^{n}a_{j k}v_{k}=\left(\displaystyle\sum_{k=1}^{n}c_{k}^{A}v_{k}\right)_{j},}}\ {{\displaystyle\forall\atop i\in\{1,\dots,l\}}}&{{y_{i}=\displaystyle\sum_{k=1}^{n}w_{k}b_{k i}=\left(\displaystyle\sum_{k=1}^{n}w_{k}r_{k}^{B}\right)_{i},}}\end{array}
$$  

thereby proving (a).  

(b): For each $i\in\{1,\ldots,l\}$ $j\in\{1,\ldots,m\}$ , one computes  

$$
(c_{i}^{A B})_{j}=(A B)_{j i}=\sum_{k=1}^{n}a_{j k}b_{k i}=(A c_{i}^{B})_{j},
$$  

proving (b).  

(c): For each $j\in\{1,\ldots,m\}$ $i\in\{1,\ldots,l\}$ , one computes  

$$
(r_{j}^{A B})_{i}=(A B)_{j i}=\sum_{k=1}^{n}a_{j k}b_{k i}=(r_{j}^{A}B)_{i},
$$  

proving (c).  

Example 7.6. Using the matrices from Ex. 7.3, we have  

$$
{\binom{-4}{-6}}={\binom{1}{2}}-10-2{\binom{-3}{1}}={\binom{1}{2}}\cdot(-3)+{\binom{-1}{0}}\cdot1+{\binom{0}{-2}}\cdot0
$$  

and  

$$
-4\quad-1\quad={\left(\begin{array}{l l l}{1}&{-1}&{0}\end{array}\right)}{\left(\begin{array}{l l}{-3}&{0}\ {1}&{1}\ {0}&{-1}\end{array}\right)}=1\cdot\left(-3\quad0\right)+\left(-1\right)\cdot\left(1\quad1\right)+0\cdot\left(0\quad-1\right)
$$  

Theorem 7.7. Let $S$ be a ring.  

(a) Matrix multiplication of matrices over $S$ is associative whenever all relevant multiplications are defined. More precisely, if $A=(a_{j i})$ is an $m\times n$ matrix, $B=\left(b_{j i}\right)$ is an $n\times{\mathit{l}}$ , and $C=\left(c_{j i}\right)$ is an $l\times p$ matrix, then  

$$
(A B)C=A(B C).
$$  

(b) Matrix multiplication of matrices over $S$ is distributive whenever all relevant multiplications are defined. More precisely, if $A=(a_{j i})$ is an $m\times n$ matrix, $B=\left(b_{j i}\right)$ and $C=\left(c_{j i}\right)$ are $n\times{\mathit{l}}$ matrices, and $D=(d_{j i})$ is an $l\times p$ matrix, then  

$$
\begin{array}{c}{{A(B+C)=A B+A C,}}\ {{(B+C)D=B D+C D.}}\end{array}
$$  

(c) For each. $n\in\mathbb{N}$ $\mathcal{M}(n,S)$ is a ring. If. $S$ is a ring with unity, then $\mathcal{M}(n,S)$ is a ring with unity as well, where the additive neutral element is the zero matrix $0\in\mathcal{M}(n,S)$ (all entries are zero) and the multiplicative neutral element of $\mathcal{M}(n,S)$ is the so-called identity matrix $\operatorname{Id}_{n}:=(\delta_{j i})$  

$$
\delta_{j i}:=\left\{\begin{array}{l l}{1}&{f o r i=j,}\ {0}&{f o r i\neq j,}\end{array}\right.\quad\mathrm{Id}_{n}=\left(\begin{array}{l l l l}{1}&{}&{}\ {}&{\ddots}&{}\ {}&{}&{1}\end{array}\right),
$$  

where the usual meaning of such notation is that all omitted entries are $0$ .We call $\mathrm{GL}_{n}(S):=\mathcal{M}(n,S)^{*}$ , i.e. the group of invertible matrices over. $S$ , general linear group (we will see in Th. 7.10(a) below that, if. $S=F$ is a field and $V$ is a vector space of dimension n over. $F^{\prime}$ , then $\mathrm{GL}_{n}(F)$ is isomorphic to the general linear group. $\operatorname{GL}(V)$ of Def. 6.22(b)). Analogous to Def. 6.22(a), we call the matrices in $\mathrm{GL}_{n}(S)$ regular and the matrices in. ${\mathcal{M}}(n,S)\setminus{\mathrm{GL}}_{n}(S)$ singular.  

Proof. (a): One has $m\times p$ matrices $(A B)C=(d_{j i})$ and $A(B C)=\left(e_{j i}\right)$ , where, using associativity and distributivity in $S$ , one computes  

$$
d_{j i}=\sum_{\alpha=1}^{l}\left(\sum_{k=1}^{n}a_{j k}b_{k\alpha}\right)c_{\alpha i}=\sum_{\alpha=1}^{l}\sum_{k=1}^{n}a_{j k}b_{k\alpha}c_{\alpha i}=\sum_{k=1}^{n}a_{j k}\left(\sum_{\alpha=1}^{l}b_{k\alpha}c_{\alpha i}\right)=e_{j i},
$$  

thereby proving (7.7).  

(b): Exercise.  

(c): While $\mathcal{M}(n,S)$ is a ring due to (a), (b), and Ex. 4.9(e) (which says that $(\mathcal{M}(n,S),+)$ is a commutative group), we check the neutrality of $\operatorname{Id}_{n}$ : For each $A=(a_{j i})\in\mathcal{M}(n,S)$ we obtain  

$$
\operatorname{Id}_{n}A=\left(\sum_{k=1}^{n}\delta_{j k}a_{k i}\right)=(a_{j i})=A=\left(\sum_{k=1}^{n}a_{j k}\delta_{k i}\right)=A\operatorname{Id}_{n},
$$  

thereby establishing the case.  

Caveat 7.8. Matrix multiplication of matrices over a ring $S$ is, in general, not com-. mutative, even if $S$ is commutative: If $A$ is an $m\times n$ matrix and $B$ is an $n\times{\mathit{l}}$ matrix with $m\neq l$ , then $B A$ is not even defined. If $m=l$ , but $m\neq n$ , then $A B$ has dimension $m\times m$ , but $B A$ has different dimension, namely. $n\times n$ . And even if $m=n=l>1$ then commutativity is, in general, not true - for example, if. $S$ is a ring with unity and $0\not=1\in S$ , then  

$$
{\begin{array}{r l}{\left({\begin{array}{c c c c}{1}&{1}&{\ldots}&{1}\ {0}&{0}&{\ldots}&{0}\ {\vdots}&{\vdots}&{\vdots}\ {0}&{0}&{\ldots}&{0}\end{array}}\right)}&{{\left(\begin{array}{c c c c}{1}&{0}&{\ldots}&{0}\ {1}&{0}&{\ldots}&{0}\ {\vdots}&{\vdots}&{\vdots}&{\vdots}\ {1}&{0}&{\ldots}&{0}\end{array}\right)}={\left(\begin{array}{l l l l}{\lambda}&{0}&{\ldots}&{0}\ {0}&{0}&{\ldots}&{0}\ {\vdots}&{\vdots}&{\vdots}&{\vdots}\ {0}&{0}&{\ldots}&{0}\end{array}\right)},}\ {\left({\begin{array}{c c c c}{1}&{0}&{\ldots}&{0}\ {1}&{0}&{\ldots}&{0}\ {\vdots}&{\vdots}&{\vdots}\ {1}&{0}&{\ldots}&{0}\end{array}}\right)}&{{\left(\begin{array}{l l l l}{1}&{1}&{\ldots}&{1}\ {0}&{0}&{\ldots}&{0}\ {\vdots}&{\vdots}&{\vdots}&{\vdots}\ {0}&{0}&{\ldots}&{0}\end{array}\right)}={\left(\begin{array}{l l l l}{1}&{1}&{\ldots}&{1}\ {1}&{1}&{\ldots}&{1}\ {\vdots}&{\vdots}&{\vdots}&{\vdots}\ {1}&{1}&{\ldots}&{1}\end{array}\right)}.}\end{array}}
$$  

Note that $\lambda=m$ for $S=\mathbb{R}$ or $S=\mathbb{Z}$ , but, in general, $\lambda$ will depend on $S$ , e.g. for $S=\{0,1\}$ , one obtains $\lambda=m\mod2$  

### 7.2 Matrices as Representations of Linear Maps  

Remark 7.9. Coming back to the situation discussed at the beginning of the previous section above, resulting in (7.1), let. $\textstyle v=\sum_{i=1}^{n}\lambda_{i}v_{i}\in V$ with $\lambda_{1},\dots,\lambda_{n}\in F$ . Then (also cf. the calculation in (6.9))  

$$
\begin{array}{l}{{\displaystyle{\cal A}(v)=\sum_{i=1}^{n}\lambda_{i}{\cal A}(v_{i})=\sum_{i=1}^{n}\lambda_{i}\sum_{j=1}^{m}\sum_{k=1}^{n}a_{j k}{\cal A}_{v_{k}w_{j}}(v_{i})\ensuremath{\stackrel{\mathrm{(6.32)}}{=}}\sum_{i=1}^{n}\lambda_{i}\sum_{j=1}^{m}a_{j i}w_{j}}}\ {{\displaystyle~=\sum_{j=1}^{m}\left(\sum_{i=1}^{n}a_{j i}\lambda_{i}\right)w_{j}}.}\end{array}
$$  

Thus, if we represent $\upsilon$ by a column vector $\tilde{v}$ (an $n\times1$ matrix) containing its coordinates $\lambda_{1},\ldots,\lambda_{n}$ with respect to the basis $\{v_{1},\ldots,v_{n}\}$ and $A(v)$ by a column vector $\tilde{w}$ (an $m\times1$ matrix) containing its coordinates with respect to the basis $\{w_{1},\ldots,w_{m}\}$ , then (7.11) shows  

$$
\tilde{w}=M\tilde{v}=M\left(\begin{array}{l}{\lambda_{1}}\ {\vdots}\ {\lambda_{n}}\end{array}\right),\quad\mathrm{where}\quad M:=(a_{j i})\in\mathcal{M}(m,n,F).
$$  

For finite-dimensional vector spaces, the precise relationship between linear maps, bases, and matrices is provided by the following theorem:  

Theorem 7.10. Let $V$ and $W$ be finite-dimensional vector spaces over the field $F^{\prime}$ let $B_{V}:=\{v_{1},\ldots,v_{n}\}$ and $B_{W}:=\{w_{1},\dots,w_{m}\}$ be bases of $V$ and $W$ , respectively; $m,n\in\mathbb{N}$ $n=\dim V$ $m=\dim W$  

(a) The map $I:=I(B_{V},B_{W})$  

$$
I:\mathcal{L}(V,W)\longrightarrow\mathcal{M}(m,n,F),\quad A\mapsto(a_{j i}),
$$  

where the $a_{j i}$ are given by (7.1), i.e. by  

$$
A=\sum_{j=1}^{m}\sum_{i=1}^{n}a_{j i}A_{v_{i}w_{j}},
$$  

constitutes a linear isomorphism. Moreover, in the special case $V=W$ $v_{i}=w_{i}$ for $i\in\{1,\ldots,n\}$ , the map $I$ also constitutes a ring isomorphism $I:\mathcal{L}(V,V)\cong$ $\mathcal{M}(n,F)$ ; its restriction to $\operatorname{GL}(V)$ then constitutes a group isomorphism $I:\operatorname{GL}(V)$ $\cong\operatorname{GL}_{n}(F)$  

(b) Let $a_{j i}\in F$ $j\in\{1,\ldots,m\}$ $i\in\{1,\ldots,n\}$ .Moreover, let. $A\in{\mathcal{L}}(V,W)$ .Then (7.1) holds if, and only if,  

$$
\forall_{i\in\{1,\dots,n\}}A v_{i}=\sum_{j=1}^{m}a_{j i}w_{j}.
$$  

Proof. (a): According to Th. 6.19, $\big\{A_{v_{i}w_{j}}:(j,i)\in\{1,\dots,m\}\times\{1,\dots,n\}\big\}$ forms a basis of $\mathcal{L}(V,W)$ . Thus, to every family of coordinates $\{a_{j i}:(j,i)\in\{1,\ldots,m\}\times$  

$\{1,\ldots,n\}\}$ in $F^{\prime}$ , (7.1) defines a unique element of $\mathcal{L}(V,W)$ , i.e. $I$ is bijective. It remains to verify that $I$ is linear. To this end, let $\lambda,\mu\in F$ and $A,B\in{\mathcal{L}}(V,W)$ with  

$$
\begin{array}{r l r}{A=\displaystyle{\sum_{j=1}^{m}\sum_{i=1}^{n}}a_{j i}A_{v_{i}w_{j}},}&{\qquad}&{(a_{j i})=I(A)\in\mathcal{M}(m,n,F),}\ {B=\displaystyle{\sum_{j=1}^{m}\sum_{i=1}^{n}}b_{j i}A_{v_{i}w_{j}},}&{\qquad}&{(b_{j i})=I(B)\in\mathcal{M}(m,n,F).}\end{array}
$$  

Then  

$$
\lambda A+\mu B=\lambda\sum_{j=1}^{m}\sum_{i=1}^{n}a_{j i}A_{v_{i}w_{j}}+\mu\sum_{j=1}^{m}\sum_{i=1}^{n}b_{j i}A_{v_{i}w_{j}}=\sum_{j=1}^{m}\sum_{i=1}^{n}(\lambda a_{j i}+\mu b_{j i})A_{v_{i}w_{j}},
$$  

showing  

$$
I(\lambda A+\mu B)=(\lambda a_{j i}+\mu b_{j i})=\lambda(a_{j i})+\mu(b_{j i})=\lambda I(A)+\mu I(B),
$$  

proving the linearity of $I$ . Now let $V=W$ and $v_{i}=w_{i}$ for each $i\in\{1,\ldots,n\}$ .We claim  

$$
B A=\sum_{j=1}^{n}\sum_{i=1}^{n}c_{j i}A_{v_{i}v_{j}},\quad\mathrm{where}\quad c_{j i}=\sum_{k=1}^{n}b_{j k}a_{k i}:
$$  

Indeed, for each $l\in\{1,\ldots,n\}$ , one calculates  

$$
\begin{array}{c l l}{\displaystyle(B A)v_{l}=B\left(\sum_{k=1}^{n}\sum_{i=1}^{n}a_{k i}A_{v_{i}v_{k}}v_{l}\right)=B\left(\sum_{k=1}^{n}a_{k l}v_{k}\right)=\sum_{j=1}^{n}\sum_{i=1}^{n}b_{j i}A_{v_{i}v_{j}}\sum_{k=1}^{n}a_{k l}v_{k}}\ {\displaystyle\qquad=\sum_{j=1}^{n}\sum_{k=1}^{n}b_{j k}a_{k l}v_{j}=\sum_{j=1}^{n}c_{j l}v_{j}=\sum_{j=1}^{n}\sum_{i=1}^{n}c_{j i}A_{v_{i}v_{j}}v_{l},}\end{array}
$$  

thereby proving (7.15). Thus,  

$$
I(B A)=\left(\sum_{k=1}^{n}b_{j k}a_{k i}\right)=(b_{j i})(a_{j i})=I(B)I(A),
$$  

proving $I$ to be a ring isomorphism. Since, clearly, $I(\mathrm{GL}(V))=\mathrm{GL}_{n}(F)$ , the proof of.   
(a) is complete.  

(b): If (7.1) holds, then the calculation (7.11) (with. $\lambda_{k}:=\delta_{i k}$ ) proves (7.14). Conversely, assume (7.14). It was then shown in the proof of Th. 6.19(b) that (7.1) must hold. $\vert$  

Definition and Remark 7.11. In the situation of Th. 7.10, for each $A\in{\mathcal{L}}(V,W)$ , one calls the matrix $I(A)=(a_{j i})\in\mathcal{M}(m,n,F)$ the (transformation) matrix corresponding to $A$ with respect to the basis $\{v_{1},\ldots,v_{n}\}$ of $V$ and the basis $\{w_{1},\ldots,w_{m}\}$ of $W$ . If the bases are understood, then one often tends to identify the map with its corresponding matrix.  

However, as $I(A)$ depends on the bases, identifying. $A$ and $I(A)$ is only admissible as. long as one keeps the bases of. $V$ and $W$ fixed! Moreover, if one represents matrices as rectangular arrays as in (7.2) (which one usually does), then one actually considers the basis vectors of $\{v_{1},\ldots,v_{n}\}$ and $\{w_{1},\ldots,w_{m}\}$ as ordered from $1$ to $n$ (resp. $m$ ), i.e. $I(A)$ actually depends on the so-called ordered bases. $\left(v_{1},\ldots,v_{n}\right)$ and $(w_{1},\ldots,w_{m})$ (ordered bases are tuples rather than sets and the matrix corresponding to. $A$ changes if the order of the basis vectors changes)..  

Similarly, we had seen in (7.12) that it can be useful to identify a vector $\begin{array}{r}{v=\sum_{i=1}^{n}\lambda_{i}v_{i}}\end{array}$ with its coordinates $(\lambda_{1},\ldots,\lambda_{n})$ , typically represented as an $n\times1$ matrix (a column vector, as in (7.12)) or a $1\times n$ matrix (a row vector). Obviously, this identification is also only admissible as long as the basis. $\{v_{1},\ldots,v_{n}\}$ and its order is kept fixed.  

Example 7.12. Let $V:=\mathbb{Q}^{4}$ with ordered basis $B_{V}:=\left(v_{1},v_{2},v_{3},v_{4}\right)$ and let. $W:=\mathbb{Q}^{2}$ with ordered basis $B_{W}:=(w_{1},w_{2})$ . Moreover, assume $A\in{\mathcal{L}}(V,W)$ satisfies  

$$
{\begin{array}{r c r c l}{A v_{1}}&{=}&{w_{1}}&&\ {A v_{2}}&{=}&{2w_{1}}&{-}&{w_{2}}\ {A v_{3}}&{=}&{3w_{1}}&&\ {A v_{4}}&{=}&{4w_{1}}&{-}&{2w_{2}.}\end{array}}
$$  

According to Th. 7.10(a),(b), the coefficients on the right-hand side of the above equations provide the columns of the matrix representing. $A$ : The matrix $I(A)$ of $A$ with respect to $B_{V}$ and $B_{W}$ $I$ according to Th. 7.10(a)) is  

$$
I(A)=\left({\begin{array}{c c c c}{1}&{2}&{3}&{4}\ {0}&{-1}&{0}&{-2}\end{array}}\right).
$$  

If we switch $v_{1}$ and $v_{4}$ in $B_{V}$ to obtain $B_{V}^{\prime}:=\left(v_{4},v_{2},v_{3},v_{1}\right)$ , and we switch $w_{1}$ and $w_{2}$ in $B_{W}$ to obtain $B_{W}^{\prime}:=(w_{2},w_{1})$ , then the matrix $I^{\prime}(A)$ of $A$ with respect to $B_{V}^{\prime}$ and $B_{W}^{\prime}$ is obtained from $I(A)$ by switching columns $^{1}$ and 4 as well as rows 1 and 2, resulting in  

$$
I^{\prime}(A)=\binom{-2}{4}\begin{array}{c c c c}{{-1}}&{{0}}&{{0}}\ {{2}}&{{3}}&{{1}}\end{array}.
$$  

Suppose, we want to determine $A v$ for the vector. $v:=-v_{1}+3v_{2}-2v_{3}+v_{4}$ .Then,  

# 7 MATRICES  

according to (7.12), we can do that via the matrix multiplication  

$$
I(A)\left({\begin{array}{r}{-1}\ {3}\ {-2}\ {1}\end{array}}\right)=\left({\begin{array}{r r r r}{1}&{2}&{3}&{4}\ {0}&{-1}&{0}&{-2}\end{array}}\right)\cdot\left({\begin{array}{r}{-1}\ {3}\ {-2}\ {1}\end{array}}\right)=\left({\begin{array}{r}{3}\ {-5}\end{array}}\right),
$$  

obtaining $A v=3w_{1}-5w_{2}$  

The following Th. 7.13 is the justification for defining matrix multiplication according to Def. 7.2(c).  

Theorem 7.13. Let $F$ be a field, let. $n,m,l\in\mathbb{N}$ , and let $V,W,X$ be finite-dimensional vector spaces over $F$ $\dim V=n$ $\dim W=m$ $\dim X=l$ , with ordered bases, $B_{V}:= $ $(v_{1},\ldots,v_{n})$ $B_{W}:=(w_{1},\dots,w_{m})$ , and $B_{X}:=(x_{1},\dots,x_{l})$ , respectively. If. $A\in{\mathcal{L}}(V,W)$ $B\in{\mathcal{L}}(W,X)$ $M=(a_{j i})\in\mathcal{M}(m,n,F)$ is the matrix corresponding to $A$ with respect to $B_{V}$ and $B_{W}$ , and $N=(b_{j i})\in\mathcal{M}(l,m,F)$ is the matrix corresponding to $B$ with respect to $B_{W}$ and $B_{X}$ , then $\begin{array}{r}{N M=(\sum_{k=1}^{m}b_{j k}a_{k i})\in\mathcal{M}(l,n,F)}\end{array}$ is the matrix corresponding to $B A$ with respect to. $B_{V}$ and $B_{X}$  

Proof. For each $i\in\{1,\ldots,n\}$ , one computes  

$$
\begin{array}{l}{({\boldsymbol B}{\boldsymbol A})(v_{i})={\boldsymbol B}\big({\boldsymbol A}(v_{i})\big)={\boldsymbol B}\left(\displaystyle\sum_{k=1}^{m}a_{k i}w_{k}\right)=\displaystyle\sum_{k=1}^{m}a_{k i}{\boldsymbol B}(w_{k})=\displaystyle\sum_{k=1}^{m}a_{k i}\displaystyle\sum_{j=1}^{l}b_{j k}\boldsymbol x_{j}}\ {=\displaystyle\sum_{j=1}^{l}\sum_{k=1}^{m}b_{j k}a_{k i}x_{j}=\displaystyle\sum_{j=1}^{l}\left(\displaystyle\sum_{k=1}^{m}b_{j k}a_{k i}\right)\boldsymbol x_{j},}\end{array}
$$  

proving $\begin{array}{r}{N M=(\sum_{k=1}^{m}b_{j k}a_{k i})}\end{array}$ is the matrix corresponding to $B A$ with respect to the bases $\{v_{1},\ldots,v_{n}\}$ and $\{x_{1},\ldots,x_{l}\}$ $\vert$  

As we have seen, given $A\in{\mathcal{L}}(V,W)$ , the matrix $I(A)$ representing $A$ depends on the chosen (ordered) bases of $V$ and $W$ .  It will be one goal of Linear Algebra II to find methods to determine bases of $V$ and $W$ such that the form of $I(A)$ becomes particularly simple. In the following Th. 7.14, we show how $I(A)$ changes for given basis transitions for $V$ and $W$ , respectively.  

Theorem 7.14. Let $V$ and $W$ be finite-dimensional vector spaces over the field $F$ $m,n\in\mathbb{N}$ $\dim V=n$ $\dim W=m$ . Let $B_{V}:=(v_{1},\ldots,v_{n})$ and $B_{W}:=(w_{1},\dots,w_{m})$ be ordered bases of. $V$ and $W$ , respectively. Moreover, let $B_{V}^{\prime}:=(v_{1}^{\prime},\ldots,v_{n}^{\prime})$ and $B_{W}^{\prime}:= $ $(w_{1}^{\prime},\dots,w_{m}^{\prime})$ also be ordered bases of $V$ and $W$ , respectively, and let $c_{j i},d_{j i},f_{j i}\in F$ be such that  

$$
\begin{array}{r l}{\underset{i\in\{1,\ldots,n\}}{\forall}}&{{}v_{i}^{\prime}=\displaystyle{\sum_{j=1}^{n}}c_{j i}v_{j},}\ {\underset{i\in\{1,\ldots,m\}}{\forall}}&{{}w_{i}^{\prime}=\displaystyle{\sum_{j=1}^{m}}f_{j i}w_{j},\quad w_{i}=\displaystyle{\sum_{j=1}^{m}}d_{j i}w_{j}^{\prime},}\end{array}
$$  

where $(d_{j i})=(f_{j i})^{-1}\in\mathrm{GL}_{m}(F)$ (we then call $(c_{j i})\in\operatorname{GL}_{n}(F)$ and $(f_{j i})\in\operatorname{GL}_{m}(F)$ the transition matrices corresponding to the basis transitions from $B_{V}$ to $B_{V}^{\prime}$ and from $B_{W}$ to $B_{W}^{\prime}$ , respectively). If $A\in{\mathcal{L}}(V,W)$ has $I(B_{V},B_{W})(A)=(a_{j i})\in\mathcal{M}(m,n,F)$ with $I(B_{V},B_{W})$ as in Th. 7.10(a), then  

$$
I(B_{V}^{\prime},B_{W}^{\prime})(A)=(e_{j i}),\quad w h e r e\quad(e_{j i})=(d_{j i})(a_{j i})(c_{j i})=(f_{j i})^{-1}(a_{j i})(c_{j i}).
$$  

In particular, in the special case, where $V=W$ $v_{i}=w_{i}$ $v_{i}^{\prime}=w_{i}^{\prime}$ for each $i\in\{1,\ldots,n\}$ one has  

$$
I(B_{V}^{\prime},B_{V}^{\prime})(A)=(e_{j i}),\quad w h e r e\quad(e_{j i})=(c_{j i})^{-1}(a_{j i})(c_{j i}).
$$  

Proof. For each $i\in\{1,\ldots,n\}$ , we compute  

$$
\begin{array}{l}{{\displaystyle1v_{i}^{\prime}=A\left(\sum_{l=1}^{n}c_{l i}v_{l}\right)=\sum_{l=1}^{n}c_{l i}A v_{l}\left.\stackrel{\left(7.14\right)}{=}\sum_{l=1}^{n}c_{l i}\sum_{k=1}^{m}a_{k l}w_{k}=\sum_{l=1}^{n}c_{l i}\sum_{k=1}^{m}a_{k l}\sum_{j=1}^{m}d_{j k}w_{j}^{\prime}\right.}}\ {{\displaystyle~\left.=\sum_{j=1}^{m}\left(\sum_{l=1}^{n}\left(\sum_{k=1}^{m}d_{j k}a_{k l}\right)c_{l i}\right)w_{j}^{\prime}\right)}}\end{array}
$$  

i.e. (7.18) holds in consequence of Th. 7.10(b),(a).  

Example 7.15. We explicitly write the transformations and matrices of Th. 7.14 for the situation of Ex. 7.12: There we had $V:=\mathbb{Q}^{4}$ with ordered bases $B_{V}:=\left(v_{1},v_{2},v_{3},v_{4}\right)$ $B_{V}^{\prime}:=\left(v_{4},v_{2},v_{3},v_{1}\right)$ , and $W:=\mathbb{Q}^{2}$ with ordered bases $B_{W}:=(w_{1},w_{2})$ $B_{W}^{\prime}:=(w_{2},w_{1})$ Thus,  

$$
\begin{array}{r l r l r l r l}{v_{1}^{\prime}}&{=}&&{}&{v_{4}}&{}&{}&{}\ {v_{2}^{\prime}}&{=}&{}&{v_{2}}&{}&{}&{}&{}\ {v_{3}^{\prime}}&{=}&{}&{}&{v_{3}}&{}&{}&{}&{}\ {v_{4}^{\prime}}&{=}&{v_{1},}&{}&{}&{}&{}&{}\end{array}\qquad(c_{j i})=\left(\begin{array}{l l l l}{0}&{0}&{0}&{1}\ {0}&{1}&{0}&{0}\ {0}&{0}&{1}&{0}\ {1}&{0}&{0}&{0}\end{array}\right)
$$  

and  

$$
\begin{array}{r c l c r c l}{w_{1}^{\prime}}&{=}&{}&{w_{2}}&{}&{}\ {w_{2}^{\prime}}&{=}&{w_{1},}&{}&{}&{(f_{j i})=\left(\begin{array}{c c}{0}&{1}\ {1}&{0}\end{array}\right)}\end{array}
$$  

and  

$$
\begin{array}{r l r}{w_{1}}&{=}&{w_{2}^{\prime}\qquad(d_{j i})=\left(\begin{array}{l l}{0}&{1}\ {1}&{0}\end{array}\right).}\end{array}
$$  

Moreover, $A\in{\mathcal{L}}(V,W)$ in Ex. 7.12 was such that  

$$
(a_{j i})=I(B_{V},B_{W})(A)=\left({1\begin{array}{c c c c}{{1}}&{{2}}&{{3}}&{{4}}\ {{0}}&{{-1}}&{{0}}&{{-2}}\end{array}}\right).
$$  

Thus, according to (7.18),  

$$
\begin{array}{c}{{I(B_{V}^{\prime},B_{W}^{\prime})(A)={\left(\begin{array}{l l}{{0}}&{{1}}\ {{1}}&{{0}}\end{array}\right)}{\left(\begin{array}{l l l l}{{1}}&{{2}}&{{3}}&{{4}}\ {{0}}&{{-1}}&{{0}}&{{-2}}\end{array}\right)}{\left(\begin{array}{l l l l}{{0}}&{{0}}&{{0}}&{{1}}\ {{0}}&{{1}}&{{0}}&{{0}}\ {{0}}&{{0}}&{{1}}&{{0}}\ {{1}}&{{0}}&{{0}}&{{0}}\end{array}\right)}}}\ {{={\left(\begin{array}{l l}{{0}}&{{1}}\ {{1}}&{{0}}\end{array}\right)}{\left(\begin{array}{l l l l}{{4}}&{{2}}&{{3}}&{{1}}\ {{-2}}&{{-1}}&{{0}}&{{0}}\end{array}\right)}={\left(\begin{array}{l l l l}{{-2}}&{{-1}}&{{0}}&{{0}}\ {{4}}&{{2}}&{{3}}&{{1}}\end{array}\right)},}}\end{array}
$$  

which is precisely $I^{\prime}(A)$ of Ex. 7.12.  

### 7.3 Rank and Transpose  

Definition 7.16. Let $F^{\prime}$ be a field and $m,n\in\mathbb{N}$  

(a) Let $V$ and $W$ be vector spaces over $F$ and $A\in{\mathcal{L}}(V,W)$ . Thens $\operatorname{rk}(A):=\dim\operatorname{Im}A$ is called the rank of $A$  

(b) Let $(a_{j i})_{(j,i)\in\{1,\ldots,m\}\times\{1,\ldots,n\}}\in\mathcal{M}(m,n,F)$ and consider the column vectors and row vectors of. $(a_{j i})$ as elements of the vector spaces $F^{r n}$ and $F^{n}$ , respectively (cf. Rem.) 7.4(b)). Then  

$$
\mathrm{rk}(a_{j i}):=\mathrm{dim}\left\langle\left\{{\binom{a_{1i}}{\vdots}}:i\in\{1,\dots,n\}\right\}\right\rangle
$$  

is called the column rank or just the rank of $(a_{j i})$ . Analogously,  

$$
\operatorname{rrk}(a_{j i}):=\dim\left\langle\left\{{\left(a_{j1}\quad\dots\quad a_{j n}\right)}:j\in\{1,\dots,m\}\right\}\right\rangle
$$  

is called the row rank of $(a_{j i})$  

A main goal of the present section is to show that, if $V$ and $W$ are finite-dimensional vector spaces, $A\in{\mathcal{L}}(V,W)$ , and $(a_{j i})$ is the matrix representing $A$ with respect to chosen ordered bases of $V$ and $W$ , respectively, then $\operatorname{rk}(A)=\operatorname{rk}(a_{j i})=\operatorname{rrk}(a_{j i})$ (cf. Th. 7.23 below).  

Theorem 7.17. Let $F^{\prime}$ be a field, $m,n\in\mathbb{N}$ (a) Let $V,W$ be finite-dimensional vector spaces over $F$ $\dim V=n$ $\dim W=m$ , where $B_{V}:=(v_{1},\ldots,v_{n})$ is an ordered basis of. $V$ and $B_{W}:=(w_{1},\dots,w_{m})$ is an ordered basis of $W$ . If $A\in{\mathcal{L}}(V,W)$ and $(a_{j i})\in\mathcal{M}(m,n,F)$ is the matrix corresponding to. $A$ with respect to. $B_{V}$ and $B_{W}$ , then  

$$
\operatorname{rk}(A)=\operatorname{rk}(a_{j i}).
$$  

(b) If the matrices $(c_{j i})\in\mathcal{M}(n,n,F)$ and $(d_{j i})\in\mathcal{M}(m,m,F)$ are regular and $(a_{j i})\in$ $\mathcal{M}(\boldsymbol{m},\boldsymbol{n},\boldsymbol{F})$ , then  

$$
\operatorname{rk}(a_{j i})=\operatorname{rk}\left((d_{j i})(a_{j i})(c_{j i})\right).
$$  

Proof. (a) is basically due to Lem. 7.5(a) and Th. 6.9: Let $B:W\longrightarrow F^{m}$ be the linear isomorphism with $B(w_{j})=e_{j}$ , where $\{e_{1},\ldots,e_{m}\}$ is the standard basis of $F^{m}$ (cf. Ex. 5.16(c)). Then  

$$
\operatorname{rk}(A)=\dim\operatorname{Im}A=\dim B(\operatorname{Im}A)=\dim\operatorname{Im}(B A)=\operatorname{rk}(B A).
$$  

Since  

$$
\begin{array}{r l}{\underset{i\in\{1,\ldots,n\}}{\forall}}&{(B A)v_{i}=B\left(\displaystyle\sum_{j=1}^{m}a_{j i}w_{j}\right)=\left(\displaystyle\sum_{i=1}^{a_{1i}}\right)=c_{i}^{A},}\end{array}
$$  

we have $\operatorname{Im}(B A)=\langle\{c_{1}^{A},\ldots,c_{n}^{A}\}\rangle$ , which, together with (7.21), proves (a)  

(b): Let $B_{V}:=(v_{1},\ldots,v_{n})$ and $B_{W}:=(w_{1},\dots,w_{m})$ be ordered bases of. $V:=F^{\ast}$ and $W:=F^{m}$ , respectively. Moreover, let $A\in{\mathcal{L}}(V,W)$ be defined by (7.14), i.e. by  

$$
\sqcap_{i\in\{1,\ldots,n\}}\quad A v_{i}=\sum_{j=1}^{m}a_{j i}w_{j}.
$$  

Then $(a_{j i})$ is the matrix representing $A$ with respect to $B_{V}$ and $B_{W}$ and $\operatorname{rk}(A)=\operatorname{rk}(a_{j i})$ by (a). Now let $B_{V}^{\prime}:=(v_{1}^{\prime},...,v_{n}^{\prime})$ and $B_{W}^{\prime}:=(w_{1}^{\prime},\dots,w_{m}^{\prime})$ also be ordered bases of $V$ and $W$ , respectively, such that (7.17) holds, i.e.  

$$
\forall_{i\in\{1,\ldots,n\}}\quad v_{i}^{\prime}=\sum_{j=1}^{n}c_{j i}v_{j},\qquad\forall_{i\in\{1,\ldots,m\}}\quad w_{i}=\sum_{j=1}^{m}d_{j i}w_{j}^{\prime}
$$  

(such bases exist, since $\left(c_{j i}\right)$ and $(d_{j i})$ are regular), then, according to Th. 7.14, the matrix $(e_{j i}):=(d_{j i})(a_{j i})(c_{j i})$ represents $A$ with respect to $B_{V}^{\prime}$ and $B_{W}^{\prime}$ . Thus, (a) yields $\operatorname{rk}(e_{j i})=\operatorname{rk}(A)=\operatorname{rk}(a_{j i})$ , as desired.  

Theorem 7.18. Let $V,W$ be finite-dimensional vector spaces over the field $F^{\prime}$ $\dim V=$ $n$ $\dim W=m$ $(m,n)\in\mathbb{N}^{2}$ $A\in{\mathcal{L}}(V,W)$ with $r:=\operatorname{rk}(A)$ . Then there exists ordered. bases $B_{V}:=(v_{1},\ldots,v_{n})$ and $B_{W}:=(w_{1},\dots,w_{m})$ of $V$ and $W$ , respectively, such that. the matrix $(a_{j i})\in\mathcal{M}(m,n,F)$ corresponding to $A$ with respect to. $B_{V}$ and $B_{W}$ satisfies  

$$
a_{j i}=\left\{\begin{array}{l l l}{1}&{f o r j=i,1\leq j\leq r,}\ {0}&{o t h e r w i s e,}\end{array}\right.\quad i.e.\quad(a_{j i})=\left(\frac{\operatorname{Id}_{r}{\bf\omega}\left|~0~\right.}{0~\left|~0~\right.}\right).
$$  

Proof. According to Th. 6.8(a), we know  

$$
n=\dim V=\dim\ker A+\dim\operatorname{Im}A=\dim\ker A+r.
$$  

Thus, we can choose an ordered basis $B_{V}=(v_{1},\ldots,v_{n})$ of $V$ , such that $\left(v_{r+1},\ldots,v_{n}\right)$ is a basis of $\ker A$ . For each $i\in\{1,\ldots,r\}$ , let $w_{i}:=A v_{i}$ . Then $(w_{1},\ldots,w_{r})$ is a basis of $\operatorname{Im}A$ and there exist $w_{r+1},\dots,w_{m}\in W$ such that $B_{W}=(w_{1},\dots,w_{m})$ constitutes a basis of $W$ . Since  

$$
\begin{array}{r l}{\forall}&{{}A v_{i}=\left\{\begin{array}{l l}{w_{i}}&{\mathrm{for}~1\leq i\leq r,}\ {0}&{\mathrm{for}~i>r,}\end{array}\right.}\end{array}
$$  

$(a_{j i})$ has the desired form.  

As a tool for showing $\mathrm{rk}(a_{j i})~=~\mathrm{rrk}(a_{j i})$ , we will now introduce the transpose of a matrix, which is also of general interest. While, here, we are mostly interested in using the transpose of a matrix for a matrix representing a linear map, the concept makes sense in the more general situation of Def. 7.1:  

Definition 7.19. Let $S$ be a nonempty set, $A:=(a_{j i})_{(j,i)\in\{1,\ldots,m\}\times\{1,\ldots,n\}}\in\mathcal{M}(m,n,S)$ and $m,n\in\mathbb{N}$ . Then we define the transpose of $A$ , denoted $A^{\mathrm{t}}$ , by  

$$
\begin{array}{r}{A^{\mathrm{t}}:=(a_{j i}^{\mathrm{t}})_{(j,i)\in\{1,\dots,n\}\times\{1,\dots,m\}}\in\mathcal{M}(n,m,S),\quad\mathrm{where}\quad_{(j,i)\in\{1,\dots,n\}\times\{1,\dots,m\}}\quad a_{j i}^{\mathrm{t}}:=0}\end{array}
$$  

Thus, if $A$ is an $m\times n$ matrix, then its transpose is an $n\times m$ matrix, where one obtains. $A^{\mathrm{t}}$ from $A$ by switching rows and columns: $A$ is the map $f:\{1,\dots,m\}\times\{1,\dots,n\}\longrightarrow S$ $f(j,i)=a_{j i}$ , and its transpose. $A^{\mathrm{t}}$ is the map. $f^{\mathrm{t}}~:~\{1,\dots,n\}\times\{1,\dots,m\}~\longrightarrow~S$ $f^{\mathrm{t}}(j,i)=a_{j i}^{\mathrm{t}}=f(i,j)=a_{i j}$  

Example 7.20. As examples of forming transposes, consider  

$$
{\left(\begin{array}{l l}{1}&{2}\ {3}&{4}\end{array}\right)}^{\mathrm{t}}={\left(\begin{array}{l l}{1}&{3}\ {2}&{4}\end{array}\right)},\qquad{\left(\begin{array}{l l l l}{1}&{2}&{3}&{4}\ {0}&{-1}&{0}&{-2}\end{array}\right)}^{\mathrm{t}}={\left(\begin{array}{l l}{1}&{0}\ {2}&{-1}\ {3}&{0}\ {4}&{-2}\end{array}\right)}.
$$  

Remark 7.21. Let $S$ be a nonempty set, $m,n\in\mathbb{N}$ . It is immediate from Def. 7.19 that the map. $A\mapsto A^{\mathrm{t}}$ is bijective from ${\mathcal{M}}(m,n,S)$ onto $\mathcal{M}(n,m,S)$ , where.  

$$
\begin{array}{r l}{\forall}&{{}(A^{\mathrm{t}})^{\mathrm{t}}=A.}\end{array}
$$  

Theorem 7.22. Let $m,n,l\in\mathbb{N}$  

(a) Let $S$ be a commutative ring. If $A\in{\mathcal{M}}(m,n,S)$ and $B\in\mathcal{M}(n,l,S)$ , then.  

$$
(A B)^{\mathrm{t}}=B^{\mathrm{t}}A^{\mathrm{t}}.
$$  

If $A\in\operatorname{GL}_{n}(S)$ , then $A^{\mathrm{t}}\in\operatorname{GL}_{n}(S)$ and  

$$
(A^{\operatorname{t}})^{-1}=(A^{-1})^{\operatorname{t}}.
$$  

(b) Let $F$ be a field. Then the map  

$$
I:{\mathcal{M}}(m,n,F)\longrightarrow{\mathcal{M}}(n,m,F),\quad A\mapsto A^{\mathrm{t}},
$$  

constitutes a linear isomorphism.  

Proof. Exercise.  

Theorem 7.23. Let $V,W$ be finite-dimensional vector spaces over the field $F^{\prime}$ $\dim V=$ $n$ $\dim W=m$ , with ordered bases $B_{V}:=(v_{1},\ldots,v_{n})$ and $B_{W}:=(w_{1},\dots,w_{m})$ , respectively. If $A\in{\mathcal{L}}(V,W)$ and $(a_{j i})\in\mathcal{M}(m,n,F)$ is the matrix corresponding to $A$ with respect to $B_{V}$ and $B_{W}$ , then  

$$
\operatorname{rk}(A)=\operatorname{rk}(a_{j i})=\operatorname{rrk}(a_{j i}).
$$  

Proof. As the first equality was already shown in Th. 7.17(a), it merely remains to show $\mathrm{rk}(a_{j i})=\mathrm{rrk}(a_{j i})$ .Let $r:=\operatorname{rk}(A)$ .According to Th. 7.18 and Th. 7.14, there exist regular matrices $(x_{j i})\in\operatorname{GL}_{m}(F)$ $(y_{j i})\in\operatorname{GL}_{n}(F)$ such that  

$$
(x_{j i})(a_{j i})(y_{j i})=\left(\frac{\mathrm{Id}_{r}\mid0}{0\mid0}\right)\quad\stackrel{(7.24)}{\Rightarrow}\quad(y_{j i})^{\mathrm{t}}(a_{j i})^{\mathrm{t}}(x_{j i})^{\mathrm{t}}=\left(\frac{\mathrm{Id}_{r}\mid0}{0\mid0}\right).
$$  

Since $(x_{j i})^{\mathrm{t}}$ and $(y_{j i})^{\mathrm{t}}$ are regular by Th. 7.22(a), we may use Th. 7.17(b) to obtain  

$$
\mathrm{rrk}(a_{j i})=\mathrm{rk}(a_{j i})^{\mathrm{t}}=\mathrm{rk}\left((y_{j i})^{\mathrm{t}}(a_{j i})^{\mathrm{t}}(x_{j i})^{\mathrm{t}}\right)=\mathrm{rk}\left(\left.\frac{\mathrm{Id}_{r}\mathrm{~\v~|~\v~0~}}{\mathrm{~0~\v~|~\v~0~}}\right)=r,
$$  

as desired.  

Remark 7.24. Let $V,W$ be finite-dimensional vector spaces over the field. $F^{\prime}$ $\dim V=n$ $\dim W=m$ , where $m,n\in\mathbb{N}$ . Moreover, let $B_{V}=(v_{1},\ldots,v_{n})$ and $B_{W}=(w_{1},\dots,w_{m})$ be ordered bases of $V$ and $W$ , respectively, let $A\in{\mathcal{L}}(V,W)$ , and let $(a_{j i})\in\mathcal{M}(m,n,F)$ be the matrix corresponding to. $A$ with respect to $B_{V}$ and $B_{W}$ . Using the transpose matrix $(a_{j i})^{\mathrm{t}}\in\mathcal{M}(n,m,F)$ , one can now also define a transpose. $A^{\mathrm{t}}$ of the map $A$ However, a subtlety arises related to basis transitions and, given $\lambda_{1},\dots,\lambda_{m}\in F$ , representing coordinates of $w\in W$ with respect to $B_{W}$ , one can not simply define. $A^{\mathrm{t}}$ by applying $(a_{j i})^{\mathrm{t}}$ to the column vector containing $\lambda_{1},\ldots,\lambda_{m}$ , as the result would, in general, depend on $B_{V}$ and $B_{W}$ . Instead, one obtains $A^{\mathrm{t}}$ by left-multiplying $(a_{j i})$ with the row vector containing $\lambda_{1},\ldots,\lambda_{m}$  

$$
A^{\operatorname{t}}w:=\left(\lambda_{1}\quad...\quad\lambda_{m}\right)(a_{j i}).
$$  

Even though the resulting coordinate values are the same that one obtains from computing $(a_{j i})^{\mathrm{t}}(\lambda_{1}~.~.~.~\lambda_{m})^{\mathrm{t}}$ , the difference appears when considering basis transitions. In. consequence, algebraically, one obtains the transpose. $A^{\mathrm{t}}$ to be a map from the dual $W^{\prime}$ of $W$ into the dual $V^{\prime}$ of $V$ . Here, we will not go into further details, as we do not want. to explain the concept of dual spaces at this time..  

### 7.4 Special Types of Matrices  

In the present section, we investigate types of matrices that posses particularly simple.   
structures, often, but not always, due to many entries being 0. For many of the sets that we introduce in the following, there does not seem to be a standard notation, at.   
least not within Linear Algebra. However, as these sets do appear very frequently, it.   
seems inconvenient and cumbersome not to introduce suitable notation..  

Definition 7.25. Let $n\in\mathbb{N}$ and let $S$ be a set containing elements denoted 0 and. $^{1}$ (usually, $S$ will be a ring with unity or even a field, but we want to emphasize that the present definition makes sense without any structure on the set $S$  

(a) We call a matrix $A=(a_{j i})\in\mathcal{M}(n,S)$ diagonal if, and only if, $a_{j i}=0$ for $j\neq i$ i.e. if, and only if, all nondiagonal entries of $A$ are $0$ . We define  

$$
\mathrm{D}_{n}(S):=\left\{A\in{\mathcal{M}}(n,S):A{\mathrm{~is~diagonal}}\right\}.
$$  

If $(s_{1},\ldots,s_{n})\in S^{n}$ , then we define  

$$
\mathrm{diag}(s_{1},\ldots,s_{n}):=D=(d_{j i})\in\mathrm{D}_{n}(S),\quad d_{j i}:=\left\{\begin{array}{l l}{s_{j}}&{\mathrm{for~}j=i,}\ {0}&{\mathrm{for~}j\not=i.}\end{array}\right.
$$  

(b) A matrix $A=(a_{j i})\in\mathcal{M}(n,S)$ is called upper triangular or right triangular (resp. lower triangular or left triangular) if, and only if, $a_{j i}=0$ for each $i,j\in\{1,\dots,n\}$ such that $j>i$ (resp. $j\mathrm{~<~}i$ ), i.e. if, and only if, all nonzero entries of $A$ are above/right (resp. below/left) of the diagonal. A triangular matrix $A$ is called strict if, and only if,. $a_{i i}=0$ for each $i\in\{1,\ldots,n\}$ ; it is called unipotent if, and only if, $a_{i i}=1$ for each $i\in\{1,\ldots,n\}$ .We define5  

$$
\begin{array}{r l}&{\mathrm{BU}_{n}(S):=\big\{A\in\mathcal{M}(n,S):A\mathrm{~is~upper~triangular}\big\},}\ &{\mathrm{BL}_{n}(S):=\big\{A\in\mathcal{M}(n,S):A\mathrm{~is~lower~triangular}\big\},}\ &{\mathrm{BU}_{n}^{0}(S):=\big\{A\in\mathcal{M}(n,S):A\mathrm{~is~strict~upper~triangular}\big\},}\ &{\mathrm{BL}_{n}^{0}(S):=\big\{A\in\mathcal{M}(n,S):A\mathrm{~is~strict~lower~triangular}\big\},}\ &{\mathrm{BU}_{n}^{1}(S):=\big\{A\in\mathrm{BU}_{n}(S):A\mathrm{~is~unipotent}\big\},}\ &{\mathrm{BL}_{n}^{1}(S):=\big\{A\in\mathrm{BL}_{n}(S):A\mathrm{~is~unipotent}\big\}.}\end{array}
$$  

(c) A matrix $A=(a_{j i})\in\mathcal{M}(n,S)$ is called symmetric if, and only if, $A^{\mathrm{t}}=A$ , i.e. if $a_{j i}=a_{i j}$ for each $i,j\in\{1,\dots,n\}$ .We define  

$$
\operatorname{Sym}_{n}(S):=\{A\in{\mathcal{M}}(n,S):A{\mathrm{~is~symmetric}}\}.
$$  

Proposition 7.26. Let $S$ be a ring and $m,n\in\mathbb{N}$ . Let $s_{1},\ldots,s_{m a x\{m,n\}}\in S$  

(a) Let $D_{1}:=\mathrm{diag}(s_{1},\ldots,s_{m})\in D_{m}(S)$ $D_{2}:=\mathrm{diag}(s_{1},\ldots,s_{n})\in D_{n}(S)$ $A=(a_{j i})\in$ $\mathcal{M}(\boldsymbol{m},\boldsymbol{n},S)$ . Then left multiplication of $A$ by $D_{1}$ multiplies the $j$ -th row of $A$ by $s_{j}$ right multiplication of $A$ by $D_{2}$ multiplies the $i$ -th column of $A$ by $s_{i}$  

$$
\begin{array}{r l}&{D_{1}A=\mathrm{diag}(s_{1},\ldots,s_{m})\left(\begin{array}{l}{r_{1}^{A}}\ {\vdots}\ {r_{m}^{A}}\end{array}\right)=\left(\begin{array}{l}{s_{1}r_{1}^{A}}\ {\vdots}\ {s_{m}r_{m}^{A}}\end{array}\right),}\ &{A D_{2}=\left(c_{1}^{A}\quad\ldots\quad c_{n}^{A}\right)\mathrm{diag}(s_{1},\ldots,s_{n})=\left(c_{1}^{A}s_{1}\quad\ldots\quad c_{n}^{A}s_{n}\right).}\end{array}
$$  

(b) $D_{n}(S)$ is a subring of. $\mathcal{M}(n,S)$ (subring with unity if $S$ is a ring with unity). If $S$ is a field, then. $D_{n}(S)$ is a vector subspace of $\mathcal{M}(n,S)$  

(c) If $S$ is a ring with unity, then $D:=\mathrm{diag}(s_{1},\ldots,s_{n})\in\mathrm{GL}_{n}(S)$ if, and only if, each $s_{i}$ is invertible, i.e. if, and only if, $s_{i}\in S^{*}$ for each $i\in\{1,\ldots,n\}$ . In that case, one has $D^{-1}=\operatorname{diag}(s_{1}^{-1},\ldots,s_{n}^{-1})\in\operatorname{GL}_{n}(S)$ . Moreover, $D_{n}(S^{*})=D_{n}(S)\cap{\mathrm{GL}}_{n}(S)$ is a subgroup of $\mathrm{GL}_{n}(S)$  

Proof. (a): If $(d_{j i}):=D_{1}$ $(e_{j i}):=D_{2}$ $(x_{j i}):=D_{1}A$ and $(y_{j i}):=A D_{2}$ , then, for each $(j,i)\in\{1,\dots,m\}\times\{1,\dots,n\}$  

$$
x_{j i}=\sum_{k=1}^{n}d_{j k}a_{k i}=s_{j}a_{j i},\quad y_{j i}=\sum_{k=1}^{m}a_{j k}e_{k i}=a_{j i}s_{i}.
$$  

(b): As a consequence of (a), we have, for $a_{1},\ldots,a_{n},b_{1},\ldots,b_{n}\in S$  

$$
\mathrm{diag}(a_{1},\ldots,a_{n})\mathrm{diag}(b_{1},\ldots,b_{n})=\mathrm{diag}(a_{1}b_{1},\ldots,a_{n}b_{n})\in D_{n}(S).
$$  

As $A,B\in D_{n}(S)$ , clearly, implies $A+B\in D_{n}(S)$ and $-A\in D_{n}(S)$ , we have shown $D_{n}(S)$ to be a subring of $\mathcal{M}(n,S)$ , where, if $1\in S$ , then $\mathrm{Id}_{n}\in D_{n}(S)$ .If $\lambda\in S$ $A\in D_{n}(S)$ , then, clearly, $\lambda A\in D_{n}(S)$ , showing that, for $S$ being a field, $D_{n}(S)$ is a vector subspace of $\mathcal{M}(n,S)$  

(c) follows from (7.28) and the fact that $(S^{*},\cdot)$ is a group according to Def. and Rem.   
4.41.  

Proposition 7.27. Let $S$ be a ring and. $n\in\mathbb N$ (a)Let $A:=(a_{j i})\in\mathcal{M}(n,S)$ and $\boldsymbol{B}:=(b_{j i})\in\mathcal{M}(n,S)$ .If $A,B\in\mathrm{BU}_{n}(S)$ or $A,B\in\mathrm{BL}_{n}(S)$ , and $C:=(c_{j i})=A B$ , then $c_{i i}=a_{i i}b_{i i}$ for each $i\in\{1,\ldots,n\}$  

(b) $\mathrm{BU}_{n}(S),\mathrm{BL}_{n}(S),\mathrm{BU}_{n}^{0}(S),\mathrm{BL}_{n}^{0}(S)$ are subrings of. $\mathcal{M}(n,S)$ $(\mathrm{BU}_{n}(S),\mathrm{BL}_{n}(S)$ are subrings with unity if $S$ is a ring with unity). If $S$ is a field, then. $\mathrm{BU}_{n}(S)$ $\mathrm{BL}_{n}(S)$ ${\mathrm{BU}}_{n}^{0}(S)$ $\operatorname{BL}_{n}^{0}(S)$ are vector subspaces of. $\mathcal{M}(n,S)$  

(c) Let $S$ be a ring with unity. If $B:=(b_{j i})\in\mathrm{BU}_{n}(S)\cap\mathrm{GL}_{n}(S)$ and $A:=(a_{j i})=B^{-1}$ then $A\in\operatorname{BU}_{n}(S)$ with  

$$
a_{j i}=\left\{\begin{array}{l l}{0}&{f o r i<j,}\ {b_{i i}^{-1}}&{f o r i=j,}\ {-\left(\sum_{k=1}^{i-1}a_{j k}b_{k i}\right)b_{i i}^{-1}}&{r e c u r s i v e l y f o r i>j.}\end{array}\right.
$$  

If $B:=(b_{j i})\in\mathrm{BL}_{n}(S)\cap\mathrm{GL}_{n}(S)$ and $A:=(a_{j i})=B^{-1}$ , then $A\in\mathrm{BL}_{n}(S)$ with  

$$
a_{j i}=\left\{\begin{array}{l l}{0}&{f o r j<i,}\ {b_{i i}^{-1}}&{f o r j=i,}\ {-\left(\sum_{k=i+1}^{j}a_{j k}b_{k i}\right)b_{i i}^{-1}}&{r e c u r s i v e l y f o r j>i.}\end{array}\right.
$$  

(d) If $S$ is a ring with unity and $A:=(a_{j i})\in\mathrm{BU}_{n}(S)\cup\mathrm{BL}_{n}(S)$ , then $A\in\operatorname{GL}_{n}(S)$ if, and only if, each $a_{i i}$ is invertible. Moreover, $\mathrm{BU}_{n}^{1}(S),\mathrm{BL}_{n}^{1}(S)$ as well as $\mathrm{BU}_{n}(S)\cap$ $\operatorname{GL}_{n}(S),\operatorname{BL}_{n}(S)\cap\operatorname{GL}_{n}(S)$ are subgroups of $\mathrm{GL}_{n}(S)$  

Proof. (a): For $A,B\in\mathrm{BU}_{n}(S)$ , we compute  

$$
c_{i i}=\sum_{k=1}^{i-1}\overbrace{a_{i k}}^{=0}b_{k i}+a_{i i}b_{i i}+\sum_{k=i+1}^{n}a_{i k}\overbrace{b_{k i}}^{=0}=a_{i i}b_{i i},
$$  

while, for $A,B\in\mathrm{BL}_{n}(S)$ , we compute  

$$
c_{i i}=\sum_{k=1}^{i-1}a_{i k}\overbrace{b_{k i}}^{=0}+a_{i i}b_{i i}+\sum_{k=i+1}^{n}\overbrace{a_{i k}}^{=0}b_{k i}=a_{i i}b_{i i}.
$$  

(b): Let $A,B\in\mathrm{BU}_{n}(S)$ and $C:=(c_{j i})=A B$ . We obtain $C\in\mathrm{BU}_{n}(S)$ , since, if $j>i$ then  

$$
c_{j i}=\sum_{k=1}^{i}a_{j k}b_{k i}+\sum_{k=i+1}^{n}a_{j k}b_{k i}=0
$$  

(the first sum equals. $0$ since $k\leq i<j$ and $A$ is upper triangular, the second sum equals $0$ since $k>i$ and $B$ is upper triangular). Now let $A,B\in\mathrm{BL}_{n}(S)$ and $C:=(c_{j i}):=A B$ We obtain $C\in\mathrm{BL}_{n}(S)$ , since, if. $j<i$ , then  

$$
c_{j i}=\sum_{k=1}^{i-1}a_{j k}b_{k i}+\sum_{k=i}^{n}a_{j k}b_{k i}=0
$$  

(the first sum equals. $0$ since $k<i$ and $B$ is lower triangular, the second sum equals $0$ since $j<i\leq k$ and $A$ is lower triangular). Now let. $\mathcal{M}\in\{\mathrm{BU}_{n}(S),\mathrm{BL}_{n}(S),\mathrm{BU}_{n}^{0}(S),\mathrm{BL}_{n}^{0}(S)\}$ Then the above and (a) show $A B\in{\mathcal{M}}$ for $A,B\in{\mathcal{M}}$ . As $A,B\in{\mathcal{M}}$ , clearly, implies $A+B\in{\mathcal{M}}$ and $-A\in{\mathcal{M}}$ , we have shown $\mathcal{M}$ to be a subring of. $\mathcal{M}(n,S)$ , where, if $1\in S$ , then $\mathrm{Id}_{n}\in\mathrm{BU}_{n}(S)\cap\mathrm{BL}_{n}(S)$ . If $\lambda\in S$ $A\in{\mathcal{M}}$ , then, clearly, $\lambda A\in{\mathcal{M}}$ , showing that, for $S$ being a field, $\mathcal{M}$ is a vector subspace of. $\mathcal{M}(n,S)$  

(c): If $B\in\mathrm{BU}_{n}(S)\cap\mathrm{GL}_{n}(S)$ , then each $b_{i i}$ is invertible by (a) and (b). Now let $A:=(a_{j i})$ be defined by (7.29a), $C:=(c_{j i}):=A B$ .We already know $C\in\mathrm{BU}_{n}(S)$ according to (b). Moreover,. $c_{i i}=1$ follows from (a) and, for $j<i$  

$$
c_{j i}=\sum_{k=j}^{i}a_{j k}b_{k i}=a_{j i}b_{i i}+\sum_{k=j}^{i-1}a_{j k}b_{k i}=0
$$  

by the recursive part of (7.29a), completing the proof of $C=\operatorname{Id}_{n}$ .If $B\in\mathrm{BL}_{n}(S)\cap$ $\mathrm{GL}_{n}(S)$ , then each. $b_{i i}$ is invertible by (a) and (b). Now let $A:=(a_{j i})$ be defined by. (7.29b), $C:=(c_{j i}):=A B$ . We already know $C\in\mathrm{BL}_{n}(S)$ according to (b). Moreover, $c_{i i}=1$ follows from (a) and, for $j>i$  

$$
c_{j i}=\sum_{k=i}^{j}a_{j k}b_{k i}=a_{j i}b_{i i}+\sum_{k=i+1}^{j}a_{j k}b_{k i}=0
$$  

by the recursive part of (7.29b), completing the proof of $C=\operatorname{Id}_{n}$  

(d) is now merely a corollary of suitable parts of (a),(b),(c).  

#### Example 7.28. Let  

$$
B:={\left(\begin{array}{l l l}{1}&{0}&{0}\ {4}&{2}&{0}\ {6}&{5}&{3}\end{array}\right)}~.
$$  

We use (7.29b) to compute $A:=(a_{j i})=B^{-1}$  

$$
\begin{array}{l}{{a_{11}=1,\quad a_{22}=\displaystyle\frac12,\quad a_{33}=\displaystyle\frac13,}}\ {{\mathrm{}}}\ {{a_{32}=-a_{33}b_{32}/b_{22}=-\displaystyle\frac53\cdot\displaystyle\frac12=-\displaystyle\frac56,}}\ {{\mathrm{}}}\ {{a_{21}=-a_{22}b_{21}/b_{11}=-\displaystyle\frac42=-2,}}\ {{\mathrm{}}}\ {{a_{31}=-\displaystyle\left(a_{32}b_{21}+a_{33}b_{31}\right)/b_{11}=-\left(-\displaystyle\frac{5\cdot4}6+\displaystyle\frac63\right)=\displaystyle\frac43.}}\end{array}
$$  

Thus,  

$$
A B={\left(\begin{array}{l l l}{1}&{0}&{0}\ {-2}&{{\frac{1}{2}}}&{0}\ {{\frac{4}{3}}}&{-{\frac{5}{6}}}&{{\frac{1}{3}}}\end{array}\right)}\cdot{\left(\begin{array}{l l l}{1}&{0}&{0}\ {4}&{2}&{0}\ {6}&{5}&{3}\end{array}\right)}={\left(\begin{array}{l l l}{1}&{0}&{0}\ {-2+{\frac{4}{2}}}&{1}&{0}\ {{\frac{4}{3}}-{\frac{5\cdot4}{6}}+{\frac{6}{3}}}&{-{\frac{5\cdot2}{6}}+{\frac{5}{3}}}&{1}\end{array}\right)}=\operatorname{Id}_{3}.
$$  

Proposition 7.29. Let $F^{\prime}$ be a field and. $n\in\mathbb N$  

(a) $\mathrm{Sym}_{n}(F)$ is a vector subspace of $\mathcal{M}(n,F)$  

(b) If $A\in\operatorname{Sym}_{n}(F)\cap\operatorname{GL}_{n}(F)$ , then $A^{-1}\in\operatorname{Sym}_{n}(F)\cap\operatorname{GL}_{n}(F)$  

Proof. (a): If. $A,B\in\mathrm{Sym}_{n}(F)$ and $\lambda\in F$ , then $(A+B)^{\mathrm{t}}=A^{\mathrm{t}}+B^{\mathrm{t}}=A+B$ and $(\lambda A)^{\mathrm{t}}=\lambda A^{\mathrm{t}}=\lambda A$ , showing. $A+B\in\operatorname{Sym}_{n}(F)$ and $\lambda A\in\operatorname{Sym}_{n}(F)$ , i.e. $\mathrm{Sym}_{n}(F)$ is a vector subspace of $\mathcal{M}(n,F)$  

(b): If $A\in\operatorname{Sym}_{n}(F)\cap\operatorname{GL}_{n}(F)$ , then $(A^{-1})^{\mathrm{t}}=(A^{\mathrm{t}})^{-1}=A^{-1}$ , proving $A^{-1}\in\operatorname{Sym}_{n}(F)\cap$ $\mathrm{GL}_{n}(F)$  

Definition 7.30. Let $S$ be a group,. $n\in\mathbb N$ $A\in{\mathcal{M}}(n,S)$  

(a) $A$ is called skew-symmetric if, and only if, $A^{\mathrm{t}}=-A$ . Define  

$$
\operatorname{Skew}_{n}(S):=\big\{A\in\mathcal{M}(n,S):A\mathrm{~is~skew\mathrm{-}s y m m e t r i c}\big\}.
$$  

(b) Assume $F:=S$ is a field with. $\operatorname{char}F\neq2$ (i.e. $2:=1+1\ne0$ in $F$ ). We then. call $A_{\mathrm{sym}}:={\textstyle\frac{1}{2}}(A+A^{\mathrm{t}})$ the symmetric part of $A$ and $A_{\mathrm{skew}}:={\textstyle\frac{1}{2}}(A-A^{\mathrm{t}})$ the skewsymmetric part of $A$  

Proposition 7.31. Let $F$ be a field,. $n\in\mathbb N$  

(a) $\operatorname{Skew}_{n}(F)$ is a vector subspace of $\mathcal{M}(n,F)$  

(b) If char $F\neq2$ , then $\operatorname{Skew}_{n}(F)\cap\operatorname{Sym}_{n}(F)=\{0\}$  

(c) If $A\in\operatorname{Skew}_{n}(F)\cap\operatorname{GL}_{n}(F)$ , then $A^{-1}\in\operatorname{Skew}_{n}(F)\cap\operatorname{GL}_{n}(F)^{6}$  

Proof. (a): If $A,B\in\operatorname{Skew}_{n}(F)$ and $\lambda\in F$ , then $(A+B)^{\mathrm{t}}=A^{\mathrm{t}}+B^{\mathrm{t}}=-A-B=$ $-(A+B)$ and $(\lambda A)^{\mathrm{t}}\:=\:\lambda A^{\mathrm{t}}\:=\:\lambda(-A)\:=\:-(\lambda A)$ , showing $A+B\in\operatorname{Skew}_{n}(F)$ and $\lambda A\in\operatorname{Skew}_{n}(F)$ , i.e. $\operatorname{Skew}_{n}(F)$ is a vector subspace of $\mathcal{M}(n,F)$  

(b): Let $A\in\operatorname{Skew}_{n}(F)\cap\operatorname{Sym}_{n}(F)$ . Then $-A=A^{\mathrm{t}}=A$ , i.e. $2A=0$ , implying $2=0$ or $A=0$ . Thus, char $F=2$ or $A=0$  

(c): If $A\in\operatorname{Skew}_{n}(F)\cap\operatorname{GL}_{n}(F)$ , then. $(A^{-1})^{\mathrm{t}}=(A^{\mathrm{t}})^{-1}=-A^{-1}$ , provinge $A^{-1}\in\mathbf{\Gamma}$ $\operatorname{Sym}_{n}(F)\cap\operatorname{GL}_{n}(F)$  

Proposition 7.32. Let $F$ be a field with char $F\neq2$ $n\in\mathbb N$ $A\in{\mathcal{M}}(n,F)$  

(a) The symmetric part $A_{\mathrm{sym}}={\textstyle\frac{1}{2}}(A+A^{\mathrm{t}})$ of $A$ is symmetric, the skew-symmetric part ${\cal A}_{\mathrm{skew}}={\textstyle\frac{1}{2}}(A-A^{\mathrm{t}})$ of $A$ is skew-symmetric.  

(b) $A$ can be uniquely decomposed into its symmetric and skew-symmetric parts, i.e. $A=A_{\mathrm{sym}}+A_{\mathrm{skew}}$ and, if $A=S+B$ with $S\in\operatorname{Sym}_{n}(F)$ and $B\in\operatorname{Skew}_{n}(F)$ , then $S=A_{\mathrm{sym}}$ and $B=A_{\mathrm{skew}}$  

(c) $A$ is symmetric if, and only if, $A=A_{\mathrm{sym}}$ $A$ is skew-symmetric if, and only if, $A=A_{\mathrm{skew}}$  

# 7 MATRICES  

Proof. (a): $A_{\mathrm{sym}}$ is symmetric due to  

$$
A_{\mathrm{sym}}^{\mathrm{t}}={\frac{1}{2}}(A+A^{\mathrm{t}})^{\mathrm{t}}={\frac{1}{2}}(A^{\mathrm{t}}+A)=A_{\mathrm{sym}}.
$$  

$A_{\mathrm{skew}}$ is skew-symmetric due to  

$$
A_{\mathrm{skew}}^{\mathrm{t}}=\frac12(A-A^{\mathrm{t}})^{\mathrm{t}}=\frac12(A^{\mathrm{t}}-A)=-A_{\mathrm{skew}}.
$$  

(b): While $A_{\mathrm{sym}}+A_{\mathrm{skew}}={\textstyle{\frac{1}{2}}}A+{\textstyle{\frac{1}{2}}}A^{\mathrm{t}}+{\textstyle{\frac{1}{2}}}A-{\textstyle{\frac{1}{2}}}A^{\mathrm{t}}=A$ is immediate; if $A=S+B$ with $S\in\operatorname{Sym}_{n}(F)$ and $B\in\operatorname{Skew}_{n}(F)$ , then  

$$
A_{\mathrm{sym}}+A_{\mathrm{skew}}=A=S+B\quad\Rightarrow\quad A_{\mathrm{sym}}-S=B-A_{\mathrm{skew}},
$$  

where $A_{\mathrm{sym}}\textrm{--}S\in\operatorname{Sym}_{n}(F)$ by Prop. 7.29(a) and $B-A_{\mathrm{skew}}\in\operatorname{Skew}_{n}(F)$ by Prop.   
7.31(a), showinge $A_{\mathrm{sym}}=S$ and $A_{\mathrm{skew}}=B$ by Prop. 7.31(b).  

(c): If $A=A_{\mathrm{sym}}$ , then $A$ is symmetric by (a); if $A=A_{\mathrm{skew}}$ , then $A$ is skew-symmetric by (b). If $A$ is symmetric, then $A_{\mathrm{skew}}=A-A_{\mathrm{sym}}\in\operatorname{Skew}_{n}(F)\cap\operatorname{Sym}_{n}(F)=\{0\}$ , showing $A=A_{\mathrm{sym}}$ . If $A$ is skew-symmetric, then $A_{\mathrm{sym}}=A-A_{\mathrm{skew}}\in\operatorname{Skew}_{n}(F)\cap\operatorname{Sym}_{n}(I$ )={0}, showing $A=A_{\mathrm{skew}}$  

### 7.5 Blockwise Matrix Multiplication  

It is sometimes useful that one can carry out matrix multiplication in a blockwise fashion,.   
i.e. by partitioning the entries of a matrix into submatrices and then performing a.   
matrix multiplication for new matrices that have the submatrices as their entries, see Th. 7.34 below. To formulate and proof Th. 7.34, we need to define matrices and their.   
multiplication, where the entries are allowed to be indexed by more general index sets:.  

Definition 7.33. Let. $S$ be a ring. Let $J,I$ be finite index sets,. $\#J,\#I\in\mathbb{N}$ . We then call each family $\left(\boldsymbol{a}_{j i}\right)_{(j,i)\in J\times I}$ in $S$ a $J\times I$ matrix over $S$ , denoting the set of all such. matrices by $\mathcal{M}(J,I,S)$ . If $K$ is another index set with $\#K\in\mathbb{N}$ , then, for each. $J\times K$ matrix $(a_{j i})$ and each $K\times I$ matrix $\left(b_{j i}\right)$ over $S$ , define the product.  

$$
(a_{j i})(b_{j i}):=\left(\sum_{k\in K}a_{j k}b_{k i}\right)_{(j,i)\in J\times I}.
$$  

Theorem 7.34. Let. $S$ be a ring. Let. $J,I,K$ be finite index sets,. $\#J,\#I,\#K\in\mathbb{N}$   
Now assume, we have disjoint partitions of $J,I,K$ into nonempty sets:.  

$$
J=\bigcup_{\alpha\in\{1,\ldots,M\}}J_{\alpha},\quad I=\bigcup_{\beta\in\{1,\ldots,N\}}I_{\beta},\quad K=\bigcup_{\gamma\in\{1,\ldots,L\}}K_{\gamma},
$$  

# 7 MATRICES  

where $M,N,L\in\mathbb{N}$  

$$
\begin{array}{r}{\underset{\alpha\in\{1,\ldots,M\}}{\forall}m_{\alpha}:=\#J_{\alpha}\in\mathbb{N},\quad\underset{\beta\in\{1,\ldots,N\}}{\forall}n_{\beta}:=\#I_{\beta}\in\mathbb{N},\quad\underset{\gamma\in\{1,\ldots,M\}}{\forall}l_{\gamma}:=\#K_{\gamma}\in\mathbb{N},}\end{array}
$$  

Let $A:=(a_{j i})$ be a $J\times K$ matrix over $S$ and let $B:=(b_{j i})$ be a $K\times I$ matrix over $S$ Define the following submatrices of $A$ and $B$ , respectively:  

$$
\begin{array}{r l r}&{}&{\underset{(\alpha,\gamma)\in\{1,\ldots,M\}\times\{1,\ldots,L\}}{\forall}A_{\alpha\gamma}:=(a_{j i})_{(j,i)\in J_{\alpha}\times K_{\gamma}},}\ &{}&{\underset{(\gamma,\beta)\in\{1,\ldots,L\}\times\{1,\ldots,N\}}{\forall}B_{\gamma\beta}:=(b_{j i})_{(j,i)\in K_{\gamma}\times I_{\beta}}.}\end{array}
$$  

Then, for each $(\alpha,\gamma,\beta)\in\{1,\dots,M\}\times\{1,\dots,L\}\times\{1,\dots,N\}$ $A_{\alpha\gamma}$ is a $J_{\alpha}\times K_{\gamma}$ matrix and $B_{\gamma\beta}$ is a $K_{\gamma}\times I_{\beta}$ matrix. Thus, we can define  

$$
(C_{\alpha\beta}):=(A_{\alpha\gamma})(B_{\gamma\beta}):=\left(\sum_{\gamma=1}^{L}A_{\alpha\gamma}B_{\gamma\beta}\right)_{(\alpha,\beta)\in\{1,\dots,M\}\times\{1,\dots,N\}}.
$$  

We claim that  

$$
C:=(c_{j i}):=A B=(C_{\alpha\beta})
$$  

in the sense that  

$$
\underset{(\alpha,\beta)\in\{1,\dots,M\}\times\{1,\dots,N\}}{\forall}\quad\underset{(j,i)\in J_{\alpha}\times I_{\beta}}{\forall}\quad c_{j i}=(C_{\alpha\beta})_{j i}.
$$  

Proof. Let $(\alpha,\beta)\in\{1,\dots,M\}\times\{1,\dots,N\}$ and $(j,i)\in J_{\alpha}\times I_{\beta}$ . Then, according to (7.32) and since $K$ is the disjoint union of the $K_{\gamma}$ , we have  

$$
(C_{\alpha\beta})_{j i}=\sum_{\gamma=1}^{L}\sum_{k\in K_{\gamma}}a_{j k}b_{k i}=\sum_{k\in K}a_{j k}b_{k i}=c_{j i},
$$  

proving (7.34) and the theorem.  

Example 7.35. Let $S$ be a ring with unity and $A,B,C,D\in{\mathrm{GL}}_{2}(S)$ . Then we can use Th. 7.34 to perform the following multiplication of a $4\times6$ matrix by a $6\times4$ matrix:  

$$
\left({\begin{array}{r r r}{A}&{B}&{0}\ {0}&{C}&{D}\end{array}}\right)\left({\begin{array}{c r}{A^{-1}}&{0}\ {B^{-1}}&{C^{-1}}\ {0}&{D^{-1}}\end{array}}\right)=\left({\begin{array}{c r}{2\operatorname{Id}_{2}}&{B C^{-1}}\ {C B^{-1}}&{2\operatorname{Id}_{2}}\end{array}}\right).
$$  

## 8 Linear Systems  

### 8.1 General Setting  

Let $F^{\prime}$ be a field. A linear equation over $F^{\prime}$ has the form.  

$$
\sum_{k=1}^{n}a_{k}x_{k}=b,
$$  

where $n\in\mathbb N$ $b\in F$ and the $a_{1},\ldots,a_{n}\in F$ are given; and one in interested in determin-. ing the "unknowns" $x_{1},\ldots,x_{n}\in F$ such that the equation holds. The equation is called linear, as. $b$ is desired to be a linear combination of the. $u_{1},\ldots,u_{n}$ . A linear system is now a finite set of linear equations that the. $x_{1},\ldots,x_{n}\in F$ need to satisfy simultaneously:  

$$
\sqcap_{j\in\{1,\ldots,m\}}\quad\sum_{k=1}^{n}a_{j k}x_{k}=b_{j},
$$  

where $m,n\in\mathbb{N}$ $b_{1},\dots,b_{m}\in F$ and the $a_{j i}\in F$ $j\in\{1,\dots,m\}$ $i\in\{1,\ldots,n\}$ are given. One observes that (8.1) can be concisely written as $A x=b$ , using matrix multiplication, giving rise to the following definition:  

Definition 8.1. Let $F^{\prime}$ be a field. Given a matrix $A\in\mathcal{M}(m,n,F)$ $m,n\in\mathbb{N}$ , and $b\in\mathcal{M}(m,1,F)\cong F^{m}$ , the equation  

$$
A x=b
$$  

is called a linear system for the unknown. $x\in\mathcal{M}(n,1,F)\cong F^{n}$ . The matrix one obtains. by adding $b$ as the $(n+1)\mathrm{th}$ column to $A$ is called the augmented matrix of the linear system. It is denoted by $(A|b)$ . The linear system (8.2) is called homogeneous for $b=0$ and inhomogeneous for $b\neq0$ . By  

$$
\mathcal{L}(A|b):=\{x\in F^{n}:A x=b\},
$$  

we denote the set of solutions to (8.2).  

Example 8.2. While linear systems arise from many applications, we merely provide a few examples, illustrating the importance of linear systems for problems from inside the subject of linear algebra.  

(a) Let $v_{1}:=(1,2,0,3)$ $v_{2}:=(0,3,2,1)$ $v_{3}:=(1,1,1,1)$ .The question if the set. $M:=\{v_{1},v_{2},v_{3}\}$ is a linearly dependent subset of $\mathbb{R}^{4}$ is equivalent to asking if there  

exist $x_{1},x_{2},x_{3}\in\mathbb{R}$ , not all $0$ , such that. $x_{1}v_{1}+x_{2}v_{2}+x_{3}v_{3}=0$ , which is equivalent. to the question if the linear system  

$$
\begin{array}{r r r r l}{x_{1}}&{}&{+}&{x_{3}}&{=}&{0}\ {2x_{1}}&{+}&{3x_{2}}&{+}&{x_{3}}&{=}&{0}\ &{}&{2x_{2}}&{+}&{x_{3}}&{=}&{0}\ {3x_{1}}&{+}&{x_{2}}&{+}&{x_{3}}&{=}&{0}\end{array}
$$  

has a solution. $x=(x_{1},x_{2},x_{3})\neq(0,0,0)$ . The linear system can be written as  

$$
{\left(\begin{array}{l l l}{1}&{0}&{1}\ {2}&{3}&{1}\ {0}&{2}&{1}\ {3}&{1}&{1}\end{array}\right)}{\left(\begin{array}{l}{x_{1}}\ {x_{2}}\ {x_{3}}\end{array}\right)}={\left(\begin{array}{l}{0}\ {0}\ {0}\ {0}\end{array}\right)}.
$$  

The augmented matrix of the linear system is  

$$
(A|b):=\left(\begin{array}{l l l l l}{{1}}&{{0}}&{{1}}&{{|}}&{{0}}\ {{2}}&{{3}}&{{1}}&{{|}}&{{0}}\ {{0}}&{{2}}&{{1}}&{{|}}&{{0}}\ {{3}}&{{1}}&{{1}}&{{|}}&{{0}}\end{array}\right).
$$  

(b) Let $b_{1}:=(1,2,2,1)$ . The question if. $b_{1}\in\langle\{v_{1},v_{2},v_{3}\}\rangle$ with $v_{1},v_{2},v_{3}$ as in (a) is equivalent to the question, whether the linear system  

$$
A x={\left(\begin{array}{l}{1}\ {2}\ {2}\ {1}\end{array}\right)},\quad A:={\left(\begin{array}{l l l}{1}&{0}&{1}\ {2}&{3}&{1}\ {0}&{2}&{1}\ {3}&{1}&{1}\end{array}\right)}
$$  

has a solution.  

(c) Let $n\in\mathbb N$ . The problem of finding an inverse to an $n\times n$ matrix $A\in\mathcal{M}(n,n,F)$ is equivalent to solving the. $n$ linear systems  

$$
A v_{1}=e_{1},\ldots,A v_{n}=e_{n},
$$  

where $e_{1},\ldots,e_{n}$ are the standard (column) basis vectors. Then the $v_{k}$ are obviously the column vectors of. $A^{-1}$  

### 8.2 Abstract Solution Theory  

Before describing in Sec. 8.3 below, how one can systematically determine the set of solutions to a linear system, we apply some of our general results from the theory of vector spaces, linear maps, and matrices to obtain criteria for the existence and uniqueness of solutions to linear systems.  

Remark 8.3. Let $F$ be a field and. $m,n\in\mathbb{N}$ .If $A\in\mathcal{M}(m,n,F)$ , then. $A$ can be interpreted as the linear map  

$$
L_{A}:F^{n}\longrightarrow F^{m},\quad L_{A}(x):=A x,
$$  

where $x\in F^{n}$ is identified with a column vector in $\mathcal{M}(n,1,F)$ and the column vector $A x\in\mathcal{M}(m,1,F)$ is identified with an element of $F^{\prime r n}$ . In view of this fact, given an $n$ -dimensional vector space $V$ over $F$ , an $m$ -dimensional vector space $W$ over $F^{\prime}$ , a linear map $L\in{\mathcal{L}}(V,W)$ , and $b\in W$ , we call  

$$
L x=b
$$  

a linear system or merely a linear equation for the unknown vector $x\in V$ and we write. $\mathcal{L}(L|b)$ for its set of solutions. If. $V=F^{n}$ $W=F^{\prime m}$ , and the the matrix $A\in\mathcal{M}(m,n,F)$ corresponds to $L$ with respect to the respective standard bases of. $F^{\mathit{\Pi}}$ and ${\cal{F}}^{\prime\prime\prime}$ (cf. Ex. $5.16(\mathrm{c})$ ), then (8.6) is identical to (8.2) and.  

$$
{\mathcal{L}}(A|b)={\mathcal{L}}(L|b)=L^{-1}\{b\},
$$  

i.e. the set of solutions is precisely the preimage of the set $\{b\}$ under $L$ . In consequence, we then have  

$$
\begin{array}{c}{{\mathcal{L}(A|0)=\mathcal{L}(L|0)=\ker L,}}\ {{\dim\ker L^{\mathrm{Th.}}\stackrel{\mathrm{6.8(a)}}{=}\dim F^{n}-\dim\mathrm{Im}L=n-\mathrm{rk}(A),}}\end{array}
$$  

and, more generally,  

$$
\begin{array}{r l}{b\notin\mathrm{Im}L\quad}&{\Rightarrow\quad\mathcal{L}(A|b)=\mathcal{L}(L|b)=\emptyset,}\ {b\in\mathrm{Im}L\quad}&{\stackrel{\mathrm{Th.4.20(f)}}{\Rightarrow}\underset{x_{0}\in\mathcal{L}(L|b)}{\forall}\mathcal{L}(A|b)=\mathcal{L}(L|b)=x_{0}+\ker L=x_{0}+\mathcal{L}(L|0).}\end{array}
$$  

One can also express (8.10b) by saying one obtains all solutions to the inhomogeneous system $L x=b$ by adding a particular solution of the inhomogeneous system to the set of all solutions to the homogeneous system $L x=0$  

Theorem 8.4 (Existence of Solutions). Let $F^{\prime}$ be a field and $m,n\in\mathbb{N}$ ,let $L\in$ $\mathcal{L}(F^{n},F^{m})$ , and let $A\in\mathcal{M}(m,n,F)$ correspond to $L$ with respect to the respective standard bases of $F^{n}$ and $F^{m}$  

(a) Given $b\in F^{m}$ , the following statements are equivalent:  

(i) ${\mathcal{L}}(A|b)={\mathcal{L}}(L|b)\neq\emptyset.$   
(ii) $b\in\operatorname{Im}L$   
(iii) $b\in\langle\{c_{1}^{A},\ldots,c_{n}^{A}\}\rangle$ , where the $c_{i}^{A}$ denote the column vectors of $A$   
(iv) $\operatorname{rk}(A)=\operatorname{rk}(A|b)$  

(b) The following statements are equivalent:  

(i) $\mathcal{L}(A|b)=\mathcal{L}(L|b)\neq\emptyset$ holds for each $b\in F^{m}$ (ii) $L$ is surjective.   
(iii) $\operatorname{rk}(A)=m$  

Proof. (a): (i) implies (ii) by (8.7). Since $A$ corresponds to $L$ with respect to the respective standard bases of $F^{\mathit{\Pi}}$ and $F^{\mathit{m}}$ , (ii) implies (i) by Lem. 7.5(a). (iii) implies (iv), since  

$$
\operatorname{rk}(A|b)=\dim\langle\{c_{1}^{A},\dots,c_{n}^{A},b\}\rangle\overset{\mathrm{(ii)}}{=}\dim\langle\{c_{1}^{A},\dots,c_{n}^{A}\}\rangle=\operatorname{rk}(A).
$$  

(iv) implies (i): If $\operatorname{rk}(A)=\operatorname{rk}(A|b)$ , then $b$ is linearly dependent on $c_{1}^{A},\ldots,c_{n}^{A}$ , which, by Lem. 7.5(a), yields the existence of $x\in F^{n}$ with $\begin{array}{r}{A x=\sum_{k=1}^{n}x_{k}c_{k}^{A}=b}\end{array}$  

(b): The equivalence between (i) and (ii) is merely the definition of $L$ being surjective. Moreover, the equivalences  

$\operatorname{rk}(A)=m\quad\Leftrightarrow\quad{\mathrm{dim~Im}}L=m\quad\Leftrightarrow\quad\operatorname{Im}L=F^{m}\quad\Leftrightarrow\quad L{\mathrm{~surjective}}$ prove the equivalence between (ii) and (iii).  

Theorem 8.5 (Uniqueness of Solutions). Consider the situation of Th. 8.4. Given $b\in\operatorname{Im}L$ , the following statements are equivalent:  

(i) $\#\mathcal{L}(A|b)=\#\mathcal{L}(L|b)=1$ , i.e. $L x=b$ has a unique solution.  

(ii) ${\mathcal{L}}(A|0)={\mathcal{L}}(L|0)=\{0\}$ , i.e. the homogeneous system $L x=0$ has only the so-called trivial solution $x=0$  

(iii) $\operatorname{rk}(A)=n.$  

Proof. Since $b\in\operatorname{Im}L$ , there exists $x_{0}\in F^{n}$ with $L(x_{0})=b$ , i.e. $x_{0}\in\mathcal{L}(L|b)$ "(i) $\Leftrightarrow$ (i)"': Since $\mathcal{L}(L|b)=x_{0}+\ker L$ by (8.10b), (i) is equivalent to $\mathcal{L}(A|0)=\ker\cal{L}=$ $\{0\}$  

"(ii) $\Leftrightarrow$ (iii)': According to Th. 6.8(a), we know $\operatorname{rk}(A)=\dim\operatorname{Im}L=\dim F^{n}-\dim\ker L=n-\dim\ker L.$  

Thus, $\mathcal{L}(A|0)=\ker L=\{0\}$ is equivalent to $\operatorname{rk}(A)=n$  

Corollary 8.6. Consider the situation of Th. 8.4 with $m=n$ .Then the following. statements are equivalent:  

(i) There exists. $b\in F^{n}$ such that $L x=b$ has a unique solution.  

(ii) $\mathcal{L}(A|b)=\mathcal{L}(L|b)\neq\emptyset$ holds for each $b\in F^{n}$ (iii) The homogeneous system $L x=0$ has only the so-called trivial solution $x=0$  

(iv) $\operatorname{rk}(A)=n$ (v) $A$ and $L$ are invertible.  

Proof. "(iii) $\Leftrightarrow$ (iv)": The equivalence is obtained by using. $b:=0$ in Th. 8.5.   
"(iii) $\Leftrightarrow$ (v)": Since $m=n$ $L$ is bijective if, and only if, it is injective by Th. 6.10.   
"(ii) $\Leftrightarrow$ (v)": Since $m=n$ $L$ is bijective if, and only if, it is surjective by Th. 6.10.   
"(i) $\Leftrightarrow$ (ii)' is another consequence of Th. 8.5..  

### 8.3 Finding Solutions  

While the results of Sec. 8.2 provide some valuable information regarding the solutions of linear systems, in general, they do not help much to solve concrete systems, especially, if the systems consist of many equations with many variables. To remedy this situation, in the present section, we will investigate methods to systematically solve linear systems.  

#### 8.3.1 Echelon Form, Back Substitution  

We recall from (8.1) and Def. 8.1 that, given a field $F$ and $m,n\in\mathbb{N}$ , we are considering linear systems  

$$
\sqcap_{j\in\{1,\ldots,m\}}\quad\sum_{k=1}^{n}a_{j k}x_{k}=b_{j},
$$  

which we can write in the form  

$$
A x=b
$$  

with $A=(a_{j i})\in\mathcal{M}(m,n,F)$ and $b\in\mathcal{M}(m,1,F)\cong F^{m}$ , where $x$ and $b$ are interpreted as column vectors, and. $(A|b)\in\mathcal{M}(m,n+1,F)$ , where $b$ is added as a last column to. $A$ , is called the augmented matrix of the linear system. The goal is to determine the set of solutions. ${\mathcal{L}}(A|b)=\{x\in F^{n}:A x=b\}$ . We first investigate a situation, where determining ${\mathcal{L}}(A|b)$ is particularly easy, namely where $(A|b)$ has so-called echelon form:  

Definition 8.7. Let. $S$ be a set with $0\in S$ and $A=(a_{j i})\in\mathcal{M}(m,n,S)$ $m,n\in\mathbb{N}$ . For each row, i.e. for each. $j\in\{1,\ldots,m\}$ , let $\nu(j)\in\{1,\ldots,n\}$ be the smallest index $k$ such that $a_{j k}\neq0$ and $\nu(j):=n+1$ if the $j$ th row consists entirely of zeros. Then. $A$ is said to be in (row) echelon form if, and only if, for each $j\in\{2,\ldots,n\}$ , one has $\nu(j)>\nu(j-1)$ or $\nu(j)=n+1$ . Thus, $A$ is in echelon form if, and only if, it looks as follows:  

$$
A=\left(\begin{array}{c c c c c c c c c c c}{0}&{\ldots}&{0}&{\boxed{}}&{*}&{*}&{*}&{*}&{\ldots}&{*}&{*}&{*}&{*}\ {0}&{\ldots}&{0}&{0}&{\ldots}&{0}&{\boxed{}}&{*}&{*}&{*}&{\ldots}&{*}&{*}\ {0}&{\ldots}&{0}&{0}&{\ldots}&{0}&{0}&{\ldots}&{0}&{\boxed{}}&{*}&{\ldots}&{*}\ {\vdots}&&&&&&&&&&{\vdots}\end{array}\right).
$$  

The first nonzero elements in each row are called pivot elements (in (8.11), the positions of the pivot elements are marked by squares. $\sqsubset$ ). The columns $c_{k}^{A}$ containing a pivot element are called pivot columns and. $k\in\{1,\ldots,n\}$ is then called a pivot index, an index $k\in\{1,\ldots,n\}$ that is not a pivot index is called a free index. Let. $I_{\mathrm{p}}^{A},I_{\mathrm{f}}^{A}\subseteq\{1,\dots,n\}$ denote the sets of pivot indices and free indices, respectively. If. $A$ represents a linear system, then the variables corresponding to pivot columns are called pivot variables. All remaining variables are called free variables..  

Example 8.8. The following matrix over $\mathbb{R}$ is in echelon form:  

$$
A:=\left({\begin{array}{c c c c c c c c c}{0}&{0}&{3}&{3}&{0}&{-1}&{0}&{3}\ {0}&{0}&{0}&{4}&{0}&{2}&{-3}&{2}\ {0}&{0}&{0}&{0}&{0}&{0}&{1}&{1}\end{array}}\right).
$$  

It remains in echelon form if one adds zero rows at the bottom. For the linear system $A x=b$ , the variables $x_{3},x_{4},x_{7}$ are pivot variables, whereas $x_{1},x_{2},x_{5},x_{6},x_{8}$ are free variables.  

Theorem 8.9. Let $F^{\prime}$ be a field and. $m,n\in\mathbb{N}$ . Let $A\in\mathcal{M}(m,n,F)$ $b\in\mathcal{M}(m,1,F)\cong$ $F^{r n}$ , and consider the linear system $A x=b$ . Assume the augmented matrix $(A|b)$ to be in echelon form.  

(a) Then the following statements are equivalent:  

(i) $A x=b$ has at least one solution, i.e.. $\mathcal{L}(A|b)\neq\emptyset$   
(ii) $\operatorname{rk}(A)=\operatorname{rk}(A|b)$   
(iii) The final column b in the augmented matrix $(A|b)$ contains no pivot elements (i.e. if there is a zero row in. $A$ , then the corresponding entry of b also van-. ishes).  

(b) Let $L_{A}:F^{n}\longrightarrow F^{m}$ be the linear map associated with $A$ according to Rem. 8.3. Noting $A$ to be in echelon form as well and using the notation from Def. 8.7, one has  

$$
\dim\ker L_{A}=\dim\mathcal{L}(A|0)=\#I_{\mathrm{f}}^{A},\quad\dim\operatorname{Im}L_{A}=\operatorname{rk}A=\#I_{\mathrm{p}}^{A},
$$  

i.e. the dimension of the kernel of $A$ is given by the number of free variables, whereas the dimension of the image of $A$ is given by the number of pivot variables.  

Proof. (a): The equivalence between (i) and (ii) was already shown in Th. 8.4.  

"(ii) $\Leftrightarrow$ (iii)" : As both $A$ and $(A|b)$ are in echelon form, their respective ranks are, clearly,. given by their respective number of nonzero rows. However, $A$ and $(A|b)$ have the same number of nonzero rows if, and only if,. $b$ contains no pivot elements.  

(b): As $A$ is in echelon form, its number of nonzero rows (i.e. its rank) is precisely the number of pivot indices, proving $\dim\operatorname{Im}L_{A}=\operatorname{rk}A=\#I_{\mathrm{p}}^{A}$ .Since $\#I_{\mathrm{p}}^{A}+\#I_{\mathrm{f}}^{A}=n=$ $\dim\ker L_{A}+\dim\operatorname{Im}L_{A}$ , the claimed $\dim\ker L_{A}=\#I_{\mathrm{f}}^{A}$ now also follows.  

If the augmented matrix $(A|b)$ of the linear system $A x=b$ is in echelon form and such that its final column $b$ contains no pivot element, then the linear system can be solved, using so-called back substitution: One obtains a parameterized representation of ${\mathcal{L}}(A|b)$ as follows: Starting at the bottom with the first nonzero row, one solves each row for the corresponding pivot variable, in each step substituting the expressions for pivot variables that were obtained in previous steps. The free variables are treated as parameters. A particular element of $\mathcal{L}(A|b)$ can be obtained by setting all free variables to 0. We now provide a precise formulation of this algorithm:  

Algorithm 8.10 (Back Substitution). Let $F^{\prime}$ be a field and $m,n\in\mathbb{N}$ .Let $0\neq A=$ $(a_{j i})\in\mathcal{M}(m,n,F)$ and $b\in\mathcal{M}(m,1,F)\cong F^{m}$ and consider the linear system. $A x=b$ Assume the augmented matrix. $(A|b)$ to be in echelon form and assume its final column $b$ to contain no pivot element. As before, let. $I_{\mathrm{p}}^{A},I_{\mathrm{f}}^{A}\subseteq\{1,\dots,n\}$ denote the sets of pivot. indices and free indices, respectively. Also note $I_{\mathrm{p}}^{A}\neq\emptyset$ , whereas $I_{\mathrm{f}}^{A}$ might be empty. Let $i_{1}<\cdots<i_{N}$ be an enumeration of the elements of. $I_{\mathrm{p}}^{A}$ , where $N\in\{1,\ldots,n\}$ . As $A$ has echelon form, for each $k\in\{1,\ldots,N\}$ $a_{k,i_{k}}$ is the pivot element occurring in pivot. column $c_{i_{k}}^{A}$ (i.e. the pivot element is in the $k$ -th row and this also implies $N\leq m$ :  

The algorithm of back substitution $7$ defines a family $\left(\alpha_{k l}\right)_{\left(k,l\right)\in J\times I}$ in $F^{\prime}$ $J:=I_{\mathrm{p}}^{A}$ $I:=$ $\{0\}\cup I_{\mathrm{f}}^{A}$ , such that.  

$$
\begin{array}{r l}{{\underset{k\in\{1,\ldots,N\}}{\forall}},\quad}&{{}\alpha_{i_{k}l}=0,}\ {{\underset{k\in\{1,\ldots,N\}}{\forall}}}&{{}\left(x_{i_{k}}=\alpha_{i_{k}0}+\underset{l\in I:l>i_{k}}{\sum}\alpha_{i_{k}l}x_{l}\quad\wedge\quad\alpha_{i_{k}0}=a_{k i_{k}}^{-1}b_{k}\right),}\end{array}
$$  

where, for $l>i_{k}$ , the $\alpha_{i_{k}l}$ are defined recursively over $k=N,\ldots,1$ as follows: Assuming $\alpha_{i_{j}l}$ have already been defined for each $j>k$ such that (8.12b) holds, solve the $k$ th equation of $A x=b$ for $x_{i_{k}}$  

$$
\sum_{i=i_{k}}^{n}a_{k i}x_{i}=b_{k}\qquad\Rightarrow\quad x_{i_{k}}=a_{k i_{k}}^{-1}b_{k}-a_{k i_{k}}^{-1}\sum_{i=i_{k}+1}^{n}a_{k i}x_{i}.
$$  

All variables $x_{i}$ in the last equation have indices. $i>i_{k}$ and, inductively, we use (8.12b) for $i_{j}>i_{k}$ to replace all pivot variables in this equation for $x_{i_{k}}$ . The resulting expression for $x_{i_{k}}$ has the form (8.12b) with $\alpha_{i_{k}l}\in{\cal F}$ , as desired.  

From $\left(\alpha_{k l}\right)$ , we now define column vectors  

$$
s:=\left(\begin{array}{c}{{s_{1}}}\ {{\vdots}}\ {{\cdot}}\ {{s_{n}}}\end{array}\right),\qquad\begin{array}{c}{{\forall}}\ {{i\in I_{\mathrm{f}}^{A}}}\end{array}v_{i}:=\left(\begin{array}{c}{{v_{1i}}}\ {{\vdots}}\ {{v_{n i}}}\end{array}\right),\qquad
$$  

where  

$$
\operatorname{\rho}_{\mathbf{\Sigma}\to\mathbf{\mathbf{\delta}}}s_{j}:={\left\{\begin{array}{l l}{\alpha_{i_{k}0}}&{{\mathrm{for~}}j=i_{k}\in I_{\mathrm{p}}^{A},}\ {0}&{{\mathrm{for~}}j\in I_{\mathrm{f}}^{A},}\end{array}\right.}\quad\quad{\forall}\quad\forall\quad\forall\quad\forall_{j}:={\left\{\begin{array}{l l}{\alpha_{i_{k}i}}&{{\mathrm{for~}}j=i_{k}\in I_{\mathrm{p}}^{A}}\ {1}&{{\mathrm{for~}}j=i,}\ {0}&{{\mathrm{for~}}j\in I_{\mathrm{f}}^{A}\setminus\{i_{k}\},}\end{array}\right.}
$$  

Theorem 8.11. Consider the situation of Alg. 8.10 and let $L_{A}:F^{n}\longrightarrow F^{m}$ be the linear map associated with. $A$ according to Rem. 8.3..  

(a) Let $x=(x_{1},\cdot\cdot\cdot,x_{n})^{\mathrm{t}}\in F^{n}$ be a column vector. Then $x\in{\mathcal{L}}(A|b)$ if, and only if, the $x_{i_{k}}$ $k\in\{1,\ldots,N\}$ , satisfy the recursion over $k=N,\ldots,1$ , given by (8.13) or, equivalently, by (8.12b). In particular, $x\in\ker L_{A}={\mathcal{L}}(A|0)$ if, and only if, the $x_{i_{k}}$ satisfy the respective recursion with $b_{1}=\cdots=b_{N}=0$  

(b) The set  

$$
B:=\{v_{i}:i\in I_{\mathrm{f}}^{A}\}
$$  

forms a basis of $\ker L_{A}=\mathcal{L}(A|0)$ and  

$$
\begin{array}{r}{\mathcal{L}(A|b)=s+\ker L_{A}.}\end{array}
$$  

Proof. (a) holds, as the implication in (8.13) is, clearly, an equivalence.  

(b): As we already know $\dim\ker L_{A}=\#I_{\mathrm{f}}^{A}$ from Th. 8.9(b), to verify $B$ is a basis of $\ker L_{A}$ , it suffices to show $B$ is linearly independent and $B\subseteq\ker L_{A}$ . If $I_{\mathrm{f}}^{A}=\varnothing$ , then there is nothing to prove. Otherwise, if $(\lambda_{i})_{i\in I_{\mathrm{f}}^{A}}$ is a family in $F$ such that  

$$
0=\sum_{i\in I_{\mathrm{f}}^{A}}\lambda_{i}v_{i},
$$  

then  

$$
\forall_{i\in I_{\mathrm{f}}^{A}}\quad0=\sum_{j\in I_{\mathrm{f}}^{A}}\lambda_{j}v_{j i}=\sum_{j\in I_{\mathrm{f}}^{A}}\lambda_{j}\delta_{j i}=\lambda_{i},
$$  

showing the linear independence of. $B$ .To show $B\subseteq\ker L_{A}$ , fix $i\in I_{\mathrm{f}}^{A}$ .To prove $v_{i}\in\ker L_{A}$ , according to (a), we need to show  

$$
\forall_{k\in\{1,\dots,N\}}\quad v_{i_{k}i}=\sum_{l\in I_{\mathrm{f}}^{A}:l>i_{k}}\alpha_{i_{k}l}v_{l i}.
$$  

Indeed, we have  

$$
v_{i_{k}i}=\alpha_{i_{k}i}=\sum_{l\in I_{\mathrm{f}}^{A}:l>i_{k}}\alpha_{i_{k}l}v_{l i}=\sum_{l\in I_{\mathrm{f}}^{A}:l>i_{k}}\alpha_{i_{k}l}\delta_{l i},
$$  

which holds, since, if $I_{k}:=\{l\in I_{\mathrm{f}}^{A}:l>i_{k}\}=\emptyset$ , then the sum is empty and, thus, 0 with $v_{i_{k}i}=0$ as well, due to $i<i_{k}$ , and, if $I_{k}\ne\emptyset$ , then, due to the Kronecker $\delta$ , the sum evaluates to $\alpha_{i_{k}i}$ as well. To prove (8.15), according to (8.10b), it suffices to show $s\in\mathcal{L}(A|b)$ and, by (a), this is equivalent to  

$$
\forall_{k\in\{1,\dots,N\}}\quad s_{i_{k}}=\alpha_{i_{k}0}+\sum_{l\in I_{\mathrm{f}}^{A}:l>i_{k}}\alpha_{i_{k}l}s_{l}.
$$  

However, the validity of these equations is immediate from the definition of $s$ , which, in particular, implies the sums to vanish ( $s_{l}=0$ for each $l\in{I}_{\mathrm{f}}^{A}$ $\vert$  

Example 8.12. Consider the linear system $A x=b$ , where  

$$
A:=\left(\begin{array}{l l l l l l}{1}&{2}&{-1}&{3}&{0}&{1}\ {0}&{0}&{1}&{1}&{-1}&{1}\ {0}&{0}&{0}&{0}&{1}&{1}\ {0}&{0}&{0}&{0}&{0}&{0}\end{array}\right)\in\mathcal{M}(4,6,\mathbb{R}),\quad b:=\left(\begin{array}{l}{1}\ {2}\ {3}\ {0}\end{array}\right)\in\mathbb{R}^{4}.
$$  

Since $(A|b)$ is in echelon form and $b$ does not have any pivot elements, the set of solutions.   
${\mathcal{L}}(A|b)$ is nonempty, and it can be obtained using back substitution according to Alg.   
8.10: Using the same notation as in Alg. 8.10, we have.  

$$
m=4,\quad n=6,\quad I_{\mathrm{p}}^{A}=\{1,3,5\},\quad N=3,\quad I_{\mathrm{f}}^{A}=\{2,4,6\}.
$$  

In particular, we have $I_{\mathrm{p}}^{A}=\{i_{1},i_{2},i_{3}\}$ with $i_{1}=1$ $i_{2}=3$ $i_{3}=5$ and the recursion for the $x_{i_{k}}$ $\alpha_{i_{k}l}$ is  

$$
\begin{array}{r l}&{x_{5}=3-x_{6},}\ &{x_{3}=2-x_{6}+x_{5}-x_{4}=5-2x_{6}-x_{4},}\ &{x_{1}=1-x_{6}-3x_{4}+x_{3}-2x_{2}=6-3x_{6}-4x_{4}-2x_{2}.}\end{array}
$$  

Thus, the $\alpha_{i_{k}l}$ are given by  

$$
\begin{array}{c c c c}{{\alpha_{50}=3,}}&{{\alpha_{52}=0,}}&{{\alpha_{54}=0,}}&{{\alpha_{56}=-1,}}\ {{\alpha_{30}=5,}}&{{\alpha_{32}=0,}}&{{\alpha_{34}=-1,}}&{{\alpha_{36}=-2,}}\ {{\alpha_{10}=6,}}&{{\alpha_{12}=-2,}}&{{\alpha_{14}=-4,}}&{{\alpha_{16}=-3,}}\end{array}
$$  

and, from Th. 8.11(b), we obtain  

$$
A|b)=s+\ker L_{A}=\left(\begin{array}{l}{6}\ {0}\ {5}\ {0}\ {3}\ {0}\end{array}\right)+\left\{x_{2}\left(\begin{array}{l}{-2}\ {1}\ {0}\ {0}\ {0}\ {0}\end{array}\right)+x_{4}\left(\begin{array}{l}{-4}\ {0}\ {-1}\ {1}\ {0}\ {0}\end{array}\right)+x_{6}\left(\begin{array}{l}{-3}\ {0}\ {-2}\ {0}\ {-1}\ {1}\end{array}\right):x_{2},x_{4},x_{6}\in\mathbb{R}^{3}.
$$  

#### 8.3.2 Elementary Row Operations, Variable Substitution  

As seen in the previous section, if the augmented matrix. $(A|b)$ of the linear system $A x=b$ is in echelon form, then the set of solutions can be obtained via back substitution.. Thus, it is desirable to transform the augmented matrix of a linear system into echelon form without changing the set of solutions. This can be accomplished in finitely many. steps by the so-called Gaussian elimination algorithm of Alg. 8.17 below (cf. Th. 8.19), using elementary row operations and variable substitutions, where variable substitutions actually turn out to constitute particular elementary row operations..  

Definition 8.13. Let $F^{\prime}$ be a field, $m,n\in\mathbb{N}$ , and $A\in\mathcal{M}(m,n,F)$ . Let $r_{1},\ldots,r_{m}$ denote the rows of. $A$ . The following three operations, which transform $A$ into another $m\times n$ matrix $A_{\mathrm{er}}$ over $F$ , are known as elementary row operations:.  

(a) Row Switching: Switching two rows $r_{i}$ and $r_{j}$ , where $i,j\in\{1,\dots,m\}$ (b) Row Multiplication: Replacing a row $r_{i}$ by some nonzero multiple $\lambda r_{i}$ of that row, $i\in\{1,\ldots,m\}$ $\lambda\in F\setminus\{0\}$  

c) Row Addition: Replacing a row $r_{i}$ by the sum. $r_{i}+\lambda r_{j}$ of that row and a multiple of another row,. $(i,j)\in\{1,\ldots,m\}^{2}$ $i\neq j$ $\lambda\in F$  

Definition and Remark 8.14. Let $F^{\prime}$ be a field. Consider a linear system  

$$
\sqcap_{j\in\{1,\ldots,m\}}\quad\sum_{k=1}^{n}a_{j k}x_{k}=b_{j},
$$  

where $m,n\in\mathbb{N}$ $b_{1},\ldots,b_{m}\in F$ ; and $a_{j i}\in F$ $j\in\{1,\ldots,m\}$ $i\in\{1,\ldots,n\}$ . For $a_{j i}\neq0$ , one has  

$$
x_{i}=a_{j i}^{-1}b_{j}-a_{j i}^{-1}\sum_{k=1,\atop k\neq i}^{n}a_{j k}x_{k},
$$  

and a variable substitution means replacing the $l$ th equation $\textstyle\sum_{k=1}^{n}a_{l k}x_{k}=b_{l}$ of the system by the equation, where the variable $x_{i}$ has been substituted using (8.16) with some $j\neq l$ , i.e. by the equation  

$$
\sum_{k=1}^{i-1}a_{l k}x_{k}+a_{l i}\left(a_{j i}^{-1}b_{j}-a_{j i}^{-1}\sum_{\underset{k\neq i}{k=1}}^{n}a_{j k}x_{k}\right)+\sum_{k=i+1}^{n}a_{l k}x_{k}=b_{l},
$$  

which, after combining the coefficients of the same variables, reads  

$$
\sum_{k=1}^{i-1}(a_{l k}-a_{l i}a_{j i}^{-1}a_{j k})x_{k}+0\cdot x_{i}+\sum_{k=i+1}^{n}(a_{l k}-a_{l i}a_{j i}^{-1}a_{j k})x_{k}=b_{l}-a_{l i}a_{j i}^{-1}b_{j}.
$$  

Comparing with Def. 8.13(c), we see that variable substitution is a particular case of row addition: One obtains (8.17) by replacing row $r_{l}$ of $(A|b)$ by the sum $r_{l}-a_{l i}a_{j i}^{-1}r_{j}$  

Theorem 8.15. Let $F^{\prime}$ be a field and $m,n\in\mathbb{N}$ .Let $A=(a_{j i})\in\mathcal{M}(m,n,F)$ and $b\in\mathcal{M}(m,1,F)\cong F^{m}$ and consider the linear system $A x=b$ . Applying elementary row. operations (and, in particular, variable substitutions as in Def. and Rem. 8.14) to the augmented matrix $(A|b)$ of the linear system. $A x=b$ does not change the system's set of. solutions, i.e. if $(A_{\mathrm{er}}|b_{\mathrm{er}})$ is the new matrix obtained from applying an elementary row. operation according to Def. 8.13 to. $(A|b)$ , then ${\mathcal{L}}(A|b)={\mathcal{L}}(A_{\mathrm{er}}|b_{\mathrm{er}})$  

Proof. For each of the three elementary row operations, it is immediate from the arithmetic laws holding in the field. $F$ that, for each. $x\in F^{n}$ , one has. $x\in\mathcal{L}(A|b)$ if, and. only if,. $x\in\mathcal{L}(A_{\mathrm{er}}|b_{\mathrm{er}})$ (where the inverse operation of row switching is merely switching. rows $r_{i}$ and $r_{j}$ again, the inverse operation of row multiplication by. $\lambda\in F\setminus\{0\}$ is row multiplication by. $\lambda^{-1}$ , and the inverse operation of row addition. $r_{i}\mapsto r_{i}+\lambda r_{j}$ $i\neq j$ , is $r_{i}\mapsto r_{i}-\lambda r_{j}$  

Corollary 8.16. Let $F$ be a field, $A=(a_{j i})\in\mathcal{M}(m,n,F)$ $m,n\in\mathbb{N}$ .Applying elementary row operations to $A$ does not change the rank of $A$ , i.e. if $A_{\mathrm{er}}$ is the new matrix obtained from applying an elementary row operation according to Def. 8.13 to $A$ then $\operatorname{rk}A=\operatorname{rk}A_{\mathrm{er}}$  

Proof. Let $L_{A}:F^{n}\longrightarrow F^{m}$ and $L_{A_{\mathrm{er}}}:F^{n}\longrightarrow F^{m}$ be the linear maps associated with $A$ and $A_{\mathrm{er}}$ , respectively, according to Rem. 8.3. According to Th. 8.15, we have $\ker L_{A}=\mathcal{L}(A|0)=\mathcal{L}(A_{\mathrm{er}}|0)=\ker L_{A_{\mathrm{er}}}$ .Thus, according to (8.9), we have $\operatorname{rk}A=$ n  dim ker LA = n - dim ker LAer = rk Aer.  

#### 8.3.3 Gaussian Elimination  

Algorithm 8.17 (Gaussian Elimination). Let $F$ be a field and $m,n\in\mathbb{N}$ .Let $A=$ $(a_{j i})\in\mathcal{M}(m,n,F)$ . The Gaussian elimination algorithm is the following procedure that, starting with $A$ , recursively applies elementary row operations of Def. 8.13:  

Let $A^{(1)}:=A$ $r(1):=1$ . For each $k\geq1$ , as long as $r(k)<m$ and $k\leq n$ , the Gaussian eliminatio alorithm transoms $A^{(k)}=(a_{j i}^{(k)})\in\mathcal{M}(m,n,F)$ into $A^{(k+1)}=(a_{j i}^{(k+1)})\in$ $\mathcal{M}(\boldsymbol{m},\boldsymbol{n},\boldsymbol{F})$ and $r(k)\in\mathbb{N}$ into $r(k+1)\in\mathbb{N}$ by performing precisely one of the following actionss:  

(a) If $a_{r(k),k}^{(k)}\neq0$ then, for each $i\in\{r(k)+1,\ldots,m\}$ , replace the $i$ th row by the $\imath$ row plus $-a_{i k}^{(k)}/a_{r(k),k}^{(k)}$ times the $r(k)$ th row?. Set $r(k+1):=r(k)+1$  

(b) If $a_{r(k),k}^{(k)}=0$ $i\in\{r(k)+1,\ldots,m\}$ such that $a_{i k}^{(k)}\neq0$ I the ome chooses such an. $i\in\{r(k)+1,\ldots,m\}$ and switches the. $i$ th with the $r(k)$ th row. One then proceeds as in (a).  

() If $a_{i k}^{(k)}=0$ for cach $i\in\{r(k),\ldots,m\}$ then set $A^{(k+1)}:=A^{(k)}$ and $r(k+1):=r(k)$  

Remark 8.18. Note that the Gaussian elimination algorithm of Alg. 8.17 stops after at most $n$ steps. Moreover, in its $k$ th step, it can only manipulate elements that have row number at least $r(k)$ and column number at least $k$ (the claim with respect to the column numbers follows since aj a( = 0 for each (i,j) E {r(k),.., m}  {1,.., k - 1}, cf. the proof of the following Th. 8.19).  

Theorem 8.19. Let $F$ be a field and $m,n\in\mathbb{N}$ .Let $A=(a_{j i})\in\mathcal{M}(m,n,F)$ .The Gaussian elimination algorithm of Alg. 8.17 yields a matrix $\tilde{A}\in\mathcal{M}(m,n,F)$ in echelon form. More precisely, if. $r(k)=m$ or $k=n+1$ , then $\tilde{A}:=A^{(k)}$ is in echelon form.. Moreover, $\operatorname{rk}\tilde{A}=\operatorname{rk}A$ and, if $A=\left(B|b\right)_{\cdot}$ and $\tilde{A}=(\tilde{B}|\tilde{b})$ represent the augmented matrices of the linear systems. $B x=b$ and $\tilde{B}x=\tilde{b}$ , respectively, then $\mathcal{L}(B|b)=\mathcal{L}(\tilde{B}|\tilde{b})$  

Proof. Let $N\in\{1,\ldots,n+1\}$ be the maximal $k$ occurring during the Gaussian elimina-. tion algorithm, i.e. $\stackrel{.}{A}:=A^{(N)}$ . To prove that $\tilde{A}$ is in echelon form, we show by induction on $k\in\{1,\ldots,N\}$ that the first $k-1$ columns of $A^{(k)}$ are in echelon form as well as the first $r(k)$ rows of $A^{(k)}$ with $a_{i j}^{(k)}=0$ for each $(i,j)\in\{r(k),\ldots,m\}\times\{1,\ldots,k-1\}$ . For $k=1$ , the assertion is trivially true. By induction, we assume the assertion for $k<N$ and prove it for $k+1$ (for $k=1$ , we do not assume anything). As already stated in. Rem. 8.18 above, the $k$ th step of Alg. 8.17 does not change the first. $r(k)-1$ rows of $A^{(k)}$ and it does not change the first $k-1$ columns of $A^{(k)}$ , since (by induction hypothesis) a() = 0 for each (i, j) E {r(k),.., m}  {1,.., k - 1}. Moreover, if we are in the case. of Alg. 8.17(a), then  

$$
\underset{i\in\{r(k)+1,\ldots,m\}}{\forall}\quad a_{i k}^{(k+1)}=a_{i k}^{(k)}-\frac{a_{i k}^{(k)}}{a_{r(k),k}^{(k)}}a_{r(k),k}^{(k)}=0.
$$  

In each case, after the application of (a), (b), or (c) of Alg. 8.17, q(k+1) = 0 for each $(i,j)\in\{r(k+1),\ldots,m\}\times\{1,\ldots,k\}$ . We have to show that the first $r(k+1)$ rows of $A^{(k+1)}$ are in echelon form. For Alg. 8.17(c), it is $r(k+1)=r(k)$ and there is nothing to prove. For Alg. 8.17(a),(b), we know $a_{r(k+1),j}^{(k+1)}=0$ for each $j\in\{1,\ldots,k\}$ , while $a_{r(k),k}^{(k+1)}\neq0$ I showing that the i s $r(k+1)$ $A^{(k+1)}$ are i cholon om in ech case. Thus, we know that the first $r(k+1)$ rows of $A^{(k+1)}$ are in echelon form, and all elements in the first $k$ columns of $A^{(k+1)}$ below row $r(k+1)$ are zero, showing that the first $k$ columns of $A^{(k+1)}$ are also in echelon form. As, at the end of the Gaussian elimination algorithm, $r(k)=m$ or $k=n+1$ , we have shown. $\tilde{A}$ to be in echelon form.. That $\operatorname{rk}\tilde{A}=\operatorname{rk}A$ is an immediate consequence of Cor. 8.16 combined with a simple induction. If $A=(B|b)$ and $\tilde{A}=(\tilde{B}|\tilde{b})$ represent the augmented matrices of the linear systems $B x=b$ and ${\tilde{B}}x={\dot{b}}$ , respectively, then. $\mathcal{L}(B|b)=\mathcal{L}(\tilde{B}|\dot{b})$ is an immediate consequence of Th. 8.15 combined with a simple induction.  

Remark 8.20. To avoid mistakes, especially when performing the Gaussian elimination algorithm manually, it is advisable to check the row sums after each step. It obviously suffices to consider how row sums are changed if (a) of Alg. 8.17 is carried out. Moreover, let $i\in\{r(k)+1,\ldots,m\}$ , as only rows with row numbers $i\in\{r(k)+1,\ldots,m\}$ can be Changed by (a) im the $k$ th step If $\begin{array}{r}{s_{i}^{(k)}=\sum_{j=1}^{n}a_{i j}^{(k)}}\end{array}$ a() is the sum of the ith row before (a) has been carried out in the $k$ th step, then  

$$
\begin{array}{c}{{s_{i}^{(k+1)}=\displaystyle\sum_{j=1}^{n}a_{i j}^{(k+1)}=\displaystyle\sum_{j=1}^{n}\left(a_{i j}^{(k)}-\frac{a_{i k}^{(k)}}{a_{r(k),k}^{(k)}}a_{r(k),j}^{(k)}\right)}}\ {{=s_{i}^{(k)}-\displaystyle\frac{a_{i k}^{(k)}}{a_{r(k),k}^{(k)}}s_{r(k)}^{(k)}}}\end{array}
$$  

must be the sum of the. $i$ th row after (a) has been carried out in the $k$ th step.  

Remark 8.21. Theorem 8.19 shows that the Gaussian elimination algorithm of Alg. 8.17 provides a reliable systematic way of solving linear systems (when combined with the back substitution Alg. 8.10). It has few simple rules, which make it easy to implement as computer code. However, the following Ex. 8.22 illustrates that Alg. 8.17 is not always the most efficient way to obtain a solution and, especially when solving small linear systems manually, it often makes sense to deviate from it. In the presence of roundoff errors, there can also be good reasons to deviate from Alg. 8.17, which are typically addressed in classes on Numerical Analysis (see, e.g. [Phi23, Sec. 5]).  

Example 8.22. Over the field $\mathbb{R}$ , consider the linear system.  

$$
A x={\left(\begin{array}{l l l}{6}&{0}&{1}\ {0}&{2}&{0}\ {1}&{-1}&{-1}\end{array}\right)}{\left(\begin{array}{l}{x_{1}}\ {x_{2}}\ {x_{3}}\end{array}\right)}={\left(\begin{array}{l}{4}\ {6}\ {0}\end{array}\right)}=:b,
$$  

which we can also write in the form  

$$
\begin{array}{r r r r r l}{{6}x_{1}}&{}&{+}&{x_{3}}&{=}&{4}\ &{}&{2x_{2}}&{}&{=}&{6}\ {x_{1}}&{-}&{x_{2}}&{-}&{x_{3}}&{=}&{0}\end{array}
$$  

One can quickly solve this linear system without making use of Alg. 8.17 and Alg.   
8.10: The second equation yields. $x_{2}=3$ , which, plugged into the third equation, yields.  

$x_{1}-x_{3}=3$ . Adding this to the first equation yields $7x_{1}=7$ , i.e. $x_{1}=1$ . Thus, the first equation then provides $x_{3}=4-6=-2$ and we obtain  

$$
\begin{array}{r}{\mathcal{L}(A|b)=\left\{\left(\begin{array}{l}{1}\ {3}\ {-2}\end{array}\right)\right\}.}\end{array}
$$  

To illustrate Alg. 8.17 and Alg. 8.10, we solve (8.19) once again, first using Alg. 8.17 to transform the system to echelon form, then using Alg. 8.10 to obtain the solution: For each $k\in\{1,2,3\}$ , we provide $(A^{(k)}|b^{(k)})$ $r(k)$ , and the row suons $s_{i}^{(k)}$ $i\in\{1,2,3\}$ :..  

$$
(A^{(1)}|b^{(1)}):=(A|b)=\left(\begin{array}{c c c}{{6}}&{{0}}&{{1}}\ {{0}}&{{2}}&{{0}}\ {{1}}&{{-1}}&{{-1}}\end{array}\right|\begin{array}{c}{{4}}\ {{6}}\ {{0}}\end{array}\right),\quad r(1):=1,
$$  

$$
s_{1}^{(1)}=11,\quad s_{2}^{(1)}=8,\quad s_{3}^{(1)}=-1.
$$  

For $k=2$ , we apply Alg. 8.10(a), where we replace the third row of $\left(A^{(1)}|b^{(1)}\right)$ by the third row plus. $\left(-{\frac{1}{6}}\right)$ times the first row to obtain.  

$$
(A^{(2)}|b^{(2)}):=\left(\begin{array}{c c c}{{6}}&{{0}}&{{1}}\ {{0}}&{{2}}&{{0}}\ {{0}}&{{-1}}&{{-\frac{7}{6}}}\end{array}\right)\begin{array}{c c c}{{4}}\ {{6}}\ {{-\frac{2}{3}}}\end{array}\right),\quad r(2):=r(1)+1=2,
$$  

$$
s_{1}^{(2)}=11,\quad s_{2}^{(2)}=8,\quad s_{3}^{(2)}=s_{3}^{(1)}-\frac{1}{6}\cdot s_{1}^{(1)}=-1-\frac{11}{6}=-\frac{17}{6}.
$$  

For $k=3$ , we apply Alg. 8.10(a) again, where we replace the third row of $(A^{(2)}|b^{(2)})$ by the third row plus $\frac{1}{2}$ times the second row to obtain  

$$
(A^{(3)}|b^{(3)}):=\left(\begin{array}{c c c}{{6}}&{{0}}&{{1}}\ {{0}}&{{2}}&{{0}}\ {{0}}&{{0}}&{{-\frac{7}{6}}}\end{array}\right)\frac{4}{3}~r(3):=r(2)+1=3,
$$  

$$
s_{1}^{(3)}=11,\quad s_{2}^{(3)}=8,\quad s_{3}^{(3)}=s_{3}^{(2)}+\frac{1}{2}\cdot s_{2}^{(2)}=-\frac{17}{6}+4=\frac{7}{6}.
$$  

Since $r(3)=3$ , Alg. 8.10 is done and $(\tilde{A}|\tilde{b}):=\left(A^{(3)}|b^{(3)}\right)$ is in echelon formto. In particular, we see. $3=\operatorname{rk}{\tilde{A}}=\operatorname{rk}({\tilde{A}}|{\tilde{b}})=\operatorname{rk}(A|b)$ , i.e. $A x=b$ has a unique solution, which we now determine via the back substitution Alg. 8.10: We obtain  

$$
x_{3}=-\frac{7}{3}\cdot\frac{6}{7}=-2,\quad x_{2}=\frac{6}{2}=3,\quad x_{1}=\frac{1}{6}\left(4-x_{3}\right)=1,
$$  

recovering (8.20)11  

Example 8.23. (a) In Ex. 8.2(b), we saw that, in $\mathbb{R}^{4}$ , the question if $b\in\langle v_{1},v_{2},v_{3}\rangle$ with $b:=(1,2,2,1)$ and $v_{1}:=(1,2,0,3)$ $v_{2}:=(0,3,2,1)$ $v_{3}:=(1,1,1,1)$ is equivalent to determining if the linear system $A x=b$ with augmented matrix  

$$
(A|b):={\left(\begin{array}{l l l l l}{1}&{0}&{1}&{|}&{1}\ {2}&{3}&{1}&{|}&{2}\ {0}&{2}&{1}&{|}&{2}\ {3}&{1}&{1}&{|}&{1}\end{array}\right)}
$$  

has a solution. Let us answer this question by transforming the system to echelon form via elementary row operations: Replacing the 2nd row by the 2nd row plus $(-2)$ times the 1st row, and replacing the 4th row by the 4th row plus $(-3)$ times the 1st row yields  

$$
\left(\begin{array}{c c c c c}{{1}}&{{0}}&{{1}}&{{|}}&{{0}}\ {{0}}&{{3}}&{{-1}}&{{|}}&{{0}}\ {{0}}&{{2}}&{{1}}&{{|}}&{{2}}\ {{0}}&{{1}}&{{-2}}&{{|}}&{{-2}}\end{array}\right).
$$  

Switching rows 2 and 4 yields  

$$
\left(\begin{array}{c c c c c}{{1}}&{{0}}&{{1}}&{{|}}&{{0}}\ {{0}}&{{1}}&{{-2}}&{{|}}&{{-2}}\ {{0}}&{{2}}&{{1}}&{{|}}&{{2}}\ {{0}}&{{3}}&{{-1}}&{{|}}&{{0}}\end{array}\right).
$$  

Replacing the 3rd row by the 3rd row plus $(-2)$ times the 2nd row, and replacing the 4th row by the 4th row plus $(-3)$ times the 2nd row yields  

$$
\left(\begin{array}{c c c c c}{{1}}&{{0}}&{{1}}&{{\mid}}&{{0}}\ {{0}}&{{1}}&{{-2}}&{{\mid}}&{{-2}}\ {{0}}&{{0}}&{{5}}&{{\mid}}&{{6}}\ {{0}}&{{0}}&{{5}}&{{\mid}}&{{6}}\end{array}\right).
$$  

Replacing the 4th row by the 4th row plus $(-1)$ times the 3rd row yields.  

$$
(\tilde{A}|\tilde{b}):=\left(\begin{array}{c c c c c}{{1}}&{{0}}&{{1}}&{{|}}&{{0}}\ {{0}}&{{1}}&{{-2}}&{{|}}&{{-2}}\ {{0}}&{{0}}&{{5}}&{{|}}&{{6}}\ {{0}}&{{0}}&{{0}}&{{|}}&{{0}}\end{array}\right).
$$  

Thus, $3=\operatorname{rk}A=\operatorname{rk}{\tilde{A}}=\operatorname{rk}({\tilde{A}}|{\tilde{b}})=\operatorname{rk}(A|b)$ , showing $A x=b$ to have a unique solution and $b\in\langle v_{1},v_{2},v_{3}\rangle$  

(b) In Ex. 8.2(a), we saw that the question, if the set $M:=\{v_{1},v_{2},v_{3}\}$ with $v_{1},v_{2},v_{3}$ as in (a) is a linearly dependent subset of $\mathbb{R}^{4}$ , can be equivalently posed as the question, if the linear system $A x=0$ , with the same matrix $A$ as in (a), has a solution $x=(x_{1},x_{2},x_{3})\neq(0,0,0)$ . From (a), we know $\operatorname{rk}A=\operatorname{rk}\tilde{A}=3$ , implying ${\mathcal{L}}(A|0)=\left\{0\right\}$ and $M$ is linearly independent.  

### 8.4 LU Decomposition  

#### 8.4.1 Definition and Motivation  

If one needs to solve linear systems $A x=b$ with the same matrix. $A$ , but varying $b$ (as, e.g., in the problem of finding an inverse to an $n\times n$ matrix $A$ , cf. Ex. 8.2(c)), then it is not efficient to separately transform each $(A|b)$ into echelon form. A more efficient way aims at decomposing. $A$ into simpler matrices $L$ and $U$ , i.e. $A=L U$ , then facilitating the simpler solution of $\boldsymbol{A}\boldsymbol{x}=\boldsymbol{L}\boldsymbol{U}\boldsymbol{x}=\boldsymbol{b}$ when varying. $b$ (i.e. without having to transform $(A|b)$ into echelon form for each new $b$ ), cf. Rem. 8.25 below.  

Definition 8.24. Let $S$ be a ring with unity and $A\in\mathcal{M}(m,n,S)$ with $m,n\in\mathbb{N}$ . A decomposition  

$$
A=L\tilde{A}
$$  

is called an $L U$ decomposition of $A$ if, and only if,. $L\in\mathrm{BL}_{m}^{1}(S)$ (i.e. $L$ is unipotent lower. triangular) and. $\tilde{A}\in\mathcal{M}(m,n,S)$ is in echelon form. If $A$ is an $m\times m$ matrix, then $\tilde{A}\in\mathrm{BU}_{m}(S)$ (i.e. $\tilde{A}$ is upper triangular) and (8.21a) is an $L U$ decomposition in the. strict sense, which is emphasized by writing $U:=\tilde{A}$  

$$
A=L U.
$$  

Remark 8.25. Let $F^{\prime}$ be a field. Suppose the goal is to solve linear systems $A x=b$ with fixed matrix. $A\in\mathcal{M}(m,n,F)$ and varying vector. $b\in F^{n}$ . Moreover, suppose one knows an LU decomposition. $A=L\tilde{A}$ . Thens  

$$
x\in\mathcal{L}(A|b)\quad\Leftrightarrow\quad A x=L\tilde{A}x=b\quad\Leftrightarrow\quad\tilde{A}x=L^{-1}b\quad\Leftrightarrow\quad x\in\mathcal{L}(\tilde{A}|L^{-1}b).
$$  

Thus, solving. $A x=L{\ddot{A}}x=b$ is equivalent to solving solving. $\mathit{L z}=\mathit{b}$ for $\mathcal{Z}$ and then solving $\tilde{A}x=z=L^{-1}b$ for $x$ . Since $\tilde{A}$ is in echelon form,. $\tilde{A}x=z=L^{-1}b$ can be solved via the back substitution Alg. 8.10; and, since $L$ is lower triangular,. $\mathit{L z}=\mathit{b}$ can be solved via an analogous version of Alg. 8.10, called forward substitution12. To obtain the entire set ${\mathcal{L}}(A|b)$ , one uses $\mathcal{L}(A|0)=\mathcal{L}(\tilde{A}|0)$ and $\mathcal{L}(A|b)=x_{0}+\mathcal{L}(A|0)$ for each $x_{0}\in\mathcal{L}(A|b)$ , where one finds $x_{0}$ as described above and $\mathcal{L}(\ddot{A}|0)$ via the back substitution Alg. 8.10. Even though the described strategy works fine in many situations, it can fail in the presence of roundoff errors (we will come back to this issue in Rem. 8.36 below).  

Example 8.26. Unfortunately, not every matrix has an LU decomposition: Consider, for example  

$$
A=(a_{j i}):={\binom{0}{1}}\in\mathcal{M}(2,2,\mathbb{R}).
$$  

Clearly, $\operatorname{rk}A=2$ , i.e. $A$ is regular. Suppose, $A$ has an LU decomposition, i.e. $A=L U$ with $L=(l_{j i})$ unipotent lower triangular and $U=\left(u_{j i}\right)$ upper triangular. But then $0=a_{11}=l_{11}u_{11}=u_{11}$ , showing the first column of $U$ to be $0$ , i.e. $U$ is singular, in contradiction to $A$ being regular.  

Even though the previous example shows not every matrix has an LU decomposition, we will see in Th. 8.34 below that every matrix does have an LU decomposition, provided one is first allowed to permute its rows in a suitable manner..  

#### 8.4.2 Elementary Row Operations Via Matrix Multiplication  

The LU decomposition of Th. 8.34 below can be obtained, with virtually no extra effort, by performing the Gaussian elimination Alg. 8.17. The proof will be founded on the observation that each elementary row operation can be accomplished via left multiplication with a suitable matrix: For row multiplication, one multiplies from the left with a diagonal matrix, for row addition, one multiplies from the left with a socalled Frobenius matrix or with the transpose of such a matrix (cf. Cor. 8.29 below); for row switching, one multiplies from the left with a so-called permutation matrix (cf. Cor. 8.33(a) below) - where, for Alg. 8.17 and the proof of Th. 8.34, we only need row switching and row addition by means of a Frobenius matrix (not its transpose).  

Definition 8.27. Let $n\in\mathbb N$ and let $S$ be a ring with unity. We call a unipotent lower triangular matrix $A=(a_{j i})\in\mathrm{BL}_{n}^{1}(S)$ a Frobenius matrix of index $k$ $k\in\{1,\ldots,n\}$ , if, and only if, $a_{j i}=0$ for each $i\notin\{j,k\}$ , i.e. if, and only if, it has the following form:  

$$
A=\left(\begin{array}{c c c c c c}{1}&&&&&\ &{.}&&&&\ &&{.}&&&&\ &&{1}&&&&\ &{a_{k+1,k}}&{1}&&&\ &{a_{k+2,k}}&&{1}&&\ &{\vdots}&&&{.}&\ &{a_{n,k}}&&&&{1}\end{array}\right).
$$  

We define  

$$
\operatorname{Fro}_{n}^{k}(S):=\big\{A\in\mathcal{M}(n,S):A\mathrm{~is~}\operatorname{Frobenius~of~index~}k\big\}.
$$  

Proposition 8.28. Let $S$ be a ring with unity, $n\in\mathbb N$  

(a) If $m\in\mathbb{N}$ $A=(a_{j i})\in\mathcal{M}(m,n,S),B=(b_{j i})\in\mathrm{Fro}_{m}^{k}(S),k\in\{1,\dots,m\},$  

$$
\boldsymbol{B}=\left(\begin{array}{c c c c c c}{1}&&&&&\ &{\ddots}&&&&\ &&{1}&&&\ &&{b_{k+1,k}}&{1}&&\ &{b_{k+2,k}}&{1}&&\ &{\vdots}&&&{\ddots}&\ &&{b_{m,k}}&&&{1}\end{array}\right),
$$  

and $C=(c_{j i})=B A\in\mathcal{M}(m,n,S)$ , then  

$$
c_{j i}=\sum_{\alpha=1}^{m}b_{j\alpha}a_{\alpha i}=\left\{{a_{j i}}\atop{b_{j k}a_{k i}+a_{j i}}}{f o r e a c h j\in\{1,\ldots,k\}},\right.
$$  

(b) Let $F:=S$ be a field and $A=(a_{j i})\in\mathcal{M}(m,n,F)$ $m\in\mathbb{N}$ .Moreover, let $A^{(k)}\mapsto A^{(k+1)}$ be the matrix transformation occurring in the kth step of the Gaussian. elimination Alg. 8.17 and assume the kth step is being performed by Alg. 8.17(a), i.e. by, for each $i\in\{r(k)+1,\ldots,m\}$ , replacing the ith row by the ith row plus. -ak/ar(k), times the r(k)th row, then  

$$
A^{(k+1)}=L_{k}A^{(k)},\quad L_{k}\in\operatorname{Fro}_{m}^{r(k)}(F),
$$  

where  

$$
L_{k}=\left(\begin{array}{c c c c c c}{{1}}&{{}}&{{}}&{{}}&{{}}&{{}}&{{}}\ {{}}&{{\ddots}}&{{}}&{{}}&{{}}&{{}}&{{}}\ {{}}&{{}}&{{1}}&{{}}&{{}}&{{}}&{{}}\ {{}}&{{}}&{{-l_{r(k)+1,r(k)}}}&{{1}}&{{}}&{{}}&{{}}\ {{}}&{{}}&{{-l_{r(k)+2,r(k)}}}&{{}}&{{1}}&{{}}\ {{}}&{{}}&{{}}&{{}}&{{}}&{{\ddots}}\ {{}}&{{}}&{{}}&{{}}&{{}}&{{1}}\end{array}\right),\quad l_{i,r(k)}:=a_{i k}^{(k)}/a_{r(k),k}^{(k)}.
$$  

(c) Let $k\in\{1,\ldots,n\}$ . If $L=(l_{j i})\in\mathrm{Fro}_{n}^{k}(S)$ , then $L^{-1}\in\mathrm{Fro}_{n}^{k}(S)$ . More precisely,  

$$
L=\left(\begin{array}{c c c c c c}{{1}}&{{}}&{{}}&{{}}&{{}}&{{}}&{{}}\ {{}}&{{\ddots}}&{{}}&{{}}&{{}}&{{}}\ {{}}&{{}}&{{1}}&{{}}&{{}}&{{}}\ {{}}&{{}}&{{l_{k+1,k}}}&{{1}}&{{}}&{{}}\ {{}}&{{}}&{{l_{k+2,k}}}&{{}}&{{1}}&{{}}\ {{}}&{{}}&{{\vdots}}&{{}}&{{\ddots}}&{{}}\ {{}}&{{}}&{{l_{n,k}}}&{{}}&{{}}&{{1}}\end{array}\right)\Rightarrow L^{-1}=\left(\begin{array}{c c c c c c}{{1}}&{{}}&{{}}&{{}}&{{}}&{{}}\ {{}}&{{\ddots}}&{{}}&{{}}&{{}}&{{}}\ {{}}&{{}}&{{1}}&{{}}&{{}}&{{}}\ {{}}&{{}}&{{-l_{k+1,k}}}&{{1}}&{{}}&{{}}\ {{}}&{{}}&{{-l_{k+2,k}}}&{{1}}&{{}}&{{}}\ {{}}&{{}}&{{\vdots}}&{{}}&{{\ddots}}\ {{}}&{{}}&{{}}&{{-l_{n,k}}}&{{1}}\end{array}\right)
$$  

(d) If  

$$
L=(l_{j i})=\left(\begin{array}{l l l l}{1}&{0}&{\dots}&{0}\ {l_{21}}&{1}&{\dots}&{0}\ {\vdots}&{\vdots}&{\ddots}&{\vdots}\ {l_{n1}}&{l_{n2}}&{\dots}&{1}\end{array}\right)\in\mathrm{BL}_{n}^{1}(S)
$$  

is an arbitrary unipotent lower triangular matrix, then it is the product of the following $n-1$ Frobenius matrices:  

$$
\boldsymbol{L}=\tilde{L}_{1}\cdot\cdot\cdot\tilde{L}_{n-1},
$$  

where  

$$
\mathbf{\Psi}_{k}:=\left(\begin{array}{c c c c c c}{1}&&&&&\ &{\ddots}&&&&\ &&{1}&&&\ &&{l_{k+1,k}}&{1}&&\ &&{l_{k+2,k}}&{1}&&\ &&{\vdots}&&&{\ddots}&\ &&&&&{1}\end{array}\right)\in\mathrm{Fro}_{n}^{k}(S)\quad f o r e a c h k\in\{1,\ldots,n-1\}.
$$  

Proof. (a): Formula (8.24) is immediate from the definition of matrix multiplication.  

(b) follows by applying (a) with $B:=L_{k}$ and $A:=A^{(k)}$  

(c): Applying (a) with. $A:=L$ and $B:=L^{-1}$ , where $L^{-1}$ is defined as in the statement. of (c), we can use (8.24) to compute $C=B A$  

$$
\mathbf{\Sigma}_{j i}\mathbf{\Sigma}\overset{(\mathrm{s.~2.~})}{=}\left\{\begin{array}{l l}{a_{j i}=\left\{\begin{array}{l l}{0}&{\mathrm{for~each~}j\in\{1,\ldots,k\},i\neq j,}\ {1}&{\mathrm{for~each~}j\in\{1,\ldots,k\},i=j,}\end{array}\right.}\ {b_{j k}a_{k i}+a_{j i}=\left\{\begin{array}{l l}{-l_{j k}\cdot0+0=0}&{\mathrm{for~each~}j\in\{k+1,\ldots,n\},i\neq j,k}\ {-l_{j k}\cdot1+l_{j k}=0}&{\mathrm{for~each~}j\in\{k+1,\ldots,n\},i=k,}\ {-l_{j k}\cdot0+1=1}&{\mathrm{for~each~}j\in\{k+1,\ldots,n\},i=j,}\end{array}\right.}\end{array}\right.
$$  

showing $C=\mathrm{Id}$ , thereby establishing the case.  

(d): We proof by induction on $k=n-1,\ldots,1$ that  

$$
\prod_{\alpha=k}^{n-1}\tilde{L}_{\alpha}=\left(\begin{array}{l l l l l l}{1}&&&&&\ {0}&{\ddots}&&&&\ {\vdots}&{\ddots}&{1}&&&&\ {0}&{0}&{1}&&&\ {0}&{0}&{l_{k+1,k}}&{\ddots}&&\ {0}&{0}&{l_{k+2,k}}&{\ddots}&{1}&\ {\vdots}&{\ldots}&{\vdots}&{\vdots}&{\ddots}&{l_{n-1,n-2}}&{1}\ {0}&{\ldots}&{0}&{l_{n k}}&{\ldots}&{l_{n,n-2}}&{l_{n,n-1}}\end{array}\right)=:A_{k}.\qquad
$$  

For $k=n-1$ , there is nothing to prove, since $\tilde{L}_{n-1}~=~A_{n-1}$ by definition. So let $1\leq k<n-1$ .We have to show that $C:=\tilde{L}_{k}A_{k+1}=A_{k}$ . Letting $A:=A_{k+1}$ and letting $B:=\tilde{L}_{k}$ , we can use (8.24) to compute $C:=B A$ ..  

$$
c_{j i}\overset{(8,24)}{=}\left\{\begin{array}{l l}{a_{j i}=\left\{\begin{array}{l l}{0}&{\mathrm{for~each~}j\in\{1,\dots,k\},j\neq i,}\ {1}&{\mathrm{for~each~}j\in\{1,\dots,k\},j=i,}\end{array}\right.}\ {b_{j k}a_{k i}+a_{j i}=\left\{\begin{array}{l l}{l_{j k}\cdot0+a_{j i}=a_{j i}}&{\mathrm{for~each~}j\in\{k+1,\dots,n\},i\neq k,}\ {l_{j k}\cdot1+0=l_{j k}}&{\mathrm{for~each~}j\in\{k+1,\dots,n\},i=k,}\end{array}\right.}\end{array}\right.
$$  

showing $C=A_{k}$ , thereby establishing the case.  

Corollary 8.29. Consider the situation of Def. 8.13, i.e. let $F$ be a field, $m,n\in\mathbb{N}$ and $A\in\mathcal{M}(m,n,F)$ with rows $r_{1},\ldots,r_{m}$  

(a) The elementary row operation of row multiplication, i.e. of replacing row $r_{i}$ by some nonzero multiple $\lambda r_{i}$ of that row,.. $i\in\{1,\ldots,m\}$ $\lambda\in F\backslash\{0\}$ , can be accomplished by. left-multiplying $A$ by the diagonal matrix. $D_{\lambda}:=\mathrm{diag}(d_{1},\ldots,d_{m})\in D_{m}(F)$ , where  

$$
\forall_{j\in\{1,\dots,m\}}\quad d_{j}:=\left\{\begin{array}{l l}{\lambda}&{f o r j=i,}\ {1}&{f o r j\not=i.}\end{array}\right.
$$  

(b) The elementary row operation of row addition, i.e. of replacing row $r_{i}$ by the sum $r_{i}+\lambda r_{k}$ of that row and a multiple of another row,. $(i,k)\in\{1,\ldots,m\}^{2}$ $i\neq k$ $\lambda\in F$ , can be accomplished, for. $i>k$ ,by left-multiplying. $A$ by the Frobenius matrix $F_{\lambda}\in\operatorname{Fro}_{m}^{k}(F)$  

$$
\begin{array}{r}{F_{\lambda}=\left(\begin{array}{c c c c c c}{1}&&&&&\ &{\ddots}&&&&\ &&{1}&&&\ &&{f_{k+1,k}}&{1}&&\ &{f_{k+2,k}}&&{1}&&\ &{\vdots}&&&{\ddots}&\ &&&&&{1}\end{array}\right),\quad\begin{array}{c}{\forall}\ {\jmath\in\{k+1,\ldots,m\}}\end{array}}f_{j,k}:=\left\{\begin{array}{c c}{\lambda}&{f o r j=i,}\ {0}&{f o r j\neq i,}\end{array}\right.}\end{array}
$$  

and, for $\textit{i}<\textit{k}$ , by left-multiplying A by the transpose of the Frobenius matrix $F_{\lambda}\in\operatorname{Fro}_{m}^{\iota}(F)$ , where $F_{\lambda}$ is as above, except with $i$ and $k$ switched.  

Proof. (a) is immediate from (7.27a).  

(b): For $i>k$ , we apply Prop. 8.28(a) with $B:=F_{\lambda}$ , obtaining for $(c_{j i}):=F_{\lambda}A$  

$$
c_{j l}=\left\{\begin{array}{l l}{a_{j l}}&{\mathrm{~for~each~}j\in\{1,\dots,k\},}\ {f_{j k}a_{k l}+a_{j l}=\lambda a_{k l}+a_{j l}}&{\mathrm{~for~}j=i,}\ {f_{j k}a_{k l}+a_{j l}=a_{j l}}&{\mathrm{~for~each~}j\in\{k+1,\dots,m\},j\neq i,}\end{array}\right.
$$  

thereby establishing the case. For $i<k$ , we obtain, for $(b_{j i}):=(F_{\lambda})^{\mathrm{t}}$ $(c_{j i}):=(F_{\lambda})^{\mathrm{t}}A$  

$$
c_{j l}=\sum_{\alpha=1}^{m}b_{j\alpha}a_{\alpha l}=\left\{{\begin{array}{l l}{a_{j l}}&{{\mathrm{for~each~}}j\in\{1,\dots,m\},j\neq i,}\ {a_{j l}+b_{j k}a_{k l}=a_{j l}+\lambda a_{k l}}&{{\mathrm{for~}}j=i,}\end{array}}\right.
$$  

once again, establishing the case.  

Definition 8.30. Let $n\in\mathbb N$ and recall the definition of the symmetric group $S_{n}$ from Ex. 4.9(b). Moreover, let $F$ be a field (actually, the following definition still makes sense  

as long as $F^{\prime}$ is a set containing elements $0$ and 1). For each permutation $\pi\in S_{n}$ , we define an $n\times n$ matrix  

$$
P_{\pi}:=\big(e_{\pi(1)}^{\mathrm{t}}\quad e_{\pi(2)}^{\mathrm{t}}\quad\cdot\cdot\cdot\quad e_{\pi(n)}^{\mathrm{t}}\big)\in\mathcal{M}(n,F),
$$  

where the $e_{i}$ denote the standard unit (row) vectors of $F^{\mathit{\Pi}}$ . The matrix $P_{\pi}$ is called the permutation matrix (in $\mathcal{M}(n,F))$ associated with $\pi$ . We define  

$$
{\mathrm{Per}}_{n}(F):=\left\{P_{\pi}\in{\mathcal{M}}(n,F):\pi\in S_{n}\right\}.
$$  

Proposition 8.31. Let $n\in\mathbb N$ and let. $F^{\prime}$ be a field..  

(a) If $\pi\in S_{n}$ and the columns of. $P_{\pi}\in\mathrm{Per}_{n}(F)$ are given according to (8.26), then the. rows of $P_{\pi}$ are given according to the inverse permutation $\pi^{-1}$  

$$
P_{\pi}=\left({\begin{array}{c}{{e_{\pi^{-1}(1)}}}\ {{e_{\pi^{-1}(2)}}}\ {{\phantom{e_{\pi^{-1}(1)}}\cdot\cdot\cdot}}\ {{e_{\pi^{-1}(n)}}}\end{array}}\right),\quad(P_{\pi})^{\mathrm{t}}=P_{\pi^{-1}}.
$$  

(b) $P:=(p_{j i})\in\mathcal{M}(n,F)$ is a permutation matrix if, and only if, each row and each column of $P$ have precisely one entry 1 and all other entries of $P$ are $0$  

(c) Left multiplication of a matrix $A\in\mathcal{M}(n,m,F)$ $m\in\mathbb{N}$ , by a permutation matrix $P_{\pi}\in\mathrm{Per}_{n}(F)$ , permutes the rows of $A$ according to $\pi$  

$$
P_{\pi}\left(\begin{array}{c c c}{{-}}&{{r_{1}}}&{{-}}\ {{-}}&{{r_{2}}}&{{-}}\ {{-}}&{{\vdots}}&{{-}}\ {{-}}&{{r_{n}}}&{{-}}\end{array}\right)=\left(\begin{array}{c c c}{{-}}&{{r_{\pi(1)}}}&{{-}}\ {{-}}&{{r_{\pi(2)}}}&{{-}}\ {{-}}&{{\vdots}}&{{-}}\ {{-}}&{{r_{\pi(n)}}}&{{-}}\end{array}\right),
$$  

which follows from the special case  

$$
P_{\pi}\boldsymbol{\mathrm{e}}_{i}^{\mathrm{t}}=\left(\begin{array}{c}{e_{\pi^{-1}(1)}}\ {e_{\pi^{-1}(2)}}\ {\cdot\cdot\cdot}\ {e_{\pi^{-1}(n)}}\end{array}\right)\boldsymbol{\mathrm{e}}_{i}^{\mathrm{t}}=\left(\begin{array}{c}{e_{\pi^{-1}(1)}\cdot e_{i}^{\mathrm{t}}}\ {e_{\pi^{-1}(2)}\cdot e_{i}^{\mathrm{t}}}\ {\cdot\cdot\cdot}\ {e_{\pi^{-1}(n)}\cdot e_{i}^{\mathrm{t}}}\end{array}\right)=\boldsymbol{\mathrm{e}}_{\pi(i)}^{\mathrm{t}},
$$  

that holds for each $i\in\{1,\ldots,n\}$  

(d) Right multiplication of a matrix $A\in\mathcal{M}(m,n,F)$ $m\in\mathbb{N}$ , by a permutation matrix $P_{\pi}\in\mathrm{Per}_{n}(F)$ permutes the columns of $A$ according to $\pi^{-1}$  

$$
\begin{array}{r}{\left(\begin{array}{c c c c}{|}&{|}&{...}&{|}\ {c_{1}}&{c_{2}}&{...}&{c_{n}}\ {|}&{|}&{...}&{|}\end{array}\right)P_{\pi}=\left(\begin{array}{c c c c}{|}&{|}&{...}&{|}\ {c_{\pi^{-1}(1)}}&{c_{\pi^{-1}(2)}}&{...}&{c_{\pi^{-1}(n)}}\ {|}&{|}&{...}&{|}\end{array}\right),}\end{array}
$$  

which follows from the special case  

$$
\begin{array}{r l}&{e_{i}P_{\pi}=e_{i}\left(e_{\pi(1)}^{\mathrm{t}}\right.\quad e_{\pi(2)}^{\mathrm{t}}\quad...\quad e_{\pi(n)}^{\mathrm{t}}\right)=\left(e_{i}\cdot e_{\pi(1)}^{\mathrm{t}}\quad e_{i}\cdot e_{\pi(2)}^{\mathrm{t}}\quad...\quad e_{i}\cdot e_{\pi(n)}^{\mathrm{t}}\right)}\ &{\qquad=e_{\pi^{-1}(i)},}\end{array}
$$  

that holds for each $i\in\{1,\ldots,n\}$  

(e) For each $\pi,\sigma\in S_{n}$ , one has  

$$
P_{\pi}P_{\sigma}=P_{\pi\circ\sigma},
$$  

such that  

$$
I:S_{n}\longrightarrow\mathrm{Per}_{n}(F),\quad I(\pi):=P_{\pi},
$$  

constitutes a group isomorphism. In particular, ${\mathrm{Per}}_{n}(F)$ is a subgroup of $\mathrm{GL}_{n}(F)$ and  

$$
\begin{array}{r l}{\forall~}&{{}P^{-1}=P^{\mathrm{t}}.}\end{array}
$$  

Proof. (a): Consider the $i$ th row of $(p_{j i}):=P_{\pi}$ . Then $p_{j i}=1$ if, and only if, $j=\pi(i)$ (since $p_{j i}$ also belongs to the $i$ th column). Thus, $p_{j i}=1$ if, and only if, $i=\pi^{-1}(j)$ which means that the jth row is en-().  

(b): Suppose $P=P_{\pi}$ $\pi\in S_{n}$ $n\in\mathbb{N}$ , is a permutation matrix. Then (8.26) implies that each column of $P$ has precisely one $1$ and all other elements are $0$ ; (8.27) implies that each row of $P$ has precisely one $^{1}$ and all other elements are 0.  

Conversely, suppose that. $P\in\mathcal{M}(n,F)$ is such that each row and each column of $P$ have precisely one entry 1 and all other entries of $P$ are $0$ . Define a map $\pi:\{1,\ldots,n\}\longrightarrow$ $\{1,\ldots,n\}$ by letting $\pi(i)$ be such that $p_{\pi(i),i}=1$ . Then  

$$
P=\left(e_{\pi(1)}^{\mathrm{t}}\quad e_{\pi(2)}^{\mathrm{t}}\quad...\quad e_{\pi(n)}^{\mathrm{t}}\right),
$$  

and it just remains to show that $\pi$ is a permutation. It suffices to show that $\pi$ is surjective. To that end, let. $k\in\{1,\ldots,n\}$ . Then there is a unique. $i\in\{1,\ldots,n\}$ such that $p_{k i}=1$ . But then, according to the definition of $\pi$ $\pi(i)=k$ , showing that. $\pi$ is surjective and $P=P_{\pi}$  

(c): Note that, for $A=(a_{j i})\in\mathcal{M}(n,m,F)$  

$$
A=\sum_{i=1}^{m}\sum_{j=1}^{n}a_{j i}\left(\begin{array}{c c c c c}{{0}}&{{\ldots}}&{{e_{j}^{\mathrm{t}}}}&{{\ldots}}&{{0}}\ {{}}&{{}}&{{i\mathrm{th~column}}}&{{}}&{{}}\end{array}\right).
$$  

$$
\begin{array}{r l}&{P_{\mathrm{r}}A=\displaystyle\sum_{i=1}^{m}\displaystyle\sum_{j=1}^{n}a_{j}P_{\mathrm{r}}\left(\begin{array}{l l l l}{0}&{\cdots}&{\underbrace{c_{j}^{\ell}}_{i\mathrm{belom~}}}&{\cdots}&{0}\ &&{\cdots}&\ &&{\cdots}&\ &&{\cdots}&\ &&{\cdots}&{\sum_{i=1}^{m}\displaystyle\sum_{j=1}^{n}a_{j}\left(\begin{array}{l}{e_{\mathrm{r}-1}(\ell)}\ {e_{\mathrm{r}-1}(\ell)}\ {\cdots}\ {e_{\mathrm{r}-1}(\ell)}\end{array}\right)\left(\begin{array}{l l l l}{0}&{\cdots}&{\underbrace{c_{j}^{\ell}}_{i\mathrm{belom~}}}&{\cdots}&{0}\ &{\cdots}&{\mathrm{inheom~}}&{\cdots}&\end{array}\right)}\ &{\quad\quad\quad=\displaystyle\sum_{i=1}^{m}\displaystyle\sum_{j=1}^{n}a_{j}\left(\begin{array}{l l l l}{0}&{\cdots}&{e_{\mathrm{r}-1}(\ell)}&{e_{j}}&{\cdots}&{0}\ {0}&{\cdots}&{e_{\mathrm{r}-1}(\ell)}&{e_{j}}&{\cdots}&{0}\ {0}&{\cdots}&{\underbrace{e_{\mathrm{r}-1}(\ell)}_{i\mathrm{belom~}}}&{\cdots}&{0}\end{array}\right)}\ &{\quad\quad\quad=\displaystyle\sum_{i=1}^{m}\displaystyle\sum_{j=1}^{n}a_{j}\left(\begin{array}{l}{0}&{\cdots}&{\underbrace{e_{j}^{\ell}}_{i\mathrm{belom~}}\cdots}&{0}\ {\vdots}&{\ddots}\ {\vdots}&{\vdots}\end{array}\right),}\end{array}
$$  

which establishes the case.  

Thus,  

(d): We have  

$$
\begin{array}{r l r}{\Bigg(\Bigg(\begin{array}{c c c c}{|}&{|}&{\dots}&{|}\ {c_{1}}&{c_{2}}&{\dots}&{c_{n}}\ {|}&{|}&{\dots}&{|}\end{array}\Bigg)P_{\pi}\Bigg)^{\mathrm{t}}}&{\stackrel{\mathrm{t}}{=}}&{P_{\pi^{-1}}\left(\begin{array}{c c c}{-}&{c_{1}}&{-}\ {-}&{c_{2}}&{-}\ {-}&{\vdots}&{-}\ {-}&{c_{n}}&{-}\end{array}\right)\stackrel{\mathrm{c}}{=}\left(\begin{array}{c c c}{-}&{c_{\pi^{-1}(1)}}&{-}\ {-}&{c_{\pi^{-1}(2)}}&{-}\ {-}&{\vdots}&{-}\ {-}&{c_{\pi^{-1}(n)}}&{-}\end{array}\right)}\ &{=}&{\Bigg(\Bigg(c_{\pi^{-1}(1)}^{|}}&{|}&{\cdots}&{|}\ {|}&{|}&{\cdots}&{|}\end{array}\Bigg)\Bigg)^{\mathrm{t}},~}\end{array}
$$  

proving (d).  

(e): For $\pi,\sigma\in S_{n}$ , we compute  

$$
P_{\pi}P_{\sigma}={\left(\begin{array}{c}{e_{\pi^{-1}(1)}}\ {e_{\pi^{-1}(2)}}\ {\quad\cdot\cdot\cdot}\ {e_{\pi^{-1}(n)}}\end{array}\right)}\left(e_{\sigma(1)}^{\mathrm{t}}\quad e_{\sigma(2)}^{\mathrm{t}}\quad\cdot\cdot\cdot\quad e_{\sigma(n)}^{\mathrm{t}}\right)
$$  

$$
\begin{array}{r l}{\stackrel{(*)}{=}\big(e_{(\pi\circ\sigma)(1)}^{\mathrm{t}}\big.}&{{}e_{(\pi\circ\sigma)(2)}^{\mathrm{t}}\quad\cdot\cdot\cdot\quad e_{(\pi\circ\sigma)(n)}^{\mathrm{t}}\big)=P_{\pi\circ\sigma},}\end{array}
$$  

showing (8.28), where, at $^{\circ\circ}(\ast)^{\prime}$ , we used that  

$$
\forall_{i,j\in\{1,\dots,n\}}\pi^{-1}(i)=\sigma(j)\quad\Leftrightarrow\quad i=(\pi\circ\sigma)(j).
$$  

Both surjectivity and injectivity of $I$ are clear from Def. 8.30 and, then, ${\mathrm{Per}}_{n}(F)$ must be a group by Prop. 4.11(c). Combining (8.28) with (b) proves (8.29) and, thus, also shows ${\mathrm{Per}}_{n}(F)$ to be a subgroup of. $\mathrm{GL}_{n}(F)$  

Definition and Remark 8.32. Let $n\in\mathbb N$ and let $F$ be a field. A permutation matrix $P_{\tau}\in\mathrm{Per}_{n}(F)$ , corresponding to a transposition $\tau=(j i)\in S_{n}$ $\tau$ permutes $i$ and $j$ and leaves all other elements fixed), is called a transposition matrix and is denoted by $P_{j i}:=P_{\tau}$ . The transposition matrix $P_{j i}$ has the form  

$$
\begin{array}{r}{P_{j i}=\left(\begin{array}{c c c c c c c}{1}&&&&&&&\ &{\ddots}&&&&&&\ &&{1}&&&&&\ &&{0}&{1}&&&&\ &&&{\ddots}&&&&\ &&&&{1}&&&\ &&{1}&&&&{0}&&\ &&&&&&{1}&&\ &&&&&&&{\ddots}&\ &&&&&&&{1}\end{array}\right).}\end{array}
$$  

Since every permutation is the composition of a finite number of transpositions (which we will prove in Linear Algebra II), it is implied by Prop. 8.31(e) that every permutation matrix is the product of a finite number of transposition matrices. It is immediate from Prop. 8.31(c),(d) that left multiplication of a matrix $A\in{\mathcal{M}}(n,m)$ $m\in\mathbb{N}$ by $P_{j i}\in\operatorname{Per}_{n}(F)$ switches the $i$ th and $j$ th row of. $A$ , whereas right multiplication of $A\in{\mathcal{M}}(m,n)$ by $P_{j i}\in\operatorname{Per}_{n}(F)$ switches the. $i$ th and $j$ th column of. $A$  

Corollary 8.33. Consider the situation of Def. 8.13, i.e. let $F^{\prime}$ be a field, $m,n\in\mathbb{N}$ and $A\in\mathcal{M}(m,n,F)$ with rows $r_{1},\ldots,r_{m}$  

(a) The elementary row operation of row switching, i.e. of switching rows $r_{i}$ and $r_{j}$ where $i,j\in\{1,\dots,m\}$ , can be accomplished by left-multiplying A by the transposition matrix $P_{i j}\in\mathrm{Per}_{m}(F)$  

(b) Let $A^{(k)}\mapsto A^{(k+1)}$ be the matrix transformation occurring in the kth step of the Gaussian elimination Alg. 8.17 and assume the kth step is being performed by Alg. 8.17(b), i.e. by first switching the ith row with the $r(k)t h$ row and then, for each. $i\in$ {r(k)+1,., m}, replacing the (new) ith row by the (new) ith row plus -a)/a),k times the (new) $r(k)t h$ row, then  

$$
A^{(k+1)}=L_{k}P_{i,r(k)}A^{(k)}
$$  

with transposition matrix $P_{i,r(k)}\in\mathrm{Per}_{m}(F)$ and with $L_{k}\in\mathrm{Fro}_{m}^{r(k)}(F)$ being the Frobenius matrix of index $r(k)$ defined in (8.25b).  

Proof. (a) is immediate from Prop. 8.31(c) (cf. Def. and Rem. (8.32).   
(b) is due to (a) combined with Prop. 8.28(b).  

#### 8.4.3 Existence  

Theorem 8.34. Let $F^{\prime}$ be a field and $A\in\mathcal{M}(m,n,F)$ with $m,n\in\mathbb{N}$ .Then there exists a permutation matrix $P\in\mathrm{Per}_{m}(F)$ such that $P A$ has an $L U$ decomposition in the sense of Def. 8.24. More precisely, if $A\in\mathcal{M}(m,n,F)$ is the matrix in echelon form resulting at the end of the Gaussian elimination Alg. 8.17 applied to $A$ , then there exist $a$ permutation matrix $P\in\mathrm{Per}_{m}(F)$ and a unipotent lower triangular matrix $L\in\mathrm{BL}_{m}^{1}(F)$ such that  

$$
P A=L{\tilde{A}}.
$$  

It is an $L U$ decomposition in the strict sense (i.e. with $\tilde{A}\in\mathrm{BU}_{m}(F))$ for $A$ being quadratic (i.e. $m\times m$ ). If no row switches occurred during the application of Alg. 8.17, then $P=\mathrm{Id}_{m}$ and $A$ itself has an $L U$ decomposition.If $A\in\operatorname{GL}_{n}(F)$ has an $L U$ decomposition, then its $L U$ decomposition is unique.  

Proof. Let $N\in\{0,\ldots,n\}$ be the final number of steps that is needed to perform the Gaussian elimination Alg. 8.17. If. $N=0$ , then $A$ consists of precisely one row and there. is nothing to prove (set $L:=P:=(1)$ ). If $N\geq1$ , then let $A^{(1)}:=A$ and, recursively, for each $k\in\{1,\ldots,N\}$ , let $A^{(k+1)}$ be the matrix obtained in the $k$ th step of the Gaussian elimination algorithm. If Alg. 8.17(b) is used in the. $k$ th step, then, according to Cor. 8.33(b),  

$$
A^{(k+1)}=L_{k}P_{k}A^{(k)},
$$  

where $P_{k}:=P_{i,r(k)}\in\operatorname{Per}_{m}(F)$ is the transposition matrix that switches rows. $r(k)$ and $i$ while $L_{k}\in\mathrm{Fro}_{m}^{r(k)}(F)$ is the Frobenius matrix of index. $r(k)$ given by (8.25b). If (a) or (c) of Alg. 8.17 is used in the. $k$ th step, then (8.33) also holds, namely with $P_{k}:=\operatorname{Id}_{m}$ for (a) and with $L_{k}:=P_{k}:=\mathrm{Id}_{m}$ for (c). By induction, (8.33) implies  

$$
\tilde{A}=A^{(N+1)}=L_{N}P_{N}\cdot\cdot\cdot L_{1}P_{1}A.
$$  

To show that we can transform (8.34) into (8.32), we first rewrite the right-hand side of (8.34) taking into account $P_{k}^{-1}=P_{k}$ for each of the transposition matrices $P_{k}$  

$$
=L_{N}(P_{N}L_{N-1}\underbrace{P_{N})(P_{N}}_{\mathrm{Id}_{m}}P_{N-1}L_{N-2}\underbrace{P_{N-1}P_{N})(P_{N}P_{N-1}}_{\mathrm{Id}_{m}}P_{N-2}\cdot\cdot\cdot L_{1}\underbrace{P_{2}\cdot\cdot P_{N})P_{N}P_{N-1}\cdot\cdot\cdot P_{N}}_{\mathrm{Id}_{m}}
$$  

Defining  

$$
\l_{N}^{\prime}:=L_{N},\quad L_{k}^{\prime}:=P_{N}P_{N-1}\cdot\cdot\cdot P_{k+1}L_{k}P_{k+1}\cdot\cdot\cdot P_{N-1}P_{N}\quad\mathrm{for~each}k\in\{1,\dots,N-1\}.
$$  

(8.35) takes the form  

$$
\tilde{A}=L_{N}^{\prime}\cdot\cdot\cdot L_{1}^{\prime}P_{N}P_{N-1}\cdot\cdot\cdot P_{2}P_{1}A.
$$  

We now observe that the. $L_{k}^{\prime}$ are still Frobenius matrices of index $r(k)$ , except that the entries $l_{j,r(k)}$ of $L_{k}$ with $j>r(k)$ have been permuted according to. $P_{N}P_{N-1}\cdot\cdot\cdot P_{k+1}$ This follows since  

$$
\begin{array}{r}{\mathbf{\Sigma}_{j i}^{\left(1\right)}\left(\begin{array}{c c c c c c}{1}&&&&&\ &{\ddots}&&&&\ &&{1}&&&\ &{\vdots}&{\ddots}&&&\ &&{l_{i,r(k)}}&&&\ &{\vdots}&&&{1}&&\ &&{\ddots}&&&\ &&{l_{j,r(k)}}&&&{\ddots}&\ &&&&&{1}&\ &&&&&&{\ddots}\ &&&&&&{\ddots}\end{array}\right)P_{j i}=\left(\begin{array}{c c c c c c}{1}&&&&&\ &{\ddots}&&&&\ &&{1}&&&\ &&{\vdots}&{\ddots}&&&\ &&{l_{j,r(k)}}&&&{1}&\ &{\vdots}&&&{\ddots}&\ &&&{1}&&\ &&&&{1}\end{array}\right)}\ {\mathbf{\Sigma}_{j}^{\left(\mathbf{\Sigma}\right)}}\end{array}
$$  

as left multiplication by $P_{j i}$ switches the $i$ th and $j$ th row, switching $l_{i,r(k)}$ and $l_{j,r(k)}$ and moving the corresponding 1's off the diagonal, whereas right multiplication by $P_{j i}$ switches $i$ th and $j$ th column, moving both 1's back onto the diagonal while leaving the $r(k)\mathrm{th}$ column unchanged.  

Finally, using that each $(L_{k}^{\prime})^{-1}$ , according to Prop. 8.28(c), exists and is also a Frobenius matrix, (8.37) becomes  

$$
L\tilde{A}=P A
$$  

with  

$$
P:=P_{N}P_{N-1}\cdot\cdot\cdot P_{2}P_{1},\quad L:=(L_{1}^{\prime})^{-1}\cdot\cdot\cdot(L_{N}^{\prime})^{-1}.
$$  

Comparing with Prop. 8.28(d) shows that $L=(L_{1}^{\prime})^{-1}\cdot\cdot\cdot(L_{N}^{\prime})^{-1}$ is a unipotent lower. triangular matrix, thereby establishing (8.32). Note: From Prop. 8.28(d) and the definition of the. $L_{k}$ , we actually know all entries of $L$ explicitly: Every nonzero entry of the $r(k)\mathrm{th}$ column is given by (8.25b). This will be used when formulating the LU. decomposition algorithm in Sec. 8.4.4 below..  

If $A$ is invertible, then so is. $U:=\tilde{A}=L^{-1}A$ .If $A$ is invertible, and we have LU decompositions  

$$
{\cal L}_{1}U_{1}=A={\cal L}_{2}U_{2},
$$  

then we obtain $U_{1}U_{2}^{-1}=L_{1}^{-1}L_{2}=:E$ . As both upper triangular and unipotent lower triangular matrices are closed under matrix multiplication, the matrix $E$ is unipotent and both upper and lower triangular, showing. $E=\operatorname{Id}_{m}$ . This, in turn, yields. $U_{1}=U_{2}$ as well as $L_{1}=L_{2}$ , i.e. the claimed uniqueness of the LU decomposition for invertible $A$  

Remark 8.35. Note that, even for invertible $A\in\operatorname{GL}_{n}(F)$ , the triple. $(P,L,{\tilde{A}})$ of (8.32) is, in general, not unique. For example  

![](https://cdn-mineru.openxlab.org.cn/extract/fe50916f-c605-4dd4-85ef-e6dc3ee061d8/60d95cfa7b81a400da5890f8648abf944e51de9474b084e1d63090b1e1bdf2c4.jpg)  

Remark 8.36. Let $F$ be a field. Suppose the goal is to solve linear systems $A x=b$ with fixed matrix $A\in\mathcal{M}(m,n,F)$ and varying vector $b\in F^{n}$ . Moreover, suppose one knows an LU decomposition $P A=L\tilde{A}$ with permutation matrix $P\in\mathrm{Per}_{m}(F)$ . One can then proceed as in Rem. 8.25 above, except with $A$ replaced by $P A$ and $b$ replaced by $P b$ (you can find code for a Python $\it{3.8}$ implementation that uses the described strategy to solve $A x=b$ over $\mathbb{R}$ and $\mathbb{C}$ given an LU decomposition of $A$ in function gaussE1SolveFromLU in Sec. F.1.2 of the Appendix). As already indicated in Rem. 8.25, in the presence of roundoff errors, such errors might be magnified by the use of an LU decomposition. If one works over the fields $\mathbb{R}$ or $\mathbb{C}$ , then there are other decompositions (e.g. the so-called QR decomposition) that tend to behave more benignly in the presence of roundoff errors (cf., e.g., [Phi23, Rem. 5.14] and [Phi23, Sec. 5.4.3]).  

#### 8.4.4 Algorithm  

Let us crystallize the proof of Th. 8.34 into an algorithm to actually compute the matrices $L$ $P$ , and $\tilde{A}$ occurring in decomposition (8.32) of a given $A\in\mathcal{M}(m,n,F)$ . As in the proof of Th. 8.19, let. $N\in\{1,\ldots,n+1\}$ be the maximal $k$ occurring during the. Gaussian elimination Alg. 8.17 applied to $A$ . For $F\in\{\mathbb{R},\mathbb{C}\}$ , you can find code for a. Python $\it{3.8}$ implementation of the following algorithm in function gaussEl in Sec. F.1.2 of the Appendix..  

(a) Algorithm for $\tilde{A}$ : Starting with $A^{(1)}:=A$ , the final step of Alg. 8.17 yields the matrix $\dot{A}:=A^{(N)}\in\mathcal{M}(m,n,F)$ in echelon form.  

(b) Algorithm for $P$ : Starting with $P^{(1)}:=\mathrm{Id}_{m}$ , in the $k$ th step of Alg. 8.17, define $P^{(k+1)}:=P_{k}P^{(k)}$ , where $P_{k}:=P_{i,r(k)}$ if rows $r(k)$ and $i$ are switched according to Alg. 8.17(b), and $P_{k}:=\operatorname{Id}_{m}$ , otherwise. In the last step, one obtains $P:=P^{(N)}$  

(c) Algorithm for $L$ : Starting with $L^{(1)}:=0$ (zero matrix), we obtain $L^{(k+1)}$ from $L^{(k)}$ in the $k$ th step of Alg. 8.17 as follows: For Alg. 8.17(c), set. $L^{(k+1)}:=L^{(k)}$ . If rows $r(k)$ and $i$ are switched according to Alg. 8.17(b), then we first switch rows. $r(k)$ and $i$ in $L^{(k)}$ to obtain some $\overset{\vartriangle}{L}^{(k)}$ (this conforms to the definition of the $L_{k}^{\prime}$ in (8.36), we will come back to this point below). For Alg. 8.17(a) and for the elimination step of $L^{(k)}$ $\tilde{L}^{(k)}$ $L^{(k+1)}$ $r(k)$ $l_{i,r(k)}^{(k+1)}:=a_{i k}^{(k)}/a_{r(k),k}^{(k)}$ for each $i\in\{r(k)+1,\ldots,m\}$ . In the last step, we obtain $L$ from $L^{(N)}$ by setting all elements on the diagonal to $1$ (postponing this step to the end avoids worrying. about the diagonal elements when switching rows earlier)..  

To see that this procedure does, indeed, provide the correct $L$ , we go back to the   
proof of Th. 8.34: From (8.38), (8.39), and (8.36), it follows that the $r(k)$ th column   
of $L$ is precisely the. $r(k)\mathrm{th}$ column of $L_{k}^{-1}$ permuted according to $P_{N}\cdots P_{k+1}$ . This $r(k)$ $L_{k}^{-1}$ $l_{i,r(k)}^{(k+1)}:=a_{i k}^{(k)}/a_{r(k),k}^{(k)}$ $P_{k+1},\ldots,P_{N}$   
steps.  

Remark 8.37. Note that in the $k$ th step of the algorithm for $\tilde{A}$ , we eliminate all elements of the $k$ th column below the row with number $r(k)$ , while in the. $k$ th step of. the algorithm for $L$ , we populate elements of the $r(k)\mathrm{th}$ column below the diagonal for the first time. Thus, when implementing the algorithm in practice, one can save memory capacity by storing the new elements for $L$ at the locations of the previously eliminated elements of $A$ . This strategy is sometimes called compact storage.  

Example 8.38. Let us determine the LU decomposition (8.32) (i.e. the matrices $P$ $L$ and $\tilde{A}$ ) for the matrix  

$$
A:={\left(\begin{array}{l l l l}{1}&{4}&{2}&{3}\ {0}&{0}&{1}&{4}\ {2}&{6}&{3}&{1}\ {1}&{2}&{1}&{0}\end{array}\right)}\in{\mathcal{M}}(4,4,\mathbb{R}).
$$  

According to the algorithm described above, we start by initializing  

$$
A^{(1)}:=A,\quad P^{(1)}:=\operatorname{Id}_{4},\quad L^{(1)}:=0,\quad r(1):=1
$$  

(where the function $r$ is the one introduced in the Gaussian elimination Alg. 8.17). We  

use Alg. 8.17(a) to eliminate in the first column, obtaining  

$$
\begin{array}{l l}{{P^{(2)}=P^{(1)}=\mathrm{Id}_{4},~}}&{{L^{(2)}=\left(\begin{array}{l l l l}{{0}}&{{0}}&{{0}}&{{0}}\ {{0}}&{{0}}&{{0}}&{{0}}\ {{2}}&{{0}}&{{0}}&{{0}}\ {{1}}&{{0}}&{{0}}&{{0}}\end{array}\right)}}\ {{A^{(2)}=\left(\begin{array}{l l l l}{{1}}&{{4}}&{{2}}&{{3}}\ {{0}}&{{0}}&{{1}}&{{4}}\ {{0}}&{{-2}}&{{-1}}&{{-5}}\ {{0}}&{{-2}}&{{-1}}&{{-3}}\end{array}\right),~}}&{{r(2)=r(1)+1=2.}}\end{array}
$$  

We now need to apply Alg. 8.17(b) and we switch rows 2 and 3 using $P_{23}$  

$$
P^{(3)}=P_{23}P^{(2)}=\left({{\bf{\sigma}}_{0}^{1}\mathrm{~{~\bf{0}}~}{\bf{\sigma}}_{1}\mathrm{~{\sigma}_{0}^{0}}}\right),
$$  

$$
P_{23}L^{(2)}=\left(\begin{array}{c c c c}{{0}}&{{0}}&{{0}}&{{0}}\ {{2}}&{{0}}&{{0}}&{{0}}\ {{0}}&{{0}}&{{0}}&{{0}}\ {{1}}&{{0}}&{{0}}&{{0}}\end{array}\right),\quad P_{23}A^{(2)}=\left(\begin{array}{c c c c}{{1}}&{{4}}&{{2}}&{{3}}\ {{0}}&{{-2}}&{{-1}}&{{-5}}\ {{0}}&{{0}}&{{1}}&{{4}}\ {{0}}&{{-2}}&{{-1}}&{{-3}}\end{array}\right).
$$  

Eliminating the second column yields  

$$
L^{(3)}=\left(\begin{array}{c c c c}{{0}}&{{0}}&{{0}}&{{0}}\ {{2}}&{{0}}&{{0}}&{{0}}\ {{0}}&{{0}}&{{0}}&{{0}}\ {{1}}&{{1}}&{{0}}&{{0}}\end{array}\right),\quad A^{(3)}=\left(\begin{array}{c c c c}{{1}}&{{4}}&{{2}}&{{3}}\ {{0}}&{{-2}}&{{-1}}&{{-5}}\ {{0}}&{{0}}&{{1}}&{{4}}\ {{0}}&{{0}}&{{0}}&{{2}}\end{array}\right),\quad r(3)=r(2)+1=3.
$$  

Accidentally, elimination of the third column does not require any additional work and we have  

$$
P=P^{(4)}=P^{(3)}=\left({\begin{array}{l l l l}{1}&{0}&{0}&{0}\ {0}&{0}&{1}&{0}\ {0}&{1}&{0}&{0}\ {0}&{0}&{0}&{1}\end{array}}\right),\quad L^{(4)}=L^{(3)},\quad L=\left({\begin{array}{l l l l}{1}&{0}&{0}&{0}\ {2}&{1}&{0}&{0}\ {0}&{0}&{1}&{0}\ {1}&{1}&{0}&{1}\end{array}}\right),
$$  

$$
\tilde{A}=A^{(4)}=A^{(3)}=\left(\begin{array}{c c c c}{{1}}&{{4}}&{{2}}&{{3}}\ {{0}}&{{-2}}&{{-1}}&{{-5}}\ {{0}}&{{0}}&{{1}}&{{4}}\ {{0}}&{{0}}&{{0}}&{{2}}\end{array}\right),\quad r(4)=r(3)+1=4.
$$  

Recall that $L$ is obtained from $L^{(4)}$ by setting the diagonal values to $1$ . One checks that, indeed, $P A=L\tilde{A}$  

Example 8.39. We remain in the situation of the previous Ex. 8.38. We see that $\operatorname{rk}A=\operatorname{rk}{\tilde{A}}=4$ , showing $A$ to be invertible. In Ex. 8.2(c), we observed that we obtain the columns $v_{k}$ of $A^{-1}$ by solving the linear systems  

$$
A v_{1}=e_{1},\ldots,A v_{n}=e_{n},
$$  

where $n=4$ in the present case and where. $e_{1},\ldots,e_{n}$ denote the standard (column) basis vectors. We now determine the. $v_{k}$ using the LU decomposition of Ex. 8.38 together with. the strategies described in Rem. 8.36 and Rem. 8.25: First, with  

$$
L={\left(\begin{array}{l l l l}{1}&{0}&{0}&{0}\ {2}&{1}&{0}&{0}\ {0}&{0}&{1}&{0}\ {1}&{1}&{0}&{1}\end{array}\right)}
$$  

we solve  

$$
L z_{1}=P e_{1}=e_{1},\quad L z_{2}=P e_{2}=e_{3},\quad L z_{3}=P e_{3}=e_{2},\quad L z_{4}=P e_{4}=e_{4},
$$  

using forward substitution:  

$$
\begin{array}{r l r l r l}&{\iota_{11}=1,}&&{z_{12}=-2z_{11}=-2,}&&{z_{13}=0,}&&{z_{14}=-z_{11}-z_{12}=-1+2=1,}\ &{\iota_{21}=0,}&&{z_{22}=0,}&&{z_{23}=1,}&&{z_{24}=0,}\ &{\iota_{31}=0,}&&{z_{32}=1-2z_{31}=1,}&&{z_{33}=0,}&&{z_{34}=-z_{31}-z_{32}=-1,}\ &{\iota_{41}=0,}&&{z_{42}=0,}&&{z_{43}=0,}&&{z_{44}=1,}\end{array}
$$  

obtaining the column vectors  

$$
z_{1}={\left(\begin{array}{l}{1}\ {-2}\ {0}\ {1}\end{array}\right)},\quad z_{2}={\left(\begin{array}{l}{0}\ {0}\ {1}\ {0}\end{array}\right)},\quad z_{3}={\left(\begin{array}{l}{0}\ {1}\ {0}\ {-1}\end{array}\right)},\quad z_{4}={\left(\begin{array}{l}{0}\ {0}\ {0}\ {1}\end{array}\right)}.
$$  

Next, with  

$$
\tilde{A}=\left(\begin{array}{c c c c}{{1}}&{{4}}&{{2}}&{{3}}\ {{0}}&{{-2}}&{{-1}}&{{-5}}\ {{0}}&{{0}}&{{1}}&{{4}}\ {{0}}&{{0}}&{{0}}&{{2}}\end{array}\right)
$$  

we solve  

$$
\tilde{A}v_{1}=z_{1},\quad\tilde{A}v_{2}=z_{2},\quad\tilde{A}v_{3}=z_{3},\quad\tilde{A}v_{4}=z_{4},
$$  

using backward substitution:  

$$
\begin{array}{r l r l r l}&{v_{14}=\displaystyle\frac12,}&&{v_{13}=0-4v_{14}=-2,\quad v_{12}=\left(-\frac12\right)\left(-2+v_{13}+5v_{14}\right)=\frac34,}&&{v_{11}=1-4v_{12}-2v_{13}-3v_{14}=-2v_{14}=-2v_{13}-3v_{14}=-2v_{14}=-2v_{13}-3v_{14}=-2v_{14}=-2v_{14}=-2v_{13}-3v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-2v_{14}=-1v_{4}=-2v_{14}=-1v_{4}=-2v_{14}=--2v_{14}=-\omega-2v_{14}= 
$$  

obtaining the column vectors  

$$
\begin{array}{r}{v_{1}=\left(\begin{array}{c}{\frac{1}{2}}\ {\frac{3}{4}}\ {-2}\ {\frac{1}{2}}\end{array}\right),\quad v_{2}=\left(\begin{array}{c}{0}\ {-\frac{1}{2}}\ {1}\ {0}\end{array}\right),\quad v_{3}=\left(\begin{array}{c}{-\frac{3}{2}}\ {-\frac{1}{4}}\ {2}\ {-\frac{1}{2}}\end{array}\right),\quad v_{4}=\left(\begin{array}{c}{\frac{7}{2}}\ {-\frac{1}{4}}\ {-2}\ {\frac{1}{2}}\end{array}\right).}\end{array}
$$  

Thus,  

$$
A^{-1}=\frac{1}{4}\cdot\left(\begin{array}{c c c c}{{2}}&{{0}}&{{-6}}&{{14}}\ {{3}}&{{-2}}&{{-1}}&{{-1}}\ {{-8}}&{{4}}&{{8}}&{{-8}}\ {{2}}&{{0}}&{{-2}}&{{2}}\end{array}\right).
$$  

One verifies  

$$
A A^{-1}={\left(\begin{array}{l l l l}{1}&{4}&{2}&{3}\ {0}&{0}&{1}&{4}\ {2}&{6}&{3}&{1}\ {1}&{2}&{1}&{0}\end{array}\right)}\cdot{\frac{1}{4}}\cdot{\left(\begin{array}{l l l l}{2}&{0}&{-6}&{14}\ {3}&{-2}&{-1}&{-1}\ {-8}&{4}&{8}&{-8}\ {2}&{0}&{-2}&{2}\end{array}\right)}={\left(\begin{array}{l l l l}{1}&{0}&{0}&{0}\ {0}&{1}&{0}&{0}\ {0}&{0}&{1}&{0}\ {0}&{0}&{0}&{1}\end{array}\right)}.
$$  

You can find Python 3.8 code that computes $A^{-1}$ via the above strategy (i.e. by first computing an LU decomposition of $A$ ) in Sec. F.1.3 of the Appendix.  

## A Axiomatic Set Theory  

### A.1 Motivation, Russell's Antinomy  

As it turns out, naive set theory, founded on the definition of a set according to Cantor. (as stated at the beginning of Sec. 1.3) is not suitable to be used in the foundation of mathematics. The problem lies in the possibility of obtaining contradictions such as. Russell's antinomy, after Bertrand Russell, who described it in 1901..  

Russell's antinomy is obtained when considering the set. $X$ of all sets that do not con-. tain themselves as an element: When asking the question if $X\in X$ , one obtains the contradiction that $X\in X\Leftrightarrow X\notin X$  

Suppose $X\in X$ .Thend $X$ is a set that contains itself. But. $X$ was defined to contain only sets that do not contain themselves, i.e. $X\not\in X$  

So suppose $X\not\in X$ . Then $X$ is a set that does not contain itself. Thus, by the definition of $X$ $X\in X$  

Perhaps you think Russell's construction is rather academic, but it is easily translated into a practical situation. Consider a library. The catalog $C$ of the library should contain. all the library's books. Since the catalog itself is a book of the library, it should occur as an entry in the catalog. So there can be catalogs such as $C$ that have themselves as. an entry and there can be other catalogs that do not have themselves as an entry. Now one might want to have a catalog. $X$ of all catalogs that do not have themselves as an entry. As in Russell's antinomy, one is led to the contradiction that the catalog $X$ must have itself as an entry if, and only if, it does not have itself as an entry.  

One can construct arbitrarily many versions, which we will not do. Just one more: Consider a small town with a barber, who, each day, shaves all inhabitants, who do not. shave themselves. The poor barber now faces a terrible dilemma: He will have to shave himself if, and only if, he does not shave himself..  

To avoid contradictions such as Russell's antinomy, axiomatic set theory restricts the construction of sets via so-called axioms, as we will see below.  

### A.2 Set-Theoretic Formulas  

The contradiction of Russell's antinomy is related to Cantor's sets not being hierarchical.. Another source of contradictions in naive set theory is the imprecise nature of informal languages such as English. In (1.6), we said that.  

$$
A:=\{x\in B:P(x)\}
$$  

defines a subset of $B$ if $P(x)$ is a statement about an element $x$ of $B$ .Now take $B:=\mathbb{N}:=\{1,2,\dots\}$ to be the set of the natural numbers and let  

P(x) := "The number $x$ can be defined by fifty English words or less".  

Then $A$ is a finite subset of $\mathbb{N}$ , since there are only finitely many English words (if you think there might be infinitely many English words, just restrict yourself to the words. contained in some concrete dictionary). Then there is a smallest natural number $n$ that is not in $A$ .But then $n$ is the smallest natural number that can not be defined by.  

fifty English words or less, which, actually, defines $n$ by less than fifty English words, in contradiction to $n\not\in A$  

To avoid contradictions of this type, we require $P(x)$ to be a so-called set-theoretic formula.  

Definition A.1. (a) The language of set theory consists precisely of the following symbols: $\land,\lnot,\exists,(,),\in,=,v_{j}$ , where $j=1,2,\ldots$  

(b) A set-theoretic formula is a finite string of symbols from the above language of set theory that can be built using the following recursive rules:. (i) $v_{i}\in v_{j}$ is a set-theoretic formula for $i,j=1,2,\dots$ (ii) $v_{i}=v_{j}$ is a set-theoretic formula for. $i,j=1,2,\ldots$ (iii) If $\phi$ and $\psi$ are set-theoretic formulas, then. $(\phi)\wedge(\psi)$ is a set-theoretic formula. (iv) If $\phi$ is a set-theoretic formula, then. $\neg(\phi)$ is a set-theoretic formula. (v) If $\phi$ is a set-theoretic formula, then $\exists v_{j}(\phi)$ is a set-theoretic formula for $j=$ $1,2,\ldots$  

Example A.2. Examples of set-theoretic formulas are ( $v_{3}~\in~v_{5}$ $\wedge$ ( $\neg(v_{2}~=~v_{3})$ $\exists v_{1}(\lnot(v_{1}=v_{1}))$ ; examples of symbol strings that are not set-theoretic formulas are $v_{1}\in v_{2}\in v_{3}$ $\exists\exists\neg$ , and $\in v_{3}\exists$  

Remark A.3. It is noted that, for a given finite string of symbols, a computer can, in. principle, check in finitely many steps, if the string constitutes a set-theoretic formula. or not. The symbols that can occur in a set-theoretic formula are to be interpreted as follows: The variables $v_{1},v_{2},\ldots.$ are variables for sets. The symbols $\wedge$ and $\neg$ are to be interpreted as the logical operators of conjunction and negation as described in. Sec. 1.2.2. Similarly, $\exists$ stands for an existential quantifier as in Sec. 1.4: The statement. $\exists v_{j}(\phi)$ means "there exists a set $v_{j}$ that has the property $\phi^{,}$ . Parentheses ( and ) are used to make clear the scope of the logical symbols $\exists,\land,\lnot$ .Where the symbol $\in$ occurs, it is interpreted to mean that the set to the left of $\in$ is contained as an element in the set to the right of $\in$ . Similarly,. $-$ is interpreted to mean that the sets occurring to the. left and to the right of $-$ are equal.  

Remark A.4. A disadvantage of set-theoretic formulas as defined in Def. A.1 is that.   
they quickly become lengthy and unreadable (at least to the human eye). To make.   
formulas more readable and concise, one introduces additional symbols and notation.   
Formally, additional symbols and notation are always to be interpreted as abbreviations.   
or transcriptions of actual set-theoretic formulas. For example, we use the rules of Th..  

1.11 to define the additional logical symbols V, $\rightarrow$ $\Leftrightarrow$ as abbreviations:  

$$
\begin{array}{l l l l}{{(\phi)\vee(\psi)}}&{{\mathrm{~is~short~for~}}}&{{\neg((\neg(\phi))\wedge(\neg(\psi)))}}&{{\mathrm{~(cf.~Th.~1.11(j)),~}}}\ {{(\phi)\Rightarrow(\psi)}}&{{\mathrm{~is~short~for~}}}&{{(\neg(\phi))\vee(\psi)}}&{{\mathrm{~(cf.~Th.~1.11(a)),}}}\ {{(\phi)\Leftrightarrow(\psi)}}&{{\mathrm{~is~short~for~}}}&{{((\phi)\Rightarrow(\psi))\wedge((\psi)\Rightarrow(\phi))}}&{{\mathrm{~(cf.~Th.~1.11(b)).}}}\end{array}
$$  

Similarly, we use (1.17a) to define the universal quantifier:  

$$
\forall v_{j}(\phi)\quad\mathrm{is~short~for}\quad\neg(\exists v_{j}(\neg(\phi))).
$$  

Further abbreviations and transcriptions are obtained from omitting parentheses if it is clear from the context and/or from Convention 1.10 where to put them in, by writing. variables bound by quantifiers under the respective quantifiers (as in Sec. 1.4), and by using other symbols than. $v_{j}$ for set variables. For example,.  

$$
\begin{array}{r l}{\bigvee}&{(\phi\Rightarrow\psi)\quad\mathrm{transcribes}\quad\neg(\exists v_{1}(\neg((\neg(\phi))\vee(\psi)))).}\end{array}
$$  

Moreover,  

$$
v_{i}\neq v_{j}\mathrm{~is~short~for~}\lnot(v_{i}=v_{j});\qquadv_{i}\notin v_{j}\mathrm{~is~short~for~}\lnot(v_{i}\in v_{j}).
$$  

Remark A.5. Even though axiomatic set theory requires the use of set-theoretic formulas as described above, the systematic study of formal symbolic languages is the subject of the field of mathematical logic and is beyond the scope of this class (see, e.g., [EFT07]). In Def. and Rem. 1.15, we defined a proof of statement $B$ from statement $A_{1}$ as a finite sequence of statements. $A_{1},A_{2},\ldots,A_{n}$ such that, for $1\leq i<n$ $A_{i}$ implies $A_{i+1}$ , and $A_{n}$ implies $B$ . In the field of proof theory, also beyond the scope of this class,. such proofs are formalized via a finite set of rules that can be applied to (set-theoretic) formulas (see, e.g., [EFT07, Sec. IV], [Kun12, Sec. II]). Once proofs have been formalized in this way, one can, in principle, mechanically check if a given sequence of symbols does, indeed, constitute a valid proof (without even having to understand the actual meaning of the statements). Indeed, several different computer programs have been devised that can be used for automatic proof checking, for example Coq [Wik22a], HOL Light [Wik21], Isabelle [Wik22b] and Lean [Wik22c] to name just a few.  

### A.3 The Axioms of Zermelo-Fraenkel Set Theory  

Axiomatic set theory seems to provide a solid and consistent foundation for conducting mathematics, and most mathematicians have accepted it as the basis of their everyday work. However, there do remain some deep, difficult, and subtle philosophical issues regarding the foundation of logic and mathematics (see, e.g., [Kun12, Sec. 0, Sec. III]).  

Definition and Remark A.6. An axiom is a statement that is assumed to be true without any formal logical justification. The most basic axioms (for example, the standard axioms of set theory) are taken to be justified by common sense or some underlying philosophy. However, on a less fundamental (and less philosophical) level, it is a common mathematical strategy to state a number of axioms (for example, the axioms defining. the mathematical structure called a group), and then to study the logical consequences of these axioms (for example, group theory studies the statements that are true for all. groups as a consequence of the group axioms). For a given system of axioms, the question if there exists an object satisfying all the axioms in the system (i.e. if the system of axioms is consistent, i.e. free of contradictions) can be extremely difficult to answer.  

We are now in a position to formulate and discuss the axioms of axiomatic set the-. ory. More precisely, we will present the axioms of Zermelo-Fraenkel set theory, usually. abbreviated as ZF, which are Axiom 0 - Axiom 8 below. While there exist various set theories in the literature, each set theory defined by some collection of axioms, the axioms of ZFC, consisting of the axioms of ZF plus the axiom of choice (Axiom 9, see. Sec. A.4 below), are used as the foundation of mathematics currently accepted by most. mathematicians.  

#### A.3.1 Existence, Extensionality, Comprehension  

Axiom 0 Existence:  

$$
{\vec{\mathbf{\tau}}}_{X}\quad(X=X).
$$  

Recall that this is just meant to be a more readable transcription of the set-theoretic formula $\exists v_{1}(v_{1}=v_{1})$ . The axiom of existence states that there exists (at least one) set $X$  

In Def. 1.18 two sets are defined to be equal if, and only if, they contain precisely the same elements. In axiomatic set theory, this is guaranteed by the axiom of extensionality:  

Axiom 1 Extensionality:  

$$
{\begin{array}{l l l l}{\forall}&{\forall}&{\left(\forall}&{\left(z\in X\iff z\in Y\right)\Rightarrow X=Y\right).}\end{array}} 
$$  

Following [Kun12], we assume that the substitution property of equality is part of the underlying logic, i.e. if $X=Y$ , then $X$ can be substituted for $Y$ and vice versa without  

changing the truth value of a (set-theoretic) formula. In particular, this yields the converse to extensionality:  

$$
\begin{array}{r l}{\forall}&{{}\forall}\ {X}&{{}Y}\end{array}\quad\left(X=Y\Rightarrow\forall_{z}\quad\left(z\in X\Leftrightarrow z\in Y\right)\right).
$$  

Before we discuss further consequences of extensionality, we would like to have the. existence of the empty set. However, Axioms 0 and. $1$ do not suffice to prove the existence of an empty set (see [Kun12, I.6.3]). This, rather, needs the additional axiom of comprehension. More precisely, in the case of comprehension, we do not have a single axiom, but a scheme of infinitely many axioms, one for each set-theoretic formula. Its formulation makes use of the following definition:.  

Definition A.7. One obtains the universal closure of a set-theoretic formula $\phi$ , by writing $\forall$ in front of $\phi$ for each variable $v_{j}$ that occurs as a free variable in $\phi$ (recall $v_{j}$ from Def. 1.31 that $v_{j}$ is free in $\phi$ if, and only if, it is not bound by a quantifier in $\phi$  

Axiom 2 Comprehension Scheme: For each set-theoretic formula $\phi$ , not containing $Y$ as a free variable, the universal closure of.  

$$
\begin{array}{r l}{{\underset{Y}{\exists}}\quad\forall}&{{}{\Bigl(}x\in Y\Leftrightarrow(x\in X\land\phi){\Bigr)}}\end{array}
$$  

is an axiom. Thus, the comprehension scheme states that, given the set $X$ there exists (at least one) set $Y$ , containing precisely the elements of $X$ that have the property $\phi$  

Remark A.8. Comprehension does not provide uniqueness. However, if both $Y$ and $Y^{\prime}$ are sets containing precisely the elements of. $X$ that have the property $\phi$ , then  

$$
{\begin{array}{r l}{\forall}&{{\Big(}x\in Y\Leftrightarrow{\big(}x\in X\land\phi{\big)}\Leftrightarrow x\in Y^{\prime}{\Big)},}\end{array}} 
$$  

and, then, extensionality implies. $Y=Y^{\prime}$ . Thus, due to extensionality, the set. $Y$ given by comprehension is unique, justifying the notation  

$$
\{x:x\in X\wedge\phi\}:=\{x\in X:\phi\}:=Y
$$  

(this is the axiomatic justification for (1.6)).  

Theorem A.9. There exists a unique empty set (which we denote by. $\varnothing$ or by 0 - it is common to identify the empty set with the number zero in axiomatic set theory).  

Proof. Axiom 0 provides the existence of a set $X$ . Then comprehension allows us to.   
define the empty set by.  

$$
0:=\varnothing:=\{x\in X:x\neq x\},
$$  

where, as explained in Rem. A.8, extensionality guarantees uniqueness.  

Remark A.10. In Rem. A.4 we said that every formula with additional symbols and notation is to be regarded as an abbreviation or transcription of a set-theoretic formula as defined in Def. A.1(b). Thus, formulas containing symbols for defined sets (e.g. 0 or $\varnothing$ for the empty set) are to be regarded as abbreviations for formulas without such. symbols. Some logical subtleties arise from the fact that there is some ambiguity in the way such abbreviations can be resolved: For example,. $0\in X$ can abbreviate either  

$$
:\exists\left(\phi(y)\land y\in X\right)\quad{\mathrm{or}}\quad\chi:\forall\left(\phi(y)\Rightarrow y\in X\right),\quad{\mathrm{where}}\phi(y){\mathrm{stands~for~}}\forall(u):=\phi(y).
$$  

Then $\psi$ and $\chi$ are equivalent if $\vec{\overline{{{y}}}}\cdot\phi(y)$ is true (e.g., if Axioms $0-2$ hold), but they can be nonequivalent, otherwise (see discussion between Lem. 2.9 and Lem. 2.10 in [Kun80, Ch. IV]).  

At first glance, the role played by the free variables in. $\phi$ , which are allowed to occur in Axiom 2, might seem a bit obscure. So let us consider examples to illustrate that allowing free variables (i.e. set parameters) in comprehension is quite natural:.  

Example A.11. (a) Suppose $\phi$ in comprehension is the formula $x\in Z$ (having. $Z$ as a free variable), then the set given by the resulting axiom is merely the intersection of $X$ and $Z$  

$$
X\cap Z:=\{x\in X:\phi\}=\{x\in X:x\in Z\}.
$$  

(b) Note that it is even allowed for $\phi$ in comprehension to have. $X$ as a free variable, so. one can let. $\phi$ be the formula $\exists\quad(x\in u\land u\in X)$ to define the set.  

$$
X^{*}:=\left\{x\in X:{\exists}\quad(x\in u\land u\in X)\right\}.
$$  

Then, if $0:=\emptyset$ $1:=\{0\}$ $2:=\{0,1\}$ , we obtain  

$$
2^{*}=\{0\}=1.
$$  

It is a consequence of extensionality that the mathematical universe consists of sets and only of sets: Suppose there were other objects in the mathematical universe, for example a cow $C$ and a monkey $M$ (or any other object without elements, other than. the empty set) - this would be equivalent to allowing a cow or a monkey (or any other. object without elements, other than the empty set) to be considered a set, which would mean that our set-theoretic variables $v_{j}$ were allowed to be a cow or a monkey as well. However, extensionality then implies the false statement $C=M=\emptyset$ , thereby excluding cows and monkeys from the mathematical universe..  

Similarly, $\{C\}$ and $\{M\}$ (or any other object that contains a non-set), can not be inside the mathematical universe. Indeed, otherwise we had  

$$
\begin{array}{r l}{\forall}&{{}\left(x\in\{C\}\Leftrightarrow x\in\{M\}\right)}\end{array}
$$  

(as $C$ and $M$ are non-sets) and, by extensionality,. $\{C\}=\{M\}$ were true, in contradiction to a set with a cow inside not being the same as a set with a monkey inside. Thus,. we see that all objects of the mathematical universe must be so-called hereditary sets, i.e. sets all of whose elements (thinking of the elements as being the children of the sets) are also sets.  

#### A.3.2 Classes  

As we need to avoid contradictions such as Russell's antinomy, we must not require the existence of a set $\{x:\phi\}$ for each set-theoretic formula $\phi$ .However, it can still be useful to think of a "collection' of all sets having the property $\phi$ . Such collections are commonly called classes:  

Definition A.12. (a) If $\phi$ is a set-theoretic formula, then we call. $\{x:\phi\}$ a class, namely the class of all sets that have the property $\phi$ (typically, $\phi$ will have $x$ as a free variable).  

(b) If $\phi$ is a set-theoretic formula, then we say the class $\{x:\phi\}$ exists (as a set) if, and only if  

$$
{\begin{array}{r l}{{\underset{X}{\rightleftharpoons}}}&{{\left(\forall\atop x}\quad\left(x\in X\Leftrightarrow\phi\right)\right)}\end{array}}
$$  

is true. Then. $X$ is actually unique by extensionality and we identify $X$ with the class $\{x:\phi\}$ . If (A.4) is false, then. $\{x:\phi\}$ is called a proper class (and the usual. interpretation is that the class is in some sense "too large" to be a set).  

Example A.13. (a) Due to Russell's antinomy of Sec. A.1, we know that ${\mathbf{R}}:=\{x\::$ $x\not\in x\}$ forms a proper class.  

(b) The universal class of all sets, $\mathbf{V}:=\{x:x=x\}$ , is a proper class. Once again, this is related to Russell's antinomy: If $\mathbf{V}$ were a set, then  

$$
\mathbf{R}=\{x:x\not\in x\}=\{x:x=x\wedge x\not\in x\}=\{x:x\in\mathbf{V}\wedge x\not\in x\}
$$  

would also be a set by comprehension. However, this is in contradiction to $\mathbf{R}$ being a proper class by (a).  

Remark A.14. From the perspective of formal logic, statements involving proper classes are to be regarded as abbreviations for statements without proper classes. For example, it turns out that the class $\mathbf{G}$ of all sets forming a group is a proper class. But we might write $G\in\mathbf G$ as an abbreviation for the statement "The set $G$ is a group."  

#### A.3.3 Pairing, Union, Replacement  

Axioms $0-2$ are still consistent with the empty set being the only set in existence (see [Kun12, I.6.13]). The next axiom provides the existence of nonempty sets:  

Axiom 3 Pairing:  

$$
\forall\forall\exists{\big(}x\in Z\land y\in Z{\big)}.
$$  

Thus, the pairing axiom states that, for all sets $x$ and $y$ , there exists a set $Z$ that contains $x$ and $y$ as elements.  

In consequence of the pairing axiom, the sets  

$$
\begin{array}{l}{0:=\emptyset,}\ {1:=\{0\},}\ {2:=\{0,1\}}\end{array}
$$  

all exist. More generally, we may define:  

Definition A.15. If $x,y$ are sets and $Z$ is given by the pairing axiom, then we call  

(a) $\{x,y\}:=\{u\in Z:u=x\vee u=y\}$ the unordered pair given by $x$ and $y$  

(b) $\{x\}:=\{x,x\}$ the singleton set given by $x$  

(c) $(x,y):=\{\{x\},\{x,y\}\}$ the ordered pair given by. $x$ and $y$ (cf. Def. 2.1).  

We can now show that ordered pairs behave as expected:  

Lemma A.16. The following holds true:  

$$
\begin{array}{r l}{\underset{x,y,x^{\prime},y^{\prime}}{\forall}}&{\Big((x,y)=(x^{\prime},y^{\prime})\Leftrightarrow(x=x^{\prime})\land(y=y^{\prime})\Big).}\end{array}
$$  

Proof. $\Leftarrow$ " is merely  

$$
(x,y)=\{\{x\},\{x,y\}\}\stackrel{x=x^{\prime},y=y^{\prime}}{=}\{\{x^{\prime}\},\{x^{\prime},y^{\prime}\}\}=(x^{\prime},y^{\prime}).
$$  

$\ '\Rightarrow\ '$ is done by distinguishing two cases: If $x=y$ , then  

$$
\{\{x\}\}=(x,y)=(x^{\prime},y^{\prime})=\{\{x^{\prime}\},\{x^{\prime},y^{\prime}\}\}.
$$  

Next, by extensionality, we first get $\{x\}=\{x^{\prime}\}=\{x^{\prime},y^{\prime}\}$ , followed by $x=x^{\prime}=y^{\prime}$ establishing the case. If $x\neq y$ , then  

$$
\{\{x\},\{x,y\}\}=(x,y)=(x^{\prime},y^{\prime})=\{\{x^{\prime}\},\{x^{\prime},y^{\prime}\}\}.
$$  

where, by extensionality $\{x\}\neq\{x,y\}\neq\{x^{\prime}\}$ . Thus, using extensionality again, $\{x\}=$ $\{x^{\prime}\}$ and $x=x^{\prime}$ . Next, we conclude  

$$
\{x,y\}=\{x^{\prime},y^{\prime}\}=\{x,y^{\prime}\}
$$  

and a last application of extensionality yields $y=y^{\prime}$  

While we now have the existence of the infinitely many different sets $0,\{0\},\{\{0\}\},\{\{\cdot\cdot\cdot,$ we are not, yet, able to form sets containing more than two elements. This is remedied by the following axiom:  

Axiom 4 Union:  

$$
\forall_{M}\exists\forall_{x}\forall_{X}{\Big(}(x\in X\land X\in{\mathcal{M}})\Rightarrow x\in Y{\Big)}.
$$  

Thus, the union axiom states that, for each set of sets $\mathcal{M}$ , there exists a set $Y$ containing all elements of elements of $\mathcal{M}$  

Definition A.17. (a) If. $\mathcal{M}$ is a set and. $Y$ is given by the union axiom, then define  

$$
\bigcup{\mathcal{M}}:=\bigcup_{X\in{\mathcal{M}}}X:=\left\{x\in Y:{\underset{X\in{\mathcal{M}}}{\exists}}\quad x\in X\right\}.
$$  

(b) If $X$ and $Y$ are sets, then define  

$$
X\cup Y:=\bigcup\{X,Y\}.
$$  

(c) If $x,y,z$ are sets, then define  

$$
\{x,y,z\}:=\{x,y\}\cup\{z\}.
$$  

Remark A.18. (a) The definition of set-theoretic unions as  

$$
\bigcup_{i\in I}A_{i}:=\left\{x:\exists_{i\in I}x\in A_{i}\right\}
$$  

in (1.25b) will be equivalent to the definition in Def. A.17(a) if we are allowed to form the set  

$$
{\mathcal{M}}:=\{A_{i}:i\in I\}.
$$  

If $I$ is a set and $A_{i}$ is a set for each $i\in I$ , then $\mathcal{M}$ as above will be a set by Axiom 5 below (the axiom of replacement).  

(b) In contrast to unions, intersections can be obtained directly from comprehension without the introduction of an additional axiom: For example  

$$
\begin{array}{l}{{X\cap Y:=\{x\in X:x\in Y\},}}\ {{\bigcap_{i\in I}A_{i}:=\left\{x\in A_{i_{0}}:\forall\mathrel{\stackrel{\rightharpoonup}{i\in I}}x\in A_{i}\right\},}}\end{array}
$$  

where $i_{0}\in I\neq\emptyset$ is an arbitrary fixed element of $I$  

(c) The union  

$$
\bigcup\emptyset=\bigcup_{X\in\emptyset}X=\bigcup_{i\in\emptyset}A_{i}=\emptyset
$$  

is the empty set - in particular, a set. However,  

$$
\bigcap\varnothing=\left\{x:\forall_{X\in\varnothing}x\in X\right\}=\mathbf{V}=\left\{x:\forall_{i\in\varnothing}x\in A_{i}\right\}=\bigcap_{i\in\varnothing}A_{i},
$$  

i.e. the intersection over the empty set is the class of all sets - in particular, a proper class and not a set.  

Definition A.19. We define the successor function  

$$
x\mapsto S(x):=x\cup\{x\}\quad{\mathrm{(for~each~set~}}x{\mathrm{)}}.
$$  

Thus, recalling (A.5), we have $1=S(0)$ $2=S(1)$ ; and we can define $3:=S(2)$ ,... In general, we call the set $S(x)$ the successor of the set $x$  

In Def. 2.3 and Def. 2.19, respectively, we define functions and relations in the usual manner, making use of the Cartesian product $A\times B$ of two sets $A$ and $B$ ,which, according to (2.2) consists of all ordered pairs $(x,y)$ , where $x\in A$ and $y\in B$ . However, Axioms $0-4$ are not sufficient to justify the existence of Cartesian products. To obtain Cartesian products, we employ the axiom of replacement. Analogous to the axiom of comprehension, the following axiom of replacement actually consists of a scheme of infinitely many axioms, one for each set-theoretic formula:  

Axiom 5 Replacement Scheme: For each set-theoretic formula, not containing $Y$ as a free variable, the universal closure of.  

$$
\left(\underset{x\in X}{\forall}\underset{y}{\exists}!\phi\right)\quad\Rightarrow\quad\left(\underset{Y}{\exists}\quad\underset{x\in X}{\forall}\quad\underset{y\in Y}{\exists}\quad\phi\right)
$$  

is an axiom. Thus, the replacement scheme states that if, for each $x\in X$ there exists a unique $y$ having the property $\phi$ (where, in general, $\phi$ will depend on $x$ ), then there exists a set $Y$ that, for each $x\in X$ , contains this $y$ with property $\phi$ . One can view this as obtaining. $Y$ by replacing each $x\in X$ by the corresponding $y=y(x)$  

Theorem A.20. If. $A$ and $B$ are sets, then the Cartesian product of $A$ and $B$ , i.e. the class  

exists as a set.  

$$
A\times B:=\left\{x:\underset{a\in A}{\exists}\quad\underset{b\in B}{\exists}\quad x=(a,b)\right\}
$$  

Proof. For each $a\in A$ , we can use replacement with $X:=B$ and $\phi:=\phi_{a}$ being the formula $y=(a,x)$ to obtain the existence of the set  

$$
\{a\}\times B:=\{(a,x):x\in B\}
$$  

(in the usual way, comprehension and extensionality were used as well). Analogously, using replacement again with. $X:=A$ and $\phi$ being the formula ${\boldsymbol{y}}=\{{\boldsymbol{x}}\}\times{\boldsymbol{B}}$ , we obtain the existence of the set.  

$$
\mathcal{M}:=\{\{x\}\times B:x\in A\}.
$$  

In a final step, the union axiom now shows  

$$
\bigcup{\mathcal{M}}=\bigcup_{a\in A}\{a\}\times B=A\times B
$$  

to be a set as well.  

#### A.3.4 Infinity, Ordinals, Natural Numbers  

The following axiom of infinity guarantees the existence of infinite sets (e.g., it will allow us to define the set of natural numbers $\mathbb{N}$ , which is infinite by Th. A.46 below).  

Axiom 6 Infinity:  

$$
\begin{array}{r l}{\underset{X}{\rightleftharpoons}}&{{}\left(0\in X\wedge\underset{x\in X}{\forall}\right.\left(x\cup\{x\}\in X\right)\right).}\end{array}
$$  

Thus, the infinity axiom states the existence of a set $X$ containing $\varnothing$ (identified with the number $0$ , and, for each of its elements $x$ , its successor $S(x)=x\cup\{x\}$  

In preparation for our official definition of $\mathbb{N}$ in Def. A.41 below, we will study so-called ordinals, which are special sets also of further interest to the field of set theory (the natural numbers will turn out to be precisely the finite ordinals). We also need some notions from the theory of relations, in particular, order relations (cf. Def. 2.19 and Def. 2.23).  

Definition A.21. Let $R$ be a relation on a set $X$ (a) $R$ is called asymmetric if, and only if,  

$$
\begin{array}{r l}{\forall_{x,y\in X}}&{{}{\Big(}x R y\Rightarrow\neg(y R x){\Big)},}\end{array}
$$  

i.e. if $x$ is related to $y$ only if $y$ is not related to $x$ (b) $R$ is called a strict partial order if, and only if, $R$ is asymmetric and transitive. It is noted that this is consistent with Not. 2.24, since, recalling the notation $\Delta(X):=$ $\{(x,x):x\in X\}$ $R$ is a partial order on $X$ if, and only if, $R\backslash\Delta(X)$ is a strict partial order on $X$ . We extend the notions lower/upper bound, min, max, inf, sup. of Def. 2.25 to strict partial orders $R$ by applying them to $R\cup\Delta(X)$ : We call $x\in X$ a lower bound of $Y\subseteq X$ with respect to. $R$ if, and only if,. $x$ is a lower bound of $Y$ with respect to. $R\cup\Delta(X)$ , and analogous for the other notions.  

(c) A strict partial order $R$ is called a strict total order or a strict linear order if, and only if, for each $x,y\in X$ , one has $x=y$ or $x R y$ or $y R x$  

(d) $R$ is called a (strict) well-order if, and only if, $R$ is a (strict) total order and every nonempty subset of. $X$ has a min with respect to $R$ (for example, the usual $\leq$ constitutes a well-order on N (see, e.g., [Phi16, Th. D.5]), but not on $\mathbb{R}$ (e.g., $\mathbb{R}^{+}$ does not have a min))..  

(e) If $Y\subseteq X$ , then the relation on $Y$ defined by  

$$
x S y:\Leftrightarrow x R y
$$  

is called the restriction of $R$ to $Y$ , denoted $S=R{\upharpoonright_{Y}}$ (usually, one still writes $R$ for the restriction).  

Lemma A.22. Let $R$ be a relation on a set $X$ and $Y\subseteq X$ (c) If R is antisymmetric, then $R\upharpoonright$ is antisymmetric.  

(d) If R is asymmetric, then $R\upharpoonright$ is asymmetric.  

(e) If $R$ is a (strict) partial order, then $R\upharpoonright$ is a (strict) partial order..  

(f) If $R$ is a (strict) total order, then $R\upharpoonright$ is a (strict) total order.  

Proof. (a): If $a,b,c\in Y$ with $a R b$ and $b R c$ , then $a R c$ , since $a,b,c\in X$ and $R$ is transitive on $X$  

(b): If $a\in Y$ , then $a\in X$ and $a R a$ , since $R$ is reflexive on. $X$   
(c): If $a,b\in Y$ with $a R b$ and $b R a$ , then $a=b$ , since $a,b\in X$ and $R$ is antisymmetric on $X$   
(d): If $a,b\in Y$ with $a R b$ , then $\neg b R a$ , since $a,b\in X$ and $R$ is asymmetric on $X$ (e) follows by combininge $\mathrm{(a)-(d)}$   
(f): If $a,b\in Y$ with $a\neq b$ and $\neg a R b$ , then $b R a$ , since $a,b\in X$ and $R$ is total on $X$ Combining this with (e) yields (f).  

(g): Due to (f), it merely remains to show that every nonempty subset $Z\subseteq Y$ has a min. However, since $Z\subseteq X$ and $R$ is a well-order on $X$ , there is $m\in Z$ such that $m$ is a min for $R$ on $X$ , implying $m$ to be a min for $R$ on $Y$ as well.  

Remark A.23. Since the universal class. $\mathbf{V}$ is not a set, $\in$ is not a relation in the sense of Def. 2.19. It can be considered as a "class relation"', i.e. a subclass of $\mathbf{V}\times\mathbf{V}$ , but it is a proper class. However, $\in$ does constitute a relation in the sense of Def. 2.19 on. each set $X$ (recalling that each element of. $X$ must be a set as well). More precisely, if. $X$ is a set, then so is  

$$
R_{\in}:=\{(x,y)\in X\times X:x\in y\}.
$$  

Then  

$$
\forall_{x,y\in X}\quad(x,y)\in R_{\in}\quad\Leftrightarrow\quad x\in y.
$$  

Definition A.24. A set. $X$ is called transitive if, and only if, every element of $X$ is also a subset of $X$  

$$
\forall_{x\in X}x\subseteq X.
$$  

Clearly, (A.9a) is equivalent to  

$$
{\underset{x,y}{\forall}}\quad{\Bigl(}x\in y\land y\in X\Rightarrow x\in X{\Bigr)}.
$$  

Lemma A.25. If $X,Y$ are transitive sets, then $X\cap Y$ is a transitive set..  

Proof. If $x\in X\cap Y$ and $y\in x$ , then $y\in X$ (since $X$ is transitive) and $y\in Y$ (since $Y$ is transitive). Thus $y\in X\cap Y$ , showing $X\cap Y$ is transitive..  

Definition A.26. (a) A set. $\alpha$ is called an ordinal number or just an ordinal if, and only if, $\alpha$ is transitive and $\in$ constitutes a strict well-order on. $\alpha$ . An ordinal. $\alpha$ is called a successor ordinal if, and only if, there exists an ordinal. $\beta$ such that $\alpha=S(\beta)$ , where. $S$ is the successor function of Def. A.19. An ordinal $\alpha\neq0$ is called a limit ordinal. if, and only if, it is not a successor ordinal. We denote the class of all ordinals by ON (it is a proper class by Cor. A.33 below).  

(b) We define  

$$
\begin{array}{r l}{\underset{\alpha,\beta\in\mathbf{ON}}{\forall}}&{(\alpha<\beta:\Leftrightarrow\alpha\in\beta),}\ {\underset{\alpha,\beta\in\mathbf{ON}}{\forall}}&{(\alpha\leq\beta:\Leftrightarrow\alpha<\beta\lor\alpha=\beta).}\end{array}
$$  

Example A.27. Using (A.5),. $0=\emptyset$ is an ordinal, and $1=S(0)$ $2=S(1)$ are both successor ordinals (in Prop. A.43, we will identify $\ensuremath{\mathbb{N}}_{0}$ as the smallest limit ordinal). Even. though $X:=\{1\}$ and $Y:=\{0,2\}$ are well-ordered by $\in$ , they are not ordinals, since. they are not transitive sets:. $1\in X$ , but $1\nsubseteq X$ (since $0\in1$ , but $0\not\in X$ ); similarly, $1\in2\in Y$ , but $1\not\in Y$  

Lemma A.28. No ordinal contains itself, i.e  

$$
\forall_{\alpha\in\mathbf{ON}}\quad\alpha\notin\alpha.
$$  

Proof. If $\alpha$ is an ordinal, then $\in$ is a strict order on $\alpha$ .Due to asymmetry of strict orders, $x\in x$ can not be true for any element of $\alpha$ , implying that $\alpha\in\alpha$ can not be true.  

Proposition A.29. Every element of an ordinal is an ordinal, i.e.  

$$
\begin{array}{r l}{\underset{\alpha\in\mathbf{ON}}{\forall}}&{{}\Big(X\in\alpha\Rightarrow X\in\mathbf{ON}\Big)}\end{array}
$$  

(in other words, ON is a transitive class).  

Proof. Let $\alpha\in\mathrm{{ON}}$ and $X\in\alpha$ .Since $\alpha$ is transitive, we have $X\subseteq\alpha$ .As $\in$ is a strict well-order on $\alpha$ , it must also be a strict well-order on $X$ by Lem. A.22(g). In consequence, it only remains to prove that $X$ is transitive as well. To this end, let $x\in X$ . Then $x\in\alpha$ , as $\alpha$ is transitive. If. $y\in x$ , then, using transitivity of $\alpha$ again, $y\in\alpha$ . Now $y\in X$ , as $\in$ is transitive on. $\alpha$ , proving $x\subseteq X$ , i.e. $X$ is transitive..  

Proposition A.30. If $\alpha,\beta\in{\bf O N}$ , then $X:=\alpha\cap\beta\in{\bf O N}$ (we will see in Th. A.35(a) below that, actually, $\alpha\cap\beta=\operatorname*{min}\{\alpha,\beta\})$  

Proof. $X$ is transitive by Lem. A.25, and, since $X\subseteq\alpha$ $\in$ is a strict well-order on. $X$ by Lem. A.22(g). $\vert$  

Proposition A.31. On the class ON, the relation $\leq$ (as defined in (A.10)) is the same.   
as the relation $\subseteq$ , i.e.  

$$
\begin{array}{r l}{\underset{\alpha,\beta\in\mathbf{ON}}{\forall}}&{\Big(\alpha\leq\beta\Leftrightarrow\alpha\subseteq\beta\Leftrightarrow(\alpha\in\beta\lor\alpha=\beta)\Big).}\end{array}
$$  

Proof. Let $\alpha,\beta\in{\bf O N}$  

Assume $\alpha\leq\beta$ . If $\alpha=\beta$ , then $\alpha\subseteq\beta$ . If $\alpha\in\beta$ , then $\alpha\subseteq\beta$ , since $\beta$ is transitive.  

Conversely, assume $\alpha\subseteq\beta$ and $\alpha\neq\beta$ .We have to show $\alpha\in\beta$ .To this end, we set $X:=\beta\backslash\alpha$ . Then $X\neq\emptyset$ and, as $\in$ well-orders $\beta$ , we can let $m:=\operatorname*{min}X$ .We will show $r n=\alpha$ (note that this will complete the proof, due to $\alpha=m\in X\subseteq\beta$ ). If $\mu\in m$ , then $\mu\in\beta$ (since $m\in\beta$ and $\beta$ is transitive) and $\mu\not\in X$ (since $m=\operatorname*{min}X$ ), implying $\mu\in\alpha$ (since $X=\beta\backslash\alpha$ ) and, thus, $m\subseteq\alpha$ . Seeking a contradiction, assume. $m\neq\alpha$ . Then there must be some $\gamma\in\alpha\backslash m\subseteq\alpha\subseteq\beta$ . In consequence $\gamma,m\in\beta$ . As $\gamma\notin m$ and $\in$ is a total order on $\beta$ , we must have either. $m=\gamma$ or $m\in\gamma$ . However, $m\neq\gamma$ , since $\gamma\in\alpha$ and $m\not\in\alpha$ (as $m\in X$ ). So it must be $m\in\gamma\in\alpha$ , implying $m\in\alpha$ , as $\alpha$ is transitive.. This contradiction proves $\prime n=\alpha$ and establishes the proposition..  

Theorem A.32. The class ON is well-ordered $b y\in$ , i.e.  

(i) $\in$ is transitive on ON:  

$$
\begin{array}{r l}{\forall}&{{}\Bigl(\alpha<\beta\land\beta<\gamma\Rightarrow\alpha<\gamma\Bigr).}\end{array}
$$  

(ii) E is asymmetric on ON:  

$$
\begin{array}{r l}{\forall_{\alpha,\beta\in\mathbf{ON}}}&{{}\Big(\alpha<\beta\Rightarrow\neg(\beta<\alpha)\Big).}\end{array}
$$  

(iii) Ordinals are always comparable:  

$$
\begin{array}{r l}{\underset{\alpha,\beta\in\mathbf{ON}}{\forall}}&{{}\Big(\alpha<\beta\lor\beta<\alpha\lor\alpha=\beta\Big).}\end{array}
$$  

(iv) Every nonempty set of ordinals has a min.  

Proof. (i) is clear, as $\gamma$ is a transitive set.  

(ii): If $\alpha,\beta\in\mathrm{{ON}}$ , then $\alpha\in\beta\in\alpha$ implies $\alpha\in\alpha$ by (i), which is a contradiction to Lem. A.28.  

(iii): Let $\gamma:=\alpha\cap\beta$ . Then $\gamma\in\mathbf{ON}$ by Prop. A.30. Thus  

$$
\gamma\subseteq\alpha\land\gamma\subseteq\beta\quad{\stackrel{\mathrm{Lem.,A.31}}{\Rightarrow}}\quad(\gamma\in\alpha\lor\gamma=\alpha)\land(\gamma\in\beta\lor\gamma=\beta).
$$  

If $\gamma\in\alpha$ and $\gamma\in\beta$ , then $\gamma\in\alpha\cap\beta=\gamma$ , in contradiction to Lem. A.28. Thus, by (A.12), $\gamma=\alpha$ or $\gamma=\beta$ . If $\gamma=\alpha$ , then $\alpha\subseteq\beta$ . If $\gamma=\beta$ , then $\beta\subseteq\alpha$ , completing the proof of. (iii).  

(iv): Let $X$ be a nonempty set of ordinals and consider $\alpha\in X$ .If $\alpha=\operatorname*{min}X$ , then we are already done. Otherwise,. $Y:=\alpha\cap X=\{\beta\in X:\beta\in\alpha\}\neq\emptyset$ . Since $\alpha$ is well-ordered by $\in$ , there is $m:=\operatorname*{min}Y$ . If $\beta\in X$ , then either $\beta<\alpha$ or $\alpha\leq\beta$ by (iii). If $\beta<\alpha$ , then $\beta\in Y$ and $m\leq\beta$ . If $\alpha\leq\beta$ , then $m<\alpha\leq\beta$ . Thus, $m=\operatorname*{min}X$ proving (iv).  

Corollary A.33. ON is a proper class (i.e. there is no set containing all the ordinals).  

Proof. If there is a set $X$ containing all ordinals, then, by comprehension, $\beta:=0\mathrm{{N}=}$ $\{\alpha\in X:\alpha$ is an ordinal} must be a set as well. But then Prop. A.29 says that the set $\beta$ is transitive and Th. A.32 yields that the set $\beta$ is well-ordered by $\in$ , implying $\beta$ to be an ordinal, i.e. $\beta\in\beta$ in contradiction to Lem. A.28.  

Corollary A.34. For each set $X$ of ordinals, we have:.  

(a) $X$ is well-ordered by $\in$  

(b) $X$ is an ordinal if, and only if, $X$ is transitive. Note: A transitive set of ordinals $X$ is sometimes called an initial segment of ON, since, here, transitivity can be restated in the form  

$$
\begin{array}{r}{{\underset{\alpha\in{\bf O N}}{\forall}}\quad\underset{\beta\in X}{\forall}\quad\left(\alpha<\beta\Rightarrow\alpha\in X\right).}\end{array}
$$  

Proof. (a) is a simple consequence of Th. A.32(i)-(iv).  

(b) is immediate from (a).  

Theorem A.35. Let. $X$ be a nonempty set of ordinals.  

(a) Then $\gamma:=\cap X$ is an ordinal, namely $\gamma=\operatorname*{min}X$ .In particular, if $\alpha,\beta\in\mathrm{{ON}}$ then $\operatorname*{min}\{\alpha,\beta\}=\alpha\cap\beta$  

(b) Then $\delta:=\cup X$ is an ordinal, namely $\delta=\operatorname*{sup}X$ . In particular, if $\alpha,\beta\in{\mathrm{{ON}}}$ , then $\operatorname*{max}\{\alpha,\beta\}=\alpha\cup\beta$  

Proof. (a): Let. $m:=\operatorname*{min}X$ . Then $\gamma\subseteq m$ , since $m\in X$ .Conversely, if $\alpha\in X$ , then $m\leq\alpha$ implies $m\subseteq\alpha$ by Prop. A.31, i.e. $m\subseteq\gamma$ . Thus, $m=\gamma$ , proving (a).  

(b): To show. $\delta\in\mathrm{ON}$ , we need to show. $\delta$ is transitive (then. $\delta$ is an ordinal by Cor.. A.34(b)). If $\alpha\in\delta$ , then there is $\beta\in X$ such that $\alpha\in\beta$ . Thus, if $\gamma\in\alpha$ , then $\gamma\in\beta$ since $\beta$ is transitive. As. $\gamma\in\beta$ implies $\gamma\in\delta$ , we see that $\delta$ is transitive, as needed. It remains to show $\delta=\operatorname*{sup}X$ . If $\alpha\in X$ , then $\alpha\subseteq\delta$ , i.e. $\alpha\leq\delta$ , showing $\delta$ to be an upper bound for $X$ . Now let $u\in\mathrm{ON}$ be an arbitrary upper bound for $X$ , i.e.  

$$
\forall_{\alpha\in X}\alpha\subseteq u.
$$  

Thus, $\delta\subseteq u$ , i.e. $\delta\leq u$ , proving $\delta=\operatorname*{sup}X$  

Next, we obtain some results regarding the successor function of Def. A.19 in the context of ordinals.  

Lemma A.36. We have  

$$
\begin{array}{r l}{\underset{\alpha\in\mathbf{ON}}{\forall}}&{{}\Big(x,y\in S(\alpha)\wedge x\in y\quad\Rightarrow\quad x\neq\alpha\Big).}\end{array}
$$  

Proof. Seeking a contradiction, we reason as follows:  

$$
x=\alpha{\stackrel{\alpha\neq\alpha}{\Rightarrow}}y\neq\alpha{\stackrel{y\in S(\alpha)}{\Rightarrow}}y\in\alpha{\stackrel{\alpha{\mathrm{~transitive}}}{\Rightarrow}}y\subseteq\alpha{\stackrel{x\in y}{\Rightarrow}}\alpha\in\alpha.
$$  

This contradiction to $\alpha\not\in\alpha$ yields $x\neq\alpha$ , concluding the proof.  

Proposition A.37. For each $\alpha\in\mathrm{ON}$ , the following holds:.  

(a) $S(\alpha)\in\mathbf{ON}$ (b) $\alpha<S(\alpha)$  

(c) For each ordinal $\beta$ $\beta<S(\alpha)$ holds if, and only if, $\beta\leq\alpha$ (d) For each ordinal $\beta$ , if $\beta<\alpha$ , then. $S(\beta)<S(\alpha)$  

(e) For each ordinal $\beta$ , if $S(\beta)<S(\alpha)$ , then $\beta<\alpha$  

Proof. (a): Due to Prop. A.29,. $S(\alpha)$ is a set of ordinals. Thus, by Cor. A.34(b), it merely remains to prove that. $S(\alpha)$ is transitive.Let. $x\in S(\alpha)$ . If $x=\alpha$ , then $x=$ $\alpha\subseteq\alpha\cup\{\alpha\}=S(\alpha)$ .If $x\neq\alpha$ , then $x\in\alpha$ and, since $\alpha$ is transitive, this implies. $x\subseteq\alpha\subseteq S(\alpha)$ , showing $S(\alpha)$ to be transitive, thereby completing the proof of (a).  

(b) holds, as $\alpha\in S(\alpha)$ holds by the definition of $S(\alpha)$  

(c) is clear, since, for each ordinal $\beta$  

$$
\beta<S(\alpha)\Leftrightarrow\beta\in S(\alpha)\Leftrightarrow\beta\in\alpha\lor\beta=\alpha\Leftrightarrow\beta\leq\alpha.
$$  

(d): If $\beta<\alpha$ , then $S(\beta)=\beta\cup\{\beta\}\subseteq\alpha$ , i.e. $S(\beta)\leq\alpha<S(\alpha)$  

(e) follows from (d) using contraposition: If $\neg(\beta<\alpha)$ , then $\beta=\alpha$ or $\alpha<\beta$ , implying $S(\beta)=S(\alpha)$ or $S(\alpha)<S(\beta)$ , i.e. $\neg(S(\beta)<S(\alpha))$  

We now proceed to define the natural numbers:  

Definition A.38. An ordinal. $n$ is called a natural number if, and only if,  

$$
n\neq0\land\ y_{m\in\mathbf{ON}}\quad\left(m\leq n\Rightarrow m=0\lor m{\mathrm{~is~successor~ordinal}}\right).
$$  

Proposition A.39. If $n=0$ or $n$ is a natural number, then $S(n)$ is a natural number and every element of $n$ is a natural number or $0$  

Proof. Suppose. $n$ is $0$ or a natural number. If $m\in n$ , then $m$ is an ordinal by Prop. A.29. Suppose $m\neq0$ and $k\in m$ . Then $k\in n$ , since $n$ is transitive. Since $n$ is a natural number, $k=0$ or $k$ is a successor ordinal. Thus, $m$ is a natural number. It remains to show that. $S(n)$ is a natural number. By definition,. $S(n)=n\cup\{n\}\ne0$ . Moreover,. $S(n)\in\mathbf{ON}$ by Prop. A.37(a), and, thus, $S(n)$ is a successor ordinal. If $m\in S(n)$ , then $m\leq n$ , implying $m=0$ or $m$ is a successor ordinal, completing the proof that $S(n)$ is a natural number.  

Theorem A.40 (Principle of Induction). If $X$ is a set satisfying.  

$$
0\in X\land\forall\quad S(x)\in X,
$$  

then $X$ contains 0 and all natural numbers.  

Proof. Let $X$ be a set satisfying (A.14). Then $0\in X$ is immediate. Let $n$ be a natural number and, seeking a contradiction, assume $n\not\in X$ . Consider $N:=S(n)\backslash X$ . According to Prop. A.39, $S(n)$ is a natural number and all nonzero elements of $S(n)$ are natural numbers. Since $N\subseteq S(n)$ and $0\in X$ $0\notin N$ and all elements of $N$ must be natural numbers. As $n\in N$ $N\neq0$ . Since $S(n)$ is well-ordered by. $\in$ and $0\neq N\subseteq S(n)$ $N$ must have a min $m\in N$ $0\neq m\le n$ . Since $m$ is a natural number, there must be $k$ such that $m=S(k)$ . Then $k<m$ , implying $k\notin N$ . On the other hand  

$$
k<m\land m\leq n\Rightarrow k\leq n\Rightarrow k\in S(n).
$$  

Thus, $k\in X$ , implying. $m=S(k)\in X$ , in contradiction to. $m\in N$ . This contradiction proves $n\in X$ , thereby establishing the case. $\vert$  

Definition A.41. If the set. $X$ is given by the axiom of infinity, then we use comprehension to define the set.  

$$
{\mathbb{N}}_{0}:=\{n\in X:n=0\vee n{\mathrm{~is~a~natural~number}}\}
$$  

and note $\ensuremath{\mathbb{N}}_{0}$ to be unique by extensionality. We also denote $\mathbb{N}:=\mathbb{N}_{0}\setminus\{0\}$ . In set theory,. it is also very common to use the symbol $\omega$ for the set $\ensuremath{\mathbb{N}}_{0}$  

Corollary A.42. $\ensuremath{\mathbb{N}}_{0}$ is the set of all natural numbers and 0, i.e.  

$$
\begin{array}{r l}{\forall}&{{}\left(n\in\mathbb{N}_{0}\Leftrightarrow n=0\lor n i s a n a t u r a l n u m b e r\right).}\end{array}
$$  

Proof. $\Longrightarrow$ " is clear from Def. A.41 and $\Leftarrow$ " is due to Th. A.40.  

Proposition A.43.. $\omega=\ensuremath{\mathbb{N}}_{0}$ is the smallest limit ordinal.  

Proof. Since. $\omega$ is a set of ordinals and. $\omega$ is transitive by Prop. A.39, $\omega$ is an ordinal. by Cor. A.34(b). Moreover $\omega\neq0$ , since $0\in\omega$ ; and $\omega$ is not a successor ordinal (if $\omega=S(n)=n\cup\{n\}$ ,then $n\in\omega$ and $S(n)\in\omega$ by Prop. A.39, in contradiction to $\omega=S(n)$ ), implying it is a limit ordinal. To see that $\omega$ is the smallest limit ordinal, let. $\alpha\in\mathrm{ON}$ $\alpha<\omega$ . Then $\alpha\in\omega$ , that means. $\alpha=0$ or $\alpha$ is a natural number (in particular, a successor ordinal).  

In the following Th. A.44, we will prove that $\mathbb{N}$ satisfies the Peano axioms P1 - P3 of Sec. 3.1 (if one prefers, one can show the same for $\ensuremath{\mathbb{N}}_{0}$ , where 0 takes over the role of 1).  

Theorem A.44. The set of natural numbers N satisfies the Peano axioms P1 - P3 of Sec. 3.1.  

Proof. For P1 and P2, we have to show that, for each $n\in\mathbb{N}$ , one has $S(n)\in\mathbb{N}\setminus\{1\}$ and that $S(m)\neq S(n)$ for each $m,n\in\mathbb{N}$ $m\neq n$ . Let $n\in\mathbb N$ . Then $S(n)\in\mathbb{N}$ by Prop. A.39. If $S(n)=1$ , then $n<S(n)=1$ by Prop. A.37(b), i.e. $n=0$ , in contradiction to $n\in\mathbb N$ . If $m,n\in\mathbb{N}$ with $m\neq n$ , then $S(m)\neq S(n)$ is due to Prop. A.37(d). To prove P3, suppose $A\subseteq\mathbb{N}$ has the property that $1\in A$ and $S(n)\in A$ for each $n\in A$ . We need to show $A=\mathbb{N}$ (i.e. $\mathbb{N}\subseteq A$ , as $A\subseteq\mathbb{N}$ is assumed). Let $X:=A\cup\{0\}$ . Then $X$ satisfies (A.14) and Th. A.40 yields $\ensuremath{\mathbb{N}}_{0}\subseteq X$ . Thus, if $n\in\mathbb{N}$ , then $n\in X\backslash\{0\}=A$ , showing $\mathbb{N}\subseteq A$  

Notation A.45. For each $n\in\ensuremath{\mathbb{N}}_{0}$ , we introduce the notation $n+1:=S(n)$ (more generally, one also defines. $\alpha+1:=S(\alpha)$ for each ordinal $\alpha$  

Theorem A.46. Let $n\in\ensuremath{\mathbb{N}}_{0}$ .Then $A:=\mathbb{N}_{0}\setminus n$ is infinite (see Def. 3.10(b)). In particular, $\ensuremath{\mathbb{N}}_{0}$ and $\mathbb{N}=\mathbb{N}_{0}\setminus\left\{0\right\}=\mathbb{N}_{0}\setminus1$ are infinite.  

Proof. Since. $n\not\in n$ , we have $n\in A\neq\emptyset$ .Thus, if $A$ were finite, then there were a bijection $f:A\longrightarrow A_{m}:=\{1,\dots,m\}=\{k\in\mathbb{N}:k\leq m\}$ for some $m\in\mathbb{N}$ .However, we will show by induction on $m\in\mathbb{N}$ that there is no injective map $f:A\longrightarrow A_{m}$ . Since $S(n)~\notin~n$ , we have $S(n)\in A$ . Thus, if $f:A\longrightarrow A_{1}=\{1\}$ , then $f(n)=f(S(n))$ showing that. $f$ is not injective and proving the cases $m=1$ . For the induction step, we proceed by contraposition and show that the existence of an injective map $f:A\longrightarrow$ $A_{m+1}$ $m\in\mathbb{N}$ , (cf. Not. A.45) implies the existence of an injective map $g:A\longrightarrow A_{m}$ To this end, let. $m\in\mathbb{N}$ and $f:A\longrightarrow A_{m+1}$ be injective. If. $m+1\not\in f(A)$ , then $f$ itself is an injective map into $A_{m}$ . If $m+1\in f(A)$ , then there is a unique $a\in A$ such that $f(a)=m+1$ . Define  

$$
g:A\longrightarrow A_{m},\quad g(k):=\left\{f(k)\atop f(k+1){\mathrm{for}}a\leq k.\right.
$$  

Then $g$ is well-defined: If $k\in A$ and $a\leq k$ , then $k+1\in A\backslash\{a\}$ , and, since $f$ is injective, $g$ does, indeed, map into $A_{m}$ .We verify $g$ to be injective: If $k,l\in A$ $k<l$ , then also $k<l+1$ and $k+1\neq l+1$ (by Peano axiom $\mathrm{P2}-k+1<l+1$ then also follows, but we do not make use of that here). In each case, $g(k)\neq g(l)$ , proving $g$ to be injective.  

For more basic information regarding ordinals see, e.g., [Kun12, Sec. I.8]  

#### A.3.5 Power Set  

There is one more basic construction principle for sets that is not covered by Axioms 0 $-~6$ , namely the formation of power sets. This needs another axiom:.  

Axiom 7 Power Set:  

$$
{\begin{array}{r l}{\forall}&{{\vec{\mathcal{A}}}{\begin{array}{r l}{Y}&{}\end{array}}\left(Y\subseteq X\Rightarrow Y\in{\mathcal{M}}\right).}\end{array}}\quad
$$  

Thus, the power set axiom states that, for each set $X$ , there exists a set $\mathcal{M}$ that contains all subsets $Y$ Of $X$ as elements.  

Definition A.47. If. $X$ is a set and $\mathcal{M}$ is given by the power set axiom, then we call  

$$
{\mathcal{P}}(X):=\{Y\in{\mathcal{M}}:Y\subseteq X\}
$$  

the power set of $X$ . Another common notation for ${\mathcal{P}}(X)$ is $2^{X}$ (cf. Prop. 2.18).  

#### A.3.6 Foundation  

Foundation is, perhaps, the least important of the axioms in ZF. It basically cleanses the mathematical universe of unnecessary "clutter', i.e. of certain pathological sets that are of no importance to standard mathematics anyway.  

Axiom 8 Foundation:  

$$
{\underset{X}{\forall}}\left({\exists}\left(x\in X\right)\Rightarrow\operatorname{\lrcorner}_{x\in X}\lnot{\exists}\left(z\in x\wedge z\in X\right)\right).
$$  

Thus, the foundation axiom states that every nonempty set $X$ contains an element $x$ that is disjoint to $X$  

Theorem A.48. Due to the foundation axiom, the $\in$ relation can have no cycles, i.e.. there do not exist sets. $x_{1},x_{2},\ldots,x_{n}$ $n\in\mathbb N$ , such that  

$$
x_{1}\in x_{2}\in\cdots\in x_{n}\in x_{1}.
$$  

In particular, sets can not be members of themselves:  

$$
\neg\exists x\in x.
$$  

Proof. If there were sets $x_{1},x_{2},\ldots,x_{n}$ $n\in\mathbb{N}$ , such that (A.16a) were true, then, by using the pairing axiom and the union axiom, we could form the set  

$$
X:=\{x_{1},\ldots,x_{n}\}.
$$  

Then, in contradiction to the foundation axiom, $X\cap x_{i}\neq\emptyset$ , for each $i=1,\dots,n$ Indeed, $x_{n}\in X\cap x_{1}$ , and $x_{i-1}\in X\cap x_{i}$ for each $i=2,\ldots,n$  

For a detailed explanation, why "sets" forbidden by foundation do not occur in standard mathematics, anyway, see, e.g., [Kun12, Sec. I.14].  

### A.4 The Axiom of Choice  

In addition to the axioms of ZF discussed in the previous section, there is one more axiom, namely the axiom of choice (AC) that, together with ZF, makes up ZFC, the axiom system at the basis of current standard mathematics. Even though AC is used and accepted by most mathematicians, it does have the reputation of being somewhat less "natural'. Thus, many mathematicians try to avoid the use of AC, where possible, and it is often pointed out explicitly, if a result depends on the use of AC (but this practice is by no means consistent, neither in the literature nor in this class, and one. might sometimes be surprised, which seemingly harmless result does actually depend on AC in some subtle nonobvious way). We will now state the axiom:.  

Axiom 9 Axiom of Choice $(A C)$  

$$
\begin{array}{r l}{{\underset{{\cal M}}{\forall}}}&{{}\left(\emptyset\not\in{\mathcal{M}}\Rightarrow\underset{f:{\mathcal{M}}\longrightarrow\underset{N\in{\mathcal{M}}}{\bigcup}^{N}}{\underset{{\cal N}\in{\mathcal{M}}}{\exists}}\left(\underset{M\in{\mathcal{M}}}{\forall}f(M)\in M\right)\right).}\end{array}
$$  

Thus, the axiom of choice postulates, for each nonempty set $\mathcal{M}$ , whose elements are all nonempty sets, the existence of a choice function, that means a function that assigns, to each $M\in\mathcal{M}$ , an element $m\in M$  

Example A.49. For example, the axiom of choice postulates, for each nonempty set $A$ , the existence of a choice function on ${\mathcal{P}}(A)\setminus\{\emptyset\}$ that assigns each subset of $A$ one of its elements.  

The axiom of choice is remarkable since, at first glance, it seems so natural that one can hardly believe it is not provable from the axioms in ZF. However, one can actually show that it is neither provable nor disprovable from ZF (see, e.g., [Jec73, Th. 3.5, Th.. 5.16] - such a result is called an independence proof, see [Kun80] for further material). If you want to convince yourself that the existence of choice functions is, indeed, a tricky matter, try to define a choice function on. ${\mathcal{P}}(\mathbb{R})\setminus\{\emptyset\}$ without AC (but do not spend too. much time on it - one can show this is actually impossible to accomplish)..  

Theorem A.52 below provides several important equivalences of AC. Its statement and proof needs some preparation. We start by introducing some more relevant notions from the theory of partial orders:  

Definition A.50. Let $X$ be a set and let $\leq$ be a partial order on $X$ (a) An element $m\in X$ is called maximal (with respect to. $\leq$ ) if, and only if, there exists. no $x\in X$ such that $m\leq x$ (note that a maximal element does not have to be a max and that a maximal element is not necessarily unique).  

(b) A nonempty subset. $C$ of $X$ is called a chain if, and only if,. $C$ is totally ordered by. $\leq$ . Moreover, a chain $C$ is called maximal if, and only if, no strict superset $Y$ of $C$ (i.e. no. $Y\subseteq X$ such that. $C\subsetneq Y$ ) is a chain..  

The following lemma is a bit technical and will be used to prove the implication AC. $\Rightarrow$ (ii) in Th. A.52 (other proofs in the literature often make use of so-called transfinite. recursion, but that would mean further developing the theory of ordinals, and we will not pursue this route in this class)..  

Lemma A.51. Let $X$ be a set and let ${\emptyset\neq\mathcal{M}\subseteq\mathcal{P}(X)}$ be a nonempty set of subsets of $X$ .We let $\mathcal{M}$ be partially ordered by inclusion, i.e. setting $A\leq B:\Leftrightarrow A\subseteq B$ for each $A,B\in{\mathcal{M}}$ . Moreover, define  

$$
\underset{\boldsymbol{S}\subseteq\mathcal{M}}{\forall}~\bigcup\boldsymbol{S}:=\bigcup_{\boldsymbol{S}\in\mathcal{S}}\boldsymbol{S}
$$  

and assume  

$$
\begin{array}{r l}{\underset{\mathcal{C}\subseteq\mathcal{M}}{\forall}}&{{}\Big(\mathcal{C}i s a c h a i n\Rightarrow\bigcup\mathcal{C}\in\mathcal{M}\Big).}\end{array}
$$  

If the function $g:\mathcal{M}\longrightarrow\mathcal{M}$ has the property that  

$$
\begin{array}{r l}{\underset{M\in\mathcal{M}}{\forall}}&{{}\Big(M\subseteq g(M)\wedge\#(g(M)\setminus M)\le1\Big),}\end{array}
$$  

then $g$ has a fixed point, i.e.  

$$
\begin{array}{r}{\underset{M\in\mathcal{M}}{\exists}\quad g(M)=M.}\end{array}
$$  

Proof. Fix some arbitrary $M_{0}\in\mathcal{M}$ .We call $\tau\subseteq{\mathcal{M}}$ an $M_{0}$ -tower if, and only if, $^{7}$ satisfies the following three properties  

(i) $M_{0}\in\mathcal{T}$  

(ii) If $\mathcal{C}\subseteq\mathcal{T}$ is a chain, then $\cup\mathcal{C}\in\mathcal{T}$ (iii) If $M\in{\mathcal{T}}$ , then $g(M)\in\mathcal{T}$  

Let $\mathbb{T}:=\{\mathcal{T}\subseteq\mathcal{M}:\mathcal{T}$ is an $M_{0}$ -tower}. If ${\mathcal{T}}_{1}:=\{M\in{\mathcal{M}}:M_{0}\subseteq M\}$ , then, clearly, $\mathcal{T}_{1}$ is an $M_{0}$ -tower and, in particular, $\mathbb{T}\neq\emptyset$ . Next, we note that the intersection of all $M_{0}$ -towers, i.e. $\textstyle{\mathcal{T}}_{0}:=\bigcap_{\mathcal{T}\in\mathbb{T}}{\mathcal{T}}$ , is also an $M_{0}$ -tower. Clearly, no strict subset of $\mathcal{T}_{0}$ can be an $M_{0}$ -tower and  

$$
M\in{\mathcal{T}}_{0}\Rightarrow M\in{\mathcal{T}}_{1}\Rightarrow M_{0}\subseteq M.
$$  

The main work of the rest of the proof consists of showing that $\mathcal{T}_{0}$ is a chain. To show.   
$\mathcal{T}_{0}$ to be a chain, define.  

$$
\Gamma:=\left\{M\in\mathcal{T}_{0}:\underset{N\in\mathcal{T}_{0}}{\forall}\quad(M\subseteq N\vee N\subseteq M)\right\}.
$$  

We intend to show that. $\Gamma=T_{0}$ by verifying that. $\Gamma$ is an $M_{0}$ -tower. As an intermediate step, we define.  

$$
\begin{array}{r l}{\underset{M\in\Gamma}{\forall}}&{{}\Phi(M):=\{N\in\mathcal{T}_{0}:N\subseteq M\vee g(M)\subseteq N\}}\end{array}
$$  

and also show each $\Phi(M)$ to be an $M_{0}$ tower. Actually, $\Gamma$ and each $\Phi(M)$ satisfy (i) due to (A.21). To verify $\Gamma$ satisfies (ii), let $\mathcal{C}\subseteq\Gamma$ be a chain and $U:=\cup{\mathcal{C}}$ . Then $U\in T_{0}$ , since $\mathcal{T}_{0}$ satisfies (ii). If $N\in\mathcal{T}_{0}$ , and $C\subseteq N$ for each $C\in{\mathcal{C}}$ , then $U\subseteq N$ . If $N\in\mathcal{T}_{0}$ , and there is $C\in{\mathcal{C}}$ such that $C\nsubseteq N$ , then $N\subseteq C$ (since $C\in\Gamma$ ), i.e. $N\subseteq U$ showing $U\in\Gamma$ and $\Gamma$ satisfying (ii). Now, let $M\in\Gamma$ . To verify $\Phi(M)$ satisfies (ii), let ${\mathcal{C}}\subseteq\Phi(M)$ be a chain and $U:=\cup\mathcal{C}$ . Then $U\in T_{0}$ , since $\mathcal{T}_{0}$ satisfies (ii). If $U\subseteq M$ , then $U\in\Phi(M)$ as desired. If $U\not\subseteq M$ , then there is $x\in U$ such that $x\notin M$ . Thus, there is $C\in{\mathcal{C}}$ such that $x\in C$ and $g(M)\subseteq C$ (since $C\in\Phi(M)$ ), i.e. $g(M)\subseteq U$ , showing $U\in\Phi(M)$ also in this case, and $\Phi(M)$ satisfies (ii). We will verify that $\Phi(M)$ satisfies (iii) next. For this purpose, fix $N\in\Phi(M)$ .We need to show $g(N)\in\Phi(M)$ . We already know $g(N)\in\mathcal{T}_{0}$ , as $\mathcal{T}_{0}$ satisfies (iii). As $N\in\Phi(M)$ , we can now distinguish three cases. Case 1: $N\subsetneq M$ . In this case, we cannot have $M\subsetneq g(N)$ (otherwise, $\sharp(g(N)\setminus N)\geq2$ in contradiction to (A.19)). Thus, $g(N)\subseteq M$ (since $M\in\Gamma$ ), showing $g(N)\in\Phi(M)$ Case 2: $N=M$ . Then $g(N)=g(M)\in\Phi(M)$ (since $g(M)\in\mathcal{T}_{0}$ and $g(M)\subseteq g(M))$ Case 3: $g(M)\subseteq N$ . Then $g(M)\subseteq g(N)$ by (A.19), again showing $g(N)\in\Phi(M)$ . Thus, we have verified that $\Phi(M)$ satisfies (iii) and, therefore, is an $M_{0}$ -tower. Then, by the definition of $\mathcal{T}_{0}$ , we have ${\mathcal{T}}_{0}\subseteq\Phi(M)$ . As we also have $\Phi(M)\subseteq{\mathcal{T}}_{0}$ (from the definition of $\Phi(M)$ ), we have shown  

$$
\begin{array}{r}{\forall\qquad\Phi(M)=\mathcal{T}_{0}.}\end{array}
$$  

As a consequence, if. $N\in\mathcal{T}_{0}$ and $M\in\Gamma$ , then $N\in\Phi(M)$ and this means $N\subseteq M\subseteq$ $g(M)$ or $g(M)\subseteq N$ , i.e. each $N\in\mathcal{T}_{0}$ is comparable to $g(M)$ , showing $g(M)\in\Gamma$ and $\Gamma$ satisfying (iii), completing the proof that. $\Gamma$ is an $M_{0}$ -tower. As with the. $\Phi(M)$ above, we conclude $\Gamma=T_{0}$ , as desired. To conclude the proof of the lemma, we note $\Gamma=T_{0}$ implies $\mathcal{T}_{0}$ is a chain. We claim that.  

$$
M:=\bigcup{\mathcal{T}}_{0}
$$  

satisfies (A.20): Indeed, $M\in\mathcal{T}_{0}$ , since $\mathcal{T}_{0}$ satisfies (ii). Then. $g(M)\in\mathcal{T}_{0}$ , since $\mathcal{T}_{0}$ satisfies (iii). We then conclude $g(M)\subseteq M$ from the definition of $M$ .As we always. have $M\subseteq g(M)$ by (A.19), we have established $g(M)=M$ and proved the lemma. $\vert$  

Theorem A.52 (Equivalences to the Axiom of Choice). The following statements (i) -(v) are equivalent to the axiom of choice (as stated as Axiom 9 above).  

(i) Every Cartesian product $\textstyle{\prod_{i\in I}A_{i}}$ of nonempty sets $A_{i}$ , where $I$ is a nonempty index set, is nonempty (cf. Def. 2.15(c)).  

(ii) Hausdorff's Maximality Principle: Every nonempty partially ordered set $X$ contains a maximal chain (i.e. a maximal totally ordered subset).  

(iii) Zorn's Lemma: Let $X$ be a nonempty partially ordered set. If every chain $C\subseteq X$ (i.e. every nonempty totally ordered subset of $X$ ) has an upper bound in $X$ (such chains with upper bounds are sometimes called inductive), then $X$ contains a maximal element (cf. Def. A.50(a)).  

(iv) Zermelo's Well-Ordering Theorem: Every set can be well-ordered (recall the definition of a well-order from Def. A.21(d))..  

(v) Every vector space $V$ over a field $F^{\prime}$ has a basis $B\subseteq V$  

Proof. $\mathrm{^{6}(i)}\Leftrightarrow\mathrm{AC^{3}};$ Assume (i). Given a nonempty set of nonempty sets $\mathcal{M}$ , let $I:={\mathcal{M}}$ and, for each $M\in\mathcal{M}$ , let $A_{M}:=M$ . If $\textstyle f\in\prod_{M\in I}A_{M}$ , then, according to Def. 2.15(c), for each $M\in I=\mathcal{M}$ , one has $f(M)\in A_{M}=M$ , proving AC holds. Conversely, assume. AC. Consider a family $(A_{i})_{i\in I}$ such that $I\neq\emptyset$ and each $A_{i}\neq\emptyset$ . Let $\mathcal{M}:=\{A_{i}:i\in I\}$ Then, by AC, there is a map $g:{\mathcal{M}}\longrightarrow\bigcup_{N\in{\mathcal{M}}}N=\bigcup_{j\in I}A_{j}$ such that $g(M)\in M$ for each $M\in\mathcal{M}$ . Then we can define  

$$
f:I\longrightarrow\bigcup_{j\in I}A_{j},\quad f(i):=g(A_{i})\in A_{i},
$$  

to prove (i).  

Next, we will show. ${\mathrm{AC}}\Rightarrow{\mathrm{(ii)}}\Rightarrow{\mathrm{(iii)}}\Rightarrow{\mathrm{(iv)}}\Rightarrow{\mathrm{AC}}.$  

$\mathrm{^{6}A C}\Rightarrow(\mathrm{ii})^{,}$ :Assume AC and let $X$ be a nonempty partially ordered set. Let $\mathcal{M}$ be the set of all chains in $X$ (i.e. the set of all nonempty totally ordered subsets of $X$ ). Then $\emptyset\notin\mathcal{M}$ and $\mathcal{M}\neq\emptyset$ (since $X\neq\emptyset$ and $\{x\}\in\mathcal{M}$ for each $x\in X$ ). Moreover, $\mathcal{M}$ satisfies the hypothesis of Lem. A.51, since, if $\mathcal{C}\subseteq\mathcal{M}$ is a chain of totally ordered subsets of $X$ then $\cup{\mathcal{C}}$ is a totally ordered subset of $X$ , i.e. in $\mathcal{M}$ (here we have used the notation of (A.17); also note that we are dealing with two different types of chains here, namely those with respect to the order on $X$ and those with respect to the order given by $\subseteq$ on $\mathcal{M}$ ). Let $f:{\mathcal{P}}(X)\setminus\{\emptyset\}\longrightarrow X$ be a choice function given by AC, i.e. such that  

$$
\forall_{Y\in{\mathcal{P}}(X)\backslash\{\emptyset\}}\quad f(Y)\in Y.
$$  

As an auxiliary notation, we set  

$$
\begin{array}{r l}{\underset{M\in\mathcal{M}}{\forall}}&{{}M^{*}:=\big\{x\in X\backslash M:M\cup\{x\}\in\mathcal{M}\big\}.}\end{array}
$$  

With the intention of applying Lem. A.51, we define  

$$
g:\mathcal{M}\longrightarrow\mathcal{M},\quad g(M):=\left\{\begin{array}{l l}{M\cup\{f(M^{*})\}}&{\mathrm{if~}M^{*}\neq\varnothing,}\ {M}&{\mathrm{if~}M^{*}=\varnothing.}\end{array}\right.
$$  

Since $g$ clearly satisfies (A.19), Lem. A.51 applies, providing an $M\in\mathcal{M}$ such that $g(M)=M$ . Thus, $M^{*}=\emptyset$ , i.e. $M$ is a maximal chain, proving (ii).  

${}^{66}(\mathrm{ii})\Rightarrow(\mathrm{iii})^{3}$ : Assume (ii). To prove Zorn's lemma, let $X$ be a nonempty set, partially ordered by $\leq$ , such that every chain $C\subseteq X$ has an upper bound. Due to Hausdorff's maximality principle, we can assume $C\subseteq X$ to be a maximal chain. Let $m\in X$ be an upper bound for the maximal chain $C$ . We claim that $m$ is a maximal element: Indeed, if there were $x\in X$ such that $m<x$ , then $x\notin C$ (since $m$ is upper bound for $C$ ) and $C\cup\{x\}$ would constitute a strict superset of $C$ that is also a chain, contradicting the maximality of $C$  

$\mathrm{^{*}(i i i)\Rightarrow(i v)^{*}}$ : Assume (iii) and let. $X$ be a nonempty set. We need to construct a well-order on $X$ . Let $\mathcal{W}$ be the set of all well-orders on subsets of. $X$ , i.e.  

We define a partial order $\leq$ on $\mathcal{W}$ by setting  

$$
\begin{array}{r l}{\underset{\substack{\langle W\rangle,(Y^{\prime},W^{\prime})\in\mathcal{W}}}{\forall}}&{\Big((Y,W)\leq(Y^{\prime},W^{\prime}):\Longleftrightarrow Y\subseteq Y^{\prime}\wedge W=W^{\prime}[_{Y}}\ &{}&{\wedge(y\in Y,y^{\prime}\in Y^{\prime},y^{\prime}W^{\prime}y\Rightarrow y^{\prime}\in Y)\Big)}\end{array}
$$  

(recall the definition of the restriction of a relation from Def. A.21(e)). To apply Zorn's lemma to $(\mathcal{W},\leq)$ , we need to check that every chain $\mathcal{C}\subseteq\mathcal{W}$ has an upper bound. To this end, if $\mathcal{C}\subseteq\mathcal{W}$ is a chain, let  

$$
U_{{\mathcal{C}}}:=(Y_{\mathcal{C}},W_{{\mathcal{C}}}),\quad\mathrm{where}\quad Y_{{\mathcal{C}}}:=\bigcup_{(Y,W)\in{\mathcal{C}}}Y,\quad W_{{\mathcal{C}}}:=\bigcup_{(Y,W)\in{\mathcal{C}}}W.
$$  

We need to verify $U_{\mathcal{C}}~\in~\mathcal{W}$ : If $a W c^{\phantom{\dagger}}$ , then there is $(Y,C)\in{\mathcal{C}}$ such that $a W b$ .In particular, $(a,b)\in Y\times Y\subseteq Y_{\mathcal{C}}\times Y_{\mathcal{C}}$ , showing $W_{\mathcal{C}}$ to be a relation on $Y_{\mathcal{C}}$ . Clearly, $W_{\mathcal{C}}$ is a total order on $Y_{\mathcal{C}}$ (one just uses that, if $a,b\in Y_{\mathcal{C}}$ , then, as $\mathcal{C}$ is a chain, there is $(Y,W)\in{\mathcal{C}}$ such that $a,b\in Y$ and $W=W c\upharpoonright$ is a total order on $Y$ ). To see that $W_{\mathcal{C}}$ is a well-order on $Y_{\mathcal{C}}$ , let $\varnothing\neq A\subseteq Y_{\mathcal{C}}$ .If $a\in A$ , then there is $(Y,W)\in{\mathcal{C}}$ such that $a\in Y$ . Since $W=W c\upharpoonright$ is a well-order on. $Y$ , we can let $m:=\operatorname*{min}Y\cap A$ . We claim that $m=\operatorname*{min}A$ as well: Let $b\in A$ .Then there is $(B,U)\in{\mathcal{C}}$ such that $b\in B$ .If $B\subseteq Y$ , then $b\in Y\cap A$ and $m W b$ .If $Y\subseteq B$ , then $m,b\in B$ .If $m U b$ , then we are done. If $b U m$ , then $b\in Y$ (since $(Y,W)\leq(B,U))$ , i.e., again, $b\in Y\cap A$ and $m W b$ (actually $m=b$ in this case), proving. $m=\operatorname*{min}A$ . This completes the proof that $W_{\mathcal{C}}$ is a well-order on $Y_{\mathcal{C}}$ and, thus, shows $U_{\mathcal{C}}\in\mathcal{W}$ . Next, we check $U_{\mathcal{C}}$ to be an upper bound. for $\mathcal{C}$ : If $(Y,W)\in{\mathcal{C}}$ , then $Y\subseteq Y_{\mathcal{C}}$ and $W=W c\upharpoonright$ are immediate. If $y\in Y$ $y^{\prime}\in Y_{\mathcal{C}}$ and $y^{\prime}W c y$ , then $y^{\prime}\in Y$ (otherwise, $y^{\prime}\in A$ with $(A,U)\in{\mathcal{C}}$ $(Y,W)\leq(A,U)$ $y^{\prime}U y$ , in contradiction to $y^{\prime}\notin Y$ ). Thus, $(Y,W)\leq U_{\mathcal{C}}$ , showing $U_{\mathcal{C}}$ to be an upper bound for $\mathcal{C}$ By Zorn's lemma, we conclude that $\mathcal{W}$ contains a maximal element $(M,W_{M})$ . But then $M=X$ and $W_{M}$ is the desired well-order on $X$ : Indeed, if there is. $x\in X\backslash M$ , then we can let $Y:=M\cup\{x\}$ and,  

$$
\begin{array}{r l}{\underset{a,b\in Y}{\forall}}&{\Big(a W b:\Leftrightarrow\big(a,b\in M\land a W_{M}b\big)\lor b=x\Big).}\end{array}
$$  

Then $(Y,W)\in\mathcal{W}$ with $(M,W_{M})<(Y,W)$ in contradiction to the maximality of $(M,W_{M})$  

$\mathrm{{}^{4}(i v)\Rightarrow A C^{3}}$ : Assume (iv). Given a nonempty set of nonempty sets $\mathcal{M}$ , let $X:=$ $\cup_{M\in\mathcal{M}}M$ . By (iv), there exists a well-order $R$ on $X$ . Then every nonempty $Y\subseteq X$ has a unique min. As every $M\in\mathcal{M}$ is a nonempty subset of $X$ , we can define a choice function  

$$
f:{\mathcal{M}}\longrightarrow X,\quad f(M):=\operatorname*{min}M\in M,
$$  

proving AC.  

"(v) $\Longleftrightarrow$ AC": That every vector space has a basis is proved in Th. 5.23 by use of Zorn's lemma. That, conversely, (v) implies AC was first shown in [Bla84], but the proof needs more algebraic tools than we have available in this class. There are also some set-theoretic subtleties that distinguish this equivalence from the ones provided in (i) - (iv), cf. Rem. A.53 below. $\vert$  

Remark A.53. What is actually proved in [Bla84] is that Th. A.52(v) implies the axiom of multiple choice (AMC), which states  

$$
\left(\emptyset\not\:{\mathcal{M}}\Rightarrow\exists\right)_{\substack{f:M\longrightarrow\mathcal{P}\left(\bigcup_{N\in{\mathcal{M}}}N\right)}}\left(\underset{M\in{\mathcal{M}}}{\forall}\left(f(M)\subseteq M\wedge0<\#f(M)<\infty)\right)\right)
$$  

i.e., for each nonempty set. $\mathcal{M}$ , whose elements are all nonempty sets, there exists a. function that assigns, to each. $M\in\mathcal{M}$ , a finite subset of $M$ . Neither the proof that (i). - (iv) of Th. A.52 are each equivalent to AC nor the proof in [Bla84] that Th. A.52(v)  

implies AMC makes use of the axiom of foundation (Axiom 8 above). However, the proof that AMC implies AC does require the axiom of foundation (cf., e.g., [Hal17, Ch. 6]).  

### A.5 Cardinality  

The following theorem provides two interesting, and sometimes useful, characterizations of infinite sets:  

Theorem A.54. Let A be a set. Using the axiom of choice (AC) of Sec. A.4, the. following statements (i) - (ii) are equivalent. More precisely, (ii) and (ii) are equivalent. even without AC (a set A is sometimes called Dedekind-infinite if, and only if, it satisfies (ii), (iii) implies (i) without AC, but. $A C$ is needed to show (i) implies (ii), (iii)..  

(i) A is infinite.  

(ii) There exists $M\subseteq A$ and a bijective map $f:M\longrightarrow\mathbb{N}$ (iii) There exists a strict subset $B\subsetneq A$ and a bijective map $g:A\longrightarrow B$  

One sometimes expresses the equivalence between (i) and (ii) by saying that a set is infinite if, and only if, it contains a copy of the natural numbers. The property stated in (ii) might seem strange at first, but infinite sets are, indeed, precisely those identical in size to some of their strict subsets (as an example think of the natural bijection $n\mapsto2n$ between all natural numbers and the even numbers).  

Proof. We first prove, without AC, the equivalence between (ii) and (iii)  

${}^{\mathrm{*}}(\mathrm{ii})\Rightarrow~(\mathrm{iii})^{\mathrm{*}}$ : Let $E$ denote the even numbers.Then $E\subsetneq\mathbb{N}$ and $h:\mathbb{N}\longrightarrow E$ $h(n):=2n$ , is a bijection, showing that (iii) holds for the natural numbers. According to (ii), there exists $M\subseteq A$ and a bijective map $f:M\longrightarrow\mathbb{N}$ . Define $B:=(A\backslash M)\cup f^{-1}(E)$ and  

$$
h:A\longrightarrow B,\quad h(x):=\left\{{x\atop f^{-1}\circ h\circ f(x)}\quad{\mathrm{for~}}x\in M.\right.
$$  

Then $B\subsetneq A$ since $B$ does not contain the elements of $M$ that are mapped to odd numbers under $f$ . Still, $h$ is bijective, since $h\lceil_{A\setminus M}=\operatorname{Id}_{A\setminus M}$ and $h\upharpoonright_{M}=f^{-1}\circ h\circ f$ is the composition of the bijective maps. $f$ $h$ , and $f^{-1}{\upharpoonright_{E}}$ .. $E\longrightarrow f^{-1}(E)$  

${}^{64}(\mathrm{iii})\Rightarrow(\mathrm{ii})^{3}$ : As (iii) is assumed, there exist $B\subseteq A$ $a\in A\setminus B$ , and a bijective map $g:A\longrightarrow B$ . Set  

$$
M:=\{a_{n}:=g^{n}(a):n\in\mathbb{N}\}.
$$  

We show that. $a_{n}\neq a_{m}$ for each $m,n\in\mathbb{N}$ with $m\neq n$ : Indeed, suppose $m,n\in\mathbb{N}$ with $n>m$ and $u_{n}=u_{m}$ . Then, since. $g$ is bijective, we can apply $g^{-1}$ $m$ times to $u_{n}=u_{m}$ to obtain  

$$
a=(g^{-1})^{m}(a_{m})=(g^{-1})^{m}(a_{n})=g^{n-m}(a).
$$  

Since $l:=n-m\geq1$ , we have $a=g(g^{l-1}(a))$ , in contradiction to $a\in A\setminus B$ . Thus, all the $a_{n}\in M$ are distinct and we can define $f:M\longrightarrow\mathbb{N}$ $f(a_{n}):=n$ , which is clearly bijective, proving (ii).  

${}^{6}(\mathrm{iii})\Rightarrow(\mathrm{i})^{,}\rangle.$ The proof is conducted by contraposition, i.e. we assume $A$ to be finite and proof that (iii) does not hold. If $A=\emptyset$ , then there is nothing to prove. If $\varnothing\neq A$ is finite, then, by Def. 3.10(b), there exists $n\in\mathbb{N}$ and a bijective map $f:A\longrightarrow\{1,\dots,n\}$ . If $B\subsetneq A$ , then, according to Th. 3.19(a), there exists $m\in\ensuremath{\mathbb{N}}_{0}$ $m<n$ , and a bijective map $h:B\longrightarrow\{1,\dots,m\}$ . If there were a bijective map. $g:A\longrightarrow B$ , then $h\circ g\circ f^{-1}$ were a bijective map from. $\{1,\ldots,n\}$ onto $\{1,\ldots,m\}$ with $m<n$ in contradiction to Th. 3.17.  

$\mathrm{^{4}(i)\Rightarrow(i i)^{3}!}$ Inductively, we construct a strictly increasing sequence $M_{1}\subseteq M_{2}\subseteq\dots$ of subsets $M_{n}$ of $A$ $n\in\mathbb N$ , and a sequence of functions $f_{n}:M_{n}\longrightarrow\{1,\dots,n\}$ , satisfying  

$$
\begin{array}{r c l}{{\forall}}&{{f_{n}\mathrm{isbijective,}}}&{{}}\ {{n\in\mathbb{N}}}&{{}}&{{}}\ {{\underset{m,n\in\mathbb{N}}{\forall}}}&{{\left(m\leq n\quad\Rightarrow\quad f_{n}\vert_{M_{m}}=f_{m}\right):}}\end{array}
$$  

Since $A\neq\emptyset$ , there exists $m_{1}\in A$ . Set $M_{1}:=\{m_{1}\}$ and $f_{1}:M_{1}\longrightarrow\{1\}$ $f_{1}(m_{1}):=1$ Then $M_{1}\subseteq A$ and $f_{1}$ bijective are trivially clear. Now let $n\in\mathbb N$ and suppose $M_{1},\ldots,M_{n}$ and $f_{1},\ldots,f_{n}$ satisfying (A.24) have already been constructed. Since $A$ is infinite, there must be $m_{n+1}\in A\backslash M_{n}$ (otherwise $M_{n}=A$ and the bijectivity of $f_{n}:M_{n}\longrightarrow\{1,\dots,n\}$ shows $A$ is finite with $\#A=n$ ; AC is used to select the $m_{n+1}\in A\setminus M_{n})$ . Set $M_{n+1}:=$ $M_{n}\cup\{m_{n+1}\}$ and  

$$
f_{n+1}:M_{n+1}\longrightarrow\{1,\dots,n+1\},\quad f_{n+1}(x):=\left\{{f_{n}(x)\atop n+1}\quad{\mathrm{for~}}x\in M_{n},\atop{\mathrm{for~}}x=m_{n+1}.\right.
$$  

Then the bijectivity of $f_{n}$ implies the bijectivity of $f_{n+1}$ , and, since. $f_{n+1}{\upharpoonright_{M_{n}}}=f_{n}$ holds by definition of. $f_{n+1}$ , the implication  

$$
m\leq n+1\quad\Rightarrow\quad f_{n+1}\vdash m=f_{m}
$$  

holds true as well. An induction also shows $M_{n}=\{m_{1},...,m_{n}\}$ and $f_{n}(m_{n})=n$ for each $n\in\mathbb N$ . We now define.  

$$
M:=\bigcup_{n\in\mathbb{N}}M_{n}=\{m_{n}:n\in\mathbb{N}\},\quad f:M\longrightarrow\mathbb{N},\quad f(m_{n}):=f_{n}(m_{n})=n.
$$  

Clearly, $M\subseteq A$ , and $f$ is bijective with $f^{-1}:\mathbb{N}\longrightarrow M$ $f^{-1}(n)=m_{n}$  

We now proceed to prove some rules regarding cardinality:  

Theorem A.55. Let $A,B$ be sets. Then  

$$
\#A\leq\#B\quad\vee\quad\#B\leq\#A,
$$  

i.e. there exists a bijective map $\phi_{A}:A\longrightarrow N$ with $N\subseteq B$ or a bijective map $\phi_{B}:$ $M\longrightarrow B$ $M\subseteq A$ (this result makes use of. $A C$  

Proof. To apply Zorn's lemma of Th. A.52(ii), we define a partial order on the set  

$$
{\mathcal{M}}:=\left\{(M,N,f):M\subseteq A,N\subseteq B,f:M\longrightarrow N{\mathrm{~is~bijective}}\right\}
$$  

by letting  

$$
(M,N,f)\leq(U,V,g)\quad:\Leftrightarrow\quad M\subseteq U,\quad g\uparrow_{M}=f.
$$  

Then $\mathcal{M}$ contains the empty map, $(\emptyset,\emptyset,\emptyset)\in{\mathcal{M}}$ , i.e. $\mathcal{M}\neq\emptyset$ . Every chain. $\mathcal{C}\subseteq\mathcal{M}$ has an upper bound, namely $(M_{C},f_{C})$ with $M_{\mathcal{C}}:=\bigcup_{(M,N,f)\in\mathcal{C}}M$ and $f_{\mathcal{C}}(x):=f(x)$ where $(M,N,f)\in\mathcal{C}$ is chosen such that $x\in M$ (since $\mathit{c}$ 'is a chain, the value of $f_{\boldsymbol{{c}}}(\boldsymbol{{x}})$ does not actually depend on the choice of $(M,N,f)\in{\mathcal{C}}$ and is, thus, well-defined). Clearly, $M\mathcal{C}\subseteq A$ and $\begin{array}{r}{N_{\mathscr{C}}:=\bigcup_{(M,N,f)\in\mathscr{C}}N\subseteq B}\end{array}$ .We need to verify.. $f_{\mathcal{C}}:M_{\mathcal{C}}\longrightarrow N_{\mathcal{C}}$ to be bijective. If $x,y\in M_{\mathcal{C}}$ , then, since. $\mathcal{C}$ is a chain, there exists $(M,N,f)\in\mathcal{C}$ with $x,y\in M$ . As $f$ is injective, we have, for $x\neq y$ , that $f_{\mathcal{C}}(x)=f(x)\neq f(y)=f_{\mathcal{C}}(y)$ showing $f_{\mathcal{C}}$ to be injective as well. If $z\in N_{\mathcal{C}}$ , then $z\in N$ for some $(f,M,N)\in\mathcal{C}$ . Since $f:M\longrightarrow N$ is surjective, there exists $x\in M\subseteq M_{\mathcal{C}}$ with $f_{\mathcal{C}}(x)=f(x)=z$ , showing $f_{\mathcal{C}}$ to be surjective as well, proving $(M_{\mathscr{C}},N_{\mathscr{C}},f_{\mathscr{C}})\in\mathscr{M}$ . To see $(M_{\cal{C}},N_{\cal{C}},f_{\cal{C}})$ to be an upper. bound for $\mathit{c}$ , note that the definition of $(M_{\mathcal{C}},N_{\mathcal{C}},f_{\mathcal{C}})$ immediately implies $M\subseteq M_{\mathcal{C}}$ for each $(M,N,f)\in\mathcal{C}$ and $f_{\boldsymbol{\mathscr{C}}}\left[\boldsymbol{\mathscr{M}}=\boldsymbol{f}\right.$ for each $(M,N,f)\in\mathcal{C}$ . Thus, Zorn's lemma applies, yielding a maximal element $(M_{\operatorname*{max}},N_{\operatorname*{max}},f_{\operatorname*{max}})\in\mathcal{M}$ . If $a\in A\setminus M_{\operatorname*{max}}$ and $b\in B\backslash N_{\operatorname*{max}}$ then  

$$
f:\{a\}\dot{\cup}M_{\mathrm{max}}\longrightarrow\{b\}\dot{\cup}N_{\mathrm{max}},\quad f(x):=\left\{\begin{array}{l l}{b}&{\mathrm{for~}x=a,}\ {f_{\mathrm{max}}(x)}&{\mathrm{for~}x\in M_{\mathrm{max}}}\end{array}\right.
$$  

is a bijective extension of $f_{\mathrm{max}}$ .Thus, the maximality of $\left(M_{\operatorname*{max}},N_{\operatorname*{max}},f_{\operatorname*{max}}\right)$ implies $M_{\operatorname*{max}}=A$ or $N_{\mathrm{max}}=B$ , completing the proof. $\vert$  

Theorem A.56. Let. $A,B$ be sets, let $A$ be infinite and assume there exists an injective map $\phi_{B}:B\longrightarrow A$ .Then  

$$
\#(A\cup B)=\#A,
$$  

i.e. there exists a bijective map, mapping $A$ onto $A\cup B$ (this result makes use of $A C$  

Proof. Since the map $a\mapsto a$ always maps $A$ injectively into $A\cup B$ , it remains to show the existence of an injective map $\phi:A\cup B\longrightarrow A$ (then (A.30) holds due to the Schroder-Bernstein Th. 3.12). Possibly replacing $B$ with $B\backslash A$ , we may also assume $A$ and $B$ to be disjoint, without loss of generality. Thus, let $M:=A\dot{\cup}B$ . We apply Zorn's lemma of Th. A.52(iii) to  

$$
\mathcal{A}:=\left\{\mathcal{A}\subseteq\mathcal{P}(A):\left(\underset{X\in A}{\forall}\#X=\#\mathbb{N}\right)\wedge\left(\underset{X,Y\in A}{\forall}X\neq Y\Rightarrow X\cap Y=\emptyset\right)\right\},
$$  

partially ordered by set inclusion. $\subseteq$ (each element of $\mathcal{M}$ constitutes a partition of some.   
subset of. $A$ into infinite, countable subsets). Then $\mathcal{M}\neq\emptyset$ by Th. A.54(ii). In the.   
usual way, if $\mathcal{C}\subseteq\mathcal{M}$ is a chain, then the union of all elements of $\mathit{c}$ is an element of. $\mathcal{M}$   
that constitutes an upper bound for. $\mathit{c}$ . Thus, Zorn's lemma applies, yielding a maximal element $\mathcal{A}_{\mathrm{max}}\in\mathcal{M}$ . The maximality of $\mathcal{A}_{\mathrm{max}}$ then implies.  

$$
F:=A\backslash\bigcup_{C\in A_{\operatorname*{max}}}C
$$  

to be finite. Replacing some fixed $C\in\mathcal{A}_{\operatorname*{max}}$ with $C\cup F$ , we may assume. $\mathcal{A}_{\mathrm{max}}$ to be a partition of $A$ . For each $X\in{\mathcal{A}}_{\operatorname*{max}}$ , we have $X\subseteq A$ and a bijective map. $\phi_{X}:\mathbb{N}\longrightarrow X$ Thus, the map.  

$$
\phi_{0}:\mathbb{N}\times{\mathcal{A}}_{\operatorname*{max}}\longrightarrow A,\quad\phi_{0}(n,X):=\phi_{X}(n),
$$  

is bijective as well. Letting $N_{0}:=\{n\in\mathbb{N}:n{\mathrm{~even}}\}$ and $N_{1}:=\{n\in\mathbb{N}:n{\mathrm{~odd}}\}$ , we obtain  

$$
\mathbb{N}\times\mathcal{A}_{\operatorname*{max}}=(N_{0}\times\mathcal{A}_{\operatorname*{max}})\dot{\cup}(N_{1}\times\mathcal{A}_{\operatorname*{max}}).
$$  

Moreover, there exist bijective maps $\psi_{0}:{\mathbb N}\times\mathcal{A}_{\operatorname*{max}}\longrightarrow N_{0}\times\mathcal{A}_{\operatorname*{max}}$ and $\psi_{1}:\mathbb{N}\times\mathcal{A}_{\operatorname*{max}}\longrightarrow$ $N_{1}\times\mathcal{A}_{\operatorname*{max}}$ . Thus, we can define  

$$
\phi:M:=A\dot{\cup}B\longrightarrow A,\quad\phi(x):=\left\{{(\phi_{0}\circ\psi_{0}\circ\phi_{0}^{-1})(x)}\qquad\mathrm{for}x\in A,\right.
$$  

which is, clearly, injective.  

Theorem A.57. Let $A,B$ be nonempty sets, let $A$ be infinite and assume there exists an injective map $\phi_{B}:B\longrightarrow A$ . Then  

$$
\#(A\times B)=\#A,
$$  

i.e. there exists a bijective map, mapping $A$ onto $A\times B$ (this result makes use of. $A C$  

Proof. Since the map $(a,b)\mapsto(a,\phi_{B}(b))$ is injective from $A\times B$ into $A\times A$ , and, for fixed $b_{0}\in B$ , the map $a\mapsto(a,b_{0})$ is injective from $A$ into $A\times B$ , it suffices to show the existence of an injective map from $A\times A$ into $A$ (then (A.30) holds due to the Schroder-Bernstein Th. 3.12). However, we will actually directly prove the existence of a bijective map from $A$ onto $A\times A$ : To apply Zorn's lemma of Th. A.52(iii), we define a partial order on the set  

$$
{\mathcal{M}}:=\Big\{(D,f):D\subseteq A,f:D\longrightarrow D\times D\mathrm{~is~bijective}\Big\}
$$  

by letting  

$$
(D,f)\leq(E,g)\quad:\Leftrightarrow\quad D\subseteq E,\quad g\upharpoonright_{D}=f.
$$  

Then $\mathcal{M}\neq\emptyset$ , since there exists a bijective map. $f:\mathbb{N}\longrightarrow\mathbb{N}\times\mathbb{N}$ by Th. 3.28 and a bijective map between some $D\subseteq A$ and $\mathbb{N}$ by Th. A.54(ii). Every chain. $\mathcal{C}\subseteq\mathcal{M}$ has an upper bound, namely $(D_{\mathcal{C}},f_{\mathcal{C}})$ with $\begin{array}{r}{D_{\mathcal{C}}:=\bigcup_{(D,f)\in\mathcal{C}}D}\end{array}$ and $f_{\mathcal{C}}(x):=f(x)$ , where $(D,f)\in{\mathcal{C}}$ is chosen such that $x\in D$ (since $\mathcal{C}$ is a chain, the value of $f_{\boldsymbol{{C}}}(\boldsymbol{{x}})$ does not actually depend on the choice of. $(D,f)\in{\mathcal{C}}$ and is, thus, well-defined). Clearly, $D c\subseteq A$ and we merely need to verify. $f_{\mathcal{C}}:D_{\mathcal{C}}\longrightarrow D_{\mathcal{C}}\times D_{\mathcal{C}}$ to be bijective. If $x,y\in D_{\mathcal{C}}$ , then, since $\mathcal{C}$ is a chain, there exists $(D,f)\in{\mathcal{C}}$ with $x,y\in D$ .As $f$ is injective, we have $f_{\mathcal{C}}(x)=f(x)\neq f(y)=f_{\mathcal{C}}(y)$ , showing $f_{\mathcal{C}}$ to be injective as well. If $(x,y)\in D_{\mathcal{C}}\times D_{\mathcal{C}}$ and $(D,f)\in{\mathcal{C}}$ with $x,y\in D$ as before, then the surjectivity of. $f:D\longrightarrow D\times D$ yields $z\in D\subseteq D_{\mathcal{C}}$ with $f_{\mathcal{C}}(z)=f(z)=(x,y)$ , showing $f_{\mathcal{C}}$ to be surjective as well, proving $(D_{\mathcal{C}},f_{\mathcal{C}})\in\mathcal{M}$ .To see $(D_{\mathcal{C}},f_{\mathcal{C}})$ to be an upper bound for $\mathit{c}$ , note that the definition of $(D_{\mathcal{C}},f_{\mathcal{C}})$ immediately implies $D\subseteq D_{\mathcal{C}}$ for each $(D,f)\in{\mathcal{C}}$ and $f_{\mathcal{C}}\mathrm{~\tiny~\left[~}D=\mathcal{f\right.}$ for each $(D,f)\in{\mathcal{C}}$ . Thus, Zorn's lemma applies, yielding a maximal element. $(D_{\operatorname*{max}},f_{\operatorname*{max}})\in\mathcal{M}$ We would like to prove $D_{\operatorname*{max}}=A$ . However, in general, this can not be expected to. hold (for example, if $A=\mathbb{N}$ , and $\mathbb{N}\setminus D$ is finite, then $(D,f)\in{\mathcal{M}}$ is always maximal - since $(E\times E)\setminus(D\times D)$ is infinite for each $D\subsetneq E\subseteq A$ $f$ does not have a bijective extension $g:E\longrightarrow E\times E)$ . What we can prove, though, is the existence of a bijective map $\phi:{\cal D}_{\operatorname*{max}}\longrightarrow A$ , which suffices, since the map  

$$
\tilde{\phi}:A\longrightarrow A\times A,\quad\tilde{\phi}:=(\phi,\phi)\circ f_{\operatorname*{max}}\circ\phi^{-1},
$$  

is then also bijective. It remains to establish the existence of the bijective map $\phi:$ $D_{\operatorname*{max}}\longrightarrow A$ ..Arguing via contraposition, we assume the nonexistence of a bijective $\phi$ and show $(D_{\mathrm{max}},f_{\mathrm{max}})$ is not maximal: Let. $E:=A\setminus D_{\operatorname*{max}}$ . Then $A=D_{\mathrm{max}}{\dot{\cup}}E$ According to Th. A.56, there does not exist an injective map from $E$ into $D_{\mathrm{max}}$ . Then, according to Th. A.55, there exists a bijective map. $\phi_{D}:D_{\mathrm{max}}\longrightarrow N$ $N\subseteq E$ . Define  

$$
P:=(N\times N)\dot{\cup}(N\times D_{\mathrm{max}})\dot{\cup}(D_{\mathrm{max}}\times N).
$$  

Since $\phi_{D}:D_{\mathrm{max}}\longrightarrow N$ is bijective and $f_{\mathrm{max}}:D_{\mathrm{max}}\longrightarrow D_{\mathrm{max}}\times D_{\mathrm{max}}$ is bijective, we conclude  

$$
\#(N\times N)=\#(N\times D_{\operatorname*{max}})=\#(D_{\operatorname*{max}}\times N)=\#D_{\operatorname*{max}}=\#N.
$$  

Thus, $\#P=\#D_{\operatorname*{max}}=\#N$ by Th. A.56 and, in particular, there exists a bijection $f_{N}:$ $N\longrightarrow P$ . In consequence, we can combine the bijections $f_{\operatorname*{max}}:D_{\operatorname*{max}}\longrightarrow D_{\operatorname*{max}}\times D_{\operatorname*{max}}$ and $f_{N}:N\longrightarrow P$ to obtain a bijection.  

$$
\begin{array}{r}{f:N\dot{\cup}D_{\mathrm{max}}\longrightarrow P\dot{\cup}(D_{\mathrm{max}}\times D_{\mathrm{max}})=(D_{\mathrm{max}}\dot{\cup}N)\times(D_{\mathrm{max}}\dot{\cup}N),}\end{array}
$$  

which is a bijective extension of $f_{\mathrm{max}}$ , i.e. $(N\cup D_{\operatorname*{max}},f)\in\mathcal{M}$ and $(D_{\mathrm{max}},f_{\mathrm{max}})$ is not maximal. Thus, the maximality of $(D_{\mathrm{max}},f_{\mathrm{max}})$ implies the existence of a bijective $\phi:{\cal D}_{\operatorname*{max}}\longrightarrow A$ as desired.  

Corollary A.58. Let $n\in\mathbb N$ and let $A$ be an infinite set. Then  

$$
\#A^{n}=\#A,
$$  

i.e. there exists a bijective map, mapping $A$ onto $A^{n}$ (this result makes use of. $A C$  

Proof. The claimed rule (A.35) follows via a simple induction from Th. A.57, since, for each $n\in\mathbb N$ with $n\geq2$ , the map  

$$
\phi:A^{n}\longrightarrow A^{n-1}\times A,\quad\phi(a_{1},\ldots,a_{n}):=\big((a_{1},\ldots,a_{n-1}),a_{n}\big),
$$  

is, clearly, bijective.  

Theorem A.59. Let A be a set and let ${\mathcal{P}}_{\mathrm{fin}}(A)$ denote the set of finite subsets of. $A$  

(a) One has  

$$
\#{\mathcal{P}}_{\mathrm{fin}}(A)=\#2_{\mathrm{fin}}^{A},
$$  

where $2_{\mathrm{fin}}^{A}:=\{0,1\}_{\mathrm{fin}}^{A}$ is defined as in Ex. 5.16(c) and a bijection between ${\mathcal{P}}_{\mathrm{fin}}(A)$ and $\{0,1\}_{\mathrm{fin}}^{A}$ is given by restricting the map  

$$
\chi:\mathcal{P}(A)\longrightarrow\{0,1\}^{A},\quad\chi(B):=\chi_{B},
$$  

of Prop. 2.18 to ${\mathcal{P}}_{\mathrm{fin}}(A)$  

(b) If $A$ is infinite, then  

$$
\begin{array}{r l}{\forall}&{{}\#\mathcal{P}_{n}(A)=\#\mathcal{P}_{\mathrm{fn}}(A)=\#A,}\end{array}
$$  

i.e. there exists a bijective map, mapping. $A$ onto ${\mathcal{P}}_{\mathrm{fin}}(A)$ as well as a bijective map,. mapping $A$ onto $\mathcal{P}_{n}(A)$ , where $\mathcal{P}_{n}(A)$ denotes the set of subsets of. $A$ with precisely n elements (both results of (b) make use of $A C$  

Proof. (a): $\chi\lceil\mathcal{P}_{\mathrm{fin}}(A)$ is injective, since $\chi$ is injective. If $f\in\{0,1\}_{\mathrm{fin}}^{A}$ , then  

$$
B_{f}:=\{a\in A:f(a)\neq0\}\in{\mathcal{P}}_{\mathrm{fin}}(A)
$$  

with $f=\chi_{B_{f}}$ , showing $\chi\lceil{\mathcal{P}}_{\mathrm{fin}}(A)$ to be surjective onto $\{0,1\}_{\mathrm{fin}}^{A}$  

(b): Let $n\in\mathbb N$ and let $a_{1},\dotsc,a_{n+1}\in A$ be $n+1$ distinct elements of $A$ . Define  

$$
\iota_{n}:A\longrightarrow\mathcal{P}_{n}(A),\quad\iota_{n}(a):=\left\{\begin{array}{l l}{a\cup\{a_{1},\ldots,a_{n-1}\}}&{\mathrm{for~}a\notin\{a_{1},\ldots,a_{n-1}\},}\ {\{a_{1},\ldots,a_{n+1}\}\setminus\{a\}}&{\mathrm{for~}a\in\{a_{1},\ldots,a_{n-1}\}.}\end{array}\right.
$$  

Then, clearly, each. $\iota_{n}$ is injective as a map into. $\mathcal{P}_{n}(A)$ and, due to ${\mathcal{P}}_{n}(A)\subseteq{\mathcal{P}}_{\mathrm{fin}}(A)$ also as a map into. ${\mathcal{P}}_{\mathrm{fin}}(A)$ . Thus, it remains to show the existence of injective maps $\phi_{n}:\mathcal{P}_{n}(A)\longrightarrow A$ and $\phi:\mathcal{P}_{\mathrm{fin}}(A)\longrightarrow A$ (then (A.37) holds due to the SchroderBernstein Th. 3.12). Fix. $n\in\mathbb N$ . Due to Cor. A.58, it suffices to define an injective map $\tilde{\phi}_{n}:\mathcal{P}_{n}(A)\longrightarrow A^{n}$ . For each $B\in\mathcal{P}_{n}(A)$ , let $\phi_{B}:\{1,\dots,n\}\longrightarrow B$ be bijective and define  

$$
\tilde{\phi}_{n}:\mathcal{P}_{n}(A)\longrightarrow A^{n},\quad\tilde{\phi}_{n}(B):=\phi_{B}.
$$  

If $B,C\in\mathcal{P}_{n}(A)$ with $x\in B\setminus C$ , then $x\in\phi_{B}(\{1,\ldots,n\})$ , but $x\notin\phi_{C}(\{1,\ldots,n\})$ showing $\phi_{B}\neq\phi_{C}$ , i.e. $\tilde{\phi}_{n}$ is injective. To obtain $\phi$ , it suffices to define an injective map $\phi:{\mathcal{P}}_{\mathrm{fin}}(A)\longrightarrow A\times\mathbb{N}$ , as there exists a bijective map from $A\times\mathbb{N}$ onto $A$ by Th. A.57. Since  

$$
{\mathcal{P}}_{\mathrm{fin}}(A)=\bigcup_{n\in\mathbb{N}}{\mathcal{P}}_{n}(A),
$$  

we may define  

$$
{\tilde{\phi}}:{\mathcal{P}}_{\mathrm{fin}}(A)\longrightarrow A\times\mathbb{N},\quad{\tilde{\phi}}(B):=\big(\phi_{n}(B),n\big)\quad\mathrm{for}\quad B\in{\mathcal{P}}_{n}(A),
$$  

which is, clearly, injective, due to (A.38) and the injectivity of $\phi_{n}$  

Theorem A.60. Let $A,B$ be sets. If. $2\le\#A$ (i.e. there exists an injective map $\iota_{2}:$ $\{0,1\}\longrightarrow A_{,}$ ), $\#A\leq\#B$ (i.e. there exists an injective map $\iota_{A}:A\longrightarrow B_{,}$ , and. $B$ is infinite, then.  

$$
\begin{array}{r}{\#A^{B}=\#2^{B}=\#\mathcal{P}(B),~}\ {\#A_{\mathrm{fn}}^{B}=\#2_{\mathrm{fn}}^{B}=\#\mathcal{P}_{\mathrm{fn}}(B)\stackrel{(\mathrm{A.37})}{=}\#B,}\end{array}
$$  

i.e. there exist bijective maps $\phi_{1}:A^{B}\longrightarrow\{0,1\}^{B}$ and $\phi_{2}:\{0,1\}^{B}\longrightarrow{\mathcal{P}}(B)$ , as well as bijective maps $\phi_{1,\mathrm{f}}:A_{\mathrm{fin}}^{B}\longrightarrow\{0,1\}_{\mathrm{fin}}^{B}$ and $\phi_{2,\mathrm{f}}:\{0,1\}_{\mathrm{fin}}^{B}\longrightarrow\mathcal{P}_{\mathrm{fin}}(B)$ (this result makes use of $A C_{\prime}$ . For the purposes of (A.39b), we introduce the notation $0:=\iota_{2}(0)\in A$ , 8o that both $A_{\mathrm{fin}}^{B}$ and $2_{\mathrm{fin}}^{B}$ make sense according to the definition in Ex. 5.16(c).  

Proof. The existence of $\phi_{2}$ was already established in Prop. 2.18, the existence of $\phi_{\mathrm{2,f}}$ in Th. A.59(a). Thus, according to the Schroder-Bernstein Th. 3.12, for the existence of $\phi_{1}$ it suffices to show the existence of injective maps $f_{1}:\{0,1\}^{B}\longrightarrow A^{B}$ $f_{2}:A^{B}\longrightarrow B^{B}$ $f_{3}:B^{B}\longrightarrow{\mathcal{P}}(B\times B)$ , as well as a bijective map $g:\mathcal{P}(B\times B)\longrightarrow\mathcal{P}(B)$ , which can be stated concisely as  

$$
\#2^{B}\leq\#A^{B}\leq\#B^{B}\leq\#\mathcal{P}(B\times B)=\#\mathcal{P}(B).
$$  

Analogously, for the existence of. $\phi_{\mathrm{1,f}}$ , it suffices to show the existence of injective maps $f_{1,\mathrm{f}}:\{0,1\}_{\mathrm{fin}}^{B}\longrightarrow A_{\mathrm{fin}}^{B}$ $f_{\mathrm{2,f}}:A_{\mathrm{fn}}^{B}\longrightarrow B_{\mathrm{fn}}^{B}$ $f_{3,\mathrm{f}}:B_{\mathrm{fin}}^{B}\longrightarrow\mathcal{P}_{\mathrm{fin}}(B\times B)$ as well as a bijective map $g_{\mathrm{f}}:\mathcal{P}_{\mathrm{fin}}(B\times B)\longrightarrow\mathcal{P}_{\mathrm{fin}}(B)$ , which can be stated concisely as  

$$
\#2_{\mathrm{fin}}^{B}\leq\#A_{\mathrm{fin}}^{B}\leq\#B_{\mathrm{fin}}^{B}\leq\#\mathcal{P}_{\mathrm{fin}}(B\times B)=\#\mathcal{P}_{\mathrm{fin}}(B)
$$  

(for $B_{\mathrm{fin}}^{B}$ to make sense according to the definition in Ex. 5.16(c), we now also introduce the notation $0:=\iota_{A}(\iota_{2}(0))\in B\rangle$ . Clearly, the maps  

$$
\begin{array}{r l r l}&{f_{1}:\{0,1\}^{B}\longrightarrow A^{B},}&&{f_{1}(\alpha)(b):=\iota_{2}(\alpha(b)),}\ &{f_{2}:A^{B}\longrightarrow B^{B},}&&{f_{2}(\alpha)(b):=\iota_{A}(\alpha(b)),}\ &{f_{3}:B^{B}\longrightarrow\mathscr{P}(B\times B),}&&{f_{3}(\alpha):=\{(x,y)\in B\times B:y=\alpha(x)\},}\end{array}
$$  

are, indeed, injective. Then the restrictions  

$$
\begin{array}{r}{\mathrm{\boldmath~\lambda~}_{1,\mathrm{f}}^{*}:\mathrm{\boldmath~\left\{0,1\right\}}_{\mathrm{fin}}^{B}\longrightarrow A_{\mathrm{fin}}^{B},\quad f_{1,\mathrm{f}}:=f_{1}\mathrm{\boldmath~\left\{0,1\right\}}_{\mathrm{fin}}^{B},\quad f_{2,\mathrm{f}}:A_{\mathrm{fin}}^{B}\longrightarrow B_{\mathrm{fin}}^{B},\quad f_{2,\mathrm{f}}:=f_{2}\mathrm{\boldmath~\left\{~A_\mathrm{fin}^{B}~,~\right\}~}}\end{array}
$$  

are well-defined and injective as well. While the restriction of $f_{3}$ does not work, as it. does not map into. ${\mathcal{P}}_{\mathrm{fin}}(B\times B)$ , we can use the injective map  

$$
f_{3,\mathrm{f}}:B_{\mathrm{fin}}^{B}\longrightarrow\mathcal{P}_{\mathrm{fin}}(B\times B),\quad f_{3,\mathrm{f}}(\alpha):=\{(x,y)\in B\times B:y=\alpha(x)\neq0\}.
$$  

From Th. A.57, we know the existence of a bijective map $\psi:B\times B\longrightarrow B$ , implying  

$$
g:{\mathcal{P}}(B\times B)\longrightarrow{\mathcal{P}}(B),\quad g({\mathcal{C}}):=\psi({\mathcal{C}})=\{\psi(x,y):(x,y)\in{\mathcal{C}}\},
$$  

to be bijective as well, thereby proving (A.40a) and (A.39a). Then the restriction  

$$
g_{\mathrm{f}}:\mathcal{P}_{\mathrm{fin}}(B\times B)\longrightarrow\mathcal{P}_{\mathrm{fin}}(B),\quad g_{\mathrm{f}}:=g\upharpoonright_{\mathrm{fin}}(B\times B),
$$  

is well-defined and also bijective, proving (A.40b) and (A.39b).  

## B General Forms of the Laws of Associativity and Commutativity  

### B.1 Associativity  

In the literature, the general law of associativity is often stated in the form that $a_{1}a_{2}\cdots a_{n}$ gives the same result "for every admissible way of inserting parentheses into $a_{1}a_{2}\cdots a_{n}^{\quad}$ , but a completely precise formulation of what that actually means seems to be rare. As a warm-up, we first prove a special case of the general law:  

Proposition B.1. Let $(A,\cdot)$ be a semigroup (i.e. . : $A\times A\longrightarrow A$ is an associative composition on $A$ ). Then  

$$
\prod_{n\in\mathbb{N},\quad a_{1},\ldots,a_{n}\in A}\quad\forall_{\textstyle k\in\{2,\ldots,n\}}\quad\left(\prod_{i=k}^{n}a_{i}\right)\left(\prod_{i=1}^{k-1}a_{i}\right)=\prod_{i=1}^{n}a_{i},
$$  

where the product symbol is defined according to (3.16a).  

Proof. The assumed associativity means the validity of  

$$
\begin{array}{r}{\forall\qquad(a b)c=a(b c).}\ {a,b,c\in A}\end{array}
$$  

If $k=n$ , then (B.1) is immediate from (3.16a). For $2\leq k<n$ , we prove (B.1) by induction on $n$ : For the base case, $n=2$ , there is nothing to prove. For. $n>2$ , one computes  

$$
\begin{array}{r l}{\displaystyle\left(\prod_{i=k}^{n}a_{i}\right)\left(\prod_{i=1}^{k-1}a_{i}\right)}&{\ensuremath{\stackrel{\mathrm{(3.16a)}}{=}}\quad\left(a_{n}\cdot\prod_{i=k}^{n-1}a_{i}\right)\left(\prod_{i=1}^{k-1}a_{i}\right)\ensuremath{\stackrel{\mathrm{(B.2)}}{=}}a_{n}\cdot\left(\left(\prod_{i=k}^{n-1}a_{i}\right)\left(\prod_{i=1}^{k-1}a_{i}\right)\right.}\ {\displaystyle\qquad\left.\mathrm{ind}\underline{{\mathrm{,}\mathrm{hyp.}}}\quad a_{n}\cdot\prod_{i=1}^{n-1}a_{i}\ensuremath{\stackrel{\mathrm{(3.16a)}}{=}}\prod_{i=1}^{n}a_{i},}\end{array}
$$  

completing the induction and the proof of the proposition.  

The difficulty in stating the general form of the law of associativity lies in giving a precise definition of what one means by "an admissible way of inserting parentheses into $a_{1}a_{2}\cdots a_{n}^{\quad}$ . So how does one actually proceed to calculate the value of $a_{1}a_{2}\cdots a_{n}$ , given that parentheses have been inserted in an admissible way? The answer is that one does it in $n-1$ steps, where, in each step, one combines two juxtaposed elements, consistent with the inserted parentheses. There can still be some ambiguity: For example, for. $(a_{1}a_{2})(a_{3}(a_{4}a_{5}))$ , one has the freedom of first combining. $a_{1},a_{2}$ , or of first combining. $a_{4},a_{5}$ . In consequence, our general law of associativity will show that, for each admissible sequence of $n-1$ directives for combining two juxtaposed elements, the final result is the same (under the hypothesis that (B.2) holds). This still needs some preparatory. work.  

In the following, one might see it as a slight notational inconvenience that we have defined $\textstyle\prod_{i=1}^{n}a_{i}$ $u_{n}\cdots u_{1}$ rather than $a_{1}\cdots a_{n}$ . For this reason, we will enumerate the elements to be combined by composition from right to left rather then from left to right.  

Definition and Remark B.2. Let $A$ be a nonempty set with a composition $\cdot:A\times$ $A\longrightarrow A$ , let $n\in\mathbb{N}$ $n\geq2$ , and let $I$ be a totally ordered index set, $\#I=n$ $I={}$ $\{i_{1},\ldots,i_{n}\}$ with $i_{1}<\cdots<i_{n}$ .Moreover, let $F:=(a_{i_{n}},\ldots,a_{i_{1}})$ be a family of $n$ elements of $A$  

(a) An admissible composition directive (for combining two juxtaposed elements of the family) is an index $i_{k}\in I$ with $1\leq k\leq n-1$ . It transforms the family $F^{\prime}$ into the family. $G:=(a_{i_{n}},\ldots,a_{i_{k+1}}a_{i_{k}},\ldots,a_{i_{1}})$ . In other words, $G=(b_{j})_{j\in J}$ . where $J:=I\setminus\{i_{k+1}\}$ $b_{j}=a_{j}$ for each $j\in J\backslash\{i_{k}\}$ , and $b_{i_{k}}=a_{i_{k+1}}a_{i_{k}}$ . We can write this transformation as two maps  

$$
\begin{array}{r l}&{F\mapsto\delta_{i_{k}}^{(1)}(F):=G=(a_{i_{n}},\ldots,a_{i_{k+1}}a_{i_{k}},\ldots,a_{i_{1}})=(b_{j})_{j\in J},}\ &{I\mapsto\delta_{i_{k}}^{(2)}(I):=J=I\setminus\{i_{k+1}\}.}\end{array}
$$  

Thus, an application of an admissible composition directive reduces the length of the family and the number of indices by one..  

(b) Recursively, we define (finite) sequences of families, index sets, and indices as follows:  

$$
F_{n}:=F,\quad I_{n}:=I,
$$  

$$
\underset{\alpha\in\{2,\ldots,n\}}{\forall}F_{\alpha-1}:=\delta_{j_{\alpha}}^{(1)}(F_{\alpha}),\quad I_{\alpha-1}:=\delta_{j_{\alpha}}^{(2)}(I_{\alpha}),\quad\mathrm{where~}j_{\alpha}\in I_{\alpha}\setminus\{\operatorname*{max}I_{\alpha}\}.
$$  

The corresponding sequence of indices $\mathcal{D}:=(j_{n},\ldots,j_{2})$ in $I$ is called an admissible evaluation directive. Clearly,.  

$$
\begin{array}{r l}{\forall}&{\#I_{\alpha}=\alpha,\quad\mathrm{i.e.}F_{\alpha}\mathrm{has~length}\alpha.}\end{array}
$$  

In particular, $I_{1}=\{j_{2}\}=\{i_{1}\}$ (where the second equality follows from (B.4b)), $F_{1}=(a)$ , and we call  

$$
{\mathcal{D}}(F):=a
$$  

the result of the admissible evaluation directive $\textit{D}$ applied to $F^{\prime}$  

Theorem B.3 (General Law of Associativity). Let $(A,\cdot)$ be a semigroup $(i.e.\cdot:A\times$ $A\longrightarrow A$ is an associative composition on $A$ ).Let $n\in\mathbb{N}$ $n\geq2$ , and let $I$ be a totally ordered index set, $\#I=n$ $I=\{i_{1},\ldots,i_{n}\}$ with $i_{1}<\cdots<i_{n}$ .Moreover, let $F:=(a_{i_{n}},\ldots,a_{i_{1}})$ be a family of n elements of $A$ . Then, for each admissible evaluation directive as defined in Def. and Rem. B.2(b), the result is the same, namely  

$$
{\mathcal{D}}(F)=\prod_{k=1}^{n}a_{i_{k}}.
$$  

Proof. We conduct the proof via induction on $n$ . For $n=3$ , there are only two possible directives and (B.2) guarantees that they yield the same result. For the induction step, let $n>3$ .As in Def. and Rem. B.2(b), we write $\mathcal{D}=(j_{n},\dots,j_{2})$ and obtain some $I_{2}=\{i_{1},i_{m}\}$ $1<m\le n$ , as the corresponding penultimate index set. Depending on $i_{m}$ , we partition $\left(j_{n},\ldots,j_{3}\right)$ as follows: Set  

$$
\begin{array}{r}{J_{1}:=\big\{k\in\{3,\ldots,n\}:j_{k}<i_{m}\big\},\quad J_{2}:=\big\{k\in\{3,\ldots,n\}:j_{k}\geq i_{m}\big\}.}\end{array}
$$  

Then, for $k\in J_{1}$ $j_{k}$ is a composition directive to combine two elements to the right of $a_{i_{m}}$ and, for $k\in J_{2}$ $j_{k}$ is a composition directive to combine two elements to the left of $a_{i_{m}}$ . Moreover, $J_{1}$ and $J_{2}$ might or might not be the empty set: If $J_{1}=\emptyset$ , then $j_{k}\neq i_{1}$ for each $k\in\{3,\ldots,n\}$ , implying $i_{m}=i_{2}$ ; if $J_{2}=\emptyset$ , then, in each of the $n-2$ steps to obtain $I_{2}$ , an $i_{k}$ with $k<m$ was removed from $I$ , implying $i_{m}=i_{n}$ (in particular, as $n\neq2$ $J_{1}$ and $J_{2}$ cannot both be empty). If $J_{1}\neq\emptyset$ , then $\mathcal{D}_{1}:=(j_{k})_{k\in J_{1}}$ is an admissible evaluation directive for $(a_{i_{m-1}},\ldots,a_{i_{1}})$ - this follows from  

$$
j_{k}\in K\subseteq\{i_{1},\ldots,i_{m-1}\}\Rightarrow\delta_{j_{k}}^{(2)}(K)\subseteq K\subseteq\{i_{1},\ldots,i_{m-1}\}.
$$  

Since $m-1<n$ , the induction hypothesis applies and yields  

$$
\mathcal{D}_{1}(a_{i_{m-1}},\ldots,a_{i_{1}})=\prod_{k=1}^{m-1}a_{i_{k}}.
$$  

Analogously, if $J_{2}\neq\emptyset$ , then $\mathcal{D}_{2}:=(j_{k})_{k\in J_{2}}$ is an admissible evaluation directive for $(a_{i_{n}},\ldots,a_{i_{m}})$ this follows from  

$$
j_{k}\in K\subseteq\{i_{m},\ldots,i_{n}\}\Rightarrow\delta_{j_{k}}^{(2)}(K)\subseteq K\subseteq\{i_{m},\ldots,i_{n}\}.
$$  

Since $m>1$ , the induction hypothesis applies and yields  

$$
{\cal D}_{2}(a_{i_{n}},\dots,a_{i_{m}})=\prod_{k=m}^{n}a_{i_{k}}.
$$  

Thus, if $J_{1}\neq\emptyset$ and $J_{2}\neq\emptyset$ , then we obtain  

$$
\gamma(F)\stackrel{j_{2}=i_{1}}{=}\mathcal{D}_{2}(a_{i_{n}},\ldots,a_{i_{m}})\cdot\mathcal{D}_{1}(a_{i_{m-1}},\ldots,a_{i_{1}})=\left(\prod_{k=m}^{n}a_{i_{k}}\right)\left(\prod_{k=1}^{m-1}a_{i_{k}}\right)\stackrel{\mathrm{Prop.}\mathrm{B.}1}{=}\prod_{k=m}^{n}a_{i_{k}}
$$  

as desired. If $J_{1}=\emptyset$ , then, as explained above, $i_{m}=i_{2}$ . Thus, in this case,  

$$
{\mathcal{D}}(F){\overset{j_{2}=i_{1}}{=}}{\mathcal{D}}_{2}(a_{i_{n}},\ldots,a_{i_{2}})\cdot a_{i_{1}}=\left(\prod_{k=2}^{n}a_{i_{k}}\right)\cdot a_{i_{1}}{\overset{\mathrm{Prop.}\mathrm{B.}1}{=}}\prod_{k=1}^{n}a_{i_{k}}
$$  

as needed. Finally, if. $J_{2}=\emptyset$ , then, as explained above, $i_{m}=i_{n}$ . Thus, in this case,.  

$$
\mathcal{D}(F)\overset{j_{2}=i_{1}}{=}a_{i_{n}}\cdot\mathcal{D}_{1}\big(a_{i_{n-1}},\ldots,a_{i_{1}}\big)=\prod_{k=1}^{n}a_{i_{k}},
$$  

again, as desired, and completing the induction.  

### B.2 Commutativity  

In the present section, we will generalize the law of commutativity $a b=b a$ to a finite number of factors, provided the composition is also associative.  

Theorem B.4 (General Law of Commutativity). Let $(A,\cdot)$ be a semigroup (i.e. : : $A\times A\longrightarrow A$ is an associative composition on $A$ ). If the composition is commutative, i. e. if  

$$
\forall_{a,b\in A}a b=b a,
$$  

then  

$$
\bigforall_{n\in\mathbb{N}}\quad\forall_{\pi\in S_{n}}\quad\underset{a_{1},\ldots,a_{n}\in A}{\forall}\quad\prod_{i=1}^{n}a_{i}=\prod_{i=1}^{n}a_{\pi(i)},
$$  

where $S_{n}$ is the set of bijective maps on $\{1,\ldots,n\}$ (cf. Ex. 4.9(b)).  

Proof. We conduct the proof via induction on $n$ : For $n=1$ , there is nothing to prove and, for $n=2$ , (B.18) is the same as (B.17). So let $n>2$ . As $\pi$ is bijective, we may define $k:=\pi^{-1}(n)$ . Then  

$$
\begin{array}{r l r}{\displaystyle\prod_{i=1}^{n}a_{\pi(i)}}&{\mathrm{Th}_{\underline{{\operatorname{\Pi}}}\underline{{\operatorname{B}}}\underline{{\operatorname{B}}}3}}&{\left(\displaystyle\prod_{i=k+1}^{n}a_{\pi(i)}\right)\cdot a_{\pi(k)}\cdot\left(\displaystyle\prod_{i=1}^{k-1}a_{\pi(i)}\right)}\ &{\displaystyle\overset{(\mathtt{B}.17)}{=}}&{a_{\pi(k)}\cdot\left(\displaystyle\prod_{i=k+1}^{n}a_{\pi(i)}\right)\cdot\left(\displaystyle\prod_{i=1}^{k-1}a_{\pi(i)}\right).}\end{array}
$$  

Define the bijective map  

$$
\begin{array}{r}{\mathrm{:}\quad\{1,\dots,n-1\}\longrightarrow\{1,\dots,n-1\},\quad\varphi(j):=\left\{\pi(j)\qquad\mathrm{for}1\leq j\leq k-1,\atop\pi(j+1)\quad\mathrm{for}k\leq j\leq n-1\}\right.}\end{array}
$$  

(where the bijectivity of $\pi$ implies the bijectivity of $\varphi$ ). Then  

$$
\begin{array}{c c l}{{\displaystyle\prod_{i=1}^{n}a_{\pi(i)}}}&{{\stackrel{\mathrm{(B.19)}}{=}}}&{{a_{n}\cdot\left(\displaystyle\prod_{i=k}^{n-1}a_{\varphi(i)}\right)\cdot\left(\displaystyle\prod_{i=1}^{k-1}a_{\varphi(i)}\right)^{\mathrm{\tiny~{Th}.\underline{{{B}}}.3}}a_{n}\cdot\displaystyle\prod_{i=1}^{n-1}a_{\varphi(i)}}}\ {{}}&{{\stackrel{\mathrm{ind.hyp.}}{=}}}&{{a_{n}\cdot\displaystyle\prod_{i=1}^{n-1}a_{i}=\displaystyle\prod_{i=1}^{n}a_{i},}}\end{array}
$$  

completing the induction proof.  

The following example shows that, if the composition is not associative, then, in general, (B.17) does not imply (B.18):  

Example B.5. Let $A:=\{a,b,c\}$ with $\#A=3$ (i.e. the elements $a,b,c$ are all distinct). Let the composition : on. $A$ be defined according to the composition table  

$$
\begin{array}{c}{{\cdot\left|\begin{array}{c c c}{{a}}&{{b}}&{{c}}\ {{a}}&{{b}}&{{b}}\end{array}\right|}}\ {{b}}\ {{c}}\end{array}
$$  

Then, clearly, - is commutative. However, - is not associative, since, e.g.,  

$$
(c b)a=a a=b\neq a=c b=c(b a),
$$  

and (B.18) does not hold, since, e.g.,  

$$
a(b c)=a a=b\neq a=c b=c(b a).
$$  

## C Groups  

In Ex. 4.9(b), we defined the symmetric group $S_{M}$ of bijective maps from $M$ into $M$ (i.e. of so-called permutations). It is a remarkable result that every group $G$ is isomorphic to a subgroup of the permutation group $S_{G}$ and the proof is surprisingly simple (cf. Th. C.2 below). On the other hand, this result seems to have surprisingly few useful applications, partly due to the fact that $S_{G}$ is usually much bigger (and, thus, usually more difficult to study) than $G$ (cf. Prop. C.4 below).  

We start with a preparatory lemma:  

Lemma C.1. Let $M,N$ be sets and let $\psi:\mathrm{~}M\longrightarrow N$ be bijective. Then the symmetric groups $S_{M}$ and $S_{N}$ are isomorphic.  

Proof. Exercise.  

Theorem C.2 (Cayley). Let $(G,\cdot)$ be a group. Then $G$ is isomorphic to a subgroup of the symmetric group $(S_{G},\circ)$ of permutations on $G$ . In particular, every finite group is isomorphic to a subgroup of $S_{n}$  

Proof. Exercise. Hint: Show that  

$$
\phi:G\longrightarrow S_{G},\quad a\mapsto f_{a},\quad f_{a}(x):=a x,
$$  

defines a monomorphism and use Lem. C.1.  

Notation C.3. Let $M,N$ be sets. Define.  

$$
S(M,N):=\{(f:M\longrightarrow N):f\mathrm{~bijective}\}.
$$  

Proposition C.4. Let $M,N$ be sets with $\#M=\#N=n\in\mathbb{N}_{0}$ ${\cal S}:={\cal S}(M,N)$ (cf. Not. C.3). Then - $\#S=n!$ ; in particular $\#S_{M}=n!$  

Proof. We conduct the proof via induction: If $n=0$ , then $S$ contains precisely the empty map (i.e. the empty set) and $\#S=1=0!$ is true. If. $n=1$ and $M=\left\{a\right\}$ $N=\{b\}$ , then $S$ contains precisely the map $f:M\longrightarrow N$ $f(a)=b$ , and $\#S=1=1!$ is true. For the induction step, fix $n\in\mathbb N$ and assume $\#M=\#N=n+1$ . Let $a\in M$ and  

$$
\mathcal{A}:=\bigcup_{b\in N}S\Big(M\backslash\{a\},N\backslash\{b\}\Big).
$$  

Since the union in (C.2) is finite and disjoint, one has  

$$
\#A=\sum_{b\in N}\#S{\Big(}M\setminus\{a\},N\setminus\{b\}{\Big)}{\overset{\mathrm{ind.hyp.}}{=}}\sum_{b\in N}(n!)=(n+1)\cdot n!=(n+1)!.
$$  

Thus, it suffices to show  

$$
\phi:S\longrightarrow A,\quad\phi(f):M\setminus\{a\}\longrightarrow N\setminus\{f(a)\},\quad\phi(f):=f\uparrow_{M\setminus\{a\}},
$$  

is well-defined and bijective. If. $f:M\longrightarrow N$ is bijective, then $f\mid_{M\backslash\{a\}}$ .. $M\setminus\{a\}\longrightarrow$ $N\setminus\{f(a)\}$ is bijective as well, i.e. $\phi$ is well-defined. Suppose $f,g\in S$ with $f\neq g$ . If $f(a)\neq g(a)$ , then $\phi(f)\neq\phi(g)$ , as they have different codomains. If $f(a)=g(a)$ , then there exists $x\in M\setminus\{a\}$ with $f(x)\neq g(x)$ , implying $\phi(f)(x)=f(x)\neq g(x)=\phi(g)(x)$  

i.e., once again, $\phi(f)\neq\phi(g)$ . Thus, $\phi$ is injective. Now let $h\in S(M\backslash\{a\},N\backslash\{b\})$ for some $b\in N$ . Letting  

$$
f:M\longrightarrow N,\quad f(x):={\left\{\begin{array}{l l}{b}&{{\mathrm{for~}}x=a,}\ {h(x)}&{{\mathrm{for~}}x\neq a,}\end{array}\right.}
$$  

we have $\phi(f)=h$ , showing $\phi$ to be surjective as well.  

## D Number Theory  

The algebraic discipline called number theory, studies properties of the ring of integers (and similar algebraic structures).  

Theorem D.1 (Remainder Theorem). For each pair of numbers $(a,b)\in\mathbb{N}^{2}$ , there exists a unique pair of numbers $(q,r)\in\mathbb{N}_{0}^{2}$ satisfying the two conditions $a=q b+r$ and $0\leq r<b$  

Proof. Existence: Define  

$$
\begin{array}{r l}&{q:=\operatorname*{max}\{n\in\mathbb{N}_{0}:n b\leq a\},}\ &{r:=a-q b.}\end{array}
$$  

Then $q\in\ensuremath{\mathbb{N}}_{0}$ by definition and (D.1b) immediately yields $a=q b+r$ as well as $r\in\mathbb{Z}$ Moreover, from (D.1a), $q b\leq a=q b+r$ , i.e. $0\leq r$ , in particular,. $r\in\ensuremath{\mathbb{N}}_{0}$ . Since (D.1a) also implies $(q+1)b>a=q b+r$ , we also have. $b>r$ as required.  

Uniqueness: Suppose $(q_{1},r_{1})\in\mathbb{N}_{0}$ , satisfying the two conditions $a=q_{1}b+r_{1}$ and $0\leq r_{1}<b$ .Then $q_{1}b=a-r_{1}\leq a$ and $(q_{1}+1)b=a-r_{1}+b>a$ , showing $q_{1}=\operatorname*{max}\{n\in\mathbb{N}_{0}:n b\leq a\}=q$ . This, in turn, implies $r_{1}=a-q_{1}b=a-q b=r$ thereby establishing the case.  

Definition D.2. (a) Let $a,k\in\mathbb{Z}$ . We define $a$ to be a divisor of $k$ (and also say that a divides $k$ , denoted $a|k$ ) if, and only if, there exists $b\in\mathbb Z$ such that $k=a b$ . If $a$ is no divisor of $k$ , then we write $a~\nearrow k$  

(b) A number $p\in\mathbb N$ $p\geq2$ , is called prime if, and only if, $^{1}$ and $p$ are its only divisors.  

(c) Let $M$ be a nonempty set of integers. If $M\ne\{0\}$ , then the number.  

$$
\operatorname*{gcd}(M):=\operatorname*{max}\left\{n\in\mathbb{N}:\operatorname*{\lrcorner}_{k\in M}n|k\right\}
$$  

is called the greatest common divisor of the numbers in $M$ . If $M=\{a,b\}$ , then one also writes $\operatorname*{gcd}(a,b):=\operatorname*{gcd}(M)$ . The numbers in. $M$ are called relatively prime or mutually prime if, and only if. $\operatorname*{gcd}(M)=1$ . If $M$ is finite and $0\not\in M$ , then the number  

$$
\operatorname{lcm}(M):=\operatorname*{min}\left\{n\in\mathbb{N}:\operatorname{\_{k\inM}}k\right|n\right\}
$$  

is called the least common multiple of the numbers in $M$ .If $M=\{a,b\}$ , then one also writes $\operatorname{lcm}(a,b):=\operatorname{lcm}(M)$  

Remark D.3. Let $M$ be a nonempty set of integers. If $M\ne\{0\}$ , then $\operatorname{gcd}(M)$ is well-defined, since, for each $k\in\mathbb{Z},1|k$ , and, if. $0\not=k\in M$ , then $\operatorname*{gcd}(M)\leq k$ . If $M$ is finite and. $0\not\in M$ , then $\mathrm{lcm}(M)$ is well-defined, since 1. $\operatorname{nax}\{|k|:k\in M\}\leq\operatorname{lcm}(M)\leq$ $\textstyle\prod_{k\in M}|k|$ . Some examples are.  

$$
\begin{array}{r l}{\operatorname*{gcd}(\mathbb{Z})=1,}&{\operatorname*{gcd}(3\mathbb{Z})=3,\quad\operatorname*{gcd}\{8,12,20\}=4,}\ {\operatorname{lcm}(2,3\}=6,}&{\operatorname{lcm}(4,8)=8,\quad\operatorname{lcm}\{8,12,20\}=120.}\end{array}
$$  

Theorem D.4 (Bezout's Lemma). If $a,b\in\mathbb{Z}$ with $\{a,b\}\neq\{0\}$ and $d:=g c d(a,b)$ then  

$$
\{x a+y b:x,y\in\mathbb{Z}\}=d\mathbb{Z}.
$$  

In particular,  

$$
\underset{x,y\in\mathbb{Z}}{\exists}\quad x a+y b=d,
$$  

which is known as Bezout's identity. An important special case is  

$$
\operatorname*{gcd}(a,b)=1\quad\Rightarrow\quad\underset{x,y\in\mathbb{Z}}{\exists}\quad x a+y b=1.
$$  

Proof. Clearly, it suffices to prove (D.4). To prove (D.4), we show  

$$
S:=\{x a+y b:x,y\in\mathbb{Z}\}\cap\mathbb{N}=d\mathbb{N}.
$$  

By setting $y:=0$ and $x:=\pm1$ , we see that $S$ contains $a$ or $-a$ , i.e. $S\neq\emptyset$ . Let $d:=\operatorname*{min}S$ Then there exist $s,t\in\ensuremath{\mathbb{Z}}$ with $s a+t b=d$ . It remains to show $d:=\operatorname*{gcd}(a,b)$ . We apply Th. D.1, to obtain $(q,r)\in\mathbb{N}_{0}^{2}$ with  

$$
|a|=q d+r\quad\wedge\quad0\leq r<d.
$$  

Then, letting $\tilde{s}:=s$ for $a=|a|$ and $\tilde{s}:=-s$ for $a=-|a|$ , we have  

$$
r=|a|-q d=|a|-q(|a|\tilde{s}+b t)=|a|(1-q\tilde{s})-b q t\in S\cup\{0\}.
$$  

Since $d=\operatorname*{min}S$ and $r<d$ , this yields $r=0$ and $d\mid a$ . Using $b$ instead of $a$ in the above reasoning, yields $d\mid b$ as well, showing $d$ to be a common divisor of $a$ and $b$ .Now let $c\in\mathbb N$ be an arbitrary common divisor of $a$ and $b$ . Then there exist $u,v\in\mathbb{Z}$ such that $a=c u$ and $b=c v$ , implying  

$$
d=a s+b t=c u s+c v t=c(u s+v t).
$$  

In consequence $c|d$ , implying $c\leq d$ , showing $d:=\operatorname*{gcd}(a,b)$ , as desired.  

Theorem D.5 (Euclid's Lemma). Let $a,b\in\mathbb{Z}$ and $n\in\mathbb N$  

(a) If $n$ and a are relatively prime (i.e. gc $\mathrm{d}(n,a)=1$ ), then  

$$
\begin{array}{r l r}{n|a b}&{{}\Rightarrow}&{n|b.}\end{array}
$$  

(b) If $n$ is prime, then  

$$
n|a b\quad\Rightarrow\quad\left(n|a\vee n|b\right).
$$  

Proof. (a): As. $\operatorname*{gcd}(n,a)=1$ , from (D.6), we obtain $x,y\in\mathbb{Z}$ such that. $x n+y a=1$ Multiplying this equation by $b$ yields  

$$
x n b+y a b=b.
$$  

Moreover, by hypothesis, there exists $c\in\mathbb{Z}$ with $a b=n c$ , implying $\textstyle n(x b+y c)=b$ , i.e.   
$n|b$ as claimed.  

(b): Suppose $n$ is prime,. $n|a b$ , and $\textit{n}/a$ .As $n$ is prime, the only divisors of $n$ are 1 and $n$ . As $\textit{n}\nearrow a$ , we know $\operatorname*{gcd}(n,a)=1$ , implying $n|b$ by (a).  

Theorem D.6 (Fundamental Theorem of Arithmetic). Every $n\in\mathbb{N}$ $n\geq2$ , has a unique factorization into prime numbers (unique, except for the order of the primes). More precisely, given n as above, there exists a unique function $k_{n}:{P}_{n}\longrightarrow\mathbb{N}$ such that $P_{n}\subseteq\{p\in\mathbb{N}:p$ prime} and  

$$
n=\prod_{p\in P_{n}}p^{k_{n}(p)}
$$  

(then, clearly, $P_{n}$ is necessarily finite)  

Proof. Existence: This is a simple induction proof: The base case is $n=2$ .As 2 is clearly prime, we can let $P_{2}:=\{2\}$ and $k_{2}(2):=1$ . For the induction step, let $n>2$ . If $n$ is prime, then, as in the base case, let $P_{n}:=\{n\}$ and $k_{n}(n):=1$ . If $n$ is not prime,  

then there exist. $a,b\in\mathbb{N}$ with $1<a\le b<n$ and $n=a b$ . By induction hypothesis, there exist functions $k_{a}:{\cal P}_{a}\longrightarrow\mathbb{N}$ $k_{b}:~P_{b}\longrightarrow\mathbb{N}$ , such that $P_{a},P_{b}\subseteq\{p\in\mathbb{N}:p{\mathrm{~prime}}\}$ and  

Letting $P_{n}:=P_{a}\cup P_{b}$ and  

$$
a=\prod_{p\in P_{a}}p^{k_{a}(p)},\quad b=\prod_{p\in P_{b}}p^{k_{b}(p)}.
$$  

$$
k_{n}:P_{n}\longrightarrow\mathbb{N},\quad k_{n}(p):={\left\{\begin{array}{l l}{k_{a}(p)}&{{\mathrm{for~}}p\in P_{a}\setminus P_{b},}\ {k_{b}(p)}&{{\mathrm{for~}}p\in P_{b}\setminus P_{a},}\ {k_{a}(p)+k_{b}(p)}&{{\mathrm{for~}}p\in P_{a}\cap P_{b},}\end{array}\right.}
$$  

we obtain  

$$
\lambda b=\prod_{p\in P_{a}}p^{k_{a}(p)}\prod_{p\in P_{b}}p^{k_{b}(p)}=\prod_{p\in P_{a}\backslash P_{b}}p^{k_{a}(p)}\prod_{p\in P_{b}\backslash P_{a}}p^{k_{b}(p)}\prod_{p\in P_{a}\cap P_{b}}p^{k_{a}(p)+k_{b}(p)}=\prod_{p\in P_{n}}p^{k_{n}}
$$  

thereby completing the induction proof.  

Uniqueness: Here we will make use of Th. D.5(b). As existence, the proof is via induction on $n$ . Since $n=2$ has precisely the divisors 1 and 2, uniqueness for the base case is clear. In the same way, uniqueness is clear for every prime $n>2$ . Thus, for the induction step, it only remains to consider the case, where $n>2$ is not prime. Suppose, we have $P,Q\subseteq\{p\in\mathbb{N}:p{\mathrm{~prime}}\}$ and $k:P\longrightarrow\mathbb{N}$ $l:Q\longrightarrow\mathbb{N}$ , such that.  

$$
n=\prod_{p\in P}p^{k(p)}=\prod_{q\in Q}q^{l(q)}.
$$  

Let $p_{0}\in P$ . Since $p_{0}$ is prime and $\begin{array}{r}{p_{0}|n=\prod_{q\in Q}q^{l(q)}}\end{array}$ , Th. D.5(b) implies $p_{0}|q_{0}$ for some $q_{0}\in Q$ . As $p_{0}$ and $q_{0}$ are both prime, this implies $p_{0}=q_{0}$ and  

$$
m:=n/p_{0}=p_{0}^{k(p_{0})-1}\prod_{p\in P\setminus\{p_{0}\}}p^{k(p)}=p_{0}^{l(p_{0})-1}\prod_{q\in Q\setminus\{p_{0}\}}q^{l(q)}.
$$  

Since $n$ is not prime, we know. $m\geq2$ .As we know. $m<n$ , we may use the induction hypothesis to conclude $P=Q$ $k(p)=l(p)$ for each $p\in P\backslash\{p_{0}\}$ , and $k(p_{0})-1=l(p_{0})-1$ i.e. $k=l$ as desired.  

Theorem D.7 (Euclid's Theorem). The set of prime numbers is infinite.  

Proof. We show that no finite set of primes contains every prime: Let $\emptyset\neq P$ be a finite set of prime numbers. Define $p:=\prod_{q\in P}q$ $\tilde{p}:=p+1$ . Then $\tilde{p}\notin P$ , since $\tilde{p}>q$ for each $q\in P$ . Thus, if $\tilde{p}$ is prime, we are already done. If. $\tilde{p}$ is not prime, then there exists a. prime $n$ such that $n|\tilde{p}$ (this is immediate from Th. D.6, but also follows easily without Th. D.6, since. $\tilde{p}$ can only have finitely many factors. $a$ with $1<a<\tilde{p}$ ). If $n\in P$ , then there is $a\in\mathbb N$ such that $n a=p$ .As there is also $b\in\mathbb N$ such that $n b=\tilde{p}$ , we have $1={\tilde{p}}-p=n b-n a=n(b-a)$ , implying $n=b-a=1$ , in contradiction to $1\not\in{\cal P}$ Thus, $n\not\in{\cal P}$ , completing the proof.  

## E Vector Spaces  

### E.1 Cardinality and Dimension  

Theorem E.1. Let $V$ be a vector space over the field $F$ and let $B$ be a basis of $V$  

(a) $\#V=\#F_{\mathrm{fin}}^{B}$ , i.e. there exists a bijective map $\phi:\:V\longrightarrow F_{\mathrm{fin}}^{B}$ , where $F_{\mathrm{fin}}^{B}$ is defined as in Ex. 5.16(c).  

(b) If $B$ is infinite and $\#F\leq\#B$ (i.e. there exists an injective map $\phi_{F}:F\longrightarrow B_{,}$ then  

$$
\#V=\#F_{\mathrm{fn}}^{B}=\#2_{\mathrm{fn}}^{B}=\#\mathcal{P}_{\mathrm{fn}}(B)=\#B,
$$  

i.e. there exist bijective functions  

$$
\begin{array}{r l}&{\phi_{1}:V\longrightarrow F_{\mathrm{fin}}^{B},\qquad\phi_{2}:F_{\mathrm{fin}}^{B}\longrightarrow\{0,1\}_{\mathrm{fin}}^{B},}\ &{\phi_{3}:\{0,1\}_{\mathrm{fin}}^{B}\longrightarrow\mathcal{P}_{\mathrm{fin}}(B),\qquad\phi_{4}:\mathcal{P}_{\mathrm{fin}}(B)\longrightarrow B.}\end{array}
$$  

Proof. (a): Given. $v\in V$ and $b\in B$ , let $c_{v}(b)$ denote the coordinate of. $\upsilon$ with respect to. $b$ according to Th. 5.19. Then  

$$
\phi:V\longrightarrow{\cal F}_{\mathrm{fn}}^{B},\quad\phi(v)(b):=c_{v}(b),
$$  

is well-defined and bijective by Th. 5.19.  

(b): The map. $\phi_{1}$ exists according to (a), whereas $\phi_{2}$ $\phi_{3}$ $\phi_{3}$ exist according to Th..   
A.60.  

Corollary E.2. Let $F^{\prime}$ be a field and let $M$ be an infinite set. If $\#F\leq\#M$ (i.e. there exists an injective map $\phi_{F}:F\longrightarrow M_{,}$ ), then  

$$
\dim{\cal F}^{M}=\#2^{M}\quad(a s v e c t o r s p a c e o v e r F),
$$  

i.e. if $B$ is a basis of $F^{M}$ , then there exists a bijective map. $\phi:B\longrightarrow{\mathcal{P}}(M)$ .In particular, we have  

$$
\begin{array}{r l}{\dim\mathbb{R}^{\mathbb{R}}=\#2^{\mathbb{R}}\qquad}&{(a s v e c t o r s p a c e o v e r\mathbb{R}),}\ {\dim(\mathbb{Z}_{2})^{\mathbb{N}}=\#2^{\mathbb{N}(\mathrm{Phil6},\underline{{\operatorname{Th.F.2}}}]}\#\mathbb{R}\qquad}&{(a s v e c t o r s p a c e o v e r\mathbb{Z}_{2}).}\end{array}
$$  

Proof. Let $B$ be a basis of $F^{M}$ . Since $F_{\mathrm{fin}}^{M}$ is a subspace of $F^{M}$ and $\mathrm{dim}F_{\mathrm{fin}}^{M}=\#M$ by (5.36), there exists an injective map $\phi_{M}:{\cal M}\longrightarrow{\cal B}$ by Th. 5.27(b). In consequence, the map $(\phi_{M}\circ\phi_{F}):F\longrightarrow B$ is injective as well. Thus, Th. E.1(b) applies and proves (E.2). For (E.3a), we apply (E.2) with $F=M=\mathbb{R}$ ; for (E.3b), we apply (E.2) with $F=\mathbb{Z}_{2}$ and $M=\mathbb{N}$  

### E.2 Cartesian Products  

Example E.3. In generalization of Ex. 5.2(d), if $I$ is a nonempty index set, $F$ is a field, and $(Y_{i})_{i\in I}$ is a family of vector spaces over. $F$ , then we make the Cartesian product. $\textstyle V:=\prod_{i\in I}Y_{i}$ into a vector space over $F^{\prime}$ by defining for each $a:=(a_{i})_{i\in I},b:=(b_{i})_{i\in I}\in V$  

$$
\begin{array}{l}{{(a+b)_{i}:=a_{i}+b_{i},}}\ {{(\lambda a)_{i}:=\lambda a_{i}\quad\mathrm{for~each~}\lambda\in F:}}\end{array}
$$  

To verify that $(V,+,\cdot)$ is, indeed, a vector space, we begin by checking Def. 5.1(i), i.e. by showing $(V,+)$ is a commutative group: Let. $n=(n_{i})_{i\in I}\in A$ $n_{i}:=0\in Y_{i}$ . Then  

$$
\begin{array}{r}{\forall\qquad\forall\qquad(a+n)_{i}=a_{i}+0=a_{i},}\ {a=(a_{i})_{i\in I}\in V\quad\forall\qquade=(a+n)_{i}=a_{i}+0=a_{i},}\end{array}
$$  

i.e. $a+n=a$ , showing $n$ is the additive neutral element of $V$ . Next, given $a=(a_{i})_{i\in I}\in$ $V$ , define $\bar{a}=(\bar{a}_{i})_{i\in{I}}$ $a_{i}:=-a_{i}$ . Then  

$$
\begin{array}{r l}{\underset{i\in I}{\forall}}&{{}(a+\bar{a})_{i}=a_{i}+(-a_{i})=0,}\end{array}
$$  

i.e. $a+\bar{a}=n=0$ , showing. $a$ to be the additive inverse element of $a$ (as usual, one then. writes $-a$ instead of. $\bar{a}$ . Associativity is verified since  

$$
\begin{array}{r l r}{\forall~}&{{}\forall~}&{\big((a+b)+c\big)_{i}=(a_{i}+b_{i})+c_{i}\overset{(*)}{=}a_{i}+(b_{i}+c_{i})}\ {\forall~}&{{}}&{\underset{i\in I}{\forall}~}\ {(a_{i})_{i}\in I,(b_{i})_{i\in I},(c_{i})_{i\in I}\in V}&{{}_{i\in I}}&{=\big(a+(b+c)\big)_{i},}\end{array}
$$  

where the associativity of addition in the vector space $Y_{i}$ was used at $(*)$ .Likewise, commutativity is verified since.  

$$
\begin{array}{r l}{\bigvee_{\begin{array}{c}{i\in I}\end{array}}}&{{}\forall_{\begin{array}{c}{i\in I}\end{array}}\big(a+b\big)_{i}=a_{i}+b_{i}\overset{(*)}{=}b_{i}+a_{i}=(b+a)_{i},}\end{array}
$$  

where the commutativity of addition in the vector space $Y_{i}$ was used at $(*)$ .This completes the proof that $(V,+)$ is a commutative group.  

To verify Def. 5.1(ii), one computes  

$$
\begin{array}{r l r}{\bigvee_{\lambda\in F}}&{{}\bigvee_{\begin{array}{c}{i\in I}\ {\lambda\in I}\end{array},i\in I}\bigvee_{i\in I}\bigvee_{i\in I}\bigstar\bigotimes_{i}\big(\lambda(a+b)\big)_{i}=\lambda(a_{i}+b_{i})\stackrel{(*)}{=}\lambda a_{i}+\lambda b_{i}}\ {\quad\times\in F}&{{}(a_{i})_{i\in I},(b_{i})_{i\in I}\in V}&{{}i\in I}\end{array}}&{=(\lambda a+\lambda b)_{i},}\end{array}
$$  

where distributivity in the vector space $Y_{i}$ was used at $(*)$ , proving $\lambda(a+b)=\lambda a+\lambda b$ Similarly,  

$$
\begin{array}{r l}{\bigforall}&{{}\underset{\left(a_{i}\right)_{i\in I}\in V}{\forall}\quad\underset{i\in I}{\forall}\quad\left((\lambda+\mu)a\right)_{i}=(\lambda+\mu)a_{i}\overset{(*)}{=}\lambda a_{i}+\mu a_{i}}\ {\underset{{\mathrm{\boldmath~\alpha~}}}{\times}\underset{\left(a_{i}\right)_{i\in I}\in V}{\nabla}\quad\underset{i\in I}{\forall}\quad}&{{}=(\lambda a+\mu a)_{i},}\end{array}
$$  

where, once more, distributivity in the vector space $Y_{i}$ was used at ( $^*$ ), proving $(\lambda+\mu)a=$ $\lambda a+\mu a$  

The proof of Def. 5.1(iii), is given by  

$$
\begin{array}{r}{\underset{\lambda,\mu\in{\cal F}}{\forall}\quad\underset{(a_{i})_{i\in{\cal I}}\in{\cal V}}{\forall}\quad\underset{i\in{\cal I}}{\forall}\quad\left((\lambda\mu)a\right)_{i}=(\lambda\mu)a_{i}\overset{(*)}{=}\lambda(\mu a_{i})=\big(\lambda(\mu a)\big)_{i},}\end{array}
$$  

where the validity of Def. 5.1(iii) in the vector space $Y_{i}$ was used at $(*)$  

Finally, to prove Def. 5.1(iv), one computes  

$$
\begin{array}{r}{\forall\quad\forall\quad(1\cdot a)_{i}=1\cdot a_{i}\stackrel{(*)}{=}a_{i},}\ {(a_{i})_{i\in I}\in V\quad\forall\quad(1\cdot a)_{i}=1\cdot a_{i}\stackrel{(*)}{=}a_{i},}\end{array}
$$  

where the validity of Def. 5.1(iv) in the vector space $Y_{i}$ was used at $(*)$  

Example E.4. In generalization of Ex. 6.7(c), we consider general projections defined on a general Cartesian product of vector spaces, as defined in Ex. E.3 above: Let $I$ be a nonempty index set, let $(Y_{i})_{i\in I}$ be a family of vector spaces over the field $F^{\prime}$ , and let $V:=\prod_{i\in I}Y_{i}$ be the Cartesian product vector space as defined in Ex. E.3. For each $\varnothing\neq J\subseteq I$ , define  

$$
\pi_{J}:V\longrightarrow V_{J}:=\prod_{i\in J}Y_{i},\quad\pi_{J}\left((a_{i})_{i\in I}\right):=(a_{i})_{i\in J},
$$  

calling $\pi_{J}$ the projection onto the coordinates in $J$ We verify $\pi_{J}$ to be linear: Let $\lambda\in F$ and $a:=(a_{i})_{i\in I},b:=(b_{i})_{i\in I}\in V$ . Then  

$$
\begin{array}{c}{{\pi_{J}(\lambda a)=(\lambda a_{i})_{i\in J},=\lambda(a_{i})_{i\in J}=\lambda\pi_{J}(a),}}\ {{\pi_{J}(a+b)=(a_{i}+b_{i})_{i\in J}=(a_{i})_{i\in J}+(b_{i})_{i\in J}=\pi_{J}(a)+\pi_{J}(b),}}\end{array}
$$  

proving $\pi_{J}$ to be linear. Moreover, for each $\varnothing\neq J\subseteq I$ ,  we have  

$$
\mathrm{Im}\pi_{J}=V_{J},\quad\mathrm{ker}\pi_{J}=\{(a_{i})_{i\in I}:a_{i}=0\mathrm{for}\mathrm{each}i\in J\}\cong Y^{I\backslash J},\quad V=V_{J}\oplus\mathrm{ken}(\mathrm{Im}).
$$  

where, for the last equality, we identified  

$$
V_{J}\cong\{(a_{i})_{i\in I}:a_{i}=0\mathrm{for~each}i\not\in J\}.
$$  

## F Python Source Code of Implemented Algorithms  

In the following, we present the source code of implementations for a number of algorithms considered in the main text. All implementations are coded in Python 3.8 (cf. [Gui]).  

### F.1 Linear Systems  

#### F.1.1 Back and Forward Substitution  

The following constitutes code for a Python 3.8 implementation that solves linear systems $A x=b$ with unique solution over. $\mathbb{R}$ and $\mathbb{C}$ via back substitution (cf. Alg. 8.10) in case of given upper triangular matrix $A$ and via forward substitution in case of given. lower triangular matrix. $A$ , providing the respective functions backSub and forwardSub.. The following code is available for download at.  

https://www.math.1mu.de/\~philip/code/LA1/python/linSysBackAndForSub.py # Define functions to solve a triangular linear system: For a lower # triangular matrix via forward substitution; for an upper triangular # matrix via back substitution (which is, actually, just forward. # substitution applied to a flipped version of the upper triangular. # matrix) :  

#### import numpy as np  

# The following functions forwardSub and backSub check if the given   
# matrix is quadratic n times n, where n is the length of the given   
# right-hand side vector b. However, the functions do not check if the   
# matrix is, indeed, triangular -- instead, they always work with the   
# corresponding triangular part of the matrix:   
def forwardSub(lowTriMat,b): # Define exceptions to allow suitable error handling: class exitDueToSizeError(Exception): pass  

try: n = len(b). if lowTriMat.shape. $\mathfrak{l}=\left(\mathtt{n},\mathtt{n}\right)$ .. # Error handling in case of size error:. raise exitDueToSizeError # Initialize with a vector of appropriate size and data type: if np.iscomplexobj(lowTriMat): ${\tt x}=$ np.empty(n,dtype $\r=$ np.complex128) else: x = np.empty(n,dtype=np.float64) # Compute entries of solution vector x, using the forward # substitution algorithm: x[O] = b[0]/lowTriMat[O,O]  

for k in range(1,n): akk $=$ lowTriMat[k,k] x[k] = (b[k] - np.sum(lowTriMat[k,O:k]\*x[O:k]))/akk return x xcept exitDueToSizeError: print("forwardSub:") print(" Error: Must be called with a quadratic matrix A and") print(" a vector b, where, if b has length n, then"). print(" A must be an n times n matrix (i.e. an array"). print(" of shape. $(\mathtt{n},\mathtt{n})!^{\mathfrak{n}})$ print(" Found $\mathsf{l e n}(\mathtt{b})=\"\mathrm{\boldmath~\mathsf~{~+~}~}\mathsf{s t r}(\mathtt{n})+\"\mathrm{\boldmath~\mathsf~{~}}^{\mathfrak{n}},\"\mathrm{\boldmath~\mathsf~{~}})$ print(" shape(A) $\begin{array}{r l}{\mathbf{\omega}}&{{}=\mathbf{\delta}^{\cdots}\mathbf{\delta}+\mathbf{\delta}}\end{array}$ str(lowTriMat.shape)) print(" Stopping program execution.")  

# Define backSub by applying forwardSub to the flipped versions of   
# upTriMat and b:   
def backSub(upTriMat,b): return np.flip(forwardSub(np.flip(upTriMat),np.flip(b)))  

### F.1.2 Gaussian Elimination and LU Decomposition  

The following constitutes code for a Python 3.8 implementation that uses the Gaussian. elimination Alg. 8.17 to solve linear systems. $A x=b$ over $\mathbb{R}$ and $\mathbb{C}$ by transforming the. system into an equivalent system in echelon form. More precisely, function gaussE1 uses the augmented version of the Gaussian elimination algorithm of Sec. 8.4.4 to compute an LU decomposition of. $A$ , and, in modification of Alg. 8.17(b), the so-called column. maximum strategy is applied for row switching: One switches rows. $r$ and $i\geq r$ such that the pivot element in row. $i$ (before the switch) has maximum absolute value (cf.. [Phi23, Def. 5.5]). Function gaussE1Solve applies gaussE1 to the augmented matrix. $(A|b)$ to solve $A x=b$ , whereas function gaussE1So1veFromLU uses a precomputed LU decomposition of. $A$ together with the strategies described in Rem. 8.36 and Rem. 8.25. to solve $A x=b$ . Function matInverseViaLU applies gaussE1SolveFromLU to compute. the inverse matrix of invertible $A$ . The used functions backSub and forwardSub can be found in Sec. F.1.1 above. The following code is available for download at https://www.math.1mu.de/\~philip/code/LA1/python/linSysGaussAndLU.py  

# Define functions to apply the Gaussian elimination algorithm and to # compute LU decompositions:  

import numpy as np from linSysBackAndForSub import backSub,forwardSub  

# Define a function that prints an LU data structure, such as produced   
# by the function gaussEl below (such a data structure consists of a   
# Python dictionary with components 'Atilde', 'p', 'L', and. $\mathbf{\nabla}^{\prime}\underline{{\mathbf{r}}}^{\prime}~,$ ) :   
def 1inSysPrintLU(LU): print("Atilde $=^{11}$ print(LU['Atilde']) print $\because\operatorname{\mathsf{P}}=\operatorname{\mathsf{1}}\operatorname{\mathsf{1}}.$ print(LU['P']) print $"\perp="\perp$ print(LU['L']) print( $\mathbf{\Psi}^{\prime\prime}\mathbf{r}\mathbf{\Psi}=\mathbf{\Psi}^{\prime\prime}\mathbf{\Psi},$ print $\mathrm{~LU}[\mathrm{{}^{\prime}}\mathbf{r}\mathrm{{}^{\prime}}])$ # Define a function that, given matrix A, performs Gaussian elimination, # determining an LU decomposition of the form.   
# $\mathsf{P}{*A}=\mathtt{L}{*A t i l d e}$   
# where Atilde is in echelon form, L is a unipotent lower triangular # matrix, and. $\mathsf{P}$ is a permutation matrix:  

def gaussEl(A): ${\mathfrak{m}}={\mathsf{A}}$ . shape [0] $\mathrm{~n~}=\mathrm{~A~}$ . shape[1] # Copy A to Atilde, casting the entries' data type to float64 # (performing the following calculations with integers will, in # general, not have the desired result): if not(np.iscomplexobj(A)): Atilde $=$ A.astype(np.float64) else: Atilde $=$ np.copy(A) ${\tt{P}}={\tt{n p}}$ .identity(m) L = np.zeros((m,m)) $\mathtt{r}=0$ for c in range(n):. if $\mathtt{r=}\mathtt{=m-1}$ .. break # Perform elimination in column with number c (if necessary), # assuming the upper r rows are already in echelon form, where  

# row switching is performed according to the so-called column # maximum strategy, where one switches rows r and $\mathrm{i}>=\tt r$ such # that the pivot element in row i (before the switch) has # maximum absolute value: index $=$ np.arange(r,m) imax $=$ np.argmax(np.abs(Atilde[index,c]))+r ival $=$ Atilde[imax,c] if ival $\!=0$ . if $\mathtt{r}!=\mathtt{i m a x}$ .. # Switch r-th row with imax-th row: r_imax $=$ np.array([r,imax]) imax_r $=$ np.array([imax,r]) Atilde[r_imax, $\]={}$ Atilde[imax_r,] P[r_imax,] = P[imax_r,] $\mathtt{L}\left[\mathtt{r\_i m a x},\mathtt{j}\right]=\mathtt{L}\left[\mathtt{i m a x\_r},\mathtt{l}\right]$ # Eliminate in column with number c of Atilde and update L # accordingly (this needs to be done first): $\begin{array}{r l r}{\mathrm{L}\left[(\mathrm{r+1}):\mathrm{m},\mathrm{r}\right]}&{=}&{(1/\mathrm{Ati}\mathrm{1de}\left[\mathrm{r},\mathrm{c}\right])*\mathrm{Ati}\mathrm{1de}\left[(\mathrm{r}+1):\mathrm{m},\mathrm{c}\right]}\end{array}$ for i in range $(\mathtt{r}{+}1,\mathtt{m})$ .. # Replace the i-th row with the i-th row plus. # (-Atilde[i,c]/Atilde[r,c]) times the r-th row:. fac $=$ -Atilde[i,c]/Atilde[r,c] Atilde[i,] $=$ Atilde[i,]+fac\*Atilde[r,] $\mathrm{~\boldmath~r~}=\mathrm{~\boldmath~r~}+1$ # Increase row index. p.fill_diagonal(L,1) # Put 1's on diagonal of L.. 'eturn {'Atilde':Atilde, 'p':P, 'L':L, 'r':r}  

# Define a function that, given matrix A and a right-hand side vector b   
# attempts to solve the linear system. $\mathtt{A x}{=}\mathtt{b}$ for x, using Gaussian   
# elimination, returning solution vector x:.   
def gaussElSolve(A,b): # Create augmented matrix of linear system. $\mathtt{A x}{=}\mathtt{b}$ matd $=$ np.column_stack((A,b)) # Perform Gaussian elimination to obtain upper triangular matrix E. # in echelon form: $\mathtt{E}=$ gaussEl(mat)['Atilde'] # Extract upper triangular matrix R and new right-hand side bnew. # for back substitution: ncolR $=$ E.shape[1]-1 R = E[0:len(b),O:ncolR]   
bnew $=$ E[:,ncolR]   
# Solve Rx $\risingdotseq$ bnew using back substitution:   
return backSub(R,bnew)   
# Define a function that, given a data structure containing an LU   
# decomposition $\tt P*A=I*A t i l c$ le of the matrix A and a right-hand side.   
# vector b, attempts to solve the linear system. $\mathtt{A x}{=}\mathtt{b}$ by first solving.   
# $\tt L z=P b$ for z via forwardSub, then solving Atilde\*x. $=_{z}$ for x via backSub,.   
# returning solution vector x:   
def gaussElSolveFromLU(LU,b): $_z=$ forwardSub(LU['L'],np.matmul(LU['P'],b)) return backSub(LU['Atilde'],z)   
# Define a function that, given a Python dictionary, containing an LU   
# decomposition $\mathsf{P}\ast\mathsf{A}{=}\mathsf{L}\ast\mathsf{A}$ tilde of an invertible matrix A, computes and   
# returns the inverse of A:   
def matInverseFromLU(LU): $\mathrm{~n~=~LU}[^{\prime}\mathrm{L}^{\prime}]$ . shape[1] # Create matrix of n standard unit vectors: rhs $=$ np.identity(n) result $=$ np.array([gaussElSolveFromLU(LU,rhs[j,]) for j in np.arange(n)]) return np.transpose(result)   
# Define a function that, given an invertible matrix A, computes and   
# returns the inverse of A, first computing an LU decomposition of A:   
def matInverseViaLU(A): LU $=$ gaussE1(A) return matInverseFromLU(LU)  

#### F.1.3 Examples  

The following constitutes Python 3.8 code, testing some functions for the solution of linear systems:  Matrix $(A|b)$ of Ex. 8.22 is stored in A0, computing the corresponding echelon form $(\tilde{A}|\tilde{b})$ as part of an LU decomposition of $(A|b)$ $(\tilde{A}|\tilde{b})$ is given by component \$Atilde of the LU decomposition) of AO. The solution $x$ to $A x=b$ is then also computed. Matrix $A$ used in Ex. 8.38 and Ex. 8.39 is stored in A1, computing its inverse via the same stragety portrayed in Ex. 8.39 (i.e. by first computing an LU decomposition of A1). The used functions gaussEl, gaussE1Solve, matInverseFromLU, and gaussElSolveFromLU can be found in Sec. F.1.2 above. The following code is available for download at https://www.math.lmu.de/\~philip/code/LA1/python/linSysTest.py  

# Testing some functions for the solution of linear systems:   
# To execute this script file, enter the following command at the   
# command prompt:   
# exec(open("linSysTest.py").read())   
import numpy as np   
from linSysGaussAndLU import 1inSysPrintLU,gaussEl,gaussElSolve   
from linSysGaussAndLU import gaussElSolveFromLU,matInverseFromLU   
print("linSysTest.py: Starting.")   
$\mathtt{A O}=$ np.array([[6,0,1,4], [0,2,0,6], [1,-1,-1, 0]])   
print( $"A O="1$   
print(AO)   
LU $=$ gaussEl(AO)   
print("LU decompostion of A0:")   
linSysPrintLU(LU)   
$\mathtt{A}=\mathtt{n p}$ .array([[6,0,1], [0,2,0], [1,-1,-1]])   
print( $"\mathtt{A}="\mathtt{\Gamma},$   
print(A)   
b $=$ np.array([4,6,0])   
print( $v_{b}=11)$   
print(np.reshape(b,(3,1)))   
${\tt x}=$ gaussElSolve(A,b)   
print $\because A x=6$ is solved by")   
print $\cdots\mathtt{x}=\mathtt{u}\cdot$   
print(np.reshape(x,(3,1))) ${\tt A1}={\tt n p}$ .array([[1,4,2,3], [0,0,1,4], [2,6,3,1], [1,2,1, 0]]) print( $"\mathbb{A}1="\$   
print(A1)   
LU $=$ gaussEl(A1)   
A1invLU $=$ matInverseFromLU(LU)   
print("Inverse of A1 via LU:").   
print( $"4*\tt A1$ invLU $=^{11}$  

print( $\mathtt{4}{\ast}\mathtt{A1}$ invLU) print("A1\*A1invLU. $=^{11}$ print(np.matmul(A1,A1invLU))  

b $=$ np.array([-1,2,-3,4])   
print( $"6="2$   
print(np.reshape(b,(4,1)))   
${\tt x}=$ gaussElSolveFromLU(LU,b)   
# ${\tt x}=$ gaussElSolve(A1,b)   
print( $\because A1*_{\mathrm{X}}=6$ is solved by (found via LU)")   
print( $\cdots_{\mathfrak{X}}="\big.$   
print(np.reshape(x,(4,1)))  

print("linSysTest.py: Done.")  

## References  

[Bla84] A. BLAss. Existence of Bases Implies the Axiom of Choice. Contemporary Mathematics 31 (1984), 31-33.   
[EFTO7] H.-D. EBBINGHAUs, J. FLUM, and W. THOMAs. Einfuhrung in die mathematische Logik, 5th ed. Spektrum Akademischer Verlag, Heidelberg, 2007 (German).   
[Gui] GUIDO VAN ROSSUM AND THE PYTHON DEVELOPMENT TEAM. PythOn Documentation. https://docs.python.org/3/, [Online; accessed 14-August2023].   
[Hal17] LORENz J. HALBEIsen. Combinatorial Set Theory, 2nd ed. Springer Mono-. graphs in Mathematics, Springer, Cham, Switzerland, 2017..   
[Jec73] T. Jech. The Axiom of Choice. North-Holland, Amsterdam, 1973..   
[Kun80] KeNneTH Kunen. Set Theory. Studies in Logic and the Foundations of Mathematics, Vol. 102, North-Holland, Amsterdam, 1980..   
[Kun12] KenneTH KuNen. The Foundations of Mathematics. Studies in Logic,. Vol. 19, College Publications, London, 2012..   
[Phi16] P. Philip. Analysis I: Calculus of One Real Variable. Lecture Notes, LMU Munich, 2015/2016, AMS Open Math Notes Ref. # OMN:202109.111306, available in PDF format at https://www.ams.org/open-math-notes/omn-view-listing?listingId=111306.   
[Phi17] P.Philip.Functional Analysis.Lecture Notes,. Ludwig-Maximilians-Universitat, Germany, 2017, available in PDF format  at http://www.math.lmu.de/\~philip/publications/lectureNot. es/philipPeter_FunctionalAnalysis.pdf.   
[Phi19] P. PhILip. Linear Algebra HI. Lecture Notes, Ludwig-Maximilians-Universitat, Germany, 2019, AMS Open Math Notes Ref. # OMN:202109.111305, available in PDF format at https://www.ams.org/open-math-notes/omn-view-listing?listingId=111305.   
[Phi23] P. PhiLip. Numerical Mathematics I. Lecture Notes, Ludwig-Maximilians-Universitat, Germany, 2022/2023, AMS Open Math Notes Ref. # OMN:202204.111317, available in PDF format at https://www.ams.org/open-math-notes/omn-view-listing?listingId=111317.   
[Str08] GeRnoT STRoTH. Lineare Algebra, 2nd ed. Berliner Studienreihe zur Mathematik, Vol. 7, Heldermann Verlag, Lemgo, Germany, 2008 (German).   
[Wik21] WIKIPEDIA CoNTRIBUTORs. HOL Light _ Wikipedia, The Free Encyclopedia. https://en.wikipedia.org/w/index.php?title=H0L_Light, 2021, [Online; accessed 5-February-2023].   
[Wik22a] WIKIPEDIA ConTRIBUTORs. Coq - Wikipedia, The Free Encyclopedia. https://en.wikipedia.org/w/index.php?title=Coq, 2022, [Online; accessed 5-February-2023].   
[Wik22b] WIKIPEDIA ConTRIBUTORs. Isabelle (proof assistant) _Wikipedia, The Free Encyclopedia. https://en.wikipedia.org/w/index.php?title= Isabelle_(proof_assistant), 2022, [Online; accessed 5-February-2023].   
[Wik22c] WIKIPEDIA CoNTRIBUTORs. Lean (proof assistant)  Wikipedia, The Free Encyclopedia. https://en.wikipedia.org/w/index.php?title=Lean_ (proof_assistant), 2022, [Online; accessed 5-February-2023].  