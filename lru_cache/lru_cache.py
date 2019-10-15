from doubly_linked_list import DoublyLinkedList
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(
    __file__)), '../doubly_linked_list'))


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.number_nodes = 0
        self.order = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def search_node_by_key(self, key):
        current = self.order.head
        node = None
        while current:
            if current.value == key:
                node = current
        return node

    def get(self, key):
        if self.storage[key]:
            value = self.storage[key]
            node = self.search_node_by_key(key)
            self.order.move_to_end(node)
            return value
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        if self.number_nodes >= 10:
            key_to_remove = self.order.head.value
            self.order.remove_from_head()
            self.storage.pop(key_to_remove, None)

        if key in self.storage.keys():
            self.storage[key] = value
            node = self.search_node_by_key(key)
            self.order.move_to_end(node)
        else:
            self.storage[key] = value
            self.order.add_to_tail(key)
