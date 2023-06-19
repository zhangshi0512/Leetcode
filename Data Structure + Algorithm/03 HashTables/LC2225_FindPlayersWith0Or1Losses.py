"""
2225. Find Players With Zero or One Losses

You are given an integer array matches where matches[i] = [winneri, loseri] indicates 
that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.
 

Example 1:

Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
Explanation:
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
Example 2:

Input: matches = [[2,3],[1,3],[5,4],[6,4]]
Output: [[1,2,5,6],[]]
Explanation:
Players 1, 2, 5, and 6 have not lost any matches.
Players 3 and 4 each have lost two matches.
Thus, answer[0] = [1,2,5,6] and answer[1] = [].
 

Constraints:

1 <= matches.length <= 105
matches[i].length == 2
1 <= winneri, loseri <= 105
winneri != loseri
All matches[i] are unique.
"""

# Brute Force: two dict approach
# T = O(nlogn)
# S = O(n)
def findWinners(matches):
    ans = [[], []]
    winner = {}
    loser = {}

    for match in matches:
        if match[0] in winner:
            winner[match[0]] += 1
        else:
            winner[match[0]] = 1

        if match[1] in loser:
            loser[match[1]] += 1
        else:
            loser[match[1]] = 1

    for w in winner:
        if not w in loser:
            ans[0].append(w)
    ans[0] = sorted(ans[0])

    for l in loser:
        if loser[l] == 1:
            ans[1].append(l)
    ans[1] = sorted(ans[1])

    return ans


print([[1, 2, 10], [4, 5, 7, 8]], findWinners([[1, 3], [2, 3], [3, 6],
      [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]))
print([[1, 2, 5, 6], []], findWinners([[2, 3], [1, 3], [5, 4], [6, 4]]))
print()

# defaultdict approach
# T = O(nlogn)
# S = O(n)
from collections import defaultdict

def findWinners2(matches):
    # 使用defaultdict简化代码
    losses = defaultdict(int) 
    winners = defaultdict(int)

    for w, l in matches:
        winners[w] += 1
        losses[l] += 1

    # 没有输过的玩家，即在输家字典中不存在的玩家
    no_losses = [player for player in winners.keys() if player not in losses]
    no_losses.sort()  # 按升序排序

    # 输过一次的玩家，即在输家字典中只出现一次的玩家，并且在赢家字典中也存在
    one_loss = [player for player, times in losses.items() if times == 1]
    one_loss.sort()  # 按升序排序

    return [no_losses, one_loss]

print([[1, 2, 10], [4, 5, 7, 8]], findWinners2([[1, 3], [2, 3], [3, 6],
      [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]))
print([[1, 2, 5, 6], []], findWinners2([[2, 3], [1, 3], [5, 4], [6, 4]]))
print()

# Counter approach
# T = O(nlogn)
# S = O(n)
from collections import Counter

def findWinners3(matches):
    # 使用Counter类计算每个玩家的输赛次数
    losses = Counter(loser for _, loser in matches)

    # 所有参赛的玩家
    players = set(winner for winner, _ in matches)

    # 没有输过的玩家，即在输家计数器中不存在的玩家
    no_losses = [player for player in players if player not in losses]
    no_losses.sort()  # 按升序排序

    # 输过一次的玩家，即在输家计数器中只出现一次的玩家
    one_loss = [player for player in players if losses[player] == 1]
    one_loss.sort()  # 按升序排序

    return [no_losses, one_loss]

print([[1, 2, 10], [4, 5, 7, 8]], findWinners3([[1, 3], [2, 3], [3, 6],
      [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]))
print([[1, 2, 5, 6], []], findWinners3([[2, 3], [1, 3], [5, 4], [6, 4]]))
print()

