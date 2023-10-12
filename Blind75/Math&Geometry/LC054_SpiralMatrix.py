"""
54. Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: 
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: 
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
    ]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""
# helper function to print matrix in square format


def print_matrix(matrix):
    for m in matrix:
        print(m)

# brute force solution


def spiralOrder_bruteforce(matrix):
    if not matrix:
        return []

    result = []
    m, n = len(matrix), len(matrix[0])
    visited = [[False] * n for _ in range(m)]

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    direction_idx = 0
    x, y = 0, 0

    for _ in range(m * n):
        result.append(matrix[x][y])
        visited[x][y] = True

        next_x, next_y = x + \
            directions[direction_idx][0], y + directions[direction_idx][1]

        if 0 <= next_x < m and 0 <= next_y < n and not visited[next_x][next_y]:
            x, y = next_x, next_y
        else:
            direction_idx = (direction_idx + 1) % 4
            x, y = x + directions[direction_idx][0], y + \
                directions[direction_idx][1]

    return result


# Test the brute force solution
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

output1 = spiralOrder_bruteforce(matrix1)
output2 = spiralOrder_bruteforce(matrix2)

print_matrix(matrix1)
print()
print(output1)
print()
print_matrix(matrix2)
print()
print(output2)
print()

# optimal solution


def spiralOrder_optimal(matrix):
    if not matrix:
        return []

    result = []
    m, n = len(matrix), len(matrix[0])

    left, right, top, bottom = 0, n - 1, 0, m - 1

    while left <= right and top <= bottom:
        # Traverse right
        for j in range(left, right + 1):
            result.append(matrix[top][j])

        # Traverse down
        for i in range(top + 1, bottom + 1):
            result.append(matrix[i][right])

        # Traverse left (only if there are more than one row)
        if top < bottom:
            for j in range(right - 1, left - 1, -1):
                result.append(matrix[bottom][j])

        # Traverse up (only if there are more than one column)
        if left < right:
            for i in range(bottom - 1, top, -1):
                result.append(matrix[i][left])

        left += 1
        right -= 1
        top += 1
        bottom -= 1

    return result


# Test the brute force solution
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

output1 = spiralOrder_optimal(matrix1)
output2 = spiralOrder_optimal(matrix2)

print_matrix(matrix1)
print()
print(output1)
print()
print_matrix(matrix2)
print()
print(output2)
print()
