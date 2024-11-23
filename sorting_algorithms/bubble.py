

from typing import TypeVar
from collections.abc import Collection

T = TypeVar('T')


def inplace_bubble_sort(input_array: Collection[T]) -> None:
    """Simple bubble sort,
    loops through list and 'bubbles' up the big elements over and over
    until list is sorted.
    Exits early when array is sorted.
    This is an 'Inplace' sort.
    
    
    Time complexity:
        Worst case: O(n^2), where n is the number of items in the input_array
        Best case: Ω(n), when the array is already sorted
        
    Space complexity:
        O(1), this is inplace

    Args:
        input_array (Collection[T]): array to sort
    """
    for i in range(len(input_array)):
        swapped = False
        for u in range(len(input_array)-i-1):
            if input_array[u] > input_array[u+1]:
                input_array[u], input_array[u+1] = input_array[u+1], input_array[u]
                swapped = True
        if not swapped:
            break
