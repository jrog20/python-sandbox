# Given a string, write a function recurring_char to find its first recurring character. 
# Return None if there is no recurring character.

# Treat upper and lower case letters as distinct characters.
# You may assume the input string includes no spaces.

# Example 1:
# Input:
# input = "fantastic"
# Output:
# output = "a"

# Example 2:
# Input:
# input = "uncopyrightable"
# Output:
# output = None

def recurring_char(input):
    viewed = set()
    
    for i in input:
        if i not in viewed:
            viewed.add(i)
        else: 
            return i
    return None

input = "fantastic"
print('Expecting: a')
print('Output:', recurring_char(input))
print('')

input = "uncopyrightable"
print('Expecting: None')
print('Output:', recurring_char(input))
print('')