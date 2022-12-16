#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    space = n-1
    symbol = 1
    for i in range(0, n):
        print (space * " " + symbol * "#")
        space -=1
        symbol += 1
    

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
