# Big O Analysis

Here is a table showing the time and space complexity for some common operations in a binary search tree (BST):

| Operation             | Average Case Time Complexity | Worst Case Time Complexity | Space Complexity |
| --------------------- | ---------------------------- | -------------------------- | ---------------- |
| Search                | O(log n)                     | O(n)                       | O(n)             |
| Insert                | O(log n)                     | O(n)                       | O(n)             |
| Delete                | O(log n)                     | O(n)                       | O(n)             |
| Access                | O(log n)                     | O(n)                       | O(n)             |
| Find Min/Max          | O(log n)                     | O(n)                       | O(n)             |
| Successor/Predecessor | O(log n)                     | O(n)                       | O(n)             |
| In-order Traversal    | O(n)                         | O(n)                       | O(n)             |

The worst case scenarios for these operations occur when the tree becomes unbalanced and effectively transforms into a linked list.

# Code Template

Here is a simple implementation of a Binary Search Tree:

```python
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if node.val < key:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)
        else:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.val == key:
            return node
        if node.val < key:
            return self._search(node.right, key)
        return self._search(node.left, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.val:
            node.left = self._delete(node.left, key)
        elif key > node.val:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.val = temp.val
            node.right = self._delete(node.right, temp.val)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.val, end=' ')
            self._inorder(node.right)


# Sample usage:
bt = BinarySearchTree()
bt.insert(50)
bt.insert(30)
bt.insert(70)
bt.insert(20)
bt.insert(40)
bt.insert(60)
bt.insert(80)
bt.inorder()  # Output: 20 30 40 50 60 70 80
bt.delete(20)
bt.inorder()  # Output: 30 40 50
```
