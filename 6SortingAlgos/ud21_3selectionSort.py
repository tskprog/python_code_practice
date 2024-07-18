"""
Udemy
Selection Sort Algorithm-You are given an array of integers. Write a function that will take this array as input and return the sorted array using Selection sort.

Test Cases
ip = [1,5,6,3,4] --> op = [1,3,4,5,6]
ip = [10,6,5,6,5,7] --> op = [5,5,6,6,7,10]
"""


def selection_sort(nums):
    size = len(nums)
    for i in range(size):
        smallest = i
        for j in range(i+1,size):
            if nums[smallest] > nums[j]:
                smallest = j
        if i != smallest:
            nums[i],nums[smallest] = nums[smallest],nums[i]
        print(i,nums)
    return nums


# SC=O(1)-->no auxiliary space TC = O(n^2))-->n(n-1)/2

from userInput import *

print(selection_sort(inputArray()))