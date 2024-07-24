"""
Udemy
Cycle Detection - You are given the head of a linked list. Check if there is a cycle and if yes,  return the node where the cycle begins. If there is no cycle, return null. There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Do not modify the linked list.

"""

def checkLoop_brute(head):
    curr = head
    l = []
    while curr:
        if curr.value not in l:
            l.append(curr.value)
        else:
            return curr
        curr = curr.next
    return None

# SC=O(n)-->for n nodes TC = O(n))-->traversing the linked list once


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
 
def checkLoop(head):    
    if not head or not head.next:
        return None
 
    hare = head
    tortoise = head
    while hare and hare.next:
        hare = hare.next.next
        tortoise = tortoise.next
        if hare == tortoise:
            break
 
    if hare != tortoise:
        return None
 
    # find where cycle begins
    pointer = head
    while pointer != tortoise:
        pointer = pointer.next
        tortoise = tortoise.next
 
    return tortoise
 
# The while loop runs at most 'n' times where 'n' is the number of elements in the linked list.  TC=O(n)
# We only use a constant amount of memory to store pointers 'head', 'hare', 'tortoise', and 'pointer'. 
# Therefore, the space complexity is O(1).

# For Testing
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
 
one.next = two
two.next = three
three.next = four
four.next = five
five.next = six
# make a loop
six.next = three
head = one
loop_node = checkLoop_brute(head)
print(f'cycle started at {loop_node.value}')
loop_node = checkLoop(head)
print(f'cycle started at {loop_node.value}')
