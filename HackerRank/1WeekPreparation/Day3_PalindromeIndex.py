"""
Given a string of lowercase letters in the range ascii[a-z], 
determine the index of a character that can be removed to make the string a palindrome. 
There may be more than one solution, but any will do. 

if the word is already a palindrome or there is no solution, return -1. 
Otherwise, return the index of a character to remove. 

Example: s = 'bcbc' Either remove 'b' at index 0 or 'c' at index 3. 
"""


def palindromeIndex(s):
    # 检查一个给定的字符串是否是回文
    def isPalindrome(s):
        if len(s) <= 1:
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

    # 遍历字符串以检查移除某个字符后的字符串
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            # 如果左右两端的字符不相等，尝试移除右边的字符并检查剩余的部分是否是回文
            if isPalindrome(s[left:right]):
                return right
            # 如果上一步不成功，尝试移除左边的字符并检查剩余的部分是否是回文
            elif isPalindrome(s[left+1:right+1]):
                return left
            else:
                # 如果两种可能都不成功，那么无法通过移除单个字符使其成为回文
                return -1
        left += 1
        right -= 1

    # 字符串已经是回文
    return -1


def palindromeIndex2(s):
    # check whether a given string is palindrome
    def isPalindrome(s):
        if len(s) <= 1:
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

    # iterate through the string to check the removed version of string
    if isPalindrome(s):
        return -1
    else:
        if isPalindrome(s[1:]):
            return 0

        elif isPalindrome(s[:len(s)-1]):
            return len(s)-1

        else:
            for i in range(1, len(s)-1):
                new_s = s[:i] + s[i+1:]
                if isPalindrome(new_s):
                    return i

        return -1


print(palindromeIndex("abcba"), palindromeIndex2("abcba"))
print(palindromeIndex("abbcba"), palindromeIndex2("abbcba"))
print(palindromeIndex("abba"), palindromeIndex2("abba"))
print(palindromeIndex("bba"), palindromeIndex2("bba"))
print(palindromeIndex("aba"), palindromeIndex2("aba"))
print()
