"""
Question

You are given an array of Integers in which each subsequent value is not less than the previous value. Write a function that takes this array as an input and returns a new array with the squares of each number sorted in ascending order.

Test Case:
    Input = [-4,-2,0,5,6]
    Output = [0,4,16,25,36]
"""

def sorted_squared_brute(array):
    squared = []
    for i in array:
        squared.append(i*i)
    return sorted(squared)
# SC=O(n) TC = O(nlogn) for sorting brute


def sorted_squared(array):
    l = len(array)
    squared = [0] * l
    i = 0
    j = l-1
    for k in range(l-1,-1,-1):
        i_sq = array[i] ** 2
        j_sq = array[j] ** 2
        if i_sq < j_sq:
            squared[k] = j_sq
            j -= 1
        else:
            squared[k] = i_sq
            i += 1
    return squared

# SC=O(n) TC = O(n) for sorting with above approach


from userInput import *

print(sorted_squared(inputArray()))