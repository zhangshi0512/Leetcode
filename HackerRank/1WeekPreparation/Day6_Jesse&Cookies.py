"""
Jesse loves cookies and wants the sweetness of some cookies to be greater than value . 
To do this, two cookies with the least sweetness are repeatedly mixed. 
This creates a special combined cookie with:

sweetness = ( 1 x Least sweet cookie + 2 x 2nd Least sweet cookie ).

This occurs until all the cookies have a sweetness >= k.

Given the sweetness of a number of cookies, determine the minimum number of operations required.

If it is not possible, return -1.

Example
k = 9 
A = [2,7,3,6,4,6]
The smallest values are 2, 3.
Remove them then return 2 + 2 x 3 = 8 to the array. 
Now A = [8,7,6,4,6]
Remove 4, 6 and return 4 + 2 x 6 = 16 to the array.
Now A = [16,8,7,6]
Remove 6, 7 and return 6 + 2 x 7 = 20 to the array.
Now A = [20,16,8,7]
Remove 7, 8 and return 7 + 2 x 8 = 23 to the array.
Now A = [23, 20, 16]

All values >= k = 9 so the process stops after 4 iterations.
Return 4. 

Function Description
Complete the cookies function in the editor below.

cookies has the following parameters:

int k: the threshold value
int A[n]: an array of sweetness values
Returns

int: the number of iterations required or -1.

Input Format

The first line has two space-separated integers, n and k, the size of A and the minimum required sweetness respectively.

The next line contains n space-separated integers, A[i].

Constraints
1 <= n <= 10^6
0 <= k <= 10^9
0 <= A[i] <= 10^6

Sample Input

STDIN               Function
-----               --------
6 7                 A[] size n = 6, k = 7
1 2 3 9 10 12       A = [1, 2, 3, 9, 10, 12]

Sample Output

2
"""

# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

import heapq


def cookies(k, A):
    # Convert the list into a min-heap
    heapq.heapify(A)

    # Initialize a counter for the operations
    operations = 0

    # While the smallest cookie is less than k and there are at least 2 cookies left
    while len(A) > 1 and A[0] < k:
        # Pop the two least sweet cookies
        least_sweet = heapq.heappop(A)
        second_least_sweet = heapq.heappop(A)

        # Combine the cookies and push the new cookie into the heap
        combined_sweetness = least_sweet + 2 * second_least_sweet
        heapq.heappush(A, combined_sweetness)

        # Increase the operations counter
        operations += 1

    # Check if all cookies have sweetness >= k
    if A[0] < k:
        return -1
    else:
        return operations


# Test the function with the given sample
sample_input = (7, [1, 2, 3, 9, 10, 12])
print(cookies(*sample_input))
