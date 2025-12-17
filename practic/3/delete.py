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

    def remove(self, value):
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        prev = self.head
        cur = self.head.next

        while cur:
            if cur.value == value:
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next

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
lst.remove(2)
print(lst.to_list())