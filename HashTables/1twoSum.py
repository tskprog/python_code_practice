"""
Udemy
Two Sum - You are given an array of Integers and another integer targetValue. Write a function that will take these inputs and return the indices of the 2 integers in the array that add up targetValue.

Test Cases
ip = [2,7,3,-1,8],2 --> op = [2,3]
ip = [25],25 --> op = []
"""


def two_sum_brute(array,target):
    size = len(array)
    for ind1 in range(size-1):
        for ind2 in range(ind1+1,size):
            if target-array[ind1] == array[ind2]:
                return [ind1,ind2]
    return []
    

# SC=O(1)-->no auxiliary space TC = O(n^2))


def two_sum(array,target):
    num_available = {}
    for ind1 in range(len(array)):
        val1 = array[ind1]
        val2 = target-val1
        if val2 in num_available.keys():
            return [ind1,num_available[val2]]
        else:
            num_available[val1] = ind1
    return []


# SC=O(n)-->dictionary space TC = O(n))


from userInput import *

print(two_sum(inputArray(),inputInt('Enter Target Value')))