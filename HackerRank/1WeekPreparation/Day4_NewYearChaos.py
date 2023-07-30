"""
It is New Year's Day and people are in line for the Wonderland rollercoaster ride. 
Each person wears a sticker indicating their initial position in the queue from 1 to n. 
Any person can bribe the person directly in front of them to swap positions, 
but they still wear their original sticker. One person can bribe at most two others.

Determine the minimum number of bribes that took place to get to a given queue order. 
Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.

Example:
q refers to the input list for your function parameter,
o only provided as original list for reference purpose.

q = [1,2,3,5,4,6,7,8]
o = [1,2,3,4,5,6,7,8]
If person 5 bribes person 4, the queue will look like: [1,2,3,5,4,6,7,8]. Only 1 bribe is required, print 1.

q = [1,2,5,3,4,6,7,8]
o = [1,2,3,4,5,6,7,8]
If person 5 bribes person 4 and also person 3, we got the queue order above. So 2 bribes are required, print 2.

q = [1,2,5,3,4,6,8,7]
o = [1,2,3,4,5,6,7,8]
If person 5 bribes person 4 and also person 3, person 8 bribes person 7, we got the queue order above.
So 3 bribes are required, print 3.

q = [4,1,2,3]
o = [1,2,3,4]
Person 4 has to bribe 3 people to get to the current position. Print 'Too chaotic'.
"""

###
# 在这段代码中，我们首先用n表示队列中的人数，并初始化count用于计算贿赂总数。
# 然后，我们通过使用一个for循环遍历队列中的每个人。
# 在循环中，我们使用条件q[i] - (i + 1) > 2来检查是否有人进行了超过两个的贿赂。
# 如果有，我们输出"Too chaotic"并立即返回，因为这样的队列是无效的。
# 接着，在嵌套的for循环中，我们检查在当前位置之前的所有人。
# 对于每个人，我们通过条件q[j] > q[i]来判断是否有人贿赂了当前的人。
# 如果是这样，我们将count增加1，表示发生了一次贿赂。
# 最后，我们打印输出count，它代表了没有超过两次贿赂的总次数。

# 现在，函数会正确地计算贿赂的次数，并在有人贿赂超过两个人的情况下输出"Too chaotic"。
###


def minimumBribes(q):
    n = len(q)
    count = 0

    # 检查是否有人进行了贿赂，通过比较贴纸上的位置和索引
    for i in range(n):
        # 如果某人贿赂了超过两个人，输出"Too chaotic"
        if q[i] - (i + 1) > 2:
            print('Too chaotic')
            return

        # 计算进行贿赂的总次数，通过检查他们移动的位置数量
        # q[i]：这表示当前位置i上的人的原始位置。
        # 例如，如果q[i]为3，则表示原始排队时，此人排在第3个位置。
        # q[i] - 2：我们从q[i]中减去2，以找到可能的起始位置。
        # 这是因为一个人可以进行最多两次贿赂，所以他的最终位置至多比原始位置向前移动两个位置。
        # max(0, q[i] - 2)：我们用max函数取这两个值中较大的一个。
        # 这是为了确保起始位置不会小于0，因为负数索引是无效的。
        # 综上所述，range(max(0, q[i] - 2), i)会生成一个范围，从可能的起始位置（不小于0）开始，一直到当前位置i（不包括i）。
        # 这样，我们就能在循环中检查在当前位置之前的所有人是否进行了贿赂。
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                count += 1

    print(count)


q = [1, 2, 3, 5, 4, 6, 7, 8]
minimumBribes(q)  # Output: 1

q = [1, 2, 5, 3, 4, 6, 7, 8]
minimumBribes(q)  # Output: 2

q = [1, 2, 5, 3, 4, 6, 8, 7]
minimumBribes(q)  # Output: 3

q = [4, 1, 2, 3]
minimumBribes(q)  # Output: Too chaotic
