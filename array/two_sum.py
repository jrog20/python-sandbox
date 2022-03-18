# 1. Two Sum

# Given an array of integers nums and an integer target, return indices 
# of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

##########################################################################
# Brute force solution:
# Loop through the nums array and find if there is an element that is target - 
# the current num

# Time complexity: O(n^2)
# Space complexity: O(1)

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i +1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]
    
##########################################################################

##########################################################################
nums = [2,7,11,15]
target = 9 
print('Expecting: [0,1]')
print(two_sum(nums, target))

nums = nums = [3,2,4]
target = 6
print('Expecting: [1,2]')
print(two_sum(nums, target))

nums = [3,3]
target = 6
print('Expecting: [0,1]')
print(two_sum(nums, target))