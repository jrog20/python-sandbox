# Method:

# Declare a variable with the length of the string.
# Declare a for loop, using half of the length of the string as a reference point.
# Check if each letter is the same as its mirror equivalent — or, 
# a character on the other side (measured with index — 1).

def palindrome(string):
    l = len(string)
    for i in range(l//2):
        if string[i] != string[l-i-1]:
            return False
    return True

string = 'carerac'
print('Expect: True')
print(palindrome(string))

string = 'helloh'
print('Expect: False')
print(palindrome(string))

string = 'jfdkjlfds'
print('Expect: False')
print(palindrome(string))

string = 'scarpepracs'
print('Expect: True')
print(palindrome(string))
