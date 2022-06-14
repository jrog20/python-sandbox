# Given two strings text1 and text2, return the length of their longest common subsequence. 
# If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some 
# characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

# Example 1:
# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.

# Example 2:
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.

# Example 3:
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
#######################################################################################
# Dynamic Programing solution - Memoization:
# In Python, we can use lru_cache to make sure that the results of the method are memoized

# *pseudocode*
# define function LCS(text1, text2):
#     # If either string is empty there can be no common subsequence
#     if length of text1 or text2 is 0:
#         return 0

#     letter1 = the first letter in text1

#     # The case where the line *is not* part of the optimal solution
#     case1 = LCS(text1.substring(1), text2)

#     case2 = 0
#     if letter1 is in text2:
#         firstOccurence = first position of letter1 in text2
#         # The case where the line *is* part of the optimal solution
#         case2 = 1 + LCS(text1.substring(1), text2.substring(firstOccurence + 1))
#     return maximum of case1 and case2

# Time complexity: O(n^2)
# Space complexity: O(n)
#######################################################################################
from functools import lru_cache

def longest_common_subsequence(text1, text2):

    def memo_solve(p1, p2):
            
        # base case - if either string is empty, we can't match any additional characters
        if p1 == len(text1) or p2 == len(text2):
            return 0
            
        # case 1: The case where the line *is not* part of the optimal solution
        # We don't include text1[p1] in the solution
        case1 = memo_solve(p1 + 1, p2)
        
        # case 2: The case where the line *is* part of the optimal solution
        # We include text1[p1] in the solution, as long as a match for it in text2 at or after p2 exists
        first_occurence = text2.find(text1[p1], p2)
        case2 = 0
        if first_occurence != -1:
            case2 = 1 + memo_solve(p1 + 1, first_occurence + 1)
        
        # return maximum of case1 and case2
        return max(case1, case2)
            
    return memo_solve(0, 0)

#######################################################################################
text1 = "abcde"
text2 = "ace"
print('Expecting: 3')
print('Output:', longest_common_subsequence(text1, text2))

text1 = "abc"
text2 = "abc"
print('Expecting: 3')
print('Output:', longest_common_subsequence(text1, text2))

text1 = "abc"
text2 = "def"
print('Expecting: 0')
print('Output:', longest_common_subsequence(text1, text2))

text1 = "actgattag"
text2 = "gtgtgatcg"
print('Expecting: 5')
print('Output:', longest_common_subsequence(text1, text2))