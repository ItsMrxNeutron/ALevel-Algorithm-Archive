
from typing import Generic, TypeVar
from linked_list import LinkedList

T = TypeVar('T')

"""
Queues are a bit more complicated,
If we naively implement it using python list with pop(0), we will end up with a O(n) time complexity.
If we use python list and keep appending + returning the front index without popping, we will lose memory (memory leak (bad ending))

Linked list can be used here, Or circular queues with modulo arithmetic
"""

class LinkedListQueue(Generic[T]):
    
    def __init__(self):
        self.length = 0
        self.linked_list = LinkedList()
        
    def enqueue(self, value: T):
        self.linked_list.add(value)
        self.length += 1
    
    def dequeue(self) -> T:
        self.length -= 1
        return self.linked_list.remove_head()
    
    def __len__(self):
        return self.length
    

class CircularQueue(Generic[T]):
    
    def __init__(self, maxsize = 5):
        self.maxsize = maxsize
        self._array = [None]*maxsize
        self.length = 0
        self.front = 0
        self.rear = 0
    
    def __len__(self):
        return self.length
    
    def is_full(self):
        return len(self) >= self.maxsize
    
    def is_empty(self):
        return len(self) == 0
    
    def enqueue(self, item: T):
        if self.is_full():
            raise Exception("Queue max size reached! (Segmentation fault jumpscare)")
        self._array[self.rear] = item
        self.length += 1
        self.rear = (self.rear+1) % self.maxsize
        
        
    def dequeue(self) -> T:
        if self.is_empty():
            raise Exception("Queue empty! (Segmentation fault jumpscare pt2)")
        
        self.length -= 1
        item = self._array[self.front]
        self.front = (self.front + 1) % self.maxsize
        return item


            