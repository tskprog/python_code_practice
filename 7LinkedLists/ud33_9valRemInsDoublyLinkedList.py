"""
Udemy
Question :DLL remove all with specified value
Create a Doubly Linked List class. Write Instance Methods for this class to be able to
1. remove all the nodes in the doubly linked list which have their value equal to a given value.
2.Insert a node at a desired position (node and position are given). The Linked List is 0 indexed. If given node is a node existing in the Linked List shift it to the desired position.

Test Cases
remove: ip = None<-3<->2<->3<->7<->3->None; 3 --> op = None<-1<->2<->7->None
insert: ip = None<-1<->2<->3<->4<->5->None;p=3,6 --> op = None<-1<->2<->3<->6<->4<->5->None
"""


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None

def linkNodes(node1, node2):
    node1.next = node2
    node2.prev = node1

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def remove(self, node):
        if self.head == node:
            self.head = node.next
        if self.tail == node:
            self.tail = node.prev

        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        node.next = None
        node.prev = None

    def insertB(self, nodePosition, nodeInsert):
        if self.head == nodeInsert and self.tail == nodeInsert:
            return
        self.remove(nodeInsert)

        nodeInsert.prev = nodePosition.prev
        nodeInsert.next = nodePosition

        if nodePosition == self.head:
            self.head = nodeInsert
        else:
            nodePosition.prev.next = nodeInsert
        nodePosition.prev = nodeInsert

    def allNodesValueRemove(self, value):
        curr = self.head
        while curr:
            temp = curr
            curr = curr.next
            if temp.val == value:
                self.remove(temp)

    def insertPosition(self, position, node):
        ind = 0
        curr = self.head
        if not curr:
            self.head = node
            self.tail = node
            return
        while curr:
            if position == ind:
                self.insertB(curr,node)
                return
            ind += 1
            curr = curr.next
        self.remove(node)
        node.next = None
        linkNodes(self.tail,node)
        self.tail = node
    
    def printLinkedList(self):
        current = self.head
        nums = []
        while current:
            nums.append(current.val)
            current = current.next
        print('<->'.join([str(i) for i in nums]))

# All nodevalues remove method
# This method involves traversing the entire linked list. Therefore, the time complexity is linear O(n),where n is the number of nodes in the list.
# Insert at position method
# This method involves traversing the list until the desired position or the end of the list is reached.Therefore, the time complexity is linear O(n), where n is the number of nodes in the list.
# No additional space is used when inserting a node at a specific position.Hence the space complexity is O(1).

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
linkNodes(one,two)
linkNodes(two,three)
linkNodes(three,four)
linkNodes(four,five)

dll = DoublyLinkedList()
dll.head = one
dll.tail = five

six = Node(3)
seven = Node(3)
dll.insertB(two,six)
dll.insertB(five,seven)

print('Input DLL is')
dll.printLinkedList()

from userInput import *

dll.allNodesValueRemove(inputInt('Enter a element to be removed in the ablve DLL'))
print('DLL after removing all:')
dll.printLinkedList()

position = inputInt('Enter position to be inserted at: ')
node = Node(inputInt('Enter value of the node to be inserted: '))
dll.insertPosition(position,node)

print('DLL after inserting:')
dll.printLinkedList()