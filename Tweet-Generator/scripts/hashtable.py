#!python

from linkedlist import LinkedList
import time

class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]
        self.KV_entries = 0

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Running time: O(n) because it traverses all buckets and then each buckets contents"""
        # Collect all keys in each bucket
        all_keys = []

        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)

        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Running time: O(n) because it traverses all buckets and then each buckets contents"""
        all_values = []

        # Loop through all buckets
        for bucket in self.buckets:
            # Collect all values in each bucket
            for key, value in bucket.items():
                all_values.append(value)

        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Running time: O(n) because it traverses all buckets and then each buckets contents"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []

        for bucket in self.buckets:
            all_items.extend(bucket.items())

        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Running time: O(1) constant because it's just returning a value"""
        return self.KV_entries

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Running time: O(l) gets index of bucket and then checks if key is in list"""
        # Find bucket where given key belongs
        bucket = self.buckets[self._bucket_index(key)]
        item = bucket.find(lambda item: item[0] == key)

        # Check if key-value entry exists in bucket
        if item is not None:
            return True

        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Running time: O(l) because it jumps straight to the bucket and then finds key in list """
        # Find bucket where given key belongs
        bucket = self.buckets[self._bucket_index(key)]
        item = bucket.find(lambda item: item[0] == key)

        # Check if key-value entry exists in bucket
        if item is not None:
            # If found, return value associated with given key
            return item[1]

        raise KeyError(f'Key not found: {key}')

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Running time: O(l) because it jumps straight to the bucket and then traverses list to check if the value already exists ( O(n) ), otherwise, it appends """
        # Find bucket where given key belongs
        bucket = self.buckets[self._bucket_index(key)]
        item = bucket.find(lambda item: item[0] == key)

        # Check if key-value entry exists in bucket
        if item is not None:
            # If found, update value associated with given key
            bucket.replace(item, (key, value))

        # Otherwise, insert given key-value entry into bucket
        else:
            bucket.append((key, value))
            self.KV_entries += 1

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        Running time: O(l) because it because it jumps straight to the bucket and then traverses list to find value (if it exists)"""
        # Find bucket where given key belongs
        bucket = self.buckets[self._bucket_index(key)]
        item = bucket.find(lambda item: item[0] == key)

        # Check if key-value entry exists in bucket
        if item is not None:
            # If found, delete entry associated with given key
            bucket.delete(item)
            self.KV_entries -= 1
            return

        # Otherwise, raise error to tell user delete failed
        raise KeyError(f'Key not found: {key}')

def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        start = time.perf_counter()
        ht.set(key, value)
        elapsed = time.perf_counter()
        print('hash table: {}'.format(ht))
    print(f'Time spent inserting or updating given key: {elapsed - start}\n')

    print('\nTesting values:')
    start = time.perf_counter()
    print(ht.values())
    elapsed = time.perf_counter()
    print(f'Time spent returning all values in hash table: {elapsed - start}\n')

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        start = time.perf_counter()
        value = ht.get(key)
        elapsed = time.perf_counter()
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))
    print(f'Time spent returning value of given key: {elapsed - start}\n')

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            start = time.perf_counter()
            ht.delete(key)
            elapsed = time.perf_counter()
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))
        print(f'Time spent deleting given key: {elapsed - start}\n')

if __name__ == '__main__':
    test_hash_table()
