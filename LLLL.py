import pdb
array1 = [1, 1, 2, 3, 2, 1, 2, 2]
# array2 = [0, 1, 1, 2, 2, 3, 3]
# array3 = [1, 1, 2, 2, 3, 4, 5]
# array4 = [2, 2, 1, 3, 4, 1, 1, 3, 3, 4, 5, 6]
# array5 = [1, 1, 3, 3]

# or abs(x - arr[i+1]) == 1
# or abs(arr[i+1] - arr[i+2]) == 1
# or abs(x - arr[i+2]) == 1


def longestSubarray(arr):
    # pdb.set_trace()
    new_arr = []
    y = range(len(arr))
    max_i = (len(arr) - 2)
    i = 0
    for x in arr:
        if i < max_i:
            if abs(x - arr[i+1]) <= 1 and abs(x - arr[i+2]) <= 1:
                print(f'{x} added to new_arr')
                print(f'the x is {x}')
                print(f'the current index is {i}')
                new_arr.append(x)
            i += 1
        print(new_arr)
    print(len(new_arr))


def compare_arrays(*args):
    return max()


if __name__ == '__main__':
    longestSubarray(array1)
    # longestSubarray(array2)
    # longestSubarray(array3)
    # longestSubarray(array4)
    # longestSubarray(array5)
    # compare_arrays(array1, array2, array3, array4, array5)
