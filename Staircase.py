# Write a staircase of N height and N base
n = 7


def staircase(n):
    height = range(0, n)
    index = n - 1
    for item in height:
        if index > 1:
            print(' ' * index, end='')
            index -= 1
        elif index == 1:
            print(' ' * index, end='')
            index -= 1
        print('#' * (item + 1), end='')
        print()


staircase(n)
