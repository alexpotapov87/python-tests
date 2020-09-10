import pdb
array1 = [1, 1, 2, 3, 2, 1, 2, 2]
array2 = [0, 1, 1, 2, 2, 3, 3]
array3 = [1, 1, 2, 2, 3, 4, 5]
array4 = [1, 1, 1, 1, 1, 2, 2, 3, 4, 5]
array5 = [0, 2, 1, 2, 1, 2, 1, 2, 4, 5, 1, 2, 1, 2]
array6 = [1, 1, 1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 5, 6, 6, 6, 9, 9, 9, 0]


def pairs(arr):
    list_m = []
    index = 0
    next_item = index+1
    pdb.set_trace()
    set_m = set()
    temp_list = []

    for item in arr:
        if index < (len(arr) - 2):
            if abs(item - arr[next_item]) <= 1:
                if index >= 1:
                    for value in set_m:
                        if abs(value-item) <= 1:
                            temp_list.append(item)
                            if item not in set_m:
                                set_m.add(item)
                else:
                    set_m.add(item)
                    temp_list.append(item)

        index += 1
        list_m.append(item)


pairs(array1)
