# 153. Find Minimum in Rotated Sorted Array

# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 

# For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times
# [0,1,2,4,5,6,7] if it was rotated 7 times

# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array 
# [a[n-1], a[0], a[1], a[2], ..., a[n-2]]

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

# Example 1:
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times

# Example 2:
# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times

# Example 3:
# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times

################################################################################################
# Brute force solution: Iterate through the array and find the smallest element
# Time complexity: O(n)
# Space complexity: O(1)

# def find_min(nums):
#     smallest = nums[0]
#     for i in range(1, len(nums)):
#         smallest = min(smallest, nums[i])
#     return smallest

################################################################################################
# Binary Search solution

# Because this is not just a sorted array, but rather a sorted array that has been
# rotated, in order to find the smallest element, we need to find the inflection point
# i.e. when the element to the right is no longer greater than the element to its left.

# 1. Find the mid point of the array
# 2. If the mid element is greater than the first element of the array, we need to 
# move to the right
# 3. If the mid element is less than the first element of the array, we need to 
# move to the left
# 4. We stop searching when we find the inflection point:
    # a. nums[mid] > nums[mid+1] => mid+1 is the smallest
    # b. nums[mid-1] > nums[mid] => mid is the smallest

# Time Complexity: O(log N)
# Space Complexity: O(1)

def find_min(nums):
    # create left and right pointer variables
    left = 0
    right = len(nums) - 1

    # if the list only has one element, return that element -OR-
    # if the last element is greater than the first element, there is no rotation,
    # so the first element is the smallest
    if len(nums) == 1 or nums[right] > nums[0]:
        return nums[0]

    # Binary search
    while right >= left:
        # Find the mid element
        mid = left + (right - left) // 2

        # if the mid element is greater than its next element then mid+1 element is the smallest
        # This point would be the point of change. From higher to lower value.
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]

        # if the mid element is less than the previous element then mid element is the smallest
        if nums[mid - 1] > nums[mid]:
            return nums[mid]

        # if the mid element is greater than the first element, the smallest value 
        # is still to the right as we are still dealing with elements greater than nums[0]
        if nums[mid] > nums[0]:
            left = mid + 1

        # if nums[0] is greater than the mid element then the smallest value is to the left
        else:
            right = mid - 1

################################################################################################
nums = [3,4,5,1,2]
print('Expecting: 1')
print(find_min(nums))

nums = [4,5,6,7,0,1,2]
print('Expecting: 0')
print(find_min(nums))

nums = [11,13,15,17]
print('Expecting: 11')
print(find_min(nums))
