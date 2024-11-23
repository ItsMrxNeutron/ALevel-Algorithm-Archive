

import unittest
from random import shuffle

from linear_search import linear_search
from binary_search import iterative_binary_search, recursive_binary_search

class TestSearch(unittest.TestCase):
    
    def setUp(self):
        temp = [i for i in range(999)]
        shuffle(temp)
        self.unsorted_case = temp
        self.sorted_case = [i for i in range(999)]
    
    
    def test_unsorted(self):
        self.assertIs(type(linear_search(self.unsorted_case, 6)), int)
        
    def test_sorted(self):
        self.assertEqual(linear_search(self.sorted_case, 6), 6)
        self.assertEqual(iterative_binary_search(self.sorted_case, 6), 6)
        self.assertEqual(recursive_binary_search(self.sorted_case, 6, 0, len(self.sorted_case)), 6)
    
if __name__ == "__main__":
    unittest.main()
        
