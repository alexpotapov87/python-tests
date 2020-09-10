a = (5, 6, 7)
b = (3, 6, 10)

c = (17, 28, 30)
d = (31, 22, 11)

e = (22, 99, 88, 77, 90, 29)
f = (22, 99, 87, 99, 92, 30)


def compareTriplets(a, b):
    list1 = []
    list2 = []

    index = 0
    for item in a:
        if item > b[index]:
            list1.append(item)
            index += 1
        elif b[index] > item:
            list2.append(b[index])
            index += 1
        elif item == b[index]:
            index += 1
            continue
    return print(len(list1), len(list2))


compareTriplets(a, b)
