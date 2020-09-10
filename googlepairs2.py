import pdb
array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'i', 'x']
array3 = ['a', 'b', 'c', 'x']
array4 = ['a', 'y', 'x']
array5 = ['m', 'n', 'd', 'o']
array6 = ['k', 'l', 'h']

# hash solution O(a+b):


def pairs2(arr1, arr2):
    # 1. Loop through 1st arr and create object (hash) where
    # properpties == items in the 1st arr
    map = {}
    for index1 in arr1:
        ifexist1 = map.get(index1)
        if ifexist1 is None:
            map[index1] = True
    print(map)
    # 2. loop through 2nd array and check if item in
    # 2nd arr exist on created obj(hash)
    # pdb.set_trace()

    for index2 in arr2:
        ifexist2 = map.get(index2)
        if ifexist2 is not None:
            print(f'{ifexist2}')
            return True
    print('False')
    return False


pairs2(array5, array6)
