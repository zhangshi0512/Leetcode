"""
159. Longest Substring with At Most Two Distinct Characters

Given a string s, return the length of the longest 
substring that contains at most two distinct characters.

Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.

Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.

Constraints:

1 <= s.length <= 105
s consists of English letters.
"""

def length_of_longest_substring_two_distinct_optimized(s):
    # 初始化一个字典来统计当前窗口中各字符的频率
    freq_count = {}
    # 初始化最大长度为 0
    max_len = 0
    # 初始化左指针（窗口的左边界）
    left = 0

    # 对输入字符串进行遍历，此处的 right 变量相当于滑动窗口的右指针
    for right in range(len(s)):
        # 更新当前字符的频率
        freq_count[s[right]] = freq_count.get(s[right], 0) + 1
        # 如果当前窗口中的不同字符数量超过 2，则需要移动左指针，缩小窗口，直到窗口中的不同字符数量不超过 2
        while len(freq_count) > 2:
            # 左指针对应的字符频率减 1
            freq_count[s[left]] -= 1
            # 如果左指针对应的字符频率为 0，那么从字典中删除这个字符
            if freq_count[s[left]] == 0:
                del freq_count[s[left]]
            # 移动左指针
            left += 1
        # 更新最大长度
        max_len = max(max_len, right - left + 1)

    # 返回最大长度
    return max_len

print(3, length_of_longest_substring_two_distinct_optimized("eceba"))
print(5, length_of_longest_substring_two_distinct_optimized("ccaabbb"))