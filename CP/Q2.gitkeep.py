#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    a = {
        1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
        11: "eleven", 12: "twelve"
    }
    
    b = [
        "o' clock", "one", "two", "three", "four", "five", "six", "seven",
        "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
        "quarter", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"
    ]

    if m == 0:
        return a[h] + " " + b[0]
    elif m == 15:
        return "quarter past " + a[h]
    elif m == 30:
        return "half past " + a[h]
    elif m == 45:
        next_hour = h + 1 if h < 12 else 1
        return "quarter to " + a[next_hour]
    elif m < 30:
        if m <= 20:
            return b[m] + (" minute" if m == 1 else " minutes") + " past " + a[h]
        else:
            return "twenty " + b[m - 20] + " minutes past " + a[h]
    else:
        k = 60 - m
        nr = h + 1 if h < 12 else 1
        if k <= 20:
            return b[k] + (" minute" if k == 1 else " minutes") + " to " + a[nr]
        else:
            return "twenty " + b[k - 20] + " minutes to " + a[nr]


        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()

