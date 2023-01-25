#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    
    swap_cnt = 0
    for i in range(len(a)):
        for j in range(len(a)-1):
            # Swap adjacent elements if they are in decreasing order
            if (a[j] > a[j + 1]):
                a[j], a[j+1] = a[j+1], a[j]
                swap_cnt += 1
    print(f'Array is sorted in {swap_cnt} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')
        

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
