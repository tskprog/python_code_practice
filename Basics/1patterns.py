"""
This contains various patterns and list is as follows
1. Rectangular star pattern
2. 
"""

  
def pattern1(n):
    print('entered')
    for i in range(n):
        for j in range(n):
            print('*',end='')
        print()

pattern = int(input('Enter Pattern number:'))
n = int(input('Enter number of Lines:'))

match pattern:
    case 1:
        pattern1(n)


