class Stack:
    def __init__(self):
        self.stack = []



    def is_empty(self):
        return self.stack is None

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("Ошибка")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("<UNK>")
        return self.stack[-1]

class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        self.stack1.push(value)

    def dequeue(self):

        for i in self.stack1.stack:
            removed = self.stack1.pop()
            self.stack2.push(removed)
        return self.stack2.pop()

    def peek(self):
        for i in self.stack1.stack:
            removed = self.stack1.pop()
            self.stack2.push(removed)
        return self.stack2.peek()

mystk1 = Stack()
mystk1.push(10)
mystk1.push(20)
mystk1.push(30)

print(mystk1.peek())