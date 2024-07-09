"""
Udemy
Binary Search - Given an array of integers which is sorted in ascending order, and a target integer, write a function to search for whether the target integer is there in the given array. If it is there then return its index. Otherwise, return -1. You must write an algorithm with O(log n) runtime complexity.

Test Cases
ip = [1,3,6,8,9];8 --> op = 3
ip = [1,2,4,5,7,10];3 --> op = -1
"""


def binary_search_iterative(array,target):
    low = 0
    high = len(array) - 1
    while low<=high:
        mid = (low+high)//2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return -1


# SC=O(1)-->no auxiliary space TC = O(logn))

def binary_search_recursive(array,target):
    low = 0
    high = len(array) - 1
    def search_num(array,target,low,high):
        if low > high:
            return -1
        mid = (low+high)//2
        if array[mid] == target:
            return mid
        elif target > array[mid]:
            return search_num(array,target,mid+1,high)
        else:
            return search_num(array,target,low,mid-1)
    return search_num(array,target,low,high)


# SC=O(logn)-->call stack,logn calls TC = O(logn))


from userInput import *

print(binary_search_iterative(inputArray(),inputInt('Enter target number')))
print(binary_search_recursive(inputArray(),inputInt('Enter target number')))