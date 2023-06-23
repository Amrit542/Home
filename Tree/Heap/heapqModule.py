import heapq
from Priority_queue_base import PriorityQueueBase


class heap_amrit(PriorityQueueBase):
    def __init__(self) -> None:
        self.data = []
    
    def parent(self, j):
        return (j-1)//2
    
    def __len__(self):
        return len(self.data)
    
    def display(self):
        print(self.data)
        return
    
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
    
# -----------------add to heap---------------------------------

    def add(self, val):
        self.data.append(val)
        # print(len(self))
        if len(self) > 1:
            last = len(self) -1
            self._upheap(last)

    def _upheap(self, j):
        parent = self.parent(j)

        if self.data[parent] > self.data[j]:
            self.swap(parent, j)
            self._upheap(parent)
    
# -------------------------remove from heap--------------------------

    def remove_min(self):
        if len(self) ==  0: 
            raise Empty("heap is empty")
        
        self.swap(0, len(self)-1)
        item = self.data.pop()
        self._downheap(0)
        return item
    
    def _downheap(self, j):
        if self.has_left(j):
            left = self.left(j)
            small = left
            if self.has_right(j):
                right = self.right(j)
                if self.data[right] < self.data[left]:
                    small = right
                if self.data[small] < self.data[j]:
                    self.swap(j, small)
                    self._downheap(small)



    
h = heap_amrit()
h.add(5)
h.add(13)
h.add(14)
h.add(24)
h.add(26)
h.add(31)


h.display()

output = []
print(len(h))
while len(h) != 0:
    v = h.remove_min()
    output.append(v)
    print(len(h))
print(output)