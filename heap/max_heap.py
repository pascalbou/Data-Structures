import math

class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        # print(f'appending... {self.storage}')

        for i in range(len(self.storage), 1, -1):
            # compare only with parent node
            j = math.floor(i/2)
            if self.storage[i-1] > self.storage[j-1]:
                self.storage[i-1], self.storage[j-1] = self.storage[j-1], self.storage[i-1]
            # print(f'swapping... {self.storage}')
        
    def delete(self):
        result = self.storage.pop(0)
        
        for i in range(len(self.storage), 1, -1):
            j = math.floor(i/2)
            if self.storage[i-1] > self.storage[j-1]:
                self.storage[i-1], self.storage[j-1] = self.storage[j-1], self.storage[i-1]

        return result

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        print(self)
        parent_index = math.floor(index+1/2) - 1
        if self.storage[index] > self.storage[parent_index]:
            self.storage[index], self.storage[parent_index] =  self.storage[parent_index], self.storage[index]
        print(self)

    def _sift_down(self, index):
        left_child_index = index * 2
        right_child_index = index * 2 + 1
        if self.storage[left_child_index] > self.storage[right_child_index]:
            if self.storage[left_child_index] > self.storage[index] :
                self.storage[left_child_index], self.storage[index] = self.storage[index], self.storage[left_child_index]
        else:
            if self.storage[right_child_index] > self.storage[index] :
                self.storage[right_child_index], self.storage[index] = self.storage[index], self.storage[right_child_index]            