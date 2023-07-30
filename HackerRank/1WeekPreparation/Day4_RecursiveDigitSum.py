"""
We define super digit of an integer x using the following rules:

Given an integer, we need to find the super digit of the integer.

If x has only 1 digit, then its super digit is x.
Otherwise, the super digit of x is equal to the super digit of the sum of the digits of x.

For example, the super digit of 9875 will be calculated as:

super_digit(9875)   	9+8+7+5 = 29 
super_digit(29) 	2 + 9 = 11
super_digit(11)		1 + 1 = 2
super_digit(2)		= 2  

Example:
n = '9875'
k = 4
p = n*k

superDigit(p) = superDigit(9875987598759875)
                9+8+7+5+9+8+7+5+9+8+7+5+9+8+7+5 = 116
superDigit(p) = superDigit(116)
                1+1+6 = 8
superDigit(p) = superDigit(8)

All of the digits of p sum to 116. 
The digits of 116 sum to 8. 
8 is only one digit, so it is the super digit.
"""


def superDigit(n, k):
    # 定义求数字之和的函数
    def digitSum(n):
        digitSum = 0
        while n > 10:
            digitSum += n % 10  # 取最后一位数值，加到digitSum上
            n = n // 10  # 将n除以10，向下取整
        digitSum += n  # 将n的最后一个数字加到digitSum上
        return digitSum  # 返回digitSum

    p = int(n) * k  # 生成新的数值p，等于n和k的乘积
    superDigit = digitSum(p)  # 对p求各位数字之和，赋值给superDigit
    while True:  # 开始循环
        if superDigit < 10:  # 如果superDigit是一位数
            return superDigit  # 返回superDigit
        else:
            # 否则，对superDigit求各位数字之和，然后赋值给superDigit
            superDigit = digitSum(superDigit)


def superDigit2(n, k):
    # 定义一个函数，计算数字之和，利用取余运算代替直接相加
    def addDigits(num):
        if num < 10:
            return num
        else:
            return num % 9 if num % 9 != 0 else 9

    # 计算n的超级数字，然后乘以k，再计算结果的超级数字
    n = str(sum(int(x) for x in n) * k)
    return addDigits(int(n))


print(8, superDigit('9875', 4))
print(8, superDigit2('9875', 4))
