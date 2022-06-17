# Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#######################################################################################
# solution:


# Time Complexity: 
# Space Complexity: 
#######################################################################################
def length_of_longest_substring(s):
    # hash = {}
    # max_len = curr = 0

    # if len(s) < 2:
    #     return len(s)

    # for i in range(len(s)):
    #     if hash[s[i]] == None: 
    #         curr += 1
    #     else:
    #         curr = min(i - hash[s[i]], curr + 1)
    #     max_len = max(max_len, curr)
    #     hash[s[i]] = i
    # return max_len

    n = len(s)
    max_len = 0
    # mp stores the current index of a character
    mp = {}

    i = 0
    # try to extend the range [i, j]
    for j in range(n):
        if s[j] in mp:
            i = max(mp[s[j]], i)

        max_len = max(max_len, j - i + 1)
        mp[s[j]] = j + 1

    return max_len
#######################################################################################
s = "abcabcbb"
print('Expecting: 3')
print('Output:', length_of_longest_substring(s))

s = "bbbbb"
print('Expecting: 1')
print('Output:', length_of_longest_substring(s))

s = "pwwkew"
print('Expecting: 3')
print('Output:', length_of_longest_substring(s))