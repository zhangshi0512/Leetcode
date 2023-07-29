"""
1631. Path With Minimum Effort

You are a hiker preparing for an upcoming hike. 
You are given heights, a 2D array of size rows x columns, 
where heights[row][col] represents the height of cell (row, col). 
You are situated in the top-left cell, (0, 0), 
and you hope to travel to the bottom-right cell, (rows-1, columns-1) 
(i.e., 0-indexed). You can move up, down, left, or right, 
and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between 
two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to 
the bottom-right cell.

Input: heights = [[1,2,2],
                  [3,8,2],
                  [5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 
in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

Input: heights = [[1,2,3],
                  [3,8,4],
                  [5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 
in consecutive cells, which is better than route [1,3,5,3,5].

Input: heights = [[1,2,1,1,1],
                  [1,2,1,2,1],
                  [1,2,1,2,1],
                  [1,2,1,2,1],
                  [1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.

Constraints:

rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 10^6
"""


# 定义求最小努力路径的函数，输入是高度的二维列表，输出是最小的努力值
def minimumEffortPath(heights):
    # 定义有效性检查函数，输入是行和列，输出是该行和列是否在高度矩阵内
    def valid(row, col):
        return 0 <= row < m and 0 <= col < n

    # 定义检查函数，输入是努力值，输出是是否存在一条路径的最大努力值小于等于该努力值
    def check(effort):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 定义四个方向
        seen = {(0, 0)}  # 记录已经访问过的点
        stack = [(0, 0)]  # 记录待访问的点

        # 当还有待访问的点时
        while stack:
            row, col = stack.pop()  # 取出一个点
            # 如果这个点是目的地，说明找到了一条路径，返回True
            if (row, col) == (m-1, n-1):
                return True

            # 遍历四个方向
            for dx, dy in directions:
                # 计算下一个点的行和列
                next_row, next_col = row + dx, col + dy
                # 如果下一个点在高度矩阵内且没有访问过
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    # 如果从当前点到下一个点的努力值小于等于输入的努力值
                    if abs(heights[next_row][next_col] - heights[row][col]) <= effort:
                        seen.add((next_row, next_col))  # 记录下一个点已经访问过
                        stack.append((next_row, next_col))  # 将下一个点加入待访问的点列表

        # 如果遍历完所有点都没有找到一条路径，返回False
        return False

    m = len(heights)  # 高度矩阵的行数
    n = len(heights[0])  # 高度矩阵的列数
    # 设定努力值的搜索范围，最小为0，最大为高度矩阵中的最大值
    left = 0
    right = max(max(row) for row in heights)

    # 用二分搜索的方式搜索努力值
    while left <= right:
        mid = (left + right)//2  # 计算中间的努力值
        # 如果中间的努力值满足要求
        if check(mid):
            # 说明可以尝试更小的努力值，所以把搜索范围缩小到左半边
            right = mid - 1
        else:
            # 如果中间的努力值不满足要求，说明需要更大的努力值，所以把搜索范围扩大到右半边
            left = mid + 1

    # 最后返回能满足要求的最小努力值
    return left


heights1 = [[1, 2, 3],
            [3, 8, 4],
            [5, 3, 5]]

heights2 = [[1, 2, 3],
            [3, 8, 4],
            [5, 3, 5]]

heights3 = [[1, 2, 1, 1, 1],
            [1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1],
            [1, 1, 1, 2, 1]]

print(2, minimumEffortPath(heights1))
print(1, minimumEffortPath(heights2))
print(0, minimumEffortPath(heights3))
