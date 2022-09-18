


def bubble_sort(x:list) -> list:
    changes = 1          # flag set to true to jumpstart the first cycle
    optimise_counter = 0    # 1 cycle of bubble sort guarentees at least one sorted element on the end
    while changes:          # since 0 in python is falsy, if changes is bigger than 0 means that there could still be an unsorted element
        
        changes = 0
        for i in range(len(x)-1 - optimise_counter):
            # one cycle of the sort
            if x[i] > x[i+1]:
                temp = x[i+1]
                x[i+1] = x[i]
                x[i] = temp
                changes += 1
        optimise_counter += 1   # one extra element is sorted, we do not need to check it anymore
    return x


test_list = [9,5,1,5,2,2]

print(bubble_sort(test_list))





