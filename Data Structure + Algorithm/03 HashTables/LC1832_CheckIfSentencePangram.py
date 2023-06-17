"""
1832. Check if the Sentence Is Pangram

A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, 
return true if sentence is a pangram, or false otherwise.

Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.

Example 2:

Input: sentence = "leetcode"
Output: false

Constraints:

1 <= sentence.length <= 1000
sentence consists of lowercase English letters.
"""


def checkIfPangram(sentence):
    Pandict = {}
    for c in sentence:
        if not c in Pandict:
            Pandict[c] = 1
        else:
            Pandict[c] += 1

    return len(list(Pandict.keys())) == 26


print(False, checkIfPangram("leetcode"))
print(True, checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
print()


def checkIfPangram2(sentence):
    return len(set(sentence)) == 26


print(False, checkIfPangram2("leetcode"))
print(True, checkIfPangram2("thequickbrownfoxjumpsoverthelazydog"))
