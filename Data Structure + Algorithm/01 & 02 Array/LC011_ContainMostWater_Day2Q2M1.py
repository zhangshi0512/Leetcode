"""
11. Container With Most Water

You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints 
of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, 
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

Input: height = [1,1]
Output: 1

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""

def max_area(array):
    max_area = 0
    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            area = min(array[i],array[j])*(j-i)
            max_area = max(max_area,area)
    return max_area


print(max_area([3,7,5,6,8,4]))