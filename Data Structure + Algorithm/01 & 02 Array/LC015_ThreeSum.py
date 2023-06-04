"""
15. 3Sum

Given an integer array nums, 
return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, 
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:

Input: nums = [0,1,1]
Output: []

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

def threeSum(nums):
    result = []
    nums.sort()
    n = len(nums)

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1

    return result

print([[-1,-1,2],[-1,0,1]], threeSum([-1,0,1,2,-1,-4]))
print([], threeSum([0,1,1]))
print([[0,0,0]], threeSum([0,0,0]))

