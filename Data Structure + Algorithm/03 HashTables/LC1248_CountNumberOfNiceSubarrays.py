"""
1248. Count Number of Nice Subarrays

Given an array of integers nums and an integer k. 
A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16

Constraints:

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length
"""

# Brute Force: Runtime Error
# T = O(n^3)
# S = O(1)

def numberOfSubarrays(nums, k):
    # 初始化计数为 0
    count = 0

    # 遍历数组
    for i in range(len(nums)):
        # 临时计数器
        odd_count = 0
        # 内部遍历
        for j in range(i, len(nums)):
            # 判断是否为奇数
            if nums[j] % 2 == 1:
                odd_count += 1
            # 如果奇数数量满足条件
            if odd_count == k:
                count += 1
    return count

print(2, numberOfSubarrays([1,1,2,1,1],3))
print(0, numberOfSubarrays([2,4,6],1))
print(16, numberOfSubarrays([2,2,2,1,2,2,1,2,2,2],2))
print()

# Sliding Window & Prefix Sum
# T = O(n)
# S = O(1)

def numberOfSubarrays2(nums, k):
    # 初始化前缀和数组，长度为 len(nums)+1，以便处理边界情况
    prefix_sums = [0]*(len(nums)+1)
    res = odd_count = 0
    for i in range(len(nums)):
        # 如果当前数字为奇数，odd_count加1
        if nums[i] % 2 == 1:
            odd_count += 1
        # 如果当前的奇数数量大于等于 k，那么就可以从前缀和数组中取出结果累加到 res
        if odd_count >= k:
            res += prefix_sums[odd_count - k]
        # 每次循环结束，更新当前奇数数量的前缀和数量
        prefix_sums[odd_count] += 1
    return res

print(2, numberOfSubarrays2([1,1,2,1,1],3))
print(0, numberOfSubarrays2([2,4,6],1))
print(16, numberOfSubarrays2([2,2,2,1,2,2,1,2,2,2],2))
print()

# Math
# T = O(n)
# S = O(n)

def numberOfSubarrays3(nums, k):
    n = len(nums)
    # 给奇数索引列表首尾各添加一个元素，处理边界问题
    oddIndex = [-1]
    for i in range(n):
        if(nums[i] % 2 == 1):
            oddIndex.append(i)
    oddIndex.append(n)

    # 计算所有满足条件的子数组数量
    ans = 0
    for i in range(1, len(oddIndex) - k):
        # 前面可以选择的子数组起始位置数
        left = oddIndex[i] - oddIndex[i - 1]
        # 后面可以选择的子数组结束位置数
        right = oddIndex[i + k] - oddIndex[i + k - 1]
        # 乘积就是当前奇数索引下，满足条件的子数组数量
        ans += left * right
    return ans

print(2, numberOfSubarrays3([1,1,2,1,1],3))
print(0, numberOfSubarrays3([2,4,6],1))
print(16, numberOfSubarrays3([2,2,2,1,2,2,1,2,2,2],2))
print()