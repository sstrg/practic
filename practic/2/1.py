class DynamicArray:
    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.data = [None] * 2

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity

        for i in range(self.size):
            new_data[i] = self.data[i]

        self.data = new_data
        self.capacity = new_capacity

    def append(self, value):
        if self.size == self.capacity:
            self._resize(self.capacity * 2)

        self.data[self.size] = value
        self.size += 1

    def get(self, index):
        if 0 <= index < self.size:
            return self.data[index]
        return None

    def __str__(self):
        items = []
        for i in range(self.size):
            items.append(str(self.data[i]))
        return "[" + ", ".join(items) + "]"

    def __len__(self):
        return self.size



arr = DynamicArray()
print(f"Пустой массив: {arr}, размер: {len(arr)}")


for i in range(5):
    arr.append(i * 10)
    print(f"Добавили {i * 10}: {arr}, размер: {len(arr)}, емкость: {arr.capacity}")


print(f"arr.get(2) = {arr.get(2)}")
print(f"arr.get(10) = {arr.get(10)}")