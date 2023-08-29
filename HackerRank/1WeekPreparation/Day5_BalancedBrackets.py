"""
A bracket is considered to be any one of the following characters: 
(, ), {, }, [, or ].

Two brackets are considered to be a matched pair if the an opening bracket 
(i.e., (, [, or {) occurs to the left of a closing bracket (i.e., ), ], or }) 
of the exact same type. 

There are three types of matched pairs of brackets: [], {}, and ().

A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. 
For example, {[(])} is not balanced because the contents in between { and } are not balanced. 
The pair of square brackets encloses a single, unbalanced opening bracket, (, and the pair of parentheses 
encloses a single, unbalanced closing square bracket, ].

By this logic, we say a sequence of brackets is balanced if the following conditions are met:

It contains no unmatched brackets.
The subset of brackets enclosed within the confines of a matched pair of brackets 
is also a matched pair of brackets.

Given n strings of brackets, determine whether each sequence of brackets is balanced. 
If a string is balanced, return YES. Otherwise, return NO.

Function Description

Complete the function isBalanced in the editor below.

isBalanced has the following parameter(s):

string s: a string of brackets
Returns

string: either YES or NO
"""
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.


def isBalanced(s):
    # Initialize an empty stack.
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}
    # Iterate through each character in the string.
    for char in s:
        # If the character is an opening bracket (i.e., (, [, or {), push it onto the stack.
        if char in ['(', '[', '{']:
            stack.append(char)
        # If character is a closing bracket
        else:
            # Check if stack is empty or top of stack doesn't match with the bracket pair
            if not stack or stack[-1] != bracket_map[char]:
                return "NO"
            stack.pop()

    # Check if there are any unmatched opening brackets left
    if stack:
        return "NO"

    return "YES"


# Test the function
test_cases = ["{}", "{[()]}", "{[(])}", "{{[[(())]]}}"]
results = [isBalanced(tc) for tc in test_cases]
results
