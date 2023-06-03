"""
509. Fibonacci Number

The Fibonacci numbers, commonly denoted F(n) form a sequence, 
called the Fibonacci sequence, such that each number is the 
sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

Example 1:

Input: n = 2
Output: 1

Example 2:

Input: n = 3
Output: 2

Example 3:

Input: n = 4
Output: 3

Constraints:

0 <= n <= 30
"""

def fibonacci_2(n, ht={0: 0, 1: 1}):
    if n in ht:
        return ht[n]
    else:
        ht[n] = fibonacci_2(n - 1, ht) + fibonacci_2(n - 2, ht)
        return ht[n]


print(fibonacci_2(4))
