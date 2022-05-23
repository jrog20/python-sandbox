# Container with the most water

# You are given an integer array height of length n. There are n vertical lines drawn 
# such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
# In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1
########################################################################################
# Brute force solution:
# Iterate through the height array, calculating the area of each potential container,
# saving the maximum area found in a variable to return.
# We calculate the area for each potential container by multiplying the difference between 
# two lines i value by the minimum value of the two line height[i] values.

# Time complexity: O(n^2)
# Space complexity: O(1)
########################################################################################
# def max_area(height):
#     max_water = 0
#     for i in range(len(height)):
#         for j in range(len(height)):
#             container_length = j - i
#             container_height = min(height[j], height[i])
#             area = container_length * container_height
#             max_water = max(area, max_water)
#     return max_water
########################################################################################
# Two pointer solution:
# The greatest area will be constrained by the lowest line height, and will be increased
# by the greater the distance between lines.
# Using two pointers, we move the pointer of the lower height one closer to the pointer
# with a higher height.

# Time complexity: O(n)
# Space complexity: O(1)
########################################################################################
def max_area(height):
    max_water = 0
    left = 0
    right = len(height) -1
    while right >= left:
        container_length = right - left
        container_height = min(height[right], height[left])
        area = container_length * container_height
        max_water = max(area, max_water)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water
########################################################################################
height = [1,8,6,2,5,4,8,3,7]
print('Expecting: 49')
print(max_area(height))

height = [1,1]
print('Expecting: 1')
print(max_area(height))

height = [11,13,15,17]
print('Expecting: 33')
print(max_area(height))