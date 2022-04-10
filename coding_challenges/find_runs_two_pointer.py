# Write a python3 function:

# def solution(A, Y)

# that accepts as arguments a list of integers and an integer run length. 
# It must find in that list all runs of run length consecutive numbers that 
# increase or decrease by 1. It should return the list indices of the first element of each run. 
# If there are no consecutive runs it should return an empty list.

# Feel free to rename the arguments in the function signature, 
# e.g.: def solution(values, run_length):

# Example: 
# values=[1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7, 8, 7]
# run_length=3 
# returns [0, 4, 6, 7]

# Additionally, please give comments on the code's runtime and space complexity. 
##########################################################################
# Two Pointer solution:

# Initiate two pointers: 
# pointer_one will point to the beginning of the possible subarray
# pointer_two will point to the end of the possible subarray
# Iterate through the possible subarray
# Start with last element in the subarray, and compare it to the previous element
# If it increases or decreases by 1, add the pointer_one index to the temp_array
# If this temp array gets to the same length as the run_length, we add pointer_one index
# to the solution_array

# Time complexity: O(n)
# Space complexity: O(1)

def solution(values, run_length):
    solution_array = []

    # return empty array if run length is greater than array length
    if len(values) < run_length:
        return solution_array

    pointer_one = 0
    pointer_two = run_length
    temp_array = []

    while pointer_one <= pointer_two - 1 and pointer_two < len(values):
        print('beginning of loop pointer two is = ', pointer_two)
        if values[pointer_two - 1] - values[pointer_two - 2] == 1 or values[pointer_two - 1] - values[pointer_two - 2] == -1 or values[pointer_two] - values[pointer_one] == 1:
            temp_array.append(pointer_one)
            print('pointer_one value = ', pointer_one)
            print('pointer_two value = ', pointer_two)
            print('temp array = ', temp_array)
            # If we get here, the subarray matches our requirements and we
            # add the index of pointer_one to the solution array
            if len(temp_array) == run_length:
                solution_array.append(pointer_one)
                print('solution array = ', solution_array)
                # reset the temp_array
                temp_array = []
                # increment pointer_one by one
                pointer_one += 1
                # pointer_two needs to be run length from pointer_one
                pointer_two = pointer_one + run_length
            else:
                # If the last element and 2nd to last element differ by 1,
                # move pointer_two one index to left
                pointer_two -= 1
        else:
            # If we get here, we don't have a current run, so we need to move pointer_one one index to the right
            # and we need to reset pointer_two to be run length from pointer_one
            pointer_one += 1
            pointer_two = pointer_one + run_length 
    return solution_array
    
##########################################################################

values = [1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7, 8, 7]
run_length = 3 
print('Expecting: [0, 4, 6, 7]')
print('This is the solution:', solution(values, run_length))