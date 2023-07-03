"""
2130. Maximum Twin Sum of a Linked List

In a linked list of size n, where n is even, 
the ith node (0-indexed) of the linked list 
is known as the twin of the (n-1-i)th node, 
if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, 
and node 1 is the twin of node 2. 

These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, 
return the maximum twin sum of the linked list.

Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6. 

Input: head = [4,2,2,3]
Output: 7
Explanation:
The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 

Input: head = [1,100000]
Output: 100001
Explanation:
There is only one node with a twin in the linked list having 
twin sum of 1 + 100000 = 100001.

Constraints:

The number of nodes in the list is an even integer in the range [2, 10^5].
1 <= Node.val <= 10^5
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head):
        # 定义两个指针，一个慢指针，一个快指针
        slow = fast = head  
        
        # 数组用于存储链表的前一半元素
        first_half = []  
        
        # 遍历链表，快指针的速度是慢指针的两倍
        while fast and fast.next:
            first_half.append(slow.val)  # 保存慢指针当前的值
            slow = slow.next  # 慢指针前进一步
            fast = fast.next.next  # 快指针前进两步

        max_twin_sum = 0  # 初始化最大双子和为0
        
        # 慢指针现在位于链表的中点，我们从这里开始遍历链表的后半部分
        index = 0
        while slow:
            # 计算双子和并更新最大双子和
            max_twin_sum = max(max_twin_sum, slow.val + first_half[-(index + 1)])
            slow = slow.next  # 前进一步
            index += 1
            
        return max_twin_sum

# helper function for test cases
def list_to_linked_list(lst):
    # 将列表转换为链表
    head = current = ListNode(lst[0])
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# 创建示例数据和测试实例
test_cases = [
    ([5,4,2,1], 6),
    ([4,2,2,3], 7),
    ([1,100000], 100001)
]

solution = Solution()
# 对每一个测试用例进行测试
for i, (input_data, expected_output) in enumerate(test_cases):
    head = list_to_linked_list(input_data)
    output = solution.pairSum(head)
    assert output == expected_output, f'Test case {i+1} failed: got {output}, expected {expected_output}'
print("All test cases passed.")

