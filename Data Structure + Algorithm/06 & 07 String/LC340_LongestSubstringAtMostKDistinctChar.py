"""
340. Longest Substring with At Most K Distinct Characters

Given a string s and an integer k, return the length of the longest 
substring of s that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.

Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.
"""

def length_of_longest_substring_optimized(s, k):
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
        # 如果当前窗口中的不同字符数量超过 k，则需要移动左指针，缩小窗口，直到窗口中的不同字符数量不超过 k
        while len(freq_count) > k:
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


print(3, length_of_longest_substring_optimized("eceba", 2))
print(2, length_of_longest_substring_optimized("aa", 1))