"""
Udemy
Power Set - Given an integer array of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets. Return the solution in any order.

Test Cases
ip = [1] --> op = [[],[1]]
ip = [1,2,3] --> op = [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
ip = [] --> op = [[]]
"""


def power_set (nums):
    powerset = []
    size = len(nums)
    def add_sets(i,nums,subset):
        if i == size:
            powerset.append(subset.copy())
            return
        add_sets(i+1,nums,subset)
        subset.append(nums[i])
        add_sets(i+1,nums,subset)
        subset.pop()
    add_sets(0,nums,[])
    return powerset


# SC=O((2^n)*n)-->no auxiliary space TC = O((2^n)*n))-->(2^n)*(n/2)
# Total pushes ranges from 0 to n ---> avg n/2


from userInput import *

print(power_set(inputArray()))