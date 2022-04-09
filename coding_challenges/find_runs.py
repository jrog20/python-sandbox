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
# brute force solution:
# nested for loop
# Iterate through array
# Start with first element, and compare next two elements
# If they all increase or decrease by 1, add the [i] element index to the final
# solution variable
# Continue this loop for each element

# Time complexity: O(n^2)
# Space complexity: O(1)

def solution(values, run_length):
    # initiate solution array
    solution_array = []
    for i in range(len(values)):
        temp_array = []
        for j in range(i, run_length-1):
            if values[j] - values[j+1] == 1 or values[j] - values[j+1] == -1:
                temp_array.append(values[j])

                if len(temp_array) == run_length:
                    solution_array.append(i)
                    
    return solution_array
    
##########################################################################

values=[1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7, 8, 7]
run_length=3 
print('Expecting: [0, 4, 6, 7]')
print('This is the solution:', solution(values, run_length))