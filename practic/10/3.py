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

    def _dfs(self, node, path, results):
        if node.end:
            results.append(path)
        for c, child in node.children.items():
            self._dfs(child, path + c, results)

    def autocomplete(self, prefix, freq_map):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return []
            node = node.children[c]
        results = []
        self._dfs(node, prefix, results)
        results.sort(key=lambda w: freq_map.get(w, 0), reverse=True)
        return results

trie = Trie()
freq_map = {}

words = ["cat", "car", "cart", "dog", "dove", "door", "car", "cart", "cat", "dog", "dog"]

for w in words:
    freq_map[w] = freq_map.get(w, 0) + 1
    trie.insert(w)

print(trie.autocomplete("ca", freq_map))  
print(trie.autocomplete("do", freq_map))
print(trie.autocomplete("car", freq_map))