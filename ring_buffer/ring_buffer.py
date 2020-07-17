from queue import Queue

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity # 5
        self.storage = [None] * capacity
        self.index = 0


    def append(self, item):
        # first attempt was close
        self.storage[self.index] = item
        self.index += 1
        if self.index == self.capacity:
            self.index = 0

    def get(self):
        # return storage
        item = [item for item in self.storage if item is not None]
        return item