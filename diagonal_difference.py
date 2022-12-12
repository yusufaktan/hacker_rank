#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    leftDiagonal = 0
    rightDiagonal = 0
    length=len(arr)-1

    for i in range(0, len(arr)):
        leftDiagonal += arr[i][i]
        rightDiagonal += arr[i][length]
        length -= 1

    return (abs(leftDiagonal-rightDiagonal))


    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
