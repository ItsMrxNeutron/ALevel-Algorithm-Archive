
from typing import TypeVar
from collections.abc import Collection

T = TypeVar('T')

def iterative_binary_search(input_array: Collection[T], expected: T) -> int:
    """Iterative binary search algorithm,
    This algorithm splits the array into smaller and smaller parts as it loops.
    It first picks a middle point and compares it to the expected:
        - If bigger than mid point, look in the right part of array
        - If smaller, look in the left part of the array
    
    it does this over and over until there is no more items to search or has found the item.
    
    Time complexity:
        O(log(n)), where n is the number of items in the input_array
        
    Space complexity:
        O(1)
        
    Args:
        input_array (Collection[T]): Input array to search
        expected (T): Expected item to look for

    Raises:
        Exception: Item not found

    Returns:
        int: integer position within the given array
    """
    low = 0
    high = len(input_array)
    while low < high-1:
        mid = (low+high)//2
        if expected >= input_array[mid]:
            low = mid
        else:
            high = mid
    if input_array[low] == expected:
        return low
    
    raise Exception("Item not found!")
    

def recursive_binary_search(array: Collection[T], expected: T, low: int, high: int):
    """Recursive binary search,
    Same thing as iterative but uses recursion to implement.
    Has worse efficiency than iterative and worse space complexity but code is easier to read/more concise.
    
    Time complexity:
        O(log(n)), where n is the number of items in the array
        
    Space complexity:
        O(log(n)), where n is the number of items in the array
            With recursion, Python has to create new stack frames for each call to the function
            which makes it take more space than the iterative method.

    Args:
        array (Collection[T]): input array to search
        expected (T): expected item to look for
        low (int): index marker to low
        high (int): index marker to high

    Returns:
        int: integer position within the given array
    """
    mid = (low+high)//2
    if array[mid] == expected:
        return mid
    
    if expected > array[mid]:
        # expected is in the bigger side
        return recursive_binary_search(array, expected, mid+1, high)
    else:
        # expected is in the smaller side
        return recursive_binary_search(array, expected, low, mid-1)

if __name__ == "__main__":
    test = [i for i in range(10)]
    
    print(recursive_binary_search(test, 6, 0, len(test)))