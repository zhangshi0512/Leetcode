"""
33. Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated 
at an unknown pivot index k (1 <= k < nums.length) such that the 
resulting array is 
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] 
(0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 
and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, 
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:

Input: nums = [1], target = 0
Output: -1

Constraints:

1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-10^4 <= target <= 10^4
"""


def search_rotated_sorted_array(nums, target):
    # 设定左右边界
    left, right = 0, len(nums) - 1
    while left <= right:
        # 计算中间索引
        mid = (left + right) // 2
        # 如果中间的值就是目标值，直接返回
        if nums[mid] == target:
            return mid
        # 如果左边的值小于等于中间的值，说明左边是有序的
        if nums[left] <= nums[mid]:
            # 如果目标值在左边的范围内
            if nums[left] <= target < nums[mid]:
                # 使得搜索范围缩小到左半部分
                right = mid - 1
            else:
                # 否则，搜索范围转到右半部分
                left = mid + 1
        else:
            # 如果右边是有序的
            # 如果目标值在右边的范围内
            if nums[mid] < target <= nums[right]:
                # 使得搜索范围缩小到右半部分
                left = mid + 1
            else:
                # 否则，搜索范围转到左半部分
                right = mid - 1
    # 如果没有找到目标值，返回-1
    return -1


print(search_rotated_sorted_array([7, 8, 1, 2, 3, 4, 5, 6], 3))
