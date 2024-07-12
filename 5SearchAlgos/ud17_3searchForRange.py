"""
Udemy
Find First and Last Position of Element in Sorted Array-You are given an array of integers sorted in non-decreasing order, find the starting and ending position of a given target value. If target is not found in the array, return [-1, -1]. You must write an algorithm with O(log n) runtime complexity.

Test Cases
ip = [1,5,6,6,8];6 --> op = [2,3]
ip = [1,4,7,9,10];9 --> op = [2,2]
ip = [1,2,3,4,5];6 --> op = [-1,-1]
"""


def search_for_range_iterative(array,target):
    pos = [-1,-1]
    size = len(array)
    left = 0
    right = size-1
    def get_left_extreme(array,target,left,right):
        while left <= right:
            mid = (left+right)//2
            if array[mid] == target:
                if mid == 0:
                    return mid
                elif array[mid-1] == target:
                    right = mid-1
                else:
                    return mid
            elif array[mid] <= target :
                left = mid+1
            else:
                right = mid-1
        return -1
    
    def get_right_extreme(array,target,left,right):
        while left <= right:
            mid = (left+right)//2
            if array[mid] == target:
                if mid == size-1:
                    return mid
                elif array[mid+1] == target:
                    left = mid+1
                else:
                    return mid
            elif array[mid] <= target :
                left = mid+1
            else:
                right = mid-1
        return -1
    pos = [get_left_extreme(array,target,left,right),get_right_extreme(array,target,left,right)]
    return pos
                
                
# SC=O(1)-->no auxiliary space TC = O(logn))-->2logn~logn


def search_for_range_recursive(array,target):
    pos = [-1,-1]
    size = len(array)
    left = 0
    right = size-1
    
    def get_left_extreme(array,target,left,right,pos):
        if left>right:
            return
        mid = (left+right)//2
        if array[mid] == target:
            if mid == 0:
                pos[0] = mid
            elif array[mid-1] == target:
                get_left_extreme(array,target,left,mid-1,pos)
            else:
                pos[0] = mid
        elif array[mid] <= target:
            get_left_extreme(array,target,mid+1,right,pos)
        else:
            get_left_extreme(array,target,left,mid-1,pos)
    
    def get_right_extreme(array,target,left,right,pos):
        if left>right:
            return
        mid = (left+right)//2
        if array[mid] == target:
            if mid == size-1:
                pos[1] = mid
            elif array[mid+1] == target:
                get_right_extreme(array,target,mid+1,right,pos)
            else:
                pos[1] = mid
        elif array[mid] <= target:
            get_right_extreme(array,target,mid+1,right,pos)
        else:
            get_right_extreme(array,target,left,mid-1,pos)
    
    get_left_extreme(array,target,left,right,pos)
    get_right_extreme(array,target,left,right,pos)
    return pos
                
# SC=O(logn)-->no auxiliary space but call stack is of 2logn TC = O(logn))-->2logn~logn

from userInput import *

print(search_for_range_iterative(inputArray(),inputInt('Enter target')))
print(search_for_range_recursive(inputArray(),inputInt('Enter target')))