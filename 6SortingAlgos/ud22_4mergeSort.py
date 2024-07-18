"""
Udemy
Merge Sort Algorithm-You are given an array of integers. Write a function that will take this array as input and return the sorted array using Merge sort.

Test Cases
ip = [1,5,6,3,4] --> op = [1,3,4,5,6]
ip = [10,6,5,6,5,7] --> op = [5,5,6,6,7,10]
"""


def merge_sort(array):
    def merge_arrays(nums1,nums2):
        size1 = len(nums1)
        size2 = len(nums2)
        i,j = 0,0
        merged = []
        while i < size1 and j < size2:
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        while i < size1:
            merged.append(nums1[i])
            i += 1
        while j < size2:
            merged.append(nums2[j])
            j += 1
        return merged
    
    def sort_array(array):
        size = len(array)
        if size < 2:
            return array
        else:
            mid = size//2
            nums1 = sort_array(array[0:mid])
            nums2 = sort_array(array[mid:size])
            return merge_arrays(nums1,nums2)
    return sort_array(array)
    

# SC=O(n)-->O(n+logn)~O(n) where n is for new array and logn is for call stack; TC = O(nlogn))-->where n ops will be done for each level and number of levels are logn(recursive calls) so n times logn is time complexity


from userInput import *

print(merge_sort(inputArray()))