# 238. Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to 
# the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

################################################################################################
# Since we cannot use the division operation, we can't just multiply all the elements together 
# and divide by nums[i]. We can, however, get the product of all the nums to the left of nums[i]
# and the product of all the nums to the right of nums[i], and multiply those together.
################################################################################################
def product_except_self(nums):
    # The length of the input array 
    length = len(nums)
    
    # The left and right arrays
    left, right, answer = [0]*length, [0]*length, [0]*length
    
    # left[i] contains the product of all the elements to the left
    # For the element at index '0', there are no elements to the left,
    # so the left[0] would be 1
    left[0] = 1
    for i in range(1, length):
        # left[i - 1] already contains the product of elements to the left of 'i - 1'
        # Multiplying it with nums[i - 1] would give the product of all elements 
        # to the left of index 'i'
        left[i] = nums[i - 1] * left[i - 1]
    
    # right[i] contains the product of all the elements to the right
    # For the element at index 'length - 1', there are no elements to the right, so the 
    # right[length - 1] would be 1
    right[length - 1] = 1
    for i in reversed(range(length - 1)):
        # right[i + 1] already contains the product of elements to the right of 'i + 1'
        # Multiplying it with nums[i + 1] would give the product of all elements 
        # to the right of index 'i'
        right[i] = nums[i + 1] * right[i + 1]
    
    # Constructing the answer array
    for i in range(length):
        # For the first element, right[i] would be product except self
        # For the last element of the array, product except self would be left[i]
        # Else, multiple product of all elements to the left and to the right
        answer[i] = left[i] * right[i]
    
    return answer
################################################################################################

################################################################################################
nums = [1,2,3,4]
print('Expecting [24,12,8,6]')
print(product_except_self(nums))

nums = [-1,1,0,-3,3]
print('Expecting [0,0,9,0,0]')
print(product_except_self(nums))