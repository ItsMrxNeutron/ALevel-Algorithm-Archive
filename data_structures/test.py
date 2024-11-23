

import unittest

from linked_list import DoublyLinkedList, LinkedList
from stacks import ArrayStack
from queues import LinkedListQueue, CircularQueue


class TestDSA(unittest.TestCase):
    
    def test_linked_list(self):
        linked_list = LinkedList()
        linked_list.add(1)
        linked_list.add(2)
        linked_list.add(3)
        
        expected = [1,2,3]
        result = [i for i in linked_list]
        self.assertListEqual(result, expected)
        
    def test_doubly_linked_list(self):
        doubly_linked_list = DoublyLinkedList()
        doubly_linked_list.add_back(1)
        doubly_linked_list.add_back(2)
        doubly_linked_list.add_back(3)
        
        expected = [1,2,3]
        result = [i for i in doubly_linked_list]
        self.assertListEqual(result, expected)
        
        expected = [3,2,1]
        result = [i for i in doubly_linked_list._test_reverse_iter()]
        self.assertListEqual(result, expected)
        
    def test_stack(self):
        stack = ArrayStack()
        
        stack.push(1)
        stack.push(2)
        stack.push(3)
        
        expected = [3,2,1]
        result = [stack.pop() for _ in range(len(stack))]
        self.assertListEqual(result, expected)
        
    def test_linked_queue(self):
        linked_queue = LinkedListQueue()
        linked_queue.enqueue(1)
        linked_queue.enqueue(2)
        linked_queue.enqueue(3)
        
        expected = [1,2,3]
        result = [linked_queue.dequeue() for _ in range(len(linked_queue))]
        self.assertListEqual(result, expected)
        
    def test_circular_queue(self):
        linked_queue = CircularQueue(3)
        linked_queue.enqueue(1)
        linked_queue.enqueue(2)
        linked_queue.enqueue(3)
        
        expected = [1,2,3]
        result = [linked_queue.dequeue() for _ in range(len(linked_queue))]
        self.assertListEqual(result, expected)
        
        
    
if __name__ == "__main__":
    unittest.main()
        
