"""
203. Remove Linked List Elements

Given the head of a linked list and an integer val, 
remove all the nodes of the linked list that has Node.val == val, 
and return the new head.

Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:
Input: head = [], val = 1
Output: []

Example 3:
Input: head = [7,7,7,7], val = 7
Output: []

Constraints:

The number of nodes in the list is in the range [0, 104].
1 <= Node.val <= 50
0 <= val <= 50
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(head, val):
    dummy = ListNode(next=head)  # 创建虚拟头节点
    prev, curr = dummy, head

    while curr:
        if curr.val == val:
            prev.next = curr.next  # 删除 curr 节点
        else:
            prev = curr
        curr = curr.next

    return dummy.next  # 返回虚拟头节点的下一个节点，即新链表的头节点


# 测试用例
head = ListNode(1, ListNode(2, ListNode(
    6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
result = removeElements(head, 6)
