"""
Udemy
Longest Unique char Substring - Given a string s, find the length of the longest substring without repeating characters.

Test Cases
ip = codingcode --> op = 7
ip = pppp --> op = 1
"""


def max_unique_length(str):
    seen = {}
    start = 0
    long = 0
    for i in range(len(str)):
        if str[i] in seen and start < seen[str[i]]+1:
            start = seen[str[i]]+1
        seen[str[i]] = i
        long = max(long,i-start+1)
        # print(i,seen,long,start)
    return long
        

# SC=O(min(n,m))-->hash table of length as count of unique chars TC = O(n))-->traversing string and doing constant ops


from userInput import *

print(max_unique_length(inputStr('Enter string')))