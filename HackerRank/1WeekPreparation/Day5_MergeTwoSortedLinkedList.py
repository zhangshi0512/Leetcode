"""
Given pointers to the heads of two sorted linked lists, merge them into a single, 
sorted linked list. 
Either head pointer may be null meaning that the corresponding list is empty.

Example:
headA refers to 1 -> 3 -> 7 -> NULL
headB refers to 1 -> 2 -> NULL

The new list is 1 -> 1 -> 2 -> 3 -> 7 -> NULL
"""

# For your reference:
#


class SinglyLinkedListNode:
    def __init__(self, x):
        self.data = x
        self.next = None
#
#


def mergeListsRecursive(head1, head2):
    # one of the two head is null
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    # if both heads are not null
    # initialize the merged_head as None
    merged_head = None

    if head1.data < head2.data:
        merged_head = head1
        merged_head.next = mergeListsRecursive(head1.next, head2)
    else:
        merged_head = head2
        merged_head.next = mergeListsRecursive(head1, head2.next)

    return merged_head


def mergeListsIterative(head1, head2):
    dummyNode = SinglyLinkedListNode(0)

    tail = dummyNode
    while True:
        if head1 is None:
            tail.next = head2
            break
        elif head2 is None:
            tail.next = head1
            break

        if head1.data <= head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next

        tail = tail.next
    return dummyNode.next


# Create first list
headA1 = SinglyLinkedListNode(1)
headA2 = SinglyLinkedListNode(3)
headA3 = SinglyLinkedListNode(7)
headA1.next = headA2
headA2.next = headA3

# Create second list
headB1 = SinglyLinkedListNode(1)
headB2 = SinglyLinkedListNode(2)
headB1.next = headB2

# Merge lists
merged_list = mergeListsRecursive(headA1, headB1)

# Print the merged list
while merged_list is not None:
    print(merged_list.data)
    merged_list = merged_list.next
