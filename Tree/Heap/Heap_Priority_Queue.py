from queue import Empty
from Priority_queue_base import PriorityQueueBase
import heapq

class Heap_PriorityQueue(PriorityQueueBase):
    def parent(self, j):
        return (j-1)//2
    
    def left(self,j):
        return 2*j + 1 # position of parent is j
    
    def right(self, j):
        return 2*j + 2
    
    def has_left(self, j):
        return self.left(j) < len(self.data)
    
    def has_right(self, j):
        return self.right(j) < len(self.data)
    
    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
    
    def upheap(self, j):
        parent = self.parent(j)
        if j > 0 and self.data[j] < self.data[parent]:
            self.swap(j, parent)
            self.upheap(parent)     # Recur at postion of parent
    
    def downHeap(self, j):
        if self.has_left(j):
            left = self.left(j)
            small_child = left
            if self.has_right(j):
                right = self.right(j)
                if self.data[right] < self.data[left]:
                    small_child = right
            if self.data[small_child] < self.data[j]:
                self.swap(j, small_child)       # dealing with indexs
                self.downHeap(small_child)   # Recur at position of small child 

    # -------------------Public behaviours-----------------------------

    def __init__(self, contents = ()) -> None:
        
        self.data = [self.Item(k,v) for k,v in contents ] # empty by default

        if len(self.data) > 1:
            self._heapify()
    
    def _heapify(self):
        start = self.parent(len(self) -1 ) # start at the parent of the last leaf
        for j in range(start, -1, -1): # going to and including the root
            self.downHeap(j)
    
    def __len__(self):
        return len(self.data)
    
    def add(self, key, value):
        self.data.append(self.Item(key, value))
        self.upheap(len(self.data) - 1)
    
    def min(self):
        # return but do not remove tuple(k,v)

        if self.is_empty():
            raise Empty("Prior queue is empty")
        item = self.data[0]
        return (item.key, item.value)
    
    def remove_min(self):
        if self.is_empty():
            raise Empty("Prior queue is empty")
        
        self.swap(0, len(self.data) -1) # move the minimum item at the end
        item = self.data.pop()
        self.downHeap(0)
        return (item.key, item.value)

r = (5, "five")
h = Heap_PriorityQueue()
h.add(5,'five')
h.add(10,'Ten')
h.add(15,'fifteen')
h.add(17,'seventeen')
h.add(20,'twenty')
h.add(22,'twentytwo')

print(h.data[0].key)