"""
Python: Monotonic Array
Question

An array is monotonic if it is either monotone increasing or monotone decreasing. An array is monotone increasing if all its elements from left to right are non-decreasing. An array is monotone decreasing if all  its elements from left to right are non-increasing. Given an integer array return true if the given array is monotonic, or false otherwise.

Test Cases
[0,1,2,3,3];[4,3,2,1,0,0];[1];[];[3,3,3]; --> True
[3,5,2] --> False
"""

def monotonic_array(array):
    size = len(array)
    if size < 3:
        return True
    else:
        mi,md = 1,1
        for i in range(size-1):
            if array[i] <= array[i+1]:
                mi += 1
            elif array[i] >= array[i+1]:
                md += 1
        if mi == size or md == size:
            return True
    return False


def monotonic_array_method2(array):
    size = len(array)
    if size < 3:
        return True
    beg = array[0]
    end = array[-1]
    if beg == end:
        for i in range(size-1):
            if array(i) != array[i+1]:
                return False
    elif beg < end:
        for i in range(size-1):
            if array[i] > array[i+1]:
                return False
    else:
        for i in range(size-1):
            if array[i] < array[i+1]:
                return False
    return True

# SC=O(1)no extra space TC = O(n) iterating only once

from userInput import *

print(monotonic_array_method2(inputArray()))