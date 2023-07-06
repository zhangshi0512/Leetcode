"""
74. Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""


def searchMatrix(matrix, target):
    # 获取矩阵的行数和列数
    m, n = len(matrix), len(matrix[0])
    # 设定搜索的范围
    left, right = 0, m * n - 1

    # 二分查找的主循环
    while left <= right:
        # 计算中间位置
        mid = (left + right) // 2
        # 计算中间位置对应的行和列
        row = mid // n
        col = mid % n
        # 获取中间位置的值
        num = matrix[row][col]

        # 如果找到目标值，返回 True
        if num == target:
            return True

        # 如果中间位置的值小于目标值，搜索范围缩小为右半部分
        if num < target:
            left = mid + 1
        # 如果中间位置的值大于目标值，搜索范围缩小为左半部分
        else:
            right = mid - 1

    # 如果没有找到目标值，返回 False
    return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]

print(True, searchMatrix(matrix, 3))
print(False, searchMatrix(matrix, 13))
