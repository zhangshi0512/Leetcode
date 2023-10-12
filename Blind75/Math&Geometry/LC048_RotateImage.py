"""
48. Rotate Image

You are given an n x n 2D matrix representing an image, 
rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to 
modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Input: 
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

Output: [
    [7,4,1],
    [8,5,2],
    [9,6,3]
    ]

Example 2:

Input: 
matrix = [
    [5,1,9,11],
    [2,4,8,10],
    [13,3,6,7],
    [15,14,12,16]
    ]

Output: [
    [15,13,2,5],
    [14,3,4,1],
    [12,6,8,9],
    [16,7,10,11]
    ]

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""
# helper function to print matrix in square format


def print_matrix(matrix):
    for m in matrix:
        print(m)


# brute force solution
def rotate_bruteforce(matrix):
    n = len(matrix)
    # Create a copy of the matrix
    matrix_copy = [[0] * n for _ in range(n)]

    # Place the elements in their rotated positions in the copy
    for i in range(n):
        for j in range(n):
            matrix_copy[j][n - 1 - i] = matrix[i][j]

    # Copy back the values to the original matrix
    for i in range(n):
        for j in range(n):
            matrix[i][j] = matrix_copy[i][j]


# Test the brute force solution
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]

print_matrix(matrix1)
print()
rotate_bruteforce(matrix1)

print_matrix(matrix1)
print()
print_matrix(matrix2)
print()
rotate_bruteforce(matrix2)

print_matrix(matrix2)
print()


def rotate_optimal(matrix):
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]


# Test the optimal solution
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]

print_matrix(matrix1)
print()
rotate_optimal(matrix1)

print_matrix(matrix1)
print()
print_matrix(matrix2)
print()
rotate_optimal(matrix2)

print_matrix(matrix2)
print()
