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
    seen = {}
    for i in range(len(str)):
        char = str[i]
        if char in seen:
            start = max(start,seen[char]+1)
        max_len = max(max_len,i-start+1)
        seen[char]=i
    return max_len


print(max_unique_length('pqbrstbuvwpvy'))
print(max_unique_length('abcabcbb'))
print(max_unique_length('bbbbb'))
print(max_unique_length('pwwkew'))