class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity # 5
        self.storage = []

    def append(self, item):
        # see if storage is at capacity (use modulo to check)
        # if it is, overwrite the eldest value
        # else append the item
        self.storage.append(item)

    def get(self):
        # return storage
        return self.storage