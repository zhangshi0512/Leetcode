"""
98. Validate Binary Search Tree

Given the root of a binary tree, 
determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Input: root = [2,1,3]
    2
  /   \
 1     3
Output: true

Input: root = [5,1,4,null,null,3,6]
            5
          /   \
         1     4
              / \
             3   6
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:

The number of nodes in the tree is in the range [1, 10^4].
-2^31 <= Node.val <= 2^31 - 1
"""
# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root):

        def validate(node, low=-math.inf, high=math.inf):
            # empty nodes are valid BST
            if not node:
                return True

            # The current node's value must be between high and low.
            if node.val <= low or node.val >= high:
                return False

            # The left and right subtree must also be valid
            return (validate(node.right, node.val, high) and validate(node.left, low, node.val))

        return validate(root)
    
######################################################
# test case helper function:
def build_BST(lst):
    # 如果列表为空，返回None
    if not lst:
        return None
    
    # 将列表的第一个元素作为根节点
    root = TreeNode(lst[0])
    
    # 创建一个队列，并将根节点加入队列
    queue = [root]
    index = 1
    
    # 使用BFS构建二叉树
    while queue and index < len(lst):
        node = queue.pop(0)
        
        if lst[index] is not None:
            node.left = TreeNode(lst[index])
            queue.append(node.left)
        index += 1
        
        if index < len(lst) and lst[index] is not None:
            node.right = TreeNode(lst[index])
            queue.append(node.right)
        index += 1
    
    return root


# 定义测试数据和期望的输出
test_cases = [
    ([2,1,3], True),
    ([5,1,4,None,None,3,6], False),
]

solution = Solution()

# 循环遍历所有测试用例
for i, (input_data, expected_output) in enumerate(test_cases):
    # 使用 build_BST 函数从列表创建二叉树
    root = build_BST(input_data)
    # 调用 isValidBST 函数并获取输出
    output = solution.isValidBST(root)
    # 打印测试用例的结果
    print(f'Test case {i+1}:')
    print(f'Expected output: {expected_output}')
    print(f'Actual output: {output}')
    print('------')
