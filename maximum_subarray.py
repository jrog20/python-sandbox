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

def maximum_subarray(nums)



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