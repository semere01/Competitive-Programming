#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    currentIndex = n-1
    currentIndexVal = arr[n-1];
    for i in range (n-2, -1, -1):
        if arr[i] > currentIndexVal:
            arr[i+1] = arr[i]
        else:
            arr[i+1] = currentIndexVal 
        for x in arr:
            print(f"{x} ",  end='')
            # print(x, " ", end='');
        print()

insertionSort1(5, [2,4,6,8,3]);
# if __name__ == '__main__':
#     n = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))

#     insertionSort1(n, arr)
