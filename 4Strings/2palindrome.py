"""
Udemy
Palindrome-You are given a string. Write a function to check whether the string is a palindrome or not.

Test Cases
ip = [1,5,6,3,4] --> op = [12]
ip = [10,6,5,6,5,7] --> op = [35]
"""


'''
In Python Strings are immutable.
Method1:
    Create a new string in reverse order. Here new string will be formed by traversing the string and appending that leads to create a new string everytime. Compare strings and return
    # SC=O(n)-->new string TC = O(n^2))-->append takes O(n) and it repeats for n times
Method2:
    Create a new array by traversing string in reverse order. Use join operation(''.join(list)) to make a string from array and compare.
    Pushing to array is constant time
    # SC=O(nn-->new array TC = O(n))-->traversing only once and using join op
'''

# optimal method 3: two pointer
def is_palindrome(str):
    size = len(str)
    left = 0
    right = size-1
    while left<right:
        if str[left] != str[right]:
            return False
        left += 1
        right -= 1
    return True
        

# SC=O(1)-->no auxiliary space TC = O(n))

from userInput import *

print(is_palindrome(inputStr('Enter string')))