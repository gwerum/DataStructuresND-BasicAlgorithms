import pdb
import unittest

## Represents a single node in the Trie
class TrieNode():
    def __init__(self, char = None, is_last_char=False):
        ## Initialize this node in the Trie
        self.char = char
        self.is_word = is_last_char
        self.children = {}

    def __repr__(self, level=0):
        ret = "  "*level+repr(self.char)+": "+str(self.is_word)+"\n"
        for child in self.children.values():
            ret += child.__repr__(level+1)
        return ret

    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode(char)

    def suffixes(self):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        suffixes = []
        if self.is_word:
            suffixes += ['']
        for child in self.children.values():
            for suffix in child.suffixes():
                suffixes += [child.char + suffix]
        return suffixes
     
## The Trie itself containing the root node and insert/find functions
class Trie():
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def __repr__(self):
        return self.root.__repr__()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.insert(char)
            current_node = current_node.children[char]

        current_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root
        for char in prefix:
            children = current_node.children
            if char not in children:
                return None
            current_node = children[char]

        return current_node

    def autocomplete(self, prefix):
        # Returns optional suffixes for given prefix
        prefix_node = self.find(prefix.lower())
        if prefix_node:
            return prefix_node.suffixes()
        return []

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


class TestWordTrie(unittest.TestCase):
    """docstring for TestWordTrie"""
    @classmethod
    def setUpClass(cls):
        super(TestWordTrie, cls).setUpClass()
        cls.word_list = [
        "ant", "anthology", "antagonist", "antonym",\
        "fun", "function", "factory",\
        "trie", "trigger", "trigonometry", "tripod"\
        ]
        cls.word_trie = Trie()
        for word in cls.word_list:
            cls.word_trie.insert(word)

    def test_existing_words(cls):
        print("\n##### Test case 1: Autocomplete existing words #####")
        print("\nInput word list to word trie:\n{}".format(cls.word_list))
        input_list = ["a","f","t","ant","fun","func","tri","trig"]
        for prefix in input_list:
            cls.run_test(prefix)

    def test_existing_words_uppercase(cls):
        print("\n##### Test case 2: Autocomplete existing words (uppercase) #####")
        print("\nInput word list to word trie:\n{}".format(cls.word_list))
        input_list = ["A","F","T","Ant","Fun","funC","TRi","TriG"]
        for prefix in input_list:
            cls.run_test(prefix)

    def test_non_existing_words(cls):
        print("\n##### Test case 3: Autocomplete non-existing words #####")
        print("\nInput word list to word trie:\n{}".format(cls.word_list))
        input_list = ["Lorem","ipsum","dolor","sit","amet"]
        for prefix in input_list:
            cls.run_test(prefix)

    def run_test(cls, input_prefix):
        print("\nInput prefix: {}".format(input_prefix))
        expected_suffixes = cls.expected_suffixes(input_prefix)
        print("Expected suffixes: {}".format(expected_suffixes))
        actual_suffixes = cls.word_trie.autocomplete(input_prefix)
        print("Returned suffixes: {}".format(actual_suffixes))
        cls.assertEqual(sorted(actual_suffixes), sorted(expected_suffixes))

    def expected_suffixes(cls, prefix):
        expected_suffixes = []
        for word in cls.word_list:
            if word.startswith(prefix.lower()):
                expected_suffixes.append(word[len(prefix.lower()):])
        return expected_suffixes
        



