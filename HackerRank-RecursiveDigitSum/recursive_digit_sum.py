#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
def getSuperDigit(p):
    if len(p)<2:
        return int(p)
    sum_ = 0
    for digit in p:
        sum_ += int(digit) 
    return getSuperDigit(str(sum_))
        
def superDigit(n, k):
    super_n = getSuperDigit(n)
    return getSuperDigit(str(super_n)*k)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
