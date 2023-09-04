"""
You have an infinite number of 4 types of lego blocks of sizes given as (depth x height x width):

d	h	w
1	1	1
1	1	2
1	1	3
1	1	4
Using these blocks, you want to make a wall of height m and width n. Features of the wall are:

- The wall should not have any holes in it.
- The wall you build should be one solid structure, so there should not be a straight vertical break across all rows of bricks.
- The bricks must be laid horizontally.

How many ways can the wall be built?

Example:
n = 2
m = 3
The height is 2 and the width is 3. 
These are not all of the valid permutations. There are 9 valid permutations in all.

Function Description

Complete the legoBlocks function in the editor below.

legoBlocks has the following parameter(s):

int n: the height of the wall
int m: the width of the wall
Returns
- int: the number of valid wall formations modulo (10^9 + 7)

Input Format

The first line contains the number of test cases t.

Each of the next t lines contains two space-separated integers n and m.

Constraints
1 <= t <= 100
1 <= n, m <= 1000

Sample Input
STDIN   Function
-----   --------
4       t = 4
2 2     n = 2, m = 2
3 2     n = 3, m = 2
2 3     n = 2, m = 3
4 4     n = 4, m = 4

Sample Output
3  
7  
9  
3375

Explanation

For the first case, we can have:
3 mod (10^9 + 7) = 3
For the second case, each row of the wall can contain either two blocks of width 1, or one block of width 2. 
However, the wall where all rows contain two blocks of width 1 is not a solid one as it can be divided vertically. 
Thus, the number of ways is 2 x 2 x 2 - 1 = 7 and 7 mod (10^9 + 7) = 7.
"""
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#


def legoBlocks(n, m):
    mod = 10**9 + 7

    # Step 1: Calculate number of ways to form a row of width w
    ways_single_row = [0] * (m+1)
    ways_single_row[0] = 1
    for width in range(1, m+1):
        for block_width in range(1, 5):
            if width - block_width >= 0:
                ways_single_row[width] += ways_single_row[width - block_width]
                ways_single_row[width] %= mod

    # Precompute power values for optimization
    power_memo = {}

    def mod_pow(base, exponent):
        if (base, exponent) in power_memo:
            return power_memo[(base, exponent)]
        result = pow(base, exponent, mod)
        power_memo[(base, exponent)] = result
        return result

    # Step 2: Calculate number of ways to form n such rows without any constraints
    # total_ways[i] gives number of ways to form walls of width i without any constraints
    total_ways = [1]
    for width in range(1, m+1):
        ways = mod_pow(ways_single_row[width], n)
        total_ways.append(ways)

    # Step 3: Calculate number of ways that result in walls with vertical holes
    for width in range(1, m+1):
        for i in range(1, width):
            total_ways[width] -= total_ways[i] * \
                mod_pow(ways_single_row[width - i], n)
            total_ways[width] = (total_ways[width] + mod) % mod

    return total_ways[m]


# Test the function with the provided sample test cases
test_cases = [(2, 2), (3, 2), (2, 3), (4, 4)]
results = [legoBlocks(n, m) for n, m in test_cases]
print(results)
