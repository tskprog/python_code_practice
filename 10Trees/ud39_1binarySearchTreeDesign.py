"""
Udemy
Question :Construct BST
Design a Binary Search Tree class that supports the following:

1.Insert a value
2.Remove a value. This method should remove the first occurrence of a value.
3.Find a value. If the value is found it should return the node with the value else return false.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        current = self.root
        if not current:
            self.root = node
            return self
        while True:
            if value < current.value:
                if not current.left:
                    current.left = node
                    return self
                current = current.left
            else:
                if not current.right:
                    current.right = node
                    return self
                current = current.right

    def find(self, value):
        curr = self.root
        while curr:
            if value == curr.value:
                return curr
            elif value < curr.value:
                curr = curr.left
            else:
                curr = curr.right
        return False

    def remove(self, value, current=None, parent=None):
        if not self.root:
            return False
        if not current:
            current = self.root
        while current:
            if value < current.value:
                parent = current
                current = current.left
            elif value > current.value:
                parent = current
                current = current.right
            else:
                # found node to be deleted
                # remove node has two child 
                if current.left and current.right:
                    current.value = self.get_min(current.right)
                    self.remove(current.value,current.right,current)
                # remove node has atmost one child 
                elif not parent:
                    if current.left:
                        current.value = current.left.value
                        current.left = current.left.left
                        current.right = current.left.right
                    elif current.right:
                        current.value = current.right.value
                        current.left = current.right.left
                        current.right = current.right.right
                    else:
                        self.root = None
                elif current == parent.left:
                    parent.left = current.left if current.left else current.right
                elif current == parent.right:
                    parent.right = current.left if current.left else current.right
                break
        return self

    def get_min(self, node):
        while node.left:
            node = node.left
        return node.value


# Adding/Removing an element is an O(logn) operation for best and worst and O(n) for worst case lke in skewed tree
# The auxiliary space complexity is O(1), because we are not using any extra space.
# We only have a one recursive call to get the left most value in right tree i.e., inorder successor value
