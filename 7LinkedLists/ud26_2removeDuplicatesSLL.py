"""
Udemy
delete duplicates - You are given the head of a Sorted Singly Linked list. Write a function that will take the given head as input, delete all nodes that have a value that is already the value of another node so that each value appears 1 time only and return the linked list, which is still to be a sorted linked list.
"""


# class Node:
#     def __init__(self, value):
#         self.val = value
#         self.next = None

def removeDupes(head):
    current = head
    while current:
        next_val = current.next
        while next_val is not None and current.value == next_val.value:
            next_val = next_val.next
        current.next = next_val
        current = next_val
    return head


# The function contains a while loop that traverses the linked list once, so the time complexity is O(n) 
# Time complexity of this function is O(n), where n is the number of nodes in the list
# This function uses a constant amount of space to store the 'head', 'curr' and 'nextDistinctVal' pointers. 
# Therefore, the space complexity is O(1).


from ud25_1linkedListSLL import *

slldup = SinglyLinkedList()
n = int(input('Enter number of elements: '))
print('Enter numbers in non-decreasing order:')
for i in range(n):
    slldup.addAtTail(int(input()))
print('Input linked list is :')
slldup.printLinkedList()
head = slldup.head
slldup.head = removeDupes(head)
print('result linked list is')
slldup.printLinkedList()
