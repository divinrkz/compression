# Lossless Data Compression.
To represent a specific encoding, we can imagine it as a binary tree diagram, where each character is a leaf node. So, we can find a character's encoding, by tracing the route from the tree's root to the character's leaf, with left edges indicating $0$ and right edges indicating $1$.

Huffman's algorithm is a [greedy algorithm](https://en.wikipedia.org/wiki/Greedy_algorithm), which operates on the principle of generating local optimal codes with the aim of achieving a global optimum. It thus chooses the most immediate option at each step that seems to progress towards the ultimate goal. Specifically for Huffman's algorithm, the key is to merge the two smallest nodes. This action increases the length of their character encodings by one bit due to the new parent node. However, since these are the least common characters, assigning them longer bit patterns is more efficient than doing so for more frequent characters. This approach of Huffman's algorithm indeed results in the most efficient overall character encoding.

I claim that Huffman’s coding gives an optimal cost prefix tree.

### <ins>Proof</ins>
Let $n$ be the number of symbols. <br>

Given frequencies $f_1,...,f_n$ to find the optimal prefix-free code that minimizes $\sum_n^if_i$ (length of encoding the $i$-<i>th</i> symbol) is the same as s finding the full binary tree with n leaves, one per symbol in $1,...n$ that minimizes $\sum^n_i=1f_i$ (depth of leaf of the $i$-<i>th</i> symbol)


We go by induction on $n$.

<b><ins>Base case ($n = 2$)</b></ins>: There’s only one full binary tree with $2$ leaves.  <br>Therefore, the base case holds.
<br>

<b><ins>Induction Hypothesis:</b></ins>: Suppose the claim is true for some sequence of $n−1$ frequencies.

 <b><ins>Inductive Step:</b></ins>: Let $f_1,...f_n$ be any $n$ frequencies. Assume
without loss of generality that $f_1 \leq f_2 \leq ... \leq f_n$ (by relabeling). Note that there’s an
optimal tree $T$ for which the leaves marked with $1$ and $2$ are siblings. Let’s denote the tree
that Huffman strategy gives by $H$. Note that we are not claiming that $T = H$ but rather that T and H have the same cost. We will now remove both leaves marked by $1$ and $2$ from $T$, making their father a new leaf with frequency $f_1+f_2$. This therefore, results into us a new binary tree $T'$ on $n−1$ leaves with frequencies $f_1 + f_2, f_3, f_4, ..., f_n$. We do the same for the Huffman tree giving us a tree $H'$ on $n − 1$ leaves with frequencies $f_1 + f_2, f_3, f_4,... , f_n$. Note that $H'$ is exactly the Huffman tree on frequencies $f1 + f2, f3, f4, ... , fn$ by definition of Huffman’s coding. By my induction
hypothesis, $cost(H') = cost(T')$. Note that, $cost(T'
) = cost(T) − (f_1 + f_2)$ since to get $T'$ from $T$ we replaced two nodes with frequencies $f_1$ and $f_2$ at some depth $d$ with one node with frequency $f1 + f2$ at depth $d − 1$. This lowers the cost by $f1 + f2$. Similarly,
$cost(H') = cost(H) − (f1 + f2)$
It follows that
$cost(H)$ = $cost(H') + f1 + f2 = cost(T') + f1 + f2 = cost(T)$