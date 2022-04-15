##########################################################################
# Counting Triplets
# FINAL SUBMISSION

#!/bin/python3

import math
import os
import random
import re
import sys

##########################################################################
# Error: Currently only accounting for runs, not all possible triplets in array
def getTripletCount(a, d):
    solution = 0
    for i in range(len(a)-2):
        if (a[i] + a[i+1] + a[i+2]) % d == 0:
            solution += 1
    return solution
##########################################################################

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    d = int(input().strip())

    result = getTripletCount(a, d)

    fptr.write(str(result) + '\n')

    fptr.close()

##########################################################################
a = [2, 3, 1, 6]
d = 3
print('Expecting: 2')
print('My solution:', getTripletCount(a, d))
