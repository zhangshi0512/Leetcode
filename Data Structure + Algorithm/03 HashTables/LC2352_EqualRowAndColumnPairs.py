"""
2352. Equal Row and Column Pairs

Given a 0-indexed n x n integer matrix grid, 
return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal 
if they contain the same elements in the same order (i.e., an equal array).

Example 1:

Input: grid = [
    [3,2,1],
    [1,7,6],
    [2,7,7]
    ]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

Example 2:

Input: grid = [
    [3,1,2,2],
    [1,4,4,5],
    [2,4,2,2],
    [2,4,2,2]
    ]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
"""
from collections import defaultdict


def equalPairs(grid):
    # 定义一个函数将数组转换为元组，以便将其用作字典的键
    def convert_to_key(arr):
        return tuple(arr)

    # 定义一个字典用于存储行数据，键是行数据，值是行索引
    row_dic = defaultdict(list)
    for i, row in enumerate(grid):
        row_dic[convert_to_key(row)].append(i)

    # 定义一个字典用于存储列数据，键是列数据，值是列索引
    col_dic = defaultdict(list)
    for col in range(len(grid[0])):
        curr_col = []
        for row in range(len(grid)):
            curr_col.append(grid[row][col])
        col_dic[convert_to_key(curr_col)].append(col)

    # 计算相同的行和列的配对数量
    ans = 0
    for arr in row_dic:
        if arr in col_dic:
            ans += len(row_dic[arr]) * len(col_dic[arr])

    return ans


grid1 = [
    [3, 2, 1],
    [1, 7, 6],
    [2, 7, 7]
]

grid2 = [
    [3, 1, 2, 2],
    [1, 4, 4, 5],
    [2, 4, 2, 2],
    [2, 4, 2, 2]
]

print(1, equalPairs(grid1))
print(3, equalPairs(grid2))
