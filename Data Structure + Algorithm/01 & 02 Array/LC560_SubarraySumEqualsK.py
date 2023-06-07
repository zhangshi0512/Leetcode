"""
560. Subarray Sum Equals K

Given an array of integers nums and an integer k, 
return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2

Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""

def subarraySum(nums, k):
    count = curr_sum = 0
    sum_map = {0: 1}  # 初始化哈希表，用于保存累计和及其出现次数
    
    for num in nums:
        curr_sum += num  # 累加当前数字
        # 如果累计和减去目标值k的结果存在于哈希表中，
        # 则将对应的次数加到结果中
        if curr_sum - k in sum_map:
            count += sum_map[curr_sum - k]
        # 将当前累计和加入哈希表
        sum_map[curr_sum] = sum_map.get(curr_sum, 0) + 1
    
    return count

print(2, subarraySum([1,1,1], 2))
print(2, subarraySum([1,2,3], 3))