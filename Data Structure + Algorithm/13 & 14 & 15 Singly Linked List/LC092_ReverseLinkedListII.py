"""
92. Reverse Linked List II

Given the head of a singly linked list and two integers left and right 
where left <= right, reverse the nodes of the list from position 
left to position right, and return the reversed list.

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n

Follow up: Could you do it in one pass?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head, left, right):
        # 创建一个dummy节点，让它指向head，使得链表从1开始
        dummy = ListNode(0)
        dummy.next = head
        # pre初始化为dummy
        pre = dummy

        # 将pre移动到需要翻转的区间的前一个位置
        for _ in range(left - 1):
            pre = pre.next

        # 定义一个指针，指向需要翻转的区间的第一个节点
        cur = pre.next
        # 然后就可以开始翻转了
        for _ in range(right - left):
            # 先把待翻转节点x的下一节点存起来
            next = cur.next
            # 然后让当前节点的下一节点指向要翻转节点的下一节点
            cur.next = next.next
            # 更新要翻转的节点的下一节点为pre的下一节点
            next.next = pre.next
            # 更新pre的下一节点为next
            pre.next = next
        return dummy.next
    
# 创建测试用例
def create_linked_list(lst):
    dummy = ListNode(0)
    ptr = dummy
    for i in lst:
        ptr.next = ListNode(i)
        ptr = ptr.next
    return dummy.next

def print_linked_list(head):
    ptr = head
    res = []
    while ptr:
        res.append(ptr.val)
        ptr = ptr.next
    return res

test_cases = [
    ([1,2,3,4,5], 2, 4, [1,4,3,2,5]),
    ([5], 1, 1, [5])
]

s = Solution()

for i, (lst, left, right, expt) in enumerate(test_cases):
    head = create_linked_list(lst)
    print(f"测试用例 {i + 1}:")
    print(f"预期输出: {expt}")
    print(f"实际输出: {print_linked_list(s.reverseBetween(head, left, right))}")
    print("-----------------------")

