"""
Udemy
Question :DLL remove insert

Create a Doubly Linked List class. Write Instance Methods for this class to be able to
Done in Prev Question -
1.remove a node when the node to be removed is given as Input.
Do as part of this exercise -
2. insert a node before a particular node(both the node to be inserted and the node before which the insertion is to happen will be given as input). If the node to be inserted is
-part of the linked list then shift its place to the desired location
-a new node, then insert the new node at the place desired.

Test Cases
ip = None<-3<->2<->7->None; 2,1 --> op = None<-3<->1<->2<->7->None

"""


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None

def linkNodes(node1,node2):
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
        if nodeInsert == self.head and nodeInsert == self.tail:
            return
        self.remove(nodeInsert)
        nodeInsert.prev = nodePosition.prev
        nodeInsert.next = nodePosition
        if nodePosition == self.head:
            self.head = nodeInsert
        else:
            nodePosition.prev.next = nodeInsert
        nodePosition.prev = nodeInsert

    
    def printLinkedList(self):
        current = self.head
        nums = []
        while current:
            nums.append(current.val)
            current = current.next
        print('<->'.join([str(i) for i in nums]))

# Both the removal and insertion operations in doubly linked list are done in constant time.
# It does not depend on the number of elements in the list.
# Hence the time complexity is O(1)
# The space complexity of the remove and insertB operations is O(1) since no additional space is used.

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

print('Input DLL is')
dll.printLinkedList()


six = Node(10)
dll.insertB(one,six)
print('DLL after inserting at head')
dll.printLinkedList()
seven = Node(11)
dll.insertB(five,seven)
print('DLL after inserting before tail')
dll.printLinkedList()
eight = Node(12)
dll.insertB(three,eight)
print('DLL after inserting at middle')
dll.printLinkedList()