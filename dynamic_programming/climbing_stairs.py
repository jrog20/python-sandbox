# Climbing Stairs

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

########################################################################################
# Dynamic Programming
# We can reach the ith step one of two ways:
# 1. Taking a single step (i - 1)
# 2. Taking a step of 2 (i - 2)
# So the total number of ways to reach the ith step is to sum the two ways: (i - 1) + (i - 2)
########################################################################################
def climb_stairs(n):
    if(n == 1):
        return 1
    steps = []
    steps.append(0)
    steps.append(1)
    steps.append(2)
    i = 3
    while i <= n:
        next = steps[i - 1] + steps[i - 2]
        steps.append(next)
        i += 1
    return steps[n]
########################################################################################
n = 2
print('Expecting: 2')
print('Output:', climb_stairs(n))

n = 3
print('Expecting: 3')
print('Output:', climb_stairs(n))