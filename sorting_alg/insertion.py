

test_list = [9,5,1,5,2,2]

def insertion_sort(_list):
    for next_val in range(1, len(_list)):
        val = _list[next_val]                       # current value held to be sorted in current cycle
        curr = next_val -1                          # makes current points to the element before the value holding
        while curr >= 0 and _list[curr] > val:      # check if: current is not out of list index, value is smaller than the one before
            _list[curr+1] = _list[curr]             # makes the next element in the list the one before
            curr -= 1
        _list[curr+1] = val                         # if the held value is bigger than the one before, sets the current index to the held value (this is the sorted place)
    return _list


print(insertion_sort(test_list))