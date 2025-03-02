


class HashTable:
    def __init__(self, size):
        self.size = size
        self.map = [None] * size

#Creates the hash key
    def _get_hash(self, package_id):

        return int(package_id) % self.size

#Resizes the hash table
    def _resize(self,current_size):
        new_size = self.size * 2
        new_map = [None] * new_size

        for bucket in range(current_size):
            if bucket is not None:
                for package in bucket:
                    new_hash = int(package[0]) % new_size  # Rehash package ID
                    if new_map[new_hash] is None:
                        new_map[new_hash] = []
                    new_map[new_hash].append(package)  # Reinsert package data

            self.size = new_size
            self.map = new_map


#Adds to the hash table
    def insert(self, package_id, delivery_address, delivery_deadline, delivery_city,
               delivery_zipcode, package_weight, delivery_status, delivery_time=""):
        """Inserts package data into the hash table."""
        hashed_key = self._get_hash(package_id)
        package_data = [package_id, delivery_address, delivery_deadline, delivery_city,
                        delivery_zipcode, package_weight, delivery_status, delivery_time]

        if self.map[hashed_key] is None:
            self.map[hashed_key] = [package_data]
        else:
            # Update if package already exists
            for package in self.map[hashed_key]:
                if package[0] == package_id:
                    package[1:] = package_data[1:]  # Update details
                    return
            self.map[hashed_key].append(package_data)  # Handle collision

        # Resize if load factor exceeds 70%
        if sum(1 for slot in self.map if slot is not None) / self.size > 0.7:
            self._resize()

#Retrieves from the hash table
    def get(self, package_id):
        """Retrieves package data by package ID."""
        hashed_key = self._get_hash(package_id)
        if self.map[hashed_key] is not None:
            for package in self.map[hashed_key]:
                if package[0] == package_id:
                    return package
        return None

#Removes from the hash table
    def delete(self, package_id):
        """Removes package data from the hash table."""
        hashed_key = self._get_hash(package_id)
        if self.map[hashed_key] is not None:
            for i, package in enumerate(self.map[hashed_key]):
                if package[0] == package_id:
                    del self.map[hashed_key][i]  # Delete package
                    if not self.map[hashed_key]:  # If bucket is empty, set to None
                        self.map[hashed_key] = None
                    return True
        return False

#Prints the table
    def print_table(self):
        """Prints all stored packages in the hash table."""
        print("\nHash Table Contents:")
        for i, bucket in enumerate(self.map):
            if bucket is not None:
                print(f"Index {i}: {bucket}")

h = HashTable(10)
h.insert('1748','august','kankakee','60954','1lb','pending','delivered')

