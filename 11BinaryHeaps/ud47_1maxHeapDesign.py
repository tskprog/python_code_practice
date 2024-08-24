"""
Udemy
Question :Construct BST
Design a max heap data structure class that supports the following:

1. Building a max heap from an input array
2. Insert integers into the heap. -->BubbleUp
3.Remove a value. This method should remove the root which is max value in this case so this can also called as extractMax. --> BubbleDown
4.Peeking heaps max/root. If the value is found it should return the node with the value else return false.
"""


class MaxBinaryHeap:
    def __init__(self):
        self.heap = []
    
    
    def buildHeap(self,array):
        size = len(array)
        lastParent = (size//2)-1
        for i in range(lastParent,-1,-1):  # From last parent to root
            self.bubbleDown(array,i)
        self.heap = array
        return self
    
    def bubbleDown(self,array,idx):
        size = len(array)
        curr = array[idx]
        while True:
            leftChildIdx = (2*idx)+1
            rightChildIdx = 2*idx+2
            largest = None
            if leftChildIdx < size:
                leftChild = array[leftChildIdx]
                if leftChild > curr:   # If it's larger than current element, it could be the largest
                    largest = leftChildIdx
            if rightChildIdx < size:
                rightChild = array[rightChildIdx]
                if (not largest and rightChild > curr) or (largest and rightChild >  leftChild ):
                    largest = rightChildIdx
            if not largest:   # If there's no larger child, stop the loop
                break
            else:   # Swap current element with the largest child    
                array[idx],array[largest] = array[largest],array[idx]
                idx = largest
    
    def extractMax(self):
        maxValue = self.heap[0]
        last = self.heap.pop()
        if len(self.heap) > 0:
            self.heap[0] = last
            self.bubbleDown(self.heap,0)
        return maxValue
    
    def insertValue(self,value):
        self.heap.append(value)
        self.bubbleUp()
        return self
    
    def bubbleUp(self):
        idx = len(self.heap)-1
        val = self.heap[idx]
        while idx > 0:
            parentIdx = (idx-1)//2
            parentVal = self.heap[parentIdx]
            if val <= parentVal:
                break
            # Swap parent with current value
            self.heap[idx],self.heap[parentIdx] = self.heap[parentIdx],self.heap[idx]
            idx = parentIdx
        
    def peek(self):
        return self.heap[0]


'''
Space complexity: The space complexity for all these functions is O(1)

Time complexity:

buildHeap: This function operates in O(n) time complexity because it's performing a constant amount of work (i.e., a constant number of operations) for n elements of the array.

bubbleDown: This function operates in O(log n) time complexity because, in the worst case, it needs to move an element from the root to the leaf of the heap.

extractMax: This function operates in O(log n) time complexity because it needs to bubble down the root element to its correct position.

insert: This function operates in O(log n) time complexity because it needs to bubble up the inserted element to its correct position.

bubbleUp: This function operates in O(log n) time complexity because, in the worst case, it needs to move an element from the leaf to the root of the heap.

peek: This function operates in O(1) time complexity because it simply returns the first element of the array.
'''



heap = MaxBinaryHeap()
case1 = [4,7,3,0,9,3,2,6]
heap.buildHeap(case1)
print('Built Heap is ',heap.heap)
max_val = heap.extractMax()
print(max_val,' is max val and latest heap is ',heap.heap)
heap.insertValue(20)
print('Inserted and latest heap is ',heap.heap)
peek = heap.peek()
print('peek is ',peek)