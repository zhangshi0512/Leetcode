"""
1004. Max Consecutive Ones III

Given a binary array nums and an integer k, 
return the maximum number of consecutive 1's in the array 
if you can flip at most k 0's.

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Constraints:

1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
0 <= k <= nums.length
"""

# 在这个问题中，我们需要找到可以通过翻转最多k个0得到的最长的连续1的序列。
# 这就需要我们维护一个滑动窗口，使得窗口内0的数量不超过k。

# 我们从数组的左端开始，逐步向右移动窗口的右端。
# 如果添加的新元素是0，那么我们需要减少我们可以翻转的0的数量k。
# 当k小于0时，我们需要移动窗口的左端，直到窗口内0的数量不超过k。
# 我们每次移动窗口的右端时，都更新窗口的长度。

# 这个滑动窗口始终维护了满足条件（窗口内最多有k个0）的最大窗口，
# 所以最后窗口的长度就是可以通过翻转最多k个0得到的最长的连续1的序列的长度。

def findMaxConsecutiveOnesIII(nums, k):
    left = 0
    for right in range(len(nums)): # 逐步向右移动窗口的右端
        if nums[right] == 0: # 如果添加的新元素是0
            k -= 1 # 减少我们可以翻转的0的数量k
        if k < 0:  # 如果k小于0
            if nums[left] == 0: # 如果左端的元素是0
                k += 1 # 增加我们可以翻转的0的数量k
            left += 1 # 向右移动窗口的左端
    return right - left + 1 # 返回窗口的长度


print(6, findMaxConsecutiveOnesIII([1,1,1,0,0,0,1,1,1,1,0], 2))
print(10, findMaxConsecutiveOnesIII([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))