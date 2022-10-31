
from random import randint


NULL_PTR = -1
class BinaryTree:
    def __init__(self) -> None:
        self.root = None
        self.curr = None
        self.free = 1
        self.memory = []
    
    def add_node(self, data):
        if self.root is None:
            self.root = 0
            self.memory.append(Node(data)) # root node
        # leaf nodes below
        self.curr = self.root
        while True:
            if data <= self.memory[self.curr].data:
                if self.memory[self.curr].left_ptr == NULL_PTR:
                    # check if end of tree
                    self.memory[self.curr].left_ptr = self.free
                    self.memory.append(Node(data))
                    self.free += 1
                    return
                # go left
                self.curr = self.memory[self.curr].left_ptr
            else:
                if self.memory[self.curr].right_ptr == NULL_PTR:
                    # check if end of tree
                    self.memory[self.curr].right_ptr = self.free
                    self.memory.append(Node(data))
                    self.free += 1
                    return
                self.curr = self.memory[self.curr].right_ptr

        
            


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left_ptr = -1
        self.right_ptr = -1


test_tree = BinaryTree()
[test_tree.add_node(randint(0, 30)) for i in range(10)]

print(test_tree.memory)
