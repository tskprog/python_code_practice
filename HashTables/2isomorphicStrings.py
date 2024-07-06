"""
Isomorphic Strings - Given two strings s and t, determine if they are isomorphic. Two strings s and t are isomorphic if the characters in s can be replaced to get t. All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself. s and t consist of any valid ascii character.

Test Cases
ip = abacus,rirfgs --> op = True
ip = abc,pq --> op = False
ip = ababr,pqrqq --> op = False
"""


def isomorphic_strings(s, t):
    char_map = {}
    size = len(s)
    if len(t) == size:
        for i in range(size):
            if s[i] in char_map:
                if t[i] != char_map[s[i]]:
                    return False
            else:
                char_map[s[i]] = t[i]
        return True
    return False



# SC=O(1)-->as input chars are valid ascii and will be fixed(n*128) TC = O(n))


from userInput import *

print(isomorphic_strings(inputStr('Enter 1st string'),inputStr('Enter 2nd string')))