"""
485. Max Consecutive Ones

Given a binary array nums, 
return the maximum number of consecutive 1's in the array.

Input: nums = [1,1,0,1,1,1]
Output: 3

Input: nums = [1,0,1,1,0,1]
Output: 2

Constraints:

1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
"""


def findMaxConsecutiveOnes(nums):
    if len(nums) == 1 and nums[0] == 1:
        return 1

    count = 0
    max_count = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            max_count = max(count, max_count)
            count = 0

    return max_count


print(3, findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
print(2, findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))
