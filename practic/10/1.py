class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end = True

    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.end

    def starts_with(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True

trie = Trie()
words = ["cat", "car", "dog", "cart"]

for w in words:
    trie.insert(w)

print(trie.search("cat"))
print(trie.search("ca"))
print(trie.starts_with("ca"))
print(trie.search("cart"))
print(trie.starts_with("do"))  
print(trie.starts_with("bat"))