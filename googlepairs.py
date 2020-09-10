# // Given 2 arrays, create a function that let's a user
# know (true/false) whether these two arrays contain any common items
# //For Example:
array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'i']
# //should return false.
# //-----------
array3 = ['a', 'b', 'c', 'x']
array4 = ['a', 'y', 'x']
# //should return true.

# // 2 parameters - arrays - no size limit
# // return true or false

# 2 loops solution:


def pairs(arr1, arr2):
    for item1 in arr1:
        for item2 in arr2:
            if item1 == item2:
                print(f'True, the pair is {item1} and {item2}')
                return True
            else:
                False
    print('False')
    return False


print(pairs(array1, array4))
