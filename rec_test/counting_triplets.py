##########################################################################
# Counting Triplets
# FINAL SUBMISSION

#!/bin/python3
# import math
# import os
# import random
# import re
# import sys

##########################################################################
# This function was submitted to the coding challenge
# Error: Currently only accounting for runs, not all possible triplets in array
# def getTripletCount(a, d):
#     solution = 0
#     for i in range(len(a)-2):
#         if (a[i] + a[i+1] + a[i+2]) % d == 0:
#             solution += 1
#     return solution

##########################################################################
# Write a function that takes in an array of numbers (a) and return the 
# number of triplets (three values in array) that can be added together
# and divided evenly by the second argument (d).

# Time complexity: O(n^2)
# Space complexity: O(1)

def get_triplet_count(a, d):
    solution = 0
    # iterate through the entire array
    for i in range(len(a)):
        # if the array is less than length of three, break and return solution
        if len(a) < 3:
            break
        left = i + 1
        right = len(a) - 1
        # for every index, loop through the array to find all other possible triplets
        while left < right:
            # if we find a triplet, increase solution by 1
            # and increase left by one and decrease right by 1
            if (a[i] + a[left] + a[right]) % d == 0:
                solution += 1
                left += 1
            # otherwise, keep incrementing left pointer one index to the left
            else:
                left += 1

    return solution

##########################################################################
# 2+3+1 and 2+1+6 are evenly divisible by 3
a = [2, 3, 1, 6]
d = 3
print('Expecting: 2')
print('My solution:', get_triplet_count(a, d))

a = [2, 3, 1, 6]
d = 5
print('Expecting: 1')
print('My solution:', get_triplet_count(a, d))

##########################################################################
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     a_count = int(input().strip())
#     a = []
#     for _ in range(a_count):
#         a_item = int(input().strip())
#         a.append(a_item)
#     d = int(input().strip())
#     result = getTripletCount(a, d)
#     fptr.write(str(result) + '\n')
#     fptr.close()
##########################################################################