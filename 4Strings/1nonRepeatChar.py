"""
Udemy
Non repeating character - You are given a string consisting of only lower case and upper-case English Alphabets and integers 0 to 9. Write a function that will take this string as Input and return the index of the first character that is non-repeating.

Test Cases
ip = 'structure' --> op = 0
ip = '','abab' --> op = None
"""


def non_repeating_char1(str):
    chars = []
    for i in str:
        if i not in chars:
            chars.append(i)
        else:
            chars.remove(i)
    if chars:
        return str.index(chars[0])
    else:
        return None


# SC=O(1)-->list of chars but bounded <O(62) TC = O(n))


def non_repeating_char(str):
    chars = {}
    for i in str:
        if i not in chars:
            chars[i] = 1
        else:
            chars[i] += 1
    for i in range(len(str)):
        if chars[str[i]] == 1:
            return i
    return None
            
# SC=O(1)-->Even there is hashtable, input string is bounded to a-zA-Z0-9 which is <62=O(62)~O(1) TC = O(n))-->2n~n


from userInput import *

print(non_repeating_char(inputStr('Enter string')))