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

    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

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

print(lst.to_list())

lst.reverse()
print(lst.to_list())