#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'unboundedKnapsack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def unboundedKnapsack(k, arr):
    max_sum = [0] * (k + 1)

    for i in range(1, k + 1):
        for num in arr:
            if num <= i:
                max_sum[i] = max(max_sum[i], max_sum[i - num] + num)

    return max_sum[k]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for _ in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])

        arr = list(map(int, input().rstrip().split()))

        result = unboundedKnapsack(k, arr)

        fptr.write(str(result) + '\n')

    fptr.close()
