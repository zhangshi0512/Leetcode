"""
Given the head of a singly linked list, 
reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

Input: head = []
Output: []

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. 
Could you implement both?
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

    def reverseListRecursive(self, head):
        if not head or not head.next:
            return head
        p = self.reverseListRecursive(head.next)
        head.next.next = head
        head.next = None
        return p


# Test Cases
solution = Solution()

# Test Case 1
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)
result1 = solution.reverseList(head1)
output1 = []
current = result1
while current:
    output1.append(current.val)
    current = current.next
print(output1)  # Expected: [5, 4, 3, 2, 1]

# Test Case 2
head2 = ListNode(1)
head2.next = ListNode(2)
result2 = solution.reverseList(head2)
output2 = []
current = result2
while current:
    output2.append(current.val)
    current = current.next
print(output2)  # Expected: [2, 1]

# Test Case 3
head3 = None
result3 = solution.reverseList(head3)
output3 = []
current = result3
while current:
    output3.append(current.val)
    current = current.next
print(output3)  # Expected: []
