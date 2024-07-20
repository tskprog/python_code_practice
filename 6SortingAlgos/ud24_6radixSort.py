"""
Udemy
Radix Sort Algorithm-You are given an array of non-negative integers. Write a function that will take this array as input and return the sorted array using Radix sort.

Test Cases
ip = [1,5,6,3,4] --> op = [1,3,4,5,6]
ip = [10,6,5,6,5,7] --> op = [5,5,6,6,7,10]
"""

def radix_sort(array):
    size = len(array)
    if size < 2:
        return array
    high = max(array)
    digits = math.floor(math.log10(high))+1 
    # len(str(high))
    # counting sort needs to be performed d times
    for p in range(digits):
        counting_sort(array,p)
    return array

def counting_sort(array, place):
    size = len(array)
    freq = [0] * 10
    sort_nums = [0 for i in range(size)]
    digit_place = 10**place
    for num in array:
        digit = math.floor(num/digit_place)%10
        freq[digit] += 1
    for i in range(1,10):
        freq[i] += freq[i-1]
    for j in range(size-1,-1,-1):
        digit = (array[j]//digit_place) %10
        freq[digit] -= 1
        sort_nums[freq[digit]] = array[j]
    array[:] = sort_nums[:]
    return array


# SC=O(n+k)-->n is output array and k is for frequency array of length as base in counting sort TC = O(d*(n+k)))-->d is max number of digits in input array and for each digit, a counting sort performed wth 3n+2k ops


from userInput import *
import math

print(radix_sort(inputArray()))
# print(math.floor(math.log10(99)))
# print(math.floor(241/(10**0))%10)