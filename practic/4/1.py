class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_after(self, prev_node, new_data):
        if not prev_node:
            print("Узел, после которого нужно вставить, не может быть None")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        new_node.prev = prev_node

        if prev_node.next:
            prev_node.next.prev = new_node

        prev_node.next = new_node

    def delete_node(self, node):
        if self.head is None or node is None:
            return

        if node == self.head:
            self.head = node.next

        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node
        new_node.prev = last

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)

node_to_insert_after = dll.head.next
dll.insert_after(node_to_insert_after, 2.5)

node_to_delete = node_to_insert_after.next
dll.delete_node(node_to_delete)

for data in dll:
    print(data)