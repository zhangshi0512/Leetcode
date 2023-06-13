"""
Given an array of integers n and a positive number k, 
find the maximum sum of any contiguous subarray of size k

Example 1:

Input: [2,1,5,1,3,2], k = 3
Output: 9
Explanation: Subarray with maximum sum is [5,1,3].

Example 2:

Input: [1,9,-1,-2,7,3,-1,2], k = 4
Output: 13
Explanation: Subarray with maximum sum is [9,-1,-2,7].
"""


def MaxSumSubarrayOfSizeK(nums, k):
    windowSum = maxSum = sum(nums[:k])
    start, end = 0, k

    while end < len(nums):
        windowSum += nums[end] - nums[start]
        end += 1
        start += 1
        maxSum = max(windowSum, maxSum)

    return maxSum


print(9, MaxSumSubarrayOfSizeK([2, 1, 5, 1, 3, 2], 3))
print(13, MaxSumSubarrayOfSizeK([1, 9, -1, -2, 7, 3, -1, 2], 4))
