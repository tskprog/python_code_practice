"""
Udemy
Question :Diameter of  binary tree

Given the root of a binary tree, find the diameter of the tree where diameter is length of the longest path between any two nodes in the tree. Length is number of edges between nodes.
"""


from ud40_2traverseBST import *
from ud41_3levelOrderTraverseBT import *


def diameterBT(root):
    diameter = 0
    if not root:   # If there's no root, the diameter is 0
        return diameter
    def dfs(node):
        nonlocal diameter  # allows us to modify the outer scope's maxDiameter variable
        if not node:    # base case: if node is null, return -1 (height of an empty tree)
            return -1
        lh = dfs(node.left)   # calculate height of left subtree
        rh = dfs(node.right)
        d = lh + rh +1 +1       # calculate diameter
        diameter = max(diameter,d)  # update maxDiameter if current diameter is greater
        return max(lh,rh)+1     # return height of current node
    dfs(root)  # start the dfs from root
    return diameter
    
                    
'''
Time complexity for both dfs calls combined is O(n), where n is the total number of nodes in the tree,because every node in the tree is visited exactly once
The space complexity here is O(h) where h is the height of the tree, this is due to the extra space required by the call stack during the depth-first search.
'''



tree = BinaryTree()
case1 = [4, 1, 3, 2, 8, 7, None, None, 5, None, None, None, None, 12, None]
case2 = [1,2,3,4,5,6,7]
tree.insert(case1)

bstt = BinarySearchTreeTraverse()
bstt.root = tree.root

print('DFS-bfs is ',bstt.breadth_first())
print('DFS-preorder is ',bstt.dfs_pre_order())

print('Diameter is ', diameterBT(bstt.root))
