import pdb
mylist = [(2, 5), (3, 8), (5, 4), (7, 9), (10, 12), (12, 8), (13, 5), (17, 8)]
number = 6
super_power = []


def power():

    # pdb.set_trace()
    for i in mylist:
        for x, y in mylist:
            if y >= number:
                super_power.append(x)
            else:
                pass
        return super_power


power()
print(super_power)
