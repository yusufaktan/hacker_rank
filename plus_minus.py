#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos = []
    neg = []
    zero = []

    for i in arr:
        if (i < 0):
            neg.append(i)
        elif (i > 0):
            pos.append(i)
        else:
            zero.append(i)

    print ("{:.6f}".format(len(pos)/len(arr)))
    print ((round((len(neg)/ len(arr)), 6)))
    print (round((len(zero)/ len(arr)), 6))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
