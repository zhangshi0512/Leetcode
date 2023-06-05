"""
169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
"""

def majorityElement(nums):
    major_count = len(nums) / 2
    elements = dict()

    for i in range(len(nums)):
        if nums[i] in elements:
            elements[nums[i]] += 1
        else:
            elements[nums[i]] = 1
    
    for key in elements.keys():
        if elements[key] > major_count:
            return key
        
print(3, majorityElement([3,2,3]))
print(2, majorityElement([2,2,1,1,1,2,2]))