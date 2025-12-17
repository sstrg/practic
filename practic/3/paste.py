class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = node

    def push_back(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def to_list(self):
        res = []
        cur = self.head
        while cur:
            res.append(cur.value)
            cur = cur.next
        return res

lst = SinglyLinkedList()
lst.push_front(2)
lst.push_front(1)
lst.push_back(3)
lst.push_back(4)

print(lst.to_list())