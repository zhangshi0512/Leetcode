"""
53. Maximum Subarray

Given an integer array nums, find the 
subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
"""

def maxSubArray(nums):
    # 初始化当前子数组的最大和为数组的第一个元素
    max_ending_here = nums[0]
    # 初始化全局最大子数组的和为数组的第一个元素
    max_ending_so_far = nums[0]
    
    # 遍历数组中的每一个元素，注意我们从第二个元素开始，因为第一个元素已经被计算过了
    for num in nums[1:]:
        # 对于每一个元素，我们都计算以该元素结尾的最大子数组和，
        # 它可以是该元素本身，或者是该元素加上前面的子数组和（如果前面的子数组和是正数的话）
        max_ending_here = max(num, max_ending_here + num)
        
        # 更新全局最大子数组和
        max_ending_so_far = max(max_ending_so_far, max_ending_here)
        
    # 返回全局最大子数组和
    return max_ending_so_far

print(6, maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(23, maxSubArray([5,4,-1,7,8]))
print(1, maxSubArray([1]))