"""
344. Reverse String

Write a function that reverses a string. 
The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
"""
def reverseString(s):
    i, j = 0, len(s)-1

    while i < j and len(s) > 1:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1

s1 = ["h","e","l","l","o"]
reverseString(s1)
print(s1)

s2 = ["H","a","n","n","a","h"]
reverseString(s2)
print(s2)