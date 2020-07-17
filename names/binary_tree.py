class BSTNode:
    def __init__(self, value):
        self.value = str(value)
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Case 1: value is less than self.value
        if value < self.value:
            # if no left child, 
            if self.left is None:
                self.left = BSTNode(value)
            #   insert here
            # else
            else: 
                # repeat the process
                self.left.insert(value)
                # self.left.insert(value)  
        # Case 2: value is greater than OR EQUAl self.value
        elif value >= self.value:
        # EQUAL IS NOT WRITTEN IN STONE but tests here assume duplicates go to the right
            if self.right is None:
                # repeat inverse of left
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):

        if self.value == target:
            return True
   
        if target < self.value:

            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):

        if self.right is None:
            return self.value
        return self.right.get_max()               


    def for_each(self, fn):

        fn(self.value)

        if self.left:
            self.left.for_each(fn)

        if self.right:
            self.right.for_each(fn)


    def __repr__(self):
        return f"{self.value}"

    def in_order_print(self, node):

        if self is None:
            return 
            
        

        if self.left is not None:
            self.left.in_order_print(self.left)
        
     
        print(node.value)

        if self.right is not None:
            self.right.in_order_print(self.right)





    # def bft_print(self, node):
 
    #     from queue import Queue

    #     q = Queue()
 
    #     q.enqueue(self)

    #     while q.size > 0:

    #         node = q.dequeue()

    #         print(node.value)
  
    #         if self.left is not None:
    #             next_node = self.left
    #             q.enqueue(next_node)

    #         if self.right is not None:
    #             next_node = self.right
    #             q.enqueue(next_node)


   
    
    # def dft_print(self, node):
    #     from stack import Stack

    #     ref_stack = Stack()
 
    #     ref_stack.push(self)

    #     while ref_stack.size > 0:
    #         this_node = ref_stack.pop()

    #         print(this_node)

    #         if self.right is not None:
    #             ref_stack.push(self.right.value)
    #         if self.left is not None:
    #             ref_stack.push(self.left.value)