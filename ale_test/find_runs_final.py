# Write a python3 function:
# that accepts as arguments a list of integers and an integer run length. 
# It must find in that list all runs of run length consecutive numbers that 
# increase or decrease by 1. It should return the list indices of the first element of each run. 
# If there are no consecutive runs it should return an empty list.

# Example: 
# values=[1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7, 8, 7]
# run_length=3 
# returns [0, 4, 6, 7]

# Additionally, please give comments on the code's runtime and space complexity. 
##########################################################################
# Time complexity: O(n^2)
# Space complexity: O(n)

def solution(values, run_length):
    solution_array = []
    if run_length == 0 or run_length > len(values):
        return solution_array
    if run_length == 1:
        for i in range(len(values)):
            solution_array.append(i)
        return solution_array
    for i in range(len(values)-run_length+1):
        counter = 0
        increase = 0
        decrease = 0
        run_index = i
        while counter < run_length-1:
            if values[run_index] - values[run_index+1] == -1:
                increase += 1
                counter += 1
                run_index += 1
                if increase == run_length-1:
                    solution_array.append(i)
            elif values[run_index] - values[run_index+1] == 1:
                decrease += 1
                counter += 1
                run_index += 1
                if decrease == run_length-1:
                    solution_array.append(i)
            else:
                counter += 1
                run_index += 1
    return solution_array
##########################################################################

values = [1, 2]
run_length = 3 
print('Expecting: []')
print('This is the solution:', solution(values, run_length))

values = [1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7, 8, 7]
run_length = 3 
print('Expecting: [0, 4, 6, 7]')
print('This is the solution:', solution(values, run_length))

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

values = [0, -2, 7, -4, 9]
run_length = 1
print('Expecting: [0, 1, 2, 3, 4]')
print('This is the solution:', solution(values, run_length))

values = [-1, -2, -3, -4, -5]
run_length = 0
print('Expecting: []')
print('This is the solution:', solution(values, run_length))

values = [0, -2, -3, -4, 8]
run_length = 2
print('Expecting: [1, 2]')
print('This is the solution:', solution(values, run_length))