

from typing import TypeVar
from collections.abc import Collection

T = TypeVar('T')

def linear_search(input_array: Collection[T], expected: T) -> int:
    """Get index of item from a collection,
    Goes through each item sequentially and compares it to expected item.
    Terminates when item found, raises Exception when item isnt found.

    Time complexity:
        O(n), where n is the number of items in the input_array
        
    Space complexity:
        O(1)
    
    Args:
        input_array (Collection[T]): Any iterable collection type
        expected (T): item to retrieve

    Raises:
        Exception: Item not found

    Returns:
        int: integer position in the iterable collection sequence
    """
    
    for index, item in enumerate(input_array):
        if item == expected:
            return index
        
    raise Exception("Item not found!")
    
