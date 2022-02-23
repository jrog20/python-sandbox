def palindrome(string):
    if string[0] != string[-1]:
        return False
    return True

string = 'carerac'
print('Expect: True')
print(palindrome(string))

string = 'hello'
print('Expect: False')
print(palindrome(string))
