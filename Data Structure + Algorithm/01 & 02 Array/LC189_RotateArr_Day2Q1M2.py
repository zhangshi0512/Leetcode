"""
189. Rotate Array

Given an integer array nums, 
rotate the array to the right by k steps, 
where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
"""

def reverse(array,start,end):
    while(start<end):
        array[start],array[end] = array[end], array[start]
        start +=1
        end -=1
    return array

def rotate_array(array,k):
    k= k % len(array)
    reverse(array, 0, len(array)-1)
    reverse(array, 0, k-1)
    reverse(array, k, len(array)-1)
    return array

print(rotate_array([1,2,3,4,5],3))
