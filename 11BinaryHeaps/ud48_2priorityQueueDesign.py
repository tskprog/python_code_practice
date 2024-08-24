"""
Udemy
Question : Construct Priority queue
Implement a priority queue as minimum binary heap. PQ supports the following:

1. Enqueue to insert an element
2. Dequeue to extract hughest priority element. Here lowest numerical priority is treated as highest priority
Note: So 1 is treated as highest priority.
"""

class Node:
    def __init__(self,value,priority):
        self.value = value
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.data = []
    
    def enqueue(self,value,priority):
        node = Node(value,priority)
        self.data.append(node)
        self.bubbleUp()

    def bubbleUp(self):
        idx = len(self.data)-1
        node = self.data[idx]
        while idx > 0:
            parentIdx = (idx-1)//2
            parentNode = self.data[parentIdx]
            if node.priority >= parentNode.priority:
                break
            # Swap parent with current node
            self.data[idx],self.data[parentIdx] = self.data[parentIdx],self.data[idx]
            idx = parentIdx
    
    # Time complexity: O(logn) as in worst case, we may have to traverse up to the root from the last node
    # The height of a binary heap is logn, hence the time complexity

    def dequeue(self):
        maxPriorNode = self.data[0]
        last = self.data.pop()
        if len(self.data) > 0:
            self.data[0] = last
            self.bubbleDown()
        return maxPriorNode

    
    def bubbleDown(self):
        idx = 0
        size = len(self.data)
        curr = self.data[idx]
        while True:
            leftChildIdx = (2*idx)+1
            rightChildIdx = 2*idx+2
            smallest = None
            if leftChildIdx < size:
                leftChild = self.data[leftChildIdx]
                if leftChild.priority < curr.priority:   # If it's less than current element priority, it could be the prioritised
                    smallest = leftChildIdx
            if rightChildIdx < size:
                rightChild = self.data[rightChildIdx]
                if (smallest is None and rightChild.priority < curr.priority) or (smallest is not None and rightChild.priority <  leftChild.priority ):
                    smallest = rightChildIdx
            if not smallest:   # If there's no prioritised child, stop the loop
                break
            else:   # Swap current element with the priority child    
                self.data[idx],self.data[smallest] = self.data[smallest],self.data[idx]
                idx = smallest
    
    # Time complexity: O(logn) as in worst case, we may have to traverse from the root to the leaf node
    # The height of a binary heap is logn, hence the time complexity


'''
Time complexity:
enqueue: O(logn)
dequeue: O(logn)

Space complexity: O(1)
'''



pq = PriorityQueue()

pq.enqueue('job1',3)
pq.enqueue('job2',4)
pq.enqueue('job3',1)
pq.enqueue('job4',2)
pq.enqueue('job5',1)

queue = [(v.value,v.priority) for v in pq.data]
print(queue)
deq = pq.dequeue()
print(deq.value,deq.priority)
