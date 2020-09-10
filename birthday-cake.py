n = 4
array = [3, 2, 1, 3]


def birthdayCakeCandles(ar):
    max_num = max(ar)
    candles_to_blow = ar.count(max_num)
    return print(candles_to_blow)


birthdayCakeCandles(array)
