"""
A queue is an abstract data type that maintains the order in which 
elements were added to it, allowing the oldest elements to be removed 
from the front and new elements to be added to the rear. 

This is called a First-In-First-Out (FIFO) data structure because 
the first element added to the queue (i.e., the one that has been waiting 
the longest) is always the first one to be removed.

A basic queue has the following operations:

Enqueue: add a new element to the end of the queue.
Dequeue: remove the element from the front of the queue and return it.
In this challenge, you must first implement a queue using two stacks. 
Then process q queries, where each query is one of the following 3 types:

1 x: Enqueue element x into the end of the queue.
2: Dequeue the element at the front of the queue.
3: Print the element at the front of the queue.

Input Format

The first line contains a single integer, q, denoting the number of queries.
Each line i of the q subsequent lines contains a single query in the form 
described in the problem statement above. All three queries start with an integer 
denoting the query type, but only query 1 is followed by an additional 
space-separated value, x, denoting the value to be enqueued.

Constraints:
 1 <= q <= 10^5
 1 <= type <= 3
 1 <= |x| <= 10^9
 it is guaranteed that a valid answer always exists for each query of type 3.


Output Format: 
For each query of type 3, print the value of the element at the front of the queue on a new line.

Sample Input:
STDIN   Function
-----   --------
10      q = 10 (number of queries)
1 42    1st query, enqueue 42
2       dequeue front element
1 14    enqueue 42
3       print the front element
1 28    enqueue 28
3       print the front element
1 60    enqueue 60
1 78    enqueue 78
2       dequeue front element
2       dequeue front element

Sample Output:
14
14
"""
# 关键步骤：
# 使用两个栈，stack1 和 stack2。
# 当向队列中加入元素时，直接将其压入 stack1。
# 当从队列的前端移除元素时：
# 如果 stack2 为空，将 stack1 中的所有元素弹出并压入 stack2。
# 然后，从 stack2 弹出顶部元素。
# 如果想获取队列的前端元素：
# 如果 stack2 不为空，stack2 的顶部元素就是前端元素。
# 如果 stack2 为空，需要将 stack1 中的所有元素转移到 stack2，然后 stack2 的顶部元素就是前端元素。


class QueueUsingTwoStacks:
    def __init__(self):
        # 初始化两个栈
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        # 入队操作：将元素压入stack1
        self.stack1.append(x)

    def dequeue(self):
        # 如果stack2为空，则从stack1转移元素到stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def get_front(self):
        # 如果stack2为空，则从stack1转移元素到stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        # 返回stack2的顶部元素
        return self.stack2[-1]


if __name__ == "__main__":
    # 输入查询次数
    q = int(input().strip())
    queue = QueueUsingTwoStacks()

    for _ in range(q):
        query = list(map(int, input().strip().split()))

        # 根据查询类型执行操作
        if query[0] == 1:  # 入队
            queue.enqueue(query[1])
        elif query[0] == 2:  # 出队
            queue.dequeue()
        else:  # 打印队列的前端元素
            print(queue.get_front())
