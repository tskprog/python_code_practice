"""
Udemy
Bubble Sort Algorithm - You are given an array of integers. Write a function that will take this array as input and return the sorted array using Bubble sort.

Test Cases
ip = [1,5,6,3,4] --> op = [1,3,4,5,6]
ip = [10,6,5,6,5,7] --> op = [5,5,6,6,7,10]
"""


def bubble_sort(array):
    size = len(array)
    for j in range(size-1):
        i = 0
        while i < size-j-1:
            if array[i] > array[i+1]:
                array[i],array[i+1] = array[i+1],array[i]
            i += 1
    return array


# SC=O(1)-->no auxiliary space TC = O(n^2))-->n swaps for 1 element sort


def bubble_sort_2(array):
    size = len(array)
    sorted = False
    sort_n = 0
    while not sorted:
        sorted = True
        for i in range(size-1-sort_n):
            if array[i] > array[i+1]:
                array[i],array[i+1] = array[i+1],array[i]
                sorted = False
        sort_n += 1
    return array


# SC=O(1)-->no auxiliary space TC = O(n^2))-->n swaps for 1 element sort


from userInput import *

print(bubble_sort(inputArray()))
print(bubble_sort_2(inputArray()))