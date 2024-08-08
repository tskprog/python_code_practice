"""
Udemy
Traverse - BFS and DFS
Question :Traverse BST

Write a 4 instance methods for a Binary Search Tree class to traverse the BST.

1. Method 1 : traverse the tree breadth first and return an array that contains all the values of the BST.
2. Method 2: traverse the tree depth first – In-order and return an array that contains all the values of the BST.
3. Method 3 : traverse the tree depth first – Pre-order and return an array that contains all the values of the BST.
4. Method 4 : traverse the tree depth first – Post-order and return an array that contains all the values of the BST.


BFS = Level by level
DFS = Based on depth. Processing order for
    1. in-order = left,current,right nodes
    2. pre-order = current,left,right nodes
    3. post-order = left,right,current nodes
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTreeTraverse:
    def __init__(self):
        self.root = None

    def bread_first(self):
        array = []
        curr = self.root
        if not curr:
            return array
        # implementing queue using array for saving time
        queue = [] #FIFO
        queue.append(curr)
        while queue:
            curr = queue.pop(0)
            array.append(curr.value)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return array
            

    def dfs_in_order(self):
        # left,current,right
        array = []
        node = self.root
        if not node:
            return array
        def trav(node):
            if node.left:
                trav(node.left)
            array.append(node.value)
            if node.right:
                trav(node.right)
        trav(node)
        return array

    def dfs_pre_order(self):
        # current,left,right
        array = []
        node = self.root
        if not node:
            return array
        def trav(node):
            array.append(node.value)
            if node.left:
                trav(node.left)
            if node.right:
                trav(node.right)
        trav(node)
        return array

    def dfs_post_order(self):
        # left,right,cuurent
        array = []
        node = self.root
        if not node:
            return array
        def trav(node):
            if node.left:
                trav(node.left)
            if node.right:
                trav(node.right)
            array.append(node.value)
        trav(node)
        return array
        

# Time complexity is TC=O(n) for all traversals as we are traversing every node once and doing some constant operations
# Space Complexity 
# BFS: O(n) n is nodes in returning array and queue length is max width in the tree i.e., O(w)
#   in best case like skewed tree(LL) it is O(1)
# DFS: O(n) for all orders n is length of returning array and O(d) where d is max depth of tree represents number of calls in a stack.

from ud39_1binarySearchTreeDesign import *

bst = BinarySearchTree()
bst.insert(20)
bst.insert(13)
bst.insert(40)
bst.insert(10)
bst.insert(13)
bst.insert(43)
bst.insert(8)
bst.insert(11)
bst.insert(41)
bst.insert(68)
bst.insert(75)

bstt = BinarySearchTreeTraverse()
bstt.root = bst.root
print('BFS is ',bstt.bread_first())
print('DFS-inorder is ',bstt.dfs_in_order())
print('DFS post-order is ',bstt.dfs_post_order())
print('DFS pre-order is ',bstt.dfs_pre_order())