from queue import Queue

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity # 5
        self.storage = []
        self.head = 0

    def append(self, item):
        # first attempt was close
        # see if storage is empty
        # if not self.storage:
        #     self.storage.enqueue(item.value)
        if not self.storage:
            self.storage.append(item)

        elif len(self.storage) > 0:
            buffer = len(self.storage) % self.capacity
            if buffer == 0:
                self.storage[0] = item
                self.storage.pop()
            else:
                self.storage.append(item)

    def get(self):
        # return storage
        return self.storage