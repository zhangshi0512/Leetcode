"""
73. Set Matrix Zeroes

Given an m x n integer matrix matrix, if an element is 0, 
set its entire row and column to 0's.

You must do it in place.

Example 1:
Input: 
matrix = [
    [1,1,1],
    [1,0,1],
    [1,1,1]
    ]
Output: [
    [1,0,1],
    [0,0,0],
    [1,0,1]
    ]

Example 2:
Input: 
matrix = [
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]
    ]
Output: [
    [0,0,0,0],
    [0,4,5,0],
    [0,3,1,0]
    ]

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-2^31 <= matrix[i][j] <= 2^31 - 1

Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""
# helper function to print matrix in square format


def print_matrix(matrix):
    for m in matrix:
        print(m)

# brute force solution


def setZeroes_bruteforce(matrix):
    m, n = len(matrix), len(matrix[0])
    rows, cols = set(), set()

    # Identify rows and columns that should be zeroed out
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    # Zero out identified rows and columns
    for i in range(m):
        for j in range(n):
            if i in rows or j in cols:
                matrix[i][j] = 0


# Test the brute force solution
matrix1 = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

matrix2 = [
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]

print("brute force solution:")
print_matrix(matrix1)
print()
setZeroes_bruteforce(matrix1)
print_matrix(matrix1)
print()
print_matrix(matrix2)
print()
setZeroes_bruteforce(matrix2)
print_matrix(matrix2)
print()


def setZeroes_optimal(matrix):
    m, n = len(matrix), len(matrix[0])
    first_row_zero, first_col_zero = False, False

    # Check if first row and first column should be zeroed
    for i in range(m):
        if matrix[i][0] == 0:
            first_col_zero = True
            break

    for j in range(n):
        if matrix[0][j] == 0:
            first_row_zero = True
            break

    # Use the first row and column as markers
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Zero out based on markers
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Zero out first row and column if needed
    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0

    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0


# Test the optimal solution
matrix1 = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

matrix2 = [
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]

print("optimal solution:")
print_matrix(matrix1)
print()
setZeroes_optimal(matrix1)
print_matrix(matrix1)
print()
print_matrix(matrix2)
print()
setZeroes_optimal(matrix2)
print_matrix(matrix2)
