



def b_search(x:list, wanted) -> int:
    """Make sure x is sorted"""
    top = len(x)-1
    bottom = 0
    mid = top//2
    while True:
        if x[mid] == wanted:
            # found
            return mid
        elif x[mid] < wanted:
            # not found, value was in higher section
            bottom = mid +1
            mid = (top+bottom)//2
        else:
            # not found, value was in lower section
            top = mid -1
            mid = (top+bottom)//2
            

test_list = [35, 68, 7, 61, 63, 7, 50, 26, 67, 57, 82, 35, 25, 40, 66, 44, 49, 50, 3, 61]
test_list.sort()
print(test_list)

print(b_search(test_list, 3))


