

from typing import List


class Node:
    def __init__(self, data, next_ptr) -> None:
        self.data = data
        self.next = next_ptr            # the focus is in Queues, I wont bother with pointers here

class Queue:
    def __init__(self) -> None:
        """FIFO style list"""
        self.node_pool: List[Node] = []
        self.top = -1
        self.free = 0
        self.MAX_NODES = 10

    def enqueue(self, node:Node):
        if self.free == -1:
            raise ValueError('Max nodes achieved.')
        self.node_pool.append(node)
        self.free += 1
        self.top += 1
        if self.free >= self.MAX_NODES:
            self.free = -1
        
    def dequeue(self):
        if self.top == -1:
            raise IndexError
        return_val = self.node_pool[0]
        del self.node_pool[0]           # pop can be used here, I am avoiding the use of it
        self.top -= 1
        self.free -= 1
        return return_val

    def is_empty(self):
        return self.top == -1
    
    def is_full(self):
        return self.free == -1

    # The part below here is unimportant to exam board but is a nice touch to the code

    def __len__(self):
        return self.free




