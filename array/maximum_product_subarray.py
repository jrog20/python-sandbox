# 152. Maximum Product Subarray

# Given an integer array nums, find a contiguous non-empty subarray within the 
# array that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# A subarray is a contiguous subsequence of the array.

# Example 1:
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Example 2:
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

#########################################################################################
# Iterate through the array. As we iterate, keep track of largest product.
# If next element makes product less than previous product, start current_product over
# with the current index.

# Time complexity: 
# Space complexity: 

def max_product(nums):
    return nums
#########################################################################################

#########################################################################################
nums = [2,3,-2,4]
print('Expecting: 6')
print('Output:', max_product(nums))

nums = [-2,0,-1]
print('Expecting: 0')
print('Output:', max_product(nums))