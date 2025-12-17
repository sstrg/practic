class PriorityQueue:
    def __init__(self):
        self.heap = []

    def _parent(self, index):
        return (index - 1) // 2

    def _left(self, index):
        return 2 * index + 1

    def _right(self, index):
        return 2 * index + 2

    def _heapify_up(self, index):
        while index > 0 and self.heap[index][1] < self.heap[self._parent(index)][1]:
            self.heap[index], self.heap[self._parent(index)] = self.heap[self._parent(index)], self.heap[index]
            index = self._parent(index)

    def _heapify_down(self, index):
        smallest = index
        left = self._left(index)
        right = self._right(index)

        if left < len(self.heap) and self.heap[left][1] < self.heap[smallest][1]:
            smallest = left
        if right < len(self.heap) and self.heap[right][1] < self.heap[smallest][1]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def push(self, value, priority):
        self.heap.append((value, priority))
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()[0]
        min_item = self.heap[0][0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_item

    def peek(self):
        return self.heap[0][0] if self.heap else None

    def is_empty(self):
        return len(self.heap) == 0

pq = PriorityQueue()
pq.push("Задача 1", 5)
pq.push("Задача 2", 3)
pq.push("Задача 3", 7)
pq.push("Задача 4", 1)

print("Элементы по приоритету:")
while not pq.is_empty():
    print(pq.pop())