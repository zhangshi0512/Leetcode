"""
202. Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, 
replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Input: n = 2
Output: false

Constraints:

1 <= n <= 2^31 - 1
"""


def isHappy(n):
    def calculateHappySum(n):
        happy_sum = 0
        while n > 0:
            digit = n % 10
            happy_sum += digit ** 2
            n = n // 10

        return happy_sum

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = calculateHappySum(n)
    return n == 1


print(True, isHappy(19))
print(False, isHappy(2))
