"""
Udemy
Construct Singly Linked List - Design a Singly linked list class that has a head and tail. Every node is to have two attributes: value:  the value of the current node, and next: a pointer to the next node. The linked list is to be 0-indexed. The class should support the following:

SinglyLinkedList() Initializes the SinglyLinkedList object.
get(index) Get the node at the index passed. If the index is invalid, return -1.
addAtHead(value)- Add a node of given value before the first element of the linked list. Return the SLL
addAtTail(value) -  Add a node of given value at the last element of the linked list. Return the SLL
addAtIndex(index, value) Add a node of given value before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, don’t insert the node(return a message 'invalid index' ). Return SLL once done.
deleteAtIndex(index) Delete the indexth node in the linked list, if the index is valid, else nothing happens.Return deleted node
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Time Complexity: O(n) as we might traverse through the entire list in the worst case
    # Space Complexity: O(1) as no additional space is required
    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        i = 0
        current = self.head
        while index != i:
            current = current.next
            i += 1
        return current


    # Time Complexity: O(1) as we perform constant time operations
    # Space Complexity: O(1) as no additional space is required
    def addAtHead(self, value):
        node = Node(value)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1
        print(f'added{value}',self.size)


    # Time Complexity: O(1) as we perform constant time operations
    # Space Complexity: O(1) as no additional space is required
    def addAtTail(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
        print(f'added{value}',self.size)
    

    # Time Complexity: O(n) as we might traverse through the entire list in the worst case
    # Space Complexity: O(1) as no additional space is required

    def addAtIndex(self, index, value):
        if index < 0 or index > self.size:
            return 'invalid index'
        elif index == 0:
            return self.addAtHead(value)
        elif index == self.size:
            return self.addAtTail(value)
        else:
            node = Node(value)
            prev = self.get(index-1)
            current = prev.next
            prev.next = node
            node.next = current
            self.size += 1
        print(f'added{value}',self.size)

    # Time Complexity: O(n) as we might traverse through the entire list in the worst case
    # Space Complexity: O(1) as no additional space is required

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return 'invalid index'
        elif index == 0:
            current = self.head
            self.head = current.next
            self.size -= 1
            if self.size == 0:
                self.tail = None
            return current.value
        elif index == self.size-1:
            current = self.tail
            new_tail = self.get(index-1)
            self.tail = new_tail
            new_tail.next = None
            self.size -= 1
            return current.value
        else:
            prev = self.get(index-1)
            current = prev.next
            prev.next = current.next
            self.size -= 1
            return current.value
    
    def printLinkedList(self):
        current = self.head
        nums = []
        while current:
            nums.append(current.value)
            current = current.next
        print('->'.join([str(i) for i in nums]))



# Below are used to Test functions
# sll = SinglyLinkedList()
# sll.addAtHead(9)
# sll.addAtTail(123)
# print(sll.addAtIndex(6,6))
# sll.addAtIndex(1,-34)
# print(sll.get(7))
# print(sll.get(1).value)
# print(sll.deleteAtIndex(4))
# print(sll.deleteAtIndex(0))
# print(sll.head.value,sll.tail.value,sll.size)