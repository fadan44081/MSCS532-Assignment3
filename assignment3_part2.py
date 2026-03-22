class HashTableChaining:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # list of buckets
        self.count = 0  # number of elements

    # ---------------------------
    # Hash function
    # ---------------------------
    def hash_function(self, key):
        return hash(key) % self.size

    # ---------------------------
    # Insert
    # ---------------------------
    def insert(self, key, value):
        index = self.hash_function(key)
        bucket = self.table[index]

        # Check if key already exists → update
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # Otherwise add new key
        bucket.append((key, value))
        self.count += 1

        # Resize if load factor too high
        if self.load_factor() > 0.75:
            self.resize()

    # ---------------------------
    # Search
    # ---------------------------
    def search(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]

        for (k, v) in bucket:
            if k == key:
                return v

        return None

    # ---------------------------
    # Delete
    # ---------------------------
    def delete(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.count -= 1
                return True

        return False

    # ---------------------------
    # Load factor
    # ---------------------------
    def load_factor(self):
        return self.count / self.size

    # ---------------------------
    # Resize (rehashing)
    # ---------------------------
    def resize(self):
        print("Resizing table...")

        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0

        for bucket in old_table:
            for (k, v) in bucket:
                self.insert(k, v)


# ---------------------------
# Testing the Hash Table
# ---------------------------
if __name__ == "__main__":
    ht = HashTableChaining()

    print("Inserting values...")
    ht.insert("apple", 10)
    ht.insert("banana", 20)
    ht.insert("orange", 30)
    ht.insert("grape", 40)

    print("Search apple:", ht.search("apple"))
    print("Search banana:", ht.search("banana"))

    print("Deleting banana...")
    ht.delete("banana")

    print("Search banana after delete:", ht.search("banana"))

    print("Current load factor:", ht.load_factor())