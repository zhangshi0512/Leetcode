"""
643. Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average 
value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Input: nums = [5], k = 1
Output: 5.00000

Constraints:

n == nums.length
1 <= k <= n <= 10^5
-10^4 <= nums[i] <= 10^4
"""

# Two Pointers Solution

def findMaxAverage(nums, k):
    # base case: when len(nums) == k
    if len(nums) == k:
        return sum(nums) / k

    # define two pointers
    l, r = 0, k-1

    max_average = sum(nums[l:r+1]) / k

    while r < len(nums)-1:
        l += 1
        r += 1
        average = sum(nums[l:r+1]) / k
        if average > max_average:
            max_average = average

    return max_average


print(12.75, findMaxAverage([1, 12, -5, -6, 50, 3], 4))
print(5.00, findMaxAverage([5], 1))

print()

# Sliding Window Solution

def findMaxAverageOptimized(nums, k):
    # 初始化前k个数字的总和
    total_k = sum(nums[:k])
    max_total = total_k

    # 从第k个数字开始，通过滑动窗口更新总和，
    # 这意味着减去最左边的数字并添加新的最右边的数字
    for i in range(k, len(nums)):
        total_k = total_k - nums[i - k] + nums[i]
        max_total = max(max_total, total_k)

    # 以浮点数返回平均值，即总和除以k
    return max_total / float(k)


print(12.75, findMaxAverageOptimized([1, 12, -5, -6, 50, 3], 4))
print(5.00, findMaxAverageOptimized([5], 1))
