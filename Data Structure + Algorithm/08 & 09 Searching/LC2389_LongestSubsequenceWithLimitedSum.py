"""
2389. Longest Subsequence With Limited Sum

You are given an integer array nums of length n, 
and an integer array queries of length m.

Return an array answer of length m where answer[i] is 
the maximum size of a subsequence that you can take from nums 
such that the sum of its elements is less than or equal to queries[i].

A subsequence is an array that can be derived from another array 
by deleting some or no elements without changing the order of the 
remaining elements.

Input: nums = [4,5,2,1], queries = [3,10,21]
Output: [2,3,4]
Explanation: We answer the queries as follows:
- The subsequence [2,1] has a sum less than or equal to 3. 
It can be proven that 2 is the maximum size of such a subsequence, 
so answer[0] = 2.
- The subsequence [4,5,1] has a sum less than or equal to 10. 
It can be proven that 3 is the maximum size of such a subsequence, 
so answer[1] = 3.
- The subsequence [4,5,2,1] has a sum less than or equal to 21. 
It can be proven that 4 is the maximum size of such a subsequence, 
so answer[2] = 4.

Input: nums = [2,3,4,5], queries = [1]
Output: [0]
Explanation: The empty subsequence is the only subsequence that has 
a sum less than or equal to 1, so answer[0] = 0.

Constraints:

n == nums.length
m == queries.length
1 <= n, m <= 1000
1 <= nums[i], queries[i] <= 10^6
"""


def answerQueries(nums, queries):
    nums.sort()  # 将数组 nums 排序
    prefix_sum = [0]  # 前缀和数组，用于计算子序列的和
    for num in nums:
        prefix_sum.append(prefix_sum[-1] + num)  # 计算前缀和

    ans = []
    for query in queries:
        left = 0  # 左指针
        right = len(nums)  # 右指针，初始位置为 nums 的末尾
        while left < right:
            mid = (left + right + 1) // 2  # 二分查找的中间位置
            if prefix_sum[mid] <= query:
                left = mid  # 若 mid 位置的前缀和小于等于 query，则更新左指针
            else:
                right = mid - 1  # 否则，更新右指针
        ans.append(left)  # 记录满足条件的最大子序列长度

    return ans


print([2, 3, 4], answerQueries([4, 5, 2, 1], [3, 10, 21]))
print([0], answerQueries([2, 3, 4, 5], [1]))
