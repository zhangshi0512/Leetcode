"""
Two players are playing a game of Tower Breakers! Player 1 always moves first, 
and both players always play optimally.The rules of the game are as follows:

Initially there are n towers.
Each tower is of height m.
The players move in alternating turns.
In each turn, a player can choose a tower of height x and reduce its height to y, 
where 1 <= y < x and y evenly divides x.
If the current player is unable to make a move, they lose the game.

Given the values of n and m, determine which player will win. 
If the first player wins, return 1. Otherwise, return 2.

Example:
n = 2
m = 6
There are 2 towers, each 6 units tall. Player 1 has a choice of two movies:
-remove 3 pieces from a tower to leave 3 as 6 modulo 3 = 0
-remove 5 pieces to leave 1.

Let Player 1 remove 3. Now the towers are 3 and 6 units tall.
Player 2 matches the move. Now the towers are both 3 units tall.

Now Player 1 has only one move.
Player 1 removes 2 pieces leaving 1. Towers are 1 and 2 units tall. 
Player 2 matches again. Towers are both 1 unit rall.
Player 1 has no move and loses. Return 2. 
"""

# 这个问题可以通过对博弈理论和游戏状态的分析来解决。

# 关键的洞察是，如果塔的高度为1，那么如果塔的数量是偶数，第一名玩家将会输（因为他们的每一步都可以被第二名玩家模仿），
# 如果塔的数量是奇数，第一名玩家将会赢（因为他们最终会把第二名玩家逼到无法行动的位置）。

# 如果塔的高度大于1，第一名玩家总是可以做出一个将塔的高度降低到1的动作，有效地将游戏转化为上述情况。
# 因此，如果塔的初始高度大于1，第一名玩家总是会赢，除非塔的数量是偶数，这种情况下第二名玩家可以模仿第一名玩家的动作。


def tower_breakers(n, m):
    # 如果塔的高度为1或者塔的数量是偶数，那么第二名玩家赢
    if m == 1 or n % 2 == 0:
        return 2
    # 否则，第一名玩家赢
    else:
        return 1


# 使用提供的示例测试函数
print(2, tower_breakers(2, 6))
print(2, tower_breakers(2, 2))
print(1, tower_breakers(1, 4))
