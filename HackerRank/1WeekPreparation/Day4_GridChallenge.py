"""
Given a square grid of characters in the range ascii[a-z], 
rearrange elements of each row alphabetically, ascending. 
Determine if the columns are also in ascending alphabetical order, top to bottom. 
Return 'YES' if they are or 'NO' if they are not.

Example
grid = ['abc', 'ade', 'efg']
The grid = [
['a', 'b', 'c'],
['a', 'd', 'e'],
['e', 'f', 'g']
]

The rows are already in alphabetical order. 
The columns a a e, b d f and c e g are also in alphabetical order, 
so the answer would be YES. 
Only elements within the same row can be rearranged. 
They cannot be moved to a different row.
"""


def gridChallenge(grid):
    # Make a 2d grid and sort each row
    new_grid = []
    for string in grid:
        char_list = list(string)  # Convert string to list of characters
        char_list.sort()  # Sort the list in-place
        new_grid.append(char_list)

    # Check if the grid is ascending order for all the columns and rows
    n = len(new_grid)
    # check row first:
    for char_list in new_grid:
        for i in range(1, len(char_list)):
            if char_list[i-1] > char_list[i]:
                return 'NO'

    # check column:
    for j in range(n-1):
        for k in range(len(new_grid[j])):
            if new_grid[j][k] > new_grid[j+1][k]:
                return 'NO'

    return 'YES'


print(gridChallenge(['eabcd', 'fghij', 'olkmn', 'trpqs', 'xywuv']))
