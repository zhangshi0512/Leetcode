"""
24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes 
(i.e., only nodes themselves may be changed.)

Input: head = [1,2,3,4]
Output: [2,1,4,3]

Input: head - [1,2,3,4,5,6]
Output: [2,1,4,3,6,5]

Input: head = []
Output: []

Input: head = [1]
Output: [1]

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
"""

# Definition for singly-linked list.
# 定义单链表。
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 创建一个新的节点作为预先指针，这是一个伪头部，并且它的下一个指针是头结点
        # Create a new node as a dummy pointer, which is a pseudo-head, and its next pointer is the head node
        dummy = ListNode(-1)
        dummy.next = head
        
        # 定义预先指针
        # Define the prev_node as the dummy node
        prev_node = dummy
        
        while head and head.next:
            # 将节点赋值给first_node和second_node
            # Nodes to be swapped
            first_node = head
            second_node = head.next

            # 交换节点
            # Swapping nodes
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # 重新初始化头和prev_node为下一次准备
            # Reinitializing head and prev_node for next swap
            prev_node = first_node
            head = first_node.next
            
        # 返回新的链表
        # Return the new linked list
        return dummy.next

# Test Case 1
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
result1 = Solution().swapPairs(head1)
output1 = []
current = result1
while current:
    output1.append(current.val)
    current = current.next
print(output1)  # Expected: [2, 1, 4, 3]

# Test Case 2
head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = ListNode(3)
head2.next.next.next = ListNode(4)
head2.next.next.next.next = ListNode(5)
head2.next.next.next.next.next = ListNode(6)
result2 = Solution().swapPairs(head2)
output2 = []
current = result2
while current:
    output2.append(current.val)
    current = current.next
print(output2)  # Expected: [2, 1, 4, 3, 6, 5]

# Test Case 3
head3 = None
result3 = Solution().swapPairs(head3)
output3 = []
current = result3
while current:
    output3.append(current.val)
    current = current.next
print(output3)  # Expected: []

# Test Case 4
head4 = ListNode(1)
result4 = Solution().swapPairs(head4)
output4 = []
current = result4
while current:
    output4.append(current.val)
    current = current.next
print(output4)  # Expected: [1]

