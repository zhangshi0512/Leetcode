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
