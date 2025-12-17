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

    def autocomplete(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return []
            node = node.children[c]
        results = []
        self._dfs(node, prefix, results)
        return results

    def _dfs(self, node, path, results):
        if node.end:
            results.append(path)
        for c, child in node.children.items():
            self._dfs(child, path + c, results)

trie = Trie()
words = ["cat", "car", "cart", "dog", "dove", "door"]

for w in words:
    trie.insert(w)

print(trie.autocomplete("ca")) 
print(trie.autocomplete("do"))
print(trie.autocomplete("car"))
print(trie.autocomplete("x"))