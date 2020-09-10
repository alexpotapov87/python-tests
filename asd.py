#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#
# n = int(sys.argv[0])


def fizzBuzz(n):
    # Write your code here
    for i in range(1, n):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0 and i % 5 != 0:
            print('Fizz')
        elif i % 5 == 0 and i % 3 != 0:
            print('Buzz')
        elif i % 5 != 0 and i % 3 != 0:
            print(f'{i}')


# if __name__ == '__main__':
fizzBuzz(5)
