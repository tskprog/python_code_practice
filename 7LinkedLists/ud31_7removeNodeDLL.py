"""
Udemy
Create a Doubly Linked List class. Write Instance Methods for this class to be able to

1.remove a node when the node to be removed is given as Input.

Test Cases
Removal: ip = None<-3<->2<->7->None; 2 --> op = None<-3<->7->None

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
        if node == self.head:
            self.head = node.next
        elif node == self.tail:
            self.tail = node.prev
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.next = None
        node.prev = None
    
    def printLinkedList(self):
        current = self.head
        nums = []
        while current:
            nums.append(current.val)
            current = current.next
        print('<->'.join([str(i) for i in nums]))

# The removal operation in doubly linked list is done in constant time.
# It does not depend on the number of elements in the list.
# Hence the time complexity is O(1)
# The space complexity of the remove operation is O(1) since no additional space is used.

one = Node(2)
two = Node(5)
three = Node(23)
four = Node(0)
five = Node(9)
linkNodes(one,two)
linkNodes(two,three)
linkNodes(three,four)
linkNodes(four,five)

dll = DoublyLinkedList()
dll.head = one
dll.tail = five

print('Input DLL is')
dll.printLinkedList()

dll.remove(one)
print('DLL after removal of head')
dll.printLinkedList()
dll.remove(three)
print('DLL after removal of mid')
dll.printLinkedList()
dll.remove(five)
print('DLL after removal of tail')
dll.printLinkedList()