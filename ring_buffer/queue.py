class Queue:
    def __init__(self):
        self.size = 0
        self.storage = [] 
        # self.storage = LinkedList() 
    
    def __len__(self):
        return self.size

    def enqueue(self, value): 
        self.size += 1
        return self.storage.append(value)
        # self.storage.add_to_tail(value)

        

    def dequeue(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.pop(0)