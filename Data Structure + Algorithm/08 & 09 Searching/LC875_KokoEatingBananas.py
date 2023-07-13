"""
875. Koko Eating Bananas

Koko loves to eat bananas. There are n piles of bananas, 
the ith pile has piles[i] bananas. 
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. 
Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
If the pile has less than k bananas, 
she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas 
before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Input: piles = [3,6,7,11], h = 8
Output: 4

Input: piles = [30,11,23,4,20], h = 5
Output: 30

Input: piles = [30,11,23,4,20], h = 6
Output: 23

Constraints:

1 <= piles.length <= 10^4
piles.length <= h <= 10^9
1 <= piles[i] <= 10^9
"""

from math import ceil


def minEatingSpeed(piles, h):
    # 定义检查函数，输入是速度，输出是是否能在规定时间内吃完
    def check(k):
        hours = 0
        # 遍历每一堆香蕉
        for bananas in piles:
            # 计算每一堆香蕉需要的时间，用香蕉数量除以吃香蕉的速度，然后向上取整
            hours += ceil(bananas / k)
        # 如果总时间小于等于规定的时间，那么这个速度是可以的
        return hours <= h

    # 设定速度的搜索范围，最小为1（每小时最少吃一个香蕉），最大为所有堆中最大的香蕉数量
    left = 1
    right = max(piles)
    # 用二分搜索的方式搜索速度
    while left <= right:
        mid = (left + right) // 2  # 计算中间速度
        # 如果中间速度满足要求
        if check(mid):
            # 说明可以尝试更小的速度，所以把搜索范围缩小到左半边
            right = mid - 1
        else:
            # 如果中间速度不满足要求，说明需要更大的速度，所以把搜索范围扩大到右半边
            left = mid + 1
    # 最后返回能满足要求的最小速度
    return left


print(4, minEatingSpeed([3, 6, 7, 11], 8))
print(30, minEatingSpeed([30, 11, 23, 4, 20], 5))
print(23, minEatingSpeed([30, 11, 23, 4, 20], 6))
