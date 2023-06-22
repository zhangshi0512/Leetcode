"""
383. Ransom Note

Given two strings ransomNote and magazine, 
return true if ransomNote can be constructed by using 
the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:

1 <= ransomNote.length, magazine.length <= 10^5
ransomNote and magazine consist of lowercase English letters.
"""
from collections import defaultdict

# Brute Force (Two dictionary)
# T = O(N)
# S = O(N)


def canConstruct(ransomNote, magazine):
    r_dict = defaultdict(int)
    m_dict = defaultdict(int)

    for r in ransomNote:
        r_dict[r] += 1

    for m in magazine:
        m_dict[m] += 1

    for key, value in r_dict.items():
        if not (key in m_dict and value <= m_dict[key]):
            return False

    return True


print(True, canConstruct("aa", "aab"))
print(False, canConstruct("a", "b"))
print(False, canConstruct("aa", "ab"))
print()

# Slightly improved solution (one dictionary)


def canConstruct2(ransomNote, magazine):
    m_dict = defaultdict(int)

    for m in magazine:
        m_dict[m] += 1

    for r in ransomNote:
        m_dict[r] -= 1
        if m_dict[r] < 0:
            return False

    return True


print(True, canConstruct2("aa", "aab"))
print(False, canConstruct2("a", "b"))
print(False, canConstruct2("aa", "ab"))
