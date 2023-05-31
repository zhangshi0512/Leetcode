"""
LC 387. First Unique Character in a String
Given a string s, find the first non-repeating character in it and return its index. 
If it does not exist, return -1.

Example 1:

Input: s = "leetcode"
Output: 0

Example 2:

Input: s = "loveleetcode"
Output: 2

Example 3:

Input: s = "aabb"
Output: -1

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
"""

def non_repeating_char(str):
    ht = {}
    for i in str:
        if i in ht:
            ht[i]+=1
        else:
            ht[i] = 1
    for i in range(len(str)):
        if ht[str[i]] == 1:
            return i
    return None


print(non_repeating_char('AbcabcdA'))