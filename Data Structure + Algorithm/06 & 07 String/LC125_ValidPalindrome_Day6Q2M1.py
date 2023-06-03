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

# In Python Strings are immutable.
def is_palindrome(str):
    new_str = ''
    for i in reversed(range(len(str))):
        new_str += str[i]
    if str == new_str:
        return True
    return False


print(is_palindrome('aab'))
