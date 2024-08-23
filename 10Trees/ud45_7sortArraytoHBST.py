"""
Udemy
Question : Sorted array to binary search tree

Given a sorted array of distinct integers. Convert into height balanced binary search tree and return the root.
"""

from ud40_2traverseBST import *

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
def BSTfromSortArr(arr,left,right):
    if left > right:   # Base case
        return None
     # The middle element of the array becomes the root of the tree
    mid = (left+right)//2
    # print(left,mid,right)
    node = Node(arr[mid])
    node.left = BSTfromSortArr(arr,left,mid-1)
    node.right = BSTfromSortArr(arr,mid+1,right)
    return node

    
                    
'''
Recursively build the left and right subtrees. As this operation is performed recursively on each half of the array,its time complexity is O(n), where n is the number of elements in the array
SPace: O(log(n)), due to the space required by the call stack for the recursive calls
        O(n) for BST
 Final space complexity: O(log(n)+ n) = O(n) ( as the BST has n elements)  
'''


case1 = [1,2,3,4,5,6,7,8,9]
case2 = [2,3,56,7,8,90,99]

bstt = BinarySearchTreeTraverse()
bstt.root = BSTfromSortArr(case2,0,len(case2)-1)

print('started')
print('DFS-preorder is ',bstt.dfs_pre_order())
print('BFS-order is ',bstt.breadth_first())
