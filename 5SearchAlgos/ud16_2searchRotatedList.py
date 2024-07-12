"""
Udemy
Search in Rotated Sorted array- You are given an integer array nums sorted in ascending order (with distinct values). Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).  For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2]. Given an integer target, return the index of target if it is in the array, else return -1. You must write an algorithm with O(log n) runtime complexity.

Test Cases
ip = [5,6,3,4];6 --> op = [1]
ip = [10,5,7];7 --> op = [2]
"""


def search_rotated_sorted_array(nums,target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        elif nums[left] <= nums[mid]:
            # left part is sorted
            if nums[left] <= target < nums[mid]:
                # search left part
                right = mid-1
            else:
                # search right part
                left = mid+1
        elif nums[mid] <= target < nums[right]: 
            left = mid+1
        else:
            right = mid-1
    return -1
            

# SC=O(1)-->no auxiliary space TC = O(logn))

from userInput import *

print(search_rotated_sorted_array(inputArray(),inputInt('Enter the target')))