"""
Udemy
Group Anagrams - Given an array of strings consisting of lower case English letters, group the anagrams together. You can return the answer in any order. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.

Test Cases
ip = [arc,car,cat,act.atc,abc] --> op = [[arc,car],[cat,act,atc],[abc]]
ip = [abc] --> op = [[abc]]
"""


def group_anagrams1(strings):
    words = {}
    for word in strings:
        order = sum(ord(c) for c in word)
        if order in words:
            words[order].append(word)
        else:
            words[order] = [word]
    return list(words.values())


def group_anagrams(strings):
    words = {}
    sort_strings = [''.join(sorted(word)) for word in strings]
    size = len(strings)
    for i in range(size):
        if sort_strings[i] in words:
            words[sort_strings[i]].append(strings[i])
        else:
            words[sort_strings[i]] = [strings[i]]
    return list(words.values())


# TC = O(s*nlogn))-->nlogn for sorting and s is number of words in strings; iterating is ignored as s<<s*nlogn
# SC = O(s*n) --> sn for sort_strings, 2sn for dict,sn for output list = 4(s*n)~s*n


from userInput import *

print(group_anagrams1(inputStringArray()))
print(group_anagrams(inputStringArray()))