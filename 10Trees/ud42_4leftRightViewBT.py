"""
Udemy
Question :Left/Right View of binary tree

1. Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
2. Given the root of a binary tree, imagine yourself standing on the left side of it, return the values of the nodes you can see ordered from top to bottom.

"""


from ud41_3levelOrderTraverseBT import *

def rightView(root):
    right = []
    if root is None: 
        return right
    tree = level_order_traversal(root)
    for row in tree:
        right.append(row[-1])
    return right

def leftView(root):
    left = []
    if root is None: 
        return left
    tree = level_order_traversal(root)
    for row in tree:
        left.append(row[0])
    return left


def rightViewBT(root):
    right = []   # We will store the right view in this list. The size of the list is equal to the height of the tree.Hence, the space complexity is O(h), where h is the height of the tree.
    if root is None: 
        return right    # No operation required if root is None, hence O(1) time and O(1) space complexity.
    queue = [root]   #In worst case scenario, the maximum size of the queue is the width of the tree, which could be equal to the number of nodes in the tree. o(n)
    while queue:
        count = 0
        size = len(queue)
        while count < size: 
            curr = queue.pop(0)
            if count == size - 1:
                right.append(curr.value)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            count += 1
    return right

def leftViewBT(root):
    left = []
    if root is None: 
        return left
    
    queue = [root]
    while queue:  # This loop runs once for each node in the tree, hence O(n) time complexity, where n is the number of nodes.
        count = 0
        size = len(queue)
        while count < size: # This loop runs once for each node in the current level.
            curr = queue.pop(0) # This operation can take O(n) time complexity in worst case scenario as all the elements have to be shifted.
            if count == 0:
                left.append(curr.value)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            count += 1
    return left

'''
Final time complexity: O(n) + O(n) = O(n), where n is the number of nodes in the tree.
Final space complexity: O(n) + O(h) = O(n), where n is the number of nodes and h is the height of the tree.
'''

tree = BinaryTree()
tree.insert([4, 1, 3, 2, 8, 7, None, None, 5, None, None, None, None, 12, None])
print(rightView(tree.root))
print(leftView(tree.root))

print(rightViewBT(tree.root))
print(leftViewBT(tree.root))
