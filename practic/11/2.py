class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if not node:
            return Node(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        return node

    def is_balanced(self):
        return self._height(self.root) != -1

    def _height(self, node):
        if not node:
            return 0
        left = self._height(node.left)
        if left == -1:
            return -1
        right = self._height(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return max(left, right) + 1


bst = BST()
for v in [10, 5, 2, 1]:
    bst.insert(v)

print(bst.is_balanced())

bst.insert(8)
bst.insert(7)

print(bst.is_balanced())