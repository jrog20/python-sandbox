# Write a function that returns the missing number in the array. Complexity of O(N) required.

# Example:
# nums = [0, 1, 2, 4, 5]
# missingNumber(nums) -> 3

############################################################
# Approach: 
# Create a new set with the array passed in.
# Iterate through the set, checking
# to see if each number for the length of the array +1
# exists in the set. If the number does not exist, 
# return the number
############################################################

def missing_number(nums):
    num_set = set(nums)
    n = len(nums) + 1
    for number in range(n):
        if number not in num_set:
            return number


nums = [0, 1, 2, 4, 5]
print(missing_number(nums))

nums = [1, 2, 3, 4]
print(missing_number(nums))
