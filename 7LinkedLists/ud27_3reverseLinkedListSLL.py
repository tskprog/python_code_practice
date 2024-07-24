"""
Udemy
Reverse SLL- You are given the head of a Singly Linked list. Write a function that will take the given head as input, reverse the Linked List and return the new head of the reversed Linked List.

Test Cases
ip = 3 ; ll = 3->4->5->6->None
op = 6 ; ll = 6->5->4->3->None
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverseLinkedList(head):
    prev = None
    current = head
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

#  The function contains a while loop that traverses the linked list once, so the time complexity is O(n) 
# where n is the number of nodes in the linked list.
#  This function uses a constant amount of space to store the 'head', 'current', 'next', and 'prev' pointers. 
# Therefore, the space complexity is O(1).


from ud25_1linkedListSLL import *

sllrev = SinglyLinkedList()
n = int(input('Enter number of elements: '))
print('Enter numbers in non-decreasing order:')
for i in range(n):
    sllrev.addAtTail(int(input()))
print('Input linked list is :')
sllrev.printLinkedList()
head = sllrev.head
sllrev.head = reverseLinkedList(head)
print('result linked list is')
sllrev.printLinkedList()
