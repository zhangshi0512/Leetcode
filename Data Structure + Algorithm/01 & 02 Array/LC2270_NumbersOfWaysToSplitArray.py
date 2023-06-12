"""
2270. Number of Ways to Split Array

You are given a 0-indexed integer array nums of length n.

nums contains a valid split at index i if the following are true:

The sum of the first i + 1 elements is greater than or equal to 
the sum of the last n - i - 1 elements.
There is at least one element to the right of i. That is, 0 <= i < n - 1.
Return the number of valid splits in nums.

Example 1:

Input: nums = [10,4,-8,7]
Output: 2

Example 2:

Input: nums = [2,3,1,0]
Output: 2

Constraints:

2 <= nums.length <= 10^5
-10^5 <= nums[i] <= 10^5
"""

def waysToSplitArray(nums):
    # 初始化prefix sum数组的首位为原数组的首位
    prefix = [nums[0]]
    # 之后的每一位数都是prefix sum数组中的末位数加上当前的原数组
    for i in range(1, len(nums)):
        # 这样就得到了和原数组长度相同的prefix sum数组
        prefix.append(prefix[-1] + nums[i])

    ans = 0 # 初始化计数变量
    # 开始遍历prefix sum数组, 注意条件要求左侧之和大于右侧之和。
    # 需要排除在末位的切分, 因为此时右侧为空集
    for j in range(len(nums) - 1):
        left = prefix[j]
        right = prefix[-1] - left
        if left >= right:
            ans += 1

    return ans

print(2, waysToSplitArray([10,4,-8,7]))
print(2, waysToSplitArray([2,3,1,0]))

print()

# Do we really need the prefix array?
# No! We can apply the concept without using prefix array.
# The method below only need 1 for loop to iterate through the nums array.
def waysToSplitArray2(nums):
    # 初始化 计数变量 和 左侧之和
    ans = left = 0
    # 直接先算出整个数列的和
    total = sum(nums)

    # 遍历原数组一次，逐个计算每一个index对应的左右之和
    # 比较并计数
    for i in range(len(nums)-1):
        left += nums[i]
        right = total - left
        if left >= right:
            ans += 1
    
    return ans

print(2, waysToSplitArray2([10,4,-8,7]))
print(2, waysToSplitArray2([2,3,1,0]))
