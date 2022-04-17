# 33. Search in Rotated Sorted Array

# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown 
# pivot index k (1 <= k < nums.length) such that the resulting array is 
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, 
# return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# Example 3:
# Input: nums = [1], target = 0
# Output: -1

################################################################################################
# You must write an algorithm with O(log n) runtime complexity.
# This requirement hints at using a binary search
# 1. Find a rotation_index, the index of the smallest element in the array.
# 2. rotation_index splits the array in two. Compare nums[0] and target to find which half we 
# to search for target.
# 3. Perform a binary search in the identified half of the array.

# def search(nums, target):
#     # 1. Find a rotation_index, the index of the smallest element in the array.
#     def find_rotate_index(left, right):
#         # If the value of the first index is less than the value of the last index,
#         # the array is not rotated, so we return the first index
#         if nums[left] < nums[right]:
#             return 0
        
#         while left < right:
#             # pick the element in the middle as the pivot
#             pivot = (left + right) // 2

#             # if the element to the right of pivot is smaller than pivot, it is the rotation_index,
#             # return the index to the right of pivot
#             if nums[pivot] > nums[pivot + 1]:
#                 return pivot + 1

#             # if the element to the right of pivot is not smaller than pivot, it is not
#             # the smallest element, so continue search on the right side
#             else:
#                 # if the value of pivot index is less than the value of left index,
#                 # move the right index to left of pivot (i.e. we know the rotate_index is on the left side)
#                 if nums[pivot] < nums[left]:
#                     right = pivot - 1 
#                 # otherwise, move the left index one to the right of pivot (i.e. we know the rotate_index
#                 # is on the right side)
#                 else:
#                     left = pivot + 1

#     def search_index(left, right):
#         # binary search
#         while left <= right:
#             pivot = (left + right) // 2
#             if nums[pivot] == target:
#                 return pivot
#             else:
#                 if target < nums[pivot]:
#                     right = pivot - 1
#                 else: 
#                     left = pivot + 1
#             return -1

#     if len(nums) == 1:
#         return 0 if nums[0] == target else -1
    
#     rotate_index = find_rotate_index(0, len(nums) - 1)

#     # if the target is the smallest element
#     if nums[rotate_index] == target:
#         return rotate_index
#     # if array is not rotated, search the entire array
#     if rotate_index == 0:
#         return search_index(0, len(nums) -1)
#     if target < nums[0]:
#         # search the right side
#         return search_index(rotate_index, len(nums) -1)
#     # search the left side
#     return search_index(0, rotate_index)
################################################################################################
# One-pass Binary Search - two pointers

# Time complexity: O(logN)
# Space complexity: O(1) 

# instead of going throgh the input array in two passes, we could go through it in one pass 
# with some conditional checks to better narrow down the scope of the search

# Keep two pionters: start and end. At each iteration, cut the search scope in half by moving
# either the start or end pointer to the middle (mid) of the previous search scope.

def search(nums, target):
    # initiate the pointers
    start = 0
    end = len(nums) -1
    # binary search
    while start <= end:
        mid = (start + end) // 2
        # if value of mid index == target, we found the target
        if nums[mid] == target:
            return mid
        # if pivot element is larger than the first element in nums array, the first half
        # of the array is non-rotated
        elif nums[mid] > nums[start]:
            # if target is located in the non-rotated subarray (left side), move the end pointer 
            # one index to the left
            if target >= nums[start] and target <= nums[mid]:
                end = mid - 1
            # otherwise move the search scope to the right half of the array
            else:
                start = mid + 1
        # if we are here, the pivot element is smaller than the fist element of the array, i.e.
        # the rotation_index is between index 0 and mid.
        else:
            # if target is located in the non-rotated subarray (right side), set the start pointer 
            # to mid + 1 and search the right side of the array
            if target >= nums[mid] and target <= nums[end]:
                start = mid + 1
            # otherwise the target is located in the left subarray, so we move the end pointer to mid - 1
            else:
                end = mid - 1

    # if we get here, the target is not found, so we return -1
    return -1

################################################################################################
nums = [4,5,6,7,0,1,2]
target = 0
print('Expecting 4')
print(search(nums, target))

nums = [4,5,6,7,0,1,2]
target = 3
print('Expecting -1')
print(search(nums, target))

nums = [1]
target = 0
print('Expecting -1')
print(search(nums, target))
