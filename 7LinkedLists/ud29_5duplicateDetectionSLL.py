"""
Udemy
Find duplicate number-Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive. There is only one repeated number in nums, return this repeated number. You must solve the problem without modifying the array nums and uses only constant extra space.

Test Cases
ip = [2,3,1,4,2] --> op = 2
ip = [1,1] --> op = 1

"""


# Floyd's Hare & Tortoise Algorithm
def getDuplicate(nums):
    hare = 0
    tortoise = 0
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if hare == tortoise:
            curr = 0
            while curr != tortoise:
                tortoise = nums[tortoise]
                curr = nums[curr]
            return tortoise

# The while loop runs at most 'n' times where 'n' is the number of elements in the array. Thus, the time complexity is O(n).
# We only use a constant amount of memory to store variables 'hare', 'tortoise', and 'pointer'. Therefore, the space complexity is O(1).


from userInput import *

array = inputArray()
print(f'Repeated element in {array} is {getDuplicate(array)}')
