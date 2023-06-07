"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Constraints:

1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.
"""

def isValid(s):
        stack = []
        closeToOpen = {')':'(', ']':'[', '}':'{'}

        for char in s:
            if char in closeToOpen:
                if len(stack) != 0 and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        if len(stack) == 0:
            return True
        else:
            return False
        
print(True, isValid("()"))
print(False, isValid("(]"))
print(True, isValid("()[]{}"))