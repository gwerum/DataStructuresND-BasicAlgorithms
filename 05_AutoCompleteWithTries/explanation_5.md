## Explanation for Trie.ipynb

### Task
The task of this exercise is to implement a *Trie data structure*, which stores word lists and will be used for an autocomplete function.

### Code explanation

Each Trie node holds one char, which means storing a word in the Trie results in a node chain whose number of nodes equals the number of chars of the word. Words starting with the same char or sequence of chars will share those nodes and, thus, reduce the storage size.

Three main methods have been implemented:

1. **Trie()::insert(word)**: This method adds a new word to the Trie by adding one Trie node per char. If the first first nodes already exist in the Trie because the words shares the starting sequence with another word already added to the Trie, only the nodes starting from the point where the words differ will be added.

2. **Trie()::find(prefix)**: This methods checks if given prefix (starting sequence of chars) exists in the Trie. It always searches starting from the root and returns the node holding the last char of the prefix, if the word exists in the Trie.

3. **TrieNode()::suffixes()**: This method returns all possible suffixes of a given Trie node. It searches the Trie downwards starting from the given node in a recursive manner.

---

### Runtime efficiency

Storing a dictionary of words in the Trie requires creating on node for each char m of each word. The number of shared chars o will reduce the storage space, however, in general, the total number of words n will be much larger than the average number of chars n per word and the average number of shared chars o per word.

Finding a node for a given prefix of size p requires for each char to check if the current node has a child holding that char. The childs are stored in a dictionary, whose maximum size equals the number of letters in the alphabet. At least for the english alphabet this number is small (26), thus, the access time can be assumed of order O(1). Therefore, finding the ending node of a given prefix of size p is of order O(p), which reduces to O(1) since p << n.

Finding all suffixes is similar to finding a prefix node with the difference that the search doesn't start from the Trie root but from the node of the last char of the prefix till the last char of each possible suffix. Assuming a suffix of average size s finding each suffix comes with a cost of order O(s). Again, the suffix size s and the number of possible suffixes is small compared to the total number of words stored in the Trie, so time complexity can be assumed to be constant O(1).


|  | Time complexity | Space complexity |
| ------------------- | --------------- | ---------------- |
| Storing m words of average size n | O(n*m) ~ **O(n)** | O(n*(m-o)) ~ **O(n)** |
| Finding node for given prefix of size p | O(p) ~ **O(1)** | |
| Finding all suffixes for given prefix | O(s) ~ **O(1)** | |

**n**: total number of words stored in Trie
**m**: average number of chars per word stored in Trie
**o**: average number of shared chars per word stored in Trie
**p**: averager number of chars in prefix to be searched
**s**: average number of chars in suffixes to be found


---

### Test Cases

For this exercise no additional test cases have been implemented. The functionality can be tested in the Jupyter Notebook.