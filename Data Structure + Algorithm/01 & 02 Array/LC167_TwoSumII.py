"""
167. Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted 
in non-decreasing order, find two numbers such that they add up to 
a specific target number. Let these two numbers be numbers[index1] 
and numbers[index2] where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by 
one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. 
You may not use the same element twice.

Your solution must use only constant extra space.

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]

Input: numbers = [2,3,4], target = 6
Output: [1,3]

Input: numbers = [-1,0], target = -1
Output: [1,2]

Constraints:

2 <= numbers.length <= 3 * 10^4
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
"""

# Two pointers
# T = O(n)


def twosumII(nums, k):
    ans = []
    left = 0
    right = len(nums)-1

    while left < right:
        if nums[left] + nums[right] == k:
            ans.append(left + 1)
            ans.append(right + 1)
            break

        elif nums[left] + nums[right] < k:
            left += 1

        else:
            right -= 1

    return ans


print([1, 2], twosumII([2, 7, 11, 15], 9))
print([1, 3], twosumII([2, 3, 4], 6))
print([1, 2], twosumII([-1, 0], -1))
