# import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack

import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(
    __file__)), '../queue_and_stack'))
from dll_queue import Queue
from dll_stack import Stack

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if  self.value > value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

        if  self.value < value:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # print(self.value)
        # print(target)

        if self.value == target:
            return True

        if self.value > target and self.left:
            return self.left.contains(target)

        if self.value < target and self.right:
            return self.right.contains(target)

        return False           

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if not node:
            return

        if self.left:
            self.left.in_order_print(self.left)

        print(self.value)    

        if self.right:
            self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)

        while queue.len():
            current_node = queue.dequeue()
            print(current_node.value)

            if current_node.left:
                queue.enqueue(current_node.left)

            if current_node.right:
                queue.enqueue(current_node.right)  

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)

        while stack.len():
            current_node = stack.pop()
            print(current_node.value)            

            if current_node.left:
                stack.push(current_node.left)

            if current_node.right:
                stack.push(current_node.right)                  

           

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        if not node:
            return

        print(self.value)    

        if self.left:
            self.left.pre_order_dft(self.left)

        if self.right:
            self.right.pre_order_dft(self.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if not node:
            return

        if self.left:
            self.left.post_order_dft(self.left)

        if self.right:
            self.right.post_order_dft(self.right)

        print(self.value)    

