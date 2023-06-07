"""
713. Subarray Product Less Than K

Given an array of integers nums and an integer k, 
return the number of contiguous subarrays where 
the product of all the elements in the subarray is strictly less than k.

Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Example 2:

Input: nums = [1,2,3], k = 0
Output: 0

Constraints:

1 <= nums.length <= 3 * 104
1 <= nums[i] <= 1000
0 <= k <= 106
"""

def numSubarrayProductLessThanK(nums, k):
    # 如果k小于或等于1，我们直接返回0，因为没有子数组的乘积会小于1
    if k <= 1:
        return 0
    # 如果数组长度为1，我们需要检查该元素是否小于k
    if len(nums) == 1:
        if nums[0] < k:
            return 1
        else:
            return 0
        
    ans = left = 0 # 初始化答案和滑动窗口的左边界
    curr = 1 # 初始化当前子数组的乘积
    for right in range(len(nums)): # 遍历整个数组，此处right是滑动窗口的右边界
        curr *= nums[right] # 将右边界的元素乘入当前子数组的乘积中
        # 当当前子数组的乘积大于等于k时，我们需要移动滑动窗口的左边界
        while curr >= k:
            curr /= nums[left] # 将左边界的元素从当前子数组的乘积中除去
            left += 1 # 左边界右移

        # 现在，从左边界到右边界的所有子数组都是满足条件的，
        # 所以我们将这些子数组的数量加入答案中
        ans += right - left + 1
    
    return ans

print(8, numSubarrayProductLessThanK([10,5,2,6], 100))
print(0, numSubarrayProductLessThanK([1,2,3], 0))