"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Test Cases
ip = [1,2,3,4,5]
k = 2 --> op = [4,5,1,2,3]
k = 8 --> op = [3,4,5,1,2]
"""


def rotate_array(array,k):
    size = len(array)
    if size == 0 or k%size == 0:
        return array
    else:
        k = k%size
        for i in range(k):
            array.insert(0,array[-1])
            array.pop()
    return array


def reverse(array,start,end):
    while start < end:
        array[start],array[end] = array[end],array[start]
        start += 1
        end -= 1
    return array

def rotate_array_method2(array,k):
    size = len(array)
    if size == 0 or k%size == 0:
        return array
    else:
        k = k%size
        array = reverse(array,0,size-1)
        array = reverse(array,0,k-1)
        array = reverse(array,k,size-1)
    return array

# SC=O(1)-->no auxiliary space TC = O(n))-->2n~n


from userInput import *

print(rotate_array_method2(inputArray(),6))