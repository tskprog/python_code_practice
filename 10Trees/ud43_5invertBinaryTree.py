"""
Udemy
Question :Invert binary tree

Given the root of a binary tree, invert the tree and return thre root. Invert means getting the mirror image of the given tree.
"""


from ud40_2traverseBST import *
from ud41_3levelOrderTraverseBT import *


def invertIterativeBT(root):
    if root is None:
        return None
    queue = [root] # We use a queue for bfs of the tree
    while queue:  # This loop runs once for each node in the tree, hence O(n) time complexity, where n is the number of nodes.
        curr = queue.pop(0)
        curr.left, curr.right = curr.right,curr.left
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
                
'''
Time complexity: O(n), where n is the number of nodes in the tree.
In worst case scenario, the maximum size of the queue is the width of the tree, which could be equal to the number of nodes in the tree.Hence, the space complexity is O(n), where n is the number of nodes in the tree.
'''

def invertRecursiveBT(node):
    if node is None:
        return None
    node.left, node.right = node.right, node.left
    # Perform the same operations for the left and right child nodes
    invertRecursiveBT(node.left) # Recursive call (Time Complexity: T(n/2))
    invertRecursiveBT(node.right) # Recursive call (Space Complexity: O(h/2))
    return node

'''
 Therefore, the overall Time Complexity of the function is O(n),where n is the total number of nodes in the binary tree. This is because each node in the tree is visited exactly once.
The overall Space Complexity of the function is O(h), where h is the height of the binary tree. This is because in a recursive function, space is required to store the recursive call stack. 
The deepest the recursion can go is till the height of the tree.
'''


tree = BinaryTree()
case1 = [4, 1, 3, 2, 8, 7, None, None, 5, None, None, None, None, 12, None]
case2 = [1,2,3,4,5,6,7]
tree.insert(case1)

bstt = BinarySearchTreeTraverse()
bstt.root = tree.root

print('DFS-bfs is ',bstt.breadth_first())
print('DFS-preorder is ',bstt.dfs_pre_order())
invertIterativeBT(bstt.root)
print('DFS-bfs is ',bstt.breadth_first())
print('DFS-inorder is ',bstt.dfs_pre_order())

print('DFS-bfs is ',bstt.breadth_first())
invertRecursiveBT(bstt.root)
print('DFS-bfs is ',bstt.breadth_first())
