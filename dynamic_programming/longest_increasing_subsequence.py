# Longest Increasing Subsequence

# Given an integer array nums, return the length of the longest strictly increasing subsequence.

# A subsequence is a sequence that can be derived from an array by deleting some or no elements 
# without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence 
# of the array [0,3,1,6,2,2,7].

# Example 1:
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

# Example 2:
# Input: nums = [0,1,0,3,2,3]
# Output: 4

# Example 3:
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
# #######################################################################################
# Dynamic Programming solution:
# 1. Initialize an array dp with length nums.length and all elements equal to 1. dp[i] represents 
# the length of the longest increasing subsequence that ends with the element at index i.

# 2. Iterate from i = 1 to i = nums.length - 1. At each iteration, use a second for loop to 
# iterate from j = 0 to j = i - 1 (all the elements before i). For each element before i, 
# check if that element is smaller than nums[i]. If so, set dp[i] = max(dp[i], dp[j] + 1).

# 3. Return the max value from dp.

# Time Complexity: O(n^2)
# Space Complexity: 0(n)

# def length_of_LIS(nums):
#     dp = [1] * len(nums)
#     for i in range(1, len(nums)):
#         for j in range(i):
#             if nums[i] > nums[j]:
#                 dp[i] = max(dp[i], dp[j] + 1)
#     return max(dp)
# #######################################################################################
# Dynamic Programming - Intelligently build the subsequence:
# 1. Initialize an array sub which contains the first element of nums.

# 2. Iterate through the input, starting from the second element. For each element num:
#     - If num is greater than any element in sub, then add num to sub.
#     - Otherwise, iterate through sub and find the first element that is 
#     greater than or equal to num. Replace that element with num.

# 3. Return the length of sub.

# Time Complexity: O(n^2)
# Space Complexity: 0(n)

def length_of_LIS(nums):
    sub = [nums[0]]
    for num in nums[1:]:
        if num > sub[-1]:
            sub.append(num)
        else:
            # iterate through sub and find the first element that is 
            # greater than or equal to num.
            i = 0
            while num > sub[i]:
                i += 1
            # Replace that element with num.
            sub[i] = num
    return len(sub)
# #######################################################################################
nums = [10,9,2,5,3,7,101,18]
print('Expecting: 4')
print('Output:', length_of_LIS(nums))

nums = [0,1,0,3,2,3]
print('Expecting: 4')
print('Output:', length_of_LIS(nums))

nums = [7,7,7,7,7,7,7]
print('Expecting: 1')
print('Output:', length_of_LIS(nums))