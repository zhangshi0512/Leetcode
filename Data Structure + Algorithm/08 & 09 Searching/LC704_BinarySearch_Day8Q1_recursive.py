"""
704. Binary Search

Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:

1 <= nums.length <= 10^4
-10^4 < nums[i], target < 10^4
All the integers in nums are unique.
nums is sorted in ascending order.
"""


def binary_search_recursive(nums, target):
    def helper(nums, target, left, right):
        if left > right:
            return -1
        middle = (left + right)//2
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            return helper(nums, target, middle+1, right)
        else:
            return helper(nums, target, left, middle-1)
    return helper(nums, target, 0, len(nums)-1)


print(binary_search_recursive([2, 3, 7, 9, 11, 23, 37, 81, 87, 89], 9))
