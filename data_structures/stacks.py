
from typing import Generic, TypeVar
from linked_list import DoublyLinkedList
T = TypeVar('T')

class LinkedListStack(Generic[T]):
    def __init__(self):
        self.length = 0
        self.doubly_linked_list = DoublyLinkedList()
        
    def pop(self) -> T:
        if len(self) == 0:
            raise Exception("Stack empty!")
        self.length -= 1
        return self.doubly_linked_list.remove_tail()
    
    def push(self, item: T):
        self.length += 1
        self.doubly_linked_list.add_back(item)

    def __len__(self):
        return len(self._array)
    

class ArrayStack(Generic[T]):
    
    def __init__(self):
        self._array = []
        
    def pop(self) -> T:
        if len(self) == 0:
            raise Exception("Stack empty!")
        return self._array.pop()
    
    def push(self, item: T):
        self._array.append(item)
    
    def __len__(self):
        return len(self._array)
    
    


