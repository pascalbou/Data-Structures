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
        pass

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        pass

    def _sift_down(self, index):
        pass
