# import sys
# sys.path.append('../doubly_linked_list')
# from doubly_linked_list import DoublyLinkedList

import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(
    __file__)), '../doubly_linked_list'))
from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        if self.size >= 1:
            value = self.storage.remove_from_head()
            self.size -= 1
            return value

    def len(self):
        return self.storage.__len__()
