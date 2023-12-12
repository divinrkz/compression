class HuffmanNode:
2 def __init__(self, data=None):
3 self.data = data
4 self.left = None
5 self.right = None
6
7 def construct_tree(huffman_codes):
8 root = HuffmanNode()
9 for code, data in huffman_codes.items():
10 node = root
11 for bit in code:
12 if bit == ’0’:
13 if not node.left:
14 node.left = HuffmanNode()
15 node = node.left
16 else:
17 if not node.right:
18 node.right = HuffmanNode()
19 node = node.right
20 node.data = data
21 return root
22
23 def decode(huffman_tree: HuffmanNode, encoded_message):
24 decoded_msg = ""
25 node = huffman_tree
26 for bit in encoded_message:
27 if bit == ’0’:
28 node = node.left
29 else:
30 node = node.right
31 if node.data is not None:
32 decoded_msg += chr(node.data)
33 node = huffman_tree
34 return decoded_msg
35
36 huffman_tree = construct_tree(dict)
37 print(decode(huffman_tree, (bin(int(msg, 16))[2:])))