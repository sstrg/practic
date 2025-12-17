class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.count += 1
        node.is_end = True

    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_end

    def count_prefix(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.count

    def delete(self, word):
        self._delete(self.root, word, 0)

    def _delete(self, node, word, i):
        if i == len(word):
            if not node.is_end:
                return False
            node.is_end = False
            return True

        c = word[i]
        if c not in node.children:
            return False

        deleted = self._delete(node.children[c], word, i + 1)
        if deleted:
            node.children[c].count -= 1
            if node.children[c].count == 0:
                del node.children[c]
        return deleted


trie = Trie()

words = ["apple", "app", "apply", "apt", "bat"]
for w in words:
    trie.insert(w)

print(trie.search("app"))
print(trie.search("apps"))

print(trie.count_prefix("ap"))
print(trie.count_prefix("app"))
print(trie.count_prefix("b"))

trie.delete("app")

print(trie.search("app"))
print(trie.count_prefix("app"))