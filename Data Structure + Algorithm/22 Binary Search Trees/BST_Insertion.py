
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.count = 1


class BST:
    def __init__(self):
        self.root = None

    def _insert(self, node, key):
        # Return a new node if the tree is empty
        if node is None:
            return Node(key)
        # Traverse to the right place and insert the node
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:  # Handling duplicates.count field is added in Node to handle duplicates.
            node.count += 1
        return node

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def print_tree(self, node, indent=""):
        # Inorder traversal to print the node
        if node is not None:
            self.print_tree(node.left, indent + "   ")
            print(indent, node.key)
            self.print_tree(node.right, indent + "   ")

# Example usage:


tree = BST()

keys = ['E', 'A', 'S', 'Y', 'Q', 'U', 'E', 'S', 'T', 'I', 'O', 'N']
for key in keys:
    tree.insert(key)
    tree.print_tree(tree.root)
    print("\n====================\n")
"""


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


def print_tree(root, indent='', is_left=True):
    if root is not None:
        # Print right branch
        print_tree(root.right, indent + ('    ' if is_left else '|   '), False)
        # Print current node
        print(indent + ('\\- ' if is_left else '/- ') + str(root.key))
        # Print left branch
        print_tree(root.left, indent + ('|   ' if is_left else '    '), True)


def find_min(root):
    while root.left is not None:
        root = root.left
    return root


def delete(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = find_min(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)
    return root


# Initialize an empty BST
root = None

# List of keys to insert in the given order
keys_to_insert = ['E', 'A', 'S', 'Y', 'Q', 'U', 'E', 'S', 'T', 'I', 'O', 'N']

# Insert keys one by one and print the tree after each insertion
for key in keys_to_insert:
    root = insert(root, key)
    print(f"\nAfter inserting {key}:")
    print_tree(root, is_left=False)  # Start with right branch for the root
    print("\n" + "-"*50)

# Delete keys in the same order they were inserted and print the tree after each deletion
for key in keys_to_insert:
    root = delete(root, key)
    print(f"\nAfter deleting {key}:")
    print_tree(root, is_left=False)  # Start with right branch for the root
    print("\n" + "-"*50)
"""
