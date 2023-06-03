"""
125. Valid Palindrome

Given a string s, return true if it is a palindrome, or false otherwise.
A phrase is a palindrome if, 
after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true

Example 2:

Input: s = "race a car"
Output: false

Example 3:

Input: s = " "
Output: true

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""

def is_palindrome3(str):
    i = 0
    j = len(str)-1
    while i<j:
        if str[i] != str[j]:
            return False
        i += 1
        j -= 1
    return True


print(is_palindrome3('a'))