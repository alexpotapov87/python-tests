arr = [1, 1, 0, -1, -1]


def PlusMinus(arr):
    number = len(arr)
    positive_list = []
    zero_list = []
    negative_list = []
    for item in arr:
        if item > 0:
            positive_list.append(item)
        elif item == 0:
            zero_list.append(item)
        elif item < 0:
            negative_list.append(item)
    pos_sum = float(len(positive_list) / number)
    zero_sum = float(len(zero_list) / number)
    neg_sum = float(len(negative_list) / number)
    return print(format(pos_sum, '.6f')), print(format(neg_sum, '.6f')), print(format(zero_sum, '.6f')),


print(PlusMinus(arr))
