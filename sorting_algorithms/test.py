

import unittest
from random import shuffle

from bubble import inplace_bubble_sort
from insertion import inplace_insertion_sort

def setup_shuffle():
    temp = [i for i in range(999)]
    shuffle(temp)
    unsorted_list = temp
    sorted_list = [i for i in range(999)]
    return unsorted_list, sorted_list

class TestSort(unittest.TestCase):
    
    def test_single_bubblesort(self):
        unsorted_list, sorted_list = setup_shuffle()
        inplace_bubble_sort(unsorted_list)
        self.assertEqual(unsorted_list, sorted_list)
    
    def test_single_insertion(self):
        unsorted_list, sorted_list = setup_shuffle()
        inplace_insertion_sort(unsorted_list)
        self.assertEqual(unsorted_list, sorted_list)
        
    def test_multi_bubblesort(self):
        for _ in range(10):
            unsorted_list, sorted_list = setup_shuffle()
            inplace_bubble_sort(unsorted_list)
            self.assertEqual(unsorted_list, sorted_list)
    
    def test_multi_insertion(self):
        for _ in range(10):
            unsorted_list, sorted_list = setup_shuffle()
            inplace_insertion_sort(unsorted_list)
            self.assertEqual(unsorted_list, sorted_list)
            
if __name__ == "__main__":
    unittest.main()
        
