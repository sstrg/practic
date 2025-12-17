class ArrayStack:
    def __init__(self, initial_capacity = 10):
        self._capacity = initial_capacity
        self._values = [None] * initial_capacity
        self._index = 0

    def push(self, value):
        if self._index == self._capacity:
            self._resize()
        self._values[self._index] = value
        self._index += 1

    def _resize(self):
        new_capacity = int(self._capacity*1,5) + 1
        new_values = [None] * new_capacity

        for i in range(self._index):
            new_values[i] = self._values[i]

        self.values = new_values
        self.capacity = new_capacity

    def pop(self):
        if self._index == 0:
            raise IndexError("pop from empty stack")
        self._index -=1
        return self._values[self._index]