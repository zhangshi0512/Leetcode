"""
2260. Minimum Consecutive Cards to Pick Up

You are given an integer array cards where cards[i] represents 
the value of the ith card. 
A pair of cards are matching if the cards have the same value.

Return the minimum number of consecutive cards you have to pick up 
to have a pair of matching cards among the picked cards. 
If it is impossible to have matching cards, return -1.

Example 1:

Input: cards = [3,4,2,3,4,7]
Output: 4
Explanation: We can pick up the cards [3,4,2,3] which contain 
a matching pair of cards with value 3. 
Note that picking up the cards [4,2,3,4] is also optimal.

Example 2:

Input: cards = [1,0,5,3]
Output: -1
Explanation: There is no way to pick up a set of consecutive cards 
that contain a pair of matching cards.

Constraints:

1 <= cards.length <= 10^5
0 <= cards[i] <= 10^6
"""
from collections import defaultdict

# defaultdict list to track all index
# T = O(n*m)
def minimumCardPickup(cards):
    # 如果每张卡的数值都不同，那么就无法找到一对匹配的卡，直接返回-1
    if len(set(cards)) == len(cards):
        return -1

    # 构建一个字典，key为卡的数值，value为该数值卡出现的位置列表
    card_dict = defaultdict(list)
    for i in range(len(cards)):
        card_dict[cards[i]].append(i)

    minNum = len(cards)
    # 遍历字典中的每一个值（位置列表）
    for value in card_dict.values():
        # 如果一种卡只出现一次，那么无法形成一对匹配的卡，我们忽略这种情况
        if len(value) > 1:
            # 对位置列表进行排序
            value.sort()
            # 计算任意两个连续出现的位置之间的最小距离（即最小的连续卡片数）
            for i in range(1, len(value)):
                if minNum > (value[i] - value[i-1] + 1):
                    minNum = value[i] - value[i-1] + 1

    return minNum

print(-1, minimumCardPickup([1,0,5,3]))
print(4, minimumCardPickup([3,4,2,3,4,7]))
print(3, minimumCardPickup([95, 11, 8, 65, 5, 86, 30, 27, 30, 73,
      15, 91, 30, 7, 37, 26, 55, 76, 60, 43, 36, 85, 47, 96, 6]))
print()

# dict approach only update distance
# T = O(n)
def minimumCardPickup2(cards):
    # 初始化字典，key为卡的数值，value为该数值卡最后一次出现的位置
    card_dict = {}
    # 初始化最小连续卡片数为卡片总数+1
    # 避免cards = [0,0]时的情况
    minNum = len(cards)+1 
    for i, card in enumerate(cards):
        # 如果这张卡已经出现过
        if card in card_dict:
            # 计算上次出现这张卡到这次出现这张卡之间的距离
            distance = i - card_dict[card] + 1
            # 更新最小连续卡片数
            minNum = min(minNum, distance)
        # 更新这张卡的最后出现位置
        card_dict[card] = i
    # 如果遍历完所有卡后，最小连续卡片数仍为卡片总数+1，
    # 说明没有一对匹配的卡，返回-1
    if minNum == len(cards)+1:
        return -1
    else:
        return minNum
    
print(-1, minimumCardPickup2([1,0,5,3]))
print(4, minimumCardPickup2([3,4,2,3,4,7]))
print(3, minimumCardPickup2([95, 11, 8, 65, 5, 86, 30, 27, 30, 73,
      15, 91, 30, 7, 37, 26, 55, 76, 60, 43, 36, 85, 47, 96, 6]))