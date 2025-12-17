def infix_to_rpn(expr):
    priority = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = []
    output = []
    i = 0

    while i < len(expr):
        if expr[i].isdigit():
            num = ''
            while i < len(expr) and expr[i].isdigit():
                num += expr[i]
                i += 1
            output.append(num)
            continue
        elif expr[i] in priority:
            while stack and stack[-1] in priority and priority[stack[-1]] >= priority[expr[i]]:
                output.append(stack.pop())
            stack.append(expr[i])
        elif expr[i] == '(':
            stack.append(expr[i])
        elif expr[i] == ')':
            while stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        i += 1

    while stack:
        output.append(stack.pop())

    return output

def calc_rpn(rpn):
    stack = []

    for t in rpn:
        if t.isdigit():
            stack.append(int(t))
        else:
            b = stack.pop()
            a = stack.pop()
            if t == '+': stack.append(a + b)
            if t == '-': stack.append(a - b)
            if t == '*': stack.append(a * b)
            if t == '/': stack.append(a // b)

    return stack[0]

expr = input("Введите выражение: ")
rpn = infix_to_rpn(expr)
print("ОПН:", " ".join(rpn))
print("Результат:", calc_rpn(rpn))