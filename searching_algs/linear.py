


def linear_search(x:list, wanted) -> int:
    for index in range(len(x)):
        if x[index] == wanted:
            return index
    return None                 # wanted element not in list


test_list = [35, 68, 7, 61, 63, 7, 50, 26, 67, 57, 82, 35, 25, 40, 66, 44, 49, 50, 3, 61]
print(linear_search(test_list, 57))


