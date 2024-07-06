"""
Fibonacci - In the Fibonacci sequence, each subsequent term is obtained by adding the preceding 2 terms. This is true for all the numbers except the first 2 numbers of the Fibonacci series as they do not have 2 preceding numbers. The first 2 terms in the Fibonacci series is 0 and 1. F(n) = F(n-1)+F(n-2) for n>1. Write a function that finds F(n) given n where n is an integer greater than equal to 0. For the first term n = 0. (You can assume that no negative value will be passed. )

Test Cases
ip = 0 --> op = 0
ip = 8 --> op = 21
"""


def fibonacci_recursive(n):
    if n < 2:
        return n
    else:
        return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)


# SC=O(n)-->no auxiliary space but there are >n calls in the call stack TC = O(2^n))-->2^(n-2)x-x~2^n 


def fibonacci_recursive_store(n):
    fib_no = {0:0,1:1}
    if n in fib_no:
        return fib_no[n]
    else:
        fib_no[n] = fibonacci_recursive_store(n-1) + fibonacci_recursive_store(n-2)
        return fib_no[n]


# SC=O(n)-->2n~n where n is for HT and n is for call stack TC = O(n))--> calculating fib for n numbers only


def fibonacci_iterative(n):
    if n<2:
        return n
    prev = 0
    curr = 1
    count = 1
    while count < n:
        next = prev + curr
        prev = curr
        curr = next
        count += 1
    return curr


# SC = O(1) no auxiliary space; TC=O(n) as there are n iterations

from userInput import *

print(fibonacci_recursive(inputInt('Enter a number')))
print(fibonacci_recursive_store(inputInt('Enter a number')))
print(fibonacci_iterative(inputInt('Enter a number')))