"""
19. Remove Nth Node From End of List

Given the head of a linked list, 
remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        # Create a dummy node to handle cases where the head itself needs to be removed
        dummy = ListNode(0)
        dummy.next = head

        # Use two pointers, slow and fast, initialized to the dummy node
        slow = fast = dummy

        # Move the fast pointer n+1 steps ahead
        for _ in range(n+1):
            fast = fast.next

        # Move both slow and fast pointers until the fast pointer reaches the end
        while fast:
            slow = slow.next
            fast = fast.next

        # Remove the nth node from the end by adjusting the next pointers
        slow.next = slow.next.next

        # Return the modified linked list (excluding the removed node)
        return dummy.next


solution = Solution()

# Test Case 1
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)
result1 = solution.removeNthFromEnd(head1, 2)
output1 = []
current = result1
while current:
    output1.append(current.val)
    current = current.next
print(output1)  # Expected: [1, 2, 3, 5]

# Test Case 2
head2 = ListNode(1)
result2 = solution.removeNthFromEnd(head2, 1)
output2 = []
current = result2
while current:
    output2.append(current.val)
    current = current.next
print(output2)  # Expected: []

# Test Case 3
head3 = ListNode(1)
head3.next = ListNode(2)
result3 = solution.removeNthFromEnd(head3, 2)
output3 = []
current = result3
while current:
    output3.append(current.val)
    current = current.next
print(output3)  # Expected: [1]
