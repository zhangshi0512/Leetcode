"""
49. Group Anagrams

Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

from collections import defaultdict


def groupAnagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = "".join(sorted(s))
        groups[key].append(s)

    return list(groups.values())


print(groupAnagrams(['arc', 'abc', 'car', 'cat', 'act', 'acb', 'atc']))
print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print()


def group_anagrams(strings):
    if len(strings) == 0:
        return []
    sorted_string = [''.join(sorted(i)) for i in strings]
    hash = {}
    for i in range(len(sorted_string)):
        if sorted_string[i] in hash:
            hash[sorted_string[i]].append(strings[i])
        else:
            hash[sorted_string[i]] = [strings[i]]
    return list(hash.values())


print(group_anagrams(['arc', 'abc', 'car', 'cat', 'act', 'acb', 'atc']))
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
