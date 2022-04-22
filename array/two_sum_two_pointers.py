# 167. Two Sum II - Input Array Is Sorted

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
# find two numbers such that they add up to a specific target number. Let these two numbers 
# be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer 
# array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. 
# You may not use the same element twice.

# Your solution must use only constant extra space.

# Example 1:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

# Example 2:
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

# Example 3:
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

##########################################################################
# Two Pointer solution:

# Because the arry is sorted, we can use two indices, initially pointing to the first 
# and the last element, respectively. Compare the sum of these two elements with target. 
# If the sum is equal to target, we found the exactly only solution. 
# If it is less than target, we increase the smaller index by one. 
# If it is greater than target, we decrease the larger index by one. 
# Move the indices and repeat the comparison until the solution is found.

# Time complexity: O(n)
# Space complexity: O(1)

def two_sum(nums, target):
    low = 0
    high = len(nums) - 1
    while low < high:
        sum = nums[low] + nums[high]
        if sum == target:
            return [low + 1, high + 1 ]
        elif sum < target:
            low += 1
        else: 
            high -= 1
    return [-1, -1]

##########################################################################
nums = [2,7,11,15]
target = 9 
print('Expecting: [1,2]')
print(two_sum(nums, target))

nums = nums = [2,3,4]
target = 6
print('Expecting: [1,3]')
print(two_sum(nums, target))

nums = [-1,0]
target = -1
print('Expecting: [1,2]')
print(two_sum(nums, target))