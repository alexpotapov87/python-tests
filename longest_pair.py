import pdb
array1 = [1, 1, 2, 3, 2, 1, 2, 2]
array2 = [0, 1, 1, 2, 2, 3, 3]
array3 = [1, 1, 2, 2, 3, 4, 5]
array4 = [1, 1, 1, 1, 1, 2, 2, 3, 4, 5]
array5 = [0, 2, 1, 2, 1, 2, 1, 2, 4, 5, 1, 2, 1, 2]
array6 = [1, 1, 1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 5, 6, 6, 6, 9, 9, 9, 0]

biggest_number = []


def longest(testarray):
    index = 0
    new_array = []
    # pdb.set_trace()
    for item in testarray:

        if 0 < index < len(testarray)-1:
            prev_item = testarray[(index-1)]
            next_item = testarray[index+1]
            prepre_item = testarray[index-2]
            print(
                f'index is {index}, item is {item}, next_item is {next_item}, prev_item is {prev_item}')
            print(
                f'new array is {new_array}, biggest_number is {biggest_number}')
            print(f'i-[i+1] = {abs(item - next_item)}')
            print(f'i-[i-1] = {abs(item - prev_item)}')
            print(f'n-p = {abs(next_item - prev_item)}')

            if abs(item - next_item) <= 1 and abs(item - prev_item) <= 1 and abs(prev_item - next_item) <= 1:
                new_array.append(item)
                index += 1
            else:
                # non_empty = list(filter(None, new_array))
                biggest_number.append(new_array)
                new_array = [prev_item]
                index += 1
        elif index == 0:
            new_array.append(item)
            index += 1
        elif index == len(testarray):
            if abs(item - prev_item) <= 1 and abs(prepre_item - item) <= 1:
                new_array.append(item)
                biggest_number.append(new_array)
            # else:
            #     biggest_number.append(new_array)
            #     new_array = []

    if len(new_array) > 1:
        biggest_number.append(new_array)
    list2 = [x for x in biggest_number if x != []]
    print(
        f'new array is {new_array}, list2 is {list2}, biggest_number is {biggest_number}')

    return len(list2)
    # return len(list(filter(None, biggest_number)))


def max_number(*arrays):
    maximum = max(longest(*arrays))
    return maximum


print(longest(array1))
