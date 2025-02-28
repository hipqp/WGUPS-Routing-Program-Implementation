class HashTable:
    def __init__(self, size):
        self.size = size
        self.map = [None] * size
#Creates the hash key
    def _get_hash(self, key):
        hash: int = 0
        for char in key:
            hash += ord(char)
        return hash % self.size
#Adds to the hash table
    def add(self, key, value):
        hashed_key = self._get_hash(key)
        key_value = [key, value]

        if self.map[hashed_key] is None:
            self.map[hashed_key] = []
            self.map[hashed_key].append(key_value)
            return True
        else:
            for pair in self.map[hashed_key]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[hashed_key].append(key_value)
            return True
#Retrieves from the hash table
    def get(self, key):
        key = self._get_hash(key)
        if self.map[key] is not None:
            for pair in self.map[key]:
                if pair[0] == key:
                    return pair[1]
        return None
#Removes from the hash table
    def delete(self, key):
        hashed_key = self._get_hash(key)

        if self.map[hashed_key] is None:
            return None
        for i in range(0, len(self.map[hashed_key])):
            if self.map[hashed_key][i][0] == key:
                self.map[hashed_key].pop(i)
                return True
        return False
#Prints the table
    def print_table(self):
        print('entire table')
        for item in range(0, len(self.map)):
            if item is not None:
                print(str(item))

h = HashTable(10)
h.add('bob','1748')
h.print_table()
h.delete('bob')
print(h.map)