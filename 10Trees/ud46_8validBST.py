"""
Udemy
Question : Valid binary search tree

Given a root of the tree. Determine whether it is valid binary search tree or not.
Valid binary search tree is
    1. All left nodes should be less than parent node.
    2. All right nodes should be greater than parent node.
    3. Both left and right childs should also be binary search trees.
"""

from ud41_3levelOrderTraverseBT import *
import math

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
def isValidBST(root):
    return rangeCheck(root,- math.inf,math.inf)
    

def rangeCheck(node,low,high):
    if node is None:
        return True
    val = node.value
    if val<=low or val>=high:  # The current node's value must be between min_val and max_val
        return False
    # Check if the left and right subtrees are valid BSTs
    # The left subtree's values must all be less than the current node's value
    # The right subtree's values must all be greater than the current node's value
    isLeftBST = rangeCheck(node.left,low,val) # Time complexity is O(n/2)
    isRightBST = rangeCheck(node.right,val,high)  # Space complexity is O(n/2) for the recursive call stack
    return isLeftBST and isRightBST


'''
Time complexity is O(n), where n is the total number of nodes in the tree. This is because each node is visited once during the traversal.
Space complexity is O(h), where h is the height of the tree.
This is because the maximum amount of space is used when the recursion goes the deepest, which happens to be the height of the tree.
'''


case1 = [1,2,3,4,5,6,7,8,9]
case2 = [10,6,30,1,20,15,50]
case3 = [10,5,20,3,7,15,30,None,4,None,None,None,17,None,None,None,None,None,18]

tree = BinaryTree()
tree.insert(case2)

print('started')
print('level order is ', level_order_traversal(tree.root))
print(isValidBST(tree.root))
