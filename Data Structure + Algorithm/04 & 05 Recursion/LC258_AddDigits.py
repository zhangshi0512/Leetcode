"""
258. Add Digits

Given an integer num, 
repeatedly add all its digits until the result has only one digit, and return it.

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.

Input: num = 0
Output: 0

Constraints:

0 <= num <= 2^31 - 1
"""


def addDigits(num):
    # 定义一个函数用于计算数字的各位数字之和
    def new_num(num):
        new_num = 0
        while num > 0:
            digit = num % 10
            new_num += digit
            num = num // 10
        return new_num

    # 如果 num 小于 10，直接返回 num，因为它已经是一个个位数了
    if num < 10:
        return num

    # 循环计算各位数字之和，直到结果变为个位数
    while num >= 10:
        num = new_num(num)

    return num


print(2, addDigits(38))
print(0, addDigits(0))
