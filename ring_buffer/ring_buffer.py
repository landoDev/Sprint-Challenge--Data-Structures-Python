from queue import Queue

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity # 5
        self.storage = [] * capacity
        self.index = 0


    def append(self, item):
        # first attempt was close
        # see if storage is empty
        self.index + 1
        if not self.storage:
            self.storage.append(item)
        buffer = len(self.storage) % self.capacity 
        if buffer == 0:
            self.storage[0] = item
            self.storage.pop(0)
        else:
            self.storage.append(item)

    def get(self):
        # return storage
        return self.storage