
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
# Space complexity: O(1)?

def get_triplet_count(a, d):
    # sort the nums array
    a.sort()
    solution = 0
    for i in range(len(a)):
        # if the array is less than length of three, break and return solution
        if len(a) < 3:
            break
        # otherwise, call the doubles function on the current index
        doubles(a, i, solution)
    return solution

def doubles(a, i, solution):
    seen = set()
    j = i + 1
    while j < len(a):
        # (a[i] + a[j] + complement) % d == 0
        complement = -(a[i] + a[j]) % d == 0
        # if we find a triplet, increase the solution count
        if complement in seen:
            solution += 1
            # and increment j one to the right while we have not reached the end of the array,
            # and while it is not the same as the next value (skip duplicates)
            while j + 1 < len(a) and a[j] == a[j+1]:
                j += 1
        # otherwise, add the current nums[i] value to the set and increment j one to the right
        seen.add(a[j])
        j += 1
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
