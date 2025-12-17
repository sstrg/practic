import random
import string

class HashTable:
    def __init__(self, size, bad=False):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.bad = bad
        self.collisions = 0

    def _hash(self, key):
        if self.bad:
            return 1
        h = 0
        for c in key:
            h = (h * 31 + ord(c)) % self.size
        return h

    def put(self, key):
        index = self._hash(key)
        if self.table[index]:
            self.collisions += 1
        self.table[index].append(key)

def random_word(length=6):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

words = [random_word() for _ in range(1000)]

bad_ht = HashTable(50, bad=True)
good_ht = HashTable(50, bad=False)

for w in words:
    bad_ht.put(w)
    good_ht.put(w)

print("Плохая хэш-функция:")
print("Коллизии:", bad_ht.collisions)
print("Размер самой длинной цепочки:", max(len(b) for b in bad_ht.table))

print()

print("Хорошая хэш-функция:")
print("Коллизии:", good_ht.collisions)
print("Размер самой длинной цепочки:", max(len(b) for b in good_ht.table))