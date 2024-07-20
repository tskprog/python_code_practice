"""
Udemy
Quick Sort Algorithm -You are given an array of integers. Write a function that will take this array as input and return the sorted array using Quick sort.

Test Cases
ip = [1,5,6,3,4] --> op = [1,3,4,5,6]
ip = [10,6,5,6,5,7] --> op = [5,5,6,6,7,10]
"""


def swap(array, i, j):
    array[i],array[j] = array[j],array[i]


def partition(array, start=0, end=None):
    mid = (start+end)//2
    swap(array,start,mid)
    pivot = array[start]
    left = start+1
    right = end
    while left <= right:
        while left <= right and array[left] <= pivot:
            left += 1
        while left <= right and array[right] > pivot:
            right -= 1
        if left<right:
            swap(array,left,right)
    swap(array,start,right)
    return right
    

def quick_sort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1
    while start < end:
        pivotind = partition(array,start,end)
        if pivotind - start < end - pivotind:
            quick_sort(array,start,pivotind-1)
            start = pivotind + 1
        else:
            quick_sort(array,pivotind+1,end)
            end = pivotind - 1
    return array


# SC=O(logn)-->no auxiliary space and call stack is logn 
# TC = O(nlogn))-->logn calls and n comparisions in each call which is best and worst case is O(n^2) when pivot is selected as extreme end instead of median and input is sorted


from userInput import *

print(quick_sort(inputArray()))