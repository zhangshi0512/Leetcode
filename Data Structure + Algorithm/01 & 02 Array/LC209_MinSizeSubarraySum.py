"""
Given an array of positive integers nums and a positive integer target, 
return the minimal length of a subarray whose sum is greater than or equal to target. 

If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Constraints:

1 <= target <= 10^9
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4
"""


def minSubArrayLen(target, nums):
    n = len(nums)
    start, end = 0, 0
    total = 0
    min_length = float('inf')

    while end < n:
        total += nums[end]
        end += 1

        while total >= target:
            min_length = min(min_length, end - start)
            total -= nums[start]
            start += 1

    return 0 if min_length == float('inf') else min_length


print(2, minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(1, minSubArrayLen(4, [1, 4, 4]))
print(0, minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
