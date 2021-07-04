"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        hash_value = self.calculate_hash_value(string)
        if self.table[hash_value]:
            print("Value already present: ", self.table[hash_value])
        else:
            self.table[hash_value] = string
            print("String stored successfully")

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        if string in self.table:
            return self.table.index(string)
        else:
            return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        hash_val = ord(string[0])*100 + ord(string[1])
        return hash_val


hash_table = HashTable()
print(hash_table.calculate_hash_value('UDACITY'))
print(hash_table.lookup('UDACITY'))
hash_table.store('UDACIOUS')
print(hash_table.lookup('UDACIOUS'))








