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

mystk = Stack()

user_write = input()
if len(user_write) % 2 != 0:
    print("Скобочное выражение неверно")
is_correct = True
for i in user_write:
    if i in "({[":
        mystk.push(i)
#()
    if i in ")":
        if "(" in mystk.stack:
            mystk.push(i)
        else:
            print("Скобочное выражение неверно")
            is_correct = False
            break
#{}
    if i in "}":
        if "{" in mystk.stack:
            mystk.push(i)
        else:
            print("Скобочное выражение неверно")
            is_correct = False
            break
#[]
    if i in "]":
        if "[" in mystk.stack:
            mystk.push(i)
        else:
            print("Скобочное выражение неверно")
            is_correct = False
            break
if mystk.stack.count("(") != mystk.stack.count(")"):
    print("Скобочное выражение неверно")
elif mystk.stack.count("{") != mystk.stack.count("}"):
    print("Скобочное выражение неверно")
elif mystk.stack.count("[") != mystk.stack.count("]"):
    print("Скобочное выражение неверно")
elif is_correct:
    print('Скобоное выражение верно')
