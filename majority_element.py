# 169. Majority Element

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

#########################################################################################
# Brute force
# Time complexity: O(n^2)
# The brute force algorithm contains two nested for loops that each run for nn iterations, 
# adding up to quadratic time complexity.

# Space complexity: O(1)
# The brute force solution does not allocate additional space proportional to the input size.

# def majority_element(nums):
#     majority_count = len(nums)//2
#     for num in nums:
#         count = sum(1 for elem in nums if elem == num)
#         if count > majority_count:
#             return num

#########################################################################################
# Hashmap solution
# Time complexity: O(n)
# Space complexity: O(n)

# import collections
# from collections import Counter

# def majority_element(nums):
#     counts = collections.Counter(nums)
#     return max(counts.keys(), key=counts.get)

#########################################################################################
# Sort solution
# Time complexity: O(n log n)
# Space complexity: O(n)

def majority_element(nums):
    nums.sort()
    return nums[len(nums)//2]

#########################################################################################

nums = [3,2,3]
print('Expecting: 3')
print('Output:', majority_element(nums))
print('')

nums = [2,2,1,1,1,2,2]
print('Expecting: 2')
print('Output:', majority_element(nums))
print('')