"""
2248. Intersection of Multiple Arrays

Given a 2D integer array nums where nums[i] 
is a non-empty array of distinct positive integers, 
return the list of integers that are present in each array of nums 
sorted in ascending order.

Example 1:

Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
Output: [3,4]
Explanation: 
The only integers present in each of 
nums[0] = [3,1,2,4,5], nums[1] = [1,2,3,4], and nums[2] = [3,4,5,6] 
are 3 and 4, so we return [3,4].

Example 2:

Input: nums = [[1,2,3],[4,5,6]]
Output: []
Explanation: 
There does not exist any integer present both in nums[0] and nums[1], 
so we return an empty list [].

Constraints:

1 <= nums.length <= 1000
1 <= sum(nums[i].length) <= 1000
1 <= nums[i][j] <= 1000
All the values of nums[i] are unique.
"""

# Brute Force
# T = O(n) for count
# T = O(MlogM) for sort
# S = O(n * m)

def intersection(nums):
    ans = []
    n = len(nums)
    counts = {}

    for arr in nums:
        for x in arr:
            if not x in counts:
                counts[x] = 1
            else:
                counts[x] += 1

    for key in counts.keys():
        if counts[key] == n:
            ans.append(key)

    return sorted(ans)


print(intersection([[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]))
print(intersection([[1, 2, 3], [4, 5, 6]]))
print()


def intersection2(nums):
    # 使用set操作将第一个列表转化为集合
    # Convert the first list to a set using set operation
    res = set(nums[0])
    
    # 遍历剩余的列表
    # Iterate over the rest of the lists
    for lst in nums[1:]:
        # 计算当前集合与新列表的交集，并更新结果集合
        # Calculate the intersection of the current set with the new list and update the result set
        res &= set(lst)
    
    # 返回排序后的结果
    # Return the sorted result
    return sorted(res)

print(intersection2([[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]))
print(intersection2([[1, 2, 3], [4, 5, 6]]))