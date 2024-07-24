"""
Udemy
Add 2 numbers-You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. You may assume the two numbers do not contain any leading zero, except the number 0 itself. 0<=Node value<=9

Test Cases
ip = 3->2->7->None; 0->4->5->None --> op = 3->6->2->1->None
ip = 2->3->None; 0->0->1->None --> op = 2->3->1->None
"""


def add2Numbers(l1, l2):
    l3 = SinglyLinkedList()
    carry = 0
    while l1 or l2 or carry:
        d1 = l1.value if l1 else 0
        d2 = l2.value if l2 else 0
        sum = d1 + d2 + carry
        d3 = sum % 10
        carry =  sum // 10
        l3.addAtTail(d3)
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return l3

# The while loop runs at most 'max(n, m)' times where 'n' and 'm' are the lengths of l1 and l2 respectively. Thus, the time complexity is O(max(n, m)).
# We are creating a new LinkedList to store the sum. The maximum possible length of this LinkedList is 'max(n, m) + 1' where 'n' and 'm' are the lengths of l1 and l2 respectively Therefore, the space complexity is O(max(n, m)).

from ud25_1linkedListSLL import *

l1 = SinglyLinkedList()
n = int(input('Enter number of digits of 1st number: '))
print('Enter digits of a number1 in reverse order:')
for i in range(n):
    l1.addAtTail(int(input()))
print('1st linked list is :')
l1.printLinkedList()
l2 = SinglyLinkedList()
n = int(input('Enter number of digits of 2nd number: '))
print('Enter digits of a number2 in reverse order:')
for i in range(n):
    l2.addAtTail(int(input()))
print('2nd linked list is :')
l2.printLinkedList()
l3 = add2Numbers(l1.head,l2.head)
print('sum of 2 numbers is')
l3.printLinkedList()