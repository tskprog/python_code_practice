"""
Udemy
Question :Construct Stack (using Linked List)
(you can do it with either SLL or DLL. Here let's try to do it with SLL)
Implement a Stack:
1.Using an Array
2.with a Stack class using a Linked list
One should be able to add to the stack and remove from the stack following the LIFO property.
Test Cases
Insert: push3  --> op = 3->None
Remove: pop --> op = 3
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def addAtBeginning(self, value):
        node = Node(value)
        node.next = self.first
        if not self.first:
            self.last = node
        self.first = node
        self.size += 1
        return self

    def removeFromBeginning(self):
        node = self.first
        if not node:
            return None
        self.first = node.next
        node.next = None
        self.size -= 1
        if self.size == 0:
            self.last = None
        return node.value
    
    def printStack(self):
        current = self.first
        nums = []
        while current:
            nums.append(current.value)
            current = current.next
        print('->'.join([str(i) for i in nums]))


# Adding an element at the beginning of a linked list is an O(1) operation,because it requires a constant amount of work: creating a new node, and changing a couple of references.
# Removing an element from the beginning of a linked list is an O(1) operation,because it requires a constant amount of work: changing a couple of references, and optionally deleting a node.
# The auxiliary space complexity of a stack implemented using a linked list is O(1), because we are not using any extra data structures that scale with the input size. 
# We only have a few variables to maintain the state of the stack.


one = Node(2)
two = Node(5)
three = Node(23)
four = Node(0)
five = Node(9)

stack = StackLinkedList()
stack.addAtBeginning(one)
stack.addAtBeginning(two)
print('stack is : ')
stack.printStack()
print(stack.removeFromBeginning())
stack.addAtBeginning(three)
print('stack is : ')
stack.printStack()
print(stack.removeFromBeginning())
print(stack.removeFromBeginning())
print('stack is : ')
stack.printStack()