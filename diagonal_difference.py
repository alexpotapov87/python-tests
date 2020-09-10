# from array import *

my_ar = [[11, 2, 4, 4, 4], [4, 5, 6, 8, 9], [10, 8, -12, 0, 12],
         [12, 6, -1, 11, 2], [2, 7, 12, 44, 12]]
# n = len(ar)


def diagonalDifference(arr):
    list_1st = []
    list_2nd = []
    i_to = 0
    i_from = len(arr)-1
    for array in arr:
        list_1st.append(array[i_to])
        i_to += 1
        list_2nd.append(array[i_from])
        i_from -= 1
    fst_sum = sum(list_1st)
    sec_sum = sum(list_2nd)
    return abs(fst_sum - sec_sum)


print(diagonalDifference(my_ar))
