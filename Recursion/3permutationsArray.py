"""
Udemy
Permutations - Given an array of distinct integers, return all the possible permutations. You can return the answer in any order.

Test Cases
ip = [1] --> op = [[1]]
ip = [1,2,3] --> op = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
ip = [] --> op = [[]]
"""


def all_permutations(nums):
    permutations = []
    size = len(nums)
    if size < 2:
        permutations.append(nums)
        return permutations
    def swap(nums,i):
        if i == size-1:
            permutations.append(nums.copy())
            return
        for j in range(i,size):
            nums[i],nums[j] = nums[j],nums[i]
            swap(nums,i+1)
            nums[i],nums[j] = nums[j],nums[i]
    swap(nums,0)
    return permutations



# SC=O(n*n!)-->n!lists of n sized lists TC = O(n*n!))-->(n*n!)+(n*n!-n!)*1 = 2(n*n!)-n! ~ n*n!
"""
n*n! swap calls are happening
for each call(two types can heppen): either copy which takes o(n) or swaps that takes o(1) as per if condition
for n!(total permutations) calls o(n) and for remaining (n-1)*n! calls o(1) 
n iterations were required to get 1 element;
"""

def function_name_method2(args):
    # definition
    pass


# SC=O(1)-->no auxiliary space TC = O(n))-->2n~n


from userInput import *

print(all_permutations(inputArray()))