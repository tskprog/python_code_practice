"""
Udemy
Question :Reverse Polish Notation
Evaluate the value of an arithmetic expression in Reverse Polish Notation(See example).
Valid operators are +, -, *, and /.
Note that division between two integers should truncate toward zero. It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation. The Input is an array of strings where each element is either a valid operator or an integer. E.g.[“1”,”2”,”+”]
Test Cases
ip = ['1','2','+']  --> op = 3
ip = ['4','3','/'] --> op = 1
"""

def rev_pol_not(tokens):
    stack = []
    ops = {'+':lambda n1,n2:n1+n2,'-':lambda n1,n2:n1-n2,'*':lambda n1,n2:n1*n2,'/':lambda n1,n2:int(n1/n2)}
    for i in tokens:
        if i in ops:
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(ops[i](num1,num2))
        else:
            stack.append(int(i))
    return stack.pop()


# We are iterating through all the tokens once, hence the time complexity is O(n), where n is the number of tokens.
# We are using a stack to store the operands, hence the auxiliary space complexity is O(n), where n is the number of operands in tokens.

n = int(input(("Enter number of elements:")))
tokens = list(map(str, input(f'Enter {n} elements separating with space : ').strip().split()))[:n]
print(rev_pol_not(tokens))