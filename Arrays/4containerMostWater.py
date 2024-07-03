"""
Container with most Water - You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]). Find two lines that together with the x-axis form a container, such that the container contains the most water(depth is constant across containers). Return the area(that the 2 lines and the X axis make) of container which can store the max amount of water. Notice that you may not slant the container.

Test Cases
ip = [1,5,6,3,4] --> op = [12]
ip = [10,6,5,6,5,7] --> op = [35]
"""


def max_area(array):
    size = len(array)
    max_area = 0
    for i in range(size-1):
        for j in range(i,size):
            area = min(array[i],array[j]) * (j-i)
            max_area = max(area,max_area)
    return max_area

# SC=O(1)-->no auxiliary space TC = O(n^2)) brute

def max_area_method2(array):
    size = len(array)
    max_area = 0
    left = 0
    right = size-1
    while left < right:
        area = min(array[left],array[right]) * (right-left)
        max_area = max(area,max_area)
        if array[left] < array[right]:
            left += 1
        else:
            right -= 1
    return max_area

# SC=O(1)-->no auxiliary space TC = O(n))-->2n~n


from userInput import *

print(max_area_method2(inputArray()))