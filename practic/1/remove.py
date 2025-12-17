arr = [None] * 10
size = 0

def append(value):
    global size
    arr[size] = value
    size += 1

def remove_manual(value):
    global size

    for i in range(size):
        if arr[i] == value:

            for j in range(i, size - 1):
                arr[j] = arr[j + 1]
            size -= 1
            return True
    return False

def to_list():
    return arr[:size]

append(10)
append(20)
append(30)

remove_manual(30)

print(to_list())