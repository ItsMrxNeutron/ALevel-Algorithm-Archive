

from typing import List


class Node:
    def __init__(self, data, next_ptr) -> None:
        self.data = data
        self.next_ptr = next_ptr


class Stack:
    def __init__(self) -> None:
        self.node_pool: List[Node] = []
        self.top = -1
        self.free = 0

        self.MAX_NODES = 10

    
    def push(self, node:Node) -> None:
        if self.free == -1:
            raise ValueError('Max nodes achieved.')
        self.node_pool.insert(0, node)
        self.top += 1
        if self.free < self.MAX_NODES:
            self.free += 1
        else:
            self.free = -1

    def pop(self) -> Node:
        if self.top == -1:
            raise IndexError
        return_elm = self.node_pool[self.top]
        del self.node_pool[self.top]            # .pop method can be used here, I am simply avoiding it.
        self.top -= 1
        if self.free == -1:
            self.free = self.top + 1
        else:
            self.free -= 1
        return return_elm

    def is_empty(self):
        return self.top == -1
    
    def is_full(self):
        return self.top == self.MAX_NODES

    # The part below here is unimportant to exam board but is a nice touch to the code

    def __len__(self):
        return self.free

s = Stack()
print(len(s))



