"""
Udemy
Insertion Sort Algorithm - You are given an array of integers. Write a function that will take this array as input and return the sorted array using Insertion sort.

Test Cases
ip = [1,5,6,3,4] --> op = [1,3,4,5,6]
ip = [10,6,5,6,5,7] --> op = [5,5,6,6,7,10]
"""


def insertion_sort(array):
    size = len(array)
    for i in range(1,size):
        j = i-1
        temp = array[i]
        while j >= 0 and array[j] > temp:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = temp
    return array


# SC=O(1)-->no auxiliary space TC = O(n^2))-->1+2+3+4+...+n-1 operations


from userInput import *

print(insertion_sort(inputArray()))