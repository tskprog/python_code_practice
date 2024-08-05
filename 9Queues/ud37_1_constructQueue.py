"""
Udemy
Question :Construct Queue
Implement a Queue:
- with a Queue class using a Linked list
One should be able to add to the queue and remove from the queue following the FIFO property.
Test Cases
Insert: enqueue 3,4,5  --> op = 3->4->5->None
Removal: dequeue --> op = 3
"""

# Implementation 1: Queue using an Array
 
queue = []  # array to hold queue elements
value = 1
queue.append(value)  # add value to end of queue, O(1)
queue.pop(0)  # remove value from start of queue, O(n)
 
# The overall time complexity of enqueue operation is O(1), and the dequeue operation is O(n).
#Space complexity is O(1) for enqueue and dequeue

# Implementation 2: Queue using a Linked List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, value):
        node = Node(value)
        if self.size == 0:
            self.first = node
        else:
            self.last.next = node
        self.last = node
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        node = self.first
        self.first = node.next
        self.size -= 1
        if self.size == 0:
            self.last = None
        return node.value
    
    def printQueue(self):
        current = self.first
        nums = []
        while current:
            nums.append(current.value)
            current = current.next
        print('->'.join([str(i) for i in nums]))


# Enqueue: Creating a new node and updating the last pointer has a time complexity of O(1)
# Dequeue: Updating the first pointer and reducing the size variable has a time complexity of O(1)

one = Node(2)
two = Node(5)
three = Node(23)
four = Node(0)
five = Node(9)

queue = QueueLinkedList()
queue.enqueue(one)
queue.enqueue(two)
print('Queue is : ')
queue.printQueue()
print(queue.dequeue())
queue.enqueue(three)
print('Queue is : ')
queue.printQueue()
print(queue.dequeue())
print(queue.dequeue())
print('Queue is : ')
queue.printQueue()