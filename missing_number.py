# Write a function that returns the missing number in the list. Complexity of O(N) required.

# Example:
# nums = [0, 1, 2, 4, 5]
# missingNumber(nums) -> 3

############################################################
# Approach: 
# Iterate through the list, checking to see if each number for the length of the list +1 exists in the list. 
# If the number does not exist, return the number
############################################################

def missing_number(nums):
    n = len(nums) + 1
    for number in range(n):
        if number not in nums:
            return number

nums = [0, 1, 2, 4, 5]
print('Expecting 3')
print('Output =', missing_number(nums))
print('')

nums = [1, 2, 3, 4]
print('Expecting 0')
print('Output =', missing_number(nums))
