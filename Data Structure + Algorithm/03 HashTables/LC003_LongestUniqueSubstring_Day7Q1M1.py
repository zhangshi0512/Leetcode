"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3

Example 2:

Input: s = "bbbbb"
Output: 1

Example 3:

Input: s = "pwwkew"
Output: 3

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


def max_unique_length(str):
    max_len = 0
    start = 0
    seen = {}  # store each char and its index into dict seen
    for i in range(len(str)):
        char = str[i]
        # found repeated char
        if char in seen:
            # Update the start position of the substring
            # to be the maximum between the current start position
            # and the next position of the last occurrence of
            # the current character
            start = max(start, seen[char]+1)
        # Update the max_len to be the maximum between the current
        # max_len and the length of the current substring
        max_len = max(max_len, i-start+1)
        # if found unique char, store its index
        seen[char] = i
    return max_len


print(max_unique_length('pqbrstbuvwpvy'))
print(max_unique_length('abcabcbb'))
print(max_unique_length('bbbbb'))
print(max_unique_length('pwwkew'))
