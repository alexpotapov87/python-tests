import pdb
arr = [1, 3, 5, 7, 8]


def minmax(arr):
    temp_min = []
    temp_min.extend(arr)
    temp_min.remove(max(temp_min))
    temp_max = []
    temp_max.extend(arr)
    temp_max.remove(min(temp_max))

    return print(sum(temp_min), sum(temp_max))

    # index = 0
    # for item in arr:
    #     if index == 0:
    #         temp_arr.append(item)
    #         index += 1
    #     if index >= 1:
    #         if
print(minmax(arr))
