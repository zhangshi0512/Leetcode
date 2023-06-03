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

def max_area_optimum(array):
    left = 0
    right = len(array)-1
    max_area=0
    while(left<right):
        area = min(array[left], array[right]) * (right - left)
        max_area = max(area,max_area)
        if array[left]<array[right]:
            left +=1
        else:
            right -= 1
    return max_area

print(max_area_optimum([3,7,5,6,8,4]))
