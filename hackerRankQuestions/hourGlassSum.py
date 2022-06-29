#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def hourglassSum(arr):
    # Write your code here
    all_sums = []
    for startV in range((len(arr[0])//2)+1):
        for startH in range((len(arr[0])//2)+1):
            all_sums.append(sum(arr[startV][startH:startH+3]) +
                            sum(arr[startV+2][startH:startH+3]) + arr[startV+1][startH+1])
    return max(all_sums)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
