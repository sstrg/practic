class MinHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, index):
        return (index - 1) // 2

    def _left(self, index):
        return 2 * index + 1

    def _right(self, index):
        return 2 * index + 2

    def _heapify_up(self, index):
        while index > 0 and self.heap[index] < self.heap[self._parent(index)]:
            self.heap[index], self.heap[self._parent(index)] = self.heap[self._parent(index)], self.heap[index]
            index = self._parent(index)

    def _heapify_down(self, index):
        smallest = index
        left = self._left(index)
        right = self._right(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        minimum = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return minimum

    def build_heap(self, arr):
        self.heap = arr[:]
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)

    def get_heap(self):
        return self.heap

# -------------------------
# проверка корректности куч
def is_min_heap(heap):
    n = len(heap)
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and heap[i] > heap[left]:
            return False
        if right < n and heap[i] > heap[right]:
            return False
    return True
heap = MinHeap()

# проверка построения кучи
arr = [5, 3, 8, 1, 2, 7]
heap.build_heap(arr)
print("это построенная куча:", heap.get_heap())
assert is_min_heap(heap.get_heap()), "ошибка: куча некорректна после build_heap"
assert heap.get_heap()[0] == min(arr), "ошибка: минимальный элемент неверен после build_heap"

# проверка вставкии
heap.insert(0)
print("после вставки 0:", heap.get_heap())
assert is_min_heap(heap.get_heap()), "ошибка: куча некорректна после вставки"

heap.insert(4)
print("после вставки 4:", heap.get_heap())
assert is_min_heap(heap.get_heap()), "ошибка: куча некорректна после вставки"

# проверка извлечения минимума
prev_heap = heap.get_heap()[:]
min_val = heap.extract_min()
print("извлеченный минимум:", min_val)
print("куча после извлечения минимума:", heap.get_heap())
assert min_val == min(prev_heap), "ошибка: извлечён неправильный минимум"
assert is_min_heap(heap.get_heap()), "ошибка: куча некорректна после извлечения минимума"