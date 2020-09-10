import pdb


array1 = [10, 20, 20, 10, 10, 30, 50, 10, 20]
n = 7

# Complete the sockMerchant function below.


def sockMerchant(n, ar):
    i = 0
    j = i + 1
    temp_ar = ar
    max_i = len(temp_ar)
    pairs = []
    # pdb.set_trace()
    for item1 in temp_ar:
        if i < max_i-1:
            if j < max_i-1:
                for item2 in temp_ar:
                    if i < j and ar[i] == ar[j]:
                        print(f'i is {i} j is {j} arI {ar[i]} arJ {ar[j]}')
                        print(f'temp_ar is {temp_ar}')
                        print(f'pairs is {pairs}')

                        pairs.append(item1)
                        temp_ar.pop(i)
                        temp_ar.pop(j)
                    i += 1
                    j = i + 1

    return len(pairs)


print(sockMerchant(n, array1))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input())

#     ar = list(map(int, input().rstrip().split()))

#     result = sockMerchant(n, ar)

#     fptr.write(str(result) + '\n')

#     fptr.close()
