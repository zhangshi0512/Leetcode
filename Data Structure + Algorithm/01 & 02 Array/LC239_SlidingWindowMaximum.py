"""
239. Sliding Window Maximum

You are given an array of integers nums, 
there is a sliding window of size k which is 
moving from the very left of the array to the very right. 
You can only see the k numbers in the window. 
Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

 Example 2:

Input: nums = [1], k = 1
Output: [1]

Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length
"""

# Brute Force
# T = O(n^2)

from collections import deque


def MaxSlidingWindow(nums, k):
    windowMax = nums[0]
    recordMax = []

    for i in range(k-1, len(nums)):
        windowMax = max(nums[i-k+1:i+1])
        recordMax.append(windowMax)

    return recordMax


print([3, 3, 5, 5, 6, 7], MaxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
print([1], MaxSlidingWindow([1], 1))
print()
# Use a Deque
# T = O(n)


def MaxSlidingWindow2(nums, k):
    deq = deque()
    result = []

    for i in range(len(nums)):
        if deq and deq[0] < i - k + 1:
            deq.popleft()

        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()

        deq.append(i)

        if i >= k-1:
            result.append(nums[deq[0]])

    return result


print([3, 3, 5, 5, 6, 7], MaxSlidingWindow2([1, 3, -1, -3, 5, 3, 6, 7], 3))
print([1], MaxSlidingWindow2([1], 1))
print()

# Dynamic Sliding Window
# T = O(n)


def MaxSlidingWindow3(nums, k):
    n = len(nums)
    if n*k == 0:
        return []

    left, right = [0]*n, [0]*n
    left[0], right[-1] = nums[0], nums[-1]

    for i in range(1, n):
        if i % k == 0:
            left[i] = nums[i]
        else:
            left[i] = max(nums[i], left[i-1])

        j = n - i - 1
        if (j + 1) % k == 0:
            right[j] = nums[j]
        else:
            right[j] = max(nums[j], right[j+1])

    return [max(right[i], left[i + k - 1]) for i in range(n - k + 1)]


print([3, 3, 5, 5, 6, 7], MaxSlidingWindow3([1, 3, -1, -3, 5, 3, 6, 7], 3))
print([1], MaxSlidingWindow3([1], 1))
