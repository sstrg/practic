arr = [None] * 10
size = 0

def append(value):
    global size
    arr[size] = value
    size += 1

def find(value):
    for i in range(size):
        if arr[i] == value:
            return i
    return -1

def remove_manual(value):
    global size
    idx = find(value)
    if idx == -1:
        return False
    for j in range(idx, size - 1):
        arr[j] = arr[j + 1]
    size -= 1
    return True

def to_list():
    return arr[:size]

append(10)
append(20)
append(30)

print(find(30))


print(to_list())