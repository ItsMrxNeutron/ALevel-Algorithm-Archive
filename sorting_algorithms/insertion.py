
from typing import TypeVar
from collections.abc import Collection

T = TypeVar('T')

def inplace_insertion_sort(input_array: Collection[T]) -> None:
    """Inplace insertion sort,
    Algorithm splits array into 2 parts, sorted and unsorted
    
    It first allocates the first index to sorted, the rest is unsorted
    Loops over the unsorted part then shifts the values bigger than the key to make space.

    Time complexity:
        Worst case: O(n^2), where n is the number of items in the input_array
        Best case: Ω(n), when the array is already sorted
        
    Space complexity:
        O(1), this is inplace

    Args:
        input_array (Collection[T]): array to sort
    """
    for i in range(1, len(input_array)):
        key = input_array[i]
        j = i-1
        while j >= 0 and input_array[j] > key:
            input_array[j+1] = input_array[j]
            j = j-1
        input_array[j+1] = key