class PyArray:
    def __init__(self):
        self.data = []

    def push_front(self, value):
        self.data.insert(0, value)

    def push_back(self, value):
        self.data.append(value)

    def __str__(self):
        return str(self.data)



py = PyArray()
py.push_back(3)
py.push_back(4)
py.push_front(2)
py.push_front(1)
py.push_back(5)

print(py)