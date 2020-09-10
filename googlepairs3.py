# O(n)
def findpairsum(arr, sum):
    myset = set([])
    for item in arr:
        if item in myset:
            return True
        myset.add(sum - item)
    return False


# print(findpairsum([6, 4, 1, 1, 1, 7], 7))


# Naive O(n^2):
def findpairsum2(arr, sum):
    i = 0
    j = i + 1
    length = len(arr)
    for item in arr:
        if i < length-1:
            for j in arr:
                if j < length:
                    if arr[i]+arr[j] == sum:
                        return True
                    print(arr[i]+arr[j])
                    i += 1
    return False


print(findpairsum2([6, 4, 1, 1, 1, 7], 7))
