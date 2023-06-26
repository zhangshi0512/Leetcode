"""
141. Linked List Cycle

Given head, the head of a linked list, 
determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node 
in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer 
is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
See LC141_Ex1.png
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, 
where the tail connects to the 1st node (0-indexed).

Example 2:
See LC141_Ex2.png
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, 
where the tail connects to the 0th node.

Example 3:
See LC141_Ex3.png
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Fast and Slow Pointer Method
# T = O(n)
# S = O(1)


def hasCycle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False


# Hash set Method
# T = O(n)
# S = O(n)

def hasCycle2(head):
    seen = set()
    while head:
        if head in seen:
            return True
        seen.add(head)
        head = head.next

    return False


# Test Case 1
head1 = ListNode(3)
head1.next = ListNode(2)
head1.next.next = ListNode(0)
head1.next.next.next = ListNode(-4)
head1.next.next.next.next = head1.next
result1 = hasCycle(head1)
print(result1)  # Expected: True

result2 = hasCycle2(head1)
print(result2)  # Expected: True

# Test Case 2
head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = head2
result3 = hasCycle(head2)
print(result3)  # Expected: True

result4 = hasCycle2(head2)
print(result4)  # Expected: True

# Test Case 3
head3 = ListNode(1)
result5 = hasCycle(head3)
print(result5)  # Expected: False

result6 = hasCycle2(head3)
print(result6)  # Expected: False
