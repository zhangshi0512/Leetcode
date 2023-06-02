"""
451. Sort Characters By Frequency

Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

Constraints:

1 <= s.length <= 5 * 105
s consists of uppercase and lowercase English letters and digits.
"""
# Solution 1:
def frequencySort(s):
    s_dict = {}

    for c in s:
        if not c in s_dict:
            s_dict[c] = 1
        else:
            s_dict[c] += 1

    sorted_dict = dict(sorted(s_dict.items(), key = lambda x: x[1], reverse = True))

    res = ""
    for char, freq in sorted_dict.items():
        res += char * freq

    return res

print("eert", frequencySort("tree"))
print("aaaccc", frequencySort("cccaaa"))
print("bbAa", frequencySort("Aabb"))

# Solution 2:
def frequencySort2(s):
    output = []
    for c in set(s):
        count = s.count(c)
        output.append(c*count)

    output = sorted(output, key = len, reverse = True)
    return "".join(output)

print("eert", frequencySort2("tree"))
print("aaaccc", frequencySort2("cccaaa"))
print("bbAa", frequencySort2("Aabb"))