
from __future__ import annotations
from typing import Generic, TypeVar, Iterator

T = TypeVar('T')

class LinkedListIterator:
    
    def __init__(self, current: LinkedListNode[T]) -> Iterator[T]:
        self.current = current
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        value = self.current.value
        self.current = self.current.next
        return value

class LinkedListNode(Generic[T]):
    
    def __init__(self, value: T):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head: LinkedListNode[T] | None = None
        self.tail: LinkedListNode[T] | None = None
    
    def __iter__(self) -> LinkedListIterator[T]:
        return LinkedListIterator(self.head)

    def add(self, value):
        if self.head is None:
            self.head = LinkedListNode(value)
            self.tail = self.head
        else:
            new_node = LinkedListNode(value)
            self.tail.next = new_node
            self.tail = new_node
            
    def remove_head(self) -> T:
        temp = self.head
        self.head = self.head.next
        return temp.value

    def remove_tail(self) -> T:
        
        # unfortunate O(n) due to lack of reverse pointer
        temp_return = self.tail
        # get the node before the tail
        temp = self.head
        for _ in range(len(self)-2):
            temp = temp.next
        self.tail = temp
        return temp_return.value


class ReversedDoublyLinkedListIterator:
    
    def __init__(self, current: DoublyLinkedListNode[T]) -> Iterator[T]:
        self.current = current
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        value = self.current.value
        self.current = self.current.previous
        return value


class DoublyLinkedListNode(Generic[T]):
    def __init__(self, value: T):
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkedList:
    # didnt inherit as this fails Liskov's substitution lol
    
    def __init__(self):
        self.head: DoublyLinkedListNode[T] | None = None
        self.tail: DoublyLinkedListNode[T] | None = None
    
    def __iter__(self) -> LinkedListIterator[T]:
        return LinkedListIterator(self.head)

    def _test_reverse_iter(self) -> ReversedDoublyLinkedListIterator[T]:
        return ReversedDoublyLinkedListIterator(self.tail)

    def add_front(self, value):
        if self.head is None:
            self.head = DoublyLinkedListNode(value)
            self.tail = self.head
        else:
            new_node = DoublyLinkedListNode(value)
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    def add_back(self, value):
        if self.head is None:
            self.head = DoublyLinkedListNode(value)
            self.tail = self.head
        else:
            new_node = DoublyLinkedListNode(value)
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    def remove_head(self) -> T:
        temp = self.head
        self.head = self.head.next
        self.head.previous = None
        return temp.value

    def remove_tail(self) -> T:
        temp = self.tail
        self.tail = self.tail.previous
        return temp.value


