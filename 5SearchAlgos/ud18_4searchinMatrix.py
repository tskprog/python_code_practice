"""
Udemy
Search in 2D Array-Write an efficient algorithm that searches for a value target in an m x n integer matrix. This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
If the value is there in the matrix return true, else false.

Test Cases
ip = [[1,2,3],[4,5,6],[7,8,9]];5 --> op = True
ip = [[34,37],[43,46],[78,90]];99 --> op = False
"""


def search_in_matrix(matrix,target):
    def search_in_row(row,target):
        left = 0
        right = len(row) - 1
        while left <= right:
            mid = (left+right)//2
            if row[mid] == target:
                return True
            elif row[mid] <= target:
                left = mid+1
            else:
                right = mid-1
        return False
    rows = len(matrix)
    for i in range(rows):
        if search_in_row(matrix[i],target):
            return True
    return False
    

# SC=O(1)-->no auxiliary space TC = O(m*logn))-->m is number of rows,nlogn is for binary search for every row where n is size of row


def search_in_matrix_2(matrix,target):
    def search_in_row(row,target):
        left = 0
        right = len(row) - 1
        while left <= right:
            mid = (left+right)//2
            if row[mid] == target:
                return True
            elif row[mid] <= target:
                left = mid+1
            else:
                right = mid-1
        return False
    rows = len(matrix)
    top = 0
    bottom = rows-1
    while top<=bottom:
        mid = (top+bottom)//2
        if matrix[mid][0] <= target <= matrix[mid][-1]:
            return search_in_row(matrix[mid],target)
        elif matrix[mid][0] > target:
            bottom = mid-1
        else:
            top = mid+1
    return False
    

# SC=O(1)-->no auxiliary space TC = O(logmn))-->logm+logn where we used binary search for fionding both rows and columns.


from userInput import *

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(search_in_matrix(matrix,inputInt('Enter the target')))
print(search_in_matrix_2(matrix,inputInt('Enter the target')))