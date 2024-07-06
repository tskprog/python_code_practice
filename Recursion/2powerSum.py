"""
Power Sum - Let’s define a peculiar type of array in which each element is either an integer or another peculiar array. Assume that a peculiar array is never empty. Write a function that will take a peculiar array as its input and find the sum of its elements. If an array is an element in the peculiar array you have to convert it to it’s equivalent value so that you can sum it with the other elements. Equivalent value of an array is the sum of its elements raised to the number which represents how far nested it is.

Test Cases
ip = [2,3,[4,1,2]] --> op = 2+3+ (4+1+2)^2 = 54
ip = [1,2,[7,[3,4],2]] --> op = 1 + 2 +( 7+(3+4)^3+2)^2 = 123907
ip = [1,2,[3,4],[[2]]] --> op = 1+2+49+((2)^3)^2 = 116
"""


def power_sum(array,power=1):
    sum = 0
    for i in array:
        if type(i) == int:
            sum += i
        else:
            sum += power_sum(i,power+1)
    return sum**power


# SC=O(d)-->no auxiliary space only recursive calls so max depth in the input i.e., 3in tc3 TC = O(n)) where n is total number of elements in every list and number of lists i.e., 8 in tc3

from userInput import *

inputs = [[2,3,[4,1,2]],[1,2,[7,[3,4],2]],[1,2,[3,4],[[2]]]]
for i in inputs:
    print(power_sum(i))