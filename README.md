# Lossless Data Compression.
To represent a specific encoding, we can imagine it as a binary tree diagram, where each character is a leaf node. o, we can find a character's encoding, by tracing the route from the tree's root to the character's leaf, with left edges indicating $0$ and right edges indicating $1$.

Huffman's algorithm is a greedy algorithm, which operates on the principle of making small-scale, local optimal decisions with the aim of achieving a global optimum. It chooses the most immediate option at each step that seems to progress towards the ultimate goal. Specifically for Huffman's algorithm, the key is to merge the two smallest nodes. This action increases the length of their character encodings by one bit due to the new parent node. However, since these are the least common characters, assigning them longer bit patterns is more efficient than doing so for more frequent characters. This approach of Huffman's algorithm indeed results in the most efficient overall character encoding.

I claim that Huffman coding is optimal.

### <u>Proof</u>
