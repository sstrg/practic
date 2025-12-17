class HashTable:
    def __init__(self, size=16):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        h = 0
        for c in key:
            h = (h * 31 + ord(c)) % self.size
        return h

    def insert(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        if key not in bucket:
            bucket.append(key)

    def search(self, key):
        index = self._hash(key)
        return key in self.table[index]

    def delete(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        if key in bucket:
            bucket.remove(key)
            return True
        return False