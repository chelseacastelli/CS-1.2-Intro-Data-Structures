#!python
import time

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.count = 0
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Running time: 0(1) - constant because it's just returning a number"""
        return self.count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(1) - constant because it just keeps track of tail node and changes it"""
        new_node = Node(item)

        # If list is empty, make new_node the head and tail, return
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.count += 1
            return
        else:
            # Make current tail point to new_node and make new_node the tail
            curr_tail = self.tail
            curr_tail.next = new_node
            self.tail = new_node
            self.count += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Running time: O(1) - constant because it just keeps track of head node and changes it"""
        new_node = Node(item)

        # If list is empty, make new_node the head and return
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.count += 1
            return

        # Make current head the next node and new_node the head
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: O(1) - constant if node is head node
        Worst case running time: O(n) if entire list traversed """

        current_node = self.head

        while current_node:
            if quality(current_node.data):
                return current_node.data
            current_node = current_node.next
        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) if first item is deleted
        Worst case running time: O(n) if last item is deleted & list is traversed """

        current_node = self.head
        previous_node = None

        while current_node is not None:
            if item == current_node.data:
                # Deleting the head node
                if previous_node is None:
                    self.head = current_node.next

                    # Deleting the tail node
                    if current_node.next is None:
                        self.tail = previous_node

                elif current_node.next is None:
                    previous_node.next = None
                    self.tail = previous_node

                else:
                    previous_node.next = current_node.next

                self.count -= 1
                return None

            else:
                previous_node = current_node
                current_node = current_node.next

        raise ValueError('Item not found: {}'.format(item))

    def replace(self, old_item, new_item):
        """Replace the given item from this linked list with new_data, or raise ValueError.
        Best case running time: O(1) if first item is replaced
        Worst case running time: O(n) if last item is replaced & whole list is traversed """

        current_node = self.head

        while current_node:
            if current_node.data == old_item:
                current_node.data = new_item
                return

            current_node = current_node.next

        # Raise error if reach tail node and value old_data never found
        raise ValueError(f'Item not found: {old_item}')


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    # TEST APPEND
    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        start = time.perf_counter()
        ll.append(item)
        elapsed = time.perf_counter()
        print('list: {}'.format(ll))
        print('head: {}'.format(ll.head))
        print('tail: {}\n'.format(ll.tail))


    print('list: {}'.format(ll))
    print('length: {}'.format(ll.length()))
    print(f'Time spent appending new node: {elapsed - start}')

    # TEST REPLACE
    print('\nTesting replace:')

    for item in ['A', 'B', 'C']:
        print('replace({!r})'.format(item))
        start = time.perf_counter()
        ll.replace(item, 'J')
        elapsed = time.perf_counter()
        print('list: {}'.format(ll))
        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        break
    print(f'Time spent replacing a node: {elapsed - start}')

    # TEST PREPEND
    print('\nTesting prepend:')
    start = time.perf_counter()
    ll.prepend('A')
    elapsed = time.perf_counter()
    print('list: {}'.format(ll))
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print(f'Time spent prepending a new node: {elapsed - start}')

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            start = time.perf_counter()
            ll.delete(item)
            elapsed = time.perf_counter()
            print('list: {}'.format(ll))
            print('head: {}'.format(ll.head))
            print('tail: {}\n'.format(ll.tail))

        print('list: {}'.format(ll))
        print('length: {}'.format(ll.length()))
        print(f'Time spent deleting a node: {elapsed - start}')

if __name__ == '__main__':
    test_linked_list()



