class PriorityQueueBase:
    class Item:
        def __init__(self, k, v) -> None:
            self.key = k
            self.value = v

        def __lt__(self, other):
            return self.key < other.key
        
    def is_empty(self):
        return len(self) == 0

