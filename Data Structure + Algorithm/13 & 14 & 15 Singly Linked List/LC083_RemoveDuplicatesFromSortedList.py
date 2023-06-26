"""
83. Remove Duplicates from Sorted List

Given the head of a sorted linked list, 
delete all duplicates such that each element appears only once. 
Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # T = O(n)
    # S = O(n)
    def deleteDuplicates(self, head):
        if not head:
            return None
        
        seen = set()  # 用于存储已经遇到的唯一值的集合
        seen.add(head.val)  # 将头节点的值添加到集合中
        current = head  # 当前节点指针
        
        while current.next:
            if current.next.val in seen:  # 如果下一个节点的值已经在集合中存在，表示有重复
                current.next = current.next.next  # 跳过重复节点
            else:
                seen.add(current.next.val)  # 将下一个节点的值添加到集合中
                current = current.next  # 移动当前节点指针到下一个节点
        
        return head
    
    # T = O(n)
    # S = O(1)
    def deleteDuplicates2(self, head):
        if not head:
            return None
        
        current = head  # 当前节点指针
        while current.next:
            if current.val == current.next.val:  # 如果当前节点和下一个节点的值相同，表示有重复
                current.next = current.next.next  # 跳过重复节点
            else:
                current = current.next  # 如果值不相同，移动当前节点指针到下一个节点

        return head

# Test Cases
solution = Solution()

# Test Case 1
head1 = ListNode(1)
head1.next = ListNode(1)
head1.next.next = ListNode(2)
result1 = solution.deleteDuplicates(head1)
output1 = []
current = result1
while current:
    output1.append(current.val)
    current = current.next
print(output1)  # Expected: [1, 2]

result2 = solution.deleteDuplicates2(head1)
output2 = []
current = result2
while current:
    output2.append(current.val)
    current = current.next
print(output2)  # Expected: [1, 2]

# Test Case 2
head3 = ListNode(1)
head3.next = ListNode(1)
head3.next.next = ListNode(2)
head3.next.next.next = ListNode(3)
head3.next.next.next.next = ListNode(3)
result3 = solution.deleteDuplicates(head3)
output3 = []
current = result3
while current:
    output3.append(current.val)
    current = current.next
print(output3)  # Expected: [1, 2, 3]

result4 = solution.deleteDuplicates2(head3)
output4 = []
current = result4
while current:
    output4.append(current.val)
    current = current.next
print(output4)  # Expected: [1, 2, 3]