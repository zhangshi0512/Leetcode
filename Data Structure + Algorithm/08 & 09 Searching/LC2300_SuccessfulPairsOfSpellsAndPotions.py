"""
2300. Successful Pairs of Spells and Potions

You are given two positive integer arrays spells and potions, 
of length n and m respectively, where spells[i] represents the strength 
of the ith spell and potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered 
successful if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of 
potions that will form a successful pair with the ith spell.

Example 1:

Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
Output: [4,0,3]
Explanation:
- 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
- 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
- 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
Thus, [4,0,3] is returned.

Example 2:

Input: spells = [3,1,2], potions = [8,5,8], success = 16
Output: [2,0,2]
Explanation:
- 0th spell: 3 * [8,5,8] = [24,15,24]. 2 pairs are successful.
- 1st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful. 
- 2nd spell: 2 * [8,5,8] = [16,10,16]. 2 pairs are successful. 
Thus, [2,0,2] is returned.

Constraints:

n == spells.length
m == potions.length
1 <= n, m <= 10^5
1 <= spells[i], potions[i] <= 10^5
1 <= success <= 10^10
"""

# 暴力解法 T = O(N^2)
def successfulPairs(spells, potions, success):
    m, n = len(spells), len(potions)
    res = [0] * min(m, n)

    # 如果咒语的数量小于或等于药剂的数量
    if len(res) == m:
        for i in range(m):
            for j in range(n):
                # 如果咒语和药剂的乘积大于或等于成功值，则成功对数加一
                if spells[i] * potions[j] >= success:
                    res[i] += 1

    # 如果咒语的数量大于药剂的数量
    else:
        for i in range(n):
            for j in range(m):
                # 如果咒语和药剂的乘积大于或等于成功值，则成功对数加一
                if spells[j] * potions[i] >= success:
                    res[i] += 1

    return res

# 优化解法，利用二分查找
def successfulPairs2(spells, potions, success):
    # 定义二分查找函数
    def binarySearch(arr, target):
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left+right)//2
            # 如果中间位置的值小于目标值，搜索范围缩小为右半部分
            if arr[mid] < target:
                left = mid + 1
            # 如果中间位置的值大于或等于目标值，搜索范围缩小为左半部分
            else:
                right = mid - 1

        return left

    ans = []
    # 对药剂数组进行排序
    potions.sort()
    m = len(potions)

    # 对咒语数组进行遍历
    for spell in spells:
        # 对每个咒语，利用二分查找找出能与之形成成功对的药剂的数量
        i = binarySearch(potions, success / spell)
        ans.append(m - i)

    return ans



print([4, 0, 3], successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7))
print([2, 0, 2], successfulPairs([3, 1, 2], [8, 5, 8], 16))
print()
print([4, 0, 3], successfulPairs2([5, 1, 3], [1, 2, 3, 4, 5], 7))
print([2, 0, 2], successfulPairs2([3, 1, 2], [8, 5, 8], 16))
