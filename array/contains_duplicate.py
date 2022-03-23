# 217. Contains Duplicate

# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

################################################################################################
# Put the nums array into a set. If the set is shorter than the the nums array, there is a duplicate
# so return True, otherwise return False.
def contains_duplicate(nums):
    num_set = set(nums)
    return True if len(num_set) < len(nums) else False

################################################################################################
nums = [1,2,3,1]
print('Expecting True')
print(contains_duplicate(nums))

nums = [1,2,3,4]
print('Expecting False')
print(contains_duplicate(nums))

nums = [1,1,1,3,3,4,3,2,4,2]
print('Expecting True')
print(contains_duplicate(nums))