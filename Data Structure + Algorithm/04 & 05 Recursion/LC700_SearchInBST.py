"""
700. Search in a Binary Search Tree

ou are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val 
and return the subtree rooted with that node. 
If such a node does not exist, return null.

Input: root = [4,2,7,1,3], val = 2
     4
   /   \
  2     7
 / \
1   3

Output: [2,1,3]

Input: root = [4,2,7,1,3], val = 5
     4
   /   \
  2     7
 / \
1   3
Output: []

Constraints:

The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 10^7
root is a binary search tree.
1 <= val <= 10^7
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root, val):
        # base case
        if not root:
            return None
        if root.val == val:
            return root

        # recursion relation
        if val > root.val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)

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

def convert_BST_to_list(root):
    # 使用层序遍历（BFS）将二叉树转换为列表
    result = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # 删除列表末尾的None元素
    while result and result[-1] is None:
        result.pop()
    
    return result

# Test cases
test_cases = [
    ([4,2,7,1,3], 2, [2,1,3]),
    ([4,2,7,1,3], 5, []),
]

solution = Solution()

for i, (input_data, val, expected_output) in enumerate(test_cases):
    root = build_BST(input_data)
    output_node = solution.searchBST(root, val)
    output = convert_BST_to_list(output_node)
    print(f'Test case {i+1}:')
    print(f'Expected output: {expected_output}')
    print(f'Actual output: {output}')
    print('------')
