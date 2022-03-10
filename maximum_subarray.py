import math

# 53. Maximum Subarray

# Given an integer array nums, find the contiguous subarray (containing at least one number) 
# which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Example 2:
# Input: nums = [1]
# Output: 1

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23

#########################################################################################
# Brute force solution
def maximum_subarray(nums):
    # initialize a variable to keep track of the best subarray
    # set it to negative infinity (not 0), because it is possible that the nums array only
    # has negative numbers
    max_subarray = -math.inf
    # nested for loop: iterate over the nums array, starting with one element
    # and for each element, loop through the array from that element, through to the end
    # of the array, each time adding the value and updating the current subarray.
    for i in range(len(nums)):
        cur_subarray = 0
        for j in range(i, len(nums)):
            cur_subarray += nums[j]
            # Continuously update max_subarray to contain the maximum out of current_subarray and itself.
            max_subarray = max(cur_subarray, max_subarray)
    # return max_subarray
    return max_subarray
#########################################################################################

nums = [-2,1,-3,4,-1,2,1,-5,4]
print('Expecting: 6')
print('Output:', maximum_subarray(nums))
print('')

nums = [1]
print('Expecting: 1')
print('Output:', maximum_subarray(nums))
print('')

nums = [5,4,-1,7,8]
print('Expecting: 23')
print('Output:', maximum_subarray(nums))
print('')