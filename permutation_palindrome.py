def permutation_palindrome(string):
    if string[0] != string[-1]:
        return False
    return True

string = 'carerac'
print('Expect: True')
print(permutation_palindrome(string))

string = 'hello'
print('Expect: False')
print(permutation_palindrome(string))