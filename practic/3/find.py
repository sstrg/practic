class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def push_back(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def find(self, value):
        cur = self.head
        while cur:
            if cur.value == value:
                return cur
            cur = cur.next
        return None

    def to_list(self):
        res = []
        cur = self.head
        while cur:
            res.append(cur.value)
            cur = cur.next
        return res

lst = SinglyLinkedList()
lst.push_back(1)
lst.push_back(2)
lst.push_back(3)

node = lst.find(3)
print(node.value if node else "Не найдено")
print(lst.to_list())