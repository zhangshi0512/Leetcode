"""
1446. Consecutive Characters

The power of the string is the maximum length of a non-empty 
substring that contains only one unique character.

Given a string s, return the power of s.

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

Constraints:

1 <= s.length <= 500
s consists of only lowercase English letters.
"""


def maxPower(s):
    count = max_count = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
            max_count = max(count, max_count)
        else:
            count = 1

    return max_count


print(2, maxPower("leetcode"))
print(5, maxPower("abbcccddddeeeeedcba"))
