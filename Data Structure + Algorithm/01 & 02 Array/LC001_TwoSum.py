"""
1. Two Sum

Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

def TwoSum(arr, target):
    result = {}

    for i in range(len(arr)):
        complement = target - arr[i]
        if complement in result:
            return [i, result[complement]]
        result[arr[i]] = i
        
    return []


print([0,1], TwoSum([2,7,11,15], 9))
print([1,2], TwoSum([3,2,4], 6))
print([0,1], TwoSum([3,3], 6))