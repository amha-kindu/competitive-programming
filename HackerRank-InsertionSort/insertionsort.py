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
    # Write your code here
    for i in range(n):
        val = arr[n-i-1]
        j = n-i-2
        for j in range(n-i-2, -2, -1):
            if j > -1 and val < arr[j]:
                arr[j+1]=arr[j]
                print(*arr)
            else:
                break
        arr[j+1]=val
    print(*arr)
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
