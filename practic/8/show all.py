class HashTable:
    def __init__(self, size=5):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        h = 0
        for c in key:
            h = (h * 31 + ord(c)) % self.size
        return h

    def put(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def remove(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False

    def show(self):
        for i, bucket in enumerate(self.table):
            print(i, "->", bucket)
