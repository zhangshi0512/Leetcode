"""
487. Max Consecutive Ones II

Given a binary array nums, return the maximum number of consecutive 1's 
in the array if you can flip at most one 0.

Input: nums = [1,0,1,1,0]
Output: 4
Explanation: 
- If we flip the first zero, nums becomes [1,1,1,1,0] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1] and we have 3 consecutive ones.
The max number of consecutive ones is 4.

Input: nums = [1,0,1,1,0,1]
Output: 4
Explanation: 
- If we flip the first zero, nums becomes [1,1,1,1,0,1] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1,1] and we have 4 consecutive ones.
The max number of consecutive ones is 4.
"""

# 时间复杂度为 O(n)
# 该方法利用动态规划的思想，将问题拆解为一系列子问题。定义两个变量 zero 和 one，
# zero表示当前连续的1的个数，one表示之前连续的1的个数加上一个0的个数。
def findMaxConsecutiveOnesII(nums):
    zero = one = max_len = 0
    # 遍历数组，如果当前数是1，则 zero 和 one 都加1，
    # 如果当前数是0，则 one 变为 zero + 1，zero 变为0。
    for num in nums:
        if num == 1:
            zero += 1
            one += 1
        else:
            one = zero + 1
            zero = 0
        # 每次遍历后都更新最大值。
        max_len = max(max_len, one)

    return max_len

print(4, findMaxConsecutiveOnesII([1,0,1,1,0]))
print(4, findMaxConsecutiveOnesII([1,0,1,1,0,1]))
