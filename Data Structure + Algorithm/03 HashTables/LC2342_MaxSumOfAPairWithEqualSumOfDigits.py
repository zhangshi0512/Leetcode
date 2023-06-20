"""
2342. Max Sum of a Pair With Equal Sum of Digits

You are given a 0-indexed array nums consisting of positive integers. 
You can choose two indices i and j, such that i != j, 
and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that 
you can obtain over all possible indices i and j that satisfy the conditions.

Example 1:

Input: nums = [18,43,36,13,7]
Output: 54
Explanation: The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.
Example 2:

Input: nums = [10,12,19,14]
Output: -1
Explanation: There are no two numbers that satisfy the conditions, so we return -1.

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
"""

from collections import defaultdict


def maximumSum(nums):
    # 先写一个辅助功能
    # 计算一个给定数的各个位数之和
    def getDigitSum(num):
        digit_sum = 0
        while num:
            digit_sum += num % 10
            num //= 10

        return digit_sum

    # 初始化一个默认字典
    # 以位数之和为key，相同位数之和的数字列表为value
    num_dict = defaultdict(list)
    for num in nums:
        digit_sum = getDigitSum(num)
        num_dict[digit_sum].append(num)

    # 初始化答案为-1
    ans = -1
    # 遍历每一个位数和对应的数字列表
    for value in num_dict.values():
        curr = value
        # 忽略列表中只有一个数的情况
        if len(curr) > 1:
            # 将列表降序排列
            curr.sort(reverse=True)
            # 比较并更新最大值
            ans = max(ans, curr[0]+curr[1])

    return ans

print(54, maximumSum([18,43,36,13,7]))
print(-1, maximumSum([10,12,19,14]))
