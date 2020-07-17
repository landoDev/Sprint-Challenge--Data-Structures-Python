class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if node is None:
            return
        # if tail, set tail to head
        if node.next_node is None:
            self.head = node
            self.head.next_node = prev
        else:
            self.reverse_list(node.next_node, node)
            node.next_node = prev
        # current = node
        # prev_node = prev
        # while current is not None:
        #     next_node = current.get_next() # intitialize next head
        #     current.set_next(prev_node) # set current node to point to the prev node
        #     prev_node = current # set the last node to the current node
        #     current = next_node # set the current node as the next node
        #     # back to top
        # self.head = prev_node # set the head to the prev node
        
