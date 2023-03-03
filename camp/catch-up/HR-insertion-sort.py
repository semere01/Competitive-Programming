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
    val=arr[n-1]
    i1=len(arr)-1
    i2=len(arr)-2
    for i in range(len(arr)):
        if val<arr[i2] and i2>=0:
            arr[i1]=arr[i2]
            i1-=1
            i2-=1
            print(*arr)
        else:
            arr[i1]=val
            print(*arr)
            break
            
    
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)