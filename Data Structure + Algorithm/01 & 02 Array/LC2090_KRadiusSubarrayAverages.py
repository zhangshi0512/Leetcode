"""
2090. K Radius Subarray Averages

You are given a 0-indexed array nums of n integers, and an integer k.

The k-radius average for a subarray of nums centered at some index i 
with the radius k is the average of all elements in nums between 
the indices i - k and i + k (inclusive). If there are less than k elements 
before or after the index i, then the k-radius average is -1.

Build and return an array avgs of length n where avgs[i] is the 
k-radius average for the subarray centered at index i.

The average of x elements is the sum of the x elements divided by x, 
using integer division. The integer division truncates toward zero, 
which means losing its fractional part.

For example, the average of four elements 2, 3, 1, and 5 
is (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75, which truncates to 2.

Input: nums = [7,4,3,9,1,8,5,2,6], k = 3
Output: [-1,-1,-1,5,4,4,-1,-1,-1]

Input: nums = [100000], k = 0
Output: [100000]

Input: nums = [8], k = 100000
Output: [-1]

Constraints:

n == nums.length
1 <= n <= 10^5
0 <= nums[i], k <= 10^5
"""

# 解法一: 遍历每个元素 (O(n*k)复杂度)
def kRadiusSubarrayAverages(nums, k):
    n = len(nums)
    avgs = []
    # 遍历每个元素
    for i in range(n):
        # 如果在索引i的前后有少于k个元素，k-半径平均数就为-1
        if i - k < 0 or i + k >= n:
            avgs.append(-1)
        else:
            # 计算k-半径平均数
            avg = sum(nums[i-k:i+k+1]) // (2*k+1)
            avgs.append(avg)

    return avgs

print([-1,-1,-1,5,4,4,-1,-1,-1], kRadiusSubarrayAverages([7,4,3,9,1,8,5,2,6], 3))
print([100000], kRadiusSubarrayAverages([100000], 0))
print([-1], kRadiusSubarrayAverages([8], 100000))
print()

# 解法二: 滑动窗口 (O(n)复杂度)
def kRadiusSubarrayAverages_Optimized(nums, k):
    n = len(nums)
    avgs = [-1]*n
    window_sum = 0
    # 初始化滑动窗口的和
    for i in range(min(n, 2*k+1)):
        window_sum += nums[i]
    # 对于每一个索引位置i，其左右都需要至少有k个元素才能计算出平均值
    for j in range(2*k, n):
        avgs[j-k] = window_sum // (2*k+1)
        # 添加右边的元素，删除左边的元素
        if j+1 < n:
            window_sum += nums[j+1] - nums[j-2*k]

    return avgs

print([-1,-1,-1,5,4,4,-1,-1,-1], kRadiusSubarrayAverages_Optimized([7,4,3,9,1,8,5,2,6], 3))
print([100000], kRadiusSubarrayAverages_Optimized([100000], 0))
print([-1], kRadiusSubarrayAverages_Optimized([8], 100000))