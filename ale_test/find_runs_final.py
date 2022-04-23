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
# Time complexity: O(n)
# Space complexity: O(n)

def solution(values, run_length):
    solution_array = []
    # Need to add +1 to range in order to get any potential runs at the end of array
    # i.e. I originally stopped the loop one index short
    for i in range(len(values)-run_length+1):
        counter = 0
        increase_array = []
        decrease_array = []
        temp_index = i
        while counter < run_length-1:
            if values[temp_index] - values[temp_index+1] == -1:
                increase_array.append(i)
                if len(increase_array) == run_length-1:
                    solution_array.append(increase_array[0])
                counter += 1
                temp_index += 1
            elif values[temp_index] - values[temp_index+1] == 1:
                decrease_array.append(i)
                counter += 1
                temp_index += 1
                if len(decrease_array) == run_length-1:
                    solution_array.append(decrease_array[0])
            else:
                counter += 1
                temp_index += 1
    return solution_array
##########################################################################

values = [1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7, 8, 7]
run_length = 3 
print('Expecting: [0, 4, 6, 7]')
print('This is the solution:', solution(values, run_length))

# Original submitted code didn't work for a run starting at the last possible index
values = [1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7, 8, 9]
run_length = 3 
print('Expecting: [0, 4, 6, 7, 10]')
print('This is the solution:', solution(values, run_length))

values = [1, 7, 3, 5, 10, 2]
run_length = 3 
print('Expecting: []')
print('This is the solution:', solution(values, run_length))

values = [1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7, 8, 9]
run_length = 4
print('Expecting: [6]')
print('This is the solution:', solution(values, run_length))

values = [1, 2, 3, 4]
run_length = 5
print('Expecting: []')
print('This is the solution:', solution(values, run_length))

values = [1, 2, 3, 4, 5]
run_length = 5
print('Expecting: [0]')
print('This is the solution:', solution(values, run_length))

values = [-1, -2, -3, -4, -5]
run_length = 5
print('Expecting: [0]')
print('This is the solution:', solution(values, run_length))