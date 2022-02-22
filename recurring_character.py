# Given a string, write a function recurring_char to find its first recurring character. 
# Return None if there is no recurring character.

# Treat upper and lower case letters as distinct characters.
# You may assume the input string includes no spaces.

# Example 1:
# Input:
# input = "interviewquery"
# Output:
# output = "i"

# Example 2:
# Input:
# input = "interv"
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

print(recurring_char(input))