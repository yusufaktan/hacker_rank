#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1],arr[j]
    
    min = 0
    max = 0
    sum = 0
    for y in arr:
        sum += y
        
    min = sum - arr[len(arr)-1]
    max = sum - arr[0]
    print (min, max)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
