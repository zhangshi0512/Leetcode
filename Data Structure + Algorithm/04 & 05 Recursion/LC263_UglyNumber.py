"""
263. Ugly Number

An ugly number is a positive integer whose prime factors are 
limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.

Input: n = 6
Output: true
Explanation: 6 = 2 x 3

Input: n = 1
Output: true
Explanation: 1 has no prime factors, 
therefore all of its prime factors are limited to 2, 3, and 5.

Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.

Constraints:

-2^31 <= n <= 2^31 - 1
"""


def isUgly(n):
    # 如果 n 小于等于 0，直接返回 False
    if n <= 0:
        return False
    # 循环判断 n 是否可以被 2、3、5 整除
    while n > 1:
        if (n % 2 == 0):
            n = n // 2
        elif (n % 3 == 0):
            n = n // 3
        elif (n % 5 == 0):
            n = n // 5
        # 如果 n 不能被 2、3、5 整除，说明 n 不是 ugly number，返回 False
        else:
            return False
    # 当 n 最终变为 1 时，说明 n 是 ugly number
    return True

print(True, isUgly(6))
print(True, isUgly(1))
print(False, isUgly(14))
