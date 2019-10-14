# import sys
# sys.path.append('../doubly_linked_list')
# print(sys.path)

from doubly_linked_list import DoublyLinkedList

class Queue():
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # print(self.storage.__len__())
        self.storage.add_to_tail(value)
        self.size += 1
        # print(self.storage.__len__())

    def dequeue(self):
        if self.size >= 1:
            value = self.storage.remove_from_head()
            self.size -= 1
            return value

    def len(self):
        return self.storage.__len__()
