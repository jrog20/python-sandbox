# 15. 3Sum

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# Example 2:
# Input: nums = []
# Output: []

# Example 3:
# Input: nums = [0]
# Output: []
##########################################################################
# Two Sum II uses the two pointers pattern and also has O(n) time complexity for a sorted array.
# We can use this approach for any array if we sort it first, which bumps the time complexity to O(nlogn).

# Time complexity: O(n^2) - We are calling two_sum n times from our main function, which is running n times.
# Space complexity: O(nlogn) - The sorting function

# def three_sum(nums):
#     # sort the nums array
#     nums.sort()
#     # initiate results array
#     results = []
#     # iterate through the array
#     for i in range(len(nums)):
#         # if the current value is greater than 0, break from the loop as the remaining values
#         # cannot sum to 0
#         if nums[i] > 0:
#             break
#         # if the current value is the same as the value before, skip it
#         elif nums[i] == nums[i - 1]:
#             break
#         # otherwise, call two_sum function on the current nums index
#         else:
#             two_sum(nums, i, results)
#     return results

# def two_sum(nums, i, results):
#     left = i + 1
#     right = len(nums) - 1
#     # with three pointers, find if i + left + right == 0
#     while left < right:
#         # if nums[i] + nums[left] + nums[right] < 0, increase left by 1
#         if nums[i] + nums[left] + nums[right] < 0:
#             left += 1
#         # if nums[i] + nums[left] + nums[right] > 0, decrease right by 1
#         elif nums[i] + nums[left] + nums[right] > 0:
#             right -= 1
#         # if the three == 0, we found a triplet. 
#         # 1. add it to the result array 
#         # 2. increase left by 1 (and skip if next value is the same as current value)
#         # 3. decrease right by 1
#         else:
#             results.append([nums[i], nums[left], nums[right]])
#             left += 1
#             while left == left - 1:
#                 left += 1
#             right -= 1

##########################################################################
# Hashset solution
# Time Complexity: O(n^2)-twoSum is O(n), and we call it n times.
# Sorting the array takes O(nlogn), so overall complexity is O(nlogn + n^2), so O(n^2)
# Space Complexity: O(n) for the hashset

# First, we sort the nums array
# Then interate through the array
# Again, if the first element is greater than 0, break because adding two positive numbers can
# not sum to zero.
# And skip duplicate numbers

# In the two_sum function:
# iterate through the array looking for a complement to nums[i] + nums[j]
# if the complement exists in the seen hashset, we found a triplet:
# add it to the results array and increment j while the next value is the same (avoid duplicates)
# add the current j element to the hash and continue iterating through the array

def three_sum(nums):
    # sort the nums array
    nums.sort()
    results = []
    for i in range(len(nums)):
        # if the current element value is greater than 0 (cannot be added to larger number to sum 0)
        # or it is the same element as the previous (duplicate), break
        if nums[i] > 0:
            break
        # otherwise, call the two_sum function on the current index
        if i == 0 or nums[i] != nums[i-1]:
            two_sum(nums, i, results)
    return results

def two_sum(nums, i, results):
    seen = set()
    j = i + 1
    while j < len(nums):
        complement = -(nums[i] + nums[j])
        # if we find a triplet, add it to the results array 
        if complement in seen:
            results.append([nums[i], nums[j], complement])
            # and increment j one to the right while we have not reached the end of the array,
            # and while it is not the same as the next value (skip duplicates)
            while j + 1 < len(nums) and nums[j] == nums[j+1]:
                j += 1
        # otherwise, add the current nums[i] value to the set and increment j one to the right
        seen.add(nums[j])
        j += 1

##########################################################################
nums = [-1,0,1,2,-1,-4]
print('Expecting: [[-1,1,0], [-1,2,-1]]')
print('This is the solution:', three_sum(nums))

nums = []
print('Expecting: []')
print('This is the solution:', three_sum(nums))

nums = [0]
print('Expecting: []')
print('This is the solution:', three_sum(nums))

##########################################################################
# One function
# def three_sum(nums):
#     # sort the nums array
#     nums.sort()
#     # initiate results array
#     results = []
#     # iterate through the array
#     for i in range(len(nums)):
#         # if the current value is greater than 0, break from the loop as the remaining values cannot sum to 0
#         # or if the current value is the same as the value before, skip it
#         if nums[i] > 0 or nums[i] == nums[i - 1]:
#             break
#         # otherwise, establish two pointers and search the array to see if there are two #s that will 
#         # combine with current index to equal 0
#         else:
#             left = i + 1
#             right = len(nums) - 1
#             # with three pointers, find if i + left + right == 0
#             while left < right:
#                 # if nums[i] + nums[left] + nums[right] < 0, increase left by 1
#                 if nums[i] + nums[left] + nums[right] < 0:
#                     left += 1
#                 # if nums[i] + nums[left] + nums[right] > 0, decrease right by 1
#                 elif nums[i] + nums[left] + nums[right] > 0:
#                     right -= 1
#                 # if the three == 0, we found a triplet. 
#                 # 1. add it to the result array 
#                 # 2. increase left by 1 (and skip if next value is the same as current value)
#                 # 3. decrease right by 1
#                 else:
#                     results.append([nums[i], nums[left], nums[right]])
#                     left += 1
#                     while left == left - 1:
#                         left += 1
#                     right -= 1
#     return results    