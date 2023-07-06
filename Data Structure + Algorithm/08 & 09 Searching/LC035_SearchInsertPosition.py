"""
35. Search Insert Position

Given a sorted array of distinct integers and a target value, 
return the index if the target is found. 

If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints:

1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums contains distinct values sorted in ascending order.
-10^4 <= target <= 10^4
"""

def searchInsert(nums, target):
    # 定义二分查找函数，查找目标值在数组中的位置
    def binarySearch(arr, target):
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            # 如果找到目标值，返回其在数组中的位置
            if arr[mid] == target:
                return mid
            # 如果中间位置的值小于目标值，搜索范围缩小为右半部分
            if arr[mid] < target:
                left = mid + 1
            # 如果中间位置的值大于目标值，搜索范围缩小为左半部分
            else:
                right = mid - 1

        # 如果没有找到目标值，返回-1
        return -1

    # 定义二分查找函数，查找目标值应该插入的位置
    def binarySearch2(arr, target):
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            # 如果找到目标值，返回其在数组中的位置
            if arr[mid] == target:
                return mid
            # 如果中间位置的值小于目标值，搜索范围缩小为右半部分
            if arr[mid] < target:
                left = mid + 1
            # 如果中间位置的值大于目标值，搜索范围缩小为左半部分
            else:
                right = mid - 1

        # 如果没有找到目标值，返回其应该插入的位置
        return right + 1

    # 先用第一个二分查找函数尝试查找目标值
    index = binarySearch(nums, target)
    # 如果没有找到目标值
    if index == -1:
        # 使用第二个二分查找函数找到目标值应该插入的位置
        return binarySearch2(nums, target)
    else:
        # 如果找到目标值，返回其在数组中的位置
        return index



print(2, searchInsert([1, 3, 5, 6], 5))
print(1, searchInsert([1, 3, 5, 6], 2))
print(4, searchInsert([1, 3, 5, 6], 7))
print(0, searchInsert([1, 3, 5, 6], 0))
